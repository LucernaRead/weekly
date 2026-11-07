import re
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg"
CO="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg"
def nodes(p):
    s=open(p,encoding="utf-8").read()
    out=[]
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>", s, re.S):
        attrs=dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        txt=re.sub(r"<[^>]+>","",m.group(2))
        out.append((attrs,txt))
    return s,out
# P7 geometry: max y of col3 area? builder: col3 ends 1706.6, teaser ends 2552.6. Find teaser nodes (VOL.3 teaser) and footer line y=2580
s,ns=nodes(ED+"/p7-ciyu.svg")
print("P7 all y max:", max(float(a.get("y",0)) for a,t in ns))
# teaser: nodes after '下期预告'
idx=[i for i,(a,t) in enumerate(ns) if "下期预告" in t]
print("teaser head idx:",idx)
if idx:
    for a,t in ns[idx[0]:]: print("  P7-teaser:",a.get("y"),repr(t[:120]))
# P8 keys: max y of key lines
s8,ns8=nodes(ED+"/p8-ceyan.svg")
keys=[(float(a["y"]),t) for a,t in ns8 if re.match(r"^\d+\.\s",t.strip())]
print("P8 keys max baseline y:",max(y for y,t in keys),"n=",len(keys))
print("P8 last keys:",sorted(keys)[-3:])
s8c,ns8c=nodes(CO+"/p8-ceyan.svg")
keysc=[(float(a["y"]),t) for a,t in ns8c if re.match(r"^\d+\.\s",t.strip())]
print("CORE P8 keys max baseline y:",max(y for y,t in keysc),"n=",len(keysc))
# P7 clinic item 3
for a,t in ns:
    if "classificateur" in t or "毛衣" in t and "件" in t:
        print("P7 clinic:",a.get("y"),repr(t[:200]))
# Shopping occurrences in ED
for f in ["p1-touiban.svg","p2-shenghuo.svg","p7-ciyu.svg"]:
    ss,nn=nodes(ED+"/"+f)
    for a,t in nn:
        if "Shopping" in t or "shopping" in t: print(f,"SHOPPING:",repr(t[:200]))
# English-apparatus scan: common English function words in ED text (excluding Chinese text nodes & pinyin?)
import glob
for f in sorted(glob.glob(ED+"/*.svg")):
    ss=open(f,encoding="utf-8").read()
    ts=[re.sub(r"<[^>]+>","",m) for m in re.findall(r"<text[^>]*>(.*?)</text>", ss, re.S)]
    for t in ts:
        # flag lines that look like English sentences: contain ' the ' or ' and ' etc and mostly latin
        if re.search(r"\b(the|and|with|from|this|that|have|are|for)\b", t, re.I) and not re.search(r"[\u4e00-\u9fff]", t):
            print("ENG-SUSPECT",f.split("/")[-1],repr(t[:160]))
