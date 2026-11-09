#!/usr/bin/env sh
# Video → moving picture for the website cover (lint rule 15).
#
#     sh tools/motion.sh <video file> <week> <target language> [slot-or-frames]
#     sh tools/motion.sh ~/Downloads/poppies.mp4 2026-w47 en
#     sh tools/motion.sh loop.mp4 2026-w43 de 1     # secondary story more[1]
#
# Writes covers/<week>/motion/<lang>.webp (or <lang>-<slot>.webp for a
# secondary slot): an animated WebP, 1200×800 — 800×800 for the square
# secondary slots 1/2 — (centre crop), 12 frames/s, loops forever. A WebP has no audio track, so the picture is always silent. The site shows it with no controls.
# Needs ffmpeg and img2webp (Homebrew: `brew install ffmpeg webp`).
# Cut the video to 2–15 s first. Make the last frame meet the first frame, or the loop jumps.
#
# Staggered durations (SOP rule 15): the 12 motions on one cover page must NOT all loop at the same
# length, or the reader sees them all jump back in sync. Each language gets its own PRIME frame count
# at 12 fps (pairwise coprime, so the loops never re-sync); the same language keeps the same count
# every week. The source loop is retimed with one uniform speed change. Durations 7.3–14.8 s,
# speeds 0.67–1.36x against the 10 s source loops. Give FRAMES explicitly to override (e.g. for a
# non-cover video); a language with no table entry and no FRAMES keeps the old behaviour (the video's
# own length at 12 fps).
#   en 89 · de 97 · fr 103 · es 109 · it 113 · pt 127 · nl 131 · ru 137 · ja 149 · ko 157 · zh-cn 167 · zh-tw 179
#
# Secondary stories (slot 1/2/3/5 as the 4th argument): the frame count
# comes from tools/motion-durations.json (secondaries[lang][slot]), the
# output is covers/<week>/motion/<lang>-<slot>.webp, and the canvas matches
# the slot's still: 800x800 for the square slots 1/2, 1200x800 for 3/5.
#
# Endpoint sampling (2026-11-08 fix): the P frames must span the CLOSED period [0, source
# duration], so the last frame IS the first frame and the loop-point step is 0. The retime
# therefore targets (P-1)/12 s, not P/12 s: sampling P frames out of a P/12 s period puts the
# last kept frame at source t = 10 - 10/P, and the wrap step measured 6.7 / 6.2 / 15.7 /255
# (fr W46 / zh-tw W43 / en W45) — not acceptable. After extraction the Pth frame is an exact
# copy of the first PNG, and after img2webp the last frame is replaced by a cwebp keyframe of
# the first frame (tools/splice_last_keyframe.py): img2webp encodes the last frame as an
# inter frame predicted from the previous one, and even with identical PNG inputs the decoded
# jump measured 1.32/255 (fr W46, q70); the keyframe decodes bit-identically to the first
# frame (measured 0.0000). The splice step verifies the decoded first-vs-last diff < 1.0/255
# and fails loud otherwise. (No SOP text for this mechanism — user 2026-11-08: stop writing
# SOP prose; the rule lives here and in the commit message.)
set -eu

src=${1:?video file}
week=${2:?week, e.g. 2026-w47}
lang=${3:?target language, e.g. en}
arg4=${4:-}
# 4th argument: a secondary slot (1/2/3/5) takes its frame count from
# tools/motion-durations.json; any other number is a frame-count override
# (lead behaviour); empty = lead default for the language.
slot=""
canvas_w=1200
canvas_h=800
nframes=""
case "$arg4" in
  1|2|3|5)
    slot=$arg4
    nframes=$(python3 -c "import json; print(json.load(open('tools/motion-durations.json'))['secondaries']['$lang']['$slot'])" 2>/dev/null) || { echo "no secondary frame count for $lang slot $slot"; exit 1; }
    case "$slot" in 1|2) canvas_w=800; canvas_h=800;; esac
    ;;
  '') ;;
  *[!0-9]*) echo "frames must be a positive integer"; exit 1;;
  *) nframes=$arg4;;
esac
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
if [ -n "$slot" ]; then
  out="covers/$week/motion/$lang-$slot.webp"
  [ -f "covers/$week/images/$lang-$slot.webp" ] || { echo "missing still covers/$week/images/$lang-$slot.webp (rule 15)"; exit 1; }
