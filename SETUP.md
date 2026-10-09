# SETUP — hướng dẫn cài đặt (dành cho Claude thực hiện)

> Người dùng là thành viên team Marketing, **không biết kỹ thuật**. Bạn (Claude) đọc file này và tự thực hiện. Tuân theo `shared/working-rules.md`: tiếng Việt thường, mỗi lần chỉ hướng dẫn **một** thao tác trên giao diện rồi chờ "xong", không bắt họ gõ lệnh.
>
> Mỗi bước có: **Mục tiêu** · **Xong khi** · **Nói với người dùng** · **Nếu lỗi**.

Mở đầu: "Chào bạn! Mình sẽ cài công cụ research cho team Marketing Redsun, khoảng 15 phút. Phần kỹ thuật mình làm, bạn chỉ cần bấm vài chỗ khi mình nhờ."

---

## Bước 1 — Nhận diện đang chạy ở đâu

- Đọc được file `shared/working-rules.md` trong thư mục này → đang ở **Claude Code** hoặc **Cowork** có thư mục. Sang Bước 2.
- Không đọc được file trên máy → đang ở chat thường. Nói: "Để dùng hằng ngày, mình cần chạy trong Cowork của Claude Desktop. Bạn mở Claude Desktop, chọn **Cowork**, rồi chọn thư mục `redsun-research-mkt` vừa tải về. Xong nhắn 'xong'." Làm lại Bước 1.

---

## Bước 2 — Cài bộ công cụ (plugin)

**Mục tiêu:** có 3 kỹ năng `mkt-setup`, `mkt-research`, `mkt-content-calendar`, kể cả khi chạy theo lịch.

**Claude Code** — tự làm, không nhờ người dùng:
1. `claude plugin marketplace add "<đường dẫn tuyệt đối thư mục repo>"` rồi `claude plugin install redsun-mkt@redsun-mkt`.
2. Kỹ năng chỉ nạp sau khi mở lại Claude. Trong lúc chờ, **đọc trực tiếp** `skills/<tên>/SKILL.md` trong repo và làm theo.
3. Lỗi → ghi lại cho người phụ trách kỹ thuật (`docs/operations-runbook.md`) và tiếp tục bằng cách đọc trực tiếp SKILL.md.

**Claude Desktop / Cowork** — hướng dẫn từng thao tác:
1. "Bạn bấm **Customize** (Tuỳ chỉnh) ở thanh bên trái." → "Chọn **Plugins**."
2. Người dùng có tài khoản GitHub trong nhóm `redsun-vn`: "Bấm **Add marketplace**, dán `redsun-vn/redsun-research-mkt`, bấm thêm." → "Tìm **redsun-mkt**, bấm **Install**."
   Không có tài khoản GitHub hoặc báo lỗi quyền: nếu chạy được lệnh thì tự chạy `bash scripts/build-desktop-zip.sh`, rồi nói "Bấm phần **tải lên plugin** (Upload), chọn file `redsun-mkt.zip` trong thư mục `dist`." Không chạy được lệnh → nhờ người phụ trách kỹ thuật gửi file đó.
3. "Bạn thấy **redsun-mkt** đã bật chưa?"

**Xong khi:** người dùng xác nhận plugin đã bật (Desktop) hoặc lệnh cài thành công (Code).

---

## Bước 3 — Cho Claude đọc/ghi Google Sheet

**Mục tiêu:** Claude đọc/ghi được bảng dữ liệu. Có 2 cách (chi tiết kỹ thuật: `shared/sheet-access.md`):
- **Cách 1 — Kết nối Google Drive + Google Sheets** (khuyên dùng; chạy được cả lịch tự động khi máy tắt).
- **Cách 2 — Chrome đã đăng nhập Google** (dùng khi công ty chưa bật kết nối; cần máy bật và Chrome mở).

**Kiểm tra:** có công cụ Google Drive `search_files` và Google Sheets `get_values` → cách 1 sẵn sàng, sang Bước 4.

