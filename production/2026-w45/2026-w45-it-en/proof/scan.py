#!/usr/bin/env python3
"""Independent proofread scans for W45 ITxEN. NOT builder scripts.
Parses shipped SVGs only; never imports content modules."""
import json, re, sys, hashlib
from xml.etree import ElementTree as ET
from collections import Counter, defaultdict
from PIL import ImageFont

BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
ED = BASE + "/files/weekly-report-w45-it-en/svg/"
CO = BASE + "/files/weekly-report-w45-it-core/svg/"
W43 = BASE + "/files/weekly-report-it-en/svg/"
FD = "/usr/share/fonts/opentype/noto/"
F = {}
def font(fam, bold, size):
    key = (fam, bold, size)
    if key not in F:
        path = (FD + ("NotoSerifCJK-Bold.ttc" if "Serif" in fam else "NotoSansCJK-Bold.ttc")) if bold \
            else (FD + ("NotoSerifCJK-Regular.ttc" if "Serif" in fam else "NotoSansCJK-Regular.ttc"))
        F[key] = ImageFont.truetype(path, int(round(size)), index=2)
    return F[key]

def texts(path):
    """text nodes in document order with geometry."""
    out = []
    for e in ET.parse(path).getroot().iter():
        if e.tag.endswith("text") and e.text:
            x, y = float(e.get("x")), float(e.get("y"))
            fs = float(e.get("font-size")); bold = e.get("font-weight") in ("700", "bold")
            fam = e.get("font-family", "")
            an = e.get("text-anchor", "start")
            f = font(fam, bold, fs)
            w = f.getlength(e.text)
            left = x - w if an == "end" else (x - w / 2 if an == "middle" else x)
            asc, desc = f.getmetrics()
            out.append(dict(x=x, y=y, fs=fs, bold=bold, fam=fam, an=an, t=e.text,
                            left=left, right=left + w, top=y - asc, bot=y + desc, w=w))
    return out

def elements(path):
    """all elements in document order, with tag + attribs."""
    return list(ET.parse(path).getroot().iter())

PAGES = ["p1-prima", "p2-vita", "p3-cultura", "p4-sport", "p5-giovani",
         "p6-approfondimento", "p7-lingua", "p8-valutazione"]
out = {}

# ---- 1. right-edge ADVANCE scan (own implementation, anchor-aware) ----
def rightedge(d):
    res = {}
    for p in PAGES:
        viol, margin = [], []
        for n in texts(d + p + ".svg"):
            if n["right"] > 1910:
                viol.append((p, round(n["left"], 1), round(n["right"], 1), round(n["y"], 2), n["t"][:60]))
            elif n["right"] > 1885:
                margin.append((p, round(n["left"], 1), round(n["right"], 1), round(n["y"], 2), n["t"][:60]))
        res[p] = dict(viol=viol, margin=margin)
    return res
re_ed, re_co = rightedge(ED), rightedge(CO)
out["rightedge_ed_viol"] = [v for p in PAGES for v in re_ed[p]["viol"]]
out["rightedge_ed_margin"] = [v for p in PAGES for v in re_ed[p]["margin"]]
out["rightedge_co_margin"] = [v for p in PAGES for v in re_co[p]["margin"]]
out["rightedge_margin_ed_texts_in_core"] = all(
    any(m[4] == c[4] and abs(m[2] - c[2]) < 0.6 for c in re_co[p]["margin"])
    for p in PAGES for m in re_ed[p]["margin"])
out["rightedge_co_viol"] = [v for p in PAGES for v in re_co[p]["viol"]]

# ---- 2. same-baseline scan: overlap or gap < 5px between adjacent runs ----
def rowcheck(d):
    flags = []
    for p in PAGES:
        by_y = defaultdict(list)
        for n in texts(d + p + ".svg"):
            by_y[round(n["y"], 2)].append(n)
        for y, ns in by_y.items():
            ns.sort(key=lambda n: n["left"])
            for a, b in zip(ns, ns[1:]):
                gap = b["left"] - a["right"]
                if gap < 5.0:
                    flags.append((p, y, round(gap, 2), a["t"][:40], b["t"][:40]))
    return flags
row_ed, row_co = rowcheck(ED), rowcheck(CO)
out["row_ed"] = row_ed; out["row_co"] = row_co
out["row_identical"] = (sorted(map(str, row_ed)) == sorted(map(str, row_co)))

