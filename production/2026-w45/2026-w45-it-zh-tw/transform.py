# -*- coding: utf-8 -*-
"""IT x ZH-TW fan-out transform for the W45 IT core build copy.

Method (same discipline as W43 IT x ZH-TW and W45 NL x ZH-TW):
  A. OUT repoint (5 content files + render.py) + PDF names (-ZHTW).
  B. OpenCC s2twp whole-file conversion of the 5 content modules ONLY,
     with a per-file assertion that the non-CJK character stream is
     byte-identical before/after (Italian body, numbers, code untouched).
  C. Taiwan-native fixes, each with a count assertion, decided by a
     full line-by-line review of the converted strings (see LOG).
  D. Column furniture from the shipped W43 IT x ZH-TW SVG (which wins
     over any generic table): badge inserted at y=574, 22pt bold BRICK;
     footer VOL.2; page line; gloss prefix; P8 head + separators.
  E. W43 same-pair precedent: .bridge( -> .expl( (def + 22 calls);
     svglib TC face switch (4 lines, EN x ZH-TW pattern).

P7 word-box rule: the Italian definition sentence (wt) is byte-frozen;
only the gloss note below it is localised. The P7 letter's Italian text
(lt, incl. its own "(esempio della redazione)" label) is byte-frozen;
only the Chinese disclosure/invitation note below it is rewritten, in
Traditional Chinese, stating all 3 facts + an explicit invitation.
No new Italian disclosure sentence is written (coordinator ruling).

Guard: refuses to run on an already-transformed copy. Fix rounds =
edit THIS file, re-copy the core build fresh, re-run from the top.
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
LOG = []
CJK = re.compile(r"[\u4e00-\u9fff]")


def rep(fname, old, new, expect=None):
    p = os.path.join(BASE, fname)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if expect is not None:
        assert n == expect, f"{fname}: {old!r} count {n} != {expect}"
    else:
        assert n >= 1, f"{fname}: {old!r} not found"
    LOG.append(f"{fname}: {n}x {old!r} -> {new!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))


def rep_if(fname, old, new):
    p = os.path.join(BASE, fname)
    if old in open(p, encoding="utf-8").read():
        rep(fname, old, new)


# ---------- guard: fresh core copy only ----------
c12 = open(os.path.join(BASE, "content12.py"), encoding="utf-8").read()
assert "weekly-report-w45-it-core" in c12, "OUT already repointed?"
assert "義大利語正文" not in c12, "already transformed?"

# ---------- A. OUT repoint + PDF names ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-it-core", "weekly-report-w45-it-zh-tw", 1)
rep("render.py", "weekly-report-w45-it-core", "weekly-report-w45-it-zh-tw", 1)
rep("render.py", "La-Lucerna-VOL2.pdf", "La-Lucerna-VOL2-ZHTW.pdf", 1)
rep("render.py", "La-Lucerna-VOL2-web.pdf", "La-Lucerna-VOL2-ZHTW-web.pdf", 1)

# ---------- B. OpenCC s2twp on the 5 content modules ----------
from opencc import OpenCC

conv = OpenCC("s2twp")
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    p = os.path.join(BASE, f)
    before = open(p, encoding="utf-8").read()
    after = conv.convert(before)
    assert CJK.sub("", before) == CJK.sub("", after), f"{f}: non-CJK stream changed!"
    open(p, "w", encoding="utf-8").write(after)
    LOG.append(f"{f}: OpenCC s2twp applied (non-CJK stream identical)")

# ---------- C. Taiwan-native fixes (full converted-string review) ----------
# C1. s2twp residue: single-char 周 missed by the phrase dictionary (3 sites).
rep("content12.py", "意 大 利 語 周 報", "意 大 利 語 週 報", 1)  # spaced nameplate (also 意->義)
rep("content12.py", "初寒之周", "初寒之週", 1)
rep("content34.py", "足球周", "足球週", 1)
# C2. NL x ZH-TW error class: s2twp maps 词组 -> 片語; Taiwan grammar term is 詞組 (2 sites).
rep("content34.py", "把片語成正確的句子", "把詞組成正確的句子", 1)
rep("content8.py", "疑問片語在句首", "疑問詞組在句首", 1)
# C3. Statistics contexts take 數據, not s2twp's 資料 (4 sites).
rep("content34.py", "資料看賽程表", "數據看賽程表", 1)
rep("content56.py", "示例資料", "示例數據", 2)
rep("content56.py", "圖表資料", "圖表數據", 1)
# C4. Explanation-layer curved quotes -> Taiwanese 「」 (4 pairs: P1 dir 1, P7 bridge 2, P7 item 1).
rep("content12.py", "“第一場寒冷”：溫和秋天後的第一波寒冷。",
    "「第一場寒冷」：溫和秋天後的第一波寒冷。", 1)
rep("content7.py", "天氣用無人稱動詞（第三人稱單數）；“我冷”說 ho freddo，“外面冷”說 fa freddo。",
    "天氣用無人稱動詞（第三人稱單數）；「我冷」說 ho freddo，「外面冷」說 fa freddo。", 1)
rep("content7.py", "“我冷”說 ho freddo", "「我冷」說 ho freddo", 1)
# C5. P7 readers' corner note (appears twice: box-height computation + print).
# Coordinator ruling: TC disclosure states all 3 facts (no real letters;
# no best P8 writing this issue; example + deferral to VOL.3) + an explicit
# invitation (imperative 請 + VOL.3 publication promise). Italian letter
# text (lt) is NOT touched; no new Italian disclosure sentence is written.
OLD_NOTE = "這是編輯部示例信，非真實來信。來信請寄編輯部，VOL.3 刊登真實來信與第 8 版最佳作文！"
NEW_NOTE = "這是編輯部示例信，非真實來信；本期無最佳第 8 版作文。請寄來信，VOL.3 刊登真實來信與最佳作文！"
rep("content7.py", OLD_NOTE, NEW_NOTE, 2)
# C6. P8 head + separators: W43 IT x ZH-TW column forms (core's 參考答案頭 replaced,
# as W45 NL x ZH-TW did for its own core head; separators PAGINA -> 第 N 版).
rep("content8.py", "RISPOSTE · 參考答案 — 按版面分頁排列，找到題號即可",
    "RISPOSTE · 全部答案與簡析（第 1–8 版）", 1)
rep("content8.py", "— PAGINA {pg} —", "— 第 {pg} 版 —", 1)

# ---------- D. bslib4 furniture + bridge -> expl (W43 same-pair precedent) ----------
rep("bslib4.py",
    '"La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY"',
    '"La Lucerna · 義大利語週報 VOL.2 · 正文義大利語 · 講解繁體中文"', 1)
rep("bslib4.py", '"译注｜" + s', '"譯注｜" + s', 1)
rep("bslib4.py", "def bridge(self, s", "def expl(self, s", 1)
for f, n in [("content12.py", 5), ("content34.py", 7), ("content56.py", 6),
             ("content7.py", 3), ("content8.py", 1)]:
    rep(f, ".bridge(", ".expl(", n)
# P1 pairing badge: W43 IT x ZH-TW geometry (no free subtitle slot in the
# IT family: y=372 is the frozen Italian strapline -> INSERT at y=574,
# 22pt bold BRICK, centred; README #20 IT-family case).
rep("content12.py",
    'p.text(RIGHT - 30, 522, "初寒之週 · 詳見第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
    'p.text(RIGHT - 30, 522, "初寒之週 · 詳見第 2 版", 21, "sans", False, "#b3a06a", anchor="end")\n'
    '\n'
    '# pairing badge (W43 IT x ZH-TW geometry: inserted y=574, 22pt bold BRICK)\n'
    'p.text(975, 574, "義大利語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 22, "sans", True, BRICK, anchor="middle")',
    1)

# ---------- E. svglib TC face switch (EN x ZH-TW 4-line pattern) ----------
rep("svglib.py", "def _sc_index(path):", "def _tc_index(path):", 1)
rep("svglib.py", 'if f.getname()[0].endswith("SC"):', 'if f.getname()[0].endswith("TC"):', 1)
rep("svglib.py", "_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}",
    "_IDX = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}", 1)
rep("svglib.py", '("Noto Serif CJK SC" if kind == "serif" else "Noto Sans CJK SC")',
    '("Noto Serif CJK TC" if kind == "serif" else "Noto Sans CJK TC")', 1)
rep("svglib.py", "for 重阳.", "for Double Ninth.", 1)  # docstring only, never rendered

# ---------- final residue assertions on operative code ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
    s = open(os.path.join(BASE, f), encoding="utf-8").read()
    for bad in ["周", "片語", "資料", "概率", "“", "”", "桥接", "bridge"]:
        assert bad not in s, f"{f}: residue {bad!r} remains"
    assert "義大利語正文" in s or f != "content12.py"

open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8").write("\n".join(LOG) + "\n")
print(f"transform done, {len(LOG)} log lines")
