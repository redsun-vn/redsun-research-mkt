---
name: mkt-content-calendar
description: Tạo Content Calendar tuần cho Redsun ngay khi team MKT hỏi (hoặc theo lịch thứ Hai) — lấy Content Idea từ các quan sát trong Research database và trụ cột đã duyệt trong Chiến lược content, ghi vào tab Content Calendar; mọi dòng lịch truy ngược được về mã quan sát (OB) và mã trụ cột. Cũng viết idea/brief theo format chuẩn để copy cho agent tạo video, tạo nội dung. Dùng khi người dùng nói "lập lịch tuần", "content calendar", "lên lịch nội dung tuần sau/tuần này", "lịch cho SIPOS/WEBINO", "hôm nay làm nội dung gì", "viết idea", "viết brief", "viết kịch bản video", "duyệt strategy", "strategy đã ổn chưa".
---

# mkt-content-calendar — lịch tuần từ Content Idea có căn cứ

Đọc trước (tính từ "Base directory" của skill):
- `../../shared/working-rules.md` — **bắt buộc**.
- `../../shared/data-contract.md` — tab Content Calendar, Chiến lược content, Research database.
- `../../shared/sheet-access.md` — đọc/ghi Sheet bằng connector hoặc bằng Chrome.
- `references/calendar-rules.md` — nhịp đăng, tỷ lệ, cách chọn Content Idea, mẫu Digest.
- `references/content-brief-format.md` — **khuôn bắt buộc** khi viết idea/brief (mục 7).

**Nguyên tắc số 1:** không tự nghĩ topic. Mỗi dòng lịch = một **Content Idea có sẵn** trong Research database (qua mã OB) được đặt vào **một trụ cột đã duyệt**. Trụ cột thiếu quan sát → ghi vào "Cần research thêm", không bịa.

Chạy được **bất cứ lúc nào** người dùng hỏi, không chỉ thứ Hai.

## 1. Xác định tuần và sản phẩm

- Tuần: người dùng nói "tuần này" → tuần ISO hiện tại; "tuần sau" hoặc không nói → tuần kế tiếp. Lời nhắn theo lịch ghi "tuần này" → tuần hiện tại. `tuan = YYYY-Www`; ngày đăng thứ Hai–thứ Sáu.
- Sản phẩm: người dùng nêu thì theo đó; không thì mọi sản phẩm có trụ cột `đã duyệt` (mặc định SIPOS, WEBINO; REDSUN BOS tạm ngoài lịch theo ghi chú trong bảng).

## 2. Đọc dữ liệu (theo `../../shared/sheet-access.md`)

1. Tìm file như `mkt-research` mục 1.
2. Đọc các tab:
   - `'Chiến lược content'!A:H` — trụ cột, giai đoạn, trạng thái; dòng `thông tin`: KÊNH (nhịp đăng), TỶ LỆ, TM-* (thông điệp chủ đạo), K-* (vai trò kênh), NN (ngành mũi nhọn).
   - `'Research database'!A:M` — quan sát và Content Idea.
   - `'Nguồn theo dõi'!A:I` — kênh **của mình** của từng sản phẩm (link Fanpage/TikTok).
   - `'Content Calendar'!A:L` — mã lịch đã có (tránh trùng; tuần này đã có lịch → hỏi người dùng muốn **lập thêm** hay **chỉ xem**; theo lịch tự động: bỏ qua, báo đã có).
3. Sản phẩm không có trụ cột `đã duyệt` → không lập lịch cho sản phẩm đó và nói: "Chiến lược content của <SP> chưa được duyệt. Người duyệt mở tab Chiến lược content, kiểm tra các dòng 'nháp' rồi đổi thành 'đã duyệt'." **Không tự đổi.**

**Câu hỏi "duyệt strategy / strategy đã ổn chưa":** tóm tắt các trụ cột theo sản phẩm và trạng thái, chỉ ra dòng `nháp`, hướng dẫn người duyệt tự đổi. Dừng ở đó.

## 3. Soạn lịch nháp

Theo `references/calendar-rules.md`:
- Số bài theo nhịp đăng (dòng KÊNH) trên các kênh **sản phẩm đang có** (dòng `của mình` có link). Kênh chưa có → không xếp, ghi vào "Cần chuẩn bị kênh".
- Chia bài theo TỶ LỆ (mặc định 60% trụ cột giai đoạn hiện tại, 25% giai đoạn trước, 15% theo ngành/nhóm khách).
- Mỗi bài: chọn 1–3 quan sát cùng sản phẩm (không `mốc`, không `bỏ`) có Content Idea khớp trụ cột; ưu tiên `Số lần thấy` cao, độ tin cậy `cao`/`vừa`, `Ngày thấy gần nhất` mới. Content Idea ghi "chưa nên làm…/cần xác minh" → chỉ dùng khi đã có điều kiện, nếu không thì bỏ qua.
- `goc_tieu_de`: phát triển **từ Content Idea của quan sát đó** theo góc của trụ cột và vai trò kênh (K-*). `cta` theo nguồn/chiến lược.
- `ma_lich = CAL-YYYY-Www-NN` (NN tiếp nối mã đã có trong tuần), `trang_thai = đề xuất, chờ duyệt`, `nguoi_phu_trach` để trống.

