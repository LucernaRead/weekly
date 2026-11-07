# Lucerna — Russian Weekly VOL.2 · RU × IT (Russian text + Italian explanations, W45)

**Edition:** Russian text + **Italian** explanations (target RU × reader-native IT), for Italian-speaking learners of Russian.
**Week:** Mon 2 – Sun 8 Nov 2026 (VOL.2, same issue week as the finalized W45 core).
**Masthead:** **Lucerna** (no article, per SOP masthead rule — Russian is article-less). Page size 1950×2700, 8 pages, warm ivory.
**Status: BUILDER-COMPLETE, NOT independently proofread.** No Discord post, no chat card/PDF dump, no repo push, no cron was made from this build. Independent proofread is the parent's next step. Weekly-git was not touched.

Source: the finalized W45 Russian core (`files/weekly-report-w45-ru-core/`, itself the zh-cn edition). Build copied to `hidden_files/weekly-report-w45-ru-it-build/`; the core's own directories were never edited (core SVGs re-hashed after all work: identical to the baseline hashes in §2). Method = the W43 RU×IT sibling pattern: rewrite the explanation layer only, freeze everything Russian. Transform script (exact-literal replacements, asserted per string): `tools/scratch/transform-w45-ru-it.py`. Verification script: `hidden_files/weekly-report-w45-ru-it-build/verify.py` (log `verify-w45-ru-it.log`).

## 1. Totals (registry-derived, identical to the core)

- **150 exercises** — A2 51 · B1 75 · B2 24; per page 10/18/18/18/18/18/12/38 (same as core).
- Writing model (P8 §H): **exactly 84 words**, unchanged Russian text; the "80–100 слов" task range unchanged.
- Registry `type` strings were localized to Italian inside this build's registry only (Completare 54 · Scelta multipla 42 · Abbinamento 20 · Frasi 12 · Trasformazione 4 · Cloze 13 · Traduzione 4 · Composizione 1 — counts identical to the core, and identical to the W43 ru-it column's type names); type strings never print.
- Exercise instructions localized per the W43 RU×IT pattern (Completa / Forma la frase / Trasforma / Scrivi / Abbina / Traduci in italiano / Traduci in russo).

## 2. Baseline reproduction (before any edit)

The unmodified copy of the core build regenerated all 8 SVGs **byte-identical** to the shipped core SVGs (`tools/freeze.py baseline`, `tools/scratch/baseline-w45-ru-it`):

| Page | Core sha256 (prefix) | Baseline |
|---|---|---|
| p1-pervaya.svg | 8bfcb7e289dc383e | 8/8 identical |
| p2-zhizn.svg | 5b35f1d7c000759f | 8/8 identical |
| p3-kultura.svg | 8be9ba7f8d32ad9b | 8/8 identical |
| p4-sport.svg | 9d699050f467482a | 8/8 identical |
| p5-molodezh.svg | f49d0ed8b09b4ec7 | 8/8 identical |
| p6-razbor.svg | 8559d61d890820e0 | 8/8 identical |
| p7-yazyk.svg | 961119d6a19e617b | 8/8 identical |
| p8-test.svg | 2738ae046bda8030 | 8/8 identical |

Core integrity: shipped core SVGs re-hashed after all build work — unchanged (all 8 match the baseline prefixes in the table above, verified against the full hashes from the task brief at the end of the build). All Italian edits were made on top of that proven baseline, executed only through the build copy's single driver (`run.py` → `render.py`, one process). The core build directory was never imported or executed in place (README #11).

## 3. Pairing furniture (W43 RU×IT registry, verbatim; VOL follows this core)

