---
name: va-chia-se-app
description: >-
  Viết kịch bản video ngắn để GIÁO VIÊN Trường Việt Anh tự giới thiệu app/skill AI mình
  làm ra, tặng phụ huynh và học sinh dùng miễn phí — phễu thu lead: follow Zalo OA + để
  lại email để nhận mật khẩu, mỗi đợt 100 tài khoản. Skill tự phỏng vấn lấy đủ thông tin,
  tự đặt tên 3 lớp (tên app / tên video / mã file), xuất kịch bản 6 nhịp kèm shotlist từng
  giây và 3 bản 90s/60s/35s, tự chấm điểm viral 100đ ngưỡng 85 mới được quay, kèm caption
  Facebook, tin nhắn Zalo OA, tiêu đề YouTube và hướng dẫn nói trước máy quay. LUÔN dùng
  khi người dùng nói "viết kịch bản giới thiệu app", "video thầy cô giới thiệu app", "kịch
  bản chia sẻ app AI", "video app giáo viên tự làm", "làm video tặng app cho phụ huynh",
  "chấm điểm kịch bản giới thiệu app", "đặt tên cho app". KHÔNG dùng cho video tuyển sinh
  cảm xúc (cau-chuyen-hoc-sinh), day-in-the-life (va-1ngay), livestream (va-livestream),
  hay khâu dựng video (va-short-reel / va-video-editing / va-long-to-short).
---

# va-chia-se-app — Kịch bản video giáo viên chia sẻ app AI tự làm

Skill này biến thông tin thô về **một thầy cô + một app** thành kịch bản quay hoàn chỉnh
mà chính thầy cô đó (không chuyên, không quen máy quay) thực hiện được, tối ưu để thu lead
phụ huynh qua email + Zalo OA.

Skill này **thay thế hoàn toàn** skill cũ `va-ai-share-on-short` (đã ngưng sử dụng).

## Bối cảnh cố định của chuỗi — không hỏi lại user

Những thông số dưới đây đã được chốt, viết sẵn vào mọi kịch bản, **không hỏi lại**:

| Thông số | Giá trị chốt |
|---|---|
| Nhịp phát hành | **1 video / tuần**, mỗi tuần một thầy cô |
| Người xuất hiện | **Chính thầy cô làm ra app** tự nói (không dùng người dẫn thay) |
| Cơ chế nhận tài khoản | **Follow Zalo OA + để lại email → nhận mật khẩu** |
| Số tài khoản mỗi đợt | **100** |
| Hạ tầng app | Base44 (sức chứa nhỏ); app nào chứng minh được nhu cầu sẽ nâng lên Supabase |
| Kênh chính | Facebook fanpage Trường Việt Anh (70% công sức, nơi chạy ads) |
| Kênh phụ | TikTok (đăng lại bản 35s), YouTube (bản 90s, tối ưu từ khoá), Zalo OA (nơi chốt) |
| Cấm tuyệt đối | Đăng trên fanpage cá nhân nguyenmanhduong1101 — vi phạm quy tắc brand safety |

Giới hạn 100 tài khoản là **giới hạn thật** (bảo vệ Base44 khỏi sập đúng lúc đông người
xem nhất), nên được phép nói thẳng lý do trong video. Không bao giờ viết giới hạn giả.

## 5 luật nền tảng — vi phạm là kịch bản hỏng

1. **Người làm app là nhân vật, app là đạo cụ.** Người xem xong chỉ nhớ tên app là thất
   bại; nhớ "có một cô giáo tự làm ra cái đó" là thành công. Điểm bán không phải phần mềm
   — thị trường đầy phần mềm. Điểm bán là **một giáo viên bình thường làm được điều đó**.
2. **Lợi ích phải thuộc về phụ huynh hoặc học sinh.** App tiết kiệm thời gian cho giáo
   viên là chuyện hay nhưng không phải nội dung cho kênh này. Nếu thầy cô chỉ nêu được lợi
   ích cho giáo viên và không quy đổi ra lợi ích cho phụ huynh/học sinh, **dừng lại và nói
   thẳng rằng app này chưa hợp để làm video hướng phụ huynh** — đừng cố viết.
3. **Demo phải là màn hình thật, không mô phỏng, không slide.** Kể cả khi giao diện chưa
   đẹp. Giao diện chưa đẹp **chính là bằng chứng** cô giáo tự làm — đừng che nó đi.
4. **Một CTA duy nhất, giới hạn phải có thật.** Không gộp "vừa đăng ký vừa chia sẻ vừa
   đăng ký tư vấn". Một video, một hành động.
5. **Không cam kết kết quả học tập.** Cấm "giúp con giỏi tiếng Anh", "cải thiện điểm số",
   "cam kết IELTS". Rủi ro pháp lý đã được ghi nhận. Chỉ mô tả app **làm gì**, không hứa
   app **mang lại gì**.

