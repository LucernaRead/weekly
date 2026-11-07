#!/usr/bin/env python3
"""Round 2 independent KO orphan scan (proofreader's own implementation).

Binding standard: tools README #16 extended - window 10-45 (line pitch),
line-initial orphan punctuation/particles AND mid-word splits with
>=3-syllable tails, for EVERY prose column (incl. parenthesised fragments).

Method (independent of Round 1 / fix-worker copies):
- Parse SVG <text> elements (x, y, font-size, text).
- Cluster elements into columns by x (cluster gap <= 25px), sort by y.
- For each consecutive pair in a column with 10 <= dy <= 45:
  - S1: continuation's first char is orphan punctuation, OR continuation's
    first whitespace-token is a bare particle (은/는/이/가/을/를/에/의/도/만).
  - TAIL: previous line ends in Hangul and continuation starts in Hangul
    and the continuation's first Hangul run has >= 3 syllables.
- Every candidate is printed for MANUAL adjudication against the source
  string and rendered context. A candidate is a TRUE split only if the
  break falls INSIDE one source word.
"""
import glob, os, re, sys
import xml.etree.ElementTree as ET

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
NS = "{http://www.w3.org/2000/svg}"
SYL = re.compile(r"[\uac00-\ud7a3]")
PUNCT = set(".,;:!?%)]}、。·…~–—\"'”’")
PARTICLES = {"은", "는", "이", "가", "을", "를", "에", "의", "도", "만", "에서", "으로", "로", "와", "과", "부터", "까지", "에게", "한테", "보다", "처럼"}


def load(fn):
    els = []
    for t in ET.parse(fn).getroot().iter(NS + "text"):
        els.append({"x": float(t.get("x")), "y": float(t.get("y")),
                    "size": float(t.get("font-size", "20")),
                    "text": "".join(t.itertext())})
    return els


def columns(els):
    xs = sorted(set(e["x"] for e in els))
    clusters = []
    for x in xs:
        if clusters and x - clusters[-1][-1] <= 25:
            clusters[-1].append(x)
        else:
            clusters.append([x])
    out = []
    for c in clusters:
        col = [e for e in els if e["x"] in c]
        col.sort(key=lambda e: e["y"])
        out.append(col)
    return out


def main():
    total = 0
    for fn in sorted(glob.glob(BASE + "/files/weekly-report-w46-es-ko/svg/*.svg")):
        els = load(fn)
        seen = set()
        for col in columns(els):
            for a, b in zip(col, col[1:]):
                dy = b["y"] - a["y"]
                if not (10 <= dy <= 45):
                    continue
                bt = b["text"].strip()
                at = a["text"].rstrip()
                if not bt or not at or not SYL.search(bt):
                    continue
                key = (round(a["y"], 1), round(b["y"], 1))
                if key in seen:
                    continue
                seen.add(key)
                kind = None
                if bt[0] in PUNCT:
                    kind = "S1-PUNCT"
                else:
                    first_tok = bt.split()[0] if bt.split() else ""
                    if first_tok in PARTICLES:
                        kind = "S1-PARTICLE"
                    elif SYL.search(at[-1]) and SYL.search(bt[0]):
                        m = re.match(r"^[\uac00-\ud7a3]+", bt)
                        if m and len(SYL.findall(m.group(0))) >= 3:
                            kind = "TAIL>=3"
                if kind:
                    total += 1
                    print(f"{os.path.basename(fn)} {kind} y={a['y']:.1f}->{b['y']:.1f} x={a['x']} fs={a['size']} | PREV: ...{at[-45:]} | CONT: {bt[:55]}")
    print(f"TOTAL CANDIDATES: {total}")


if __name__ == "__main__":
    main()
