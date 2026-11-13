# WEEKLY-KIT — 2026-W47 · nl → ko (Korean readers)

Dutch weekly newspaper for Korean readers. Target language Dutch (nl), reader
native language Korean (ko). VOL.4, issue 2026-11-16 – 2026-11-22. Target:
150 exercises (10/18/18/18/18/18/12/38 across pages 1–8); A2 46 / B1 73 / B2 31;
model essay 81 words.

## Source

Fan-out of the frozen Dutch core `production/2026-w47/core-nl/` (slug
`2026-w47-nl-zh-cn`). Dutch target text, facts, and answer keys are frozen; only
the explanation layer (glosses, notes, section subtitles, exercise type words)
was rewritten in Korean. No new trend research, no invented reader letters.

## Files delivered

- 8 SVGs (`svg/p1-voorpagina.svg` … `svg/p8-toets.svg`), 8 render cards (`cards/`)
- Print PDF: `De-Lucerna-VOL4-nl-ko.pdf` — 13,871,386 bytes,
  sha256 `e7fa69a263fe85ef08205ac654e55e2333f590de5f6bd6f1ea73103150746bff`
  (CJK fonts embedded)
- Web PDF: `De-Lucerna-VOL4-nl-ko-web.pdf` — 1,791,786 bytes,
  sha256 `218aebe12b4ba140a0180cfdd3fcb2719547737f1e7c59682aca83a57fed231a`
  (via `tools/webpdf.py`, text layer pdftotext 47,512 B)
- Source export: `2026-w47-nl-ko.text.md` — 47,576 bytes,
  sha256 `e13db87160d1477972824431d9f4e194f90f53a53b7954e659cc74484801f537`
  (142 single + 2 match headers + 8 match items = 150; 8 golden, 6 gloss)
- `ABSTRACT.txt` (Korean, one line, no ASCII double quotes)
- This KIT.

## Build record (final = build 1)

- `run.py` exit 0, TOTAL 150, **zero OVERFLOW / TOO WIDE warnings**.
  `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core);
  `flow[P8-keys] ended col 3/3 y=2472 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0 (< 7 MB).
- Gates (build 1): **ALL PASS** — occlusion 0 flags; p8 extract 150/150;
  p8 compare CLEAN, 0 key diffs; freeze direct sha256 8/8; print/web text
  posdiff 0 msdiff 0 on all 8 pages (P1 733/733 … P8 1639/1639); pdftotext
  print 47,558 B / web 47,557 B; P8 answer-zone min font 10.12 pt
  (median 10.12); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit
  clean (off-palette {}, VOL.5 = 5 = core, paper fills 8).
- Visual: all 8 cards viewed, clean. P1 numbers box fits col 1; P2 ZO ONTHOUD
  "기억해요" fits and the GEDICHT strip gloss fits its box; P6 chart head
  "그래프(연습 데이터)" fits; P7 BRIEVEN box ends above the ZINNEN rule;
  P8 answers 1–150 complete, pen photo in col 4.

## Fixes vs the generated fan-out (explanation layer only)

1. P1 subtitle → 36 pt, spacing 11.5 (W46 ko; 1428 px < 1818 px limit).
2. Numbers-box title → "DE WEEK IN CIJFERS　이번 주 숫자" (371 px).
3. Numbers-box items shortened ([2,1,2,2], total 357 px).
4. P6 chart head kept "DE GRAFIEK　그래프(연습 데이터)" (365 px, fits).
5. P2 box title → "ZO ONTHOUD JE HET　기억해요" (was 416 px, 11.5 px over).
6. P7 BRIEVEN glosses shortened (g1 2 lines; g2 3 lines with a lower ly=1330
   so the box still ends at 1927, above the ZINNEN rule; VOL.5 reference
   kept so the §1.1 VOL.5 count stays 5 = core).
7. No P1-headline overflow: the ko bridge is 3 lines at 20.5 pt (ends 1411);
   the box (357 px) fits col 1 with 48 px to spare. No P8-keys overflow:
   Korean notes are compact (flow ends 2472).
8. **Re-fanout fix2 D3:** P2 D-set option c → `"eten voor Sinterklaas' paard"`
   (core fix2 short form); clearance +71.9px.
9. **Re-fanout fix2 D5:** P4 HET PROGRAMMA box gained `"Stand Eredivisie na 12
   ronden: PSV 26, Feyenoord 25, Ajax 25 punten."` (5th fact, after Speelronde
   12, before Speelronde 13); box +73px.
