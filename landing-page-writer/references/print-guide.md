# Hướng dẫn Tờ rơi A5 2 mặt — In ấn

Đọc file này khi tạo ấn phẩm in ấn (tờ rơi, flyer, voucher) cho hệ thống Trường Việt Anh.

---

## Thông số kỹ thuật A5

| Thông số | Giá trị |
|----------|---------|
| Kích thước | 148mm × 210mm |
| CSS `@page` | `size: 148mm 210mm; margin: 0;` |
| Font tối thiểu | **16pt** — không có ngoại lệ |
| Font loại | **Sans-serif** — Arial (print), Be Vietnam Pro (web preview) |
| Màu sắc | Theo `brand-configs.md` |
| Xuất file | HTML → PDF qua WeasyPrint |

---

## Quy tắc layout bắt buộc

### Dùng `position: absolute` — không dùng flexbox

WeasyPrint có lỗi với flexbox: `flex: 1` không phân phối đúng không gian, và `page-break-after: always` tạo trang trắng thừa. Thay vào đó:

```css
/* Cấu trúc chuẩn */
body {
  width: 148mm;
  height: 210mm;
  position: relative;
  overflow: hidden;
  font-family: Arial, Helvetica, sans-serif;
}

.section-name {
  position: absolute;
  top: [X]mm;
  left: 0;
  right: 0;
  height: [Y]mm;
  overflow: hidden;
}
```

**Tổng chiều cao các section phải bằng đúng 210mm.** Kiểm tra bằng cách cộng tất cả `height` lại.

### Cách tính layout ví dụ (tờ rơi mặt trước)

```
Header:     14mm  (top: 0)
Ảnh hero:   60mm  (top: 14mm)
Stats bar:  13mm  (top: 74mm)
Badges:     13mm  (top: 87mm)
Benefits:   69mm  (top: 100mm) — 3 mục × 23mm
CTA:        41mm  (top: 169mm)
TOTAL:      210mm ✓
```

---

## Quy trình tạo PDF — 2 trang riêng biệt

### Bước 1: Tạo 2 file HTML riêng

```
front.html  → Mặt trước (thông tin chính, CTA)
back.html   → Mặt sau (voucher, chương trình, liên hệ)
```

Mỗi file chỉ chứa nội dung 1 trang — không dùng `page-break-after`.

### Bước 2: Render từng file thành PDF riêng, rồi ghép

```python
from weasyprint import HTML, CSS
from pypdf import PdfReader, PdfWriter
import io

css = CSS(string='@page { size: 148mm 210mm; margin: 0; }')
writer = PdfWriter()

for name in ['front', 'back']:
    pdf_bytes = HTML(filename=f'/path/to/{name}.html').write_pdf(stylesheets=[css])
    reader = PdfReader(io.BytesIO(pdf_bytes))
    writer.add_page(reader.pages[0])  # Lấy page[0] — tránh trang trắng thừa

with open('output.pdf', 'wb') as f:
    writer.write(f)
```

**Tại sao không render 1 file 2 trang?** WeasyPrint tạo thêm trang trắng sau mỗi section có `height: 210mm`, dẫn đến 4 trang thay vì 2. Tách 2 file là cách đáng tin cậy nhất.

### Cài đặt thư viện

```bash
pip install weasyprint pypdf qrcode[pil] --break-system-packages
```

---

## Nhúng hình ảnh

### Ảnh từ CDN Trường Việt Anh

HTML mở trực tiếp trên trình duyệt: dùng URL CDN đầy đủ.

```html
<img src="https://storage.fotoowl.ai/events/207302/[path]/1.webp" />
```

**Lưu ý**: WeasyPrint chạy trong Python sandbox có thể bị block khi tải ảnh ngoài (trả về 403). Trong trường hợp này, dùng placeholder màu hoặc base64.

### QR Code — nhúng base64

```python
import qrcode, base64
from io import BytesIO
from qrcode.constants import ERROR_CORRECT_H

qr = qrcode.QRCode(version=3, error_correction=ERROR_CORRECT_H,
                   box_size=8, border=2)
qr.add_data('https://mgis.edu.vn/trai-he-lioncamps')
img = qr.make_image(fill_color='#00553B', back_color='white')
buf = BytesIO()
img.save(buf, format='PNG')
b64 = base64.b64encode(buf.getvalue()).decode()
qr_src = f'data:image/png;base64,{b64}'
```

