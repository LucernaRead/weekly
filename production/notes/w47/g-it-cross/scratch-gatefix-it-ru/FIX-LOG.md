# FIX-LOG — W47 boxtitle gate fix: 2026-w47-it-ru P2 «ЗАПОМНИТЕ»

Scope: the last of the 21 defects in the 130-wide pre-insert run
(`Reports-preinsert/new-gates-130.md`, 2026-11-12 01:54 UTC,
`tools/boxtitle_check.py`, commit 45ca73fc). Only `2026-w47-it-ru` touched.
No commit / push / lint. No text-content change — layout-only fix.

## §0 Before-state (verified on disk — CORRECTS the task brief)

The brief said the R2R3 sync had landed it-ru's `_run_w` rebuilt PDFs in
production with print `12f897b2…` / web `6fce91e4…`. **That is wrong on
both counts, verified on disk:**

- Print `12f897b2f27cbc8e50c08c497c36e41c72f894be6403a63654c498eea69e07db`
  and web `6fce91e40ee95c736ed07ef71e838147318591be2d09c7696195f64bb7a42cd1`
  are **2026-w47-ru-it** SHAs (R2R3 `SYNC-LOG.md` §1a + `scratch-ru-rerun-R2/
  ru-it/after-sha.txt`), a different edition. it-ru was never part of R2
  (ru family, target=ru); it-ru is target=it, native=ru.
- Production it-ru at fix start was still the **spacing2 build**:
  - Print: `La-Lucerna-VOL4-RU.pdf`, 14,179,828 B, sha256
    `7e9a384300a6e77625fecddd3b225f313d8d040e5bb29c91fa9612a6ec7db931`
    (matches KIT §14)
  - Web: `La-Lucerna-VOL4-RU-web.pdf`, 1,440,147 B, sha256
    `04705169efdd9ef61fb0c15c0417956c8cbe215faaa9d1cc642c6d67107b615d`
    — **differs from the KIT §14 record** (`3ac0fa44…`, 1,440,142 B) by 5
    font-subset bytes: the production web PDF (mtime Nov 12 00:01 UTC) was
    regenerated after the §14 KIT update, same non-determinism class §14
    itself documents. Verified text-identical to the KIT-recorded build
    (53,087 chars / 6,112 words, same as the rebuilt web PDF).
  - Text: `2026-w47-it-ru.text.md`, 67,731 B, sha256
    `47c0471515d3b249855e33a290d0c4259ecce431995db45ac0ce926cf5a52b1d`
- Full production snapshot before the fix: `before-sha.txt` (41 files).
- `svglib.py` md5 at fix start: `ee3211298f274e02ade2d4ca318ce354`
  (pre-port). By build time the concurrent Hangul-fix port had landed:
  `27f11789af7c828e47ca14eb00c1dded` (post-port) — **both builds below were
  built against the post-port svglib**. The port sweeps 0/3,893 differing
  runs for it-ru, and the 7 unchanged pages came out byte-identical
  SVG+card vs production, confirming 0 output change from the port.
- Disk at start: 99G used (below the 100G stop line); 99G at end.

## §1 Defect — reproduced

- Gate report: P2 TITLE `ЗАПОМНИТЕ`, fs 23, ink 873.5→1024.5, box
  [538.5, 1273.5, 422.5, 210.9] (right edge 961.0), **over +63.5 px**,
  core −18.0, backup +62.1 (98% inherited, +1.4 regression).
- Re-ran `tools/boxtitle_check.py` on production: reproduced exactly
  (+63.5, exit 1). `before/2026-w47-it-ru.json`.
- Visual: `crop-p2-frase-BEFORE.png` — the final «ТЕ» of ЗАПОМНИТЕ sits
  on white paper past the cream box's right edge.
- Cause: the box title is one line of two runs —
  `LA FRASE PER RICORDARE　` (Italian, «Noto Sans CJK SC») +
  `ЗАПОМНИТЕ` (Russian, «Noto Sans») at 23 pt bold. The Italian part
  alone is 317.0 px of advance; the Russian gloss adds 151 px. Core-it's
  title (`LA FRASE PER RICORDARE　口诀`) fits at −18.0. Same structural
  pattern as it-es/it-ja/it-ko (OBSERVE there, same as backup); it-ru is
  a DEFECT only because of the +1.4 regression vs backup.

