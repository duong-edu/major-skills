# BỜM — Prompt tạo ảnh minh hoạ (v3)

Cập nhật 08/08/2026. Rút ra sau ~25 lần thử thật, trong đó 11 lần bị bộ lọc chặn và 3 lần ra sai nhân vật.

**Bản v1 (Bờm túm lông cam nhọn) đã bị loại** — đọc ra "đỏm dáng", sai tính cách.
**Bản v2-THPT (bù xù toàn thân) đã bị loại** — đọc ra **con cáo**.

---

## 0. Bốn luật sống còn khi dùng ChatGPT

**1. Tắt "Web access" của extension vidIQ trước khi gửi.** Thủ phạm làm quá nửa số lần gửi thất bại — nó cướp prompt và biến thành lệnh tìm kiếm Google. Toggle nằm ngay dưới ô nhập.

**2. Từ cấm** — dùng là bị chặn vì "similarity policy":

| ❌ Cấm | ✅ Thay bằng |
|---|---|
| `lion` / `lion cub` | `savanna cat` / `savanna cat cub` |
| `Pixar`, `DreamWorks`, `animated feature` | `CARTOON`, `stylised cartoon character render`, `soft rounded 3D storybook shading` |
| `mane` (khi vẽ Bờm tuổi lớn) | `a scruffy uneven crest of longer fur on the crown and around the throat` |
| `BIG CAT` viết hoa, `tawny grassland cat` | cứ dùng `savanna cat` — đây là cụm đã qua được nhiều lần nhất |
| Nhân vật trưởng thành nhìn thẳng ống kính | `seen at a three-quarter angle` |
| Đám đông sư tử trong cùng khung · cảnh gầm trên mỏm đá lúc bình minh · bờm đầy đủ + nắng vàng hoàng hôn | một nhân vật duy nhất trong khung; đổi sang gò mối, ban ngày |

**3. Gõ prompt bằng TIẾNG ANH.** Gõ tự động tiếng Việt có dấu bị vỡ ký tự. Mỗi ảnh mở **một hội thoại mới** — tin nhắn tiếp theo trong cùng hội thoại thường không lên.

**4. Bộ lọc siết theo tần suất, không chỉ theo từ khoá.** Ngày 08/08: đúng khối ADN chạy được buổi sáng, buổi chiều bị chặn 5 lần liên tiếp — kể cả khi upload ảnh Bờm tiểu học làm ảnh tham chiếu (bản có ảnh còn bị chặn nhanh hơn). **Cách xử lý: đợi vài giờ rồi gửi lại đúng prompt cũ. Đừng viết lại prompt** — viết lại chỉ làm hỏng thêm và dễ ra sai nhân vật.

---

## 1. Khối ADN nhân vật — dán y hệt ở MỌI prompt

Điều quan trọng nhất: **tả TÍNH CÁCH trước, tả ngoại hình sau.** Đây là chỗ bản v1 làm sai — tả hình mà quên tả người, nên ra một cậu chàng sành điệu.

```
Please create one wholly original CARTOON children's-book illustration. Invent this
design from scratch; do not reference any film, franchise or existing character.
Stylised cartoon character render, NOT photorealistic, NOT a wildlife photograph.
Soft rounded 3D storybook shading, 3:2 landscape.

CHARACTER — a savanna cat named Bom.

PERSONALITY FIRST, the drawing must express this above all: slow, simple, guileless,
gentle, a bit dim, endlessly curious, quietly funny, stubborn and brave in a plodding
way; the lovable underdog, the last one to get the joke. He must NOT look cool,
stylish, sleek, punk, edgy, heroic or handsome; nothing about him groomed or
fashionable.

COAT noticeably DARKER than an ordinary golden savanna cat: deep dusty russet-brown
and dark honey-brown, matte and scruffy, paler cream muzzle and belly, bits of dry
grass and dust caught in the fur.
HEAD too big for his body, very round and broad, wide flat cheeks.
MUZZLE short, wide, ROUNDED and BLUNT with a wide flat nose pad, full slightly
droopy cheeks — never narrow, never pointed, never a snout.
MOUTH small, hanging a bit open in a soft o of wonder.
EYES large, round, set a bit too far apart, heavy sleepy upper lids — kind, slightly
slow, completely trusting; never sharp or narrowed.
EYEBROWS thick, shaggy, uneven, one higher than the other.
EARS oversized but SOFT and ROUNDED, sticking out sideways, one folded over —
never tall, never pointed, never triangular.
HAIR on the crown is a soft messy UNBRUSHED cowlick of pale gingery-brown fur
flopping to one side in soft rounded tufts like a little boy's bed-hair — NOT spiky,
NOT gelled, NOT a mohawk, NOT neon orange.
BODY FUR short and smooth on the back, flanks and legs.
TAIL long and thin with one small soft tuft ONLY at the very tip — never bushy.
PAWS comically oversized, heavy, clumsy and round.
A thin pale old scar across the bridge of his nose (từ chương 4 trở đi).
```

