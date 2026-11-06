# -*- coding: utf-8 -*-
"""Independent proof script for W45 zh-tw x ja (proofreader-written, fresh).
Reads only; writes report text to stdout (captured by caller)."""
import ast, base64, hashlib, html, json, os, re, sys
from collections import Counter

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_SVG = os.path.join(GOAL, "files/weekly-report-w45-zhtw-core/svg")
ED_SVG = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja/svg")
W43_SVG = os.path.join(GOAL, "files/weekly-report-zh-tw-ja/svg")
CORE_BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w45-zhtw-build")
ED_BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w45-zh-tw-ja-build")
WORK = os.path.join(GOAL, "hidden_files/w45/zh-tw-ja-proof/work")
TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
CJK_RE = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
KANA_RE = re.compile(r"[\u3040-\u30ff]")
HAN_RE = re.compile(r"[\u4e00-\u9fff]")

def texts(d):
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            s = open(os.path.join(d, fn), encoding="utf-8").read()
            out[fn] = [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TEXT_RE.findall(s)]
    return out

def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()

core_txt, ed_txt, w43_txt = texts(CORE_SVG), texts(ED_SVG), texts(W43_SVG)

print("== PINS ==")
kit_pins = {
 "p1-front.svg": "dc36d99206915d076365d95826e664e73a5065b64bed90177d18a51b815eaac5",
 "p2-life.svg": "45872bce8345bbaf8863e4ff3bd16df40ab069686bd51808826eff1bcc1437bd",
 "p3-culture.svg": "aa58b266ec10b54a19197f2ba8903a2dd742d920a1c3eb4d9661f4c3a0634ce",
 "p4-sport.svg": "701bd92da8f101e3a8d8296bc468c90422d30a56027a35edd2e2275a13b749d1",
 "p5-youth.svg": "c203ed08b951f95f6e49a1e432e50cc6b51fee22c62e764f6658f6cbf4c94103",
 "p6-deep.svg": "9970560b86c78ba1550985495910d203767ba8a77821099a27f590f7c91d2b29",
 "p7-lang.svg": "e07438a80eccc83423562bbd9155744e2533bdb7d6d077f24d8c78c687ffd9c3",
 "p8-test.svg": "8e2b224d93a219140559b630cd93ec5c090c302a940415a7a7a847cc45e7b1e3",
}
for fn, want in kit_pins.items():
    got = sha(os.path.join(ED_SVG, fn))
    print(f"  {fn} match={got == want} {got[:16]}")
core_pins = {"p1-front.svg": "4672c972763b0eaf", "p2-life.svg": "889fb533ef3ff62e",
 "p3-culture.svg": "508703c2b3c313c6", "p4-sport.svg": "e04b62ea6211c9ff",
 "p5-youth.svg": "4dfce72d88000fbc", "p6-deep.svg": "06ba4c6627cb8165",
 "p7-lang.svg": "00ac7f57125fcc09", "p8-test.svg": "e6e97d02595aef3b"}
for fn, want in core_pins.items():
    got = sha(os.path.join(CORE_SVG, fn))[:16]
    print(f"  CORE {fn} unchanged={got == want} {got}")
from PIL import Image
card_bytes = {"p1-front.png": 1131378, "p2-life.png": 1270402, "p3-culture.png": 1072967,
 "p4-sport.png": 1044850, "p5-youth.png": 1335675, "p6-deep.png": 945176,
 "p7-lang.png": 1088820, "p8-test.png": 1292509}
for fn, want in card_bytes.items():
    p = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja/cards", fn)
    im = Image.open(p)
    print(f"  CARD {fn} bytes={os.path.getsize(p)} match={os.path.getsize(p)==want} size={im.size}")

print("== TRANSFORM AUDIT (AST rep pairs) ==")
tsrc = open(os.path.join(ED_BUILD, "transform.py"), encoding="utf-8").read()
tree = ast.parse(tsrc)
pairs = []
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "rep":
        args = [a.value for a in node.args if isinstance(a, ast.Constant)]
        if len(args) >= 3:
            pairs.append((args[0], args[1], args[2]))
print(f"  rep pairs: {len(pairs)}")
bad = []
for fn, old, new in pairs:
    oc = set(HAN_RE.findall(old)) | set(re.findall(r"[\u3040-\u30ff]", old))
    nc = set(HAN_RE.findall(new)) | set(re.findall(r"[\u3040-\u30ff]", new))
    # every CJK char in old must survive in new (Traditional parts kept verbatim)
    missing = oc - nc
    # punctuation/Traditional fragments: old stripped of Latin must be substring-ish;
    # use char-set check above plus: any Traditional-only run in old must appear in new
    for run in re.findall(r"[\u4e00-\u9fff]+", old):
        if run not in new:
            bad.append((fn, run, old[:50]))
    if missing:
        bad.append((fn, f"chars-missing:{sorted(missing)}", old[:50]))
