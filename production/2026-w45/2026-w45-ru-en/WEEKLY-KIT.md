# Lucerna — Russian Weekly VOL.2 · RU × EN (Russian text + English explanations, W45)

**Edition:** Russian text + **English** explanations (target RU × reader-native EN), for English-speaking learners of Russian.
**Week:** Mon 2 – Sun 8 Nov 2026 (VOL.2, same issue week as the finalized W45 core).
**Masthead:** **Lucerna** (no article, per SOP masthead rule — Russian is article-less). Page size 1950×2700, 8 pages, warm ivory.
**Status: BUILDER-COMPLETE, NOT independently proofread.** No Discord post, no chat card/PDF dump, no repo push, no cron was made from this build. Independent proofread is the parent's next step.

Source: the finalized W45 Russian core (`files/weekly-report-w45-ru-core/`, itself the zh-cn edition). Build copied to `hidden_files/weekly-report-w45-ru-en-build/`; the core's own directories were never edited (core SVGs re-hashed after all work: identical to the baseline hashes in §2). Method = the W43 RU×EN sibling pattern: rewrite the explanation layer only, freeze everything Russian. Transform script (exact-literal replacements, asserted per string): `tools/scratch/transform-w45-ru-en.py`.

## 1. Totals (registry-derived, identical to the core)

- **150 exercises** — A2 51 · B1 75 · B2 24; per page 10/18/18/18/18/18/12/38 (same as core).
- Writing model (P8 §H): **exactly 84 words**, unchanged Russian text; the "80–100 слов" task range unchanged.
- Registry `type` strings were localized to English inside this build's registry only (fill-in 54 · multiple choice 42 · matching 20 · sentence building 12 · transformation 4 · cloze 13 · translation 4 · writing 1 — counts identical to the core); type strings never print.
- Exercise instructions localized per the W43 RU×EN pattern (Fill in / Build a sentence / Rewrite / Writing / Match the pairs / Translate into English / Translate into Russian).

## 2. Baseline reproduction (before any edit)

The unmodified copy of the core build regenerated all 8 SVGs **byte-identical** to the shipped core SVGs (`tools/freeze.py baseline`, `tools/scratch/baseline-w45-ru-en`):

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

Core integrity: shipped core SVGs re-hashed after all build work — unchanged (same 8 hashes). All English edits were made on top of that proven baseline, executed only through the build copy's single driver (`run.py` → `render.py`, one process).

## 3. Pairing furniture (W43 RU×EN registry, verbatim; VOL follows this core)

