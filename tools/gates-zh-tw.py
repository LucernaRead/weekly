#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-fanout gates for one zh-tw edition. Usage: gates.py <lang> <run-tag>
Writes a JSON summary + logs under <scratch>/gates/<lang>-<tag>/.
Assumes print+web PDFs and text.md already built in the edition dir.
Does NOT rebuild anything (except freeze.py baseline, which rebuilds a
scratch copy only)."""
import collections, glob, html, json, os, re, subprocess, sys

HOME = os.path.expanduser("~")
M = os.path.join(HOME, "workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-refanout-zh-tw")
WEEK = os.path.join(HOME, "workspace/weekly-git")
VENV = os.path.join(WEEK, "tools/venv/bin/python")
TOOLS = os.path.join(WEEK, "tools")
CORE = os.path.join(WEEK, "production/2026-w47/core-zh-tw")

LANG = sys.argv[1]
TAG = sys.argv[2] if len(sys.argv) > 2 else "final"
UP = LANG.upper()
ED = os.path.join(WEEK, f"production/2026-w47/2026-w47-zh-tw-{LANG}")
SLUG = f"2026-w47-zh-tw-{LANG}"
G = os.path.join(M, "gates", f"{LANG}-{TAG}")
os.makedirs(G, exist_ok=True)
res = {"lang": LANG, "tag": TAG, "edition": SLUG, "gates": {}}

def run(cmd, logname, cwd=None, expect=0):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    open(os.path.join(G, logname), "w", encoding="utf-8").write(p.stdout + p.stderr)
    ok = (p.returncode == expect)
    return ok, p

def svg_texts(d):
    out = []
    for f in sorted(glob.glob(os.path.join(d, "*.svg"))):
        s = open(f, encoding="utf-8").read()
        for c in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S):
            t = html.unescape(re.sub(r"<[^>]+>", "", c)).strip()
            if t:
                out.append(t)
    return out

def multiset_diff(a, b):
    ca, cb = collections.Counter(a), collections.Counter(b)
    return {k: ca[k] - cb[k] for k in set(ca) | set(cb) if ca[k] != cb[k]}

# ---- 1. checks.py ----
ok, p = run([VENV, "checks.py"], "checks.log", cwd=ED)
res["gates"]["checks"] = {"rc": p.returncode,
                          "pass": ("CHECKS PASS" in p.stdout or "PASS" in p.stdout) and p.returncode == 0,
                          "tail": (p.stdout + p.stderr).strip().splitlines()[-3:]}

# ---- 2. occlusion selftest + audit ----
ok, p = run([VENV, os.path.join(TOOLS, "occlusion_audit.py"), "--selftest"], "occlusion-selftest.log")
selftest_ok = p.returncode == 0
ok, p = run([VENV, os.path.join(TOOLS, "occlusion_audit.py"), "--json",
             os.path.join(G, "occlusion.json"), os.path.join(ED, "svg")], "occlusion.log")
oc = json.load(open(os.path.join(G, "occlusion.json"))) if os.path.exists(os.path.join(G, "occlusion.json")) else {}
flags = oc.get("flag_count", oc.get("flags", "?"))
if isinstance(flags, list):
    flags = len(flags)
res["gates"]["occlusion"] = {"selftest_rc": 0 if selftest_ok else 1, "flags": flags, "rc": p.returncode}

# ---- 3. p8 extract + compare (explicit --core-p8 / --edition-p8) ----
ok, p = run([VENV, os.path.join(TOOLS, "p8.py"), "extract", "--p8",
             os.path.join(ED, "svg/p8-test.svg"), "--total", "150",
             "--json", os.path.join(G, "p8-extract.json")], "p8-extract.log")
ext = json.load(open(os.path.join(G, "p8-extract.json"))) if os.path.exists(os.path.join(G, "p8-extract.json")) else {}
noted = len(ext["noted_set"]) if "noted_set" in ext else ext.get("noted", ext.get("count", "?"))
ok, p = run([VENV, os.path.join(TOOLS, "p8.py"), "compare",
             "--core-p8", os.path.join(CORE, "svg/p8-test.svg"),
             "--edition-p8", os.path.join(ED, "svg/p8-test.svg"),
             "--total", "150", "--json", os.path.join(G, "p8-compare.json")], "p8-compare.log")
comp = json.load(open(os.path.join(G, "p8-compare.json"))) if os.path.exists(os.path.join(G, "p8-compare.json")) else {}
res["gates"]["p8"] = {"extract_noted": noted, "compare": comp.get("status", comp),
                      "keydiff": comp.get("keydiff", "?"), "missing": comp.get("missing", "?"),
                      "extra": comp.get("extra", "?")}  # NOTE: JSON key is `extra`, not `extra_count`

# ---- 4. canonical creambox full scan ----
ok, p = run(["python3", os.path.join(HOME, "workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py")]
            + sorted(glob.glob(os.path.join(ED, "svg/*.svg"))), "creambox.log")
clog = open(os.path.join(G, "creambox.log"), encoding="utf-8").read()
sections = {}
cur = None
for ln in clog.splitlines():
    if ln.startswith("== "):
        cur = ln[3:].strip()
        sections[cur] = []
    elif cur is not None:
        sections[cur].append(ln)
boxes = len(re.findall(r"inside-only", clog))
neg = [float(v) for v in re.findall(r"inside-only(?: \[P7-TOOLBOX\])?: last baseline [\d.]+ clearance ([+-]?[\d.]+)", clog) if float(v) < 0]
toolbox = [(round(float(v), 1), t[:44]) for v, t in re.findall(r"inside-only \[P7-TOOLBOX\]: last baseline [\d.]+ clearance ([+-]?[\d.]+) desc-clear [+-]?[\d.]+ \| '(.*?)'", clog)]
p7min = None
allmins = {}
for path, lines in sections.items():
    vals = [float(v) for v in re.findall(r"inside-only(?: \[P7-TOOLBOX\])?: last baseline [\d.]+ clearance ([+-]?[\d.]+)", "\n".join(lines))]
    if vals:
        allmins[path.split("/")[-1]] = round(min(vals), 1)
p7key = [k for k in allmins if "p7-lang" in k]
p7min = allmins[p7key[0]] if p7key else None
res["gates"]["creambox_canonical"] = {"boxes": boxes, "negative_inside_clearances": neg,
                                      "p7_min_inside_clearance": p7min, "min_inside_clearance_by_page": allmins,
                                      "p7_toolbox_clearances": toolbox, "rc": p.returncode}

# ---- 5. boxtitle + PIL creambox (parameterized copies) ----
ok, p = run([VENV, os.path.join(M, "gtools/boxtitle.py"), os.path.join(ED, "svg"), G], "boxtitle.log")
blog = open(os.path.join(G, "boxtitle.log"), encoding="utf-8").read()
m = re.search(r"title/line overruns past box right edge: (\d+)", blog)
m2 = re.search(r"min title right margin overall: ([-\d.]+) px", blog)
res["gates"]["boxtitle"] = {"boxes": re.search(r"boxes measured: (\d+)", blog).group(1) if re.search(r"boxes measured: (\d+)", blog) else "?",
                            "overruns": int(m.group(1)) if m else "?",
                            "min_right_margin": float(m2.group(1)) if m2 else None, "rc": p.returncode}
ok, p = run([VENV, os.path.join(M, "gtools/creambox-pil.py"), os.path.join(ED, "svg"), G], "creambox-pil.log")
plog = open(os.path.join(G, "creambox-pil.log"), encoding="utf-8").read()
strad = re.search(r"STRADDLE flags: (\d+)", plog)
cover = re.search(r"CREAM-COVER flags: (\d+)", plog)
p7lines = [ln.strip() for ln in plog.splitlines() if ln.strip().startswith(("p7", "[1439", "[")) and "clearance" in ln]
p7min_pil = None
p7vals = []
for ln in plog.split("P7 cream boxes")[1].splitlines() if "P7 cream boxes" in plog else []:
    mm = re.search(r"'bottom': ([-\d.]+)", ln)
    if mm:
        p7vals.append(float(mm.group(1)))
if p7vals:
    p7min_pil = min(p7vals)
res["gates"]["creambox_pil"] = {"straddle": int(strad.group(1)) if strad else "?",
                               "cream_cover": int(cover.group(1)) if cover else "?",
                               "p7_min_clearance": p7min_pil, "rc": p.returncode}

# ---- 6. text layer print vs web ----
def pdftotext(pdf, out):
    subprocess.run(["pdftotext", "-layout", pdf, out], capture_output=True)
pp = os.path.join(ED, f"Lucerna-VOL4-{UP}.pdf")
wp = os.path.join(ED, f"Lucerna-VOL4-{UP}-web.pdf")
run(["pdftotext", "-layout", pp, os.path.join(G, "print.txt")], "pdftotext-print.log")
run(["pdftotext", "-layout", wp, os.path.join(G, "web.txt")], "pdftotext-web.log")
pt = open(os.path.join(G, "print.txt"), encoding="utf-8", errors="replace").read()
wt = open(os.path.join(G, "web.txt"), encoding="utf-8", errors="replace").read()
diff = multiset_diff(pt, wt)
def cnt(s, sub):
    return s.count(sub)
res["gates"]["text_layer"] = {"print_bytes": len(pt.encode()), "web_bytes": len(wt.encode()),
    "multiset_diff_chars": sum(abs(v) for v in diff.values()),
    "print_only": sum(v for v in diff.values() if v > 0),
    "web_only": sum(-v for v in diff.values() if v < 0),
    "counts_print": {"本週日": cnt(pt, "本週日"), "下週日": cnt(pt, "下週日"),
                     "BABYMONSTER": cnt(pt, "BABYMONSTER"), "取捨": cnt(pt, "取捨"),
                     "end point": cnt(pt, "end point"), "小雪": cnt(pt, "小雪")},
    "counts_web": {"本週日": cnt(wt, "本週日"), "下週日": cnt(wt, "下週日"),
                   "BABYMONSTER": cnt(wt, "BABYMONSTER"), "取捨": cnt(wt, "取捨"),
                   "end point": cnt(wt, "end point"), "小雪": cnt(wt, "小雪")}}

# ---- 7. PDF metrics via PyMuPDF ----
import fitz
out7 = {}
for name, path in [("print", pp), ("web", wp)]:
    doc = fitz.open(path)
    sizes = []
    for pg in doc:
        for b in pg.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                for sp in ln["spans"]:
                    sizes.append(sp["size"])
    p8 = doc[7]
    p8sizes = [sp["size"] for b in p8.get_text("dict")["blocks"] for ln in b.get("lines", []) for sp in ln["spans"]]
    out7[name] = {"pages": len(doc), "size_pt": [round(doc[0].rect.width, 1), round(doc[0].rect.height, 1)],
                   "p8_min_pt": round(min(p8sizes), 2) if p8sizes else None,
                   "p8_max_pt": round(max(p8sizes), 2) if p8sizes else None,
                   "bytes": os.path.getsize(path)}
    doc.close()
# headline size P1 (largest span on p1 that is the lead headline is hard to isolate;
# report p1 max size as sanity)
doc = fitz.open(pp)
p1sizes = sorted({round(sp["size"], 2) for b in doc[0].get_text("dict")["blocks"] for ln in b.get("lines", []) for sp in ln["spans"]}, reverse=True)
out7["p1_top_sizes"] = p1sizes[:4]
doc.close()
res["gates"]["pdf"] = out7

# ---- 8. keycheck: fill-in keys + key continuity ----
ok, p = run(["python3", os.path.join(M, "gtools/check_fillin_keys.py"),
             os.path.join(ED, f"{SLUG}.text.md"), ED], "fillin-check.log")
flog = open(os.path.join(G, "fillin-check.log"), encoding="utf-8").read()
fm = re.search(r"填空键总数: (\d+)", flog)
fmiss = re.search(r"缺失|MISS", flog)
textmd = open(os.path.join(ED, f"{SLUG}.text.md"), encoding="utf-8").read()
km = re.search(r"^答案\s", textmd, re.M)
keys_area = textmd[km.start():] if km else ""
nums = sorted({int(n) for n in re.findall(r"^(\d+)\.\s", keys_area, re.M)})
res["gates"]["keycheck"] = {"fillin_total": int(fm.group(1)) if fm else "?",
    "fillin_missing_lines": [ln for ln in flog.splitlines() if "MISS" in ln],
    "keys_continuous_1_150": (nums == list(range(1, 151))),
    "keys_found": len(nums)}

# ---- 9. leak scan: untranslated English source strings in edition SVGs ----
DENY = ["next Sunday", "Next Sunday", "finish line", "the place it happens",
        "The ceremony is at the Taipei Music Center.", "Xiaoxue is Nov 22.",
        "Four big events fall on the same Sunday.", "Collecting points is 集點.",
        "Memory trick: learn 入圍 first, then the ceremony",
        "Parades give you four useful words: 遊行 (parade), 封王 (clinching the title), 夜間 (night-time) and 終點 (finish line)"]
ed_texts = svg_texts(os.path.join(ED, "svg"))
core_texts = svg_texts(os.path.join(CORE, "svg"))
ed_joined = "\n".join(ed_texts)
leaks = {d: ed_joined.count(d) for d in DENY if ed_joined.count(d) > 0}
# mostly-ASCII long strings identical to core (English leftovers), minus shared proper nouns
def mostly_ascii(s):
    a = sum(1 for c in s if ord(c) < 128)
    return len(s) >= 15 and a / max(len(s), 1) >= 0.9
shared = sorted({t for t in ed_texts if mostly_ascii(t)} & set(core_texts))
res["gates"]["leak_scan"] = {"deny_hits": leaks, "shared_ascii_long": shared}

# ---- 10. abutting: P6 timeline adjacent-label true-ink gap ----
sys.path.insert(0, TOOLS)
import occlusion_audit as oa
els, W, H = oa.parse_svg(open(os.path.join(ED, "svg/p6-deep.svg"), encoding="utf-8").read())
texts = [e for e in els if e.kind == "text" and e.box]
def find_lbl(s):
    return [t for t in texts if s in (t.text or "")]
c1, c2 = find_lbl("頒獎典禮"), find_lbl("夜間遊行")
gap = None
lab1 = lab2 = None
best = None
for a in c1:
    for b in c2:
        if b.box[0] <= a.box[2]:
            continue
        if abs((a.box[1] + a.box[3]) / 2 - (b.box[1] + b.box[3]) / 2) > 5:
            continue
        gap_ab = b.box[0] - a.box[2]
        if best is None or gap_ab < best:
            best, lab1, lab2 = gap_ab, a, b
if lab1 and lab2:
    gap = round(lab2.box[0] - lab1.box[2], 1)
res["gates"]["abutting"] = {"p6_1830_1900_ink_gap_px": gap,
    "label1_box": [round(v, 1) for v in lab1.box] if lab1 else None,
    "label2_box": [round(v, 1) for v in lab2.box] if lab2 else None}

# ---- 11. freeze baseline (canonical; rebuilds a scratch copy only) ----
ok, p = run([VENV, os.path.join(TOOLS, "freeze.py"), "baseline", "--build", ".",
             "--core-svg", "svg", "--out", os.path.join(G, "freeze-base")],
            "freeze.log", cwd=ED)
flog2 = open(os.path.join(G, "freeze.log"), encoding="utf-8").read()
fm2 = re.search(r"baseline: (\d+)/(\d+) SVGs byte-identical", flog2)
res["gates"]["freeze"] = {"match": f"{fm2.group(1)}/{fm2.group(2)}" if fm2 else "?",
                          "rc": p.returncode, "log_tail": flog2.strip().splitlines()[-2:]}

# ---- 12. file SHAs ----
import hashlib
def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()
res["files"] = {
    "print_pdf": {"name": f"Lucerna-VOL4-{UP}.pdf", "bytes": os.path.getsize(pp), "sha256": sha(pp)},
    "web_pdf": {"name": f"Lucerna-VOL4-{UP}-web.pdf", "bytes": os.path.getsize(wp), "sha256": sha(wp)},
    "text_md": {"name": f"{SLUG}.text.md", "bytes": os.path.getsize(os.path.join(ED, f"{SLUG}.text.md")),
                "sha256": sha(os.path.join(ED, f"{SLUG}.text.md"))},
    "svg_sha256": {os.path.basename(f): sha(f) for f in sorted(glob.glob(os.path.join(ED, "svg/*.svg")))}}

json.dump(res, open(os.path.join(G, "gates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
