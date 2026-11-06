# INDEPENDENT RE-PROOFREAD — W45 ZH-TW × NL (Traditional Chinese target · Dutch reader)

**Verdict: PASS — ZERO PROBLEMS.** All 16 gates re-verified from scratch on the
fixed render, including Gate 10 reproduction at 8/8 and the B1 letter-box fix
by direct measurement (not by the audit's 0 flags). This report is the
finalization evidence for the coordinator's insert. No file in the delivery or
build dirs was modified by this reproof; all proof work is under
`hidden_files/w45/zh-tw-nl-reproof/` (this report + `work/`). No subagent was
spawned, `weekly-git` was not touched, `insert.py` was not run, nothing was
posted to Discord or main chat, no cron was created, no shared scratch dir was
cleaned. Nothing in this report declares the edition shipped — the coordinator
inserts.

**Delivery verified:** `files/weekly-report-w45-zh-tw-nl/` — svg ×8, cards ×8
(1950×2700 PNG), print + web PDF, WEEKLY-KIT.md (with §11 fix-round section;
§10 pins marked superseded), ABSTRACT.txt (351 B, unchanged mtime 09:17).
SVG/card filenames use the ZH-TW core's naming (p1-front, p2-life, p3-culture,
p4-sport, p5-youth, p6-deep, p7-lang, p8-test), as delivered.

