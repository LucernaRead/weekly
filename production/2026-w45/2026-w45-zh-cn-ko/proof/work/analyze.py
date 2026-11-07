# -*- coding: utf-8 -*-
"""Independent proof analysis for W45 zh-cn x ko. Read-only on delivery/core/W43."""
import base64, glob, hashlib, html, os, re, sys
from collections import Counter

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-ko")
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core")
W43 = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-ko")
OUT = sys.stdout

def texts(path):
    src = open(path, encoding="utf-8").read()
    nodes = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>(.*?)</text>', src, flags=re.S):
        raw = re.sub(r"<[^>]+>", "", m.group(4))
        t = html.unescape(raw)
        attrs = m.group(3)
        sz = re.search(r'font-size="([\d.]+)"', attrs)
        wt = "700" if 'font-weight="700"' in attrs else "400"
        fill = re.search(r'fill="([^"]+)"', attrs)
        anch = re.search(r'text-anchor="([^"]+)"', attrs)
        nodes.append(dict(x=float(m.group(1)), y=float(m.group(2)), size=float(sz.group(1)) if sz else None,
                          weight=wt, fill=fill.group(1) if fill else None,
                          anchor=anch.group(1) if anch else "start", text=t))
    return src, nodes

def tspan_check(path):
    src = open(path, encoding="utf-8").read()
    return src.count("<tspan"), src.count("<text ")

HAN = re.compile(r"[\u4e00-\u9fff]")
HANG = re.compile(r"[\uac00-\ud7a3]")
LAT = re.compile(r"[A-Za-z]")

pages = ["p1-touiban", "p2-shenghuo", "p3-wenhua", "p4-tiyu", "p5-qingnian", "p6-shendu", "p7-ciyu", "p8-ceyan"]
print("=== tspan/text counts (edition) ===")
for p in pages:
    print(p, tspan_check(os.path.join(ED, "svg", p + ".svg")))

print("\n=== 1. multiset diff + charwise ===")
core_all_hanzi = set()
for p in pages:
    _, cn = texts(os.path.join(CORE, "svg", p + ".svg"))
    for n in cn:
        core_all_hanzi |= set(HAN.findall(n["text"]))
for p in pages:
    _, en = texts(os.path.join(ED, "svg", p + ".svg"))
    _, cn = texts(os.path.join(CORE, "svg", p + ".svg"))
    ce, cc = Counter(n["text"] for n in en), Counter(n["text"] for n in cn)
    added = ce - cc; removed = cc - ce
    add_hang = sum(len(HANG.findall(s)) * k for s, k in added.items())
    add_hanzi = sum(len(HAN.findall(s)) * k for s, k in added.items())
    rem_hanzi = sum(len(HAN.findall(s)) * k for s, k in removed.items())
    novel = set()
    for s in added:
        novel |= (set(HAN.findall(s)) - core_all_hanzi)
    print(f"{p}: added_strings={sum(added.values())} removed_strings={sum(removed.values())} "
          f"Hangul_added={add_hang} Hanzi_added={add_hanzi} Hanzi_removed={rem_hanzi} novel_hanzi={sorted(novel)}")
    if p in ("p3-wenhua", "p8-ceyan"):
        print(f"  -- {p} added strings containing 候:")
        for s, k in sorted(added.items()):
            if "候" in s: print(f"     x{k} {s!r}")
        print(f"  -- {p} removed strings containing 候:")
        for s, k in sorted(removed.items()):
            if "候" in s: print(f"     x{k} {s!r}")
    # pure-Hanzi removed strings (no Latin, no Hangul) - must be page-line/footer segments only
    pure = [(s, k) for s, k in removed.items() if HAN.search(s) and not LAT.search(s) and not HANG.search(s)]
    if pure:
        print(f"  -- pure-Hanzi removed strings ({p}):")
        for s, k in pure: print(f"     x{k} {s!r}")

print("\n=== 1b. removed strings containing Hanzi but no Hangul, per page (furniture audit) ===")
for p in pages:
    _, en = texts(os.path.join(ED, "svg", p + ".svg"))
    _, cn = texts(os.path.join(CORE, "svg", p + ".svg"))
    ce, cc = Counter(n["text"] for n in en), Counter(n["text"] for n in cn)
    removed = cc - ce
    for s, k in sorted(removed.items()):
        if HAN.search(s) and not HANG.search(s):
            print(f"{p} x{k} {s!r}")

print("\n=== 2. residual Latin nodes (edition) ===")
for p in pages:
    _, en = texts(os.path.join(ED, "svg", p + ".svg"))
    for n in en:
        if LAT.search(n["text"]):
            print(f"{p} y={n['y']} :: {n['text']!r}")

print("\n=== 3. P1 badge / strapline / footer ===")
def show_badge(d, label):
    _, nodes = texts(os.path.join(d, "svg", "p1-touiban.svg"))
    for n in nodes:
        if "독자를 위한 판" in n["text"] or "English-speaking readers" in n["text"] or "독자를" in n["text"]:
            print(f"{label} badge :: x={n['x']} y={n['y']} size={n['size']} weight={n['weight']} fill={n['fill']} anchor={n['anchor']} :: {n['text']!r}")
    for n in nodes:
        if n["y"] == 372 or (370 <= n["y"] <= 374):
            print(f"{label} y~372 :: x={n['x']} y={n['y']} size={n['size']} :: {n['text']!r}")
