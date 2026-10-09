"""Tests for scripts/validate_trace.py — the traceability gate for insights and calendars."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "validate_trace.py"
FIX = ROOT / "tests" / "fixtures"


def run(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *map(str, args)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


class InsightSchemaTest(unittest.TestCase):
    def test_valid_insights_pass(self):
        result = run("--insights", FIX / "insights-valid.csv")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_invalid_insights_report_each_problem(self):
        result = run("--insights", FIX / "insights-invalid.csv")
        self.assertEqual(result.returncode, 1)
        out = result.stdout
        self.assertIn("product_line", out)
        self.assertIn("source_url", out)
        self.assertIn("observation", out)
        self.assertIn("tags", out)
        self.assertIn("bad-id", out)
        self.assertIn("channel", out)
        self.assertIn("source_mode", out)

    def test_duplicate_insight_id_across_files_fails(self):
        result = run("--insights", FIX / "insights-valid.csv", FIX / "insights-valid.csv")
        self.assertEqual(result.returncode, 1)
        self.assertIn("trùng", result.stdout)


class CalendarTraceTest(unittest.TestCase):
    def test_valid_calendar_passes(self):
        result = run(
            "--calendar", FIX / "calendar-valid.csv",
            "--insights", FIX / "insights-valid.csv",
            "--strategy", FIX / "strategy-approved.txt",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_draft_strategy_blocks_calendar(self):
        result = run(
            "--calendar", FIX / "calendar-valid.csv",
            "--insights", FIX / "insights-valid.csv",
            "--strategy", FIX / "strategy-draft.txt",
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("approved", result.stdout)

    def test_every_untraceable_row_is_rejected_by_cal_id(self):
        result = run(
            "--calendar", FIX / "calendar-invalid.csv",
            "--insights", FIX / "insights-valid.csv",
            "--strategy", FIX / "strategy-approved.txt",
        )
        self.assertEqual(result.returncode, 1)
        out = result.stdout
        # fake insight id
        self.assertIn("CAL-2026-W42-01", out)
        self.assertIn("INS-20990101-000000-99", out)
        # pillar belongs to another product line
        self.assertIn("CAL-2026-W42-02", out)
        # pillar missing from strategy
        self.assertIn("CAL-2026-W42-03", out)
        # insight marked as duplicate
        self.assertIn("CAL-2026-W42-04", out)
        # no insight at all
        self.assertIn("CAL-2026-W42-05", out)

    def test_rejected_ids_listed_in_machine_readable_line(self):
        result = run(
            "--calendar", FIX / "calendar-invalid.csv",
            "--insights", FIX / "insights-valid.csv",
            "--strategy", FIX / "strategy-approved.txt",
        )
        line = next(l for l in result.stdout.splitlines() if l.startswith("REJECTED:"))
        rejected = set(line.split(":", 1)[1].strip().split(","))
        self.assertEqual(rejected, {f"CAL-2026-W42-0{i}" for i in range(1, 6)})


class ContractStrictnessTest(unittest.TestCase):
    def test_loose_insight_values_are_rejected(self):
        result = run("--insights", FIX / "insights-loose.csv")
        self.assertEqual(result.returncode, 1)
        out = result.stdout
        self.assertNotIn("Traceback", result.stderr)
        self.assertIn("run_id", out)          # prefix mismatch with insight_id
        self.assertIn("captured_at", out)     # "yesterday"
        self.assertIn("source_url", out)      # "httpfoo"
        self.assertIn("300", out)             # evidence too long
        self.assertIn("dup_of", out)          # "not-an-id"
        self.assertIn("-00", out)             # NN must start at 01
        self.assertIn("thiếu", out)           # short row handled, no crash

    def test_loose_calendar_rows_are_rejected(self):
        result = run(
            "--calendar", FIX / "calendar-loose.csv",
            "--insights", FIX / "insights-valid.csv",
            "--strategy", FIX / "strategy-approved.txt",
        )
        line = next(l for l in result.stdout.splitlines() if l.startswith("REJECTED:"))
        rejected = line.split(":", 1)[1].strip().split(",")
        self.assertEqual(result.returncode, 1)
        self.assertIn("CAL-2026-W42-01", rejected)   # same insight twice
        self.assertIn("CAL-2026-W42-02", rejected)   # email insight on hosting row, duplicate cal_id
        self.assertIn("CAL-2026-W42-04", rejected)   # date outside week
        self.assertIn("CAL-2026-W42-05", rejected)   # empty product_line
        self.assertIn("trùng cal_id", result.stdout)


class StrategyParsingTest(unittest.TestCase):
    def test_human_edited_strategy_is_parsed(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import validate_trace as v
        for name in ("strategy-human-edited.txt", "strategy-nfd.txt"):
            status, pillars, warnings = v.read_strategy(FIX / name)
            self.assertEqual(status, "approved", name)
            self.assertEqual(pillars.get("P-HOSTING-01"), "hosting", name)
            self.assertTrue(any("P-EMAIL-01" in w for w in warnings), name)

    def test_instruction_text_does_not_count_as_approval(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import validate_trace as v
        status, _, _ = v.read_strategy(FIX / "strategy-instruction-only.txt")
        self.assertEqual(status, "draft")


class SheetSafeOutputTest(unittest.TestCase):
    def test_formula_like_cells_are_neutralised(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import validate_trace as v
        self.assertEqual(v.sheet_safe("=IMPORTXML(1)"), "'=IMPORTXML(1)")
        self.assertEqual(v.sheet_safe("+84901"), "'+84901")
        self.assertEqual(v.sheet_safe("-50% phí"), "'-50% phí")
        self.assertEqual(v.sheet_safe("@redsun"), "'@redsun")
        self.assertEqual(v.sheet_safe("0800"), "'0800")
        self.assertEqual(v.sheet_safe("Bình thường"), "Bình thường")
        self.assertEqual(v.sheet_safe(""), "")

    def test_sheet_safe_out_writes_neutralised_csv(self):
        import csv
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "safe.csv"
            result = run("--insights", FIX / "insights-valid.csv", "--sheet-safe-out", out)
            self.assertEqual(result.returncode, 0, result.stdout)
            with open(out, encoding="utf-8") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[0]["insight_id"], "INS-20261005-080000-01")


class CalendarExitCodeTest(unittest.TestCase):
    def test_old_insight_errors_do_not_fail_clean_calendar(self):
        result = run(
            "--calendar", FIX / "calendar-valid.csv",
            "--insights", FIX / "insights-valid.csv", FIX / "insights-invalid.csv",
            "--strategy", FIX / "strategy-approved.txt",
        )
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("INSIGHT_WARNINGS", result.stdout)


if __name__ == "__main__":
    unittest.main()
