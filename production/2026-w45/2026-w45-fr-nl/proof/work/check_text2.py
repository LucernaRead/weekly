import re, xml.etree.ElementTree as ET
from pathlib import Path
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
def texts(d):
    out={}
    for p in sorted(d.glob("*.svg")):
        t=ET.parse(p); ns=[]
        for el in t.iter():
            if el.tag.endswith('}text') or el.tag=='text':
                s=''.join(el.itertext())
                if s.strip(): ns.append(s)
        out[p.name]=(ns,' '.join(ns))
    return out
CORE=texts(BASE/"weekly-report-w45-fr-core/svg"); ED=texts(BASE/"weekly-report-w45-fr-nl/svg"); W43=texts(BASE/"weekly-report-fr-nl/svg")
for term in ["Nanterre","irais","irai","Q120","120."]:
    print(f"--- {term} ---")
    for pn,(ns,j) in ED.items():
        hits=[s for s in ns if term in s]
        if hits: print(pn, hits[:6], "joinedcount", j.count(term))
print("=== ED P7 nodes ===")
for s in ED["p7-langue.svg"][0]: print(repr(s))
print("=== CORE P7 nodes ===")
for s in CORE["p7-langue.svg"][0]: print(repr(s))
