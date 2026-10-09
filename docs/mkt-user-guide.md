# Hướng dẫn sử dụng cho team Marketing

Hướng dẫn từng bước, không cần biết kỹ thuật. Bạn chỉ **nói chuyện với Claude bằng tiếng Việt**; Claude làm phần còn lại.

Mọi kết quả nằm trong một Google Sheet chung của team: **Redsun MKT — Research database**.

---

## Phần 0 — Chuẩn bị (kiểm tra 1 lần)

- Bạn có **tài khoản Claude của công ty** (gói Team) và đăng nhập được Claude Desktop.
- Bạn có **tài khoản Google công ty**.
- Máy có **Google Chrome**, đã đăng nhập **Facebook** và **TikTok** bằng **tài khoản thật của bạn** (không dùng tài khoản ảo).
- Người quản trị Claude đã bật các mục cần thiết (xem `docs/owner-setup-guide.md`). Chưa chắc thì cứ cài, Claude sẽ báo nếu thiếu.

---

## Phần 1 — Cài đặt (làm 1 lần, khoảng 15 phút)

- **Bước 1. Tải thư mục công cụ về máy**
  - Mở https://github.com/redsun-vn/redsun-research-mkt (đăng nhập GitHub đã được mời vào nhóm `redsun-vn`).
  - Bấm nút xanh **Code** → **Download ZIP**.
  - Bấm đúp file ZIP vừa tải để giải nén. Bạn có thư mục `redsun-research-mkt`.
  - Không có tài khoản GitHub: nhờ người phụ trách kỹ thuật gửi file ZIP.
- **Bước 2. Mở Claude Desktop trong thư mục đó**
  - Mở **Claude Desktop** → chọn **Cowork**.
  - Chọn thư mục `redsun-research-mkt` vừa giải nén.
- **Bước 3. Nhờ Claude cài đặt**
  - Dán câu này vào ô chat và gửi:
    > Đọc file SETUP.md trong thư mục này và cài đặt giúp tôi.
- **Bước 4. Làm theo từng bước Claude nhờ**
  - Claude sẽ nhờ bạn bấm vài chỗ (cài công cụ, kết nối Google Drive và Google Sheets, cài tiện ích Claude trên Chrome).
  - Mỗi lần chỉ một việc. Làm xong thì nhắn **"xong"**.
  - Không thấy nút như Claude tả: chụp màn hình gửi Claude.
- **Bước 5. Trả lời vài câu hỏi**
  - Claude hỏi về bảng dữ liệu (dùng bảng team đã có hay tạo mới), đối thủ, từ khoá. Trả lời tự nhiên là được.
- **Bước 6. Tạo lịch tự động (chỉ 1 người trong team làm)**
  - Claude hướng dẫn tạo 3 tác vụ: research thường (09:00), research Chrome (09:30), lịch tuần (16:00 thứ Sáu).
  - Người khác trong team **không** tạo lại, để tránh chạy trùng.
- **Xong khi** Claude báo ✅ và gửi link bảng **Redsun MKT — Research database**.

---

## Phần 2 — Mỗi sáng (2–5 phút)

- **Bước 1. Mở bảng dữ liệu xem có gì mới**
  - Nếu đã có lịch tự động: research đã tự chạy lúc 09:00 và 09:30.
  - Mở tab **Digest** để đọc tóm tắt hôm nay (chủ đề, offer, CTA, pain point, đối thủ mới…).
- **Bước 2. Chưa có lịch tự động, hoặc sáng nay máy tắt**
  - Mở Claude (Cowork, thư mục `redsun-research-mkt`) và nói:
    > Research hôm nay
  - Muốn đọc thêm Fanpage, TikTok, quảng cáo của đối thủ (cần Chrome đang mở):
    > Research bằng Chrome
  - Muốn chạy cả hai một lần:
    > Research đầy đủ
- **Bước 3. Xem Claude báo gì**
  - Số insight mới, quan sát mới, Content Idea mới, nguồn nào bị chặn.
  - Bấm link để mở bảng.
