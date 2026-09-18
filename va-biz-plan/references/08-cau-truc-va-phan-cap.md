# Cấu trúc chín tầng và phân cấp giữa tập đoàn với đơn vị

## Phần 1 — Chín tầng mục tiêu

Cấu trúc này ngăn việc lẫn lộn giữa la bàn với đích đến. Bốn khái niệm hay bị dùng thay nhau, và mỗi lần dùng sai là một lần cả hệ thống chỉ số lệch đi. Chín tầng này ánh xạ trực tiếp vào 13 khối (0–12) của `01-khung-12-khoi.md` — dùng tệp này để hiểu **vì sao** khung có hình dạng đó, dùng tệp kia để lấy **câu hỏi phỏng vấn** cụ thể.

| # | Tầng | Nhịp thay đổi | Trả lời câu hỏi | Tương ứng khối |
|---|---|---|---|---|
| **0** | **Nguyên tắc vận hành (SMAC)** | Nhiều năm | Được phép ra quyết định theo cách nào | Khối 0 |
| 1 | **Sứ mệnh** | Vĩnh viễn | Đơn vị tồn tại để làm gì | Khối 3 (Lời hứa) |
| 2 | **Tầm nhìn / Lời hứa có thể sai** | 10–20 năm | Sẽ trở thành gì, phục vụ ai | Khối 3 |
| 3 | **Chẩn đoán** | Mỗi năm | Hôm nay đang ở đâu, ràng buộc thật là gì | Khối 2 |
| 4 | **Bắc Đẩu** | Ổn định nhiều năm | Đang đi đúng hướng không | Khối 7 |
| 5 | **Mục tiêu năm** | 1 năm | Năm nay đi tới đâu | Khối 7 |
| 6 | **Cược** | 1 năm | Đổ nguồn lực bất thường vào đâu | Khối 5 |
| 7 | **Mục tiêu quý** | 3 tháng | Ba tháng tới việc quan trọng nhất là gì | Khối 9 (thử nghiệm quý) |
| 8 | **Lead measure** | Tuần | Tuần này làm gì | Khối 7 |
| 9 | **Cam kết cá nhân** | Tuần | Mỗi người làm gì | Khối 1 / họp WIG, `06-nhip-van-hanh.md` |

**SMAC không phải một tầng — nó cắt ngang cả chín tầng, tức cả 12 khối.** Vị trí trong tài liệu: ngay sau Trang Cam kết, trước phần Chẩn đoán. Khi kế hoạch mâu thuẫn với SMAC, SMAC thắng.

### Phân biệt bốn khái niệm hay bị lẫn

| Khái niệm | Là gì | Đổi bao lâu một lần |
|---|---|---|
| **Bắc Đẩu** | Một **con số** đo giá trị khách hàng nhận được | Nhiều năm |
| **Mục tiêu năm** | Một mục tiêu dạng **"từ X đến Y trước ngày Z"** — thường là lag measure | Mỗi năm |
| **Cược** | Nơi đổ nguồn lực bất thường, **có thể sai** | Mỗi năm |
| **Lead measure** | Việc đội tác động trực tiếp hằng tuần, **dự báo được mục tiêu năm** | Mỗi quý |

## Phần 2 — Bắc Đẩu phải là một CON SỐ ⛔

Đây là lỗi phổ biến nhất khi lập kế hoạch, và nó làm hỏng cả hệ chỉ số.

> **Sai:** *"Bắc Đẩu của chúng ta là trở thành hệ thống giáo dục hàng đầu."*
> **Đúng:** *"Bắc Đẩu là tỷ lệ giới thiệu — % gia đình hiện hữu giới thiệu ít nhất một gia đình mới trong 12 tháng. Mục tiêu: 30%/năm."* — đây chính là Bắc Đẩu hiện hành của Major, theo tài liệu 28/7/2026.

**Định nghĩa chuẩn (Sean Ellis, người khai sinh khái niệm):** *"chỉ số duy nhất nắm bắt tốt nhất giá trị cốt lõi mà sản phẩm mang lại cho khách hàng."*

**Cấu trúc bắt buộc:** Bắc Đẩu ← lead measure của từng đơn vị ← công việc hằng ngày. **Đội không bao giờ chạm trực tiếp vào Bắc Đẩu — họ chỉ dịch chuyển lead measure của mình.** Đơn vị **không tự chọn lại Bắc Đẩu** — chỉ dịch nó thành 1 lead measure riêng.

