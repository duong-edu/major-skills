---
name: zalo-oa-writer
description: >
  Viết nội dung cho Zalo Official Account của Trường Việt Anh — ba định dạng: Bài viết OA,
  Tin Truyền thông (Broadcast, chỉ 4 tin miễn phí mỗi tháng), và ZNS (Zalo Notification
  Service). Skill nắm thông số kỹ thuật thật của nền tảng (tiêu đề <= 150 ký tự, mô tả <= 300,
  nút CTA <= 50, ảnh bìa 16:9 vùng an toàn 14:9, khung giờ gửi 6:00–20:00, tối đa 1 broadcast
  mỗi ngày), phân biệt đúng loại tin để không vi phạm chính sách Zalo, viết theo văn phong
  Zalo (tiếng Việt thuần, lịch sự, không hashtag, không caps), quản lý sổ ngân sách broadcast,
  và chấm điểm 100 với ngưỡng xuất bản 90. LUÔN dùng skill này khi người dùng nói: "viết bài
  Zalo", "viết nội dung Zalo OA", "soạn tin broadcast Zalo", "gửi tin cho phụ huynh qua Zalo",
  "viết ZNS", "tin nhắn Zalo cho phụ huynh", "đăng bài lên Zalo OA", "nội dung Zalo tuyển
  sinh", hoặc bất kỳ yêu cầu tạo nội dung nào cho kênh Zalo của trường.
---

# Zalo OA Writer — Nội dung Zalo cho Trường Việt Anh

## Vì sao Zalo cần một skill riêng

Zalo không phải Facebook viết ngắn lại. Người dùng Zalo mở app để nhắn tin với người thân, nên
ngưỡng chịu đựng quảng cáo thấp hơn hẳn và kỳ vọng "đáng tin" cao hơn "đẹp". Với phụ huynh,
Zalo là kênh **thông báo và chăm sóc**, không phải kênh giải trí. Một bài Facebook giật hook
kiểu "Đừng khen con là giỏi quá!" bê nguyên sang Zalo sẽ bị đọc như spam.

Ba khác biệt phải nhớ:

1. **Xưng hô trang trọng.** "Kính gửi Quý phụ huynh", "Anh/chị" — không "bạn", không "các mẹ ơi".
2. **Không hashtag, không CAPS, không dãy dấu chấm than.** Zalo kiểm duyệt nghiêm hơn Facebook.
3. **Một CTA duy nhất**, ưu tiên hoàn tất ngay trong Zalo (nhắn tin OA, form Zalo) thay vì đẩy
   ra web — trừ khi mục tiêu là kéo traffic về truongvietanh.com.

## Bước 1 — Xác định ĐÚNG loại tin (bắt buộc, hỏi trước khi viết)

Chọn sai loại tin là lỗi nghiêm trọng nhất trên Zalo: có thể bị từ chối duyệt, bị phạt phí, hoặc
bị người dùng báo cáo làm giảm chất lượng OA.

| Loại | Dùng cho | Người nhận | Chi phí & giới hạn |
|---|---|---|---|
| **Bài viết OA** | Nội dung giá trị, tin hoạt động, bài chuyển thể từ blog | Ai vào trang OA đều xem được | Miễn phí, **không tốn quota broadcast** — mặc định nên chọn |
| **Tin Truyền thông (Broadcast)** | Marketing, khuyến mãi, thông báo chung của trường | Chỉ follower đang hoạt động | **Miễn phí nhưng OA đã xác thực chỉ được 4 tin/tháng, tối đa 1 tin/ngày** |
| **ZNS** | Thông báo giao dịch & chăm sóc khách hàng: xác nhận lịch tham quan, nhắc hạn đăng ký, thông báo kết quả | Gửi tới số điện thoại đã đăng ký Zalo | Trả phí theo tin, **template phải đăng ký và được duyệt trước** |
| **Tin tư vấn** | Trả lời phụ huynh đang hỏi | Người vừa tương tác | 8 tin đầu miễn phí trong 48 giờ kể từ tương tác, sau đó tính phí |

**Luật cứng về ZNS:** ZNS chỉ dành cho *thông báo giao dịch* và *chăm sóc khách hàng*. **Không
dùng ZNS để quảng cáo tuyển sinh thuần**, không "ưu đãi giảm học phí" trá hình dưới dạng thông
báo. Nếu người dùng yêu cầu nội dung quảng cáo qua ZNS, nói thẳng rằng template sẽ bị từ chối
duyệt và đề xuất chuyển sang Broadcast hoặc Bài viết OA.

