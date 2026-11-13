# WEEKLY-KIT — 2026-W47 · nl → it (Italian readers)

Dutch weekly newspaper for Italian readers. Target language Dutch (nl), reader
native language Italian (it). VOL.4, issue 2026-11-16 – 2026-11-22. Target: 150
exercises (10/18/18/18/18/18/12/38 across pages 1–8); A2 46 / B1 73 / B2 31;
model essay 81 words.

## Source

Fan-out of the frozen Dutch core `production/2026-w47/core-nl/` (slug
`2026-w47-nl-zh-cn`). Dutch target text, facts, and answer keys are frozen; only
the explanation layer (glosses, notes, section subtitles, exercise type words)
was rewritten in Italian. No new trend research, no invented reader letters.

## Files delivered

- 8 SVGs (`svg/p1-voorpagina.svg` … `svg/p8-toets.svg`), 8 render cards (`cards/`)
- Print PDF: `De-Lucerna-VOL4-nl-it.pdf` — 12,102,273 bytes,
  sha256 `dc91af0aa78da597d0f3025087cd8695ccda1cb9ca454fc5445924e12bbe0059`
  (was build 6: 12,667,201 bytes,
  `4d297162d9e9f2ac99896ab2cf41865af0588d0d060ad76b89b3a7dabe44da15`)
- Web PDF: `De-Lucerna-VOL4-nl-it-web.pdf` — 1,534,364 bytes,
  sha256 `9eff96cf487a6beb5e26413ac9683bf771aac12f0ef9d6c2eca1de5b399fbf93`
  (was build 6: 1,610,244 bytes,
  `e2f6d07544458961b59020b7b54bb4114b041ab03cc542c78feb64a563d3ae11`)
  (via `tools/webpdf.py`, text layer pdftotext 46,365 B)
- Source export: `2026-w47-nl-it.text.md` — 47,194 bytes
  sha256 `e9880da2da990ad87348c650cc4f82637a108284d7929de2ed901019ef77ac0a` (current);
  (was build 5: 47,049 bytes,
  sha256 `f1d9e3f58b82e1bc0f9f51c52a1c7e14ac8bb69c87dd60a3d54df44bb44b781b`;
  old `62142f938c6a814297b5b4602a5a95ea0d7df38b1c4f86df5402a9a8dad629e8`)
  (142 single + 2 match headers + 8 match items = 150; 8 golden, 6 gloss)
- `ABSTRACT.txt` (Italian, one line, no ASCII double quotes)
- This KIT.

## Build record (final = build 3)

- `run.py` exit 0, TOTAL 150, **zero OVERFLOW / TOO WIDE warnings**.
  `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core);
  `flow[P8-keys] ended col 3/3 y=2533 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0 (< 7 MB).
- Gates (build 3): **ALL PASS** — occlusion 0 flags; p8 extract 150/150;
  p8 compare CLEAN, 0 key diffs; freeze direct sha256 8/8; print/web text
  posdiff 0 msdiff 0 on all 8 pages (P1 809/809 … P8 2344/2344); pdftotext
  print 46,461 B / web 46,461 B; P8 answer-zone min font 10.12 pt
  (median 10.12); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit
  clean (off-palette {}, VOL.5 = 5 = core, paper fills 8).
- Visual: all 8 cards viewed, clean. P1 numbers box fits col 1; P2 ZO ONTHOUD
  "RICORDA" fits; P6 chart head "DATI INVENTATI" fits and the VOOR OF TEGEN
  head "PRO O CONTRO?" fits; P7 BRIEVEN box ends above the ZINNEN rule;
  P8 answers 1–150 complete, pen photo in col 4.

## Fixes vs the generated fan-out (explanation layer only)

