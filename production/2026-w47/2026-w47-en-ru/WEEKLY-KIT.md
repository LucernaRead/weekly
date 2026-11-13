# WEEKLY-KIT — 2026-W47 en-ru (English target, Russian reader)

## 1. Identity
- Slug: `2026-w47-en-ru`
- Target language: English (en). Reader language: Russian (ru).
- Issue week: Monday 16 – Sunday 22 November 2026. VOL.4.
- Core: `production/2026-w47/core-en/` (en-zh-cn), copied whole, explanation layer rewritten in Russian.
- Exercises: 150 (registry 150; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- MODEL words: 82.

## 2. Files delivered
- 8 SVG (`svg/p1-front.svg` … `svg/p8-test.svg`) + 8 card PNGs (`cards/`).
- Print PDF: `The-Lucerna-VOL4-en-ru.pdf` — 28,991,765 bytes,
  SHA-256 `7336fdd65c17baa107ecb7ef3871c696499c52176d131573214c08ec7195bbc3`
  [boxtitle fix2, 12 Nov 2026 — see §3; pre-fix values were print `dde756cb…` 28,991,750 B,
  web `21d12637…` 2,468,667 B.]
  [fix-xru, 12 Nov 2026 — see §3; pre-fix values were print `9e503c05…` 29,097,780 B,
  web `8875c559…` 2,573,323 B.]
  [D5 rebuild, 12 Nov 2026 — see §3; pre-D5 values were print `a42edc0e…` 29,241,520 B,
  web `588002ff…` 2,452,552 B.]
  [F1 fix, 12 Nov 2026 — see §3; pre-fix values were print `e8c2cc4e…` 29,097,398 B,
  web `f50ae8fc…` 2,572,948 B.]
  (delta fix2, 2026-11-11; was 29,241,529 / `fb849665…`).
- Web PDF: `The-Lucerna-VOL4-en-ru.web.pdf` — 2,468,694 bytes,
  SHA-256 `8ded0e80780b33981cb31bf438c9ceb1ac804cc226f6aa985ae94507dbcca0ad`
  [boxtitle fix2, 12 Nov 2026 — see §3; pre-fix web was 2,468,667 B `21d12637…`.]
  [fix-xru, 12 Nov 2026 — see §3; pre-fix web was 2,573,323 B `8875c559…`.]
  (delta fix2; was 2,452,560 / `5aac849d…`)
  (built only with `tools/webpdf.py`; 8 pages).
- `2026-w47-en-ru.text.md` — 62,552 bytes, SHA-256 `13e0e75ce382f9ed9ae4d390f95026febd92ed08d1689347302c623fa34351f5` (F1 fix, 12 Nov 2026 — see §3; pre-fix 62,381 B `78c1b137…`; delta fix2; was 62,384 / `bf3a9127…`), exported from the build source (never from the PDF);
  stub registry 150 = real registry 150.
- `ABSTRACT.txt` — one line, Russian, no ASCII double quotes.
- `registry.json` — fresh dump (150 keys), copied over the stale core copy from apply.py.

## 3. Gates (all green, re-run fresh 2026-11-11)
- run.py exit 0; 0 FLOW OVERFLOW / HEAD TOO WIDE; every Flow end y ≤ its bottom
  (P8-keys 2460/2560; P2-feature 1498/1540; P2-ex 2532/2560).
- occlusion audit: 0 flags (selftest OK).
- p8 extract: 60/150 noted (same set as core); compare CLEAN; keydiff [137, 138, 139, 140, 150]
  (reader-language translation keys + writing key — expected).
- freeze baseline tool: 8/8 byte-identical; direct sha256 re-render vs shipped core SVGs: 8/8 MATCH.
  Freeze diff: added CJK = only 9× U+3000 separators; removed = core Chinese layer.
- print/web text token-multiset diff: 0/0 (47,655 chars each; token-multiset diff 0/0; per-page byte-identical 8/8).
- `check_s11.py ru`: ALL §1.1/P8 CHECKS PASS (colour set core 19 = edition 19;
  badge colours A2 #5c6e30 / B1 #46581f / B2 #37402f; P8 min font 13.5 pt ≥ 9.75;
  chip-rect counts = core per page; Q113–120 options line with [A2] tag present;
  "Levels: 145–149 [A2]" present; Q120 [A2] chip OK;
  P8 WRITING head "H　WRITING　Письмо [B1]" present).
- **D5 rebuild + gates (12 Nov 2026; full log `hidden_files/w47/scratch-d5-rebuild-en/logs/2026-w47-en-ru/GATES-SUMMARY.txt`)**: SOP §1.1 font fix — installed via `scratch-d5-plan/mechanism/apply_variant.py --target en --reader ru` (mode ru, D5 block in this edition's `svglib.py`, `_D5_READER = "ru"`; routing unit-checked: `check_routing.py` FAILURES: 0; U+201C fix2 routing preserved — census: curly in CJK 0, all 164 curly quotes in Newsreader). Pre-fix census: 395 Latin-in-CJK + 303 Cyrillic-in-CJK elements. Post-fix defects: **none** — run.py clean first run (0 FLOW OVERFLOW, 0 HEAD TOO WIDE), all gates green without any source fix. NOTE: PILOT-REPORT §5.4's en-ru P8 "answer key-row collisions ×3" is VOID (mechanism-confirmed measurement false positive, occlusion_audit.py resolve_font fixed) — no P8 key-row change was made; the (fixed) occlusion audit reports 0 flags on the rebuilt edition. Layout only, text unchanged. Gates: run rc=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; `head_check.py` PASS 0 defects; `render.py` + `webpdf.py` rc=0; `occlusion_audit.py` 0 flags (selftest OK); `p8.py extract` 60/150 (same set), `compare` **CLEAN**, keydiff=[137, 138, 139, 140, 150] (expected); `freeze.py baseline` **8/8**; `freeze.py diff` vs core-en TOTAL added CJK 9, all U+3000; added Latin strings 135 (D5 run-splitting); `spill_sweep.py` 0 SPILL (150 OBSERVE); `boxtitle_check.py` 0 DEFECT / 0 OBSERVE / 0 marginal (34 titles, 238 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` **PASS 0 defects** (ratios n=472 median 1.008, bold 0.956); `d5_census.py` **PASS** — D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, `Noto Sans` elements 0; print/web `pdftotext` byte-identical, 37,997 chars, unchanged vs pre-fix; text.md byte-identical (`78c1b137…`, 62,381 B). P8: 192 → 203 lines, footer slack 47.8 → 36.3 px. **OVERALL: ALL-GREEN.** Pre-D5 baselines (disk-measured): print `a42edc0e…` (29,241,520 B), web `588002ff…` (2,452,552 B); new SHAs in §2 (print `e8c2cc4e…`, web `f50ae8fc…`).
- **F1 fix (12 Nov 2026, proof-round defect F1 — Georgia runoff written as pending; work log in `hidden_files/w47/scratch-fix-en/FIX-LOG.md`, gates in `hidden_files/w47/scratch-fix-en/logs/2026-w47-en-ru/`):** P2 :185 + P6 :651 rewritten as settled law + result (Georgia law calls for a Dec 1 runoff only if no one wins a majority — AP called Jon Ossoff reelected 3 Nov, ~59%, so no runoff). Q13/Q142 untouched (rule questions, answers still 1 December). Source `content12.py:171` + `content56.py:103`; text.md re-exported with `scratch-fix-en/make_textmd_fix.py` (diff exactly the 2 lines, no title lost). Full rebuild + gates ALL-GREEN: run rc=0 TOTAL 150 MODEL 82, 0 overflow; head_check PASS; occlusion 0 flags (selftest OK); p8 extract 60/150, compare CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); freeze baseline 8/8; freeze diff added CJK 9, all U+3000; spill 0 (152 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal (34 titles, 238 body lines); edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (P8 203 lines, slack 36.3); census PASS — D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, `Noto Sans` elements 817 (Russian reader layer, expected); print/web text layers byte-identical. New deliverables: print 29,097,780 B SHA-256 `9e503c05…` (was 29,097,398 B `e8c2cc4e…`), web 2,573,323 B `8875c559…` (was 2,572,948 B `f50ae8fc…`), text 62,552 B `13e0e75c…` (was 62,381 B `78c1b137…`); text layer 38,129 chars (was 37,997). NOTE: `svglib.py` font routing untouched per task scope (Latin title font issue handled separately, cross-family).
- **fix-xru (12 Nov 2026, SOP §1.1):** `svglib.py` `_D5_READER == "ru"` branch routed Latin text to Noto Sans CJK; branch removed (marked `[removed 2026-11-12 fix-xru]`), now always else logic — Latin → Newsreader, Cyrillic → Noto Sans. Print PDF rebuilt by previous worker (accepted by coordinator: text-layer character multiset identical pre/post, 38,129 non-space chars); web PDF rebuilt by this worker (`webpdf.py` rc=0, 8 pages). Probe (SVG runs): pre-fix LAT@NotoSans=4066 LAT@Newsreader=22918 CYR@NotoSans=5600; post-fix LAT@NotoSans=0 LAT@Newsreader=26984 CYR@NotoSans=5600 (unchanged). New deliverables: print 28,991,750 B SHA-256 `dde756cb…` (was 29,097,780 B `9e503c05…`), web 2,468,667 B `21d12637…` (was 2,573,323 B `8875c559…`); text.md unchanged 62,552 B `13e0e75c…`. No retry.
- **boxtitle fix2 (12 Nov 2026, *-ru sweep follow-up; work log in `hidden_files/w47/scratch-fix-en-ru2/`, gates in `hidden_files/w47/scratch-fix-en-ru2/gates2/`):** fix-xru (Latin → Newsreader) regressed 3 box titles right over the cream box (sweep `scratch-sweep-xru-occl-1/SWEEP-LOG.md`; core对照皆为负). Fix = title font-size only, wording untouched, per-box minimal (nl 25→23pt precedent): P1 `THE WEEK IN NUMBERS　Цифры` tsize 23→22 (was +8.5px, now +9.1px margin); P5 `ODD SOCKS, IN NUMBERS　Цифры` tsize 23→21 (was +24.3px — 22pt still −6.0px — now +12.7px margin); P6 `A PRACTICE BALLOT　Бюллетень` tsize 23→22 (was +11.4px, now +7.1px margin). Source `content12.py:43` + `content56.py:22,106`; `svglib.py` untouched. Only `svg/p1-front.svg`, `p5-youth.svg`, `p6-deep.svg` changed (other 5 byte-identical). Full rebuild + gates: run rc=0 TOTAL 150 MODEL 82, 0 FLOW OVERFLOW; HEAD TOO WIDE = 2 = the two already-adjudicated-accepted heads (P7 AN EXAMPLE LETTER, P8 Понимание текста — out of scope per task, on untouched P7/P8 pages; head_check RC=1 on those two only); occlusion 0 flags (selftest OK); p8 extract 60/150, compare CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); freeze baseline 8/8; freeze diff added CJK 9, all U+3000 (added Latin 145 vs F1's 135 = fix-xru run-splitting, pre-existing); spill 0 (176 OBSERVE); **boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal (42 titles, 397 body lines)**; edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (P8 203 lines, slack 36.3); census PASS — D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader; text.md byte-identical (`13e0e75c…`, 62,552 B, diff 0 lines), registry diff 0; print/web text layers byte-identical; print text-layer token-multiset diff vs pre-fix 0/0, non-space char multiset diff 0 (27-line pdftotext diff is whitespace-only line-reflow from the 1–2px box shrink). New deliverables: print 28,991,765 B SHA-256 `7336fdd6…` (was 28,991,750 B `dde756cb…`), web 2,468,694 B `8ded0e80…` (was 2,468,667 B `21d12637…`).
- **HEADS-NOTE acceptance record A1/A2 (2026-11-12裁定, `hidden_files/w47/scratch-fix-xru-heads/HEADS-NOTE.md`):** the two HEAD TOO WIDE heads named above are accepted items, not to be fixed, and were not rebuilt. A1 — P7 `AN EXAMPLE LETTER`, +5.2u (200dpi pixel measurement; 200dpi 像素实测); crop clean, no collision, does not cross the column （裁图干净、无碰撞、不越栏）. A2 — P8 `Понимание текста`, +0.4u; negligible, sub-pixel （亚像素可忽略）. The HEAD TOO WIDE warning for these two may still appear in build logs / head_check — it is an accepted item, not an unfixed defect.
- **fix1 re-gate (2026-11-11, logs in `hidden_files/w47/scratch-fix-en-ru2/`):** all gates
  re-run on the rebuilt edition and green — run.py exit 0, TOTAL 150, 0 OVERFLOW/TOO WIDE;
  occlusion 0 flags; p8 extract 60/150 noted = core set, compare CLEAN, keydiff
  [137, 138, 139, 140, 150]; freeze baseline 8/8 + direct sha 8/8; freeze diff added CJK
  9× U+3000 only; print/web text 47,649 chars each, token-multiset diff 0/0, per-page
  byte-identical 8/8; check_s11 ALL PASS; source boxtitle 12/12 fit; SVG boxtitle 18/18 fit;
  canonical creambox 0 OVERFLOW; h-containment H-SPILL 0 (D1 closed); P8 min PDF font
  10.12 pt ≥ 9.75 pt; keycheck registry-vs-P8extract 149/150 exact + #150 short-label
  exception; 150 keys 3-source (registry / P8 extract / text.md answers) exact; orphan
  punctuation visual-line scan 0 (core-en control also 0); quotes 201C=201D (81 text.md /
  82 SVG), U+2019 = 0, banned words 0. See §5 item 7 for the fix and two observations
  (gates.sh stale-registry path bug repaired; Q73 key flagged, NOT fixed — out of scope).
- **delta fix2 re-gate (2026-11-11, logs in `hidden_files/w47/scratch-delta-en-ru/`):** all gates
  re-run on the rebuilt edition and green — run.py exit 0, TOTAL 150, 0 OVERFLOW/TOO WIDE;
  occlusion 0 flags; p8 extract 150/150 noted 60/150 = core set, compare CLEAN, keydiff
  [137, 138, 139, 140, 150]; freeze baseline 8/8 + direct sha 8/8; freeze diff added CJK
  9× U+3000 only; print/web text 47,646 chars each, token-multiset diff 0/0, per-page
  byte-identical 8/8; check_s11 ALL PASS; verify_ed ALL PASS; source boxtitle 12/12 fit;
  SVG boxtitle 18/18 fit; canonical creambox 0 OVERFLOW; h-containment H-SPILL 0;
  P8 min PDF font 10.12 pt ≥ 9.75 pt; keycheck registry-vs-P8extract 149/150 exact +
  #150 short-label exception; registry-vs-core 145/150 (only the 5 reader keys differ —
  Q73 now matches core `up`); 150 keys 3-source (registry / P8 extract / text.md answers)
  exact; orphan punctuation visual-line scan 0; quotes 201C=201D (81 text.md / 82 SVG),
  U+2019 = 0, banned words 0; D5 font inventory 1798 `<text>` / 26 sizes, identical to
  fix1 (record only). Key-fit review: all 57 blank/rewrite items + 14 cloze/dialogue/
  writing items re-checked stem-vs-key — 0 misfits (weekdays re-verified: 3 Nov Tue,
  20 Nov Fri, 26 Nov Thu, 27 Nov Fri). SVG change scope: only `p8-test.svg` changed,
  other 7 byte-identical — **p5 与修前字节一致是正确且预期的**（Q73 键只印 P8 答案区，
  从不上 P5 题干页；en-es delta 同证）。

## 4. Translation decisions (Russian)
- Follows W46 ru (TM): ты-form imperatives (Заполни, Перепиши, Подбери пары, Исправь); gloss format
  "term = translation", "·" separators, "Пояснение — " box prefix (bslib4 gloss() prepends it;
  gloss translations are bare — only the P1 bridge carries its own label, "Пояснение — ",
  which the bridge-size patch matches via the empty gloss_word, first f.bridge() call).
- "runoff" = "второй тур"; "call a race" = "объявить результат"
  (registry notes keep the TM "объявить итоги выборов" — two different source literals, both
  correct); "to certify" = "официально утвердить" (registry notes keep the TM "утвердить
  официально" — word order differs, both correct); "midterm" = "промежуточные выборы";
  "seat" = "мандат"; theme "Break the Silence" = "Нарушь молчание".
- Numbers box keeps the English term with a Russian gloss in parentheses (W46 ru precedent).
- P2 calendar lines in full-Russian short form (es precedent — avoids the fr P2 overflow):
  "10 нояб. — республиканцы выбирают лидера · 18–19 нояб. — демократы голосуют" /
  "20 нояб. — Всемирный день ребёнка · 26 нояб. — День благодарения · 27 нояб. — Чёрная пятница".
- SAY IT title = "Как назвать дату" (date, not clock time — the de D-de1 lesson).
- P1 word-of-week bridge pre-shortened to 2 lines: "Промежуточные выборы: вся Палата
  и треть Сената." (fr/es lesson).
- TM types (used as-is): 完成句子→"Дополнить предложения", 翻译→"Перевести", 写作→"Сочинение",
  阅读理解→"Понимание текста", 单选→"Выбрать ответ", 完形填空→"Заполнить пропуски",
  词汇配对→"Подобрать пары", 句型转换→"Преобразовать предложения", 对话补全→"Диалог".
  TM instr: 填空→"Заполни", 把词和释义配对→"Подбери пары", 改写→"Перепиши", 配对→"Подбери пары".
- Fresh sets: instr 纠错→"Исправь"; types 从句→"Придаточные", 将来时→"Будущее время",
  时态→"Времена глагола", 比较填空→"Сравнения", 过去时→"Прошедшее время",
  金句填空→"Золотые фразы", 纠错→"Исправление ошибок", 图表读数→"Чтение графиков"
  (overrides the poisoned TM value "sans").
- ekeys: 137 "Демократы выиграли Палату представителей и Сенат.",
  138 "Подсчёт голосов продолжается.", 139 "Новый Конгресс соберётся в январе 2027 года.",
  140 "Нарушь молчание.", 150 "Открытый вопрос — критерии в рамке сочинения; образец —
  в рамке на этой странице" (dash form — lit_override; the TM value used a colon, the es/pt
  Q150 trap).
- Box titles (single-line, short forms): "ERROR CLINIC　Ошибки", "READERS' CORNER　Письма",
  "AN EXAMPLE LETTER　Пример", "THE TOOLBOX　Инструменты", "NEXT WEEK　Анонс VOL.5",
  "SENATE IN NUMBERS　Сенат" (short gloss, nl lesson applied pre-emptively; core fix1
  dropped "THE"), "HOW LONG?　Срок полномочий", "ODD SOCKS, IN NUMBERS　Цифры",
  "SATURDAY, NOV 21　Суббота" (core fix1 title), "HAYMITCH'S GAMES　Игры",
  "THE CALENDAR　Календарь" — all short forms, no collision (occlusion 0 flags).
- P8 section heads use TM short labels ("Выбор", "Предложения", "Диалог", "Письмо") that differ
  from the registry type names ("Выбрать ответ", "Дополнить предложения", "Диалог", "Сочинение") —
  same pattern as fr/es/it/pt/nl. **"H　WRITING　Письмо [B1]" is the shipped W46 ru head
  (content8.py:131), verified in the TM — kept as-is, not a defect.**

## 5. Fixes in this round
1. **Q150 colon → dash via lit_overrides** (es/pt lesson, caught before the first build): the W46 ru
   TM value for the Q150 key uses a colon ("Открытый вопрос: …"); p8.py detect_note needs " — "
   before the trailing paren note. Overrode to dash form in fresh-ru.json.
2. **P8 key size pre-set to 13.5/1.26** (not 15.5/1.3 from the W46 meta) on the es/it lesson.
   P8-keys ends 2460/2560.
3. **SENATE title pre-shortened** ("Сенат" only) on the nl lesson — no title-to-neighbour collision
   on the final card (verified visually).
4. **SCRATCH path fixed at sed time** (it/nl lesson): verified SCRATCH = ru before running.
5. **Rebuild + fix1 (11 Nov 2026, core-en fix1 sync — this round).** Core-en was fixed and
   re-proofed (Q39→a, Q40→d, Ashes rewritten as a 2025–26 retrospective, 已宣布 wording,
   SEARCHES/DID YOU KNOW box heights, SENATE/SATURDAY titles, SAY IT middle panel widened)
   and this edition was rebuilt from the fixed core via `scratch-fanout-en2/fanout/apply.py` +
   patched `map-ru.json` (14 new literals: Q39/Q40 keys + notes, Q46/Q52/Q55/Q125 notes,
   SATURDAY/SENATE titles, P1 strip, Q7/Q82/Q83/Q84 notes, P6 bridge). Proof1 defects D1–D3
   were core-level and are resolved by the rebuild (verified per edition: registry keys
   39=a/40=d, notes `mentor = наставник a` / `arena = арена d`; Q46 note dated Fri 21 Nov
   2025; Q52 `hosted`, Q55 `won`, Q125 `A (4–1)`; text.md answers 39→a, 40→d, 125→A;
   `Arsenal are winning!`; no `Perth is winning!` / `second week in Perth` / `Ashes begin`).
   The old ABSTRACT was short-form (§9-class, like ja D4) and was rewritten to the full form
   (announced results; certification 10 Nov–18 Dec; 16 Nov Anti-Bullying/Odd Socks; 20 Nov
   Children's Day + Hunger Games; 21 Nov Premier League back + Turin ATP final + Ashes 4–1
   look-back; reader language; A2–B2; 150).
   **D4 (edition-level) fixed — SAY IT panels:** the Russian line 1 "Подсчёт голосов всё ещё
   продолжается." (394.5 px) overflowed the 280 px panel (ink 103–490 vs box [159,439]);
   RU line 2 (360.6 px) fit the core-widened w=380 middle panel. Fix: post-apply code edit in
   `content12.py` — `phrase_panel(299, …, w=420)` (panel 89–509; the 51 px gap to the middle
   panel at 560 is empty margin at that y). Verified on the P2 card: all three Russian subs
   inside their panels with margins; the SAY IT glossary column (lx=1370) keeps its gutter
   (panel 3 still ends at 1340).
   **D5 (edition-level) fixed in the map:** P3 HAYMITCH title `HAYMITCH'S GAMES　Игры Хеймитча`
   (429.8 px, −20.4) → `HAYMITCH'S GAMES　Игры` (309.6 px, +94.9); P4 SATURDAY title
   (408.2 px, −8.1) is fixed by the core's shorter "SATURDAY, NOV 21" — rebuilt title
   "SATURDAY, NOV 21　Суббота" measures 328.9 px (+75.6). All 18 SVG box titles now fit.
7. **fix1 — D1 P1 SEARCHES gloss overflow (proof1 (b), 2026-11-11).** Russian gloss
   `Относительный интерес, не точные цифры.` (409.0 px at 19 px sans, x=1461.5) spilled
   8.5 px past the cream-box right edge (1862.0); pre-existing, not a rebuild regression.
   Fix: drop one word → `Относительный интерес, не точные.` (339.4 px, ends 1800.9,
   margin +61.1 px), keeping "relative interest, not exact". Changed in two places, kept
   identical: `scratch-fanout-en/map-ru.json:228` (`lit` section, key
   `相对热度示意，非精确搜索量。`) and edition `content12.py:85`. No other source touched.
   Rebuilt en-ru only (run.py + render.py + webpdf.py + text.md re-export); only
   `p1-front.svg` changed (other 7 SVGs byte-identical). Re-measured three ways:
   SVG advance +61.1 px; print-PDF ink span ends 1351.3 pt vs box 1396.5 pt (+45.2 pt);
   150 dpi render rightmost ink 1349.3 pt (+47.2 pt), cream→white transition at 1396.3 pt.
   New SHAs in §2. Full gate table + logs: `hidden_files/w47/scratch-fix-en-ru2/FIX-LOG.md`.
   **Two observations (not fixed, out of scope):** (a) `gates.sh` assumed `dump_reg.py`
   writes to `scratch-fanout-en/ru/registry.json`, but it writes to
   `scratch-fanout-en2/fanout/ru/registry.json` — the ru copy was stale (04:39, pre-refanout
   keys Q39/40/52/55/125 + notes) and `make_textmd_w47.py` failed its key assert until the
   fresh dump was copied over (stale copy preserved as `registry-stale-0439.json` in the
   fix scratch); (b) **Q73 key is wrong vs its stem:** stem `Speak ___: tell a teacher.`
   needs `up`, edition keys `speak` (registry + P8 extract + text.md all agree, so the
   3-source check passes — the error is stem-vs-key, invisible to consistency gates);
   core-en has since been corrected to `up` (core `content56.py` edited 14:28 today by
   concurrent en-zh-cn work; proof1's keycheck showed registry-vs-core 145/150, now
   144/150 with only Q73 differing besides the 5 reader keys). Flagged for the
   coordinator / re-proof; NOT changed by this fix (scope = D1 only).
   **→ 已由本次 delta fix2 执行（见下条）。**
8. **delta fix2 — Q73 key speak→up (2026-11-11, core-en fix2 已定稿 + re-proof (a) 通过)。**
   只改版内 `content56.py:49` 一行：key `"speak"` → `"up"`；note
   `speak up = говорить открыто` 与题干 `Speak ___: tell a teacher.` 一字未动。重导 registry +
   text.md、重建 run.py / render.py / webpdf.py。Registry diff 恰 1 条（n=73 speak→up）；
   text.md diff 恰 1 行（:1151）；Q73 四源一致为 up（registry、text.md、P8 印出键、P5 题干 +
   `speak up = говорить открыто` 注释）。D1 修复全程保留：`content12.py:85` 的
   `Относительный интерес, не точные.`、map-ru.json:228 对应值、P1 SVG gloss 均未动，重建前后
   三重核查仍为修复态（未 re-fanout，未碰 map）。SVG 变化范围：仅 `p8-test.svg` 变，其余 7 页
   字节一致——**p5 与修前字节一致是正确且预期的**（Q73 键只印 P8 答案区，从不上 P5 题干页；
   en-es delta 同证：p8 含 `73. up`，p5 不变）。新三件 SHA 见 §2；全部门禁见 §3 delta 条目；
   键-题干适配抽查：57 条填空/改写 + 14 条 cloze/对话/写作逐条复核，0 不符。日志与证据：
   `hidden_files/w47/scratch-delta-en-ru/DELTA-NOTE.md`。未动：core-en、其他 9 个 en-* 版、
   tools/、issues/；未 commit、未 push（由协调员统一做）。
6. **Rebuild gates (11 Nov 2026; logs in `hidden_files/w47/scratch-fanout-en2/fanout/ru/build-gates.log`)**:
   `run.py` exit 0, zero OVERFLOW / TOO WIDE, all flows within bottom, TOTAL 150, MODEL 82;
   `occlusion_audit.py` 0 flags, selftest OK; `p8.py extract` noted set 60/150 (same set as
   core); `p8.py compare` CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); registry vs P8
   extract 149/150 exact + n=150 short-label exception; registry keys vs core 145/150 (diff
   only the 5 reader-language keys 137–140, 150); `freeze.py baseline` 8/8 SVGs byte-identical;
   `freeze.py diff` TOTAL added CJK 9, all U+3000; print/web text layers 47,655 chars each,
   token-multiset diff 0/0, per-page byte-identical 8/8; `check_s11.py` ALL PASS; source
   boxtitle sweep 12/12 fit; SVG boxtitle sweep 18/18 fit; canonical `creambox.py` scan: all
   inside-only clearances positive; P8 min PDF font 10.12 pt ≥ 9.75 pt; SVG zero real CJK.

## 6. Self-check (2026-11-11)
- Full read of `2026-w47-en-ru.text.md` (all ~1,306 lines): zero issues.
  Notes kept: Q2/Q95 note "call a race = объявить итоги выборов" (TM) vs P6 gloss
  "объявить результат" — two source literals, both correct; Q94 "certify = утвердить
  официально" (TM) vs "официально утвердить" — word order differs, both correct; Q34
  "(open = выйти в прокат (3-е лицо ед. ч. + s))" correct; Q54 "eight (восемь = eight)"
  tautological like the core's note pattern; Q97 "take time = занимать время" correct; Q110
  "more than, конструкция" terse as in core; Q136 "whether = ли" vs Q105
  "whether = ли (о том, чего не знаешь)" — two source literals, both correct; "Пять фраз
  рецензии: кто, где, что случилось, поворот, финал — пяти хватит." is the W46 ru TM value
  for the FIVE SENTENCES bridge (kept); "Язык матча: счёт, кто забил, кто ведёт — короткие
  фразы, как в прямом эфире." and "Одна карта: пятьдесят штатов — пятьдесят правил; …" are
  W46 ru TM values (kept).
- All 8 cards visually checked after the final render — clean. P1: bridge 2 lines clear of
  IN BRIEF, numbers box English+gloss, "TRY IT NOW · Попробуй сразу", footer "Страница 1 из 8".
  P2: calendar short form, "THE SENATE, IN NUMBERS · Сенат", SAY IT "Как назвать дату",
  gloss single "Пояснение — to certify = …". P3: "COMING SOON · Скоро в кино",
  "HAYMITCH'S GAMES · Игры", gloss single "Пояснение — a tribute = …", Rousseau tiger.
  P4: "SATURDAY, NOV 21 · Суббота" (core fix1 title), gloss single "Пояснение — a Test: …", W. G. Grace photo; P4 lead is the Ashes 2025–26 retrospective "Perth, One Year On: How Australia Kept the Ashes".
  P5: "ODD SOCKS, IN NUMBERS · Цифры", gloss single "Пояснение — bullying = …",
  "SPEAK UP · Говори громко", Lawrence children photo. P6: "HOW LONG? · Срок полномочий",
  gloss single "Пояснение — to call a race = …", "A PRACTICE BALLOT · Бюллетень", voting booth
  photo. P7: all gloss boxes single "Пояснение —", "THE TOOLBOX · Инструменты",
  "READERS' CORNER · Письма", "AN EXAMPLE LETTER · Пример", "ERROR CLINIC · Ошибки",
  "NEXT WEEK · Анонс VOL.5", Johnson portrait. P8: cloze + [A2] option tags,
  "B MULTIPLE CHOICE · Выбор", "C READING · Понимание текста", "D SENTENCES · Предложения",
  "E TRANSLATION · Перевод" with "Переведи:", "F WORDS · Подобрать пары",
  "G DIALOGUE · Диалог" + "Levels: 145–149 [A2]", "H WRITING · Письмо [B1]" +
  Russian instruction, MODEL + Reading Room photo, ANSWERS block all 150 keys ending well above
  the footer with "150. Открытый вопрос — критерии в рамке сочинения; образец — в рамке на
  этой странице (Оценка по пунктам)"; footer "Страница 8 из 8".

## 7. Furniture
- foot_left "The Lucerna　АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4　ТЕКСТЫ НА АНГЛИЙСКОМ　ОБЪЯСНЕНИЯ
  НА РУССКОМ"; foot_right "Страница {n} из 8"; gloss_prefix "Пояснение — ";
  p8_sep "— СТРАНИЦА {pg} —"; translate prefix "Переведи: ";
  badge "ТЕКСТЫ НА АНГЛИЙСКОМ　ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ";
  topstrip "WEEKLY IN ENGLISH　Каждую неделю　О чём говорит англоязычный мир";
  edition line "АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК　VOL.4　ВЫБОРЫ　ДЖУНГЛИ　КИНО";
  edition spacing 9.1; p1_bridge_size 19.5; p8_mode "notes".

## 8. Provenance
- TM: W46 `2026-w46-en-ru` positional alignment (260 pairs). Poisoned values caught:
  'note' → 'P8 saved, TOTAL exercises:' (harmless, rejected by build_map's POISON regex);
  '图表读数' → 'sans' (overridden by fresh type "Чтение графиков").
  'THE ERROR CLINIC　易错诊所' → 'THE ERROR CLINIC　Ошибки' is a legitimate translation, not poison.
- Map: `scratch-fanout-en2/fanout/map-ru.json` (lit 248, instr 5, type 17, ekey 4).
  Misses: 205 total, 182 with real CJK = 171 lit + 7 types + 4 ekeys.
  build_map normalizes U+2019 → ASCII apostrophe in all map values (fr lesson).
- F-MAIL: no real letters arrived; P7 prints the labelled editor's example + the VOL.3
  disclosure promising real letters from VOL.5. No invented letters, no email checked.

## 9. Build record
- `scratch-fanout-en2/fanout/ru/` — build-gates.log, make_textmd_w47.py, occlusion.log/json,
  p8-extract/compare.json, freeze.log/diff.json, webpdf.log, textmd.log, registry.json, dump_reg.log,
  freeze-final/.
- fix1 (2026-11-11): `hidden_files/w47/scratch-fix-en-ru2/` — FIX-LOG.md, run.log, render.log,
  gates.log (gates.sh run), textmd.log, verify_fix.py + verify_fix.log (D1 triple re-measure,
  P8 min font, D5 inventory, quotes/banned, orphan scan, 3-source check), verify_3src.log,
  verify_fix2.log, gates/ (occlusion, p8-extract/compare, freeze log/diff, webpdf, check_s11,
  boxtitle, boxtitle-svg, verify, keycheck, keycheck.py, creambox, h-containment,
  h-containment.py), render/ (150 dpi print P1 + p1-searches-gloss-new.png zoom crop),
  svg-before.sha256, registry-stale-0439.json, probe.txt.

## 10. Tool note (NOT fixed — p8.py is off-limits to the builder)
- `tools/p8.py` FOOTER_RE does not match the mixed-case footer "The Lucerna …" + "Страница 8 из 8":
  the merged footer line leaks into the last answer segment (key 150) for every edition.
  Masked when key 150 is dash-style (ru, nl, pt, it, fr, de), bites when paren-style without a dash
  (es, before its fix). A case-insensitive match on the masthead, or dropping the merged footer line
  by its y=2624 baseline, would close it.
- Occlusion audit gap (found in the nl round): the audit does not flag a box title running into live
  text in the neighbouring column. A title-vs-neighbour text proximity check would close it.
