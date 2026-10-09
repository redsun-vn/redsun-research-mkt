# UPDATE — cập nhật bản mới (dành cho Claude thực hiện)

> Người dùng là team Marketing, **không biết kỹ thuật**. Họ chỉ nói "Đọc file UPDATE.md và cập nhật giúp tôi" (hoặc "cập nhật công cụ research"). Tuân theo `shared/working-rules.md`: tiếng Việt thường, mỗi lần một thao tác, chờ "xong".

Mở đầu: "Mình cập nhật công cụ research lên bản mới nhé, khoảng 5 phút. Dữ liệu trong Google Sheet của team giữ nguyên."

---

## Bước 1 — Xem đang dùng bản nào, bản mới có gì

1. Đọc `version` trong `.claude-plugin/plugin.json` của bản đang cài (Claude Code: thư mục plugin đã cài, ví dụ trong `~/.claude/plugins/cache/redsun-mkt/`; Cowork: thư mục repo đang mở).
2. Đọc `CHANGELOG.md` của **bản mới** (sau khi tải ở Bước 2 thì đọc lại). Tóm tắt cho người dùng 2–3 dòng: có gì mới, và mục **"Team cần làm"** của từng bản mới hơn bản đang dùng.

---

## Bước 2 — Lấy bản mới

### Claude Code — tự làm, không nhờ người dùng
1. Thư mục repo có `.git` → chạy `git pull` trong thư mục đó.
   Không có `.git` (tải bằng ZIP) → nói: "Bạn tải lại file ZIP mới từ trang GitHub (nút xanh **Code** → **Download ZIP**), giải nén và **thay** thư mục `redsun-research-mkt` cũ. Xong nhắn 'xong'." Chưa có tài khoản GitHub → nhờ người phụ trách kỹ thuật gửi ZIP.
2. Chạy `claude plugin marketplace update redsun-mkt` rồi `claude plugin update redsun-mkt@redsun-mkt`.
   Báo lỗi "không tìm thấy marketplace" → cài lại như `SETUP.md` Bước 2.
3. Nói: "Bản mới sẽ có hiệu lực khi bạn mở lại Claude. Bạn thoát rồi mở lại giúp mình nhé." (Trong lúc chờ, có thể đọc trực tiếp `skills/<tên>/SKILL.md` mới trong thư mục repo.)

### Claude Desktop / Cowork — hướng dẫn từng thao tác
**Cài từ GitHub (marketplace):**
1. "Bạn bấm **Customize** (Tuỳ chỉnh) ở thanh bên trái → **Plugins**."
2. "Tìm **redsun-mkt**. Nếu thấy nút **Update** (Cập nhật) thì bấm." Không thấy nút: "Bấm vào marketplace **redsun-mkt** rồi chọn làm mới (Refresh/Sync), sau đó quay lại plugin và bấm **Update**." Giao diện khác mô tả → nhờ chụp màn hình, hướng dẫn theo ảnh.
3. "Bạn mở một cuộc trò chuyện mới để dùng bản mới."

**Cài bằng file ZIP:**
1. Nhận file `redsun-mkt.zip` mới (người phụ trách kỹ thuật gửi, hoặc nếu chạy được lệnh: tải bản mới như phần Claude Code rồi tự chạy `bash scripts/build-desktop-zip.sh`).
2. "Customize → Plugins → **redsun-mkt** → gỡ (Remove/Uninstall)." → "Bấm **tải lên plugin** (Upload), chọn file `redsun-mkt.zip` mới."
3. "Bạn mở một cuộc trò chuyện mới để dùng bản mới."

**Thư mục repo đang mở trong Cowork** (để đọc SETUP/UPDATE): tải ZIP mới và thay thư mục cũ như phần Claude Code bước 1.

**Xong khi:** `version` trong bản đang dùng bằng `version` mới nhất trong `CHANGELOG.md`.

---

## Bước 3 — Làm phần "Team cần làm" trong CHANGELOG

Chỉ làm khi bản mới có ghi. Thường gặp:
- **Bảng cần thêm tab/cột:** chạy skill `mkt-setup` Bước 2 (chỉ bổ sung phần thiếu, không đụng dữ liệu cũ). Chỉ **một người** trong team làm việc này; người khác bỏ qua nếu bảng đã có.
- **Lời nhắn của lịch tự động thay đổi:** người đã tạo lịch mở Cowork → **Scheduled**, sửa nội dung từng tác vụ theo lời nhắn mới trong `SETUP.md` Bước 6.
- **Cần bật thêm kết nối:** theo `SETUP.md` Bước 3 hoặc 4.

Không có mục "Team cần làm" → bỏ qua bước này.

---

## Bước 4 — Kiểm tra nhanh và báo

1. Hỏi Claude một câu không ghi dữ liệu để thử: đọc tab Digest, báo lượt research gần nhất.
2. Báo:
```
✅ Đã cập nhật lên bản <version>.
Có gì mới: <1–3 dòng từ CHANGELOG>
Team cần làm thêm: <đã làm / không có>
Bạn dùng như bình thường: "Research hôm nay" · "Lập lịch tuần sau" · "Hôm nay làm nội dung gì?"
```