1. P1 subtitle → 36 pt, spacing 4 (W46 it; 1734 px < 1818 px limit).
2. Numbers-box title → "DE WEEK IN CIJFERS　IN CIFRE" (348 px).
3. Numbers-box items shortened ([2,1,2,2], total 357 px).
4. P6 chart head → "DE GRAFIEK　DATI INVENTATI" (346 px).
5. P2 box title → "ZO ONTHOUD JE HET　RICORDA".
6. P7 BRIEVEN glosses shortened to telegraphic W46 style (g1 2, g2 2 lines;
   VOL.5 reference kept so the §1.1 VOL.5 count stays 5 = core).
7. P1 agenda gloss → "Date e orari: articoli di pagina 2–5." (299.7 px).
8. P1 agenda sub-head → "GLI APPUNTAMENTI" (374.8 px; was 543 px, off-page).
9. P1 IN DEZE EDITIE head → "L'EDIZIONE" (331.6 px; was 441 px, past the box).
10. **P8-keys overflow (build 1, flow ended 2590)**: shortened 5 col-3 answer
    notes, each measured to 1 line: #133 "S + V + tempo", #134 "S + V + C +
    luogo", #135 "S + V + tempo + luogo", #136 "S + V + O + modo", #139
    "Ordinale 88e". Keys untouched; abbreviated forms keep ALL word-order
    elements. Flow ends 2533.
11. **P6 right-column head overflow (build 2, class 12th)**: "VOOR OF TEGEN?
    FAVOREVOLE O CONTRARIO?" (493 px, 4.5 px past the page edge) → "PRO O
    CONTRO?" (333.3 px). The same head in pt/ru/ja/ko/zh-tw was measured and
    fits (382/346/294/274/294 px) — no fix needed there.
12. No P1-headline overflow: the it bridge is 3 lines at 20.5 pt (ends 1411);
    the box (357 px) fits col 1 with 48 px to spare.
13. **Re-fanout fix2 (2026-11-11, proof1 D1/D3):** P7 `HET WOORD　PAROLA DELLA
    SETTIMANA` (+65.5px over) → `HET WOORD　PAROLA` (+147.5 clearance).
    4× U+2019 → U+0027 (content7.py 1 — golden sentence; content8.py 3 — #126
    note, #140 note, P8 answers header `l'esercizio`); post-build sweep:
    U+2018/U+2019/U+201C/U+201D = 0 in `content*.py`, `svg/`, `.text.md`, both
    PDF text layers. (The P8-header fix does not appear in the text.md diff —
    the header is page furniture, not exported.)
14. **Re-fanout fix2 D3:** P2 D-set option c → `"eten voor Sinterklaas' paard"`
    (core fix2 short form); clearance +71.9px.
15. **Re-fanout fix2 D5:** P4 HET PROGRAMMA box gained `"Stand Eredivisie na 12
    ronden: PSV 26, Feyenoord 25, Ajax 25 punten."` (5th fact, after Speelronde
    12, before Speelronde 13); box +73px.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 4)

Rebuilt from the fixed core (D3 + D5 + D4 export + proof1 fixes §Fixes 13–15). Build only — no commit, no push. Logs: `hidden_files/w47/scratch-refanout-nl/` — `it-build.log`, `it-check.log`, `it-creambox.log`, review `it-review/` (p1–p8 + crops).

