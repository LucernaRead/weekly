# -*- coding: utf-8 -*-
"""Proof round 2: registry, gloss, quotes, frame scan, chart, s2twp, vocab."""
import glob, json, os, re, sys
from collections import Counter
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
from PIL import ImageFont

B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = f"{B}/files/weekly-report-w45-nl-zh-tw/svg"
CO = f"{B}/files/weekly-report-w45-nl-core/svg"
PAGES = ["p1-voorpagina", "p2-leven", "p3-cultuur", "p4-sport", "p5-jongeren",
         "p6-verdieping", "p7-taal", "p8-toets"]
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")

def texts(path):
    s = open(path, encoding="utf-8").read()
    return [OA.clean_text(m.group("tcontent")) for m in OA.TAG_RE.finditer(s)
            if m.group("tattrs") is not None]

print("=== R1 registry diff ===")
rc = json.load(open(f"{B}/hidden_files/weekly-report-w45-nl-zh-tw-build/reg-core/reg.json"))
re_ = json.load(open(f"{B}/hidden_files/weekly-report-w45-nl-zh-tw-build/reg-ed/reg.json"))
print("len", len(rc), len(re_))
kd, td, nd = [], [], []
for a, b in zip(rc, re_):
    assert a["n"] == b["n"]
    if a["page"] != b["page"] or a["level"] != b["level"]: print("PAGE/LEVEL DIFF", a, b)
    if a["key"] != b["key"]: kd.append((a["n"], a["key"], b["key"]))
    if a["type"] != b["type"]: td.append((a["n"], a["type"], b["type"]))
    if a["note"] != b["note"]: nd.append(a["n"])
print("KEY diffs:", kd)
print("TYPE diffs count:", len(td), "mapping:", Counter((a, b) for _, a, b in td))
print("NOTE diffs count:", len(nd), "unchanged notes:", 150 - len(nd))
print("notes ending ）core:", [it["n"] for it in rc if it["note"].rstrip().endswith("）")])
print("notes ending ）ed:", [it["n"] for it in re_ if it["note"].rstrip().endswith("）")])
print("item 139/140 registry:", json.dumps(rc[138], ensure_ascii=False), json.dumps(re_[138], ensure_ascii=False))
print("item 139/140 registry:", json.dumps(rc[139], ensure_ascii=False), json.dumps(re_[139], ensure_ascii=False))
print("item 139/140: note core has 简体? ed has 繁体? (stem = question stem field?) keys:", rc[138].keys(), re_[138].keys())
# stems live in content files, not registry: check P8 exercise area lines for 139/140
for name, d in [("core", CO), ("ed", ED)]:
    for t in texts(f"{d}/p8-toets.svg"):
        if "Museumnacht duurt" in t or "Ik doe mee aan" in t or "博物馆之夜" in t or "博物館之夜" in t or "我参加" in t or "我參加" in t:
            print(f"  P8-ex {name}:", repr(t))

print("\n=== R2 gloss blocks (join lines from 譯注｜/译注｜ to section end) ===")
def gloss_block(ts):
    # find start line containing 譯注｜ or 译注｜, then join following lines until a line that is a header (all-caps section or OEFENINGEN) or ends with 。 and next line starts a new section
    out, cur = [], None
    for t in ts:
        if "譯注｜" in t or "译注｜" in t:
            cur = t.split("｜", 1)[1]; out.append(cur); continue
        if cur is not None:
            if t.startswith("OEFENINGEN") or t.startswith("EN JIJ") or t.startswith("DE ") or t.startswith("VOOR OF") or t.startswith("HET WOORD") or t.startswith("ZINNEN"):
                cur = None; continue
            # continuation lines of gloss: they contain · or end with 。 or are a single word fragment
            out.append(t)
            if t.rstrip().endswith("。"):
                cur = None
    return out
