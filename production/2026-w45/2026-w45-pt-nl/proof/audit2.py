#!/usr/bin/env python3
"""Proof part 2: P8 item-by-item, gloss from source, frozen-PT survival,
geometry supplements, exercise counts, ABSTRACT, PDFs."""
import re, json, hashlib, base64, xml.etree.ElementTree as ET
from pathlib import Path
BASE = Path.home()/"workspace/goals/lucernaread-social-media-operations"
ED = BASE/"files/weekly-report-w45-pt-nl/svg"
CO = BASE/"files/weekly-report-w45-pt-core/svg"
W43 = BASE/"files/weekly-report-pt-nl/svg"
EDB = BASE/"hidden_files/weekly-report-w45-pt-nl-build"
COB = BASE/"hidden_files/weekly-report-w45-pt-build"
PAGES = ["p1-capa","p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento","p7-lingua","p8-avaliacao"]

def texts(p):
    t=ET.parse(str(p)); out=[]
    for el in t.iter():
        if el.tag.split('}')[-1]=='text':
            out.append({'x':el.get('x'),'y':el.get('y'),'fs':el.get('font-size'),'fill':el.get('fill'),'txt':''.join(el.itertext())})
    return out
def collapsed(s): return re.sub(r'\s+',' ',s).strip()
ed={pg:texts(ED/f"{pg}.svg") for pg in PAGES}
co={pg:texts(CO/f"{pg}.svg") for pg in PAGES}
ed_bare={pg:collapsed(' '.join(e['txt'] for e in ed[pg])) for pg in PAGES}
co_bare={pg:collapsed(' '.join(e['txt'] for e in co[pg])) for pg in PAGES}
CJK=re.compile(r'[\u2e80-\u9fff\uac00-\ud7af\u3040-\u30ff\uff00-\uffef]')

print("== P8: p8.py extract, 18 keydiff items + 139/140/150 ==")
import subprocess, sys
for name, path in [("core", CO/"p8-avaliacao.svg"), ("edition", ED/"p8-avaliacao.svg")]:
    r=subprocess.run([str(BASE/"tools/venv/bin/python"), str(BASE/"tools/p8.py"), "extract","--p8",str(path),"--total","150","--json",str(BASE/f"hidden_files/w45/pt-nl-proof/p8-{name}.json")],capture_output=True,text=True,cwd=str(BASE/"tools"))
    print(f"  {name}: {r.stdout.strip()} {r.stderr.strip()[:200]}")
kc=json.load(open(BASE/"hidden_files/w45/pt-nl-proof/p8-core.json"))
ke=json.load(open(BASE/"hidden_files/w45/pt-nl-proof/p8-edition.json"))
print("  extract keys:", list(kc.keys()), list(ke.keys()))
def get(d, *names):
    for n in names:
        if n in d: return d[n]
    return None
# dump structure sample
print("  core sample:", json.dumps(kc, ensure_ascii=False)[:800])
print("  ed sample:", json.dumps(ke, ensure_ascii=False)[:800])

print("== P8 printed lines (raw SVG text-node reconstruction) ==")
# P8 answer lines are sequences of text nodes; reconstruct by joining nodes in order and splitting on number pattern
def p8_lines(els):
    s=' '.join(e['txt'] for e in els)
    s=collapsed(s)
    parts=re.split(r'(?=\b\d{1,3}\.\s)', s)
    d={}
    for p in parts:
        m=re.match(r'(\d{1,3})\.\s(.*)', p)
        if m: d[int(m.group(1))]=m.group(2)
    return d
lc=p8_lines(co["p8-avaliacao"]); le=p8_lines(ed["p8-avaliacao"])
print(f"  lines parsed core={len(lc)} edition={len(le)} missing_ed={sorted(set(lc)-set(le))} extra_ed={sorted(set(le)-set(lc))}")
for n in [2,4,25,26,27,28,52,53,54,55,101,137,138,141,142,143,144,146,139,140,150]:
    tok_c = lc[n].split(' — ')[0] if n in lc else '?'
    tok_e = le[n].split(' — ')[0] if n in le else '?'
    print(f"  #{n} CORE token={tok_c!r}")
    print(f"      ED   token={tok_e!r}  token_equal={tok_c==tok_e}")
    print(f"      CORE full={lc.get(n,'?')[:160]!r}")
    print(f"      ED   full={le.get(n,'?')[:160]!r}")

print("== P8 notes language: CJK on P8 ==", sum(1 for ch in ed_bare["p8-avaliacao"] if CJK.match(ch)))
print("   P8 font sizes (edition, top counts):")
from collections import Counter
print("  ", Counter(e['fs'] for e in ed["p8-avaliacao"]).most_common(8))
print("   P8 font sizes (core, top counts):")
print("  ", Counter(e['fs'] for e in co["p8-avaliacao"]).most_common(8))

print("== gloss() source count (split on · itself, README #21) ==")
def gloss_calls(d):
    out={}
    for f in sorted(d.glob("content*.py")):
        src=f.read_text()
        for m in re.finditer(r'gloss\((.*?)\)', src, re.S):
            arg=m.group(1)
            # string literal contents
            lits=re.findall(r'"([^"]*)"', arg)
            joined=''.join(lits)
            out.setdefault(f.name, []).append(joined)
    return out
