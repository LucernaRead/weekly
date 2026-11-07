import re, sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from occlusion_audit import ink_box
raw = open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-nl/svg/p6-politique.svg"), encoding="utf-8").read()
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
rects = [(float(a), float(b), float(a)+float(c), float(b)+float(d))
         for a, b, c, d, f in re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]*)"', raw) if f != "none"]
chart = []
for m in ATTR.finditer(raw):
    x, y = float(m.group(1)), float(m.group(2))
    if 1330 <= y <= 1800 and 65 <= x <= 961:
        bold = 'font-weight="700"' in m.group(5)
        am = re.search(r'text-anchor="([^"]*)"', m.group(5))
        chart.append(dict(x=x, y=y, fam=m.group(3), size=float(m.group(4)), bold=bold,
                          anchor=am.group(1) if am else "start", s=m.group(6)))
print(f"chart texts found: {len(chart)}")
maxcov = 0.0
for e in chart:
    ib = ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])
    l, t, r, b = ib
    area = max(0.0, (r-l)*(b-t))
    if area == 0: continue
    cov = 0.0
    for (rl, rt, rr, rb) in rects:
        if abs(rl-65) < 1 and abs(rt-1330) < 1: continue  # chart's own box (drawn before texts)
        ow = max(0.0, min(r, rr)-max(l, rl)); oh = max(0.0, min(b, rb)-max(t, rt))
        cov = max(cov, ow*oh/area)
    maxcov = max(maxcov, cov)
    if cov > 0: print(f"  cov {cov:.1%}: {e['s'][:60]}")
print(f"max baseline-anchored chart-label coverage: {maxcov:.1%} (gate <30%)")
