# Prompt dựng video tự động từ source đã quay

Mục tiêu: người quay đổ thẻ, đặt tên file đúng quy tắc, rồi DÁN prompt (sinh sẵn trong
kịch bản) vào công cụ dựng AI (Descript prompt_project_agent, hoặc AI/người dựng bất kỳ)
là ra bản nháp đầu tiên mà không cần hỏi lại. Prompt phải TỰ CHỨA: cấu trúc block, toàn bộ
lời dẫn, quy tắc phụ đề, thông số thương hiệu.

## Quy tắc đặt tên file (điều kiện sống còn của dựng tự động)

`[Block][Số shot]-[Máy]-[ghi chú tuỳ chọn].mp4`
- Ví dụ: `B4-03-A-an-trua.mp4` = block 4, shot 03, máy A. Bản dọc thêm hậu tố `-doc`.
- Mã shot trong shot-list của kịch bản chính là tên file → người quay chỉ việc đổi tên
  theo cột đầu tiên của bảng shot.
- Thư mục: `source/[so-tap]-[co-so]/` chứa toàn bộ clip phẳng (không chia thư mục con);
  thêm `source/.../audio/` nếu ghi âm rời; `assets/` chứa logo + nhạc.
- Clip hỏng/nhầm vẫn giữ, thêm hậu tố `-x` để máy dựng bỏ qua.

## Thông số thương hiệu (điền vào mọi prompt)
- Tập TVA chuẩn: Navy #26275D (nền title/phụ đề nhấn), Vàng #F9DD0E (accent — chữ trên
  nền vàng phải là Navy, không dùng chữ trắng). Font: Be Vietnam Pro (fallback Arial).
- RIÊNG tập MGIS: xanh lá #046F4A + vàng #F5A623 (CTA chữ trắng).
- Phụ đề: bật toàn bộ thoại; cỡ to đọc được trên điện thoại; 1–2 dòng; đặt vùng an toàn
  dưới khung hình. Bản cuts dọc: phụ đề to hơn nữa (85% người xem không bật tiếng).
- Nhạc: nhẹ, không lời, không lấn thoại (nguồn có bản quyền của team); block 7 để tiếng
  hiện trường là chính, nhạc rất nhỏ hoặc tắt.

## Template PROMPT BẢN DÀI (điền phần {...} theo kịch bản)

```
Bạn là người dựng phim cho video tài liệu "Một Ngày Của {Tên} — {twist}" (tập {N} series
"1 Ngày Của Học Sinh Việt Anh"). Nguồn: thư mục source/{tap}/, file đặt tên theo mã
[Block][Shot]-[Máy] khớp shot-list dưới. Bỏ qua file có hậu tố -x.

MỤC TIÊU: bản dựng 12–15 phút, giữ chân người xem theo 3 đỉnh: hook 55s đầu — viral
moment giữa — đỉnh cảm xúc ở 85–90% thời lượng.

CẤU TRÚC (theo đúng thứ tự, timecode đích ± 15%):
{dán bảng: block | timecode | dùng file nào | nội dung | lời dẫn đầy đủ của block}

QUY TẮC DỰNG:
1. Cold open: 5s đầu là {câu twist} chữ to giữa hình; tiếp 3 flash-forward lấy từ
   {B4-xx}, {B5-xx}, {B7-xx} (mỗi cảnh ≤1,5s, cảnh B7 chỉ 1s không lộ nội dung); rồi câu
   tự giới thiệu của em ({B0-02-A}); title card 2s màu {màu tập này}.
2. Voiceover: dùng đúng lời dẫn từng block ở bảng trên ({giọng đọc: ai đọc / TTS nào}).
   Không thêm lời khen trường. Chỗ nào thoại thật của nhân vật hay hơn lời dẫn → ưu tiên
   thoại thật, cắt lời dẫn.
3. Giữ khoảnh khắc "không hoàn hảo" tự nhiên (cười, vấp, chê món ăn) — đó là chất tài
   liệu. Cắt: khoảng chết >3s không có hành động, mặt các em không có consent (nếu lỡ
   dính → chọn góc khác hoặc làm mờ).
4. Phụ đề toàn bộ thoại, {thông số phụ đề + màu}. Caption giới thiệu nhân vật 1 dòng ở
   {B1}. Quotable facts hiện chữ trên hình tại {liệt kê 2–3 mốc}.
5. Nhạc nền {nguồn}, block 7 ưu tiên tiếng hiện trường. Âm lượng thoại > nhạc.
6. Kết: {câu kết của em} + end screen tập sau + 1 dòng CTA "{CTA quiz + link}".
XUẤT: 16:9 1080p, kèm file phụ đề .srt riêng.
```

## Template PROMPT 5 CUTS DỌC (chạy sau khi có bản dài)

```
Từ cùng thư mục source (hoặc từ bản dài đã dựng), cắt 5 video dọc 9:16, 60–90s/video,
mỗi video đứng độc lập với người CHƯA xem bản dài:
1. {Cut giờ ăn trưa}: mở bằng 2s "{hook cut 1}", quy trình ăn trưa rút gọn, chốt bằng
   fact "{quotable fact}".
2. {Cut khoảnh khắc đáng yêu}: nguyên đoạn {B3-xx}, không voiceover, chỉ phụ đề.
3. {Cut đỉnh cảm xúc}: từ {B7-xx}, mở bằng 1 câu bối cảnh, để trọn cảm xúc, KHÔNG nhạc
   kịch tính chồng lên.
4. {Cut routine sáng}: dựng nhịp nhanh theo format "get ready with me".
5. {Cut tự chọn theo tập}: {mô tả}.
Phụ đề to {thông số}, câu hỏi kéo comment ở cuối mỗi cut: "{câu hỏi}". Không logo đầu
video, logo mờ góc trên từ giây 3. Xuất 1080×1920 + cover frame mỗi cut.
```

## Hướng dẫn riêng khi dùng Descript (nếu MCP Descript có kết nối)
1. `import_media`: tải toàn bộ thư mục source vào 1 project tên `1Ngay-{tap}-{co-so}`.
2. `prompt_project_agent`: dán PROMPT BẢN DÀI ở trên (đã điền đủ) — agent của Descript
   đọc được tên file nên quy tắc đặt tên là bắt buộc từ trước khi upload.
3. Duyệt bản nháp theo transcript, sửa bằng lệnh văn bản tiếp theo (cắt filler, chỉnh
   đoạn) thay vì kéo timeline.
4. Bản cuts: chạy tiếp PROMPT CUTS trong cùng project; `export_timeline` nếu team muốn
   tinh chỉnh trong Premiere/Resolve; `publish_project` lấy link duyệt nội bộ.
5. Không có Descript → 2 prompt trên đưa nguyên cho người dựng (hoặc CapCut/AI khác) —
   chúng được viết để con người đọc cũng triển khai được.

## Nhắc trong kịch bản (mục 8)
In đậm 1 dòng ngay đầu mục 8: "Điều kiện để prompt này chạy được: đặt tên file theo mã
shot NGAY KHI ĐỔ THẺ (cột 1 của bảng shot-list) — mất 15 phút, tiết kiệm 1 ngày dựng."
