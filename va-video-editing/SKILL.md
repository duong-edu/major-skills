---
name: va-video-editing
description: >
  Chỉnh sửa video bằng ngôn ngữ tự nhiên với FFmpeg + Whisper — cắt theo mốc thời gian,
  jump cut tự động (xóa khoảng lặng), tạo và burn phụ đề (hormozi / standard / minimal /
  viet có dấu tiếng Việt), chèn text overlay, đổi tốc độ, và chuyển video ngang sang dọc
  9:16 cho Reel/Short/TikTok. Dùng skill này khi người dùng nói: "edit video", "cắt video",
  "chỉnh sửa video", "thêm phụ đề", "thêm sub", "burn caption", "xóa khoảng lặng",
  "jump cut", "làm reel từ video", "chuyển video sang dọc", "9:16", "tăng tốc video",
  "chèn chữ vào video", "trim video", "cắt từ phút X đến phút Y", hoặc bất kỳ yêu cầu
  xử lý file video/mp4 nào bằng dòng lệnh.
---

# va-video-editing — Chỉnh sửa video bằng FFmpeg + Whisper

Skill này điều khiển một bộ script Bash thuần dùng FFmpeg và Whisper. Không cần GPU,
không cần Node.js, không cần Remotion. Phù hợp cho video dài (bài giảng, webinar,
livestream, phỏng vấn) và cả việc chuyển video dài thành Reel/Short dọc.

## Pre-Flight — bắt buộc chạy trước

### 1. Xác định thư mục gốc của skill

```bash
VE_ROOT=""
for dir in "$HOME/.claude/skills/va-video-editing" \
           "$HOME/.claude/skills/video-editing" \
           "$(pwd)"; do
    if [ -f "$dir/SKILL.md" ]; then VE_ROOT="$dir"; break; fi
done
[ -z "$VE_ROOT" ] && echo "ERROR: không tìm thấy thư mục skill va-video-editing"
chmod +x "$VE_ROOT/scripts/"*.sh 2>/dev/null
echo "VE_ROOT=$VE_ROOT"
```

### 2. Kiểm tra phụ thuộc

```bash
command -v ffmpeg  >/dev/null && echo "ffmpeg: OK"  || echo "ffmpeg: THIẾU"
command -v ffprobe >/dev/null && echo "ffprobe: OK" || echo "ffprobe: THIẾU"
command -v whisper >/dev/null && echo "whisper: OK" || echo "whisper: THIẾU (chỉ cần khi làm phụ đề)"
```

Nếu thiếu, hướng dẫn cài:
- macOS: `brew install ffmpeg` và `pip3 install -U openai-whisper`
- Ubuntu/Debian: `sudo apt install ffmpeg` và `pip3 install -U openai-whisper`

Whisper chỉ cần khi người dùng yêu cầu phụ đề. Các thao tác cắt / jump cut /
overlay / đổi tốc độ / chuyển dọc chỉ cần FFmpeg.

### 3. Đọc thông số video đầu vào

Luôn chạy trước khi xử lý, để biết thời lượng, độ phân giải, tỷ lệ khung hình:

```bash
ffprobe -v error -show_entries format=duration,size \
    -show_entries stream=codec_type,width,height,r_frame_rate \
    -of default=noprint_wrappers=1 INPUT.mp4
```

Báo lại cho người dùng: thời lượng, độ phân giải, dung lượng, và ước tính thời gian xử lý.

## Các thao tác

### Cắt video (trim)

```bash
bash "$VE_ROOT/scripts/trim.sh" video.mp4 --start 00:01:30 --end 00:05:00
```

### Jump cut — xóa khoảng lặng / dead air

```bash
bash "$VE_ROOT/scripts/jumpcut.sh" video.mp4 --threshold -30 --duration 0.5 --padding 0.1
```

- `--threshold`: ngưỡng dB coi là im lặng. Mặc định `-30`. Phòng thu yên tĩnh dùng `-40`;
  quay ở nơi ồn (lớp học, ngoài trời) dùng `-25` hoặc `-20`.
- `--duration`: khoảng lặng tối thiểu bị cắt (giây). Mặc định `0.5`.
- `--padding`: chừa lại bao nhiêu giây quanh đoạn có tiếng, tránh cắt cụt âm đầu/cuối.

Luôn cảnh báo người dùng nghe thử kết quả — jump cut quá tay làm video giật.

### Phụ đề (transcribe + burn)

Bước 1 — tạo file SRT:

```bash
bash "$VE_ROOT/scripts/transcribe.sh" video.mp4 --model base --language vi
```

