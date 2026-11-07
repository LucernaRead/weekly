# -*- coding: utf-8 -*-
import re, os, glob
from collections import Counter
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = BASE + "/files/weekly-report-w45-zhtw-core/svg"
ED = BASE + "/files/weekly-report-w45-zh-tw-ko/svg"

def pagetext(d):
    out = {}
    for f in sorted(glob.glob(d + "/*.svg")):
        t = open(f, encoding="utf-8").read()
        nodes = re.findall(r'<text[^>]*>([^<]*)</text>', t)
        out[os.path.basename(f)] = "".join(nodes)
    return out
cp, ep = pagetext(CORE), pagetext(ED)
quotes = [
    ("用手機轉帳、掃碼付款、網上買保險，都是金融科技", "p. 1"),
    ("123個國家及城市、1,600個攤位", "p. 1"),
    ("需要才買，不要為了折扣買一堆用不到的東西", "p. 2"),
    ("在高雄，鋼鐵也能變成舞台", "p. 3"),
    ("福隆的夏天，在10月26日畫下句點", "p. 3"),
    ("6比0完封兄弟，龍隊拋下紅色彩帶", "p. 4"),
    ("250家店家一起討糖", "p. 5"),
    ("旅展首日中午12點才開門", "p. 6"),
]
print("GOLDEN (concatenated nodes, no separator):")
for q, pg in quotes:
    cc = sum(v.count(q) for v in cp.values())
    ec = sum(v.count(q) for v in ep.values())
    print(f"  core={cc} ed={ec} tag={pg} :: {q[:28]}")
# tag distribution in P7 (Korean translations + (p. N))
p7 = ep["p7-lang.svg"]
print("P7 tag distribution ed:", dict(sorted(Counter(re.findall(r'\(p\. \d\)', p7)).items())))
print("P7 tag distribution core:", dict(sorted(Counter(re.findall(r'\(p\. \d\)', cp["p7-lang.svg"])).items())))
# Hanzi set difference core - ed
def hset(txt):
    return set(ch for ch in txt if (0x4E00 <= ord(ch) <= 0x9FFF) or (0x3400 <= ord(ch) <= 0x4DBF) or (0xF900 <= ord(ch) <= 0xFAFF))
cs = set().union(*[hset(v) for v in cp.values()])
es = set().union(*[hset(v) for v in ep.values()])
print("core-only Hanzi chars:", sorted(cs - es), "ed-only:", sorted(es - cs))
# P1: which core text nodes contain 文 and are absent in ed?
cn = re.findall(r'<text[^>]*>([^<]*)</text>', open(CORE + "/p1-front.svg", encoding="utf-8").read())
en = re.findall(r'<text[^>]*>([^<]*)</text>', open(ED + "/p1-front.svg", encoding="utf-8").read())
print("P1 core nodes with 文 not in ed nodes:")
for n in cn:
    if "文" in n and n not in en:
        print("   ", repr(n[:120]))
# footer/page-line/badge accounting for P1 removed -30
print("P1 removed recount check: footer(16)+pageline(4)+badge(9)=29, observed 30; extra node above explains it")