## §2 Fix choice — measured, minimal

Box width cannot grow (column width CW=422.5, grid fixed) and a line
break has no vertical room in the P2 flow. `bslib4.py:174`
`box(..., tsize=23, ...)` takes a per-call title size, so: **one keyword
argument at one call site**.

- `content12.py:177`:
  `f.box("LA FRASE PER RICORDARE　ЗАПОМНИТЕ", [...], tsize=19.5)`
  (default 23). Comment added on the line. No text changed.
- Candidates measured with the gate's own PIL true-ink math
  (`measure_candidates.py`, two-run composition with the real SVG
  families; validated against the gate: fs 23 reproduces to 1.4 px —
  the known layout-vs-PIL advance delta):

  | tsize | predicted margin |
  |---|---|
  | 20   | −0.9 px (touching — rejected) |
  | **19.5** | **+9.0 px predicted** |
  | 19   | +19.9 px |
  | 18.5 | +29.7 px |

  Smallest half-point step leaving ≥5 px margin (de-en gatefix rule) →
  **19.5**. Box height shrinks 3.5 px (tsize+10 line); gloss and flow
  below shift up 3.5 px, no reflow elsewhere.
- Measured on the built SVG: Russian run ink 825.3→953.3, margin
  **+7.7 px** inside the box (prediction 9.0 − 1.4 layout delta).

## §3 Rebuild (scratch only)

- `tools/run_build.py --build production/2026-w47/2026-w47-it-ru
  --out <scratch>/build1 --steps run,render`: rc=0, TOTAL 150,
  0 FLOW OVERFLOW / 0 HEAD TOO WIDE, production unchanged (41 files
  re-hashed). `run_build1.log`.
- `tools/webpdf.py` on build1 svg: rc=0, 1,440,177 B, 53,087 text bytes.
  `webpdf1.log`.
- build2 (independent rebuild for the freeze check): rc=0, TOTAL 150,
  production unchanged. `run_build2.log`.
- Serial; memory gate observed (waited while available <1500 MB before
  build1: 1414→1557 MB; build2 started at 1717 MB).
- `text.md` byte-identical in build1 (sha256 `47c04715…`, `cmp` clean).

## §4 Gates on the rebuilt edition

