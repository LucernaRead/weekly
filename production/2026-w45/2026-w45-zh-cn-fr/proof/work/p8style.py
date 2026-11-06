import re
def keys(p, n=8):
    s=open(p,encoding="utf-8").read()
    ts=[re.sub(r"<[^>]+>","",m) for m in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]
    # P8 keys area: lines starting with number.
    out=[]
    for t in ts:
        if re.match(r"^\d+\.\s", t.strip()) and ("—" in t or "(" in t):
            out.append(t.strip())
    return out
for label,p in [("ED","/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg/p8-ceyan.svg"),
("CORE","/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg/p8-ceyan.svg"),
("W43FR","/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-fr/svg/p8-ceyan.svg")]:
    ks=keys(p)
    print("=====",label,"key-like lines:",len(ks))
    for k in ks[:4]: print("   ",repr(k[:150]))
    for k in ks[-3:]: print("   ...",repr(k[:150]))
    dash=sum(1 for k in ks if " — " in k); paren=sum(1 for k in ks if re.search(r"\d+\.\s\S+ \(",k))
    print("   dash-count:",dash,"paren-count:",paren)