- **Pairing badge (P1, olive #3e4c2a, 20pt bold, centred):** "TEXT IN RUSSIAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS" — **REPLACING the y=372 subtitle in place** (975, 372), exactly as the shipped W43 ru-en edition does. This is deliberately NOT the ru-de family slot (insert at (975, 574) 22pt BRICK, subtitle kept): the task brief states the EN column follows the W43 ru-en shipped edition, and the W43 ru-en build source confirms the in-place replacement (`content12.py`: badge line at y=372, 20pt sans bold OLIVE). The ru-de slot is the German column's precedent, not the English column's.
- **Top strip centre:** "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · ONE ISSUE A WEEK · THE RUSSIAN RUSSIANS READ" (W43 ru-en verbatim). Measured on the rendered P1: centre spans 548.9–1401.1, clear of the left item (ends 371.5) and the date (starts 1464.6).
- **Footers (English, every page):** left "Lucerna · RUSSIAN WEEKLY VOL.2 · Russian text · English explanations" · right "Page N of 8".
- **Gloss prefix:** "Note — " (W43 shipped gloss boxes).
- **P8 answer separators:** kept as shipped in W43 RU×EN — "— СТРАНИЦА N —" (Russian form; the P8 answer-generation loop is otherwise byte-identical to the core, dash style kept — see §5).
- **Bilingual section heads** = Russian original · English short form (e.g. "УПРАЖНЕНИЯ · Page N exercises", "ГЛАВНАЯ ТЕМА · The lead", "НЕДЕЛЯ В ЦИФРАХ · Numbers", "В ЭТОМ НОМЕРЕ · In this issue", "ФРАЗЫ НЕДЕЛИ · Phrases of the week (verbatim from this issue)", "СЛЕДУЮЩАЯ НЕДЕЛЯ · Next week (VOL.3)").
- **Contents table:** kept verbatim from the core, including the level tag "все" on the Стр. 8 row — exactly as the shipped W43 ru-en edition keeps it (Russian level tag, not apparatus).
- **Captions and credits stay Russian by design** (as in W43 RU×EN); image payloads byte-identical to the core on every page.

## 4. Freeze verification (rendered SVGs, this edition vs core)

- `tools/freeze.py diff` (`tools/scratch/diff-w45-ru-en.json`): added CJK characters = **0** on all 8 pages; edition SVGs contain **0 CJK characters** total.
- **Cyrillic token-multiset diff per page (target-language proof):** P2–P8 exactly equal (counts 443/338/306/316/354/397/641 — the same counts ru-de measured for the core). P1 differs by exactly the subtitle line, itemized: the replaced y=372 line "ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ" contributes one occurrence each of ЕЖЕНЕДЕЛЬНАЯ, ДЛЯ, ИЗУЧАЮЩИХ, РУССКИЙ, ЯЗЫК, НАСТОЯЩАЯ, РОССИЯ (1→0) and one each of ГАЗЕТА (2→1), ПО (3→2), РУССКИ (2→1); no other Cyrillic token differs anywhere. This is the documented W43 ru-en accommodation (§3), not a content loss.
- All 8 P7 golden sentences occur exactly as in the core (Russian quotes byte-identical; only their English translations are new; page tags stay Russian "Страница N"). Bare-sentence counts on page-joined text: 2× each in both core and edition.

## 5. P8 answers (dash family; generation code byte-identical)

- `tools/p8.py compare` core vs edition: **CLEAN, 150 noted = 150 noted, missing = [], extra = [], uncertain = []**; keydiff = [83, 137, 138, 148].
- **137, 138 — documented re-aims (W43 translation precedent):** RU→EN items; Russian stems kept, instruction "Translate into English"; keys are English in this edition (137 "Wednesday, 4 November is a day off."; 138 "A promo code is a discount code."). 139/140 are the reverse direction (English prompts, "Translate into Russian", keys Russian byte-identical); 150 is the writing apparatus line ("(open task, model text below)" / "Model text in section H of this page (84 words)"), model text unchanged Russian.
- **83, 148 — p8.py extraction artifacts, NOT key changes (README #13 lesson applied):** the tool's paren branch treats a trailing paren group as part of the extracted "key" in one edition but not the other. Printed keys are identical in both SVGs (83: "83. B — …"; 148: "148. A — …"). Verified by an independent dash-parse of all 150 printed P8 lines (split on the first " — "): **key diffs = [137, 138] only**; counts 150 = 150, no missing/extra. All other keys byte-identical; notes translated (note-only diffs, keys unchanged).
- English notes use half-width parentheses throughout; the answer-generation loop format (`N. key — note`, writing items `N. ✓ note`) is unchanged from the core, with the type-string comparison already rewritten to "writing" by the global type mapping.
- P8 keys flow ends at y=2274 (rule at 2580) — ample clearance.

## 6. Gloss counts (split on `·` itself, README #21)

9 gloss() calls, **26 items** — per-call counts identical to the core (content12: 3/3/3; content34: 3/3/3; content56: 3/2/3). No gloss item was added, dropped, or merged in translation.

## 7. Geometric audit (mandatory SOP gate — builder run)

- `tools/occlusion_audit.py`: selftest OK (all 6 planted classes fire, clean controls silent). **Final run: 0 flags on all 8 pages; core control 0 flags; NEW vs core: 0.**
- **Same-baseline ink scan (README #10):** all pages 0 flags at <5 px gaps (advance-width extents), including the P1 top band and the badge row.
- **Chart page (P6) element check (README #12):** zero text elements overlapped by any later-drawn rect in both core and edition; all four bar labels and values fully visible on the card (bars 34/28/22/16 as the core). The chart note line is one line, 1177.6 px wide (< 1820 full width).
- **No frozen-geometry tail collisions on P6:** the P6 check reads 0 overlaps in the edition and 0 in the core — there is no ≤5 px frozen tail graze to record in this edition (unlike the ru-de precedent, which recorded one and kept it).
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final run. Cards P1, P6, P7 viewed by the builder after the final render; P2–P5, P8 covered by the audits + Cyrillic diff.
- P7 col3 ends at **1727.58 — exactly the core's value, 28.4 units clear** of the phrases rule (1756). P2 col3 ends 1184.5 (band at 1566 — ample clearance). P1 bridge wraps cleanly across the headline flow with no orphan line-start punctuation.

### 7a. KNOWN ITEM FOR THE INDEPENDENT PROOFREADER — P7 letters-box border graze (inherited core geometry, disclosed)

On a full-resolution crop, the letters box's bottom border (light #d8cfb4) passes through the middle of the second line of the disclosure in BOTH editions, pixel-identically: box bottom 1727.58, disclosure line-2 baseline 1738.28, in the core (Chinese line) and in this edition (English line) alike. The text stays fully legible — glyphs paint over the light border — and the occlusion audit reports 0 flags for both editions, but the border visibly straddles the last line. This is NOT a newly introduced overlap: this edition adds zero displacement (col3 ends exactly at the core value, same line counts throughout the P7 col-3 stack). Builder decision: keep the core-identical geometry rather than re-engineer it unilaterally, and hand the adjudication to the independent proofreader. If the proofreader rules it a defect, the contained fix is lh +20 in `content7.py` (box bottom 1747.58, still 8.4 clear of the phrases rule) — do NOT grow the box past the rule, and do NOT shorten the disclosure to one line (it must carry: no real letters, no best texts, editor's example, promise for VOL.3).

## 8. Re-aimed items (the only key/prompt changes — translation pedagogy)

| # | Change | Key in this edition |
|---|---|---|
| 137 | RU→EN: Russian stem kept; instruction "Translate into English" | "Wednesday, 4 November is a day off." (note: Compare page 3) |
| 138 | RU→EN: Russian stem kept; instruction "Translate into English" | "A promo code is a discount code." (note: Compare page 5) |
| 139 | Prompt now English: "On Saturday, Krasnodar play CSKA. → ___"; instruction "Translate into Russian" | Russian sentence, **byte-identical** (note: Note: играть + с + instrumental) |
| 140 | Prompt now English: "I wish everyone a happy Unity Day! → ___"; instruction "Translate into Russian" | Russian sentence, **byte-identical** (note: поздравляю + с + instrumental) |
| 150 | Registry line is English apparatus | "(open task, model text below)"; note "Model text in section H of this page (84 words)" |

All other 145 keys byte-identical to the core (verified by the §5 dash-parse).

## 9. Readers' corner — no fabrication (disclosure + example kept, explanation layer only translated)

P7 prints the core's editor's example unchanged (Russian, "— М. (пример от редакции)") and the core's Russian disclosure unchanged, plus the English disclosure line ("No real letters or best texts yet — editor's example; promise for VOL.3.", 2 lines, same line count as the Chinese line it replaces). No new reader, letter, name, or quote was invented. The VOL.3 teaser repeats the call for letters, as in the core.

## 10. Images & credits (byte-identical payloads; credits identical to the core)

| Page | Image | Credit (as printed) |
|---|---|---|
| P1 | November park photo (autumn_path.jpg, reused from W43) | Фото: Toxer427 — лицензия CC0 (Wikimedia Commons) |
| P4 | 1912 football photo (football1912.jpg, reused from W43) | Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons) |
| P5 | Market photo (market.jpg) | Фото: Престон Керес (USDA) — общественное достояние (Wikimedia Commons) |

Image licensing verification is the core's (W45 RU core KIT §4); this edition changes no image. P2, P3, P6, P7, P8 carry no embedded photos in either edition.

## 11. Facts (identical to the core)

Split week (2–3 Nov work, 4 Nov Wednesday holiday, 3 Nov one hour shorter, school-holiday tail to 4 Nov), 11.11 sale 22 Oct – 12 Nov (attributed trade-press note only), RPL round 14 6–8 Nov (Krasnodar–CSKA Sat 19:30 Ozon Arena; Spartak–Akron Sun 16:15; round-13 closer Mon 2 Nov; pause until 20 Nov), reported past events only (CSKA–Spartak 2:0 on 25 Oct; first snow forecast failed; 28 Oct Grandparents Day; 31 Oct Halloween). Russian domestic life only; no politics. The P6 chart is labeled practice data in both languages ("УЧЕБНЫЕ ДАННЫЕ · Practice data" + "Это учебный опрос редакции для упражнений — не настоящая статистика. This is the editors' practice data, not real statistics."), bars 34/28/22/16 as the core.

## 12. Files

- `files/weekly-report-w45-ru-en/svg/` — 8 final SVGs
- `files/weekly-report-w45-ru-en/cards/` — 8 cards (1950×2700 PNG)
- `files/weekly-report-w45-ru-en/Lucerna-VOL2-EN.pdf` — print PDF, 8 pages, **13,515,528 bytes**
- `files/weekly-report-w45-ru-en/Lucerna-VOL2-EN-web.pdf` — web PDF, 8 pages, **3,137,814 bytes** (< 10 MB)
- `files/weekly-report-w45-ru-en/WEEKLY-KIT.md` — this file
- `files/weekly-report-w45-ru-en/ABSTRACT.txt` — one-line English abstract
- Build: `hidden_files/weekly-report-w45-ru-en-build/` (run.py → render.py; transform script at `tools/scratch/transform-w45-ru-en.py`; verification scripts at `tools/scratch/verify-w45-ru-en.py`, `tools/scratch/verify2-w45-ru-en.py`)

## 13. Build notes (transform recovery, for the next builder)

- The first transform run died mid-content12 on an ordering lesson worth keeping: the global pass runs before per-file pairs, so any per-file old string containing a global pattern must be written in its POST-global form. Three cases: the P2 letter line ("你呢？Wednesday, 4 November你怎么过？…"), the P7 quote 1 ("Wednesday, 4 November，是工作周中间的休息日。"), and the P8-E key 137 ("Wednesday, 4 November放假。"). The recovered script handles these; already-applied early steps (repoint/bslib4/badge/pre-pass) are guarded with a tolerant re-apply so the script is re-runnable to that point.
- Two further corrections found by the post-global checker: the P3 note is "можно + 不定式" (Russian можно + Chinese 不定式), not "可以 + 不定式"; and the P8 writing type check needs no per-file pair (the global '"写作"' → '"writing"' mapping already rewrites it).
- Changed-line parity vs the ru-de build: identical changed-line sets in all six source files except the two deliberate EN-column divergences — the badge line (replaced in place, §3) and the contents "все" tag (kept, §3).

## 14. Delivery status

Builder-complete, NOT proofread-finalized, NOT pushed, NOT posted: per the task brief, repo insertion is done by the parent line (serialized) and independent proofread is still pending. No git push, no Discord post, no user message, no cron was made from this build. Weekly-git was not touched.

## 15. Coordinator adjudication (2026-10-27, binding — documentation only, no render change)

**P7 readers'-corner box-bottom contact: ACCEPTED as-is, no change. This edition is FINALIZED.** Evidence (independent proof, hidden_files/w45/ru-en-proof/REPORT.md): box rect bottom 1727.58 (outer edge 1728.28), disclosure line-2 baseline 1738.28 IDENTICAL in core and edition — zero displacement, frozen core geometry. True ink contact: core 7.0px, edition 6.0px, at the TOP ~1/3 of the ink (correction to §7a's "middle" wording — it is top-third, not middle). Box is drawn BEFORE the text, so the text is fully readable (crops p7-box-ed-crop.png / p7-box-core-crop.png confirm). Canonical occlusion audit 0 flags (LINEX counts only later-drawn graphics over earlier text; BOXTITLE attribution does not trigger here) — 0 flags ≠ no contact, but the contact is core-inherent and the text is legible. Precedent: es-en/es-de P6 graze (frozen core geometry + fully readable text + audit 0 flags = non-blocking). The contained lh+20 fix (box bottom →1747.58, 8.4px clearance to the golden-sentence rule) would deviate the edition from core geometry for no reader benefit and is NOT applied. **Future RU×EN proofs must NOT re-flag this item**; fail only if the geometry differs from the core or the text becomes unreadable.
