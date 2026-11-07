# INDEPENDENT PROOF — W45 zh-cn × ru (Simplified Chinese target · Russian reader)

**Verdict: NOT PASS — one blocking item (B-1, Gate 10). Do NOT ship on this report.
The coordinator inserts nothing yet.**

The delivered artifact itself passed every other gate (see per-gate evidence):
freeze, P8, occlusion, gloss, phrases, images, readers' corner, furniture
(including the badge — this edition really is BRICK, unlike the just-failed
zh-cn×fr case), registry, web-PDF regeneration, and the 8-card visual read.
The single failure is reproducibility: the builder's one-shot transform
script does not reproduce the delivered edition, because four post-transform
fix rounds were never folded back into it. Per the tasking, reproduction
failure is BLOCKING, so this edition cannot be declared finalized on this
round — even though the delivered pages themselves are clean.

**Remedy (for the builder/coordinator, NOT performed by this proofreader):**
fold the four fix groups listed under B-1 into
`hidden_files/weekly-report-w45-zh-cn-ru-build/scratch/transform_ru_w45.py`,
re-run transform-alone to 8/8 byte-identical, then commission a fresh full
proof round. Do not patch the delivered SVGs by hand.

---

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live worker writing to the delivery/build dirs: the only processes
  seen during the run were short-lived sibling-edition checks (a JA-edition
  PDF check); both had exited on re-check, and a final `ps` sweep at
  08:10 UTC found no `run.py`/`render.py`/`transform_ru` process. A scan of
  open file descriptors found nothing under the zh-cn-ru dirs.
- (b) mtime snapshots of BOTH dirs (`files/weekly-report-w45-zh-cn-ru/` and
  `hidden_files/weekly-report-w45-zh-cn-ru-build/`): snap1 ~07:56 UTC,
  snap2, snap3 07:58 UTC, snap4 08:10 UTC — the epoch+size multiset is
  IDENTICAL across first and last snapshots (snap1 vs snap3 diff was only
  a relative-vs-absolute path spelling artifact; epochs and sizes match
  file for file). Last delivery write predates proof start (WEEKLY-KIT.md
  07:53 UTC; SVGs 07:44–07:45; cards 07:45–07:47; PDFs 07:48–07:49).
- (c) Builder session completed: final driver log `run4.log` present, KIT
  written, no further writes. **Pre-flight PASSES — full proof run.**

Read-only scope respected: nothing was written to `~/workspace/weekly-git`,
no `insert.py`, no Discord, no main-chat cards/PDFs, no cron, no shared
scratch cleanup, no edit to the core build, the W43 shipped edition,
`tools/`, or the delivery dir. All proof work lives under
`hidden_files/w45/zh-cn-ru-proof/` (`REPORT.md` + `work/`).
Toolchain: `tools/venv/bin/python` throughout (Python 3.12.3 per KIT).

Documents read before starting: `files/weekly-report-SOP.md`,
`tools/README.md` (notes #7–#22), the edition KIT
(`files/weekly-report-w45-zh-cn-ru/WEEKLY-KIT.md`), the core KIT
(`files/weekly-report-w45-zhcn-core/WEEKLY-KIT.md`), and the W43 shipped
same-pairing KIT (`files/weekly-report-zh-cn-ru/WEEKLY-KIT.md`).

---

## Blocking item

### B-1 — Gate 10, transform solo reproduction: 4/8, not 8/8

**Procedure (exactly as tasked):** fresh copy of the W45 zh-cn core build →
`work/repro-build`, OUT repointed (all 5 content files + render.py, verified
by grep that NO reference to the real edition/core dirs remained) to
`work/repro-out`, the build's `scratch/transform_ru_w45.py` copied into the
fresh copy's `scratch/` (it derives BUILD from its own location, so no path
edit was needed), transform run (exit 0, "TRANSFORM OK"), then the single
one-process driver `run.py` (content12 → 34 → 56 → 7 → 8, in order), output
compared to the delivered SVGs. Log: `work/repro-run.log`,
`work/repro-transform.log`; string diff: `work/repro-vs-delivered.json`
(`freeze.py diff` repro → delivered).

**Result:** P2, P3, P5, P6 byte-identical; **P1, P4, P7, P8 differ.**
Repro hashes (first 16 hex) vs delivered:

| Page | Repro | Delivered |
|---|---|---|
| P1 | b05843dc57afc849 | 3882336be16fc885 |
| P2 | f63257465ce4475c = delivered | f63257465ce4475c |
| P3 | 6631b2e4d3949ed0 = delivered | 6631b2e4d3949ed0 |
| P4 | 65df954e557f2fe6 | af82610d5531ffaa |
| P5 | 5a2173e6b2726380 = delivered | 5a2173e6b2726380 |
| P6 | ffc887409a33ab21 = delivered | ffc887409a33ab21 |
| P7 | ee5282b53454f7a7 | 028afef1fbeda7e |
| P8 | d8b739bb47a10652 | f7dfab8374bee69a |

**String-level diff (repro → delivered, freeze.py diff):**

- P1 +1/−1: the P1 calendar-box line shortening is missing from the
  transform. Repro renders "Команды S16 зависят от швейцарского этапа";
  delivered renders "Команды S16 зависят от этапа" (the fix the KIT
  records after the BOXTITLE flag: right ink 1892.2 > border 1885.0).
- P4 +1/−1: the P4 section-C head translation is missing from the
  transform. Repro renders "C · 读赛程 · Schedule work" — an untranslated
  English head; delivered renders "C · 读赛程 · Читаем расписание"
  (the fix the KIT records as caught by the residual scan).
