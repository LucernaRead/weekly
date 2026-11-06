# -*- coding: utf-8 -*-
"""Supplementary gates for the KO x FR W45 edition (fresh implementation).

Run with the tools venv python from this directory:
  python audit_fr.py <edition-svg-dir> <core-svg-dir> <wrap-log>
Sections: 1 advance right edge, 2 rect-border frame scan, 3 same-baseline
scan, 4 P6 label coverage (canonical ink_box, which anchors on the
getmetrics ascent), 5 rendered-line window scan (dy in 10..45), 6 P8 keys
flow end + P7 teaser end, 7 gloss counts, 8 phrase counts, 9 image payloads.
The wrap-log itself is produced by orphan_log.py (scratch copy only).
"""
import html
import json
import os
import re
import sys

TOOLS = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools")
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import occlusion_audit as OA
from svglib import text_w

HANGUL = re.compile(r"[\uac00-\ud7a3]")
HAN = re.compile(r"[\u4e00-\u9fff]")
NO_START = "。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;\""
TEXT_RE = re.compile(r'<text([^>]*)>(.*?)</text>')
RECT_RE = re.compile(r'<rect([^>]*)/?>')
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')


def _attrs(s):
    return dict(ATTR_RE.findall(s))


def parse_texts(path):
    out = []
    s = open(path, encoding="utf-8").read()
    for m in TEXT_RE.finditer(s):
        a = _attrs(m.group(1))
        if "x" not in a or "y" not in a or "font-size" not in a:
            continue
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        out.append({"x": float(a["x"]), "y": float(a["y"]),
                    "size": float(a["font-size"]),
                    "bold": a.get("font-weight") == "700",
                    "family": a.get("font-family", ""),
                    "anchor": a.get("text-anchor", "start"), "text": t})
    return out


def parse_rects(path):
    out = []
    s = open(path, encoding="utf-8").read()
    for m in RECT_RE.finditer(s):
        a = _attrs(m.group(1))
        if "stroke" in a and all(k in a for k in ("x", "y", "width", "height")):
            w, h = float(a["width"]), float(a["height"])
            if w > 0 and h > 0:
                out.append((float(a["x"]), float(a["y"]), w, h))
    return out


def kind_of(family):
    if "Serif" in family:
        return "serif"
    if "Sans" in family:
        return "sans"
    return None


