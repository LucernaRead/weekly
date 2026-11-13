# EDITION RECORD — 2026-W47 ko-fr (run 1; 2026-11-11)

- Slug: `2026-w47-ko-fr` (target ko, reader French). Core: `core-ko` run 11 (fix1) + textmd fix2.
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-fr.json`, `gen-map-fr.py` via `mk-lang.py` + `fr-replace.json` / `fr-meta.json`); apply log `apply-fr.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-FR.pdf` — **45,468,252 bytes**, SHA-256 `e4db2a54a97f2d4a0c5f949617d7760055832e3096076599d15c16e40d98bdc2`
- Web PDF: `Lucerna-VOL4-KO-FR-web.pdf` — **4,022,321 bytes** (< 7 MB), SHA-256 `a5f712d25aa52a65d967bba45966bffe22d39b231098b37924cd0f0458c0cbc9`
- Text export: `2026-w47-ko-fr.text.md` — 35,275 bytes, 449 items, SHA-256 `4e5487a69ec8c6584f90d9674f16775696daf55cb892af88203c700f6c59f378`
- `ABSTRACT.txt` — 378 bytes, SHA-256 `d34aecc9380d252bd3f669b6306e47e85bcdccbd1b0971bbf6297b1d055b5054`
- 8 SVGs in `svg/` (hashes in `fr/sha-fr-run1.txt`).

## Gates (all pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 1) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2426, P7 teaser 2510.22 | `fr/build-fr-run1.log` |
| boxtitle width | 8/8 titles ≤ 386.5px (no shortening needed) | `fr/boxtitle-fr.log` |
| U+2019 scan (8 SVGs) | 0 | measured inline |
| occlusion audit | **0 flags** (selftest OK, 6 classes fired, clean controls silent) | `fr/occlusion-fr.json` / `fr/occlusion-fr.log` |
| p8.py extract | 150/150 noted | `fr/p8-extract-fr.log`, `fr/p8-fr.json` |
| p8.py compare vs core | CLEAN, keydiff `[137, 138]` (E-group re-aimed, W46 precedent) | `fr/p8-compare-fr.log` |
| freeze diff vs core | added CJK 7, all U+3000 (footer) | `fr/freeze-diff-fr.log` |
| freeze baseline (/usr/bin/python3) | **8/8 byte-identical** | `fr/freeze-fr.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `fr/check-fr.log` |
| check_gloss (scratch copy) | gloss fails 0 | `fr/check-fr.log` |
| print/web text layers | byte-identical, 52,304 bytes each | `fr/textlayer-diff-fr.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `fr/keycheck-fr.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `fr/style11-fr.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `fr/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 0 Chinese characters in `<text>` | measured inline |

## Fixes in this edition

1. **Frame curly quotes (ko3):** the map reproduces curly double quotes U+201C/U+201D in `content7.py:81` (`Cadre : “après ~”. Demandez : “〜 후에 뭐 해요?”`). Re-applied the core-style 「」 form `Cadre : 「après ~」. Demandez : 「〜 후에 뭐 해요?」` post-apply, before building. Post-build sweep: U+201C = 0, U+201D = 0, U+2019 = 0 across all 8 SVGs + text.md; the 「」 form is visible in the P7 render and in text.md line 761.
2. **Core D2/D3/D4 flow through the rebuild (old fr was stale):** the #2 fr was built from the PRE-08:40 core (run 10). This rebuild brings it to the finalized core run 11: P1 quiz #10 `어느 팀이에요`, P4 #47 `어느 팀이에요` + #48 without the duplicated `시리즈`, P7 frame example + phrase #7 now the new sentence `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요` (1면) — all verified in the renders and in check_core phrases 8/8 verbatim. SVG footprint vs #2 run 1: exactly P1/P4/P7 changed; P2/P3/P5/P6/P8 byte-identical.
3. **SHA difference vs the old edition, explained:** print 45,468,290 B `ef842955…` → 45,468,252 B `e4db2a54…` (−38 B) = P1/P4/P7 core fixes + the P7 Frame 「」 fix. Web 4,024,760 B `adcaba49…` → 4,022,321 B `a5f712d2…` (−2,439 B) = the same subset regeneration (text bytes 52,232 → 52,304, +72: the new core sentences are longer). Text.md 26,727 B / 332 items `fabcc1c3…` → 35,275 B / 449 items `4e5487a6…` = the fixed textmd.py re-export.

