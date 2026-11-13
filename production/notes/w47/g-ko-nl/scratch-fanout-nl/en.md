# W47 nl fan-out — nl-en (English reader) — builder record

Slug: `2026-w47-nl-en` · VOL.4 · issue 2026-11-16–2026-11-22 · build dir
`~/workspace/weekly-git/production/2026-w47/fanout-nl/2026-w47-nl-en/`
Built from frozen core `production/2026-w47/core-nl/` (slug `2026-w47-nl-zh-cn`).
Explanation layer: English. Dutch target text, facts, answer keys untouched.

## Fixes applied (explanation-layer only, deletion-only shortening)

All five were found by the pre-build sweep + 8-page visual pass; every one
follows the W46 nl-en precedent where one exists.

1. P1 subtitle clipped (36pt/spacing=8 → 2145px > 1950): `content12.py`
   subtitle → 34pt, spacing=0 (W46 en; measured 1557px).
2. P1 numbers box jumped to col 2 (box 465px > 417 cliff): shortened the
   four English parentheticals → `"(16 Nov: Germany–Netherlands)"`,
   `"(kick-off)"`, `"(8 points each)"`, `"(5 December, in 19 days)"`;
   items now [2,1,2,2] = 7 lines, box 357px; P1-headline ends col 2 y=1465
   (as core). Zero FLOW OVERFLOW.
3. Numbers-box title spilled 502px → `DE WEEK IN CIJFERS　IN NUMBERS`
   (395.8px, inside the box).
4. P6 chart head off-page (ink to x=1963): `DE GRAFIEK　THE CHART`
   (297px); the "(PRACTICE DATA)" disclosure is redundant — the caption
   below already says "Practice data: made-up numbers, for practice only,
   not a real survey."
5. P2 box title spilled 532px → `ZO ONTHOUD JE HET　REMEMBER`
   (W46 en precedent).
6. **P7 BRIEVEN box overflow (found on visual pass, build 5):** the col-3
   box bottom measured 2014px, 77px past the ZINNEN rule (y=1937); the
   rule struck through the box between its text lines. Core ends 1898.
   Cause: the English glosses are longer than the core's Chinese ones.
   Fix: shortened the two English glosses to
   `No real letters yet — so, an example.` (1 line) and
   `Editor's example, not a real letter. Send yours — we print them in VOL.5!`
   (2 lines). Box bottom now 1928 (9px above the rule); last text line
   ends ~1904. Same defect class found by `p7check.py` in de/fr/es/it/pt/
   ru/ja/ko (zh-tw clean at 1898) and fixed there pre-build with the
   W46 telegraphic style; `p7check.py` in scratch-fanout-nl/.

## Fix1 (2026-11-11, proof1 D1 + same-class residual) — build 8

- Proof1 found 1 defect (D1): P7 BRIEVEN gloss `Editor’s` used U+2019, wide
  glyph in Noto Sans CJK SC ("Editor' s"). Fixed in `content7.py` lines 92
  + 101 (wrap calc + render call): U+2019 → U+0027.
- Same full-sweep also found the only other curly quotes in the edition:
  P1 word-of-the-week gloss `“Group win”` (`content12.py` line 113,
  U+201C/U+201D), reader-visible in the same sans font, rendering with the
  same wide gaps (verified on a crop of the build-7 P1 render). Fixed to
  straight ASCII `"` (string re-quoted with single quotes). No other
  changes; proof observation items O1–O7 untouched.
- Post-fix sweep: U+2018/U+2019/U+201C/U+201D/U+201A/U+201E/U+2032/U+2033
  = 0 in `content*.py`, `svg/`, `.text.md`, and both PDF text layers.
- Re-rendered whole edition (build 8): run.py rc=0 TOTAL 150, zero
  OVERFLOW / TOO WIDE / WARNING; P7 col3 still ends 1927.5.
- P1 gloss + P7 BRIEVEN crops from the build-8 print PDF visually
  verified (straight quotes, no wide gaps; BRIEVEN box still above the
  ZINNEN rule).

