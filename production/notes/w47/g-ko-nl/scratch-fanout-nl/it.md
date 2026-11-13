# it (Italian readers) — 2026-W47 nl fan-out

COMPLETE 2026-11-11 (build 3 final).

## Deliverables

- Print PDF `De-Lucerna-VOL4-nl-it.pdf`: 12,715,556 bytes,
  sha256 `a05cc4be4048cc23b357d9f0d35e03725ff68a80f082ecec46249ee42175ab3c`
- Web PDF `De-Lucerna-VOL4-nl-it-web.pdf`: 1,575,654 bytes,
  sha256 `072c7f2e808ad6c93cd5469f981b14688432cab0fc8794a1260e3d5c58301fe9`
- `.text.md`: 46,851 bytes (142 single + 2 match headers + 8 match items = 150;
  8 golden, 6 gloss)
- `ABSTRACT.txt` (Italian, one line, no ASCII double quotes) + `WEEKLY-KIT.md`

## Gates (build 3) — ALL PASS

occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze
direct sha256 8/8; print/web text posdiff 0 msdiff 0 (8/8 pages); pdftotext
print 46,461 B / web 46,461 B; P8 answer-zone min font 10.12 pt; P8 chips =
core {A2: 8, B1: 24, B2: 3}; §1.1 SVG clean (off-palette {}, VOL.5 = 5 = core).

## Build

- `run.py` exit 0, TOTAL 150, zero OVERFLOW / TOO WIDE warnings.
- `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core).
- `flow[P8-keys] ended col 3/3 y=2533 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0.

## Visual — 8/8 clean

P1 numbers box fits col 1; P2 ZO ONTHOUD "RICORDA" fits; P6 chart head and
VOOR OF TEGEN head fit; P7 BRIEVEN box ends above the ZINNEN rule; P8 answers
1–150 complete, pen photo in col 4.

## Fixes (explanation layer only; Dutch text, facts, keys untouched)

1. Subtitle → 36 pt / spacing 4 (W46 it). Numbers title → "IN CIFRE".
   Numbers items shortened ([2,1,2,2]). P6 head → "DATI INVENTATI".
   ZO ONTHOUD → "RICORDA".
2. P7 BRIEVEN glosses → W46-telegraphic (g1 2, g2 2 lines; VOL.5 kept).
3. P1 agenda gloss → "Date e orari: articoli di pagina 2–5." (299.7 px).
4. P1 agenda sub-head → "GLI APPUNTAMENTI" (374.8 px; was 543 px).
5. P1 IN DEZE EDITIE head → "L'EDIZIONE" (331.6 px; was 441 px).
6. **P8-keys overflow (build 1)**: flow ended 2590. Shortened 5 col-3 answer
   notes to 1 line: #133 "S + V + tempo", #134 "S + V + C + luogo", #135
   "S + V + tempo + luogo", #136 "S + V + O + modo", #139 "Ordinale 88e".
   Flow ends 2533.
7. **P6 right-column head overflow (build 2)**: "VOOR OF TEGEN?　FAVOREVOLE O
   CONTRARIO?" (493 px, 4.5 px past the page edge) → "PRO O CONTRO?"
   (333.3 px). Same head in pt/ru/ja/ko/zh-tw measured and fits — no fix.
8. No P1-headline overflow: it bridge is 3 lines at 20.5 pt (ends 1411); the
   box (357 px) fits col 1 with 48 px to spare.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 4)

Rebuilt from fixed core (D3 + D5 + D4 export + proof1 D1/D3 fixes). Build only, no commit/push. Logs: `scratch-refanout-nl/it-{build,check,creambox}.log`, review `it-review/`.

