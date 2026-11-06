#!/usr/bin/env python3
# Independent IT x NL W45 proofread measurements. Own parser + PIL metrics;
# does NOT import tools/occlusion_audit, freeze or p8 (cross-checks them).
import html, json, math, os, re, sys
from collections import Counter, defaultdict
from PIL import ImageFont

D = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = D + "/files/weekly-report-w45-it-nl"
CO = D + "/files/weekly-report-w45-it-core"
W43 = D + "/files/weekly-report-it-nl"
EDB = D + "/hidden_files/weekly-report-w45-it-nl-build"
COB = D + "/hidden_files/weekly-report-w45-it-build"
SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIFB = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SANSB = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
BLACK = os.path.expanduser("~/.local/share/fonts/UnifrakturMaguntia.ttf")
FACE = {"HK": 4, "JP": 0, "KR": 1, "SC": 2, "TC": 3}
_cache = {}
SCALE = 4

def resolve(fam, bold):
    fam = fam or "Noto Sans CJK SC"
    if "Unifraktur" in fam: return (BLACK, 0)
    serif = "Serif" in fam
    suf = fam.strip().split()[-1] if fam.strip().split() else "SC"
    idx = FACE.get(suf, 2)
    if serif: return (SERIFB if bold else SERIF, idx)
    return (SANSB if bold else SANS, idx)

def font(fam, size, bold):
    p, idx = resolve(fam, bold)
    px = max(1, int(round(size * SCALE)))
    k = (p, idx, px)
    if k not in _cache: _cache[k] = ImageFont.truetype(p, px, index=idx)
    return _cache[k]

def fnum(a, n, d=0.0):
    try: return float(a.get(n, d))
    except: return d

ATTR = re.compile(r'([\w-]+)="([^"]*)"')
TAG = re.compile(r"<text\b([^>]*)>(.*?)</text>|<(rect|line|image|circle|path)\b([^>]*?)/?>", re.S)

def parse(path):
    s = open(path, encoding="utf-8").read()
    els = []
    for i, m in enumerate(TAG.finditer(s)):
        if m.group(1) is not None:
            a = dict(ATTR.findall(m.group(1)))
            t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
            els.append({"kind": "text", "idx": i, "a": a, "text": t})
        else:
            els.append({"kind": m.group(3), "idx": i, "a": dict(ATTR.findall(m.group(4))), "text": None})
    return els, s

def ink(el):
    a, t = el["a"], el["text"]
    if not t or not t.strip(): return None
    size = fnum(a, "font-size", 20.0); bold = a.get("font-weight", "") in ("700", "bold")
    sp = fnum(a, "letter-spacing", 0.0)
    f = font(a.get("font-family", ""), size, bold)
    adv = f.getlength(t) / SCALE + (sp * (len(t) - 1) if sp else 0.0)
    l, tt, r, b = [v / SCALE for v in f.getbbox(t)]
    asc = f.getmetrics()[0] / SCALE
    x, y = fnum(a, "x"), fnum(a, "y"); anc = a.get("text-anchor", "start")
    if anc == "middle": left, right = x - adv/2 + l, x - adv/2 + r
    elif anc == "end": left, right = x - adv + l, x - adv + r
    else: left, right = x + l, x + r
    return (left, y - asc + tt, right, y - asc + b, adv)

def adv_right(el):
    a, t = el["a"], el["text"]
    if not t or not t.strip(): return None
    size = fnum(a, "font-size", 20.0); bold = a.get("font-weight", "") in ("700", "bold")
    sp = fnum(a, "letter-spacing", 0.0)
    f = font(a.get("font-family", ""), size, bold)
    adv = f.getlength(t) / SCALE + (sp * (len(t) - 1) if sp else 0.0)
    x = fnum(a, "x"); anc = a.get("text-anchor", "start")
    if anc == "middle": return x + adv/2
    if anc == "end": return x
    return x + adv

def shape_box(el):
    a = el["a"]
    if el["kind"] == "rect":
        x, y, w, h = fnum(a, "x"), fnum(a, "y"), fnum(a, "width"), fnum(a, "height")
        sw = fnum(a, "stroke-width", 0.0)/2 if a.get("stroke") not in (None, "none") else 0.0
        return (x-sw, y-sw, x+w+sw, y+h+sw)
    if el["kind"] == "image":
        return (fnum(a, "x"), fnum(a, "y"), fnum(a, "x")+fnum(a, "width"), fnum(a, "y")+fnum(a, "height"))
    if el["kind"] == "circle":
        cx, cy, r = fnum(a, "cx"), fnum(a, "cy"), fnum(a, "r"); return (cx-r, cy-r, cx+r, cy+r)
    if el["kind"] == "line":
        x1, y1, x2, y2 = fnum(a, "x1"), fnum(a, "y1"), fnum(a, "x2"), fnum(a, "y2")
        e = fnum(a, "stroke-width", 1.0)/2
        return (min(x1,x2)-e, min(y1,y2)-e, max(x1,x2)+e, max(y1,y2)+e)
    if el["kind"] == "path":
        # own proper walker (absolute+relative, M/L/H/V/C/S/Q/T/A/Z)
        d = a.get("d", ""); pts = []; cx = cy = sx = sy = 0.0
        toks = re.findall(r"([MmLlHhVvCcSsQqTtAaZz])|(-?\d*\.?\d+(?:[eE]-?\d+)?)", d)
        # simpler: tokenise commands+numbers in order
        seq = re.findall(r"[MmLlHhVvCcSsQqTtAaZz]|-?\d*\.?\d+(?:[eE]-?\d+)?", d)
        cmd = None; nums = []
        def flush():
            nonlocal cx, cy, sx, sy, nums
            if cmd is None: return
            up = cmd.upper(); rel = cmd.islower(); i = 0
            if up == "Z": cx, cy = sx, sy; return
            if up == "M" and len(nums) >= 2:
                x, y = nums[0], nums[1]; cx, cy = (cx+x, cy+y) if rel else (x, y); sx, sy = cx, cy; pts.append((cx, cy)); i = 2; up = "L"
            while i < len(nums):
                if up == "L" and i+1 < len(nums):
                    x, y = nums[i], nums[i+1]; cx, cy = (cx+x, cy+y) if rel else (x, y); pts.append((cx, cy)); i += 2
                elif up == "H" and i < len(nums):
                    x = nums[i]; cx = cx+x if rel else x; pts.append((cx, cy)); i += 1
                elif up == "V" and i < len(nums):
                    y = nums[i]; cy = cy+y if rel else y; pts.append((cx, cy)); i += 1
                elif up == "C" and i+5 < len(nums):
                    pr = [(nums[i],nums[i+1]),(nums[i+2],nums[i+3]),(nums[i+4],nums[i+5])]
                    for (x,y) in pr: pts.append((cx+x, cy+y) if rel else (x,y))
                    cx, cy = pts[-1]; i += 6
                elif up in ("S","Q") and i+3 < len(nums):
                    pr = [(nums[i],nums[i+1]),(nums[i+2],nums[i+3])]
                    for (x,y) in pr: pts.append((cx+x, cy+y) if rel else (x,y))
                    cx, cy = pts[-1]; i += 4
                elif up == "T" and i+1 < len(nums):
                    x, y = nums[i], nums[i+1]; cx, cy = (cx+x, cy+y) if rel else (x,y); pts.append((cx, cy)); i += 2
                elif up == "A" and i+6 < len(nums):
                    x, y = nums[i+5], nums[i+6]; cx, cy = (cx+x, cy+y) if rel else (x,y); pts.append((cx, cy)); i += 7
                else: break
        for tok in seq:
            if tok.isalpha() and len(tok) == 1 and tok in "MmLlHhVvCcSsQqTtAaZz":
                flush(); cmd = tok; nums = []
            else:
                try: nums.append(float(tok))
                except: pass
        flush()
        if not pts: return None
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        e = fnum(a, "stroke-width", 0.0)/2
        return (min(xs)-e, min(ys)-e, max(xs)+e, max(ys)+e)
    return None