## Quy trình 5 bước

### Bước 1 — Phỏng vấn thu thập thông tin

Dùng `AskUserQuestion` nếu có (tối đa 4 câu mỗi đợt); nếu không thì hỏi bằng văn bản, gọn,
đánh số. **Chỉ hỏi những gì chưa biết** từ prompt và hội thoại. Thầy cô bận — câu nào tự
đề xuất được phương án thì đưa sẵn 3 phương án cho chọn, đừng bắt nghĩ từ đầu.

**Đợt 1 — Nội dung (quyết định kịch bản hay dở):**

1. **Ai làm app?** Tên, môn dạy, **lớp/cấp cụ thể**, cơ sở. (Vào on-screen text giây thứ 5
   và vào công thức tên video YouTube.)
2. **App giải quyết nỗi đau gì của phụ huynh hoặc học sinh?** Bắt buộc diễn đạt bằng câu
   phụ huynh sẽ tự nói ra, không phải bằng tính năng. Sai: "app dùng AI phân tích âm vị".
   Đúng: "phụ huynh không biết con phát âm sai chỗ nào để sửa".
   → Nếu thầy cô không trả lời được ở dạng này, áp dụng Luật 2.
3. **Câu chuyện thật nào dẫn tới việc làm app?** Một tình huống cụ thể có **thời gian và
   nhân vật**. Đây là chất liệu cho nhịp 3 và cho hook — phần không ai sao chép được.
4. **Mô tả luồng dùng app: người dùng nhập gì → bấm gì → nhận kết quả gì, mất bao lâu?**
   Đây là câu **bắt buộc** — nhịp demo chiếm 27 trong 90 giây và không viết được nếu thiếu
   câu này. Không có câu trả lời thì dừng, đừng bịa luồng.
5. **Đã có ai dùng chưa, kết quả gì?** Con số thật dù nhỏ ("lớp tôi 32 em dùng 3 tuần").
   Nếu chưa ai dùng → nói rõ video sẽ yếu ở trục Bằng chứng, đề nghị cho 5–10 học sinh
   dùng trước một tuần rồi mới quay.
6. **Có phụ huynh hoặc học sinh nào chịu nói vài câu trước máy quay không?** Lời chứng thực
   thật đáng 10/10 điểm trục Bằng chứng, chỉ có con số thì tối đa 6/10 — hỏi câu này trước
   khi lên lịch quay, không phải sau.

**Đợt 2 — Sản xuất:**

7. **Ngày quay dự kiến, ai cầm máy?** (Đội media Nghĩa/Hùng/Thịnh hay thầy cô tự quay điện
   thoại — kịch bản viết đúng theo thiết bị thật.)
8. **Có học sinh hoặc phụ huynh xuất hiện trong video không?** Nếu có → nhắc xin consent.
9. **Tuần này là số thứ tự bao nhiêu trong chuỗi?** (Để đánh mã file.)
10. **App có phần nào chưa hoàn thiện, thầy cô ngại quay không?** (Nếu có, kịch bản sẽ đưa
    câu thừa nhận thẳng thắn vào — nó làm tăng độ tin, không giảm.)

**Đợt 3 — Vận hành phễu (chỉ hỏi trước khi làm Bước 5, không hỏi ở đầu):**

11. Link app trên Base44 (kèm tham số UTM theo file UTM builder của team)
12. Từ khoá bình luận của tuần này (mỗi tuần một từ khác nhau để đo được video nào ra lead)
13. Link Zalo OA và số suất còn lại để điền vào mẫu tin nhắn
14. Người phụ trách và mốc thời gian cho to-do list sản xuất

**Không hỏi lại** những gì đã chốt ở bảng "Bối cảnh cố định" phía trên — đặc biệt là nền
tảng Base44, con số 100 tài khoản, nhịp 1 video/tuần và cơ chế email + Zalo OA.

### Bước 2 — Đặt tên

Đọc `references/dat-ten.md` và xuất **cả ba lớp tên**, mỗi lớp kèm 2 phương án dự phòng
để thầy cô chọn. Không bao giờ bỏ qua bước này — đặt tên sai làm hỏng cả video tốt.

### Bước 3 — Viết kịch bản

Đọc `references/khung-kich-ban.md`. Xuất bảng shotlist từng giây gồm 5 cột: Thời gian —
Hình — Lời thoại — Số tiếng — Chữ trên màn. Cột "Số tiếng" là công cụ tự kiểm thời lượng ở
Bước 4, không phải trang trí. Viết **bản 90 giây** làm bản chính, rồi bản cắt 60 giây
(Facebook ads) và 35 giây (TikTok).

