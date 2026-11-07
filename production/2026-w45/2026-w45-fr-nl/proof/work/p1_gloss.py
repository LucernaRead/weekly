import re
from pathlib import Path
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
for label,path in [("ED",BASE/"weekly-report-w45-fr-nl/svg/p1-une.svg"),("CORE",BASE/"weekly-report-w45-fr-core/svg/p1-une.svg")]:
    raw=path.read_text(encoding="utf-8"); rows=[]
    for m in ATTR.finditer(raw):
        rows.append((float(m.group(2)),float(m.group(1)),float(m.group(4)),m.group(6)))
    print(f"===== {label} P1 gloss box x=545 lines =====")
    for y,x,fs,s in sorted(rows):
        if x==545.0 and 1300<=y<=1500: print(f" y={y} fs={fs} {s!r}")
