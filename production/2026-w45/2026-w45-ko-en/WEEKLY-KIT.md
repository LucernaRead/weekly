# WEEKLY KIT — Lucerna Weekly VOL.2, Korean target × English reader (KO×EN)

Issue week: Mon Nov 2 – Sun Nov 8, 2026. Dated Mon Nov 2, 2026.
Status: **builder-complete** — built by the KO×EN builder, NOT finalized;
independent proofread still pending. No Discord post, no main-chat card/PDF
dump, no cron, no weekly-git write was made by this build.

## 1. Edition identity

- Masthead: `Lucerna` with NO article (Korean takes no article — same as the
  core and as W43 KO×EN).
- Badge (verbatim, W43 same-pairing string): `TEXT IN KOREAN · EXPLANATIONS
  IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`, 17pt, weight-700,
  olive #3e4c2a, y=394 (see §7 for the deviation from the tools README #20
  generalization).
- Footer: `Lucerna · KOREAN WEEKLY VOL.2 · Korean text · English explanations`.
  Page line: `Page N of 8`.
- Top strip: `매주 한국어로 · A new issue every week · …`.
- Band pattern: title `Korean · English` (e.g. `생활 · Life`); subtitle
  `Korean first half · English second half`; P8 band subtitle stays
  Korean-only (`제8면 · 이번 주의 큰 시험 + 모든 답`).
- Gloss prefix: `Note — ` (core uses `译注｜`). Type labels in English
  (fill-in / multiple choice / matching / cloze / sentence building /
  transformation / true/false / translation / writing); instruction labels
  (Fill in / Rewrite / Build a sentence / Translate / Write / Match the
  pairs / Match word to meaning).
- P8 answer header: `답 · Answer key — grouped by page; find your item
  number`, right line `Each item has a short English note · ✓ marks the
  model-writing item`. P8 separators kept Korean (`— 제N면 —`).
- Exercise headers: `연습 · Page N exercises`, right line `Answers on page
  8 · Items may mix levels; find them by number`.
- Phrases header: `이번 주의 문장 · Phrases of the week (verbatim from
  this issue)`, page tags kept Korean (`(1면)` etc.).

## 2. Core measured numbers (from disk, never copied from other families)

Source core: `files/weekly-report-w45-ko-core/` (VOL.2). Core explanation
layer is Simplified Chinese; articles/exercises are Korean.

- TOTAL 150; by page 10/18/18/18/18/18/12/38; by level A2 51 / B1 72 / B2 27.
- By type: 完成句子 48, 单选 52, 词汇配对 16, 完形单选 13, 造句 8,
  句型转换 4, 判断 4, 翻译 4, 写作 1.
- P7 structure: A2 column `입동의 말`, B1 column `날짜 세는 말`, B2 column
  `예보 읽는 법`; error clinic ×4; frame `〜부터 〜까지` (산불조심기간
  example); readers' corner with editor's example letter + on-page
  disclosure; 8 phrases of the week; VOL.3 preview (teaser).
- P8 zones: A 연표 完形单选 8, B 一般问题 单选 8, C mini-reading 지민이
  story + 单选 4, D 造句 4, E 翻译 4 both directions, F 词汇配对 4, G
  dialogue 完形单选 5, H writing 1 on `나의 겨울 준비`.
- P8 E-zone re-aim (core KO↔ZH → this edition KO↔EN), verified on the
  rendered P8: 137 stem Korean `11월 7일은 입동이에요.` → key `Nov 7 is
  Ipdong.`; 138 stem Korean `수능까지 12일이 남았어요.` → key `There are
  12 days left until the CSAT.`; 139 stem English `Special measures apply
  only on November 19.` → key Korean `특별 조치는 11월 19일에만 적용돼요.`;
  140 stem English `I go to Naejangsan on Saturday to see the autumn
  leaves.` → key Korean `저는 토요일에 내장산에 단풍을 보러 가요.`
  Answer-key notes: `From page 1 / 5 / 6 / 3` respectively.
- Writing model: 157 Korean characters excluding spaces (counted from the
  frozen source text, identical in core and edition); printed instruction
  `150–200자`. Model text frozen verbatim.
- P8 printed-note standard, measured from the core render with
  `tools/p8.py extract --total 150`: noted set = 150 of 150 (the KO core's
  own measured value). Core P8 style is dash style (`N. key — note`).
- P1 geometry (core render): subtitle y=372, rules 392/401, dark band
  y=424, band lines 478/522, headline block starts hy=580.
