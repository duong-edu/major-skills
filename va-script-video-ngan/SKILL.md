---
name: va-script-video-ngan
description: >
  Viết kịch bản video ngắn 15–60 giây cho TikTok, Instagram Reels, YouTube Shorts và Facebook
  Reels, từ một chủ đề hoặc từ hạt nhân nội dung của một bài blog. Skill sinh 10 phương án hook,
  chọn hook mạnh nhất, viết kịch bản 4 nhịp, rồi rẽ theo hai nhánh sản xuất mà người dùng chọn:
  QUAY THẬT (shotlist từng giây, lời thoại nguyên văn, ghi chú máy–ánh sáng–âm thanh, checklist
  đạo cụ) hoặc AI DỰNG (timeline theo giây, prompt tạo ảnh/video bối cảnh Việt Nam, hướng dẫn
  bàn giao cho va-short-reel hoặc va-video-editing). Có bảng điều chỉnh theo từng nền tảng và
  chấm điểm 100 với ngưỡng 90. LUÔN dùng skill này khi người dùng nói: "viết script TikTok",
  "kịch bản video ngắn", "script reel", "làm short từ bài này", "viết kịch bản 30 giây",
  "script video dọc", "kịch bản quay video ngắn", "video ngắn cho fanpage", hoặc khi cần chuyển
  một nội dung có sẵn thành video dưới 60 giây.
---

# VA Script Video Ngắn — TikTok / Reels / Shorts

## Phạm vi

Skill này viết **kịch bản**, không dựng video. Sau khi có kịch bản: nhánh quay thật giao cho
người quay; nhánh AI dựng giao cho `va-short-reel` (Remotion) hoặc `va-video-editing` (FFmpeg).
Nếu đã có sẵn video dài và chỉ cần cắt, **dùng `va-long-to-short` thay vì skill này**.

## Bước 1 — Hỏi 4 câu trước khi viết

Dùng AskUserQuestion, chỉ hỏi phần còn thiếu:

1. **Nền tảng chính**: TikTok / Instagram Reels / YouTube Shorts / Facebook Reels. Cho phép chọn
   nhiều — skill sẽ viết một kịch bản lõi và ghi chú điều chỉnh cho từng nền tảng.
2. **Độ dài**: 15s / 30s / 45s / 60s. Mặc định 30s nếu không nói.
3. **Chế độ sản xuất**: **QUAY THẬT** hay **AI DỰNG**. Đây là câu hỏi quan trọng nhất — nó đổi
   hoàn toàn cấu trúc output.
4. **Người xuất hiện**: anh Dương / giáo viên / học sinh (cần xác nhận đã có quyền hình ảnh) /
   không có người, chỉ chữ và B-roll.

Hỏi thêm khi cần: chủ đề và chất liệu thật, tệp phụ huynh (cấp học), link đích của CTA.

## Bước 2 — 10 hook, chọn 1

Sinh **10 phương án hook cho 3 giây đầu**, mỗi phương án ghi rõ dạng và câu nói nguyên văn.
Trình bảng cho người dùng, kèm đề xuất của mình và lý do một dòng.

Sáu dạng hook hiệu quả với phụ huynh Việt Nam:

| Dạng | Khung | Ví dụ |
|---|---|---|
| Phủ định số đông | "Phần lớn phụ huynh vẫn..." | "Phần lớn phụ huynh vẫn hỏi con câu này mỗi tối. Và con không bao giờ trả lời thật." |
| Sai lầm tôi từng mắc | "Tôi từng... cho đến khi..." | "Tôi từng ép con học thêm 3 ca. Đến khi con nói một câu, tôi dừng hết." |
| Con số gây sốc | "[Số] [đơn vị]..." | "15 phút mỗi tối. Đó là toàn bộ thời gian cần để con đọc trôi chảy." |
| Câu hỏi trực diện | "Anh chị có biết...?" | "Anh chị có biết con im lặng ở nhà nhưng nói rất nhiều ở lớp không?" |
| Cảnh mở giữa hành động | Vào thẳng cảnh, chưa giải thích | Cảnh đứa trẻ đóng sập cửa phòng — rồi mới nói |
| Lời hứa có deadline | "Trong [thời gian], anh chị sẽ..." | "Trong 40 giây tới, anh chị sẽ có 3 câu hỏi khiến con kể chuyện trường lớp." |

