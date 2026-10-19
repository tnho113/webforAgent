---
name: fb-live-to-notes
description: Chuyển một video/livestream Facebook (hoặc bản chép lời của nó) thành tài liệu tổng hợp học tập bằng tiếng Việt, lưu vào Google Drive; buổi thuộc chuỗi CEO Talk Vinhomes Green Paradise Cần Giờ được thêm thành tab mới trong file chung. Dùng khi người dùng gửi link video Facebook, link facebook.com/watch, fb.watch, hoặc link Google Doc chứa bản chép lời và muốn có bản tổng hợp, ghi chú học tập, tóm tắt nội dung buổi live.
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

Nội dung gồm các phần sau, theo đúng thứ tự:

1. **Thông tin chung**: tên sự kiện, chủ đề, người dẫn, diễn giả và vai trò, bản chất buổi nói chuyện (đào tạo, bán hàng, chia sẻ...).
2. **Tóm tắt trong một đoạn**: 5–7 câu.
3. **Điểm cần lưu ý** (tiêu đề không đánh số, đặt ngay sau tóm tắt): 4–7 gạch đầu dòng về số liệu sai hoặc mâu thuẫn, con số là dự đoán/mục tiêu, ví dụ thiếu ngữ cảnh, phát biểu không có căn cứ không nên dùng khi tư vấn, và lưu ý chung về độ tin cậy của bản chép lời.
4. **Các ý chính theo chủ đề**: chia mục nhỏ, gạch đầu dòng, giữ ví dụ và lập luận của diễn giả.
5. **Số liệu được nêu**: bảng gồm Nội dung, Số liệu, Ghi chú kiểm tra. Ghi rõ đây là phát biểu, chưa kiểm chứng. Tự kiểm tra phép tính, nếu sai thì ghi chú.
6. **Bài học áp dụng**: kỹ năng, cách làm có thể dùng ngay (người dùng làm tư vấn bán hàng).
7. **Góc nhìn phản biện**: lợi ích của người nói, thiên lệch, điều chưa được nói tới.
8. **Câu hỏi tự kiểm tra**: 5–7 câu.

Đánh số tiêu đề các phần chính là 1, 2, 3... trừ "Điểm cần lưu ý". Dòng đầu (chữ nghiêng) ghi nguồn và ngày biên tập. Nếu buổi này nói khác buổi trước cùng chuỗi (ngày, số liệu), ghi vào "Điểm cần lưu ý".

### Lưu vào đâu

**Chuỗi "CEO Talk Vinhomes Green Paradise Cần Giờ"**: thêm một tab mới vào file chung [Ghi chú học tập - CEO Talk Vinhomes Green Paradise Cần Giờ](https://docs.google.com/document/d/1b3egOqmOY2SrFaZNSiDYY9yhhyQlFo1QQGWj3NLA_7k/edit) (ID `1b3egOqmOY2SrFaZNSiDYY9yhhyQlFo1QQGWj3NLA_7k`), tên tab là tên buổi, không tạo file riêng. Cần connector Google Docs; nếu chưa bật thì dừng và nhờ người dùng bật. Trước khi sửa, đọc `references/docs.md` của skill google-workspace.

1. Viết nội dung ra file Markdown trong scratchpad theo cú pháp mà `scripts/md_to_tab.py` hỗ trợ (xem đầu file script). Đặt bảng số liệu ngay sau dòng ghi chú của phần số liệu.
2. `update_doc` với `addDocumentTab` (`tabProperties.title` = tên buổi, `index` = số tab hiện có) và lấy `tabId` trong phản hồi.
3. `read_doc` để lấy `revisionId` mới (kết quả lớn được lưu ra file; dùng `jq '.content'` rồi `jq -r .revisionId`, không đọc vào ngữ cảnh).
4. `python3 scripts/md_to_tab.py notes.md --tab <tabId> --revision <rev> --out req.json`, rồi gửi `requests` và `writeControl` trong `req.json` bằng một lần `update_doc`.
5. Nếu có bảng: `read_doc` lại, chạy `docs_index.py outline` (skill google-workspace) để tìm đoạn đứng trước bảng, rồi `docs_index.py new-table --at <endIndex - 1> --data rows.json --revision <rev> --tab <tabId> --bold-header` và gửi kết quả. Sau đó `read_doc` lại và trong một lần `update_doc`: xóa đoạn trống ngay sau bảng nếu tiếp theo là tiêu đề, và đặt `italic: false` cho phạm vi bảng (chữ trong bảng bị kế thừa nghiêng từ dòng ghi chú).

Giới hạn đã biết: danh sách đánh số lồng trong danh sách gạch đầu dòng sẽ hiển thị bằng dấu tròn.

**Buổi khác (không thuộc chuỗi trên)**: tạo Google Doc mới bằng Google Drive `create_file` với `contentMimeType: text/html` và `parentId` là thư mục ở trên. Tiêu đề: `Ghi chú học tập - <tên buổi/chủ đề>`.

## Bước 4: Kiểm tra và báo kết quả

- File mới: gọi `get_file_metadata` (snippetVerbosity: BRIEF) để xác nhận có nội dung.
- Tab mới: `read_doc`, chạy `docs_index.py outline` trên tab đó, kiểm tra thứ tự tiêu đề, gạch đầu dòng và bảng.
- Trả lời người dùng tối đa khoảng 8 dòng: link file (gắn vào tên file), tên tab nếu có, các phần chính, và những điểm cần lưu ý quan trọng nhất.
