---
name: kg-quan-he-lien-ket
description: >
  Gắn quan hệ giữa các điểm tri thức nguyên tử trong Knowledge Graph của Trường Việt Anh:
  tiền đề cứng, liên quan mềm, dễ-nhầm-với, và liên kết chéo môn (vd Hoá ↔ Toán), kèm trọng số.
  Dùng khi người dùng nói: "gắn tiền đề", "nối quan hệ các node", "vẽ prerequisite", "liên kết chéo môn",
  "xây cạnh knowledge graph", "quan hệ giữa các điểm tri thức".
---

# Trạm 2 — Quan hệ & liên kết chéo  (chuẩn ID v3)

Nhiệm vụ: nhận danh sách node (từ Trạm 1) và sinh các CẠNH có hướng, có loại, có trọng số.

## Hỏi trước nếu thiếu
- Danh sách node của chương (`ref` + label + mô tả).
- Có cần liên kết chéo sang môn khác không (vd Hoá cần kỹ năng Toán nào)?

## Năm loại cạnh (đúng schema v3)
1. `prerequisite_hard` (trọng số ~1.0): A BẮT BUỘC trước B. Dùng để khoá/mở lộ trình. **Giữ HIẾM và CHẮC.** (có hướng)
2. `related_soft` (0.3–0.5): A giúp hiểu sâu B nhưng không bắt buộc. (VÔ HƯỚNG)
3. `misconception` (0.5–0.7): hai điểm học sinh hay lẫn (vd chỉnh hợp ↔ tổ hợp). (VÔ HƯỚNG)
4. `cross_subject` (0.4–0.6): liên kết sang môn khác để chẩn đoán xuyên môn. (có hướng)
5. `part_of` (bộ phận — tổng thể). (có hướng)

## QUY ƯỚC CẠNH v3 (BẮT BUỘC — thay cho cách cũ)
- **KHÔNG đặt "ID cạnh" và TUYỆT ĐỐI KHÔNG gắn hậu tố loại** (bỏ hẳn `..._PRE`, `..._MIS`).
  Loại quan hệ nằm ở **trường `relation`**; database tự có khóa riêng cho cạnh.
- Cạnh chỉ gồm `from`, `to`, `relation`, `weight` (+ `ghi_chu` tuỳ chọn). `from`/`to` trỏ tới
  **`ref` của node** (Trạm 1) — sẽ được ánh xạ sang `KC-#######` khi import.
- **Quan hệ VÔ HƯỚNG (`misconception`, `related_soft`): CHỈ ghi MỘT chiều**, đừng ghi cả A→B
  lẫn B→A (database có ràng buộc chống trùng vô hướng; ghi hai lần sẽ bị chặn/coi là trùng).
- Không tạo cạnh trỏ tới node không tồn tại (database có khóa ngoại chặn cạnh mồ côi).

## Các bước
1. Với mỗi node, hỏi: "Để làm được điểm này, BẮT BUỘC phải nắm trước điểm nào?" → cạnh tiền đề cứng.
2. Thêm các quan hệ mềm / dễ-nhầm nếu rõ ràng (ghi một chiều).
3. Rà liên kết chéo môn: điểm này có dùng kỹ năng môn khác không?
4. **Kiểm soát mật độ:** nếu một node nối quá nhiều cạnh cứng → rà lại, vì sẽ gây nhiễu chẩn đoán.

## Định dạng xuất
- Bảng: `from(ref) | to(ref) | relation | weight | ghi chú`.
- JSON: mảng edge `{from, to, relation, weight}` (dùng `ref`, KHÔNG có trường id cạnh).
- Cuối: liệt kê các node "khởi đầu" (không có tiền đề) và node "đích/tích hợp".

## Quy ước
- Tiền đề cứng sai là sai cả chuỗi → ghi: "Chủ biên phải duyệt sơ đồ tiền đề."
