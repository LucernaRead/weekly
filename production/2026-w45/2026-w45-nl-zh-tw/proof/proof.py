# -*- coding: utf-8 -*-
"""Independent proof for NL x ZH-TW W45. Does NOT import builder checks.py.
Reuses only canonical tools/occlusion_audit.py parsing + PIL metrics."""
import glob, html, json, os, re, sys
from collections import Counter
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA

B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = f"{B}/files/weekly-report-w45-nl-zh-tw/svg"
CO = f"{B}/files/weekly-report-w45-nl-core/svg"
W43 = f"{B}/files/weekly-report-nl-zh-tw/svg"
PAGES = ["p1-voorpagina", "p2-leven", "p3-cultuur", "p4-sport", "p5-jongeren",
         "p6-verdieping", "p7-taal", "p8-toets"]
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
CJKP = "，。、；：？！「」『』（）《》·—"

def texts(path):
    s = open(path, encoding="utf-8").read()
    return [OA.clean_text(m.group("tcontent")) for m in OA.TAG_RE.finditer(s)
            if m.group("tattrs") is not None]

def raw(path):
    return open(path, encoding="utf-8").read()

def cjkset(d):
    out = set()
    for f in sorted(glob.glob(f"{d}/*.svg")):
        out |= set(CJK.findall(raw(f)))
    return out

def strip_cjk(s):
    return CJK.sub("", s)

def norm(s):
    s = strip_cjk(s)
    for ch in CJKP:
        s = s.replace(ch, "")
    return re.sub(r"\s+", " ", s).strip()

print("=== A. CJK reference sets ===")
ed_cjk = cjkset(ED); w43_cjk = cjkset(W43); co_cjk = cjkset(CO)
print(f"edition distinct CJK: {len(ed_cjk)}")
print(f"W43 zh-tw distinct CJK: {len(w43_cjk)}")
print(f"core distinct CJK: {len(co_cjk)}")
unseen_w43 = sorted(ed_cjk - w43_cjk)
print(f"edition chars NOT in W43 zh-tw set: {len(unseen_w43)}")
print("unseen list:", "".join(unseen_w43))
# candidate simplified-form chars: single-char s2t change via opencc if available
try:
    from opencc import OpenCC
    cc = OpenCC("s2t")
    cand = [c for c in sorted(ed_cjk) if cc.convert(c) != c]
    print(f"s2t-changing chars in edition (simplified-form candidates): {len(cand)}: {''.join(cand)}")
except Exception as e:
    print("opencc unavailable:", e); cand = []
# contexts for unseen + candidates
all_ed_texts = {}
for p in PAGES:
    all_ed_texts[p] = texts(f"{ED}/{p}.svg")
for c in unseen_w43:
    ctxs = []
    for p, ts in all_ed_texts.items():
        for t in ts:
            if c in t:
                i = t.index(c); ctxs.append(f"{p}:{t[max(0,i-8):i+9]!r}")
    print(f"  UNSEEN {c} U+{ord(c):04X} n_ctx={len(ctxs)} :: " + " | ".join(ctxs[:6]))
for c in cand:
    if c not in unseen_w43:
        continue
    # already printed above
    pass
print("--- all occurrences of 只 ---")
for p, ts in all_ed_texts.items():
    for t in ts:
        if "只" in t:
            print(f"  {p}: {t!r}")

print("\n=== B. non-CJK residual (freeze strings, CJK stripped) ===")
fd = json.load(open(f"{B}/hidden_files/w45/nl-zh-tw-proof/freeze-diff.json"))
for pno, pg in fd["pages"].items():
    add = Counter(); rem = Counter()
    for it in pg["added_strings"]: add[norm(it["text"])] += it["count"]
    for it in pg["removed_strings"]: rem[norm(it["text"])] += it["count"]
    diff_add = add - rem; diff_rem = rem - add
    print(f"page {pno}: residual added={dict(diff_add)} removed={dict(diff_rem)}")

print("\n=== C. geometry non-text multiset core vs edition ===")
TAG = re.compile(r"<(rect|line|path|image|circle)\b([^>]*?)/?>", re.S)
for p in PAGES:
    a = Counter(m.group(0) for m in TAG.finditer(raw(f"{CO}/{p}.svg")))
    b = Counter(m.group(0) for m in TAG.finditer(raw(f"{ED}/{p}.svg")))
    print(f"{p}: core {sum(a.values())} edition {sum(b.values())} equal={a==b}")
    if a != b:
        print("  only-core:", list((a-b).items())[:5]); print("  only-ed:", list((b-a).items())[:5])