Nếu người dùng đưa một câu tầm nhìn vào ô Bắc Đẩu, hỏi lại: *"Nếu điều đó đang xảy ra, con số nào sẽ tăng?"* Câu trả lời chính là Bắc Đẩu — nhưng nhắc người dùng: **Bắc Đẩu là của tập đoàn, đã có sẵn (tỷ lệ giới thiệu 30%/năm)**, câu hỏi này chỉ dùng để kiểm tra hiểu đúng khái niệm, không phải để họ tự đặt Bắc Đẩu mới cho đơn vị mình.

### Sáu tiêu chí kiểm tra Bắc Đẩu

| # | Tiêu chí | Câu hỏi kiểm |
|---|---|---|
| 1 | Một con số | Có phải một chỉ số duy nhất không? |
| 2 | Đo giá trị cho **khách hàng** | Nếu con số này tăng, học sinh và phụ huynh được lợi gì? |
| 3 | Ổn định nhiều năm | Có còn đúng sau 5 năm không? |
| 4 | **Dịch chuyển được quanh năm** | Tháng 3 có ai làm được gì để nó tăng không? |
| 5 | Dự báo được doanh thu | Mỗi đơn vị tăng tương ứng bao nhiêu tiền? |
| 6 | Ai cũng hiểu | Cô giáo mầm non có hiểu ngay không? |

Tiêu chí 4 loại bỏ nhiều ứng viên tưởng là tốt — ví dụ **sĩ số bình quân mỗi lớp** đóng băng sau khai giảng, nên nó là **lead measure của quý I**, không phải Bắc Đẩu năm.

## Phần 3 — Phân cấp: khối nào tập đoàn viết, khối nào đơn vị tự viết

⛔ **Hai khối không bao giờ được kế thừa: Khối 2 (Chẩn đoán) và Khối 4 (Kinh tế đơn vị).**

| # | Khối | HQ (tập đoàn) | A · Chuyên môn | B · Marketing-Sales | C · Trường/cơ sở | F · Chức năng |
|---|---|---|---|---|---|---|
| **0** | SMAC | Viết một lần | Kế thừa nguyên văn | Kế thừa nguyên văn | Kế thừa nguyên văn | Kế thừa nguyên văn |
| **1** | Trang Cam kết | Riêng | Tự viết riêng | Tự viết riêng | Tự viết riêng | Tự viết riêng |
| **2** | Chẩn đoán | Riêng | ⛔ Tự viết riêng | ⛔ Tự viết riêng | ⛔ Tự viết riêng | ⛔ Tự viết riêng |
| **3** | Lời hứa có thể sai | Riêng | ⛔ Viết lại | Kế thừa | Kế thừa + thêm phần riêng | ⛔ Viết lại (khách hàng nội bộ) |
| **4** | Kinh tế đơn vị | Riêng | ⛔ Chi phí/giờ dạy | ⛔ Kinh tế phễu | ⛔ Biên đóng góp | ⛔ Chi phí phục vụ |
| **5** | Cược | 3 cược | 1–2 | 2 | 2 | 1–2 |
| **6** | Bảng Ngừng làm | Riêng | Tự viết riêng, đúng 3 dòng | Tự viết riêng, đúng 3 dòng | Tự viết riêng, đúng 3 dòng | Tự viết riêng, đúng 3 dòng |
| **7** | Hệ mục tiêu | Bắc Đẩu + mục tiêu năm | Kế thừa Bắc Đẩu → tự dịch lead measure | Kế thừa Bắc Đẩu → tự dịch lead measure | Kế thừa Bắc Đẩu → tự dịch lead measure | Kế thừa Bắc Đẩu → tự dịch lead measure |
| **8** | Đối trọng và 5 sàn | Đặt nhóm sàn và ngưỡng tối thiểu | Kế thừa nhóm, đặt ngưỡng riêng ≥ tập đoàn | Kế thừa nhóm, đặt ngưỡng riêng ≥ tập đoàn | Kế thừa nhóm, đặt ngưỡng riêng ≥ tập đoàn | Kế thừa nhóm, đặt ngưỡng riêng ≥ tập đoàn |
| **9** | Giả định và thử nghiệm | 4–6 thử nghiệm/quý | 1–2/quý | 1–2/quý | 1–2/quý | 1–2/quý |
| **10** | Quy trình thiết kế lại | 1–2 quy trình liên phòng | 1 quy trình trong đơn vị | 1 quy trình trong đơn vị | 1 quy trình trong đơn vị | 1 quy trình trong đơn vị |
| **11** | Năng lực và dữ liệu | Chuẩn dữ liệu chung | Áp chuẩn + bảng năng lực riêng | Áp chuẩn + bảng năng lực riêng | Áp chuẩn + bảng năng lực riêng | Áp chuẩn + bảng năng lực riêng |
| **12** | Tài chính và buồng lái | Toàn bộ + dòng tiền 13 tuần | Ngân sách + 3–5 ô dashboard | Ngân sách + 3–5 ô dashboard | P&L cơ sở + 3–5 ô dashboard | Ngân sách + 3–5 ô dashboard |

