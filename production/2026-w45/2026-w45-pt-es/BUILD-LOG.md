# W45 PT×ES build log

Builder: subagent (depth 2/2), 2026-10-27. Build copy made from the W45 PT
core build (`hidden_files/weekly-report-w45-pt-build/`), which was never
modified; the W43 PT×ES edition and the W45 PT×EN sibling build were
read-only reference.

## Pre-start

- No PT×ES delivery or build dir existed; no in-progress render process
  was running. Safe to start.
- Core freeze baseline (tools/freeze.py): core build re-run reproduces the
  shipped core SVGs 8/8 byte-identical (p1 0dc8089d…, p2 56db3aa8…,
  p3 82f6fc3a…, p4 c5647cf6…, p5 92e86020…, p6 e6097473…, p7 a72cb75a…,
  p8 82630480…); shipped core SVGs re-hashed unchanged afterwards
  (same hashes at delivery).

## transform.py

Single source of truth for every change: OUT/BASE repoint
weekly-report-w45-pt-core → weekly-report-w45-pt-es (+ render.py PDF
names Lucerna-VOL2-ES); bslib furniture per shipped W43 PT×ES (footer
SEMANARIO PORTUGUÉS VOL.2, page line Página N de 8, gloss prefix
Nota —); type/instruction labels (instr first, then bare typ); all
Chinese explanation strings → Spanish by exact-literal replacement
(longest-first, deduped) with count assertions; line-anchored
replacements for the P1 edition line (38pt, measured) + badge line
(W43 verbatim, BRICK 19pt bold, strapline slot), numbers-box tsize,
P7 B2 bridge line, P8 key size, quote spacing, word-box pad.
Post-transform: zero CJK in bslib4.py + all content*.py; diff vs core
build shows every changed line either contained Chinese or is an
allowlisted furniture line (OUT path, 975/330, 975/372, disc_cn,
c.bridge, type check) — zero Portuguese content lines altered, except
the strapline slot which the badge replaces per W43 precedent.
Reproducibility: transform.py run on a pristine core-build copy
reproduces all 7 build sources byte-for-byte (verified after the
final render).

## Fix rounds (sha256 baseline recorded before each re-render)

- Round 1: 150/150, levels/pages exact, model 93 words, zero FLOW
  OVERFLOW / HEAD TOO WIDE. Occlusion: edition 9 / core 0 / NEW 9, all
  real P7 quote/preview-box overlaps (col3 ended 2027.5).
  Baseline: build-round1-baseline.sha.
- Round 2: 4 error-clinic notes shortened to one line each + word-box
  gloss to one line → col3 1880.5; quote spacing 128→104. Occlusion: 1
  flag — BOXTITLE real, word-box gloss descender pressed border 0.6px
  (1283.1 > 1282.5). Baseline: build-round2-baseline.sha.
- Round 3: word-box bottom pad 20→30 (EN precedent). Occlusion 0 /
  core 0 / NEW 0; col3 1890.5; gates FAILURES: none.
  Baseline: build-round3-baseline.sha (= final SVG/card/PDF state,
  verified: build-final-svg.sha matches).
- Round-3 PDF measurements: print 3,471,166 B SHA-256
  83fa3515fbfefd9f2b84ec31f425808e6420a250aaffbcc5fe4ed9c0088ddc06;
  web 3,494,583 B SHA-256
  892eb78d9e91e7fd5865082abe05e90e01b37108d9be1f18bb3c77e1d5d64762.

## Interpreters (both run.py and render.py)

tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1,
pypdf 6.21.2. System python3 (also 3.12.3, Pillow 10.2.0) has no cairosvg
and was not used.

## Gate outputs (final)

- gates.py → gates-final.log (FAILURES: none)
- freeze diff → freeze-diff.json (added CJK 0, all pages)
- occlusion → occlusion-edition-final.json, occlusion-new-final.json
  (edition 0, core 0, NEW 0)
- p8.py compare → CLEAN 150=150, keydiff [2, 4, 101, 137, 138, 146]
  adjudicated in the KIT (137/138 true translation redirections;
  2/4/101/146 paren-branch extraction artifacts, printed keys
  byte-identical to the core)
- SVG baselines → build-final-svg.sha

## What was NOT done

No Discord post, no card/PDF sent to main chat, no cron created,
weekly-git untouched, core and W43 directories untouched (read-only
comparison only), no independent-proofread claim. This log reports
builder-complete only.