## Adjudicated (not defects — inherited from core or by design)

- P8 match-item notes end with the option letter repeated: the letter is in the source note literal itself, core's own convention.
- #43/#123/#124 note "prévisions Weatheri": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(tâche libre — texte modèle ci-dessous)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (fr): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure).
- text.md 449 items vs core 452: three accounted drops, no content gap — (1) `is_prose` drops the bare 3-letter Latin word "Tout" (P1 contents 8면 row level; the SVG/PDF render "Tout" correctly, visible on the P1 render); (2) `lcn2` removed by design; (3) `lko` removed by design. Same pattern as en/de/es.
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style.
- P8 answer-note stem 10.35pt is the recorded core adjudication — not a defect, not changed.

## 150-key table (REG from edition sources vs keys extracted from P8 SVG)

| # | Page | Type | Key | Note (French) | SVG |
|---|---|---|---|---|---|
| 1 | 1 | Compléter | 1 | 18 nov. = D-1 | OK |
| 2 | 1 | Compléter | 김장 | La saison du kimchi bat son plein | OK |
| 3 | 1 | Compléter | 19 | Le CSAT, c'est le jeudi 19 nov. | OK |
| 4 | 1 | Compléter | 3 | 16 nov. = D-3 | OK |
| 5 | 1 | Compléter | 4승 1패 | Samsung a battu kt 4-1 | OK |
| 6 | 1 | Compléter | 11 | Inscriptions sur places libérées dès le 11 nov. | OK |
| 7 | 1 | Choix multiple | A | 18 nov. = D-1 | OK |
| 8 | 1 | Choix multiple | A | Le kimjang coûte 9,0 % de moins que l'an dernier | OK |
| 9 | 1 | Choix multiple | A | Le Jour du kimchi, c'est le dimanche 22 nov. | OK |
| 10 | 1 | Choix multiple | A | Samsung a gagné la Korean Series | OK |
| 11 | 2 | Choix multiple | A | 20 choux : 54 980 wons | OK |
| 12 | 2 | Choix multiple | A | Le kimjang a baissé de 9,0 % | OK |
| 13 | 2 | Choix multiple | A | Le Jour du kimchi, c'est le dimanche 22 nov. | OK |
| 14 | 2 | Choix multiple | A | L'examen d'histoire, c'est le samedi 28 nov. | OK |
| 15 | 2 | Choix multiple | A | Le festival WiKim, c'est le vendredi 20 nov. | OK |
| 16 | 2 | Compléter | 한창 | La saison du kimchi bat son plein | OK |
| 17 | 2 | Compléter | 22 | Le Jour du kimchi, c'est le 22 nov. | OK |
| 18 | 2 | Compléter | 54,980 | 20 choux : 54 980 wons | OK |
| 19 | 2 | Compléter | 토 | L'examen d'histoire a lieu un samedi | OK |
| 20 | 2 | Compléter | 배추 | Les prix ont baissé car le chou est moins cher | OK |
| 21 | 2 | Compléter | 199,456 | Kimjang pour quatre : 199 456 wons | OK |
| 22 | 2 | Compléter | 54,980 | 20 choux : 54 980 wons | OK |
| 23 | 2 | Compléter | 26.5 | 20 choux, moins 26,5 % par rapport à l'an dernier | OK |
| 24 | 2 | Compléter | 13 | Places libérées : inscriptions du 11 au 13 nov. | OK |
| 25 | 2 | Apparier | d | 김장비용 = kimjang pour quatre, 199 456 wons d | OK |
| 26 | 2 | Apparier | a | 김치의 날 = 22 nov. a | OK |
| 27 | 2 | Apparier | c | 위킴 페스티벌 = 20 nov. à Séoul c | OK |
| 28 | 2 | Apparier | b | 한능검 = abrév. de l'examen d'histoire b | OK |
| 29 | 3 | Choix multiple | A | Le Jour du kimchi, c'est le 22 nov. | OK |
| 30 | 3 | Choix multiple | B | 22, ce sont les 22 bienfaits du kimchi | OK |
| 31 | 3 | Choix multiple | A | Le festival WiKim, c'est le vendredi 20 nov. | OK |
| 32 | 3 | Choix multiple | B | Naejangsan : pic prévu par l'Office des forêts le 4 nov. | OK |
| 33 | 3 | Choix multiple | A | L'Office des forêts compte 50 % des feuilles | OK |
| 34 | 3 | Compléter | 절정 | Les plus belles feuilles s'appellent 절정 | OK |
| 35 | 3 | Compléter | 예보 | Les dates prévues diffèrent des dates observées | OK |
| 36 | 3 | Compléter | 관측 | Vraiment observé le 16 oct. | OK |
| 37 | 3 | Compléter | 김치의 날 | Le 22 nov., c'est le Jour du kimchi | OK |
| 38 | 3 | Compléter | 발효 | Le kimchi est un aliment fermenté | OK |
| 39 | 3 | Compléter | 22 | Le kimchi a 22 bienfaits | OK |
| 40 | 3 | Compléter | 11 | Naejangsan : prévisions Weatheri, 11 nov. | OK |
| 41 | 3 | Compléter | 4 | Naejangsan : prévisions de l'Office des forêts, 4 nov. | OK |
| 42 | 3 | Compléter | 20 | Le festival WiKim, c'est le 20 nov. | OK |
| 43 | 3 | Apparier | b | 내장산 = prévisions Weatheri, 11 nov. b | OK |
| 44 | 3 | Apparier | a | 월출산 = prévisions de l'Office des forêts, 9 nov. a | OK |
| 45 | 3 | Apparier | d | 두륜산 = prévisions de l'Office des forêts, 11 nov. d | OK |
| 46 | 3 | Apparier | c | 설악산 = observé le 16 oct. c | OK |
| 47 | 4 | Choix multiple | A | Samsung a gagné la Korean Series | OK |
| 48 | 4 | Choix multiple | C | La série s'est terminée 4-1 | OK |
| 49 | 4 | Choix multiple | B | Match 5, 8 nov. à Daegu : Samsung 12-1 | OK |
| 50 | 4 | Choix multiple | A | Match 1 : kt a gagné 8-7 | OK |
| 51 | 4 | Choix multiple | B | Premier titre de Samsung depuis 12 ans | OK |
| 52 | 4 | Compléter | 4승 1패 | Samsung a battu kt 4-1 | OK |
| 53 | 4 | Compléter | 수원 | Les matches 1 et 2 ont eu lieu à Suwon | OK |
| 54 | 4 | Compléter | 12대 1 | Match 5 : Samsung a gagné 12-1 | OK |
| 55 | 4 | Compléter | 12 | Samsung a gagné de nouveau après 12 ans | OK |
| 56 | 4 | Compléter | 4연승 | Samsung a enchaîné quatre victoires après une défaite | OK |
| 57 | 4 | Transformer | 삼성이 kt wiz를 이겼어요. | 이기다 : passé 이겼어요 | OK |
| 58 | 4 | Transformer | 1차전이 수원에서 열렸어요. | 열리다 : passé 열렸어요 | OK |
| 59 | 4 | Transformer | 한국시리즈가 끝났어요. | 끝나다 : passé 끝났어요 | OK |
| 60 | 4 | Transformer | 삼성이 5차전에서 이겼어요. | 이기다 : passé 이겼어요 | OK |
| 61 | 4 | Apparier | c | 준플레이오프 = KIA, trois victoires de suite c | OK |
| 62 | 4 | Apparier | d | 플레이오프 = Samsung 3-2 d | OK |
| 63 | 4 | Apparier | a | 한국시리즈 = Samsung 4-1 a | OK |
| 64 | 4 | Apparier | b | K리그1 = Séoul, victoire anticipée b | OK |
| 65 | 5 | Choix multiple | A | La convocation préalable, c'est le mercredi 18 nov. | OK |
| 66 | 5 | Choix multiple | B | Le CSAT commence à 8 h 40 | OK |
| 67 | 5 | Choix multiple | A | Candidats cette année : 551 864 | OK |
| 68 | 5 | Choix multiple | B | Les résultats sortent le vendredi 11 déc. | OK |
| 69 | 5 | Choix multiple | A | Soyez dans votre salle avant 8 h 10 le jour de l'examen | OK |
| 70 | 5 | Compléter | 예비소집 | Retirez votre convocation à la réunion préalable | OK |
| 71 | 5 | Compléter | 수험표 | Retirez votre convocation et vérifiez votre centre | OK |
| 72 | 5 | Compléter | 2,310 | 2 310 candidats de moins que l'an dernier | OK |
| 73 | 5 | Compléter | 성적 | Les résultats sortent le 11 déc. | OK |
| 74 | 5 | Compléter | 김치의 날 | Le 22 nov., c'est le Jour du kimchi | OK |
| 75 | 5 | Compléter | 551,864 | Candidats cette année : 551 864 | OK |
| 76 | 5 | Compléter | 1,312 | Centres d'examen dans tout le pays : 1 312 | OK |
| 77 | 5 | Compléter | 85 | 85 zones d'examen dans tout le pays | OK |
| 78 | 5 | Compléter | 10 | Le jour de l'examen, les bureaux ouvrent à 10 h | OK |
| 79 | 5 | Faire des phrases | 수험생은 열심히 공부해요. | Ordre des mots : sujet + adverbe + verbe | OK |
| 80 | 5 | Faire des phrases | 우리는 수험생을 응원해요. | Sujet + objet + verbe | OK |
| 81 | 5 | Faire des phrases | 비행기는 듣기 시간에 뜨지 않아요. | Pas de vols pendant l'épreuve d'écoute | OK |
| 82 | 5 | Faire des phrases | 친구는 김치를 나눠 줘요. | Un ami partage le kimchi | OK |
| 83 | 6 | Choix multiple | B | Cette semaine, la Korean Series a un résultat | OK |
| 84 | 6 | Choix multiple | A | Enquête du 9 nov. : le kimjang coûte 199 456 wons | OK |
| 85 | 6 | Choix multiple | B | Les dates de feuillages prévues sont passées | OK |
| 86 | 6 | Choix multiple | C | Les résultats du CSAT sortent le 11 déc. | OK |
| 87 | 6 | Choix multiple | A | La semaine dernière, la Series n'était qu'un calendrier | OK |
| 88 | 6 | Choix multiple | A | Match 1 : kt a gagné 8-7 | OK |
| 89 | 6 | Choix multiple | B | Le service météo observe environ 80 % | OK |
| 90 | 6 | Choix multiple | A | Un chou, 16 oct. : 5 557 wons | OK |
| 91 | 6 | Choix multiple | A | La date de référence de l'enquête kimjang, c'est le 9 nov. | OK |
| 92 | 6 | Choix multiple | A | Candidats cette année : 551 864 | OK |
| 93 | 6 | Compléter | 발표 | Un calendrier publié peut changer | OK |
| 94 | 6 | Compléter | 결과 | Les résultats ne viennent qu'après les matches | OK |
| 95 | 6 | Compléter | 기준 | Les dates diffèrent parce que les critères diffèrent | OK |
| 96 | 6 | Compléter | 날짜 | Quand vous lisez les infos, vérifiez d'abord la date | OK |
| 97 | 6 | Vrai ou faux | 틀리다 | Les mesures spéciales ne valent que le 19 nov. | OK |
| 98 | 6 | Vrai ou faux | 맞다 | Samsung a gagné le titre 4-1 | OK |
| 99 | 6 | Vrai ou faux | 틀리다 | Les dates prévues ne sont pas des dates observées | OK |
| 100 | 6 | Vrai ou faux | 맞다 | Les résultats sortent le 11 déc. | OK |
| 101 | 7 | Compléter | 김장 | Préparer le kimchi d'hiver = 김장 | OK |
| 102 | 7 | Choix multiple | A | Le Jour du kimchi, c'est le 22 nov. | OK |
| 103 | 7 | Compléter | 절임배추 | Chou salé à l'avance | OK |
| 104 | 7 | Choix multiple | A | L'assaisonnement contient des crevettes salées | OK |
| 105 | 7 | Compléter | D-1 | 18 nov. = D-1 | OK |
| 106 | 7 | Choix multiple | B | D-3 = 16 nov. | OK |
| 107 | 7 | Compléter | 데이 | 19 nov. = D-day | OK |
| 108 | 7 | Choix multiple | A | D-1 : l'examen, c'est demain | OK |
| 109 | 7 | Compléter | 기준 | Les dates diffèrent parce que les critères diffèrent (p. 3) | OK |
| 110 | 7 | Choix multiple | A | Le service météo observe environ 80 % | OK |
| 111 | 7 | Compléter | 결과 | Les résultats ne viennent qu'après les matches | OK |
| 112 | 7 | Choix multiple | B | Distinguer annonces et résultats | OK |
| 113 | 8 | Texte à trous | A | Le Jour du kimchi, c'est le dimanche 22 nov. | OK |
| 114 | 8 | Texte à trous | A | Le CSAT, c'est le jeudi 19 nov. | OK |
| 115 | 8 | Texte à trous | A | L'examen d'histoire, c'est le samedi 28 nov. | OK |
| 116 | 8 | Texte à trous | A | Le festival WiKim, c'est le vendredi 20 nov. | OK |
| 117 | 8 | Texte à trous | A | Samsung a gagné le titre 4-1 | OK |
| 118 | 8 | Texte à trous | A | Kimjang pour quatre : 199 456 wons | OK |
| 119 | 8 | Texte à trous | A | 20 choux : 54 980 wons | OK |
| 120 | 8 | Texte à trous | A | Candidats cette année : 551 864 | OK |
| 121 | 8 | Choix multiple | A | Candidats cette année : 551 864 | OK |
| 122 | 8 | Choix multiple | B | Centres d'examen dans tout le pays : 1 312 | OK |
| 123 | 8 | Choix multiple | A | Naejangsan : pic prévu par l'Office des forêts le 4 nov. | OK |
| 124 | 8 | Choix multiple | B | Naejangsan : pic prévu par Weatheri, 11 nov. | OK |
| 125 | 8 | Choix multiple | B | Duryunsan : pic prévu par l'Office des forêts, 11 nov. | OK |
| 126 | 8 | Choix multiple | A | Match 1 : kt a gagné 8-7 | OK |
| 127 | 8 | Choix multiple | A | Places libérées : inscriptions du 11 au 13 nov. | OK |
| 128 | 8 | Choix multiple | B | La vigilance incendie s'arrête le 15 déc. | OK |
| 129 | 8 | Choix multiple | B | Minjun va à la convocation préalable mercredi | OK |
| 130 | 8 | Choix multiple | A | Il passe le CSAT jeudi | OK |
| 131 | 8 | Choix multiple | B | Il partage le kimchi en famille dimanche | OK |
| 132 | 8 | Choix multiple | C | La semaine prochaine, il prépare l'examen d'histoire | OK |
| 133 | 8 | Faire des phrases | 저는 수요일에 예비소집에 가요. | Ordre des mots : sujet + temps + lieu + verbe | OK |
| 134 | 8 | Faire des phrases | 우리는 김치를 나눠 먹어요. | Sujet + objet + verbe | OK |
| 135 | 8 | Faire des phrases | 민준이는 한국사를 좋아해요. | 좋아하다 = aimer | OK |
| 136 | 8 | Faire des phrases | 수험생은 도서관에서 공부해요. | Pour le lieu d'une action, on met 「에서」 | OK |
| 137 | 8 | Traduire | Le 22 nov., c'est le Jour du kimchi. | Voir p. 2 | OK |
| 138 | 8 | Traduire | Samsung a gagné le titre après 12 ans. | Voir p. 4 | OK |
| 139 | 8 | Traduire | 11월 18일은 예비소집이에요. | Voir p. 5 | OK |
| 140 | 8 | Traduire | 일요일에는 가족과 김치를 나눠 먹어요. | Voir la partie C, p. 8 | OK |
| 141 | 8 | Apparier | b | 예비소집 = convocation préalable b | OK |
| 142 | 8 | Apparier | c | 김치의 날 = 22 nov. c | OK |
| 143 | 8 | Apparier | a | 발효 = le processus de fermentation a | OK |
| 144 | 8 | Apparier | d | 우승 = titre d | OK |
| 145 | 8 | Texte à trous | A | Il va à la convocation préalable mercredi | OK |
| 146 | 8 | Texte à trous | A | Le Jour du kimchi, c'est le 22 nov. | OK |
| 147 | 8 | Texte à trous | A | L'examen d'histoire, c'est le 28 nov. | OK |
| 148 | 8 | Texte à trous | A | Kimjang pour quatre : 199 456 wons | OK |
| 149 | 8 | Texte à trous | A | Les résultats sortent le 11 déc. | OK |
| 150 | 8 | Écrire | (tâche libre — texte modèle ci-dessous) | Texte modèle dans la partie H de cette page (169 caractères) | OK ✓ |
