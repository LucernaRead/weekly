# W45 ES core (VOL.2) — INDEPENDENT PROOFREAD (fresh eyes, not the builder)

**Edition:** `files/weekly-report-w45-es-core/` (8 SVGs, 8 PNGs, `La-Lucerna-VOL2-web.pdf`, `WEEKLY-KIT.md`, `ABSTRACT.txt`)
**Proofreader:** independent subagent, 2026-10-26. Builder's own record (`hidden_files/w45/es-core/PROOFREAD.md`, `occlusion4.json`) was read but NOT trusted; every check below was re-run.
**Method:** SOP §§1–8 + occlusion appendix read first; full text extracted from all 8 SVGs and read end to end; all dates re-checked with `date -d` (Europe/Madrid); exercise numbering and P8 keys re-derived question by question; CIS figures re-checked against the Reuters Oct 14 source; Nov 12 date re-verified from independent sources; all 8 rendered PNGs viewed; `tools/occlusion_audit.py --selftest` + full audit re-run by me.

## VERDICT: 5 PROBLEMS — NOT ZERO-PROBLEM, CORE NOT FINALIZED

The single hard blocker is Problem 1 (unverified Nov 12 date printed twice). Problems 3–5 are one-word/one-line fixes. Problem 2 is a promise gap that needs a parent/user decision (see below). After fixes, the edition must be re-rendered and given a fresh full proofread round per SOP §8.4 — a fix-and-ship without a new full round does not count.

---

## Numbered problem list

### Problem 1 (BLOCKING — unverified fact, printed twice)
- **Locations:** P6 timeline box, entry `12 NOV. — La Diputación Permanente vota los decretos.`; P7 preview box (LA PRÓXIMA SEMANA · VOL.3), `El jueves 12: la Diputación Permanente vota los decretos de vivienda.`
- **Evidence:** I could NOT confirm this date from any independent source, and the evidence points against it:
  - Exact-phrase searches (`"12 de noviembre" "Diputación Permanente" vivienda`) return zero corroboration; the only source ever cited for it is the trend pool's Hipotecas.me calendar note — a single secondary source, which the builder already flagged as unconfirmed.
  - Demócrata's complete 29-N electoral calendar (the builder's own other cited source, https://www.democrata.es/en/general-elections-spain/general-elections-calendar-2026-all-the-key-dates-of-29-n/) lists Oct 6 call, Oct 16 coalitions, Oct 21–26 candidacies, Oct 28 publication, **Nov 2 proclamation, Nov 3 publication of proclaimed candidacies, Nov 13 campaign start, Nov 29 election — and no Nov 12 entry at all**.
  - The same Demócrata article says the government intended to re-approve the two housing decree-laws "this Tuesday" (the week of the Oct 5 announcement). Decree-laws must be convalidated within 30 days of promulgation, which points to early November, not Nov 12.
  - Weekday is correct (Nov 12, 2026 is a Thursday, verified with `date -d`), but a correct weekday does not verify the event.
- **Required fix (per task instruction):** remove the Nov 12 entry from BOTH P6 and P7 before finalization. Do not carry it into VOL.3 as a preview item unless/until a second independent source confirms it. The KIT §6.1 debt note ("VOL.3 must re-verify") does not cure printing an unverified date in a learners' newspaper.

### Problem 2 (PROMISE GAP — W43 printed promise not honored)
- **Locations:** P7 CARTAS DE LOS LECTORES (example letter signed "Ana") and P7 preview box (`tus cartas y los mejores textos de la página 8`); absence of any best-P8-texts section anywhere in the issue.
- **Evidence:** W43 VOL.1's printed preview promised, verbatim: "Además: tus cartas y los mejores textos de la página 8." The promises register (`hidden_files/w45/w43-promises.md` §ES) records the W45 action as: "print real reader letters and the best VOL.1 P8 texts (overdue)." This issue instead reprints an editor's example letter (labeled ejemplo — see "Checked, not a problem" below) and re-promises the same two items for VOL.3, printing no real letters and no best P8 texts.
- **Note on the builder's justification:** KIT §6.4 claims a task instruction overrode the promise ("no real letters available, must not fabricate"). Not fabricating is correct — but the override is documented only in the KIT, not disclosed on the page, and the page re-promises the items for VOL.3 as if on schedule. SOP §10 requires printed preview/reader-corner promises to be honored.
- **Required fix:** either (a) obtain and print real letters + best P8 texts, or (b) get an explicit parent/user decision recording the deferral AND disclose the deferral on the P7 page itself (not only in the KIT). I cannot clear this one unilaterally.

