# EDITION RECORD — 2026-W47 ko-es (run 3; 2026-11-11)

- Slug: `2026-w47-ko-es` (target ko, reader Spanish). Core: `core-ko` run 10 as modified 2026-11-11 08:40 UTC (see Adjudicated note on the core move).
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-es.json`, `gen-map-es.py` via `mk-lang.py` + `es-replace.json` / `es-meta.json`); apply log `apply-es.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-ES.pdf` — **45,679,702 bytes**, SHA-256 `f04438c0c4b588095c61962689069516dc02652412340f53137879d13ecf18b9`
- Web PDF: `Lucerna-VOL4-KO-ES-web.pdf` — **4,034,870 bytes** (< 7 MB), SHA-256 `4abcc6e26026d3d4cf9f09ec576e6a7247f8679dffe77cb285e4cc04036cb96d`
- Text export: `2026-w47-ko-es.text.md` — 26,696 bytes, 332 items, SHA-256 `ebac600a0af8ee1f0f85bbacd3bae8a8e8fa8bf65413520ca11296b0753ad291`
- `ABSTRACT.txt` — 384 bytes, SHA-256 `383ccd7f7751d1701585eb271d507b5dd626173dca241d74c7bc8c81fb2c8cdf`
- 8 SVGs in `svg/` (hashes in `es/sha-es-run3.txt`).

## Gates (all pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 3) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2457, P7 teaser 2483.7 | `es/build-es-run3.log` |
| boxtitle width | 8/8 titles ≤ 386.5px (apply round 2: P3 `A saber` 317.4px, after `Conviene saber` 408.6px OVER; P2 shopping `Lista de la compra` 385.8px — 0.7px under the limit) | `es/boxtitle-es.log` |
| U+2019 scan (8 SVGs) | 0 | measured inline |
| occlusion audit | **0 flags** (selftest OK, 6 classes fired, clean controls silent) | `es/occlusion-es.json` / `es/occlusion-es.log` |
| p8.py extract | 150/150 noted | `es/p8-extract-es.log`, `es/p8-es.json` |
| p8.py compare vs core | CLEAN, keydiff `[137, 138]` (E-group re-aimed, W46 precedent) | `es/p8-compare-es.log` |
| freeze diff vs core | added CJK 7, all U+3000 (footer) | `es/freeze-diff-es.log` |
| freeze baseline (/usr/bin/python3) | **8/8 byte-identical** | `es/freeze-es.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `es/check-es.log` |
| check_gloss (scratch copy) | gloss fails 0 | `es/check-es.log` |
| print/web text layers | byte-identical, 52,007 bytes each | `es/textlayer-diff-es.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `es/keycheck-es.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `es/style11-es.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `es/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 0 Chinese characters in `<text>` | measured inline |

## Fixes in this edition

