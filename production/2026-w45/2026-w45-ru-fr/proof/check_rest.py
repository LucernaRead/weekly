import re, pathlib, html, hashlib, sys, collections
sys.path.insert(0, str(pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-build"))
from svglib import text_w
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def raw(p): return p.read_text(encoding='utf-8')
def texts(p):
    s=raw(p)
    out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        out.append((m.group(1), html.unescape(re.sub(r'<[^>]+>','',m.group(2))).strip()))
    return out
# --- images ---
print("### images (data-URI / href payload sha256)")
for label,d in [('core','files/weekly-report-w45-ru-core/svg'),('ed','files/weekly-report-w45-ru-fr/svg')]:
    for pg in ['p1-pervaya.svg','p4-sport.svg','p5-molodezh.svg']:
        s=raw(base/d/pg)
        imgs=re.findall(r'(?:xlink:href|href)="([^"]+)"', s)
        hs=[hashlib.sha256(i.encode()).hexdigest()[:16] for i in imgs]
        print(f" {label} {pg} images={len(imgs)} sha16={hs} lens={[len(i) for i in imgs]}")
    for pg in ['p2-zhizn.svg','p3-kultura.svg','p6-razbor.svg','p7-yazyk.svg','p8-test.svg']:
        s=raw(base/d/pg)
        imgs=re.findall(r'(?:xlink:href|href)="([^"]+)"', s)
        print(f" {label} {pg} images={len(imgs)}")
# --- P7 golden sentences: quoted Russian strings in content7? use SVG joined text, count quoted segments ---
print("\n### P7 quoted sentences (space-joined page text, count occurrences)")
for label,d in [('core','files/weekly-report-w45-ru-core/svg'),('ed','files/weekly-report-w45-ru-fr/svg')]:
    ts=[t for _,t in texts(base/d/'p7-yazyk.svg')]
    joined=' '.join(ts)
    quotes=re.findall(r'«[^»]+»', joined)
    print(f" {label} quoted segments total={len(quotes)} counter={collections.Counter(quotes)}")
# --- P6 chart ---
print("\n### P6 chart labels/values + later-rect overlap (advance-width boxes)")
for label,d in [('core','files/weekly-report-w45-ru-core/svg'),('ed','files/weekly-report-w45-ru-fr/svg')]:
    s=raw(base/d/'p6-razbor.svg')
    els=[]
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>|<rect([^>]*)/>', s):
        if m.group(1) is not None:
            a=m.group(1); txt=m.group(2)
            def get(k):
                mm=re.search(rf'{k}="([^"]*)"', a); return mm.group(1) if mm else None
            x=float(get('x') or 0); y=float(get('y') or 0); sz=float(get('font-size') or 20)
            fam=get('font-family') or ''; bold='bold' in (get('font-weight') or '')
            kind='sans' if 'sans' in fam.lower() else 'serif'
            try: w=text_w(txt, kind, bold, sz)
            except Exception: w=len(txt)*sz*0.5
            anch=get('text-anchor') or 'start'
            x0=x-w if anch=='end' else (x-w/2 if anch=='middle' else x); x1=x if anch=='end' else (x+w/2 if anch=='middle' else x+w)
            els.append(('text',x0,y-sz,x1,y,txt))
        else:
            a=m.group(3)
            def get(k):
                mm=re.search(rf'{k}="([^"]*)"', a); return mm.group(1) if mm else None
            try: els.append(('rect',float(get('x') or 0),float(get('y') or 0),float(get('x') or 0)+float(get('width') or 0),float(get('y') or 0)+float(get('height') or 0),'' ))
            except Exception: pass
    labels=['Дома с семьёй','Короткая поездка','Ярмарка или концерт','Просто выспятся']
    vals=['34','28','22','16']
    for target in labels+vals:
        hits=[(i,e) for i,e in enumerate(els) if e[0]=='text' and e[5].strip()==target or (e[0]=='text' and target in e[5] and target in vals and False)]
        # exact for labels, and for values require standalone or "34 %" style: print all containing
        hits=[(i,e) for i,e in enumerate(els) if e[0]=='text' and (e[5].strip()==target)]
        for i,e in hits:
            ov=[]
            for j,f in enumerate(els):
                if j>i and f[0]=='rect' and not (f[3]<e[1] or f[1]>e[3] or f[4]<e[2] or f[2]>e[4]): ov.append((j,round(f[1],1),round(f[2],1),round(f[3],1),round(f[4],1)))
            print(f" {label} {target!r} idx={i} box=({e[1]:.1f},{e[2]:.1f},{e[3]:.1f},{e[4]:.1f}) later-rect-overlaps={ov}")
    # values as "34" may be part of "34%"? search containing
    for v in vals:
        cont=[e[5] for e in els if e[0]=='text' and v in e[5]]
        print(f" {label} value {v} containing-texts={cont}")
# --- same-baseline ink/advance scan: group by baseline y, gap <5px ---
print("\n### same-baseline advance-width gap scan (<5px)")
for label,d in [('core','files/weekly-report-w45-ru-core/svg'),('ed','files/weekly-report-w45-ru-fr/svg')]:
    for pg in sorted((base/d).glob('*.svg')):
        s=raw(pg); groups=collections.defaultdict(list)
        for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', s):
            a=m.group(1); txt=m.group(2)
            def get(k):
                mm=re.search(rf'{k}="([^"]*)"', a); return mm.group(1) if mm else None
            try: x=float(get('x') or 0); y=float(get('y') or 0); sz=float(get('font-size') or 20)
            except Exception: continue
            fam=get('font-family') or ''; bold='bold' in (get('font-weight') or '')
            kind='sans' if 'sans' in fam.lower() else 'serif'
            try: w=text_w(txt, kind, bold, sz)
            except Exception: w=len(txt)*sz*0.5
            anch=get('text-anchor') or 'start'
            x0=x-w if anch=='end' else (x-w/2 if anch=='middle' else x); x1=x if anch=='end' else (x+w/2 if anch=='middle' else x+w)
            groups[y].append((x0,x1,txt))
        flags=[]
        for y,lst in groups.items():
            lst=sorted(lst)
            for a,b in zip(lst,lst[1:]):
                if b[0]-a[1] < 5: flags.append((y,a[2][:25],b[2][:25],round(b[0]-a[1],1)))
        print(f" {label} {pg.name} flags={len(flags)} {flags[:4]}")