### Problem 3 (MINOR — temporal wording error in article prose)
- **Location:** P5 article, closing lines: "Y el sábado 31, Madrid ya vivió su otra noche americana: Halloween llenó las calles de disfraces, calabazas y monstruos de mentira. Del susto del sábado al deporte del domingo: el puente, para los jóvenes, tiene dos noches seguidas."
- **Evidence:** The two nights named are Saturday Oct 31 and Sunday Nov 8 — 8 days apart, not consecutive ("seguidas"). Oct 31 → Nov 8 is not "dos noches seguidas" under any reading that anchors on "el sábado" (Oct 31) and "el domingo" (Nov 8).
- **Fix:** change to e.g. "tiene dos noches grandes" (one word).

### Problem 4 (MINOR — P8 answer note misnames a fixture)
- **Location:** P8 RESPUESTAS, `123. C — 国家德比与 NFL 都在周日`.
- **Evidence:** Q123 asks about Sunday Nov 8: "la NFL y el Atlético–Barça". The note calls the Atlético–Barça match "国家德比" (El Clásico). El Clásico is Real Madrid–Barcelona — the paper itself uses it that way on P4 ("El Clásico del domingo 25", Madrid–Barça 2–1). Atlético–Barça is not the Clásico. The answer key (C) is correct; only the note wording is wrong.
- **Fix:** change the note to "马竞–巴萨与 NFL 都在周日".

### Problem 5 (MINOR — glossed word absent from the article it annotates)
- **Location:** P1 headline gloss block: "讲解｜la cuenta atrás … · el BOE 《国家官方公报》".
- **Evidence:** SOP §8.1 requires every glossed word to actually appear in the text it annotates. On P1, "BOE" occurs ONLY inside that gloss line itself; the P1 headline article never mentions the BOE (BOE first appears in article text on P2 and P6). The other P1 gloss words check out: la cuenta atrás (headline), disolver las Cortes ("disolvió las Cortes"), el decreto ("decretos"), la candidatura ("candidaturas").
- **Fix:** drop "el BOE" from the P1 gloss, or add a BOE mention to the P1 article.

---

## Per-dimension verdicts