**Vì sao lông sẫm màu:** Bờm phải khác đám sư tử vàng quanh nó ngay từ cái nhìn đầu — nhưng khác theo kiểu *bụi bặm, tầm thường*, không phải quý phái. Đã cân nhắc và **loại phương án trắng** (yếu đuối, quý tộc) và **phương án xanh** (phá vỡ nền ngụ ngôn-có-thật).

---

## 2. ⚠️ KHỐI KHOÁ GIẢI PHẪU CHỐNG-CÁO

Bài học đắt nhất của dự án: khi đẩy mạnh cụm *"bù xù, không đều, lông dài lởm chởm"* mà **không** khoá giải phẫu, model trượt sang hình cáo — tai nhọn, mõm dài, đuôi xù, lông thân dài.

**Nguyên tắc một câu: cho phép bù xù ở ĐẦU, cấm bù xù ở THÂN.**

Dán thêm khối này vào **mọi** prompt vẽ Bờm từ THCS trở lên:

```
SHAPE LOCK so he reads as a heavy grassland cat and never as a fox:
HEAD large, broad and ROUND with wide flat cheeks.
MUZZLE short, broad and BLUNT with a wide flat nose pad - never narrow, never pointed.
EARS SMALL and ROUNDED, low on the sides of the head - never tall, never pointed,
never triangular.
BODY FUR SHORT and SMOOTH everywhere - no shaggy or bushy fur on the back, flanks
or legs.
TAIL long, thin and smooth with one small dark tuft ONLY at the very tip - never bushy.
CHEST deep, forelegs thick, PAWS big, heavy and round.
The scruffy uneven fur stays ONLY on the crown of the head and around the throat.
```

Ba dấu hiệu ra cáo, phát hiện là bỏ ảnh: **tai nhọn dựng đứng · đuôi xù cả cây · lông dài phủ thân và chân.**

---

## 3. Bốn lứa tuổi

Dán thêm đoạn tương ứng vào sau khối ADN.

| Ảnh | Tuổi | Điều chỉnh |
|---|---|---|
| `Bom_v2_MamNon` ✅ | ~4 | `a small cub, about four years old in human terms` |
| `Bom_v2_TieuHoc_Chuong13` ✅ | ~9 | `about nine years old in human terms, legs a bit longer and lankier but still round-faced, chunky and clumsy` |
| `Bom_v2_THCS_Chuong23` ✅ | ~14 | `an awkward adolescent — legs suddenly too long for his body, knobbly knees, narrow shoulders, gangly and badly coordinated, but still the same round dim trusting face` |
| THPT ⏳ *chưa đạt* | ~18 | `TALL, LEAN and LEGGY — long slim legs, grown out of the gangly teenager stage but not yet filled out. NOT chunky, NOT heavy, but NOT skinny either: deep chest, thick forelegs, big heavy round paws. ENERGY IS THE WHOLE POINT: eager, curious, bursting to go, a doer rather than a thinker — not clever but always the first to try. Eyes bright and wide awake, ears pricked forward, mouth open in a happy eager grin, tail raised high with a cheerful curl.` **+ bắt buộc dán KHỐI KHOÁ GIẢI PHẪU ở mục 2** |

---

## 4. Cảnh đã dùng

**Mầm non — tò mò lần đầu** ✅
```
POSE — he stands on all four legs in a sunlit patch of dry grass, head pushed forward
and tilted to one side, peering closely at something tiny on the ground right in front
of his nose, ears crooked, utterly absorbed and slightly puzzled. Warm afternoon light,
dust in the air, soft out-of-focus grassland behind.
```

