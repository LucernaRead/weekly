# WEEKLY-KIT — La Lucerna · Edizione Italiana VOL.1 · IT × EN

## Edition identity

- **Grid cell: IT × EN** — Italian text, English explanations; the edition for English-speaking readers of Italian.
- **Same frozen Italian core as VOL.1** (first issued pair = Chinese explanations, `files/weekly-report-it-vol1/`). Week **Mon 2026-10-19 – Sun 2026-10-25**; lead story «Un'ora in più di sonno» (ora solare) + P6 deep read on the Manovra 2027.
- **Pairing badge (P1 masthead, brick red, under the black banner):** "Text in Italian · Explanations in English — the edition for English-speaking readers".
- **Footer on every page:** left "La Lucerna · ITALIAN WEEKLY VOL.1 · TEXT IN ITALIAN · EXPLANATIONS IN ENGLISH", right "Page N of 8".
- Spec: 8 pages, 1950×2700, 4 columns, warm ivory — identical to the core edition.

## Method

- Build copied from the core build (`hidden_files/weekly-report-it-build/` → `hidden_files/weekly-report-it-en-build/`); the original build was never modified. Pipeline unchanged: Python → SVG → CairoSVG → PNG/PDF → pypdf (venv `/tmp/wp-venv`).
- The Italian core is frozen: articles, exercises, images, credits, facts and answer keys identical — including the honest Manovra chart presentation (the three published DPB components 5,0 + 5,0 + 3,4 = 13,4 are **not** the total ~23,5; noted on the page itself, and again in the P8 note for #85).
- The **entire explanation layer was rewritten in English**: all glosses (prefix "NOTE · "), notes, exercise instructions, section explainers, the error-clinic notes, the readers'-corner note, the teaser apparatus and **all 150 P8 answer notes**. Section headers are Italian + English (e.g. "VITA · DAILY LIFE", "APPROFONDIMENTO · IN DEPTH").
- Registry exercise-type names are kept in Chinese inside the build data (never printed anywhere; same precedent as the fr-en edition) so the registry stays byte-comparable with the core.

## Reader-language items (re-aimed at English, keys adjusted)

- **#137** （翻译， IT → reader language): key → "On Sunday we sleep an hour longer."
- **#138** （翻译， IT → reader language): key → "The show stays open till April."
- **#139 / #140** （翻译， reader language → IT): prompts are now printed in English ("On Saturday at 18:00, Napoli play Roma." / "Every figure must have a source."); the Italian keys are unchanged.
- **#150** (writing): key → "(open task — model text below)"; the model text itself is Italian core text and is unchanged.
- **All other 147 keys are byte-identical to the core registry.**

## Verification (measured on the final render)

- **Baseline reproducibility:** the original core build, re-run in a scratch copy, reproduces the finalized SVGs byte-for-byte — so any diff below is attributable to this edition's work alone.
- **Registry:** 150 exercises; meta (number / page / level / type) **zero diff** vs the core; distribution identical (A2 46 · B1 71 · B2 33; per page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38). The only key diffs are #137, #138, #150 above.
- **Text-node diff:** every non-Chinese text node of the core render appears verbatim in the English render. The only exceptions are two *wrap fragments* of explanation-layer bridge lines whose English wording was compressed (the P6 chart-bridge tail and the P7 B2-bridge tail) — both are apparatus, not article text; their Italian content survives in full in the English source strings. **No Italian article or exercise text differs.**
- **Images:** embedded image payloads are byte-identical to the core edition on all 8 pages; credits unchanged (Wikimedia Commons / NIST).
- **CJK scan of the final SVGs: 0 characters.** No Chinese remains anywhere in the render.
- **Answer-key typography:** space before each note parenthesis verified across all 150 notes — 0 violations (the fr-en defect class).
- **P7 phrases of the week:** all 8 phrases occur exactly 2× in the render (once in their article, once in the P7 list) — verbatim Italian, contiguous.
- **Build log:** zero FLOW OVERFLOW / HEAD TOO WIDE warnings. End positions vs the core: P1 headline flow 1809 = core; P6 exercises 2569 = core; P7 column 3 ends 1674 = core; P8 answer-key flow ends y=2523 (core 2540 — English notes are tighter than the Chinese ones).
- **Totals** (visible text, XML text-node method — the same method that reproduces the core's 37,115): **EN edition = 43,003 characters**; per page P1 4,724 · P2 4,499 · P3 4,217 · P4 4,378 · P5 4,620 · P6 4,673 · P7 4,543 · P8 11,349. **150 exercises.**

## Layout-fitting adjudications (wording only)

English runs wider than Chinese, so a handful of explanation-layer strings were compressed to fit the frozen layout. No Italian text, no fact, no key and no layout parameter was changed — the single exception is one furniture title size, following the es-en edition's own precedent:

- **P1:** CIFRE box title → "LA SETTIMANA IN CIFRE · Numbers" (the de-en edition's solution); trends-box subtitle reordered Italian-first ("Cosa cerca l'Italia · Tuesday's searches"); the snapshot line shortened to "Google Trends snapshot, 20 Oct. (approx.)"; sommario title → "IN QUESTO NUMERO · CONTENTS"; the weather-word gloss shortened to one line ("'Bad weather': rain, wind and storms — Adam.") so it clears the IN BREVE box.
- **P2:** FRASE box title → "LA FRASE PER RICORDARE · Remember" at title size 19 (single-line box titles cannot wrap; es-en reduced a box title the same way).
- **Match instructions** shortened to "Match the pairs" (P2 D, P4 B, P8 F) — the registry instruction string sits in a narrow slot beside the level badge.
- **P5:** the E TU English line shortened ("Going to Lucca, or films at home? Write two sentences and send them in.") so the coffee box keeps its clearance above the exercises rule.
- **P6:** section-A bridge → "Look at the charts and choose."
- **P7:** the four error-clinic English notes compressed to one line each (content unchanged), and the parola / lettere English notes tightened, so the right-column box stack ends at exactly the core's y=1674 and clears the phrases section.
- **P8:** about fifteen answer notes trimmed by a few words each after measuring the key flow (it renders in serif 14, wider than the Chinese notes' footprint); every note still states the point of its answer.
- One CJK docstring inside the copied `svglib.py` (an unused illustration helper) was translated, so the EN build sources are CJK-free; it prints nothing and changes no output.

## Proofread notes (own full pass)

- 100% audit of the English apparatus: every gloss, instruction, explainer and all 150 answer notes read for accuracy and grammar against the Italian they explain; translation exercises re-aimed consistently (translate *into* English on #137–138, *into* Italian on #139–140).
- Facts and figures unchanged from the proofread core — including the Manovra honesty note (components ≠ total) and the forecast labelling on the P6 charts.
- All 8 page cards visually inspected after the final build: badge, footers, box titles, image credits, clocks, charts and the P8 key block all clean; no overflow, no clipped line, no collision found.

## Deliverables (this directory)

- `svg/` — 8 page SVGs (p1-prima … p8-valutazione)
- `cards/` — 8 PNG cards, 1950×2700
- `The-Lucerna-VOL1-it-en.pdf` — print PDF (D5 rebuild), 7995110 B, 8 pages, sha256 `5174f985235ada26acfddb6a64a0f5eabcae389a71696a7bbba7bda82ef796dd`
- `2026-w43-it-en.web.pdf` — web PDF (D5 rebuild, tools/webpdf.py shipped file), 1139183 B, sha256 `0c49b7b5afd976de3792c069e2ca1eb4bb2033665e591fe8d2f6e32ccf669c6e` (**< 7 MB** ✓; old 3,630,225 B value was the render.py-era web PDF)
- Build sources: `hidden_files/weekly-report-it-en-build/` (copy of the core build; original untouched)

Not posted to Discord — delivery is the parent agent's call.

## Independent proofread (SOP gate) — 2026-10-21

Fresh full pass by an independent proofreader (not the builder), working from the rendered artifacts and the build sources, not from the builder's claims. Method: text-node extraction and node-by-node diff of all 8 SVGs against the frozen core; independent registry dumps of both builds compared entry by entry; all 150 exercises re-solved against their page articles/charts (not the 30-exercise minimum — the full set); CJK scan over the raw SVGs; paint-order occlusion sweep using the build's own PIL text metrics (every text node vs every later-painted opaque shape); box-containment check; all 8 cards viewed in full, plus zoomed crops of the dense areas.

### Problems found and fixed (2 — both geometry, both inherited from the core's coordinates, fixed in the IT×EN build sources only)

1. **P1 — section rule struck through the weather gloss.** The full-width rule above row B (y=1844) passed through the glyphs of "'Bad weather': rain, wind and storms — Adam." (baseline y=1847). The builder's adjudication said the shortened gloss "clears the IN BREVE box" — it clears the box, but not the rule above it; visually the line was struck through. Fix: rule moved 1844 → 1864 in `content12.py` (gloss descenders end ≈1852, row B still starts at 1874). The gloss text itself is unchanged.
2. **P8 — answer key #75 struck through by the footer rule.** The key flow's last item in column 2 ("75. cosplay — …", baseline y=2588.1) sat below the footer rule (y=2580), which cut through the line in the render. The KIT's earlier "flow ends y=2523" figure described only the last column's flow cursor, not the maximum baseline over the four columns — corrected here: the binding figure pre-fix was 2588.1. Fix in `content8.py`: key-flow leading lh 1.21 → 1.15 and flow bottom 2606 → 2562. Post-fix lowest key baseline = #75 at y=2554.5 (≈22 px clear of the rule). Registry re-dumped after the fix: **byte-identical** (no key, note or meta changed — layout only).

### Verified clean

- **Core integrity:** every differing text node between the editions classifies as apparatus or as a documented reader-language item (#137/#138 keys → English sentences; #139/#140 prompts → English with Italian keys unchanged; #150 note). The only non-Chinese core fragments not carried over node-for-node are three wrap fragments (P5 calendar parenthetical, P6 word-box instruction tail, P7 B2 bridge tail) whose Italian content survives complete in the English lines — as the builder stated. No Italian article sentence, exercise stem, option or key differs. Shape geometry differs only where English apparatus reflows (NOTE-box heights, badge-pill positions); the P6 chart bars are identical to the core (170 / 170 / 115.6 px for 5,0 / 5,0 / 3,4 = 34 px per billion, exactly proportional).
- **Manovra honesty:** the on-page line "Tre voci pubblicate nel DPB del 15 ottobre — non è il totale della manovra (circa 23,5 miliardi)" is intact, #85's key tests 5 + 5 + 3,4 = 13,4 with the note "(not the total)", and #86 (5 − 3,4 = 1,6) is consistent.
- **Registry:** 150 exercises; meta zero-diff vs the core; distributions identical (pages 10/18/18/18/18/18/12/38; A2 46 · B1 71 · B2 33); the only key diffs are #137, #138, #150 as documented. Key block numbering continuous 1–150.
- **Explanation language:** CJK scan of all 8 raw SVGs = 0 characters (wide ranges incl. fullwidth forms). Every gloss, note, instruction, explainer, clinic note, teaser and all 150 answer notes read: all English, grammatical, and accurate against the Italian they explain. Space before every note parenthesis across all 150 key lines: 0 violations.
- **P7 phrases:** all 8 occur exactly 2× in the issue text, byte-verbatim, with correct page tags.
- **Images:** embedded payloads byte-identical to the core on all 8 pages; credits unchanged (Wikimedia Commons / NIST).
- **Badge & footers:** the pairing line "Text in Italian · Explanations in English — the edition for English-speaking readers" is rendered on P1 under the black banner (seen in the card); every page footer carries "TEXT IN ITALIAN · EXPLANATIONS IN ENGLISH" + "Page N of 8".
- **Build log** after fixes: zero FLOW OVERFLOW / HEAD TOO WIDE warnings.
- **Kept as-is, with reason:** #86's key line carries no note in either edition (bare arithmetic answer in the frozen core, reproduced identically); the masthead strap "THE ITALIAN ITALIANS ARE READING" is headline ellipsis for "the Italian [that] Italians are reading" — intelligible and parallel to the core's strap.

### Note on the core baseline

During this proofread the frozen core's own files were re-rendered by a parallel geometry patch (core P8). The core's text content is unchanged (P8 character total identical; the only node-level effect is that key lines #46/#139, whose notes previously wrapped onto a second text node, now sit on one). All core-integrity conclusions above were re-checked against the current core files in the second pass and stand.

### Second pass

After the two fixes, the whole issue was re-rendered and a complete second pass run (full node diff, registry diff, CJK scan, occlusion sweep, containment check, geometry measurements, full views of the changed pages and crops of both fixed areas): **zero problems**. The edition is final under the SOP gate.

---

## D5 rebuild (2026-11-13)

D5 + §1.1 合并重建记录（2026-11-13；一任 builder 至 run2 循环，二任 builder 接手核实 + gate 2 补跑；不 commit、不 push；独立重校另派他人）。

- 装机：`apply_variant.py --patch-core it --week 2026-w43 --i-understand-this-writes-production`（core-it 落盘 `_D5_READER = "latin"`）；本版 `apply_variant.py --svglib <版>/svglib.py --target it --reader en --week 2026-w43`，`_D5_READER = "latin"`；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2（U+201C/U+201D/U+2019 → serif）保留。
- 基线：run TOTAL 150、0 警告；SVG 8/8 与 fanout 逐字节相同；印 PDF 与 fanout SHA 一致（8526959 B）；修前普查 D5 拉丁 490 / 西里尔 0 / 弯引号 CJK 0。
- 二次修复（只动字号，文字零改动；盒修法行号指 tsize 行，D19）：`content34.py:22` P3 头 25→22; `content12.py:51` P1 盒 `LA SETTIMANA IN CIFRE　Numbers` tsize 23→21（397.2，余 7.3px）; `content12.py:94` P1 `IN QUESTO NUMERO　CONTENTS` p.text 24→21（385.3，余 15.2px）; `content7.py:73` P7 `ERRORI TIPICI　COMMON ERRORS` p.text 23→21（394.9，余 5.6px）; `content7.py:84` P7 `LA PAROLA　WORD OF THE WEEK` p.text 23→21（387.1，余 13.4px）。
- P8：行数 201→201，距页脚线余量 53.1 px；p8 compare CLEAN（keydiff [137, 138]）。
- 新交付物：印 PDF `The-Lucerna-VOL1-it-en.pdf` `5174f985235ada26acfddb6a64a0f5eabcae389a71696a7bbba7bda82ef796dd`（7995110 B；修前 `1ffd541d5167596bd35b7b84ef4725be2e49bfcd07cf9d4c16301b76f6eed01b`，8526959 B）；网 PDF（tools/webpdf.py）`0c49b7b5afd976de3792c069e2ca1eb4bb2033665e591fe8d2f6e32ccf669c6e`（1139183 B；已发版 `3becceabe661d26155b5726656691ffe869761900b0dc4c04e7c4c8efe5a1add`，1245514 B）；text.md 与 fanout `.text.md.new` BYTE-IDENTICAL（55327 B，SHA `ad3417cd7065e604f3548d4e043399c601e281c224755d9f2245d6d4b52390ba`），W43 it issues/ 内无已发 `.text.md`，closer 落仓时新建补入。
- 门禁 run2 ALL-GREEN（18 门：run TOTAL 150 / head_check 0 / d5 census 0/0/0 / render RC=0 / webpdf RC=0 / occlusion 0 / p8 extract 150/150 / p8 compare CLEAN / freeze baseline 8/8 / freeze diff 新增 CJK TOTAL 0 / spill 0 / boxtitle 0 DEFECT（20 titles、245 body lines）/ edge 0/0 / creambox PASS 0 defects（n=405）/ 文字层 print=web 多重集差 0 / census_quotes 0 defective / 家族 gates.py N/A / 刊头间距 367.5 px PASS）。日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-en/GATES-SUMMARY.txt`；D5 报告：`production/notes/2026-w43/g-it/scratch-d5-rebuild-it/D5-REPORT-2026-w43-it-en.md`。
- 本 KIT 交付物行已更新为以上 D5 新值；旧针脚为旧配方值，已过期，以上实测发运值为准。