- **Text (Spanish + Chinese): NOT CLEAN — Problems 3, 4, 5.** Otherwise clean on a full end-to-end read: no spelling/accent/agreement/conjugation errors found; no repeated words or truncated sentences; P7 grammar columns correct (lunes singular, más mejor rejected, gente singular, creo que + indicative); P3 Q31 correctly keyed Falso ("Samaín 是加利西亚古节，不是万圣节译名", consistent with Q41); P5 "cuatro intentos" rule, P6 subjunctive exercises all correct.
- **Numbers: CLEAN.** Exercises 1–150 continuous (grouped ranges 25–28, 52–55, 141–144 print as ranges and expand individually in the answers; no gaps or dupes); per-page counts P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38 = 150; every P8 key re-derived against its question and source text (including the previously-fixed Q131: A, Ana only NFL, Pablo watches Atlético–Barça at night); CIS arithmetic Q87: 34 + 22.2 + 17.1 = 73.3 ✓; model text (P8-H) counted by hand at 84 words, inside the printed 80–100 range and matching the printed "84 词"; countdown 27 days (Nov 2 → Nov 29) ✓.
- **Facts: NOT CLEAN — Problems 1, 2.** Everything else verified: all weekdays re-checked with `date -d` (Nov 2 Mon, 3 Tue, 4 Wed, 5 Thu, 6 Fri, 7 Sat, 8 Sun, 9 Mon, 12 Thu, 13 Fri, 29 Sun; Oct 29 Thu, Oct 31 Sat, Nov 1 Sun) ✓; puente nine-community list verified verbatim against two independent sources (Demócrata + elconstitucional, both citing the BOE calendar: Andalucía, Aragón, Asturias, Canarias, Castilla-La Mancha, Castilla y León, Extremadura, Madrid, Navarra; workday list likewise matches) ✓; CIS October figures verified against Reuters Oct 14 (PSOE 34%, PP 22.2%, Vox 17.1%, Sumar 6.1%, Podemos 3.1%; field Oct 1–6, n = 5,025, published Oct 14; housing 55.7%, immigration 20.9%, economy 20.3%; "20 points higher than the previous month") ✓; Mourinho as Real Madrid coach verified (Britannica: reappointed July 2026; Sportradar Oct 25 Clásico roster lists Manager: Jose Mourinho) ✓; Clásico Oct 25, 21:00, Madrid 2–1, Mbappé brace, Barça first league defeat, gap 3 points ✓; matchday-12 fixtures ✓; UCL Nov 3 (Barça–Aston Villa, Atlético–Bayern, Villarreal–PSG), Nov 4 AEK–Real Madrid 18:45, UEL Nov 5 Real Sociedad–Lyon 18:45 ✓; NFL Nov 8, 15:30, Bernabéu, Bengals–Falcons, Sáinz-Villegas (Spain anthem) / Taylor Momsen (US anthem), first Bernabéu NFL Nov 16, 2025 Dolphins–Commanders ✓; Idealista Sep 2.930 €/m² (+11.8%) ✓; no predicted Nov 29 winner (no "ganará" anywhere; P6 explicitly refuses a mixed average) ✓; no foreign-policy spat lines, no Feijóo mention ✓; DANA Oct 29 report carries no casualty/participation numbers and is a just-passed culture item, not the lead ✓; matchday-11 fixtures confirmed ABSENT (Levante–Celta, Alavés–Espanyol, Barcelona–Elche, Betis–Mallorca, Real Oviedo–Osasuna all 0 hits; note Celta–Levante on Nov 8 is the matchday-12 reverse fixture, not matchday 11) ✓; banned term «桥接» absent ✓; no "primera vez" overstatement — P6 now reads "Es una cifra récord, veinte puntos más que en septiembre" ✓.
- **Layout (visual, all 8 PNGs viewed): CLEAN.** No overflow, overlap, or footer intrusion visible on any page; P1 illustration honestly captioned "(Ilustración de la redacción, no una fotografía)" + "Ilustración: La Lucerna" ✓; P3 chestnut photo matches its Castanyada caption with "Foto: Wikimedia Commons — CC0 (dominio público)" ✓; P5 pumpkin-market photo matches its caption with "Foto: Departamento de Agricultura de EE. UU. — dominio público" ✓; masthead "La Lucerna" (Spanish article La) and per-page footers with pairing + page numbers present on all 8 pages ✓; mid-page whitespace on P3/P5/P7 is breathing space, not a defect.
- **Geometry: CLEAN (independently re-run).** `tools/occlusion_audit.py --selftest` passed (all six planted classes fired, clean controls silent); my own run on the edition dir returned **0 flags**, matching the builder's `occlusion4.json`. No COVER/LINEX/FOOTER/EDGE/TEXTX/BOXTITLE flags to adjudicate.
- **Golden sentences: CLEAN.** All 8 P7 sentences verified programmatically to occur exactly 2× across the 8 SVGs (article + P7), each with the correct source-page label.
- **Readers'-corner honesty: CLEAN on labeling.** P7 letter is signed "— Ana (ejemplo, escrito por la redacción)" AND carries the Chinese note "编辑部示例信，非真实来信。本期起征集真实来信与第 8 版最佳作文——写信来吧！" — no reader could mistake it for a real letter. (The honesty of the labeling is clean; the unfulfilled W43 promise behind it is Problem 2, a separate matter.)

## Observations (not counted as problems)
- P3 article opens "tres noches seguidas de otoño" for Oct 29 / Oct 31 / Nov 1 — one night (Fri Oct 30) is skipped, so "seguidas" is loose here too, but the three nights fall inside a single week as a festive trio; I flag P5 (8-day gap) and not this. Recommend dropping "seguidas" on P3 as well for precision when P5 is fixed.
- P6 timeline "28 OCT. — Las listas se publican en el BOE" is the submitted-candidacies publication; P2 correctly gives Nov 3 for the proclaimed candidacies in the BOE. The two lines together are consistent and were not flagged.
- Builder's level split (A2 50 / B1 72 / B2 28) was spot-checked, not fully recounted; per-page exercise counts and all answer keys were fully verified.

## What the builder must do before finalization
1. Delete the Nov 12 entry from P6 and P7 (Problem 1).
2. Fix Problems 3, 4, 5 (one word / one note / one gloss item).
3. Resolve Problem 2 with the parent (honor or formally disclose the deferral on the P7 page).
4. Re-render, then run a FRESH full proofread round (SOP §8.4) — this report does not pre-clear the fixed version.

## Independent audit artifact
My own occlusion run: `/tmp/w45-es-independent-occlusion.json` (0 flags, selftest OK). This report: `hidden_files/w45/es-core-independent-proof.md`.