- D3 short form in P2, clearance +71.9px; D5 standings line in P4 box + text.md; D4 142 `— Risposta:` + 8 `(Risposta x)`, 答案 0; italic print=web=1.
- Title: P7 `PAROLA` +147.5 (from `PAROLA DELLA SETTIMANA` +65.5 over).
- Curly quotes: 4× U+2019 → U+0027 (golden + #126 + #140 + P8 header `l'esercizio`); post-build sweep 0 in content files, svg/, text.md, both PDF text layers.
- text.md diff vs build 3: exactly 11 lines (D3 2 + D5 1 + title 2 + 3 quote pairs; the P8-header quote is page furniture, not in text.md).
- Gates: occlusion 0, p8 150/150 CLEAN, freeze 8/8, print/web text diff 0 (tokens 809/817/722/726/793/735/915/2344), pdftotext 46,500 B both, P8 10.12pt, chips A2:8/B1:24/B2:3, §1.1 clean.
- Creambox: 2 CREAM-BOTTOM flags pixel-probed 0 dark pixels → false positives (P2 + P5 EN JIJ). 0 true overflow.
- Visual: 8/8 pages clean.

## Deliverables (re-fanout build 4, core HEAD `5de7492f`)

- Print PDF `De-Lucerna-VOL4-nl-it.pdf`: 12,667,197 bytes,
  sha256 `2520e5ad82096ef3c860e46b15934849faf2962ed8d61f885dc17151d2089826`
- Web PDF `De-Lucerna-VOL4-nl-it-web.pdf`: 1,610,225 bytes,
  sha256 `a54bb92d9802b1704ad0f629b97853dd792aa18fb8f71f3c6ecfcf2b2d985e9b`
- `2026-w47-nl-it.text.md` (47,049 B), `ABSTRACT.txt`, `WEEKLY-KIT.md` (Re-fanout §)

Status: COMPLETE — all gates pass, 8/8 pages + 3 crops viewed clean. Core fix3 (D6/D7 orphan 。) NOT included — separate incremental rebuild pending.

## Re-fanout follow-up (build 5, proof1 c53043f4 late handoff, 2026-11-11)

- Mechanism fixes in `scratch-fanout-nl/trans_table.py`: it HET WOORD value
  `"HET WOORD　PAROLA DELLA SETTIMANA"` → `"HET WOORD　PAROLA"`; 4 it U+2019
  sources → U+0027 (1524 `un’antica`, 1616 `all’Eredivisie`, 1726
  `un’espressione`, 1792 `l’esercizio`). Table U+2019 15 → 11 (rest: fr 7,
  en 1, it dead entry 1436 `c’erano` — not in this edition, untouched).
- Build 5 (core HEAD `5de7492f`): TOTAL 150, gates ALL PASS, check_one ALL
  PASS, creambox 2 flags re-probed 0 dark pixels (false positives), titles_h
  56 titles ALL PASS. P7 PAROLA PIL true-ink right 1714, clearance +148.
- Print PDF + text.md byte-identical to build 4 (same SHAs); web PDF
  1,610,232 B, sha256
  `609dc9a534f109e61d86a4a58d42b9dd4a2ef1673b2a78fb7abb5b668cf97f0c`
  (7 B larger than build 4 — webpdf subset nondeterminism, text layer identical).
- Visual: 8/8 clean again. Before/after renders kept in
  `scratch-refanout-nl/it-d1-d3-before-after/` (D1 hetwoord, D3 un'antica +
  l'esercizio, es P6 chart-head zoom, BEFORE-AFTER-NOTE.md).
- Horizontal box-title true-ink check (`check_titles_h.py`, new): all 10
  editions run — 9 completed + zh-tw: 56 titles each, 0 FAIL. Tightest:
  es P6 chart head +0 (solid ink 1861, 1px inside; only a 1px antialiased
  fringe touches the edge — not an overflow, no fix), pt P7 +1, ru P6 +10,
  en P7 / fr P6 / ja P2 +13. (First version misattributed sibling ink on
  shared baselines — P2 table headers, P1 numbers title; fixed to probe each
  text's own advance span, re-run 0 FAIL.)
- Status: COMPLETE (build 5). Core fix3 (D6/D7 orphan 。) NOT included — separate
  incremental rebuild pending. NEW: P6 chart-caption gloss 。 at line start
  (`。問題：你在鞋裡放什麼？`) is still in the current core f567bcea and in
  zh-tw — fix3 did not cover it; flagged for coordinator.
