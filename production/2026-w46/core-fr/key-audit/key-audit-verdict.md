# Key Audit Verdict — Lucerna Weekly W46, FR family (VOL.4, 9–15 Nov 2026)

- **Auditor role:** focused key auditor. Read-only: fixed nothing, re-rendered nothing, edited no edition file, touched no git/index/Discord state.
- **Scope:** frozen FR core (`files/weekly-report-w46-fr-core/`) + all 11 FR-target editions: fr-de, fr-en, fr-es, fr-it, fr-ja, fr-ko, fr-nl, fr-pt, fr-ru, fr-zh-cn, fr-zh-tw.
- **Date of audit:** 2026-11-02 (EST). Artifacts audited are the post-fix final artifacts (Round 2, 2026-11-03 UTC gate logs / 2026-11-03 cards).
- **Question closed:** whether every answer-key letter 1–150 is semantically correct in the core and correctly rendered in every edition — the gap Round 2 left open (see §0).

## §0. What Round 2 did and did not establish (gap statement)

Round 2 (`hidden_files/w46/fr-proofread-gates-round2/proofreader-verdict-round2.md`, PASS all 11) verified: fix sites D1/D2/D3 in the final artifacts; freeze diffs; `p8.py compare` CLEAN (noted-set equality); occlusion 0 flags; counts 150/150; weekday/date consistency; P1/P8 cards visually clean. It did **not** explicitly establish full key-letter correctness: it never verified matching blocks option-by-option, never compared bare (un-noted) P8 keys letter-by-letter across editions, and its `p8.py compare` keydiff only fires when *both* core and edition carry a printed note for the number. 29 keys print bare (no note) — including the D1 fix site 35–37 and most matching letters — so a transposed letter there would pass `p8.py compare` and sampled checks while core-vs-edition sets still agreed. That is exactly the ZH-CN defect class this audit was commissioned to exclude. This audit closes it by (a) semantically verifying all 150 core keys against stems/articles/options, and (b) comparing all 150 printed P8 keys (noted *and* bare) across all 12 directories.

## §1. Sources and method

Core build sources (read-only): `hidden_files/weekly-report-w46-fr-build/content12.py`, `content34.py`, `content56.py`, `content7.py`, `content8.py`, `bslib4.py` (registry + `match_set` renderer), `expl.py` (core/zh-cn notes). Printed artifacts: each edition's `svg/*.svg` + `.text.md` export.

1. **Shared-source check.** `content12/34/56/7/8.py`, `bslib4.py`, `svglib.py` are byte-identical across all 12 build directories except the `OUT` path line (verified by diff after stripping `^OUT =`). Stems, option lists, matching-rights order and registry keys are therefore literally one shared source; per-edition variation lives only in `expl.py` (native notes/glosses/stems 135–139, 150 label). The semantic verification of the core (§3) therefore applies to every edition's French layer; §4 then verifies the printed rendering and the native layer separately.
2. **Semantic verification, core (§3).** Every key 1–150 checked against its stem, the issue's articles/calendar, its option list, French grammar/agreement, and — for numbers/dates — recomputation from the issue's own data. Weekdays independently re-verified with `date` (America/Toronto): 9 Nov 2026 = Monday, 11 Nov = Wednesday, 14 Nov = Saturday, 15 Nov = Sunday, 8 Nov = Sunday, 12 Nov = Thursday, 19 Nov = Thursday, 3 Nov = Tuesday.
3. **Printed-key comparison, all editions (§4).** `tools/p8.py extract --total 150` run on all 12 P8 SVGs (keys for all 150 numbers, noted and bare) and compared string-by-string; `tools/p8.py compare` re-run as supplement; `.text.md` answers sections (last-occurrence parse, 150/150 in all 12) compared head-by-head against the core; SVG `<text>` continuous-order check for all 5 matching blocks' rights in all 12 directories; every `expl.py` matching-note letter (`m_*`) and every fact-bearing gloss (`n_g1`, `n_cloze*`, `n_chart*`, `n_56e`, `n_samedi14`, `n_14h`, `n_comp4a/6a`, `n_cl4`, `n_neg3`, `n_e1/e5`, `stem_e1`) read in all 11 edition `expl.py` files and checked against the keys.
4. **Regression checks (§5).** Item 37 and item 135 re-verified in the final SVGs of all 12 directories with wrap-aware joined-text search.

## §2. Matching-block verification (option-by-option)

The renderer (`bslib4.py: match_set`) prints the left words numbered and the right definitions lettered a/b/c/… in the order given in source, and registers the keys in that same order. A transposition would therefore appear as a left word whose semantically correct definition sits at a different letter. Each block below quotes the stem as printed (words in order; definitions in printed letter order a–e), the semantically correct letter for each word, and the printed key. **All five blocks are correct in the core, and the rights order + letter prefixes were verified identical in all 12 SVGs (§4).**

### Block D — P2, items 22–25 (stem: "D · LES MOTS", match the words to the definitions)

| # | Word (left) | a. un bouquet de fleurs déposé en hommage | b. le feu qui brûle sans s'éteindre | c. le lieu où l'on regarde des œuvres | d. la première soirée d'une exposition | Correct | Printed |
|---|---|---|---|---|---|---|---|
| 22 | une gerbe | **a — a wreath/bouquet laid in tribute is a gerbe** | — | — | — | a | a |
| 23 | une flamme | — | **b — a flame is fire that burns without going out** | — | — | b | b |
| 24 | un musée | — | — | **c — a museum is the place where one looks at works** | — | c | c |
| 25 | un vernissage | — | — | — | **d — a vernissage is the first evening of an exhibition** | d | d |

