import re, sys, collections
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
from occlusion_audit import ink_box
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
def texts(path):
    out = []
    for m in ATTR.finditer(open(path, encoding="utf-8").read()):
        attrs = m.group(5)
        bold = 'font-weight="700"' in attrs
        am = re.search(r'text-anchor="([^"]*)"', attrs)
        out.append(dict(x=float(m.group(1)), y=float(m.group(2)), fam=m.group(3),
                        size=float(m.group(4)), bold=bold,
                        anchor=am.group(1) if am else "start", s=m.group(6)))
    return out
def ink(e):
    try:
        b = ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"], e["y"], e["anchor"])
        return b if (isinstance(b, tuple) and len(b) == 4) else None
    except Exception:
        return None
ED = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-zh-tw/svg"
CO = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg"
PAGES = ["p1-une","p2-vie","p3-culture","p4-sport","p5-jeunesse","p6-politique","p7-langue","p8-exercices"]
print("== A. FULL same-baseline ink scan (every y, every page) ==")
for pg in PAGES:
    ts = texts(f"{ED}/{pg}.svg")
    rows = collections.defaultdict(list)
    for e in ts: rows[e["y"]].append(e)
    overlaps = []
    mingap = {}
    for y, row in sorted(rows.items()):
        row = sorted(row, key=lambda e: e["x"])
        for a, b in zip(row, row[1:]):
            ia, ib = ink(a), ink(b)
            if ia and ib:
                g = round(ib[0]-ia[2], 2)
                if g < 0: overlaps.append((y, g, a["s"][:40], b["s"][:40]))
    # furniture bands: P1 top y=92, footers y=2624 detail
    for y in (92.0, 2624.0):
        row = sorted([e for e in ts if e["y"]==y], key=lambda e: e["x"])
        gaps = []
        for a, b in zip(row, row[1:]):
            ia, ib = ink(a), ink(b)
            if ia and ib: gaps.append(round(ib[0]-ia[2],1))
        print(f"  {pg} y={y}: {len(row)} segs gaps={gaps}")
    print(f"  {pg}: baselines={len(rows)} OVERLAPS={len(overlaps)} {overlaps[:10]}")
print("== B. right-edge scan (>1885 adv or ink) edition vs core ==")
for pg in PAGES:
    for label, D in [("ED", ED), ("CO", CO)]:
        pass
    ed_flags, co_flags = [], []
    for label, D, acc in [("ED", ED, ed_flags), ("CO", CO, co_flags)]:
        for e in texts(f"{D}/{pg}.svg"):
            ib = ink(e)
            ir = ib[2] if ib else None
            # advance end
            try:
                from occlusion_audit import get_font
                f = get_font(e["fam"], e["size"], e["bold"])
                adv = f.getlength(e["s"])/100.0  # SCALE? check: ink_box divides by SCALE; verify below
            except Exception:
                adv = 0
            # use text_w-like: replicate via ink_box adv? simpler: report ink only + x+len-based adv from get_font without scale guess
            if ir is not None and ir > 1885:
                acc.append((round(e["y"],2), round(ir,3), e["s"][:70]))
    print(f"  {pg} ED ink>1885: {len(ed_flags)}")
    for fl in ed_flags: print(f"    ED {fl}")
    print(f"  {pg} CO ink>1885: {len(co_flags)}")
    for fl in co_flags: print(f"    CO {fl}")
print("== C. orphan scan (single-char>=19, closer-led, opener-ended) ==")
CJK = re.compile(r"[\u4e00-\u9fff]")
CLOSERS = set("。，、；：？！」』）)]")
OPENERS = set("（「『([")
for pg in PAGES:
    for label, D in [("ED", ED), ("CO", CO)]:
        flags = []
        for e in texts(f"{D}/{pg}.svg"):
            s = e["s"]
            cj = CJK.findall(s)
            if len(cj) == 1 and len(s.strip()) <= 3 and e["size"] >= 19:
                flags.append(("single-char", e["y"], s))
            if s[:1] in CLOSERS:
                flags.append(("closer-led", e["y"], s[:50]))
            if s[-1:] in OPENERS:
                flags.append(("opener-ended", e["y"], s[-50:]))
        print(f"  {pg} {label}: {len(flags)} flags")
        for fl in flags: print(f"    {label} {fl}")
print("== D. P6 later-rect coverage (all P6 texts) ==")
src6 = open(f"{ED}/p6-politique.svg", encoding="utf-8").read()
combo = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>|<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
ordered = []
for m in combo.finditer(src6):
    if m.group(1) is not None:
        ordered.append(("rect", float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))))
    else:
        attrs = m.group(9)
        ordered.append(("text", float(m.group(5)), float(m.group(6)), m.group(7), float(m.group(8)),
                        'font-weight="700"' in attrs,
                        (re.search(r'text-anchor="([^"]*)"', attrs).group(1) if 'text-anchor' in attrs else "start"),
                        m.group(10)))
worst = 0.0; worst_desc = None; nonzero = []
for i, el in enumerate(ordered):
    if el[0] != "text": continue
    _, x, y, fam, size, bold, anchor, s = el
    ib = ink_box(s, fam, size, bold, x, y, anchor)
    if not (isinstance(ib, tuple) and len(ib) == 4): continue
    l, t, r, b = ib
    area = max(0.0, (r-l)*(b-t))
    if area <= 0: continue
    for later in ordered[i+1:]:
        if later[0] != "rect": continue
        _, rx, ry, rw, rh = later
        ox = max(0.0, min(r, rx+rw)-max(l, rx)); oy = max(0.0, min(b, ry+rh)-max(t, ry))
        frac = (ox*oy)/area
        if frac > 0: nonzero.append((round(frac,4), s[:40], rx, ry, rw, rh))
        if frac > worst: worst, worst_desc = frac, (s[:40], rx, ry, rw, rh)
print(f"  worst={worst:.4f} {worst_desc} gate<0.30: {'PASS' if worst<0.30 else 'FAIL'}; nonzero coverages: {len(nonzero)} {sorted(nonzero, reverse=True)[:5]}")
print("== E. P8 keys-region line gaps 10-45 window ==")
p8 = texts(f"{ED}/p8-exercices.svg")
ys = sorted(set(e["y"] for e in p8 if e["y"] > 1600))
gaps = [round(b-a,2) for a,b in zip(ys, ys[1:])]
print(f"  n={len(gaps)} min={min(gaps)} max={max(gaps)} all-in-10-45={all(10<=g<=45 for g in gaps)}")
from collections import Counter
print(f"  gap histogram: {Counter(gaps).most_common(10)}")
