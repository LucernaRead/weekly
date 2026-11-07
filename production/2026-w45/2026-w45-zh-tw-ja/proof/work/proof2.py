# -*- coding: utf-8 -*-
"""Proof round 2: corrected attribution, furniture exclusion, readers-corner
precise check, P8 heads, match instr counts, P7 geometry."""
import ast, html, json, os, re
from collections import Counter

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_SVG = os.path.join(GOAL, "files/weekly-report-w45-zhtw-core/svg")
ED_SVG = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja/svg")
W43_SVG = os.path.join(GOAL, "files/weekly-report-zh-tw-ja/svg")
ED_BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w45-zh-tw-ja-build")
WORK = os.path.join(GOAL, "hidden_files/w45/zh-tw-ja-proof/work")
TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)

def texts(d):
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            s = open(os.path.join(d, fn), encoding="utf-8").read()
            out[fn] = [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TEXT_RE.findall(s)]
    return out
core_txt, ed_txt, w43_txt = texts(CORE_SVG), texts(ED_SVG), texts(W43_SVG)

def norm(s):
    table = str.maketrans({"？": "?", "！": "!", "：": ":", "；": ";", "，": ",",
                           "。": ".", "、": ",", "（": "(", "）": ")", "＋": "+",
                           "～": "~", "－": "-", "／": "/", "「": "", "」": "",
                           "『": "", "』": "", "・": ".", "…": "..."})
    return re.sub(r"\s+", "", s.translate(table).replace("{NCHARS}", "138"))

tsrc = open(os.path.join(ED_BUILD, "transform.py"), encoding="utf-8").read()
tree = ast.parse(tsrc)
pairs = []
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "rep":
        args = [a.value for a in node.args if isinstance(a, ast.Constant)]
        if len(args) >= 3:
            pairs.append((args[0], args[1], args[2]))
new_all = norm("".join(new for _, _, new in pairs))
old_all = norm("".join(old for _, old, _ in pairs))
core_all = "".join(t for v in core_txt.values() for t in v)
core_all_n = norm(core_all)
# MODELO text (frozen): find core content8 MODELO literal start
c8 = open(os.path.join(GOAL, "hidden_files/weekly-report-w45-zhtw-build/content8.py"), encoding="utf-8").read()
mm = re.search(r"MODELO\s*=\s*\"([^\"]+)\"", c8)
modelo_n = norm(mm.group(1)) if mm else ""
print(f"MODELO found: {bool(mm)} len={len(modelo_n)}")

print("== TRANSFORM AUDIT, furniture pairs excluded ==")
FURN = ["Lucerna · 繁體中文週報", "第 {n} 版", "繁體中文正文 · 英語講解"]
bad = []
for fn, old, new in pairs:
    if any(f in old for f in FURN):
        continue
    for run in re.findall(r"[\u4e00-\u9fff]+", old):
        if run not in new:
            bad.append((fn, run, old[:60]))
print(f"  non-furniture CJK-loss violations: {len(bad)} {bad[:10]}")
print(f"  furniture pairs excluded: {sum(1 for _, o, _ in pairs if any(f in o for f in FURN))}")

print("== ATTRIBUTION, corrected norm ==")
fd = json.load(open(os.path.join(WORK, "freeze-diff.json")))
inst_new = "".join(f"{n}ページ(全8ページ)" for n in range(1, 9)) + "".join(f"—{n}ページ—" for n in range(1, 9))
inst_old = "".join(f"第{n}版/共8版" for n in range(1, 9)) + "".join(f"—Page{n}—" for n in range(1, 9))
unattr_add, unattr_rem = [], []
for pg, d in fd["pages"].items():
    for s in d.get("added_strings", []):
        st = s["text"] if isinstance(s, dict) else s
        nst = norm(st)
        nst2 = re.sub(r"^解説—", "", nst)
        nst2 = re.sub(r"^\d+\.\s*(✓\s*|.*?—\s*)", "", nst2)
        nst2 = re.sub(r"^モデル解答:", "", nst2)
        nst2 = re.sub(r"^作文—", "", nst2)
        nst2 = re.sub(r"\s*\(p\.\s*\d\)$", "", nst2)
        if nst in new_all or nst in core_all_n or nst in inst_new or nst2 in new_all or nst2 in core_all_n:
            continue
        if modelo_n and (nst in modelo_n or nst2 in modelo_n):
            continue
        if re.fullmatch(r"[\d\s·\-–.,:;()/]+", st) or st in ("Lucerna",) or st.startswith("Photo:"):
            continue
        unattr_add.append((pg, st[:80]))
    for s in d.get("removed_strings", []):
        st = s["text"] if isinstance(s, dict) else s
        nst = norm(st)
        nst_note = re.sub(r"^\d+\.\s*(✓\s*|.*?—\s*)", "", nst)
        if nst in inst_old or st.startswith("Modelanswer:") or nst in old_all or nst_note in old_all:
            continue
        if modelo_n and (nst in modelo_n or nst_note in modelo_n):
            continue
        if nst in core_all_n:
            continue
        unattr_rem.append((pg, st[:80]))
