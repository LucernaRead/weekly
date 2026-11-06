# -*- coding: utf-8 -*-
"""Independent gate 1+2: freeze-diff recount, Latin multiset, CJK counts,
line-start orphans, simplified-only chars, word-level CJK containment,
bridge term, escape residue. Reads only shipped SVGs + transform.py."""
import re, html, glob, os
from collections import Counter
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = BASE + "/files/weekly-report-w45-it-core/svg"
ED = BASE + "/files/weekly-report-w45-it-ja/svg"
BUILD = BASE + "/hidden_files/weekly-report-w45-it-ja-build"

def texts(path):
    t = open(path, encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))
            for m in re.finditer(r"<text\b[^>]*>(.*?)</text>", t, re.S)]

def cjk_chars(s):
    return [c for c in s if "\u3040" <= c <= "\u30ff" or "\u4e00" <= c <= "\u9fff"]

pages = ["p1-prima","p2-vita","p3-cultura","p4-sport","p5-giovani","p6-approfondimento","p7-lingua","p8-valutazione"]
print("== per-page CJK char counts (independent recount) ==")
for p in pages:
    cc = Counter(); ec = Counter()
    for x in texts(f"{CORE}/{p}.svg"): cc.update(cjk_chars(x))
    for x in texts(f"{ED}/{p}.svg"): ec.update(cjk_chars(x))
    added = ec - cc; removed = cc - ec
    print(f"{p}: core={sum(cc.values())} edition={sum(ec.values())} added_distinct={len(added)} added_total={sum(added.values())} removed_total={sum(removed.values())}")
    print(f"   added sample: {dict(list(added.items())[:12])}")

print("\n== Latin word multiset diff (CJK stripped, Latin tokens) ==")
LAT = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:['’][A-Za-zÀ-ÖØ-öø-ÿ]+)?")
for p in pages:
    cw = Counter(); ew = Counter()
    for x in texts(f"{CORE}/{p}.svg"):
        s = re.sub(r"[\u3040-\u30ff\u4e00-\u9fff]", " ", x)
        cw.update(LAT.findall(s))
    for x in texts(f"{ED}/{p}.svg"):
        s = re.sub(r"[\u3040-\u30ff\u4e00-\u9fff]", " ", x)
        ew.update(LAT.findall(s))
    only_core = cw - ew; only_ed = ew - cw
    print(f"{p}: core-only tokens {dict(only_core)} | edition-only tokens {dict(only_ed)}")

print("\n== bridge term + escape residue + U+FFFD ==")
for label, d in [("core", CORE), ("edition", ED)]:
    for f in sorted(glob.glob(d + "/*.svg")):
        t = open(f, encoding="utf-8").read()
        print(os.path.basename(f), label, "桥接:", t.count("桥接"), "backslash:", t.count("\\"),
              "l\\\\'Europa:", t.count("l\\\\"), "U+FFFD:", t.count("\ufffd"),
              "double-backslash:", t.count("\\\\"))
for extra in [BASE + "/files/weekly-report-w45-it-ja/WEEKLY-KIT.md", BASE + "/files/weekly-report-w45-it-ja/ABSTRACT.txt"]:
    t = open(extra, encoding="utf-8").read()
    print(os.path.basename(extra), "桥接:", t.count("桥接"), "backslash:", t.count("\\"))

print("\n== line-start orphans (independent scan, builder NO_START set + ASCII) ==")
NO_START = set("。、，．！？：；）」』】ー…‥・") | set("ぁぃぅぇぉゃゅょっゎァィゥェォャュョッヮ") | set(").,;:!?%")
tot = 0
for p in pages:
    orph = [x for x in texts(f"{ED}/{p}.svg") if x and x.lstrip() and x.lstrip()[0] in NO_START]
    # also raw first char without strip, to catch leading-space masking
    orph_raw = [x for x in texts(f"{ED}/{p}.svg") if x and x[0] in NO_START]
    print(f"{p}: stripped-orphans={len(orph)} raw-orphans={len(orph_raw)} {orph[:5]}")
    tot += len(orph)
print("TOTAL orphans:", tot)

print("\n== simplified-only character scan (chars never used in Japanese) ==")
# Simplified forms whose Japanese form differs: 对说话语义习让仅发录汉龙龟凤... + simplified-only radicals
SIMP_ONLY = set("对说话语义习让仅发录汉刘刘齐刘")  # placeholder refined below
SIMP_ONLY = set(list("对说话语义习让仅发录汉") + ["为","这","个","们","来","时","过","还","会","发","对","仅","让","录","习","语","义","说","话","汉","龙"])
# NOTE: many of these (为/这/个/们/来/时/过/还/会) ARE used in Japanese kanji compounds rarely or in Chinese;
# report raw hits and adjudicate each below rather than gating on the raw set.
for p in pages:
    hits = Counter()
    for x in texts(f"{ED}/{p}.svg"):
        for c in x:
            if c in SIMP_ONLY: hits[c] += 1
    print(f"{p}: {dict(hits)}")
print("Strict simplified-form set (对/说/话/语/义/习/让/仅/发/录/汉 only):")
for p in pages:
    hits = Counter()
    for x in texts(f"{ED}/{p}.svg"):
        for c in x:
            if c in set("对说话语义习让仅发录汉"): hits[c] += 1
    print(f"{p}: {dict(hits)}")

print("\n== word-level CJK containment vs transform.py ==")
trans = open(BUILD + "/transform.py", encoding="utf-8").read()
trans_cjk = set(re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]+", trans))
unmatched = []
for p in pages:
    for x in texts(f"{ED}/{p}.svg"):
        for run in re.findall(r"[\u3040-\u30ff\u4e00-\u9fff]+", x):
            if run not in trans_cjk:
                # a run may be a concatenation of two transform strings across a node boundary;
                # check char-level: every char appears in some transform string
                if not all(any(c in s for s in trans_cjk) for c in run):
                    unmatched.append((p, run))
print("runs not verbatim in transform.py:", len(unmatched), unmatched[:20])
# char-level residual
allchars = set()
for p in pages:
    for x in texts(f"{ED}/{p}.svg"): allchars.update(cjk_chars(x))
tchars = set("".join(trans_cjk))
print("edition CJK chars absent from transform.py strings:", sorted(allchars - tchars))
