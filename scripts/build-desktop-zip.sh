#!/usr/bin/env bash
# Đóng gói plugin thành dist/redsun-mkt.zip để tải lên Claude Desktop khi chưa cài được từ GitHub.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/dist/redsun-mkt.zip"

mkdir -p "$ROOT/dist"
rm -f "$OUT"
cd "$ROOT"
zip -rq "$OUT" .claude-plugin skills commands shared templates scripts docs/mkt-user-guide.md docs/owner-setup-guide.md CLAUDE.md SETUP.md DAILY.md UPDATE.md CHANGELOG.md README.md \
  -x '*/__pycache__/*' '*.DS_Store'
echo "Đã tạo $OUT"
