"""Documentation-contract tests for the CALCULA design-artifact repository.

This suite checks document integrity and evidence labeling only. It does not
verify a runtime, agent execution, payment protocol, or empirical scientific law.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CalculaDocumentationContractTests(unittest.TestCase):
    def test_design_artifact_documents_and_license_are_present(self) -> None:
        for relative in (
            "README.md",
            "ROADMAP.md",
            "WHITEPAPER.md",
            "ESSAYS.md",
            "ATTRIBUTION.md",
            "LICENSE",
        ):
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file(), f"missing design artifact: {relative}")

    def test_readme_distinguishes_design_from_implementation(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        self.assertIn("research and design package", readme)
        self.assertIn("does not contain an executable calcula engine", readme)
        self.assertIn("not independently validated scientific law", readme)
        self.assertIn("not evidence of a live payment protocol", readme)

    def test_roadmap_labels_legacy_status_as_unverified(self) -> None:
        roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8").lower()
        self.assertIn("historical status snapshot", roadmap)
        self.assertIn("not verified against the current repository", roadmap)
        self.assertIn("not verified implementation evidence", roadmap)
        self.assertIn("repeatable ci evidence", roadmap)

    def test_documented_evaluation_weights_sum_to_one_hundred(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        rows = re.findall(
            r"^\|\s*(Flourishing|Harm Reduction|Equity|Regenerative Capacity|Cooperation|Beauty)\s*\|\s*(\d+)%\s*\|$",
            readme,
            re.MULTILINE,
        )
        weights = {name: int(weight) for name, weight in rows}
        self.assertEqual(
            weights,
            {
                "Flourishing": 25,
                "Harm Reduction": 20,
                "Equity": 20,
                "Regenerative Capacity": 15,
                "Cooperation": 12,
                "Beauty": 8,
            },
        )
        self.assertEqual(sum(weights.values()), 100)

    def test_attribution_preserves_openclaw_credit(self) -> None:
        attribution = (ROOT / "ATTRIBUTION.md").read_text(encoding="utf-8").lower()
        self.assertIn("openclaw", attribution)
        self.assertIn("https://github.com/openclaw", attribution)


if __name__ == "__main__":
    unittest.main()
