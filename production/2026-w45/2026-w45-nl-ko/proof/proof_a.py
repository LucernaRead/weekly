import re, glob, collections, os
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg'
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ko/svg'
W43='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-ko/svg'
def texts(dire, fname):
    s=open(os.path.join(dire,fname),encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'<text\s+([^>]*)>([^<]*)</text>', s):
        out.append((m.group(1), m.group(2)))
    return out
def attr(attrs, name):
    m=re.search(name+r'="([^"]*)"', attrs)
    return m.group(1) if m else ''
def plain(dire, fname):
    return ''.join(t for _,t in texts(dire,fname))

print("=== A1: claimed Dutch phrases in edition ===")
checks=[('p5-jongeren.svg','Kijk zondag om 20:00 uur op RTL 4'),
 ('p7-taal.svg','een boom'),('p7-taal.svg','blijf ik thuis'),('p7-taal.svg','zij zette vast'),
 ('p7-taal.svg','«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.')]
for f, ph in checks:
    print(f, repr(ph), '->', ph in plain(ED,f))
print("P7 word-box sentence in CORE too:", '«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.' in plain(CORE,'p7-taal.svg'))
print()
print("=== A2: Latin-word loss audit: Latin tokens in core page text absent from edition page text ===")
LAT=re.compile(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'’\-]*")
for f in sorted(os.listdir(CORE)):
    ct=plain(CORE,f); et=plain(ED,f)
    cw=collections.Counter(LAT.findall(ct)); ew=set(LAT.findall(et))
    missing={w:c for w,c in cw.items() if w not in ew}
    # filter: single letters / roman numerals noise? print all
    print(f, 'missing Latin tokens:', missing)
print()
print("=== A3: Latin tokens in EDITION absent from CORE (new Dutch words) ===")
for f in sorted(os.listdir(CORE)):
    ct=plain(CORE,f); et=plain(ED,f)
    cw=set(LAT.findall(ct)); ew=collections.Counter(LAT.findall(et))
    new={w:c for w,c in ew.items() if w not in cw}
    print(f, 'new Latin tokens:', new)
print()
print("=== A4: P1 badge elements ===")
for dire,label in [(CORE,'CORE'),(ED,'ED'),(W43,'W43')]:
    for attrs,t in texts(dire,'p1-voorpagina.svg'):
        if '372' in attr(attrs,'y') or '네덜란드어 텍스트' in t or 'DE WEKELIJKSE KRANT' in t:
            print(label, 'y=',attr(attrs,'y'),'x=',attr(attrs,'x'),'size=',attr(attrs,'font-size'),'weight=',attr(attrs,'font-weight'),'family=',attr(attrs,'font-family'),'anchor=',attr(attrs,'text-anchor'),'fill=',attr(attrs,'fill'),'text=',repr(t))
print()
print("=== A5: gloss prefix lines ===")
for dire,label in [(CORE,'CORE'),(ED,'ED')]:
    print('--',label)
    for f in sorted(os.listdir(dire)):
        for attrs,t in texts(dire,f):
            if t.startswith('해설 — ') or t.startswith('译注｜'):
                print(' ',f,'y=',attr(attrs,'y'),'text=',repr(t))
print()
print("=== A6: footer VOL.2 ===")
for f in sorted(os.listdir(ED)):
    foots=[t for _,t in texts(ED,f) if 'VOL.2' in t]
    print(f, foots)
print()
print("=== A7: 桥接 count edition ===")
tot=0
for f in sorted(os.listdir(ED)):
    c=plain(ED,f).count('桥接'); tot+=c
    if c: print(f,c)
print('total 桥接 =',tot)
print()
print("=== A8: residual scripts in edition ===")
for f in sorted(os.listdir(ED)):
    t=plain(ED,f)
    han=sum(1 for c in t if 0x4E00<=ord(c)<=0x9FFF)
    cyr=sum(1 for c in t if 0x0400<=ord(c)<=0x04FF)
    kana=sum(1 for c in t if 0x3040<=ord(c)<=0x30FF)
    print(f,'hanzi=',han,'cyrillic=',cyr,'kana=',kana)
