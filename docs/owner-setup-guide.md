# Hướng dẫn cho người quản trị Claude Team (Owner)

Gửi người quản trị Claude Team của công ty. Làm **một lần**, khoảng 10–15 phút, bằng tài khoản **Owner** hoặc **Primary Owner** trên **claude.ai**.

Mục đích: team Marketing dùng công cụ research của Redsun. Claude đọc web và Fanpage đối thủ, rồi đọc/ghi bảng **Redsun MKT — Research database** trên Google Sheets.

Bật kết nối Google chỉ cho phép dùng. Mỗi người vẫn tự đăng nhập tài khoản Google của mình, và Claude chỉ thấy file mà chính người đó có quyền.

---

## Danh sách cần bật (9 mục)

Tất cả nằm trong **claude.ai → Organization settings**.

| # | Vào mục | Bật gì | Chọn / đặt | Để làm gì |
|---|---|---|---|---|
| 1 | **Capabilities** | **Web search** | Bật (On) | Đọc blog, bảng giá, kết quả tìm kiếm của đối thủ |
| 2 | **Capabilities** | **Cloud code execution and file creation** | Bật (On) | Chạy kỹ năng (skill) và máy kiểm tra dữ liệu |
| 3 | **Plugins & skills** → tab **Policy** | **Skills** | Bật (On) | Dùng 3 kỹ năng research, lập lịch, cài đặt |
| 4 | **Plugins & skills** | Cho phép thành viên **thêm plugin** | Bật (cho phép) | Cài plugin `redsun-mkt` từ GitHub hoặc file ZIP |
| 5 | **Connectors** → **Browse connectors** → **Google Drive** | **Add to your team** | Bấm thêm | Tìm, tạo bảng dữ liệu, xuất bảng ra file để kiểm tra |
| 6 | **Connectors** → **Browse connectors** → **Google Sheets** | **Add to your team** | Bấm thêm, rồi đặt các quyền **ghi/sửa** là **Always allow** (hoặc **Needs approval**) | Đọc và ghi từng tab của bảng |
| 7 | **Claude in Chrome** | **Enable for your team** | Bật (On). Phần trang web: chọn **mọi trang trừ trang bị chặn**; nếu công ty chọn **chỉ trang được phép** thì bấm **Add websites** và thêm: `facebook.com`, `tiktok.com`, `docs.google.com`, `drive.google.com`, `trends.google.com` | Đọc Fanpage, TikTok, quảng cáo Meta; ghi bảng qua Chrome khi cần |
| 8 | **Cowork** | **Enable for your organization** | Bật (On) | Dùng Claude Desktop (Cowork) và tác vụ định kỳ |
| 9 | **Cowork** | **Run Cowork in the cloud** | Bật (On) | Research tự chạy mỗi sáng **kể cả khi máy tắt** |

Gói **Enterprise** có thêm công tắc **Scheduled tasks**: bật (On). Gói **Team** không có công tắc riêng này.

Không cần bật: Gmail, Google Calendar, Google Docs, Google Slides.

---

## Nếu Google Workspace công ty chặn ứng dụng ngoài

Chỉ làm khi thành viên báo lỗi lúc kết nối Google (ví dụ "ứng dụng bị chặn", "admin chưa cho phép"). Cần **quản trị viên Google Workspace**:

| # | Vào đâu | Làm gì |
|---|---|---|
| 10 | **admin.google.com** → **Security** → **Access and data control** → **API controls** → **Manage third-party app access** | Tìm ứng dụng **Claude** → đặt **Trusted** (tin cậy). Chờ khoảng 15 phút |
| 11 | (Chỉ khi công ty quản lý Chrome tập trung) **admin.google.com** → **Devices** → **Chrome** → **Apps & extensions** | Cho phép (hoặc cài sẵn) tiện ích **Claude** trên Chrome Web Store |

---

## Kiểm tra sau khi bật

1. Một thành viên MKT mở Claude → **Settings** (hoặc **Customize**) → **Connectors**: thấy **Google Drive** và **Google Sheets** → bấm **Connect**, đăng nhập tài khoản Google công ty.
2. Thành viên đó mở Claude trong thư mục `redsun-research-mkt` và nói: **"Đọc file SETUP.md và cài đặt giúp tôi."** Claude tự kiểm tra và báo ✅ cho từng mục.

Tên nút có thể khác một chút theo phiên bản. Không thấy đúng tên thì xem hướng dẫn chính thức:
- Kết nối Google: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
- Web search: https://support.claude.com/en/articles/10684626-enable-and-use-web-search
- Code execution: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- Skills: https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization
- Claude in Chrome: https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls
- Cowork: https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans

---

## Tin nhắn ngắn (copy gửi qua chat)

```
Chào anh/chị, team Marketing nhờ bật giúp các mục sau cho Claude Team của công ty (làm 1 lần, khoảng 10–15 phút, tài khoản Owner trên claude.ai → Organization settings):

1. Capabilities → bật Web search
2. Capabilities → bật Cloud code execution and file creation
3. Plugins & skills → tab Policy → bật Skills
4. Plugins & skills → bật cho phép thành viên thêm plugin
5. Connectors → Browse connectors → Google Drive → Add to your team
6. Connectors → Browse connectors → Google Sheets → Add to your team, đặt quyền ghi/sửa là Always allow
7. Claude in Chrome → bật Enable for your team (nếu chỉ cho phép một số trang: thêm facebook.com, tiktok.com, docs.google.com, drive.google.com, trends.google.com)
8. Cowork → bật Enable for your organization
9. Cowork → bật Run Cowork in the cloud

Nếu thành viên báo lỗi "ứng dụng bị chặn" khi kết nối Google: admin.google.com → Security → Access and data control → API controls → Manage third-party app access → đặt Claude là Trusted.

Không cần bật Gmail, Calendar, Docs, Slides. Bật xong mỗi người tự kết nối tài khoản Google của mình và chỉ thấy file mình có quyền.
Hướng dẫn chi tiết: docs/owner-setup-guide.md trong repo redsun-vn/redsun-research-mkt. Cảm ơn anh/chị!
```
