# WEEKLY-KIT — 2026-W47 · nl → ru (Russian readers)

Dutch weekly newspaper for Russian readers. Target language Dutch (nl), reader
native language Russian (ru). VOL.4, issue 2026-11-16 – 2026-11-22. Target:
150 exercises (10/18/18/18/18/18/12/38 across pages 1–8); A2 46 / B1 73 / B2 31;
model essay 81 words.

## Source

Fan-out of the frozen Dutch core `production/2026-w47/core-nl/` (slug
`2026-w47-nl-zh-cn`). Dutch target text, facts, and answer keys are frozen; only
the explanation layer (glosses, notes, section subtitles, exercise type words)
was rewritten in Russian. No new trend research, no invented reader letters.

## Files delivered

- 8 SVGs (`svg/p1-voorpagina.svg` … `svg/p8-toets.svg`), 8 render cards (`cards/`)
- Print PDF: `De-Lucerna-VOL4-nl-ru.pdf` — 12,261,013 bytes,
  sha256 `d4f081587c7d85e155734d4008d191e8b6f009f50738b3370f966c311053002e`
- Web PDF: `De-Lucerna-VOL4-nl-ru-web.pdf` — 1,674,522 bytes,
  sha256 `7a06f80d9238669ae1c8c1bfc848a2b814d9f0999e3e9f4c79b942dd17747dff`
  (via `tools/webpdf.py`, text layer pdftotext 55,036 B)
- Source export: `2026-w47-nl-ru.text.md` — 57,909 bytes,
  sha256 `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228`
  (142 single + 2 match headers + 8 match items = 150; 8 golden, 6 gloss)
- `ABSTRACT.txt` (Russian, one line, no ASCII double quotes)
- This KIT.

## Build record (final = build 6)

- `run.py` exit 0, TOTAL 150, **zero OVERFLOW / TOO WIDE warnings**.
  `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core);
  `flow[P8-keys] ended col 3/3 y=2486 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0 (< 7 MB).
- Gates (build 4): **ALL PASS** — occlusion 0 flags; p8 extract 150/150;
  p8 compare CLEAN, 0 key diffs; freeze direct sha256 8/8; print/web text
  posdiff 0 msdiff 0 on all 8 pages (P1 797/797 … P8 2149/2149); pdftotext
  print 54,915 B / web 54,913 B; P8 answer-zone min font 10.12 pt
  (median 10.12); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit
  clean (off-palette {}, VOL.5 = 5 = core, paper fills 8).
- Visual: all 8 cards viewed, clean. P1 numbers box fits col 1; P2 ZO ONTHOUD
  "ЗАПОМНИ" fits and the GEDICHT strip gloss fits its box; P6 chart head
  "УЧЕБНЫЕ ДАННЫЕ" fits and the VOOR OF TEGEN head "ЗА ИЛИ ПРОТИВ?" fits;
  P7 BRIEVEN box ends above the ZINNEN rule; P8 answers 1–150 complete,
  pen photo in col 4.

## Fixes vs the generated fan-out (explanation layer only)

1. P1 subtitle → 36 pt, spacing 0 (W46 ru; 1656 px < 1818 px limit).
2. Numbers-box title → "DE WEEK IN CIJFERS　В ЦИФРАХ" (370 px).
3. Numbers-box items shortened ([3,1,2,2], total 384 px) — item 1
   "(16 ноября: Германия — Нидерланды)" → "(16 ноября: Германия)" (pre-fixed
   during the es build).