show_badge(CORE, "CORE"); show_badge(W43, "W43ko"); show_badge(ED, "ED")
print("--- footers (all pages, edition) ---")
for p in pages:
    _, nodes = texts(os.path.join(ED, "svg", p + ".svg"))
    for n in nodes:
        if "주간지" in n["text"] or "제 " in n["text"] and "면" in n["text"]:
            print(f"{p} :: x={n['x']} y={n['y']} :: {n['text']!r}")
print("--- footers W43 ko p1/p8 ---")
for p in ["p1-touiban", "p8-ceyan"]:
    _, nodes = texts(os.path.join(W43, "svg", p + ".svg"))
    for n in nodes:
        if "주간지" in n["text"] or ("제 " in n["text"] and "면" in n["text"]):
            print(f"W43 {p} :: {n['text']!r}")

print("\n=== 4. P8 separators + answers head ===")
for d, label in [(ED, "ED"), (W43, "W43ko")]:
    _, nodes = texts(os.path.join(d, "svg", "p8-ceyan.svg"))
    seps = [n["text"] for n in nodes if re.match(r"^— .* —$", n["text"].strip())]
    print(f"{label} separators: {seps}")
    for n in nodes:
        if "모든 정답과 해설" in n["text"] or "해설은 모두" in n["text"] or "Answer keys" in n["text"] or "All notes" in n["text"]:
            print(f"{label} answers-head :: {n['text']!r}")
print("--- gloss prefix nodes (edition) ---")
for p in pages:
    _, nodes = texts(os.path.join(ED, "svg", p + ".svg"))
    for n in nodes:
        if n["text"].startswith("해설") or n["text"].startswith("Notes"):
            print(f"{p} :: {n['text'][:60]!r}")

print("\n=== 5. P7 geometry: rect multisets core vs edition ===")
def rects(path):
    src = open(path, encoding="utf-8").read()
    return Counter(re.findall(r'<rect [^>]*>', src))
for p in pages:
    rc = rects(os.path.join(CORE, "svg", p + ".svg"))
    re_ = rects(os.path.join(ED, "svg", p + ".svg"))
    if rc != re_:
        print(f"{p}: rect multiset DIFFERS: core-only={list((rc-re_).items())[:5]} ed-only={list((re_-rc).items())[:5]}")
    else:
        print(f"{p}: rect multiset identical")
print("--- P7 teaser/footer-line elements (edition vs core) ---")
for d, label in [(CORE, "CORE"), (ED, "ED")]:
    src, _ = texts(os.path.join(d, "svg", "p7-ciyu.svg"))
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>', src):
        y = float(m.group(2))
        if 2400 <= y <= 2600:
            print(f"{label} rect x={m.group(1)} y={y} w={m.group(3)} h={m.group(4)}")
    for m in re.finditer(r'<line [^>]*>', src):
        if 'y1="2580"' in m.group(0) or '2580' in m.group(0):
            print(f"{label} line :: {m.group(0)[:160]}")

