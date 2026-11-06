# INDEPENDENT RE-PROOF — W45 zh-cn × ru (Simplified Chinese target · Russian reader)

**Verdict: PASS — ZERO PROBLEMS across all gates, including Gate 10.
This report is the finalization evidence for the coordinator's insert.**

The first proof (`hidden_files/w45/zh-cn-ru-proof/REPORT.md`) was NOT PASS
on one item only — Gate 10 (transform-solo reproduction 4/8). The fix
round (`hidden_files/weekly-report-w45-zh-cn-ru-build/scratch/FIX-GATE10.md`)
folded 30 transform edits into `scratch/transform_ru_w45.py`. This round
re-verified EVERYTHING independently from scratch, not by copying the
first proof or the fix log. The delivered paper itself is unchanged
since the first proof (all 18 delivered files hash-identical at start,
mid-round, and close).

Read before starting: `files/weekly-report-SOP.md`, `tools/README.md`
(notes #7–#22), the first proof REPORT.md, the fix log FIX-GATE10.md,
the edition KIT, the core KIT, and the W43 same-pairing KIT.

Scope respected: nothing written to `~/workspace/weekly-git`, no
`insert.py`, no Discord, no main-chat cards/PDFs, no cron, no shared
scratch cleanup, no edit to the core build, the W43 shipped edition,
`tools/`, `tables.json`, or the delivery dir. All proof work lives under
`hidden_files/w45/zh-cn-ru-reproof/` (`REPORT.md` + `work/`).
Toolchain: `tools/venv/bin/python` throughout.

---

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER) — PASSES

- (a) No live worker writing to the delivery/build dirs: `ps` sweeps at
  start found no process mentioning zh-cn-ru paths and no
  `transform_ru`/`run.py`/`render.py` worker. The only other process
  seen was a sibling zh-tw-de pre-flight snapshot job (sleep + find),
  which touches only zh-tw-de dirs. An open-FD scan found nothing
  under the zh-cn-ru dirs.
- (b) mtime snapshots of BOTH dirs (epoch+size multiset, delivery +
  build): snap1 08:26, snap2 08:29, snap3 08:30 UTC — all three
  IDENTICAL. A closing snapshot matches snap1 exactly. Last delivery
  write predates this round (WEEKLY-KIT.md 08:22, transform 08:18 —
  both from the fix session, before proof start 08:26).
- (c) Fix session completed: FIX-GATE10.md filed, transform post-fix
  sha256 `ffb71d1b8f00575961c4b3b4244e4897b302b4948d7806d67dc72919320346e6`
  (matches the fix log's claimed post-fix sha exactly — the transform
  was not touched after the fix).
- **Pre-flight PASSES — full proof run.**

Method note (honest, no effect on the verdict): the first repro run's
sed-based OUT repoint left the `~` prefix in place, so the driver wrote
its 8 SVGs into a nested junk path under the goal dir
(`.../lucernaread-social-media-operations/home/hatch/.../repro-out/svg/`)
instead of `work/repro-out/`. That run's SVGs were themselves already
8/8 byte-identical to the delivered SVGs, delivery hashes were verified
unchanged immediately afterwards, the junk tree (9 files: 8 SVGs +
1 probe) was removed in full, the script was fixed to replace whole
OUT/BASE lines, and the reproduction was re-run cleanly. All Gate 10
evidence below comes from the clean rerun.

---

## Per-gate evidence (all PASS)

### Gate 1 — Pre-flight + delivery hash verification (start AND close): PASS

Start hashes = fix log's pre-fix pins = close hashes, all 18 files
(8 SVGs, 8 cards, print + web PDFs, ABSTRACT.txt); see "Delivered-file
pins" below. Mid-round check after the repro runs also identical.
Any change during the round would have stopped the proof; none occurred.

### Gate 2 — Gate 10, DOCUMENTATION CHAIN (the fixed item): PASS

Procedure (exactly as tasked): fresh copy of the W45 zh-cn core build →
`work/repro-build`, fixed `scratch/transform_ru_w45.py` copied into the
fresh copy's `scratch/` (it derives BUILD from its own location, so no
path edit was needed), transform run alone, then OUT/BASE repointed by
whole-line replacement to `work/repro-out` (verified by grep: NO
reference to the real edition/core dirs remained), then the single
one-process driver `run.py` (content12 → 34 → 56 → 7 → 8). No post-step
was run: `apply_trims.py` was never executed. Logs: `work/repro-transform.log`,
`work/repro-run.log`; script: `work/repro.sh`.

