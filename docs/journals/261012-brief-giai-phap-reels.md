# Brief "bán giải pháp" + brief video cho redsun-reels: release tag thiếu file, Sheet thật lệch tên

**Ngày**: 2026-10-12 (Asia/Saigon)
**Mức độ**: Medium
**Thành phần**: `shared/working-rules.md`, `shared/data-contract.md`, `templates/sheet/5-research-database.csv`, `scripts/validate_trace.py`, skill `mkt-content-calendar` (brief video Khuôn 1)
**Trạng thái**: Code xong, test pass, chưa commit (nhánh `feat/brief-giai-phap-reels`, v0.3.0)

## Chuyện gì đã xảy ra

Làm theo plan `plans/261012-1038-brief-giai-phap-reels`:

- `shared/working-rules.md`: thêm luật bán giải pháp và luật trích nguyên văn lời khách.
- Thêm 5 cột tuỳ chọn N–R (`mo_hinh`, `loi_khach`, `tinh_huong`, `hau_qua`, `khoang_trong`) vào data-contract, template CSV và `validate_trace.py`. Mỗi phần tách bằng `;` của `loi_khach` phải có URL http(s). Sheet cũ 13 cột vẫn pass.
- Thêm 5 test mới, tổng 16 test pass.
- Viết lại brief video (Khuôn 1) thành gói nguyên liệu cho redsun-reels, không chia cảnh. Calendar đọc luật reels từ GitHub.

## Cảm nhận thật

Tưởng đọc từ release là an toàn nhất, hoá ra release lại cũ hơn chính thứ mình cần. Sheet thật thì đặt tên khác với tên skill tìm. Cả hai lỗi đều chỉ lộ ra khi chạy trên dữ liệu thật, đọc tài liệu thì không thấy.

## Chi tiết kỹ thuật

- Release mới nhất của redsun-reels là v0.5.0, thiếu `config/kieu-ke.ts` và `.claude/skills/tao-reel/references/luat-kich-ban.md` (404). Hai file này chỉ có trên main.
- **Quyết định**: đọc từ release tag trước. Nếu thiếu file nào thì đọc cả 4 file từ `main@<sha7>` và ghi phiên bản đó vào brief. Không chọn trộn file từ tag với file từ main, vì luật đọc ra có thể không khớp phiên bản với nhau.
- Sheet thật của team tên là `"Research database "` (có dấu cách cuối), không khớp tên `'Redsun MKT — Research database'` mà skill tìm. User đã đồng ý, nên mình ghi header vào `N1:R1`. Ô `N1` trước đó chỉ chứa ký tự xuống dòng, nên luật UPDATE giờ coi ô chỉ có khoảng trắng là ô trống.
- Mô phỏng bước "Brief đủ chưa" của reels trên 3 brief video thật tuần W42:
  - Brief 1: không còn câu hỏi nào.
  - Brief 2: chỉ hỏi về `tinhNang`, hook ở mức sát ngưỡng (~18–20/25).
  - Brief 3: thiếu dữ liệu nỗi đau của khách sạn.
- Đã vá 3 lỗ hổng của template: goal phải khớp CTA; danh sách storytelling mặc định là `pov,tieu-pham,twist`; chặn "chưa gửi redsun-reels" khi thiếu nỗi đau hoặc có dưới 3 hook ứng viên.

## Bài học

- Đừng tin release tag là bản mới nhất. Phải kiểm tra từng file cần đọc có tồn tại không, và ghi phiên bản đã đọc vào output.
- Phải dò tên Sheet thật trước khi giả định tên. Tên do người đặt sẽ có dấu cách thừa.
- Coi ô chỉ có khoảng trắng là ô trống khi ghi đè header.
- Mô phỏng phía nhận (reels) trên brief thật thì bắt được lỗ hổng template mà unit test không bắt được.

## Việc tiếp theo

- Các dòng calendar cũ còn số không có nguồn ("30 giây", "1 phút") và định dạng "20-40 giây". Cần dọn hoặc đánh dấu. Chưa có owner.
- Lệch tên Sheet thật với tên skill tìm: chưa xử lý. Cần quyết định đổi tên Sheet hay nới cách skill tìm Sheet.
- Commit nhánh `feat/brief-giai-phap-reels` và phát hành v0.3.0.

Status: Code xong, 16/16 test pass, chưa commit. Calendar cũ và lệch tên Sheet còn mở.
