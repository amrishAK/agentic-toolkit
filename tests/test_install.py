from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts import install as installer
from scripts.clients import ClientAdapter, get_client


class AlternateTestAdapter:
    name = "test-client"
    compatibility_notice = "Test adapter only; not a supported client."

    def installation_root(self, scope: str, base: Path) -> Path:
        return base / f".test-{scope}"

    def definition_path(self, kind: str, name: str) -> Path:
        if kind == "agents":
            return Path("roles") / name / "ROLE.md"
        return Path("workflows") / name / "GUIDE.md"

    def translate_definition(self, kind: str, text: str) -> str:
        return text.replace("CLIENT_MARKER", f"translated-{kind}")


class ClientAdapterTests(unittest.TestCase):
    def test_client_selection_is_explicit(self) -> None:
        self.assertEqual(get_client("copilot").name, "copilot")
        for name in ["claude", "missing", "../copilot"]:
            with self.subTest(name=name):
                with self.assertRaisesRegex(ValueError, "Available clients: copilot"):
                    get_client(name)

    def test_copilot_preserves_definition_metadata_and_body(self) -> None:
        client = get_client("copilot")
        for path, (kind, _) in installer.inventory(installer.ROOT).items():
            text = path.read_text(encoding="utf-8")
            self.assertEqual(client.translate_definition(kind, text), text)

    def test_shared_engine_rewrites_all_surfaces_for_another_layout(self) -> None:
        client: ClientAdapter = AlternateTestAdapter()
        with tempfile.TemporaryDirectory(prefix="adapter space ") as directory:
            root = Path(directory).resolve()
            agents = root / "src" / "suites" / "example" / "agents"
            skills = agents.parent / "skills"
            agents.mkdir(parents=True)
            (skills / "references").mkdir(parents=True)
            (root / "LICENSE").write_text("Test license", encoding="utf-8")
            (agents / "sample.md").write_text(
                '---\nname: sample\ndescription: "Example agent"\n---\n'
                "CLIENT_MARKER\n[workflow](../skills/workflow.md#steps)\n",
                encoding="utf-8",
            )
            (skills / "workflow.md").write_text(
                '---\nname: workflow\ndescription: "Example skill"\n---\n'
                "CLIENT_MARKER\n[reference](references/workflow-details.md)\n",
                encoding="utf-8",
            )
            (skills / "references" / "workflow-details.md").write_text(
                "[agent](../../agents/sample.md#role)\n[workflow](../workflow.md?mode=read#steps)\n",
                encoding="utf-8",
            )
            files = installer.render(root, "example", agent="sample", client=client)
            agent = Path("roles") / "sample" / "ROLE.md"
            skill = Path("workflows") / "workflow" / "GUIDE.md"
            resource = skill.parent / "references" / "workflow-details.md"
            self.assertIn(b"translated-agents", files[agent])
            self.assertIn(b"translated-skills", files[skill])
            self.assertIn(b"GUIDE.md#steps", files[agent])
            self.assertIn(b"ROLE.md#role", files[resource])
            self.assertIn(b"GUIDE.md?mode=read#steps", files[resource])
            self.assertIn(b"[reference](references/workflow-details.md)", files[skill])
            self.assertNotIn(Path("agents") / "sample.agent.md", files)
            self.assertEqual(
                installer.destination_path("workspace", str(root), "", client=client),
                root / ".test-workspace",
            )
            with patch.object(Path, "home", return_value=root):
                self.assertEqual(
                    installer.destination_path("user", "", "", client=client),
                    root / ".test-user",
                )
            destination = root / "installed"
            installer.install(destination, files)
            for relative in files:
                if relative.suffix == ".md":
                    source = destination / relative
                    for match in installer.markdown_links(source.read_text(encoding="utf-8")):
                        resolved = installer.local_link(source, match[2], destination)
                        if resolved is not None:
                            self.assertTrue(resolved[0].is_file())


