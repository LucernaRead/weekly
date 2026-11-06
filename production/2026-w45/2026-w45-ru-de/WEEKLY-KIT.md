# Lucerna — Русская газета VOL.2 · RU × DE (俄语正文 + 德语讲解版，W45)

**Edition:** Russian text + **German** explanations (target RU × reader-native DE), for German-speaking learners of Russian.
**Week:** Mon 2 – Sun 8 Nov 2026 (VOL.2, same issue week as the finalized W45 core).
**Masthead:** **Lucerna** (no article, per SOP masthead rule — Russian is article-less). Page size 1950×2700, 8 pages, warm ivory.
**Status: BUILDER-COMPLETE, NOT independently proofread.** No Discord post, no chat card/PDF dump, no repo push, no cron was made from this build. Independent proofread is the parent's next step.

Source: the finalized W45 Russian core (`files/weekly-report-w45-ru-core/`, itself the zh-cn edition). Build copied to `hidden_files/weekly-report-w45-ru-de-build/`; the core's own directories were never edited (core SVGs re-hashed after all work: identical to the baseline hashes in §2). Method = the W43 RU×DE sibling pattern: rewrite the explanation layer only, freeze everything Russian. Transform script (exact-literal replacements, asserted per string): `tools/scratch/transform-w45-ru-de.py`.

---

## 1. Totals (registry-derived, identical to the core)

- **150 exercises** — A2 51 · B1 75 · B2 24; per page 10/18/18/18/18/18/12/38 (same as core).
- Writing model (P8 §H): **exactly 84 words**, unchanged Russian text; the "80–100 слов" task range unchanged.
- Registry `type` strings were localized to German inside this build's registry only (Ausfüllen 54 · Ankreuzen 42 · Zuordnen 20 · Sätze bilden 12 · Umformen 4 · Lückentext 13 · Übersetzen 4 · Schreiben 1 — counts identical to the core); type strings never print.
- Exercise instructions localized per the W43 RU×DE pattern (Ausfüllen / Sätze bilden / Umformen / Ins Deutsche übersetzen / Ins Russische übersetzen / Paare zuordnen).

## 2. Baseline reproduction (before any edit)

The unmodified copy of the core build regenerated all 8 SVGs **byte-identical** to the shipped core SVGs (`tools/freeze.py baseline`, `tools/scratch/baseline-w45-ru-de`):

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

Core integrity: shipped core SVGs re-hashed after all build work — unchanged (same 8 hashes). All German edits were made on top of that proven baseline, executed only through the build copy's single driver (`run.py` → `render.py`, one process).

## 3. Pairing furniture (W43 RU×DE registry, verbatim; VOL follows this core)

