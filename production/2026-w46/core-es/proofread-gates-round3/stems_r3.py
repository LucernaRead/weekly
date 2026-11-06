import re, pathlib
p=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-core/2026-w46-es-core.text.md"
lines=[l.rstrip("\n") for l in p.read_text(encoding="utf-8").splitlines()]
# sections by ##
secs=[]; cur=None
for l in lines:
    if l.startswith("## "):
        cur=[l[3:],[]]; secs.append(cur)
    elif cur is not None:
        cur[1].append(l)
for name,ls in secs:
    # join non-empty lines with space, keep markers
    flow=" ".join(x.strip() for x in ls if x.strip())
    flow=re.sub(r"\s+"," ",flow)
    print(f"\n########## {name} ##########")
    print(flow[:6000])
