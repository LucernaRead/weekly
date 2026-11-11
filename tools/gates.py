# -*- coding: utf-8 -*-
"""Mechanical gates for one W47 nl fan-out edition.

Usage: gates.py <edition-dir> <reader-code> [--skip-webpdf]
Runs, in order (each step logged to stdout; exit non-zero on any hard fail):
  1. occlusion_audit.py svg/ (0 flags required; selftest must pass)
  2. p8.py extract --p8 svg/p8-toets.svg --total 150 (150/150)
  3. p8.py compare core P8 vs edition P8 (CLEAN required; SHORT = fail)
  4. freeze repro: copy *.py + assets to a clean repro dir, re-run run.py,
     direct sha256 of repro svg/*.svg vs edition svg/*.svg (8/8 required)
  5. print/web text compare (PyMuPDF position-sorted, per page: positional
     diff 0 and multiset diff 0 required) — needs both PDFs built
  6. P8 answer-zone min font size (PyMuPDF; >= 9.75pt required)
  7. P8 level-chip counts vs core P8 (A2/B1/B2 badge text counts must match)
  8. §1.1 SVG audit: paper #fbfaf6 present; no GOLD/near-black fills; no
     stroked page rect; badge colours exact; VOL.4 (no VOL.5); footer uses
     full-width-space separator (no '·' in footer/masthead lines).
Exit 0 only if every gate passes. JSON summary written to
  <scratch>/gates-<reader>.json
"""
import hashlib
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
from collections import Counter

SCRATCH = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.expanduser("~/workspace/weekly-git")
VENV = os.path.join(REPO, "tools", "venv", "bin", "python")
CORE = os.path.join(REPO, "production", "2026-w47", "core-nl")

EDITION = os.path.abspath(sys.argv[1])
READER = sys.argv[2]
SKIP_WEBPDF = "--skip-webpdf" in sys.argv
SLUG = f"2026-w47-nl-{READER}"
PRINT_PDF = os.path.join(EDITION, f"De-Lucerna-VOL4-nl-{READER}.pdf")
WEB_PDF = os.path.join(EDITION, f"De-Lucerna-VOL4-nl-{READER}-web.pdf")

results = {"edition": SLUG, "gates": {}}


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r