- Images (all verified public-domain/CC0, credit lines from the Commons
  API Artist field, captions honest as file photos): P1 autumn.jpg
  (lumoplank, CC0); P2 ssam.jpg (wizdata, CC0); P3 bukhansan-ui.jpg
  (Udonhan1992, CC0) + apples.jpg (Cézanne, public domain); P4
  baseball.jpg (Bain News Service, public domain); P5 study.jpg (Gary
  Todd, CC0); P6/P7/P8 no photos.
- Core SVG sha256 (recorded 2026-10-27, re-verified unchanged after this
  build): p1 f1e6913d…, p2 839dcdd0…, p3 74371179…, p4 7f0aed9b…,
  p5 68e6ead9…, p6 e7f53e42…, p7 ddb4e76c…, p8 17031514…; core print PDF
  33,125,291 bytes sha 4b9642d1…, web PDF 3,366,637 bytes sha 26075ca5…
  (full hashes in the build dir `core-baseline-sha256.txt`).
- Trend-first check (from `hidden_files/w45/trend-batch-C.md` KO section,
  research date 2026-10-26): core lead `입동 주간: 단풍의 끝, 김장의 시작,
  수능 카운트다운` matches the trend pool's W45 lead recommendation exactly
  — 입동 Sat Nov 7, last foliage weekend, kimjang season opening, CSAT
  countdown mood (exam itself Nov 19, outside the week), 한능검 81회
  registration week (Seoul/Gangwon/Jeju Fri Nov 6 10:00–12:00 only),
  산불조심기간 from Nov 1. This is a genuine Korean-ecosystem current
  hotspot, NOT anniversary/commemorative marketing; CSAT-day measures are
  dated Nov 19 only throughout; no international politics.

## 3. Build method and interpreters

- Build dir: `hidden_files/weekly-report-w45-ko-en-build/` — copied from
  the W45 core build (`bslib4.py`, `content12/34/56/7/8.py`, `svglib.py`,
  `run.py`, `render.py`, assets), OUT paths repointed to this edition dir,
  PDFs renamed `Lucerna-VOL2-EN.pdf` / `Lucerna-VOL2-EN-web.pdf`.
- `tools/freeze.py baseline` on the unmodified copy: 8/8 SVGs byte-identical
  to core before any change.
- run.py interpreter: `tools/venv/bin/python` = Python 3.12.3, PIL 13.0.0.
  render.py interpreter: the same venv (`tools/venv/bin/python`, Python
  3.12.3, PIL 13.0.0) — render.py must use the venv because system python3
  has no cairosvg. The venv run byte-reproduced the core SVGs, satisfying
  the byte-reproduction requirement.
- svglib.py left byte-identical: the W45 core's NO_START already includes
  ASCII closers `)]}〉》.,!?%:;`, so no extension was needed. Core
  bslib4 orphan-control params kept (`para` w, `ex` bw, `match_set`
  narrow).
- transform.py: exact unique-literal / whole-line replacements with
  per-replacement occurrence assertions and counts logged. Korean target
  text never touched; only the explanation layer (Chinese glosses, notes,
  furniture second halves, P8 notes) rewritten in English.
- Transform-list corrections made during the run: (1) content34 has no
  cloze items — entry removed; (2) content8 has no fill-in items — entry
  removed; (3) P8 answer-header old string starts with Korean 답
  (U+B2F5), not Chinese 答 (U+7B54) — fixed; (4) content56 substring trap:
  `特别措施只适用于11月19日` must be replaced before `措施只适用于11月19日`;
  (5) per-file gaps: `당신은? · 说说你自己` → `당신은? · And you?` and
  `把词和说明配对` → `Match the pairs` occur in content34/content56 as
  well as content12; (6) a clinic translation typo caught before rendering
  (past form of 담그다 is 담갔어요, not the mistyped form).
- Post-transform check: 0 Han (U+4E00–U+9FFF) lines in bslib4.py + all
  content*.py files.

## 4. Round 1 → round 2 fix log

Round 1 rendered TOTAL 150 with matching level/page distribution, but one
defect: `FLOW OVERFLOW [P1-headline]` (English gloss box taller → numbers
box displaced to column 2 → drill 6 spilling past bottom 1828 into row B).
Round-1 canonical occlusion audit: 10 flags, all real, all in the English
layer (core 0 flags). Round-1 pre-fix hashes saved in
`round-baselines/round1-sha256.txt`; round-1 PDFs: print 32,378,810 bytes,
web 3,511,505 bytes (superseded).

