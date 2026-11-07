# W45 PT×EN build log

Builder: subagent (depth 2/2), 2026-10-27. Build copy made from the W45 PT
core build (`hidden_files/weekly-report-w45-pt-build/`), which was never
modified; the W43 PT×EN build was read-only reference.

## Pre-start

- No PT×EN delivery or build dir existed; only an unrelated NL×DE insert.py
  process was running. Safe to start.
- Core freeze baseline (tools/freeze.py): core build re-run reproduces the
  shipped core SVGs 8/8 byte-identical (p1 0dc8089d…, p2 56db3aa8…, p3
  82f6fc3a…, p4 c5647cf6…, p5 92e86020…, p6 e6097473…, p7 a72cb75a…,
  p8 82630480…); shipped core SVGs re-hashed unchanged afterwards.

## transform.py

Single source of truth for every change: OUT/BASE repoint
weekly-report-w45-pt-core → weekly-report-w45-pt-en; bslib footer/page-line/
gloss-prefix; type/instruction labels (instr first, then bare typ); all
Chinese explanation strings → English by exact-literal replacement
(longest-first, deduped) with count assertions; line-anchored replacements
for the P1 badge lines, P7 B2 bridge, P8 key size, numbers-box tsize,
word-box pad, quote spacing. Post-transform: zero CJK in bslib4.py + all
content*.py; diff vs core build shows every changed line either contained
Chinese or is an allowlisted furniture line (OUT path, 975/330, 975/372,
disc_cn, c.bridge(, type check) — zero Portuguese content lines altered.
Reproducibility: transform.py run on a pristine core-build copy reproduces
all 7 build sources byte-for-byte (verified after the final render).

## Fix rounds (sha256 baseline recorded before each re-render)

- Round 1: P8-keys FLOW OVERFLOW ×3 (EN notes longer; keys clamped past
  flow bottom 2552, max baseline 2565.5) + predicted P7 quotes/preview-box
  overlap. Baseline: build-round1-baseline.sha.
- Round 2: P8 key paras 13.5pt/1.16 → 13pt/1.12; P7 error-clinic notes
  shortened to one line each; P7 word-box gloss shortened. Result: zero
  FLOW OVERFLOW / HEAD TOO WIDE; P7 col3 ends 1880.5; P8 max key baseline
  2546.6. Baseline: build-round2-baseline.sha.
- Round 3: P7 quote spacing 128→108 (last translation baseline 2445.17 was
  inside the preview box 2404–2522). Result: last translation baseline
  2385.17. Baseline: build-round4-baseline.sha (round-3 baseline file was
  written into the round-4 slot by the same script; contents are the
  pre-round-4 state).
- Round 4: occlusion audit found 3 NEW flags (edition 3, core 0), all real
  defects in the EN apparatus: (a) P1 word-of-week gloss second line struck
  by the row-B rule → gloss shortened to one line ("a holiday plus the
  weekend", 422.0px at sans 19 in 434px width); (b) P1 numbers-box title ink
  right 997.0 > box border 961.0 → tsize=20 on that box only (W43
  precedent; 20pt bold title = 393.0px); (c) P7 word-box gloss ink bottom
  1283.6 > box border 1282.5 (1.1px descender press) → word-box bottom pad
  20→30, plus quote spacing 108→104. A patch script crashed on a malformed
  regex before saving, so the render that followed merely reproduced round
  3 (still 3 flags); the fix was rewritten as plain-string replacement in
  transform.py. Baseline: build-round5-baseline.sha.
- Round 5 (fresh transform): zero FLOW OVERFLOW / HEAD TOO WIDE; P7 col3
  ends 1890.5; 150/150 exercises; all gates pass (see gates-final.log,
  occlusion-edition-final.json, occlusion-new-final.json, freeze-diff.json).
  Round-5 PDF measurements: print 3,471,730 B SHA-256
  2ca66f42c0eb1892cc112cde30b5857a5c9aa07813c198c2648fa13907e736d7; web
  3,425,358 B SHA-256 f4f26f8ef049acd4bf868d8ba0447fb2c0272154a73fb37387ab535d4791293b.
- Round 6 (apostrophes): visual inspection found U+2019 rendering with a
  visible gap in the CJK font ("week' s", "Editor' s", "SUNDAY' S") while
  W43 PT×EN uses ASCII apostrophes throughout. All 5 occurrences (P2
  SUNDAY'S, P7 week's + Editor's ×2, P8 exam's) switched to ASCII in
  transform.py, the build sources and gates.py. Baseline:
  build-round6-baseline.sha. Result: zero FLOW OVERFLOW / HEAD TOO WIDE;
  gates re-run FAILURES: none; occlusion re-run 0 flags; U+2019 count 0 on
  all 8 pages; affected cards (P2 band title, P7 bridges, P7 corner)
  re-inspected visually — apostrophes now tight.
  Final PDFs: print 3,471,726 B SHA-256
  b0d063255527208917a9c0248781a13bb9926f3e0a8bfb001505fc4e4fdef7c7; web
  3,425,058 B SHA-256
  04aec5b5aca654f39d3ded6778085a80c94f8696d0e434a00e277fe1276bcda8.

## Interpreters (both run.py and render.py)

tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1,
pypdf 6.21.2. System python3 (also 3.12.3) has no cairosvg and was not used.

## Gate outputs (final)

- gates.py → gates-final.log (round 5) + re-run after round 6 (FAILURES: none)
- freeze diff → freeze-diff.json
- occlusion → occlusion-edition-final.json, occlusion-new-final.json
  (round 5; round-6 re-run: edition 0 flags, core 0 flags, NEW 0)
- p8.py compare → CLEAN (see KIT for keydiff adjudication)
- SVG baselines → build-final-svg.sha (round-6 final SVGs)

## What was NOT done

No Discord post, no card/PDF sent to main chat, no cron created, weekly-git
untouched, core and W43 directories untouched (read-only comparison only),
no independent-proofread claim. This log reports builder-complete only.