# ---- 3. chart-label ink coverage on P6 (baseline-anchored ink: getmetrics band) ----
def chartcheck(d, page):
    elems = elements(d + page + ".svg")
    seq = []
    for e in elems:
        if e.tag.endswith("text") and e.text:
            x, y = float(e.get("x")), float(e.get("y")); fs = float(e.get("font-size"))
            bold = e.get("font-weight") in ("700", "bold"); f = font(e.get("font-family", ""), bold, fs)
            w = f.getlength(e.text); an = e.get("text-anchor", "start")
            left = x - w if an == "end" else (x - w / 2 if an == "middle" else x)
            asc, desc = f.getmetrics()
            seq.append(("text", left, y - asc, left + w, y + desc, e.text))
        elif e.tag.endswith("rect"):
            fill = e.get("fill", "none")
            if fill not in ("none", "#f7f1e2"):
                seq.append(("rect", float(e.get("x", 0)), float(e.get("y", 0)),
                            float(e.get("x", 0)) + float(e.get("width", 0)),
                            float(e.get("y", 0)) + float(e.get("height", 0)), fill))
    worst = []
    for i, (k, x0, y0, x1, y1, t) in enumerate(seq):
        if k != "text":
            continue
        area = max(0.0, (x1 - x0) * (y1 - y0))
        if area == 0:
            continue
        cov = 0.0
        for (k2, rx0, ry0, rx1, ry1, _) in seq[i + 1:]:
            if k2 != "rect":
                continue
            ix = max(0.0, min(x1, rx1) - max(x0, rx0)); iy = max(0.0, min(y1, ry1) - max(y0, ry0))
            cov = max(cov, ix * iy / area)
        worst.append((round(cov * 100, 2), t[:60]))
    worst.sort(reverse=True)
    return worst[:10]
out["chart_p6_ed_worst"] = chartcheck(ED, "p6-approfondimento")
out["chart_p6_co_worst"] = chartcheck(CO, "p6-approfondimento")

# ---- 4. frame/box pressure: ink crossing page frames (x=28/40, y=28/40, right 1922/1910, bottom 2672/2660) + out of page ----
def framecheck(d):
    hits = []
    for p in PAGES:
        for n in texts(d + p + ".svg"):
            if n["left"] < 28 or n["right"] > 1922 or n["top"] < 28 or n["bot"] > 2672:
                hits.append((p, round(n["left"], 1), round(n["right"], 1), round(n["top"], 1), round(n["bot"], 1), n["t"][:50]))
    return hits
out["frame_ed"] = framecheck(ED)

# ---- 5. P8 printed keys: reconstruct key lines per number from SVG text ----
def p8keys(d):
    ns = texts(d + "p8-valutazione.svg")
    # key block lines: node text starting with 'N. ' (dash style) - join wrapped continuations is unnecessary:
    # the key is on the first line of each item (number + key + ' — ' + note start or key alone)
    keys = {}
    for n in ns:
        m = re.match(r"^(\d+)\.\s+(.*)$", n["t"])
        if m and 113 <= int(m.group(1)) <= 150 or (m and int(m.group(1)) >= 113):
            keys.setdefault(int(m.group(1)), []).append(n["t"])
    return keys
# Better: use the full node list; key lines are those whose text begins with N. and y in key region (>1332?) - inspect separately
ke, kc = p8keys(ED), p8keys(CO)
out["p8_keyline_numbers_ed"] = sorted(ke); out["p8_keyline_numbers_co"] = sorted(kc)
def before_dash(s):
    return s.split(" — ")[0]
diff14 = {}
for num in [6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 137, 138, 139, 140, 150]:
    pass
out["p8_note"] = "see p8keys2 below"
# Direct approach: dump all P8 nodes whose text starts with a number for manual file
with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-en-proof/p8-nodes.txt", "w") as fh:
    for label, d in [("ED", ED), ("CO", CO)]:
        fh.write(f"===== {label} P8 numbered nodes =====\n")
        for n in texts(d + "p8-valutazione.svg"):
            if re.match(r"^\d+\.", n["t"]):
                fh.write(f"{n['x']:.1f} {n['y']:.2f} {n['t']!r}\n")

