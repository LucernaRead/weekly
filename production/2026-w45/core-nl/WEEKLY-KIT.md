# WEEKLY KIT — De Lucerna, VOL.2 (Nederlands core, W45)

## 1. Spec

- **Issue week:** Monday 2 November – Sunday 8 November 2026; issue dated Monday 2 November 2026.
- **Volume:** VOL.2 for Nederlands (sequel to W43 VOL.1).
- **Masthead:** De Lucerna (article De, per tools/tables.json article rule for Dutch).
- **Format:** 8 pages (multiple of 4), page size 1950 × 2700, 4 columns, warm ivory paper, dark olive-green accents.
- **Lead topic:** «Nederland in de Klimaatweek» — the national Klimaatweek (2–8 Nov), Museumnacht Amsterdam (7 Nov), Crossing Border Festival (3–8 Nov), Eredivisie matchday 12 (6–8 Nov).
- **Explanation layer convention (same as W43 NL core):** Dutch target text + Chinese small grey notes (译注 / 简析 / 答案说明). All exercise instructions and answer notes are in Chinese; all articles, prompts and golden sentences are in Dutch.
- **Pipeline:** Python → SVG → CairoSVG → PNG/PDF via tools/venv (same as W43). Build code lives in `hidden_files/weekly-report-w45-nl-build/` (run.py runs all content modules in ONE process so the exercise registry accumulates; render.py produces cards + PDFs).

## 2. Content per page

- **P1 — Voorpagina (A2, 10 ex.):** headline «Nederland in de Klimaatweek: bomen, musea en voetbal»; week agenda; numbers box (7 days, 200 Coevorden trees/shrubs, 70+ Museumnacht museums, 9 matchday-12 matches); word of the week «het klimaat»; photo herfstbos; IN HET KORT box; lightning quiz (7–10).
- **P2 — Leven (A2, 18 ex.):** «De Klimaatweek: wat kun jij doen?» — Coevorden giveaway, energy saving, KNMI colour codes (geel/oranje/rood, local warnings); photo kinderdijk (windmills); WIST JE DAT facts; EN JIJ box (best entries to VOL.3).
- **P3 — Cultuur (A2→B1, 18 ex.):** «Amsterdam blijft wakker: de Museumnacht» — Museumnacht, Crossing Border, PAN Amsterdam, Mega Snuffelmarkt; photo gracht (Amsterdam canal).
- **P4 — Sport (B1, 18 ex.):** «Europa: drie keer feest, twee keer verlies» — verified European results, matchday-10 results, standings after 10 rounds, full matchday-12 programme; photo elftal1912 (1912 Netherlands team).
- **P5 — Jongeren (B1, 18 ex.):** «Expeditie Robinson is begonnen!» — Robinson premiere follow-up, ADE (30 years) and DDW closings, youth climate actions; no photo on this page.
- **P6 — Verdieping (B2, 18 ex.):** «Geel, oranje, rood: hoe werken de codes?» — KNMI local-warning deep read, pro/contra local warnings, program-drawn chart explicitly labeled OEFENDATA (practice data, not a real survey: 100 jongeren — thuis 45, eerst tekst 25, toch naar buiten 20, weet niet 10).
- **P7 — Taal (A2/B1/B2, 12 ex.):** A2 klimaatwoorden; B1 scheidbare werkwoorden (meedoen, opruimen, vastzetten); B2 mening geven (Ik vind dat…, Volgens mij…, Het lijkt me dat…); PAS OP clinic (4 items); word «meedoen»; readers' corner (editor's example + invitation, see §6); 8 golden sentences; VOL.3 preview (Sinterklaas 15 Nov, Sint-Maarten 11 Nov, letters + best P8 texts).
- **P8 — Toets en antwoorden (38 ex.):** A kroniek (8), B algemene vragen (8), C lees en antwoord (4, new Daan/Coevorden text), D maak de zinnen (4), E vertaal (4), F woorden match (4), G dialoog bij de bomen (5), H schrijf zelf (1); all 150 answers with Chinese notes in dash style.

## 3. Measured exercise counts

- **Total: 150 exercises.** By page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- By level: A2 47, B1 72, B2 31.
- By type: 完成句子 65, 单选 44, 词汇配对 8, 判断对错 7, 造句 8, 完形单选 13, 翻译 4, 写作 1.
- Model essay (P8 H, ex. 150): **87 words** (requirement 80–100).
- Numbering continuous 1–150; P8 printed answers verified against the registry (p8.py extract: noted set = 150 of 150).

