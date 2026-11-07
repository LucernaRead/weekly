#!/usr/bin/env python3
"""Round 4 independent geometry/contrast/multiset analysis for RU P7.
Reads ONLY final artifacts + pre-fix copies; edits nothing."""
import json, math, os, re, sys
from collections import Counter
import xml.etree.ElementTree as ET

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
GATE = os.path.join(BASE, "hidden_files/w46/zh-cn-proofread-gates-round4")
FINAL = os.path.join(BASE, "files/weekly-report-w46-zh-cn-ru/svg/p7-ciyu.svg")
PREF = os.path.join(BASE, "hidden_files/w46/zh-cn-fix-round4/p7-ciyu-before.svg")
CARD = os.path.join(BASE, "files/weekly-report-w46-zh-cn-ru/cards/p7-ciyu.png")

def local(tag): return tag.split('}', 1)[-1]

def parse(path):
    tree = ET.parse(path)
    root = tree.getroot()
    els = []
    for el in root.iter():
        text = "".join(el.itertext()) if local(el.tag) == "text" else ""
        els.append({"tag": local(el.tag), "attrs": dict(el.attrib), "text": text})
    return els

def sig(e):
    return (e["tag"], tuple(sorted(e["attrs"].items())), e["text"])

final = parse(FINAL); pref = parse(PREF)
print(f"FINAL elements incl root: {len(final)}")
print(f"PREF  elements incl root: {len(pref)}")

diffs = []
for i, (a, b) in enumerate(zip(pref, final)):
    if sig(a) != sig(b):
        diffs.append((i, a, b))
if len(pref) != len(final):
    print(f"COUNT MISMATCH pref={len(pref)} final={len(final)}")
print(f"DIFFERING ELEMENT INDICES (document order, root=0): {[d[0] for d in diffs]}")
for i, a, b in diffs:
    print(f"--- idx {i} ---")
    print(f"  PRE : {a}")
    print(f"  POST: {b}")
    # attribute-level diff
    for k in sorted(set(a["attrs"]) | set(b["attrs"])):
        if a["attrs"].get(k) != b["attrs"].get(k):
            print(f"    attr {k}: {a['attrs'].get(k)!r} -> {b['attrs'].get(k)!r}")
    if a["text"] != b["text"]:
        print(f"    TEXT: {a['text']!r} -> {b['text']!r}")

# Identify band / footer in FINAL by attributes (not by index assumption)
def find(pred, els, label):
    hits = [(i, e) for i, e in enumerate(els) if pred(e)]
    print(f"{label}: {[(i, e['attrs'], e['text'][:60]) for i, e in hits]}")
    return hits

band = find(lambda e: e["tag"]=="rect" and e["attrs"].get("fill")=="#2c2822" and float(e["attrs"].get("width","0"))==1820, final, "BAND candidates")
band_pre = find(lambda e: e["tag"]=="rect" and e["attrs"].get("fill")=="#2c2822" and float(e["attrs"].get("width","0"))==1820, pref, "BAND pre-fix")
assert len(band)==1 and len(band_pre)==1
bi, band_el = band[0]
band_y = float(band_el["attrs"]["y"]); band_h = float(band_el["attrs"]["height"])
band_bottom = band_y + band_h
print(f"BAND final: idx={bi} x={band_el['attrs']['x']} y={band_y} w={band_el['attrs']['width']} h={band_h} fill={band_el['attrs']['fill']} bottom={band_bottom}")
print(f"BAND pre  : y={band_pre[0][1]['attrs']['y']} bottom={float(band_pre[0][1]['attrs']['y'])+float(band_pre[0][1]['attrs']['height'])} dy={band_y-float(band_pre[0][1]['attrs']['y'])}")

