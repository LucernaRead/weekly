import re, html, pathlib, collections
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def els(path):
    s=path.read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        out.append(html.unescape(re.sub(r'<[^>]+>','',m.group(2))))
    return out
print("=== EXERCISE COUNTS per page (level-chip + number pairs) ===")
tot=collections.Counter(); perpage={}
for f in ['p1-portada','p2-vida','p3-cultura','p4-deporte','p5-juventud','p6-afondo','p7-lengua','p8-ejercicios']:
    ts=els(base/f"files/weekly-report-w45-es-pt/svg/{f}.svg")
    pairs=[]
    for i in range(len(ts)-1):
        if ts[i] in ('A2','B1','B2') and re.fullmatch(r'\d+\.', ts[i+1] or ''):
            pairs.append((ts[i], int(ts[i+1][:-1])))
    # also standalone numbers without level? (quiz?) count numbers not paired
    nums=set(int(t[:-1]) for t in ts if re.fullmatch(r'\d+\.', t))
    paired=set(n for _,n in pairs)
    print(f"  {f}: paired={len(pairs)} levels={dict(collections.Counter(l for l,_ in pairs))} numbers={min(paired) if paired else '-'}..{max(paired) if paired else '-'} unpaired_numbers={sorted(nums-paired)[:20]}")
    perpage[f]=pairs
    for l,n in pairs: tot[l]+=1
print("  TOTAL paired:", sum(len(v) for v in perpage.values()), "levels:", dict(tot))
print("\n=== P8 answer groups by separator (pagination cross-check) ===")
ts=els(base/"files/weekly-report-w45-es-pt/svg/p8-ejercicios.svg")
# answer section only
start=[i for i,t in enumerate(ts) if t.startswith('RESPUESTAS ·')][0]
cur=None; groups=collections.defaultdict(list)
for t in ts[start+1:]:
    m=re.match(r'^— PÁGINA (\d+) —$', t)
    if m: cur=int(m.group(1)); continue
    m2=re.match(r'^(\d+)\.\s', t)
    if m2 and cur: groups[cur].append(int(m2.group(1)))
for pg in sorted(groups): print(f"  answers for source page {pg}: n={len(groups[pg])} range {min(groups[pg])}..{max(groups[pg])}")
print("  sum:", sum(len(v) for v in groups.values()))
print("\n=== P7 QUOTES: occurrences in full ED issue (joined page text, whitespace-normalised) ===")
pages={}
for f in ['p1-portada','p2-vida','p3-cultura','p4-deporte','p5-juventud','p6-afondo','p7-lengua','p8-ejercicios']:
    pages[f]=' '.join(els(base/f"files/weekly-report-w45-es-pt/svg/{f}.svg"))
full=' '.join(pages.values())
def norm(s): return re.sub(r'\s+',' ',s).strip()
fulln=norm(full)
quotes=[
"Las listas ya están presentadas: ahora los partidos escriben sus programas.",
"El lunes 2 de noviembre es festivo en nueve comunidades — y día de trabajo en las demás.",
"Tres fiestas, una misma noche de otoño.",
"El Madrid ganó 2–1 en el Camp Nou: fue la primera derrota liguera del Barça.",
"El Bernabéu cambia el césped por el emparrillado: el fútbol americano llega a Madrid.",
"La vivienda es el principal problema para el 55,7 % de los españoles.",
"Una encuesta es una foto con margen de error, tomada en un día concreto.",
"El domingo 8, Madrid tiene dos citas: la NFL a las 15:30 y el Atlético–Barça a las 21:00.",
]
for q in quotes:
    qn=norm(q)
    # count in full issue; also per-page
    per={f: norm(t).count(qn) for f,t in pages.items() if norm(t).count(qn)}
    print(f"  total={fulln.count(qn)} per-page={per} :: {q[:70]}")
    # also check verbatim contiguous in article pages: article occurrence should be in its tagged page
