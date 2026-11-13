# EDITION RECORD — 2026-W47 ko-fr (run 1; 2026-11-11)

- Slug: `2026-w47-ko-fr` (target ko, reader French). Core: `core-ko` run 10.
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-fr.json`, `gen-map-fr.py` via `mk-lang.py` + `fr-replace.json` / `fr-meta.json`); apply log `apply-fr.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-FR.pdf` — **45,468,290 bytes**, SHA-256 `ef8429557ec75f1473cd594185df8275056caf6338feeb6499872dfa314c2f7b`
- Web PDF: `Lucerna-VOL4-KO-FR-web.pdf` — **4,024,760 bytes** (< 7 MB), SHA-256 `adcaba49b643ed26f4b3b1b22461ac0f1cf1275ae9f6177f64280678e77b1245`
- Text export: `2026-w47-ko-fr.text.md` — 26,727 bytes, 332 items, SHA-256 `fabcc1c3ddafda61e2a2382548f525c5836ee3e1cc9ddda48b4b39434d0f5c43`
- `ABSTRACT.txt` — 378 bytes, SHA-256 `d34aecc9380d252bd3f669b6306e47e85bcdccbd1b0971bbf6297b1d055b5054`
- 8 SVGs in `svg/` (hashes in `fr/sha-fr-run1.txt`).

## Gates (all pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 1) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2426, P7 teaser 2510.2 | `fr/build-fr-run1.log` |
| boxtitle width | 8/8 titles ≤ 386.5px (apply round 2: P7 frame `La structure` 275.9px) | `fr/boxtitle-fr.log` |
| U+2019 scan (8 SVGs) | 0 | measured inline |
| occlusion audit | **0 flags** (selftest OK, 6 classes fired, clean controls silent) | `fr/occlusion-fr.json` / `fr/occlusion-fr.log` |
| p8.py extract | 150/150 noted | `fr/p8-extract-fr.log`, `fr/p8-fr.json` |
| p8.py compare vs core | CLEAN, keydiff `[137, 138]` (E-group re-aimed, W46 precedent) | `fr/p8-compare-fr.log` |
| freeze diff vs core | added CJK 7, all U+3000 (footer) | `fr/freeze-diff-fr.log` |
| freeze baseline (/usr/bin/python3) | **8/8 byte-identical** | `fr/freeze-fr.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `fr/check-fr.log` |
| check_gloss (scratch copy) | gloss fails 0 | `fr/check-fr.log` |
| print/web text layers | byte-identical, 52,232 bytes each | `fr/textlayer-diff-fr.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `fr/keycheck-fr.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `fr/style11-fr.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `fr/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 0 Chinese characters in `<text>` | measured inline |

## Fixes in this edition

1. **Box title wider than the 386.5px inner width** (found by `boxtitle-ko.py` after apply round 1, before any build): P7 frame title `이번 주의 틀　Structure de la semaine` 406.8px. Shortened to `La structure` (275.9px); re-applied, boxtitle 8/8. Other titles kept (P1 `En chiffres` 326.9px, P2 hanneung `Inscription` 256.9px, P2 shopping `Liste de courses` 360.4px, P3 `À savoir` 323.7px, P5 `Chiffres jeunesse` 379.1px, P7 clinic `Clinique des fautes` 327.0px, P7 letters `Courrier des lecteurs` 369.5px).
2. **Disk-quota incident (process, not content):** first `freeze.py baseline` died rc=120 with `Disk quota exceeded` (EDQUOT; df showed 45G free). Stopped at once, deleted only reproducible freeze rebuild dirs in my own note dir (`fr/freeze-fr`, `en/freeze-en`, `de/freeze-de`, 43M; gate logs kept), retried once: freeze baseline rc=0, 8/8. `p8.py compare` first call also failed on a missing `--total` argument; re-ran with `--total 150` → CLEAN.

## Adjudicated (not defects — inherited from core or by design)

- P8 match-item notes end with the option letter repeated (`25. d — … 199 456 wons d`): the letter is in the SOURCE note literal itself, core's own convention (`김장비용=四口之家199,456韩元 d` in core-ko); the fr map translated the note text and kept the letter.
- #43/#123/#124 note "prévisions Weatheri": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(tâche libre — texte modèle ci-dessous)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (fr): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure replaces `lcn`; `lko`/`lcn2` lines + render lines removed, W46 ko-fr precedent).
- text.md 332 items vs core 333: `textmd.py`'s `is_prose` drops the bare 3-letter Latin word "Tout" (P1 contents 8면 row level); the SVG/PDF render "Tout" correctly (visible on the P1 render). Export quirk, not a content gap.
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- P8 answer-note person names: only personal name is 민준 (Minjun, section C protagonist + P8 #129 note) — standard Revised Romanization, consistent within the edition; no sumo-style romaji issue (ja-family class does not apply here). Team/company names (Samsung, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings.

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
