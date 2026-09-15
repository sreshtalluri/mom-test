"""Exercise the real installer in isolated checkouts; no agent or packages needed."""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "checkout with spaces"
        self.repo.mkdir()
        shutil.copy2(ROOT / "install.sh", self.repo / "install.sh")
        shutil.copytree(ROOT / "skills", self.repo / "skills")
        self.dest = Path(self.temp.name) / "installed skills"

    def run_installer(self, *args):
        return subprocess.run(
            ["sh", str(self.repo / "install.sh"), "--dir", str(self.dest), *args],
            capture_output=True, text=True,
        )

    def test_install_repeat_and_uninstall(self):
        for _ in range(2):
            result = self.run_installer()
            self.assertEqual(result.returncode, 0, result.stderr)
        skills = list((self.repo / "skills").iterdir())
        self.assertEqual(len(list(self.dest.iterdir())), len(skills))
        for skill in skills:
            self.assertEqual((self.dest / skill.name).resolve(), skill.resolve())
            self.assertFalse((skill / skill.name).exists(), "nested link created")
        self.assertEqual(self.run_installer("--uninstall").returncode, 0)
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_foreign_paths_are_preserved_on_install_and_uninstall(self):
        for kind in ("file", "directory", "symlink", "broken symlink"):
            with self.subTest(kind=kind):
                self.dest.mkdir(exist_ok=True)
                path = self.dest / "mom-test-roleplay"
                if kind == "file":
                    path.write_text("keep me")
                elif kind == "directory":
                    path.mkdir()
                    (path / "keep.txt").write_text("keep me")
                else:
                    path.symlink_to(self.repo if kind == "symlink" else self.repo / "missing")
                result = self.run_installer()
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("unrelated path", result.stderr)
                self.assertEqual(list(self.dest.iterdir()), [path], "partial install")
                self.assertEqual(self.run_installer("--uninstall").returncode, 0)
                self.assertTrue(path.exists() or path.is_symlink())
                if kind == "directory":
                    self.assertEqual((path / "keep.txt").read_text(), "keep me")
                    shutil.rmtree(path)
                else:
                    if kind == "file":
                        self.assertEqual(path.read_text(), "keep me")
                    path.unlink()

    def test_invalid_frontmatter_fails_before_installing_anything(self):
        skill = self.repo / "skills/mom-test-roleplay/SKILL.md"
        skill.write_text(skill.read_text().replace("name: mom-test-roleplay", "name: wrong"))
        self.assertNotEqual(self.run_installer().returncode, 0)
        self.assertFalse(self.dest.exists())

    def test_missing_directory_argument_has_actionable_error(self):
        result = self.run_installer("--dir")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires a directory path", result.stderr)
        self.assertFalse(self.dest.exists())

    def test_uninstall_without_install_creates_nothing(self):
        self.assertEqual(self.run_installer("--uninstall").returncode, 0)
        self.assertFalse(self.dest.exists())


if __name__ == "__main__":
    unittest.main()
