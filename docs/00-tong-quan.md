# Tổng quan: Bộ não thứ 2 & Công ty bot

> Tài liệu nền tảng, tổng hợp các thảo luận và quyết định đến ngày 2026-10-27.
> Đây là phần mở đầu của đặc tả (Giai đoạn 0). Mọi thay đổi quyết định cần cập nhật tại đây.

## 1. Tầm nhìn

**Bộ não thứ 2 cá nhân** → **Công ty bot** (CEO, nhân viên, QA) do bộ não thứ 2 điều phối dần → **Khuôn mẫu hóa** để **coaching** người khác làm được như mình.

Ý tưởng gốc: coi mỗi bot AI như một nhân viên có việc riêng, được onboard và cải thiện dần theo thời gian (Peter Yang). Tham khảo mô hình OPC HQ / weOPC.vn.

## 2. Kiến trúc

```
                         CHỦ (người ký cuối cùng)
           Telegram: chữ / tin thoại        Claude Code: web · desktop · điện thoại
                 │                                     │
   ┌─────────────▼──────────────┐                      │ xây & cải tiến
   │  BOT BỘ NÃO THỨ 2          │◄─────────────────────┘
   │  Thư ký · Cố vấn · Ôn tập  │  chạy 24/7 trên Oracle Free (dự phòng: VPS)
   │  Thang tự chủ (tầng Ký)    │  người gác cổng bên ngoài: GitHub Actions
   └──────┬─────────────────────┘
          │ (giai đoạn sau)
          ▼
   CEO bot → nhân viên · QA         ← la bàn: cây mục tiêu; QA chấm điểm
   (nhóm Telegram = phòng họp;      ← chat riêng: giao việc gấp
    backend trung tâm điều phối)
   ──────────────────────────────── LƯU TRỮ ────────────────────────────────
   Google Drive            Repo HỆ THỐNG                Repo DỮ LIỆU (private)
   kho thô, file nặng      code · skill · mẫu ·         CLAUDE.md · now.md · sessions/
   (cấu trúc PARA)         hướng dẫn → template         inbox/ · sources/ · wiki-drafts/
                           coaching                     wiki/ · decisions/ · journey/
```

### Vai trò các repo

| Repo | Vai trò | Trạng thái |
|---|---|---|
| `webforAgent` (repo này) | Học tập, nghiên cứu, viết đặc tả | Đang dùng |
| Repo hệ thống (tên tạm `second-brain-system`) | Code bot, skill, mẫu cấu trúc, hướng dẫn cài đặt; dùng làm template cho học viên | Tạo khi bắt đầu làm sản phẩm, **có hướng dẫn khởi tạo từng bước** |
| Repo dữ liệu (tên tạm `second-brain-data`, private) | Dữ liệu cá nhân: wiki, nhật ký, phiên làm việc | Tạo ở Giai đoạn 1 |

## 3. Nguyên tắc xuyên suốt

1. **Bot không tự học.** Mọi cải thiện nằm trong file: sổ tay, nhật ký quyết định, skill.
2. **Máy ghi → AI soát → Người ký.** Khung chính cho mọi quy trình. Tri thức chính thức chỉ đổi khi Chủ duyệt. Thang tự chủ chỉ áp dụng cho tầng "Người ký".
3. **Chỉ tin kết quả thật**, không tin chữ "thành công". Có kiểm tra kết quả và người gác cổng độc lập với server.
4. **Độ la bàn** cho cả việc lẫn dữ liệu: tập trung vào điều phục vụ mục tiêu.

## 4. Quyết định đã chốt

