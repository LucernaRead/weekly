# W45 PT×RU build log

Builder: subagent (depth 2/2), 2026-10-27. Build copy made from the W45 PT
core build (`hidden_files/weekly-report-w45-pt-build/`), which was never
modified; the W43 PT×RU build and shipped edition were read-only reference.
No Discord post, no card/PDF sent to main chat, no cron created, weekly-git
untouched, core and W43 directories untouched (read-only comparison only),
no final-approval claim. This log reports builder-complete only.

## Pre-start

- No PT×RU delivery or build dir existed; no rendering process was running.
  Safe to start (60–120 s re-check rule not triggered: nothing existed).
- Core freeze baseline (tools/freeze.py): core build re-run reproduces the
  shipped core SVGs 8/8 byte-identical (p1 0dc8089d…, p2 56db3aa8…,
  p3 82f6fc3a…, p4 c5647cf6…, p5 92e86020…, p6 e6097473…, p7 a72cb75a…,
  p8 82630480…); shipped core SVGs re-hashed unchanged afterwards, and
  again at the end of the build (same 8 hashes).

## transform.py

Single source of truth for every change: OUT/BASE repoint
weekly-report-w45-pt-core → weekly-report-w45-pt-ru; bslib footer/page-line/
gloss-prefix; bridge() renamed expl() (W43 RU-column rule, 1 def + 21 calls,
asserted); type/instruction labels (instr first, then bare typ); all Chinese
explanation strings → Russian by exact-literal replacement (longest-first,
deduped) with count assertions; line-anchored replacements for the P1 serif
size, P7 box pads, quote spacing, P8 key size, disc_cn → disc_ru rename
(3 occurrences, asserted) and P7 page tags «Página N» → «Страница N»
(8, asserted, W43 RU furniture). Post-transform: zero CJK in bslib4.py +
all content*.py (asserted, no WARN skips). Reproducibility: every fix round
re-copied the pristine core build and re-ran the updated transform.py;
the final render comes from that clean re-run, not from hand patches.

## Fix rounds (sha256 baseline recorded before each re-render)

- Round 1 (first render): 150/150 exercises, levels 49/70/31, pages
  10/18/18/18/18/18/12/38, model 93 words; P8-keys FLOW OVERFLOW ×7 +
  P7 quotes colliding with the preview box (occlusion COVER/TEXTX/FOOTER/
  LINEX cascade). Print 3,436,042 B, web 3,529,209 B (superseded).
- Round 2 (in transform.py): P8 keys 13.5/1.16 → 13/1.12; P7 errs notes →
  1 line each, word gloss → 1 line, letters label → 2 lines, disclosure RU
  → 3 lines (all wrap()-verified), word-box pad 20→10, letters pad 35→25,
  quote spacing 128→104. Result: zero FLOW OVERFLOW / HEAD TOO WIDE;
  P7 col3 2056 → 1802.5; occlusion 5 NEW flags (all P1/P7, real). NOTE:
  the round-2 pre-fix baseline file (round2-baseline.sha, 18 entries) was
  lost when the build directory was reset for the clean re-run; the round-1
  outputs it recorded were superseded, and every fix lives in transform.py
  (see KIT §6). The round-3 baseline file survived and is archived.
- Round 3 (in transform.py): P1 serif 40pt → 36pt (measured 2055px →
  1849px, ink 50..1900); P1 late note → short form (321px, in box); P1 word
  para → 1-line form (399px ≤ 434); word-box pad 10→30 (EN precedent for
  the descender press); quote spacing 104→100. Result: zero FLOW OVERFLOW
  / HEAD TOO WIDE; P7 col3 1822.5; occlusion edition 0 / core 0 / NEW 0.
  Final PDFs: print 3,435,753 B SHA-256
  d95f3e647d88999ce25e58a5d7e3129098eac73621b359c4bcb1cceee2cb18c3;
  web 3,520,353 B SHA-256
  606eb5efb7b82eb67242b8a7ec9a73b559ebc5dbf8e2a158f0923c0d65d82148.

## Interpreters (both run.py and render.py)

tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1,
pypdf 6.21.2. System python3 was not used (no cairosvg).

## Gate outputs (final render)

- gates.py → gates-r3.log (rowcheck: 8 items, all byte-identical to the
  core's own design-grid items, NEW 0; right-edge ADVANCE scan 0; P6 chart
  coverage 0 at the 30% threshold; edition SVG CJK 0; banned-term
  occurrences 0 — the check pattern is stored as a unicode escape, and a
  literal-term scan of both the delivery dir and this build dir returns
  NONE)
- freeze diff → freeze-diff-final.json (added CJK 0, all pages)
- occlusion → occlusion-r3.json (edition 0, core 0, NEW 0)
- p8.py compare → p8-final.txt (CLEAN 150=150; keydiff adjudication in KIT §4)
- registry double dump → tools/scratch/regdump-core/REG.json,
  tools/scratch/regdump-ru/REG.json (page/level 0 diffs, key diffs exactly
  {137, 138, 150}, notes differ 149, unchanged exactly #86)
- SVG baselines → build-final-svg.sha (final SVGs, cards, PDFs)

## What was NOT done

No Discord post, no card/PDF sent to main chat, no cron created, weekly-git
untouched, core and W43 directories untouched (read-only comparison only),
no independent-proofread claim. This log reports builder-complete only.
