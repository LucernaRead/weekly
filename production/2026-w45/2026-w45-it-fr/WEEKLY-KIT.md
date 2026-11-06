# La Lucerna — HEBDOMADAIRE ITALIEN VOL.2 · W45 IT × FR

**Pairing:** Italian target text (frozen W45 IT core, `files/weekly-report-w45-it-core/`) + explanation layer written natively in **French**, for francophone readers.
**Status:** builder-complete. **Independent proofread: PENDING** (parent runs it; repo insert + Discord posting happen only after it passes — not done here). No Discord post, no GitHub push, no chat card/PDF dump, no cron was made by this build.

## 1. Spec
- Issue: week Mon Nov 2 – Sun Nov 8, 2026; issue dated Mon Nov 2, 2026. VOL.2 for Italiano.
- Format: 8 pages, 1950×2700 px, 4 columns, warm ivory paper, dark olive-green accents.
- Masthead: "La Lucerna" (Italian feminine noun, article La, UnifrakturMaguntia).
- Pairing / explanation layer: **Italian text + explanations in French** — the same convention as the W43 IT × FR edition (small grey notes, gloss boxes, exercise instructions, answer notes). Every explanation, gloss, bridge and answer note is in French; the Italian article text is original, never translated from another language.
- Exercises: 150 total, continuously numbered 1–150. By page: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38. By level: A2 47, B1 70, B2 33. P8 writing model text: 81 words (brief 80–100). Counts verified twice: build registry print AND an independent SVG expansion count (exercise-number/range nodes paired with their level chips by baseline + x-offset; match ranges 25–28 and 52–55 and 141–144 counted at their chip level).
- P8: sections A cronaca 8, B generali 8, C leggi e rispondi 4, D frasi 4, E traduci 4, F matching 4, G dialogo 5, H scrittura 1. Answers generated from the exercise registration table in the build code (content12/34/56/7/8.py), not hand-typed.
- P7 golden sentences: 8 quotes, each verified to occur exactly 2× in the joined SVG text (case-sensitive quote form: once in its article, once on P7) — see §7.

## 2. Contents per page (core topics, unchanged)
- P1 Prima (A2) — «Arriva il primo freddo: l'Italia si copre e si mette a tavola». Lead: first cold snap + Forum Cultura + Panettone/Torrone weekend + Serie A. LA SETTIMANA day-by-day box, LA SETTIMANA IN CIFRE, LA PAROLA DELLA SETTIMANA (il primo freddo), frost drawing (redazione), IN BREVE, QUIZ LAMPO. Ex. 1–10.
- P2 Vita (A2) — «Il primo freddo: come ci si veste e che cosa si mangia». Clothing/layering, heating, chrysanthemums; Nov 2 Commemorazione dei defunti + regional school closures. Just-passed box: Lucca Comics 60th, Ognissanti Sun Nov 1 (no ponte), Manovra vote expected ~Oct 28 — NO outcome claimed (disclosed on-page, Italian + French). IL 2 NOVEMBRE wide box. Ex. 11–28.
- P3 Cultura (A2→B1) — «Il weekend più dolce: panettone a Milano, torrone a Cremona». Panettone World Cup final Milan Nov 7–8 (19 countries, traditional + chocolate categories, free public tasting); Festa del Torrone Cremona Nov 7–22; Alba White Truffle Fair to Dec 6; Forum Cultura Milan Nov 3–8. Photo: tartufo. Ex. 29–46.
- P4 Sport (B1) — «L'undicesima giornata: Genoa–Milan, Inter–Como, Fiorentina–Juventus». Serie A matchday 11 Fri Nov 6–Sun Nov 8; European matchday 4 Tue Nov 3–Thu Nov 5. ALL matches are previews with explicit "senza risultati" notes. Full-width fixture table. Ex. 47–64.
- P5 Giovani (B1) — «Dopo Lucca: la settimana giovane continua a Milano e Firenze». Lucca Comics 60th, theme «Legacy», Oct 28–Nov 1, closed Sun Nov 1; Forum Cultura; Festival dei Popoli Florence Nov 3–9. Photo: castagne. Ex. 65–82.
- P6 Approfondimento (B2) — «Come si legge una previsione: probabilità, non certezze». ECMWF models, probability vs certainty. Practice-data chart of example minimum temperatures (Torino 3°, Milano 4°, Bologna 5°, Roma 9°, Napoli 12°) EXPLICITLY labeled on-page "DATI INVENTATI PER L'ESERCIZIO / NON sono previsioni reali". Manovra sidebar uses only verified items with NO outcome claimed. Ex. 83–100.
- P7 Lingua (A2/B1/B2) — A2 weather impersonals; B1 passato prossimo with essere/avere; B2 congiuntivo of probability. ERRORI TIPICI 4. LA PAROLA «l'assaggio» (Italian definition sentence FROZEN verbatim — see §5). LETTERE = labeled editor's example (Li, Pechino) + open invitation for real letters in VOL.3 (see §5). FRASI DELLA SETTIMANA 8 quotes. Preview for VOL.3. Ex. 101–112.
- P8 Valutazione e risposte — all 150 answers, grouped by page, with one-line French notes. Writing topic «La tua settimana del primo freddo» (80–100 words); model text 81 words. Ex. 113–150.

