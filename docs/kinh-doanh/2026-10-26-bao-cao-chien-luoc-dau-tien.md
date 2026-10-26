# Báo cáo chiến lược đầu tiên: HaiBrain

_Ngày: 2026-10-26 · Người soạn: Trưởng phòng Chiến lược OPC & Coaching · Gửi: CEO → Chủ · Trạng thái: đề xuất, chưa chốt_

Ký hiệu dùng trong báo cáo:
- **[SỰ THẬT]**: có nguồn (tài liệu trong repo, lời Chủ, nguồn web có dẫn).
- **[SUY LUẬN]**: rút ra từ sự thật, có lập luận.
- **[GIẢ ĐỊNH]**: chưa kiểm chứng, cần thử.
- **[DỰ ĐOÁN]**: ước lượng tương lai, độ tin cậy ghi kèm.

---

## Tóm tắt

1. **Cần đổi cấu trúc sản phẩm.** Hệ thống kỹ thuật của Chủ (bot Telegram, GitHub, VPS) là **phòng thí nghiệm và bằng chứng**, không phải sản phẩm bán cho đại trà. Sản phẩm bán đầu tiên nên là **Cấp 1 (không code, dùng chủ yếu trên điện thoại)** và **Cấp 2 (Obsidian liên kết)**. Bot là Cấp 3, để sau.
2. **Bậc thang giá đề xuất** (giả định, cần kiểm chứng): Zoom miễn phí → bộ khởi động 299 nghìn → khóa nhóm 21 ngày 1,5–2,5 triệu → thành viên 199–299 nghìn/tháng → coaching 1:1 8–15 triệu (giới hạn số suất).
3. **Kế hoạch 90 ngày: bán trước, xây sau, và tránh Tết.** Tết Nguyên đán 2027 rơi vào khoảng đầu tháng 2/2027, đúng mốc Chủ đặt. Đề xuất mở bán trước khóa nhóm "founding" sau 2 buổi Zoom vào tháng 12, chạy lớp thử 10–20 người trong tháng 1, rồi mở lớp 2 sau Tết.
4. **Không làm "nhóm founder hưởng hoa hồng nhiều tầng".** Rủi ro hình ảnh (khách mục tiêu quen Amway) và rủi ro pháp lý về đa cấp đều cao. Thay bằng **giới thiệu một tầng** (chỉ hưởng trên đơn mình trực tiếp bán) và **trợ giảng được trả công**. Phải hỏi luật sư trước khi mở.
5. **50 triệu/tháng khả thi nhưng không trong 6 tháng đầu nếu chỉ dựa vào 5.000 người.** Cần khoảng 80 thành viên, 10 học viên khóa và 1 khách coaching mỗi tháng. Riêng phần khóa học đã cần khoảng 200 người dự Zoom mỗi tháng. Như Chạm Station, cộng đồng sẵn có sẽ cạn sau đợt đầu, nên phải xây kênh thu hút người mới đều đặn ngay từ tháng 1.

---

## Phân tích

### Câu 1. Kế hoạch kỹ thuật có quá phức tạp cho khách mục tiêu không?

**[SỰ THẬT]** Khách mục tiêu: 30–50 tuổi, môi giới BĐS, kinh doanh mạng lưới, tư vấn sức khỏe. Dùng tốt máy tính, không biết code, làm việc chủ yếu trên điện thoại, đi lại nhiều (lời Chủ, `01-tra-loi-cua-chu.md`).
Nỗi đau Chủ nêu:
- (a) dữ liệu cũ nhiều, không liên kết, tìm lại không thấy;
- (b) AI không có bức tranh tổng thể nên trả lời chưa như ý;
- (c) cần chỗ chứa chung để không mất bối cảnh khi di chuyển.

**[SỰ THẬT]** Kiến trúc hiện tại (`00-tong-quan.md`) gồm 2 repo GitHub, Google Drive, bot Telegram chạy 24/7 trên Oracle Cloud, GitHub Actions làm người gác cổng, API trả phí. Bước "khuôn mẫu hóa cho coaching" nằm **cuối lộ trình**, sau giai đoạn 6+.

