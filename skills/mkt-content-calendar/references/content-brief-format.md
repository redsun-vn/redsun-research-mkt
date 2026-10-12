# Format chuẩn khi viết idea / brief

Dùng khi người dùng xin "viết idea", "viết brief", "viết kịch bản", "làm nội dung cho bài …", hoặc muốn đưa idea cho redsun-reels (làm video) / agent tạo nội dung.

## Nguyên tắc

- **Bán giải pháp, không bán phần mềm** — theo `shared/working-rules.md` mục "Cách nói về sản phẩm": mô hình kinh doanh → bài toán (tình huống + hậu quả) → quy trình cách mới → tính năng là bằng chứng.
- **Mỗi idea là một khối chữ thường, copy nguyên khối là dùng được**. Không dùng JSON, không dùng bảng, không dùng mã code.
- Câu ngắn, tiếng Việt thường. Mỗi dòng một ý.
- Chỉ dùng số liệu, lời khách có trong Research database / Insight hằng ngày / Digest / Nguồn theo dõi, kèm link. Số chưa có thì ghi `[cần team xác nhận: …]`, không tự điền.
- Lời khách: trích **nguyên văn** kèm link bài/bình luận; không ghi tên, ảnh, link trang cá nhân người viết.
- Tính năng chỉ lấy từ `tinhNang` trong luật reels đã đọc (`brand/products.json`); tính năng khác ghi `[cần team xác nhận: …]`.
- Đối thủ: trong khối **VÌ SAO ĐÁNG LÀM** (nội bộ) được nêu tên để giải thích góc. Phần nội dung đăng (Nguyên liệu cho reels, Nội dung, Caption) **không** nêu tên, không so sánh trực tiếp.
- Mỗi khối luôn ghi mã lịch, mã quan sát (OB) và mã trụ cột để truy ngược.
- Trả lời trong chat theo đúng khuôn bên dưới, mỗi idea một khối, giữa các khối có một dòng trống. Không thêm lời dẫn dài trước hoặc sau.

## Khối chung — VÌ SAO ĐÁNG LÀM (dùng cho cả hai khuôn)

```
VÌ SAO ĐÁNG LÀM
- Mô hình kinh doanh: <mo_hinh>
- Insight: <1 câu: điều mình thấy và vì sao quan trọng với mô hình này>
- Căn cứ: <OB…> thấy <so_lan_thay> lần, độ tin cậy <…> — <nguồn ngắn + URL>
- Lời khách: "<câu nguyên văn>" — <URL> | không có
- Đối thủ đang nói: <…> → góc mình khác: <…>
```

## Khuôn 1 — Video (TikTok, Reels, YouTube Shorts): gói nguyên liệu cho redsun-reels

Brief video **không viết cảnh, không viết lời thoại, không chấm điểm câu mở, không chọn kiểu hình**. redsun-reels tự viết 3 concept theo 3 kiểu kể, tự chấm câu mở; MKT chọn kiểu hình và concept trong reels. Brief chỉ đưa đủ nguyên liệu thật để reels không phải hỏi lại.

```
==================== IDEA <số>: <tên ngắn, ≤ 10 chữ> ====================
Dán vào redsun-reels: "làm reel cho <SẢN PHẨM> theo brief dưới đây"

Sản phẩm: <SẢN PHẨM> · Kênh: <TikTok / Reels / Shorts> — <DD/MM/YYYY> · Mã lịch <CAL-…>
Loại video gợi ý: <mã videoType trong luật reels> (<tên>) · Dài: <N trong 15–30> giây
Người xem: <mô hình kinh doanh + vai trò, vd. chủ quán cafe mang đi tự đứng quầy>
Mục tiêu: <người xem nghĩ gì, và làm đúng hành động ở CTA>
Giọng điệu: <…> · CTA: <defaultCta trong luật reels | theo chiến lược>

VÌ SAO ĐÁNG LÀM
<khối chung>

NGUYÊN LIỆU CHO REELS
- Bài toán: <mô hình> gặp <tình huống: lúc nào, ở đâu, ai làm gì> → <hậu quả thấy được: mất tiền/giờ/khách>
- Cách mới (giải pháp): <quy trình mới, người xem làm khác đi thế nào> — bằng chứng: <tên tính năng trong tinhNang | [cần team xác nhận: tính năng nào gỡ việc này]>
- Ứng viên câu mở (3–5):
  · (<vỡ lẽ | hậu quả | nỗi đau | vật gây tò mò | đối lập | con số thật | lời đắt giá>) <nội dung> — <nguồn: OB… / URL>
  · …
- Số liệu: <số + nguồn | không có → không dùng kiểu kể meo-so-lieu>
- Kiểu kể hợp: <pov, tieu-pham, twist (+ meo-so-lieu khi có số thật)> — tieu-pham và twist không làm được với clip quay sẵn
- Không được: <hứa vượt tính năng; nêu tên đối thủ; số ngoài nguồn; …>
- Cần team cung cấp: <ảnh/quay màn hình tính năng thật | không có>
- Cần team xác nhận: <… | không có>

Dựa trên: <OB…> · Trụ cột <mã> <tên> · Mã lịch <CAL-…> · Luật reels main@<sha7>
==========================================================================
```

