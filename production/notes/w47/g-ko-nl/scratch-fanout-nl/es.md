# es (Spanish readers) — 2026-W47 nl fan-out

COMPLETE 2026-11-11 (build 2 final).

## Deliverables

- Print PDF `De-Lucerna-VOL4-nl-es.pdf`: 12,669,477 bytes,
  sha256 `47f15cc8cb137a228df290fa28469bfce1061f89de9d16cc91bb1876937f0ec1`
- Web PDF `De-Lucerna-VOL4-nl-es-web.pdf`: 1,579,768 bytes,
  sha256 `4b416858f1412e22010b46fbc24ebab13ca630f31526cf93a56f6d9065abfb20`
- `.text.md`: 47,276 bytes (142 single + 2 match headers + 8 match items = 150;
  8 golden, 6 gloss)
- `ABSTRACT.txt` (Spanish, one line, no ASCII double quotes) + `WEEKLY-KIT.md`

## Gates (build 2) — ALL PASS

occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze
direct sha256 8/8; print/web text posdiff 0 msdiff 0 (8/8 pages); pdftotext
print 46,748 B / web 46,742 B; P8 answer-zone min font 10.12 pt; P8 chips =
core {A2: 8, B1: 24, B2: 3}; §1.1 SVG clean (off-palette {}, VOL.5 = 5 = core).

## Build

- `run.py` exit 0, TOTAL 150, zero OVERFLOW / TOO WIDE warnings.
- `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core).
- `flow[P8-keys] ended col 3/3 y=2502 (bottom 2560)` — 58 px headroom.
- `render.py` exit 0; `webpdf.py` exit 0.

## Visual — 8/8 clean

P1 numbers box fits col 1; P2 ZO ONTHOUD "RECUERDA" fits; P6 chart head
"DATOS DE PRÁCTICA" 401 px (0.5 px past the box edge, invisible at render —
W46-shipped string, accepted like de "MERK ES DIR" 405 px); P7 BRIEVEN box
ends above the ZINNEN rule; P8 answers 1–150 complete, pen photo in col 4.

## Fixes (explanation layer only; Dutch text, facts, keys untouched)

1. Subtitle → 36 pt / spacing 2 (W46 es). Numbers title → "EN CIFRAS".
   Numbers items shortened ([2,1,2,2]). P6 head → "DATOS DE PRÁCTICA".
   ZO ONTHOUD → "RECUERDA".
2. P7 BRIEVEN glosses → W46-telegraphic (g1 2, g2 2 lines; VOL.5 kept).
3. P1 agenda gloss → "Fechas y horas: artículos, págs. 2 a 5." (322.9 px).
4. P1 agenda sub-head → "CITAS SEMANALES" (362.1 px; was 421 px).
5. P1 IN DEZE EDITIE head → "ESTE NÚMERO" (370.1 px; was 408 px).
6. **P8-keys overflow (build 1)**: flow ended 2590. Shortened 5 col-3 answer
   notes, each measured to 1 line: #133 "S + V + tiempo", #134 "S + V + O +
   lugar", #136 "S + V + O + modo", #139 "Ordinal 88e", #140 "surprise:
   expresión fija". Abbreviated forms keep ALL word-order elements.
   Flow ends 2502.
7. No P1-headline overflow: es bridge is 3 lines at 20.5 pt (ends 1411); the
   box (357 px) fits col 1 with 48 px to spare.

## Cross-edition actions done during es

- pt item 3 → "(8 pontos: empatados)"; ru item 1 → "(16 ноября: Германия)"
  — both 3→2 lines, so their 4-line bridges (1441) fit the 357 px box.
- Bridge/box fit verified for all remaining: it 3 lines / 357 fits, pt 4 / 357
  fits (after item fix), ru 4 / 357 fits (after item fix), ja 3 / 357 fits,
  ko 3 / 357 fits, zh-tw 3 / 384 fits.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 3)

Rebuilt from fixed core (D3 + D5 + D4 export + proof1 D1/D2/D6/O2 fixes). Build only, no commit/push. Logs: `scratch-refanout-nl/es-{build,check,creambox}.log`, review `es-review/`; handoff note `es-proof-handoff-note.md`.

- D3 short form in P2, clearance +71.9px; D5 standings line in P4 box + text.md; D4 142 `— Respuesta:` + 8 `(Respuesta x)`, 答案 0; italic print=web=1.
- Titles re-measured from built SVGs (handoff item 2): P6 `¿SÍ O NO?` +103.5, P7 `PALABRA SEMANAL` +21.5 — both fit, no further shortening.
- Q140 (handoff item 1, D6): key now `Ik maak een surprise met een kort gedicht.`, note `corto = kort`; verified text.md:415 + printed P8 answer 140; p8 compare still CLEAN. Key source is core `content8.py:75` (core defect; core source itself carries 小诗).
- Q78 (handoff item 3, O1): stem + key `gaat maken` unchanged, singular-zij convention accepted.
- text.md diff vs build 2: exactly 9 lines (D3 2 + D5 1 + titles 4 + Q140 2).
- Gates: occlusion 0, p8 150/150 CLEAN, freeze 8/8, print/web text diff 0 (tokens 812/820/727/731/794/743/913/2403), pdftotext 46,814 B both, P8 10.12pt, chips A2:8/B1:24/B2:3, §1.1 clean.
- Creambox: 3 flags adjudicated non-overflow (P2/P5 bottom: 0 dark pixels in strip; P6 chart head: true ink rightmost x=1861, inside box at 1862 — advance metric overstates by side bearing). 0 true overflow.
- Visual: 8/8 pages clean.

## Deliverables (re-fanout build 3, core HEAD `5de7492f`)

- Print PDF `De-Lucerna-VOL4-nl-es.pdf`: 12,669,541 bytes,
  sha256 `0388d59c7e7085bbd4a733f235081f26dac901489ebe1f10ee121f391306b771`
- Web PDF `De-Lucerna-VOL4-nl-es-web.pdf`: 1,616,172 bytes,
  sha256 `5b4f81621c77233cf9d89fa44eb6a1a249fb943f39d64ca96749e70f39cd7a21`
- `2026-w47-nl-es.text.md` (47,649 B), `ABSTRACT.txt`, `WEEKLY-KIT.md` (Re-fanout §)

Status: COMPLETE — all gates pass, 8/8 pages + 3 crops viewed clean. Core fix3 (D6/D7 orphan 。) NOT included — separate incremental rebuild pending. Q140 mismatch in 6 other editions recorded in `es-proof-handoff-note.md`, not fixed (coordinator scope: es only).