10. **Re-fanout proof1 D7 (task item 5):** P2 EN JIJ Korean gloss orphan period —
    the gloss was reflowed by dropping `함께`, so it now wraps to 3 lines with
    the last line ending `...편집부에 보내세요.` (period attached, verified
    visually on the P2 card + with the ko svglib `wrap()`). No orphan `.` left.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 2)

Rebuilt from the fixed core (D3 + D5 + D4 export + proof1 D7 fix). Build only — no commit, no push. Logs: `hidden_files/w47/scratch-refanout-nl/` — `ko-build.log`, `ko-check.log`, `ko-creambox.log`, review `ko-review/` (p1–p8 + crops).

- D3 short form in P2, clearance +71.9px (x+adv 1790.1); D5 standings line in P4 box + text.md; D4 142 `— 정답：` + 8 `(정답 x)`, 答案 0; italic print=web=1.
- text.md diff vs build 1: exactly 5 changed lines (D3 2 + D5 1 + gloss 2) — no unintended changes.
- Gates (build 2): TOTAL 150, zero OVERFLOW / TOO WIDE; occlusion 0; p8 extract 150/150, compare CLEAN; freeze 8/8; print/web text posdiff 0, msdiff 0, all 8 pages (tokens 733/713/668/667/695/657/754/1639); pdftotext 47,613 B both; P8 font min=median 10.12pt, spans 613 (CJK renders as many small spans); chips core=edition {A2:8, B1:24, B2:3}; §1.1 clean.
- Creambox: 3 flags, all CREAM-BOTTOM, all pixel-probed 0 dark pixels in the 7px strip below the box bottom → false positives (descent-allowance artifacts on descender-free last lines): P2 EN JIJ `'...편집부에 보내세요.'` (bottom 1417.8 vs rect 1416.8), P5 EN JIJ `'...써서 보내세요.'` (bottom 966.4 vs rect 965.5), P6 `'은이 100명)'` (bottom 689.4 vs rect 691.0, inside). 0 true overflow.
- 8-page visual pass: P1–P8 clean (P2 EN JIJ gloss ends `...편집부에 보내세요.` with the period attached — D7 fixed; P6 chart head + `찬성? 반대?` in boxes; P7 BRIEVEN ends above the ZINNEN rule; P8 answers 1–150 complete).
- Known core item NOT in this build: core-nl re-proof (post-fix2) found D6/D7 — a Chinese full stop `。` orphaned alone on its own line on core P3 and P7. Core fix3 is being done by another agent; this edition gets a separate incremental rebuild then. This build is against core HEAD `5de7492f` only.
- Note (Q140, recorded not fixed): ko Q140 source `작은 시가 담긴…` carries the qualifier, but the key lacks `kort` — same key-vs-source mismatch as en/fr/ja/pt/zh-tw; per coordinator instruction only es was corrected (see `es-proof-handoff-note.md`).

## Delta (core fix3 + fix4 + fix5, 2026-11-11, build 3)

Synced core-nl fix3 (D6/D7) + fix4 (D8/D9/D10) + fix5 (D11) into this edition.
Build only — no commit, no push. Full record: DELTA-LOG.md in
`hidden_files/w47/scratch-delta-nl-ko/`. New SHAs (build 3, also in
"Files delivered" above): print `c4f446b9…42d537d` / 17,281,343 B;
web `75f6730e…ae1176e` / 1,919,772 B;
text `75fbaa30…31105dd9` / 47,585 B.
Old SHAs (build 2, history): print `aaeeba2c…5113bd` / 17,281,343 B;
web `ed38e32f…4065d5` / 1,919,763 B; text `1d103d29…31fe408` / 47,580 B.

- D6 (P3 bridge, `content34.py:78`): pre-existing clean — 2 lines, no orphan.
  Structural sync only: `bslib4.py` gained the fix3 `w` mechanism
  (`Flow.para`/`Flow.bridge` optional `w`); bridge call passes `w=414.35`
  (width-scan band 405.0–423.7px, 0.1px step, mid). Lines verbatim, p3 SVG
  byte-identical.
- D7 (P7 bridge, `content7.py:19`): pre-existing clean — 2 lines, final `.`
  attached. Call passes `w=423.65` (window band 417.3–430.0px, mid; true
  upper edge 530.1). Lines verbatim, p7 SVG byte-identical.
- D8 (P6 caption, `content56.py`): pre-existing clean — 3 lines, no
  line-initial punctuation. `capcn_w=380.7` (band 376.6–384.8px, mid), used
  in the box-height computation and the `p.para` call. Lines/baselines
  unchanged, p6 SVG byte-identical.
