---
name: kg-tai-nguyen-giang-day
description: >
  Soạn đề cương tài nguyên giảng dạy cho MỘT điểm tri thức của Trường Việt Anh, chọn định dạng
  THEO BẢN CHẤT KIẾN THỨC (không theo "phong cách học"): infographic cho quy tắc, video cho kỹ năng,
  bài có bẫy cho vận dụng. Dùng khi người dùng nói: "soạn tài nguyên giảng dạy", "làm học liệu cho điểm ...",
  "tạo infographic/video/mindmap dạy ...", "thiết kế học liệu 3 bậc".
---

# Trạm 5 — Tài nguyên giảng dạy  (chuẩn ID v3)

Nhiệm vụ: với một điểm nguyên tử, đề xuất và phác thảo tài nguyên cho 3 bậc thành thạo.

## Hỏi trước nếu thiếu
- Node đích: `ref` hoặc `node_key` (`KC-#######`) + tên điểm + loại (KN/QT/KY/VD) + mục tiêu 3 bậc.

## Nguyên tắc chọn định dạng (BẮT BUỘC)
Chọn theo BẢN CHẤT kiến thức, **KHÔNG theo "phong cách học" (VARK là lầm tưởng đã bị bác bỏ):**
- KN (khái niệm) → văn bản ngắn + hình minh hoạ + 1 ví dụ (dual coding: chữ + hình).
- QT (quy tắc/định lý) → infographic / thẻ ghi nhớ + phản ví dụ.
- KY (kỹ năng) → video / animation làm mẫu từng bước.
- VD (vận dụng) → bài toán có bẫy + checklist tự kiểm + mindmap nối nhiều điểm.
- Mọi tài nguyên có **bản tiếp cận thay thế** (text/audio) cho accessibility.

## Các bước
1. Xác định loại điểm → chọn định dạng cốt lõi theo bảng trên.
2. Phác nội dung tài nguyên cốt lõi (kịch bản video / bố cục infographic / nội dung text).
3. Đề xuất 1 tài nguyên bổ trợ (định dạng khác) + bản tiếp cận.
4. Ghi rõ tài nguyên phục vụ Bậc nào (1/2/3).

## QUY ƯỚC ĐỊNH DANH v3 (BẮT BUỘC — thay cho cách cũ)
- **Không tự đặt mã tài nguyên.** Mã thật là `R-#######` bất biến, do DATABASE cấp tự động
  (sequence tập trung) khi nạp → không trùng. Khi soạn để **`resource_key` TRỐNG**.
- Trường trỏ node dùng **`node_key` (`KC-#######`)** hoặc `ref` — **KHÔNG** dùng mã mã hoá
  môn/lớp/chương (không "SI10-C07-...").

## Định dạng xuất
- Mỗi tài nguyên: `resource_key(để trống), node_key(hoặc ref), tier, format, ly_do_chon_format, dual_coding, accessibility, noi_dung_phac_thao`.
- Ưu tiên gợi ý công cụ rẻ (Canva, AI tạo ảnh/video, TTS) để giáo viên ít rành công nghệ vẫn làm được.
- Cuối ghi: "Giáo viên bộ môn duyệt nội dung trước khi phát hành."
