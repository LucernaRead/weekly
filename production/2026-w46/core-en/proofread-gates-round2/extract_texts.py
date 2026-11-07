#!/usr/bin/env python3
import re, sys
from pathlib import Path
TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
ATTR_RE = re.compile(r'(\w[\w-]*?)="([^"]*)"')
def texts_of(p):
    raw = Path(p).read_text(encoding='utf-8', errors='replace')
    out=[]
    for m in TEXT_RE.finditer(raw):
        attrs=dict(ATTR_RE.findall(m.group(1)))
        inner=re.sub(r'<[^>]+>','',m.group(2)).replace('&amp;','&').replace('&lt;','<').replace('&gt;','>').replace('&quot;','"').replace('&apos;',"'")
        out.append({'x':attrs.get('x'),'y':attrs.get('y'),'size':attrs.get('font-size'),'weight':attrs.get('font-weight'),'anchor':attrs.get('text-anchor'),'family':attrs.get('font-family'),'text':inner})
    return out
base=Path.home()/'workspace/goals/lucernaread-social-media-operations/files'
outdir=Path(sys.argv[1]); outdir.mkdir(parents=True,exist_ok=True)
for eddir in sorted(base.glob('weekly-report-w46-en-*')):
    ed=eddir.name.replace('weekly-report-w46-en-','')
    lines=[]
    for svg in sorted((eddir/'svg').glob('*.svg')):
        for i,t in enumerate(texts_of(svg)):
            lines.append(f"[{svg.stem}#{i} x={t['x']} y={t['y']} {t['size']}pt w={t['weight']} a={t['anchor']}] {t['text']}")
    (outdir/f'texts-{ed}.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(ed,len(lines))
