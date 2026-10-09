# Quy tắc soạn lịch tuần

Thông số lấy từ tab **Chiến lược content** (dòng `thông tin`). Bảng mẫu team chốt ngày 09/10/2026; nếu bảng đổi, theo bảng.

## Nhịp đăng (dòng KÊNH)

- Đăng 5 ngày/tuần, thứ Hai đến thứ Sáu.
- Facebook: 1 bài hoặc video mỗi ngày **mỗi Fanpage**. TikTok: 1 video mỗi ngày.
- Chỉ xếp lịch cho kênh mà sản phẩm **đã có** (dòng `của mình` trong Nguồn theo dõi có link). Zalo OA chưa đưa vào lịch.
- Ví dụ với bảng mẫu: SIPOS có Fanpage + TikTok → 10 bài/tuần; WEBINO chưa có Fanpage/TikTok → 0 bài, ghi "Cần chuẩn bị kênh".

## Tỷ lệ (dòng TỶ LỆ)

- 60% trụ cột **giai đoạn hiện tại** (`giai_doan` chứa "hiện tại").
- 25% trụ cột **giai đoạn trước**.
- 15% **theo ngành / nhóm khách** (mã SV-*, WG*…). Ưu tiên ngành mũi nhọn (dòng NN).
- Làm tròn theo số bài; thiếu quan sát cho nhóm nào thì chuyển phần thiếu sang nhóm còn quan sát và ghi lại trong Digest.

## Vai trò kênh (dòng K-*) và thông điệp (TM-*)

- Facebook (SIPOS): kênh chủ lực, đánh ngành sâu, thông điệp riêng từng ngành → định dạng bài viết/carousel/video.
- TikTok (SIPOS): tạo nhu cầu, video 20–40 giây, tình huống thực tế, nói vấn đề không nói tính năng → `goc_tieu_de` dạng tình huống.
- Góc/tiêu đề không trái thông điệp chủ đạo của sản phẩm.

## Chọn Content Idea

1. Lọc quan sát cùng sản phẩm, `trang_thai` khác `mốc`/`bỏ`, có Content Idea.
2. Khớp với trụ cột: Content Idea hoặc Ý nghĩa liên quan trực tiếp tới `tru_cot`/`goc`/`chu_de_de_xuat` của trụ cột. Không khớp rõ ràng → không ép.
3. Ưu tiên: `so_lan_thay` cao → độ tin cậy `cao`/`vừa` → `ngay_gan_nhat` mới.
4. Một quan sát dùng tối đa 2 bài/tuần (khác kênh hoặc khác góc).
5. Content Idea có điều kiện ("cần xác minh", "chưa nên làm…") → bỏ qua, ghi vào Digest "chờ xác minh".

## Định dạng gợi ý

| Kênh | Định dạng |
|---|---|
| Facebook | bài viết, carousel, video ngắn |
| TikTok | video ngắn 20–40 giây |

## Ví dụ một dòng hợp lệ

```
CAL-2026-W42-01 | 2026-W42 | 2026-10-12 | Facebook | SIPOS | S3.1 | OB004 |
"Phần mềm + thiết bị: tổng chi phí năm đầu thật sự là bao nhiêu?" | carousel | Nhắn tin nhận bảng giá | | đề xuất, chờ duyệt
```
OB004 có Content Idea "So sánh tổng chi phí một năm khi dùng phần mềm kèm thiết bị"; S3.1 "Quyết định ngay — Chậm là mất cơ hội" (giai đoạn hiện tại, đã duyệt).
