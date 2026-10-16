"""Test evaluation data, paired scoring and deterministic portable archive."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def load_python(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


REPORT = load_python(ROOT / "tools" / "eval_report.py", "eval_report")
PACKAGE = load_python(ROOT / "tools" / "package_skill.py", "package_skill")


class EvaluationTest(unittest.TestCase):
    def test_valid_case_coverage(self):
        cases = json.loads((ROOT / "evals" / "cases.json").read_text("utf-8"))
        ids = REPORT.load_cases(ROOT / "evals" / "cases.json")
        self.assertGreaterEqual(len(ids), 10)
        self.assertTrue({"engineering", "design", "ux", "marketing", "business",
                         "security", "general"}.issubset({c["domain"] for c in cases["cases"]}))
        self.assertTrue(all(isinstance(c.get("expect_skill"), bool)
                            and c.get("request") and c.get("context") and c.get("pass")
                            for c in cases["cases"]))
        self.assertTrue(any(not c["expect_skill"] for c in cases["cases"]))

    @staticmethod
    def scores(value=2):
        return {name: value for name in REPORT.DIMENSIONS}

    def test_paired_summary_and_critical_gate(self):
        pairs = {"runs": [
            {"case_id": "one", "variant": "baseline", "scores": self.scores()},
            {"case_id": "one", "variant": "skill", "scores": self.scores()},
        ]}
        self.assertIn("gate_pass=1/1", REPORT.report(pairs, ["one"]))
        pairs["runs"][1]["scores"]["decision_integrity"] = 1
        actual = REPORT.report(pairs, ["one"])
        self.assertIn("regressions=1: one", actual)
        self.assertIn("critical_gate_delta=-1 cases", actual)

    def test_missing_or_duplicate_runs_rejected(self):
        runs = {"runs": [{"case_id": "one", "variant": "skill", "scores": self.scores()}]}
        with self.assertRaisesRegex(ValueError, "missing paired results"):
            REPORT.report(runs, ["one"])
        runs["runs"].append(runs["runs"][0])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            REPORT.report(runs, ["one"])

    def test_bad_scores_rejected(self):
        for value in (3, -1, 1.5, True):
            runs = {"runs": [
                {"case_id": "one", "variant": variant, "scores": self.scores(value)}
                for variant in ("baseline", "skill")
            ]}
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "scores"):
                REPORT.report(runs, ["one"])


class PackagingTest(unittest.TestCase):
    def test_archive_is_portable_and_deterministic(self):
        with tempfile.TemporaryDirectory() as d:
            a = Path(d) / "first.zip"
            b = Path(d) / "second.zip"
            names = PACKAGE.package(a)
            PACKAGE.package(b)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            self.assertIn("senmonka-kun/SKILL.md", names)
            self.assertIn("senmonka-kun/references/validation.md", names)
            with ZipFile(a) as z:
                self.assertEqual(z.namelist(), names)
                self.assertTrue(all(n.startswith("senmonka-kun/") for n in names))
                self.assertIn(b"name: senmonka-kun", z.read("senmonka-kun/SKILL.md"))


if __name__ == "__main__":
    unittest.main()