## 4. Trend/fact sources and verification debts

**Verified 2026-10-26 (web search + official listings):**

- Eredivisie matchday 12: Fri 6 Nov Willem II–PEC Zwolle 19:00; Sat 7 Nov Fortuna–Telstar 15:30, ADO–Sparta 17:45, Excelsior–Go Ahead Eagles 20:00; Sun 8 Nov Heerenveen–Feyenoord 11:15, Twente–Ajax 13:30, Cambuur–PSV 15:45, AZ–Groningen 15:45, Utrecht–NEC 19:00.
- European week results: Wed 21 Oct 2026 Real Betis 1–0 Feyenoord (Isco, 59th minute); Thu 22 Oct 2026 Ajax 2–0 Atalanta, Twente 4–1 Lincoln Red Imps, AZ 4–0 Ararat-Armenia, NEC 2–4 Dinamo Zagreb.
- Matchday 10, Sun 25 Oct 2026: PSV 1–1 Feyenoord, Sparta 1–2 Ajax, AZ 0–2 Twente.
- Standings after 10 rounds: Feyenoord 24, Ajax 21, PSV / Twente / AZ 20 each; bottom ADO 6, Telstar 6, Willem II 2.
- Museumnacht Amsterdam: Sat 7 Nov 2026, 19:00–02:00, 26th edition, 70+ museums; Museumkaart not valid that night, separate ticket needed.
- PAN Amsterdam art fair: 1–8 Nov 2026, RAI.
- Mega Snuffelmarkt Zaandam: 7–8 Nov 2026, about 250 stalls.
- Weekdays verified with `date -d` (Europe/Amsterdam): 2 Nov Monday, 3 Nov Tuesday, 7 Nov Saturday, 8 Nov Sunday, 1 Nov Sunday, 25 Oct Sunday, 22 Oct Thursday, 21 Oct Wednesday, 15 Nov Sunday, 11 Nov Wednesday.

**NOT independently re-confirmed — verification debts (paper states only what is safe):**

- **KNMI warning-system switch on 2 Nov: NOT confirmed.** A May 2026 report already describes localised KNMI warnings, so the trend pool's single-secondary-source 2 Nov switch claim was DROPPED. The paper only says warnings are "tegenwoordig lokaal" (nowadays local), with no 2 Nov switch date.
- **Klimaatweek 2–8 Nov national framing: not independently re-confirmed** by web search; the paper relies on the trend pool's citation of `coevorden.nl`, «Klimaatweek 2-8 november 2026», plus the Coevorden programme detail (200 organically grown trees/shrubs, Sat 7 Nov, Fair Groen Coevorden, Zweeloo, 13:00–16:00).
- **Crossing Border Festival dates Tue 3 – Sun 8 Nov 2026 in The Hague:** rest on the Rick Steves listing in the trend pool only.
- **Belastingplan item: DROPPED** (not printed), per the task instruction to verify against official sources or drop it.

**Rejected and NOT used:** EU budget dispute, Tropical Forest Forever Facility pledge, Ukraine / Middle East / ICC items, RDW plate cleanup 18 Nov, Sinterklaas arrival 15 Nov as a W45 lead (outside the week). Sinterklaas appears only in the VOL.3 preview (arrival Amsterdam Sun 15 Nov, inside the VOL.3 week 9–15 Nov), with Sint-Maarten Wed 11 Nov.

**W43 promises honored:** Expeditie Robinson premiere Sun 1 Nov follow-up (show now running; NO eliminations or outcomes invented), European-week results, ADE and Dutch Design Week closings (both ended Sun 25 Oct 2026).

## 5. Image credits (all reused from the W43 NL build assets, verified 2026-10-21 via the Commons API per the W43 CREDITS.md; no new downloads)

- P1 herfstbos — Vovogov90, CC0.
- P2 kinderdijk — Nationaal Archief, CC0.
- P3 gracht — W. Punt / Anefo, Nationaal Archief, CC0.
- P4 elftal1912 — Spaarnestad Photo, public domain.

## 6. Readers' corner — honest note

No real reader letter exists for this issue. P7 prints a **clearly labeled editor's example** («Li (voorbeeldbrief van de redactie)», with the Chinese note 编辑部示例信，非真实来信） plus an open invitation for real letters and best P8 texts to appear in VOL.3. This overrides the W43 promise of real letters from VOL.2, per the W45 task instruction: do NOT fabricate any reader, letter, name, or quote. (Note: the example signature "Li" is part of the labeled example, not a real reader.)

## 7. Build / reproduce commands