Nếu người dùng chưa nói rõ loại tin, hỏi trước bằng AskUserQuestion. Kèm câu hỏi phụ: chủ đề,
tệp phụ huynh (cấp học / cơ sở), mục tiêu (thông báo / kéo traffic / thu lead / mời sự kiện),
và link đích.

## Bước 2 — Kiểm tra ngân sách trước khi viết Broadcast

Đọc `outputs/zalo-broadcast-ledger.md`. Nếu tháng hiện tại đã dùng đủ 4 tin, **dừng lại và báo**:
đề xuất hạ xuống Bài viết OA, hoặc xếp lịch sang tháng sau, kèm bảng các tin đã gửi để người
dùng cân nhắc đổi ưu tiên. Nếu tin trước gửi trong cùng ngày, nhắc luật **1 tin/ngày**.

Sau khi người dùng chốt, ghi thêm một dòng vào sổ.

## Bước 3 — Thông số kỹ thuật phải tuân thủ

**Bài viết OA:**

- Tiêu đề: **<= 150 ký tự** (nên 40–70 để không bị cắt trên mobile)
- Mô tả / tóm tắt: **<= 300 ký tự**
- Tên tác giả: <= 50 ký tự · Chữ trên nút CTA: <= 50 ký tự
- Ảnh bìa: `.png` / `.jpg`, **<= 15MB**, tỉ lệ **16:9**, đặt nội dung quan trọng trong vùng an toàn **14:9**
- Video: **<= 50MB**, hoặc nhúng từ Facebook, Zing MP3, Dailymotion, Vimeo, Zalo Video
- Có thể liên kết tối đa 6 bài viết hoặc 3 video liên quan
- Số bài đăng mỗi tháng phụ thuộc gói dịch vụ OA đang dùng

**Tin Broadcast:**

- Tối đa **5 nội dung** trong một tin (ảnh, video, bài viết)
- Khung giờ gửi **6:00–20:00**; đặt lịch ngoài khung sẽ tự dời sang hôm sau
- Có thể lọc người nhận theo độ tuổi, giới tính, khu vực, hệ điều hành
- Khung giờ đề xuất cho phụ huynh: **19:30–20:00** các ngày trong tuần, hoặc **9:00–10:00** thứ Bảy

**ZNS:** viết theo template đã đăng ký, các trường tham số điền bằng `{{ten_tham_so}}`; nội dung
phải trung tính, đúng sự việc, không có ngôn ngữ khuyến mãi.

Luôn in ra số ký tự thực tế bên cạnh mỗi trường có giới hạn, dạng `(87/150)`.

**Quy tắc link (từ 07/09/2026, yêu cầu của anh Dương):** trường "Thân bài" / "Mô tả" của Bài viết
OA, Broadcast và ZNS không được chứa URL hay tên miền viết dạng chữ. Zalo OA đã có sẵn trường
"Link đích" riêng gắn với nút CTA, nên link thật luôn đặt ở đó, tách khỏi phần chữ người đọc thấy
trong thân bài, không cần và không dùng cách nhắc "xem link ở bình luận" như Facebook.

## Bước 4 — Công thức viết theo từng định dạng

### Bài viết OA — khung 5 khối

1. **Tiêu đề nêu lợi ích cụ thể**, không giật tít. Đúng: "5 câu hỏi giúp con kể chuyện trường lớp
   mỗi tối". Sai: "Bí mật ít ai biết khiến con thay đổi hoàn toàn".
2. **Mô tả 2 câu** trả lời: bài này giúp anh/chị điều gì, mất bao lâu để đọc.
3. **Thân bài dạng danh sách đánh số**, mỗi mục có câu nói nguyên văn hoặc bước làm cụ thể.
   Đoạn ngắn 2–3 dòng — phụ huynh đọc trên điện thoại giữa hai việc.
4. **Khối tin cậy**: một dòng gắn với thực tế trường (số cơ sở, số năm hoạt động, tên chương trình
   giáo dục đang áp dụng) — chỉ dùng dữ kiện có thật.
5. **Một CTA duy nhất**; link bài blog gốc trên truongvietanh.com đặt ở trường "Link đích" riêng,
   không viết URL hay tên miền trong thân bài.

### Tin Broadcast — khung 4 dòng

Broadcast hiện ra như một tin nhắn. Viết như tin nhắn, không như bài đăng:

```
[Dòng 1 — lợi ích hoặc thông tin cốt lõi, <= 60 ký tự, đọc được ở preview]
[Dòng 2–3 — 5W1H gọn: cái gì, cho ai, khi nào, ở đâu]
[Dòng 4 — một CTA duy nhất, động từ rõ ràng]
[Ký: Trường Việt Anh]
```

Không mở đầu bằng lời chào dài. Preview trên màn hình khoá chỉ hiện được khoảng 60 ký tự đầu —
đó là toàn bộ cơ hội để phụ huynh quyết định mở.

### ZNS — khung thông báo

Một sự việc, một hành động. Trường thông tin rõ ràng, không tính từ cảm xúc, không emoji trang
trí. Ví dụ đúng: xác nhận lịch tham quan trường, nhắc hạn nộp hồ sơ, thông báo lịch khai giảng.

## Bước 5 — Chấm điểm bắt buộc, ngưỡng 90/100

| # | Tiêu chí | Điểm | Cách chấm |
|---|---|---|---|
| 1 | **Đúng loại tin** | 15 | Nội dung khớp định nghĩa loại tin đã chọn (10đ); không có yếu tố quảng cáo trong ZNS (5đ) |
| 2 | **Đúng thông số kỹ thuật** | 15 | Mọi trường trong giới hạn ký tự, có in số đếm (8đ); ảnh/video đúng tỉ lệ và dung lượng (4đ); khung giờ gửi hợp lệ (3đ) |
| 3 | **Văn phong Zalo** | 20 | Xưng hô trang trọng, tiếng Việt thuần có dấu, không lỗi chính tả (8đ); không hashtag, không CAPS, không !!! (6đ); câu ngắn, đọc được trên mobile (6đ) |
| 4 | **Giá trị dùng ngay** | 15 | Phụ huynh làm được điều gì đó sau khi đọc, trong 24h (15đ); chỉ là thông tin để biết (6đ) |
| 5 | **Tín hiệu tin cậy** | 15 | Có dữ kiện thật của trường (5đ); thông tin liên hệ rõ ràng (5đ); không claim tuyệt đối về kết quả học tập (5đ) |
| 6 | **CTA và đường chuyển đổi** | 12 | Đúng một CTA, động từ rõ (6đ); đường chuyển đổi ngắn nhất, ưu tiên hoàn tất trong Zalo hoặc landing page tối ưu mobile (6đ) |
| 7 | **Tôn trọng người nhận** | 8 | Không dùng nỗi sợ để thúc ép (4đ); tần suất hợp lý, không trùng tin đã gửi trong 14 ngày (4đ) |

Dưới 90: sửa mục mất điểm rồi chấm lại, tối đa 2 vòng. Sau 2 vòng vẫn dưới 90 → không bàn giao,
báo rõ điểm yếu còn lại và chất liệu cần bổ sung. Luôn hiển thị bảng điểm.

Khi nội dung dùng để **chạy quảng cáo Zalo** (Zalo Feed / Zalo Article Ad), chấm thêm bằng
`zalo-ads-scorer` trước khi bàn giao.

## Bước 6 — Định dạng output

```
# [Tên nội dung] — [Loại tin]

## Thông số
Loại tin: | Người nhận: | Khung giờ gửi đề xuất: | Tin broadcast số __/4 của tháng __

## Nội dung sẵn sàng đăng
**Tiêu đề (87/150):** ...
**Mô tả (214/300):** ...
**Thân bài:** ...
**Nút CTA (18/50):** ...
**Link đích:** ...

## Yêu cầu hình ảnh
[Mô tả ảnh bìa 16:9, nội dung chính nằm trong vùng 14:9, bối cảnh Việt Nam, học sinh Việt Nam]

## Bảng điểm: XX/100

## Checklist trước khi bấm gửi
- [ ] Đã đối chiếu sổ ngân sách broadcast
- [ ] Ảnh đúng tỉ lệ, dưới 15MB
- [ ] Link đích mở được trên điện thoại
- [ ] Chủ kênh đã duyệt
```

Sau khi người dùng chốt gửi, cập nhật `outputs/zalo-broadcast-ledger.md`.

## Nguồn thông số

Thông số kỹ thuật và chính sách trong skill này lấy từ tài liệu chính thức Zalo Official Account
(oa.zalo.me — hướng dẫn tạo bài viết, hướng dẫn tin Truyền thông, chính sách gửi tin và phí gửi
tin, tài liệu ZNS). **Zalo thay đổi chính sách khá thường xuyên** — nếu người dùng báo có gì khác
với thực tế trên OA của trường, tin người dùng và cập nhật lại skill.
