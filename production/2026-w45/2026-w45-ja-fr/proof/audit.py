#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent proof audit for W45 JA x FR. Read-only vs delivery/core dirs.
Writes evidence txt/json into this proof dir only."""
import re, html, json, os, sys
from collections import Counter
sys.path.insert(0, os.path.expanduser('~/workspace/goals/lucernaread-social-media-operations/tools'))
import p8 as P8

B = os.path.expanduser('~/workspace/goals/lucernaread-social-media-operations')
ED = f'{B}/files/weekly-report-w45-ja-fr'
CORE = f'{B}/files/weekly-report-w45-ja-core'
W43 = f'{B}/files/weekly-report-ja-fr'
OUT = f'{B}/hidden_files/w45/ja-fr-proof'
os.makedirs(OUT, exist_ok=True)

def texts(path):
    s = open(path, encoding='utf-8').read()
    return [(float(x), float(y), html.unescape(re.sub(r'<[^>]+>', '', c)),
             dict(re.findall(r'([\w-]+)="([^"]*)"', a)))
            for x, y, c, a in
            [(m.group(1), m.group(2), m.group(4), m.group(3))
             for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>(.*?)</text>', s, re.S)]]

def all_texts(d):
    return {fn: texts(os.path.join(d, 'svg', fn)) for fn in sorted(os.listdir(os.path.join(d, 'svg'))) if fn.endswith('.svg')}

EDT = all_texts(ED); CORET = all_texts(CORE)
PAGES = ['p1-hyoushi.svg','p2-kurashi.svg','p3-bunka.svg','p4-supotsu.svg','p5-wakamono.svg','p6-fukayomi.svg','p7-kotoba.svg','p8-tesuto.svg']

def join2(a, b):
    if not a: return b
    if re.search(r'[\u2e80-\u9fff\u3040-\u30ff]$', a) or re.search(r'^[\u2e80-\u9fff\u3040-\u30ff]', b): return a + b
    return a + ' ' + b

# ---------- P8 answer-section line alignment ----------
def p8_lines(T):
    els = T['p8-tesuto.svg']
    items = {}; cur = None
    started = False
    for x, y, t, attrs in els:
        if y < 1302 or y >= 2580: continue
        if t.startswith('答え') or t.startswith('Une courte') or t.startswith('每题'): continue
        if re.match(r'^—\s*.*\s*—$', t.strip()): continue
        m = re.match(r'^(\d+)\.\s?(.*)$', t.strip())
        if m:
            cur = int(m.group(1)); items[cur] = m.group(2)
        elif cur is not None:
            items[cur] = join2(items[cur], t.strip())
    return items
ce = p8_lines(CORET); ee = p8_lines(EDT)
with open(f'{OUT}/p8-lines-mine.txt', 'w', encoding='utf-8') as f:
    f.write(f"core items: {len(ce)} nums {min(ce)}..{max(ce)} contiguous={sorted(ce)==list(range(1,151))}\n")
    f.write(f"edition items: {len(ee)} nums {min(ee)}..{max(ee)} contiguous={sorted(ee)==list(range(1,151))}\n")
    f.write(f"missing in edition: {sorted(set(ce)-set(ee))} extra in edition: {sorted(set(ee)-set(ce))}\n\n")
    f.write("== IDENTICAL full lines (core == edition) ==\n")
    ident = [n for n in range(1,151) if ce[n]==ee[n]]
    f.write(f"count={len(ident)} nums={ident}\n")
    for n in ident: f.write(f"  #{n}: {ce[n]}\n")
    f.write("\n== KEYDIFF items (p8.py list) with full-line对照 + parsed keys ==\n")
    kd = [1,2,5,7,8,9,29,32,65,69,78,101,113,115,117,118,137,138,140,146,147]
    for n in kd:
        seg_c, seg_e = ce[n], ee[n]
        kc = P8.detect_note(seg_c); ke = P8.detect_note(seg_e)
        true_c = seg_c.split(' — ',1)[0]; true_e = seg_e.split(' — ',1)[0]
        f.write(f"#{n}:\n  CORE : {seg_c}\n  ED   : {seg_e}\n  true-key-before-dash identical={true_c==true_e} | core true-key={true_c!r} | ed true-key={true_e!r}\n  p8-parsed core key={kc[1]!r} method={kc[2]} | ed key={ke[1]!r} method={ke[2]}\n")
    f.write("\n== #139 / #140 / #150 spotlight ==\n")
    for n in (139,140,150):
        f.write(f"#{n} CORE: {ce[n]}\n#{n} ED  : {ee[n]}\n  identical={ce[n]==ee[n]}\n")
    f.write("\n== P8 note-language check: every edition line's note part ==\n")
    # note part = after first ' — ' if present else after '=' gloss etc; flag any CJK run that is a Chinese explanation:
    # simpler: list edition lines containing Simplified-Chinese-only indicator chars in note position
    bad=[]
    for n in range(1,151):
        ln=ee[n]
        # strip Japanese key part before ' — ' or ' = ' headword: check remainder for Chinese chars not in Japanese headword set
        if '工艺展' in ln or '传统' in ln: bad.append((n,ln))
    f.write(f"lines containing 工艺展/传统: {bad}\n")

# ---------- kinsoku ----------
FORBID_START = set('、。．，・：；？！）〕］｝〉》」』】)]}>}・ァィゥェォッャュョヮー')
FORBID_END = set('（〔［｛〈《「『【(')
with open(f'{OUT}/kinsoku.txt','w',encoding='utf-8') as f:
    tot=0
    for pg in PAGES:
        hits=[]
        for x,y,t,attrs in EDT[pg]:
            s=t.strip()
            if not s: continue
            if s[0] in FORBID_START: hits.append(('START',round(y,1),s))
            if s[-1] in FORBID_END: hits.append(('END',round(y,1),s))
        f.write(f"{pg}: start-violations={sum(1 for h in hits if h[0]=='START')} end-violations={sum(1 for h in hits if h[0]=='END')}\n")
        for h in hits: f.write(f"   {h}\n")
        tot+=len(hits)
    f.write(f"TOTAL violations={tot}\n")

# ---------- banned word + 工艺展 + English residue ----------
with open(f'{OUT}/residue.txt','w',encoding='utf-8') as f:
    for label, d, files in [('ED-SVG', ED, PAGES), ('ED-KIT', ED, None), ('ED-ABSTRACT', ED, None)]:
        pass
    ed_svg_text = '\n'.join(t for pg in PAGES for _,_,t,_ in EDT[pg])
    kit = open(f'{ED}/WEEKLY-KIT.md', encoding='utf-8').read()
    ab = open(f'{ED}/ABSTRACT.txt', encoding='utf-8').read()
    f.write(f"桥接 in ED SVG: {ed_svg_text.count('桥接')} | in KIT: {kit.count('桥接')} | in ABSTRACT: {ab.count('桥接')}\n")
    f.write(f"工艺展 in ED SVG: {ed_svg_text.count('工艺展')} | 传统 in ED SVG: {ed_svg_text.count('传统')}\n")
    f.write(f"Readers' corner in ED SVG: {ed_svg_text.count(chr(82)+'eaders')} ; exact \"Readers' corner\": {'Readers' in ed_svg_text and 'corner' in ed_svg_text}\n")
    f.write(f"Le courrier des lecteurs in ED SVG: {ed_svg_text.count('Le courrier des lecteurs')}\n")
    # distinct Latin tokens
    toks = Counter(re.findall(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'’-]*", ed_svg_text))
    f.write("\nDistinct Latin tokens (freq>=2 or len>=3), sorted:\n")
    for tok,c in sorted(toks.items(), key=lambda kv:(-kv[1],kv[0])):
        f.write(f"  {tok} x{c}\n")

# ---------- CJK runs word-level ----------
CJK = re.compile(r'[\u2e80-\u9fff\u3040-\u30ff]+')
core_runs = set(); core_text_set=set()
for pg in PAGES:
    for _,_,t,_ in CORET[pg]:
        core_text_set.add(t)
        core_runs.update(CJK.findall(t))
ed_runs = set()
for pg in PAGES:
    for _,_,t,_ in EDT[pg]:
        ed_runs.update(CJK.findall(t))
# runs in edition that never occur in any core text node
novel = sorted(ed_runs - core_runs)
with open(f'{OUT}/cjk-wordlevel.txt','w',encoding='utf-8') as f:
    f.write(f"distinct CJK runs core={len(core_runs)} edition={len(ed_runs)} edition-runs-not-verbatim-in-any-core-text-node={len(novel)}\n")
    for r in novel: f.write(f"  NOVEL-RUN: {r}\n")
    # runs in edition non-identical nodes: list nodes not identical to core, with their CJK runs
    f.write("\nEdition text nodes NOT byte-identical to any core node, with CJK runs (first 400):\n")
    n=0
    for pg in PAGES:
        for _,_,t,_ in EDT[pg]:
            if t not in core_text_set and CJK.search(t):
                f.write(f"  {pg}: {t}  | runs={CJK.findall(t)}\n"); n+=1
                if n>=400: break
        if n>=400: break
    f.write(f"total such nodes (capped display): {n}\n")
    # Simplified-exclusive indicator: chars in edition that appear ONLY in core removed (non-identical) nodes
    core_retained_chars = set()
    for pg in PAGES:
        for _,_,t,_ in CORET[pg]:
            if t in {tt for p in PAGES for _,_,tt,_ in EDT[p]}:
                core_retained_chars.update(t)
    ed_chars = set(''.join(ed_runs))
    only_removed = sorted(ed_chars - core_retained_chars)
    f.write(f"\nEdition CJK chars NOT in any retained (identical) core node: {len(only_removed)}: {''.join(only_removed)}\n")
    for ch in only_removed:
        # where does it occur in edition?
        occ=[]
        for pg in PAGES:
            for _,_,t,_ in EDT[pg]:
                if ch in t: occ.append(f"{pg}:{t}")
                if len(occ)>=3: break
            if len(occ)>=3: break
        f.write(f"  U+{ord(ch):04X} {ch}: {occ[:3]}\n")

# ---------- gloss ----------
def gloss_runs(T):
    """Reconstruct gloss boxes from SVG: lines starting 'Note — ' plus following
    same-x wrapped continuation lines (consecutive in doc order, y-step < 40)."""
    out={}
    for pg in PAGES:
        els=T[pg]; runs=[]; cur=None; lasty=None; lastx=None
        for x,y,t,attrs in els:
            if t.startswith('Note — '):
                cur=[t]; runs.append(cur); lasty=y; lastx=x; continue
            if cur is not None and x==lastx and 0 < y-lasty < 40:
                # continuation only if previous run line is a gloss wrap: next element after a gloss
                # line at same x within one line-height is a wrap continuation (exercises sit at col x, gloss at col x+18)
                cur.append(t); lasty=y; continue
            cur=None
        out[pg]=[''.join(r) for r in runs]
    return out
eg = gloss_runs(EDT); cg = gloss_runs(CORET)
with open(f'{OUT}/gloss.txt','w',encoding='utf-8') as f:
    f.write("Per-page rendered gloss counts (split by ·):\n")
    for pg in PAGES:
        ce_c=[g.count('·')+1 for g in cg[pg]]; ee_c=[g.count('·')+1 for g in eg[pg]]
        f.write(f"  {pg}: core boxes={len(cg[pg])} entries-per-box={ce_c} total={sum(ce_c)} | edition boxes={len(eg[pg])} entries-per-box={ee_c} total={sum(ee_c)}\n")
        for g in eg[pg]: f.write(f"      ED: {g}\n")
        for g in cg[pg]: f.write(f"      CORE: {g}\n")
    f.write(f"TOTAL core={sum(sum(g.count(chr(183))+1 for g in v) for v in cg.values())} edition={sum(sum(g.count(chr(183))+1 for g in v) for v in eg.values())}\n")
    # source gloss strings
    import ast
    for label, build in [('CORE','weekly-report-w45-ja-build'), ('ED','weekly-report-w45-ja-fr-build')]:
        f.write(f"\nSource gloss() strings in {label} build:\n")
        for cf in ['content12.py','content34.py','content56.py']:
            src=open(f'{B}/hidden_files/{build}/{cf}',encoding='utf-8').read()
            for m in re.finditer(r'\.gloss\("([^"]+)"\)', src):
                s=m.group(1); f.write(f"  {cf}: entries={s.count('·')+1} :: {s}\n")

# ---------- P7 ----------
with open(f'{OUT}/p7.txt','w',encoding='utf-8') as f:
    # definition paras: P7 texts identical core vs edition?
    ct=[t for _,_,t,_ in CORET['p7-kotoba.svg']]; et=[t for _,_,t,_ in EDT['p7-kotoba.svg']]
    f.write(f"P7 core text nodes={len(ct)} edition={len(et)}\n")
    f.write("P7 edition nodes NOT in core (should be French notes/glosses/headers only):\n")
    cs=set(ct)
    for t in et:
        if t not in cs: f.write(f"  ED-ONLY: {t}\n")
    f.write("P7 core nodes NOT in edition (should be Chinese notes/glosses/headers only):\n")
    es=set(et)
    for t in ct:
        if t not in es: f.write(f"  CORE-ONLY: {t}\n")
    # golden sentences: from edition content7 quotes
    src=open(f'{B}/hidden_files/weekly-report-w45-ja-fr-build/content7.py',encoding='utf-8').read()
    quotes=re.findall(r'\(\"([「『].*?[」』])\"', src)
    # the quotes list is in content7: extract the 8 tuples
    qlist=re.findall(r'\(\"(「.*?」)\",', src)
    f.write(f"\nGolden quotes extracted from content7: {len(qlist)}\n")
    whole=''.join(t for pg in PAGES for _,_,t,_ in EDT[pg])
    norm=lambda s: re.sub(r'\s+','',s).replace('「','').replace('」','').replace('『','').replace('』','')
    whole_n=norm(whole)
    for q in qlist:
        f.write(f"  {q} -> normalized count in whole book (whitespace+brackets stripped) = {whole_n.count(norm(q))}\n")
    # also count with brackets kept
    whole2=re.sub(r'\s+','',whole)
    for q in qlist:
        f.write(f"  with-brackets count = {whole2.count(re.sub(chr(32),'',q))} for {q}\n")
    # P7 teaser rect: dark rect on P7 near bottom
    s=open(f'{ED}/svg/p7-kotoba.svg',encoding='utf-8').read()
    rects=re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]*)"', s)
    f.write("\nP7 rects with fill #2c2822 (dark):\n")
    for x,y,w,h,fl in rects:
        if fl=='#2c2822': f.write(f"  x={x} y={y} w={w} h={h} ends={float(y)+float(h)}\n")
    # footer mapping
    f.write("\nFooters:\n")
    for pg in PAGES:
        ef=[t for _,_,t,_ in EDT[pg] if t.startswith('Page ')]; cf=[t for _,_,t,_ in CORET[pg] if '版 / 共' in t]
        f.write(f"  {pg}: core={cf} edition={ef}\n")
    # P7 teaser text lines
    f.write("\nP7 teaser (dark band) texts:\n")
    for x,y,t,attrs in EDT['p7-kotoba.svg']:
        if y>2300 and y<2540: f.write(f"  y={y} x={x} {t}\n")

# ---------- furniture three-way ----------
with open(f'{OUT}/furniture.txt','w',encoding='utf-8') as f:
    def mast(d):
        T=all_texts(d)['p1-hyoushi.svg']
        out={}
        for x,y,t,attrs in T:
            if t=='Lucerna' and attrs.get('text-anchor')=='middle': out['wordmark_y']=y; out['wordmark_size']=attrs.get('font-size')
            if t.startswith('日本語版 · VOL'): out['edition_y']=y; out['edition_size']=attrs.get('font-size')
            if 'EXPLICATIONS EN FRANÇAIS' in t and y<400: out['badge_y']=y; out['badge_size']=attrs.get('font-size'); out['badge_fill']=attrs.get('fill'); out['badge_text']=t
            if t.startswith('日本語を学ぶ人のための週刊新聞'): out['tagline_y']=y; out['tagline_size']=attrs.get('font-size')
        s=open(os.path.join(d,'svg','p1-hyoushi.svg'),encoding='utf-8').read()
        lines=re.findall(r'<line x1="65" y1="([\d.]+)" x2="1885" y2="([\d.]+)" stroke="#28251d" stroke-width="([\d.]+)"/>', s)
        out['rules']=[(a,c) for a,b,c in lines]
        rects=re.findall(r'<rect x="65" y="([\d.]+)" width="1820" height="118"[^>]*fill="#2c2822"/>', s)
        out['dark_y']=rects
        return out
    for label,d in [('W43-JA-FR',W43),('W45-CORE',CORE),('W45-JA-FR',ED)]:
        f.write(f"{label}: {json.dumps(mast(d),ensure_ascii=False)}\n")
    f.write("\nFooters pairing on all 8 pages (edition):\n")
    for pg in PAGES:
        fl=[t for _,_,t,_ in EDT[pg] if t.startswith('Lucerna · HEBDOMADAIRE')]
        f.write(f"  {pg}: {fl}\n")

# ---------- model essay + ABSTRACT + images ----------
with open(f'{OUT}/model-abstract-images.txt','w',encoding='utf-8') as f:
    # model essay: P8 section H para lines starting 例：
    p8texts=[t for _,_,t,_ in EDT['p8-tesuto.svg']]
    f.write("P8 texts containing 例： or モデル:\n")
    for t in p8texts:
        if '例：' in t or 'Modèle' in t: f.write(f"  {t}\n")
    # reconstruct model essay: lines after '例： ' until end_report? In SVG, para split=False wraps: lines start with 例： then continuations at same x? Print all P8 texts with y between section H para start: find '例：'
    els=EDT['p8-tesuto.svg']
    idx=[i for i,(x,y,t,a) in enumerate(els) if t.startswith('例：')]
    f.write(f"model start idx={idx}\n")
    if idx:
        i=idx[0]; seg=[els[i][2]]
        j=i+1
        while j<len(els) and els[j][1]<1252 and els[j][0]==els[i][0]:
            seg.append(els[j][2]); j+=1
        joined=''.join(seg)
        f.write(f"  joined model lines: {seg}\n")
        body=joined[2:] if joined.startswith('例：') else joined
        f.write(f"  model char count (no spaces, after 例：) = {len(body.replace(' ',''))} ; body={body}\n")
        f.write(f"  claimed 167? {len(body.replace(' ',''))==167}\n")
    ab=open(f'{ED}/ABSTRACT.txt',encoding='utf-8').read()
    f.write(f"\nABSTRACT raw: {ab!r}\nlines={ab.count(chr(10))} has-ascii-dquote={'\"' in ab}\n")
    # images: data:image payloads per page vs core: compare decoded bytes hash
    import hashlib, base64
    def img_hashes(d):
        out={}
        for pg in PAGES:
            s=open(os.path.join(d,'svg',pg),encoding='utf-8').read()
            imgs=re.findall(r'<image x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*href="data:image/(png|jpeg);base64,([^"]+)"', s)
            out[pg]=[(x,y,w,h,hashlib.sha256(base64.b64decode(b)).hexdigest()[:16],len(b)) for x,y,w,h,ext,b in imgs]
        return out
    ci=img_hashes(CORE); ei=img_hashes(ED)
    for pg in PAGES:
        f.write(f"  {pg}: core images={ci[pg]} edition images={ei[pg]} payload-equal={[c[4]==e[4] for c,e in zip(ci[pg],ei[pg])]} count-equal={len(ci[pg])==len(ei[pg])}\n")
    # credits: caption credit lines in SVG (15.5px grey texts near images) + assets CREDITS
    f.write("\nCredit-like lines in edition SVGs:\n")
    for pg in PAGES:
        for x,y,t,attrs in EDT[pg]:
            if attrs.get('font-size')=='15.5': f.write(f"  {pg} y={y}: {t}\n")
    f.write(f"\nBuild assets CREDITS.md:\n{open(f'{B}/hidden_files/weekly-report-w45-ja-fr-build/assets/CREDITS.md',encoding='utf-8').read()}\n")

# ---------- round4 vs current ----------
with open(f'{OUT}/round4-scope.txt','w',encoding='utf-8') as f:
    def load(p):
        d={}
        for ln in open(p,encoding='utf-8'):
            h,path=ln.split(None,1); d[os.path.basename(path.strip())]=h
        return d
    r4=load(f'{B}/hidden_files/weekly-report-w45-ja-fr-build/sha256-round4.txt')
    r4c=load(f'{B}/hidden_files/weekly-report-w45-ja-fr-build/sha256-round4-cards-pdf.txt')
    import hashlib
    def sha(p):
        h=hashlib.sha256()
        with open(p,'rb') as fh:
            for ch in iter(lambda: fh.read(1<<20), b''): h.update(ch)
        return h.hexdigest()
    cur_svg={fn:sha(f'{ED}/svg/{fn}') for fn in PAGES}
    cur_cards={fn:sha(f'{ED}/cards/{fn.replace(".svg",".png")}') for fn in PAGES}
    cur_pdfs={'Lucerna-VOL2-FR.pdf':sha(f'{ED}/Lucerna-VOL2-FR.pdf'),'Lucerna-VOL2-FR-web.pdf':sha(f'{ED}/Lucerna-VOL2-FR-web.pdf')}
    f.write("SVG round4 -> current:\n")
    for fn in PAGES: f.write(f"  {fn}: same={r4.get(fn)==cur_svg[fn]} r4={r4.get(fn)} cur={cur_svg[fn]}\n")
    f.write("Cards+PDF round4 -> current:\n")
    for fn,cur in list(cur_cards.items())+list(cur_pdfs.items()):
        f.write(f"  {fn}: same={r4c.get(fn)==cur} r4={r4c.get(fn)} cur={cur}\n")

print("audit done")
print(f"p8 core={len(ce)} edition={len(ee)} identical-lines={[n for n in range(1,151) if ce[n]==ee[n]]}")
