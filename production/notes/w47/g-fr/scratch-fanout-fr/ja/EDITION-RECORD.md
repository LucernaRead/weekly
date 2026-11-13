# EDITION RECORD — 2026-w47-fr-ja (run1, DONE)

**Status:** DONE — gates 15/15 PASS on first build (2026-11-11).

## Files

- Print PDF `La-Lucerna-VOL4-fr-ja.pdf` — 30,566,551 B,
  SHA-256 `b137834de17569ccac619569df1569544a823e868986565852a718315f331b8f`
- Web PDF `La-Lucerna-VOL4-fr-ja-web.pdf` — 2,310,518 B,
  SHA-256 `42907782ecdbee6b667bd5bcfe46c7c9e8b5928d23c8895e3fb8313e174c886d`
- `.text.md` — 47,551 B, SHA-256 `1b111aad84bbf1c1101131b13ce85745793b24f59ff88086151c744afed98e60`,
  1,087 lines, 150 exercises
- Freeze direct 8/8: `8bf58ae5`, `db490888`, `83ad866a`, `8252ca19`, `cae84c75`, `7fdd8932`,
  `7a37897c`, `66b5fa78`
- Text layer print/web byte-equal, 102,274 B; P8 min font 11.625pt; chips 134
  [10,12,18,15,14,15,12,38]; MCQ 45 bodies, 1,454 lines, 0 defects
- band_spans: FR title ends 1236.9, band_r1 starts 1380.0 (gap 143.1), FR sub ends 837.2,
  band_r2 starts 1430.1; string_freeze 0 unaccounted CJK chars, 1 string excused
  (core `stem_e1` prefix `Traduisez: `)

## Gates log (`ja/gates-run1.json`)

```
PASS run: exit 0, zero overflow/wide; TOTAL 150
PASS occlusion: 0 flags, selftest OK
PASS p8_extract: keys 150/150, printed notes 121/150
PASS p8_compare: CLEAN, keydiff [150] (writing key only)
PASS source_freeze: content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
PASS string_freeze: all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
PASS freeze_direct: two builds sha256 8/8 identical
PASS text_layer: print/web pdftotext byte-equal (102274 B); web 2310518 B < 7MB; print 30566551 B
PASS p8_font: P8 min font 11.625pt >= 9.75pt
PASS scans: U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
PASS chips: 134 total [10, 12, 18, 15, 14, 15, 12, 38]
PASS keycheck: 150 keys vs core: only Q150 differs (writing key)
PASS mcq: bodies: 45  rendered lines: 1454
PASS widths: 31 single-line strings all within budget
PASS band_spans: FR title ends 1236.9, band_r1 starts 1380.0, FR sub ends 837.2, band_r2 starts 1430.1
GATES 15/15 PASS
```

## Build log

`ja/build-run1.log` — rc=0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150.

## Pre-build

- `gen_expl.py ja`: first failed on extra key `gp8` (REUSED in align/ja.json); removed from
  fresh file; re-ran OK (318 keys).
- `precheck.py ja`: PASS first run. Heads pre-measured (dieppe_ex 252.2, mots_fetes 286.7,
  mots_photo 266.1, chart 496.4, agenda_note 209.0 — all within budget).
- gp1–gp8: only gp4 was 2 lines → shortened to 1 line before building.
- Diag: stems 1/1/2/1/1 (e3 1L vs core 2L); keys diff 161px → batch 1 (18 shortenings,
  6 reused→fresh moves) → 101px ≤124.
- Fresh count 160 (158 reused / 15 frozen).

## Visual QA

- 8 pages at 100 dpi (`ja/qa/p-1.png` … `p-8.png`) + 300 dpi P1 band crop
  (`ja/qa/p1-band.png`, PDF-y 380–470): **zero problems**.
- Span-gap analysis (serif lost-space class): **0 lost-space boundaries**.
- `.text.md` read through in full: no Chinese residue, no typos; answers consistent;
  person names verified against French article text (ドント, メノシェ, フィス, ヘイミッチ,
  ローレンス, スミア, メドゥール, スコット・トーマス, ギズ, メーリエ, ドレ, ヒロシゲ,
  アトジェ, モロー).

## 150-key table (core key vs ja key; `ja/keytable-run1.txt`)

