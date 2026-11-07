# W45 ES core (VOL.2) — INDEPENDENT PROOFREAD, ROUND 2 (after Fix 1)

**Edition:** `files/weekly-report-w45-es-core/` (8 SVGs, 8 PNGs, `La-Lucerna-VOL2-web.pdf` [8 pages, verified], `WEEKLY-KIT.md`, `ABSTRACT.txt`)
**Proofreader:** independent subagent, 2026-10-26. NOT the builder, NOT the fix agent. Round-1 report (`hidden_files/w45/es-core-independent-proof.md`), fix log (`hidden_files/w45/es-core-fix1.md`) and SOP §§1–8 + occlusion appendix were read first, but every check below was re-run fresh on the re-rendered files.
**Method:** full text extracted from all 8 SVGs and read end to end; all dates re-checked with `date -d` (Europe/Madrid); exercise numbering and every P8 key re-derived question by question; model text counted by hand; golden sentences counted programmatically; all 8 rendered PNGs viewed; `tools/occlusion_audit.py --selftest` + full audit re-run by me.

## VERDICT: 1 PROBLEM — NOT ZERO-PROBLEM, CORE NOT FINALIZED

All 5 round-1 fixes verify on the rendered pages (see §"Round-1 fix verification" below). However this fresh full round found one new defect in the P8 answer notes. Per SOP §8.4 only a full round finding zero problems finalizes the core, so after this one-word fix the edition needs another fresh full proofread round — this report does not pre-clear the fixed version.

---

## Numbered problem list

### Problem 1 (MINOR — P8 answer note uses the wrong noun)
- **Location:** P8 RESPUESTAS, PÁGINA 4 section: `57. muchísimos — muchísimos goles 进球很多`.
- **Evidence:** Q57 (P4, section C) reads: "El domingo hay ___ partidos: ¡toda la jornada 12! (muchos)". The blank is filled by *muchísimos* modifying **partidos** (matches). The answer note restates it as "muchísimos **goles**" (goals) — a noun that appears nowhere in the question. The key itself (*muchísimos*) is correct; only the note wording is wrong, exactly the same defect class as round-1 Problem 4 (note 123, now fixed).
- **Fix:** change the note to `57. muchísimos — muchísimos partidos 比赛很多`.
- **Checked, not the same defect elsewhere:** every other P8 note was re-read against its question; no other note misnames its question's noun (spot examples: 47 Clásico ✓, 123 now Atlético–Barça ✓, 131 Ana/Pablo ✓, 132 title ✓).

---

## Round-1 fix verification (all 5 verified on rendered pages)

1. **Nov 12 Diputación Permanente vote date ABSENT — VERIFIED.** Grep over all 8 SVGs: zero occurrences of `12 NOV`, `jueves 12`, `Diputación Permanente`. P6 timeline (`EL CAMINO AL 29N`) runs 2 OCT → 29 NOV in 9 entries, 3 NOV → 13 NOV directly (confirmed on the P6 PNG). P7 preview reads in full: "El viernes 13: empieza la campaña electoral. El domingo 29: España vota. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!" — no Nov 12 item. No replacement date was invented.
2. **P7 readers'-corner on-page disclosure — VERIFIED.** Inside the `CARTAS DE LOS LECTORES` box itself (confirmed on the P7 PNG, fully inside the box border, no overflow): Spanish "Nota de la redacción: al cierre no había cartas reales ni los mejores textos de la página 8; publicamos este ejemplo y la promesa pasa al VOL.3." and Chinese "编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！". The example letter is unchanged and still labeled "— Ana (ejemplo, escrito por la redacción)" plus the standing Chinese example note; no reader could mistake it for a real letter. Reflow holds: frases block repositioned below the box, quote-row spacing clean, preview box intact, footer intact (all visible on the P7 PNG).
3. **P5 "dos noches grandes" — VERIFIED.** P5 article closing now reads "…el puente, para los jóvenes, tiene dos noches grandes." (confirmed on the P5 PNG). No dependent exercise contradicts it: Q82 only states "Halloween llenó las calles el sábado 31" ✓. No other "seguidas" for P5 anywhere (only remaining "seguidas" is the P3 observation below).
4. **P8 note 123 wording — VERIFIED.** P8 answer now reads `123. C — 马竞–巴萨与 NFL 都在周日`; key still C, matching Q123 ("la NFL y el Atlético–Barça"). The only other 国家德比 on P8 is note 47, which correctly describes the actual Clásico (Madrid 2–1) ✓.
5. **P1 gloss "el BOE" removed; remaining glosses anchored — VERIFIED.** P1 gloss now reads: "讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。" Zero occurrences of "BOE" in the P1 SVG. Anchors confirmed in the P1 article: la cuenta atrás (headline), "disolvió las Cortes", "dos decretos", "sus candidaturas" ✓.

