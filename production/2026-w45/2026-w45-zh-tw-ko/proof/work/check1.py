# -*- coding: utf-8 -*-
"""Independent proof checks for W45 zh-tw x ko. Read-only on delivery/core/W43."""
import re, os, glob, hashlib, json
from collections import Counter
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = BASE + "/files/weekly-report-w45-zhtw-core/svg"
ED = BASE + "/files/weekly-report-w45-zh-tw-ko/svg"
W43 = BASE + "/files/weekly-report-zh-tw-ko/svg"
PAGES = ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]

def nodes(d, p):
    t = open(f"{d}/{p}.svg", encoding="utf-8").read()
    return re.findall(r'<text[^>]*>([^<]*)</text>', t)
def raw(d, p):
    return open(f"{d}/{p}.svg", encoding="utf-8").read()
def is_hanzi(ch):
    o = ord(ch)
    return (0x4E00 <= o <= 0x9FFF) or (0x3400 <= o <= 0x4DBF) or (0xF900 <= o <= 0xFAFF)
def is_hangul(ch):
    o = ord(ch)
    return 0xAC00 <= o <= 0xD7A3 or 0x1100 <= o <= 0x11FF or 0x3130 <= o <= 0x318F

print("=== PDF/SVG sizes ===")
for f in sorted(glob.glob(BASE+"/files/weekly-report-w45-zh-tw-ko/*.pdf")):
    b = open(f,'rb').read()
    print(os.path.basename(f), len(b), hashlib.sha256(b).hexdigest())

print("\n=== 1. Hanzi accounting per page ===")
for p in PAGES:
    cc = Counter(ch for n in nodes(CORE,p) for ch in n if is_hanzi(ch))
    ec = Counter(ch for n in nodes(ED,p) for ch in n if is_hanzi(ch))
    add = ec - cc; rem = cc - ec
    print(f"{p}: added={sum(add.values())} {dict(add)} | removed={sum(rem.values())} {dict(rem)}")
    # removed chars must be subset of furniture alphabet
    furn = set("繁體中文正文英語講解週報第版共")
    bad = {ch: n for ch, n in rem.items() if ch not in furn}
    print(f"   removed-not-in-furniture-alphabet: {bad}")

print("\n=== 2. Union independence ===")
def hset(d):
    s = set()
    for p in PAGES:
        for n in nodes(d,p):
            s |= {ch for ch in n if is_hanzi(ch)}
    return s
edset, coreset, w43set = hset(ED), hset(CORE), hset(W43)
print(f"|ed|={len(edset)} |core|={len(coreset)} |w43|={len(w43set)} outside={sorted(edset-w43set-coreset)}")
print(f"core-only (chars in core not ed): {sorted(coreset-edset)}")
print(f"ed-only vs core: {sorted(edset-coreset)}")

print("\n=== 2b. Simplified-only spot (expanded list) ===")
# Chars whose Traditional form differs, incl builder list + extras
simp = set("汉说国龙发对东车门见长马鸟鱼气电为让认议论设访证评读课谚艳艺节艰难风时实万与写军农冲决况冻净凛凝爱亲亿仅仪义尔发会个这进远运选录识观现头买卖里劳疗怜邻龙")
for p in PAGES:
    txt = "".join(nodes(ED,p))
    hits = sorted({ch for ch in txt if ch in simp})
    if hits: print(f"  {p}: {hits}")
print("  (blank = 0 hits on all pages)")
# U+FFFD check
for p in PAGES:
    t = raw(ED,p)
    if "\ufffd" in t: print(f"  U+FFFD FOUND in {p}: {t.count(chr(0xfffd))}")
print("  U+FFFD scan done")
print("  byte check 穿 U+7A7F present per page:", {p: ("穿" in "".join(nodes(ED,p))) for p in PAGES})
print("  byte check 고객 present in p8:", "고객" in "".join(nodes(ED,"p8-test")))
print("  ord 穿:", hex(ord("穿")), " 고객 ords:", [hex(ord(c)) for c in "고객"])

print("\n=== 3. Target-text run-level check ===")
# Strip Hangul + Latin letters from each node, compare Hanzi/digit/CJK-punct skeletons
def skel(n):
    out = []
    for ch in n:
        if is_hangul(ch): continue
        if ch.isascii() and ch.isalpha(): continue
        out.append(ch)
    return "".join(out)
for p in PAGES:
    cm = Counter(skel(n) for n in nodes(CORE,p))
    em = Counter(skel(n) for n in nodes(ED,p))
    rem = cm - em; add = em - cm
    print(f"{p}: skeleton-removed nodes ({sum(rem.values())}):")
    for n, c in rem.items():
        if n.strip(): print(f"    REM x{c}: {n[:130]!r}")
    print(f"   skeleton-added nodes ({sum(add.values())}):")
    for n, c in add.items():
        if n.strip(): print(f"    ADD x{c}: {n[:130]!r}")

print("\n=== 9. Gloss prefix + 算一算 + Latin sweep ===")
for p in PAGES:
    txt = "".join(nodes(ED,p))
    print(f"{p}: 해설 — count={txt.count('해설 — ')} Notes｜={txt.count('Notes｜')} 算一算 heads: {[n for n in nodes(ED,p) if '算一算' in n]}")
block = ["Fill in","Work it out","Did you get it","Over to you","Read the chart","Test & keys","True or false","Readers' corner","Phrases of the week","Next week","Error clinic","Sentence frame","Language focus","Word of the week","Quick quiz","Headline words","This week's facts","Champion deals","Model answer","Answer keys","All notes in English","Writing —","Open task","in English","English explanations","Explanations in English"]
alled = " ".join("".join(nodes(ED,p)) for p in PAGES)
for b in block:
    if b in alled: print(f"  BLOCKLIST HIT: {b!r}")
