#!/usr/bin/env python3
# Independent proof scan for W45 FR x KO. Own code; ink boxes reuse the
# canonical tools/occlusion_audit.py ink_box (same anchoring as the gate).
import sys, os, re, glob, json
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
import occlusion_audit as OA

BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
ED = f"{BASE}/files/weekly-report-w45-fr-ko"
CO = f"{BASE}/files/weekly-report-w45-fr-core"
SRC = ""
for sf in sorted(glob.glob("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-ko-proof/work/repro-build/content*.py")):
    SRC += open(sf, encoding="utf-8").read() + "\n"

def texts(path):
    out = []
    for el in ET.parse(path).getroot().iter():
        if el.tag.endswith("text"):
            out.append({"x": float(el.get("x") or 0), "y": float(el.get("y") or 0),
                        "size": float(el.get("font-size") or 20),
                        "bold": el.get("font-weight") == "bold",
                        "anchor": el.get("text-anchor") or "start",
                        "fam": el.get("font-family") or "",
                        "s": "".join(el.itertext())})
    return out

def ink(n):
    try:
        return OA.ink_box(n["s"], n["fam"], n["size"], n["bold"], n["x"], n["y"], n["anchor"])
    except Exception:
        return None

def svgfiles(d):
    return sorted(glob.glob(d + "/svg/*.svg"))

out = {}
# 1 rowcheck
bad = []
for f in svgfiles(ED):
    rows = defaultdict(list)
    for n in texts(f):
        if n["y"] < 200 or abs(n["y"] - 2624) < 1:
            rows[round(n["y"])].append(n)
    for y, g in rows.items():
        boxes = sorted([(ink(n), n["s"][:50]) for n in g if ink(n)])
        for (b1, s1), (b2, s2) in zip(boxes, boxes[1:]):
            if b2[0] < b1[2] - 1:
                bad.append((os.path.basename(f), y, s1, round(b1[2], 1), s2, round(b2[0], 1)))
out["rowcheck"] = bad
print("ROWCHECK", len(bad), bad[:10])

# 2 right-edge + 3 frame
over, cross = [], []
for f in svgfiles(ED):
    for n in texts(f):
        b = ink(n)
        if not b: continue
        if b[2] > 1885.5: over.append((os.path.basename(f), round(n["y"], 1), round(b[2], 1), n["s"][:60]))
        if b[0] < 40 or b[2] > 1910 or b[1] < 40 or b[3] > 2660:
            cross.append((os.path.basename(f), round(n["y"], 1), tuple(round(v, 1) for v in b), n["s"][:50]))
out["right_edge"] = over; out["frame"] = cross
print("RIGHT_EDGE", len(over), over)
print("FRAME", len(cross), cross)

# 4 P6 chart labels
t = ET.parse(f"{ED}/svg/p6-politique.svg").getroot()
rects = []
for el in t.iter():
    if el.tag.endswith("rect"):
        try: rects.append((float(el.get("x")), float(el.get("y")), float(el.get("width")), float(el.get("height"))))
        except (TypeError, ValueError): pass
hits = []
for n in texts(f"{ED}/svg/p6-politique.svg"):
    if 1330 <= n["y"] <= 1800 and n["x"] < 1000:
        b = ink(n)
        if not b: continue
        for (rx, ry, rw, rh) in rects:
            if not (b[2] < rx or b[0] > rx + rw or b[3] < ry or b[1] > ry + rh):
                hits.append((round(n["y"], 1), (round(rx, 1), round(ry, 1), round(rw, 1), round(rh, 1)), n["s"][:50]))
                break
out["p6_chart"] = hits
print("P6_CHART", len(hits), hits)

# 5 kinsoku + 6 Han
CLOSERS = set(")]}〉》.,!?%:;\"'」』）〕，。、！？；：")
starts = []
han = re.compile(r'[\u4e00-\u9fff]')
han_nodes = {}
for f in svgfiles(ED):
    ns = texts(f)
    han_nodes[os.path.basename(f)] = sum(1 for x in ns if han.search(x["s"]))
    for n in ns:
        s = n["s"].strip()
        if s and s[0] in CLOSERS:
            starts.append((os.path.basename(f), round(n["y"], 1), s[:60]))
out["kinsoku"] = starts; out["han_nodes"] = han_nodes
print("KINSOKU", len(starts), starts)
print("HAN_NODES", han_nodes, "total", sum(han_nodes.values()))