- D3 short form in P2, clearance +71.9px (x+adv 1790.1); D5 standings line in P4 box + text.md; D4 142 `— Risposta:` + 8 `(Risposta x)`, 答案 0; italic print=web=1.
- text.md diff vs build 3: exactly 11 changed lines (D3 2 + D5 1 + P7 title 2 + 3 curly-quote line-pairs) — no unintended changes.
- Gates (build 4): TOTAL 150, by page 10/18/18/18/18/18/12/38, zero OVERFLOW / TOO WIDE; occlusion 0; p8 extract 150/150, compare CLEAN; freeze 8/8; print/web text posdiff 0, msdiff 0, all 8 pages (tokens 809/817/722/726/793/735/915/2344); pdftotext 46,500 B both; P8 font min=median 10.12pt, spans 185; chips core=edition {A2:8, B1:24, B2:3}; §1.1 clean.
- Creambox: 2 CREAM-BOTTOM flags, both pixel-probed 0 dark pixels in the 7px strip below the box bottom → false positives: P2 EN JIJ last line `'olandese e mandale alla redazione.'` (bottom 1446.2 vs rect 1445.8, no descenders) and P5 `'due frasi in olandese e mandale.'` (bottom 994.8 vs rect 994.5). 0 true overflow.
- 8-page visual pass: P1–P8 clean (P7 `PAROLA` in box; straight apostrophes in `l'articolo`, `un'antica`, P8 header `l'esercizio`; P7 BRIEVEN ends above the ZINNEN rule; P8 answers 1–150 complete).
- Known core item NOT in this build: core-nl re-proof (post-fix2) found D6/D7 — a Chinese full stop `。` orphaned alone on its own line on core P3 and P7. Core fix3 is being done by another agent; this edition gets a separate incremental rebuild then. This build is against core HEAD `5de7492f` only.
- Note (Q140, recorded not fixed): it Q140 source `Faccio una surprise con una poesia.` carries no qualifier, so its key matches — no defect in it. The same key-vs-source mismatch exists in en/fr/ja/ko/pt/zh-tw (see `es-proof-handoff-note.md`); per coordinator instruction only es was corrected.

## Re-fanout follow-up (proof1 c53043f4 late handoff, build 5, 2026-11-11)

Build 4 already contained the D1/D3 content fixes; build 5 adds the
**mechanism-level** fixes and the requested verification. Same core HEAD
`5de7492f` (fix2). Logs: `it-build5.log`, `it-check5.log`, `it-creambox5.log`,
`it-titles_h5.log`; before/after renders:
`scratch-refanout-nl/it-d1-d3-before-after/` (+ `BEFORE-AFTER-NOTE.md`).

- **D1 mechanism:** `scratch-fanout-nl/trans_table.py` it value
  `"HET WOORD　PAROLA DELLA SETTIMANA"` → `"HET WOORD　PAROLA"` (the table
  still held the long form; a future re-gen would have regressed). Rebuilt
  (build 5) and re-measured with PIL **true ink**: P7 title ink right 1714,
  box right 1862, clearance **+148px** (≤1862 required, ≥10px margin wanted).
  Before/after crops confirm: build 3 `SETTIMANA` on the newsprint, build 5
  `PAROLA` inside the cream box.
- **D3 mechanism:** the 4 U+2019 sources in `trans_table.py` also changed to
  U+0027 (1524 `un’antica`, 1616 `all’Eredivisie`, 1726 `un’espressione`,
  1792 `l’esercizio`); table U+2019 count 15 → 11. The remaining 11 are
  fr (7) / en (1) / it dead entry 1436 `c’erano` (not in this edition's
  content files — the BRIEVEN note is a rewritten short sentence) — all out
  of nl-it scope, untouched. Before/after crops confirm: `un’  antica` gap
  gone, `l’esercizio` tight. (Direction conflict with es-it fix1
  straight→curly is recorded in the before/after note for the coordinator;
  nl-it follows rendering evidence only, es-it untouched.)
- Build 5: TOTAL 150, zero OVERFLOW / TOO WIDE; gates ALL PASS (tokens
  809/817/722/726/793/735/915/2344; pdftotext 46,500 B both; P8 10.12pt
  spans 185; chips match; §1.1 clean). check_one ALL PASS (D3 +71.9, D5 ✓,
  D4 142 + 8, 答案 0, title PAROLA +147.5 advance, italic 1/1).
- Creambox: same 2 CREAM-BOTTOM flags as build 4, re-probed on build-5 cards:
  0 dark pixels → false positives. 0 true overflow.
- Horizontal box-title true-ink check (new tool `check_titles_h.py`, added
  per this handoff): 56 titles ALL PASS; P7 PAROLA +148.
- Print PDF and text.md are **byte-identical to build 4** (same SHAs). Web PDF
  differs by 7 bytes (1,610,232 vs 1,610,225 — webpdf font-subset
  nondeterminism; text layer identical, 46,500 B both, gates green).
