# WEEKLY-KIT — W45 FR × JA (target: French, reader native: Japanese)

**Status: builder-complete — NOT finalized.** Finalization is the independent
proofreader's decision. This KIT records only measured values from the build.

## Delivery contents

| File | Value |
|---|---|
| `svg/` × 8 | hashes below (round7 baseline) |
| `cards/` × 8 (1950×2700 PNG) | hashes below |
| `Le-Lucerna-VOL3-JA.pdf` (print, 8 pp, 1462.5×2025 pts) | 24,422,314 bytes, sha256 `6d5aa28dadd8c19846872c579b1542a1e73f57bcd3e04f2ae53717862f5d5f89` |
| `Le-Lucerna-VOL3-JA-web.pdf` (web, 8 pp, 936×1296 pts) | 5,199,959 bytes, sha256 `46a1e7af60d62f63d54cd2d5e10f3804084e2525894e3e6e7741784fb1d52235` |
| `ABSTRACT.txt` | Japanese one-liner, no ASCII double quotes |
| `WEEKLY-KIT.md` | this file |

### SVG hashes (final, `round7.sha`)

| Page | sha256 |
|---|---|
| p1-une | `658e3b408c3e64a90a67bd0fc3b6dd7fd959b5fa541e86e79f3dcad27a095af3` |
| p2-vie | `812e77447b07beee96f26a54c3c9f8557e384306ca574c5abdbe7444fab4963d` |
| p3-culture | `6f4ba510b1da208c8cd4c299616e8e761f89f3761ada63b758bf18e70d315ba6` |
| p4-sport | `f70d79eaf587f943cceb258e0ff311a2d6ed7a2db4cec4b021f45b037b30185a` |
| p5-jeunesse | `38f8a8debd5e073eb3993f3bf5f2d9eab84db1277e055dc016bfd88068093a62` |
| p6-politique | `bf24b0bebbd9151379e956d130e35251b4cd8a82bca991aedef574a8fb106232` |
| p7-langue | `b7c9dd53cd9cea4e24de5571ef46a44654775fb7a678c7a721d3fa503a3c6b07` |
| p8-exercices | `5b76e718f8e456a111d76e3c91538c00e4a05cd031df7b19ebb271e572befb9f` |

### Card hashes (final, 1950×2700 PNG)

| Card | sha256 |
|---|---|
| p1-une.png | `5ae912a337941229bec43879d18ac85fee7bda69c0be286a7391f3313e73e923` |
| p2-vie.png | `188037a02c8a8d786bc18f21f89a7758f38209fec5308a6523276c3c9af8beab` |
| p3-culture.png | `227ae538c3ba7954e69485b9a11005d70199df67254a3431b01622044a4d7a8c` |
| p4-sport.png | `e8c5de88292c21c04c64e9089beafbcff25f45853c86705df832e99a33894b15` |
| p5-jeunesse.png | `065a30d62301034b91ca9805309bb00203a8b442f5d2429f34a4cc235d308422` |
| p6-politique.png | `b74e21d5a9e21a159d37627b71b29ea33113f8c97353f578ca180ce2f223b3d3` |
| p7-langue.png | `b2713c4c29adda0011080a13ee4af06d34cb18e3f11e61fc5b66a220d8a05359` |
| p8-exercices.png | `c35e8a35faf86d48a6054fc37ee6fc8232e03d40376af55217024d1b874cb37d` |

## Source and toolchain

- **Frozen source:** W45 FR core VOL.3 (`files/weekly-report-w45-fr-core/`):
  150 exercises; per-page 10/15/18/18/17/18/12/42; levels A2 53 / B1 75 /
  B2 22; model essay 86 words; gloss 38 = 7/6/6/7/6/6; golden-sentence
  joint counts #1=5 #2=3 #3=1 #4=5 #5=1 #6=3 #7=1 #8=3; P8 prints 97
  noted answers + 53 bare keys by design.
- **Build driver:** `hidden_files/weekly-report-w45-fr-ja-build/transform.py`
  (single source for ALL fixes) + `render.py` (one-process driver, cards,
  dual PDFs). No script that writes SVGs into the delivery directory was
  ever run in place; comparisons used a copied tree with OUT redirected.
