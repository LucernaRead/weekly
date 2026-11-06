#!/usr/bin/env python3
# Independent proof scans for W45 IT x KO. Fresh implementation, not a copy
# of the builder's ko_scans.py. Reads only: edition SVGs + edition build
# content sources (for the source-word set). Writes nothing into delivery.
import glob, json, os, re, sys
from PIL import ImageFont

ED = sys.argv[1]
BUILD = sys.argv[2]
OUT = sys.argv[3]

SERIF = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SERIF_B = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SANS = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SANS_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
# SVGs declare CJK SC family; SC face index = 2 (tables.json font table).
def font(fam, bold, size):
    p = (SERIF_B if bold else SERIF) if "Serif" in fam else (SANS_B if bold else SANS)
    return ImageFont.truetype(p, int(round(size)), index=2)

def hang(ch): return "\uac00" <= ch <= "\ud7a3"
def syll(tok): return sum(1 for c in tok if hang(c))
STRIP = "()[]{}<>\"'\u201c\u201d\u2018\u2019\u00b7,.;:!? \u3002\uff0c\u3001\uff1a\uff1b\uff1f\uff01\uff09\u300b\u300d\u300f"
def strip_p(tok): return tok.strip(STRIP)

TEXT_RE = re.compile(
    r'<text x="([\d.]+)" y="([\d.]+)"(?: font-family="([^"]*)")?'
    r'(?: font-size="([\d.]+)")?(?: font-weight="([^"]*)")?'
    r'(?: fill="([^"]*)")?(?: text-anchor="([^"]*)")?[^>]*>([^<]*)</text>')
def parse(path):
    s = open(path, encoding="utf-8").read()
    nodes = []
    for m in TEXT_RE.finditer(s):
        nodes.append({"x": float(m.group(1)), "y": float(m.group(2)),
                      "fam": m.group(3) or "", "size": float(m.group(4)) if m.group(4) else 20.0,
                      "bold": m.group(5) == "700", "anchor": m.group(7) or "start",
                      "t": m.group(8)})
    return nodes, s

# source-word set from edition build content (read-only)
src = set()
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    s = open(os.path.join(BUILD, f), encoding="utf-8").read()
    for lit in re.findall(r'"(?:[^"\\]|\\.)*"', s):
        body = lit[1:-1]
        if any(hang(c) for c in body):
            for tok in body.split():
                st = strip_p(tok)
                if st: src.add(st)

