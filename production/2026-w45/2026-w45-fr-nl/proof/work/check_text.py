import re, xml.etree.ElementTree as ET, json, sys, collections
from pathlib import Path
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
CORE=BASE/"weekly-report-w45-fr-core/svg"
ED=BASE/"weekly-report-w45-fr-nl/svg"
W43=BASE/"weekly-report-fr-nl/svg"
def texts(d):
    out={}
    for p in sorted(d.glob("*.svg")):
        t=ET.parse(p)
        ns=[]
        for el in t.iter():
            if el.tag.endswith('}text') or el.tag=='text':
                s=''.join(el.itertext())
                if s.strip(): ns.append(s)
        out[p.name]=(ns, ' '.join(ns))
    return out
C=texts(CORE); E=texts(ED); W=texts(W43)
def cnt(s,sub): return s.count(sub)
def show(label, val): print(f"{label}: {val}")
# joined per page + all
call=' '.join(v[1] for v in E.values()); ccall=' '.join(v[1] for v in C.values())
show("ED 40e count all", cnt(call,"40e")); show("ED 41e count all", cnt(call,"41e"))
show("CORE 40e", cnt(ccall,"40e")); show("CORE 41e", cnt(ccall,"41e"))
for name in ["p4-sport.svg"]:
    show("ED p4 joined has 41e edition", "41e édition en 2026 (40e anniversaire)" in E[name][1])
    show("CORE p4 joined has", "41e édition en 2026 (40e anniversaire)" in C[name][1])
    # per-node search
    print(" ED p4 nodes containing 41e:", [s for s in E[name][0] if "41e" in s or "40e" in s])
    print(" CORE p4 nodes containing 41e:", [s for s in C[name][0] if "41e" in s or "40e" in s])
checks={
 "Q120 stem": "Si j'étais libre dimanche, j'___ à Nanterre.",
 "Q120 opt irai": "irai", "Q120 opt irais": "irais", "Q120 opt vais": "vais",
 "P7 quote4 comparatif": "plus excitante ou plus frustrante",
 "P7 quote8 verbatim": "Les jeunes créateurs y rencontrent leur public, en vrai.",
 "P6 sync": "Ce calendrier peut encore bouger.",
 "badge NL": "TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS",
 "gloss prefix sample": "Uitleg — ",
 "P8 sep": "— PAGINA ",
 "footer left": "Le Lucerna · FRANS WEEKBLAD VOL.3 · TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS",
 "solicit": "Stuur je brief én je beste pagina-8-tekst in voor VOL.4!",
 "no real letters NL": "geen echte brieven",
 "no best VOL2": "geen beste VOL.2-pagina-8-tekst",
 "VOL4 defer": "beide volgen in VOL.4",
 "editor example marker": "Exemple de la rédaction",
 "not a reader letter": "ce texte n'est pas une lettre de lecteur",
 "arrow NL": "→ NL:", "arrow FR": "→ FR:",
 "135 NL key": "Een programma lezen is al Frankrijk begrijpen.",
 "136 NL stem": "Hij rent sneller dan zijn broer.",
 "137 NL stem": "De leerlingen zijn sinds 17 oktober op vakantie.",
 "138 NL stem": "Vanavond gaan we onze schooltassen klaarmaken.",
 "139 NL stem": "Men kent de finalisten nog niet.",
 "150 NL key": "Open opdracht",
 "Q106 error": "rencontre", "Q106 key context": "rencontrent",
}
for k,v in checks.items():
    # page breakdown
    pages=[pn for pn,(ns,j) in E.items() if v in j]
    print(f"CHECK {k!r} -> pages {pages} count_all={cnt(call,v)}")
# CJK in edition nodes
import unicodedata
def cjk(s): return [ch for ch in s if '\u4e00'<=ch<='\u9fff' or '\u3040'<=ch<='\u30ff' or '\uac00'<=ch<='\ud7af']
for pn,(ns,j) in E.items():
    print(f"CJK {pn}: {len(cjk(j))}")
for pn,(ns,j) in C.items():
    print(f"CORE CJK {pn}: {len(cjk(j))}")
# Q119/Q121 P8 lines: dump P8 nodes containing 119/121
for n in ["119","120","121"]:
    print(f"--- P8 ED nodes with {n}. ---")
    for s in E["p8-exercices.svg"][0]:
        if re.search(rf"(^|\s){n}\.", s): print("  ",repr(s[:300]))
    print(f"--- P8 CORE nodes with {n}. ---")
    for s in C["p8-exercices.svg"][0]:
        if re.search(rf"(^|\s){n}\.", s): print("  ",repr(s[:300]))
# P8 135-139,150 printed lines ED vs CORE
for n in [135,136,137,138,139,150,106]:
    print(f"=== item {n} ED ===")
    for s in E["p8-exercices.svg"][0]:
        if re.search(rf"(^|\s){n}\.", s): print("  ",repr(s[:400]))
    print(f"=== item {n} CORE ===")
    for s in C["p8-exercices.svg"][0]:
        if re.search(rf"(^|\s){n}\.", s): print("  ",repr(s[:400]))
# Q120 on P7? exercises pages: search all pages for stem fragments
for pn,(ns,j) in E.items():
    if "j'étais libre" in j or "j’" in j: print("libre page",pn)
    if "Si j" in j: print(" Si j page",pn,[s for s in ns if "Si j" in s][:3])
# footer per page
for pn,(ns,j) in E.items():
    foots=[s for s in ns if "Pagina" in s or "FRANS WEEKBLAD" in s]
    print(f"FOOTER {pn}: {foots}")
    footsW=[s for s in W[pn][0] if "Pagina" in s or "FRANS WEEKBLAD" in s] if pn in W else []
    print(f"  W43: {footsW}")
# badge geometry: raw svg regex for badge text element
for label,d in [("ED",ED),("W43",W),("CORE",CORE)]:
    svg=(d/"p1-une.svg").read_text(encoding="utf-8")
    for pat in ["TEKSTEN IN HET FRANS","法语周报"]:
        idx=svg.find(pat)
        if idx>=0:
            print(label, pat, repr(svg[max(0,idx-400):idx+len(pat)+50]))
# '桥接' search in delivery svg/abstract/kit + build code (later separate)
for label,d in [("ED",ED)]:
    for p in sorted(d.glob("*.svg")):
        t=p.read_text(encoding="utf-8")
        if "桥接" in t: print("QIAOJIE in",p.name)
print("ABSTRACT qiaojie:", "桥接" in (BASE/"weekly-report-w45-fr-nl/ABSTRACT.txt").read_text(encoding="utf-8"))
print("KIT qiaojie count:", (BASE/"weekly-report-w45-fr-nl/WEEKLY-KIT.md").read_text(encoding="utf-8").count("桥接"))
# gloss prefix occurrences
for pn,(ns,j) in E.items():
    print(f"GLOSSPREFIX {pn}: nodes starting Uitleg={sum(1 for s in ns if s.strip().startswith('Uitleg'))} total Uitleg nodes={sum(1 for s in ns if 'Uitleg' in s)}")
# P7 golden sentences: need list from core P7? dump P7 nodes ED
print("=== ED P7 all nodes ===")
for s in E["p7-langue.svg"][0]: print("  ",repr(s))
