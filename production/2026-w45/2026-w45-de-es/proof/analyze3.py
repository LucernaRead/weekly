import re, os
from collections import Counter
G=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED=f"{G}/files/weekly-report-w45-de-es/svg"; CORE=f"{G}/files/weekly-report-w45-de-core/svg"
import html
def texts(p):
    s=open(p,encoding="utf-8").read()
    return [re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>","",c))).strip() for c in re.findall(r"<text[^>]*>(.*?)</text>",s,re.S)]
def joined(p): return " ".join(texts(p))
print("== gloss precise: gloss sentence = Nota..first period, split by · ==")
for pg in ["p2-leben.svg","p3-kultur.svg","p4-sport.svg","p5-jugend.svg","p6-vertiefung.svg"]:
    j=joined(f"{ED}/{pg}"); i=j.find("Nota —"); sent=j[i:j.find(".",i)+1]
    parts=[x.strip() for x in sent.split("·")]
    print(pg, len(parts), parts)
    jc=joined(f"{CORE}/{pg}"); k=jc.find("译注｜"); sentc=jc[k:jc.find("。",k)+1] if k>=0 else ""
    print("  core gloss parts by · :", len([x.strip() for x in sentc.split("·")]) if sentc else "?", sentc[:120])
print("\n== P6 chart exact labels ==")
import xml.etree.ElementTree as ET
for label in ["familiares","servicio","residencia"]:
    s=open(f"{ED}/p6-vertiefung.svg",encoding="utf-8").read()
    ms=re.findall(r'<text[^>]*>'+re.escape(label)+r'</text>',s)
    print(label, ms)
for longlabel in ["familiares que cuidan","servicio profesional","en una residencia"]:
    s=open(f"{ED}/p6-vertiefung.svg",encoding="utf-8").read()
    print("long absent:", longlabel, longlabel not in s)
print("\n== P2 box4 / Rechnen line ==")
s=open(f"{ED}/p2-leben.svg",encoding="utf-8").read()
# find texts near y? print all text elements with y and content containing Rechnen or box4? dump elements around
for m in re.finditer(r'<text[^>]*x="([^"]+)"[^>]*y="([^"]+)"[^>]*>([^<]*)</text>',s):
    if "RECHNEN" in m.group(3) or "Rechnen" in m.group(3): print(m.groups())
# find lines/rects: print elements with y around 1554
for m in re.finditer(r'<(line|rect)[^>]*>',s):
    t=m.group(0)
    if "1554" in t or "1550" in t: print(t[:300])
print("\n== P8 font/size/keys endpoint: grep content8 ==")
c=open(f"{G}/hidden_files/weekly-report-w45-de-es-build/content8.py",encoding="utf-8").read()
for pat in ["12","1.22","gap","2113","2560"]:
    pass
# print lines mentioning font-size in p8 svg tail (keys area)
s8=open(f"{ED}/p8-uebungen.svg",encoding="utf-8").read()
sizes=Counter(re.findall(r'font-size="([^"]+)"',s8)); print("P8 font sizes:", sizes)
# last text elements y values
els=re.findall(r'<text[^>]*y="([^"]+)"[^>]*>([^<]{0,60})</text>',s8)
print("P8 max y text:", max(float(y) for y,_ in els), "last few:", els[-5:])
print("\n== P1 top elements ==")
s1=open(f"{ED}/p1-front.svg",encoding="utf-8").read()
for m in re.finditer(r'<text[^>]*x="([^"]+)"[^>]*y="([^"]+)"[^>]*>([^<]*)</text>',s1):
    if float(m.group(2))<450: print(m.groups())