print(f"  transform CJK-loss violations: {len(bad)} {bad[:10]}")
print(f"  conversion logic present: opencc={('opencc' in tsrc.lower())} s2t={('s2t' in tsrc)} mapping_table={('mapping' in tsrc.lower())}")
print(f"  rep() with expect counts: all pairs have expect? {[len(p) for p in pairs][:3]}")

print("== FREEZE-DIFF ATTRIBUTION (fresh diff json) ==")
fd = json.load(open(os.path.join(WORK, "freeze-diff.json")))
new_ns = ""
for fn, old, new in pairs:
    new_ns += new
def norm(s):
    table = str.maketrans({"？": "?", "！": "!", "：": ":", "；": ";", "，": ",",
                           "。": ".", "、": ",", "（": "(", "）": ")", "＋": "+",
                           "～": "~", "－": "-", "／": "/", "「": "", "」": "",
                           "『": "", "』": "", "・": ".", "…": "..."})
    return re.sub(r"\s+", "", s.translate(table))
new_all = norm(new_ns)
core_all = "".join(t for v in core_txt.values() for t in v)
core_all_n = norm(core_all)
inst_new = "".join(f"{n}ページ(全8ページ)" for n in range(1, 9)) + "".join(f"—{n}ページ—" for n in range(1, 9))
inst_old = "".join(f"第{n}版/共8版" for n in range(1, 9)) + "".join(f"—Page{n}—" for n in range(1, 9))
old_all = "".join(old for _, old, _ in pairs)
old_all_n = norm(old_all)
unattr_add, unattr_rem = [], []
suspicious_added_hanzi = []  # added strings with no kana, not in transform news
for pg, d in fd["pages"].items():
    for s in d.get("added_strings", []):
        st = s["text"] if isinstance(s, dict) else s
        nst = norm(st)
        nst2 = re.sub(r"^解説—", "", nst)
        nst2 = re.sub(r"^\d+\.\s*(✓\s*|.*?—\s*)", "", nst2)
        nst2 = re.sub(r"\s*\(p\.\s*\d\)$", "", nst2)
        if nst in new_all or nst in core_all_n or nst in inst_new or nst2 in new_all or nst2 in core_all_n:
            pass
        elif re.fullmatch(r"[\d\s·\-–.,:;()/]+", st) or st in ("Lucerna",) or st.startswith("Photo:"):
            pass
        else:
            unattr_add.append((pg, st[:70]))
        # pure-Hanzi added string not accounted by transform = possible target-text addition
        if not KANA_RE.search(st) and HAN_RE.search(st) and nst not in new_all and nst2 not in new_all and nst not in core_all_n:
            suspicious_added_hanzi.append((pg, st[:70]))
    for s in d.get("removed_strings", []):
        st = s["text"] if isinstance(s, dict) else s
        nst = norm(st)
        nst_note = re.sub(r"^\d+\.\s*(✓\s*|.*?—\s*)", "", nst)
        if nst in inst_old or st.startswith("Modelanswer:") or nst in old_all_n or nst_note in old_all_n:
            continue
        modelo = None
        if nst in core_all_n:
            continue
        unattr_rem.append((pg, st[:70]))
print(f"  unattributed ADDED: {len(unattr_add)} {unattr_add[:10]}")
print(f"  unattributed REMOVED: {len(unattr_rem)} {unattr_rem[:10]}")
print(f"  suspicious pure-Hanzi added strings: {len(suspicious_added_hanzi)} {suspicious_added_hanzi[:20]}")
for pg, d in fd["pages"].items():
    print(f"  {pg}: +{len(d.get('added_strings', []))}/-{len(d.get('removed_strings', []))}")

print("== UNION TEST (re-extracted) ==")
def cjk_set(txt):
    s = set()
    for v in txt.values():
        for t in v:
            s |= set(CJK_RE.findall(t))
    return s
ed_set = cjk_set(ed_txt)
union_set = cjk_set(w43_txt) | cjk_set(core_txt)
outside = sorted(ed_set - union_set)
print(f"  edition={len(ed_set)} union={len(union_set)} outside={len(outside)}")
print(f"  outside={outside}")
# adjudicate each outside char: find edition nodes containing it; kana? else does node contain kana?
for ch in outside:
    nodes = [t for v in ed_txt.values() for t in v if ch in t]
    with_kana = sum(1 for t in nodes if KANA_RE.search(t))
    print(f"    {ch!r} nodes={len(nodes)} with_kana={with_kana} ex={nodes[0][:60] if nodes else ''!r}")

