# WEEKLY KIT — Lucerna Weekly VOL.2, W45 (2026-11-02 – 2026-11-08)

## Status (builder-complete, NOT finalized)

- **Pairing:** target language **Korean (KO)** × reader native language **Traditional Chinese (ZH-TW)**.
  This is a legal pairing: the ban is on Simplified↔Traditional Chinese *target* inter-translation;
  KO target × Traditional-Chinese readers is not in the ban list.
- **Builder-complete** means: all gates below were measured by the builder on 2026-10-28.
  Finalization is by independent proofread; this edition is **NOT finalized** by this document.
- **NOT posted to Discord** (delivery paused by the user's 2026-10-21 decision).
  **NOT inserted into any repo** (insertion is the coordinator's serial step).
  **NOT sent into the main chat** (no cards/PDFs dumped). **No cron created.**
- **Build tree:** `hidden_files/weekly-report-w45-ko-zh-tw-build/` (single edit source: `transform.py`;
  working scratch in `scratch/` inside that tree).
- **Core (read-only reference):** `files/weekly-report-w45-ko-core/` and its build tree
  `hidden_files/weekly-report-w45-ko-build/`.
- **W43 same-pairing furniture benchmark (read-only):** `files/weekly-report-ko-zh-tw/`
  and its build tree `hidden_files/weekly-report-ko-zh-tw-build/`.

## Delivery list

Directory: `files/weekly-report-w45-ko-zh-tw/`

| File | Value (round 3, final, re-verified at KIT write time) |
|---|---|
| `svg/p1-pyoji.svg` … `svg/p8-siheom.svg` | 8 SVGs, SHA-256 unchanged vs `scratch/round3-sha256.txt` after the orphan-harness re-render |
| `cards/p1-pyoji.png` … `cards/p8-siheom.png` | 8 cards, all 8 visually inspected (see Visual check) |
| `Lucerna-VOL2-ZHTW.pdf` (print) | **33,167,237 bytes**, SHA-256 `0c48d6a99b662e57b5c176ec6a055673b9a23412e6b8098187fb4664579a1358`, 8 pages, page size 1462.5 × 2025 pt |
| `Lucerna-VOL2-ZHTW-web.pdf` (web) | **3,376,265 bytes**, SHA-256 `43066bd4b7069660a633dd950fa659747d9ae08c136c36d667504ab02f17b13c`, 8 pages, page size 1400 × 1938 pt |
| `WEEKLY-KIT.md` | this file |
| `ABSTRACT.txt` | Traditional Chinese, single line, no ASCII double quotes (see Abstract) |

## Spec (core-measured values, not copied from other families)

- VOL.2; masthead `Lucerna` with **no article**; page size 1950 × 2700; 4 columns.
- Issue week 2026-11-02 to 2026-11-08; theme: Ipdong week, last foliage weekend,
  kimjang / winter-prep season opening, CSAT countdown D-17 (Nov 2) → D-12 (Nov 7);
  CSAT-day measures dated **2026-11-19 only**.
- 150 exercises; pages 10/18/18/18/18/18/12/38; levels A2 51 / B1 72 / B2 27;
  types: 完成句子 48, 單選 52, 詞彙配對 16, 完形單選 13, 造句 8, 句型轉換 4, 判斷 4, 翻譯 4, 寫作 1.
- P8: 38 items (A8/B8/C4/D4/E4/F4/G5/H1); printed-note set 150/150; dash style `N. key — note`;
  writing model 157 characters excluding spaces, starting `나의 겨울 준비는 김장부터 시작해요.` (frozen byte-for-byte;
  MODELO assignment diff core vs edition is empty; NCHARS formula identical).
- P7: A2/B1/B2 columns ×4 exercises each + error clinic ×4 + frame `〜부터 〜까지` +
  readers' corner + VOL.3 preview; golden sentences whole-issue frequencies **5/2/4/2/2/2/2/2**.
- Images per page 1/1/2/1/1/0/0/0: P1 autumn, P2 ssam, P3 Bukhansan + apples,
  P4 baseball (Bain, public domain), P5 study photo; P6/P7/P8 no photos.

## Furniture: three-way table (W45 core / W43 ko-zh-tw measured / this edition)

W43 ko-zh-tw measured SVGs take priority over README generalizations; the KO-family
general form (subtitle 366, badge y=394, rules +20, band +9) is reference only.

| Item | W45 core | W43 ko-zh-tw (measured) | This edition |
|---|---|---|---|
| Pairing badge, P1 | — (core is the zh-cn edition) | `韓語正文 · 繁體中文講解 — 給繁體中文讀者的版本`, 20pt sans bold, BRICK `#a4553a`, centered x=975, y=394 | Same string, size, color, x, y |
| Subtitle y | 372 | 366 | 366 |
| Masthead rules | 392 / 401 | 412 / 421 | 412 / 421 |
| Dark band rect y | 424 | 433 | 433 |
| Band texts y | 478 / 522 | 487 / 531 | 487 / 531 |
| Footer, every page | (Simplified footer) | `Lucerna · 韓語週報 VOL.2 · 正文韓語 · 講解繁體中文`, 20pt, y=2624 | Same |
| Page line | (Simplified form) | `第 N 版 / 共 8 版` | Same |
| P8 head left | `답 · 参考答案 — 按版面分页排列，找到题号即可` | `답 · 全部答案與簡析（第 1–8 版）` | W43 form |
| P8 head right | `每题附一句中文简析 · 带 ✓ 的为范文题` | `每題附一句中文簡析 · 帶 ✓ 的為範本題` | W43 form |
| P8 separators | `— 제N면 —` (Korean) | `— 第 N 版 —` | W43 form |
| P8 band sub-line | `제8면 · 이번 주의 큰 시험 + 모든 답` | stays Korean-only | Same (Korean-only) |
| Gloss prefix | `译注｜` | `譯注｜` | `譯注｜` |
| Band titles | 生活 / 文化 / 体育 / 青年 / 深读 / 语言 / 测验与答案 | 生活 / 文化 / 體育 / 青年 / 深讀 / 語言 / 測驗與答案 | W43 Traditional forms |
| Type names | 完成句 / 单选 / 配对 / 完形 / 造句 / 变换 / 判断 / 翻译 / 写作 | 單選, 詞彙配對, 完形單選, 句型轉換, 翻譯, 改寫, 判斷, 寫作; shared: 完成句子, 填空, 造句, 全部 | W43 Traditional forms (see Registry comparison for counts) |
| Font faces | `Noto Serif/Sans CJK KR` | `Noto Serif/Sans CJK TC` | TC faces; shipped SVGs use only `Noto Sans CJK TC`, `Noto Serif CJK TC`, and (P1 only) `UnifrakturMaguntia` |

## Language-layer method and transform assertion regime

- **Method:** fresh copy of the core build tree each round; `transform.py` (single edit source) applies:
  (1) a literal map (Simplified explanation strings → natively authored Traditional strings,
  longest-source-first, with pre-count and post-absence assertions);
  (2) structural edits (output paths, PDF names, svglib TC faces, footer/page line,
  P8 separators, P1 badge geometry, P7 readers-box slack, P7 phrase pitch);
  (3) the svglib docstring change (`_sc_index` → `_tc_index`, `endswith("KR")` → `endswith("TC")`,
  defaults `Noto Serif/Sans CJK KR` → `CJK TC`, example `重阳` → `重陽`).
  Transform refuses to run twice (badge-present abort).
- **Simplified/Traditional independence:** Simplified and Traditional Chinese are independent native
  editions, never generated by converting one from the other. Explanation text was written natively
  for Taiwan/Hong Kong Traditional readers (Taiwan/Hong Kong usage forms; e.g. `準季後賽` for
  준플레이오프 — the P4 note `半决赛胜队是KIA` refers to the semi-playoff — and `漢拏山` for 한라산).
  Only the explanation layer changes; Korean target text is frozen byte-for-byte.
- **Transform verification (2026-10-28):** fresh tokenize extraction of the transformed tree vs the
  core tree gave 238 distinct CJK literals on each side; 210 new literals, all accounted for
  (MAP destinations, STRUCT products such as the badge and the top-strip `每週一期`, or substring
  products such as `青松現場慶典11月4日起`); the 28 core literals still present were all verified
  as Simplified/Traditional shared glyphs — with one real exception found later and fixed in round 3
  (see Rounds log).

## Gate 1 — Freeze (8/8)

- Baseline first: `tools/freeze.py baseline` against the core build reproduced all 8 core SVGs
  byte-identically (8/8); shipped core SVGs re-verified unchanged at KIT time
  (`scratch/round1-core-svg-sha256.txt`, 8/8 OK).
- `tools/freeze.py diff` raw output (core → edition CJK totals per page: P1 1462→1492,
  P2 1612→1623, P3 1524→1534, P4 1232→1242, P5 1433→1444, P6 1276→1287, P7 1365→1391,
  P8 2496→2507; total added CJK 949 — round-4 re-run of current tools/freeze.py
  (per-page added 75/74/63/51/57/41/88/500; an earlier draft of this KIT wrote 948) is **not** itself the gate, because the added CJK are
  Traditional explanation characters, which must be accounted separately from frozen Korean text.
- Operative proof (`scratch/audit_extra.py`): after excluding registered furniture (both Korean and
  Traditional page lines, both separator forms, both footers, P1 badge, P8 head form, and the P7
  disclosure by substring), the Han-stripped, whitespace-stripped concatenation of all removed vs
  added strings in draw order is **equal on all 8 pages**. All remaining per-line differences were
  individually adjudicated as gloss-box wrap splits at different points in the TC face (same
  underlying text), the P3 caption split, or registered furniture. P8 has 0 added pure-Hangul
  strings; P1–P7 added CJK are explanation-layer Traditional characters only.
- P8 Korean-word-head exceptions: none needed — P8 keys are Korean-frozen except 138 (see Gate 2);
  no ko-fr/ko-es-style #104 절기-type citation was required.

## Gate 2 — P8

- `tools/p8.py compare` with explicit dual paths (`--core-p8` / `--edition-p8`, `--total 150`):
  **CLEAN**, core 150 noted = edition 150 noted, missing [], extra 0, uncertain [],
  tool keydiff **[138]**.
- Key-part adjudication (keys only, notes excluded):
  - True key difference is **138 only** (`离高考还剩 12 天。` → `離高考還剩 12 天。`, note `對照第 5 版`).
  - **137 is not a key difference:** its key `11月7日是立冬。` is Simplified/Traditional shared-glyph
    identical (note Traditionalized to `對照第 1 版`). This corrects the task's prior expectation
    of [137,138] with printed-line evidence.
  - 139/140 keys are Korean byte-identical to core (notes Traditionalized; notes `對照第 6 版` / `對照第 3 版`).
  - 109 has no key difference (key `기준` identical; note Traditionalized) — consistent with the
    old-tool 109 item being a dash-style extraction artifact.
  - 150 is the H apparatus line (`✓ 範本見本版 H 區（157 字）`), localized as designed and excluded
    from the tool keydiff by design (same treatment as the ko-fr edition).
- P8 numbered key lines 1–150 present exactly once; P8 keys-flow region (y 1328–2580) max baseline
  **2514.92**, max ink bottom **2517.92** (< 2540); run-log flow cursor `flow[P8-keys] ended col 3/3 y=2351
  (bottom 2540)`.
- P8 flow calibers (three, all < 2540): flow cursor 2351; last-column last baseline 2335.05;
  last-column last ink bottom 2338.05; overall max ink bottom 2517.92.

## Gate 3 — Gloss (both calibers, both equal to core)

Two calibers, method stated (README #21 caliber issue is for the parent to settle; the gate is
equality with core, not reconciling 66 vs 84):

- Call-string caliber (source `gloss()`/`glossline()` arguments split on `·`): core = edition per file —
  content12 24, content34 26, content56 28, content7 6, content8 0 — **total 84**.
- Rendered-page caliber (gloss boxes in rendered SVGs, segments = `·` separators + 1 per box):
  core = edition per page — P1 5, P2 16, P3 13, P4 7, P5 12, P6 8, P7 0 boxes
  (P7 glosslines covered by the call-string 6), P8 0.
- P7 word boxes: definition sentences frozen; only gloss lines localized (localizing a definition
  sentence would be a freeze failure per the DE×NL/general ruling).

## Gate 4 — Golden sentences

All 8 verified verbatim from this issue's own articles with correct page tags;
whole-issue frequencies edition = core = **5/2/4/2/2/2/2/2**; each phrase present on its tagged page.
(An earlier audit-extraction false positive matched P7 clinic error strings in 「」; the fixed
extraction restricts to the phrases section after the `이번 주의 문장` header.)

## Gate 5 — Geometry

- Canonical `tools/occlusion_audit.py` (self-test OK: all 6 planted classes fired, clean controls
  silent): edition **0 flags**, core **0 flags**, NEW (edition-minus-core) **0 flags** — re-verified on round 3.
- Supplementary scans (`scratch/audit_geom.py`, baseline-anchored ink; see note on the anchor fix below):
  - ADVANCE full-page right-edge scan (inner frame x=1910): worst advance end **1885.0** (= frame edge)
    on every page, **0 flags** on all 8 pages.
  - Same-baseline ink-overlap scan (0.6px grouping, gap <2 flagged): **0 pairs** on all 8 pages.
  - Footer-band intrusion (ink below y=2580 except footer texts at y=2624): **0 flags** on all 8 pages.
  - P6 chart-label coverage (baseline-anchored ink boxes vs later rects/images): worst **0.0%**,
    gate <30%, **passed** (167 labels).
  - Web-PDF vs cards page-by-page comparison: mean absolute difference 0.85–1.2 per page,
    % pixels differing by >30 = **0.0% on all 8 pages** — no noise pages (see Gate 11).
- Anchor-fix note: the first version of the supplement used PIL `getbbox` with the default ascender
  origin, which overstated ink bottoms by ~an ascent (P7 readers air −11.19, P6 coverage 54.55% on
  `날짜 세기`). Both were measurement artifacts, not defects: with baseline-anchored ink
  (`anchor="ls"`) the true values are P7 readers air +12.81px and P6 coverage 0.0%. The canonical
  occlusion audit (0 flags throughout) corroborates the corrected values.

## Gate 6 — Orphan scan

`scratch/orphan_harness.py` (full single-process rebuild, 535 `svglib.wrap()` calls recorded):
- KO-dominant multi-line wraps with NO_START residuals: **0**.
- KO mid-word splits with tail ≥3 Hangul syllables: **0**.
- KO lone final fragments (≤3 chars): **11**, all adjudicated legitimate:
  gloss-box final segments (`害怕。`, `品嚐。`, `禮儀。`, `滑。`, `混淆。` — complete final gloss segments);
  P3 caption second line (`사진` — benign reflow, same caption text);
  frozen title final (`소식`); frozen option word (`대구`); true/false options (`틀리다` ×3).
- ZH-dominant multi-line wraps: 10, NO_START residuals: **0**.
- Rendered-line window scan (dy 10–45) over shipped SVGs: line-start NO_START flags: **0**.
- Rendered lines starting with `·`/`—` (supplementary): P3/P6 identical to core (frozen exercise-option
  continuations); P5 `· 합격 合格。` is a new gloss-continuation line of the same class as W43's
  adjudicated P4 gloss case (separator carried to the next line; segment complete) — non-defect;
  P8 `—` lines are dialogue lines and the registered `— 第 N 版 —` separators.
- The orphan-harness re-render reproduced all 8 delivery SVGs byte-identically
  (verified against `scratch/round3-sha256.txt`), so no new round was required.

## Gate 7 — P7/P8 ends

- P8: see Gate 2 (cursor 2351, last-column last baseline 2335.05, overall max ink 2517.92, all < 2540).
- P7 teaser band bottom **2461.94** (< 2540).
- P7 readers box: rect y=1230.44, height 577.5, bottom 1807.94; last disclosure line baseline 1793.13,
  ink bottom **1795.13**, i.e. inside the box with **+12.81px air** (the +40 slack fix: core `lh` formula
  trailing `+26` → `+66`, following the ko-fr +40 precedent; the core formula itself undercounts
  ~26–29px and the core P7 last line spills below its box — that core defect is inherited, not fixed
  in the core). Phrases rule y=1837.94 (30px below the box bottom; 42.81px below the last ink).
- P7 phrases pitch 132 → 102 is a documented deliberate deviation (forced by the longer Traditional
  readers' box; both the row formula and the teaser formula in `content7.py`), keeping ~26px inter-row air.
  Round-1 teaser end was 2581.94 (over the 2540 gate); round-2 pitch fix brought it to 2461.94.

## Gate 8 — Readers' corner (all 5 verified on the whitespace-insensitive joined P7 text)

- Labeled editor's example present (`編輯部範例信，非真實來信。`).
- Disclosure 1 (no real reader letters yet: `未收到真實讀者來信`).
- Disclosure 2 (no best P8 writing yet: `未收到真實讀者來信與第8版優秀作文`).
- Disclosure 3 (both deferred to VOL.3: `順延至VOL.3`).
- Explicit imperative public solicitation covering **both** letters and P8 texts
  (`請把你的來信和第8版作文寄給我們！`). The solicitation was added by appending a sentence to the
  Traditional `lcn2` disclosure (ko-fr precedent of folding it into the disclosure paragraph, so no
  extra box-line count change beyond wrap); teaser lines, content previews, and other-page exercise
  prompts were **not** counted as solicitation. No invented names, letters, or quotes anywhere.

## Gate 9 — Images

Payload equality core vs edition, both calibers (base64-text SHA-256 prefix and decoded-JPEG
SHA-256 prefix), all pages identical; counts 1/1/2/1/1/0/0/0:

| Page | Base64-text prefix | Decoded-JPEG prefix | Credit line (as placed) |
|---|---|---|---|
| P1 | `535fff46b7ce` | `6f7f33ed8f40` | `사진: lumoplank — CC0 (Wikimedia Commons) · 자료 사진` |
| P2 | `e66d2b455ec6` | `96a6a19b612a` | `사진: wizdata — CC0 (Wikimedia Commons) · 자료 사진` |
| P3 (1) | `e266b6ee1a87` | `158ea3a0e81f` | `사진: Udonhan1992 — CC0 (Wikimedia Commons) · 자료 사진` (wraps to 2 lines; see Visual check) |
| P3 (2) | `5bea45d1f81e` | `214cc390ac7c` | `그림: Paul Cézanne — Public domain (Wikimedia Commons)` |
| P4 | `1a7e7d6d5ffc` | `18ad8ae06fac` | `사진: Bain News Service — Public domain (Wikimedia Commons)` |
| P5 | `6a1bab177d54` | `35e7dc69d417` | `사진: Gary Todd — CC0 (Wikimedia Commons) · 자료 사진` |
| P6/P7/P8 | — | — | no photos |

Credits are taken from the Commons API Artist field; every credited image is verified as actually
placed (payload equality + credit line on the same page). Visual check confirms all 6 images render.

## Gate 10 — Abstract

`ABSTRACT.txt` (delivery directory): Traditional Chinese, single line, no ASCII double quotes,
containing this week's real theme keywords (Ipdong week Nov 2–8 2026, last autumn foliage,
kimjang season opening, CSAT countdown, Korean-history-exam registration) plus a learner search
phrase, the publication name, Korean as target language, A2–B2 levels, and 150 exercises.
`insert.py` aborts without it; it is present.

## Gate 11 — Web PDF vs cards

8 pages each (print and web, verified via pypdf page counts). Web JPEGs vs cards resized to
1400px wide: mean absolute difference 0.85–1.2 per page, % pixels differing by >30 = 0.0% on all
8 pages. No noise/wrong pages; web PDF matches the cards page by page.

## Gate 12 — Round discipline

Full SHA-256 baselines were recorded before each fix round (`scratch/round1-sha256.txt`,
`round2-sha256.txt`, `round3-sha256.txt`); the build directory was never reset in a way that loses
a baseline (transform copies and scratch were preserved across the fresh-copy rebuilds).
Any rendering change requires a complete new proofreading round; KIT-only text changes are exempt
but still require re-verification.

## Simplified-residue gate (Traditional-independence door)

- Corrected residue set = CJK characters appearing in this edition's or W43's transform sources but
  in **no** transform destination and in **no** frozen (core-and-edition-shared) string — **170 characters**.
- Scan of round-3 shipped SVGs: **0 hits**.
- Mainland-vocabulary scan (视频, 软件, 硬件, 表情包, 老挝, 打印, 光盘, 宽带, 打车, 外卖, 质量,
  服务器, 鼠标, 文件夹, 登录, 信息, 信号): **0 hits on all pages**.
- Quote balance: 「」 balanced on every page (P1 1/1, P2 1/1, P3–P6 0/0, P7 20/20, P8 2/2);
  ASCII double quotes in text nodes: 0 on every page.
- (An earlier residue-scan version was buggy — it counted ASCII/punctuation and Traditional-valid
  characters dropped by word changes — and was replaced by the definition above.)
- Registry identical notes (17 of 150) re-checked against the 170-character set: **0 hits**
  (notes 4, 21, 44, 63, 65, 69, 74, 75, 78, 91, 98, 105, 106, 107, 121, 128, 135 — all shared-glyph).

## Registry comparison (core vs edition, separate subprocess dumps)

- Counts 150/150; numbers 1–150 continuous; page and level identical for all 150.
- Registry keydiff: **[138, 150]** exactly — 138 genuine E re-aim (`离高考还剩 12 天。` →
  `離高考還剩 12 天。`), 150 apparatus localized (`(开放题，范文如下)` → `（開放題，範本如下）`).
  137 key identical (shared glyphs), confirming the tool keydiff [138] + apparatus.
- Notes changed 133/150; identical 17 listed above, all shared-glyph, 0 residue hits.
- Type mapping exactly the SC→TC name changes: 单选→單選 52, 词汇配对→詞彙配對 16,
  完形单选→完形單選 13, 句型转换→句型轉換 4, 判断→判斷 4, 翻译→翻譯 4, 写作→寫作 1;
  unchanged shared forms: 完成句子 48, 造句 8. Total 150.

## Element-position multisets (core → edition)

- P1 removed 5 / added 6 = badge design only (subtitle/rules/band shifts, matching W43's 5-for-6 pattern).
- P2 0/0; P5 0/0; P6 0/0; P8 0/0.
- P3 removed 15 / added 16 = P3 caption wrap split (+1 line, downstream col-3 texts shifted +20.15px)
  plus gloss wrap shifts.
- P4 removed 5 / added 6 = one gloss box wrapping to 3 lines instead of 2 (same class as W43's P4
  gloss case: box self-sizes, audit 0 flags).
- P7 removed 19 / added 20 = pitch change + readers-box growth.
- Fonts in shipped SVGs: only `Noto Sans CJK TC`, `Noto Serif CJK TC`, and (P1 only) `UnifrakturMaguntia`.

## Visual check (builder, all 8 cards, 2026-10-28)

- P1: badge (brick, centered, y=394), subtitle, dark band, footer, page line, gloss boxes, autumn
  photo + lumoplank credit — clean.
- P2: D-day boxes, Traditional notes, ssam photo + wizdata credit (honestly captioned as ssam,
  not kimjang) — clean.
- P3: Bukhansan photo + Udonhan1992 credit (caption wraps to 2 lines, `... · 자료` + `사진`,
  no overlap, downstream text shifted cleanly); Cézanne apples image + credit — clean.
- P4: title fragment `소식` on its own line (frozen title wrap, legitimate); ladder diagram labels
  clean; Bain photo + credit — clean.
- P5: study photo + Gary Todd credit; gloss continuation `· 합격 合格。` visible (adjudicated, see Gate 6) — clean.
- P6: comparison table labels fully visible (구분 / 이번 주 / 시험 날 rows), no grazed labels — clean.
- P7: readers box fully contains its last line with air before the phrases rule; golden sentences
  with page tags; teaser band — clean.
- P8: keys flow fills 3 columns, ends well above the footer; separators `— 第 N 版 —`;
  150 apparatus line `✓ 範本見本版 H 區（157 字）`; H model paragraph — clean.
- No missing glyphs (tofu), no overlaps, no cut text on any page.

## Rounds log

- **Round 1** (rendered 04:31 UTC file times): registry correct (150; levels/pages/types as above;
  model 157 chars; no FLOW OVERFLOW / HEAD TOO WIDE warnings), but P7 teaser end was **2581.94**,
  over the 2540 gate, because the longer Traditional readers' box pushed the phrases section down.
  Round-1 full SHA-256 baseline (SVG/card/PDF) saved to `scratch/round1-sha256.txt`.
  Round-1 PDFs: print 33,167,430 bytes, web 3,373,563 bytes.
  (Note: `run.py` was accidentally executed twice in round 1 — same inputs, same outputs, harmless.)
- **Round 2** (rendered 04:33 UTC): fix, following the ko-fr precedent: P7 phrases pitch 132 → 102
  (both the row formula and the teaser formula in `content7.py`), keeping ~26px inter-row air.
  Result: P7 teaser end **2461.94** (< 2540); P7 col3 ends 1807.94. Round-2 diff vs round 1 was
  exactly scoped: only P7 SVG + P7 card + both PDFs changed.
  Round-2 PDFs: print 33,167,434 bytes, web 3,376,241 bytes; baseline saved to `scratch/round2-sha256.txt`.
- **Round 3** (rendered 04:42 UTC): fix for the one real Simplified residue found by audit:
  `考试日就是D-day` → `考試日就是D-day`. It occurred only once in the core sources
  (`content56.py:196`, a P6 exercise note); because `ex()` prints the body but not the note on
  exercise pages, the P6 SVG was unchanged and only the P8 SVG/card (line 86 note) plus both PDFs
  changed round 2 → round 3, exactly as expected.
  Round-3 PDFs: print **33,167,237 bytes**, web **3,376,265 bytes**; baseline saved to
  `scratch/round3-sha256.txt`. Transform copies preserved as `scratch/transform-round2.py` and
  `scratch/transform-round3.py`.
- Post-round-3 verification (orphan harness re-render, geometry supplement, registry comparison,
  visual check, ABSTRACT/KIT writing) changed no rendered file: delivery SVGs re-verified
  byte-identical to round 3 after the orphan re-render.

## Deliberate deviations from W43 ko-zh-tw

- VOL.2 (W43 was VOL.1) and the W45 theme (Ipdong week, foliage, kimjang, CSAT countdown) — issue content.
- P7 phrases pitch 132 → 102 (forced by the longer Traditional readers' box).
- P7 readers-box slack +40 (ko-fr precedent; W43 did not need it for its shorter box).
- P8 head form carried from W43 (`답 · 全部答案與簡析（第 1–8 版）`, `— 第 N 版 —` separators).
- `準季後賽` / `漢拏山` usage decisions (see Language-layer method).
- Solicitation sentence added per Gate 8 (folded into the `lcn2` disclosure paragraph).

## Toolchain

- `run.py` interpreter: `tools/venv/bin/python`, Python 3.12.3, PIL 13.0.0.
- `render.py` interpreter: `tools/venv/bin/python`, Python 3.12.3, PIL 13.0.0, cairosvg 2.9.1.
  (System python3 is 3.12.3 with PIL 10.2.0 and has no cairosvg; it was **not** used for rendering.)
- The venv baseline proof (8/8 core reproduction) validates this choice, but the coordinator's
  toolchain decision is pending — recorded here for that decision.
- Tool versions: `tools/p8.py` SHA-256
  `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9` (current new version);
  `tools/occlusion_audit.py` SHA-256
  `e1f92b42eb8996fe04c5ffb60c4ec23e1911239a5f94b76808f01ed9414addf2`;
  `tools/freeze.py` SHA-256
  `d9adfa486a788e57e15805d383f5691094067d26f1884c127dea4d1a1e587d54`.
- Run logs: round-3 single-process run captured in `scratch/run-round3.log` (TOTAL 150;
  no FLOW OVERFLOW / HEAD TOO WIDE warnings; P7 col3 ends 1807.94; P7 teaser ends 2461.94;
  P8-ex flow ended col 3/3 y=403; model chars 157).

## Observations for the independent proofreader

- Core P7 readers-box formula undercounts ~26–29px (core P7 last line spills below its box);
  this edition uses the +40 slack workaround — do not "fix" it back to the core formula.
- P3 caption split (`... · 자료` + `사진`) is a TC-face Latin-metrics reflow of the identical caption
  text, not a content change; visually confirmed clean.
- P4 gloss 3-line box and P5 `· 합격` gloss continuation are the same wrap class as W43's P4 gloss case.
- The 137 shared-glyph note: key `11月7日是立冬。` is identical in both scripts; only its note was
  Traditionalized. Do not re-open [137,138] as a pair.
- The corrected residue-scan definition (170 characters, destination/frozen-excluded) supersedes
  the earlier buggy version; the 0-hit result stands under the corrected definition.

## Inherited core fact debts (inherited, NOT re-adjudicated, NOT blockers for this edition)

- Korean Series Nov 2 start may shift after rain delay (issue uses `발표된` wording + press-time note).
- Playoff G1 (Oct 26) result was unknown at cutoff; no score printed.
- Champi record-breaking claim was deleted.
- Ipdong Nov 7 / Sosol Nov 22 come from a calendar blog (KASI official page not retrieved).
- Korean-history-exam details are secondhand.
- Commons shortfall: no verified PD/CC0 Korean foliage / kimjang / Korean-student-studying photo;
  ssam photo is honestly captioned as ssam, not kimjang.

## Round 4 verification (recovery check, 2026-10-28; no re-render, no fix round)

A second, independent verification pass re-ran every canonical gate fresh on the
quiescent round-3 disk (no delivery file changed; SVG/card/PDF SHA-256 re-verified
identical to `scratch/round3-sha256.txt` afterwards). Results, all agreeing with
the gates above unless noted:

- `tools/occlusion_audit.py` (edition + `--core`): edition 0 flags, core 0 flags,
  NEW 0 flags; self-test OK.
- `tools/freeze.py diff`: per-page CJK totals as in Gate 1; total added CJK 949
  (see corrected figure above). Independent Hangul-run multiset diff: the ONLY
  core-vs-edition Hangul differences on all 8 pages are the furniture runs
  제/면/총 (core page line `제 N 면 / 총 8 면` and P8 `— 제N면 —` separators →
  edition `第 N 版 / 共 8 版` / `— 第 N 版 —`); added Hangul runs: none on any page.
- `tools/p8.py compare` with explicit dual paths, `--total 150`: CLEAN, keydiff
  [138] only (adjudication as in Gate 2).
- Supplementary geometry re-run (`scratch/audit_geom.py`, baseline-anchored ink):
  ADVANCE worst 1885.0, 0 flags all pages; same-baseline 0 pairs; footer 0 flags;
  P6 label coverage worst 0.0% (gate <30%); P7 readers air +12.81px, phrases rule
  1837.94, teaser bottom 2461.94; P8 flow cursor 2351, last-column baseline
  2335.05 / ink 2338.05, overall max baseline 2514.92 / ink 2517.92 (audit_extra's
  4× method reads the same max line at 2533.92 — both < 2540); web-vs-cards
  mean 0.85–1.2, % pixels >30 = 0.0% on all 8 pages; image payloads equal.
  NOTE: a concurrent 04:47 run of the same supplement (racing the orphan-harness
  re-render) reported phantom values (P7 air −11.19, P6 coverage 54.55%); those
  numbers are superseded — the quiescent re-run and the canonical 0-flag audit
  agree, and the P7 card visually confirms the last line inside its box.
- Traditional-independence re-screen (independent of the build's transform map):
  edition Han set 439 chars; W43 ko-zh-tw Han set 454; edition-only 146 chars,
  each adjudicated a Traditional or shared form (theme words such as 颱, 蘿, 蠶,
  鹽, 醃, 廳, 嶽); OpenCC s2t over all edition visible text changes exactly one
  pair, 峰→峯 ×10 (shared char, Taiwan-common 高峰 — not Simplified residue), so
  Simplified residue = 0; mainland marker words (信息, 视频, 软件, 网络, 质量,
  水平, 出租车, 土豆, etc.): 0 hits. 「」 balanced every page.
- Orphan read-only window scan (dy 10–45) over shipped SVGs: 0 flags (matches the
  harness's win_flags = [] and ko_splits = 0 at tail ≥3 syllables).
- Render provenance: re-rendering all 8 cards from the shipped SVGs with
  `tools/venv/bin/python` reproduces the delivered cards byte-identically (8/8);
  system python3 has no cairosvg, so the delivered render could only be venv-built.
- Core integrity: core SVG SHA-256 values match the pins recorded in the W45
  ko-pt KIT (p1 `f1e6913d…`, p2 `839dcdd0…`, p3 `74371179…`, p5 `68e6ead9…`);
  the core was never written by this recovery (read-only throughout).
- Concurrent-write note: this KIT and `ABSTRACT.txt` were written to the delivery
  directory at 04:52–04:53 UTC during the recovery pass by a parallel worker;
  this pass verified them against its own independent measurements instead of
  overwriting them, correcting only the freeze total above (948 → 949) and
  appending this section. No Discord post, no repo insert, no main-chat card/PDF,
  no cron was created by this pass; insertion remains the coordinator's serial step.
