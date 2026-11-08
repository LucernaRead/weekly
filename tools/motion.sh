#!/usr/bin/env sh
# Video → moving picture for the website cover (lint rule 15).
#
#     sh tools/motion.sh <video file> <week> <target language> [frames]
#     sh tools/motion.sh ~/Downloads/poppies.mp4 2026-w47 en
#
# Writes covers/<week>/motion/<lang>.webp: an animated WebP, 1200×800 (3:2, centre crop), 12 frames/s,
# loops forever. A WebP has no audio track, so the picture is always silent. The site shows it with no controls.
# Needs ffmpeg and img2webp (Homebrew: `brew install ffmpeg webp`).
# Cut the video to 2–15 s first. Make the last frame meet the first frame, or the loop jumps.
#
# Staggered durations (SOP rule 15): the 12 motions on one cover page must NOT all loop at the same
# length, or the reader sees them all jump back in sync. Each language gets its own PRIME frame count
# at 12 fps (pairwise coprime, so the loops never re-sync); the same language keeps the same count
# every week. The source loop is retimed with one uniform speed change, which preserves seamlessness
# (frame(t) = frame(t mod source duration) for a seamless source loop). Durations 7.4–14.9 s,
# speeds 0.67–1.35x against the 10 s source loops. Give FRAMES explicitly to override (e.g. for a
# non-cover video); a language with no table entry and no FRAMES keeps the old behaviour (the video's
# own length at 12 fps).
#   en 89 · de 97 · fr 103 · es 109 · it 113 · pt 127 · nl 131 · ru 137 · ja 149 · ko 157 · zh-cn 167 · zh-tw 179
set -eu

src=${1:?video file}
week=${2:?week, e.g. 2026-w47}
lang=${3:?target language, e.g. en}
nframes=${4:-}
case "$lang" in
  en)    nframes=${nframes:-89} ;;
  de)    nframes=${nframes:-97} ;;
  fr)    nframes=${nframes:-103} ;;
  es)    nframes=${nframes:-109} ;;
  it)    nframes=${nframes:-113} ;;
  pt)    nframes=${nframes:-127} ;;
  nl)    nframes=${nframes:-131} ;;
  ru)    nframes=${nframes:-137} ;;
  ja)    nframes=${nframes:-149} ;;
  ko)    nframes=${nframes:-157} ;;
  zh-cn) nframes=${nframes:-167} ;;
  zh-tw) nframes=${nframes:-179} ;;
esac
out="covers/$week/motion/$lang.webp"
[ -f "covers/$week/images/$lang.webp" ] || { echo "missing still covers/$week/images/$lang.webp (rule 15)"; exit 1; }

framesdir=""
warped=""
# Frame PNGs are ~1 MB each at 1200x800; a 179-frame motion needs ~200 MB of
# scratch. /tmp on this VM is a 512 MB tmpfs shared by parallel jobs, so use
# the repo's gitignored scratch dir (disk-backed) instead of mktemp's /tmp.
mkdir -p tools/scratch
framesdir=$(mktemp -d tools/scratch/motion-frames.XXXXXX)
trap 'rm -rf "$framesdir"; [ -n "$warped" ] && rm -f "$warped"' EXIT
if [ -n "$nframes" ]; then
  case "$nframes" in ''|*[!0-9]*) echo "frames must be a positive integer"; exit 1;; esac
  dur=$(awk -v n="$nframes" 'BEGIN{printf "%.6f", n/12}')
  srcdur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$src")
  factor=$(awk -v n="$nframes" -v d="$srcdur" 'BEGIN{printf "%.6f", (n/12)/d}')
  warped=$(mktemp --suffix=.mp4 tools/scratch/motion-warped.XXXXXX)
  # Uniform retime: output lasts exactly nframes/12 s. factor = target duration / source duration.
  # NOTE: do NOT force -pix_fmt here. The source loops are yuv444p, and forcing yuv420p
  # downsamples chroma enough to erase the tiny differences between near-static frames:
  # measured 2026-11-08 on W43 pt, the forced conversion made the opening pair differ by
  # at most 11/255 (vs 13 without it), and at -q 30 libwebp then merged the pair into one
  # 166 ms frame (126 frames instead of 127). The warped file is an intermediate consumed
  # only by ffmpeg's own PNG extraction below, so keeping the native format costs nothing.
  ffmpeg -hide_banner -loglevel error -y -i "$src" -an \
    -vf "setpts=PTS*$factor" -t "$dur" -c:v libx264 -crf 16 -preset fast "$warped"
  src="$warped"
