# Lọc thông tin nhạy cảm + Checklist QC

## 1. Danh sách trường PHẢI CHẶN khỏi báo cáo

Học bạ và phiếu đánh giá thật chứa các trường dưới đây. Không trường nào được xuất hiện trong báo cáo, trong tên file, hay bất kỳ tài liệu nào rời khỏi hồ sơ đơn hàng. Lý do chung: báo cáo có thể được phụ huynh chia sẻ tiếp (cho người thân, lên mạng) — mọi thứ trong đó phải an toàn khi bị chia sẻ.

| Trường | Có ở đâu | Vì sao chặn |
|---|---|---|
| Mã định danh Bộ GD&ĐT, mã số học sinh (MSHS) | Phiếu đánh giá, học bạ | Định danh suốt đời của trẻ |
| Ảnh thẻ học sinh | Trang bìa học bạ | Hình ảnh trẻ em |
| Ngày sinh đầy đủ | Học bạ | Ghép với tên = định danh; báo cáo chỉ cần lớp |
| Địa chỉ nhà | Học bạ | An toàn của trẻ |
| Họ tên + nghề nghiệp cha mẹ | Học bạ | Riêng tư của người lớn, không liên quan phân tích |
| SĐT, chữ ký, họ tên giáo viên | Mọi phiếu | Riêng tư của giáo viên; trích nhận xét thì ghi "giáo viên chủ nhiệm lớp X nhận xét", không nêu tên |
| Chiều cao, cân nặng, ghi chú sức khỏe | Phiếu tiểu học | Dữ liệu sức khỏe trẻ em — nhạy cảm nhất trong toàn bộ hồ sơ; kể cả khi liên quan (thể chất), báo cáo không nhắc lại, chỉ tư vấn viên trao đổi riêng nếu gia đình chủ động hỏi |

Trong báo cáo, con được gọi bằng **tên gọi** (tên riêng hoặc tên thân mật phụ huynh dùng trong khảo sát) + lớp. Tên trường hiện tại chỉ ghi nếu cần cho phân tích (ví dụ chuyển trường ảnh hưởng xu hướng) và trung lập.

## 2. Disclaimer chuẩn (đặt cuối mọi báo cáo, cỡ chữ nhỏ hơn 1 bậc)

> Báo cáo này là tư vấn giáo dục tham khảo dựa trên dữ liệu gia đình cung cấp, không phải đánh giá tâm lý hay cam kết kết quả học tập. Quy đổi GPA là ước lượng; bản quy đổi chính thức do các tổ chức như WES/ECE thực hiện. Số liệu chi phí (nếu có) thay đổi theo thời gian — gia đình kiểm tra lại nguồn chính thức trước khi quyết định. Dữ liệu của con chỉ dùng để lập báo cáo này và được bảo mật theo chính sách của Bản đồ học tập.

## 3. Checklist QC 12 điểm — đạt cả 12 mới gửi

1. Mọi con điểm trong báo cáo khớp bảng đã được phụ huynh xác nhận; không còn ô `[?]`.
2. Không sót trường nào trong danh sách chặn (rà cả biểu đồ — tiêu đề biểu đồ hay dính họ tên đầy đủ).
3. Trả lời trực tiếp nỗi lo câu 2 khảo sát trong trang đầu.
4. Có ít nhất 1 phát hiện "gia đình chưa để ý", có trích dẫn cụ thể.
5. Qua bài kiểm tra che tên (không dùng được cho bạn cùng lớp).
6. Đúng chế độ cấp học (tiểu học không có GPA/xếp hạng; THCS-THPT có đủ GPA + xu hướng + định vị).
7. Nếu có ý định du học: trang reality-check có mặt, cờ khả thi chấm trung thực (không nâng cờ để dễ nghe).
8. Không câu chữ nào cam kết kết quả, chẩn đoán tâm lý, hay hù dọa.
9. Đúng brand: Navy #26275D chủ đạo, vàng #F9DD0E chỉ điểm nhấn, font đúng, có disclaimer, trang kết "1/4 con bạn" + đúng MỘT CTA.
10. Đã render ra ảnh xem bằng mắt: không lỗi font tiếng Việt, bảng không tràn, biểu đồ hiển thị đúng — và điểm theo môn dùng biểu đồ CỘT nhóm (`diem_mon_cot`), không có biểu đồ đường nhiều môn.
11. Mọi con số đối chiếu quốc gia/quốc tế đều có nguồn + năm, và so đúng cùng thước đo (quy tắc trong `benchmark-va-trich-dan.md`); tổng 2–4 số, không nhồi.
12. Tài nguyên miễn phí: tối đa 3, mỗi cái gắn đúng một vùng cần vun, chỉ lấy từ danh mục đã duyệt (`tai-nguyen-mien-phi.md`).

## 4. Sự cố thường gặp

- **Phụ huynh không phản hồi xác nhận bảng điểm sau 24h:** nhắc 1 lần kèm ghi chú "các ô [?] em sẽ để trống trong báo cáo nếu không có xác nhận"; sau 36h, xuất báo cáo với ô [?] ghi "chưa xác nhận được" — đúng SLA quan trọng hơn đủ 100% ô.
- **Ảnh quá mờ không đọc nổi:** xin chụp lại NGAY khi nhận đơn (Bước 0), kèm hướng dẫn 1 dòng: đặt phẳng, đủ sáng, chụp thẳng từng trang.
- **Phụ huynh khai điểm miệng khác ảnh:** dùng số trong ảnh, ghi chú chênh lệch cho tư vấn viên.