diff keys: [150] — only Q150 differs: core `开放题` → ja `自由作文`.
diff keys: [150]
| Q | 核心键 | ja 键 | 备注 |
|---|---|---|---|
| 1 | gagné | gagné |  |
| 2 | mercredi | mercredi |  |
| 3 | jeudi | jeudi |  |
| 4 | premier | premier |  |
| 5 | 12,7 | 12,7 |  |
| 6 | 22 | 22 |  |
| 7 | A | A |  |
| 8 | B | B |  |
| 9 | A | A |  |
| 10 | B | B |  |
| 11 | mercredi | mercredi |  |
| 12 | lundi | lundi |  |
| 13 | jeudi | jeudi |  |
| 14 | dimanche | dimanche |  |
| 15 | Le Sénat va voter mercredi. | Le Sénat va voter mercredi. |  |
| 16 | Nous allons goûter le beaujolais jeudi. | Nous allons goûter le beaujolais jeudi. |  |
| 17 | Tu vas raconter ton jeudi 19 novembre. | Tu vas raconter ton jeudi 19 novembre. |  |
| 18 | Vous allez regarder les finales dimanche. | Vous allez regarder les finales dimanche. |  |
| 19 | C | C |  |
| 20 | B | B |  |
| 21 | A | A |  |
| 22 | a | a |  |
| 23 | b | b |  |
| 24 | c | c |  |
| 25 | d | d |  |
| 26 | Vrai | Vrai |  |
| 27 | Faux | Faux |  |
| 28 | Vrai | Vrai |  |
| 29 | Faux | Faux |  |
| 30 | Vrai | Vrai |  |
| 31 | gamay | gamay |  |
| 32 | jeudi | jeudi |  |
| 33 | Beaujeu | Beaujeu |  |
| 34 | 1985 | 1985 |  |
| 35 | Le vin ne se vend jamais avant le troisième jeudi. | Le vin ne se vend jamais avant le troisième jeudi. |  |
| 36 | On ne boit pas d'alcool avant 18 ans. | On ne boit pas d'alcool avant 18 ans. |  |
| 37 | Le beaujolais n'est pas un vin blanc. | Le beaujolais n'est pas un vin blanc. |  |
| 38 | 75 ans | 75 ans |  |
| 39 | minuit | minuit |  |
| 40 | troisième | troisième |  |
| 41 | B | B |  |
| 42 | 13 | 13 |  |
| 43 | saucisson | saucisson |  |
| 44 | B | B |  |
| 45 | A | A |  |
| 46 | C | C |  |
| 47 | A | A |  |
| 48 | A | A |  |
| 49 | a | a |  |
| 50 | b | b |  |
| 51 | c | c |  |
| 52 | d | d |  |
| 53 | plus vite | plus vite |  |
| 54 | plus grand | plus grand |  |
| 55 | moins longue | moins longue |  |
| 56 | forfait | forfait |  |
| 57 | finale | finale |  |
| 58 | groupes | groupes |  |
| 59 | tirage | tirage |  |
| 60 | Bordeaux | Bordeaux |  |
| 61 | Milan | Milan |  |
| 62 | B | B |  |
| 63 | B | B |  |
| 64 | B | B |  |
| 65 | A | A |  |
| 66 | A | A |  |
| 67 | mercredi | mercredi |  |
| 68 | prequel | prequel |  |
| 69 | Ménochet | Ménochet |  |
| 70 | 21 | 21 |  |
| 71 | produit | produit |  |
| 72 | acheter | acheter |  |
| 73 | a | a |  |
| 74 | b | b |  |
| 75 | c | c |  |
| 76 | d | d |  |
| 77 | des billets | des billets |  |
| 78 | deux | deux |  |
| 79 | B | B |  |
| 80 | B | B |  |
| 81 | B | B |  |
| 82 | B | B |  |
| 83 | C | C |  |
| 84 | B | B |  |
| 85 | a | a |  |
| 86 | b | b |  |
| 87 | c | c |  |
| 88 | d | d |  |
| 89 | plus long | plus long |  |
| 90 | moins simple | moins simple |  |
| 91 | aussi important | aussi important |  |
| 92 | examine | examine |  |
| 93 | ont rejeté | ont rejeté |  |
| 94 | part | part |  |
| 95 | peut | peut |  |
| 96 | connus | connus |  |
| 97 | battu | battu |  |
| 98 | est arrivé | est arrivé |  |
| 99 | vote | vote |  |
| 100 | beauté | beauté |  |
| 101 | produit | produit |  |
| 102 | sortent | sortent |  |
| 103 | rejetée | rejetée |  |
| 104 | jouer | jouer |  |
| 105 | Alcaraz a battu Shelton. | Alcaraz a battu Shelton. |  |
| 106 | Le Sénat vote mercredi. | Le Sénat vote mercredi. |  |
| 107 | Il est prévu que le Sénat examine le texte. | Il est prévu que le Sénat examine le texte. |  |
| 108 | Le beaujolais nouveau arrive jeudi 19 novembre. | Le beaujolais nouveau arrive jeudi 19 novembre. |  |
| 109 | A | A |  |
| 110 | B | B |  |
| 111 | A | A |  |
| 112 | B | B |  |
| 113 | A | A |  |
| 114 | A | A |  |
| 115 | B | B |  |
| 116 | A | A |  |
| 117 | A | A |  |
| 118 | A | A |  |
| 119 | B | B |  |
| 120 | B | B |  |
| 121 | A | A |  |
| 122 | B | B |  |
| 123 | A | A |  |
| 124 | C | C |  |
| 125 | A | A |  |
| 126 | A | A |  |
| 127 | A | A |  |
| 128 | A | A |  |
| 129 | A | A |  |
| 130 | Le Sénat va voter mercredi. | Le Sénat va voter mercredi. |  |
| 131 | Si tu venais dimanche, tu verrais les finales. | Si tu venais dimanche, tu verrais les finales. |  |
| 132 | Il a goûté le beaujolais à Beaujeu. | Il a goûté le beaujolais à Beaujeu. |  |
| 133 | Selon moi, la semaine est bien remplie. | Selon moi, la semaine est bien remplie. |  |
| 134 | Il est prévu que le Sénat examine le texte mercredi. | Il est prévu que le Sénat examine le texte mercredi. |  |
| 135 | Regarder une finale, c'est déjà apprendre le français. | Regarder une finale, c'est déjà apprendre le français. |  |
| 136 | Il court plus vite que son frère. | Il court plus vite que son frère. |  |
| 137 | Nous suivons le vote du Sénat depuis lundi. | Nous suivons le vote du Sénat depuis lundi. |  |
| 138 | Ce soir, nous allons préparer nos affaires. | Ce soir, nous allons préparer nos affaires. |  |
| 139 | On ne connaît pas encore les résultats. | On ne connaît pas encore les résultats. |  |
| 140 | a | a |  |
| 141 | b | b |  |
| 142 | c | c |  |
| 143 | d | d |  |
| 144 | e | e |  |
| 145 | des billets | des billets |  |
| 146 | deux | deux |  |
| 147 | quelle heure | quelle heure |  |
| 148 | devant | devant |  |
| 149 | film | film |  |
| 150 | 开放题 | 自由作文 | 仅此题不同 |