**Chưa có kết nối**, hướng dẫn từng thao tác:
1. Desktop/Cowork: "Bấm **Settings** (Cài đặt) → **Connectors** (Kết nối). Bạn có thấy **Google Drive** và **Google Sheets** trong danh sách không?"
   Claude Code: "Bạn mở **claude.ai** trên trình duyệt (cùng tài khoản) → **Settings → Connectors**. Bạn có thấy **Google Drive** và **Google Sheets** không?"
2. **Có thấy** → "Bấm **Connect** ở Google Drive, đăng nhập **tài khoản Google công ty**; làm tương tự với Google Sheets." Rồi: "Bạn mở lại cuộc trò chuyện (Claude Code: thoát và mở lại Claude) và nhắn 'xong'." Đã kết nối mà vẫn chưa thấy công cụ: "Bấm biểu tượng kết nối ở ô chat và bật Google Drive / Google Sheets."
3. **Không thấy** → công ty dùng Claude Team và **Owner chưa bật**. Nói: "Phần này cần người quản trị Claude của công ty bật một lần. Bạn gửi giúp tin nhắn này cho người quản trị:"
   ```
   Nhờ anh/chị bật giúp cho Claude Team (claude.ai → Organization settings):
   1. Capabilities → bật Web search
   2. Capabilities → bật Cloud code execution and file creation
   3. Plugins & skills → tab Policy → bật Skills
   4. Plugins & skills → bật cho phép thành viên thêm plugin
   5. Connectors → Browse connectors → Google Drive → Add to your team
   6. Connectors → Browse connectors → Google Sheets → Add to your team, quyền ghi/sửa đặt Always allow
   7. Claude in Chrome → bật Enable for your team
   8. Cowork → bật Enable for your organization
   9. Cowork → bật Run Cowork in the cloud
   Nếu kết nối Google báo "ứng dụng bị chặn": admin.google.com → Security → Access and data control → API controls → Manage third-party app access → đặt Claude là Trusted.
   Hướng dẫn chi tiết: docs/owner-setup-guide.md. Cảm ơn!
   ```
   Người quản trị cần hướng dẫn chi tiết → gửi họ file `docs/owner-setup-guide.md`.
   Trong lúc chờ: dùng **cách 2** (mục dưới) để team vẫn làm việc được.
4. Kết nối báo lỗi quyền (Owner chỉ cho đọc): "Người quản trị đang chỉ cho phép đọc. Nhờ họ cho phép sửa với Google Sheets." Trong lúc chờ: cách 2.

**Cách 2 — Chrome:**
1. Cần công cụ Claude in Chrome (cài theo Bước 4 mục 2 nếu chưa có).
2. "Trên Chrome, bạn kiểm tra đã đăng nhập **tài khoản Google công ty** chưa (mở drive.google.com thấy Drive của bạn là được)."
3. Tự kiểm tra: mở `https://drive.google.com` trong tab mới, không bị hỏi đăng nhập → được. Đóng tab.
4. Nói: "Mình sẽ đọc/ghi bảng qua Chrome của bạn. Khi mình chạy, bạn để Chrome mở và đừng đóng tab mình đang dùng."

**Nếu lỗi quyền với bảng:** "Tài khoản của bạn chưa có quyền sửa bảng. Nhờ người tạo bảng chia sẻ quyền **Người chỉnh sửa** cho bạn."

---

## Bước 4 — (Khuyên dùng) Chrome cho Facebook, TikTok, quảng cáo

Hỏi: "Team research cả Fanpage, TikTok và quảng cáo của đối thủ mỗi ngày đúng không? Phần này cần Google Chrome và tiện ích Claude."
1. Đã có công cụ Claude in Chrome → sang 3.
2. "Bạn mở Chrome, vào cửa hàng tiện ích Chrome, tìm **Claude** (của Anthropic), bấm **Thêm vào Chrome**. Rồi bấm biểu tượng Claude trên thanh Chrome và đăng nhập cùng tài khoản Claude." Chờ "xong".
3. "Trên Chrome, bạn kiểm tra đã đăng nhập **Facebook** và **TikTok** bằng tài khoản của chính bạn. Dùng tài khoản thật, không dùng tài khoản ảo."

