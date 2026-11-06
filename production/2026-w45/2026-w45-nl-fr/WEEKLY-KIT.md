# WEEKLY KIT — De Lucerna, VOL.2 (Nederlands × Français, W45)

## 1. Spec

- **Issue week:** Monday 2 November – Sunday 8 November 2026; issue dated Monday 2 November 2026.
- **Volume:** VOL.2 for Nederlands (sequel to W43 VOL.1).
- **Pairing:** target language **Dutch** × reader native language **French** (matrix cell NL × FR).
- **Masthead:** De Lucerna (article De, per the Dutch convention).
- **Format:** 8 pages (multiple of 4), page size 1950 × 2700, 4 columns, warm ivory paper, dark olive-green accents.
- **Relation to the core:** built from `files/weekly-report-w45-nl-core/` (VOL.2, masthead De Lucerna). The Dutch core — articles, exercises, images, facts, answer keys — is frozen and identical; only the explanation layer was rewritten, into French. No Discord post, no chat card/PDF dump, no cron, no weekly-git touch, no core/W43 modification (core and W43 dirs read-only throughout; core SVGs re-hashed 8/8 unchanged at the end).
- **Lead topic:** «Nederland in de Klimaatweek» — the national Klimaatweek (2–8 Nov), Museumnacht Amsterdam (7 Nov), Crossing Border Festival (3–8 Nov), Eredivisie matchday 12 (6–8 Nov). Facts, trend sources and verification debts are inherited unchanged from the core KIT §4.

## 2. Content per page (identical structure to the core; only the explanation layer differs)

- **P1 — Voorpagina (A2, 10 ex.):** headline «Nederland in de Klimaatweek: bomen, musea en voetbal»; week agenda; numbers box; word of the week «het klimaat»; photo herfstbos; IN HET KORT box; lightning quiz (7–10).
- **P2 — Leven (A2, 18 ex.):** «De Klimaatweek: wat kun jij doen?» — Coevorden giveaway, energy saving, KNMI colour codes; photo kinderdijk; WIST JE DAT facts; EN JIJ box (best entries to VOL.3).
- **P3 — Cultuur (A2→B1, 18 ex.):** «Amsterdam blijft wakker: de Museumnacht» — Museumnacht, Crossing Border, PAN Amsterdam, Mega Snuffelmarkt; photo gracht.
- **P4 — Sport (B1, 18 ex.):** «Europa: drie keer feest, twee keer verlies» — verified European results, matchday-10 results, standings after 10 rounds, full matchday-12 programme; photo elftal1912.
- **P5 — Jongeren (B1, 18 ex.):** «Expeditie Robinson is begonnen!» — Robinson premiere follow-up, ADE (30 years) and DDW closings, youth climate actions; no photo on this page.
- **P6 — Verdieping (B2, 18 ex.):** «Geel, oranje, rood: hoe werken de codes?» — KNMI local-warning deep read, pro/contra local warnings, program-drawn chart explicitly labeled OEFENDATA (practice data, not a real survey: 100 jongeren — thuis 45, eerst tekst 25, toch naar buiten 20, weet niet 10).
- **P7 — Taal (A2/B1/B2, 12 ex.):** A2 klimaatwoorden; B1 scheidbare werkwoorden; B2 mening geven; PAS OP clinic (4 items); word «meedoen» (definition frozen verbatim, see §6); readers' corner (editor's example + disclosure + invitation, see §7); 8 golden sentences; VOL.3 preview (Sinterklaas 15 Nov, Sint-Maarten 11 Nov, letters + best P8 texts).
- **P8 — Toets en antwoorden (38 ex.):** A kroniek (8), B algemene vragen (8), C lees en antwoord (4, Daan/Coevorden text), D maak de zinnen (4), E vertaal (4, re-aimed — see §5), F woorden match (4), G dialoog bij de bomen (5), H schrijf zelf (1); all 150 answers with French notes in dash style.

## 3. Measured exercise counts (registry output, identical to the core KIT §3)