---

## Per-dimension verdicts

- **Text (Spanish + Chinese): NOT CLEAN — Problem 1 (note 57) only.** Otherwise clean on a full end-to-end read: no spelling/accent/agreement/conjugation errors; no repeated words or truncated sentences; P7 grammar columns correct (lunes singular, más mejor rejected, gente singular, creo que + indicative); P3 Q31 keyed Falso ✓; P5 "cuatro intentos" rule, P6 subjunctive exercises all correct; all explanation-layer glosses anchored in their own page's article (P1–P5 gloss blocks each checked word by word against the article text).
- **Numbers: CLEAN.** Exercises 1–150 continuous (answers section verified programmatically: 150 entries, no gaps, no dupes); per-page counts P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38 = 150 (ranges 25–28, 52–55, 141–144 expand individually in the answers); every P8 key re-derived against its question and source text (including Q131: A, Ana only NFL, Pablo watches Atlético–Barça at night); CIS arithmetic Q87: 34 + 22.2 + 17.1 = 73.3 ✓; countdown 27 days (Nov 2 → Nov 29) ✓; model text (P8-H) counted by hand at **84 words**, matching the printed "84 词" and inside the 80–100 range.
- **Facts: CLEAN.** All weekdays re-checked with `date -d` (Nov 2 Mon, 3 Tue, 4 Wed, 5 Thu, 6 Fri, 7 Sat, 8 Sun, 9 Mon, 13 Fri, 29 Sun; Oct 29 Thu, Oct 31 Sat, Nov 1 Sun; Oct 25 Sun, Oct 5 Mon, Oct 2 Fri, Oct 6 Tue, Oct 16 Fri, Oct 28 Wed; Nov 16, 2025 Mon) ✓; puente nine-community list + ten workday places ✓; CIS October figures (PSOE 34, PP 22.2, Vox 17.1, Sumar 6.1, Podemos 3.1; field Oct 1–6, n = 5,025, ±1.4, published Oct 14; housing 55.7%, immigration 20.9%, economy 20.3%) ✓; Clásico Oct 25, 21:00, Madrid 2–1, Mbappé brace, Barça first league defeat, gap 3 points ✓; matchday-12 fixtures ✓; UCL Nov 3 (Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG), Nov 4 AEK–Real Madrid 18:45, UEL Nov 5 Real Sociedad–Lyon 18:45 ✓; NFL Nov 8, 15:30, Bernabéu, Bengals–Falcons, Sáinz-Villegas / Taylor Momsen anthems, first Bernabéu NFL Nov 16, 2025 ✓; Idealista Sep 2.930 €/m² (+11.8%) ✓; no predicted Nov 29 winner (zero occurrences of ganará/vencerá) ✓; no foreign-policy lines (Ucrania/Gaza/Trump/Feijóo/Bruselas all 0) ✓; DANA Oct 29 report carries no casualty/participation numbers and is a just-passed item, not the lead ✓; matchday-11 fixtures confirmed ABSENT (Levante–Celta, Alavés–Espanyol, Barcelona–Elche, Betis–Mallorca, Real Oviedo–Osasuna all 0) ✓; banned term «桥接» absent ✓; P6 "Es una cifra récord, veinte puntos más que en septiembre" ✓.
- **Layout (visual, all 8 PNGs viewed): CLEAN.** No overflow, overlap, or footer intrusion on any page; P7 disclosure + reflow clean (see fix 2 above); P1 illustration honestly captioned "(Ilustración de la redacción, no una fotografía)" + "Ilustración: La Lucerna" ✓; P3 chestnut photo matches its Castanyada caption with "Foto: Wikimedia Commons — CC0 (dominio público)" ✓; P5 pumpkin-market photo matches its caption with "Foto: Departamento de Agricultura de EE. UU. — dominio público" ✓; masthead "La Lucerna" and per-page footers with pairing + page numbers present on all 8 pages ✓; mid-page whitespace on P3/P5/P7 is breathing space, not a defect.
- **Geometry: CLEAN (independently re-run).** `tools/occlusion_audit.py --selftest` passed (all six planted classes fired, clean controls silent); my own run on the edition dir returned **0 flags** (`/tmp/w45-es-proof2-occlusion.json`, `flag_count: 0`). No COVER/LINEX/FOOTER/EDGE/TEXTX/BOXTITLE flags to adjudicate.
- **Golden sentences: CLEAN.** All 8 P7 sentences verified programmatically to occur exactly 2× across the 8 SVGs (article + P7), each with the correct source-page label (P1, P2, P3, P4, P5, P6, P6, P1).
- **Trend-pool + W43-promise compliance: CLEAN.** Lead matches trend-batch-A ES headline candidate (29-N countdown, housing decides); sporting climax Atlético–Barça + Valencia–Real Madrid as pooled; NFL framed as Madrid hosting per the pool; rejected pool items absent (foreign-policy spat lines, DANA anniversary as lead, matchday-11 fixtures). W43 promises: Nov 2 puente as lead ✓; Oct 29/31/Nov 1 as just-passed reports ✓; Oct 21 UCL results omitted as two-weeks-old per the promises register ✓; real-letters/best-P8-texts promise now carried to VOL.3 by the verified on-page disclosure (parent decision) ✓.
- **ABSTRACT: CLEAN.** Names the week's real topics + a learner search phrase; contains no Nov 12 date and no letters promise.