res = {}
ORPHAN_START = set("\u3002\uff0c\u3001\uff1a\uff1b\uff1f\uff01\uff09\u300b\u300d\u300f.?! )".replace(" ", ""))
for p in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    pg = os.path.basename(p)
    nodes, s = parse(p)
    cands, start_orph, final_frag = [], [], []
    for i, (a, b) in enumerate(zip(nodes, nodes[1:])):
        if not any(hang(c) for c in a["t"]):
            continue
        dy = b["y"] - a["y"]
        same_col = abs(b["x"] - a["x"]) < 1
        col_trans = b["x"] > a["x"] + 100 and b["y"] < a["y"]
        if not ((same_col and 10 <= dy <= 45) or col_trans):
            continue
        if re.match(r"^\d+[.\-–]", b["t"].strip()):
            continue
        if b["t"] and b["t"][0] in ORPHAN_START and any(hang(c) for c in b["t"]):
            start_orph.append({"prev_y": a["y"], "y": b["y"], "prev": a["t"], "line": b["t"]})
        at, bt = a["t"].split(), b["t"].split()
        if not at or not bt:
            continue
        f1, f2 = strip_p(at[-1]), strip_p(bt[0])
        if f1 and f2 and (f1 + f2) in src:
            cands.append({"prev_y": a["y"], "y": b["y"], "frag": f1 + "|" + f2,
                          "tail_syll": syll(f2), "prev": a["t"], "line": b["t"],
                          "gate": syll(f2) >= 3})
    # block-final lines: a node whose successor is NOT a same-col continuation
    for i, a in enumerate(nodes):
        if i + 1 >= len(nodes):
            continue
        b = nodes[i + 1]
        dy = b["y"] - a["y"]
        cont = (abs(b["x"] - a["x"]) < 1 and 10 <= dy <= 45) or (b["x"] > a["x"] + 100 and b["y"] < a["y"])
        if cont:
            continue
        # a is final line of its run; flag only if it is a short fragment
        # following a same-column predecessor (i.e. a wrapped tail)
        if i > 0:
            pr = nodes[i - 1]
            if abs(pr["x"] - a["x"]) < 1 and 10 <= a["y"] - pr["y"] <= 45:
                toks = a["t"].split()
                if toks and syll(a["t"]) <= 2 and any(hang(c) for c in a["t"]):
                    final_frag.append({"y": a["y"], "line": a["t"], "syll": syll(a["t"])})
    # all line-start orphan punctuation (broader than pair-window version)
    all_start = [{"y": n["y"], "line": n["t"]} for n in nodes
                 if n["t"] and n["t"][0] in ORPHAN_START and any(hang(c) for c in n["t"])]
    # right-edge ADVANCE scan, band [40,1910]
    edge = []
    for n in nodes:
        f = font(n["fam"], n["bold"], n["size"])
        adv = f.getlength(n["t"])
        if n["anchor"] == "middle": lo, hi = n["x"] - adv / 2, n["x"] + adv / 2
        elif n["anchor"] == "end": lo, hi = n["x"] - adv, n["x"]
        else: lo, hi = n["x"], n["x"] + adv
        if lo < 40 or hi > 1910:
            edge.append({"y": n["y"], "anchor": n["anchor"], "lo": round(lo, 1), "hi": round(hi, 1), "t": n["t"]})
    # same-baseline collisions on EVERY baseline (advance intervals)
    base = []
    bands = {}
    for n in nodes:
        bands.setdefault(round(n["y"], 1), []).append(n)
    for yy, ns in bands.items():
        ivs = []
        for n in ns:
            f = font(n["fam"], n["bold"], n["size"])
            adv = f.getlength(n["t"])
            if n["anchor"] == "middle": lo, hi = n["x"] - adv / 2, n["x"] + adv / 2
            elif n["anchor"] == "end": lo, hi = n["x"] - adv, n["x"]
            else: lo, hi = n["x"], n["x"] + adv
            ivs.append((lo, hi, n["t"]))
        ivs.sort()
        for (l1, h1, t1), (l2, h2, t2) in zip(ivs, ivs[1:]):
            if h1 > l2 + 0.5:
                base.append({"y": yy, "a": t1, "b": t2, "overlap": round(h1 - l2, 1)})
    res[pg] = {"split_candidates": cands, "gate_ge3": [c for c in cands if c["gate"]],
               "line_start_orphan_pairs": start_orph, "line_start_orphan_all": all_start,
               "final_fragments": final_frag, "right_edge_advance": edge,
               "same_baseline_overlaps": base}
    print(f"{pg}: splits={len(cands)} gate>=3={len([c for c in cands if c['gate']])} "
          f"max_tail={max([c['tail_syll'] for c in cands], default=0)} "
          f"start_orph_pairs={len(start_orph)} start_orph_all={len(all_start)} "
          f"final_frag={len(final_frag)} edge={len(edge)} base_overlaps={len(base)}")
    for c in cands:
        print(f"   SPLIT tail={c['tail_syll']} {'GATE' if c['gate'] else 'ok'} {c['frag']} :: {c['prev']!r} // {c['line']!r}")
    for o in start_orph:
        print(f"   START-ORPHAN :: {o['prev']!r} // {o['line']!r}")
    for o in all_start:
        print(f"   START-ALL :: y={o['y']} {o['line']!r}")
    for o in final_frag:
        print(f"   FINAL-FRAG y={o['y']} syll={o['syll']} {o['line']!r}")
    for o in edge:
        print(f"   EDGE {o}")
    for o in base:
        print(f"   BASE-OVERLAP y={o['y']} +{o['overlap']}px {o['a']!r} // {o['b']!r}")

json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", OUT)
