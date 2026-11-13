# WEEKLY-KIT — 2026-W47 · nl → pt (Portuguese readers)

Dutch weekly newspaper for Portuguese readers. Target language Dutch (nl), reader
native language Portuguese (pt). VOL.4, issue 2026-11-16 – 2026-11-22. Target:
150 exercises (10/18/18/18/18/18/12/38 across pages 1–8); A2 46 / B1 73 / B2 31;
model essay 81 words.

## Source

Fan-out of the frozen Dutch core `production/2026-w47/core-nl/` (slug
`2026-w47-nl-zh-cn`). Dutch target text, facts, and answer keys are frozen; only
the explanation layer (glosses, notes, section subtitles, exercise type words)
was rewritten in Portuguese. No new trend research, no invented reader letters.

## Files delivered

- 8 SVGs (`svg/p1-voorpagina.svg` … `svg/p8-toets.svg`), 8 render cards (`cards/`)
- Print PDF: `De-Lucerna-VOL4-nl-pt.pdf` — 12,110,707 bytes,
  sha256 `e2fe3b3a95686bd48e01a7975f62ee33bb821dd6a8a743c1a188bb8e6f119d37`
- Web PDF: `De-Lucerna-VOL4-nl-pt-web.pdf` — 1,542,854 bytes,
  sha256 `40c51869695b80e165661c6adb9309c70341342d56d632c472a7ba18f9ace508`
  (via `tools/webpdf.py`, text layer pdftotext 46,588 B)
- Source export: `2026-w47-nl-pt.text.md` — 47,365 bytes,
  sha256 `67516e2163c8c769ab9574b60b472c7d97706b3c4d89182bb95faa221513727a`
  (142 single + 2 match headers + 8 match items = 150; 8 golden, 6 gloss)
- `ABSTRACT.txt` (Portuguese, one line, no ASCII double quotes)
- This KIT.

## Build record (final = build 4)

- `run.py` exit 0, TOTAL 150, **zero OVERFLOW / TOO WIDE warnings**.
  `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core);
  `flow[P8-keys] ended col 3/3 y=2550 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0 (< 7 MB).
- Gates (build 2): **ALL PASS** — occlusion 0 flags; p8 extract 150/150;
  p8 compare CLEAN, 0 key diffs; freeze direct sha256 8/8; print/web text
  posdiff 0 msdiff 0 on all 8 pages (P1 815/815 … P8 2372/2372); pdftotext
  print 46,631 B / web 46,637 B; P8 answer-zone min font 10.12 pt
  (median 10.12); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit
  clean (off-palette {}, VOL.5 = 5 = core, paper fills 8).
- Visual (build 2): all 8 cards viewed, clean. P1 numbers box fits col 1; P2 ZO ONTHOUD
  "LEMBRA-TE" fits; P6 chart head "DADOS DE TREINO" fits; P7 BRIEVEN box ends above the ZINNEN
  rule; P8 answers 1–150 complete, pen photo in col 4. (The build-2 note that the P6
  VOOR OF TEGEN head "A FAVOR OU CONTRA?" fits was wrong — proof1 D1 later measured it
  +21.5px over the cream box; fixed in the re-fanout, §Fixes 13.)

## Fixes vs the generated fan-out (explanation layer only)

1. P1 subtitle → 34 pt, spacing 0 (W46 pt; 1557 px < 1818 px limit).
2. Numbers-box title → "DE WEEK IN CIJFERS　NÚMEROS" (368 px).
3. Numbers-box items shortened ([2,1,2,2], total 357 px) — item 3
   "(8 pontos: empatados na frente)" → "(8 pontos: empatados)" (pre-fixed
   during the es build).
4. P6 chart head → "DE GRAFIEK　DADOS DE TREINO" (380 px).
5. P2 box title → "ZO ONTHOUD JE HET　LEMBRA-TE".
6. P7 BRIEVEN glosses shortened to telegraphic W46 style (g1 2, g2 2 lines;
   VOL.5 reference kept so the §1.1 VOL.5 count stays 5 = core).
7. P1 agenda gloss → "Datas e horas: artigos das páginas 2 a 5." (348.2 px).
8. P1 agenda sub-head → "OS COMPROMISSOS" (376.8 px; was 484 px, past the box).
9. **P8-keys overflow (build 1, flow ended 2590)**: shortened 5 col-3 answer
   notes, each measured to 1 line: #133 "S + V + tempo", #134 "S + V + O +
   lugar", #135 "S + V + tempo + lugar", #136 "S + V + O + modo", #139
   "Ordinal 88e". Keys untouched; abbreviated forms keep ALL word-order
   elements. Flow ends 2550.