- Visual: 8/8 clean again (P6 subtitle `un'antica` tight, P7 golden
  `un'antica` tight, P8 header `l'esercizio` tight, P7 `PAROLA` in box,
  P8 answers 1–150 complete).

## Delta (core fix3 + fix4 + fix5, 2026-11-11, build 6)

Incremental rebuild syncing core-nl fix rounds 3–5 (FIX-LOG.md) into this
edition. No commit, no push. Logs + gate evidence:
`hidden_files/w47/scratch-delta-nl-it/` (DELTA-LOG.md, rebuild/, gates/).

- Location note: the canonical edition directory
  `production/2026-w47/2026-w47-nl-it/` did not exist when this delta
  started (only the fan-out staging copy at
  `production/2026-w47/fanout-nl/2026-w47-nl-it/`); it was created by a
  byte-identical copy (`diff -r` clean) of that staging edition, and the
  staging copy was left untouched (its three SHAs re-verified after the
  promote: print `2520e5ad…`, web `609dc9a5…`, text.md `62142f93…`).
  All delta work happened in the canonical directory. The rebuild itself
  ran in a scratch copy (`scratch-delta-nl-it/rebuild/2026-w47-nl-it/`,
  OUT verified inside scratch before running); the rebuilt svg/cards/PDFs
  were promoted into the canonical directory only after all gates passed,
  and re-verified byte-identical to the scratch build there. The staging
  web PDF was never overwritten — only its text layer was compared.

- Pre-build finding (measured on the build-5 SVGs, before any edit):
  the D6/D7/D8/D10 orphan punctuation of the core does NOT occur in this
  edition — the Italian reader text reflows differently, and the full
  orphan sweep (both classes, CJK + Latin closers) was already 0/0 on
  all 8 pages. D6 bridge ends `hebben/zijn.` on line 2 of 2, D7 ends
  `scoren segnare.` on line 3 of 3, D8 caption is 4 clean lines ending
  `(100 giovani)`, D10 letters are 2 clean lines ending `VOL.5.`. The
  four w-syncs below are therefore structural (mechanism + locally
  scanned widths that reproduce the current clean wraps exactly); the
  rebuilt SVGs prove it — p3/p6/p7 are byte-identical to build 5. D9 and
  D11 were real defects here and are fixed for real.

- D6 (`bslib4.py` + `content34.py:78`): `Flow.para` / `Flow.bridge` take
  an optional `w` wrap-width override (default = column width, copied
  mechanism from core fix3); the HET PERFECTUM bridge passes `w=419.4`
  — width scan with this edition's own `wrap()` (0.1px steps, lower edge
  cross-checked analytically from line widths) gives band 399.9–438.9px
  for the current 2 lines, mid 419.4. Lines unchanged.
- D7 (`content7.py:19`): A2 VOETBALWOORDEN gloss bridge passes
  `w=432.7` — scan band 415.5–449.9px for the current 3 lines, mid
  432.7. Lines unchanged. (The band sits above the column width 422.5;
  the widest rendered line is 415.5px, so no overflow — the w is only a
  wrap width.)
- D8 (`content56.py:143–144, 156`): `capcn_w = 377.7` — scan band
  367.4–388.0px for the current 4 lines, mid 377.7; used in both the
  box-height computation and the `p.para` call. Box height unchanged.
- D9 (`content8.py:75` + text.md:415, two-piece): Q140 registry key
  `Ik maak een surprise met een gedicht.` →
  `Ik maak een surprise met een kort gedicht.` (Dutch target sentence,
  same in every edition) AND the Italian stem `Faccio una surprise con
  una poesia.` → `Faccio una surprise con una breve poesia.` — the
  stem must carry the «small» or the reader cannot derive `kort` from
  it (the nl-de D12 analogue: fixing the key alone leaves a stem that
  cannot produce the key). This supersedes the build-4 KIT note («no
  defect in it»): the coordinator's 2026-11-11 instruction is that the
  stem is fixed too. The note `surprise è un'espressione fissa` is
  unchanged. Re-exported registry + text.md: diff is exactly text.md
  line 415 (+11 bytes). Three-source check: registry key = text.md:415
  answer = P8 node.