# ---- 6. gloss NOTE boxes P2-P6 ----
def gloss(d, page):
    ns = texts(d + page + ".svg")
    # NOTE lines: consecutive nodes starting with 'NOTE' then continuation lines at same x until next header;
    # simpler: find node starting with NOTE prefix, then collect following nodes with same x and fs until a node that starts a new block (bold/header or exercise number)
    res = []
    for i, n in enumerate(ns):
        if n["t"].startswith("NOTE"):
            joined = n["t"]
            j = i + 1
            while j < len(ns) and abs(ns[j]["x"] - n["x"]) < 1 and not ns[j]["bold"] and not re.match(r"^\d+\.", ns[j]["t"]) and ns[j]["y"] - ns[j - 1]["y"] < 40:
                joined += " " + ns[j]["t"]; j += 1
            res.append(joined)
    return res
for pg, name in [("p2-vita", "P2"), ("p3-cultura", "P3"), ("p4-sport", "P4"), ("p5-giovani", "P5"), ("p6-approfondimento", "P6")]:
    for label, d in [("ed", ED), ("co", CO)]:
        gs = gloss(d, pg)
        for g in gs:
            body = g.split("·", 1)[1] if "·" in g else g
            items = [s.strip() for s in body.split("·") if s.strip()]
            out[f"gloss_{name}_{label}"] = dict(raw=g, n=len(items), items=items)

# ---- 7. exercise numbers + levels from rendered SVGs ----
# Level chips: nodes exactly 'A2'/'B1'/'B2' adjacent to exercise numbers? Count exercise-number nodes per page:
# Exercise stems carry a leading number node on P1-P7 (standalone 'N.' nodes) and P8 stems.
def exnumbers(d):
    per = {}
    for p in PAGES:
        ns = texts(d + p + ".svg")
        nums = []
        for n in ns:
            m = re.match(r"^(\d+)\.$", n["t"])
            if m:
                nums.append(int(m.group(1)))
        per[p] = sorted(set(nums))
    return per
out["exnums_ed"] = exnumbers(ED); out["exnums_co"] = exnumbers(CO)

# ---- 8. P7 golden sentences, word box, readers corner, FRASI rule ----
p7ed = texts(ED + "p7-lingua.svg"); p7co = texts(CO + "p7-lingua.svg")
joined_ed = " ".join(n["t"] for n in p7ed); joined_co = " ".join(n["t"] for n in p7co)
gold = ["arriva il primo freddo vero della stagione", "Non è una certezza, è una probabilità",
        "il 2 novembre è la Commemorazione dei defunti", "Fa freddo, copriti bene!",
        "il pubblico può assaggiare gratis", "il calcio non si ferma per il primo freddo",
        "la cultura continua", "Una probabilità alta non è una certezza"]
out["gold_ed"] = {g: joined_ed.count(g) for g in gold}
out["gold_co"] = {g: joined_co.count(g) for g in gold}
def wordbox(ns):
    lines = [n["t"] for n in ns if n["x"] == 1473.0 and 1128 <= n["y"] <= 1221]
    return " ".join(lines)
out["wordbox_ed"] = wordbox(p7ed); out["wordbox_co"] = wordbox(p7co)
out["wordbox_expected"] = "« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone."
col3 = [n for n in p7ed if n["x"] >= 1451 and n["y"] < 1686]
out["p7_col3_last_baseline"] = max(n["y"] for n in col3)
out["p7_col3_last_bot"] = max(n["bot"] for n in col3)
out["p7_frasi_rule_y"] = 1686
out["p7_slack_px"] = 1686 - max(n["bot"] for n in col3)
out["p7_col3_note_lines"] = [(n["y"], n["fs"], n["t"]) for n in p7ed if n["x"] == 1473.0 and 1600 <= n["y"] <= 1686]
# line spacing in that note block
out["p7_note_spacing"] = [round(b - a, 2) for a, b in zip(
    [n["y"] for n in p7ed if n["x"] == 1473.0 and 1600 <= n["y"] <= 1686][:-1],
    [n["y"] for n in p7ed if n["x"] == 1473.0 and 1600 <= n["y"] <= 1686][1:])]

# ---- 9. images: payload hash + credit lines ----
def images(d, page):
    res = []
    for e in elements(d + page + ".svg"):
        if e.tag.endswith("image"):
            href = e.get("href", "")
            res.append((e.get("x"), e.get("y"), e.get("width"), e.get("height"),
                        hashlib.sha256(href.encode()).hexdigest()[:16], len(href)))
    return res