**[SUY LUẬN]** Có, quá phức tạp cho đại trà, vì 4 lý do:
1. GitHub, VPS, API key và chi phí token là các khái niệm lạ với người không biết code. Mỗi khái niệm là một điểm dễ bỏ cuộc và một nguồn câu hỏi hỗ trợ đổ về Chủ.
2. Bot chạy 24/7 cần người vận hành. Nếu học viên tự chạy, Chủ phải hỗ trợ kỹ thuật dài hạn, trái với mục tiêu "làm 6 tháng/năm".
3. Nỗi đau (a), (b), (c) đều giải được ở mức "đủ tốt" **không cần code**: kho tài liệu trên đám mây, cấu trúc thư mục rõ ràng, và công cụ AI hỏi đáp trên tài liệu của chính mình, có trích nguồn (loại công cụ như NotebookLM, Projects của Claude hoặc ChatGPT). Cần kiểm lại tính năng và giá hiện hành của từng công cụ trước khi đưa vào khóa học.
4. Obsidian trên điện thoại dùng được, nhưng đồng bộ giữa máy tính và điện thoại là điểm ma sát lớn: phải trả phí dịch vụ đồng bộ hoặc tự cấu hình. Với người "sống trên điện thoại", đây là rủi ro hàng đầu. **[GIẢ ĐỊNH]** cần thử với vợ Chủ và 3–5 người thật.

**Đề xuất 3 cấp sản phẩm** (mỗi cấp có kết quả đo được, đo bằng hành vi chứ không chỉ bằng ảnh chụp):

| Cấp | Dành cho | Công cụ (tham khảo) | Kết quả đo được |
|---|---|---|---|
| **1. HaiBrain Cơ bản** (không code, ưu tiên điện thoại) | Đa số khách mục tiêu | Google Drive theo cấu trúc PARA, mẫu thư mục theo nghề, một công cụ AI hỏi đáp trên tài liệu riêng, thói quen ghi bằng giọng nói | (1) Có ảnh cấu trúc thư mục đúng mẫu; (2) đã nạp ≥ 30 tài liệu thật của nghề mình; (3) hỏi AI 5 câu về công việc của chính mình, ≥ 4 câu đúng và có trích nguồn; (4) tìm lại một thông tin cũ trong dưới 1 phút; (5) sau 30 ngày vẫn dùng ≥ 3 lần/tuần |
| **2. HaiBrain Liên kết** (Obsidian) | Người thích hệ thống, có thời gian ngồi máy tính | Obsidian, mẫu ghi chú, liên kết hai chiều, đồng bộ sang điện thoại | Kết quả Cấp 1, cộng thêm: ≥ 50 ghi chú có liên kết, ảnh sơ đồ liên kết (graph), làm ôn tập hằng tuần liên tục 4 tuần. Đây là bài kiểm tra đầu ra Chủ đã đề xuất |
| **3. HaiBrain Tự động** (bot, GitHub) | Người rành công nghệ, hoặc khách mua gói "làm hộ" | Hệ thống của Chủ đã khuôn mẫu hóa | Gửi tin thoại từ điện thoại, dưới 1 phút đã thấy trong kho; có báo cáo sức khỏe hằng ngày (đúng chỉ tiêu giai đoạn 2 của Chủ) |

**Điểm khác biệt nên đầu tư** **[SUY LUẬN]**: **mẫu theo nghề**, chứ không phải độ phức tạp kỹ thuật.
- Môi giới BĐS: hồ sơ dự án, pháp lý dự án, khách hàng, lịch hẹn.
- Tư vấn sức khỏe: hồ sơ khách, nhật ký theo dõi chỉ số.
- Kinh doanh mạng lưới: danh sách, lịch chăm sóc, kịch bản tư vấn.

Các khóa học cơ bản đang có trên thị trường (theo Chủ: "cài Obsidian và một câu prompt") không có lớp mẫu theo nghề này.

**Lưu ý ngoài phạm vi, chuyển CEO:** Hồ sơ sức khỏe và dữ liệu khách hàng là dữ liệu cá nhân, có thể thuộc loại nhạy cảm. Việc tải lên công cụ AI hoặc đám mây có thể chịu ràng buộc của quy định bảo vệ dữ liệu cá nhân tại Việt Nam. Cần chuyên gia pháp lý xác nhận; khóa học nên có một bài về "dữ liệu nào không đưa lên AI".

### Câu 2. Bậc thang sản phẩm và giá

**[SỰ THẬT]**
- Chạm Station: 80% doanh thu quý 3/2026 đến từ gói thành viên weOPC, 19% từ OPC HQ.
- Họ có coaching 1:1, kết quả bàn giao là bộ não thứ 2 cho học viên.
- Theo Chủ, các khóa bộ não thứ 2 cơ bản có giá hàng trăm USD.

Tôi chưa kiểm chứng được giá cụ thể của weOPC và của các khóa này: lần thử truy cập weopc.vn và cham.media hôm nay đều lỗi tên miền. **Chưa đủ dữ liệu để kết luận về mặt bằng giá.** Cách kiểm chứng: CEO hoặc Chủ chụp lại bảng giá 3–5 khóa tương tự.

