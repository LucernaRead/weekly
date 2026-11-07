# -*- coding: utf-8 -*-
"""Independent FR x IT SVG probe (own code, read-only over shipped SVGs).
Outputs JSON to stdout file given as argv[1]. Uses PIL Noto CJK faces
directly (same faces the builder uses) for advance/ink measurements.
"""
import os, re, sys, json, glob, hashlib, base64
import xml.etree.ElementTree as ET
from PIL import ImageFont

ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
ED = os.path.join(ROOT, "weekly-report-w45-fr-it", "svg")
CORE = os.path.join(ROOT, "weekly-report-w45-fr-core", "svg")
W43 = os.path.join(ROOT, "weekly-report-fr-it", "svg")
FRDE = os.path.join(ROOT, "weekly-report-w45-fr-de", "svg")

FONTS_DIR = "/usr/share/fonts/opentype/noto"
def _sc_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith("SC"):
                return i
        except Exception:
            break
    return 0
_SERIF = os.path.join(FONTS_DIR, "NotoSerifCJK-Regular.ttc")
_SERIF_B = os.path.join(FONTS_DIR, "NotoSerifCJK-Bold.ttc")
_SANS = os.path.join(FONTS_DIR, "NotoSansCJK-Regular.ttc")
_SANS_B = os.path.join(FONTS_DIR, "NotoSansCJK-Bold.ttc")
_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}
_cache = {}
def _font(kind, bold, size):
    path = {"serif": _SERIF_B if bold else _SERIF, "sans": _SANS_B if bold else _SANS}[kind]
    key = (path, int(size))
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, int(size), index=_IDX[path])
    return _cache[key]
def text_w(s, kind, bold, size):
    return _font(kind, bold, size).getlength(s)
SCALE = 4
def ink_bottom(y, s, kind, bold, size):
    # canonical occlusion_audit ink_box: supersampled font, bottom = y - ascent + b/SCALE
    f = _font(kind, bold, int(size) * SCALE)
    bb = f.getbbox(s)
    ascent = f.getmetrics()[0] / SCALE
    return y - ascent + bb[3] / SCALE, y - ascent + bb[1] / SCALE

def nodes(path):
    out = []
    root = ET.parse(path).getroot()
    for el in root.iter():
        if not el.tag.endswith("text"):
            continue
        t = el.text or ""
        if not t.strip():
            continue
        fam = el.get("font-family") or ""
        kind = "serif" if "Serif" in fam else "sans"
        bold = el.get("font-weight") == "700"
        out.append({"x": float(el.get("x") or 0), "y": float(el.get("y") or 0),
                    "size": float(el.get("font-size") or 20), "kind": kind, "bold": bold,
                    "anchor": el.get("text-anchor") or "start",
                    "fill": el.get("fill") or "", "text": t})
    return out

def joined(ns):
    return re.sub(r"\s+", " ", " ".join(n["text"] for n in ns)).strip()

def han_count(s):
    return sum(1 for c in s if "\u4e00" <= c <= "\u9fff")

PAGES = ["p1-une.svg","p2-vie.svg","p3-culture.svg","p4-sport.svg","p5-jeunesse.svg","p6-politique.svg","p7-langue.svg","p8-exercices.svg"]
out = {"pages": {}, "core_pages": {}, "w43_pages": {}}
for label, d, key in [("ed", ED, "pages"), ("core", CORE, "core_pages"), ("w43", W43, "w43_pages")]:
    for pg in PAGES:
        ns = nodes(os.path.join(d, pg))
        txt = joined(ns)
        raw = " ".join(n["text"] for n in ns)
        out[key][pg] = {"n_nodes": len(ns), "joined_len": len(txt),
                        "han": han_count(raw), "fw_parens": raw.count("（") + raw.count("）"),
                        "joined": txt, "nodes": ns}

# ---- specific string searches (joined text) ----
def find_all(txt, s):
    return txt.count(s)

