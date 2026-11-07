# -*- coding: utf-8 -*-
"""Self-verification for W45 zh-tw x ja (builder-side, before proofread).
Reads: core build sources, edition build sources, core/edition/W43 SVGs,
tools/scratch freeze-diff JSON. Prints PASS/FAIL lines + evidence lists.
"""
import ast, html, json, re, sys, os, base64, hashlib
from collections import Counter

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w45-zhtw-build")
ED_BUILD = os.path.join(GOAL, "hidden_files/weekly-report-w45-zh-tw-ja-build")
CORE_SVG = os.path.join(GOAL, "files/weekly-report-w45-zhtw-core/svg")
ED_SVG = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja/svg")
W43_SVG = os.path.join(GOAL, "files/weekly-report-zh-tw-ja/svg")
TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
CJK_RE = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
KANA_RE = re.compile(r"[\u3040-\u30ff]")


def texts(d):
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            s = open(os.path.join(d, fn), encoding="utf-8").read()
            out[fn] = [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TEXT_RE.findall(s)]
    return out


def literals(d, files):
    out = {}
    for fn in files:
        src = open(os.path.join(d, fn), encoding="utf-8").read()
        tree = ast.parse(src)
        out[fn] = [n.value for n in ast.walk(tree)
                   if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    return out


FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]
core_lit = literals(CORE_BUILD, FILES)
ed_src = {fn: open(os.path.join(ED_BUILD, fn), encoding="utf-8").read() for fn in FILES + ["bslib4.py"]}

# ---- A. source-level: every transform old string gone; every other literal kept
# Re-derive old strings from transform.py rep() calls (first arg after filename).
tsrc = open(os.path.join(ED_BUILD, "transform.py"), encoding="utf-8").read()
olds = re.findall(r"rep\(\"(\w+\.py)\", \"((?:[^\"\\]|\\.)*)\"", tsrc)
olds += [(fn, s) for fn, s in re.findall(r"rep\(\"(\w+\.py)\", '((?:[^'\\]|\\.)*)'", tsrc)]
oldset = {}
for fn, s in olds:
    oldset.setdefault(fn, []).append(s)
# transform NEW strings (second quoted arg of multi-line rep calls is on the
# next line; capture rep blocks instead: old -> new pairs in order)
newset = []
for m in re.finditer(r"rep\(\"(\w+\.py)\", \"((?:[^\"\\]|\\.)*)\",\s*\n?\s*\"((?:[^\"\\]|\\.)*)\"", tsrc):
    newset.append(m.group(3))
for m in re.finditer(r"rep\(\"(\w+\.py)\", '((?:[^'\\]|\\.)*)',\s*\n?\s*'((?:[^'\\]|\\.)*)'", tsrc):
    newset.append(m.group(3))


def norm(s):
    table = str.maketrans({"？": "?", "！": "!", "：": ":", "；": ";", "，": ",",
                           "。": ".", "、": ",", "（": "(", "）": ")", "＋": "+",
                           "～": "~", "－": "-", "／": "/", "「": "", "」": "",
                           "『": "", "』": "", "・": ".", "…": "..."})
    return re.sub(r"\s+", "", s.translate(table).replace("{NCHARS}", "138"))


new_all_ns = norm("".join(newset))
missing_old = []
for fn, lst in oldset.items():
    for s in lst:
        if s in ed_src[fn]:
            missing_old.append((fn, s[:60]))
print(f"A1 transform olds still present in edition sources: {len(missing_old)} {missing_old[:5]}")
ed_lit = literals(ED_BUILD, FILES + ["bslib4.py"])
kept_fail = []
for fn, lst in core_lit.items():
    from collections import Counter as _C
    cc, ec = _C(lst), _C(ed_lit.get(fn, []))
    for s in lst:
        if not s.strip():
            continue
        # skip literals that are (or contain) a replaced old string, code strings, paths
        if any(s == o or o in s or s in o for o in oldset.get(fn, [])):
            continue
        if s in ("serif", "sans", "middle", "end") or s.startswith("~") or s.startswith("#"):
            continue
        if ec[s] < cc[s]:
            kept_fail.append((fn, s[:70]))
            ec[s] += 1  # report each missing copy once per deficit only
print(f"A2 core literals lost from edition sources: {len(kept_fail)} {kept_fail[:5]}")