Hook phải **không spoil hết** nội dung, và phải nói được khi **tắt tiếng** — vì phần lớn lượt
xem đầu tiên là không có âm thanh. Mọi hook đều phải có bản chữ trên màn hình.

## Bước 3 — Kịch bản 4 nhịp

| Nhịp | Thời lượng (bản 30s) | Nhiệm vụ |
|---|---|---|
| **1. Hook** | 0–3s | Chặn ngón tay lướt. Chữ to trên màn hình. Không logo, không intro. |
| **2. Lật / Bằng chứng** | 3–8s | Nêu vì sao cách làm cũ không hiệu quả, hoặc đưa dẫn chứng thật. Đây là chỗ tạo niềm tin. |
| **3. Giá trị dùng ngay** | 8–25s | 2–3 điểm cụ thể, mỗi điểm một câu nói nguyên văn hoặc một hành động làm được tối nay. |
| **4. Chốt + CTA mềm** | 25–30s | Một câu đóng gói ý chính + một lời mời nhẹ (lưu lại, gửi cho người cần, đọc bài đầy đủ ở bio). Không bán tuyển sinh trực tiếp trong video giá trị. |

Quy tắc nhịp: **cứ 3 giây phải có một thay đổi** — đổi góc máy, đổi chữ trên màn hình, đổi cảnh,
hoặc một cú cắt. Video 30 giây không đổi gì trong 8 giây là video mất người xem.

## Bước 4A — Nhánh QUAY THẬT

Xuất bảng shotlist từng giây:

| Giây | Hình | Lời thoại (nguyên văn) | Chữ trên màn hình | Ghi chú sản xuất |
|---|---|---|---|---|
| 0–3 | Cận mặt, ngang tầm mắt | "..." | "..." | Ánh sáng cửa sổ bên trái, quay dọc 9:16 |

Kèm theo:

- **Lời thoại đầy đủ** dạng liền mạch để người nói học thuộc hoặc đọc teleprompter.
- **Danh sách B-roll cần quay** (mỗi cảnh 3–5 giây, quay dư gấp đôi).
- **Checklist thiết bị và đạo cụ**: điện thoại dọc, chân máy hoặc điểm tựa, micro cài áo nếu quay
  ngoài trời, đạo cụ cụ thể.
- **Ghi chú âm thanh**: quay trong phòng có rèm/thảm để giảm vang; không quay cạnh quạt trần.
- **Hướng dẫn nói trước máy quay**: nhìn thẳng ống kính ở nhịp 1 và 4; nói chậm hơn bình thường
  10%; sai thì dừng 2 giây rồi nói lại cả câu, đừng quay lại từ đầu.

## Bước 4B — Nhánh AI DỰNG

Xuất timeline theo giây + prompt sinh hình:

| Giây | Lớp hình | Prompt tạo ảnh/video | Chuyển cảnh | Chữ động |
|---|---|---|---|---|

Quy tắc prompt — **bắt buộc bối cảnh Việt Nam**:

- Người Việt Nam, trẻ em Việt Nam, đồng phục học sinh Việt Nam, lớp học và nhà ở Việt Nam.
- Mô tả rõ: độ tuổi, trang phục, bối cảnh, ánh sáng, cảm xúc, góc máy, tỉ lệ 9:16.
- Không tạo hình ảnh trẻ em có thể nhận diện là học sinh có thật của trường.
- Không dùng hình ảnh gây lo sợ về trẻ em (khóc, bị phạt, cô lập) để làm đòn bẩy cảm xúc.

Kèm theo: gợi ý giọng đọc (nam/nữ, tốc độ, vùng miền), nhạc nền theo mood, và **bàn giao**:
video có motion graphics → `va-short-reel`; video ghép ảnh + phụ đề + đổi tỉ lệ → `va-video-editing`.

Luật chống "trông như AI làm" (theo `va-short-reel`): không easing tuyến tính, bắt buộc stagger,
Ken Burns cho mọi ảnh tĩnh, tối thiểu 5 lớp hình mỗi cảnh, và **render xong phải tự soi từng
khung hình** trước khi giao.

