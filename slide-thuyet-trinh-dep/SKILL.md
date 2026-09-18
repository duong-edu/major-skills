---
name: slide-thuyet-trinh-dep
description: >
  Tạo slide thuyết trình đẹp chuẩn design DOTAKA cho TAKI Academy và các dự án kinh doanh. 
  Dùng skill này bất cứ khi nào người dùng yêu cầu: "tạo slide", "làm bài thuyết trình", 
  "tạo deck", "làm slide đẹp", "tạo presentation", "làm pptx", "slide training", "slide 
  khóa học", "slide pitch", "slide CEO", "slide báo cáo", "slide marketing", hoặc bất kỳ 
  yêu cầu nào liên quan đến tạo file .pptx. Kể cả khi người dùng chỉ nói "làm cho tôi 
  mấy slide về [chủ đề]" — cũng phải dùng skill này ngay. Output luôn là file .pptx 
  chuyên nghiệp theo đúng design system DOTAKA/TAKI.
---

# Skill: Slide Thuyết Trình Đẹp

Tạo slide .pptx chuyên nghiệp theo **Design System DOTAKA** — màu sắc, font, layout đã được
xây dựng từ slide mẫu thực tế của dự án.

---

## Bước 1: Đọc hướng dẫn kỹ thuật PPTX

Trước khi code, đọc file này:

```
/mnt/skills/public/pptx/pptxgenjs.md
```

Slide mẫu dùng **pptxgenjs** (Node.js). Luôn dùng thư viện này.

---

## Bước 2: Design System DOTAKA

### 2.1 Màu sắc chính

```js
const COLORS = {
  // === BACKGROUND ===
  bgDark:       '1E293B',   // Slide title/cover — navy dark
  bgLight:      'F8FAFC',   // Content slides — gần trắng
  bgWhite:      'FFFFFF',

  // === PRIMARY BRAND ===
  blue:         '1E40AF',   // Tiêu đề section, header bar
  blueLight:    '3B82F6',   // Accent, icon background, border
  bluePale:     'DBEAFE',   // Card background nhạt
  blueXLight:   'EFF6FF',   // Row highlight nhạt

  // === ACCENT / HIGHLIGHT ===
  orange:       'F97316',   // CTA, số liệu nổi bật, badge
  orangeLight:  'FFEDD5',   // Card background cam nhạt
  orangeDeep:   'EA580C',   // Text cam đậm trong badge

  // === TEXT ===
  textPrimary:  '0F172A',   // Tiêu đề, text tối
  textBody:     '334155',   // Body text
  textMuted:    '64748B',   // Caption, phụ đề
  textLight:    '94A3B8',   // Watermark, placeholder

  // === STATUS / FUNCTIONAL ===
  green:        '22C55E',
  greenPale:    'DCFCE7',
  greenDark:    '166534',
  red:          'EF4444',
  redPale:      'FEE2E2',
  redDark:      '991B1B',
  yellow:       'FEF3C7',
  yellowDark:   '92400E',

  // === BORDER / DIVIDER ===
  border:       'E2E8F0',
  borderMid:    'CBD5E1',
};
```

### 2.2 Typography

**Font duy nhất: `Montserrat`** (Google Font — luôn dùng font này)

```js
const FONTS = {
  heading:   { name: 'Montserrat', size: 28, bold: true,  color: COLORS.bgWhite },
  subheading:{ name: 'Montserrat', size: 14, bold: false, color: COLORS.textMuted },
  h2:        { name: 'Montserrat', size: 18, bold: true,  color: COLORS.textPrimary },
  h3:        { name: 'Montserrat', size: 14, bold: true,  color: COLORS.blue },
  body:      { name: 'Montserrat', size: 12, bold: false, color: COLORS.textBody },
  caption:   { name: 'Montserrat', size: 10, bold: false, color: COLORS.textMuted },
  badge:     { name: 'Montserrat', size: 10, bold: true,  color: COLORS.bgWhite },
  stat:      { name: 'Montserrat', size: 36, bold: true,  color: COLORS.orange },
  footer:    { name: 'Montserrat', size: 9,  bold: false, color: COLORS.textLight },
};
```

### 2.3 Slide size

```js
pptx.layout = 'LAYOUT_WIDE';   // 13.33" x 7.5" — widescreen 16:9 chuẩn
```

---

## Bước 3: Cấu trúc Slide Templates