**Đề xuất bậc thang** (toàn bộ giá là **[GIẢ ĐỊNH]**, phải kiểm chứng bằng đặt cọc thật):

| Bậc | Sản phẩm | Giá tham khảo | Vai trò | Thời gian của Chủ |
|---|---|---|---|---|
| 0 | Zoom miễn phí 2 tuần/lần, video ngắn lồng giọng clone, checklist PDF, nhóm cộng đồng | 0 | Marketing bằng dạy; xây danh sách | 3–4 giờ mỗi buổi (tính cả chuẩn bị) |
| 1 | **Bộ khởi động HaiBrain**: mẫu thư mục theo nghề và 5 video tự học Cấp 1 | 199–399 nghìn | Lọc người mua thật; doanh thu không tốn giờ | ~0 sau khi làm xong |
| 2 | **Khóa nhóm 21 ngày** (Cấp 1, có thể thêm Cấp 2): 4 buổi Zoom, nhóm hỗ trợ, bài kiểm tra đầu ra | 1,5–2,5 triệu (giá founding lớp 1: ~1,5 triệu, đổi lấy phản hồi và lời chứng thực) | Sản phẩm chủ lực giai đoạn đầu | ~15 giờ mỗi lớp |
| 3 | **Thành viên HaiBrain**: mẫu cập nhật, hỏi đáp hằng tháng, thư viện bài | 199–299 nghìn/tháng hoặc 1,5–2,5 triệu/năm | Doanh thu định kỳ; giữ chân sau khóa | ~4–6 giờ/tháng |
| 4 | **Coaching 1:1 "làm cùng"**: bàn giao bộ não Cấp 2 theo nghề, có thể kèm Cấp 3 nhẹ | 8–15 triệu, tối đa 3–4 suất/tháng | Biên lợi nhuận cao; nguồn nghiên cứu tình huống | ~8–10 giờ/khách |
| 5 (sau) | **Làm hộ Cấp 3** (bot) và phí duy trì | Chưa đề xuất giá; chờ hệ thống của Chủ chạy ổn ≥ 3 tháng | Nâng cao | Cần đo |

**[SUY LUẬN]**
- Nên bắt đầu ở bậc 2 (khóa nhóm), không bắt đầu ở bậc 3 (thành viên). Thành viên chỉ có giá trị khi đã có thư viện và cộng đồng.
- Khóa nhóm cho phép bán trước rồi dạy trực tiếp: dạy đến đâu ghi lại đến đó, sau này thành khóa tự học.
- So với mức "hàng trăm USD" Chủ quan sát được: 1,5–2,5 triệu đồng thấp hơn (khoảng 60–100 USD nếu giả định tỷ giá ~25–26 nghìn đồng/USD). Mức này phù hợp để thử với cộng đồng đang tin Chủ. Có thể tăng giá khi đã có lời chứng thực.

### Câu 3. Kế hoạch 90 ngày (26/10/2026 → cuối 1/2027)

**[SỰ THẬT]**
- Chạm Station: doanh thu theo tháng 23,2 → 37,9 → 9,7 triệu. Đợt đầu đến từ người theo dõi lâu năm rồi cạn, sau đó họ chuyển sang Zoom miễn phí 2 tuần/lần.
- Lợi thế của Chủ: cộng đồng khoảng 5.000 người tin tưởng; có thể mở Zoom miễn phí; không lộ mặt, không livestream; được dùng giọng clone.

**Lưu ý lịch:** **[SỰ THẬT, CEO nên kiểm lại]** Tết Nguyên đán 2027 rơi vào khoảng ngày 6/2/2027. Tháng 2 là tháng khó bán và khó học. Vì vậy nên đưa khách trả tiền đầu tiên lên trước Tết (tháng 12–1), hoặc chấp nhận lớp đầu bắt đầu sau Tết (cuối tháng 2).

**Giai đoạn A: Kiểm chứng nỗi đau (26/10 – 22/11, 4 tuần)**
- Chủ dựng Cấp 1 và Cấp 2 cho chính mình và cho vợ (khách số 0). Ghi lại thời gian, chỗ vướng và kết quả vào `journey/`.
- Phỏng vấn 10–15 người trong cộng đồng, mỗi người 20 phút. Hỏi về hành vi trong quá khứ, không hỏi "có mua không". Ví dụ: "Lần gần nhất bạn mất thông tin quan trọng là khi nào? Bạn đã làm gì? Đã trả tiền cho công cụ hoặc khóa nào chưa?"
- Gửi khảo sát 5 câu cho cộng đồng.
- **Mốc đo được:** vợ Chủ đạt 4/5 tiêu chí Cấp 1; ≥ 10 cuộc phỏng vấn; ≥ 150 phiếu khảo sát; xếp hạng 3 nỗi đau hàng đầu theo nghề.

