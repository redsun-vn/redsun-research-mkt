# DAILY — dùng hằng ngày (dành cho Claude thực hiện)

> Người dùng là team Marketing, không biết kỹ thuật. Tuân theo `shared/working-rules.md`. Nếu chưa cài đặt (không thấy thư mục `RedSun-MKT-Research` trên Drive) → làm theo `SETUP.md`.

## Người dùng nói gì → Claude làm gì

| Người dùng nói (ví dụ) | Việc của Claude |
|---|---|
| "Research hôm nay", "chạy research", "cập nhật insight" | Skill `mkt-research`, chế độ `public-auto` |
| "Research bằng Chrome", "xem Fanpage/TikTok đối thủ", "research đầy đủ" | Skill `mkt-research`, chế độ `chrome` |
| "Lập lịch tuần sau", "content calendar tuần này" | Skill `mkt-content-calendar` |
| "Kho insight có gì về <chủ đề/dòng SP/đối thủ>?", "tuần này có gì mới?" | Đọc các bảng trong `insights/` (mặc định 7 ngày), lọc theo yêu cầu, tóm tắt 5–10 ý **kèm link nguồn và insight_id**. Không thêm ý không có trong kho |
| "Thêm đối thủ…", "bỏ keyword…", "sửa cấu hình" | Skill `mkt-setup`, phần sửa cấu hình (tạo bản mới, chuyển bản cũ vào `config/_cu/`) |
| "Duyệt strategy giúp tôi", "strategy đã ổn chưa?" | Đọc `config/strategy`, tóm tắt các pillar. Chỉ người duyệt được nêu trong file mới đổi sang `approved`: hướng dẫn họ mở file và tự sửa dòng trạng thái. **Không tự đổi.** |
| "Hôm qua research có chạy không?" | Đọc bảng mới nhất trong `runs/`, báo giờ chạy, số insight, nguồn bị chặn |

Câu không khớp bảng → hỏi lại một câu ngắn để làm rõ.

## Báo kết quả

- Mở đầu bằng kết quả, tối đa 5 dòng, kèm link Drive.
- Có nguồn bị chặn: nói đời thường ("Facebook yêu cầu đăng nhập lại", "trang TikTok không tải được") và việc người dùng cần làm nếu có.
- Không dán bảng dữ liệu thô vào chat trừ khi người dùng xin.

## Khi có sự cố

| Tình huống | Nói với người dùng |
|---|---|
| Không kết nối được Google Drive | "Mình chưa vào được Google Drive. Bạn làm giúp mình bước kết nối Drive nhé" → `SETUP.md` Bước 3 |
| Chrome không kết nối | "Chrome chưa mở hoặc chưa bật tiện ích Claude. Hôm nay mình research phần website trước, bạn mở Chrome rồi nhắn 'research bằng Chrome' sau nhé." |
| Facebook/TikTok hiện xác minh/captcha | Dừng phần đó ngay. "Facebook đang yêu cầu xác minh tài khoản. Bạn tự mở Facebook kiểm tra giúp; mình tạm dừng đọc Facebook hôm nay." |
| Strategy chưa duyệt khi lập lịch | Câu mẫu trong skill `mkt-content-calendar` bước 2 |
| Lỗi lạ, lặp lại | "Có trục trặc kỹ thuật, mình đã ghi lại. Bạn báo người phụ trách kỹ thuật giúp nhé." Ghi chi tiết vào cột `reason` của run log |