**Vì sao Khối 2 và 4 không kế thừa được:** chẩn đoán của tập đoàn không nói hộ được rằng cơ sở A lấp đầy 44% còn cơ sở B là 63%; và kinh tế của một đơn vị bán hàng ra ngoài (loại B) khác hoàn toàn kinh tế của một phòng chức năng không có doanh thu (loại F). Bỏ hai khối này ở cấp dưới thì đơn vị nhận mục tiêu mà **không hiểu vì sao mục tiêu là con số đó** — và mục tiêu không hiểu thì không ai bảo vệ khi khó khăn.

## Phần 4 — Bộ giao xuống: một trang tập đoàn phát cho mỗi đơn vị

Phát **trước** khi đơn vị bắt đầu viết, đúng ngày 3/8 theo lịch trình. Năm mục, không hơn:

| # | Nội dung |
|---|---|
| 1 | **Vai của đơn vị năm nay** — Tăng trưởng / Giữ ổn định / Sửa chữa / Thu hẹp |
| 2 | **Một lead measure** đơn vị phải nhận từ Bắc Đẩu tập đoàn |
| 3 | **Năm sàn stakeholder** và ngưỡng tối thiểu không được vi phạm |
| 4 | **Trần ngân sách** — ngân sách và biên chế được cấp |
| 5 | **Ngày trình** (8/8) |

⛔ **Không có mục 1, mọi đơn vị sẽ nộp lên kế hoạch tăng trưởng** — vì không ai tự nguyện viết kế hoạch thu hẹp cho đơn vị mình — **và vốn sẽ bị chia đều.** Đây là cơ chế phổ biến nhất tạo ra công suất thừa trong hệ thống nhiều cơ sở.

Nếu người dùng chưa nhận được bộ giao xuống này, nhắc: *"Chưa nhận thì chưa viết. Đừng tự đoán vai của mình."*

## Phần 5 — Quy tắc không gộp số ⛔

> **Trong kế hoạch cấp tập đoàn, không chỉ số nào được trình bày chỉ ở dạng bình quân toàn hệ thống. Mọi chỉ số phải có cột cho từng đơn vị đứng cạnh cột tổng.**

Lý do: khi các đơn vị có giá bán chênh nhau nhiều lần, con số bình quân **không mô tả một khách hàng nào có thật**. Ví dụ ba cụm có học phí 40, 60 và 125 triệu thì "bình quân 100 triệu" là con số không ai đóng.

**Lỗi kèm theo phải cảnh giác — lỗi phạm vi:** không được lấy một chỉ số đo trên phạm vi hẹp rồi áp vào phép tính trên phạm vi rộng. Ví dụ: tỷ lệ tái tục chỉ đo cho khối lớp 1–12 tại một cơ sở thì **không được** dùng để kiểm tra biến động số học sinh toàn hệ thống, vì mẫu số khác nhau. Trước khi so hai con số, luôn hỏi: *"Hai con số này có cùng phạm vi và cùng mẫu số không?"*

## Phần 6 — Ba loại số phải tách rời ⛔

Một con số không thể phục vụ ba mục đích cùng lúc. Nếu ép nó gánh cả ba, nó hỏng cả ba.

| Loại số | Trả lời câu hỏi | Ai dùng |
|---|---|---|
| **Mục tiêu** | Ta **muốn** gì | Truyền cảm hứng, đánh giá |
| **Dự báo** | Ta **kỳ vọng** gì, **bất kể muốn gì** | Lập kế hoạch tiền mặt |
| **Phân bổ** | Ta **giao** bao nhiêu tiền thật | Cấp ngân sách |

Rủi ro lớn nhất khi trộn: **dự báo bị nhiễm khát vọng.** Với đơn vị đang khó khăn tiền mặt, đây là rủi ro sống còn — vì kế hoạch tiền mặt xây trên một con số đã bị làm đẹp.

Trong kế hoạch, ghi rõ ba con số khác nhau cho cùng một chỉ tiêu. Ví dụ: *"Dòng tiền — mục tiêu 120 tỷ · dự báo 112 tỷ · phân bổ ngân sách theo mức 105 tỷ."*
