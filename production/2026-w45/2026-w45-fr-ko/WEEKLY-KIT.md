# WEEKLY-KIT — W45 FR×KO (Le Lucerna VOL.3)

**Status: builder-complete — NOT finalized.** Finalization belongs to
independent proofreading. This edition was built by the FR×KO builder
2026-10-28; it is delivered to the coordinator only (no staging, no
Discord, no main-chat cards/PDFs by the builder).

- Target language: French. Reader native language: Korean.
- Issue week: Mon 2 – Sun 8 Nov 2026. Masthead: Le Lucerna (French article).
- Pairing badge + per-page footer pairing note on all 8 pages.
- 150 exercises; per-page 10/15/18/18/17/18/12/42 (P1–P8);
  levels A2 53 / B1 75 / B2 22; P8 model essay 86 words.
- The forbidden bridge term appears nowhere in the delivered paper or the
  build code (explanation function is `expl()`, prefix `해설 — `).

## Deliverables (this directory)

- `svg/` ×8: p1-une, p2-vie, p3-culture, p4-sport, p5-jeunesse,
  p6-politique, p7-langue, p8-exercices.
- `cards/` ×8 PNG, 1950×2700, rendered from the delivered SVGs (cairosvg).
- Print PDF `Le-Lucerna-VOL3-KO.pdf`: 15,453,079 bytes,
  sha256 `994fff4df860893094a6e83b6acfb800b355fdf9d8633f595120c10c93514e26`.
- Web PDF `Le-Lucerna-VOL3-KO-web.pdf`: 5,098,770 bytes,
  sha256 `6aca62a37060a7c21b8573c953e9592203a95df03f154e91c48dbf5da451881c`.
  Freshly generated from the delivered cards in the final render
  (NOT reused from the FR core); verified page by page (§Web PDF).
- `WEEKLY-KIT.md` (this file), `ABSTRACT.txt`.

## Toolchain (measured)

- transform.py + render.py both run under `tools/venv/bin/python`:
  Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1.
- No separate run.py step exists in this build: SVG generation is
  render.py's single-process import of content12/34/56/7/8
  (REG accumulates 1..150 once), per README #7. System python3 is also
  3.12.3 but lacks cairosvg and was never used for rendering.
- transform.py is the single source of all fixes: the delivered paper
  must be reproducible from a fresh core copy + transform.py alone.
  Pair counts asserted every run (bslib4 3, content12 57, content34 81,
  content56 68, content7 30, content8 59 = 298).

## Round history + baseline files

Build tree: `hidden_files/weekly-report-w45-fr-ko-build/`
(transform.py, render.py, checks.py, build logs, scratch/).

