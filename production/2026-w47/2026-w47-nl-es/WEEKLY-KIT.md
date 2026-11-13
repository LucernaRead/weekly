# WEEKLY-KIT — 2026-W47 · nl → es (Spanish readers)

Dutch weekly newspaper for Spanish readers. Target language Dutch (nl), reader
native language Spanish (es). VOL.4, issue 2026-11-16 – 2026-11-22. Target: 150
exercises (10/18/18/18/18/18/12/38 across pages 1–8); A2 46 / B1 73 / B2 31;
model essay 81 words.

## Source

Fan-out of the frozen Dutch core `production/2026-w47/core-nl/` (slug
`2026-w47-nl-zh-cn`). Dutch target text, facts, and answer keys are frozen; only
the explanation layer (glosses, notes, section subtitles, exercise type words)
was rewritten in Spanish. No new trend research, no invented reader letters.

## Files delivered

- 8 SVGs (`svg/p1-voorpagina.svg` … `svg/p8-toets.svg`), 8 render cards (`cards/`)
- Print PDF: `De-Lucerna-VOL4-nl-es.pdf` — 12,107,932 bytes,
  sha256 `06f0e2e00aece0d687edf0540098e4cc8b6e4e4c62b451792a1be6cb11608874`
- Web PDF: `De-Lucerna-VOL4-nl-es-web.pdf` — 1,540,051 bytes,
  sha256 `7025ce05d97599d1910ab4e27f1e1c583ae86d43ef5d64a169b22bdb77ef0721`
  (via `tools/webpdf.py`, text layer pdftotext 46,703 B)
- Source export: `2026-w47-nl-es.text.md` — 47,648 bytes
  (142 single + 2 match headers + 8 match items = 150; 8 golden, 6 gloss)
  sha256 `672bd4c0080c14ab11026a13ccdecf826bd759cc3f348c5751852386efe4684b`
- `ABSTRACT.txt` (Spanish, one line, no ASCII double quotes)
- This KIT.

## Build record (final = build 2)

- `run.py` exit 0, TOTAL 150, **zero OVERFLOW / TOO WIDE warnings**.
  `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core);
  `flow[P8-keys] ended col 3/3 y=2502 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0 (< 7 MB).
- Gates (build 2): **ALL PASS** — occlusion 0 flags; p8 extract 150/150;
  p8 compare CLEAN, 0 key diffs; freeze direct sha256 8/8; print/web text
  posdiff 0 msdiff 0 on all 8 pages (P1 812/812 … P8 2391/2391); pdftotext
  print 46,748 B / web 46,742 B; P8 answer-zone min font 10.12 pt
  (median 10.12); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit
  clean (off-palette {}, VOL.5 = 5 = core, paper fills 8).
- Visual: all 8 cards viewed, clean. P1 numbers box fits col 1; P2 ZO ONTHOUD
  "RECUERDA" fits; P6 chart head "DATOS DE PRÁCTICA" 401 px (0.5 px past the
  box edge, invisible — W46-shipped string); P7 BRIEVEN box ends above the
  ZINNEN rule; P8 answers 1–150 complete, pen photo in col 4.

## Fixes vs the generated fan-out (explanation layer only)

1. P1 subtitle → 36 pt, spacing 2 (W46 es; 1629 px < 1818 px limit).
2. Numbers-box title → "DE WEEK IN CIJFERS　EN CIFRAS" (370 px).
3. Numbers-box items shortened ([2,1,2,2], total 357 px).
4. P6 chart head → "DE GRAFIEK　DATOS DE PRÁCTICA" (401 px, W46-shipped).
5. P2 box title → "ZO ONTHOUD JE HET　RECUERDA".
6. P7 BRIEVEN glosses shortened to telegraphic W46 style (g1 2, g2 2 lines;
   VOL.5 reference kept so the §1.1 VOL.5 count stays 5 = core).