print("\n=== D. P7 word box ===")
core7 = texts(f"{CO}/p7-taal.svg"); ed7 = texts(f"{ED}/p7-taal.svg")
target = "«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee."
print("core has definition verbatim:", any(target in t for t in core7))
print("edition has definition verbatim:", any(target in t for t in ed7))
for t in ed7:
    if "meedoen" in t: print("  ed meedoen line:", repr(t))
    if "參加" in t and "meedoen" in t: print("  ed gloss line:", repr(t))

print("\n=== E. P7 quotes + labels ===")
for name, ts in [("core", core7), ("edition", ed7)]:
    print(f"--- {name} P7 texts (last 40) ---")
    for t in ts[-40:]:
        print("   ", repr(t))

print("\n=== F. gloss counts P2-P6 (rendered gloss lines split on ·) ===")
def gloss_lines(ts):
    # gloss lines: contain ' · ' and a Dutch word followed by CJK gloss; exclude headers
    out = []
    for t in ts:
        if " · " in t and CJK.search(t) and re.search(r"[A-Za-z]", t):
            out.append(t)
    return out
for p in ["p2-leven", "p3-cultuur", "p4-sport", "p5-jongeren", "p6-verdieping"]:
    ct = gloss_lines(texts(f"{CO}/{p}.svg")); et = gloss_lines(texts(f"{ED}/{p}.svg"))
    print(f"{p}: core lines={len(ct)} items={[len(t.split('·')) for t in ct]}")
    print(f"{p}: ed   lines={len(et)} items={[len(t.split('·')) for t in et]}")
    for t in et: print("    ed:", repr(t))

print("\n=== G. P8 printed lines ===")
def p8lines(path):
    return texts(path)
co8 = p8lines(f"{CO}/p8-toets.svg"); ed8 = p8lines(f"{ED}/p8-toets.svg")
print(f"core P8 text elements: {len(co8)}, edition: {len(ed8)}")
for n in [7, 70, 71, 76, 96, 137, 138, 148, 150, 139, 140]:
    def find(ts, n):
        pat = re.compile(rf"(^|\D){n}\.\s")
        return [t for t in ts if pat.search(t)]
    print(f"#{n} core:", find(co8, n))
    print(f"#{n} ed  :", find(ed8, n))
print("--- P8 separators / header ---")
for t in ed8:
    if "第" in t and "版" in t or "ANTWOORDEN" in t or "答案" in t:
        print("  ed:", repr(t))
for t in co8:
    if "PAGINA" in t or "ANTWOORDEN" in t or "参考答案" in t:
        print("  core:", repr(t))

print("\n=== H. registry diff ===")
rc = json.load(open(f"{B}/hidden_files/weekly-report-w45-nl-zh-tw-build/reg-core/reg.json"))
re_ = json.load(open(f"{B}/hidden_files/weekly-report-w45-nl-zh-tw-build/reg-ed/reg.json"))
def reg_items(r):
    if isinstance(r, dict):
        items = r.get("items") or r.get("exercises") or r
        if isinstance(items, dict): return items
        if isinstance(items, list): return {str(it.get("n", it.get("num", i+1))): it for i, it in enumerate(items)}
    return {}
ic, ie = reg_items(rc), reg_items(re_)
print("registry types:", type(rc), list(rc.keys())[:10] if isinstance(rc, dict) else "", "| items:", len(ic), len(ie))
print("registry top-level keys core:", list(rc.keys()) if isinstance(rc, dict) else "")
print("registry top-level keys ed:", list(re_.keys()) if isinstance(re_, dict) else "")
# dump one item shape
for k in list(ic)[:1]:
    print("sample core item:", json.dumps(ic[k], ensure_ascii=False)[:600])
    print("sample ed item:", json.dumps(ie.get(k), ensure_ascii=False)[:600])
keydiff_reg = []
for k in sorted(ic, key=lambda x: int(x) if str(x).isdigit() else 9999):
    a, b = ic[k], ie.get(k)
    if b is None: print("missing in ed registry:", k); continue
    ka = a.get("key") if isinstance(a, dict) else None
    kb = b.get("key") if isinstance(b, dict) else None
    if ka != kb: keydiff_reg.append((k, ka, kb))
print("registry KEY diffs:", keydiff_reg)
# bracket-ending notes
def note_of(it):
    if isinstance(it, dict):
        for f in ("note", "notes", "comment", "explanation"):
            if f in it: return it[f]
    return None
brack = []
for k, it in ic.items():
    n = note_of(it)
    if isinstance(n, str) and n.rstrip().endswith("）"):
        brack.append(int(k))
