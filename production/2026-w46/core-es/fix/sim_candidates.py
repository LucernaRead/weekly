# -*- coding: utf-8 -*-
"""Candidate rewordings for D-2..D-5 — wrap simulation."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib_sim import wrap, text_w

def show(label, text, kind, bold, size, max_w):
    lines = wrap(text, kind, bold, size, max_w)
    print(f"== {label} ==")
    for ln in lines:
        print(f"  [{text_w(ln, kind, bold, size):6.1f}px] {ln!r}")
    return lines

# D-2 candidates (serif 20.5, w=398)
show("D2-A short-paren", "24 — horas dura la huelga general del miércoles 11 de noviembre (총파업은 24시간이에요)", "serif", False, 20.5, 398)
show("D2-B reorder", "24 — horas dura la huelga general del miércoles 11 de noviembre (총파업은 11월 11일에 24시간이에요)", "serif", False, 20.5, 398)
show("D2-C comma", "24 — horas dura la huelga general del miércoles 11 de noviembre (11월 11일 총파업, 24시간이에요)", "serif", False, 20.5, 398)
show("D2-D keep-date-short", "24 — horas dura la huelga general del miércoles 11 de noviembre (11월 11일, 총파업 24시간이에요)", "serif", False, 20.5, 398)

# D-3 candidates (serif 21, w=398)
show("D3-A place-first", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (세스타오에서 토요일 연방컵 결승)", "serif", False, 21, 398)
show("D3-B place-late", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일 연방컵 결승은 세스타오에서 열려요)", "serif", False, 21, 398)
show("D3-C comma", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일 세스타오, 연방컵 결승)", "serif", False, 21, 398)
show("D3-D drop-place", "Sábado 14 — final de la Copa Federación en Sestao, 19:00 (토요일 연방컵 결승이에요)", "serif", False, 21, 398)

# D-4 candidates (sans 20.5, w=434)
show("D4-A lengthen", "괄호 안에 있는 단어의 비교급이나 -ísimo 형태로 빈칸을 채우세요.", "sans", False, 20.5, 434)
show("D4-B superlative", "괄호 안 단어의 비교급이나 최상급 -ísimo 형태로 빈칸을 채우세요.", "sans", False, 20.5, 434)
show("D4-C reorder-verb-first", "빈칸을 채우세요. 괄호 안 단어의 비교급이나 -ísimo 형태를 쓰세요.", "sans", False, 20.5, 434)
show("D4-D shorten", "괄호 안 단어의 비교급·-ísimo 형으로 빈칸을 채우세요.", "sans", False, 20.5, 434)
show("D4-E lengthen2", "괄호 안에 있는 단어를 비교급이나 -ísimo 형태로 바꿔 빈칸을 채우세요.", "sans", False, 20.5, 434)

# D-5 candidates (sans 20.5, w=434)
show("D5-A drop-dongsa", "ir a + 원형으로 문장을 바꿔 ‘~할 것’을 나타내세요.", "sans", False, 20.5, 434)
show("D5-B future-word", "ir a + 동사 원형으로 문장을 바꿔 미래를 나타내세요.", "sans", False, 20.5, 434)
show("D5-C reorder", "문장을 바꿔 ‘~할 것’을 나타내세요. ir a + 동사 원형을 쓰세요.", "sans", False, 20.5, 434)
show("D5-D shorten2", "ir a + 원형으로 바꿔 ‘~할 것’을 나타내세요.", "sans", False, 20.5, 434)
show("D5-E lengthen", "ir a + 동사 원형으로 문장을 바꿔서 ‘~할 것’을 나타내세요.", "sans", False, 20.5, 434)
