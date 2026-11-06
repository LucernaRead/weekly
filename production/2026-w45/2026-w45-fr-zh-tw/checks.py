# -*- coding: utf-8 -*-
"""FR x ZH-TW W45 builder self-checks (run with tools venv python).

A. same-baseline ink spacing (P1 top y=92, footers y=2624)
B. right-edge scan (advance end / ink right > 1885)
C. orphan scan: single-CJK-char lines, closer-led lines, opener-ended
   lines; plus P8 key-line spacing coverage of the 10-45 window
D. P6 calendar-label ink vs later-drawn rects (baseline-anchored <30%)
E. gloss item counts, split on '·' (README #21), core vs edition
F. frozen points (41e/40e, Q120, P7 #4/#8, Q106, P6 calendar sentence)
G. simplified-residual scan (opencc s2twp char flags + mainland words)
H. image payload dual-diameter (core vs edition base64 sha256)
I. furniture three-way (W43 fr-zh-tw vs W45 core vs this edition)
J. quote-char counts per page, core vs edition
"""
import base64
import collections
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/tools"))
from svglib import text_w
from occlusion_audit import ink_box

G = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(G, "files/weekly-report-w45-fr-zh-tw/svg")
CO = os.path.join(G, "files/weekly-report-w45-fr-core/svg")
W43 = os.path.join(G, "files/weekly-report-fr-zh-tw/svg")
PAGES = ["p1-une", "p2-vie", "p3-culture", "p4-sport", "p5-jeunesse",
         "p6-politique", "p7-langue", "p8-exercices"]
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" '
                  r'font-size="([\d.]+)"([^>]*)>([^<]*)</text>')


def texts(path):
    out = []
    for m in ATTR.finditer(open(path, encoding="utf-8").read()):
        attrs = m.group(5)
        bold = 'font-weight="700"' in attrs
        am = re.search(r'text-anchor="([^"]*)"', attrs)
        out.append(dict(x=float(m.group(1)), y=float(m.group(2)),
                        fam=m.group(3), size=float(m.group(4)), bold=bold,
                        anchor=am.group(1) if am else "start", s=m.group(6)))
    return out


def adv(e):
    kind = "serif" if "Serif" in e["fam"] else "sans"
    return text_w(e["s"], kind, e["bold"], e["size"])


def ink(e):
    try:
        return ink_box(e["s"], e["fam"], e["size"], e["bold"], e["x"],
                       e["y"], e["anchor"])
    except Exception as ex:
        return ("ERR", str(ex))


print("== A. same-baseline spacing ==")
for pg in PAGES:
    ts = texts(os.path.join(ED, pg + ".svg"))
    for y in (92.0, 2624.0):
        row = sorted([e for e in ts if e["y"] == y], key=lambda e: e["x"])
        gaps = []
        for a, b in zip(row, row[1:]):
            ia, ib = ink(a), ink(b)
            if isinstance(ia, tuple) and len(ia) == 4 and \
               isinstance(ib, tuple) and len(ib) == 4:
                gaps.append(round(ib[0] - ia[2], 1))
        print(f"  {pg} y={y}: {len(row)} segs, ink gaps {gaps} "
              f"{'OVERLAP!' if any(g < 0 for g in gaps) else 'ok'}")

print("== B. right-edge scan ==")
bad = 0
for pg in PAGES:
    for e in texts(os.path.join(ED, pg + ".svg")):
        a = adv(e)
        ae = e["x"] + a if e["anchor"] == "start" else \
            (e["x"] - a if e["anchor"] == "end" else e["x"] + a / 2)
        ib = ink(e)
        ir = ib[2] if isinstance(ib, tuple) and len(ib) == 4 else None
        if ae > 1885 or (ir is not None and ir > 1885):
            print(f"  {pg} y={e['y']}: adv_end={ae:.1f} ink_right={ir} "
                  f"{e['s'][:60]!r}")
            bad += 1
print(f"  right-edge violations: {bad}")

