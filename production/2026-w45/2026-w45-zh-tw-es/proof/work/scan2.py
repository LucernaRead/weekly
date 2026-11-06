import re, json, sys
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
from PIL import ImageFont
G = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
W = f"{G}/hidden_files/w45/zh-tw-es-proof/work"
NAMES = ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]
out = {}

# --- model char count (verbatim, minus label)
def nodes(d, n):
    txt = open(f"{G}/{d}/svg/{n}.svg", encoding="utf-8").read()
    return re.findall(r"<text[^>]*>(.*?)</text>", txt)
for lab, d, labstr in [("core", "files/weekly-report-w45-zhtw-core", "Model answer: "),
                       ("ed", "files/weekly-report-w45-zh-tw-es", "Respuesta modelo: ")]:
    ns = nodes(d, "p8-test")
    i = [j for j, t in enumerate(ns) if labstr in t][0]
    seg = [ns[i].split(labstr, 1)[1]] + ns[i+1:i+5]
    model = "".join(seg)
    out[f"model_{lab}"] = {"text": model, "chars_nospace": len(model.replace(" ", "").replace("　", "")),
                          "chars_total": len(model)}
out["model_identical"] = out["model_core"]["text"] == out["model_ed"]["text"]

# --- badge width via PIL (TC face 3, Bold, 21pt -> px at 96dpi? builder used PIL measure;
# report raw getlength at size 21 and size 28 for comparison across the three)
sans_b = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
for size in (21, 28):
    f = ImageFont.truetype(sans_b, size, index=3)
    for lab, s in [("core", "繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers"),
                   ("ed", "TEXTOS EN CHINO TRADICIONAL · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES")]:
        out.setdefault("badge_width", {})[f"{lab}_{size}"] = f.getlength(s)

# --- same-baseline ink scan + chart graze, using SVG text/rect elements in draw order
from PIL import ImageFont as IF
sans_r = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
serif_r = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
serif_b = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
def font_for(fam, size, weight):
    base = sans_b if ("Sans" in fam and weight == "700") else (sans_r if "Sans" in fam else (serif_b if weight == "700" else serif_r))
    try:
        return IF.truetype(base, int(round(size)), index=3)
    except Exception:
        return IF.load_default()
def ink_box(x, y, t, size, fam, weight, anchor):
    # y is baseline in these SVGs (text y attr); use getbbox for ink extents
    f = font_for(fam, size, weight)
    l, tp, r, b = f.getbbox(t)
    w = r - l
    if anchor == "middle":
        x0 = x - w / 2
    elif anchor == "end":
        x0 = x - w
    else:
        x0 = x
    # ink vertical: baseline y + top..bottom (PIL bbox top negative above baseline)
    return (x0 + l, y + tp, x0 + r, y + b)
for n in NAMES:
    raw = open(f"{G}/files/weekly-report-w45-zh-tw-es/svg/{n}.svg", encoding="utf-8").read()
    # ordered elements: text and rect
    els = []
    for m in re.finditer(r"<(text|rect)[^>]*>", raw):
        tag = m.group(1)
        attrs = m.group(0)
        if tag == "text":
            mm = re.search(r'x="([\d.]+)" y="([\d.]+)"[^>]*font-size="([\d.]+)"', attrs)
            fam = re.search(r'font-family="([^"]+)"', attrs)
            wt = re.search(r'font-weight="([^"]+)"', attrs)
            an = re.search(r'text-anchor="([^"]+)"', attrs)
            # text content follows
            cm = re.search(r">([^<]*)</text>", raw[m.end():m.end()+400])
            if mm and cm:
                els.append(("text", float(mm.group(1)), float(mm.group(2)), float(mm.group(3)),
                            fam.group(1) if fam else "", wt.group(1) if wt else "",
                            an.group(1) if an else "start", cm.group(1)))
        else:
            mm = re.search(r'x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', attrs)
            fill = re.search(r'fill="([^"]+)"', attrs)
            if mm and fill and fill.group(1) not in ("none",):
                els.append(("rect", float(mm.group(1)), float(mm.group(2)), float(mm.group(3)), float(mm.group(4))))
    # same-baseline: group texts by y (exact), check ink x-intervals overlap with >0 gap violation
    by_y = {}
    for e in els:
        if e[0] == "text":
            _, x, y, size, fam, wt, an, t = e
            if not t.strip():
                continue
            by_y.setdefault(y, []).append((x, size, fam, wt, an, t))
    sb_flags = []
    for y, items in by_y.items():
        boxes = []
        for x, size, fam, wt, an, t in items:
            boxes.append((ink_box(x, y, t, size, fam, wt, an), t))
        boxes.sort(key=lambda b: b[0][0])
        for (b1, t1), (b2, t2) in zip(boxes, boxes[1:]):
            if b2[0] < b1[2] - 0.5:
                sb_flags.append((y, t1[:60], t2[:60], round(b1[2]-b2[0], 1)))
    out[f"samebase_{n}"] = sb_flags
    # chart graze: text ink vs LATER-drawn rects (all pages; chart pages matter)
    graze = []
    textboxes = []
    for idx, e in enumerate(els):
        if e[0] == "text":
            _, x, y, size, fam, wt, an, t = e
            if t.strip():
                textboxes.append((idx, ink_box(x, y, t, size, fam, wt, an), t))
    for idx, e in enumerate(els):
        if e[0] == "rect":
            _, rx, ry, rw, rh = e
            for ti, tb, t in textboxes:
                if ti < idx:  # text drawn before rect -> rect may cover it
                    ix0, iy0, ix1, iy1 = max(tb[0], rx), max(tb[1], ry), min(tb[2], rx+rw), min(tb[3], ry+rh)
                    if ix1 > ix0 and iy1 > iy0:
                        cov = (ix1-ix0)*(iy1-iy0)
                        gw = (tb[2]-tb[0]); gh = (tb[3]-tb[1])
                        if gw > 0 and gh > 0 and cov / (gw*gh) >= 0.05:
                            graze.append((t[:60], round(cov/(gw*gh), 2)))
    out[f"graze_{n}"] = graze[:10]

# --- residual Latin scan: whole-word English prose words outside frozen sets
import collections
EN = ["the","and","with","from","this","that","work","words","baseball","week","quiz","notes","answer","page","test","read","chart","sport","life","culture","youth","language","true","false"]
frozen = {"fintech","nexus","bridging","world","building","future","startmeuphk","itf","super","stage","solid","tides","jump","trick","treat","wei","chuan","dragons","ctbc","brothers","mercedes","jurassic","shrek","kung","fu","panda","mvp","tamagotchi","halloween","lucerna","vol","photo","wikimedia","commons","cc0","public","domain","wilfredor","corraleh","bain","news","service","benjamin","balazs","nt"}
hits = collections.Counter()
for n in NAMES:
    for t in nodes("files/weekly-report-w45-zh-tw-es", n):
        for w in re.findall(r"[A-Za-z]+", t):
            lw = w.lower()
            if lw in EN and lw not in frozen:
                hits[(n, lw)] += 1
out["residual_en_words"] = {f"{k[0]}:{k[1]}": v for k, v in hits.items()}
json.dump(out, open(f"{W}/scan2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("model identical:", out["model_identical"], "core chars nospace:", out["model_core"]["chars_nospace"], "ed:", out["model_ed"]["chars_nospace"])
print("badge widths:", out["badge_width"])
for n in NAMES:
    print(n, "samebase:", out[f"samebase_{n}"], "graze:", out[f"graze_{n}"])
print("residual EN:", out["residual_en_words"])