4. P6 chart head → "DE GRAFIEK　УЧЕБНЫЕ ДАННЫЕ" (394 px).
5. P2 box title → "ZO ONTHOUD JE HET　ЗАПОМНИ".
6. P7 BRIEVEN glosses shortened to telegraphic W46 style (g1 2, g2 2 lines;
   VOL.5 reference kept so the §1.1 VOL.5 count stays 5 = core); PAS OP!
   err1 → 1 line ("Oranje — имя собственное."), err3 → 1 line ("Прошедшее
   время winnen — won."), err4 → 2 lines.
7. P1 agenda gloss → "Все даты и время: статьи, страницы 2–5." (373.0 px).
8. P1 IN DEZE EDITIE head → "В ВЫПУСКЕ" (340.4 px; was 441 px, past the box).
9. **P8-keys overflow (builds 1–2, worst of all editions)**: the flow ended
   at 2590 with #148/#149/#150 clamped on one baseline (y=2573.5), #150's
   3 lines overlapping. Root cause, not a single-note overflow: Russian
   notes are the longest of all editions — col 3 held 41 blocks (vs ~37 in
   other editions) with 10 two-line answers, so the col-3 content was
   ~94 px over. Fix in two parts: (a) six col-3 notes shortened to 1 line
   (#127, #132, #133 "П + Г + время", #134 "П + Г + Д + место", #135
   "П + Г + вр. + место", #136 "П + Г + Д + обр.") — build 2 still ended
   2590 (the flow-end number is a clamp artifact, not a sum); (b) eleven
   more notes shortened to 1 line across cols 2–3 (#82, #83, #88, #89, #91,
   #97, #98, #99, #112, #139 "— 88-й", #140 "— surprise (фикс.)"), which
   let col 2 absorb 4 more blocks and moved the col-3 boundary later. Flow
   ends 2486. Abbreviated forms keep ALL word-order elements (П/Г/Д =
   подлежащее/глагол/дополнение).
10. **P2 GEDICHT strip gloss overflow (build 3, class 13th)**: the 4-line
    gloss "Маленькое стихотворение: смешное, тёплое или с лёгкой насмешкой"
    ran 13.3 px past the 150 px box bottom (last baseline 1781.3 vs box
    bottom 1768; occlusion does not flag box-internal spills). → "Маленькое
    стихотворение: смешное или тёплое" (3 lines at 19 pt, lw 201 px).
11. No P1-headline overflow: the ru bridge is 4 lines at 20.5 pt (ends 1441),
    but the shortened box (357 px) fits col 1 (1441 + 369 = 1810 ≤ 1828).
12. **Re-fanout fix2 D3:** P2 D-set option c → `"eten voor Sinterklaas' paard"`
    (core fix2 short form); clearance +71.9px.
13. **Re-fanout fix2 D5:** P4 HET PROGRAMMA box gained `"Stand Eredivisie na 12
    ronden: PSV 26, Feyenoord 25, Ajax 25 punten."` (5th fact, after Speelronde
    12, before Speelronde 13); box +73px.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 5)

Rebuilt from the fixed core (D3 + D5 + D4 export only — ru has no proof dir, so no edition-level proof fixes). Build only — no commit, no push. Logs: `hidden_files/w47/scratch-refanout-nl/` — `ru-build.log`, `ru-check.log`, `ru-creambox.log`, review `ru-review/` (p1–p8 + crops).

- D3 short form in P2, clearance +71.9px (x+adv 1790.1); D5 standings line in P4 box + text.md; D4 142 `— Ответ：` + 8 `(Ответ x)`, 答案 0; italic print=web=1.
- text.md diff vs build 4: exactly 3 changed lines (D3 2 + D5 1) — no unintended changes.
- Gates (build 5): TOTAL 150, zero OVERFLOW / TOO WIDE; occlusion 0; p8 extract 150/150, compare CLEAN; freeze 8/8; print/web text posdiff 0, msdiff 0, all 8 pages (tokens 797/802/722/727/783/730/885/2149); pdftotext 54,978 B both; P8 font min=median 10.12pt, spans 598 (Cyrillic renders as many small spans); chips core=edition {A2:8, B1:24, B2:3}; §1.1 clean.
- Creambox: 3 flags, all adjudicated non-overflow: P2 CREAM-BOTTOM EN JIJ last line `'редакцию.'` (bottom 1503.0 vs rect 1503.8) and P5 CREAM-BOTTOM `'отправь их.'` (bottom 1051.6 vs rect 1052.5) both pixel-probed 0 dark pixels in the 7px strip below the box bottom (2px-margin rule, ink inside); P6 CREAM-RIGHT `DE GRAFIEK　УЧЕБНЫЕ ДАННЫЕ` (right 1855.6 vs rect 1862.0, inside by 6.4px) is the 8px warning band only. 0 true overflow.
- 8-page visual pass: P1–P8 clean (P6 chart head + `ЗА ИЛИ ПРОТИВ?` in boxes; P7 BRIEVEN ends above the ZINNEN rule; P8 answers 1–150 complete).
- Known core item NOT in this build: core-nl re-proof (post-fix2) found D6/D7 — a Chinese full stop `。` orphaned alone on its own line on core P3 and P7. Core fix3 is being done by another agent; this edition gets a separate incremental rebuild then. This build is against core HEAD `5de7492f` only.
- Note (Q140, recorded not fixed): ru Q140 source `... со стихотворением.` carries no qualifier, so its key matches — no defect in ru. The same key-vs-source mismatch exists in en/fr/ja/ko/pt/zh-tw (see `es-proof-handoff-note.md`); per coordinator instruction only es was corrected.

## Delta (core fix3 + fix4 + fix5, 2026-11-11, build 6)

Core fix3 (D6/D7) + fix4 (D8/D9/D10) + fix5 (D11) synced to this edition. Build only —
no commit, no push. Full log: `hidden_files/w47/scratch-delta-nl-ru/DELTA-LOG.md`
(width scans, per-item measurements, all gates).

- D6/D7/D8/D10 were **pre-clean in this edition** (reader-layer line breaks differ
  from the core Chinese): orphan sweep 0/0 on all 8 pages pre-fix. Structural sync
  only — `bslib4.py` gained the core fix3 `w` mechanism (`Flow.para`/`Flow.bridge`
  optional wrap-width override); w re-derived per edition with a 0.1px width scan
  (core numbers never copied): D6 bridge w=366.05 (band 304.3–427.8, 3 lines);
  D7 bridge w=435.85 (band 419.8–451.9, 3 lines; line 1 measures 419.78px, inside
  CW 422.5); D8 `capcn_w=369.3` (band 353.1–385.5, 4 lines); D10 `dt_zh_w=384.3`
  (band 373.2–395.4, 2 lines). Each w reproduces the current clean breaks exactly —
  p3/p6/p7 SVGs byte-identical after rebuild.
- D9 Q140 fixed in **two places** (key + stem, both required): key
  `Ik maak een surprise met een gedicht.` → `Ik maak een surprise met een kort gedicht.`
  and stem `Я делаю сюрприз со стихотворением.` →
  `Я делаю сюрприз с небольшим стихотворением.` (registry + text.md:415 + P8 node
  all agree; 149/149 three-way MATCH). This supersedes the build-5 note above
  ("no defect in ru"): the core stem says 带小诗 ("small poem") and the reader
  can only derive `kort` from the stem — without `небольшим` the key is
  underivable (nl-de D12 class defect).
- D11 P4 HET PROGRAMMA box: top reserve 62 → 89 (= 16 pad + 52 title block +
  21 para y-offset), `sh` 611.0 → 638.0; last line `18:45 uur.` baseline 1209.49
  now +20.11px inside the box (was +6.89px below); true-ink margin +20.60px
  (cards) / +20.05px (print PDF 150dpi); 7px strip below the box bottom 0 ink
  pixels by both methods.
- Gates (build 6): TOTAL 150, zero OVERFLOW / TOO WIDE; occlusion 0; p8 extract
  150/150, compare CLEAN, keydiff [137, 138] (translation keys in reader language,
  by design; 140 removed by D9); three-way 149/149; freeze core 8/8 + clean-dir
  repro 8/8; print/web text posdiff 0, msdiff 0, all 8 pages (tokens
  797/802/722/727/783/730/885/2151); pdftotext 55,000 B both; P8 font
  min=median 10.12pt, spans 598; chips core=edition {A2:8, B1:24, B2:3}; §1.1
  clean. Creambox 3 flags, all adjudicated false positives (same as build 5:
  P2/P5 bottom strips 0 non-paper pixels; P6 title true ink +9.5px inside the
  box edge). Box-title true-ink scan (isolated render): 59 titles, 0 over-edge.
  Spill sweep: 0 true spills. Orphan sweep post: 0/0, 1464 lines.
- SVG changes vs build 5: only `p4-sport.svg` (D11) and `p8-toets.svg` (D9).
- New SHAs (build 6): print `21b7adf007a15e195756d49b22c824e828f854e11e02a10c916426997c468cc8` /
  12,718,418 B; web `1a17474368591008dcefb73661be58a17edc38c5dcc98f674fc0afe6ea6cc9bf` /
  1,661,392 B; text `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984` /
  57,870 B.
- Old SHAs (build 5, history): print `f945029d3a736dd3d139c555a4693283dc3aa9feba732edc91805b556ff889c2` /
  12,718,382 B; web `e5e3d5d3fd36b767858c96cafce0b4bf317f7ed2fd62a605aaa7eed327352724` /
  1,661,354 B; text `558786fc6247329c319fd1cf965e458ec32cea1daf3d7ae534f02c9804829273` /
  57,848 B.

## D5 rebuild (2026-11-12, B档 — explanation-layer Latin/Cyrillic rendered in Noto Sans CJK instead of Newsreader; REDO in top-level production)

- **Why a redo:** the first D5 worker (2026-11-12, `scratch-d5-rebuild-nl/`) rebuilt the `fanout-nl/` COPY, not this top-level production dir, and deleted its build-copy — production still held pre-D5 PDFs (print `b9847bb2…`, web `cbaac2df…`). This redo rebuilt from the current top-level build-6 sources in place. The copy's D5 SHAs are superseded and do NOT describe production.
- **Pre-D5 baseline (top-level, verified on disk, `scratch-d5-redo-nl/2026-w47-nl-ru/baseline.txt`):** svglib md5 `9b2531b76693…` (carries the unkerned-run patch, build 6); print `b9847bb26eac3011660c767b4ae17857ddeb39014fe8b9ffa7b9ec90b0404933` / 12,718,074 B; web `cbaac2df7c7acd38f35c9cd9eaba04b3416c290b72e676057f68dccb47b6c7ca` / 1,661,043 B (matches KIT §Files delivered — no drift on this edition); text `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984` / 57,870 B. Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by the build-6 sh=89 port), boxtitle 0 DEFECT, edge 0; census FAIL 612 (Latin 346 + Cyrillic 266 in CJK sans). `run.py` pre-run reproduced the on-disk SVGs 8/8 byte-identical.
- **Install:** mechanism `apply_variant.py --target nl --reader ru` (mode ru), `added _D5_READER = 'ru'` + Noto Sans faces/cmaps + sans_noto `_PATH` rows + fix2 block + D5 sans block. Routing assert: FAILURES 0.
- **Ported core fix:** P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt applied in this rebuild (core-nl D5 defect, same line here). P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 6).
- **Defects found by the gates:** NONE beyond the P2 head. The first worker's copy build also found zero D5-caused defects on this edition — the Cyrillic tails route to Noto Sans unchanged, and no box title overflowed. No en-ru-style P8 key-row collisions appeared (those were a proven measurement false positive in `occlusion_audit.py`, since fixed in the tool).
- **Gates (final rebuild, all in top-level production):** `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS 0 defects); `render.py` / `webpdf.py` RC 0; `p8.py extract` 150/150, `compare` vs core-nl CLEAN, keydiff=[137, 138] (reader-language keys, expected); `freeze.py baseline` 8/8 byte-identical; `freeze.py diff` vs core-nl: added CJK 7 (all U+3000); vs pre-D5 baseline: added CJK 0, added Latin strings 165 (run-splitting, expected); `occlusion_audit.py` 0 flags; `spill_sweep.py` 0 SPILL (36 OBSERVE); `boxtitle_check.py` 0 DEFECT; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` PASS 0 defects (P8 lines 248 → 248, footer slack 39.0px unchanged); `d5_census.py` PASS — D5 Latin 0, Cyrillic 0, curly-in-CJK 0; `census_quotes.py` 0 defective; text layer print = web = 54,983 bytes, word multiset diff 0; orphan sweep (a) 0, (b) 0.
- **New SHAs (lowercase, verified on production files):** print `8fa079cbd094b7b0863fcc526cd5a4f6d719cdadc7a41cdc97a261adbb3d1227` (12,367,658 B); web `e025daa39ff503cb06938cd05877a0e98951daaf8bcb3523e6535de1a942221f` (1,779,860 B — larger than pre-D5 because the Cyrillic Noto Sans faces are now embedded). **text.md unchanged:** 57,870 B, sha256 `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984`, byte-identical to the pre-D5 baseline.
- **Repro check (2026-11-12, third worker):** re-running `render.py` + `webpdf.py` in place reproduced the print PDF byte-identically (SHA unchanged); the web PDF rebuilt with a new SHA `69678fdcdd00e05fe188555d7aa5d6fc2235473a3b2a03cb027e009747d6dbff` (1,779,868 B) — content-equivalent (pdftotext 54,983 B, identical; `textlayer.py` re-run RC 0, word multiset diff 0). Only embedded-font `head`-table checksums differ (stream-level diff on nl-de: 70 bytes in 18/126 streams). Web PDF SHA is not reproducible run to run (see build-7 note); "Files delivered" above is re-synced to the new production file; the SHA on the "New SHAs" line above is the rebuild's original output, kept as history (was `e025daa39ff503cb06938cd05877a0e98951daaf8bcb3523e6535de1a942221f`, 1,779,860 B).
- **Fix (2026-11-12, W47 nl repair, second worker):** PROOF-NOTE item 7 — P1 numbers-box Russian annotation truncated to `(16 ноября: Германия)`. Source fix landed by the first worker (`content12.py:44` + text.md line 13), but the SVG/print PDF were never re-rendered (print SHA still the PROOF value, SVG lacked `Нидерланды, Берлин`). This round re-ran the full pipeline: `run.py` TOTAL 150 RC 0, `render.py` RC 0, export dry-run to /tmp byte-identical to shipped text.md then re-exported (150 exercises, 8 golden, 6 gloss), `webpdf.py` RC 0. Print P1 now reads in full `16 — november: Duitsland – Nederland in Berlijn (16 ноября: Германия – Нидерланды, Берлин)`. Gates (`tools/gates.py`, ALL PASS): occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (reader-language keys, expected); freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages; pdftotext print = web = 55,025 B; P8 answer-zone min 10.12pt; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean. Extras: `boxtitle_check.py` 0 DEFECT; `spill_sweep.py` 0 SPILL (36 OBSERVE); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `head_check.py` PASS 0 defects; `d5_creambox_audit.py` PASS 0 defects. Items 8/9 (R1/R2 font routing) NOT touched — coordinator ruling, left for the cross-family *-ru worker. **New SHAs (lowercase, verified on production files):** print `bb407a7b067e0ce84e8f61149a5fcd913e32174b6a6db1ac755ba466468b78f8` (12,368,148 B); web `1c13bb4f7311b55d6c048cf0a8f72142829aa8b49e6be0a4f210a67ef5014363` (1,780,327 B); text.md `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228` (57,909 B). Logs: `hidden_files/w47/scratch-fix-nl/nl-ru/`.
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `svglib.py` (D5 install, mode ru), `content12.py` (P2 head 25 → 23pt), `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-ru/` (`rebuild-1.log`, `run.log`, `render.log`, `webpdf.log`, `routing.log`, `post/` gates + `post.txt`, `pre/` pre-D5 gates, `baseline.txt`).

