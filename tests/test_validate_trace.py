"""Tests for scripts/validate_trace.py against the Research database workbook contract."""

import base64
import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "validate_trace.py"
TEMPLATES = ROOT / "templates" / "sheet"
sys.path.insert(0, str(ROOT / "tests"))
sys.path.insert(0, str(ROOT / "scripts"))

from xlsx_builder import build_xlsx  # noqa: E402
import validate_trace as vt  # noqa: E402

TAB_FILES = {
    "Hướng dẫn": "1-huong-dan.csv",
    "Nguồn theo dõi": "2-nguon-theo-doi.csv",
    "Chiến lược content": "3-chien-luoc-content.csv",
    "Insight hằng ngày": "4-insight-hang-ngay.csv",
    "Research database": "5-research-database.csv",
    "Digest": "6-digest.csv",
    "Content Calendar": "7-content-calendar.csv",
}

INSIGHT = ["2026-10-08", "SIPOS", "Quảng cáo Meta", "KiotViet", "offer",
           "Tặng máy quét mã vạch khi đăng ký 2 năm", "", "mới",
           "https://www.facebook.com/ads/library/?country=VN&q=KiotViet"]
OB1 = ["OB001", "2026-10-08", "2026-10-09", "2", "SIPOS", "KiotViet",
       "KiotViet cạnh tranh bằng ưu đãi phần cứng", "Quảng cáo: tặng máy quét mã vạch",
       "https://www.facebook.com/ads/library/?country=VN&q=KiotViet",
       "Đối thủ giảm rào cản đầu tư ban đầu", "vừa", "So sánh tổng chi phí một năm", "gợi ý, chờ người duyệt"]
OB2 = ["OB002", "2026-10-09", "2026-10-09", "1", "WEBINO", "Haravan",
       "Haravan quảng cáo AI website", "Quảng cáo Meta", "https://www.haravan.com/",
       "Khách quan tâm AI", "thấp (nhà bán tự nhận)", "Website AI làm được gì", "gợi ý, chờ người duyệt"]
OB3_MOC = ["OB003", "2026-10-08", "2026-10-08", "1", "SIPOS", "SIPOS",
           "Facebook SIPOS 143 người theo dõi", "Fanpage", "https://www.facebook.com/sipos.vn/",
           "", "", "", "mốc"]


def template_tabs(extra=None):
    tabs = {}
    for title, name in TAB_FILES.items():
        with open(TEMPLATES / name, encoding="utf-8") as f:
            tabs[title] = list(csv.reader(f))
    for title, rows in (extra or {}).items():
        tabs[title] = tabs[title] + rows
    return tabs


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                          capture_output=True, text=True, encoding="utf-8")