print("== C. orphan scan ==")
CJK = re.compile(r"[\u4e00-\u9fff]")
CLOSERS = set("。，、；：？！」』）)]")
OPENERS = set("（「『([")
for pg in PAGES:
    flags = []
    for e in texts(os.path.join(ED, pg + ".svg")):
        s = e["s"]
        cj = CJK.findall(s)
        if len(cj) == 1 and len(s.strip()) <= 3 and e["size"] >= 19:
            flags.append(("single-char", e["y"], s))
        if s[:1] in CLOSERS:
            flags.append(("closer-led", e["y"], s[:40]))
        if s[-1:] in OPENERS:
            flags.append(("opener-ended", e["y"], s[-40:]))
    print(f"  {pg}: {len(flags)} flags {flags[:8]}")
# P8 key-line spacing coverage of the 10-45 window
p8 = texts(os.path.join(ED, "p8-exercices.svg"))
ys = sorted(set(e["y"] for e in p8 if e["y"] > 1600))
gaps = [round(b - a, 2) for a, b in zip(ys, ys[1:])]
print(f"  P8 keys-region line gaps: min={min(gaps)} max={max(gaps)} "
      f"n={len(gaps)} (window 10-45 covers: "
      f"{all(10 <= g <= 45 for g in gaps)})")

print("== D. P6 calendar-label ink vs later rects ==")
src6 = open(os.path.join(ED, "p6-politique.svg"), encoding="utf-8").read()
# paint order = document order; combined pattern over rects + texts
combo = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" '
                   r'height="([\d.]+)"[^>]*>|<text x="([\d.]+)" y="([\d.]+)" '
                   r'font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
ordered = []
for m in combo.finditer(src6):
    if m.group(1) is not None:
        ordered.append(("rect", float(m.group(1)), float(m.group(2)),
                        float(m.group(3)), float(m.group(4))))
    else:
        attrs = m.group(9)
        ordered.append(("text", float(m.group(5)), float(m.group(6)),
                        m.group(7), float(m.group(8)),
                        'font-weight="700"' in attrs,
                        (re.search(r'text-anchor="([^"]*)"', attrs).group(1)
                         if 'text-anchor' in attrs else "start"),
                        m.group(10)))
worst = 0.0
worst_desc = None
for i, el in enumerate(ordered):
    if el[0] != "text":
        continue
    _, x, y, fam, size, bold, anchor, s = el
    ib = ink_box(s, fam, size, bold, x, y, anchor)
    if not (isinstance(ib, tuple) and len(ib) == 4):
        continue
    l, t, r, b = ib
    area = max(0.0, (r - l) * (b - t))
    if area <= 0:
        continue
    for later in ordered[i + 1:]:
        if later[0] != "rect":
            continue
        _, rx, ry, rw, rh = later
        ox = max(0.0, min(r, rx + rw) - max(l, rx))
        oy = max(0.0, min(b, ry + rh) - max(t, ry))
        frac = (ox * oy) / area
        if frac > worst:
            worst, worst_desc = frac, (s[:40], rx, ry, rw, rh)
print(f"  worst later-rect ink coverage on P6: {worst:.3f} {worst_desc} "
      f"(gate <0.30: {'PASS' if worst < 0.30 else 'FAIL'})")

print("== E. gloss box line counts (render level) ==")
# render-level: count gloss-prefix lines core vs edition; item-level
# counts (split on '·') are verified at source level in the KIT audit
for pg in PAGES:
    c = sum(1 for e in texts(os.path.join(CO, pg + ".svg"))
            if e["s"].startswith("译注｜"))
    e2 = sum(1 for e in texts(os.path.join(ED, pg + ".svg"))
             if e["s"].startswith("譯注｜"))
    print(f"  {pg}: gloss lines core={c} edition={e2} "
          f"{'OK' if c == e2 else 'MISMATCH'}")

print("== F. frozen points ==")
all_ed = {pg: "".join(t["s"] for t in texts(os.path.join(ED, pg + ".svg")))
          for pg in PAGES}
p4 = all_ed["p4-sport"]
print(f"  P4 '41e édition en 2026 (40e anniversaire)': "
      f"{p4.count('41e édition en 2026 (40e anniversaire)')} (expect 1)")