Printed stem (core `.text.md`): "22–25 une gerbe — un bouquet de fleurs déposé en hommage / une flamme — le feu qui brûle sans s'éteindre / un musée — le lieu où l'on regarde des œuvres / un vernissage — la première soirée d'une exposition". No word fits any other definition (a gerbe is not a fire, a flamme is not a place, etc.). **22 a, 23 b, 24 c, 25 d — CORRECT.**

### Block P4 — items 49–52 (stem: match tennis/football words to definitions)

| # | Word | a. ne pas jouer, à cause d'une blessure | b. la liste des matches d'un tournoi | c. quatre joueurs qui se rencontrent | d. la pause entre deux séries de matches | Correct | Printed |
|---|---|---|---|---|---|---|---|
| 49 | un forfait | **a — a forfait/withdrawal is not playing because of injury** (Sinner, knee injury) | — | — | — | a | a |
| 50 | un tableau | — | **b — the draw is the list of a tournament's matches** (56 joueurs au tableau) | — | — | b | b |
| 51 | un groupe | — | — | **c — a group is four players who meet each other** (deux groupes de quatre) | — | c | c |
| 52 | la trêve | — | — | — | **d — the (international) break is the pause between series of matches** | d | d |

**49 a, 50 b, 51 c, 52 d — CORRECT.**

### Block P5 — items 73–76 (stem: match photography words to definitions)

| # | Word | a. une photographie imprimée sur papier | b. le lieu où l'on expose des œuvres | c. la première soirée d'une exposition | d. le petit texte sous une image | Correct | Printed |
|---|---|---|---|---|---|---|---|
| 73 | un tirage | **a — a print is a photograph printed on paper** | — | — | — | a | a |
| 74 | une galerie | — | **b — a gallery is the place where works are exhibited** | — | — | b | b |
| 75 | un vernissage | — | — | **c — a vernissage is the first evening of an exhibition** (same definition as block D, letter c here because the rights order differs) | — | c | c |
| 76 | une légende | — | — | — | **d — a caption is the small text under an image** | d | d |

**73 a, 74 b, 75 c, 76 d — CORRECT.** Note: `vernissage` is d in block D and c here; each is correct within its own block's rights order — no cross-block confusion, and the `expl.py` glosses keep the two blocks distinct (`m_vernissage` = d, `m_vernissage2` = c in every edition).

### Block P6 — items 85–88 (stem: "LES MOTS · 词汇")

| # | Word | a. un élu du Sénat | b. dire non à un texte | c. la décision ensemble | d. le groupe qui prépare | Correct | Printed |
|---|---|---|---|---|---|---|---|
| 85 | un sénateur | **a — a senator is an elected member of the Senate** | — | — | — | a | a |
| 86 | rejeter | — | **b — to reject is to say no to a text** (115–1 rejection) | — | — | b | b |
| 87 | un vote | — | — | **c — a vote is the decision taken together** (decision procedure; gloss is loose but is the only decision-word among the four) | — | c | c |
| 88 | une commission | — | — | — | **d — a committee is the group that prepares (the report)** (commission des affaires sociales, rapport le 4 nov.) | d | d |

**85 a, 86 b, 87 c, 88 d — CORRECT.** The definition of 87 ("la décision ensemble") is the block's weakest wording, but it cannot belong to any other word, and c is the only remaining letter.

### Block P8 F — items 140–144 (stem: "F · LES MOTS · 词汇配对")

| # | Word | a. un élu du Sénat | b. un bouquet déposé en hommage | c. une photographie imprimée | d. une grande fête populaire | e. la petite fleur bleue du 11 novembre | Correct | Printed |
|---|---|---|---|---|---|---|---|---|
| 140 | un sénateur | **a** | — | — | — | — | a | a |
| 141 | une gerbe | — | **b — a gerbe is a bouquet laid in tribute** | — | — | — | b | b |
| 142 | un tirage | — | — | **c — a tirage is a printed photograph** | — | — | c | c |
| 143 | une foire | — | — | — | **d — a fair is a big popular festival** (Foire de Dieppe) | — | d | d |
| 144 | un bleuet | — | — | — | — | **e — a bleuet is the little blue flower of 11 November** | e | e |

**140 a, 141 b, 142 c, 143 d, 144 e — CORRECT.** No transposition in any of the five blocks: 21 matching keys, all correct. The `m_*` gloss letters in all 11 editions' `expl.py` files agree with these letters without exception (§4).

## §3. Full 1–150 core verification (stem + options + printed key + verdict)

"Printed key" is the P8 key as extracted wrap-aware from the core P8 SVG and confirmed in the core `.text.md` answers section (identical). "Reason" is the semantic/grammatical/article evidence. **Correct: 150/150. Wrong: 0.**

### P1 (1–10)

