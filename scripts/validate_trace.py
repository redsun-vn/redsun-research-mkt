#!/usr/bin/env python3
"""Traceability gate for the MKT insight database and weekly content calendar.

Checks insight rows against shared/data-contract.md and, for a calendar, that every
row points to 1-3 real non-duplicate insights of a compatible product line and to a
pillar of an approved strategy. Standard library only, so it runs in Claude Code and
in Cowork sandboxes without installing anything.

Exit codes:
  insights mode: 0 = clean, 1 = rows failed validation
  calendar mode: 0 = no calendar row rejected, 1 = some rows rejected,
                 2 = strategy not approved
  (in calendar mode, schema problems in old insight files are printed as
   INSIGHT_WARNINGS and do not change the exit code)
"""

import argparse
import csv
import datetime as dt
import re
import sys
import unicodedata
from pathlib import Path

PRODUCT_LINES = {"saas", "hosting", "server", "email", "general"}
CHANNELS = {
    "website", "facebook_page", "facebook_ads", "tiktok",
    "tiktok_creative_center", "google_trends", "search", "other",
}
SOURCE_MODES = {"public-auto", "chrome"}
TAGS = {"pain_point", "offer", "cta", "keyword", "content_pattern", "topic"}
RUN_STATUSES = {"ok", "blocked", "empty", "skipped"}
INSIGHT_COLUMNS = [
    "insight_id", "run_id", "captured_at", "product_line", "competitor", "channel",
    "source_mode", "source_url", "observation", "evidence", "meaning",
    "content_idea", "tags", "dup_of",
]
REQUIRED_INSIGHT = [c for c in INSIGHT_COLUMNS if c != "dup_of"]
CALENDAR_COLUMNS = [
    "cal_id", "week", "date", "channel", "product_line", "format", "pillar_id",
    "insight_ids", "angle", "cta", "owner", "status",
]
RUN_COLUMNS = [
    "run_id", "trigger", "runtime", "mode", "source", "product_line", "status",
    "rows_written", "reason", "started_at",
]
MAX_EVIDENCE = 300
MAX_INSIGHTS_PER_ROW = 3

_STAMP = r"(\d{8})-([01]\d|2[0-3])([0-5]\d)([0-5]\d)"
INSIGHT_ID_RE = re.compile(rf"^INS-{_STAMP}-(0[1-9]|[1-9]\d)$")
RUN_ID_RE = re.compile(rf"^RUN-{_STAMP}$")
CAL_ID_RE = re.compile(r"^CAL-(\d{4})-W(\d{2})-\d{2}$")
WEEK_RE = re.compile(r"^(\d{4})-W(\d{2})$")
ISO_VN_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?\+07:00$")
URL_RE = re.compile(r"^https?://\S+$")
PILLAR_RE = re.compile(
    r"(P-[A-Z]+-\d{2})\s*\|\s*(saas|hosting|server|email|general)\s*\|", re.IGNORECASE
)
# Only a line that starts with the label counts, so instruction prose that
# mentions "Trạng thái: approved" can never approve a draft.
STATUS_RE = re.compile(r"^\s*Trạng thái\s*:\s*(draft|approved)\b", re.IGNORECASE | re.MULTILINE)
SHEET_FORMULA_PREFIXES = ("=", "+", "-", "@")


def sheet_safe(value):
    """Prefix an apostrophe so Google Sheets stores the cell as literal text.

    Verified on Drive CSV import: '=1+1 is kept as text and exports back as =1+1,
    while =1+1 is evaluated and 0800 loses its leading zero.
    """
    if not value:
        return value
    if value.startswith(SHEET_FORMULA_PREFIXES) or re.fullmatch(r"0\d+", value):
        return "'" + value
    return value


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, restval="")
        rows = []
        for row in reader:
            row.pop(None, None)  # extra cells beyond the header
            rows.append({k: (v or "") for k, v in row.items()})
        return reader.fieldnames or [], rows


def split_multi(value):
    return [v.strip() for v in (value or "").split("|") if v.strip()]


def check_columns(path, fieldnames, expected, errors):
    missing = [c for c in expected if c not in fieldnames]
    if missing:
        errors.append(f"{path}: thiếu cột {', '.join(missing)}")
    return not missing


