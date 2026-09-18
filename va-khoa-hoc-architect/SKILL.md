---
name: va-khoa-hoc-architect
description: >
  Điều phối viên cho MỌI yêu cầu thiết kế khoá học của Trường Việt Anh. Nhận yêu cầu còn mơ hồ, hỏi đủ
  ba tham số (chủ đề/pain, nhóm tuổi, tầng phễu + định dạng), phân loại vào đúng cụm nội dung, rồi ĐỊNH
  TUYẾN sang skill chuyên biệt (họ va-khoa-*). Nếu skill con chưa cài, tự dựng khoá tại chỗ theo khung
  lõi Việt Anh (5 Giá trị / 7 Thói quen / 16 kỹ năng WEF / HighScope Plan–Do–Review / AI-Powered School),
  chấm điểm 100 trước khi xuất, và luôn có đường lên phễu về sản phẩm chính là ghi danh Trường.
  LUÔN dùng khi người dùng nói chung chung: "thiết kế khoá học", "tạo khoá cho trường", "làm khoá tư duy
  / giá trị sống / cảm xúc / hướng nghiệp / tiếng Anh", "mình muốn có một khoá về ...", "giúp lên khoá
  cho nhóm ...", "khoá này nên có gì", hoặc khi CHƯA RÕ nên dùng skill con nào — skill này là CỬA VÀO,
  nó sẽ chọn giúp skill con đúng nhất. KHÔNG dùng để: chấm quảng cáo (*-ads-scorer), viết email
  (email-marketing-sequence), bài Facebook (fb-*), landing page (landing-page-writer).
---

# Va Khoá Học Architect — Điều phối thiết kế khoá học Việt Anh

Skill này là **một cửa vào duy nhất** cho mọi yêu cầu thiết kế khoá học của Trường Việt Anh. Nó không tự
ôm hết nội dung — nó **hỏi cho rõ, phân loại, rồi giao đúng skill chuyên biệt**. Khi skill chuyên biệt
chưa có, nó tự dựng khoá theo cùng chuẩn để không bao giờ để người dùng chờ.

> Trước khi làm: đọc `references/routing.md` (bảng định tuyến chủ đề → cụm nội dung → skill con) và
> `references/khung-loi-viet-anh.md` (khung 6 lớp, thư viện pain thật từ CRM, các tầng phễu, brand voice,
> điều KHÔNG được hứa). Hai file này là bộ não định tuyến.

---

## Bước 1 — Thu thập & làm rõ (intake)

Rút thông tin có sẵn trong tin nhắn; chỉ hỏi phần thiếu. **Ba tham số bắt buộc trước khi định tuyến:**

1. **Chủ đề / pain** — khoá về cái gì (vd "tư duy phản biện", "quản trị cảm xúc", "con mất gốc tiếng Anh").
   Nếu mơ hồ, gợi ý từ **Thư viện Pain thật** trong `references/khung-loi-viet-anh.md`.
2. **Nhóm tuổi** — Mầm non (3–6) / Tiểu học (6–11) / THCS (11–15) / THPT (15–18) / Phụ huynh / Nội bộ (giáo viên).
3. **Tầng phễu & định dạng** — Online Free (SP1) / Tripwire (SP2) / Offline nhiều buổi (SP3) / Nội bộ (đào tạo).

Tham số nên hỏi nếu thiếu: vùng (HCM ads-driven vs Rạch Giá referral), giọng (Vui vẻ & Thực dụng / NMD),
mục tiêu WIG.

---

## Bước 2 — Phân loại & định tuyến

Dựa trên `references/routing.md`, xác định **cụm nội dung** và **tầng phễu**, rồi chọn skill con:

