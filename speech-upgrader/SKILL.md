---
name: speech-upgrader
description: Review & nâng cấp bài phát biểu / diễn thuyết / keynote bằng cách triệu hồi 3 public speaker huyền thoại (Steve Jobs, JFK, Oprah, MLK, Obama, Mandela, Churchill, Greta Thunberg, Reagan, Brené Brown) để góp ý song song, sau đó tổng hợp thành bản nâng cấp giữ giọng người nói gốc và xuất file Word có ghi chú dàn dựng sân khấu. LUÔN dùng skill này khi user nói "viết bài phát biểu", "nâng cấp bài speech", "review bài diễn thuyết", "viết keynote", "viết bài cho lễ tổng kết / khai giảng / tốt nghiệp / ra mắt sản phẩm / hội nghị", "viết bài phát biểu cho [tên người]", "speech writer", "public speaking", "làm bài cho ai đó đọc trên sân khấu", "biến bài thường thành bài hay", "viết bài kiểu Steve Jobs / JFK / Obama". Cũng dùng khi user paste vào một bài speech rồi xin feedback hoặc xin cải thiện, ngay cả khi không nhắc đến tên speaker huyền thoại nào — vì skill này chính là cách tiếp cận đa-lăng-kính để cải thiện chất lượng diễn thuyết.
---

# Speech Upgrader — Multi-Speaker Review Method

## Skill này làm gì

Skill này biến bất kỳ bài phát biểu nào thành một bài có "thịt" của những diễn giả vĩ đại nhất lịch sử, mà vẫn giữ giọng riêng của người sẽ đọc. Cách làm cốt lõi: triệu hồi 3 agent đóng vai 3 public speaker huyền thoại phù hợp với mục tiêu bài nói → mỗi agent đưa ra critique từ lăng kính riêng → tổng hợp thành 1 bản nâng cấp duy nhất → xuất file Word có cấu trúc 3 phần (bản gốc / bản nâng cấp / ghi chú dàn dựng).

Lý do skill này tồn tại: hầu hết bài phát biểu trong thực tế bị "an toàn" — đúng nhưng không cháy. Một editor giỏi đôi khi vẫn không đủ vì họ chỉ có một góc nhìn. Khi mời nhiều speaker huyền thoại review song song, các điểm yếu khác nhau sẽ lộ ra: thiếu hook, thiếu reveal moment, thiếu moonshot, thiếu sự thừa nhận nỗi sợ khán giả, thiếu CTA có thể forward được. Sau khi gom feedback, người biên tập (LLM hoặc người dùng) có một bản đồ rất rõ để làm gì.

## Khi nào trigger skill này

Trigger ngay khi:
- User paste vào một bài speech và xin review hoặc xin nâng cấp.
- User yêu cầu viết bài phát biểu cho một sự kiện cụ thể (lễ tổng kết, khai giảng, tốt nghiệp, ra mắt sản phẩm, hội nghị, gala, đám cưới, tang lễ tưởng niệm).
- User nói muốn "bài speech kiểu Steve Jobs / Obama / JFK".
- User cần biến một bản nháp lý thuyết thành một bài có khả năng truyền cảm hứng và dẫn đến hành động.

Đừng trigger nếu user chỉ xin viết một đoạn email, bài blog, hoặc văn bản không đọc trên sân khấu — đó là việc của copywriter, không phải speech writer.

## Workflow 6 bước

### Bước 1 — Hỏi 4 câu cốt lõi qua AskUserQuestion

Trước khi bắt tay vào việc, dùng `AskUserQuestion` (tool có sẵn trong Cowork) để hỏi đồng thời 4 câu sau. Đừng để user phải suy nghĩ từng câu rời rạc — đưa cùng lúc, kèm options cụ thể:

1. **Cấu trúc output**: (a) Chỉ bản nâng cấp; (b) Bản gốc + bản nâng cấp song song để so sánh; (c) Ba phiên bản theo phong cách khác nhau (Jobs / JFK / Oprah riêng từng bản).
2. **Độ dài đọc trên sân khấu**: (a) 3-5 phút (ngắn, phong cách TED); (b) 7-10 phút (chuẩn keynote); (c) 12-15 phút (đầy đủ, lễ trang trọng); (d) Mở rộng với storytelling chi tiết.
3. **CTA cuối bài (multi-select)**: (a) Đăng ký / mua / hành động thương mại; (b) Giới thiệu bạn bè / lan truyền; (c) Cam kết đồng hành; (d) Truyền cảm hứng không kèm CTA cụ thể.
4. **Format file đầu ra**: (a) Word .docx chuyên nghiệp; (b) Markdown để dễ sửa; (c) Cả hai.

Nếu user đã cung cấp đủ thông tin trong prompt ban đầu, có thể bỏ qua câu nào đã rõ.

### Bước 2 — Thu thập context bài nói

