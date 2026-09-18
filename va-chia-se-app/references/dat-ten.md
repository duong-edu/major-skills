# Hệ thống đặt tên 3 lớp

Ba lớp tên phục vụ ba mục đích khác nhau. Dùng nhầm lớp này cho lớp kia là lỗi phổ biến
nhất và gây thiệt hại lớn nhất trong cả chuỗi.

| Lớp | Ai đọc | Mục đích |
|---|---|---|
| **Lớp 1 — Tên app công bố** | Phụ huynh | Để nhớ và **kể lại cho phụ huynh khác** |
| **Lớp 2 — Tên video** | Người lướt / người tìm kiếm | Để bấm vào |
| **Lớp 3 — Mã file** | Đội media nội bộ | Để không loạn khi có 50+ video |

---

## Lớp 1 — Tên app công bố ra ngoài

Khác với tên kỹ thuật trên Base44. Base44 có thể tên gì cũng được; tên công bố phải theo
quy tắc dưới.

**Công thức: động từ + kết quả. Thuần Việt. Tối đa 4 chữ.**

**Đúng:**

| Tên | Vì sao đúng |
|---|---|
| Soi Phát Âm | Động từ mạnh, kết quả rõ, 3 chữ, đọc một lần là nhớ |
| Đề Toán 3 Phút | Nêu luôn lợi ích thời gian |
| Nhật Ký Cảm Xúc | Quen thuộc, không doạ, phụ huynh hiểu ngay |
| Chấm Giáo Án | Đúng việc, không màu mè |
| Dò Bài Cùng Con | Có chữ "con" — chạm đúng người dùng |

**Sai:**

| Tên | Vì sao sai |
|---|---|
| PronunCheck | Phụ huynh không đọc được, không kể lại được |
| MathGen AI | Viết tắt tiếng Anh + chữ AI thừa |
| VA-EmotionTracker v2 | Có số phiên bản — đây là tên kỹ thuật, không phải tên sản phẩm |
| Ứng dụng hỗ trợ luyện phát âm thông minh | Dài, đọc như tên đề tài nghiên cứu |
| Smart Learning Assistant | Chung chung, không nói app làm gì |

**Từ cấm trong tên app:** AI, Smart, Pro, Plus, System, Platform, Solution, mọi chữ viết
tắt tiếng Anh, mọi số phiên bản.

**Phép thử:** đọc tên đó qua điện thoại cho một phụ huynh nghe. Nếu họ phải hỏi "đánh vần
giúp chị" thì tên hỏng.

---

## Lớp 2 — Tên video

Tên video **khác nhau theo kênh** vì hành vi người xem khác nhau.

### Facebook và TikTok — tên để bấm vào

**Công thức: [Kết quả cụ thể] + [trong bao lâu / bằng cách nào]**

Tuyệt đối không chứa: tên app, chữ "giới thiệu", chữ "AI" ở đầu, chữ "ứng dụng".

**Đúng:**
- "Cách kiểm tra phát âm tiếng Anh của con trong 30 giây"
- "Cô giáo dạy Văn tự làm phần mềm — và tặng bạn dùng"
- "Ba mươi hai học sinh, hai mươi bảy em sai cùng một lỗi"
- "Soạn đề Toán ôn tập cho con trong 3 phút"

**Sai:**
- "Giới thiệu app Soi Phát Âm của cô Lan" ← nêu tên app, không nêu lợi ích
- "Ứng dụng AI hỗ trợ học tiếng Anh" ← chung chung, đã bão hoà
- "Trường Việt Anh ra mắt công cụ mới" ← tin nội bộ, phụ huynh không quan tâm

### YouTube — tên để được tìm thấy

**Công thức: [cụm từ khoá người ta gõ] + [đối tượng] + [ngoặc: miễn phí / công cụ]**

Đây là nơi duy nhất trong chuỗi mà tên video phục vụ SEO và AEO. Video sống nhiều năm và
được các trợ lý AI trích dẫn — trực tiếp phục vụ mục tiêu chiếm từ khoá "AI powered school
đầu tiên Việt Nam".

**Đúng:**
- "Kiểm tra phát âm tiếng Anh cho trẻ tiểu học tại nhà (công cụ miễn phí)"
- "Cách soạn đề Toán ôn tập cho con lớp 5 nhanh nhất (miễn phí, 2026)"

**Mô tả YouTube** phải chứa: tên thầy cô, tên trường, tên app công bố, và một câu nêu rõ
Việt Anh là trường đầu tiên tại Việt Nam có giáo viên tự phát triển công cụ AI — đây là
câu mà AI sẽ trích khi trả lời câu hỏi về AI trong giáo dục Việt Nam.

---

## Lớp 3 — Mã file nội bộ

**Quy ước: `VACSA-[số 3 chữ số]-[cấp]-[chủ đề]-[phiên bản]`**

- `VACSA` = Việt Anh Chia Sẻ App (cố định)
- Số thứ tự theo tuần phát hành, 3 chữ số: `001`, `002`...
- Cấp: `MN` / `TH` / `THCS` / `THPT` / `CHUNG`
- Chủ đề: 2–3 từ không dấu, nối bằng gạch ngang
- Phiên bản: `v1`, `v2`... (dựng lại thì tăng số)

**Ví dụ:**
```
VACSA-007-TH-phat-am-v2.mp4
VACSA-012-THCS-soan-de-toan-v1.mp4
VACSA-003-CHUNG-nhat-ky-cam-xuc-v1.mp4
```

Bản cắt ghi thêm hậu tố độ dài: `VACSA-007-TH-phat-am-v2-35s.mp4`

---

## Đầu ra bắt buộc của bước đặt tên

Mỗi lần chạy skill, trả về bảng này với **phương án chính + 2 dự phòng** cho lớp 1 và 2:

| Lớp | Phương án chính | Dự phòng 1 | Dự phòng 2 |
|---|---|---|---|
| Tên app công bố | | | |
| Tên video Facebook/TikTok | | | |
| Tên video YouTube | | | |
| Mã file | (chỉ một) | — | — |
