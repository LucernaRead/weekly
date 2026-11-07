# WEEKLY-KIT — W45 FR × ZH-TW (VOL.3)

Target language: French (frozen byte-for-byte). Reader native language:
Traditional Chinese, written natively — never converted from the
Simplified edition. Issue week: Mon 2026-11-02 – Sun 2026-11-08.
Masthead article: **Le** (French-only). 8 pages, **150 exercises**
(10 / 15 / 18 / 18 / 17 / 18 / 12 / 42), levels **A2 53 / B1 75 / B2 22**,
P8 model essay 86 words (range 80–100).

Build tree: `hidden_files/weekly-report-w45-fr-zh-tw-build/`
(`transform.py` single source + `checks.py` + `render.py` + `scratch/`).
Delivery dir: `files/weekly-report-w45-fr-zh-tw/`.

## 1. Single-source transform

- Pristine core build (never written to):
  `hidden_files/weekly-report-w45-fr-build/` (`content12/34/56/7/8.py`,
  `bslib4.py`, `svglib.py`, `assets/`).
- `transform.py`: line-based exact quoted-literal replacement
  (tools README #17 — never AST byte-offset splicing of UTF-8 source).
  Clean run: **265 map entries, 327 literal hits replaced**.
- Structural changes in `transform.py`: (a) OUT repoint in all 5 content
  files, core dir → edition dir, 1 occurrence each; (b) svglib SC→TC
  face, 4 sites (`_sc_index`→`_tc_index` ×2, `endswith("SC")`→`("TC")`,
  `Noto Serif CJK SC`→`TC`, `Noto Sans CJK SC`→`TC`); rendered SVGs
  carry `Noto Sans CJK TC` / `Noto Serif CJK TC`. (c) content8 P8 rule
  replaced by explicit `PRINT_NOTES` = the core's measured 97-set
  (list form in code) + half-width paren note style ` (note)`
  (W45 zh-tw column convention, cf. de-zh-tw / en-zh-tw builds; W43
  fr-zh-tw also used half-width P8 notes while keeping the P8 head's
  full-width `（第 1–8 版）`).
- Kept deliberately: all French text; shared-glyph literals; svglib
  line-120 docstring `Mountains, sun, two stick climbers, chrysanthemums
  — for 重阳` (library-internal, never rendered, W43 precedent);
  f-string page-line fragments (`第 {n} 版 / 共 {total} 版`,
  `— 第 {pg} 版 —`).
- Reproducibility proof (final `transform.py`, 2026-10-28): fresh core
  copy + `transform.py` → rendered SVGs **8/8 byte-identical** to
  delivered; transformed sources identical except the 5 OUT-redirect
  lines of the test harness (evidence `scratch/repro2/`).
  A docstring-only edit after round 2 was re-verified the same way
  (repro2); the delivered SVG hashes did not move.
- No other edition, `weekly-git`, or `tools/` was modified. No Discord
  post, no chat card/PDF dump, no cron, no shelving (coordinator owns
  shelving). The core web-PDF noise question is for the parent and is
  unrelated to this edition (see §10).

## 2. Rounds and baselines

- Round 1 (2026-10-28): full transform + one-process render, all gates
  run (see §3–§9 for values). Baselines: `scratch/round1-svg.hashes`
  (full hashes; `round1-svg.sha` listing is filenames only due to a
  `sed` that stripped hashes — superseded by the hashes file).
- Round 2 (2026-10-28): the three orphan trims (§8) folded into
  `transform.py`'s MAP, build files restored from the pristine core
  build, `transform.py` re-run cleanly, one-process re-render.
  Change scope r1→r2 verified by hash: **only p3, p4, p7 changed**;
  p1, p2, p5, p6, p8 byte-identical to round 1.
- Baseline files in `scratch/`: `cjk-inventory.txt`,
  `pristine-build.sha`, `core-p8-extract.json`, `freeze-diff-r1.json`,
  `freeze-diff-r2.json`, `p8-r1.json`, `p8-r2.json`,
  `keycompare-r1.json`, `occlusion-r1.json`, `checks-r1.txt`,
  `round1-svg.hashes`, `round2-svg.sha`, `webstreams/`, `pdftoppm/`.

## 3. Freeze gates (French target text)

- Core baseline reproduction: `tools/freeze.py baseline` on the core
  build = **8/8 byte-identical**; core SVGs re-hashed unchanged
  afterwards (first-16: p1 `f02e628efa06424c`, p2 `b192c1927b701fa0`,
  p3 `5f332e9f0106fa5d`, p4 `240f379d3a756fe0`, p5 `a4d64e3ef35a7459`,
  p6 `47e4346dba1f7cbc`, p7 `e997123f96cffdcd`, p8 `822dbe3d54d4ef06`).
- Pre-transform fidelity render (scratch only, OUT repointed):
  matched shipped core 8/8; the scratch fidelity dir was deleted.
- `tools/freeze.py diff` core vs edition (round 2, `freeze-diff-r2.json`):
  P1–P6 string counts equal (+N/−N identical) and per-page CJK totals
  identical (pure 1:1 glyph swaps). P7 CJK 390→410 (+20) = solicitation
  CJK +19, editorial-note delta −1, plus full-width `，` (+1) and `！`
  (+1) from the solicitation (freeze's CJK regex includes full-width
  forms). P8 freeze CJK 1030→840 (−190) = −194 full-width print parens
  (97 notes × 2, removed by the half-width style) + 4 from
  `三单`→`第三人稱單數`. Direct strict-CJK node count for P8 confirms
  788→792 (+4): no content lost. Latin-char multiset: P1–P6 identical,
  pure-Latin strings identical; P7 Latin diffs are exactly the
  solicitation/editorial changes (`VOL.4` +1, spaces +4, `，` +1, `！`
  +1, `8` +1 — the +4 spaces decompose as solicitation +3 and editorial
  `延至 VOL.4` +1); P8 Latin diffs are only `(`/`)` counts (19→116,
  the half-width style) and spaces from reflow.
- Round-2 CJK deltas vs round 1 (intended rewordings only): P3 −3,
  P4 +2, P7 −2 (§8).
- Frozen points (whitespace-normalized space-joined text, final SVGs):
  P4 `41e édition en 2026 (40e anniversaire)` = 1; whole-edition `40e`
  = 1 (only that site); P7 #4 comparatif
  `plus excitante ou plus frustrante ?` = 5 edition-wide (B1 column
  para + B1 example box + tools box + golden sentence + P4 debate box);
  P7 #8 sentence `Les jeunes créateurs y rencontrent leur public, en
  vrai.` = 1 on P7 (golden sentence only — the clinic key prints in
  P8, item 106 key verified as `Les jeunes créateurs y rencontrent
  leur public`); Q106 error `y rencontre leur public` = 1;
  P6 `Ce calendrier peut encore bouger.` = 1 on P6, 2 on P7 (B2 column
  para + example box), 0 on P8; Q120 stem
  `Si j'étais libre dimanche, j'___ à Nanterre.` = 1, word-boundary
  options `irai` = 1 / `irais` = 1, key B, P8 note in sync
  (`si + imparfait → conditionnel` + elision `j'`); neighbours
  Q119/Q121 untouched; P4 contains the comparatif; P7 French definition
  sentences present (`Reprendre, c'est recommencer`,
  `plus / moins / aussi + adjectif`) — only the explanation lines were
  localized, never the definition sentences.
- Chinese-string inventory of the pristine core build (tokenize-based):
  **311 distinct CJK literals, 422 occurrences** (content12: 63/88,
  content34: 88/119, content56: 77/104, content7: 32/39, content8: 69/69,
  bslib4: 2 string tokens + 1 f-string page line, svglib: 1 docstring).
  F-string CJK fragments (`第 {n} 版 / 共 {total} 版`,
  `— 第 {pg} 版 —`) are all shared glyphs and need no change.

## 4. P8 gates

- Plain `tools/p8.py compare` with explicit dual paths + `--total 150`
  (the `--target` form and the default total 149 are both forbidden:
  wrong P8 filename / wrong segmentation): **CLEAN, core 97 = edition
  97, missing=[], extra=0, keydiff=[135, 150]**.
- `hidden_files/w45/p8-fr-gap-fix/keycompare.py` full 150:
  **2 mismatches [135, 150], both noted on both sides** — bare-key
  mismatches = **0** (all 53 bare keys identical). Note: keycompare
  exits 1 on any mismatch by design; the gate is bare=0 plus
  item-by-item adjudication of noted diffs.
- Redirection table (measured, not copied from another edition):
  - 135: core key `读一份日程，本身就是在了解法国。` → edition
    `讀一份日程，本身就是在了解法國。` (noted both sides; the key
    sentence itself is the Traditional rendering).
  - 150: extracted key core `开放题` → edition `開放題` (noted both
    sides). Printed line 150 verified half-width both sides:
    `寫作框，範本在第 8 版寫作框內 (按要點給分)`.
  - 137 (non-diff explanation, required): its key is the frozen French
    sentence `Les élèves sont en vacances depuis le 17 octobre.` with
    a French-only note `être en vacances + depuis`, so it produces no
    keydiff. The neighbouring shared-glyph case is item 136's body
    `Traduisez: 他跑得比他哥哥更快。`, byte-identical in both scripts.
- P8 flow: battery ends y=1410 (bottom 1485); downstream section
  geometry identical to core (MODÈLE y=1538.0, RÉPONSES head y=1838.0
  in both); keys ends y=2046
  (bottom 2545; core 2167 — shorter due to half-width parens).
  Max 15.5 px baseline 2539.19 (= core 2539.19), footer rule 2580,
  gap **40.81 px**.
- P8 keys-only line spacing (exact-column method, 15.5 px nodes,
  columns x=65/527/989/1451 with 22/24/30/8 lines = 84 lines):
  modal gap **20.15 px**; 73/80 gaps exactly 20.15; the 7 other gaps are
  **86.41 px** section transitions (`— 第 N 版 —` boundaries) —
  identical in count and value to core's 7 × 86.41 (core columns
  22/24/30/14). The earlier mixed-column measurement (min 1.46) was a
  binning error and is discarded.