7. P1 agenda gloss → "Fechas y horas: artículos, págs. 2 a 5." (322.9 px).
8. P1 agenda sub-head → "CITAS SEMANALES" (362.1 px; was 421 px, past the box).
9. P1 IN DEZE EDITIE head → "ESTE NÚMERO" (370.1 px; was 408 px, past the box).
10. **P8-keys overflow (build 1, flow ended 2590)**: shortened 5 col-3 answer
    notes, each measured to drop from 2 lines to 1 (13.5 pt serif, 422.5 px):
    #133 "S + V + tiempo", #134 "S + V + O + lugar", #136 "S + V + O + modo",
    #139 "Ordinal 88e", #140 "surprise: expresión fija". Keys untouched; the
    abbreviated forms keep ALL word-order elements (S/V/O/tiempo/lugar/modo) —
    unlike the fr #133/#136 cuts that dropped an element. Flow ends 2502.
11. No P1-headline overflow: the es bridge is 3 lines at 20.5 pt (1411) and the
    box (357 px) fits col 1 with 48 px to spare.
12. **Re-fanout fix2 (2026-11-11, proof1 D1/D2):** P6 `VOOR OF TEGEN?　¿A FAVOR O
    EN CONTRA?` (+47.8px over) → `VOOR OF TEGEN?　¿SÍ O NO?` (+103.5 clearance);
    P7 `HET WOORD　PALABRA DE LA SEMANA` (+34.0) → `HET WOORD　PALABRA SEMANAL`
    (+21.5). Both re-measured from the built SVGs (coordinator handoff item 2);
    no further shortening needed.
13. **Re-fanout fix2 D6 (proof1 + coordinator handoff 2026-11-11 12:45 EST):**
    Q140 key `Ik maak een surprise met een gedicht.` → `Ik maak een surprise
    met een kort gedicht.`, note `surprise: expresión fija` → `surprise:
    expresión fija; corto = kort`. Source: the key is copied verbatim from
    core `content8.py:75`; the core's own source sentence (`我做一个带小诗的伪装礼物`)
    carries 小诗, so the defect originates in the core. Verified post-build in
    text.md:415 and on the printed P8 (answer 140). p8 compare still CLEAN
    (translation items 137–140 are legitimately re-aim, exempt from key compare).
14. **Re-fanout fix2 D3:** P2 D-set option c → `"eten voor Sinterklaas' paard"`
    (core fix2 short form); clearance +71.9px.
15. **Re-fanout fix2 D5:** P4 HET PROGRAMMA box gained `"Stand Eredivisie na 12
    ronden: PSV 26, Feyenoord 25, Ajax 25 punten."` (5th fact, after Speelronde
    12, before Speelronde 13); box +73px.
16. **O2 hardening (proof1):** EN JIJ boxes (P2 `content12.py`, P5
    `content56.py`) bottom pad +20 → +22.

## Cross-edition actions done during es

- pt/ru item-3/item-1 shortening pre-fixed (pt item 3 → "(8 pontos:
  empatados)", ru item 1 → "(16 ноября: Германия)") so their 4-line bridges
  (1441) fit the box (357 px, 1441 + 369 = 1810 ≤ 1828).
- Bridge/box fit pre-checked for all remaining editions: it 3 lines / 357 fits,
  pt 4 lines / 357 fits (after item fix), ru 4 lines / 357 fits (after item
  fix), ja 3 lines / 357 fits, ko 3 lines / 357 fits, zh-tw 3 lines / 384 fits.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 3)

Rebuilt from the fixed core (D3 + D5 + D4 export + proof1 fixes §Fixes 12–16). Build only — no commit, no push. Logs: `hidden_files/w47/scratch-refanout-nl/` — `es-build.log`, `es-check.log`, `es-creambox.log`, review `es-review/` (p1–p8 + crops); handoff note `es-proof-handoff-note.md`.