| # | Chủ đề | Quyết định |
|---|---|---|
| 1 | Thứ tự | Bộ não thứ 2 trước, công ty bot sau |
| 2 | Kênh | Telegram trước; Zalo và kênh khác để sau. Bot Telegram không đọc được tin của bot khác nên cần backend trung tâm điều phối |
| 3 | Lưu trữ | Kết hợp: Google Drive cho kho thô; GitHub cho bộ não. Không đặt repo git trong thư mục Drive đang đồng bộ |
| 4 | Repo | Tách 2 repo: hệ thống (template) và dữ liệu (private). `webforAgent` giữ vai trò nghiên cứu, đặc tả |
| 5 | Bàn giao phiên | `CLAUDE.md` (sổ tay), `now.md` (trạng thái), `sessions/` (biên bản); nghi thức đầu và cuối phiên |
| 6 | Server | Oracle Cloud Always Free, có phương án dự phòng |
| 7 | Pro và API | Gói Pro cho làm việc có Chủ tham gia; API cho bot và việc lặp lại khối lượng lớn |
| 8 | Dọn kho cũ | Quy trình B1–B5: kiểm kê → lọc trùng và chuyển đổi → thiết kế phân loại → phân loại hàng loạt → chiết xuất có chọn lọc |
| 9 | Giám sát | Người gác cổng bên ngoài bằng GitHub Actions, gửi Telegram khi bot im lặng quá 24 giờ |
| 10 | Khung vận hành | 3 tầng là khung chính; thang tự chủ (0–4) chỉ cho tầng "Người ký" |
| 11 | Nhật ký hành trình | `journey/` soạn hằng tháng từ `sessions/`, gắn nhãn riêng tư hoặc chia sẻ được, Chủ duyệt |
| 12 | Bài học của bot | Bot soạn bài học dạng nháp; Chủ duyệt một lượt mỗi tuần |
| 13 | Bối cảnh xuyên suốt | Làm việc với bộ não qua Claude Code hoặc bot; chat claude.ai thường không tự đọc repo |
| 14 | Bổ sung từ bài "3 tháng làm OPC" | `journey/`, kiểm tra kết quả thật, khung 3 tầng, nhập liệu bằng tin thoại, thiết kế dạng template |
| 15 | Vai trò CEO | Trong `webforAgent`, phiên Claude chính là CEO, điều phối subagent. Subagent đầu tiên: `chien-luoc-opc-coaching` |
| 16 | Sản phẩm bán đầu tiên (chốt 2026-10-27) | Bán Cấp 1 (không code, dùng trên điện thoại) và Cấp 2 (Obsidian liên kết) trước. Bot (Cấp 3) và công ty bot tạm hoãn đến khi có doanh thu |
| 17 | Không hoa hồng nhiều tầng (chốt 2026-10-27) | Bỏ "founder hưởng hoa hồng". Thay bằng nhóm founder không hoa hồng; sau đó giới thiệu một tầng và trợ giảng được trả công. Hỏi luật sư trước khi chi bất kỳ khoản hoa hồng nào |
| 18 | Mốc bán (chốt 2026-10-27) | Mở bán trước lớp founding trong tháng 12/2026, chạy lớp trước Tết (tháng 1/2027) |
| 19 | Giới hạn kỹ thuật (chốt 2026-10-27) | Trong 90 ngày tới, việc kỹ thuật tối đa 10 giờ/tuần; ưu tiên phỏng vấn, Zoom, bán |
| 20 | Đảo lộ trình (chốt 2026-10-27) | Template trước, bot sau. Tách hai luồng: sản phẩm bán (ưu tiên) và phòng thí nghiệm kỹ thuật |

## 5. Còn mở

| # | Câu hỏi | Khi nào cần |
|---|---|---|
| 1 | Chép lời tin thoại: Whisper trên server hay dịch vụ qua API? (thử cả hai với 10 tin thoại thật) | Giai đoạn 2 |
| 2 | Dọn kho B4: kết hợp Pro và API, hay chỉ dùng Pro? | Giai đoạn 1 |
| 3 | Khối lượng và loại dữ liệu cũ | Giai đoạn 1 |
| 4 | Vault Obsidian hiện tại nằm trong thư mục Drive hay thư mục thường? | Giai đoạn 1 |
| 5 | Nhà cung cấp API: Anthropic (đang giả định, chưa xác nhận) | Giai đoạn 2 |
| 6 | Quy tắc chat riêng (5 tình huống) và số tầng quản lý của công ty bot | Giai đoạn công ty bot |
| 7 | Chiến lược kinh doanh và coaching: Chủ trả lời 10 câu hỏi trong `docs/kinh-doanh/00-y-tuong-kinh-doanh.md` | Trước khi subagent chiến lược phân tích |
| 8 | Có thêm subagent "Nghiên cứu thị trường" và "Phản biện" không? | Sau khi subagent chiến lược chạy lần đầu |
| 9 | Chọn luật sư và chi phí tư vấn về giới thiệu hưởng hoa hồng | Trước khi mở giới thiệu một tầng |