**Giai đoạn B: Marketing bằng dạy và bán trước (23/11 – 20/12, 4 tuần)**
- Zoom miễn phí #1 (khoảng 5/12) và #2 (khoảng 19/12). Chủ đề theo nỗi đau, không theo công cụ. Ví dụ: "Tìm lại mọi thông tin khách hàng trong 30 giây bằng AI, trên điện thoại".
- Hình thức: chia sẻ màn hình và giọng nói, không bật camera.
- Cuối mỗi buổi mở bán trước **lớp founding** (tối đa 20 chỗ, khoảng 1,5 triệu, đặt cọc hoặc trả đủ, cam kết hoàn tiền nếu không đạt kết quả Cấp 1).
- **Mốc đo được** (ngưỡng là **[GIẢ ĐỊNH]**): ≥ 200 người đăng ký mỗi buổi; ≥ 40% tham dự; ≥ 5% người tham dự trả tiền. Tức là ≥ 8–10 người trả tiền sau 2 buổi.
- **Ngưỡng quyết định:** dưới 5 người trả tiền thì xem lại thông điệp, giá hoặc đối tượng trước khi xây tiếp. Không đổ thêm thời gian vào kỹ thuật.

**Giai đoạn C: Giao hàng và lấy bằng chứng (21/12 – 31/1, 6 tuần)**
- Lớp founding chạy 21 ngày, từ khoảng 4/1 đến 24/1, xong trước Tết.
- Dạy trực tiếp, ghi hình lại để làm Bộ khởi động (bậc 1) và nội dung cho thành viên.
- Zoom #3 (giữa tháng 1) nhằm mở danh sách chờ lớp 2, khai giảng sau Tết (khoảng cuối tháng 2 hoặc đầu tháng 3).
- **Mốc đo được:** ≥ 70% học viên đạt kết quả Cấp 1; ≥ 5 lời chứng thực có số liệu trước và sau (được phép công khai); ≥ 30 người trong danh sách chờ lớp 2; doanh thu tích lũy ≥ 15 triệu (**[DỰ ĐOÁN]**, độ tin cậy thấp).

**Kế hoạch marketing không lộ mặt**

| Trụ nội dung | Hình thức | Tần suất | Mục đích |
|---|---|---|---|
| Nhật ký hành trình HaiBrain (`journey/` bản chia sẻ được) | Bài viết kèm ảnh chụp màn hình | 1–2 bài/tuần | Lòng tin, câu chuyện |
| Hướng dẫn 2–5 phút theo nghề | Quay màn hình, lồng giọng clone, có ghi rõ "giọng AI của tác giả" | 2 video/tuần | Thu hút người mới, tìm kiếm lâu dài |
| Trước/sau của học viên thật (bắt đầu từ vợ Chủ, có đồng ý) | Ảnh, số liệu, trích lời | Sau mỗi lớp | Bằng chứng xã hội |
| Zoom miễn phí | Chia sẻ màn hình | 2 tuần/lần | Chuyển đổi |

Kênh:
- Ưu tiên cộng đồng 5.000 người. **Chưa biết cộng đồng ở kênh nào; câu 4 của Chủ chưa trả lời.**
- Kênh phụ dài hạn: kênh video không lộ mặt; nhóm Zalo hoặc Telegram cho người đăng ký.
- **[GIẢ ĐỊNH]** Khách 30–50 tuổi ở Việt Nam dùng Zalo nhiều hơn Telegram. Kênh cộng đồng cho khách nên chọn theo nơi họ đang có mặt, tách khỏi quyết định "Telegram trước" dành cho bot của Chủ.

Cách kiểm chứng rẻ:
- Trang đăng ký đơn giản kèm form đặt cọc. Không xây web, không xây bot cho khách.
- Đo phễu ở mỗi buổi: người thấy thông báo → đăng ký → tham dự → trả tiền.

### Câu 4. Ý tưởng "nhóm founder 20–100 người bán hưởng hoa hồng"

**Lợi ích** **[SUY LUẬN]**
- Có thêm người bán mà không tốn chi phí cố định.
- Lời giới thiệu từ người quen có sức thuyết phục cao.
- Tạo cảm giác cùng sở hữu, hợp với tầm nhìn cộng đồng 1 triệu người.

