---
name: mkt-setup
description: Cài đặt lần đầu (hoặc bổ sung) hệ thống research Marketing redsun.vn — kiểm tra Google Drive/Chrome, tạo thư mục kho insight trên Drive, phỏng vấn để điền đối thủ/keyword/kênh cho 4 dòng sản phẩm, soạn bản nháp Content Strategy chờ duyệt, chạy thử research. Dùng khi người dùng nói "chạy setup", "cài đặt", "thiết lập", "thêm đối thủ", "sửa cấu hình", hoặc khi skill khác báo chưa cài đặt.
---

# mkt-setup — cài đặt cho team MKT

Đọc trước (tính từ thư mục chứa file này):
- `../../shared/working-rules.md` — **bắt buộc**, đặc biệt phần nói chuyện với người không biết kỹ thuật.
- `../../shared/data-contract.md` — thư mục Drive, định dạng file.
- `references/interview-questions.md` — câu hỏi phỏng vấn.
- `references/strategy-drafting-guide.md` — soạn strategy nháp.
- Template ở `../../templates/`: `config.md`, `strategy.md`, `settings.md`, `drive-readme.md`.

Mở đầu bằng: "Mình sẽ cài đặt giúp bạn, mất khoảng 10–15 phút. Mình hỏi từng câu một, bạn cứ trả lời tự nhiên nhé."

## Bước 1 — Kiểm tra công cụ (tự làm, chỉ báo kết quả)

| Kiểm tra | Cách | Nếu không được |
|---|---|---|
| Google Drive | Gọi `search_files` với `title = 'RedSun-MKT-Research'` | Dừng. Hướng dẫn bật Google Drive theo `SETUP.md` bước "Kết nối Google Drive" (một thao tác mỗi lần), rồi thử lại |
| Đọc web | WebFetch `https://trends.google.com/trending?geo=VN` | Ghi nhận; research vẫn chạy được phần còn lại |
| Chrome | Có công cụ Claude in Chrome không | Ghi nhận "chưa có Chrome — phần Fanpage/TikTok sẽ cần cài sau" |
| Môi trường | Claude Code / Cowork / chat thường | Ghi nhận để chọn cách lên lịch |

Báo người dùng bằng 3–4 dòng dấu ✅/⚠️, không thuật ngữ.

## Bước 2 — Thư mục trên Drive

- **Đã có** `RedSun-MKT-Research`: nói "Mình thấy team đã cài trước đó." Đọc `config/config`, `config/strategy`, `config/settings`, rồi chỉ hỏi phần còn trống (`<điền>`) hoặc phần người dùng muốn sửa. Không tạo thư mục trùng.
- **Chưa có**: hỏi một câu:
  "Bạn muốn lưu kho dữ liệu ở đâu? (1) Bộ nhớ dùng chung của công ty (Shared Drive) — nên chọn, dữ liệu thuộc về team; (2) Drive của riêng bạn rồi chia sẻ cho team."
  - (1): nhờ họ dán link một thư mục trong Shared Drive mà họ có quyền thêm file. Lấy ID từ link, tạo `RedSun-MKT-Research` bên trong.
  - (2): tạo ở gốc My Drive.
  - Tạo các thư mục con: `config`, `config/_cu`, `insights`, `runs`, `calendar`. Tạo Doc `README` từ `templates/drive-readme.md`.

Tạo Doc: `create_file` với `contentMimeType: text/plain`, `textContent` là nội dung, không đặt `disableConversionToGoogleType` → Drive tạo Google Doc.

## Bước 3 — Phỏng vấn cấu hình

Theo `references/interview-questions.md`. **Mỗi lần một câu**, có ví dụ trả lời. Nhận câu trả lời tự nhiên (dán link fanpage, viết tắt…) và tự chuẩn hoá. Hỏi lần lượt 4 dòng sản phẩm: SaaS, hosting, server, email. Người dùng nói "chưa biết"/"bỏ qua" → để `<điền>` và đi tiếp.

Trước khi ghi, tóm tắt lại thành danh sách ngắn và hỏi "Đúng chưa?".

## Bước 4 — Content Strategy nháp

Team chưa có Content Strategy. Nói: "Lịch nội dung tuần cần dựa trên chiến lược nội dung. Team chưa có, nên mình sẽ hỏi vài câu để soạn **bản nháp**. Trưởng nhóm MKT sẽ duyệt trước khi dùng."

Theo `references/strategy-drafting-guide.md`. Chỉ soạn pillar từ câu trả lời của người dùng, không tự thêm định hướng họ không nói. Ghi `Trạng thái: draft`.

## Bước 5 — Ghi cấu hình lên Drive

- Lần đầu: tạo 3 Doc `config`, `strategy`, `settings` trong `config/` từ template đã điền (settings: điền ID thư mục gốc).
- Đã có và người dùng xác nhận sửa: tạo Doc mới cùng tên, chuyển bản cũ vào `config/_cu/` bằng `update_file` (đổi `parentId`) và thêm hậu tố ngày vào tên bản cũ. Không xoá.

## Bước 6 — Chạy thử

Nói "Giờ mình chạy thử research một lần nhỏ để chắc mọi thứ hoạt động." Chạy skill `mkt-research` ở chế độ `public-auto` với số insight = 3. Đọc lại file vừa tạo, kiểm tra đủ cột. Báo link.

Nếu có Chrome: hỏi "Bạn có muốn thử luôn phần đọc Fanpage/TikTok bằng Chrome không? Bạn cần đang đăng nhập Facebook/TikTok bằng tài khoản của mình trên Chrome." Đồng ý → chạy thử chế độ `chrome` với 1 đối thủ.

## Bước 7 — Lên lịch chạy tự động

Theo `SETUP.md` mục "Lịch chạy tự động" (ở gốc repo/plugin: `../../SETUP.md`). Hướng dẫn từng thao tác.

## Bước 8 — Kết thúc

```
✅ Cài đặt xong!
- Kho dữ liệu: <link thư mục>
- Strategy: bản nháp — nhờ <người duyệt> duyệt tại <link> (đổi "draft" thành "approved")
- Lịch tự động: <đã tạo / chưa tạo — cách chạy tay>

Từ giờ bạn chỉ cần nói:
• "Research hôm nay"
• "Research bằng Chrome" (đọc Fanpage/TikTok đối thủ)
• "Lập lịch tuần sau"
```
