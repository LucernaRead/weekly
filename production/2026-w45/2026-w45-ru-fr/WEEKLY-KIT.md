# Lucerna — Russian Weekly VOL.2 · RU × FR (Russian text + French explanations, W45)

**Edition:** Russian text + **French** explanations (target RU × reader-native FR), for French-speaking learners of Russian.
**Week:** Mon 2 – Sun 8 Nov 2026 (VOL.2, same issue week as the finalized W45 core).
**Masthead:** **Lucerna** (no article, per SOP masthead rule — Russian is article-less). Page size 1950×2700, 8 pages, warm ivory.
**Status: BUILDER-COMPLETE, NOT independently proofread.** No Discord post, no chat card/PDF dump, no repo push, no cron was made from this build. Weekly-git was not touched. Independent proofread is the parent's next step.

Source: the finalized W45 Russian core (`files/weekly-report-w45-ru-core/`, itself the zh-cn edition). Build copied to `hidden_files/weekly-report-w45-ru-fr-build/`; the core's own directories were never edited (core SVGs re-hashed after all work: identical to the baseline hashes in §2). Method = the W43 RU×FR sibling pattern: rewrite the explanation layer only, freeze everything Russian. Transform script (exact-literal replacements, asserted per string): `tools/scratch/transform-w45-ru-fr.py`. All content modules were run only through the build's single driver (`run.py` → `render.py`, one process); no content module was ever imported inside the core build directory.

## 1. Totals (registry-derived, identical to the core)

- **150 exercises** — A2 51 · B1 75 · B2 24; per page 10/18/18/18/18/18/12/38 (same as core).
- Writing model (P8 §H): **exactly 84 words**, unchanged Russian text; the "80–100 слов" task range unchanged. The MODELO block is byte-identical to the core (the only content8 diff line touching it is the `instr="写作"` → `instr="Rédaction"` apparatus change).
- Registry `type` strings were localized to French inside this build's registry only (Compléter 54 · Choix 42 · Appariement 20 · Phrases 12 · Transformer 4 · Cloze 13 · Traduction 4 · Rédaction 1 — counts identical to the core); type strings never print.
- Exercise instructions localized per the W43 RU×FR pattern (Compléter / Former la phrase / Transformer / Écrire / Associer / Traduire en français / Traduire en russe).

## 2. Baseline reproduction (before any edit)

The unmodified copy of the core build regenerated all 8 SVGs **byte-identical** to the shipped core SVGs (`tools/freeze.py baseline`, `tools/scratch/baseline-w45-ru-fr`):

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

Core integrity: shipped core SVGs re-hashed after all build work — unchanged (same 8 hashes). All French edits were made on top of that proven baseline, executed only through the build copy's single driver.

## 3. Pairing furniture (W43 RU×FR registry, verbatim; VOL follows this core)

