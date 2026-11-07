# -*- coding: utf-8 -*-
"""KO x JA (W45) builder checks — part 1: freeze adjudication, gloss,
P7 phrases, P8/P7 geometry, images. Run from this build dir with the
tools venv python. Reads only the delivery + core dirs."""
import base64
import glob
import hashlib
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import _font

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ko-core/svg")
ED = os.path.join(GOAL, "files/weekly-report-w45-ko-ja/svg")
TEXT_RE = re.compile(r"<text([^>]*)>(.*?)</text>", re.S)
HANGUL = re.compile(r"[\uac00-\ud7af]")


def load_texts(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for attrs, c in TEXT_RE.findall(s):
        m = dict(re.findall(r'(\S+?)="([^"]*)"', attrs))
        out.append((m, html.unescape(re.sub(r"<[^>]+>", "", c))))
    return out


def page_texts(d, n):
    f = sorted(glob.glob(os.path.join(d, "*.svg")))[n - 1]
    return load_texts(f)


def hangul_count(texts):
    return sum(len(HANGUL.findall(t)) for _, t in texts)


print("=== 1. Hangul char-level delta (core -> edition) ===")
# expected: P1 -(badge 25 + footer 4) = -29; P2-P7 -4 each; P8 -(footer 4 + separators 16) = -20
expected = {1: -29, 2: -4, 3: -4, 4: -4, 5: -4, 6: -4, 7: -4, 8: -20}
for n in range(1, 9):
    c = hangul_count(page_texts(CORE, n))
    e = hangul_count(page_texts(ED, n))
    print(f"  p{n}: core {c} edition {e} delta {e - c} expected {expected[n]} {'OK' if e - c == expected[n] else 'MISMATCH'}")

print("=== 2. Freeze diff string adjudication ===")
fd = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "freeze-diff.json"), encoding="utf-8"))
# freeze-diff.json structure: inspect keys
print("  freeze-diff top keys:", list(fd.keys())[:10])

print("=== 2b. Added-string Hangul runs must all occur in core text ===")
core_all = ""
for n in range(1, 9):
    core_all += "".join(t for _, t in page_texts(CORE, n))
bad = []
for pg, data in fd["pages"].items():
    for item in data["added_strings"]:
        for run in HANGUL.findall(item["text"]):
            pass
        runs = re.findall(r"[\uac00-\ud7af]+", item["text"])
        for r in runs:
            if r not in core_all:
                bad.append((pg, item["text"], r))
print(f"  added strings with Hangul runs absent from core: {len(bad)}")
for b in bad[:20]:
    print("   ", b)
print("=== 2c. Removed strings containing Hangul (must be furniture only) ===")
for pg, data in fd["pages"].items():
    for item in data["removed_strings"]:
        if HANGUL.search(item["text"]):
            print(f"  p{pg} REMOVED-HANGUL :: {item['text']}")

print("=== 3. Gloss counts: call-string vs render-page ===")
import ast as _ast
# call-string: gloss() call args in build sources, split on '·'
def gloss_call_items(src_dir):
    items = {}
    pages = {"content12.py": [1, 2], "content34.py": [3, 4], "content56.py": [5, 6]}
    total = 0
    for fn, _pgs in pages.items():
        src = open(os.path.join(src_dir, fn), encoding="utf-8").read()
        calls = re.findall(r"\.gloss\(\"([^\"]+)\"\)", src)
        n = 0
        for c in calls:
            n += len(c.split("·"))
        items[fn] = (len(calls), n)
        total += n
    return items, total