10. No P1-headline overflow: the pt bridge is 4 lines at 20.5 pt (ends 1441),
    but the shortened box (357 px) fits col 1 (1441 + 369 = 1810 ≤ 1828).
11. **Re-fanout fix2 D3:** P2 D-set option c → `"eten voor Sinterklaas' paard"`
    (core fix2 short form); clearance +71.9px.
12. **Re-fanout fix2 D5:** P4 HET PROGRAMMA box gained `"Stand Eredivisie na 12
    ronden: PSV 26, Feyenoord 25, Ajax 25 punten."` (5th fact, after Speelronde
    12, before Speelronde 13); box +73px.
13. **Re-fanout proof1 D1:** P6 `VOOR OF TEGEN?　A FAVOR OU CONTRA?` (+21.5px
    over the cream box) → `VOOR OF TEGEN?　A FAVOR / CONTRA` (+11.5 clearance,
    measured from the built SVG).
14. **Re-fanout proof1 D4 — type labels localized (task item 2):** the pt TYPES
    row in `scratch-fanout-nl/trans_table.py` had been copied from en (all
    English). Row fixed and all 144 English type tokens in the content files
    replaced: complete → `Completa a frase` (65), choice → `Escolha múltipla`
    (44), cloze choice → `Cloze` (13), matching → `Relaciona as palavras` (2),
    true or false → `Verdadeiro ou falso` (7; no `?` — the `?` belongs to the
    separate instr form only), make sentences → `Forma frases` (8), translate
    → `Traduzir` (4), writing → `Escrita` (1, incl. the `e_["type"] ==
    "Escrita"` comparison in content8.py:142, which must match or the P8
    answers loop breaks). Verified post-build: type-bracket counts in text.md
    are all Portuguese; English instr phrases 0 in the print PDF.
    NOTE: instr `Complete` ×59 is NOT leftover English — it is the Portuguese
    você-imperative of *completar*, deliberately mapped in the trans_table
    INSTRS pt row (parallel to es `Completar` ×59 and it `Completa`); the
    re-fanout check was corrected to scope type brackets only.
15. **Re-fanout proof1 O1:** P2 + P5 EN JIJ boxes bottom pad +20 → +22
    (proof-recommended hardening; both boxes end inside the cream rect).

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 3)

Rebuilt from the fixed core (D3 + D5 + D4 export + proof1 fixes §Fixes 11–15). Build only — no commit, no push. Logs: `hidden_files/w47/scratch-refanout-nl/` — `pt-build.log`, `pt-check.log`, `pt-creambox.log`, review `pt-review/` (p1–p8 + crops).

- D3 short form in P2, clearance +71.9px (x+adv 1790.1); D5 standings line in P4 box + text.md; D4 142 `— Resposta:` + 8 `(Resposta x)`, 答案 0; italic print=web=1.
- text.md diff vs build 2: exactly 293 changed lines (D3 2 + D5 1 + P6 title 2 + 144 type-label line-pairs) — no unintended changes.
- Gates (build 3): TOTAL 150, zero OVERFLOW / TOO WIDE; occlusion 0; p8 extract 150/150, compare CLEAN; freeze 8/8; print/web text posdiff 0, msdiff 0, all 8 pages (tokens 815/817/721/728/792/741/913/2372); pdftotext 46,693 B both; P8 font min=median 10.12pt, spans 188; chips core=edition {A2:8, B1:24, B2:3}; §1.1 clean.
- Creambox: 4 flags, all adjudicated non-overflow (true-ink probes on `cards/`, SVG is 1950×2700 so scale 1.0): P2 CREAM-BOTTOM EN JIJ `'em neerlandês e envia-as à redação.'` (bottom 1446.2 vs rect 1447.8) and P5 CREAM-BOTTOM `'em neerlandês e envia-as.'` (bottom 994.8 vs rect 994.5) both 0 dark pixels in the 7px strip below the box bottom; P2 PAGE-EDGE `Ligue palavra-significado` (advance right 1862.7) true ink rightmost pixel 1861, i.e. 1px INSIDE the 1862 content edge — advance-width side bearing, same pattern as es P6; P7 CREAM-RIGHT `HET WOORD　PALAVRA DA SEMANA` (advance right 1861.1 vs rect 1862.0) true ink 1861, inside by 1px — the flag is the 8px warning band only. 0 true overflow.
- 8-page visual pass: P1–P8 clean (P6 `A FAVOR / CONTRA` in box; P7 `PALAVRA DA SEMANA` in box; Portuguese instrs throughout — `Complete`, `Forme a frase`, `Verdadeiro ou falso?`, `Traduzir para português/neerlandês`, `Escreva`; P8 answers 1–150 complete).
- Known core item NOT in this build: core-nl re-proof (post-fix2) found D6/D7 — a Chinese full stop `。` orphaned alone on its own line on core P3 and P7. Core fix3 is being done by another agent; this edition gets a separate incremental rebuild then. This build is against core HEAD `5de7492f` only.
- Note (Q140, recorded not fixed): pt Q140 source `Faço uma surprise com um poema curto.` carries `curto`, but the key is `Ik maak een surprise met een gedicht.` without `kort` — same key-vs-source mismatch as en/fr/ja/ko/zh-tw; per coordinator instruction only es was corrected (see `es-proof-handoff-note.md`).

