import re, glob, os, html, collections
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def els_of(fn):
    s=open(fn,encoding="utf-8").read()
    out=[]
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>(.*?)</text>', s, re.S):
        t=html.unescape(re.sub(r"<[^>]+>","",m.group(3)))
        out.append((float(m.group(1)),float(m.group(2)),t))
    return out
for code in ["core"]:
    print("===== CORE: stems without same-baseline level chip =====")
    for fn in sorted(glob.glob(BASE+f"/files/weekly-report-w46-es-{code}/svg/*.svg")):
        els=els_of(fn)
        chips=[e for e in els if e[2].strip() in ("A2","B1","B2")]
        stems=[e for e in els if re.fullmatch(r"\d{1,3}\.", e[2].strip() or "")]
        print(os.path.basename(fn), "stems:", len(stems), "chips:", len(chips))
        print("  stem numbers:", [e[2].strip() for e in stems])
        for sx,sy,st in stems:
            near=[c for c in chips if abs(c[1]-sy)<6 and c[0]<sx]
            if not near:
                # context: nearest text on same line
                ctx=" | ".join(e[2][:60] for e in els if abs(e[1]-sy)<6)
                print(f"  NO-CHIP stem {st} y={sy}: {ctx[:200]}")