gc=gloss_calls(COB); ge=gloss_calls(EDB)
for f in sorted(set(gc)|set(ge)):
    cc=sum(len(s.split('·')) for s in gc.get(f,[]))
    ec=sum(len(s.split('·')) for s in ge.get(f,[]))
    print(f"  {f}: core items={cc} edition items={ec}")
    for s in ge.get(f,[]):
        for it in s.split('·'):
            head=it.strip().split('=')[0].strip()
            alive = head in ' '.join(ed_bare.values())
            print(f"      ED item head {head!r} alive_in_render={alive} :: {it.strip()[:90]}")
print("  core gloss heads:")
for f in sorted(gc):
    for s in gc[f]:
        for it in s.split('·'):
            print(f"      {it.strip()[:90]}")

print("== frozen PT survival: core sentences (no CJK, len>=25) ==")
# split core bare per page into sentences on . ! ? — keep order; check presence in edition same page
missing=[]
for pg in PAGES:
    sents=[s.strip() for s in re.split(r'(?<=[.!?])\s+', co_bare[pg]) if len(s.strip())>=25 and not CJK.search(s)]
    for s in sents:
        if s not in ed_bare[pg]:
            missing.append((pg,s))
print(f"  core PT sentences len>=25: checked; missing={len(missing)}")
for pg,s in missing: print(f"    MISS {pg}: {s[:180]!r}")

print("== freeze-diff removed strings with Latin content ==")
diff=json.load(open(BASE/"hidden_files/w45/pt-nl-proof/freeze-diff.json"))
for pgnum, pg in diff["pages"].items():
    for st in pg.get("removed_strings",[]):
        t=st["text"]; stripped=CJK.sub('', t).strip()
        if len(stripped)>=15:
            print(f"  p{pgnum} removed (Latin remnant): {t[:170]!r}")
print("  (removed strings fully CJK/explanation are expected; only Latin remnants listed)")

print("== band subs append pattern ==")
for pg, frag in [("p2-vida","Finados e revisão: o feriadão do Brasil"),("p7-lingua","Três níveis, três ferramentas")]:
    print(f"  {pg} PT half {frag!r} in ED: {frag in ed_bare[pg]}")
    # find full band-sub node(s)
    for e in ed[pg]:
        if frag in e['txt']: print(f"      node: {e['txt'][:200]!r}")
for pg in PAGES:
    subs=[e['txt'] for e in ed[pg] if '·' in e['txt'] and len(e['txt'])>60 and e['y'] and float(e['y'])<700]
    if subs: print(f"  {pg} top-band long nodes: {subs[:3]}")
print("  W43 P2 band sub nodes:")
w43p2=texts(W43/"p2-vida.svg")
for e in w43p2:
    if e['y'] and float(e['y'])<700 and len(e['txt'])>50: print(f"      {e['txt'][:200]!r}")

print("== image blob hash conventions ==")
for name, d in [("edition", ED), ("core", CO)]:
    raw=ET.parse(str(d/"p1-capa.svg"))
    for el in raw.iter():
        if el.tag.split('}')[-1]=='image':
            href=el.get('{http://www.w3.org/1999/xlink}href') or el.get('href')
            b64=href.split(',',1)[1]
            print(f"  {name}: decoded sha256={hashlib.sha256(base64.b64decode(b64)).hexdigest()} b64text sha256={hashlib.sha256(b64.encode()).hexdigest()} b64text md5={hashlib.md5(b64.encode()).hexdigest()}")

print("== ABSTRACT ==")
ab=(BASE/"files/weekly-report-w45-pt-nl/ABSTRACT.txt").read_text()
print(f"  lines={ab.strip().count(chr(10))+1} ascii_double_quotes={ab.count(chr(34))} chars={len(ab.strip())}")
print(f"  text: {ab.strip()}")
for kw in ["Enem","Finados","8 november","Portugees","Nederlands","A2","B2","150"]:
    print(f"  contains {kw!r}: {kw in ab}")

print("== PDFs (pypdf) ==")
sys.path.insert(0, str(BASE/"tools/venv/lib/python3.12/site-packages"))
try:
    from pypdf import PdfReader
    for f in ["A-Lucerna-VOL2.pdf","A-Lucerna-VOL2-web.pdf"]:
        r=PdfReader(str(BASE/f"files/weekly-report-w45-pt-nl/{f}"))
        txt=''.join((p.extract_text() or '') for p in r.pages)
        imgs=sum(len(p.images) for p in r.pages)
        print(f"  {f}: pages={len(r.pages)} mediabox0={r.pages[0].mediabox} images={imgs} textchars={len(txt)} has_badge={'TEKSTEN IN HET PORTUGEES' in txt}")
except Exception as ex:
    print("  pypdf failed:", ex)

print("== exercise numbering in rendered SVGs ==")
# exercise items carry a leading number token; count distinct 'N.' starts per page region is unreliable;
# instead count level badges and type labels
for pg in PAGES:
    lvl={lv: ed_bare[pg].count(f"[{lv}]") for lv in ["A2","B1","B2"]}
    print(f"  {pg} level-badge occurrences A2/B1/B2 = {lvl}")
for lab in ["Voltooi de zin","Meerkeuze","Woorden koppelen","Bouw de zin","Waar of onwaar","Gatentekst","Vertaal","Schrijven"]:
    tot=sum(ed_bare[pg].count(lab) for pg in PAGES)
    print(f"  type label {lab!r}: total occurrences={tot}")
