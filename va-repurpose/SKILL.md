---
name: va-repurpose
description: >
  Điều phối tái sử dụng (repurpose) MỘT bài blog đã đăng trên truongvietanh.com hoặc
  nguyenmanhduong.com thành gói nội dung đa kênh: post Facebook (fanpage Trường Việt Anh /
  trang cá nhân Nguyễn Mạnh Dương), nội dung Zalo OA (bài viết / tin broadcast / ZNS),
  script video ngắn (TikTok, Reels, Shorts) và script video dài YouTube. Skill tự chấm
  "Repurpose Score" để quyết định bài nào đáng bung ra kênh nào, kiểm tra ngân sách 4 tin
  broadcast Zalo mỗi tháng, gọi đúng skill con để viết thay vì tự viết lại, bắt buộc mọi
  đầu ra đạt >= 90/100 trước khi bàn giao, và đóng gói thành bộ file kèm trạng thái chờ
  người thật duyệt. LUÔN dùng skill này khi người dùng nói: "repurpose bài này", "bung bài
  blog ra các kênh", "chuyển bài blog thành post", "từ blog làm video", "tái sử dụng nội
  dung", "bài này đăng được ở đâu", "làm gói nội dung từ link này", "blog sang Facebook /
  Zalo / TikTok / YouTube", hoặc khi người dùng đưa một URL blog của truongvietanh.com /
  nguyenmanhduong.com kèm yêu cầu tạo nội dung cho mạng xã hội.
---

# VA Repurpose — Từ một bài blog ra gói nội dung đa kênh

## Nguyên tắc lõi

Skill này **không viết nội dung**. Nó **điều phối**: trích hạt nhân từ bài blog, quyết định
bài nào đáng bung ra kênh nào, rồi giao cho skill chuyên trách viết và tự chấm điểm trước
khi bàn giao. Nếu một skill con tồn tại trong môi trường, **luôn gọi skill đó** thay vì tự
viết — vì giọng thương hiệu và công thức đã được mã hoá trong skill con.

Ba luật bất biến:

1. **Không bịa.** Mọi số liệu, tên nhân vật, câu chuyện học sinh phải có trong bài gốc hoặc
   được người dùng xác nhận. Chi tiết chưa xác nhận phải đánh dấu `[CẦN XÁC NHẬN]`.
2. **Không trộn giọng.** Bài từ `nguyenmanhduong.com` mang giọng cá nhân anh Dương, không
   đăng nguyên si lên fanpage trường; và ngược lại. Muốn dùng chéo thì phải viết lại từ hạt
   nhân, không copy.
3. **Không tự đăng.** Skill chỉ tạo bản nháp và file bàn giao. Việc xuất bản luôn do người
   thật bấm nút.

## Bước 0 — Lấy bài và trích hạt nhân

Nhận input: URL, file, hoặc nội dung dán trực tiếp. Với URL, dùng WebFetch để lấy toàn văn.
Nếu không lấy được, yêu cầu người dùng dán nội dung — **không đoán nội dung từ tiêu đề**.

Trích ra **Hạt nhân nội dung** và hiển thị cho người dùng xác nhận trước khi đi tiếp:

```
## Hạt nhân nội dung
- Nguồn: [URL] | Site: truongvietanh.com | nguyenmanhduong.com
- Ngày đăng gốc:
- Luận điểm lõi (1 câu):
- Pain của phụ huynh mà bài chạm tới:
- 3–7 điểm dùng được ngay (mỗi điểm 1 dòng, dạng hành động):
- Số liệu / dẫn chứng có trong bài (kèm nguồn gốc):
- Câu chuyện thật có trong bài (nhân vật, bối cảnh):
- Tệp đối tượng: mầm non / tiểu học / THCS / THPT / phụ huynh chung / nhà giáo dục
- CTA gốc của bài:
- Chất liệu hình ảnh sẵn có:
```

## Bước 1 — TRIAGE: bài này có đáng repurpose không

Không phải bài nào cũng đáng bung ra mọi kênh. Chấm **Repurpose Score** (100 điểm):

| # | Tiêu chí | Điểm | Cách chấm |
|---|---|---|---|
| 1 | **Pain thật, phổ biến** | 25 | Chạm nỗi lo mà >= 30% phụ huynh trong tệp cùng có (25đ); pain ngách hoặc chỉ đúng với một nhóm nhỏ (10đ); chỉ là thông tin nội bộ/tin hoạt động (0đ) |
| 2 | **Chất liệu cụ thể** | 20 | Có số liệu, chuyện thật, ví dụ nguyên văn (20đ); chỉ có lý thuyết chung (5đ) |
| 3 | **Dùng được ngay** | 20 | Phụ huynh áp dụng được trong 24h không cần nghĩ thêm (20đ); phải tự suy ra cách làm (5đ) |
| 4 | **Đúng thời điểm** | 20 | Trúng mùa vụ hiện tại — tuyển sinh T2–T4, trại hè T5–T7, khai giảng T8–T9, thi cử T5–T6, Tết (20đ); trung tính quanh năm (12đ); đã lỗi thời (0đ) |
| 5 | **Không trùng lặp** | 15 | Góc nhìn khác hẳn 4 tuần gần nhất trên kênh đích (15đ); trùng chủ đề nhưng khác góc (8đ); trùng cả chủ đề lẫn góc (0đ) |