# Teaser lines: the two text elements immediately after band in document order
for j in (bi+1, bi+2):
    e = final[j]; pe = pref[j]
    print(f"TEASER idx {j}: final y={e['attrs'].get('y')} fill={e['attrs'].get('fill')} offset_from_band_top={float(e['attrs']['y'])-band_y} | pre y={pe['attrs'].get('y')} offset={float(pe['attrs']['y'])-float(band_pre[0][1]['attrs']['y'])} | text={e['text']!r}")
    print(f"   dy vs pre: {float(e['attrs']['y'])-float(pe['attrs']['y'])}")

# Footer rule + texts
rule = find(lambda e: e["tag"]=="line" and e["attrs"].get("y1")=="2580", final, "FOOTER RULE")
foot = find(lambda e: e["tag"]=="text" and e["attrs"].get("y")=="2624" and e["attrs"].get("fill")=="#57523f", final, "FOOTER TEXTS")
foot_pre = find(lambda e: e["tag"]=="text" and e["attrs"].get("y")=="2624", pref, "FOOTER TEXTS pre")
rule_y = float(rule[0][1]["attrs"]["y1"]) if rule else None
print(f"FOOTER rule y={rule_y}, band_bottom={band_bottom}, rule_minus_bandbottom={rule_y-band_bottom if rule_y else None}")
print(f"Band bottom <=2570 ? {band_bottom<=2570}; band bottom below rule? {band_bottom<rule_y}")

# ---- font-metric ink boxes (own implementation, same font files as tables.json) ----
sys.path.insert(0, os.path.join(BASE, "tools"))
import tables as T
FONTS = T.load()["fonts"]; FACE_INDEX = FONTS["face_index"]; SCALE=4
from PIL import ImageFont
_cache={}
def get_font(family, size, bold):
    fam = family or "Noto Sans CJK SC"
    serif = "Serif" in fam
    suffix = fam.strip().split()[-1] if fam.strip().split() else "SC"
    index = FACE_INDEX.get(suffix, FACE_INDEX["SC"])
    path = (FONTS["serif_bold"] if bold else FONTS["serif_regular"]) if serif else (FONTS["sans_bold"] if bold else FONTS["sans_regular"])
    px = max(1, int(round(size*SCALE))); key=(path,index,px)
    if key not in _cache: _cache[key]=ImageFont.truetype(path, px, index=index)
    return _cache[key]
def ink_box(text, family, size, bold, x, y, anchor="start"):
    f = get_font(family, size, bold)
    adv = f.getlength(text)/SCALE
    l,t,r,b = [v/SCALE for v in f.getbbox(text)]
    ascent = f.getmetrics()[0]/SCALE
    if anchor=="end": left=x-adv+l; right=x-adv+r
    elif anchor=="middle": left=x-adv/2+l; right=x-adv/2+r
    else: left=x+l; right=x+r
    return (left, y-ascent+t, right, y-ascent+b)

for i,e in foot:
    size=float(e["attrs"]["font-size"]); fam=e["attrs"].get("font-family","")
    bold=e["attrs"].get("font-weight","") in ("700","bold")
    box=ink_box(e["text"], fam, size, bold, float(e["attrs"]["x"]), float(e["attrs"]["y"]), e["attrs"].get("text-anchor","start"))
    print(f"FOOTER idx {i}: font-size={size} family={fam} ink_box={tuple(round(v,2) for v in box)} ink_top={box[1]:.2f} ink_bottom={box[3]:.2f} gap_bandbottom_to_inktop={box[1]-band_bottom:.2f}")
    print(f"   text={e['text']!r}")

# Teaser ink boxes (confirm on band, light fills)
for j in (bi+1, bi+2):
    e=final[j]; size=float(e["attrs"]["font-size"])
    box=ink_box(e["text"], e["attrs"].get("font-family",""), size, e["attrs"].get("font-weight","") in ("700","bold"), float(e["attrs"]["x"]), float(e["attrs"]["y"]), e["attrs"].get("text-anchor","start"))
    print(f"TEASER idx {j} ink_box={tuple(round(v,2) for v in box)} inside_band_y={band_y}..{band_bottom} ? top>={band_y}={box[1]>=band_y} bottom<={band_bottom}={box[3]<=band_bottom}")