**Note on a task-path discrepancy:** the fix work products live at
`hidden_files/w45-zh-tw-nl-fix/` (plus `w45-zh-tw-nl-fix-gate10-build/`,
`w45-zh-tw-nl-fix-gate10-run.log`, `w45-zh-tw-nl-fix-build/`,
`w45-zh-tw-nl-fix-render.log`), not at the task's stated
`hidden_files/w45/zh-tw-nl-fix/` path, which does not exist. All fix evidence
below was read from the actual locations.

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live worker writing to the delivery/build dirs: `ps` at start and at
  close showed no run/render/insert/transform process at all (only a sibling
  zh-tw×pt reproof's `sleep` wait, touching other dirs).
- (b) Three mtime snapshots of both dirs (start 09:38, mid 09:42, end of proof):
  **ZERO changes** — snap1 = snap2 = snap3, byte-for-byte identical listings.
- (c) Fix session completed: delivery files dated Oct 28 09:35–09:37, fix logs
  present, no build in progress.
- Pre-flight PASSED; reproof proceeded.

## B1 FIX VERIFICATION (the critical gate — DIRECT MEASUREMENT)

Measured myself on the delivered SVG with the audit tool's own ink parser
(`tools/occlusion_audit.py` `ink_box`), and confirmed on the P7 card crop
(`work/p7-letterbox-crop.png`):

- Letter box rect: x=1451, y=1155.86, w=434, h=**555.5** → bottom **1711.36**
  (expanded 1712.06). The +50 pad from transform §10 is in the delivered SVG.
- Last Dutch line UNCHANGED: node y=1694.23,
  text `blijft, uitnodiging open. Stuur je brief in!`,
  ink box [1473.0, 1677.98, 1844.5, 1699.23], ink center 1688.61 —
  now **23.45 px inside** the expanded border (was 0.55 px outside).
- **Clearance: 12.13 px raw (12.83 px vs expanded border)** — meets the
  ≥ ~10 px requirement. (Pre-fix: ink bottom 1699.23 vs border 1687.36,
  11.87 px past — the defect is gone, the line did not move, the box grew.)
- Card crop: the last line sits FULLY INSIDE the box with clear space below;
  the border touches NO glyph. The pre-fix strike-through is gone.
- No new collision below the enlarged box: phrases gold rule at **1741.36**
  (30 px below the new box bottom, was 1717.36); teaser flow ends 2509.36
  (last teaser ink bottom 2478.11), footer rule 2580 → **70.64 px clear**
  (101.89 px from last teaser ink). Phrases strip, teaser, footer all clean
  on the card (`work/p7-lower.png`).
- The audit's BOXTITLE blind spot is acknowledged, not relied on: audit 0 is
  reported in gate 7 as required, but the evidence for this box is the direct
  measurement above.
- Wording byte-identical to the pre-fix disclosure (all 3 disclosure nodes,
  same texts and same y positions; only the box geometry changed).

## Per-gate evidence (all 16 gates pass)

### 1. Freeze baseline + strict-CJK diff — PASS
- `tools/freeze.py baseline` on the pristine core copy: **8/8 byte-identical**
  to the zh-tw core SVGs; core SVG hashes after the run match the builder KIT
  table exactly (p1 4672c972…, p7 00ac7f57…, p8 e6e97d02…, etc.); core
  integrity re-confirmed by the tool itself.
- `freeze.py diff --strict-cjk` core → edition: p1 +23/−22, p2 +37/−35,
  p3 +41/−38, p4 +33/−32, p5 +41/−40, p6 +41/−37, p7 +86/−87, p8 +194/−186;
  CJK 952→920, 1018→996, 1088→1065, 831→809, 1101→1079, 942→921, 808→788,
  1114→1094; **strict-CJK added = 0 on all 8 pages**.
- CJK-decrease analysis: core − edition = ONLY `解`, occurring in the core
  solely in the P1 badge string (1) and the every-page footer string (8) —
  both legitimately replaced by Dutch furniture. No target-text character lost.
- Builder's run: exit 0, ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings
  (reproduced independently in Gate 10, exit 0, 0 warnings).

### 2. Traditional independence — HARD GATE — PASS
- Own re-extraction from the shipped SVGs themselves (CJK regex covering
  2E80–2FFF, 3000–303F, 3400–4DBF, 4E00–9FFF, F900–FAFF, 20000–2A6DF):
  edition **772**, core **773**, W43 zh-tw-nl **790**, union (core ∪ W43)
  **1030**, **edition chars outside the union: 0**, **edition − core: 0**,
  core − edition: only `解` (see gate 1). Judged by outside=0.
- Curated Simplified-only spot list (邮 说 国 龙 马 发 让 对 为 体 汉 语 学 读 书
  车 东 头 乐 买 卖 练 线 纸 宝 电 话 见 观 现 丽 亿 仅 优 礼 认 讲 许 论 设 证
  丰 义 习 乡 乱 争 产 亲 刘）over all edition text nodes: **0 hits**.
- Transform inspected (423 lines): exact-literal `sub()` calls with count
  assertions only; grep for opencc/convert/s2t/mapping: **empty** — no OpenCC,
  no conversion, no mapping table, no Simplified→Traditional logic anywhere.
  The fix-round §10 `sub()` changes only the `lh` formula's bottom pad
  (+26 → +50); it touches no text. Target Traditional text is never a
  replacement target.

### 3. Target text ZERO difference (run level) — PASS
- Freeze-diff audit of every removed string containing CJK (180 strings,
  all 8 pages): every one is (a) badge/footer/page-line furniture
  (incl. `第 N 版 / 共 8 版` → `Pagina N van 8`), (b) a bilingual head whose
  Traditional half survives in the Dutch-headed replacement, or (c) an English
  explanation/gloss/P8 note citing CJK terms, replaced by its Dutch
  equivalent. No pure target-text string (article, exercise body, option)
  appears in the removed set. Combined with added CJK = 0 and
  edition − core = 0, target text is unchanged at run level.

### 4. Gate 10 — REPRODUCTION — PASS (8/8)
- Method (own replay, not the fixer's gate10 output): fresh copy of the
  zh-tw core build dir → builder's transform ALONE (exit 0, TRANSFORM
  COMPLETE) → whole-dir-name repoint of the edition-dir path to
  `hidden_files/w45/zh-tw-nl-reproof/work/gate10-out` (no spliced temp dir,
  no es-template failure mode) → one-process driver `run.py` then `render.py`.
- Repoint verified clean before running: zero references to the real edition
  dir or the core dir in the copy (`files/weekly-report` grep: clean).
- Run exit **0**, **zero** FLOW OVERFLOW / HEAD TOO WIDE warnings, registry
  TOTAL **150** (A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38;
  types 67/54/16/12/1).
- Byte comparison gate10-out vs delivered: **SVGs 8/8 byte-identical**,
  **cards 8/8 byte-identical**, print PDF byte-identical (same SHA-256).
- Gate10-out SVGs re-hashed after the registry dumps: still 8/8 identical
  (determinism re-confirmed).
- No stray nested tree: delivery dir is flat (svg/, cards/, 2 PDFs, KIT,
  ABSTRACT.txt only); no `files/`-level gate10/reproof dir exists; the
  fixer's first-attempt `files/` misplacement is gone — `find` under
  `files/` shows no gate10-like entry, and the final Gate 10 replay is clean
  under `hidden_files/`.

### 5. p8.py — PASS
- Explicit-path form:
  `p8.py compare --core-p8 <core p8-test.svg> --edition-p8 <edition p8-test.svg> --total 150`
  → **CLEAN — 150 noted, missing=[], extra_count=0, uncertain=[], keydiff=[]**.
  (tables.json zh-tw `p8_file` is `p8-test.svg`, matching this core's file;
  the explicit form was used anyway, as required.)
- Independent registry-dump diff (REG dumped from a fresh repointed core copy
  vs the gate10 edition copy, 150 items each): **keys identical 150/150,
  levels identical, types identical, pages identical**; notes differ on all
  150 items, all being the expected EN→NL translations. Item 150 key frozen
  `(開放題,範文如下)` in both; its note properly Dutch
  (`Open opdracht — het modelantwoord staat hierboven in deel F (138 tekens)`).
  The writing-item change is therefore the translated note of the frozen
  writing item, with no key/level/type/page change anywhere. notediff 150/150.

### 6. P8 dash style + AI-variant trap — PASS (adjudication CONFIRMED, not overturned)
- Dash unchanged from the core: edition build `content8.py` answer rendering
  at **12.8 pt / lh 1.12 / gap 1** — the W45 core geometry (W43 used
  13.3/1.16/gap2; W45 core geometry wins on geometry, style follows the W43
  column). Rendered P8 keys are `N. key — note` throughout (149 dash-form
  keys; item 150 is the ✓ writing item by design); separators
  `— Pagina N —` at 12.8 pt (W43 shipped separator: 13.3 pt — geometry
  difference recorded, not a defect).
- Dash family verified from the W43 zh-tw-nl build code myself: W43
  `content8.py` separator `— Pagina {pg} —` at 13.3/1.16/gap2, gloss prefix
  `Uitleg — `, footer `Pagina {n} van {total}` — the NL column is a dash
  family (es/pt/it = paren, fr/de/nl/ru/ko/ja = dash), consistent here.
- AI trap — BOTH forms Dutch in the final render:
  - P6 gloss (`content56.py` line 118, rendered on p6-deep): `Drie plustekens:
    Finance+ (financiën plus technologie), AI+ (kunstmatige intelligentie in
    banken, beleggingen en verzekeringen)…` — Dutch.
  - P8 key 138 (rendered on p8-test): `138. 人工智慧 — AI in de financiële
    wereld is 人工智慧＋.` — Dutch note, term cited verbatim.
- Adjudication re-verified against THIS column's shipped P8: W43's shipped P8
  contains NO AI item (confirmed: `人工智慧` absent), so there is no direct
  term precedent; the column precedent visible in W43's shipped P8 is keys
  printed in characters plus pinyin pronunciation glosses for specific terms
  (e.g. `108. … xīngguāng dàdào`, `112. 品味 — … pǐnwèiquàn`). The edition's
  note is a concept mapping (AI inside finance = the `人工智慧＋` term), not a
  pronunciation gloss, and it cites the key term itself in characters — the
  keys-in-characters practice. **Verbatim is correct here; the first proof's
  adjudication stands.** Importing the zh-tw-it pinyin-only rule or the
  zh-tw-es verbatim rule would be wrong. Strict-CJK added stays 0.

### 7. Occlusion audit + P7 letter-box + change scope — PASS
- `occlusion_audit.py --selftest`: OK (all 6 planted classes fire, clean
  controls silent). Edition **0 flags**, core **0 flags**, **NEW vs core 0**.
- Same-baseline ink-collision scan (own implementation on the canonical
  `ink_box`): **0 collisions** on all 8 pages.
- Chart-label element check (text ink vs later-drawn rects, P4/P6, chips and
  full-page frames excluded): **0 overlaps**.
- P4 bars 120/600, P6 bars 600/800/800/800 — verified against the core
  (identical rect-width multisets core vs edition on both pages).
- P7 heads: A2 ink right 433.5, B1 **960.8** (column edge 961, fits by 0.2 px),
  B2 1405.8 — all inside their columns (see non-blocking notes).
- P7 col ends (fix log + my gate10 run): a2 1529, b1 1463, b2 1529 (b2 vs core
  1496, +1 line, ≤1560 nominal bottom, no warning).
- B1 fix: see the dedicated section above — direct measurement, not audit 0.
- CHANGE-SCOPE CHECK: delivered SVGs+cards P1–P6, P8 are **byte-identical to
  the pre-fix delivery** (first proof's gate10-out, which reproduced the
  pre-fix delivery 8/8); **P7 is the sole changed page** (SVG + card differ,
  all others identical). No other changed page exists.

### 8. Gloss/match counts (ZH-TW core's true counts) — PASS
- Render counts: `Uitleg — ` ×**12** (P1 2, P2 2, P3 3, P4 2, P5 2, P6 1, P7 0,
  P8 0) = the core's 12 Notes boxes (core per-page Notes: 2/2/3/2/2/1/0/0);
  `Notes` residual **0** (core has 12 `Notes` nodes, edition 0).
- Sources: `gloss(` ×12 across content12/34/56 (4+5+3); `glossline(` **4 = 4**
  (content7 ×3 + content8 §F ×1); match notes **16 = 16** — P8 keys 25–28,
  43–46, 61–64, 79–82 (4 sets × 4), all Dutch in the render (verified
  key-by-key). (The zh-cn family's "33" figure does not apply and was not used.)
- Registry **150** (A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38;
  types 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1); writing model
  **138** characters (`138 tekens` nodes on P8; model text frozen from the core).

### 9. P7 golden sentences — PASS
- All 8 full sentences verbatim from this issue's own articles, bare-sentence
  count exactly **2 each** issue-wide (article + P7 strip), in edition AND
  core: 用手機轉帳、掃碼付款、網上買保險，都是金融科技；123個國家及城市、1,600個攤位；
  需要才買，不要為了折扣買一堆用不到的東西；在高雄，鋼鐵也能變成舞台；
  福隆的夏天，在10月26日畫下句點；6比0完封兄弟，龍隊拋下紅色彩帶；
  250家店家一起討糖；旅展首日中午12點才開門.
  (Note: the substring 用手機轉帳 alone counts 3 in both edition and core
  because P8 Q129 reuses its first clause as a fill-in stem — the gate's
  full-sentence bare count is 2, matching the core KIT's method.)
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

### 11. Readers' corner — PASS
- Frozen Traditional disclosure line-for-line identical core vs edition
  (verified on the matching text nodes, incl. the full 延期披露 paragraph).
- Dutch disclosure present in the 5-line form: label
  `Voorbeeldbrief — geen echte.`, deferral (VOL.1 promised real letters +
  page-8 writing from this issue, nothing arrived), explicit open invitation
  ending verbatim `Stuur je brief in!`.
- W43 precedent note: W43's Dutch disclosure wording differs
  (`Voorbeeldbrief van de redactie — geen…`) because it is a different issue;
  the required elements (no genuine letters arrived + verbatim invitation) hold.
- Wording byte-identical to the pre-fix disclosure apart from geometry
  (see B1 section); geometry now passes (see B1 section).

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
  Nederlandse noot bij elk item` — byte-identical to the W43 shipped string;
  P8 right note `Alle noten in het Nederlands · ✓ = het modelantwoord`
  matches W43 form. No tables.json discrepancy arose (tables.json was not
  edited; shipped W43 wins wherever it matters, and it agrees).

### 13. Residual Latin — RENDERED-OUTPUT SWEEP — PASS
- Sweep of ALL **1,450** text nodes in the delivered SVGs (not just sources).
- Required counts, all exact: `算一算 · Work it out` = **0**,
  `算一算 · Reken uit` = **3** (P2, P3, P5; P3 card visually confirmed);
  `Baseball words` = **0** / `Honkbaltaal` = **1** (P4 title);
  `Deep-read quiz` = **0** / `Diep-leesquiz` = **1** (P6 head).
  Both late title fixes are present as `sub()` calls in the transform AND
  reproduced by the Gate 10 replay (byte-identical SVGs).
- English-phrase grep (19-phrase set incl. `Explanations in English`,
  `Quick quiz`, `Did you get it`, `Fill in`, `True or false`, `Answer keys`,
  `Model answer`, `Open task`, `Notes`, `Match`, `Writing`, `Over to you`,
  `Practice example`, `Read the chart`, `Work it out`, `Sentence frame`,
  `Readers' corner`, `Phrases of the week`, `Next week`): **all 0**.
- English-marker adjudication (own scan, all hits listed):
  ` the ` 3 = frozen theme line `Fintech Nexus: Bridging the World, Building
  the Future` + `Back to the Future` film title in a Dutch gloss;
  ` and ` 2 = proper name `Hong Kong Convention and Exhibition Centre`;
  `quiz` 3 = Dutch loanword (`Snelle quiz`, `De grote quiz`, `Diep-leesquiz`);
  `week` 24 = Dutch `week` + proper-name `FinTech Week` + footer `WEEKBLAD`;
  ` was ` 2 = Dutch verb (`was de wedstrijd voorbij`, `Ik was hier`);
  `halloween` 4, `festival` 11, `model` 4, `shows` 3, `fair`/`travel` 1 each,
  `centre` 2 / `center` 3 = Dutch words/compounds (`Staalsculptuurfestival`,
  `Zandsculptuurfestival`), Dutch loanwords, and venue/event proper names
  (`Taipei International Travel Fair (ITF)`, `Nangang Exhibition Center`).
  **Zero real English explanation prose.**
- Other legitimate survivals (adjudicated): frozen target-text proper names and
  theme strings, `Fintech`/`AI`/`AI+`/`Finance+` abbreviations, `NT$`, `VOL.2`,
  level chips A2/B1/B2, option letters, Dutch loanword `Frame:` in the P7 frame
  note, `體育 · Sport` (Dutch word identical to English, recorded not changed),
  all 4 Commons credit lines byte-identical.

### 14. Web regen — PASS (with the explicit timestamp exception)
- Cards **8/8 byte-identical** (gate10 render vs delivered).
- Print PDF **byte-identical** (SHA-256 `b6e3…b8f`, see §Pins).
- Web PDF: same size (3,395,098 B) and **content-identical except timestamp
  bytes, stated explicitly**: exactly 8 differing bytes in 2 spans, both the
  digits of `/CreationDate (D:…Z)` and `/ModDate (D:…Z)`
  (delivered `20261028093535Z` = delivery render time;
  gate10 `20261028094342Z` = replay render time). Every other byte identical.

### 15. Eyeball all 8 cards — ALL CLEAN (P7 FULLY re-eyeballed)
- P1: badge, masthead, harbour photo + Wilfredor credit, gloss boxes, footer —
  clean. P2: `Reken uit` head, 2-line Dutch question, champion-deals box,
  rain photo + CorraleH credit — clean. P3: `Reken uit` (visually confirmed),
  solar-term table, visit planner — clean. P4: `Honkbaltaal` title, runs chart
  with labels, team photo + Bain credit fully visible, caption uncovered —
  clean. P5: pumpkin photo + Balazs credit, `Reken uit`, schedule/stage boxes
  — clean. P6: `Diep-leesquiz` head, hours chart, AI+ gloss, price box — clean.
  P8: dash keys, `Pagina` separators, Dutch notes, F writing model + 138
  tekens, footer — clean.
- P7 FULLY re-eyeballed: A2/B1/B2 columns, error clinic, sentence frame,
  readers'-corner letter box (last line fully inside, clear space below,
  border touches no glyph — the B1 defect is gone), phrases strip with
  `(p. N)` tags + Dutch translations, teaser, footer — all clean.

### 16. ABSTRACT.txt — PASS
- Dutch single line (1 trailing newline), **0 ASCII double quotes**, 351 B.
- Contains: paper name (`Lucerna weekblad`), target language
  (`Traditioneel Chinees`), A2–B2, 150 exercises (`150 oefeningen`), learner
  search phrase (`Chinees leren lezen met Nederlandse uitleg`), and the real
  topic keywords — Hong Kong FinTech Week, Taipei International Travel Fair,
  Wei Chuan Dragons Taiwan Series title, Lidong, Kaohsiung steel festival,
  Fulong sand festival, Tianmu Halloween.
- Every named topic cross-checked against the zh-tw core's actual content
  (core contains 金融科技， 旅展， 龍隊， 立冬， 鋼雕， 沙雕， 天母） — **no topic
  outside the core**. ABSTRACT.txt untouched by the fix round (351 B,
  unchanged mtime), as claimed.

## Non-blocking observations (do NOT affect the verdict)

- **N1. P7 b2 column ends 1529 vs core 1496 (+1 line).** Within the 1560 nominal
  bottom, no warning, phrases rule far below (gold rule 1741.36). On the card
  the B2 column ends cleanly with no collision. Not a defect.
- **N2. P7 B1 head ink right 960.8 vs column edge 961 (fits by 0.2 px).**
  Same-baseline scan passes at 0; on the card the head
  (`B1 · 球賽與節氣 · Sport & seizoenen`) is fully inside its column and
  visually clean. Tight but passing; recorded, not a defect.
- **N3. Core's own P7 letter-box line (inherited behavior).** The core's last
  English disclosure line is struck through by its own letter-box border by
  the same mechanism (ink bottom 1756.38 vs expanded border 1746.06; center
  outside by 0.20 px, hence 0 audit flags). This is frozen core text and is
  recorded as non-blocking inherited behavior for the CORE. It does not excuse
  — and no longer parallels — the edition's Dutch line, which now clears its
  border by 12.13 px.
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
- The fixer's fix-round path in the task brief (`hidden_files/w45/zh-tw-nl-fix/`)
  does not exist; the actual fix products were found at
  `hidden_files/w45-zh-tw-nl-fix/` and used. No fix claim was taken on trust:
  every number above was re-measured from the delivered files.

## PDF pins re-verified (delivered files)

| file | bytes | SHA-256 |
|---|---|---|
| Lucerna-VOL2-NL.pdf (print) | 20,844,849 | b6e3a207b89626786a66e448b3badfb251691366e3c607c8d93057a5b1b97b8f |
| Lucerna-VOL2-NL-web.pdf (web) | 3,395,098 | 590e04aabf9f3724c54266d5ee89448b98e3caa9e6267316a51999193665ba90 |

Both match the coordinator-verified pins. Print PDF reproduced byte-identical
by Gate 10; web PDF content-identical except the 8 timestamp bytes (gate 14).

## Verdict restated

**PASS with ZERO PROBLEMS** — all 16 gates pass on the fixed render, including
the B1 letter-box fix verified by direct measurement (box bottom 1711.36,
last-line ink bottom 1699.23, clearance 12.13 px raw / 12.83 px vs expanded
border, border touches no glyph on the card) and Gate 10 reproduction at 8/8.
The first proof's single blocking item is closed. This report is the
finalization evidence for the coordinator's insert; nothing in this report
declares the edition shipped, and no insert, post, or delivery was performed
by this reproof.
