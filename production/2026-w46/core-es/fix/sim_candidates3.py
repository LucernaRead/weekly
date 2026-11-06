# -*- coding: utf-8 -*-
"""Round 3 candidates for D-5."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib_sim import wrap, text_w

def show(label, text, kind, bold, size, max_w):
    lines = wrap(text, kind, bold, size, max_w)
    print(f"== {label} ==")
    for ln in lines:
        print(f"  [{text_w(ln, kind, bold, size):6.1f}px] {ln!r}")
    return lines

show("D5-L meaning-long", "ir a + 동사 원형으로 문장을 바꿔서 ‘~할 것’이라는 의미를 나타내세요.", "sans", False, 20.5, 434)
show("D5-M meaning", "ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이라는 뜻을 나타내세요.", "sans", False, 20.5, 434)
show("D5-O fronted-obj", "문장을 ir a + 동사 원형으로 바꿔서 ‘~할 것’을 나타내세요.", "sans", False, 20.5, 434)
show("D5-P use-verb", "ir a + 동사 원형을 써서 문장을 ‘~할 것’으로 나타내세요.", "sans", False, 20.5, 434)
show("D5-Q plain", "ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이 되게 나타내세요.", "sans", False, 20.5, 434)
