---
name: va-short-reel
description: >
  Dựng video Reel/Short/TikTok và motion graphics TỪ ĐẦU bằng Remotion (React render ra
  MP4). Tạo intro/outro, logo animation, video quảng cáo, video "faceless", kinetic
  typography, phụ đề động đồng bộ theo từng từ, ghép ảnh và B-roll thành video. Chứa bộ
  quy tắc thiết kế chuyển động để video không bị "trông như AI làm": cấm easing tuyến
  tính, bắt buộc stagger, Ken Burns cho mọi ảnh tĩnh, 5 lớp hình ảnh mỗi cảnh, và bắt
  buộc render rồi tự soi từng khung hình trước khi giao. Dùng skill này khi người dùng
  nói: "làm video reel", "dựng video từ ảnh", "tạo video quảng cáo", "làm intro/outro",
  "animate logo", "motion graphics", "kinetic typography", "video faceless", "Remotion",
  "video trông generic quá", "làm video đẹp hơn", hoặc muốn tạo video mới mà KHÔNG có
  video quay sẵn. Nếu đã có video dài cần cắt thì dùng va-long-to-short; nếu chỉ cắt
  ghép và thêm phụ đề vào video có sẵn thì dùng va-video-editing.
  LUÔN đọc skill này TRƯỚC KHI viết bất kỳ dòng code Remotion nào.
---

# va-short-reel — Dựng Reel/Short & Motion Graphics bằng Remotion

Remotion renders React components frame-by-frame into video. Code quality is not the
bottleneck — **motion design craft is**. Untrained generation produces linear easing,
opacity-only fades, simultaneous entrances, flat colors, and no texture. That is the
"generic AI video" look. This skill exists to prevent it.

## Non-negotiable rules (apply to EVERY composition)

1. **NEVER use linear interpolation.** Every `interpolate()` gets an easing curve;
   every entrance prefers `spring()`. Always `extrapolateLeft/Right: "clamp"`.
2. **Entrances animate 2–3 properties together** (opacity + translateY + scale).
   A lone fade is forbidden.
3. **Stagger everything.** Lists, words, rays, cards: 3–6 frame offsets. Nothing
   enters simultaneously.
4. **Exits exist and are faster than entrances** (~10 frames vs ~20).
5. **Five-layer stack in every scene**, bottom to top: background mesh → assets →
   graphics/type → color grade → grain + vignette. Never a flat solid background.
6. **Every still image gets Ken Burns** (slow scale 1→1.08 + pan). Every video asset
   uses `<OffthreadVideo>`, never `<Video>`.
7. **Idle elements breathe**: anything on screen >2s gets sin-wave micro-motion.
8. **All timing derives from `fps`** via `useVideoConfig()`. No magic frame numbers.
9. **One theme object** at the top of the project (colors, easings, spring presets,
   fonts). Never inline a hex color or easing in a component.
10. **Render, extract frames, LOOK at them, fix, re-render.** Never deliver an
    unverified render. This loop is mandatory — see Verification below.

## Workflow

### Step 1 — Scope
Determine: duration, fps (30 default; 60 only for heavy fast motion), dimensions
(1080×1920 Reels/Shorts, 1920×1080 landscape), what assets exist (images, footage,
audio, logos), and whether this is a new composition or an edit to an existing project.
If editing an existing project: read `src/` fully first, find the theme (or create one),
and refactor violations of the rules above before adding features.

### Step 2 — Setup
New project:
```bash
npm install remotion @remotion/cli react react-dom
# optional: @remotion/transitions @remotion/motion-blur @remotion/google-fonts
```
Copy `assets/theme.ts` from this skill into `src/theme.ts` and adjust the palette to
the user's brand. Structure: `src/index.ts` (registerRoot) → `src/Root.tsx`
(Composition, duration/fps/size) → `src/scenes/*.tsx` → `src/components/*.tsx`.
User assets go in `public/`, loaded via `staticFile()`.

### Step 3 — Build
Read `references/motion-patterns.md` for the reusable component implementations
(BgMesh, Grade, Grain, Vignette, KenBurns, WordReveal, Stagger, Counter, Spark,
transitions, parallax). Compose scenes from those patterns. For pacing, rhythm,
typography, color palettes, and sound design rules, read
`references/design-rules.md`.

Scene rhythm: HIT → hold (15–20 still frames) → build → HIT. Something must move
in the first 15 frames. Never >90 frames without a new visual element.

### Step 4 — Render
```bash
npx remotion render src/index.ts <CompId> out/video.mp4 --codec h264 --crf 17
```
Remotion needs a Chromium binary. If its auto-download fails (sandboxes, offline CI),
find one and pass it explicitly:
```bash
which chromium chromium-browser google-chrome 2>/dev/null
ls /opt/pw-browsers 2>/dev/null   # Playwright installs live here
npx remotion render ... --browser-executable=<path>
```
If full Chrome errors with "Old Headless mode has been removed", use a
`headless_shell` binary instead (Playwright ships one as
`chromium_headless_shell-*/chrome-linux/headless_shell`).