## Delta (core fix3 + fix4 + fix5, 2026-11-11, build 4)

Synced core-nl fix3 (D6/D7), fix4 (D8/D9/D10) and fix5 (D11) into this
edition. No commit, no push. Full record: `hidden_files/w47/scratch-delta-nl-pt/DELTA-LOG.md`.

- D6 P3 bridge `w=464.7` (width-scan band 416.7–512.7px, 0.1px steps,
  mid; 2 lines reproduced verbatim, p3 SVG byte-identical). D6/D7/D8/D10
  were pre-absent in this edition (no orphan/leading punctuation in the
  pre-fix SVGs); the sync is structural: mechanism copied, values
  re-measured from the pt text, never copied from the core.
- D7 P7 bridge `w=423.95` (band 415.7–432.2px, 3 lines verbatim, p7 SVG
  byte-identical).
- D8 P6 caption `capcn_w=378.1` (band 359.6–396.6px, 4 lines verbatim,
  p6 SVG byte-identical).
- D10 P7 letters `dt_zh_w=401.45` (band 356.3–446.6px, 2 lines verbatim,
  p7 SVG byte-identical).
- D9 Q140 key `Ik maak een surprise met een gedicht.` →
  `Ik maak een surprise met een kort gedicht.` (registry + text.md:415 +
  P8 node; stem `Faço uma surprise com um poema curto.` already had
  `curto`). This edition had NOT been fixed before (unlike es).
- D11 P4 HET PROGRAMMA box top reserve 62 → 89 (`sh` 611.0 → 638.0,
  bottom 1202.6 → 1229.6); last line `18:45 uur.` baseline 1209.49,
  margin +20.11px (true ink +20.60px cards / +20.48px print PDF 150dpi).
- `bslib4.py`: `Flow.para`/`Flow.bridge` gained the optional `w`
  wrap-width override (verbatim core fix3 mechanism).
- Build: `run.py` rc=0, TOTAL 150, 0 overflow; only `p4-sport.svg` and
  `p8-toets.svg` changed. Gates ALL PASS: occlusion 0; p8 extract
  150/150; p8 compare CLEAN, keydiff [137, 138] (translation items, by
  design); 3-way 149/149 MATCH (Q150 open-writing exception);
  freeze core baseline 8/8 + own repro 8/8; print/web text posdiff 0
  msdiff 0 all 8 pages; P8 font min 10.12pt; orphan sweep 0/0;
  creambox 4 flags, all adjudicated false positives; spill sweep 0;
  box-title true-ink scan 59 titles, 0 past the box/column outer edge.
- Old build-3 SHAs (history): print
  `e85aa1a01bea9c7894546e9e33f45f2c519f202f3404103dff59265f5daac834` /
  12,672,018 B; web
  `a0c8c87bd941fc87d945eac257053a482de7b1f1fc8a088070f3d66351146d85` /
  1,618,472 B; text
  `865e659fc2d4a9b1639c3513cd8e3326536feac8ae5fed14dca411d0cc137efc` /
  47,204 B.

## D5 rebuild (2026-11-12, B档 — explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader; REDO in top-level production)

