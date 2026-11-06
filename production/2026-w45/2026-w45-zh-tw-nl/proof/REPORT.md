# INDEPENDENT PROOFREAD — W45 ZH-TW × NL (Traditional Chinese target · Dutch reader)

**Verdict: NOT PASS** — one blocking item (§B1). All other gates pass, including
Gate 10 reproduction at 8/8. The edition must NOT be inserted until the builder
fixes §B1 and a full reproof passes on the new render.

**Proofreader:** independent round (not the builder). No file in the delivery or
build dirs was modified; all proof work is under
`hidden_files/w45/zh-tw-nl-proof/` (this report + `work/`).

**Delivery verified:** `files/weekly-report-w45-zh-tw-nl/` — svg ×8, cards ×8
(1950×2700 PNG), print PDF, web PDF, WEEKLY-KIT.md, ABSTRACT.txt.
SVG/card filenames use the ZH-TW core's naming (p1-front, p2-life, p3-culture,
p4-sport, p5-youth, p6-deep, p7-lang, p8-test) as delivered.

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live worker writing to the delivery/build dirs: `ps` showed only
  sibling-edition workers (a zh-tw×RU freeze baseline, later a zh-tw×JA render)
  targeting other dirs. None touched `weekly-report-w45-zh-tw-nl` or its build dir.
- (b) Three mtime snapshots of both dirs (start / mid-proof / end-proof):
  **ZERO changes** across the whole proof.
- (c) Builder session completed: delivery files dated Oct 28 09:13–09:17, KIT
  written, no build in progress.
- Pre-flight PASSED; proof proceeded. No subagent was spawned, `weekly-git` was
  not touched, `insert.py` was not run, nothing was posted to Discord or main chat,
  no cron was created, no shared scratch dir was cleaned.

## B. BLOCKING LIST (1 item)

### B1. P7 readers'-corner letter box: the last Dutch disclosure line is struck through by the box border (visible on the card)

- **Where:** `files/weekly-report-w45-zh-tw-nl/svg/p7-lang.svg`, readers'-corner
  box; visible on `files/weekly-report-w45-zh-tw-nl/cards/p7-lang.png`.
  Source of the geometry: `hidden_files/weekly-report-w45-zh-tw-nl-build/content7.py`
  (`lh` letter-box height formula).
