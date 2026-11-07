# -*- coding: utf-8 -*-
"""Positive control for audit_ru_it.py: plant one defect per flag class plus
two clean texts; the audit must flag exactly the planted ones."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, INK, LINE
from audit_ru_it import audit

p = Page(1950, 2700)
# 1 COVER: text then opaque rect over its right half
p.text(100, 200, "COVERME пожалуйста посмотри внимательно сюда", 28, "serif", False, INK)
p.rect(330, 170, 420, 44, fill="#a4553a")
# 2 FOOTER: content text with ink bottom in the footer band
p.text(100, 2600, "FOOTERME этот текст стоит слишком низко", 28, "serif", False, INK)
# 3 EDGE: text running past the right page edge
p.text(1700, 400, "EDGEME длинный текст выходит за край страницы далеко", 28, "serif", False, INK)
# 4 LINEX: text, then a thin line through its ink band
p.text(100, 600, "LINEXME строка через которую пройдёт линия", 28, "serif", False, INK)
p.hline(100, 900, 592, "#b3a06a", 2)
# 5 STRADDLE-V: box title wider than its stroked box
p.rect(100, 800, 400, 200, fill="none", stroke=LINE, sw=1.4)
p.text(122, 850, "STRADDLEME заголовок шире своей рамки намного", 24, "sans", True, INK)
# 6 STRADDLE-H: text ink crossing the bottom border of its box
p.rect(1100, 800, 500, 120, fill="none", stroke=LINE, sw=1.4)
p.text(1122, 930, "BOTTOMME нижняя строка коробки", 24, "sans", False, INK)
# 7 CLEAN: text fully inside a stroked box
p.rect(100, 1200, 500, 160, fill="none", stroke=LINE, sw=1.4)
p.text(122, 1260, "Чистый заголовок внутри рамки", 24, "sans", True, INK)
# 8 CLEAN: plain text, nothing near it
p.text(100, 1600, "Совершенно чистая строка текста.", 28, "serif", False, INK)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "control.svg")
p.save(out)
flags = audit(out)
for kind, label, why in flags:
    print(f"[{kind}] {label} -- {why}")
expect = {"COVERME": "COVER", "FOOTERME": "FOOTER", "EDGEME": "EDGE",
          "LINEXME": "LINEX", "STRADDLEME": "STRADDLE-V", "BOTTOMME": "STRADDLE-H"}
ok = True
for marker, kind in expect.items():
    hit = any(kind == k and marker in l for k, l, w in flags)
    print(("PASS" if hit else "FAIL"), marker, "->", kind)
    ok &= hit
for marker in ["Чистый заголовок", "Совершенно чистая"]:
    hit = any(marker in l for k, l, w in flags)
    print(("FAIL" if hit else "PASS"), "clean text unflagged:", marker)
    ok &= not hit
print("CONTROL:", "ALL PASS" if ok else "FAILED")