else
  out="covers/$week/motion/$lang.webp"
  [ -f "covers/$week/images/$lang.webp" ] || { echo "missing still covers/$week/images/$lang.webp (rule 15)"; exit 1; }
fi

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
  # Endpoint sampling: the retimed period is (P-1)/12 s, so frame P-1 lands
  # exactly on the source loop's endpoint (source t = duration == frame 0).
  # A P/12 s period would put the last frame 10/P of source motion short of
  # the endpoint, and the wrap step measured up to 15.7/255 — not acceptable.
  dur=$(awk -v n="$nframes" 'BEGIN{printf "%.6f", (n-1)/12}')
  srcdur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$src")
  factor=$(awk -v n="$nframes" -v d="$srcdur" 'BEGIN{printf "%.6f", ((n-1)/12)/d}')
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
# Extract the frames at 12 fps. Cap the extraction at exactly P-1 frames: the retimed
# period is (P-1)/12 s, so the fps filter yields P-1 frames, and the Pth frame is then
# an exact copy of the first PNG — the P frames span the closed period [0, source
# duration], so the loop closes on itself. (The old code capped at P and dropped the
# extra frame at the wrap point; that extra frame WAS the endpoint, and dropping it
# left the last kept frame 10/P of source motion short of closure — the 6–16/255 bug.)
cap_args=""
if [ -n "$nframes" ]; then cap_args="-frames:v $((nframes - 1))"; fi
ffmpeg -hide_banner -loglevel error -y -i "$src" -an \
  -vf "fps=12,scale=$canvas_w:$canvas_h:force_original_aspect_ratio=increase,crop=$canvas_w:$canvas_h" $cap_args "$framesdir/%04d.png"
n=$(ls "$framesdir" | wc -l)
if [ -n "$nframes" ]; then
  if [ "$n" -ne $((nframes - 1)) ]; then
    echo "expected $((nframes - 1)) frames at 12 fps, got $n; the retime did not land — not writing $out"; exit 1
  fi
  cp "$framesdir/0001.png" "$framesdir/$(printf '%04d' "$nframes").png"
  n=$nframes
fi
mkdir -p "covers/$week/motion"
# 83 ms per frame = 12 frames/s. Lower -q until the file is ≤ 4 MB (rule 15).
# Measured 2026-11-08 on the noisiest loop (W45 de, 97 frames): -m 6 -q 20
# saves only ~2% over -m 4 -q 20 (5.32 vs 5.45 MB) at 5x the time, so the
# ladder stays at -m 4 and goes down to q10/q5 instead; q10 fixed that loop
# (3.93 MB). If even q5 is over the cap the file is deleted, not written:
# a missing motion is legal (rule 15 is optional), an over-cap one is not.
# When a frame count is set, the quality ladder also closes the loop: after
# img2webp, tools/splice_last_keyframe.py replaces the last frame with a
# keyframe of the first frame (the decoded jump would otherwise be ~1.3/255
# even with identical PNG inputs — inter-frame prediction residual). The
# splice verifies the decoded first-vs-last diff < 1.0/255 and fails loud
# if it cannot close the loop. It can change the size slightly, so the cap
# is re-checked after the splice; if the spliced file is over the cap, drop
# a quality rung and redo.
wrote=""
for q in 70 60 50 40 30 20 10 5; do
  img2webp -loop 0 -lossy -q "$q" -m 4 -d 83 "$framesdir"/*.png -o "$out" >/dev/null 2>&1
  [ -f "$out" ] && [ "$(wc -c < "$out")" -le 4194304 ] || continue
  if [ -n "$nframes" ]; then
    py=tools/venv/bin/python
    [ -x "$py" ] || py=python3
    if ! "$py" tools/splice_last_keyframe.py "$out" "$framesdir/0001.png" "$q"; then
      rm -f "$out"
      echo "splice failed for $out — not writing it (rule 15)"; exit 1
    fi
    [ "$(wc -c < "$out")" -le 4194304 ] || { rm -f "$out"; continue; }
  fi
  wrote=1
  break
done
if [ -z "$wrote" ]; then
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