### Template A — Cover Slide (Trang bìa)

```
┌─────────────────────────────────────────────────────────────┐
│  BG: bgDark (1E293B) + hình tròn blur trang trí              │
│                                                               │
│  [LOGO / ICON vùng trái]    [Tiêu đề lớn — trắng, 32pt]     │
│                              [Subtitle — orange, 14pt]       │
│                                                               │
│  [Tag nav: chủ đề 1 | 2 | 3 | 4]  4 pill nhỏ               │
│  [Mục tiêu khóa học — italic, 12pt, textLight]               │
│  © Brand Name 2025  ·  Confidential                          │
└─────────────────────────────────────────────────────────────┘
```

```js
// Ví dụ cover
slide.addRect({ x: 0, y: 0, w: '100%', h: '100%', fill: { color: COLORS.bgDark } });
// Tròn trang trí blur
slide.addShape(pptx.shapes.ELLIPSE, { x: 8.5, y: -1, w: 3.5, h: 3.5,
  fill: { color: '3B82F6', transparency: 80 }, line: { none: true } });
slide.addShape(pptx.shapes.ELLIPSE, { x: 10.5, y: 4, w: 2.5, h: 2.5,
  fill: { color: 'F97316', transparency: 85 }, line: { none: true } });
// Tiêu đề
slide.addText('TÊN KHÓA HỌC', {
  x: 1, y: 1.8, w: 9, h: 1.5,
  fontFace: 'Montserrat', fontSize: 34, bold: true,
  color: COLORS.bgWhite, align: 'left'
});
```

---

### Template B — Content 2 cột (Layout phổ biến nhất)

```
┌─────────────────────────────────────────────────────────────┐
│  [Header bar — blue, full width]  TIÊU ĐỀ SLIDE | Subtitle  │
├──────────────────────────┬──────────────────────────────────┤
│  CỘT TRÁI (6.2")         │  CỘT PHẢI (6.2")                │
│                          │                                   │
│  Card/section 1          │  Card/section 2                  │
│  ○ bullet                │  ○ bullet                        │
│  ○ bullet                │  ○ bullet                        │
│                          │                                   │
│  Card/section 3          │  Card/section 4                  │
└──────────────────────────┴──────────────────────────────────┘
│  Footer: © Brand  ·  Section Name | N/Total               │
└─────────────────────────────────────────────────────────────┘
```

```js
// Header bar
slide.addRect({ x: 0, y: 0, w: '100%', h: 0.85, fill: { color: COLORS.blue } });
slide.addText('TIÊU ĐỀ SLIDE', {
  x: 0.3, y: 0.1, w: 8, h: 0.45,
  fontFace: 'Montserrat', fontSize: 18, bold: true, color: COLORS.bgWhite
});
slide.addText('Phụ đề mô tả ngắn', {
  x: 0.3, y: 0.52, w: 8, h: 0.28,
  fontFace: 'Montserrat', fontSize: 11, color: 'BFD8FF'
});
```

---

### Template C — Section Header (Trang chuyển chủ đề)

```
┌─────────────────────────────────────────────────────────────┐
│  BG: blue (1E40AF)                                           │
│                                                              │
│           [Số thứ tự — oval cam, 72pt]                      │
│           [Tên section — trắng, 32pt, bold]                 │
│           [Mô tả — BFD8FF, 16pt]                            │
│                                                              │
│           [3-4 bullet điểm sẽ cover — trắng, 12pt]         │
└─────────────────────────────────────────────────────────────┘
```

---

### Template D — Bảng / Quy trình

```
Header row: blue background
Data rows: xen kẽ F8FAFC và FFFFFF
Border: E2E8F0
Accent column: bluePale (DBEAFE)
```

---

### Template E — Stat / KPI Callout

```
┌────────────────┐  ┌────────────────┐  ┌────────────────┐
│   orangeLight  │  │   bluePale     │  │   greenPale    │
│   [ICON/emoji] │  │   [ICON/emoji] │  │   [ICON/emoji] │
│   [Số — 36pt]  │  │   [Số — 36pt]  │  │   [Số — 36pt]  │
│  [Label 12pt]  │  │  [Label 12pt]  │  │  [Label 12pt]  │
└────────────────┘  └────────────────┘  └────────────────┘
```

---

## Bước 4: Components tái sử dụng