1. **Box title wider than the 386.5px inner width** (found by `boxtitle-ko.py` after apply round 1, before any build): P3 `김치의 날에 알아 둘 것　Conviene saber` 408.6px. Shortened to `A saber` (317.4px); re-applied, boxtitle 8/8. P2 shopping `Lista de la compra` 385.8px passes by 0.7px — kept, measured.
2. **P2 matching-instruction EDGE + P8 F-header TEXTX** (found by `occlusion_audit.py` on run-1 build): (a) P2 instr `Relacionar las palabras con las notas` (37 chars, 332px) ran past the right page edge by 17.75px → shortened to `Relacionar palabras y notas`. (b) P8 section-F instr `Relacionar la palabra con su significado` (41 chars) overlapped the F option lines → shortened to `Relacionar palabra y significado`; the audit STILL flagged 2 TEXTX (overlap 103.5px → 34.2px), because the F header sits at x=1185.0 and the option text starts at x=1439.5 — a 254.5px budget, i.e. the header must be ≈21 chars (the en edition uses `Match word to meaning`). Final form `Palabra y significado` (21 chars) → occlusion 0 flags on run 3. The same defect class was swept pre-emptively in it/pt metas (F instr shortened to `Parola e significato` / `Palavra e significado`; it mountain instr to `Abbinare montagna e nota`).
3. **Disk-quota incidents (process, not content):** freeze baseline died rc=120 (EDQUOT) twice — first during run-2 gates, again during run-3 gates — although df shows 45G free (quota, not disk-full). Deleted only reproducible intermediates in my own note dir (partial `es/freeze-es` rebuild dirs, 49M + 17M; en/de/fr `pages/` PNGs, ~28M, reproducible via pdftoppm). Baseline finally passed with `--out /tmp/freeze-es-ko` (tmpfs, 150M free): 8/8 byte-identical; the /tmp rebuild dir was deleted right after. Remaining es gates were run with outputs in /tmp (`/tmp/es-gates/`): freeze diff, checks (via a /tmp copy of check-edition.py with the work dir repointed), textmd, webpdf, P8 font, keycheck, style11, visual pages — ALL PASS. **Not yet landed in the edition/scratch dirs (EDQUOT):** `Lucerna-VOL4-KO-ES-web.pdf` (4,034,870 B, SHA-256 `4abcc6e2…cb96d`, in /tmp/es-gates/), `2026-w47-ko-es.text.md` (26,696 B, 332 items, SHA-256 `ebac600a…ad291`, in /tmp/es-gates/), gate logs `check-es.log`, `textmd-es.log`, `webpdf-es.log`, `freeze-diff-es.log`, `p8font-es.log`, `keycheck-es.log`, `style11-es.log`, `print-es.txt`, `web-es.txt`, `freeze-diff-es.json` (all in /tmp/es-gates/), and this record + WEEKLY-KIT.md (drafts in /tmp/es-gates/). Copy them into place with plain `cp` the moment quota frees; no rebuild needed. Quota is a VM-wide blocker — my note dir is already minimal; freeing space elsewhere is a coordinator decision.

## Adjudicated (not defects — inherited from core or by design)