def ov_area(a, b):
    l, t = max(a[0], b[0]), max(a[1], b[1]); r, bo = min(a[2], b[2]), min(a[3], b[3])
    if r <= l or bo <= t: return 0.0, 0.0, 0.0
    return (r-l)*(bo-t), r-l, bo-t

def texts_of(d, fn):
    els, _ = parse(os.path.join(d, "svg", fn))
    return els

def joined(d):
    out = {}
    for fn in sorted(os.listdir(os.path.join(d, "svg"))):
        if fn.endswith(".svg"):
            els, _ = parse(os.path.join(d, "svg", fn))
            out[fn] = " ".join(e["text"] for e in els if e["kind"] == "text")
    return out

def P(s): print(s, flush=True)

# ============ §A masthead geometry ============
def masthead(d, label):
    P(f"\n===== §A MASTHEAD {label} =====")
    els, _ = parse(os.path.join(d, "svg", "p1-prima.svg"))
    for e in els:
        if e["kind"] != "text": continue
        y = fnum(e["a"], "y")
        if y <= 700:
            P(f"  y={y} x={fnum(e['a'],'x')} size={e['a'].get('font-size')} w={e['a'].get('font-weight')} anchor={e['a'].get('text-anchor')} fam={e['a'].get('font-family')} :: {e['text']!r}")
    # all rects/lines in masthead band
    for e in els:
        if e["kind"] in ("rect", "line"):
            y = fnum(e["a"], "y", fnum(e["a"], "y1", 99999))
            if y <= 700:
                P(f"  [{e['kind']}] {e['a']}")

masthead(CO, "W45 CORE p1")
masthead(ED, "W45 ITxNL p1")
masthead(W43, "W43 ITxNL p1")
for sib, fn in [("W45 ITxEN", "weekly-report-w45-it-en"), ("W45 ITxDE", "weekly-report-w45-it-de"),
                ("W45 ITxFR", "weekly-report-w45-it-fr"), ("W45 ITxPT", "weekly-report-w45-it-pt")]:
    p = D + "/files/" + fn
    if os.path.isdir(p):
        P(f"\n--- sibling {sib} p1 masthead (y 300..700) ---")
        els, _ = parse(os.path.join(p, "svg", "p1-prima.svg"))
        for e in els:
            if e["kind"] == "text" and 300 <= fnum(e["a"], "y") <= 700:
                P(f"  y={fnum(e['a'],'y')} x={fnum(e['a'],'x')} size={e['a'].get('font-size')} w={e['a'].get('font-weight')} anchor={e['a'].get('text-anchor')} :: {e['text']!r}")

# ============ §B right-edge ADVANCE, full ============
def rightedge(d, label):
    P(f"\n===== §B RIGHT-EDGE ADVANCE {label} (FULL) =====")
    viol, marg = [], []
    for fn in sorted(os.listdir(os.path.join(d, "svg"))):
        if not fn.endswith(".svg"): continue
        els, _ = parse(os.path.join(d, "svg", fn))
        for e in els:
            if e["kind"] != "text": continue
            r = adv_right(e)
            if r is None: continue
            y = fnum(e["a"], "y")
            if r > 1910: viol.append((fn, y, round(r, 1), e["text"]))
            elif r > 1885: marg.append((fn, y, round(r, 1), e["text"]))
    P(f"  violations(>1910): {len(viol)}")
    for v in viol: P(f"    VIOL {v}")
    P(f"  margin-zone(1885,1910]: {len(marg)}")
    for v in marg: P(f"    MARG {v}")
    return viol, marg
rightedge(CO, "CORE"); rightedge(ED, "EDITION")

# ============ §C same-baseline pairs ============
def rowcheck(d, label):
    P(f"\n===== §C SAME-BASELINE pairs gap<10px {label} (FULL) =====")
    for fn in sorted(os.listdir(os.path.join(d, "svg"))):
        if not fn.endswith(".svg"): continue
        els, _ = parse(os.path.join(d, "svg", fn))
        byy = defaultdict(list)
        for e in els:
            if e["kind"] != "text": continue
            b = ink(e)
            if b: byy[fnum(e["a"], "y")].append((b[0], b[2], e["text"]))
        for y in sorted(byy):
            row = sorted(byy[y])
            for (l1, r1, t1), (l2, r2, t2) in zip(row, row[1:]):
                gap = l2 - r1
                if gap < 10:
                    P(f"  {fn} y={y} gap={gap:.1f}: {t1!r} <> {t2!r}")
rowcheck(CO, "CORE"); rowcheck(ED, "EDITION")

