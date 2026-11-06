# -*- coding: utf-8 -*-
"""Independent proofread checks for W45 PT x ZH-TW. Reads only; never imports
content modules, never writes outside the proof dir. PIL parts use TC faces."""
import re, os, sys, glob, json, hashlib, ast
from collections import Counter
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-pt-zh-tw/svg")
CO = os.path.join(BASE, "files/weekly-report-w45-pt-core/svg")
W43 = os.path.join(BASE, "files/weekly-report-pt-zh-tw/svg")
EB = os.path.join(BASE, "hidden_files/weekly-report-w45-pt-zh-tw-build")
CB = os.path.join(BASE, "hidden_files/weekly-report-w45-pt-build")
PROOF = os.path.join(BASE, "hidden_files/w45/pt-zh-tw-proof")
PAGES = ["p1-capa", "p2-vida", "p3-cultura", "p4-esporte", "p5-jovens",
         "p6-aprofundamento", "p7-lingua", "p8-avaliacao"]
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]+)"')

def texts_of(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for m in TEXT_RE.finditer(s):
        bold = 'font-weight="700"' in m.group(5)
        anchor = "middle" if 'text-anchor="middle"' in m.group(5) else ("end" if 'text-anchor="end"' in m.group(5) else "start")
        fm = re.search(r'fill="([^"]+)"', m.group(5))
        out.append({"x": float(m.group(1)), "y": float(m.group(2)), "fam": m.group(3),
                    "size": float(m.group(4)), "bold": bold, "anchor": anchor, "t": m.group(6),
                    "fill": fm.group(1) if fm else ""})
    return out, s

def all_texts(d):
    return {pg: texts_of(os.path.join(d, pg + ".svg")) for pg in PAGES}

EDT = all_texts(ED); COT = all_texts(CO); W43T = all_texts(W43)
ed_all = " ".join(t["t"] for pg in PAGES for t in EDT[pg][0])
co_all = " ".join(t["t"] for pg in PAGES for t in COT[pg][0])

print("=== A. forbidden term 桥接/橋接 ===")
for label, txt in [("edition SVGs", ed_all), ("core SVGs", co_all)]:
    print(f"  {label}: 桥接={txt.count(chr(0x6865)+chr(0x63a5))} 橋接={txt.count(chr(0x6a4b)+chr(0x63a5))}")
for fn in ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py",
           "content8.py", "render.py", "transform.py", "svglib.py", "gates.py", "run.py"]:
    p = os.path.join(EB, fn)
    if not os.path.exists(p):
        print(f"  {fn}: MISSING"); continue
    src = open(p, encoding='utf-8').read()
    hits = []
    for term in ["桥接", "橋接", "bridge"]:
        if term in src:
            for i, line in enumerate(src.splitlines(), 1):
                if term in line:
                    hits.append(f"L{i} [{term}] {line.strip()[:120]}")
    print(f"  {fn}: forbidden-term lines={len([h for h in hits if '桥接' in h or '橋接' in h])} bridge-lines={len([h for h in hits if 'bridge' in h])}")
    for h in hits[:6]:
        print(f"    {h}")

print("=== B. svglib illus_climb ===")
src = open(os.path.join(EB, "svglib.py"), encoding='utf-8').read()
for i, line in enumerate(src.splitlines(), 1):
    if "illus_climb" in line:
        print(f"  L{i}: {line.strip()[:200]}")
print(f"  'illus_climb' in edition SVG text nodes: {'illus_climb' in ed_all}")
print(f"  'illus_climb' in edition SVG raw (incl attrs/comments): {any('illus_climb' in EDT[pg][1] for pg in PAGES)}")
print(f"  'climb' in edition SVG text nodes: {'climb' in ed_all}")

print("=== C. non-CJK added/removed strings (freeze diff, own filter) ===")
fd = json.load(open(os.path.join(PROOF, "freeze-diff-proof.json")))
CJK = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\u3000-\u303f\uff00-\uffef]')
for pg, v in fd["pages"].items():
    for kind in ["added_strings", "removed_strings"]:
        non = [x["text"] for x in v[kind] if not CJK.search(x["text"])]
        print(f"  p{pg} {kind} non-CJK ({len(non)}): {non}")