### Header Bar (mọi content slide)

```js
function addHeader(slide, title, subtitle) {
  slide.addRect({ x: 0, y: 0, w: 13.33, h: 0.85, fill: { color: '1E40AF' } });
  slide.addText(title, {
    x: 0.35, y: 0.08, w: 10, h: 0.44,
    fontFace: 'Montserrat', fontSize: 18, bold: true, color: 'FFFFFF'
  });
  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.35, y: 0.52, w: 10, h: 0.28,
      fontFace: 'Montserrat', fontSize: 11, color: 'BFD8FF'
    });
  }
}
```

### Footer (mọi slide)

```js
function addFooter(slide, brand, section, page) {
  slide.addRect({ x: 0, y: 7.18, w: 13.33, h: 0.32, fill: { color: 'F1F5F9' } });
  slide.addText(`© ${brand} 2025`, {
    x: 0.3, y: 7.2, w: 4, h: 0.25,
    fontFace: 'Montserrat', fontSize: 9, color: '94A3B8'
  });
  slide.addText(`${section} | ${page}`, {
    x: 9, y: 7.2, w: 4, h: 0.25,
    fontFace: 'Montserrat', fontSize: 9, color: '94A3B8', align: 'right'
  });
}
```

### Card với viền màu trái

```js
function addCard(slide, x, y, w, h, accentColor, bgColor) {
  // Viền màu bên trái — signature style DOTAKA
  slide.addRect({ x, y, w: 0.06, h, fill: { color: accentColor } });
  slide.addRect({ x: x+0.06, y, w: w-0.06, h, fill: { color: bgColor },
    line: { color: 'E2E8F0', width: 0.5 } });
}
```

### Badge / Tag pill

```js
function addBadge(slide, text, x, y, color) {
  slide.addText(text, {
    x, y, w: 1.8, h: 0.28,
    fontFace: 'Montserrat', fontSize: 9, bold: true,
    color: 'FFFFFF', fill: { color: color || '1E40AF' },
    align: 'center',
    rectRadius: 0.14   // pill shape
  });
}
```

### Icon circle

```js
function addIconCircle(slide, emoji, x, y, size, bgColor) {
  slide.addShape(pptx.shapes.ELLIPSE, {
    x, y, w: size, h: size,
    fill: { color: bgColor || 'DBEAFE' },
    line: { none: true }
  });
  slide.addText(emoji, {
    x, y: y + size*0.1, w: size, h: size*0.8,
    fontSize: Math.round(size * 22),
    align: 'center', valign: 'middle'
  });
}
```

---

## Bước 5: Quy tắc thiết kế bắt buộc

### ✅ BẮT BUỘC làm

