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

## Phần sau của phiên: chiến lược HaiBrain
- Claude nhận vai trò CEO; tạo subagent `chien-luoc-opc-coaching`.
- Chủ trả lời 10 câu hỏi (trang chữ to: https://claude.ai/artifact/6drev5EzBfBHhLwMrg9612). Thương hiệu **HaiBrain**, tầm nhìn 1 triệu người; khách đầu tiên là vợ Chủ; cộng đồng Mentor Master khoảng 5.000 người; mục tiêu 50 triệu/tháng thu nhập ròng; mốc khách trả tiền tháng 2/2027.
- Báo cáo chiến lược đầu tiên: đề xuất đổi sang sản phẩm 3 cấp (Cấp 1 không code), bỏ hoa hồng nhiều tầng, bán trước tháng 12, kỹ thuật tối đa 10 giờ/tuần. **Chờ Chủ quyết.**
- Phát hiện nguyên nhân mất bối cảnh giữa các thiết bị: phiên cloud làm trên nhánh riêng, chưa gộp vào `main`. Giải pháp "một nhà, ba cửa"; thêm bước gộp vào `main` vào nghi thức kết thúc phiên.
- Lưu ý: không dùng danh sách học viên Mentor Master cho việc riêng khi chưa được phép; thay bằng đề xuất hợp tác và thí điểm chính danh.
- Đề xuất thí điểm "Bộ não thứ 2 cho EWIT": subagent soạn, CEO phản biện và sửa 6 điểm. Cập nhật theo câu trả lời của Chủ: phụng sự kèm hỗ trợ chi phí công cụ; hệ sinh thái Google (Workspace, Gemini, NotebookLM); IT EWIT khoảng 10 giờ/tuần.

## Hướng dẫn cài đặt trên Windows (tóm tắt)
1. Cài Git for Windows (git-scm.com), giữ lựa chọn mặc định.
2. Cài GitHub Desktop, đăng nhập `tnho113`.
3. File → Clone repository → `tnho113/webforAgent` → lưu vào `C:\Users\<tên>\Documents\webforAgent` (không đặt trong ổ Google Drive).
4. (Bỏ qua: đã gộp vào `main`.)
5. Cài Claude Code: PowerShell → `irm https://claude.ai/install.ps1 | iex`, mở lại PowerShell.
6. `cd $HOME\Documents\webforAgent` rồi `claude`, đăng nhập tài khoản Pro, thử "Đọc now.md và tóm tắt".
7. (Tùy chọn) Obsidian → Open folder as vault.

## Ghi chú môi trường
- Môi trường cloud chặn một số tên miền (hq.weopc.vn, weopc.vn, cham.media). Muốn đọc trực tiếp thì thêm vào Allowed domains, hoặc dán nội dung dưới dạng file.
