"""Resolve source dependencies and install them through a selected client adapter."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import quote

from scripts.clients import CLIENTS, DEFAULT_CLIENT, ClientAdapter, get_client
from scripts.utils import (
    NAME,
    InstallError,
    atomic_write,
    digest,
    local_link,
    markdown_links,
    metadata,
    safe_path,
)


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ".agentic-toolkit.json"
REPOSITORY = "https://github.com/amrishAK/agentic-toolkit/blob/HEAD/"
CATALOGUES = {
    "documentation-matrix.md",
    "programming-language-matrix.md",
    "skill-selection-workflow-matrix.md",
}
SEMVER = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)


def inventory(root: Path) -> dict[Path, tuple[str, str]]:
    definitions: dict[Path, tuple[str, str]] = {}
    names: set[str] = set()
    paths = sorted(
        path
        for kind in ("agents", "skills")
        for path in (root / "src" / kind).rglob("*.md")
    )
    for path in paths:
        fields = metadata(path)
        if not fields:
            continue
        kind = path.relative_to(root / "src").parts[0]
        key = kind, fields["name"]
        if key[1] in names:
            raise InstallError(f"Duplicate definition name: {key[1]}")
        names.add(key[1])
        definitions[path] = key
    return definitions


def load_suite(
    root: Path, suite: str, definitions: dict[Path, tuple[str, str]],
    optional_packages: str = "include",
) -> dict:
    """Load the canonical suite membership, never inferring it from categories."""
    if not NAME.fullmatch(suite):
        raise InstallError(f"Unknown suite: {suite!r}")
    path = root / "src" / "suites" / f"{suite}.yaml"
    if not path.is_file():
        raise InstallError(f"Unknown suite: {suite!r}; missing manifest: {path}")
    try:
        import yaml
    except ImportError as error:
        raise InstallError(
            "PyYAML is required; use your selected Python to run "
            "'-m pip install -r requirements.txt' before installing."
        ) from error

    class SuiteLoader(yaml.SafeLoader):
        def construct_mapping(self, node, deep=False):
            mapping = {}
            for key_node, value_node in node.value:
                key = self.construct_object(key_node, deep=deep)
                if not isinstance(key, str):
                    raise InstallError(f"Invalid suite manifest {path}: field names must be strings.")
                if key in mapping:
                    raise InstallError(f"Invalid suite manifest {path}: duplicate field {key!r}.")
                mapping[key] = self.construct_object(value_node, deep=deep)
            return mapping

    try:
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=SuiteLoader)
    except yaml.YAMLError as error:
        raise InstallError(f"Invalid YAML in suite manifest {path}: {error}") from error
    required = {"schema_version", "name", "version", "description"}
    if not isinstance(data, dict) or not required <= set(data):
        raise InstallError(
            f"Invalid suite manifest {path}: missing required fields "
            f"{', '.join(sorted(required - set(data) if isinstance(data, dict) else required))}."
        )
    schema_version = data["schema_version"]
    if (
        not isinstance(schema_version, str)
        or not SEMVER.fullmatch(schema_version)
        or schema_version.split(".", 1)[0] != "1"
    ):
        raise InstallError(
            f"Invalid suite manifest {path}: unsupported schema_version {schema_version!r}."
        )
    if not isinstance(data["version"], str) or not SEMVER.fullmatch(data["version"]):
        raise InstallError(f"Invalid suite manifest {path}: version must be a semver string.")
    if "agents" not in data and "packages" not in data:
        raise InstallError(f"Invalid suite manifest {path}: requires agents or packages.")
    known = required | {"agents", "skills", "optional_agents", "language_packs", "packages", "optional_packages"}
    unknown_fields = set(data) - known
    if unknown_fields:
        print(
            f"Warning: unknown suite manifest field(s) in {path}: "
            f"{', '.join(sorted(unknown_fields))}; ignored.",
            file=sys.stderr,
        )
    language_packs = data.get("language_packs")
    if language_packs is not None:
        if not isinstance(language_packs, dict):
            raise InstallError(
                f"Invalid suite manifest {path}: language_packs must be a mapping."
            )
        unknown_language_fields = set(language_packs) - {"optional"}
        if unknown_language_fields:
            print(
                f"Warning: unknown suite manifest language_packs field(s) in {path}: "
                f"{', '.join(sorted(unknown_language_fields))}; ignored.",
                file=sys.stderr,
            )
    if data["name"] != suite:
        raise InstallError(f"Invalid suite manifest {path}: name must match {suite!r}.")
    if not isinstance(data["description"], str) or not data["description"].strip():
        raise InstallError(f"Invalid suite manifest {path}: description must be a non-empty string.")
    data.setdefault("agents", [])
    data.setdefault("skills", [])
    data.setdefault("optional_agents", [])
    for kind in ("agents", "optional_agents", "skills"):
        values = data[kind]
        if not isinstance(values, list) or any(
            not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64
            for name in values
        ):
            raise InstallError(
                f"Invalid suite manifest {path}: {kind} must be a list of canonical definition names."
            )
        if len(values) != len(set(values)):
            raise InstallError(f"Invalid suite manifest {path}: duplicate {kind} names.")
        definition_kind = "agents" if kind == "optional_agents" else kind
        available = {
            name for current_kind, name in definitions.values()
            if current_kind == definition_kind
        }
        unknown = set(values) - available
        if unknown:
            raise InstallError(
                f"Invalid suite manifest {path}: unknown {kind}: {', '.join(sorted(unknown))}."
            )
    if "packages" in data:
        packages = data["packages"]
        if (
            not isinstance(packages, list) or not packages
            or any(not isinstance(name, str) or not NAME.fullmatch(name) for name in packages)
            or len(packages) != len(set(packages))
        ):
            raise InstallError(f"Invalid suite manifest {path}: packages must be unique package IDs.")
        for package in packages:
            resolved = resolve_package(root, package, definitions)
            for kind in ("agents", "skills", "references"):
                data[kind] = sorted(set(data.get(kind, [])) | set(resolved[kind]))
    optional = data.setdefault("optional_packages", [])
    if (
        not isinstance(optional, list)
        or any(not isinstance(name, str) or not NAME.fullmatch(name) for name in optional)
        or len(optional) != len(set(optional))
        or set(optional) & set(data.get("packages", []))
    ):
        raise InstallError(
            f"Invalid suite manifest {path}: optional_packages must be unique package IDs "
            "not already listed in packages."
        )
    if optional_packages in {"include", "exclude"}:
        enabled = optional if optional_packages == "include" else []
    else:
        enabled = [name.strip() for name in optional_packages.split(",")]
        unknown_optional = set(enabled) - set(optional)
        if unknown_optional or len(set(enabled)) != len(enabled):
            raise InstallError(
                "OPTIONAL_PACKAGES must be include, exclude, or unique names from the suite's "
                f"optional_packages ({', '.join(optional) or 'none'})."
            )
    for package in enabled:
        resolved = resolve_package(root, package, definitions)
        for kind in ("agents", "skills", "references"):
            data[kind] = sorted(set(data.get(kind, [])) | set(resolved[kind]))
    data["enabled_optional_packages"] = enabled
    overlap = set(data["agents"]) & set(data["optional_agents"])
    if overlap:
        raise InstallError(
            f"Invalid suite manifest {path}: agents cannot also be optional_agents: "
            f"{', '.join(sorted(overlap))}."
        )
    return data


def output_path(
    source: Path, definitions: dict[Path, tuple[str, str]], root: Path,
    client: ClientAdapter = DEFAULT_CLIENT,
) -> Path:
    if source in definitions:
        kind, name = definitions[source]
        return client.definition_path(kind, name)
    # Keep supporting resources with their owner when its filename identifies it.
    for definition, (kind, name) in definitions.items():
        if (
            kind == "skills"
            and source.parent.parent == definition.parent
            and source.name.startswith(name + "-")
        ):
            return client.definition_path(kind, name).parent / source.parent.name / source.name
    return Path("agentic-toolkit") / "resources" / source.relative_to(root)


def load_package(
    root: Path, package: str, definitions: dict[Path, tuple[str, str]],
) -> dict:
    if not NAME.fullmatch(package):
        raise InstallError(f"Invalid package name: {package!r}")
    path = root / "src" / "packages" / f"{package}.yaml"
    if not path.is_file():
        raise InstallError(f"Unknown package: {package!r}; missing manifest: {path}")
    try:
        import yaml
        from jsonschema import Draft202012Validator
        from scripts.validate_manifests import load_yaml, unknown_fields
    except ImportError as error:
        raise InstallError(
            "Package validation dependencies are required; run "
            "'python -m pip install -r requirements.txt'."
        ) from error
    try:
        data = load_yaml(path.read_text(encoding="utf-8"))
    except (ValueError, yaml.YAMLError) as error:
        raise InstallError(f"Invalid package manifest {path}: {error}") from error
    schema = json.loads((ROOT / "schemas" / "package.schema.json").read_text(encoding="utf-8"))
    errors = list(Draft202012Validator(schema).iter_errors(data))
    if errors:
        raise InstallError(
            f"Invalid package manifest {path}: "
            + "; ".join(error.message for error in errors)
        )
    warnings: list[str] = []
    unknown_fields(data, schema, str(path), warnings)
    for warning in warnings:
        print(f"Warning: {warning}", file=sys.stderr)
    if data["name"] != package:
        raise InstallError(f"Invalid package manifest {path}: name must match {package!r}.")
    for kind in ("agents", "skills"):
        available = {name for current_kind, name in definitions.values() if current_kind == kind}
        unknown = set(data[kind]) - available
        if unknown:
            raise InstallError(
                f"Invalid package manifest {path}: unknown {kind}: {', '.join(sorted(unknown))}."
            )
    for reference in data.get("references", []):
        target = (root / reference).resolve()
        if not target.is_relative_to(root / "src") or not target.is_file():
            raise InstallError(
                f"Invalid package manifest {path}: reference is not a source file: {reference}."
            )
    return data


def resolve_package(
    root: Path, package: str, definitions: dict[Path, tuple[str, str]],
) -> dict[str, list[str]]:
    members: dict[str, set[str]] = {"agents": set(), "skills": set(), "references": set()}
    visited: set[str] = set()
    active: list[str] = []

    def visit(name: str) -> None:
        if name in active:
            raise InstallError("Package dependency cycle: " + " -> ".join([*active, name]))
        if name in visited:
            return
        active.append(name)
        data = load_package(root, name, definitions)
        for dependency in data.get("depends_on", []):
            visit(dependency)
        for kind in members:
            members[kind].update(data.get(kind, []))
        active.pop()
        visited.add(name)

    visit(package)
    return {kind: sorted(names) for kind, names in members.items()}


def render(
    root: Path, suite: str, agent: str = "", skill: str = "",
    *, skills: tuple[str, ...] = (), language_skills: str = "include",
    client: ClientAdapter = DEFAULT_CLIENT,
    package: str = "", optional_packages: str = "include",
) -> dict[Path, bytes]:
    if language_skills not in {"include", "exclude"}:
        raise InstallError("LANGUAGE_SKILLS must be include or exclude.")
    definitions = inventory(root)
    if package and (agent or skill or skills):
        raise InstallError("PACKAGE cannot be combined with AGENT, SKILL, or SKILLS.")
    collection = (
        resolve_package(root, package, definitions)
        if package else load_suite(
            root, suite, definitions,
            # Targeted selections may name any suite member, optional or not.
            "include" if agent or skill or skills else optional_packages,
        )
    )
    language_skills_root = root / "src" / "skills" / "programming-languages"
    if sum(bool(selection) for selection in (agent, skill, skills)) > 1:
        raise InstallError("Select only one of AGENT, SKILL, or SKILLS.")
    if len(set(skills)) != len(skills) or any(not NAME.fullmatch(name) for name in skills):
        raise InstallError("SKILLS must contain unique, valid skill names.")
    selected_names = set(skills)
    if skill:
        selected_names.add(skill)
    available_agents = set(collection["agents"]) | set(collection.get("optional_agents", []))
    if agent and agent not in available_agents:
        raise InstallError(f"Unknown agent {agent!r} for suite {suite!r}")
    available_skills = set(collection["skills"])
    unknown_skills = selected_names - available_skills
    if unknown_skills:
        raise InstallError(
            f"Unknown skill(s) for suite {suite!r}: {', '.join(sorted(unknown_skills))}"
        )
    # Filter collection seeds only; targeted selections and dependency traversal stay intact.
    selected = [
        path
        for path, (kind, name) in definitions.items()
        if (
            (
                not agent and not skill and not skills
                and name in collection[kind]
                and not (
                    language_skills == "exclude" and kind == "skills"
                    and path.is_relative_to(language_skills_root)
                )
            )
            or (
                agent and kind == "agents" and name == agent
            )
            or (
                name in selected_names and kind == "skills"
            )
        )
    ]
    if not selected:
        raise InstallError(
            f"No definitions match suite={suite!r}, agent={agent!r}, "
            f"skill={skill!r}, skills={','.join(skills)!r}"
        )
    pending = list(selected)
    if not agent and not skill and not skills:
        # Package references ship with the collection so their matrices stay updatable.
        pending.extend(
            (root / name).resolve() for name in collection.get("references", [])
            if not (
                language_skills == "exclude"
                and (root / name).resolve().is_relative_to(language_skills_root)
            )
        )
    sources: set[Path] = set()
    visited: set[Path] = set()
    while pending:
        source = pending.pop()
        if source in visited:
            continue
        visited.add(source)
        text = source.read_text(encoding="utf-8")
        sources.add(source)
        if not source.is_relative_to(root / "src"):
            continue
        for match in markdown_links(text):
            resolved = local_link(source, match[2], root)
            if resolved is None:
                continue
            target, _ = resolved
            if (
                source.name in CATALOGUES
                and target in definitions
                and definitions[target][0] == "skills"
            ):
                continue
            if not target.is_file():
                raise InstallError(f"Source dependency must be a file: {source}: {match[2]}")
            pending.append(target)

    files: dict[Path, bytes] = {}
    for source in sorted(sources):
        destination = output_path(source, definitions, root, client)
        text = source.read_text(encoding="utf-8")
        if source in definitions:
            text = client.translate_definition(definitions[source][0], text)
        chunks: list[str] = []
        offset = 0
        for match in markdown_links(text):
            chunks.append(text[offset:match.start()])
            resolved = local_link(source, match[2], root)
            if resolved is None:
                chunks.append(match[0])
            else:
                target, suffix = resolved
                if not source.is_relative_to(root / "src"):
                    # Repository documentation is a snapshot, not a dependency registry.
                    link = REPOSITORY + quote(target.relative_to(root).as_posix()) + suffix
                elif (
                    source.name in CATALOGUES
                    and target in definitions
                    and definitions[target][0] == "skills"
                    and target not in sources
                ):
                    link = REPOSITORY + quote(target.relative_to(root).as_posix()) + suffix
                else:
                    relative = os.path.relpath(
                        output_path(target, definitions, root, client), destination.parent
                    )
                    link = quote(Path(relative).as_posix()) + suffix
                chunks.append(match[1] + link + match[3])
            offset = match.end()
        chunks.append(text[offset:])
        translated = "".join(chunks).encode("utf-8")
        if destination in files:
            raise InstallError(f"Generated path collision: {destination}")
        files[destination] = translated
    files[Path("agentic-toolkit") / "LICENSE"] = (root / "LICENSE").read_bytes()
    return files


def parse_skills(value: str) -> tuple[str, ...]:
    if not value:
        return ()
    skills = tuple(name.strip() for name in value.split(","))
    if any(not name for name in skills):
        raise InstallError("SKILLS must be a comma-separated list of skill names.")
    if len(set(skills)) != len(skills) or any(not NAME.fullmatch(name) for name in skills):
        raise InstallError("SKILLS must contain unique, valid skill names.")
    return skills


def preflight(destination: Path, files: dict[Path, bytes]) -> dict[str, str]:
    manifest = safe_path(destination, Path(MANIFEST))
    managed: dict[str, str] = {}
    if manifest.exists():
        data = json.loads(manifest.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("version") != 1:
            raise InstallError(f"Unsupported ownership manifest: {manifest}")
        records = data.get("files")
        if not isinstance(records, dict) or not all(
            isinstance(key, str) and isinstance(value, str)
            and re.fullmatch(r"[0-9a-f]{64}", value)
            for key, value in records.items()
        ):
            raise InstallError(f"Invalid ownership manifest: {manifest}")
        managed = records
        for name in managed:
            safe_path(destination, Path(name))
    for relative in files:
        target = safe_path(destination, relative)
        for parent in target.parents:
            if parent == destination:
                break
            if parent.exists() and not parent.is_dir():
                raise InstallError(f"Destination parent is not a directory: {parent}")
        if target.exists():
            expected = managed.get(relative.as_posix())
            if not target.is_file() or expected is None:
                raise InstallError(f"Refusing to overwrite an unmanaged path: {target}")
            if digest(target.read_bytes()) != expected:
                raise InstallError(f"Installed file was edited; preserve or move it first: {target}")
    return managed.copy()


def install(destination: Path, files: dict[Path, bytes]) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    lock = safe_path(destination, Path(".agentic-toolkit.lock"))
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as error:
        raise InstallError(f"Installation lock exists: {lock}; check for another installer.") from error
    try:
        os.close(descriptor)
        managed = preflight(destination, files)
        for relative, data in sorted(files.items()):
            target = safe_path(destination, relative)
            if not target.exists() or target.read_bytes() != data:
                atomic_write(target, data)
            managed[relative.as_posix()] = digest(data)
        atomic_write(
            destination / MANIFEST,
            (json.dumps({"version": 1, "files": managed}, indent=2, sort_keys=True) + "\n").encode(),
        )
    finally:
        lock.unlink()


def destination_path(
    scope: str, workspace: str, destdir: str,
    *, client: ClientAdapter = DEFAULT_CLIENT,
) -> Path:
    if scope not in {"user", "workspace"}:
        raise InstallError("SCOPE must be user or workspace.")
    if destdir:
        destination = Path(destdir).expanduser().absolute()
    elif scope == "user":
        destination = client.installation_root(scope, Path.home())
    else:
        if not workspace or not Path(workspace).is_dir():
            raise InstallError("SCOPE=workspace requires WORKSPACE pointing to an existing directory.")
        destination = client.installation_root(scope, Path(workspace).absolute())
    resolved = destination.resolve()
    if (
        resolved == ROOT or ROOT.is_relative_to(resolved)
        or resolved.is_relative_to(ROOT / "src")
        or resolved == Path.home().resolve()
    ):
        raise InstallError(f"Unsafe installation root: {destination}")
    # Do not redirect writes through a linked root or one of its ancestors.
    if any(path.is_symlink() for path in [destination, *destination.parents]):
        raise InstallError(f"Refusing linked installation root: {destination}")
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["help", "list", "plan", "install"])
    args = parser.parse_args()
    if args.command == "help":
        print(
            "make list | plan | install | check\n"
            f"  CLIENT={'|'.join(sorted(CLIENTS))} SCOPE=user|workspace SUITE=software-product-development\n"
            "  PACKAGE=<name> selects a functional agent + skill package instead of SUITE\n"
            "  AGENT=<name>, SKILL=<name>, or SKILLS=<name,name> (listed in suite YAML)\n"
            "  Omit selections to install a suite, or set PACKAGE to install a package\n"
            "  LANGUAGE_SKILLS=include|exclude (default include; full suite/package only)\n"
            "  OPTIONAL_PACKAGES=include|exclude|<name,name> (default include) enables the\n"
            "  suite's optional_packages; targeted AGENT/SKILL/SKILLS are unaffected.\n"
            "  Exclude skips programming-languages skills, not required dependencies;\n"
            "  AGENT, SKILL, and SKILLS selections are unaffected.\n"
            "  WORKSPACE=<existing project> (required for workspace scope)\n"
            "  DESTDIR=<installation root> (optional staging override)\n"
            "  PYTHON=<Python 3.10+ executable>\n"
            "Run make plan with the same variables before make install."
        )
        return 0
    client = get_client(os.environ.get("CLIENT", DEFAULT_CLIENT.name))
    suite = os.environ.get("SUITE", "software-product-development")
    package = os.environ.get("PACKAGE", "")
    optional_packages = os.environ.get("OPTIONAL_PACKAGES", "include")
    if args.command == "list":
        definitions = inventory(ROOT)
        suites = sorted(path.stem for path in (ROOT / "src" / "suites").glob("*.yaml"))
        packages = sorted(path.stem for path in (ROOT / "src" / "packages").glob("*.yaml"))
        collection = (
            resolve_package(ROOT, package, definitions)
            if package else load_suite(ROOT, suite, definitions, optional_packages)
        )
        print("Suites: " + ", ".join(suites))
        print("Packages: " + ", ".join(packages))
        for path, (kind, name) in definitions.items():
            if name in collection[kind]:
                print(f"{kind[:-1]}: {name}")
        return 0
    files = render(
        ROOT, suite, os.environ.get("AGENT", ""), os.environ.get("SKILL", ""),
        skills=parse_skills(os.environ.get("SKILLS", "")),
        language_skills=os.environ.get("LANGUAGE_SKILLS", "include"),
        client=client,
        package=package, optional_packages=optional_packages,
    )
    if not package:
        optional = load_suite(ROOT, suite, inventory(ROOT), "include").get("optional_packages", [])
        if optional:
            print(
                f"Optional packages in suite {suite!r}: {', '.join(optional)} "
                f"(OPTIONAL_PACKAGES={optional_packages}; set OPTIONAL_PACKAGES=exclude "
                "to skip them or a comma-separated list to choose)."
            )
    destination = destination_path(
        os.environ.get("SCOPE", "user"), os.environ.get("WORKSPACE", ""),
        os.environ.get("DESTDIR", ""),
        client=client,
    )
    if args.command == "install":
        install(destination, files)
    else:
        preflight(destination, files)
    print(f"{'Installed' if args.command == 'install' else 'Planned'} {len(files)} files in {destination}")
    for relative in sorted(files):
        print(f"  {relative}")
    print(client.compatibility_notice)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (InstallError, OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
