---
name: kg-sinh-cau-hoi
description: "Sinh ngân hàng câu hỏi cho MỘT điểm tri thức nguyên tử trong Knowledge Graph của Trường Việt Anh: 8–12 câu trải 3 bậc, mỗi câu gắn 2 nhãn ĐỘC LẬP (DOK và độ khó), mỗi phương án nhiễu gắn một quan niệm sai. Dùng khi người dùng nói: \"sinh câu hỏi cho điểm ...\", \"tạo ngân hàng câu hỏi\", \"viết bài tập gắn nhãn DOK\", \"làm câu hỏi 3 bậc\", \"tạo distractor theo quan niệm sai\"."
---

# Trạm 3 — Ngân hàng câu hỏi  (chuẩn ID v3.1)

Nhiệm vụ: với một điểm nguyên tử, sinh 8–12 câu hỏi đủ chất lượng để đo độ thành thạo.

## Hỏi trước nếu thiếu
- Node đích: `ref` hoặc `node_key` (`KC-#######`) + tên điểm + mô tả + mục tiêu 3 bậc
  (Bậc 1 Hiểu / Bậc 2 Vận dụng chuẩn / Bậc 3 Vận dụng cao).

## Quy tắc BẮT BUỘC
- Mỗi câu mang **2 nhãn ĐỘC LẬP**: `dok` (1–4, độ sâu nhận thức) và `do_kho` (dễ/TB/khó). KHÔNG trộn.
- Mỗi **phương án nhiễu (distractor) phải gắn một quan niệm sai cụ thể** (để chẩn đoán, không chỉ để đánh đố).
- Phân bổ: ~3 câu Bậc 1 (DOK1), ~4 câu Bậc 2 (DOK2), ~3 câu Bậc 3 (DOK3).
- PHẦN ĐỊNH LƯỢNG (Toán/Lý/Hoá): ưu tiên **câu tham số hoá** (khuôn thay số), GHI lời giải
  từng bước, khai báo **`tham_so_mien`** (miền biến + ràng buộc bảo toàn độ khó, vd "không
  phát sinh nhớ", "nghiệm nguyên dương") và **`xac_minh_dinh_luong`** (đáp án đã kiểm bằng
  máy tính/CAS: {da_xac_minh: true, cong_cu, ngay}). Tự kiểm lại mọi đáp án số.
- Câu Bậc 2–3 mặc định bật `do_tu_tin: true` (app sẽ hỏi mức tự tin 1–3 kèm câu trả lời).

## Dạng thức câu hỏi cho phép (16 mã — không đổi giữa các phiên bản schema)
Mỗi câu PHẢI ghi trường `dang_cau_hoi`, chọn trong 16 mã: Nhóm A chấm tự động: mcq,
dung_sai, dien_dap_an, dien_khuyet, sap_xep, noi_cot, nhieu_buoc. Nhóm B chấm rubric
(≤30% ngân hàng mỗi node): tu_luan_ngan, tim_loi, viet_doan, giai_thich_cho_ban,
du_doan_giai_thich, phan_bien, van_dung_thuc_te (chỉ node tích hợp), phan_tu (không tính
mastery). Nhóm C media: noi, nghe.
Phân bổ khuyến nghị mỗi node 8–12 câu: Bậc 1 = mcq/dung_sai/dien_khuyet; Bậc 2 = mcq
+ dien_dap_an + nhieu_buoc + (tim_loi hoặc tu_luan_ngan); Bậc 3 = dien_dap_an +
tu_luan_ngan/giai_thich_cho_ban/phan_bien tuỳ môn. Câu định lượng ưu tiên dien_dap_an
tham số hoá. Câu nhieu_buoc và tim_loi: bước hỏng/lỗi cài sẵn PHẢI gắn quan niệm sai (misc_ref).

## QUY ƯỚC ĐỊNH DANH v3 (BẮT BUỘC — CHỈ thay quy tắc đặt MÃ, KHÔNG bớt trường nội dung)
- **Không tự đặt mã câu hỏi.** Mã thật là `Q-#######` bất biến, do DATABASE cấp tự động
  (sequence tập trung) khi nạp → không trùng dù nhiều người soạn. Khi soạn để **`question_key` TRỐNG**.
- Trường trỏ node dùng **`node_key` (`KC-#######`)** hoặc `ref` của node — **KHÔNG** dùng mã
  mã hoá môn/lớp/chương (không "SI10-C07-...").
- **Quan niệm sai:** mỗi quan niệm sai của node được liệt kê MỘT LẦN ở đầu kết quả với mã tạm
  cục bộ **`misc_ref`** (m01, m02...) + mô tả. Distractor và Trạm 4 trỏ bằng `misc_ref`.
  DB sẽ cấp mã bất biến `M-#######` khi nạp — KHÔNG tự chế mã mã hoá vị trí (không "MISC-HOA10-017").
- File cũ dùng mã kiểu cũ: giữ nguyên, coi mã cũ là `ref`/`misc_ref` legacy khi import.

## Mỗi câu gồm (GIỮ ĐỦ trường)
`question_key(để trống), node_key(hoặc ref), tier, dok, do_kho, dang_cau_hoi, noi_dung, dap_an, loi_giai,
distractors[{phuong_an, misc_ref, quan_niem_sai}], tham_so_hoa (true/false), tham_so_mien (khi tham_so_hoa=true),
xac_minh_dinh_luong (môn định lượng), do_tu_tin (mặc định true với Bậc 2–3)`

## Các bước
1. Liệt kê trước bảng quan niệm sai của node: `misc_ref | mô tả | ví dụ biểu hiện`.
2. Sinh câu theo từng bậc, bám đúng mục tiêu bậc.
3. Với mỗi câu MCQ, viết 3 distractor, mỗi cái trỏ một `misc_ref`; ghi rõ lỗi đó.
4. Gắn nhãn DOK và độ khó riêng biệt.
5. Tự bấm máy tính kiểm đáp án số; ghi kết quả vào `xac_minh_dinh_luong`.

## Định dạng xuất
- Bảng quan niệm sai (misc_ref) + bảng tóm tắt câu hỏi + JSON mảng câu hỏi đúng schema v3.1
  (`question_key` để trống, trỏ node bằng `node_key`/`ref`, distractor trỏ `misc_ref`).
- Cuối ghi: "Giáo viên phải kiểm đáp án + chất lượng distractor trước khi phát hành."