## Gates (final build 8)

- run.py exit 0, TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31, essay 81 words, zero OVERFLOW / TOO WIDE.
- occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN (0 key diffs);
  freeze direct sha256 8/8; print/web text posdiff 0 msdiff 0 on all 8 pages
  (tokens 795/830/738/724/807/748/915/2318); pdftotext print 45,404B /
  web 45,409B; P8 answer-zone min = median 10.12pt; P8 chips
  core = edition {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean
  (off-palette {}, VOL.5 = 5 = core). VOL.4 ×10 in print text layer.
- `.text.md` exported from source: 45,074 B; 142 single + 2 match headers
  + 8 match items = 150; 8 golden, 6 gloss. CJK only 答案×150 +
  full-width spaces; no Chinese remnants.

## Visual pass (all 8 cards)

- P1 clean; P2 clean (ZO ONTHOUD fix verified); P3 clean; P4 clean;
  P5 clean; P6 clean (chart head fits box); P7 clean after the BRIEVEN
  fix (box ends above the ZINNEN rule); P8 clean (exercises 113–150
  continuous, answers 1–150 complete, pen photo in col 4).

## Deliverables (final build 8)

- Print PDF `De-Lucerna-VOL4-nl-en.pdf`: 12,665,899 bytes,
  sha256 `2cc431f2572abad8790d1b99d6211d3aa87a5278a4052f3f0810dd6d764b0b58`
- Web PDF `De-Lucerna-VOL4-nl-en-web.pdf`: 1,574,228 bytes,
  sha256 `0fc6232bbe2bd8d3794169d83b4c233df519845f07eef1f9f35e2fdada2f6d18`
- `2026-w47-nl-en.text.md` (45,074 B), `ABSTRACT.txt`, `WEEKLY-KIT.md`

Status: COMPLETE — all gates pass, 8/8 cards viewed clean, fix1 applied
(D1 + P1 curly quotes), awaiting second-round full proofread.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 9)

Rebuilt from fixed core (D3 + D5 + D4 export + proof2-en1 D1 note shortening). Build only, no commit/push. Logs: `scratch-refanout-nl/en-{build,render,export,webpdf,gates,check,creambox}.log`, review `en-review/`.

- D3 short form in P2, clearance +71.9px (x+adv 1790.1); D5 standings line in P4 box (col3 ends 1202.6); D4 142 `— Correct:` + 8 `(Correct x)`, 答案 0; italic print=web=1.
- text.md diff vs build 8: exactly 5 lines (note 2 + D3 2 + D5 1).
- Gates: occlusion 0, p8 150/150 CLEAN, freeze 8/8, print/web text diff 0 (tokens 790/828/738/735/807/748/915/2318), pdftotext 45,429 B both, P8 10.12pt, chips A2:8/B1:24/B2:3, §1.1 clean.
- Creambox: 2 CREAM-BOTTOM flags pixel-probed 0 dark pixels → false positives (P2 EN JIJ, P5). 0 true overflow.
- Visual: 8/8 pages clean (P1 note now 1 line above the y=1853 rule; P2 c. line fits; P4 box with new line).

## Deliverables (re-fanout build 9, core HEAD `5de7492f`)

- Print PDF `De-Lucerna-VOL4-nl-en.pdf`: 12,665,902 bytes,
  sha256 `3352492cf30e965d8249c55638f0ed73d4e07c0a4a97d61f4c9aa55c696a693c`
- Web PDF `De-Lucerna-VOL4-nl-en-web.pdf`: 1,610,568 bytes,
  sha256 `2589cac4102d70f9041138f3c67a0176eff726a770cc89034ebd9c8905e39a06`
- `2026-w47-nl-en.text.md` (45,106 B), `ABSTRACT.txt`, `WEEKLY-KIT.md` (§7 re-fanout)

Status: COMPLETE — all gates pass, 8/8 pages + 3 crops viewed clean. Core fix3 (D6/D7 orphan 。) NOT included — separate incremental rebuild pending.
