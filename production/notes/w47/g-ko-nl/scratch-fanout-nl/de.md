# de (German readers) — 2026-W47 nl fan-out

COMPLETE 2026-11-11 (build 5 final).

## Deliverables

- Print PDF `De-Lucerna-VOL4-nl-de.pdf`: 12,669,843 bytes,
  sha256 `0df8e6146159d4592fe1925472dd42f3aa6181f3db1fb50508c08bf0cd7fc13e`
- Web PDF `De-Lucerna-VOL4-nl-de-web.pdf`: 1,581,124 bytes,
  sha256 `8859e18a23b46d84d20fe52015e7e5e19d9ec168142eeee13e96de3bdef8de64`
- `.text.md`: 46,161 bytes (142 single + 2 match headers + 8 match items = 150;
  8 golden, 6 gloss)
- `ABSTRACT.txt` (German, one line, no ASCII double quotes) + `WEEKLY-KIT.md`

## Gates (build 5) — ALL PASS

occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze
direct sha256 8/8; print/web text posdiff 0 msdiff 0 (8/8 pages); pdftotext
print 46,688 B / web 46,690 B; P8 answer-zone min font 10.12 pt; P8 chips =
core {A2: 8, B1: 24, B2: 3}; §1.1 SVG clean (off-palette {}, VOL.5 = 5 = core).

## Build

- `run.py` exit 0, TOTAL 150, zero OVERFLOW / TOO WIDE warnings.
- `flow[P8-keys] ended col 3/3 y=2565 (bottom 2560)` — flow cursor only; last
  ink baseline 2548.5, ink bottom ~2552, 44 px above the footer rule (y=2596).
  Same shape as en (flow 2551, ink ~2540). No overflow warning.
- `render.py` exit 0; `webpdf.py` exit 0.

## Visual — 8/8 clean

P1 numbers box fits col 1; P2 ZO ONTHOUD "MERK ES DIR" 405 px (0.5 px past the
404.5 px box edge, invisible); P6 chart head fits; P7 BRIEVEN box ends 1927.5
(above the ZINNEN rule y=1937); P8 answers 1–150 complete, pen photo in col 4.

## Fixes (explanation layer only; Dutch text, facts, keys untouched)

1. Subtitle → 36 pt / spacing 6 (W46 de). Numbers title → "IN ZAHLEN".
   Numbers items shortened ([3,1,2,2], total 384 px). P6 head → "ÜBUNGSDATEN".
   ZO ONTHOUD → "MERK ES DIR".
2. P7 BRIEVEN glosses → W46-telegraphic (g1 2 lines, g2 2 lines; VOL.5 kept).
3. P8-keys overflow (build 1): shortened 4 answer notes to 1 line each
   (measured with wrap, 13.5 pt serif, 422.5 px): #88, #89, #11, #131
   (#131 in the P7/P8 group was the col-3 lever). Keys untouched.
4. **P1 agenda gloss** (new defect class, 7th): single unwrapped p.text line
   ran off the page edge (ink to x=1968.75 > 1950) → "Alle Daten und Zeiten:
   Artikel Seite 2–5." (345.2 px, inside the box).
5. **P7 golden gloss #2** (new defect class, 8th): wrapped to 2 lines and
   overlapped the next quote (156×6.5 px) → "Nach vier Spielen stehen die
   Niederlande und Griechenland mit 8 Punkten vorn. (Pagina 1)" (1 line).
6. HET WOORD gloss stays 2 lines — no faithful 1-line version fits 422.5 px
   at 19 pt; ends above the row-B rule (y=1853), occlusion clean.

## Cross-edition actions done during de

- Checked the 2 new defect classes in the other 8 editions: P7 golden glosses
  all 1 line (OK); P1 agenda gloss overflows in fr (514 px, off-page), es
  (581 px, off-page), pt (511 px, off-page), it (437 px, past box edge), ru
  (440 px, past box edge) — all 5 pre-fixed with measured 1-liners
  (fr 343.0, es 322.9, it 299.7, pt 348.2, ru 373.0 px; limit 378.5).
  ja/ko/zh-tw agenda glosses fit (285/285/202 px).

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 6)

Rebuilt from fixed core (D3 + D5 + D4 export + proof1 D1/D2/O2 title fixes). Build only, no commit/push. Logs: `scratch-refanout-nl/de-{build,check,creambox}.log`, review `de-review/`.

- D3 short form in P2, clearance +71.9px; D5 standings line in P4 box + text.md; D4 142 `— Antwort:` + 8 `(Antwort x)`, 答案 0; italic print=web=1.
- Titles: P1 `AUSGABE` +89.5, P2 `MERK DIR` +32.5, P6 `DAFÜR / DAGEGEN` +13.5 (all PIL + built-SVG ink).
- text.md diff vs build 5: exactly 9 lines (P1 title 2 + P2 title 2 + D3 2 + D5 1 + P6 title 2).
- Gates: occlusion 0, p8 150/150 CLEAN, freeze 8/8, print/web text diff 0 (tokens 832/813/719/720/795/729/890/2255), pdftotext 46,734 B both, P8 10.12pt, chips A2:8/B1:24/B2:3, §1.1 clean.
- Creambox: 2 CREAM-BOTTOM flags pixel-probed 0 dark pixels → false positives (P2 + P5 EN JIJ). 0 true overflow.
- Visual: 8/8 pages clean.

## Deliverables (re-fanout build 6, core HEAD `5de7492f`)

- Print PDF `De-Lucerna-VOL4-nl-de.pdf`: 12,669,890 bytes,
  sha256 `f87d3f4d6518a10a42e9ebbc05d55eda09cb1b2ce2786aa695c4fb183341ab59`
- Web PDF `De-Lucerna-VOL4-nl-de-web.pdf`: 1,617,821 bytes,
  sha256 `44d1550835408e1df9bd414608ad7f507557f49f438ca61c5141ab7a7e0f3ab6`
- `2026-w47-nl-de.text.md` (46,214 B), `ABSTRACT.txt`, `WEEKLY-KIT.md` (Re-fanout §)

Status: COMPLETE — all gates pass, 8/8 pages + 3 crops viewed clean. Core fix3 (D6/D7 orphan 。) NOT included — separate incremental rebuild pending.