- D3 short form in P2, clearance +71.9px (x+adv 1790.1); D5 standings line in P4 box + text.md; D4 142 `— Respuesta:` + 8 `(Respuesta x)`, 答案 0; italic print=web=1.
- text.md diff vs build 2: exactly 9 changed lines (D3 2 + D5 1 + P6 title 2 + P7 title 2 + Q140 2) — no unintended changes.
- Q140 (handoff item 1): key + note verified in text.md:415 and on printed P8 answer 140; p8 compare CLEAN. Q78 (handoff item 3, O1): stem and key `gaat maken` unchanged — singular-zij convention accepted, verified in text.md:262.
- Gates (build 3): TOTAL 150, by page 10/18/18/18/18/18/12/38, zero OVERFLOW / TOO WIDE; occlusion 0; p8 extract 150/150, compare CLEAN; freeze 8/8; print/web text posdiff 0, msdiff 0, all 8 pages (tokens 812/820/727/731/794/743/913/2403); pdftotext 46,814 B both; P8 font min=median 10.12pt, spans 184; chips core=edition {A2:8, B1:24, B2:3}; §1.1 clean.
- Creambox: 3 flags, all adjudicated non-overflow: P2 CREAM-BOTTOM `'neerlandés y envíalas a la redacción.'` (bottom 1446.2 vs rect 1447.8) and P5 CREAM-BOTTOM `'neerlandés y envíalas.'` (bottom 994.8 vs rect 996.5) both pixel-probed 0 dark pixels in the 7px strip below the box bottom (2px-margin rule only); P6 CREAM-RIGHT on the chart head `DE GRAFIEK　DATOS DE PRÁCTICA` (advance-based right 1862.5 vs rect 1862.0) — true-ink probe of the rendered card finds the rightmost dark pixel at x=1861, i.e. the ink ends 1px INSIDE the box; the 0.5px is advance-width side bearing, not ink. This supersedes the build-2 note "(0.5 px past the box edge, invisible)". 0 true overflow.
- 8-page visual pass: P1–P8 clean (P6 `¿SÍ O NO?` and P7 `PALABRA SEMANAL` in their boxes; P2/P5 EN JIJ glosses end inside their boxes with the +22 pad; P4 box with new standings line; P8 answers 1–150 complete, Q140 key as fixed).
- Known core item NOT in this build: core-nl re-proof (post-fix2) found D6/D7 — a Chinese full stop `。` orphaned alone on its own line on core P3 and P7. Core fix3 is being done by another agent; this edition gets a separate incremental rebuild then. This build is against core HEAD `5de7492f` only.
- Open item for the coordinator: the Q140 key-vs-source mismatch also exists in en/fr/ja/ko/pt/zh-tw (their Q140 source sentences carry little/petit/小/curto, keys omit `kort`) and in the core itself — see `es-proof-handoff-note.md`. Per coordinator instruction only es was corrected; a core-level fix (add `kort` to the core key) would correct all 7 at once.

## Delta (core fix3 + fix4 + fix5, 2026-11-11, build 4)

Core-nl fix3 (D6/D7) + fix4 (D8/D9/D10) + fix5 (D11) synced to this edition.
Only this edition's own sources changed; core-nl untouched, staging copy
`fanout-nl/2026-w47-nl-es/` untouched. No commit, no push. Logs:
`hidden_files/w47/scratch-delta-nl-es/` (DELTA-LOG.md, width-scan.log,
orphan-sweep-pre/post.log, p8-compare-pre.json, p8-compare.json,
p8-compare-3way.json, gates.log, gates-es.json, crops).

- Old SHAs (build 3, history): print
  `0388d59c7e7085bbd4a733f235081f26dac901489ebe1f10ee121f391306b771` /
  12,669,541 B; web
  `5b4f81621c77233cf9d89fa44eb6a1a249fb943f39d64ca96749e70f39cd7a21` /
  1,616,172 B; text
  `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` /
  47,649 B (unchanged by this delta).
- New SHAs (build 4): print
  `45a4c25ea7780d378dbc41c8b95290d4c12121b99e11634611383cb9593697a8` /
  12,669,539 B; web
  `47d4a6c6c0e8e3b150ced86ceb830ca9bc41b3d72a6d67b7523d7c499fed59eb` /
  1,616,177 B; text unchanged (see above).
