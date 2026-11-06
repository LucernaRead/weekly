#!/usr/bin/env python3
"""Proof part 3: exercise expansion count + geometry supplements
(same-baseline ink, ADVANCE right-edge, P2 frozen line, P7 clearance,
P6 chart-label coverage, P8 flow end). Uses tools/occlusion_audit.py
measurement functions (shared tool, not a private fork)."""
import re, sys, xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
BASE = Path.home()/"workspace/goals/lucernaread-social-media-operations"
sys.path.insert(0, str(BASE/"tools"))
sys.path.insert(0, str(BASE/"tools/venv/lib/python3.12/site-packages"))
import occlusion_audit as OA
from PIL import ImageFont
ED = BASE/"files/weekly-report-w45-pt-nl/svg"
CO = BASE/"files/weekly-report-w45-pt-core/svg"
PAGES = ["p1-capa","p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento","p7-lingua","p8-avaliacao"]

def nodes(p):
    t=ET.parse(str(p)); out=[]
    for el in t.iter():
        tag=el.tag.split('}')[-1]
        if tag=='text':
            out.append({'x':float(el.get('x') or 0),'y':float(el.get('y') or 0),
                        'fs':float(el.get('font-size') or 20),'fam':el.get('font-family',''),
                        'bold':el.get('font-weight','') in ('700','bold'),
                        'anchor':el.get('text-anchor','start'),'txt':''.join(el.itertext())})
        elif tag in ('rect','line'):
            out.append({'shape':tag,'x':float(el.get('x') or 0),'y':float(el.get('y') or 0),
                        'w':float(el.get('width') or 0),'h':float(el.get('height') or 0),
                        'x1':float(el.get('x1') or 0),'y1':float(el.get('y1') or 0),
                        'x2':float(el.get('x2') or 0),'y2':float(el.get('y2') or 0)})
    return out

ed={pg:nodes(ED/f"{pg}.svg") for pg in PAGES}
co={pg:nodes(CO/f"{pg}.svg") for pg in PAGES}

print("== exercise expansion count (rendered number nodes) ==")
total={}; lvlcount=defaultdict(int); perpage={}
for pg in PAGES:
    els=[e for e in ed[pg] if 'txt' in e]
    nums=set(); lvls={}
    # badges: 19pt A2/B1/B2 nodes; number nodes: 24pt '^N.' or range '^N–M.'
    badges=[e for e in els if e['fs']==19 and e['txt'] in ('A2','B1','B2')]
    for e in els:
        m=re.match(r'^(\d+)\.\s', e['txt'])
        if m and e['fs'] in (24,):
            n=int(m.group(1))
            # level = nearest badge above-left within 60px x and 3px y
            cand=[b for b in badges if abs(b['y']-e['y'])<=3 and -60 <= (e['x']-b['x']) <= 120]
            lv=cand[0]['txt'] if cand else '?'
            nums.add(n); lvls[n]=lv
        m2=re.match(r'^(\d+)–(\d+)\.\s*$', e['txt'])
        if m2:
            cand=[b for b in badges if abs(b['y']-e['y'])<=3 and -60 <= (e['x']-b['x']) <= 120]
            lv=cand[0]['txt'] if cand else '?'
            for n in range(int(m2.group(1)), int(m2.group(2))+1):
                nums.add(n); lvls[n]=lv
    perpage[pg]=sorted(nums)
    for n,lv in lvls.items(): lvlcount[lv]+=1
    print(f"  {pg}: {len(nums)} items {sorted(nums)[:8]}...{sorted(nums)[-4:] if nums else []} levels_in_page={ {k: sum(1 for v in lvls.values() if v==k) for k in ('A2','B1','B2','?')} }")
allnums=set().union(*[set(v) for v in perpage.values()])
print(f"  union across P1-P7 pages (stem nodes): {len(allnums)} numbers {min(allnums)}..{max(allnums)} missing={sorted(set(range(1,151))-allnums)[:20]}")
print(f"  level totals from stem nodes: {dict(lvlcount)}")
# P8 stems: 24pt-ish nodes on P8 with ^N. patterns (exercises 113-150 section, before key area)
p8els=[e for e in ed['p8-avaliacao'] if 'txt' in e]
stems=[e for e in p8els if re.match(r'^(11[3-9]|12\d|13\d|14\d|150)\.', e['txt'])]
print(f"  P8 stem-like nodes (113-150, any font): {len(stems)}")
for e in stems[:6]: print(f"      {e['x']} {e['y']} fs={e['fs']} {e['txt'][:80]!r}")
# P8 key lines: 13pt nodes starting with number
keys=[e for e in p8els if e['fs']==13 and re.match(r'^\d+\.', e['txt'])]
print(f"  P8 key nodes fs=13: {len(keys)} first={keys[0]['txt'][:60]!r} last={keys[-1]['txt'][:60]!r} last_y={keys[-1]['y']}")
print(f"  P8 key node y range: {min(e['y'] for e in keys)}..{max(e['y'] for e in keys)} (footer rule 2580, footer baseline 2624)")

print("== same-baseline ink collisions (>1px x-overlap, all pages) ==")
tot_coll=0
for pg in PAGES:
    bybase=defaultdict(list)
    for e in ed[pg]:
        if 'txt' not in e or not e['txt'].strip(): continue
        box=OA.ink_box(e['txt'], e['fam'], e['fs'], e['bold'], e['x'], e['y'], e['anchor'])
        if box: bybase[round(e['y'],2)].append((box, e['txt']))
    coll=[]
    for y, items in bybase.items():
        items.sort(key=lambda t: t[0][0])
        for (b1,t1),(b2,t2) in zip(items, items[1:]):
            if b2[0] < b1[2]-1: coll.append((y,t1[:50],t2[:50],round(b1[2]-b2[0],1)))
    tot_coll+=len(coll)
    print(f"  {pg}: {len(coll)} collisions {coll[:4]}")
