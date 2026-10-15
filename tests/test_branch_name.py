"""Exercise branch names accepted and rejected by the required CI check."""

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_branch_name.py"


class BranchNameTests(unittest.TestCase):
    def check_branch(self, branch: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), branch], capture_output=True, text=True
        )

    def test_issue_branches_and_documented_exceptions(self) -> None:
        for branch in (
            "feat/1-booking", "fix/23-timezone-conversion", "docs/12-readme",
            "perf/5-availability", "build/9-dependencies", "refactor/8-calendar",
            "test/6-conflicts", "ci/7-checks", "chore/2-bootstrap", "revert/4-change",
            "main", "dependabot/github_actions/checkout-7", "release-please--branches--main",
        ):
            with self.subTest(branch=branch):
                result = self.check_branch(branch)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_missing_issue_invalid_type_and_malformed_slug(self) -> None:
        for branch in (
            "feature/1-booking", "feat/booking", "feat/0-booking", "feat/01-booking",
            "feat/1-Booking", "feat/1-booking_appointment", "feat/1-booking--flow",
            "feat/1-booking-", "main-extra", "dependabot/", "release-please--", "",
        ):
            with self.subTest(branch=branch):
                result = self.check_branch(branch)
                self.assertEqual(result.returncode, 1)
                self.assertIn("does not follow <type>/<issue>-<slug>", result.stderr)


if __name__ == "__main__":
    unittest.main()
