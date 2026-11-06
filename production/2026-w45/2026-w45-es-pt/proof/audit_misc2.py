import re, html, pathlib, hashlib
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def texts(path):
    s=path.read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        out.append(html.unescape(re.sub(r'<[^>]+>','',m.group(2))))
    return out
print("=== GLOSS ===")
gloss={'p2-vida':(['festivo','el puente','la comunidad','anochecer','el horario de invierno']),
 'p3-cultura':(['sobrio','el homenaje','el disfraz','el boniato','el cementerio']),
 'p4-deporte':(['la jornada','recortar la distancia','recibir','visitar','el Metropolitano']),
 'p5-juventud':(['el emparrillado','el himno','el touchdown','la calabaza'])}
for f,heads in gloss.items():
    for label,root in [('CORE','files/weekly-report-w45-es-core/svg'),('ED','files/weekly-report-w45-es-pt/svg')]:
        ts=texts(base/f"{root}/{f}.svg")
        # gloss paragraph: elements containing 'Nota' (ed) or '译注' (core); join it + following until next header (element starting with all-caps title or y jump) - use known spans from previous run: find start, then join while element does not start with a known next-box title; simpler: join start + next 4 elements, then count '·' in the portion up to final ').'/'。'
        si=[i for i,t in enumerate(ts) if t.startswith('Nota —') or '译注' in t][0]
        joined=' '.join(ts[si:si+6])
        # cut at first sentence terminator after gloss: gloss ends with '。' (core) or ').' (ed)
        m=re.search(r'^(.*?)(?:。|\)\.)', joined)
        para=m.group(1)+('。' if '。' in joined[:len(m.group(1))+1] else ').') if m else joined
        print(f"  {f} {label}: segments split on '·' = {len(para.split('·'))} :: {para!r}")
        print(f"    heads present in order: {[h for h in heads if h in para]} (expected {heads})")
print("\n=== IMAGES: element counts + payload MD5 (base64 decoded) ===")
for pg,f in [('P1','p1-portada'),('P2','p2-vida'),('P3','p3-cultura'),('P4','p4-deporte'),('P5','p5-juventud'),('P6','p6-afondo'),('P7','p7-lengua'),('P8','p8-ejercicios')]:
    for label,root in [('CORE','files/weekly-report-w45-es-core/svg'),('ED','files/weekly-report-w45-es-pt/svg')]:
        s=(base/f"{root}/{f}.svg").read_text(encoding='utf-8')
        uris=re.findall(r'xlink:href="data:image/[^;]+;base64,([A-Za-z0-9+/=]+)"', s)
        hrefs=re.findall(r'<image\b[^>]*?(?:href|xlink:href)="([^"]{0,80})', s)
        import base64
        md5s=[hashlib.md5(base64.b64decode(u)).hexdigest() for u in uris]
        print(f"  {pg} {label}: image elements={len(re.findall(r'<image\b', s))} dataURIs={len(uris)} payloadMD5={md5s} hrefs={hrefs}")
print("\n=== P5 credit lines (all small texts containing Foto/Crédit/USDA/dominio) ===")
for label,root in [('CORE','files/weekly-report-w45-es-core/svg'),('ED','files/weekly-report-w45-es-pt/svg')]:
    ts=texts(base/f"p5-juventud.svg".replace('p5-juventud.svg', f"{root}/p5-juventud.svg"))
    print(f"  P5 {label}: {[t for t in ts if any(k in t for k in ['Foto','USDA','dominio','Crédit','Commons','fuente'])]}")
    # also P3
    ts3=texts(base/f"{root}/p3-cultura.svg")
    print(f"  P3 {label}: {[t for t in ts3 if any(k in t for k in ['Foto','USDA','dominio','Crédit','Commons','fuente'])]}")
