"""Explicit client selection; shared installation code depends on this contract."""

from pathlib import Path
from typing import Protocol

from .copilot import CopilotAdapter


class ClientAdapter(Protocol):
    name: str
    compatibility_notice: str

    def installation_root(self, scope: str, base: Path) -> Path: ...

    def definition_path(self, kind: str, name: str) -> Path: ...

    def translate_definition(self, kind: str, text: str) -> str: ...


CLIENTS: dict[str, ClientAdapter] = {"copilot": CopilotAdapter()}
DEFAULT_CLIENT = CLIENTS["copilot"]


def get_client(name: str) -> ClientAdapter:
    if name not in CLIENTS:
        raise ValueError(
            f"Unsupported CLIENT={name!r}. Available clients: {', '.join(sorted(CLIENTS))}."
        )
    return CLIENTS[name]