## Bước 5 — Điều chỉnh theo nền tảng

| Nền tảng | Điều chỉnh bắt buộc |
|---|---|
| **TikTok** | Hook trong 1,5s đầu (nhanh hơn các nền tảng khác). Cân nhắc sound đang trend. Cảm giác UGC — hơi mộc tốt hơn quá bóng bẩy. Chữ tránh vùng đáy 15% (bị che bởi caption và nút). |
| **Instagram Reels** | Thẩm mỹ cao hơn, transition mượt. Khung hình đầu phải đẹp vì nó là ảnh bìa trên lưới. |
| **YouTube Shorts** | Hook dạng cụm từ đọc được; kết cần vòng lặp (câu cuối nối lại câu đầu) để tăng lượt xem lại. Tiêu đề Shorts quan trọng gần bằng hook. |
| **Facebook Reels** | **Phụ đề bắt buộc** — tệp phụ huynh xem tắt tiếng nhiều nhất ở đây. Chữ to hơn 20% so với TikTok. |

Luôn xuất **một bản lõi + bảng điều chỉnh**, không viết lại 4 kịch bản riêng.

## Bước 6 — Chấm điểm, ngưỡng 90/100

| # | Tiêu chí | Điểm | Cách chấm |
|---|---|---|---|
| 1 | **Sức mạnh hook 3 giây** | 20 | Chặn được lướt, có tension hoặc con số (12đ); đọc hiểu được khi tắt tiếng (8đ) |
| 2 | **Nhịp** | 15 | Có thay đổi ít nhất mỗi 3 giây (10đ); không có đoạn chết dài quá 4 giây (5đ) |
| 3 | **Giá trị dùng ngay** | 20 | 2–3 điểm cụ thể, làm được tối nay (20đ); chỉ khuyên chung chung (6đ) |
| 4 | **Tính thật** | 15 | Chất liệu từ chuyện/số liệu có thật, không bịa (10đ); mọi chi tiết chưa xác nhận được đánh dấu `[CẦN XÁC NHẬN]` (5đ) |
| 5 | **Khả thi sản xuất** | 15 | Đội 1–2 người quay được trong 1 buổi, hoặc prompt đủ rõ để dựng (10đ); có checklist/timeline đầy đủ (5đ) |
| 6 | **Đúng nền tảng** | 8 | Có bảng điều chỉnh, chữ nằm ngoài vùng bị che, tỉ lệ 9:16 (8đ) |
| 7 | **An toàn và thương hiệu** | 7 | Không dùng nỗi sợ làm đòn bẩy, không claim tuyệt đối, tôn trọng hình ảnh trẻ em (7đ) |

Dưới 90: sửa rồi chấm lại, tối đa 2 vòng. Sau 2 vòng vẫn dưới 90 → không bàn giao, nêu rõ điểm
yếu. Nếu video dùng để **chạy quảng cáo**, chấm thêm bằng `tiktok-ads-scorer` (TikTok),
`meta-ads-scorer` (FB/IG) hoặc `youtube-ads-scorer` (Shorts/In-feed).

## Bước 7 — Định dạng output

```
# [Tên video] — [Nền tảng] — [Độ dài] — [QUAY THẬT | AI DỰNG]

## Hook đã chọn
[Nguyên văn] — lý do chọn: [1 dòng]
(9 phương án còn lại để ở cuối file, dùng cho A/B test)

## Kịch bản
[Bảng shotlist từng giây HOẶC timeline + prompt, tuỳ nhánh]

## Lời thoại đầy đủ
[Liền mạch, để đọc teleprompter hoặc lồng tiếng]

## Điều chỉnh theo nền tảng
[Bảng]

## Checklist sản xuất
[Thiết bị, đạo cụ, người, địa điểm, thời gian dự kiến] HOẶC [danh sách asset cần sinh]

## Bảng điểm: XX/100

## Bàn giao
[File giao cho ai, bước tiếp theo là gì — không tự đăng]
```

**Không đăng video.** Skill luôn giao file và brief; người thật quyết định đăng.