# ---- B. freeze-diff attribution
fd = json.load(open(os.path.join(GOAL, "tools/scratch/w45-zhtw-ja-freeze-diff-fix.json")))
core_txt = texts(CORE_SVG)
ed_txt = texts(ED_SVG)
core_all = "".join(t for v in core_txt.values() for t in v)
core_all_ns = re.sub(r"\s+", "", core_all)
core_en_lits = []
for lst in core_lit.values():
    for s in lst:
        if re.search(r"[A-Za-z]", s):
            core_en_lits.append(re.sub(r"\s+", "", s))
bad_added, bad_removed = [], []
core_all_n = norm(core_all)
# instantiated f-string furniture (page lines, separators) in both languages
inst_new = "".join(f"{n}ページ(全8ページ)" for n in range(1, 9))
inst_new += "".join(f"—{n}ページ—" for n in range(1, 9))
inst_old = "".join(f"第{n}版/共8版" for n in range(1, 9))
inst_old += "".join(f"—Page{n}—" for n in range(1, 9))
for pg, d in fd["pages"].items():
    for s in d.get("added_strings", []):
        st = s["text"] if isinstance(s, dict) else (s[0] if isinstance(s, list) else s)
        nst = norm(st)
        # strip gloss prefix and P8 key-line prefix before substring check
        nst2 = re.sub(r"^解説—", "", nst)
        nst2 = re.sub(r"^\d+\.\s*(✓\s*|.*?—\s*)", "", nst2)
        nst2 = re.sub(r"^モデル解答:", "", nst2)
        nst2 = re.sub(r"\s*\(p\.\s*\d\)$", "", nst2)
        if nst in new_all_ns or nst in core_all_n or nst in inst_new:
            continue
        if nst2 in new_all_ns or nst2 in core_all_n:
            continue
        if re.fullmatch(r"[\d\s·\-–.,:;()/]+", st):
            continue
        if st in ("Lucerna",) or st.startswith("Photo:"):
            continue
        bad_added.append((pg, st[:70]))
    for s in d.get("removed_strings", []):
        st = s["text"] if isinstance(s, dict) else (s[0] if isinstance(s, list) else s)
        nst = norm(st)
        # P8 key lines carry a frozen "N. KEY — " (or "N. ✓ ") prefix; strip it
        nst_note = re.sub(r"^\d+\.\s*(✓\s*|.*?—\s*)", "", nst)
        if nst in inst_old:
            continue  # instantiated old page lines / separators
        if nst.startswith("Modelanswer:"):
            continue  # old label + frozen MODELO text
        # frozen MODELO wrap fragments (label change re-wraps the same text)
        modelo = [s for s in core_lit.get("content8.py", []) if s.startswith("旅展從11月6日")]
        if modelo and (nst in norm(modelo[0]) or nst_note in norm(modelo[0])):
            continue
        # removed OK iff it is (a fragment of) a replaced old string / core English literal
        ok = False
        for fn, lst in oldset.items():
            for o in lst:
                if nst in norm(o) or norm(o) in nst or nst_note in norm(o) or norm(o) in nst_note:
                    ok = True
                    break
            if ok:
                break
        if not ok:
            for lit in core_en_lits:
                if nst in norm(lit) or nst_note in norm(lit):
                    ok = True
                    break
        if not ok:
            bad_removed.append((pg, st[:70]))
print(f"B1 unattributed ADDED strings: {len(bad_added)} {bad_added[:10]}")
print(f"B2 unattributed REMOVED strings: {len(bad_removed)} {bad_removed[:10]}")

# ---- C. CJK union set test
def cjk_set(txt):
    s = set()
    for v in txt.values():
        for t in v:
            s |= set(CJK_RE.findall(t))
    return s
ed_set = cjk_set(ed_txt)
union_set = cjk_set(texts(W43_SVG)) | cjk_set(core_txt)
outside = sorted(ed_set - union_set)
print(f"C union test: edition CJK set={len(ed_set)} union={len(union_set)} outside={len(outside)} {outside}")

# ---- D. Simplified-only spot list over frozen (shared) strings
SIMP_ONLY = list("让说国学发对为经时车马龙凤云电动话语读认点头乐尔广厂厅开贝见长门问间队阳阴孙学宝实汉刘关应并复万与发")
shared = set()
for fn in core_txt:
    shared |= set(core_txt[fn]) & set(ed_txt[fn])
