# INDEPENDENT PROOFREAD — W45 FR × ZH-TW (VOL.3)

**Verdict: ZERO PROBLEMS — edition passes all 11 mandatory gates. No blocking items.**
This report does NOT declare the edition shipped; the coordinator inserts it.

- Edition: French target (frozen) × Traditional Chinese reader, issue week Mon 2026-11-02 – Sun 2026-11-08.
- Delivery dir: `files/weekly-report-w45-fr-zh-tw/` (svg×8, cards×8, print PDF, web PDF, WEEKLY-KIT.md, ABSTRACT.txt).
- Proof work dir: `hidden_files/w45/fr-zh-tw-proof/work/` (all scripts, logs, JSONs, repro, webregen).
- Tools: `tools/venv/bin/python` = Python 3.12.3, Pillow 13.0.0. SOP + tools README notes #7–#22 read before starting.
- Builder claims were read from LEDGER.md ("fr-zh-tw BUILDER-COMPLETE") and the edition KIT, then verified independently item by item — nothing below rests on a builder claim alone. Where a builder number did NOT reproduce (KIT charset NEW count), it is reported in Non-blocking observations, and the gate conclusion rests on my own recomputation.

## Pre-flight (duplicate check)

- At start (2026-10-28 06:59 UTC): no live fr-zh-tw process (`ps` clean). The only live worker was the fr-ru `insert.py` (different edition dir + weekly-git); it never touched fr-zh-tw dirs.
- Last fr-zh-tw writes were the builder's finalization (delivery KIT 06:52, build scratch 06:49–06:58 UTC) before the 06:58 UTC dispatch — a finished run, not a moving target. Per the brief's "judge by CURRENT activity" note, I proceeded (did NOT stand down) and compensated with hash stability: delivery hashes at start vs end are identical for all 20 files (only the printed path prefix differed between the two hash runs), and core hashes are identical start-to-end.
- I did NOT spawn any subagent; did NOT touch `weekly-git`, `insert.py`, Discord, main-chat cards/PDFs, crons, shared scratch, the core build, the W43 shipped edition, `tools/`, or the delivery dir. All writes are in my own proof dir + scratch.

## Gate 1 — Freeze baseline + diff: PASS

- `freeze.py baseline --build hidden_files/weekly-report-w45-fr-build --core-svg files/weekly-report-w45-fr-core/svg --out <proof>/work/freeze-baseline`: **8/8 SVGs byte-identical** (p1 `f02e628efa06424c` … p8 `822dbe3d54d4ef06`, matching KIT §3 first-16). Core SVGs re-hashed unchanged afterwards (also unchanged start-to-end of this whole proof).
- `freeze.py diff` core vs edition (`work/freeze-diff.json`): string counts +22/−22 (P1), +23/−23 (P2), +26/−27 (P3), +26/−26 (P4), +22/−22 (P5), +23/−23 (P6), +32/−33 (P7), +101/−107 (P8).
- CJK totals per page: 202→202, 244→244, 179→176, 197→199, 177→177, 198→198, 390→408, 1030→840. Total 2617→2444 (delta −173).
- Full CJK decomposition (added/removed instances per page, recomputed from the diff JSON + node multisets; added − removed = delta on every page):
  - P1: added 89 / removed 89 (delta 0) — pure 1:1 SC→TC glyph swaps.
  - P2: 83 / 83 (0) — pure swaps.
  - P3: 61 / 64 (−3) — round-2 instruction shortening only.
  - P4: 71 / 69 (+2) — round-2 debate `到底` only.
  - P5: 70 / 70 (0) — pure swaps.
  - P6: 69 / 69 (0) — pure swaps.
  - P7: 150 / 132 (+18) = solicitation +19, editorial note −1, full-width `，`/`！` +2, round-2 bridge rewrite −2. (19−1+2−2 = 18 ✓.)
  - P8: 315 / 505 (−190) = −194 full-width print parens (97 notes × 2, replaced by the half-width style) + 4 from `三单`→`第三人稱單數`. Strict-CJK node count confirms 788→792 (+4): no content lost.
  - Total added CJK instances 908; total removed 1081; 908−1081 = −173 ✓ reconciles exactly.