## 5. Traditional-independence gates

- Explanation layer written directly in Traditional Chinese; no
  Simplified→Traditional conversion step exists in the pipeline
  (transform maps Simplified core literals to independently authored
  Traditional values; the mapping is a localization table, not a
  converter pass).
- Charset cross-check (SVG-only walk, final SVGs): edition **513**
  chars, W43 fr-zh-tw **526**, zh-tw core **786**, **86 NEW chars**
  (in the edition but in neither reference set):
  `仍付代傾儀其冕刊刺協印口否嚐土媒室審布師底廳徽怪恐恰悉愉感慄慣懼扇扮拭揭擬故敘斜曉曲曼材梭椅泰淆漫激濟熟產皆盤研硬科穩絕耶聆致興舞萊虛衛被該認諾謂貝負財跳迎逆院雜靜頁顏餘驅`.
  Each is a standard Traditional form from new W45 content (e.g.
  決賽-week vocabulary, 預算-week vocabulary); none is a
  Simplified-only form. (A non-SVG walk that also read PNG/PDF bytes
  inflated the reference sets to 18536/19759 and is discarded;
  the SVG-only walk reproduces the round-1 86 exactly.)
- OpenCC `s2twp` single-char scan over all 513 distinct CJK chars in
  the edition: only flag is **`台`**, adjudicated as a converter false
  positive — it occurs only in `看台` (P4 `tribunes 看台。`) and `舞台`
  (P8 `scène=舞台 b`), both correct Taiwan forms that never take `臺`.
  Cross-check: `台` is present in the zh-tw core charset (True) though
  absent from W43 fr-zh-tw (False).
