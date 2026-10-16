"""Dependency-free packaging and rule checks for the senmonka-kun Agent Skill."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "senmonka-kun"
SKILL = SKILL_DIR / "SKILL.md"
REFERENCES = {
    "engineering", "design", "ux", "marketing", "business", "security",
    "documentation", "mechanical-engineering", "manufacturing-engineering", "validation"
}
MANDATORY_RULE = (
    "既存の仕様・決定事項は制約として扱い、より良い代替案を発見した場合は、"
    "根拠と期待効果を示して提案する。承認なしに変更しない。"
)


class SkillPackageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = SKILL.read_text(encoding="utf-8")

    def test_valid_manifest(self):
        match = re.match(r"\A---\n(.*?)\n---\n", self.content, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md must start with YAML frontmatter")
        lines = match.group(1).splitlines()
        fields = dict(
            line.split(": ", 1) for line in lines if ": " in line
        )
        name = fields.get("name")
        description = fields.get("description", "")
        self.assertEqual(name, SKILL_DIR.name)
        self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        self.assertTrue(1 <= len(description) <= 1024)
        self.assertEqual(fields.get("license"), "MIT")

    def test_explicit_decision_rule(self):
        self.assertIn(MANDATORY_RULE, self.content)
        self.assertIn(MANDATORY_RULE, (ROOT / "README.ja.md").read_text(encoding="utf-8"))
        self.assertIn("without explicit authorization", self.content)
        self.assertIn("do not merge, publish, deploy", self.content.lower())

    def test_reference_files_and_links(self):
        for name in REFERENCES:
            file = SKILL_DIR / "references" / f"{name}.md"
            self.assertTrue(file.is_file(), str(file))
            self.assertIn(f"(references/{name}.md)", self.content)
        for target in re.findall(r"\]\((references/[^)#]+)\)", self.content):
            self.assertTrue((SKILL_DIR / target).is_file(), target)

    def test_examples_and_docs(self):
        for filename in (
            "README.md", "README.ja.md", "LICENSE", "tests/scenarios.md",
            "examples/code-review.md", "examples/design-review.md",
            "examples/ux-review.md", "examples/marketing-analysis.md",
            "examples/documentation-creation.md",
            "examples/mechanical-engineering-review.md",
            "examples/manufacturing-engineering-review.md",
        ):
            self.assertTrue((ROOT / filename).is_file(), filename)

    def test_principles_and_modes(self):
        for term in (
            "Altitude", "Depth", "Range", "Validation",
            "Light", "Standard", "Deep", "Never claim a tool, test, review",
        ):
            self.assertIn(term.lower(), self.content.lower())


if __name__ == "__main__":
    unittest.main()