| Yêu cầu | Định tuyến tới |
|---|---|
| Khoá **online / tripwire / lead magnet** (bất kỳ chủ đề) | `va-khoa-online-tripwire` |
| Khoá **tư duy, phản biện, sáng tạo** (16 kỹ năng WEF) | `va-khoa-tu-duy-khai-phong` |
| Khoá **giá trị sống, 5 Giá trị, 7 Thói quen** | `va-khoa-gia-tri-song` |
| Khoá **tiếng Anh + tự tin nói** (pain #1) | `va-khoa-tieng-anh-tu-tin` |
| Khoá **quản trị cảm xúc / SEL** (THCS mạnh nhất) | `va-khoa-quan-tri-cam-xuc` |
| Khoá **hướng nghiệp + AI-ready** (THPT) | `va-khoa-huong-nghiep-ai` |

Quy tắc ưu tiên: **tầng phễu thắng chủ đề.** Nếu là online/tripwire → luôn dùng `va-khoa-online-tripwire`
(nó nhận chủ đề làm tham số). Chỉ khi là offline nhiều buổi hoặc đào tạo nội bộ mới định tuyến theo cụm nội dung.

**Nếu skill con đã cài:** thông báo ngắn "đang dùng skill X", rồi để skill đó chạy với tham số đã thu thập.
**Nếu skill con CHƯA cài:** không để người dùng chờ — tự dựng khoá tại chỗ theo Bước 3, và gợi ý người dùng
cài skill con để lần sau chuyên sâu hơn.

---

## Bước 3 — Dựng khoá tại chỗ (khi chưa có skill con)

Áp dụng phương pháp 5 bước dùng chung cho mọi khoá Việt Anh (giống xương sống của các skill con):

1. **Neo khung lõi** — map chủ đề vào 6 lớp nội dung; chọn cầu từ nỗi đau/đề tài sang năng lực lõi.
2. **Mục tiêu & Big Promise** — cụ thể, đo được, đúng cấp; không hứa điều cấm.
3. **Cấu trúc theo nhịp HighScope Plan–Do–Review + phản tư Dewey** — nói/làm trước, rút nguyên tắc sau;
   mỗi buổi đóng bằng một cam kết hành động nhỏ.
4. **Đường lên phễu (ascension)** — khoá dẫn tới đâu tiếp theo; online → offline → ghi danh Trường.
5. **Đầu ra** — outline khoá + học liệu chính + (nếu marketing) landing/CTA; kèm rubric tiến trình
   (không điểm số) khi là khoá học sinh.

Chi tiết theo tầng phễu:
- **Online/Tripwire:** ưu tiên gọi `va-khoa-online-tripwire`; nếu tự làm, theo đúng cấu trúc tripwire
  (hook nỗi đau → giá trị thật → CTA ascension → offer/giá).
- **Offline nhiều buổi:** thiết kế 8–12 buổi, mỗi buổi nhịp 5 bước Connect–Plan–Do–Review–Commit; kèm
  rubric tiến trình 4 mức + báo cáo phụ huynh (VAAR rút gọn).
- **Nội bộ (giáo viên):** giáo viên tự trải nghiệm trước khi dạy; nhấn kỹ năng điều phối (facilitation),
  không thuyết giảng.

---

## Bước 4 — Kiểm định (bắt buộc)

Mọi khoá — dù do skill con hay tự dựng — phải qua **thang 100 điểm** trước khi xuất (dùng rubric của skill
con nếu có; nếu tự dựng, chấm theo 8 tiêu chí: bám pain thật 20 · Big Promise 15 · Hook 10 · nhịp PDR 10 ·
giá trị thật 10 · CTA/ascension 15 · brand voice & không hứa cấm 10 · neo khung lõi 10). **Chỉ xuất khi ≥ 90.**

---

## Bước 5 — Giao & định vị

- Xuất file (Markdown mặc định; Word nếu cần trình bày — dùng skill `docx`).
- Gắn **WIG** liên quan và **bước phễu kế tiếp**.
- Nếu wiki 2nd brain có sẵn: đề xuất lưu + ghi `log.md` theo schema (hỏi trước khi ghi).
- Cuối cùng, gợi ý các khoá/skill kế tiếp trong hệ sinh thái để người dùng mở rộng bộ.

---

## Nguyên tắc không thoả hiệp (áp cho mọi định tuyến)

- Chủ đề "gần khách hàng" để câu, khung lõi 5 lớp để giữ.
- Pain phải có thật (ưu tiên CRM); không cho điểm số / không thuyết giảng.
- Không hứa thứ hạng/kết quả tuyệt đối.
- Khoá không bao giờ đứng một mình — luôn có đường về sản phẩm chính (ghi danh Trường).
- Bối cảnh & con người Việt Nam.
