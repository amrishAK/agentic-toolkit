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


def inventory(root: Path) -> dict[Path, tuple[str, str]]:
    definitions: dict[Path, tuple[str, str]] = {}
    names: set[tuple[str, str]] = set()
    for path in sorted((root / "src").rglob("*.md")):
        fields = metadata(path)
        if not fields:
            continue
        kind = "agents" if "agents" in path.relative_to(root / "src").parts else "skills"
        key = kind, fields["name"]
        if key in names:
            raise InstallError(f"Duplicate {kind} name: {key[1]}")
        names.add(key)
        definitions[path] = key
    return definitions


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


def render(
    root: Path, suite: str, agent: str = "", skill: str = "",
    *, skills: tuple[str, ...] = (), language_skills: str = "include",
    client: ClientAdapter = DEFAULT_CLIENT,
) -> dict[Path, bytes]:
    if language_skills not in {"include", "exclude"}:
        raise InstallError("LANGUAGE_SKILLS must be include or exclude.")
    definitions = inventory(root)
    suite_root = root / "src" / "suites" / suite
    language_skills_root = suite_root / "skills" / "programming-languages"
    if not NAME.fullmatch(suite) or not suite_root.is_dir():
        raise InstallError(f"Unknown suite: {suite!r}")
    if sum(bool(selection) for selection in (agent, skill, skills)) > 1:
        raise InstallError("Select only one of AGENT, SKILL, or SKILLS.")
    if len(set(skills)) != len(skills) or any(not NAME.fullmatch(name) for name in skills):
        raise InstallError("SKILLS must contain unique, valid skill names.")
    selected_names = set(skills)
    if skill:
        selected_names.add(skill)
    shared_agents_root = root / "src" / "shared" / "agents"
    available_agents = {
        name
        for path, (kind, name) in definitions.items()
        if kind == "agents"
        and (
            path.is_relative_to(suite_root)
            or path.is_relative_to(shared_agents_root)
        )
    }
    if agent and agent not in available_agents:
        raise InstallError(f"Unknown agent {agent!r} for suite {suite!r}")
    available_skills = {
        name
        for path, (kind, name) in definitions.items()
        if kind == "skills"
        and (
            path.is_relative_to(suite_root)
            or path.is_relative_to(root / "src" / "shared")
        )
    }
    unknown_skills = selected_names - available_skills
    if unknown_skills:
        raise InstallError(
            f"Unknown skill(s) for suite {suite!r}: {', '.join(sorted(unknown_skills))}"
        )
    # Filter suite seeds only; targeted selections and dependency traversal stay intact.
    selected = [
        path
        for path, (kind, name) in definitions.items()
        if (
            (
                not agent and not skill and not skills
                and (
                    path.is_relative_to(suite_root)
                    or path.is_relative_to(shared_agents_root)
                )
                and not (
                    language_skills == "exclude" and kind == "skills"
                    and path.is_relative_to(language_skills_root)
                )
            )
            or (
                agent and kind == "agents" and name == agent
                and (
                    path.is_relative_to(suite_root)
                    or path.is_relative_to(shared_agents_root)
                )
            )
            or (
                name in selected_names and kind == "skills"
                and (
                    path.is_relative_to(suite_root)
                    or path.is_relative_to(root / "src" / "shared")
                )
            )
        )
    ]
    if not selected:
        raise InstallError(
            f"No definitions match suite={suite!r}, agent={agent!r}, "
            f"skill={skill!r}, skills={','.join(skills)!r}"
        )
    pending = list(selected)
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
            f"  CLIENT={'|'.join(sorted(CLIENTS))} SCOPE=user|workspace SUITE=engineering\n"
            "  AGENT=<name> (suite or shared), SKILL=<name>, or SKILLS=<name,name>\n"
            "  Omit selections to install a suite\n"
            "  LANGUAGE_SKILLS=include|exclude (default include; full suite only)\n"
            "  Exclude skips programming-languages skills, not required dependencies;\n"
            "  AGENT, SKILL, and SKILLS selections are unaffected.\n"
            "  WORKSPACE=<existing project> (required for workspace scope)\n"
            "  DESTDIR=<installation root> (optional staging override)\n"
            "  PYTHON=<Python 3.10+ executable>\n"
            "Run make plan with the same variables before make install."
        )
        return 0
    client = get_client(os.environ.get("CLIENT", DEFAULT_CLIENT.name))
    suite = os.environ.get("SUITE", "engineering")
    if args.command == "list":
        definitions = inventory(ROOT)
        suites = sorted(path.name for path in (ROOT / "src" / "suites").iterdir() if path.is_dir())
        if suite not in suites:
            raise InstallError(f"Unknown suite: {suite!r}")
        print("Suites: " + ", ".join(suites))
        for path, (kind, name) in definitions.items():
            if path.is_relative_to(ROOT / "src" / "suites" / suite) or path.is_relative_to(ROOT / "src" / "shared"):
                print(f"{kind[:-1]}: {name}")
        return 0
    files = render(
        ROOT, suite, os.environ.get("AGENT", ""), os.environ.get("SKILL", ""),
        skills=parse_skills(os.environ.get("SKILLS", "")),
        language_skills=os.environ.get("LANGUAGE_SKILLS", "include"),
        client=client,
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
