# EDITION RECORD — 2026-W47 ko-nl (run 2; 2026-11-11)

- Slug: `2026-w47-ko-nl` (target ko, reader Dutch). Core: `core-ko` run 11 (fix1) + textmd fix2.
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-nl.json`, `gen-map-nl.py` via `mk-lang.py` + `nl-replace.json` / `nl-meta.json`); apply log `apply-nl.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-NL.pdf` — **45,473,131 bytes**, SHA-256 `2bf684453f9bb187001070bcdae607bee74f51d193fb886a3fa2d76c77790a7b`
- Web PDF: `Lucerna-VOL4-KO-NL-web.pdf` — **4,020,321 bytes** (< 7 MB), SHA-256 `c4ad9cc631b7d35230510f0920eac2310537bdffba5baec1793341ef4611eef5`
- Text export: `2026-w47-ko-nl.text.md` — 35,040 bytes, 449 items, SHA-256 `a51d9fa51f86c3ca3b10475ea9701326aef55bd1afb99f2c58d2b62a048b669d`
- `ABSTRACT.txt` — 339 bytes, SHA-256 `804a1ec11dc87f4ee3fa66329601e42f4cb14c512aa1a8e61d65b6ab74e1bf6d`
- 8 SVGs in `svg/` (hashes in `nl/sha-nl-run2.txt`).

## Gates (all pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 2) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2487, P7 teaser 2512.7 | `nl/build-nl-run2.log` |
| boxtitle width | 8/8 titles ≤ 386.5px (no shortening needed) | `nl/boxtitle-nl.log` |
| U+2019 scan (8 SVGs) | 0 | measured inline |
| occlusion audit | **0 flags** (selftest OK, 6 classes fired, clean controls silent) | `nl/occlusion-nl.json` / `nl/occlusion-nl.log` |
| p8.py extract | 150/150 noted | `nl/p8-extract-nl.log`, `nl/p8-nl.json` |
| p8.py compare vs core | CLEAN, keydiff `[137, 138]` (E-group re-aimed, W46 precedent) | `nl/p8-compare-nl.log` |
| freeze diff vs core | added CJK 7, all U+3000 (footer) | `nl/freeze-diff-nl.log` |
| freeze baseline (/usr/bin/python3) | **8/8 byte-identical** | `nl/freeze-nl.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `nl/check-nl.log` |
| check_gloss (scratch copy) | gloss fails 0 | `nl/check-nl.log` |
| print/web text layers | byte-identical, 51,630 bytes each | `nl/textlayer-diff-nl.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt (region spans 172, at-min 167)** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `nl/keycheck-nl.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `nl/style11-nl.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `nl/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 0 Chinese characters in `<text>` | measured inline |

## Fixes in this edition