# ============ §D independent occlusion (own code, canonical semantics) ============
def indep_occlusion(d, label):
    P(f"\n===== §D INDEPENDENT OCCLUSION {label} (FULL) =====")
    total = Counter(); allf = []
    for fn in sorted(os.listdir(os.path.join(d, "svg"))):
        if not fn.endswith(".svg"): continue
        els, _ = parse(os.path.join(d, "svg", fn))
        for e in els:
            e["box"] = ink(e)[:4] if e["kind"] == "text" else shape_box(e)
        texts = [e for e in els if e["kind"] == "text" and e["box"]]
        shapes = [e for e in els if e["kind"] != "text" and e["box"]]
        for el in texts:
            l, t, r, b = el["box"]; area = max(1.0, (r-l)*(b-t)); bl = fnum(el["a"], "y")
            if l < -0.5 or r > 1950.5 or t < -0.5 or b > 2700.5:
                allf.append((fn, "EDGE", el["text"], el["box"])); total["EDGE"] += 1
            if b > 2580.5 and bl < 2600:
                allf.append((fn, "FOOTER", el["text"], el["box"])); total["FOOTER"] += 1
            for sh in shapes:
                if sh["idx"] <= el["idx"]: continue
                ov, _, _ = ov_area(el["box"], sh["box"])
                if ov <= 0: continue
                thin = sh["kind"] == "line" or (sh["kind"] == "rect" and (fnum(sh["a"], "height") <= 4.5 or fnum(sh["a"], "width") <= 4.5)
                        and (sh["a"].get("fill", "#000") not in ("none", "transparent") or sh["a"].get("stroke") not in (None, "none")))
                opaque = sh["kind"] == "image" or (sh["a"].get("fill", "#000") not in ("none", "transparent") and sh["a"].get("fill-opacity") != "0" and sh["a"].get("opacity") != "0")
                if thin:
                    allf.append((fn, "LINEX", el["text"], sh["box"])); total["LINEX"] += 1
                elif opaque and ov/area >= 0.30:
                    allf.append((fn, "COVER", el["text"], (round(ov/area, 3), sh["box"]))); total["COVER"] += 1
        ordered = sorted(texts, key=lambda e: e["box"][1])
        for i, a in enumerate(ordered):
            for bb in ordered[i+1:]:
                if bb["box"][1] > a["box"][3]: break
                ov, ow, oh = ov_area(a["box"], bb["box"])
                if ov >= 9.0 and ow >= 3.0 and oh >= 3.0:
                    allf.append((fn, "TEXTX", a["text"], f"vs {bb['text']!r} {ow:.1f}x{oh:.1f}")); total["TEXTX"] += 1
        rects = [e for e in shapes if e["kind"] == "rect" and (e["a"].get("stroke") not in (None, "none") or e["a"].get("fill") == "#2c2822")
                 and fnum(e["a"], "width") < 1950*0.95 and not (fnum(e["a"], "width") >= 1800 and fnum(e["a"], "height") >= 2500)]
        for el in texts:
            ax, ay = fnum(el["a"], "x"), fnum(el["a"], "y")
            cx, cy = (el["box"][0]+el["box"][2])/2, (el["box"][1]+el["box"][3])/2
            cands = []
            for rc in rects:
                if rc["idx"] >= el["idx"] or el["idx"] - rc["idx"] > 80: continue
                rl, rt, rr, rb = rc["box"]
                if (rl-2 <= ax <= rr+2 and rt-2 <= ay <= rb+2) or (rl <= cx <= rr and rt <= cy <= rb):
                    cands.append((fnum(rc["a"], "width")*fnum(rc["a"], "height"), rc))
            if not cands: continue
            rc = min(cands)[1]
            rl, rt = fnum(rc["a"], "x"), fnum(rc["a"], "y"); rr, rb = rl+fnum(rc["a"], "width"), rt+fnum(rc["a"], "height")
            l, t, r, b = el["box"]; sides = []
            if l < rl-0.5: sides.append(f"left {l:.1f}<{rl:.1f}")
            if r > rr+0.5: sides.append(f"right {r:.1f}>{rr:.1f}")
            if t < rt-0.5: sides.append(f"top {t:.1f}<{rt:.1f}")
            if b > rb+0.5: sides.append(f"bottom {b:.1f}>{rb:.1f}")
            if sides:
                allf.append((fn, "BOXTITLE", el["text"], "; ".join(sides))); total["BOXTITLE"] += 1
    P(f"  total flags: {len(allf)} {dict(total)}")
    for f in allf: P(f"    {f}")
    return allf
indep_occlusion(CO, "CORE"); indep_occlusion(ED, "EDITION")

# ============ §E P6 chart labels: tight-ink + ls-box coverage ============
def chartcheck(d, label):
    P(f"\n===== §E P6 CHART-LABEL coverage {label} (FULL, all >0%) =====")
    els, _ = parse(os.path.join(d, "svg", "p6-approfondimento.svg"))
    for e in els: e["box"] = ink(e)[:4] if e["kind"] == "text" else shape_box(e)
    worst_t, worst_l = 0.0, 0.0; rows = []
    texts = [e for e in els if e["kind"] == "text" and e["box"]]
    for el in texts:
        l, t, r, b = el["box"]; area = max(1.0, (r-l)*(b-t))
        # ls-box: (x, y-ascent, x+adv, y+descent) at 1x
        a = el["a"]; size = fnum(a, "font-size", 20.0); bold = a.get("font-weight", "") in ("700", "bold")
        f1 = font(a.get("font-family", ""), size, bold)  # 4x font; metrics scaled below
        asc, desc = f1.getmetrics()[0]/SCALE, f1.getmetrics()[1]/SCALE
        adv = ink(el)[4]; x, y = fnum(a, "x"), fnum(a, "y"); anc = a.get("text-anchor", "start")
        if anc == "middle": lx, rx = x-adv/2, x+adv/2
        elif anc == "end": lx, rx = x-adv, x
        else: lx, rx = x, x+adv
        lsbox = (lx, y-asc, rx, y+desc); lsarea = max(1.0, (rx-lx)*(desc+asc))
        ct, cl = 0.0, 0.0
        for sh in els:
            if sh["kind"] == "text" or sh["idx"] <= el["idx"] or not sh["box"]: continue
            if sh["kind"] not in ("rect", "image"): continue
            ov, _, _ = ov_area(el["box"], sh["box"]); ct = max(ct, ov/area)
            ov2, _, _ = ov_area(lsbox, sh["box"]); cl = max(cl, ov2/lsarea)
        worst_t = max(worst_t, ct); worst_l = max(worst_l, cl)
        if ct > 0 or cl > 0: rows.append((el["text"], round(ct*100, 2), round(cl*100, 2)))
    P(f"  worst tight-ink coverage: {worst_t*100:.2f}% ; worst ls-box coverage: {worst_l*100:.2f}% (gate <30%)")
    for row in rows: P(f"    {row}")
