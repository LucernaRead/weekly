#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 3 independent change isolation.
(a) Hash diff: current sha256 of every delivered file vs the fix worker's
    pre-fix inventory.log (same relative paths, per edition section).
(b) SVG-text multiset diff: current <text> node multisets vs the pre-fix
    svg-text snapshot, per edition/page (own implementation).
(c) .text.md diff: current exports vs pre-fix textmd-backup (unified diff)."""
import os, glob, hashlib, difflib, json
from collections import Counter
from xml.etree import ElementTree as ET
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
R3 = os.path.join(GOAL, "hidden_files", "w46", "ko-proofread-gates-round3")
PRE = os.path.join(GOAL, "hidden_files", "w46", "ko-fix-round3", "pre-fix")
NS = "{http://www.w3.org/2000/svg}"
EDITIONS = {"zh-cn": "weekly-report-w46-ko-core", "de": "weekly-report-w46-ko-de",
            "en": "weekly-report-w46-ko-en", "es": "weekly-report-w46-ko-es",
            "fr": "weekly-report-w46-ko-fr", "it": "weekly-report-w46-ko-it",
            "ja": "weekly-report-w46-ko-ja", "nl": "weekly-report-w46-ko-nl",
            "pt": "weekly-report-w46-ko-pt", "ru": "weekly-report-w46-ko-ru",
            "zh-tw": "weekly-report-w46-ko-zh-tw"}
FILES = ["cards/p1-pyoji.png","cards/p2-saenghwal.png","cards/p3-munhwa.png",
         "cards/p4-seupocheu.png","cards/p5-cheongnyeon.png","cards/p6-gipi.png",
         "cards/p7-mal.png","cards/p8-siheom.png",
         "svg/p1-pyoji.svg","svg/p2-saenghwal.svg","svg/p3-munhwa.svg",
         "svg/p4-seupocheu.svg","svg/p5-cheongnyeon.svg","svg/p6-gipi.svg",
         "svg/p7-mal.svg","svg/p8-siheom.svg"]

# --- (a) parse pre-fix inventory: sections "== <code> ==" then "hash  relpath" ---
pre = {}
cur_code = None
for line in open(os.path.join(PRE, "inventory.log"), encoding="utf-8"):
    line = line.rstrip("\n")
    if line.startswith("== ") and line.endswith(" =="):
        cur_code = line[3:-3].strip()
        pre[cur_code] = {}
    elif cur_code and len(line) > 66:
        parts = line.split(None, 1)
        if len(parts) == 2:
            pre[cur_code][parts[1].strip()] = parts[0]
print("pre-fix inventory sections:", {k: len(v) for k, v in pre.items()})
hashdiff = {}
for code, d in EDITIONS.items():
    edir = os.path.join(GOAL, "files", d)
    changed = []
    for rel in FILES:
        h = hashlib.sha256(open(os.path.join(edir, rel), "rb").read()).hexdigest()
        if pre.get("core" if code=="zh-cn" else code, {}).get(rel) != h:
            changed.append(rel)
    # PDFs + text.md: find actual filenames
    for pat in ["*.pdf", "*.text.md"]:
        for f in sorted(glob.glob(os.path.join(edir, pat))):
            rel = os.path.basename(f)
            h = hashlib.sha256(open(f, "rb").read()).hexdigest()
            if pre.get("core" if code=="zh-cn" else code, {}).get(rel) != h:
                changed.append(rel)
    hashdiff[code] = changed
    print(code, "changed files:", len(changed), changed)

# --- (b) multiset diff ---
def load_dir(dd):
    out = {}
    for f in sorted(glob.glob(os.path.join(dd, "*.txt"))):
        lines = open(f, encoding="utf-8").read().split("\n")
        if lines and lines[-1] == "":
            lines.pop()
        out[os.path.basename(f)] = Counter(lines)
    return out

def current(code):
    edir = os.path.join(GOAL, "files", EDITIONS[code])
    out = {}
    for path in sorted(glob.glob(os.path.join(edir, "svg", "*.svg"))):
        root = ET.parse(path).getroot()
        lines = ["".join(t.itertext()) for t in root.iter(NS + "text")]
        out[os.path.splitext(os.path.basename(path))[0] + ".txt"] = Counter(lines)
    return out

msdiff = {}
tot_a = tot_r = 0
for code in EDITIONS:
    pre_c = load_dir(os.path.join(PRE, "svg-text", code))
    post_c = current(code)
    pages = {}
    for page in sorted(set(pre_c) | set(post_c)):
        a, b = pre_c.get(page, Counter()), post_c.get(page, Counter())
        added, removed = b - a, a - b
        if added or removed:
            pages[page] = {"added": dict(added), "removed": dict(removed)}
            tot_a += sum(added.values()); tot_r += sum(removed.values())
            print(code, page, f"+{sum(added.values())} -{sum(removed.values())}")
            for s, n in removed.items(): print("   REMOVED x%d: %r" % (n, s))
            for s, n in added.items(): print("   ADDED   x%d: %r" % (n, s))
        else:
            print(code, page, "identical", sum(a.values()), "nodes")
    msdiff[code] = pages
print("MULTISET TOTAL: +%d -%d" % (tot_a, tot_r))

# --- (c) text.md diffs ---
tmdiff = {}
for code, d in EDITIONS.items():
    pre_files = glob.glob(os.path.join(PRE, "textmd-backup", "*.text.md"))
    # match by edition code suffix
    cand = [f for f in pre_files if f.endswith(f"-{code}.text.md")]
    cur_files = glob.glob(os.path.join(GOAL, "files", d, "*.text.md"))
    assert len(cand) == 1 and len(cur_files) == 1, (code, cand, cur_files)
    a = open(cand[0], encoding="utf-8").read().splitlines()
    b = open(cur_files[0], encoding="utf-8").read().splitlines()
    diff = list(difflib.unified_diff(a, b, lineterm=""))
    tmdiff[code] = diff
    print(code, "text.md diff lines:", len(diff))
    for ln in diff: print("   ", ln)

json.dump({"hashdiff": hashdiff, "multiset": msdiff},
          open(os.path.join(R3, "change-isolation.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
open(os.path.join(R3, "textmd-diffs.txt"), "w", encoding="utf-8").write(
    "\n".join(f"== {c} ==\n" + "\n".join(d) for c, d in tmdiff.items()))
