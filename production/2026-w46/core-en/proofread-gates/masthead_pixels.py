#!/usr/bin/env python3
"""Masthead pixel check (proofreader-only, read-only).
Cards are 1950x2700, same coords as SVG. Masthead line: P1 text #4,
baseline y=330, center-anchored x=975. Wordmark baseline y=262 (168pt).
Measure dark-ink bbox in band y in [288, 352] (below wordmark descenders,
above badge at y=372 baseline) on the P1 card. Ink = pixel darker than
mid-grey on any channel (cards are ivory paper, dark olive/black ink).
Also scan the full top band y in [60, 400] for ink touching frame edges
x<5 or x>1944, and report the wordmark band separately.
"""
from PIL import Image
from pathlib import Path
import json

BASE = Path.home() / 'workspace/goals/lucernaread-social-media-operations/files'
OUT = {}
for eddir in sorted(BASE.glob('weekly-report-w46-en-*')):
    ed = eddir.name.replace('weekly-report-w46-en-', '')
    im = Image.open(eddir / 'cards/p1-front.png').convert('RGB')
    assert im.size == (1950, 2700), im.size
    px = im.load()
    def ink_bbox(y0, y1):
        xs, ys = [], []
        for y in range(y0, y1 + 1):
            for x in range(1950):
                r, g, b = px[x, y]
                if r < 110 and g < 110 and b < 110:
                    xs.append(x); ys.append(y)
        if not xs:
            return None
        return min(xs), max(xs), min(ys), max(ys)
    band = ink_bbox(288, 352)
    word = ink_bbox(120, 285)
    top = ink_bbox(60, 400)
    # also: masthead font size from SVG text #4
    res = {'card': str(im.size), 'masthead_band_288_352': band,
           'masthead_clearance_px': (band[0], 1949 - band[1]) if band else None,
           'masthead_width_px': (band[1] - band[0] + 1) if band else None,
           'wordmark_band_120_285': word,
           'top_band_60_400_edge_touch': (top[0] < 5 or top[1] > 1944) if top else None,
           'top_band_bbox': top}
    OUT[ed] = res
    print(ed, json.dumps(res))

Path('/tmp/masthead.json').write_text(json.dumps(OUT, indent=1), encoding='utf-8')