def main():
    svgdir, coredir, wraplog = sys.argv[1], sys.argv[2], sys.argv[3]
    print("== 1. ADVANCE right-edge scan (inner frame x=1910) ==")
    worst = 0.0
    flags = []
    for fn in sorted(os.listdir(svgdir)):
        for t in parse_texts(os.path.join(svgdir, fn)):
            k = kind_of(t["family"])
            if k is None or not t["text"].strip():
                continue
            adv = text_w(t["text"], k, t["bold"], t["size"])
            if t["anchor"] == "middle":
                end = t["x"] + adv / 2
            elif t["anchor"] == "end":
                end = t["x"]
            else:
                end = t["x"] + adv
            worst = max(worst, end)
            if end > 1910:
                flags.append((fn, t["text"][:40], round(end, 1)))
    print(f"  worst advance end: {worst:.1f} (frame 1910); flags: {len(flags)}")
    for f in flags:
        print("   FLAG", f)

    print("== 2. Rect-border frame scan (ink vs stroked rect borders) ==")
    bflags = []
    for fn in sorted(os.listdir(svgdir)):
        path = os.path.join(svgdir, fn)
        rects = parse_rects(path)
        for t in parse_texts(path):
            ib = OA.ink_box(t["text"], t["family"], t["size"], t["bold"], t["x"], t["y"], t["anchor"])
            if ib is None:
                continue
            l, tp, r, b = ib
            for (rx, ry, rw, rh) in rects:
                # horizontal borders
                for by in (ry, ry + rh):
                    if tp < by < b and l < rx + rw and r > rx:
                        bflags.append((fn, "h-border", round(by, 1), t["text"][:40]))
                for bx in (rx, rx + rw):
                    if l < bx < r and tp < ry + rh and b > ry:
                        bflags.append((fn, "v-border", round(bx, 1), t["text"][:40]))
    print(f"  border-crossing flags: {len(bflags)}")
    for f in bflags[:40]:
        print("   FLAG", f)

    print("== 3. Same-baseline ink overlap scan (0.6px tolerance) ==")
    sflags = []
    for fn in sorted(os.listdir(svgdir)):
        texts = parse_texts(os.path.join(svgdir, fn))
        boxes = []
        for t in texts:
            ib = OA.ink_box(t["text"], t["family"], t["size"], t["bold"], t["x"], t["y"], t["anchor"])
            if ib:
                boxes.append((t, ib))
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                (t1, b1), (t2, b2) = boxes[i], boxes[j]
                if abs(t1["y"] - t2["y"]) > 0.6:
                    continue
                if b1[0] < b2[2] and b2[0] < b1[2]:
                    sflags.append((fn, round(t1["y"], 1), t1["text"][:30], t2["text"][:30]))
    print(f"  same-baseline overlap flags: {len(sflags)}")
    for f in sflags[:40]:
        print("   FLAG", f)

    print("== 4. P6 table-label coverage (later rects, getmetrics-anchored ink) ==")
    p6 = os.path.join(svgdir, "p6-gipi.svg")
    s = open(p6, encoding="utf-8").read()
    els = []
    for m in re.finditer(r'<(rect|text)([^>]*?)(/>|>(.*?)</text>)', s):
        kind, attr_s, content = m.group(1), m.group(2), m.group(4)
        a = _attrs(attr_s)
        if kind == "rect":
            if a.get("fill") not in (None, "none") and all(k in a for k in ("x", "y", "width", "height")):
                els.append(("rect", float(a["x"]), float(a["y"]),
                            float(a["width"]), float(a["height"])))
        else:
            if all(k in a for k in ("x", "y", "font-size")):
                t = html.unescape(re.sub(r"<[^>]+>", "", content or ""))
                els.append(("text", float(a["x"]), float(a["y"]),
                            float(a["font-size"]), a.get("font-family", ""),
                            a.get("font-weight") == "700", t))
    worst_cov = 0.0
    nlab = 0
    for i, el in enumerate(els):
        if el[0] != "text":
            continue
        _, x, y, size, fam, bold, t = el
        if not (1240 <= y <= 1470 and 65 <= x <= 1453):
            continue
        ib = OA.ink_box(t, fam, size, bold, x, y, "start")
        if ib is None:
            continue
        nlab += 1
        l, tp, r, b = ib
        area = max(0.0, (r - l) * (b - tp))
        cov = 0.0
        for el2 in els[i + 1:]:
            if el2[0] != "rect":
                continue
            _, rx, ry, rw, rh = el2
            ox = max(0.0, min(r, rx + rw) - max(l, rx))
            oy = max(0.0, min(b, ry + rh) - max(tp, ry))
            if area:
                cov = max(cov, ox * oy / area)
        worst_cov = max(worst_cov, cov)
        print(f"  label y={y} cov={cov * 100:.1f}% {t[:40]!r}")
    print(f"  P6 labels: {nlab}, worst coverage {worst_cov * 100:.1f}% (gate <30%)")

    print("== 5. Rendered-line window scan (dy in 10..45) ==")
    wflags = []
    for fn in sorted(os.listdir(svgdir)):
        texts = [t for t in parse_texts(os.path.join(svgdir, fn)) if t["text"].strip()]
        # group by column band (x // 460) then sort by y
        cols = {}
        for t in texts:
            cols.setdefault(int(t["x"] // 460), []).append(t)
        for col, ts in cols.items():
            ts.sort(key=lambda t: t["y"])
            for a, b in zip(ts, ts[1:]):
                dy = b["y"] - a["y"]
                if 10 <= dy <= 45 and b["text"] and b["text"][0] in NO_START and HANGUL.search(b["text"]):
                    wflags.append((fn, col, round(a["y"], 1), round(b["y"], 1), b["text"][:30]))
    print(f"  window line-start flags: {len(wflags)}")
    for f in wflags:
        print("   FLAG", f)

    print("== 6. P8 keys flow end + P7 teaser end ==")
    p8texts = parse_texts(os.path.join(svgdir, "p8-siheom.svg"))
    keys = [t for t in p8texts if 1328 < t["y"] < 2540]
    kb = []
    for t in keys:
        ib = OA.ink_box(t["text"], t["family"], t["size"], t["bold"], t["x"], t["y"], t["anchor"])
        if ib:
            kb.append((t["y"], ib[3], t["text"][:30]))
    kb.sort()
    print(f"  P8 keys lines: {len(keys)}; max baseline {kb[-1][0]:.2f}, ink bottom {kb[-1][1]:.2f} (gate <2540)")
    print(f"  last keys lines: {kb[-3:]}")
    p7s = open(os.path.join(svgdir, "p7-mal.svg"), encoding="utf-8").read()
    darks = []
    for m in RECT_RE.finditer(p7s):
        a = _attrs(m.group(1))
        if a.get("fill") == "#2c2822" and "height" in a:
            darks.append((a["x"], a["y"], a["width"], a["height"]))
    print(f"  P7 dark rects (teaser band): {darks} -> teaser end {[float(y) + float(h) for _, y, _, h in darks]}")

    print("== 7. Gloss counts (split rendered gloss()/glossline() strings on ·) ==")
    import glob as _glob
    build = os.path.dirname(os.path.abspath(__file__))
    for label, bdir in (("edition", build), ("core", None)):
        pass
    print("  (see gloss_compare.py output for core-vs-edition counts)")

    print("== 8. Phrase occurrence counts (whole issue, spaceless) ==")
    phrases = [
        ("11월 7일은 입동이에요", "1면"),
        ("절정에 가까운 주말이라고만 말할 수 있어요", "1면"),
        ("김장은 겨울 내내 먹는 김치를 담그는 일이에요", "1면"),
        ("수능까지 17일 남았어요. 오늘이 D-17예요", "2면"),
        ("낮은 길은 더 늦게 물들어요", "3면"),
        ("KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요", "4면"),
        ("온 나라가 수험생을 응원해요", "5면"),
        ("날짜를 먼저 보세요", "6면"),
    ]
    for label, d in (("edition", svgdir), ("core", coredir)):
        alltxt = ""
        per_page = {}
        for fn in sorted(os.listdir(d)):
            tt = "".join(t["text"] for t in parse_texts(os.path.join(d, fn)))
            per_page[fn] = tt.replace(" ", "").replace("\n", "")
            alltxt += per_page[fn]
        counts = []
        for ph, pg in phrases:
            key = ph.replace(" ", "")
            counts.append(alltxt.count(key))
        print(f"  {label}: phrase counts {counts} (expected core 5/2/4/2/2/2/2/2)")
        for (ph, pg), c in zip(phrases, counts):
            # tagged page check: phrase must occur on its tagged page
            pagemap = {"1면": "p1-pyoji.svg", "2면": "p2-saenghwal.svg", "3면": "p3-munhwa.svg",
                       "4면": "p4-seupocheu.svg", "5면": "p5-cheongnyeon.svg", "6면": "p6-gipi.svg"}
            onpage = per_page[pagemap[pg]].count(ph.replace(" ", ""))
            print(f"    phrase {pg}: whole-issue {c}, tagged-page {onpage}")

    print("== 9. Image payloads ==")
    import base64
    import hashlib
    for label, d in (("edition", svgdir), ("core", coredir)):
        tot = []
        for fn in sorted(os.listdir(d)):
            s = open(os.path.join(d, fn), encoding="utf-8").read()
            uris = re.findall(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', s)
            hs = []
            for u in uris:
                raw = base64.b64decode(u)
                hs.append((hashlib.sha256(u.encode()).hexdigest()[:12],
                           hashlib.sha256(raw).hexdigest()[:12]))
            tot.append(len(uris))
            print(f"  {label} {fn}: {len(uris)} images {hs}")
        print(f"  {label} per-page counts: {tot}")

    print("== 10. Wrap-log orphan scan ==")
    seen = set()
    start_flags, split_flags, lone = [], [], []
    for line in open(wraplog, encoding="utf-8"):
        rec = json.loads(line)
        key = (rec["text"], rec["size"], rec["max_w"])
        if key in seen:
            continue
        seen.add(key)
        for ln in rec["post"]:
            if ln and ln[0] in NO_START and HANGUL.search(ln):
                start_flags.append((rec["text"][:30], ln))
        src = rec["text"]
        pos = 0
        pre = rec["pre"]
        for j, ln in enumerate(pre):
            seg = ln.rstrip()
            if src[pos:pos + len(seg)] == seg:
                pos += len(seg)
            elif src[pos:pos + 1] == " " and src[pos + 1:pos + 1 + len(seg)] == seg:
                pos += 1 + len(seg)
            else:
                break
            if j + 1 < len(pre):
                if pos < len(src) and src[pos] == " ":
                    pos += 1
                elif pos < len(src):
                    tail = []
                    k = pos
                    while k < len(src) and src[k] != " ":
                        tail.append(src[k])
                        k += 1
                    nsyl = len(HANGUL.findall("".join(tail)))
                    if nsyl >= 3:
                        split_flags.append((nsyl, "".join(tail)[:20], src[max(0, pos - 8):pos + 12]))
        if len(pre) > 1:
            last = pre[-1].strip()
            if len(last) <= 3 and HANGUL.search(last):
                lone.append((src[:40], last))
    print(f"  unique wrap records: {len(seen)}")
    print(f"  post-kinsoku line-start NO_START flags: {len(start_flags)}")
    for f in start_flags[:20]:
        print("   START", f)
    print(f"  mid-word splits tail>=3 syllables: {len(split_flags)}")
    for f in split_flags[:20]:
        print("   SPLIT>=3", f)
    print(f"  lone final-line fragments (<=3 chars, adjudicate): {len(lone)}")
    for f in lone[:40]:
        print("   LONE", f)

    print("== 11. Below-box spill candidates (baseline within 45px under a stroked rect bottom, x inside rect) ==")
    spills = []
    for fn in sorted(os.listdir(svgdir)):
        path = os.path.join(svgdir, fn)
        rects = parse_rects(path)
        for t in parse_texts(path):
            if not t["text"].strip() or t["y"] >= 2580:
                continue
            for (rx, ry, rw, rh) in rects:
                if rx <= t["x"] <= rx + rw and ry + rh < t["y"] <= ry + rh + 45:
                    spills.append((fn, round(ry + rh, 1), round(t["y"], 1), t["text"][:50]))
                    break
    print(f"  spill candidates: {len(spills)}")
    for f in spills:
        print("   SPILL?", f)


if __name__ == "__main__":
    main()
