# WEEKLY KIT — De Lucerna, VOL.2 (Nederlands × English, W45)

## 1. Spec

- **Issue week:** Monday 2 November – Sunday 8 November 2026; issue dated Monday 2 November 2026.
- **Volume:** VOL.2 for Nederlands (sequel to W43 VOL.1).
- **Pairing:** target language **Dutch** × reader native language **English** (matrix cell NL × EN).
- **Masthead:** De Lucerna (article De, per the Dutch convention).
- **Format:** 8 pages (multiple of 4), page size 1950 × 2700, 4 columns, warm ivory paper, dark olive-green accents.
- **Relation to the core:** built from `files/weekly-report-w45-nl-core/` (VOL.2, masthead De Lucerna). The Dutch core — articles, exercises, images, facts, answer keys — is frozen and identical; only the explanation layer was rewritten, into English. No Discord post, no chat card/PDF dump, no cron, no weekly-git touch, no core/W43 modification (core and W43 dirs read-only throughout; core SVGs re-hashed 8/8 unchanged at the end).
- **Lead topic:** «Nederland in de Klimaatweek» — the national Klimaatweek (2–8 Nov), Museumnacht Amsterdam (7 Nov), Crossing Border Festival (3–8 Nov), Eredivisie matchday 12 (6–8 Nov). Facts, trend sources and verification debts are inherited unchanged from the core KIT §4.

## 2. Content per page (identical structure to the core; only the explanation layer differs)

- **P1 — Voorpagina (A2, 10 ex.):** headline «Nederland in de Klimaatweek: bomen, musea en voetbal»; week agenda; numbers box; word of the week «het klimaat»; photo herfstbos; IN HET KORT box; lightning quiz (7–10).
- **P2 — Leven (A2, 18 ex.):** «De Klimaatweek: wat kun jij doen?» — Coevorden giveaway, energy saving, KNMI colour codes; photo kinderdijk; WIST JE DAT facts; EN JIJ box (best entries to VOL.3).
- **P3 — Cultuur (A2→B1, 18 ex.):** «Amsterdam blijft wakker: de Museumnacht» — Museumnacht, Crossing Border, PAN Amsterdam, Mega Snuffelmarkt; photo gracht.
- **P4 — Sport (B1, 18 ex.):** «Europa: drie keer feest, twee keer verlies» — verified European results, matchday-10 results, standings after 10 rounds, full matchday-12 programme; photo elftal1912.
- **P5 — Jongeren (B1, 18 ex.):** «Expeditie Robinson is begonnen!» — Robinson premiere follow-up, ADE (30 years) and DDW closings, youth climate actions; no photo on this page.
- **P6 — Verdieping (B2, 18 ex.):** «Geel, oranje, rood: hoe werken de codes?» — KNMI local-warning deep read, pro/contra local warnings, program-drawn chart explicitly labeled OEFENDATA (practice data, not a real survey: 100 jongeren — thuis 45, eerst tekst 25, toch naar buiten 20, weet niet 10).
- **P7 — Taal (A2/B1/B2, 12 ex.):** A2 klimaatwoorden; B1 scheidbare werkwoorden; B2 mening geven; PAS OP clinic (4 items); word «meedoen»; readers' corner (editor's example + invitation, see §6); 8 golden sentences; VOL.3 preview (Sinterklaas 15 Nov, Sint-Maarten 11 Nov, letters + best P8 texts).
- **P8 — Toets en antwoorden (38 ex.):** A kroniek (8), B algemene vragen (8), C lees en antwoord (4, Daan/Coevorden text), D maak de zinnen (4), E vertaal (4, re-aimed — see §5), F woorden match (4), G dialoog bij de bomen (5), H schrijf zelf (1); all 150 answers with English notes in dash style.

## 3. Measured exercise counts (registry output, identical to the core KIT §3)

- **Total: 150 exercises.** By page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- By level: A2 47, B1 72, B2 31.
- By type (English registry labels): complete 65, choice 44, matching 8, true or false 7, make sentences 8, cloze choice 13, translate 4, writing 1.
- Model essay (P8 H, ex. 150): **87 words** (requirement 80–100).
- Numbering continuous 1–150; P8 printed answers verified against the registry (p8.py extract: noted set = 150 of 150).