# Last content above band: all text elements (excluding band-adjacent teaser) with baseline < band top, ink bottom max
cands=[]
for i,e in enumerate(final):
    if e["tag"]!="text": continue
    if i in (bi+1, bi+2): continue
    y=float(e["attrs"]["y"])
    if y>=band_y: continue
    if not e["text"].strip(): continue
    size=float(e["attrs"].get("font-size","20"))
    box=ink_box(e["text"], e["attrs"].get("font-family",""), size, e["attrs"].get("font-weight","") in ("700","bold"), float(e["attrs"]["x"]), y, e["attrs"].get("text-anchor","start"))
    cands.append((box[3], box[1], i, y, e["text"][:50], box))
cands.sort(reverse=True)
print("TOP 5 ink-bottoms above band (ink_bottom, ink_top, idx, baseline, text):")
for c in cands[:5]: print(f"  {c[0]:.2f} top={c[1]:.2f} idx={c[2]} baseline={c[3]} text={c[4]!r} box={tuple(round(v,2) for v in c[5])}")
print(f"MAX ink bottom above band = {cands[0][0]:.2f}; clearance to band top = {band_y-cands[0][0]:.2f} px (must be >0)")

# ---- contrast WCAG ----
def lum(hexs):
    hexs=hexs.lstrip('#'); r,g,b=[int(hexs[i:i+2],16)/255 for i in (0,2,4)]
    def f(c): return c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    r,g,b=f(r),f(g),f(b); return 0.2126*r+0.7152*g+0.0722*b
def contrast(a,b):
    la,lb=lum(a),lum(b); hi,lo=max(la,lb),min(la,lb); return (hi+0.05)/(lo+0.05)
for fg,bg,label in [("#57523f","#f7f1e2","footer on paper"),("#57523f","#2c2822","footer on band (pre-fix bg)"),("#e8dfc8","#2c2822","teaser title on band"),("#f3edda","#2c2822","teaser sentence on band")]:
    print(f"CONTRAST {label}: {fg} on {bg} = {contrast(fg,bg):.2f}:1 (WCAG >=4.5 required for footer)")

# Paper fill: root background rect
print(f"PAPER bg rect: {final[1]}")

# ---- text multiset diff ----
def multiset(els): return Counter(e["text"] for e in els if e["tag"]=="text")
mc_pre, mc_fin = multiset(pref), multiset(final)
print(f"TEXT nodes: pre={sum(mc_pre.values())} final={sum(mc_fin.values())}")
print(f"  before-only: {dict((mc_pre-mc_fin))}")
print(f"  after-only : {dict((mc_fin-mc_pre))}")
print(f"  changed strings: {sum((mc_pre-mc_fin).values())+sum((mc_fin-mc_pre).values())}")

# Stem / key checks in final P7
stem="我拿了___包裹。"; old="我拿了一个___包裹。"
alltext="".join(e["text"] for e in final if e["tag"]=="text")
print(f"STEM new count in P7 SVG text nodes: {sum(1 for e in final if e['tag']=='text' and e['text']==stem)} (exact-node); substring count={alltext.count(stem)}; old stem substring={alltext.count(old)}")
print(f"DOUBLED '我拿了一个个包裹' count={alltext.count('我拿了一个个包裹')}")