- D6 (structural sync): `bslib4.py` gained the `w` wrap-width override on
  `Flow.para`/`Flow.bridge` (core fix3 mechanism); P3 bridge
  `Completa en perfecto. Fíjate en los auxiliares hebben/zijn.` passes
  `w=377.5` (width-scan band 329.5–425.5 px, midpoint, re-derived from the
  Spanish text; core's 382.5 not copied). Pre-fix SVG had no orphan — 2
  lines ending `hebben/zijn.`; post-build p3 SVG byte-identical.
- D7 (structural sync): P7 gloss bridge passes `w=419.5` (band
  414.5–424.5 px, midpoint). Pre-fix 3 lines ending `final; scoren
  marcar.`; post-build p7 SVG byte-identical.
- D8 (structural sync): `content56.py` `capcn_w = 370.75` (band
  349.5–392.0 px, midpoint), used in both the box-height computation and
  the `p.para` call. Pre-fix 4 lines, baselines 635.02/659.44/683.86/708.28,
  no line-initial punctuation; post-build p6 SVG byte-identical.
- D9 (already fixed, no change): registry key, text.md:415 answer and the
  P8 node all already read `Ik maak een surprise met een kort gedicht.`
  (fixed in this edition at re-fanout, KIT §13). Pre-fix p8 compare
  keydiff was already [137, 138] (translation items, by design); 140 was
  never in it. `content8.py` untouched.
- D10 (structural sync): `content7.py` `dt_zh_w = 362.5` (band
  319.5–405.5 px, midpoint), used in both the `lh` computation and the
  `p.para` call. Pre-fix 2 lines, baselines 1783.27/1811.67, no
  line-initial punctuation; post-build p7 SVG byte-identical, `P7 col3
  ends 1927.0` unchanged.
- D11 (TRUE FIX): `content34.py` P4 HET PROGRAMMA box top reserve 62 → 89
  (= 16 pad + 52 title block + 21 para y-offset); `sh` 611.0 → 638.0,
  `P4 col3 ends 1229.6`. Pre-fix last line `18:45 uur.` baseline 1209.49
  sat 6.89 px BELOW the box bottom (1202.6); post-fix margin +20.11 px
  (true ink lowest row 1209, +20.60 px), 7px strip below the box bottom 0
  non-paper pixels. Only `p4-sport.svg` changed among the 8 SVGs.
- Gates (build 4): `run.py` rc=0, TOTAL 150, by page
  10/18/18/18/18/18/12/38, A2 46 / B1 73 / B2 31, zero OVERFLOW / TOO WIDE;
  occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff
  [137, 138]; 3-way compare 149/149 MATCH (Q150 open-writing exception);
  freeze core-standard 8/8 + in-edition freeze 8/8; print/web text
  posdiff 0 msdiff 0 all 8 pages (tokens 812/820/727/731/794/743/913/2403);
  pdftotext print 46,814 B = web 46,814 B, and print text byte-identical
  to build 3 (no wording changed); P8 answer-zone min font 10.12 pt;
  orphan sweep (a)/(b) 0/0 both methods, all pages, pre and post;
  creambox 3 flags byte-identical to build 3, true overflow 0 (P2/P5
  strips 0 non-paper pixels; P6 title solid ink rightmost 1861, 1px
  inside); spill sweep 0 (P4 box: no BELOW hit). text.md re-export
  byte-identical to build 3 (47,649 B).

## Fix round 1 (nl-es proof1 D1/D2/D3, 2026-11-11, build 5)

Sync of the fix1 source repair into the production deliverables (SVG +
cards + print/web PDF + this KIT). Sources were repaired by the fix1
agent (10 lines in 5 files, strings unchanged); this round only rebuilt
from those sources and synced the outputs. No commit, no push. Logs:
`hidden_files/w47/scratch-fix-nl-es2/` (SYNC-LOG.md, run-fix1.log,
render-fix1.log, webpdf-fix1.log, svg-diff.log, edge-sync.json,
pil-edge-sync.json, pil-render-sync.json, text-compare-sync.json,
p8-compare-sync.json, occlusion-sync.json, freeze-diff-sync.json,
freeze-baseline-sync.log).

- Old SHAs (build 4, history): print
  `45a4c25ea7780d378dbc41c8b95290d4c12121b99e11634611383cb9593697a8` /
  12,669,539 B; web
  `47d4a6c6c0e8e3b150ced86ceb830ca9bc41b3d72a6d67b7523d7c499fed59eb` /
  1,616,177 B; text
  `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` /
  47,649 B (unchanged by this round).
- New SHAs (build 5): print
  `e6c285668e99e80a4651d2377ee3dd3ccce6c5ea54a288963aa07012e233a8e5` /
  12,669,546 B; web
  `55e8489d18ee3d038c1da5a3c93aea144d2221289c98603c3c808306d577ad0b` /
  1,616,170 B; text unchanged (see above).
- Fix (source, unchanged by this round): `bslib4.py:21`
  `NOTE_RIGHT = RIGHT - 10`; 8× `p.text(RIGHT, …)` →
  `p.text(NOTE_RIGHT, …)` (`content12.py:147/:214/:235`,
  `content34.py:50/:147`, `content56.py:65/:183`, `content8.py:133`),
  strings unchanged; `content56.py:153` P6 chart-title size 24 → 23
  (comment at :150–152). Note: the 5th furniture line sits at
  `content56.py:183`, not :180 as the handoff wrote — same line, same
  `# fix1 … 5 of 5` comment, verified by content.
- Rebuild determinism: scratch rebuild of the print PDF is byte-identical
  to the fix1 agent's candidate (`e6c28566…`, 12,669,546 B). The web PDF
  is 1 byte smaller than the candidate (1,616,170 vs 1,616,171 B,
  SHA differs) — web-PDF SHA is known non-reproducible; the text layer
  is byte-identical to the candidate (pdftotext 46,815 B both, 0 diff) and
  to the rebuilt print PDF (0 diff).
- SVG element diff (production vs rebuild): element counts identical on
  all 8 pages; exactly 9 changed elements, all fix1 (P1 row x
  1141.9→1131.9; P2 rows 1200.1→1190.1, 1175.3→1165.3; P3/P4/P5 furniture
  1175.3→1165.3; P6 title 24→23 + furniture −10; P7 0 changes,
  byte-identical; P8 row 1120.8→1110.8). Rebuilt SVGs byte-identical to
  the fix1 candidate SVGs; rebuilt cards byte-identical to the candidate
  cards.
- Gates (build 5, re-run on the synced production files): `run.py` rc=0,
  TOTAL 150, by page 10/18/18/18/18/18/12/38, A2 46 / B1 73 / B2 31,
  zero OVERFLOW; edge raster (delivered print PDF, 600 dpi, limit 1862):
  D1 1849.44 (+12.56), D2 P1 1856.16 (+5.84), D2 P2 1855.68 (+6.32),
  D3 P2–P6 1853.92 (+8.08), D3 P8 1854.08 (+7.92) — all byte-identical
  to the fix1 measurements; PIL true-ink re-render (same font files,
  4× supersampled): D1 1845.5, D2 P1 1850.75, D2 P2 1850.5, D3 1850.5,
  P8 1850.5 — all ≤1862; whole-page (excl footer) P1 1862.24 (design
  edges, unchanged from build 4), P2–P8 1861.92; freeze core baseline
  8/8, freeze diff rc=0 (added CJK only U+3000 ×7, P2–P8 each 1);
  p8 extract 150/150, compare CLEAN, keydiff [137, 138]; occlusion
  0 flags; print/web text posdiff 0 msdiff 0 on all 8 pages (tokens
  812/820/727/731/794/743/913/2403); pdftotext print 46,815 B = web
  46,815 B; P8 answer-zone min font 10.12 pt (median 10.12, 184 spans).
- Synced files: 7 SVG (P1–P6, P8; P7 byte-identical, unchanged), 7 cards
  (P1–P6, P8; P7 card unchanged), print PDF, web PDF, this KIT. `.py`,
  `.text.md`, `ABSTRACT.txt`, `assets/` byte-identical to the pre-sync
  snapshot; no `__pycache__` written into production.

## D5 rebuild (2026-11-12, B档 — explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader; REDO in top-level production)

- **Why a redo:** the first D5 worker (2026-11-12, `scratch-d5-rebuild-nl/`) rebuilt the `fanout-nl/` COPY, not this top-level production dir, and deleted its build-copy — production still held pre-D5 PDFs (print `e6c28566…`, web `b483f73d…`). This redo rebuilt from the current top-level build-5 sources in place. The copy's D5 SHAs (print `a6f78752…` / 12,107,935 B) are superseded and do NOT describe production.
- **Pre-D5 baseline (top-level, verified on disk, `scratch-d5-redo-nl/2026-w47-nl-es/baseline.txt`):** svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `e6c285668e99e80a4651d2377ee3dd3ccce6c5ea54a288963aa07012e233a8e5` / 12,669,546 B; web `b483f73d80199a96b4a390c165ce7fb94c3d01c7104975e1a749cf5156687a4f` / 1,616,179 B (KIT §Files delivered recorded a different web SHA `55e8489d…` — pre-existing drift, web rebuilt after KIT written); text `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` / 47,649 B. Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by the build-4 sh=89 port), boxtitle 0 DEFECT (the copy-era pre-existing +1.5px P6 defect was already fixed in production by fix1 D1, 24 → 23pt), edge 0; census FAIL 497 Latin-in-CJK-sans. `run.py` pre-run reproduced the on-disk SVGs 8/8 byte-identical.
- **Install:** mechanism `apply_variant.py --target nl --reader es` (mode latin), svglib md5 `78fdfbb037538b1f8a738434ea90a782` → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.
- **Ported core fixes (already in production before this rebuild):** P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11); P6 `DE GRAFIEK` 24 → 23pt (fix1 D1). P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt applied in this rebuild (core-nl D5 defect, same line here).
- **Defects found by the gates (all D5-caused, same class: bold-caps box titles widen in Newsreader SemiBold) — conclusions reused from the first worker's copy build, re-verified on the top-level rebuild; all fixed by size only, text unchanged:**
  1. P1 `DE WEEK IN CIJFERS　EN CIFRAS` +10.2px → `f.box` tsize 23 → 22 (`content12.py:43`).
  2. P1 `IN DEZE EDITIE　ESTE NÚMERO` +20.5px → 24 → 22pt (`content12.py:90`).
  3. P2 `ZO ONTHOUD JE HET　RECUERDA` +24.0px → `f.box` tsize 23 → 21 (`content12.py:177`).
  4. P6 `DE GRAFIEK　DATOS DE PRÁCTICA` +58.6px → 23 → 20pt (`content56.py:153`; production already at 23pt via fix1 D1).
  5. P7 `HET WOORD　PALABRA SEMANAL` +32.1px → 23 → 21pt (`content7.py:84`).
  6. P2 TEXTX: `PAKJESAVOND IN VIER WOORDEN　PAKJESAVOND EN CUATRO PALABRAS` overlapped right-anchored subtitle by 6.8×15.5px → head 28 → 27pt (`content12.py:213`).