- Mainland-word scan: **NONE** found for 视频, 屏幕, 网络, 软件, 信息,
  邮件, 博客, 鼠标, 键盘, 光盘, 打印, 质量, 节目, 动画, 元音, 三单,
  范文, 示例, 邮局, 邮寄, 发廊, 头发, 干活, 谷物, 咸菜, 土豆, 西红柿,
  黄瓜, 菠菜, 草莓, 樱桃. Taiwan usages applied in the mapping include:
  `線上`/`線下`, `資訊` (演出資訊), `計畫` (not 计划), `母音` (not 元音),
  `第三人稱單數` (not 三单), `範本` (not 范文), `範例` (not 示例),
  `賽季` for the P4 tennis indoor season (recorded decision: Taiwan
  sports general term; W43's `球季` precedent was a team-sport-season
  context), `籤表` for 签表, `戰慄` for 战栗, `在哪裡` (裡), `品嚐`,
  `日曆`. No 影片-family word occurs in the core, so no such mapping
  was needed; `螢幕`-family and `時鐘`-family are n/a.
- The dropped intermediary term appears **nowhere** in the delivered
  paper (SVGs + ABSTRACT.txt, one-off grep: 0) or in build code
  (`transform.py` / `checks.py` / `render.py`, grep: 0). Two
  self-references found in round-2 verification (a transform.py
  docstring sentence and a checks.py scan-list entry) were removed;
  the term's absence is verified by one-off grep, not by a literal
  inside build code, so that the build code itself stays clean.
  (The KIT phrases this without spelling the term, for the same reason.)
