# Data contract — Research database của Redsun

Đây là nguồn duy nhất định nghĩa cấu trúc dữ liệu. Mọi skill tham chiếu file này, không định nghĩa lại. Cấu trúc lấy đúng theo bảng mẫu team MKT làm ngày 2026-10-08, thêm tab **Content Calendar** và cột **Trạng thái** trong tab Chiến lược content.

## 1. Một Google Sheet duy nhất cho cả team

- Tên mặc định: **Redsun MKT — Research database**. Mọi thành viên dùng chung một file (chia sẻ quyền chỉnh sửa).
- Tìm file: Google Drive `search_files` với `title = 'Redsun MKT — Research database' and mimeType = 'application/vnd.google-apps.spreadsheet'`. Nhiều kết quả → hỏi người dùng chọn (khi chạy theo lịch: dừng, ghi lý do vào Digest nếu đọc được, hoặc báo lỗi).
- Cần **Google Sheets connector** để đọc/ghi từng tab (`get_spreadsheet`, `get_values`, `update_values`, `update_spreadsheet`). Google Drive connector dùng để tìm file, tạo file, xuất cả file ra `.xlsx` cho máy kiểm tra.

### Tab và cột (dòng 1 là tiêu đề, giữ nguyên chữ)

Tiêu đề có dạng `Nhãn tiếng Việt (khoa)`. Máy kiểm tra đọc phần `khoa` trong ngoặc.

**Hướng dẫn** — `Mục | Nội dung`. Giải thích bảng và 7 quy tắc. Chỉ người phụ trách sửa.

**Nguồn theo dõi** (cấu hình)
`Sản phẩm (san_pham) | Loại (loai) | Tên (ten) | Fanpage (fanpage) | TikTok (tiktok) | YouTube (youtube) | Blog / giá / website (blog_gia_website) | Từ khóa Ad Library (tu_khoa_ad_library) | Ghi chú (ghi_chu)`
- `loai`: `cấu_hình` (dòng tham số, `san_pham = CẤU HÌNH`), `của mình`, `đối thủ`, `đề xuất chờ duyệt` (chưa chạy), `từ khóa` (danh sách từ khoá ở cột Ghi chú, ngăn bằng `;`).
- Dòng cấu hình bắt buộc: `Giới hạn mỗi lần chạy`, `Luân phiên sản phẩm`, `Chủ đề nóng hằng tuần`.
- Ô ghi `không có`, `chưa có`, `chưa xác minh` = không có nguồn đó.

**Chiến lược content**
`Mã (ma) | Sản phẩm (san_pham) | Giai đoạn (giai_doan) | Trụ cột (tru_cot) | Góc (goc) | Chủ đề đề xuất (chu_de_de_xuat) | Ghi chú (ghi_chu) | Trạng thái (trang_thai)`
- `trang_thai`: `đã duyệt` (dùng được cho lịch), `nháp` (chờ người duyệt), `thông tin` (dòng tham số như KÊNH, TỶ LỆ, TM-*, K-*, NN — không phải trụ cột).
- Chỉ **người duyệt** đổi `nháp` → `đã duyệt`. Claude không bao giờ tự ghi `đã duyệt`.
- Giai đoạn hiện tại: dòng có `giai_doan` chứa chữ `hiện tại`.

**Insight hằng ngày** (dữ liệu thô, Bước 1)
`Ngày (ngay) | Sản phẩm (san_pham) | Kênh (kenh) | Đối thủ (doi_thu) | Loại thông tin (truong) | Insight (insight) | Tín hiệu (tin_hieu) | Nhãn (nhan) | URL nguồn (url)`
- `ngay`: `YYYY-MM-DD`.
- `kenh`: `Facebook`, `Facebook Groups`, `Quảng cáo Meta`, `TikTok`, `YouTube`, `Website blog`, `Tìm kiếm web`, `Google Trends`; nhiều kênh nối bằng `+`.
- `truong`: `chu_de` (chủ đề nhắc nhiều), `tu_khoa` (keyword lặp lại), `execution` (cách đối thủ triển khai), `offer`, `cta`, `pain` (nỗi đau khách hàng), `pattern` (mẫu nội dung đáng chú ý).
- `insight`: tối đa một câu ngắn (≤ 250 ký tự), không dán toàn văn.
- `tin_hieu`: số liệu hiển thị công khai (lượt thích, chia sẻ, xem, số quảng cáo…), có thể trống.
- `nhan`: bắt đầu bằng `mới`, `lặp lại (lần N)` (đã thấy trong 7 ngày trước) hoặc `mốc` (số liệu của chính thương hiệu); có thể thêm ghi chú sau dấu `;`.
- `url`: link `http(s)://` mở lại được.