## fix-xru (2026-11-12, *-ru font-routing repair)

- **Defect:** `svglib.py` `_D5_READER == "ru"` branch routed Latin text to Noto Sans CJK, violating SOP §1.1 (Latin → Newsreader, Cyrillic → Noto Sans).
- **Fix:** deleted the `_D5_READER == "ru"` branch (marker `[removed 2026-11-12 fix-xru]`); Latin now always takes the else path to Newsreader, Cyrillic stays on Noto Sans. Patch applied by the previous worker; this round only rebuilt.
- **Probe (probe_xru.py):** pre — `runs=2512 LAT@NotoSans=2979 LAT@Newsreader=20470 CYR@NotoSans=5291 CYR@Newsreader=0`; post — `runs=3282 LAT@NotoSans=0 LAT@Newsreader=23449 CYR@NotoSans=5291 CYR@Newsreader=0`. LAT@NotoSans 2979 → 0; CYR@NotoSans unchanged (5291).
- **Rebuild:** `driver.sh nl` (`run.py` TOTAL 150 RC 0 → probe RC 0 → `render.py` RC 0 → text-layer multiset gate IDENTICAL, 36,605 non-space chars → `webpdf.py` RC 0). Print PDF mtime 2026-11-12 23:43:54 UTC, 8 pages. Web PDF 8 pages, 1,674,515 B. No retry.
- **New SHAs (verified on production files):** print `5541fc59de37cc5186b447e37f317f7f5dd628f862dd1b0701986c6d29e3e19e` (12,260,999 B); web `5df8b0d6af5b2b94ed9c55222e572df9c8b76fee907b24a07b037b9bbcb4d3b8` (1,674,515 B); text.md unchanged `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228` (57,909 B).
- **Old SHAs (pre-fix, history):** print `bb407a7b067e0ce84e8f61149a5fcd913e32174b6a6db1ac755ba466468b78f8` (12,368,148 B); web `1c13bb4f7311b55d6c048cf0a8f72142829aa8b49e6be0a4f210a67ef5014363` (1,780,327 B).
- Logs: `hidden_files/w47/scratch-fix-xru-w47/` (`build-nl.log`, `summary-nl.txt`, `logs/nl-*.log`, `probe-post-nl.json`).