def validate_insight_row(row, rid):
    errs = []
    get = lambda c: row.get(c, "").strip()
    for col in REQUIRED_INSIGHT:
        if not get(col):
            errs.append(f"cột {col} trống (thiếu dữ liệu)")
    iid, run_id = get("insight_id"), get("run_id")
    m = INSIGHT_ID_RE.match(iid)
    if iid and not m:
        errs.append("insight_id sai định dạng INS-YYYYMMDD-HHMMSS-NN (NN từ 01)")
    if run_id and not RUN_ID_RE.match(run_id):
        errs.append("run_id sai định dạng RUN-YYYYMMDD-HHMMSS")
    elif m and run_id and run_id[4:] != iid[4:19]:
        errs.append(f"run_id {run_id} không khớp thời điểm trong insight_id")
    if get("captured_at") and not ISO_VN_RE.match(get("captured_at")):
        errs.append("captured_at phải dạng 2026-10-09T08:05:00+07:00")
    checks = (("product_line", PRODUCT_LINES), ("channel", CHANNELS), ("source_mode", SOURCE_MODES))
    for col, allowed in checks:
        if get(col) and get(col) not in allowed:
            errs.append(f"{col} '{get(col)}' không hợp lệ")
    if get("source_url") and not URL_RE.match(get("source_url")):
        errs.append("source_url phải là link http(s):// đầy đủ")
    if len(get("evidence")) > MAX_EVIDENCE:
        errs.append(f"evidence dài {len(get('evidence'))} ký tự, tối đa {MAX_EVIDENCE}")
    bad_tags = [t for t in split_multi(get("tags")) if t not in TAGS]
    if bad_tags:
        errs.append(f"tags không hợp lệ {bad_tags}")
    if get("dup_of") and not INSIGHT_ID_RE.match(get("dup_of")):
        errs.append("dup_of phải là một insight_id")
    return errs


def validate_insights(paths):
    """Return (insights_by_id, errors). The first occurrence of an id wins."""
    errors, insights = [], {}
    for path in paths:
        fieldnames, rows = read_csv(path)
        if not check_columns(path, fieldnames, INSIGHT_COLUMNS, errors):
            continue
        for n, row in enumerate(rows, start=2):
            iid = row["insight_id"].strip()
            rid = iid or f"{Path(path).name}:dòng {n}"
            errors.extend(f"{rid}: {e}" for e in validate_insight_row(row, rid))
            if iid:
                if iid in insights:
                    errors.append(f"{iid}: insight_id bị trùng giữa các dòng/file")
                else:
                    insights[iid] = row
    return insights, errors


def read_strategy(path):
    """Return (status, {pillar_id: product_line}, warnings)."""
    text = unicodedata.normalize("NFC", Path(path).read_text(encoding="utf-8-sig"))
    status = STATUS_RE.search(text)
    pillars, warnings = {}, []
    for pid, line in PILLAR_RE.findall(text):
        pid, line = pid.upper(), line.lower()
        if pid in pillars:
            warnings.append(f"{pid}: mã pillar xuất hiện nhiều lần trong strategy, dùng dòng đầu tiên")
            continue
        pillars[pid] = line
    return (status.group(1).lower() if status else None), pillars, warnings


def week_bounds(week):
    m = WEEK_RE.match(week)
    if not m:
        return None
    try:
        monday = dt.date.fromisocalendar(int(m.group(1)), int(m.group(2)), 1)
    except ValueError:
        return None
    return monday, monday + dt.timedelta(days=6)


def validate_calendar_row(row, insights, pillars, seen_cal_ids):
    errs = []
    get = lambda c: row.get(c, "").strip()
    cid, line, pid = get("cal_id"), get("product_line"), get("pillar_id")
    if not CAL_ID_RE.match(cid):
        errs.append("cal_id sai định dạng CAL-YYYY-Www-NN")
    if cid in seen_cal_ids:
        errs.append("trùng cal_id với dòng khác")
    bounds = week_bounds(get("week"))
    if bounds is None:
        errs.append(f"week '{get('week')}' không hợp lệ (dạng 2026-W42)")
    else:
        try:
            day = dt.date.fromisoformat(get("date"))
            if not bounds[0] <= day <= bounds[1]:
                errs.append(f"date {day} nằm ngoài tuần {get('week')}")
        except ValueError:
            errs.append(f"date '{get('date')}' không hợp lệ (dạng YYYY-MM-DD)")
    if line not in PRODUCT_LINES:
        errs.append(f"product_line '{line}' không hợp lệ")
    if get("status") != "de-xuat":
        errs.append("status phải là de-xuat")
    pillar_line = pillars.get(pid)
    if pillar_line is None:
        errs.append(f"pillar {pid or '(trống)'} không có trong strategy")
    elif pillar_line not in (line, "general"):
        errs.append(f"pillar {pid} thuộc '{pillar_line}', không khớp product_line '{line}'")
    ids = split_multi(get("insight_ids"))
    if not ids:
        errs.append("không có insight_ids")
    if len(ids) > MAX_INSIGHTS_PER_ROW:
        errs.append(f"quá {MAX_INSIGHTS_PER_ROW} insight cho một bài")
    if len(set(ids)) != len(ids):
        errs.append("một insight bị lặp trong cùng dòng")
    for iid in dict.fromkeys(ids):
        insight = insights.get(iid)
        if insight is None:
            errs.append(f"insight {iid} không tồn tại trong kho")
        elif insight["dup_of"].strip():
            errs.append(f"insight {iid} là bản trùng của {insight['dup_of']}")
        elif pillar_line != "general" and insight["product_line"].strip() not in (line, "general"):
            errs.append(f"insight {iid} thuộc '{insight['product_line']}', không khớp product_line '{line}'")
    return errs


