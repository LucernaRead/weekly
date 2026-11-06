#!/usr/bin/env python3
"""W46 reconciliation: one consistent method per edition.
Complete = slug-named non-empty <slug>.text.md + exactly one *-web.pdf with a
real text layer (pdftotext bytes > 0) + valid single-line ABSTRACT.txt.
Canonical dir: per-edition dir if present, else the -core dir
(zh-cn-en -> zh-cn-core, zh-tw-en -> zhtw-core, ru-zh-cn -> ru-core).
Usage: python3 reconcile.py [target ...]  (no args = all 12 targets)
"""
import os, subprocess, glob, sys
F = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
TARGETS = sys.argv[1:] or ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "zh-cn", "zh-tw", "ja", "ko"]
ALL = ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "zh-cn", "zh-tw", "ja", "ko"]

def natives(t):
    return [n for n in ALL if n != t and not (t == "zh-cn" and n == "zh-tw") and not (t == "zh-tw" and n == "zh-cn")]

def cand_dirs(t, n):
    c = [f"weekly-report-w46-{t}-{n}", f"weekly-report-w46-{t}-core"]
    if t == "zh-tw" and n == "en":
        c.insert(0, "weekly-report-w46-zhtw-core")
    return c

rows = []
for t in TARGETS:
    for n in natives(t):
        slug = f"2026-w46-{t}-{n}"
        found = None
        for c in cand_dirs(t, n):
            d = os.path.join(F, c)
            if os.path.isdir(d):
                found = d
                break
        if not found:
            rows.append((slug, "NO-DIR", "MISSING", 0, 0, "MISSING|MISSING"))
            continue
        tm = os.path.join(found, slug + ".text.md")
        if os.path.exists(tm) and os.path.getsize(tm) > 0:
            tm_disp, tm_ok = "ok", True
        else:
            alts = glob.glob(os.path.join(found, "*.text.md"))
            tm_disp = "ALT:" + ",".join(os.path.basename(a) for a in alts) if alts else "MISSING"
            tm_ok = False
        webs = [f for f in os.listdir(found) if f.lower().endswith(".pdf") and ("web" in f.lower() or "网页版" in f)]
        web = webs[0] if len(webs) == 1 else ("MULTI:" + ",".join(webs) if webs else "MISSING")
        tb = 0
        wsize = 0
        if len(webs) == 1:
            wp = os.path.join(found, webs[0])
            wsize = os.path.getsize(wp)
            try:
                out = subprocess.run(["pdftotext", wp, "-"], capture_output=True, timeout=120)
                tb = len(out.stdout)
            except Exception:
                tb = -1
        ab = os.path.join(found, "ABSTRACT.txt")
        if os.path.exists(ab):
            a = open(ab, encoding="utf-8").read()
            ab_ok = "ok" if (a.strip() and "\n" not in a.strip() and '"' not in a) else "BAD"
        else:
            ab_ok = "MISSING"
        rows.append((slug, os.path.basename(found), tm_disp, wsize, tb, f"{web}|{ab_ok}"))

complete = [r for r in rows if r[2] == "ok" and r[4] and r[4] > 0 and r[5].endswith("|ok")]
print(f"TOTAL {len(rows)} COMPLETE {len(complete)}")
for r in rows:
    if r not in complete:
        print("INCOMPLETE:", r)
for t in TARGETS:
    c = sum(1 for r in complete if r[0].startswith(f"2026-w46-{t}-"))
    print(t, f"{c}/{len(natives(t))}")
