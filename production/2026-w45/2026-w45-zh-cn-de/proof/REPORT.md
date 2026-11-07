# INDEPENDENT PROOFREAD — W45 ZH-CN × DE (Simplified Chinese target · German reader)

## VERDICT: NOT PASS — 1 blocking item (Gate 10, P8 only)

The edition is defect-free on every content and geometry gate (Gates 1–9, 11
all pass with independent evidence below). It is NOT finalized because
mandatory Gate 10, as specified, reproduces only 7/8 SVGs from a fresh core
copy + the build's transform scripts alone. The P8 delta is confined to the
builder's documented, meaning-preserving fix-round-1 tightenings, which exist
only as direct source edits in the final edition build — not in
`transform_de.py` / `fixround_de.py`. The final edition-build sources DO
reproduce all 8 SVGs byte-for-byte (proven below), so the gap is a build
provenance gap, not an edition content defect. Remedy (for the coordinator /
builder, NOT done by this proofreader): fold the 11 tightenings + the P8
glossline shortening + the #109 rewording into the transform scripts (or
otherwise make the documented procedure reproduce P8), re-run, and re-verify
Gate 10. No other change is needed on the evidence here.

This proofreader did NOT fix the edition, touch `~/workspace/weekly-git`,
run `insert.py`, post to Discord or main chat, create cron jobs, clean
shared scratch, or edit the core build, the W43 shipped edition, `tools/`,
or the delivery dir. All proof work ran under
`~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python`
except card viewing. Scratch:
`hidden_files/w45/zh-cn-de-proof/work/` (`regen/`, `t10/`, `t10b/`).

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live process writing to the DE delivery/build dirs: `ps` showed no
  DE builder/render/transform process. One unrelated process was running
  (the zh-cn-fr proofreader's `occlusion_audit.py` on the FR edition dir);
  it never touched DE dirs and was left alone.
- (b) Two mtime snapshots of both DE dirs (delivery +
  `hidden_files/weekly-report-w45-zhcn-build`), ~3.5 min apart (07:36 →
  07:40 UTC): ZERO changes.
- (c) Builder session completed: delivery complete (8 SVG, 8 cards, both
  PDFs, WEEKLY-KIT.md, ABSTRACT.txt; last write 07:35 UTC, before proof).
- Result: PROCEED. Final re-check: delivery/core-build mtimes unchanged at
  end of proof (only path-prefix formatting differed in the diff); core SVG
  hashes identical before/after (see Gate 1).

## Gate 1 — Freeze baseline + strict-CJK diff: PASS

- `freeze.py baseline --build ../hidden_files/weekly-report-w45-zhcn-build
  --core-svg ../files/weekly-report-w45-zhcn-core/svg`:
  **8/8 SVGs byte-identical** (p1 e057bbfc… … p8 eaf368f8…); "core integrity:
  shipped core SVGs unchanged by the run (8 files re-hashed)". Core hashes
  re-verified unchanged at end of proof.
- `freeze.py diff --strict-cjk` core vs edition: per-page added/removed
  strings P1 +47/−45, P2 +66/−60, P3 +41/−38, P4 +40/−40, P5 +45/−41,
  P6 +42/−38, P7 +90/−83, P8 +196/−198; **added CJK = 0 on every page,
  TOTAL 0**. Independently re-verified at character level: per page, the
  edition's CJK character multiset adds 0 new character types and 0 new
  instances vs the core (all CJK in added strings are citations of words
  already in the core: bilingual heads, gloss headwords, P8 answer tokens,
  frozen captions). No new target text.

## Gate 2 — P8 compare + style from code: PASS

- `p8.py compare --core-dir …zhcn-core --edition-dir …zh-cn-de --target zh-cn`:
  **core 150 noted, edition 150 noted, status CLEAN, missing = [],
  extra_count = 0, keydiff = []**.
- Style verified from BUILD CODE, not memory: core build `content8.py:119`
  `f"{n}. {key} — {note}"` and `:121` `f"{n}. ✓ {note}"` (dash style);
  edition build `content8.py:119/121` byte-identical in code, only note
  strings changed. No keydiff items to verify from SVG nodes (list empty).
- Registry-only writing-key change verified invisible on paper: core key
  `(开放题，范文如下)` → edition `(offene Aufgabe — Mustertext unten)`
  (`content8.py:103` both builds); `grep -c "offene Aufgabe"` on the
  edition P8 SVG's registry-key form = 0 occurrences of the apparatus line
  itself; the printed item 150 reads
  `150. ✓ Offene Aufgabe — der Mustertext steht unten in Abschnitt F
  (172 Zeichen)` (wrapped over 2 lines), matching the core's printed form
  with translated note. Writing model text frozen: extracted model block
  counts **172 characters** (no spaces) in both core and edition, text
  byte-identical.
- P8 geometry (measured, see also Gate 3): keys rule `<line … y1="1264" …
  stroke-width="2"/>` present in both; last test-flow baseline below the
  rule 1225.1 (identical node in core); last key baseline 2532.0 in both;
  footer baseline 2624. Final-sources run log gives flow ends
  P8-ex col 2/3 y=1243 (bottom 1252), P8-keys col 3/3 y=2411 (bottom 2540),
  exactly the builder's claimed values. (Note: 2411/1243 are flow-tracker
  ends, not raw text baselines — see Non-blocking observations.)