for p in ["p2-leven", "p3-cultuur", "p4-sport", "p5-jongeren", "p6-verdieping"]:
    ct, et = gloss_block(texts(f"{CO}/{p}.svg")), gloss_block(texts(f"{ED}/{p}.svg"))
    cj = "".join(ct); ej = "".join(et)
    # join rule: CJK-adjacent joins without space (renderer's wrap); count items by splitting on ·
    def items(j):
        parts = [x.strip() for x in j.split("·")]
        return [x for x in parts if x]
    print(f"{p}: core lines={ct} items={len(items(cj))} :: {items(cj)}")
    print(f"{p}: ed   lines={et} items={len(items(ej))} :: {items(ej)}")
    # Dutch headwords 1:1
    def heads(items):
        hs = []
        for it in items:
            m = re.match(r"([A-Za-z' ]+?)\s", it)
            hs.append(it.split()[0] if it.split() else it)
        return hs
    print(f"   core heads={[it.split()[0] for it in items(cj)]}")
    print(f"   ed   heads={[it.split()[0] for it in items(ej)]}")

print("\n=== R3 P7 quotes: labels + 2x + labelled-page presence ===")
def quotes(ts):
    out = []
    for i, t in enumerate(ts):
        if t.startswith("«") and t.endswith("»"):
            lab = None
            for j in range(i + 1, min(i + 3, len(ts))):
                m = re.search(r"\(Pagina (\d+)\)", ts[j])
                if m: lab = int(m.group(1)); break
            out.append((t, lab))
    return out
cq, eq = quotes(texts(f"{CO}/p7-taal.svg")), quotes(texts(f"{ED}/p7-taal.svg"))
cq = [(q, l) for q, l in cq if l is not None]; eq = [(q, l) for q, l in eq if l is not None]
print("core labels (金句 only):", [l for _, l in cq]); print("ed labels (金句 only):", [l for _, l in eq])
print("count:", len(cq), len(eq))
print("Dutch sentences identical:", [a == b for (a, _), (b, _) in zip(cq, eq)])
arts = {}
for p in ["p1-voorpagina", "p2-leven", "p3-cultuur", "p4-sport", "p5-jongeren", "p6-verdieping"]:
    arts[p] = " ".join(texts(f"{ED}/{p}.svg"))
p7joined = " ".join(texts(f"{ED}/p7-taal.svg"))
for (q, lab), (qc, lc) in zip(eq, cq):
    bare = q.strip("«»")
    # count occurrences: article pages joined + P7 (quote itself). Normalise whitespace.
    def cnt(hay, needle):
        return len(re.findall(re.escape(needle), re.sub(r"\s+", " ", hay)))
    art_total = sum(cnt(v, bare) for v in arts.values())
    labelled_page = ["p1-voorpagina", "p2-leven", "p3-cultuur", "p4-sport", "p5-jongeren", "p6-verdieping"][lab - 1]
    on_label = cnt(arts[labelled_page], bare)
    print(f"  lab={lab} on_labelled_page={on_label} article_total={art_total} P7={cnt(p7joined, bare)} :: {bare[:70]}")

print("\n=== R4 P7 phrases from articles (A2/B1/B2 phrase blocks) ===")
# P7 phrase lines: Dutch phrases in the three level columns; verify each Dutch token-phrase appears in P1-P6 article text
ed7 = texts(f"{ED}/p7-taal.svg")
for i, t in enumerate(ed7):
    print(f"  P7[{i}]: {t!r}") if i < 60 else None

print("\n=== R5 frame straddle scan (any rect vertical/horizontal border strictly inside ink) ===")
for p in PAGES:
    els, W, H = OA.parse_svg(open(f"{ED}/{p}.svg", encoding="utf-8").read())
    rects = [e for e in els if e.kind == "rect" and e.box]
    flags = []
    for e in els:
        if e.kind != "text" or not e.box: continue
        l, t, r, b = e.box
        for rc in rects:
            if rc.idx == e.idx: continue
            rl, rt, rr, rb = rc.box
            # vertical border inside ink x-range with y-overlap > 3
            for bx in (rl, rr):
                if l + 0.5 < bx < r - 0.5 and min(b, rb) - max(t, rt) > 3:
                    flags.append((e.text[:40], f"vborder x={bx:.1f} rect@{rc.idx} box={tuple(round(v,1) for v in rc.box)} ink={tuple(round(v,1) for v in e.box)}"))
            for by in (rt, rb):
                if t + 0.5 < by < b - 0.5 and min(r, rr) - max(l, rl) > 3:
                    flags.append((e.text[:40], f"hborder y={by:.1f} rect@{rc.idx} box={tuple(round(v,1) for v in rc.box)} ink={tuple(round(v,1) for v in e.box)}"))
        # page-frame proximity: ink right vs page width
        if r > W - 1 or l < 1:
            flags.append((e.text[:40], f"PAGE-EDGE ink r={r:.1f}"))
    print(f"{p}: straddle flags={len(flags)}")
    for f in flags[:20]: print("   ", f)

