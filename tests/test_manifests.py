from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml
from jsonschema import Draft202012Validator

from scripts.validate_manifests import ROOT, SCHEMAS, validate_repository


class ManifestSchemaTests(unittest.TestCase):
    def test_all_schemas_use_draft_2020_12(self) -> None:
        for schema_name in SCHEMAS.values():
            with self.subTest(schema=schema_name):
                schema = json.loads((ROOT / "schemas" / schema_name).read_text(encoding="utf-8"))
                self.assertEqual(
                    schema["$schema"],
                    "https://json-schema.org/draft/2020-12/schema",
                )
                Draft202012Validator.check_schema(schema)

    def test_current_repository_manifests_and_references_are_valid(self) -> None:
        errors, warnings = validate_repository(ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])


class ManifestCrossReferenceTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        shutil.copytree(ROOT / "schemas", self.root / "schemas")
        self.agents = self.root / "src" / "agents" / "unit-tester"
        self.skills = self.root / "src" / "skills" / "testing"
        self.suites = self.root / "src" / "suites"
        self.packs = self.root / "src" / "packs"
        self.agents.mkdir(parents=True)
        self.skills.mkdir(parents=True)
        self.suites.mkdir(parents=True)
        (self.packs / "rust").mkdir(parents=True)
        (self.agents / "unit-tester.md").write_text(
            "---\nname: unit-tester\ndescription: Test agent\n---\n",
            encoding="utf-8",
        )
        (self.skills / "unit-test-design.md").write_text(
            "---\nname: unit-test-design\ndescription: Test skill\n---\n",
            encoding="utf-8",
        )
        (self.agents / "selection-matrix.yaml").write_text(
            yaml.safe_dump({
                "schema_version": "1.0.0",
                "context_signals": ["task_type"],
                "rules": [{
                    "when": {"task_type": ["plan"]},
                    "use": ["unit-test-design"],
                    "mode": "required",
                }],
                "fallback": {
                    "use": ["unit-test-design"],
                    "reason": "Default guidance.",
                },
            }),
            encoding="utf-8",
        )
        (self.agents / "agent.yaml").write_text(
            yaml.safe_dump({
                "schema_version": "1.0.0",
                "name": "unit-tester",
                "version": "0.1.0",
                "description": "Tests agent manifest.",
                "role": "qa",
                "autonomy": "gated",
                "requires": {
                    "skills": ["unit-test-design"],
                    "selection_matrix": "selection-matrix.yaml",
                },
                "outputs": [{"path": "qa/plan.md", "type": "test-plan"}],
                "workflows": {
                    "plan": {
                        "description": "Plan tests.",
                        "inputs": ["feature"],
                        "outputs": ["qa/plan.md"],
                    },
                },
            }),
            encoding="utf-8",
        )
        (self.suites / "example.yaml").write_text(
            yaml.safe_dump({
                "schema_version": "1.0.0",
                "name": "example",
                "version": "0.1.0",
                "description": "Test suite.",
                "agents": ["unit-tester"],
                "skills": ["unit-test-design"],
            }),
            encoding="utf-8",
        )
        (self.packs / "rust" / "pack.yaml").write_text(
            yaml.safe_dump({
                "schema_version": "1.0.0",
                "name": "rust",
                "version": "0.1.0",
                "description": "Test language pack.",
                "extends": {"skills": ["unit-test-design"]},
            }),
            encoding="utf-8",
        )

    def test_agent_skill_and_matrix_references_are_checked(self) -> None:
        (self.agents / "agent.yaml").write_text(
            (self.agents / "agent.yaml")
            .read_text(encoding="utf-8")
            .replace("unit-test-design", "missing-skill"),
            encoding="utf-8",
        )
        matrix_path = self.agents / "selection-matrix.yaml"
        matrix_path.write_text(
            matrix_path.read_text(encoding="utf-8").replace(
                "unit-test-design", "missing-skill",
            ),
            encoding="utf-8",
        )
        errors, _ = validate_repository(self.root)
        self.assertTrue(any("required skill 'missing-skill' does not exist" in e for e in errors))
        self.assertTrue(any("rules[0] references unknown skill 'missing-skill'" in e for e in errors))

    def test_agent_language_pack_references_are_checked(self) -> None:
        agent_path = self.agents / "agent.yaml"
        agent = yaml.safe_load(agent_path.read_text(encoding="utf-8"))
        agent["requires"]["language_packs"] = ["rust"]
        agent_path.write_text(yaml.safe_dump(agent), encoding="utf-8")
        errors, _ = validate_repository(self.root)
        self.assertEqual(errors, [])

        agent["requires"]["language_packs"] = ["missing-pack"]
        agent_path.write_text(yaml.safe_dump(agent), encoding="utf-8")
        errors, _ = validate_repository(self.root)
        self.assertTrue(any(
            "required language pack 'missing-pack' does not exist" in error
            for error in errors
        ))

    def test_agent_language_pack_references_must_match_schema(self) -> None:
        agent_path = self.agents / "agent.yaml"
        agent = yaml.safe_load(agent_path.read_text(encoding="utf-8"))
        agent["requires"]["language_packs"] = ["Rust"]
        agent_path.write_text(yaml.safe_dump(agent), encoding="utf-8")
        errors, _ = validate_repository(self.root)
        self.assertTrue(any(
            "requires.language_packs.0" in error and "does not match" in error
            for error in errors
        ))

    def test_required_skill_cannot_be_excluded_for_the_same_condition(self) -> None:
        matrix_path = self.agents / "selection-matrix.yaml"
        matrix = yaml.safe_load(matrix_path.read_text(encoding="utf-8"))
        matrix["exclusions"] = [{
            "when": {"task_type": ["plan"]},
            "exclude": ["unit-test-design"],
            "reason": "Conflict test.",
        }]
        matrix_path.write_text(yaml.safe_dump(matrix), encoding="utf-8")
        errors, _ = validate_repository(self.root)
        self.assertTrue(any("are excluded under the same condition" in e for e in errors))

    def test_unknown_fields_are_warnings_not_errors(self) -> None:
        suite_path = self.suites / "example.yaml"
        suite = yaml.safe_load(suite_path.read_text(encoding="utf-8"))
        suite["future_field"] = "ignored"
        suite_path.write_text(yaml.safe_dump(suite), encoding="utf-8")
        errors, warnings = validate_repository(self.root)
        self.assertEqual(errors, [])
        self.assertTrue(any("unknown field 'future_field' (ignored)" in warning for warning in warnings))


if __name__ == "__main__":
    unittest.main()
