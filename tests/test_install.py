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
    def test_language_skills_default_includes_all_language_definitions(self) -> None:
        files = installer.render(installer.ROOT, "engineering")
        self.assertEqual(
            files,
            installer.render(installer.ROOT, "engineering", language_skills="include"),
        )
        language_root = installer.ROOT / "src/suites/engineering/skills/programming-languages"
        definitions = installer.inventory(installer.ROOT)
        language_definitions = [path for path in definitions if path.is_relative_to(language_root)]
        self.assertTrue(language_definitions)
        for source in language_definitions:
            self.assertIn(installer.output_path(source, definitions, installer.ROOT), files)

    def test_suite_excludes_language_only_definitions_but_keeps_other_content(self) -> None:
        included = installer.render(installer.ROOT, "engineering")
        excluded = installer.render(installer.ROOT, "engineering", language_skills="exclude")
        language_root = installer.ROOT / "src/suites/engineering/skills/programming-languages"
        definitions = installer.inventory(installer.ROOT)
        for source in definitions:
            destination = installer.output_path(source, definitions, installer.ROOT)
            if source.is_relative_to(language_root):
                self.assertNotIn(destination, excluded)
            elif destination in included:
                self.assertIn(destination, excluded)
        self.assertIn(
            Path("skills/agent-output-standardization/templates/agent-output-standardization-review-report.md"),
            excluded,
        )
        self.assertIn(Path("agentic-toolkit/LICENSE"), excluded)
        matrix = Path(
            "agentic-toolkit/resources/src/shared/skills/references/programming-language-matrix.md"
        )
        self.assertIn(
            (installer.REPOSITORY
             + "src/suites/engineering/skills/programming-languages/rust/rust-code-quality.md").encode(),
            excluded[matrix],
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            installer.install(root, excluded)
            for relative, data in excluded.items():
                if relative.suffix != ".md":
                    continue
                for match in installer.markdown_links(data.decode()):
                    resolved = installer.local_link(root / relative, match[2], root)
                    if resolved is not None:
                        self.assertTrue(resolved[0].is_file(), (relative, match[2]))

    def test_language_exclusion_keeps_explicit_transitive_dependencies(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            sources = {
                "agents/example.md": (
                    "---\nname: example\ndescription: Example\n---\n"
                    "[workflow](../skills/workflow.md)\n"
                ),
                "skills/workflow.md": (
                    "---\nname: workflow\ndescription: Workflow\n---\n"
                    "[required](programming-languages/example/required.md)\n"
                    "[matrix](references/programming-language-matrix.md)\n"
                ),
                "skills/programming-languages/example/required.md": (
                    "---\nname: required\ndescription: Required\n---\n"
                    "[dependency](dependency.md)\n"
                ),
                "skills/programming-languages/example/dependency.md": (
                    "---\nname: dependency\ndescription: Dependency\n---\n"
                ),
                "skills/programming-languages/example/navigation-only.md": (
                    "---\nname: navigation-only\ndescription: Navigation only\n---\n"
                ),
                "skills/references/programming-language-matrix.md": (
                    "[navigation](../programming-languages/example/navigation-only.md)\n"
                ),
            }
            for relative, text in sources.items():
                source = root / "src/suites/example" / relative
                source.parent.mkdir(parents=True, exist_ok=True)
                source.write_text(text, encoding="utf-8")
            (root / "LICENSE").write_text("Test license", encoding="utf-8")
            for selection in ({}, {"agent": "example"}, {"skill": "workflow"}):
                with self.subTest(selection=selection):
                    files = installer.render(
                        root, "example", language_skills="exclude", **selection,
                    )
                    self.assertIn(Path("skills/required/SKILL.md"), files)
                    self.assertIn(Path("skills/dependency/SKILL.md"), files)
                    self.assertNotIn(Path("skills/navigation-only/SKILL.md"), files)

    def test_targeted_selections_are_unaffected_by_language_exclusion(self) -> None:
        for selection in (
            {"agent": "benchmark-engineer"},
            {"agent": "technical-documentation-writer"},
            {"skill": "rust-code-quality"},
            {"skills": ("rust-code-quality", "c-code-quality")},
        ):
            with self.subTest(selection=selection):
                self.assertEqual(
                    installer.render(installer.ROOT, "engineering", **selection),
                    installer.render(
                        installer.ROOT, "engineering", language_skills="exclude", **selection,
                    ),
                )

    def test_invalid_language_skills_option_fails_even_for_targeted_selection(self) -> None:
        for value in ("", "invalid", "INCLUDE"):
            for selection in ({}, {"skill": "rust-code-quality"}):
                with self.subTest(value=value, selection=selection):
                    with self.assertRaisesRegex(
                        installer.InstallError, "LANGUAGE_SKILLS must be include or exclude",
                    ):
                        installer.render(
                            installer.ROOT, "engineering", language_skills=value, **selection,
                        )

    def test_suite_layout_and_all_links(self) -> None:
        files = installer.render(installer.ROOT, "engineering")
        self.assertEqual(sum(path.suffix == ".md" and path.parent == Path("agents") for path in files), 13)
        self.assertEqual(sum(path.name == "SKILL.md" for path in files), 45)
        governance = Path("skills") / "documentation-selection-workflow"
        self.assertIn(governance / "SKILL.md", files)
        common_docs = (
            Path("agentic-toolkit") / "resources" / "src" / "shared"
            / "skills" / "references" / "documentation"
        )
        documentation_matrix = (
            Path("agentic-toolkit") / "resources" / "src" / "shared"
            / "skills" / "references" / "documentation-matrix.md"
        )
        self.assertIn(documentation_matrix, files)
        for topic in (
            "documentation-rules", "docs-layout", "technical-guides",
            "product-overview", "architecture-docs",
            "feature-docs", "project-tracking", "release-docs",
            "release-notes", "roadmap-known-issues", "community-docs",
        ):
            self.assertIn(common_docs / f"{topic}.md", files)
        self.assertFalse(any(
            path.is_relative_to(governance / "references") for path in files
        ))
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

    def test_shared_documentation_agent_installs_with_required_workflows(self) -> None:
        files = installer.render(
            installer.ROOT, "engineering", agent="technical-documentation-writer",
        )
        agent = Path("agents") / "technical-documentation-writer.agent.md"
        self.assertIn(agent, files)
        content = files[agent].decode()
        self.assertIn("documentation-selection-workflow", content)
        self.assertIn("technical-documentation-workflow", content)
        self.assertIn(
            Path("skills") / "documentation-selection-workflow" / "SKILL.md",
            files,
        )
        self.assertIn(
            Path("skills") / "technical-documentation-workflow" / "SKILL.md",
            files,
        )
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory).resolve()
            installer.install(destination, files)
            for relative in files:
                if relative.suffix != ".md":
                    continue
                source = destination / relative
                for match in installer.markdown_links(source.read_text(encoding="utf-8")):
                    resolved = installer.local_link(source, match[2], destination)
                    if resolved is not None:
                        self.assertTrue(resolved[0].is_file(), (source, match[2]))

    def test_shared_agent_can_be_selected_from_any_suite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            for suite in ("engineering", "research"):
                (root / "src" / "suites" / suite).mkdir(parents=True)
            shared_agents = root / "src" / "shared" / "agents" / "review"
            shared_agents.mkdir(parents=True)
            (root / "LICENSE").write_text("Test license", encoding="utf-8")
            (shared_agents / "shared-reviewer.md").write_text(
                "---\nname: shared-reviewer\ndescription: Shared review role\n---\n",
                encoding="utf-8",
            )

            for suite in ("engineering", "research"):
                with self.subTest(suite=suite):
                    files = installer.render(root, suite, agent="shared-reviewer")
                    self.assertIn(Path("agents/shared-reviewer.agent.md"), files)

    def test_documentation_matrix_shares_resources_without_installing_listed_skills(self) -> None:
        common_docs = (
            Path("agentic-toolkit") / "resources" / "src" / "shared"
            / "skills" / "references" / "documentation"
        )
        documentation_matrix = (
            Path("agentic-toolkit") / "resources" / "src" / "shared"
            / "skills" / "references" / "documentation-matrix.md"
        )
        technical = Path("skills") / "technical-documentation-workflow" / "SKILL.md"
        for include_writer in (False, True):
            with self.subTest(include_writer=include_writer):
                selection = ("documentation-selection-workflow",)
                if include_writer:
                    selection += ("technical-documentation-workflow",)
                files = installer.render(installer.ROOT, "engineering", skills=selection)
                self.assertEqual(
                    sum(path.parent == common_docs for path in files), 11,
                )
                self.assertIn(common_docs / "technical-guides.md", files)
                self.assertNotIn(common_docs / "document-outlines.md", files)
                self.assertFalse(any(path.parent == Path("agents") for path in files))
                self.assertNotIn(
                    Path("skills") / "architecture-workflow" / "SKILL.md", files,
                )
                matrix = files[documentation_matrix].decode()
                guides = files[common_docs / "technical-guides.md"].decode()
                for anchor in (
                    "user-and-developer-guides", "setup-and-onboarding",
                    "package-and-module-guides", "integration-guides",
                    "data-and-request-flow", "runbooks", "troubleshooting",
                    "migration-notes",
                ):
                    self.assertIn(f"(documentation/technical-guides.md#{anchor})", matrix)
                    self.assertTrue(any(
                        line.startswith("## ")
                        and line[3:].lower().replace(" ", "-") == anchor
                        for line in guides.splitlines()
                    ), anchor)
                self.assertIn(
                    installer.REPOSITORY
                    + "src/suites/engineering/skills/design-and-planning/architecture-workflow.md",
                    matrix,
                )
                self.assertTrue(all(
                    not line or line.startswith(("# ", "## ", "|"))
                    for line in matrix.splitlines()
                ))
                workflow = files[
                    Path("skills") / "documentation-selection-workflow" / "SKILL.md"
                ].decode()
                self.assertIn("documentation-matrix.md#document-and-topic-reference-matrix", workflow)
                self.assertIn("documentation-rules.md", workflow)
                self.assertIn("### Document routing and maintenance ownership", workflow)
                if include_writer:
                    self.assertIn(technical, files)
                    relative = Path(
                        os.path.relpath(technical, documentation_matrix.parent)
                    ).as_posix()
                    self.assertIn(f"[technical documentation workflow]({relative})", matrix)
                else:
                    self.assertNotIn(technical, files)
                    self.assertIn(
                        installer.REPOSITORY
                        + "src/shared/skills/technical-documentation-workflow.md",
                        matrix,
                    )

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
        self.assertIn(
            Path("skills/skill-selection-workflow/SKILL.md"),
            files,
        )
        matrix = files[
            Path("skills/skill-selection-workflow/references/skill-selection-workflow-matrix.md")
        ].decode()
        self.assertIn(
            "[benchmark-workflow](../../benchmark-workflow/SKILL.md)",
            matrix,
        )
        self.assertIn(
            "https://github.com/amrishAK/agentic-toolkit/blob/HEAD/src/suites/engineering/skills/testing/fuzz-testing-workflow.md",
            matrix,
        )
        self.assertNotIn(Path("skills/fuzz-testing-workflow/SKILL.md"), files)
        original = (installer.ROOT / "src/suites/engineering/agents/benchmark-engineer.md").read_text(encoding="utf-8")
        translated = files[Path("agents/benchmark-engineer.agent.md")].decode()
        self.assertEqual(original.split("\n---\n")[0], translated.split("\n---\n")[0])

    def test_multiple_skill_selection_keeps_catalogue_links_out_of_dependencies(self) -> None:
        files = installer.render(
            installer.ROOT,
            "engineering",
            skills=("rust-code-quality", "c-code-quality"),
        )
        self.assertIn(Path("skills/rust-code-quality/SKILL.md"), files)
        self.assertIn(Path("skills/c-code-quality/SKILL.md"), files)
        self.assertNotIn(Path("skills/cpp-code-quality/SKILL.md"), files)
        self.assertFalse(any(path.parent == Path("agents") for path in files))
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

    def test_individual_shared_skill(self) -> None:
        files = installer.render(installer.ROOT, "engineering", skill="agent-output-standardization")
        self.assertFalse(any(path.parent == Path("agents") for path in files))
        self.assertIn(Path("skills/agent-output-standardization/SKILL.md"), files)

    def test_shared_selection_skill_includes_its_suite_matrix_without_all_skills(self) -> None:
        files = installer.render(installer.ROOT, "engineering", skill="skill-selection-workflow")
        self.assertIn(Path("skills/skill-selection-workflow/SKILL.md"), files)
        self.assertIn(
            Path("skills/skill-selection-workflow/references/skill-selection-workflow-matrix.md"),
            files,
        )
        self.assertNotIn(Path("skills/code-quality-workflow/SKILL.md"), files)
        self.assertFalse(any(path.parent == Path("agents") for path in files))

    def test_bad_selections(self) -> None:
        for suite, agent, skill, skills in [
            ("missing", "", "", ()), ("../engineering", "", "", ()),
            ("engineering", "missing", "", ()), ("engineering", "", "missing", ()),
            ("engineering", "benchmark-engineer", "benchmark-workflow", ()),
            ("engineering", "", "", ("benchmark-workflow", "benchmark-workflow")),
            ("engineering", "", "", ("bad name",)),
            ("engineering", "", "", ("rust-code-quality", "missing-skill")),
            ("engineering", "", "benchmark-workflow", ("rust-code-quality",)),
        ]:
            with self.subTest(suite=suite, agent=agent, skill=skill):
                with self.assertRaises(installer.InstallError):
                    installer.render(installer.ROOT, suite, agent, skill, skills=skills)

    def test_parse_skills(self) -> None:
        self.assertEqual(
            installer.parse_skills("rust-code-quality, c-code-quality"),
            ("rust-code-quality", "c-code-quality"),
        )
        for value in ("rust-code-quality,", "rust-code-quality,,c-code-quality", "bad name"):
            with self.subTest(value=value):
                with self.assertRaises(installer.InstallError):
                    installer.parse_skills(value)

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
    def test_language_exclusion_does_not_prune_previous_installation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            language_skill = Path("skills/rust-code-quality/SKILL.md")
            installer.install(
                root, installer.render(installer.ROOT, "engineering", skill="rust-code-quality"),
            )
            original = (root / language_skill).read_bytes()
            installer.install(
                root, installer.render(installer.ROOT, "engineering", language_skills="exclude"),
            )
            self.assertEqual((root / language_skill).read_bytes(), original)
            manifest = json.loads((root / installer.MANIFEST).read_text(encoding="utf-8"))
            self.assertIn(language_skill.as_posix(), manifest["files"])

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
                "SKILLS": "", "LANGUAGE_SKILLS": "include",
                "DESTDIR": str(destination),
            }
            command = [sys.executable, "-B", "-m", "scripts.install"]
            plan = subprocess.run(command + ["plan"], env=env, capture_output=True, text=True)
            self.assertEqual(plan.returncode, 0, plan.stderr)
            self.assertFalse(destination.exists())
            result = subprocess.run(command + ["install"], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((destination / "skills/agent-output-standardization/SKILL.md").is_file())
            env["SKILL"] = ""
            env["SKILLS"] = "code-quality-workflow,rust-code-quality"
            result = subprocess.run(command + ["plan"], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            result = subprocess.run(command + ["install"], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((destination / "skills/code-quality-workflow/SKILL.md").is_file())
            self.assertTrue((destination / "skills/rust-code-quality/SKILL.md").is_file())
            self.assertFalse((destination / "skills/cpp-code-quality/SKILL.md").exists())
            help_text = subprocess.run(
                command + ["help"], env=env, capture_output=True, text=True
            ).stdout
            self.assertIn("SKILLS=", help_text)
            self.assertIn("LANGUAGE_SKILLS=include|exclude", help_text)
            env["LANGUAGE_SKILLS"] = "invalid"
            result = subprocess.run(command + ["plan"], env=env, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("LANGUAGE_SKILLS must be include or exclude", result.stderr)
            env["LANGUAGE_SKILLS"] = "include"
            env["CLIENT"] = "unsupported"
            result = subprocess.run(command + ["plan"], env=env, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Unsupported CLIENT=", result.stderr)


if __name__ == "__main__":
    unittest.main()
