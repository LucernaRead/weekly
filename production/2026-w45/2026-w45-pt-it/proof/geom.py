import re, html, json, os
from PIL import Image, ImageDraw, ImageFont
G=os.path.expanduser('~/workspace/goals/lucernaread-social-media-operations')
ED=f'{G}/files/weekly-report-w45-pt-it/svg'
SERIF='/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'; SERIFB='/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
SANS='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'; SANSB='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
IDX=2
def font(kind,bold,size):
    p={( 'serif',False):SERIF,('serif',True):SERIFB,('sans',False):SANS,('sans',True):SANSB}[(kind,bold)]
    return ImageFont.truetype(p,int(size) if float(size)==int(float(size)) else size,index=IDX) if False else ImageFont.truetype(p,round(float(size)),index=IDX)
DUMMY=Image.new('RGB',(10,10)); DR=ImageDraw.Draw(DUMMY)
TEXT_RE=re.compile(r'<text([^>]*)>(.*?)</text>',re.S); RECT_RE=re.compile(r'<rect([^>]*)/?>',re.S)
def attr(a,n,d=None):
    m=re.search(rf'{n}="([^"]+)"',a); return m.group(1) if m else d
def parse(path):
    s=open(path,encoding='utf-8').read(); texts=[]
    for attrs,body in TEXT_RE.findall(s):
        t=html.unescape(re.sub(r'<[^>]+>','',body))
        if not t.strip(): continue
        x=float(attr(attrs,'x','0')); y=float(attr(attrs,'y','0')); size=float(attr(attrs,'font-size','20'))
        fam=attr(attrs,'font-family','Noto Sans CJK SC'); bold=attr(attrs,'font-weight','') in ('700','bold')
        kind='serif' if 'Serif' in fam else 'sans'; anchor=attr(attrs,'text-anchor','start')
        f=font(kind,bold,size)
        anch={'start':'ls','middle':'ms','end':'rs'}.get(anchor,'ls')
        try: box=DR.textbbox((x,y),t,font=f,anchor=anch)
        except Exception: box=(x,y-size,x+f.getlength(t),y+size*0.3)
        adv=f.getlength(t)
        adv_r=x if anchor=='end' else (x+adv/2 if anchor=='middle' else x+adv)
        texts.append({'x':x,'y':y,'size':size,'anchor':anchor,'text':t,'ink':box,'adv_right':adv_r,'adv':adv})
    rects=[]
    for attrs in RECT_RE.findall(s):
        if 'stroke=' not in attrs: continue
        try: rects.append({'x':float(attr(attrs,'x','0')),'y':float(attr(attrs,'y','0')),'w':float(attr(attrs,'width','0')),'h':float(attr(attrs,'height','0')),'sw':float(attr(attrs,'stroke-width','1'))})
        except (TypeError,ValueError): pass
    # all rects (incl filled, for P7 preview box + P6 bars)
    allrects=[]
    for attrs in RECT_RE.findall(s):
        try: allrects.append({'x':float(attr(attrs,'x','0')),'y':float(attr(attrs,'y','0')),'w':float(attr(attrs,'width','0')),'h':float(attr(attrs,'height','0')),'fill':attr(attrs,'fill'),'sw':attr(attrs,'stroke-width')})
        except (TypeError,ValueError): pass
    return texts,rects,allrects,s
