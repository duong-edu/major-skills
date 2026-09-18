# Brand Configurations — Hệ thống Trường Việt Anh

Đọc file này trước khi thiết kế bất kỳ landing page nào.
Chọn đúng config theo trường được chỉ định.

---

## 1. Trường Việt Anh (truongvietanh.com)

**Dùng khi**: website là truongvietanh.com, lioncamps.com, hoặc không chỉ định trường cụ thể.

```css
--primary:     #26275D;   /* Navy đậm — màu chủ đạo */
--accent:      #f9dd0e;   /* Vàng — CTA, highlight */
--light-bg:    #f0f4f8;   /* Nền sáng */
--text:        #1a1a2e;   /* Màu chữ chính */
--border:      #e2e8f0;
```

**Font**: Be Vietnam Pro (Google Fonts) — heading 700-900, body 400-500

**Logo**: `https://truongvietanh.com/wp-content/uploads/logo.png` *(placeholder — xác nhận URL thật)*

**Màu CTA button**: `#f9dd0e` (vàng), chữ navy

**Testimonials**: Dùng tên thật + lớp học / cơ sở cụ thể

**Tone**: Ấm áp, chân thật, giọng anh Dương (Nguyễn Mạnh Dương — Chủ tịch)

---

## 2. MGIS — Mekong Xanh (mgis.edu.vn)

**Dùng khi**: website là mgis.edu.vn, đề cập đến Rạch Giá / Kiên Giang / Mekong Xanh.

```css
--green:       #046F4A;   /* Xanh lá chủ đạo */
--green-dark:  #00553B;   /* Xanh đậm — header, footer */
--green-light: #e8f5f0;   /* Nền xanh nhạt */
--gold:        #f5a623;   /* Vàng — CTA, highlight, badge */
--red:         #e03c31;   /* Đỏ — urgency, warning */
--text:        #1a1a2e;
--border:      #e2e8f0;
--light-bg:    #f4faf7;
```

**Font**: Be Vietnam Pro (web) hoặc Arial (print/PDF)

**Logo**: `https://mgis.edu.vn/wp-content/uploads/2025/08/cropped-cropped-Logo_round-1.png`
*(hình tròn, border-radius: 50% khi dùng trong header)*

**Màu CTA button**: `#f5a623` (vàng), chữ trắng

**Địa chỉ**: Rạch Giá, Kiên Giang *(điền địa chỉ chính xác khi có)*

**Ảnh trường**: CDN `storage.fotoowl.ai/events/207302/Ec9mVyB2lgelwG662syxparCnEl2/high_without_logo/v2/[UUID]/[UUID]/1.webp`

**Tone**: Tự hào địa phương — "ngay tại Rạch Giá, không cần đi xa"

**Đối tượng chính**: Phụ huynh có con Tiểu học (lớp 1–5, 6–11 tuổi) tại Kiên Giang

---

## 3. Lion Camps (lioncamps.com / trên truongvietanh.com)

**Dùng khi**: sản phẩm là trại hè Lion Camps, URL chứa "trai-he" hoặc "lioncamps".

```css
--navy:        #26275D;   /* Navy — hero background */
--orange:      #f07d00;   /* Cam — CTA, badge */
--gold:        #fde68a;   /* Vàng nhạt — text trên nền tối */
--light-bg:    #f0f4f8;
```

**Mascot**: 🦁 Lion — dùng emoji trong headline/badge nếu phù hợp

**Slogan mặc định**: "Vui vẻ và thực dụng"

**7 Trụ cột Lion Camps** (luôn nhắc đến, điều chỉnh theo lứa tuổi):
1. Tiếng Anh thực dụng (giáo viên bản ngữ)
2. Tư duy phản biện
3. Lãnh đạo bản thân
4. SteamE & sáng tạo
5. Sức khoẻ & dinh dưỡng (5 nguyên tắc)
6. Kỹ năng tài chính
7. AI Education

**Ảnh Olympic 2026**: `storage.fotoowl.ai/events/242155/...`
**Ảnh hoạt động hàng ngày**: `storage.fotoowl.ai/events/252184/...`

**Cam kết luôn đề cập**: Hoàn 100% học phí sau 4 tuần nếu không hài lòng

**Giá Lion Camps Hè 2026** (mặc định cho tất cả cơ sở):
- Giá niêm yết: 29.998.000 VND
- Ưu đãi 100 suất đầu tháng 4: 19.998.000 VND
- Khai mạc: 15/6/2026, kéo dài 6 tuần

---

## Quy tắc chung cho mọi trường

### Font size tối thiểu
- **Digital (web)**: 16px minimum — KHÔNG có ngoại lệ
- **Print (PDF, tờ rơi)**: 16pt minimum — KHÔNG có ngoại lệ
- Font phải là **sans-serif** — không dùng font có chân (serif)

### Khoảng trống
- Landing page phải **thoáng** — không nhồi nhét nội dung
- Ảnh trường cần nhiều không gian — đây là lợi thế marketing
- Padding section tối thiểu: 60px (web), 6mm (print)

### CTA
- Mỗi trang chỉ có **1 CTA chính** — không phân tán
- CTA button phải nổi bật — màu tương phản với nền
- CTA text phải cụ thể: "Đăng ký cho con ngay →" thay vì "Click here"

### Urgency
- Chỉ dùng urgency thật (deadline thật, số suất thật)
- Không dùng countdown giả hoặc "chỉ còn X suất" không có cơ sở

### Testimonials
- Phải có tên thật + bối cảnh cụ thể (lớp học, cơ sở)
- Không dùng testimonial chung chung như "Phụ huynh tại TP.HCM"
- Nếu không có testimonial thật, để placeholder rõ ràng: `[TESTIMONIAL: phụ huynh học sinh lớp X]`