print("\n=== 6. images payloads ===")
def payloads(path):
    s = open(path, encoding="utf-8").read()
    return [hashlib.md5(base64.b64decode(m.group(1))).hexdigest()
            for m in re.finditer(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', s)]
for p in pages:
    ep, cp = payloads(os.path.join(ED, "svg", p + ".svg")), payloads(os.path.join(CORE, "svg", p + ".svg"))
    print(f"{p}: ed={len(ep)} core={len(cp)} equal={ep == cp}")
print("--- credit nodes ---")
for d, label in [(CORE, "CORE"), (ED, "ED"), (W43, "W43ko")]:
    for p in pages:
        _, nodes = texts(os.path.join(d, "svg", p + ".svg"))
        for n in nodes:
            if "Photo:" in n["text"]:
                print(f"{label} {p} :: {n['text']!r}")

print("\n=== 7. golden sentences (P7) ===")
gold = ["不用等11月11日", "下单就能发货", "先看结算页，再付款", "水开始结冰", "三场都输了", "小局一场没赢", "故事够不够好", "别以后，就现在"]
for d, label in [(CORE, "CORE"), (ED, "ED")]:
    _, nodes = texts(os.path.join(d, "svg", "p7-ciyu.svg"))
    concat = "".join(n["text"] for n in nodes)
    print(f"{label} P7 counts:", {g: concat.count(g) for g in gold})
    tags = sorted(set(re.findall(r"\(p\. \d+\)", concat)))
    print(f"{label} P7 (p. N) tags present: {tags}")
    # sentence -> nearest tag: print node pairs in order
    seq = [(n["text"]) for n in nodes]
    for i, t in enumerate(seq):
        for g in gold:
            if g in t:
                ctx = " | ".join(seq[max(0, i-1):i+2])
                print(f"  {label} {g!r} ctx: {ctx[:180]!r}")
print("--- W43 ko P7 (p. N) form ---")
_, nodes = texts(os.path.join(W43, "svg", "p7-ciyu.svg"))
concat = "".join(n["text"] for n in nodes)
print("W43 tags:", sorted(set(re.findall(r"\(p\. \d+\)", concat))), "count:", len(re.findall(r"\(p\. \d+\)", concat)))

print("\n=== 8. readers corner P7 ===")
for d, label in [(CORE, "CORE"), (ED, "ED")]:
    _, nodes = texts(os.path.join(d, "svg", "p7-ciyu.svg"))
    for n in nodes:
        if "编辑部示例信" in n["text"] or "편집자 주" in n["text"] or "Editor's note" in n["text"]:
            print(f"{label} :: len={len(n['text'])} :: {n['text'][:240]!r}")
_, cn = texts(os.path.join(CORE, "svg", "p7-ciyu.svg"))
_, en = texts(os.path.join(ED, "svg", "p7-ciyu.svg"))
core_disc = [n["text"] for n in cn if "编辑部示例信" in n["text"]]
ed_disc = [n["text"] for n in en if "编辑部示例信" in n["text"]]
if core_disc and ed_disc:
    print("frozen Chinese prefix identical (first 106 chars):", core_disc[0][:106] == ed_disc[0][:106])
    print("core prefix:", repr(core_disc[0][:106]))
    print("ed prefix:  ", repr(ed_disc[0][:106]))
    print("full node identical except Korean tail:", ed_disc[0][:len(core_disc[0][:106])] == core_disc[0][:106])

print("\n=== 9. round-1 orphan fixes + 5 residual notes ===")
_, p4 = texts(os.path.join(ED, "svg", "p4-tiyu.svg"))
_, p6 = texts(os.path.join(ED, "svg", "p6-shendu.svg"))
print("P4 lone '것.' nodes:", [n for n in p4 if n["text"].strip() == "것."])
print("P6 lone '광고.' nodes:", [n for n in p6 if n["text"].strip() == "광고."])
for n in p4:
    if "역전승" in n["text"]: print("P4 역전승 ::", repr(n["text"]))
for n in p6:
    if "광고예요" in n["text"]: print("P6 광고예요 ::", repr(n["text"]))
checks = {
    "P3 bǔdōng note": ("p3-wenhua", "bǔdōng — 겨울을 앞두고 잘 먹기"),
    "P6 WeChat 35d": ("p6-shendu", "35일 동안"),
    "P8 WeChat 35d": ("p8-ceyan", "35일 동안"),
    "P8 TES/G2": ("p8-ceyan", "TES는 10월 26일에 G2를 이겼어요"),
    "P8 new film Nov7": ("p8-ceyan", "새 영화는 11월 7일에 개봉해요"),
    "P8 Huang Yan": ("p8-ceyan", "황옌은 화장터 직원이에요"),
    "P8 shùzì AI": ("p8-ceyan", "영화 속 인물은 디지털 이미지예요"),
}
eng = ["bǔdōng — eating well before winter", "runs 35 days", "TES beat G2", "new film opens on Nov 7", "crematory worker", "characters are digital images"]
for name, (pg, frag) in checks.items():
    _, nodes = texts(os.path.join(ED, "svg", pg + ".svg"))
    hits = [n["text"] for n in nodes if frag in n["text"]]
    print(f"{name}: Korean hits={len(hits)} :: {hits[:2]}")
for e in eng:
    found = []
    for p in pages:
        _, nodes = texts(os.path.join(ED, "svg", p + ".svg"))
        for n in nodes:
            if e in n["text"]: found.append((p, n["text"][:80]))
    print(f"English residual {e!r}: {found}")

print("\n=== 10. S2 candidate P8 key 94 context ===")
_, p8 = texts(os.path.join(ED, "svg", "p8-ceyan.svg"))
for i, n in enumerate(p8):
    if n["text"].startswith("94."):
        print(f"idx {i} :: x={n['x']} y={n['y']} :: {n['text']!r}")
        for j in range(max(0, i-2), min(len(p8), i+3)):
            print(f"   ctx[{j}] x={p8[j]['x']} y={p8[j]['y']} :: {p8[j]['text'][:80]!r}")

print("\n=== 11. 候 multiset counts ===")
for d, label in [(CORE, "CORE"), (ED, "ED")]:
    for p in ["p3-wenhua", "p8-ceyan"]:
        _, nodes = texts(os.path.join(d, "svg", p + ".svg"))
        tot = sum(n["text"].count("候") for n in nodes)
        print(f"{label} {p} 候 total={tot}")
print("--- P8 候 sites (edition) ---")
_, p8 = texts(os.path.join(ED, "svg", "p8-ceyan.svg"))
for n in p8:
    if "候" in n["text"]: print(f"  :: {n['text'][:120]!r}")
print("--- P3 候 sites (edition) ---")
_, p3 = texts(os.path.join(ED, "svg", "p3-wenhua.svg"))
for n in p3:
    if "候" in n["text"]: print(f"  :: {n['text'][:120]!r}")