print("\n=== R6 rowcheck (same-baseline ink collisions) ===")
total = 0
for p in PAGES:
    els, W, H = OA.parse_svg(open(f"{ED}/{p}.svg", encoding="utf-8").read())
    txts = [e for e in els if e.kind == "text" and e.box]
    by = {}
    for e in txts: by.setdefault(round(e.baseline), []).append(e)
    for base, g in sorted(by.items()):
        g.sort(key=lambda e: e.box[0])
        for a, b in zip(g, g[1:]):
            if b.box[0] < a.box[2] - 0.01:
                print(f"  COLLISION {p} y={base}: {a.text[:40]!r} vs {b.text[:40]!r}"); total += 1
print("rowcheck total:", total)

print("\n=== R7 P6 chart coverage: correct baseline-anchored + true-ink ===")
els, W, H = OA.parse_svg(open(f"{ED}/p6-verdieping.svg", encoding="utf-8").read())
for method in ("baseline-anchored", "true-ink"):
    worst = 0.0; worst_desc = ""
    for i, e in enumerate(els):
        if e.kind != "text": continue
        x = OA.fnum(e.attrs, "x")
        if not (1451 <= x <= 1885 and 200 <= e.baseline <= 691): continue
        size = OA.fnum(e.attrs, "font-size", 20.0); bold = e.attrs.get("font-weight", "") in ("700", "bold")
        if method == "baseline-anchored":
            font = OA.get_font(e.attrs.get("font-family", ""), size, bold)
            asc, desc = font.getmetrics(); asc, desc = asc / OA.SCALE, desc / OA.SCALE
            w = font.getlength(e.text) / OA.SCALE
            anch = e.attrs.get("text-anchor", "start")
            x0 = x - w / 2 if anch == "middle" else x - w if anch == "end" else x
            box = (x0, e.baseline - asc, x0 + w, e.baseline + desc)
        else:
            box = e.box
        area = (box[2] - box[0]) * (box[3] - box[1])
        for later in els[i + 1:]:
            if later.kind != "rect" or not later.box: continue
            ix = max(0, min(box[2], later.box[2]) - max(box[0], later.box[0]))
            iy = max(0, min(box[3], later.box[3]) - max(box[1], later.box[1]))
            cov = ix * iy / area if area > 0 else 0
            if cov > worst: worst, worst_desc = cov, (e.text[:40], later.box)
    print(f"{method}: worst={worst*100:.2f}% desc={worst_desc}")

print("\n=== R8 fixup counts + 周/只/數據 ===")
full_ed = "\n".join("\n".join(texts(f"{ED}/{p}.svg")) for p in PAGES)
full_co = "\n".join("\n".join(texts(f"{CO}/{p}.svg")) for p in PAGES)
for w in ["週", "周", "只", "數據", "資料", "代碼", "程式碼", "比賽項目", "比賽專案", "專案", "報導", "報道", "市集", "集市", "把詞組成", "把片語成", "腳踏車", "搜尋", "搜索"]:
    print(f"  ed {w}: {full_ed.count(w)} | core {w}: {full_co.count(w)}")
print("周 contexts in ed:")
for p in PAGES:
    for t in texts(f"{ED}/{p}.svg"):
        if "周" in t: print(f"   {p}: {t!r}")
