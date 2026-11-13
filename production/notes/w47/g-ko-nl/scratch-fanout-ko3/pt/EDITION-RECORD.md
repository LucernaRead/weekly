# EDITION RECORD — 2026-W47 ko-pt (run 1; 2026-11-11)

- Slug: `2026-w47-ko-pt` (target ko, reader Portuguese). Core: `core-ko` run 11 (fix1) + textmd fix2.
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-pt.json`, `gen-map-pt.py` via `mk-lang.py` + `pt-replace.json` / `pt-meta.json`); apply log `apply-pt.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-PT.pdf` — **45,680,335 bytes**, SHA-256 `358303d15e17c8a2589f3edcad416368720a1f091a560b475180ade171131c74`
- Web PDF: `Lucerna-VOL4-KO-PT-web.pdf` — **4,033,877 bytes** (< 7 MB), SHA-256 `9abb351ca17918574a0f143a4486a8aa9deaaf8ff6e99495ca793c68500ac6da`
- Text export: `2026-w47-ko-pt.text.md` — 35,080 bytes, 449 items, SHA-256 `80cc61ef7bc993f8e3681a971009a72969a4a42b612a6bdca9e8a6216c868ca0`
- `ABSTRACT.txt` — 375 bytes, SHA-256 `56ad1cda0f5af7af5e00d2c6d99b06c78f14494d58945382d7535f7287a3a637`
- 8 SVGs in `svg/` (hashes in `pt/sha-pt-run1.txt`).

## Gates (all pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 1) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2411, P7 teaser 2483.7 | `pt/build-pt-run1.log` |
| boxtitle width | 8/8 titles ≤ 386.5px (P5 shortened in map: Números dos jovens → Números jovens) | `pt/boxtitle-pt.log` |
| U+2019 scan (8 SVGs) | 0 | measured inline |
| occlusion audit | **0 flags** (selftest OK, 6 classes fired, clean controls silent) | `pt/occlusion-pt.json` / `pt/occlusion-pt.log` |
| p8.py extract | 150/150 noted | `pt/p8-extract-pt.log`, `pt/p8-pt.json` |
| p8.py compare vs core | CLEAN, keydiff `[137, 138]` (E-group re-aimed, W46 precedent) | `pt/p8-compare-pt.log` |
| freeze diff vs core | added CJK 7, all U+3000 (footer) | `pt/freeze-diff-pt.log` |
| freeze baseline (/usr/bin/python3) | **8/8 byte-identical** | `pt/freeze-pt.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `pt/check-pt.log` |
| check_gloss (scratch copy) | gloss fails 0 | `pt/check-pt.log` |
| print/web text layers | byte-identical, 51,790 bytes each | `pt/textlayer-diff-pt.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `pt/keycheck-pt.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `pt/style11-pt.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `pt/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 0 Chinese characters in `<text>` | measured inline |

## Fixes in this edition