- **Lưu ý khi Claude dùng Chrome**
  - Để Chrome mở, đừng đóng tab Claude đang dùng.
  - Facebook/TikTok hiện yêu cầu xác minh: Claude tự dừng. Bạn mở Facebook/TikTok tự xác minh, rồi nhắn lại Claude.

---

## Phần 3 — Lấy ý tưởng làm nội dung hôm nay

- **Bước 1. Hỏi Claude**
  > Hôm nay làm nội dung gì?
  - Hoặc cho một bài cụ thể trong lịch:
  > Viết idea cho bài CAL-2026-W42-01
- **Bước 2. Claude trả về từng idea thành một khối chữ**
  - Mỗi khối bắt đầu và kết thúc bằng dòng `=====`.
  - Video: có kịch bản theo cảnh và giây. Bài đăng/carousel: có nội dung từng ảnh.
  - Cuối khối có dòng **"Dựa trên"**: quan sát (mã OB) và trụ cột chiến lược mà idea dựa vào.
- **Bước 3. Copy và dùng**
  - Copy **nguyên khối** (từ dòng `=====` đầu đến dòng `=====` cuối).
  - Dán cho agent tạo video / agent viết bài, hoặc gửi cho người làm. Không cần viết thêm gì.
- **Bước 4. Trước khi đăng**
  - Xem mục **"Cần team xác nhận"** trong khối: kiểm tra các số liệu/chính sách đó trước.
  - Xem mục **"Không được"**: không nêu tên đối thủ, không tự thêm số liệu.

---

## Phần 4 — Lịch nội dung tuần

- **Bước 1. Hỏi Claude bất cứ lúc nào**
  > Lập lịch tuần sau
  - Hoặc: "Lập lịch tuần này", "Lịch tuần sau cho SIPOS".
- **Bước 2. Mở tab Content Calendar trong bảng**
  - Mỗi dòng: ngày đăng, kênh, sản phẩm, mã trụ cột, mã quan sát, góc/tiêu đề, định dạng, CTA.
  - Mọi dòng ở trạng thái **đề xuất, chờ duyệt**.
- **Bước 3. Xem phần giải thích**
  - Tab **Digest**, mục **Lịch tuần …**: trụ cột nào còn thiếu dữ liệu, kênh nào chưa có.
  - Mục **Lịch tuần … — đã loại**: ý tưởng bị loại vì không truy được nguồn.
- **Bước 4. Chốt lịch**
  - Điền **Người phụ trách**, đổi trạng thái khi đã duyệt.
  - Muốn có brief chi tiết cho từng bài: làm Phần 3.

---

## Phần 5 — Duyệt (dành cho trưởng nhóm MKT)

- **Chiến lược content** (tab Chiến lược content, cột Trạng thái)
  - Chỉ trụ cột **đã duyệt** mới được dùng để lập lịch.
  - Trụ cột mới Claude soạn luôn là **nháp**: đọc, sửa nếu cần, rồi đổi thành **đã duyệt**.
  - Hỏi Claude "Strategy đã ổn chưa?" để xem tóm tắt các trụ cột và dòng nào còn nháp.
- **Content Idea** (tab Research database, cột Trạng thái)
  - Claude ghi **gợi ý, chờ người duyệt**. Bạn đổi thành **đã duyệt** hoặc **bỏ** (ý tưởng **bỏ** sẽ không vào lịch).
- **Lịch tuần** (tab Content Calendar): duyệt như Phần 4 bước 4.

---

## Phần 6 — Hỏi nhanh kho dữ liệu

- "Kho insight tuần này có gì về SIPOS?"
- "Đối thủ nào đang chạy ưu đãi mạnh nhất cho WEBINO?"
- "Hôm qua research có chạy không?"
- Claude trả lời kèm mã quan sát (OB…) hoặc link nguồn để bạn mở kiểm tra. Claude không ghi gì vào bảng khi bạn chỉ hỏi.

---