- **Total: 150 exercises.** By page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- By level: A2 47, B1 72, B2 31.
- By type (registry labels kept core-identical per the W43 NL × FR precedent — types are never printed; only the printed instruction words were localised): 完成句子 65, 单选 44, 词汇配对 8, 判断对错 7, 造句 8, 完形单选 13, 翻译 4, 写作 1.
- Model essay (P8 H, ex. 150): **87 words** (requirement 80–100).
- Numbering continuous 1–150; P8 printed answers verified against the registry (p8.py extract: noted set = 150 of 150).

## 4. Gates — measured values (all builder-run; logs in hidden_files/weekly-report-w45-nl-fr-build/)

- **Pages:** 8 (multiple of 4). SVGs 8, cards 8 at 1950×2700, print PDF 8 pages, web PDF 8 pages.
- **Core freeze:** `tools/freeze.py baseline` on the unmodified build copy reproduced the core **8/8 byte-identical** (tools venv) and re-hashed the shipped core unchanged; `freeze.py diff` core-vs-edition: added CJK characters **0 on every page**, edition CJK **0** (core CJK counts per page 191 / 212 / 153 / 126 / 214 / 192 / 373 / 1033 → edition 0). Every changed string belongs to the explanation layer, page furniture, the masthead badge/footers, or the re-aimed translation items (§5); no Dutch article, exercise body, option, fact or figure differs.
- **P8 printed-note set:** `tools/p8.py compare` (explicit P8 paths, total 150): core 150 noted, edition 150 noted, status **CLEAN**, missing [] extra 0 uncertain []. Keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148] — adjudicated in §5; no key is missing, no extra key, no SHORT.
- **Geometric occlusion audit:** `tools/occlusion_audit.py` (selftest OK): edition **0 flags**, core **0 flags**, NEW vs core **0** (final render, after fix rounds §9).
- **Supplementary scans (build/rowcheck.py):** same-baseline text-ink collisions: exactly **1** site — P1 contents row «Musea bij nacht en boeken» vs level «A2→B1», 1.0 px bbox touch at y=1436, **identical in the core** (frozen Dutch row, same geometry); visually separated on the card, no overprint — adjudicated inherited, not a defect. P6 chart-label ink vs later-drawn bars: **0.0% coverage** on all 8 labels/values (below the 30% threshold). P1 word-gloss vs the full-width rule at y=1853: line 1 ink 1829.3–1851.3, line 2 ink 1855.9–1875.9 — the rule passes through the inter-line gap touching neither, the same adjudicated geometry as W43 NL × FR.
- **Gloss counts (split on · in the gloss() strings themselves, README #21):** P2 6 = 6, P3 5 = 5, P4 5 = 5, P5 5 = 5, P6 5 = 5 — core 1:1 in every box. P7 bridges: A2 4, B1 3, B2 3 items, unchanged in count.
- **P7 golden sentences:** all 8 Dutch sentences occur exactly **2×** (source article page + P7), verbatim, with page tags identical to the core: Pagina 1, 1, 2, 3, 4, 5, 6, 6. Each sentence was confirmed on its tagged article page (P1 ×2, P2, P3, P4, P5, P6 ×2). P7 phrases are verbatim from this issue's articles with correct page tags.
- **P7 word-box definition freeze (§6):** the core's Dutch definition sentence is retained verbatim (see §6).
- **Readers' corner (§7):** no reader, letter, name or quote invented; the only letter on the page is the labeled editor's example, with all three facts and an explicit French public invitation on the page.
- **Images:** only clearly public-domain/CC0 images, reused byte-identical from the core build assets (assets diff clean): P1 herfstbos, P2 kinderdijk, P3 gracht, P4 elftal1912. Every credited image is typeset on its page (1 `<image>` element per photo page; P5/P6/P7/P8 carry no photo, as in the core).
- **Image credits (from the Commons API Artist field, per the core KIT §5 / W43 CREDITS.md):** P1 Foto: Vovogov90 — CC0; P2 Foto: Nationaal Archief — CC0; P3 Foto: W. Punt / Anefo, Nationaal Archief — CC0; P4 Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein. All four credit lines verified present in the rendered SVGs (P4's credit wraps over two text nodes, «publiek» / «domein», identical to the core).
- **Banned-string scan (all 8 SVGs):** the banned intermediary term 0, spaced guillemets (« / ») 0, double spaces 0, CJK characters 0.
- **Footers:** 8/8 carry «De Lucerna · HEBDOMADAIRE NÉERLANDAIS VOL.2 · TEXTE EN NÉERLANDAIS · EXPLICATIONS EN FRANÇAIS» with «Page n sur 8» (n = 1–8).
- **Build warnings:** final render log shows **zero FLOW OVERFLOW / HEAD TOO WIDE** warnings.
- **Visual inspection:** all 8 rendered PNG cards viewed page by page: clean, no overlaps, no cut-off text, no defects (including the P1 badge row, the P1 word-note/rule gap, the P2 code boxes and match set, the P6 chart, the P7 col-3 stack and the P8 key block foot).

## 5. What changed vs the core — and what did not

Rewritten into French (the whole explanation layer): every word gloss («Note — …» boxes, W43 measured form), every section instruction, the error-clinic notes, the readers'-corner notes, the teaser apparatus, the phrases-of-the-week translations, all 150 answer notes, all bilingual page headers and subtitles, the P1 numbers-box parentheticals, the P2 code-box labels, the P6 chart caption's second line, the readers' prompts (EN JIJ boxes), and the P8 answer-key header lines.

Unchanged: all Dutch articles, headlines, exercise bodies and options, all facts and figures, all images and credits, the chart geometry and values, and the answer keys except §5 items.

### P8 keydiff adjudication (compare output keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148])

- **Genuine re-aims (translation items, as in the W43 NL × FR precedent): 137, 138.** Exercises 137–138 keep their Dutch source sentences and are now translated **into French** (137 «La Semaine du climat dure sept jours.», 138 «Le code orange signifie : préparez-vous.»). Exercises 139–140 swap direction — the printed source is now French and the key is the Dutch sentence, byte-identical to the core's keys (139 «Museumnacht duurt van 19:00 uur tot 02:00 uur.», 140 «Ik doe mee aan de Klimaatweek.»); 139/140 are therefore NOT in the keydiff, and 150's printed line is the translated writing-task pointer (apparatus) with the 87-word Dutch model text byte-identical.
- **Extraction artifacts, not key changes: 7, 17, 70, 71, 76, 96, 148.** For these seven, the printed answer token before the dash is byte-identical to the core (7 B, 17 wortelen, 70 eiland, 71 proef, 76 gaat winnen, 96 advies, 148 B); only the translated note differs. p8.py's key field absorbs the note difference — the same artifact family as README #13 and the W45 NL × EN sibling's identical keydiff list. Verified against the printed P8 lines in both SVGs, not just the tool output. No P8 note contains a parenthesis, per the task's key-candidate rule (notes use commas and colons instead of parentheticals).

### Layout adjudications (apparatus only — the Dutch core was never touched)

1. **P8 answer-key typography** follows the W43 NL × FR measured values: key lines at **13.0 pt / 1.12 leading / 0.4 gap** (core: 13.5 pt / 1.16 / 0.5), separator unchanged (14 pt / 1.16, gap 2), flow bottom 2552. French notes are longer than the Chinese notes they replace; final keys flow ends y = 2339, clear of the footer rule.
2. **P2 exercise spacing:** P2 exercise gaps 8 → 4, section-head gaps → 4 and match-set gap → 8 (P2 only; the W45 NL × EN sibling used 8 → 4 / 13 → 8). French bridges wrap to two lines where the Chinese bridges took one; without this the P2 exercise flow overflowed (first-render overflow, match set short by 39 px). Final P2 exercise flow ends y = 2392 (bottom 2580). P2 col-3 ends 1449.1 (codes rule at 1554).
3. **P7 column-3 stack:** clinic notes, word gloss, disclosure and invitation were kept telegraphic (W43 NL × FR precedent: short clinic notes; W45 NL × EN precedent: shortened col-3 stack) so the three-box stack ends at y = 1926, clear of the phrases rule at 1937 (11 px slack; formula includes the core's measured +50 correction, verified against the rendered box). No Dutch text, quote or preview text changed.
4. **P1 agenda subtitle** shortened per the first-render occlusion flag: «Agenda van de week · LES RENDEZ-VOUS» (the longer «LES GRANDS RENDEZ-VOUS» form crossed the agenda box border at 1924.5 > 1885).
5. **Match instruction** shortened in both places it is printed (P2 match set, P8 F match set): «Associez les paires» — the full «Associez chaque mot à sa définition» form overflowed the page edge on P2 (ink to 1970.25 > 1950) and overlapped the P8 model text.
6. **P1 word gloss guillemets** tightened to «Le climat» (no inner spaces) so the whole edition passes the core's spaced-guillemet scan uniformly; the W43 NL × FR word gloss used French-spaced guillemets, but the tight form changes no wrap (same two lines) and matches every other quote in this paper.
7. **P6 chart title** shortened to «DE GRAFIEK · DONNÉES D'ESSAI» (371.2 px; the full «DONNÉES D'EXERCICE» form measured 435.8 px against the 412 px box inner edge). The OEFENDATA label stays in the Dutch caption («OEFENDATA — verzonnen cijfers…») and the French caption («Données d'exercice : chiffres inventés…»).
8. **P1 subtitle kept at 40 pt** (measured 1766.8 px ≤ 1820 px inner width) — unlike W43, which had to drop to 36 pt for its longer subtitle string; all Dutch theme words (KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12) retained.
9. **P5 watch-box parentheticals** use French half-width parentheses with a preceding space (W43 §5 rule), trimmed so box line counts stay near the core's (2 / 3 / 3 / 3 lines vs core 2 / 3 / 2 / 2).

## 6. P7 word-box definition freeze — measured retention

The core's target-language definition sentence in the P7 HET WOORD box is retained **verbatim**, with only the French gloss line below it localised:

- Frozen Dutch definition (byte-identical in the rendered P7 SVG): ««meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.»
- French gloss line (localised): «meedoen = participer.»
- The same freeze was applied to the PAS OP clinic: all Dutch wrong/right sentences verbatim; only the third line (the note) was translated into French.

## 7. Readers' corner — honest note

No real reader letter exists for this issue. P7 prints a **clearly labeled editor's example** («Li (voorbeeldbrief van de redactie)», Dutch example letter text kept verbatim from the core — the W43 NL × FR precedent localised the example signature to Camille/Parijs, but this W45 edition keeps the core's frozen example unchanged under the no-fabrication gate; no new name was invented) plus the Dutch disclosure kept verbatim («Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.») and a French disclosure. All three facts are on the page, in Dutch and in French: (1) no real letters had arrived at press time, (2) no best page-8 texts had arrived, (3) the example stands with the promise carried to VOL.3. The explicit French public invitation, verbatim:

> Exemple de la rédaction. Envoyez vos vraies lettres et textes de page 8 : nous les publierons dans le VOL.3 !

(Imperative + publication promise; the contents-preview line and other pages' exercise prompts are not counted as the invitation.) No reader, letter, name or quote was invented for this edition.

## 8. Furniture — measured attributes and W43 comparison

W43 shipped `files/weekly-report-nl-fr/` measured from its SVGs (task rule: W43 measured beats README #20's generic text; tables.json FR column confirms badge/footer/page-line/gloss-prefix). Every value below was re-measured on the W43 shipped SVGs and on this edition's SVGs:

- **Pairing badge (P1 masthead, W43 family case):** «TEXTES EN NÉERLANDAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES», centered x = 975, **y = 568**, 20 pt, bold, BRICK #a4553a, Noto Sans CJK SC; measured width 1058.8 px (fits the 1820 px inner width). **Family case (README #20):** the NL core family keeps its Dutch strapline at y = 372 verbatim AND inserts the badge at y = 568 between the dark band (ends 542) and the headline (starts 580) — this is the W43 NL × FR / NL × DE geometry, NOT the W45 NL × EN strapline replacement at y = 372. Frozen elements below y = 606 unmoved.
- **Masthead strapline (kept verbatim):** «DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS», y = 372, 19 pt, grey.
- **P1 subtitle (y = 330, 40 pt serif bold, centered):** «JOURNAL NÉERLANDAIS · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12» (1766.8 px; W43 used the JOURNAL variant at 36 pt for its longer string — see §5 item 8).
- **Top strip centre (y = 92, 21 pt):** «ELKE WEEK IN HET NEDERLANDS · CHAQUE SEMAINE EN NÉERLANDAIS» (704.1 px, W43 string verbatim). Left «VOL. 2»; right week dates in Dutch, unchanged.
- **Band right notes (P1):** «SEMAINE DU CLIMAT» / «Tout le pays participe · voir page 2» (W43 pattern: French right notes).
- **Footer (all pages):** «De Lucerna · HEBDOMADAIRE NÉERLANDAIS VOL.2 · TEXTE EN NÉERLANDAIS · EXPLICATIONS EN FRANÇAIS» (20 pt sans, grey, baseline 2624, footer rule y = 2580) with «Page n sur 8» right-aligned — the W43 form with VOL.1 → VOL.2.
- **Gloss prefix:** «Note — » (W43 shipped gloss boxes; README #4's «Note | » note concerns an early EN × FR variant, not this family). P1 bridge prefix: «Notes — ».
- **Page headers:** Dutch + French throughout (e.g. «LEVEN · VIE», «CULTUUR · CULTURE», «JONGEREN · JEUNESSE», «VERDIEPING · APPROFONDISSEMENT», «TAAL · LANGUE», «TOETS EN ANTWOORDEN · TEST ET RÉPONSES»; «SPORT» is the same word in both languages, as in W43). Band sub-lines give the Dutch description followed by the French one. Section heads follow the W43 short forms («OEFENINGEN · EXERCICES», «Réponses page 8 · exercices mélangés par niveau, cherchez par numéro», «DE WEEK IN CIJFERS · CHIFFRES», «ZO ONTHOUD JE HET · ASTUCE», «EN JIJ? · ET TOI ?», «BLIKSEMQUIZ · QUIZ ÉCLAIR», «PAS OP! · PIÈGES FRÉQUENTS» (348.2 px), «HET WOORD · MOT DE LA SEMAINE», «ZINNEN VAN DE WEEK · PHRASES DE LA SEMAINE (MOT POUR MOT, DE CETTE ÉDITION)» (1149.0 px), «VOLGENDE WEEK · LA SEMAINE PROCHAINE (VOL.3)», «ANTWOORDEN · RÉPONSES — classées par page, trouvez votre numéro»).
- **P8 separator:** «— PAGINA {n} —» kept from the core (as in W43).
- **Instruction words (printed):** Compléter (fill) · Associez les paires (match) · Vrai ou faux (judge) · Former la phrase (make sentence) · Traduire (translate) · Écrire (write).

## 9. Toolchain

- **run.py interpreter:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0 (same venv that reproduced the core baseline 8/8 byte-identical; system python3 is also 3.12.3 but ships Pillow 10.2.0 and no cairosvg, so it was NOT used).
- **render.py (CairoSVG) interpreter:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1 (system python3 lacks cairosvg, as the task states).
- **Pipeline:** one-process run.py (content12 → 34 → 56 → 7 → 8, so the exercise registry accumulates — never run modules standalone, never import them inside the core build dir, per README #11) → render.py (SVG → 1950×2700 PNG cards → print PDF via cairosvg+pypdf → web PDF JPEG q85 @1400 px).
- **Transform record:** build/transform.py (line-literal replacements with counts, plus the width fixes of §5) maps the core build to this build; build/rowcheck.py holds the supplementary scans. The core build directory was copied, never modified; repointing covered every OUT spelling (expanduser form) in content12/34/56/7/8 and render.py, verified by grep (no reference to weekly-report-w45-nl-core remains in the build code).

## 10. Build rounds

1. **First render:** counts exact (150; levels/pages as §3), but P2 exercise flow overflowed (match set short 39 px) and content7 crashed on an un-renamed dt_zh reference in the readers'-corner paragraph (definition and wrap call had been renamed to dt_fr; the para call had not) — fixed per §5 item 2 and the dt rename completion.
2. **Fix 1:** zero build warnings; P2 ends 2392, P7 col-3 ends 1926, P8 keys end 2339 — but occlusion audit flagged 3 NEW defects (P1 agenda subtitle box overflow; P2 match instruction past the page edge; P8 match instruction overlapping the model text) — fixed per §5 items 4–5. Pre-fix hashes recorded in build/fix1-baseline-sha256.txt before the re-render.
3. **Fix 2:** P1 word-gloss guillemets tightened (§5 item 6); occlusion re-read 0 / 0 / NEW 0. Pre-fix hashes recorded in build/fix2-baseline-sha256.txt before the re-render.
- **Fix-round baselines:** pre-fix sha256 of the edition's SVG/cards/PDFs written to build/fix0-baseline-sha256.txt (first render), fix1-baseline-sha256.txt and fix2-baseline-sha256.txt before each re-render round, per the fix-round baseline rule.

## 11. Delivery note

- This edition is delivered as files only (builder-complete, NOT finalized — finalization needs the independent proofread gate). NOT pushed to git, NOT posted to Discord, NOT messaged anywhere (per task instruction).
- Files: `files/weekly-report-w45-nl-fr/` — `svg/` (8 SVGs), `cards/` (8 PNGs, 1950×2700), `De-Lucerna-VOL2-FR.pdf` (print PDF, 8 pages), `De-Lucerna-VOL2-FR-web.pdf` (web PDF, 8 pages, under the 10 MB limit), `WEEKLY-KIT.md`, `ABSTRACT.txt`.
- Build tree: `hidden_files/weekly-report-w45-nl-fr-build/` — build code (bslib4/content*/svglib/run/render), transform.py + transform-log.txt, rowcheck.py + rowcheck.txt + rowcheck-final.txt, build logs (build-log.txt, build-log-fix1.txt, build-log-fix2.txt), freeze-diff.txt/json + freeze-diff-final.txt, p8-core.txt, p8-ed.txt, p8-compare.txt + p8-compare-final.txt, occlusion-edition.txt + occlusion-edition-fix1.txt, occlusion-core.txt, occlusion-new.txt + occlusion-new-fix1.txt, core-sha256-before.txt, fix0/fix1/fix2-baseline-sha256.txt.

## 12. Deliverable sizes and hashes (final render)

- `De-Lucerna-VOL2-FR.pdf` — 7,939,994 bytes, sha256 b3368d87d897977b089dbdda2ade9b9951a27aacf3f2421422169e1d999be4b1
- `De-Lucerna-VOL2-FR-web.pdf` — 3,679,467 bytes, sha256 db2423c9265b923103d38b34d6bbe7a307b368d7c902888e3a03feb707e49439
- SVGs (sha256): p1-voorpagina 2743f8057a862732df7e352751c887c27b80cae1c93f102641872cf46ef16d71; p2-leven 756fbcf0a94790bdc3cf17868ecf35ab363023c65994254284122b3c7bdef9b4; p3-cultuur b04e2212c6d1ee94a7440613621d3268225273990325560a1943cb84749e9e87; p4-sport 09f32ccef15c8adc59a69d251ed926a2fc8a7437c633723a5e25503c4b33d112; p5-jongeren 43ad9c4d9bffbe3e2e931fc487019349a1e605da84c82f6eb1dc2241495c7556; p6-verdieping e93982ba33e3c66d93ace28c902fcffcee70d6e8177fb224794cd42b73903c5f; p7-taal 68726be3db9f990d9825a9cbef0dcf422b4bf665e2747d0155e97e4250a76e68; p8-toets 98fad8e5bdd5d82b48813e92997d2a0c01b1135b680a02ee6a56893a393d4619
- Cards (sha256): p1 24caf12f9b4ab55b6a25d8fba91aae205b98c2f313c33408fd07c986a49e5fad; p2 b0ad99e575749696b62251793f28864c230b6a3a01be7cfd62bec9e0f72f5852; p3 fd5723450c70d12d31e26b3dab38f83244abd65aff1fa7e5698e7127b1a7e708; p4 e2f7e7a283557f8cca36e4fb251653351c8eaaf60dcb91116806f24cd0977e37; p5 a8ddafe2593a030dc04e98e1243cbca69caab306acdf60e72195f14b7a1df36c; p6 d3c33832e604a3adf4bfb784f2c4797608dcfe3c2dee9fa537f16902a928f6b3; p7 c7b52ffe63aec459a6716291202baca34d8abb5d05c5e47fd85dec06953c0f1b; p8 717b4e0444a66a33d9fc32489719d96ba819a768c037728610c14a37fda36697
