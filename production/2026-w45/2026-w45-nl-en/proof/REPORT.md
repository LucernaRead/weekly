# INDEPENDENT PROOFREAD REPORT — Lucerna Weekly W45, NL × EN (De Lucerna VOL.2)

## CONCLUSION: ZERO PROBLEMS — 可定稿

Independent re-measurement from the rendered SVGs/cards/PDFs (builder claims
never taken on trust; every gate below was re-run by the proofreader).
No Discord post, no chat card/PDF dump, no cron, no weekly-git touch, no
core/W43 modification, no subagent spawned. Nothing was edited in the
edition, core, or W43 directories; proof artifacts only in this directory
(`hidden_files/w45/nl-en-proof/`).

## 0. 开工查重 (stand-down check)

- No rendering/build process was writing to `files/weekly-report-w45-nl-en/`
  or `hidden_files/weekly-report-w45-nl-en-build/` at task start (only an
  unrelated de-ja proofread process was running; it touches neither dir).
- The fresh mtimes (WEEKLY-KIT.md 21:17 UTC, final-sha256.txt 21:17 UTC)
  were a completed delivery: a 90-second recheck showed zero new writes
  (mtimes unchanged through the wait), so work proceeded per the task rule.

## 1. Freeze — PASS

- `tools/freeze.py baseline` on the W45 NL core build, re-run by the
  proofreader: **8/8 SVGs byte-identical** to the shipped core, and the
  shipped core re-hashed unchanged afterwards (before/after hash files
  identical, re-verified again at the end of this proofread).
- `tools/freeze.py diff` core-vs-edition: added CJK **0 on every page**,
  edition CJK total **0** (core per-page CJK 191/212/153/126/214/192/373/1033
  → edition 0); full-text banned-term scan: **桥接 = 0** on all 8 SVGs.
- Removed-string adjudication (full list in `freeze-diff-nocjk.txt`):
  every removed string is explanation layer (Chinese notes/glosses/
  instructions), furniture (footer, page line, section heads, P1 strapline
  at y=372, P1 subtitle at y=330), or a re-aimed translation item.
  The only removed strings without CJK are individually adjudicated:
  P1 strapline (furniture, replaced in place by the badge); P6 lone `）`
  (fragment of a wrapped Chinese note); P7 fragments `bomen。/thuis。/
  zij zette vast。/。` (fragments of Chinese clinic-note lines quoting
  Dutch examples — explanation layer, not frozen article text); P8
  `104. blijf — rood = blijf binnen`, `6. planten — veel mensen → planten`,
  `voorgelezen` (answer-note fragments; keys blijf/planten unchanged in
  the edition). No Dutch article, exercise body, option, fact, or figure
  differs. No frozen Dutch text was deleted or altered.

## 2. 核心层冻结专项 (P7 词框定义句) — PASS

Core P7 HET WOORD box (the NL×ZH-CN core, i.e. the Chinese-noted core in
`files/weekly-report-w45-nl-core/`) target-language definition sentence,
verbatim:

> «meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet
> heel Nederland mee.

Edition P7 HET WOORD box: the same three lines **byte-identical**
(only the y position moved 1101→1042 as part of the shortened col-3
stack — layout, not text). Only the gloss line was localized:
core `meedoen = 参加、参与：气候周全荷兰都参/加。` →
edition `meedoen = to take part.` No definition sentence was deleted,
rewritten, or translated into English. Standing de-nl ruling satisfied.
Core-vs-edition对照: definition sentence identical; gloss localized only.

## 3. P8 — PASS (compare CLEAN 150=150)

- `tools/p8.py compare` re-run: core **150 noted**, edition **150 noted**,
  status **CLEAN**, missing [] extra 0 uncertain [], keydiff exactly
  **[7, 17, 70, 71, 76, 96, 137, 138, 148]**.
- Artifact claim independently verified against the printed P8 lines in
  both SVGs (first segment of each printed line, before ` — `):
  7 → `B` = `B`; 17 → `wortelen` = `wortelen`; 70 → `eiland` = `eiland`;
  71 → `proef` = `proef`; 76 → `gaat winnen` = `gaat winnen`;
  96 → `advies` = `advies`; 148 → `B` = `B`. All seven are genuine
  p8.py paren-branch artifacts (the translated note ends in a
  parenthetical, e.g. `wortelen = to take root (plural subject)`,
  `eiland = island (het)`, `zachte = soft (soil)`), not key changes.
  **Artifact claim TRUE on all 7.**
