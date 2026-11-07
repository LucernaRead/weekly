# Key-Letter Audit — Verdict: W46 IT family (2026-11-09 – 2026-11-15)

- **Auditor:** focused key auditor (read-only; nothing edited, re-rendered, pushed, inserted, or posted; `~/workspace/weekly-git` untouched; `index.json` untouched; no subagents).
- **Date:** Mon 2026-11-02 (evening EST), on the final shipped artifacts (same SVGs Round 2 passed).
- **Scope:** all 11 IT-target editions — `2026-w46-it-zh-cn` (frozen core), `-de`, `-en`, `-es`, `-fr`, `-ja`, `-ko`, `-nl`, `-pt`, `-ru`, `-zh-tw` — plus the frozen IT core build sources.
- **Task:** verify EVERY answer-key letter/answer 1–150 semantically against stems, articles, options, and fixtures, closing the gap left by set-equality gating.

## 0. What Round 2 did and did not establish (the gap this audit closes)

Round 2 (`it-proofread-gates-round2/proofreader-verdict-round2.md`, ROUND 2 PASS) established via `tools/p8.py compare` that all 11 editions print notes for the same 150 numbers (CLEAN, keydiff=[137,138,139] in all 10 fan-outs, adjudicated as E-section translation re-aims), verified the Round 1 fix sites, and read explanation layers in full (en/de) / P7+P8 (others). It did **not** explicitly establish full key-letter correctness: set-equality cannot catch wrong letters where core and edition agree, and sampled key checks cannot catch frozen-core letter transpositions of the class just found in the ZH-CN sibling family. This audit therefore verified every key semantically, from the printed artifacts — not from the registry alone.

## 1. Method (all read-only, from the shipped SVGs)

1. **Frozen core registry:** read `hidden_files/weekly-report-w46-it-build/content12.py`, `content34.py`, `content56.py`, `content7.py`, `content8.py` (the exercise registration table; P8 answers are generated from it) and `bslib4.py:match_set` (rights printed in listed order, lettered a/b/c/d sequentially). Cross-checked against the core `.text.md` export (stems + inline keys).
2. **Printed stems/options:** extracted the SVG text layer of every shipped core SVG (P1–P8) and verified the *printed* option order for all 61 letter-keyed choice items and all 3 matching blocks — so a rendering-order swap could not hide behind registry agreement. Printed orders matched the registry in every case.
3. **Printed P8 keys:** parsed the RISPOSTE key list out of each edition's shipped `p8-valutazione.svg` (150/150 numbers, no duplicates, in all 11 editions) and compared full key strings edition-by-edition against the core; ran canonical `tools/p8.py compare` as a supplement (see §5).
4. **Semantic verification of all 150:** each key checked against its stem, the issue's own articles/fixtures/chart, Italian grammar, or arithmetic recomputed from the issue's own data (§§2–4).
5. **Regression sites:** P4 stems 56/57 (NON) + P8 notes, and the Q1 replacement sentence + ex. 112 key, re-verified on the printed SVGs of all 11 editions (§6).

## 2. Matching blocks — full verification (the known defect class)

Options are quoted in printed order (a, b, c, d). "Correct" = the letter whose definition matches the word semantically. "Printed" = the P8 key letter in the core AND in every fan-out (identical in all 11; native glosses repeat the same trailing letter — checked programmatically in all editions, PT paren style included).

### Block 1 — P2, ex. 25–28 (A2 · LE PAROLE DI SAN MARTINO)

Printed option list (P2 SVG, verified on the rendered page):
- a. il luogo dove si fa e si conserva il vino
- b. cambiare casa, andare a vivere altrove
- c. il succo d'uva prima che diventi vino
- d. la lunga veste che protegge dal freddo