Dán `qr_src` vào HTML: `<img src="{qr_src}" width="18mm" height="18mm" />`

### Placeholder khi chưa có ảnh thật

```html
<div style="position:absolute; top:14mm; left:0; right:0; height:60mm;
            background:#046F4A; display:flex; align-items:center;
            justify-content:center; color:rgba(255,255,255,0.5);
            font-size:16pt; font-family:Arial;">
  [HÌNH ẢNH: mô tả ngắn]
</div>
```

---

## Cấu trúc mặt trước (Front) — Thông tin chính

```
HEADER (14mm)
  Logo + Tên trường + Địa chỉ web

ẢNH HERO (50–60mm)
  Ảnh đẹp nhất của trường / chương trình
  Có thể overlay text hoặc badge

STATS BAR (12–15mm)
  3–4 con số nổi bật ngang hàng (năm thành lập, số học sinh, v.v.)

HEADLINE + SUBHEADLINE (20–30mm)
  Lợi ích chính, ngắn gọn, đúng nỗi đau

BENEFITS (40–70mm)
  3 lợi ích chính, mỗi cái 1 icon + tiêu đề + 1–2 dòng mô tả

CTA (35–45mm)
  Nút đăng ký nổi bật
  URL + Hotline + QR code
  Urgency strip (nếu có deadline thật)
```

---

## Cấu trúc mặt sau (Back) — Voucher / Chi tiết

```
VOUCHER SECTION (30–40mm)
  Tiêu đề "Phiếu ưu đãi"
  Giảm bao nhiêu %, điều kiện áp dụng
  Đường cắt (cut line) phân cách với phần còn lại

DISCOUNT BAND (15–25mm)
  Con số giảm giá nổi bật — lớn, màu tương phản

HOW TO USE (20–30mm)
  3 bước đơn giản để dùng voucher

DANH SÁCH CHƯƠNG TRÌNH (50–70mm)
  Các khoá học / chương trình ngoại khoá
  Dùng 2 cột để tiết kiệm không gian
  Mỗi khoá: icon + tên + 1 câu mô tả

CONTACT (25–35mm)
  Địa chỉ, hotline, email, website
  Logo

HIỆU LỰC (8–12mm)
  Hạn sử dụng voucher
```

### Đường cắt (Cut line)

```css
.cut-line {
  position: absolute;
  top: [Xmm];
  left: 5mm;
  right: 5mm;
  height: 8mm;
  display: flex;
  align-items: center;
  gap: 2mm;
}
.cut-icon { font-size: 16pt; }  /* ✂ */
.cut-dash {
  flex: 1;
  border-top: 1pt dashed #aaa;
}
```

---

## Checklist trước khi giao nhà in

- [ ] Font ≥ 16pt ở mọi phần (kể cả footer, fine print, caption)
- [ ] Font sans-serif — không có font có chân (serif)
- [ ] Tổng chiều cao các section = 210mm (front) + 210mm (back)
- [ ] QR code test: quét được, dẫn đúng URL
- [ ] Hotline, địa chỉ, email đã điền thật (không còn placeholder)
- [ ] Logo hiển thị đúng
- [ ] Urgency text dùng deadline thật
- [ ] PDF xuất đúng 2 trang, không có trang trắng thừa
- [ ] File PDF ≥ 300 DPI hoặc vector (nếu nhà in yêu cầu)

---

## Font size — Quy tắc bất di bất dịch

| Loại nội dung | Tối thiểu |
|---------------|-----------|
| Headline chính | 18–24pt |
| Subheadline | 16–18pt |
| Body text | 16pt |
| Label / caption | 16pt |
| Fine print / footer | 16pt |
| Icon / emoji | 16–24pt |

**Không có ngoại lệ.** Nếu không đủ chỗ, rút ngắn nội dung — không được thu nhỏ chữ.

---

## Màu sắc theo brand

Xem `brand-configs.md` để biết palette đầy đủ của từng trường.

- **MGIS Mekong Xanh**: xanh `#046F4A`, vàng `#f5a623`, đỏ urgency `#e03c31`
- **Trường Việt Anh**: navy `#26275D`, vàng `#f9dd0e`
- **Lion Camps**: navy `#26275D`, cam `#f07d00`, vàng nhạt `#fde68a`