for p in PAGES:
    out[f"img_ed_{p}"] = images(ED, p); out[f"img_co_{p}"] = images(CO, p)
def credits(d):
    res = []
    for p in PAGES:
        for n in texts(d + p + ".svg"):
            if re.search(r"Fonte|Wikimedia|Commons|©|Credit|Foto", n["t"]):
                res.append((p, n["t"]))
    return res
out["credits_ed"] = credits(ED); out["credits_co"] = credits(CO)

# ---- 10. furniture spot values ----
def find(d, page, pred):
    return [(n["x"], n["y"], n["fs"], n["t"]) for n in texts(d + page + ".svg") if pred(n["t"])]
out["furn_badge"] = find(ED, "p1-prima", lambda t: "Text in Italian" in t)
out["furn_footer"] = find(ED, "p1-prima", lambda t: t.startswith("La Lucerna ·"))
out["furn_subtitle"] = find(ED, "p1-prima", lambda t: "THE ITALIAN WEEKLY" in t)
out["furn_match"] = {}
for p in PAGES:
    out["furn_match"][p] = [n["t"] for n in texts(ED + p + ".svg") if "Match" in n["t"]]
out["furn_w43_subtitle"] = find(W43, "p1-prima", lambda t: "WEEKLY" in t and "VOL" in t)
out["furn_w43_match"] = {}
for p in ["p1-prima", "p2-vita", "p3-cultura", "p4-sport", "p5-giovani", "p6-approfondimento", "p7-lingua", "p8-valutazione"]:
    try:
        out["furn_w43_match"][p] = [n["t"] for n in texts(W43 + p + ".svg") if "Match" in n["t"]]
    except Exception as e:
        out["furn_w43_match"][p] = [f"ERR {e}"]
out["furn_w43_frase_title"] = []
try:
    for n in texts(W43 + "p2-vita.svg"):
        if "FRASE" in n["t"]:
            out["furn_w43_frase_title"].append((n["x"], n["y"], n["fs"], n["t"]))
except Exception as e:
    out["furn_w43_frase_title"] = [str(e)]
out["furn_ed_frase_title"] = [(n["x"], n["y"], n["fs"], n["t"]) for n in texts(ED + "p2-vita.svg") if "FRASE" in n["t"]]
out["furn_w43_files"] = __import__("os").listdir(W43)

with open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-en-proof/independent-scan.json", "w") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
print("ROW_ED", len(row_ed)); print("ROW_CO", len(row_co)); print("ROW_IDENTICAL", out["row_identical"])
print("RE_VIOL_ED", out["rightedge_ed_viol"]); print("RE_MARGIN_ED", out["rightedge_ed_margin"])
print("RE_MARGIN_IN_CORE", out["rightedge_margin_ed_texts_in_core"])
print("CHART_ED", out["chart_p6_ed_worst"][:3]); print("FRAME_ED", out["frame_ed"])
print("P7 col3 last bot", out["p7_col3_last_bot"], "slack", out["p7_slack_px"], "spacing", out["p7_note_spacing"])
print("GOLD_ED", out["gold_ed"])
for k in sorted(out):
    if k.startswith("gloss_"):
        print(k, out[k]["n"], out[k]["items"])
print("EXNUMS_ED", {k: len(v) for k, v in out["exnums_ed"].items()})
print("EXNUMS_CO", {k: len(v) for k, v in out["exnums_co"].items()})
print("IMG equal:", all(out[f"img_ed_{p}"] == out[f"img_co_{p}"] for p in PAGES))
for p in PAGES:
    if out[f"img_ed_{p}"] != out[f"img_co_{p}"]:
        print(" IMG DIFF", p, out[f"img_ed_{p}"], out[f"img_co_{p}"])
print("CREDITS_ED", out["credits_ed"]); print("CREDITS_CO", out["credits_co"])
print("BADGE", out["furn_badge"]); print("FOOTER", out["furn_footer"]); print("SUBTITLE", out["furn_subtitle"])
print("MATCH_ED", out["furn_match"]); print("W43_SUB", out["furn_w43_subtitle"]); print("W43_MATCH", out["furn_w43_match"])
print("FRASE_ED", out["furn_ed_frase_title"]); print("FRASE_W43", out["furn_w43_frase_title"]); print("W43_FILES", out["furn_w43_files"])
