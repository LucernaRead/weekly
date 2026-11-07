import sys, pathlib
sys.path.insert(0, str(pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
import xml.etree.ElementTree as ET, collections
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-de"
NS="{http://www.w3.org/2000/svg}"
names=["p1-portada.svg","p2-vida.svg","p3-cultura.svg","p4-deporte.svg","p5-juventud.svg","p6-afondo.svg","p7-lengua.svg","p8-ejercicios.svg"]
total_parsed=0; reports=[]; unparsed=0
for nm in names:
    t=ET.parse(BASE/"svg"/nm)
    els=[]
    for el in t.iter(NS+"text"):
        total_parsed+=1
        txt=el.text or ""
        if not txt:
            unparsed+=1; continue
        x=float(el.get("x")); y=float(el.get("y")); size=float(el.get("font-size"))
        bold=(el.get("font-weight") in ("700","bold"))
        fam=el.get("font-family","")
        anchor=el.get("text-anchor","start")
        try:
            box=OA.ink_box(txt, fam, size, bold, x, y, anchor)
        except Exception as e:
            unparsed+=1; continue
        els.append((y, box, txt))
    byg=collections.defaultdict(list)
    for y,box,txt in els: byg[y].append((box,txt))
    for y,group in byg.items():
        if len(group)<2: continue
        boxes=sorted(group, key=lambda g: g[0][0])
        for (b1,t1),(b2,t2) in zip(boxes,boxes[1:]):
            gap=b2[0]-b1[2]
            if gap<2.0:
                reports.append((nm,y,round(gap,2),t1,t2))
print(f"parsed <text>: {total_parsed}, skipped-empty/error: {unparsed}")
print(f"reports (gap<2px or overlap): {len(reports)}")
for r in reports: print(r)
