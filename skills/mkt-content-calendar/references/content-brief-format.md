# Format chuẩn khi viết idea / brief

Dùng khi người dùng xin "viết idea", "viết brief", "viết kịch bản", "làm nội dung cho bài …", hoặc muốn đưa idea cho agent tạo video / tạo nội dung.

## Nguyên tắc

- **Mỗi idea là một khối chữ thường, copy nguyên khối là dùng được**: dán cho agent tạo video, agent viết bài, hoặc gửi cho người làm. Không dùng JSON, không dùng bảng, không dùng mã code.
- Đoạn đầu khối là **lời giao việc** cho agent, nên người dùng không cần viết thêm gì.
- Câu ngắn, tiếng Việt thường. Mỗi dòng một ý.
- Chỉ dùng số liệu có trong Research database hoặc Nguồn theo dõi. Số chưa có thì ghi `[cần team xác nhận: …]`, không tự điền.
- Không nêu tên đối thủ, không so sánh trực tiếp với đối thủ trong nội dung đăng công khai. Thông tin đối thủ chỉ dùng để chọn góc, và chỉ ghi ở dòng "Dựa trên".
- Mỗi khối luôn ghi mã lịch, mã quan sát (OB) và mã trụ cột để truy ngược.
- Trả lời trong chat theo đúng khuôn bên dưới, mỗi idea một khối, giữa các khối có một dòng trống. Không thêm lời dẫn dài trước hoặc sau.

## Khuôn 1 — Video (TikTok, Reels, YouTube Shorts)

```
==================== IDEA <số>: <tên ngắn, ≤ 10 chữ> ====================
Giao việc: Bạn là người làm video cho <SẢN PHẨM>. Hãy làm video theo brief dưới đây. Giữ đúng thông điệp, không thêm số liệu hay tính năng ngoài brief.

Sản phẩm: <SẢN PHẨM>
Kênh: <TikTok / Reels / Shorts> — ngày đăng <DD/MM/YYYY>
Định dạng: video dọc 9:16, dài <N> giây, có phụ đề tiếng Việt
Người xem: <ai, 1 dòng>
Mục tiêu: <muốn người xem làm/nghĩ gì, 1 dòng>
Thông điệp chính: <1 câu>
Giọng điệu: <ví dụ: đời thường, hài nhẹ, đồng cảm>

Kịch bản:
Cảnh 1 (0–3 giây)
- Hình: <thấy gì>
- Chữ trên màn hình: <…>
- Lời nói: <… hoặc "không có">
Cảnh 2 (3–10 giây)
- Hình: …
- Chữ trên màn hình: …
- Lời nói: …
(… thêm cảnh, tổng đúng <N> giây; cảnh cuối có logo + CTA)

Nhạc / âm thanh: <ví dụ: nhạc nền không lời, được phép dùng thương mại>
Caption: <caption đăng kèm, có 3–5 hashtag>
CTA: <1 hành động>

Không được: <liệt kê ngắn>
Cần team cung cấp: <logo, ảnh/màn hình thật, giọng đọc…>
Cần team xác nhận: <số liệu/chính sách chưa chắc | không có>

Dựa trên: <OB… — tóm tắt 1 câu quan sát> · Trụ cột <mã> <tên trụ cột> · Mã lịch <CAL-…>
==========================================================================
```

## Khuôn 2 — Bài đăng / Carousel (Facebook, blog ngắn, email)

```
==================== IDEA <số>: <tên ngắn, ≤ 10 chữ> ====================
Giao việc: Bạn là người viết nội dung cho <SẢN PHẨM>. Hãy làm <bài viết / carousel N ảnh> theo brief dưới đây. Giữ đúng thông điệp, không thêm số liệu hay tính năng ngoài brief.

Sản phẩm: <SẢN PHẨM>
Kênh: <Facebook / Blog / Email> — ngày đăng <DD/MM/YYYY>
Định dạng: <carousel N ảnh, khổ 4:5 | bài viết khoảng N chữ>
Người xem: <ai>
Mục tiêu: <…>
Thông điệp chính: <1 câu>
Giọng điệu: <…>

Nội dung:
Ảnh 1 — Tiêu đề: <…>
         Nội dung: <… hoặc để trống>
         Hình gợi ý: <…>
Ảnh 2 — Tiêu đề: …
         Nội dung: …
         Hình gợi ý: …
(… với bài viết: Mở bài / Thân bài (các ý chính) / Kết bài)

Caption: <…>
CTA: <1 hành động>

Không được: <…>
Cần team cung cấp: <…>
Cần team xác nhận: <… | không có>

Dựa trên: <OB… — tóm tắt 1 câu> · Trụ cột <mã> <tên> · Mã lịch <CAL-…>
==========================================================================
```

## Kiểm tra trước khi gửi

- [ ] Có mã OB, mã trụ cột, mã lịch ở dòng "Dựa trên"; mã có thật trong Sheet.
- [ ] Không có tên đối thủ trong phần nội dung đăng (Kịch bản/Nội dung/Caption).
- [ ] Mọi con số đều có trong Sheet, hoặc đã ghi `[cần team xác nhận]`.
- [ ] Video: tổng thời lượng các cảnh đúng bằng số giây đã ghi.
- [ ] Không dùng JSON, bảng hay thuật ngữ kỹ thuật.
