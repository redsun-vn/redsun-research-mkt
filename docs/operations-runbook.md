# Operations runbook — người phụ trách kỹ thuật

Dành cho người bảo trì plugin `redsun-mkt` (không phải team MKT).

## Cấu trúc repo

| Đường dẫn | Vai trò |
|---|---|
| `.claude-plugin/` | Manifest plugin + marketplace (cài từ GitHub `redsun-vn/redsun-research-mkt` hoặc đường dẫn local) |
| `skills/mkt-setup` | Tạo/kết nối Google Sheet, thêm sản phẩm/đối thủ |
| `skills/mkt-research` | Bước 1 (Insight hằng ngày + Digest) và Bước 2 (Research database) |
| `skills/mkt-content-calendar` | Bước 3 (Content Calendar) |
| `commands/` | Lệnh tắt `/redsun-mkt:setup`, `:research`, `:research-chrome`, `:calendar` |
| `shared/data-contract.md` | Nguồn duy nhất về tab, cột, quy tắc ghi |
| `shared/working-rules.md` | Quy tắc giao tiếp + dữ liệu mọi skill phải theo |
| `templates/sheet/*.csv` | Nội dung khởi tạo 7 tab (nguồn theo dõi + chiến lược content lấy từ bảng mẫu team ngày 08/10/2026) |
| `scripts/validate_trace.py` | Máy kiểm tra workbook xuất .xlsx + lịch nháp (stdlib) |
| `SETUP.md`, `DAILY.md` | Runbook Claude thực thi cho người dùng |

## Kiểm tra trước khi phát hành

```bash
python3 -m unittest discover -s tests      # validator + template
claude plugin validate .                   # manifest
bash scripts/build-desktop-zip.sh          # dist/redsun-mkt.zip cho người không có GitHub
```

## Phát hành bản mới

1. Chạy 3 lệnh kiểm tra ở trên; tất cả phải pass.
2. Tăng `version` trong `.claude-plugin/plugin.json` (sửa lỗi: 0.1.0 → 0.1.1; thêm tính năng: 0.1.x → 0.2.0). Plugin chỉ báo có bản mới khi `version` thay đổi.
3. Thêm mục mới ở **đầu** `CHANGELOG.md`: ngày, 1–4 dòng "có gì mới" bằng lời thường, và **Team cần làm** (thêm tab/cột Sheet, sửa lời nhắn lịch tự động, bật kết nối mới… hoặc "Không có").
4. Nếu thay đổi cấu trúc Sheet: cập nhật `shared/data-contract.md`, `templates/sheet/`, máy kiểm tra, và đảm bảo `mkt-setup` Bước 2 bổ sung được phần thiếu cho bảng cũ mà không đụng dữ liệu.
5. Nếu đổi lời nhắn lịch tự động: cập nhật bảng ở `SETUP.md` Bước 6 và ghi rõ trong "Team cần làm".
6. Commit, push lên `main`, chạy `bash scripts/build-desktop-zip.sh` và gửi `dist/redsun-mkt.zip` cho người không có GitHub.
7. Gửi thông báo vào nhóm chat MKT:

```
📢 Công cụ research Marketing có bản mới <version>
Có gì mới: <1–3 dòng từ CHANGELOG>
Team cần làm: <… | Không có>
Cách cập nhật: mở Claude trong thư mục redsun-research-mkt và nói "Đọc file UPDATE.md và cập nhật giúp tôi".
(Ai cài bằng file ZIP: tải file đính kèm.)
```

Kiểm tra bảng thật bất kỳ lúc nào: xuất Sheet ra .xlsx (Drive → Tải xuống → Microsoft Excel) rồi `python3 scripts/validate_trace.py --workbook file.xlsx`.

## Giới hạn đã kiểm chứng (2026-10-09)

- Google Drive connector không sửa được nội dung file → ghi vào tab cần **Google Sheets connector** (`get_values`, `update_values`, `update_spreadsheet`).
- Sheets tự đổi chữ thành số/ngày/công thức (`=1+1` → `2`, `0800` → `800`); dấu `'` ở đầu giữ nguyên chữ. Ngày gõ tay được lưu dạng số ngày của Sheets — máy kiểm tra chấp nhận cả hai.
- WebFetch không đọc được Meta Ad Library, TikTok, Facebook → các nguồn này chỉ qua Claude in Chrome. Chrome đọc được Ad Library không cần đăng nhập.
- Tìm kiếm Drive không trả file trong thùng rác.

## Kiểm tra sức khoẻ hằng tuần (10 phút)

1. Tab Digest: mỗi ngày làm việc có `Tóm tắt lượt chạy`? Thiếu → lịch tự động không chạy (máy tắt, Owner tắt tính năng, mất quyền).
2. `Nguồn lỗi/bị chặn` lặp ≥ 3 ngày cho cùng nguồn → sửa link ở tab Nguồn theo dõi hoặc cập nhật `skills/mkt-research/references/sources-playbook.md`.
3. `Lịch tuần … — đã loại` nhiều dòng → quan sát thiếu Content Idea tốt hoặc trụ cột thiếu quan sát.
4. Chạy máy kiểm tra trên bản xuất .xlsx; lỗi ở dòng cũ do người sửa tay → nhắc team quy tắc không chèn/sắp xếp.

## Sự cố thường gặp

| Triệu chứng | Nguyên nhân | Xử lý |
|---|---|---|
| "Chưa cài đặt" dù đã có bảng | Tài khoản chưa được chia sẻ bảng, hoặc tên bảng bị đổi | Chia sẻ quyền Người chỉnh sửa; giữ đúng tên `Redsun MKT — Research database` |
| Không ghi được vào bảng | Thiếu Google Sheets connector | SETUP.md Bước 3 |
| Lịch tự động không chạy | Owner tắt Scheduled tasks, hoặc máy tắt (tác vụ Chrome) | Kiểm tra cài đặt admin; tạm chạy tay |
| Research Chrome bị dừng | Facebook/TikTok yêu cầu xác minh | Người dùng tự xác minh; giảm giới hạn trong tab Nguồn theo dõi |
| Lịch tuần không có bài cho WEBINO | WEBINO chưa có Fanpage/TikTok ở dòng `của mình` | Điền link kênh khi có |