1. **P5 box title (pt, run 1):** `이번 주 청년 숫자　Números dos jovens` measured 414.3px over the 386.5px inner width. Shortened in the map source (`pt-replace.json`, then `mk-lang.py pt` + `gen-map-pt.py` + re-apply) to `Números jovens`; boxtitle 8/8 before the build. Same map-source discipline as it: `mk-lang.py pt` must regenerate the gen-map script first.
2. **Frame line clean at map level:** `content7.py:81` is `Quadro: 「depois de ~」. Pergunta: 「〜 후에 뭐 해요?」` straight from the map — no post-apply fix needed. Post-build sweep: U+201C = 0, U+201D = 0, U+2019 = 0 across all 8 SVGs + text.md; the 「」 form is visible in the P7 render and in text.md line 761.
3. **New edition (fan-out #3):** built from the finalized core run 11 (fix1) + fixed textmd.py re-export. No prior pt edition existed.

## Adjudicated (not defects — inherited from core or by design)

- P8 match-item notes end with the option letter repeated: the letter is in the source note literal itself, core's own convention.
- #43/#123/#124 note "previsão da Weatheri": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(tarefa livre — texto modelo abaixo)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (pt): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 449 items vs core 452: three accounted drops, no content gap — (1) `is_prose` drops the bare 4-letter Latin word "Tudo" (P1 contents 8면 row level; the SVG/PDF render "Tudo" correctly, visible on the P1 render); (2) `lcn2` removed by design; (3) `lko` removed by design. Same pattern as en/de/es/fr/it.
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style.
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.

## 150-key table (REG from edition sources vs keys extracted from P8 SVG)

| # | Page | Type | Key | Note (Portuguese) | SVG |
|---|---|---|---|---|---|
| 1 | 1 | Completar | 1 | 18 nov. = D-1 | OK |
| 2 | 1 | Completar | 김장 | A época do kimchi está em pleno auge | OK |
| 3 | 1 | Completar | 19 | O CSAT é na quinta-feira, 19 nov. | OK |
| 4 | 1 | Completar | 3 | 16 nov. = D-3 | OK |
| 5 | 1 | Completar | 4승 1패 | O Samsung venceu o kt 4-1 | OK |
| 6 | 1 | Completar | 11 | Inscrição em vagas livres a partir de 11 nov. | OK |
| 7 | 1 | Escolha múltipla | A | 18 nov. = D-1 | OK |
| 8 | 1 | Escolha múltipla | A | O kimjang custa menos 9,0 % do que no ano passado | OK |
| 9 | 1 | Escolha múltipla | A | O Dia do Kimchi é no domingo, 22 nov. | OK |
| 10 | 1 | Escolha múltipla | A | O Samsung venceu a Série Coreana | OK |
| 11 | 2 | Escolha múltipla | A | 20 repolhos: 54 980 wons | OK |
| 12 | 2 | Escolha múltipla | A | O kimjang baixou 9,0 % | OK |
| 13 | 2 | Escolha múltipla | A | O Dia do Kimchi é no domingo, 22 nov. | OK |
| 14 | 2 | Escolha múltipla | A | O exame de história é no sábado, 28 nov. | OK |
| 15 | 2 | Escolha múltipla | A | O Festival WiKim é na sexta-feira, 20 nov. | OK |
| 16 | 2 | Completar | 한창 | A época do kimchi está em pleno auge | OK |
| 17 | 2 | Completar | 22 | O Dia do Kimchi é a 22 nov. | OK |
| 18 | 2 | Completar | 54,980 | 20 repolhos: 54 980 wons | OK |
| 19 | 2 | Completar | 토 | O exame de história é ao sábado | OK |
| 20 | 2 | Completar | 배추 | Os preços baixaram porque o repolho está mais barato | OK |
| 21 | 2 | Completar | 199,456 | Kimjang para quatro: 199 456 wons | OK |
| 22 | 2 | Completar | 54,980 | 20 repolhos: 54 980 wons | OK |
| 23 | 2 | Completar | 26.5 | 20 repolhos, menos 26,5 % do que no ano passado | OK |
| 24 | 2 | Completar | 13 | Vagas livres: inscrição de 11 a 13 nov. | OK |
| 25 | 2 | Ligar | d | 김장비용 = kimjang para quatro, 199 456 wons d | OK |
| 26 | 2 | Ligar | a | 김치의 날 = 22 nov. a | OK |
| 27 | 2 | Ligar | c | 위킴 페스티벌 = 20 nov. em Seul c | OK |
| 28 | 2 | Ligar | b | 한능검 = abreviatura do exame de história b | OK |
| 29 | 3 | Escolha múltipla | A | O Dia do Kimchi é a 22 nov. | OK |
| 30 | 3 | Escolha múltipla | B | 22 são os 22 benefícios do kimchi | OK |
| 31 | 3 | Escolha múltipla | A | O Festival WiKim é na sexta-feira, 20 nov. | OK |
| 32 | 3 | Escolha múltipla | B | Naejangsan: pico previsto pelo Serviço Florestal a 4 nov. | OK |
| 33 | 3 | Escolha múltipla | A | O Serviço Florestal conta 50 % das folhas | OK |
| 34 | 3 | Completar | 절정 | As folhas mais bonitas chamam-se 절정 | OK |
| 35 | 3 | Completar | 예보 | As datas previstas diferem das observadas | OK |
| 36 | 3 | Completar | 관측 | Observado de facto a 16 out. | OK |
| 37 | 3 | Completar | 김치의 날 | A 22 nov. é o Dia do Kimchi | OK |
| 38 | 3 | Completar | 발효 | O kimchi é um alimento fermentado | OK |
| 39 | 3 | Completar | 22 | O kimchi tem 22 benefícios | OK |
| 40 | 3 | Completar | 11 | Naejangsan: previsão da Weatheri, 11 nov. | OK |
| 41 | 3 | Completar | 4 | Naejangsan: previsão do Serviço Florestal, 4 nov. | OK |
| 42 | 3 | Completar | 20 | O Festival WiKim é a 20 nov. | OK |
| 43 | 3 | Ligar | b | 내장산 = previsão da Weatheri, 11 nov. b | OK |
| 44 | 3 | Ligar | a | 월출산 = previsão do Serviço Florestal, 9 nov. a | OK |
| 45 | 3 | Ligar | d | 두륜산 = previsão do Serviço Florestal, 11 nov. d | OK |
| 46 | 3 | Ligar | c | 설악산 = observado a 16 out. c | OK |
| 47 | 4 | Escolha múltipla | A | O Samsung venceu a Série Coreana | OK |
| 48 | 4 | Escolha múltipla | C | A série terminou 4-1 | OK |
| 49 | 4 | Escolha múltipla | B | Jogo 5, 8 nov. em Daegu: Samsung 12-1 | OK |
| 50 | 4 | Escolha múltipla | A | Jogo 1: o kt venceu 8-7 | OK |
| 51 | 4 | Escolha múltipla | B | O primeiro título do Samsung em 12 anos | OK |
| 52 | 4 | Completar | 4승 1패 | O Samsung venceu o kt 4-1 | OK |
| 53 | 4 | Completar | 수원 | Os jogos 1 e 2 foram em Suwon | OK |
| 54 | 4 | Completar | 12대 1 | Jogo 5: o Samsung venceu 12-1 | OK |
| 55 | 4 | Completar | 12 | O Samsung voltou a vencer após 12 anos | OK |
| 56 | 4 | Completar | 4연승 | O Samsung venceu quatro seguidas após uma derrota | OK |
| 57 | 4 | Transformar | 삼성이 kt wiz를 이겼어요. | 이기다: passado 이겼어요 | OK |
| 58 | 4 | Transformar | 1차전이 수원에서 열렸어요. | 열리다: passado 열렸어요 | OK |
| 59 | 4 | Transformar | 한국시리즈가 끝났어요. | 끝나다: passado 끝났어요 | OK |
| 60 | 4 | Transformar | 삼성이 5차전에서 이겼어요. | 이기다: passado 이겼어요 | OK |
| 61 | 4 | Ligar | c | 준플레이오프 = KIA, três vitórias seguidas c | OK |
| 62 | 4 | Ligar | d | 플레이오프 = Samsung 3-2 d | OK |
| 63 | 4 | Ligar | a | 한국시리즈 = Samsung 4-1 a | OK |
| 64 | 4 | Ligar | b | K리그1 = Seul, vitória antecipada b | OK |
| 65 | 5 | Escolha múltipla | A | A convocação prévia é na quarta-feira, 18 nov. | OK |
| 66 | 5 | Escolha múltipla | B | O CSAT começa às 8:40 | OK |
| 67 | 5 | Escolha múltipla | A | Candidatos este ano: 551 864 | OK |
| 68 | 5 | Escolha múltipla | B | Os resultados saem na sexta-feira, 11 dez. | OK |
| 69 | 5 | Escolha múltipla | A | Entra na tua sala até às 8:10 no dia do exame | OK |
| 70 | 5 | Completar | 예비소집 | Levanta o teu cartão na convocação prévia | OK |
| 71 | 5 | Completar | 수험표 | Levanta o teu cartão e confirma o teu centro | OK |
| 72 | 5 | Completar | 2,310 | 2 310 candidatos a menos do que no ano passado | OK |
| 73 | 5 | Completar | 성적 | Os resultados saem a 11 dez. | OK |
| 74 | 5 | Completar | 김치의 날 | A 22 nov. é o Dia do Kimchi | OK |
| 75 | 5 | Completar | 551,864 | Candidatos este ano: 551 864 | OK |
| 76 | 5 | Completar | 1,312 | Centros de exame em todo o país: 1 312 | OK |
| 77 | 5 | Completar | 85 | 85 zonas de exame em todo o país | OK |
| 78 | 5 | Completar | 10 | No dia do exame, os gabinetes abrem às 10:00 | OK |
| 79 | 5 | Formar frases | 수험생은 열심히 공부해요. | Ordem das palavras: sujeito + advérbio + verbo | OK |
| 80 | 5 | Formar frases | 우리는 수험생을 응원해요. | Sujeito + objeto + verbo | OK |
| 81 | 5 | Formar frases | 비행기는 듣기 시간에 뜨지 않아요. | Não há voos durante o teste de audição | OK |
| 82 | 5 | Formar frases | 친구는 김치를 나눠 줘요. | Um amigo partilha kimchi | OK |
| 83 | 6 | Escolha múltipla | B | Esta semana a Série Coreana já tem resultado | OK |
| 84 | 6 | Escolha múltipla | A | Sondagem de 9 nov.: o kimjang custa 199 456 wons | OK |
| 85 | 6 | Escolha múltipla | B | As datas previstas das folhas já passaram | OK |
| 86 | 6 | Escolha múltipla | C | Os resultados do CSAT saem a 11 dez. | OK |
| 87 | 6 | Escolha múltipla | A | Na semana passada a Série era só um calendário | OK |
| 88 | 6 | Escolha múltipla | A | Jogo 1: o kt venceu 8-7 | OK |
| 89 | 6 | Escolha múltipla | B | O serviço meteorológico observa cerca de 80 % | OK |
| 90 | 6 | Escolha múltipla | A | Um repolho, 16 out.: 5 557 wons | OK |
| 91 | 6 | Escolha múltipla | A | A data de referência da sondagem do kimjang é 9 nov. | OK |
| 92 | 6 | Escolha múltipla | A | Candidatos este ano: 551 864 | OK |
| 93 | 6 | Completar | 발표 | Um calendário publicado pode mudar | OK |
| 94 | 6 | Completar | 결과 | Os resultados só chegam depois dos jogos | OK |
| 95 | 6 | Completar | 기준 | As datas diferem porque os critérios diferem | OK |
| 96 | 6 | Completar | 날짜 | Quando leres as notícias, vê primeiro a data | OK |
| 97 | 6 | Verdadeiro ou falso | 틀리다 | As medidas especiais valem só a 19 nov. | OK |
| 98 | 6 | Verdadeiro ou falso | 맞다 | O Samsung venceu o título 4-1 | OK |
| 99 | 6 | Verdadeiro ou falso | 틀리다 | As datas previstas não são datas observadas | OK |
| 100 | 6 | Verdadeiro ou falso | 맞다 | Os resultados saem a 11 dez. | OK |
| 101 | 7 | Completar | 김장 | Preparar o kimchi de inverno = 김장 | OK |
| 102 | 7 | Escolha múltipla | A | O Dia do Kimchi é a 22 nov. | OK |
| 103 | 7 | Completar | 절임배추 | Repolho salgado com antecedência | OK |
| 104 | 7 | Escolha múltipla | A | O tempero leva camarão salgado | OK |
| 105 | 7 | Completar | D-1 | 18 nov. = D-1 | OK |
| 106 | 7 | Escolha múltipla | B | D-3 = 16 nov. | OK |
| 107 | 7 | Completar | 데이 | 19 nov. = D-day | OK |
| 108 | 7 | Escolha múltipla | A | D-1: o exame é amanhã | OK |
| 109 | 7 | Completar | 기준 | As datas diferem porque os critérios diferem (p. 3) | OK |
| 110 | 7 | Escolha múltipla | A | O serviço meteorológico observa cerca de 80 % | OK |
| 111 | 7 | Completar | 결과 | Os resultados só chegam depois dos jogos | OK |
| 112 | 7 | Escolha múltipla | B | Distingue anúncios e resultados | OK |
| 113 | 8 | Texto com lacunas | A | O Dia do Kimchi é no domingo, 22 nov. | OK |
| 114 | 8 | Texto com lacunas | A | O CSAT é na quinta-feira, 19 nov. | OK |
| 115 | 8 | Texto com lacunas | A | O exame de história é no sábado, 28 nov. | OK |
| 116 | 8 | Texto com lacunas | A | O Festival WiKim é na sexta-feira, 20 nov. | OK |
| 117 | 8 | Texto com lacunas | A | O Samsung venceu o título 4-1 | OK |
| 118 | 8 | Texto com lacunas | A | Kimjang para quatro: 199 456 wons | OK |
| 119 | 8 | Texto com lacunas | A | 20 repolhos: 54 980 wons | OK |
| 120 | 8 | Texto com lacunas | A | Candidatos este ano: 551 864 | OK |
| 121 | 8 | Escolha múltipla | A | Candidatos este ano: 551 864 | OK |
| 122 | 8 | Escolha múltipla | B | Centros de exame em todo o país: 1 312 | OK |
| 123 | 8 | Escolha múltipla | A | Naejangsan: pico previsto pelo Serviço Florestal a 4 nov. | OK |
| 124 | 8 | Escolha múltipla | B | Naejangsan: pico previsto pela Weatheri, 11 nov. | OK |
| 125 | 8 | Escolha múltipla | B | Duryunsan: pico previsto pelo Serviço Florestal, 11 nov. | OK |
| 126 | 8 | Escolha múltipla | A | Jogo 1: o kt venceu 8-7 | OK |
| 127 | 8 | Escolha múltipla | A | Vagas livres: inscrição de 11 a 13 nov. | OK |
| 128 | 8 | Escolha múltipla | B | A prevenção de incêndios termina a 15 dez. | OK |
| 129 | 8 | Escolha múltipla | B | O Minjun vai à convocação prévia na quarta-feira | OK |
| 130 | 8 | Escolha múltipla | A | Ele faz o CSAT na quinta-feira | OK |
| 131 | 8 | Escolha múltipla | B | Ele partilha kimchi com a família no domingo | OK |
| 132 | 8 | Escolha múltipla | C | Na próxima semana ele prepara o exame de história | OK |
| 133 | 8 | Formar frases | 저는 수요일에 예비소집에 가요. | Ordem das palavras: sujeito + tempo + lugar + verbo | OK |
| 134 | 8 | Formar frases | 우리는 김치를 나눠 먹어요. | Sujeito + objeto + verbo | OK |
| 135 | 8 | Formar frases | 민준이는 한국사를 좋아해요. | 좋아하다 = gostar | OK |
| 136 | 8 | Formar frases | 수험생은 도서관에서 공부해요. | Para o lugar de uma ação usa-se 「에서」 | OK |
| 137 | 8 | Traduzir | A 22 nov. é o Dia do Kimchi. | Ver p. 2 | OK |
| 138 | 8 | Traduzir | O Samsung venceu o título após 12 anos. | Ver p. 4 | OK |
| 139 | 8 | Traduzir | 11월 18일은 예비소집이에요. | Ver p. 5 | OK |
| 140 | 8 | Traduzir | 일요일에는 가족과 김치를 나눠 먹어요. | Ver a seção C, p. 8 | OK |
| 141 | 8 | Ligar | b | 예비소집 = convocação prévia b | OK |
| 142 | 8 | Ligar | c | 김치의 날 = 22 nov. c | OK |
| 143 | 8 | Ligar | a | 발효 = o processo de fermentação a | OK |
| 144 | 8 | Ligar | d | 우승 = título d | OK |
| 145 | 8 | Texto com lacunas | A | Ele vai à convocação prévia na quarta-feira | OK |
| 146 | 8 | Texto com lacunas | A | O Dia do Kimchi é a 22 nov. | OK |
| 147 | 8 | Texto com lacunas | A | O exame de história é a 28 nov. | OK |
| 148 | 8 | Texto com lacunas | A | Kimjang para quatro: 199 456 wons | OK |
| 149 | 8 | Texto com lacunas | A | Os resultados saem a 11 dez. | OK |
| 150 | 8 | Escrever | (tarefa livre — texto modelo abaixo) | Texto modelo na seção H desta página (169 caracteres) | OK ✓ |