print("=== D. TC independence: charset union ===")
CJKC = re.compile(r'[\u4e00-\u9fff]')
ed_chars = set()
for pg in PAGES:
    for t in EDT[pg][0]:
        ed_chars |= set(CJKC.findall(t["t"]))
ref_dirs = [W43,
            os.path.join(BASE, "files/weekly-report-w45-zhtw-core/svg"),
            os.path.join(BASE, "files/weekly-report-w45-nl-zh-tw/svg"),
            os.path.join(BASE, "files/weekly-report-w45-es-zh-tw/svg"),
            os.path.join(BASE, "files/weekly-report-w45-de-zh-tw/svg"),
            os.path.join(BASE, "files/weekly-report-w45-ru-zh-tw/svg")]
ref_chars = set(); missing_dirs = []
for d in ref_dirs:
    if not os.path.isdir(d):
        missing_dirs.append(d); continue
    for f in glob.glob(os.path.join(d, "*.svg")):
        ts, _ = texts_of(f)
        for t in ts:
            ref_chars |= set(CJKC.findall(t["t"]))
unseen = sorted(ed_chars - ref_chars)
print(f"  edition CJK chars: {len(ed_chars)}; ref union: {len(ref_chars)}; unseen: {len(unseen)}")
print(f"  unseen: {''.join(unseen)}")
print(f"  missing ref dirs: {missing_dirs}")
print(f"  builder claimed unseen (24): 亡亮努匆容寂彌懷撒燃牢盧碑禱腦菊藍藏近遲靈頁額魂")
print(f"  match builder set exactly: {set(unseen) == set('亡亮努匆容寂彌懷撒燃牢盧碑禱腦菊藍藏近遲靈頁額魂')}")
for ch in unseen:
    ctx = []
    for pg in PAGES:
        for t in EDT[pg][0]:
            if ch in t["t"]:
                ctx.append(f"{pg}:{t['t'][:48]}")
    print(f"    {ch} U+{ord(ch):04X} :: {ctx[:3]}")

print("=== E. independent SC-codepoint scan (own list, not builder's) ===")
SC = set("发让说国对车马门问电话语学头义云龙着钟种获达练认识为带见级别关开进远运动读写长闭观览赛胜负续亲卢贝奥与兴汉双仅仪尔杰枪桥桩洁涛泽弯湾玛琼毕莱欧苏兰亚图书万亿乔劳历郑邻邓邮释译诚诺护报担拟挣测传专创东发广辽宁鲁陕湘鄂豫冀晋皖赣琼滇黔")
print(f"  SC hits in edition SVGs: {sorted(ed_chars & SC)}")
for fn in ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py",
           "content8.py", "render.py", "transform.py", "svglib.py"]:
    fc = set(CJKC.findall(open(os.path.join(EB, fn), encoding='utf-8').read()))
    print(f"  SC hits in {fn}: {sorted(fc & SC)}")

print("=== F. mainland word scans + TC correct forms ===")
SC_WORDS = ["代码", "比赛项目", "报道", "集市", "把词组成", "搜索", "数据", "信息",
            "视频", "网络", "软件", "质量", "出租车", "网友", "博客", "视频", "程式码",
            "比赛專案", "報道", "片語成", "只", "仅"]
for w in SC_WORDS:
    c = ed_all.count(w)
    if c:
        print(f"  HIT {w}: {c}")
print("  (no HIT line above = 0 for that word)")
for w in ["代碼", "比賽項目", "報導", "市集", "把詞組成正確的句子"]:
    print(f"  TC form {w}: count={ed_all.count(w)}")
print("=== G. 只 / 僅 contexts ===")
for ch in ["只", "僅"]:
    for pg in PAGES:
        for t in EDT[pg][0]:
            if ch in t["t"]:
                print(f"  {ch} {pg}: {t['t'][:80]}")
print("=== H. quotes + 松 ===")
print(f"  ASCII double-quote in SVG text: {ed_all.count(chr(34))}")
print(f"  CJK straight quotes “”: {ed_all.count(chr(0x201c)) + ed_all.count(chr(0x201d))}")
print(f"  corner brackets 「」: {ed_all.count(chr(0x300c))} / {ed_all.count(chr(0x300d))}")
for pg in PAGES:
    for t in EDT[pg][0]:
        if "松" in t["t"]:
            print(f"  松 {pg}: {t['t'][:80]}  inside馬拉松={'馬拉松' in t['t']}")