checks = {}
ed_all = " ".join(out["pages"][p]["joined"] for p in PAGES)
core_all = " ".join(out["core_pages"][p]["joined"] for p in PAGES)
for s in ["41e édition en 2026 (40e anniversaire)", "40e", "22e édition", "15e édition",
          "Si j'étais libre dimanche, j'___ à Nanterre.",
          "plus excitante ou plus frustrante?",
          "Les jeunes créateurs y rencontrent leur public, en vrai.",
          "Ce calendrier peut encore bouger.",
          "Le lundi 2 novembre, on reprend les cours.",
          "On ne connaît pas encore les finalistes.",
          "Les cimetières se sont remplis de chrysanthèmes.",
          "Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?",
          "Le festival se promène dans Paris.",
          "Ce week-end, tout se joue.",
          "Mandateci lettere e migliori testi!",
          "ancora nessuna lettera vera",
          "Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)",
          "Note de la rédaction : aucun texte du VOL.2",
          ]:
    checks[s] = {"ed_total": find_all(ed_all, s), "core_total": find_all(core_all, s),
                 "ed_per_page": {p: find_all(out["pages"][p]["joined"], s) for p in PAGES},
                 "core_per_page": {p: find_all(out["core_pages"][p]["joined"], s) for p in PAGES}}

out["checks"] = checks
# 40e nodes with coords
def nodes_with(d, substr):
    res = []
    for pg in PAGES:
        for n in nodes(os.path.join(d, pg)):
            if substr in n["text"]:
                res.append({"page": pg, "x": n["x"], "y": n["y"], "size": n["size"], "text": n["text"]})
    return res
out["nodes_40e_ed"] = nodes_with(ED, "40e")
out["nodes_40e_core"] = nodes_with(CORE, "40e")
out["nodes_41e_ed"] = nodes_with(ED, "41e")
out["nodes_41e_core"] = nodes_with(CORE, "41e")
out["nodes_giusta_ed"] = nodes_with(ED, "giusta.")
out["nodes_giusta_frde"] = nodes_with(FRDE, "giusta.") if os.path.exists(os.path.join(FRDE, "p4-sport.svg")) else []
# giusta neighbours in edition P4: nodes with x near giusta node and y within +-60
for pg in ["p4-sport.svg"]:
    ns = nodes(os.path.join(ED, pg))
    for n in ns:
        if "giusta." in n["text"]:
            out["giusta_context_ed"] = [m for m in ns if abs(m["y"] - n["y"]) < 80 and abs(m["x"] - n["x"]) < 600]
    ns2 = nodes(os.path.join(FRDE, pg)) if os.path.exists(os.path.join(FRDE, pg)) else []
    for n in ns2:
        if "richtige Antwort." in n["text"] or "Sie die richtige" in n["text"]:
            out["frde_debate_context"] = [m for m in ns2 if abs(m["y"] - n["y"]) < 80]
    # also fr-de P4 nodes at same y as giusta? record all nodes y==220.5 in fr-de
    out["frde_p4_y220"] = [m for m in ns2 if abs(m["y"] - 220.5) < 1.0]

# Q120 / Q119 / Q121 neighbourhoods on P8 (stems + options + keys region)
for label, d in [("ed", ED), ("core", CORE)]:
    ns = nodes(os.path.join(d, "p8-exercices.svg"))
    out[f"q_stems_{label}"] = {}
    for q, pat in [("Q119", "s'intéresse"), ("Q120", "Si j'étais libre"), ("Q121", "mon avis")]:
        out[f"q_stems_{label}"][q] = [n for n in ns if pat in n["text"]]
    # options row for Q120: nodes with irai/irais/vais near stem y
    stem = out[f"q_stems_{label}"]["Q120"]
    if stem:
        sy = stem[0]["y"]
        out[f"q120_options_{label}"] = [n for n in ns if abs(n["y"] - sy) < 80]
    # keys lines containing 119./120./121. tokens
    out[f"q_keys_lines_{label}"] = [n for n in ns if re.search(r"\b(119|120|121)\.", n["text"])]

