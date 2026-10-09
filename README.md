# Công cụ Research Marketing — redsun.vn

Claude tự động research đối thủ và khách hàng mỗi ngày (website, Google Trends, Fanpage, TikTok, quảng cáo), lưu thành kho insight trên Google Drive của team, và lập **lịch nội dung tuần** mà mỗi ý tưởng đều truy ngược được về insight thật và chiến lược nội dung.

Bạn **không cần biết kỹ thuật**. Claude làm hết, bạn chỉ trả lời câu hỏi và bấm vài chỗ khi Claude nhờ.

## Cài đặt (làm 1 lần, khoảng 15 phút)

1. **Tải thư mục này về máy.** Mở https://github.com/redsun-vn/redsun-research-mkt (đăng nhập GitHub bằng tài khoản đã được mời vào nhóm `redsun-vn`), bấm nút xanh **Code** → **Download ZIP**, rồi giải nén (bấm đúp vào file zip). Bạn sẽ có thư mục `redsun-research-mkt`.
   Chưa có tài khoản GitHub? Nhờ người phụ trách kỹ thuật gửi file zip của thư mục này.
2. **Mở Claude:**
   - **Claude Desktop** (khuyên dùng): mở ứng dụng, chọn **Cowork**, chọn thư mục `redsun-research-mkt` vừa giải nén.
   - **Claude Code**: mở Claude Code trong thư mục `redsun-research-mkt`.
3. **Dán câu này vào Claude và gửi:**

   > Đọc file SETUP.md trong thư mục này và cài đặt giúp tôi.

Claude sẽ hướng dẫn từng bước. Khi Claude nhờ bấm gì đó, làm xong thì nhắn **"xong"**.

Bạn cần có: tài khoản Claude của công ty (gói Team), tài khoản Google công ty. Nếu muốn research Fanpage/TikTok: Google Chrome đã đăng nhập Facebook và TikTok bằng tài khoản của chính bạn.

## Dùng hằng ngày

Mở Claude và nói một trong các câu sau:

| Bạn nói | Claude làm |
|---|---|
| **Research hôm nay** | Đọc website đối thủ, Google Trends, tìm kiếm → thêm insight vào kho |
| **Research bằng Chrome** | Đọc Fanpage, TikTok, quảng cáo của đối thủ (cần Chrome đang mở) |
| **Lập lịch tuần sau** | Lập lịch nội dung từ insight + chiến lược đã duyệt |
| **Kho insight tuần này có gì về hosting?** | Tóm tắt insight kèm link nguồn |
| **Thêm đối thủ X cho dòng email** | Cập nhật cấu hình |

Nếu đã tạo lịch tự động lúc cài đặt, research và lịch tuần sẽ tự chạy. Kết quả nằm trong thư mục **RedSun-MKT-Research** trên Google Drive.

## Duyệt chiến lược nội dung (dành cho trưởng nhóm MKT)

Lúc cài đặt, Claude soạn **bản nháp** chiến lược nội dung từ câu trả lời của team. Lịch tuần chỉ được lập sau khi bản nháp được duyệt:
1. Mở Google Drive → `RedSun-MKT-Research` → `config` → `strategy`.
2. Đọc, sửa trực tiếp nếu cần.
3. Đổi dòng `Trạng thái: draft` thành `Trạng thái: approved`, điền ngày duyệt.

## Lưu ý khi dùng Chrome

Claude chỉ **đọc** trang bằng tài khoản bạn đang đăng nhập: không thích, không bình luận, không nhắn tin, mỗi trang chỉ xem khoảng 10 bài gần nhất. Nếu Facebook/TikTok hiện yêu cầu xác minh, Claude sẽ dừng ngay. Dùng tài khoản thật, không dùng tài khoản ảo.

---

Người phụ trách kỹ thuật: xem `docs/operations-runbook.md`.

REPO: redsun-vn/redsun-research-mkt
