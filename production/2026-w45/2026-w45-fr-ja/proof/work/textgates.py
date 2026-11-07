import xml.etree.ElementTree as ET, re, base64, hashlib
from collections import Counter
def texts(path):
    root=ET.parse(path).getroot()
    out=[]
    for el in root.iter():
        if el.tag.endswith('text'):
            out.append((float(el.get('x',0)), float(el.get('y',0)), el.get('font-size'), el.get('font-weight'), el.get('fill'), ''.join(el.itertext())))
    return out
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ja/svg/'
CO='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg/'
W43='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-fr-ja/svg/'
print('=== SMALL KANA line-start (explicit) ===')
small=set('ゃゅょぁぃぅぇぉっゎ')
for pg in ['p1-une.svg','p2-vie.svg','p3-culture.svg','p4-sport.svg','p5-jeunesse.svg','p6-politique.svg','p7-langue.svg','p8-exercices.svg']:
    for x,y,fs,fw,fill,t in texts(ED+pg):
        if t and t[0] in small: print(pg,y,repr(t[:40]))
print('(end small kana: none above = 0)')
print('=== BADGE 3-way ===')
for label,base in [('ED',ED),('CO',CO),('W43',W43)]:
    ts=texts(base+'p1-une.svg')
    for x,y,fs,fw,fill,t in ts:
        if '読者のための版' in t or '读者的版本' in t or '読者の版' in t:
            print(label,'badge x,y,size,weight,fill:',x,y,fs,fw,fill,repr(t))
print('=== FOOTER / PAGE LINE every page ===')
for pg in ['p1-une.svg','p2-vie.svg','p3-culture.svg','p4-sport.svg','p5-jeunesse.svg','p6-politique.svg','p7-langue.svg','p8-exercices.svg']:
    for label,base in [('ED',ED),('W43',W43)]:
        ts=texts(base+pg)
        foot=[t for x,y,fs,fw,fill,t in ts if y==2624]
        print(pg,label,foot)
print('=== GLOSS: split on middle dot per README #21, from rendered gloss lines ===')
# gloss lines: texts starting with '解説 — ' in ED, '译注｜' in CO
for label,base,prefix in [('ED',ED,'解説 — '),('CO',CO,'译注｜')]:
    tot=0
    for pg in ['p1-une.svg','p2-vie.svg','p3-culture.svg','p4-sport.svg','p5-jeunesse.svg','p6-politique.svg']:
        ts=texts(base+pg)
        # gloss call strings are wrapped across lines; count via build source instead below; here list gloss-start lines
        gl=[t for x,y,fs,fw,fill,t in ts if t.startswith(prefix)]
        print(label,pg,'gloss-start lines:',gl)
print('=== GLOSS from build source (gloss() call strings) ===')
import re as _re
for label,path in [('ED-core-transformed','/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-ja-proof/work/repro-build/content12.py'),('CO','/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-fr-build/content12.py')]:
    pass
# use repro-build (transformed) + core build content files: extract f.gloss("...") strings
def gloss_counts(builddir):
    counts={}
    for f in ['content12.py','content34.py','content56.py']:
        src=open(builddir+'/'+f,encoding='utf-8').read()
        for m in _re.finditer(r'\.gloss\("((?:[^"\\]|\\.)*)"\)', src):
            s=m.group(1)
            # page from file+order: approximate by counting in file order; instead return list
            counts.setdefault(f,[]).append(s)
    return counts
for label,bd in [('ED-repro','/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-ja-proof/work/repro-build'),('CO','/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-fr-build')]:
    gc=gloss_counts(bd)
    for f,ss in gc.items():
        print(label,f,'gloss calls:',[len(s.split('·')) for s in ss],'total items:',sum(len(s.split('·')) for s in ss))
print('=== P7 items: #1-#8 phrases + grammar bridges ===')
ts=texts(ED+'p7-langue.svg')
for x,y,fs,fw,fill,t in ts:
    if 'LES PHRASES DE LA SEMAINE' in t or t.startswith('文法｜') or '文法｜' in t: print('ED P7',y,repr(t))
ts=texts(CO+'p7-langue.svg')
for x,y,fs,fw,fill,t in ts:
    if 'LES PHRASES DE LA SEMAINE' in t or '语法点｜' in t: print('CO P7',y,repr(t))
print('=== P7 phrases section full text flow ===')
ts=texts(ED+'p7-langue.svg')
for x,y,fs,fw,fill,t in ts:
    if 1180<=y<=1830: print('ED P7 flow',y,repr(t))
print('=== P6 sync sentence ===')
for label,base in [('ED',ED),('CO',CO)]:
    ts=texts(base+'p6-politique.svg')
    for x,y,fs,fw,fill,t in ts:
        if 'bouger' in t or 'peut' in t and 'calendrier' in t: print(label,y,repr(t))
    # micro-drill keys: find 'peut' lines
    print(label,'peut-lines:',[t for x,y,fs,fw,fill,t in ts if t.strip()=='peut' or 'peut' in t][:10])
print('=== IMAGES ===')
for pg in ['p1-une.svg','p2-vie.svg','p3-culture.svg']:
    for label,base in [('ED',ED),('CO',CO)]:
        raw=open(base+pg,encoding='utf-8').read()
        imgs=_re.findall(r'<image[^>]*>', raw)
        print(pg,label,'n_images',len(imgs),[i[:200] for i in imgs])
        for m in _re.finditer(r'xlink:href="data:image/jpeg;base64,([^"]+)"', raw):
            b64=m.group(1); dec=base64.b64decode(b64)
            print('   b64sha',hashlib.sha256(b64.encode()).hexdigest()[:16],'jpegsha',hashlib.sha256(dec).hexdigest()[:16],'bytes',len(dec))
print('=== CREDITS ===')
for pg in ['p1-une.svg','p2-vie.svg','p3-culture.svg']:
    for label,base in [('ED',ED),('CO',CO)]:
        ts=texts(base+pg)
        for x,y,fs,fw,fill,t in ts:
            if 'domaine public' in t or 'Atget' in t or 'Hiroshige' in t or 'Blanco' in t or 'Flora' in t: print(pg,label,y,repr(t))
