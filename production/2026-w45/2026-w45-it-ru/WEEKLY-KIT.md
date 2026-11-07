# WEEKLY-KIT — Lucerna Weekly W45 · IT × RU

**Edition:** Italian-target × Russian-native · **Issue week:** Mon 2026-11-02 – Sun 2026-11-08 ·
**Volume:** VOL.2 · **Masthead:** La Lucerna · **Build status: builder-complete, NOT finalized**
(independent proofread still required before delivery).

**Delivery directory:** `files/weekly-report-w45-it-ru/`
**Build directory:** `hidden_files/weekly-report-w45-it-ru-build/`
**Core (read-only source):** `files/weekly-report-w45-it-core/` (VOL.2, 8 pages, 150 exercises)

## 1. Spec

- Italian body text frozen from the W45 IT core; only the explanation layer is localized,
  fully into Russian. No Italian body string was removed (see §2).
- 150 exercises: A2 47 / B1 70 / B2 33; per page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- P8 model text 81 words, byte-identical to the core (see §10).
- Core themes: first cold snap of November; 2 November Commemorazione dei defunti;
  Panettone World Cup final, Milan, 7–8 November; Festa del Torrone, Cremona (to 22 November);
  Serie A matchday 11. P7 word box: LA PAROLA «l'assaggio». P7 golden sentences: 8.
- Readers' corner: editor's example letter + VOL.3 open invitation; no real letters exist.
- The banned bridge-term appears 0 times in every deliverable (SVG, cards, PDFs, KIT, ABSTRACT).

## 2. Freeze check (core vs edition)

**Core baseline reproduced 8/8 byte-identical** (`tools/freeze.py baseline`, 2026-10-27):

| page | core sha256 (first 16) |
|---|---|
| p1 | `81051bbb0799fafe` |
| p2 | `d42ce9aedc445111` |
| p3 | `9e45586d3187ec8e` |
| p4 | `62f75269d2878cd0` |
| p5 | `c907b869e4cda01e` |
| p6 | `5545f8ddae0dab5a` |
| p7 | `9fc999f45c9826e6` |
| p8 | `3b87e54f30b6c050` |

Core re-hashed at the end of this build (2026-10-27): all 8 hashes unchanged —
the core was not modified. (Full hashes in `build/freeze-baseline/` and §15.)

**Freeze diff, R2 SVGs** (`tools/freeze.py diff`, output `freeze-diff-r2.json/.txt`):

| page | added strings | removed strings | core CJK → edition CJK | added CJK |
|---|---|---|---|---|
| p1 | +27 | −26 | 193 → 0 | 0 |
| p2 | +35 | −29 | 179 → 0 | 0 |
| p3 | +34 | −31 | 169 → 0 | 0 |
| p4 | +29 | −25 | 145 → 0 | 0 |
| p5 | +46 | −35 | 215 → 0 | 0 |
| p6 | +31 | −24 | 149 → 0 | 0 |
| p7 | +44 | −41 | 319 → 0 | 0 |
| p8 | +175 | −174 | 1034 → 0 | 0 |

Total added CJK characters: **0**. (P1 +27 vs the R1 +28 is the fix-round-2
parola-note re-wrap: the 2-line note became 1 line, i.e. one fewer added text node;
the removed set is unchanged from R1.)

