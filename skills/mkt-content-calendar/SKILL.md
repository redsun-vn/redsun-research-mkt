---
name: mkt-content-calendar
description: Lập Content Calendar tuần cho redsun.vn theo từng kênh và dòng sản phẩm, chỉ từ insight thật trong kho insight trên Google Drive và pillar của Content Strategy đã duyệt — mỗi dòng lịch truy ngược được về insight_id và pillar_id. Dùng khi người dùng nói "lập lịch tuần", "content calendar", "lên lịch nội dung tuần sau", hoặc khi lịch tự động thứ Hai gọi.
---

# mkt-content-calendar — lịch nội dung tuần truy vết được

Trước khi làm, đọc (tính từ thư mục chứa file này):
- `../../shared/working-rules.md` — **bắt buộc**.
- `../../shared/data-contract.md` — cột lịch, cách đọc Drive.
- `references/calendar-rules.md` — cách chọn insight, phân bổ pillar, viết file review.

**Nguyên tắc số 1:** không có dòng lịch nào được tự nghĩ ra. Mỗi dòng phải dựa trên 1–3 insight có thật và 1 pillar trong strategy đã duyệt. Thiếu insight cho một pillar → ghi vào phần "Cần research thêm", **không** bịa topic.

## 1. Xác định tuần

Mặc định là tuần ISO kế tiếp (gọi vào thứ Hai thì lập cho chính tuần đó nếu người dùng nói "tuần này"). `week = YYYY-Www`. Ngày đăng nằm trong tuần đó.

## 2. Kiểm tra strategy đã duyệt

1. Tìm thư mục `RedSun-MKT-Research` → `config/strategy` (Doc), export `text/plain`.
2. Không có dòng `Trạng thái: approved` → **dừng**, không tạo file nào, và nói:
   "Content Strategy vẫn đang ở bản nháp nên mình chưa lập lịch được (để tránh ý tưởng lệch chiến lược). Nhờ <Người duyệt trong strategy> mở file strategy trên Drive, kiểm tra các pillar, rồi đổi dòng 'Trạng thái: draft' thành 'Trạng thái: approved'. Link: <link>."
3. Lấy danh sách pillar từ các dòng `P-<LINE>-NN | <product_line> | <tên>` cùng mục tiêu, kênh, tần suất, tỷ trọng.

## 3. Đọc kho insight

- Đọc `config/config` (kênh team đăng) và `config/settings` (số ngày lookback, mặc định 30).
- `search_files` trong `insights/` với `createdTime` trong lookback. Export từng Sheet ra `text/csv`, gộp lại. Bỏ dòng có `dup_of`.
- Kho trống → dừng và nói "Kho insight chưa có dữ liệu trong <n> ngày qua, mình cần chạy research trước."

## 4. Soạn lịch

Theo `references/calendar-rules.md`:
- Với mỗi kênh × dòng sản phẩm trong strategy: số bài theo tần suất của pillar; chọn pillar theo tỷ trọng.
- Mỗi bài: chọn 1–3 insight cùng `product_line` (hoặc `general`) khớp với mục tiêu/pain point của pillar. Viết `angle` và `cta` **dựa trên evidence của các insight đó**.
- `cal_id = CAL-YYYY-Www-NN`, `status = de-xuat`, `owner` để trống.

## 5. Kiểm tra truy vết (bắt buộc)

Nếu chạy được lệnh (Claude Code, Cowork):
1. Lưu ra file tạm ngoài thư mục plugin: `/tmp/redsun-mkt/cal.csv`, `/tmp/redsun-mkt/insights.csv` (gộp, giữ cả dòng `dup_of`), `/tmp/redsun-mkt/strategy.txt`.
2. Chạy:
   `python3 "<thư mục skill này>/../../scripts/validate_trace.py" --calendar /tmp/redsun-mkt/cal.csv --insights /tmp/redsun-mkt/insights.csv --strategy /tmp/redsun-mkt/strategy.txt --clean-out /tmp/redsun-mkt/cal-clean.csv`
3. Exit `2` → strategy chưa duyệt (quay lại bước 2). Dòng trong `REJECTED:` → đưa vào mục "Đã loại" cùng lý do in ra. Chỉ ghi `cal-clean.csv` lên Drive.

Không chạy được lệnh (chat thường): với **từng dòng**, đối chiếu từng `insight_id` có trong bảng insight đã đọc và không có `dup_of`; `pillar_id` có trong strategy và cùng product line (hoặc `general`). Ghi rõ trong file review: "Kiểm tra thủ công, không có máy kiểm tra" và khuyên lần sau chạy trên Cowork/Claude Code.

## 6. Ghi lên Drive (không ghi đè)

1. Kiểm tra `calendar/` đã có `CAL_YYYY-Www` chưa; có rồi thì đặt tên `CAL_YYYY-Www_v2` (v3…).
2. `create_file` Sheet lịch (CSV → Sheet, như insight).
3. `create_file` Doc review `CAL_YYYY-Www_review` (upload `text/plain`), theo mẫu trong `references/calendar-rules.md`: độ phủ pillar, insight được dùng nhiều nhất, "Cần research thêm", "Đã loại".

## 7. Báo kết quả

```
Đã lập lịch tuần <YYYY-Www>: <n> bài cho <các kênh>.
- Mỗi bài đều ghi rõ dựa trên insight nào và pillar nào.
- Pillar còn thiếu insight: <danh sách hoặc "không">
- Ý tưởng bị loại vì không truy được nguồn: <số>
Lịch: <link Sheet> · Giải thích: <link Doc>
```
