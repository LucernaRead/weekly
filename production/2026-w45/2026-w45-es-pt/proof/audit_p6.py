import re, html, pathlib, collections
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def elements(path):
    s=path.read_text(encoding='utf-8')
    out=[]
    for m in re.finditer(r'<(text|rect|line|circle|path|image)\b([^>]*?)(/?)>', s):
        tag=m.group(1); attrs=m.group(2)
        out.append((tag, attrs.strip()))
    # texts with content separately
    texts=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        texts.append((m.group(1).strip(), html.unescape(re.sub(r'<[^>]+>','',m.group(2)))))
    return s, out, texts
for label,path in [('CORE', base/"files/weekly-report-w45-es-core/svg/p6-afondo.svg"), ('ED', base/"files/weekly-report-w45-es-pt/svg/p6-afondo.svg")]:
    s,out,texts=elements(path)
    print(label, "elements:", len(out), "texts:", len(texts))
    # Inmigración
    for i,(a,t) in enumerate(texts):
        if 'Inmigración' in t:
            print(f"  {label} Inmigración text idx {i}: attrs={a!r} text={t!r}")
            # following rect in raw order after this text's position
            pos=s.find('Inmigración')
            m=re.search(r'<rect\b([^>]*?)>', s[pos:])
            print(f"  {label} next rect after it: {m.group(1).strip()!r}" if m else "  no rect")
    # chart-ish texts: find all texts with y between 900 and 2100 containing digits/% or chart labels
    print(f"  {label} P6 texts sample (chart region candidates):")
    for a,t in texts:
        y=re.search(r'y="([\d.]+)"',a)
        if y and 900<float(y.group(1))<2150 and (re.search(r'\d',t) or t in ('Inmigración','Vivienda','Empleo','Sanidad','Educación','PSOE','PP','Vox','Sumar')):
            print(f"    y={y.group(1)} :: {t!r} attrs={a!r}")
