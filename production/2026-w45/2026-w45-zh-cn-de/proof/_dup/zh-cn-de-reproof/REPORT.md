# INDEPENDENT RE-PROOFREAD — W45 ZH-CN × DE (Simplified Chinese target · German reader)

## VERDICT: PASS — ZERO PROBLEMS

Full independent round from scratch. Every gate passes, including Gate 10
(the single item that failed the first proof): fresh core copy +
`transform_de.py` + `fixround_de.py` alone now reproduce **8/8 SVGs
byte-identical** to the delivered files, with all exit codes 0 and zero
warnings. This report is the finalization evidence for the coordinator.
This proofreader did NOT fix anything, touch `~/workspace/weekly-git`,
run `insert.py`, post to Discord or main chat, create cron jobs, clean
shared scratch, or edit the core build, the W43 shipped edition, `tools/`,
or the delivery dir. All proof work ran under
`~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python`
except card viewing. Scratch:
`hidden_files/w45/zh-cn-de-reproof/work/` (`t10/` Gate 10, `t10b/`
final-sources bounding run, `regen/` web regen, `freeze-baseline/`,
`freeze-diff.json`, `occlusion.json`, hash/snapshot files, logs).

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER) — PROCEED

- (a) No live worker writing to the DE delivery/build dirs. Live
  processes seen at 08:07 UTC were unrelated and left alone: a RU-proof
  `webregen/render.py` (cwd `hidden_files/w45/zh-cn-ru-proof/work`),
  an IT-build `render.py` (cwd `weekly-report-w45-zh-cn-it-build`), and
  a PT occlusion audit. No process with a DE cwd or DE target.
- (b) Two mtime snapshots of both DE dirs (delivery +
  `hidden_files/weekly-report-w45-zh-cn-de-build`), 08:08 → 08:12 UTC:
  **ZERO changes**.
- (c) Fix session completed: `FIX-LOG.md` and `WEEKLY-KIT.md` last
  written 08:06 UTC, before this proof; delivery SVGs last written
  08:04 UTC (the fix re-render, hashes identical to the fix log).
- Close re-check: delivery hashes identical start → close, mtimes
  unchanged since snap2, core SVGs unchanged (see Gate 1).

## Gate 1 — Pre-flight + delivery hash verification (start AND close): PASS

All 19 files (8 SVGs, 8 cards, both PDFs, ABSTRACT.txt) hashed at start
(08:08), mid-round (08:12), and close (08:26): **identical all three
times**, matching the fix log's pre/post-fix hashes exactly. Sizes:
print PDF 48,987,273 B, web PDF 3,241,736 B, P8 SVG 58,134 B.
WEEKLY-KIT.md is also covered by the whole-dir mtime snapshots
(unchanged).

## Gate 2 — Freeze baseline + strict-CJK diff: PASS

- `freeze.py baseline` (core build `weekly-report-w45-zhcn-build`):
  **8/8 SVGs byte-identical** (p1 e057bbfc… … p8 eaf368f8…);
  "core integrity: shipped core SVGs unchanged by the run".
  Core hashes re-verified unchanged at close.
- `freeze.py diff --strict-cjk` core vs edition: P1 +47/−45, P2 +66/−60,
  P3 +41/−38, P4 +40/−40, P5 +45/−41, P6 +42/−38, P7 +90/−83,
  P8 +196/−198; **added CJK = 0 on every page, TOTAL 0**.

## Gate 3 — p8.py compare + dash style from code: PASS

- `p8.py compare --core-dir …zhcn-core --edition-dir …zh-cn-de
  --target zh-cn`: **core 150 noted, edition 150 noted, status CLEAN,
  missing = [], extra_count = 0, keydiff = []** (exit 0).
- Style verified from build code: core build `content8.py:119`
  `f"{n}. {key} — {note}"` and `:121` `f"{n}. ✓ {note}"`;
  edition build lines byte-identical in code, only note strings changed.

## Gate 4 — Occlusion + same-baseline + P6 chart-label: PASS

- `occlusion_audit.py --selftest`: OK — all 6 planted classes fired
  (BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX 1 each), clean controls
  silent.