# P8 notes purity probes + cross-family probes (whole edition)
GERMAN_PROBES = ["Schulbeginn", "Jakobsmuschel", "Nachtveranstaltung", "Übersetzen Sie", "Übersetzung", "Schul", "Lesen Sie", "Woche", "Montagmorgen"]
out["german_probes_ed"] = {w: ed_all.count(w) for w in GERMAN_PROBES}
out["german_probes_ed_per_page"] = {w: {p: out["pages"][p]["joined"].count(w) for p in PAGES} for w in GERMAN_PROBES}
# P8 printed notes: nodes in keys area (y>1560, excluding footer 2624) joined; check Han/German there
for label, d in [("ed", ED), ("core", CORE)]:
    ns = [n for n in nodes(os.path.join(d, "p8-exercices.svg")) if 1600 < n["y"] < 2580]
    txt = joined(ns)
    out[f"p8_keys_text_{label}"] = txt
    out[f"p8_keys_han_{label}"] = han_count(txt)

# P7 reader corner + preview verbatim nodes
for label, d in [("ed", ED), ("core", CORE)]:
    ns = nodes(os.path.join(d, "p7-langue.svg"))
    out[f"p7_reader_{label}"] = [n for n in ns if any(k in n["text"] for k in ["Exemple de la rédaction", "Nota della redazione", "Note de la rédaction", "Mandateci", "LE COURRIER", "L'ANGOLO", "PROSSIMA SETTIMANA", "LA SEMAINE PROCHAINE", "le vostre lettere", "Et vos lettres"])]
    # P7 max baseline excluding footer (y<2600), and preview lines (y>2300, y<2600)
    body = [n for n in ns if n["y"] < 2600]
    out[f"p7_max_baseline_{label}"] = max(n["y"] for n in body)
    out[f"p7_last_nodes_{label}"] = sorted(body, key=lambda n: n["y"])[-12:]
    # ink bottom of last node
    last = max(body, key=lambda n: n["y"])
    b, t = ink_bottom(last["y"], last["text"], last["kind"], last["bold"], last["size"])
    out[f"p7_last_ink_{label}"] = {"baseline": last["y"], "ink_bottom": b, "text": last["text"]}

# P8 flow ends: battery (y<1486 excl headers?) vs keys (y>1600, <2580)
for label, d in [("ed", ED), ("core", CORE)]:
    ns = nodes(os.path.join(d, "p8-exercices.svg"))
    batt = [n for n in ns if n["y"] < 1486]
    keys = [n for n in ns if 1600 < n["y"] < 2580]
    def maxink(lst):
        best = None
        for n in lst:
            b, _ = ink_bottom(n["y"], n["text"], n["kind"], n["bold"], n["size"])
            if best is None or b > best[0]:
                best = (b, n)
        return best
    bb = maxink(batt); kk = maxink(keys)
    out[f"p8_battery_{label}"] = {"max_baseline": max(n["y"] for n in batt), "ink_bottom": bb[0], "ink_node": bb[1], "last_nodes": sorted(batt, key=lambda n: n["y"])[-6:]}
    out[f"p8_keys_{label}"] = {"max_baseline": max(n["y"] for n in keys), "ink_bottom": kk[0], "ink_node": kk[1], "last_nodes": sorted(keys, key=lambda n: n["y"])[-10:]}
    # keys per-column max baseline: columns by x clusters (battery/keys use COLX ~ 65/527/989/1451 starts)
    cols = {}
    for n in keys:
        # column start: nearest of 65,527,989,1451 at or below x
        starts = [65, 527, 989, 1451]
        c = max([s for s in starts if s <= n["x"] + 1] or [65])
        cols.setdefault(c, []).append(n)
    out[f"p8_keys_cols_{label}"] = {str(c): {"max_baseline": max(n["y"] for n in v), "n": len(v), "last": sorted(v, key=lambda n: n["y"])[-3:]} for c, v in cols.items()}