Round-2 fixes (all in transform.py; pre-fix state verified unchanged since
round 1 and saved as `round-baselines/round2-pre-sha256.txt`):
- P1 gloss shortened 5 lines → 3 lines: `입동 = ipdong · 절정 = peak ·
  김장 = kimchi-making · 상륙하다 = landfall · 온대저기압 = extratropical
  cyclone` (3-line candidate with no leading `·` on line 3 and full
  `extratropical cyclone` kept; 4-line candidates and the candidate
  ending `= cyclone` rejected).
- Box titles shortened (W43 precedent style), with measured ink widths:
  P1 numbers `숫자로 보는 이번 주 · Numbers` (316.1px); P2 한능검
  `한능검 접수 · Korean History sign-up` (394.9px, right ink 939.9 <
  961); P3 prep `단풍 구경 준비물 · Leaf-viewing list` (369.7px); P5
  youth `이번 주 청년 숫자 · Youth numbers` (363.1px, also fixes the P5
  TEXTX graze).
- Calendar backbone line → `These five dates frame this issue.` (299.5px
  at 18.5pt < 390px box inner width, one line, no collision with fixed
  source lines).
- P7 disclosure shortened 10 lines → 8 lines (text in §6), saving 58px.
- Round-2 render: zero FLOW OVERFLOW / HEAD TOO WIDE warnings; P1-headline
  flow ends col 2 y=1413 (exactly the core value); P7 col3 ends 1741.46;
  P7 teaser ends 2515.46 (< 2540 gate); P8 exercise flow ends col 3 y=403
  (core value); P8 keys flow ends y=2440 in its last column; TOTAL 150.

## 5. Gate measurements (round 2, final delivery)

- Canonical occlusion audit (`tools/occlusion_audit.py`, selftest OK — all
  6 planted classes fire, clean controls silent): edition 0 flags, core 0
  flags, NEW vs core 0.
- Custom rendered-SVG audit (`audit.py`, venv PIL): ED line-start=0,
  splits≥3=0, row-overlap=0, right-edge=0 on all 8 pages; core likewise
  0 on all pages. The split scan is source-aware (eojeol vocabulary +
  consecutive word pairs from build source via ast, no execution; window
  10–45; ≥3-syllable tail; English explanation layer excluded; Korean
  furniture strings included). Anchor-aware attribute parsing (the
  round-1 false-positive bug class is fixed and documented in
  `round1-audit.txt`).
- Paint-order graze check (`graze.py`: anchor-aware PIL advance boxes vs
  every later-drawn rect/image box; advance boxes are ink supersets, so 0
  hits proves 0 ink coverage without getbbox): ED 0 hits on all 8 pages,
  core 0 hits. P6 comparison-table label coverage by later rects = 0%
  (< 30% gate); the table spans x=65..1453, col-3 boxes start x=1451 but
  are y-disjoint, exercises start y≥1548, table ends y≈1476.
- ADVANCE full-page right-edge scan: 0 on all pages (part of `audit.py`
  above). Full-page frame-line scan: canonical audit LINEX covers line
  crossings (0 flags); frame rects are drawn first, so no later frame
  element can cover text (graze check confirms 0 later-rect hits).
- Freeze diff core vs edition: added CJK characters = 0 on every page
  (p1 +20/−19, p2 +39/−36, p3 +30/−28, p4 +23/−21, p5 +32/−31, p6 +17/−15,
  p7 +41/−39, p8 +174/−167; CJK totals drop because the Chinese layer
  left and Korean stays). TOTAL added CJK = 0.
- P8 compare (`tools/p8.py`, explicit dual paths, `--total 150`): CLEAN,
  missing=[], extra_count=0, uncertain=[], keydiff=[137, 138] — exactly
  the two E-zone re-aimed keys, unambiguous as required (tool version
  note: under the pre-fix tools/p8.py, sha 67df05f1…, keydiff read
  [109, 137, 138] with 109 as a tool artifact — printed keys both 기준;
  under the adopted post-fix tools/p8.py, sha 96fc2cfe…, keydiff reads
  [137, 138]). Note:
  `--core-dir` form selects the wrong P8 filename by native, so dual
  paths are mandatory.
- P8 note-completeness (keys-flow lines only, y in (1328, 2540),
  column-grouped): core 150 lines, edition 150 lines, numbers 1..150 in
  both, byte-identical lines = 0 — every core Chinese note localized to
  English. Korean-containing core P8 notes (23 items: 25–28, 34, 43–46,
  57–64, 135–136, 141–144) are frozen Korean headword citations with the
  surrounding explanation localized to English (e.g. 34 `절정 — The most
  beautiful autumn leaves are called 절정`; 57 `Past form of 이기다:
  이겼어요`; 135 `보러 가요 = to go to see`); none is an untranslated
  Chinese note. Item 150 note: `✓ Model text in section H of this page
  (157 characters)`.