- **Toolchain (both driver and render):** `tools/venv/bin/python`,
  Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1, pypdf 6.21.2.
  System python3 is also 3.12.3 but Pillow 10.2.0 without cairosvg, so it
  cannot run render.
- **svglib swap (round 1, md5-asserted):** core svglib
  `0703a8814abe388f131c89f3d7ffb946` → JA core svglib
  `d73e23b365676c3618d7e060b835eb4d` (differs only in JP face selection
  2 spots + kinsoku oidashi + `SEAM_SLACK = 28`).
- **Freeze baseline:** `tools/freeze.py baseline` reproduced the core 8/8
  byte-identically before transforming; core pre-build hashes in
  `core-prebuild.sha`; final re-check: core SVGs 8/8 unchanged.

## Build rounds (each gated by TRANSFORM_ROUND; baseline saved first)

| Round | Change | SVG pages changed |
|---|---|---|
| 1 | Chinese → Japanese explanation layer; svglib swap; OUT redirect; footer/page-line/gloss-prefix furniture; explicit `PRINT_NOTES` (97) block | all 8 (first build) |
| 2 | Occlusion fixes (6 NEW flags): P1 agenda note shortened; P2 ET VOUS prompt shortened; P5 Creator Week box title → bare `PARIS CREATOR WEEK`; P8 E-group stems → `和訳：` / `仏訳：` | P1, P2, P5, P8 |
| 3 | Line-start small-kana fix: P7 clinic bridge → `各文に誤りが1つ。見つけて直しましょう。` | P7 |
| 4 | Word-split + orphan-tail fixes: P4 comparative bridge (drop `文を`); P7 grammar bridges #4/#8 shortened to single lines | P4, P7 |
| 5 | P8 #107 note (correct file `content7.py`): `接続法：il examine、s はつけない` → `接続法：examine、s はつけない` | P8 |
| 6 | Zero-doubt wording: P2 date-head `注意：` → `注：` | P2 |
| 7 | Zero-doubt wording: P3 DATES box `注意：` → `注：` | P3 |

Baseline files: `round1.sha`–`round7.sha`, `occlusion.json`,
`occlusion2.json`–`occlusion7.json`, `checks-round2.txt`–`checks-round5.txt`,
`freeze-diff.json`, `keycompare.json`, `core-prebuild.sha`
(all under `hidden_files/weekly-report-w45-fr-ja-build/`).

**Round-4 note (found by the reproducibility pass):** an earlier draft of
round 4 applied the #107 fix to `content8.py` by mistake and aborted after
the P4/P7 applies; the real #107 fix is round 5 in `content7.py`. The
mis-attributed block was removed from round 4, after which rounds 1–7 run
clean from a fresh core copy (see Reproducibility below). Delivery files
were unaffected — they already carried the correct round-5 fix.

## Gates (all measured, not claimed)

### Geometry

- **Canonical occlusion audit** (`tools/occlusion_audit.py`, selftest passing
  each run): **0 flags, NEW vs core = 0** (round 2 through round 7,
  `occlusion2.json`–`occlusion7.json`).
- **Same-baseline rowcheck:** all 8 footers min gap 966.0 px; P1 top band
  min gap 112.0 px; no collisions.
- **Full-page right-edge scan:** only the P8 F-group 3 lines exceed 1885
  (ink rights 1892.0 / 1891.0 / 1900.0), byte-identical to the core at the
  same positions — inherited core geometry inside the 1922 page frame,
  not an edition defect; canonical audit 0 flags.
- **P6 chart-label coverage (baseline-anchored method):** 0% — no
  later-drawn rect overlaps any P6 chart text ink box (36 chart texts
  checked, edition and core both 0). The P6 chart here is text rows, not
  bars; the FR×EN precedent measured 0.0% on the same chart.
- **Orphan scan** (column x in {65, 527, 989, 1451}, consecutive baselines
  ≤ 60 px apart, runs ≥ 2 lines, final-line ink width in [10, 45) px):
  only P2 `___` finals (2, y=2170.6 and y=2488.8, x=527) and P3 `7).`
  (1, y=2405.3, x=1451). Both inherited: the P2 blanks also occur in the
  core (y=2140.9 and y=2459.1, same x, shifted only because Japanese
  bridges/heads moved the flow); the P3 `7).` is identical in core and
  edition (same y and x). P7 orphan candidates are 0 after round 4.
