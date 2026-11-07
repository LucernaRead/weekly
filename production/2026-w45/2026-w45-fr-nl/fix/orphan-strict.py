import re, os
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
PUNCT = set(".,;:!?%)]}")
PAGES = ["p1-une","p2-vie","p3-culture","p4-sport","p5-jeunesse","p6-politique","p7-langue","p8-exercices"]
def scan(d):
    flags = []  # (page, y, kind, text)
    for pg in PAGES:
        ts = []
        for m in ATTR.finditer(open(os.path.join(d, pg+".svg"), encoding="utf-8").read()):
            ts.append(dict(x=float(m.group(1)), y=float(m.group(2)), fam=m.group(3), size=float(m.group(4)), s=m.group(6)))
        ts.sort(key=lambda e: (round(e["x"],1), e["y"]))
        blocks, cur = [], []
        for e in ts:
            if cur and (round(e["x"],1) != round(cur[-1]["x"],1) or e["size"] != cur[-1]["size"] or e["fam"] != cur[-1]["fam"] or not (10 <= e["y"]-cur[-1]["y"] <= 45)):
                blocks.append(cur); cur = []
            cur.append(e)
        if cur: blocks.append(cur)
        for bl in blocks:
            if len(bl) < 2: continue
            for i, e in enumerate(bl):
                s0 = e["s"].lstrip()
                if s0 and s0[0] in PUNCT:
                    flags.append((pg, e["y"], "LINE-START-PUNCT@%d/%d" % (i+1, len(bl)), e["s"][:70]))
            lt = bl[-1]["s"].strip()
            if len(lt.split()) == 1 and len(lt) <= 3:
                flags.append((pg, bl[-1]["y"], "SHORT-FINAL", repr(lt)))
    return flags
G = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ed = scan(os.path.join(G, "hidden_files/w45/fr-nl-fix/render/svg"))
co = scan(os.path.join(G, "files/weekly-report-w45-fr-core/svg"))
print("=== EDITION strict flags:", len(ed))
for f in ed: print("  ED", f)
print("=== CORE strict flags:", len(co))
for f in co: print("  CO", f)
edset = {(p, round(y,2), t) for p,y,k,t in ed}
coset = {(p, round(y,2), t) for p,y,k,t in co}
new = [f for f in ed if (f[0], round(f[1],2), f[3]) not in coset]
print("=== EDITION flags NOT in core (by page/y/text):", len(new))
for f in new: print("  NEW", f)
# P4 cheer box lines explicitly
import re as _re
raw = open(os.path.join(G, "hidden_files/w45/fr-nl-fix/render/svg/p4-sport.svg"), encoding="utf-8").read()
for m in ATTR.finditer(raw):
    if float(m.group(1)) == 1007.0 and 880 <= float(m.group(2)) <= 1060:
        print(f"  P4BOX y={m.group(2)} {m.group(6)!r}")