| # | Stem (+ options) | Printed key | Verdict / reason |
|---|---|---|---|
| 1 | "Lundi 9 novembre, le ___ ouvre la discussion sur le budget." | Sénat | CORRECT — article: "le Sénat ouvre la discussion". |
| 2 | "L'Armistice, c'est ___ 11 novembre." | mercredi | CORRECT — 11 Nov 2026 is a Wednesday (date-verified). |
| 3 | "À Dieppe, on fête les ___ et la coquille Saint-Jacques." | harengs | CORRECT — Foire aux harengs. |
| 4 | "Le 23 octobre, les recettes ont été rejetées par ___ voix contre 1." | 115 | CORRECT — recomputed from issue data: "115 voix contre 1" (P1 article, P6 calendar). |
| 5 | "Sous l'Arc de Triomphe, on ravive la ___ du Soldat inconnu." | flamme | CORRECT — "ravive la flamme". |
| 6 | "La foire aux harengs a lieu à ___." | Dieppe | CORRECT — fair is in Dieppe, not Paris. |
| 7 | "La discussion au Sénat commence... A. lundi 9 · B. mercredi 11 · C. samedi 14" | A | CORRECT — opens Monday 9 Nov. |
| 8 | "L'Armistice, c'est... A. lundi 9 · B. mercredi 11 · C. dimanche 15" | B | CORRECT — Wednesday 11 Nov. |
| 9 | "La foire de Dieppe a lieu... A. à Paris · B. à Bordeaux · C. à Dieppe" | C | CORRECT — Dieppe. |
| 10 | "France – Turquie, dimanche 15, c'est à... A. Bordeaux · B. Milan · C. Turin" | A | CORRECT — Bordeaux hosts France–Turkey; Milan hosts Italy–France (12th); Turin hosts the Finals. |

### P2 (11–25)

| # | Stem (+ options) | Printed key | Verdict / reason |
|---|---|---|---|
| 11 | "L'Armistice a lieu ___ 11 novembre." | mercredi | CORRECT — Wednesday 11 Nov. |
| 12 | "La discussion au Sénat commence ___ 9 novembre." | lundi | CORRECT — Monday 9 Nov. |
| 13 | "Paris Photo ouvre au public ___ 12 novembre." | jeudi | CORRECT — public enters Thursday 12 (vernissage Wed is invitation-only). |
| 14 | "France – Turquie, c'est ___ 15 novembre." | dimanche | CORRECT — Sunday 15 Nov. |
| 15 | "Lundi, le Sénat (ouvrir) la discussion. → ___" (futur proche) | Le Sénat va ouvrir la discussion lundi. | CORRECT — aller (3sg va) + infinitive. |
| 16 | "Jeudi, nous (visiter) Paris Photo. → ___" | Nous allons visiter Paris Photo jeudi. | CORRECT — nous → allons. |
| 17 | "Tu (raconter) ton mercredi férié. → ___" | Tu vas raconter ton mercredi férié. | CORRECT — tu → vas. |
| 18 | "À Dieppe, vous (goûter) des harengs. → ___" | Vous allez goûter des harengs à Dieppe. | CORRECT — vous → allez. |
| 19 | "Le 11 novembre, les cérémonies commencent à... A. 9 h · B. 10 h · C. 11 h" | C | CORRECT — ceremonies at 11 heures (11 Nov, 11 h). |
| 20 | "Le bleuet est le symbole... A. de Dieppe · B. du 11 novembre · C. du Sénat" | B | CORRECT — bleuet is the symbol of 11 November. |
| 21 | "Paris Photo ouvre au public... A. jeudi 12 · B. mercredi 11 · C. dimanche 15" | A | CORRECT — Thursday 12. |
| 22–25 | Matching block D | a / b / c / d | CORRECT — see §2 Block D. |

### P3 (26–43)

| # | Stem (+ options) | Printed key | Verdict / reason |
|---|---|---|---|
| 26 | "L'Armistice a été signé le 11 novembre 1918." [Vrai/Faux] | Vrai | CORRECT — Armistice signed 11 Nov 1918, 11 h (article). |
| 27 | "La flamme du Soldat inconnu brûle depuis 1923." [Vrai/Faux] | Vrai | CORRECT — flame burns since 1923 (article). |
| 28 | "Le 11 novembre est un jour de travail comme les autres." [Vrai/Faux] | Faux | CORRECT — it is a jour férié. |
| 29 | "La foire de Dieppe a lieu le 11 novembre." [Vrai/Faux] | Faux | CORRECT — fair is 14–15 Nov. |
| 30 | "Le hareng est le « poisson roi » de la foire." [Vrai/Faux] | Vrai | CORRECT — "poisson roi" (article). |
| 31 | "On dépose une ___ devant le monument aux morts." | gerbe | CORRECT — "On dépose une gerbe" (article). |
| 32 | "Le ___ est la fleur du 11 novembre." | bleuet | CORRECT — bleuet, blue flower of the day. |
| 33 | "La foire a lieu sur les ___ de Dieppe." | quais | CORRECT — "sur les quais" (article). |
| 34 | "Devant les restaurants, les ___ fument." | grills | CORRECT — "les grills fument" (article). |
| 35 | "(jamais) La flamme s'éteint. → ___" | La flamme ne s'éteint jamais. | CORRECT — ne...jamais, ne before verb, jamais after; factually the flame never goes out. |
| 36 | "(pas) On oublie les morts pour la France. → ___" | On n'oublie pas les morts pour la France. | CORRECT — ne...pas with elision n'oublie. |
| 37 | "(pas) La foire est à Paris. → ___" | La foire n'est pas à Paris. | CORRECT — **regression site (§5)**: ne...pas; factually the fair is in Dieppe. No `ne...plus` remains. |
| 38 | "C'est la ___ édition de la foire de Dieppe." | 56e | CORRECT — 56e Foire (article). |
| 39 | "L'inauguration a lieu ___ 14 novembre, à 10 heures." | samedi | CORRECT — 14 Nov 2026 is a Saturday; inauguration Saturday 10 h. |
| 40 | "L'inauguration part du ___." | pont Colbert | CORRECT — départ du pont Colbert (article). |
| 41 | "La coquille Saint-Jacques est... A. un poisson · B. l'emblème du port · C. un bateau" | B | CORRECT — "emblème du port"; the hareng (not the coquille) is the "poisson roi". |
| 42 | "La visite « Les quatre ports » part à ___." | 14 heures | CORRECT — guided tour at 14 h (article). |
| 43 | "L'entrée de la foire est ___." | libre | CORRECT — "L'entrée est libre" (free entry). |