- **Line-start scan** (kinsoku NO_START set + small kana
  `ゃゅょぁぃぅぇぉっゎ`): **0 violations** after round 3.
- **Latin-token split detector** (1680-word vocabulary from edition
  sources; a split fires only when line-final fragment + next-line-initial
  fragment forms a vocabulary word while neither alone is one):
  edition 0 splits, core 0 splits, after round 5 (it had caught exactly
  the P4 `moin|s` and P8 `examin|e` splits before their fixes).
- **Render warnings:** zero FLOW OVERFLOW / HEAD TOO WIDE warnings;
  150 exercises in one process. Flow ends P1-hiver 2298 and P6-ex 2557
  are identical to core values and stay clear of the footer rule at 2580
  (23 px clearance on P6-ex).

### French freeze (target text byte-identical)

- P4: `41e édition en 2026 (40e anniversaire)` — 41e is the edition
  number, 40e the anniversary number; total `40e` occurrences in the
  whole edition = 1; `54e` = 0.
- Q120 stem `Si j'étais libre dimanche, j'___ à Nanterre.`, options
  A. `irai` / B. `irais` / C. `vais`, key B, P8 note synchronized
  (si + imparfait → conditionnel + j' elision); Q119/Q121 untouched.
- P7 quotation #4 keeps the P4 debate box verbatim comparatif
  `plus excitante ou plus frustrante?`.
- #8 uses the P5 verbatim `Les jeunes créateurs y rencontrent leur
  public, en vrai.` + Q106 rewrite (error `rencontre`, key `rencontrent`).
- P6 synchronized to `Ce calendrier peut encore bouger.` (the P6
  deep-read lowercase form and the micro-drill key `peut` are not
  quotations and stay unchanged).
- P7 French definition sentences, example sentences, and toolbox French
  sentences are frozen — only explanation lines are localized.
- **Freeze diff** (`freeze-diff.json`, core vs edition SVG text
  multisets): per-page added/removed strings P1 +23/−23, P2 +37/−34,
  P3 +36/−33, P4 +40/−37, P5 +32/−29, P6 +29/−27, P7 +41/−35,
  P8 +123/−119; CJK counts core→edition P1 202→262, P2 244→344,
  P3 179→279, P4 197→311, P5 177→273, P6 198→300, P7 390→513,
  P8 1030→1193; total added CJK characters 2776.
  Pure-Latin added/removed strings are **0 except adjudicated items**:
  P1/P2/P6 0/0; P3 +1/−1, P4 +1/−0, P5 +2/−0, P7 +0/−1 are wrap
  fragments of mixed French+Japanese lines (same French tokens, different
  wrap points, e.g. `Vrai / Faux`, `finale / quarts / …`); P8 14/14 are
  keys-flow reflow fragments (same French keys, different wrap points
  from Japanese notes + half-width parens), plus the two documented
  redirections below. No French word or sentence was added or removed.

### P8

- Plain `tools/p8.py` with explicit dual paths + `--total 150`:
  **CLEAN, core noted 97 = edition noted 97, missing = [], extra = 0,
  keydiff = [135, 150]** (the `--target` form and the default total 149
  were not used).
- Full-150 key comparison (`hidden_files/w45/p8-fr-gap-fix/keycompare.py`):
  mismatches exactly 2, [135, 150], both noted; **bare-key mismatch = 0**.
- **Redirections (both printed and recorded):**
  - 135: key changed from the Chinese sentence to
    `日程表を読むことは、それ自体がフランスを理解することです。`;
    stem is `和訳：« Lire un programme, c'est déjà comprendre la France. »`.
  - 150: key changed from the Chinese apparatus text to
    `自由記述 — ポイントは作文欄に、範文はこのページの作文欄の中にあります`
    with note `ポイントで採点`.
  - 136–139 keys are unchanged French sentences; their stems are the
    Japanese source sentences with `仏訳：` prefixes (136
    `彼は兄より速く走ります。`, 137 `生徒たちは10月17日から休みです。`,
    138 `今夜、私たちはかばんを準備します。`, 139
    `決勝進出者はまだ誰も知らない。`).
- `content8.py` carries an explicit `PRINT_NOTES` set equal to the core's
  noted set (97 items, measured with `tools/p8.py extract --total 150`);
  P8 notes print as half-width ` (note)` form and separators as
  `— N ページ —`, following the W43 FR×JA shipped form.
- Registry type names (Chinese internal metadata, never printed) are
  intentionally kept per the W43 precedent. The forbidden bridging term
  occurs **0 times** in delivery files, build `*.py`, `ABSTRACT.txt`,
  and this KIT.
- E-group translation stems use the compact `和訳：` / `仏訳：` prefixes
  (instead of the W43 full `日本語に訳しなさい` /
  `フランス語に訳しなさい` forms) because the full forms wrapped to 2
  lines each and pushed the P8 battery across the writing-strip rule;
  instruction meaning is unchanged and keys are unaffected.

### Explanation layer: Japanese purity (word-level review)

- Residual marker scan over edition SVG text: all Chinese markers
  (决赛, 扇贝, 夜场, 词表, 简体, 读者园地, etc.) = 0; `注意：` = 0 after
  rounds 6–7 (both occurrences switched to the unambiguous `注：`).
- Shared-kanji word `文化` occurs 2 times in edition SVG text, both
  standard Japanese: P3 band title `CULTURE · 文化` and P8 key note 79
  `火曜3日：文化とメディア`.
- Gloss count (split on `·` per README #21, from the `gloss()` call
  strings): P1 7, P2 6, P3 6, P4 7, P5 6, P6 6, total 38 = core 38.

### Readers' corner (zero fabrication, P7)

- Labeled editorial example (French frozen text) with the explicit label
  `(ce texte n'est pas une lettre de lecteur)`.
- Three-fact disclosure (Japanese): no real letters received, no VOL.2
  P8 best essay received, both deferred to VOL.4 — the FR core's W44
  issue did not appear. Japanese text:
  `編集部より：印刷時点で手紙も VOL.2 の作文投稿も届かず（W44号は未発行）、今号は例文を明記して掲載。VOL.4で実際の投稿を講評します。`
  corroborated by the frozen French note:
  `Note de la rédaction: aucun texte du VOL.2 n'était arrivé au moment
  de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4
  reprendra la promesse.`
- Explicit imperative solicitation (final sentence of the Japanese
  comment paragraph, literally covering both letters and best P8 texts):
  `手紙も、今号の作文の力作も、VOL.4へ送ってください！`
  (The VOL.4 preview paragraph is separate and is not counted as the
  solicitation.)

### Furniture — W43 same-pair three-way comparison

| Item | W43 FR×JA measured | W45 FR core measured | W45 FR×JA (this edition) |
|---|---|---|---|
| P1 pairing badge | y=574, x=975, 22 pt BRICK, fill #a4553a, `フランス語テキスト · 日本語の解説 — 日本語読者のための版` | y=574, x=975, 22 pt BRICK, fill #a4553a, `法语正文 · 简体中文讲解 — 给简体中文读者的版本` | **identical geometry** to both; W43 Japanese string |
| Masthead article | Le | Le | Le |
| Footer (left) | `Le Lucerna · フランス語週刊 VOL.2 · 本文はフランス語 · 解説は日本語` | `Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文` | `Le Lucerna · フランス語週刊 VOL.3 · 本文はフランス語 · 解説は日本語` |
| Page line | `N ページ（全 8 ページ）` | `第 N 版 / 共 8 版` | `N ページ（全 8 ページ）` |
| Gloss prefix | `解説 — ` | `译注｜` | `解説 — ` |
| P8 header | `RÉPONSES · 全解答と解説（1–8ページ）` | (Chinese form) | `RÉPONSES · 全解答と解説（1–8ページ）` |
| P8 band | `EXERCICES & RÉPONSES · 練習と答え`, subline `総合テスト ÉVALUATION · 答えはこのページの下にあります` | (Chinese form) | same as W43 FR×JA |
| P8 section heads | A `穴埋め`, B `選択問題`, C `読解`, D `文の完成と変換`, E `翻訳`, F `語の対応`, G `会話の穴埋め`, H `作文` | (Chinese form) | same as W43 FR×JA |
| `MODÈLE` | `MODÈLE · 範文` | (Chinese form) | `MODÈLE · 範文` |
| Instruction forms | 空所補充 / 書きかえ / 誤り直し / 組み合わせ / 語と意味を結ぶ; core French `Vrai ou faux?` kept in French | — | same as W43 FR×JA |

Badge rule note: README #20's FR-as-target general form (y=574, 22 pt
BRICK, inserted) is only a reference; the W43 same-pair measurement
above governs, and this edition matches it exactly.