print("=== I. exercise counts, chips method, edition vs core ===")
def chip_count(T):
    tot = 0; by_level = {}; by_page = {}
    for pg in PAGES:
        ts = T[pg][0]
        chips = [t for t in ts if t["size"] == 19 and t["t"] in ("A2", "B1", "B2") and t.get("fill") == "#fdfaf0"]
        ranges = {}
        for t in ts:
            m = re.fullmatch(r"(\d+)–(\d+)\.", t["t"])
            if m and t["size"] == 24:
                ranges[(t["x"], t["y"])] = int(m.group(2)) - int(m.group(1)) + 1
        n = 0; lv = {}
        for c in chips:
            k = 1
            for (x, y), ln in ranges.items():
                if abs(y - c["y"]) < 2 and abs(x - (c["x"] + 42)) < 3:
                    k = ln
            n += k; lv[c["t"]] = lv.get(c["t"], 0) + k
        by_page[pg] = n; tot += n
        for k2, v in lv.items():
            by_level[k2] = by_level.get(k2, 0) + v
        print(f"  {pg}: {n} {lv}")
    print(f"  TOTAL {tot} {by_level}")
    return tot, by_level, by_page
print("  edition:"); e_tot, e_lv, e_pg = chip_count(EDT)
print("  core:"); c_tot, c_lv, c_pg = chip_count(COT)
print(f"  edition==core: {e_tot == c_tot and e_lv == c_lv and e_pg == c_pg}")

print("=== J. gloss counts (ast read-only, split on U+00B7) + rendered headwords ===")
def gloss_counts(builddir):
    out = {}
    for fn in ["content12.py", "content34.py", "content56.py"]:
        src = open(os.path.join(builddir, fn), encoding='utf-8').read()
        tree = ast.parse(src)
        per = []
        items_all = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and getattr(node.func, 'attr', '') == 'gloss' and node.args:
                a = node.args[0]
                if isinstance(a, ast.Constant):
                    items = a.value.split('·')
                    per.append(len(items)); items_all.extend(items)
        out[fn] = (per, items_all)
    return out
gc = gloss_counts(CB); ge = gloss_counts(EB)
for fn in ["content12.py", "content34.py", "content56.py"]:
    print(f"  {fn} core={gc[fn][0]} edition={ge[fn][0]}")
print(f"  totals core={sum(sum(v[0]) for v in gc.values())} edition={sum(sum(v[0]) for v in ge.values())}")
ed_joined = "".join(t["t"] for pg in PAGES for t in EDT[pg][0])
miss = []
for fn in ["content12.py", "content34.py", "content56.py"]:
    for it in ge[fn][1]:
        head = re.split(r'[ ＝=·]', it.strip())[0]
        if head and head not in ed_joined:
            miss.append((fn, it[:40], head))
print(f"  rendered-headword misses: {miss}")

print("=== K. P7 quotes 2x + tags, edition vs core ===")
quotes = ["Do feriadão à prova: a semana do Enem",
          "Muita gente viaja, visita a família e vai ao cemitério levar flores",
          "Finados é o dia da memória", "lembrar é um jeito de continuar perto",
          "cada ponto vale uma posição, cada gol vale uma história",
          "quem dorme bem lembra melhor", "primeiro as fáceis, depois as difíceis",
          "Confira o cartão, durma bem, chegue cedo"]
for label, T in [("edition", EDT), ("core", COT)]:
    alltext = " ".join(t["t"] for pg in PAGES for t in T[pg][0])
    norm = re.sub(r"\s+", " ", alltext.replace("«", "").replace("»", ""))
    print(f"  {label}: " + ", ".join(f"{norm.count(q)}" for q in quotes))
    tags = Counter()
    for t in T["p7-lingua"][0]:
        for mm in re.finditer(r"\(Página (\d)\)", t["t"]):
            tags[mm.group(1)] += 1
    print(f"  {label} P7 tags: {dict(sorted(tags.items()))}")

