import re, glob, os, html, collections
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def els_of(fn):
    s=open(fn,encoding="utf-8").read()
    out=[]
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>(.*?)</text>', s, re.S):
        t=html.unescape(re.sub(r"<[^>]+>","",m.group(3)))
        out.append((float(m.group(1)),float(m.group(2)),t))
    return out
for code in ["core","de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    tot=collections.Counter(); per=[]
    for fn in sorted(glob.glob(BASE+f"/files/weekly-report-w46-es-{code}/svg/*.svg")):
        els=els_of(fn)
        chips=[e for e in els if e[2].strip() in ("A2","B1","B2")]
        stems=[e for e in els if re.fullmatch(r"\d{1,3}\.", (e[2].strip() or ""))]
        c=collections.Counter()
        for sx,sy,st in stems:
            near=[ch for ch in chips if abs(ch[1]-sy)<6 and ch[0]<sx]
            assert near, (code, fn, st)
            c[near[-1][2].strip()]+=1
        per.append(dict(c)); tot.update(c)
    print(code, "paired-stem levels A2=",tot["A2"],"B1=",tot["B1"],"B2=",tot["B2"],"sum=",sum(tot.values()),"perpage=",per)
print("\n===== grouped items 25-28 / 52-55 / 141-144: context in core =====")
for fn, pat in [("p2-vida.svg",None),("p4-deporte.svg",None),("p8-ejercicios.svg",None)]:
    els=els_of(BASE+f"/files/weekly-report-w46-es-core/svg/{fn}")
    print("---",fn,"---")
    for x,y,t in els:
        print(f" y={y} :: {t[:150]}")
