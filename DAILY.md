# DAILY — dùng hằng ngày (dành cho Claude thực hiện)

> Người dùng là team Marketing, không biết kỹ thuật. Tuân theo `shared/working-rules.md`. Chưa có Google Sheet **Redsun MKT — Research database** → làm theo `SETUP.md`.

## Người dùng nói gì → Claude làm gì

| Người dùng nói (ví dụ) | Việc của Claude |
|---|---|
| "Research hôm nay", "chạy research" | `mkt-research`, chế độ thường (sản phẩm theo vòng luân phiên) |
| "Research bằng Chrome", "xem Fanpage/TikTok/quảng cáo đối thủ" | `mkt-research`, chế độ chrome |
| "Research đầy đủ", "research SIPOS" | `mkt-research` (cả hai chế độ / đúng sản phẩm) |
| "Lập lịch tuần sau", "content calendar tuần này", "lịch cho SIPOS" | `mkt-content-calendar` — chạy ngay, không cần chờ thứ Hai |
| "Hôm nay làm nội dung gì", "viết idea/brief", "viết kịch bản video cho bài …" | `mkt-content-calendar` mục 7: trả về các khối idea theo khuôn chuẩn, copy được cho agent tạo video/nội dung |
| "Kho insight có gì về …", "tuần này có gì mới" | `mkt-research` mục Hỏi đáp: trả lời kèm mã OB/link nguồn, không ghi gì |
| "Hôm qua research có chạy không?" | Đọc Digest: `Tóm tắt lượt chạy`, `Nguồn lỗi/bị chặn` gần nhất |
| "Strategy đã ổn chưa?", "duyệt strategy" | `mkt-content-calendar`: tóm tắt trụ cột + trạng thái; chỉ người duyệt tự đổi `nháp` → `đã duyệt` |
| "Thêm đối thủ…", "thêm sản phẩm hosting…", "thêm từ khoá…" | `mkt-setup` → `references/add-product-guide.md` |

Câu không khớp bảng → hỏi lại một câu ngắn.

## Báo kết quả

- Mở đầu bằng kết quả, tối đa 5 dòng, kèm link Google Sheet.
- Nguồn bị chặn: nói đời thường ("Facebook yêu cầu xác minh tài khoản") và việc người dùng cần làm nếu có.
- Không dán bảng dữ liệu thô vào chat trừ khi người dùng xin.

## Khi có sự cố

| Tình huống | Nói với người dùng |
|---|---|
| Thiếu kết nối Google Drive/Sheets | "Mình chưa vào được Google Sheets. Bạn làm giúp mình bước kết nối nhé" → `SETUP.md` Bước 3 |
| Chrome không kết nối | "Chrome chưa mở hoặc chưa bật tiện ích Claude. Hôm nay mình research phần website trước; bạn mở Chrome rồi nhắn 'research bằng Chrome' sau nhé." |
| Facebook/TikTok hiện xác minh/captcha | Dừng phần đó. "Facebook đang yêu cầu xác minh tài khoản. Bạn tự mở Facebook kiểm tra giúp; hôm nay mình tạm dừng đọc Facebook." |
| Sản phẩm chưa có trụ cột đã duyệt | Câu mẫu trong `mkt-content-calendar` bước 2 |
| Không có quyền sửa bảng | "Bạn chưa có quyền sửa bảng. Nhờ người tạo bảng chia sẻ quyền Người chỉnh sửa." |
| Lỗi lạ, lặp lại | "Có trục trặc kỹ thuật, mình đã ghi vào Digest. Bạn báo người phụ trách kỹ thuật giúp nhé." |