print("=== L. readers garden: verbatim extracts ===")
for label, T in [("core", COT), ("edition", EDT)]:
    print(f"  --- {label} P7 lines containing Nota/redação/cartas/來信/編輯部/說明/順延/VOL.3/預告 ---")
    for t in T["p7-lingua"][0]:
        if any(k in t["t"] for k in ["Nota da redação", "cartas", "redação", "來信", "編輯部", "說明", "順延", "VOL.3", "預告", "PRÓXIMA"]):
            print(f"    y={t['y']} size={t['size']}: {t['t'][:130]}")
print("  --- PT disclosure: core vs edition identical multiset? ---")
def pt_disclosure(T):
    return sorted(t["t"] for t in T["p7-lingua"][0] if "Nota da redação" in t["t"] or "VOL.1" in t["t"] and "cartas" in t["t"])
print("  core:", pt_disclosure(COT))
print("  edition:", pt_disclosure(EDT))
print("=== M. P7 lone 。 line + preview-box geometry ===")
for t in EDT["p7-lingua"][0]:
    if t["t"].strip() == "。":
        print(f"  lone 。 at x={t['x']} y={t['y']} size={t['size']} fam={t['fam']}")
s7 = EDT["p7-lingua"][1]
for m in RECT_RE.finditer(s7):
    x, y, w, h = (float(m.group(i)) for i in (1, 2, 3, 4))
    if y >= 2300 and w > 1000:
        print(f"  wide rect y={y} h={h} x={x} w={w} fill={m.group(5)} (bottom {y+h})")
for t in EDT["p7-lingua"][0]:
    if t["y"] >= 2350:
        print(f"  P7 low text y={t['y']}: {t['t'][:70]}")

print("=== N. P8 raw lines for keydiff items + 101 + 139/140/150 ===")
def p8_lines(T, nums):
    out = {}
    for t in T["p8-avaliacao"][0]:
        m = re.match(r"^(\d+)\.\s", t["t"])
        if m and int(m.group(1)) in nums:
            out.setdefault(int(m.group(1)), []).append(t["t"])
    return out
nums = {2, 4, 101, 137, 138, 139, 140, 146, 150}
cl = p8_lines(COT, nums); el = p8_lines(EDT, nums)
for n in sorted(nums):
    print(f"  #{n} core: {cl.get(n)}")
    print(f"  #{n} ed:   {el.get(n)}")
    print(f"  #{n} identical: {cl.get(n) == el.get(n)}")

print("=== O. P8 notes language: SC chars in edition P8 text ===")
p8ed = "".join(t["t"] for t in EDT["p8-avaliacao"][0])
print(f"  SC hits in edition P8: {sorted(set(CJKC.findall(p8ed)) & SC)}")
for t in EDT["p8-avaliacao"][0]:
    if "RESPOSTAS" in t["t"] or "參考答案" in t["t"]:
        print(f"  P8 header ed: {t['t'][:120]}")
for t in COT["p8-avaliacao"][0]:
    if "RESPOSTAS" in t["t"]:
        print(f"  P8 header core: {t['t'][:120]}")
for t in W43T["p8-avaliacao"][0]:
    if "RESPOSTAS" in t["t"]:
        print(f"  P8 header W43: {t['t'][:120]}")

print("=== P. furniture vs W43 (measured) ===")
def pick(T, pg, pred, label):
    hits = [t for t in T[pg][0] if pred(t)]
    print(f"  {label}: {[(round(t['y'],1), t['size'], t['t'][:90]) for t in hits]}")
for label, T in [("W43", W43T), ("W45ed", EDT)]:
    print(f"  --- {label} ---")
    pick(T, "p1-capa", lambda t: abs(t["y"] - 372) < 3, "P1 y=372 line")
    pick(T, "p1-capa", lambda t: "TODA SEMANA" in t["t"] or "每週一期" in t["t"], "P1 top strip")
    pick(T, "p1-capa", lambda t: abs(t["y"] - 330) < 3, "P1 y=330 subtitle")
    pick(T, "p1-capa", lambda t: "A Lucerna" in t["t"] and "週報" in t["t"], "footer P1")
    pick(T, "p2-vida", lambda t: "A Lucerna" in t["t"] and "週報" in t["t"], "footer P2")
    pick(T, "p1-capa", lambda t: t["t"].startswith("第 1 版") or t["t"].startswith("第 1 版"), "page line P1")
    pick(T, "p2-vida", lambda t: "譯注｜" in t["t"], "gloss prefix P2 (first)")
    pick(T, "p8-avaliacao", lambda t: "第 1 版" in t["t"] or "第 2 版" in t["t"], "P8 separators sample")
    pick(T, "p1-capa", lambda t: "講解｜" in t["t"], "講解｜ P1")
