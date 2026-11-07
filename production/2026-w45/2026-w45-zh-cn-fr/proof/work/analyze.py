import re, glob, os, sys
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg"
CO="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg"
W43="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-fr/svg"
def texts(p):
    s=open(p,encoding="utf-8").read()
    return re.findall(r"<text[^>]*>(.*?)</text>", s, re.S), s
def clean(t): return re.sub(r"<[^>]+>","",t)
for label, d in [("ED",ED),("CORE",CO),("W43",W43)]:
    print("=====",label)
    for f in sorted(glob.glob(d+"/*.svg")):
        ts,s=texts(f)
        joined=" | ".join(clean(t) for t in ts)
        print(os.path.basename(f), "ntext=",len(ts))
    print()
# P1 badge/footer lines ED vs CORE vs W43
for label,d in [("ED",ED),("CORE",CO),("W43",W43)]:
    p=d+"/p1-touiban.svg"; ts,s=texts(p)
    print("--- P1",label)
    for t in ts:
        c=clean(t)
        if any(k in c for k in ["TEXTES","TEXTE","简体中文正文","HEBDOMADAIRE","简体中文版","Page ","第 ","给学中文"]):
            # extract y attr
            m=re.search(r'<text[^>]*y="([^"]*)"[^>]*>'+re.escape(t[:30]), s)
            print("   ",repr(c[:160]))
