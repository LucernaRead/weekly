import re, html, pathlib, json
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def parse(path):
    s=path.read_text(encoding='utf-8')
    els=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        attrs=m.group(1); t=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        fs=re.search(r'font-size="([\d.]+)"',attrs); fs=float(fs.group(1)) if fs else 0
        els.append((fs,t))
    # answer section: first element exactly starting 'RESPUESTAS ·'
    start=[i for i,(fs,t) in enumerate(els) if t.startswith('RESPUESTAS ·')][0]
    segs={}; cur=None; order=[]
    for fs,t in els[start+1:]:
        if t.startswith('— PÁGINA') or t.startswith('La Lucerna ·') or t.startswith('Página 8 de 8'):
            cur=None; continue
        m=re.match(r'^(\d+)\.\s+(.*)$', t)
        if m:
            cur=int(m.group(1)); segs[cur]=m.group(2); order.append(cur); continue
        if cur is not None:
            if fs>=20: cur=None; continue
            # model section: after 150, a header-like element or the model body lines (long Spanish prose, no number)
            # model body is preceded by a section header; detect header texts containing MODELO
            if 'MODELO' in t.upper(): cur=None; continue
            segs[cur]+= ' ' + t
    return segs, els
def key(seg):
    # dash-parse: split on FIRST ' — '; for 150 check-mark form: '✓ ...'
    if ' — ' in seg: return seg.split(' — ',1)[0].strip()
    return seg.strip()
core,_=parse(base/"files/weekly-report-w45-es-core/svg/p8-ejercicios.svg")
ed,_=parse(base/"files/weekly-report-w45-es-pt/svg/p8-ejercicios.svg")
print("core segments:", len(core), "nums", min(core), max(core), "missing:", sorted(set(range(1,151))-set(core)))
print("ed segments:", len(ed), "nums", min(ed), max(ed), "missing:", sorted(set(range(1,151))-set(ed)))
diffs=[]
for n in range(1,151):
    kc, ke = key(core[n]), key(ed[n])
    if kc!=ke: diffs.append(n)
print("DASH-PARSE KEY DIFFS:", diffs)
for n in [34,57,83,85,93,94,95,96,98,101,107,109,110,111,117,137,138,148,139,140,150,1]:
    print(f"--- #{n} ---\n  CORE seg: {core[n]!r}\n  CORE key: {key(core[n])!r}\n  ED   seg: {ed[n]!r}\n  ED   key: {key(ed[n])!r}")
json.dump({'core':core,'ed':ed,'diffs':diffs}, open(base/"hidden_files/w45/es-pt-proof/dashparse.json",'w'), ensure_ascii=False, indent=1)
# also: 150 model text word count: find MODELO section in ed svg
s=(base/"files/weekly-report-w45-es-pt/svg/p8-ejercicios.svg").read_text(encoding='utf-8')
els=[]
for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
    els.append(html.unescape(re.sub(r'<[^>]+>','',m.group(2))))
print("\nTAIL elements (last 25):")
for t in els[-25:]: print("  ", repr(t[:160]))
