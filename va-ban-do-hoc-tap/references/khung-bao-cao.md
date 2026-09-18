# Khung báo cáo Định vị Học tập + chuẩn brand

## Cấu trúc 7 mục + trang kết (dùng đúng thứ tự)

```
BÁO CÁO ĐỊNH VỊ HỌC TẬP — [Tên gọi của con], lớp [X]
[ngày lập · logo Bản đồ học tập / Việt Anh]

1. Điều gia đình đang quan tâm
   → Trích lại nguyên văn nỗi lo (câu 2) + mong muốn 3 năm (câu 3) của phụ huynh,
     và 2–3 câu trả lời thẳng: dữ liệu nói gì về nỗi lo đó. Đây là mục phụ huynh
     đọc đầu tiên — nếu mục này chung chung, họ ngừng đọc.

2. Bức tranh học tập của con
   → Tiểu học: lưới tín hiệu qua các năm. THCS/THPT: bảng điểm chuẩn hóa
     + GPA quy đổi + biểu đồ xu hướng.

3. Thế mạnh nổi bật (2–4 mục, mỗi mục có BẰNG CHỨNG)
   → Mỗi thế mạnh: 1 câu kết luận + trích dẫn cụ thể (con điểm, lời nhận xét,
     xu hướng). Ưu tiên thứ lặp lại nhiều năm/nhiều nguồn.

4. Vùng cần vun (1–3 mục, giọng xây dựng)
   → "Cần vun" chứ không phải "điểm yếu". Mỗi mục kèm 1 việc làm được ngay
     trong 3 tháng + 1 dòng "Tài nguyên miễn phí để bắt đầu" (chọn theo
     tai-nguyen-mien-phi.md). Với THCS/THPT luôn soi riêng tiếng Anh ở đây
     nếu chưa đạt mốc, kèm số đối chiếu quốc gia có nguồn.

5. Điều gia đình có thể chưa để ý
   → 1–2 phát hiện từ dữ liệu mà khảo sát không nhắc. Mục đáng tiền nhất
     của báo cáo.

6. Đối chiếu mong muốn ↔ thực tế [+ trang reality-check du học nếu kích hoạt]
   → Khớp / Lệch / Đường đi 12 tháng tới (3–5 việc cụ thể, có mốc thời gian).
     KHÔNG lập kế hoạch chi tiết — đó là việc của sản phẩm chính.

7. Định vị chung
   → Tiểu học: 3–4 câu về nền tảng đang vững và 1 ưu tiên năm tới.
     THCS/THPT: định vị so mặt bằng (thang 3 nhóm trong che-do-theo-cap.md)
     + 1 câu về cửa sổ thời gian (đặc biệt lớp 9).

TRANG KẾT — "Bản đồ này mới thấy 1/4 con bạn"
   → Báo cáo đo được Kiến thức — 1 trong 4 lĩnh vực giáo dục toàn diện:
     Kiến thức · Kỹ năng · Phẩm chất · Sức khỏe. 3–4 câu giới thiệu bản đồ
     4 chiều (không quảng cáo trường, nói về phương pháp).
   → KHỐI CTA 3 tầng (vẫn là MỘT CTA duy nhất — một hành động: đặt lịch):
     (a) "3 câu hỏi còn bỏ ngỏ về [Tên]" — 3 câu hỏi CÁ NHÂN HÓA rút thẳng
         từ phát hiện của chính báo cáo này, viết ở dạng câu hỏi gia đình
         chưa trả lời được (vd với ca Poppy: "Nếu Tiếng Trung là đích, ta
         làm gì với tiếng Anh đang tụt?"). Đây là lý do buổi tư vấn tồn tại
         — phụ huynh đặt lịch vì muốn nghe nốt câu trả lời, không phải vì
         được mời chung chung. Không bao giờ dùng 3 câu template.
     (b) Lời hứa cụ thể của buổi 30 phút, 1 dòng: "Anh chị ra về với 3 việc
         ưu tiên cho học kỳ tới của [Tên] — không cam kết mua gì."
     (c) Nút vàng #F9DD0E chữ Navy #26275D: "Đặt lịch 30 phút — miễn phí"
         + Zalo OA (kèm QR nếu bản in) + 1 dòng ai tư vấn (vai trò, không PR).
   → Disclaimer chuẩn (xem loc-pii-va-qc.md).
```

Độ dài mục tiêu: 6–8 trang A4. Ngắn hơn 5 trang = thiếu cá nhân hóa; dài hơn 10 = phụ huynh không đọc hết.

## Chuẩn brand (theo Brand Guideline Viet Anh MASTER v2.0)

- **Màu:** Navy `#26275D` cho tiêu đề, thanh trang trí, nền header. Vàng `#F9DD0E` CHỈ cho CTA và điểm nhấn nhỏ — không tô mảng lớn. Nền sáng `#F0F4F8`, chữ chính `#1A1A2E`, viền `#E2E8F0`. Quy tắc cứng: chữ trên nền vàng phải là Navy, không bao giờ trắng.
- **Font:** Be Vietnam Pro (heading 700, body 400–500); file Word dùng Arial thay thế. Cỡ chữ body ≥ 11pt.
- **Biểu đồ:** dùng `scripts/ve_bieu_do.py`, xuất PNG nhúng vào Word; tiêu đề biểu đồ dùng tên gọi của con, không họ tên đầy đủ. Điểm theo môn: LUÔN dùng `diem_mon_cot()` (cột, nhóm màu) — cấm biểu đồ đường nhiều môn; đường chỉ dành cho 1 chuỗi xu hướng (`gpa_xu_huong`).
- **Giọng điệu:** ấm áp, chân thật, thực tế — "Vui vẻ và Thực dụng". Nói với phụ huynh như một nhà giáo dục đáng tin: khen có bằng chứng, chê có đường ra, không đao to búa lớn, không thuật ngữ khoa trương (nói "quy đổi điểm quốc tế" thay vì "chuẩn hóa GPA weighted"). Xưng "chúng tôi", gọi "anh/chị" và gọi con bằng tên.
- **Điều cấm trong báo cáo:** logo trường khác, so sánh chê bai trường con đang học, ngôn ngữ tạo khan hiếm giả ("chỉ còn 3 suất"), mọi cam kết đầu ra.

## Cách build file Word

Đọc SKILL.md của skill `docx` trước khi build (quy tắc bảng, ảnh, font). Trình tự chuẩn: sinh biểu đồ PNG → viết script docx theo khung 7 mục → build → render ra ảnh → tự xem lại từng trang (QC điểm 10) → sửa nếu lỗi → giao.