### P4 (44–61)

| # | Stem (+ options) | Printed key | Verdict / reason |
|---|---|---|---|
| 44 | "Les finales du Masters ont eu lieu... A. samedi 7 · B. dimanche 8 · C. lundi 9" | B | CORRECT — finals Sunday 8 Nov. |
| 45 | "Sinner n'a pas joué parce qu'il est... A. blessé au genou · B. en vacances · C. à Turin" | A | CORRECT — knee injury, season ended 6 Oct. |
| 46 | "Les Masters de Turin commencent... A. le 9 nov. · B. le 12 nov. · C. le 15 nov." | C | CORRECT — Turin starts Sunday 15 Nov. |
| 47 | "France – Turquie, c'est... A. à Milan · B. à Bordeaux · C. à Nanterre" | B | CORRECT — Bordeaux (Milan = Italy–France; Nanterre = Masters arena). |
| 48 | "La 11e journée de Ligue 1, c'est... A. les 21–22 nov. · B. le 15 nov. · C. le 9 nov." | A | CORRECT — 21–22 Nov after the international break. |
| 49–52 | Matching block P4 | a / b / c / d | CORRECT — see §2. |
| 53 | "En salle, la balle va ___ (vite) qu'en plein air." | plus vite | CORRECT — comparative of superiority; indoor ball travels faster (no wind, hard indoor court) — the conventional real-world reading; no article contradiction. See observation O1. |
| 54 | "Turin est ___ (grand) qu'un petit tournoi." | plus grand | CORRECT — the Turin Finals are bigger than a small tournament; masculine agreement (grand). |
| 55 | "La trêve est ___ (longue) que la saison. (moins)" | moins longue | CORRECT — hint (moins) + semantics: the break is shorter than the season; feminine agreement (longue / trêve). |
| 56 | "Sinner a déclaré ___ : blessé, il n'a pas joué." | forfait | CORRECT — "a déclaré forfait" (article). |
| 57 | "La ___ du simple a eu lieu dimanche 8." | finale | CORRECT — singles final Sunday 8. |
| 58 | "À Turin, huit joueurs, en deux ___ de quatre." | groupes | CORRECT — deux groupes de quatre (article). |
| 59 | "Pas de Ligue 1 : c'est la ___ internationale." | trêve | CORRECT — trêve internationale. |
| 60 | "France – Turquie, dimanche 15, à ___." | Bordeaux | CORRECT. |
| 61 | "Italie – France, jeudi 12, à ___." | Milan | CORRECT — Milan, 12 Nov. |

### P5 (62–78)

| # | Stem (+ options) | Printed key | Verdict / reason |
|---|---|---|---|
| 62 | "Paris Photo 2026, c'est la... A. 15e édition · B. 29e édition · C. 56e édition" | B | CORRECT — 29e édition (56e is the Dieppe fair — the distractor). |
| 63 | "La photographie est née en... A. 1826 · B. 1926 · C. 2026" | A | CORRECT — born 1826; 200 years to 2026 (recomputed: 2026 − 200 = 1826). |
| 64 | "Le salon ouvre au public... A. mercredi 11 · B. mardi 10 · C. jeudi 12" | C | CORRECT — public Thursday 12. |
| 65 | "Le billet du soir coûte... A. 36 € · B. 26 € · C. 41 €" | B | CORRECT — evening/student ticket 26 € (36 weekday, 41 weekend). |
| 66 | "« Kaamelott » sort... A. le 10 mars 2027 · B. le 11 novembre · C. le 12 novembre" | A | CORRECT — postponed to 10 March 2027. |
| 67 | "Paris Photo a lieu au ___." | Grand Palais | CORRECT — Grand Palais venue. |
| 68 | "Chaque photo a une ___ à lire." | légende | CORRECT — "chaque photo a une légende à lire". |
| 69 | "Le ___ est réservé aux invités." | vernissage | CORRECT — vernissage invitation-only. |
| 70 | "« Elles × Paris Photo » met en avant les femmes ___." | photographes | CORRECT — women photographers; plural agreement. |
| 71 | "« Scrooge », c'est avec Johnny ___." | Depp | CORRECT — Johnny Depp. |
| 72 | "Les nouveautés cinéma sortent le ___ 11 novembre." | mercredi | CORRECT — Wednesday 11 Nov. |
| 73–76 | Matching block P5 | a / b / c / d | CORRECT — see §2. |
| 77 | "— Tu vas à Paris Photo quand ? — ___, le premier jour." | jeudi | CORRECT — first public day is Thursday 12 (Wednesday is the invitation-only vernissage). |
| 78 | "— Tu as pris ___ ? — Oui, pour toi et moi." | deux billets | CORRECT — two people → two tickets. |