- P8 match-item notes end with the option letter repeated (`25. d — … 199 456 wones d`): the letter is in the SOURCE note literal itself, core's own convention (`김장비용=四口之家199,456韩元 d` in core-ko); the es map translated the note text and kept the letter.
- #43/#123/#124 note "previsión de Weatheri": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(tarea abierta — texto modelo abajo)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (es): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure replaces `lcn`; `lko`/`lcn2` lines + render lines removed, W46 ko-es precedent).
- text.md 332 items vs core 333: `textmd.py`'s `is_prose` drops the bare 3-letter Latin word "Todo" (P1 contents 8면 row level); the SVG/PDF render "Todo" correctly (visible on the P1 render). Export quirk, not a content gap.
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- P8 answer-note person names: only personal name is 민준 (Minjun, section C protagonist + P8 #129 note) — standard Revised Romanization, consistent within the edition; no sumo-style romaji issue (ja-family class does not apply here). Team/company names (Samsung, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings.
- es was built from the core as modified 2026-11-11 08:40 UTC (content12/34/7), NOT from run-10 as shipped at 08:35: P1 quiz stem `한국시리즈에서 우승한 팀은 어느 팀이에요?`, P4 `한국시리즈 전적은…` (dropped duplicated 시리즈), P7 frame example `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요`. See FANOUT-REPORT-ko.md "core moved" note — ko-fr/ko-en/ko-de are now stale vs this core; coordinator to decide on re-fanout.

## 150-key table (REG from edition sources vs keys extracted from P8 SVG)

| # | Page | Type | Key | Note (Spanish) | SVG |
|---|---|---|---|---|---|
| 1 | 1 | Completar | 1 | 18 nov. = D-1 | OK |
| 2 | 1 | Completar | 김장 | La temporada del kimchi está en pleno apogeo | OK |
| 3 | 1 | Completar | 19 | El CSAT es el jueves 19 nov. | OK |
| 4 | 1 | Completar | 3 | 16 nov. = D-3 | OK |
| 5 | 1 | Completar | 4승 1패 | Samsung ganó a kt 4-1 | OK |
| 6 | 1 | Completar | 11 | Inscripción en plazas libres desde el 11 nov. | OK |
| 7 | 1 | Opción múltiple | A | 18 nov. = D-1 | OK |
| 8 | 1 | Opción múltiple | A | El kimjang cuesta un 9,0 % menos que el año pasado | OK |
| 9 | 1 | Opción múltiple | A | El Día del Kimchi es el domingo 22 nov. | OK |
| 10 | 1 | Opción múltiple | A | Samsung ganó la Serie Coreana | OK |
| 11 | 2 | Opción múltiple | A | 20 repollos: 54 980 wones | OK |
| 12 | 2 | Opción múltiple | A | El kimjang bajó un 9,0 % | OK |
| 13 | 2 | Opción múltiple | A | El Día del Kimchi es el domingo 22 nov. | OK |
| 14 | 2 | Opción múltiple | A | El examen de historia es el sábado 28 nov. | OK |
| 15 | 2 | Opción múltiple | A | El festival WiKim es el viernes 20 nov. | OK |
| 16 | 2 | Completar | 한창 | La temporada del kimchi está en pleno apogeo | OK |
| 17 | 2 | Completar | 22 | El Día del Kimchi es el 22 nov. | OK |
| 18 | 2 | Completar | 54,980 | 20 repollos: 54 980 wones | OK |
| 19 | 2 | Completar | 토 | El examen de historia es un sábado | OK |
| 20 | 2 | Completar | 배추 | Los precios bajaron porque el repollo es más barato | OK |
| 21 | 2 | Completar | 199,456 | Kimjang para cuatro: 199 456 wones | OK |
| 22 | 2 | Completar | 54,980 | 20 repollos: 54 980 wones | OK |
| 23 | 2 | Completar | 26.5 | 20 repollos, un 26,5 % menos que el año pasado | OK |
| 24 | 2 | Completar | 13 | Plazas libres: inscripción del 11 al 13 nov. | OK |
| 25 | 2 | Relacionar | d | 김장비용 = kimjang para cuatro, 199 456 wones d | OK |
| 26 | 2 | Relacionar | a | 김치의 날 = 22 nov. a | OK |
| 27 | 2 | Relacionar | c | 위킴 페스티벌 = 20 nov. en Seúl c | OK |
| 28 | 2 | Relacionar | b | 한능검 = abreviatura del examen de historia b | OK |
| 29 | 3 | Opción múltiple | A | El Día del Kimchi es el 22 nov. | OK |
| 30 | 3 | Opción múltiple | B | 22 son los 22 beneficios del kimchi | OK |
| 31 | 3 | Opción múltiple | A | El festival WiKim es el viernes 20 nov. | OK |
| 32 | 3 | Opción múltiple | B | Naejangsan: pico previsto por el Servicio Forestal el 4 nov. | OK |
| 33 | 3 | Opción múltiple | A | El Servicio Forestal cuenta el 50 % de las hojas | OK |
| 34 | 3 | Completar | 절정 | Las hojas más bonitas se llaman 절정 | OK |
| 35 | 3 | Completar | 예보 | Las fechas previstas difieren de las observadas | OK |
| 36 | 3 | Completar | 관측 | Observado de verdad el 16 oct. | OK |
| 37 | 3 | Completar | 김치의 날 | El 22 nov. es el Día del Kimchi | OK |
| 38 | 3 | Completar | 발효 | El kimchi es un alimento fermentado | OK |
| 39 | 3 | Completar | 22 | El kimchi tiene 22 beneficios | OK |
| 40 | 3 | Completar | 11 | Naejangsan: previsión de Weatheri, 11 nov. | OK |
| 41 | 3 | Completar | 4 | Naejangsan: previsión del Servicio Forestal, 4 nov. | OK |
| 42 | 3 | Completar | 20 | El festival WiKim es el 20 nov. | OK |
| 43 | 3 | Relacionar | b | 내장산 = previsión de Weatheri, 11 nov. b | OK |
| 44 | 3 | Relacionar | a | 월출산 = previsión del Servicio Forestal, 9 nov. a | OK |
| 45 | 3 | Relacionar | d | 두륜산 = previsión del Servicio Forestal, 11 nov. d | OK |
| 46 | 3 | Relacionar | c | 설악산 = observado el 16 oct. c | OK |
| 47 | 4 | Opción múltiple | A | Samsung ganó la Serie Coreana | OK |
| 48 | 4 | Opción múltiple | C | La serie terminó 4-1 | OK |
| 49 | 4 | Opción múltiple | B | Partido 5, 8 nov. en Daegu: Samsung 12-1 | OK |
| 50 | 4 | Opción múltiple | A | Partido 1: kt ganó 8-7 | OK |
| 51 | 4 | Opción múltiple | B | Primer título de Samsung en 12 años | OK |
| 52 | 4 | Completar | 4승 1패 | Samsung ganó a kt 4-1 | OK |
| 53 | 4 | Completar | 수원 | Los partidos 1 y 2 fueron en Suwon | OK |
| 54 | 4 | Completar | 12대 1 | Partido 5: Samsung ganó 12-1 | OK |
| 55 | 4 | Completar | 12 | Samsung volvió a ganar después de 12 años | OK |
| 56 | 4 | Completar | 4연승 | Samsung encadenó cuatro victorias tras una derrota | OK |
| 57 | 4 | Transformar | 삼성이 kt wiz를 이겼어요. | 이기다: pasado 이겼어요 | OK |
| 58 | 4 | Transformar | 1차전이 수원에서 열렸어요. | 열리다: pasado 열렸어요 | OK |
| 59 | 4 | Transformar | 한국시리즈가 끝났어요. | 끝나다: pasado 끝났어요 | OK |
| 60 | 4 | Transformar | 삼성이 5차전에서 이겼어요. | 이기다: pasado 이겼어요 | OK |
| 61 | 4 | Relacionar | c | 준플레이오프 = KIA, tres victorias seguidas c | OK |
| 62 | 4 | Relacionar | d | 플레이오프 = Samsung 3-2 d | OK |
| 63 | 4 | Relacionar | a | 한국시리즈 = Samsung 4-1 a | OK |
| 64 | 4 | Relacionar | b | K리그1 = Seúl, victoria anticipada b | OK |
| 65 | 5 | Opción múltiple | A | La convocatoria previa es el miércoles 18 nov. | OK |
| 66 | 5 | Opción múltiple | B | El CSAT empieza a las 8:40 | OK |
| 67 | 5 | Opción múltiple | A | Candidatos este año: 551 864 | OK |
| 68 | 5 | Opción múltiple | B | Los resultados salen el viernes 11 dic. | OK |
| 69 | 5 | Opción múltiple | A | Entra en tu aula antes de las 8:10 el día del examen | OK |
| 70 | 5 | Completar | 예비소집 | Recoge tu convocatoria en la reunión previa | OK |
| 71 | 5 | Completar | 수험표 | Recoge tu convocatoria y comprueba tu centro | OK |
| 72 | 5 | Completar | 2,310 | 2 310 candidatos menos que el año pasado | OK |
| 73 | 5 | Completar | 성적 | Los resultados salen el 11 dic. | OK |
| 74 | 5 | Completar | 김치의 날 | El 22 nov. es el Día del Kimchi | OK |
| 75 | 5 | Completar | 551,864 | Candidatos este año: 551 864 | OK |
| 76 | 5 | Completar | 1,312 | Centros de examen en todo el país: 1 312 | OK |
| 77 | 5 | Completar | 85 | 85 zonas de examen en todo el país | OK |
| 78 | 5 | Completar | 10 | El día del examen, las oficinas abren a las 10:00 | OK |
| 79 | 5 | Formar frases | 수험생은 열심히 공부해요. | Orden de palabras: sujeto + adverbio + verbo | OK |
| 80 | 5 | Formar frases | 우리는 수험생을 응원해요. | Sujeto + objeto + verbo | OK |
| 81 | 5 | Formar frases | 비행기는 듣기 시간에 뜨지 않아요. | No hay vuelos durante la prueba de escucha | OK |
| 82 | 5 | Formar frases | 친구는 김치를 나눠 줘요. | Un amigo comparte kimchi | OK |
| 83 | 6 | Opción múltiple | B | Esta semana la Serie Coreana ya tiene resultado | OK |
| 84 | 6 | Opción múltiple | A | Encuesta del 9 nov.: el kimjang cuesta 199 456 wones | OK |
| 85 | 6 | Opción múltiple | B | Las fechas previstas de las hojas ya pasaron | OK |
| 86 | 6 | Opción múltiple | C | Los resultados del CSAT salen el 11 dic. | OK |
| 87 | 6 | Opción múltiple | A | La semana pasada la Serie era solo un calendario | OK |
| 88 | 6 | Opción múltiple | A | Partido 1: kt ganó 8-7 | OK |
| 89 | 6 | Opción múltiple | B | El servicio meteorológico observa cerca del 80 % | OK |
| 90 | 6 | Opción múltiple | A | Un repollo, 16 oct.: 5 557 wones | OK |
| 91 | 6 | Opción múltiple | A | La fecha de referencia de la encuesta del kimjang es el 9 nov. | OK |
| 92 | 6 | Opción múltiple | A | Candidatos este año: 551 864 | OK |
| 93 | 6 | Completar | 발표 | Un calendario publicado puede cambiar | OK |
| 94 | 6 | Completar | 결과 | Los resultados llegan solo después de los partidos | OK |
| 95 | 6 | Completar | 기준 | Las fechas difieren porque los criterios difieren | OK |
| 96 | 6 | Completar | 날짜 | Cuando leas las noticias, mira primero la fecha | OK |
| 97 | 6 | Verdadero o falso | 틀리다 | Las medidas especiales valen solo el 19 nov. | OK |
| 98 | 6 | Verdadero o falso | 맞다 | Samsung ganó el título 4-1 | OK |
| 99 | 6 | Verdadero o falso | 틀리다 | Las fechas previstas no son fechas observadas | OK |
| 100 | 6 | Verdadero o falso | 맞다 | Los resultados salen el 11 dic. | OK |
| 101 | 7 | Completar | 김장 | Preparar el kimchi de invierno = 김장 | OK |
| 102 | 7 | Opción múltiple | A | El Día del Kimchi es el 22 nov. | OK |
| 103 | 7 | Completar | 절임배추 | Repollo salado con antelación | OK |
| 104 | 7 | Opción múltiple | A | El aliño lleva gambas saladas | OK |
| 105 | 7 | Completar | D-1 | 18 nov. = D-1 | OK |
| 106 | 7 | Opción múltiple | B | D-3 = 16 nov. | OK |
| 107 | 7 | Completar | 데이 | 19 nov. = D-day | OK |
| 108 | 7 | Opción múltiple | A | D-1: el examen es mañana | OK |
| 109 | 7 | Completar | 기준 | Las fechas difieren porque los criterios difieren (p. 3) | OK |
| 110 | 7 | Opción múltiple | A | El servicio meteorológico observa cerca del 80 % | OK |
| 111 | 7 | Completar | 결과 | Los resultados llegan solo después de los partidos | OK |
| 112 | 7 | Opción múltiple | B | Distingue anuncios y resultados | OK |
| 113 | 8 | Texto con huecos | A | El Día del Kimchi es el domingo 22 nov. | OK |
| 114 | 8 | Texto con huecos | A | El CSAT es el jueves 19 nov. | OK |
| 115 | 8 | Texto con huecos | A | El examen de historia es el sábado 28 nov. | OK |
| 116 | 8 | Texto con huecos | A | El festival WiKim es el viernes 20 nov. | OK |
| 117 | 8 | Texto con huecos | A | Samsung ganó el título 4-1 | OK |
| 118 | 8 | Texto con huecos | A | Kimjang para cuatro: 199 456 wones | OK |
| 119 | 8 | Texto con huecos | A | 20 repollos: 54 980 wones | OK |
| 120 | 8 | Texto con huecos | A | Candidatos este año: 551 864 | OK |
| 121 | 8 | Opción múltiple | A | Candidatos este año: 551 864 | OK |
| 122 | 8 | Opción múltiple | B | Centros de examen en todo el país: 1 312 | OK |
| 123 | 8 | Opción múltiple | A | Naejangsan: pico previsto por el Servicio Forestal el 4 nov. | OK |
| 124 | 8 | Opción múltiple | B | Naejangsan: pico previsto por Weatheri, 11 nov. | OK |
| 125 | 8 | Opción múltiple | B | Duryunsan: pico previsto por el Servicio Forestal, 11 nov. | OK |
| 126 | 8 | Opción múltiple | A | Partido 1: kt ganó 8-7 | OK |
| 127 | 8 | Opción múltiple | A | Plazas libres: inscripción del 11 al 13 nov. | OK |
| 128 | 8 | Opción múltiple | B | La prevención de incendios termina el 15 dic. | OK |
| 129 | 8 | Opción múltiple | B | Minjun va a la convocatoria previa el miércoles | OK |
| 130 | 8 | Opción múltiple | A | Hace el CSAT el jueves | OK |
| 131 | 8 | Opción múltiple | B | Comparte kimchi con su familia el domingo | OK |
| 132 | 8 | Opción múltiple | C | La semana que viene prepara el examen de historia | OK |
| 133 | 8 | Formar frases | 저는 수요일에 예비소집에 가요. | Orden de palabras: sujeto + tiempo + lugar + verbo | OK |
| 134 | 8 | Formar frases | 우리는 김치를 나눠 먹어요. | Sujeto + objeto + verbo | OK |
| 135 | 8 | Formar frases | 민준이는 한국사를 좋아해요. | 좋아하다 = gustar | OK |
| 136 | 8 | Formar frases | 수험생은 도서관에서 공부해요. | Para el lugar de una acción se usa 「에서」 | OK |
| 137 | 8 | Traducir | El 22 nov. es el Día del Kimchi. | Ver p. 2 | OK |
| 138 | 8 | Traducir | Samsung ganó el título después de 12 años. | Ver p. 4 | OK |
| 139 | 8 | Traducir | 11월 18일은 예비소집이에요. | Ver p. 5 | OK |
| 140 | 8 | Traducir | 일요일에는 가족과 김치를 나눠 먹어요. | Ver la sección C, p. 8 | OK |
| 141 | 8 | Relacionar | b | 예비소집 = convocatoria previa b | OK |
| 142 | 8 | Relacionar | c | 김치의 날 = 22 nov. c | OK |
| 143 | 8 | Relacionar | a | 발효 = el proceso de fermentación a | OK |
| 144 | 8 | Relacionar | d | 우승 = título d | OK |
| 145 | 8 | Texto con huecos | A | Va a la convocatoria previa el miércoles | OK |
| 146 | 8 | Texto con huecos | A | El Día del Kimchi es el 22 nov. | OK |
| 147 | 8 | Texto con huecos | A | El examen de historia es el 28 nov. | OK |
| 148 | 8 | Texto con huecos | A | Kimjang para cuatro: 199 456 wones | OK |
| 149 | 8 | Texto con huecos | A | Los resultados salen el 11 dic. | OK |
| 150 | 8 | Escribir | (tarea abierta — texto modelo abajo) | Texto modelo en la sección H de esta página (169 caracteres) | OK ✓ |
