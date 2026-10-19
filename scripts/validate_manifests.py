"""Validate source manifests against JSON Schema and cross-file contracts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = {
    "skill": "skill.schema.json",
    "agent": "agent.schema.json",
    "suite": "suite.schema.json",
    "selection-matrix": "selection-matrix.schema.json",
    "pack": "pack.schema.json",
    "package": "package.schema.json",
}
SEMVER = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)


class DuplicateKeyError(ValueError):
    """A YAML mapping contains a repeated key."""


class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node: yaml.MappingNode, deep: bool = False) -> dict:
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str):
                raise DuplicateKeyError("YAML mapping keys must be strings")
            if key in mapping:
                raise DuplicateKeyError(f"duplicate YAML key: {key}")
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


def load_yaml(text: str) -> Any:
    return yaml.load(text, Loader=UniqueKeyLoader)


def load_frontmatter(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    header, separator, _ = text[4:].partition("\n---\n")
    if not separator:
        raise ValueError("unterminated frontmatter")
    data = load_yaml(header)
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data


def unknown_fields(
    data: Any, schema: dict[str, Any], location: str, warnings: list[str],
) -> None:
    if isinstance(data, dict):
        properties = schema.get("properties", {})
        patterns = schema.get("patternProperties", {})
        additional = schema.get("additionalProperties")
        for key, value in data.items():
            child_schema = properties.get(key)
            if child_schema is None:
                child_schema = next(
                    (
                        pattern_schema
                        for pattern, pattern_schema in patterns.items()
                        if re.search(pattern, key)
                    ),
                    None,
                )
            if child_schema is None:
                if isinstance(additional, dict):
                    child_schema = additional
                elif properties and additional is not False:
                    warnings.append(f"{location}: unknown field {key!r} (ignored)")
            if child_schema is not None:
                unknown_fields(value, child_schema, f"{location}.{key}", warnings)
    elif isinstance(data, list) and isinstance(schema.get("items"), dict):
        for index, value in enumerate(data):
            unknown_fields(value, schema["items"], f"{location}[{index}]", warnings)


def safe_relative_file(base: Path, relative: str) -> bool:
    candidate = (base / relative).resolve()
    return candidate.is_relative_to(base.resolve()) and candidate.is_file()


def validate_repository(root: Path) -> tuple[list[str], list[str]]:
    root = root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    schemas: dict[str, dict[str, Any]] = {}
    for kind, filename in SCHEMAS.items():
        path = root / "schemas" / filename
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
        except (OSError, json.JSONDecodeError, SchemaError) as error:
            errors.append(f"{path}: invalid JSON Schema: {error}")
            continue
        schemas[kind] = schema

    if len(schemas) != len(SCHEMAS):
        return errors, warnings

    manifests: dict[str, list[tuple[Path, dict[str, Any]]]] = {
        kind: [] for kind in SCHEMAS
    }

    def validate_document(kind: str, path: Path, data: Any) -> None:
        schema = schemas[kind]
        document_errors = list(Draft202012Validator(schema).iter_errors(data))
        for error in document_errors:
            json_path = ".".join(str(part) for part in error.absolute_path)
            location = f"{path}:{json_path}" if json_path else str(path)
            errors.append(f"{location}: {error.message}")
        unknown_fields(data, schema, str(path), warnings)
        if isinstance(data, dict) and not document_errors:
            manifests[kind].append((path, data))
            schema_version = data.get("schema_version")
            if schema_version is not None:
                match = SEMVER.fullmatch(schema_version) if isinstance(schema_version, str) else None
                if match and match.group(1) != "1":
                    errors.append(
                        f"{path}: unsupported schema_version {schema_version!r}; "
                        "this validator supports schema major version 1"
                    )

    def load_document(kind: str, path: Path, text: str | None = None) -> None:
        try:
            data = load_yaml(text if text is not None else path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError, DuplicateKeyError, ValueError) as error:
            errors.append(f"{path}: invalid YAML: {error}")
            return
        validate_document(kind, path, data)

    for path in sorted((root / "src" / "suites").glob("*.yaml")):
        load_document("suite", path)
    for path in sorted((root / "src" / "packages").glob("*.yaml")):
        load_document("package", path)

    for path in sorted((root / "src" / "agents").rglob("agent.yaml")):
        load_document("agent", path)
    for path in sorted((root / "src").rglob("selection-matrix.yaml")):
        load_document("selection-matrix", path)
    for path in sorted((root / "src").rglob("pack.yaml")):
        load_document("pack", path)

    definitions: dict[str, dict[str, set[str]]] = {
        "agents": {},
        "skills": {},
    }
    for kind in ("agents", "skills"):
        directory = root / "src" / kind
        for path in sorted(directory.rglob("*.md")):
            try:
                data = load_frontmatter(path)
            except (OSError, yaml.YAMLError, DuplicateKeyError, ValueError) as error:
                errors.append(f"{path}: invalid frontmatter: {error}")
                continue
            if data is None:
                continue
            if kind == "skills":
                validate_document("skill", path, data)
            name = data.get("name")
            if isinstance(name, str):
                definitions[kind].setdefault(name, set()).add(str(path))
                expected_name = path.parent.name if path.name == "SKILL.md" else path.stem
                if name != expected_name:
                    errors.append(
                        f"{path}: name {name!r} must match {expected_name!r}"
                    )

    for kind, names in definitions.items():
        for name, paths in names.items():
            if len(paths) > 1:
                errors.append(
                    f"duplicate {kind[:-1]} name {name!r}: {', '.join(sorted(paths))}"
                )

    packs = {
        data.get("name"): path
        for path, data in manifests["pack"]
        if isinstance(data.get("name"), str)
    }
    for path, data in manifests["agent"]:
        name = data.get("name")
        if isinstance(name, str) and path.parent.name != name:
            errors.append(f"{path}: name {name!r} must match its containing folder")
        requires = data.get("requires")
        if not isinstance(requires, dict):
            continue
        for skill in requires.get("skills", []):
            if skill not in definitions["skills"]:
                errors.append(f"{path}: required skill {skill!r} does not exist")
        for pack in requires.get("language_packs", []):
            if pack not in packs:
                errors.append(f"{path}: required language pack {pack!r} does not exist")
        matrix = requires.get("selection_matrix")
        if isinstance(matrix, str) and not safe_relative_file(path.parent, matrix):
            errors.append(
                f"{path}: selection_matrix {matrix!r} must exist relative to the agent folder"
            )

    for path, data in manifests["suite"] + manifests["package"]:
        overlap = set(data.get("agents", ())) & set(data.get("optional_agents", ()))
        if overlap:
            errors.append(
                f"{path}: agents cannot also be optional_agents: {', '.join(sorted(overlap))}"
            )
        name = data.get("name")
        if isinstance(name, str) and name != path.stem:
            errors.append(f"{path}: name {name!r} must match the manifest filename")
        for field, definition_kind in (
            ("agents", "agents"),
            ("optional_agents", "agents"),
            ("skills", "skills"),
        ):
            for identifier in data.get(field, []):
                if identifier not in definitions[definition_kind]:
                    errors.append(
                        f"{path}: {field} entry {identifier!r} does not exist"
                    )

    packages = {path.stem: data for path, data in manifests["package"]}
    for path, data in manifests["suite"]:
        for field in ("packages", "optional_packages"):
            for package in data.get(field, []):
                if package not in packages:
                    errors.append(f"{path}: missing or invalid package {package!r}")
        both = set(data.get("packages", [])) & set(data.get("optional_packages", []))
        if both:
            errors.append(
                f"{path}: packages cannot also be optional_packages: {', '.join(sorted(both))}"
            )
    visited_packages: set[str] = set()
    active_packages: list[str] = []

    def check_package(name: str) -> None:
        if name in active_packages:
            errors.append(
                "Package dependency cycle: " + " -> ".join([*active_packages, name])
            )
            return
        if name in visited_packages:
            return
        active_packages.append(name)
        for dependency in packages[name].get("depends_on", []):
            if dependency not in packages:
                errors.append(f"Package {name!r}: missing or invalid dependency {dependency!r}")
            else:
                check_package(dependency)
        for reference in packages[name].get("references", []):
            if not isinstance(reference, str) or not safe_relative_file(root, reference):
                errors.append(
                    f"Package {name!r}: reference {reference!r} must be an existing file"
                )
        active_packages.pop()
        visited_packages.add(name)

    for name in packages:
        check_package(name)

    for path, data in manifests["selection-matrix"]:
        signals = set(data.get("context_signals", []))
        rules = data.get("rules", [])
        exclusions = data.get("exclusions", [])
        for index, rule in enumerate(rules):
            when = rule.get("when", {})
            for signal in when:
                if signal not in signals:
                    errors.append(
                        f"{path}: rules[{index}].when uses undeclared signal {signal!r}"
                    )
            for skill in rule.get("use", []) + rule.get("order", []):
                if skill not in definitions["skills"]:
                    errors.append(
                        f"{path}: rules[{index}] references unknown skill {skill!r}"
                    )
            if not set(rule.get("order", ())) <= set(rule.get("use", ())):
                errors.append(f"{path}: rules[{index}].order must contain only skills in use")
        for index, exclusion in enumerate(exclusions):
            when = exclusion.get("when", {})
            for signal in when:
                if signal not in signals:
                    errors.append(
                        f"{path}: exclusions[{index}].when uses undeclared signal {signal!r}"
                    )
            for skill in exclusion.get("exclude", []):
                if skill not in definitions["skills"]:
                    errors.append(
                        f"{path}: exclusions[{index}] references unknown skill {skill!r}"
                    )
            for rule_index, rule in enumerate(rules):
                if (
                    rule.get("mode") == "required"
                    and rule.get("when") == when
                    and set(rule.get("use", ())) & set(exclusion.get("exclude", ()))
                ):
                    conflict = sorted(
                        set(rule.get("use", ())) & set(exclusion.get("exclude", ()))
                    )
                    errors.append(
                        f"{path}: required skills {conflict} are excluded under "
                        f"the same condition (rules[{rule_index}], exclusions[{index}])"
                    )
        for skill in data.get("fallback", {}).get("use", []):
            if skill not in definitions["skills"]:
                errors.append(f"{path}: fallback references unknown skill {skill!r}")

    for path, data in manifests["pack"]:
        name = data.get("name")
        if isinstance(name, str) and path.parent.name != name:
            errors.append(f"{path}: name {name!r} must match its containing folder")
        extends = data.get("extends", {})
        for skill in extends.get("skills", []):
            if skill not in definitions["skills"]:
                errors.append(f"{path}: extends references unknown skill {skill!r}")
        for override in data.get("overrides", []):
            if override.get("skill") not in definitions["skills"]:
                errors.append(
                    f"{path}: override references unknown skill {override.get('skill')!r}"
                )
            reference = override.get("reference")
            if isinstance(reference, str) and not safe_relative_file(path.parent, reference):
                errors.append(f"{path}: override reference {reference!r} does not exist")
        provides = data.get("provides", {})
        provided_files = []
        if isinstance(provides.get("style"), str):
            provided_files.append(provides["style"])
        provided_files.extend(provides.get("templates", []))
        for filename in provided_files:
            if not safe_relative_file(path.parent, filename):
                errors.append(f"{path}: provided file {filename!r} does not exist")

    for path, data in manifests["suite"]:
        for pack in data.get("language_packs", {}).get("optional", []):
            if pack not in packs:
                errors.append(f"{path}: optional language pack {pack!r} does not exist")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    args = parser.parse_args()

    errors, warnings = validate_repository(args.root)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("Manifest schemas and cross-file references are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
