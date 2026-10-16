"""Copilot-specific layout and definition translation."""

from pathlib import Path


class CopilotAdapter:
    name = "copilot"
    compatibility_notice = (
        "Compatibility notice: Copilot tool aliases and role boundaries are preserved, not "
        "sandboxed. Discovery, tool availability and approval-gated subagent delegation "
        "must be verified in your client; unsupported delegation must be reported, not "
        "replaced with direct reviewer edits."
    )

    def installation_root(self, scope: str, base: Path) -> Path:
        return base / (".copilot" if scope == "user" else ".github")

    def definition_path(self, kind: str, name: str) -> Path:
        if kind == "agents":
            return Path("agents") / f"{name}.agent.md"
        if kind == "skills":
            return Path("skills") / name / "SKILL.md"
        raise ValueError(f"Unsupported Copilot definition kind: {kind!r}")

    def translate_definition(self, kind: str, text: str) -> str:
        # The maintained metadata and tool aliases already target Copilot.
        return text