# Save structured summary
summary={"n_elements_final":len(final),"n_elements_pre":len(pref),
 "diff_indices":[d[0] for d in diffs],
 "band":{"idx":bi,"y":band_y,"h":band_h,"bottom":band_bottom},
 "band_pre_y":float(band_pre[0][1]['attrs']['y']),
 "rule_y":rule_y,
 "footer_ink_tops":[round(ink_box(e['text'],e['attrs'].get('font-family',''),float(e['attrs']['font-size']),e['attrs'].get('font-weight','') in ('700','bold'),float(e['attrs']['x']),float(e['attrs']['y']),e['attrs'].get('text-anchor','start'))[1],2) for _,e in foot],
 "max_ink_bottom_above_band":round(cands[0][0],2),
 "clearance_above_band":round(band_y-cands[0][0],2),
 "contrast_footer_on_paper":round(contrast("#57523f","#f7f1e2"),2),
 "contrast_footer_on_band":round(contrast("#57523f","#2c2822"),2),
 "multiset_before_only":dict(mc_pre-mc_fin),"multiset_after_only":dict(mc_fin-mc_pre),
 "text_node_count_pre":sum(mc_pre.values()),"text_node_count_final":sum(mc_fin.values())}
json.dump(summary, open(os.path.join(GATE,"geometry-contrast-r4.json"),"w"), ensure_ascii=False, indent=1)
print("WROTE geometry-contrast-r4.json")

# ---- rendered-pixel measurement from the card PNG (1:1 with SVG coords) ----
from PIL import Image
im=Image.open(CARD).convert("RGB"); W,H=im.size
print(f"CARD PNG size {W}x{H} (SVG 1950x2700, scale {W/1950:.3f}x{H/2700:.3f})")
px=im.load()
def is_band(c): return c==(44,40,34)
def is_paper(c): return c==(247,241,226)
# Band extent: column x=1000, scan y 2300..2700 for band colour
band_rows=[y for y in range(2300,2700) if is_band(px[1000,y])]
print(f"PIXEL band at x=1000: first={min(band_rows) if band_rows else None} last={max(band_rows) if band_rows else None} count={len(band_rows)}")
# Footer ink rows: scan y 2560..2700, x 65..1885, pixels close to footer fill (dark, not paper, not gold, not band, not border black)
# Footer ink approx #57523f = (87,82,63). Accept pixels with R 60..115, G 55..110, B 40..90 and R>G>B-ish, excluding band colour.
def is_footer_ink(c):
    r,g,b=c
    return 55<=r<=120 and 50<=g<=115 and 35<=b<=95 and r>=g>=b and c!=(44,40,34)
ink_rows={}
for y in range(2560,2700):
    n=sum(1 for x in range(65,1886) if is_footer_ink(px[x,y]))
    if n>0: ink_rows[y]=n
if ink_rows:
    print(f"PIXEL footer ink rows: first={min(ink_rows)} last={max(ink_rows)} per-row counts first5={list(ink_rows.items())[:5]}")
    print(f"PIXEL gap: band_last={max(band_rows)} -> footer_ink_first={min(ink_rows)} = {min(ink_rows)-max(band_rows)} px (rows strictly between, exclusive of band last row)")
    # rows between band bottom and footer ink: what colours dominate?
    for y in range(max(band_rows)+1, min(ink_rows)):
        from collections import Counter as C
        cnt=C(px[x,y] for x in range(65,1886))
        print(f"  row y={y} top colours: {cnt.most_common(3)}")
# Gold rule row: pixels #b3a06a (179,160,106) near y 2580
gold_rows=[y for y in range(2550,2620) if sum(1 for x in range(65,1886) if px[x,y]==(179,160,106))>100]
print(f"PIXEL gold-rule rows (>100 gold px): {gold_rows}")
# Check any footer-ink pixel ON band rows (y <= band last): should be 0 below? count
onband=sum(1 for y in band_rows for x in range(65,1886) if is_footer_ink(px[x,y]))
print(f"PIXEL footer-ink pixels inside band rows: {onband} (must be 0; teaser light text excluded by colour test)")
json.dump({"png_size":[W,H],"band_rows":[min(band_rows),max(band_rows)],"footer_ink_rows":[min(ink_rows),max(ink_rows)] if ink_rows else None,"gold_rows":gold_rows,"footer_ink_on_band_px":onband}, open(os.path.join(GATE,"pixel-measurement-r4.json"),"w"), indent=1)
print("WROTE pixel-measurement-r4.json")