## 3. Furniture (as rendered; W43 IT × FR shipped SVGs are the authority)
- Masthead: **La Lucerna**
- P1 badge (brick #a4553a, 22pt bold, INSERTED at y=574 centered): `TEXTES EN ITALIEN · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES` — byte-identical to the shipped W43 IT × FR badge (verified byte-for-byte after fix round 4; the round-1 U+2019 apostrophe was corrected to the shipped ASCII apostrophe). Geometry differs from W43 (see §8: W43 replaced the tagline slot at y=372, 20pt; the W45 core's y=372 is frozen Italian strapline, so the badge is inserted at y=574 following the W45 IT × EN precedent and tools README #20's FR/IT family case).
- P1 edition line (46pt serif bold, ink 1788.5px ≤ 1820): `JOURNAL ITALIEN · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A` (W43 JOURNAL short variant, VOL.1 → VOL.2).
- P1 band right lines: `LE PREMIER FROID ARRIVE CETTE SEMAINE` / `La semaine du premier froid · Voir page 2`
- Band subs: P2 `VITA · VIE QUOTIDIENNE`, P3 `CULTURA · CULTURE`, P4 `SPORT · SPORT`, P5 `GIOVANI · JEUNESSE`, P6 `APPROFONDIMENTO · EN PROFONDEUR`, P7 `LINGUA · LANGUE`, P8 `VALUTAZIONE E RISPOSTE · EXERCICES ET RÉPONSES` / `Page 8 · …`
- Footers, all 8 pages: `La Lucerna · HEBDOMADAIRE ITALIEN VOL.2 · TEXTE EN ITALIEN · EXPLICATIONS EN FRANÇAIS` and `Page N sur 8`
- Gloss prefix: `Note — `; P8 answer-key title: `RISPOSTE · CORRIGÉS — classés par page, cherchez le numéro`; P8 separators stay Italian `— PAGINA n —` (W43 precedent).
- Instruction labels: Compléter / Former une phrase / Vrai ou faux / Associer / Traduire en français / Traduire en italien / Écrire.
- P8 E-section re-aiming (W43 IT × FR ruling): items 137–139 are IT→FR (French keys, Italian bodies unchanged); item 140 is FR→IT (French body, Italian key byte-identical).

## 4. Method & baseline proof
- Build dir: `hidden_files/weekly-report-w45-it-fr-build/` — a copy of the core build (`weekly-report-w45-it-build/`), transformed only by `transform.py` (literal replacements, abort-on-mismatch, per content file; fix rounds appended to the same file, never hand-edited content files).
- **Baseline proven before any edit:** `tools/freeze.py baseline` on the unmodified core build reproduced all 8 shipped core SVGs byte-identically (sha256 matched all 8), and re-hashed the shipped core SVGs afterwards to prove they were untouched. Core SVGs re-verified untouched at the end of this build (8/8 sha256 OK against the pre-build baseline).
- Only the explanation layer was rewritten. Italian target text is byte-identical to the core, with the documented exceptions in §3/§5 (none — every Italian string change is either a P8 note-side punctuation/translation or a wrapped line fragment of an explanation string; see §7).
- Full SVG text-node diff vs core reviewed: every removed string contains Chinese (explanation layer) except 11 wrapped fragments / note-side items listed in §7, all adjudicated with keys byte-identical per `p8.py`.
- CJK scan of all 8 final SVGs: **zero**. Banned intermediary term: absent from the paper SVGs, the ABSTRACT, and all build code.
- Images: the 2 embedded photo payloads (P3 tartufo, P5 castagne) are byte-identical to the core; credit lines unchanged (Italian apparatus of the frozen core). P1 frost drawing + P2 clocks + P6 chart are programmatic, as in the core.

## 5. P7 word box & readers' corner (hard gates)
- **LA PAROLA «l'assaggio»:** the Italian definition sentence is FROZEN verbatim: « l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone. Only the gloss line below it is localised into French: `assaggio = dégustation. Voir page 3, finale du Panettone.` (2 lines, second line descender-free — see fix round 3).
- **LETTERE DEI LETTORI — no fabrication:** no reader, letter, name, or quote was invented as real. The page prints the frozen Italian editor's-example label `(esempio della redazione)` on the letter itself, plus a French note stating all three disclosure facts — no real letters yet, no best page-8 essay yet, the sample stands in and both are promised for VOL.3 — plus an explicit imperative invitation with a VOL.3 publication promise: `Exemple de rédaction, pas une vraie lettre : pas encore de lettres ni de meilleur texte page 8, promis au VOL.3. Écrivez-nous !` The disclosure therefore exists as the Italian original label + the French equivalent sentence on the same page.

## 6. Build / reproduce
- Build dir: `hidden_files/weekly-report-w45-it-fr-build/` (transform.py + per-round sha256 baselines + all tool outputs + scans.py + raw tool outputs).
- Pipeline (W43/W45 pipeline reused as-is):
  - Transform: `cd hidden_files/weekly-report-w45-it-fr-build && ../../tools/venv/bin/python transform.py` (re-runnable from a fresh core copy: round-1 + fix rounds 1–4 in one file).
  - Build: `../../tools/venv/bin/python run.py` (ONE process only — never run content modules standalone, per tools/README lessons 7/11).
  - Render: `../../tools/venv/bin/python render.py` (writes svg/ + cards/ + both PDFs into files/weekly-report-w45-it-fr/).
- Interpreters (both steps use the persistent tools venv, never system python3 which lacks cairosvg):
  - run.py: `tools/venv/bin/python` — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1, pypdf 6.21.2.
  - render.py: `tools/venv/bin/python` — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1, pypdf 6.21.2.
- Final build: FLOW OVERFLOW 0, HEAD TOO WIDE 0; TOTAL 150; by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}; by level {A2: 47, B1: 70, B2: 33}; model words 81; P7 col3 ends 1673.0 (core value, 13px clear of the FRASI rule at 1686); P8-keys flow ends y=2514 (38px clear of bottom 2552); P8-ex flow ends y=965 (bottom 1332).
- Print PDF: `La-Lucerna-VOL2-FR.pdf` — 7,207,873 bytes, sha256 `5abb80f209355a3b43033b14008207b5f12e6305626551d6d216d9c78410af27`, 8 pages.
- Web PDF: `La-Lucerna-VOL2-FR-web.pdf` — 3,644,909 bytes (< 10 MB), sha256 `d154fc10ec78839453d34b2de7af57e5b8b4b3700683fdb4e83f803857b69f6a`, 8 pages.
- SVG sha256 (final, after fix round 4): p1 `a551611531cfaa2fdd26f383d1cf50a989af57c6c7ea3f9934b6193ce9e9e6e2`, p2 `b35596fe82b3f8aa5408b744bcad71b70735b40b6e39b3b96967d1ebd9c2f136`, p3 `11b326aa595a2daba042c6b5fe59edf704ebd3c6c6d5d2cc11c82cf6f5b9fe94`, p4 `bd8b3cc44b71778e6491c86dfad7781c2a04b7757b509fae6db42abdd42c60a4`, p5 `a4adc4e39500fd0821ead76d6694645eef49e4c0745bef651ff45d4f3b067598`, p6 `2c3d1fbaeac06685205e596d279933453221eb99cf1d03c42b0e13301ab35c0e`, p7 `f4a80672bf861c79160c0ac28e264b569360a3aa54f5d7ffee89b93dab08eb2d`, p8 `c4cf720a4687a520b6f6bffee58622ca0148901234bca4f375e91b0a69b1635e` (round 4 changed only P1, as expected — P2–P8 hashes are unchanged from the round-3 run, confirming build determinism).

