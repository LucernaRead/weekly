#!/usr/bin/env python3
"""Masthead pixel check v2: exclude horizontal rule rows (single dark run
> 800px). For each row in y 280..360, report ink x-extent after removing
runs longer than 800px (rules) — text glyphs never form an 800px run.
Also report, per row, the leftmost/rightmost ink pixel after filtering,
so the masthead text rows can be identified by their extent pattern."""
from PIL import Image
from pathlib import Path
import json

BASE = Path.home() / 'workspace/goals/lucernaread-social-media-operations/files'

def row_ink(px, y, max_run=800):
    xs = []
    x = 0
    while x < 1950:
        r, g, b = px[x, y]
        if r < 110 and g < 110 and b < 110:
            x0 = x
            while x < 1950:
                r, g, b = px[x, y]
                if not (r < 110 and g < 110 and b < 110):
                    break
                x += 1
            if x - x0 <= max_run:
                xs.extend(range(x0, x))
        else:
            x += 1
    return xs

for eddir in sorted(BASE.glob('weekly-report-w46-en-*')):
    ed = eddir.name.replace('weekly-report-w46-en-', '')
    im = Image.open(eddir / 'cards/p1-front.png').convert('RGB')
    px = im.load()
    rows = {}
    for y in range(280, 361):
        xs = row_ink(px, y)
        if xs:
            rows[y] = (min(xs), max(xs), len(xs))
    # masthead text rows: rows with substantial ink (glyphs) and extent
    # clearly inside the frame; print compact summary: min/max over rows
    # 296..348 excluding rows with <5 ink px (noise) and rule rows already removed
    sel = {y: v for y, v in rows.items() if 296 <= y <= 348 and v[2] >= 5}
    if sel:
        lo = min(v[0] for v in sel.values()); hi = max(v[1] for v in sel.values())
        print(f"{ed}: masthead ink x {lo}..{hi} width {hi-lo+1} clearance L={lo} R={1949-hi} rows={len(sel)} y-range={min(sel)}..{max(sel)}")
    else:
        print(f"{ed}: NO TEXT ROWS FOUND")
    # dump per-row extents for fr + one 46pt edition for the record
    if ed in ('fr', 'es'):
        print('  rows:', {y: (v[0], v[1]) for y, v in sorted(rows.items())})