- Genuine re-aims: 137 core `气候周持续七天。` → edition
  `The Climate Week lasts seven days.`; 138 core
  `橙色预警意味着：做好准备。` → edition
  `Code orange means: be prepared.` Both are translation items re-aimed
  Dutch→English, legitimate per the W43 NL×EN precedent (P8 section E
  headers confirm: 137/138 `Translate into English`, 139/140
  `Translate into Dutch`).
- 139/140 keys byte-identical Dutch in both versions
  (`Museumnacht duurt van 19:00 uur tot 02:00 uur.`,
  `Ik doe mee aan de Klimaatweek.`), correctly absent from keydiff.
  Item 150 is apparatus only (`✓ See the model text in section H
  (87 words)`); the 87-word Dutch model text itself is byte-identical
  (recounted: **87 words**, in range 80–100).
- P8 pagination from separators, identical both versions:
  10/18/18/18/18/18/12/38, continuous 1–150.

## 4. 几何遮挡审计 — PASS

- `tools/occlusion_audit.py` (selftest OK, all 6 planted classes fired):
  edition **0 flags**, core **0 flags**, NEW vs core **0**.
- Same-baseline ink-collision scan (independent implementation, PIL
  baseline-anchored ink, all 8 edition pages): **0 flags on every page**.
- P6 chart-label coverage, measured with the CORRECT method
  (baseline-anchored ink: PIL mask render with anchor `ls`, i.e. ink
  measured relative to the SVG baseline, plus getmetrics cross-check):
  all 9 chart texts (title + 4 category labels + 4 values) vs every
  later-drawn bar: **worst coverage 0.00%**. Label ink bottoms
  299.2/357.2/415.0/468.2 vs bar tops 304/362/420/478 — gaps
  4.8/4.8/5.0/9.8 px; labels sit above their bars.
- The builder's method-error explanation was verified, not copied: the
  naive default-anchor `getbbox` box for `Ik blijf thuis` gives a
  baseline-relative bottom of 321.8 (bar top 304) — a false overlap —
  because that box is ascender-relative (ascent 22.5 px at this size);
  the correct baseline-anchored bottom is 299.2. The mechanism and
  direction of the claimed bug are confirmed by measurement; the
  correct-method result is 0.0%.
- Process note: my first chart scan used a regex element walk that
  swallowed some texts after `<rect/>` elements; it was discarded and
  redone with a proper XML parse covering all 9 chart texts
  (`chart-coverage2.txt`). The canonical audit result (0) never depended
  on that scan.
- Card visual check (below) confirms the P6 chart labels are visibly
  above the bars with no压盖.

## 5. Gloss — PASS (core 1:1, split on ·)