## Gate 3 — Occlusion + same-baseline + P6 chart-label: PASS

- `occlusion_audit.py --selftest`: OK — all 6 planted classes fired
  (BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX 1 each), clean controls
  silent.
- `occlusion_audit.py …zh-cn-de --core …zhcn-core`:
  **edition 0 flags; core 0 flags; NEW vs core: 0** (json in
  `work/occlusion.json`).
- Same-baseline scan (builder's `rowcheck.py`, read-only over the edition
  SVG dir): **0 same-baseline flags** (covers the P1 top band).
- P6 chart-label element check (README #12 blind spot): bar rects identical
  to core — x=325, widths 810.0 / 537.0 / 480.0, y=1282/1340/1398, h=34.
  Row-label ink ends x ≤ 201 (bar start 325); value labels start exactly
  16 px right of each bar end (1135→1151, 862→878, 805→821); value-ink
  vertical bands sit below each bar's bottom edge with no overlap
  (A [1319,1341] vs bar [1282,1316]; B/C likewise). No text ink intersects
  any later-drawn bar rect. Chart note reads as claimed (German).
- Final-sources re-run log: **zero `FLOW OVERFLOW` / `HEAD TOO WIDE`**
  warnings (see Gate 10).

## Gate 4 — Gloss counts (split on `·` itself): PASS

Rendered `gloss()` strings extracted from the build sources, split on `·`:
core and edition identical item-by-item, same headwords in same order —
P1 4; P2 4 + 4; P3 3 + 3; P4 3; P5 3 + 3; P6 3 + 3. Gloss prefix `HINWEIS · `
on all gloss boxes (counts per page 1/2/2/1/2/2/0/0, matching the core's
box layout; P4's W43 count of 2 boxes is a different issue's content, not
a furniture mismatch — the prefix string is identical).

## Gate 5 — P7 golden sentences: PASS

All 8 phrases occur exactly 2× in the edition (article page + P7) with the
correct source pages: 「不用等11月11日」 p.1; 「下单就能发货」 p.2;
「先看结算页，再付款」 p.2; 「水开始结冰」 p.3; 「三场都输了」 p.4;
「小局一场没赢」 p.4; 「故事够不够好」 p.5; 「别以后，就现在」 p.5.
P7 tags are German `(S. N)` — counts S.1×1, S.2×2, S.3×1, S.4×2, S.5×2 = 8;
zero English `(p. ` tags. Core adjudications inherited only where frozen
text is byte-identical — it is (phrases match the core exactly, including
the full-width ， in phrase 3).

## Gate 6 — Images: PASS

- Image-element counts per page, edition = core = 1/1/2/1/1/0/0/0 (6 total).
- Embedded payload MD5s byte-identical core vs edition for all 6
  (locker, valley, frost, dumplings, lanparty, popcorn).
- Credit lines: artist names identical to the core; only the house prefix
  changed `Photo:` → `Foto:` (W43 precedent): Map hobby — CC0; Paul
  Gilmore — CC0; Gerda Arendt — CC0; Syced — CC0 (×2); Based5290 — Public
  domain (all Wikimedia Commons). Every credited image is placed; no
  uncredited image is embedded. (Commons API re-query: see Limitations.)

## Gate 7 — Readers' corner: PASS

P7 col 3 (x=1473) verified node by node: the letter (Shanghai, frozen
Chinese) and the Chinese disclosure sentences (y=1437.2–1579.2) are
byte-identical to the core. The German note (y=1579.2–1692.8) (a) labels
the letter an editor's example — `Redaktionsbeispiel — kein echter
Brief.`; (b) discloses no genuine letters exist — `VOL.1 versprach echte
Briefe in VOL.2; keiner kam an.`; and (c) carries the EXPLICIT open
invitation — `… schreiben Sie uns Ihren Brief auf Chinesisch!`
(wrapped over y=1664.4 → 1692.8; verbatim when joined). This is not a
facts-only disclosure, not a teaser line, and not another page's prompt.
Col-3 end and teaser geometry match the core (teaser last baseline 2520.1
both; header `下期预告 · Nächste Woche (VOL.3)`).

## Gate 8 — Furniture three-way + two adjudications: PASS

Measured from SVG nodes (x, y, size, weight, fill):

| Item | W43 shipped zh-cn-de | W45 core | This edition |
|---|---|---|---|
| Badge | (975, 434), 19.5 pt, w700, #a4553a, `CHINESISCHER TEXT (VEREINFACHT) · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER` | (975, 434), 19.5 pt, w700, olive, EN/Chinese badge | **identical to W43** (same coords, size, weight, BRICK fill, text) |
| Subtitle | y=372 `给学中文的人的周报 — Das echte China lesen, auf Chinesisch` | y=372, English second half | y=372 preserved, German second half = W43's |
| Footer | `Lucerna · CHINESISCHE WOCHENZEITUNG VOL.1 · …` | Chinese/English VOL.2 footer | Same template, VOL.2, all 8 pages |
| Page line | `Seite N von 8` | `第 N 版 / 共 8 版` | `Seite N von 8`, all 8 pages |
| Gloss prefix | `HINWEIS · ` | `Notes｜` | `HINWEIS · ` |
| P8 separators | `— Seite 1 —` … `— Seite 8 —` | `— Page N —` | `— Seite 1 —` … `— Seite 8 —` |

- **Adjudication (a) badge slot: RULED FOR the builder.** The zh-cn family
  in-place case applies (README #20: EN/DE/ES cores have a subtitle slot
  → badge replaces it in place at 19.5 pt BRICK). W43 shipped zh-cn-de,
  the core, and this edition all carry the badge at exactly (975, 434),
  19.5 pt, bold; only the fill/text change (olive→BRICK #a4553a, EN→DE).
  Subtitle at y=372 preserved with the German second half. No shift,
  no overprint.
- **Adjudication (b) P8 separators: RULED FOR the builder, shipped wins.**
  The shipped W43 SVG uses sentence-case `— Seite {n} —`; this edition
  matches it. `tools/tables.json` records the abstract form
  `/columns/de/p8_separator_template = — SEITE {N} —` — that is a
  tables.json discrepancy, recorded here and NOT edited (per tasking).
  The edition follows the shipped artifact, as required.
- Bilingual section heads follow the W43 pattern (Chinese head + German
  second half), e.g. `练习 · Übungen`, `答案 · Lösungen — nach Seiten, mit
  einer Anmerkung zu jeder Antwort`, `Alle Anmerkungen auf Deutsch ·
  ✓ = die Schreibaufgabe`. Instruction words Ausfüllen / Zuordnen /
  Schreiben throughout.

## Gate 9 — Web PDF regeneration: PASS (with explained timestamp note)

- Delivered pins verified by direct hash: print
  `Lucerna-VOL2-DE.pdf` **48,987,273 bytes, sha256
  f5b4a70d98bba29889d8988efbf97cc3ee0717b374e8325e13a14d643818c56f**;
  web `Lucerna-VOL2-DE-web.pdf` **3,241,736 bytes, sha256
  56a965187a6fc63e5a4114298ff1d8e5bce30330c84c622617db6bd18fa22c44** —
  both exactly the KIT pins; both 8 pages (pypdf); web < 10 MB.
- Regeneration in own scratch (`work/regen/`, build `render.py` with BASE
  redirected): cards **8/8 byte-identical** to delivered cards; print PDF
  **byte-identical** (same sha256 f5b4a70d…); regenerated web PDF same
  size (3,241,736), 8 pages, but sha256 a3ec31c5… — the ONLY differing
  bytes in the whole file are 8 bytes of trailer metadata:
  `/CreationDate (D:20261028073144Z)` / `/ModDate (D:20261028073144Z)`
  (delivered) vs `…074858Z` (regen). All page image streams are
  byte-identical. A re-run at a different second cannot reproduce a
  timestamp; the KIT pin itself verifies against the delivered file.
- ABSTRACT.txt: single German line, no ASCII double quotes, names the
  real topics (Double-11 spot sales/direct cuts, Winteranfang Sat 7 Nov,
  S16 quarter-finals, AI film 三星堆：未来往事， winter film
  我们仅有一次的人生， Journalists' Day 8 Nov), masthead, target-language
  name, A2–B2 levels, 150 exercises, and a learner search phrase
  (`Chinesisch lesen lernen`). Form per README #22.

## Gate 10 — Transform solo reproduction: FAIL (BLOCKING — P8 only)

- Procedure: fresh copy of the zh-cn core build → `work/t10/`, OUT
  repointed (expanduser form) to scratch, then the build's
  `transform_de.py` + `fixround_de.py`, then `run.py` (one process,
  content12 → 34 → 56 → 7 → 8 in order).
- Result: **P1–P7 byte-identical to delivered (7/8)**; **P8 DIFFERS**
  (delivered 58,134 B vs reproduced 59,754 B). The reproduced P8 run
  itself reports `!! FLOW OVERFLOW [P8-keys] col 3 y=2531 need 31 bottom
  2540`, `flow[P8-keys] ended col 3/3 y=2585` — the builder's first-render
  overflow, before the fix round.
- Root cause (proven by source diff, not guessed): the builder's fix-round-1
  tightenings were applied as direct edits to the edition build's content
  sources and are NOT encoded in `transform_de.py` or `fixround_de.py`.
  Diff of post-transform scratch sources vs final edition-build sources
  (excluding the OUT repoint line) is exactly: 11 exercise-note
  shortenings + the P8 glossline shortening + the #109 rewording —
  content12: #2 `Vorverkauf bei Taobao und Tmall ab 15. Okt.`,
  Spot-Verkauf `ab 20. Okt.`; content34: journalist note (×2 exercises),
  `Finale: 15. Nov., 03:00 Uhr Pekinger Zeit.`; content56: #71
  `Kartenverkauf, etwa 1,192 Mio. Yuan.`, 24.–25. Okt. Zuschauer note,
  #84 `Kassenpreis der Zahlpreis`; content7: #109
  `「最低价」 ist Werbung, keine gemessenen Daten.` (no colon after CJK);
  content8: finale note + glossline
  `Schreiben — keine einzige richtige Antwort. Ein Mustertext mit 172
  Zeichen folgt.` Every one preserves meaning (verified pair by pair);
  none touches frozen Chinese text.
- Bounding proof: a second scratch copy made from the FINAL edition-build
  sources (`work/t10b/`, OUT repointed only) run through `run.py` alone
  reproduces **8/8 SVGs byte-for-byte** with **zero FLOW OVERFLOW /
  HEAD TOO WIDE warnings** and registry TOTAL 150, A2 56 / B1 69 / B2 25,
  pages 10/18/18/18/18/18/12/38, writing model 172. The delivered artifact
  is therefore deterministic from its final sources; what is missing is
  the transform-script encoding of the last fix round.
- This is the edition's ONLY failing gate. The proofreader does not waive
  it: the task states reproduction failure is blocking, and the specified
  procedure (fresh core + transform alone) yields 7/8.

## Gate 11 — All 8 cards visual: PASS

All 8 delivered cards read in full (1950×2700 PNGs): masthead/badge/
subtitle, footers, page lines, gloss boxes, photos + credits, P6 chart
with unclipped labels, P7 clinic/frame/readers'-corner (invitation
visible)/phrases/teaser, P8 test flow, keys rule with clean gap, and key
columns ending clear of the footer. No overflow, overlap, covered,
clipped, struck-through, or footer-intruding text; no missing content.
P8 item 150's note wraps to a second line `(172 Zeichen)` inside the
keys area — clean.

## Other builder claims verified (spot-checks)

- P8 keys end 2411 / test flow end 1243: confirmed as flow-tracker ends
  in the final-sources run log (see Gate 2); raw baselines are lower and
  identical to the core's geometry.
- P7 teaser end 2554.1: consistent with last teaser baseline 2520.1 in
  both core and edition (flow-box end); geometry identical to core.
- 11 tightened P8 notes preserve meaning: verified pair-by-pair in the
  Gate 10 source diff (see above).
- #109 colon rewording: final note has no colon after CJK; strict-CJK
  added = 0 (Gate 1). Full-width colons in edition P8 = 1, same as core
  (frozen Chinese punctuation).
- Fixed English strings: `Spielplan lesen` (P4), `Zeiten & Zahlen` (P5,
  stored as `&amp;`), `Korbrechnen` (P6) all present; old strings
  `Schedule work`, `Times & numbers`, `Basket maths`,
  `TES beat G2 on Oct 26.`, `the AI film's characters are digital images`
  all absent; fixed notes `TES schlug G2 am 26. Okt.` and
  `die Figuren des KI-Films sind digitale Bilder.` present (1 key line
  each in the keys area).
- Fixed-head ink widths measured (PIL, SC Bold 25 pt): 352 / 406 / 424 px
  vs builder's 351.6 / 405.7 / 424.4 — all ≤ 434 px head limit.
- English-remnant rescan (full edition, Latin-token scan + context check):
  zero English prose remnants. Remaining Latin tokens are German words,
  pinyin, team/league codes (AL, IG, TES, BLG, GEN, DK, HLE, G2, KC…),
  brand names (Taobao, Tmall, JD.com, WeChat, Maoyan, Sina), the event
  proper name `Worlds` (also in the core's frozen P4 title), the Commons
  licence label `Public domain` (frozen credit), and standard German
  loanwords (Fans, Team, online, Quiz, Test, Shopping-App).
- `Winteranfang` judgment: **correct and complete, no failure.** 15
  occurrences, every one adjacent to 立冬 (lìdōng) — the word-of-week box
  (`「立冬」 lìdōng — Winteranfang: der erste Solarterm des Winters`),
  the P7 clinic, and P8 notes all pair the Chinese term with the German
  term. `Winteranfang` is the standard German term for 立冬 and matches
  the shipped W43 zh-cn-de precedent. `Start of Winter`: 0 occurrences.
  No English gloss is needed; the term is never left unexplained.
- Registry: TOTAL 150, A2 56 / B1 69 / B2 25, pages 10/18/18/18/18/18/12/38,
  types 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1 —
  confirmed in the final-sources run log and independently from the SVGs
  (per-page distinct numbered items 10/18/18/18/18/18/12/38; chips 1–150
  complete with 130 singles + 5 match ranges 25–28 / 43–46 / 61–64 /
  79–82 / 97–100; per-stem level-badge counts equal core vs edition).
- Zero FLOW OVERFLOW / HEAD TOO WIDE on the final render: confirmed in
  the final-sources run log (Gate 10 bounding proof).

## Non-blocking observations (NOT blocking items — kept separate)

1. Freeze-diff string counts differ from the KIT by 1 on three pages
   (measured P4 +40 / P5 +45 / P6 +42 vs KIT +39 / +44 / +41). Counting
   methodology difference only; added CJK = 0 is unaffected. Not a defect.
2. The edition KIT renders P7 phrase 3 with an ASCII comma
   (`先看结算页,再付款`); the actual delivered SVG uses the full-width ，
   byte-identical to the core. KIT typo only.
3. Builder flow-end figures (P8 2411/1243, P7 teaser 2554.1) are flow-box
   ends, not raw text baselines (last key baseline 2532.0, last test-flow
   baseline 1225.1, teaser baseline 2520.1 — all identical to the core's
   geometry). The substantive claim (edition geometry ≤ core, rule and
   footer clear) holds; occlusion audit confirms 0 flags.
4. Regenerated web PDF SHA differs from the KIT pin only in
   CreationDate/ModDate timestamps (8 bytes; Gate 9). Delivered file
   matches the KIT pin exactly.
5. `tables.json` P8 separator form (`— SEITE {N} —`) disagrees with the
   shipped W43 SVG (`— Seite {N} —`); the edition correctly follows the
   shipped artifact. Recommend a future tables.json correction from the
   shipped artifact (NOT done here, per tasking).
6. W43 zh-cn-de P4 carries 2 gloss boxes vs this issue's 1 — different
   issue content, not a furniture mismatch; the gloss prefix string is
   identical and this issue's box counts match its own core exactly.

## Limitations (stated plainly)

- Simplified purity: OpenCC is NOT installed on this VM, so no OpenCC t2s
  diff was possible (same as the builder). Purity evidence is strict-CJK
  added = 0 + the edition's CJK character set being a subset of the
  core's + a Traditional-sample scan (0 hits) + full-text read-through of
  extracted text. A Traditional character that also appears in the core
  would not be caught by the subset test; none was seen in read-through.
- Image credits: verified frozen-identical to the core and consistent with
  the core build's `assets/CREDITS.md` (which documents Commons API
  `Artist`/`LicenseShortName` verification on 2026-10-27). The Commons API
  was not re-queried live during this proofread.
- German quality: judged by full read-through of extracted German text
  and card review, not by a native-speaker check.
- Visual check: card eyeball at rendered resolution, not a pixel-diff
  against the core (cards are byte-identical to the independent regen,
  which is the determinism check for the render path).

## PDF pins (delivered files, verified)

- Print: `Lucerna-VOL2-DE.pdf` — 48,987,273 bytes, 8 pages, sha256
  `f5b4a70d98bba29889d8988efbf97cc3ee0717b374e8325e13a14d643818c56f`
- Web: `Lucerna-VOL2-DE-web.pdf` — 3,241,736 bytes, 8 pages, sha256
  `56a965187a6fc63e5a4114298ff1d8e5bce30330c84c622617db6bd18fa22c44`
- Edition SVGs (sha256): p1 ed19e7c6…, p2 9fd48f09…, p3 12455f50…,
  p4 cea4a5dc…, p5 79d01866…, p6 45908520…, p7 f204da52…, p8 eac3fd97…
  (full hashes in the proof session log; delivery dir untouched).

## Bottom line for the coordinator

Do NOT insert yet on this proofread alone: Gate 10 must be closed first.
The closure is mechanical — encode the 11 tightenings + glossline
shortening + #109 rewording into the transform scripts (or present the
final-sources 8/8 reproduction as the adjudicated gate evidence) and
re-run Gate 10 to 8/8. Everything else about this edition — content,
geometry, furniture, images, readers'-corner invitation, PDFs, cards —
passed independent verification with zero problems.
