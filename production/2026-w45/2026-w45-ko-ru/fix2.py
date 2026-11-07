# -*- coding: utf-8 -*-
"""Fix round 2 (after round-1 build): overflow repairs, all Russian-side only.
Korean target text untouched. Same assertion discipline as transform.py.
Also recorded in the KIT fix log.

1. P5-feature FLOW OVERFLOW (last gloss box clamped past 1560): terse P5
   glosses save 3 lines (~89px), matching the core's 8 gloss lines.
2. P8-keys FLOW OVERFLOW (flow end 2569 > 2540): 5 shortened notes save
   5 lines (~77px).
3. P7 teaser end 2695 > 2540: phrases pitch 132 -> 102 (rows measure 76px,
   26px air, same as ko-fr) + shorter readers-corner disclosure (6 -> 4
   lines). Predicted teaser end ~2517.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = {
    # P5 glosses (content56.py)
    "정리 = приводить в порядок, повторять · 끈끈하다 = липкий · 합격 = успешная сдача.":
        "정리 = повторение · 끈끈하다 = липкий · 합격 = сдача.",
    "중점 = приоритетный · 배치하다 = размещать · 통제하다 = перекрывать, контролировать.":
        "중점 = главный · 배치하다 = разместить · 통제하다 = перекрывать.",
    "챙기다 = приготовить заранее · 졸리다 = хотеть спать · 평소 = обычно.":
        "챙기다 = приготовить · 졸리다 = сонливость · 평소 = обычно.",
    "비다 = молиться, желать · 피하다 = избегать · 미끄럽다 = скользкий.":
        "비다 = молиться · 피하다 = избегать · 미끄럽다 = скользкий.",
    # P8 notes (content34.py + content8.py share several strings)
    "Пик по прогнозу лесной службы по Нэчжансану — 4 ноября":
        "Пик по лесной службе, Нэчжансан — 4 ноября",
    "Пик по прогнозу парковой корпорации по Нэчжансану — 11 ноября":
        "Пик по парковой корпорации, Нэчжансан — 11 ноября",
    "Прогноз парковой корпорации по Нэчжансану — 11-е число":
        "Прогноз парковой корпорации, Нэчжансан — 11-е",
    "С 13 часов 6 ноября — запись по всей стране на оставшиеся места":
        "С 13 часов 6 ноября — запись на оставшиеся места",
    "Пик по прогнозу лесной службы по Вольчхульсану — 9 ноября":
        "Пик по лесной службе, Вольчхульсан — 9 ноября",
    # P7 readers-corner disclosure (content7.py)
    "К моменту сдачи в печать настоящих писем читателей и лучшего сочинения со стр. 8 не поступило: пример остаётся, а обещание переносится в VOL.3. Присылайте нам свои письма и свои тексты со стр. 8!":
        "Настоящих писем и лучшего сочинения со стр. 8 к сдаче номера не поступило: пример остаётся, обещание — в VOL.3. Присылайте письма и тексты со стр. 8!",
    # P7 phrases pitch (content7.py)
    "cyq = fy + 66 + (i % 4) * 132": "cyq = fy + 66 + (i % 4) * 102",
    "py = fy + 66 + 4 * 132 + 18": "py = fy + 66 + 4 * 102 + 18",
}
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]
texts = {}
for fn in FILES:
    with open(os.path.join(HERE, fn), encoding="utf-8") as fh:
        texts[fn] = fh.read()
for src, dst in sorted(FIX.items(), key=lambda kv: -len(kv[0])):
    total = sum(t.count(src) for t in texts.values())
    assert total >= 1, f"fix2 source absent: {src!r}"
    for fn in FILES:
        texts[fn] = texts[fn].replace(src, dst)
    assert not any(src in t for t in texts.values()), src
    print(f"ok x{total}: {src[:50]!r}")
for fn in FILES:
    with open(os.path.join(HERE, fn), "w", encoding="utf-8") as fh:
        fh.write(texts[fn])
print("fix2 applied")
