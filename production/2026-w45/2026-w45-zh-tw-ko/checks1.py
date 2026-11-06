# -*- coding: utf-8 -*-
"""Golden phrases, image payloads, Hanzi accounting, Simplified spot,
union-set check for W45 zh-tw x ko."""
import re, os, glob, hashlib
from collections import Counter
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = BASE + "/files/weekly-report-w45-zhtw-core/svg"
ED = BASE + "/files/weekly-report-w45-zh-tw-ko/svg"
W43 = BASE + "/files/weekly-report-zh-tw-ko/svg"

def texts(d):
    out = []
    for f in sorted(glob.glob(d + "/*.svg")):
        t = open(f, encoding="utf-8").read()
        out.append(" ".join(re.findall(r'<text[^>]*>([^<]*)</text>', t)))
    return out

# --- golden phrases: 8 Traditional quotes from core content7, each exactly 2x issue-wide
quotes = [
    "用手機轉帳、掃碼付款、網上買保險，都是金融科技",
    "123個國家及城市、1,600個攤位",
    "需要才買，不要為了折扣買一堆用不到的東西",
    "在高雄，鋼鐵也能變成舞台",
    "福隆的夏天，在10月26日畫下句點",
    "6比0完封兄弟，龍隊拋下紅色彩帶",
    "250家店家一起討糖",
    "旅展首日中午12點才開門",
]
ct, et = " ".join(texts(CORE)), " ".join(texts(ED))
print("GOLDEN:")
for q in quotes:
    print(f"  core={ct.count(q)} ed={et.count(q)} :: {q[:30]}")
# page tags in edition P7
p7 = open(ED + "/p7-lang.svg", encoding="utf-8").read()
print("P7 page tags:", sorted(set(re.findall(r'\(p\. \d\)', p7))))

# --- image payloads: base64 image blobs per page, core vs ed
def images(d):
    out = {}
    for f in sorted(glob.glob(d + "/*.svg")):
        t = open(f, encoding="utf-8").read()
        blobs = re.findall(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', t)
        out[os.path.basename(f)] = [hashlib.sha256(b.encode()).hexdigest()[:16] for b in blobs]
    return out
ci, ei = images(CORE), images(ED)
print("IMAGES (per-page payload sha prefixes):")
for k in sorted(ci):
    print(f"  {k}: core={ci[k]} ed={ei[k]} equal={ci[k]==ei[k]}")
# credits verbatim
for f in sorted(glob.glob(ED + "/*.svg")):
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r'Photo:[^<]*', t):
        print("  CREDIT", os.path.basename(f), m.group(0)[:90])

# --- Hanzi accounting: Hanzi = U+4E00-U+9FFF, U+3400-U+4DBF, U+F900-U+FAFF
def hanzi_counter(d):
    c = Counter()
    for f in sorted(glob.glob(d + "/*.svg")):
        t = open(f, encoding="utf-8").read()
        txt = " ".join(re.findall(r'<text[^>]*>([^<]*)</text>', t))
        for ch in txt:
            o = ord(ch)
            if (0x4E00 <= o <= 0x9FFF) or (0x3400 <= o <= 0x4DBF) or (0xF900 <= o <= 0xFAFF):
                c[ch] += 1
    return c
def per_page(d):
    out = {}
    for f in sorted(glob.glob(d + "/*.svg")):
        t = open(f, encoding="utf-8").read()
        txt = " ".join(re.findall(r'<text[^>]*>([^<]*)</text>', t))
        c = Counter(ch for ch in txt if (0x4E00 <= ord(ch) <= 0x9FFF) or (0x3400 <= ord(ch) <= 0x4DBF) or (0xF900 <= ord(ch) <= 0xFAFF))
        out[os.path.basename(f)] = c
    return out
cp, ep = per_page(CORE), per_page(ED)
print("HANZI per page (added / removed chars with counts):")
for k in sorted(cp):
    add = ep[k] - cp[k]
    rem = cp[k] - ep[k]
    print(f"  {k}: +{sum(add.values())} {dict(add)} / -{sum(rem.values())} {dict(rem)}")
# union set check: edition Hanzi set ⊆ W43-set ∪ core-set ?
w43set = set(hanzi_counter(W43))
coreset = set(hanzi_counter(CORE))
edset = set(hanzi_counter(ED))
outside = sorted(edset - w43set - coreset)
print(f"UNION: |ed|={len(edset)} |w43|={len(w43set)} |core|={len(coreset)} outside={outside}")
# Simplified-only spot list (chars whose Traditional form differs)
simp_only = set("汉说国龙发对东车门见长马鸟鱼气电为让认议论设访证评读课谚艳艺节艰难风时实万与写军农冲决况冻净凛凝爱亲亿仅仪义尔发")
found = sorted(set(ch for ch in " ".join(texts(ED)) if ch in simp_only))
print("SIMPLIFIED-ONLY spot hits in edition:", found)
# also: any Simplified-only char in my Korean source strings? check build sources
src = ""
for f in glob.glob(BASE + "/hidden_files/weekly-report-w45-zh-tw-ko-build/content*.py") + [BASE + "/hidden_files/weekly-report-w45-zh-tw-ko-build/bslib4.py"]:
    src += open(f, encoding="utf-8").read()
print("SIMPLIFIED-ONLY in build sources:", sorted(set(ch for ch in src if ch in simp_only)))