print("== SIMPLIFIED-ONLY SPOT ==")
SIMP_ONLY = list("让说国学发对为经时车马龙凤云电动话语读认点头乐尔广厂厅开贝见长门问间队阳阴孙学宝实汉刘关应并复万与发")
shared = set()
for fn in core_txt:
    shared |= set(core_txt[fn]) & set(ed_txt[fn])
shared_text = "".join(shared)
print(f"  shared-string hits: {sorted(set(ch for ch in SIMP_ONLY if ch in shared_text))}")
ed_all_text = "".join(t for v in ed_txt.values() for t in v)
hits_all = sorted(set(ch for ch in SIMP_ONLY if ch in ed_all_text))
print(f"  all-edition-string hits: {hits_all}")
for ch in hits_all:
    nodes = [t for v in ed_txt.values() for t in v if ch in t]
    wk = sum(1 for t in nodes if KANA_RE.search(t))
    print(f"    {ch!r} nodes={len(nodes)} with_kana={wk} ex={nodes[0][:70]!r}")

print("== GOLDEN SENTENCES (core source quotes) ==")
c7 = open(os.path.join(CORE_BUILD, "content7.py"), encoding="utf-8").read()
m = re.search(r"quotes = \[(.*?)\n\]", c7, re.S)
quotes = re.findall(r"\((\"「[^\"]+\"),\s*\"[^\"]*\",\s*\"(p\. \d)\"\)", m.group(1))
print(f"  core quotes: {len(quotes)}")
e7 = open(os.path.join(ED_BUILD, "content7.py"), encoding="utf-8").read()
m2 = re.search(r"quotes = \[(.*?)\n\]", e7, re.S)
quotes_ed = re.findall(r"\((\"「[^\"]+\"),\s*\"[^\"]*\",\s*\"(p\. \d)\"\)", m2.group(1))
print(f"  edition quotes identical list: {quotes == quotes_ed}")
print(f"  tags core: {Counter(p for _, p in quotes)} ; tags edition: {Counter(p for _, p in quotes_ed)}")
def norm2(s):
    table = str.maketrans({"？": "?", "！": "!", "：": ":", "；": ";", "，": ",",
                           "。": ".", "、": ",", "（": "(", "）": ")", "＋": "+",
                           "～": "~", "－": "-", "／": "/", "「": "", "」": "",
                           "『": "", "』": "", "・": ".", "…": "..."})
    return re.sub(r"\s+", "", s.translate(table))
core_all_ns = norm2(core_all)
ed_all_ns = norm2(ed_all_text)
for q, pg in quotes:
    qq = q.strip('"')
    print(f"  {qq[:24]}... tag={pg} core_count={core_all_ns.count(norm2(qq))} ed_count={ed_all_ns.count(norm2(qq))}")
# tags as rendered on edition P7
p7ed = "".join(ed_txt["p7-lang.svg"])
print(f"  rendered edition P7 tags: {sorted(Counter(re.findall(r'\(p\. \d\)', p7ed)).items())}")
p7core = "".join(core_txt["p7-lang.svg"])
print(f"  rendered core P7 tags: {sorted(Counter(re.findall(r'\(p\. \d\)', p7core)).items())}")

print("== GLOSS / MATCH ==")
def gloss_rendered(txt):
    return {fn: sum(1 for t in v if t.startswith("解説 — ") or t.startswith("Notes｜")) for fn, v in txt.items()}
print(f"  gloss rendered core={gloss_rendered(core_txt)}")
print(f"  gloss rendered edition={gloss_rendered(ed_txt)}")
print(f"  core gloss strings contain '·': {[t for v in core_txt.values() for t in v if t.startswith('Notes｜') and '·' in t]}")
print(f"  edition gloss strings contain '·' in gloss body check: {[t[:40] for v in ed_txt.values() for t in v if t.startswith('解説 — ')]}")
# match: count via registry later; here check '語と意味を結ぶ' occurrences = match sets
for label, txt in [("core", core_txt), ("edition", ed_txt)]:
    n = sum(1 for v in txt.values() for t in v if "語と意味を結ぶ" in t or t.strip() == "Match")
    print(f"  {label} match-instr nodes: {n}")

print("== IMAGES ==")
def img_hashes(d):
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            s = open(os.path.join(d, fn), encoding="utf-8").read()
            out[fn] = sorted(hashlib.sha256(base64.b64decode(mm)).hexdigest()[:16]
                             for mm in re.findall(r"data:image/\w+;base64,([A-Za-z0-9+/=]+)", s))
    return out
