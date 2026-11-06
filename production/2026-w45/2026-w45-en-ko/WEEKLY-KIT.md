# WEEKLY KIT — The Lucerna VOL.2 · W45 (Nov 2–8, 2026) · EN × KO

- Pairing: target language **English**, reader native language **Korean**.
  Masthead badge (P1): `영어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`.
  English body text is frozen from the W45 EN core; only the explanation layer
  is Korean. No Chinese characters, no full-width CJK punctuation anywhere.
- Delivery: `files/weekly-report-w45-en-ko/` — `svg/` × 8, `cards/` × 8,
  print PDF `The-Lucerna-VOL2-KO.pdf`, web PDF `The-Lucerna-VOL2-KO-web.pdf`,
  this KIT, `ABSTRACT.txt`.
- Build tree: `hidden_files/weekly-report-w45-en-ko-build/` — `transform.py`
  (single source of truth), `run.py` (single-process driver), `render.py`,
  `svglib.py` (byte-identical to core, md5 `0703a8814abe388f131c89f3d7ffb946`),
  `content*.py`, `assets/` (core's 5 images + CREDITS.md, copied unchanged),
  `ko_scan.py` / `rightedge.py` / `rowcheck.py` / `chartcheck.py`,
  per-round sha256 baselines and raw gate outputs.
- Status: **fix-complete (fix round 1), pending a fresh full independent
  proofread per SOP §8.4. Not finalized.** The fix round below changed
  rendered output, so the round-3 proofread does not carry over.

## 1. Issue spec (measured from the W45 EN core, not from any sibling edition)

- 150 exercises; levels A2 60 / B1 69 / B2 21.
- Page distribution: P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39.
  Note P2 17 and P8 39 — not the generic 10/18/18/18/18/18/12/38.
- P8 structure: A cloze 8 + B multiple choice 9 + C reading 4 + D sentences 4
  + E translation 4 (EN↔KO in this edition) + F word matching 4 + G dialogue 5
  + H writing 1. Model essay « My Tuesday, November 3 »: 80–100 words, model
  text counted at 85 words, identical to core.
- P7 structure (measured from core): top 4 columns A2 / B1 / B2 / toolbox
  (y200–1150); phrases band (py 1210); bottom-left error clinic (by7 1870),
  bottom-right readers' corner box (2–3 cols, height 300) + VOL.3 dark
  preview box below it. Golden-sentence English originals and `(page N)`
  labels are verbatim from core; only gloss/explanation is Korean.
- P6 teaching chart « WHY DO VOTERS VOTE EARLY? »: 38 / 29 / 21 / 12 = 100.
  The page states it is teaching data, not a real poll.
- Core freeze verified: `tools/freeze.py baseline` reproduces the W45 EN core
  **8/8 SVGs byte-identical** (repointed copy build; shipped core SVGs
  re-hashed unchanged after the run). Core hashes (sha256, full in
  `hidden_files/weekly-report-w45-en-ko-build/freeze-baseline.txt`):
  p1 `c7e7d019…`, p2 `07f5df7e…`, p3 `d9f7cc37…`, p4 `3b8be517…`,
  p5 `73486e2f…`, p6 `3e2187b3…`, p7 `5a268409…`, p8 `4de34a13…`.

## 2. Content by page

- **P1 — front.** Headline: America votes Tuesday, November 3; clocks fell
  back Sunday, November 1. Big story: midterm election (all 435 House seats
  + ~a third of the Senate + governorships). Searches of the week (snapshots,
  late October; relative interest, not exact figures): election day,
  nfl week 9, cat in the hat, daylight saving, f1 sao paulo. Directory p.2–p.8,
  word of the week « midterm », IN BRIEF (election / clocks / movies),
  photo: voting booth, Old State House, Hartford (Kenneth C. Zirkel, CC0).
  Lightning quiz 7–10.
- **P2 — LIFE.** One more hour of sleep: clocks back 2 a.m. → 1 a.m.,
  25-hour night, Arizona and Hawaii do not change; Halloween Saturday,
  October 31 (past event). Telling-the-time clocks (1:00 / 1:30 / 7:45),
  vocab list, DO THE MATHS (25 hours), AND YOU box (write two English
  sentences about Sunday). Exercises 11–27.
- **P3 — CULTURE.** Friday, November 6 films: « The Cat in the Hat »
  (Bill Hader voice) and « Godzilla Minus Zero » (Takashi Yamazaki).
  At-home week (Wed Nov 4 – Sun Nov 8 screen guide), THE CAT'S HAT box,
  FIVE SENTENCES task. Exercises 28–45. Photo: « Cat and Flowers »,
  Édouard Manet, CC0.
- **P4 — SPORT.** Sunday, November 8: NFL in Madrid (Bengals–Falcons,
  Santiago Bernabéu), F1 São Paulo GP, NASCAR Homestead-Miami, WTA Finals
  Indian Wells, boxing Baumgardner–Turhan, MLS Saturday Nov 7.
  WHY MADRID? box, SUNDAY NOVEMBER 8 schedule box, ONE SCREEN TWO SCREENS.
  Exercises 46–63. Photo: American football 1910, Frank R. Snyder, public domain.
- **P5 — YOUTH.** Election night at home: maps, phones, pizza; TOO CLOSE TO
  CALL box, FIVE SENTENCES task, ELECTION-NIGHT PHRASES, SATURDAY SPORT.
  Exercises 64–81.
- **P6 — DEEP READ (B2).** How America votes: fifty state elections, House
  2 years / Senate 6 years / President 4 years / Governor usually 4 years;
  A PRACTICE BALLOT box, numbers note (no poll figures or predictions in
  this issue), READ THE CHART (teaching data, see §1), chart reading,
  comprehension, sentences. Exercises 82–99. Photo: U.S. Capitol,
  public domain. The ballot-checkbox glyph renders identically to core
  (verified by cropped pixel comparison of the ballot box).
- **P7 — LANGUAGE IN HAND.** A2 falling back / going to + verb; B1
  comparatives / past simple; B2 headline present / whether = if?;
  toolbox (3 pocket sentences); PHRASES OF THE WEEK: 8 sentences, each
  with a grammar point + one practice item (100–107); ERROR CLINIC 108–111;
  READERS' CORNER (see §6); NEXT WEEK / VOL.3 preview: Wednesday,
  November 11 Veterans Day, Sunday, November 15 NFL in Munich, midterm
  results reported. Exercises 100–111.
- **P8 — FINAL TEST.** See §1 for structure. Answers stream with
  `— 제 {n} 면 —` separators for all 8 pages; answers at the bottom of
  the page; H writing prompt (80–100 words) + MODEL box. Exercises 112–150.

## 3. Trend / fact sources and image licences

- Trend hook (printed on P1, “Snapshots, late October”): U.S. search
  interest around the election date, NFL Week 9, the two November 6 films,
  daylight saving, and the São Paulo GP — the same set the core's P1
  searches box prints. The chart on P6 is labelled teaching data, not a
  real poll, and §1 above repeats that label.
- All images are public-domain / CC0 via Wikimedia Commons; the credit
  line printed under each photo is taken from the Commons Artist field:
  P1 voting booth (Kenneth C. Zirkel, CC0); P2 Halloween postcard 1912
  (public domain); P3 Manet illustration (CC0); P4 1910 football
  (Frank R. Snyder, public domain); P6 Capitol (public domain).
- No international politics. U.S. domestic election coverage is the
  target-country domestic-politics case allowed by the editorial line.

## 4. Reproduction

- `run.py` interpreter: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0.
- `render.py` interpreter: `tools/venv/bin/python` (system python3 has no
  cairosvg) — Python 3.12.3, PIL 13.0.0, cairosvg 2.9.1, pypdf 6.21.2.
  Render recipe (core formula): SVG → 1950×2700 PNG → print PDF; web PDF
  from 1400 px-wide JPEG q85.
- Rebuild: `transform.py` (audits: quoted literal replacement longest-first;
  badge / footer / page-line / P8-separator / P8-note-condition / note-bracket
  line edits; PRINT_NOTES block inserted before `from itertools import groupby`;
  asserts: no core OUT residue, no stale quoted values, no forbidden bridge-term, no Han
  in content/bslib, no full-width punctuation) → single-process `run.py`
  → `render.py`. Every fix lands in `transform.py` first; content files
  are never hand-edited alone.
- Geometry constants (measured from `bslib4.py`): page 1950×2700; CW=434;
  COLX=[65,527,989,1451]; RIGHT=1885; MX=65.

## 5. Proofread record (builder self-check; independent proofread still open)

Final (round 3) gate values — all raw outputs in the build tree:

| Gate | Result |
|---|---|
| Core baseline `freeze.py baseline` | 8/8 byte-identical; core SVGs unchanged |
| `freeze.py diff` (round 3) | added CJK 2452 chars, 100% Hangul, Han 0; full-width punct 0; `。` 0; forbidden bridge-term 0 |
| `occlusion_audit.py` edition / core / NEW | 0 / 0 / 0 (selftest planted classes all fired; clean controls silent) |
| `p8.py compare` (explicit `--core-p8` / `--edition-p8`, `--total 150`) | CLEAN; core 78 = edition 78 noted; missing=[]; extra=0; uncertain=[]; keydiff=[137,138,139,140,150] |
| P8 notes | 129 changed / 21 unchanged (unchanged = pure-English neutral notes); changed-note ASCII-word loss 0 |
| P8 note set | printed-note sets equal (no EXTRA_ONLY) |
| Registry re-dump (150) | page dist 10/17/18/18/18/18/12/39; levels A2 60 / B1 69 / B2 21; page/level per-item mismatches 0 |
| Gloss (rendered `gloss()` strings, split on `·`) | core 18 = edition 18; per box P2 3 / P3 4 / P4 4 / P5 3 / P6 4; double prefix `해설 — 해설` 0 (core's own 5 `译注｜讲解｜` double prefixes cleaned to single prefix, per W43 EN×KO precedent) |
| P7 golden sentences | 8/8 English originals verbatim; `(page N)` counts core=edition: (page 1) 1, (page 2) 4, (page 3) 1, (page 4) 2, (page 5) 1, (page 6) 2 |
| Korean scan `ko_scan.py` window 10–45 | S1 0 / S2 4 / S3 0 / S4 0 (the 4 S2 are adjudicated non-defects, §7) |
| Right-edge ADVANCE scan | 2 violations, both core-identical inherited lines (§7) |
| Same-baseline ink scan (`rowcheck.py`) | 0 collisions |
| P6 chart-label coverage (baseline-anchored ink, anchor ls) | 0.0% (gate <30%); P6 chart is text lines, no bars |
| Build warnings | no FLOW OVERFLOW / HEAD TOO WIDE in any round |
| Cards | all 8 pages visually inspected (P1–P8), incl. P7 readers'-corner box (disclosure inside the box, clear of the VOL.3 dark box) and P8 answer stream |
| Model essay | 85 words, = core |

Final SVG sha256 (round 3; `round3-baseline.sha256`):

- p1 `7de029da3348f7e3ea1a782cf4886c86e1d0b7661826767ab67915629fadbb76`
- p2 `c76ddd56be898815beb82b6f999d63c46624c0b46b7b1eea62f0acf0fcaa1b31`
- p3 `6c2116809bb83d3aa6e93b46c46acf828648bfab9c3e524e9662ddf014e31fc9`
- p4 `1ed87062592a4b10b36df7b27aa89b8676e228ecab13af45828a3150862bdcda`
- p5 `e5580ad4b64901e2b1c109e257d6633a7e52453eab99053d38ecc915d5298bff`
- p6 `1f8aac07225959614ef5d56108c0da3b81b32f84e207bfa22511e9bd1770dacc`
- p7 `397c2356b38550268531a9a86285b278aa6582893b11436d2d58e6b13b370e91`
- p8 `4bf81c17a5b9457d12fbe4efccca928042c76139a50c1ca2e1970c027d4fee7c`

Final PDFs:

- Print `The-Lucerna-VOL2-KO.pdf`: 21,530,330 bytes,
  sha256 `9a805dba23f7a6dc2d25f9e196d2fe8b9300dfdd178f43f973a76254ba0539b1`
- Web `The-Lucerna-VOL2-KO-web.pdf`: 3,898,955 bytes,
  sha256 `8ce20818fbc8ba537f08f505d0109f4bafca2e5713309e2b0eb2e0b45a4fa4df`
- Card PNG sha256 in `hidden_files/weekly-report-w45-en-ko-build/round3-cards-pdfs.sha256`.

## 6. P8 translation redirections and readers' corner (coordinator ruling applied)

P8 keydiff, item by item (core → this edition; English stems frozen):

- **#137** (EN→KO; stem `Translate: « Patience is part of the system, not a
  failure of it. »` frozen): core key `耐心是制度的一部分，而不是制度的失败。`
  → `인내는 제도의 일부예요, 실패가 아니에요.`; note
  `part of 一部分；not a failure 不是失败` → `part of = 일부분; not a failure = 실패가 아님`.
  Round-2 wording shortened the key to kill a mid-word line split (see §8).
- **#138** (stem redirected): core stem `翻译：Tuesday, November 3, is Election
  Day in the United States.` → `번역: Tuesday, November 3, is Election Day in
  the United States.`; key `11 月 3 日周二是美国的选举日。` →
  `11월 3일 화요일은 미국의 선거일이에요.`; note `Election Day 选举日；on Tuesday`
  → `Election Day = 선거일; on Tuesday = 화요일에`.
- **#139** (stem redirected): core stem `翻译：On Sunday, the NFL plays in
  Madrid.` → `번역: On Sunday, the NFL plays in Madrid.`; key
  `这周日，NFL 在马德里比赛。` → `일요일에 NFL이 마드리드에서 경기를 해요.`
  (round-2 shortening dropped `이번 주`, matching the English `On Sunday`
  and pulling the note's closing bracket back onto its line); note
  `on Sunday；in Madrid` → `on Sunday = 일요일에; in Madrid = 마드리드에서`.
- **#140** (EN→KO; stem `Translate: « Not every place changes. »` frozen):
  key `并非每处都拨回时钟。` → `모든 곳이 시계를 되돌리는 건 아니에요.`
  (note: core's key narrows the sentence to the clock context; the Korean
  key translates the sentence as printed); note `not every 并非每处；change 变化`
  → `not every = 모든 ~가 아니다; change = 바뀌다`.
- **#150** (writing-device item; key is rubric text, not an answer): core key
  `开放题 — 要点见写作框，范文在第 8 版写作框内` →
  `열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에`; note
  `按要点给分` → `기준 항목대로 채점해요` (verbatim W43 EN×KO wording).
- P8 note style: half-width brackets with a leading space ` ({note})`,
  explicit PRINT_NOTES set (78 items, from the W45 core extract) — the
  core's length≤10 rule is NOT used. P8 comments are pure Korean.
- P8 answer-stream direction note: items 137/140 keep the English
  `Translate:` stem; items 138/139 carry the Korean `번역:` label. All four
  keys are Korean.

Readers' corner (P7): no reader, letter, name, or quote is invented.
The core's English elements are kept verbatim: the letter paragraph
(including `(editor's example: no real reader letters had arrived when this
issue went to press, so the example stays, honestly labeled)`) and the
VOL.3 promise in the writing prompt. The disclosure itself is Korean and
states the 3 facts (no real letters arrived; no best P8 writing arrived;
the example is printed, honestly labelled, with the promise carried to
VOL.3) plus an explicit imperative invitation
(`여러분의 편지와 쓰기를 보내 주세요`) with a VOL.3 publication promise
(`VOL.3부터 실제 편지를 싣겠습니다`). The VOL.1→VOL.2 promise chain is
named (`VOL.1에서는 VOL.2에 실제 편지를 싣겠다고 약속했지만…`). No English
disclosure sentence was invented for a sentence the core does not contain.
Wording note: this disclosure is W45-specific (it names the VOL.1 promise
and the VOL.3 carry-over); it is not a copy of W43's disclosure.

## 7. Adjudicated non-defects (kept, with reasons)

- P2 `= two times(두 번)`: a telling-the-time vocab-list entry (word +
  gloss as a designed pair), not a wrap fragment; the column has the same
  shape in `= one more time(한 번 더)` and `= to go back one hour(한 시간 되돌리기)`.
- P8 `번역: On Sunday, the NFL plays in Madrid.`: a complete translation
  item stem (label + English sentence), not a fragment.
- P8 stream line-end numbers (`16.`, `60.`): full-width joined-stream lines
  (` · ` chains); the trailing number is the next item's number. Core P8
  has 31 structurally identical bare-number line ends — inherited layout.
- `·`-initial continuation lines (G flags): family format for gloss /
  option / answer continuations.
- Right-edge 2 lines, core-identical values: p8 y=806.4 edge=1899.4
  `b. an election in the middle of a term`; p8 y=882.4 edge=1903.8
  `d. the paper you mark your choice on`. Cause: `match_set` right items
  wrap at `self.w-34` then draw with a `b. `/`d. ` prefix, overshooting
  RIGHT 1885 but staying inside the 1950 page edge. Inherited, not new.
- Korean instruction counts: core `改写` 20 vs edition `바꿔 쓰기` 16 is
  not a loss — the 4 bridge sentences use the imperative
  `바꿔 쓰세요`, while the 16 item labels match 1:1 (core `填空` 24 =
  edition `빈칸 채우기` 24; core `把词和释义配对` 4 = edition
  `단어와 뜻 짝짓기` 4; match-set `짝짓기` 6 = 6).

## 8. Fix rounds (all in `transform.py`; pre-fix baselines archived)

- **Round 1 → 2 (8 fixes):** P2 bridge ending `날 일).` → `(계획을 말할 때).`;
  P4 gloss `지키다` split → `타이틀 지키기`; P6 bridge ending `에요.` →
  `숫자가 아니에요.`; P7 grammar point → `선택 의지예요.`; P2 AND YOU
  `편집부로` split → word order changed (editorial office moved before the
  object); P8 #139 key shortened (`이번 주` dropped); P8 #30 note
  shortened (고양이 dropped); P8 #137 key rewritten to
  `인내는 제도의 일부예요, 실패가 아니에요.`. Round-2 SVG changes: exactly
  P2/P4/P6/P7/P8; P1/P3/P5 byte-identical.
- **Round 2 → 3 (1 fix):** P8 #30 note still split `헤|이더가` because the
  line-full point, not the note length, set the break: dropped the leading
  `빌 ` so the break moved off the name (`헤이더가 목소리를 맡아요`).
  Round-3 SVG changes: only P8; all other pages byte-identical.
  Final scan: S1 0 / S2 4 (adjudicated, §7) / S3 0 / S4 0.
- Transform defects fixed during the build (also in `transform.py`):
  missing `svglib.py` copy (added with md5 gate); ASCII double quotes in a
  MAP value breaking generated code (switched to single quotes); two
  missing MAP entries (bare `对话补全` → `대화 완성`; cloze note
  `still 仍然` → `still 여전히`).

## 9. W43 deviations (W43 EN×KO furniture kept; W45 values re-derived)

- Furniture carried verbatim from the published W43 EN×KO SVGs: P1 badge,
  top-band middle line, footer, page line `제 {n} 면 / 총 {total} 면`,
  gloss prefix `해설 — ` (single), section-head bilingual form
  (`ENGLISH HEAD · 韩语短名`), P8 separators, P8 band right note, all
  item-type labels (incl. `문장 완성`, `객관식`, `단어 짝짓기`,
  `문장 바꾸기`, `빈칸 채우기`, `바꿔 쓰기`, `단어와 뜻 짝짓기`,
  `오류 고치기`, `도표 읽기`, `읽기 이해`, `따라 연습`, `번역`, `쓰기`,
  `짝짓기`, `대화 완성`), P7 `(page N)` labels kept in English, 해요체
  explanation voice.
- Re-derived from the W45 core (never copied from W43 or any sibling):
  VOL.2 (W43 was VOL.1); serif keywords `투표 · 축구 · 영화`; dark-band
  right lines (`화요일 선거일 · 일요일 시계 되돌림` /
  `11월 3일 화요일 선거일 · 6면 참조`, widths re-measured: left line ends
  1244, right line starts 1491); week Nov 2–8, 2026; all topics, gloss
  distribution (18, per §5), P7 labels, P1 word of the week, P8 printed
  set (78) and keydiff values, readers'-corner disclosure chain (§6),
  chart values 38/29/21/12, box titles (widths re-measured against the
  434 column; `A PRACTICE BALLOT · 연습용 투표용지` at 429.9 and
  `TOO CLOSE TO CALL · 승부를 알 수 없음` at 445.1 rejected as too
  tight / over limit; adopted `연습용 투표` ≈379 and `접전`).
- Box-title widths adopted (PIL SC-face advance, with margin):
  `AT HOME THIS WEEK · 집에서 볼 것` 400.8; `WHY MADRID? · 왜 마드리드일까?`
  382.4; `FIVE SENTENCES · 다섯 문장 과제` 381.0; `A PRACTICE BALLOT · 연습용 투표`
  ≈379; `SUNDAY, NOVEMBER 8 · 일요일` 364.3 — all < 434.

## 10. Fix round 1 (independent proofread blockers, P8 Korean splits only)

Independent proofread (`hidden_files/w45/en-ko-proof/REPORT.md`) blocked
the edition on 4 P8 mid-word Korean splits (tail ≥3 syllables, 10–45
window), all missed by the builder's `ko_scan.py`: its S3 check used
space tokenisation + `first.split("(")[0]` and excluded `(`-starting
continuations, so a split whose two sides carry parens produced a
parenthesised concatenation absent from the corpus. All other proofread
gates had passed and were not touched. This round changed ONLY the 4
notes below, all in `transform.py` (MAP values); no key, number, or
question fact changed, and no other item's note changed.

Pre-fix deliverable baseline (`fix-round1-prefixed.sha256` in the build
tree; 18 files: 8 SVG + 8 cards + 2 PDFs + KIT + ABSTRACT):

- p1 SVG `7de029da…`, p2 `c76ddd56…`, p3 `6c211680…`, p4 `1ed87062…`,
  p5 `e5580ad4…`, p6 `1f8aac07…`, p7 `397c2356…`, p8 `4bf81c17…`
- p8 card `1c7da9c7…`; print PDF 21,530,330 bytes `9a805dba…`;
  web PDF 3,898,955 bytes `8ce20818…`; KIT `ebfeb76c…`;
  ABSTRACT `1f482236…` (full hashes in the baseline file).
- Opening check: no rendering process was running; the last deliverable
  mtime (proofreader's disclosed in-place `dump_reg.py` rewrite, content
  verified unchanged) was >120 s old, so the run was safe to start.
  This round never ran `dump_reg.py` in place: the registry re-dump was
  done from a scratch copy with OUT repointed (see below).

Changes (old → new note; keys unchanged):

- **#67** (P8, x=527, y=2042.51→2062.66, was `휴대|전화예요` tail 4):
  `두 번째 화면은 휴대전화예요` → `두 번째 화면 = 폰`.
  Rendered now as `67. B (두 번째 화면 = 폰)` closed on one line, no
  split, no orphan paren. (An intermediate `= 휴대폰` form closed the
  note exactly at the line end and stranded a lone `)` on the next line
  — a new S1 flag — so it was shortened once more to `폰`; the
  intermediate form never shipped.)
- **#93** (P8, x=527, y=2390.87→2411.02, was `일|부예요` tail 3):
  `인내는 제도의 일부예요` → `인내는 제도의 일부`.
  Rendered now `일|부` tail 1. Meaning kept: patience is part of the system.
- **#102** (P8, x=527, y=2517.58→2537.73, was `동|사원형` tail 3):
  `would + 동사원형` → `would + 원형`.
  Rendered now `원|형` tail 1. Meaning kept: would + base form.
- **#149** (P8, x=1451, y=1895.65→1915.8, was `선|거일은` tail 3):
  `선거일은 11월 3일 화요일이에요` → `선거일 = 11월 3일 화요일`.
  Rendered now `선|거일` tail 2. Meaning kept: election day is Tuesday,
  November 3. The #137 key (`인내는 제도의 일부예요, 실패가 아니에요.`)
  and the P7 grammar point (`would + 동사원형, 선택 의지예요.`) are
  different strings and were NOT changed.

Tool fix (build tree only, not shared `tools/`): `ko_scan.py` in the
build tree was patched to strip parens/punctuation and take the
trailing Hangul run of the previous token and the leading Hangul run of
the next token, requiring both non-empty. Synthetic check: the patched
scanner flags all 4 original splits (S3=4); the old logic flags 0 of 4.
A first patched version without the non-empty guard produced 8 false
S3 flags from empty fragments (e.g. an English token followed by a
Korean word); the guard was added before the final run. The shared
`tools/` scanner was not touched — if it carries the same gap, that is
for the main line to fix.

Rebuild: `transform.py` → single-process `run.py` → `render.py`, all
with `tools/venv/bin/python`. P8-keys flow end stayed y=1965, TOTAL 150,
no FLOW OVERFLOW / HEAD TOO WIDE. One interrupted render (service
restart during a duplicated parallel call) produced a corrupt interim
p5 card; it was discarded and the render was redone once, cleanly, so
the shipped cards come from a single uninterrupted render.

Re-run gates (raw outputs `fix1b-*` in the build tree):

| Gate | Result |
|---|---|
| `freeze.py baseline` (core) | 8/8 byte-identical; core SVGs unchanged |
| `freeze.py diff` | P1–P7 added CJK unchanged; P8 872 → 858; TOTAL 2438 (not 2452 — the −14 is exactly the Hangul removed by the 4 shortenings: #67 −6, #93 −2, #102 −2, #149 −4); text-node Hangul 2438, Han 0 |
| `p8.py compare` (explicit dual SVG paths, `--total 150`) | CLEAN, core 78 = edition 78 noted, missing=[], extra=0, uncertain=[], keydiff=[137,138,139,140,150] unchanged |
| `occlusion_audit.py` (selftest first) | selftest 6/6 classes fired, clean controls silent; edition 0 flags, core 0 flags, NEW vs core 0 |
| Patched `ko_scan.py` window 10–45 | S1 0 / S2 4 (same 4 adjudicated non-defects as round 3) / S3 0 / S4 0 |
| Full-book candidate list (paren-aware, all tails) | same-x 16 candidates, tail ≥3 = 0; cross-x 0. The 16 are the round-3 tail ≤2 set (14, minus #67 which no longer splits, plus `모|범` tail 1) with #93/#102/#149 downgraded to tail 1/1/2 |
| Registry re-dump (scratch copy, OUT repointed, no in-place run) | 150 items; levels A2 60 / B1 69 / B2 21; pages 10/17/18/18/18/18/12/39; diff vs round-3 registry = exactly the 4 notes above, all keys/pages/levels/types identical; scratch renders 8/8 byte-identical to shipped SVGs (the stray scratch renders first landed under `files/weekly-report-w45-en-ko-build/` because the OUT string keeps its `files/` prefix; they were removed, delivery SVGs verified untouched) |
| `rowcheck.py` same-baseline ink | 0 collisions |
| `rightedge.py` ADVANCE | same 2 core-identical inherited lines as round 3 (p8 y=806.4 edge 1899.4; y=882.4 edge 1903.8); no new line |
| P8 card visual (cropped zones) | 4 splits gone; #67 closed on one line, #93/#102/#149 tails 1/1/2; answer stream clean, no overlap/truncation |

Change scope (pre-fix → post-fix hashes, full in `fix1b-postfix.sha256`):

- CHANGED: only `p8-exercices.svg` (`7cee4087…`), `p8-exercices.png`
  (`4868c268…`), print PDF, web PDF, and this KIT. P1–P7 SVG and cards
  are byte-identical to pre-fix.
- Print `The-Lucerna-VOL2-KO.pdf`: 21,530,271 bytes,
  sha256 `305b69f2413cb500f80f03d6229d7115e68e40d9286775eea5ea7c6cd4691949`
  (supersedes §5's round-3 print hash).
- Web `The-Lucerna-VOL2-KO-web.pdf`: 3,898,191 bytes,
  sha256 `380f734d1f2094eb9426827ce3b08153929f7598a7fe710f2bcd88b22642df0f`
  (supersedes §5's round-3 web hash).
- ABSTRACT.txt unchanged (`1f482236…`).

Status note: this KIT-only text update did not touch any SVG, card, or
PDF. Per SOP §8.4 this fix round changed rendered output, so a fresh
full independent proofread is still required — this section reports
fix-complete only and does not declare the edition final.