Lời thoại viết đầy đủ **nhưng luôn kèm dòng ghi chú**: *"Đây là ý — thầy cô nói bằng lời
của mình, không học thuộc."* Người thật nói vấp còn hơn người thật đọc trôi chảy.

Nếu bí hook, đọc `references/thu-vien-hook.md`.

### Bước 4 — Tự chấm điểm

Đọc `references/scorecard.md`, chấm kịch bản vừa viết theo 6 trục / 100 điểm. Mọi tiêu chí
bắt đầu từ 0 và **chỉ được điểm khi trích dẫn được câu cụ thể** trong kịch bản làm bằng
chứng — bảng điểm không có cột trích dẫn là bảng điểm tự khen.

- **Đạt ≥ 85** → giao kịch bản kèm bảng điểm.
- **Dưới 85** → **không được giao bản kém**. Chỉ ra trục yếu, tự viết lại, chấm lại. Chỉ
  giao khi đạt. Nếu sau 2 lần viết lại vẫn không đạt vì thiếu chất liệu thật (không có
  câu chuyện, không có con số), báo thẳng cho user rằng cần bổ sung gì trước khi quay.

Luôn hiển thị bảng điểm cho user xem, kèm cột "sửa thế nào" cho mọi trục chưa tối đa.

### Bước 5 — Xuất phụ kiện phễu

Đọc `references/phu-kien-phieu.md` và xuất đủ 4 thứ:

1. Caption Facebook (có CTA comment-to-DM, không đặt link ngoài trong bài)
2. Tin nhắn tự động Zalo OA gửi tài khoản + mật khẩu
3. Tiêu đề + mô tả YouTube tối ưu từ khoá
4. Email chào mừng gửi qua GetResponse (nối vào chuỗi nuôi dưỡng sẵn có)

Kèm `references/huong-dan-noi-truoc-may-quay.md` gửi cho thầy cô trước ngày quay, và xuất
to-do list sản xuất theo `references/to-do-san-xuat.md`.

## Đầu ra chuẩn của skill

Một lần chạy trả về đúng 6 mục, theo thứ tự:

1. **Ba lớp tên** (tên app công bố / tên video từng kênh / mã file), mỗi lớp có phương án dự phòng
2. **Kịch bản 90 giây** — bảng shotlist 5 cột (có cột đếm tiếng của mỗi nhịp)
3. **Bản cắt 60 giây và 35 giây**
4. **Bảng chấm điểm 100đ** kèm cột sửa thế nào
5. **4 phụ kiện phễu**
6. **To-do list sản xuất** theo `references/to-do-san-xuat.md`, có người phụ trách và mốc

## Checklist trước khi giao — skill tự kiểm

- [ ] Hook 4 giây đầu dưới 12 tiếng, không chứa "AI", "giới thiệu", "ứng dụng", "công nghệ"
- [ ] Tên thầy cô + môn + cấp + cơ sở xuất hiện trọn trong nhịp 2 (trước giây thứ 11)
- [ ] Nhịp demo có mô tả luồng thật: nhập gì → bấm gì → hiện gì
- [ ] **Mọi nhịp cộng đúng 90 giây**, và mọi câu thoại nói lọt ô của nó ở 3 tiếng/giây
- [ ] Đủ ba bản 90s / 60s / 35s, mỗi bản cộng đúng
- [ ] Chỉ có một CTA, và CTA nêu rõ: làm gì → nhận gì → trong bao lâu
- [ ] Con số 100 tài khoản và lý do giới hạn được nói ra
- [ ] Không có câu nào cam kết kết quả học tập
- [ ] Lời thoại không khen trường và **không nhắc "AI Powered School"** — câu định vị chỉ
      được xuất hiện ở endcard và ở mô tả YouTube
- [ ] Có câu mời phụ huynh nói ra nhu cầu công cụ tiếp theo (nguồn ý tưởng cho tuần sau)
- [ ] Điểm scorecard ≥ 85, kèm trích dẫn cho từng tiêu chí được điểm

## Ranh giới với skill khác

| Yêu cầu của user | Skill đúng |
|---|---|
| Thầy cô giới thiệu app mình làm, thu lead dùng thử | **va-chia-se-app** (skill này) |
| Video cảm xúc đưa phụ huynh vào phễu quiz tuyển sinh | `cau-chuyen-hoc-sinh` |
| Theo chân một học sinh cả ngày | `va-1ngay` |
| Kịch bản livestream tuyển sinh | `va-livestream` |
| Reel thương mại chung, không đặc thù Việt Anh | `mkt-instagram-reel-script` |
| Dựng / cắt / burn phụ đề | `va-video-editing`, `va-short-reel`, `va-long-to-short` |
| Viết chuỗi email nuôi dưỡng sau khi thu lead | `email-marketing-sequence` |
