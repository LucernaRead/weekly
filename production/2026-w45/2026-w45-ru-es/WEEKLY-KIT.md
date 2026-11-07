# Lucerna — Русская газета VOL.2 · RU × ES (俄语正文 + 西班牙语讲解版，W45)

**Edition:** Russian text + **Spanish** explanations (target RU × reader-native ES), for Spanish-speaking learners of Russian.
**Week:** Mon 2 – Sun 8 Nov 2026 (VOL.2, same issue week as the finalized W45 core).
**Masthead:** **Lucerna** (no article, per SOP masthead rule — Russian is article-less). Page size 1950×2700, 8 pages, warm ivory.
**Status: BUILDER-COMPLETE, NOT independently proofread.** No Discord post, no chat card/PDF dump, no repo push, no cron was made from this build. Independent proofread is the parent's next step.

Source: the finalized W45 Russian core (`files/weekly-report-w45-ru-core/`, itself the zh-cn edition). Build copied to `hidden_files/weekly-report-w45-ru-es-build/`; the core's own directories were never edited (core SVGs re-hashed after all work: identical to the baseline hashes in §2). Method = the W43 RU×ES sibling pattern: rewrite the explanation layer only, freeze everything Russian. Transform script (exact-literal replacements, asserted per string, 284 replacements): `tools/scratch/transform-w45-ru-es.py`, plus 4 wording-only P7 fit shortenings (§7) applied directly to the build copy.

---

## 1. Totals (registry-derived, identical to the core)

- **150 exercises** — A2 51 · B1 75 · B2 24; per page 10/18/18/18/18/18/12/38 (same as core).
- Writing model (P8 §H): **exactly 84 words**, unchanged Russian text; the «80–100 слов» task range unchanged.
- Registry `type` strings were localized to Spanish inside this build's registry only (Completar 54 · Opción múltiple 42 · Emparejamiento 20 · Frases 12 · Transformación 4 · Cloze 13 · Traducción 4 · Redacción 1 — counts identical to the core); type strings never print.
- Exercise instructions localized per the W43 RU×ES pattern (Completar / Formar la frase / Transformar / Traducir al español / Traducir al ruso / Relacionar / Escribir).

## 2. Baseline reproduction (before any edit)

The unmodified copy of the core build regenerated all 8 SVGs **byte-identical** to the shipped core SVGs (`tools/freeze.py baseline`, `tools/scratch/baseline-w45-ru-es`):

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

Core integrity: shipped core SVGs re-hashed after all build work — unchanged (same 8 hashes). All Spanish edits were made on top of that proven baseline, executed only through the build copy's single driver (`run.py` → `render.py`, one process). Final re-render from the final code reproduces the shipped SVGs byte-identically (pre/post sha256 diff empty).

## 3. Pairing furniture (W43 RU×ES registry, verbatim; VOL follows this core)