- **Why a redo:** the first D5 worker (2026-11-12, `scratch-d5-rebuild-nl/`) rebuilt the `fanout-nl/` COPY, not this top-level production dir, and deleted its build-copy — production still held pre-D5 PDFs (print `dd74de0a…`, web `1c8b8a6c…`). This redo rebuilt from the current top-level build-4 sources in place. The copy's D5 SHAs (print `773eb8bb…` / 12,110,804 B) are superseded and do NOT describe production.
- **Pre-D5 baseline (top-level, verified on disk, `scratch-d5-redo-nl/2026-w47-nl-pt/baseline.txt`):** svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `dd74de0a45556e96fdfcc216a9d249bbae577ace249bfbc256dd564ef6e5113e` / 12,672,019 B; web `1c8b8a6c3ecccdb8a95268077cfc8b97b6c0750f80b112bdfb29d4180c2d59d3` / 1,618,464 B (KIT §Files delivered recorded a different web SHA `4e795b31…` — pre-existing drift, web rebuilt after KIT written); text `7e6b0c54dcb2f0025b90bd6074407d32ec24c8f6d78a018e4b49ae9d621f7d8f` / 47,209 B. Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by the build-4 sh=89 port), boxtitle 0 DEFECT, edge 0; census FAIL 497 Latin-in-CJK-sans. `run.py` pre-run reproduced the on-disk SVGs 8/8 byte-identical.
- **Install:** mechanism `apply_variant.py --target nl --reader pt` (mode latin), svglib md5 `78fdfbb037538b1f8a738434ea90a782` → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.
- **Ported core fixes (already in production before this rebuild):** P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11). P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt applied in this rebuild (core-nl D5 defect, same line here).
- **Defects found by the gates (all D5-caused, same class: bold-caps box titles widen in Newsreader SemiBold) — conclusions reused from the first worker's copy build, re-verified on the top-level rebuild; all fixed by size only, text unchanged:**
  1. P1 `DE WEEK IN CIJFERS　NÚMEROS` +7.2px → `f.box` tsize 23 → 22 (`content12.py:43`).
  2. P1 `IN DEZE EDITIE　NESTA EDIÇÃO` +21.5px → 24 → 22pt (`content12.py:90`).
  3. P2 `ZO ONTHOUD JE HET　LEMBRA-TE` +33.0px → `f.box` tsize 23 → 21 (`content12.py:177`).
  4. P2 TEXTX: `PAKJESAVOND IN VIER WOORDEN　PAKJESAVOND EM QUATRO PALAVRAS` overlapped right-anchored subtitle by 11.8×19.5px → head 28 → 27pt (`content12.py:213`).
  5. P6 `DE GRAFIEK　DADOS DE TREINO` +28.6px → 24 → 22pt (`content56.py:150`).
  6. P6 `VOOR OF TEGEN?　A FAVOR / CONTRA` +32.1px → 21 → 19pt (`content56.py:170`).
  7. P7 `HET WOORD　PALAVRA DA SEMANA` +57.1px → 23 → 19pt (`content7.py:84`).
