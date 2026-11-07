# -*- coding: utf-8 -*-
"""W46 ESxKO orphan scan: S1 line-initial orphan punctuation/particle, S2 short residue lines.
An element is a wrapped continuation iff the previous element in reading order
shares (x, size) and sits within 1.8x size above it.
Method A: document order.  Method B: sorted by (x, y). Flag sets must agree.
Only elements containing Hangul syllables. S2 skips bold headings (size>=22
and weight 700) and single-element boxes are still flagged for adjudication.
Usage: es_ko_orphan.py <svgdir>"""
import os, re, sys, xml.etree.ElementTree as ET
from collections import Counter
HANGUL = re.compile(r"[\uac00-\ud7a3]")
NS = "{http://www.w3.org/2000/svg}"
ORPHAN_CHARS = set(".,,)]}\u3002\u3001?!:;%\u2030~-\u2013\u2014\u00b7\u2026")
PARTICLES = ["\uc740", "\ub294", "\uc774", "\uac00", "\uc744", "\ub97c", "\uc5d0", "\uc5d0\uc11c",
             "\ub85c", "\uc73c\ub85c", "\uc640", "\uacfc", "\ub3c4", "\ub9cc", "\uae4c\uc9c0",
             "\ubd80\ud130", "\uc5d0\uac8c", "\ud55c\ud14c", "\ubcf4\ub2e4", "\ucc98\ub7fc", "\uac19\uc774"]
SYL = re.compile(r"[\uac00-\ud7a3]")

def load(svgdir):
    pages = {}
    for fn in sorted(os.listdir(svgdir)):
        if not fn.endswith(".svg"):
            continue
        tree = ET.parse(os.path.join(svgdir, fn))
        els = []
        for t in tree.getroot().iter(NS + "text"):
            txt = "".join(t.itertext())
            if not HANGUL.search(txt):
                continue
            els.append({"x": float(t.get("x")), "y": float(t.get("y")),
                        "size": float(t.get("font-size", "20")),
                        "weight": t.get("font-weight", "") or "",
                        "text": txt})
        pages[fn] = els
    return pages

def flags(ordered):
    out = []
    prev = None
    for e in ordered:
        cont = (prev is not None and round(e["x"], 1) == round(prev["x"], 1)
                and e["size"] == prev["size"] and 0 < e["y"] - prev["y"] <= e["size"] * 1.8)
        if cont:
            t = e["text"].strip()
            if t and t[0] in ORPHAN_CHARS:
                out.append(("S1-PUNCT", e["y"], t))
            else:
                for p in PARTICLES:
                    if t.startswith(p) and (len(t) == len(p) or t[len(p)] in " .,;:!?)]}·。、"):
                        out.append(("S1-PART:" + p, e["y"], t))
                        break
            syls = SYL.findall(t)
            if 0 < len(syls) <= 2 and len(t) < 14 and not any(ch.isdigit() for ch in t):
                if not (e["size"] >= 22 and "700" in e["weight"]):
                    out.append(("S2", e["y"], t))
        prev = e
    return out

def main(svgdir):
    pages = load(svgdir)
    disagree = []
    for fn, els in pages.items():
        fa = flags(els)
        fb = flags(sorted(els, key=lambda e: (round(e["x"], 1), e["y"])))
        sa = Counter((k, round(y, 1), t) for k, y, t in fa)
        sb = Counter((k, round(y, 1), t) for k, y, t in fb)
        if sa != sb:
            disagree.append(fn)
            print(f"!! grouping disagreement {fn}: A-only={list((sa-sb).elements())} B-only={list((sb-sa).elements())}")
        for k, y, t in fa:
            print(f"{k} {fn} y={y:.1f} {t[:70]}")
    print("grouping disagreements:", disagree if disagree else "none")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
