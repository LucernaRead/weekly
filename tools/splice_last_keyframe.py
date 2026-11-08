#!/usr/bin/env python3
"""Close the loop of an animated WebP exactly: replace its last frame with a
cwebp keyframe of the first frame.

Why: img2webp encodes every frame after the first as an inter frame predicted
from the previous one. Even when the last frame's PNG input is byte-identical
to the first frame's, the decoded last frame differs by the quantized
prediction residual — measured 1.32/255 on fr W46 at q70. A cwebp keyframe of
the same PNG decodes bit-identically to the first frame (measured 0.0000), so
splicing it in as the last frame closes the loop at exactly 0.

Usage: splice_last_keyframe.py <in.webp> <first.png> <quality>
  in.webp   animated WebP built by img2webp (its last frame is replaced)
  first.png the first frame's PNG (1200x800, as fed to img2webp)
  quality   the -q img2webp used, so the keyframe matches the first frame's
            quantizer (cwebp -q <quality> -m 4)
Rewrites in.webp in place (via a .tmp file, only on success). Verifies the
result before replacing: same frame count, loop count 0, and the decoded
first-vs-last mean abs diff on 240x160 thumbnails < 1.0/255. Exits non-zero
and leaves the original untouched on any failure.
"""
import os
import re
import subprocess
import sys
import tempfile

ROW = re.compile(
    r"^\s*(\d+):\s+(\d+)\s+(\d+)\s+(\S+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\S+)\s*$"
)
BG = re.compile(r"Background color\s*:\s*(0x[0-9A-Fa-f]+)")
LOOP = re.compile(r"Loop Count\s*:\s*(\d+)")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed: {r.stderr.strip()}")
    return r.stdout


def thumb_diff(im1, im2):
    from PIL import ImageChops, ImageStat
    t1 = im1.convert("RGB").resize((240, 160))
    t2 = im2.convert("RGB").resize((240, 160))
    d = ImageChops.difference(t1, t2)
    return sum(ImageStat.Stat(d).mean) / 3.0


def main():
    in_webp, first_png, quality = sys.argv[1:4]
    info = run(["webpmux", "-info", in_webp])
    rows = []
    for line in info.splitlines():
        m = ROW.match(line)
        if m:
            n, w, h, alpha, x, y, dur, disp, blend, size, comp = m.groups()
            rows.append({
                "n": int(n), "x": int(x), "y": int(y), "dur": int(dur),
                "disp": 0 if disp == "none" else 1,
                "blend": "+b" if blend == "yes" else "-b",
            })
    if not rows:
        print(f"{in_webp}: no frames parsed from webpmux -info", file=sys.stderr)
        return 1
    bg = BG.search(info)
    bgcolor = bg.group(1) if bg else "0xFFFFFFFF"
    tmp = tempfile.mkdtemp(prefix="splice-", dir="tools/scratch")
    try:
        files = []
        for r in rows:
            f = os.path.join(tmp, f"f_{r['n']:04d}.webp")
            run(["webpmux", "-get", "frame", str(r["n"]), in_webp, "-o", f])
            files.append(f)
        last = rows[-1]
        run(["cwebp", "-q", quality, "-m", "4", first_png, "-o", files[-1]])
        out_tmp = in_webp + ".tmp"
        cmd = ["webpmux"]
        for r, f in zip(rows, files):
            if r is last:
                spec = f"+{r['dur']}+0+0+{r['disp']}{r['blend']}"
            else:
                spec = f"+{r['dur']}+{r['x']}+{r['y']}+{r['disp']}{r['blend']}"
            cmd += ["-frame", f, spec]
        cmd += ["-loop", "0", "-o", out_tmp]
        run(cmd)
        # Verify the spliced file before replacing the original.
        info2 = run(["webpmux", "-info", out_tmp])
        bg2 = BG.search(info2)
        if not bg2 or bg2.group(1).upper() != bgcolor.upper():
            print(f"{in_webp}: splice changed background color "
                  f"{bgcolor} -> {bg2.group(1) if bg2 else 'unknown'}",
                  file=sys.stderr)
            return 1
        from PIL import Image
        im = Image.open(out_tmp)
        frames = getattr(im, "n_frames", 1)
        if frames != len(rows):
            print(f"{in_webp}: splice holds {frames} frames, want {len(rows)}",
                  file=sys.stderr)
            return 1
        if im.info.get("loop", None) != 0:
            print(f"{in_webp}: splice loop count {im.info.get('loop')}, want 0",
                  file=sys.stderr)
            return 1
        decoded = []
        for i in range(frames):
            im.seek(i)
            decoded.append(im.copy())
        jump = thumb_diff(decoded[-1], decoded[0])
        if jump >= 1.0:
            print(f"{in_webp}: spliced loop jump {jump:.4f} >= 1.0, not replacing",
                  file=sys.stderr)
            return 1
        os.replace(out_tmp, in_webp)
        print(f"spliced {in_webp}: last frame is now a keyframe of frame 1, "
              f"jump={jump:.4f}, {frames} frames, "
              f"{os.path.getsize(in_webp)} bytes")
        return 0
    finally:
        for name in os.listdir(tmp):
            os.unlink(os.path.join(tmp, name))
        os.rmdir(tmp)


if __name__ == "__main__":
    sys.exit(main())