chartcheck(CO, "CORE"); chartcheck(ED, "EDITION")

# ============ §F P7 word box ============
def p7word(d, label):
    P(f"\n===== §F P7 WORD BOX {label} =====")
    els, _ = parse(os.path.join(d, "svg", "p7-lingua.svg"))
    for e in els: e["box"] = ink(e)[:4] if e["kind"] == "text" else shape_box(e)
    for e in els:
        if e["kind"] == "text" and "assaggio" in e["text"]:
            P(f"  text idx={e['idx']} y={fnum(e['a'],'y')} x={fnum(e['a'],'x')} size={e['a'].get('font-size')} :: {e['text']!r} ink={tuple(round(v,1) for v in e['box'])}")
    # definition sentence: join texts in word-box region (search for the sentence fragments)
    alltxt = " ".join(e["text"] for e in els if e["kind"] == "text")
    for frag in ["è la prova di un cibo", "un piccolo pezzo per decidere", "se piace", "Questa settimana vive a pagina 3", "alla finale del Panettone"]:
        P(f"  frag {frag!r} present: {frag in alltxt}")
    # gloss box rect: rect drawn just before the gloss text node
    gloss_idx = next((e["idx"] for e in els if e["kind"] == "text" and e["text"].startswith("assaggio =")), None)
    if gloss_idx is not None:
        for e in reversed(els[:gloss_idx]):
            if e["kind"] == "rect":
                P(f"  rect before gloss idx={e['idx']} {e['a']} box={tuple(round(v,1) for v in e['box'])}")
                break
        # all texts inside that rect's x-range near gloss: print box + ink bottoms
        g = next(e for e in els if e["idx"] == gloss_idx)
        P(f"  gloss ink bottom: {g['box'][3]:.1f}")
p7word(CO, "CORE"); p7word(ED, "EDITION")
# definition sentence byte comparison (space-joined P7 text, sentence span)
def defsent(d):
    els, _ = parse(os.path.join(d, "svg", "p7-lingua.svg"))
    txt = " ".join(e["text"] for e in els if e["kind"] == "text")
    i = txt.find("« l'assaggio »")
    return txt[i:i+220] if i >= 0 else "NOT-FOUND"
P(f"\n  CORE definition span: {defsent(CO)!r}")
P(f"  ED   definition span: {defsent(ED)!r}")
P(f"  definition spans identical: {defsent(CO) == defsent(ED)}")

# ============ §G golden sentences ============
def golden():
    P("\n===== §G GOLDEN SENTENCES =====")
    ed = joined(ED); co = joined(CO)
    p7 = ed["p7-lingua.svg"]
    # FRASI section: Italian sentences are the P7 texts that also appear in articles;
    # recover by taking P7 texts after the FRASI title and matching against P1-P6 Italian text.
    els, _ = parse(os.path.join(ED, "svg", "p7-lingua.svg"))
    texts = [e["text"] for e in els if e["kind"] == "text"]
    # candidate golden sentences: from core P7 FRASI block — identify via core: sentences
    # printed in P7 that are NOT Dutch notes and NOT titles; use the 8 known from KIT §2/§7 context:
    # instead, derive: take edition P7 texts, strip Dutch "(Pagina N)" tails, keep Italian-looking lines
    # that occur in P1-P6 edition text (article occurrence) — print all such with counts.
    allt_ed = " ".join(ed.values()); allt_co = " ".join(co.values())
    seen = []
    for e in els:
        if e["kind"] != "text": continue
        t = e["text"].strip()
        if not t or "(Pagina" in t or t.startswith(("FRASI", "LA ", "LINGUA", "ERRORI", "Pagina", "La Lucerna")): continue
        # golden sentences are full Italian sentences; test membership in article pages
        if len(t) > 25 and any(ch.isalpha() for ch in t):
            # count occurrences of distinctive core (first 40 chars) in joined texts
            key = t[:40]
            n_ed = allt_ed.count(key); n_co = allt_co.count(key)
            if n_ed >= 1 and ("Pagina" not in t):
                seen.append((t, n_ed, n_co))
    for t, n_ed, n_co in seen: P(f"  cand count_ed={n_ed} count_core={n_co} :: {t!r}")
golden()

# ============ §H gloss from code + SVG verification ============
def gloss_from_code(builddir, label):
    P(f"\n===== §H GLOSS() strings {label} =====")
    total = 0; per = {}
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(builddir, fn)
        if not os.path.exists(p): continue
        s = open(p, encoding="utf-8").read()
        # gloss calls: gloss("...") possibly multiline; find via regex on string literals after 'gloss('
        for m in re.finditer(r"gloss\(\s*\"((?:[^\"\\]|\\.)*)\"", s, re.S):
            g = m.group(1)
            items = [x for x in g.split("·")]
            # page attribution: gloss boxes live P2..P6; infer from file: content12->P2, 34->P3/P4, 56->P5/P6
            pg = {"content12.py": "P2", "content34.py": "P3/P4", "content56.py": "P5/P6"}.get(fn, "?")
            P(f"  {fn} ({pg}) items={len(items)} :: {g!r}")
            total += len(items)
    P(f"  TOTAL gloss items (code): {total}")
    return total
