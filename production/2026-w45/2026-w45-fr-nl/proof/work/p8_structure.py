import re, xml.etree.ElementTree as ET
from pathlib import Path
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
for label,path in [("ED",BASE/"weekly-report-w45-fr-nl/svg/p8-exercices.svg"),("CORE",BASE/"weekly-report-w45-fr-core/svg/p8-exercices.svg")]:
    t=ET.parse(path); rows=[]
    for el in t.iter():
        if el.tag.endswith('}text') or el.tag=='text':
            s=''.join(el.itertext()).strip()
            if not s: continue
            rows.append((float(el.get('y')), float(el.get('x')), el.get('font-size'), s))
    rows.sort()
    print(f"===== {label} P8: {len(rows)} texts, y range {rows[0][0]}..{rows[-1][0]}")
    # print last 40 by y and section heads
    for y,x,fs,s in rows:
        if re.search(r"^(A|B|C|D|E|F|G|H) ·|RÉPONSES|MODÈLE|— PAGINA|— 第", s):
            print(f"  HEAD y={y} x={x} fs={fs} {s!r}")
    print("  --- last 25 rows ---")
    for y,x,fs,s in rows[-25:]: print(f"  y={y} x={x} fs={fs} {s[:110]!r}")
    print("  --- rows with y in 1400-1600 (battery end zone) ---")
    for y,x,fs,s in rows:
        if 1400<=y<=1600: print(f"  y={y} x={x} fs={fs} {s[:110]!r}")
    # rects: find rect y/height that could be writing strip / modele box
    print("  --- rects y>1300 ---")
    for el in t.iter():
        if el.tag.endswith('}rect') or el.tag=='rect':
            try: y=float(el.get('y')); h=float(el.get('height'))
            except: continue
            if y>1300: print(f"  rect x={el.get('x')} y={y} w={el.get('width')} h={h} fill={el.get('fill')} stroke={el.get('stroke')}")
