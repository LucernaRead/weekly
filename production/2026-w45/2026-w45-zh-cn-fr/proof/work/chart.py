import re
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg"
CO="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg"
for label,d in [("ED",ED),("CORE",CO)]:
    s=open(d+"/p6-shendu.svg",encoding="utf-8").read()
    print("=====",label)
    # rects with x=325
    for m in re.finditer(r"<rect([^>]*)/>", s):
        a=dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        if a.get("x")=="325":
            print("  bar rect:",a)
    # texts containing yuan values near chart: 270, 179, 160 with x attr
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>", s, re.S):
        t=re.sub(r"<[^>]+>","",m.group(2))
        a=dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        if re.search(r"^(270|179|160)\b", t.strip()) or t.strip() in ("270","179","160"):
            print("  label:",a.get("x"),a.get("y"),repr(t[:80]))
    # all rects drawn AFTER each label? check order: find positions of label texts and later rects overlapping label bbox roughly
    # simpler: list rects with y in chart band: print rects whose y between 1000-1400
    print("  rects y 900-1500:")
    for m in re.finditer(r"<rect([^>]*)/>", s):
        a=dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        try: y=float(a.get("y",0))
        except: continue
        if 900<=y<=1500: print("   ",a)
