# -*- coding: utf-8 -*-
"""Independent RE-proproof for W45 zh-tw-pt (post-fix full round). Read-only on
delivery/build dirs; all renders go to fresh copies under this work dir."""
import re, html, json, hashlib, base64, os
from collections import Counter

BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
ED = BASE + "/files/weekly-report-w45-zh-tw-pt/svg"
CO = BASE + "/files/weekly-report-w45-zhtw-core/svg"
W43 = BASE + "/files/weekly-report-zh-tw-pt/svg"
W43B = BASE + "/hidden_files/weekly-report-zh-tw-pt-build"
OUT = BASE + "/hidden_files/w45/zh-tw-pt-reproof/work"

TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
TAG_RE = re.compile(r"<text([^>]*)>(.*?)</text>", re.S)
CJK = re.compile(r"[\u2e80-\u9fff]")

def texts(path):
    s = open(path, encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TEXT_RE.findall(s)]

def elems(path):
    """(x, y, font-size, text) per text element."""
    s = open(path, encoding="utf-8").read()
    out = []
    for m in TAG_RE.finditer(s):
        a, inner = m.group(1), html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        def g(k):
            mm = re.search(r'\b' + k + r'="([^"]+)"', a)
            return mm.group(1) if mm else None
        try: x, y = float(g("x")), float(g("y"))
        except (TypeError, ValueError): continue
        out.append((x, y, g("font-size"), inner))
    return out

