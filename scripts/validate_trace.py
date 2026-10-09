#!/usr/bin/env python3
"""Traceability gate for the Redsun MKT "Research database" Google Sheet.

Reads the workbook exported from Google Drive as .xlsx (or the JSON result file a
Drive download tool saved, whose "content" field holds the base64 xlsx) and checks
it against shared/data-contract.md. For the weekly calendar it validates a draft
CSV row by row against Research database and Chiến lược content, and writes the
valid rows as a JSON 2D array ready for the Sheets connector's update_values.

Standard library only, so it runs in Claude Code and Cowork without installs.

Exit codes: 0 = clean, 1 = rows failed / were rejected,
            2 = a product to plan for has no approved pillar.
"""

import argparse
import base64
import csv
import datetime as dt
import io
import json
import re
import sys
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

TAB_INSIGHTS = "Insight hằng ngày"
TAB_DB = "Research database"
TAB_STRATEGY = "Chiến lược content"
TAB_SOURCES = "Nguồn theo dõi"
TAB_DIGEST = "Digest"
TAB_CALENDAR = "Content Calendar"

KENH = {"Facebook", "Facebook Groups", "Quảng cáo Meta", "TikTok", "YouTube",
        "Website blog", "Tìm kiếm web", "Google Trends"}
TRUONG = {"chu_de", "tu_khoa", "execution", "offer", "cta", "pain", "pattern"}
DB_STATUSES = {"", "gợi ý, chờ người duyệt", "đã duyệt", "bỏ", "mốc"}
STRATEGY_STATUSES = {"đã duyệt", "nháp", "thông tin"}
CALENDAR_STATUS = "đề xuất, chờ duyệt"
MAX_INSIGHT_CHARS = 250
MAX_OBS_PER_ROW = 3

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
OB_RE = re.compile(r"^OB\d{3,}$")
CAL_RE = re.compile(r"^CAL-(\d{4})-W(\d{2})-\d{2}$")
WEEK_RE = re.compile(r"^(\d{4})-W(\d{2})$")
URL_RE = re.compile(r"^https?://\S+")
NHAN_RE = re.compile(r"^(mới|lặp lại \(lần \d+\)|mốc)(\s*;.*)?$")
TRUST_RE = re.compile(r"^(cao|vừa|thấp)\b")
KEY_RE = re.compile(r"\(([a-z_]+)\)\s*$")
SHEET_FORMULA_PREFIXES = ("=", "+", "-", "@")

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}


# ---------------------------------------------------------------- workbook io

def _norm(text):
    return unicodedata.normalize("NFC", text or "").strip()


def _col_index(ref):
    n = 0
    for ch in re.match(r"[A-Z]+", ref).group():
        n = n * 26 + ord(ch) - 64
    return n - 1


def _xlsx_bytes(path):
    raw = Path(path).read_bytes()
    if raw[:2] == b"PK":
        return raw
    # A tool-result file: {"content": "<base64 xlsx>", ...}
    return base64.b64decode(json.loads(raw.decode("utf-8"))["content"])


