#!/usr/bin/env python3
"""Independent proofread analysis for W45 PT x NL. Reads ONLY shipped SVGs
(edition + core + W43 same-pairing), never writes to them."""
import re, json, hashlib, base64, unicodedata, xml.etree.ElementTree as ET
from pathlib import Path

BASE = Path.home()/"workspace/goals/lucernaread-social-media-operations"
ED = BASE/"files/weekly-report-w45-pt-nl/svg"
CO = BASE/"files/weekly-report-w45-pt-core/svg"
W43 = BASE/"files/weekly-report-pt-nl/svg"
PAGES = ["p1-capa","p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento","p7-lingua","p8-avaliacao"]

def parse(p):
    t = ET.parse(str(p)); els=[]
    for el in t.iter():
        tag = el.tag.split('}')[-1]
        if tag=='text':
            els.append({'x':el.get('x'),'y':el.get('y'),'fs':el.get('font-size'),
                        'fill':el.get('fill'),'fw':el.get('font-weight'),
                        'ta':el.get('text-anchor'),'txt':''.join(el.itertext())})
        elif tag=='image':
            els.append({'image':True,'href':el.get('{http://www.w3.org/1999/xlink}href') or el.get('href'),
                        'x':el.get('x'),'y':el.get('y'),'w':el.get('width'),'h':el.get('height')})
    return els

def bare(els):
    return ' '.join(e['txt'] for e in els if 'txt' in e)
def collapsed(s):
    return re.sub(r'\s+',' ',s).strip()

ed={pg:parse(ED/f"{pg}.svg") for pg in PAGES}
co={pg:parse(CO/f"{pg}.svg") for pg in PAGES}
w43={pg:parse(W43/f"{pg}.svg") for pg in PAGES} if (W43/"p1-capa.svg").exists() else {}
ed_bare={pg:collapsed(bare(ed[pg])) for pg in PAGES}
co_bare={pg:collapsed(bare(co[pg])) for pg in PAGES}
ed_all=collapsed(' '.join(ed_bare.values()))
co_all=collapsed(' '.join(co_bare.values()))

CJK = re.compile(r'[\u2e80-\u9fff\uac00-\ud7af\u3040-\u30ff\uff00-\uffef]')
print("== 1a CJK per page (rendered text nodes) ==")
for pg in PAGES:
    c=sum(1 for ch in ed_bare[pg] if CJK.match(ch))
    cc=sum(1 for ch in co_bare[pg] if CJK.match(ch))
    print(f"  {pg}: edition {c} core {cc}")
print("  edition total CJK:", sum(1 for ch in ed_all if CJK.match(ch)))

print("== 1b forbidden terms in rendered text ==")
for term in ["桥接","Bridge","bridge","NOCH EIN WORT","meedoen","HINWEIS","Seite","EXPLICATIONS","EXPLICACIONES","SPIEGAZIONI","Nota — "]:
    hits=[pg for pg in PAGES if term in ed_bare[pg]]
    print(f"  {term!r}: pages {hits}")

print("== 1c freeze-diff removed/added strings (from canonical diff json) ==")
diff=json.load(open(BASE/"hidden_files/w45/pt-nl-proof/freeze-diff.json"))
print("  diff keys:", list(diff.keys())[:10])
print(json.dumps(diff, ensure_ascii=False)[:600])

print("== 2 P7 word box ==")
wt="« feriadão »: sábado, domingo e segunda — três dias de descanso."
print("  definition verbatim in edition P7:", wt in ed_bare["p7-lingua"])
print("  definition verbatim in core P7:", wt in co_bare["p7-lingua"])
for pg in PAGES:
    if "feriadão = " in ed_bare[pg]:
        m=re.search(r'feriadão = [^·]*', ed_bare[pg]); print(f"  gloss on {pg}: {m.group(0) if m else '?'}")
    if "feriadão = " in co_bare[pg]:
        m=re.search(r'feriadão = [^·]*', co_bare[pg]); print(f"  core gloss on {pg}: {m.group(0) if m else '?'}")
print("  DE/NL-family word-box markers in edition:", [t for t in ["NOCH EIN WORT","Wort der Woche","meedoen"] if t in ed_all])

