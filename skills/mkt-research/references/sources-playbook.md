# Playbook nguồn dữ liệu

Danh sách nguồn cụ thể (link Fanpage, TikTok, YouTube, blog/bảng giá, từ khoá Ad Library) nằm ở tab **Nguồn theo dõi**. File này hướng dẫn **cách đọc** từng loại.

Kiểm chứng thật ngày 2026-10-09 (từ Claude Code):

| Nguồn | Chế độ | Công cụ | Kết quả kiểm chứng |
|---|---|---|---|
| Website, blog, bảng giá | thường | WebFetch | Đọc được (URL sai trả 404 → thử trang chủ) |
| Google Trends VN | thường | WebFetch `https://trends.google.com/trending?geo=VN` | Đọc được từ khoá + lượng tìm |
| Tìm kiếm web | thường | WebSearch | — |
| YouTube kênh đối thủ | thường | WebFetch | Chưa kiểm chứng; trống thì ghi `trống` |
| Meta Ad Library | chrome | Claude in Chrome | WebFetch bị ngắt kết nối; Chrome đọc được quảng cáo thật, không cần đăng nhập |
| Fanpage, Facebook Groups | chrome | Claude in Chrome + tài khoản thật | Facebook chặn đọc tự động khi chưa đăng nhập |
| TikTok | chrome | Claude in Chrome + tài khoản thật | WebFetch chỉ trả tiêu đề trang |

Giới hạn đã biết (từ bảng mẫu của team): Facebook chỉ đọc được các bài mới nhất của Fanpage; TikTok chỉ có lượt xem từng video.

## Cách đọc

**Website / blog / bảng giá** — trang ở cột `Blog / giá / website`. Lấy: bài blog mới (tiêu đề, ngày), gói và giá, ưu đãi, nút CTA. `kenh = Website blog`. Đếm tỷ lệ chủ đề khi có thể ("3/5 bài blog gần nhất về vay vốn").

**Meta Ad Library** — mở
`https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=VN&q=<Từ khóa Ad Library>&search_type=keyword_unordered`
(ô Ghi chú ghi "cụm từ chính xác" → dùng `search_type=keyword_exact_phrase`). Chờ khoảng 5 giây rồi đọc chữ trên trang. Chỉ giữ quảng cáo của đúng đối thủ. Lấy: số quảng cáo đang chạy, ngày bắt đầu, ngành/đối tượng nhắm, ưu đãi, CTA, "nhiều phiên bản". URL ghi `https://www.facebook.com/ads/library/?country=VN&q=<từ khoá>`. `kenh = Quảng cáo Meta`.

**Fanpage** — mở link cột `Fanpage`. Đọc các bài mới nhất (không cuộn quá giới hạn). Lấy: ngày đăng, câu mở đầu, định dạng, ưu đãi, CTA, lượt thích/chia sẻ/bình luận **hiển thị công khai** → cột `Tín hiệu`. `kenh = Facebook`.

**Facebook Groups / tìm bài** — chỉ khi có nhóm/từ khoá trong Nguồn theo dõi. Ghi *chủ đề* người dùng bàn, không ghi tên hay thông tin người đăng/bình luận. `kenh = Facebook Groups`.

**TikTok** — mở link cột `TikTok`. Lấy: caption, hashtag, lượt xem từng video, kiểu video. `kenh = TikTok`.

**Từ khoá** — dòng `từ khóa` của sản phẩm: WebSearch từng từ khoá (thêm năm hiện tại), đọc 1–3 kết quả để tìm chủ đề nóng và nỗi đau khách hàng nói ra; Google Trends xem từ khoá nào đang lên. `kenh = Tìm kiếm web` / `Google Trends`.

**Nguồn của mình** (dòng `của mình`) — lấy số liệu `mốc` (người theo dõi, lượt thích…) để so sánh về sau, `nhan = mốc`.

## Giới hạn bắt buộc khi dùng Chrome

- Tài khoản thật mà người dùng đã tự đăng nhập. Không đăng nhập hộ, không tạo tài khoản, không giả danh.
- Chỉ đọc. Không thích, bình luận, theo dõi, nhắn tin, bấm quảng cáo, đồng ý popup quyền.
- Theo `Giới hạn mỗi lần chạy` trong Nguồn theo dõi (mặc định tối đa 30 trang mở, 20 phút). Mở từng trang một, đóng tab khi xong.
- Gặp captcha, yêu cầu đăng nhập, checkpoint → **dừng ngay** nguồn đó, ghi `Nguồn lỗi/bị chặn`, báo người dùng. Không tìm cách vượt.
- Chỉ mở URL có trong Nguồn theo dõi hoặc URL tìm kiếm ở trên. Không mở hộp thư, thông báo, bảng tin cá nhân.
- Không lưu dữ liệu cá nhân của người dùng mạng xã hội.