Trước khi triệu hồi speaker, cần biết:
- **Người sẽ đọc bài** (Ai? Vai trò gì? Có gendered tone không?)
- **Khán giả mục tiêu** (phụ huynh? nhân viên? cổ đông? sinh viên?)
- **Sự kiện** (lễ gì? trang trọng đến đâu? có quay phim không?)
- **Mục tiêu KPI** (sau bài này, user muốn khán giả LÀM gì cụ thể?)
- **Proof points sẵn có** (con số, câu chuyện thật, sản phẩm demo được — đây là "vàng" mà bài speech yếu thường bỏ qua)

Nếu user paste sẵn bài gốc, đọc kỹ rồi note lại proof points đáng nhấn mạnh. Nếu chưa có bài gốc, viết outline 10 section trước (xem `references/speech-structure.md`) rồi mới triệu hồi speaker.

### Bước 3 — Auto-match 3 speaker theo mục tiêu

Đọc `references/speaker-matrix.md` để chọn 3 speaker phù hợp nhất. Nguyên tắc auto-match:

- **Ra mắt sản phẩm / công bố định hướng** → Jobs (cấu trúc keynote) + JFK (moonshot statement) + Oprah (intimate connection với khách hàng).
- **Kêu gọi nhân quyền / công bằng xã hội** → MLK (dream + cadence) + Mandela (forgiveness + nation-building) + Obama (hopeful idealism).
- **Lễ tốt nghiệp / khai giảng** → Steve Jobs (Stanford 2005) + Brené Brown (vulnerability) + Oprah (Harvard 2013).
- **Hội nghị doanh nghiệp / cổ đông** → Jobs + Bezos (long-term thinking) + Churchill (resolve trong thời điểm khó).
- **Tang lễ / tưởng niệm** → Lincoln (Gettysburg gravity) + Reagan (Challenger sweetness) + Mandela (transcendence).
- **Phong trào khí hậu / thay đổi** → Greta Thunberg (moral clarity của thế hệ trẻ) + Al Gore (urgency với data) + MLK (moral imperative).
- **Đám cưới / sự kiện gia đình** → Brené Brown + Oprah + một storyteller địa phương phù hợp.

Đề xuất 3 speaker cho user TRƯỚC KHI triệu hồi, để user có thể thay đổi nếu muốn. Đừng chọn 3 speaker có cùng DNA (ví dụ Jobs + Bezos + Musk → đều product launch) — chọn 3 lăng kính khác nhau (cấu trúc / tu từ / cảm xúc) để feedback đa chiều.

### Bước 4 — Triệu hồi 3 agent song song

Dùng tool `Agent` (subagent) để spawn 3 agent CÙNG MỘT LƯỢT (single message, multiple tool calls) — không tuần tự. Mỗi agent là một public speaker khác nhau, được brief đầy đủ context:

```
Bạn đang đóng vai [TÊN SPEAKER] — [mô tả 1 câu về phong cách].
Bạn nổi tiếng với [2-3 bài speech tiêu biểu].
Phong cách: [3-5 đặc trưng tu từ và cấu trúc].

NHIỆM VỤ: Review bài phát biểu sau (sẽ được đọc tại [SỰ KIỆN] bởi [NGƯỜI ĐỌC]) và đề xuất nâng cấp THEO PHONG CÁCH [TÊN SPEAKER].

CONTEXT: [tất cả proof points, mục tiêu KPI, insight khán giả]

YÊU CẦU OUTPUT (dưới 800 từ):
1. Top 5 nhận xét QUAN TRỌNG NHẤT về bài gốc qua lăng kính của bạn
2. 3-5 ĐOẠN VIẾT LẠI cụ thể bằng tiếng [ngôn ngữ] mang DNA của bạn
3. 1 đoạn / khoảnh khắc đặc trưng của phong cách bạn (ví dụ: Jobs → "one more thing"; JFK → moonshot statement; Oprah → đoạn xử lý nỗi sợ)
4. Cách lồng CTA theo phong cách bạn
5. Đề xuất 1 dàn dựng sân khấu

BÀI GỐC: [paste full]
```

Mỗi agent phải nhận đủ context — không tiết kiệm. Theo Claude Agent SDK best practice, agent không thấy được conversation history nên cần brief đầy đủ trong prompt.

### Bước 5 — Tổng hợp thành bản nâng cấp duy nhất

Sau khi 3 agent trả về, KHÔNG paste nguyên feedback của agent vào output. Thay vào đó, đọc cả 3, lấy "best of 3":
- Mở bài hay nhất (thường là Jobs với hook bất ngờ hoặc JFK với lời triệu hồi sứ mệnh).
- Chuyển đoạn mạnh nhất (thường là JFK với anaphora hoặc chiasmus).
- Proof point reveal moment đắt nhất (thường là Jobs với "one more thing").
- Đoạn xử lý nỗi sợ / chạm cảm xúc (thường là Oprah hoặc Brené Brown).
- CTA cụ thể nhất (Jobs hoặc bất kỳ ai có frame "nhắn 7 chữ cho 1 người bạn").
- Câu kết neo lại sứ mệnh (JFK hoặc MLK).