print(f"  unattributed ADDED: {len(unattr_add)} {unattr_add}")
print(f"  unattributed REMOVED: {len(unattr_rem)} {unattr_rem}")
# counted totals (with multiplicity)
for k, v in fd["pages"].items():
    ta = sum(s.get("count", 1) for s in v["added_strings"])
    tr = sum(s.get("count", 1) for s in v["removed_strings"])
    print(f"  p{k}: +{ta}/-{tr} cjk_added={v['cjk_added']}")
print(f"  cjk_added_total={fd['cjk_added_total']}")

print("== READERS CORNER, precise ==")
def p7nodes(txt):
    return txt["p7-lang.svg"]
for label, txt in [("CORE", core_txt), ("ED", ed_txt)]:
    v = p7nodes(txt)
    i = [j for j, t in enumerate(v) if "讀者園地" in t][0]
    print(f"  {label} corner header idx {i}: {v[i]!r}")
core_v, ed_v = p7nodes(core_txt), p7nodes(ed_txt)
ci = [j for j, t in enumerate(core_v) if "讀者園地" in t][0]
ei = [j for j, t in enumerate(ed_v) if "讀者園地" in t][0]
# letter = 4 nodes after header (quoted letter), disclosure = next 5 nodes
print(f"  letter identical: {core_v[ci+1:ci+5] == ed_v[ei+1:ei+5]}")
print(f"  trad disclosure identical: {core_v[ci+5:ci+10] == ed_v[ei+5:ei+10]}")
print(f"  ED disclosure nodes: {ed_v[ei+5:ei+10]}")
print(f"  ED japanese disclosure nodes: {ed_v[ei+10:ei+16]}")
print(f"  CORE english disclosure nodes: {core_v[ci+10:ci+15]}")

print("== P8 HEADS three-way ==")
for label, txt in [("CORE", core_txt), ("W43", w43_txt), ("ED", ed_txt)]:
    v = txt["p8-test.svg"]
    heads = [t for t in v if t.startswith("答案") or "解説はすべて日本語" in t or "All notes in English" in t]
    print(f"  {label}: {heads}")

print("== MATCH instr source counts ==")
for label, d in [("CORE", os.path.join(GOAL, "hidden_files/weekly-report-w45-zhtw-build")),
                 ("ED", ED_BUILD)]:
    tot = 0
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        src = open(os.path.join(d, fn), encoding="utf-8").read()
        tot += src.count('instr="Match"') + src.count('instr="語と意味を結ぶ"')
    print(f"  {label} match-instr occurrences: {tot}")

print("== P7 teaser + P8 keys geometry (SVG parse) ==")
import sys
sys.path.insert(0, os.path.join(GOAL, "tools"))
from occlusion_audit import ink_box, parse_svg
for label, path in [("ED-P7", os.path.join(ED_SVG, "p7-lang.svg")),
                    ("CORE-P7", os.path.join(CORE_SVG, "p7-lang.svg"))]:
    els, _, _ = parse_svg(open(path, encoding="utf-8").read())
    rects = [e for e in els if e.kind == "rect"]
    texts = [e for e in els if e.kind == "text"]
    print(f"  {label}: rects={len(rects)} texts={len(texts)}")
    # teaser = darkest rect near bottom (fill DARK); print bottom-most rects
    for r in sorted(rects, key=lambda e: e.box[3])[-3:]:
        print(f"    rect fill={r.attrs.get('fill')} box={tuple(round(x, 2) for x in r.box)}")
    # footer rule: line/rect at y=2580?
    for r in rects:
        if abs(r.box[1] - 2580) < 3 or abs(r.box[3] - 2580) < 3:
            print(f"    footer-rule rect: {tuple(round(x, 2) for x in r.box)} fill={r.attrs.get('fill')}")
print("== P8 keys last ink ==")
for label, path in [("ED-P8", os.path.join(ED_SVG, "p8-test.svg"))]:
    els, _, _ = parse_svg(open(path, encoding="utf-8").read())
    texts = [e for e in els if e.kind == "text"]
    mx = max(e.box[3] for e in texts if e.box[3] < 2580)
    last = sorted([e for e in texts if e.box[3] == mx], key=lambda e: e.box[0])
    print(f"  {label}: max ink bottom below-rule-excluded={mx:.1f}; last nodes: {[(e.text[:40], tuple(round(x,1) for x in e.box)) for e in last]}")