### Images (core 3 public-domain images only)

| Page | Payload vs core | Credit line (frozen core text, verified placed) |
|---|---|---|
| P1 | base64 sha prefix `ff20bc2bd2654cdc` / decoded-JPEG sha prefix `f3705af28f175ce4` / 334,674 bytes — identical to core | `Eugène Atget (1857-1927), photographie, domaine public` |
| P2 | base64 `6918cb8bbe4b4bec` / JPEG `5b772facb5db886c` / 646,242 bytes — identical to core | `Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA` |
| P3 | base64 `bfaadf5b6b912416` / JPEG `be071fdae81a71b4` / 142,340 bytes — identical to core | `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public` |

Each page embeds exactly 1 JPEG; decoded byte sizes match the core exactly.

### Web PDF verification (from this edition's own cards, fresh)

- 8 pages; `pdftoppm -r 150` renders vs delivered cards (1950×2700):
  mean abs diff per page 6.350 / 6.288 / 5.802 / 6.355 / 5.210 / 5.483 /
  6.518 / 9.306 — paper-toned, clean values; **no noise pages**.
- Extracted JPEG streams (`pdfimages -j`) byte-match Pillow q75
  (no-optimize) encodings of the delivered cards on all 8 pages;
  q72 encodings do **not** match. Conclusion: **q75 measured, q72
  excluded** (Pillow default quality = q75 without optimize).