- P7 +12/−23: the P7 disclosure rewrite + clinic/frame trims are missing
  from the transform. Repro renders the longer first-version disclosure
  ("Пояснение редакции: в VOL.1 было обещано, что в этом номере (VOL.2)
  появятся настоящие письма читателей и лучшее сочинение со страницы 8
  из VOL.1; до сих пор настоящих писем не пришло, и публиковать нечего,
  поэтому здесь снова пример от редакции. Это отсрочка, а не отмена.
  Присылайте ваши письма в редакцию! … лучшие письма мы напечатаем в
  VOL.3.") plus the untrimmed clinic/frame notes ("Частица 地 (de)
  показывает, как совершается действие.", "Конструкция: 先 … 再 … —
  сначала X, потом Y.", etc.); delivered renders the shortened disclosure
  and trimmed notes.
- P8 +31/−59: the `apply_trims.py` tersenings + purity rephrases are
  missing from the transform (the 24+ note trims, e.g. "К полудню
  26 октября Maoyan показывал около 1,192 миллиона юаней." →
  "Maoyan к полудню 26 октября: около 1,192 млн юаней.", and the #101/#104
  pinyin-only rephrases "件 jiàn" / "件， а не 个 или 条" → "jiàn" /
  "jiàn, а не gè или tiáo"). The rest of the ± counts is line reflow
  from those changes.

**The repro run reproduces the builder's pre-fix defects:** 7×
`FLOW OVERFLOW [P8-keys]` warnings (col 3 y=2551…2585, bottom 2540 —
identical to the builder's own `run1.log`), whereas the delivered build's
final driver log has zero warnings. The transform file's mtime
(2026-10-28 07:23) predates the fix-round edits (content files 07:36–07:44,
delivered SVGs 07:44–07:45); its text contains the pre-fix strings.

**Root cause (evidence, not speculation):** the four fix groups above were
applied to the build's content files (via `apply_trims.py` and direct
edits) but never folded back into `transform_ru_w45.py`. The transform
script is therefore a record of the first render, not of the delivered
edition. Note the transform path itself is sound (exact-literal
replacements, whole lines, asserts ≥1 match, exit 0, no AST byte offsets)
— it is simply stale, not broken.

**What this does NOT mean:** the delivered pages are not thereby defective
— every content gate below passed on the delivered files. But SOP §8.4
requires a complete zero-problem round, and the tasking makes transform
solo reproduction a blocking gate: an edition whose build cannot be
replayed from its own record cannot be finalized.

---

## Per-gate evidence (all other gates PASS)

### Gate 1 — Freeze baseline 8/8 + strict-CJK diff: PASS

- `freeze.py baseline --build ../hidden_files/weekly-report-w45-zhcn-build
  --core-svg ../files/weekly-report-w45-zhcn-core/svg --out
  ../hidden_files/w45/zh-cn-ru-proof/work/freeze-baseline`:
  **8/8 SVGs byte-identical** (p1 e057bbfc…, p2 c87aa67e…, p3 d50f09e1…,
  p4 dd3b1b0f…, p5 c71ef315…, p6 b06a85d2…, p7 f2319cb8…, p8 eaf368f8…);
  core SVGs re-hashed unchanged after the run (8 files). Core hashes also
  match the builder's `core-svg-hashes-before.txt` 8/8.
- `freeze.py diff --strict-cjk` core → edition, per page +/− strings and
  CJK core→edition: P1 851→820, P2 1053→1031, P3 812→790, P4 810→789,
  P5 944→922, P6 1005→983, P7 760→647, P8 1102→985; **added CJK = 0 on every
  page (multiset `cjk_added` {}), total 0** — exactly the KIT's numbers.
  CJK-changing build hunks were classified line by line (content12/34/56/
  7/8 vs core build): every one is explanation-layer only — badge
  furniture, English notes citing Chinese words → Russian with pinyin,
  matching-note pinyinisation (keys themselves untouched), P7 heads/paras
  (quoted Chinese examples unchanged), error-clinic notes (particle
  characters 地/得/个/件 kept, as in the core's own note strings), and the
  P7 disclosure Chinese+English → Russian. No article sentence, stem,
  option, or caption changes.
- Build-code diff core build vs RU build: `bslib4.py` differs in EXACTLY
  3 lines (footer left, footer right, gloss prefix `Notes｜` →
  `Пояснение — `); `svglib.py` and `run.py` byte-identical; `render.py`
  differs only in its BASE path. Content-module diffs contain NO
  structural change except the badge line (OLIVE → BRICK, same slot/size)
  and a comment-only change in content7.py; all other changed lines are
  string literals only. OUT repointing verified in all 5 content files.

### Gate 2 — P8 printed-note set: PASS (CLEAN)

- `p8.py compare --core-dir …zhcn-core --edition-dir …zh-cn-ru --target
  zh-cn`: **CLEAN — core 150 noted, edition 150 noted, missing [],
  extra 0, keydiff []**. `p8.py extract` on the delivered P8 independently:
  noted set = 150/150, full list 1–150.
- P8 note style verified from the core's shipped fan-out BUILD CODE, not
  memory: core `content8.py` keys generation is dash style —
  `f"{e_['n']}. {e_['key']} — {e_['note']}"`, writing
  `f"{e_['n']}. ✓ {e_['note']}"` — and the RU build's content8 has zero
  structural diff, so the same code path. Delivered P8 renders dash
  style with `— СТРАНИЦА N —` headers ×8.
- Printed keys vs the independently dumped delivered registry
  (`work/reg-ed.json`, see Registry below): 150 printed keys; the ONLY
  apparent diff is #150, where the registry key
  "(открытый вопрос — образец ниже)" prints as "150. ✓ …" by the writing
  code path — the same rendering the core gives its own #150 device key.
  Not a diff. Key 55 prints 翻盘, matching the registry and the core's
  post-proof-fix article support ("TES一度落后,后来翻盘打赢了G2" present
  on delivered P4).

### Gate 3 — Occlusion audit + same-baseline + chart labels: PASS

- `occlusion_audit.py --selftest`: OK (all 6 planted classes fire exactly
  once, clean controls silent). Full audit on the edition with
  `--core`: **0 flags, core 0 flags, NEW vs core 0**
  (`work/occlusion.json`: `flag_count 0, new_flag_count 0`).
- Same-baseline ink-collision scan (builder's `scratch/rowcheck.py`, copied
  to `work/rowcheck.py`, true ink boxes): edition **0 flags**, core 0 flags.
  P1 top band specifically clean.
- P6 chart-label element check (README #12): bars byte-identical rects —
  810/537/480 px at x=325, y 1282/1340/1398, fills #3e4c2a/#b3a06a/#b3a06a
  — and all six labels identical to the core in position and text
  (A "270 元" x=1151, B "179 元" x=878, C "160 元" x=821). Label clearances
  vs bar ends are 16/16/16 px; no clipping, no sub-30% graze. (The
  edition's P6 col-3 paragraph sits +29.7 y below the core's — a gloss
  reflow shift of the W43-precedent type; audit-clean, see O-4.)
- P8 top rule: last pre-rule test-flow node y=1225.1, rule y=1264, keys
  head y=1302 — clean gap, no touch (core KIT's P8-rule note checked and
  clear on this edition too). P8 keys end at baseline ~2514.9, footer
  line 2580, FOOTER=0.

### Gate 4 — Gloss counts (split on `·` itself): PASS

Rendered `gloss()` strings (AST-extracted from the build, split on `·`,
headwords verified present in the delivered SVGs):

| Page | Core | Edition |
|---|---|---|
| P1 | 4 | 4 |
| P2 | 8 (4+4) | 8 (4+4) |
| P3 | 6 (3+3) | 6 (3+3) |
| P4 | 3 | 3 |
| P5 | 6 (3+3) | 6 (3+3) |
| P6 | 6 (3+3) | 6 (3+3) |
| P7 | 0 (no gloss() calls) | 0 |
| P8 | 0 | 0 |

Item-by-item identical; every gloss headword found in the rendered page
SVG (missing-headwords [] on all 10 boxes). Gloss prefix
`Пояснение — ` on all boxes, matching W43.

### Gate 5 — P7 golden sentences: PASS

All 8 phrases verbatim (rendered full-width punctuation, as in the core)
from this issue's own articles, with correct (Страница N) tags:

| Phrase | Tag | Found in |
|---|---|---|
| 不用等11月11日 | 1 | p1 + p7 |
| 下单就能发货 | 2 | p2 + p7 |
| 先看结算页，再付款 | 2 | p2 + p7 |
| 水开始结冰 | 3 | p3 + p7 |
| 三场都输了 | 4 | p4 + p7 |
| 小局一场没赢 | 4 | p4 + p7 |
| 故事够不够好 | 5 | p5 + p7 |
| 别以后，就现在 | 5 | p5 + p7 |

(Core KIT's table prints two of these with half-width commas; the rendered
SVGs — core and edition alike — use full-width ，, verified by direct
search. The KIT's half-width rendering is typography, not a text
difference.) P7 phrase-tag counts per page (1:1, 2:2, 3:1, 4:2, 5:2,
total 8) equal the core's `(p. N)` counts exactly.

### Gate 6 — Images: PASS

Counts per page: P1 1, P2 1, P3 2, P4 1, P5 1, P6 0, P7 0, P8 0 — 6 total,
as in the core and the KIT. Embedded payload MD5s are byte-identical to
the core asset files AND to the core SVGs' payloads: locker 420c6150…,
valley 550e463b…, frost d0b015bc…, dumplings e8d75277…, lanparty
6b8e9037…, popcorn a903e35f…. Credit lines taken from the Commons API
Artist field (per the identical RU-build and core `assets/CREDITS.md`,
verified 2026-10-27): Map hobby, Paul Gilmore, Gerda Arendt, Syced ×2,
Based5290 — artist names byte-identical; only `Photo:` → `Фото:` and
`Public domain` → `общественное достояние` localised (P5 credit wraps
across two lines: "Фото: Based5290 — общественное достояние (Wikimedia /
Commons)"). File photos captioned 资料图; P4 LAN-party caption states its
real date (2003) and place (France).

### Gate 7 — Readers' corner: PASS (both limbs)

Delivered P7 SVG text, reconstructed verbatim from the wrapped lines
(x=1473, y 1467.7–1694.9):

> Пример письма от редакции — не настоящее письмо. В VOL.1 было обещано
> напечатать здесь настоящие письма и лучшее сочинение VOL.1, но писем
> пока нет — это отсрочка, а не отмена. Присылайте ваши письма! Напишите
> два предложения по-китайски и отправьте их нам: лучшие появятся в VOL.3.

- (a) Disclosure that no genuine letters exist, labelled editor's
  example: "не настоящее письмо" + "писем пока нет". The letter itself is
  the core's frozen Chinese example letter, byte-identical ("「你好！我住
  在上海。立冬那天，我吃了饺子，也给妈妈打了电话。双11，我买了一件毛衣，
  现货第二天就到了。」"). No reader, letter, name, or quotation invented.
- (b) EXPLICIT open invitation for real letters, in Russian:
  "Присылайте ваши письма! Напишите два предложения по-китайски и
  отправьте их нам: лучшие появятся в VOL.3." — not a facts-only
  disclosure, not a teaser line, not another page's exercise prompt
  (the P2/P3/P5 "А вы?" prompts are separate and were not counted).
- Substance vs the core's bilingual disclosure: VOL.1 promise (letters +
  best VOL.1 writing) ✓, none arrived ✓, editor's example ✓,
  deferred-not-cancelled ("это отсрочка, а не отмена") ✓, invitation ✓.
  One compression is noted under O-1 (non-blocking).
- P7 teaser: last text baseline y=2521.6; builder's "ends y=2555.6" is
  baseline + font height, consistent and above the 2580 footer line
  (core: 2554.1). Teaser band read visually on the card: clean, no
  footer intrusion.

### Gate 8 — Furniture three-way + BADGE ADJUDICATION: PASS

Measured from the SVGs (not from KITs):

| Element | Core (zh-cn × en) | W43 shipped zh-cn × ru | This edition |
|---|---|---|---|
| P1 badge | 简体中文正文 · 英语讲解 — … (975, 434), 19.5pt, weight 700, fill #3e4c2a (OLIVE) | ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ (975, 434), 19.5pt, weight 700, fill #a4553a (BRICK) | **Identical to W43: same text, (975, 434), 19.5pt, weight 700, fill #a4553a (BRICK)** |
| P1 top line | 每周读中文 · Read real Chinese, every week (y=92) | 每周读中文 · Читайте настоящий китайский — каждую неделю | Same as W43, verbatim |
| P1 subtitle (y=372) | 给学中文的人的周报 — Read the real China, in Chinese | 给学中文的人的周报 — Настоящий Китай — по-китайски | Same as W43, verbatim |
| Footer left (all 8 pp.) | Lucerna · 简体中文周报 VOL.2 · … English explanations | Lucerna · КИТАЙСКИЙ (УПРОЩЁННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.1 · … | W43 form with VOL.2, verbatim on all 8 pages |
| Page line | 第 N 版 / 共 8 版 | Страница N из 8 | Same as W43, verbatim, all 8 pages |
| Gloss prefix | Notes｜ | Пояснение — | Same as W43, verbatim |
| P8 separators | — Page N — | — СТРАНИЦА N — | Same as W43, verbatim, ×8 |
| P8 note style | Dash (code-verified, Gate 2) | Dash | Dash, same code path |
| Section heads | Chinese · English | Chinese · Russian short forms | W43 Russian forms reused where the Chinese head matches (Жизнь/Культура/Спорт/Молодёжь/Глубокое чтение/Языковой фокус/Тест и ответы; Выбор ответа/Впишите слово/Числа и даты/Сопоставьте пары; Верно или неверно/Большой опрос/Закончите фразы/Читаем и отвечаем/В разговоре/Письмо); new heads in the same short style (Главная тема, Сразу к практике, Содержание, Слово недели, Коротко, Быстрый опрос, Слова для покупок, Упражнения, Расписание S16, Слова матча, Даты фильмов, Главное, Три вопроса, Учебные корзины, Покупки, Время и даты, Читаем новости, Клиника ошибок, Конструкция недели, Уголок читателей, Фразы недели, На следующей неделе (VOL.3)); P6 C head ships as "Считаем" (372.0 px at 25pt, fits; disclosed HEAD TOO WIDE avoidance) |
| Bylines | Lucerna editors · Reading level … | Редакция Lucerna · Уровень чтения … | Same as W43 (A2 / A2→B1 / B1 / B2 per page) |
| Answers line | Answers on page 8 · 答案见第 8 版 | Ответы на странице 8 · 答案见第 8 版 | Same as W43, verbatim (P2–P6) |
| P8 keys head | 答案 · Answer keys — … / All notes in English · ✓ = the writing task | 答案 · Ответы — … / Все примечания на русском · ✓ = письменное задание | Same as W43 |
| Writing glossline + model prefix | Writing — … / Model answer: | Письмо — единственно верного ответа нет. Ниже — образец из N иероглифов. / Образец: | Same as W43 |

**BADGE ADJUDICATION (required):** the zh-cn family in-place slot applies
here (the core's y=372 is the FROZEN bilingual strapline
给学中文的人的周报 — …, so the badge does NOT take the subtitle slot; it
sits at y=434 below the rules, exactly as in W43 zh-cn × ru). Measured:
core badge (975, 434) 19.5pt OLIVE #3e4c2a; W43 shipped badge (975, 434)
19.5pt weight-700 BRICK #a4553a; this edition's badge (975, 434) 19.5pt
weight-700 BRICK #a4553a — **exactly matching the W43 shipped
same-pairing SVG**. The parallel zh-cn×fr failure (olive inherited from
the core) does NOT occur here: the colour change OLIVE → BRICK is present
in the build code (`content12.py` badge line) and in the render. **Badge
gate PASSES.**

### Gate 9 — Web PDF regeneration: PASS (with timestamp note, O-3)

- Rendered from the delivered cards via the build's `render.py` in
  `work/webregen` (ED redirected): cards **8/8 byte-identical** to the
  delivered cards; print PDF **byte-identical** to the delivered print
  PDF (sha256 a938d5a679a88bc675d347ab60644fd0bcc41ac7d73c3f4584610843176190c1,
  38,103,379 B, 8 pages).
- Delivered web PDF verified against the KIT pins: 3,252,467 B (< 10 MB),
  8 pages, sha256
  cf7fbef3ebbd30392abbd847250a22464d043db5da150841b98459f9fe7db634 — **matches
  the KIT exactly**.
- Regenerated web PDF: same size 3,252,467 B, 8 pages, all 8 page-image
  payloads byte-identical to the delivered web PDF's (hashes dc8fe769…,
  1c9395fa…, 4576f392…, 289f3fec…, 8a0bf92a…, 41a93a08…, 40a7187e…,
  92f7a847…), identical PDF skeleton. Its file SHA differs
  (7206abaa001dad2c…) for exactly one reason: Pillow stamps
  CreationDate/ModDate with the wall clock (delivered 20261028074917Z vs
  regen 20261028080826Z) — the ONLY byte difference in the file. No
  re-run at a different time could ever reproduce the KIT pin; the
  delivered file's pin is verified, and the content reproduces exactly.
  See O-3.

### Gate 10 — Transform solo reproduction: FAIL (see B-1)

4/8 byte-identical (P2, P3, P5, P6); P1, P4, P7, P8 differ for the four
fix groups itemised in B-1. **BLOCKING.**

### Gate 11 — All 8 cards visual: PASS

Every delivered card read in full (P1–P8): masthead furniture, badge,
footers, gloss boxes, photos + credits, schedule box, chart, clinic/
frame/readers'-corner boxes, phrases, teaser band, test sections, and the
full keys area are clean — no overflow, no overlap, no footer intrusion,
no missing content. Specifics: P1 calendar box + contents + photo; P2
word cards + exercises 11–28; P3 frost/dumpling photos + exercises 29–46;
P4 LAN-party file photo + schedule + exercises 47–64 (Q55 stem in place,
article support present); P5 popcorn photo + film dates + exercises
65–82; P6 chart bars/labels + exercises 83–100; P7 three level columns +
clinic + frame + readers' corner (disclosure + invitation legible) +
phrases + teaser band; P8 sections A–F + writing model + keys 1–150
grouped by page, ending well above the footer.

### Registry (independent re-run of the delivered build code)

Copied the delivered RU build to `work/reg-build` (OUT repointed to
`work/reg-out-ed`) and the core build to `work/reg-core`, ran the
one-process driver in each with a registry dump (`work/reg-ed.json`,
`work/reg-core.json`):

- TOTAL **150**, A2 **56** / B1 **69** / B2 **25**; by page
  10/18/18/18/18/18/12/38; by type 完成句子 68 / 单选 50 / 词语配对 20 /
  完形单选 11 / 写作 1 — identical in both builds and identical to the
  core KIT's authoritative numbers.
- n/page/level/type diffs: **none**. Key diffs: **exactly one — #150**,
  "(开放题，范文如下)" → "(открытый вопрос — образец ниже)", a device
  item in the same category as the W43 zh-cn × ru KIT §4 precedent (and
  the only key-arg change in the whole build diff). Its note is likewise
  translated ("Открытый вопрос — образец напечатан выше, в разделе F
  (172 иероглифов)"). The other 149 keys are byte-identical to the core.
- Writing model: **172 characters** in both builds (driver print +
  independent recount of MODELO, 5 parts, spaces removed).
- Notes purity: **150/150 notes contain Cyrillic; 0 contain CJK; 0
  contain full-width parentheses** (the two P7 measure-word notes are
  pinyin-only: "jiàn" / "jiàn, а не gè или tiáo"; the characters remain
  visible in stems/options, and the clinic particle characters are the
  teaching point, already in the core's note strings).
- English-residue scan: visible-text scan of all 8 delivered SVGs for
  English explanation words (the/and/page/Nov/Oct/English/Notes/Photo/
  Fill/Match/Read/Choose/Answers/…) returns **zero hits**; a string-literal
  scan of the build's content files finds no English explanation leftover
  (the single word-boundary hit, content8.py L114 `by_page`, is a code
  variable, not rendered text). Remaining Latin is frozen brands
  (JD.com, Taobao, Tmall, WeChat, S16, LPL, Maoyan), pinyin, option
  letters, and level codes.
- Final driver log (independent re-run of the delivered code): **0 FLOW
  OVERFLOW / 0 HEAD TOO WIDE** warnings.
- Adjudicated builder claims, all confirmed:
  - P7 teaser ends y=2555.6 (baseline 2521.6 + font), footer line 2580 ✓.
  - P8 keys end well above footer (last key baseline ~2514.9) ✓.
  - Shortened P1 calendar line drops «швейцарского»: the Swiss-stage
    reference survives — the same box's note directly above reads
    "Швейцарский этап заканчивается 1 ноября, поэтому на момент сдачи
    номера четвертьфиналисты ещё неизвестны. Четвертьфиналы пройдут
    4–7 ноября, первый полуфинал — 8 ноября, всё в 06:00 по пекинскому
    времени." No information is lost on the page. (The shortened line
    itself is also the B-1 P1 repro item — the fix is real and correct;
    it is only missing from the transform record.)
  - «млн» confined to the single #67/#126 note wording ("Maoyan к
    полудню 26 октября: около 1,192 млн юаней."), standard Russian
    abbreviation, same figure 1,192; the #71 note keeps the full form
    ("около 1,192 миллиона юаней"). ✓
  - «южное блюдо» for the tangyuan note (#37): the stem itself says
    南方有的地方吃___, so the southern link is preserved on the page. ✓
  - 24+ wrap-tested P8 note tersenings: 18 spot-checked (#20, #35, #37,
    #53, #67, #71, #77, #87, #91, #92, #101, #104, #107, #109, #111, #126,
    #133, #139) — keys and levels identical in every case; facts kept in
    substance (see O-2 for two qualifier compressions).
  - #150 is truly registry-only and matches the W43 precedent form. ✓
- Trend/fact sources: inherited from the core KIT without re-verification
  (17:52 Start-of-Winter source chain, S16 2026-10-27 cutoff caveats) —
  noted as inherited, NOT re-verified. No NEW error in how the edition
  renders those facts was found; core-inherited facts are not failed here.

### Abstract: PASS

`ABSTRACT.txt`: single line (1 newline, 417 chars), 0 ASCII double quotes,
written natively in Russian, naming the issue's real topics (Double 11
spot sales + direct cuts, Start of Winter Saturday 7 November, S16
Worlds quarter-finals, AI film Sanxingdui: Future Past, winter film We
Only Have One Life), a learner search phrase ("учи китайский, читая
настоящие китайские новости"), the masthead (Lucerna), the target
language name, A2–B2 levels, and the 150-exercise count. Facts only from
this issue.

---

## Non-blocking observations (NOT blocking items — do not mix with B-1)

- **O-1 — P7 disclosure compression (substance inherited, wording
  compressed).** The core's disclosure says both "至今没有收到真实来信"
  (no real letters received) AND "也没有可刊登的投稿" (no publishable
  submission). The Russian version states the letters limb explicitly
  ("писем пока нет") and conveys the writing limb implicitly (the promise
  sentence names "лучшее сочинение VOL.1", the corner still prints the
  editor's example, and the whole promise is "отсрочка, а не отмена").
  All five facts the task lists (VOL.1 promise, none arrived, editor's
  example, deferred-not-cancelled, invitation) are present; the
  writing-submission absence is implied rather than separately stated.
  The mandatory Gate-7 limbs (disclosure + explicit invitation) are fully
  met, so this is an observation, not a failure. A future round could
  add "и работ на конкурс пока нет" for exactness — but that would be a
  new text change requiring a fresh proof round, and it must NOT be
  folded into this round's fix without re-proof.
- **O-2 — Two note tersenings compress qualifiers that survive elsewhere
  on the page.** #35 drops "(1st micro-season)" from the 水始冰 note
  (the ordinal is taught in the P3 article 一候 and the stem
  "立冬一候是___"); #37 compresses "eaten in some southern places" to
  "южное блюдо" (the stem preserves 南方有的地方吃). Keys, levels,
  figures, and dates are unchanged in all 18 spot-checked tersenings.
  Not a factual error; noted for the record.
- **O-3 — Web-PDF regen SHA differs only by Pillow timestamps** (see
  Gate 9). The delivered file matches its KIT pin; the content reproduces
  exactly. Not a defect.
- **O-4 — P6 col-3 paragraph y shifted +29.7 vs the core** (gloss reflow,
  same type as the W43 §9.9 shift). Audit-clean, visually clean. Not a
  defect.

---

## Limitations (stated plainly)

- Trend/fact sources (Double 11 timetable, Start-of-Winter 17:52 chain,
  S16 results through the 2026-10-27 cutoff, film figures) were inherited
  from the core KIT and NOT independently re-verified, per the tasking;
  the core's own caveats (17:52 not independently second-confirmed; S16
  cutoff honestly dated) carry over.
- The visual card read was performed on the delivered 1950×2700 PNG cards
  (byte-identical to the regen cards); no separate print-PDF page raster
  was eyeballed, but the print PDF is byte-identical to the regen from
  the same SVGs.
- The "U+FFFD" glyphs seen in one intermediate diff dump were a display
  artifact of that dump, not file content: a byte-level scan found 0
  U+FFFD in all RU build content files and in the delivered P8 SVG, and
  the affected string ("Начало зимы — 7 ноября.") renders correctly.
- Sibling-edition processes (JA) were running on the VM during proof;
  they touched only their own dirs and had exited before the final
  snapshot. The pre-flight conclusion rests on the RU dirs' own mtimes
  (unchanged 07:53 → 08:10) plus the process/FD sweeps, not on the absence
  of all VM activity.

---

## Delivered-file pins (measured, not carried over)

- Print PDF `Lucerna-VOL2.pdf`: 38,103,379 B, 8 pages, sha256
  `a938d5a679a88bc675d347ab60644fd0bcc41ac7d73c3f4584610843176190c1`
- Web PDF `Lucerna-VOL2-web.pdf`: 3,252,467 B, 8 pages, sha256
  `cf7fbef3ebbd30392abbd847250a22464d043db5da150841b98459f9fe7db634`
- Delivered SVGs (sha256): p1
  3882336be16fc8855ad145c039668f681868c8e598d6776d22316b0da95abf42,
  p2 f63257465ce4475c7cd10e52033c39fdfa460b14a1e42e8a725aea2849e5e41e,
  p3 6631b2e4d3949ed0c4eb05c357b4324796ccd1f1daf0cdee68943d5faf5f9459,
  p4 af82610d5531ffaa842d6fee63ce8214403e1d0f42f015c79fc586c8784745d1,
  p5 5a2173e6b272638020b96aa1e169e6f14e809018059355206c29f5f6bf6005ec,
  p6 ffc887409a33ab21a11a5a8067a68778b412a661047a4ebdba6f282461f857a8,
  p7 028afef1fbeda7e9764b5a08fbfae1ad6ac2685fee5cb126b24b6698fb297fa9,
  p8 f7dfab8374bee69a7cbef07232eb219b2bc2aa55d37b40ea636dbaa25f53dcb9
- Report: `hidden_files/w45/zh-cn-ru-proof/REPORT.md`; scratch evidence
  under `hidden_files/w45/zh-cn-ru-proof/work/` (mtime snapshots,
  `freeze-diff.json`, `occlusion.json`, `repro-vs-delivered.json`,
  `repro-run.log`, `repro-transform.log`, `reg-ed.json`,
  `reg-core.json`, `p8-ed.json`, `rowcheck.py`, `webregen/`).

**Final statement: NOT PASS on blocking item B-1 only. The edition is NOT
declared finalized and NOT declared shipped — the coordinator inserts
nothing until the transform is consolidated, transform-alone replays 8/8,
and a fresh full proof round passes.**