- **Measured evidence (audit tool's own parser, `tools/occlusion_audit.py`):**
  - Letter box rect: x=1451, y=1155.86, w=434, h=531.5 → raw bottom **1687.36**,
    stroke 1.4 → expanded bottom **1688.06**.
  - Last Dutch disclosure line node: x=1473, y=**1694.23**, font Noto Sans CJK TC
    20, text `blijft, uitnodiging open. Stuur je brief in!`, true ink box
    **[1473.0, 1677.98, 1844.5, 1699.23]**.
  - Ink bottom **1699.23 exceeds the raw border by 11.87 px** (11.17 px past the
    expanded border). The baseline itself (1694.23) sits 6.87 px BELOW the border.
  - Card crop (`work/p7-letterbox-crop.png`, and the full P7 card) shows the box
    border line running horizontally **through the glyphs** of that last line.
    The teaser gold rule below (y≈1717) is clear of it; the defect is solely the
    letter-box border strike-through.
- **Why the audit reads 0 flags (blind spot, not a pass):** the audit's BOXTITLE
  check only considers texts whose anchor point or ink center lies inside the
  rect. Here ink center y=1688.61 exceeds the expanded bottom 1688.06 by
  0.55 px, so the line gets **no candidate rect and no flag** — the audit is
  structurally blind to a line that has fallen (nearly) entirely outside its box.
  The 0-flag result is real but does not cover this line.
- **Why this is blocking, not inherited:** the core shows the SAME pattern
  (core last English line ink bottom 1756.38 vs expanded box bottom 1746.06;
  center 1746.26 vs 1746.06, 0.20 px outside — the builder's "0.24 px slack";
  core card crop `work/p7-core-letterbox-crop.png` shows the same strike-through
  on `invitation stays open.`). The core's instance is recorded below as
  non-blocking inherited behavior (frozen core text). But the edition's line is
  the edition's OWN Dutch text, written by this build, and gate 7 of this
  proofread requires the edition's last line to be FULLY INSIDE the box. It is
  not. The builder's KIT claim ("this edition's 5-line disclosure sits
  comfortably inside") is factually false: shortening to 5 lines did not fix the
  geometry because the `lh` formula under-budgets the laid-out text by ~12 px.
  Precedent: the builder's own round-1 fix treated a 10.6 px past-border
  letter-box line as a defect requiring a fix; the current 11.87 px overflow is
  larger than that.
- **Concrete remedy (builder, via the TRANSFORM — never a hand patch):**
  1. In the transform, enlarge the letter box so the last Dutch line sits fully
     inside with clear space — e.g. raise the `lh` formula's bottom pad from
     +26 to +50 (+24 px), or equivalently shorten the Dutch disclosure by one
     line. Either is acceptable if the measurement below holds.
  2. Re-render in ONE process (`run.py` → `render.py`), then re-measure with the
     audit parser: last-line ink bottom must clear the new border by ≥ ~10 px.
  3. Re-run the occlusion audit (must stay 0 flags) and re-eyeball the P7 card
     (border must not touch any glyph).
  4. Re-run Gate 10 from the updated transform: the replay must reproduce the
     FIXED SVGs 8/8 byte-identical.
  5. Full reproof of the new render (this report's gates re-run, not a delta check).

## Per-gate evidence (all gates except B1 pass)

### 1. Freeze baseline + strict-CJK diff — PASS
- `tools/freeze.py baseline` on the pristine core copy: **8/8 byte-identical**
  to the zh-tw core SVGs; core SVGs re-hashed unchanged afterwards (hashes match
  the builder KIT table exactly).
- `freeze.py diff --strict-cjk` core → edition: p1 +23/−22, p2 +37/−35,
  p3 +41/−38, p4 +33/−32, p5 +41/−40, p6 +41/−37, p7 +86/−87, p8 +194/−186;
  CJK core → edition 952→920, 1018→996, 1088→1065, 831→809, 1101→1079,
  942→921, 808→788, 1114→1094; **strict-CJK added = 0 on all 8 pages**.
- CJK-decrease analysis: core − edition = ONLY `解`. All 9 occurrences of `解`
  in the core are in the P1 badge string (1) and the every-page footer string
  (8) — both legitimately replaced by Dutch furniture. No target-text character
  was lost.
- Builder's run: exit 0, **ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings**
  (reproduced independently in Gate 10, exit 0, 0 warnings).

### 2. Traditional independence — HARD GATE — PASS
- Own re-extraction from the shipped SVGs themselves (broader CJK regex than the
  builder's): edition **772**, core **773**, W43 zh-tw-nl **790**,
  union (core ∪ W43) **1030**, **edition chars outside the union: 0**,
  **edition − core: 0**, core − edition: only `解` (see gate 1).
  Judged by outside=0, not by matching the builder's counts (they happen to match).
- Curated Simplified-only spot list (邮 说 国 龙 马 发 让 对 为 体 汉 语 学 读 书
  车 东 头 乐 买 卖 练 线 纸 宝 电 话 见 观 现 丽 亿 仅 优 礼 认 讲 许 论 设 证
  丰 义 习 乡 乱 争 产 亲）over all edition text nodes: **0 hits** (core also 0).
  (An earlier draft list built from a surname table was discarded: it contained
  characters shared by both scripts and was not a valid Simplified-only list.)
- Transform inspected end to end (413 lines): exact-literal `sub()` calls with
  count assertions only; **no OpenCC, no conversion, no mapping table, no
  Simplified→Traditional logic anywhere** (grep for opencc/convert/s2t/mapping:
  empty). Target Traditional text is never a replacement target.

### 3. Target text zero difference (run level) — PASS
- Freeze-diff audit of every removed string containing CJK (all 8 pages):
  every one is (a) badge/footer/page-line furniture, (b) a bilingual head whose
  Traditional half survives in the Dutch-headed replacement, or (c) an English
  explanation/gloss/P8 note citing CJK terms, replaced by its Dutch equivalent.
  No pure target-text string (article, exercise body, option) appears in the
  removed set. Combined with added CJK = 0 and edition − core = 0, target text
  is unchanged at run level.

### 4. Gate 10 — REPRODUCTION — PASS (8/8)
- Method (own replay, not the builder's gate10 output): fresh copy of the zh-tw
  core build dir → builder's transform ALONE → whole-path-segment repoint of
  the edition-dir path to `hidden_files/w45/zh-tw-nl-proof/work/gate10-out`
  (no spliced temp dir, no es-template failure mode) → one-process driver
  `run.py` then `render.py`.
- Repoint verified clean: zero remaining references to the edition dir or the
  core dir in the copy before running.
- Run exit **0**, **zero** FLOW OVERFLOW / HEAD TOO WIDE warnings, registry
  TOTAL **150**.
- Byte comparison gate10-out vs delivered: **SVGs 8/8 byte-identical**,
  **cards 8/8 byte-identical**, print PDF byte-identical (same SHA-256, see §Pins).
- No stray nested tree: delivery dir is flat (svg/, cards/, 2 PDFs, KIT,
  ABSTRACT.txt only); no `files/`-level gate10 dir exists; my gate10 tree lives
  only under `hidden_files/w45/zh-tw-nl-proof/work/`.

### 5. p8.py — PASS
- Explicit-path form (tables.json zh-tw `p8_file` is `p8-test.svg`, matching this
  core's file, but the explicit form was used anyway):
  `p8.py compare --core-p8 <core p8-test.svg> --edition-p8 <edition p8-test.svg> --total 150`
  → **CLEAN — 150 noted, missing=[], extra_count=0, uncertain=[], keydiff=[]**.
- Independent registry-dump diff (REG dumped from a fresh repointed core copy
  vs the gate10 edition copy, 150 items each): **keys identical 150/150,
  levels identical, types identical, pages identical**; notes differ on all 150
  items, all being the expected EN→NL translations. Item 150 key frozen
  `(開放題,範文如下)` in both; its note properly Dutch
  (`Open opdracht — het modelantwoord staat hierboven in deel F (138 tekens)`).
  The "writing-item change" is therefore the translated note of the frozen
  writing item, with no key/level/type/page change anywhere.
- Gate10-out SVGs re-hashed after the registry dumps: still 8/8 identical
  (determinism re-confirmed).

### 6. P8 dash style + AI-variant trap — PASS (adjudicated)
- Dash unchanged from the core: edition build `content8.py` answer rendering at
  **12.8 pt / lh 1.12 / gap 1** — the W45 core geometry (W43 used 13.3/1.16/gap2;
  W45 core geometry wins on geometry, style follows the W43 column). Rendered
  P8 keys are `N. key — note` throughout; separators `— Pagina N —` at 12.8 pt
  (W43 shipped separator: 13.3 pt — geometry difference recorded, not a defect).
- Dash family verified from the W43 zh-tw-nl build code: W43 `content8.py`
  separator `— Pagina {pg} —`, gloss prefix `Uitleg — `, footer
  `Pagina {n} van {total}` — the NL column is a dash family
  (es/pt/it = paren, fr/de/nl/ru/ko/ja = dash), consistent with this edition.
- AI trap — BOTH forms Dutch in the final render:
  - P6 gloss (`content56.py` line 118, rendered on p6-deep): `Drie plustekens:
    Finance+ (financiën plus technologie), AI+ (kunstmatige intelligentie in
    banken, beleggingen en verzekeringen)…` — Dutch.
  - P8 key 138 (rendered on p8-test): `138. 人工智慧 — AI in de financiële
    wereld is 人工智慧＋.` — Dutch note, term cited verbatim.
- Verbatim-vs-pinyin adjudication against THIS column's shipped P8: W43's
  shipped P8 contains NO AI item (different issue), so there is no direct term
  precedent; the column precedent visible in W43's shipped P8 is keys printed
  in characters plus pinyin pronunciation glosses for specific terms
  (e.g. `108. … xīngguāng dàdào`, `112. 品味 — … pǐnwèiquàn`). The edition's
  note is a concept mapping (AI inside finance = the `人工智慧＋` term), not a
  pronunciation gloss, and it cites the key term itself in characters — the
  keys-in-characters practice. Verbatim is correct here; importing the
  zh-tw-it pinyin-only rule or the zh-tw-es verbatim rule would be wrong.
  Strict-CJK added stays 0.

### 7. Occlusion audit + P7 letter-box — FAIL (see B1; all other parts pass)
- `occlusion_audit.py --selftest`: OK (all 6 planted classes fire, clean
  controls silent). Edition **0 flags**, core **0 flags**, **NEW vs core 0**.
- Same-baseline ink-collision scan (own implementation on the canonical
  `ink_box`): **0 collisions** on all 8 pages.
- Chart-label element check (text ink vs later-drawn rects, P4/P6, chips and
  full-page frames excluded): **0 overlaps**.
- P7 heads: A2 ink right 433.5, B1 **960.8** (column edge 961, fits by 0.2 px),
  B2 1405.8 — all inside their columns (see non-blocking notes).
- P7 col3/teaser geometry as claimed: col3 box bottom 1687.36, teaser rule clear
  (teaser content ends 2485.36 per the build log; footer rule 2580 clear).
- **The letter-box last line fails the "fully inside" criterion: see B1.**
  The audit's 0 flags do not cover this line (blind spot documented in B1).

### 8. Gloss/match counts (ZH-TW core's true counts) — PASS
- Render counts: `Uitleg — ` ×**12** (P1 2, P2 2, P3 3, P4 2, P5 2, P6 1, P7 0,
  P8 0) = the core's 12 Notes boxes (core per-page Notes: 2/2/3/2/2/1/0/0);
  `Notes` residual **0**.
- Sources: `gloss(` ×12 across content12/34/56 (4+5+3); `glossline(` **4 = 4**
  (content7 ×3 + content8 §F ×1); match notes **16 = 16** — P8 keys 25–28,
  43–46, 61–64, 79–82 (4 sets × 4), all Dutch in the render.
  (The zh-cn family's "33" figure does not apply and was not used.)
- Registry **150** (A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38;
  types 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1); writing model
  **138** characters (`138 tekens` node on P8; model text frozen from the core).

### 9. P7 golden sentences — PASS
- All 8 verbatim from this issue's own articles, bare-sentence count exactly
  **2 each** issue-wide (article + P7 strip; the bracketed `「…」` form counts 1
  because the article occurrence carries no brackets — the bare count is the
  correct measure, matching the core KIT's method):
  用手機轉帳…金融科技 (p. 1); 123個國家及城市、1,600個攤位 (p. 1);
  需要才買… (p. 2); 在高雄，鋼鐵也能變成舞台 (p. 3);
  福隆的夏天，在10月26日畫下句點 (p. 3); 6比0完封兄弟，龍隊拋下紅色彩帶 (p. 4);
  250家店家一起討糖 (p. 5); 旅展首日中午12點才開門 (p. 6).
- `(p. N)` tags present for all 8; all 8 Dutch translations present.
- Tag form is the zh-tw core's `(p. N)` form (not zh-tw-de's `S.` form).

### 10. Images — PASS (provenance NOT re-litigated)
- Per-page payloads byte-identical core vs edition with identical placement
  (P1 1, P2 1, P3 0, P4 1, P5 1, P6 0, P7 0, P8 0; base64-payload SHA-256 prefix
  match per page).
- Credit lines byte-identical to the core and verbatim from the Commons Artist
  field: P1 `Photo: Wilfredor — CC0 (Wikimedia Commons)`,
  P2 `Photo: CorraleH — CC0 (Wikimedia Commons)`,
  P4 `Photo: Bain News Service — Public domain (Wikimedia Commons)`,
  P5 `Photo: Benjamin Balazs — CC0 (Wikimedia Commons)`.
  P4 photo + caption + credit fully visible on the card, no overlap.
- Per the binding core-KIT adjudication (2026-10-27, CLOSED): placed bytes and
  credit line are unchanged, so P4 provenance is NOT re-flagged.

### 11. Readers' corner — PASS (content; geometry fails per B1)
- Frozen Traditional disclosure line-for-line identical core vs edition
  (verified on the matching text nodes).
- Dutch disclosure present in the 5-line form: label `Voorbeeldbrief — geen
  echte.`, deferral (VOL.1 promised real letters + page-8 writing from this
  issue, nothing arrived), explicit open invitation ending verbatim
  `Stuur je brief in!`.
- W43 precedent note: W43's Dutch disclosure wording differs
  (`Voorbeeldbrief van de redactie — geen…`) because it is a different issue;
  the required elements (no genuine letters arrived + verbatim invitation) hold.
- Geometry of this disclosure's last line: see B1 (the only failure).

### 12. Furniture three-way — PASS
- Badge MEASURED on all three P1s (PIL, sans bold 21):
  core y=378, 21 pt bold, OLIVE #3e4c2a, width 1227.3 px;
  W43 y=378, 21 pt bold, BRICK #a4553a, width 1256.8 px;
  this edition y=378, 21 pt bold, BRICK #a4553a, width 1256.8 px,
  in-place replacement, string identical to W43:
  `TEKSTEN IN HET CHINEES (TRADITIONEEL) · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`.
  Color follows the NL column (BRICK), judged by the W43 zh-tw-nl shipped P1,
  not by the RU column's OLIVE.
- Footer (all 8 pages): `Lucerna · CHINEES WEEKBLAD VOL.2 · TEKSTEN IN HET
  CHINEES (TRADITIONEEL) · UITLEG IN HET NEDERLANDS` + `Pagina N van 8` —
  identical to W43 except VOL.1 → VOL.2.
- Gloss prefix `Uitleg — `; P8 separators `— Pagina N — `;
  P8 keys header `答案 · Antwoordsleutel — in paginavolgorde, met een korte
  Nederlandse noot bij elk item` — byte-identical to the W43 shipped string.
  No tables.json discrepancy arose (tables.json was not edited; shipped W43
  wins wherever it matters, and it agrees).

### 13. Residual Latin — RENDERED-OUTPUT SWEEP — PASS
- Sweep of ALL **1,450** text nodes in the delivered SVGs (not just sources).
- Required counts, all exact: `算一算 · Work it out` = **0**,
  `算一算 · Reken uit` = **3** (P2, P3, P5; P3 card visually confirmed);
  `Baseball words` = **0** / `Honkbaltaal` = **1** (P4 title);
  `Deep-read quiz` = **0** / `Diep-leesquiz` = **1** (P6 head).
  Both late fixes are present as `sub()` calls in the transform AND reproduced
  by the Gate 10 replay (byte-identical SVGs).
- English-phrase grep (37-phrase set incl. `Explanations in English`,
  `Quick quiz`, `Did you get it`, `Fill in`, `True or false`, `Answer keys`,
  `Model answer`, `Open task`, `Notes`, `Match`, `Writing`, `Over to you`,
  `Practice example`, `Read the chart`, `Work it out`): **all 0**.
- English-marker adjudication (own scan, all hits listed):
  ` the ` 1 = frozen theme line `Fintech Nexus: Bridging the World, Building
  the Future`; ` and ` 1 = proper name `Hong Kong Convention and Exhibition
  Centre`; ` with/from/this/that/have/were/will/would/about/into/after/before/
  during/between/through/each/every/first` = 0; `quiz` 2 = Dutch loanword
  (`Snelle quiz`, `De grote quiz`); `week` 24 = Dutch `week` + proper-name
  `FinTech Week` + footer `WEEKBLAD` (each of the 24 listed and checked);
  ` was ` 2 = Dutch verb (`was de wedstrijd voorbij`, `Ik was hier`);
  `halloween` 4, `festival` 2, `model` 3 = Dutch words/loanwords;
  `shows/show` 0; `fair/travel` 1 each = proper name `Taipei International
  Travel Fair (ITF)`; `centre` 2 / `center` 3 = venue proper names.
  **Zero real English explanation prose.**
- Other legitimate survivals (adjudicated): frozen target-text proper names and
  theme strings, `Fintech`/`AI`/`AI+`/`Finance+` abbreviations, `NT$`, `VOL.2`,
  level chips A2/B1/B2, option letters, Dutch loanword `Frame:` in the P7 frame
  note, `體育 · Sport` (Dutch word identical to English, recorded not changed),
  all 4 Commons credit lines byte-identical.

### 14. Web regen — PASS (with the explicit timestamp exception)
- Cards **8/8 byte-identical** (gate10 render vs delivered).
- Print PDF **byte-identical** (SHA-256 `828d…e7`, see §Pins).
- Web PDF: same size (3,395,927 B) and **content-identical except timestamp
  bytes, stated explicitly**: exactly 8 differing bytes in 2 spans, both the
  digits of `/CreationDate (D:…Z)` and `/ModDate (D:…Z)`
  (delivered `20261028091406Z` = delivery render time;
  gate10 `20261028092722Z` = replay render time). Every other byte identical.

### 15. Eyeball all 8 cards — 7 CLEAN, P7 FAILS ONLY ON B1
- P1: badge, masthead, harbour photo + Wilfredor credit, gloss boxes, footer —
  clean. P2: `Reken uit` head, 2-line `你呢?` Dutch question, champion-deals box,
  rain photo + CorraleH credit — clean. P3: `Reken uit`, solar-term table,
  visit planner — clean. P4: `Honkbaltaal` title, runs chart with labels, team
  photo + Bain credit fully visible, caption uncovered — clean.
  P5: pumpkin photo + Balazs credit, `Reken uit`, schedule/stage boxes — clean.
  P6: `Diep-leesquiz` head, hours chart, AI+ gloss, price box — clean.
  P8: dash keys, `Pagina` separators, Dutch notes, F writing model + 138 tekens,
  footer — clean.
- P7: columns, clinic, frame, phrases strip with `(p. N)` tags + Dutch
  translations, teaser, footer — all clean EXCEPT the readers'-corner last line
  (B1): the letter-box border strikes through `blijft, uitnodiging open.
  Stuur je brief in!`.

### 16. ABSTRACT.txt — PASS
- Dutch single line (1 line), **0 ASCII double quotes**.
- Contains: paper name (`Lucerna weekblad`), target language
  (`Traditioneel Chinees`), A2–B2, 150 exercises (`150 oefeningen`), learner
  search phrase (`Chinees leren lezen met Nederlandse uitleg`), and the real
  topic keywords — Hong Kong FinTech Week, Taipei International Travel Fair,
  Wei Chuan Dragons Taiwan Series title, Lidong, Kaohsiung steel festival,
  Fulong sand festival, Tianmu Halloween.
- Every named topic cross-checked against the zh-tw core's actual content
  (core contains 金融科技， 旅展， 龍隊， 立冬， 鋼雕， 沙雕， 天母） — **no topic
  outside the core**.

## Non-blocking observations (do NOT affect the verdict)

- **N1. P7 b2 column ends 1529 vs core 1496 (+1 line).** Within the 1560 nominal
  bottom, no warning, phrases strip far below (teaser rule ≈1717). On the card
  the B2 column ends cleanly with no collision. Not a defect.
- **N2. P7 B1 head ink right 960.8 vs column edge 961 (fits by 0.2 px).**
  Same-baseline scan passes at 0; on the card the head
  (`B1 · 球賽與節氣 · Sport & seizoenen`) is fully inside its column and
  visually clean. Tight but passing; recorded, not a defect.
- **N3. Core's own P7 letter-box line (inherited behavior).** The core's last
  English disclosure line is struck through by its own letter-box border by the
  same mechanism (ink bottom 1756.38 vs expanded border 1746.06; center outside
  by 0.20 px, hence 0 audit flags). This is frozen core text and is recorded as
  non-blocking inherited behavior for the CORE. It does not excuse the
  edition's own Dutch line (see B1).
- **N4. P8 separator geometry 12.8 pt vs W43's 13.3 pt.** The W45 core geometry
  wins by design (style follows W43, geometry follows the W45 core). Not a defect.
- **N5. AI-term adjudication (see gate 6).** Verbatim citation of `人工智慧＋`
  in the P8 note is adjudicated correct for this column; no pinyin form is
  required here. Not a defect.
- **N6. P8 key 100 prints `45,000`.** The key is the frozen registry value from
  the core (article figure with English thousands comma); the Dutch note beside
  it uses `45.000`. Frozen key, not explanation prose. Not a defect.

## Limitations (stated honestly)

- Dutch was checked by full reading of every rendered node against the core and
  the transform, not by a native Dutch speaker.
- Commons was NOT re-queried live in this round: credits were verified
  byte-identical to the core and matched to the core KIT's Commons Artist-field
  records; P4 provenance stands on the binding 2026-10-27 coordinator
  adjudication (placed bytes + credit unchanged), not on a fresh fetch.
- No live-browser check was possible in this subagent role; eyeballing was done
  on the delivered rendered PNG cards (the shipped artifacts), which is the
  correct surface for layout verdicts.
- One builder-KIT claim was overturned by measurement (the "comfortably inside"
  letter-box claim, B1); every other builder claim re-verified as stated.

## PDF pins re-verified (delivered files)

| file | bytes | SHA-256 |
|---|---|---|
| Lucerna-VOL2-NL.pdf (print) | 20,844,848 | 828dcde3b809aea7761f1abad1bca8266841799dbbfa8be35a750f152e760de7 |
| Lucerna-VOL2-NL-web.pdf (web) | 3,395,927 | 3001b65131cdb8b1768d98105790f37e8b005774355179569ce5a5027d753a38 |

Both match the coordinator-verified pins. Print PDF reproduced byte-identical
by Gate 10; web PDF content-identical except the 8 timestamp bytes (gate 14).

## Verdict restated

**NOT PASS** — blocking item B1 only: the P7 readers'-corner letter-box border
strikes through the last Dutch disclosure line on the shipped card. Fix per B1's
remedy (via the transform), re-render, re-run Gate 10, then full reproof. Nothing
in this report declares the edition shipped, and no insert, post, or delivery
was performed by this proofread.