### P6 (79–96)

| # | Stem (+ options) | Printed key | Verdict / reason |
|---|---|---|---|
| 79 | "Le 23 octobre, les recettes ont été... A. adoptées · B. rejetées · C. reportées" | B | CORRECT — rejected 115–1 on 23 Oct (calendar + article). |
| 80 | "Mardi 3 novembre, on vote... A. les dépenses · B. les recettes · C. les deux" | B | CORRECT — solemn vote on the recettes part (first part). |
| 81 | "La commission du Sénat a préparé son rapport le... A. 9 nov. · B. 4 nov. · C. 23 oct." | B | CORRECT — report Wednesday 4 Nov. |
| 82 | "La discussion générale s'ouvre le... A. 9 nov. · B. 3 nov. · C. 26 nov." | A | CORRECT — Monday 9 Nov. |
| 83 | "Le Sénat examine... A. le texte des députés · B. un texte neuf · C. le texte du gouvernement" | C | CORRECT — government text in its initial version (rejection stopped the deputies' examination). |
| 84 | "Le Parlement a cinquante jours, jusqu'au... A. 9 nov. · B. 26 nov. · C. 18 déc." | B | CORRECT — 50 days to 26 Nov (article/calendar). |
| 85–88 | Matching block P6 | a / b / c / d | CORRECT — see §2. |
| 89 | "Un débat au Sénat est ___ (long) qu'un concert." | plus long | CORRECT — a multi-day Senate debate is longer than a concert; masculine agreement. See O1. |
| 90 | "Le budget est ___ (simple) qu'un calendrier. (moins)" | moins simple | CORRECT — hint (moins); budget less simple than a calendar. |
| 91 | "Le budget de la Sécu est ___ (important) que le budget de l'État. (aussi)" | aussi important | CORRECT — hint (aussi); equality comparative, masculine agreement. |
| 92 | "Cette semaine, le Sénat ___ le budget de la Sécu." | examine | CORRECT — present 3sg; "le Sénat examine" (article). |
| 93 | "Le 23 octobre, les députés ___ les recettes du texte." | ont rejeté | CORRECT — passé composé, plural subject; object follows verb → no agreement on rejeté. |
| 94 | "Le texte ___ au Sénat." | part | CORRECT — present 3sg of partir; "Le texte part au Sénat" (article). |
| 95 | "Le calendrier ___ encore bouger." | peut | CORRECT — modal pouvoir + infinitive; "peut encore bouger". |
| 96 | "Les résultats du 3 novembre ne sont pas encore ___." | connus | CORRECT — masculine plural agreement with résultats; "ne sont pas encore connus". |

### P7 (97–108)

| # | Stem | Printed key | Verdict / reason |
|---|---|---|---|
| 97 | "Lundi, le Sénat ___ (ouvrir) la discussion." | ouvre | CORRECT — present 3sg of ouvrir; golden sentence verbatim. |
| 98 | "En 1918, les armes se sont ___ (taire)." | tues | CORRECT — se taire, passé composé with être, feminine plural (les armes) → tues. |
| 99 | "La flamme ___ (brûler) depuis 1923." | brûle | CORRECT — present with depuis (action still going on). |
| 100 | "Trois temps : débattre, se souvenir et ___." | fêter | CORRECT — third infinitive of the golden sentence's list. |
| 101 | "Le hareng est le « poisson ___ »." | roi | CORRECT — "poisson roi". |
| 102 | "Les résultats ___ (être) dans le VOL.5." | seront | CORRECT — futur simple, plural. |
| 103 | "Regarder une photo, c'est déjà ___." | lire | CORRECT — "c'est déjà lire" (golden sentence). |
| 104 | "Le texte est celui du ___." | gouvernement | CORRECT — "celui du gouvernement" (article). |
| 105 | Clinic ✗ "La flamme s'éteint jamais." (correct it) | La flamme ne s'éteint jamais. | CORRECT — adds the missing ne to ne...jamais. (Same sentence as 35; intentional reuse.) |
| 106 | Clinic ✗ "Les sénateurs examine le texte lundi." | Les sénateurs examinent le texte lundi. | CORRECT — plural subject → examinent. |
| 107 | Clinic ✗ "Il est prévu que le Sénat examines le texte." | Il est prévu que le Sénat examine le texte. | CORRECT — subjunctive present 3sg of -er verb has no -s: examine. |
| 108 | Clinic ✗ "La foire a lieu samedi 15 novembre." | La foire a lieu samedi 14 novembre. | CORRECT — fair starts Saturday 14 Nov (15 Nov is a Sunday); fixes both the date and the weekday/date mismatch. |

### P8 battery (109–150)

| # | Stem (+ options) | Printed key | Verdict / reason |
|---|---|---|---|
| 109 | Cloze: "Le (109)___ 9 novembre, il se lève tôt..." A. lundi · B. samedi · C. dimanche | A | CORRECT — 9 Nov = Monday. |
| 110 | Cloze: "...il va à (110)___ pour la cérémonie du 11 novembre." A. Paris · B. Dieppe · C. Turin | A | CORRECT — Paris is the ceremony city (national ceremony, Arc de Triomphe); Dieppe = the fair, Turin = tennis. See observation O2. |
| 111 | Cloze: "« Les (111)___ du Masters seront dans le VOL.5 »" A. résultats · B. finalistes · C. spectateurs | A | CORRECT — article's own wording: "les résultats … seront dans le VOL.5". |
| 112 | Cloze: "« À Dieppe, on a (112)___ des harengs, un régal ! »" A. acheté · B. goûté · C. vendu | B | CORRECT — tasting context ("un régal !") + issue collocation "on goûte"; goûté is the designed answer. See O2. |
| 113 | Cloze: "Paris Photo (113)___ au Grand Palais." A. tient · B. tiennent · C. se tient | C | CORRECT — se tenir = to take place (event); singular subject excludes tiennent; tient alone is transitive/incomplete here. |
| 114 | Cloze: "Théo a (114)___ les photos." A. aimé · B. aimée · C. aimer | A | CORRECT — avoir + past participle, object after verb → no agreement: aimé (not aimée, not infinitive aimer). Classic trap, key correct. |
| 115 | Cloze: "Les Bleus (115)___ dimanche" A. joue · B. jouent · C. jouer | B | CORRECT — plural subject Les Bleus → jouent. |
| 116 | Cloze: "...et il l'(116)___ dans son cahier." A. écrit · B. écrivent · C. écris | A | CORRECT — 3sg il → écrit (écrivent plural; écris 1st/2nd person). |
| 117 | "La discussion au Sénat commence... A. dimanche 8 · B. lundi 9 · C. mercredi 11" | B | CORRECT — Monday 9. |
| 118 | "Le 11 novembre, on dépose... A. une gerbe · B. un billet · C. un ballon" | A | CORRECT — une gerbe. |
| 119 | "Le Soldat inconnu repose... A. à Dieppe · B. sous l'Arc de Triomphe · C. à Turin" | B | CORRECT — under the Arc de Triomphe since 1920. |
| 120 | "Si j'étais libre dimanche, j'___ à Dieppe. A. irai · B. irais · C. vais" | B | CORRECT — si + imparfait → conditionnel: irais (irai = futur, vais = present, both wrong after si + imparfait). |
| 121 | "À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant" | A | CORRECT — 3sg present semble (infinitive/participle wrong). |
| 122 | "Dimanche, la France ___ la Turquie à Bordeaux. A. reçoivent · B. reçoit · C. recevoir" | B | CORRECT — la France (singular collective) → reçoit. |
| 123 | "Paris Photo, c'est... A. un salon de photographie · B. un match · C. une foire aux harengs" | A | CORRECT — photography salon. |
| 124 | "Le beaujolais nouveau arrive... A. le 11 nov. · B. le 15 nov. · C. le 19 nov." | C | CORRECT — 19 Nov (P7 teaser). |
| 125 | Reading (Martin family): "L'inauguration a lieu à... A. 9 h · B. 11 h · C. 10 h" | C | CORRECT — passage: "à 10 heures". |
| 126 | "La famille goûte... A. des harengs grillés · B. des bonbons · C. des gâteaux" | A | CORRECT — passage: "ils goûtent des harengs grillés". |
| 127 | "Dimanche, la famille... A. reste à Dieppe · B. rentre et regarde les Bleus · C. va à Turin" | B | CORRECT — passage: "ils rentrent à Paris et ils regardent les Bleus". |
| 128 | "Dimanche soir, les enfants dorment tôt parce que... A. lundi, c'est l'école · B. il pleut · C. ils sont malades" | A | CORRECT — passage states the reason: "lundi, c'est l'école". |
| 129 | "Lundi, les enfants... A. retournent à l'école · B. restent à Dieppe · C. vont au Sénat" | A | CORRECT — Monday = school; return to school. |
| 130 | "Futur proche : « Le Sénat ouvre la discussion lundi. » → ___" | Le Sénat va ouvrir la discussion lundi. | CORRECT — aller + infinitive (same sentence as 15). |
| 131 | "Hypothèse : « Si tu (venir) samedi, tu verrais la foire. »" | Si tu venais samedi, tu verrais la foire. | CORRECT — si + imparfait (venais) + conditionnel (verrais). |
| 132 | "Passé composé : « Il (goûter) les harengs à Dieppe. »" | Il a goûté les harengs à Dieppe. | CORRECT — avoir + past participle. |
| 133 | "Opinion : « ___ moi, la semaine est bien remplie. »" | Selon moi, la semaine est bien remplie. | CORRECT — "Selon moi" (in my opinion); single-word slot before "moi" (cf. P6 opinion openers). |
| 134 | "Subjonctif : « Il est prévu que le Sénat (examiner) le texte lundi. » → ___" | Il est prévu que le Sénat examine le texte lundi. | CORRECT — subjunctive examine, no -s (same as 107). |
| 135 | Translation (reader-language stem → French; core stem: 读一份日程，本身就是在了解法国。) | Lire un programme, c'est déjà comprendre la France. | CORRECT — **regression site (§5)**: "reading a programme is itself understanding France"; déjà = emphatic "already" (stem omission adjudicated non-blocking in Round 2, R1; the KEY is faithful and contains déjà). |
| 136 | Translation (core stem: 他跑得比他哥哥更快。= he runs faster than his elder brother) | Il court plus vite que son frère. | CORRECT — comparative plus vite; frère covers "brother" (French has no elder-brother noun without aîné; standard translation). |
| 137 | Translation (core stem: 学生们自 11 月 9 日起就在放假。= pupils have been on holiday since 9 Nov) | Les élèves sont en vacances depuis le 9 novembre. | CORRECT — present + depuis = duration since a date. |
| 138 | Translation (core stem: 今晚，我们要准备行装。= tonight we are going to prepare our luggage) | Ce soir, nous allons préparer nos affaires. | CORRECT — futur proche (allons préparer); affaires = belongings/luggage. |
| 139 | Translation (core stem: 人们尚不知道结果。= people do not yet know the results) | On ne connaît pas encore les résultats. | CORRECT — ne...pas encore = not yet; generic on = people. |
| 140–144 | Matching block P8 F | a / b / c / d / e | CORRECT — see §2. |
| 145 | Dialogue: "Pour (145)___, le 14 novembre : je veux des harengs..." | samedi | CORRECT — 14 Nov = Saturday; "Pour samedi, le 14 novembre". |
| 146 | Dialogue: "je veux des (146)___ pour ma famille." | harengs (des harengs) | CORRECT — at the herring fair, wants (some) herrings; parenthetical confirms "des" is retained before the blank. |
| 147 | Dialogue: "Vous voulez les (147)___ au grill ?" | griller | CORRECT — vouloir + infinitive: "les griller" (grill them); no other form fits after vouloir. |
| 148 | Dialogue: "Oui, donnez-moi votre (148)___." | recette | CORRECT — "votre recette" (your recipe, for the grilled herrings) — the only cooking noun fitting the dialogue. |
| 149 | Dialogue: "Voilà. Bon (149)___ !" | week-end | CORRECT — "Bon week-end !" standard farewell; fair weekend. |
| 150 | Writing: "Écrivez un petit texte (80 à 100 mots) : « Mon mercredi 11 novembre »." | Open question — points in the writing box; model text in the P8 writing box (marked on the points) | CORRECT as an open item — no letter key exists to transpose. Present in all 12 directories (native-language label in editions). Model text present on P8. |

**Core result: 150 correct, 0 wrong.** No transposed letter, no wrong word, no wrong agreement, no wrong date/number was found in the frozen core.

## §4. Per-edition P8 key agreement (all 150, noted + bare) + native-gloss check

### 4.1 Printed keys: core vs each edition (SVG, wrap-aware extraction)

`tools/p8.py extract --total 150` was run on the core P8 SVG and on all 11 edition P8 SVGs (JSONs in this audit directory: `p8-extract-core.json`, `p8-extract-<native>.json`). Keys were compared string-by-string for all 150 numbers, including the 29 bare keys that `p8.py compare` cannot flag (bare numbers: 1, 2, 11, 16, 18, 23, 24, 25, 27, 29, 35, 36, 37, 39, 48, 49, 50, 51, 52, 63, 73, 74, 75, 76, 85, 86, 88, 98, 99).

| Edition | Noted set (121) identical to core? | Keys 1–149 identical to core? | Key 150 | Agreement |
|---|---|---|---|---|
| 2026-w46-fr-de | yes | yes, all 149 | "Offene Aufgabe" (native label for the same open item) | **AGREE** |
| 2026-w46-fr-en | yes | yes, all 149 | "Open question" | **AGREE** |
| 2026-w46-fr-es | yes | yes, all 149 | "Pregunta abierta" | **AGREE** |
| 2026-w46-fr-it | yes | yes, all 149 | "Domanda aperta" | **AGREE** |
| 2026-w46-fr-ja | yes | yes, all 149 | "自由作文" | **AGREE** |
| 2026-w46-fr-ko | yes | yes, all 149 | "자유 작문" | **AGREE** |
| 2026-w46-fr-nl | yes | yes, all 149 | "Open vraag" | **AGREE** |
| 2026-w46-fr-pt | yes | yes, all 149 | "Pergunta aberta" | **AGREE** |
| 2026-w46-fr-ru | yes | yes, all 149 | "Открытый вопрос" | **AGREE** |
| 2026-w46-fr-zh-cn | yes | yes, all 149 | identical to core | **AGREE (exact)** |
| 2026-w46-fr-zh-tw | yes | yes, all 149 | "開放題——評分點在方框內；範文在第8版方框內" | **AGREE** |

The only difference anywhere in the 1,650 edition key slots (11 × 150) is the native-language wording of the open-question label at #150, which carries no letter and no French answer. **No edition transposes, alters, or drops any key letter or key word.** In particular the bare keys — matching letters 23/24/25, 49–52, 73–76, 85/86/88 and negation keys 35–37 — print identically (bare, correct) in every edition.

### 4.2 `p8.py compare` supplement (set-equality; known blind spot recorded)

Re-run independently (`p8-compare-all.log`, `p8-compare-<native>.json`): CLEAN for all 11, 121 noted in core and edition, missing = [], extra = 0, uncertain = []. Keydiff = [150] for all editions except fr-zh-cn ([ ]). The [150] entry is the native-language #150 label only. (Round 2 measured keydiff = [145] under a total-145 run; the #145 entry is the native date gloss beside the identical key word `samedi` — core "11月14日星期六" vs e.g. German "Samstag, 14. November" — also note-only, not a key-word difference. Both readings agree: no key-word diff exists. The [145]/[150] discrepancy is a run-parameter/segment-joining difference in what counts as the "printed key" string, not a difference in the artifacts. This audit's `extract` comparison in §4.1 is the letter-level check and supersedes both for key correctness.)

Blind spot, stated plainly: `compare` only flags a keydiff when *both* sides carry a printed note, so it is blind to the 29 bare keys. The §4.1 extraction comparison closes that blind spot for this family.

### 4.3 `.text.md` cross-check

Each edition's `.text.md` answers section was parsed (last-occurrence parse, 150/150 in all 12). Against the core, the only head differences are the native-language translation stems at 135–139 (which are the *stems*, re-aimed at each reader language; the French *keys* in the answers section are identical in all editions — verified in the same parse) and the #150 native label. All other 144 heads are identical. SVG and `.text.md` renderings therefore agree on every key.

### 4.4 Matching rights order in the printed SVGs

For all 5 matching blocks in all 12 directories, the right-hand definitions occur in the SVG `<text>` stream in the core order (continuous-text search, wrap-tolerant), with letter prefixes a–e in order (spot-shown for P2/P8 in core, ja, ru; order verified for all). No edition reorders, drops, or re-letters a definition.

### 4.5 Native-language key glosses (expl.py) — no contradiction with any letter

- **Matching gloss letters (`m_*`, 21 per edition):** identical letters in all 11 editions and the core — block D a/b/c/d, P4 a/b/c/d, P5 a/b/c/d, P6 a/b/c/d, P8 a/b/c/d/e — and each gloss word is the correct native translation of its French word (e.g. en gerbe = wreath · a; de tableau = Turnierbaum · b; ja tirage = プリント · a; ru bleuet = василёк · e). No gloss letter contradicts any printed key.
- **Fact-bearing glosses:** `n_g1` (Saturday 14 Nov), `n_cloze1` (9 Nov = Monday), `n_cloze2` (ceremony in Paris), `n_samedi14`, `n_14h`, `n_56e`, `n_chart1–6` (115–1, Tue 3rd recettes, report 4th, debate Mon 9th, government text, 50 days to 26th), `n_comp4a` (indoor ball faster), `n_comp6a` (Senate debate longer), `n_cl4` (fair 14th not 15th), `n_neg3` (ne...pas), `n_e1`/`n_e5` — read in all 11 `expl.py` files: all state the same facts as the keys, in the reader's language. No contradiction found.
- **Translation stems 135–139 (`stem_e1`–`stem_e5`):** meanings spot-verified in all editions from the `.text.md` battery text; each expresses the same proposition as the French key (135: reading a programme = understanding/knowing France, in the Round-2-verified forms; 136: runs faster than his brother; 137: on holiday since 9 Nov; 138: tonight pack/prepare bags; 139: results not yet known). The six D2 stems and five accepted stems are exactly as recorded in Round 2 §D2. No stem contradicts its key.

## §5. Regression checks (Round 1/2 fix sites, keys only)

- **Item 37 (ne...pas).** P3 stem `(pas) La foire est à Paris. → ___` present in all 12 P3 SVGs (wrap-aware joined-text search, 1 occurrence each). P8 key `La foire n'est pas à Paris.` present in all 12 P8 SVGs (joined-text + extract keys, bare key 37 identical in all 12). Strings `n'est plus`, `(plus)`, `ne...plus`: 0 occurrences in all 12 P3+P8 SVGs. **PASS — no regression.**
- **Item 135 (déjà).** P8 key `Lire un programme, c'est déjà comprendre la France.` present in all 12 P8 SVGs (joined-text + extract keys, identical in all 12). **PASS — no regression.** (The stems' omission of déjà is Round 2 residual R1, already adjudicated non-blocking; it is a stem matter, not a key defect, and is not re-opened here.)

## §6. Observations (not defects; no action required for keys)

- **O1 — Unguided comparatives 53 and 89.** Items 53 ("plus vite") and 89 ("plus long") carry no plus/moins/aussi hint, unlike 55/90/91. Either direction would be grammatical; the printed keys are the conventional real-world readings (indoor ball faster; Senate debate longer than a concert) and contradict nothing in the issue. They are correct as designed answers, not transpositions. Recorded only so a future auditor does not mistake "no hint" for "ambiguous key".
- **O2 — Designed-answer cloze items 110 and 112.** Item 110 (Paris) and 112 (goûté) are fixed by elimination + issue framing + collocation ("un régal !") rather than by a unique entailment in the cloze passage alone: Paris is the only ceremony city among the options (Dieppe = fair, Turin = tennis), and goûté is the only tasting verb fitting "un régal". Both keys are correct and are the only defensible answers among the options. No change warranted.
- **O3 — Duplicate keys 15/130 and 35/105.** The same correct sentence serves as the key twice (futur proche drill + P8 sentence item; negation drill + clinic). This is reuse, not error; both printings are correct and identical in all editions.
- **O4 — Item 87's definition wording** ("la décision ensemble") is loose French for "vote", but it is the only decision-word in its block and the letter c is unambiguous. Not a key defect.

## §7. Audit evidence (in this directory)

- `key-audit-verdict.md` (this file).
- `p8-extract-core.json`, `p8-extract-<native>.json` (12×, `p8.py extract --total 150`).
- `p8-compare-all.log`, `p8-compare-<native>.json` (11×, `p8.py compare` supplement).
- `textmd-svg-crosscheck.log`, `textmd-svg-crosscheck2.log` (`.text.md` last-occurrence parse + SVG rights-order check; the first log's "FAIL" lines were a join-separator artifact in the check script itself — the corrected second run shows all blocks OK; both logs retained for transparency).

Nothing in `~/workspace/weekly-git` was touched; no file outside this audit directory was written.

## Final line

KEY AUDIT PASS (all 150 keys correct in core + all 11 editions; Round 2 PASS stands)