Không cài được → ghi nhận, tiếp tục; research chạy phần website/tìm kiếm.

---

## Bước 5 — Tạo hoặc kết nối bảng dữ liệu (skill mkt-setup)

Chạy skill `mkt-setup` (hoặc đọc `skills/mkt-setup/SKILL.md` và làm theo). Skill này tìm bảng team đã có hoặc tạo bảng mới theo mẫu (7 tab), cho phép thêm sản phẩm/đối thủ, và chạy thử research.

**Xong khi:** có Google Sheet **Redsun MKT — Research database** đủ 7 tab và ít nhất 1 dòng trong `Insight hằng ngày`.

---

## Bước 6 — Lịch chạy tự động

Bỏ qua nếu team đã có các tác vụ này (hỏi: "Team đã tạo lịch tự động chưa?"). Chỉ **một người** trong team tạo lịch, tránh chạy trùng.

| Tác vụ | Giờ | Lời nhắn (người dùng dán nguyên văn) |
|---|---|---|
| Research thường | 09:00, thứ Hai–thứ Sáu | `Chạy skill mkt-research của plugin redsun-mkt, chế độ thường. Đây là lần chạy theo lịch.` |
| Research Chrome | 09:30, thứ Hai–thứ Sáu | `Chạy skill mkt-research của plugin redsun-mkt, chế độ chrome. Đây là lần chạy theo lịch.` |
| Lịch tuần | 16:00 thứ Sáu | `Chạy skill mkt-content-calendar của plugin redsun-mkt cho tuần sau. Đây là lần chạy theo lịch.` |

**Claude Desktop (Cowork)** — từng thao tác:
1. "Trong Cowork, bấm mục **Scheduled** (Tác vụ định kỳ) ở thanh bên trái." (Không thấy → nhờ chụp màn hình.)
2. "Bấm **New task**."
3. "Dán lời nhắn này vào ô nội dung: `<lời nhắn>`."
4. "Chọn lặp lại: <thứ Hai–thứ Sáu lúc 09:00 | … >, rồi lưu." Lặp cho 3 tác vụ.

Nói với người dùng:
- "Research thường chạy được cả khi máy tắt" — **chỉ khi dùng cách 1 (kết nối)**. Dùng cách 2 (Chrome) thì mọi tác vụ cần máy bật và Chrome mở.
- "Research Chrome cần máy bật, Chrome mở và đã đăng nhập. Sáng nào máy tắt, bạn chỉ cần nhắn 'research bằng Chrome'."
- "Lịch tuần: lúc nào cần, bạn cứ nhắn 'lập lịch tuần sau' là có ngay."
- "Nếu công ty tắt tính năng lịch tự động, mỗi sáng bạn nhắn 'research hôm nay' là được."

**Claude Code:** "Trên Claude Code, mỗi sáng bạn nhắn 'research hôm nay'. Nếu có Claude Desktop, mình khuyên tạo lịch tự động bên đó." Không cấu hình gì thêm.

---

## Bước 7 — Bàn giao

1. Tự kiểm tra: bảng có đủ 7 tab; tab Chiến lược content có trụ cột `đã duyệt`.
2. Gửi:
```
✅ Đã cài xong!
• Bảng dữ liệu: <link Research database>
• Chiến lược content: <n> trụ cột đã duyệt (<sản phẩm>), <m> nháp chờ duyệt
• Tự động: <đã tạo lịch / chạy tay>

Hằng ngày bạn chỉ cần nói:
• "Research hôm nay"  • "Research bằng Chrome"
• "Lập lịch tuần sau" • "Kho insight tuần này có gì về SIPOS?"
```