- Gloss: render-level gloss-prefix line counts equal core on every page
  (p1 1, p2 2, p3 1, p4 2, p5 1, p6 2, p7 0, p8 0); source-level item
  counts split on `·` (README #21) equal core for all 9 gloss/`譯注`
  strings (7, 6, 3, 6, 7, 3, 6, 6, 3). The brief's gloss 38 = the 6 main
  vocab boxes (7+6+6+7+6+6); the three 3-item `譯注` boxes add 9,
  total 47 — consistent.
- Quote-char counts per page: **NONE differ** core vs edition
  (all of `«»「」“”‘’'"`).
- P8 notes, gloss, column heads, footers, reader's-corner disclosure:
  all Traditional (see §6–§7).

## 6. Furniture — three-way (W43 shipped vs W45 core vs this edition)

- Badge: W43 `法語正文 · 繁體中文講解 — 給繁體中文讀者的版本` =
  edition badge, identical. Core:
  `法语正文 · 简体中文讲解 — 给简体中文读者的版本`. Slot follows the
  FR-family precedent (not the EN-core subtitle-slot form): **inserted
  at y=574, 22pt BRICK, centred**, between the dark band and the
  headline kicker.
- Footer: W43 `Le Lucerna · 法語週報 VOL.2 · 正文法語 · 講解繁體中文`;
  edition `Le Lucerna · 法語週報 VOL.3 · 正文法語 · 講解繁體中文`;
  core is the Simplified counterpart. Page line
  `第 N 版 / 共 8 版` is shared-glyph identical in all three.
- Gloss prefix `譯注｜` (W43 and edition; core `译注｜`).
- P8 separator `— 第 N 版 —` shared. P8 head keeps full-width
  `（第 1–8 版）`; P8 printed notes use half-width parens (see §1c).
- Band heads (French + Traditional bilingual, same pattern as W43):
  P1 `VOL. 3 · 總第 3 期`, P2 `VIE QUOTIDIENNE · 生活`,
  P3 `CULTURE · 文化`, P4 `SPORT · 體育`,
  P5 `JEUNESSE & MUSIQUE · 青年`,
  P6 `POLITIQUE & CHIFFRES · 時事`, P7 `LANGUE EN MAIN · 精講`,
  P8 `EXERCICES & RÉPONSES · 練習與答案`.
  Section heads follow the same French + Traditional pattern, e.g.
  `À VOUS ! · 即學即練`, `LE DÉBAT · 討論`, `LES MOTS · 詞彙`,
  `LE COURRIER DES LECTEURS · 讀者園地`,
  `LA SEMAINE PROCHAINE · VOL.4 下週預告`.
- Section-head tabulation method: freeze-diff added strings (§3) list
  every head's Traditional form against its Simplified removed
  counterpart, 1:1.

## 7. Reader's corner (P7, verified in rendered card)

- Editorial example labelled: French
  `Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)`
  (frozen) + Traditional `小墨點評｜編輯部範例：…`.
- Three-fact disclosure, all printed in the reader's corner: (a) no real
  letters, (b) no VOL.2 page-8 submissions, (c) both deferred to VOL.4 —
  via the frozen French note `Note de la rédaction: aucun texte du
  VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44
  n'a pas paru). Le VOL.4 reprendra la promesse.` plus the
  strengthened Traditional note (see below). No fabrication: the
  strengthened wording renders the French note's `aucun texte` scope;
  W44-not-published and VOL.4-deferral are core facts.
- Traditional comment para (2 lines, ends y=2094, French note at
  y=2142, no collision):
  `小墨點評｜編輯部範例：週末敘事用 passé composé 很穩，分號連接兩天值得學。下期讀者園地將點評真實投稿。請把你的來信和最棒的第 8 版作文寄給我們，VOL.4 見！`
  — the final sentence is the explicit imperative solicitation literally
  covering **both** letters and best page-8 texts (FR×NL precedent,
  same slot). The VOL.4 preview line `還有你們的來信！` is explicitly
  NOT counted as the solicitation.
- Traditional editorial note (2 lines, ends y=2233.3, box bottom 2258):
  `編輯部說明：截至付印，編輯部尚未收到真實來信與 VOL.2 第 8 版投稿作文（W44 未出刊），故本期刊登標註明確的編輯部範例；兩者皆延至 VOL.4 點評。`
  (Core Simplified note named only the VOL.2 p8 submissions; the
  edition names both facts explicitly, rendering the frozen French
  `aucun texte`.)
- VOL.4 preview line:
  `下週：參議院審議社保預算、11 月 11 日停戰紀念日、迪耶普扇貝集市；還有你們的來信！`
  (single line at y=2466).

## 8. Geometry gates

- Canonical `tools/occlusion_audit.py` (selftest passed, all 6 planted
  classes fired once, clean controls silent): **edition 0 flags, core 0
  flags, NEW vs core 0** (round 2, final SVGs).
- Same-baseline ink spacing: P1 top y=92 gaps [387.5, 196.2], all
  footers y=2624 gap [1157.1], no overlaps (P1 unchanged r1→r2).
- Right-edge scan: 11 flags, **all proven inherited** — core shows
  byte-identical values: footer page lines ink_right 1885.074
  (0.074 px sub-pixel rounding at the right margin, not a page-edge
  breach) and P8 matching right-column French lines adv/ink ends
  1891.2 / 1891.3 / 1899.5 (frozen French, still on-page within 1950).
- P6 chart-label check: P6 calendar is a text-row table, not bars;
  the box rect is drawn before the labels. Worst later-rect ink
  coverage on P6 = **0.000, gate <0.30 PASS** (P6 unchanged r1→r2).
- Orphan scan (window 10–45, all lines scanned — a superset of the
  window, so coverage is compliant). Round-2 final:
  P1 0, P2 1, P3 0, P4 0, P5 0, P6 0, P7 0, P8 4.
  - P2's `、`-led line (`、反之 · un rituel 習慣、儀式。`) is an
    inherited separator-led wrap: core shows the same line at the same
    y (same class as W43's accepted `·`-led lines). **Kept, not fixed.**
  - P8's 4 flags are structural joined key-flow wrap splits
    (open-paren-ended lines, one `。`-led line from the frozen 135 key
    sentence `讀一份日程，本身就是在了解法國。`, whose wording cannot
    change because it is the answer key). Same defect class as core's
    8 flags, fewer in count; fixing would require changing frozen keys
    or flow parameters. **Kept, with this rationale.**
  - Round-2 fixes (all folded into `transform.py`'s MAP, never as
    post-edits to build files; each verified by full one-process
    re-render before folding):
    | Page | Before (core Simplified) | After (edition) | Effect |
    |---|---|---|---|
    | P3 | `改写句子（用 ne...jamais / ne...plus / ne...pas）。` | `改寫（ne...jamais / ne...plus / ne...pas）。` | −3 chars (W43 remedy verbatim); lone `）。` line gone, single line at y=1024.65 |
    | P7 | `语法点｜reprendre：复课、重新开始（pause 后）。` | `語法點｜reprendre：復課、重開（pause 後）。` | −2 chars (`重新開始`→`重開`); single line at y=1319.1. Trade-off recorded: `重開` is the shorter resume-verb; the column para above carries the full French definition, so no meaning is lost. Candidates B (reorder, predicted `始。` tail) and C (drop `(pause 後)`, loses gloss) were rejected. |
    | P4 | `事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。` | `事先不知道決賽選手，到底是更刺激還是更掃興？寫兩句支持、兩句反對。` | +2 chars (`到底`); `？` now mid-line (`掃興？寫兩句支持、兩句反對。` at y=2384.40) |
  - Round-1 orphan state for reference: P1 0, P2 1, P3 1, P4 1, P5 0,
    P6 0, P7 1, P8 4; core at identical positions: P2 1, P3 1, P4 1,
    P7 1, P8 8. The three fixed lines were explanation-layer text, not
    French and not keys, so rewording was allowed (W43 precedent: the
    fan-out fixed its core's orphans by ±1–3 char rewording).
- All 8 cards visually inspected (1950×2700): no overflow, no overlap,
  no footer intrusion, images + credits placed, reader's-corner box
  fits. Gate outputs were not truncated.

## 9. Images (only the core's 3, all verified public domain)

- Base64-embedded, same payload as core. Dual-diameter (decoded JPEG
  sha256, first 16 hex): P1 `f3705af28f175ce4`, P2 `5b772facb5db886c`,
  P3 `be071fdae81a71b4` — edition = core, 1 payload each on P1/P2/P3,
  0 payloads on P4–P8 in both. (Payload extraction uses the SVG2
  `href="data:image/jpeg;base64,..."` attribute; an `xlink:href`-only
  pattern returns empty and is a measurement error, not a missing
  image.)
- Credits are the Commons Artist originals, placed via `caption()` in
  the code and verified in SVG text and on cards:
  P1 `Eugène Atget (1857-1927), photographie, domaine public`;
  P2 `Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA`;
  P3 `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle,
  domaine public`.

## 10. Cards + dual PDFs + web-PDF verification

- Recipe (`render.py`, venv): cairosvg svg2png @1950 → cards
  1950×2700 PNG ×8; cairosvg svg2pdf + pypdf merge → print PDF;
  cards → PIL PDF save directly (no explicit quality → Pillow default,
  empirically q75; see below) → web PDF, fresh from THIS edition's
  cards, never from the core's web PDF.
- q72/q75 measured conclusion: **default quality = q75** — web-PDF
  embedded JPEG streams (pdfimages extraction, pg-000…pg-007) match
  fresh-card q75 encodings **8/8 byte-for-byte** (stream bytes:
  p1 658098 / p2 641018 / p3 591503 / p4 638917 / p5 531567 /
  p6 562228 / p7 638347 / p8 827682; sha16: p1 `7fa564565ca712ac`,
  p2 `ee05e06d98ca1c2c`, p3 `361bd685faf26c37`, p4 `3436c39afd15a085`,
  p5 `a03954ae4054623d`, p6 `cbec4836e7eecc10`, p7 `398215ea7335fc67`,
  p8 `bae851367e543969`) and differ from q72 encodings 8/8. Hence the
  streams are fresh card encodings; the core web PDF's old-noise root
  (streams not from fresh cards) does not apply here.
- pdftoppm -r 150 per-page render (1950×2700, same as cards): 8 pages,
  mean RGB all paper tones (p1 (219.6,214.2,199.3) /
  p2 (226.9,221.4,205.8) / p3 (230.1,224.6,209.1) /
  p4 (229.7,224.1,208.3) / p5 (232.5,227.0,211.6) /
  p6 (231.9,226.2,210.9) / p7 (222.0,216.7,201.5) /
  p8 (227.2,221.6,205.9)); 195×270 downsample vs cards mean abs diff
  p1–p8 = 1.521 / 1.404 / 1.339 / 1.354 / 1.224 / 1.282 / 1.462 / 1.595 —
  all ~1 magnitude (**noise pages would be ~100 magnitude**). 8 pages
  all clean, no noise page.
- Print PDF p1 downsample对照 (pdftoppm vs card): mean abs diff 1.499,
  same clean magnitude.
- Toolchain: run.py (one-process SVG render) and render.py (cairosvg)
  both used `tools/venv/bin/python` = **Python 3.12.3, Pillow 13.0.0**
  (system python3 is also 3.12.3 but Pillow 10.2.0 and lacks cairosvg,
  so it cannot run render.py). Family baseline SVG byte-reproduction
  8/8 proved in §3.

## 11. Delivery pins

| File | Bytes | SHA-256 |
|---|---|---|
| svg/p1-une.svg | 475009 | e4ed3e3818a2fc720ff9209cb1f43f2b027427e56f150a111eeb1c6f97248d84 |
| svg/p2-vie.svg | 890923 | 80316ad9f39474dda0c959792d413fce6a6467318926be0fc6fc45616879dbd4 |
| svg/p3-culture.svg | 220438 | d1b6fc159e8ac661e5e7b015b58971442f8293f0f107b317cb543035e79269cd |
| svg/p4-sport.svg | 32517 | 1c8376b3c9d1ece7f4f346be1c5699c829ce5a381a2b9ffbf514f7bfc4ec1571 |
| svg/p5-jeunesse.svg | 26107 | bf0dfac60b28764e0ff613742f56dfc31d7c74586020ae98997455dce4dadd99 |
| svg/p6-politique.svg | 28537 | ab31d91c07a1aae38b1e96b2d05d3425a8c46cb96913434ab3b86d54cbfe9da7 |
| svg/p7-langue.svg | 29290 | f0ae1cf7a6c7f6ae3ae0b09717da54e0fb925fb8cf1f7907ebc1be7822da51ab |
| svg/p8-exercices.svg | 45133 | ccc82fccf1de71f566d5461c3de4d77bd1e52ba1f0e890549f4e0c93ed127b81 |
| cards/p1-une.png | 1102598 | c5957d869ba9d8093fbc5b091b2eeacd8b528ee1bbb77958ed2608079818c337 |
| cards/p2-vie.png | 1233577 | 6cbef4deac9cda606efabe80b95ea234ca0a00eae8207300528d8d9a94661fe5 |
| cards/p3-culture.png | 964009 | 5a1ea67387980eef37771274cd43e12bce4c27406633f7ad8217371c3237b40a |
| cards/p4-sport.png | 894708 | 2eecaa84609e3e8d26473e0685dfe165e799aea8ab3a94acca5d5a44eec1ad54 |
| cards/p5-jeunesse.png | 730986 | 3e0db124d4cd3f4410fe6eeea7812e9e740e8bf9dfa9e9c525c68345ee504428 |
| cards/p6-politique.png | 780816 | 21dccd950ea032ce748ab819c57a276b6e5d49c4c4b465d9fac3d4cc2835c5e0 |
| cards/p7-langue.png | 814764 | 7e9e55c80d9a3254077d3923d7b112a86b5ffb1ea2cc069e059981035c77c02c |
| cards/p8-exercices.png | 1273339 | 073fd94fcb38cbd04403b455d944a2d1877beb72ab88af4e51d12a1d1e101991 |
| Le-Lucerna-VOL3-ZHTW.pdf | 23611048 | b1ed9e6aa7f8ccd8569bf04b30571f35daa1e6727aa61f54900b464fdd88315a |
| Le-Lucerna-VOL3-ZHTW-web.pdf | 5093804 | 0b3501aeedec53c809870c3161ac0216ed74abca0b75dfd1d585782f1c834d49 |
| ABSTRACT.txt | 337 | 03f55a191b2b75a439ffb0a1f3eb786bf34dc4a74910b13ae93066d1f906830b |

- Print PDF: 8 pages, 1462.5 × 2025 pts. Web PDF: 8 pages,
  Title `Le-Lucerna-VOL3-ZHTW-web`.
- ABSTRACT.txt: Traditional Chinese, single line, no ASCII double
  quotes, real topic keywords (開學復課、巴黎大師賽決賽週末、萬聖節與
  諸聖節、Pitchfork 巴黎音樂節、2027 社保預算國會審議) + learner
  search phrase (用法語讀真實生活) + masthead (法語週報 VOL.3) +
  levels (A2 到 B2) + exercise count (150).

## 12. Final verification pass (2026-10-28)

- Delivery dir contains exactly: svg×8, cards×8, print PDF, web PDF,
  `WEEKLY-KIT.md`, `ABSTRACT.txt`. No other files.
- Core SVGs re-hashed unchanged vs §3 baseline (8/8 first-16 match).
- No other edition, `weekly-git`, or `tools/` modified.
- Dropped-term grep: 0 in delivered SVGs + ABSTRACT.txt, 0 in build
  code (`transform.py` / `checks.py` / `render.py` / `scratch/`).
- This report does not declare finalization; finalization is for
  independent proofreading.