## 6. Lộ trình

Theo quyết định 16–20, lộ trình tách **hai luồng chạy song song**:

**Luồng A: Sản phẩm bán (ưu tiên trong 90 ngày)**

| Thời gian | Nội dung | Thế nào là xong |
|---|---|---|
| Tháng 11/2026 | Dựng Cấp 1–2 cho chính Chủ và vợ (khách số 0); phỏng vấn, khảo sát; đóng gói template | Vợ Chủ đạt 4/5 tiêu chí Cấp 1; ≥ 10 phỏng vấn; ≥ 150 phiếu khảo sát |
| Tháng 12/2026 | 2 buổi Zoom, mở bán trước lớp founding (tối đa 20 chỗ) | Có học viên đặt cọc hoặc trả đủ |
| Tháng 1/2027 | Chạy lớp founding 21 ngày, trước Tết | ≥ 70% học viên đạt kết quả Cấp 1; ≥ 5 lời chứng thực có số liệu |
| Sau Tết | Mở lớp 2 | Theo kết quả lớp founding |

**Luồng B: Phòng thí nghiệm kỹ thuật (tối đa 10 giờ/tuần)**: các giai đoạn dưới đây, làm chậm lại; GĐ 6+ (công ty bot) tạm hoãn đến khi có doanh thu.

| GĐ | Nội dung | Thế nào là xong |
|---|---|---|
| 0 | Đặc tả toàn hệ thống | Chủ duyệt |
| 1 | Bộ não trên máy: khởi tạo 2 repo và Drive; skill phân loại và chiết xuất wiki; dọn kho cũ B1–B5 | ≥ 85% phân loại đúng, ≥ 80% trang wiki được chấp nhận trên bộ mẫu thử |
| 2 | Bot Telegram thu thập: chữ, link, file, tin thoại; kiểm tra kết quả thật; người gác cổng | Gửi từ điện thoại, dưới 1 phút đã thấy trong kho; có báo cáo sức khỏe hằng ngày |
| 3 | Hỏi đáp và cố vấn, có dẫn nguồn, có chế độ phản biện | ≥ 80% câu trả lời đúng và có nguồn trên bộ câu hỏi thử |
| 4 | Ôn tập theo lặp lại ngắt quãng | Nhận câu ôn đúng lịch mỗi ngày |
| 5 | Nhật ký quyết định và `journey/` | ≥ 20 quyết định đúng mẫu; cột mốc hành trình đầu tiên |
| 6+ | Công ty bot: CEO, nhân viên, QA, độ la bàn, chat riêng (**tạm hoãn đến khi có doanh thu**) | Đặc tả riêng khi đến lúc |

Khuôn mẫu hóa cho coaching không còn là bước cuối: Cấp 1–2 được đóng gói thành template ngay trong Luồng A.

Chỉ tiêu là đề xuất ban đầu, điều chỉnh khi duyệt đặc tả.

## 7. Chi phí ước tính

- API: khoảng $15–25/tháng cho mức dùng vừa phải (ước tính; đo thật bằng lệnh `/cost`). Tiếng Việt có thể tốn token hơn tiếng Anh khoảng 1,5 lần.
- Dọn kho cũ bằng API Haiku dạng batch: khoảng vài USD cho vài nghìn tài liệu (ước tính).
- Server: Oracle Free (miễn phí) hoặc VPS dự phòng khoảng $5/tháng.

## 8. Nguồn tham khảo

- [OPC HQ](https://hq.weopc.vn/) · [weOPC.vn](https://weopc.vn/)
- [6 tỷ và 70 triệu: hai con số sau 3 tháng tôi vận hành công ty 1 người cùng AI (OPC) — CHẠM.media](https://cham.media/p/3-thang-lam-opc)
