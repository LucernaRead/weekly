# EDITION RECORD — 2026-W47 ko-it (run 1; 2026-11-11)

- Slug: `2026-w47-ko-it` (target ko, reader Italian). Core: `core-ko` run 11 (fix1) + textmd fix2.
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-it.json`, `gen-map-it.py` via `mk-lang.py` + `it-replace.json` / `it-meta.json`); apply log `apply-it.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-IT.pdf` — **45,676,964 bytes**, SHA-256 `54e35033290e55ff439025e873dab750770cfcff730f907e2fecbb9d5c0aa4b0`
- Web PDF: `Lucerna-VOL4-KO-IT-web.pdf` — **4,025,960 bytes** (< 7 MB), SHA-256 `f6135c5054ca28278a66c8b074a578d99061a7cf93bf7a0dd0749916115a4900`
- Text export: `2026-w47-ko-it.text.md` — 35,213 bytes, 449 items, SHA-256 `247ed6bd653c78b62e26a25322bef7e07a22c028cdbf3436878f6c9aad85575c`
- `ABSTRACT.txt` — 364 bytes, SHA-256 `c3e23f5ab61b434c4f0b8a35e4970eec308c31cdfdc56f9d0946c255b1237fbe`
- 8 SVGs in `svg/` (hashes in `it/sha-it-run1.txt`).

## Gates (all pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 1) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2442, P7 teaser 2483.7 | `it/build-it-run1.log` |
| boxtitle width | 8/8 titles ≤ 386.5px (P5 shortened in map: Numeri dei giovani → Numeri giovani) | `it/boxtitle-it.log` |
| U+2019 scan (8 SVGs) | 0 | measured inline |
| occlusion audit | **0 flags** (selftest OK, 6 classes fired, clean controls silent) | `it/occlusion-it.json` / `it/occlusion-it.log` |
| p8.py extract | 150/150 noted | `it/p8-extract-it.log`, `it/p8-it.json` |
| p8.py compare vs core | CLEAN, keydiff `[137, 138]` (E-group re-aimed, W46 precedent) | `it/p8-compare-it.log` |
| freeze diff vs core | added CJK 7, all U+3000 (footer) | `it/freeze-diff-it.log` |
| freeze baseline (/usr/bin/python3) | **8/8 byte-identical** | `it/freeze-it.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `it/check-it.log` |
| check_gloss (scratch copy) | gloss fails 0 | `it/check-it.log` |
| print/web text layers | byte-identical, 51,894 bytes each | `it/textlayer-diff-it.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `it/keycheck-it.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `it/style11-it.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `it/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 0 Chinese characters in `<text>` | measured inline |

## Fixes in this edition

