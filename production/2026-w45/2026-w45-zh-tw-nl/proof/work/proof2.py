# -*- coding: utf-8 -*-
"""Independent proof pass 2: same-baseline ink collisions, chart-label element
check, P7 letter-box geometry (edition + core), P7 B1 head edge, P7 col geometry."""
import re, os, html, importlib.util
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-zh-tw-nl/svg")
CORE = os.path.join(BASE, "files/weekly-report-w45-zhtw-core/svg")
spec = importlib.util.spec_from_file_location("oa", os.path.join(BASE, "tools/occlusion_audit.py"))
oa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oa)
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"([^>]*)>')

def parse(path):
    s = open(path, encoding="utf-8").read()
    els = []
    for m in TEXT_RE.finditer(s):
        x, y, attrs, t = float(m.group(1)), float(m.group(2)), m.group(3), html.unescape(m.group(4))
        fm = re.search(r'font-family="([^"]+)"', attrs)
        sm = re.search(r'font-size="([\d.]+)"', attrs)
        bold = 'font-weight="700"' in attrs or 'font-weight="bold"' in attrs
        anchor = "middle" if 'text-anchor="middle"' in attrs else ("end" if 'text-anchor="end"' in attrs else "start")
        fam = fm.group(1) if fm else ""
        size = float(sm.group(1)) if sm else 20.0
        box = oa.ink_box(t, fam, size, bold, x, y, anchor, 0.0)
        els.append({"x": x, "y": y, "t": t, "box": box, "size": size, "fam": fam, "bold": bold})
    return s, els

print("== same-baseline collisions (edition) ==")
nflag = 0
for fn in sorted(os.listdir(ED)):
    _, els = parse(os.path.join(ED, fn))
    byy = {}
    for e in els:
        byy.setdefault(e["y"], []).append(e)
    for y, group in byy.items():
        if len(group) < 2:
            continue
        group = sorted(group, key=lambda e: e["box"][0])
        for a, b in zip(group, group[1:]):
            gap = b["box"][0] - a["box"][2]
            if gap < 0:
                print(f"  COLLISION {fn} y={y}: {a['t'][:40]!r} vs {b['t'][:40]!r} gap={gap:.2f}")
                nflag += 1
print("  total:", nflag)

print("== chart-label element check (edition P4/P6) ==")
nflag2 = 0
for fn in ["p4-sport.svg", "p6-deep.svg"]:
    s, els = parse(os.path.join(ED, fn))
    items = []
    for m in TEXT_RE.finditer(s):
        items.append(("text", m.start()))
    for m in RECT_RE.finditer(s):
        items.append(("rect", m.start(), (float(m.group(1)), float(m.group(2)),
                                          float(m.group(1)) + float(m.group(3)),
                                          float(m.group(2)) + float(m.group(4)))))
    items.sort(key=lambda z: z[1])
    titer = iter(els)
    seq = []
    for it in items:
        if it[0] == "text":
            seq.append(("text", next(titer)))
        else:
            seq.append(("rect", it[2]))
    for i, (kind, obj) in enumerate(seq):
        if kind != "text":
            continue
        l, t, r, b = obj["box"]
        for kind2, rbox in seq[i + 1:]:
            if kind2 != "rect":
                continue
            rl, rt, rr, rb = rbox
            if l < rr and r > rl and t < rb and b > rt:
                if (rr - rl) == 60.0 and (rb - rt) == 30.0:
                    continue
                if (rr - rl) > 1800:
                    continue
                print(f"  OVERLAP {fn}: {obj['t'][:50]!r} ink {[round(v,1) for v in obj['box']]} vs rect {[round(v,1) for v in rbox]}")
                nflag2 += 1
print("  total:", nflag2)

def letterbox(d, label):
    s, els = parse(os.path.join(d, "p7-lang.svg"))
    # disclosure nodes: Dutch (edition) or English (core)
    disc = [e for e in els if ("Voorbeeldbrief" in e["t"] or "Stuur je brief" in e["t"] or
                                "Deferral notice" in e["t"] or "invitation stays open" in e["t"])]
    print(f"== P7 letter-box ({label}) ==")
    for e in disc:
        print(f"  node y={e['y']} size={e['size']} ink={[round(v,2) for v in e['box']]} text={e['t'][:90]}")
    # rects: find the bordered box containing the disclosure (col3 x~1451-1885)
    rects = [(float(m.group(1)), float(m.group(2)), float(m.group(1)) + float(m.group(3)),
              float(m.group(2)) + float(m.group(4))) for m in RECT_RE.finditer(s)]
    # candidate boxes: contain last disclosure ink center
    if disc:
        last = disc[-1]
        cx = (last["box"][0] + last["box"][2]) / 2
        cy = (last["box"][1] + last["box"][3]) / 2
        for r in rects:
            if r[0] <= cx <= r[2] and r[1] <= cy <= r[3] and (r[2] - r[0]) < 1000 and (r[3] - r[1]) < 1500:
                print(f"  containing rect: {[round(v,2) for v in r]} expanded-border bottom={r[3] + 0.7:.2f} "
                      f"last-line ink bottom={last['box'][3]:.2f} ink-center={(last['box'][1]+last['box'][3])/2:.2f} "
                      f"clearance below ink bottom={(r[3] + 0.7) - last['box'][3]:.2f}")
    # all col3 rects for context
    col3 = [r for r in rects if r[0] >= 1400 and (r[2] - r[0]) < 1000]
    print(f"  col3 rects: {[[round(v,1) for v in r] for r in col3]}")

letterbox(ED, "edition")
letterbox(CORE, "core")

print("== P7 heads (edition) ==")
_, els = parse(os.path.join(ED, "p7-lang.svg"))
for e in els:
    if e["t"].startswith(("A2 ·", "B1 ·", "B2 ·")) and e["size"] >= 20:
        print(f"  {e['t'][:60]} ink right={e['box'][2]:.1f} size={e['size']}")
print("== P7 teaser/footer geometry (edition) ==")
for e in els:
    if "VOL.3" in e["t"] or "Volgende week" in e["t"] or "下期預告" in e["t"]:
        print(f"  teaser node y={e['y']} ink bottom={e['box'][3]:.2f} text={e['t'][:80]}")
