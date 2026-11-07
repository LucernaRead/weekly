# -*- coding: utf-8 -*-
"""Independent conservation check (substring method, own implementation):
every UNIQUE Han run in the core page (minus replaced furniture strings)
must occur as a substring of the edition page joined text. Also reports
the no-furniture-removal picture, the 45-vs-44 kana-less set diff vs the
builder's list, MODELO joined equality, and the P1/件 cases."""
import re, html, os, glob
from collections import Counter
B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = f"{B}/files/weekly-report-w45-zhcn-core/svg"
ED = f"{B}/files/weekly-report-w45-zh-cn-ja/svg"
TRE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
HAN = re.compile(r"[\u4e00-\u9fff]+")
def load(d):
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            s = open(os.path.join(d, fn), encoding="utf-8").read()
            out[fn] = [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TRE.findall(s)]
    return out
core, ed = load(CORE), load(ED)
FURN = set()
for fn, lines in core.items():
    for ln in lines:
        if ln.startswith("Lucerna · 简体中文周报") or re.match(r"^第 \d+ 版 / 共 8 版$", ln):
            FURN.add(ln)
FURN.add("简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers")
print("Furniture strings excluded:", len(FURN))
tot_miss = 0
for fn in sorted(core):
    cj = "".join(core[fn]); ej = "".join(ed[fn])
    cj_nf = cj
    for f in FURN: cj_nf = cj_nf.replace(f, "")
    runs = dict.fromkeys(HAN.findall(cj_nf))
    miss = [r for r in runs if r not in ej]
    runs_all = dict.fromkeys(HAN.findall(cj))
    miss_all = [r for r in runs_all if r not in ej]
    tot_miss += len(miss)
    print(f"{fn}: unique core runs (furn-removed) {len(runs)}, MISSING {len(miss)} {miss}")
    print(f"   without furniture removal: unique {len(runs_all)}, missing {len(miss_all)} {miss_all}")
print("TOTAL missing (furn-removed):", tot_miss)

# ---- kana-less added set vs builder's 44 ----
KANA = re.compile(r"[\u3040-\u30ff]")
my45 = set()
for fn in sorted(core):
    cr, er = Counter(core[fn]), Counter(ed[fn])
    for s in (er - cr):
        if not KANA.search(s): my45.add((fn, s))
b = open(f"{B}/hidden_files/weekly-report-w45-zh-cn-ja-build/scratch/attribute-out.txt", encoding="utf-8").read()
bset = set()
for line in b.splitlines():
    m = re.match(r"  (\S+\.svg) :: (.*)$", line)
    if m and "ADDED strings" not in line:
        # only the ADDED section: lines after the ADDED header
        bset.add((m.group(1), m.group(2)))
# restrict bset to the ADDED section
sec = b.split("ADDED strings without kana (manual adjudication): 44\n", 1)[1].split("\n--- Chinese-run", 1)[0]
bset = set()
for line in sec.splitlines():
    m = re.match(r"  (\S+\.svg) :: (.*)$", line)
    if m: bset.add((m.group(1), m.group(2)))
print(f"\nmy kana-less added: {len(my45)}; builder list: {len(bset)}")
print("in mine but not builder's:", sorted(my45 - bset))
print("in builder's but not mine:", sorted(bset - my45))

# ---- MODELO joined equality ----
def model_block(lines, head_pred):
    idx = next(i for i, s in enumerate(lines) if head_pred(s))
    # collect until the keys head line containing 答案 and 'Answer'/'全解答'
    out = [lines[idx]]
    for s in lines[idx+1:]:
        if ("答案" in s and ("Answer keys" in s or "全解答" in s)):
            break
        out.append(s)
    return out
cb = model_block(core['p8-ceyan.svg'], lambda s: s.startswith("Model answer:"))
eb = model_block(ed['p8-ceyan.svg'], lambda s: "モデル解答" in s)
cj = "".join(cb); ej = "".join(eb)
print("\ncore model block head:", repr(cb[0][:60]), "nlines:", len(cb))
print("ed model block head:", repr(eb[0][:60]), "nlines:", len(eb))
core_model = cj[len("Model answer: "):]
ed_model = ej[ej.index("：")+1:] if "：" in ej[:20] else ej
print("core model chars:", len(core_model), "ed model chars:", len(ed_model), "IDENTICAL:", core_model == ed_model)
if core_model != ed_model:
    for i, (a, bb) in enumerate(zip(core_model, ed_model)):
        if a != bb: print(" first diff at", i, repr(core_model[max(0,i-20):i+20]), "VS", repr(ed_model[max(0,i-20):i+20])); break
    print(" core tail:", repr(core_model[-60:]), "\n ed tail:", repr(ed_model[-60:]))
# ---- P1 sentence + 件 cases ----
p1e = "".join(ed['p1-touiban.svg'])
print("\nP1 sentence intact across lines:", "立冬那天，我们吃饺子。" in p1e.replace("」", "」") or ("立冬那天，" in p1e and "我们吃饺子。" in p1e))
p7e = "".join(ed['p7-ciyu.svg'])
print("P7 clinic conserves 一件毛衣/一条围巾/一部电影:", all(x in p7e for x in ("一件毛衣", "一条围巾", "一部电影")))
print("P7 件 present:", "件" in p7e, "| P8 件 present:", "件" in "".join(ed['p8-ceyan.svg']))
