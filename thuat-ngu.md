# Thuật ngữ (thuật ngữ | ví dụ đời thường | nghĩa kỹ thuật | ngày ghi)
| Blockchain | Một cuốn sổ cái chung, nhiều người cùng giữ bản sao, ghi rồi không ai tự ý tẩy xóa được | Cơ sở dữ liệu phân tán; các giao dịch được gom thành khối, nối nhau bằng mã hóa và được nhiều nút (node) xác nhận | 2026-10-15 |
| Stablecoin | "Phiếu đổi tiền" 1 phiếu = 1 USD, có thể đổi lại tiền thật ở nhà phát hành | Token trên blockchain giữ giá ổn định so với một đồng tiền pháp định (thường USD), được bảo chứng bằng tiền mặt/trái phiếu ngắn hạn; ví dụ USDC, USDT | 2026-10-15 |
| Nhà phát hành (issuer) | Ngân hàng in phiếu và giữ tiền thật trong két | Công ty tạo và mua lại stablecoin, giữ tài sản dự trữ (ví dụ Circle với USDC, Tether với USDT) | 2026-10-15 |
| Layer 1 (L1) | Con đường chính, không phải làn phụ xây đè lên đường khác | Blockchain nền tảng tự vận hành và tự xác nhận giao dịch (ví dụ Ethereum, Solana, Tempo) | 2026-10-15 |
| Ví (wallet) | Hộp thư có địa chỉ công khai để nhận tiền, và chìa khóa riêng để mở hộp | Phần mềm/thiết bị quản lý khóa; địa chỉ ví công khai, khóa bí mật dùng để ký giao dịch | 2026-10-15 |
| Khóa bí mật / cụm từ khôi phục (private key / seed phrase) | Chìa khóa két: ai cầm là người đó lấy được tiền | Chuỗi bí mật dùng để ký giao dịch; lộ là mất quyền kiểm soát ví. Không bao giờ chia sẻ hay lưu vào file | 2026-10-15 |
| Phí gas | Phí cầu đường trả cho người duy trì con đường | Phí trả cho mạng lưới để xử lý giao dịch; nhiều chain thu bằng token riêng, Tempo thu bằng stablecoin | 2026-10-15 |
| Mainnet / Testnet | Đường thật có xe thật / sân tập lái | Mạng chính dùng tiền thật / mạng thử dùng tiền giả để thử nghiệm | 2026-10-15 |
| Validator | Người kiểm phiếu, cùng ký xác nhận mỗi trang sổ | Nút mạng xác nhận giao dịch và tạo khối; "permissioned" nghĩa là chỉ đơn vị được duyệt mới làm validator | 2026-10-15 |
| Finality (tính chung cuộc) | Lúc tiền đã "vào két" người nhận, không rút lại được | Thời điểm giao dịch được xác nhận không thể đảo ngược | 2026-10-15 |
| Chargeback (hoàn tiền bắt buộc) | Khiếu nại với ngân hàng để đòi lại tiền đã quẹt thẻ | Cơ chế của mạng thẻ cho phép chủ thẻ tranh chấp và đảo ngược giao dịch; stablecoin không có cơ chế mặc định này | 2026-10-15 |
| AI agent | Trợ lý ảo được giao việc và tự làm nhiều bước, không cần hỏi từng bước | Chương trình dùng mô hình AI để tự lập kế hoạch, gọi công cụ/API và hành động thay người dùng | 2026-10-15 |
| HTTP 402 "Payment Required" | Cửa hàng tự động báo "trả tiền trước rồi mới lấy hàng" | Mã trạng thái HTTP dành cho yêu cầu cần thanh toán; được x402 và MPP dùng để agent trả tiền ngay trong yêu cầu web | 2026-10-15 |
| x402 | Máy bán hàng tự động trên internet nhận stablecoin | Giao thức mở do Coinbase khởi xướng (05/2025), thanh toán stablecoin qua mã HTTP 402 | 2026-10-15 |
| MPP (Machine Payments Protocol) | Quầy thu ngân chung cho máy, nhận nhiều loại tiền | Chuẩn mở của Stripe và Tempo (03/2026) cho thanh toán máy-với-máy qua HTTP; hỗ trợ stablecoin trên Tempo, thẻ qua Stripe, Lightning | 2026-10-15 |
