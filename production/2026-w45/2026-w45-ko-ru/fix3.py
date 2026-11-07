# -*- coding: utf-8 -*-
"""Fix round 3 (after round-2 build): two remaining overflows, Russian-side only.
Korean target text untouched. Same assertion discipline as transform.py.

1. P1-headline FLOW OVERFLOW: the RU P1 gloss ran 5 lines (core: 3), pushing
   the numbers box out of column 1 and the last drill past 1828. Terser gloss
   measures exactly 3 lines (same as core), so the numbers box fits col 1
   again. Gloss note: "온대저기압 = циклон" underspecifies "внетропический"
   (extratropical); the full term is carried by the P1/P4 articles, and the
   4-line variant with the full term still misses the fit by ~0.4px.
2. P8-keys FLOW OVERFLOW (cursor 2569 > 2540): 6 more note shortenings
   (each verified 2 -> 1 wrapped lines at 13.3pt/434px), covering items
   67/81, 68/119, 72, 77, 99, 131.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = {
    # P1 gloss (content12.py) — must measure 3 lines
    "입동 = ипдон, начало зимы · 절정 = пик, апогей · 김장 = заготовка кимчи на зиму · 상륙하다 = выйти на берег · 온대저기압 = внетропический циклон.":
        "입동 = ипдон · 절정 = пик · 김장 = кимчжан · 상륙하다 = выйти на берег · 온대저기압 = циклон.",
    # P8 notes
    "Во время аудирования самолёты не взлетают и не садятся":
        "Во время аудирования самолёты не летают",
    "Сотрудников безопасности в Сеуле на Хэллоуин — 3 271 человек":
        "Безопасность в Сеуле на Хэллоуин — 3 271 человек",
    "С пожеланием успешной сдачи дарят тток из клейкого риса и ёт":
        "С пожеланием сдачи дарят тток и ёт",
    "В день экзамена учреждения начинают работу в 10 часов":
        "В день экзамена учреждения работают с 10 часов",
    "Во время аудирования в день экзамена самолёты ограничены":
        "Самолёты ограничены во время аудирования",
    "На следующей неделе готовится к экзамену по истории Кореи":
        "На следующей неделе — экзамен по истории Кореи",
}
FILES = ["content12.py", "content34.py", "content56.py", "content8.py"]
texts = {}
for fn in FILES:
    with open(os.path.join(HERE, fn), encoding="utf-8") as fh:
        texts[fn] = fh.read()
for src, dst in sorted(FIX.items(), key=lambda kv: -len(kv[0])):
    total = sum(t.count(src) for t in texts.values())
    assert total >= 1, f"fix3 source absent: {src!r}"
    for fn in FILES:
        texts[fn] = texts[fn].replace(src, dst)
    assert not any(src in t for t in texts.values()), src
    print(f"ok x{total}: {src[:50]!r}")
for fn in FILES:
    with open(os.path.join(HERE, fn), "w", encoding="utf-8") as fh:
        fh.write(texts[fn])
print("fix3 applied")
