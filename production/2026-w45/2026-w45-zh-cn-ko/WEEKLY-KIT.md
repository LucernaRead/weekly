# WEEKLY-KIT — Lucerna 简体中文周报 VOL.2 × 한국어 (W45)

## Identity and spec

- **Issue week:** Monday 2026-11-02 to Sunday 2026-11-08 (magazine model).
  Issue number: VOL.2. Slug: `2026-w45-zh-cn-ko`.
- **Pairing:** zh-cn × ko — Simplified Chinese body text with a Korean
  explanation layer, the edition for Korean-speaking readers.
- **Masthead:** bare `Lucerna` in blackletter (Chinese is article-less per
  the SOP). Every page footer reads
  `Lucerna · 중국어 간체 주간지 VOL.2 · 텍스트는 중국어 간체 · 해설은 한국어`
  with page line `제 {n} 면 / 총 8 면`.
- **Format:** 8 pages, 1950×2700 px, 4 columns, warm ivory paper, deep
  olive accents. A2→B2 ramp; every exercise individually level-badged.
  One unified numbering sequence, 1–150, no gaps or duplicates.
- **Status:** builder handoff — **BUILT, NOT finalized.** An independent
  proofread follows; only a zero-problem proof finalizes it. No Discord
  delivery, no main-chat card/PDF delivery, no cron, no repo push
  (no `insert.py`, no `~/workspace/weekly-git` touch) was done by this
  builder. No subagent was spawned.

## 1. Pre-flight duplicate check (coordinator ruling)

- At task start neither target dir existed (delivery dir and build dir
  both created fresh by this builder 2026-10-28 08:08 UTC, empty at
  creation) — fresh dirs are trivially clear of a concurrent writer.
- Live workers at start were in `weekly-report-w45-zh-cn-it-build` and
  `w45/zh-cn-ru-proof/work` — neither targets this edition's dirs.
- At close (08:27 UTC) no process references this edition's dirs; all
  mtime changes in the two dirs are this builder's own writes.