- D10 (`content7.py:91–92, 100`): `dt_zh_w = 388.7` — scan band
  343.7–433.7px for the current 2 lines, mid 388.7; used in both the
  `lh` height computation and the `p.para` call. Box height unchanged.
- D11 (`content34.py:130`): P4 HET PROGRAMMA box top reserve 62 → 89
  (= 16 pad + 52 title block + 21 para y-offset). Facts wrap 3/3/3/2/3
  = 14 lines, as in the core. Box 611.0 → 638.0px, bottom 1202.6 →
  1229.6; last line `18:45 uur.` baseline 1209.49, margin +20.11px
  (was −6.89px). P3's SINTERKLAAS box (`content34.py:37`) untouched.

- Rebuild: `run.py` exit 0, TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31; `render.py` exit 0; `webpdf.py` exit 0
  (1,610,237 B < 7 MB); zero OVERFLOW / TOO WIDE warnings. SVG hashes
  vs build 5: only `p4-sport.svg` (D11) and `p8-toets.svg` (D9) changed;
  the other 6 are byte-identical.
- Gates (build 6): occlusion selftest OK, 0 flags; creambox/spill sweep
  0 spills (28 BELOW/ABOVE hits, all independent blocks at +24/+60px —
  section heads, captions, notes; the P4 D11 box has no below hit at
  all); 7px strip below every cream-box bottom: 0 non-paper pixels on
  the card PNGs; p8 extract 150/150; p8 compare vs core CLEAN, keydiff
  [137, 138] — the two translation items whose keys are reader-language
  by design, Italian here vs Chinese in core (pre-build keydiff was
  [137, 138, 140], D9 removed 140); 3-way registry/text.md/P8 compare
  149/149 MATCH, only Q150 differs (open-writing exception); freeze
  baseline (core control) 8/8; edition self-freeze (clean-dir re-run)
  8/8; print/web text content-multiset diff 0, positional diff 0 (0.3pt)
  all 8 pages (tokens 220/202/187/185/194/200/186/384 = 1,758);
  pdftotext print 46,510 B = web 46,510 B (staging 46,500 B; +10 = the
  D9 words, token diff vs staging is exactly the two changed P8 spans,
  nothing else); P8 answer-zone min font 10.12pt (≥ 10pt); orphan sweep
  (1451 line segments): class (a) 0 / class (b) 0, brute-force 0
  closer-leading elements. D11 double measurement: PIL 4× mask true ink
  bottom 1209.74 (margin +19.86px); delivered print-PDF 150dpi render
  lowest ink row 1209.60 (margin +20.00px), 7px strip below the box
  bottom 0 non-paper pixels.
- Visual: crops `crop-p4-programma.png` (`18:45 uur.` inside the box
  with clear margin), `crop-p8-q140.png` (`... met een kort gedicht.`),
  `crop-p8-q140-stem.png` (`... con una breve poesia. → ___`),
  `crop-p3-d6.png`, `crop-p7-d7.png`, `crop-p6-d8.png`,
  `crop-p7-d10.png` all confirmed by eye.

- New SHAs (build 6, lowercase) — old build-5 SHAs kept as history:
  print `4d297162d9e9f2ac99896ab2cf41865af0588d0d060ad76b89b3a7dabe44da15`
  (12,667,201 B; was `2520e5ad82096ef3c860e46b15934849faf2962ed8d61f885dc17151d2089826`,
  12,667,197 B); web `15d1b6480e5d3456b527f8f5f2e70b0afd6fa7d90e0b17e9e5ea145ddfe410f6`
  (1,610,237 B; was `609dc9a534f109e61d86a4a58d42b9dd4a2ef1673b2a78fb7abb5b668cf97f0c`,
  1,610,232 B); text.md `f1d9e3f58b82e1bc0f9f51c52a1c7e14ac8bb69c87dd60a3d54df44bb44b781b`
  (47,060 B; was `62142f938c6a814297b5b4602a5a95ea0d7df38b1c4f86df5402a9a8dad629e8`,
  47,049 B). Web PDF SHA/size are not reproducible run to run — only
  its text layer is compared (identical above).