## 4. Gates — measured values (all builder-run; logs in hidden_files/weekly-report-w45-nl-en-build/)

- **Pages:** 8 (multiple of 4). SVGs 8, cards 8 at 1950×2700, print PDF 8 pages, web PDF 8 pages.
- **Core freeze:** `tools/freeze.py baseline` on the W45 NL core build reproduced the core **8/8 byte-identical** (tools venv) and re-hashed the shipped core unchanged; `freeze.py diff` core-vs-edition: added CJK characters **0 on every page**, edition CJK **0** (core CJK counts per page 191 / 212 / 153 / 126 / 214 / 192 / 373 / 1033 → edition 0). Every changed string belongs to the explanation layer, page furniture, the masthead badge/footers, or the re-aimed translation items (§5); no Dutch article, exercise body, option, fact or figure differs.
- **P8 printed-note set:** `tools/p8.py compare` (explicit P8 paths, total 150): core 150 noted, edition 150 noted, status **CLEAN**, missing [] extra 0 uncertain []. Keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148] — adjudicated in §5; no key is missing, no extra key, no SHORT.
- **Geometric occlusion audit:** `tools/occlusion_audit.py` (selftest OK): edition **0 flags**, core **0 flags**, NEW vs core **0**. Supplementary scans (build/rowcheck.py): same-baseline text-ink collisions **CLEAN on all 8 pages**; P6 chart-label ink vs later-drawn rects **0.0% coverage** (below the 30% threshold; an early 78.3% reading was a scan bug — PIL getbbox is ascender-relative, not baseline-relative — fixed by using getmetrics, and the canonical audit independently reads 0).
- **Gloss counts (split on · in the rendered gloss strings):** P2 6 = 6, P3 5 = 5, P4 5 = 5, P5 5 = 5, P6 5 = 5 — core 1:1 in every box. P1 bridge 4 items, P7 bridges 4 / 3 / 3 items, unchanged in count.
- **P7 golden sentences:** all 8 Dutch sentences occur exactly **2×** (source article page + P7), verbatim, with page tags identical to the core: Pagina 1, 1, 2, 3, 4, 5, 6, 6. Each sentence was confirmed on its tagged article page (P1 ×2, P2, P3, P4, P5, P6 ×2).
- **Readers' corner (§6):** no reader, letter, name or quote invented; the only letter on the page is the labeled editor's example.
- **Images:** only clearly public-domain/CC0 images, reused byte-identical from the core build assets (assets diff clean): P1 herfstbos, P2 kinderdijk, P3 gracht, P4 elftal1912. Every credited image is typeset on its page (1 `<image>` element per photo page; P5/P6/P7/P8 carry no photo, as in the core).
- **Image credits (from the Commons API Artist field, per the core KIT §5 / W43 CREDITS.md):** P1 Foto: Vovogov90 — CC0; P2 Foto: Nationaal Archief — CC0; P3 Foto: W. Punt / Anefo, Nationaal Archief — CC0; P4 Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein. All four credit lines verified present in the rendered SVGs.
- **Banned-string scan (all 8 SVGs):** the banned intermediary term 0, spaced guillemets (« / ») 0, double spaces 0, CJK characters 0.
- **Footers:** 8/8 carry «De Lucerna · VOL.2 · Dutch text · English explanations · LUCERNA DUTCH WEEKLY» with «Page n of 8» (n = 1–8).
- **Build warnings:** final render log shows **zero FLOW OVERFLOW / HEAD TOO WIDE** warnings.
- **Visual inspection:** all 8 rendered PNG cards viewed page by page: clean, no overlaps, no cut-off text, no defects (including the fixed P1 agenda/word-note area, the P2 match set, the P6 chart, the P7 col-3 stack and the P8 key block foot).

## 5. What changed vs the core — and what did not

Rewritten into English (the whole explanation layer): every word gloss («Note | …» boxes, W43 measured form), every section instruction, the error-clinic notes, the readers'-corner notes, the teaser apparatus, the phrases-of-the-week translations, all 150 answer notes, all bilingual page headers and subtitles, the P1 numbers-box parentheticals, the P2 code-box labels, the P6 chart caption's second line, the readers' prompts (EN JIJ boxes), and the P8 answer-key header lines.