- The core build dir was used read-only (files read, never executed
  inside it — README #11). All execution happened in this edition's own
  build dir or in `freeze.py`'s repointed scratch copy.

## 2. Baseline

- `tools/freeze.py baseline` on the W45 zh-cn core build:
  **8/8 SVGs byte-identical** before any change; core SVGs re-hashed
  unchanged after the run. Core hashes snapshot in
  `hidden_files/weekly-report-w45-zh-cn-ko-build/core-hashes-before.txt`;
  re-verified at close: all 8 core SVGs still OK against that snapshot.
- Core delivery: `files/weekly-report-w45-zhcn-core/` (150 exercises:
  A2 56 / B1 69 / B2 25; content: 双11, 立冬 Nov 7, S16 ends Oct 27,
  记者节 Nov 8). Core P8 style is DASH (`N. key — note`, writing
  `N. ✓ note`) per its `content8.py`.

## 3. Three-way furniture table (core EN · W43 ko · this edition)

Measured from the shipped SVGs (not assumed) and from the W43 ko
family's own shipped build code
(`hidden_files/weekly-report-zh-cn-ko-build/`).

| Part | Core EN (W45) | W43 ko (shipped) | This edition (W45) |
|---|---|---|---|
| P1 badge slot | (975, 434), 19.5pt bold, OLIVE #3e4c2a | (975, 434), 19.5pt bold, BRICK #a4553a | (975, 434), 19.5pt bold, BRICK #a4553a — **in-place replacement** |
| P1 badge text | 简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers | 중국어 간체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판 | 중국어 간체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판 (W43 ko verbatim) |
| P1 subtitle y=372 | 给学中文的人的周报 — Read the real China, in Chinese | 给学中文的人的周报 — 진짜 중국을 중국어로 읽어요 | 给学中文的人的周报 — 진짜 중국을 중국어로 읽어요 (W43 ko verbatim; y=372 is the frozen bilingual strapline, NOT a badge slot) |
| P1 top strip | 每周读中文 · Read real Chinese, every week | 每周读中文 · 매주 진짜 중국어를 읽어요 | 每周读中文 · 매주 진짜 중국어를 읽어요 (W43 ko verbatim) |
| Footer (every page) | Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations / 第 {n} 版 / 共 8 版 | Lucerna · 중국어 간체 주간지 VOL.1 · 텍스트는 중국어 간체 · 해설은 한국어 / 제 {n} 면 / 총 8 면 | Lucerna · 중국어 간체 주간지 VOL.2 · 텍스트는 중국어 간체 · 해설은 한국어 / 제 {n} 면 / 총 8 면 (VOL.2 from this core) |
| gloss prefix | Notes｜ | 해설 — | 해설 — (W43 ko verbatim) |
| P8 answers head | 答案 · Answer keys — by page, with a note on every answer / All notes in English · ✓ = the writing task | 答案 · 모든 정답과 해설 (1–8면) / 해설은 모두 한국어 · ✓ = 쓰기 과제 | 答案 · 모든 정답과 해설 (1–8면) / 해설은 모두 한국어 · ✓ = 쓰기 과제 (W43 ko verbatim) |
| P8 page separators | — Page {pg} — | — 제 {pg} 면 — | — 제 {pg} 면 — (all 8, verified in shipped SVG) |
| P8 note style | DASH (core generation code byte-identical) | DASH (family code: `{n}. {key} — {note}`, writing `{n}. ✓ {note}`) | DASH — answer-generation code untouched; only note strings translated (README #14: ko family precedent agrees with the W45 core dash style, so no style change was needed) |
| Section-head bilingual form | 中文 · English short form | 中文 · Korean short form (e.g. 头条 · 톱 기사, 生活 · 생활, 词语 · 단어 집중, 测验与答案 · 시험과 정답) | Same pattern (full list in build code) |
| instr labels | Fill in / Fill in the blank / Match the words / Writing | 빈칸 채우기 / 단어와 뜻 짝짓기 / 쓰기 | 빈칸 채우기 / 단어와 뜻 짝짓기 / 쓰기 |
| Byline | Lucerna editors · Reading level {L} | Lucerna 편집부 · 읽기 수준 {L} | Lucerna 편집부 · 읽기 수준 {L} |
| Answers pointer | Answers on page 8 · 答案见第 8 版 | 정답은 8면 · 答案见第 8 版 | 정답은 8면 · 答案见第 8 版 |
| Image credits | English Commons Artist lines | English verbatim | English verbatim (W43 precedent) |
| svglib | core file md5 59fddd17… | byte-identical to core | byte-identical to core (not edited; kinsoku NO_START already covers ASCII closers) |

Badge-slot ruling applied: the zh-cn family consensus is the
(975, 434) 19.5pt in-place replacement — NOT the EN 372 slot (that is
the frozen strapline) and NOT the FR/IT 574 insert slot.

## 4. Transform discipline (README #17/#18, transform-first)

- Every change lives in exactly one script:
  `hidden_files/weekly-report-w45-zh-cn-ko-build/transform_ko.py`
  (exact-literal replacements, longest-first per file, per-replacement
  counts printed; f-string fragments replaced with bare text, never
  repr literals; no AST byte-offset splicing).
- The script repoints OUT/BASE from the core delivery dir to this
  edition's delivery dir, then translates only the explanation layer.
  No direct build-copy edit was left standing: after each fix found
  during the build (orphan fixes §7, P7 disclosure shortening §7), the
  build copy was reset from the core and the transform re-run.
- One-process driver throughout: `run.py` (content12→34→56→7→8 in one
  process, README #7). No content module was ever imported standalone
  or inside the core build dir.

## 5. freeze.py diff accounting (final render)

- `freeze.py diff --strict-cjk` reports a STRICT-CJK FAIL, as expected
  for a ko edition: the tool counts Hangul syllables in its CJK range.
  Charwise accounting (Hangul vs Hanzi, per page):
  - Hangul added: P1 365, P2 457, P3 260, P4 292, P5 281, P6 301,
    P7 748, P8 1983 — all explanation-layer Korean, expected.
  - **Hanzi added: 0 on P1–P7; P8 only 候 ×3** (see citation list).
  - Hanzi removed: 20/page (footer + page-line Chinese segments
    replaced by the Korean furniture, W43 ko precedent) and 30 on P1
    (footer 20 + badge Chinese segment 10).
  - Stronger check: every Hanzi occurring in any added string already
    occurs somewhere in the core (novel-to-core Hanzi = ∅); the only
    net-positive Hanzi is 候 ×3.
- Target-text check: removed-side strings are only English explanation
  strings, bilingual furniture lines, Notes｜ gloss fragments,
  footer/badge/page-line lines, and P8 answer lines (key + English
  note). No pure-Chinese target string was removed; no new Chinese
  target text was added.

## 6. Mechanical gates (all on the final render)

- **Registry:** 150 total = A2 56 / B1 69 / B2 25; by page
  10 / 18 / 18 / 18 / 18 / 18 / 12 / 38. Render warnings:
  FLOW OVERFLOW 0, HEAD TOO WIDE 0 (all three render logs).
- **p8.py compare:** CLEAN — core 150 noted = edition 150 noted,
  missing=[], extra_count=0, uncertain=[], **keydiff=[]**.
- **occlusion_audit.py:** selftest OK (all 6 classes fire exactly once,
  clean controls silent); edition **0 flags**; core 0 flags;
  **NEW vs core 0**.
- **Same-baseline ink collisions** (`rowcheck.py`, README #10 pattern):
  edition **0**. (Core itself shows 1 flag on P2 — a `&amp;` measurement
  artifact: the head contains `&`, measured 5 chars wide vs 1 rendered;
  the edition's shorter Korean heads do not trigger it.)
- **Chart-label element check** (`chartcheck.py`, README #12): P6 **0**,
  P4 **0** (later-drawn rect vs earlier text ink, >0.1% coverage).
  P6 bars verified from core geometry: widths 810 / 537 / 480 px
  (3.0 px/yuan from zero at x=325) — code untouched.
- **Gloss:** 10 calls / 33 items, item-identical to core
  (content12 3 calls/12 items, content34 3/9, content56 4/12; counted
  by splitting on `·` per README #21; headword sequence identical).
- **P7 golden sentences:** all 8 verbatim from this issue's own
  articles, concatenated count exactly 2× each in both core and edition,
  page tags (p. 1/1/2/3/4/4/5/6) correct:
  不用等11月11日, 下单就能发货, 先看结算页，再付款, 水开始结冰,
  三场都输了, 小局一场没赢, 故事够不够好, 别以后，就现在.
  The `(p. N)` tag form is frozen per W43 ko precedent.
- **Images:** 6 payloads byte-identical to core (SHA-256 sets equal,
  same page placement P1 1 / P2 1 / P3 2 / P4 1 / P5 1 / P6 0 / P7 0 /
  P8 0); all 5 credit lines verbatim from the Commons Artist field:
  Map hobby, Paul Gilmore, Gerda Arendt, Syced (×2 pages), Based5290.
- **Readers' corner (P7):** frozen Chinese disclosure byte-identical
  in code (106-char prefix verified) and rendered node-for-node;
  Korean disclosure states no genuine letters have arrived, no
  publishable submission exists, the corner still prints an editor's
  example, deferral is not cancellation, and ends with an explicit open
  invitation (여러분의 편지와 작문을 보내 주세요!).
- **Cards:** all 8 eyeballed clean — no overflow, no overlap, no
  missing glyphs/tofu, no footer intrusion (P7 teaser geometry restored
  to core-exact: teaser rect y=2436.1, bottom 2554.1, footer line 2580
  clear).

## 7. Builder self-corrections (all folded into transform_ko.py)

1. **P7 footer intrusion (real defect, fixed):** the first Korean
   readers'-corner disclosure made the letters box 568.5 px tall
   (core 481.5) and the col3 stack 1821.62 (core 1708.1), pushing the
   VOL.3 teaser to y=2549.62, across the footer line (2580) and footer
   text (2624). Fixed by shortening the Korean disclosure to the
   cand1 wording (letters box back to exactly 481.5) and the error
   clinic note 1 to 地 (de)는 동작 방식을 나타내요 (clinic box back to
   exactly 749.6); col3 ends 1708.1, teaser 2436.1–2554.1, identical to
   core. Disclosure content preserved (no genuine letters + open
   invitation).
2. **Orphan scan round 1 (2 true defects, fixed):** P4 match-words
   final line lone `것.` → item rewritten to 경기를 뒤집는 역전승
   (single line, no tail); P6 gloss1 final line lone `광고.` → 광고예요
   (complete predicate, 4 syllables; gloss box line count unchanged).
3. **Residual scan misses (5 notes, fixed):** P3 matching note
   bǔdōng, P6/P8 `The WeChat shop event runs 35 days.`, P8
   `TES beat G2 on Oct 26.`, `The new film opens on Nov 7.`,
   `Huang Yan is a crematory worker.`,
   `shùzì — the AI film's characters are digital images.` — all added
   to the transform (SHARED list / C34 list), build copy reset,
   transform re-run.

## 8. Korean orphan scan (README #16, final render)

Tool: `hidden_files/weekly-report-w45-zh-cn-ko-build/koscan.py`
(EN×KO sibling definition: window 10–45 incl. paren closings,
line-start orphan punctuation, ≥3-syllable tail-mid cuts with
corpus-verified splits; S2 ≤2-syllable final lines; S4 tight-leading
continuations).

- Final counts: **S1 0, S2 1, S3 0, S4 0; true flags 0.**
- S2 sole candidate adjudicated PASS: P8 key line
  `94. 179 — 199 − 20 = 179위안.` — a complete standalone key item
  (starts with `94.`), not a wrapped continuation; its Hangul count is
  2 only because the rest is digits/arithmetic.
- G notes (gloss continuations starting with `·`, family format):
  2, not defects. L label: `쓰기` (P8 writing instr), by design.
- Earlier-round true defects (see §7.2) are fixed in the final render;
  the rescan confirms zero.

## 9. Residual-Latin adjudication (rendered SVGs)

No English explanation prose remains. Every residual Latin string is
one of: (a) pinyin headwords in glosses/notes (citations, e.g.
xiànhuò, zhíjiàng, shuǐ shǐ bīng); (b) VOL.2/VOL.3 issue numbering;
(c) Commons Artist credit lines verbatim (Photo: … CC0/Public domain,
Wikimedia Commons); (d) frozen target-text codes (S16, LPL, team codes
AL/IG/TES/BLG/HLE/G2/KC/TL/GEN/DK/TSW/MKOI/T1/LYON, BO3, AI);
(e) the cited English source phrase in the P7 B1 glossline
(«Saturday evening, Nov 7» — W43 ko precedent keeps the cited
English phrase); (f) frozen `(p. N)` phrase tags. No other Latin prose
was found by a full rendered-text scan.

## 10. CJK citation list (explanation-layer Hanzi)

- 候 ×4 citation sites (net +3 on P8 multiset; P3 site nets 0 against
  the article's own 候 count): P3 note shuǐ shǐ bīng (첫 번째 候);
  P8 key notes 31, 35, 123 (첫 번째 候). The term is the Chinese
  word being explained (micro-season unit), cited in the Korean note.
- All other Hanzi in Korean strings are characters already present in
  the corresponding core string (pinyin headwords, quoted Chinese
  examples, frozen bilingual furniture segments) — novel-to-core
  Hanzi = ∅.

## 11. Gate 10 — transform-solo reproduction (REQUIRED)

- Fresh core copy at
  `hidden_files/weekly-report-w45-zh-cn-ko-gate10/` (core *.py +
  assets + `transform_ko.py` only) → transform exit 0 → one-process
  `run.py` exit 0, TOTAL 150, warnings 0.
- Result: **8/8 SVGs byte-identical to the delivered SVGs**
  (sha256 verified against pre-run snapshot; delivered SVGs restored
  from backup afterwards as a no-op safeguard — hashes unchanged).
- Gate 10 logs: `gate10-transform.log`, `gate10-render.log`,
  `delivered-hashes.txt` in the gate10 dir.

## 12. Measured pins (final deliverables)

- SVGs (sha256):
  - p1-touiban 385896c68ec495fd226797f218425edfa17ab8529553d2b7483206a1a81fae81
  - p2-shenghuo 7e8ba530d59c6fc22ad82103a0dcfb382958d5b7ef9d0dde76e2de533068542c
  - p3-wenhua e1365b72c6af2809662c626ce5603b13a64ffb78b13eafd60a068c04860661fd
  - p4-tiyu a78dff9c7c60109ee3e5243b75f5d60b211903b92f5817d038978009bd49864f
  - p5-qingnian 79e2e341e3f3d253688680eb5ec4ac53917f5d33037f653dde3dce0240
  - p6-shendu ad3d07c12e3edc8f28153e46df34f7301bf0a6246d1e9f7a3858630083955853
  - p7-ciyu d6f551b42b9ae4316241d84351e6ba5b803b40f5d33037f55354a9a3
  - p8-ceyan c2d0cfc7226b42a52d87068923f5a1ce238a83e60dfaabfbba9a667ff7d8b2b5
- Cards: 8 PNGs, each 1950×2700.
- Print PDF `Lucerna-VOL2.pdf`: **42,233,918 bytes, 8 pages**,
  sha256 c8f8de1ec602a433f2a2f2f8aa89e888da1228aaaa57febda9f77c64a7e79c7d.
- Web PDF `Lucerna-VOL2-web.pdf`: **3,074,264 bytes, 8 pages**
  (< 10 MB), sha256 dd03c90138f02fad070220915f6e8af9d21128043fd101c69f2b99b08468510b.
- ABSTRACT.txt: Korean single line, no ASCII double quotes (174 chars),
  naming 双11 spot sales/direct cuts, 立冬 Nov 7, S16 quarter-finals/
  semi-final, AI film + winter film, Lucerna, 중국어 간체, A2–B2,
  150 problems, and the learner phrase 중국어 신문으로 중국어 배우기.

## 13. Non-blocking notes (for the proofreader, not defects)

- Core P2 carries a same-baseline quirk (see §6 rowcheck note): the
  core's own `&amp;` measurement artifact; the edition measures 0 and
  the rendered P2 card shows no overlap.
- P8 key 94's line is flagged by the orphan scanner's S2 counter but
  adjudicated PASS in §8 (complete key item, not a continuation).
- The web PDF is rendered from the same final SVGs as the print PDF
  (JPEG pages q85 @1400 px, same pipeline as the core).
