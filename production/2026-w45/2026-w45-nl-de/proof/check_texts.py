import re, glob, xml.etree.ElementTree as ET, json
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-de/svg/'
CO='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg/'
W43='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-de/svg/'
def texts(d, f):
    t=ET.parse(d+f)
    out=[]
    for el in t.iter():
        if el.tag.endswith('}text') or el.tag=='text':
            s=''.join(el.itertext()).strip()
            if s: out.append(s)
    return out
def joined(d,f): return ' '.join(texts(d,f))
def norm(s): return re.sub(r'\s+',' ',s).strip()
# --- 8 fragments ---
ed5=norm(joined(ED,'p5-jongeren.svg')); ed6=norm(joined(ED,'p6-verdieping.svg')); ed7=norm(joined(ED,'p7-taal.svg')); ed8=norm(joined(ED,'p8-toets.svg'))
print("P5 RTL full sentence in edition:", [m for m in re.findall(r'.{0,60}RTL 4.{0,80}', ed5)][:3])
print("P6 caption with paren in edition:", [m for m in re.findall(r'.{0,80}100 jongeren.{0,80}', ed6)][:2])
print("P7 bridges in edition:")
for pat in ['opruimen','vastzetten','meedoen']:
    print('  ', pat, [m for m in re.findall(r'.{0,40}'+pat+r'.{0,80}', ed7)][:3])
print("P8 item6 in edition:", [m for m in re.findall(r'6\. planten.{0,60}', ed8)][:2])
print("P8 item41 in edition:", [m for m in re.findall(r'41\. hebben voorgelezen.{0,80}', ed8)][:2])
# --- long Dutch-only core sentences survival P1-P7 ---
files=['p1-voorpagina.svg','p2-leven.svg','p3-cultuur.svg','p4-sport.svg','p5-jongeren.svg','p6-verdieping.svg','p7-taal.svg']
def has_cjk(s): return any('\u4e00'<=c<='\u9fff' for c in s)
for f in files:
    core_texts=texts(CO,f); ed=norm(joined(ED,f))
    missing=[]
    for s in core_texts:
        ns=norm(s)
        if len(ns)>=40 and not has_cjk(ns) and ns not in ed:
            # allow re-wrap: check all words present in order ignoring line splits? try removing spaces around punctuation
            missing.append(ns)
    print(f, "long pure-Latin core strings:", sum(1 for s in core_texts if len(norm(s))>=40 and not has_cjk(norm(s))), "not-verbatim-substring:", len(missing))
    for m in missing: print("   MISSING-VERBATIM:", m[:160])
# --- banned strings + CJK in edition ---
for f in sorted(glob.glob(ED+'*.svg')):
    t=open(f,encoding='utf-8').read()
    cjk=len(re.findall(r'[\u4e00-\u9fff]',t))
    print(f.split('/')[-1], "CJKchars:",cjk, "桥接:",t.count('桥接'), "讲解:",t.count('讲解'), "译注:",t.count('译注'))
