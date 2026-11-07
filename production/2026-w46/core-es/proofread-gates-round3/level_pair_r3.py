import re, xml.etree.ElementTree as ET, pathlib, collections
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
NS="{http://www.w3.org/2000/svg}"
names=["p1-portada.svg","p2-vida.svg","p3-cultura.svg","p4-deporte.svg","p5-juventud.svg","p6-afondo.svg","p7-lengua.svg","p8-ejercicios.svg"]
for d,label in [(BASE/"weekly-report-w46-es-de","DE"),(BASE/"weekly-report-w46-es-core","CORE")]:
    lvl=collections.Counter(); unpaired=[]
    for nm in names:
        t=ET.parse(d/"svg"/nm)
        els=[(float(el.get("x")),float(el.get("y")),(el.text or "").strip()) for el in t.iter(NS+"text")]
        chips=[e for e in els if e[2] in ("A2","B1","B2")]
        stems=[e for e in els if re.fullmatch(r"\d+\.", e[2])]
        for sx,sy,snum in stems:
            cands=[c for c in chips if abs(c[1]-sy)<=2.5 and 0 < (sx-c[0]) <= 60]
            if len(cands)==1: lvl[cands[0][2]]+=1
            else: unpaired.append((nm,snum,cands))
    print(label, dict(lvl), "total paired:", sum(lvl.values()), "unpaired:", unpaired)
    # grouped section chips: chips NOT paired to a stem, near grouped headers
    print(label, "grouped addition: 25-28 A2, 52-55 B1, 141-144 B2 -> totals A2", lvl["A2"]+4, "B1", lvl["B1"]+4, "B2", lvl["B2"]+4)