- **Pairing badge (P1, brick #a4553a, 20pt bold, centred):** "TEXTES EN RUSSE · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES" — **REPLACING the y=372 subtitle in place** (975, 372), exactly as the shipped W43 ru-fr edition does. See §3a for the README #20 slot difference, recorded for the coordinator.
- **P1 edition line (W43 ru-fr pattern: first segment translated, topic keywords stay Russian):** "HEBDOMADAIRE RUSSE · VOL.2 · ПРАЗДНИК · СКИДКИ · ФУТБОЛ" (W43: "HEBDOMADAIRE RUSSE · VOL.1 · ПЕРВЫЙ СНЕГ · КАНИКУЛЫ · ДЕРБИ"). The W45 RU×EN/RU×DE editions kept the Russian line; the FR column follows its own W43 precedent.
- **Top strip centre:** "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · CHAQUE SEMAINE · LE RUSSE QUE LIT LA RUSSIE" (W43 ru-fr verbatim).
- **Footers (French, every page):** left "Lucerna · HEBDOMADAIRE RUSSE VOL.2 · TEXTE EN RUSSE · EXPLICATIONS EN FRANÇAIS" (singular TEXTE in the footer, as in W43) · right "Page N sur 8".
- **Gloss prefix:** "Note — " (W43 shipped gloss boxes; same as the W45 RU×EN prefix).
- **P8 answer separators:** kept as shipped in W43 RU×FR — "— СТРАНИЦА N —" (Russian form; the P8 answer-generation loop is otherwise byte-identical to the core, dash style kept — see §5).
- **Bilingual section heads** = Russian original · French short form (e.g. "ГЛАВНАЯ ТЕМА · Le thème principal", "НЕДЕЛЯ В ЦИФРАХ · En chiffres", "В ЭТОМ НОМЕРЕ · Sommaire", "СЛОВО НЕДЕЛИ · Mot de la semaine", "УПРАЖНЕНИЯ · Exercices de la page N", "ФРАЗЫ НЕДЕЛИ · Phrases de la semaine (mot pour mot, de cette édition)", "СЛЕДУЮЩАЯ НЕДЕЛЯ · La semaine prochaine (VOL.3)", "ТЕСТ И ОТВЕТЫ · Test et réponses", "ОТВЕТЫ · Réponses — classées par page ; cherchez votre numéro").
- **Contents table:** kept verbatim from the core, including the level tag "все" on the Стр. 8 row — exactly as the shipped W43 ru-fr edition keeps it (Russian level tag, not apparatus).
- **Captions and credits stay Russian by design** (as in W43 RU×FR); image payloads byte-identical to the core on every page.
- **P6 chart disclaimer (W43 ru-fr verbatim French sentence, appended to the Russian line):** "Un sondage d'exercice de la rédaction, pour s'entraîner — pas de vraies statistiques."

### 3a. Furniture difference recorded for the coordinator (README #20)

README #20's inserted-at-(975, 574), 22pt BRICK badge slot describes **FR as the target language** (FR/IT cores have no free subtitle slot because y=372 is frozen body strapline). It does **not** describe FR as the reader language on a Russian target. The RU target family's own shipped precedent — W43 RU×FR, verified in both its shipped SVG and its build source — replaces the y=372 subtitle in place at 20pt BRICK, and this edition follows that precedent, not the §20 generalization. No other furniture string deviates from the W43 ru-fr shipped SVG.

## 4. Freeze verification (rendered SVGs, this edition vs core)

- `tools/freeze.py diff` (`tools/scratch/diff-w45-ru-fr.json`): added CJK characters = **0** on all 8 pages; edition SVGs contain **0 CJK characters** total.
- **Cyrillic token-multiset diff per page (target-language proof):** P2–P8 exactly equal (counts 443/338/306/316/354/397/641 — the same counts ru-de/ru-en measured for the core). P1 differs by exactly the two documented furniture lines, itemized in full — no other Cyrillic token differs anywhere:
  - Badge replacement (y=372 subtitle removed): ЕЖЕНЕДЕЛЬНАЯ 1, ГАЗЕТА 1, ДЛЯ 1, ИЗУЧАЮЩИХ 1, РУССКИЙ 1, ЯЗЫК 1, НАСТОЯЩАЯ 1, РОССИЯ 1, ПО 1, РУССКИ 1 (the last two are the split of ПО-РУССКИ).
  - Edition-line first segment (y=330, §3): РУССКАЯ 1, ГАЗЕТА 1 (the second ГАЗЕТА of the P1 total of 2).
- All 8 P7 golden sentences occur exactly as in the core (Russian quotes byte-identical; only their French translations are new; page tags stay Russian "Страница N"). Bare-sentence counts on space-joined page text: 2× each in both core and edition.
- Changed-line parity vs the core build: bslib4 6, content12 150, content34 138, content56 158, content7 90, content8 104, svglib 0, render 6, run 0 — identical to the RU×EN changed-line set except content12 +2, which is exactly the edition-line pair (§3).

## 5. P8 answers (dash family; generation code byte-identical)

- `tools/p8.py compare` core vs edition: **CLEAN, 150 noted = 150 noted, missing = [], extra = [], uncertain = []**; keydiff = [83, 137, 138, 148].
- **137, 138 — documented re-aims (W43 translation precedent):** RU→FR items; Russian stems kept, instruction "Traduire en français"; keys are French in this edition (137 "Mercredi 4 novembre, c'est un jour férié."; 138 "Un code promo est un code de réduction."). 139/140 are the reverse direction (French prompts, "Traduire en russe", keys Russian byte-identical); 150 is the writing apparatus line ("(Question ouverte — texte modèle ci-dessous)" / "Le texte modèle se trouve dans la section H de cette page (84 mots)"), model text unchanged Russian.
- **83, 148 — p8.py extraction artifacts, NOT key changes (README #13 lesson applied):** the tool's paren branch treats a trailing paren group as part of the extracted "key" in one edition but not the other. Printed keys are identical in both SVGs. Verified by an independent dash-parse of all 150 printed P8 lines (split on the first " — "): **key diffs = [137, 138] only**; counts 150 = 150, no missing/extra. All other keys byte-identical; notes translated (note-only diffs, keys unchanged).
- French notes use half-width parentheses throughout (edition P8 full-width paren count = 0, vs core 6 in Chinese notes); the answer-generation loop format (`N. key — note`, writing items `N. ✓ note`) is unchanged from the core, with the type-string comparison already rewritten to "Rédaction" by the global type mapping.
- P8 keys flow ends at y=2375 (rule at 2580) — ample clearance.

## 6. Gloss counts (split on `·` itself, README #21)

9 gloss() calls, **26 items** — per-call counts identical to the core (content12: 3/3/3; content34: 3/3/3; content56: 3/2/3). No gloss item was added, dropped, or merged in translation.

## 7. Geometric audit (mandatory SOP gate — builder run)

- `tools/occlusion_audit.py`: selftest OK (all 6 planted classes fire, clean controls silent). **Final run: 0 flags on all 8 pages; core control 0 flags; NEW vs core: 0.**
- **Same-baseline ink scan (README #10):** all pages 0 flags at <5 px gaps (advance-width extents), including the P1 top band and the badge row, in both core and edition.
- **Chart page (P6) element check (README #12):** all 4 bar labels (Дома с семьёй, Короткая поездка, Ярмарка или концерт, Просто выспятся) and all 4 values (34/28/22/16) at core-identical positions, with **zero** later-drawn rect overlaps in both core and edition. The RU P6 chart has no ES-style frozen overprint — 0 overlaps is the correct, expected result, not a missed defect.
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final run. Cards P1, P6, P7 viewed by the builder after the final render; P2–P5, P8 covered by the audits + Cyrillic diff.
- P7 col3 ends at **1727.58 — exactly the core's value** (see §9 for how that was restored).

## 8. Fit shortenings (French apparatus only — no core geometry or Russian moved)

Three French strings were shortened during the build; each keeps its full meaning, and the shortened form is what ships:

1. **P7 error-clinic note #1** (2 lines → 1): "Instrumental après « с » : с Днём единства." (391.6 px > 390 inner width) → "« с » + instrumental : с Днём единства." (351.7 px). The grammar point and the full example survive.
2. **P7 word-box note** (2 lines → 1): "промокод = code promo, à saisir à la caisse." (408.6 px) → "промокод = code promo à la caisse." (334.3 px). The checkout meaning survives; the Russian head text already says the code is entered when buying.
3. **P1 word-of-the-week para** (2 lines → 1): "сокращённый день = une journée de travail raccourcie." (491.5 px > 434) → "сокращённый день = une journée raccourcie." (405.2 px). Without this fix the first occlusion run reported the edition's only NEW flag: a LINEX where the fixed 1844 rule crossed the wrapped second line "raccourcie." — a real fan-out defect (README #15: a fan-out's own text must be shortened even when the core shows no flag). The full form "journée de travail raccourcie" is kept on P2 (words strip) and P7 (bridge), so no information is lost anywhere in the issue. After the fix the audit reads 0 flags.
- Together, fixes 1+2 restore P7 col3 from 1783.1 back to exactly 1727.58 (see §9); fix 3 clears the P1 LINEX.

## 9. Readers' corner — no fabrication (disclosure + example kept, explanation layer only translated)

P7 prints the core's editor's example unchanged (Russian, "— М. (пример от редакции)") and the core's Russian disclosure unchanged, plus the French disclosure line ("Aucune lettre réelle reçue — exemple de la rédaction ; promesse pour VOL.3.", 2 lines, same line count as the Chinese line it replaces). No new reader, letter, name, or quote was invented. The VOL.3 teaser repeats the call for letters, as in the core.

**Geometry (coordinator-adjudicated pattern, kept frozen, not re-engineered):** P7 letters-box bottom 1727.58 and disclosure line-2 baseline 1738.28 are **identical in core and edition** (all three col-3 boxes: errors 200–1008.08, word 1020.08–1242.58, letters 1254.58–1727.58, byte-identical rects). The box is drawn before the text, so the text stays fully readable, and the canonical occlusion audit reports 0 flags for both editions — the same disposition as the RU×EN precedent, whose coordinator adjudication (2026-10-27) accepted this core-inherent contact as non-blocking. This edition adds zero displacement; any re-flagging should check geometry against the core first.

## 10. Images & credits (byte-identical payloads; credits identical to the core)

| Page | Image | Credit (as printed) |
|---|---|---|
| P1 | November park photo (autumn_path.jpg, reused from W43) | Фото: Toxer427 — лицензия CC0 (Wikimedia Commons) |
| P4 | 1912 football photo (football1912.jpg, reused from W43) | Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons) |
| P5 | Market photo (market.jpg) | Фото: Престон Керес (USDA) — общественное достояние (Wikimedia Commons) |

Image licensing verification is the core's (W45 RU core KIT §4); this edition changes no image. P2, P3, P6, P7, P8 carry no embedded photos in either edition. Data-URI hashes match the core on P1/P4/P5.

## 11. Facts (identical to the core)

Split week (2–3 Nov work, 4 Nov Wednesday holiday, 3 Nov one hour shorter, school-holiday tail to 4 Nov), 11.11 sale 22 Oct – 12 Nov (attributed trade-press note only), RPL round 14 6–8 Nov (Krasnodar–CSKA Sat 19:30 Ozon Arena; Spartak–Akron Sun 16:15; round-13 closer Mon 2 Nov; pause until 20 Nov), reported past events only (CSKA–Spartak 2:0 on 25 Oct; first snow forecast failed; 28 Oct Grandparents Day; 31 Oct Halloween). Russian domestic life only; no politics. The P6 chart is labeled practice data in both languages ("УЧЕБНЫЕ ДАННЫЕ · Données d'exercice" + "Это учебный опрос редакции для упражнений — не настоящая статистика. Un sondage d'exercice de la rédaction, pour s'entraîner — pas de vraies statistiques."), bars 34/28/22/16 as the core.

## 12. Files

- `files/weekly-report-w45-ru-fr/svg/` — 8 final SVGs (sha256: p1 d513d03e…, p2 48003025…, p3 d3d1a8ef…, p4 28f872c0…, p5 df751ed5…, p6 697b64a8…, p7 c5f43b47…, p8 66e4d713…)
- `files/weekly-report-w45-ru-fr/cards/` — 8 cards (1950×2700 PNG)
- `files/weekly-report-w45-ru-fr/Lucerna-VOL2-FR.pdf` — print PDF, 8 pages, **13,518,341 bytes**, sha256 `3bfa593e86e2a2479e46943e0b7aecdacb5b5f843755918b169ce01fd4cb0d0f`
- `files/weekly-report-w45-ru-fr/Lucerna-VOL2-FR-web.pdf` — web PDF, 8 pages, **3,197,163 bytes** (< 10 MB), sha256 `df56e15e4fb717a1e827456ada2e62bcec1d8bb9bb70a9eacb785867c940d71e`
- `files/weekly-report-w45-ru-fr/WEEKLY-KIT.md` — this file
- `files/weekly-report-w45-ru-fr/ABSTRACT.txt` — one-line French abstract, no ASCII double quotes
- Build: `hidden_files/weekly-report-w45-ru-fr-build/` (run.py → render.py; transform script at `tools/scratch/transform-w45-ru-fr.py`; verification scripts at `tools/scratch/verify-w45-ru-fr.py`, `tools/scratch/check-w45-ru-fr-p6-baseline.py`, `tools/scratch/check-w45-ru-fr-extra.py`; final run log at `tools/scratch/run-w45-ru-fr2.log`)

## 13. Build notes (transform recovery, for the next builder)

- The global pass runs before per-file pairs, so any per-file old string containing a global pattern must be written in its POST-global form — the same three cases as RU×EN: the P2 letter line ("你呢？Mercredi 4 novembre你怎么过？…"), the P7 quote 1 ("Mercredi 4 novembre，是工作周中间的休息日。"), and the P8-E key 137 ("Mercredi 4 novembre放假。"). The transform script handles these; the global Chinese-old list is identical to the RU×EN script's so the post-global forms match exactly.
- The mid-build service restart (2026-10-27 ~18:48 UTC) interrupted a combined edit+render command after run.py had completed but before render.py finished: the state was verified before retrying (both content12 edits present, P1 SVG refreshed, PDFs still at the pre-fix timestamp), then render.py alone was re-run to regenerate cards/PDFs. The interrupted run's own log was checked and shows the full run had completed (ALL DONE, P7 col3 1727.58) before the restart, and all 8 SVGs were re-verified afterwards (freeze diff, Cyrillic multiset, p8, occlusion) — no half-written artifact survived into the final deliverables.
- The svglib.py "重阳" hit in a CJK scan is a pre-existing English docstring in the core's own svglib (line 120, identical in core/ru-en/ru-fr builds), not rendered text; rendered edition SVGs contain 0 CJK characters.

## 14. Delivery status

Builder-complete, NOT proofread-finalized, NOT pushed, NOT posted: per the task brief, repo insertion is done by the parent line (serialized) and independent proofread is still pending. No git push, no Discord post, no user message, no cron was made from this build. Weekly-git was not touched.

## 15. Coordinator adjudication (2026-10-27, documentation only, no render change)

- Independent proof (hidden_files/w45/ru-fr-proof/REPORT.md): ZERO PROBLEMS, cleared to finalize. Badge slot single item ACCEPTED as-is: edition badge (975,372) 20pt bold #a4553a in-place replacement is byte-consistent with W43 shipped ru-fr; README #20's (975,574) 22pt insert describes French-as-target, not this edition. This matches the standing RU slot rule (372 family: ru-en/ru-fr/ru-it/ru-pt; 574 family: ru-de/ru-es). Future RU×FR proofs must NOT re-flag badge slot. FINALIZED.