# Model essay: P8 nodes between MODELE header and keys header (y between model header and ky)
for label, d in [("ed", ED), ("core", CORE)]:
    ns = nodes(os.path.join(d, "p8-exercices.svg"))
    mh = [n for n in ns if n["text"].startswith("MODÈLE") and n["x"] > 900]
    kh = [n for n in ns if n["text"].startswith("RÉPONSES") and mh and n["y"] > mh[0]["y"]]
    if mh and kh:
        y0, y1 = mh[0]["y"], kh[0]["y"]
        body = [n for n in ns if y0 < n["y"] < y1 and n["x"] >= 1000]
        txt = joined(body)
        out[f"model_{label}"] = {"header": mh, "body_text": txt, "word_count": len(txt.split()), "body_nodes": body}

# Right-edge ADVANCE + frame + rowcheck + kinsoku + hyphen
def adv_box(n):
    w = text_w(n["text"], n["kind"], n["bold"], n["size"])
    if n["anchor"] == "middle":
        return n["x"] - w/2, n["x"] + w/2
    if n["anchor"] == "end":
        return n["x"] - w, n["x"]
    return n["x"], n["x"] + w
out["right_edge"] = {}
for pg in PAGES:
    overs = []
    for n in out["pages"][pg]["nodes"]:
        x0, x1 = adv_box(n)
        if x1 > 1885:
            overs.append({"page": pg, "y": n["y"], "x1": round(x1, 1), "text": n["text"]})
    out["right_edge"][pg] = overs
out["right_edge_core"] = {}
for pg in PAGES:
    overs = []
    for n in out["core_pages"][pg]["nodes"]:
        x0, x1 = adv_box(n)
        if x1 > 1885:
            overs.append({"page": pg, "y": n["y"], "x1": round(x1, 1), "text": n["text"]})
    out["right_edge_core"][pg] = overs
out["frame_hits"] = []
for pg in PAGES:
    for n in out["pages"][pg]["nodes"]:
        x0, x1 = adv_box(n)
        top, bot = n["y"] - n["size"], n["y"] + n["size"]*0.3
        if x1 > 1908 and top <= 2672 and bot >= 28:
            out["frame_hits"].append({"page": pg, "y": n["y"], "x1": round(x1, 1), "text": n["text"]})
out["rowcheck"] = {}
for pg in PAGES:
    for band in (92, 574, 2624):
        row = sorted([(adv_box(n)[0], adv_box(n)[1], n["text"]) for n in out["pages"][pg]["nodes"] if abs(n["y"] - band) < 1.5])
        for (x0a, x1a, ta), (x0b, x1b, tb) in zip(row, row[1:]):
            if x0b < x1a - 1:
                out["rowcheck"].setdefault(pg, []).append({"band": band, "a": ta, "b": tb, "gap": round(x0b - x1a, 1)})
out["kinsoku"] = []
for pg in PAGES:
    for n in out["pages"][pg]["nodes"]:
        t = n["text"].strip()
        if t and t[0] in ")]}.,;:!?%\"'":
            out["kinsoku"].append({"page": pg, "y": n["y"], "x": n["x"], "text": n["text"]})
out["kinsoku_core"] = []
for pg in PAGES:
    for n in out["core_pages"][pg]["nodes"]:
        t = n["text"].strip()
        if t and t[0] in ")]}.,;:!?%\"'":
            out["kinsoku_core"].append({"page": pg, "y": n["y"], "x": n["x"], "text": n["text"]})
# mid-line hyphen / en-dash list breaks
out["line_end_dash"] = []
for pg in PAGES:
    ns = out["pages"][pg]["nodes"]
    for n in ns:
        t = n["text"].strip()
        if t.endswith("-") or t.endswith("–"):
            out["line_end_dash"].append({"page": pg, "y": n["y"], "x": n["x"], "text": n["text"]})
out["line_end_dash_core"] = []
for pg in PAGES:
    for n in out["core_pages"][pg]["nodes"]:
        t = n["text"].strip()
        if t.endswith("-") or t.endswith("–"):
            out["line_end_dash_core"].append({"page": pg, "y": n["y"], "x": n["x"], "text": n["text"]})

