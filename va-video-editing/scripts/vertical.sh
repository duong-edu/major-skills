#!/usr/bin/env bash
set -euo pipefail

# vertical.sh — Convert a landscape (16:9) video into vertical 9:16 for Reels/Shorts/TikTok
#
# Usage: ./vertical.sh <input_video> [options]
#
# Options:
#   --mode <mode>      crop | blur | pad   (default: blur)
#   --output <path>    Output path (default: <input>_vertical.<ext>)
#   --size <WxH>       Output size (default: 1080x1920)
#   --focus <pos>      For crop mode: left, center, right (default: center)
#
# Modes:
#   crop  — Zoom and crop to 9:16. Best for talking-head footage where the
#           subject is centred. Loses the sides of the frame.
#   blur  — Original video centred over a blurred, zoomed copy of itself.
#           Safest default: nothing is cut off, fills the whole vertical frame.
#   pad   — Original video centred over solid black bars. Cleanest look,
#           but leaves large empty areas.
#
# Examples:
#   ./vertical.sh talk.mp4 --mode crop --focus center
#   ./vertical.sh screencast.mp4 --mode blur
#   ./vertical.sh interview.mp4 --mode crop --focus left --output reel.mp4

print_usage() {
    sed -n '3,24p' "$0" | sed 's/^# \?//'
}

if [[ $# -lt 1 ]]; then
    print_usage
    exit 1
fi

INPUT_VIDEO="$1"
shift

MODE="blur"
OUTPUT=""
SIZE="1080x1920"
FOCUS="center"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --mode)   MODE="$2";   shift 2 ;;
        --output) OUTPUT="$2"; shift 2 ;;
        --size)   SIZE="$2";   shift 2 ;;
        --focus)  FOCUS="$2";  shift 2 ;;
        *)
            echo "Error: Unknown option '$1'"
            print_usage
            exit 1
            ;;
    esac
done

if [[ ! -f "$INPUT_VIDEO" ]]; then
    echo "Error: Input video not found: $INPUT_VIDEO"
    exit 1
fi

command -v ffmpeg >/dev/null 2>&1 || { echo "Error: ffmpeg is not installed."; exit 1; }

W="${SIZE%x*}"
H="${SIZE#*x}"

INPUT_DIR="$(dirname "$INPUT_VIDEO")"
INPUT_BASENAME="$(basename "$INPUT_VIDEO" | sed 's/\.[^.]*$//')"
INPUT_EXT="$(basename "$INPUT_VIDEO" | sed 's/.*\.//')"

if [[ -z "$OUTPUT" ]]; then
    OUTPUT="${INPUT_DIR}/${INPUT_BASENAME}_vertical.${INPUT_EXT}"
fi

case "$FOCUS" in
    left)   CROP_X="0" ;;
    right)  CROP_X="in_w-out_w" ;;
    center) CROP_X="(in_w-out_w)/2" ;;
    *)
        echo "Error: Unknown focus '$FOCUS'. Use: left, center, right" >&2
        exit 1
        ;;
esac

case "$MODE" in
    crop)
        # Scale so height fills the frame, then crop the width to 9:16
        FILTER="scale=-2:${H},crop=${W}:${H}:${CROP_X}:0,setsar=1"
        ;;
    blur)
        # Blurred zoomed background + original video centred on top
        FILTER="[0:v]scale=${W}:${H}:force_original_aspect_ratio=increase,crop=${W}:${H},boxblur=luma_radius=40:luma_power=2,eq=brightness=-0.08[bg];[0:v]scale=${W}:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1"
        ;;
    pad)
        FILTER="scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2:black,setsar=1"
        ;;
    *)
        echo "Error: Unknown mode '$MODE'. Use: crop, blur, pad" >&2
        exit 1
        ;;
esac

echo "Converting to vertical ${W}x${H}"
if [[ "$MODE" == "crop" ]]; then echo "Mode: crop (focus: $FOCUS)"; else echo "Mode: $MODE"; fi
echo "Input: $INPUT_VIDEO"

if [[ "$MODE" == "blur" ]]; then
    ffmpeg -y -i "$INPUT_VIDEO" \
        -filter_complex "$FILTER" \
        -c:v libx264 -crf 20 -preset medium \
        -c:a aac -b:a 192k \
        "$OUTPUT" 2>&1 | tail -5
else
    ffmpeg -y -i "$INPUT_VIDEO" \
        -vf "$FILTER" \
        -c:v libx264 -crf 20 -preset medium \
        -c:a aac -b:a 192k \
        "$OUTPUT" 2>&1 | tail -5
fi

echo "Output: $OUTPUT"
