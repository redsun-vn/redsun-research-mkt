# Quy tắc soạn lịch tuần

## Chọn insight cho pillar

1. Lọc insight cùng `product_line` với pillar (pillar `general` dùng insight của mọi dòng).
2. Ưu tiên theo thứ tự:
   - insight có tag khớp mục tiêu pillar (pillar về giá/chi phí → `offer`, `pain_point`; pillar về nhận diện → `topic`, `content_pattern`);
   - insight được xác nhận ở ≥2 nguồn (evidence ghi "cũng thấy ở…");
   - insight mới hơn.
3. Không dùng một insight cho quá 2 bài trong cùng tuần.
4. `angle` phải trả lời được câu hỏi "insight nào cho thấy khách quan tâm điều này?" — nếu không trả lời được thì bỏ bài đó.

## Phân bổ

- Tần suất trong strategy (ví dụ "facebook 3 bài/tuần") quyết định số bài mỗi kênh.
- Tỷ trọng (%) của pillar quyết định chia số bài giữa các pillar cùng kênh; làm tròn, ưu tiên pillar có nhiều insight hơn khi phải cắt.
- Pillar không có insight phù hợp → không tạo bài, ghi vào "Cần research thêm".
- Không xếp hai bài cùng dòng sản phẩm vào cùng ngày trên cùng kênh nếu tránh được.

## Định dạng gợi ý theo kênh

| Kênh | Định dạng thường dùng |
|---|---|
| facebook | bài viết, carousel, video ngắn |
| tiktok | video ngắn |
| website-blog | bài blog |
| email | email |

Dùng đúng tên kênh như trong config.

## Mẫu file review (Doc `CAL_YYYY-Www_review`)

```
LỊCH NỘI DUNG TUẦN <YYYY-Www> — GIẢI THÍCH

Nguồn dữ liệu: <số> insight từ <ngày> đến <ngày>; strategy duyệt ngày <ngày>.
Cách kiểm tra: <máy kiểm tra (validate_trace) — 0 lỗi | kiểm tra thủ công>

1. ĐỘ PHỦ PILLAR
- P-HOSTING-01 Chi phí minh bạch: 2 bài (CAL-…-01, CAL-…-04) — dựa trên INS-…, INS-…
- P-EMAIL-01 …: 0 bài — thiếu insight

2. INSIGHT ĐƯỢC DÙNG
- INS-… (Bnix, giá gia hạn): CAL-…-01

3. CẦN RESEARCH THÊM
- Pillar <…>: chưa có insight về <…>. Gợi ý: research <đối thủ/kênh/keyword>.

4. ĐÃ LOẠI (không truy vết được)
- CAL-…-07: insight INS-… không tồn tại trong kho
(hoặc "Không có")
```
