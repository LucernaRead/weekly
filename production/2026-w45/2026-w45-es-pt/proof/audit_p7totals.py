import re, html, pathlib, collections
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def texts_with_attrs(path):
    s=path.read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        out.append((m.group(1), html.unescape(re.sub(r'<[^>]+>','',m.group(2)))))
    return out
def alltexts(root):
    out=[]
    for f in ['p1-portada','p2-vida','p3-cultura','p4-deporte','p5-juventud','p6-afondo','p7-lengua','p8-ejercicios']:
        out += [t for a,t in texts_with_attrs(base/f"{root}/{f}.svg")]
    return out
print("=== P7 FRASES: extract Spanish quotes from ED P7, count occurrences across ED issue ===")
ed_p7=texts_with_attrs(base/"files/weekly-report-w45-es-pt/svg/p7-lengua.svg")
core_p7=texts_with_attrs(base/"files/weekly-report-w45-es-core/svg/p7-lengua.svg")
# FRASES section: after 'FRASES DE LA SEMANA' element; Spanish quote lines are serif? Print neighbourhood
for label,ts in [('ED',ed_p7),('CORE',core_p7)]:
    fi=[i for i,(a,t) in enumerate(ts) if 'FRASES' in t]
    print(f"  {label} FRASES idx {fi}")
    if fi:
        for i in range(fi[0], min(fi[0]+40, len(ts))):
            print(f"    [{i}] {ts[i][1][:150]!r}")