gloss_from_code(COB, "CORE build")
gloss_from_code(EDB, "EDITION build")
# per-page attribution via SVG gloss boxes: P2..P6 each have one 'Uitleg —'/'译注｜' box; count its · items
def gloss_svg(d, label):
    P(f"\n===== §H2 gloss items in rendered SVG {label} =====")
    tot = 0
    for fn, pg in [("p2-vita.svg", "P2"), ("p3-cultura.svg", "P3"), ("p4-sport.svg", "P4"), ("p5-giovani.svg", "P5"), ("p6-approfondimento.svg", "P6")]:
        els, _ = parse(os.path.join(d, "svg", fn))
        # gloss box texts: consecutive texts starting with prefix, joined in paint order
        seq = [e["text"] for e in els if e["kind"] == "text"]
        joined_txt = " ".join(seq)
        # find gloss: the box text contains '=' pairs and '·' separators; take segment from prefix to sentence end '.'
        import re as _re
        m = _re.search(r"(Uitleg — .+?\.)|(译注｜.+?。)", joined_txt)
        seg = m.group(0) if m else "NOT-FOUND"
        n = seg.count("·") + 1 if seg != "NOT-FOUND" else 0
        P(f"  {pg} items={n} :: {seg!r}")
        tot += n
    P(f"  TOTAL gloss items (SVG): {tot}")
gloss_svg(CO, "CORE"); gloss_svg(ED, "EDITION")

# ============ §I P8 printed lines ============
def p8lines(d, label):
    els, _ = parse(os.path.join(d, "svg", "p8-valutazione.svg"))
    seq = [(e["text"], fnum(e["a"], "y")) for e in els if e["kind"] == "text"]
    return seq
def p8keymap(d):
    # group consecutive text nodes by (number) — key lines start with 'N. ' or 'N. ✓'
    els, _ = parse(os.path.join(d, "svg", "p8-valutazione.svg"))
    out = {}
    cur = None
    for e in els:
        if e["kind"] != "text": continue
        t = e["text"]
        m = re.match(r"^(\d+)\.\s", t)
        if m:
            cur = int(m.group(1)); out[cur] = [(t, fnum(e["a"], "y"))]
        elif cur is not None and re.match(r"^(✓|—|plaats|wordt|model|\+ datum)", t):
            out[cur].append((t, fnum(e["a"], "y")))
    return out
P("\n===== §I P8 keydiff table (FULL, tool 17 + #140 + #150) =====")
ck, ek = p8keymap(CO), p8keymap(ED)
for n in [6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 83, 84, 102, 137, 138, 139, 140, 150]:
    P(f"  #{n} CORE: {[t for t, _ in ck.get(n, [])]!r}")
    P(f"  #{n} ED  : {[t for t, _ in ek.get(n, [])]!r}")
P("\n===== §I2 P8 exercise stems 137-140 (E section) =====")
for d, label in [(CO, "CORE"), (ED, "EDITION")]:
    els, _ = parse(os.path.join(d, "svg", "p8-valutazione.svg"))
    seq = [e["text"] for e in els if e["kind"] == "text"]
    txt = " ".join(seq)
    for stem in ["→ ___"]:
        pass
    # print all texts containing '→' 
    P(f"  -- {label} arrow stems --")
    for e in els:
        if e["kind"] == "text" and "→" in e["text"]:
            P(f"    y={fnum(e['a'],'y')} :: {e['text']!r}")
P("\n===== §I3 P8 #139 vs P4 stem byte check =====")
p4ed = " ".join(e["text"] for e in parse(os.path.join(ED, "svg", "p4-sport.svg"))[0] if e["kind"] == "text")
p4co = " ".join(e["text"] for e in parse(os.path.join(CO, "svg", "p4-sport.svg"))[0] if e["kind"] == "text")
P(f"  ED P4 contains 'Domenica sera si gioca Fiorentina–Juventus': {'Domenica sera si gioca Fiorentina–Juventus' in p4ed}")
P(f"  CORE P4 contains it: {'Domenica sera si gioca Fiorentina–Juventus' in p4co}")
P(f"  ED P8 key #139 == that string: {ek.get(139, [['']])[0][0].startswith('139. Domenica sera si gioca Fiorentina–Juventus.')}")

# ============ §J banned term + CJK ============
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
def cjk_scan():
    P("\n===== §J BANNED-TERM + CJK =====")
    for fn in sorted(os.listdir(os.path.join(ED, "svg"))):
        if fn.endswith(".svg"):
            s = open(os.path.join(ED, "svg", fn), encoding="utf-8").read()
            P(f"  SVG {fn}: CJKchars={len(CJK.findall(s))} 桥接={s.count('桥接')}")
    for name, path in [("WEEKLY-KIT.md", ED + "/WEEKLY-KIT.md"), ("ABSTRACT.txt", ED + "/ABSTRACT.txt")]:
        s = open(path, encoding="utf-8").read()
        P(f"  {name}: CJKchars={len(CJK.findall(s))} 桥接={s.count('桥接')} CJKlist={sorted(set(CJK.findall(s)))[:20]}")
    try:
        from pypdf import PdfReader
        for pdf in ["La-Lucerna-VOL2-NL.pdf", "La-Lucerna-VOL2-NL-web.pdf"]:
            r = PdfReader(os.path.join(ED, pdf))
            P(f"  PDF {pdf}: pages={len(r.pages)}")
            for i, pg in enumerate(r.pages):
                t = pg.extract_text() or ""
                P(f"    p{i+1}: CJKchars={len(CJK.findall(t))} 桥接={t.count('桥接')} chars={len(t)}")
    except Exception as ex:
        P(f"  PDF scan failed: {ex!r}")
cjk_scan()

# ============ §K images ============
def images(d, label):
    P(f"\n===== §K IMAGES {label} =====")
    import hashlib
    for fn in sorted(os.listdir(os.path.join(d, "svg"))):
        if not fn.endswith(".svg"): continue
        s = open(os.path.join(d, "svg", fn), encoding="utf-8").read()
        imgs = re.findall(r'<image[^>]*>', s)
        for im in imgs:
            a = dict(ATTR.findall(im))
            href = a.get("xlink:href", a.get("href", ""))
            payload = href.split(",", 1)[1] if "," in href else href
            P(f"  {fn}: x={a.get('x')} y={a.get('y')} w={a.get('width')} h={a.get('height')} payload_sha={hashlib.sha256(payload.encode()).hexdigest()[:16]} payload_len={len(payload)}")
        # credit-ish texts
        els, _ = parse(os.path.join(d, "svg", fn))
        for e in els:
            if e["kind"] == "text" and re.search(r"Wikimedia|Commons|CC0|Public domain|publiek domein|Fotograaf|Bron", e["text"]):
                P(f"    credit-text :: {e['text']!r}")
images(CO, "CORE"); images(ED, "EDITION")