## 7. Gates (all measured, final files)
- Freeze baseline: 8/8 byte-identical (see §4). Freeze diff core→edition: added CJK = 0 on every page (p1 +28/−26, p2 +35/−29, p3 +33/−31, p4 +30/−25, p5 +43/−35, p6 +29/−24, p7 +45/−41, p8 +171/−168; counts are multiset occurrences). Removed strings with no CJK, all adjudicated: p6 `bollettino · modello` and p7 `è probabile che / è possibile che / bisogna` are wrapped line fragments of Chinese explanation bridges; p8's 9 (answer lines 17, 18, 19, 20, 60, 61, 85, 86, 103) are note-side changes only — their printed keys are byte-identical, confirmed because `p8.py` does NOT list them as keydiffs.
- P8: `tools/p8.py compare` — **CLEAN 150=150**, missing=[] extra_count=0 uncertain=[]. Keydiff list [6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 137, 138, 139], adjudicated item by item:
  - Bracket-branch artifacts (11): 6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77 — the extractor's paren branch takes everything before the note's parenthesised plural/gender marker as the pseudo-key (e.g. core pseudo-key `previsioni — previsioni = 预报` vs edition `previsioni — previsioni = prévisions`); the TRUE printed keys, i.e. the text before ` — ` in each segment, are byte-identical: previsioni, guanti, crisantemi, termosifoni, fa, resta, mandorle, più bella, gratuiti, castagne, ci sarà.
  - True redirections (3, legal per the W43 IT × FR ruling): 137 key `周一第一场寒冷来了。` → `Lundi, le premier froid arrive.`; 138 `观众可以免费品尝。` → `Le public peut déguster gratuitement.`; 139 `周日晚上，佛罗伦萨对尤文图斯。` → `Dimanche soir, on joue Fiorentina–Juventus.` Item 140's Italian key is byte-identical (FR→IT direction).
  - P8 printed-note set equality: EXTRA_ONLY not needed — sets are exactly equal.
  - P8 notes are entirely French (one-line notes); the only non-French note content is language-neutral arithmetic (85 `12 − 9 = 3` → French wording `12 moins 9 = 3`, as in the IT × EN precedent).