- D9 (Q140): real fix. Registry key + text.md:415 answer + P8 node all now
  `Ik maak een surprise met een kort gedicht.` (was missing `kort`). Stem
  `작은 시가 담긴…` already carries "small"; note unchanged.
- D10 (P7 letters, `content7.py`): pre-existing clean — 2 lines, no
  line-initial punctuation. `dt_zh_w=376.3` (band 364.9–387.7px, mid), used
  in `lh` and the `p.para` call. Lines/baselines unchanged, p7 SVG
  byte-identical. (Narrowing past 364.8 would itself create a line-initial
  `.` — hence the midpoint, not the edge.)
- D11 (P4 HET PROGRAMMA, `content34.py:130`): real fix. Top reserve 62 → 89
  (= 16 pad + 52 title block + 21 para y-offset); box 611.0 → 638.0,
  bottom 1202.6 → 1229.6; last line `18:45 uur.` baseline 1209.49, margin
  **+20.11px**; true-ink margins +20.60px (cards 1×) / +20.48px (print PDF
  150dpi); 7px strip below the box: 0 ink on both renders.
- Gates (build 3): run.py rc=0, TOTAL 150, zero OVERFLOW / TOO WIDE;
  occlusion 0; p8 extract 150/150; p8 compare CLEAN, keydiff [137, 138]
  (translation keys, by design; 140 fixed out); 3-way registry vs text.md
  vs P8 **149/149 MATCH** (+ Q150 open-writing exception); freeze core
  baseline 8/8 + edition self-freeze 8/8; print/web text posdiff 0 msdiff 0
  all 8 pages (tokens 733/713/668/667/695/657/754/1640); pdftotext 47,618 B
  both; P8 answer font min 10.12pt; orphan sweep (a)=0/(b)=0, 1427 lines,
  brute-force leftmost 0; creambox 3 flags, same as build 2, all false
  positives (7px strips 0 ink); spill sweep 0 spills; §1.1 clean;
  boxtitle true-ink scan 58 titles, 1 OVER — P8 `A　VUL DE KRONIEK IN`
  −26.5px, **pre-existing** (head element byte-identical to staging;
  same numbers in nl-en), out of D6–D11 scope, left for proof1/coordinator.
- SVG changes vs build 2: only `p4-sport.svg` (D11) and `p8-toets.svg`
  (D9). text.md diff vs build 2: exactly line 415 (`kort `, +5 B).

## D5 rebuild (2026-11-12, B档 — explanation-layer Latin rendered in Newsreader instead of Noto Sans CJK; REDO in top-level production)

