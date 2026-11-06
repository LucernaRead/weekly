import re, html, pathlib
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def texts(path):
    s=path.read_text(encoding='utf-8')
    out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        a=m.group(1); t=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        x=float(re.search(r'x="([\d.]+)"',a).group(1)); y=float(re.search(r'y="([\d.]+)"',a).group(1))
        out.append((x,y,t))
    return out
for pg,f in [('P2','p2-vida'),('P3','p3-cultura'),('P4','p4-deporte'),('P5','p5-juventud')]:
    for label,root in [('CORE','files/weekly-report-w45-es-core/svg'),('ED','files/weekly-report-w45-es-pt/svg')]:
        ts=texts(base/f"{root}/{f}.svg")
        # find Nota start indices
        starts=[i for i,(x,y,t) in enumerate(ts) if t.startswith('Nota —')]
        print(f"== {pg} {label} Nota starts: {starts}")
        for si in starts:
            # join this and following elements while they look like continuation: same-ish x? print next 6
            seg=[ts[si][2]]
            for j in range(si+1, min(si+7, len(ts))):
                seg.append(ts[j][2])
            print(f"   start y={ts[si][1]} :: {' | '.join(seg)}")