# ============ §L ABSTRACT ============
def abstract():
    P("\n===== §L ABSTRACT =====")
    s = open(os.path.join(ED, "ABSTRACT.txt"), encoding="utf-8").read()
    P(f"  raw: {s!r}")
    P(f"  lines (stripped): {len(s.strip().splitlines())} ; ASCII double-quote present: {'\"' in s}")
    P(f"  contains 'La Lucerna': {'La Lucerna' in s} ; 'Italiaans': {'Italiaans' in s} ; 'A2-B2': {'A2-B2' in s} ; '150': {'150' in s}")
    for kw in ["Panettone", "Torrone", "Serie A", "Forum Cultura", "Italiaans leren"]:
        P(f"  keyword {kw!r}: {kw in s}")
abstract()

# ============ §M flow-end rendered measurements ============
def flowends(d, label):
    P(f"\n===== §M FLOW-END rendered ink {label} =====")
    def maxink(fn, pred):
        els, _ = parse(os.path.join(d, "svg", fn))
        vals = []
        for e in els:
            if e["kind"] != "text": continue
            b = ink(e)
            if b and pred(e, b): vals.append((b[3], fnum(e["a"], "y"), e["text"]))
        return max(vals) if vals else None
    # P1 headline region: y<1830, x in col2? headline flow spans cols; report max ink bottom for y<1828
    P(f"  P1 ink max bottom y<1828: {maxink('p1-prima.svg', lambda e, b: fnum(e['a'], 'y') < 1828)}")
    P(f"  P6-ex ink max bottom (y>1500): {maxink('p6-approfondimento.svg', lambda e, b: fnum(e['a'], 'y') > 1500 and fnum(e['a'], 'y') < 2580)}")
    # P7: FRASI rule line y + col3 ink max bottom above it
    els, _ = parse(os.path.join(d, "svg", "p7-lingua.svg"))
    for e in els:
        if e["kind"] == "line":
            y1, y2 = fnum(e["a"], "y1"), fnum(e["a"], "y2")
            if y1 == y2 and 1600 < y1 < 1800:
                P(f"  P7 rule line: {e['a']}")
    P(f"  P7 col3-region ink max bottom (x>1423? col3 x>=1423, y<1686): {maxink('p7-lingua.svg', lambda e, b: fnum(e['a'], 'x') >= 1423 and b[3] < 1750)}")
    # P7 letter-box bottom vs FRASI: print all P7 texts with y in 1600..1750
    for e in els:
        if e["kind"] == "text" and 1600 <= fnum(e["a"], "y") <= 1760:
            b = ink(e); P(f"    P7 y={fnum(e['a'],'y')} inkbot={b[3]:.1f} :: {e['text']!r}")
    # P8 keys: max ink bottom below y=1332
    P(f"  P8 keys ink max bottom (y>1332, y<2580): {maxink('p8-valutazione.svg', lambda e, b: 1332 < fnum(e['a'], 'y') < 2580)}")
    # P8 footer line y
    els8, _ = parse(os.path.join(d, "svg", "p8-valutazione.svg"))
    for e in els8:
        if e["kind"] == "line":
            y1 = fnum(e["a"], "y1")
            if y1 > 2500: P(f"  P8 line >2500: {e['a']}")
flowends(CO, "CORE"); flowends(ED, "EDITION")

# ============ §N P4 gloss box geometry ============
def p4gloss(d, label):
    P(f"\n===== §N P4 GLOSS BOX {label} =====")
    els, _ = parse(os.path.join(d, "svg", "p4-sport.svg"))
    for e in els: e["box"] = ink(e)[:4] if e["kind"] == "text" else shape_box(e)
    gi = next((e["idx"] for e in els if e["kind"] == "text" and e["text"].startswith(("Uitleg —", "译注｜"))), None)
    P(f"  gloss first-node idx: {gi}")
    if gi is not None:
        for e in reversed(els[:gi]):
            if e["kind"] == "rect":
                P(f"  gloss rect: {e['a']} box={tuple(round(v, 1) for v in e['box'])}"); break
        for e in els:
            if e["kind"] == "text" and e["idx"] >= gi and e["idx"] <= gi + 12:
                P(f"    idx={e['idx']} y={fnum(e['a'],'y')} x={fnum(e['a'],'x')} ink={tuple(round(v,1) for v in e['box'])} :: {e['text']!r}")
        # neighbours: texts whose ink overlaps gloss rect expanded? report texts within 40px of rect
        rect = next(e for e in reversed(els[:gi]) if e["kind"] == "rect")
        rb = rect["box"]
        for e in els:
            if e["kind"] == "text" and e["box"] and e["idx"] < gi:
                ov, _, _ = ov_area(e["box"], rb)
                if ov > 0: P(f"    OVERLAP with earlier text idx={e['idx']} :: {e['text']!r}")
p4gloss(CO, "CORE"); p4gloss(ED, "EDITION")

# ============ §O subtitle widths + footnote ============
def widths():
    P("\n===== §O SUBTITLE / FOOTNOTE widths =====")
    els, _ = parse(os.path.join(ED, "svg", "p1-prima.svg"))
    sub = next((e for e in els if e["kind"] == "text" and "ITALIAANS WEEKBLAD" in e["text"]), None)
    P(f"  ED subtitle node: {sub['a'] if sub else None} :: {sub['text'] if sub else ''!r}")
    if sub:
        fam, bold = sub["a"].get("font-family", ""), sub["a"].get("font-weight", "") in ("700", "bold")
        for size in (46, 44, 43):
            f = font(fam, size, bold); adv = f.getlength(sub["text"]) / SCALE
            P(f"    size {size}: advance={adv:.1f} centred edges {975-adv/2:.1f}..{975+adv/2:.1f} (frame line 1885, page edge 1910)")
    # W43 subtitle
    els43, _ = parse(os.path.join(W43, "svg", "p1-prima.svg"))
    sub43 = next((e for e in els43 if e["kind"] == "text" and "WEEKBLAD" in e["text"]), None)
    P(f"  W43 subtitle node: {sub43['a'] if sub43 else None} :: {sub43['text'] if sub43 else ''!r}")
    if sub43:
        fam, bold = sub43["a"].get("font-family", ""), sub43["a"].get("font-weight", "") in ("700", "bold")
        for size in (46,):
            f = font(fam, size, bold); adv = f.getlength(sub43["text"]) / SCALE
            P(f"    W43 size {size}: advance={adv:.1f} centred edges {975-adv/2:.1f}..{975+adv/2:.1f}")
    # footnote: ED + CORE settimana footnote nodes
    for d, label in [(ED, "ED"), (CO, "CORE"), (W43, "W43")]:
        elsx, _ = parse(os.path.join(d, "svg", "p1-prima.svg"))
        P(f"  -- {label} footnote candidates (y 1200..1300) --")
        for e in elsx:
            if e["kind"] == "text" and 1200 <= fnum(e["a"], "y") <= 1300:
                b = ink(e)
                P(f"    y={fnum(e['a'],'y')} x={fnum(e['a'],'x')} size={e['a'].get('font-size')} ink-right={b[2]:.1f} adv-right={adv_right(e):.1f} :: {e['text']!r}")