for label, d in [("CORE", os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-build")),
                 ("JA", os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-ja-build"))]:
    items, total = gloss_call_items(d)
    print(f"  {label} call-string: {items} total items {total}")
print("  render-page prefix counts (core 译注｜ vs JA 解説 — ):")
for n in range(1, 9):
    ct = "".join(t for _, t in page_texts(CORE, n)).count("译注｜")
    et = "".join(t for _, t in page_texts(ED, n)).count("解説 — ")
    print(f"    p{n}: core {ct} ja {et} {'OK' if ct == et else 'MISMATCH'}")
print("  P7 glosslines (A2/B1/B2, items split on ·):")
for label, d in [("CORE", os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-build")),
                 ("JA", os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-ja-build"))]:
    src = open(os.path.join(d, "content7.py"), encoding="utf-8").read()
    gl = re.findall(r"\.glossline\(\"([^\"]+)\"\)", src)
    print(f"    {label}: {gl} -> items {[len(g.split('·')) for g in gl]}")

print("=== 4. P7 phrases: verbatim on tagged page + whole-issue frequencies ===")
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
def norm(s):
    return re.sub(r"\s+", "", s)
for label, d in [("CORE", CORE), ("JA", ED)]:
    alltext = {}
    for n in range(1, 9):
        alltext[n] = norm("".join(t for _, t in page_texts(d, n)))
    whole = "".join(alltext.values())
    print(f"  {label}:")
    for ph, tag in phrases:
        pg = int(tag[0])
        onpage = norm(ph) in alltext[pg]
        freq = whole.count(norm(ph))
        print(f"    tag {tag} onpage={onpage} freq={freq} :: {ph}")

print("=== 5. P8 flow-end three calibers + P7 letter/teaser geometry ===")
# (a) flow cursor from round-3 build log
import subprocess as _sp
log = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "round3-build.log"), encoding="utf-8").read()
for line in log.splitlines():
    if "P8-keys" in line or "P7 col3" in line or "teaser ends" in line:
        print("  log:", line)
# (b) last baseline + (c) ink bottom on P8 keys (last text node before footer)
p8 = page_texts(ED, 8)
key_nodes = [(m, t) for m, t in p8 if float(m.get("y", 0)) > 1328 and float(m.get("y", 0)) < 2580]
last = key_nodes[-1]
print(f"  last P8 key node: y={last[0].get('y')} size={last[0].get('font-size')} :: {last[1][:60]}")
fnt = _font("serif", False, float(last[0].get("font-size", 13.3)))
bb = fnt.getbbox(last[1])
print(f"  ink bottom caliber: baseline {last[0].get('y')} + bbox ymax {bb[3]} = {float(last[0].get('y')) + bb[3]:.2f} (limit 2540)")
# P7 letter box + phrases rule
p7svg = open(os.path.join(ED, "p7-mal.svg"), encoding="utf-8").read()
rects = re.findall(r'<rect x="1451" y="([\d.]+)" width="434" height="([\d.]+)"', p7svg)
print(f"  P7 col3 rects (y,h,bottom): {[(r[0], r[1], round(float(r[0]) + float(r[1]), 2)) for r in rects]}")
rules = re.findall(r'<line x1="65" x2="1885" y1="([\d.]+)" y2="[\d.]+" stroke="#b3a06a" stroke-width="2"', p7svg)
print(f"  P7 phrases gold rules: {rules}")
p7 = page_texts(ED, 7)
letter_lines = [(m, t) for m, t in p7 if float(m.get("x", 0)) >= 1473 and 1256 < float(m.get("y", 0)) < 1900]
last_letter = letter_lines[-1]
fnt2 = _font("sans", False, float(last_letter[0].get("font-size", 20)))
bb2 = fnt2.getbbox(last_letter[1])
print(f"  last letter line: y={last_letter[0].get('y')} :: {last_letter[1]} ink bottom={float(last_letter[0].get('y')) + bb2[3]:.2f} box bottom={float(rects[-1][0]) + float(rects[-1][1]):.2f} rule={rules[0] if rules else '?'}")

print("=== 6. Images: payload hashes + credits + placement ===")
for n in range(1, 9):
    for label, d in [("CORE", CORE), ("JA", ED)]:
        svg = open(sorted(glob.glob(os.path.join(d, "*.svg")))[n - 1], encoding="utf-8").read()
        imgs = re.findall(r'href="(data:image/[^;]+;base64,([^"]+))"', svg)
        hs = [(hashlib.sha256(b64.encode()).hexdigest()[:12],
               hashlib.sha256(base64.b64decode(b64)).hexdigest()[:12]) for _, b64 in imgs]
        if label == "CORE":
            core_hs = hs
        else:
            print(f"  p{n}: core {core_hs} ja {hs} {'OK' if core_hs == hs else 'MISMATCH'}")
    for label, d in [("JA", ED)]:
        texts = page_texts(d, n)
        for _, t in texts:
            if t.startswith("사진:") or t.startswith("그림:"):
                print(f"    p{n} credit :: {t}")

print("=== 3b. Gloss-box prefix, counted by node start (badge excluded) ===")
for n in range(1, 9):
    ct = sum(1 for _, t in page_texts(CORE, n) if t.startswith("译注｜"))
    et = sum(1 for _, t in page_texts(ED, n) if t.startswith("解説 — "))
    print(f"    p{n}: core {ct} ja {et} {'OK' if ct == et else 'MISMATCH'}")

print("=== 5b. Ink bottoms via canonical occlusion_audit.ink_box ===")
import importlib.util as _ilu
spec = _ilu.spec_from_file_location("occ", os.path.join(GOAL, "tools/occlusion_audit.py"))
occ = _ilu.module_from_spec(spec)
spec.loader.exec_module(occ)
# last P8 key node
p8n = [(m, t) for m, t in page_texts(ED, 8) if float(m.get("y", 0)) > 1328 and float(m.get("y", 0)) < 2580][-1]
fam = p8n[0].get("font-family", "Noto Serif CJK KR")
ib = occ.ink_box(p8n[1], fam, float(p8n[0].get("font-size", 13.3)), False, float(p8n[0].get("x", 0)), float(p8n[0].get("y", 0)), p8n[0].get("text-anchor", "start"))
print(f"  P8 last key ink box: {tuple(round(v, 2) for v in ib)} bottom={ib[3]:.2f} (limit 2540)")
p7n = [(m, t) for m, t in page_texts(ED, 7) if float(m.get("x", 0)) >= 1473 and 1256 < float(m.get("y", 0)) < 1900][-1]
fam7 = p7n[0].get("font-family", "Noto Sans CJK KR")
ib7 = occ.ink_box(p7n[1], fam7, float(p7n[0].get("font-size", 20)), False, float(p7n[0].get("x", 0)), float(p7n[0].get("y", 0)), p7n[0].get("text-anchor", "start"))
print(f"  P7 last letter ink box: {tuple(round(v, 2) for v in ib7)} bottom={ib7[3]:.2f} box bottom=1863.46 rule=1893.46 gap_to_rule={1893.46 - ib7[3]:.2f}")
print(f"  P7 teaser rect bottom=2517.46 (limit 2540) margin={2540 - 2517.46:.2f}")

print("=== 7. Right-edge ADVANCE scan (all pages, edition) ===")
NO_START_KO = set("。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;\"")
for n in range(1, 9):
    flags = []
    for m, t in page_texts(ED, n):
        if not t.strip():
            continue
        size = float(m.get("font-size", 20))
        bold = m.get("font-weight") == "700"
        kind = "serif" if "Serif" in m.get("font-family", "") else "sans"
        fnt = _font(kind, bold, size)
        adv = fnt.getlength(t)
        x = float(m.get("x", 0))
        anchor = m.get("text-anchor", "start")
        if anchor == "middle":
            right = x + adv / 2
        elif anchor == "end":
            right = x
        else:
            right = x + adv
        if right > 1898:
            flags.append((round(right, 1), t[:50]))
    print(f"  p{n}: advance past band-right 1898: {len(flags)} {flags[:5]}")

print("=== 8. Same-baseline ink spacing scan (edition) ===")
for n in range(1, 9):
    groups = {}
    for m, t in page_texts(ED, n):
        if not t.strip():
            continue
        groups.setdefault(float(m.get("y", 0)), []).append((m, t))
    overlaps = []
    tight = 0
    for y, nodes in groups.items():
        if len(nodes) < 2:
            continue
        boxes = []
        for m, t in nodes:
            size = float(m.get("font-size", 20))
            bold = m.get("font-weight") == "700"
            famx = m.get("font-family", "Noto Serif CJK KR")
            ibx = occ.ink_box(t, famx, size, bold, float(m.get("x", 0)), y, m.get("text-anchor", "start"))
            boxes.append((ibx[0], ibx[2], t))
        boxes.sort()
        for (l1, r1, t1), (l2, r2, t2) in zip(boxes, boxes[1:]):
            gap = l2 - r1
            if gap < 0:
                overlaps.append((y, round(gap, 1), t1[:30], t2[:30]))
            elif gap < 6:
                tight += 1
    print(f"  p{n}: same-baseline overlaps={len(overlaps)} tight(<6)={tight} {overlaps[:4]}")

print("=== 9. P6 chart-label ink vs later-rect coverage (max) ===")
import xml.etree.ElementTree as _ET
svg6 = open(os.path.join(ED, "p6-gipi.svg"), encoding="utf-8").read()
# paint order: iterate all elements in document order
tokens = re.findall(r"<(rect|text|image)[^>]*?(/?)>", svg6)
# simpler: walk raw elements in order with positions
elems = []
for mm in re.finditer(r"<(rect|text|image)\b([^>]*)>([^<]*)</(?:rect|text|image)>|<rect\b([^>]*)/>|<image\b([^>]*)/>", svg6):
    pass
# fallback: use regex over tags in order
order = []
for mm in re.finditer(r"<(rect|text|image)\b([^>]*?)(?:>([^<]*)</\1>|/>)", svg6):
    tag, attrs, body = mm.group(1), mm.group(2), mm.group(3) or ""
    am = dict(re.findall(r'(\S+?)="([^"]*)"', attrs))
    order.append((tag, am, html.unescape(body)))
maxcov = 0.0
maxinfo = None
for i, (tag, am, body) in enumerate(order):
    if tag != "text" or not body.strip():
        continue
    size = float(am.get("font-size", 20))
    bold = am.get("font-weight") == "700"
    famx = am.get("font-family", "Noto Serif CJK KR")
    ibx = occ.ink_box(body, famx, size, bold, float(am.get("x", 0)), float(am.get("y", 0)), am.get("text-anchor", "start"))
    iarea = max(0.0, ibx[2] - ibx[0]) * max(0.0, ibx[3] - ibx[1])
    if iarea <= 0:
        continue
    for tag2, am2, _ in order[i + 1:]:
        if tag2 != "rect":
            continue
        fill = am2.get("fill", "none")
        if fill in ("none", "transparent"):
            continue
        rx, ry = float(am2.get("x", 0)), float(am2.get("y", 0))
        rw, rh = float(am2.get("width", 0)), float(am2.get("height", 0))
        ox = max(0.0, min(ibx[2], rx + rw) - max(ibx[0], rx))
        oy = max(0.0, min(ibx[3], ry + rh) - max(ibx[1], ry))
        cov = (ox * oy) / iarea if iarea else 0
        if cov > maxcov:
            maxcov = cov
            maxinfo = (body[:40], round(ibx[1], 1), round(cov, 3))
print(f"  P6 max ink-vs-later-rect coverage: {maxcov:.3f} {maxinfo} (gate <0.30)")

print("=== 10. Rendered-line window scan 10-45px + JA line-start scan ===")
COLBANDS = [(65, 499), (527, 961), (989, 1423), (1451, 1885)]
SMALL_KANA = set("ぁぃぅぇぉゃゅょっァィゥェォャュョッ")
JA_CLOSERS = set("、。！？：；）」』】ー…‥・")
for n in range(1, 9):
    nodes = [(m, t) for m, t in page_texts(ED, n) if t.strip()]
    # window scan per column band (by node start x)
    pairs = 0
    flags = []
    for ci, (lo, hi) in enumerate(COLBANDS):
        col = sorted([(float(m["y"]), t) for m, t in nodes if lo <= float(m.get("x", 0)) <= hi])
        for (y1, t1), (y2, t2) in zip(col, col[1:]):
            dy = y2 - y1
            if 10 <= dy <= 45:
                pairs += 1
                if t2[0] in NO_START_KO or t2[0] in SMALL_KANA:
                    flags.append((ci, round(y2, 1), t2[:30]))
                if t1 and t1[-1] in set("「『（【〈《([{"):
                    flags.append((ci, round(y1, 1), "END-OPENER " + t1[-20:]))
    # JA line-start scan over ALL lines (any x): closers + small kana
    ja_flags = [(m.get("x"), m.get("y"), t[:30]) for m, t in nodes
                if t[0] in JA_CLOSERS or t[0] in SMALL_KANA]
    print(f"  p{n}: window pairs={pairs} window flags={len(flags)} {flags[:5]} | JA line-start flags={len(ja_flags)} {ja_flags[:5]}")

print("=== 11. KO wrap-spy orphan scan (10-45 window definition: rendered pairs above; ===")
print("    wrap-call junction scan below: line-start NO_START / line-end NO_END /")
print("    mid-word splits with >=3-syllable tails, parenthesised fragments included) ===")
import json as _json
HANG = re.compile(r"[\uac00-\ud7af]")
NO_END = set("「『（【〈《([{\"")
n_calls = 0
ls_flags = []
le_flags = []
mw_flags = []
mw_info = 0
for line in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "orphan-wrap.log"), encoding="utf-8"):
    rec = _json.loads(line)
    n_calls += 1
    pre = rec["pre"]
    post = rec["post"]
    orig = rec["text"]
    # map nospace positions -> whether next original char is a space
    # build: walk original; nospace_idx counts non-space chars
    next_is_space = {}
    cnt = 0
    chars = list(orig)
    for j, ch in enumerate(chars):
        if ch == " ":
            continue
        nxt = chars[j + 1] if j + 1 < len(chars) else ""
        next_is_space[cnt] = (nxt == " ")
        cnt += 1
    # junction positions in nospace coordinates from PRE lines
    # (kinsoku moves punctuation only, so Hangul junctions are identical;
    # line-start/end checks use POST lines, the actually rendered form)
    pos = 0
    for li in range(len(post) - 1):
        pa, pb = post[li], post[li + 1]
        if pb and pb[0] in NO_START_KO:
            ls_flags.append((pa[-20:], pb[:20]))
        if pa and pa[-1] in NO_END:
            le_flags.append((pa[-20:], pb[:20]))
    pos = 0
    for li in range(len(pre) - 1):
        a, b = pre[li], pre[li + 1]
        pos += len(re.sub(r"\s+", "", a))
        # mid-word: leading Hangul run of next line
        tail = ""
        if b:
            k = 0
            while k < len(b) and HANG.match(b[k]):
                tail += b[k]
                k += 1
        head = ""
        if a:
            k = len(a) - 1
            while k >= 0 and HANG.match(a[k]):
                head = a[k] + head
                k -= 1
        if head and tail:
            is_space = next_is_space.get(pos - 1, None) if False else None
            # junction nospace index = pos (chars before junction); the char
            # before junction is nospace index pos-1; space-after flag for it:
            sp = next_is_space.get(pos - 1)
            if sp is False:
                if len(tail) >= 3:
                    mw_flags.append((a[-20:], b[:20], len(tail)))
                else:
                    mw_info += 1
print(f"  wrap calls: {n_calls}")
print(f"  line-start NO_START: {len(ls_flags)} {ls_flags[:5]}")
print(f"  line-end NO_END: {len(le_flags)} {le_flags[:5]}")
print(f"  mid-word splits >=3-syllable tails: {len(mw_flags)} {mw_flags[:8]}")
print(f"  mid-word splits 1-2-syllable tails (info): {mw_info}")

print("=== 12. REPL-source absence + Han token inventory (word-level) ===")
import ast as _ast
tsrc = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "transform.py"), encoding="utf-8").read()
tree = _ast.parse(tsrc)
repl = {}
for node in _ast.walk(tree):
    if isinstance(node, _ast.Assign) and getattr(node.targets[0], "id", "") == "REPL":
        repl = _ast.literal_eval(node.value)
        break
ed_all = ""
for n in range(1, 9):
    ed_all += "".join(t for _, t in page_texts(ED, n))
keeps = ["立冬", "生活", "文化", "体育", "青年"]
present = []
for src in repl:
    if src in ed_all and src not in keeps and all(k not in src for k in keeps):
        present.append(src)
print(f"  REPL sources still present in edition SVGs (excluding KEEP words): {len(present)}")
for p in present[:20]:
    print("   ", p)
# Han tokens inventory
toks = {}
for t in re.findall(r"[\u4e00-\u9fff]+", ed_all):
    toks[t] = toks.get(t, 0) + 1
print(f"  distinct Han-only tokens in edition: {len(toks)}")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "han-tokens.txt"), "w", encoding="utf-8") as fh:
    for t, c in sorted(toks.items(), key=lambda kv: -kv[1]):
        fh.write(f"{c}\t{t}\n")
print("  inventory written to han-tokens.txt")