print("只 contexts in ed:")
for p in PAGES:
    for t in texts(f"{ED}/{p}.svg"):
        if "只" in t: print(f"   {p}: {t!r}")

print("\n=== R9 mainland vocab scan (expanded) ===")
vocab = ["搜索", "谷歌", "数据", "信息", "视频", "网络", "软件", "质量", "出租车", "上网", "网友", "博客",
         "服务器", "打印机", "鼠标", "电脑", "手机", "宽带", "光盘", "硬盘", "文件夹", "程序", "项目",
         "发 ", "让", "说", "国", "对", "车", "马", "门", "问", "电", "话", "语", "学", "头", "义", "云",
         "龙", "着", "钟", "种", "获", "达", "发", "乐", "节", "会", "东", "兰", "图", "书", "馆",
         "出租車", "網友", "視頻", "軟件", "質量", "信息", "数据"]
# single-char simplified scan must be contextual: report hits with context for a curated simplified-only list
simp_only = list("发让说国对车马门问电话语学头义云龙着钟种获达乐节会东兰图书馆发")
for ch in sorted(set(simp_only)):
    hits = []
    for p in PAGES:
        for t in texts(f"{ED}/{p}.svg"):
            if ch in t: hits.append(f"{p}:{t}")
    if hits: print(f"  SIMP-CAND {ch}: {hits[:4]}")
for w in ["搜索", "谷歌", "数据", "信息", "视频", "网络", "软件", "质量", "出租车", "上网", "网友", "博客", "服务器", "打印机", "鼠标", "电脑", "手机", "宽带", "光盘", "硬盘", "程序", "影片", "资讯"]:
    if w in full_ed: print(f"  VOCAB HIT {w}: count {full_ed.count(w)}")
print("  (no line above = zero hits for that list)")

print("\n=== R10 s2twp baseline diff: edition vs fresh s2twp(core strings) ===")
from opencc import OpenCC
cc = OpenCC("s2twp")
diffs = []
for p in PAGES:
    ct, et = texts(f"{CO}/{p}.svg"), texts(f"{ED}/{p}.svg")
    assert len(ct) == len(et), (p, len(ct), len(et))
    for a, b in zip(ct, et):
        conv = cc.convert(a)
        if conv != b:
            diffs.append((p, a, conv, b))
print(f"strings differing from pure s2twp: {len(diffs)}")
for p, a, conv, b in diffs:
    print(f"  {p} core={a!r}\n     s2twp={conv!r}\n     ed   ={b!r}")

print("\n=== R11 abstract / 桥接 / quotes / baseline sha ===")
ab = open(f"{B}/files/weekly-report-w45-nl-zh-tw/ABSTRACT.txt", encoding="utf-8").read()
print("ABSTRACT lines:", ab.count("\n"), "ascii-double-quote:", '"' in ab, "repr:", repr(ab))
print("ABSTRACT has 氣候週:", "氣候週" in ab, "has 學荷蘭語/讀荷蘭語新聞:", ("學荷蘭語" in ab or "讀荷蘭語" in ab))
for name, d in [("ed-svg", ED), ("core-svg", CO)]:
    joined = "\n".join("\n".join(texts(f"{d}/{p}.svg")) for p in PAGES)
    print(f"{name}: 桥接={joined.count('桥接')} bridge={joined.count('bridge')} ASCIIquote={joined.count(chr(34))}")
import subprocess
r = subprocess.run(["sha256sum", "-c", f"{B}/hidden_files/weekly-report-w45-nl-zh-tw-build/baseline-run1.sha256"],
                   cwd=f"{B}/files/weekly-report-w45-nl-zh-tw", capture_output=True, text=True)
print("baseline-run1 sha check stdout:", r.stdout.strip().replace("\n", " | "))
print("baseline-run1 sha check stderr:", r.stderr.strip(), "exit:", r.returncode)
print("card sizes:")
from PIL import Image
for p in PAGES:
    im = Image.open(f"{B}/files/weekly-report-w45-nl-zh-tw/cards/{p}.png")
    print(f"  {p}: {im.size} {im.mode}")
