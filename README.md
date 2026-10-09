# Công cụ Research Marketing — redsun.vn

Claude research đối thủ và khách hàng mỗi ngày (Fanpage, TikTok, YouTube, blog/bảng giá, quảng cáo Meta, tìm kiếm) cho SIPOS, WEBINO, REDSUN BOS, ghi vào **một Google Sheet chung của team** (Research database: Quan sát → Căn cứ → Ý nghĩa → Content Idea), và lập **Content Calendar tuần** ngay khi bạn hỏi — mỗi bài đều truy ngược được về quan sát thật và trụ cột chiến lược đã duyệt.

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

Bạn cần có: tài khoản Claude do công ty cấp, tài khoản Google công ty (Claude sẽ nhờ bạn kết nối Google Drive và Google Sheets). Nếu muốn research Fanpage/TikTok: Google Chrome đã đăng nhập Facebook và TikTok bằng tài khoản của chính bạn.

## Cần bật những gì

**Người quản trị Claude Team (Owner) bật một lần cho cả công ty** — claude.ai → Organization settings. Hướng dẫn từng bước và tin nhắn mẫu: [`docs/owner-setup-guide.md`](docs/owner-setup-guide.md).

| # | Vào mục | Bật gì |
|---|---|---|
| 1 | Capabilities | Bật **Web search** |
| 2 | Capabilities | Bật **Cloud code execution and file creation** |
| 3 | Plugins & skills → Policy | Bật **Skills** |
| 4 | Plugins & skills | Bật cho phép thành viên **thêm plugin** |
| 5 | Connectors → Browse connectors | Thêm **Google Drive** (Add to your team) |
| 6 | Connectors → Browse connectors | Thêm **Google Sheets** (Add to your team), đặt quyền ghi/sửa là **Always allow** |
| 7 | Claude in Chrome | Bật **Enable for your team** |
| 8 | Cowork | Bật **Enable for your organization** |
| 9 | Cowork | Bật **Run Cowork in the cloud** (để research chạy khi máy tắt) |

Nếu kết nối Google báo "ứng dụng bị chặn": **quản trị Google** vào admin.google.com → Security → Access and data control → API controls → Manage third-party app access → đặt **Claude** là **Trusted**.

**Mỗi thành viên MKT tự làm** (Claude sẽ hướng dẫn khi cài đặt):
- Kết nối **Google Drive** và **Google Sheets** bằng tài khoản Google công ty (Settings → Connectors → Connect).
- Cài tiện ích **Claude in Chrome**, đăng nhập Claude; trên Chrome đăng nhập Google, Facebook, TikTok bằng tài khoản thật của mình.
- Được chia sẻ quyền **Người chỉnh sửa** trên bảng **Redsun MKT — Research database**.

Không cần: Gmail, Google Calendar, Google Docs, Google Slides.

## Dùng hằng ngày

Mở Claude và nói một trong các câu sau:

| Bạn nói | Claude làm |
|---|---|
| **Research hôm nay** | Đọc blog/bảng giá đối thủ, tìm kiếm, xu hướng → thêm insight, quan sát và Content Idea vào bảng |
| **Research bằng Chrome** | Đọc Fanpage, TikTok, quảng cáo của đối thủ (cần Chrome đang mở) |
| **Lập lịch tuần sau** | Lập Content Calendar từ Content Idea + trụ cột đã duyệt (chạy ngay, bất cứ lúc nào) |
| **Hôm nay làm nội dung gì?** / **Viết idea cho bài CAL-2026-W42-01** | Trả về từng idea theo khuôn chuẩn: copy nguyên khối dán cho agent tạo video, tạo nội dung, hoặc gửi người làm |
| **Kho insight tuần này có gì về SIPOS?** | Tóm tắt kèm mã quan sát và link nguồn |
| **Thêm đối thủ X cho WEBINO** / **Thêm sản phẩm hosting** | Cập nhật tab Nguồn theo dõi (sản phẩm mới có chiến lược nháp chờ duyệt) |

Nếu đã tạo lịch tự động lúc cài đặt, research sẽ tự chạy mỗi sáng thứ Hai–thứ Sáu (mỗi ngày một sản phẩm theo vòng). Mọi kết quả nằm trong Google Sheet **Redsun MKT — Research database**.

## Khi có bản mới

Người phụ trách kỹ thuật sẽ báo trong nhóm chat khi có bản mới. Khi nhận được thông báo:

1. Mở Claude **trong thư mục `redsun-research-mkt`** (Claude Desktop: Cowork → chọn thư mục; Claude Code: mở trong thư mục).
2. Dán câu này và gửi:

   > Đọc file UPDATE.md và cập nhật giúp tôi.

3. Làm theo từng bước Claude nhờ (thường chỉ bấm **Update** hoặc tải lại file ZIP), rồi mở cuộc trò chuyện mới.

Dữ liệu trong Google Sheet **không bị ảnh hưởng**. Muốn xem bản mới có gì: mở file `CHANGELOG.md`, hoặc hỏi Claude "bản mới có gì?".

## Duyệt (dành cho trưởng nhóm MKT)

Mở Google Sheet **Redsun MKT — Research database**:
- Tab **Chiến lược content**: cột Trạng thái. Chỉ trụ cột `đã duyệt` mới được dùng cho lịch tuần. Trụ cột mới Claude soạn luôn là `nháp` — bạn đọc, sửa nếu cần, rồi đổi thành `đã duyệt`.
- Tab **Research database**: Content Idea ở trạng thái `gợi ý, chờ người duyệt`; bạn có thể đổi thành `đã duyệt` hoặc `bỏ` (ý tưởng `bỏ` sẽ không vào lịch).
- Tab **Content Calendar**: mọi dòng là `đề xuất, chờ duyệt`; điền Người phụ trách và đổi trạng thái khi chốt.

Quy tắc: không chèn dòng, không sắp xếp lại các bảng Claude đang ghi.

## Lưu ý khi dùng Chrome

Claude chỉ **đọc** trang bằng tài khoản bạn đang đăng nhập: không thích, không bình luận, không nhắn tin, mỗi lượt tối đa 30 trang trong 20 phút (chỉnh ở tab Nguồn theo dõi). Nếu Facebook/TikTok hiện yêu cầu xác minh, Claude sẽ dừng ngay. Dùng tài khoản thật, không dùng tài khoản ảo.

---

Người phụ trách kỹ thuật: xem `docs/operations-runbook.md`.

REPO: redsun-vn/redsun-research-mkt
