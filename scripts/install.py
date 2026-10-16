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


def inventory(root: Path) -> dict[Path, tuple[str, str]]:
    definitions: dict[Path, tuple[str, str]] = {}
    names: set[tuple[str, str]] = set()
    for path in sorted((root / "src").rglob("*.md")):
        fields = metadata(path)
        if not fields:
            continue
        kind = "agents" if path.parent.name == "agents" else "skills"
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
    *, client: ClientAdapter = DEFAULT_CLIENT,
) -> dict[Path, bytes]:
    definitions = inventory(root)
    suite_root = root / "src" / "suites" / suite
    if not NAME.fullmatch(suite) or not suite_root.is_dir():
        raise InstallError(f"Unknown suite: {suite!r}")
    if agent and skill:
        raise InstallError("Select AGENT or SKILL, not both.")
    selected = [
        path
        for path, (kind, name) in definitions.items()
        if (
            (not agent and not skill and path.is_relative_to(suite_root))
            or (
                agent and kind == "agents" and name == agent
                and path.is_relative_to(suite_root)
            )
            or (
                skill and kind == "skills" and name == skill
                and (
                    path.is_relative_to(suite_root)
                    or path.is_relative_to(root / "src" / "shared")
                )
            )
        )
    ]
    if not selected:
        raise InstallError(f"No definitions match suite={suite!r}, agent={agent!r}, skill={skill!r}")
    pending = list(selected)
    files: dict[Path, bytes] = {}
    visited: set[Path] = set()
    while pending:
        source = pending.pop()
        if source in visited:
            continue
        visited.add(source)
        destination = output_path(source, definitions, root, client)
        text = source.read_text(encoding="utf-8")
        if source in definitions:
            text = client.translate_definition(definitions[source][0], text)

        def rewrite(match: re.Match[str]) -> str:
            resolved = local_link(source, match[2], root)
            if resolved is None:
                return match[0]
            target, suffix = resolved
            if not source.is_relative_to(root / "src"):
                # Repository documentation is a snapshot, not a dependency registry.
                link = REPOSITORY + quote(target.relative_to(root).as_posix()) + suffix
            else:
                if not target.is_file():
                    raise InstallError(f"Source dependency must be a file: {source}: {match[2]}")
                pending.append(target)
                relative = os.path.relpath(
                    output_path(target, definitions, root, client), destination.parent
                )
                link = quote(Path(relative).as_posix()) + suffix
            return match[1] + link + match[3]

        chunks: list[str] = []
        offset = 0
        for match in markdown_links(text):
            chunks.extend((text[offset:match.start()], rewrite(match)))
            offset = match.end()
        chunks.append(text[offset:])
        translated = "".join(chunks).encode("utf-8")
        if destination in files:
            raise InstallError(f"Generated path collision: {destination}")
        files[destination] = translated
    files[Path("agentic-toolkit") / "LICENSE"] = (root / "LICENSE").read_bytes()
    return files


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
            "  AGENT=<name> or SKILL=<name> (omit both for a suite)\n"
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
