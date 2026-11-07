# -*- coding: utf-8 -*-
"""Offline wrap simulator for W46 ESxKO fix candidates.
Uses a verbatim copy of the build svglib.py (wrap/text_w, SC faces) so
simulated breaks match the renderer. Run with tools/venv python.
Usage: sim_wrap.py  (candidates hardcoded below; prints lines + widths)
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib_sim import wrap, text_w

CASES = [
    # (label, text, kind, bold, size, max_w)
    ("D2-ORIG", "24 — horas dura la huelga general del miércoles 11 de noviembre (11월 11일 총파업은 24시간이에요)", "serif", False, 20.5, 398),
    ("D3-ORIG", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일 세스타오에서 연방컵 결승)", "serif", False, 21, 398),
    ("D4-ORIG", "괄호 안 단어의 비교급이나 -ísimo 형태로 빈칸을 채우세요.", "sans", False, 20.5, 434),
    ("D5-ORIG", "ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’을 나타내세요.", "sans", False, 20.5, 434),
]

def show(label, text, kind, bold, size, max_w):
    lines = wrap(text, kind, bold, size, max_w)
    print(f"== {label} ({kind} {size}pt w={max_w}) ==")
    for ln in lines:
        print(f"  [{text_w(ln, kind, bold, size):6.1f}px] {ln!r}")
    print(f"  nlines={len(lines)}")
    return lines

if __name__ == "__main__":
    for c in CASES:
        show(*c)
