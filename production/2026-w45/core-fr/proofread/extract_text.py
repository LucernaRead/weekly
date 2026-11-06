import re, glob, os, xml.etree.ElementTree as ET
NS={'s':'http://www.w3.org/2000/svg'}
base='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg'
for f in sorted(glob.glob(base+'/*.svg')):
    tree=ET.parse(f)
    root=tree.getroot()
    lines=[]
    for el in root.iter():
        tag=el.tag.split('}')[-1]
        if tag=='text':
            t=''.join(el.itertext()).strip()
            if t:
                lines.append((float(el.get('y',0)), float(el.get('x',0)), el.get('font-size','?'), t))
    lines.sort()
    out=os.path.basename(f).replace('.svg','.txt')
    with open(out,'w',encoding='utf-8') as o:
        for y,x,fs,t in lines:
            o.write(f"y={y:7.1f} x={x:7.1f} fs={fs:>6} | {t}\n")
    print(out, len(lines))
