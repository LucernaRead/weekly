# -*- coding: utf-8 -*-
"""RU core -> RU x ZH-TW explanation-layer transform (W45).

Rules honoured: whole quoted-literal replacement with per-file count
assertions (never byte-offset splicing); bare-text values (never repr
literals); single-process re-render through run.py afterwards.
The old explanation-function name appears below ONLY as a search
pattern for the rename; it never survives into the operative code or
any deliverable.
"""
import json, os, sys

B = os.path.dirname(os.path.abspath(__file__))
FILES = ["content12.py", "content34.py", "content56.py", "content7.py",
         "content8.py", "bslib4.py", "svglib.py"]

with open(os.path.join(B, "map.json"), encoding="utf-8") as f:
    MAP = json.load(f)

contents = {}
for fn in FILES:
    with open(os.path.join(B, fn), encoding="utf-8") as f:
        contents[fn] = f.read()

# ---- 1. literal map (quoted match, so short literals cannot hit longer ones)
total_repl = 0
for old, new in MAP.items():
    assert old != new
    qold, qnew = '"' + old + '"', '"' + new + '"'
    hit_files = 0
    for fn in FILES:
        n = contents[fn].count(qold)
        if n:
            hit_files += 1
            contents[fn] = contents[fn].replace(qold, qnew)
            total_repl += n
    assert hit_files >= 1, f"map entry never matched: {old!r}"
    for fn in FILES:
        assert contents[fn].count(qold) == 0, f"leftover {old!r} in {fn}"
print(f"literal map: {len(MAP)} entries, {total_repl} replacements")


def edit(fn, old, new, expect):
    global contents
    n = contents[fn].count(old)
    assert n == expect, f"{fn}: expected {expect} of {old[:60]!r}, found {n}"
    contents[fn] = contents[fn].replace(old, new)
    print(f"edit {fn}: {expect}x {old[:50]!r}")


# ---- 2. badge (W43 shipped same-pairing slot, verbatim string)
BADGE = ('p.text(975, 574, "俄語正文 · 繁體中文講解 — 給繁體中文讀者的版本", '
         '22, "sans", True, BRICK, anchor="middle")')
edit("content12.py",
     "p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)",
     "p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)\n"
     "# W43 shipped same-pairing badge slot (975, 574), 22pt BRICK\n" + BADGE,
     1)

# ---- 3. P8 separators (W43 shipped same-pairing form)
edit("content8.py", 'af.para(f"— СТРАНИЦА {pg} —"',
     'af.para(f"— 第 {pg} 版 —"', 1)

# ---- 4. explanation-function rename (definition + 20 call sites)
edit("bslib4.py", "def bridge(self, s", "def expl(self, s", 1)
for fn, n in [("content12.py", 4), ("content34.py", 6), ("content56.py", 6),
              ("content7.py", 3), ("content8.py", 1)]:
    edit(fn, ".bridge(", ".expl(", n)
for fn in FILES:
    assert "bridge" not in contents[fn], f"old function name left in {fn}"
print("rename: definition 1 + calls 20, old name 0 in operative code")

# ---- 5. svglib TC face (W43 shipped same-pairing form: 4 functional changes)
edit("svglib.py", "def _sc_index(path):", "def _tc_index(path):", 1)
edit("svglib.py", "_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}",
     "_IDX = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}", 1)
edit("svglib.py", 'endswith("SC")', 'endswith("TC")', 1)
edit("svglib.py", '"Noto Serif CJK SC"', '"Noto Serif CJK TC"', 1)
edit("svglib.py", '"Noto Sans CJK SC"', '"Noto Sans CJK TC"', 1)
assert "CJK SC" not in contents["svglib.py"]

# ---- 6. write back
for fn in FILES:
    with open(os.path.join(B, fn), "w", encoding="utf-8") as f:
        f.write(contents[fn])
print("TRANSFORM DONE")