Khi viết bản tổng hợp, GIỮ GIỌNG của người sẽ đọc — không chèn nguyên văn của Jobs/JFK/Oprah vào miệng họ. Giữ những từ ngữ, cách xưng hô, nhịp điệu của người đọc; chỉ áp dụng STRUCTURE và RHETORICAL DEVICES từ các speaker huyền thoại.

Cấu trúc 10 section tham khảo (xem `references/speech-structure.md` chi tiết):
1. Hook (0-45s) — câu hỏi định mệnh hoặc đối lập gây sốc
2. Tri ân & nhìn lại (45-90s) — giữ tinh thần lễ
3. Gọi tên kẻ thù / vấn đề (90-150s) — định nghĩa thế lực đang chống lại
4. Reveal #1 — proof point bất ngờ nhất
5. Reveal #2 — câu chuyện nhân vật cụ thể
6. Đối thoại nỗi sợ — thừa nhận điều khán giả đang nghĩ
7. Tuyên ngôn — anaphora + chiasmus + moonshot
8. Lộ trình cụ thể — ngày tháng, con số, cam kết
9. CTA — lời mời hành động có frame forward được
10. One more thing — đóng bài bằng câu chuyện 10 năm sau hoặc một hình ảnh đọng lại

Mỗi section có timestamp ước lượng + ghi chú sân khấu (in nghiêng đỏ trong file Word, không đọc thành tiếng).

### Bước 6 — Xuất file Word + verify độ dài

Dùng `scripts/build_speech_docx.js` để build file Word có cấu trúc:
- Trang bìa (tên sự kiện, người đọc, ngày)
- Phần I: Bản gốc (nếu user chọn cấu trúc song song)
- Phần II: Bản nâng cấp (10 section, timestamp, stage notes)
- Phần III: Ghi chú dàn dựng + bảng so sánh + cảm hứng tham chiếu speaker

**Quan trọng — kiểm tra độ dài**: sau khi build, đếm word count của Phần II (chỉ phần đọc, bỏ stage notes và heading). Tốc độ đọc tiếng Việt: ~200-220 từ/phút (whitespace split). Tốc độ đọc tiếng Anh: ~130-150 wpm. Nếu lệch quá target user yêu cầu, cắt thẳng những đoạn giải thích trùng lặp; KHÔNG cắt hook, reveal moment, CTA, hay one more thing.

Lưu file vào folder Cowork chính (workspace folder), không lưu vào temporary outputs. Sau đó present file cho user kèm computer:// link.

## Lưu ý quan trọng khi triệu hồi speaker

**Không trộn speaker không tương thích văn cảnh.** Greta Thunberg trong lễ ra mắt iPhone sẽ thành nhảm. Lincoln trong đám cưới sẽ thành nặng nề. Đọc kỹ matrix trước khi chọn.

**Brief mỗi agent với context đầy đủ về speaker đó.** LLM có theory of mind tốt — khi bạn nói "bạn là Oprah, nổi tiếng với Stanford Commencement 2008 và Golden Globes 2018", agent sẽ tự nhiên hơn khi đóng vai. Đừng để agent đoán mò.

**Đừng để bài nâng cấp trở thành Frankenstein.** Mỗi agent đề xuất 3-5 đoạn — không nghĩa là bản tổng hợp có 9-15 đoạn paste. Chọn lọc, viết lại, hàn dính. Bản tổng hợp nên đọc như một người duy nhất viết, không phải 3 nhà tu từ cãi nhau.

**Stage notes là vũ khí bí mật.** Phần ghi chú dàn dựng sân khấu thường có giá trị bằng chính bài speech: bước chân, ánh mắt, slide, demo, khoảnh khắc dừng. Đầu tư vào phần này — đó là điều biến một bài đọc thành một bài biểu diễn.

## Files trong skill này

- `SKILL.md` (file này) — workflow chính
- `references/speaker-matrix.md` — bảng tham chiếu 10 speaker huyền thoại với DNA, khi nào dùng, ví dụ
- `references/speech-structure.md` — cấu trúc 10 section keynote chi tiết kèm template
- `scripts/build_speech_docx.js` — Node.js script build file Word
- `assets/agent-prompt-template.md` — template prompt để triệu hồi speaker agent

## Phụ thuộc

- Node.js + `docx` package (`npm install docx` trong working folder)
- Tool `Agent` (subagent) để spawn parallel
- Tool `AskUserQuestion` cho phase clarification

## Kết quả mong đợi

Sau khi chạy skill này, user nhận được:
1. Một file Word có thể in/gửi luôn cho người đọc speech.
2. Bài nâng cấp có ít nhất 5 trong 8 đặc trưng sau: hook gây dừng-thở, kẻ thù được gọi tên, reveal moment bất ngờ, đối thoại nỗi sợ khán giả, anaphora 3 lần, chiasmus đáng nhớ, CTA có thể forward, one-more-thing closing.
3. Ghi chú dàn dựng đủ cụ thể để đạo diễn sân khấu có thể follow.

Nếu bản đầu chưa đạt — chạy lại bước 5 với một speaker khác trong matrix. Đây là một skill iterative, không phải one-shot.
