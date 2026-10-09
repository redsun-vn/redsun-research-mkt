# Lập kế hoạch plugin nghiên cứu thị trường và lịch nội dung (MKT)

**Date**: 2026-10-09 09:47 (Asia/Saigon)
**Severity**: Medium
**Component**: redsun-research-mkt — Claude plugin (mkt-setup, mkt-research, mkt-content-calendar)
**Status**: Ongoing

## Điều gì đã xảy ra

Chạy brainstorm `--ultra` (best-of-5), chọn phương án A nhưng biên thắng thấp. Từ đó lập plan 7 phase tại `plans/261009-0947-mkt-research-calendar-plugin/plan.md`. Báo cáo brainstorm: `plans/reports/brainstorm-261009-0941-mkt-research-calendar-workflow.md`. Chưa viết dòng code nào. Chưa có repo GitHub nên chưa push.

## Sự thật phũ phàng

Biên thắng thấp nghĩa là năm phương án gần như ngang nhau. Chọn A là chọn có lý lẽ, chưa có bằng chứng mạnh. Plan đứng trên vài giả định chưa kiểm chứng, và chưa có dòng nào được chạy thử.

## Quyết định chính

- Dữ liệu trên Drive: file CSV bất biến theo từng lần chạy, cộng `index.csv` dựng lại. Không dùng một Google Sheet vì connector "append" chưa được xác nhận.
- Đường cài đặt chính là marketplace plugin, zip là phương án dự phòng.
- Tag cố định: `pain_point | offer | cta | keyword | content_pattern | topic`.
- Bốn dòng sản phẩm cho redsun.vn: saas, hosting, server, email.
- Nghiên cứu công khai chạy tự động. Nghiên cứu hằng ngày dùng Chrome thủ công qua tài khoản thật của nhân viên, không giả danh ai.
- Cổng duyệt: chiến lược phải ở trạng thái approved mới sinh được lịch nội dung. Có validator truy vết và negative test.
- MKT không rành kỹ thuật, nên `SETUP.md` và `DAILY.md` là runbook để Claude thực thi từng thao tác UI một. Thêm AC9: test với người dùng thật.

## Rủi ro đã ghi nhận

- Tài khoản Facebook có thể bị gắn cờ do đọc Chrome hằng ngày.
- Owner có thể tắt lịch chạy.
- Nguồn render bằng JS (Ad Library, TikTok Creative Center VN) có thể trả về rỗng khi dùng WebFetch.

## Chi tiết kỹ thuật

Phase 1 là spike phải kiểm chứng: ghi file lên Drive; WebFetch trên Ad Library và TikTok Creative Center VN; Chrome chạy trong scheduled task cục bộ; lịch từ xa của Cowork; connector routines.

## Đã thử gì

Chỉ có brainstorm best-of-5. Chưa có thử nghiệm nào được chạy. Mọi kết luận hiện tại là suy luận từ tài liệu và giả định.

## Phân tích nguyên nhân gốc

Yêu cầu có hai phần khó chung: dữ liệu phải ghi được vào Drive và nguồn phải đọc được qua công cụ tự động. Cả hai chưa được kiểm chứng, nên brainstorm chỉ có thể so sánh trên giấy.

## Bài học

Trước khi cam kết lịch trình, mọi thứ phụ thuộc connector phải chạy thử. Biên thắng thấp trong best-of-5 là tín hiệu phải làm spike sớm, không phải lý do để tiếp tục lập kế hoạch dài hơn.

## Bước tiếp theo

- Chạy Phase 1 spike trước mọi việc khác. Chưa xác định owner trong đầu vào, cần người nhận rõ ràng.
- Nếu spike ghi Drive hoặc đọc nguồn thất bại, viết lại plan trước khi làm Phase 2.
- Xác nhận với Owner về việc có chấp nhận lịch chạy bị tắt không.

Status: Ongoing. Plan đã lập, chưa có bằng chứng kỹ thuật, đang chờ Phase 1 spike.