Rendered gloss strings, joined across wrapped lines, split on `·` itself
(README #21 method), headwords in identical order:
P2 **6 = 6** (klimaat/wortelen/besparen/verwarming/waarschuwing/lokaal),
P3 **5 = 5** (museum/rondleiding/tijdslot/tweedehands/beurs),
P4 **5 = 5** (balans/gelijkspelen/speelronde/topper/stand),
P5 **5 = 5** (eiland/proef/stemmen/aflevering/voorbij),
P6 **5 = 5** (meteoroloog/waarschuwingsmoeheid/vastzetten/advies/
voorstander). Gloss prefix `Note | ` matches the shipped W43 NL×EN form.

## 6. P7 金句 — PASS

All 8 Dutch sentences occur **exactly 2×** in the edition (space-joined
whole-issue text): once on the tagged article page, once on P7, verbatim
(no period inside the P7 guillemets; article occurrence carries the
sentence-final period — same sentence). Page tags identical to the core,
in article-page order: **Pagina 1, 1, 2, 3, 4, 5, 6, 6**
(Klimaatweek→1, herfst→1, geel→2, musea→3, Ajax→4, Robinson→5,
code→6, weer→6). Each sentence was confirmed present on its tagged page.

## 7. 读者园地 — PASS (no fabrication; explicit invitation; bilingual)

P7 BRIEVEN VAN LEZERS box, verified line by line against the core:
- Example letter Dutch text **verbatim from the core**:
  `«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de
  Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief
  van de redactie)` — labeled editor's example, not a real reader.
- Dutch disclosure **verbatim from the core**:
  `Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen —
  daarom dit voorbeeld; belofte naar VOL.3.`
- English explanation layer (not frozen core, not mistaken for it):
  `No real letters or best page-8 texts yet — hence this example;
  promise carries to VOL.3.`
- All three facts are on the page, in both Dutch and English:
  (1) no real letters arrived, (2) no best page-8 texts arrived,
  (3) the example stands with the promise carried to VOL.3.
- Explicit English public invitation, judged on its own wording
  (imperative + publication promise, not the VOLGENDE WEEK preview line
  and not any exercise prompt):
  `Editors' example — not real. Send your real letters and best
  page-8 texts: we will print them in VOL.3!`
  **Judgment: this is an explicit invitation.** No reader, letter, name,
  or quote was invented.

## 8. 家具三方对照 — PASS (W43实测胜过 README #20 泛写)

- Pairing badge, edition P1 vs shipped W43 NL×EN P1 SVG, attribute for
  attribute: string `TEXT IN DUTCH · EXPLANATIONS IN ENGLISH — THE
  EDITION FOR ENGLISH-SPEAKING READERS`, x=975, y=372, 20 pt, weight 700,
  fill #3e4c2a, anchor middle, Noto Sans CJK SC — **identical**.
  Measured advance width 941.7 px (≈ builder's 941.8, rounding).
  The badge replaces the core's Dutch strapline at y=372 in place
  (core y=372: `DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — …`);
  no masthead shift; frozen elements below y=606 unmoved. This is the
  NL-family case (native subtitle slot at y=330, strapline slot at
  y=372), not a generic README #20 value.
- Footers **8/8**: `De Lucerna · VOL.2 · Dutch text · English
  explanations · LUCERNA DUTCH WEEKLY` at baseline 2624 with
  `Page n of 8` (n = 1–8) — the W43 form with VOL.1 → VOL.2.
- Masthead `De Lucerna` identical to W43 and core (x=975, y=262,
  168 pt UnifrakturMaguntia).
- Page level headers match the core structure with English third
  segments (A2 / A2→B1 / B1 / B1 / B2 on P2–P6).

## 9. PDF/卡片 — PASS

- Print PDF `De-Lucerna-VOL2-EN.pdf`: **8 pages**,
  7,877,914 bytes, sha256
  b934f9010adf72618a98a3a9272a18dd4aa22dc1f19bdd88ca1d37784fd88b2f —
  matches KIT §11.
- Web PDF `De-Lucerna-VOL2-EN-web.pdf`: **8 pages**,
  3,610,480 bytes, sha256
  fe96959f638401a8c709c6e213179e1a885ab8a0d4287131f33a5bd30d63a7fb —
  matches KIT §11, under 10 MB.
- All 8 SVG hashes and all 8 card hashes match KIT §11 exactly;
  all 8 cards are 1950×2700.
- All 8 cards viewed page by page: **no overlaps, no cut-off text**,
  including the P1 agenda/word-note area, the P2 match set, the P6 chart
  (labels visibly above bars), the P7 col-3 stack (ends clear of the
  phrases rule), and the P8 key-block foot (clear of the footer rule).
- 150 exercises, pagination 10/18/18/18/18/18/12/38, level headers as
  §8; level distribution inherits the frozen core's measured
  A2 47 / B1 72 / B2 31 (Dutch bodies and numbering frozen per §1;
  no exercise added, removed, or re-leveled).
- ABSTRACT.txt: **English, single line, 0 ASCII double quotes**,
  375 chars: names the masthead (De Lucerna), VOL.2, real topic
  keywords (Netherlands Climate Week 2–8 November, Museumnacht
  Amsterdam 7 November with 70+ museums, Eredivisie matchday 12 with
  Twente–Ajax and Heerenveen–Feyenoord, Expeditie Robinson, KNMI
  weather codes), A2–B2, 150 exercises, and a learner search phrase
  (`learn Dutch by reading real Dutch news`).
- Image credits typeset on their pages, identical to core KIT §5:
  P1 `Foto: Vovogov90 — CC0`; P2 `Foto: Nationaal Archief — CC0`;
  P3 `Foto: W. Punt / Anefo, Nationaal Archief — CC0`;
  P4 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein`
  (wrapped over two lines). Image counts match the core page by page
  (1 each on P1–P4, 0 on P5–P8).

## 问题清单

无。No blocking or minor problems found. All nine gates pass on
independent re-measurement.

## 交回说明

- 结论：**ZERO PROBLEMS，可定稿**（定稿≠上架；上架由协调员串行执行，
  本报告不宣称上架）。
- 证明文件：本目录下 `freeze-diff.json`, `freeze-diff-nocjk.txt`,
  `occlusion-edition.txt`, `occlusion-core.txt`, `occlusion-new.txt`,
  `p8-compare.txt`, `p8-core.json`, `p8-ed.json`,
  `chart-coverage2.txt`, `rowcheck.txt`,
  `core-sha256-before.txt`, `core-sha256-after.txt`,
  `baseline-nl-core/`（freeze 基线复现产物）。
