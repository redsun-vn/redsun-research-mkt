# Operations runbook — người phụ trách kỹ thuật

Dành cho người bảo trì plugin `redsun-mkt` (không phải team MKT).

## Cấu trúc repo

| Đường dẫn | Vai trò |
|---|---|
| `.claude-plugin/` | Manifest plugin + marketplace (cài từ GitHub `owner/repo` hoặc đường dẫn local) |
| `skills/mkt-setup`, `skills/mkt-research`, `skills/mkt-content-calendar` | 3 skill chính |
| `commands/` | Lệnh tắt `/redsun-mkt:setup`, `:research`, `:research-chrome`, `:calendar` |
| `shared/data-contract.md` | Nguồn duy nhất về cột, ID, tag, thư mục Drive |
| `shared/working-rules.md` | Quy tắc giao tiếp + dữ liệu mọi skill phải theo |
| `templates/` | Nội dung khởi tạo Doc trên Drive |
| `scripts/validate_trace.py` | Máy kiểm tra insight/calendar (stdlib, exit 0/1/2) |
| `SETUP.md`, `DAILY.md` | Runbook Claude thực thi cho người dùng |

## Kiểm tra trước khi phát hành

```bash
python3 -m unittest discover -s tests      # 7 test validator
claude plugin validate .                   # manifest
bash scripts/build-desktop-zip.sh          # dist/redsun-mkt.zip
```

Phát hành: tăng `version` trong `.claude-plugin/plugin.json`, commit, push. Người dùng Desktop cập nhật trong Customize → Plugins; Claude Code: `claude plugin update redsun-mkt`.

## Giới hạn đã kiểm chứng (2026-10-09)

- Google Drive connector **không sửa được nội dung file** (`update_file` chỉ đổi tên/thư mục). Thiết kế vì vậy chỉ tạo file mới; config được "sửa" bằng cách tạo bản mới và chuyển bản cũ vào `config/_cu/`.
- Upload CSV không đặt `disableConversionToGoogleType` → Drive tạo Google Sheet; export `text/csv` đọc lại không mất dữ liệu (tiếng Việt, dấu phẩy, ngoặc kép, xuống dòng).
- WebFetch không đọc được Meta Ad Library, TikTok, TikTok Creative Center → các nguồn này chỉ qua Claude in Chrome.

## Kiểm tra sức khoẻ hằng tuần (10 phút)

1. Drive → `runs/`: có bảng mỗi ngày làm việc? Thiếu ngày → lịch tự động không chạy (máy tắt, Owner tắt tính năng, hoặc connector mất quyền).
2. Lọc cột `status = blocked` trong các run tuần qua. Một nguồn bị chặn ≥3 ngày liên tiếp → kiểm tra URL trong `config/config` hoặc cập nhật `skills/mkt-research/references/sources-playbook.md`.
3. Kiểm tra lịch tuần mới nhất: file `CAL_…_review` có mục "Đã loại" nhiều dòng → insight kém chất lượng hoặc strategy thiếu pillar.
4. Số insight mỗi run thấp liên tục (<5) → nguồn cạn hoặc keyword quá hẹp; gợi ý team bổ sung đối thủ/keyword.

## Sự cố thường gặp

| Triệu chứng | Nguyên nhân hay gặp | Xử lý |
|---|---|---|
| Skill báo "chưa cài đặt" dù đã cài | Người dùng khác tài khoản Google, không thấy thư mục | Chia sẻ thư mục `RedSun-MKT-Research` (hoặc Shared Drive) cho tài khoản đó |
| Lịch tự động không chạy | Owner workspace tắt Scheduled tasks/Routines, hoặc máy tắt (tác vụ Chrome) | Kiểm tra cài đặt admin; tạm thời chạy tay |
| Research Chrome bị dừng | Facebook/TikTok yêu cầu xác minh | Người dùng tự xác minh tài khoản; giảm `Số bài tối đa` trong `config/settings` |
| Insight trùng nhiều | Cùng nguồn ngày nào cũng quét | Kiểm tra "Ngày quét sâu" trong config, tăng số ngày so trùng |
| Calendar từ chối chạy | Strategy chưa `approved` | Đúng thiết kế; nhắc MKT lead duyệt |