```
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-nl-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py   # SVGs → edition svg/ dir
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py  # cards + PDFs
cd ~/workspace/goals/lucernaread-social-media-operations/tools
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-nl-core
./venv/bin/python p8.py extract --p8 ../files/weekly-report-w45-nl-core/svg/p8-toets.svg --total 150
```

## 8. Self-proofread record (2026-10-26, builder's own pass over rendered pages)

- Full text extracted from all 8 SVGs and read end to end (Dutch spelling, de/het, verb forms, word order).
- All 150 exercise keys re-derived against question text / articles / chart; P8 printed answers match the registry (150/150).
- Numbering continuous 1–150.
- Golden sentences: all 8 verified line-joined — each appears exactly twice (once in its article, once on P7), verbatim, with correct page labels. Two P6 sentences required an article edit (split into standalone sentences so the P7 quote matches verbatim); rebuilt and re-verified.
- Chinese glosses checked: no orphan punctuation; glossed words genuinely occur in the text.
- Banned-string scan clean: 桥接 0, AFSCAFFEN 0, spaced guillemets (« / ») 0, double spaces 0.
- P6 chart-label vs bar check: labels and values match (45 / 25 / 20 / 10, total 100); chart labeled OEFENDATA.
- Same-baseline furniture-band scan: no collisions (top strip left/center/right bands separated).
- Two content-quality fixes during proofread: P2 ex. 11 changed to a non-duplicate question (was identical to the P1 quiz item); P2 ex. 17 changed from planten to wortelen (was the third planten item).
- Visual inspection of all 8 rendered PNG cards: clean, no overlaps, no cut-off text, no defects.

## 9. Occlusion audit output reference

- `occlusion_audit.py` selftest OK (all 6 planted classes fired, clean controls silent).
- Final audit on the edition: **0 flags** (`../files/weekly-report-w45-nl-core/svg: 0 flags`).
- Final build: **zero FLOW OVERFLOW / HEAD TOO WIDE warnings**.
- Full build log: `hidden_files/w45/nl-core/build-log.txt`.

## 10. Delivery note

- This core edition is delivered as files only. NOT pushed to git, NOT posted to Discord, NOT messaged anywhere (per task instruction). Handoff to the parent agent for repo insert.
- Files: `files/weekly-report-w45-nl-core/` — `svg/` (8 SVGs), `cards/` (8 PNGs), `De-Lucerna-VOL2.pdf` (20,574,293 bytes), `De-Lucerna-VOL2-web.pdf` (3,473,315 bytes, under the 10 MB limit), `WEEKLY-KIT.md`, `ABSTRACT.txt`.

## 11. Fix-1 record (2026-10-26, against independent proof `hidden_files/w45/nl-core-independent-proof.md`)

Fixes only — no other content changed; ABSTRACT untouched; no git push, no Discord.

1. **P4 tally (HARD):** headline → «Europa: drie keer feest, twee keer verlies»; article ¶1 → «de balans is drie keer feest, twee keer verlies» and «Alleen» dropped («NEC verloor: 2–4 bij Dinamo Zagreb.»); ex. 52 stem → «De ___ van de Europese week is: drie keer feest, twee keer verlies.» P8 key 52 («balans») verified unchanged and still matching; no other key/note affected.
2. **P7 promise disclosure (PROMISE GAP):** no letters/texts fabricated. An on-page disclosure was added inside the P7 BRIEVEN VAN LEZERS box itself (Dutch: «Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.»; Chinese: «截稿时未收到真实来信或第 8 版最佳作文，刊登示例信，承诺顺延 VOL.3。»), with the existing labeling («Li (voorbeeldbrief van de redactie)» + «编辑部示例信，非真实来信») kept verbatim. Layout only, to make room: BRIEVEN box height +250 (formula + a measured +50 correction, after the first re-render showed the last line 21px below the box edge), ZINNEN section moved down (fy 1712 → 1951), golden-sentence row pitch 158 → 90, VOLGENDE WEEK box 2404 → 2439; no quote or preview text changed. Final P7 visually re-checked: all BRIEVEN lines inside the box, no overlap anywhere on the page.
3. **P8 key 99 (MINOR):** «Rood komt weinig voor in Nederland.» → «Rood komt weinig voor.», matching the exercise prompt and the P6 article sentence. No note repeated the added words, so no other change was needed.
- Full re-render after the fixes (see fix log `hidden_files/w45/nl-core-fix1.md` for counts, warnings, and occlusion-audit results). This edition is NOT self-certified: a fresh full independent proof round is still required before finalization.
