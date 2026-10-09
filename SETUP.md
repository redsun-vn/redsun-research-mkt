# SETUP — hướng dẫn cài đặt (dành cho Claude thực hiện)

> Người dùng là thành viên team Marketing, **không biết kỹ thuật**. Bạn (Claude) đọc file này và tự thực hiện. Tuân theo `shared/working-rules.md`: tiếng Việt thường, mỗi lần chỉ hướng dẫn **một** thao tác trên giao diện rồi chờ "xong", không bắt họ gõ lệnh.
>
> Mỗi bước có: **Mục tiêu** · **Kiểm tra xong khi** · **Nói với người dùng** · **Nếu lỗi**.

Mở đầu: "Chào bạn! Mình sẽ cài đặt công cụ research cho team Marketing Redsun. Mất khoảng 15 phút. Mình làm phần kỹ thuật, bạn chỉ cần bấm vài chỗ khi mình nhờ."

---

## Bước 1 — Nhận diện đang chạy ở đâu

**Mục tiêu:** biết đang ở Claude Code, Claude Desktop (Cowork) hay chat thường.

- Có công cụ chạy lệnh (Bash) và đang mở thư mục repo này → **Claude Code** hoặc **Cowork có thư mục**. Đi Bước 2A.
- Không đọc được file trên máy (người dùng dán nội dung file vào chat) → **chat thường**. Nói: "Để dùng được hằng ngày, mình cần chạy trong Cowork của Claude Desktop. Bạn mở Claude Desktop, chọn mục **Cowork**, rồi chọn thư mục `redsun-research-mkt` vừa tải về. Xong nhắn mình 'xong'." Sau đó làm lại Bước 1.

**Kiểm tra xong khi:** đọc được file `shared/working-rules.md` trong repo.

---

## Bước 2A — Cài plugin

**Mục tiêu:** các skill `mkt-setup`, `mkt-research`, `mkt-content-calendar` dùng được, kể cả khi chạy theo lịch.

### Nếu là Claude Code
1. Tự chạy (không nhờ người dùng): `claude plugin marketplace add "<đường dẫn tuyệt đối tới thư mục repo>"` rồi `claude plugin install redsun-mkt@redsun-mkt`.
2. Plugin chỉ nạp sau khi khởi động lại. Trong lúc chờ, bạn vẫn làm tiếp được bằng cách **đọc trực tiếp** `skills/<tên>/SKILL.md` trong repo và làm theo.
3. Cuối buổi, nói: "Lần sau mở Claude, các lệnh tắt như /redsun-mkt:research sẽ có sẵn."

**Nếu lỗi:** ghi lại lỗi cho người phụ trách kỹ thuật (xem `docs/operations-runbook.md`), tiếp tục bằng cách đọc trực tiếp các SKILL.md. Không bắt người dùng xử lý.

### Nếu là Claude Desktop / Cowork
Hướng dẫn từng thao tác (một thao tác mỗi lần, chờ "xong"):
1. "Bạn bấm vào **Customize** (Tuỳ chỉnh) ở thanh bên trái."
2. "Chọn **Plugins**."
3. Người dùng có tài khoản GitHub trong nhóm `redsun-vn`: "Bấm **Add marketplace**, dán dòng này: `redsun-vn/redsun-research-mkt`, rồi bấm thêm." → "Tìm **redsun-mkt** trong danh sách và bấm **Install**."
   Không có tài khoản GitHub hoặc bước trên báo lỗi quyền truy cập: "Bấm phần **tải lên plugin** (upload), chọn file `redsun-mkt.zip` trong thư mục `dist` mà mình vừa tạo." (Nếu chưa có file zip và bạn chạy được lệnh: tự chạy `bash scripts/build-desktop-zip.sh` trước.)
4. "Bạn thấy **redsun-mkt** đã bật chưa?"

**Kiểm tra xong khi:** người dùng xác nhận thấy plugin redsun-mkt đã bật.

**Nếu lỗi / giao diện khác mô tả:** nhờ người dùng chụp màn hình gửi bạn, rồi hướng dẫn theo đúng những gì thấy trên ảnh. Không đoán.

---

## Bước 3 — Kết nối Google Drive

**Mục tiêu:** Claude đọc/ghi được Drive của team.

**Kiểm tra:** gọi công cụ Google Drive `search_files` với `title = 'RedSun-MKT-Research'`. Gọi được (kể cả không có kết quả) → đã kết nối, sang Bước 4.

Chưa kết nối, hướng dẫn từng thao tác:
- Desktop/Cowork: "Bấm **Settings** (Cài đặt) → **Connectors** (Kết nối) → tìm **Google Drive** → bấm **Connect** và đăng nhập **tài khoản Google công ty** của bạn." Sau đó: "Bạn mở lại cuộc trò chuyện này, rồi nhắn 'xong'."
- Claude Code: "Bạn mở trình duyệt vào **claude.ai** (cùng tài khoản đang dùng), vào **Settings → Connectors → Google Drive → Connect**, đăng nhập tài khoản Google công ty. Xong nhắn 'xong'." Nếu sau đó vẫn không thấy công cụ Drive: tự kiểm tra lại; vẫn không được thì nói "Bạn thoát Claude rồi mở lại giúp mình nhé" (đây là thao tác duy nhất cần làm ngoài chat).

