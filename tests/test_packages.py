from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

from scripts import install as installer
from scripts.validate_manifests import validate_repository


class PackageTests(unittest.TestCase):
    def test_package_installs_its_reference_matrices(self) -> None:
        for package, name in (
            ("core", "skill-selection-workflow-matrix.md"),
            ("core", "documentation-matrix.md"),
            ("design-and-planning", "feature-docs.md"),
            ("design-and-planning", "roadmap-known-issues.md"),
            ("build-and-delivery", "release-notes.md"),
            ("project-standards", "project-tracking.md"),
            ("core", "documentation-rules.md"),
            ("programming-languages", "programming-language-matrix.md"),
        ):
            with self.subTest(package=package, matrix=name):
                files = installer.render(installer.ROOT, "engineering", package=package)
                self.assertTrue(any(path.name == name for path in files))

    def test_optional_packages_are_enabled_by_default_and_can_be_excluded(self) -> None:
        definitions = installer.inventory(installer.ROOT)
        default = installer.load_suite(installer.ROOT, "engineering", definitions)
        self.assertEqual(default["optional_packages"], ["programming-languages"])
        self.assertIn("rust-code-quality", default["skills"])
        excluded = installer.load_suite(installer.ROOT, "engineering", definitions, "exclude")
        self.assertNotIn("rust-code-quality", excluded["skills"])
        with self.assertRaises(installer.InstallError):
            installer.load_suite(installer.ROOT, "engineering", definitions, "testing")
        files = installer.render(
            installer.ROOT, "engineering", skill="rust-code-quality", optional_packages="exclude"
        )
        self.assertTrue(files)

    def test_packages_include_expected_core_guidance_and_agents(self) -> None:
        definitions = installer.inventory(installer.ROOT)
        paths = sorted((installer.ROOT / "src" / "packages").glob("*.yaml"))
        self.assertEqual(len(paths), 9)
        core_agents = {"source-documentation-writer", "technical-documentation-writer"}
        core_skills = {
            "agent-guidelines", "agent-output-standardization", "skill-selection-workflow",
            "documentation-selection-workflow", "technical-documentation-workflow",
        }
        for path in paths:
            with self.subTest(package=path.stem):
                data = installer.load_package(installer.ROOT, path.stem, definitions)
                files = installer.render(installer.ROOT, "missing-suite", package=path.stem)
                includes_core = path.stem != "programming-languages"
                expected = {
                    Path("agents") / f"{name}.agent.md"
                    for name in set(data["agents"]) | (core_agents if includes_core else set())
                }
                self.assertEqual(
                    {relative for relative in files if relative.parts[0] == "agents"},
                    expected,
                )
                for skill in data["skills"]:
                    self.assertIn(Path("skills") / skill / "SKILL.md", files)
                if includes_core:
                    for skill in core_skills:
                        self.assertIn(Path("skills") / skill / "SKILL.md", files)
                    if path.stem != "core":
                        self.assertIn("core", data["depends_on"])
                else:
                    self.assertNotIn("core", data.get("depends_on", []))

    def test_transitive_shared_dependencies_and_dependency_only_packages(self) -> None:
        packages = {
            "root": {"agents": [], "skills": [], "depends_on": ["left", "right"]},
            "left": {"agents": [], "skills": ["unit-test-workflow"], "depends_on": ["core"]},
            "right": {"agents": [], "skills": [], "depends_on": ["core"]},
            "core": {"agents": [], "skills": ["agent-output-standardization"]},
        }
        with patch.object(installer, "load_package", side_effect=lambda root, name, defs: packages[name]) as load:
            result = installer.resolve_package(installer.ROOT, "root", {})
        self.assertEqual(result["skills"], ["agent-output-standardization", "unit-test-workflow"])
        self.assertEqual(load.call_count, 4)

    def test_suite_package_lists_resolve_and_reject_invalid_references(self) -> None:
        definitions = installer.inventory(installer.ROOT)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(installer.ROOT / "schemas", root / "schemas")
            shutil.copytree(installer.ROOT / "src" / "packages", root / "src" / "packages")
            for package in (root / "src" / "packages").glob("*.yaml"):
                for reference in yaml.safe_load(package.read_text(encoding="utf-8")).get("references", []):
                    (root / reference).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(installer.ROOT / reference, root / reference)
            suites = root / "src" / "suites"
            suites.mkdir()
            data = {
                "schema_version": "1.0.0", "name": "example", "version": "0.1.0",
                "description": "Package suite", "packages": ["testing", "core"],
            }
            path = suites / "example.yaml"
            path.write_text(yaml.safe_dump(data), encoding="utf-8")
            collection = installer.load_suite(root, "example", definitions)
            expected = installer.resolve_package(root, "testing", definitions)
            self.assertEqual(collection["agents"], expected["agents"])
            self.assertEqual(collection["skills"], expected["skills"])
            for value in ([], "testing", ["testing", "testing"], ["../testing"], ["missing"]):
                with self.subTest(packages=value):
                    path.write_text(yaml.safe_dump({**data, "packages": value}), encoding="utf-8")
                    with self.assertRaises(installer.InstallError):
                        installer.load_suite(root, "example", definitions)
            errors, _ = validate_repository(root)
            self.assertTrue(any("missing or invalid package 'missing'" in e for e in errors))

    def test_missing_and_cyclic_dependencies_fail_install_and_validation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(installer.ROOT / "schemas", root / "schemas")
            folder = root / "src" / "packages"
            folder.mkdir(parents=True)
            for dependency, message in (("missing", "missing or invalid dependency"), ("example", "cycle")):
                data = {
                    "schema_version": "1.0.0", "name": "example", "version": "0.1.0",
                    "description": "Dependency-only package", "agents": [], "skills": [],
                    "depends_on": [dependency],
                }
                (folder / "example.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
                with self.assertRaises(installer.InstallError):
                    installer.resolve_package(root, "example", {})
                errors, _ = validate_repository(root)
                self.assertTrue(any(message in error for error in errors), errors)

    def test_invalid_package_manifests_are_rejected(self) -> None:
        definitions = installer.inventory(installer.ROOT)
        valid = {
            "schema_version": "1.0.0", "name": "example", "version": "0.1.0",
            "description": "Test package", "agents": [], "skills": ["unit-test-workflow"],
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            folder = root / "src" / "packages"
            folder.mkdir(parents=True)
            path = folder / "example.yaml"
            for data in (
                None, {**valid, "skills": []}, {**valid, "version": "bad"},
                {**valid, "name": "wrong"}, {**valid, "schema_version": "2.0.0"},
                {**valid, "skills": ["missing"]},
                {**valid, "skills": ["unit-test-workflow", "unit-test-workflow"]},
            ):
                with self.subTest(data=data):
                    path.write_text(yaml.safe_dump(data), encoding="utf-8")
                    with self.assertRaises(installer.InstallError):
                        installer.load_package(root, "example", definitions)
            for text in ("name: [broken", "name: example\nname: example\n"):
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(installer.InstallError):
                    installer.load_package(root, "example", definitions)
            path.write_text(yaml.safe_dump({**valid, "future": True}), encoding="utf-8")
            with patch("sys.stderr") as stderr:
                installer.load_package(root, "example", definitions)
            self.assertTrue(stderr.write.called)
        for name in ("missing", "../testing", ""):
            with self.assertRaises(installer.InstallError):
                installer.load_package(installer.ROOT, name, definitions)

    def test_package_rejects_individual_selectors(self) -> None:
        for selection in (
            {"agent": "unit-tester"}, {"skill": "unit-test-workflow"},
            {"skills": ("unit-test-workflow",)},
        ):
            with self.subTest(selection=selection):
                with self.assertRaisesRegex(installer.InstallError, "PACKAGE cannot"):
                    installer.render(installer.ROOT, "engineering", package="testing", **selection)

    def test_cli_package_plan_install_and_repeat_update(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "stage"
            env = {
                **os.environ,
                "PACKAGE": "testing", "SUITE": "missing-suite",
                "AGENT": "", "SKILL": "", "SKILLS": "", "CLIENT": "copilot",
                "LANGUAGE_SKILLS": "include", "SCOPE": "user", "DESTDIR": str(destination),
            }
            for command in ("list", "plan", "install", "install"):
                result = subprocess.run(
                    [sys.executable, "-B", "-m", "scripts.install", command],
                    cwd=installer.ROOT, env=env, text=True, capture_output=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                if command in ("list", "plan"):
                    self.assertFalse(destination.exists())
            manifest = json.loads((destination / installer.MANIFEST).read_text(encoding="utf-8"))
            self.assertIn("agents/unit-tester.agent.md", manifest["files"])
            self.assertIn("agents/source-documentation-writer.agent.md", manifest["files"])
            self.assertIn("agents/technical-documentation-writer.agent.md", manifest["files"])
            self.assertIn("skills/unit-test-workflow/SKILL.md", manifest["files"])
