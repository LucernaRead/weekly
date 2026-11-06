import json, re, sys, unicodedata
from collections import Counter
import xml.etree.ElementTree as ET
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    # extract <text> element full text (concatenate tspans in order)
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'):
            s=''.join(el.itertext())
            out.append(s)
    return out
def hangul(s): return sum(1 for c in s if '\uAC00'<=c<='\uD7A4' or '\u1100'<=c<='\u11FF' or '\u3130'<=c<='\u318F')
def cjk(s): return sum(1 for c in s if ('\u4E00'<=c<='\u9FFF' or '\u3040'<=c<='\u30FF'))
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
hangul_segments=re.compile(r'[\uAC00-\uD7A3\u1100-\u11FF\u3130-\u318F]+')
for i,p in enumerate(pages,1):
    core=texts(f"{BASE}/files/weekly-report-w45-ko-core/svg/{p}.svg")
    ed=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg")
    cc, ec = Counter(core), Counter(ed)
    added=list((ec-cc).elements()); removed=list((cc-ec).elements())
    hc=sum(hangul(s)*n for s,n in cc.items()); he=sum(hangul(s)*n for s,n in ec.items())
    print(f"=== p{i} {p}: nodes core {len(core)} ed {len(ed)} added {len(added)} removed {len(removed)} hangul core {hc} ed {he} delta {he-hc}")
    # core hangul segments set
    core_segs=set()
    for s in cc: core_segs.update(hangul_segments.findall(s))
    # added strings with hangul: check segments
    print("  ADDED with Hangul:")
    for s in sorted(set(added)):
        hs=hangul_segments.findall(s)
        if hs:
            new=[x for x in hs if x not in core_segs]
            print(f"    NEWSEG={new} :: {s!r}")
    print("  REMOVED with Hangul:")
    for s in sorted(set(removed)):
        hs=hangul_segments.findall(s)
        if hs:
            print(f"    :: {s!r} segs={hs}")
    # added strings with NO hangul but with CJK: sample count
    print(f"  added no-hangul count {sum(1 for s in set(added) if not hangul_segments.search(s))}, added pure-JA/CJK strings sample:")
    for s in sorted(set(added))[:5]:
        pass
