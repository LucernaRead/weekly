import glob, os, re, collections
from xml.etree import ElementTree as ET
S="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhtw-core/svg"
D="/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zhtw-core-reproof"
def texts_of(f):
    tree=ET.parse(f); out=[]
    for el in tree.iter():
        if el.tag.endswith('text'):
            out.append((''.join(el.itertext()), el.get('x'), el.get('y'), el.get('font-size'), el.get('text-anchor'), el.get('font-family'), el.get('font-weight')))
    return out
# 1. OpenCC s2t over final SVG text nodes
from opencc import OpenCC
cc=OpenCC('s2t')
diffs=collections.Counter(); examples=collections.defaultdict(list)
simp_only=set()
for f in sorted(glob.glob(S+"/*.svg")):
    for t,*_ in texts_of(f):
        conv=cc.convert(t)
        if conv!=t:
            for a,b in zip(t,conv):
                if a!=b:
                    diffs[(a,b)]+=1
                    if len(examples[(a,b)])<3: examples[(a,b)].append((os.path.basename(f),t[:40]))
print("S2T diffs total:", sum(diffs.values()))
for k,v in diffs.most_common(): print("  ",k,v,examples[k][:1])
# Simplified-only scan: chars that s2t would NOT change but are simplified-only forms.
# Practical check used by KIT: chars in text that differ under s2t->t2s roundtrip? Instead: list all CJK chars present and flag known simplified-only set.
# Known simplified-only chars (common): 为发对会干并汉龙发 etc are ambiguous; use strict list of chars with no traditional counterpart usage in TW text:
strict_simp = set("为发对会干并汉龙发头长车门马风飞行见贝见车龙龟发发")
# Instead do proper check: convert text s2t, then t2s back; chars that survive s2t unchanged but change under a second mapping are variants, not simplified-only.
# Report: chars changed by s2t are the variants; remaining text after s2t should contain no char from a curated simplified-only list:
curated = set(list("简体独用字") )  # placeholder, replaced below
# Curated simplified-only characters (not used in Traditional at all):
curated = set("为会发对干并汉龙头长车门马风飞见贝车龟发简体显亲爱国学书画话语请诸课读让认说讲设许论识词诚详译试诗诚访证评读课谢谅谦讲论设访译试诗评")
# NOTE: many of those ARE traditional too (e.g. 说? no). This curated approach is unreliable; use instead: s2t output vs input diff is the variant set; simplified-only = chars present in input that OpenCC t2s would produce from traditional? Skip: rely on diff inventory + manual list below.
print("S2T variant pairs (full inventory above).")
# 2. Kinsoku for Chinese: line-start closers 、，。．！？：；）」』】》… and line-end openers （「『【《〈
NO_START=set("、，。．！？：；）」』】》…·")
NO_END=set("（「『【《〈")
ls_hits=[]; le_hits=[]
for f in sorted(glob.glob(S+"/*.svg")):
    for t,*_ in texts_of(f):
        s=t.strip()
        if s and s[0] in NO_START: ls_hits.append((os.path.basename(f),s[:30]))
        if s and s[-1] in NO_END: le_hits.append((os.path.basename(f),s[:30]))
print("KINSOKU line-start closer violations:", len(ls_hits), ls_hits[:10])
print("KINSOKU line-end opener violations:", len(le_hits), le_hits[:10])
# ASCII line-start closers
ah=[]
for f in sorted(glob.glob(S+"/*.svg")):
    for t,*_ in texts_of(f):
        s=t.lstrip()
        if s and s[0] in ").,!?%:;\"'": ah.append((os.path.basename(f),s[:30]))
print("ASCII line-start hits:", len(ah), ah[:10])
# 3. Same-baseline ink collision, TC font index 3
from PIL import ImageFont
def load(bold, size):
    path="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
    try: return ImageFont.truetype(path, size, index=3)
    except Exception: return ImageFont.truetype(path, size)
tot=0
for f in sorted(glob.glob(S+"/*.svg")):
    nodes=[]
    for t,x,y,fs,ta,fam,w in texts_of(f):
        if not t.strip(): continue
        try: yy=float(y); xx=float(x)
        except: continue
        try: size=float(fs) if fs else 28
        except: size=28
        anchor=ta or 'start'
        bold=('Bold' in (fam or '')) or (w in ('bold','700'))
        font=load(bold, int(round(size)))
        try:
            l,top,r,bot=font.getbbox(t); wd=r-l
        except Exception:
            wd=font.getlength(t)
        if anchor=='middle': x0,x1=xx-wd/2,xx+wd/2
        elif anchor=='end': x0,x1=xx-wd,xx
        else: x0,x1=xx,xx+wd
        nodes.append((round(yy,1),x0,x1,t[:40]))
    from collections import defaultdict
    byy=defaultdict(list)
    for y,x0,x1,t in nodes: byy[y].append((x0,x1,t))
    coll=[]
    for y,items in byy.items():
        items.sort()
        for a,b in zip(items,items[1:]):
            if b[0] < a[1]-2: coll.append((y,a,b))
    print(os.path.basename(f),"same-baseline collisions:",len(coll), coll[:5])
    tot+=len(coll)
print("TOTAL same-baseline collisions:", tot)
# 4. Politics / red-line scan over flat text
flat=""
for f in sorted(glob.glob(S+"/*.svg")):
    for t,*_ in texts_of(f): flat+=t
flat_ns=re.sub(r'\s+','',flat)
terms=["烏克蘭","俄羅斯","戰爭","以色列","巴勒斯坦","地緣","兩岸","統一","台獨","選舉","政黨","民進黨","國民黨","民眾黨","共產黨","中央政府","特區政府","五年規劃","五中全會","人大","政協","習近平","賴清德","總統大選"]
for term in terms:
    c=flat_ns.count(term)
    if c: print("REDLINE term hit:", term, c)
print("Redline scan done (unlisted terms = 0).")
# 5. Simplified-only audit via t2s: a char is simplified-only if it appears in input and OpenCC t2s->s2t roundtrip changes it? 
# Direct approach: use opencc t2s on the s2t output: if s2t output differs from input only by variant pairs listed, and no other char classes, then zero simplified-only.
# Additionally scan for a hard list of characters that are simplified forms never used in Traditional Chinese text:
hard_simp = "为发对会干并汉龙头长车门马风飞见贝龟简显亲爱国学书画话语请诸课读让认说讲设许论识词诚详译试诗访证评谢谅谦"
# NOTE: several of these (e.g. 说? not in list) — restrict to chars that are unambiguously simplified-only in TW usage:
hard_simp = set("为发对干并汉龙龟简显亲爱书画话语诸让认说讲设许论识词诚详译试诗访证评谢谅谦")
hits={}
for ch in hard_simp:
    c=flat_ns.count(ch)
    if c: hits[ch]=c
print("Hard simplified-only char hits (curated unambiguous set):", hits)