- French zero-change proof (independent of freeze's string diff): CJK-stripped text-multiset diff per page is **0 on P1, P2, P4, P5, P6**. Residuals elsewhere are explanation-layer only:
  - P3 (+1/−2): the shortened instruction reflow (`ne...jamais / ne...plus / ne...pas` kept verbatim; the lone `）。` line removed).
  - P7 (+2/−3): only `VOL.4`/`8`/space redistribution from the solicitation + editorial rewording; no French word appears or disappears.
  - P8 (+83/−89 stripped nodes): entirely the full-width→half-width paren conversion + reflow; every French word, number, and key preserved (see Gate 2).
- Note on `--strict-cjk`: it exits 1 (908 added CJK instances) — EXPECTED for an SC-core→TC fan-out, where the explanation layer legitimately gains Traditional forms. The applicable gate for this pairing is the full decomposition above (not added=0, which holds only when the core is already in the reader's script). Not a failure.

## Gate 2 — P8 dual-gate: PASS

- Plain `p8.py compare --core-p8 <core P8 svg> --edition-p8 <edition P8 svg> --total 150` (explicit dual paths, NOT `--target`, NOT default total): **CLEAN, core 97 = edition 97, missing=[], extra=0, keydiff=[135, 150]**, exit 0 (`work/p8.json`, `work/p8.log`).
- Full-150 `hidden_files/w45/p8-fr-gap-fix/keycompare.py --core … --edition … --total 150 --p8 tools/p8.py` (`work/keycompare.json`): **mismatches exactly [135, 150], both noted on both sides; bare-key mismatches = 0** (all 53 bare keys identical; exit 1 is by design on any mismatch).
- Node evidence for both noted diffs (not extractor artifacts):
  - 135: core node `· 135. 读一份日程，本身就是在了解法国。（lire un…` vs edition `· 135. 讀一份日程，本身就是在了解法國…` — the key sentence itself is the Traditional rendering, noted both sides. Legitimate translation item.
  - 150: core `· 150. 开放题 — 要点见写作框，范文在第 8 版写作框内（按要…` + `点给分）` vs edition `· 150. 開放題 — 要點見` + `寫作框，範本在第 8 版寫作框內 (按要點給分)` — matches the KIT's claimed printed line exactly; Traditional rendering, noted both sides.
  - 137 (required non-diff): key `Les élèves sont en vacances depuis le 17 octobre.` identical both sides; note is French-only (`être en vacances + depuis`), hence no keydiff — verified from nodes (`…octobre.（être en vacances + depuis）` vs `…octobre. (être en vacances + depuis)`).
  - 136 shared-glyph body `Traduisez : 他跑得比他哥哥更快。` byte-identical both sides.
- P8 flow geometry (re-measured): battery ends y=1410 (bottom 1485); MODÈLE y=1538.0, RÉPONSES head y=1838.0 in both; keys end y=2046 (core 2167, shorter from half-width parens); max baseline 2539.19 = core; footer rule 2580; gap 40.81 px.
- P8 keys-only spacing, exact-column method (15.5 px nodes, columns x=65/527/989/1451, 22/24/30/8 lines = 84 lines): modal gap **20.15 px; 73/80 gaps exactly 20.15; 7 × 86.41 section jumps** — identical in count and value to core's 7 × 86.41 (core columns 22/24/30/14). The earlier mixed-column min 1.46 is a binning error (columns interleaved) and is discarded.

## Gate 3 — Occlusion + ink + P6 labels: PASS

- Canonical `tools/occlusion_audit.py` (selftest OK first: all 6 planted classes fired once, clean controls silent): **edition 0 flags, core 0 flags, NEW vs core 0** (`work/occlusion.json`); edition-only run also 0 flags.
- Same-baseline ink scan (my own script, `work/geom_scan.py`, PIL true-ink boxes via the tool's `ink_box`, EVERY baseline on all 8 pages): **0 overlaps**. P1 top y=92 gaps [387.5, 196.2]; every footer y=2624 gap [1157.1] — matching KIT exactly.
- Right-edge scan (ink_right > 1885 AND advance-end > 1885, edition vs core): **11 ink flags, all byte-identical to core** — 8 footer page lines at 1885.074 (0.074 px sub-pixel rounding at the right margin, 65 px inside the 1950 page edge, not a breach) + 3 frozen P8 French lines (y=940.0 adv/ink 1891.254/1891.25; y=1016.0 1891.305/1891.25; y=1054.0 1899.582/1899.5; texts `b. une soirée qui dure jusqu'à la nuit`, `d. le coquillage fêté à Port-en-Bessin`, `e. plusieurs concerts en une semaine`). Advance-end > 1885 gives exactly those same 3 P8 lines on both sides. Every flag is frozen text byte-identical to the core; no explanation-layer flag exists. Inheritance is valid here because the flagged texts are byte-identical frozen French (not fan-out text).
- P6 chart-label element check (all P6 texts vs later-drawn rects): **worst later-rect ink coverage 0.000, gate <0.30 PASS, zero nonzero coverages**. The P6 calendar is a text-row table, not bars; the box rect is drawn before the labels. The below-30% COVER blind spot does not apply — coverage is literally zero, and the P6 card shows all labels unclipped.

## Gate 4 — Gloss counts: PASS

- Method: split the rendered `gloss()` / `譯注` bridge strings on `·` itself (never on ` · `), edition build sources vs core build sources, item by item.
- 9 strings, core = edition: **[7, 6, 3, 6, 7, 3, 6, 6, 3], total 47**. Six `gloss()` boxes (P1 7, P2 6, P3 6, P4 7, P5 6, P6 6 = 38) + three `譯注｜` bridge boxes (P2 3, P4 3, P6 3 = 9).
- French headwords identical item by item; the only apparent "headword diffs" are the prefix glyph itself (`译注`→`譯注`).
- Render-level `譯注｜`-led line counts equal core on every page: p1 1, p2 2, p3 1, p4 2, p5 1, p6 2, p7 0, p8 0.
- Dual-caliber reconciliation: the brief's "38" = the 6 main gloss boxes only; the TRUE total including the 3 bridge note boxes is **47**. No spaced-split undercount case occurs in these 9 strings, but the count was done with the `·`-split method regardless.
- Every edition gloss item's French headword survives in the rendered SVGs (space-normalized check: NONE missing).

## Gate 5 — P7 golden sentences + frozen points: PASS

- Frozen points (whitespace-normalized joined SVG text, edition):
  - P4 `41e édition en 2026 (40e anniversaire)` = 1; whole-edition `40e édition en 2026` = 0; whole-edition `40e` = 1.
  - P7 #4 comparatif `plus excitante ou plus frustrante ?` = 4 on P7 (B1 column para + B1 example box + tools box + golden sentence) + 1 in the P4 debate box = **5 edition-wide**.
  - P7 #8 `Les jeunes créateurs y rencontrent leur public, en vrai.` = 1 on P7 (golden only) + 1 on P5 (article source) + 1 on P8 (answer key 106, expected).
  - Q106 error `y rencontre leur public` = 1 on P7 (clinic item 106).
  - P6 sync `Ce calendrier peut encore bouger.` = 1 on P6, 2 on P7 (B2 column para + example box), 0 on P8.
  - Q120 stem `Si j'étais libre dimanche, j'___ à Nanterre.` = 1; word-boundary options `irai` = 1 / `irais` = 1 / `vais` = 1; key B (keycompare 120 = B); P8 note in sync (`si + imparfait → conditionnel` + elision `j'`).
  - P7 French definition sentences present: `Reprendre, c'est recommencer` = 1; `plus / moins / aussi + adjectif` = 1. Only the explanation lines were localized, never the definition sentences.
- Golden 8 (P7 nodes 76–128), each verified verbatim contiguous in its tagged article page, in this issue's own SVGs:
  1. `Le lundi 2 novembre, on reprend les cours.` (page 2) — exact.
  2. `On ne connaît pas encore les finalistes.` (page 1) — article has mid-sentence `on ne connaît pas encore les finalistes — …` (golden capitalizes sentence-initially and truncates before the dash; the core's recorded adjudication, inherited because the French text is byte-identical — ED and CO contexts identical at the same offset).
  3. `Les cimetières se sont remplis de chrysanthèmes.` (page 3) — article `…se sont remplis de chrysanthèmes — blancs, …` (dash-truncation adjudication, same inheritance).
  4. `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?` (page 4) — exact, debate box.
  5. `Le festival se promène dans Paris.` (page 5) — article `…le festival se promène dans Paris : …` (initial-cap + colon-truncation adjudication, same inheritance).
  6. `Ce calendrier peut encore bouger.` (page 6) — exact.
  7. `Ce week-end, tout se joue.` (page 1) — MOT box `Ce week-end, tout se joue : les finales, …` (colon-truncation adjudication, same inheritance).
  8. `Les jeunes créateurs y rencontrent leur public, en vrai.` (page 5) — exact.
  - Page tags correct on all 8 (2, 1, 3, 4, 5, 6, 1, 5). All 8 are from this issue's own articles; no classic/external sentence leads.
- Pagination (from P8 answer-section separators, in order 1–8): **10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**, ranges continuous 1–10, 11–25, 26–43, 44–61, 62–78, 79–96, 97–108, 109–150. Sum = 150.
- Levels: KIT's A2 53 / B1 75 / B2 22 is the core's registry (登記表） count, inherited unchanged — no transform MAP entry touches a level literal, and rendered level chips are identical core vs edition (A2 42 / B1 62 / B2 20 = 124; the 26 gap is exercises whose level is not a standalone chip node, e.g. grouped P8 items — see Non-blocking N3). Exercise total 150 confirmed independently (one-process render `TOTAL exercises: 150`; keycompare 150 keys).

## Gate 6 — Images: PASS

- Payloads (SVG2 `href=` base64, decoded JPEG sha256 first-16): P1 `f3705af28f175ce4`, P2 `5b772facb5db886c`, P3 `be071fdae81a71b4` — **edition = core, 1 payload each on P1/P2/P3, 0 on P4–P8 in both**. `<image>` elements placed 1/1/1 on P1/P2/P3 (visible on cards).
- Credit lines, edition = core verbatim:
  - P1 `Eugène Atget (1857-1927), photographie, domaine public`.
  - P2 `Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA`.
  - P3 `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public`.
- Provenance: the core's asset register (`hidden_files/weekly-report-w45-fr-build/assets/CREDITS.md`) records all three as Public Domain with Wikimedia Commons metadata checked 2026-10-20, with the same Artist fields (Atget 1857–1927; Hiroshige 1797–1858 / LACMA; Blanco, Flora de Filipinas). See Limitations for the scope of this check.

## Gate 7 — Readers' corner: PASS

- P7 reader's-corner box (nodes, and visible on the P7 card, fitting inside its box with no collision):
  - Labeled editor's example: French `Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)` (frozen) + Traditional `小墨點評｜編輯部範例：…`. No invented reader, no invented quote: the example is explicitly labeled as NOT a reader letter. (`小墨` is the inherited editorial-comment persona from the core, not a reader.)
  - Three-fact disclosure ON THE PAGE in French + Traditional:
    - French note: `Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.`
    - Traditional note: `編輯部說明：截至付印，編輯部尚未收到真實來信與 VOL.2 第 8 版投稿作文（W44 未出刊），故本期刊登標註明確的編輯部範例；兩者皆延至 VOL.4 點評。`
    - Covers: (a) no real letters, (b) no VOL.2 page-8 submissions, (c) both deferred to VOL.4 — the Traditional note names both facts explicitly (the core's Simplified note named only the VOL.2 p8 submissions; the edition renders the frozen French `aucun texte` scope in full).
  - Explicit open invitation for real letters, in Traditional, in the corner: the comment para's final sentence `請把你的來信和最棒的第 8 版作文寄給我們，VOL.4 見！` — imperative, literally covering BOTH letters and best page-8 texts (FR×NL precedent, same slot). The VOL.4 preview line (`還有你們的來信！`) is explicitly NOT counted as the invitation, and no other-page exercise prompt (e.g. P2's "寫兩句法語寄給編輯部") is counted either. See Non-blocking N7 for the placement adjudication.
- VOL.4 preview line: `下週：參議院審議社保預算、11 月 11 日停戰紀念日、迪耶普扇貝集市；還有你們的來信！` (single line, y=2466).

## Gate 8 — Furniture three-way: PASS

- Badge (FR/IT-target family precedent, NOT the EN-core 372/19.5pt instance): string = W43 shipped same-pairing string verbatim (`法語正文 · 繁體中文講解 — 給繁體中文讀者的版本`), **inserted at y=574, 22pt, bold, BRICK (#a4553a), centered (x=975, anchor=middle)**. Core carries the Simplified counterpart at the same geometry. The y=372 slot is the frozen French body strapline (`LE JOURNAL DES APPRENANTS DE FRANÇAIS — LIRE LA VRAIE VIE, EN FRANÇAIS`), byte-identical in core / W43 / edition — confirming FR cores have NO free slot and the 574 insertion is correct.
- Footer (all 8 pages): `Le Lucerna · 法語週報 VOL.3 · 正文法語 · 講解繁體中文` (W43: same with VOL.2; core: Simplified counterpart).
- Page line: `第 N 版 / 共 8 版`, shared-glyph identical in all three (x=1885, end-anchored).
- Gloss prefix `譯注｜` (W43 and edition; core `译注｜`).
- P8 head keeps full-width `（第 1–8 版）` (`RÉPONSES · 全部答案與簡析（第 1–8 版）`, y=1838.0); P8 printed notes use half-width parens; separators `— 第 N 版 —` shared.
- Band heads follow the French + Traditional pattern as W43 (P1 `VOL. 3 · 總第 3 期`, P2 `VIE QUOTIDIENNE · 生活`, P3 `CULTURE · 文化`, P4 `SPORT · 體育`, P5 `JEUNESSE & MUSIQUE · 青年`, P6 `POLITIQUE & CHIFFRES · 時事`, P7 `LANGUE EN MAIN · 精講`, P8 `EXERCICES & RÉPONSES · 練習與答案`). P5's second element differs from W43 (`MUSIQUE` vs `ÉCRANS`) — this week's own content theme (Pitchfork), not furniture drift; the pattern holds (see N2).

## Gate 9 — Web PDF (q75 gate): PASS — measured conclusion: q75

- Regenerated from the delivered cards via the build's `render.py` in my own scratch (`work/webregen/`, ED redirected; render.py itself otherwise untouched): **cards 8/8 byte-identical** (sizes match delivered exactly), **print PDF byte-identical** (23,611,048 B).
- Delivered web PDF: **8 pages, 936 × 1296 pts, 5,093,804 B (< 10 MB), Title `Le-Lucerna-VOL3-ZHTW-web`**, PDF 1.4.
- Web PDF bytes vs my regen differ in exactly **8 bytes, all inside the `CreationDate`/`ModDate` strings** (`D:20261028064249Z` vs `D:20261028070943Z`) — timestamp only, same length, same file size. Not a content difference.
- Stream identity (pdfimages extraction): delivered streams = regen streams **8/8 byte-identical**; sizes 658098 / 641018 / 591503 / 638917 / 531567 / 562228 / 638347 / 827682 and sha16 `7fa564565ca712ac`, `ee05e06d98ca1c2c`, `361bd685faf26c37`, `3436c39afd15a085`, `a03954ae4054623d`, `cbec4836e7eecc10`, `398215ea7335fc67`, `bae851367e543969` — matching KIT §10 exactly.
- Fresh-encoding distance test (delivered cards → PIL JPEG): **fresh-q75 byte-match 8/8; fresh-q72 byte-match 0/8** (q72 sha16 differ on all 8).
- pdftoppm −r 150 render of the delivered web PDF vs cards (195×270 downsample, corrected channel-split mean): **1.450 / 1.330 / 1.271 / 1.289 / 1.177 / 1.226 / 1.384 / 1.523** — all ~1 magnitude (noise pages would be ~100). Paper-tone means match KIT (p1 ≈ (219, 214, 199), etc.). 8 pages all clean, no noise page.
- Quality conclusion, stated explicitly: **q75 by pipeline identity** — the web stream is the render.py product (Pillow default quality, empirically q75) from THESE cards: streams byte-equal fresh q75 encodings of these cards, byte-unequal to q72, and byte-equal to my independent render.py regen. A literal "stream = independently saved bytes" reading is NOT required and NOT used: the Pillow PDF writer re-encodes by construction; the judgment is pipeline identity, and it is q75.

## Gate 10 — Transform solo reproduction: PASS

- Fresh pristine core build copy + the build's `transform.py` alone (sections in order), in `work/repro/`: transform run OK (**265 map entries, 327 literal hits replaced** — matching KIT §1 exactly), P8 PRINT_NOTES=97.
- Harness-only change: the 5 OUT lines redirected to my scratch svg dir AFTER the transform run (transform.py itself untouched); the content modules were then run in ONE process (`import content12, content34, content56, content7, content8` — README #7 one-process rule; render log: `TOTAL exercises: 150`, P7 clinic ends 2140, P8 battery 1410, P8 keys 2046).
- Transformed scratch sources vs the build's transformed sources differ ONLY in the 5 OUT-redirect lines (bslib4.py and svglib.py: 0 diff lines).
- Rendered SVGs vs delivered: **8/8 byte-identical**. Delivery SVGs re-hashed unchanged after the repro.

## Gate 11 — All 8 cards visual: PASS

- Every card eyeballed at full page (1950×2700): furniture, boxes, flows, answer blocks all present; no overflow, no overlap, no footer intrusion, no missing content. Specific risk spots checked on the cards:
  - P1: badge, strapline, Atget photo + credit, quiz 7–10, footer.
  - P2: gloss box with the 、-led continuation line (see focus f); Hiroshige image + credit; exercises 11–25.
  - P3: shortened instruction single line + negation items 35–37 below it; Blanco plate + credit.
  - P4: `41e édition en 2026 (40e anniversaire)` in the chiffres box; debate box with ？ mid-line.
  - P5: golden #8 source sentence in the Creator Week box; exercises 62–78.
  - P6: calendar table labels fully visible, unclipped; `Ce calendrier peut encore bouger.` in the journal-phrases box; exercises 79–96.
  - P7: all 8 golden sentences with page tags; bridge sentence single line; clinic 105–108; reader's-corner box fits (comment + French note + Traditional note, no collision); VOL.4 preview.
  - P8: battery 109–150 (Q120 options visible: `irai · irais · vais`), model essay box, full answers with all 8 page separators, keys + half-width notes readable, answers end well above the footer.
  - P1 gloss wrap `戰慄、刺` / `激感` across two lines is the core's identical wrap (core node `战栗、刺` at the same position) — inherited, content complete, not a defect.

## Focus points — item-by-item

- (a) Traditional independence: PASS. SVG-only charset walk (4e00–9fff): edition **513**, W43 fr-zh-tw **526**, zh-tw core **767** (see N1 for the KIT's irreproducible 786/86). True NEW set = **79 chars**, EACH verified in context as a standard Traditional form from new W45 vocabulary (e.g. 決賽-week: 決賽/揭曉/戰慄；預算-week: 審議/參議院；all 79 contexts recorded in `work/charset.json` + `work/charset2.json`). Reference charsets themselves are clean (W43 OpenCC flags []; zh-tw core only 台）. "Simplified-residue = 0" therefore rests on this complete cross-check, NOT on the builder's table — and the builder's table is in fact wrong in both directions (see N1), which is why the independent recomputation matters. The edition still passes because my recomputation covers the true NEW set (including 16 chars the builder never listed).
- (b) OpenCC "台" false-positive verification: PASS, with measured evidence. OpenCC `s2twp` single-char scan over all 513 edition chars flags ONLY `台` (→`臺`). Occurrences in the edition: exactly 2, both correct Taiwan forms that never take `臺`: P4 `tribunes 看台。` and P8 `scène=舞台 b`. Cross-check: `台` is present in the zh-tw core charset (True) though absent from W43 (False). TRUE false positive, not residue.
- (c) Mainland vocabulary independent rescan (my own list, not the builder's): PASS. Builder's 31 Simplified forms: all absent. My additional Traditional-character mainland-vocab list (視頻/軟件/網絡/信息/打印/鼠標/博客/郵件/質量/出租車/地鐵/公交車/酸奶/盒飯/打車/閨蜜/給力/土豆/西紅柿/黃瓜/菠菜/草莓/櫻桃/髮廊/乾活/穀物/鹹菜/蕃茄/馬鈴薯）: ZERO hits. The only hits in the Taiwan-form check were correct Taiwan usages in appropriate contexts: 線上/線下， 資訊， 計畫 (×4), 母音， 第三人稱單數， 範本 (×2), 範例 (×2), 籤表 (×2), 戰慄， 在哪裡， 品嚐 (×2), 日曆， 賽季 (P8 `室內賽季比室外短` — the KIT's recorded Taiwan-sports-term decision; acceptable). No 影片/視頻， 捷運/地鐵， 計程車/公車 terms occur at all.
- (d) CJK change decomposition: see Gate 1 — every page reconciled exactly (added − removed = delta; totals 2617→2444, −173).
- (e) Gloss dual-caliber reconciliation: see Gate 4 — true count **47** (brief's 38 = gloss boxes only; +9 bridge note boxes).
- (f) P2 "、"-led lines: exactly 1, verified individually. P2 y=1154.675: `、反之 · un rituel 習慣、儀式。` — continuation of the gloss box (`en revanche 相反` ends the previous line at y=1124.95); the full gloss string is present across the 4 box lines; same y, same class as the core's identical line (core: `、反之 · un rituel 习惯、仪式。` at y=1154.675). Inherited separator-led wrap, same class as W43's accepted `·`-led lines. Kept, not a defect; visible on the P2 card reading naturally.
- (g) P8 flow-split flags: all 4 verified individually against the rendered P8 (nodes + card):
  1. y=1917.26 opener-ended `…3. coquilles (` → next line `波爾諾曼底賣扇貝) · 4. reprend…` — note continues; key 3 intact.
  2. y=2203.71 opener-ended `…123. A (` → next line `三區同日復課) · 124. C…` — note continues; key 123 intact.
  3. y=2445.51 closer-led `。 (lire un programme = 讀日程) · 136. …` — the 。 belongs to the frozen 135 key sentence (`…了解法國。`), wrapping to line start; wording cannot change because it is the answer key; key 135 intact.
  4. y=1956.1 opener-ended `…147. goûter (goûter 品嚐（` → next line `原形）) · 148. …` — note continues; key 147 intact.
  All structural joined key-flow wrap splits; no content lost; keys intact (proven by Gate 2: bare-key mismatch 0, p8 CLEAN). Same defect class as the core's 8 flags, fewer in count. Fixing would require changing frozen keys or flow parameters. Kept with this rationale.
- (h) Round-2 three fixes, item by item:
  1. P3 instruction shortening: rendered single line at y=1024.65: `改寫（ne...jamais / ne...plus / ne...pas）。` — complete (verb + all three negation patterns + 。）; the items it governs (Q35–37) are negation rewrites, visible directly below on the card. Old long instruction gone. (Drops 句子/用 vs the core; the task stays unambiguous — the W43 remedy verbatim.)
  2. P7 bridge-sentence rewrite: rendered single line at y=1319.1: `語法點｜reprendre：復課、重開（pause 後）。` — old `重新開始` form gone. `重開` trade-off stands: the column para above carries the full French definition (`Reprendre, c'est recommencer…`), so no meaning is lost. Dropped intermediary term: **0 occurrences** in delivered SVGs, ABSTRACT.txt, WEEKLY-KIT.md, and build code (`transform.py`/`checks.py`/`render.py`) — verified by direct grep.
  3. P4 debate-sentence rewrite: y=2356.4 `事先不知道決賽選手，到底是更刺激還是更` + y=2384.4 `掃興？寫兩句支持、兩句反對。` — `？` now mid-line (KIT's claimed y=2384.40 exact); the Chinese prompt renders the frozen debate-box verbatim's meaning (`plus excitante ou plus frustrante ?` = 更刺激還是更掃興， present on P4 as French, counted 1×).
- (i) Right-edge 11 flags, item by item: see Gate 3 — all 11 are frozen-core-identical (8 footers + 3 P8 French lines); NO explanation-layer flag exists, so no fan-out text needed shortening. Frozen-core inheritance is adjudicated only for byte-identical frozen text, which is exactly what these 11 are.
- (j) q75 measured conclusion: see Gate 9 — q75, with numbers (fresh-q75 8/8 byte-match, fresh-q72 0/8, streams 8/8 identical to regen, pdftoppm diffs 1.18–1.52).
- (k) Builder's other claims: pagination 10/15/18/18/17/18/12/42 verified via P8 sections (Gate 5); levels A2 53/B1 75/B2 22 inherited from the core registry (Gate 5 + N3); exercise count 150 verified three ways (render total, keycompare 150 keys, P8 section ranges); PDF pins verified on disk (below); ABSTRACT.txt verified (337 B, sha 03f55a19…, single line, 0 ASCII double quotes, Traditional, real topic keywords + learner phrase + masthead + target language name + A2–B2 + 150 — see Gate 9/ABSTRACT section above).

## Delivery pins (measured on disk at end of proof)

| File | Bytes | SHA-256 |
|---|---|---|
| Le-Lucerna-VOL3-ZHTW.pdf (print) | 23611048 | b1ed9e6aa7f8ccd8569bf04b30571f35daa1e6727aa61f54900b464fdd88315a |
| Le-Lucerna-VOL3-ZHTW-web.pdf (web) | 5093804 | 0b3501aeedec53c809870c3161ac0216ed74abca0b75dfd1d585782f1c834d49 |
| ABSTRACT.txt | 337 | 03f55a191b2b75a439ffb0a1f3eb786bf34dc4a74910b13ae93066d1f906830b |

All match the builder's claimed pins exactly (full hashes, not just prefixes). SVG/card hashes match KIT §11 exactly (verified at start: all 16 files). Delivery dir contains exactly: svg×8, cards×8, print PDF, web PDF, WEEKLY-KIT.md, ABSTRACT.txt — no other files.

## Non-blocking observations (SEPARATE from blocking items — none of these block shipping)

- N1 — KIT §5 charset numbers do NOT reproduce (documentation error, paper unaffected). KIT claims zh-tw core 786 and 86 NEW chars "all adjudicated". My independent SVG-only recomputation (three regex variants agree) gives zh-tw core 767 (4e00–9fff; 782 under freeze.py's wider CJK regex; 770 for build sources) and NEW = 79, not 86. 23 chars on the KIT's NEW list ARE attested in the zh-tw core (spread across all 8 core pages, so no single skipped file explains it), and 16 true NEW chars are missing from the KIT list (`修凌境尚強惡擺晨濱相眾知籤菜迪音`). The builder's reference computation is irreproducible from current disk state under any tested definition (delivery SVGs, build sources, their union). Impact: NONE on the paper — I adjudicated the true 79 (including the 16 the builder never listed) and all are standard Traditional forms; OpenCC confirms residue = 0. Action for the coordinator: correct KIT §5's numbers (767 / 79) or note the discrepancy; no rebuild is needed or justified by this.
- N2 — P5 band head `JEUNESSE & MUSIQUE` vs W43's `JEUNESSE & ÉCRANS`: this week's content theme (Pitchfork festival), not furniture drift. Pattern (French + Traditional) holds.
- N3 — Rendered level-chip count (124) vs registry count (150): the KIT's A2 53 / B1 75 / B2 22 is the core's exercise-registry count, not a count of standalone chip nodes. Do not "correct" the KIT to 124; the registry count is inherited unchanged (see Gate 5).
- N4 — `freeze.py diff --strict-cjk` exits 1 for this pairing by design (908 added CJK instances from SC→TC explanation localization). The gate applied here is full decomposition (Gate 1), not added=0. Do not misread the exit code as a gate failure.
- N5 — Web PDF bytes differ from an independent regen in exactly 8 bytes = CreationDate/ModDate timestamps only. Not a defect; streams are identical.
- N6 — P1 gloss wrap splits `刺激感` as `刺` / `激感` across two lines. The core wraps identically at the same position (`战栗、刺` / `激感`); content is complete across the lines. Inherited wrap, not a defect.
- N7 — Reader's-corner invitation placement (adjudication, stated so the coordinator can overrule if they read Gate 7 strictly): the explicit imperative invitation sits in the Traditional comment para of the same reader's-corner box, NOT inside the editorial-note paragraph itself. I accept this under the corner-as-a-whole reading + the FR×NL precedent (same slot) cited in the KIT: a reader reading the corner encounters an explicit invitation, and the corner is not "only the 3 facts". The teaser preview line and other-page prompts were explicitly NOT counted. If the coordinator requires the invitation sentence to move inside the editorial-note paragraph, that is a layout edit, not a content failure — but under the stated gate ("an explicit open invitation for real letters in the Traditional disclosure"), the corner as delivered satisfies it.

## Limitations (stated plainly)

- Commons Artist-field provenance: verified via the core's asset register (CREDITS.md, Commons metadata checked 2026-10-20) + credit strings byte-identical to the core. I did not re-query the live Commons API image-by-image in this round; a live re-query would be a belt-and-braces check, not a gap in the paper (payloads and credits are frozen from the core).
- French prose: the French target text is byte-identical to the shipped FR core (proven by freeze baseline + CJK-stripped multiset diff + frozen points + keys + pagination). French correctness therefore inherits the core's own full proofread (core KIT records a ZERO-PROBLEMS reproof); this fan-out proof verified the frozen points, golden sentences, keys, pagination, and geometry, but did not re-proofread all French prose from scratch — that would duplicate the core's gate rather than test the fan-out.
- Card review was visual at rendered-card resolution; sub-pixel geometry is covered by the occlusion/ink audits, not by eye.
- The concurrently running fr-ru insert touched only its own edition dir and weekly-git; hash stability confirms it did not affect this edition or the core during this proof.