1. **P5 box title (it, run 1):** `이번 주 청년 숫자　Numeri dei giovani` measured 399.8px over the 386.5px inner width. Shortened in the map source (`it-replace.json`, then `mk-lang.py it` + `gen-map-it.py` + re-apply) to `Numeri giovani`; boxtitle 8/8 before the build. Note: the map value lives in `gen-map-it.py`'s embedded MAP dict — editing `it-replace.json` alone does not change `map-it.json`; `mk-lang.py it` must regenerate the gen-map script first.
2. **Frame line clean at map level:** `content7.py:81` is `Quadro: 「dopo ~」. Domanda: 「〜 후에 뭐 해요?」` straight from the map — no post-apply fix needed. Post-build sweep: U+201C = 0, U+201D = 0, U+2019 = 0 across all 8 SVGs + text.md; the 「」 form is visible in the P7 render and in text.md line 761.
3. **New edition (fan-out #3):** built from the finalized core run 11 (fix1) + fixed textmd.py re-export. No prior it edition existed.

## Adjudicated (not defects — inherited from core or by design)

- P8 match-item notes end with the option letter repeated: the letter is in the source note literal itself, core's own convention.
- #43/#123/#124 note "previsione di Weatheri": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(compito libero — testo modello qui sotto)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (it): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 449 items vs core 452: three accounted drops, no content gap — (1) `is_prose` drops the bare 3-letter Latin word "Tutto" (P1 contents 8면 row level; the SVG/PDF render "Tutto" correctly, visible on the P1 render); (2) `lcn2` removed by design; (3) `lko` removed by design. Same pattern as en/de/es/fr.
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style.
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.

## 150-key table (REG from edition sources vs keys extracted from P8 SVG)

| # | Page | Type | Key | Note (Italian) | SVG |
|---|---|---|---|---|---|
| 1 | 1 | Completare | 1 | 18 nov. = D-1 | OK |
| 2 | 1 | Completare | 김장 | La stagione del kimchi è in pieno svolgimento | OK |
| 3 | 1 | Completare | 19 | Il CSAT è giovedì 19 nov. | OK |
| 4 | 1 | Completare | 3 | 16 nov. = D-3 | OK |
| 5 | 1 | Completare | 4승 1패 | Samsung ha battuto kt 4-1 | OK |
| 6 | 1 | Completare | 11 | Iscrizioni per i posti liberi dall'11 nov. | OK |
| 7 | 1 | Scelta multipla | A | 18 nov. = D-1 | OK |
| 8 | 1 | Scelta multipla | A | Il kimjang costa il 9,0 % in meno dell'anno scorso | OK |
| 9 | 1 | Scelta multipla | A | Il Giorno del Kimchi è domenica 22 nov. | OK |
| 10 | 1 | Scelta multipla | A | Samsung ha vinto le Korean Series | OK |
| 11 | 2 | Scelta multipla | A | 20 cavoli: 54 980 won | OK |
| 12 | 2 | Scelta multipla | A | Il kimjang è sceso del 9,0 % | OK |
| 13 | 2 | Scelta multipla | A | Il Giorno del Kimchi è domenica 22 nov. | OK |
| 14 | 2 | Scelta multipla | A | L'esame di storia è sabato 28 nov. | OK |
| 15 | 2 | Scelta multipla | A | Il festival WiKim è venerdì 20 nov. | OK |
| 16 | 2 | Completare | 한창 | La stagione del kimchi è in pieno svolgimento | OK |
| 17 | 2 | Completare | 22 | Il Giorno del Kimchi è il 22 nov. | OK |
| 18 | 2 | Completare | 54,980 | 20 cavoli: 54 980 won | OK |
| 19 | 2 | Completare | 토 | L'esame di storia è di sabato | OK |
| 20 | 2 | Completare | 배추 | I prezzi sono scesi perché il cavolo costa meno | OK |
| 21 | 2 | Completare | 199,456 | Kimjang per quattro: 199 456 won | OK |
| 22 | 2 | Completare | 54,980 | 20 cavoli: 54 980 won | OK |
| 23 | 2 | Completare | 26.5 | 20 cavoli, in calo del 26,5 % rispetto all'anno scorso | OK |
| 24 | 2 | Completare | 13 | Posti liberi: iscrizioni dall'11 al 13 nov. | OK |
| 25 | 2 | Abbinare | d | 김장비용 = kimjang per quattro, 199 456 won d | OK |
| 26 | 2 | Abbinare | a | 김치의 날 = 22 nov. a | OK |
| 27 | 2 | Abbinare | c | 위킴 페스티벌 = 20 nov. a Seul c | OK |
| 28 | 2 | Abbinare | b | 한능검 = abbreviazione dell'esame di storia b | OK |
| 29 | 3 | Scelta multipla | A | Il Giorno del Kimchi è il 22 nov. | OK |
| 30 | 3 | Scelta multipla | B | 22 sono i 22 benefici del kimchi | OK |
| 31 | 3 | Scelta multipla | A | Il festival WiKim è venerdì 20 nov. | OK |
| 32 | 3 | Scelta multipla | B | Naejangsan: picco previsto dal Servizio Forestale il 4 nov. | OK |
| 33 | 3 | Scelta multipla | A | Il Servizio Forestale conta il 50 % delle foglie | OK |
| 34 | 3 | Completare | 절정 | Le foglie più belle si chiamano 절정 | OK |
| 35 | 3 | Completare | 예보 | Le date previste differiscono da quelle osservate | OK |
| 36 | 3 | Completare | 관측 | Osservato davvero il 16 ott. | OK |
| 37 | 3 | Completare | 김치의 날 | Il 22 nov. è il Giorno del Kimchi | OK |
| 38 | 3 | Completare | 발효 | Il kimchi è un alimento fermentato | OK |
| 39 | 3 | Completare | 22 | Il kimchi ha 22 benefici | OK |
| 40 | 3 | Completare | 11 | Naejangsan: previsione di Weatheri, 11 nov. | OK |
| 41 | 3 | Completare | 4 | Naejangsan: previsione del Servizio Forestale, 4 nov. | OK |
| 42 | 3 | Completare | 20 | Il festival WiKim è il 20 nov. | OK |
| 43 | 3 | Abbinare | b | 내장산 = previsione di Weatheri, 11 nov. b | OK |
| 44 | 3 | Abbinare | a | 월출산 = previsione del Servizio Forestale, 9 nov. a | OK |
| 45 | 3 | Abbinare | d | 두륜산 = previsione del Servizio Forestale, 11 nov. d | OK |
| 46 | 3 | Abbinare | c | 설악산 = osservato il 16 ott. c | OK |
| 47 | 4 | Scelta multipla | A | Samsung ha vinto le Korean Series | OK |
| 48 | 4 | Scelta multipla | C | La serie è finita 4-1 | OK |
| 49 | 4 | Scelta multipla | B | Gara 5, 8 nov. a Daegu: Samsung 12-1 | OK |
| 50 | 4 | Scelta multipla | A | Gara 1: kt ha vinto 8-7 | OK |
| 51 | 4 | Scelta multipla | B | Primo titolo Samsung dopo 12 anni | OK |
| 52 | 4 | Completare | 4승 1패 | Samsung ha battuto kt 4-1 | OK |
| 53 | 4 | Completare | 수원 | Le gare 1 e 2 erano a Suwon | OK |
| 54 | 4 | Completare | 12대 1 | Gara 5: Samsung ha vinto 12-1 | OK |
| 55 | 4 | Completare | 12 | Samsung ha vinto di nuovo dopo 12 anni | OK |
| 56 | 4 | Completare | 4연승 | Samsung ha vinto quattro gare di fila dopo una sconfitta | OK |
| 57 | 4 | Trasformare | 삼성이 kt wiz를 이겼어요. | 이기다: passato 이겼어요 | OK |
| 58 | 4 | Trasformare | 1차전이 수원에서 열렸어요. | 열리다: passato 열렸어요 | OK |
| 59 | 4 | Trasformare | 한국시리즈가 끝났어요. | 끝나다: passato 끝났어요 | OK |
| 60 | 4 | Trasformare | 삼성이 5차전에서 이겼어요. | 이기다: passato 이겼어요 | OK |
| 61 | 4 | Abbinare | c | 준플레이오프 = KIA, tre vittorie di fila c | OK |
| 62 | 4 | Abbinare | d | 플레이오프 = Samsung 3-2 d | OK |
| 63 | 4 | Abbinare | a | 한국시리즈 = Samsung 4-1 a | OK |
| 64 | 4 | Abbinare | b | K리그1 = Seul, vittoria anticipata b | OK |
| 65 | 5 | Scelta multipla | A | La convocazione preliminare è mercoledì 18 nov. | OK |
| 66 | 5 | Scelta multipla | B | Il CSAT inizia alle 8:40 | OK |
| 67 | 5 | Scelta multipla | A | Candidati quest'anno: 551 864 | OK |
| 68 | 5 | Scelta multipla | B | I risultati escono venerdì 11 dic. | OK |
| 69 | 5 | Scelta multipla | A | Entra in aula entro le 8:10 il giorno dell'esame | OK |
| 70 | 5 | Completare | 예비소집 | Ritira il pass alla convocazione preliminare | OK |
| 71 | 5 | Completare | 수험표 | Ritira il pass e controlla la sede d'esame | OK |
| 72 | 5 | Completare | 2,310 | 2 310 candidati in meno dell'anno scorso | OK |
| 73 | 5 | Completare | 성적 | I risultati escono l'11 dic. | OK |
| 74 | 5 | Completare | 김치의 날 | Il 22 nov. è il Giorno del Kimchi | OK |
| 75 | 5 | Completare | 551,864 | Candidati quest'anno: 551 864 | OK |
| 76 | 5 | Completare | 1,312 | Sedi d'esame in tutto il paese: 1 312 | OK |
| 77 | 5 | Completare | 85 | 85 zone d'esame in tutto il paese | OK |
| 78 | 5 | Completare | 10 | Il giorno dell'esame, gli uffici aprono alle 10:00 | OK |
| 79 | 5 | Formare frasi | 수험생은 열심히 공부해요. | Ordine delle parole: soggetto + avverbio + verbo | OK |
| 80 | 5 | Formare frasi | 우리는 수험생을 응원해요. | Soggetto + oggetto + verbo | OK |
| 81 | 5 | Formare frasi | 비행기는 듣기 시간에 뜨지 않아요. | Niente voli durante la prova d'ascolto | OK |
| 82 | 5 | Formare frasi | 친구는 김치를 나눠 줘요. | Un amico condivide il kimchi | OK |
| 83 | 6 | Scelta multipla | B | Questa settimana le Korean Series hanno un risultato | OK |
| 84 | 6 | Scelta multipla | A | Sondaggio del 9 nov.: il kimjang costa 199 456 won | OK |
| 85 | 6 | Scelta multipla | B | Le date previste delle foglie sono passate | OK |
| 86 | 6 | Scelta multipla | C | I risultati del CSAT escono l'11 dic. | OK |
| 87 | 6 | Scelta multipla | A | La settimana scorsa la Serie era solo un calendario | OK |
| 88 | 6 | Scelta multipla | A | Gara 1: kt ha vinto 8-7 | OK |
| 89 | 6 | Scelta multipla | B | Il servizio meteo osserva circa l'80% | OK |
| 90 | 6 | Scelta multipla | A | Un cavolo, 16 ott.: 5 557 won | OK |
| 91 | 6 | Scelta multipla | A | La data di riferimento del sondaggio sul kimjang è il 9 nov. | OK |
| 92 | 6 | Scelta multipla | A | Candidati quest'anno: 551 864 | OK |
| 93 | 6 | Completare | 발표 | Un calendario pubblicato può cambiare | OK |
| 94 | 6 | Completare | 결과 | I risultati arrivano solo dopo le partite | OK |
| 95 | 6 | Completare | 기준 | Le date differiscono perché i criteri differiscono | OK |
| 96 | 6 | Completare | 날짜 | Quando leggi le notizie, controlla prima la data | OK |
| 97 | 6 | Vero o falso | 틀리다 | Le misure speciali valgono solo il 19 nov. | OK |
| 98 | 6 | Vero o falso | 맞다 | Samsung ha vinto il titolo 4-1 | OK |
| 99 | 6 | Vero o falso | 틀리다 | Le date previste non sono date osservate | OK |
| 100 | 6 | Vero o falso | 맞다 | I risultati escono l'11 dic. | OK |
| 101 | 7 | Completare | 김장 | Preparare il kimchi invernale = 김장 | OK |
| 102 | 7 | Scelta multipla | A | Il Giorno del Kimchi è il 22 nov. | OK |
| 103 | 7 | Completare | 절임배추 | Cavolo salato in anticipo | OK |
| 104 | 7 | Scelta multipla | A | Il condimento contiene gamberetti salati | OK |
| 105 | 7 | Completare | D-1 | 18 nov. = D-1 | OK |
| 106 | 7 | Scelta multipla | B | D-3 = 16 nov. | OK |
| 107 | 7 | Completare | 데이 | 19 nov. = D-day | OK |
| 108 | 7 | Scelta multipla | A | D-1: l'esame è domani | OK |
| 109 | 7 | Completare | 기준 | Le date differiscono perché i criteri differiscono (p. 3) | OK |
| 110 | 7 | Scelta multipla | A | Il servizio meteo osserva circa l'80% | OK |
| 111 | 7 | Completare | 결과 | I risultati arrivano solo dopo le partite | OK |
| 112 | 7 | Scelta multipla | B | Distingui annunci e risultati | OK |
| 113 | 8 | Testo con buchi | A | Il Giorno del Kimchi è domenica 22 nov. | OK |
| 114 | 8 | Testo con buchi | A | Il CSAT è giovedì 19 nov. | OK |
| 115 | 8 | Testo con buchi | A | L'esame di storia è sabato 28 nov. | OK |
| 116 | 8 | Testo con buchi | A | Il festival WiKim è venerdì 20 nov. | OK |
| 117 | 8 | Testo con buchi | A | Samsung ha vinto il titolo 4-1 | OK |
| 118 | 8 | Testo con buchi | A | Kimjang per quattro: 199 456 won | OK |
| 119 | 8 | Testo con buchi | A | 20 cavoli: 54 980 won | OK |
| 120 | 8 | Testo con buchi | A | Candidati quest'anno: 551 864 | OK |
| 121 | 8 | Scelta multipla | A | Candidati quest'anno: 551 864 | OK |
| 122 | 8 | Scelta multipla | B | Sedi d'esame in tutto il paese: 1 312 | OK |
| 123 | 8 | Scelta multipla | A | Naejangsan: picco previsto dal Servizio Forestale il 4 nov. | OK |
| 124 | 8 | Scelta multipla | B | Naejangsan: picco previsto da Weatheri, 11 nov. | OK |
| 125 | 8 | Scelta multipla | B | Duryunsan: picco previsto dal Servizio Forestale, 11 nov. | OK |
| 126 | 8 | Scelta multipla | A | Gara 1: kt ha vinto 8-7 | OK |
| 127 | 8 | Scelta multipla | A | Posti liberi: iscrizioni dall'11 al 13 nov. | OK |
| 128 | 8 | Scelta multipla | B | La prevenzione incendi finisce il 15 dic. | OK |
| 129 | 8 | Scelta multipla | B | Minjun va alla convocazione preliminare mercoledì | OK |
| 130 | 8 | Scelta multipla | A | Fa il CSAT giovedì | OK |
| 131 | 8 | Scelta multipla | B | Condivide il kimchi con la famiglia domenica | OK |
| 132 | 8 | Scelta multipla | C | La prossima settimana prepara l'esame di storia | OK |
| 133 | 8 | Formare frasi | 저는 수요일에 예비소집에 가요. | Ordine delle parole: soggetto + tempo + luogo + verbo | OK |
| 134 | 8 | Formare frasi | 우리는 김치를 나눠 먹어요. | Soggetto + oggetto + verbo | OK |
| 135 | 8 | Formare frasi | 민준이는 한국사를 좋아해요. | 좋아하다 = piacere | OK |
| 136 | 8 | Formare frasi | 수험생은 도서관에서 공부해요. | Per il luogo di un'azione si usa 「에서」 | OK |
| 137 | 8 | Tradurre | Il 22 nov. è il Giorno del Kimchi. | Vedi p. 2 | OK |
| 138 | 8 | Tradurre | Samsung ha vinto il titolo dopo 12 anni. | Vedi p. 4 | OK |
| 139 | 8 | Tradurre | 11월 18일은 예비소집이에요. | Vedi p. 5 | OK |
| 140 | 8 | Tradurre | 일요일에는 가족과 김치를 나눠 먹어요. | Vedi la sezione C, p. 8 | OK |
| 141 | 8 | Abbinare | b | 예비소집 = convocazione preliminare b | OK |
| 142 | 8 | Abbinare | c | 김치의 날 = 22 nov. c | OK |
| 143 | 8 | Abbinare | a | 발효 = il processo di fermentazione a | OK |
| 144 | 8 | Abbinare | d | 우승 = titolo d | OK |
| 145 | 8 | Testo con buchi | A | Va alla convocazione preliminare mercoledì | OK |
| 146 | 8 | Testo con buchi | A | Il Giorno del Kimchi è il 22 nov. | OK |
| 147 | 8 | Testo con buchi | A | L'esame di storia è il 28 nov. | OK |
| 148 | 8 | Testo con buchi | A | Kimjang per quattro: 199 456 won | OK |
| 149 | 8 | Testo con buchi | A | I risultati escono l'11 dic. | OK |
| 150 | 8 | Scrivere | (compito libero — testo modello qui sotto) | Testo modello nella sezione H di questa pagina (169 caratteri) | OK ✓ |
