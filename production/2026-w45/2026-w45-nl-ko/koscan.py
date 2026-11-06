# -*- coding: utf-8 -*-
"""Korean mid-word split scan (NLxKO, W45) — rendered-SVG based.
Pairs consecutive <text> elements sharing x (±1) with 10<=dy<=45 (the
10-45 window: P8 answer lines sit at ~14.7px spacing, excluded by 15-45).
A pair is a CANDIDATE when line A ends in Hangul and line B starts in
Hangul. Each candidate is adjudicated against the build sources: if the
joined fragments occur contiguously (no space) in a Korean source string
it is a TRUE mid-word split; if they occur space-separated it is a clean
word-boundary break. Tail = Hangul syllables of B's first token.
S3 = true splits with tail >= 3. Also reports: true splits total,
orphan final lines (whole line <=1 Hangul syllable + optional trailing
punct), line-start orphan punctuation.
Usage: python koscan.py <edition-svg-dir> <build-dir>
"""
import re, sys, glob, os
HANG = re.compile(r'[\uac00-\ud7a3]')
TRAIL = ".,!?;:…»」)]}’\"'。"
def texts(path):
    txt = open(path, encoding="utf-8").read()
    els = re.findall(r'<text x="([^"]+)" y="([^"]+)"[^>]*>([^<]*)</text>', txt)
    return [(float(x), float(y), t) for x, y, t in els]
def first_token(s):
    return s.split()[0] if s.split() else ""
def last_token(s):
    return s.split()[-1] if s.split() else ""
def hang_count(s):
    return len(HANG.findall(s))
def strip_trail(s):
    while s and s[-1] in TRAIL: s = s[:-1]
    return s
def strip_lead(s):
    while s and s[0] in "([«“\"'": s = s[1:]
    return s
def main():
    svgdir, builddir = sys.argv[1], sys.argv[2]
    src = ""
    for f in glob.glob(os.path.join(builddir, "content*.py")):
        src += open(f, encoding="utf-8").read() + "\n"
    # normalize: source strings contain escaped forms? keep raw; also strip quotes not needed
    total_true = 0; s3 = 0; cands = 0; orphans = []; lead_orph = []
    for path in sorted(glob.glob(os.path.join(svgdir, "*.svg"))):
        els = texts(path)
        pg = os.path.basename(path)
        for i in range(len(els) - 1):
            x1, y1, t1 = els[i]; x2, y2, t2 = els[i + 1]
            if abs(x1 - x2) > 1: continue
            dy = y2 - y1
            if not (10 <= dy <= 45): continue
            a = strip_trail(last_token(t1)); b = strip_lead(first_token(t2))
            if not (a and b and HANG.search(a[-1]) and HANG.search(b[0])): continue
            cands += 1
            joined = a + b
            spaced = a + " " + b
            if joined in src and spaced not in src:
                tail = hang_count(b)
                total_true += 1
                if tail >= 3: s3 += 1
                print(f"SPLIT {pg} y={y1}->{y2} head={a!r}({hang_count(a)}) tail={b!r}({tail}) :: ...{t1[-18:]!r} / {t2[:18]!r}")
            elif spaced in src:
                pass
            else:
                print(f"UNRESOLVED {pg} y={y1} head={a!r} tail={b!r} :: {t1[-18:]!r} / {t2[:18]!r}")
        # orphan scans over all lines
        for x, y, t in els:
            tt = t.strip()
            if not tt: continue
            h = hang_count(tt)
            core = strip_trail(strip_lead(tt))
            if h <= 1 and HANG.search(tt) and len(tt) <= 4:
                # exclude furniture-like short lines: page labels etc. still list them
                orphans.append((pg, y, tt))
            if tt and tt[0] in "?.!,;:…»」)]" :
                lead_orph.append((pg, y, tt))
    print(f"CANDIDATES={cands} TRUE_SPLITS={total_true} S3={s3}")
    print("ORPHAN final lines (<=1 syllable):", len(orphans))
    for o in orphans: print("  ORPHAN", o)
    print("LINE-START orphan punct:", len(lead_orph))
    for o in lead_orph: print("  LEAD", o)
main()
