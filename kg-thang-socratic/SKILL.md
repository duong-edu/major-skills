---
name: kg-thang-socratic
description: >
  Soạn "thang Socratic" dẫn dắt học sinh tự sửa lỗi cho MỘT điểm tri thức của Trường Việt Anh:
  với mỗi quan niệm sai, tạo thang 4 bậc (ít → nhiều trợ giúp) + đáy hé đáp án + luật "cổng nỗ lực".
  Dùng khi người dùng nói: "soạn thang Socratic", "tạo câu hỏi dẫn dắt", "hint ladder", "gợi ý từng bậc",
  "câu hỏi Socratic theo quan niệm sai", "dẫn dắt học sinh tự tìm đáp án".
---

# Trạm 4 — Thang Socratic  (chuẩn ID v3.1)

Nhiệm vụ: với mỗi quan niệm sai đã có (từ distractor ở Trạm 3), soạn thang gợi ý dẫn học sinh tự sửa.

## Hỏi trước nếu thiếu
- Node đích: `ref` hoặc `node_key` (`KC-#######`) + tên điểm + **bảng quan niệm sai kèm `misc_ref`
  (từ Trạm 3)** + lời giải đúng.

## Cấu trúc mỗi thang (theo schema v3.1)
- **Bậc 1 — Siêu nhận thức:** hỏi học sinh đã suy luận thế nào ("Em ra kết quả này bằng cách nào?").
- **Bậc 2 — Hướng chú ý:** kéo sự chú ý về đúng chỗ hổng, KHÔNG nói lỗi.
- **Bậc 3 — Dẫn về tiền đề:** câu hỏi dẫn tới điểm tiền đề bị thiếu.
- **Bậc 4 — Giàn giáo mạnh:** ví dụ tương tự đơn giản hơn / điền khuyết.
- **Đáy:** chỉ mở khi qua cổng nỗ lực — hé đáp án KÈM lý do, rồi cho làm lại bài tương tự.

## Luật cổng nỗ lực (BẮT BUỘC ghi kèm)
- Mở đáy khi: đã thử ≥2–3 lần thực chất VÀ đã diễn đạt được lý lẽ ở Bậc 1, HOẶC có dấu hiệu bí thật.
- Học sinh giỏi: ít gợi ý, mở muộn. Học sinh yếu: giàn giáo nhiều, mở sớm hơn.
- CẤM nhảy thẳng xuống đáy chỉ vì học sinh xin đáp án.

## Nguyên tắc viết
- Mỗi lượt chỉ một câu hỏi; ngắn, đúng trình độ lớp.
- Giọng ấm áp, khích lệ; không hạ thấp.
- TUYỆT ĐỐI không lộ đáp án trước khi tới đáy.
- Phần định lượng: bám lời giải đã lưu, không tự tính lại.

## QUY ƯỚC ĐỊNH DANH v3 (BẮT BUỘC — CHỈ thay quy tắc đặt MÃ, KHÔNG bớt trường nội dung)
- **Không tự đặt mã thang.** Mã thật là `L-#######` bất biến, do DATABASE cấp tự động
  (sequence tập trung) khi nạp → không trùng. Khi soạn để **`ladder_key` TRỐNG**.
- Trường trỏ node dùng **`node_key` (`KC-#######`)** hoặc `ref` — **KHÔNG** dùng mã mã hoá vị trí.
- **Mỗi thang trỏ đúng MỘT quan niệm sai bằng `misc_ref`** (mã tạm cục bộ m01, m02... do Trạm 3
  lập). DB cấp `M-#######` khi nạp — KHÔNG tự chế mã mã hoá môn/lớp/chương.
- File cũ dùng mã kiểu cũ: giữ nguyên, coi là ref legacy khi import.

## Định dạng xuất
- Mỗi quan niệm sai (`misc_ref`) = một khối thang (Bậc 1→4 + Đáy) + luật cổng nỗ lực.
- JSON đúng trường `socratic_ladder` schema v3.1: `ladder_key(để trống), node_key(hoặc ref),
  misc_ref, rungs[4], bottom_out, cong_no_luc`.
- Kiểm chéo: MỌI `misc_ref` xuất hiện trong distractor Trạm 3 phải có đúng một thang.
- Cuối ghi: "Giáo viên dạy giỏi phải duyệt thang trước khi đưa vào app."
