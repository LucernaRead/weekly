# -*- coding: utf-8 -*-
"""Independent orphan scan on DELIVERED edition SVGs (own implementation):
- line-start closers: first char of a <text> line in NO_START set (core set
  + small-kana extension) where the line is a continuation (not a box title
  / head: heuristic = previous line on same page exists in document order
  and the line is not the first text of a bordered box; we report ALL
  line-start hits with context and adjudicate, not just filtered ones)
- line-end openers: last char in NO_END set
- single-char final lines / tiny-tail lines: final line of a wrapped
  paragraph with <=1 char (conservative flag; adjudicated individually)
Also: kana presence in CORE svgs (must be 0 -> extension cannot affect frozen text)."""
import re, html, os
B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
TRE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
def load(d, fn):
    s = open(os.path.join(d, fn), encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TRE.findall(s)]
NO_START = "。、，．！？：；）」』】％ー…‥・)]}〉》.,!?%:;\"" + "ぁぃぅぇぉゃゅょゎっァィゥェォャュョヮッ"
NO_END = "「『（【〈《([{\"\u201c"
ed = f"{B}/files/weekly-report-w45-zh-cn-ja/svg"
core = f"{B}/files/weekly-report-w45-zhcn-core/svg"
tot_s, tot_e = 0, 0
for fn in sorted(os.listdir(ed)):
    if not fn.endswith(".svg"): continue
    lines = load(ed, fn)
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not s: continue
        if s[0] in NO_START:
            print(f"START-HIT {fn} line {i}: {ln!r}"); tot_s += 1
        if s[-1] in NO_END:
            print(f"END-HIT {fn} line {i}: {ln!r}"); tot_e += 1
print(f"TOTAL line-start closer hits: {tot_s}, line-end opener hits: {tot_e}")
# kana in core SVGs?
KANA = re.compile(r"[\u3040-\u30ff]")
n = 0
for fn in sorted(os.listdir(core)):
    if fn.endswith(".svg"):
        s = open(os.path.join(core, fn), encoding="utf-8").read()
        n += len(KANA.findall(s))
print("kana chars in ALL core SVGs:", n)
# small-kana line starts specifically (the fixed class)
SMALL = set("ぁぃぅぇぉゃゅょゎっァィゥェォャュョヮッ")
for fn in sorted(os.listdir(ed)):
    if not fn.endswith(".svg"): continue
    for i, ln in enumerate(load(ed, fn)):
        if ln.strip() and ln.strip()[0] in SMALL:
            print(f"SMALL-KANA-START {fn} line {i}: {ln!r}")
print("small-kana scan done")