## 4. Kiểm tra truy vết (bắt buộc)

Chạy được lệnh và có Drive connector (Claude Code, Cowork):
1. Ghi lịch nháp ra file tạm riêng cho lần chạy (ví dụ `/tmp/redsun-mkt/<YYYY-Www>-<HHMMSS>/draft.csv`), dòng đầu là khoá cột: `ma_lich,tuan,ngay_dang,kenh,san_pham,ma_tru_cot,ma_quan_sat,goc_tieu_de,dinh_dang,cta,nguoi_phu_trach,trang_thai`.
2. Xuất Research database ra `.xlsx` bằng Drive `download_file_content` (`exportMimeType: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`), lấy đường dẫn file kết quả.
3. Chạy:
   `python3 "<Base directory>/../../scripts/validate_trace.py" --workbook "<file xuất>" --check none --calendar-draft "<draft.csv>" --products "<SP1>,<SP2>" --clean-out "<thư mục>/clean.json"`
4. Mã thoát `2` → sản phẩm thiếu trụ cột đã duyệt (quay lại bước 2). Dòng trong `REJECTED:` → đưa vào mục "đã loại" kèm lý do in ra. `VALID_ROWS: 0` → không ghi lịch, chỉ ghi Digest.

Không chạy được lệnh hoặc đang ghi qua Chrome: với **từng dòng**, đối chiếu mã trụ cột (đã duyệt, cùng sản phẩm), từng mã OB (có thật, cùng sản phẩm, không mốc/bỏ), ngày thứ Hai–thứ Sáu của tuần. Dòng sai → loại. Ghi trong Digest: "kiểm tra thủ công".

## 5. Ghi vào Sheet

1. Nối các dòng hợp lệ vào cuối `'Content Calendar'` theo `../../shared/sheet-access.md`. Có `clean.json` → dùng đúng các giá trị đó (đã có dấu `'`). Không có → tự thêm `'` vào mọi ô.
2. Nối vào `'Digest'` 2 dòng:
   - `Lịch tuần YYYY-Www`: số bài theo sản phẩm/kênh, độ phủ trụ cột, trụ cột thiếu quan sát (Cần research thêm), kênh chưa có (Cần chuẩn bị kênh), cách kiểm tra (máy/thủ công).
   - `Lịch tuần YYYY-Www — đã loại`: mã + lý do, hoặc `không có`.
3. Đọc lại vùng vừa ghi.

## 6. Báo kết quả

```
Đã lập lịch tuần <YYYY-Www>: <n> bài (<SP>: <a> Facebook, <b> TikTok…).
- Mỗi bài dựa trên Content Idea của quan sát OB… và trụ cột đã duyệt.
- Trụ cột cần research thêm: <danh sách | không có>
- Ý tưởng bị loại vì không truy vết được: <số>
Xem lịch: <link Research database> (tab Content Calendar). Tất cả đang ở trạng thái "đề xuất, chờ duyệt".
```

## 7. Viết idea / brief cho agent (khi người dùng xin)

Người dùng nói "viết idea", "viết brief", "viết kịch bản", "hôm nay làm nội dung gì", "làm video cho bài CAL-…":
1. Xác định các dòng lịch cần viết: theo mã lịch người dùng nêu; "hôm nay" → các dòng có `ngay_dang` là hôm nay; chưa có lịch cho ngày đó → lập lịch trước (mục 1–5) rồi viết.
2. Đọc quan sát (OB) và trụ cột của từng dòng để lấy căn cứ, thông điệp chủ đạo (TM-*), vai trò kênh (K-*), giá/chính sách công khai ở Nguồn theo dõi.
3. Viết **đúng khuôn** trong `references/content-brief-format.md`: Khuôn 1 cho video, Khuôn 2 cho bài đăng/carousel. Mỗi idea một khối chữ thường copy được ngay; không JSON, không bảng.
4. Chạy checklist cuối file khuôn trước khi gửi.
5. Chỉ trả lời trong chat; không ghi brief vào Sheet (lịch đã có mã để truy ngược). Sản phẩm/ngày không có idea đủ điều kiện → thêm một dòng ngắn sau các khối: "<SẢN PHẨM>: chưa có idea dùng được hôm nay vì <lý do>. Việc nên làm: <…>".