# Furniture
def furniture(d):
    res = {}
    p1 = nodes(os.path.join(d, "p1-une.svg"))
    res["badge"] = [n for n in p1 if n["y"] == 574]
    res["top92"] = [n for n in p1 if n["y"] == 92]
    res["masthead"] = [n for n in p1 if n["y"] == 262]
    res["subtitle"] = [n for n in p1 if n["y"] == 330]
    res["slogan"] = [n for n in p1 if n["y"] == 372]
    res["band478"] = [n for n in p1 if n["y"] == 478]
    res["band522"] = [n for n in p1 if n["y"] == 522]
    res["footers"] = {}
    for pg in PAGES:
        res["footers"][pg] = [n for n in nodes(os.path.join(d, pg)) if n["y"] == 2624]
    return res
out["furn_ed"] = furniture(ED)
out["furn_w43"] = furniture(W43)
out["furn_core"] = furniture(CORE)

# Images: <image> elements + credit nodes
def images(d):
    res = {}
    for pg in PAGES:
        root = ET.parse(os.path.join(d, pg)).getroot()
        imgs = []
        for el in root.iter():
            if el.tag.endswith("image"):
                href = el.get("{http://www.w3.org/1999/xlink}href") or el.get("href") or ""
                b64 = href.split(",", 1)[1] if "," in href else href
                raw = base64.b64decode(b64) if b64 else b""
                imgs.append({"x": el.get("x"), "y": el.get("y"), "width": el.get("width"), "height": el.get("height"),
                             "b64_sha": hashlib.sha256(b64.encode()).hexdigest(),
                             "jpg_sha": hashlib.sha256(raw).hexdigest(), "jpg_len": len(raw)})
        res[pg] = imgs
    return res
out["images_ed"] = images(ED)
out["images_core"] = images(CORE)
out["credits_ed"] = {pg: [n for n in out["pages"][pg]["nodes"] if any(k in n["text"] for k in ["Atget", "Hiroshige", "Blanco", "domaine public"])] for pg in PAGES}
out["credits_core"] = {pg: [n for n in out["core_pages"][pg]["nodes"] if any(k in n["text"] for k in ["Atget", "Hiroshige", "Blanco", "domaine public"])] for pg in PAGES}

# P6 chart coverage (baseline-anchored getmetrics, rects after text)
def p6_coverage(d):
    path = os.path.join(d, "p6-politique.svg")
    root = ET.parse(path).getroot()
    elems = list(root.iter())
    maxcov = 0.0; worst = ""
    for i, el in enumerate(elems):
        if not el.tag.endswith("text"):
            continue
        t = el.text or ""
        if not t.strip():
            continue
        y = float(el.get("y") or 0)
        if not (1330 <= y <= 1800):
            continue
        size = float(el.get("font-size") or 20)
        fam = el.get("font-family") or ""
        kind = "serif" if "Serif" in fam else "sans"
        bold = el.get("font-weight") == "700"
        f = _font(kind, bold, size)
        asc, desc = f.getmetrics()
        x = float(el.get("x") or 0)
        w = text_w(t, kind, bold, size)
        anch = el.get("text-anchor") or "start"
        x0 = x if anch == "start" else (x - w/2 if anch == "middle" else x - w)
        box = (x0, y - asc, x0 + w, y + desc)
        for el2 in elems[i+1:]:
            if not el2.tag.endswith("rect"):
                continue
            rx, ry = float(el2.get("x") or 0), float(el2.get("y") or 0)
            rw, rh = float(el2.get("width") or 0), float(el2.get("height") or 0)
            ix = max(0, min(box[2], rx+rw) - max(box[0], rx))
            iy = max(0, min(box[3], ry+rh) - max(box[1], ry))
            area = (box[2]-box[0])*(box[3]-box[1])
            cov = ix*iy/area*100 if area else 0
            if cov > maxcov:
                maxcov = cov; worst = t
    return maxcov, worst
out["p6_coverage_ed"] = p6_coverage(ED)
out["p6_coverage_core"] = p6_coverage(CORE)

with open(sys.argv[1], "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("wrote", sys.argv[1])
