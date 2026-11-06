import re, xml.etree.ElementTree as ET
from pathlib import Path
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
def nodes(d):
    out={}
    for p in sorted(d.glob("*.svg")):
        t=ET.parse(p); ns=[]
        for el in t.iter():
            if el.tag.endswith('}text') or el.tag=='text':
                s=''.join(el.itertext())
                if s.strip(): ns.append(s)
        out[p.name]=ns
    return out
ED=nodes(BASE/"weekly-report-w45-fr-nl/svg"); CORE=nodes(BASE/"weekly-report-w45-fr-core/svg")
def norm(s): return re.sub(r"\s+"," ",s.replace("’","'"))
tests=[
 ("#2","p1-une.svg",["On ne connaît pas encore","ne connaît pas encore les","finalistes"]),
 ("#5","p5-jeunesse.svg",["se promène dans Paris","festival se promène","promène"]),
 ("#7","p1-une.svg",["tout se joue","Ce week-end, tout se joue","se joue"]),
 ("#1","p2-vie.svg",["on reprend les cours"]),
 ("#3","p3-culture.svg",["se sont remplis de","chrysanthèmes"]),
 ("#4","p4-sport.svg",["plus excitante ou plus frustrante"]),
 ("#6","p6-politique.svg",["peut encore bouger"]),
 ("#8","p5-jeunesse.svg",["rencontrent leur public"]),
]
for num,pg,frags in tests:
    for label,D in [("ED",ED),("CORE",CORE)]:
        joined=norm(' '.join(D[pg]))
        print(num,pg,label,[(f, f in joined) for f in frags])
        if num in ("#2","#5","#7") and label=="ED":
            # print nodes containing key word
            print("   nodes:",[s for s in D[pg] if any(k in s for k in ["finalistes","promène","se joue","joue"])][:10])
