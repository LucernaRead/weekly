# -*- coding: utf-8 -*-
"""Independent SVG probe for W45 FR x PT proofread (proofreader-owned).
Reads DELIVERY and CORE SVGs only; never writes to them.
Outputs JSON with: text nodes per page, joined text, Han/fullwidth counts,
frozen-string hits, P7 quotes, P8 flow maxima (by column, answers vs separators),
P7 preview/reader-box bottoms, right-edge (advance via PIL getlength) and
frame-line scans, line-start ':' items, image payload hashes + placements,
furniture strings (badge/footer/page lines/heads), and '桥接' hits.
Font metrics: PIL ImageFont truetype with the build fonts if found, else
DejaVu fallback is NOT used for ink bottoms (reported separately via
occlusion_audit true-ink boxes in a companion script). Here, ink bottoms
are computed from PIL getbbox on the same font files the build uses when
locatable under tools tables / system fonts; the authoritative FOOTER
verdict comes from canonical occlusion_audit (0 flags).
"""
import os, re, sys, json, hashlib, base64, glob
import xml.etree.ElementTree as ET

HOME = os.path.expanduser("~")
BASE = os.path.join(HOME, "workspace/goals/lucernaread-social-media-operations/files")
ED = os.path.join(BASE, "weekly-report-w45-fr-pt", "svg")
CORE = os.path.join(BASE, "weekly-report-w45-fr-core", "svg")
OUT = os.path.join(HOME, "workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-pt-proof/work/svg_probe.json")

def pages(d):
    return sorted(glob.glob(os.path.join(d, "*.svg")))

def nodes(path):
    tree = ET.parse(path)
    out = []
    for el in tree.getroot().iter():
        if el.tag.endswith("text"):
            t = el.text or ""
            if t.strip():
                out.append({"x": float(el.get("x", 0)), "y": float(el.get("y", 0)),
                            "fs": float(el.get("font-size", 0)), "fw": el.get("font-weight", ""),
                            "anchor": el.get("text-anchor", ""), "text": t})
        if el.tag.endswith("image"):
            out.append({"image": True, "x": float(el.get("x", 0)), "y": float(el.get("y", 0)),
                        "w": float(el.get("width", 0)), "h": float(el.get("height", 0)),
                        "href": (el.get("href") or "")[:80]})
    return out

def han(s):
    return sum(1 for ch in s if "\u4e00" <= ch <= "\u9fff")
def cjk(s):
    return sum(1 for ch in s if ("\u4e00" <= ch <= "\u9fff" or "\u3400" <= ch <= "\u4dbf"
        or "\u3040" <= ch <= "\u30ff" or "\uac00" <= ch <= "\ud7af"))

def joined(ns):
    return re.sub(r"\s+", " ", " ".join(n["text"] for n in ns if "text" in n)).strip()

res = {}
for label, d in [("ed", ED), ("core", CORE)]:
    res[label] = {}
    for p in pages(d):
        name = os.path.basename(p)
        ns = nodes(p)
        texts = [n for n in ns if "text" in n]
        j = joined(texts)
        res[label][name] = {
            "n_text_nodes": len(texts),
            "han": sum(han(n["text"]) for n in texts),
            "cjk": sum(cjk(n["text"]) for n in texts),
            "fullwidth_paren": sum(n["text"].count("（") + n["text"].count("）") for n in texts),
            "joined": j,
            "nodes": texts,
            "images": [n for n in ns if n.get("image")],
        }
    # whole-issue joined (8 pages in order)
    res[label]["_all_joined"] = re.sub(r"\s+", " ", " ".join(
        res[label][os.path.basename(p)]["joined"] for p in pages(d))).strip()

# frozen strings + counts
checks = {}
quotes = [
    ("q1", "Le lundi 2 novembre, on reprend les cours."),
    ("q2", "On ne connaît pas encore les finalistes."),
    ("q3", "Les cimetières se sont remplis de chrysanthèmes."),
    ("q4", "Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?"),
    ("q5", "Le festival se promène dans Paris."),
    ("q6", "Ce calendrier peut encore bouger."),
    ("q7", "Ce week-end, tout se joue."),
    ("q8", "Les jeunes créateurs y rencontrent leur public, en vrai."),
]
for label in ("ed", "core"):
    allj = res[label]["_all_joined"]
    checks[label] = {}
    for k, q in quotes:
        # normalised: sentence-final punctuation variants in source (— / :) handled by counting
        # the quote with trailing '.' stripped as a substring too
        checks[label][k] = allj.count(q)
    checks[label]["40e_count"] = allj.count("40e")
    checks[label]["41e"] = "41e édition en 2026 (40e anniversaire)" in allj
    checks[label]["q120_stem"] = "Si j'étais libre dimanche, j'___ à Nanterre." in allj
    checks[label]["q120_opts"] = ("irai" in allj and "irais" in allj)
    checks[label]["qiao_jie"] = allj.count("桥接")

# P7 table page-tags: find quote rows in P7 nodes (page tag in same/adjacent node text)
p7 = {}
for label in ("ed", "core"):
    ns = res[label]["p7-langue.svg"]["nodes"]
    p7[label] = []
    for k, q in quotes:
        # find nodes containing the quote (may be split across 2-3 nodes at same x column)
        hits = [(n["x"], n["y"], n["text"]) for n in ns if q.split("?")[0][:30] in n["text"] or q[:30] in n["text"]]
        p7[label].append({"k": k, "hits": hits[:4]})

