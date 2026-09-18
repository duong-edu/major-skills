---
name: so-sanh-truong-viet-anh
description: >-
  So sánh sản phẩm giáo dục của Trường Việt Anh với một trường đối thủ cụ thể (hoặc trường công lập
  TP.HCM nếu không nêu đối thủ), theo từng khối lớp, giúp phụ huynh chọn trường cho con. Skill đã đóng
  gói sẵn chương trình, học phí, thời khóa biểu và phương pháp Việt Anh; người dùng chỉ cần đưa thông
  tin đối thủ (thời khóa biểu, học phí, lịch ngoại khóa — text/ảnh/PDF/Word/Excel/link). Kết quả: so
  sánh 4 mảng (Kiến thức học thuật, Kỹ năng, Tiếng Anh, Thể chất), phân tích Khoảng trống theo khung
  WEF, quy đổi giá trị tài chính + ROI lương, nhiều biểu đồ, đề xuất trường phù hợp với ai. LUÔN dùng
  khi nói: "so sánh Việt Anh với trường X", "so sánh trường", "Việt Anh vs [trường]", "trường nào tốt
  hơn cho con", "so sánh học phí/chương trình trường", "bảng so sánh chọn trường", hoặc bất kỳ yêu cầu
  đối chiếu Việt Anh với trường khác để tư vấn tuyển sinh — kể cả khi chỉ đưa thông tin một trường và
  hỏi "trường này so với Việt Anh thế nào".
---

# So sánh Trường Việt Anh với Trường đối thủ

## Mục tiêu & người dùng

Tạo một bản **so sánh khách quan, thuyết phục, dựa trên dữ kiện** giữa **Trường Việt Anh** và **một trường đối thủ cụ thể**, để **phụ huynh ra quyết định đúng về việc chọn trường cho con**. Người đọc cuối cùng là phụ huynh; người dùng skill thường là anh Dương hoặc tư vấn viên tuyển sinh (admission).

Nguyên tắc nền tảng: **trung thực và chính trực** (đúng giá trị cốt lõi Việt Anh). Skill KHÔNG bịa số liệu, KHÔNG hạ thấp đối thủ bằng thông tin sai. Khi Việt Anh thực sự mạnh hơn ở một mảng, chứng minh bằng thời lượng – cách tổ chức – giá trị nhận được – quy đổi tài chính. Khi đối thủ có điểm mạnh, ghi nhận trung thực. Một bản so sánh đáng tin (thừa nhận cả điểm yếu của Việt Anh) thuyết phục phụ huynh hơn nhiều một bản một chiều.

## Dữ liệu Việt Anh đã có sẵn (KHÔNG cần hỏi người dùng)

Skill đã đóng gói sẵn chương trình, phương pháp, **học phí chính xác từng khối**, **thời khóa biểu (số tiết/tuần từng cấp)**, sĩ số, và số liệu nguồn uy tín. **Luôn đọc 3 file này trước khi so sánh:**

- `references/viet-anh-noi-dung.md` — chương trình theo 4 mảng × cấp; **TKB & số tiết/tuần chính xác** (THCS thường 9 tiết tiếng Anh gồm 6 GVNN; THCS OIC 10 tiết + nhiều môn bằng tiếng Anh; THPT 11 tiết; mầm non ~6 tiết); sĩ số **24 HS/lớp**; 4 phương pháp dạy học, IELTS/PDR (mầm non: Plan-Do-**Recall** hằng ngày; tiểu học: Plan-Do-**Review** hằng ngày; THCS/THPT: Plan-Do-**Review** hằng tuần), Foundation, 5 giá trị, 16 kỹ năng, thể thao bắt buộc, dinh dưỡng.
- `references/viet-anh-hoc-phi.md` — học phí chính xác lớp 1–12 (VAPN & VAGV/VABT), nội trú, ăn uống, mầm non, rèn luyện thêm, học bổng (2026-2027). Bộ **neo đơn giá** để quy đổi.
- `references/khoang-trong-va-gia-tri.md` — khung **Khoảng trống WEF Davos** + số liệu có nguồn; **mốc trường công** (GDPT 2018 + sĩ số TP.HCM); **ROI lương** (tiếng Anh/FDI vs nội địa); kỹ thuật **"Những con số biết nói"**; đặc tả **biểu đồ**.