- **Gates (final rebuild, after the 7 fixes, all in top-level production):** `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS 0 defects); `render.py` / `webpdf.py` RC 0; `p8.py extract` 150/150, `compare` vs core-nl CLEAN, keydiff=[137, 138] (reader-language keys, expected); `freeze.py baseline` 8/8 byte-identical; `freeze.py diff` vs core-nl: added CJK 7 (all U+3000); vs pre-D5 baseline: added CJK 0, added Latin strings 239 (run-splitting, expected); `occlusion_audit.py` 0 flags; `spill_sweep.py` 0 SPILL (39 OBSERVE); `boxtitle_check.py` 0 DEFECT; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` PASS 0 defects (P8 lines 240 → 240, footer slack 38.3px unchanged); `d5_census.py` PASS — D5 Latin 0, Cyrillic 0, curly-in-CJK 0; `census_quotes.py` 0 defective; text layer print = web = 46,598 bytes, word multiset diff 0; orphan sweep (a) 0, (b) 0.
- **New SHAs (lowercase, verified on production files):** print `dc43c521becb6e20ddc578dd544e8bd717bd07903aef4e5d4cb48939947bb326` (12,110,806 B); web `a5c9fd90831465afe86d9629d2e1cbe07d4875c0d9bdc983cdff4cd47bfc1f17` (1,542,942 B). **text.md unchanged:** 47,209 B, sha256 `7e6b0c54dcb2f0025b90bd6074407d32ec24c8f6d78a018e4b49ae9d621f7d8f`, byte-identical to the pre-D5 baseline.
- **Repro check (2026-11-12, third worker):** re-running `render.py` + `webpdf.py` in place reproduced the print PDF byte-identically (SHA unchanged); the web PDF rebuilt with a new SHA `b9e2c0d5b7f2bbfedc3a97fd1817d614c93b30e0480b8c2749d96d8769bcf07c` (1,542,946 B) — content-equivalent (pdftotext 46,598 B, identical; `textlayer.py` re-run RC 0, word multiset diff 0). Only embedded-font `head`-table checksums differ (stream-level diff on nl-de: 70 bytes in 18/126 streams). Web PDF SHA is not reproducible run to run (see build-7 note); "Files delivered" above is re-synced to the new production file; the SHA on the "New SHAs" line above is the rebuild's original output, kept as history (was `a5c9fd90831465afe86d9629d2e1cbe07d4875c0d9bdc983cdff4cd47bfc1f17`, 1,542,942 B).
- **Fix (2026-11-12, W47 nl repair, second worker):** PROOF-NOTE items 6 + 14 + 15. 6: `content8.py` 13 × `Cloze` → `Texto com lacunas` (cf. es `Texto con huecos`; label only in text.md — SVG grep 0 hits). 14: P1 kicker Portuguese part `O NEERLANDÊS QUE OS NEERLANDESES LEEM` → `TODAS AS SEMANAS EM NEERLANDÊS` (`content12.py:15`); pre-fix width model (Newsreader 12.75pt + 1.7px spacing) predicted the new total 563.6pt vs 628.2pt; measured in print P1: kicker now ends x=1014.6, date starts x=1039.5 → gap 24.9pt (was overlap 44.4pt, merged span `LEEMWEEK`); P1 visually confirmed on the render card — top line reads clean with a clear gap, no collision. 15: masthead line first token `WEEKBLAD IN HET NEDERLANDS` → `SEMANÁRIO NEERLANDÊS` (`content12.py:18`); the line is a per-edition string (es `SEMANARIO NEERLANDÉS` / it `SETTIMANALE OLANDESE` in the same position), consistent with this edition's H1 `Semanário neerlandês` and footer `SEMANÁRIO NEERLANDÊS VOL.4`; en edition untouched. Rebuilt: `run.py` TOTAL 150 RC 0, `render.py` RC 0, export dry-run to /tmp then re-exported (150 exercises, 8 golden, 6 gloss), `webpdf.py` RC 0. Exporter trap (ru FIX-LOG §7) fired twice: the fresh export dropped the `### ` prefix on lines 287 (`VOOR OF TEGEN?　A FAVOR / CONTRA`) and 360 (`HET WOORD　PALAVRA DA SEMANA`) — both backfilled by hand; final diff vs pre-fix text.md contains ONLY the 13 Cloze lines. Gates (`tools/gates.py`, ALL PASS): occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (reader-language keys, expected); freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages; pdftotext print = web = 46,588 B; P8 answer-zone min 10.12pt; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean. Extras: `boxtitle_check.py` 0 DEFECT, 0 OBSERVE, 0 marginal; `spill_sweep.py` 0 SPILL (39 OBSERVE); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `head_check.py` PASS 0 defects; `d5_creambox_audit.py` PASS 0 defects. Items 18/20 (P2/P6 tight box titles, +2.0/+2.4pt margins) NOT touched — coordinator ruling, known-tight, no overflow. **New SHAs (lowercase, verified on production files):** print `e2fe3b3a95686bd48e01a7975f62ee33bb821dd6a8a743c1a188bb8e6f119d37` (12,110,707 B); web `40c51869695b80e165661c6adb9309c70341342d56d632c472a7ba18f9ace508` (1,542,854 B); text.md `67516e2163c8c769ab9574b60b472c7d97706b3c4d89182bb95faa221513727a` (47,365 B). Logs: `hidden_files/w47/scratch-fix-nl/nl-pt/`.
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `svglib.py` (D5 install), `content12.py` (P2 head 25 → 23pt; 4 title sizes), `content56.py` (P6 titles 24 → 22pt, 21 → 19pt), `content7.py` (P7 title 23 → 19pt), `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-pt/` (`rebuild-1.log`, `run.log`, `render.log`, `webpdf.log`, `routing.log`, `post/` gates + `post.txt`, `pre/` pre-D5 gates, `baseline.txt`).
