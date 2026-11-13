# RUN-LOG — W47 D5 nl-family, third worker (2026-11-12)

Task: take over the nl family after the second worker (d8e28d7f) was interrupted
by a runtime restart. Verify the 7 Latin/Russian fan-outs + 3 CJK reader
editions in TOP-LEVEL production, finish whatever is unfinished, sync KITs.

## What I found on arrival (verified on disk, not taken from the handoff)
- The first worker (eef895e6) rebuilt the `fanout-nl/` COPY, not top-level
  production; its D5-REPORT SHAs describe the copy. Its fix conclusions are
  still valid as a recipe (see "Fix reuse" below).
- The second worker (d8e28d7f) discovered this and redid the work in top-level
  production, logging in `scratch-d5-redo-nl/` (RUN-LOG.md + 9 D5-REPORTs).
  On arrival, 9 of 10 editions were DONE there with all gates green and KITs
  synced; only nl-zh-tw was unfinished (Phase A + install + rebuild-1 done,
  interrupted during `render.py`, 0-byte render.log; 1 defect found in
  rebuild-1: HEAD TOO WIDE [P2-feature] `DRIE DINGEN VOOR 5 DECEMBER`).
- Production SHAs I measured on arrival matched the second worker's redo
  reports for all 9 done editions (en `d87a5242…`, de `97420549…`,
  es `2da02d5b…`, fr `08f57ec2…`, it `675f2bf3…`, pt `dc43c521…`,
  ru `8fa079cb…`, ja `67aeebb4…`, ko `fd8daad8…`).

## Fix reuse (7 Latin/Russian fan-outs — what the redo reused from the first worker)
- The redo reused the first worker's per-edition defect conclusions (box-title
  sizes + TEXTX head fixes), re-verified on the top-level rebuild, applying
  ONLY the `# D5:`-marked hunks to the top-level content files and KEEPING
  newer production drift (delta D7/D8/D10 width-scans, fix1 NOTE_RIGHT
  anchors, build-11 content8 text changes, bslib4 `w` mechanism) — see
  redo RUN-LOG.md header + `d5-hunks-top-vs-copy.txt`.