| Gate | Result |
|---|---|
| boxtitle (build-copy) | **0 DEFECT, 0 OBSERVE, 0 marginal**, exit 0 (37 titles, 492 body lines; the title counts as body lines now only because the gate's TITLE class needs ≥22 pt) — `boxtitle-after.log`, `after/build-copy.json` |
| run.py TOTAL | 150 (build1 + build2) |
| p8 extract | 150/150 |
| p8 compare vs core-it | CLEAN, missing=[] extra_count=0, keydiff=[137, 138, 139] (expected) |
| occlusion | 0 flags, selftest OK |
| text layer print vs web | per-page byte-identical, 35,582 non-ws chars each — TEXTLAYER PASS |
| freeze.py diff vs core | rc=0; counts byte-identical to the BEFORE run (added CJK 8 = U+3000 ×8; added Latin 223 — a pre-existing fan-out property, unchanged by this fix) — `gates/freeze-diff.log`, `gates/freeze-diff-BEFORE.log` |
| frozen_check (core ∩ before vs core ∩ after) | **PASS 8/8 identical** |
| freeze build1 vs build2 | **8/8 SVGs + print PDF byte-identical** (print `5281accd…` both builds) |
| census print + web (R2 census.py) | 15 distinct join tokens / 34 boundaries; rows **byte-identical to the production BEFORE run** — 0 new joins, 0 real joins (all 15 are pre-existing en-dash/quote/arrow/checkmark run-boundaries, e.g. `Atalanta–Inter.`, `≠LEGGE`, `→prega`, `✓Образец`; none a fused word pair) |
| gaps (R2 gap_rude.py) print + web | BEFORE == AFTER except file-path header lines; all fixed-join/byline/arrow probe lists empty |

- Visual AFTER: `crop-p2-frase-AFTER.png` — the whole title sits inside
  the cream box with clear margin.
- Only p2 changed: build1 vs production — `SVG DIFF p2-vita.svg` only,
  `CARD DIFF p2-vita.png` only; the other 7 SVGs + 7 cards byte-identical.
- Tool notes (pre-existing, NOT this fix): the shared
  `frozen_check.py` and `scratch-ru-rerun-R2/checks.py freeze()` hardcode
  de/ru page names (`p1-front`, `p1-pervaya`), so they fail with
  FileNotFoundError on it pages — re-ran with it-family variants
  (`frozen_check_it.py`, `freeze_b1b2_it.py`, same math, Italian page
  names) in this scratch dir; the shared tools were not modified.
  `check_core.py` is ru-family-only (no such script in it-ru); its
  coverage for it-ru is the gate list above.

## §5 Sync (2026-11-12 ~02:43 UTC)

Copied from build1 into production: `svg/*.svg` (8) +
`cards/p2-vita.png` + print PDF + web PDF. SHA-256 verified **11/11
identical** after copy (`after-sync-sha.txt` vs `build-sha.txt`).
Production re-hash vs `before-sha.txt`: only the 4 synced files differ
(p2 svg, p2 card, 2 PDFs); `content12.py` was already in the snapshot;
KIT was then edited (below); `svglib.py` still `27f11789…`.

- Print: `La-Lucerna-VOL4-RU.pdf` — 14,179,824 bytes, sha256
  `5281accd9cf3a9e44f009a92a088fdcc415ad82138216d8a39b9ed25554ad3b7`
  (was 14,179,828 B, `7e9a3843…`)
- Web: `La-Lucerna-VOL4-RU-web.pdf` — 1,440,177 bytes (< 7 MB),
  53,087 text bytes, sha256
  `b8679dceb6bf91072ea2190147893eb30eda26e3bc708e37aa3aed3d0861b87d`
  (was 1,440,147 B, `04705169…`)
- Text: `2026-w47-it-ru.text.md` — 67,731 bytes, sha256
  `47c0471515d3b249855e33a290d0c4259ecce431995db45ac0ce926cf5a52b1d` —
  UNCHANGED.
- KIT: new §15 appended (defect, fix, gates, deliverables superseding
  §14; also records the brief's SHA mix-up and the pre-existing §14 web
  staleness). The task's "KIT §5+§7" maps to this KIT's §7 deliverables,
  superseded per the it-ru KIT's own convention by the new §15 section.

## §6 Final confirmation (production files)

`tools/boxtitle_check.py production/2026-w47/2026-w47-it-ru`:
**0 DEFECT, 0 OBSERVE, 0 marginal, exit 0** (`final/2026-w47-it-ru.json`).
Production SHAs re-verified: print `5281accd…`, web `b8679dce…`,
text.md `47c04715…` (unchanged).

## §7 Files in this scratch dir

- `FIX-LOG.md` (this file), `measure_candidates.py`, `driver-gates.sh`,
  `frozen_check.py` (de-en copy) + `frozen_check_it.py` (it variant),
  `freeze_b1b2_it.py`, `before-sha.txt`, `after-sha.txt`,
  `after-sync-sha.txt`, `build-sha.txt`, `text-before.sha256`,
  `run_build1.log`, `run-build1.log`, `run_build2.log`, `webpdf1.log`,
  `gates1.log`, `boxtitle-after.log`,
  `crop-p2-frase-BEFORE.png`, `crop-p2-frase-AFTER.png`,
  `before/` (gate JSON on production before the fix),
  `after/` (gate JSON on build-copy), `final/` (gate JSON on production
  after sync), `gates/` (p8, occlusion, freeze-diff ± BEFORE,
  frozen_check_it, freeze_b1b2, textlayer, census ±, gaps ±),
  `before-svg/` (production SVGs before sync),
  `census-{BEFORE,AFTER}-{print,web}.json/.txt`,
  `gaps-{BEFORE,AFTER}.txt`, `gaps-{BEFORE,AFTER}-web.txt`,
  `crops/` (gap_rude crops), `build1/` + `build2/` (full scratch builds).