def write_draft(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(vt.CALENDAR_KEYS)
        w.writerows(rows)


def cal(cid, day, product, pillar, obs, status="đề xuất, chờ duyệt", week="2026-W42"):
    return [cid, week, day, "Facebook", product, pillar, obs, "Góc từ content idea",
            "bài viết", "Nhắn tin", "", status]


class WorkbookTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def workbook(self, extra=None, tabs=None):
        path = self.dir / "wb.xlsx"
        build_xlsx(path, tabs or template_tabs(extra))
        return path


class TemplateTest(WorkbookTest):
    def test_fresh_template_is_valid(self):
        result = run("--workbook", self.workbook())
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_template_has_approved_pillars_for_sipos_and_webino(self):
        _, recs = vt.as_records(template_tabs()["Chiến lược content"])
        approved = {r["san_pham"] for r in recs if r["trang_thai"] == "đã duyệt"}
        self.assertTrue({"SIPOS", "WEBINO"} <= approved)

    def test_tool_result_json_is_accepted(self):
        xlsx = self.workbook()
        wrapped = self.dir / "result.txt"
        wrapped.write_text(json.dumps({"content": base64.b64encode(xlsx.read_bytes()).decode()}))
        result = run("--workbook", wrapped)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class DataCheckTest(WorkbookTest):
    def test_valid_rows_pass(self):
        wb = self.workbook({"Insight hằng ngày": [INSIGHT], "Research database": [OB1, OB2, OB3_MOC]})
        result = run("--workbook", wb)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_sheets_date_serials_and_float_counts_are_accepted(self):
        serial_insight = ["46303.0"] + INSIGHT[1:]
        serial_ob = OB1[:1] + ["46303", "46304.0", "2.0"] + OB1[4:]
        wb = self.workbook({"Insight hằng ngày": [serial_insight], "Research database": [serial_ob]})
        result = run("--workbook", wb)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(vt.normalize_date("46303.0"), "2026-10-08")

    def test_contract_violations_are_reported(self):
        bad_insight = ["08/10/2026", "SIPOS", "Zalo", "KiotViet", "giam_gia", "x" * 300, "", "hot", "kiotviet.vn"]
        bad_ob = ["OB1", "2026-10-09", "2026-10-08", "0", "SIPOS", "KiotViet", "", "", "ftp://x",
                  "", "chắc chắn", "", "đã chốt"]
        wb = self.workbook({"Insight hằng ngày": [bad_insight], "Research database": [OB1, OB1, bad_ob]})
        out = run("--workbook", wb).stdout
        for needle in ("YYYY-MM-DD", "kênh 'Zalo'", "giam_gia", "tối đa 250", "nhãn 'hot'",
                       "http(s)", "OB001 bị trùng", "phải dạng OB001", "sớm hơn",
                       "số nguyên", "cao / vừa / thấp", "trạng thái 'đã chốt'"):
            self.assertIn(needle, out)

    def test_missing_calendar_tab_is_reported(self):
        tabs = template_tabs()
        del tabs["Content Calendar"]
        result = run("--workbook", self.workbook(tabs=tabs))
        self.assertEqual(result.returncode, 1)
        self.assertIn("Content Calendar", result.stdout)


class CalendarTest(WorkbookTest):
    def setUp(self):
        super().setUp()
        self.wb = self.workbook({"Research database": [OB1, OB2, OB3_MOC]})
        self.draft = self.dir / "draft.csv"
        self.clean = self.dir / "clean.json"

    def test_traceable_rows_are_kept_and_written_sheet_safe(self):
        write_draft(self.draft, [
            cal("CAL-2026-W42-01", "2026-10-12", "SIPOS", "S3.1", "OB001"),
            cal("CAL-2026-W42-02", "2026-10-13", "WEBINO", "W2", "OB002"),
        ])
        result = run("--workbook", self.wb, "--calendar-draft", self.draft,
                     "--products", "SIPOS,WEBINO", "--clean-out", self.clean)
        self.assertEqual(result.returncode, 0, result.stdout)
        rows = json.loads(self.clean.read_text(encoding="utf-8"))
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0][0], "'CAL-2026-W42-01")
        self.assertEqual(rows[0][2], "'2026-10-12")

    def test_untraceable_rows_are_rejected_with_reasons(self):
        write_draft(self.draft, [
            cal("CAL-2026-W42-01", "2026-10-12", "SIPOS", "S3.1", "OB999"),   # fake observation
            cal("CAL-2026-W42-02", "2026-10-12", "SIPOS", "W2", "OB001"),     # pillar of other product
            cal("CAL-2026-W42-03", "2026-10-12", "SIPOS", "R-?", "OB001"),    # draft pillar
            cal("CAL-2026-W42-04", "2026-10-12", "SIPOS", "S3.1", "OB002"),   # observation of WEBINO
            cal("CAL-2026-W42-05", "2026-10-12", "SIPOS", "S3.1", "OB003"),   # brand milestone
            cal("CAL-2026-W42-06", "2026-10-17", "SIPOS", "S3.1", "OB001"),   # Saturday
            cal("CAL-2026-W42-07", "2026-10-12", "SIPOS", "S3.1", ""),        # no observation
            cal("CAL-2026-W42-08", "2026-10-12", "SIPOS", "TỶ LỆ", "OB001"),  # info row, not a pillar
            cal("CAL-2026-W42-09", "2026-10-12", "SIPOS", "S3.1", "OB001", status="đã duyệt"),
            cal("CAL-2026-W42-01", "2026-10-13", "SIPOS", "S3.1", "OB001"),   # duplicate id
        ])
        result = run("--workbook", self.wb, "--calendar-draft", self.draft, "--clean-out", self.clean)
        self.assertEqual(result.returncode, 1)
        line = next(l for l in result.stdout.splitlines() if l.startswith("REJECTED:"))
        self.assertEqual(len(line.split(":", 1)[1].split(",")), 10)
        for needle in ("OB999 không có", "thuộc WEBINO", "chưa được duyệt", "đang 'mốc'",
                       "thứ Hai–thứ Sáu", "không có mã quan sát", "trùng mã lịch", "đề xuất, chờ duyệt"):
            self.assertIn(needle, result.stdout)
        self.assertEqual(json.loads(self.clean.read_text(encoding="utf-8")), [])

    def test_product_without_approved_pillar_stops_with_exit_2(self):
        write_draft(self.draft, [])
        result = run("--workbook", self.wb, "--calendar-draft", self.draft, "--products", "REDSUN BOS")
        self.assertEqual(result.returncode, 2)
        self.assertIn("REDSUN BOS", result.stdout)


class SheetSafeTest(unittest.TestCase):
    def test_every_value_gets_a_text_marker(self):
        self.assertEqual(vt.sheet_safe("=1+1"), "'=1+1")
        self.assertEqual(vt.sheet_safe("0800"), "'0800")
        self.assertEqual(vt.sheet_safe("2026-10-12"), "'2026-10-12")
        self.assertEqual(vt.sheet_safe(""), "")


if __name__ == "__main__":
    unittest.main()