class RenderingTests(unittest.TestCase):
    def test_suite_layout_and_all_links(self) -> None:
        files = installer.render(installer.ROOT, "engineering")
        self.assertEqual(sum(path.suffix == ".md" and path.parent == Path("agents") for path in files), 13)
        self.assertEqual(sum(path.name == "SKILL.md" for path in files), 43)
        governance = Path("skills") / "documentation-requirements"
        self.assertIn(governance / "SKILL.md", files)
        for topic in (
            "product-overview", "architecture-docs",
            "release-docs", "roadmap-known-issues", "community-docs",
        ):
            self.assertIn(
                governance / "references" / f"documentation-requirements-{topic}.md",
                files,
            )
        self.assertIn(Path("agentic-toolkit") / "LICENSE", files)
        for source, (kind, name) in installer.inventory(installer.ROOT).items():
            if kind == "agents":
                original = source.read_text(encoding="utf-8").split("\n---\n")[0]
                translated = files[Path("agents") / f"{name}.agent.md"].decode().split("\n---\n")[0]
                self.assertEqual(original, translated)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            installer.install(root, files)
            for relative in files:
                if relative.suffix != ".md":
                    continue
                source = root / relative
                for match in installer.markdown_links(source.read_text(encoding="utf-8")):
                    resolved = installer.local_link(source, match[2], root)
                    if resolved is not None:
                        self.assertTrue(resolved[0].is_file(), (source, match[2]))

    def test_agent_selection_includes_only_one_agent_and_transitive_skills(self) -> None:
        files = installer.render(installer.ROOT, "engineering", agent="benchmark-engineer")
        self.assertEqual(
            [path.name for path in files if path.parent == Path("agents")],
            ["benchmark-engineer.agent.md"],
        )
        self.assertIn(Path("skills/benchmark-workflow/SKILL.md"), files)
        self.assertIn(Path("skills/agent-output-standardization/SKILL.md"), files)
        self.assertIn(
            Path("skills/agent-output-standardization/templates/agent-output-standardization-review-report.md"),
            files,
        )
        original = (installer.ROOT / "src/suites/engineering/agents/benchmark-engineer.md").read_text(encoding="utf-8")
        translated = files[Path("agents/benchmark-engineer.agent.md")].decode()
        self.assertEqual(original.split("\n---\n")[0], translated.split("\n---\n")[0])

    def test_individual_shared_skill(self) -> None:
        files = installer.render(installer.ROOT, "engineering", skill="agent-output-standardization")
        self.assertFalse(any(path.parent == Path("agents") for path in files))
        self.assertIn(Path("skills/agent-output-standardization/SKILL.md"), files)

    def test_bad_selections(self) -> None:
        for suite, agent, skill in [
            ("missing", "", ""), ("../engineering", "", ""),
            ("engineering", "missing", ""), ("engineering", "", "missing"),
            ("engineering", "benchmark-engineer", "benchmark-workflow"),
        ]:
            with self.subTest(suite=suite, agent=agent, skill=skill):
                with self.assertRaises(installer.InstallError):
                    installer.render(installer.ROOT, suite, agent, skill)

    def test_missing_link_fails(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(installer.InstallError, "Missing"):
                installer.local_link(root / "source.md", "missing.md", root)

    def test_markdown_examples_are_not_dependencies(self) -> None:
        text = (
            "[real](actual.md)\n`[inline](<relative link>)`\n"
            "```markdown\n[example](missing.md)\n```\n"
            "~~~markdown\n[example](also-missing.md)\n~~~\n"
        )
        self.assertEqual([match[2] for match in installer.markdown_links(text)], ["actual.md"])

    def test_cycle_and_broken_dependency(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            skills = root / "src" / "suites" / "example" / "skills"
            skills.mkdir(parents=True)
            (root / "LICENSE").write_text("Test license", encoding="utf-8")
            first = skills / "first.md"
            first.write_text(
                '---\nname: first\ndescription: "First"\n---\n[second](second.md#heading)',
                encoding="utf-8",
            )
            (skills / "second.md").write_text(
                '---\nname: second\ndescription: "Second"\n---\n[first](first.md)',
                encoding="utf-8",
            )
            files = installer.render(root, "example", skill="first")
            self.assertEqual(len(files), 3)
            self.assertIn(b"#heading", files[Path("skills/first/SKILL.md")])
            first.write_text(first.read_text(encoding="utf-8") + "\n[bad](missing.md)", encoding="utf-8")
            with self.assertRaisesRegex(installer.InstallError, "Missing"):
                installer.render(root, "example", skill="first")


class InstallationTests(unittest.TestCase):
    def test_repeat_update_and_additive_selection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = Path("agents/first.agent.md")
            second = Path("agents/second.agent.md")
            installer.install(root, {first: b"original"})
            timestamp = (root / first).stat().st_mtime_ns
            installer.install(root, {first: b"original"})
            self.assertEqual((root / first).stat().st_mtime_ns, timestamp)
            installer.install(root, {first: b"updated"})
            installer.install(root, {second: b"second"})
            self.assertEqual((root / first).read_bytes(), b"updated")
            manifest = json.loads((root / installer.MANIFEST).read_text(encoding="utf-8"))
            self.assertEqual(len(manifest["files"]), 2)

    def test_unmanaged_conflict_prevents_any_file_writes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "occupied").write_bytes(b"personal")
            with self.assertRaisesRegex(installer.InstallError, "unmanaged"):
                installer.install(root, {Path("new"): b"new", Path("occupied"): b"replace"})
            self.assertFalse((root / "new").exists())
            self.assertEqual((root / "occupied").read_bytes(), b"personal")
            self.assertFalse((root / ".agentic-toolkit.lock").exists())

    def test_local_edits_protected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            installer.install(root, {Path("owned"): b"original"})
            (root / "owned").write_bytes(b"local edit")
            with self.assertRaisesRegex(installer.InstallError, "was edited"):
                installer.install(root, {Path("owned"): b"replacement"})
            self.assertEqual((root / "owned").read_bytes(), b"local edit")

    def test_lock_prevents_parallel_writes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            lock = root / ".agentic-toolkit.lock"
            lock.write_bytes(b"")
            with self.assertRaisesRegex(installer.InstallError, "lock exists"):
                installer.install(root, {Path("owned"): b"data"})
            self.assertTrue(lock.exists())
            self.assertFalse((root / "owned").exists())

    def test_bad_manifest_and_parent_conflicts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = root / installer.MANIFEST
            manifest.write_text('{"version":1,"files":{"../escape":"' + "0" * 64 + '"}}', encoding="utf-8")
            with self.assertRaisesRegex(installer.InstallError, "Unsafe"):
                installer.preflight(root, {})
            manifest.write_text('{"version":1,"files":[]}', encoding="utf-8")
            with self.assertRaisesRegex(installer.InstallError, "Invalid"):
                installer.preflight(root, {})
            manifest.unlink()
            (root / "agents").write_bytes(b"not a directory")
            with self.assertRaisesRegex(installer.InstallError, "not a directory"):
                installer.install(root, {Path("agents/name.agent.md"): b"data"})

    def test_user_workspace_and_staging_destinations(self) -> None:
        with tempfile.TemporaryDirectory(prefix="toolkit space ") as directory:
            root = Path(directory).resolve()
            with patch.object(Path, "home", return_value=root):
                self.assertEqual(installer.destination_path("user", "", ""), root / ".copilot")
            self.assertEqual(installer.destination_path("workspace", str(root), ""), root / ".github")
            self.assertEqual(installer.destination_path("user", "", str(root / "stage")), root / "stage")
            with self.assertRaises(installer.InstallError):
                installer.destination_path("workspace", "", "")
            for unsafe in [installer.ROOT, installer.ROOT.parent, installer.ROOT / "src" / "generated", Path.home()]:
                with self.subTest(unsafe=unsafe):
                    with self.assertRaises(installer.InstallError):
                        installer.destination_path("user", "", str(unsafe))

    def test_cli_plan_is_read_only_and_install_persists(self) -> None:
        with tempfile.TemporaryDirectory(prefix="toolkit space ") as directory:
            destination = Path(directory) / "not created"
            env = {
                **os.environ, "CLIENT": "copilot", "SCOPE": "user",
                "SUITE": "engineering", "AGENT": "", "SKILL": "agent-output-standardization",
                "DESTDIR": str(destination),
            }
            command = [sys.executable, "-B", "-m", "scripts.install"]
            plan = subprocess.run(command + ["plan"], env=env, capture_output=True, text=True)
            self.assertEqual(plan.returncode, 0, plan.stderr)
            self.assertFalse(destination.exists())
            result = subprocess.run(command + ["install"], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((destination / "skills/agent-output-standardization/SKILL.md").is_file())
            env["CLIENT"] = "unsupported"
            result = subprocess.run(command + ["plan"], env=env, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Unsupported CLIENT=", result.stderr)


if __name__ == "__main__":
    unittest.main()
