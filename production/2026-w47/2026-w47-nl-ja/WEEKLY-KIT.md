# WEEKLY-KIT — 2026-W47 · nl → ja (Japanese readers)

Dutch weekly newspaper for Japanese readers. Target language Dutch (nl), reader
native language Japanese (ja). VOL.4, issue 2026-11-16 – 2026-11-22. Target:
150 exercises (10/18/18/18/18/18/12/38 across pages 1–8); A2 46 / B1 73 / B2 31;
model essay 81 words.

## Source

Fan-out of the frozen Dutch core `production/2026-w47/core-nl/` (slug
`2026-w47-nl-zh-cn`). Dutch target text, facts, and answer keys are frozen; only
the explanation layer (glosses, notes, section subtitles, exercise type words)
was rewritten in Japanese. No new trend research, no invented reader letters.

## Files delivered

- 8 SVGs (`svg/p1-voorpagina.svg` … `svg/p8-toets.svg`), 8 render cards (`cards/`)
- Print PDF: `De-Lucerna-VOL4-nl-ja.pdf` — 18,803,540 bytes,
  sha256 `b886a483f64181624efef8f17c4d1a6d2e421571cf26c2de576f72b5682399b6`
  (larger than the Latin-script editions — embedded CJK fonts, same as the
  core's 25,955,551 B)
- Web PDF: `De-Lucerna-VOL4-nl-ja-web.pdf` — 1,967,732 bytes,
  sha256 `2b38c2547606d2a33b436cea4337acf4a93ddfbe4acdd93ef5533781d2755b7b`
  (via `tools/webpdf.py`, text layer pdftotext 47,840 B)
- Source export: `2026-w47-nl-ja.text.md` — 47,804 bytes,
  sha256 `b7e5f5dc8b484da52b0a22493149d93f0bbd3a0aeb79deb56b2f28e017a80084`
  (142 single + 2 match headers + 8 match items = 150; 8 golden, 6 gloss)
- `ABSTRACT.txt` (Japanese, one line, no ASCII double quotes)
- This KIT.

## Build record (final = build 1)

- `run.py` exit 0, TOTAL 150, **zero OVERFLOW / TOO WIDE warnings**.
  `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core);
  `flow[P8-keys] ended col 3/3 y=2504 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0 (< 7 MB).
- Gates (build 1): **ALL PASS** — occlusion 0 flags; p8 extract 150/150;
  p8 compare CLEAN, 0 key diffs; freeze direct sha256 8/8; print/web text
  posdiff 0 msdiff 0 on all 8 pages (P1 745/745 … P8 1600/1600); pdftotext
  print 47,855 B / web 47,854 B; P8 answer-zone min font 10.12 pt
  (median 10.12); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit
  clean (off-palette {}, VOL.5 = 5 = core, paper fills 8).
- Visual (build 1): all 8 cards viewed, clean. P1 numbers box fits col 1; P2 ZO ONTHOUD
  "こう覚えよう" fits and the GEDICHT strip gloss fits its box; P6 chart
  head "グラフ（練習データ）" fits; P7 BRIEVEN box ends above the
  ZINNEN rule; P8 answers 1–150 complete, pen photo in col 4. (The build-1 note
  "403 px, 2.5 px past the box edge" was the advance-width estimate — the re-fanout
  true-ink probe puts the ink's right edge at 1846, 16px INSIDE the 1862 edge.)

## Fixes vs the generated fan-out (explanation layer only)

1. P1 subtitle → 36 pt, spacing 8 kept (W46's 36/11.5 spills at 1857 px;
   36/8 measures 1686 px < 1818 px limit).
2. Numbers-box title → "DE WEEK IN CIJFERS　今週の数字" (367 px).
3. Numbers-box items shortened ([2,1,2,2], total 357 px).
4. P6 chart head kept "DE GRAFIEK　グラフ（練習データ）" (403 px; W46 shipped).
5. P2 box title kept "ZO ONTHOUD JE HET　こう覚えよう" (399 px, fits).
6. P7 BRIEVEN glosses shortened to telegraphic W46 style (g1 2, g2 2 lines;
   VOL.5 reference kept so the §1.1 VOL.5 count stays 5 = core).
7. No P1-headline overflow: the ja bridge is 3 lines at 20.5 pt (ends 1411);
   the box (357 px) fits col 1 with 48 px to spare. No P8-keys overflow:
   Japanese notes are compact (flow ends 2504).
8. **Re-fanout fix2 D3:** P2 D-set option c → `"eten voor Sinterklaas' paard"`
   (core fix2 short form); clearance +71.9px.
9. **Re-fanout fix2 D5:** P4 HET PROGRAMMA box gained `"Stand Eredivisie na 12
   ronden: PSV 26, Feyenoord 25, Ajax 25 punten."` (5th fact, after Speelronde
   12, before Speelronde 13); box +73px.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 2)

Rebuilt from the fixed core (D3 + D5 + D4 export only — no edition-level proof fixes beyond the core). Build only — no commit, no push. Logs: `hidden_files/w47/scratch-refanout-nl/` — `ja-build.log`, `ja-check.log`, `ja-creambox.log`, review `ja-review/` (p1–p8 + crops).

- D3 short form in P2, clearance +71.9px (x+adv 1790.1); D5 standings line in P4 box + text.md; D4 142 `— 答え：` + 8 `(答え x)`, 答案 0; italic print=web=1.
- text.md diff vs build 1: exactly 3 changed lines (D3 2 + D5 1) — no unintended changes.
- Gates (build 2): TOTAL 150, zero OVERFLOW / TOO WIDE; occlusion 0; p8 extract 150/150, compare CLEAN; freeze 8/8; print/web text posdiff 0, msdiff 0, all 8 pages (tokens 745/706/665/661/683/647/734/1600); pdftotext 47,919 B both; P8 font min=median 10.12pt, spans 561 (CJK renders as many small spans); chips core=edition {A2:8, B1:24, B2:3}; §1.1 clean.
- Creambox: 6 flags, all adjudicated non-overflow (true-ink probes on `cards/`, scale 1.0): P2 CREAM-RIGHT `ZO ONTHOUD JE HET　こう覚えよう` (right 955.6 vs rect 961.0, inside by 5.4px) is the 8px warning band only; P2 CREAM-BOTTOM EN JIJ last line `'…編集部に送ろう。'` (bottom 1417.8 vs rect 1416.8, 1.0px past) and P5 CREAM-BOTTOM `'…送ろう。'` (bottom 966.4 vs rect 965.5, 0.9px past) both 0 dark pixels in the 7px strip below the box bottom — the checker's bottom includes a 0.3×size descent allowance, but the last lines end in `。` with no descenders, so no ink is actually below the rect; P6 PAGE-EDGE + CREAM-RIGHT `DE GRAFIEK　グラフ（練習データ）` (advance right 1864.8, 2.8px past the 1862 edge) true ink rightmost pixel 1846, i.e. 16px INSIDE the edge — the advance-width metric overstates CJK full-width parens/bearings by ~19px, superseding the build-1 "2.5 px past" note; P6 CREAM-BOTTOM `'れる？（若者100人）'` (bottom 689.4 vs rect 691.0, inside) 0 dark pixels in the strip. 0 true overflow.
- 8-page visual pass: P1–P8 clean (P1 HET WOORD note 2 lines, ends above the IN HET KORT rule; P6 chart head inside its box; P7 BRIEVEN ends above the ZINNEN rule; P8 answers 1–150 complete).
- ABSTRACT `De` (proof1 D2) deliberately NOT fixed: all 101 W47 ABSTRACT.txt files use bare "Lucerna" except core-nl; the pt proof adjudicated bare "Lucerna VOL.4" as the family convention, and the it proof passed its ABSTRACT. One prover's strict reading vs family convention + another prover's ruling — left unchanged, flagged for the coordinator.
- Known core item NOT in this build: core-nl re-proof (post-fix2) found D6/D7 — a Chinese full stop `。` orphaned alone on its own line on core P3 and P7. Core fix3 is being done by another agent; this edition gets a separate incremental rebuild then. This build is against core HEAD `5de7492f` only.
- Note (Q140, recorded not fixed): ja Q140 source `小さな詩つきのプレゼント…` carries the qualifier, but the key lacks `kort` — same key-vs-source mismatch as en/fr/ko/pt/zh-tw; per coordinator instruction only es was corrected (see `es-proof-handoff-note.md`).

## Delta (core fix3 + fix4 + fix5, 2026-11-11, build 6)

Core-nl fix3 (D6/D7) + fix4 (D8/D9/D10) + fix5 (D11) synced to this edition.
Only this edition's own sources changed; core untouched, staging copy
(`fanout-nl/2026-w47-nl-ja/`, build-5 control) untouched. No commit, no push.
Logs + gate evidence: `hidden_files/w47/scratch-delta-nl-ja/` (DELTA-LOG.md,
GATE-LOG.md, width-scan.py/log, gates/, crops).

- Pre-fix (build 5, verified on disk): D6 P3 bridge 2 lines
  `現在完了形で補おう。助動詞hebben／zijnに` / `注意。` (2303.5/2333.22);
  D7 P7 bridge 3 lines ending `する。` (785.11); D8 P6 caption 3 lines
  (635.02/659.44/683.86); D10 P7 letters 2 lines (1783.77/1812.17) — none
  orphaned, so D6/D7/D8/D10 are structural syncs only (mechanism copied,
  widths rescanned on this edition's own text, chosen w exactly reproduces
  the current splits: p3/p6/p7 SVGs byte-identical after rebuild).
  D9 Q140: registry key, text.md:415 answer and P8 node all read
  `Ik maak een surprise met een gedicht.` (missing `kort`) — real defect;
  stem `小さな詩つきのプレゼントを作ります。` already contains 小さな, so
  only the key changed. D11 P4 box: bottom 1202.6, last line `18:45 uur.`
  baseline 1209.49, +6.89px below the box — real defect.
- Width scan (own text + own `svglib.wrap()`, 0.1px steps; core numbers never
  copied): D6 band 412.8–430.0 → w=421.4; D7 band 414.9–430.0 → w=422.45;
  D8 band 369.5–387.7 → capcn_w=378.6 (3 lines kept); D10 band 378.0–397.9
  → dt_zh_w=387.95 (2 lines kept); D11 facts 3/3/3/2/3 = 14 lines,
  sh 611.0 → 638.0 (top reserve 62 → 89 = 16 + 52 + 21).
- D11 re-measurement: box bottom 1229.6, last baseline 1209.49, margin
  +20.11px; PIL true ink bottom y=1208.74, margin +20.86px; card 1× lowest
  text-ink row 1209 (+20.6px), 7px strip below box bottom 0 non-paper
  pixels; print PDF 150dpi same strip 0 non-paper pixels.
  `P4 col3 ends 1229.6`; exercises hline at y=1608, clearance 378.40px.
- Gates (build 6): run.py rc=0 TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31, 0 FLOW OVERFLOW / HEAD TOO WIDE; occlusion 0 flags;
  p8 extract 150/150; p8 compare vs core CLEAN, keydiff [137, 138] (the two
  translation items whose keys are reader-language by design, Japanese here
  vs Chinese in core; pre-build keydiff was [137, 138, 140], D9 removed
  140); 3-way registry/text.md/P8 compare 149/149 MATCH, only Q150 differs
  (open-writing exception); freeze baseline (core control) 8/8; edition
  self-freeze (clean-dir re-run) 8/8; print/web text posdiff 0 msdiff 0 all
  8 pages (tokens 745/706/665/661/683/647/734/1600); pdftotext print
  47,924 B = web 47,924 B; P8 answer-zone min font 10.12pt (≥ 10pt),
  spans 561; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean.
  Orphan sweep (PIL + svglib advances, 1444 lines): class (a) 0 / class (b)
  0 both methods, brute-force 0 leftmost closer-leading elements — same
  0/0 pre-fix, 0 new. Creambox: same 6 flags as build 5, unchanged
  (P2 CREAM-RIGHT + 2 CREAM-BOTTOM, P5 CREAM-BOTTOM, P6 PAGE-EDGE +
  CREAM-RIGHT + CREAM-BOTTOM — all adjudicated non-overflow in build 2,
  P4 D11 box 0 flags). Spill sweep: 0 spills; P4 box has no below hit.
- Visual: crops `crop-p3-d6.png`, `crop-p7-d7.png`, `crop-p4-programma.png`
  (`18:45 uur.` inside the box with clear margin), `crop-p8-q140.png`
  (`... met een kort gedicht.`) all confirmed by eye.

- New SHAs (build 6, lowercase) — old build-5 SHAs kept as history:
  print `f78ffe324aaf24d39fa71cc815b96d6c163cf2747c27a10d7633e94cb41943b0`
  (26,049,309 B; was `40e58eb248ea12da5d52e592f582e44bbf35246a17df05c8d27240d492446e49`,
  26,049,308 B); web `b4d4501b8665d0adee4b8484a66a8bd17031ee4953f397e7c0142b7b0ee4762b`
  (2,155,389 B; was `3c60dddbd2f917d99c82a447d9964a3f72a42ca8c9243465949eba9e65f4ae49`,
  2,155,388 B); text.md `060bfdea243483edb1a30691ff26291eac1a90bc69f2ea4c38fe97eac05bb93a`
  (47,801 B; was `e890ba135c8c5ad2873d41bbf9133a23ece29bdf08f7a1f6686765e9beb0dcf6`,
  47,796 B). Web PDF SHA/size are not reproducible run to run — only
  its text layer is compared (identical above).

## D5 rebuild (2026-11-12, B档 — explanation-layer Latin rendered in Newsreader instead of Noto Sans CJK; REDO in top-level production)

- **Why a redo:** the first D5 worker (2026-11-12, `scratch-d5-rebuild-nl/`) never started the CJK reader editions (only empty scratch dirs). This is the first D5 build of this edition, done in place in top-level production.
- **Pre-D5 baseline (top-level, verified on disk, `scratch-d5-redo-nl/2026-w47-nl-ja/baseline.txt`):** svglib md5 `ae9985696bf2f828e53eab9894d73cb4`; print `f78ffe324aaf24d39fa71cc815b96d6c163cf2747c27a10d7633e94cb41943b0` / 26,049,309 B; web `591836f2de9ddf6609658c0fe101e6cfad60d4aa49aa4287989a3815be40248a` / 2,155,393 B (KIT §Files delivered recorded a different web SHA `b4d4501b…` / 2,155,389 B — pre-existing drift, web rebuilt after KIT written); text `060bfdea243483edb1a30691ff26291eac1a90bc69f2ea4c38fe97eac05bb93a` / 47,801 B. Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by the build-6 sh=89 port), boxtitle 1 DEFECT (P6 `DE GRAFIEK　グラフ（練習データ）` +2.5px, pre-existing), edge 0; census FAIL 336 Latin-in-CJK-sans. `run.py` pre-run reproduced the on-disk SVGs 8/8 byte-identical.
- **Install:** mechanism `apply_variant.py --target nl --reader ja` (mode cjk — character-script routing, no `_READER_LANG` gate, per CJK-DECISION §1; CJK index SC → JP; kinsoku already present), svglib md5 `ae9985696bf2f828e53eab9894d73cb4` → `910444d24366a0cc60c970e49847dcea`. Routing assert: FAILURES 0.
- **Ported core fix:** P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 6).
- **Defects found by the gates (rebuild-1, all D5-caused — the widened Latin head pushes the CJK tail out of the box; same class as the en-ja pilot) — all fixed by size only, text unchanged:**
  1. HEAD TOO WIDE [P2-feature]: `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt (`content12.py:175`; core-nl D5 defect, same line).
  2. P2 `ZO ONTHOUD JE HET　こう覚えよう` over +21.0px → `f.box` tsize 23 → 21 (`content12.py:177`).
  3. P6 `DE GRAFIEK　グラフ（練習データ）` over +25.6px (was +2.5px pre-D5) → 24 → 21pt (`content56.py:148`).
- **Gates (final rebuild-2, after the 3 fixes, all in top-level production):** `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS 0 defects); `render.py` / `webpdf.py` RC 0; `p8.py extract` 150/150, `compare` vs core-nl CLEAN, keydiff=[137, 138] (reader-language keys, expected); `freeze.py baseline` 8/8 byte-identical; `freeze.py diff` vs core-nl: added CJK 3315 (Japanese text now in Noto Sans CJK JP, expected); vs pre-D5 baseline: added CJK 0, added Latin strings 216 (run-splitting, expected); `occlusion_audit.py` 0 flags; `spill_sweep.py` 0 SPILL (67 OBSERVE); `boxtitle_check.py` 0 DEFECT; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` PASS 0 defects (P8 lines 230 → 230, footer slack 39.4px unchanged); `d5_census.py` PASS — D5 Latin 0, Cyrillic 0, curly-in-CJK 0; `census_quotes.py` 0 defective; text layer print = web = 47,834 bytes, word multiset diff 0; orphan sweep (a) 0, (b) 0.
- **New SHAs (lowercase, verified on production files):** print `67aeebb40b5820193277cfea8a05b075849612f4d2e7e75a4e021485953702bc` (18,803,852 B); web `6840df0c1e61710d944b539a10241e6b1ae480f4702eff0bbb2bbc9f51d1714d` (1,968,009 B). **text.md unchanged:** 47,801 B, sha256 `060bfdea243483edb1a30691ff26291eac1a90bc69f2ea4c38fe97eac05bb93a`, byte-identical to the pre-D5 baseline.
- **Repro check (2026-11-12, third worker):** re-running `render.py` + `webpdf.py` in place reproduced the print PDF byte-identically (SHA unchanged); the web PDF rebuilt with a new SHA `9a4b3dbd5dad2ec271e699d39e49c2820af4d7c2770e172bb61b68fe9700af07` (1,968,007 B) — content-equivalent (pdftotext 47,834 B, identical; `textlayer.py` re-run RC 0, word multiset diff 0). Only embedded-font `head`-table checksums differ (stream-level diff on nl-de: 70 bytes in 18/126 streams). Web PDF SHA is not reproducible run to run (see build-7 note); "Files delivered" above is re-synced to the new production file; the SHA on the "New SHAs" line above is the rebuild's original output, kept as history (was `6840df0c1e61710d944b539a10241e6b1ae480f4702eff0bbb2bbc9f51d1714d`, 1,968,009 B).
- **Fix (2026-11-12, W47 nl repair, second worker):** PROOF-NOTE items 1 + 3 landed by the first worker (Q140 サプライズ, Q135/136 全角＋); item 2 was partial — P2 band subtitle `靴とパッケスアフォント` still old form (content12.py:165). Fixed to `靴とパッケスアーフォント`; print PDF now has new form ×7, old form ×0 (full-text count). Rebuilt: `run.py` TOTAL 150 RC 0, `render.py` RC 0, export dry-run to /tmp byte-identical to shipped text.md (band is furniture, excluded from export) then re-exported (150 exercises, 8 golden, 6 gloss), `webpdf.py` RC 0. Gates (`tools/gates.py`, ALL PASS): occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (reader-language keys, expected); freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages; pdftotext print = web = 47,840 B; P8 answer-zone min 10.12pt; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean. Extras: `boxtitle_check.py` 0 DEFECT; `spill_sweep.py` 0 SPILL (67 OBSERVE); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `head_check.py` PASS 0 defects; `d5_creambox_audit.py` PASS 0 defects. **New SHAs (lowercase, verified on production files):** print `b886a483f64181624efef8f17c4d1a6d2e421571cf26c2de576f72b5682399b6` (18,803,540 B); web `2b38c2547606d2a33b436cea4337acf4a93ddfbe4acdd93ef5533781d2755b7b` (1,967,732 B); text.md `b7e5f5dc8b484da52b0a22493149d93f0bbd3a0aeb79deb56b2f28e017a80084` (47,804 B, unchanged by this round). Logs: `hidden_files/w47/scratch-fix-nl/nl-ja/`.
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `svglib.py` (D5 install, mode cjk), `content12.py` (P2 head 25 → 23pt; P2 box tsize 21), `content56.py` (P6 title 24 → 21pt), `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-ja/` (`rebuild-1.log`, `rebuild-2.log`, `run.log`, `render.log`, `webpdf.log`, `routing.log`, `post/` gates + `post.txt`, `pre/` pre-D5 gates, `baseline.txt`).