## Observations (not counted as problems)

- P3 article opens "tres noches seguidas de otoño" for Oct 29 / Oct 31 / Nov 1 — Friday Oct 30 is skipped, so "seguidas" is loose (same class as the fixed P5 wording, but a 4-day festive trio, not an 8-day gap). Carried over from round 1 as an observation, not a counted problem, per round 1's own judgment; recommend dropping "seguidas" on P3 at the next natural edit for precision.
- P4 Q57 stem "El domingo hay ___ partidos: ¡toda la jornada 12!" is loose (only Sunday's 5 of 10 matchday-12 games are on Sunday), but the answer (muchísimos) is unaffected; the counted defect is only the note's noun (Problem 1).
- KIT staleness (documentation only, not edition content): WEEKLY-KIT.md §2 P6 table and §6.1 still describe the Nov 12 timeline entry / VOL.3 preview item, while §9 correctly records them as superseded/deleted. The rendered pages are correct; recommend a KIT §2/§6.1 cleanup note at the next edit so fan-out builders are not misled. Not counted as a problem because §9 already records the supersession and the SOP gate applies to the edition pages.
- An earlier extraction artifact ("首要���题" in my own text dump) was checked against the raw SVG bytes: the P8 note 85 text is intact ("住房是首要问题"), not a defect.

## What must happen before finalization

1. Fix Problem 1 (one word: note 57 "goles" → "partidos").
2. Re-render, then run a FRESH full independent proofread round (SOP §8.4) — this report does not pre-clear the fixed version.

## Independent audit artifact

My own occlusion run: `/tmp/w45-es-proof2-occlusion.json` (0 flags, selftest OK). This report: `hidden_files/w45/es-core-independent-proof2.md`.
