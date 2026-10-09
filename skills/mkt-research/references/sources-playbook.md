# Playbook nguồn dữ liệu

Kết quả kiểm chứng thật ngày 2026-10-09 quyết định nguồn nào đọc tự động, nguồn nào cần Chrome.

| Nguồn | Chế độ | Công cụ | Đã kiểm chứng |
|---|---|---|---|
| Website/blog đối thủ | public-auto | WebFetch | Đọc được menu sản phẩm, trang khuyến mãi; URL sai trả 404 |
| Google Trends VN | public-auto | WebFetch | `trends.google.com/trending?geo=VN` trả từ khoá + lượng tìm |
| Tìm kiếm theo keyword | public-auto | WebSearch | — |
| Meta Ad Library | chrome | Claude in Chrome | WebFetch bị ngắt kết nối; Chrome đọc được quảng cáo thật (không cần đăng nhập) |
| Fanpage đối thủ | chrome | Claude in Chrome + tài khoản thật | Facebook chặn đọc tự động khi chưa đăng nhập |
| TikTok profile đối thủ | chrome | Claude in Chrome + tài khoản thật | WebFetch chỉ trả tiêu đề trang |
| TikTok Creative Center | chrome | Claude in Chrome | WebFetch chỉ trả khung trang + nút đăng nhập |

## Cách đọc từng nguồn

### Website/blog đối thủ (public-auto)
- Ưu tiên trang chủ, trang khuyến mãi, bảng giá, blog mới nhất. Nếu URL trong config trả 404, thử trang chủ rồi tìm link "khuyến mãi"/"bảng giá".
- Lấy: tên gói, giá, ưu đãi, câu headline, nút CTA, chủ đề bài blog mới.
- `channel = website`.

### Google Trends VN (public-auto)
- URL: `https://trends.google.com/trending?geo=VN`. Chỉ giữ xu hướng liên quan tới doanh nghiệp, website, email, phần mềm, công nghệ, mùa vụ kinh doanh (ví dụ khai trương, Tết, mùa thuế). Bỏ xổ số, thể thao, giải trí không liên quan.
- `channel = google_trends`, `competitor = thi-truong`, `product_line = general` hoặc dòng sản phẩm liên quan.

### Tìm kiếm theo keyword (public-auto)
- WebSearch từng keyword trong config, thêm năm hiện tại. Đọc 1–3 kết quả từ diễn đàn, nhóm hỏi đáp, bài so sánh để tìm **pain point khách hàng nói ra**.
- `channel = search`.

### Meta Ad Library (chrome)
- URL theo tên page đối thủ: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=VN&q=<Tên trên Ad Library>&search_type=keyword_unordered`
- URL theo keyword: thay `q=<keyword tiếng Việt>`. Kết quả theo keyword lẫn nhiều quảng cáo nước ngoài: chỉ giữ quảng cáo nhắm thị trường Việt Nam hoặc của đối thủ trong config.
- Trang tải chậm: chờ khoảng 5 giây rồi mới lấy chữ trên trang.
- Lấy: tên advertiser, ngày bắt đầu chạy, nội dung quảng cáo, ưu đãi/giá, CTA, số phiên bản ("This ad has multiple versions" = đang thử nhiều mẫu).
- `source_url` = link trang Ad Library đã tìm (kèm Library ID trong `evidence`). `channel = facebook_ads`.

### Fanpage đối thủ (chrome, tài khoản thật)
- Mở link Fanpage trong config. Đọc tối đa số bài cấu hình, mới nhất trước. Không cuộn quá phạm vi đó.
- Lấy: ngày đăng, câu mở đầu (hook), định dạng (ảnh/video/carousel), ưu đãi, CTA, lượt tương tác **hiển thị công khai**.
- Không đọc, không ghi tên/thông tin người bình luận. Có thể ghi nhận *chủ đề* bình luận lặp lại (ví dụ "nhiều người hỏi giá gia hạn") mà không nêu ai.
- `channel = facebook_page`.

### TikTok profile đối thủ (chrome, tài khoản thật)
- Mở link/@tên trong config. Đọc tối đa số video cấu hình.
- Lấy: caption, hashtag, lượt xem hiển thị, định dạng (talking head, màn hình, hài…), 3 giây đầu nói gì nếu caption mô tả.
- `channel = tiktok`.

### TikTok Creative Center (chrome)
- Trang xu hướng hashtag/nội dung, chọn khu vực Vietnam nếu có. Nếu trang yêu cầu đăng nhập hoặc không có Vietnam: ghi `blocked`/`empty` kèm lý do, bỏ qua.
- `channel = tiktok_creative_center`.

## Giới hạn bắt buộc khi dùng Chrome (ToS & an toàn tài khoản)

- Chỉ dùng tài khoản thật mà người dùng đã tự đăng nhập. Không đăng nhập hộ, không tạo tài khoản, không giả danh.
- Chỉ đọc. Không thích, không bình luận, không theo dõi, không nhắn tin, không bấm vào quảng cáo.
- Khối lượng thấp như người đọc bình thường: tối đa số bài cấu hình mỗi trang, mở từng trang một, đóng tab khi xong.
- Nền tảng hiện cảnh báo/captcha/yêu cầu xác minh: **dừng ngay**, ghi `blocked`, báo người dùng. Không tìm cách vượt.
- Không lưu dữ liệu cá nhân (tên, ảnh, số điện thoại của người dùng mạng xã hội).
