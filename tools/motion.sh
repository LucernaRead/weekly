#!/usr/bin/env sh
# Video → moving picture for the website cover (lint rule 15).
#
#     sh tools/motion.sh <video file> <week> <target language>
#     sh tools/motion.sh ~/Downloads/poppies.mp4 2026-w47 en
#
# Writes covers/<week>/motion/<lang>.webp: an animated WebP, 1200×800 (3:2, centre crop), 12 frames/s,
# loops forever. A WebP has no audio track, so the picture is always silent. The site shows it with no controls.
# Needs ffmpeg and img2webp (Homebrew: `brew install ffmpeg webp`).
# Cut the video to 2–15 s first. Make the last frame meet the first frame, or the loop jumps.
set -eu

src=${1:?video file}
week=${2:?week, e.g. 2026-w47}
lang=${3:?target language, e.g. en}
out="covers/$week/motion/$lang.webp"
[ -f "covers/$week/images/$lang.webp" ] || { echo "missing still covers/$week/images/$lang.webp (rule 15)"; exit 1; }

frames=$(mktemp -d)
trap 'rm -rf "$frames"' EXIT
ffmpeg -hide_banner -loglevel error -i "$src" -an \
  -vf "fps=12,scale=1200:800:force_original_aspect_ratio=increase,crop=1200:800" "$frames/%04d.png"
mkdir -p "covers/$week/motion"
# 83 ms per frame = 12 frames/s. Lower -q until the file is ≤ 4 MB (rule 15).
for q in 70 60 50 40 30; do
  img2webp -loop 0 -lossy -q "$q" -m 4 -d 83 "$frames"/*.png -o "$out" >/dev/null 2>&1
  [ "$(wc -c < "$out")" -le 4194304 ] && break
done
echo "wrote $out ($(wc -c < "$out" | tr -d ' ') bytes, quality $q). Now run: node lint.mjs --write && node lint.mjs"