print(f"  whole-edition '40e' occurrences: "
      f"{sum(s.count('40e') for s in all_ed.values())} (expect 1)")
p8t = all_ed["p8-exercices"]
print("  Q120 stem present:",
      "Si j'étais libre dimanche" in "".join(
          t["s"] for t in texts(os.path.join(ED, "p8-exercices.svg"))))
p7t = all_ed["p7-langue"]
print("  P7 #4 verbatim:",
      p7t.count("plus excitante ou plus frustrante ?"), "(expect >=3: "
      "column + outils + golden)")
print("  P7 #8 verbatim:",
      p7t.count("Les jeunes créateurs y rencontrent leur public, en vrai."),
      "(expect >=2: clinic key + golden)")
print("  Q106 error 'rencontre' present:",
      "y rencontre leur public" in p7t)
p6t = all_ed["p6-politique"]
print("  P6 calendar sentence:",
      p6t.count("Ce calendrier peut encore bouger."), "(expect >=1)")
print("  P6 micro key 'peut' in P6:", "peut" in p6t)

print("== G. simplified-residual scan ==")
from opencc import OpenCC
cc = OpenCC("s2twp")
ed_chars = set()
for pg in PAGES:
    for e in texts(os.path.join(ED, pg + ".svg")):
        ed_chars |= {c for c in e["s"] if "\u4e00" <= c <= "\u9fff"}
flags = sorted(c for c in ed_chars if cc.convert(c) != c)
print(f"  distinct CJK chars in edition: {len(ed_chars)}")
print(f"  s2twp-flagged chars: {flags}")
MAINLAND = ["视频", "屏幕", "网络", "软件", "信息", "邮件", "博客", "鼠标",
            "键盘", "光盘", "打印", "质量", "节目", "动画", "元音", "三单",
            "范文", "示例", "邮局", "邮寄", "发廊", "头发", "干活",
            "谷物", "咸菜", "土豆", "西红柿", "黄瓜", "菠菜", "草莓", "樱桃"]
alltext = "".join(all_ed.values())
hits = [w for w in MAINLAND if w in alltext]
print(f"  mainland-word hits: {hits if hits else 'NONE'}")

print("== H. image payload dual-diameter ==")
def payloads(path):
    src = open(path, encoding="utf-8").read()
    return [hashlib.sha256(base64.b64decode(m)).hexdigest()
            for m in re.findall(r'data:image/\w+;base64,([A-Za-z0-9+/=]+)', src)]
for pg in PAGES:
    pc, pe = payloads(os.path.join(CO, pg + ".svg")), payloads(
        os.path.join(ED, pg + ".svg"))
    print(f"  {pg}: core={len(pc)} ed={len(pe)} "
          f"identical={pc == pe} {pe[:2] if pe else []}")

print("== I. furniture three-way ==")
def first(path, pred):
    for e in texts(path):
        if pred(e["s"]):
            return e["s"]
    return None
for label, pred in [
        ("badge", lambda s: "講解" in s or "讲解" in s),
        ("footer", lambda s: "Lucerna ·" in s and "週報" in s or
         "Lucerna ·" in s and "周报" in s)]:
    print(f"  {label} W43: {first(os.path.join(W43, 'p1-une.svg'), pred)}")
    print(f"  {label} core: {first(os.path.join(CO, 'p1-une.svg'), pred)}")
    print(f"  {label} ed: {first(os.path.join(ED, 'p1-une.svg'), pred)}")

print("== J. quote counts per page ==")
for pg in PAGES:
    qc = collections.Counter("".join(t["s"] for t in texts(
        os.path.join(CO, pg + ".svg"))))
    qe = collections.Counter("".join(t["s"] for t in texts(
        os.path.join(ED, pg + ".svg"))))
    diffs = {ch: (qc.get(ch, 0), qe.get(ch, 0)) for ch in "«»「」“”‘’'\""
             if qc.get(ch, 0) != qe.get(ch, 0)}
    print(f"  {pg}: quote diffs: {diffs if diffs else 'NONE'}")