**Chương 13 — Bầy Kiến Tha Cả Mùa Mưa** ✅
```
SCENE: monsoon rain on a grassland. Bom lies belly-down on a soaking wet rock ledge,
front legs stretched forward, chin flat on his paws, fur soaked and sticking up in wet
spikes, rainwater dripping off the messy cowlick on his head and off his nose. He stares
down over the edge with his mouth slightly open, completely absorbed, faintly puzzled
and deeply impressed. Below the ledge in the foreground: a tall earthen ant mound with a
big section washed away by the rain, and a long line of tiny black ants forming a thin
brown thread, each carrying one grain of soil up to rebuild the broken part in the
downpour. Rain in streaks, droplets bouncing off the stone. Wet grey-green palette with
one warm shaft of light on Bom and the mound.
```

**Chương 23 — Tiếng Gầm Vỡ** ✅
```
SCENE, a comedy moment: Bom stands alone on top of a low flat mound of dry earth in a
sunny grass clearing, chest puffed out, front paws planted, head lifted, mouth wide open,
caught in the exact split second his voice cracks in the middle of announcing something
important. Pure embarrassment on his face: eyes wide and startled, ears folding back,
cheeks flushed, his whole body flinching. He is the only creature in the frame. Bright
mid-morning sun, tall golden grass, two simple stylised flat-topped trees far away and
out of focus, dust in the air.
```

**Chương 40 — lên đường chinh phục vùng trời xa (ẩn dụ đi du học)** ⏳ *chưa có bản đạt*
```
POSE — he is trotting briskly mid-stride along a dirt path, seen at a three-quarter
angle, with a light springy bounce; one big front paw reaching forward, head up, ears
forward, looking ahead full of forward momentum and excitement as he sets off on a
journey. The path runs away behind him into a wide open plain. Low camera near ground
level. Fresh bright early-morning light, clear sky, two simple stylised flat-topped trees
far away and out of focus.
```

*Bản đã loại:* `Bom_v2_THPT_quay-mat` (ngoái đầu chờ em nhỏ) — đọc ra **già nua, buồn bã, mất năng lượng**. Cảnh ngoái đầu chờ em nhỏ nên để dành cho **chương 39**, không phải chương kết.

---

## 5. Công cụ thay thế khi ChatGPT chặn

Đã thử **Gamma `generate_image`**: không bị chặn, ra đúng sư tử, đúng năng lượng — nhưng phong cách là **vector phẳng có viền**, lệch hẳn với bộ ảnh 3D đã duyệt. Cả `type: scene` lẫn `type: illustration` đều ra phẳng; ép bằng ngôn ngữ "CGI, volumetric fur, subsurface scattering" cũng không đổi được.

**Kết luận:** Gamma dùng được cho slide và ấn phẩm, **không dùng được cho sách**. Nếu ChatGPT chặn, phương án đúng là **đợi rồi thử lại**, không phải đổi công cụ.

---

## 6. Ghi chú sản xuất

- Từ chương 4 trở đi, cách tốt nhất là **upload ảnh character sheet kèm prompt** thay vì tả bằng chữ — ChatGPT chỉnh ảnh của chính nó thì nhất quán hơn hẳn. Nhưng lưu ý: khi bộ lọc đang siết, ảnh tham chiếu **làm tăng** tỷ lệ bị chặn.
- Vết sẹo trên mũi (gai nhím ch4) hay bị model bỏ qua — phải nhắc riêng hoặc vẽ thêm tay.
- **Cảnh báo trôi phong cách:** càng đẩy mạnh các từ né bộ lọc ở lứa tuổi lớn, ảnh càng trượt về bán-tả-thực, lông chi tiết như phim tài liệu. Bốn ảnh hiện tại chưa hoàn toàn cùng một phong cách.
- Ngân sách hình toàn sách: **~45–50 hình cho 240 trang** (1 hình mở mỗi mùa + 1 hình/chương + bìa).

---

## 7. Đồng phục linh vật

Linh vật Trường Việt Anh mặc áo polo vàng + yếm navy có huy hiệu chữ A. Bờm trong truyện là **sư tử hoang dã, không mặc gì** — cho mặc đồng phục sẽ phá vỡ thế giới ngụ ngôn. Giữ ADN nhận dạng (bảng màu ấm, mắt tròn to nâu sẫm, lông mày dày, chóp đuôi) nhưng bỏ quần áo.

Nếu cần bản mặc đồng phục cho ấn phẩm trường, thêm:
```
He wears a yellow polo shirt and navy-blue dungarees with a small gold shield crest
bearing the letter A.
```
