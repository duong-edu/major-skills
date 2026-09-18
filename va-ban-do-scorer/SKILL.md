---
name: va-ban-do-scorer
description: Chấm chất lượng một Bản đồ học tập (sản phẩm Main của Trường Việt Anh) theo rubric 10 tiêu chí × 10 điểm, ngưỡng ĐẠT 85/100 — dùng để QC bản đồ trước khi giao gia đình, chấm bài "tốt nghiệp" của giáo viên chủ nhiệm trong khóa huấn luyện advisor, và rà hàng loạt khi cả khối cùng lập bản đồ. LUÔN dùng skill này khi người dùng nói "chấm bản đồ", "chấm điểm bản đồ học tập", "QC bản đồ", "bản đồ này đạt chưa", "chấm bài tốt nghiệp advisor", hoặc đưa một file Bản đồ học tập và hỏi chất lượng.
---

# Scorer — chấm chất lượng Bản đồ học tập

Đầu vào: MỘT file Bản đồ (docx/pdf/md/text — đọc toàn bộ trước khi chấm). Đầu ra: scorecard theo mẫu cuối file. Chấm theo `references/rubric-10-tieu-chi.md` — đọc rubric TRƯỚC mỗi lần chấm, không chấm theo trí nhớ.

Ba quy tắc chấm:

1. **Chấm bằng bằng chứng, không bằng cảm tình.** Mỗi tiêu chí phải trích được dòng/chi tiết cụ thể trong bản đồ làm căn cứ. Không tìm được bằng chứng = không có điểm phần đó. Người được chấm (GVCN) phải học được từ scorecard — bằng chứng cụ thể là thứ dạy họ, con số suông thì không.
2. **Nghiêm ở 3 tiêu chí sống còn (T1, T2, T10).** Bản đồ generic, bản đồ do người lớn viết hộ, và bản đồ lộ dữ liệu nhạy cảm là 3 lỗi giết sản phẩm — 3 tiêu chí này chấm gắt, không vớt.
3. **Điểm không phải đích.** Scorecard tồn tại để bản đồ sau tốt hơn bản đồ trước — phần "3 việc sửa ưu tiên" quan trọng hơn con số tổng. Viết 3 việc đó cụ thể đến mức làm được ngay trong 30 phút.

## Hai chế độ chấm — xác định TRƯỚC khi chấm

Nhìn bản đồ để xác định giai đoạn:

- **Chế độ BẢN CHÍNH THỨC** (đã qua buổi khám phá + ba bên, sẵn sàng giao gia đình): chấm đủ 10 tiêu chí, dùng thang kết luận dưới đây.
- **Chế độ BẢN NHÁP nhịp 1** (còn nhãn `[chờ em điền]`, học sinh chưa làm phiếu khám phá): KHÔNG chấm T3/T4/T5/T7 bằng điểm — các tiêu chí đó cần lời học sinh, thứ quy trình cấm advisor tự tạo; bản nháp làm đúng sẽ oan nếu chấm đủ thang. Thay vào đó chấm "chất lượng giàn giáo": T1, T2, T6, T8, T9, T10 như thường + kiểm tra placeholder đặt đúng chỗ, quota 4D đã khóa sẵn trong khung phần 4, câu hỏi thay chỗ trống (không bỏ trống lặng lẽ). Kết luận nhị phân: **ĐỦ / CHƯA ĐỦ điều kiện sang nhịp 2**, kèm việc cần làm. Lý do chế độ này tồn tại: nếu chấm bản nháp bằng thang đầy đủ, advisor sẽ học được bài học sai — viết hộ học sinh 5 mục tiêu để lấy điểm T3/T4, tức rubric thưởng cho chính lỗi giết sản phẩm.

## Thang kết luận (chế độ bản chính thức)

- **90–100 · ĐẠT — XUẤT SẮC:** dùng làm bài mẫu huấn luyện.
- **85–89 · ĐẠT:** giao gia đình được.
- **70–84 · CHƯA ĐẠT — SỬA ĐƯỢC:** liệt kê 3 việc sửa, hẹn chấm lại; thường sửa trong 1 buổi.
- **<70 · CHƯA ĐẠT — LÀM LẠI CÓ HƯỚNG DẪN:** lỗi nằm ở quy trình (thiếu phiếu khám phá, viết hộ...), không phải câu chữ; chỉ ra bước quy trình cần làm lại, đừng bảo "viết lại cho hay".
- **Phủ quyết (tự động CHƯA ĐẠT bất kể tổng điểm):** T10 (an toàn dữ liệu) < 5, hoặc T2 (học sinh làm chủ) = 0. Ghi rõ lý do phủ quyết đầu scorecard.

## Mẫu scorecard đầu ra (dùng đúng khung)

```
SCORECARD BẢN ĐỒ HỌC TẬP
Bản đồ của: [tên gọi + lớp] · Advisor: [tên] · Ngày chấm: [ngày] · Người chấm: va-ban-do-scorer

TỔNG: [X]/100 → [ĐẠT — XUẤT SẮC / ĐẠT / CHƯA ĐẠT — SỬA ĐƯỢC / CHƯA ĐẠT — LÀM LẠI]
[Dòng phủ quyết nếu có]

| # | Tiêu chí | Điểm | Bằng chứng / lý do trừ |
|---|----------|------|------------------------|
| T1..T10 | ... | x/10 | trích cụ thể |

3 VIỆC SỬA ƯU TIÊN (cụ thể, làm được trong 30'):
1. ...
2. ...
3. ...

1 ĐIỀU LÀM TỐT NHẤT (giữ lại ở bản đồ sau): ...
```

Chấm nhiều bản cùng lúc (rà cả khối): thêm bảng tổng hợp xếp theo điểm + nhận xét lỗi LẶP LẠI toàn khối (lỗi xuất hiện ≥30% số bản là lỗi huấn luyện, không phải lỗi cá nhân — báo chủ dự án chỉnh khóa huấn luyện thay vì sửa từng người).