| # | Stem (word) | Correct letter | Printed letter | Evidence |
|---|---|---|---|---|
| 25 | il mosto — "A San Martino ogni mosto diventa vino"; P2 gloss: mosto = grape juice before it becomes wine | c (il succo d'uva prima che diventi vino) | c | Definition is the literal meaning of *mosto*; P2 article: "«mosto» è il succo d'uva prima che diventi vino". |
| 26 | la cantina — place where wine is made/kept | a (il luogo dove si fa e si conserva il vino) | a | *Cantina* = wine cellar; article: wine "si assaggia nelle cantine". |
| 27 | il mantello — the garment Martino divides | d (la lunga veste che protegge dal freddo) | d | *Mantello* = cloak; legend: Martino "divide con lui il mantello". |
| 28 | traslocare — "fare San Martino voleva dire cambiare casa" | b (cambiare casa, andare a vivere altrove) | b | Article: "«Fare San Martino» … vuol dire traslocare, cambiare casa". |

No transposition. Letters c/a/d/b are a genuine scramble of the word order (mosto, cantina, mantello, traslocare), not an identity mapping — the scramble itself is correct.

### Block 2 — P4, ex. 52–55 (B1 · LE PAROLE)

Printed option list (P4 SVG):
- a. il racconto prima della partita, senza risultati
- b. che decide tutto, molto importante
- c. il gruppo di squadre che giocano tra loro
- d. la pausa del campionato, senza partite

| # | Stem (word) | Correct letter | Printed letter | Evidence |
|---|---|---|---|---|
| 52 | la sosta — "il campionato si ferma per la sosta delle nazionali" | d (la pausa del campionato, senza partite) | d | *Sosta* = break/pause in the league calendar. |
| 53 | il girone — "Nel girone 1 di Lega A, la Francia è prima…" | c (il gruppo di squadre che giocano tra loro) | c | *Girone* = group of teams playing each other (standings table). |
| 54 | decisivo — "le due partite … sono decisive" | b (che decide tutto, molto importante) | b | *Decisivo* = decisive. |
| 55 | la presentazione — previews "senza risultati" | a (il racconto prima della partita, senza risultati) | a | Article: "qui sono presentazioni, senza risultati". |

No transposition. Letters d/c/b/a correct.

### Block 3 — P8 §F, ex. 141–144 (B2 · LE PAROLE DELLA MANOVRA)

Printed option list (P8 SVG, §F block on the same page as the keys):
- a. la parte del sistema fiscale, un livello di reddito
- b. i soldi che pagano una misura, la sua fonte
- c. la differenza tra spese ed entrate, in rosso
- d. la legge di bilancio, il documento dello Stato

| # | Stem (word) | Correct letter | Printed letter | Evidence |
|---|---|---|---|---|
| 141 | la manovra — "La manovra è la legge di bilancio" (P6) | d (la legge di bilancio, il documento dello Stato) | d | P6 lead: "La manovra è la legge di bilancio". |
| 142 | il deficit — "un deficit del 3,4% del PIL" (P6) | c (la differenza tra spese ed entrate, in rosso) | c | Deficit = spending minus revenue; P6: "deficit del 3,4% del PIL". |
| 143 | la copertura — "Ogni misura deve avere la sua ___" | b (i soldi che pagano una misura, la sua fonte) | b | *Copertura* = funding source; P6 "cifre diverse per le coperture". |
| 144 | lo scaglione — "Il secondo ___ Irpef si allarga" | a (la parte del sistema fiscale, un livello di reddito) | a | *Scaglione* = tax bracket; P6 "secondo scaglione Irpef al 33%". |

No transposition. Letters d/c/b/a correct.

**Matching-block result: 12/12 correct, 0 transposed, in core and in all 11 editions.**

## 3. Full 1–150 result: 150/150 correct, 0 wrong keys

Printed core key = P8 RISPOSTE key as printed in the core SVG (identical key string in every fan-out except 137–139 translations and the 150 pointer wording — see §5). Every item below was verified semantically against its printed stem/options and the issue's own text; the "Basis" column gives the deciding evidence. Choice items cite the printed options (verified in §1 step 2).

### P1 (1–10)

| # | Type | Stem (short) / printed options | Printed key | Verdict / basis |
|---|---|---|---|---|
| 1 | fill-in | Mercoledì 11 novembre è ___. | San Martino | CORRECT — P1: "Mercoledì 11 novembre è San Martino". |
| 2 | fill-in | A San Martino ogni ___ diventa vino. | mosto | CORRECT — proverb "ogni mosto diventa vino". |
| 3 | fill-in | In tutta Italia si aprono le ___. | cantine | CORRECT — "Si aprono le cantine". Plural agrees with *le*. |
| 4 | fill-in | Giovedì 12 novembre l'Italia gioca con la ___. | Francia | CORRECT — "l'Italia gioca con la Francia a San Siro". |
| 5 | fill-in | Eurochocolate apre venerdì a ___. | Perugia | CORRECT — "venerdì 13 novembre apre a Perugia Eurochocolate". |
| 6 | fill-in | A Cremona continua la Festa del ___. | Torrone | CORRECT — "a Cremona continua la Festa del Torrone". |
| 7 | choice | San Martino è... A. mercoledì 11 novembre · B. sabato 14 novembre · C. domenica 1° novembre | A | CORRECT — 11 Nov is a Wednesday (calendar-verified in Round 2). |
| 8 | choice | La leggenda … A. un viaggio · B. un mantello diviso · C. una gara | B | CORRECT — cloak legend, P1/P2. |
| 9 | choice | Italia–Francia si gioca... A. a Bruxelles · B. a Perugia · C. a San Siro | C | CORRECT — San Siro, P1/P4/fixture table. |
| 10 | choice | Eurochocolate apre... A. a Cremona · B. a Perugia · C. a Firenze | B | CORRECT — Perugia. |

### P2 (11–28)

| # | Type | Stem / options | Key | Verdict / basis |
|---|---|---|---|---|
| 11 | fill-in | A San Martino ogni ___ diventa vino. | mosto | CORRECT — as #2. |
| 12 | fill-in | Il vino nuovo si assaggia in ___. | cantina | CORRECT — singular after *in*; "nelle cantine" in article. |
| 13 | fill-in | A San Martino si mangiano le ___ arrosto. | castagne | CORRECT — "le castagne arrosto". |
| 14 | fill-in | Martino divide il suo ___ con il mendicante. | mantello | CORRECT — "divide con lui il mantello". |
| 15 | fill-in | In molte case si prepara l'___ arrosto. | oca | CORRECT — "si prepara l'oca arrosto". |
| 16 | fill-in | Martino ___ il mantello… (dividere) | divide | CORRECT — 3sg present of *dividere*. |
| 17 | fill-in | Noi ___ il vino nuovo… (assaggiare) | assaggiamo | CORRECT — 1pl present *assaggiamo*. |
| 18 | fill-in | Le cantine ___ le porte… (aprire) | aprono | CORRECT — 3pl present *aprono*. |
| 19 | fill-in | Noi ___ le castagne arrosto. (mangiare) | mangiamo | CORRECT — 1pl present *mangiamo*. |
| 20 | fill-in | L'estate di San Martino ___ tre giorni… (durare) | dura | CORRECT — 3sg *dura*; subject *l'estate* singular. |
| 21 | choice | Leggenda… A. un viaggio · B. un mantello diviso · C. una gara | B | CORRECT — as #8. |
| 22 | choice | «Fare San Martino»… A. traslocare · B. vendemmiare · C. viaggiare | A | CORRECT — "voleva dire cambiare casa" = *traslocare*. |
| 23 | choice | Cantine Aperte dura fino al... A. 7 · B. 11 · C. 15 novembre | C | CORRECT — "Dal 1° al 15 novembre". |
| 24 | choice | Il Festival dei Popoli ha presentato... A. 50 · B. 86 · C. 19 film | B | CORRECT — 86 films (50 = Forum Cultura events, distractor). |
| 25–28 | matching | see §2 Block 1 | c / a / d / b | CORRECT — see §2. |

### P3 (29–46)

| # | Type | Stem / options | Key | Verdict / basis |
|---|---|---|---|---|
| 29 | choice | Secondo weekend del Torrone... A. 7–8 · B. 14–15 · C. 21–22 nov | B | CORRECT — "sabato 14 e domenica 15 novembre". |
| 30 | choice | Eurochocolate dura fino al... A. 6 dic · B. 15 nov · C. 22 nov | C | CORRECT — "fino al 22 novembre". |
| 31 | choice | Eurochocolate è alla sua... A. 29ª · B. 32ª · C. 67ª edizione | B | CORRECT — 32nd (29ª = Torrone, 67ª = Festival dei Popoli). |
| 32 | choice | Titolo Eurochocolate 2026... A. «Fate dolci» · B. «Il Confine» · C. «Legacy» | A | CORRECT — «Fate dolci» («Il Confine» = Torrone theme). |
| 33 | choice | Fiera del Tartufo di Alba chiude... A. 22 nov · B. 6 dic · C. 8 nov | B | CORRECT — "continua fino al 6 dicembre". |
| 34 | fill-in (box) | A Cremona si festeggia il ___. | torrone | CORRECT — box word *torrone*; Cremona = Torrone. |
| 35 | fill-in (box) | A Perugia si festeggia il ___. | cioccolato | CORRECT — Perugia = Eurochocolate. |
| 36 | fill-in (box) | Per i più piccoli c'è il ___ della dolcezza. | laboratorio | CORRECT — "laboratori per i più piccoli"; singularised stem per KIT fix (keys unchanged). |
| 37 | fill-in (box) | Alla festa c'è una ___ con i dolci. | degustazione | CORRECT — "degustazioni" in article; singular *una degustazione* fits. |
| 38 | fill-in (box) | Il torrone è fatto di ___ e miele. | mandorle | CORRECT — torrone of almonds + honey (also P8 §G dialogue). |
| 39 | fill-in (box) | Il ___ bianco è il fungo più prezioso d'Italia. | tartufo | CORRECT — "il fungo più prezioso" = white truffle. Box fully used once each (6 words / 6 stems). |
| 40 | fill-in | Il Treno Storico ___ (arrivare) a Cremona domenica. | è arrivato | CORRECT — *arrivare* takes *essere*; masc. sg. *è arrivato*. |
| 41 | fill-in | Noi ___ (assaggiare) il torrone a Cremona. | abbiamo assaggiato | CORRECT — *assaggiare* takes *avere*. |
| 42 | fill-in | I visitatori ___ (andare) a Perugia… | sono andati | CORRECT — *andare* takes *essere*, masc. pl. |
| 43 | fill-in | Perugia ___ (aprire) Eurochocolate venerdì. | ha aperto | CORRECT — *aprire* takes *avere*. |
| 44 | sentence | Eurochocolate / è a Perugia / dal 13 novembre | Eurochocolate è a Perugia dal 13 novembre. | CORRECT — S + *essere* + place + date; fact: opens Fri 13 Nov in Perugia. |
| 45 | sentence | a Cremona / il torrone / è il re | A Cremona il torrone è il re. | CORRECT — fronted place + subject + predicate; word-order exercise. |
| 46 | sentence | la fiera / dura / fino al 6 dicembre | La fiera dura fino al 6 dicembre. | CORRECT — *dura fino a* = lasts until; Alba fair to 6 Dec. |

### P4 (47–64)

| # | Type | Stem / options | Key | Verdict / basis |
|---|---|---|---|---|
| 47 | choice | Italia–Francia... A. dom 15 · B. gio 12 · C. lun 9 nov | B | CORRECT — Thu 12 Nov, fixture table. |
| 48 | choice | Domenica, l'Italia gioca... A. San Siro · B. Bruxelles · C. Torino | B | CORRECT — Belgium–Italy in Brussels, Sun 15. |
| 49 | choice | Nel girone, la Francia ha... A. 10 · B. 7 · C. 6 punti | A | CORRECT — standings: France 10, Italy 7, Belgium 6, Turkey 0. |
| 50 | choice | Le partite … sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati | C | CORRECT — previews only; matches played after press time. |
| 51 | choice | Le ATP Finals si giocano... A. Milano · B. Torino · C. Bruxelles | B | CORRECT — Inalpi Arena, Turin. |
| 52–55 | matching | see §2 Block 2 | d / c / b / a | CORRECT — see §2. |
| 56 | fill-in | Le partite di domenica sera NON cominciano ___ di quelle di giovedì. (tardi) | più tardi | CORRECT — both matches 20:45 (P1 cifre, P4 article, fixture table, week plan). Negated stem: Sunday's do NOT start later. Without NON the key would be false; with NON it is true. See §6. |
| 57 | fill-in | Le partite di giovedì NON cominciano ___ di quelle di domenica. (presto) | più presto | CORRECT — same 20:45 facts; Thursday's do NOT start earlier. See §6. |
| 58 | fill-in | …la serata di giovedì è la serata ___ del weekend. (bella) | più bella | CORRECT — *la serata più bella del weekend* = superlative with definite article; note flags it as a subjective judgement (see observation O-K2). |
| 59 | transform | L'Italia gioca bene. → L'Italia gioca ___ (bene). | meglio | CORRECT — irregular comparative of *bene* is *meglio*. |
| 60 | fill-in | La mia squadra ___ (vincere) la partita di ieri. | ha vinto | CORRECT — *vincere* takes *avere*; *ha vinto*. |
| 61 | fill-in | La mia squadra ___ (pareggiare) 1–1. | ha pareggiato | CORRECT — *pareggiare* takes *avere*. |
| 62 | fill-in | I tifosi ___ (arrivare) allo stadio alle cinque. | sono arrivati | CORRECT — *arrivare* + *essere*, masc. pl. |
| 63 | fill-in | Noi ___ (guardare) la partita in televisione. | abbiamo guardato | CORRECT — *guardare* + *avere*. |
| 64 | fill-in | Il portiere ___ (prendere) un gol al 90°. | ha preso | CORRECT — irregular past participle *preso*; *ha preso*. |

### P5 (65–82)

| # | Type | Stem / options | Key | Verdict / basis |
|---|---|---|---|---|
| 65 | choice | Scrittorincittà è a... A. Milano · B. Cuneo · C. Firenze | B | CORRECT — Cuneo, 11–15 Nov. |
| 66 | choice | Scrittorincittà ha... A. 50 · B. più di 100 · C. 19 autori | B | CORRECT — "più di cento autori". |
| 67 | choice | Il tema … A. «Legacy» · B. «Fate dolci» · C. «Finestrini» | C | CORRECT — theme «Finestrini». |
| 68 | choice | Il Filmmaker Festival è a... A. Milano · B. Cuneo · C. Perugia | A | CORRECT — Milan, 14–22 Nov. |
| 69 | choice | L'Offside Festival parla di... A. calcio e cultura · B. solo libri · C. solo dolci | A | CORRECT — "quattro giorni di calcio e cultura". |
| 70 | fill-in (box) | A Cuneo arrivano più di cento ___. | autori | CORRECT — plural of *autore* (box note: some words become plural). |
| 71 | fill-in (box) | Il Filmmaker Festival è un festival del cinema ___. | indipendente | CORRECT — "cinema indipendente e della sperimentazione". |
| 72 | fill-in (box) | Si entra in un libro come da un ___. | finestrino | CORRECT — "come da un finestrino". |
| 73 | fill-in (box) | L'Offside Festival ha tanti ___ importanti. | ospiti | CORRECT — plural of *ospite* ("ospiti, incontri e storie"). |
| 74 | fill-in (box) | Le piazze profumano di ___ arrosto. | castagne | CORRECT — "profumano di caldarroste"; *castagne arrosto*. |
| 75 | fill-in (box) | Il Filmmaker Festival è il festival della ___. | sperimentazione | CORRECT — "della sperimentazione". Box fully used once each. |
| 76 | fill-in | Mercoledì noi ___ (andare) a Cuneo… | andremo | CORRECT — futuro 1pl *andremo*. |
| 77 | fill-in | A Milano ___ (esserci) tanto cinema giovane. | ci sarà | CORRECT — futuro of *esserci*, 3sg *ci sarà*. |
| 78 | fill-in | Giovedì noi ___ (guardare) Italia–Francia. | guarderemo | CORRECT — futuro 1pl *guarderemo*. |
| 79 | fill-in | Eurochocolate ___ (durare) fino al 22 novembre. | durerà | CORRECT — futuro 3sg *durerà*. |
| 80 | true/false | Scrittorincittà ha più di 100 autori. | Vero | CORRECT — article fact. |
| 81 | true/false | Il Filmmaker Festival è a Milano. | Vero | CORRECT — article fact. |
| 82 | true/false | Scrittorincittà chiude il 22 novembre. | Falso | CORRECT — closes 15 Nov (22 Nov is Filmmaker/Eurochocolate closing). |

### P6 (83–100)

| # | Type | Stem / options | Key | Verdict / basis |
|---|---|---|---|---|
| 83 | choice | Città più fredda del grafico... A. Milano · B. Torino · C. Napoli | B | CORRECT — chart: Torino 6° < Milano 7° < Bologna 8° < Roma 12° < Napoli 14°. |
| 84 | choice | Città più calda... A. Napoli · B. Roma · C. Bologna | A | CORRECT — Napoli 14°, highest. |
| 85 | choice | Differenza Napoli (14°) – Roma (12°)... A. 3° · B. 2° · C. 4° | B | CORRECT — recomputed: 14 − 12 = 2. |
| 86 | choice | Milano (7°) + Bologna (8°)... A. 15° · B. 14° · C. 16° | A | CORRECT — recomputed: 7 + 8 = 15. |
| 87 | choice | I numeri del grafico sono... A. previsioni reali · B. dati inventati · C. temperature di ieri | B | CORRECT — chart labelled DATI INVENTATI PER L'ESERCIZIO on page (title, header, caption, stem). |
| 88 | choice | «Il governo propone»... A. non è ancora legge · B. è già legge · C. è un errore | A | CORRECT — "approvato dal governo non vuol dire già legge"; text not yet law. |
| 89 | choice | La manovra è... A. una festa · B. la legge di bilancio · C. un film | B | CORRECT — P6 lead. |
| 90 | choice | Le Camere devono votare... A. entro fine anno · B. entro 9 nov · C. mai | A | CORRECT — "discusso e votato dalle Camere entro la fine dell'anno". |
| 91 | choice | Il DPB mandato a Bruxelles... A. 15 ott · B. 19 ott · C. 28 ott | A | CORRECT — 15 Oct (28 Oct = Council approval, distractor). |
| 92 | choice | Crescita prevista 2027... A. +3,4% · B. +0,8% · C. +5% | B | CORRECT — growth +0.8% (3.4% = deficit figure, distractor). |
| 93 | fill-in | È probabile che domani ___ (piovere)… | piova | CORRECT — *è probabile che* + subjunctive; *piovere* → *piova*. |
| 94 | fill-in | È possibile che in montagna ___ (nevicare)… | nevichi | CORRECT — subjunctive; *nevicare* → *nevichi*. |
| 95 | fill-in | Bisogna che i lettori ___ (controllare)… | controllino | CORRECT — *bisogna che* + subjunctive 3pl *controllino*. |
| 96 | fill-in | È importante che la cifra ___ (essere) chiara… | sia | CORRECT — subjunctive of *essere* → *sia*. |
| 97 | fill-in (box) | La ___ è la legge di bilancio. | manovra | CORRECT — box word fits uniquely; P6 lead. |
| 98 | fill-in (box) | Il ___ previsto per il 2027 è del 3,4% del PIL. | deficit | CORRECT — "deficit del 3,4% del PIL". |
| 99 | fill-in (box) | Ogni misura deve avere la sua ___. | copertura | CORRECT — *copertura* = funding for a measure. |
| 100 | fill-in (box) | Il secondo ___ Irpef si allarga… | scaglione | CORRECT — "secondo scaglione Irpef". Box fully used once each. |

### P7 (101–112)

| # | Type | Stem / options | Key | Verdict / basis |
|---|---|---|---|---|
| 101 | fill-in | Mercoledì noi ___ (andare) a Cuneo. | andremo | CORRECT — futuro 1pl (P7 A2 column). |
| 102 | fill-in | Noi ___ (assaggiare) il vino nuovo. | assaggeremo | CORRECT — futuro 1pl of *assaggiare* (*assaggeremo*). |
| 103 | fill-in | Giovedì noi ___ (guardare) Italia–Francia. | guarderemo | CORRECT — futuro 1pl. |
| 104 | choice | L'estate di San Martino... A. dura tre giorni · B. durerà tre giorni · C. durava tre giorni | B | CORRECT — futuro form taught in the A2 column; column bridge itself models "durerà tre giorni" ("Il verbo è durare, regolare"). See observation O-K1. |
| 105 | fill-in | Il Treno Storico ___ (arrivare) a Cremona. | è arrivato | CORRECT — as #40. |
| 106 | fill-in | Noi ___ (assaggiare) il torrone a Cremona. | abbiamo assaggiato | CORRECT — as #41. |
| 107 | fill-in | I visitatori ___ (andare) a Perugia. | sono andati | CORRECT — as #42. |
| 108 | choice | Perugia ___ Eurochocolate. A. è aperta · B. ha aperto · C. sono aperti | B | CORRECT — *aprire* takes *avere*; A is ungrammatical with the object, C disagrees (plural vs *Perugia*). |
| 109 | fill-in | È probabile che domani ___ (piovere)… | piova | CORRECT — as #93. |
| 110 | fill-in | È possibile che in montagna ___ (nevicare)… | nevichi | CORRECT — as #94. |
| 111 | fill-in | Bisogna che la cifra ___ (essere) chiara… | sia | CORRECT — as #96. |
| 112 | choice | «So che il sole...» A. torni · B. torna · C. tornare | B | CORRECT — *so che* + indicative *torna* (vs subjunctive after *è probabile che*); Q1 replacement sentence ("la Festa del Torrone è a Cremona") is the column's other indicative fact example. See §6. |

### P8 (113–150)

| # | Type | Stem / printed options | Key | Verdict / basis |
|---|---|---|---|---|
| 113 | cloze-choice | Mercoledì 11 novembre è ___. (A. Natale · B. San Martino) | B | CORRECT. |
| 114 | cloze-choice | …ogni mosto diventa ___. (A. vino · B. latte) | A | CORRECT — proverb. |
| 115 | cloze-choice | Italia–Francia si gioca a ___. (A. San Siro · B. Cremona) | A | CORRECT. |
| 116 | cloze-choice | Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo) | A | CORRECT. |
| 117 | cloze-choice | La Festa del Torrone continua a ___. (A. Milano · B. Cremona) | B | CORRECT. |
| 118 | cloze-choice | Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86) | B | CORRECT. |
| 119 | cloze-choice | Belgio–Italia si gioca domenica ___. (A. sera · B. mattina) | A | CORRECT — 20:45 evening kickoff. |
| 120 | cloze-choice | Scrittorincittà è a ___. (A. Milano · B. Cuneo) | B | CORRECT. |
| 121 | choice | L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora | B | CORRECT — proverb "tre giorni e un pochino". |
| 122 | choice | Martino divide... A. il pane · B. il mantello · C. il vino | B | CORRECT — cloak. |
| 123 | choice | Eurochocolate è alla sua... A. 32ª · B. 29ª · C. 67ª edizione | A | CORRECT — as #31. |
| 124 | choice | Nel girone, la Francia ha... A. 7 · B. 10 · C. 0 punti | B | CORRECT — standings (option order differs from #49; key follows printed options). |
| 125 | choice | Fiera del Tartufo chiude... A. 22 nov · B. 8 nov · C. 6 dic | C | CORRECT — as #33 (option order differs from #33; key follows printed options). |
| 126 | choice | Il DPB partito per Bruxelles... A. 15 ott · B. 19 ott · C. 28 ott | A | CORRECT — as #91. |
| 127 | choice | «Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore | B | CORRECT — as #88 (option order differs from #88; key follows printed options). |
| 128 | choice | Il Festival dei Popoli si è chiuso... A. 31 ott · B. 8 nov · C. 15 nov | B | CORRECT — closed Sun 8 Nov; 31 Oct = opening. |
| 129 | choice | Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due | B | CORRECT — passage: Giulia (Cuneo) goes Wed 11 Nov; Paolo (Cremona) goes to Torrone. |
| 130 | choice | Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio | A | CORRECT — passage: Paolo, Sat 14 Nov, Festa del Torrone. |
| 131 | choice | L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno | B | CORRECT — Giulia "ascolta un autore". |
| 132 | choice | Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo» | A | CORRECT — two cities (Cuneo, Cremona), two festivals (Scrittorincittà, Torrone); other titles off-topic. |
| 133 | sentence | mercoledì / è / San Martino | Mercoledì è San Martino. | CORRECT — time-fronted statement; Wednesday 11 Nov is San Martino. |
| 134 | sentence | Eurochocolate / è a Perugia / dal 13 novembre | Eurochocolate è a Perugia dal 13 novembre. | CORRECT — as #44. |
| 135 | sentence | a che ora / gioca / l'Italia / ? | A che ora gioca l'Italia? | CORRECT — interrogative phrase fronted; *a che ora* + verb + subject. |
| 136 | sentence | il vino nuovo / si assaggia / in cantina | Il vino nuovo si assaggia in cantina. | CORRECT — subject + verb + place. |
| 137 | translate | A San Martino ogni mosto diventa vino. → (into reader language) | 圣马丁节葡萄汁变成酒。 | CORRECT — faithful translation; fan-out renderings verified per edition (§5). |
| 138 | translate | Giovedì sera si gioca Italia–Francia. → | 周四晚上意大利对法国。 | CORRECT — *si gioca* = a match is played; fan-out renderings verified (§5). |
| 139 | translate | Domenica sera si gioca Belgio–Italia. → | 周日晚上，比利时对意大利。 | CORRECT — as #138; fan-out renderings verified (§5). |
| 140 | translate | 每个数字都必须清楚。→ (into Italian) | Ogni cifra deve essere chiara. | CORRECT — 每→ogni, 数字→cifra, 必须→deve, 清楚→chiara (fem. agreement with *cifra*). Identical Italian key in all 11 editions. |
| 141–144 | matching | see §2 Block 3 | d / c / b / a | CORRECT — see §2. |
| 145 | cloze-choice | — Cerco il ___ di Cremona. (A. biglietto · B. torrone) | B | CORRECT — "il torrone di Cremona". |
| 146 | cloze-choice | — È fatto di ___ e miele. (A. mandorle · B. patate) | A | CORRECT — torrone of almonds + honey. |
| 147 | cloze-choice | — Quanto ___ tutto? (A. dorme · B. costa) | B | CORRECT — *quanto costa?* = how much? |
| 148 | cloze-choice | — Pago con ___. (A. carta · B. cosplay) | A | CORRECT — *pagare con carta* = pay by card. |
| 149 | cloze-choice | — La festa dura fino al ___. (A. 6 dic · B. 22 nov) | B | CORRECT — Torrone festival to 22 Nov (6 Dec = truffle fair). |
| 150 | writing | «La tua settimana di San Martino», 80–100 words | ✓ model text (98 words) | CORRECT — no unique key; model text word-count recomputed: 98 words, within the 80–100 brief. Model text restates issue facts (11 Nov, cantina, cloak legend, Torrone/Cremona, 20:45 matches) with no invented fact. |

**Full-result count: 150 correct / 0 wrong. No frozen-core transposition, no wrong letter, no wrong word/phrase key, no arithmetic error.**

## 4. Observations (non-blocking; neither is a wrong key)

- **O-K1 (ex. 104):** option A (*dura tre giorni*, present) is grammatical Italian in isolation. Key B (*durerà*) stands: the item sits in the P7 A2 *futuro semplice* column, ex. 101–103 are futuro blanks, and the column bridge itself models "durerà tre giorni". The exercise tests the futuro form; B is the uniquely intended key. Recorded for transparency, not raised as a defect.
- **O-K2 (ex. 58):** *più bella* is read as the relative superlative ("the finest evening of the weekend") via the definite article + *del weekend*; the P8 note itself flags it as a subjective judgement. Key stands.
- **ES ex. 57 note wording:** "no es antes que" is slightly awkward Spanish for "not earlier than", but the meaning and the 20:45 facts are unambiguous and the key (*più presto*) is unaffected. Not a key defect; no action.

## 5. Per-edition P8 key agreement (all 11 editions)

Method: full key-string comparison of each edition's printed RISPOSTE list against the core's (independent SVG-text parse), plus canonical `tools/p8.py compare` as supplement (re-run by this auditor; `extract` noted 150/150 for the core).

| Edition | P8 keys 1–150 present | Key strings identical to core except | Letters/word-keys differing | Native glosses contradicting a letter? |
|---|---|---|---|---|
| zh-cn (core) | 150/150 | — | — | No |
| de | 150/150 | 137, 138, 139, 150-pointer | None (137–139 are German translations, each verified: "An Martinstag wird Most zu Wein." / "Donnerstagabend: Italien–Frankreich." / "Sonntagabend: Belgien–Italien."; 140 Italian key identical) | No — high-risk notes (47/48/49/56/57/83–86/91/92/124/128) checked, all agree with letters |
| en | 150/150 | 137, 138, 139, 150-pointer | None (137–139 verified: "At San Martino, grape must becomes wine." / "On Thursday evening, Italy play France." / "On Sunday evening, Belgium v Italy.") | No |
| es | 150/150 | 137, 138, 139, 150-pointer | None (137–139 verified: "En San Martín, el mosto se convierte en vino." / "El jueves por la noche: Italia–Francia." / "El domingo por la noche: Bélgica–Italia.") | No |
| fr | 150/150 | 137, 138, 139, 150-pointer | None (137–139 verified: "À la Saint-Martin, le moût devient vin." / "Jeudi soir : Italie–France." / "Dimanche soir : Belgique–Italie.") | No |
| ja | 150/150 | 137, 138, 139, 150-pointer | None (137–139 verified in Japanese; 140 "into Italian" direction as printed) | No |
| ko | 150/150 | 137, 138, 139, 150-pointer | None (137–139 verified in Korean) | No |
| nl | 150/150 | 137, 138, 139, 150-pointer | None (137–139 verified: "Met Sint-Maarten wordt most wijn." / "Donderdagavond: Italië–Frankrijk." / "Zondagavond: België–Italië.") | No — shortened 56/57 notes still state both-at-20:45 + negation |
| pt | 150/150 | 137, 138, 139, 150-pointer | None (137–139 verified: "Em São Martinho, o mosto vira vinho." / "Na quinta à noite: Itália–França." / "No domingo à noite: Bélgica–Itália."; paren answer style) | No |
| ru | 150/150 | 137, 138, 139, 150-pointer | None (137–139 verified: "В день святого Мартина сусло становится вином." / "В четверг вечером: Италия–Франция." / "В воскресенье вечером: Бельгия–Италия.") | No |
| zh-tw | 150/150 | 137, 138, 139, 150-pointer | None (137–139 are the same translations in traditional characters; 140 identical) | No |

- **p8.py supplement:** `compare` = CLEAN, missing=[], extra_count=0, uncertain=[], keydiff=[137,138,139] for all 10 fan-outs; core self-compare keydiff=[]. This agrees exactly with the independent full-string comparison (which additionally shows the 150-pointer wording difference, a native-language pointer, not a key difference — p8.py normalises it).
- **Printed stems in fan-outs:** probe stems 7 (P1), 47 (P4), 85 (P6), 104 (P7), 145 (P8) verified character-identical in all 11 editions' SVGs (frozen layer intact); matching-block option lists verified on core P2/P4/P8 renderings and keys identical across editions.
- **Matching-gloss check:** in every edition, each matching P8 note repeats its word-gloss with the same trailing letter as the printed key (25–28, 52–55, 141–144) — no gloss contradicts its letter.

## 6. Regression check on Round 1/2 fix sites (keys only)

| Site | Check on printed SVGs, all 11 editions | Result |
|---|---|---|
| P4 stems 56/57 | `NON cominciano` ×2 in every edition's P4 SVG; stems read "Le partite di domenica sera NON cominciano ___ di quelle di giovedì. (tardi)" / "Le partite di giovedì NON cominciano ___ di quelle di domenica. (presto)" | PASS ×11 |
| P8 keys/notes 56/57 | Keys `più tardi` / `più presto` in every edition; every edition's note states both matches at 20:45 (20.45 / 20:45 / 20 h 45 / 20시 45분 / 20時45分) PLUS the negation ("not later" / "not earlier" in the reader's language; full note text read in all 11) | PASS ×11; keys verified against the negated stems and the 20:45 fixture facts (P1 cifre, P4 article, fixture table, week plan) |
| Q1 replacement sentence | "la Festa del Torrone è a Cremona" present in every edition's P7 SVG; old "la finale è a Perugia" absent in every edition | PASS ×11 |
| Q1 exercise key (ex. 112) | P8 key B (*torna*, indicative after *so che*) in every edition; column contrast (subjunctive after *è probabile che* vs indicative after *so che/scrivono che*) intact | PASS ×11 |

## 7. Final line

**KEY AUDIT PASS (all 150 keys correct in core + all 11 editions; Round 2 PASS stands)**

Wrong keys: none. No fix round is needed for keys.