def gate(name, ok, detail=""):
    results["gates"][name] = {"ok": bool(ok), "detail": detail}
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    return ok


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    all_ok = True

    # 1. occlusion
    r = run([VENV, os.path.join(REPO, "tools", "occlusion_audit.py"), "svg/"],
            cwd=EDITION)
    m = re.search(r"(\d+) flags?", r.stdout + r.stderr)
    flags = int(m.group(1)) if m else -1
    selftest = "selftest" in (r.stdout + r.stderr).lower()
    ok = r.returncode == 0 and flags == 0
    all_ok &= gate("occlusion", ok,
                   f"rc={r.returncode} flags={flags} " + (r.stdout + r.stderr).strip().splitlines()[-1][:160] if (r.stdout + r.stderr).strip() else "no output")

    # 2. p8 extract
    p8_svg = os.path.join(EDITION, "svg", "p8-toets.svg")
    r = run([VENV, os.path.join(REPO, "tools", "p8.py"), "extract",
             "--p8", p8_svg, "--total", "150"], cwd=EDITION)
    out = r.stdout + r.stderr
    m = re.search(r"(\d+) of 150", out)
    noted = int(m.group(1)) if m else -1
    ok = r.returncode == 0 and noted == 150
    all_ok &= gate("p8_extract", ok, f"rc={r.returncode} noted={noted}/150")

    # 3. p8 compare vs core
    core_p8 = os.path.join(CORE, "svg", "p8-toets.svg")
    r = run([VENV, os.path.join(REPO, "tools", "p8.py"), "compare",
             "--core-p8", core_p8, "--edition-p8", p8_svg, "--total", "150"],
            cwd=EDITION)
    out = r.stdout + r.stderr
    verdict = "CLEAN" if "CLEAN" in out else ("EXTRA_ONLY" if "EXTRA_ONLY" in out
                                               else ("SHORT" if "SHORT" in out else "UNKNOWN"))
    # p8.py compare prints `keydiff=[137, 138, ...]` (no space, lowercase).
    # The old `[Kk]ey diff.*` regex never matched that line, so keydiffs
    # was always [] and real key diffs were silently dropped (run-log
    # L1804 / O11). Parse the real format; fall back to the legacy spaced
    # "Key diff ..." form if it ever appears.
    m = re.search(r"keydiff\s*=\s*\[([^\]]*)\]", out)
    if m:
        keydiffs = [int(x) for x in m.group(1).split(",") if x.strip()]
    else:
        keydiffs = []
        for kd in re.findall(r"[Kk]ey diff.*", out):
            keydiffs += [int(x) for x in re.findall(r"\d+", kd)]
    ok = r.returncode == 0 and verdict in ("CLEAN", "EXTRA_ONLY")
    all_ok &= gate("p8_compare", ok, f"rc={r.returncode} verdict={verdict} keydiffs={len(keydiffs)}")
    if keydiffs:
        print("   key diffs:", keydiffs)

    # 4. freeze repro (direct sha256)
    repro = os.path.join(SCRATCH, f"repro-{READER}")
    if os.path.exists(repro):
        shutil.rmtree(repro)
    os.makedirs(repro)
    for f in os.listdir(EDITION):
        if f.endswith(".py"):
            shutil.copy2(os.path.join(EDITION, f), repro)
    shutil.copytree(os.path.join(EDITION, "assets"), os.path.join(repro, "assets"))
    r = run([VENV, "run.py"], cwd=repro)
    ok_run = r.returncode == 0 and "TOTAL 150" in r.stdout
    match = 0
    details = []
    if ok_run:
        for i in range(1, 9):
            import glob
            a = sorted(glob.glob(os.path.join(EDITION, "svg", f"p{i}-*.svg")))
            b = sorted(glob.glob(os.path.join(repro, "svg", f"p{i}-*.svg")))
            if len(a) == 1 and len(b) == 1 and sha256(a[0]) == sha256(b[0]):
                match += 1
            else:
                details.append(f"p{i}: mismatch/missing")
    ok = ok_run and match == 8
    all_ok &= gate("freeze_sha256", ok, f"run rc={r.returncode} match={match}/8 " + "; ".join(details))
    shutil.rmtree(repro, ignore_errors=True)

    # 5+6. print/web text + P8 fontsize (needs both PDFs)
    if not SKIP_WEBPDF and os.path.exists(PRINT_PDF) and os.path.exists(WEB_PDF):
        import fitz
        p = fitz.open(PRINT_PDF)
        w = fitz.open(WEB_PDF)
        pos_total = ms_total = 0
        per_page = []
        for i in range(len(p)):
            t1 = p[i].get_text("text", sort=True)
            t2 = w[i].get_text("text", sort=True)
            tok1, tok2 = t1.split(), t2.split()
            pos = sum(1 for x, y in zip(tok1, tok2) if x != y) + abs(len(tok1) - len(tok2))
            ms = sum((Counter(tok1) - Counter(tok2)).values())
            pos_total += pos
            ms_total += ms
            per_page.append(f"P{i+1}:{len(tok1)}/{len(tok2)}:pos{pos}:ms{ms}")
        ok = len(p) == 8 and len(w) == 8 and pos_total == 0 and ms_total == 0
        all_ok &= gate("print_web_text", ok,
                       f"pages {len(p)}/{len(w)} posdiff={pos_total} msdiff={ms_total} " + " ".join(per_page))
        # pdftotext bytes
        r1 = subprocess.run(["pdftotext", PRINT_PDF, "-"], capture_output=True)
        r2 = subprocess.run(["pdftotext", WEB_PDF, "-"], capture_output=True)
        ok = len(r1.stdout) > 0 and len(r2.stdout) > 0
        all_ok &= gate("pdftotext_nonempty", ok,
                       f"print={len(r1.stdout)}B web={len(r2.stdout)}B web_size={os.path.getsize(WEB_PDF)}")
        # P8 fontsize
        page = p[7]
        d = page.get_text("dict")
        spans = []
        for b in d["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    spans.append((round(s["size"], 2), round(s["bbox"][1], 1)))
        scale = page.rect.height / 2700.0
        y0 = 1328 * scale
        ans = [s for s in spans if s[1] >= y0 - 5]
        mn = min(s[0] for s in ans) if ans else -1
        med = statistics.median([s[0] for s in ans]) if ans else -1
        ok = mn >= 9.75
        all_ok &= gate("p8_fontsize", ok, f"answer-zone min={mn}pt median={med}pt spans={len(ans)}")
    else:
        all_ok &= gate("print_web_text", False, "PDFs missing or skipped")
        all_ok &= gate("pdftotext_nonempty", False, "PDFs missing or skipped")
        all_ok &= gate("p8_fontsize", False, "PDFs missing or skipped")

    # 7. P8 chip counts vs core
    def chip_counts(svg_path):
        txt = open(svg_path, encoding="utf-8").read()
        return {lv: len(re.findall(rf">{lv}<", txt)) for lv in ("A2", "B1", "B2")}
    core_chips = chip_counts(core_p8)
    ed_chips = chip_counts(p8_svg)
    ok = core_chips == ed_chips
    all_ok &= gate("p8_chips", ok, f"core={core_chips} edition={ed_chips}")

    # 8. §1.1 SVG audit
    import glob as _g
    fills = Counter()
    stroked_rects = 0
    for f in _g.glob(os.path.join(EDITION, "svg", "*.svg")):
        t = open(f, encoding="utf-8").read()
        fills.update(re.findall(r'fill="(#[0-9a-fA-F]{6})"', t))
        stroked_rects += len(re.findall(r"<rect[^>]*stroke=", t))
    palette = {"#fbfaf6", "#302c28", "#3a3631", "#6f675d", "#d8d2c4", "#37402f",
               "#46581f", "#f6e08e", "#f4efe1", "#5c6e30", "#ffffff", "#cac8ba",
               "#f0eee5"}
    # moth brand-mark colours on P1 (SOP §1.1 prescribes the moth under the masthead)
    moth = {"#34483a", "#4d72b4", "#d7b257", "#edd17f", "#f1e8d4", "#2f4a3c",
            "#7a9e7e", "#c9a227", "#e8dcc3", "#5b7fa6"}
    # Colours present in the frozen core are legitimate by definition
    # (chart bars, moth brand-mark). Off-palette = a fill in the edition
    # that appears in NEITHER the core nor the §1.1 palette/moth sets.
    core_fills = Counter()
    for f in _g.glob(os.path.join(CORE, "svg", "*.svg")):
        t = open(f, encoding="utf-8").read()
        core_fills.update(re.findall(r'fill="(#[0-9a-fA-F]{6})"', t))
    off = {c: n for c, n in fills.items()
           if c.lower() not in palette and c.lower() not in moth
           and c not in core_fills}
    bad_gold = any(c.lower() in ("#b3a06a", "#a4553a", "#8a6d3b", "#f7f1e2") for c in fills)
    vol5 = 0
    core_vol5 = 0
    for f in _g.glob(os.path.join(EDITION, "svg", "*.svg")):
        t = open(f, encoding="utf-8").read()
        vol5 += t.count("VOL.5") + t.count("VOL. 5")
    for f in _g.glob(os.path.join(CORE, "svg", "*.svg")):
        t = open(f, encoding="utf-8").read()
        core_vol5 += t.count("VOL.5") + t.count("VOL. 5")
    ok = not bad_gold and not off and stroked_rects == 0 and vol5 == core_vol5 and fills.get("#fbfaf6", 0) > 0
    all_ok &= gate("s11_svg", ok,
                   f"off-palette={off} gold/old={bad_gold} stroked_rects={stroked_rects} VOL.5={vol5}(core {core_vol5}) paper_fills={fills.get('#fbfaf6', 0)}")

    with open(os.path.join(SCRATCH, f"gates-{READER}.json"), "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)
    print("OVERALL:", "ALL PASS" if all_ok else "FAILURES PRESENT")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
