# -*- coding: utf-8 -*-
"""Export 2026-w47-ja-fr.text.md from the edition's 8 final SVGs.

Method: <text> elements in document order, one line each, grouped under
"## Page N" sections, with a 2-line header — never from the PDF.
Recreated 2026-11-11 (first-round fix): the original export-textmd-fr.py
was missing from the repo (first-round proof O6); this reconstruction was
verified byte-identical (46,880 bytes, 1350 text lines) against the
pre-fix text.md before the fix was applied.
"""
import os, xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
SVG_NS = "{http://www.w3.org/2000/svg}"
PAGES = ["p1-hyoushi", "p2-kurashi", "p3-bunka", "p4-supotsu",
         "p5-wakamono", "p6-fukayomi", "p7-kotoba", "p8-tesuto"]

lines = ["# 2026-w47-ja-fr", "", "Week: 2026-W47 (16–22 Nov 2026)", ""]
total = 0
for i, name in enumerate(PAGES, 1):
    tree = ET.parse(os.path.join(BASE, "svg", name + ".svg"))
    texts = ["".join(n.itertext()) for n in tree.iter(SVG_NS + "text")]
    total += len(texts)
    lines.append("## Page %d" % i)
    lines.append("")
    lines.extend(texts)
    if i < 8:
        lines.append("")
out = "\n".join(lines) + "\n"
dest = os.path.join(BASE, "2026-w47-ja-fr.text.md")
open(dest, "w", encoding="utf-8").write(out)
print("wrote %s (%d text lines, %d bytes)" % (dest, total, len(out.encode("utf-8"))))