- **Pairing badge (P1, brick red #a4553a, 22pt bold, centred):** «TEXTOS EN RUSO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES» — **INSERTED at (975, 574)** per the W45 RU-family slot (ru-de/ru-en precedent), NOT the W43 subtitle slot: see §4 for the recorded difference. Measured ink span 402.5–1547.5 (width 1145.0); clear of the dark band above (ends 542; badge ink top 551.75) and the headline head below (baseline 606; badge ink bottom 574.25). Visually confirmed on the P1 card.
- **Top strip centre:** «КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · CADA SEMANA · EL RUSO QUE LEE RUSIA» (W43 RU×ES verbatim).
- **Footers (Spanish, every page):** left «Lucerna · SEMANARIO RUSO VOL.2 · TEXTO EN RUSO · EXPLICACIONES EN ESPAÑOL» · right «Página N de 8».
- **Gloss prefix:** «Nota — » (W43 RU×ES verbatim, incl. the build-code form).
- **P8 answer separators:** kept as shipped in W43 RU×ES — «— СТРАНИЦА N —» (Russian form; the P8 answer-generation loop is otherwise byte-identical to the core, dash style kept — see §5).
- **Contents level tag:** «все» kept unchanged, as in the shipped W43 RU×ES SVG (its P1 contents row also prints «все»).
- **Bilingual section heads** = Russian original · Spanish short form (e.g. «ГЛАВНАЯ ТЕМА · El tema principal», «НЕДЕЛЯ В ЦИФРАХ · En cifras», «В ЭТОМ НОМЕРЕ · Sumario», «ЗА И ПРОТИВ · Pros y contras», «ФРАЗЫ НЕДЕЛИ · Frases de la semana (textuales de esta edición)», «СЛЕДУЮЩАЯ НЕДЕЛЯ · La próxima semana (VOL.3)», «ТЕСТ И ОТВЕТЫ · Test y respuestas», «PÁGINA 8 · Большой тест недели + все ответы»).
- **Captions and credits stay Russian by design** (as in W43 RU×ES); image payloads byte-identical to the core on every page.

## 4. Recorded furniture difference — badge slot (for coordinator adjudication)

W43 RU×ES placed its badge at y=372, 20pt, replacing the VOL.1 core's strap subtitle. The W45 RU core's y=372 line is **frozen Russian strapline** («ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ»), not a free slot — replacing it would delete target-language text. This edition therefore follows the W45 RU-family precedent already shipped by ru-de (and ru-en): badge string verbatim from W43 RU×ES, geometry INSERTED at (975, 574), 22pt BRICK. The badge string itself is unchanged; only the slot differs, forced by the core's frozen geometry. README #20's family-slot rule (FR/IT-style insert at y=574 when no free slot exists) points the same way.

## 5. Freeze verification (rendered SVGs, this edition vs core)

- `tools/freeze.py diff` (`tools/scratch/diff-w45-ru-es.json`): added CJK characters = **0** on all 8 pages; edition SVGs contain **0 CJK characters** total.
- **Cyrillic token-multiset diff per page (target-language proof):** P1–P8 **all exactly equal** — P1 400 = 400 with zero differing tokens (the badge is Latin-only and the contents tag «все» was kept, so P1 has no Cyrillic churn at all); P2–P8 counts 443/338/306/316/354/397/641, exactly the brief's values. **No Russian token was added, removed, or altered anywhere.**
- All 8 P7 golden sentences occur exactly as in the core (Russian quotes byte-identical; only their Spanish translations are new; page tags stay Russian «Страница N»).

## 6. P8 answers (dash family; generation code byte-identical)

- `tools/p8.py compare` core vs edition: **CLEAN, 150 noted = 150 noted, missing = [], extra = [], uncertain = []**; keydiff = [83, 137, 138, 148].
- **137, 138 — documented re-aims (W43 translation precedent):** RU→ES items; Russian stems kept, instruction «Traducir al español»; keys are Spanish in this edition (137 «El miércoles 4 de noviembre es festivo.»; 138 «Un código promocional es un código de descuento.»). 139/140 are the reverse direction (Spanish prompts, «Traducir al ruso», keys Russian byte-identical); 150 is the writing apparatus line («(Pregunta abierta — texto modelo a continuación)» / «El texto modelo está en la sección H de esta página (84 palabras)»), model text unchanged Russian.
- **83, 148 — p8.py extraction artifacts, NOT key changes (README #13 lesson applied):** the tool's paren branch treats a trailing half-width paren group as part of the extracted «key», while the core's fullwidth parens are not. Printed keys are identical in both SVGs (83: key «B»; 148: key «A»). Verified by an independent dash-parse of all 150 printed P8 lines (split on the first « — »): **key diffs = [137, 138] only**; counts 150 = 150, no missing/extra.
- Spanish notes use half-width parentheses throughout (W43 RU×ES typography); the answer-generation loop format (`N. key — note`, writing items `N. ✓ note`) is unchanged from the core, with the type-string comparison already carried by the global type localization («Redacción»).
- P8 keys flow ends at y=2419 (rule at 2580) — ample clearance.

## 7. Geometric audit (mandatory SOP gate — builder run)

- `tools/occlusion_audit.py`: selftest OK (all 6 planted classes fire, clean controls silent). **Final run: 0 flags on all 8 pages; core control 0 flags; NEW vs core: 0** (`tools/scratch/occlusion-w45-ru-es.json`).
- **Same-baseline ink scan (README #10, true PIL ink boxes):** all pages 0 flags at <5 px gaps, including the P1 top band and the badge row.
- **One real defect found and fixed during production (P7):** the first render's Spanish readers'-corner disclosure (3 lines vs the core's 2), two error-clinic notes (2 lines vs 1 each), and the word-box gloss (2 lines vs 1) pushed col3 to y=1838.62, crossing the phrases rule at y=1756 (+111.04 = exactly the four excess line heights). Fix (explanation layer only, no target text moved): clinic note 1 → ««с» + instrumental: с Днём единства.» (1 line), clinic note 3 → «Desde 5: «процентов»: 25 процентов.» (1 line), word-box gloss → «промокод = código de descuento.» (1 line — the Russian definition above it already says the code is entered at purchase), disclosure → «Sin cartas ni textos al cierre: ejemplo de la redacción. La promesa pasa a VOL.3.» (2 lines; the full disclosure still stands in Russian in the same box). Final P7 col3 ends at **1727.58 — exactly the core's value, 28.4 units clear** of the rule. Visually confirmed on the P7 card.
- **Chart page (P6) element check (README #12, proper XML parse):** zero text elements overlapped by any later-drawn rect; all four bar labels and values fully visible on the card (bars 34/28/22/16, rect widths 600/494/388/282, identical to the core). Note: the RU P6 chart carries no frozen overprint of the kind seen on the ES core's chart — 0 overlap here is the normal, correct result. An early regex-based scan reported one spurious overlap; re-parsing with a real XML parser showed 0 in both core and edition (the flagged string was a frozen exercise stem at an identical baseline in both files).
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final run. Cards P1, P6, P7, P8 viewed by the builder after the final render; P2–P5 covered by the audits + Cyrillic diff.

## 8. Gloss counts (split on `·` itself, README #21)

9 gloss() calls, **26 items** — per-call counts identical to the core (content12: 3/3/3; content34: 3/3/3; content56: 3/2/3). No gloss item was added, dropped, or merged in translation.

## 9. Re-aimed items (the only key/prompt changes — translation pedagogy)

| # | Change | Key in this edition |
|---|---|---|
| 137 | RU→ES: Russian stem kept; instruction «Traducir al español» | «El miércoles 4 de noviembre es festivo.» (note: Compáralo con la página 3) |
| 138 | RU→ES: Russian stem kept; instruction «Traducir al español» | «Un código promocional es un código de descuento.» (note: Compáralo con la página 5) |
| 139 | Prompt now Spanish: «El sábado, el Krasnodar juega contra el CSKA. → ___»; instruction «Traducir al ruso» | Russian sentence, **byte-identical** (note: Fíjate en: играть + с + instrumental) |
| 140 | Prompt now Spanish: «¡Feliz Día de la Unidad Nacional para todos! → ___»; instruction «Traducir al ruso» | Russian sentence, **byte-identical** (note: поздравляю + с + instrumental) |
| 150 | Registry line is Spanish apparatus | «(Pregunta abierta — texto modelo a continuación)»; note «El texto modelo está en la sección H de esta página (84 palabras)» |

All other 145 keys byte-identical to the core (verified by the §6 dash-parse).

## 10. Readers' corner — no fabrication (disclosure + example kept, explanation layer only translated)

P7 prints the core's editor's example unchanged (Russian, «— М. (пример от редакции)») and the core's Russian disclosure unchanged, plus the Spanish disclosure line (§7). No new reader, letter, name, or quote was invented. The VOL.3 teaser repeats the call for letters, as in the core.

**Frozen-geometry note (coordinator-adjudicated, non-blocking — same as the ru-en precedent):** the letters box bottom is 1727.58 and the disclosure's 2nd line baseline is 1738.28 — i.e. the 2nd disclosure line sits below the box bottom. This geometry is **identical in the core, this edition, and ru-de** (verified element by element); it is frozen core geometry, not something this edition introduced, and the box was deliberately NOT resized. Recorded here per the brief; no action taken.

## 11. Images & credits (byte-identical payloads; credits identical to the core)

| Page | Image | Credit (as printed) |
|---|---|---|
| P1 | November park photo (autumn_path.jpg, reused from W43) | Фото: Toxer427 — лицензия CC0 (Wikimedia Commons) |
| P4 | 1912 football photo (football1912.jpg, reused from W43) | Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons) |
| P5 | Market photo (market.jpg) | Фото: Престон Керес (USDA) — общественное достояние (Wikimedia Commons) |

Image licensing verification is the core's (W45 RU core KIT §4); this edition changes no image.

## 12. Facts (identical to the core)

Split week (2–3 Nov work, 4 Nov Wednesday holiday, 3 Nov one hour shorter, school-holiday tail to 4 Nov), 11.11 sale 22 Oct – 12 Nov (attributed trade-press note only), RPL round 14 6–8 Nov (Krasnodar–CSKA Sat 19:30 Ozon Arena; Spartak–Akron Sun 16:15; round-13 closer Mon 2 Nov; pause until 20 Nov), reported past events only (CSKA–Spartak 2:0 on 25 Oct; first snow forecast failed; 28 Oct Grandparents Day; 31 Oct Halloween). Russian domestic life only; no politics. The P6 chart is labeled practice data in both languages («УЧЕБНЫЕ ДАННЫЕ · Datos de práctica» + «Una encuesta de práctica de la redacción: no son estadísticas reales.»), bars 34/28/22/16 as the core.

## 13. Files

- `files/weekly-report-w45-ru-es/svg/` — 8 final SVGs
- `files/weekly-report-w45-ru-es/cards/` — 8 cards (1950×2700 PNG)
- `files/weekly-report-w45-ru-es/Lucerna-VOL2-ES.pdf` — print PDF, 8 pages, **13,554,108 bytes**, sha256 `5bead5b33bd234535468971d7007e67396548731e7ced27a9bad9f2e733438f1`
- `files/weekly-report-w45-ru-es/Lucerna-VOL2-ES-web.pdf` — web PDF, 8 pages, **3,212,084 bytes** (< 10 MB), sha256 `daaab9ea4e31947639650c9f4e59acdef916703bc800d6d05f037067bd6375aa`
- `files/weekly-report-w45-ru-es/WEEKLY-KIT.md` — this file
- `files/weekly-report-w45-ru-es/ABSTRACT.txt` — one-line Spanish abstract
- Build: `hidden_files/weekly-report-w45-ru-es-build/` (run.py → render.py; transform script at `tools/scratch/transform-w45-ru-es.py`)

## 14. Delivery status

Builder-complete, NOT proofread-finalized, NOT pushed, NOT posted: per the task brief, repo insertion is done by the parent line (serialized) and independent proofread is still pending. No git push, no Discord post, no user message, no cron was made from this build. The weekly-git checkout was not touched.

## Coordinator adjudication (2026-10-27, binding — documentation only, no render change)

**Badge slot (975,574) 22pt BRICK: ACCEPTED as-is, no change. This edition is FINALIZED.** Independent proof three-way measurement: edition badge string VERBATIM from W43 shipped, at (975,574), 22pt, BRICK #a4553a, bold, centered, ink 402.46–1547.46; W43 badge at (975,372), 20pt, same color, ink 454.50–1495.50; W45 core y=372 row is frozen Russian strapline text, fully retained in this edition — using the 372 slot would delete target-language text, a worse outcome. Geometry is clean on all sides (dark-band bottom 542 → badge ink top 551.75 = 9.75; badge ink bottom 574.25 → title ink top 588.00 = 13.75; right-column top 580 → badge ink bottom = 5.75 vertical clearance), P1 card visual confirms no collision. Precedent: ru-de uses the same (975,574) 22pt #a4553a insert and passed proof + shipped; ru-en/ru-fr/ru-it/ru-pt use (975,372) 20pt — BOTH slot patterns are accepted RU-target precedents. Rule for future RU fan-outs: badge string must be verbatim from W43 shipped; slot follows the W45 core's frozen-text constraint and must show clean clearances + no collision. **Future RU×ES proofs must NOT re-flag badge slot.** (P7 disclosure line-2/box-bottom contact: core-identical, readable, per the ru-en adjudication non-blocking, not re-flagged.)