Model: `tiny` (nhanh, kém chính xác) → `base` → `small` → `medium` → `large`.
**Với tiếng Việt, luôn dùng `small` trở lên**; `base` sai dấu và sai từ rất nhiều.
Luôn truyền `--language vi` cho video tiếng Việt thay vì để tự nhận diện.

Bước 2 — luôn cho người dùng đọc lại file SRT trước khi burn. Whisper thường sai
tên riêng, thuật ngữ và số. Sửa file SRT rồi mới burn.

Bước 3 — burn phụ đề vào video:

```bash
bash "$VE_ROOT/scripts/caption.sh" video.mp4 video.srt --style viet
```

| Style | Mô tả | Dùng khi |
|-------|-------|----------|
| `viet` | Chữ đậm, giữa dưới, viền dày, font đủ dấu tiếng Việt | **Mặc định cho mọi video tiếng Việt** |
| `hormozi` | Chữ rất to, giữa màn hình, kiểu Alex Hormozi | Reel/Short tiếng Anh, cần bắt mắt |
| `standard` | Phụ đề đáy màn hình có nền mờ | Video dài, bài giảng tiếng Anh |
| `minimal` | Chữ nhỏ, lower-third, kín đáo | Video doanh nghiệp, phỏng vấn |

**Quy tắc font (rất quan trọng với tiếng Việt):** style `hormozi`, `standard`,
`minimal` dùng font Arial / Helvetica Neue — trên Linux các font này không tồn tại,
và một số bản Arial Black thiếu dấu tiếng Việt, gây mất dấu hoặc hiện ô vuông.
Nếu nội dung có dấu tiếng Việt, dùng `--style viet`, hoặc ép font thủ công:

```bash
bash "$VE_ROOT/scripts/caption.sh" video.mp4 video.srt \
    --style hormozi --font "Be Vietnam Pro" --fontsize 30
```

Kiểm tra font có sẵn trên máy: `fc-list : family | grep -i <tên font>`
(macOS có sẵn Arial Unicode MS; Linux nên dùng DejaVu Sans hoặc cài Be Vietnam Pro).

Sau khi burn, **luôn trích một khung hình để tự kiểm tra dấu tiếng Việt hiển thị đúng**:

```bash
ffmpeg -v error -ss 5 -i OUTPUT.mp4 -frames:v 1 /tmp/check.png
```

Rồi dùng công cụ Read để xem ảnh đó trước khi báo hoàn thành.

### Chèn text overlay

```bash
bash "$VE_ROOT/scripts/overlay-text.sh" video.mp4 \
    --text "Đăng ký ngay" --start 00:01:00 --end 00:01:05 --position bottom-right
```

Vị trí hỗ trợ: `center`, `top`, `bottom`, `top-left`, `top-right`, `bottom-left`, `bottom-right`.

### Đổi tốc độ

```bash
bash "$VE_ROOT/scripts/edit.sh" video.mp4 --speed 1.25
```

Cao độ giọng nói được giữ nguyên qua bộ lọc `atempo`. Trên 1.5x giọng bắt đầu méo.

### Chuyển video ngang sang dọc 9:16 (Reel / Short / TikTok)

```bash
bash "$VE_ROOT/scripts/vertical.sh" video.mp4 --mode blur
```

| Mode | Mô tả | Dùng khi |
|------|-------|----------|
| `blur` | Video gốc đặt giữa, nền là chính nó phóng to và làm mờ | **Mặc định an toàn** — không mất nội dung nào |
| `crop` | Phóng to và cắt hai bên còn 9:16 | Video talking-head, người ngồi giữa khung |
| `pad` | Video gốc giữa, hai đầu là dải đen | Cần nhìn rõ toàn khung, chấp nhận vùng trống |

Với `crop`, chọn vùng giữ lại bằng `--focus left|center|right`:

```bash
bash "$VE_ROOT/scripts/vertical.sh" phongvan.mp4 --mode crop --focus left
```

**Lưu ý bố cục 9:16:** nội dung quan trọng phải nằm trong khoảng 75% giữa theo chiều dọc.
Phần trên và dưới bị giao diện TikTok/Reels che (nút, caption, avatar). Vì vậy style
`viet` đặt `MarginV=60` để phụ đề không bị che.

### Pipeline gộp nhiều thao tác

```bash
bash "$VE_ROOT/scripts/edit.sh" video.mp4 \
  --trim-start 00:00:10 --trim-end 00:10:00 \
  --jumpcut \
  --caption --caption-style standard --caption-model small --caption-language vi \
  --speed 1.25 \
  --overlay-text "Truong Viet Anh" --overlay-start 00:01:00 \
  --output final.mp4
```