Cách điền:
- **Loại video**: chọn mã `id` trong `config/video-types.ts` có sản phẩm này trong `products`; ưu tiên loại bán giải pháp (không thuộc `NO_PAIN_TYPES`) như `truoc-sau`, `so-sanh`, `meo-hay`, `cau-hoi-thuong-gap`, `ra-mat-tinh-nang`. Số giây nằm trong khoảng của loại đó **giao** 15–30. Loại cần ảnh/clip/lời khách thật có đồng ý (`khach-hang-noi`, `video-co-nguoi-noi`, `so-lieu-thanh-tich`, `khuyen-mai`) chỉ chọn khi Sheet đã có đủ; không thì chọn loại khác.
- **Ứng viên câu mở**: lấy từ nguyên liệu thật (lời khách, hậu quả, tình huống, số liệu). Không tự chấm điểm.
- **Mục tiêu và CTA**: hành động trong Mục tiêu trùng với CTA (CTA là `defaultCta` "…tại sipos.vn" thì mục tiêu là vào web, không phải nhắn tin). Không hứa "demo", "tư vấn", "dùng thử" khi chưa có nguồn.
- **Kiểu kể**: reels viết 3 concept thuộc 3 kiểu kể khác nhau và kiểu kể còn tuỳ kiểu hình MKT chọn sau, nên mặc định ghi `pov, tieu-pham, twist`; thêm `meo-so-lieu` chỉ khi dòng Số liệu có số thật kèm nguồn (`canSoThat`). Không loại kiểu kể theo cảm tính. Ghi thêm: "tieu-pham và twist không làm được với clip quay sẵn".
- **Chưa đủ để gửi reels**: dòng Bài toán hoặc bằng chứng của Cách mới còn trống / chỉ có `[cần team xác nhận]` về **nỗi đau** (không phải tính năng), hoặc có dưới 3 ứng viên câu mở → thay dòng "Dán vào redsun-reels…" bằng `TRẠNG THÁI: chưa gửi redsun-reels — chờ team bổ sung`, và viết dòng "Cần team xác nhận" thành câu hỏi có lựa chọn sẵn (vd. "Chủ khách sạn mất gì khi nhận phòng bằng sổ: tiền / giờ / khách?"). Chỉ thiếu tính năng trong `tinhNang` thì vẫn gửi được (reels sẽ hỏi team về tính năng).

## Khuôn 2 — Bài đăng / Carousel (Facebook, blog ngắn, email)

```
==================== IDEA <số>: <tên ngắn, ≤ 10 chữ> ====================
Giao việc: Bạn là người viết nội dung cho <SẢN PHẨM>. Hãy làm <bài viết / carousel N ảnh> theo brief dưới đây. Giữ đúng thông điệp, không thêm số liệu hay tính năng ngoài brief.

Sản phẩm: <SẢN PHẨM>
Kênh: <Facebook / Blog / Email> — ngày đăng <DD/MM/YYYY>
Định dạng: <carousel N ảnh, khổ 4:5 | bài viết khoảng N chữ>
Người xem: <mô hình kinh doanh + vai trò>
Mục tiêu: <…>
Thông điệp chính: <1 câu>
Giọng điệu: <…>

VÌ SAO ĐÁNG LÀM
<khối chung>

BÀI TOÁN → CÁCH MỚI
- Bài toán: <mô hình> gặp <tình huống> → <hậu quả>
- Cách cũ đang làm: <…>
- Cách mới: <quy trình mới>
- Bằng chứng: <tính năng | [cần team xác nhận: …]>

Nội dung:
Ảnh 1 — Tiêu đề: <mở bằng bài toán, không bằng tên tính năng>
         Nội dung: <… hoặc để trống>
         Hình gợi ý: <…>
Ảnh 2 — Tiêu đề: …
         Nội dung: …
         Hình gợi ý: …
(… với bài viết: Mở bài (bằng bài toán) / Thân bài (các ý chính) / Kết bài)

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
- [ ] Có dòng mô hình kinh doanh; mở bằng bài toán, không bằng tính năng.
- [ ] Có ít nhất một căn cứ thật kèm link.
- [ ] Không có tên đối thủ trong phần nội dung đăng (Nguyên liệu cho reels / Nội dung / Caption).
- [ ] Mọi con số đều có nguồn trong Sheet, hoặc đã ghi `[cần team xác nhận]`.
- [ ] Lời khách nguyên văn, kèm link, không kèm tên/ảnh người viết.
- [ ] Video: hành động trong Mục tiêu trùng CTA; đủ điều kiện gửi reels (có bài toán thật, ≥ 3 ứng viên câu mở) hoặc đã ghi `TRẠNG THÁI: chưa gửi redsun-reels`.
- [ ] Video: không có "Cảnh"; dài 15–30 giây; loại video và kiểu kể là mã có trong luật reels đã đọc; tính năng có trong `tinhNang` hoặc ghi `[cần team xác nhận]`; có ghi phiên bản luật reels.
- [ ] Không dùng JSON, bảng hay thuật ngữ kỹ thuật.
