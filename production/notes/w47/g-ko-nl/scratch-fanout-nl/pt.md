# pt (Portuguese readers) — 2026-W47 nl fan-out

COMPLETE 2026-11-11 (build 2 final).

## Deliverables

- Print PDF `De-Lucerna-VOL4-nl-pt.pdf`: 12,671,956 bytes,
  sha256 `d70937d8fb72c5a62969c4a09792a63fc9abc930d2b5f37854013a35e57e4cc5`
- Web PDF `De-Lucerna-VOL4-nl-pt-web.pdf`: 1,582,075 bytes,
  sha256 `05faf02640908dd0e31c93cc0b4e105bdb3186945c0841fafc3ad9dc6187658e`
- `.text.md`: 46,025 bytes (142 single + 2 match headers + 8 match items = 150;
  8 golden, 6 gloss)
- `ABSTRACT.txt` (Portuguese, one line, no ASCII double quotes) + `WEEKLY-KIT.md`

## Gates (build 2) — ALL PASS

occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, 0 key diffs; freeze
direct sha256 8/8; print/web text posdiff 0 msdiff 0 (8/8 pages); pdftotext
print 46,631 B / web 46,637 B; P8 answer-zone min font 10.12 pt; P8 chips =
core {A2: 8, B1: 24, B2: 3}; §1.1 SVG clean (off-palette {}, VOL.5 = 5 = core).

## Build

- `run.py` exit 0, TOTAL 150, zero OVERFLOW / TOO WIDE warnings.
- `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core).
- `flow[P8-keys] ended col 3/3 y=2550 (bottom 2560)` — flow cursor only; last
  ink baseline ~2533, ink bottom ~2537, 59 px above the footer rule (y=2596).
- `render.py` exit 0; `webpdf.py` exit 0.

## Visual — 8/8 clean

P1 numbers box fits col 1; P2 ZO ONTHOUD "LEMBRA-TE" fits; P6 chart head and
VOOR OF TEGEN head fit; P7 BRIEVEN box ends above the ZINNEN rule; P8 answers
1–150 complete, pen photo in col 4.

## Fixes (explanation layer only; Dutch text, facts, keys untouched)

1. Subtitle → 34 pt / spacing 0 (W46 pt). Numbers title → "NÚMEROS".
   Numbers items shortened ([2,1,2,2]); item 3 pre-fixed during es.
   P6 head → "DADOS DE TREINO". ZO ONTHOUD → "LEMBRA-TE".
2. P7 BRIEVEN glosses → W46-telegraphic (g1 2, g2 2 lines; VOL.5 kept).
3. P1 agenda gloss → "Datas e horas: artigos das páginas 2 a 5." (348.2 px).
4. P1 agenda sub-head → "OS COMPROMISSOS" (376.8 px; was 484 px).
5. **P8-keys overflow (build 1)**: flow ended 2590. Shortened 5 col-3 answer
   notes to 1 line: #133 "S + V + tempo", #134 "S + V + O + lugar", #135
   "S + V + tempo + lugar", #136 "S + V + O + modo", #139 "Ordinal 88e".
   Flow ends 2550.
6. No P1-headline overflow: pt bridge is 4 lines at 20.5 pt (ends 1441); the
   shortened box (357 px) fits col 1 (1441 + 369 = 1810 ≤ 1828).

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 3)

Rebuilt from fixed core (D3 + D5 + D4 export + proof1 D1/D4 + O1 fixes). Build only, no commit/push. Logs: `scratch-refanout-nl/pt-{build,check,creambox}.log`, review `pt-review/`.

- D3 short form in P2, clearance +71.9px; D5 standings line in P4 box + text.md; D4 142 `— Resposta:` + 8 `(Resposta x)`, 答案 0; italic print=web=1.
- Title: P6 `A FAVOR / CONTRA` +11.5 (from `A FAVOR OU CONTRA?` +21.5 over).
- Type labels localized (task item 2): pt TYPES row fixed in trans_table.py (was copied from en); 144 English type tokens replaced in content files (Completa a frase 65, Escolha múltipla 44, Cloze 13, Relaciona as palavras 2, Verdadeiro ou falso 7, Forma frases 8, Traduzir 4, Escrita 1 incl. content8.py:142 comparison). Type brackets in text.md all Portuguese; English instr phrases 0 in print PDF.
- NOTE (check correction): instr `Complete` ×59 is the Portuguese você-imperative of *completar* (INSTRS pt row, deliberate; parallel es `Completar` ×59 / it `Completa`), NOT leftover English. check_one.py pt-types checks were over-broad (whole-file grep) and were corrected to scope type brackets / English instr phrases; re-run ALL PASS.
- text.md diff vs build 2: exactly 293 lines (D3 2 + D5 1 + P6 title 2 + 144 type-label line-pairs).
- Gates: occlusion 0, p8 150/150 CLEAN, freeze 8/8, print/web text diff 0 (tokens 815/817/721/728/792/741/913/2372), pdftotext 46,693 B both, P8 10.12pt, spans 188, chips A2:8/B1:24/B2:3, §1.1 clean.
- Creambox: 4 flags, all adjudicated non-overflow by true-ink probes (scale 1.0; SVG 1950×2700): P2+P5 EN JIJ bottom strips 0 dark pixels; P2 `Ligue palavra-significado` true ink rightmost 1861 (1px inside 1862 edge; advance-width side bearing); P7 `HET WOORD PALAVRA DA SEMANA` true ink 1861 (inside by 1px; 8px-band flag only). 0 true overflow.
- Visual: 8/8 pages clean.
- Q140 recorded not fixed (key lacks `kort`; source has `curto`) — coordinator scope: es only.

## Deliverables (re-fanout build 3, core HEAD `5de7492f`)

- Print PDF `De-Lucerna-VOL4-nl-pt.pdf`: 12,672,018 bytes,
  sha256 `e85aa1a01bea9c7894546e9e33f45f2c519f202f3404103dff59265f5daac834`
- Web PDF `De-Lucerna-VOL4-nl-pt-web.pdf`: 1,618,472 bytes,
  sha256 `a0c8c87bd941fc87d945eac257053a482de7b1f1fc8a088070f3d66351146d85`
- `2026-w47-nl-pt.text.md` (47,204 B), `ABSTRACT.txt`, `WEEKLY-KIT.md` (Re-fanout §)

Status: COMPLETE — all gates pass, 8/8 pages + 4 crops viewed clean. Core fix3 (D6/D7 orphan 。) NOT included — separate incremental rebuild pending.
