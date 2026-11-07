import xml.etree.ElementTree as ET, re
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
ed5=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p5-cheongnyeon.svg")
print("P5 D-12 hits:", [t for t in ed5 if 'D-12' in t or '12일' in t])
ed1=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p1-pyoji.svg")
print("P1 立冬 hits:", [t for t in ed1 if '입동' in t or '立冬' in t])
# P8 section ranges: walk P8 texts in order, track current section header
p8=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/p8-siheom.svg")
sec=None; ranges={}
for t in p8:
    m=re.match(r'^([A-H]) ·', t)
    if m: sec=m.group(1); ranges.setdefault(sec,[]); continue
    m2=re.match(r'^(\d+)\.', t.strip())
    if m2 and sec: ranges[sec].append(int(m2.group(1)))
for s,v in ranges.items(): print(f"section {s}: {min(v)}-{max(v)} n={len(v)}")