- Geometric occlusion audit (`tools/occlusion_audit.py`, selftest OK — all 6 planted classes fired, clean controls silent): edition **0 flags**, core **0 flags**, NEW vs core **0**.
- Same-baseline row check (supplementary scan, `scans.py`): 0 same-baseline collisions on furniture bands (P1 top band + footers).
- Right-edge ADVANCE scan (supplementary): 4 flags > 1885, ALL frozen Italian strings, ALL byte-identical to the core's own scan (same strings, same advances): P1 parola lines (1889.3 / 1888.8), P2 option `b. il calorifero di casa, che si accende` (1902.5), P8 writing-topic line (1898.6). None crosses the page edge (1950), none crosses a drawn box border, and the canonical true-ink audit reports 0 EDGE flags — these are advance-width measurement tolerance on frozen text, not edition defects. The P8 flag's y-shift vs core (662.8 vs 633.1) is the French E-item body wrapping one extra line inside P8-ex slack (ends 965, bottom 1332).
- P6 chart-label coverage, baseline-anchored ink method (PIL getbbox, anchor `ls`, vs later-drawn rects): max **0%** (gate <30%). All chart labels (Torino 3°, Milano 4°, Bologna 5°, Roma 9°, Napoli 12°) fully visible on the P6 card.
- Gloss counts (rendered gloss() strings split on `·`): per box 6/5/4/4/5, total **24 = 24** vs core, headwords identical in every item.
- P7 golden sentences: all 8 occur exactly 2× in the joined SVG text (case-sensitive quote form).
- Readers' corner: see §5 (3 disclosure facts + imperative invitation + VOL.3 promise, Italian original + French equivalent, both on the page).
- Visual check: all 8 rendered PNGs in cards/ inspected (overflow, overlap, footer clearance, badge, edition line, fixture table, chart + caption, P8 answers bottom vs footer, parola box border clearance after fix round 3). No defects remain.