def load_workbook(path):
    """Return {tab title: [rows as lists of str]} for every tab."""
    z = zipfile.ZipFile(io.BytesIO(_xlsx_bytes(path)))
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter(f"{{{NS['m']}}}t")))
    rels = {r.get("Id"): r.get("Target")
            for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    tabs = {}
    for sheet in ET.fromstring(z.read("xl/workbook.xml")).find("m:sheets", NS):
        target = rels[sheet.get(f"{{{NS['r']}}}id")].lstrip("/")
        target = target if target.startswith("xl/") else "xl/" + target
        rows = []
        for row in ET.fromstring(z.read(target)).iter(f"{{{NS['m']}}}row"):
            cells = {}
            for c in row.findall("m:c", NS):
                v, kind = c.find("m:v", NS), c.get("t")
                if kind == "s" and v is not None:
                    val = shared[int(v.text)]
                elif kind == "inlineStr":
                    val = "".join(t.text or "" for t in c.iter(f"{{{NS['m']}}}t"))
                else:
                    val = v.text if v is not None else ""
                cells[_col_index(c.get("r"))] = _norm(val)
            if cells:
                rows.append([cells.get(i, "") for i in range(max(cells) + 1)])
        tabs[_norm(sheet.get("name"))] = rows
    return tabs


def normalize_date(value):
    """Accept text YYYY-MM-DD or a Sheets date serial (e.g. 46303.0 = 2026-10-08)."""
    if re.fullmatch(r"\d{5}(\.0+)?", value or ""):
        return (dt.date(1899, 12, 30) + dt.timedelta(days=int(float(value)))).isoformat()
    return value


def normalize_int(value):
    return value[:-2] if re.fullmatch(r"\d+\.0", value or "") else value


DATE_KEYS = {"ngay", "ngay_dau", "ngay_gan_nhat", "ngay_dang"}


def header_key(label):
    m = KEY_RE.search(_norm(label))
    return m.group(1) if m else _norm(label)


def as_records(rows):
    """First row is the header; return (keys, [dict]) skipping fully blank rows."""
    if not rows:
        return [], []
    keys = [header_key(h) for h in rows[0]]
    records = []
    for n, row in enumerate(rows[1:], start=2):
        if not any(c.strip() for c in row):
            continue
        rec = {k: (row[i] if i < len(row) else "").strip() for i, k in enumerate(keys) if k}
        for k in DATE_KEYS & rec.keys():
            rec[k] = normalize_date(rec[k])
        if "so_lan_thay" in rec:
            rec["so_lan_thay"] = normalize_int(rec["so_lan_thay"])
        rec["_row"] = n
        records.append(rec)
    return keys, records


def sheet_safe(value):
    """Text for update_values: a leading apostrophe keeps it literal in Sheets."""
    value = "" if value is None else str(value)
    return "'" + value if value else value


# ---------------------------------------------------------------- data checks

def require_tab(tabs, name, errors):
    if name not in tabs:
        errors.append(f"thiếu tab '{name}'")
        return None
    return tabs[name]


def require_columns(tab, keys, expected, errors):
    missing = [k for k in expected if k not in keys]
    if missing:
        errors.append(f"{tab}: thiếu cột {', '.join(missing)}")
    return not missing


def valid_kenh(value):
    parts = [p.strip() for p in value.split("+") if p.strip()]
    return bool(parts) and all(p in KENH for p in parts)


def check_insights(tabs, errors):
    rows = require_tab(tabs, TAB_INSIGHTS, errors)
    if rows is None:
        return
    keys, recs = as_records(rows)
    need = ["ngay", "san_pham", "kenh", "doi_thu", "truong", "insight", "tin_hieu", "nhan", "url"]
    if not require_columns(TAB_INSIGHTS, keys, need, errors):
        return
    for r in recs:
        at = f"{TAB_INSIGHTS} dòng {r['_row']}"
        for k in ("ngay", "san_pham", "kenh", "truong", "insight", "nhan", "url"):
            if not r[k]:
                errors.append(f"{at}: cột {k} trống")
        if r["ngay"] and not DATE_RE.match(r["ngay"]):
            errors.append(f"{at}: ngày '{r['ngay']}' phải dạng YYYY-MM-DD")
        if r["kenh"] and not valid_kenh(r["kenh"]):
            errors.append(f"{at}: kênh '{r['kenh']}' không thuộc danh sách")
        if r["truong"] and r["truong"] not in TRUONG:
            errors.append(f"{at}: loại thông tin '{r['truong']}' không hợp lệ")
        if len(r["insight"]) > MAX_INSIGHT_CHARS:
            errors.append(f"{at}: insight dài {len(r['insight'])} ký tự (tối đa {MAX_INSIGHT_CHARS})")
        if r["nhan"] and not NHAN_RE.match(r["nhan"]):
            errors.append(f"{at}: nhãn '{r['nhan']}' phải bắt đầu bằng mới / lặp lại (lần N) / mốc")
        if r["url"] and not URL_RE.match(r["url"]):
            errors.append(f"{at}: URL phải bắt đầu bằng http(s)://")


def load_observations(tabs, errors):
    """Return {OB id: record}. Errors are added for every contract violation."""
    rows = require_tab(tabs, TAB_DB, errors)
    if rows is None:
        return {}
    keys, recs = as_records(rows)
    need = ["id", "ngay_dau", "ngay_gan_nhat", "so_lan_thay", "san_pham", "doi_thu", "quan_sat",
            "can_cu", "url", "y_nghia", "do_tin_cay", "content_idea", "trang_thai"]
    if not require_columns(TAB_DB, keys, need, errors):
        return {}
    obs = {}
    for r in recs:
        at = f"{TAB_DB} dòng {r['_row']}"
        oid = r["id"]
        if not OB_RE.match(oid):
            errors.append(f"{at}: mã '{oid}' phải dạng OB001")
        elif oid in obs:
            errors.append(f"{at}: mã {oid} bị trùng")
            continue
        for k in ("ngay_dau", "ngay_gan_nhat"):
            if not DATE_RE.match(r[k]):
                errors.append(f"{at}: {k} '{r[k]}' phải dạng YYYY-MM-DD")
        if DATE_RE.match(r["ngay_dau"]) and DATE_RE.match(r["ngay_gan_nhat"]) \
                and r["ngay_gan_nhat"] < r["ngay_dau"]:
            errors.append(f"{at}: ngày thấy gần nhất sớm hơn ngày đầu thấy")
        if not re.fullmatch(r"[1-9]\d*", r["so_lan_thay"]):
            errors.append(f"{at}: số lần thấy '{r['so_lan_thay']}' phải là số nguyên ≥ 1")
        required = ["san_pham", "quan_sat", "can_cu", "url"]
        if r["trang_thai"] != "mốc":
            required += ["y_nghia", "do_tin_cay", "content_idea"]
        for k in required:
            if not r[k]:
                errors.append(f"{at}: cột {k} trống")
        if r["url"] and not URL_RE.match(r["url"]):
            errors.append(f"{at}: URL phải bắt đầu bằng http(s)://")
        if r["do_tin_cay"] and not TRUST_RE.match(r["do_tin_cay"]):
            errors.append(f"{at}: độ tin cậy phải bắt đầu bằng cao / vừa / thấp")
        if r["trang_thai"] not in DB_STATUSES:
            errors.append(f"{at}: trạng thái '{r['trang_thai']}' không hợp lệ")
        obs[oid] = r
    return obs


def load_pillars(tabs, errors):
    """Return {code: record} for every strategy row, plus status problems."""
    rows = require_tab(tabs, TAB_STRATEGY, errors)
    if rows is None:
        return {}
    keys, recs = as_records(rows)
    if not require_columns(TAB_STRATEGY, keys, ["ma", "san_pham", "tru_cot", "trang_thai"], errors):
        return {}
    pillars = {}
    for r in recs:
        at = f"{TAB_STRATEGY} dòng {r['_row']}"
        status = r["trang_thai"].lower()
        if status not in STRATEGY_STATUSES:
            errors.append(f"{at}: trạng thái '{r['trang_thai']}' phải là đã duyệt / nháp / thông tin")
        if r["ma"] in pillars:
            errors.append(f"{at}: mã {r['ma']} bị trùng, dùng dòng đầu tiên")
            continue
        r["trang_thai"] = status
        pillars[r["ma"]] = r
    return pillars


def check_calendar_tab(tabs, errors):
    rows = tabs.get(TAB_CALENDAR)
    if rows is None:
        errors.append(f"thiếu tab '{TAB_CALENDAR}'")


# ---------------------------------------------------------------- calendar

def week_bounds(week):
    m = WEEK_RE.match(week)
    if not m:
        return None
    try:
        monday = dt.date.fromisocalendar(int(m.group(1)), int(m.group(2)), 1)
    except ValueError:
        return None
    return monday, monday + dt.timedelta(days=4)  # posting days: Monday–Friday


def split_ids(value):
    return [v.strip() for v in re.split(r"[;,|]", value or "") if v.strip()]


def check_calendar_row(r, obs, pillars, seen):
    errs = []
    if not CAL_RE.match(r.get("ma_lich", "")):
        errs.append("mã lịch phải dạng CAL-YYYY-Www-NN")
    if r.get("ma_lich") in seen:
        errs.append("trùng mã lịch")
    bounds = week_bounds(r.get("tuan", ""))
    if bounds is None:
        errs.append(f"tuần '{r.get('tuan', '')}' phải dạng 2026-W42")
    else:
        try:
            day = dt.date.fromisoformat(r.get("ngay_dang", ""))
            if not bounds[0] <= day <= bounds[1]:
                errs.append(f"ngày đăng {day} không thuộc thứ Hai–thứ Sáu của tuần {r['tuan']}")
        except ValueError:
            errs.append(f"ngày đăng '{r.get('ngay_dang', '')}' phải dạng YYYY-MM-DD")
    product = r.get("san_pham", "")
    for k in ("kenh", "san_pham", "goc_tieu_de", "dinh_dang"):
        if not r.get(k):
            errs.append(f"cột {k} trống")
    if r.get("trang_thai") != CALENDAR_STATUS:
        errs.append(f"trạng thái phải là '{CALENDAR_STATUS}'")
    pillar = pillars.get(r.get("ma_tru_cot", ""))
    if pillar is None:
        errs.append(f"trụ cột '{r.get('ma_tru_cot', '')}' không có trong Chiến lược content")
    elif pillar["trang_thai"] != "đã duyệt":
        errs.append(f"trụ cột {pillar['ma']} đang '{pillar['trang_thai']}', chưa được duyệt")
    elif pillar["san_pham"] != product:
        errs.append(f"trụ cột {pillar['ma']} thuộc {pillar['san_pham']}, không phải {product}")
    ids = split_ids(r.get("ma_quan_sat", ""))
    if not ids:
        errs.append("không có mã quan sát")
    if len(ids) > MAX_OBS_PER_ROW:
        errs.append(f"quá {MAX_OBS_PER_ROW} quan sát cho một bài")
    if len(set(ids)) != len(ids):
        errs.append("một mã quan sát bị lặp")
    for oid in dict.fromkeys(ids):
        o = obs.get(oid)
        if o is None:
            errs.append(f"quan sát {oid} không có trong Research database")
        elif o["trang_thai"] in ("mốc", "bỏ"):
            errs.append(f"quan sát {oid} đang '{o['trang_thai']}', không dùng cho lịch")
        elif o["san_pham"] != product:
            errs.append(f"quan sát {oid} thuộc {o['san_pham']}, không phải {product}")
    return errs


def read_draft(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    keys, recs = as_records([[_norm(c) for c in row] for row in rows])
    return keys, recs


CALENDAR_KEYS = ["ma_lich", "tuan", "ngay_dang", "kenh", "san_pham", "ma_tru_cot", "ma_quan_sat",
                 "goc_tieu_de", "dinh_dang", "cta", "nguoi_phu_trach", "trang_thai"]


def validate_calendar(draft_path, obs, pillars):
    keys, recs = read_draft(draft_path)
    errors, rejected, valid, seen = [], [], [], set()
    missing = [k for k in CALENDAR_KEYS if k not in keys]
    if missing:
        return [f"lịch nháp thiếu cột {', '.join(missing)}"], [r.get("ma_lich", "?") for r in recs], []
    for r in recs:
        cid = r["ma_lich"] or f"dòng {r['_row']}"
        row_errs = check_calendar_row(r, obs, pillars, seen)
        seen.add(r["ma_lich"])
        if row_errs:
            rejected.append(cid)
            errors.extend(f"{cid}: {e}" for e in row_errs)
        else:
            valid.append(r)
    return errors, rejected, valid


# ---------------------------------------------------------------- cli

def report(label, items):
    print(f"{label}: {len(items)}")
    for e in items:
        print(f"- {e}")


def main(argv=None):
    p = argparse.ArgumentParser(description="Kiểm tra Research database và lịch tuần (truy vết quan sát → trụ cột).")
    p.add_argument("--workbook", required=True,
                   help="File .xlsx xuất từ Drive, hoặc file JSON kết quả công cụ có trường content (base64)")
    p.add_argument("--check", choices=["data", "none"], default="data",
                   help="data: kiểm các tab dữ liệu (mặc định); none: bỏ qua")
    p.add_argument("--calendar-draft", help="CSV lịch nháp, tiêu đề là khoá cột (ma_lich, tuan, …)")
    p.add_argument("--products", help="Sản phẩm cần lập lịch, ngăn bằng dấu phẩy (kiểm có trụ cột đã duyệt)")
    p.add_argument("--clean-out", help="Ghi các dòng lịch hợp lệ ra file JSON (mảng 2 chiều cho update_values)")
    args = p.parse_args(argv)

    tabs = load_workbook(args.workbook)
    data_errors = []
    if args.check == "data":
        check_insights(tabs, data_errors)
    obs = load_observations(tabs, data_errors if args.check == "data" else [])
    pillars = load_pillars(tabs, data_errors if args.check == "data" else [])
    if args.check == "data":
        check_calendar_tab(tabs, data_errors)

    if not args.calendar_draft:
        print(f"Workbook: {len(obs)} quan sát, {sum(1 for x in pillars.values() if x['trang_thai'] == 'đã duyệt')} trụ cột đã duyệt")
        report("ERRORS", data_errors)
        return 1 if data_errors else 0

    if args.products:
        products = [_norm(x) for x in args.products.split(",") if x.strip()]
        lacking = [pr for pr in products
                   if not any(x["san_pham"] == pr and x["trang_thai"] == "đã duyệt" for x in pillars.values())]
        if lacking:
            print("NO_APPROVED_PILLAR: " + ", ".join(lacking) +
                  " — chưa có trụ cột 'đã duyệt' trong Chiến lược content.")
            return 2

    cal_errors, rejected, valid = validate_calendar(args.calendar_draft, obs, pillars)
    if args.clean_out:
        Path(args.clean_out).write_text(
            json.dumps([[sheet_safe(r[k]) for k in CALENDAR_KEYS] for r in valid], ensure_ascii=False),
            encoding="utf-8")
    print(f"Lịch: {len(valid)} dòng hợp lệ, {len(rejected)} dòng bị loại")
    report("ERRORS", cal_errors)
    if data_errors:
        report("DATA_WARNINGS", data_errors)
    print("VALID_ROWS: " + str(len(valid)))
    print("REJECTED: " + ",".join(rejected))
    return 1 if rejected else 0


if __name__ == "__main__":
    sys.exit(main())
