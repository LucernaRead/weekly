# -*- coding: utf-8 -*-
"""Reverse the W45 EN x ES transform to reconstruct the pristine EN core
build sources, as provenance for the EN x PT fan-out.

Method: import the ES build's transform.py R list and apply every pair
backwards (new -> old) in exact reverse order, with the same count
assertions. Then repoint OUT from the ES edition dir back to the core
svg dir. The reconstruction is PROVEN, not trusted: the copy is then
run through tools/freeze.py baseline, which must report 8/8 SVGs
byte-identical to the shipped core SVGs. Never run this copy with OUT
pointing at any files/ dir except through freeze.py's scratch repoint.
"""
import os
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ES_BUILD = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w45-en-es-build")
ES_ED = "weekly-report-w45-en-es"
CORE_ED = "weekly-report-w45-en-core"

spec = importlib.util.spec_from_file_location(
    "es_transform", os.path.join(ES_BUILD, "transform.py"))
es = importlib.util.module_from_spec(spec)
spec.loader.exec_module(es)

cache = {}


def load(fname):
    if fname not in cache:
        cache[fname] = open(os.path.join(HERE, fname), encoding="utf-8").read()
    return cache[fname]


# Two forward pairs each collide on one Spanish string; disambiguate by
# full-tuple context, verified against file order + the ES transform's
# own section order (TRY IT NOW f.ex sequence vs LIGHTNING QUIZ qf.ex
# sequence; cloze_defs vs dlg_defs) and the core P8 printed notes
# (116. A(sticker 贴纸) vs 148. sticker(sticker = 贴纸)).
CONTEXT = [
    ("content8.py",
     '("A2", "A", "sticker = pegatina")',
     '("A2", "A", "sticker 贴纸")'),
    ("content8.py",
     '("A2", "sticker", "sticker = pegatina")',
     '("A2", "sticker", "sticker = 贴纸")'),
    ("content12.py",
     'f.ex("A2", "Completar frases", "November 3", "día de elecciones, martes 3 de noviembre",',
     'f.ex("A2", "Completar frases", "November 3", "选举日 11 月 3 日（周二）",'),
    ("content12.py",
     'qf.ex("A2", "Opción múltiple", "B", "día de elecciones, martes 3 de noviembre",',
     'qf.ex("A2", "Opción múltiple", "B", "选举日 11 月 3 日周二",'),
]
SKIP = {("content8.py", '"sticker 贴纸"'), ("content8.py", '"sticker = 贴纸"'),
        ("content12.py", '"选举日 11 月 3 日（周二）"'),
        ("content12.py", '"选举日 11 月 3 日周二"')}
for fname, new_ctx, old_ctx in CONTEXT:
    s = load(fname)
    n = s.count(new_ctx)
    assert n == 1, f"CONTEXT {fname}: {new_ctx[:60]} found {n}"
    cache[fname] = s.replace(new_ctx, old_ctx)

problems = []
for fname, old, new, exp in reversed(es.R):
    if (fname, old) in SKIP:
        continue
    if old == new:
        continue
    s = load(fname)
    n = s.count(new)
    if exp is None:
        if n < 1:
            problems.append(f"NOT FOUND {fname}: {new[:70]}")
            continue
    elif n != exp:
        problems.append(f"COUNT {fname}: {new[:70]} found {n} expected {exp}")
        continue
    cache[fname] = s.replace(new, old)

if problems:
    print("REVERSE PROBLEMS (aborting, nothing written):")
    for p in problems:
        print(" ", p)
    sys.exit(1)

for fname in ["content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py"]:
    s = load(fname)
    assert ES_ED in s, f"OUT not found in {fname}"
    cache[fname] = s.replace(ES_ED, CORE_ED)

for fname, s in cache.items():
    open(os.path.join(HERE, fname), "w", encoding="utf-8").write(s)
    print("reversed", fname)
print("reverse OK")
