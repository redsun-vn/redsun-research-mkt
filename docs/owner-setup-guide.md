# Hướng dẫn cho người quản trị Claude Team (Owner)

Gửi người quản trị Claude Team của công ty. Làm **một lần**, khoảng 10 phút. Mục đích: team Marketing dùng công cụ research của Redsun (Claude đọc và ghi bảng **Redsun MKT — Research database** trên Google Sheets).

Bật một kết nối chỉ cho phép thành viên sử dụng. Mỗi người vẫn phải tự đăng nhập tài khoản Google của mình, và Claude chỉ thấy những file mà chính người đó có quyền.

---

## Phần A — Trên Claude (claude.ai, tài khoản Owner)

**A1. Thêm kết nối Google Drive**
1. Mở **claude.ai**, đăng nhập bằng tài khoản Owner.
2. Vào **Organization settings** → **Connectors**.
3. Bấm **Browse connectors** (cuối trang) → chọn **Google Drive** → **Add to your team**.

**A2. Thêm kết nối Google Sheets (cho phép sửa)**
1. Vẫn ở **Organization settings** → **Connectors** → **Browse connectors**.
2. Chọn **Google Sheets** → **Add to your team**.
3. Mở phần quyền của Google Sheets: để các quyền **ghi/sửa** ở mức **Always allow** hoặc **Needs approval**, **không** để **Blocked**. Nếu chặn quyền ghi, Claude chỉ đọc được bảng chứ không ghi được.

**A3. Bật tìm kiếm web (Web search)**
- Trong phần cài đặt tổ chức, bật **Web search** để Claude đọc được blog, bảng giá và kết quả tìm kiếm.

**A4. Không chặn các tính năng sau**
- **Claude in Chrome**: để đọc Fanpage, TikTok, quảng cáo Meta của đối thủ.
- **Cowork** và **Scheduled tasks** (tác vụ định kỳ): để research tự chạy mỗi sáng.

Không cần bật: Gmail, Google Calendar, Google Docs, Google Slides.

---

## Phần B — Trên Google Workspace (chỉ khi công ty chặn ứng dụng ngoài)

Làm phần này nếu thành viên báo lỗi khi bấm kết nối Google (ví dụ "ứng dụng bị chặn" hoặc "admin chưa cho phép"). Cần **quản trị viên Google Workspace**:
1. Mở **admin.google.com**.
2. **Security** → **Access and data control** → **API controls** → **Manage third-party app access**.
3. Tìm ứng dụng **Claude**, đặt **Trusted** (tin cậy).
4. Chờ khoảng 15 phút để thay đổi có hiệu lực.

---

## Phần C — Kiểm tra sau khi bật

1. Một thành viên MKT mở Claude → **Settings** (hoặc **Customize**) → **Connectors**: thấy **Google Drive** và **Google Sheets** → bấm **Connect**, đăng nhập tài khoản Google công ty.
2. Thành viên đó mở Claude trong thư mục `redsun-research-mkt` và nói: **"Đọc file SETUP.md và cài đặt giúp tôi."** Claude sẽ tự kiểm tra và báo ✅ khi đọc/ghi được bảng.

Giao diện có thể thay đổi theo thời gian. Không thấy đúng tên nút như trên thì xem hướng dẫn chính thức: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors

---

## Tin nhắn ngắn (copy gửi qua chat)

```
Chào anh/chị, team Marketing cần bật giúp mấy mục cho Claude Team của công ty (làm 1 lần, khoảng 10 phút):

Trên claude.ai (tài khoản Owner) → Organization settings:
1. Connectors → Browse connectors → Google Drive → Add to your team
2. Connectors → Browse connectors → Google Sheets → Add to your team, và KHÔNG chặn quyền ghi (Blocked)
3. Bật Web search
4. Không chặn Claude in Chrome, Cowork và Scheduled tasks

Chỉ khi thành viên báo lỗi "ứng dụng bị chặn" lúc kết nối Google: admin.google.com → Security → Access and data control → API controls → Manage third-party app access → đặt Claude là Trusted.

Không cần bật Gmail, Calendar, Docs, Slides. Bật xong mỗi người tự kết nối tài khoản Google của mình và chỉ thấy file mình có quyền.
Hướng dẫn chi tiết: docs/owner-setup-guide.md trong repo redsun-vn/redsun-research-mkt. Cảm ơn anh/chị!
```
