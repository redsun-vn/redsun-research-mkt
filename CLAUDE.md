# Hướng dẫn cho Claude — repo redsun-mkt

Repo này là plugin Claude cho team Marketing redsun.vn. Bạn (Claude) thực thi mọi việc kỹ thuật; người dùng chỉ ra yêu cầu bằng lời.

## Quy tắc bắt buộc

Đọc và tuân theo `shared/working-rules.md` (cách nói chuyện với team MKT không biết kỹ thuật + nguyên tắc dữ liệu).

## Đọc file nào khi nào

| Người dùng nói | Bạn đọc và làm theo |
|---|---|
| "cài đặt", "setup", "đọc SETUP.md" | `SETUP.md` |
| "cập nhật", "update", "bản mới", "đọc UPDATE.md", "bản mới có gì" | `UPDATE.md` (và `CHANGELOG.md`) |
| "research hôm nay", "chạy research", "research bằng Chrome", "lập lịch tuần", "kho insight có gì" | `DAILY.md` |
| câu hỏi về cấu trúc dữ liệu | `shared/data-contract.md` |

## Dành cho người bảo trì repo

- Kiểm tra script: `python3 -m unittest discover -s tests`
- Kiểm tra plugin: `claude plugin validate .`
- Đóng gói cho Desktop: `bash scripts/build-desktop-zip.sh`