## D5 rebuild (2026-11-12, B档 — explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader; REDO in top-level production)

- **Why a redo:** the first D5 worker (2026-11-12, `scratch-d5-rebuild-nl/`) rebuilt the `fanout-nl/` COPY, not this top-level production dir, and deleted its build-copy — production still held pre-D5 PDFs (print `4d297162…`, web `e2f6d075…`). This redo rebuilt from the current top-level build-6 sources in place. The copy's D5 SHAs (print `5a90aa6d…` / 12,102,400 B) are superseded and do NOT describe production.
- **Pre-D5 baseline (top-level, verified on disk, `scratch-d5-redo-nl/2026-w47-nl-it/baseline.txt`):** svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `4d297162d9e9f2ac99896ab2cf41865af0588d0d060ad76b89b3a7dabe44da15` / 12,667,201 B; web `e2f6d07544458961b59020b7b54bb4114b041ab03cc542c78feb64a563d3ae11` / 1,610,244 B (KIT §Files delivered recorded a different web SHA `15d1b648…` — pre-existing drift, web rebuilt after KIT written); text `f1d9e3f58b82e1bc0f9f51c52a1c7e14ac8bb69c87dd60a3d54df44bb44b781b` / 47,060 B. Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by the build-6 sh=89 port), boxtitle 0 DEFECT, edge 0; census FAIL 495 Latin-in-CJK-sans. `run.py` pre-run reproduced the on-disk SVGs 8/8 byte-identical.
- **Install:** mechanism `apply_variant.py --target nl --reader it` (mode latin), svglib md5 `78fdfbb037538b1f8a738434ea90a782` → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.
- **Ported core fixes (already in production before this rebuild):** P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11). P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt applied in this rebuild (core-nl D5 defect, same line here).
- **Defects found by the gates (all D5-caused, same class: bold-caps box titles widen in Newsreader SemiBold) — conclusions reused from the first worker's copy build, re-verified on the top-level rebuild; all fixed by size only, text unchanged:**
  1. P6 `VOOR OF TEGEN?　PRO O CONTRO?` +3.1px → 21 → 20pt (`content56.py:168`).
  2. P7 `PAS OP!　CLINICA DEGLI ERRORI` +8.1px → 23 → 22pt (`content7.py:73`).