shared_text = "".join(shared)
hits = sorted(set(ch for ch in SIMP_ONLY if ch in shared_text))
print(f"D Simplified-only spot hits over frozen shared strings: {len(hits)} {hits}")

# ---- E. gloss boxes + match sets + golden sentences
def gloss_count(txt):
    return {fn: sum(1 for t in v if t.startswith("解説 — ") or t.startswith("Notes｜")) for fn, v in txt.items()}
print(f"E1 gloss boxes core={gloss_count(core_txt)} edition={gloss_count(ed_txt)}")
# match lefts/rights: Traditional match lines are frozen; compare match-set lines (contain 'a. ' style rights?) -> compare full node multisets restricted to match pages
for fn in core_txt:
    cm, em = Counter(core_txt[fn]), Counter(ed_txt[fn])
    # frozen nodes: nodes identical in both, minus explanation churn
    print(f"E2 {fn}: core nodes={sum(cm.values())} edition nodes={sum(em.values())}")
# golden: 8 quotes from core content7, each exactly 2x issue-wide in edition
import subprocess
quotes = []
for m in re.finditer(r"\(\"「([^\"]+)\"", open(os.path.join(CORE_BUILD, "content7.py"), encoding="utf-8").read()):
    quotes.append("「" + m.group(1))
ed_all = "".join(t for v in ed_txt.values() for t in v)
ed_all_ns = norm(ed_all)
print(f"E3 golden quotes found in core source (incl. 3 clinic lines): {len(quotes)}")
for q in quotes:
    qns = norm(q)
    print(f"   {q[:22]}... count={ed_all_ns.count(qns)}")
# page tags
tags = re.findall(r"\(p\. \d\)", "".join(t for v in ed_txt.values() for t in v))
print(f"E4 P7 page tags in edition: {sorted(Counter(tags).items())}")

# ---- F. images: base64 payload hashes per page + credits
def img_hashes(d):
    out = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            s = open(os.path.join(d, fn), encoding="utf-8").read()
            out[fn] = sorted(hashlib.sha256(base64.b64decode(m)).hexdigest()[:16]
                             for m in re.findall(r"data:image/\w+;base64,([A-Za-z0-9+/=]+)", s))
    return out
ci, ei = img_hashes(CORE_SVG), img_hashes(ED_SVG)
print(f"F1 image payloads identical per page: {ci == ei} core={ci} edition={ei}")
for fn in core_txt:
    cc = sorted(t for t in core_txt[fn] if t.startswith("Photo:"))
    ec = sorted(t for t in ed_txt[fn] if t.startswith("Photo:"))
    print(f"F2 {fn} credits identical: {cc == ec} {cc}")

# ---- G. rendered-output sweep: dump EVERY edition node containing Latin letters
print("G rendered sweep: all edition nodes with [A-Za-z]{2,}:")
for fn, nodes in ed_txt.items():
    for t in nodes:
        if re.search(r"[A-Za-z]{2,}", t):
            print(f"   {fn} :: {t[:110]}")

# ---- H. kinsoku line-start / line-end scan (W43 zh-tw-ja precedent, fix round)
# Renderer NO_START (svglib) covers punctuation closers only; small kana
# (sutegana) are NOT in it, so they must be caught by scan. A node whose
# first character is in NO_START or is a small kana is a violation, as is a
# node whose last character is in NO_END (line-end opener).
NO_START = set("。、，．！？：；）」』】％ー…‥・)]}〉》.,!?%:;\"")
NO_END = set("「『（【〈《([{\"")
SMALL_KANA = set("ぁぃぅぇぉっゃゅょゎゕゖァィゥェォッャュョヮヵヶ")
h_start, h_small, h_end, h_total = [], [], [], 0
for fn, nodes in ed_txt.items():
    for t in nodes:
        if not t:
            continue
        h_total += 1
        if t[0] in SMALL_KANA:
            h_small.append((fn, t[:40]))
        elif t[0] in NO_START:
            h_start.append((fn, t[:40]))
        if t[-1] in NO_END:
            h_end.append((fn, t[:40]))
print(f"H kinsoku: nodes={h_total} NO_START={len(h_start)} {h_start[:5]} small-kana-starts={len(h_small)} {h_small[:5]} NO_END={len(h_end)} {h_end[:5]}")
