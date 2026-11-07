import json, re, html
from collections import Counter
CJK = re.compile(r"[\u2e80-\u9fff\uff00-\uffef]")
TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
def load(d, fn):
    s = open(f"{d}/{fn}", encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TEXT_RE.findall(s)]
CORE = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg"
ED = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-zh-tw/svg"
FILES = ["p1-une.svg","p2-vie.svg","p3-culture.svg","p4-sport.svg","p5-jeunesse.svg","p6-politique.svg","p7-langue.svg","p8-exercices.svg"]
d = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-zh-tw-proof/work/freeze-diff.json"))
for pg in sorted(d["pages"], key=int):
    v = d["pages"][pg]
    print(f"--- P{pg}: strings +{sum(x['count'] for x in v['added_strings'])} -{sum(x['count'] for x in v['removed_strings'])} | CJK {v['cjk_core_total']}->{v['cjk_edition_total']} (delta {v['cjk_edition_total']-v['cjk_core_total']}) | addedCJKinst {sum(v['cjk_added'].values())} distinct {len(v['cjk_added'])}")
# removed CJK per page (recompute)
for i, fn in enumerate(FILES, 1):
    c, e = Counter(load(CORE, fn)), Counter(load(ED, fn))
    cc = Counter(ch for s,n in c.items() for ch in s if CJK.match(ch) for _ in range(n))
    ce = Counter(ch for s,n in e.items() for ch in s if CJK.match(ch) for _ in range(n))
    rem = cc - ce; add = ce - cc
    print(f"P{i} removedCJK inst={sum(rem.values())} distinct={len(rem)} | addedCJK inst={sum(add.values())} | check delta={sum(add.values())-sum(rem.values())}")
    if i == 8:
        print("  P8 removed full-width parens:", rem.get("（",0), rem.get("）",0), " added half-width parens are ASCII (not CJK)")
        print("  P8 removed top:", rem.most_common(12))
        print("  P8 added top:", add.most_common(12))
    if i == 7:
        print("  P7 removed top:", rem.most_common(12))
        print("  P7 added top:", add.most_common(12))
# CJK-stripped multiset diff (French-freeze test)
print("\n=== CJK-stripped multiset diff (French + Latin + punctuation skeleton) ===")
for i, fn in enumerate(FILES, 1):
    c, e = Counter(load(CORE, fn)), Counter(load(ED, fn))
    strip = lambda s: CJK.sub("", s)
    cs = Counter(); es = Counter()
    for s,n in c.items(): cs[strip(s)] += n
    for s,n in e.items(): es[strip(s)] += n
    add, rem = es - cs, cs - es
    print(f"P{i}: stripped +{sum(add.values())} -{sum(rem.values())}")
    for s,n in add.items(): print(f"    ADDED  x{n} {s!r}")
    for s,n in rem.items(): print(f"    REMOVED x{n} {s!r}")