Lưu ý: số liệu cập nhật theo năm. Nếu người dùng cung cấp bảng phí/TKB Việt Anh mới hơn, **ưu tiên số người dùng đưa** + ghi năm.

## Thông tin cần từ người dùng (về trường đối thủ)

Đầu vào về **trường đối thủ** có thể đến ở bất kỳ định dạng nào — **dán text, ảnh chụp (TKB/bảng phí), file PDF/Word/Excel, hoặc link website**. Xử lý tương ứng: đọc ảnh trực tiếp, dùng tool đọc PDF/Excel, hoặc fetch link.

Ba nhóm thông tin đối thủ cần thu thập (nếu thiếu, hỏi hoặc tự tìm trên website):

1. **Thời khóa biểu** (bắt buộc) — số tiết/buổi mỗi tuần, phân bổ các môn/mảng, giờ học, có bán trú/nội trú không.
2. **Danh mục học phí** (bắt buộc) — học phí theo khối, phí cơ sở vật chất, ăn uống, các phí khác, học bổng.
3. **Lịch ngoại khóa / chương trình bổ trợ** (tùy chọn) — CLB, dã ngoại, sự kiện, chương trình kỹ năng, tiếng Anh tăng cường.

**Trước khi bắt đầu, xác nhận 3 điều với người dùng** (nếu chưa rõ trong yêu cầu): (a) **tên trường đối thủ**; (b) **khối lớp trọng tâm** cần so sánh (vd lớp 1, lớp 6, lớp 10); (c) **cơ sở Việt Anh nào** để đối chiếu — VAPN (Phú Nhuận) hay VAGV/VABT (Gò Vấp/Bình Tân, có Oxford OIC), vì học phí và chương trình khác nhau. Nếu phụ huynh không chỉ định, mặc định chọn cơ sở Việt Anh **cùng phân khúc địa lý/giá** với đối thủ và nêu rõ giả định.

Nếu dữ liệu đối thủ thiếu một mảng (vd không có lịch ngoại khóa), **vẫn so sánh các mảng còn lại** và ghi rõ "đối thủ chưa công bố thông tin về…" thay vì suy diễn bất lợi cho họ.

**Mặc định khi KHÔNG có thông tin đối thủ:** nếu người dùng chỉ nói "so sánh" mà không đưa dữ liệu trường nào, **tự tìm thời khóa biểu + sĩ số trường công lập tại TP.HCM** ở khối tương ứng (web search) làm đối tượng so sánh, ghi rõ nguồn + năm. Nếu không tìm được TKB trường cụ thể, dùng mốc GDPT 2018 trong `khoang-trong-va-gia-tri.md`.

## Khung phân tích

Đọc `references/khung-so-sanh.md` (chi tiết 7 bước) và `references/khoang-trong-va-gia-tri.md` (Khoảng trống WEF + ROI + Making Numbers Count + biểu đồ). Tóm tắt:

1. **Chuẩn hóa dữ liệu** hai trường (thời lượng tiết/tuần + chi phí trọn gói/năm cùng đơn vị). Không có đối thủ → tìm trường công TP.HCM.
2. **So sánh 4 mảng** (Kiến thức / Kỹ năng / Tiếng Anh / Thể chất), đối chiếu **thời lượng + chiều sâu**, **dịch chênh lệch thành bội số** (tiếng Anh 11 vs 3 → "1 năm ≈ 3,7 năm"; sĩ số 24 vs 48 → "gấp đôi sự quan tâm"). Nhấn: **Kiến thức** so tầng tư duy **Bloom** (công dừng ở Vận dụng vs VA Active Learning chạm Phân tích–Sáng tạo); **Kỹ năng lồng ghép xuyên mọi môn** + Morning Meeting/PDR/TLIM/Foundation/sự kiện HS → tỷ lệ kỹ năng rất cao, map vào khung WEF; **Thể chất** = 5 nguyên tắc sống khỏe + thể thao hằng ngày + Olympic. Vẽ biểu đồ.
3. **PHÂN TÍCH KHOẢNG TRỐNG (đặt TRƯỚC giá trị)** — với mỗi nội dung đối thủ thiếu: (a) đó là khoảng trống so với khung **WEF Davos** (dẫn số: 70% DN cần tư duy phân tích, 39% kỹ năng lỗi thời đến 2030, 59/100 người phải học lại…); (b) thiếu nó bất lợi gì cho con (việc làm/thu nhập/hội nhập) + số + nguồn + biểu đồ; (c) Việt Anh lấp ra sao.
4. **Điểm mạnh / cần cân nhắc** mỗi trường (trung thực cả hai). Việt Anh soi 5 trục: thời lượng · cách tổ chức · giá trị học sinh nhận · **giá trị của giá trị (dài hạn)** · chi phí.
5. **Giá trị của giá trị** — (a) quy đổi tài chính phần chênh lệch ra tiền mua lẻ ngoài; (b) **ROI lương**: tiếng Anh sớm + phát âm chuẩn → công ty đa quốc gia (cao hơn ~26–33%; premium tiếng Anh 30–50%); (c) **ROI sức khỏe**: thể thao hằng ngày → +3,4–4,7 năm tuổi thọ, 5 thói quen lành mạnh +10 năm (WHO/PLOS/Harvard); (d) **Thời gian không lấy lại được**: cửa sổ vàng học tiếng Anh (~17–18 tuổi), não 90% trước 5 tuổi, Heckman ROI sớm cao nhất — nhấn tính cấp thiết, trung thực. Ghi "ước tính tham khảo" + nguồn. Vẽ biểu đồ ROI.
6. **Mở rộng khối → cấp → toàn hành trình K-12** (tổng đầu tư & tổng giá trị tích lũy, dùng học phí chính xác từng khối; timeline cột mốc giá trị).
7. **Đề xuất "phù hợp với ai" theo MỤC TIÊU** — 2 ma trận: (A) mục tiêu học tập tiếp theo (du học / du học học bổng / ngành hiện đại vs thi đại học công lập, ngành đặc thù công an–quân đội–hành chính–văn hóa dân tộc, gần nhà); (B) mục tiêu nghề nghiệp (doanh nhân / chuyên gia quốc tế / thu nhập cao vs nghề ổn định địa phương: công chức, chính trị gia, nghệ nhân). + 2–3 chân dung. Trung thực: Việt Anh giữ cả 2 cửa (thi trong nước + quốc tế); nếu mục tiêu là nghề địa phương + ngân sách tối giản → nói thẳng trường công hợp lý hơn. (Chi tiết: `khung-so-sanh.md` Bước 7.)

## Định dạng đầu ra: PDF trình bày đẹp

Đầu ra mặc định là **một file PDF đẹp**, dành cho phụ huynh (gửi Zalo/email hoặc in màu). Quy trình tạo:

1. Viết toàn bộ nội dung so sánh thành **một file HTML hoàn chỉnh, tự chứa** (CSS inline, không phụ thuộc internet), theo cấu trúc báo cáo ở `references/khung-so-sanh.md` (mục "Cấu trúc bản PDF") và bảng màu/giao diện ở `assets/pdf-style.md`.
2. Chuyển HTML → PDF. Cách ổn định trong sandbox: dùng Chromium headless qua Playwright Node — `npm i -g playwright && npx playwright install chromium` rồi script `page.pdf({format:'A4', printBackground:true})`. Nếu không cài được, fallback Python `weasyprint` (`pip install weasyprint --break-system-packages`). Nếu cần trình bày mỹ thuật cao, có thể dùng skill **canvas-design** hoặc **pdf**.
3. Đặt tên file: `So-sanh-VietAnh-vs-[TenDoiThu]-[Khoi]-[YYYY-MM-DD].pdf`.
4. Lưu vào thư mục làm việc của người dùng và `present_files` để anh xem.