- **Gates (final rebuild, after the 2 fixes, all in top-level production):** `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS 0 defects); `render.py` / `webpdf.py` RC 0; `p8.py extract` 150/150, `compare` vs core-nl CLEAN, keydiff=[137, 138] (reader-language keys, expected); `freeze.py baseline` 8/8 byte-identical; `freeze.py diff` vs core-nl: added CJK 7 (all U+3000); vs pre-D5 baseline: added CJK 0, added Latin strings 234 (run-splitting, expected); `occlusion_audit.py` 0 flags; `spill_sweep.py` 0 SPILL (39 OBSERVE); `boxtitle_check.py` 0 DEFECT, 1 marginal (P2 `RICORDA` 0.8px margin, ink inside — same as the copy build); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` PASS 0 defects (P8 lines 228 → 228, footer slack 41.7px unchanged); `d5_census.py` PASS — D5 Latin 0, Cyrillic 0, curly-in-CJK 0; `census_quotes.py` 0 defective; text layer print = web = 46,372 bytes, word multiset diff 0; orphan sweep (a) 0, (b) 0.
- **New SHAs (lowercase, verified on production files):** print `675f2bf33c42a74ff6991e72e5e27564b4b6d3abf8e84b94ae22a8d6d94ae437` (12,102,402 B); web `f042c93a0522a6c1d89c7747c12bcb4710d00c065ca38d318e182157b2cc01e7` (1,534,505 B). **text.md unchanged:** 47,060 B, sha256 `f1d9e3f58b82e1bc0f9f51c52a1c7e14ac8bb69c87dd60a3d54df44bb44b781b`, byte-identical to the pre-D5 baseline.
- **Repro check (2026-11-12, third worker):** re-running `render.py` + `webpdf.py` in place reproduced the print PDF byte-identically (SHA unchanged); the web PDF rebuilt with a new SHA `81a3ffaf8e8ea2d23b521e16c4a8f73db9d28d73c0ed17532711f22579b40833` (1,534,500 B) — content-equivalent (pdftotext 46,372 B, identical; `textlayer.py` re-run RC 0, word multiset diff 0). Only embedded-font `head`-table checksums differ (stream-level diff on nl-de: 70 bytes in 18/126 streams). Web PDF SHA is not reproducible run to run (see build-7 note); "Files delivered" above is re-synced to the new production file; the SHA on the "New SHAs" line above is the rebuild's original output, kept as history (was `f042c93a0522a6c1d89c7747c12bcb4710d00c065ca38d318e182157b2cc01e7`, 1,534,505 B).
- **Fix (2026-11-12, W47 nl repair, second worker):** PROOF-NOTE items 6 + 16 + 17. 6: `content8.py` 13 × `Cloze` → `Testo con lacune` (cf. es `Texto con huecos` / fr `Texte à trous`; label only in text.md — SVG grep 0 hits). 16: P2 heading `PAKJESAVOND IN QUATTRO PAROLE` → `PAKJESAVOND IN 4 PAROLE` (`content12.py:213`); measured in print P2: heading now ends x=797.1, question starts x=897.7 → gap 100.6pt (was overlap 1.8pt). 17: P2 cream-box title `ZO ONTHOUD JE HET　RICORDA` → `…　NOTA` (`content12.py:177`); measured: `NOTA` ends x=688.4, box edge 720.8 → 32.4pt margin (was overflow 0.5pt). Rebuilt: `run.py` TOTAL 150 RC 0, `render.py` RC 0, export dry-run to /tmp then re-exported (150 exercises, 8 golden, 6 gloss), `webpdf.py` RC 0. Exporter trap (ru FIX-LOG §7) fired once: the fresh export dropped the `### ` prefix on line 287 (`VOOR OF TEGEN?　PRO O CONTRO?`) — backfilled by hand; final diff vs pre-fix text.md contains ONLY the intended lines (73 NOTA, 83 4 PAROLE, 383–390 + 423–427 Testo con lacune). Gates (`tools/gates.py`, ALL PASS): occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (reader-language keys, expected); freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages; pdftotext print = web = 46,365 B; P8 answer-zone min 10.12pt; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean. Extras: `boxtitle_check.py` 0 DEFECT, 1 marginal — P6 `DATI INVENTATI` ink overhang 0.6px, within the tool's 1.0px tolerance (the old P2 `RICORDA` marginal is gone with the NOTA fix); `spill_sweep.py` 0 SPILL (39 OBSERVE); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `head_check.py` PASS 0 defects; `d5_creambox_audit.py` PASS 0 defects. **New SHAs (lowercase, verified on production files):** print `dc91af0aa78da597d0f3025087cd8695ccda1cb9ca454fc5445924e12bbe0059` (12,102,273 B); web `9eff96cf487a6beb5e26413ac9683bf771aac12f0ef9d6c2eca1de5b399fbf93` (1,534,364 B); text.md `e9880da2da990ad87348c650cc4f82637a108284d7929de2ed901019ef77ac0a` (47,194 B). Logs: `hidden_files/w47/scratch-fix-nl/nl-it/`.
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `svglib.py` (D5 install), `content12.py` (P2 head 25 → 23pt), `content56.py` (P6 title 21 → 20pt), `content7.py` (P7 title 23 → 22pt), `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-it/` (`rebuild-1.log`, `run.log`, `render.log`, `webpdf.log`, `routing.log`, `post/` gates + `post.txt`, `pre/` pre-D5 gates, `baseline.txt`).