**Rủi ro**
1. **Hình ảnh** **[SUY LUẬN]**: khách mục tiêu quen mô hình Amway. Combo "founder", "hoa hồng", "1 triệu người" rất dễ bị nhìn như một hệ thống đa cấp. Như vậy sẽ làm mất uy tín "người chia sẻ kiến thức đáng tin", là lợi thế lớn nhất của Chủ.
2. **Pháp lý** (**ngoài phạm vi, cần luật sư**, tôi không kết luận về luật):
   - **[SỰ THẬT]** Hoạt động kinh doanh theo phương thức đa cấp tại Việt Nam được quản lý bằng nghị định riêng: Nghị định 40/2018/NĐ-CP, sửa đổi bởi Nghị định 18/2023/NĐ-CP và Nghị định 55/2024/NĐ-CP. Bộ Công Thương đang đề xuất gộp và siết thêm, ví dụ đề xuất nâng mức ký quỹ ([LSVN](https://lsvn.vn/de-xuat-tang-muc-ky-quy-cua-doanh-nghiep-da-cap-len-50-ti-dong-a160171.html), [LuatVietnam](https://luatvietnam.vn/thuong-mai/nghi-dinh-18-2023-nd-cp-sua-nghi-dinh-40-kinh-doanh-da-cap-251170-d1.html), [Caselaw: NĐ 40/2018](https://caselaw.vn/van-ban-phap-luat/302045-nghi-dinh-40-2018-nd-cp-ve-quan-ly-hoat-dong-kinh-doanh-theo-phuong-thuc-da-cap), [Tạp chí Công Thương](https://tapchicongthuong.vn/bai-viet/chinh-phu-ban-hanh-mot-so-quy-dinh-moi-ve-hoat-dong-ban-hang-da-cap-104685.htm)). Có văn bản hợp nhất năm 2026 ([22/2026/VBHN-BCT](https://vbpl.moj.gov.vn/TW/Lists/vbpq/Attachments/187676/22.2026.VBHN-BCT.doc)) mà tôi chưa đọc được nội dung.
   - **[SUY LUẬN, cần luật sư xác nhận]** Mô hình trả hoa hồng theo nhiều tầng (hưởng trên doanh số của người mình tuyển) có nguy cơ rơi vào phạm vi điều chỉnh của các quy định trên, kèm điều kiện đăng ký và ký quỹ mà một người kinh doanh không đáp ứng được.
3. **Động cơ lệch** **[SUY LUẬN]**: founder tập trung bán thay vì học và dùng thật. Họ có thể hứa quá mức ("AI làm giàu"), dẫn đến khiếu nại và hoàn tiền.
4. **Kiểm soát chất lượng**: 20–100 người nói thay thương hiệu, trong khi chưa có tài liệu chuẩn.
5. **Thuế và chứng từ chi hoa hồng**: ngoài phạm vi, chuyển CEO.

**Phương án an toàn hơn** (vẫn cần luật sư duyệt trước khi mở):

| Phương án | Cách làm | Ghi chú |
|---|---|---|
| **A. Giới thiệu một tầng** | Mỗi người có mã giới thiệu, hưởng 20–30% trên đơn **do chính mình trực tiếp giới thiệu**. Không hưởng gì từ người mình tuyển. Không phí gia nhập, không bắt mua để được giới thiệu, không có cấp bậc | Đơn giản, minh bạch, gần với mô hình affiliate phổ biến |
| **B. Trợ giảng / Đại sứ được trả công** | Học viên xuất sắc (đã đạt Cấp 2) được đào tạo để hỗ trợ lớp hoặc làm coaching Cấp 1, được trả theo giờ hoặc theo học viên | Đây là trả công dịch vụ, không phải hoa hồng chuỗi. Đồng thời giải bài toán thời gian của Chủ (câu 5) |
| **C. Nhóm founder không hoa hồng** | 20–100 người đầu tiên được giá founding trọn đời, tên trong "sổ founder", quyền góp ý sản phẩm | Giữ cảm giác sở hữu mà không có rủi ro hoa hồng |

**Khuyến nghị:** kết hợp C ngay từ lớp 1, thêm A khi có ≥ 30 học viên hài lòng, thêm B từ tháng 4–6. **Tránh hẳn chữ "hoa hồng" và "tuyến dưới"** trong truyền thông.

### Câu 5. Tính ngược kinh tế đơn vị cho mục tiêu 50 triệu/tháng

**[SỰ THẬT]**
- Chạm Station đạt trung bình khoảng 23,5 triệu/tháng trong quý 3/2026 (70,4 triệu / 3), dù đã có thương hiệu.
- Chi phí AI của họ khoảng 17% doanh thu, giấy tờ và kế toán khoảng 17%.

**Điểm cần làm rõ:** 50 triệu là **doanh thu** hay **thu nhập ròng**? Nếu là ròng và cơ cấu chi phí giống Chạm (khoảng 34%), cần doanh thu khoảng **75 triệu/tháng**.

**Các cách đạt 50 triệu doanh thu/tháng** (giá theo bậc thang ở câu 2, **[GIẢ ĐỊNH]**):

| Kịch bản | Thành phần | Giờ của Chủ/tháng (ước tính) |
|---|---|---|
| Chỉ thành viên (250 nghìn) | ~200 thành viên duy trì | ~6 giờ, nhưng cần thư viện lớn và lượng người mới đều |
| Chỉ khóa nhóm (2 triệu) | 25 học viên/tháng | ~30 giờ |
| Chỉ coaching 1:1 (12 triệu) | ~4–5 khách/tháng | ~40–50 giờ; bị giới hạn bởi thời gian, ngược tầm nhìn 6 tháng/năm |
| **Kết hợp (đề xuất)** | 80 thành viên (20 triệu) + 10 học viên khóa (20 triệu) + 1 coaching (10 triệu) | ~30–35 giờ |

**Phễu cần có cho kịch bản kết hợp** (tỷ lệ là **[GIẢ ĐỊNH]**):
- 10 học viên khóa mỗi tháng, chuyển đổi 5% → khoảng 200 người dự Zoom/tháng → khoảng 500 người đăng ký/tháng.
- Thành viên rời đi giả định 10%/tháng → cần khoảng 8 thành viên mới mỗi tháng chỉ để giữ mức 80.
- **[SUY LUẬN]** Với 5.000 người, sau 2–3 đợt Zoom phần lớn người quan tâm đã được tiếp cận, đúng bài học "đợt đầu rồi cạn" của Chạm. Muốn duy trì 500 người đăng ký mỗi tháng thì phải có nguồn người mới: nội dung tìm kiếm, giới thiệu một tầng, trợ giảng mang học viên về.

**[DỰ ĐOÁN, độ tin cậy thấp]**
- Tháng 6 (khoảng 4/2027): 10–25 triệu/tháng.
- 50 triệu/tháng đều đặn: có thể đạt trong 12–18 tháng, nếu (1) lớp founding đạt mốc ở giai đoạn B và C, và (2) kênh người mới chạy được.

**"Làm 6 tháng/năm, tài sản tăng 100%/năm"**
- **[SUY LUẬN]** Chỉ đạt được khi doanh thu tách khỏi giờ của Chủ. Coaching 1:1 do Chủ làm phải là bậc cao cấp, giới hạn số suất, dần chuyển cho trợ giảng.
- Phải xây từ nền tảng:
  1. Khóa tự học: ghi từ các lớp trực tiếp, không quay riêng.
  2. Thư viện mẫu theo nghề.
  3. Cộng đồng có người hỗ trợ người.
  4. Đội trợ giảng hoặc đại sứ.
  5. Lịch lớp gom vào các "tháng làm việc".
- Cần định nghĩa "tài sản kinh doanh" bằng chỉ số đo được, đề xuất ba chỉ số:
  - doanh thu định kỳ hằng tháng (MRR);
  - số người trong danh sách liên hệ do HaiBrain sở hữu;
  - số học viên đạt kết quả Cấp 1 lũy kế.

**"1 triệu người"**
- **[SUY LUẬN]** Đây là chỉ số tầm ảnh hưởng (số người được tiếp cận hoặc tự thiết lập được), không phải số khách trả tiền. Chỉ đạt được bằng nội dung miễn phí, khóa tự học giá rẻ và cộng đồng tự lan tỏa.
- Nên đặt làm "sao Bắc Đẩu" 5–10 năm. Mốc 12 tháng nên là khoảng 1.000 người đạt Cấp 1 (**[GIẢ ĐỊNH]**, cần Chủ chốt).

### Câu 6. Độ la bàn: chỗ lệch và mâu thuẫn

| # | Chỗ lệch | Mức độ | Đề xuất xử lý |
|---|---|---|---|
| 1 | Lộ trình kỹ thuật đặt "khuôn mẫu hóa cho coaching" sau giai đoạn 6+, nhưng mốc khách trả tiền là tháng 2/2027 | **Cao** | Tách hai luồng: luồng sản phẩm bán (Cấp 1–2, dựng từ giai đoạn 1 hiện tại) và luồng phòng thí nghiệm (bot, công ty bot). Tạm hoãn công ty bot đến khi có doanh thu |
| 2 | "Tự xây bộ não kỹ thuật cao" khác với "bán cho người không biết code" | **Cao** | Hệ thống của Chủ là bằng chứng và nội dung ("xem tôi làm"). Thứ bán cho đa số là Cấp 1 |
| 3 | 30 giờ/tuần so với khối lượng việc. Ước tính: xây kỹ thuật 10–15 giờ, nội dung và marketing 8–10 giờ, khách và cộng đồng 5–10 giờ, tổng 23–35+ giờ. Chưa rõ 30 giờ đã tính công việc IT ở EWIT chưa | **Trung bình–cao** | Trong 90 ngày tới, giới hạn kỹ thuật ≤ 10 giờ/tuần; ưu tiên phỏng vấn, Zoom, bán |
| 4 | Kế hoạch "tháng 1 học xong, tháng 2–3 làm sản phẩm" đi ngược nguyên tắc "bán trước, xây sau" | Trung bình | Bán trước ngay trong lúc học; lớp founding là nơi vừa dạy vừa hoàn thiện |
| 5 | Bài kiểm tra đầu ra đo cấu trúc thư mục (đầu vào), trái với nguyên tắc "chỉ tin kết quả thật" | Trung bình | Thêm tiêu chí hành vi: tìm lại thông tin dưới 1 phút, AI trả lời đúng có nguồn, còn dùng sau 30 ngày |
| 6 | "Nhóm founder hưởng hoa hồng" mâu thuẫn với lợi thế "được tin vì chia sẻ kiến thức" | **Cao** | Xem câu 4 |
| 7 | Mốc tháng 2/2027 trùng Tết | Trung bình | Bán trong tháng 12, giao hàng trong tháng 1 |
| 8 | Không lộ mặt + giọng clone khác với việc bán coaching dựa trên lòng tin cho người lạ | Thấp–trung bình | Trong cộng đồng sẵn có thì ổn. Với người lạ, bù bằng lời chứng thực thật. Nên công khai việc dùng giọng AI |
| 9 | Bằng chứng sẵn sàng trả tiền mới đến từ người nhà (vợ Chủ) | Trung bình | Bằng chứng thật là người lạ đặt cọc (giai đoạn B) |
| 10 | Decision "Telegram trước" phù hợp cho bot của Chủ, nhưng khách có thể quen Zalo | Thấp | Chọn kênh cộng đồng cho khách theo khảo sát |

---

## Đề xuất

1. **Đổi cấu trúc sản phẩm thành 3 cấp.** Bán Cấp 1 trước, Cấp 2 kèm theo, Cấp 3 để sau.
   - **Cái giá phải trả:** sản phẩm bán đầu tiên "kém kỹ thuật" hơn điều Chủ đang hứng thú xây; lộ trình công ty bot chậm lại.
   - **Cách kiểm chứng:** vợ Chủ và 3–5 người thật làm thử Cấp 1 trong tháng 11, đo theo 5 tiêu chí.
2. **Tách hai luồng công việc:** sản phẩm bán (ưu tiên trong 90 ngày) và phòng thí nghiệm kỹ thuật (≤ 10 giờ/tuần).
3. **Chạy kế hoạch 90 ngày A → B → C:** phỏng vấn, 2 buổi Zoom, bán trước lớp founding, lớp chạy trước Tết. Có ngưỡng dừng rõ: dưới 5 người trả tiền thì xem lại trước khi xây thêm.
4. **Thay "founder hưởng hoa hồng" bằng nhóm founder không hoa hồng**, sau đó thêm giới thiệu một tầng và trợ giảng được trả công. Hỏi luật sư trước khi chi bất kỳ khoản hoa hồng nào.
5. **Định nghĩa lại các mục tiêu thành chỉ số đo được:**
   - 50 triệu là doanh thu hay thu nhập ròng;
   - "tài sản" đo bằng MRR, danh sách liên hệ và số học viên đạt Cấp 1;
   - "1 triệu người" là sao Bắc Đẩu dài hạn; mốc 12 tháng là khoảng 1.000 người đạt Cấp 1.

---

## Rủi ro và giả định

**Rủi ro lớn nhất** **[SUY LUẬN]**: Chủ dồn thời gian vào xây hệ thống kỹ thuật (thứ thú vị và quen tay) và trì hoãn việc bán. Đến tháng 2/2027 có hệ thống đẹp nhưng chưa có người lạ nào trả tiền.

**Giả định dễ sai nhất:**
1. **"5.000 người tin Chủ về AI" sẽ chuyển thành người mua.** Chưa biết kênh, mức tương tác, nghề nghiệp của họ, và Chủ có được phép bán trong cộng đồng đó không.
2. **Người 30–50 tuổi bận rộn sẽ duy trì thói quen ghi chép sau khóa học.** Bộ não thứ 2 là sản phẩm cần thói quen; rủi ro "cài xong rồi bỏ" cao. Vì vậy cần tiêu chí "còn dùng sau 30 ngày".
3. **Các tỷ lệ phễu** (40% tham dự, 5% mua, 10% thành viên rời đi mỗi tháng) là giả định, chưa có dữ liệu Việt Nam để đối chiếu. Đo ngay ở buổi Zoom #1.
4. **Mức giá 1,5–2,5 triệu:** chưa có dữ liệu giá đối thủ đã kiểm chứng (không truy cập được weopc.vn và cham.media hôm nay).

**Phản biện chính mình:**
- Có thể tôi đánh giá thấp mong muốn "có bot riêng" của khách. Bot Telegram ghi tin thoại có thể chính là yếu tố "wow" để bán. Cách kiểm: ở Zoom #1, demo cả Cấp 1 và bot của Chủ, rồi hỏi người tham dự chọn cấp nào.
- Cấp 1 dựa vào công cụ của bên thứ ba (Google, Anthropic, OpenAI). Họ có thể đổi tính năng hoặc giá bất kỳ lúc nào, làm khóa học lỗi thời. Giảm rủi ro bằng cách dạy **phương pháp** (cấu trúc, thói quen, cách hỏi AI) nhiều hơn dạy công cụ.
- Bài học của Chạm Station là một trường hợp, không phải quy luật thị trường.

**Ngoài phạm vi, chuyển CEO:** pháp lý đa cấp và giới thiệu hưởng hoa hồng; bảo vệ dữ liệu cá nhân (dữ liệu sức khỏe khách hàng); thuế và chứng từ cho doanh thu khóa học và tiền hoa hồng; quy định về nội dung dùng giọng AI.

---

## Câu hỏi cần Chủ trả lời

1. **Cộng đồng 5.000 người** ở kênh nào (Facebook, Zalo, Telegram, nhóm Amway...)? Họ chủ yếu làm nghề gì? Chủ có được phép mở Zoom và bán khóa trong cộng đồng đó không?
2. **50 triệu/tháng** là doanh thu hay thu nhập ròng? **30 giờ/tuần** là ngoài công việc IT ở EWIT, hay đã tính chung?
3. Chủ có **đồng ý sản phẩm bán đầu tiên là Cấp 1–2 (không code)**, và tạm hoãn công ty bot đến khi có doanh thu không?
4. Chủ có **đồng ý thay "founder hưởng hoa hồng" bằng nhóm founder không hoa hồng, sau đó giới thiệu một tầng và trợ giảng**, và chi một khoản để hỏi luật sư trước khi mở không?
5. Chủ có **đồng ý dời mốc bán lên tháng 12/2026** (bán trước lớp founding, chạy lớp trước Tết)? Zoom chỉ chia sẻ màn hình và giọng thật, không camera, có chấp nhận được không?

---

## Nguồn

- Tài liệu nội bộ: `docs/00-tong-quan.md`, `docs/kinh-doanh/00-y-tuong-kinh-doanh.md`, `docs/kinh-doanh/01-tra-loi-cua-chu.md`; số liệu Chạm Station do CEO cung cấp từ phiên trước.
- [LSVN: Đề xuất tăng mức ký quỹ doanh nghiệp đa cấp](https://lsvn.vn/de-xuat-tang-muc-ky-quy-cua-doanh-nghiep-da-cap-len-50-ti-dong-a160171.html)
- [LuatVietnam: Nghị định 18/2023/NĐ-CP](https://luatvietnam.vn/thuong-mai/nghi-dinh-18-2023-nd-cp-sua-nghi-dinh-40-kinh-doanh-da-cap-251170-d1.html)
- [Caselaw: Nghị định 40/2018/NĐ-CP](https://caselaw.vn/van-ban-phap-luat/302045-nghi-dinh-40-2018-nd-cp-ve-quan-ly-hoat-dong-kinh-doanh-theo-phuong-thuc-da-cap)
- [Tạp chí Công Thương: quy định mới về bán hàng đa cấp](https://tapchicongthuong.vn/bai-viet/chinh-phu-ban-hanh-mot-so-quy-dinh-moi-ve-hoat-dong-ban-hang-da-cap-104685.htm)
- [Văn bản hợp nhất 22/2026/VBHN-BCT](https://vbpl.moj.gov.vn/TW/Lists/vbpq/Attachments/187676/22.2026.VBHN-BCT.doc)
