import json, re, xml.etree.ElementTree as ET
from collections import defaultdict
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
NO_START="。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;\""
NO_END="「『（【〈《([{\""
OPEN_SET=set("「『（【〈《([{")
CLOSE_SET=set("」』）】〉》)]}")
JP_START=set("、。！？：；）」』】ー…‥・") | set("ぁぃぅぇぉゃゅょっァィゥェォャュョッ")
def is_hangul_syl(c): return '\uAC00'<=c<='\uD7A3'
# --- 1. wrap log analysis ---
calls=[json.loads(l) for l in open(f"{BASE}/hidden_files/w45/ko-ja-proof/work/wrap-proof.log", encoding='utf-8')]
print(f"wrap calls: {len(calls)}")
post_start=0; post_end=0; post_start_ex=[]; post_end_ex=[]
for c in calls:
    for ln in c['post']:
        if ln and ln[0] in NO_START: post_start+=1; post_start_ex.append((c['text'][:40],ln[:40]))
        if ln and ln[-1] in NO_END: post_end+=1; post_end_ex.append((c['text'][:40],ln[:40]))
print(f"POST line-start NO_START flags: {post_start} {post_start_ex[:5]}")
print(f"POST line-end NO_END flags: {post_end} {post_end_ex[:5]}")
# PRE mid-word splits
def word_spans(text):
    # spans in space-removed coordinates: list of (start,end,word)
    spans=[]; pos=0
    for w in text.split(' '):
        if w=='': continue
        spans.append((pos,pos+len(w),w)); pos+=len(w)
    return spans, pos
ge3=[]; lt3=[]; bracket=[]
for c in calls:
    pre=c['pre']; text=c['text']
    if len(pre)<2: continue
    spans,_=word_spans(text)
    # positions of boundaries in space-removed coords: cumulative len of pre lines with spaces removed
    pos=0
    for a,b in zip(pre,pre[1:]):
        pos+=len(a.replace(' ',''))
        # find word containing boundary pos (boundary between pos-1 and pos)
        for s,e,w in spans:
            if s<pos<e:
                tail=w[pos-s:] if False else None
                # tail fragment at end of line a = word chars from (pos-s) onward? Actually boundary inside word: chars before boundary belong to line a end, after to line b start.
                # "tail" per task = fragment length: use chars of word on line-a side? Report both.
                before=w[:pos-s]; after=w[pos-s:]
                nb=sum(1 for ch in before if is_hangul_syl(ch)); na=sum(1 for ch in after if is_hangul_syl(ch))
                rec=(text[:50],a[-20:],b[:20],w,before,after,nb,na)
                if nb>=3 or na>=3: ge3.append(rec)
                else: lt3.append(rec)
                break
        # bracket fragments: line ends with opening bracket or next starts with closing bracket
        if a and a[-1] in OPEN_SET: bracket.append(('END-OPEN', text[:40], a[-20:], b[:20]))
        if b and b[0] in CLOSE_SET: bracket.append(('START-CLOSE', text[:40], a[-20:], b[:20]))
print(f"PRE mid-word splits: >=3-syllable-side: {len(ge3)}; 1-2-syllable-side: {len(lt3)}; bracket-fragment boundaries: {len(bracket)}")
for r in ge3[:10]: print("  GE3",r)
for r in lt3[:10]: print("  LT3",r)
for r in bracket[:10]: print("  BR",r)
# --- 2. rendered-line scan ---
def texts(path):
    tree=ET.parse(path); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'):
            out.append((float(el.get('x')), float(el.get('y')), ''.join(el.itertext())))
    return out
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
tot_pairs=0
for i,p in enumerate(pages,1):
    nodes=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg")
    # columns by x clustering: sort unique x, split on gaps>150
    xs=sorted(set(x for x,y,t in nodes))
    bounds=[]; start=xs[0]; prev=xs[0]
    for x in xs[1:]:
        if x-prev>150: bounds.append((start,prev)); start=x
        prev=x
    bounds.append((start,prev))
    def col(x):
        for ci,(lo,hi) in enumerate(bounds):
            if lo-1<=x<=hi+1: return ci
        return -1
    groups=defaultdict(list)
    for x,y,t in nodes: groups[col(x)].append((y,t))
    pairs=0; f_start=0; f_end=0; ex=[]
    for ci,lst in groups.items():
        lst.sort()
        for (y1,t1),(y2,t2) in zip(lst,lst[1:]):
            dy=y2-y1
            if 10<=dy<=45:
                pairs+=1
                if t2 and t2[0] in NO_START: f_start+=1; ex.append(('START',y2,t2[:30]))
                if t1 and t1[-1] in NO_END: f_end+=1; ex.append(('END',y1,t1[:30]))
    print(f"p{i}: x-clusters={bounds} pairs(10-45px)={pairs} start-flags={f_start} end-flags={f_end} {ex[:3]}")
    tot_pairs+=pairs
print(f"TOTAL rendered pairs: {tot_pairs}")
# --- 3. Japanese line-start scan (all nodes, task set) ---
print("--- JP line-start scan ---")
for i,p in enumerate(pages,1):
    nodes=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg")
    flags=[(y,t[:40]) for x,y,t in nodes if t and t[0] in JP_START]
    print(f"p{i}: flags={len(flags)} {flags[:5]}")
