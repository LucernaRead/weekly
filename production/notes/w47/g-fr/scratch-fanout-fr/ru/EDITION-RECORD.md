# EDITION-RECORD — 2026-W47 fr-ru (Russian reader)

- Status: DONE (run2, gates 15/15 PASS, 2026-11-11)
- Edition dir: `production/2026-w47/2026-w47-fr-ru/`
- Print PDF `La-Lucerna-VOL4-fr-ru.pdf` — 17,477,487 B, SHA-256 `96aa5eb73b02cf756ec0a4fefd1dafcd36a024c4e87d78343c84ff93f285cd86`
- Web PDF `La-Lucerna-VOL4-fr-ru-web.pdf` — 1,760,059 B, SHA-256 `f25ad674cfdc40a2e5aa3d85ab185e67e640554aa55ac7a1d646709cb62d45f8`
- `.text.md` — 50,537 B, SHA-256 `cfb2cf442b447e7da93faab9de857b723109997f5b3a6bb1cd03ffac1de73740`, 542 entries, 150 exercises
- Text layer print/web byte-equal, 107,479 B
- Freeze 8/8: [`45d7ade2`, `e805be98`, `8bc49b18`, `c9dc8270`, `b7577f84`, `69a1f37e`, `e825ca39`, `3cdf7e52`]
- Chips 134 [10, 12, 18, 15, 14, 15, 12, 38]; P8 min font 11.625pt; MCQ 45 bodies, 1,478 lines, 0 defects
- Build: `ru/build-run2.log` (rc=0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150;
  battery ends 1427.52, keys end 2045.7, Hiroshige placed at 2055.7)
- Gates: `ru/gates-run2.json` (15/15 PASS)
- Visual QA: `ru/qa/p-1.png` … `ru/qa/p-8.png` + `ru/qa/p1-band.png`, `ru/qa/p4-chiffres-v2.png`, `ru/qa/p8-e135-v2.png` — zero problems
- Counts: 131 reused / 187 new / 14 frozen; `gloss_prefix` "Пояснение — ", `note_wrap` "half"
- Build interpreter: `tools/venv/bin/python` (PIL 13.0.0)

## Run history

- Pre-build: keys diff 383px → batch 1 (45 cuts, 12 moves) 242px → batch 2 (29 cuts,
  16 moves) 141px → batch 3 (7 cuts, 4 moves) 121px ≤124. Stems matched core after
  batch 1. Precheck fixes: band_r1, agenda_note, gp1–gp8 (all 2L→1L), g6 (prefix counts).
- run1: gates 15/15 PASS first build. Visual QA found the serif-renderer lost-space
  defect class (3 spots: P4 chiffres_note ×2, P8 stem_e1 ×1; W46 ru shipped the same
  chiffres_note artifact — pre-existing limitation).
- run2: chiffres_note + stem_e1 rewritten at value level (colon instead of dash,
  Latin word dropped); span-gap analysis 0 lost spaces; gates 15/15 PASS.

## 150-key table (core key vs ru key; only Q150 differs)

diff keys: [150]
| Q | 核心键 | ru 键 | 备注 |
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
| 150 | 开放题 | Открытый вопрос | 仅此题不同 |
