import re, json, html, os, glob
from collections import Counter
G=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE=f"{G}/files/weekly-report-w45-de-core/svg"
ED=f"{G}/files/weekly-report-w45-de-es/svg"
W43=f"{G}/files/weekly-report-de-es/svg"
TEXT_RE=re.compile(r"<text[^>]*>(.*?)</text>",re.S)
def texts(p):
    s=open(p,encoding="utf-8").read()
    return [re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>","",c))).strip() for c in TEXT_RE.findall(s)]
def alltexts(d):
    out={}
    for f in sorted(glob.glob(d+"/*.svg")): out[os.path.basename(f)]=texts(f)
    return out
core=alltexts(CORE); ed=alltexts(ED)
print("== CJK / forbidden ==")
CJK=re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
for name,ts in ed.items():
    cjk="".join(t for t in ts if CJK.search(t))
    print(name, "CJK chars in texts:", len(CJK.findall(" ".join(ts))), "bridge:", sum(t.count("桥接") for t in ts), "译注:", sum(t.count("译注") for t in ts), "｜:", sum(t.count("｜") for t in ts))
print("== freeze multiset per page ==")
for name in sorted(core):
    cc,ec=Counter(core[name]),Counter(ed[name])
    added=list((ec-cc).elements()); removed=list((cc-ec).elements())
    print(f"\n--- {name} +{len(added)} -{len(removed)}")
    print(" REMOVED:", removed)
    print(" ADDED:", added)
print("\n== P8 keys via p8 json ==")
d=json.load(open(f"{G}/hidden_files/w45/de-es-proof/p8-compare.json"))
# p8.py json may not include keys; extract separately below