- P8 answers-flow end: max last baseline across columns 2530.35 (col 2,
  item 113), glyph bottom ≈2534 < 2540 gate; footer rule at 2580.
- P7 teaser end 2515.46 < 2540 gate; P7 teaser title y=2441.46, body first
  line 2481.5.
- Phrase verification: 8 P7 phrases, whole-issue occurrence counts core vs
  edition identical — 5 / 2 / 4 / 2 / 2 / 2 / 2 / 2 (English translations
  underneath are new apparatus and do not affect Korean counts).
- Gloss verification: per-file gloss/glossline ·-item counts core vs
  edition identical — content12 24, content34 26, content56 28,
  content7 6, TOTAL 84; every edition gloss string verified present in
  the rendered page text (spaceless substring check, 0 missing).
- Image payloads: sha256 of embedded data URIs core vs edition identical
  per page, pattern 1/1/2/1/1/0/0/0 (p1/p2/p3/p4/p5/p6/p7/p8).
- Rendered-text checks on final SVGs: Han characters in text nodes = 0
  on all 8 pages; ASCII double-quote characters in text nodes = 0 on all
  8 pages; banned-word gate = 0 occurrences in final SVGs, build code,
  ABSTRACT.txt, and this KIT.
- Visual gate: all 8 cards viewed (p1–p8), zero defects found.
- Final delivery hashes (see §8) equal the round-2 baseline; core SVGs
  re-hashed unchanged after the build.

## 6. Readers' corner gate

- Korean example letter frozen verbatim from the core; zero invented
  names/letters/quotes.
- English disclosure (8 rendered lines, box col 3 y=1528.61–1727.41):
  `Editor's note: this is an example letter from the editors, not a real
  reader's letter. No real reader letters or best page 8 writing had
  arrived by press time, so the example stands and last issue's promise
  carries to VOL.3. Send us your letter and your page 8 writing — write
  two sentences in Korean and send them in!`
- Covers all three facts (example not a real letter; no real reader
  letters; no best P8 writing) + explicit imperative solicitation covering
  BOTH letters and P8 writing + VOL.3 promise. The teaser line
  (`여러분의 편지와 8면 쓰기 우수작도 실어요`) is NOT counted as the
  solicitation. The pt-family scope adjudication (solicitation literally
  covering letters + disclosure deferring best P8 + teaser naming P8 best
  = combined satisfaction) was considered but made moot by writing the
  imperative to cover both directly.

## 7. W43 same-pairing deviations (measured, with reasons)

W43 KO×EN (`files/weekly-report-ko-en/`, VOL.1) takes precedence over the
tools README #20 generalization wherever they differ; all differences
below are measured, not assumed.

1. Badge geometry: W43 measured badge is 17pt, weight-700, olive #3e4c2a
   at y=394 — NOT the README #20 majority 20pt BRICK. This edition uses
   the W43 measurement (subtitle 366, badge 394, rules 412/421, dark band
   433, band lines 487/531; core values 372 / 392/401 / 424 / 478/522).
   Headline block (hy=580) and everything below y=606 unmoved.
2. Readers'-corner disclosure is deliberately STRONGER than W43's single
   short English honesty line: the W45 brief requires three facts +
   imperative + VOL.3 promise, so the disclosure was rebuilt (see §6).
3. Box-title shortenings are new to W45 (round-2 fixes, §4) with measured
   ink widths; W43 titles were not reused verbatim because the English
   layer is longer in W45.
4. Shared-tool fix made during this build: `tools/p8.py` `detect_note` —
   a ` — ` separator occurring strictly BEFORE the last paren group opens
   now wins as dash style (root cause of the initial keydiff item 109:
   edition note `The dates differ because the criteria differ (page 3)`,
   a dash-style segment trailing with an ASCII parenthetical; the core
   note used full-width （3版） so it parsed as dash). A dash only INSIDE
   the paren group still loses (Russian case preserved). Unit checks
   post-fix: ED109 → dash key `기준`; Russian paren case → paren; plain
   dash → dash; paren-only → paren; multi-dash → dash; core109 → dash.
   Regression checks run before/after: en-es (total 149) unchanged
   [137,138,139,140,149]; de-nl (150) unchanged [137,138,139,150]; es-nl
   (150) changed from [17,18,19,20,60,61,62,63,64,72,83,85,95,96,98,107,
   117,137,138,148] to [137,138] — verified by inspection that es-nl
   items 17/60/148 have identical keys and only Dutch notes adding
   trailing parentheticals (e.g. `17. preguntan — todos → preguntan (zij
   vragen)`). Conclusion: es-nl's long pre-fix keydiff list was the same
   tool artifact class, not edition errors. Flagged to the parent; es-nl
   itself NOT modified.

