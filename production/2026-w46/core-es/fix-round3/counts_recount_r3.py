# -*- coding: utf-8 -*-
"""Independent recount (fix round): standalone stems + grouped match sets,
per page, from final SVGs; level split via chip pairing is re-derived from
the build registry output recorded in the build log (cross-checked here
against chip-adjacent stem counts is NOT attempted — registry is the
source of truth, as in Round 1 §4). This script verifies stem sequences
and grouped sets only."""
import os, re, glob, html
import xml.etree.ElementTree as ET
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
NS = "{http://www.w3.org/2000/svg}"
PAGES = ["p1-portada", "p2-vida", "p3-cultura", "p4-deporte", "p5-juventud", "p6-afondo", "p7-lengua", "p8-ejercicios"]
EXPECT = {1: list(range(1, 11)), 2: list(range(11, 29)), 3: list(range(29, 47)),
          4: list(range(47, 65)), 5: list(range(65, 83)),
          6: list(range(83, 101)), 7: list(range(101, 113)),
          8: list(range(113, 151))}
for code in ["de"]:
    print(f"===== es-{code} stem recount =====")
    total = 0
    for i, pg in enumerate(PAGES, 1):
        els = []
        for t in ET.parse(f"{BASE}/files/weekly-report-w46-es-{code}/svg/{pg}.svg").getroot().iter(NS + "text"):
            els.append("".join(t.itertext()).strip())
        standalone = sorted(int(m.group(1)) for e in els for m in [re.fullmatch(r"(\d+)\.", e)] if m)
        grouped = []
        for e in els:
            m = re.fullmatch(r"(\d+)–(\d+)\.", e)
            if m:
                grouped.extend(range(int(m.group(1)), int(m.group(2)) + 1))
        seq = sorted(standalone + grouped)
        ok = seq == EXPECT[i]
        print(f"  P{i}: standalone={len(standalone)} grouped={len(grouped)} total={len(seq)} seq-ok={ok}" + ("" if ok else f"  SEQ={seq}"))
        total += len(seq)
    print(f"  TOTAL stems = {total} (expect 150)")
