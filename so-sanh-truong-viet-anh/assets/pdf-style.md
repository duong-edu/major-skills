# Style cho bản PDF so sánh (chuẩn thương hiệu Việt Anh)

> Dùng khi dựng HTML để in PDF. Mục tiêu: chuyên nghiệp, ấm áp, quét nhanh được; đúng nhận diện Việt Anh.

## Màu thương hiệu (chính thức v1.1)
- **Navy (chủ đạo)**: `#26275D` — chữ chính, đường kẻ bảng, header bảng, cột Việt Anh.
- **Đỏ nhấn tiêu đề lớn**: `#C8102E` — dùng cho **các tiêu đề lớn** (tên báo cáo ở bìa, tiêu đề mục H2). Đây là yêu cầu của anh Dương: tiêu đề lớn màu đỏ cho nổi bật.
- **Vàng Gold (nhấn)**: `#F9DD0E` — highlight, gạch chân tiêu đề, ô "quy đổi tài chính". Dùng tiết chế.
- **Phụ trợ**: trắng `#FFFFFF` nền; xám nhạt `#F4F5F8` nền bảng xen kẽ; xám chữ phụ `#5B5E73`; xanh tích cực `#1F9D6B`, cam `#E08A2B`, xám `#9AA0AE`.

> Quy tắc màu: **NỀN LUÔN TRẮNG** (kể cả trang bìa) để dễ in, tiết kiệm mực. KHÔNG dùng nền tối/đậm phủ cả trang. Tiêu đề lớn dùng **đỏ `#C8102E`**; chữ thân dùng Navy/đen. Vàng/Navy chỉ làm điểm nhấn nhỏ (viền, gạch chân, header bảng, cột biểu đồ) — không phủ mảng lớn.

## Typography (cỡ chữ — anh Dương yêu cầu lớn, dễ đọc)
- Font: hệ sans-serif có dấu tốt — ưu tiên "Be Vietnam Pro", "Inter", fallback `system-ui, 'Segoe UI', Roboto, Arial`. Nhúng qua `@font-face` base64 nếu cần in offline, hoặc dùng system-ui cho chắc.
- **Nội dung/thân bài: 16px** (line-height 1.6), màu Navy/đen. **Tiêu đề mục (heading H2): 24px, màu đỏ `#C8102E`**, đậm (gạch chân Vàng nếu muốn).
- Tiêu đề trang lớn (tên báo cáo ở bìa): 30–36px, **màu đỏ `#C8102E`**, nền trắng. Tiêu đề phụ (H3): 18–20px Navy. Caption/nguồn dưới biểu đồ: 12px xám.
- Vì chữ to hơn, cân nhắc nội dung mỗi trang gọn lại để không vỡ layout; bảng có thể để 14–15px nếu nhiều cột, nhưng thân bài giữ 16px.

## Thành phần
- **Bảng**: header nền Navy chữ trắng; hàng xen kẽ nền `#F4F5F8`; viền mảnh `#E3E5EC`. Số tiền canh phải.
- **Trang bìa (NỀN TRẮNG)**: nền trắng cho dễ in; **tên báo cáo cỡ lớn màu đỏ `#C8102E`**; dải Vàng/Navy mảnh trang trí; tên 2 trường đối xứng (card viền, không tô nền đậm); khối + ngày; dòng "Tài liệu tư vấn dành cho phụ huynh". Có thể thêm logo. KHÔNG dùng nền tối phủ trang.
- **Ô "Quy đổi giá trị tài chính"**: viền Vàng 2px, nền vàng nhạt `#FEF9CC`, con số lớn Navy/đỏ đậm.
- **Tiêu đề mục (H2)**: chữ **đỏ `#C8102E`**, có thể gạch chân Vàng; nền trắng.
- **Cột so sánh 2 trường**: 2 card cạnh nhau; card Việt Anh viền Navy, header Navy; card đối thủ viền xám, header xám — phân biệt thị giác nhưng vẫn tôn trọng.
- **Icon trạng thái**: ✓ (xanh) = mạnh/đầy đủ; ◐ (cam) = có nhưng hạn chế; — (xám) = không có/chưa rõ.
- Lề trang A4: 18–22mm. `@page { size: A4; margin: 18mm; }`, `-webkit-print-color-adjust: exact; print-color-adjust: exact;` để giữ màu nền khi in.

## Giọng & nội dung hiển thị
- Tiêu đề ấm áp, hướng phụ huynh: "So sánh giúp ba mẹ chọn trường cho con", không khô như báo cáo doanh nghiệp.
- Mọi số liệu kèm chú thích nguồn nhỏ. Ô quy đổi tài chính luôn có dòng "* Ước tính tham khảo theo giá thị trường".
- Tránh tường chữ: ưu tiên bảng, bullet ngắn, ô nhấn.

## Chống lỗi hiển thị khi in PDF (weasyprint)
- **KHÔNG dùng emoji** (⏳😊✓ kiểu emoji màu, ⭐…) trong nội dung in — font PDF thường thiếu, sẽ ra ô vuông "tofu". Thay bằng: chữ thường, ký hiệu an toàn (✓ ✕ – có thể OK nếu font hỗ trợ, nhưng an toàn nhất là tự vẽ icon bằng SVG: dấu tích, chấm tròn, biểu tượng người…).
- Icon trạng thái ✓/◐/— nên **vẽ bằng SVG nhỏ** (vòng tròn + path) thay vì ký tự, để chắc chắn hiện.
- Sau khi tạo PDF, **render mỗi trang ra PNG** (`pdftoppm -png -r 110 file.pdf out`) và **xem lại bằng mắt**: kiểm tra (a) không có ô vuông tofu, (b) không có chữ bị cắt trong biểu đồ, (c) bảng không tràn trang. Sửa và render lại nếu cần.