Unchanged: all Dutch articles, headlines, exercise bodies and options, all facts and figures, all images and credits, the chart geometry and values, and the answer keys except §5 items.

### P8 keydiff adjudication (compare output keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148])

- **Genuine re-aims (translation items, as in the W43 NL × EN precedent): 137, 138.** Exercises 137–138 keep their Dutch source sentences and are now translated **into English** (137 «The Climate Week lasts seven days.», 138 «Code orange means: be prepared.»). Exercises 139–140 swap direction — the printed source is now English and the key is the Dutch sentence, byte-identical to the core's keys (139 «Museumnacht duurt van 19:00 uur tot 02:00 uur.», 140 «Ik doe mee aan de Klimaatweek.»); 139/140 are therefore NOT in the keydiff, and 150's printed line is the translated writing-task pointer (apparatus) with the 87-word Dutch model text byte-identical.
- **Extraction artifacts, not key changes: 7, 17, 70, 71, 76, 96, 148.** For these seven, the printed answer token before the dash is byte-identical to the core (7 B, 17 wortelen, 70 eiland, 71 proef, 76 gaat winnen, 96 advies, 148 B); only the translated note differs. p8.py's paren branch swallows the note into its key field exactly when a note ends in a parenthetical (e.g. «wortelen = to take root (plural subject)», «eiland = island (het)», «zachte = soft (soil)») — the same artifact family as README #13. Verified against the printed P8 lines in both SVGs, not just the tool output.

### Layout adjudications (apparatus only — the Dutch core was never touched)

1. **P8 answer-key typography** follows the W43 NL × EN measured values: key lines at **13.0 pt / 1.14 leading** (core: 13.5 pt / 1.16), separator 13.5 pt / 1.17, flow bottom 2540. English notes are longer than the Chinese notes they replace; at the original size the key block overflowed (3 overflow warnings in the first render). Final lowest key baseline is well clear of the footer rule (keys flow ends y = 2332).
2. **P2 exercise spacing:** P2 exercise gaps 8 → 4 and section-head gaps 13 → 8 (P2 only). English bridges wrap to two lines where the Chinese bridges took one; without this the P2 match set overflowed its region (first-render overflow). Final P2 exercise flow ends y = 2402 (bottom 2580).
3. **P7 column-3 stack:** the English clinic notes, word gloss, disclosure and invitation were shortened to telegraphic form (W43 NL × EN precedent: short clinic notes) so the three-box stack ends at y = 1867, clear of the phrases rule at 1937 (first render ended 2071.5 and collided with the phrases section). No Dutch text, quote or preview text changed.
4. **P1 agenda note** split into two lines («See the articles on pages 2–4» / «for all dates and times.») and the **P1 word-of-the-week English gloss** shortened to two lines (««Climate»: the weather and nature around us, long-term. Climate Week is about our climate.») — the first render flagged both as occlusion defects (box-title overflow; last gloss line covered by the IN HET KORT box). Final audit: 0 flags.
5. **Masthead subtitle** shortened by one theme word per the W43 NL × EN precedent (the full Dutch topic line measured 1958.8 px against the 1820 px inner width): «WEEKBLAD IN HET NEDERLANDS · VOL.2 · KLIMAATWEEK · SPEELRONDE 12» (1581.9 px). MUSEUMNACHT stays in the headline, contents and P3 coverage.
6. **P6 chart title** shortened to «DE GRAFIEK · PRACTICE DATA» (355.5 px; the longer form measured 459.4 px against the 412 px box inner edge). The OEFENDATA label stays in the Dutch caption («OEFENDATA — verzonnen cijfers…») and the English caption («Practice data: invented numbers…»).

## 6. Readers' corner — honest note

No real reader letter exists for this issue. P7 prints a **clearly labeled editor's example** («Li (voorbeeldbrief van de redactie)», Dutch example letter text kept verbatim from the core) plus an on-page disclosure and invitation. All three facts are on the page, in Dutch and in English: (1) no real letters had arrived at press time, (2) no best page-8 texts had arrived, (3) the example stands with the promise carried to VOL.3. The explicit English public invitation, verbatim:

> Editors' example — not real. Send your real letters and best page-8 texts: we will print them in VOL.3!

