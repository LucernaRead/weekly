import re, html, sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-de-zh-cn-build"))
import occlusion_audit as OA
from svglib import text_w
SVGDIR = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/de-fix-round4/scratch/build-strict/svg")
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
# show lines around the two former defect sites: all keys lines with y in windows
for a,t in keys:
    y=float(a["y"])
    if 2160<=y<=2240 or 2470<=y<=2560:
        x=float(a["x"]); adv=text_w(t,"sans",False,14.5); box=OA.ink_box(t,a.get("font-family","Noto Sans CJK SC"),14.5,False,x,y)
        print(f"  x={x} y={y} adv={adv:.1f} inkR={box[2]:.1f} :: {t!r}")
# kinsoku scans over all 8 strict pages
NO_START=set("。、，．！？：；）」』】}),.:;!?"); NO_END=set("（(［｛〈《「『")
hs=he=lone=0
for pg in ["p1-front.svg","p2-leben.svg","p3-kultur.svg","p4-sport.svg","p5-jugend.svg","p6-vertiefung.svg","p7-sprache.svg","p8-uebungen.svg"]:
    for a,t in elements(os.path.join(SVGDIR,pg)):
        if t and t[0] in NO_START: hs+=1; print("START-HIT",pg,a["y"],repr(t[:50]))
        if t and t[-1] in NO_END: he+=1; print("END-HIT",pg,a["y"],repr(t[:50]))
        if t in ("。","）",".","，","、","！","？",")"): lone+=1; print("LONE",pg,repr(t))
print(f"kinsoku start={hs} end={he} lone={lone}")
# 76. + repairs present
p8txt=" ".join(t for _,t in els)
for tok in ["76. Die Kinder freuen sich, weil St. Martin kommt.","begonnen）","beginnt.（beginnt置尾）","das NFL-Spiel.","· 16.","· 24.","· 129.","sNFL"]:
    print(f"token {tok!r}: {'PRESENT' if tok in p8txt else 'ABSENT'} count={p8txt.count(tok)}")
