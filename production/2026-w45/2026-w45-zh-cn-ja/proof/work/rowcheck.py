# -*- coding: utf-8 -*-
"""Independent same-baseline ink-collision scan (own implementation):
PIL/FreeType true-ink spans at 4x supersampling, SC face (the edition's
face), grouped by baseline y; flags gaps < 6 units incl. overlaps."""
import re, glob, os, html
from PIL import ImageFont
BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-ja/svg"
F = {
    ("serif", False): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", 2),
    ("serif", True): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 2),
    ("sans", False): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 2),
    ("sans", True): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 2),
}
def measure(t, kind, bold, size):
    path, idx = F[(kind, bold)]
    f = ImageFont.truetype(path, int(round(size * 4)), index=idx)
    bb = f.getbbox(t)
    return bb[0] / 4.0, bb[2] / 4.0, f.getlength(t) / 4.0
bad = 0
for path in sorted(glob.glob(os.path.join(BASE, "*.svg"))):
    src = open(path, encoding="utf-8").read()
    rows = {}
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>', src):
        x, y, fam, size, bold, anchor, t = (float(m.group(1)), float(m.group(2)), m.group(3),
                                            float(m.group(4)), bool(m.group(5)), m.group(6) or "start", html.unescape(m.group(7)))
        if not t.strip(): continue
        kind = "serif" if "Serif" in fam else "sans"
        l, r, adv = measure(t, kind, bold, size)
        if anchor == "start": a, b = x + l, x + r
        elif anchor == "end": a, b = x - adv + l, x - adv + r
        else: a, b = x - adv / 2 + l, x - adv / 2 + r
        rows.setdefault(round(y, 1), []).append((a, b, t))
    for y, spans in rows.items():
        spans.sort()
        for (a1, b1, t1), (a2, b2, t2) in zip(spans, spans[1:]):
            if a2 - b1 < 6:
                print(f"{os.path.basename(path)} y={y} gap={a2-b1:.1f}: {t1[:40]!r} <> {t2[:40]!r}"); bad += 1
print("collisions:", bad)
