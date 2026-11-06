import re, html, os, json, hashlib, base64
from collections import Counter
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg'
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-en/svg'
def raw(path): return open(path,encoding='utf-8').read()
def texts(path):
    s=raw(path)
    return [(m.group(1), html.unescape(re.sub(r"<[^>]+>","",m.group(2)))) for m in re.finditer(r"<text([^>]*)>(.*?)</text>",s,re.S)]
def attrs(a): return dict(re.findall(r'([\w-]+)="([^"]*)"',a))
# --- Images: extract <image ...> href/xlink + data? Check hrefs and compare embedded payloads
for label,d in [('core',CORE),('ed',ED)]:
    for fn in sorted(os.listdir(d)):
        s=raw(os.path.join(d,fn))
        imgs=re.findall(r"<image[^>]*>",s)
        if imgs: print(label,fn,imgs)
# image payload identity: compare whole <image> elements core vs ed per page
for fn in sorted(os.listdir(CORE)):
    ci=re.findall(r"<image[^>]*>",raw(os.path.join(CORE,fn)))
    ei=re.findall(r"<image[^>]*>",raw(os.path.join(ED,fn)))
    print(fn,'image elements identical:',ci==ei,'count',len(ci),len(ei))
    # if data-uri, hash payload
    for a,b in zip(ci,ei):
        print('   href core:',re.search(r'(?:href|xlink:href)="([^"]*)"',a).group(1)[:80] if re.search(r'(?:href|xlink:href)="([^"]*)"',a) else None)
        print('   href ed  :',re.search(r'(?:href|xlink:href)="([^"]*)"',b).group(1)[:80] if re.search(r'(?:href|xlink:href)="([^"]*)"',b) else None)
# --- Footers / top strip every page
for label,d in [('core',CORE),('ed',ED)]:
    print('== footers',label)
    for fn in sorted(os.listdir(d)):
        ts=texts(os.path.join(d,fn))
        foots=[t for a,t in ts if attrs(a).get('y')=='2624']
        print(' ',fn,foots)
# --- P8 separators
for label,d in [('core',CORE),('ed',ED)]:
    ts=texts(os.path.join(d,'p8-test.svg'))
    seps=[t for a,t in ts if 'СТРАНИЦА' in t]
    print(label,'P8 seps:',seps)
# --- gloss prefix in edition SVGs
for fn in sorted(os.listdir(ED)):
    ts=texts(os.path.join(ED,fn))
    notes=[t for a,t in ts if t.startswith('Note —')]
    if notes: print('gloss Note — in',fn,notes)
# --- P7 golden sentences: extract quoted sentences? KIT says 8; check core P7 phrases list vs articles: use builder verify scripts if present
