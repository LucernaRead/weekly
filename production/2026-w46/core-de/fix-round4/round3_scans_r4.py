#!/usr/bin/env python3
"""Round 3 independent scans (proofreader's own): kinsoku line-start/line-end,
lone-punctuation elements, S1 token-split signature, and a positional
mid-word-split scan over consecutive same-column lines. Read-only."""
import re, html, pathlib, json, sys
BASE = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/w46/de-fix-round4/scratch/build-strict/svg"
PAGES = ["p1-front.svg","p2-leben.svg","p3-kultur.svg","p4-sport.svg","p5-jugend.svg","p6-vertiefung.svg","p7-sprache.svg","p8-uebungen.svg"]
NO_START = set("。、，．！？：；）」』】}),.:;!?")  # must not START a line (incl ASCII punct per fix report)
NO_END = set("（(［｛〈《「『")  # must not END a line
def elements(pg):
    s = (BASE/pg).read_text(encoding="utf-8")
    out=[]
    for m in re.finditer(r'<text[^>]*x="([^"]+)" y="([^"]+)"[^>]*>(.*?)</text>', s, re.S):
        out.append((float(m.group(1)), float(m.group(2)), html.unescape(re.sub(r"<[^>]+>","",m.group(3))).strip()))
    return out
log=[]
hits_start=hits_end=lone=0
for pg in PAGES:
    for x,y,t in elements(pg):
        if t and t[0] in NO_START:
            hits_start+=1; log.append(f"START-HIT {pg} x={x} y={y} :: {t[:60]!r}")
        if t and t[-1] in NO_END:
            hits_end+=1; log.append(f"END-HIT {pg} x={x} y={y} :: {t[:60]!r}")
        if t in ("。","）",".","，","、","！","？","）",")"):
            lone+=1; log.append(f"LONE-PUNCT {pg} x={x} y={y} :: {t!r}")
print(f"kinsoku: line-start hits={hits_start} line-end hits={hits_end} lone-punct elements={lone}")
# S1 signature: line starting with 1-2 lowercase letters + capital (Round 2 signature)
s1=[]
for pg in PAGES:
    for x,y,t in elements(pg):
        if re.match(r"^[a-z]{1,2}[A-Z]", t):
            s1.append((pg,x,y,t[:70]))
print(f"S1-signature lines: {len(s1)}")
for r in s1: print("  S1", r)
# Positional mid-word-split scan: consecutive lines, same x, dy in [15,23]:
# flag if prev line ends with a lowercase letter AND next line starts with
# lowercase letters that together with the tail would form a longer word,
# UNLESS the break is at a space/token boundary evidenced by the joined
# stream containing the whole word. We check against the German word stock
# from the P8 key stream + all SVG text: a split is SUSPECT if
# (tail+head) with no space is a word occurring elsewhere whole, while
# tail and head alone are not words. Manual review of every suspect below.
# Simpler decisive check for the P8 keys block: every line's text, when
# joined with single spaces in paint order per column, must contain the
# extracted keys verbatim (p8.py already proves key identity); here we
# additionally list ALL line pairs where prev ends [a-z] and next starts
# [a-z] (potential fragment joins) for review.
pairs=[]
for pg in PAGES:
    els=elements(pg)
    for a,b in zip(els, els[1:]):
        if a[0]==b[0] and 15<=b[1]-a[1]<=23 and a[2] and b[2]:
            if re.search(r"[a-zA-ZäöüÄÖÜß]$", a[2]) and re.match(r"^[a-zäöü]", b[2]):
                pairs.append((pg,a[1],b[1],a[2][-40:],b[2][:40]))
print(f"lowercase-fragment line pairs (all pages): {len(pairs)}")
for r in pairs: print("  PAIR", r)
# 76. check + repaired tokens present as whole tokens on one line
p8txt=" ".join(t for _,_,t in elements("p8-uebungen.svg"))
for tok in ["76. Die Kinder freuen sich, weil St. Martin kommt.", "begonnen）", "beginnt.（beginnt置尾）", "das NFL-Spiel.", "· 16.", "· 24.", "· 129."]:
    print(f"token-present {tok!r}: {tok in p8txt}")
for bad in ["begonne\n", "sNFL", "beginn\nt", "da\nsNFL"]:
    print(f"bad-fragment {bad!r} in p8 stream: {bad in p8txt}")
print("---")
for l in log: print(l)
