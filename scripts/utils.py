"""Client-independent Markdown parsing and safe filesystem helpers."""

from __future__ import annotations

from collections.abc import Iterator
import hashlib
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")
CODE = re.compile(
    r"(?ms)^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?^ {0,3}\1[ \t]*$|(`+)[^\n]*?\2"
)
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


class InstallError(Exception):
    """An actionable source, selection, or destination error."""


def markdown_links(text: str) -> Iterator[re.Match[str]]:
    code = list(CODE.finditer(text))
    for match in LINK.finditer(text):
        if not any(span.start() <= match.start() < span.end() for span in code):
            yield match


def metadata(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    header, separator, _ = text[4:].partition("\n---\n")
    if not separator:
        raise InstallError(f"Unterminated frontmatter: {path}")
    fields = dict(re.findall(r"^([\w-]+):[ \t]*(.+)$", header, re.MULTILINE))
    name = fields.get("name", "")
    if not NAME.fullmatch(name) or len(name) > 64 or name != path.stem:
        raise InstallError(f"Invalid or mismatched definition name: {path}")
    if not fields.get("description", "").strip("\"' "):
        raise InstallError(f"Missing description: {path}")
    return fields


def local_link(source: Path, target: str, root: Path) -> tuple[Path, str] | None:
    url = urlsplit(target)
    if url.scheme or url.netloc or not url.path:
        return None
    path = (source.parent / unquote(url.path)).resolve()
    if not path.is_relative_to(root) or not path.exists():
        raise InstallError(f"Missing or out-of-tree link in {source}: {target}")
    suffix = ("?" + url.query if url.query else "") + (
        "#" + url.fragment if url.fragment else ""
    )
    return path, suffix


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(root: Path, relative: Path) -> Path:
    if relative.is_absolute() or ".." in relative.parts or relative == Path("."):
        raise InstallError(f"Unsafe installed path: {relative}")
    target = root / relative
    for path in [target, *target.parents]:
        if path.is_symlink():
            raise InstallError(f"Refusing symlink destination: {path}")
        if path == root:
            break
    return target


def atomic_write(target: Path, data: bytes) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
        os.replace(temporary, target)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