- **Why a redo:** the first D5 worker (2026-11-12, `scratch-d5-rebuild-nl/`) never started the CJK reader editions (only empty scratch dirs). This is the first D5 build of this edition, done in place in top-level production.
- **Pre-D5 baseline (top-level, verified on disk, `scratch-d5-redo-nl/2026-w47-nl-ko/baseline.txt`):** svglib md5 `51f469d99e12dd041ed171fc401ea648`; print `c4f446b9adc06c29be6a047abf30c83a445062bc26335a578a9609afb42d537d` / 17,281,343 B; web `f0c2cc079a5c8330ca6153206e7202ea424e25d295d7ae8333a3935265e8b7bc` / 1,919,763 B (KIT §Files delivered recorded a different web SHA `75f6730e…` / 1,919,772 B — pre-existing drift, web rebuilt after KIT written); text `75fbaa3004d0da29ce096953bd584b891afc2daee6a2bffa8d7cd7fe31105dd9` / 47,585 B. Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by the build-3 sh=89 port), boxtitle 0 DEFECT, edge 0; census FAIL 333 Latin-in-CJK-sans. `run.py` pre-run reproduced the on-disk SVGs 8/8 byte-identical.
- **Install:** mechanism `apply_variant.py --target nl --reader ko` (mode cjk — character-script routing, no `_READER_LANG` gate, per CJK-DECISION §1; CJK index already KR), svglib md5 `51f469d99e12dd041ed171fc401ea648` → `956ddfde0e783827b69304f80ddb98af`. Routing assert: FAILURES 0.
- **Ported core fix:** P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 3).
- **Defects found by the gates (rebuild-1):** exactly one — HEAD TOO WIDE [P2-feature]: `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt (`content12.py:175`; core-nl D5 defect, same line). No box-title defect: all 39 titles fit after the install (the Korean tails are short; cf. ja, where the same class produced 2 defects).
- **Freeze gate note:** `freeze.py baseline` ran under `tools/venv/bin/python` with RC=0 (8/8 byte-identical) — the task's system-python3 fallback for a ko freeze ABORT was NOT needed.
- **Gates (final rebuild-2, after the 1 fix, all in top-level production):** `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS 0 defects); `render.py` / `webpdf.py` RC 0; `p8.py extract` 150/150, `compare` vs core-nl CLEAN, keydiff=[137, 138] (reader-language keys, expected); `freeze.py baseline` 8/8 byte-identical; `freeze.py diff` vs core-nl: added CJK 3447 (Korean text now in Noto Sans CJK KR, expected); vs pre-D5 baseline: added CJK 0, added Latin strings 215 (run-splitting, expected); `occlusion_audit.py` 0 flags; `spill_sweep.py` 0 SPILL (123 OBSERVE); `boxtitle_check.py` 0 DEFECT (39 titles, 492 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` PASS 0 defects (P8 lines 229 → 229, footer slack 54.0px unchanged); `d5_census.py` PASS — D5 Latin 0, Cyrillic 0, curly-in-CJK 0; `census_quotes.py` 0 defective (KR quotes not a defect per task); text layer print = web = 47,521 bytes, word multiset diff 0; orphan sweep (a) 0, (b) 0.
- **New SHAs (lowercase, verified on production files):** print `fd8daad8ba7eeee962fdd0479c389a36d8c435b2fc78d2262f87c23ceeeee039` (13,871,308 B); web `7dd70f00993ae30759fc1e9d3ecd9f8f05c5e0075ab255dbb185c83943953fe0` (1,791,909 B). **text.md unchanged:** 47,585 B, sha256 `75fbaa3004d0da29ce096953bd584b891afc2daee6a2bffa8d7cd7fe31105dd9`, byte-identical to the pre-D5 baseline.
- **Repro check (2026-11-12, third worker):** re-running `render.py` + `webpdf.py` in place reproduced the print PDF byte-identically (SHA unchanged); the web PDF rebuilt with a new SHA `694720afc0ccf6ebfb7f3800b22aaa114c097d4b85c79c369a58d8fb457db974` (1,791,910 B) — content-equivalent (pdftotext 47,521 B, identical; `textlayer.py` re-run RC 0, word multiset diff 0). Only embedded-font `head`-table checksums differ (stream-level diff on nl-de: 70 bytes in 18/126 streams). Web PDF SHA is not reproducible run to run (see build-7 note); "Files delivered" above is re-synced to the new production file; the SHA on the "New SHAs" line above is the rebuild's original output, kept as history (was `7dd70f00993ae30759fc1e9d3ecd9f8f05c5e0075ab255dbb185c83943953fe0`, 1,791,909 B).
- **Fix (2026-11-12, W47 nl repair; items 4 + 5 landed by the first worker, verified by the second worker):** 4: Pakjesavond name unified to `팍예스아폰트` — golden line (text.md:371) `파크예스아본트` → `팍예스아폰트`; `ABSTRACT.txt` likewise now `팍예스아폰트`. Print full-text count: `팍예스아폰트` present, `파크예스아본트` 0. 5: Q135/Q136 separators ` + ` → `·` (both had ASCII ` + ` in the pre-fix file, not only Q135). Parenthesis spacing (`Berlijn(11월 16일` etc.) NOT changed: full-print scan finds 25 no-space-before-`(` cases across many distinct strings — a systemic edition habit, not a single template source (task ruling). Gates re-run by the second worker (`tools/gates.py`, ALL PASS): occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (reader-language keys, expected); freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages; pdftotext print = web = 47,512 B; P8 answer-zone min 10.12pt; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean. Extras: `boxtitle_check.py` 0 DEFECT, 0 OBSERVE, 0 marginal; `spill_sweep.py` 0 SPILL (123 OBSERVE); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `head_check.py` PASS 0 defects (first worker's run.log); `d5_creambox_audit.py` PASS 0 defects. **New SHAs (lowercase, verified on production files):** print `e7fa69a263fe85ef08205ac654e55e2333f590de5f6bd6f1ea73103150746bff` (13,871,386 B); web `218aebe12b4ba140a0180cfdd3fcb2719547737f1e7c59682aca83a57fed231a` (1,791,786 B); text.md `e13db87160d1477972824431d9f4e194f90f53a53b7954e659cc74484801f537` (47,576 B). Logs: `hidden_files/w47/scratch-fix-nl/nl-ko/`.
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `svglib.py` (D5 install, mode cjk), `content12.py` (P2 head 25 → 23pt), `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-ko/` (`rebuild-1.log`, `rebuild-2.log`, `run.log`, `render.log`, `webpdf.log`, `routing.log`, `post/` gates + `post.txt`, `pre/` pre-D5 gates, `baseline.txt`).