- Transform exit **0**, "TRANSFORM OK", **zero ZERO-match lines**.
- Driver exit **0**, TOTAL **150** (A2 56 / B1 69 / B2 25; by page
  10/18/18/18/18/18/12/38; by type 完成句子 68 / 单选 50 / 词汇配对 20 /
  完形单选 11 / 写作 1), writing model 172 chars.
- **0 FLOW OVERFLOW / 0 HEAD TOO WIDE** warnings — all 7 pre-fix
  P8-keys overflows are gone.
- **8/8 SVGs byte-identical to the delivered SVGs** (p1–p8, see pins).
- Repro build sources vs real RU build sources (OUT/BASE lines
  excluded): **identical for all 8 files** (content12/34/56/7/8,
  bslib4, svglib, run.py) — transform-alone now reproduces the build
  sources byte-for-byte.

Folded groups verified individually against the fix log (not assumed):

- P1 (content12): calendar BOXTITLE shortening present in the
  transform (`S16 teams depend on the Swiss stage` →
  `Команды S16 зависят от этапа`); delivered P1 renders the shortened
  line.
- P4 (content34): section-C head translation present as an ADD
  (`C · 读赛程 · Schedule work` → `C · 读赛程 · Читаем расписание`);
  delivered P4 renders `Читаем расписание`, and `Schedule work`
  occurs 0 times in the delivered P4 SVG. Trim NEW literals present
  in repro content34: **7**, matching the fix log.
- P7 (content7): disclosure rewrite present (delivered shortened
  disclosure + invitation as the transform target); clinic/frame
  trims present (4: 地/得/时间/先…再…); measure-word purity rephrases
  present (2: `毛衣 takes the measure word 件 jiàn` → `Для свитера
  счётное слово — jiàn`; `Clothes take 件, not 个 or 条` →
  `Для одежды — jiàn, а не gè или tiáo`).
- P8 (all of `apply_trims.py`): all **24 distinct trim NEW literals**
  are present in the transform (0 missing), all 24 present in the
  repro build, 0 intermediate OLD literals leftover in the repro
  build. Per-file occurrence counts in the repro build (shared
  literals counted per file): content12 1, content34 7, content56 8,
  content7 8, content8 8 — consistent with the fix log's "7 shared
  across 2–3 files' pairs". The transform's OLD literals are the
  core's English originals (not the intermediate long Russian forms),
  which is why the intermediate forms correctly do not appear in the
  transform; the direct core→final mapping is what makes the
  post-step redundant.
- Redundancy of `apply_trims.py` confirmed: transform-alone output
  is 8/8 byte-identical with no post-step run, and the repro build
  sources equal the real build sources. `apply_trims.py` remains on
  disk as history only.