print("  blocklist scan done")
# residual Latin runs (excluding known frozen)
import string
lat = re.findall(r'[A-Za-z][A-Za-z0-9\'\-\.\,\:\!\? ]{2,}', alled)
from collections import Counter as C2
print("  Latin runs (top):", C2(lat).most_common(60))

print("\n=== 10. Golden sentences ===")
quotes = [
    ("用手機轉帳、掃碼付款、網上買保險，都是金融科技","p. 1"),
    ("123個國家及城市、1,600個攤位","p. 1"),
    ("需要才買，不要為了折扣買一堆用不到的東西","p. 2"),
    ("在高雄，鋼鐵也能變成舞台","p. 3"),
    ("福隆的夏天，在10月26日畫下句點","p. 3"),
    ("6比0完封兄弟，龍隊拋下紅色彩帶","p. 4"),
    ("250家店家一起討糖","p. 5"),
    ("旅展首日中午12點才開門","p. 6"),
]
cp_all = "".join("".join(nodes(CORE,p)) for p in PAGES)
ep_all = "".join("".join(nodes(ED,p)) for p in PAGES)
for q, tag in quotes:
    print(f"  core={cp_all.count(q)} ed={ep_all.count(q)} claimed-tag={tag} :: {q[:30]}")
p7e = "".join(nodes(ED,"p7-lang")); p7c = "".join(nodes(CORE,"p7-lang"))
print("  P7 tag dist ed:", dict(sorted(Counter(re.findall(r'\(p\. \d\)', p7e)).items())))
print("  P7 tag dist core:", dict(sorted(Counter(re.findall(r'\(p\. \d\)', p7c)).items())))
# which quote carries which tag: find P7 nodes containing quote + nearby tag
p7nodes = nodes(ED,"p7-lang")
for q, tag in quotes:
    hits = [n for n in p7nodes if q[:12] in n]
    print(f"  P7 node for {q[:12]}: {hits}")

print("\n=== 11. Images ===")
def images(d):
    out = {}
    for p in PAGES:
        t = raw(d,p)
        blobs = re.findall(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', t)
        out[p] = [hashlib.sha256(b.encode()).hexdigest()[:16] for b in blobs]
    return out
ci, ei = images(CORE), images(ED)
for p in PAGES:
    print(f"  {p}: core={ci[p]} ed={ei[p]} equal={ci[p]==ei[p]}")
for p in PAGES:
    for m in re.finditer(r'Photo:[^<]*', raw(ED,p)):
        print(f"  CREDIT {p}: {m.group(0)[:160]}")

print("\n=== 12. Readers corner ===")
for p in ["p7-lang"]:
    for n in nodes(ED,p):
        if "延期披露" in n or "편집부" in n or "편지" in n or "독자 코너" in n or "讀者園地" in n:
            print(f"  ED {p}: {n[:220]!r}")
    for n in nodes(CORE,p):
        if "延期披露" in n:
            print(f"  CORE {p}: {n[:220]!r}")
    # frozen letter lt: compare core vs ed nodes containing Taipei reader letter markers
    print("  ED P7 nodes with 台北小讀者/編輯範例:", [n[:80] for n in nodes(ED,p) if "台北小讀者" in n or "編輯範例" in n])

print("\n=== 13. Furniture ===")
for d, label in [(CORE,"CORE"),(W43,"W43"),(ED,"ED")]:
    p1 = raw(d,"p1-front")
    for m in re.finditer(r'<text[^>]*>([^<]*)</text>', p1):
        pass
    # badge: node containing 해설 or 英語講解 or 한국어 해설
    ns = nodes(d,"p1-front")
    badge = [n for n in ns if "해설" in n or "英語講解" in n or "한국어 독자" in n]
    print(f"  {label} badge nodes: {badge}")
    # extract badge element attrs
    for m in re.finditer(r'<text([^>]*)>([^<]*(?:해설|英語講解)[^<]*)</text>', p1):
        print(f"    {label} badge attrs: {m.group(1)[:200]} :: {m.group(2)[:80]}")
    foot = [n for n in ns if n.startswith("Lucerna")]
    print(f"  {label} footer-ish: {foot}")
print("  ED P8 heads:")
for n in nodes(ED,"p8-test"):
    if "答案" in n or "모든 해설" in n or "測驗與答案" in n or "第 8 版" in n:
        print(f"    {n[:160]!r}")
print("  W43 P8 heads:")
for n in nodes(W43,"p8-test"):
    if "答案" in n or "모든 해설" in n or "測驗與答案" in n or "第 8 版" in n:
        print(f"    {n[:160]!r}")
print("  ED P8 separators:", sorted(set(re.findall(r'— 제 \d+ 면 —', "".join(nodes(ED,"p8-test"))))))
print("  ED gloss prefix total rendered:", sum("".join(nodes(ED,p)).count("해설 — ") for p in PAGES))

print("\n=== 6. AI forms ===")
for p in PAGES:
    for n in nodes(ED,p):
        if "人工智慧" in n or "AI는" in n or "AI를" in n:
            print(f"  {p}: {n[:200]!r}")
print("  P8 key 138-ish nodes:")
for n in nodes(ED,"p8-test"):
    if n.strip().startswith("138."):
        print(f"    {n[:200]!r}")

print("\n=== P7 geometry (raw) ===")
p7 = raw(ED,"p7-lang")
# find rects near readers box: print all rects with y in 1100-1800
for m in re.finditer(r'<rect[^>]*>', p7):
    s = m.group(0)
    ys = re.search(r'y="([\d.]+)"', s); hs = re.search(r'height="([\d.]+)"', s)
    if ys and hs and 1100 <= float(ys.group(1)) <= 1800:
        print(f"  rect: {s[:220]}")