Thứ tự xử lý cố định: **trim → jump cut → speed → caption → overlay**.

Thứ tự này quan trọng: caption phải chạy sau trim và jump cut, nếu không mốc thời gian
trong file SRT sẽ lệch so với video đã bị cắt.

`vertical.sh` chạy **riêng, sau cùng**, không nằm trong `edit.sh`. Quy trình làm reel
từ video dài: trim → jumpcut → vertical → caption.

## Quy trình khi người dùng yêu cầu

1. **Chạy Pre-Flight** — xác định `VE_ROOT`, kiểm tra ffmpeg/whisper, đọc `ffprobe`.
2. **Phân tích yêu cầu** — xác định cần thao tác nào và theo thứ tự nào.
3. **Xác nhận trước khi chạy việc nặng.** Transcribe model `medium`/`large` trên video
   một tiếng có thể mất 20–60 phút trên CPU. Báo ước tính và hỏi trước.
4. **Không bao giờ ghi đè file gốc.** Mọi script đều ghi ra file mới; nếu người dùng
   truyền `--output` trùng file đầu vào, cảnh báo và đổi tên.
5. **Chọn script phù hợp** — một thao tác thì gọi script riêng (nhanh hơn, ít mã hóa lại);
   nhiều thao tác thì dùng `edit.sh`.
6. **Với phụ đề tiếng Việt**: mặc định `--model small --language vi` và `--style viet`.
7. **Tự kiểm tra kết quả** — chạy `ffprobe` trên file đầu ra để xác nhận thời lượng và
   độ phân giải đúng như mong đợi; với video có phụ đề thì trích một khung hình và xem.
8. **Báo cáo** — đường dẫn file đầu ra, thời lượng, độ phân giải, dung lượng.

## Lỗi thường gặp

- **Phụ đề mất dấu / hiện ô vuông**: font không hỗ trợ tiếng Việt. Dùng `--style viet`
  hoặc `--font "DejaVu Sans"`.
- **Lỗi `No such filter: 'subtitles'`**: bản FFmpeg cài thiếu libass. Cài lại FFmpeg
  đầy đủ (`brew install ffmpeg` hoặc gói `ffmpeg` chính thức của distro).
- **Phụ đề lệch thời gian**: đã burn caption trước khi trim hoặc jump cut. Làm lại theo
  đúng thứ tự pipeline.
- **File đầu ra không có tiếng**: video gốc dùng codec âm thanh lạ. Các script đã ép
  `-c:a aac`, nếu vẫn lỗi thì kiểm tra `ffprobe` xem stream audio có tồn tại không.
- **Đường dẫn có dấu cách hoặc dấu tiếng Việt**: luôn đặt trong dấu nháy kép. Nếu
  FFmpeg vẫn lỗi ở bộ lọc `subtitles`, copy file SRT sang `/tmp/sub.srt` rồi dùng
  đường dẫn đó.
- **Video dọc bị mất mặt người khi dùng `--mode crop`**: đổi sang `--focus left/right`
  hoặc dùng `--mode blur`.

## Bảng tra script

| Script | Chức năng |
|--------|-----------|
| `scripts/edit.sh` | Orchestrator chính — gộp trim, jumpcut, speed, caption, overlay |
| `scripts/trim.sh` | Cắt theo mốc thời gian |
| `scripts/jumpcut.sh` | Tự động xóa khoảng lặng |
| `scripts/transcribe.sh` | Whisper → file SRT |
| `scripts/caption.sh` | Burn SRT vào video theo style (có style `viet`) |
| `scripts/overlay-text.sh` | Chèn chữ theo vị trí và thời điểm |
| `scripts/vertical.sh` | Chuyển 16:9 sang 9:16 cho Reel/Short (crop/blur/pad) |

## Yêu cầu hệ thống

- **ffmpeg + ffprobe** — bắt buộc, phải có libass để burn phụ đề
- **whisper** (`pip3 install -U openai-whisper`) — chỉ cần khi tạo phụ đề
- Không cần GPU. Có GPU thì Whisper chạy nhanh hơn nhiều.

---

Dựa trên [6missedcalls/video-editing-skill](https://github.com/6missedcalls/video-editing-skill)
(MIT License). Đã bổ sung: YAML frontmatter, hỗ trợ font và phụ đề tiếng Việt,
script chuyển video dọc 9:16, kiểm tra phụ thuộc, và quy trình tự kiểm tra kết quả.
