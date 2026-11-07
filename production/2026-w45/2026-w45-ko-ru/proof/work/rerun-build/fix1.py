# -*- coding: utf-8 -*-
"""Fix round 1 applier: the 4 REPL entries appended to transform.py AFTER
its first run (transform.py is single-use: a second full run would abort
on already-applied sources). Same assertion discipline: each source must
occur >=1 time and be absent afterwards. The entries live in transform.py;
this file only applies them to the already-transformed tree."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = {
    "内藏山公团预报峰值11月11日": "Пик по прогнозу парковой корпорации по Нэчжансану — 11 ноября",
    "月出山林业厅预报峰值11月9日": "Пик по прогнозу лесной службы по Вольчхульсану — 9 ноября",
    "首尔报名窗口10点至12点": "Окно записи в Сеуле с 10 до 12 часов",
    # Repair of a first-pass substring artifact (see transform.py note).
    "特别Меры действуют только 19 ноября": "Особые меры действуют только 19 ноября",
}
FILES = ["content56.py", "content8.py"]
texts = {}
for fn in FILES:
    with open(os.path.join(HERE, fn), encoding="utf-8") as fh:
        texts[fn] = fh.read()
for src, dst in sorted(FIX.items(), key=lambda kv: -len(kv[0])):
    total = sum(t.count(src) for t in texts.values())
    assert total >= 1, f"fix source absent: {src!r}"
    for fn in FILES:
        texts[fn] = texts[fn].replace(src, dst)
    assert not any(src in t for t in texts.values()), src
    print(f"ok x{total}: {src!r}")
for fn in FILES:
    with open(os.path.join(HERE, fn), "w", encoding="utf-8") as fh:
        fh.write(texts[fn])
print("fix1 applied")
