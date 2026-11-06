import re
from collections import Counter
import xml.etree.ElementTree as ET, json
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
def hangul(s): return sum(1 for c in s if '\uAC00'<=c<='\uD7A4' or '\u1100'<=c<='\u11FF' or '\u3130'<=c<='\u318F')
def is_kana(c): return '\u3040'<=c<='\u30FF'
def is_han(c): return '\u4E00'<=c<='\u9FFF'
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
for i,p in enumerate(pages,1):
    cc, ec = Counter(texts(f"{BASE}/files/weekly-report-w45-ko-core/svg/{p}.svg")), Counter(texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg"))
    added=list((ec-cc).elements()); removed=list((cc-ec).elements())
    ha=sum(hangul(s) for s in added); hr=sum(hangul(s) for s in removed)
    print(f"p{i}: hangul added {ha} removed {hr} net {ha-hr}")
    # added strings with Han but NO kana and NO hangul -> pure Han strings (potential Chinese residue)
    pure=[s for s in set(added) if any(is_han(c) for c in s) and not any(is_kana(c) for c in s) and not hangul(s)]
    print(f"  added pure-Han (no kana, no hangul): {pure}")
    # removed strings that are pure Korean target (hangul + punctuation/digits only, no Han/kana/ASCII-letters beyond?)
    pureko=[]
    for s in set(removed):
        if hangul(s) and not any(is_han(c) or is_kana(c) for c in s):
            pureko.append(s)
    print(f"  removed pure-Hangul-only strings: {pureko}")
# builder freeze json vs mine
b=json.load(open(f"{BASE}/hidden_files/weekly-report-w45-ko-ja-build/freeze-diff.json"))
m=json.load(open(f"{BASE}/hidden_files/w45/ko-ja-proof/work/freeze-proof.json"))
print("builder pages:", {k:(len(v['added_strings']),len(v['removed_strings'])) for k,v in b['pages'].items()})
print("mine keys:", list(m.keys())[:5])
print(json.dumps(m, ensure_ascii=False)[:1500])