**Research database** (BẢNG CHÍNH, Bước 2: Quan sát → Căn cứ → Ý nghĩa → Content Idea)
`Mã (id) | Ngày đầu thấy (ngay_dau) | Ngày thấy gần nhất (ngay_gan_nhat) | Số lần thấy (so_lan_thay) | Sản phẩm (san_pham) | Đối thủ (doi_thu) | Quan sát (quan_sat) | Căn cứ / dữ liệu (can_cu) | URL nguồn (url) | Ý nghĩa (y_nghia) | Độ tin cậy (do_tin_cay) | Content Idea (content_idea) | Trạng thái (trang_thai)`
- `id`: `OB001`, `OB002`… liên tục, không dùng lại.
- `so_lan_thay`: số nguyên ≥ 1.
- `do_tin_cay`: bắt đầu bằng `cao`, `vừa` hoặc `thấp` (kèm lý do trong ngoặc khi `thấp`).
- `trang_thai`: `gợi ý, chờ người duyệt` (Claude ghi), `đã duyệt` / `bỏ` (chỉ người duyệt ghi), `mốc` (số liệu thương hiệu, không dùng cho lịch).
- Quan sát lặp lại: **không thêm dòng**, chỉ sửa `ngay_gan_nhat` và `so_lan_thay` của dòng cũ.

**Digest** — `Ngày (ngay) | Mục (muc) | Nội dung (noi_dung)`
- Mỗi lần research ghi các mục: `Chủ đề`, `Từ khóa lặp lại`, `Cách đối thủ triển khai`, `Offer`, `CTA`, `Pain point`, `Pattern`, `Mới so với hôm qua`, `Nguồn lỗi/bị chặn`, `Tóm tắt lượt chạy`. Thêm khi có: `Đối thủ mới nên xem xét thêm vào watchlist`, `Mốc <SẢN PHẨM>`.
- Mỗi lần lập lịch ghi: `Lịch tuần YYYY-Www` (tóm tắt) và `Lịch tuần YYYY-Www — đã loại` (ý tưởng không truy vết được, kèm lý do; ghi `không có` nếu không có).
- `Tóm tắt lượt chạy` ghi: sản phẩm, chế độ (thường/Chrome), kích hoạt (theo lịch/chạy tay), môi trường (Claude Code/Cowork), số insight, số quan sát mới/cập nhật.

**Content Calendar** (Bước 3, tab mới)
`Mã lịch (ma_lich) | Tuần (tuan) | Ngày đăng (ngay_dang) | Kênh (kenh) | Sản phẩm (san_pham) | Mã trụ cột (ma_tru_cot) | Mã quan sát (ma_quan_sat) | Góc / tiêu đề (goc_tieu_de) | Định dạng (dinh_dang) | CTA (cta) | Người phụ trách (nguoi_phu_trach) | Trạng thái (trang_thai)`
- `ma_lich`: `CAL-YYYY-Www-NN`. `tuan`: `YYYY-Www` (tuần ISO). `ngay_dang`: `YYYY-MM-DD`, thứ Hai–thứ Sáu của tuần đó.
- `ma_tru_cot`: một mã trong Chiến lược content có `trang_thai = đã duyệt` và cùng `san_pham`.
- `ma_quan_sat`: 1–3 mã `OBxxx` có trong Research database, cùng `san_pham`, không phải `mốc`/`bỏ`; nối bằng `; `.
- `trang_thai`: `đề xuất, chờ duyệt`.

## 2. Quy tắc ghi (bắt buộc)

1. **Chỉ nối dòng mới ở cuối bảng.** Đọc cột A bằng `get_values` với vùng mở (ví dụ `'Insight hằng ngày'!A:A`) để biết dòng cuối, rồi `update_values` từ dòng kế tiếp. Không chèn dòng, không sắp xếp, không xoá.
2. **Dòng cũ:** chỉ được sửa `Ngày thấy gần nhất` và `Số lần thấy` trong Research database. Không sửa gì khác.
3. **Mọi ô chữ ghi kèm dấu `'` ở đầu** (ví dụ `'2026-10-08`, `'OB015`, `'-50% phí gia hạn`). Lý do: Sheets tự đổi chữ thành số/ngày/công thức (`=1+1` thành `2`, `0800` thành `800`); dấu `'` giữ nguyên chữ và không hiện ra. Ngoại lệ duy nhất: `Số lần thấy` ghi số.
4. **Đọc lại sau khi ghi** (`get_values` đúng vùng vừa ghi) và so số dòng.
5. Không bao giờ ghi `đã duyệt` vào Chiến lược content hay Research database.

## 3. Máy kiểm tra

`scripts/validate_trace.py` đọc file `.xlsx` xuất từ Drive (`download_file_content` với `exportMimeType: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`; nhận cả file kết quả JSON mà công cụ lưu lại, hoặc thư mục CSV mỗi tab một file) và kiểm:
- `--check data`: các tab dữ liệu đúng quy ước ở trên.
- `--calendar-draft lich.csv --clean-out lich-sach.csv`: kiểm từng dòng lịch nháp với Research database và Chiến lược content; ghi các dòng hợp lệ ra file sạch.

Mã thoát: `0` sạch · `1` có dòng lỗi/bị loại · `2` không có trụ cột nào `đã duyệt` cho sản phẩm cần lập lịch. Xem `--help`.