def ov(a,b): return a[0]<b[2] and b[0]<a[2] and a[1]<b[3] and b[1]<a[3]
out={'A':[],'B_ink_over':[],'B_adv_over':[],'C':[]}
for fn in sorted(os.listdir(ED)):
    if not fn.endswith('.svg'): continue
    texts,rects,allrects,s=parse(os.path.join(ED,fn))
    byg={}
    for t in texts: byg.setdefault(round(t['y'],2),[]).append(t)
    for y,ns in byg.items():
        ns=sorted(ns,key=lambda n:n['ink'][0])
        for a,b in zip(ns,ns[1:]):
            if ov(a['ink'],b['ink']): out['A'].append({'page':fn,'y':y,'a':a['text'][:60],'b':b['text'][:60],'a_ink':[round(v,1) for v in a['ink']],'b_ink':[round(v,1) for v in b['ink']]})
    for t in texts:
        for bound,name in ((1910,'inner'),(1922,'outer'),(1950,'edge')):
            if t['ink'][2]>bound: out['B_ink_over'].append({'page':fn,'bound':name,'text':t['text'][:70],'ink_right':round(t['ink'][2],2),'adv_right':round(t['adv_right'],2),'adv_over':round(t['adv_right']-bound,2)})
        if t['ink'][0]<28: out['B_ink_over'].append({'page':fn,'bound':'left','text':t['text'][:70],'ink_left':round(t['ink'][0],2)})
    for t in texts:
        ix0,iy0,ix1,iy1=t['ink']
        for r in rects:
            if r['w']<=0 or r['h']<=0: continue
            half=r['sw']/2+0.5
            for bx in (r['x'],r['x']+r['w']):
                if ix0<bx<ix1 and r['y']-half<=(iy0+iy1)/2<=r['y']+r['h']+half: out['C'].append({'page':fn,'border':f'v@{bx}','text':t['text'][:70],'ink':[round(v,1) for v in t['ink']]})
            for by in (r['y'],r['y']+r['h']):
                if iy0<by<iy1 and r['x']-half<=(ix0+ix1)/2<=r['x']+r['w']+half: out['C'].append({'page':fn,'border':f'h@{by}','text':t['text'][:70],'ink':[round(v,1) for v in t['ink']]})
print('COUNTS A/B_ink/B_adv-over/C:',len(out['A']),len(out['B_ink_over']),sum(1 for b in out['B_ink_over'] if b.get('adv_over',0)>0),len(out['C']))
print(json.dumps(out,ensure_ascii=False,indent=1)[:3000])
json.dump(out,open(f'{G}/hidden_files/w45/pt-it-proof/geom.json','w'),ensure_ascii=False,indent=1)
# P6 chart: baseline-anchored ink (ascent 24, descent 6, anchor ls) vs bar rects
texts,rects,allrects,s=parse(f'{ED}/p6-aprofundamento.svg')
print('--- P6 chart labels ---')
for t in texts:
    if t['text'] in ('portões abertos','espera','prova') or 'portões' in t['text']:
        print('label node:',t['x'],t['y'],t['size'],repr(t['text']),'ink',[round(v,1) for v in t['ink']],'adv',round(t['adv'],1))
print('--- P6 filled rects near chart (h=22) ---')
for r in allrects:
    if r['h']==22: print(r)
# baseline-anchored coverage: ink=(x, y-24, x+adv, y+6)
for t in texts:
    if t['text'] in ('portões abertos','espera','prova'):
        ix0,iy0,ix1,iy1=t['x'],t['y']-24,t['x']+t['adv'],t['y']+6
        for r in allrects:
            if r['h']==22 and abs(r['y']-(t['y']-18))<40 and r['x']>t['x']:
                ox=max(0,min(ix1,r['x']+r['w'])-max(ix0,r['x'])); oy=max(0,min(iy1,r['y']+r['h'])-max(iy0,r['y']))
                area=(ix1-ix0)*(iy1-iy0); print(f"  {t['text']!r} anchored-ink=[{ix0:.1f},{iy0:.1f},{ix1:.1f},{iy1:.1f}] bar={r} coverage={ox*oy/area*100:.2f}%")
# P7 Fix-2 geometry
texts7,rects7,allrects7,s7=parse(f'{ED}/p7-lingua.svg')
print('--- P7 preview box rects (dark fill, y~2400) ---')
for r in allrects7:
    if r['y']>2300: print(r)
print('--- P7 nodes y>1900 (quote area + readers corner + preview) ---')
for t in texts7:
    if t['y']>1900: print(f"  x={t['x']:.0f} y={t['y']:.1f} fs={t['size']} {t['text'][:110]!r}")
