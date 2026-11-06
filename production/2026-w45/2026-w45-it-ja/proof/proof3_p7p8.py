# -*- coding: utf-8 -*-
"""Gates 3, 4, 6 + counts + model text, independently from shipped SVGs."""
import re, html, os
from collections import Counter
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = BASE + "/files/weekly-report-w45-it-core/svg"
ED = BASE + "/files/weekly-report-w45-it-ja/svg"

def texts(p):
    t = open(p, encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
            for m in re.finditer(r"<text\b[^>]*>(.*?)</text>", t, re.S)]

def nodes(p):
    t = open(p, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<text\b([^>]*)>(.*?)</text>", t, re.S):
        out.append((m.group(1), html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))))
    return out

print("== Gate 3: P7 word box ==")
DEF = "« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone."
for label, d in [("core", CORE), ("edition", ED)]:
    joined = " ".join(texts(f"{d}/p7-lingua.svg"))
    print(label, "definition verbatim present:", DEF in joined)
    # also check the gloss line
    for x in texts(f"{d}/p7-lingua.svg"):
        if "assaggio" in x and ("試食" in x or "品尝" in x or "＝" in x or "=" in x):
            print("  ", label, repr(x))
print("P7 edition lines containing assaggio/試食:")
for x in texts(f"{ED}/p7-lingua.svg"):
    if "assaggio" in x or "試食" in x: print("  ", repr(x))

print("\n== Gate 3: P7 golden sentences 2x each, (Pagina N) tags ==")
core7 = " ".join(texts(f"{CORE}/p7-lingua.svg"))
ed7 = " ".join(texts(f"{ED}/p7-lingua.svg"))
# golden sentences: text nodes on P7 that are quote lines followed by (Pagina N) tag nodes
ednodes = texts(f"{ED}/p7-lingua.svg")
corenodes = texts(f"{CORE}/p7-lingua.svg")
print("core (Pagina tags):", [x for x in corenodes if x.startswith("(Pagina")])
print("edition (Pagina tags):", [x for x in ednodes if x.startswith("(Pagina")])
# candidate golden sentences = nodes immediately preceding a (Pagina tag in core order
for label, nds, joined in [("core", corenodes, core7), ("edition", ednodes, ed7)]:
    gold = []
    for i, x in enumerate(nds):
        if x.startswith("(Pagina") and i > 0:
            gold.append(nds[i-1])
    print(label, "gold count:", len(gold))
    for g in gold:
        print(f"   {g!r} x-core={core7.count(g)} x-ed={ed7.count(g)}")
    # also node-level count
    for g in gold:
        print(f"   node-count ed={sum(1 for x in ednodes if x==g)} core={sum(1 for x in corenodes if x==g)}")

print("\n== Gate 6: gloss counts ==")
# gloss() strings live in the build content files: find gloss calls in core build + JA build
import glob
def gloss_counts(builddir):
    tot = []
    for f in sorted(glob.glob(builddir + "/content*.py")):
        s = open(f, encoding="utf-8").read()
        for m in re.finditer(r"gloss\((.*?)\)\s*$", s, re.M):
            arg = m.group(1)
            # gloss string is the first quoted literal; split on middle dot
            lit = re.search(r'"([^"]*)"', arg)
            if lit:
                items = [i for i in lit.group(1).split("·")]
                tot.append((os.path.basename(f), lit.group(1)[:60], len(items)))
    return tot
# The build gloss() may be defined differently; instead extract from rendered SVGs:
# gloss boxes are the '解説 — ...' / '译注｜...' nodes; join consecutive nodes of the box.
# Simpler robust check: count '·' separators in the gloss-box node sequences per page.
# Here we report the raw gloss-box node texts per page for both sides.
for label, d, prefix in [("core", CORE, "译注"), ("edition", ED, "解説")]:
    print(f"-- {label} gloss-box nodes --")
    for p in ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento"]:
        for x in texts(f"{d}/{p}.svg"):
            if x.startswith(prefix):
                print(f"   {p} {x!r}")

print("\n== Gate 6: expl prefix counts ==")
for label, d in [("core", CORE), ("edition", ED)]:
    n1 = sum(1 for p in ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento","p7-lingua","p8-valutazione"]
             for x in texts(f"{d}/{p}.svg") if x.startswith("解説 — ") or x.startswith("译注"))
    n_single = sum(1 for p in ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento","p7-lingua","p8-valutazione"]
             for x in texts(f"{d}/{p}.svg") if "解説 — " in x)
    n_double = sum(1 for p in ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento","p7-lingua","p8-valutazione"]
             for x in texts(f"{d}/{p}.svg") if "解説 — 解説" in x or "解説 — —" in x)
    n_gram = sum(1 for p in ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento","p7-lingua","p8-valutazione"]
             for x in texts(f"{d}/{p}.svg") if x.startswith("文法ポイント — "))
    print(label, "解説/译注-start nodes:", n1, "解説 — occurrences:", n_single, "double-prefix:", n_double, "文法ポイント — :", n_gram)
    for p in ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento","p7-lingua"]:
        for x in texts(f"{d}/{p}.svg"):
            if "文法ポイント" in x: print("   grammar:", p, repr(x))

print("\n== Gate 6: P1 expl items ==")
for label, d in [("core", CORE), ("edition", ED)]:
    # P1 expl box: nodes starting at x=527 in the expl region; join nodes starting with prefix through '。' end
    seq = []
    grab = False
    for x in texts(f"{d}/p1-prima.svg"):
        if x.startswith("解説 — ") or x.startswith("译注"):
            grab = True
        if grab:
            seq.append(x)
            if x.rstrip().endswith("。"):
                break
    joined = "".join(seq)
    print(label, "P1 expl joined:", repr(joined))
    body = joined.split("—", 1)[1] if "—" in joined else joined
    print(label, "P1 expl items by · split:", [i for i in body.split("·")], "count:", len([i for i in body.split("·") if i.strip()]))
