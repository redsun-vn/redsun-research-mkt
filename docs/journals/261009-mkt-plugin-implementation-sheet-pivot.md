# Plugin redsun-mkt: đổi kiến trúc lưu trữ sang Google Sheet giữa lúc đang build

**Ngày**: 2026-10-09 10:42 (Asia/Saigon)
**Mức độ**: High
**Thành phần**: redsun-mkt Claude plugin (3 skill, runbook SETUP/DAILY, `validate_trace.py`)
**Trạng thái**: Đang dở, bị chặn ở E2E ghi Sheet và AC9

## Chuyện gì đã xảy ra

Plugin xong phần lớn: 3 skill, runbook SETUP/DAILY, `validate_trace.py` (stdlib), 11 test pass, `plugin validate` pass. Đã push `redsun-vn/redsun-research-mkt` nhánh main (ccbc4a7, ce13c4f). Giữa chừng team gửi Google Sheet template sẵn có, nên phải đổi lưu trữ sang một Sheet dùng chung, ghi qua Google Sheets connector, thêm tab Content Calendar và cột Trạng thái trong Chiến lược content.

## Cảm nhận thật

Mệt. Chốt kiến trúc khi chưa biết team đã có template là lỗi của mình. Đổi giữa chừng nghĩa là viết lại tầng ghi và tầng validate. Nhưng spike sớm đã bắt được giới hạn connector, nếu không sẽ đi sai hướng hoàn toàn.

## Chi tiết kỹ thuật

- Drive connector không sửa được nội dung file, chỉ upload CSV thành Google Sheet.
- Sheets parse `=1+1` thành 2, `0800` thành 800. Dấu nháy đơn đầu giữ text.
- WebFetch lỗi trên Meta Ad Library và TikTok. Chrome đọc được Ad Library.
- Drive search loại file đã trashed.
- Code review 4 High, 13 Medium, đã fix: spoof dòng approval, parse pillar lệch NFC/case, formula injection, lên lịch trùng, validation lỏng, temp path, rule chống prompt injection.
- Test dữ liệu thật ngày 2026-10-09: 2 dòng SIPOS truy vết được, 1 dòng REDSUN BOS sai bị reject.
- Đã thử: sửa file qua Drive (không được), upload CSV (chạy được nhưng phải chặn công thức và số 0 đầu bị mất).

## Nguyên nhân gốc và bài học

Thiết kế lưu trữ được chốt trước khi kiểm tra artifact có sẵn của team. Spike năng lực connector đến muộn.

- Hỏi team về artifact có sẵn trước khi chọn kiến trúc.
- Spike năng lực connector (ghi, sửa, parse) trước khi viết code.
- Mọi giá trị ghi vào Sheets phải chặn tiền tố `=`, `+`, `-`, `@`.

## Việc tiếp theo

- Bật Google Sheets connector trong session, chạy E2E ghi Sheet thật. Owner chưa gán, cần PM xác nhận.
- Chạy AC9 với user thật, tạo scheduled tasks (đang pending). Chưa có deadline trong input.
- Team xác nhận: WEBINO chưa có kênh riêng, REDSUN BOS chưa có pillar và observation.

Status: Đang dở. Code đã push, E2E ghi Sheet và AC9 chưa test.