**Ngưỡng quyết định:**

- **>= 75** → repurpose toàn kênh phù hợp.
- **55–74** → chỉ bung ra **2 kênh mạnh nhất** cho nội dung đó. Nói rõ vì sao loại các kênh còn lại.
- **< 55** → **khuyến nghị KHÔNG repurpose**. Giữ bài ở blog, nêu 1–2 điều kiện để bài đáng bung
  (ví dụ: "cần thêm một câu chuyện thật của học sinh"). Nếu người dùng vẫn muốn làm, làm — nhưng
  ghi rõ cảnh báo ở đầu gói bàn giao.

Luôn hiển thị bảng điểm này. Đây là công cụ giúp team marketing học cách chọn bài.

## Bước 2 — Ma trận chọn kênh

Chọn kênh theo **nguồn bài** trước, rồi lọc theo Repurpose Score.

### Bài từ `truongvietanh.com` (giọng nhà trường)

| Kênh | Skill gọi | Khi nào làm |
|---|---|---|
| Facebook fanpage trường | `fb-value-sharing` | Mặc định — luôn làm nếu score >= 55 |
| Zalo OA — bài viết | `zalo-oa-writer` (định dạng: bài viết) | Mặc định — không tốn quota broadcast |
| Zalo OA — tin broadcast | `zalo-oa-writer` (định dạng: broadcast) | Chỉ khi score >= 75 **và** còn quota tháng (xem Bước 3) |
| Video ngắn TikTok / Reels / Shorts | `va-script-video-ngan` | Khi hạt nhân có 1 ý lật được trong 3 giây |
| Video dài YouTube | `mkt-youtube-script-writer` | Chỉ khi bài đủ sâu cho 8–15 phút (>= 5 điểm dùng ngay + có chuyện thật) |
| Bài AI cho phụ huynh | `va-kien-thuc-ai` | Khi chủ đề là dùng AI trong học tập / nuôi dạy con |

### Bài từ `nguyenmanhduong.com` (giọng cá nhân anh Dương)

| Kênh | Skill gọi | Khi nào làm |
|---|---|---|
| Facebook cá nhân anh Dương | `fb-post-writer-nmd` | Mặc định — luôn làm |
| Zalo OA — bài viết | `zalo-oa-writer` | Chỉ khi bài có giá trị trực tiếp cho phụ huynh, không phải suy nghĩ cá nhân/nghề nghiệp thuần |
| Video talking-head | `video-chua-lanh-mood` (nếu là chiêm nghiệm) hoặc `va-script-video-ngan` (nếu là bài dạy) | Khi bài mang giọng người thật kể chuyện |
| Video dài YouTube | `mkt-youtube-script-writer` | Khi bài là quan điểm dài có luận cứ |
| Fanpage trường | — | **Không đăng chéo nguyên si.** Nếu muốn, viết lại từ hạt nhân qua `fb-value-sharing` |

Trình bảng đề xuất kênh cho người dùng chọn (dùng AskUserQuestion nếu có), mặc định tick sẵn
kênh đạt điều kiện. Người dùng có quyền bỏ bớt hoặc thêm kênh.

## Bước 3 — Kiểm tra ngân sách Zalo trước khi hứa broadcast

OA đã xác thực chỉ có **4 tin broadcast miễn phí mỗi tháng, tối đa 1 tin/ngày**, và tin chỉ
đến follower đang hoạt động. Đây là tài nguyên khan hiếm nhất trong cả hệ thống kênh.

Trước khi đề xuất broadcast, **luôn đọc sổ ngân sách** `outputs/zalo-broadcast-ledger.md`.
Nếu file chưa có, tạo mới theo mẫu:

```markdown
# Sổ ngân sách tin Broadcast Zalo OA — [Tên OA]
| Tháng | Tin # | Ngày gửi | Chủ đề | Nguồn bài | Người duyệt |
|---|---|---|---|---|---|
```

Quy tắc phân bổ 4 tin/tháng (đề xuất mặc định, người dùng có thể đổi):

1. Một tin **mùa vụ / tuyển sinh** — ưu tiên cao nhất.
2. Một tin **giá trị thuần** (mẹo nuôi dạy con, không bán) để giữ tỉ lệ mở.
3. Một tin **sự kiện / lời mời** (tham quan trường, hội thảo, trại hè).
4. Một tin **dự phòng** — để trống đến tuần cuối tháng cho tin gấp.

Nếu quota đã hết: **hạ cấp xuống bài viết OA** (không tốn quota, follower vẫn xem được trên
trang OA) và xếp lịch broadcast cho tháng sau. Nói rõ điều này với người dùng, đừng im lặng bỏ.

