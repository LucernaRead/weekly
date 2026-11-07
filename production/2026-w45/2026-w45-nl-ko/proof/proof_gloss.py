import re, os
CORE='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg'
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ko/svg'
def els(dire,f):
    s=open(dire+'/'+f,encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'<text\s+([^>]*)>([^<]*)</text>', s):
        a,t=m.group(1),m.group(2)
        x=re.search(r'x="([0-9.]+)"',a); y=re.search(r'y="([0-9.]+)"',a)
        if x and y: out.append((float(x.group(1)),float(y.group(1)),t))
    return sorted(out)
for dire,label,prefixes in [(CORE,'CORE',['讲解｜','译注｜']),(ED,'ED',['해설 — '])]:
    print('=====',label)
    for f in sorted(os.listdir(dire)):
        E=els(dire,f)
        for i,(x,y,t) in enumerate(E):
            if any(t.startswith(p) for p in prefixes):
                # follow same-x chain gap 20-35
                parts=[t]; j=i
                while j+1<len(E) and abs(E[j+1][0]-x)<=1 and 20<=E[j+1][1]-E[j][1]<=35:
                    # stop if next line starts a new gloss or is a header? gloss continuations don't start with prefix
                    parts.append(E[j+1][2]); j+=1
                joined=''.join(parts)
                for p in prefixes:
                    if joined.startswith(p): joined=joined[len(p):]
                items=[it.strip() for it in joined.split('·')]
                items=[it for it in items if it]
                print(f' {f} start-y={y} nlines={len(parts)} count={len(items)} items={items}')