print("core registry notes ending with fullwidth ）:", sorted(brack), "count", len(brack))
brack_ed = []
for k, it in ie.items():
    n = note_of(it)
    if isinstance(n, str) and n.rstrip().endswith("）"):
        brack_ed.append(int(k))
print("ed registry notes ending with fullwidth ）:", sorted(brack_ed), "count", len(brack_ed))

print("\n=== I. reader garden P7 ===")
for t in ed7:
    if any(w in t for w in ["BRIEVEN", "voorbeeld", "編輯部", "歡迎", "VOL.3", "來信", "作文"]):
        print("  ed:", repr(t))
for t in core7:
    if any(w in t for w in ["BRIEVEN", "voorbeeld", "VOL.3"]):
        print("  core:", repr(t))

print("\n=== J. furniture vs W43 ===")
def badge_footer(d, p="p1-voorpagina"):
    s = raw(f"{d}/{p}.svg")
    out = []
    for m in OA.TAG_RE.finditer(s):
        if m.group("tattrs") is not None:
            at = OA.parse_attrs(m.group("tattrs")); tx = OA.clean_text(m.group("tcontent"))
            if "De Lucerna ·" in tx or "荷語週報" in tx or "荷兰语周报" in tx or "繁體中文講解" in tx or "简体中文讲解" in tx or "荷語正文" in tx:
                out.append((at, tx))
    return out
print("W45 ed P1 furniture:", badge_footer(ED))
print("W43 ed P1 furniture:", badge_footer(W43))
print("W45 core P1 furniture:", badge_footer(CO))
# P1 badge-slot element: text near y=372
for name, d in [("W45ed", ED), ("W43ed", W43), ("W45core", CO)]:
    s = raw(f"{d}/p1-voorpagina.svg")
    for m in OA.TAG_RE.finditer(s):
        if m.group("tattrs") is not None:
            at = OA.parse_attrs(m.group("tattrs"))
            if abs(OA.fnum(at, "y") - 372) < 3:
                print(f"  {name} y~372:", at, repr(OA.clean_text(m.group("tcontent"))[:90]))
print("footers all pages (ed):")
for p in PAGES:
    for t in texts(f"{ED}/{p}.svg"):
        if "De Lucerna ·" in t: print(f"  {p}:", repr(t))
print("footers W43:")
for p in PAGES:
    for t in texts(f"{W43}/{p}.svg"):
        if "De Lucerna ·" in t: print(f"  {p}:", repr(t))

print("\n=== K. credits / images ===")
for p in ["p1-voorpagina", "p2-leven", "p3-cultuur", "p4-sport"]:
    for name, d in [("core", CO), ("ed", ED)]:
        s = raw(f"{d}/{p}.svg")
        nimg = len(re.findall(r"<image\b", s))
        cred = [t for t in texts(f"{d}/{p}.svg") if "Foto" in t or "CC0" in t or "公共" in t or "Spaarnestad" in t or "Archief" in t or "Vovogov" in t or "Punt" in t]
        print(f"{p} {name}: images={nimg} credits={cred}")

print("\n=== L. lone punctuation structures ===")
for p in PAGES:
    ct, et = texts(f"{CO}/{p}.svg"), texts(f"{ED}/{p}.svg")
    for label, ts in [("core", ct), ("ed", et)]:
        for i, t in enumerate(ts):
            if t in ("）", "。") or t.startswith("："):
                nxt = ts[i+1][:60] if i+1 < len(ts) else ""
                print(f"  {p} {label} idx{i}: {t!r} prev={ts[i-1][:60]!r} next={nxt!r}")

print("\n=== M. P6 bars ===")
for name, d in [("core", CO), ("ed", ED)]:
    s = raw(f"{d}/p6-verdieping.svg")
    els, W, H = OA.parse_svg(s)
    bars = [(e.attrs, e.box) for e in els if e.kind == "rect" and e.box and 1451 <= e.box[0] <= 1885 and 200 <= e.box[1] <= 714]
    print(f"{name} chart-region rects:", [(a.get('x'), a.get('y'), a.get('width'), a.get('height'), a.get('fill')) for a, b in bars])
    print(f"{name} chart labels:")
    for e in els:
        if e.kind == "text" and 1451 <= OA.fnum(e.attrs, "x") <= 1885 and 200 <= e.baseline <= 691:
            print("   ", repr(e.text), e.attrs.get("x"), e.baseline, e.attrs.get("font-size"), e.attrs.get("text-anchor"))
