import re, html, pathlib
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def els(root,f):
    s=(base/f"{root}/{f}.svg").read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        a=m.group(1); t=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        fs=float(re.search(r'font-size="([\d.]+)"',a).group(1)); x=float(re.search(r'x="([\d.]+)"',a).group(1)); y=float(re.search(r'y="([\d.]+)"',a).group(1))
        out.append((x,y,fs,t))
    return out
def show(label, root):
    print(f"===== {label} =====")
    p1=els(root,'p1-portada')
    print(" P1 badge candidates (y~372, long):")
    for x,y,fs,t in p1:
        if 360<=y<=385: print(f"   y={y} fs={fs} :: {t!r}")
    print(" P1 top strip (y~?):")
    for x,y,fs,t in p1:
        if 'SEMANAL' in t or 'CADA SEMANA' in t: print(f"   y={y} fs={fs} :: {t!r}")
    print(" P1 title line:")
    for x,y,fs,t in p1:
        if 'SEMANÁRIO' in t: print(f"   y={y} fs={fs} :: {t!r}")
    print(" Footers (all pages, unique):")
    foots=set()
    for f in ['p1-portada','p2-vida','p3-cultura','p4-deporte','p5-juventud','p6-afondo','p7-lengua','p8-ejercicios']:
        for x,y,fs,t in els(root,f):
            if y>=2620: foots.add(t)
    for t in sorted(foots): print(f"   {t!r}")
    print(" Bands:")
    for f in ['p1-portada','p2-vida','p3-cultura','p4-deporte','p5-juventud','p6-afondo','p7-lengua','p8-ejercicios']:
        for x,y,fs,t in els(root,f):
            if re.match(r'^(VIDA|CULTURA|DEPORTE|JUVENTUD|A FONDO|LENGUA|EJERCICIOS)', t) and '·' in t: print(f"   {f}: {t!r}")
    print(" Exercise headers + right text:")
    for f in ['p2-vida','p3-cultura','p4-deporte','p5-juventud','p6-afondo']:
        for x,y,fs,t in els(root,f):
            if t.startswith('EJERCICIOS ·') or 'Respostas na página 8' in t: print(f"   {f}: {t!r}")
    print(" Nota prefixes (first Nota element per page):")
    for f in ['p2-vida','p3-cultura','p4-deporte','p5-juventud']:
        for x,y,fs,t in els(root,f):
            if t.startswith('Nota —'): print(f"   {f}: {t[:60]!r}"); break
    print(" P1 furniture headers:")
    for x,y,fs,t in p1:
        if re.match(r'^(LA NOTICIA|AHORA TÚ|EN ESTA EDICIÓN|BREVES|QUIZ RELÁMPAGO)', t): print(f"   {t!r}")
    print(" P8 header + right text:")
    for x,y,fs,t in els(root,'p8-ejercicios'):
        if 'RESPUESTAS ·' in t or 'Cada resposta' in t or 'marca a questão' in t: print(f"   {t!r}")
    print(" Box titles (P1 CIFRAS, P2 CALENDARIO, P5 PLAN, P7 ERRORES/PALABRA) with sizes:")
    for f,pat in [('p1-portada','CIFRAS'),('p2-vida','CALENDARIO'),('p5-juventud','PLAN'),('p7-lengua','ERRORES'),('p7-lengua','PALABRA')]:
        for x,y,fs,t in els(root,f):
            if pat in t: print(f"   {f} y={y} fs={fs} :: {t!r}")
show('W43', 'files/weekly-report-es-pt/svg')
show('W45ED', 'files/weekly-report-w45-es-pt/svg')