- `core-prebuild.sha`: core SVG sha256 before any transform (core untouched;
  identical to the FR×JA build's recorded core hashes).
- Round 1: rename + full translation. Transform exit 0 first try (298 pairs,
  Han gate clean). Render: 150 exercises, zero FLOW OVERFLOW / HEAD TOO WIDE.
- Round 2: P5 creator title → bare form, P6 quote reword, P5/P6 gloss
  shortenings, P2 expl reword, P3 gloss comma fix, P7 disclosure reword,
  content8 E-prompt shortenings + P1 #4 note shortening. The run FAILED on
  its last content8 pair (the P1 #4 note lives in content12, not content8),
  so content8.py was left unwritten while the other round-2 files were
  already saved. A render then ran anyway because the pipeline
  `transform | tail && render` masked the nonzero exit with tail's exit
  code — that mixed-state render was superseded, never delivered.
  Lesson: run transform and render as separate steps, check transform's
  exit code directly.
- Round 3: exactly the remainder (five content8 E-prompt pairs + the
  content12 note pair). Transform exit 0, render exit 0, zero warnings.
  P8 battery 1526 → 1439 (−87px, 3 saved lines).
- `pre-fix-round2.sha` (18 lines = 8 SVG + 8 cards + 2 PDFs, round-1 state):
  change-scope check vs round-3 output = EXACTLY as predicted: P1/P4
  SVG+cards unchanged (OK), P2/P3/P5/P6/P7/P8 changed, both PDFs changed.
- Round 4: one pair — #137 prompt `방학 중이에요` → `방학이에요`
  (fixes a lone 1-character `요.` final line; measured 1-line fit with
  wrap() before applying). First attempt failed on a rep() assertion:
  the round-4 old string carried a 1-codepoint typo, `17읽부터`
  (U+B144 읽, “to read”) for `17일부터` (U+C77C 일, “day”) — the
  assertion gate caught it before anything was written; fixed by a
  codepoint-exact replacement confined to the section(4) block, then
  re-ran clean (transform exit 0, FINAL HAN GATE OK, render exit 0).
  P8 battery 1439 → 1410 (−29px, 1 saved line, as predicted).
- `final-round4.sha` (18 lines): snapshot of the delivered state;
  re-checked after all verification — all 18 match (render deterministic,
  files stable).
- Round-4 scope by construction: only content8.py changed (1 pair), so
  only the P8 SVG/card + both PDFs differ from round 3; P1–P7 inputs
  unchanged. (No separate round-3 hash file was saved; the scope claim
  rests on the single-pair transform log, not a hash diff.)

## Gates (all measured on the final round-4 output)

### Geometry

- Canonical `tools/occlusion_audit.py` (selftest passed): edition 0 flags,
  core 0 flags, NEW vs core = 0.
- checks.py: rowcheck 0; right-edge 1 (P6 TROIS DATES only, inherited —
  see Adjudications); frame 1 (same node); P6 chart-label rect overlap 0
  with the baseline-anchored true-ink method (< 30% gate; the first ink-box
  implementation omitted PIL's ascender offset and false-flagged — fixed
  to the canonical `y - ascent + t/b` anchoring from occlusion_audit.py);
  kinsoku 4 (French inherited closers only); Han ideograph nodes 0 on all
  8 pages; frozen counts = core; orphan SPLIT≥3 = 0 and LONE-FRAG = 0
  (only the 4 inherited French START-CLOSERs remain);
  gloss 38 = 7/6/6/7/6/6 (core 38).
- Flow ends (final render): P1-headline 1588 (< 1812), P1-hiver 2298
  (= core), P1-quiz 2521 (< 2540), P2-ex 2365, P3-main 677, P4-main 1139,
  P4-micro 2154, P5-main 2502 (< 2540), P6-deep 989, P6-ex 2557 (= core),
  P6-opinion 1225, P6-micro 1990, P7-A2 954, P7-B1 1053, P7-B2 988,
  P7-outils 979, P7-phrases 1574, P7-clinic 2140, P8-battery 1410
  (< 1485 strip rule), P8-keys 2187 (< 2545). Zero warnings.
- Visual inspection of all 8 cards (1950×2700): no overlaps, no overflow,
  no footer pressure; images/credits placed; P6 chart clean; P7 reader's
  corner clean with clear gap to the VOL.4 teaser strip; P8 battery/strip
  boundary clean; P6 TROIS DATES title confirmed on-page (see Adjudications).

### Freeze (French target text)

- `tools/freeze.py diff` (core vs edition, final): +335 / −326 strings;
  added CJK chars 2795, ALL Hangul (non-Hangul CJK: none).
- French-word multiset per page, from SVG text nodes, excluding
  explanation-layer (CJK-carrying) strings: P1/P2/P3/P6/P7 NONE;
  P4/P5 diffs resolve to words moved into CJK-carrying strings
  (equal total counts on both sides); P8 diffs resolve likewise EXCEPT
  `Traduisez` (core 5× → edition 0×): all 5 are the instruction verb of
  the translation items (#135–139), replaced by Korean `한국어로:` /
  `프랑스어로:` — instruction layer, not target text; the French
  sentences themselves are preserved. `coquilles` word occurrences
  9 = 9 (string-count dip was a rewrap merge).
- Frozen-item checklist (text nodes only — raw-file grep counts base64
  image blobs and is banned for this check):
  `41e édition en 2026 (40e anniversaire)` 1×; standalone `40e` 1,
  standalone `41e` 1 (41e = edition number, 40e = anniversary number);
  Q120 stem `Si j'étais libre dimanche, j'___ à Nanterre.` 1×,
  options A. irai / B. irais / C. vais, key B, P8 note
  si + imparfait → conditionnel + j' elision; Q119/Q121 untouched;
  P7 quote #4 `plus excitante ou plus frustrante?` 5× (P4 debate-box
  verbatim comparatif); quote #8 `Les jeunes créateurs y rencontrent
  leur public, en vrai.` 3× + Q106 rewrite (error `rencontre`, key
  `rencontrent`); P6 sync `Ce calendrier peut encore bouger.` 3×
  (P6 deep-read lowercase form and micro-exercise key `peut` untouched,
  not quotes); P7 French definition sentences frozen — only explanation
  lines localized.

### P8 dual gate

- Plain `tools/p8.py compare` (explicit dual paths, `--total 150`;
  `--target` form and default total 149 both banned): CLEAN, 97 = 97,
  missing = [], extra = 0, keydiff = [135, 150].
- `hidden_files/w45/p8-fr-gap-fix/keycompare.py` full 150-key comparison:
  2 mismatches, exactly [135, 150], both noted=True; bare-key mismatches 0.
- Core noted set (from `tools/p8.py extract`, total 150): 97 items — the
  same PRINT_NOTES list as FR×EN (full list in the build log); bare = 53.
- REG dump (scratch copies only, OUT repointed, one-process import):
  150 = 150; pages 10/15/18/18/17/18/12/42; levels A2 53/B1 75/B2 22;
  key mismatches only [135, 150]; REG notes containing Han ideographs 0;
  byte-identical notes 14, all French-only language-neutral items
  (#15–18, #97, #99, #101–104, #118, #119, #137, #138: verb conjugations
  and French grammar); every printed note checked item by item, not just
  via the mapping table (JA-family lesson closed).
- Redirection table (reader-language redirection, FR-family expected
  pattern [135, 150], confirmed by measurement, not copied):
  #135 key FR→KO (`일정을 읽는 것 자체가 이미 프랑스를 이해하는 거예요.`),
  prompt `한국어로: « Lire un programme, c'est déjà comprendre la France. »`
  (2 lines, same as core); #136–139 print Korean source sentences with
  French keys unchanged (#136 `그는 형보다 더 빨리 달려요.`,
  #137 `학생들은 10월 17일부터 방학이에요.`,
  #138 `오늘 밤 책가방을 챙길 거예요.`,
  #139 `아직 결승 진출자를 몰라요.`); #150 writing guidance key →
  `열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에`,
  note `기준에 따라 채점`.
- P8 keys note #4 shortened in round 3: `2일 월요일 전역 복교`
  (fixes a keys-flow `월|요일에` split; REG note #4 confirms).

### Reader's corner (P7, zero fabrication)

- French editorial example frozen, labelled as an editorial example
  (`— Exemple de la rédaction`), not a reader letter.
- Korean comment (2 lines): `샤오모의 한마디 — passé composé가 안정적이고
  세미콜론이 좋아요. VOL.4에 여러분의 편지와 최고의 P8 작문을 보내 주세요!`
  — explicit imperative solicitation literally covering BOTH letters and
  best P8 texts (the VOL.4 teaser line is NOT counted as the solicitation).
- Korean disclosure (2 lines): `편집부 알림: 인쇄 때까지 VOL.2 편지가 오지
  않았고(W44 미발행), 최고의 P8 작문도 없어 예시를 싣습니다. VOL.4에서 실제
  편지와 작문을 다룹니다.` — all three facts: no real letters arrived,
  no VOL.2 best P8 composition, both deferred to VOL.4.
- Teaser Korean (1 line): `다음 주: 상원 사회보장 예산 심의, 11월 11일 정전
  기념일, 디에프 가리비 시장. 여러분의 편지도요!` — mirrors the core
  teaser's scope (no 14–15 dates).
- Fixed-position box constraint respected: comment ≤ 2 lines at 20pt in
  848px, disclosure ≤ 2 lines at 19.5pt in 848px, teaser strip starts
  ty7 = 2270; no spill observed.

### Images (3 public-domain images only, same as core)

Payload dual-caliber hashes, core vs edition — all byte-identical:

- P1 Atget Paris photo (Eugène Atget 1857–1927):
  b64sha256 `ff20bc2bd2654cdc075f7e09bcb5a96622650c7cb5921fe07384703067fa8e5d`,
  jpegsha256 `f3705af28f175ce48d8abad95944accb7aacc45d6a8a50c47b24af5c5144595f`,
  334,674 bytes. Credit placed:
  `Eugène Atget (1857-1927), photographie, domaine public`.
- P2 Hiroshige maple print (Utagawa Hiroshige 1797–1858, LACMA):
  b64sha256 `6918cb8bbe4b4bec2d6dd9bafb1636901ed2a46f9df8e49566749e404d1664ae`,
  jpegsha256 `5b772facb5db886c18fa96c05b9c8fb1a459eaaff931a4a8c121896edf970ee2`,
  646,242 bytes. Credit placed:
  `Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA`.
- P3 Blanco chrysanthemum plate (Flora de Filipinas, 19th century):
  b64sha256 `bfaadf5b6b912416f770c1bf579c3467e47c662efd130b5656292bb86171eca9`,
  jpegsha256 `be071fdae81a71b48d76383bd33147371968f44e37eef4312102d52dea6d0c94`,
  142,340 bytes. Credit placed:
  `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public`.
- Credit lines taken from the Commons Artist field verbatim (frozen French).

### Web PDF (fresh from this edition's cards)

- 8 pages, one 1950×2700 JPEG per page at 150 ppi (pdfimages list).
- `pdftoppm -r 150` renders vs delivered cards: same 1950×2700 size,
  mean absolute difference 4.5–8.4 per page (JPEG-artifact level);
  card means all warm ivory (~220–232) — NO noise pages (the FR-core /
  FR×EN round-5 failure mode, pages 1–7 as red/yellow/green/blue blocks,
  is absent).
- Embedded JPEG streams byte-compared against fresh Pillow encodings of
  the delivered cards: byte-identical at q75 on ALL 8 pages
  (653,212 / 639,798 / 591,990 / 642,499 / 531,188 / 563,859 / 633,988 /
  837,796 bytes); q72 encodings differ on all 8 pages.
  Measured conclusion: Pillow default = q75 (measured, not assumed).

## Furniture three-way comparison (README #20)

README #20 generic: FR/IT cores have NO free badge slot (their y=372 is
frozen body strapline) → badge is INSERTED at y=574, 22pt BRICK centered,
per the family's own fan-out precedents (FR×JA/FR×KO/IT×JA).

| Item | #20 generic | W43 FR×KO measured | W45 core measured | This edition measured |
|---|---|---|---|---|
| Badge slot | y=574 inserted, 22pt BRICK centered (FR family case) | y=574, 22pt, BRICK #a4553a, centered x=975 | y=574, 22pt, BRICK #a4553a, centered x=975 (core's own Chinese badge line) | y=574, 22pt, BRICK #a4553a, centered x=975 — identical to both |
| Badge text | — | `프랑스어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판` | `法语正文 · 简体中文讲解 — 给简体中文读者的版本` | `프랑스어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판` (W43 exact) |
| Footer | — | `Le Lucerna · 프랑스어 주간지 VOL.2 · 텍스트는 프랑스어 · 해설은 한국어` | `Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文` | `Le Lucerna · 프랑스어 주간지 VOL.3 · 텍스트는 프랑스어 · 해설은 한국어` |
| Page line | — | `제 {n} 면 / 총 {total} 면` | Chinese equivalent | `제 {n} 면 / 총 8 면` |
| P1 top-left | — | `VOL. 2 · 제2호` (W43; volume number advances per issue) | — | `VOL. 3 · 제3호` |
| Strapline | — | `HEBDOMADAIRE EN FRANÇAIS · 매주 발행 · 프랑스가 읽는 프랑스어` (W43 exact) | — | same string |
| Subtitle | — | `프랑스어 주간지 · VOL.2 · 깊은 가을 · 명절` (W43; pattern identical, tail is issue-specific) | — | `프랑스어 주간지 · VOL.3 · 결승 주말` |
| Gloss prefix | — | `해설 — ` (single prefix; label prefixes inside explanation strings stripped per W43 KO precedent) | — | `해설 — ` |
| Explanation fn | — | bridge() → expl() (1 def + 26 calls) | — | expl() (1 def + 26 calls) |
| P8 separator | — | `— 제 {pg} 면 —` | — | same |
| P8 note paren | — | half-width paren with space ` ({note})`, explicit PRINT_NOTES set | — | same |
| Section heads | — | French + short Korean suffix | — | e.g. `VIE QUOTIDIENNE · 생활`, `CULTURE · 축제`, `SPORT · 스포츠`, `JEUNESSE & MUSIQUE · 청년`, `POLITIQUE & CHIFFRES · 시사`, `LANGUE EN MAIN · 정독`, `EXERCICES & RÉPONSES · 연습과 정답`; P7 clinic head shortened to `CLINIQUE DES ERREURS · 오류` (377.7 ≤ 416, same value as W43 KO's shortened form); P5 creator-week title shortened to bare `PARIS CREATOR WEEK` (FR×EN round-4 precedent) |
| Explanation style | — | polite haeyo form throughout | — | same; registry type names (Chinese internal metadata, never printed) intentionally kept per W43 FR×KO and W45 FR×EN precedents; rendered Han-ideograph nodes 0 |

## Inherited-geometry adjudications (do NOT re-fix without new evidence)

- P6 `TROIS DATES POUR COMPRENDRE` right-edge 1935 / inner-frame
  crossing: node byte-identical to core (x=1469, y=1367, same string) —
  inherited frozen-French geometry, past even the outer frame line (1922)
  but still on the 1950-wide page. Same adjudication class as FR×EN's
  P8 F-group rows (1891.2/1899.5, core-identical). Confirmed visually on
  the P6 card: title on-page, no clipping, no neighbor overlap.
- Four French line-start closers are core-identical (same page, same y,
  same string): P3 y=790 (`: on le pose sur les tombes…`), P4 y=837
  (`: quarts de finale vendredi 6`), P5 y=431 (`: clôture du festival.`),
  P7 y=428 (`: attention à l'accord avec le sujet:`) — frozen French
  wraps, not edition defects.
- P6-ex flow end 2557 and P1-hiver 2298 are core-identical values
  (FR×EN adjudicated the same).
- Gloss line-start `·` separators and 1–2-syllable mid-word tails are
  wrapper behavior within the stated ≥3-syllable standard, not defects.
- Orphan-scan method notes (checks.py, fixed during this build): dy window
  tightened to 10–45; keys-flow ` (note)` wrapper parens stripped before
  source matching; pairs matching neither the spaced nor the unspaced
  source form are cross-block artifacts and are dropped (not counted).

## Korean proofread pass (builder self-check, before independent proofread)

- All Hangul text nodes extracted from the 8 delivered SVGs and read
  through: no typos found. The one 일/읽 confusion found during round 4
  (see Round history) was in transform.py's old string, never reached the
  paper; all `읽` usages in the delivered paper are legitimate
  reading-words (`읽었나요`, `읽고`, `읽으면`, `읽는 것`, `일정 읽기`).
- Note: the P8 keys listing filtered to Hangul nodes only drops
  French-only continuation lines (e.g. keys #16–18) — they are present in
  the SVG; see the full-node check in the build log.

## Open items for the coordinator / independent proofreader

- None from the builder's gates: every hard gate above measured clean on
  the final output. Finalization decision belongs to independent
  proofreading (not claimed here).
- The FR core's own web-PDF noise issue is explicitly out of scope for
  this edition (parent decision pending); this edition's web PDF was
  freshly generated and verified as above.
