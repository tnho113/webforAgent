---
name: fb-live-to-notes
description: Chuyển một video/livestream Facebook (hoặc bản chép lời của nó) thành tài liệu tổng hợp học tập bằng tiếng Việt, lưu vào Google Drive. Dùng khi người dùng gửi link video Facebook, link facebook.com/watch, fb.watch, hoặc link Google Doc chứa bản chép lời và muốn có bản tổng hợp, ghi chú học tập, tóm tắt nội dung buổi live.
---

# Video Facebook → Bản tổng hợp học tập

Đầu vào: một link video Facebook, HOẶC một link Google Doc/file chứa bản chép lời.
Đầu ra: một Google Doc "Ghi chú học tập - <tên buổi>" trong thư mục Drive "Tài liệu học tập", và một tin nhắn ngắn kèm link.

## Quy tắc chung

- Trả lời bằng tiếng Việt, ngắn gọn. Không dùng icon, emoji, ký hiệu trang trí.
- Dùng "biết ơn" thay cho "cảm ơn". Sai thì sửa, không xin lỗi.
- Phân biệt rõ sự thật, phát biểu của diễn giả, suy luận và dự đoán. Không bịa nội dung không có trong bản chép lời.
- Thư mục lưu mặc định: "Tài liệu học tập", Drive folder ID `1uHC1aj8Fh34uqFx7YYGkWQQLSkX09hZJ` (nằm trong "Trợ lý làm việc hiệu quả", ID `1o7RLnn1x3elWHzHtDE_JkdtILrui34TT`). Nội dung về Amway lưu vào thư mục "Amway", ID `10zJ0Ar0Qu8Ta-pK8iJe3ApNkiU1v2TLS`.
- Chỉ xử lý video công khai. Không đăng lại nội dung, chỉ dùng để học cá nhân.

## Bước 1: Lấy bản chép lời

Nếu đầu vào là link Google Doc: lấy file ID trong link, gọi Google Drive `read_file_content` (includeComments: true). Sang bước 2.

Nếu đầu vào là link Facebook, thử tự động (chạy trong scratchpad, không chạy trong repo):

```bash
pip install -q yt-dlp faster-whisper   # cần ffmpeg; nếu thiếu: apt-get install -y ffmpeg
yt-dlp -f "worstaudio/worst" -x --audio-format mp3 --audio-quality 64K -o "audio.%(ext)s" "<LINK>"
python3 - <<'EOF'
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
segs, _ = m.transcribe("audio.mp3", language="vi", vad_filter=True)
open("transcript.txt", "w").write("\n".join(s.text.strip() for s in segs))
EOF
```

- Video dài hơn khoảng 1 giờ, model "small" trên CPU có thể chạy lâu: chạy nền và báo người dùng thời gian ước tính.
- Nếu bất kỳ bước nào bị chặn (mạng không vào được Facebook, yêu cầu đăng nhập, không cài được gói, bị từ chối quyền): DỪNG, không tìm cách vượt qua, và gửi người dùng đúng hướng dẫn thủ công dưới đây.

Hướng dẫn thủ công (gửi nguyên văn cho người dùng):

1. Dán link Facebook vào https://en1.savefrom.net/19wr/ và tải bản nhẹ nhất (ưu tiên bản chỉ có âm thanh nếu có).
2. Nếu là video, vào https://www.freeconvert.com, chọn công cụ chuyển Video sang MP3 (bitrate 64 kbps). File MP3 phải dưới 200MB.
3. Tải file MP3 lên NotebookLM, mở nguồn vừa tải và copy toàn bộ bản chép lời.
4. Dán vào một Google Doc trong thư mục "Tài liệu học tập", rồi gửi link Doc cho trợ lý. Nếu biết, ghi thêm tên diễn giả đúng chính tả ở đầu Doc.

## Bước 2: Đọc bản chép lời tiết kiệm token

- Kết quả lớn bị lưu ra file: dùng `jq -r '.fileContent'` xuất ra scratchpad, kiểm tra độ dài bằng `wc -c`, rồi đọc theo từng đoạn khoảng 30.000 ký tự (`tail -c +N | head -c 30000`). Đọc hết, không đoán phần chưa đọc.
- Ghi lại trong lúc đọc: diễn giả và vai trò, các ý chính theo chủ đề, mọi con số kèm ngữ cảnh, câu nói đáng nhớ, ví dụ minh họa.
- Bản chép lời tự động hay sai tên riêng và số. Chỉ sửa khi chắc chắn; chỗ không chắc thì ghi "theo bản chép lời, cần đối chiếu".

## Bước 3: Viết bản tổng hợp

Tạo Google Doc bằng Google Drive `create_file` với `contentMimeType: text/html` và `parentId` là thư mục ở trên. Tiêu đề: `Ghi chú học tập - <tên buổi/chủ đề>`. Cấu trúc:

1. **Thông tin chung**: tên sự kiện, chủ đề, người dẫn, diễn giả và vai trò, bản chất buổi nói chuyện (đào tạo, bán hàng, chia sẻ...).
2. **Tóm tắt trong một đoạn**: 5–7 câu.
3. **Các ý chính theo chủ đề**: chia mục nhỏ, gạch đầu dòng, giữ ví dụ và lập luận của diễn giả.
4. **Số liệu được nêu**: bảng gồm Nội dung, Số liệu, Ghi chú. Ghi rõ đây là phát biểu, chưa kiểm chứng. Tự kiểm tra phép tính, nếu sai thì ghi chú.
5. **Bài học áp dụng**: kỹ năng, cách làm có thể dùng ngay (người dùng làm tư vấn bán hàng).
6. **Góc nhìn phản biện**: lợi ích của người nói, thiên lệch, điều chưa được nói tới.
7. **Câu hỏi tự kiểm tra**: 5–7 câu.

Dòng đầu Doc ghi nguồn (link video hoặc tên file chép lời) và ngày biên tập.

## Bước 4: Kiểm tra và báo kết quả

- Gọi `get_file_metadata` (snippetVerbosity: BRIEF) để xác nhận Doc có nội dung.
- Trả lời người dùng tối đa khoảng 8 dòng: link Doc (gắn vào tên file), cấu trúc các phần, và những điểm không chắc chắn hoặc số liệu bị sai cần lưu ý.