- **Pairing badge (P1, BRICK #a4553a, 20pt bold, centred):** "TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI" — **REPLACING the y=372 subtitle in place** (975, 372), exactly as the shipped W43 ru-it edition does (verified in the W43 ru-it build source, `content12.py` line 20, and in the shipped W43 ru-it P1 SVG: x=975 y=372, 20pt bold, fill #a4553a). This is deliberately NOT the 574-insert family case: README #20's insert-at-574 rule describes ×ZH-TW editions of FR/IT-target cores (whose y=372 is a frozen body strapline); the RU-target ×IT column's own shipped precedent is the in-place replacement, and the task brief's rule (W43 shipped edition beats the generalized description) confirms it. **Recorded difference for the coordinator:** README #20 generalized text vs W43 ru-it shipped practice — shipped practice applied.
- **Top strip centre:** "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · OGNI SETTIMANA · IL RUSSO CHE LEGGE LA RUSSIA" (W43 ru-it verbatim). Measured: spans 547.5–1402.5, clear of the left item and the date (same clearance pattern as ru-en's 548.9–1401.1).
- **Strap y=330 kept Russian:** "РУССКАЯ ГАЗЕТА · VOL.2 · ПРАЗДНИК · СКИДКИ · ФУТБОЛ" — this is frozen Russian target text in the W45 core (unlike W43, whose core strap carried Chinese and was rendered in Italian). Both W45 siblings (ru-en, ru-de) keep it Russian, and the freeze gate (§4) confirms it is not explanation layer. Not a deviation: it is the core's own Russian line.
- **Footers (Italian, every page):** left "Lucerna · SETTIMANALE RUSSO VOL.2 · TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO" · right "Pagina N di 8".
- **Gloss prefix:** "Nota — " (W43 shipped gloss boxes).
- **P8 answer separators:** kept as shipped in W43 RU×IT — "— СТРАНИЦА N —" (Russian form; the P8 answer-generation loop is otherwise byte-identical to the core, dash style kept — see §5).
- **Bilingual section heads** = Russian original · Italian short form, following W43 ru-it shipped shortenings where the same element exists (e.g. "НЕДЕЛЯ В ЦИФРАХ · In cifre", "В ЭТОМ НОМЕРЕ · Sommario", "СЛОВО НЕДЕЛИ · La parola", "БЛИЦ-ВИКТОРИНА · Quiz lampo", "КОРОТКО · In breve", "ЗА И ПРОТИВ · Pro e contro", "БОЛЬШОЙ РАЗБОР · Analisi", "МОЛОДЁЖЬ · Giovani", "А ВЫ? · E tu?").
- **Contents table:** kept verbatim from the core, including the level tag "все" on the Стр. 8 row — exactly as the shipped W43 ru-it edition keeps it (Russian level tag, not apparatus).
- **Captions and credits stay Russian by design** (as in W43 RU×IT); image payloads byte-identical to the core on every page.

## 4. Freeze verification (rendered SVGs, this edition vs core)

- `tools/freeze.py diff` (`tools/scratch/diff-w45-ru-it.json`): added CJK characters = **0** on all 8 pages; edition SVGs contain **0 CJK characters** total.
- **Cyrillic token-multiset diff per page (target-language proof):** P2–P8 exactly equal (counts 443/338/306/316/354/397/641 — the same counts ru-en/ru-de measured for the core). P1 differs by exactly the badge-replacement line, itemized: the replaced y=372 line "ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ" contributes one occurrence each of ЕЖЕНЕДЕЛЬНАЯ, ДЛЯ, ИЗУЧАЮЩИХ, РУССКИЙ, ЯЗЫК, НАСТОЯЩАЯ, РОССИЯ (1→0) and one each of ГАЗЕТА (2→1), ПО (3→2), РУССКИ (2→1); no other Cyrillic token differs anywhere. No contents-furniture Cyrillic change (contents rows are frozen Russian, unchanged). This is the documented W43 ru-it accommodation (§3), not a content loss.
- All 8 P7 golden sentences occur exactly as in the core (Russian quotes byte-identical; only their Italian translations are new; page tags stay Russian "Страница N"). Bare-sentence counts on page-joined text: 2× each in both core and edition.

## 5. P8 answers (dash family; generation code byte-identical)

- `tools/p8.py compare` core vs edition: **CLEAN, 150 noted = 150 noted, missing = [], extra = [], uncertain = []**; keydiff = [83, 137, 138, 148].
- **137, 138 — documented re-aims (W43 translation precedent):** RU→IT items; Russian stems kept, instruction "Traduci in italiano"; keys are Italian in this edition (137 "Mercoledì 4 novembre è festa."; 138 "Il codice promozionale è un codice sconto."). 139/140 are the reverse direction (Italian prompts, "Traduci in russo", keys Russian byte-identical); 150 is the writing apparatus line ("(Domanda aperta — testo modello qui sotto)" / "Testo modello nella sezione H di questa pagina (84 parole)"), model text unchanged Russian.
- **83, 148 — p8.py extraction artifacts, NOT key changes (README #13 lesson applied):** the tool's paren branch treats a trailing paren group as part of the extracted "key" in one edition but not the other. Printed keys are identical in both SVGs. Verified by an independent dash-parse of all 150 printed P8 lines (split on the first " — "): **key diffs = [137, 138] only**; counts 150 = 150, no missing/extra. All other keys byte-identical; notes translated (note-only diffs, keys unchanged).
- Italian notes use half-width parentheses throughout (0 full-width parentheses in any page SVG, verified); the answer-generation loop format (`N. key — note`, writing items `N. ✓ note`) is unchanged from the core, with the type-string comparison already rewritten to "Composizione" by the global type mapping.
- P8 keys flow ends at y=2375 (rule at 2580) — ample clearance.

## 6. Gloss counts (split on `·` itself, README #21)

9 gloss() calls, **26 items** — per-call counts identical to the core (content12: 3/3/3; content34: 3/3/3; content56: 3/2/3). No gloss item was added, dropped, or merged in translation.

## 7. Geometric audit (mandatory SOP gate — builder run)

- `tools/occlusion_audit.py`: selftest OK (all 6 planted classes fire, clean controls silent). **Final run: 0 flags on all 8 pages; core control 0 flags; NEW vs core: 0.**
- **Same-baseline ink scan (README #10):** P1 furniture bands 0 flags at <5 px gaps (advance-width extents), including the P1 top band and the badge row; core P1 same result.
- **Chart page (P6) element check (README #12):** zero text elements overlapped by any later-drawn rect in the edition (bars start at x=685; labels end at x≤307.6; values start 14 units past their bar ends: 34% at x=1299 after bar end 1285, 28% at 1193, 22% at 1087, 16% at 981); all four bar labels and values fully visible on the card (bars 34/28/22/16 as the core). The chart note line is one line, 1241.9 px wide (< 1820 full width). The RU P6 chart has no ES-style frozen overprint — 0 overlaps is the normal result here, as the task brief states.
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final run. Cards P1, P6, P7 viewed by the builder after the final render; P2–P5, P8 covered by the audits + Cyrillic diff.
- P7 col3 ends at **1727.58 — exactly the core's value** (see §8).

### 7a. KNOWN ITEM FOR THE INDEPENDENT PROOFREADER — P7 letters-box border contact (inherited core geometry, disclosed, NOT changed)

On the rendered P7, the letters box's bottom border (light #d8cfb4) passes through the top third of the second line of the disclosure in BOTH editions, pixel-identically: box bottom 1727.58, disclosure line-2 baseline 1738.28, in the core (Chinese line) and in this edition (Italian line) alike. The text stays fully legible — glyphs paint over the light border — and the occlusion audit reports 0 flags for both editions. This is NOT a newly introduced overlap: this edition adds zero displacement (col3 ends exactly at the core value, same line counts throughout the P7 col-3 stack). Builder decision, per the task brief's gate 6 and the coordinator's binding ru-en adjudication (2026-10-27, ru-en KIT §15 — same geometry, same contact, accepted as non-blocking frozen core geometry): keep the core-identical geometry rather than re-engineer it unilaterally, and record it here. Do NOT re-flag as a new defect; fail only if the geometry differs from the core or the text becomes unreadable.

## 8. Readers' corner — no fabrication (disclosure + example kept, explanation layer only translated)

P7 prints the core's editor's example unchanged (Russian, "— М. (пример от редакции)") and the core's Russian disclosure unchanged, plus the Italian disclosure line ("Nessuna lettera vera né testo migliore: esempio redazionale, promessa VOL.3.", 2 lines, same line count as the Chinese line it replaces — wrap-verified with the build's own `wrap()` before rendering). No new reader, letter, name, or quote was invented. The VOL.3 teaser repeats the call for letters, as in the core.
Geometry proof (measured from the SVGs, core vs edition): letters-box rect (x=1451) y=1254.58 height 473.0 → bottom **1727.58 in both**; disclosure line-2 baseline **1738.28 in both** (core line-2 "为编辑部示例；承诺顺延至 VOL.3。", edition line-2 "esempio redazionale, promessa VOL.3."). No box geometry was touched.

## 9. Re-aimed items (the only key/prompt changes — translation pedagogy)

| # | Change | Key in this edition |
|---|---|---|
| 137 | RU→IT: Russian stem kept; instruction "Traduci in italiano" | "Mercoledì 4 novembre è festa." (note: Confronta pagina 3) |
| 138 | RU→IT: Russian stem kept; instruction "Traduci in italiano" | "Il codice promozionale è un codice sconto." (note: Confronta pagina 5) |
| 139 | Prompt now Italian: "Sabato il Krasnodar gioca contro il CSKA. → ___"; instruction "Traduci in russo" | Russian sentence, **byte-identical** (note: Nota: играть + с + strumentale) |
| 140 | Prompt now Italian: "Auguri a tutti per il Giorno dell'Unità Nazionale! → ___"; instruction "Traduci in russo" | Russian sentence, **byte-identical** (note: поздравляю + с + strumentale) |
| 150 | Registry line is Italian apparatus | "(Domanda aperta — testo modello qui sotto)"; note "Testo modello nella sezione H di questa pagina (84 parole)" |

All other 145 keys byte-identical to the core (verified by the §5 dash-parse).

## 10. Images & credits (byte-identical payloads; credits identical to the core)

| Page | Image | Credit (as printed) |
|---|---|---|
| P1 | November park photo (autumn_path.jpg, reused from W43) | Фото: Toxer427 — лицензия CC0 (Wikimedia Commons) |
| P4 | 1912 football photo (football1912.jpg, reused from W43) | Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons) |
| P5 | Market photo (market.jpg) | Фото: Престон Керес (USDA) — общественное достояние (Wikimedia Commons) |

Image licensing verification is the core's (W45 RU core KIT §4); this edition changes no image. P2, P3, P6, P7, P8 carry no embedded photos in either edition. Payload check: per-page base64-blob sha256 (first 16) identical core vs edition on P1/P4/P5, empty on all other pages.

## 11. Facts (identical to the core)

Split week (2–3 Nov work, 4 Nov Wednesday holiday, 3 Nov one hour shorter, school-holiday tail to 4 Nov), 11.11 sale 22 Oct – 12 Nov (attributed trade-press note only), RPL round 14 6–8 Nov (Krasnodar–CSKA Sat 19:30 Ozon Arena; Spartak–Akron Sun 16:15; round-13 closer Mon 2 Nov; pause until 20 Nov), reported past events only (CSKA–Spartak 2:0 on 25 Oct; first snow forecast failed; 28 Oct Grandparents Day; 31 Oct Halloween). Russian domestic life only; no politics. The P6 chart is labeled practice data in both languages ("УЧЕБНЫЕ ДАННЫЕ · Dati di esercitazione" + "Это учебный опрос редакции для упражнений — не настоящая статистика. Dati di esercitazione della redazione, non statistiche reali."), bars 34/28/22/16 as the core.

## 12. Files

- `files/weekly-report-w45-ru-it/svg/` — 8 final SVGs
- `files/weekly-report-w45-ru-it/cards/` — 8 cards (1950×2700 PNG)
- `files/weekly-report-w45-ru-it/Lucerna-VOL2-IT.pdf` — print PDF, 8 pages, **13,551,274 bytes**, sha256 `20bd14c011d1bc03f475fda5ac03d5bb5a447097bbe30074911f9b8edd2079a7`
- `files/weekly-report-w45-ru-it/Lucerna-VOL2-IT-web.pdf` — web PDF, 8 pages, **3,173,183 bytes** (< 10 MB), sha256 `b393544320f532ec16d01bbe3fa14e0eace27101b80a20858b86661375a5ab88`
- `files/weekly-report-w45-ru-it/WEEKLY-KIT.md` — this file
- `files/weekly-report-w45-ru-it/ABSTRACT.txt` — one-line Italian abstract (see §13)
- Build: `hidden_files/weekly-report-w45-ru-it-build/` (run.py → render.py; transform script at `tools/scratch/transform-w45-ru-it.py`; verification script + log at `hidden_files/weekly-report-w45-ru-it-build/verify.py`, `verify-w45-ru-it.log`; build log `run-w45-ru-it.log`)

Final SVG sha256:

| Page | sha256 |
|---|---|
| p1-pervaya.svg | c1d2fb118d8ab2692fb93ae169b15195d15633430d331a71d316a729b5b32b65 |
| p2-zhizn.svg | 423543926f102eba7019db4425e8a3434b87b965c80b462645efeb896f361faa |
| p3-kultura.svg | 98020e283d53e98d604d5190205301ed132de95f1a7e5bf43f0a4d1a50468221 |
| p4-sport.svg | a94154971cad99da58d96b5d0a419745354b61699358a319b97c0e7c676035fd |
| p5-molodezh.svg | c5ca985498b4de9584447f34533b9da1e1086363c9683752945f77984d1597d4 |
| p6-razbor.svg | 12b8a90175590ecc5c047d0d6dec27f060292db1d8dbd8186fe4353e6cb2a012 |
| p7-yazyk.svg | 77c049c9ae88bc42f4e635cc86267c12889498fa1d63ef8da2b5a4cdc505f78e |
| p8-test.svg | f421a428e16fdbefb9472fd49c7409f266151c9f74a7c9fac03dfad195ca0bc4 |

## 13. Abstract

`ABSTRACT.txt` in this dir (one line, no ASCII double quotes, Italian):

> Lucerna Settimana Russa VOL.2: mercoledì 4 novembre festa, martedì 3 novembre un'ora in meno, acquisti intelligenti per i saldi 11.11 e 14ª giornata di calcio russo dal 6 all'8 novembre — 150 esercizi da A2 a B2 per italiani che imparano il russo con le notizie russe.

## 14. Build notes (transform decisions, for the next builder)

- The transform follows the ru-en script's structure exactly (repoint → bslib4 furniture → badge → P8-E pre-pass → global apparatus → per-file pairs), with Italian strings. The ru-en ordering lesson is preserved: the global pass runs before per-file pairs, so per-file old strings containing a global pattern are written in their POST-global form (P2 letter line, P7 quote 1, P8-E key 137 — all contain "mercoledì 4 novembre" from the global "11 月 4 日星期三" mapping).
- Wording shortenings forced by PIL ink measurements — wording changed, geometry never changed (all measured with the build's own `wrap()`/`text_w()` before rendering):
  - P1 word para: "сокращённый день = giornata più corta." (1 line at 19pt in 434px; the fuller "giornata lavorativa più corta" wraps to 2 lines there — the full form is kept in the P7 bridge and exercise notes, where width allows).
  - P7 word box: "промокод = codice promozionale." (1 line; adding ", da inserire alla cassa" wraps to 2 lines and would shift the whole col-3 stack — the purchase-time nuance remains in the frozen Russian line above).
  - P7 disclosure: "Nessuna lettera vera né testo migliore: esempio redazionale, promessa VOL.3." (exactly 2 lines, same as the core; longer variants wrap to 3 lines and would push the box bottom onto the phrases rule).
  - P1 media head: "СМИ · Di che parlano" (ends 1772.5 in the col-4 box; the literal "Di che cosa parlano i media" ends 1933.2, past the box border 1885).
  - P1 numbers box / contents / word heads use the W43 ru-it shipped shortenings ("In cifre", "Sommario", "La parola"), all measured inside their boxes.
- Transform safety (README #17/#18): replacements are whole-line or exact unique literals with a per-pair assertion (rep() aborts if a pair matches 0 times); value-map replacements use bare text, never repr literals — verified by the quote-digit leak scan (0 hits on all pages) and 0 full-width parentheses on all pages.
- Changed-line parity vs the ru-en build: identical changed-line sets in all six source files except the deliberate IT-column divergences — badge color (BRICK, not OLIVE), top strip, footer/page line/gloss prefix, and Italian strings throughout (including the "Sommario"/"In cifre"/"La parola" shortenings, which ru-en renders in full English forms).

## 15. Delivery status

Builder-complete, NOT proofread-finalized, NOT pushed, NOT posted: per the task brief, repo insertion is done by the parent line (serialized) and independent proofread is still pending. No git push, no Discord post, no user message, no cron was made from this build. Weekly-git was not touched.
