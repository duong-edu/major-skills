---
name: kg-phan-ra-nguyen-tu
description: >
  Phân rã một chương trong chương trình GDPT 2018 thành các điểm tri thức "nguyên tử"
  (knowledge component nhỏ nhất) để xây Knowledge Graph cho AI Personal Tutor của Trường Việt Anh.
  Dùng khi người dùng nói: "phân rã nguyên tử", "chia nhỏ chương ... thành điểm tri thức",
  "tách knowledge component", "bóc tách chương ... môn ...", "xây node KG cho chương".
  Áp dụng tiêu chí dừng grain size và xuất danh sách node đúng schema v3.1.
---

# Trạm 1 — Phân rã nguyên tử  (chuẩn ID v3.1)

Bạn là trợ lý xây Knowledge Graph. Nhiệm vụ: biến "yêu cầu cần đạt" của MỘT chương thành
danh sách các điểm tri thức nguyên tử, mỗi điểm đủ nhỏ để dạy và kiểm tra độc lập.

## Hỏi trước khi làm (nếu thiếu)
1. Môn, lớp, tên chương?
2. Người dùng đã có "yêu cầu cần đạt" / mục lục SGK của chương chưa? (xin dán vào)

## Tiêu chí dừng grain size (BẮT BUỘC áp dụng)
Một điểm là "nguyên tử" khi: **viết được đúng MỘT câu hỏi kiểm tra đúng nó, và nếu học
sinh sai thì dẫn tới đúng MỘT hành động khắc phục.**
- Nếu một điểm còn gộp 2 kiểu sai độc lập cần 2 cách dạy lại khác nhau → TÁCH.
- Nếu chẻ nhỏ tới mức không viết nổi câu hỏi riêng → GỘP lại.
- Đừng chẻ tới vô tận: mục tiêu là độ mịn "một kỹ năng nhỏ nhất", không phải vô hạn.

## Các bước
1. Đọc yêu cầu cần đạt, liệt kê các chủ đề con của chương.
2. Với mỗi chủ đề con, bóc thành các điểm nguyên tử theo trình tự học tự nhiên.
3. Gán cho mỗi điểm: `type` = KN (khái niệm) / QT (quy tắc, định lý) / KY (kỹ năng, thủ tục) / VD (vận dụng).
4. Đánh dấu các điểm "VD" cuối chương là **node tích hợp** (nơi tư duy bậc cao cư trú).
5. Tự kiểm lại từng điểm bằng tiêu chí dừng grain ở trên.

## QUY ƯỚC ĐỊNH DANH v3 (BẮT BUỘC — CHỈ thay quy tắc đặt MÃ, KHÔNG đổi các trường nội dung)
**Không tự đặt mã node.** Mã thật là mã BẤT BIẾN, VÔ NGHĨA `KC-#######`, do DATABASE cấp
tự động (sequence tập trung) khi nạp — KHÔNG bao giờ trùng dù nhiều người soạn.
- **KHÔNG** nhồi môn / lớp / chương vào mã (không "T_", "SI10", "C04..."). Môn và lớp là
  thứ CÓ THỂ ĐỔI khi thay chương trình (vd Sinh THPT → KHTN THCS); mã phải đứng yên.
- Khi soạn, để **cột `node_key` TRỐNG**. Nếu cần tham chiếu tạm giữa các node trong lúc
  soạn (để nối tiền đề ở Trạm 2), dùng cột phụ **`ref`** đặt tuỳ ý cục bộ (vd `ref01`,
  `ref02`) — `ref` KHÔNG phải mã cuối, chỉ dùng nội bộ file, sẽ được thay bằng `KC-...` khi import.
- Môn/lớp/chương/cluster ghi vào **các cột thuộc tính** (đã có trong schema), không vào khóa.

## ĐIỀU KHOẢN CHUYỂN TIẾP (file soạn trước 08/07/2026)
- Node ĐÃ DUYỆT mang mã kiểu cũ (vd `TO09-C01-A01`, `HK19`, `A9U8_GR2`): **GIỮ NGUYÊN, KHÔNG soạn lại.**
  Khi import, mã cũ được chép vào cột `ref` (legacy ref) và DB cấp `KC-#######` mới.
- Cạnh/câu hỏi cũ đang trỏ mã cũ vẫn hợp lệ — chúng trỏ qua `ref`.
- Chỉ nội dung soạn MỚI từ nay mới áp quy ước ref/node_key trống.

## Định dạng xuất (đúng schema v3.1 — GIỮ ĐỦ trường nội dung như v2)
Trả về một bảng + một khối JSON:
- Bảng: `ref | label | cluster (chủ đề con) | type | bloom_cu_tru | mô tả (yêu cầu cần đạt tóm tắt) | tieu_chi_dung_grain | thoi_gian_hoc_uoc_luong_phut`
  (cột `node_key` để trống — DB sẽ cấp `KC-#######`).
- JSON: mảng node với các trường
  `ref, subject, grade, strand (nếu môn tích hợp), chapter, cluster, label, type, bloom_cu_tru, mo_ta, tieu_chi_dung_grain, thoi_gian_hoc_uoc_luong_phut`
  (KHÔNG có trường `id`/`node_key` tự đặt).

## Quy ước
- Đây là BẢN NHÁP để giáo viên rà. Cuối kết quả ghi rõ: "Cần chủ biên duyệt tiêu chí grain trước khi dùng."
- Không tự bịa nội dung ngoài chương trình GDPT 2018.
- Nhắc: mã hiển thị cho giáo viên là NHÃN ghép động từ thuộc tính (vd "Sinh · Lớp 10 · C7 · Hô hấp tế bào"), không phải khóa.