print("=== Q. images: payload hash + credits ===")
IMG_RE = re.compile(r'<image[^>]*xlink:href="([^"]{0,80})')
def img_info(d):
    out = {}
    for pg in PAGES:
        s = open(os.path.join(d, pg + ".svg"), encoding='utf-8').read()
        hrefs = re.findall(r'<image[^>]*?href="([^"]+)"', s)
        hs = [hashlib.sha256(h.encode()).hexdigest()[:16] for h in hrefs]
        out[pg] = (len(hrefs), hs)
    return out
ci = img_info(CO); ei = img_info(ED)
for pg in PAGES:
    print(f"  {pg} core n={ci[pg][0]} ed n={ei[pg][0]} payloads identical: {ci[pg][1] == ei[pg][1]}")
    if ci[pg][1] != ei[pg][1]:
        print(f"    core {ci[pg][1]} ed {ei[pg][1]}")
for label, T in [("core", COT), ("edition", EDT)]:
    print(f"  --- credits {label} ---")
    for pg in PAGES:
        for t in T[pg][0]:
            if any(k in t["t"] for k in ["©", "Wikimedia", "Commons", "出處", "來源", "Public domain", "Domínio público"]):
                print(f"    {pg}: {t['t'][:110]}")

print("=== R. ABSTRACT ===")
ab = open(os.path.join(BASE, "files/weekly-report-w45-pt-zh-tw/ABSTRACT.txt"), encoding='utf-8').read()
print(f"  raw repr: {ab!r}")
print(f"  lines (strip): {len(ab.strip().splitlines())} chars: {len(ab.strip())} ASCII-dquote: {ab.count(chr(34))}")
for kw in ["亡靈節", "Enem", "巴西盃", "米內羅競技", "格雷米奧", "瓦斯科", "帕爾梅拉斯", "葡萄牙語", "A2", "B2", "150", "學葡萄牙語"]:
    print(f"  keyword {kw}: {kw in ab}")

print("=== S. essay model (content8 source, read-only) ===")
for label, bd in [("core", CB), ("edition", EB)]:
    src = open(os.path.join(bd, "content8.py"), encoding='utf-8').read()
    tree = ast.parse(src)
    cands = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and len(node.value) > 200:
            cands.append(node.value)
    for c in cands:
        print(f"  {label} long-string words={len(c.split())} head={c[:90]!r}")
    if not cands:
        print(f"  {label}: no >200-char string constant found")

print("=== T. delivery hashes vs final.sha256 + run1 scope ===")
fin = {}
for line in open(os.path.join(EB, "final.sha256"), encoding='utf-8'):
    parts = line.split()
    if len(parts) == 2:
        fin[parts[1]] = parts[0]
ok = True
for rel, h in fin.items():
    p = os.path.join(BASE, rel)
    cur = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    match = (cur == h)
    ok &= match
    print(f"  {rel}: {'OK' if match else 'MISMATCH cur=' + cur}")
print(f"  all final.sha256 match current delivery: {ok}")
r1 = {}
for line in open(os.path.join(EB, "run1-full.sha256"), encoding='utf-8'):
    parts = line.split()
    if len(parts) == 2:
        r1[parts[1]] = parts[0]
diffs = [k for k in fin if k in r1 and fin[k] != r1[k]]
print(f"  run1->final differing files: {diffs}")
print(f"  run1-only / final-only keys: {[k for k in r1 if k not in fin]} / {[k for k in fin if k not in r1]}")
print("=== U. core hashes at proof time ===")
for pg in PAGES:
    cur = hashlib.sha256(open(os.path.join(CO, pg + ".svg"), 'rb').read()).hexdigest()
    print(f"  {pg}: {cur[:16]}")
