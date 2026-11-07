import re, html, os, sys
sys.path.insert(0,'/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
from occlusion_audit import parse_svg, fnum
for label,base in [('core','/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg'),('ed','/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-en/svg')]:
    els,W,H=parse_svg(open(f'{base}/p6-razbor.svg',encoding='utf-8').read())
    # later-drawn rect overlapping any text ink?
    overlaps=[]
    texts=[e for e in els if e.kind=='text' and e.box]
    rects=[e for e in els if e.kind=='rect' and e.box]
    for t in texts:
        for r in rects:
            if r.idx>t.idx:
                l,tt=max(t.box[0],r.box[0]),max(t.box[1],r.box[1]); rr,bb=min(t.box[2],r.box[2]),min(t.box[3],r.box[3])
                if rr>l and bb>tt: overlaps.append((t.text[:40],r.idx,[round(v,1) for v in r.box]))
    print(label,'P6 later-rect overlaps text ink:',overlaps)
    # bar labels/values: texts containing 34/28/22/16 as standalone or with %
    s=open(f'{base}/p6-razbor.svg',encoding='utf-8').read()
    ts=[html.unescape(re.sub(r"<[^>]+>","",c)) for c in re.findall(r"<text[^>]*>(.*?)</text>",s,re.S)]
    print(label,'bar-value candidates:',[t for t in ts if t.strip() in ('34','28','22','16','34%','28%','22%','16%')])
    # print P6 texts mentioning numbers + chart note
    for t in ts:
        if '34' in t or '28' in t or '22' in t or '16' in t or 'Practice data' in t or 'УЧЕБНЫЕ ДАННЫЕ' in t or 'учебный опрос' in t or 'practice data' in t:
            print('   ',repr(t))
