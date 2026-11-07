import re
from pathlib import Path
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
for label,path in [("ED",BASE/"weekly-report-w45-fr-nl/svg/p4-sport.svg"),("CORE",BASE/"weekly-report-w45-fr-core/svg/p4-sport.svg")]:
    raw=path.read_text(encoding="utf-8"); rows=[]
    for m in ATTR.finditer(raw):
        rows.append((float(m.group(2)),float(m.group(1)),m.group(3),float(m.group(4)),m.group(6)))
    print(f"===== {label} P4 y 780-1000 =====")
    for y,x,fam,fs,s in sorted(rows):
        if 780<=y<=1000: print(f" y={y} x={x} fs={fs} fam={fam} {s!r}")
