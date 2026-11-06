import re, os, glob
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-ko/svg'
BUILD='/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-nl-ko-build'
def is_hangul(ch): return 0xAC00 <= ord(ch) <= 0xD7A3
def syl_count(s): return sum(1 for c in s if is_hangul(c))
def hangul_tokens(s):
    return re.findall(r'[\uAC00-\uD7A3]+', s)
# source corpus: all .py string content in build dir (read-only)
src=''
for f in glob.glob(BUILD+'/*.py'):
    src+=open(f,encoding='utf-8').read()+'\n'
src_nospace = re.sub(r'\s+','',src)

def parse(fname):
    s=open(os.path.join(ED,fname),encoding='utf-8').read()
    els=[]
    for m in re.finditer(r'<text\s+([^>]*)>([^<]*)</text>', s):
        a,t=m.group(1),m.group(2)
        x=re.search(r'x="([0-9.]+)"',a); y=re.search(r'y="([0-9.]+)"',a)
        if x and y: els.append((float(x.group(1)),float(y.group(1)),t))
    els.sort(key=lambda e:(e[0],e[1]))
    return els

total_cand=0; splits=[]; unresolved=[]
for fname in sorted(os.listdir(ED)):
    els=parse(fname)
    for i in range(len(els)-1):
        x1,y1,t1=els[i]; x2,y2,t2=els[i+1]
        if abs(x1-x2)>1: continue
        gap=y2-y1
        if not (10<=gap<=45): continue
        # Korean end of upper + Korean start of lower
        m1=re.search(r'([\uAC00-\uD7A3]+)[^ \uAC00-\uD7A3]*$', t1)
        m2=re.match(r'([\uAC00-\uD7A3]+)', t2)
        if not m1 or not m2: continue
        tail_word=m1.group(1); head_word=m2.group(1)
        # last syllable-run at end: actually need last token: use trailing hangul run
        # tail = last hangul run of t1, head = first hangul run of t2
        total_cand+=1
        joined = tail_word + head_word
        # adjudicate via source: spaced form present?
        spaced = (tail_word+' '+head_word) in src or (tail_word+' '+head_word) in src_nospace and False
        joined_in_src = joined in src
        # also check: does the paragraph text (rendered lines joined) contain joined as a word?
        if joined_in_src and not spaced:
            verdict='SPLIT'
        elif spaced and not joined_in_src:
            verdict='CLEAN-BREAK'
        else:
            verdict='UNRESOLVED'
        rec=(fname,y1,y2,tail_word,head_word,syl_count(head_word),verdict,t1[-40:],t2[:40:])
        if verdict=='SPLIT': splits.append(rec)
        elif verdict=='UNRESOLVED': unresolved.append(rec)
print(f"CANDIDATES={total_cand} TRUE_SPLITS={len(splits)} UNRESOLVED={len(unresolved)}")
print(f"S3 (head>=3 syllables) = {sum(1 for r in splits if r[5]>=3)}")
for r in splits:
    print(f"SPLIT {r[0]} y={r[1]}->{r[2]} tail={r[3]!r} head={r[4]!r} head_syl={r[5]} :: ...{r[7]!r} / {r[8]!r}")
print("--- UNRESOLVED ---")
for r in unresolved:
    print(f"UNRES {r[0]} y={r[1]}->{r[2]} tail={r[3]!r} head={r[4]!r} head_syl={r[5]} :: ...{r[7]!r} / {r[8]!r}")
# orphan final lines: element whose next same-x element gap>45 or none, Korean syllables<=1 in its LAST hangul token? Builder def: final line <=1 syllable total Korean? Use: whole line hangul count<=1 and line contains hangul and is paragraph-final
print("--- ORPHAN final lines (hangul<=1, paragraph-final) ---")
orph=0
for fname in sorted(os.listdir(ED)):
    els=parse(fname)
    for i,(x,y,t) in enumerate(els):
        if syl_count(t)==0: continue
        nxt = els[i+1] if i+1<len(els) else None
        is_final = (nxt is None) or abs(nxt[0]-x)>1 or not (10<=nxt[1]-y<=45)
        if is_final and syl_count(t)<=1:
            orph+=1; print(f"ORPH {fname} y={y} {t!r}")
print("orphan count:", orph)
print("--- LINE-START orphan punct ---")
lp=0
for fname in sorted(os.listdir(ED)):
    els=parse(fname)
    for i in range(1,len(els)):
        x,y,t=els[i]; px,py,pt=els[i-1]
        if abs(x-px)<=1 and 10<=y-py<=45 and t and t[0] in ':.,;!?)]）':
            # only flag if previous line ends with hangul/latin (i.e. punct belongs to prev sentence)
            lp+=1; print(f"LPUNCT {fname} y={py}->{y} prev=...{pt[-30:]!r} cur={t[:30]!r}")
print("line-start punct count:", lp)
print()
print("=== First-round S3 sites in FINAL edition ===")
sites=[('p1-voorpagina.svg','쿠포르던이'),('p6-verdieping.svg','여러분은'),('p7-taal.svg','네덜란드가'),('p8-toets.svg','헤이렌베인'),('p3-cultuur.svg','주의하세요')]
for f,w in sites:
    els=parse(f)
    hits=[(y,t) for x,y,t in els if w in t]
    print(f, w, 'lines containing intact:', hits)
    # also check split form: line ending with first part
    print('   all lines with fragments:', [(y,t) for x,y,t in els if any(frag in t for frag in ['쿠포르던','포르던이','네덜','란드가','헤이렌베','페예노르트','주의','하세요'])][:6])