## Bước 4 — Gọi skill con để viết

Với mỗi kênh đã chọn, gọi skill tương ứng và **truyền Hạt nhân nội dung** làm chất liệu, kèm:
link bài gốc (để skill con dùng làm CTA), tệp đối tượng, và các chi tiết `[CẦN XÁC NHẬN]`.

Nếu một skill con không tồn tại trong môi trường, tự viết theo công thức chung của kênh đó và
**ghi rõ ở đầu file**: `Viết trực tiếp, chưa qua skill chuyên trách [tên skill]`.

Mọi đầu ra đều phải giữ **một link về bài blog gốc** — mục tiêu của repurpose không chỉ là
nội dung, mà là kéo lưu lượng và tín hiệu AEO về hai website.

## Bước 5 — Cổng chất lượng 90 điểm (bắt buộc)

Mỗi đầu ra phải qua **hai lớp chấm** trước khi bàn giao:

1. **Rubric nội tại của skill con** (nếu skill con có) — theo ngưỡng riêng của nó.
2. **Cổng chung 90/100** — chấm bằng `mkt-content-scorer`. Nếu đầu ra là creative dùng để
   chạy quảng cáo, chấm thêm bằng scorer nền tảng: `meta-ads-scorer` (FB/IG),
   `tiktok-ads-scorer`, `youtube-ads-scorer`, `zalo-ads-scorer`.

Xử lý khi dưới 90:

- Sửa các mục mất điểm, chấm lại. **Tối đa 2 vòng.**
- Sau 2 vòng vẫn dưới 90 → **không bàn giao bản đó**. Ghi vào bảng điều phối trạng thái
  `KHÔNG ĐẠT (xx/100)` kèm 1–2 dòng nêu điểm yếu và đề xuất chất liệu cần bổ sung.
- Không bao giờ hạ ngưỡng để cho qua.

## Bước 6 — Đóng gói bàn giao

Tạo thư mục `outputs/repurpose/YYYY-MM-DD-<slug-bai>/` gồm:

```
00-tom-tat.md          <- bảng điều phối: kênh, skill dùng, điểm, chủ kênh duyệt, trạng thái
01-fb-fanpage.md       <- caption + carousel + comment ghim + bảng điểm
02-fb-ca-nhan.md
03-zalo-bai-viet.md    <- kèm thông số kỹ thuật (tiêu đề <=150, mô tả <=300 ký tự...)
04-zalo-broadcast.md   <- kèm số thứ tự tin trong tháng và khung giờ gửi đề xuất
05-script-video-ngan.md
06-script-youtube.md
07-brief-hinh-anh.md   <- prompt ảnh/video (bối cảnh Việt Nam, người Việt) + chất liệu cần quay
```

Mỗi file mở đầu bằng khối trạng thái:

```yaml
kenh: Facebook fanpage Trường Việt Anh
nguon: [URL bài gốc]
skill_dung: fb-value-sharing
diem: 93/100
chu_kenh_duyet: [tên người duyệt]
trang_thai: CHỜ DUYỆT
khung_gio_de_xuat: 20:00–21:00 thứ Ba
```

Bảng trong `00-tom-tat.md`:

| Kênh | Skill | Điểm | Trạng thái | Người duyệt | Ghi chú |
|---|---|---|---|---|---|

## Bước 7 — Đăng nháp và giao file

**Bài viết (Facebook, Zalo):** nếu môi trường có kết nối đăng bài (Pancake, n8n, Facebook API,
Zalo OA API), tạo **bản nháp / unpublished** và trả về đường dẫn để người duyệt vào bấm đăng.
**Tuyệt đối không publish trực tiếp**, kể cả khi có quyền. Nếu không có kết nối, xuất file kèm
checklist dán tay theo đúng thứ tự thao tác trên từng nền tảng.

**Video:** luôn **giao file và brief**, không đăng. Nếu người dùng chọn nhánh AI dựng, chuyển
tiếp sang `va-short-reel` (Remotion) hoặc `va-video-editing` (FFmpeg) để render, rồi giao file
MP4 kèm bản phụ đề.

Kết thúc, báo cáo cho người dùng đúng 5 dòng: bài nguồn, Repurpose Score, số kênh đạt / tổng
kênh làm, kênh nào không đạt và vì sao, việc cần người thật làm tiếp.

## An toàn nội dung

- Không đưa tên thật, ảnh, điểm số của học sinh nếu bài gốc không có hoặc chưa được phép.
- Nội dung liên quan AI cho trẻ em: bám chuẩn an toàn của UNESCO & UNICEF như `va-kien-thuc-ai` đã quy định.
- Không claim kết quả học tập tuyệt đối ("chắc chắn giỏi", "cam kết đỗ"). Dùng ngôn ngữ mềm có cơ sở.
- Không dùng nỗi sợ của phụ huynh làm đòn bẩy bán hàng. Chạm pain để giúp, không để doạ.