- **Gates (final rebuild, after the 6 fixes, all in top-level production):** `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS 0 defects); `render.py` / `webpdf.py` RC 0; `p8.py extract` 150/150, `compare` vs core-nl CLEAN, keydiff=[137, 138] (reader-language keys, expected); `freeze.py baseline` 8/8 byte-identical; `freeze.py diff` vs core-nl: added CJK 7 (all U+3000); vs pre-D5 baseline: added CJK 0, added Latin strings 231 (run-splitting, expected); `occlusion_audit.py` 0 flags; `spill_sweep.py` 0 SPILL (39 OBSERVE); `boxtitle_check.py` 0 DEFECT; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` PASS 0 defects (P8 lines 237 → 237, footer slack 41.7px unchanged); `d5_census.py` PASS — D5 Latin 0, Cyrillic 0, curly-in-CJK 0; `census_quotes.py` 0 defective; text layer print = web = 46,704 bytes, word multiset diff 0; orphan sweep (a) 0, (b) 0.
- **New SHAs (lowercase, verified on production files):** print `2da02d5b30814f011adc75399fd5c4b1b90e41e8877bf3eb16c0610d4408f776` (12,107,937 B); web `ac5498117a56a0d7125e4b59ab39d6db8371297ca1671feb269bc46f13ef14b5` (1,540,064 B). **text.md unchanged:** 47,649 B, sha256 `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb`, byte-identical to the pre-D5 baseline.
- **Repro check (2026-11-12, third worker):** re-running `render.py` + `webpdf.py` in place reproduced the print PDF byte-identically (SHA unchanged); the web PDF rebuilt with a new SHA `249fda66604bdda210ee57701c27931bc8beb17ba978c99fb85e9cb40b482684` (1,540,062 B) — content-equivalent (pdftotext 46,704 B, identical; `textlayer.py` re-run RC 0, word multiset diff 0). Only embedded-font `head`-table checksums differ (stream-level diff on nl-de: 70 bytes in 18/126 streams). Web PDF SHA is not reproducible run to run (see build-7 note); "Files delivered" above is re-synced to the new production file; the SHA on the "New SHAs" line above is the rebuild's original output, kept as history (was `ac5498117a56a0d7125e4b59ab39d6db8371297ca1671feb269bc46f13ef14b5`, 1,540,064 B).
- **Fix (2026-11-12, W47 nl repair, round 2):** PROOF-NOTE-2 item 2 (low) — Q140 source sentence used Spanish `sorpresa` while the edition's term is the Dutch loanword `surprise`. `content8.py:76`: `Hago una sorpresa con un poema corto. → ___` → `Hago un surprise con un poema corto. → ___` (answer `Ik maak een surprise met een kort gedicht.` and its note `(surprise: expresión fija; corto = kort)` untouched; cf. Q14 note `Un surprise es un regalo disfrazado`, glossary `de surprise regalo disfrazado`). Print P8 verified: `Hago un surprise con un poema corto.`, old form 0. Rebuilt: `run.py` TOTAL 150 RC 0, `render.py` RC 0, export dry-run to /tmp then re-exported (150 exercises, 8 golden, 6 gloss), `webpdf.py` RC 0. Exporter trap (ru FIX-LOG §7) fired once: the fresh export dropped the `### ` prefix on line 280 (`DE GRAFIEK　DATOS DE PRÁCTICA`) — backfilled by hand; final diff vs pre-fix text.md contains ONLY line 415. Tool fix (needed for this export): the shared exporter stub `scratch-nl/stub_bslib47.py` lacked es-only `NOTE_RIGHT` (defined in es `bslib4.py:21`, absent from core bslib, which the stub loads) — added `NOTE_RIGHT = RIGHT - 10` and added it to the stub's `__all__`; no production source touched. Gates (`tools/gates.py`, ALL PASS): occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (reader-language keys, expected); freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages; pdftotext print = web = 46,703 B; P8 answer-zone min 10.12pt; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean. Extras: `boxtitle_check.py` 0 DEFECT, 0 OBSERVE, 0 marginal; `spill_sweep.py` 0 SPILL (39 OBSERVE); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `head_check.py` PASS 0 defects; `d5_creambox_audit.py` PASS 0 defects (vs pre-fix baseline rebuilt in /tmp; P8 lines 237 → 237, footer slack 41.7px unchanged). D5 census (self-written SVG font-family direct count): D5_lat 0, curly-in-CJK 0. **New SHAs (lowercase, verified on production files):** print `06f0e2e00aece0d687edf0540098e4cc8b6e4e4c62b451792a1be6cb11608874` (12,107,932 B); web `7025ce05d97599d1910ab4e27f1e1c583ae86d43ef5d64a169b22bdb77ef0721` (1,540,051 B); text.md `672bd4c0080c14ab11026a13ccdecf826bd759cc3f348c5751852386efe4684b` (47,648 B). Logs: `hidden_files/w47/scratch-fix-nl/nl-es/`.
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `svglib.py` (D5 install), `content12.py` (P2 head 25 → 23pt; 4 title sizes), `content56.py` (P6 title 23 → 20pt), `content7.py` (P7 title 23 → 21pt), `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-es/` (`rebuild-1.log`, `run.log`, `render.log`, `webpdf.log`, `routing.log`, `post/` gates + `post.txt`, `pre/` pre-D5 gates, `baseline.txt`).
