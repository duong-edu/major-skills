# Hai chế độ phân tích theo cấp học

Chọn chế độ theo lớp ở câu 1 khảo sát. Ranh giới: lớp 1–5 = chế độ Nền tảng; lớp 6–12 = chế độ Định lượng. Lớp 6 dùng chế độ Định lượng nhưng đọc thêm mục "vùng chuyển cấp" bên dưới.

## Chế độ NỀN TẢNG (tiểu học, lớp 1–5)

Phiếu đánh giá tiểu học Việt Nam (Thông tư 27) chấm theo mức **T (Hoàn thành tốt) / H (Hoàn thành) / C (Chưa hoàn thành)** cho môn học, **T (Tốt) / Đ (Đạt) / C (Cần cố gắng)** cho năng lực – phẩm chất, và chỉ vài môn có điểm KTĐK (thường Toán, Tiếng Việt, đôi khi Tiếng Anh/Tin). Ép dữ liệu này sang GPA là bóp méo — một bé toàn T không có nghĩa GPA 4.0.

Cách phân tích đúng:

1. **Lập lưới tín hiệu qua các năm.** Mỗi năm một cột; mỗi hàng một môn/năng lực/phẩm chất. Điền mức đạt + trích cụm từ khóa từ lời nhận xét (ví dụ: "sáng tạo nổi bật, phối hợp màu sắc" → tín hiệu Mỹ thuật).
2. **Tìm tín hiệu LẶP LẠI.** Lời khen cùng chủ đề xuất hiện ≥2 năm hoặc ≥2 nguồn (GVCN + giáo viên quốc tế, phiếu + PDR) = thế mạnh thật, đưa vào báo cáo với trích dẫn. Xuất hiện 1 lần = ghi nhận, không kết luận.
3. **Đọc cả phần chữ, không chỉ phần mức.** Với học sinh "toàn T" (rất phổ biến), toàn bộ giá trị phân biệt nằm trong lời nhận xét — đó là nơi giáo viên nói thật điều gì nổi bật. Mức C hoặc H lẻ loi giữa rừng T là tín hiệu đáng chú ý số một.
4. **Đầu ra định hướng phẩm chất, không nghề.** Báo cáo tiểu học trả lời: nền tảng nào đang vững (đọc, tự học, tự tin...), năng khiếu nào đang lộ, thói quen nào cần vun trong 1–2 năm tới. KHÔNG gợi ý nghề nghiệp, không xếp hạng, không "định vị cạnh tranh" — trẻ 7 tuổi không cần biết mình đứng đâu so với thế giới.
5. **Biểu đồ:** chỉ vẽ radar nếu có đủ điểm KTĐK có ý nghĩa; thường thì thay bằng "bảng tín hiệu 3 năm" trực quan hơn.

## Chế độ ĐỊNH LƯỢNG (THCS/THPT, lớp 6–12)

1. **Bảng điểm chuẩn hóa:** môn × năm, điểm cả năm là số chính; ghi cả HK1/HK2 khi chênh ≥1.0 (chênh lớn giữa hai kỳ là câu chuyện đáng kể).
2. **Quy đổi GPA 4.0 + percentage** theo `quy-doi-gpa.md`. Luôn ghi chú "ước lượng tham khảo, mỗi trường/nước quy đổi khác nhau (WES/ECE là bản chính thức)".
3. **Xu hướng** — vẽ `gpa_xu_huong()`. Chiều đi lên qua các năm đáng giá hơn con số tuyệt đối; nếu học sinh chuyển trường và điểm đổi chiều sau khi chuyển, nêu rõ (một cách trung lập — môi trường phù hợp hơn, không chê trường cũ).
4. **Biểu đồ theo môn** — `diem_mon_cot()`: cột theo môn, xếp theo nhóm chuẩn STEM (Toán, Lý, Hóa, Sinh, Tin) / Ngôn ngữ (Văn, Ngoại ngữ) / Xã hội (Sử, Địa, GDKT&PL, GDCD, GDQP nếu có điểm), cùng nhóm cùng tông màu, kèm đường mốc 8.0. Radar nhóm môn dùng kèm cho cái nhìn tổng. Môn chỉ có "Đạt" không vào biểu đồ.
5. **Soi riêng tiếng Anh:** điểm Ngoại ngữ + chứng chỉ nếu khảo sát khai. Tiếng Anh là rào cản TÁCH BIỆT với GPA cho mọi lộ trình quốc tế — nói rõ khoảng cách giữa hiện tại và mốc cần (ví dụ IELTS 6.5 cho đa số cửa du học).
6. **Định vị so mặt bằng:** sau quy đổi, nói thẳng học lực này rơi vào nhóm nào (một câu, có căn cứ): GPA ≥3.7 + xu hướng lên = cạnh tranh được học bổng/trường khá quốc tế; 3.2–3.7 = đủ điều kiện đa số đại học tầm trung thế giới, chưa đủ nổi bật cho học bổng lớn nếu không có yếu tố khác; <3.2 = cần kế hoạch cải thiện trước khi nói chuyện lộ trình quốc tế. Kèm câu chuẩn: "8,5/10 ở Việt Nam không tự động là 'giỏi' với chuẩn tuyển sinh quốc tế."

### Vùng chuyển cấp (lớp 6 và lớp 9–10)

Điểm lớp 6 thường tụt so với tiểu học (chuẩn chấm khác) — nếu thấy, ghi chú điều này để phụ huynh không hoảng. Lớp 9–10 là điểm rơi quyết định trường cấp 3: báo cáo cho lớp 9 nên nêu rõ "cửa sổ 12 tháng tới" vì đây là lúc mọi lựa chọn (trường, hệ, du học sớm) còn mở.

## Cả hai chế độ đều phải có

- Trả lời trực tiếp nỗi lo ở câu 2 khảo sát ngay phần đầu báo cáo.
- Ít nhất MỘT phát hiện "gia đình chưa để ý" (Bước 3.3 trong SKILL.md) — thường lấy từ nhận xét giáo viên hoặc môn lệch khỏi mặt bằng.
- Bài kiểm tra che tên trước khi xuất.
