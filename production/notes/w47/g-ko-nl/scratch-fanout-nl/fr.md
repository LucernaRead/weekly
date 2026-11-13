# fr (French readers) — 2026-W47 nl fan-out

COMPLETE 2026-11-11 (build 4 final).

## Deliverables

- Print PDF `De-Lucerna-VOL4-nl-fr.pdf`: 12,704,394 bytes,
  sha256 `e6db69e3cb07c8050bb95a9c29bab3862a1b57c24cc60a0b6c25a861b6ffb60a`
- Web PDF `De-Lucerna-VOL4-nl-fr-web.pdf`: 1,577,894 bytes,
  sha256 `d26a0b571ddb268ce34bb363bd39cbb63e8c48d7108d63063e1b1ae626fbe5a0`
- `.text.md`: 47,536 bytes (142 single + 2 match headers + 8 match items = 150;
  8 golden, 6 gloss)
- `ABSTRACT.txt` (French, one line, no ASCII double quotes) + `WEEKLY-KIT.md`

## Gates (build 4) — ALL PASS

occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze
direct sha256 8/8; print/web text posdiff 0 msdiff 0 (8/8 pages); pdftotext
print 46,820 B / web 46,821 B; P8 answer-zone min font 10.12 pt; P8 chips =
core {A2: 8, B1: 24, B2: 3}; §1.1 SVG clean (off-palette {}, VOL.5 = 5 = core).

## Build

- `run.py` exit 0, TOTAL 150, zero OVERFLOW / TOO WIDE warnings.
- `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core).
- `flow[P8-keys] ended col 3/3 y=2550 (bottom 2560)` — flow cursor only; last
  ink baseline ~2533, ink bottom ~2537, 59 px above the footer rule (y=2596).
- `render.py` exit 0; `webpdf.py` exit 0. (The first webpdf3 run was interrupted
  before writing the file; re-run completed and wrote 1,577,894 B.)

## Visual — 8/8 clean

P1 numbers box fits col 1; P6 chart head fits; P7 BRIEVEN box ends above the
ZINNEN rule; P8 answers 1–150 complete, pen photo in col 4.

## Fixes (explanation layer only; Dutch text, facts, keys untouched)

1. Subtitle → 36 pt / spacing 2 (W46 fr). Numbers title → "EN CHIFFRES".
   Numbers items shortened ([2,1,2,3]). P6 head → "DONNÉES FICTIVES".
   ZO ONTHOUD → "À RETENIR".
2. P7 BRIEVEN glosses → W46-telegraphic (g1 2, g2 2 lines; VOL.5 kept).
3. **P1-headline overflow (build 1)**: numbers box jumped to col 2 (French
   bridge is 4 lines at 20.5 pt; box needed 396 px but only 387 remained —
   8.7 px short); flow ended 1942. Fix: item 4 "(5 déc. : Pakjesavond, dans
   19 jours)" → "(5 déc. : dans 19 jours)" (3→2 lines, box 357 px). Flow ends
   1465 = core. Lesson: each exercise's real advance is 15.5 px more than
   Flow._fit assumes, so a jumped box cannot be absorbed by the tail — the
   box must stay in col 1. (Bridge measurement trap: the bridge is 20.5 pt,
   not 19 pt — measuring at 19 pt undercounts by a line.)
4. **P8-keys overflow (build 1)**: flow ended 2590, #150 drawn clamped past
   the footer. Shortened 4 col-3 answer notes to 1 line each: #131, #133
   ("S + V + temps"), #136, #139 ("Ordinal 88e"). Flow ends 2550.
5. P1 agenda gloss → "Toutes les dates et heures : pages 2 à 5." (343 px).
6. P1 agenda sub-head → "LES RENDEZ-VOUS" (364 px; was 503 px, off-page).
7. P1 IN DEZE EDITIE head → "CE NUMÉRO" (341.7 px; was 412.3 px, past box).

## Cross-edition actions done during fr

- Agenda sub-head spills pre-fixed in es (421→"CITAS SEMANALES" 362.1),
  it (543→"GLI APPUNTAMENTI" 374.8), pt (484→"OS COMPROMISSOS" 376.8).
- IN DEZE EDITIE head spills pre-fixed in es (408→"ESTE NÚMERO" 370.1),
  it (441→"L'EDIZIONE" 331.6), ru (414→"В ВЫПУСКЕ" 340.4).
- ru/ja/ko/zh-tw agenda sub-heads fit (373/313/334/275 px); pt IN DEZE EDITIE
  fits (371 px); ja/ko/zh-tw IN DEZE EDITIE heads fit (320/321/296 px).

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 5)

Rebuilt from fixed core (D3 + D5 + D4 export + proof1 D1/D2/D4 fixes). Build only, no commit/push. Logs: `scratch-refanout-nl/fr-{build,check,creambox}.log`, review `fr-review/`.

- D3 short form in P2, clearance +71.9px; D5 standings line in P4 box + text.md; D4 142 `— Réponse:` + 8 `(Réponse x)`, 答案 0; italic print=web=1.
- Titles: P7 `MOT DE LA SEMAINE` +10.5 (chosen over proof's `LE MOT`; verified PIL + SVG ink + visual crop), P6 `POUR OU CONTRE` +14.5.
- Curly quotes: U+2018/U+2019/U+201C/U+201D = 0 in content files, svg/, text.md, both PDF text layers (8× U+2019 → U+0027).
- text.md diff vs build 4: exactly 19 lines (D3 2 + D5 1 + titles 4 + 6 quote line-pairs).
- Gates: occlusion 0, p8 150/150 CLEAN, freeze 8/8, print/web text diff 0 (tokens 819/824/722/725/799/739/944/2436), pdftotext 46,862 B both, P8 10.12pt, chips A2:8/B1:24/B2:3, §1.1 clean.
- Creambox: 3 flags adjudicated non-overflow (P1 numbers title in-box 4.5px clearance, 8px-band flag only; P2/P5 bottom flags pixel-probed 0 dark pixels). 0 true overflow.
- Visual: 8/8 pages clean.

## Deliverables (re-fanout build 5, core HEAD `5de7492f`)

- Print PDF `De-Lucerna-VOL4-nl-fr.pdf`: 12,656,012 bytes,
  sha256 `50d9182b11a9b587f6cb4dd726cb1379387d7c5c7b52a2b36903a6c627aca544`
- Web PDF `De-Lucerna-VOL4-nl-fr-web.pdf`: 1,612,638 bytes,
  sha256 `9e90d0ab053b8fef4c8c1534294060bb0110aa5e5a395c1d11c572a9881084e4`
- `2026-w47-nl-fr.text.md` (47,739 B), `ABSTRACT.txt`, `WEEKLY-KIT.md` (Re-fanout §)

Status: COMPLETE — all gates pass, 8/8 pages + 3 crops viewed clean. Core fix3 (D6/D7 orphan 。) NOT included — separate incremental rebuild pending. Q140 `petit`/`kort` mismatch recorded, not fixed (coordinator scope: es only).