**Nếu lỗi quyền (Shared Drive):** "Tài khoản của bạn chưa có quyền thêm file vào thư mục chung. Nhờ quản trị Drive cấp quyền 'Người quản lý nội dung' cho bạn."

---

## Bước 4 — (Khuyến nghị) Chrome cho Fanpage/TikTok

**Mục tiêu:** đọc được Fanpage, TikTok, quảng cáo của đối thủ bằng tài khoản thật của người dùng.

Hỏi: "Team muốn research cả Fanpage và TikTok của đối thủ mỗi ngày đúng không? Phần này cần Google Chrome và tiện ích Claude."
1. Đã có công cụ Claude in Chrome → sang 3.
2. Chưa có: "Bạn mở Chrome, vào cửa hàng tiện ích Chrome, tìm **Claude** (của Anthropic) và bấm **Thêm vào Chrome**. Sau đó bấm biểu tượng Claude trên thanh Chrome và đăng nhập cùng tài khoản Claude." Chờ "xong".
3. "Trên Chrome, bạn kiểm tra đã đăng nhập **Facebook** và **TikTok** bằng tài khoản của chính bạn chưa. Lưu ý: dùng tài khoản thật, không dùng tài khoản ảo."

**Nếu không cài được:** ghi nhận, vẫn tiếp tục; research sẽ chạy phần website/xu hướng.

---

## Bước 5 — Cài đặt nội dung (skill mkt-setup)

Chạy skill `mkt-setup` (hoặc đọc `skills/mkt-setup/SKILL.md` và làm theo). Skill này: tạo thư mục trên Drive, phỏng vấn đối thủ/keyword/kênh cho 4 dòng sản phẩm (SaaS, hosting, server, email), soạn Content Strategy nháp, chạy thử research.

**Kiểm tra xong khi:** Drive có thư mục `RedSun-MKT-Research` với `config/config`, `config/strategy`, `config/settings` và ít nhất 1 bảng trong `insights/`.

---

## Bước 6 — Lịch chạy tự động

**Mục tiêu:** research tự chạy mỗi sáng, lịch nội dung tự lập mỗi thứ Hai.

Cần tạo 3 tác vụ theo lịch. Nội dung lời nhắn cho từng tác vụ (người dùng dán nguyên văn):

| Tác vụ | Giờ | Lời nhắn |
|---|---|---|
| Research thường | 08:00 mỗi ngày | `Chạy skill mkt-research của plugin redsun-mkt, chế độ public-auto. Đây là lần chạy theo lịch (trigger=scheduled).` |
| Research Chrome | 08:30 mỗi ngày | `Chạy skill mkt-research của plugin redsun-mkt, chế độ chrome. Đây là lần chạy theo lịch (trigger=scheduled).` |
| Lịch tuần | 09:00 thứ Hai | `Chạy skill mkt-content-calendar của plugin redsun-mkt cho tuần này. Đây là lần chạy theo lịch (trigger=scheduled).` |

**Trên Claude Desktop (Cowork)** — hướng dẫn từng thao tác:
1. "Trong Cowork, bấm mục **Scheduled** (Tác vụ định kỳ) ở thanh bên trái." (Không thấy: nhờ chụp màn hình.)
2. "Bấm **New task** (Tạo tác vụ)."
3. "Dán lời nhắn này vào ô nội dung: `<lời nhắn>`."
4. "Chọn tần suất: <mỗi ngày lúc 08:00 | thứ Hai lúc 09:00>, rồi bấm lưu."
5. Lặp cho 3 tác vụ.

Lưu ý nói với người dùng:
- "Research thường chạy được cả khi máy bạn tắt."
- "Research Chrome cần máy bật, Chrome mở và đã đăng nhập Facebook/TikTok. Nếu sáng đó máy tắt, bạn chỉ cần nhắn Claude 'research bằng Chrome' là được."
- "Nếu công ty tắt tính năng lịch tự động, mỗi sáng bạn nhắn 'research hôm nay' là xong."

**Trên Claude Code:** nói "Trên Claude Code, cách đơn giản nhất là mỗi sáng nhắn 'research hôm nay'. Nếu bạn có Claude Desktop, mình khuyên tạo lịch tự động bên đó." Không bắt người dùng cấu hình gì thêm.

**Kiểm tra xong khi:** người dùng xác nhận đã tạo tác vụ, hoặc chọn chạy tay.

---

## Bước 7 — Kiểm tra cuối và bàn giao

1. Tự kiểm tra trên Drive: có `config/strategy` (`Trạng thái: draft`), có ít nhất 1 bảng `INS_…` và 1 bảng `RUN_…`.
2. Gửi tóm tắt:
```
✅ Đã cài xong!
• Kho dữ liệu: <link>
• Chiến lược nội dung: bản nháp, chờ <người duyệt> duyệt → <link>
• Tự động: <đã tạo 3 lịch / chạy tay>

Hằng ngày bạn chỉ cần nói:
• "Research hôm nay"
• "Research bằng Chrome"
• "Lập lịch tuần sau"
• "Kho insight tuần này có gì về hosting?"
```
