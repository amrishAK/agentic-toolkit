from __future__ import annotations

import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import utils


class UtilityTests(unittest.TestCase):
    def test_digest(self) -> None:
        self.assertEqual(utils.digest(b"example"), hashlib.sha256(b"example").hexdigest())

    def test_metadata_validation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.md"
            for content, expected in [
                ("# Plain document", {}),
                ('---\nname: example\ndescription: "Example"\n---\nBody',
                 {"name": "example", "description": '"Example"'}),
            ]:
                path.write_text(content, encoding="utf-8")
                self.assertEqual(utils.metadata(path), expected)
            for content in [
                "---\nname: example\n",
                "---\nname: other\ndescription: Example\n---\n",
                "---\nname: example\n---\n",
            ]:
                path.write_text(content, encoding="utf-8")
                with self.subTest(content=content):
                    with self.assertRaises(utils.InstallError):
                        utils.metadata(path)

    def test_links_preserve_suffixes_and_ignore_examples(self) -> None:
        text = "[real](target%20file.md?mode=read#section)\n`[example](missing.md)`"
        matches = list(utils.markdown_links(text))
        self.assertEqual(len(matches), 1)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            target = root / "target file.md"
            target.write_bytes(b"content")
            self.assertEqual(
                utils.local_link(root / "source.md", matches[0][2], root),
                (target, "?mode=read#section"),
            )
            self.assertIsNone(utils.local_link(root / "source.md", "https://example.com", root))
            self.assertIsNone(utils.local_link(root / "source.md", "#section", root))
            with self.assertRaises(utils.InstallError):
                utils.local_link(root / "source.md", "../outside.md", root)

    def test_safe_relative_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            relative = Path("nested") / "file.md"
            self.assertEqual(utils.safe_path(root, relative), root / relative)
            for unsafe in [Path("."), Path("..") / "escape", root.resolve() / "absolute"]:
                with self.subTest(unsafe=unsafe):
                    with self.assertRaises(utils.InstallError):
                        utils.safe_path(root, unsafe)

    def test_atomic_write_and_failure_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "nested" / "file.md"
            utils.atomic_write(target, b"original")
            self.assertEqual(target.read_bytes(), b"original")
            with patch("scripts.utils.os.replace", side_effect=OSError("replacement failed")):
                with self.assertRaisesRegex(OSError, "replacement failed"):
                    utils.atomic_write(target, b"replacement")
            self.assertEqual(target.read_bytes(), b"original")
            self.assertEqual(list(target.parent.iterdir()), [target])
            utils.atomic_write(target, b"updated")
            self.assertEqual(target.read_bytes(), b"updated")


if __name__ == "__main__":
    unittest.main()
