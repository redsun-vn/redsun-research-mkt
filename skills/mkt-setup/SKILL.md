---
name: mkt-setup
description: Cài đặt hệ thống research Marketing Redsun — kiểm tra Google Drive/Google Sheets/Chrome, tạo Google Sheet "Redsun MKT — Research database" theo mẫu team (7 tab, đã có nguồn theo dõi và chiến lược content của SIPOS, WEBINO, REDSUN BOS) hoặc kết nối vào Sheet team đã có, chạy thử research; thêm sản phẩm mới (ví dụ SaaS, hosting, server, email) với đối thủ, từ khoá và trụ cột nháp. Dùng khi người dùng nói "chạy setup", "cài đặt", "thêm sản phẩm", "thêm đối thủ", "sửa nguồn theo dõi", hoặc khi skill khác báo chưa cài đặt.
---

# mkt-setup — cài đặt và cấu hình

Đọc trước (tính từ "Base directory" của skill):
- `../../shared/working-rules.md` — **bắt buộc**.
- `../../shared/data-contract.md` — 7 tab, cột, quy tắc ghi.
- `references/add-product-guide.md` — khi thêm sản phẩm hoặc đối thủ.
- Template từng tab: `../../templates/sheet/1-huong-dan.csv` … `7-content-calendar.csv` (tên tab theo thứ tự: Hướng dẫn, Nguồn theo dõi, Chiến lược content, Insight hằng ngày, Research database, Digest, Content Calendar).

## Bước 1 — Kiểm tra công cụ (tự làm, chỉ báo kết quả)

| Kiểm tra | Cách | Không được thì |
|---|---|---|
| Google Drive | `search_files` với `title = 'Redsun MKT — Research database'` | Dừng; hướng dẫn kết nối theo `../../SETUP.md` Bước 3 |
| Google Sheets | Có công cụ `get_values`/`update_values` của Google Sheets | Dừng; hướng dẫn kết nối theo `../../SETUP.md` Bước 3 |
| Đọc web | WebFetch `https://trends.google.com/trending?geo=VN` | Ghi nhận |
| Chrome | Có công cụ Claude in Chrome | Ghi nhận "phần Facebook/TikTok/quảng cáo cần Chrome, cài sau cũng được" |

Báo 3–4 dòng ✅/⚠️, không thuật ngữ.

## Bước 2 — Sheet dùng chung

- **Đã có** (tìm thấy đúng 1 file): "Team đã có bảng Research database, mình dùng luôn." Đọc `get_spreadsheet` (`fields: ["sheets.properties"]`) và so với 7 tab; thiếu tab `Content Calendar` hoặc cột `Trạng thái` ở Chiến lược content → bổ sung (xem Bước 3 mục 4–5), không đụng dữ liệu khác. Sang Bước 4.
- **Nhiều file**: liệt kê tên + người sở hữu, hỏi dùng file nào.
- **Chưa có**: hỏi một câu: "Mình tạo bảng Research database mới cho team nhé? Bảng sẽ có sẵn danh sách đối thủ và chiến lược content của SIPOS, WEBINO, REDSUN BOS từ bảng mẫu team đã làm." Hỏi thêm: lưu ở **Drive chung của công ty** (khuyên dùng — nhờ dán link thư mục) hay Drive cá nhân rồi chia sẻ.

## Bước 3 — Tạo Sheet mới từ template

1. Drive `create_file`: `title = "Redsun MKT — Research database"`, `contentMimeType = "application/vnd.google-apps.spreadsheet"`, `parentId` = thư mục người dùng chọn (nếu có).
2. `update_spreadsheet` một lần: đổi tên tab đầu (`sheetId 0`) thành `Hướng dẫn`; `addSheet` 6 tab còn lại theo đúng thứ tự (đặt `sheetId` 1…6).
3. Với từng tab, đọc file CSV template tương ứng và ghi toàn bộ bằng `update_values` từ ô `A1`. **Mọi ô có dấu `'` ở đầu** (ô trống để trống).
4. `update_spreadsheet` một lần cho định dạng: hàng 1 in đậm và cố định (frozen) ở mọi tab; tự giãn độ rộng cột chữ (`autoResizeDimensions`) hoặc đặt độ rộng hợp lý; bật xuống dòng (wrap) cho cột dài (Insight, Quan sát, Căn cứ, Ý nghĩa, Content Idea, Nội dung).
5. Đọc lại hàng 1–3 mỗi tab bằng `get_values` để kiểm tra.
6. Nhắc người dùng chia sẻ Sheet (quyền **Người chỉnh sửa**) cho cả team; cho link.

Nội dung Chiến lược content trong template là chiến lược team đã duyệt ngày 08/10/2026 (cột Trạng thái `đã duyệt`). Nói rõ điều này với người dùng và mời người duyệt xem lại.

## Bước 4 — Cập nhật nguồn theo dõi (tuỳ chọn)

Hỏi: "Danh sách đối thủ và từ khoá hiện có: <tóm tắt 1 dòng mỗi sản phẩm>. Bạn có muốn thêm/bớt gì, hoặc thêm sản phẩm khác (ví dụ hosting, email doanh nghiệp…) không?"
- Có → làm theo `references/add-product-guide.md`.
- Không → sang Bước 5.

## Bước 5 — Chạy thử

"Giờ mình chạy thử research một lượt nhỏ để chắc mọi thứ hoạt động." Chạy skill `mkt-research` chế độ thường cho sản phẩm của hôm nay, giới hạn khoảng 5 insight. Có Chrome → hỏi có muốn thử luôn chế độ Chrome với 1 đối thủ không (cần đã đăng nhập Facebook/TikTok bằng tài khoản thật).

## Bước 6 — Kết thúc

Khi được gọi từ `SETUP.md`: **không** hướng dẫn lịch tự động và **không** in tóm tắt — `SETUP.md` Bước 6–7 làm việc đó. Khi được gọi riêng: in

```
✅ Xong!
- Bảng dữ liệu: <link>
- Chiến lược content: <n> trụ cột đã duyệt, <m> trụ cột nháp chờ duyệt
Từ giờ bạn chỉ cần nói: "Research hôm nay" · "Research bằng Chrome" · "Lập lịch tuần sau"
```