# 8 orphan 10-45
HANG = re.compile(r'[\uac00-\ud7a3]')
def syll(s): return len(HANG.findall(s))
flags = []
for f in svgfiles(ED):
    ns = texts(f)
    cols = defaultdict(list)
    for n in ns: cols[round(n["x"])].append(n)
    for x, g in cols.items():
        g.sort(key=lambda n: n["y"])
        for prev, cur in zip(g, g[1:]):
            dy = cur["y"] - prev["y"]
            if dy < 10 or dy > 45: continue
            ps, cs = prev["s"], cur["s"]
            if cs and cs[0] in CLOSERS:
                flags.append(("START-CLOSER", os.path.basename(f), round(cur["y"], 1), cs[:40], ps[-20:]))
            if ps and cs and HANG.search(ps[-1]) and HANG.search(cs[0]) and ps[-1] not in " .,;:!?·—-":
                run = cs.split(" ")[0]
                if syll(run) >= 3:
                    tail = ps.split(" ")[-1].lstrip("("); run_c = run.rstrip(")")
                    nospace = (tail + run_c) in SRC; spaced = (tail + " " + run_c) in SRC
                    verdict = "SPLIT>=3" if (nospace and not spaced) else ("SPACE-BREAK" if (spaced and not nospace) else ("AMBIG" if (nospace and spaced) else "CROSS-BLOCK"))
                    if verdict in ("SPLIT>=3", "AMBIG"):
                        flags.append((verdict, os.path.basename(f), round(cur["y"], 1), ps[-12:], cs[:30], syll(run_c)))
            cst = cs.strip()
            if len(cst) <= 2 and HANG.search(cst or " ") and len(ps.strip()) > 10:
                flags.append(("LONE-FRAG", os.path.basename(f), round(cur["y"], 1), cst, ps[-20:]))
out["orphan"] = flags
print("ORPHAN", len(flags))
for fl in flags: print("  ", fl)

# 9 P8 calibers + P7 bottoms
def calibers(d, name):
    p8 = texts(f"{d}/svg/p8-exercices.svg")
    # battery block: baselines < 1560 (header RÉPONSES sits below); keys block: >= 1560
    bat = [n for n in p8 if n["y"] < 1560]; keys = [n for n in p8 if n["y"] >= 1560]
    def meas(ns):
        bs = [ink(n) for n in ns]; bs = [b for b in bs if b]
        return {"max_baseline": max(n["y"] for n in ns), "max_ink_bottom": round(max(b[3] for b in bs), 1), "n": len(ns)}
    p7 = texts(f"{d}/svg/p7-langue.svg")
    res = {"battery": meas(bat), "keys": meas(keys),
           "p7_max_baseline": max(n["y"] for n in p7),
           "p7_texts_below_1900": [(round(n["y"], 1), n["s"][:60]) for n in p7 if n["y"] > 1900]}
    # P7 rects
    rt = ET.parse(f"{d}/svg/p7-langue.svg").getroot()
    res["p7_rects"] = [(round(float(el.get("x")), 1), round(float(el.get("y")), 1), round(float(el.get("width")), 1), round(float(el.get("height")), 1))
                       for el in rt.iter() if el.tag.endswith("rect") and el.get("y") and float(el.get("y")) > 1500]
    print(name, json.dumps(res, ensure_ascii=False))
    return res
out["cal_ed"] = calibers(ED, "ED")
out["cal_co"] = calibers(CO, "CO")

# 10 images
def images(d):
    res = {}
    for f in svgfiles(d):
        root = ET.parse(f).getroot(); lst = []
        for el in root.iter():
            if el.tag.endswith("image"):
                href = el.get("{http://www.w3.org/1999/xlink}href") or el.get("href") or ""
                import hashlib, base64
                payload = href.split(",", 1)[1] if "," in href else ""
                lst.append({"x": el.get("x"), "y": el.get("y"), "w": el.get("width"), "h": el.get("height"),
                            "sha": hashlib.sha256(base64.b64decode(payload)).hexdigest() if payload else None,
                            "bytes": len(base64.b64decode(payload)) if payload else 0})
        res[os.path.basename(f)] = lst
    return res
out["img_ed"] = images(ED); out["img_co"] = images(CO)
for k in out["img_ed"]:
    print("IMG", k, "ed", out["img_ed"][k], "co", out["img_co"].get(k))

json.dump(out, open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-ko-proof/work/myscan.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("SAVED myscan.json")