print("== 5 gloss boxes (rendered 'Uitleg — ' boxes, split on ·) ==")
tot=0
for pg in ["p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento"]:
    boxes=[e['txt'] for e in ed[pg] if 'txt' in e and e['txt'].startswith('Uitleg')]
    items=[]
    for b in boxes:
        body=b[len('Uitleg — '):] if b.startswith('Uitleg — ') else b
        items += [i.strip() for i in body.split('·') if i.strip()]
    print(f"  {pg}: boxes={len(boxes)} items={len(items)}")
    for it in items: print(f"      - {it}")
    tot+=len(items)
print("  TOTAL gloss items:", tot)
print("  gloss prefix 'Uitleg — ' present on all 5 pages:",
      all(any(e['txt'].startswith('Uitleg') for e in ed[pg] if 'txt' in e) for pg in ["p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento"]))
print("  any gloss box starting with other prefix:",
      [e['txt'][:30] for pg in PAGES for e in ed[pg] if 'txt' in e and ('Uitleg' in e['txt'][:12] and not e['txt'].startswith('Uitleg — '))])

print("== 5 P7 quotes 2x + tagged page ==")
quotes=[
 ("Do feriadão à prova: a semana do Enem","Página 1"),
 ("Muita gente viaja, visita a família e vai ao cemitério levar flores","Página 1"),
 ("Finados é o dia da memória","Página 2"),
 ("lembrar é um jeito de continuar perto","Página 3"),
 ("cada ponto vale uma posição, cada gol vale uma história","Página 4"),
 ("quem dorme bem lembra melhor","Página 5"),
 ("primeiro as fáceis, depois as difíceis","Página 6"),
 ("Confira o cartão, durma bem, chegue cedo","Página 2"),
]
for q,tag in quotes:
    per={pg: ed_bare[pg].count(q) for pg in PAGES if q in ed_bare[pg]}
    print(f"  {q[:50]!r} tag={tag} total={sum(per.values())} per-page={per} on_tagged_page={ed_bare[[p for p in PAGES if tag in ed_bare[p]][0]] if False else ''}")
    # tagged page: find page whose P7 tag line corresponds; check quote on the page number in tag
    pgnum=int(tag.split()[-1]); pgname=PAGES[pgnum-1]
    print(f"      on source page {pgname}: {ed_bare[pgname].count(q)}x ; on P7: {ed_bare['p7-lingua'].count(q)}x ; tag on P7: {(q in ed_bare['p7-lingua'] and tag in ed_bare['p7-lingua'])}")

print("== 6 readers corner ==")
p7=ed_bare["p7-lingua"]
disc_pt="Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3."
ex="«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
inv="Stuur je brief op: de beste verschijnen op pagina 7 in VOL.3!"
print("  disc PT verbatim:", disc_pt in p7)
print("  example verbatim:", ex in p7)
print("  invitation verbatim:", inv in p7)
for frag in ["Opmerking van de redactie","de echte brieven en beste teksten uit VOL.1 waren nog niet binnen","het voorbeeld blijft, de belofte gaat naar VOL.3","Voorbeeld van de redactie — geen echte brief"]:
    print(f"  NL frag {frag!r}: {frag in p7}")
print("  preview line (PT, frozen) 'as suas cartas e os melhores textos da página 8':",
      "as suas cartas e os melhores textos da página 8" in p7)
# extract full invitation context
i=p7.find("Stuur je brief op")
print("  invitation context:", p7[max(0,i-60):i+120] if i>=0 else "NOT FOUND")
i2=p7.find("Opmerking van de redactie")
print("  NL disclosure context:", p7[i2:i2+220] if i2>=0 else "NOT FOUND")

print("== 7 furniture edition vs W43 ==")
def find(els, pred):
    return [e for e in els if 'txt' in e and pred(e)]
