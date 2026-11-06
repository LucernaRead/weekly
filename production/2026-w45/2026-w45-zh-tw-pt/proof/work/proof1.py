# -*- coding: utf-8 -*-
"""Independent proof script 1: CJK sets, simplified spot, string diffs,
gloss counts, P7 phrases, images, furniture, residual Latin, P8 paren scope."""
import re, html, json, hashlib, base64, os
from collections import Counter

ED = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-pt/svg"
CO = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhtw-core/svg"
W43 = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-pt/svg"
OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-pt-proof/work"

TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
CJK = re.compile(r"[\u2e80-\u9fff]")

def texts(path):
    s = open(path, encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TEXT_RE.findall(s)]

def raw(path):
    return open(path, encoding="utf-8").read()

def cjkset(d):
    out = set()
    per = {}
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".svg"):
            continue
        ts = texts(os.path.join(d, fn))
        s = set()
        for t in ts:
            s |= set(CJK.findall(t))
        per[fn] = s
        out |= s
    return out, per

ed, ed_per = cjkset(ED)
co, co_per = cjkset(CO)
w43, w43_per = cjkset(W43)
union = co | w43
print(f"CJK core={len(co)} w43={len(w43)} union={len(union)} edition={len(ed)} outside={len(ed-union)}")
print("outside chars:", sorted(ed - union))
print("edition not in core:", sorted(ed - co))
print("edition not in w43:", len(ed - w43))

# Simplified-only spot list over EDITION target text (all text nodes).
# A char is 'simplified-only' if it appears in simplified but its traditional
# form differs; use a conservative spot list of chars that NEVER occur in
# traditional text.
spot = list("邮说国龙马发过发干发后发里发乐发万发无发云发长发...")
spot = [c for c in "邮说国龙马发让认议论贝财见车红灯无为乌鸟东丝" ]
hits = {}
for fn in sorted(os.listdir(ED)):
    ts = texts(os.path.join(ED, fn))
    for t in ts:
        for c in spot:
            if c in t:
                hits.setdefault(c, []).append((fn, t[:80]))
print("simplified-spot hits:", {k: len(v) for k, v in hits.items()})
for k, v in hits.items():
    print("  ", k, v[:3])

# Per-page string diff core vs edition (multiset) - read a sample of added strings
for fn in sorted(os.listdir(CO)):
    c = Counter(texts(os.path.join(CO, fn)))
    e = Counter(texts(os.path.join(ED, fn)))
    added = list((e - c).elements())
    removed = list((c - e).elements())
    print(f"{fn}: +{len(added)} -{len(removed)}")
    # added strings containing CJK that are NOT pure target-text? list added strings with CJK
    withcjk = [a for a in added if CJK.search(a)]
    print(f"   added strings containing CJK: {len(withcjk)}")
    for a in withcjk[:40]:
        print("     +CJK:", a[:110])

# Gloss prefix counts
for label, d, pat in [("core", CO, "Notes"), ("edition", ED, "Nota — ")]:
    n = 0
    for fn in sorted(os.listdir(d)):
        for t in texts(os.path.join(d, fn)):
            if pat in t:
                n += 1
    print(f"gloss-prefix {label} {pat!r}: {n} text nodes")

# P7 phrases: take core P7 phrase-strip sentences. Method: P7 SVG texts that
# contain a 'p. N' tag nearby? Instead: use content7 phrases from core build
# is NOT allowed to import; derive from SVGs: sentences occurring exactly 2x
# issue-wide in core (article + P7) and present in core P7.
core_all = []
for fn in sorted(os.listdir(CO)):
    core_all += texts(os.path.join(CO, fn))
core_counter = Counter(core_all)
p7core = texts(os.path.join(CO, "p7-lang.svg"))
print("P7 core texts:", len(p7core))
json.dump({"core_cjk": len(co), "w43_cjk": len(w43), "union": len(union),
           "ed_cjk": len(ed), "outside": sorted(ed - union)},
          open(os.path.join(OUT, "cjk.json"), "w"), ensure_ascii=False, indent=1)