fi
# Cap the extraction at exactly nframes: the warped stream's last frame
# duration can push the fps filter one slot past N (measured 2026-11-08:
# W43 en warped to 89 frames came out as 90). The extra frame sits at
# t = N/12, i.e. the wrap point, and is a duplicate of frame 0 in a
# seamless loop, so dropping it preserves closure. The guard below still
# catches a warp that lands SHORT of N.
cap_args=""
if [ -n "$nframes" ]; then cap_args="-frames:v $nframes"; fi
ffmpeg -hide_banner -loglevel error -y -i "$src" -an \
  -vf "fps=12,scale=1200:800:force_original_aspect_ratio=increase,crop=1200:800" $cap_args "$framesdir/%04d.png"
n=$(ls "$framesdir" | wc -l)
if [ -n "$nframes" ] && [ "$n" -ne "$nframes" ]; then
  echo "expected $nframes frames at 12 fps, got $n; the retime did not land — not writing $out"; exit 1
fi
mkdir -p "covers/$week/motion"
# 83 ms per frame = 12 frames/s. Lower -q until the file is ≤ 4 MB (rule 15).
# Measured 2026-11-08 on the noisiest loop (W45 de, 97 frames): -m 6 -q 20
# saves only ~2% over -m 4 -q 20 (5.32 vs 5.45 MB) at 5x the time, so the
# ladder stays at -m 4 and goes down to q10/q5 instead; q10 fixed that loop
# (3.93 MB). If even q5 is over the cap the file is deleted, not written:
# a missing motion is legal (rule 15 is optional), an over-cap one is not.
for q in 70 60 50 40 30 20 10 5; do
  img2webp -loop 0 -lossy -q "$q" -m 4 -d 83 "$framesdir"/*.png -o "$out" >/dev/null 2>&1
  [ "$(wc -c < "$out")" -le 4194304 ] && break
done
if [ "$(wc -c < "$out")" -gt 4194304 ]; then
  rm -f "$out"
  echo "still over 4 MB at quality 5 — not writing $out (rule 15)"; exit 1
fi
# Frame-count guard: at low quality libwebp merges near-identical frames into one
# longer frame (measured 2026-11-08: W43 pt lost 1 of 127 frames at -q 30). Size
# alone cannot catch that — a merged file is SMALLER. Verify the WebP really holds
# $nframes frames (webpmux ships with img2webp; fall back to PIL). Fail loud.
if [ -n "$nframes" ]; then
  got=""
  if command -v webpmux >/dev/null 2>&1; then
    got=$(webpmux -info "$out" 2>/dev/null | sed -n 's/.*Number of frames: \([0-9]*\).*/\1/p')
  fi
  if [ -z "$got" ] && [ -x tools/venv/bin/python ]; then
    got=$(tools/venv/bin/python -c "from PIL import Image; print(Image.open('$out').n_frames)" 2>/dev/null)
  fi
  if [ "$got" != "$nframes" ]; then
    rm -f "$out"
    echo "wrote $nframes frames but $out holds ${got:-unknown} — not writing $out (rule 15)"; exit 1
  fi
fi
echo "wrote $out ($(wc -c < "$out" | tr -d ' ') bytes, quality $q, $n frames). Now run: node lint.mjs --write && node lint.mjs"
