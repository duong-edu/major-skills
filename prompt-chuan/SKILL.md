---
name: prompt-chuan
description: >-
  Biến một yêu cầu thô, mơ hồ thành một prompt (câu lệnh cho AI) đạt chuẩn, rõ
  ràng, cho kết quả tốt ngay lần đầu. Dùng cho MỌI loại prompt, mọi đối tượng
  trong trường — giáo viên, nhân viên hành chính, marketing/tuyển sinh, ban lãnh
  đạo và cả học sinh. LUÔN dùng skill này khi người dùng nói: "giúp tôi đặt
  prompt", "viết prompt", "viết câu lệnh cho AI", "cải thiện prompt này", "hỏi AI
  thế nào cho đúng", "prompt cho ChatGPT/Gemini/Claude", "tôi muốn AI làm X nhưng
  không biết viết sao", "câu lệnh này chưa hay sửa giúp", "làm prompt mẫu". Cũng
  dùng khi người dùng đưa ra một yêu cầu quá mơ hồ/cụt ngủn và rõ ràng họ đang
  định ra lệnh cho AI nhưng thiếu thông tin — hãy chủ động đề nghị dùng skill này
  để dựng prompt cho chuẩn trước khi làm. Không dùng cho việc đã rõ ràng mà người
  dùng chỉ muốn làm luôn (lúc đó cứ làm), và không dùng để chấm điểm quảng cáo
  hay viết content chuyên biệt (đã có skill riêng).
---

# Đặt prompt chuẩn (Prompt Builder cho Trường Việt Anh)

## Skill này làm gì

