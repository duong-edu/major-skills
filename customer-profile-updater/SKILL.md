---
name: customer-profile-updater
description: "Cập nhật hồ sơ khách hàng (customer profile) cho hệ thống Trường Việt Anh theo khung Value Proposition Canvas (Jobs / Pains / Gains). LUÔN dùng skill này khi người dùng nói 'cập nhật hồ sơ khách hàng', 'update customer profile', 'cập nhật chân dung khách hàng', 'cập nhật insight khách hàng', 'cập nhật Pains Gains', 'cập nhật VPC', 'phân tích phụ huynh', 'quét mạng xã hội tìm pain points', 'scan social listening phụ huynh', hoặc bất kỳ yêu cầu nào liên quan đến việc tổng hợp Jobs/Pains/Gains của phụ huynh Việt Anh. Skill sẽ tự hỏi đầy đủ tham số đầu vào (cấp học, nguồn dữ liệu, phạm vi scan), đối chiếu với hồ sơ cũ, phân tích trọng số - xu hướng - trạng thái (mới/cũ/thay đổi), liệt kê giải pháp đối thủ, đề xuất giải pháp Việt Anh cần phát triển, và xuất ra file Word hoàn chỉnh kèm to-do list hành động."
---

# Customer Profile Updater — Trường Việt Anh

Skill này giúp anh Dương (Chủ tịch Trường Việt Anh) cập nhật hồ sơ khách hàng (phụ huynh mục tiêu) một cách hệ thống theo khung **Value Proposition Canvas** đã được dùng trong tổ chức.

## Nguyên tắc cốt lõi

1. **Giữ đúng khung 7 cột** của Việt Anh: Jobs / Pains / Gains / Gain Creators / Pain Relievers / Products & Services / Nguồn dữ liệu. Skill có thể mở rộng thêm cột (trọng số, trạng thái, xu hướng) nhưng KHÔNG thay đổi 7 cột gốc.
2. **Luôn đối chiếu với hồ sơ cũ** — không tạo hồ sơ từ số 0. Hồ sơ cũ hiện có 5 sheet: Mầm non, Tiểu học, THCS, THPT, Nội trú.
3. **Đánh dấu minh bạch** cái nào MỚI, cái nào CŨ, cái nào THAY ĐỔI — để anh Dương biết dữ liệu thay đổi ra sao theo thời gian.
4. **Nói thẳng hạn chế** — nếu scan internet không đủ dữ liệu, hoặc nếu không thể xử lý audio/video, nói rõ thay vì bịa.

---

## Quy trình 6 bước

### Bước 1: Thu thập tham số đầu vào (hỏi tất cả trong 1 lần)

Ngay khi skill được kích hoạt, dùng tool `ask_user_input_v0` để hỏi TẤT CẢ 4 câu hỏi sau trong MỘT lần gọi (anh Dương yêu cầu hỏi gộp, không hỏi từng câu):

```
Câu 1 — Cấp học cần cập nhật (multi_select):
  - Mầm non
  - Tiểu học
  - THCS
  - THPT
  - Nội trú
  - Tất cả

Câu 2 — Nguồn dữ liệu (multi_select):
  - Upload file
  - Scan internet
  - Cả hai

Câu 3 — Nếu scan internet, phạm vi scan (multi_select):
  - Mạng xã hội đối thủ (Facebook, TikTok, YouTube của các trường đối thủ)
  - Hội nhóm phụ huynh (Facebook Groups, Webtretho, LamChaMe)
  - Các KOL giáo dục cùng tệp (xem danh sách trong references/competitors.md)
  - Bài báo/blog giáo dục mới 6 tháng gần đây
  - Tất cả

Câu 4 — Có đối chiếu với hồ sơ cũ không (single_select):
  - Có (mặc định — anh Dương đã yêu cầu LUÔN đối chiếu)
  - Không (tạo hồ sơ từ số 0)
```

**Nếu người dùng chọn "Upload file"** ở Câu 2, hỏi thêm 1 câu phụ sau khi họ trả lời 4 câu trên (dùng `ask_user_input_v0` lần 2):

```
Câu 5 — File upload là loại gì (multi_select):
  - Excel/CSV (bảng dữ liệu có cấu trúc)
  - Word/Text (báo cáo, ghi chép)
  - Ảnh chụp (chat, post, screenshot)
  - Audio/Video (ghi âm phỏng vấn, họp)
  - Hỗn hợp
```

---

### Bước 2: Đọc và xử lý dữ liệu đầu vào

#### 2a. Đọc hồ sơ cũ (LUÔN LÀM nếu user chọn "Có đối chiếu")

- Hỏi người dùng đường dẫn file hồ sơ cũ (thường là file Excel có 5 sheet theo cấp học)
- Nếu người dùng không upload, báo: *"Em cần anh upload file hồ sơ khách hàng hiện tại để đối chiếu. Nếu không có, skill sẽ phải tạo từ số 0."*
- Dùng `extract-text` hoặc `pandas` đọc từng sheet tương ứng cấp học đã chọn
- Trích xuất 7 cột: Jobs, Pains, Gains, Gain Creators, Pain Relievers, Products & Services, + thông tin đối tượng (độ tuổi, thu nhập, địa chỉ) ở đầu sheet