widths()

# ============ §P W43 furniture values ============
def w43():
    P("\n===== §P W43 ITxNL furniture =====")
    kit = open(os.path.join(W43, "WEEKLY-KIT.md"), encoding="utf-8").read()
    for pat in ["47", "46 /", "150", "90", "81"]:
        pass
    # print KIT lines mentioning counts/levels/words
    for line in kit.splitlines():
        if re.search(r"(A2|B1|B2|oefeningen|woorden|VOL\.1|150|90)", line) and len(line) < 220:
            P(f"  KIT: {line}")
    els, _ = parse(os.path.join(W43, "svg", "p1-prima.svg"))
    P("  W43 P1 texts y 340..400 (badge/slot zone):")
    for e in els:
        if e["kind"] == "text" and 340 <= fnum(e["a"], "y") <= 400:
            P(f"    y={fnum(e['a'],'y')} size={e['a'].get('font-size')} w={e['a'].get('font-weight')} :: {e['text']!r}")
    els8, _ = parse(os.path.join(W43, "svg", "p8-valutazione.svg"))
    P("  W43 P8 E-section keys 137-140:")
    for e in els8:
        if e["kind"] == "text" and re.match(r"^13[789]\.|^140\.", e["text"]):
            P(f"    :: {e['text']!r}")
w43()

# ============ §Q SVG recount: labels + chips + match groups ============
def recount(d, label):
    P(f"\n===== §Q SVG RECOUNT {label} =====")
    tot_lab = 0; tot_chip = 0; per = {}
    for fn in sorted(os.listdir(os.path.join(d, "svg"))):
        if not fn.endswith(".svg"): continue
        els, _ = parse(os.path.join(d, "svg", fn))
        labs, chips = [], []
        for e in els:
            if e["kind"] != "text": continue
            t = e["text"]
            m = re.match(r"^(\d+)\.\s", t)
            if m: labs.append(int(m.group(1)))
            if re.match(r"^\[(A2|B1|B2)\]", t): chips.append(t)
        # chips also appear as standalone '[A2]' nodes? count nodes containing [A2]/[B1]/[B2] as whole
        chipnodes = [e["text"] for e in els if e["kind"] == "text" and e["text"].strip() in ("[A2]", "[B1]", "[B2]")]
        P(f"  {fn}: number-labels={len(labs)} distinct={len(set(labs))} range={min(labs) if labs else None}..{max(labs) if labs else None} chip-prefix-lines={len(chips)} chip-nodes={len(chipnodes)}")
        tot_lab += len(labs); tot_chip += len(chipnodes)
        per[fn] = (len(labs), len(chipnodes))
    P(f"  TOTAL labels={tot_lab} chip-nodes={tot_chip}")
    # match groups: lettered rows for 25-28, 52-55, 141-144 — find texts like 'a — ...' near those pages
    for fn, nums in [("p2-vita.svg", (25, 28)), ("p4-sport.svg", (52, 55)), ("p8-valutazione.svg", (141, 144))]:
        els, _ = parse(os.path.join(d, "svg", fn))
        P(f"  match-group candidates {fn}:")
        for e in els:
            if e["kind"] == "text" and re.match(r"^[a-d]\s", e["text"]) and len(e["text"]) < 60:
                P(f"    :: {e['text']!r}")
recount(CO, "CORE"); recount(ED, "EDITION")

# ============ §R model text ============
def model(d, label):
    P(f"\n===== §R MODEL TEXT {label} =====")
    els, _ = parse(os.path.join(d, "svg", "p8-valutazione.svg"))
    seq = [e["text"] for e in els if e["kind"] == "text"]
    # model text follows the H bridge line; find bridge then take following Italian-looking lines until footer/page line
    txt = " ".join(seq)
    i = txt.find("Schrijfopdracht")
    j = txt.find("写作题")
    P(f"  bridge idx ED-style: {i}, CORE-style: {j}")
    # print last 25 text nodes of P8 (model area)
    for e in els[-30:]:
        if e["kind"] == "text": P(f"    y={fnum(e['a'],'y')} :: {e['text']!r}")
model(CO, "CORE"); model(ED, "EDITION")
def model_words(d):
    els, _ = parse(os.path.join(d, "svg", "p8-valutazione.svg"))
    seq = [e["text"] for e in els if e["kind"] == "text"]
    # model = Italian paragraph after H title: locate 'La tua settimana' title then collect until 'Pagina 8 van'/'第 8 版' footer or RISPOSTE? Model sits at end; use KIT method: count words of the H model paragraph.
    # Heuristic: texts after the last 'Schrijfopdracht'/'写作题' bridge line, excluding footer/page-line/badge lines.
    out = []
    grab = False
    for e in els:
        if e["kind"] != "text": continue
        t = e["text"]
        if t.startswith("Schrijfopdracht") or t.startswith("写作题"): grab = True; continue
        if grab:
            if t.startswith(("Pagina 8 van", "第 8 版", "La Lucerna ·")): break
            out.append(t)
    joined_m = " ".join(out)
    P(f"  model joined: {joined_m!r}")
    P(f"  model word count (whitespace split): {len(joined_m.split())}")
    return joined_m
P("\n===== §R2 MODEL word counts =====")
mc = model_words(CO); me = model_words(ED)
P(f"  model texts identical: {mc == me}")

