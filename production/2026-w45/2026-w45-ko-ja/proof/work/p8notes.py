import xml.etree.ElementTree as ET, re
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
def hangul(s): return [c for c in s if '\uAC00'<=c<='\uD7A4']
ed=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p8-siheom.svg")
core=texts(f"{BASE}/files/weekly-report-w45-ko-core/svg/p8-siheom.svg")
# printed answer lines: start with N. and contain ' — '
def lines(ts):
    out={}
    for t in ts:
        m=re.match(r'^(\d+)\.\s*(.*)$', t.strip())
        if m and ' — ' in t: out[int(m.group(1))]=t.strip()
    return out
el, cl = lines(ed), lines(core)
print(f"edition dash-lines {len(el)} core dash-lines {len(cl)}")
print("--- edition notes containing Hangul (after ' — ') ---")
for n in sorted(el):
    note=el[n].split(' — ',1)[1]
    if hangul(note): print(f"{n}. NOTE={note!r}  FULL={el[n]!r}")
print("--- edition notes with NO kana and NO hangul (pure kanji/latin/digit notes) ---")
for n in sorted(el):
    note=el[n].split(' — ',1)[1]
    if not any('\u3040'<=c<='\u30FF' for c in note) and not hangul(note):
        print(f"{n}. NOTE={note!r} FULL={el[n]!r}")
print("--- edition notes identical to core note (residue check) ---")
for n in sorted(el):
    if n in cl:
        en=el[n].split(' — ',1)[1]; cn=cl[n].split(' — ',1)[1]
        if en==cn: print(f"{n}. SAME={en!r}")
print("--- 137/138/139/140 full ---")
for n in (137,138,139,140,109,81,99,150):
    print(f"ED {n}: {el.get(n)!r}")
    print(f"CO {n}: {cl.get(n)!r}")
# sections E: find P8 section headers
print("--- P8 headers ---")
for t in ed:
    if re.match(r'^[A-H] ·', t): print(repr(t))