#### 2b. Đọc file upload mới

- **Excel/CSV**: dùng `pandas` với `pd.read_excel()` hoặc `pd.read_csv()`
- **Word/Text**: dùng `python-docx` hoặc đọc trực tiếp text
- **Ảnh chụp**: Claude đọc ảnh trực tiếp từ context (vision)
- **Audio/Video**: Claude **KHÔNG** có speech-to-text tiếng Việt tích hợp. Phải báo:

> *"Em chưa có công cụ chuyển audio/video tiếng Việt thành text trực tiếp. Anh có 3 lựa chọn:*
> *(1) Upload Google NotebookLM (nhận audio tiếng Việt tốt), lấy bản transcript, rồi paste lại cho em.*
> *(2) Dùng Otter.ai hoặc Google Meet transcript để transcribe trước.*
> *(3) Em ghi chú file đã nhận nhưng không phân tích nội dung — chỉ coi như metadata."*

#### 2c. Scan internet (nếu chọn)

Dùng `web_search` và `web_fetch` theo thứ tự:

1. **Đọc `references/competitors.md`** để lấy danh sách đối thủ cố định
2. **Đọc `references/sources.md`** để lấy danh sách nguồn quét (Facebook Groups, forums, hashtags TikTok)
3. Tạo các truy vấn tìm kiếm theo mẫu:
   - `"phụ huynh [cấp học]" "chọn trường" 2026`
   - `"review trường [tên đối thủ]"`
   - `"học phí [cấp học]" "có đáng không"`
   - `"[tên KOL]" phụ huynh [cấp học]`
4. Dùng `web_fetch` đọc 3–5 bài viết/post có tương tác cao nhất cho mỗi truy vấn
5. Ghi chú nguồn (URL + ngày) cho MỖI insight — đây là yêu cầu bắt buộc của anh Dương (trong userPreferences: "luôn đưa ra nguồn trích dẫn")

**Giới hạn scan**: không quá 15–20 lần `web_search` + `web_fetch` tổng cộng cho 1 lần chạy skill, để tránh chạy quá lâu. Nếu người dùng cần scan sâu hơn, đề xuất họ dùng Research feature của Claude.

---

### Bước 3: Phân tích và gán trọng số

Với mỗi mục Jobs/Pains/Gains tìm được, gán 3 thuộc tính:

#### 3a. Trọng số (1–5)

Tính theo công thức:

```
Trọng số = (Tần suất × 0.4) + (Cường độ cảm xúc × 0.3) + (Tính thời sự × 0.3)
```

- **Tần suất**: số lần đề cập trong dữ liệu scan (1: 1–2 lần → 5: >20 lần)
- **Cường độ cảm xúc**: từ ngữ mạnh/yếu (1: trung tính → 5: rất mạnh như "tuyệt vọng", "không chịu nổi")
- **Tính thời sự**: xuất hiện gần đây (1: >1 năm → 5: trong 3 tháng gần nhất)

Làm tròn về số nguyên 1–5. Viết công thức tính ra trong báo cáo để anh Dương thấy minh bạch.

#### 3b. Trạng thái (so với hồ sơ cũ)

- **MỚI**: không có trong hồ sơ cũ
- **CŨ**: có trong hồ sơ cũ, không thay đổi
- **THAY ĐỔI**: có trong hồ sơ cũ nhưng cường độ/ngữ cảnh thay đổi (ví dụ: "con nghiện game" cũ → "con nghiện TikTok short-form" mới)
- **BIẾN MẤT**: có trong hồ sơ cũ nhưng không còn thấy trong dữ liệu mới (ghi chú riêng)

#### 3c. Xu hướng

- **↑ Tăng**: tần suất/cường độ tăng so với cũ
- **↓ Giảm**: giảm so với cũ
- **→ Ổn định**: không đổi
- **⟳ Chu kỳ**: xuất hiện theo mùa (ví dụ: Pains về chọn trường thường đỉnh điểm tháng 3–5)

---

### Bước 4: Liệt kê giải pháp thị trường đang có

Với mỗi Pain/Gain có trọng số ≥ 3, liệt kê đối thủ nào đang giải quyết vấn đề đó như thế nào. Dùng danh sách đối thủ trong `references/competitors.md`.

Bảng mẫu:

| Pain/Gain | Trọng số | Đối thủ giải quyết | Cách họ làm | Mức độ hiệu quả (1–5) |
|-----------|----------|--------------------|-----------| ----------------------|
| Con nghiện TikTok | 5 | Vinschool | Khóa "Digital Wellbeing" tuần 1 tiết | 3 |

---

### Bước 5: Đề xuất giải pháp Việt Anh cần phát triển

Đưa ra 5–10 đề xuất, với mỗi đề xuất ghi:

- **Tên giải pháp** (ngắn gọn)
- **Pain/Gain đang giải quyết**
- **Mô tả** (2–3 câu)
- **Độ khó triển khai** (Thấp / Trung bình / Cao)
- **Độ tác động dự kiến** (1–5)
- **Tài nguyên cần** (nhân sự, ngân sách, thời gian ước tính)
- **Mối liên hệ với các dự án hiện có của Việt Anh** (Lion Camp, AI Powered School, PDR — Plan-Do-Review, mầm non là Plan-Do-Recall — Buddy System, v.v. — dùng userMemories để tham chiếu đúng)

Sau khi liệt kê, **dùng `ask_user_input_v0` để anh Dương chọn** 3–5 giải pháp muốn triển khai (type: multi_select).

---

### Bước 6: Xuất báo cáo Word + To-do list

Dùng skill `docx` (ở `/mnt/skills/public/docx/SKILL.md`) để tạo file Word với cấu trúc:

```
Trang 1 — Tóm tắt điều hành
  - Ngày cập nhật, cấp học, nguồn dữ liệu
  - 3–5 insight quan trọng nhất
  - Ý kiến của Claude (bắt buộc — anh Dương yêu cầu trong userPreferences)

Trang 2–N — Bảng VPC cập nhật
  - Bảng 9 cột: Jobs | Pains | Gains | Gain Creators | Pain Relievers | Products & Services | Trọng số | Trạng thái | Xu hướng | Nguồn
  - 1 bảng cho mỗi cấp học được chọn

Trang N+1 — Giải pháp thị trường đang có
  - Bảng: Pain/Gain × Đối thủ × Cách làm × Hiệu quả

Trang N+2 — Đề xuất giải pháp Việt Anh cần phát triển
  - 5–10 đề xuất có sắp xếp theo Độ tác động / Độ khó

Trang N+3 — To-do list cho các giải pháp đã chọn
  - Với mỗi giải pháp: danh sách 5–10 việc cụ thể, có thời hạn gợi ý, có người chịu trách nhiệm gợi ý (dùng userMemories để biết team Việt Anh — ví dụ: Duy - VAGV, Thảo - NTT, Tuyền - VABT, Tú - finance, Tiến - ops, Dương - PR)

Trang cuối — Ghi chú nguồn dữ liệu
  - Liệt kê đầy đủ URL, ngày truy cập, số post/comment đã scan
```

Lưu file vào `/mnt/user-data/outputs/ho-so-khach-hang-[cap-hoc]-[YYYY-MM-DD].docx` và dùng `present_files` để gửi cho anh Dương.

---

## Bảo đảm chất lượng — Checklist trước khi giao báo cáo

- [ ] Giữ đúng 7 cột gốc của VPC Việt Anh (không thay tên cột)
- [ ] Mọi Pain/Gain đều có trọng số, trạng thái, xu hướng
- [ ] Mọi insight đều có nguồn (URL + ngày) — KHÔNG bịa nguồn
- [ ] Đã đối chiếu với hồ sơ cũ (trừ khi user chọn "Không")
- [ ] File docx đã được tạo ở `/mnt/user-data/outputs/` và present qua `present_files`
- [ ] Có phần "Ý kiến của Claude" và "To-do list" như anh Dương yêu cầu trong userPreferences
- [ ] Nêu rõ hạn chế nếu có (audio không transcribe được, scan internet thiếu dữ liệu, v.v.)

---

## Giọng điệu và phong cách viết

Theo userPreferences của anh Dương:

- Văn phong đơn giản, trang trọng, chân thực
- Dùng nhiều dữ kiện cụ thể, hạn chế hoa mỹ
- Viết đủ ý, không cắt ngắn
- LUÔN có "Ý kiến của Claude" — nêu rõ em nghĩ gì, không chỉ liệt kê
- LUÔN có "To-do list" cụ thể ở cuối
- Nếu cần thêm thông tin, nói rõ cần gì để ra quyết định tốt hơn

---

## Xử lý lỗi và trường hợp đặc biệt

| Tình huống | Cách xử lý |
|-----------|-----------|
| User không upload file cũ | Hỏi có muốn tiếp tục không; nếu có thì ghi chú rõ "Không đối chiếu được" |
| Scan internet trả về <5 kết quả | Báo rõ, đề xuất mở rộng từ khóa hoặc Research feature |
| File upload bị hỏng/không đọc được | Báo lỗi cụ thể, đề xuất định dạng thay thế |
| User cung cấp audio/video | Theo 3 lựa chọn ở Bước 2b |
| User chọn "Tất cả cấp học" | Làm đủ 5 cấp, báo sẽ mất thời gian (ước tính 10–15 phút) |
| Dữ liệu mâu thuẫn (cũ nói A, mới nói ngược A) | Ghi cả 2, đánh dấu "MÂU THUẪN — cần anh xác nhận" |

---

## Tham chiếu

- `references/competitors.md` — Danh sách đối thủ cạnh tranh và KOL giáo dục cùng tệp
- `references/sources.md` — Danh sách nguồn scan internet (Facebook Groups, forums, hashtags)
- `references/vpc-template.md` — Template Value Proposition Canvas đúng chuẩn Việt Anh
- `/mnt/skills/public/docx/SKILL.md` — Skill tạo file Word
- `/mnt/skills/public/xlsx/SKILL.md` — Skill đọc/ghi file Excel (cho file hồ sơ cũ)
