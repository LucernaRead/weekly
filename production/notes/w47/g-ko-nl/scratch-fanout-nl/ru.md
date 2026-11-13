# ru (Russian readers) — 2026-W47 nl fan-out

COMPLETE 2026-11-11 (build 4 final).

## Deliverables

- Print PDF `De-Lucerna-VOL4-nl-ru.pdf`: 12,718,342 bytes,
  sha256 `d60da2784c30d2834e14f08ce45f3b697c20fa2fd50cbbdf09f2f87f52ecd542`
- Web PDF `De-Lucerna-VOL4-nl-ru-web.pdf`: 1,625,792 bytes,
  sha256 `22ac256f24bc3585dfb35f44ffd57dab4f5d403bbaa49f11e8a638d604fca4c4`
- `.text.md`: 57,044 bytes (142 single + 2 match headers + 8 match items = 150;
  8 golden, 6 gloss)
- `ABSTRACT.txt` (Russian, one line, no ASCII double quotes) + `WEEKLY-KIT.md`

## Gates (build 4) — ALL PASS

occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze
direct sha256 8/8; print/web text posdiff 0 msdiff 0 (8/8 pages); pdftotext
print 54,915 B / web 54,913 B; P8 answer-zone min font 10.12 pt; P8 chips =
core {A2: 8, B1: 24, B2: 3}; §1.1 SVG clean (off-palette {}, VOL.5 = 5 = core).

## Build

- `run.py` exit 0, TOTAL 150, zero OVERFLOW / TOO WIDE warnings.
- `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core).
- `flow[P8-keys] ended col 3/3 y=2486 (bottom 2560)` — 74 px margin, best of
  the non-Chinese editions.
- `render.py` exit 0; `webpdf.py` exit 0.

## Visual — 8/8 clean

P1 numbers box fits col 1; P2 ZO ONTHOUD "ЗАПОМНИ" fits, GEDICHT strip gloss
fits its box; P6 chart head and VOOR OF TEGEN head fit; P7 BRIEVEN box ends
above the ZINNEN rule; P8 answers 1–150 complete, pen photo in col 4.

## Fixes (explanation layer only; Dutch text, facts, keys untouched)

1. Subtitle → 36 pt / spacing 0 (W46 ru). Numbers title → "В ЦИФРАХ".
   Numbers items shortened ([3,1,2,2]); item 1 pre-fixed during es.
   P6 head → "УЧЕБНЫЕ ДАННЫЕ". ZO ONTHOUD → "ЗАПОМНИ".
2. P7 BRIEVEN glosses → W46-telegraphic (g1 2, g2 2 lines; VOL.5 kept);
   PAS OP! err1 → 1 line, err3 → 1 line, err4 → 2 lines.
3. P1 agenda gloss → "Все даты и время: статьи, страницы 2–5." (373.0 px).
4. P1 IN DEZE EDITIE head → "В ВЫПУСКЕ" (340.4 px; was 441 px).
5. **P8-keys overflow (builds 1–2, worst of all editions)**: flow ended 2590,
   #148/#149/#150 clamped on one baseline (y=2573.5), #150's 3 lines
   overlapping. Root cause is structural, not one note: Russian notes are
   the longest — col 3 held 41 blocks with 10 two-line answers, ~94 px over.
   Fix in two parts: (a) 6 col-3 notes to 1 line (#127, #132, #133–136 with
   "П + Г + …" abbreviations) — build 2 still ended 2590 (the flow-end
   number is a clamp artifact); (b) 11 more notes to 1 line across cols 2–3
   (#82, #83, #88, #89, #91, #97, #98, #99, #112, #139 "— 88-й", #140
   "— surprise (фикс.)"), letting col 2 absorb 4 more blocks and moving
   the col-3 boundary later. Flow ends 2486.
6. **P2 GEDICHT strip gloss overflow (build 3)**: 4-line gloss ran 13.3 px
   past the 150 px box bottom → "Маленькое стихотворение: смешное или
   тёплое" (3 lines).
7. No P1-headline overflow: ru bridge is 4 lines at 20.5 pt (ends 1441); the
   shortened box (357 px) fits col 1 (1441 + 369 = 1810 ≤ 1828).

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 5)

Rebuilt from fixed core (D3 + D5 + D4 export only; ru has no proof dir, no edition-level proof fixes). Build only, no commit/push. Logs: `scratch-refanout-nl/ru-{build,check,creambox}.log`, review `ru-review/`.

- D3 short form in P2, clearance +71.9px; D5 standings line in P4 box + text.md; D4 142 `— Ответ：` + 8 `(Ответ x)`, 答案 0; italic print=web=1.
- text.md diff vs build 4: exactly 3 lines (D3 2 + D5 1).
- Gates: occlusion 0, p8 150/150 CLEAN, freeze 8/8, print/web text diff 0 (tokens 797/802/722/727/783/730/885/2149), pdftotext 54,978 B both, P8 10.12pt, spans 598, chips A2:8/B1:24/B2:3, §1.1 clean.
- Creambox: 3 flags, all adjudicated non-overflow (P2+P5 EN JIJ bottom strips 0 dark pixels; P6 chart head inside by 6.4px, 8px-band flag only). 0 true overflow.
- Visual: 8/8 pages clean.
- Q140: no defect in ru (source carries no qualifier, key matches).

## Deliverables (re-fanout build 5, core HEAD `5de7492f`)

- Print PDF `De-Lucerna-VOL4-nl-ru.pdf`: 12,718,382 bytes,
  sha256 `f945029d3a736dd3d139c555a4693283dc3aa9feba732edc91805b556ff889c2`
- Web PDF `De-Lucerna-VOL4-nl-ru-web.pdf`: 1,661,354 bytes,
  sha256 `e5e3d5d3fd36b767858c96cafce0b4bf317f7ed2fd62a605aaa7eed327352724`
- `2026-w47-nl-ru.text.md` (57,848 B), `ABSTRACT.txt`, `WEEKLY-KIT.md` (Re-fanout §)

Status: COMPLETE — all gates pass, 8/8 pages + 4 crops viewed clean. Core fix3 (D6/D7 orphan 。) NOT included — separate incremental rebuild pending.