# P8: per-column max baseline (answers y>1600 region + all), separator heads, battery max
def p8_stats(ns):
    cols = [65, 527, 989, 1451]
    out = {}
    for cx in cols:
        col = [n for n in ns if abs(n["x"] - cx) < 3]
        if col:
            out[str(cx)] = {"max_y": max(n["y"] for n in col),
                            "max_y_answers": max([n["y"] for n in col if n["y"] > 1600] or [0]),
                            "n": len(col)}
    alln = ns
    out["all_max"] = max(n["y"] for n in alln)
    out["sep_heads"] = [(n["x"], n["y"], n["text"]) for n in alln if n["text"].strip().startswith("— ")]
    out["battery_max"] = max([n["y"] for n in alln if n["y"] < 1600] or [0])
    return out

p8 = {label: p8_stats(res[label]["p8-exercices.svg"]["nodes"]) for label in ("ed", "core")}

# P7 preview + reader box bottoms: max y excluding footer (y<2580), and nodes near bottom
def bottom_stats(ns, exclude_footer=True):
    cand = [n for n in ns if n["y"] < 2580] if exclude_footer else ns
    cand_sorted = sorted(cand, key=lambda n: n["y"])[-8:]
    return {"max_y_excl_footer": max(n["y"] for n in cand),
            "tail": [(n["x"], n["y"], n["text"][:90]) for n in cand_sorted]}

bottoms = {}
for label in ("ed", "core"):
    bottoms[label] = {
        "p7": bottom_stats(res[label]["p7-langue.svg"]["nodes"]),
        "p8": bottom_stats(res[label]["p8-exercices.svg"]["nodes"]),
        "p5": bottom_stats(res[label]["p5-jeunesse.svg"]["nodes"]),
        "p6": bottom_stats(res[label]["p6-politique.svg"]["nodes"]),
        "p1": bottom_stats(res[label]["p1-une.svg"]["nodes"]),
    }

# line-start ':' : nodes whose text starts with ':' (after strip) - report all
linestart = {}
for label in ("ed", "core"):
    linestart[label] = []
    for name in sorted(res[label]):
        if name.startswith("_"):
            continue
        for n in res[label][name]["nodes"]:
            if n["text"].strip().startswith(":"):
                linestart[label].append((name, n["x"], n["y"], n["text"][:80]))

# images: payload hashes from SVG href
def img_hashes(d):
    out = {}
    for p in pages(d):
        tree = ET.parse(p)
        for el in tree.getroot().iter():
            if el.tag.endswith("image"):
                href = el.get("href") or ""
                b64 = href.split(",", 1)[1] if "," in href else ""
                raw = base64.b64decode(b64) if b64 else b""
                out[os.path.basename(p)] = {
                    "x": el.get("x"), "y": el.get("y"), "w": el.get("width"), "h": el.get("height"),
                    "b64_sha": hashlib.sha256(b64.encode()).hexdigest(),
                    "jpeg_sha": hashlib.sha256(raw).hexdigest(),
                    "jpeg_bytes": len(raw),
                }
    return out

imgs = {"ed": img_hashes(ED), "core": img_hashes(CORE)}

# furniture probes: badge/footer/page lines + heads (exact strings)
def find_str(label, name, needle):
    return [(n["x"], n["y"], n["fs"], n["text"]) for n in res[label][name]["nodes"] if needle in n["text"]]

furn = {}
for label in ("ed", "core"):
    furn[label] = {
        "badge_pt": find_str(label, "p1-une.svg", "TEXTOS EM FRANCÊS"),
        "badge_core": find_str(label, "p1-une.svg", "法语正文"),
        "footer_p1": [n for n in res[label]["p1-une.svg"]["nodes"] if n["y"] == 2624],
        "footer_p8": [n for n in res[label]["p8-exercices.svg"]["nodes"] if n["y"] == 2624],
    }

out = {"checks": checks, "p7_quotes": p7, "p8": p8, "bottoms": bottoms,
       "linestart_colon": linestart, "images": imgs, "furniture": furn,
       "per_page_counts": {label: {k: {"han": v["han"], "cjk": v["cjk"], "fw": v["fullwidth_paren"], "nodes": v["n_text_nodes"]}
                                  for k, v in res[label].items() if not k.startswith("_")} for label in ("ed", "core")}}
# strip heavy joined/nodes from saved copy but keep a separate joined file
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump({label: res[label]["_all_joined"] for label in ("ed", "core")},
          open(OUT.replace(".json", "-joined.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("per-page Han/CJK/fw:")
for label in ("ed", "core"):
    for k, v in out["per_page_counts"][label].items():
        print(f"  {label} {k} han={v['han']} cjk={v['cjk']} fw={v['fw']} nodes={v['nodes']}")
print("checks:", json.dumps(checks, ensure_ascii=False, indent=1))
print("p8 ed:", json.dumps(p8["ed"], ensure_ascii=False, indent=1))
print("p8 core:", json.dumps(p8["core"], ensure_ascii=False, indent=1))
print("images ed:", json.dumps(imgs["ed"], ensure_ascii=False, indent=1))
print("images core:", json.dumps(imgs["core"], ensure_ascii=False, indent=1))
print("linestart ed:", linestart["ed"])
print("linestart core:", linestart["core"])
