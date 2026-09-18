---
name: major-cfo
description: Phân tích chênh lệch tài chính và đọc báo cáo cho Major Education — phân rã sĩ số/học phí/cơ cấu cấp học, phân rã chi phí nhân sự, ngưỡng trọng yếu, khung viết diễn giải. Nạp khi làm báo cáo tài chính, so sánh thực tế với ngân sách, hoặc phân tích biến động chi phí.
---

# Phân tích tài chính Major Education

Nguồn gốc: phát triển từ skill variance-analysis của anthropics/
knowledge-work-plugins, bổ sung bối cảnh trường học Việt Nam.

## Luật trước tiên
Skill này hỗ trợ phân tích, KHÔNG đưa lời khuyên đầu tư hay quyết định
tài chính. Kết quả là đầu vào cho quyết định của con người.
Không có số thì ghi rõ "chưa có dữ liệu", không ước lượng thay.
Mọi con số phải kèm nguồn: tên bảng, kỳ, ngày lấy dữ liệu.
Đơn vị thống nhất: VND, ghi theo triệu hoặc tỷ, không dùng USD trừ khi
được yêu cầu.

## Đặc thù phải nhớ trước khi phân tích
Năm học Việt Anh dài 10 tháng, không phải 12 — mọi so sánh theo tháng
phải chuẩn hoá theo số tháng học, không chia đều cho 12.
80% học sinh nhập học tháng 8, 10% tháng 12, phần còn lại rải rác.
Riêng mầm non nhập học quanh năm, giảm dần T10–T2, tăng từ T3.
Doanh thu không đồng nhất giữa các cấp: học phí lớp 10 niêm yết
124.900.000đ/năm, mầm non thấp hơn nhiều. Vì vậy cơ cấu cấp học
(mix) là biến số lớn ngang với sĩ số.
Chính sách hoàn phí 4 tuần đầu tạo rủi ro đảo doanh thu trong tháng
đầu mỗi kỳ nhập học — tách riêng khi phân tích.

## Phân rã doanh thu: ba thành phần, không phải hai
Chênh lệch doanh thu = tác động SĨ SỐ + tác động HỌC PHÍ + tác động
CƠ CẤU.
Tác động sĩ số: (sĩ số thực tế − sĩ số kế hoạch) × học phí bình quân
kế hoạch.
Tác động học phí: (học phí bình quân thực tế − kế hoạch) × sĩ số
thực tế.
Tác động cơ cấu: phần còn lại — phản ánh dịch chuyển giữa các cấp học,
giữa nội trú và bán trú, giữa các cơ sở.
Luôn tách theo ba chiều: cấp học, cơ sở, hình thức học. Một con số
tổng không nói được gì.

## Phân rã chi phí nhân sự
Chi phí nhân sự là khoản lớn nhất. Phân rã thành năm phần: số lượng
nhân sự, mức lương, cơ cấu vị trí, thời điểm tuyển, và biến động
nghỉ việc. Nêu rõ phần nào do quyết định quản trị, phần nào do
thị trường.

## Phân rã chi phí vận hành
Chia theo bản chất, không theo phòng ban: theo nhân sự, theo quy mô
học sinh, chi tuỳ ý, chi theo hợp đồng, chi một lần, và lệch thời điểm.
Cấm gộp "chi phí khác" quá 5% tổng chi.

## Ngưỡng trọng yếu — khi nào phải điều tra
So với ngân sách: lệch trên 10%.
So với cùng kỳ năm trước: lệch trên 15%.
So với dự báo gần nhất: lệch trên 5%.
So với tháng liền trước: lệch trên 20%.
Dưới ngưỡng thì ghi nhận, không mở điều tra — tránh tốn công vào nhiễu.

## Thứ tự ưu tiên điều tra
Số tiền tuyệt đối lớn nhất trước. Rồi đến tỷ lệ lệch lớn nhất. Rồi đến
lệch ngược chiều dự kiến. Rồi đến lệch mới xuất hiện. Cuối cùng là
lệch nhỏ nhưng lặp lại nhiều kỳ.

## Khung viết diễn giải
Mỗi diễn giải 2–4 câu, đạt sáu tiêu chí: cụ thể, có số, chỉ ra nguyên
nhân, nói được ảnh hưởng tới kỳ sau, nêu hành động, và ngắn.

Sáu lỗi cấm:
Lý luận vòng tròn — "doanh thu cao hơn vì doanh thu tăng".
Từ mơ hồ — "do một số yếu tố", "do thị trường".
Nói "lệch thời điểm" mà không nói lệch sang kỳ nào.
Nói "một lần" mà không mô tả đó là khoản gì.
Gộp nhiều nguyên nhân thành một dòng không phân rã.
Đưa con số mà không nói so với cái gì.

## Bảng cầu nối
Khi trình bày biến động từ kỳ trước sang kỳ này, dùng bảng cầu nối tối
đa 5–8 yếu tố, sắp theo độ lớn, và BẮT BUỘC kiểm tra: số đầu kỳ cộng
các yếu tố phải bằng đúng số cuối kỳ. Lệch một đồng cũng phải tìm ra.

## Chỉ số nền của Major — dùng để đối chiếu, không phải mục tiêu cứng
CAC khoảng 25 triệu/học sinh. Biên đóng góp khoảng 92 triệu/học sinh/
năm. Tỷ lệ tái tục khoảng 86%. CPL mục tiêu 3 triệu/Qlead.
Khi một chỉ số lệch quá 20% so với các số nền này, nêu lên như một
phát hiện, kèm câu hỏi chứ không kèm kết luận.

## Trước khi bàn giao
Đối chiếu skill major-smac: đủ Specific chưa, có theo đúng quy trình
chưa, có mâu thuẫn với báo cáo kỳ trước không.