## fix-nl-ru2 (2026-11-12, boxtitle right-overflow after fix-xru)

- **Defect:** `*-ru` sweep (`hidden_files/w47/scratch-sweep-xru-occl-2/SWEEP-LOG.md`) found 4 boxtitle right overflows, all regressions vs core (core same box not overflowing) after Latin moved to wider Newsreader; occlusion 0 flags. P1 [TITLE] `ЦИФРАХ` +1.5px (core −7.8); P2 [TITLE] `ЗАПОМНИ` +8.5px (core −18.0); P6 [TITLE] `ДАННЫЕ` +14.1px (core −22.0); P6 [BODY] `?` +9.7px (core −22.0, the final `?` of the `VOOR OF TEGEN?　ЗА ИЛИ ПРОТИВ?` head). No ink collision, no clipping.
- **Fix (font size only, wording unchanged — text.md byte-identical):** P1 numbers-box title `f.box(..., tsize=22)` (`content12.py:43`); P2 box title `f.box(..., tsize=22)` (`content12.py:179`); P6 chart head 24 → 22pt (`content56.py:148`); P6 pro/contra head 21 → 20pt (`content56.py:168`). Pre-fix width probe (`text_w`): savings ≈ 17.5 / 17.9 / 34.5 / 19.4px vs overflows 1.5 / 8.5 / 14.1 / 9.7px. Follows the nl 25 → 23pt precedent (P2 head, D5). No wording shortened, so no text.md re-export.
- **Post-fix ink margins (measured on rebuilt SVG runs):** P1 `ЦИФРАХ` ink_r 944.0, +17.0px inside; P2 `ЗАПОМНИ` ink_r 951.9, +9.1px; P6 `ДАННЫЕ` ink_r 1841.4, +20.6px; P6 `?` ink_r 1851.9, +10.1px.
- **Rebuild:** `run.py` TOTAL 150 RC 0, zero FLOW OVERFLOW / HEAD TOO WIDE; `render.py` RC 0; `webpdf.py` RC 0 (web PDF 1,674,522 B < 7 MB). SVG changes vs pre-fix: only p1, p2, p6; p3–p5, p7, p8 byte-identical.
- **Gates (all green):** `tools/gates.py` ALL PASS — occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (reader-language keys, expected); freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages (tokens 799/805/725/726/783/734/887/2207); pdftotext print = web = 55,036 B; P8 answer-zone min 10.12pt; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean. Extras: `boxtitle_check.py` 0 DEFECT, 0 OBSERVE, 0 marginal (34 titles, 483 body lines); `spill_sweep.py` 0 SPILL (110 OBSERVE — same order as sibling es-ru 149 in the same Newsreader generation; the rise vs the old 36 predates this fix); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `head_check.py` PASS 0 defects; `d5_census.py` PASS (D5 Latin 0, Cyrillic 0, curly 0); `census_quotes.py` 0 defective.
- **New SHAs (verified on production files):** print `d4f081587c7d85e155734d4008d191e8b6f009f50738b3370f966c311053002e` (12,261,013 B); web `7a06f80d9238669ae1c8c1bfc848a2b814d9f0999e3e9f4c79b942dd17747dff` (1,674,522 B); text.md unchanged `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228` (57,909 B).
- **Old SHAs (pre-fix, history):** print `5541fc59de37cc5186b447e37f317f7f5dd628f862dd1b0701986c6d29e3e19e` (12,260,999 B); web `5df8b0d6af5b2b94ed9c55222e572df9c8b76fee907b24a07b037b9bbcb4d3b8` (1,674,515 B).
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `content12.py` (2× tsize 23 → 22), `content56.py` (24 → 22, 21 → 20), SVG p1/p2/p6, print/web PDFs, `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-fix-nl-ru2/` (`FIX-LOG.md`, `logs/`, `gates/`, `pre-sha256.txt`, `pre-svg.sha256`, `boxtitle-pre.json`).