- The one extra hunk is **comment-only, verified**: the transform
  replaces a 3-line `# NOTE:` comment in content7.py (line 93 in both
  core and repro builds) — old text ("the disclosure above mixes
  Chinese and English in one string…") → new text ("the disclosure
  above is Russian-only in this edition…"). Both versions are pure
  `#` comment lines; no code line is touched; the repro build's
  content7.py is SRC-IDENTICAL to the real build's. It cannot affect
  rendered output, and Gate 10 passes 8/8 with it in place. No gate
  is failed on the comment.

### Gate 3 — Freeze baseline 8/8 + strict-CJK diff: PASS

- `freeze.py baseline` on the unmodified core build: **8/8 SVGs
  byte-identical** (p1 e057bbfc…, p2 c87aa67e…, p3 d50f09e1…,
  p4 dd3b1b0f…, p5 c71ef315…, p6 b06a85d2…, p7 f2319cb8…,
  p8 eaf368f8…); core SVGs re-hashed unchanged after the run (8 files).
  Core hashes match the builder's `core-svg-hashes-before.txt` 8/8 and
  the first proof's baseline.
- `freeze.py diff --strict-cjk` core → edition: CJK core→edition
  P1 851→820, P2 1053→1031, P3 812→790, P4 810→789, P5 944→922,
  P6 1005→983, P7 760→647, P8 1102→985; **added CJK = 0 on every page,
  total 0** — exactly the KIT's numbers.

### Gate 4 — p8.py CLEAN + notes purity: PASS

- `p8.py compare`: **CLEAN — core 150 noted, edition 150 noted,
  missing [], extra 0, keydiff []**. `p8.py extract` on the delivered
  P8 independently: noted set = 150/150 (1–150).
- Registry notes (independent dump from a repointed copy of the
  delivered build, `work/reg-ed.json`): **150/150 contain Cyrillic;
  0 contain CJK; 0 contain full-width parentheses**. The two P7
  measure-word notes are pinyin-only as designed.
- P8 note style: dash style with `— СТРАНИЦА N —` headers ×8,
  same code path as the core (build diff contains no structural
  change to content8.py's keys generation).

### Gate 5 — Occlusion audit + same-baseline + chart labels: PASS

- `occlusion_audit.py --selftest`: OK (all 6 planted classes fire
  exactly once, clean controls silent). Full audit on the edition
  with `--core`: **0 flags, core 0 flags, NEW vs core 0**
  (`work/occlusion.json`).
- Same-baseline ink-collision scan (`work/rowcheck.py`, true ink
  boxes): edition **0 flags**, core 0 flags.
- P6 chart-label element check: bars byte-identical rects —
  810/537/480 px at x=325, y 1282/1340/1398, fills
  #3e4c2a/#b3a06a/#b3a06a — and all six labels identical to the core
  in position and text (A "270 元" x=1151 y=1310, B "179 元" x=878
  y=1368, C "160 元" x=821 y=1426, 24pt). No clipping, no graze.
- P8 top rule: rule line y=1264; keys head follows below it; keys
  end at baseline 2514.92, footer line 2580 — clean gap.
  P7 teaser: last text baseline 2521.6, ends 2555.6, above 2580.

### Gate 6 — Gloss counts: PASS

Rendered `gloss()` strings (extracted in source order from the
repointed build copies, split on `·` itself), edition = core on
every page:

| Page | Core | Edition |
|---|---|---|
| P1 | 4 | 4 |
| P2 | 8 (4+4) | 8 (4+4) |
| P3 | 6 (3+3) | 6 (3+3) |
| P4 | 3 | 3 |
| P5 | 6 (3+3) | 6 (3+3) |
| P6 | 6 (3+3) | 6 (3+3) |
| P7 | 0 | 0 |
| P8 | 0 | 0 |

10 gloss boxes total; every gloss headword (CJK run of each item)
found in its page SVG (missing-headwords []). Gloss prefix
`Пояснение — ` on all boxes (counts per page 1/2/2/1/2/2),
matching W43.

### Gate 7 — P7 phrases: PASS

All 8 phrases verbatim from this issue's own articles, with correct
(Страница N) tags (counts 1:1, 2:2, 3:1, 4:2, 5:2, total 8, equal
to the core's counts). Four phrases are line-wrap split in the raw
source-page SVGs and were confirmed via joined text-node order:

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

### Gate 8 — Images: PASS

Counts per page: P1 1, P2 1, P3 2, P4 1, P5 1, P6 0, P7 0, P8 0 —
6 total, as in the core and the KIT. Embedded payload MD5s are
byte-identical to the core asset files AND to the core SVGs'
payloads: locker 420c6150…, valley 550e463b…, frost d0b015bc…,
dumplings e8d75277…, lanparty 6b8e9037…, popcorn a903e35f….
Credit lines: artist names byte-identical to the core's
(Map hobby, Paul Gilmore, Gerda Arendt, Syced ×2, Based5290);
only `Photo:` → `Фото:` and `Public domain` →
`общественное достояние` localised. P5 credit wraps across two
lines ("Фото: Based5290 — общественное достояние (Wikimedia /
Commons)"). File photos captioned 资料图; P4 LAN-party caption
states its real date (2003) and place (France). Commons API was
NOT re-queried this round (see Limitations); the credit source is
the build's `assets/CREDITS.md` (Commons API Artist field, verified
2026-10-27) plus byte-identity to the core SVGs' credits.

### Gate 9 — Readers' corner: PASS (both limbs)

Delivered P7 SVG text (joined text-node order):

> Пример письма от редакции — не настоящее письмо. В VOL.1 было
> обещано напечатать здесь настоящие письма и лучшее сочинение VOL.1,
> но писем пока нет — это отсрочка, а не отмена. Присылайте ваши
> письма! Напишите два предложения по-китайски и отправьте их нам:
> лучшие появятся в VOL.3.

- (a) Disclosure that no genuine letters exist, labelled editor's
  example: "не настоящее письмо" + "писем пока нет".
- (b) EXPLICIT open invitation: "Присылайте ваши письма! … лучшие
  появятся в VOL.3."
- The letter itself is the core's frozen Chinese example letter,
  byte-identical in joined text (with brackets) in both the edition
  and core P7. No reader, letter, name, or quotation invented.
- The P2/P3/P5 "А вы?" prompts are separate and were not counted.

### Gate 10 — Furniture three-way (core EN · W43 ru · this edition): PASS

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
| P8 note style | Dash | Dash | Dash, same code path |
| P8 keys head | 答案 · Answer keys — … / All notes in English · ✓ = the writing task | 答案 · Ответы — … / Все примечания на русском · ✓ = письменное задание | Same as W43 |
| Writing glossline + model prefix | Writing — … / Model answer: | Письмо — единственно верного ответа нет. Ниже — образец из N иероглифов. / Образец: | Same as W43 |
| Section heads | Chinese · English | Chinese · Russian short forms | W43 Russian forms reused where the Chinese head matches; new heads in the same short style (incl. P4 C "Читаем расписание"); P6 C ships as "Считаем" (372.0 px at 25pt, fits; disclosed HEAD TOO WIDE avoidance) |
| Bylines | Lucerna editors · Reading level … | Редакция Lucerna · Уровень чтения … | Same as W43 (A2 / A2→B1 / B1 / B2 per page) |
| Answers line | Answers on page 8 · 答案见第 8 版 | Ответы на странице 8 · 答案见第 8 版 | Same as W43, verbatim (P2–P6) |

**BADGE ADJUDICATION:** the zh-cn family in-place slot applies (the
core's y=372 is the FROZEN bilingual strapline, so the badge does
NOT take the subtitle slot; it sits at y=434 below the rules,
exactly as in W43). Measured: core badge (975, 434) 19.5pt weight-700
OLIVE #3e4c2a; W43 shipped badge (975, 434) 19.5pt weight-700 BRICK
#a4553a; this edition's badge (975, 434) 19.5pt weight-700 BRICK
#a4553a — **exactly matching the W43 shipped same-pairing SVG**.
The parallel zh-cn×fr olive-inheritance failure does NOT occur here.
`tables.json` was NOT edited (mtime 2026-10-22, predates this round);
no discrepancy required adjudication against tables.json.

### Gate 11 — English residue 0 + sole key diff #150: PASS

- Visible-text scan of all 8 delivered SVGs for English explanation
  words (the/and/page/Nov/Oct/English/Notes/Photo/Fill/Match/Read/
  Choose/Answers/Schedule work/…) returns **zero hits**; remaining
  Latin is frozen brands (JD.com, Taobao, Tmall, WeChat, S16, LPL,
  Maoyan), pinyin, option letters, and level codes.
- Independent core-vs-edition registry comparison (repointed copies
  of both builds, `work/reg-core.json` vs `work/reg-ed.json`):
  n/page/level/type diffs: **none**; key diffs: **exactly one — #150**,
  "(开放题，范文如下)" → "(открытый вопрос — образец ниже)", a
  device item in the same category as the W43 zh-cn × ru KIT §4
  precedent. Its note is likewise translated ("Открытый вопрос —
  образец напечатан выше, в разделе F (172 иероглифов)"). The other
  149 keys are byte-identical to the core. Key 55 prints 翻盘,
  matching the registry and the core's article support.
- Writing model: **172 characters** in both builds (driver print +
  registry run). P8 printed-key rendering of #150 ("150. ✓ …") is
  the core's own device-key code path, not a diff.
- Delivered-build re-render (repointed copy of the real RU build):
  SVGs **8/8 byte-identical to the delivered SVGs**.

### Gate 12 — Web regen: PASS (with timestamp note, O-3)

- Rendered from copies of the delivered SVGs via the build's
  `render.py` in `work/webregen` (BASE redirected): cards **8/8
  byte-identical** to the delivered cards; print PDF **byte-identical**
  to the delivered print PDF (sha256 a938d5a6…6190c1, 38,103,379 B,
  8 pages).
- Delivered web PDF verified against the KIT pins: 3,252,467 B,
  8 pages, sha256 cf7fbef3…db634 — **matches the KIT exactly**.
- Regenerated web PDF: same size 3,252,467 B, 8 pages, all 8
  page-image payloads byte-identical to the delivered web PDF's
  (dc8fe769…, 1c9395fa…, 4576f392…, 289f3fec…, 8a0bf92a…, 41a93a08…,
  40a7187e…, 92f7a847…), identical page sizes (1400×1938).
  Its file SHA differs (c26a48a3…) for exactly one reason, stated
  explicitly: Pillow stamps CreationDate/ModDate with the wall clock
  (delivered D:20261028074917Z vs regen D:20261028083738Z) — after
  normalising only those two date fields, the files are
  **byte-identical**. No re-run at a different time could ever
  reproduce the KIT pin; the delivered file's pin is verified, and
  the content reproduces exactly.

### Gate 13 — All 8 cards visual: PASS

Every delivered card read in full (P1–P8): masthead furniture, badge,
footers, gloss boxes, photos + credits, schedule box, chart, clinic/
frame/readers'-corner boxes, phrases, teaser band, test sections, and
the full keys area are clean — no overflow, no overlap, no footer
intrusion, no missing content. Specifics: P1 calendar box (shortened
line in place) + contents + photo; P2 word cards + exercises 11–28;
P3 frost/dumpling photos + exercises 29–46 (Q35 stem "立冬一候是___",
Q37 stem "南方有的地方吃___" visible); P4 LAN-party file photo +
schedule + section-C head "Читаем расписание" + exercises 47–64
(Q55 stem in place); P5 popcorn photo + film dates + exercises
65–82; P6 chart bars/labels unclipped + exercises 83–100; P7 three
level columns + clinic + frame + readers' corner (disclosure +
invitation legible) + phrases + teaser band; P8 sections A–F +
writing model + keys 1–150 grouped by page, ending well above the
footer.

### Gate 14 — ABSTRACT.txt: PASS

Single line (722 bytes, 1 trailing newline), **0 ASCII double
quotes**, written natively in Russian, naming the issue's real topics
(Double 11 spot sales + direct cuts, Start of Winter Saturday
7 November, S16 Worlds quarter-finals, AI film Sanxingdui: Future
Past, winter film We Only Have One Life), a learner search phrase
("учи китайский, читая настоящие китайские новости"), the masthead
(Lucerna), the target language name (китайском (упрощённом)),
A2–B2 levels, and the 150-exercise count. sha256
c6c2a28e666ec89865f2ddda7f2a7de4e5c459b008a6a460c14a39348d3d9301 —
unchanged since the fix log (paper untouched by the fix). Facts only
from this issue.

### Gate 15 — First-proof non-blocking notes re-checked: PASS (unchanged)

- P7 disclosure compression (O-1): re-read in the delivered P7.
  The Russian version states the letters limb explicitly ("писем
  пока нет") and conveys the writing-submission limb implicitly (the
  promise sentence names "лучшее сочинение VOL.1", the corner still
  prints the editor's example, the whole promise is "отсрочка, а не
  отмена"). All five substance facts (VOL.1 promise, none arrived,
  editor's example, deferred-not-cancelled, invitation) are present.
  The paper is unchanged since the first proof, so this remains a
  non-blocking observation, not a failure — and it must NOT be
  "fixed" without a fresh proof round.
- #35/#37 qualifier compressions (O-2): re-verified in the delivered
  P8. #35 drops "(1st micro-season)" from the 水始冰 note, but the
  ordinal is taught in the P3 article 一候 and the stem
  "立冬一候是___", and the P8 keys themselves carry "Первый
  микросезон" at #31/#123. #37 compresses "eaten in some southern
  places" to "южное блюдо", but the stem preserves 南方有的地方吃.
  Keys, levels, figures, and dates unchanged. Not a factual error.

---

## Non-blocking observations (NOT blocking items — do not mix with the verdict)

- **O-1 — P7 disclosure compression** (see Gate 15): the
  writing-submission absence is implied rather than separately
  stated. Observation only.
- **O-2 — Two note tersenings compress qualifiers that survive
  elsewhere on the page** (see Gate 15): #35, #37. Observation only.
- **O-3 — Web-PDF regen SHA differs only by Pillow timestamps**
  (see Gate 12). The delivered file matches its KIT pin; the content
  reproduces exactly. Not a defect.
- **O-4 — P6 col-3 paragraph y shift (carried over, not re-measured
  this round):** the first proof measured +29.7 y vs the core (gloss
  reflow, same type as the W43 §9.9 shift). This round verified the
  P6 card visually clean and the occlusion audit 0 flags, but did
  not re-measure the shift itself. Not a defect on the evidence
  available.

---

## Limitations (stated plainly)

- Trend/fact sources (Double 11 timetable, Start-of-Winter 17:52
  chain, S16 results through the 2026-10-27 cutoff, film figures)
  were inherited from the core KIT and NOT independently re-verified,
  per the tasking; the core's own caveats carry over. No NEW error
  in how the edition renders those facts was found.
- The Commons API was NOT re-queried this round: image credits rest
  on the build's `assets/CREDITS.md` (Commons API Artist field,
  verified 2026-10-27) plus byte-identity of artist names and payload
  MD5s to the core's shipped SVGs/assets.
- The visual card read was performed on the delivered 1950×2700 PNG
  cards (byte-identical to the regen cards); no separate print-PDF
  page raster was eyeballed, but the print PDF is byte-identical to
  the regen from the same SVGs.
- The "U+FFFD" glyphs seen in one intermediate registry dump were a
  display artifact of that dump, not file content: a byte-level scan
  found 0 U+FFFD bytes in all registry records and in all 8 delivered
  SVGs, and the affected strings ("Четвертьфиналы — в 06:00 по
  пекинскому времени." etc.) are correct in the files.
- The gloss AST walk found 0 `gloss()` calls (the build invokes gloss
  through a wrapper, not a bare `gloss(` call); gloss counts were
  therefore taken from source-order string extraction, cross-checked
  against the core's identical extraction and against headword
  presence in the rendered SVGs. The counts are exact, not estimated.

---

## Delivered-file pins (measured at start AND close — identical)

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
- Delivered cards (sha256): p1
  f10e22c3c1ed1b2f0515afac74753f27ad50cc3f8a0fa47448ed5785523b7151,
  p2 d03f0382465d0edadfd2f00c44063884a015fcf6c002e7fcf4d2e482bc09232b,
  p3 858ad9ee40563f19cfb823b37b3f7fab8bf8b1b8282627777308b92ba3895282,
  p4 7f615ec6b66b11a0ec2acb81e066dafb609ff6136e52fa32c3a053ccb23204d5,
  p5 8476268be39bead8dc84fe8f65878eb0af4209073be45635544379b495cbe2bf,
  p6 8a24cbb969e11335d3243c59bdda6192e478f8a57be34d1a23f1d784a15d81dc,
  p7 0abba4e626f558a942d6dd46cf9ad80863fa50c99a944507210865b83dd52982,
  p8 5c6ac1a04fe7d6ba6c236bab3842f7ac31d7829ea9de0f10d008fa799ce3652b
- ABSTRACT.txt sha256
  `c6c2a28e666ec89865f2ddda7f2a7de4e5c459b008a6a460c14a39348d3d9301`
  (722 bytes, single line, 0 ASCII double quotes)
- Transform post-fix sha256
  `ffb71d1b8f00575961c4b3b4244e4897b302b4948d7806d67dc72919320346e6`
- Report: `hidden_files/w45/zh-cn-ru-reproof/REPORT.md`; scratch
  evidence under `hidden_files/w45/zh-cn-ru-reproof/work/`
  (snap1/2/3/close, delivery-hashes-start/mid/close, repro.sh,
  repro-transform.log, repro-run.log, repro-summary.txt, repro-out/,
  repro-build/, reg-ed.json, reg-core.json, freeze-baseline/,
  freeze-diff.json, occlusion.json, rowcheck.py, webregen/).

**Final statement: PASS with ZERO PROBLEMS. The single blocking item
from the first proof (B-1, Gate 10) is closed: transform-alone now
reproduces the delivered edition 8/8 with exit 0 and zero warnings.
This report is the finalization evidence; the coordinator may insert.**
