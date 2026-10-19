from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

from scripts import install as installer
from scripts.clients import ClientAdapter, get_client


def write_suite(root: Path, suite: str = "example", **membership) -> Path:
    definitions = installer.inventory(root)
    data = {
        "schema_version": "1.0.0",
        "name": suite,
        "version": "0.1.0",
        "description": "Test collection",
        **{
            kind: [name for definition_kind, name in definitions.values() if definition_kind == kind]
            for kind in ("agents", "skills")
        },
        **membership,
    }
    path = root / "src" / "suites" / f"{suite}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    return path


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
            agents = root / "src" / "agents" / "implementation"
            skills = root / "src" / "skills" / "example"
            agents.mkdir(parents=True)
            (skills / "references").mkdir(parents=True)
            (root / "LICENSE").write_text("Test license", encoding="utf-8")
            (agents / "sample.md").write_text(
                '---\nname: sample\ndescription: "Example agent"\n---\n'
                "CLIENT_MARKER\n[workflow](../../skills/example/workflow.md#steps)\n",
                encoding="utf-8",
            )
            (skills / "workflow.md").write_text(
                '---\nname: workflow\ndescription: "Example skill"\n---\n'
                "CLIENT_MARKER\n[reference](references/workflow-details.md)\n",
                encoding="utf-8",
            )
            (skills / "references" / "workflow-details.md").write_text(
                "[agent](../../../agents/implementation/sample.md#role)\n[workflow](../workflow.md?mode=read#steps)\n",
                encoding="utf-8",
            )
            write_suite(root)
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


class SuiteManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        (self.root / "LICENSE").write_text("Test license", encoding="utf-8")
        for kind, name in (
            ("agents", "included-agent"), ("agents", "outside-agent"),
            ("skills", "included-skill"), ("skills", "outside-skill"),
        ):
            path = self.root / "src" / kind / "example" / f"{name}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                f"---\nname: {name}\ndescription: Test definition\n---\n",
                encoding="utf-8",
            )
        self.path = write_suite(
            self.root, agents=["included-agent"], skills=["included-skill"],
        )
        self.data = yaml.safe_load(self.path.read_text(encoding="utf-8"))

    def write(self, data) -> None:
        self.path.write_text(yaml.safe_dump(data), encoding="utf-8")

    def test_yaml_metadata_and_explicit_membership(self) -> None:
        self.path.write_text(
            'schema_version: "1.0.0"\n'
            "name: example\n"
            'version: "0.1.0"\n'
            "description: >-\n  A multiline\n  suite description.\n"
            "agents: [included-agent]\n"
            "skills:\n  - included-skill # canonical name, not a path\n",
            encoding="utf-8",
        )
        suite = installer.load_suite(self.root, "example", installer.inventory(self.root))
        self.assertEqual(suite["description"], "A multiline suite description.")
        files = installer.render(self.root, "example")
        self.assertEqual(set(files), {
            Path("agents/included-agent.agent.md"), Path("skills/included-skill/SKILL.md"),
            Path("agentic-toolkit/LICENSE"),
        })
        for selection in (
            {"agent": "outside-agent"}, {"skill": "outside-skill"},
            {"skills": ("included-skill", "outside-skill")},
        ):
            with self.subTest(selection=selection):
                with self.assertRaisesRegex(installer.InstallError, "Unknown"):
                    installer.render(self.root, "example", **selection)

    def test_required_dependencies_need_not_be_suite_members(self) -> None:
        agent = self.root / "src/agents/example/included-agent.md"
        agent.write_text(
            agent.read_text(encoding="utf-8")
            + "[required](../../skills/example/outside-skill.md)\n",
            encoding="utf-8",
        )
        for selection in ({}, {"agent": "included-agent"}):
            with self.subTest(selection=selection):
                files = installer.render(self.root, "example", **selection)
                self.assertIn(Path("skills/outside-skill/SKILL.md"), files)
                self.assertNotIn(Path("agents/outside-agent.agent.md"), files)

    def test_membership_is_not_implicit_in_another_suite(self) -> None:
        write_suite(self.root, "other", agents=["outside-agent"], skills=[])
        self.assertIn(
            Path("agents/outside-agent.agent.md"),
            installer.render(self.root, "other", agent="outside-agent"),
        )
        with self.assertRaisesRegex(installer.InstallError, "Unknown agent"):
            installer.render(self.root, "example", agent="outside-agent")

    def test_missing_or_unsafe_suite(self) -> None:
        for name in ("missing", "../example", "Example", ""):
            with self.subTest(name=name):
                with self.assertRaisesRegex(installer.InstallError, "Unknown suite"):
                    installer.render(self.root, name)

    def test_missing_extra_and_non_mapping_fields(self) -> None:
        invalid = [None, [], "example"]
        invalid.extend(
            {key: value for key, value in self.data.items() if key != missing}
            for missing in {"schema_version", "name", "version", "description", "agents"}
        )
        for data in invalid:
            with self.subTest(data=data):
                self.write(data)
                with self.assertRaisesRegex(installer.InstallError, "Invalid suite manifest"):
                    installer.render(self.root, "example")

    def test_unknown_fields_are_ignored_with_a_warning(self) -> None:
        self.write({
            **self.data,
            "future_field": "ignored",
            "language_packs": {"optional": [], "future_option": True},
        })
        with patch("sys.stderr") as stderr:
            installer.load_suite(self.root, "example", installer.inventory(self.root))
        warnings = "".join(call.args[0] for call in stderr.write.call_args_list)
        self.assertIn("future_field", warnings)
        self.assertIn("future_option", warnings)

    def test_bad_field_values(self) -> None:
        for field, values in {
            "schema_version": [None, 1, "2.0.0", "invalid"],
            "name": [None, 1, "", "other", ["example"]],
            "version": [None, 1, "invalid"],
            "description": [None, 1, "", "  ", []],
            "agents": [None, "included-agent", {}, [None], [1], ["Bad Name"], ["path/agent.md"]],
            "skills": [None, "included-skill", {}, [False], ["bad_name"], ["path/skill.md"]],
        }.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    self.write({**self.data, field: value})
                    with self.assertRaisesRegex(installer.InstallError, "Invalid suite manifest"):
                        installer.render(self.root, "example")

    def test_duplicate_and_unknown_members(self) -> None:
        for kind, name in (("agents", "included-agent"), ("skills", "included-skill")):
            for values, message in (
                ([name, name], "duplicate"), (["missing"], "unknown"),
                (["included-skill" if kind == "agents" else "included-agent"], "unknown"),
            ):
                with self.subTest(kind=kind, values=values):
                    self.write({**self.data, kind: values})
                    with self.assertRaisesRegex(installer.InstallError, message):
                        installer.render(self.root, "example")

    def test_invalid_yaml_and_duplicate_keys(self) -> None:
        for text, message in (
            ("name: [broken\n", "Invalid YAML"),
            ("!!python/object:builtins.object {}", "Invalid YAML"),
            ("name: example\nname: example\n", "duplicate field"),
            ("? [invalid, key]\n: value\n", "field names must be strings"),
        ):
            with self.subTest(text=text):
                self.path.write_text(text, encoding="utf-8")
                with self.assertRaisesRegex(installer.InstallError, message):
                    installer.render(self.root, "example")

    def test_definition_names_are_globally_unique(self) -> None:
        for kind in ("agents", "skills"):
            with self.subTest(kind=kind):
                duplicate = self.root / "src" / kind / "another-category" / "included-agent.md"
                duplicate.parent.mkdir(parents=True, exist_ok=True)
                duplicate.write_text(
                    "---\nname: included-agent\ndescription: Duplicate\n---\n",
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(installer.InstallError, "Duplicate definition name"):
                    installer.inventory(self.root)
                duplicate.unlink()

    def test_engineering_manifest_covers_every_maintained_definition(self) -> None:
        definitions = installer.inventory(installer.ROOT)
        collection = installer.load_suite(installer.ROOT, "engineering", definitions)
        files = installer.render(installer.ROOT, "engineering")
        for kind in ("agents", "skills"):
            self.assertEqual(
                set(collection[kind]),
                {name for definition_kind, name in definitions.values() if definition_kind == kind},
            )
        for source in definitions:
            self.assertIn(installer.output_path(source, definitions, installer.ROOT), files)
        self.assertFalse((installer.ROOT / "src/shared").exists())
        self.assertFalse((installer.ROOT / "src/suites/engineering").exists())


class RenderingTests(unittest.TestCase):
    def test_language_skills_default_includes_all_language_definitions(self) -> None:
        files = installer.render(installer.ROOT, "engineering")
        self.assertEqual(
            files,
            installer.render(installer.ROOT, "engineering", language_skills="include"),
        )
        language_root = installer.ROOT / "src/skills/programming-languages"
        definitions = installer.inventory(installer.ROOT)
        language_definitions = [path for path in definitions if path.is_relative_to(language_root)]
        self.assertTrue(language_definitions)
        for source in language_definitions:
            self.assertIn(installer.output_path(source, definitions, installer.ROOT), files)

    def test_suite_excludes_language_only_definitions_but_keeps_other_content(self) -> None:
        included = installer.render(installer.ROOT, "engineering")
        excluded = installer.render(installer.ROOT, "engineering", language_skills="exclude")
        language_root = installer.ROOT / "src/skills/programming-languages"
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
            "agentic-toolkit/resources/src/skills/programming-languages/references/programming-language-matrix.md"
        )
        self.assertIn(
            (installer.REPOSITORY
             + "src/skills/programming-languages/rust/rust-code-quality.md").encode(),
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
                "agents/implementation/example.md": (
                    "---\nname: example\ndescription: Example\n---\n"
                    "[workflow](../../skills/example/workflow.md)\n"
                ),
                "skills/example/workflow.md": (
                    "---\nname: workflow\ndescription: Workflow\n---\n"
                    "[required](../programming-languages/example/required.md)\n"
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
                "skills/example/references/programming-language-matrix.md": (
                    "[navigation](../../programming-languages/example/navigation-only.md)\n"
                ),
            }
            for relative, text in sources.items():
                source = root / "src" / relative
                source.parent.mkdir(parents=True, exist_ok=True)
                source.write_text(text, encoding="utf-8")
            (root / "LICENSE").write_text("Test license", encoding="utf-8")
            write_suite(root)
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
            Path("agentic-toolkit") / "resources" / "src" / "skills"
            / "documentation" / "references" / "documentation"
        )
        documentation_matrix = (
            Path("agentic-toolkit") / "resources" / "src" / "skills"
            / "documentation" / "references" / "documentation-matrix.md"
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

    def test_documentation_agent_installs_with_required_workflows(self) -> None:
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

    def test_documentation_matrix_shares_resources_without_installing_listed_skills(self) -> None:
        common_docs = (
            Path("agentic-toolkit") / "resources" / "src" / "skills"
            / "documentation" / "references" / "documentation"
        )
        documentation_matrix = (
            Path("agentic-toolkit") / "resources" / "src" / "skills"
            / "documentation" / "references" / "documentation-matrix.md"
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
                    + "src/skills/design-and-planning/architecture-workflow.md",
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
                        + "src/skills/documentation/technical-documentation-workflow.md",
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
            "https://github.com/amrishAK/agentic-toolkit/blob/HEAD/src/skills/testing/fuzz-testing-workflow.md",
            matrix,
        )
        self.assertNotIn(Path("skills/fuzz-testing-workflow/SKILL.md"), files)
        original = (installer.ROOT / "src/agents/performance/benchmark-engineer.md").read_text(encoding="utf-8")
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

    def test_individual_workflow_skill(self) -> None:
        files = installer.render(installer.ROOT, "engineering", skill="agent-output-standardization")
        self.assertFalse(any(path.parent == Path("agents") for path in files))
        self.assertIn(Path("skills/agent-output-standardization/SKILL.md"), files)

    def test_selection_skill_includes_its_suite_matrix_without_all_skills(self) -> None:
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
            skills = root / "src" / "skills" / "example"
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
            write_suite(root)
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
                "SUITE": "engineering", "PACKAGE": "", "AGENT": "",
                "SKILL": "agent-output-standardization",
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