## 8. Three-way furniture comparison

| Element | W45 core (KO×ZH) | W43 KO×EN (VOL.1) | This edition (VOL.2) |
|---|---|---|---|
| Masthead article | none | none | none |
| Subtitle y | 372 | 366 | 366 |
| Badge | none (Chinese strip) | y=394, 17pt bold olive, verbatim string | same as W43 |
| Rules / band / band lines | 392/401 / 424 / 478/522 | 412/421 / 433 / 487/531 | same as W43 |
| Footer | Chinese explanations | `KOREAN WEEKLY VOL.1 · Korean text · English explanations` | VOL.2 form |
| Page line | `Page N of 8` (Chinese furniture) | `Page N of 8` | `Page N of 8` |
| Gloss prefix | `译注｜` | `Note — ` | `Note — ` |
| P8 header | Chinese | `답 · Answer key — grouped by page; find your item number` | same as W43 |
| P8 separators | `— 제N면 —` | `— 제N면 —` | `— 제N면 —` |
| Readers' disclosure | Korean + Chinese | short English honesty line | 8-line English (§6) |
| Band subtitle P8 | Korean-only | Korean-only | Korean-only |

## 9. Delivery files

- `files/weekly-report-w45-ko-en/svg/` — p1-pyoji.svg
  6e268ccb62183ec1ede80949b286bade24fcc0aa8eea2d04204e4346bd7c5192,
  p2-saenghwal.svg
  ab3c14223b098ce0fbd526101d8eb00ca103b052b6a6aa9234392fe52086a243,
  p3-munhwa.svg
  75ade374bcd2c8a1f056f673547ca6cd1387c5265d165ef6d3c179900ef5ffd1,
  p4-seupocheu.svg
  2c1675226edb7526a4c032fd5db54922510304c26ccdd40369bb593c79739f12,
  p5-cheongnyeon.svg
  744901fb902cb2310fd81d2b9d8feffa4ea13bb82aae87a4743b06797e819b27,
  p6-gipi.svg
  0678de1924533b406238cfcb5efd3b9a63a5165494dd5bd239bb19e7d547747c,
  p7-mal.svg
  7a989f6b4fc58a12bda4472bf46ebd7d4395fcdd204cbdc2368715c5d4a722d7,
  p8-siheom.svg
  c75acc23c4721f19ebb6e2866085a032bd9b62e33ca0892f695ea6485a930a6c.
- `files/weekly-report-w45-ko-en/cards/` — p1 79ff123c…, p2 8260baf7…,
  p3 0f8b10da…, p4 8fb3c076…, p5 8d2d94dd…, p6 6d3695db…,
  p7 4f4a2d93…, p8 6de0dbf2… (full hashes in build dir
  `round-baselines/final-sha256.txt`).
- `files/weekly-report-w45-ko-en/Lucerna-VOL2-EN.pdf` — 32,378,317 bytes,
  sha256 d169aff6b8740f66c4aad18c8cdb919df3d922eeae8fe5347c0f71d6f8800254.
- `files/weekly-report-w45-ko-en/Lucerna-VOL2-EN-web.pdf` — 3,502,762
  bytes, sha256 20d9d1d5909cb88a331dfd829c6556170346e5194a5c1e532fb2aa5ca3c99e1c.
- `files/weekly-report-w45-ko-en/ABSTRACT.txt` — English, single line,
  no ASCII double quotes, 294 chars: names Ipdong week, last autumn
  foliage weekend, kimjang season opening, CSAT countdown, Korean History
  exam sign-up, autumn baseball, levels A2–B2, 150 exercises, learner
  search phrase `learn Korean by reading`.
- Build tree: `hidden_files/weekly-report-w45-ko-en-build/` (transform.py,
  audit.py, graze.py, round1/2 run logs and audits, round1/2 diffs,
  round1 p8.json, round-baselines/{core-baseline,round1,round2-pre,
  round2,final}-sha256.txt, round2-measurements.txt).

## 10. Non-goals respected

No writes to the core dir, W43 dirs, or `~/workspace/weekly-git`; no
Discord post; no cards/PDFs sent to main chat; no cron created; no
subagents spawned; no shared scratch directories cleaned. The core SVGs
were re-hashed unchanged after the build (§5).