1. **P2-feature FLOW OVERFLOW (nl, run 1):** the P2 feature flow ended 390px past its frame (col 2 y=1930 vs bottom 1540), 0/8 gates otherwise green. Root cause: the Dutch P2 gloss #2 (`효능 = voordeel · 등재되다 = geregistreerd worden · 발효 = fermentatie`) wrapped to 3 lines at the gloss-box inner width (CW − 2·pad = 386.5px, 20.5px/1.45) vs en's 2 lines (+29.7px); the +30px shift plus column-break waste pushed the 390px `Boodschappen` box past the 361px left in col 2, so `_fit` clamped it past the frame and it overlapped the D-day strip. Fix in the map source (`nl-replace.json`, then `mk-lang.py nl` + `gen-map-nl.py` + re-apply): `geregistreerd worden` → `geregistreerd` (passive auxiliary droppable in a gloss; meaning preserved — `geregistreerd` = listed/registered). Re-run (run 2): P2-feature ends 1531 (same as en, 9px margin), 0 FLOW OVERFLOW, and the run-1 text.md/print/web were discarded and rebuilt. Note: the probe suite (probe-p8keys) does not simulate the P2-feature flow — this defect class is only caught by run.py's own overflow line.
2. **Frame line clean at map level:** `content7.py:81` is `Kader: 「na ~」. Vraag: 「〜 후에 뭐 해요?」` straight from the map — no post-apply fix needed. Post-build sweep: U+201C = 0, U+201D = 0, U+2019 = 0 across all 8 SVGs + text.md; the 「」 form is visible in the P7 render and in text.md line 761.
3. **New edition (fan-out #3):** built from the finalized core run 11 (fix1) + fixed textmd.py re-export. No prior nl edition existed. Shipped build is run 2 (run 1 overflowed, see #1).

## Adjudicated (not defects — inherited from core or by design)

- #43/#123/#124 notes "Weatheri-voorspelling" / "Bosdienst voorspelt piek" / "Weatheri voorspelt piek": core's own renderings of the Weatheri (private weather company) and Forestry Service (산림청) forecasts — not typos.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(open opdracht — modeltekst hieronder)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (nl): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 449 items vs core 452: three accounted drops, no content gap — (1) `is_prose` drops the bare 5-letter Latin word "Alles" (P1 contents 8면 row level; the SVG/PDF render "Alles" correctly, visible on the P1 render); (2) `lcn2` removed by design; (3) `lko` removed by design. Same pattern as en/de/es/fr/it/pt.
- Repeated page citations (1면/2면/4면/6면) appear once in text.md: textmd.py dedupes repeated citation strings — the rendered P7 phrases carry the full per-phrase citations (check_core phrases 8/8 verbatim).
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style.
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.

## 150-key table (REG from edition sources vs keys extracted from P8 SVG)

| # | Page | Type | Key | Note (Dutch) | SVG |
|---|---|---|---|---|---|
| 1 | 1 | invullen | 1 | 18 nov. is D-1 | OK |
| 2 | 1 | invullen | 김장 | Het kimchiseizoen is in volle gang | OK |
| 3 | 1 | invullen | 19 | De CSAT is op donderdag 19 nov. | OK |
| 4 | 1 | invullen | 3 | 16 nov. is D-3 | OK |
| 5 | 1 | invullen | 4승 1패 | Samsung versloeg kt met 4-1 | OK |
| 6 | 1 | invullen | 11 | Inschrijving vrije plaatsen vanaf 11 nov. | OK |
| 7 | 1 | meerkeuze | A | 18 nov. is D-1 | OK |
| 8 | 1 | meerkeuze | A | De kimjangkosten zijn 9,0% lager dan vorig jaar | OK |
| 9 | 1 | meerkeuze | A | Kimchidag is zondag 22 nov. | OK |
| 10 | 1 | meerkeuze | A | Samsung won de Korean Series | OK |
| 11 | 2 | meerkeuze | A | 20 koolkoppen: 54.980 won | OK |
| 12 | 2 | meerkeuze | A | De kimjangkosten zijn 9,0% lager | OK |
| 13 | 2 | meerkeuze | A | Kimchidag is zondag 22 nov. | OK |
| 14 | 2 | meerkeuze | A | Het examen geschiedenis is zaterdag 28 nov. | OK |
| 15 | 2 | meerkeuze | A | Het WiKim-festival is vrijdag 20 nov. | OK |
| 16 | 2 | invullen | 한창 | Het kimchiseizoen is in volle gang | OK |
| 17 | 2 | invullen | 22 | Kimchidag is op 22 nov. | OK |
| 18 | 2 | invullen | 54,980 | 20 koolkoppen: 54.980 won | OK |
| 19 | 2 | invullen | 토 | Het examen geschiedenis is op zaterdag | OK |
| 20 | 2 | invullen | 배추 | De kosten daalden omdat kool goedkoper is | OK |
| 21 | 2 | invullen | 199,456 | Kimjang voor vier: 199.456 won | OK |
| 22 | 2 | invullen | 54,980 | 20 koolkoppen: 54.980 won | OK |
| 23 | 2 | invullen | 26.5 | 20 koolkoppen, 26,5% minder dan vorig jaar | OK |
| 24 | 2 | invullen | 13 | Inschrijving vrije plaatsen: 11-13 nov. | OK |
| 25 | 2 | combineren | d | 김장비용 = kimjang voor vier, 199.456 won d | OK |
| 26 | 2 | combineren | a | 김치의 날 = 22 nov. a | OK |
| 27 | 2 | combineren | c | 위킴 페스티벌 = 20 nov. in Seoel c | OK |
| 28 | 2 | combineren | b | 한능검 = afkorting van het examen geschiedenis b | OK |
| 29 | 3 | meerkeuze | A | Kimchidag is op 22 nov. | OK |
| 30 | 3 | meerkeuze | B | 22 staat voor de 22 voordelen van kimchi | OK |
| 31 | 3 | meerkeuze | A | Het WiKim-festival is vrijdag 20 nov. | OK |
| 32 | 3 | meerkeuze | B | Naejangsan: Bosdienst voorspelt piek op 4 nov. | OK |
| 33 | 3 | meerkeuze | A | De Bosdienst telt 50% van de bladeren | OK |
| 34 | 3 | invullen | 절정 | De mooiste bladeren heten 절정 | OK |
| 35 | 3 | invullen | 예보 | Voorspelde data verschillen van waargenomen data | OK |
| 36 | 3 | invullen | 관측 | Werkelijk waargenomen op 16 okt. | OK |
| 37 | 3 | invullen | 김치의 날 | 22 nov. is Kimchidag | OK |
| 38 | 3 | invullen | 발효 | Kimchi is gefermenteerd voedsel | OK |
| 39 | 3 | invullen | 22 | Kimchi heeft 22 voordelen | OK |
| 40 | 3 | invullen | 11 | Naejangsan: Weatheri voorspelt 11 nov. | OK |
| 41 | 3 | invullen | 4 | Naejangsan: Bosdienst voorspelt 4 nov. | OK |
| 42 | 3 | invullen | 20 | Het WiKim-festival is op 20 nov. | OK |
| 43 | 3 | combineren | b | 내장산 = Weatheri-voorspelling 11 nov. b | OK |
| 44 | 3 | combineren | a | 월출산 = Bosdienst-voorspelling 9 nov. a | OK |
| 45 | 3 | combineren | d | 두륜산 = Bosdienst-voorspelling 11 nov. d | OK |
| 46 | 3 | combineren | c | 설악산 = werkelijk waargenomen 16 okt. c | OK |
| 47 | 4 | meerkeuze | A | Samsung won de Korean Series | OK |
| 48 | 4 | meerkeuze | C | De serie eindigde met 4-1 | OK |
| 49 | 4 | meerkeuze | B | Wedstrijd 5, 8 nov. in Daegu: Samsung 12-1 | OK |
| 50 | 4 | meerkeuze | A | Wedstrijd 1: kt won met 8-7 | OK |
| 51 | 4 | meerkeuze | B | De eerste titel van Samsung in 12 jaar | OK |
| 52 | 4 | invullen | 4승 1패 | Samsung versloeg kt met 4-1 | OK |
| 53 | 4 | invullen | 수원 | Wedstrijd 1 en 2 waren in Suwon | OK |
| 54 | 4 | invullen | 12대 1 | Wedstrijd 5: Samsung won met 12-1 | OK |
| 55 | 4 | invullen | 12 | Samsung won na 12 jaar opnieuw | OK |
| 56 | 4 | invullen | 4연승 | Samsung won vier keer op rij na één nederlaag | OK |
| 57 | 4 | omzetten | 삼성이 kt wiz를 이겼어요. | 이기다: verleden tijd 이겼어요 | OK |
| 58 | 4 | omzetten | 1차전이 수원에서 열렸어요. | 열리다: verleden tijd 열렸어요 | OK |
| 59 | 4 | omzetten | 한국시리즈가 끝났어요. | 끝나다: verleden tijd 끝났어요 | OK |
| 60 | 4 | omzetten | 삼성이 5차전에서 이겼어요. | 이기다: verleden tijd 이겼어요 | OK |
| 61 | 4 | combineren | c | 준플레이오프 = KIA won drie keer op rij c | OK |
| 62 | 4 | combineren | d | 플레이오프 = Samsung won met 3-2 d | OK |
| 63 | 4 | combineren | a | 한국시리즈 = Samsung won met 4-1 a | OK |
| 64 | 4 | combineren | b | K리그1 = Seoel won voortijdig b | OK |
| 65 | 5 | meerkeuze | A | De voorbereidende bijeenkomst is woensdag 18 nov. | OK |
| 66 | 5 | meerkeuze | B | De CSAT begint om 8.40 uur | OK |
| 67 | 5 | meerkeuze | A | Kandidaten dit jaar: 551.864 | OK |
| 68 | 5 | meerkeuze | B | De uitslag komt vrijdag 11 dec. | OK |
| 69 | 5 | meerkeuze | A | Wees op de examendag vóór 8.10 uur in je lokaal | OK |
| 70 | 5 | invullen | 예비소집 | Bewijs ophalen bij de voorbereidende bijeenkomst | OK |
| 71 | 5 | invullen | 수험표 | Bewijs ophalen, examenlocatie controleren | OK |
| 72 | 5 | invullen | 2,310 | 2.310 kandidaten minder dan vorig jaar | OK |
| 73 | 5 | invullen | 성적 | De uitslag komt op 11 dec. | OK |
| 74 | 5 | invullen | 김치의 날 | 22 nov. is Kimchidag | OK |
| 75 | 5 | invullen | 551,864 | Kandidaten dit jaar: 551.864 | OK |
| 76 | 5 | invullen | 1,312 | Examenlocaties in het hele land: 1.312 | OK |
| 77 | 5 | invullen | 85 | 85 examendistricten in het hele land | OK |
| 78 | 5 | invullen | 10 | Op de examendag beginnen kantoren om 10.00 uur | OK |
| 79 | 5 | zinnen bouwen | 수험생은 열심히 공부해요. | Woordvolgorde: onderwerp + bijwoord + werkwoord | OK |
| 80 | 5 | zinnen bouwen | 우리는 수험생을 응원해요. | Onderwerp + lijdend voorwerp + werkwoord | OK |
| 81 | 5 | zinnen bouwen | 비행기는 듣기 시간에 뜨지 않아요. | Geen vluchten tijdens de luistertoets | OK |
| 82 | 5 | zinnen bouwen | 친구는 김치를 나눠 줘요. | Een vriend deelt kimchi | OK |
| 83 | 6 | meerkeuze | B | Deze week heeft de Korean Series een uitslag | OK |
| 84 | 6 | meerkeuze | A | Onderzoek van 9 nov.: kimjang kost 199.456 won | OK |
| 85 | 6 | meerkeuze | B | De voorspelde bladerdata zijn voorbij | OK |
| 86 | 6 | meerkeuze | C | De CSAT-uitslag komt op 11 dec. | OK |
| 87 | 6 | meerkeuze | A | Vorige week was de Series nog maar een schema | OK |
| 88 | 6 | meerkeuze | A | Wedstrijd 1: kt won met 8-7 | OK |
| 89 | 6 | meerkeuze | B | De weerdienst neemt ongeveer 80% waar | OK |
| 90 | 6 | meerkeuze | A | Eén koolkop, 16 okt.: 5.557 won | OK |
| 91 | 6 | meerkeuze | A | De referentiedatum van het kimjangonderzoek is 9 nov. | OK |
| 92 | 6 | meerkeuze | A | Kandidaten dit jaar: 551.864 | OK |
| 93 | 6 | invullen | 발표 | Een gepubliceerd schema kan veranderen | OK |
| 94 | 6 | invullen | 결과 | Uitslagen komen pas na de wedstrijden | OK |
| 95 | 6 | invullen | 기준 | Data verschillen omdat de criteria verschillen | OK |
| 96 | 6 | invullen | 날짜 | Kijk bij het lezen van het nieuws eerst naar de datum | OK |
| 97 | 6 | juist of onjuist | 틀리다 | De speciale maatregelen gelden alleen op 19 nov. | OK |
| 98 | 6 | juist of onjuist | 맞다 | Samsung won de titel met 4-1 | OK |
| 99 | 6 | juist of onjuist | 틀리다 | Voorspelde data zijn geen waargenomen data | OK |
| 100 | 6 | juist of onjuist | 맞다 | De uitslag komt op 11 dec. | OK |
| 101 | 7 | invullen | 김장 | Kimchi maken voor de winter = 김장 | OK |
| 102 | 7 | meerkeuze | A | Kimchidag is op 22 nov. | OK |
| 103 | 7 | invullen | 절임배추 | Kool vooraf gezouten | OK |
| 104 | 7 | meerkeuze | A | De kruiden bevatten gezouten garnalen | OK |
| 105 | 7 | invullen | D-1 | 18 nov. is D-1 | OK |
| 106 | 7 | meerkeuze | B | D-3 = 16 nov. | OK |
| 107 | 7 | invullen | 데이 | 19 nov. is D-day | OK |
| 108 | 7 | meerkeuze | A | D-1 betekent dat het examen morgen is | OK |
| 109 | 7 | invullen | 기준 | De data verschillen omdat de criteria verschillen (pagina 3) | OK |
| 110 | 7 | meerkeuze | A | De weerdienst neemt ongeveer 80% waar | OK |
| 111 | 7 | invullen | 결과 | Uitslagen komen pas na de wedstrijden | OK |
| 112 | 7 | meerkeuze | B | Onderscheid aankondigingen en uitslagen | OK |
| 113 | 8 | gatentekst | A | Kimchidag is zondag 22 nov. | OK |
| 114 | 8 | gatentekst | A | De CSAT is op donderdag 19 nov. | OK |
| 115 | 8 | gatentekst | A | Het examen geschiedenis is zaterdag 28 nov. | OK |
| 116 | 8 | gatentekst | A | Het WiKim-festival is vrijdag 20 nov. | OK |
| 117 | 8 | gatentekst | A | Samsung won de titel met 4-1 | OK |
| 118 | 8 | gatentekst | A | Kimjang voor vier: 199.456 won | OK |
| 119 | 8 | gatentekst | A | 20 koolkoppen: 54.980 won | OK |
| 120 | 8 | gatentekst | A | Kandidaten dit jaar: 551.864 | OK |
| 121 | 8 | meerkeuze | A | Kandidaten dit jaar: 551.864 | OK |
| 122 | 8 | meerkeuze | B | Examenlocaties in het hele land: 1.312 | OK |
| 123 | 8 | meerkeuze | A | Naejangsan: Bosdienst voorspelt piek op 4 nov. | OK |
| 124 | 8 | meerkeuze | B | Naejangsan: Weatheri voorspelt piek op 11 nov. | OK |
| 125 | 8 | meerkeuze | B | Duryunsan: Bosdienst voorspelt piek op 11 nov. | OK |
| 126 | 8 | meerkeuze | A | Wedstrijd 1: kt won met 8-7 | OK |
| 127 | 8 | meerkeuze | A | Inschrijving vrije plaatsen: 11-13 nov. | OK |
| 128 | 8 | meerkeuze | B | De periode van brandpreventie eindigt op 15 dec. | OK |
| 129 | 8 | meerkeuze | B | Minjun gaat woensdag naar de voorbereidende bijeenkomst | OK |
| 130 | 8 | meerkeuze | A | Hij doet donderdag de CSAT | OK |
| 131 | 8 | meerkeuze | B | Hij deelt zondag kimchi met zijn familie | OK |
| 132 | 8 | meerkeuze | C | Volgende week bereidt hij zich voor op het examen geschiedenis | OK |
| 133 | 8 | zinnen bouwen | 저는 수요일에 예비소집에 가요. | Woordvolgorde: onderwerp + tijd + plaats + werkwoord | OK |
| 134 | 8 | zinnen bouwen | 우리는 김치를 나눠 먹어요. | Onderwerp + lijdend voorwerp + werkwoord | OK |
| 135 | 8 | zinnen bouwen | 민준이는 한국사를 좋아해요. | 좋아하다 = leuk vinden | OK |
| 136 | 8 | zinnen bouwen | 수험생은 도서관에서 공부해요. | Gebruik 「에서」 voor de plaats van een handeling | OK |
| 137 | 8 | vertaling | 22 nov. is Kimchidag. | Zie pagina 2 | OK |
| 138 | 8 | vertaling | Samsung won de titel na 12 jaar. | Zie pagina 4 | OK |
| 139 | 8 | vertaling | 11월 18일은 예비소집이에요. | Zie pagina 5 | OK |
| 140 | 8 | vertaling | 일요일에는 가족과 김치를 나눠 먹어요. | Zie deel C op pagina 8 | OK |
| 141 | 8 | combineren | b | 예비소집 = voorbereidende bijeenkomst b | OK |
| 142 | 8 | combineren | c | 김치의 날 = 22 nov. c | OK |
| 143 | 8 | combineren | a | 발효 = het fermentatieproces a | OK |
| 144 | 8 | combineren | d | 우승 = kampioenschap d | OK |
| 145 | 8 | gatentekst | A | Hij gaat woensdag naar de voorbereidende bijeenkomst | OK |
| 146 | 8 | gatentekst | A | Kimchidag is op 22 nov. | OK |
| 147 | 8 | gatentekst | A | Het examen geschiedenis is op 28 nov. | OK |
| 148 | 8 | gatentekst | A | Kimjang voor vier: 199.456 won | OK |
| 149 | 8 | gatentekst | A | De uitslag komt op 11 dec. | OK |
| 150 | 8 | schrijven | (open opdracht — modeltekst hieronder) | Modeltekst in deel H op deze pagina (169 tekens) | OK ✓ |
