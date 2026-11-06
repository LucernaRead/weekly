import re
from pathlib import Path
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
def badge(path):
    raw=path.read_text(encoding="utf-8")
    for m in ATTR.finditer(raw):
        if "TEKSTEN IN HET FRANS" in m.group(6) or "法语正文" in m.group(6) or "TEXTES" in m.group(6):
            print(f" {path.parent.name} badge x={m.group(1)} y={m.group(2)} fam={m.group(3)} fs={m.group(4)} rest={m.group(5)!r} s={m.group(6)!r}")
for label,p in [("ED",BASE/"weekly-report-w45-fr-nl/svg/p1-une.svg"),("W43",BASE/"weekly-report-fr-nl/svg/p1-une.svg"),("CORE",BASE/"weekly-report-w45-fr-core/svg/p1-une.svg")]:
    print(label); badge(p)
# P1 top band elements ED vs W43 vs CORE: y=92 lines + subtitle y=372? + strapline
for label,p in [("ED",BASE/"weekly-report-w45-fr-nl/svg/p1-une.svg"),("W43",BASE/"weekly-report-fr-nl/svg/p1-une.svg"),("CORE",BASE/"weekly-report-w45-fr-core/svg/p1-une.svg")]:
    raw=p.read_text(encoding="utf-8"); print(f"--- {label} P1 top ---")
    for m in ATTR.finditer(raw):
        y=float(m.group(2))
        if y in (92.0,372.0) or (300<=y<=600 and float(m.group(4))>=20):
            print(f"  y={y} x={m.group(1)} fs={m.group(4)} {m.group(6)[:90]!r}")