### Step 5 — VERIFY (mandatory, never skip)
Extract frames at key moments and visually inspect each one. The portable
method — works on machines with no system ffmpeg, renders the exact frame:
```bash
for f in 15 45 90 150; do
  npx remotion still src/index.ts <CompId> out/check_$f.png --frame $f --overwrite
done
```
If system ffmpeg IS available, extracting from the finished mp4 also verifies
the encode itself (`-ss` seeking is more portable than `select=` filters, whose
quoting breaks in some shells and in Remotion's bundled ffmpeg):
```bash
ffmpeg -v error -ss 1.5 -i out/video.mp4 -frames:v 1 check_1.png
```
Look for, and fix, in order of frequency:
- **Spacing bugs**: `gap`/`margin` in `em` resolves against the PARENT font-size
  (often 16px), not the text size — use px values in flex containers around big type.
- Text overflowing or touching frame edges (keep critical content in middle 75%
  vertically for 9:16 — platform UI covers top/bottom).
- Elements visible before their entrance or after their exit (missing clamp).
- Color/contrast failures: hero color on >1 element per frame, dim text unreadable
  over the grade.
- Layer order mistakes (grain/vignette must be on top, grade above content).
Fix → re-render → re-extract → re-inspect. Only deliver after a clean pass.
Then run the final checklist at the bottom of `references/design-rules.md`.

### Editing the user's existing footage
To enhance an existing mp4 (captions, grade, intro/outro) rather than build from
scratch: put the file in `public/`, render it as the asset layer with
`<OffthreadVideo src={staticFile("clip.mp4")} />`, set composition duration from the
clip length, and stack graphics/grade/grain above it. Get the clip's duration and fps
with `ffprobe` before setting up the composition. For word-synced captions over
speech, see the captions section of `references/motion-patterns.md`.

## Tiếng Việt — bắt buộc đọc khi video có chữ tiếng Việt

Phần lớn font display trên Google Fonts **không có đủ dấu tiếng Việt**. Nếu chọn sai
font, chữ sẽ mất dấu hoặc hiện ô vuông, và lỗi này chỉ lộ ra ở bước soi khung hình.

Font Google có hỗ trợ tiếng Việt đầy đủ, đã kiểm chứng: **Be Vietnam Pro** (tốt nhất
cho tiêu đề, có đủ 9 độ đậm), **Montserrat**, **Open Sans**, **Roboto**, **Inter**,
**Lora** (serif), **Bungee** (chữ khối cho hook).

Nạp font trong Remotion:
```tsx
import { loadFont } from "@remotion/google-fonts/BeVietnamPro";
const { fontFamily } = loadFont();
```

Đưa `fontFamily` vào theme object, không inline vào từng component.

Quy tắc riêng cho chữ tiếng Việt:
1. **Dấu chiếm thêm chiều cao.** Chữ như "Ế", "Ộ", "ỡ" cao hơn chữ Latin thường. Đặt
   `lineHeight` tối thiểu `1.3` cho tiêu đề (không dùng `1.0` như với tiếng Anh),
   nếu không dấu bị cắt cụt ở dòng trên.
2. **Không dùng `textTransform: uppercase` cho tiêu đề tiếng Việt** trừ khi đã kiểm tra
   khung hình. Chữ hoa có dấu (Ữ, Ằ, Ộ) rất dễ chạm vào dòng trên hoặc mép khung.
3. **Từ tiếng Việt ngắn hơn tiếng Anh** nhưng câu dài hơn khoảng 20–30%. Khi làm phụ đề
   động, giới hạn 5–7 chữ mỗi dòng thay vì 3–5 như tiếng Anh.
4. **Bước VERIFY là bắt buộc với tiếng Việt.** Khi soi khung hình, kiểm tra riêng: mọi
   dấu thanh (sắc, huyền, hỏi, ngã, nặng) và dấu mũ (ă, â, ê, ô, ơ, ư, đ) đều hiển thị
   đủ, không bị cắt, không thành ô vuông.

Bối cảnh hình ảnh: khi tạo hoặc chọn ảnh/B-roll cho video của người dùng Việt Nam, ưu
tiên bối cảnh và con người Việt Nam trừ khi được yêu cầu khác.

## Reference files
- `references/motion-patterns.md` — copy-paste component library: backgrounds,
  grade/grain/vignette, Ken Burns, text reveals, counters, transitions, parallax,
  audio sync, captions. Read before writing components.
- `references/design-rules.md` — palettes, typography rules, scene architecture,
  sound design, pre-delivery checklist. Read before designing scenes and before
  final delivery.
- `assets/theme.ts` — the theme template to copy into every project.

## Common failure modes to actively avoid
- **Emoji as icons.** Emoji render as full-color platform glyphs (green ✳️,
  blue 🌐) that ignore your palette and silently break the one-hero-color rule,
  and they sit on whatever background you gave them (orange mascot on orange
  tile = invisible). Draw glyphs with CSS/SVG in theme colors, or verify every
  emoji against the extracted frames.
- **No SFX assets is not a reason to ship silent.** Synthesize a minimal kit as
  16-bit WAVs from a Node script (noise-burst whoosh, pitch-drop pop, sine-thump
  kick/bass, detuned-sine pad) into `public/sfx/` — see `examples/scripts/` in
  the repo. Zero downloads, fully deterministic.
- Generating one giant component instead of themed, reusable pieces.
- `durationInFrames` mismatch between Composition and scene content (dead air).
- Forgetting `--overwrite` on re-renders, then inspecting the stale file.
- Fonts: never rely on system defaults for hero text; load a display font via
  `@remotion/google-fonts` or `@font-face` + `staticFile`.
- Trying to "describe" the result to the user instead of rendering and verifying it.