- **Font Montserrat** trên toàn bộ slide
- **Header bar màu blue** (#1E40AF) trên mọi content slide
- **Footer** với brand name và số trang
- **Viền màu bên trái** cho card/section groups
- **Xen kẽ màu card**: bluePale ↔ orangeLight ↔ greenPale cho variety
- **Số liệu nổi bật** dùng màu orange, font 32–40pt
- **Trang bìa và section header** dùng nền tối (bgDark hoặc blue)
- **Trang content** dùng nền sáng (bgLight hoặc white)

### ❌ TUYỆT ĐỐI KHÔNG làm

- Không dùng font khác Montserrat
- Không dùng màu ngoài Design System (trừ khi user yêu cầu)
- Không tạo slide chỉ có text + bullet, không có visual element
- Không dùng gạch chân dưới tiêu đề (hallmark of AI-generated)
- Không căn giữa body text
- Không để text quá nhỏ (< 10pt)
- Không dùng quá 3 màu trên 1 slide

---

## Bước 6: Workflow thực hiện

```
1. Đọc /mnt/skills/public/pptx/pptxgenjs.md  ← BẮT BUỘC trước khi code
2. Setup project: mkdir /home/claude/slides && cd slides && npm install pptxgenjs
3. Tạo file generate.js với Design System DOTAKA (import colors, fonts, helpers trên)
4. Build từng slide theo template phù hợp
5. Chạy: node generate.js → tạo file .pptx
6. QA visual:
   a. python /mnt/skills/public/pptx/scripts/thumbnail.py output.pptx
   b. Xem thumbnail, kiểm tra layout, màu sắc, overflow
7. Fix và re-generate nếu có lỗi
8. Copy sang /mnt/user-data/outputs/ và present_files
```

---

## Bước 7: Ví dụ slide hoàn chỉnh

Đây là mẫu slide content 2 cột chuẩn DOTAKA:

```js
const pptx = new PptxGenJS();
pptx.layout = 'LAYOUT_WIDE';

const slide = pptx.addSlide();

// BG
slide.addRect({ x: 0, y: 0, w: 13.33, h: 7.5, fill: { color: 'F8FAFC' } });

// Header
slide.addRect({ x: 0, y: 0, w: 13.33, h: 0.85, fill: { color: '1E40AF' } });
slide.addText('5 Nguyên Tắc Vàng', {
  x: 0.35, y: 0.08, w: 10, h: 0.44,
  fontFace: 'Montserrat', fontSize: 18, bold: true, color: 'FFFFFF'
});
slide.addText('Nền tảng để bán hàng hiệu quả', {
  x: 0.35, y: 0.52, w: 10, h: 0.28,
  fontFace: 'Montserrat', fontSize: 11, color: 'BFD8FF'
});

// Card trái — có viền cam
slide.addRect({ x: 0.4, y: 1.0, w: 0.06, h: 1.4, fill: { color: 'F97316' } });
slide.addRect({ x: 0.46, y: 1.0, w: 5.6, h: 1.4,
  fill: { color: 'FFF7ED' }, line: { color: 'E2E8F0', width: 0.5 } });
slide.addText('💡 Bán bằng trải nghiệm thị giác', {
  x: 0.6, y: 1.08, w: 5.2, h: 0.35,
  fontFace: 'Montserrat', fontSize: 13, bold: true, color: '1E40AF'
});
slide.addText('Luôn gửi hình thi công thật, video ánh sáng ban đêm, feedback khách hàng.',
  { x: 0.6, y: 1.45, w: 5.2, h: 0.8,
    fontFace: 'Montserrat', fontSize: 11, color: '334155' });

// Card phải — có viền xanh
slide.addRect({ x: 7.1, y: 1.0, w: 0.06, h: 1.4, fill: { color: '3B82F6' } });
slide.addRect({ x: 7.16, y: 1.0, w: 5.6, h: 1.4,
  fill: { color: 'EFF6FF' }, line: { color: 'E2E8F0', width: 0.5 } });
slide.addText('🎯 Bán bằng cảm xúc', {
  x: 7.3, y: 1.08, w: 5.2, h: 0.35,
  fontFace: 'Montserrat', fontSize: 13, bold: true, color: '1E40AF'
});
slide.addText('Biết khen, biết đồng cảm. Kết nối cảm xúc trước khi kết nối lý trí.',
  { x: 7.3, y: 1.45, w: 5.2, h: 0.8,
    fontFace: 'Montserrat', fontSize: 11, color: '334155' });

// Stat callout
slide.addRect({ x: 0.4, y: 6.3, w: 12.5, h: 0.65,
  fill: { color: 'DBEAFE' }, line: { color: 'BFDBFE', width: 0.5 } });
slide.addText('🏆 Kết Luận Vàng: Người bán hàng không chỉ bán ánh sáng — mà bán cảm giác được sống trong không gian đáng tự hào.', {
  x: 0.6, y: 6.36, w: 12, h: 0.5,
  fontFace: 'Montserrat', fontSize: 11, bold: false,
  color: '1E40AF', italic: true
});

// Footer
slide.addRect({ x: 0, y: 7.18, w: 13.33, h: 0.32, fill: { color: 'F1F5F9' } });
slide.addText('© DOTAKA Marketing 2025', {
  x: 0.3, y: 7.2, w: 4, h: 0.25,
  fontFace: 'Montserrat', fontSize: 9, color: '94A3B8'
});
slide.addText('Slide 4/10', {
  x: 9, y: 7.2, w: 4, h: 0.25,
  fontFace: 'Montserrat', fontSize: 9, color: '94A3B8', align: 'right'
});

await pptx.writeFile({ fileName: 'output.pptx' });
```

---

## Tham khảo thêm

- Kỹ thuật tạo từ scratch: `/mnt/skills/public/pptx/pptxgenjs.md`
- Chỉnh sửa template có sẵn: `/mnt/skills/public/pptx/editing.md`
- QA và thumbnail: `/mnt/skills/public/pptx/SKILL.md` (phần QA)