(Imperative + publication promise; the contents-preview line and other pages' exercise prompts are not counted as the invitation.) The Dutch disclosure is kept verbatim: «Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.» No reader, letter, name or quote was invented for this edition.

## 7. Furniture — measured attributes and W43 comparison

W43 shipped `files/weekly-report-nl-en/` measured from its SVGs (task rule: W43 measured beats README #20's generic text; tables.json has no established EN-native furniture column — `furniture en --target nl` errors — so the shipped W43 NL × EN SVG is the authority):

- **Pairing badge (P1 masthead, replaces the core's Dutch strapline at y = 372):** «TEXT IN DUTCH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS», centered x = 975, y = 372, 20 pt, bold, olive #3e4c2a, Noto Sans CJK SC; measured width 941.8 px (fits the 1820 px inner width). Identical string, size, weight, colour and slot to W43.
- **Footer (all pages):** «De Lucerna · VOL.2 · Dutch text · English explanations · LUCERNA DUTCH WEEKLY» (20 pt sans, grey, baseline 2624, footer rule y = 2580) with «Page n of 8» right-aligned — the W43 form with VOL.1 → VOL.2.
- **Gloss prefix:** «Note | » (W43 shipped gloss boxes, verified in the W43 SVGs; README #4's «Note — » note concerns the EN × FR KIT, not this family).
- **Page headers:** Dutch + English throughout (e.g. «LEVEN · LIFE», «CULTUUR · CULTURE», «JONGEREN · YOUNG PEOPLE», «VERDIEPING · IN DEPTH», «TAAL · LANGUAGE», «TOETS EN ANTWOORDEN · TEST AND ANSWERS»; «SPORT» is the same word in both languages, as in W43). Band sub-lines give the Dutch description followed by the English one. Section heads follow the W43 short forms («OEFENINGEN · EXERCISES ON PAGE N», «Answers on page 8 · levels are mixed; find your number», «DE WEEK IN CIJFERS · IN NUMBERS», «ZO ONTHOUD JE HET · REMEMBER», «EN JIJ? · AND YOU?», «BLIKSEMQUIZ · LIGHTNING QUIZ», «PAS OP! · ERROR CLINIC», «HET WOORD · WORD OF THE WEEK», «ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)», «VOLGENDE WEEK · NEXT WEEK (VOL.3)», «ANTWOORDEN · ANSWER KEY — grouped by page: find your number»).
- **P8 separator:** «— PAGINA {n} —» kept from the core (as in W43).
- **Top strip:** centre «ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH» (W43 string, 21 pt, measured 629.4 px); left «VOL. 2»; right week dates in Dutch, unchanged.
- **Family case (README #20):** the NL core has a native subtitle slot at y = 330 and a Dutch strapline at y = 372; the W43 NL × EN precedent replaces the strapline in place with the badge at y = 372 (20 pt bold olive) and rewrites the subtitle in Dutch — this edition follows that case exactly (no masthead shift, no inserted badge row; frozen elements below y = 606 unmoved).

## 8. Toolchain

- **run.py interpreter:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0 (same venv that reproduced the core baseline 8/8 byte-identical; system python3 is also 3.12.3 but ships Pillow 10.2.0 and no cairosvg, so it was NOT used).
- **render.py (CairoSVG) interpreter:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1 (system python3 lacks cairosvg, as the task states).
- **Pipeline:** one-process run.py (content12 → 34 → 56 → 7 → 8, so the exercise registry accumulates — never run modules standalone, never import them inside the core build dir, per README #11) → render.py (SVG → 1950×2700 PNG cards → print PDF via cairosvg+pypdf → web PDF JPEG q85 @1400 px).
- **Transform record:** build/transform.py (line-literal replacements with counts, plus the width fixes of §5) maps the core build to this build; build/rowcheck.py holds the supplementary scans. The core build directory was copied, never modified; repointing covered every OUT spelling (expanduser form) in content12/34/56/7/8 and render.py, verified by grep (no production output path in the build code points at the core dir; the only core-dir references left are read-only: rowcheck.py reads the core SVGs for gloss comparison, and transform.py holds the old strings as replacement sources).

## 9. Build rounds

1. **First render:** counts exact (150; levels/pages/types as §3), but P2 exercise overflow, P8 key overflow (3 warnings) and P7 col-3 collision (ends 2071.5) — fixed per §5 items 1–3.
2. **Fix 1:** zero build warnings; P2 ends 2402, P7 col-3 ends 1867, P8 keys end 2332 — but occlusion audit flagged 2 NEW P1 defects (agenda note box overflow; word-note line covered) — fixed per §5 item 4.
3. **Fix 2:** zero build warnings; occlusion edition 0 / core 0 / NEW 0; all gates in §4 re-run on the final render.
- **Fix-round baselines:** pre-fix sha256 of the edition's SVG/cards/PDFs written to build/fix1-baseline-sha256.txt before each re-render round, per the fix-round baseline rule.

## 10. Delivery note

- This edition is delivered as files only (builder-complete, NOT finalized — finalization needs the independent proofread gate). NOT pushed to git, NOT posted to Discord, NOT messaged anywhere (per task instruction).
- Files: `files/weekly-report-w45-nl-en/` — `svg/` (8 SVGs), `cards/` (8 PNGs, 1950×2700), `De-Lucerna-VOL2-EN.pdf` (print PDF, 8 pages), `De-Lucerna-VOL2-EN-web.pdf` (web PDF, 8 pages, under the 10 MB limit), `WEEKLY-KIT.md`, `ABSTRACT.txt`.
- Build tree: `hidden_files/weekly-report-w45-nl-en-build/` — build code (bslib4/content*/svglib/run/render), transform.py + transform-log.txt, rowcheck.py + rowcheck.txt, build logs (build-log.txt, build-log-fix1.txt, build-log-fix2.txt), freeze-diff.txt/json, p8-compare.txt, p8-core.txt, p8-ed.txt, occlusion-edition2.txt, occlusion-core.txt, occlusion-new2.txt, core-sha256-before.txt, fix1-baseline-sha256.txt.

## 11. Deliverable sizes and hashes (final render)

- `De-Lucerna-VOL2-EN.pdf` — 7,877,914 bytes, sha256 b934f9010adf72618a98a3a9272a18dd4aa22dc1f19bdd88ca1d37784fd88b2f
- `De-Lucerna-VOL2-EN-web.pdf` — 3,610,480 bytes, sha256 fe96959f638401a8c709c6e213179e1a885ab8a0d4287131f33a5bd30d63a7fb
- SVGs (sha256): p1-voorpagina 55561afadf5bae6803b9b31ef6f5e069ff0351d84c3902e19e437b286acc0342; p2-leven 8914adfb8c4e4fe96c06609392d333f7cba8352428a9ba3ff405138724c0607f; p3-cultuur 418dd3bd1729066b826fbde0839eef589706ab43f96a212218c7ffa3b7cd143f; p4-sport 369bece0c0f9ac3330dab5af7c302f5100a3dd71ae70d7cdcdcd41c0c5f26a31; p5-jongeren 859542c330ae1df522219b5f1d0f0035590bd921b914cfb11bf40cf92b5f1c2f; p6-verdieping c8e53e8da9353902356e62522620e388cb2e14b92ba1fa60952d20c829a825a9; p7-taal dfdc42bc11df7f30a01da0c900d017c11f2ab50d1beb090022c8019e4663f975; p8-toets c615f70bfd6efcbd68ca9ba533f8a8f9b7e1152ddff1133f0cf5ad626cee9c5c
- Cards (sha256): p1 28ef6aae1ef13b2d3e2182fb33228e1bc4ff5408850fd0de34e8008dfc58720f; p2 2e86cf43a8fb795932770c2fba7ce3e8bb10128c1361bd4b1692b2cba1850f22; p3 655143f0a2db8c0d47a2fc041ee448e8fa63430b329356a7260f90402cd8ce31; p4 a84f426f16262c567dd28cd8ecdaafccebdce649b9ea84dabc836bd429058624; p5 105771cdc098c7cc81d97bdbdba3b4a3423a42aebbd254797796e86bdf1fcb1a; p6 b893c1799614be08dcc0d6989bc16a982653c03ceedb72f627c641638381db69; p7 a009e691d8174ee26069d4d0d3924a3b393e955162f9c8f5835191df9d304a04; p8 58aaddcea1c63ff01298aefbb2eb04df4c596eb20e47100b4dc72dc94370f1f7