**Removed-string adjudication (R1, unchanged in R2 except as noted above):**
every removed string contains Chinese (explanation layer only), EXCEPT:
- p6 `bollettino · modello` — a re-wrap fragment (same class as the DE sibling's p6 adjudication);
- p7 `è probabile che / è possibile che / bisogna` — a re-wrap fragment
  (same as the DE sibling's p7 adjudication);
- p8 full-width-colon/paren punctuation-form lines for items 103, 17, 18, 19, 20, 60, 61
  (keys identical; only `：`→`:` / `（）`→`()` in translated notes, same class as DE's p8);
- p8 `— PAGINA N —` ×8 — intentionally replaced by `— СТРАНИЦА N —`
  per the W43 IT×RU furniture precedent (see §3).
No Italian body string was removed.

## 3. Furniture three-way check (edition / W43 shipped IT×RU / README)

W43 shipped SVGs (`files/weekly-report-it-ru/`) govern over README §20 generalizations.
All W43 IT×RU furniture strings are used verbatim, with VOL.2 for the W45 issue:

| element | edition string | W43 source |
|---|---|---|
| Badge (P1) | `ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ` | W43 IT×RU verbatim |
| Footer (all 8 pages) | `La Lucerna · ИТАЛЬЯНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ` | W43 form, VOL.2 (W43 said VOL.1) |
| Page line | `Страница N из 8` | W43 IT×RU verbatim |
| Gloss prefix | `Пояснение — ` | W43 IT×RU verbatim |
| P8 separators | `— СТРАНИЦА N —` | W43 IT×RU verbatim (DE kept PAGINA per its own W43 precedent; the pair precedent governs) |
| Section heads | VITA · ЖИЗНЬ, CULTURA · КУЛЬТУРА, SPORT · СПОРТ, GIOVANI · МОЛОДЁЖЬ, APPROFONDIMENTO · РАЗБОР, LINGUA · ЯЗЫК; LA NOTIZIA · ГЛАВНАЯ НОВОСТЬ; LA SETTIMANA IN CIFRE · ЦИФРЫ; LA FRASE PER RICORDARE · ПАМЯТКА; ERRORI TIPICI · ОШИБКИ; LA PAROLA · СЛОВО НЕДЕЛИ; FRASI DELLA SETTIMANA · ФРАЗЫ НЕДЕЛИ (дословно из статей выпуска); LA PROSSIMA SETTIMANA · В СЛЕДУЮЩЕМ ВЫПУСКЕ (VOL.3); VALUTAZIONE E RISPOSTE · ПРОВЕРКА И ОТВЕТЫ; RISPOSTE · ОТВЕТЫ — по страницам: ищите по номеру задачи; right line `К каждой задаче — пояснение · ✓ — задание с образцом`; exercise heads `ESERCIZI · УПРАЖНЕНИЯ СТРАНИЦЫ N`; right line `Ответы — на странице 8 · уровни смешаны: ищите по номеру` | W43 IT×RU forms |
| Instruction words | Вставьте (填空）, Составьте предложение (造句）, Переведите (翻译）, Верно или нет (判断）, Напишите (写作）, Соедините пары (把词和释义配对）; `E TU? · А ВЫ?` | W43 IT×RU forms |
| P1 strap | `OGNI SETTIMANA IN ITALIANO · ИТАЛЬЯНСКИЙ, КОТОРЫЙ ЧИТАЮТ ИТАЛЬЯНЦЫ` | W43 RU verbatim |
| P1 330 line | `ИТАЛЬЯНСКИЙ · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A` | W43 form, VOL.2 |
| P1 band right | `НА ЭТОЙ НЕДЕЛЕ ПРИХОДИТ ПЕРВЫЙ ХОЛОД` / `Неделя первого холода · см. страницу 2` | W43 RU form |

**Badge geometry deviation (documented for the proofreader):**
W43 IT×RU placed its badge at y=372, 20 pt, replacing the W43 core's y=372 line.
The W45 core's y=372 line is frozen Italian body strapline
(`IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA`),
so it cannot be replaced without breaking the freeze gate. This build instead inserts
the W43 string at **y=574, 22 pt bold BRICK, centered (x=975)** — exactly like the
W45 IT×DE / IT×EN / IT×FR siblings (dark band bottom 542 → badge 574 → headline 606,
displaces nothing). Measured width at 22 pt bold: 1164.25 px, inside the frame.
Verified present on P1 in SVG and in the print PDF (space-stripped text extraction).

**Footer geometry (measured, ADVANCE method):** left string ends at x=1155.1,
right page line starts at x=1731.8, gap **576.7 px**. Footer + page line verified
present on all 8 pages in both SVG and print PDF.

**Frozen Italian cross-references kept:** the 4 `(Pagina N)` references inside P1/P2
body text are frozen Italian and stay (frost caption `(Pagina 2)`, IN BREVE
`(Pagina 2)`, `(Pagina 5)`, `(Pagina 3)`). Only P7 quote tags use `Страница`.

## 4. P7 word-box hard gate — PASSED

The Italian definition sentence is byte-frozen and was NOT localized.
Source line identical in core and RU `content7.py`:
`« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone.`
Only the gloss note below it was localized, final form (1 line):
`assaggio = дегустация (стр. 3).`
All P7 `«…»`-starting text nodes are byte-identical between core and edition SVGs.

## 5. Readers' corner — disclosure mapping

Coordinator clarification (2026-10-27, supersedes the original task wording):
the W45 IT core's Italian side has NO disclosure sentence to keep — its Italian
elements are only the letter verbatim + `(esempio della redazione)` label + preview
promise, and the deferral disclosure itself was Chinese in the core (the core's
reader-native language). Therefore the disclosure sentence is written in the reader's
language only (Russian); NO new Italian disclosure sentence was invented
(the core has none, W43 has none, shipped IT×DE has none, and P7 col3 has no room).
The same point in IT×EN proofread was already ruled non-blocking (item B1).

Kept frozen (Italian): the letter verbatim (`«Ciao! Sono Li, studio italiano a
Pechino. Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone —
almeno in foto!» — Li (esempio della redazione)`) and the preview band's Italian
promise line (not counted as the invitation).

Printed Russian disclosure (P7 letter box, 3 lines at 20 pt / 390 px):
`Пример редакции, а не настоящие письма; лучшего текста со страницы 8 нет. Напишите нам — лучшие в VOL.3!`
— covers (1) no real letters, (2) no best P8 writing, (3) editor's example +
VOL.3 deferral/promise, plus an imperative invitation with a VOL.3 publication
promise. No reader, letter, name, or quotation was fabricated as real.

## 6. Gloss distribution (source `gloss()` strings split on bare `·`, core 1:1)

| page | count | headwords |
|---|---|---|
| P2 | 6 | il cappotto · la sciarpa · i guanti · a strati · il termosifone · il crisantemo |
| P3 | 5 | il panettone · il torrone · l'assaggio · la bancarella · il cantiere |
| P4 | 4 | la giornata · la presentazione · gli spalti · la sera |
| P5 | 4 | il cosplay · gratuito · il documentario · lo schermo |
| P6 | 5 | la probabilità · la media · il modello · il bollettino · aggiornare |
| **Total** | **24** | |

Every headword verified present in the rendered RU SVGs' gloss strings.
P1 bridge word list (separate from `gloss()`): 4 items, 1:1
(`primo freddo · versante adriatico · previsione · assaggi`).

## 7. P8 gate — CLEAN, 150 = 150

`tools/p8.py compare` on the R2 SVGs (explicit core/edition paths):
**CLEAN — 150 noted = 150 noted, missing=[], extra_count=0, uncertain=[].**
P8 answer notes contain 0 CJK items; the printed note set equals the core's
(stronger than acceptable EXTRA_ONLY).

**Keydiff (15 items, same list as the W45 IT×DE sibling):**
`[6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 102, 137, 138, 139]`

- The 12 items 6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 102 are paren-branch
  pseudo-diffs — printed keys byte-identical to the core
  (`previsioni`, `guanti`, `crisantemi`, `termosifoni`, `fa`, `resta`, `mandorle`,
  `più bella`, `gratuiti`, `castagne`, `ci sarà`, `fa`); only the note is translated
  and brackets switch full-width→half-width (W43 family form).
- The 3 true re-aims are legal translation-item re-aims (section E, Italian→Russian,
  following W43 IT×RU + W45 IT×DE precedent):
  - 137: core `周一第一场寒冷来了。 — 对照原文` → RU `В понедельник приходит первый холод. — См. оригинал`;
  - 138: core `观众可以免费品尝。 — assaggiare gratis = 免费品尝` → RU `Публика может пробовать бесплатно. — gratis = бесплатно`;
  - 139: core `周日晚上，佛罗伦萨对尤文图斯。 — si gioca = 进行比赛` → RU `«Фиорентина» — «Ювентус» в воскр. веч. — si gioca = играют`.
- Item 140 keeps its Italian key (`Ogni previsione deve essere chiara.`,
  note translated to `dovere = должен, нужно`) and is NOT in keydiff.
- Item 150 prints `✓ Образец — в разделе H этой страницы (81 слово)`.

## 8. Geometry gates

- **Occlusion audit** (`tools/occlusion_audit.py`, selftest first: all 6 planted classes
  fired, clean controls silent): edition **0** flags, core **0** flags, NEW vs core **0**.
  Output: `occlusion-r2.json/.txt`. R0 had 49 NEW flags (overflow cascades); R1 had 2 NEW
  flags (fixed in round 2); R2 is clean.
- **Flow ends (R2, no `!!` warnings):** P1-headline 1497/1828, P1-freddo 2264/2290,
  P1-quiz 2491/2540, P2 col3 1054.0, P2-ex 2389/2580, P3 col3 1281.25, P3-ex 2497/2580,
  P4 col3 904.0, P4-ex 2456/2580, P5 col3 1285.75, P5-ex 2377/2580, P6 col3 1096.5,
  P6-ex 2569/2580 (same as core), P7 col3 1646.0 (40 px clear of the FRASI rule at 1686),
  P8-ex 965/1332, P8-keys 2484/2552.
- **Right-edge scan (ADVANCE method, PIL advance widths per anchor, band [40, 1910]):**
  **0 flags** on all 8 pages (masthead UnifrakturMaguntia exempt: different font metrics;
  masthead visually confirmed in the P1 card).
- **Same-baseline ink collision scan** (furniture bands incl. P1 top band y=92 and every
  footer y=2624): **0 overlaps**.
- **Frame-line scan:** all 8 pages carry both frame rects (28/40) and the footer rule at 2580.
- **P6 chart-label coverage** (baseline-anchored ink method, PIL `getmetrics`, anchor `ls`,
  later-drawn rects vs label ink; threshold <30%): **maximum 0.0%**
  (Torino/Milano/Bologna/Roma/Napoli labels + value labels 3°/4°/5°/9°/12° + captions).
- **Visual inspection:** all 8 cards inspected page by page (p1-prima, p2-vita, p3-cultura,
  p4-sport, p5-giovani, p6-approfondimento, p7-lingua, p8-valutazione) — no overflow,
  overlap, footer-clearance, frost-drawing, fixture-table, chart, col3-vs-FRASI-rule,
  or answers-bottom defect. P6 chart bars clear of labels; P7 col3 ends 40 px above the
  FRASI rule; P8 answers end well above the footer.

## 9. Independent counts (from the rendered R2 SVGs, not the registry)

Exercise numbers extracted from P1–P7 SVGs + the P8 exercise region
(chip level text paired with its following `N.` / `N–M.` node, ranges expanded):
**exactly 1–150, no missing, no duplicates; levels A2 47 / B1 70 / B2 33;**
per page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38 — identical to the core and the registry.

## 10. Model text

Extracted from both P8 SVGs (16 pt serif, last column, after `Testo modello:`):
**81 words, byte-identical to the core.**
Text: `Lunedì 2 novembre metto il cappotto e la sciarpa: arriva il primo freddo e la
mattina è pungente. A scuola parliamo del Forum Cultura di Milano e del Festival dei
Popoli di Firenze. Sabato assaggio il panettone con la mia famiglia: preferisco quello
tradizionale, con i canditi. Domenica sera guardiamo Fiorentina–Juventus in televisione.
Il freddo è arrivato, ma la settimana è dolce: cultura, dolci e calcio, come nel
giornale. Lunedì prossimo racconto tutto alla classe, con le parole nuove del freddo.`
(The label-inclusive count is 83 including `Testo modello:` per the DE sibling's method;
the 81-word count is the model body, matching the core's brief 80–100.)

## 11. Residual scans (R2 deliverables)

- Banned term: **0** everywhere (SVGs, KIT, ABSTRACT).
- CJK characters in the 8 edition SVGs: **0**.
- Leftover German strings: `Mailand` 0, `Kostprobe` 0, `Seite ` 0, `HINWEIS` 0,
  `ÜBUNGEN` 0, `MERK` 0, `LÖSUNGEN` 0. (Residual German in the transform audit was only
  intentional Italian grammar strings identical in both, e.g. `mettere: io → metto`,
  `vincere: ha vinto` — these are Italian, not German.)
- P7 golden sentences: with guillemets stripped (the article occurrence has none),
  each of the 8 inner phrases occurs **exactly 2×** in both core and edition
  (once in its article, once on P7); the counting method is stated here because a
  naive quoted-form count returns 1× for 7 of 8 (only `«Fa freddo, copriti bene!»`
  is 2× in quoted form, its article occurrence also being quoted).
- P7 quote tags in the rendered edition, in order:
  (Страница 1, 1, 2, 2, 3, 4, 5, 6) — matching the W43 RU `(Страница N)` form
  and the core's page sequence.
- Badge, footer, page line, gloss prefix, P8 separators: present verbatim
  (see §3; also verified in the print PDF by space-stripped text extraction, all 8 pages).

## 12. Build / reproduce

- Build tree: `hidden_files/weekly-report-w45-it-ru-build/` — `transform.py`
  (derived from the W45 IT×DE transform by mapping every German target string to
  Russian, three mapping passes + systematic audit), content modules copied from
  `hidden_files/weekly-report-w45-it-build/`, `run.py`, `render.py`, `assets/`.
- Pipeline: single-process `run.py` (all content modules in ONE driver process,
  sharing the bslib4 exercise registry), then `render.py` — never standalone module runs.
- Interpreters (measured for THIS build, not copied from the DE sibling):
  - `run.py`: `tools/venv/bin/python` **3.12.3**, PIL **13.0.0**.
  - `render.py`: `tools/venv/bin/python` **3.12.3**, PIL **13.0.0**,
    cairosvg **2.9.1**, pypdf **6.21.2**.
  - System `python3` (3.12.3) has NO cairosvg — `render.py` must use `tools/venv/bin/python`.
- Freeze-baseline reproduction: the core baseline run reproduces the 8 core SVGs
  byte-identically (see §2), so the interpreter/PIL choice is validated for this family.
- Per-round sha256 baselines (all under the build dir): `sha256-r0.txt`,
  `sha256-r1.txt`, `sha256-r2.txt` — each fix round was preceded by a full pre-fix
  baseline of SVG/card/PDF outputs, and every fix-round edit was synced into
  `transform.py` (never only into content files).

### Fix round 1 (R0 → R1; wording-only except one box-size tweak)

R0 defects: P1-headline flow overflow (ended col 2 y=1945 vs bottom 1828),
P7 col3 ends 1790.0 (vs FRASI rule 1686), P8-keys flow overflow (8 clamped lines,
ended 2580 vs bottom 2552); occlusion R0: 49 NEW flags.
Fixes: P1 bridge gloss shortened to 3 lines; cifre parentheticals shortened
(item 1 → `(граница снегопадов)`, item 3 → `(стран-участниц)`,
item 4 → `(11-й тур Серии А)`); cifre title → `LA SETTIMANA IN CIFRE · ЦИФРЫ`;
settimana subtitle → `План недели · Giorno per giorno`; settimana footnote split
into two `p.text` lines; P2 frase box title kept verbatim but rendered at tsize=21
(its ink at 23 pt, 438.5 px, crossed the box border by 22.8 px); 19 P8 notes/keys
shortened to verified 1-line forms at 13 pt serif / 434 px (content12: 24;
content34: 44, 45, 48, 56, 57, 58, 59; content56: 87, 90, 94, 95; content7: 110;
content8: 119, 134, 135, 136, 138, 139, 150 grammar only; notable telegraphic forms:
44/134 note `S + essere + место + дата` where S = soggetto; 138 key
`Публика может пробовать бесплатно.` + note `gratis = бесплатно`; 139 key
`«Фиорентина» — «Ювентус» в воскр. веч.` + note `si gioca = играют`; 150 note
grammar fixed to `(81 слово)`); P7 letter note replaced with the Russian-only
disclosure (§5); parola gloss to 1 line; errori notes 2 and 4 abbreviated to 1 line
each (`nevicare: только 3-е лицо ед. ч.`, `gente — ед. число (жен. род).`).
R1 result: FLOW OVERFLOW 0, HEAD TOO WIDE 0; changed vs R0: exactly p1/p2/p7/p8
SVGs + cards + both PDFs (p3–p6 byte-identical); occlusion R1: 2 NEW flags.

### Fix round 2 (R1 → R2; synced into `transform.py` after the round-1 section)

Fixes: (a) P1 parola note wrapped to 2 lines with its 2nd line ink crossing the
row-B rule at y=1864 (core note is 1 line at baseline 1846.3) → shortened to 1 line:
`«il primo freddo»: холод после мягкой осени.` (the headword itself carries "primo");
(b) P7 parola gloss ink bottom exceeded its box border by 1.1 px (box-height formula
underestimates the 1-line gloss descent) → parola box height +2 px (trailing pad
20 → 22 in the `wh =` line of `content7.py`).
Note: the round-2 section uses `rep2` defined in the round-1 section, so
`transform.py` must be run whole from the top on any fresh copy.
R2 result: no `!!` flow warnings; changed vs R1: exactly p1/p7 SVGs + cards + both
PDFs; occlusion R2: **0 / 0 / 0**.

## 13. ABSTRACT

`ABSTRACT.txt` (Russian, single line, no ASCII double quotes) names the week's real
topics (first cold snap, 2 November Day of Remembrance, Panettone World Cup final
Milan 7–8 November, Torrone festival Cremona, Serie A matchday 11) + a learner search
phrase (учите итальянский по настоящим текстам) + masthead (La Lucerna) +
target-language name (Italian) + levels A2–B2 + 150 exercises.
Without it, `insert.py` aborts — the edition is not complete without it.

## 14. W43 deviation list (vs shipped W43 IT×RU)

- VOL.2 (W43: VOL.1) — follows the W45 core.
- Counts/model: A2 47 / B1 70 / B2 33 and 81-word model (W43: A2 46 / B1 71 / B2 33
  and 90-word model) — follows the W45 core.
- Badge slot geometry: y=574, 22 pt (W43: y=372, 20 pt) — forced by the frozen W45
  core strapline at y=372; see §3 deviation note. String itself is W43-verbatim.
- P8 separator already `— СТРАНИЦА N —` in W43 (no change of convention).
- Wording-only tightenings from fix rounds 1–2 (§12) — no structural deviation.
- Everything else (footer form, page line, gloss prefix, section heads, instruction
  words, P1 strap/band) follows W43 IT×RU verbatim.

## 15. Deliverables (final R2 hashes)

| file | bytes | sha256 |
|---|---|---|
| `La-Lucerna-VOL2-RU.pdf` (print) | 7,094,801 | `4de5a0668e071dff344a68edba8cf5c6b0df56b5ab740b043273385459826b04` |
| `La-Lucerna-VOL2-RU-web.pdf` (web) | 3,655,383 | `59ce56805a236fbacc900d146dba42cf0dd8d36dff141842fae4cd9600e914c9` |
| `svg/p1-prima.svg` | — | `074cd9302c92c87160379329b0e9e511388f8b6ea64e2d12eff757fa8671aee0` |
| `svg/p2-vita.svg` | — | `73b7691fff5f280994ff44545f4b46c8ca90ad57879fe902321cc1f98a41c377` |
| `svg/p3-cultura.svg` | — | `1977aceb8b99291c5a2fef7b99baf4a4e819ed2be863bf7c6169871a70229214` |
| `svg/p4-sport.svg` | — | `7dfe42e66c0140bce3f01dc94329fa1177d6b351efbc710ca9f4e7d71158ca41` |
| `svg/p5-giovani.svg` | — | `97a3aa11c52fe689e2d5cbac0e4edba6268f862108adc34a8b1cf068964c4adc` |
| `svg/p6-approfondimento.svg` | — | `c4c585728c65580dcf8701471552107d47aade766ea59aab59f30c8fb10c91e9` |
| `svg/p7-lingua.svg` | — | `f5f6c316bd9464ba3f125c6f4b90b84a910936b771959e2cf7575fc4a19cad0f` |
| `svg/p8-valutazione.svg` | — | `d902efc466eeeaa99db8d2eca7cf76f353083b5fc391cebe2881fc227ca0dd8e` |
| `cards/p1-prima.png` | 744,901 | `09d7e4e6574cc28e8e36d8fdae97a350701f8419017a15ed284fc5d47f235ac8` |
| `cards/p2-vita.png` | 727,542 | `327efd9968315c1e45ccd6ae945b012408c7f0fcc357bbadaae98d255f888231` |
| `cards/p3-cultura.png` | 888,059 | `47752ff0ae661cd6fcc232b270b4a513481a1da01dd38fc5052f909cc3d7f8fd` |
| `cards/p4-sport.png` | 657,320 | `61aaaf5a7c281b81e068a2984adb7e605feac83681034ae31f555c2a8e41bd06` |
| `cards/p5-giovani.png` | 992,533 | `f351f18ed1094863423bc354b6f5ca282421e7b6ba0fcc3f2c560bc1f0831da4` |
| `cards/p6-approfondimento.png` | 720,071 | `46b542f3c12be12eb04a7cc11f2e00e9da447bb49dbd2344efe7a92eed615f20` |
| `cards/p7-lingua.png` | 534,725 | `3fd960b0cfc71c94a95e30b93e39313caf2973dfe8aad7562a440a7050c56fc0` |
| `cards/p8-valutazione.png` | 1,009,982 | `3d9996af5f2441cc699114c85e67aa3fb2a1908421d0baf19b6cb9ca9d47fca3` |
| `WEEKLY-KIT.md` | — | (this file) |
| `ABSTRACT.txt` | — | (Russian single line, see §13) |

Both PDFs: 8 pages. Print mediabox 1462.5 × 2025; web mediabox 1400 × 1938.
Badge, footer, and page line verified on all 8 print-PDF pages by text extraction.

## 16. Delivery status

**Builder-complete, NOT finalized.** All mechanical gates in §§2–11 pass on the R2
deliverables. A fresh full independent proofread round is still required before
delivery to the LucernaRead/weekly repo. Per standing rules: no Discord post
(delivery paused by the user's 2026-10-21 decision), no card/PDF dump into the main
chat, no cron created, weekly-git untouched, W45 IT core and W43 directories untouched
(core re-hash verified 8/8 at the end of this build).