def cjkset(d):
    out, per = set(), {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            s = set()
            for t in texts(os.path.join(d, fn)):
                s |= set(CJK.findall(t))
            per[fn], out = s, out | s
    return out, per

# ---- Gate 2: CJK sets ----
ed, _ = cjkset(ED); co, _ = cjkset(CO); w43, _ = cjkset(W43)
union = co | w43
print(f"CJK core={len(co)} w43={len(w43)} union={len(union)} edition={len(ed)} "
      f"outside={sorted(ed-union)} ed-not-in-core={sorted(ed-co)}")
spot = list("邮说国龙马发让认议论贝财见车红灯无为乌鸟东丝")
hits = {}
for fn in sorted(os.listdir(ED)):
    for t in texts(os.path.join(ED, fn)):
        for c in spot:
            if c in t: hits.setdefault(c, []).append((fn, t[:80]))
print("simplified-spot hits:", {k: len(v) for k, v in hits.items()})

# ---- Gate 3: added strings with CJK (target-text drift check) ----
for fn in sorted(os.listdir(CO)):
    c, e = Counter(texts(os.path.join(CO, fn))), Counter(texts(os.path.join(ED, fn)))
    added = list((e - c).elements()); removed = list((c - e).elements())
    withcjk = [a for a in added if CJK.search(a)]
    print(f"{fn}: +{len(added)} -{len(removed)} added-with-CJK={len(withcjk)}")
    for a in withcjk: print(f"    +CJK: {a[:130]}")

# ---- Gate 6: P8 wrap-aware reassembly (keys block y>=1328) ----
p8 = elems(os.path.join(ED, "p8-test.svg"))
keys_block = [e for e in p8 if e[1] >= 1328]
print(f"P8 keys-block elements: {len(keys_block)}")
# columns at x 65/527/989/1451 width 434; sort by column then y
def col(x):
    for i, cx in enumerate([65, 527, 989, 1451]):
        if abs(x - cx) < 200: return i
    return 0 if x < 527 else 1 if x < 989 else 2 if x < 1451 else 3
keys_block.sort(key=lambda e: (col(e[0]), e[1]))
items, cur = {}, None
for x, y, fs, t in keys_block:
    m = re.match(r"^(\d+)\.\s", t)
    if m:
        cur = int(m.group(1)); items[cur] = [(x, y, t)]
    elif cur is not None and not t.startswith("— Página"):
        items[cur].append((x, y, t))
print(f"reassembled items: {len(items)} numbers={min(items)}..{max(items)} missing="
      f"{[n for n in range(1,151) if n not in items]}")
fw = {n: [t for _,_,t in fr if "（" in t or "）" in t] for n, fr in items.items() if any("（" in t or "）" in t for _,_,t in fr)}
print(f"answer-block full-width paren items: {list(fw)}")
reassembled = {}
for n, fr in sorted(items.items()):
    # join fragments: fragments are line wraps; join with space, then fix
    # split-word joins are inspected separately from raw fragments
    reassembled[n] = " ".join(t for _,_,t in fr)
json.dump(reassembled, open(os.path.join(OUT, "p8-reassembled.json"), "w"),
          ensure_ascii=False, indent=1)
# note extraction: strip "N. key (" prefix using registry keys loaded later is
# done in reproof2; here: note = text between FIRST '(' and LAST ')'
han_notes = {}
for n, s in reassembled.items():
    i, j = s.find("("), s.rfind(")")
    if i >= 0 and j > i:
        note = s[i+1:j]
        han = CJK.findall(note)
        if han: han_notes[n] = (note, han)
print(f"notes containing Han: {sorted(han_notes)}")
for n, (note, han) in sorted(han_notes.items()):
    print(f"  HAN {n}: {note[:140]} :: {han}")
# keys intact check: first segment before ' (' must contain the Han key for the 12
for n in [17, 35, 55, 101, 103, 105, 110, 112, 132, 133, 134, 138]:
    print(f"  item {n}: {reassembled[n][:130]}")
print(f"  item 149: {reassembled.get(149)}")
print(f"  item 138: {reassembled.get(138)}")

# ---- Gate 6c: KIT 13.1 table forms present in reassembled notes ----
table = {17:"jìnbǔ",25:"lìdōng",26:"jìnbǔ",27:"pàotāng",28:"jízhāng",35:"jiéqì",
43:"lìdōng",44:"jìnbǔ",45:"gāngdiāo",46:"shādiāo",55:"fēng wáng",61:"wánfēng",
62:"fēng wáng",63:"quánlěidǎ",64:"āndǎ",79:"tǎotáng",80:"cǎijiē",81:"nánguā tǒng",
82:"dǎkǎ",101:"tānwèi",103:"jízhāng",105:"fēng wáng",106:"wánfēng",109:"dǎkǎ",
110:"tǎotáng",111:"cǎijiē",112:"pàotāng",132:"fēng wáng",133:"tǎotáng",
134:"jízhāng",138:"réngōng zhìnéng＋",149:"xiān bǐjià, zài jiézhàng"}
for n, form in table.items():
    s = reassembled.get(n, "")
    # space-insensitive fallback for wrap-split words
    ok = form in s or form.replace(" ", "") in s.replace(" ", "")
    print(f"  table {n}: form {form!r} present={ok} :: {s[:130]}")

# ---- W43 precedent: feng wang / taotang in W43 P8; 人工智慧 anywhere in W43 ----
w43p8 = " ".join(texts(os.path.join(W43, "p8-test.svg")))
for form in ["fēng wáng", "tǎotáng", "人工智慧"]:
    print(f"W43 P8 contains {form!r}: {form in w43p8}")
print("W43 P8 feng-wang contexts:")
for t in texts(os.path.join(W43, "p8-test.svg")):
    if "fēng wáng" in t or "tǎotáng" in t: print("   ", t[:150])

# ---- Gate 7/12: badge, footer, separators, gloss, P3 catch ----
for label, path in [("core P1", CO+"/p1-front.svg"), ("W43pt P1", W43+"/p1-front.svg"),
                    ("edition P1", ED+"/p1-front.svg")]:
    print(f"--- badge {label}")
    s = open(path, encoding="utf-8").read()
    for m in TAG_RE.finditer(s):
        inner = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        if "TEXTOS EM" in inner or "繁體中文正文" in inner:
            print(f"   attrs={m.group(1).strip()[:240]} :: {inner[:140]}")
ed_p1_badge = [t for t in texts(os.path.join(ED,"p1-front.svg")) if "TEXTOS EM" in t]
w43_p1_badge = [t for t in texts(os.path.join(W43,"p1-front.svg")) if "TEXTOS EM" in t]
print("badge text edition==W43:", ed_p1_badge == w43_p1_badge, ed_p1_badge)
for label, d in [("edition", ED)]:
    for fn in sorted(os.listdir(d)):
        for t in texts(os.path.join(d, fn)):
            if "Lucerna ·" in t or re.match(r"^Página \d+ de \d+$", t.strip()) \
               or re.match(r"^— Página \d+ —$", t.strip()):
                print(f"   furn {fn}: {t}")
for label, d, pat in [("core", CO, "Notes"), ("edition", ED, "Nota — ")]:
    n = sum(1 for fn in sorted(os.listdir(d)) if fn.endswith(".svg")
            for t in texts(os.path.join(d, fn)) if pat in t)
    print(f"gloss-prefix {label}: {n}")
p3 = texts(os.path.join(ED, "p3-culture.svg"))
print("P3 算一算 nodes:", [t for t in p3 if "算一算" in t])
print("Work it out anywhere:", sum(1 for fn in sorted(os.listdir(ED))
      for t in texts(os.path.join(ED, fn)) if "Work it out" in t))

# ---- Gate 10/11: images + bars ----
IMG_RE = re.compile(r"<image([^>]*)>", re.S)
def images(path):
    s = open(path, encoding="utf-8").read(); out = []
    for m in IMG_RE.finditer(s):
        a = m.group(1)
        href = re.search(r'(?:xlink:href|href)="([^"]+)"', a)
        def g(k):
            mm = re.search(r'\b'+k+r'="([^"]+)"', a); return mm.group(1) if mm else None
        data = href.group(1) if href else ""
        dg = hashlib.sha256(base64.b64decode(data.split(",",1)[1])).hexdigest()[:16] if data.startswith("data:") else "EXT"
        out.append((g("x"), g("y"), g("width"), g("height"), dg))
    return out
RECT_RE = re.compile(r"<rect([^>]*)>", re.S)
def rects(path):
    s = open(path, encoding="utf-8").read(); out = []
    for m in RECT_RE.finditer(s):
        a = m.group(1)
        def g(k):
            mm = re.search(r'\b'+k+r'="([^"]+)"', a); return mm.group(1) if mm else None
        out.append((g("x"), g("y"), g("width"), g("height"), g("fill")))
    return out
for fn in sorted(os.listdir(CO)):
    ci, ei = images(os.path.join(CO, fn)), images(os.path.join(ED, fn))
    print(f"images {fn}: identical={ci==ei} core={ci} ed={ei}")
for label, d in [("core", CO), ("edition", ED)]:
    for fn in ["p4-sport.svg", "p6-deep.svg"]:
        rs = rects(os.path.join(d, fn))
        big = sorted(set((r[2], r[4]) for r in rs if r[2] and float(r[2]) >= 100))
        print(f"bars {label} {fn}: {big}")
for label, d in [("core", CO), ("edition", ED)]:
    for fn in ["p1-front.svg","p2-life.svg","p4-sport.svg","p5-youth.svg"]:
        for t in texts(os.path.join(d, fn)):
            if "Photo:" in t: print(f"credit {label} {fn}: {t}")

# ---- Gate 9/12: readers corner + disclosure ----
for label, d in [("core", CO), ("edition", ED)]:
    p7 = texts(os.path.join(d, "p7-lang.svg"))
    disc = [t for t in p7 if "convite continua aberto" in t or "invitation stays open" in t
            or "延期披露" in t or "Deferral notice" in t]
    print(f"readers-disclosure {label}: {disc}")
ed_p7 = texts(os.path.join(ED, "p7-lang.svg"))
print("PT disclosure full nodes:", [t for t in ed_p7 if "Carta de exemplo" in t])
print("frozen TW disclosure present in edition:",
      any("延期披露" in t for t in ed_p7))

# ---- Gate 10 golden sentences (quoted in P7, count issue-wide) ----
def alltexts(d):
    out = []
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"): out += texts(os.path.join(d, fn))
    return out
for label, d in [("core", CO), ("edition", ED)]:
    p7 = texts(os.path.join(d, "p7-lang.svg"))
    qs = []
    for t in p7: qs += re.findall(r"「([^」]+)」", t)
    all_t = " ".join(alltexts(d))
    print(f"--- P7 quoted {label}: {len(qs)}")
    for q in qs: print(f"   count={all_t.count(q)} :: {q[:70]}")
    print("   tags:", [t for t in p7 if re.search(r"p\.\s*\d", t)][:12])