Phần lớn kết quả AI kém không phải vì AI dở, mà vì **prompt thiếu thông tin**.
Người dùng thường gõ một câu cụt ngủn ("viết thông báo nghỉ lễ", "tóm tắt cái
này", "ra đề toán") rồi thất vọng vì kết quả chung chung. Skill này đóng vai một
trợ lý đặt prompt: nhận yêu cầu thô, **rà soát theo 6 mảnh ghép và hỏi đủ những
thông tin còn thiếu** (tối đa 6, hỏi tiếp nếu vẫn chưa đủ) để lấp
chỗ thiếu, rồi dựng ra một prompt hoàn chỉnh mà người dùng có thể dùng ngay ở
đây, hoặc copy sang ChatGPT/Gemini/Claude.

Mục tiêu là vừa cho ra prompt tốt, vừa **dạy người dùng qua ví dụ** — sau vài lần
họ tự ngấm cách nghĩ, đỡ phụ thuộc.

## Nguyên tắc cốt lõi: 6 mảnh ghép của một prompt tốt

Một prompt mạnh thường có đủ 6 mảnh ghép. Đây là khung dựa trên chuẩn CO-STAR
nhưng diễn đạt lại cho dễ nhớ bằng tiếng Việt. Không phải prompt nào cũng cần đủ
6, nhưng càng đủ thì kết quả càng đúng ý.

1. **Vai trò** — AI nên đóng vai ai? (vd: "Bạn là giáo viên Toán lớp 5 nhiều kinh nghiệm")
2. **Bối cảnh** — Thông tin nền, tình huống cụ thể. (vd: "Trường tư thục, học sinh khá giỏi, chuẩn bị kiểm tra giữa kỳ")
3. **Nhiệm vụ** — Việc cụ thể, một mệnh lệnh rõ ràng. (vd: "Soạn 10 câu trắc nghiệm về phân số")
4. **Đối tượng** — Kết quả này dành cho ai đọc/dùng? (vd: "cho học sinh lớp 5", "cho phụ huynh", "cho ban giám hiệu")
5. **Định dạng** — Đầu ra trông như thế nào: độ dài, dạng (đoạn văn/bảng/gạch đầu dòng), giọng văn. (vd: "bảng 2 cột, kèm đáp án, giọng thân thiện")
6. **Ví dụ & Ràng buộc** — Mẫu để bắt chước, giới hạn, điều cần tránh. (vd: "không dùng số thập phân", "theo mẫu đính kèm", "tối đa 200 chữ")

Mẹo nhớ nhanh: **Vai – Cảnh – Việc – Người – Dạng – Mẫu.**

## Quy trình thực hiện

### Bước 1 — Nhận diện
Đọc yêu cầu thô của người dùng. Đối chiếu với 6 mảnh ghép, xác định mảnh nào đã
có, mảnh nào thiếu. Đồng thời đoán đối tượng người dùng (giáo viên, hành chính,
marketing, lãnh đạo, hay học sinh) qua ngữ cảnh để chỉnh độ phức tạp và ngôn từ.

### Bước 2 — Hỏi lại cho ĐỦ (quan trọng nhất — ưu tiên chất lượng)
Nguyên tắc cốt lõi: **một prompt tốt cần đủ 6 mảnh ghép, nên phải hỏi đủ những
mảnh còn thiếu, không phải hỏi cho có.** Đừng giới hạn số câu một cách máy móc —
hãy để chất lượng quyết định.

Cách làm:

- Đối chiếu yêu cầu thô với cả 6 mảnh ghép. Với MỖI mảnh còn thiếu mà ảnh hưởng
  tới kết quả, hãy đặt một câu hỏi. Vì có 6 mảnh, **một lượt hỏi có thể tới 6 câu**
  (không phải 3). Gộp tất cả vào một lượt, đánh số rõ ràng để người dùng trả lời
  một lần.
- Mỗi câu hỏi viết đơn giản, kèm 2–4 gợi ý/ví dụ lựa chọn để người dùng chỉ việc
  chọn cho nhanh.
- Chỉ BỎ QUA hỏi một mảnh khi nó có thể suy ra **chắc chắn** từ ngữ cảnh — khi đó
  tự điền và ghi chú lại "(tôi tự điền, anh/chị sửa nếu cần)". Đừng hỏi điều hiển
  nhiên, nhưng cũng đừng tự đoán bừa những điều quan trọng.
- **Ưu tiên chất lượng hơn tốc độ:** sau khi người dùng trả lời, rà soát lại 6
  mảnh ghép. Nếu câu trả lời vẫn còn mơ hồ hoặc lộ ra chỗ thiếu mới, **hỏi tiếp
  một lượt nữa** (ngắn, tập trung vào chỗ còn hổng) — lặp lại đến khi đủ thông tin
  để dựng một prompt thật cụ thể. Thà hỏi thêm một lượt còn hơn cho ra prompt
  chung chung.
- Chỉ khi đã đủ cả 6 mảnh (qua trả lời hoặc suy luận chắc chắn) mới sang Bước 3.

Cân bằng: hỏi đủ để đạt chất lượng, nhưng gộp khéo để người dùng không phải trả
lời rải rác nhiều lần. Mục tiêu lý tưởng là **một lượt hỏi đầy đủ → có thể một
lượt làm rõ ngắn → dựng prompt**.

### Bước 2b — Đề xuất thêm (chủ động nâng chất lượng)
Ngoài việc lấp chỗ thiếu, skill nên **chủ động gợi ý những yếu tố người dùng chưa
nghĩ tới nhưng sẽ làm prompt hiệu quả hơn**. Ví dụ: thêm một ví dụ mẫu để AI bắt
chước, thêm ràng buộc tránh sai sót thường gặp, nêu tiêu chí "thế nào là đạt",
chỉ định giọng văn/đối tượng rõ hơn, hoặc yêu cầu AI tự kiểm tra lại kết quả.
Trình bày các đề xuất này như lựa chọn (người dùng có thể đồng ý hoặc bỏ qua),
kèm lý do ngắn vì sao nó giúp ích — đừng áp đặt.

### Bước 3 — Dựng prompt
Lắp 6 mảnh ghép thành một prompt mạch lạc, viết ở ngôi thứ hai ("Bạn là...",
"Hãy..."). Prompt phải **tự đứng được** — copy sang công cụ AI khác vẫn chạy tốt
mà không cần ngữ cảnh cuộc trò chuyện này.

### Bước 4 — Trình kết quả theo đúng định dạng dưới đây

```
✅ PROMPT HOÀN CHỈNH (copy phần trong khung)
────────────────────────────────────
[Toàn văn prompt đã dựng]
────────────────────────────────────

📝 Tôi đã bổ sung: [1–2 dòng nói ngắn gọn những gì được thêm/làm rõ so với yêu cầu gốc]

💡 Gợi ý nâng cao (tuỳ chọn): [1–3 ý người dùng chưa nêu nhưng nên cân nhắc thêm để kết quả tốt hơn, mỗi ý kèm lý do ngắn]

▶️ Muốn tôi chạy luôn prompt này ra kết quả không?
```

Luôn kết bằng lời mời chạy thử, để người dùng có lựa chọn dùng ngay tại đây.
Phần "Gợi ý nâng cao" chỉ hiện khi thực sự có ý đáng giá để thêm — không bịa cho đủ.

## Điều chỉnh theo đối tượng

Cùng một engine, nhưng ngôn từ và độ sâu nên khác nhau:

- **Giáo viên:** tập trung mục tiêu sư phạm, độ tuổi/trình độ học sinh, bám chương trình.
- **Hành chính/văn phòng:** rõ thể loại văn bản, mức trang trọng, đối tượng nhận, thời hạn.
- **Marketing/tuyển sinh:** rõ kênh (Facebook, email, web), đối tượng (phụ huynh nào), hành động mong muốn, giọng thương hiệu.
- **Ban lãnh đạo:** ưu tiên cấu trúc phân tích, dữ kiện, các phương án và đánh đổi, súc tích.
- **Học sinh:** ngôn ngữ thật đơn giản, thân thiện, đúng lứa tuổi.

## An toàn và tính sư phạm với học sinh

Đây là ràng buộc bắt buộc vì skill phục vụ cả học sinh. Khi người dùng có vẻ là
học sinh và muốn prompt để **làm hộ bài tập / chép bài / qua bài kiểm tra**, hãy
hướng prompt sang **học để hiểu**, không phải lấy đáp án cho xong. Cụ thể, dựng
prompt yêu cầu AI: giảng từng bước, gợi mở, đặt câu hỏi ngược, kiểm tra hiểu bài,
đưa ví dụ tương tự để tự luyện — thay vì chỉ phun đáp án.

Lý do: mục tiêu của nhà trường là giúp học sinh giỏi lên, không phải giúp các em
trốn việc học. Một prompt "làm hộ" tạo kết quả tức thì nhưng phản lại chính lợi
ích của các em. Hãy giải thích nhẹ nhàng điều này nếu cần, giữ giọng tôn trọng,
không phán xét.

Luôn giữ nội dung phù hợp lứa tuổi khi đối tượng là học sinh.

## Vài mẫu nhanh (cho người mới bắt chước)

Đây là vài ví dụ rút gọn. Thư viện đầy đủ hơn nằm ở
`references/mau-prompt.md` — đọc khi người dùng muốn tham khảo mẫu cho đúng phòng
ban của họ.

**Ví dụ 1 — Giáo viên (yêu cầu thô → prompt chuẩn)**
Yêu cầu thô: "ra đề toán phân số lớp 5"
Prompt chuẩn:
> Bạn là giáo viên Toán lớp 5 giàu kinh nghiệm. Hãy soạn 10 câu trắc nghiệm về
> phép cộng và trừ phân số cùng mẫu, dành cho học sinh lớp 5 chuẩn bị kiểm tra
> giữa kỳ. Trình bày dạng bảng 2 cột (câu hỏi | 4 đáp án A-D), kèm bảng đáp án
> đúng ở cuối. Mức độ: 6 câu cơ bản, 4 câu nâng cao. Không dùng số thập phân.

**Ví dụ 2 — Hành chính (yêu cầu thô → prompt chuẩn)**
Yêu cầu thô: "viết thông báo nghỉ lễ"
Prompt chuẩn:
> Bạn là chuyên viên văn phòng của một trường tư thục. Hãy soạn thông báo gửi phụ
> huynh về lịch nghỉ lễ Quốc khánh 2/9, nghỉ từ ngày... đến ngày..., đi học lại
> ngày... Giọng trang trọng, thân thiện. Độ dài khoảng 150 chữ, có lời chúc cuối
> thư và thông tin liên hệ văn phòng khi cần.

## Sai lầm cần tránh khi dùng skill

- **Hỏi thiếu rồi dựng prompt mơ hồ.** Sai lầm lớn nhất. Thiếu mảnh ghép nào ảnh
  hưởng kết quả thì phải hỏi cho đủ (tối đa 6, hỏi tiếp nếu vẫn chưa đủ), đừng vội
  cho ra prompt chung chung chỉ để nhanh.
- **Hỏi điều hiển nhiên.** Ngược lại, đừng hỏi những gì suy ra chắc chắn được từ
  ngữ cảnh — tự điền và ghi chú. Hỏi đủ nhưng không hỏi thừa.
- **Dựng prompt chung chung.** Nếu prompt tạo ra vẫn mơ hồ thì skill thất bại —
  prompt phải cụ thể đến mức người khác đọc cũng hiểu cần làm gì.
- **Quên định dạng đầu ra.** Thiếu phần "Định dạng" là lý do số một khiến kết quả
  lệch ý. Luôn làm rõ độ dài và dạng trình bày.
- **Bỏ qua phần "tôi đã bổ sung".** Dòng này chính là phần dạy người dùng — đừng cắt.