## 8. W43 deviations (same pairing, W43 → W45)
- Badge geometry: W43 replaced the tagline slot (y=372, 20pt); W45 inserts at y=574, 22pt BRICK — forced by the W45 core (y=372 is frozen Italian strapline `IL GIORNALE SETTIMANALE PER IMPARARE — …`), following the W45 IT × EN precedent and tools README #20's FR/IT family case. Badge STRING is byte-identical to W43.
- Edition line: W43 JOURNAL variant kept; VOL.1 → VOL.2 (core VOL).
- Footer: W43 HEBDOMADAIRE form kept; VOL.1 → VOL.2.
- Gloss prefix `Note — `, P8 separators `— PAGINA n —`, dash-style P8 answers, instruction-label set: identical to W43.
- Letter disclosure: W43 promised VOL.2; W45 promises VOL.3 (core's next volume).
- P7 word: W43 `anteprima`; W45 `l'assaggio` (core's word).
- Exercise counts: W43 150, A2 46 / B1 71 / B2 33; W45 150, A2 47 / B1 70 / B2 33 (core difference — one badge reclassified in the core's fix round 1, see core KIT §10).
- P8 geometry: W45 core's moved exercise/answer split (exercises flow bottom 1332, RISPOSTE rule 1344, answer titles 1382, answers flow start 1408, answers font 13pt) is inherited from the core, not changed by this edition.
- P1 parola gloss: W43's one-line gloss precedent (line-strike fix) re-applied in W45 as a 2-line descender-free gloss (fix round 3) because the W45 parola box geometry differs.

## 9. Fix rounds (all edits live in transform.py; each round re-ran from a fresh core copy)
- Round 1 (P1-headline overflow + P7 col3 1789.5 + box-title crossings): P1 bridge 4→3 lines; cifre #2 4→3 and #4 3→2 lines; CIFRE box title tsize 23→20 (W43 precedent, ink 446.8→~388px); diary subtitle → `Semaine · Cosa succede, giorno per giorno` (387.8px ≤ 412px slot); settimana French footer note → `Dates selon les calendriers ; horaires modifiables.` (377.5px ≤ 412px slot); P1 parola gloss 2→1 line (row-B rule at 1864, IT × EN precedent); P7 errori #2 2→1 line; parola gloss 3→2 lines; letter note 5→3 lines (core count) keeping all 3 disclosure facts + imperative + VOL.3 promise. Result: P1 overflow gone, P7 col3 1673.0.
- Round 2 (P8-keys overflow, 7 items past footer): 14 wording-only P8 note trims, each verified 2→1 wrapped lines at 13pt/width 434 (items 3, 22, 122, 24, 41, 50, 56, 57, 58, 83, 84, 87, 90, 135); items 138/139 deliberately left at 2 lines (minimal re-aimed keys/notes). Result: P8-keys ends y=2514, warnings 0.
- Round 3 (occlusion audit 1 NEW BOXTITLE): P7 parola gloss second line's Latin descenders grazed the box border by 0.5px (pixel-confirmed on the P7 card); reworded to `assaggio = dégustation. Voir page 3, finale du Panettone.` — verified wrap puts descender-free `du Panettone.` on line 2, same 2-line geometry, col3 still 1673.0. Result: audit 0/0/0.
- Round 4 (W43 furniture byte-fidelity): badge apostrophe U+2019 → ASCII `'` to match the shipped W43 badge byte-for-byte. Result: badge byte-identical; all gates re-run green.

## 10. Delivery
- NOT pushed to git, NOT posted to Discord, NO messages sent (per task). Delivery to the LucernaRead/weekly repo is the main line's job, after the independent proofread passes.
- Files: files/weekly-report-w45-it-fr/ (svg/ 8 SVGs, cards/ 8 PNGs, La-Lucerna-VOL2-FR.pdf, La-Lucerna-VOL2-FR-web.pdf, WEEKLY-KIT.md, ABSTRACT.txt).

## 11. Open gate
**Independent proofread has NOT run — marked PENDING.** No GitHub repo insert and no Discord post were made (parent handles both after the proofread passes).
