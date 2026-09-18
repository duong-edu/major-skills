# Quy đổi thang điểm 10 (Việt Nam) sang GPA 4.0 & Percentage

Trường nước ngoài không đọc thang 10 của VN. Phải quy đổi trước khi so sánh yêu cầu đầu vào.

## Bảng quy đổi tham khảo (phổ biến nhất)

| Điểm 10 (VN) | Percentage | GPA 4.0 | Xếp loại |
|---|---|---|---|
| 9.0 – 10 | 90–100% | 4.0 | Xuất sắc |
| 8.0 – 8.9 | 80–89% | 3.5 – 3.9 | Giỏi |
| 7.0 – 7.9 | 70–79% | 3.0 – 3.4 | Khá |
| 6.5 – 6.9 | 65–69% | 2.5 – 2.9 | Trung bình khá |
| 5.5 – 6.4 | 55–64% | 2.0 – 2.4 | Trung bình |
| < 5.5 | < 55% | < 2.0 | Yếu |

## Cách tính GPA tổng
1. Quy mỗi môn (hoặc mỗi năm) sang GPA 4.0 theo bảng trên.
2. GPA tổng = trung bình cộng (hoặc trung bình có trọng số theo số tín chỉ/số tiết nếu biết).
3. Ghi rõ GPA đang tính trên cơ sở nào (tất cả các năm / chỉ 3 năm THPT / v.v.).

## Lưu ý quan trọng
- Đây là **quy đổi tương đối**, mỗi trường/nước có cách quy đổi riêng — một số dùng WES, ECE (đánh giá chính thức, tốn phí). Nêu rõ trong báo cáo rằng con số là ước lượng.
- Nhiều trường top nhìn **xu hướng điểm** (đi lên qua các năm) chứ không chỉ GPA trung bình. Nếu điểm con cải thiện rõ theo năm → nhấn mạnh điểm này, và vẽ bằng hàm `gpa_xu_huong()` trong `scripts/ve_bieu_do.py`.
- Tiếng Anh học thuật (IELTS/TOEFL) là **rào riêng, tính tách biệt** — GPA cao không bù được IELTS thấp.
