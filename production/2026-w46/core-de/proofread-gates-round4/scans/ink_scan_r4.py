#!/usr/bin/env python3
"""Round 4 independent TRUE-INK scan of ALL P8 keys lines (14.5pt, 100 lines).
Uses canonical tools/occlusion_audit.ink_box (PIL/FreeType getbbox at 4x).
Columns: x starts 65/527/989/1451, width 434 -> right edges 499/961/1423/1885.
Writes JSON + text report. Read-only on edition files."""
import re, html, pathlib, json, sys
sys.path.insert(0, str(pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
SVG = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-zh-cn/svg/p8-uebungen.svg"
s = SVG.read_text(encoding="utf-8")
els=[]
for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, re.S):
    a=dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
    t=html.unescape(re.sub(r"<[^>]+>","",m.group(2)))
    if a.get('font-size')=='14.5':
        els.append(dict(x=float(a['x']), y=float(a['y']), family=a.get('font-family',''),
                        bold=a.get('font-weight','') in ('700','bold'), text=t))
COLS=[(65,499),(527,961),(989,1423),(1451,1885)]
rows=[]
for i,e in enumerate(els):
    box=OA.ink_box(e['text'], e['family'], 14.5, e['bold'], e['x'], e['y'], anchor='start')
    col=None; edge=None
    for ci,(sx,ex) in enumerate(COLS):
        if abs(e['x']-sx)<0.01: col=ci+1; edge=ex
    assert col is not None, e
    ink_w=box[2]-box[0]
    rows.append(dict(idx=i, col=col, x=e['x'], y=round(e['y'],2), ink_left=round(box[0],2),
        ink_right=round(box[2],2), ink_top=round(box[1],2), ink_bottom=round(box[3],2),
        ink_width=round(ink_w,2), col_edge=edge, clearance=round(edge-box[2],2),
        overflow=round(box[2]-edge,2), text=e['text']))
outdir=pathlib.Path(__file__).resolve().parent.parent
(outdir/"scans/ink-scan-r4.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"keys lines: {len(rows)}")
for c in range(1,5):
    cr=[r for r in rows if r['col']==c]
    print(f"col-{c}: n={len(cr)} max_ink_width={max(r['ink_width'] for r in cr):.2f} max_ink_right={max(r['ink_right'] for r in cr):.2f} min_clearance={min(r['clearance'] for r in cr):.2f} overflowing={sum(1 for r in cr if r['overflow']>0)}")
print(f"OVERALL overflowing lines: {sum(1 for r in rows if r['overflow']>0)}")
print("worst 5 by clearance:")
for r in sorted(rows, key=lambda r: r['clearance'])[:5]:
    print(f"  col-{r['col']} y={r['y']} clearance={r['clearance']} inkR={r['ink_right']} w={r['ink_width']} :: {r['text'][:80]!r}")
print("defect sites:")
for r in rows:
    if r['y'] in (2198.02, 2193.96, 2523.12, 2527.18, 2541.97, 2216.87) or 'Falsch' in r['text'] and r['y']>2500:
        print(f"  col-{r['col']} y={r['y']} ink={r['ink_left']},{r['ink_top']},{r['ink_right']},{r['ink_bottom']} :: {r['text']!r}")
print(f"last keys baseline max y={max(r['y'] for r in rows)} max ink bottom={max(r['ink_bottom'] for r in rows)}")
# also check: any 14.5 line ink overlapping neighbour column start?
for r in rows:
    nxt = COLS[r['col']][0] if r['col']<4 else None
    if nxt is not None and r['ink_right']>nxt: print("CROSSES NEXT COL START:", r)
