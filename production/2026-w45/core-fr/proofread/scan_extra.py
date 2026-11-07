# Independent supplement to occlusion_audit.py (read-only on shipped SVGs):
# (a) same-baseline text-ink collisions (FRxRU lesson: TEXTX misses same-line pairs)
# (b) graze scan: ANY ink overlap between a text node and a LATER-drawn opaque rect
#     (below the 30% COVER threshold), reported for adjudication, esp. chart pages.
import sys, glob, os, json
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as OA

base='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg'
same=[]; graze=[]
for f in sorted(glob.glob(base+'/*.svg')):
    page=os.path.basename(f)
    els,_,_=OA.parse_svg(open(f,encoding='utf-8').read())
    texts=[e for e in els if e.kind=='text']
    # (a) group by rounded baseline y; check x-overlap of ink boxes on same line
    by_y={}
    for e in texts:
        by_y.setdefault(round(e.baseline),[]).append(e)
    for y,grp in by_y.items():
        grp=sorted(grp,key=lambda e:e.box[0])
        for i in range(len(grp)):
            for j in range(i+1,len(grp)):
                a,b=grp[i],grp[j]
                ox=OA.overlap(a.box,b.box)
                if ox and ox[0]>0:
                    same.append((page,y,a.text[:40],b.text[:40],ox))
    # (b) text vs later opaque rect (any overlap area > 0)
    for i,e in enumerate(texts):
        for later in els:
            if later.idx<=e.idx: continue
            if later.kind!='rect': continue
            if not OA.is_opaque(later): continue
            ox=OA.overlap(e.box,later.box)
            if ox and ox[0]>0:
                graze.append((page,e.text[:50],ox))
    print(page, "texts:", len(texts))
print("\nSAME-BASELINE collisions:", len(same))
for s in same: print(s)
print("\nGRAZE (text vs later opaque rect, any overlap):", len(graze))
for g in graze[:60]: print(g)
with open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-core-proofread/scan-extra.json','w',encoding='utf-8') as o:
    json.dump({"same_baseline":[str(s) for s in same],"graze":[str(g) for g in graze]},o,ensure_ascii=False,indent=1)