- `occlusion_audit.py …zh-cn-de --core …zhcn-core`:
  **edition 0 flags; core 0 flags; NEW vs core: 0**.
- Same-baseline scan (builder's `rowcheck.py`, read-only over the
  edition SVG dir): **0 same-baseline flags**.
- P6 chart-label element check: bar rects identical to core — x=325,
  widths 810.0 / 537.0 / 480.0, y=1282/1340/1398, h=34. Row labels
  frozen Chinese at x=65; value labels at 1151/878/821 = bar ends
  (1135/862/805) + 16 px exactly, same as core. Chart note in German.
  No text ink intersects any later-drawn bar rect.

## Gate 5 — Gloss counts (split on `·` itself): PASS

AST-parsed (not imported) `gloss()` calls from both build sources:
**10 calls, 33 items, both builds**. Headwords equal item-by-item in
order (xiànhuò 现货 … tuìhuànhuò 退换货; full list in the proof
session log). Delivered SVG gloss-prefix counts per page
1/2/2/1/2/2/0/0; `HINWEIS · ` on all boxes, `Notes` 0 occurrences.

## Gate 6 — P7 golden sentences: PASS

All 8 phrases occur exactly 2× (article page + P7) with correct source
pages, verified on document-order-joined text (article occurrences are
line-wrapped splits, e.g. P2 "下单就" + "能发货。", which a naive
per-node count misses — this proof initially saw 1× for four phrases
and closed the gap by rejoining wrapped lines): 「不用等11月11日」
p.1; 「下单就能发货」 p.2; 「先看结算页，再付款」 p.2; 「水开始结冰」
p.3; 「三场都输了」 p.4; 「小局一场没赢」 p.4; 「故事够不够好」
p.5; 「别以后，就现在」 p.5. P7 tags are German `(S. N)` with
correct pairing per phrase: S.1×1, S.2×2, S.3×1, S.4×2, S.5×2;
zero English `(p. ` tags. Phrase 3 uses the full-width ，,
byte-identical to the core.

## Gate 7 — Images: PASS

- Image counts per page, edition = core = 1/1/2/1/1/0/0/0 (6 total).
- Embedded payload MD5s byte-identical core vs edition for all 6
  (locker 420c6150…, valley 550e463b…, frost d0b015bc…,
  dumplings e8d75277…, lanparty 6b8e9037…, popcorn a903e35f…).
- Credit lines: artist names identical to the core; only the house
  prefix changed `Photo:` → `Foto:` (W43 precedent): Map hobby — CC0;
  Paul Gilmore — CC0; Gerda Arendt — CC0; Syced — CC0 (×2);
  Based5290 — Public domain (all Wikimedia Commons). Every credited
  image is placed; no uncredited image is embedded. (Commons API
  re-query: see Limitations.)

## Gate 8 — Readers' corner: PASS

P7 col 3 (x=1473) verified node by node: the letter (Shanghai) lines
(y=1315.6–1376.7) and the Chinese disclosure lines (y=1437.2–1550.8)
are byte-identical to the core, same baselines. The German note
(y=1579.2–1692.8) (a) labels the letter an editor's example —
`Redaktionsbeispiel — kein echter Brief.`; (b) discloses no genuine
letters exist — `VOL.1 versprach echte Briefe in VOL.2; keiner kam
an.`; and (c) carries the verbatim invitation — `schreiben Sie uns
Ihren Brief auf Chinesisch!` (wrapped over y=1664.4 → 1692.8, verbatim
when joined). Teaser header y=2480.1 and body last baseline 2520.1
identical to core; header `下期预告 · Nächste Woche (VOL.3)`.

## Gate 9 — Furniture three-way (core EN · W43 de · this edition): PASS — both adjudications CONFIRMED

Measured from SVG nodes (x, y, size, weight, fill):

