import re, html, sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-de-zh-cn-build"))
import occlusion_audit as OA
from svglib import text_w
SVGDIR = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-zh-cn/svg")
def elements(path):
    s = open(path, encoding="utf-8").read(); out=[]
    for m in re.finditer(r'<text[^>]*>(.*?)</text>', s, re.S):
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(0).split(">",1)[0]))
        out.append((attrs, html.unescape(re.sub(r"<[^>]+>","",m.group(1)))))
    return out
els = elements(os.path.join(SVGDIR,"p8-uebungen.svg"))
print("elements:", len(els))
COLX=[65,527,989,1451]
keys=[(a,t) for a,t in els if float(a.get("font-size","0"))==14.5]
print("keys lines:", len(keys))
bad=0; maxink={}
for a,t in keys:
    x=float(a["x"]); y=float(a["y"]); fam=a.get("font-family","Noto Sans CJK SC")
    adv=text_w(t,"sans",False,14.5); box=OA.ink_box(t,fam,14.5,False,x,y)
    edge=x+434; col=COLX.index(x)
    maxink[col]=max(maxink.get(col,0), box[2]-x)
    if adv>434 or box[2]>edge:
        bad+=1; print(f"OVER x={x} y={y} adv={adv:.1f} inkR={box[2]:.1f} edge={edge} :: {t[:70]!r}")
print("overflowing keys lines:", bad)
print("max ink width per col:", {k:round(v,1) for k,v in sorted(maxink.items())})
ys=[float(a["y"]) for a,t in keys]; print("keys baseline range:", min(ys), max(ys))
for a,t in keys:
    y=float(a["y"])
    if (abs(y-2198.02)<0.01 and float(a["x"])==65) or (abs(y-2523.12)<0.01 and float(a["x"])==527):
        x=float(a["x"]); adv=text_w(t,"sans",False,14.5); box=OA.ink_box(t,a.get("font-family","Noto Sans CJK SC"),14.5,False,x,y)
        print(f"FIXED-LINE x={x} y={y} adv={adv:.1f} ink={box} :: {t!r}")
print("sNFL occurrences in P8 SVG:", sum(t.count("sNFL") for _,t in els))