# ============ §S round baselines scope ============
def rounds():
    P("\n===== §S ROUND BASELINE scope =====")
    def load(p):
        out = {}
        for line in open(p, encoding="utf-8"):
            parts = line.split()
            if len(parts) == 2: out[os.path.basename(parts[1])] = parts[0][:12]
        return out
    B = EDB
    for name in ["baseline-round1.txt", "baseline-round2-pre.txt", "baseline-round3-pre.txt", "baseline-round4-pre.txt", "baseline-round4-final.txt"]:
        p = os.path.join(B, name)
        if os.path.exists(p): P(f"  {name}: {load(p)}")
    r3pre = load(os.path.join(B, "baseline-round3-pre.txt")); r4pre = load(os.path.join(B, "baseline-round4-pre.txt")); r4fin = load(os.path.join(B, "baseline-round4-final.txt"))
    P(f"  round3 changed pages (r3pre vs r4pre): {[k for k in r3pre if r3pre.get(k) != r4pre.get(k)]}")
    P(f"  round4 changed pages (r4pre vs r4fin): {[k for k in r4pre if r4pre.get(k) != r4fin.get(k)]}")
    P("  shipped edition == r4fin: (see below)")
    import hashlib
    ok = True
    for fn, h in r4fin.items():
        if not fn.endswith(".svg"): continue
        actual = hashlib.sha256(open(os.path.join(ED, "svg", fn), "rb").read()).hexdigest()[:12]
        if actual != h: ok = False; P(f"    MISMATCH {fn}: shipped {actual} vs r4fin {h}")
    P(f"  shipped==r4fin: {ok}")
rounds()

# ============ §T P1 bridge/cifre line counts + P8 trims ============
def linecounts():
    P("\n===== §T LINE COUNTS =====")
    def lines(d, fn, pred):
        els, _ = parse(os.path.join(d, "svg", fn))
        return [(fnum(e["a"], "y"), e["text"]) for e in els if e["kind"] == "text" and pred(e["text"])]
    P("  ED P1 bridge lines (Uitleg — / versante / previsione):")
    for y, t in lines(ED, "p1-prima.svg", lambda t: t.startswith("Uitleg —") or t.startswith("versante") or t.startswith("previsione")):
        P(f"    y={y} :: {t!r}")
    P("  ED P1 cifre item4 lines (speelronde / settimana):")
    for y, t in lines(ED, "p1-prima.svg", lambda t: "speelronde 11 dit weekend" in t or t.startswith("settimana(")):
        P(f"    y={y} :: {t!r}")
    P("  ED P8 trim items line counts (#41/#50/#138 nodes):")
    for n in (41, 50, 138):
        els, _ = parse(os.path.join(ED, "svg", "p8-valutazione.svg"))
        nodes = [(fnum(e["a"], "y"), e["text"]) for e in els if e["kind"] == "text" and re.match(rf"^{n}\.\s", e["text"])]
        P(f"    #{n}: {nodes}")
    P("  ED P7 disclosure lines (Voorbeeld/nog geen/van pagina/voor VOL.3):")
    for y, t in lines(ED, "p7-lingua.svg", lambda t: t.startswith("Voorbeeld van") or t.startswith("nog geen") or t.startswith("van pagina") or t.startswith("voor VOL")):
        P(f"    y={y} :: {t!r}")
    P("  ED P7 letter + label + preview presence:")
    allt = " ".join(e["text"] for e in parse(os.path.join(ED, "svg", "p7-lingua.svg"))[0] if e["kind"] == "text")
    P(f"    '(esempio della redazione)' present: {'(esempio della redazione)' in allt}")
    for frag in ["Cara redazione", "VOL.3"]:
        P(f"    frag {frag!r}: {frag in allt}")
    # best-essay coverage ruling inputs: print P8 H title + P7 preview lines
    for y, t in lines(ED, "p7-lingua.svg", lambda t: "VOLGENDE WEEK" in t or "VOL.3" in t):
        P(f"    P7 preview y={y} :: {t!r}")
linecounts()

# ============ §U Latin-only removed strings: Italian survival ============
def latin_removed():
    P("\n===== §U LATIN-ONLY REMOVED strings: Italian survival in edition =====")
    import json as _json
    d = _json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "freeze-diff.json")))
    edjoined = " ".join(joined(ED).values())
    CJKr = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
    for pg, v in d["pages"].items():
        for item in v["removed_strings"]:
            t = item["text"]
            if CJKr.search(t): continue
            # strip to Latin core: remove punctuation-only? check whole string in edition joined
            survives = t in edjoined
            P(f"  p{pg} survives={survives} :: {t!r}")
latin_removed()

# ============ §V P7 box padding: code formula + measured clearance ============
def padding():
    P("\n===== §V P7 PAROLA BOX padding =====")
    for bd, label in [(COB, "CORE build content7"), (EDB, "EDITION build content7")]:
        s = open(os.path.join(bd, "content7.py"), encoding="utf-8").read()
        for i, line in enumerate(s.splitlines()):
            if "wh" in line and ("+ 2" in line or "parola" in line.lower() or "assaggio" in line):
                P(f"  {label} L{i+1}: {line.strip()[:200]}")
    # measured: gloss ink bottom vs containing rect bottom in edition P7
    els, _ = parse(os.path.join(ED, "svg", "p7-lingua.svg"))
    for e in els: e["box"] = ink(e)[:4] if e["kind"] == "text" else shape_box(e)
    gi = next((e["idx"] for e in els if e["kind"] == "text" and e["text"].startswith("assaggio =")), None)
    rect = next((e for e in reversed(els[:gi]) if e["kind"] == "rect"), None) if gi is not None else None
    if rect:
        P(f"  ED gloss rect bottom: {rect['box'][3]:.1f} ; gloss ink bottom: {next(e for e in els if e['idx']==gi)['box'][3]:.1f} ; clearance: {rect['box'][3]-next(e for e in els if e['idx']==gi)['box'][3]:.1f}px")
        # all texts inside rect: max ink bottom
        inside = [e for e in els if e["kind"] == "text" and e["box"] and rect["box"][0] <= e["box"][0] and e["box"][2] <= rect["box"][2] and rect["box"][1] <= e["box"][1] and e["box"][3] <= rect["box"][3]+1]
        P(f"  texts fully inside rect: {len(inside)}; nearby texts:")
        near = [e for e in els if e["kind"] == "text" and e["box"] and rect["box"][1]-5 <= e["box"][1] <= rect["box"][3]+5]
        for e in near: P(f"    y={fnum(e['a'],'y')} inkbot={e['box'][3]:.1f} :: {e['text']!r}")
        P("")
padding()
P("\n===== END proof_audit =====")