| Item | W43 shipped zh-cn-de | W45 core | This edition |
|---|---|---|---|
| Badge | (975, 434), 19.5 pt, w700, #a4553a, `CHINESISCHER TEXT (VEREINFACHT) · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER` | (975, 434), 19.5 pt, w700, olive, EN/Chinese badge | **identical to W43** (same coords, size, weight, BRICK fill, text) |
| Subtitle | y=372 `给学中文的人的周报 — Das echte China lesen, auf Chinesisch` | y=372, English second half | y=372 preserved, German second half = W43's |
| Footer | `Lucerna · CHINESISCHE WOCHENZEITUNG VOL.2 · …` | Chinese/English VOL.2 footer | Same template, VOL.2, all 8 pages |
| Page line | `Seite N von 8` | `第 N 版 / 共 8 版` | `Seite N von 8`, all 8 pages |
| Gloss prefix | `HINWEIS · ` | `Notes｜` | `HINWEIS · ` |
| P8 separators | `— Seite 1 —` … `— Seite 8 —` | `— Page N —` | `— Seite 1 —` … `— Seite 8 —` |

- **Adjudication (a) badge slot: CONFIRMED for the builder.** The
  zh-cn family in-place case applies (README #20: EN/DE/ES cores have
  a subtitle slot → badge replaces it in place at 19.5 pt BRICK).
  No shift, no overprint.
- **Adjudication (b) P8 separators: CONFIRMED, shipped wins.**
  `tools/tables.json` still records `/columns/de/
  p8_separator_template = — SEITE {N} —` (file mtime 2026-10-22,
  untouched — NOT edited, per tasking). The edition correctly follows
  the shipped W43 artifact (`— Seite {n} —`).

## Gate 10 — DOCUMENTATION CHAIN (the fixed item): PASS — 8/8

Procedure: fresh copy of the zh-cn core build → `work/t10/`, OUT
repointed (expanduser form, all 5 content files) to scratch, then the
build's `transform_de.py` + `fixround_de.py` (copied verbatim from the
edition build), then one-process `run.py`
(content12 → 34 → 56 → 7 → 8).

- **transform exit 0** ("transform applied to 7 files").
- **fixround exit 0.** R counts as expected; **R2 counts verified
  independently: 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1 = 13 occurrences**
  across 11 pairs, in KIT order: Vorverkauf (1×), Spot-Verkauf (1×),
  Journalist plain (1×), jìzhě gloss (2×, content34 + content8),
  Finale (2×, content34 + content8), piàofáng (1×), 24.–25. Okt. (1×),
  Kassenpreis (1×), #109 (1×), Spot-Ware (1×), P8 glossline (1×).
  Each old→new pair matches the KIT's table; exact old literals are
  0× in the post-fixround sources and new forms occur at the counted
  rates (one substring check initially looked off — "Einnahmen aus
  dem Kartenverkauf" also occurs in three unrelated sentences, the
  gloss definition, a matching exercise, and a different exercise's
  note — all present identically in the final edition build; the
  exact R2 literal is 0× old / 1× new, as claimed).