ci, ei = img_hashes(CORE_SVG), img_hashes(ED_SVG)
print(f"  payloads identical: {ci == ei} {ci}")
for fn in core_txt:
    cc = sorted(t for t in core_txt[fn] if t.startswith("Photo:"))
    ec = sorted(t for t in ed_txt[fn] if t.startswith("Photo:"))
    print(f"  {fn} credits identical: {cc == ec} {cc}")

print("== FURNITURE THREE-WAY ==")
def find(txt, needles):
    out = {}
    for fn, v in txt.items():
        for t in v:
            for nd in needles:
                if nd in t:
                    out.setdefault(nd, []).append(fn)
    return out
for label, txt in [("CORE", core_txt), ("W43", w43_txt), ("ED", ed_txt)]:
    foot = sorted(set(t for v in txt.values() for t in v if t.startswith("Lucerna ·")))
    print(f"  {label} footers: {foot}")
    pageline = sorted(set(t for v in txt.values() for t in v if "ページ（全" in t or "版 / 共" in t))
    print(f"  {label} pagelines: {pageline}")
    p8head = sorted(set(t for v in txt.items() for t in v if "全解答と解説" in t or "Answer keys" in t))
    print(f"  {label} p8heads: {p8head}")
    seps = sorted(set(t for v in txt.values() for t in v if re.match(r"^— \d+ ページ —$", t.strip()) or re.match(r"^— Page \d+ —$", t.strip())))
    print(f"  {label} p8seps: {seps}")

print("== LATIN SWEEP ==")
for fn, v in ed_txt.items():
    for t in v:
        if re.search(r"[A-Za-z]{2,}", t):
            print(f"  {fn} :: {t[:130]}")
print("== ENGLISH-HEAD CHECKS ==")
heads = ["Work it out", "Did you get it", "Over to you", "Quick quiz", "Headline words",
 "This week", "Word of the week", "Practice example", "Read the chart", "Deep-read quiz",
 "True or false", "The big quiz", "Read and answer", "Say it in context", "Test & keys",
 "Language focus", "Fill in"]
for h in heads:
    print(f"  {h!r}: {ed_all_text.count(h)}")
for pg in ["p2-life.svg", "p3-culture.svg", "p5-youth.svg"]:
    n = sum(1 for t in ed_txt[pg] if "算一算 · 計算してみよう" in t)
    print(f"  {pg} 算一算·計算してみよう nodes: {n}")

print("== KINSOKU + APOSTROPHES ==")
CLOSERS = set("、。，．・：；？！）」』】》〉〕］｝\"'") | set("ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ")
n_nodes = sum(len(v) for v in ed_txt.values())
bad_starts = [(fn, t[:40]) for fn, v in ed_txt.items() for t in v if t and t[0] in CLOSERS]
print(f"  edition nodes={n_nodes} line-start closers={len(bad_starts)} {bad_starts[:10]}")
n_core = sum(len(v) for v in core_txt.values())
bad_core = [(fn, t[:40]) for fn, v in core_txt.items() for t in v if t and t[0] in CLOSERS]
print(f"  core nodes={n_core} line-start closers={len(bad_core)} {bad_core[:10]}")
apos = [(fn, t[:60]) for fn, v in ed_txt.items() for t in v if "'" in t]
print(f"  edition ASCII apostrophe nodes={len(apos)} {apos[:10]}")
apos_c = [(fn, t[:60]) for fn, v in core_txt.items() for t in v if "'" in t]
print(f"  core ASCII apostrophe nodes={len(apos_c)}")

print("== READERS CORNER FROZEN ==")
def corner(txt):
    v = txt["p7-lang.svg"]
    i = [j for j, t in enumerate(v) if "讀者園地" in t][0]
    return v[i:i+12]
print(f"  core corner == edition corner (letter+disclosure nodes): {corner(core_txt) == corner(ed_txt)}")
for t in corner(ed_txt):
    print(f"    {t!r}")
print("== AI FORMS ==")
for fn, v in ed_txt.items():
    for t in v:
        if "人工智慧" in t or "AI＋" in t or "AIはデータ" in t:
            print(f"  {fn} :: {t[:120]}")
for fn, v in core_txt.items():
    for t in v:
        if "人工智慧" in t or "AI+" in t or "AI helps" in t:
            print(f"  CORE {fn} :: {t[:120]}")

print("== ABSTRACT ==")
ab = open(os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja/ABSTRACT.txt"), encoding="utf-8").read()
print(f"  lines={ab.count(chr(10))} trailing_newline={ab.endswith(chr(10))} ascii_dquote={'chr(34)' in ab} has_dquote={chr(34) in ab}")
print(f"  text: {ab.strip()}")
print(f"  contains Lucerna={('Lucerna' in ab)} A2～B2={('A2～B2' in ab)} 150={('150' in ab)} 中国語（繁体字）={('中国語（繁体字）' in ab)}")