print(f"  TOTAL same-baseline collisions: {tot_coll}")

print("== ADVANCE right-edge scan (frames outer 28..1922, inner 40..1910) ==")
for pg in PAGES:
    mx=0; mx_txt=''; mn=9999
    for e in ed[pg]:
        if 'txt' not in e or not e['txt'].strip(): continue
        f=OA.get_font(e['fam'], e['fs'], e['bold'])
        adv=f.getlength(e['txt'])/OA.SCALE
        if e['anchor']=='middle': r=e['x']+adv/2; l=e['x']-adv/2
        elif e['anchor']=='end': r=e['x']; l=e['x']-adv
        else: r=e['x']+adv; l=e['x']
        if r>mx: mx, mx_txt=r, e['txt'][:80]
        if l<mn: mn=l
    print(f"  {pg}: max_adv_right={mx:.1f} min_adv_left={mn:.1f} worst={mx_txt!r} defects={mx>1910 or mn<40}")
print("  P2 frozen line (edition vs core):")
for name, d in [("edition", ed), ("core", co)]:
    for e in d['p2-vida']:
        if 'txt' in e and 'o objeto que dá luz' in e['txt']:
            f=OA.get_font(e['fam'], e['fs'], e['bold']); adv=f.getlength(e['txt'])/OA.SCALE
            print(f"    {name}: x={e['x']} y={e['y']} fs={e['fs']} adv_right={e['x']+adv:.1f} txt={e['txt']!r} inner_clearance={1910-(e['x']+adv):.1f}")

print("== P7 quote pitch + preview-box clearance ==")
p7=[e for e in ed['p7-lingua'] if 'txt' in e]
quotes=[e for e in p7 if e['txt'].startswith('«')]
trans=[e for e in p7 if '(Página' in e['txt'] and e['fs'] and e['fs']<22]
print(f"  quote head nodes: {len(quotes)}")
for q in quotes: print(f"    y={q['y']} {q['txt'][:60]!r}")
print(f"  translation nodes with (Página: {len(trans)}")
for t in trans: print(f"    y={t['y']} {t['txt'][:70]!r}")
rects=[e for e in ed['p7-lingua'] if e.get('shape')=='rect' and e['y']==2404]
print(f"  preview rects at y=2404: {rects}")
if trans and rects:
    last=max(trans, key=lambda e: e['y'])
    print(f"  LAST translation baseline={last['y']} clearance_to_box_top_2404={2404-last['y']:.2f}px txt={last['txt']!r}")
    pitches=[round(b['y']-a['y'],2) for a,b in zip(quotes, quotes[1:])]
    print(f"  quote-row pitches: {pitches}")

print("== P6 chart-label coverage (baseline-anchored ink vs later rects) ==")
p6=ed['p6-aprofundamento']
# rects in paint order with their index
seq=[]
for i,e in enumerate(p6):
    seq.append((i,e))
for lab in ['portões abertos','espera','prova','60 min','30 min','330 min']:
    for i,e in seq:
        if 'txt' in e and e['txt'].strip()==lab:
            f=OA.get_font(e['fam'], e['fs'], e['bold'])
            # baseline-anchored: getbbox anchor ls at (x, y)
            px=int(round(e['fs']*OA.SCALE)); font=ImageFont.truetype(*OA.resolve_font(e['fam'], e['fs'], e['bold'])[:1], size=px, index=OA.resolve_font(e['fam'], e['fs'], e['bold'])[1]) if False else None
            # use OA font + getbbox with anchor
            ff=OA.get_font(e['fam'], e['fs'], e['bold'])
            l,t,r,b=[v/OA.SCALE for v in ff.getbbox(e['txt'], anchor='ls')]
            # anchor ls: (x,y) is baseline-left; getbbox returns relative box
            box=(e['x']+l, e['y']+t, e['x']+r, e['y']+b)
            area=(box[2]-box[0])*(box[3]-box[1])
            cov=0.0
            for j,e2 in seq:
                if j<=i or e2.get('shape')!='rect': continue
                rx,ry,rw,rh=e2['x'],e2['y'],e2['w'],e2['h']
                ox=max(0,min(box[2],rx+rw)-max(box[0],rx)); oy=max(0,min(box[3],ry+rh)-max(box[1],ry))
                if area: cov=max(cov, ox*oy/area*100)
            print(f"  label {lab!r} at ({e['x']},{e['y']}) ink={tuple(round(v,1) for v in box)} coverage={cov:.1f}%")
print("  P6 bar rects present (w=90/45/495 check):")
for i,e in seq:
    if e.get('shape')=='rect' and e['w'] in (90.0,45.0,495.0): print(f"    rect w={e['w']} x={e['x']} y={e['y']} h={e['h']}")

print("== ink right-edge max per page (true ink) ==")
for pg in PAGES:
    mx=0; t=''
    for e in ed[pg]:
        if 'txt' not in e or not e['txt'].strip(): continue
        box=OA.ink_box(e['txt'], e['fam'], e['fs'], e['bold'], e['x'], e['y'], e['anchor'])
        if box and box[2]>mx: mx,t=box[2],e['txt'][:60]
    print(f"  {pg}: max_ink_right={mx:.1f} {t!r}")