- **run exit 0, zero `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings**
  (grep counts 0/0), registry **TOTAL 150, A2 56 / B1 69 / B2 25,
  pages 10/18/18/18/18/18/12/38, types 完成句子 68 / 单选 50 /
  词汇配对 20 / 完形单选 11 / 写作 1**.
- **SVG comparison: 8/8 byte-identical to delivered**, sizes
  782101 / 1174950 / 2125644 / 804653 / 1059795 / 26375 / 27314 /
  **58134 B (P8 — the fixed version, not the 59,754 B overflow)**.
- Completeness proof beyond the byte match: post-transform+fixround
  sources vs final edition-build sources diff = **NO DIFF on all 6
  files** (bslib4 + content12/34/56/7/8, OUT lines excluded) — the
  transform scripts now encode everything, nothing remains as a
  direct-only edit.
- Bounding run (`work/t10b/`, final edition-build sources, OUT
  repointed only): run exit 0, zero warnings, same registry,
  **8/8 byte-identical** to delivered.

## Gate 11 — Web regen: PASS

Regeneration in own scratch (`work/regen/`, render.py BASE redirected):
cards **8/8 byte-identical** to delivered cards; print PDF
**byte-identical** (same sha256 f5b4a70d…); regenerated web PDF same
size (3,241,736 B), 8 pages, and **content-identical after stripping
CreationDate/ModDate timestamp bytes only** — delivered
`D:20261028073144Z` vs regen `D:20261028081909Z`; all other bytes
identical. (A re-run at a different second cannot reproduce a
timestamp; the KIT pin itself verifies against the delivered file.)
`render.py` was deliberately NOT re-run against the delivery dir.

## Gate 12 — All 8 cards visual: PASS

All 8 delivered cards read in full (1950×2700 PNGs): masthead/badge/
subtitle, footers, page lines, gloss boxes, photos + credits, P6 chart
with unclipped labels, P7 clinic/frame/readers'-corner (invitation
visible)/phrases/teaser, P8 test flow, keys rule with clean gap, and
key columns ending clear of the footer. No overflow, overlap, covered,
clipped, struck-through, or footer-intruding text; no missing content.
P8 item 150's note wraps to a second line `(172 Zeichen)` inside the
keys area — clean. Fixed heads visible: `Spielplan lesen` (P4),
`Zeiten & Zahlen` (P5, stored as `&amp;`), `Korbrechnen` (P6).

## Gate 13 — First-proof settled items re-checked, not assumed: PASS

- **Winteranfang ×15 correct and complete; `Start of Winter` ×0.**
  Per-file occurrences: P1 2, P3 1, P7 1, P8 11. Pairing, stated
  precisely (refining the first proof's "adjacent" wording): 9 of the
  15 share a node/wrapped sentence with 立冬 (P1 calendar line, P1
  word box, P3 band, P7 clinic sentence, P8 keys 4/34/74/103/131
  whose key is 立冬 itself). The other 6 are P8 key notes whose
  exercises are 立冬-topic exercises, verified at source level
  (content12:63 key 一 in a 立冬 sentence, content12:151, content34:69,
  content34:93, content56:75, content8:16) — the note explains a
  立冬 exercise, so the term is never left unexplained. A narrow
  ±40-character window check initially flagged 4 of these; the
  per-exercise check closes them. `Winteranfang` is the standard
  German term for 立冬 and matches the shipped W43 precedent.
- **English-remnant rescan clean.** Old strings absent (0×):
  `Schedule work`, `Times & numbers`, `Basket maths`,
  `TES beat G2 on Oct 26.`, `the AI film's characters are digital
  images`. Fixed strings present: `Spielplan lesen` (1×),
  `Zeiten & Zahlen` (1× as `&amp;`), `Korbrechnen` (1×),
  `TES schlug G2 am 26. Okt.` (1×),
  `die Figuren des KI-Films sind digitale Bilder.` (2× — keys 70
  and 135, two exercises sharing the note; see Non-blocking obs. 2).
  Latin-token scan: the only suspect English function word, `was`
  (6×), is German in every context (relative/interrogative pronoun).
  Remaining Latin tokens are German words, pinyin, team/league codes,
  brand names, the event proper name `Worlds` (also in the core's
  frozen P4 title), the Commons licence label `Public domain`
  (frozen credit), and standard German loanwords.
- **Registry-only writing-key change invisible on paper:** the
  apparatus key `(offene Aufgabe — Mustertext unten)` occurs 0× in
  the P8 SVG; the printed item 150 reads `150. ✓ Offene Aufgabe —
  der Mustertext steht unten in Abschnitt F (172 Zeichen)` (1×);
  core key `(开放题，范文如下)` 0×.
- **Writing model 172 chars frozen:** MODELO extracted from both
  builds counts **172 characters** (no spaces), text byte-identical.
- **Zero render warnings on final sources:** t10b run log, 0 FLOW
  OVERFLOW / 0 HEAD TOO WIDE; Gate 10 run log likewise 0/0.
- **Full-width colon count in P8: 1, same as core** (frozen Chinese
  punctuation); #109 note has no colon after CJK.

## Gate 14 — ABSTRACT.txt: PASS

Single German line, no ASCII double quotes, naming the real topics
(Double-11 spot sales/direct cuts, Winteranfang Sat 7 Nov, S16
quarter-finals, AI film 三星堆：未来往事， winter film
我们仅有一次的人生， Journalists' Day 8 Nov), the paper name
(Lucerna Chinesisch-Wochenzeitung VOL.2), the reader group
(deutschsprachige Leser), the target language (Chinesisch
(vereinfacht)), A2–B2 levels, 150 exercises, and a learner search
phrase (`Chinesisch (vereinfacht) lesen lernen`). Every required
element verified present by string check (15/15).

## Non-blocking observations (NOT blocking items — kept separate)

1. Freeze-diff string counts match the first proof's measured values
   (P4 +40 / P5 +45 / P6 +42), differing from the KIT by 1 on those
   pages. Counting methodology difference only; added CJK = 0 is
   unaffected. Not a defect.
2. The fixed AI-film note renders on 2 P8 key lines (keys 70 and 135),
   not 1: two 完成句子 exercises (content56 and content8) share the
   identical note text. Both lines are correct German; the first
   proof's "1 key line each" phrasing was loose. Not a defect.
3. `tables.json` P8 separator form (`— SEITE {N} —`) still disagrees
   with the shipped W43 SVG (`— Seite {N} —`); the edition correctly
   follows the shipped artifact. A future tables.json correction from
   the shipped artifact is recommended (NOT done here, per tasking).
4. The KIT/fixround docstring label "colon rewording" for #109 does
   not match the R2 pair's text: the old string
   `「最低价」 ist eine Werbebehauptung, keine gemessenen Daten.`
   itself contains no colon. The pair is verified correct and
   complete (byte reproduction + strict-CJK 0 + P8 full-width colon
   count 1 = core); only the mechanism label is loose. Not a defect.
5. P7 col-3 line y=1579.2 carries both the final Chinese character
   (消。) and the start of the reader-language note, so that one line
   differs between core (English tail) and edition (German tail) by
   design; the frozen Chinese disclosure sentences themselves
   (y=1437.2–1550.8) are byte-identical. Not a defect.
6. The edition KIT renders P7 phrase 3 with an ASCII comma
   (`先看结算页,再付款`); the actual delivered SVG uses the full-width
   ，, byte-identical to the core. KIT typo only (carried from the
   first proof).

## Limitations (stated plainly)

- Simplified purity: OpenCC is NOT installed on this VM, so no OpenCC
  t2s diff was possible (same as the builder and the first proof).
  Purity evidence is strict-CJK added = 0 + the edition's CJK
  character set accounting in the freeze diff + full-text read-through
  of extracted text and cards.
- Image credits: verified frozen-identical to the core and consistent
  with the core build's `assets/CREDITS.md` (which documents Commons
  API `Artist`/`LicenseShortName` verification on 2026-10-27). The
  Commons API was not re-queried live during this reproof.
- German quality: judged by full read-through of extracted German text
  and card review, not by a native-speaker check.
- Visual check: card eyeball at rendered resolution, not a pixel-diff
  against the core (cards are byte-identical to the independent regen,
  which is the determinism check for the render path).

## PDF pins (delivered files, re-verified at close)

- Print: `Lucerna-VOL2-DE.pdf` — 48,987,273 bytes, 8 pages, sha256
  `f5b4a70d98bba29889d8988efbf97cc3ee0717b374e8325e13a14d643818c56f`
- Web: `Lucerna-VOL2-DE-web.pdf` — 3,241,736 bytes, 8 pages, sha256
  `56a965187a6fc63e5a4114298ff1d8e5bce30330c84c622617db6bd18fa22c44`
- Edition SVGs (sha256): p1 ed19e7c6…, p2 9fd48f09…, p3 12455f50…,
  p4 cea4a5dc…, p5 79d01866…, p6 45908520…, p7 f204da52…,
  p8 eac3fd97… (full hashes in `work/hash_close.txt`; delivery dir
  untouched).

## Bottom line for the coordinator

**PASS with ZERO PROBLEMS.** The first proof's single blocking item is
closed: transform + fixround alone now reproduce 8/8 SVGs
byte-identical, with exit codes 0/0/0, zero warnings, registry 150,
and P8 at the fixed 58,134 B. Every other gate re-verified
independently with zero problems. This report may serve as the
finalization evidence for insert.