Bản PDF phải có (đúng thứ tự 11 phần trong `khung-so-sanh.md`): **bìa NỀN TRẮNG, tên báo cáo màu đỏ**; **TRANG SUMMARY TOÀN BIỂU ĐỒ ("hiểu trong 1 phút")**; tóm tắt 4 mảng (chữ); bảng học phí; chi tiết 4 mảng; phân tích Khoảng trống WEF; giá trị của giá trị (quy đổi + ROI lương + sức khỏe + thời gian); điểm mạnh/cần cân nhắc; hành trình K-12; đề xuất (2 ma trận mục tiêu); chân trang nguồn. **Bắt buộc ≥ 4–6 biểu đồ** vẽ **SVG inline** (theo quy tắc chống mất chữ), màu thương hiệu, mỗi biểu đồ có nguồn nhỏ; **tiêu đề lớn màu đỏ `#C8102E`, NỀN TRẮNG toàn bộ** (dễ in). Áp dụng **"Những con số biết nói"**. Sau khi tạo PDF, **render PNG kiểm tra** mất chữ/tofu/tràn trang.

## Kiểm tra trước khi giao (bắt buộc)

Trước khi xuất bản, tự rà:
- [ ] Mọi con số học phí/thời lượng có nguồn (từ file Việt Anh đã đóng gói hoặc input đối thủ); không có số "thả nổi".
- [ ] Phần quy đổi tài chính + ROI lương đều ghi rõ giả định + đơn giá/nguồn tham khảo.
- [ ] Có phần **Phân tích Khoảng trống (WEF Davos)** với số liệu + nguồn, đặt trước phần giá trị.
- [ ] Có **≥ 4–6 biểu đồ**, mỗi biểu đồ có nguồn nhỏ; có áp dụng "Những con số biết nói" (bội số).
- [ ] **Biểu đồ KHÔNG mất chữ**: `overflow="visible"`, chữ cách mép viewBox ≥ 12, nhãn không tràn/đè; đánh số biểu đồ liên tục đúng thứ tự (xem quy tắc chống mất chữ trong `khoang-trong-va-gia-tri.md` Phần 5). Mở PDF kiểm tra lại.
- [ ] Phần đề xuất có **2 ma trận mục tiêu** (học tập tiếp theo + nghề nghiệp), trung thực cả hướng nội địa/địa phương.
- [ ] Mọi số liệu/trích dẫn nguồn uy tín ghi đúng (WEF 2025, EF EPI, Talentnet–Mercer, GDPT 2018) — không trích sai.
- [ ] Có nêu điểm mạnh của **cả** đối thủ (không một chiều) → tăng độ tin cậy.
- [ ] So sánh đúng **cùng cơ sở Việt Anh** đã chọn, đúng khối lớp; sĩ số 24 vs trường công.
- [ ] Có đủ 7 bước; mở rộng khối → cấp → hành trình K-12.
- [ ] Văn phong dành cho phụ huynh: rõ ràng, ấm áp, không thuật ngữ rối; tôn trọng đối thủ.

## Tài liệu tham khảo trong skill
- `references/viet-anh-noi-dung.md` — chương trình, 4 phương pháp, **TKB số tiết/tuần**, sĩ số, 4 mảng × cấp.
- `references/viet-anh-hoc-phi.md` — học phí chính xác lớp 1–12, dịch vụ, học bổng + neo đơn giá.
- `references/khoang-trong-va-gia-tri.md` — Khoảng trống WEF Davos + nguồn, mốc trường công, ROI lương, "Những con số biết nói", đặc tả biểu đồ.
- `references/khung-so-sanh.md` — phương pháp 7 bước, đơn giá thị trường, cấu trúc PDF có biểu đồ.
- `assets/pdf-style.md` — bảng màu, typography, layout PDF.