## Phần 7 — Thêm đối thủ, từ khoá, sản phẩm

- **Thêm đối thủ**: "Thêm đối thủ Nhanh.vn cho WEBINO". Claude hỏi link Fanpage/TikTok/website (chưa có link thì Claude tự tìm và hỏi bạn xác nhận).
- **Thêm từ khoá**: "Thêm từ khoá 'phần mềm quản lý spa' cho SIPOS".
- **Thêm sản phẩm** (ví dụ hosting, email doanh nghiệp): "Thêm sản phẩm hosting". Claude hỏi đối thủ, từ khoá, và vài câu để soạn **chiến lược nháp**; trưởng nhóm duyệt xong mới lập lịch được.
- Đối thủ Claude tự phát hiện (Digest, mục "Đối thủ mới nên xem xét…") chỉ được thêm khi bạn đồng ý.

---

## Phần 8 — Khi có bản mới

- Người phụ trách kỹ thuật báo trong nhóm chat.
- Mở Claude (Cowork, thư mục `redsun-research-mkt`) và nói:
  > Đọc file UPDATE.md và cập nhật giúp tôi.
- Làm theo từng bước Claude nhờ, rồi mở cuộc trò chuyện mới.
- Dữ liệu trong bảng không bị ảnh hưởng. Muốn biết có gì mới: "Bản mới có gì?"

---

## Phần 9 — Quy tắc khi sửa bảng bằng tay

- **Không chèn dòng, không xoá dòng, không sắp xếp/lọc lại** các tab Claude đang ghi (Claude tìm dòng theo mã).
- Được sửa: cột **Trạng thái** (duyệt), **Người phụ trách**, tab **Nguồn theo dõi** (thêm dòng ở cuối), tab **Chiến lược content** (sửa nội dung trụ cột, đổi trạng thái).
- Không đổi tên bảng và tên các tab.

---

## Phần 10 — Gặp sự cố

- **Claude nói chưa vào được bảng dữ liệu**
  - Nhắn: "Đọc file SETUP.md và kiểm tra kết nối giúp tôi." Claude hướng dẫn kết nối lại.
  - Công ty chưa bật kết nối Google: Claude dùng Chrome của bạn (để Chrome mở, đã đăng nhập Google), và đưa bạn tin nhắn mẫu gửi người quản trị.
- **Claude nói không có quyền sửa bảng**: nhờ người tạo bảng chia sẻ quyền **Người chỉnh sửa**.
- **Facebook/TikTok yêu cầu xác minh**: tự mở và xác minh tài khoản, rồi nhắn "research bằng Chrome".
- **Sáng nay không thấy research tự chạy**: nhắn "Hôm qua research có chạy không?" rồi "Research hôm nay".
- **Lịch tuần không có bài cho WEBINO**: WEBINO chưa có Fanpage/TikTok trong tab Nguồn theo dõi. Có link kênh thì báo Claude: "Thêm Fanpage WEBINO: <link>".
- **Lỗi lạ lặp lại**: báo người phụ trách kỹ thuật, kèm ảnh chụp màn hình.

---

## Bảng câu nói nhanh

| Bạn muốn | Nói với Claude |
|---|---|
| Cài lần đầu | Đọc file SETUP.md trong thư mục này và cài đặt giúp tôi. |
| Research hôm nay | Research hôm nay |
| Research Fanpage, TikTok, quảng cáo | Research bằng Chrome |
| Research cả hai | Research đầy đủ |
| Ý tưởng làm hôm nay | Hôm nay làm nội dung gì? |
| Brief cho một bài | Viết idea cho bài CAL-… |
| Lịch tuần | Lập lịch tuần sau |
| Hỏi kho dữ liệu | Kho insight tuần này có gì về SIPOS? |
| Xem chiến lược | Strategy đã ổn chưa? |
| Thêm đối thủ / sản phẩm | Thêm đối thủ … cho … / Thêm sản phẩm … |
| Cập nhật bản mới | Đọc file UPDATE.md và cập nhật giúp tôi. |