- **Pairing badge (P1, brick red #a4553a, 22pt bold, centred):** „RUSSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER" — **INSERTED at (975, 574)** per the RU-core family slot (README #20 family precedent), NOT the EN/DE/ES subtitle slot: the core's Russian subtitle at y=372 stays untouched. Measured span 452.0–1498.0 (width 1045.9); clear of the dark band above (ends 542) and the headline head below (baseline 606). Visually confirmed on the P1 card.
- **Top strip centre:** „КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · JEDE WOCHE · RUSSISCH, WIE RUSSLAND ES LIEST" (W43 RU×DE verbatim).
- **Footers (German, every page):** left „Lucerna · RUSSISCHE WOCHENZEITUNG VOL.2 · TEXT AUF RUSSISCH · ERKLÄRUNGEN AUF DEUTSCH" · right „Seite N von 8".
- **Gloss prefix:** „HINWEIS · " (tables.json DE column + W43 shipped SVGs).
- **P8 answer separators:** kept as shipped in W43 RU×DE — „— СТРАНИЦА N —" (Russian form; the P8 answer-generation loop is otherwise byte-identical to the core, dash style kept — see §5).
- **Bilingual section heads** = Russian original · German short form (e.g. „УПРАЖНЕНИЯ · Übungen zu Seite N", „ГЛАВНАЯ ТЕМА · Das Hauptthema", „НЕДЕЛЯ В ЦИФРАХ · Zahlen", „В ЭТОМ НОМЕРЕ · Inhalt", „ФРАЗЫ НЕДЕЛИ · Sätze der Woche (wörtlich aus dieser Ausgabe)", „СЛЕДУЮЩАЯ НЕДЕЛЯ · Nächste Woche (VOL.3)").
- **Captions and credits stay Russian by design** (as in W43 RU×DE); image payloads byte-identical to the core on every page.

## 4. Freeze verification (rendered SVGs, this edition vs core)

- `tools/freeze.py diff` (`tools/scratch/diff-w45-ru-de.json`): added CJK characters = **0** on all 8 pages; edition SVGs contain **0 CJK characters** total.
- **Cyrillic token-multiset diff per page (target-language proof):** P2–P8 exactly equal (counts 443/338/306/316/354/397/641). P1 differs by exactly **one** token: core „все" → edition „alle" — the contents-table level tag for page 8, German apparatus, not target text. No other Cyrillic token differs anywhere.
- All 8 P7 golden sentences occur exactly as in the core (Russian quotes byte-identical; only their German translations are new; page tags stay Russian „Страница N").

## 5. P8 answers (dash family; generation code byte-identical)

- `tools/p8.py compare` core vs edition: **CLEAN, 150 noted = 150 noted, missing = [], extra = [], uncertain = []**; keydiff = [83, 137, 138, 148].
- **137, 138 — documented re-aims (W43 translation precedent):** RU→DE items; Russian stems kept, instruction „Ins Deutsche übersetzen"; keys are German in this edition (137 „Am Mittwoch, dem 4. November, ist frei."; 138 „Ein Promocode ist ein Rabattcode."). 139/140 are the reverse direction (German prompts, „Ins Russische übersetzen", keys Russian byte-identical); 150 is the writing apparatus line („(offene Aufgabe — Mustertext unten)" / „Der Mustertext steht in Abschnitt H dieser Seite (84 Wörter)"), model text unchanged Russian.
- **83, 148 — p8.py extraction artifacts, NOT key changes (README #13 lesson applied):** the tool's paren branch treats a trailing half-width paren group as part of the extracted "key", while the core's fullwidth parens are not. Printed keys are identical in both SVGs (83: „83. B — …"; 148: „148. A — …"). Verified by an independent dash-parse of all 150 printed P8 lines (split on the first „ — "): **key diffs = [137, 138] only**; counts 150 = 150, no missing/extra.
- German notes use half-width parentheses throughout (W43 RU×DE typography); the answer-generation loop format (`N. key — note`, writing items `N. ✓ note`) is unchanged from the core, with only the type-string comparison adapted to „Schreiben" as in W43.
- P8 keys flow ends at y=2361 (rule at 2580) — ample clearance.

## 6. Gloss counts (split on `·` itself, README #21)

9 gloss() calls, **26 items** — per-call counts identical to the core (content12: 3/3/3; content34: 3/3/3; content56: 3/2/3). No gloss item was added, dropped, or merged in translation.

## 7. Geometric audit (mandatory SOP gate — builder run)

- `tools/occlusion_audit.py`: selftest OK (all 6 planted classes fire, clean controls silent). **Final run: 0 flags on all 8 pages; core control 0 flags; NEW vs core: 0.**
- **One real defect found and fixed during production (P7):** the first render's German readers'-corner disclosure (5 lines vs the core's 2) plus the 2-line word-box gloss pushed the letters box to y=1843.58, crossing the phrases rule at y=1756 (1 NEW LINEX flag). Fix (explanation layer only, no target text moved): disclosure shortened to 2 lines („Keine echten Briefe und Texte — Beispiel der Redaktion; Versprechen für VOL.3." — the full disclosure still stands in Russian in the same box) and the word-box gloss shortened to one line („промокод = Rabattcode." — the Russian definition above it already says the code is entered at purchase). Final P7 col3 ends at **1727.58 — exactly the core's value, 28.4 units clear** of the rule. Visually confirmed on the P7 card.
- **Same-baseline ink scan (README #10):** all pages 0 flags at <5 px gaps (advance-width extents), including the P1 top band and the badge row.
- **Chart page (P6) element check (README #12):** zero text elements overlapped by any later-drawn rect; all four bar labels and values fully visible on the card (bars 34/28/22/16 as the core).
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final run. Cards P1, P2, P6, P7, P8 viewed by the builder after the final render; P3–P5 covered by the audits + Cyrillic diff.

## 8. Re-aimed items (the only key/prompt changes — translation pedagogy)

| # | Change | Key in this edition |
|---|---|---|
| 137 | RU→DE: Russian stem kept; instruction „Ins Deutsche übersetzen" | „Am Mittwoch, dem 4. November, ist frei." (note: Vergleichen Sie Seite 3) |
| 138 | RU→DE: Russian stem kept; instruction „Ins Deutsche übersetzen" | „Ein Promocode ist ein Rabattcode." (note: Vergleichen Sie Seite 5) |
| 139 | Prompt now German: „Am Samstag spielt Krasnodar gegen ZSKA. → ___"; instruction „Ins Russische übersetzen" | Russian sentence, **byte-identical** (note: Achten Sie auf: играть + с + Instrumental) |
| 140 | Prompt now German: „Ich wünsche allen einen schönen Tag der Volkseinheit! → ___"; instruction „Ins Russische übersetzen" | Russian sentence, **byte-identical** (note: поздравляю + с + Instrumental) |
| 150 | Registry line is German apparatus | „(offene Aufgabe — Mustertext unten)"; note „Der Mustertext steht in Abschnitt H dieser Seite (84 Wörter)" |

All other 145 keys byte-identical to the core (verified by the §5 dash-parse).

## 9. Readers' corner — no fabrication (disclosure + example kept, explanation layer only translated)

P7 prints the core's editor's example unchanged (Russian, „— М. (пример от редакции)") and the core's Russian disclosure unchanged, plus the German disclosure line (§7). No new reader, letter, name, or quote was invented. The VOL.3 teaser repeats the call for letters, as in the core.

## 10. Images & credits (byte-identical payloads; credits identical to the core)

| Page | Image | Credit (as printed) |
|---|---|---|
| P1 | November park photo (autumn_path.jpg, reused from W43) | Фото: Toxer427 — лицензия CC0 (Wikimedia Commons) |
| P4 | 1912 football photo (football1912.jpg, reused from W43) | Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons) |
| P5 | Market photo (market.jpg) | Фото: Престон Керес (USDA) — общественное достояние (Wikimedia Commons) |

Image licensing verification is the core's (W45 RU core KIT §4); this edition changes no image.

## 11. Facts (identical to the core)

Split week (2–3 Nov work, 4 Nov Wednesday holiday, 3 Nov one hour shorter, school-holiday tail to 4 Nov), 11.11 sale 22 Oct – 12 Nov (attributed trade-press note only), RPL round 14 6–8 Nov (Krasnodar–CSKA Sat 19:30 Ozon Arena; Spartak–Akron Sun 16:15; round-13 closer Mon 2 Nov; pause until 20 Nov), reported past events only (CSKA–Spartak 2:0 on 25 Oct; first snow forecast failed; 28 Oct Grandparents Day; 31 Oct Halloween). Russian domestic life only; no politics. The P6 chart is labeled practice data in both languages („УЧЕБНЫЕ ДАННЫЕ · Übungsdaten" + „Das sind Übungsdaten der Redaktion, keine echte Statistik."), bars 34/28/22/16 as the core.

## 12. Files

- `files/weekly-report-w45-ru-de/svg/` — 8 final SVGs
- `files/weekly-report-w45-ru-de/cards/` — 8 cards (1950×2700 PNG)
- `files/weekly-report-w45-ru-de/Lucerna-VOL2-DE.pdf` — print PDF, 8 pages, **13,557,259 bytes**
- `files/weekly-report-w45-ru-de/Lucerna-VOL2-DE-web.pdf` — web PDF, 8 pages, **3,222,331 bytes** (< 10 MB)
- `files/weekly-report-w45-ru-de/WEEKLY-KIT.md` — this file
- `files/weekly-report-w45-ru-de/ABSTRACT.txt` — one-line German abstract
- Build: `hidden_files/weekly-report-w45-ru-de-build/` (run.py → render.py; transform script at `tools/scratch/transform-w45-ru-de.py`)

## 13. Delivery status

Builder-complete, NOT proofread-finalized, NOT pushed, NOT posted: per the task brief, repo insertion is done by the parent line (serialized) and independent proofread is still pending. No git push, no Discord post, no user message, no cron was made from this build.