- Per edition (from the first worker's D5-REPORTs, all re-verified in the redo):
  - nl-de: 6 box-title size fixes (P1 CIJFERS 23→21, Agenda 19→17,
    IN HET KORT 24→22, P2 ZO ONTHOUD 23→22, P6 VOOR OF TEGEN 21→19,
    P7 HET WOORD 23→21) + P2 head 25→23pt + P4 sh 62→89.
  - nl-en: 6 box-title size fixes (CIJFERS 23→20, Agenda 19→18,
    IN DEZE EDITIE 24→23, ZO ONTHOUD 23→20, VOOR OF TEGEN 21→19,
    HET WOORD 23→20; the CIJFERS fix also cleared a TEXTX overlap) +
    P2 head 25→23pt + P4 sh 62→89.
  - nl-es: 5 box-title size fixes (CIJFERS 23→22, IN DEZE EDITIE 24→22,
    ZO ONTHOUD 23→21, DE GRAFIEK 24→20, HET WOORD 23→21) + P2 PAKJESAVOND
    head 28→27pt (TEXTX) + P2 head 25→23pt + P4 sh 62→89.
  - nl-fr: 6 box-title size fixes (CIJFERS 23→20 + TEXTX, ZO ONTHOUD 23→21,
    DE GRAFIEK 24→21, VOOR OF TEGEN 21→19, PAS OP 23→21, HET WOORD 23→20)
    + P2 head 25→23pt + P4 sh 62→89.
  - nl-it: 2 box-title size fixes (VOOR OF TEGEN 21→20, PAS OP 23→22) +
    P2 head 25→23pt + P4 sh 62→89. (P2 `RICORDA` 0.8px marginal, ink inside.)
  - nl-pt: 6 box-title size fixes + P2 PAKJESAVOND head 28→27pt (TEXTX) +
    P2 head 25→23pt + P4 sh 62→89.
  - nl-ru: zero D5-caused defects (Cyrillic tails route to Noto Sans, Dutch
    heads stayed inside every box); only P2 head 25→23pt + P4 sh 62→89.
- The CJK editions were fresh discoveries, not reuses: nl-ja 3 fixes
  (P2 head, P2 ZO ONTHOUD 23→21, P6 DE GRAFIEK 24→21); nl-ko 1 fix
  (P2 head only); nl-zh-tw 1 fix (P2 head only — this worker).

## nl-zh-tw — DONE (this worker, 2026-11-12)
- State on arrival: install done (svglib md5 `83c4820e…`, routing FAILURES 0),
  rebuild-1 run.py TOTAL 150 with 1 HEAD TOO WIDE (P2-feature); render.py
  killed by the restart (0-byte render.log); PDFs still pre-D5.
- Pre-fix read-only gates on the rebuild-1 SVGs (this worker): census PASS
  0/0/0; boxtitle 0 DEFECT (25 titles); creambox PASS 0 defects
  (P8 221→221, slack 53.0px); occlusion 0 flags; spill 0 SPILL; edge 0/0.
- Fix: `content12.py:175` P2 head 25 → 23pt (same line as ja/ko).
- Rebuild-2 (`scripts/redo-rebuild.sh 2026-w47-nl-zh-tw`): all gates green —
  run TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; head_check PASS 0;
  render/webpdf RC 0; p8 extract 150/150, compare CLEAN keydiff=[137, 138];
  freeze baseline 8/8 byte-identical; freeze diff vs baseline added CJK 0
  (vs core-nl added CJK 1051, TC reader text); occlusion 0; spill 0
  (55 OBSERVE); boxtitle 0 DEFECT; edge 0/0; creambox PASS 0 (P8 221→221,
  slack 53.0px); census PASS; quotes 0; text layer print = web = 44,254 B,
  word multiset diff 0, char streams equal; orphan (a) 0, (b) 0.
- Production SHAs (verified): print `90710eae78ae9ddd78f02a8a47041fbb09f322aa5adb351e214034384679e32b`
  13,888,370 B; web `1a923a7a42c6c7bdcff8805c3ae0faca314a59cb3f632a7378dd7d4c3e93c954`
  1,976,962 B; text.md unchanged `30af89dfbfe2…` 44,320 B.
- KIT synced (Files delivered + new D5 rebuild section; history preserved).
  D5-REPORT: `scratch-d5-redo-nl/D5-REPORT-nl-nl-zh-tw.md`. Freeze build-copy
  removed after verification.

## Independent verification of the 9 earlier editions (this worker)
- Re-ran the read-only gates on current top-level production (logs in
  `scratch-d5-redo-nl/verify-3rd/<slug>/`): d5_census PASS + census_quotes 0
  for all 9 (de/en/es/fr/it/pt/ru/ja/ko). Per-edition sweep results
  (background session `proc_9d4a5c8e6a7c`, RC 0, SWEEP-DONE):

  | edition | occlusion | spill (OBSERVE) | boxtitle (titles) | edge | p8 extract/compare | creambox P8 lines / slack |
  |---|---|---|---|---|---|---|
  | nl-de | 0 | 0 (38) | 0 DEFECT (21) | 0/0 | 150/150 CLEAN keydiff=[137,138] | 228→228 / 43.5px |
  | nl-en | 0 | 0 (37) | 0 DEFECT (19) | 0/0 | 150/150 CLEAN keydiff=[137,138] | 236→236 / 38.4px |
  | nl-es | 0 | 0 (39) | 0 DEFECT (19) | 0/0 | 150/150 CLEAN keydiff=[137,138] | 237→237 / 41.7px |
  | nl-fr | 0 | 0 (38) | 0 DEFECT (15) | 0/0 | 150/150 CLEAN keydiff=[137,138] | 215→215 / 37.6px |
  | nl-it | 0 | 0 (39) | 0 DEFECT (25, 1 marginal: P2 `RICORDA` 0.8px, ink inside) | 0/0 | 150/150 CLEAN keydiff=[137,138] | 228→228 / 41.7px |
  | nl-pt | 0 | 0 (39) | 0 DEFECT (21) | 0/0 | 150/150 CLEAN keydiff=[137,138] | 240→240 / 38.3px |
  | nl-ru | 0 | 0 (36) | 0 DEFECT (25) | 0/0 | 150/150 CLEAN keydiff=[137,138] | 248→248 / 39.0px |
  | nl-ja | 0 | 0 (67) | 0 DEFECT (21) | 0/0 | 150/150 CLEAN keydiff=[137,138] | 230→230 / 39.4px |
  | nl-ko | 0 | 0 (123) | 0 DEFECT (39) | 0/0 | 150/150 CLEAN keydiff=[137,138] | 229→229 / 54.0px |

  All 9 fully green; nothing needed fixing. (nl-zh-tw's own gates were run
  in its rebuild-2, same table shape: occlusion 0, spill 0 (55 OBSERVE),
  boxtitle 0 DEFECT (25), edge 0/0, p8 150/150 CLEAN keydiff=[137,138],
  creambox P8 221→221 / 53.0px.)
- Render reproducibility (re-run render.py + webpdf.py in place, logs in
  `scratch-d5-redo-nl/verify-3rd/repro/`; background session
  `proc_3408b03e22b3`, RC 0, REPRO-DONE):
  - Print PDFs: **10/10 reproduced byte-identically** — every print SHA
    unchanged (de `97420549…`, en `d87a5242…`, es `2da02d5b…`,
    fr `08f57ec2…`, it `675f2bf3…`, pt `dc43c521…`, ru `8fa079cb…`,
    ja `67aeebb4…`, ko `fd8daad8…`, zh-tw `90710eae…`).
  - Web PDFs: **10/10 got a new SHA on re-run** — webpdf.py output is NOT
    byte-reproducible (known toolchain property; KIT build-7 note already
    says "Web PDF SHA/size are not reproducible run to run — only its text
    layer is compared"). Sizes moved by −5…+8 B; pdftotext bytes identical
    per edition (de 46,657; en 45,350; es 46,704; fr 46,769; it 46,372;
    pt 46,598; ru 54,983; ja 47,834; ko 47,521; zh-tw 44,254).
  - Root cause (verified by stream-level diff of two de web builds,
    `/tmp/diff_webpdf.py`, scratch deleted after): PDF skeleton identical;
    18/126 streams differ, 70 bytes total out of 2,362,076 decompressed
    bytes, all inside embedded TTF `head`-table checksums — content,
    images and text streams identical. A third independent run produced
    yet another SHA (`bf3d78ca…` for de), confirming per-run variance.
  - `textlayer.py` re-run vs the NEW web PDFs: RC 0 for all 10, word
    multiset diff 0, de-whitespaced char streams equal, orphan (a)/(b) 0
    (logs: `verify-3rd/<slug>/textlayer-repro.log`).
- Web-SHA re-sync (this worker): the repro re-runs overwrote the production
  web PDFs, so the KITs + D5-REPORTs were re-synced to the new files with
  `verify-3rd/resync-web-sha.py` (RESYNC-OK, idempotent, assertion-checked):
  KIT "Files delivered" web SHA/size updated; D5 "New SHAs" line kept as
  history + dated repro note appended; D5-REPORT web line updated + repro
  note appended (old SHA preserved in the note). New web SHAs (current
  production truth, re-measured from disk after the sync): de
  `2361bedfd4d5…` 1,536,341 B; en `db7a9ace064a…` 1,534,348 B; es
  `249fda66604b…` 1,540,062 B; fr `1b429a3ff61e…` 1,538,511 B; it
  `81a3ffaf8e8e…` 1,534,500 B; pt `b9e2c0d5b7f2…` 1,542,946 B; ru
  `69678fdcdd00…` 1,779,868 B; ja `9a4b3dbd5dad…` 1,968,007 B; ko
  `694720afc0cc…` 1,791,910 B; zh-tw `42b892b5c065…` 1,976,958 B.
  Print + text.md SHAs unchanged everywhere. `issues/2026-w47/` is still
  empty (no nl editions inserted yet), so no issues-side copies to sync.
  Redo RUN-LOG.md appended with the same finding.

## Disk
- df on arrival: 93G used / 57G avail. Freeze build-copies removed after
  verification; no build-copy left in production or scratch.

## Status
- 10/10 nl-family editions DONE in top-level production (7 Latin/Russian +
  3 CJK) + core-nl (done by the first worker, verified by the coordinator).
  No commit, no push, no `lint.mjs --write`. Independent re-proof (§8.4) is
  the coordinator's separate step, not done here.
- Repro finding (2026-11-12): print PDFs reproduce byte-identically (10/10);
  web PDFs do NOT (per-run SHA variance, content-equivalent, text layer
  identical). KITs + D5-REPORTs re-synced to the new production web SHAs;
  final disk re-measurement confirms all 10 print/web/text SHAs as reported.
  Disk: 93G used / 57G avail — under the 100G threshold throughout.
