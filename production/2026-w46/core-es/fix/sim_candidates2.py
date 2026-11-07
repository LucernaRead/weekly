# -*- coding: utf-8 -*-
"""Round 2 candidates for D-3 / D-5 (robustness: break at a space with slack)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib_sim import wrap, text_w

def show(label, text, kind, bold, size, max_w):
    lines = wrap(text, kind, bold, size, max_w)
    print(f"== {label} ==")
    for ln in lines:
        print(f"  [{text_w(ln, kind, bold, size):6.1f}px] {ln!r}")
    return lines

# D-3 (serif 21, w=398) — shift 세스타오 off the boundary
show("D3-E -에 particle", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일에 세스타오에서 연방컵 결승)", "serif", False, 21, 398)
show("D3-F evening", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일 저녁 세스타오에서 연방컵 결승)", "serif", False, 21, 398)
show("D3-G held-form", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일에 세스타오에서 열리는 연방컵 결승)", "serif", False, 21, 398)
show("D3-H final-late", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일 연방컵 결승이 세스타오에서 열려요)", "serif", False, 21, 398)
show("D3-I match-word", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일 세스타오에서 열리는 연방컵 결승전)", "serif", False, 21, 398)
show("D3-J place-after-verb", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일 연방컵 결승, 세스타오에서 열려요)", "serif", False, 21, 398)

# D-5 (sans 20.5, w=434) — full semantics, robust break
show("D5-F use-form", "ir a + 동사 원형을 써서 문장을 바꿔 ‘~할 것’을 나타내세요.", "sans", False, 20.5, 434)
show("D5-G fronted", "‘~할 것’을 나타내도록 ir a + 동사 원형으로 문장을 바꾸세요.", "sans", False, 20.5, 434)
show("D5-H meaning-noun", "ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’의 뜻을 나타내세요.", "sans", False, 20.5, 434)
show("D5-I when-form", "문장을 바꿀 때는 ir a + 동사 원형을 써서 ‘~할 것’을 나타내세요.", "sans", False, 20.5, 434)
show("D5-J two-sent", "ir a + 동사 원형으로 문장을 바꾸세요. ‘~할 것’을 나타내세요.", "sans", False, 20.5, 434)
show("D5-K shorter-verb", "ir a + 동사 원형으로 문장을 고쳐 ‘~할 것’을 나타내세요.", "sans", False, 20.5, 434)

# D-4 extra: lengthened single-sentence with big slack check
show("D4-F long", "괄호 안에 있는 단어의 비교급이나 -ísimo 형태를 사용해서 빈칸을 채우세요.", "sans", False, 20.5, 434)