def validate_calendar(path, insights, pillars):
    """Return (rejected_cal_ids, errors, valid_rows, fieldnames)."""
    errors, rejected, valid, seen = [], [], [], set()
    fieldnames, rows = read_csv(path)
    if not check_columns(path, fieldnames, CALENDAR_COLUMNS, errors):
        return [r.get("cal_id", "?") for r in rows], errors, [], fieldnames
    for row in rows:
        cid = row["cal_id"].strip() or "?"
        row_errors = validate_calendar_row(row, insights, pillars, seen)
        seen.add(cid)
        if row_errors:
            rejected.append(cid)
            errors.extend(f"{cid}: {e}" for e in row_errors)
        else:
            valid.append(row)
    return rejected, errors, valid, fieldnames


def validate_runs(paths):
    errors = []
    for path in paths:
        fieldnames, rows = read_csv(path)
        if not check_columns(path, fieldnames, RUN_COLUMNS, errors):
            continue
        for n, row in enumerate(rows, start=2):
            where = f"{Path(path).name}:dòng {n}"
            if not RUN_ID_RE.match(row["run_id"].strip()):
                errors.append(f"{where}: run_id sai định dạng")
            if row["status"].strip() not in RUN_STATUSES:
                errors.append(f"{where}: status '{row['status']}' không hợp lệ")
            elif row["status"].strip() != "ok" and not row["reason"].strip():
                errors.append(f"{where}: thiếu reason khi status là {row['status']}")
    return errors


def write_csv(path, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: sheet_safe(row.get(k, "")) for k in fieldnames})


def report(errors, summary, label="ERRORS"):
    print(summary)
    print(f"{label}: {len(errors)}")
    for e in errors:
        print(f"- {e}")


def main(argv=None):
    p = argparse.ArgumentParser(description="Kiểm tra truy vết insight → calendar → strategy.")
    p.add_argument("--insights", nargs="+", required=True,
                   help="Một hoặc nhiều file CSV insight (mỗi file Drive xuất ra một file, không gộp)")
    p.add_argument("--calendar", help="File CSV calendar cần kiểm")
    p.add_argument("--strategy", help="Strategy đã xuất ra text (bắt buộc khi có --calendar)")
    p.add_argument("--clean-out", help="Ghi các dòng calendar hợp lệ (đã an toàn cho Sheet) ra file này")
    p.add_argument("--sheet-safe-out", help="Ghi insight (đã an toàn cho Sheet) ra file này để upload")
    p.add_argument("--runs", nargs="+", help="File CSV run log cần kiểm")
    args = p.parse_args(argv)

    insights, errors = validate_insights(args.insights)
    run_errors = validate_runs(args.runs) if args.runs else []

    if not args.calendar:
        if args.sheet_safe_out:
            rows = []
            for path in args.insights:
                rows.extend(read_csv(path)[1])
            write_csv(args.sheet_safe_out, INSIGHT_COLUMNS, rows)
        report(errors + run_errors, f"Insight: {len(insights)} dòng")
        return 1 if (errors or run_errors) else 0

    if not args.strategy:
        p.error("--strategy là bắt buộc khi kiểm calendar")
    status, pillars, strategy_warnings = read_strategy(args.strategy)
    if status != "approved":
        print(f"STRATEGY_NOT_APPROVED: trạng thái hiện tại là '{status or 'không tìm thấy'}'. "
              "Calendar chỉ chạy khi strategy có dòng bắt đầu bằng 'Trạng thái: approved'.")
        return 2

    rejected, cal_errors, valid, fieldnames = validate_calendar(args.calendar, insights, pillars)
    if args.clean_out:
        write_csv(args.clean_out, fieldnames or CALENDAR_COLUMNS, valid)
    report(cal_errors, f"Calendar: {len(valid)} dòng hợp lệ, {len(rejected)} dòng bị loại")
    if errors or strategy_warnings:
        report(errors + strategy_warnings, "Cảnh báo dữ liệu cũ (không làm loại dòng lịch):",
               label="INSIGHT_WARNINGS")
    print("VALID_ROWS: " + str(len(valid)))
    print("REJECTED: " + ",".join(rejected))
    return 1 if rejected else 0


if __name__ == "__main__":
    sys.exit(main())