- The FR core web PDF noise problem is the parent's separate matter and
  is unrelated to this edition.

### Visual check

All 8 cards inspected whole-page (P1–P8, plus P3 re-checked after round
7): no overflow, no overlap, no footer intrusion, images and credit
lines placed correctly. The only visual notes are the adjudicated
inherited shapes listed above (P8 F-group right edge, P2 `___` finals,
P3 `7).` final).

## Reproducibility (ko-ru B-1 lesson, required)

Procedure: copy the W45 FR core build to a scratch repro directory, copy
`transform.py` with only its OUT replacement target changed from
`weekly-report-w45-fr-ja` to `weekly-report-w45-fr-ja-repro`, copy
`render.py` with only its BASE changed to the repro directory, run
`TRANSFORM_ROUND=1` through `=7` in order plus the render, then compare
all 8 SVG hashes and 8 card hashes against `round7.sha` and the card
hashes above.

**Result: PASS.** All 7 rounds exit 0 (after the round-4 correction
noted above); repro SVG 8/8 byte-identical and repro cards 8/8
byte-identical to the delivered files. The repro delivery directory was
removed after verification so it cannot be mistaken for an edition.

Reproduction procedure for the coordinator: same steps against the
shipped `transform.py` + `render.py` in
`hidden_files/weekly-report-w45-fr-ja-build/`.

## Integrity

- Core SVGs re-hashed against `core-prebuild.sha` after all rounds:
  **8/8 unchanged**.
- No other edition, `weekly-git`, or `tools/` file was touched by this
  build. The only directories written are this edition's build directory,
  its delivery directory, and its own scratch (including the removed
  repro directory).

## Open observations for the independent proofreader (not blocking)

- P8 F-group 3 lines have ink rights 1892.0/1891.0/1900.0, past the
  nominal column edge 1885 but inside the 1922 page frame,
  byte-identical to the core — inherited geometry; changing it would
  require touching frozen French text.
- P1-hiver flow end 2298 and P6-ex flow end 2557 exceed their nominal
  bottoms but stay clear of the footer rule at 2580 (23 px clearance on
  P6-ex); both are identical to core values.
- E-group translation stems use the compact `和訳：` / `仏訳：` prefixes
  (see P8 section) — instruction meaning unchanged, keys unaffected.
- The P7 grammar #8 line uses `y＝場所` (shortened from
  `y は場所を指す`) and #4 uses `ou の対比` (shortened from
  `ou による対比`) to keep each bridge on one line and avoid stranded
  single-kanji final lines; meaning is preserved.
- The P7 grammar bridges and clinic bridge were shortened for line
  geometry only; all French sentences in those blocks are frozen core
  text.
