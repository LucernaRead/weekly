# ja (Japanese readers) — 2026-W47 nl fan-out

COMPLETE 2026-11-11 (build 1 final).

## Deliverables

- Print PDF `De-Lucerna-VOL4-nl-ja.pdf`: 26,049,268 bytes,
  sha256 `af010c1f2d2f0d39a61417aa3ace0bc02e9e20fcece5e4181314721a5361c1b1`
  (CJK fonts embedded, like the core's 25,955,551 B)
- Web PDF `De-Lucerna-VOL4-nl-ja-web.pdf`: 2,119,188 bytes,
  sha256 `07243a6bc87aee40eeb1b03b4967e7917db835d709a0245e86678fac2dbd1d2f`
- `.text.md`: 47,592 bytes (142 single + 2 match headers + 8 match items = 150;
  8 golden, 6 gloss)
- `ABSTRACT.txt` (Japanese, one line, no ASCII double quotes) + `WEEKLY-KIT.md`

## Gates (build 1) — ALL PASS

occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze
direct sha256 8/8; print/web text posdiff 0 msdiff 0 (8/8 pages); pdftotext
print 47,855 B / web 47,854 B; P8 answer-zone min font 10.12 pt; P8 chips =
core {A2: 8, B1: 24, B2: 3}; §1.1 SVG clean (off-palette {}, VOL.5 = 5 = core).

## Build

- `run.py` exit 0, TOTAL 150, zero OVERFLOW / TOO WIDE warnings.
- `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core).
- `flow[P8-keys] ended col 3/3 y=2504 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0.

## Visual — 8/8 clean

P1 numbers box fits col 1; P2 ZO ONTHOUD "こう覚えよう" fits, GEDICHT strip
gloss fits its box; P6 chart head fits (403 px, 2.5 px past the box edge,
W46-shipped, invisible); P7 BRIEVEN box ends above the ZINNEN rule; P8
answers 1–150 complete, pen photo in col 4.

## Fixes (explanation layer only; Dutch text, facts, keys untouched)

1. Subtitle → 36 pt / spacing 8 kept (W46's 36/11.5 spills at 1857 px).
   Numbers title → "今週の数字". Numbers items shortened ([2,1,2,2]).
2. P6 chart head kept "グラフ（練習データ）" (W46 shipped). ZO ONTHOUD kept
   "こう覚えよう".
3. P7 BRIEVEN glosses → W46-telegraphic (g1 2, g2 2 lines; VOL.5 kept).
4. No P1-headline overflow (bridge 3 lines, ends 1411; box 357 px fits col 1).
   No P8-keys overflow (Japanese notes compact; flow ends 2504).

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 2)

Rebuilt from fixed core (D3 + D5 + D4 export only; no edition-level proof fixes beyond the core). Build only, no commit/push. Logs: `scratch-refanout-nl/ja-{build,check,creambox}.log`, review `ja-review/`.

- D3 short form in P2, clearance +71.9px; D5 standings line in P4 box + text.md; D4 142 `— 答え：` + 8 `(答え x)`, 答案 0; italic print=web=1.
- text.md diff vs build 1: exactly 3 lines (D3 2 + D5 1).
- Gates: occlusion 0, p8 150/150 CLEAN, freeze 8/8, print/web text diff 0 (tokens 745/706/665/661/683/647/734/1600), pdftotext 47,919 B both, P8 10.12pt, spans 561, chips A2:8/B1:24/B2:3, §1.1 clean.
- Creambox: 6 flags, all adjudicated non-overflow by true-ink probes (scale 1.0): P2 ZO ONTHOUD title inside by 5.4px (band only); P2+P5 EN JIJ bottom strips 0 dark pixels (descent allowance artifact, last lines end in 。 with no descenders); P6 chart head advance 1864.8 but true ink rightmost 1846 — 16px INSIDE the edge (advance overstates CJK parens/bearings ~19px; supersedes build-1 "2.5 px past" note); P6 bottom strip 0 dark pixels. 0 true overflow.
- Visual: 8/8 pages clean.
- ABSTRACT `De` (proof1 D2) deliberately NOT fixed — family convention is bare "Lucerna" (101 W47 abstracts; pt proof adjudicated it as convention, it proof passed). Flagged for coordinator.
- Q140 recorded not fixed (key lacks `kort`; source has 小さな詩) — coordinator scope: es only.

## Deliverables (re-fanout build 2, core HEAD `5de7492f`)

- Print PDF `De-Lucerna-VOL4-nl-ja.pdf`: 26,049,308 bytes (CJK fonts embedded),
  sha256 `40e58eb248ea12da5d52e592f582e44bbf35246a17df05c8d27240d492446e49`
- Web PDF `De-Lucerna-VOL4-nl-ja-web.pdf`: 2,155,388 bytes,
  sha256 `3c60dddbd2f917d99c82a447d9964a3f72a42ca8c9243465949eba9e65f4ae49`
- `2026-w47-nl-ja.text.md` (47,796 B), `ABSTRACT.txt`, `WEEKLY-KIT.md` (Re-fanout §)

Status: COMPLETE — all gates pass, 8/8 pages + 4 crops viewed clean. Core fix3 (D6/D7 orphan 。) NOT included — separate incremental rebuild pending.
