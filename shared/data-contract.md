# Data contract — kho insight & content calendar

Đây là nguồn duy nhất định nghĩa cấu trúc dữ liệu. Mọi skill tham chiếu file này, không định nghĩa lại.

## 1. Sự thật về Google Drive connector (đã kiểm chứng 2026-10-09)

- `create_file` tạo được folder, Google Doc, Google Sheet (upload CSV → tự chuyển thành Sheet).
- **Không sửa được nội dung file đã tạo.** `update_file` chỉ đổi tên và thư mục cha.
- Đọc Sheet thành CSV: `download_file_content` với `exportMimeType: "text/csv"` (kết quả base64).
- Đọc Doc thành text: `download_file_content` với `exportMimeType: "text/plain"`, hoặc `read_file_content`.
- Lưu nội dung base64 ra file (chạy được trên macOS, Linux, Windows): ghi chuỗi base64 vào `x.b64` rồi `python3 -m base64 -d x.b64 > x.csv`. **Không** dùng `base64 -d x.b64` (macOS không nhận đối số file).
- Liệt kê: `search_files` với `parentId = '<id>' and createdTime > '<RFC3339>'`.
- Xoá: chỉ `trash_file` (vào thùng rác).

Hệ quả: dữ liệu **chỉ ghi thêm** (mỗi lần chạy tạo file mới). Muốn "sửa" config thì tạo bản mới và chuyển bản cũ vào `config/_cu/` bằng `update_file` đổi `parentId`.

## 2. Cấu trúc thư mục trên Drive

```
RedSun-MKT-Research/
  config/
    config        (Google Doc)  — product line, đối thủ, keyword, kênh
    strategy      (Google Doc)  — Content Strategy + trạng thái duyệt
    settings      (Google Doc)  — tham số chạy
    _cu/                        — bản config cũ
  insights/       — mỗi lần research: 1 Google Sheet  INS_YYYYMMDD_HHMM_<mode>
  runs/           — mỗi lần research: 1 Google Sheet  RUN_YYYYMMDD_HHMM_<mode>
  calendar/       — mỗi tuần: Sheet CAL_YYYY-Www (+ _v2…) và Doc CAL_YYYY-Www_review
  README          (Google Doc)  — giải thích thư mục cho người xem
```

Thư mục `insights/` phẳng (không chia tháng). Lọc theo `createdTime`.

## 3. Bảng insight (mỗi file trong `insights/`)

Cột theo đúng thứ tự:

| Cột | Bắt buộc | Quy tắc |
|---|---|---|
| `insight_id` | có | `INS-YYYYMMDD-HHMM-NN` (giờ bắt đầu run, NN = 01..99) — duy nhất mà không cần đọc dữ liệu cũ |
| `run_id` | có | `RUN-YYYYMMDD-HHMM` |
| `captured_at` | có | ISO 8601, giờ VN, ví dụ `2026-10-09T08:05:00+07:00` |
| `product_line` | có | một trong `saas`, `hosting`, `server`, `email`, `general` |
| `competitor` | có | tên đối thủ trong config, hoặc `thi-truong` nếu là tín hiệu chung |
| `channel` | có | `website`, `facebook_page`, `facebook_ads`, `tiktok`, `tiktok_creative_center`, `google_trends`, `search`, `other` |
| `source_mode` | có | `public-auto` hoặc `chrome` |
| `source_url` | có | bắt đầu bằng `http` — trang cụ thể chứa bằng chứng |
| `observation` | có | **Quan sát**: điều thấy được, mô tả trung lập |
| `evidence` | có | **Căn cứ/dữ liệu**: trích nguyên văn ngắn (≤300 ký tự) hoặc số liệu, kèm ngữ cảnh |
| `meaning` | có | **Ý nghĩa**: vì sao quan trọng với product line này / khách hàng |
| `content_idea` | có | **Content Idea**: hướng ý tưởng 1–2 câu, không phải bài viết hoàn chỉnh |
| `tags` | có | ≥1 giá trị trong `pain_point`, `offer`, `cta`, `keyword`, `content_pattern`, `topic`, nối bằng `\|` |
| `dup_of` | không | `insight_id` cũ nếu trùng; để trống nếu mới |

Ý nghĩa 6 tag:
- `pain_point` — nỗi đau/khó khăn khách hàng nói ra hoặc đối thủ nhắm vào.
- `offer` — ưu đãi, giá, quà tặng, gói.
- `cta` — lời kêu gọi hành động và cách dẫn dắt.
- `keyword` — từ khoá/cụm từ lặp lại nhiều lần.
- `content_pattern` — định dạng/cấu trúc nội dung đáng chú ý (hook, độ dài, format video, series…).
- `topic` — chủ đề đang được nhắc nhiều.

**Trùng lặp:** khoá = `source_url` + `observation` đã chuẩn hoá (chữ thường, bỏ dấu câu, gộp khoảng trắng). So với insight 14 ngày gần nhất. Dòng trùng vẫn ghi, điền `dup_of`. Calendar bỏ qua dòng có `dup_of`.

## 4. Bảng run log (mỗi file trong `runs/`)

Một dòng cho mỗi nguồn đã thử, cột: `run_id, trigger, runtime, mode, source, product_line, status, rows_written, reason, started_at`.
- `trigger`: `manual` | `scheduled`
- `runtime`: `claude-code` | `cowork` | `routine` | `chat`
- `mode`: `public-auto` | `chrome`
- `status`: `ok` | `blocked` | `empty` | `skipped`
- `reason`: bắt buộc khi status khác `ok` (ví dụ "trang trống do JS", "yêu cầu đăng nhập", "timeout").

## 5. Bảng content calendar (`calendar/CAL_YYYY-Www`)

| Cột | Quy tắc |
|---|---|
| `cal_id` | `CAL-YYYY-Www-NN` |
| `week` | `YYYY-Www` (ISO week) |
| `date` | `YYYY-MM-DD` trong tuần đó |
| `channel` | kênh đăng của team, lấy từ config |
| `product_line` | như bảng insight |
| `format` | ví dụ `bài viết`, `carousel`, `video ngắn`, `email` |
| `pillar_id` | phải tồn tại trong strategy và cùng `product_line` (pillar `general` dùng được cho mọi line) |
| `insight_ids` | 1–3 `insight_id` có thật, không có `dup_of`, nối bằng `\|` |
| `angle` | góc tiếp cận, viết dựa trên evidence của insight |
| `cta` | CTA đề xuất |
| `owner` | để trống cho team điền |
| `status` | `de-xuat` |

## 6. Strategy (Google Doc `config/strategy`)

- Dòng trạng thái: `Trạng thái: draft` hoặc `Trạng thái: approved`. Calendar chỉ chạy khi `approved`.
- Mỗi pillar có một dòng tiêu đề dạng: `P-HOSTING-01 | hosting | Tên pillar` (mã `P-<LINE>-NN`, product line, tên).

## 7. Kiểm tra máy móc

`scripts/validate_trace.py` kiểm insight (`--insights`) và calendar (`--calendar --insights --strategy`). Xem `--help`.