for pg, label in [("p1-capa","P1")]:
    print("  ED badge:", [(e['y'],e['fs'],e['fill'],e['txt']) for e in find(ed[pg], lambda e: 'TEKSTEN IN HET PORTUGEES' in e['txt'])])
    if w43: print("  W43 badge:", [(e['y'],e['fs'],e['fill'],e['txt']) for e in find(w43[pg], lambda e: 'TEKSTEN IN HET PORTUGEES' in e['txt'])])
    print("  ED subtitle:", [(e['y'],e['fs'],e['txt']) for e in find(ed[pg], lambda e: e['y']=='330')])
    if w43: print("  W43 subtitle:", [(e['y'],e['fs'],e['txt']) for e in find(w43[pg], lambda e: e['y']=='330')])
    print("  ED topstrip:", [(e['txt']) for e in find(ed[pg], lambda e: 'ELKE WEEK' in e['txt'])])
    if w43: print("  W43 topstrip:", [(e['txt']) for e in find(w43[pg], lambda e: 'ELKE WEEK' in e['txt'])])
    print("  ED band right:", [(e['txt']) for e in find(ed[pg], lambda e: 'DE WEEK VAN HET ENEM' in e['txt'] or 'dag 1 van het Enem' in e['txt'])])
for pg in PAGES:
    fl=[e['txt'] for e in find(ed[pg], lambda e: 'PORTUGEES WEEKBLAD VOL.2' in e['txt'])]
    fr=[e['txt'] for e in find(ed[pg], lambda e: e['txt'].startswith('Pagina ') and 'van 8' in e['txt'])]
    print(f"  {pg} footer L={fl} R={fr}")
    if w43:
        wfl=[e['txt'] for e in find(w43[pg], lambda e: 'PORTUGEES WEEKBLAD' in e['txt'])]
        print(f"      W43 footer L={wfl}")
print("  ED P8 separators:", sorted(set(e['txt'] for e in find(ed['p8-avaliacao'], lambda e: 'Pagina' in e['txt'] and '—' in e['txt']))))
if w43: print("  W43 P8 separators:", sorted(set(e['txt'] for e in find(w43['p8-avaliacao'], lambda e: 'Pagina' in e['txt'] and '—' in e['txt']))))
print("  ED band titles P1-8 (red band heads):")
for pg in PAGES:
    heads=[e['txt'] for e in find(ed[pg], lambda e: e['fill']=='#a4553a' and e['fs']=='22')]
    print(f"    {pg}: {heads}")

print("== 8 images ==")
for pg in PAGES:
    imgs=[e for e in ed[pg] if e.get('image')]
    cimgs=[e for e in co[pg] if e.get('image')]
    print(f"  {pg}: edition images={len(imgs)} core images={len(cimgs)}")
    for e in imgs:
        raw=base64.b64decode(e['href'].split(',',1)[1]) if e['href'] and ',' in e['href'] else b''
        print(f"      x={e['x']} y={e['y']} {e['w']}x{e['h']} bytes={len(raw)} sha256={hashlib.sha256(raw).hexdigest()} md5={hashlib.md5(raw).hexdigest()}")
    for e in cimgs:
        raw=base64.b64decode(e['href'].split(',',1)[1]) if e['href'] and ',' in e['href'] else b''
        print(f"      CORE x={e['x']} y={e['y']} bytes={len(raw)} sha256={hashlib.sha256(raw).hexdigest()} md5={hashlib.md5(raw).hexdigest()}")
print("  credit on P1:", "Foto: Gary Todd / Wikimedia Commons — CC0" in ed_bare["p1-capa"])
print("  credit on P1 core:", "Foto: Gary Todd / Wikimedia Commons — CC0" in co_bare["p1-capa"])

print("== 9 English apparatus scan (all pages) ==")
EN=["Note | ","Page N of 8","Page 1 of 8","Answers on page","Levels are mixed","Complete the sentence","Multiple choice","Build the sentence","True or false","Cloze","Vocabulary matching","Sentence building","Fill in","Match the pairs","IN THIS ISSUE","IN NUMBERS","Text in Portuguese","Explanations in English","THE EDITION FOR ENGLISH-SPEAKING","PORTUGUESE WEEKLY","Editor's note","Send your letters"]
for ph in EN:
    hits=[pg for pg in PAGES if ph in ed_bare[pg]]
    if hits: print(f"  HIT {ph!r}: {hits}")
print("  (only hits printed; silence = 0)")
print("  'Note' occurrences:", [(pg, ed_bare[pg].count('Note')) for pg in PAGES if 'Note' in ed_bare[pg]])
print("  ASCII double-quote count in ABSTRACT check done separately")
