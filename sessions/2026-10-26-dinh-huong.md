# Phiên 2026-10-26: Định hướng tổng thể

## Đã làm
- Phân tích ý tưởng "mỗi bot là một nhân viên" (Peter Yang) và mô hình OPC HQ / weOPC.vn.
- Thiết kế ý tưởng công ty bot trên Telegram: CEO, nhân viên, QA; chat riêng giao việc gấp; độ la bàn cho bot.
- Thống nhất xây bot bộ não thứ 2 trước.
- Chốt mô hình lưu trữ kết hợp (Drive cho kho thô, GitHub cho bộ não) và cơ chế bàn giao phiên.
- Phân tích bài "6 tỷ và 70 triệu" (CHẠM.media), rút 5 điểm bổ sung vào đặc tả.
- Rà soát mâu thuẫn: tách 2 repo; chép lời tin thoại để Giai đoạn 2 thử nghiệm; thêm người gác cổng GitHub Actions; làm rõ 3 tầng và thang tự chủ, `sessions/` và `journey/`, bài học dạng nháp, nơi có bối cảnh xuyên suốt.

## Quyết định
Xem mục 4 trong [`docs/00-tong-quan.md`](../docs/00-tong-quan.md). Thêm trong phiên này:
- `webforAgent` giữ vai trò học tập, nghiên cứu, đặc tả. Repo hệ thống tạo riêng khi bắt đầu làm sản phẩm.

## Còn dở
- Chủ chưa xác nhận bắt đầu viết đặc tả chi tiết.
- Các câu hỏi mở ở mục 5 của tổng quan.

## Ghi chú môi trường
- Môi trường cloud chặn một số tên miền (hq.weopc.vn, weopc.vn, cham.media). Muốn đọc trực tiếp thì thêm vào Allowed domains, hoặc dán nội dung dưới dạng file.
