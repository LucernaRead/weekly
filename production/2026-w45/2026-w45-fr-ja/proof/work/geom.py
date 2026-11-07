import sys, os, re
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as oa
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ja/svg/'
CO='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg/'
W43='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-fr-ja/svg/'
def load(base, pg):
    els,W,H=oa.parse_svg(open(base+pg,encoding='utf-8').read())
    return els
pages=['p1-une.svg','p2-vie.svg','p3-culture.svg','p4-sport.svg','p5-jeunesse.svg','p6-politique.svg','p7-langue.svg','p8-exercices.svg']
print('=== RIGHT EDGE >1885 (text ink right) ===')
for pg in pages:
    for label,base in [('ED',ED),('CO',CO)]:
        els=load(base,pg)
        over=[(round(e.box[2],1), round(e.baseline,1), e.text[:60]) for e in els if e.kind=='text' and e.box and e.box[2]>1885]
        print(pg,label,'n=',len(over), over)
print('=== MAX BASELINE / MAX INK BOTTOM per page ===')
for pg in pages:
    for label,base in [('ED',ED),('CO',CO)]:
        els=load(base,pg); ts=[e for e in els if e.kind=='text' and e.box]
        mb=max(e.baseline for e in ts); mib=max(e.box[3] for e in ts)
        print(pg,label,'max_baseline',mb,'max_ink_bottom',round(mib,1))
print('=== P8 detail: groups by y ===')
els=load(ED,'p8-exercices.svg')
for e in els:
    if e.kind=='text' and e.box:
        print('P8-ED', round(e.baseline,1), 'ink', [round(v,1) for v in e.box], repr(e.text[:70]))
