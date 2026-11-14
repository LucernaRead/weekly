# Lucerna Weekly — KO × ES (VOL.1 fan-out edition)

**Pairing:** Korean target text (frozen VOL.1 core) · all explanations in Spanish, for Spanish-speaking readers.
**Status:** built + builder-proofread · **independent proofread: PASS** (2026-10-21, zero problems — see §9).

- Build dir: `hidden_files/weekly-report-ko-es-build/` (copy of the frozen core build, explanation layer rewritten)
- Core (never edited): `files/weekly-report-ko-vol1/` · build `hidden_files/weekly-report-ko-build/`

## 1. Baseline proof (before any edit)

The copied core build was run UNMODIFIED first: registry TOTAL 150 and all 8 SVGs reproduced the shipped core **byte-identically (sha256 8/8)**:

| page | sha256 (prefix) |
|---|---|
| p1 | f7db160498eee3d8… |
| p2 | f38afa34251e6d2c… |
| p3 | f5a258a4869c36d… |
| p4 | 6ceb1f220e2b120… |
| p5 | 0adf32b904a2b327… |
| p6 | e5e849ad6d528cdd… |
| p7 | d8219859284e98ea… |
| p8 | bd3b245f4edb4ff… |

Only after this proof was the explanation layer rewritten.

## 2. Totals (identical to core)

- **150 exercises** — A2 57 · B1 66 · B2 27; per page 10/18/18/18/18/18/12/38.
- Types (Spanish labels, same counts as core): Completar 49 · Opción múltiple 51 · Emparejar 16 · Texto con huecos 13 · Formar una frase 8 · Transformación 4 · Verdadero o falso 4 · Traducción 4 · Redacción 1.
- P8 writing model: 162 characters (printed range 150–200자）, unchanged.
- Registry-level diff vs core (both builds' registries dumped and compared): numbering, pages, levels identical; **keys differ at exactly #137, #138, #150**; all 150 notes rewritten in Spanish; stems differ only at #139/#140 (see §3).
- 해요체, Korean articles, stems, options, images and layout geometry frozen. Image payloads byte-identical to core on all 8 pages (data-URI comparison; counts 1/1/2/1/2/1/0/0).
- Final build log: zero FLOW OVERFLOW, zero HEAD TOO WIDE. P7 col3 ends 1621.72 (core 1645.76); phrases/teaser geometry unchanged (teaser ends 2514).

## 3. Key-diff registry (complete)

Translation-type items re-aim at Spanish; everything else keeps the core key byte-identically.

| # | change | core → ES |
|---|---|---|
| 137 | key (translation KO→reader language) | 台风的路径还可能改变。 → **La trayectoria del tifón todavía puede cambiar.** (note: Compara con la pág. 1) |
| 138 | key (translation KO→reader language) | 离考试还剩 29 天。 → **Quedan 29 días para el examen.** (note: Compara con la pág. 2) |
| 139 | stem re-aimed (was Chinese→Korean); **key byte-identical** | stem → "El fin de semana, consulta el pronóstico más reciente. → ___"; key 주말에는 최신 날씨를 확인하세요. (note: Compara con la pág. 1) |
| 140 | stem re-aimed (was Chinese→Korean); **key byte-identical** | stem → "El viernes voy al Parque Haneul a ver la hierba plateada. → ___"; key 저는 금요일에 하늘공원에 억새를 보러 가요. (note: Compara con la pág. 3) |
| 150 | key apparatus (open writing item) | (开放题，范文如下） → **(pregunta abierta — modelo a continuación)**; note: "El modelo está en la sección H de esta página (162 caracteres)" |

All other 145 keys byte-identical to the core. All 150 answer notes are in Spanish; match-set notes use the format `word = gloss (x)`; half-width parentheses only, space before each note parenthesis. Numbers inside notes use Spanish grouping (551.864, 1.312, 75.000, 1,5 millones); key tokens keep the printed formats (551,864 / 1,312).

## 4. Pairing furniture (ES column pattern)

- P1 badge (brick, bold, y=394): **TEXTOS EN COREANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES**; edition line «SEMANARIO COREANO · VOL.1 · 태풍 참피 · 가을야구 · 단풍»; Korean tagline kept, moved y 372→366; double rules 412/421; band shifted +9 (rect y 433, texts 487/531) — the established fan-out P1 structure; headline position unchanged.
- Footers (all 8 pages): «Lucerna · SEMANARIO COREANO VOL.1 · TEXTO EN COREANO · EXPLICACIONES EN ESPAÑOL» / «Página N de 8».
- Gloss prefix: **«Nota — »** (the core's gloss method renamed to `expl()`; the intermediary-layer term occurs **0 times** in the paper, this KIT, and the build code — verified by scan, Chinese and English forms).
- Masthead: blackletter **Lucerna**, no article (Korean/Spanish convention), exactly as the core ships.
- Every furniture string's rendered width was measured with real-font metrics before the build; all fit (P1 practice head shortened to «지금 바로 연습 · Práctica inmediata», 439.6→fits 434 col).
- Instruction lines (exercise apparatus) are in Spanish throughout, per the KO fan-out house pattern (cf. shipped KO×FR/DE/EN): e.g. «Lee los textos de la pág. 2 y elige la respuesta correcta.», «Pon la palabra adecuada en el hueco.», instr chips Completa / Reescribe / Forma la frase / Verdadero o falso / Traduce / Escribe / Relaciona.
- Spanish number/date style in the explanation layer: «el jueves 19 de noviembre», «el viernes 23», «1,5 millones».

## 5. Builder's proofread (full pass, this build)

- All 8 pages read end-to-end on the rendered cards; all 150 keys re-derived from the Korean text — agree with the registry diff (§3).
- P7 phrases: all 8 Korean quotes verified **verbatim contiguous** excerpts of their tagged pages, (N면) tags correct; full-issue occurrence counts identical to the core (2 each; phrases 1 and 4 count 4 through the core's own documented apparatus reuse — P1 standfirst deck / P2 matching option / P8 stems — frozen with the target layer).
- Weekday/date claims re-checked against the real 2026 calendar (Oct 19 Mon, 20 Tue, 21 Wed, 23 Fri, 24 Sat, 25 Sun, 31 Sat; Nov 2 Mon, Nov 4 Wed, Nov 19 Thu; Sep 22 Tue; D-29: Oct 21 → Nov 19 = 29 days) — the Spanish notes' claims («jueves 19 de noviembre», «viernes 23», playoff «el domingo») all agree.
- Freeze check (text-node multiset diff, ES vs core, all 8 pages): every difference is explanation layer / pairing furniture / §3 registry items. No Korean target text outside the registry changed. Han characters in final SVGs: **0**. Full-width parentheses: **0**.

## 6. Geometric occlusion audit (builder's run)

Script: paint-order SVG parse, real-font (PIL) glyph metrics via the build's svglib, line boxes **expanded by half the stroke width**. Validated first on a synthetic positive control — planted 100% cover, line crossing, footer-band intrusion, page-edge spill, and box spill **all fired**; a clean text did not.

Final run on the shipped ES SVGs: **0 COVER, 0 COVER-IMG, 0 LINEX, 0 FOOTER, 0 EDGE.** Two BOXSPILL metric flags (P2/P3 «Te toca a ti» box last line), both **pixel-adjudicated**:

1. **Real graze found & fixed (wording only):** the reader-box last line «…y envíalas.» put descender ink within <1px of the box's bottom border (P3 ink reached the border's top-edge row). Reworded to «Escribe dos frases en coreano; envíalas.» — a descender-free last line. After the fix: ink bottom row 1162 vs border top ≈1164 (P2) and 1363 vs ≈1364.7 (P3) — ~2 rows of clear air. The residual metric flag (generic +0.30em band overshoots the rect by 0.9–1.5px) is a proven false positive at pixel level; the geometry is the core's frozen box structure, identical in the shipped siblings.
2. **P1 search-box text-on-text collision — REAL defect, found in visual proofread, fixed by wording:** the Spanish line under the Korean topic line wrapped to 2 lines («…temas del / número.», second baseline y=1209.5) and collided with the fixed source line at y=1216. Shortened to one line: **«Estas cuatro palabras, temas de la semana.»** (369.0px ≤ 390 wrap width). Supplementary text–text ink-band overlap scan then run on all pages: ES shows exactly the core control's single pair — the P1 blackletter wordmark vs edition line — crop-adjudicated false positive (clear air between wordmark ink and edition line, as in core/FR/DE/EN).
3. Frozen-geometry spot check: P2 D-day sentence ink ends at card row **1795**, rows 1796–1802 empty, exercises rule at 1803–1804 — the core's patched geometry intact.
4. P8 keys: all 8 group headings have their first key 30.7px below in the same column (no orphans; keep-with-next logic active); max key baseline y=2499.7, above the 2540 flow limit.

## 7. Images & credits (from the core KIT; payloads byte-identical)

- P1: NASA ISS-43 Typhoon Maysak eye — Public domain (captioned as 2015 file photo).
- P2: Gary Todd, students at Sias Library — CC0.
- P3: Matsumura Keibun, quail/susuki — Public domain; Paul Cézanne, Still Life with Apples — Public domain.
- P4: Bain News Service, baseball team — Public domain.
- P5: US Army (Fort Knox concert crowd) — Public domain, file photo; Elijah Flores, cinema seats — CC0.
- P6: lumoplank, Hakkoda valley — CC0, file photo.

## 8. Deliverables & hashes

In `files/weekly-report-ko-es/`: `svg/` ×8, `cards/` ×8 (1950×2700), print + web PDFs, this KIT.

- Print PDF `Lucerna-VOL1-ES.pdf`: **32,299,760 B**, sha256 `04f39f85e127ff2f371a48d7673d112bd615cb48385c1dfc99f959784b488eb7` (D5 rebuild, 2026-11-13)
- Web PDF `Lucerna-VOL1-ES-web.pdf`: **2,014,558 B** (< 7 MB), sha256 `149e7eb96c061158820ca5dcf5b6be65e831b6f1a4869ed9b0dc79eca422a409` (D5 rebuild, 2026-11-13)

## 9. Gate status

Builder's full proofread + audits complete (above). **Independent proofread: PASS** — record below. No repo insert, no Discord (delivery paused), per scope.

### Independent proofread record (2026-10-21, fresh proofreader, one complete pass — ZERO problems)

1. **Freeze diff vs core** — text-multiset diff per page + build-code diffs (bslib4: only footer strings + `glossline`→`expl()` rename + «Nota — » prefix; svglib: one docstring; render.py: paths only; content8: type labels + note texts). Every delta is explanation layer / pairing furniture / documented registry items. **Zero Korean target-text changes outside the registry.**
2. **Spanish apparatus completeness** — full read of all 8 pages in both editions. Every explanation element in Spanish (glosses, instructions, type labels, clinic/frame-box notes, P7 glosses, P8 header + all 150 notes). **Han (CJK) characters in the ES edition: 0** in text layer and raw bytes; full-width parens 0. Korean words inside Spanish notes are cited headwords only (benign, house pattern).
3. **Keys re-derived independently** from the Korean articles/stems for all 150 — full agreement with the printed keys. Registry key diff = exactly {#137, #138, #150}: #137 «La trayectoria del tifón todavía puede cambiar.» and #138 «Quedan 29 días para el examen.» verified faithful to the printed Korean stems; #150 is apparatus. Stems #139/#140 re-aimed into Spanish with byte-identical Korean keys (directly observed in both shipped P8 SVGs). Page/level identical for all 150.
4. **PRINTED-NOTE SET EQUALITY — PASS.** The KO core's P8 rule prints every registry entry unconditionally (verified in core build source: 150/150). Sets extracted from both shipped P8 SVGs by exercise number: core = {1..150}, ES = {1..150}. **Sets EQUAL.**
5. **Totals** — 150 exercises (A2 57 · B1 66 · B2 27; pages 10/18/18/18/18/18/12/38); numbering 1–150 continuous; writing model 162 chars.
6. **P7 phrases** — all 8 quotes verified verbatim-contiguous against their articles with correct (N면) tags; occurrence counts ES == core for every phrase (2 each; phrases 1 & 4 count 4 via documented deck/key-stem reuse).
7. **Calendar** — verified against the real 2026 calendar (Oct 19 Mon, Oct 23 Fri, Oct 25 Sun, Nov 2 Mon, Nov 19 Thu, D-29 from Oct 21, etc.); all weekday claims in articles, stems and Spanish notes agree. **Typhoon Champi remains an open forecast** (landfall explicitly undecided in the article; no invented landfall anywhere).
8. **Furniture** — pairing badge on P1 («TEXTOS EN COREANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES»); pairing footers + «Página N de 8» on all 8 pages; masthead «Lucerna» (no article).
9. **Geometric occlusion audit (proofreader's own implementation)** — paint-order SVG parse, PIL real-font ink boxes (Noto Serif/Sans CJK KR faces), line boxes expanded by half stroke width, synthetic positive control validated first (COVER + LINEX fire; clean text unflagged). **Result: 0 flags on all 8 ES pages** (COVER/LINEX/FOOTER/EDGE/BOXSPILL), and 0 on the core as reference. Pixel adjudications on the shipped cards: P1 search box — Spanish line is a single ink band (rows 1170–1187), source line separate (1200–1220), no collision ✓; P2 reader box — box was extended (bottom border top row 1164.2), Spanish ink ends row 1159 → ≈5 rows of air (core: ≈3) ✓; P3 reader box — ink ends 1360 vs border top 1364.9 → ≈5 rows (core: ≈4) ✓; P2 D-day adjacency — sentence ink ends row 1795, rule rows 1803–1804, identical to the frozen core ✓.
10. **Images/credits** — embedded image payloads byte-identical to core on all 8 pages (counts 1/1/2/1/2/1/0/0); credit lines match the placed images and the core KIT list (NASA ISS-43 Maysak eye PD; Gary Todd CC0; Matsumura Keibun PD; Cézanne PD; Bain News Service PD; US Army PD; Elijah Flores CC0; lumoplank CC0).
11. **Banned-term scan** — the intermediary-layer term (Chinese and English forms) over paper SVGs + this KIT + ES build code: **0 occurrences**.
12. **Deliverables re-verified by the proofreader** — web PDF 3,115,958 B, sha256 `f20a6a64142d440b32efeebc4e82773b6853b377f32806327943b6be0299f4b7`, 8 pages, < 10 MB; print PDF 34,453,333 B, sha256 `a9e8acebad62e219ec065e8e551bb1f8f4009ce8ba24101c592df3ae292d9c17`, 8 pages. Pins match §8 exactly.

**Process disclosure (two proofreader-side incidents, both fully verified harmless):** (a) The proofreader's sandbox rebuild script failed to rewrite output paths (the build files carry a literal `~/…` inside `expanduser`), so sandbox rebuilds wrote into the real `files/` SVG dirs, overwriting shipped core + ES SVGs in place. Verified harmless: all 8 core SVG sha256 == the §1 baseline table; all 16 cards (core + ES) pixel-identical to fresh renders of the on-disk SVGs; PDFs untouched. The run independently re-proved the baseline claim (8/8). (b) Later, a direct import of the core's `content8.py` (which renders on execution and needs the full driver context) briefly wrote a partial-registry P8 variant over the core's `p8-siheom.svg`. The proofreader immediately restored it by running the core build through its proper driver (all five content modules, REG 150) and verified **all 8 core SVGs byte-identical to the §1 baseline table, including P8 = `bd3b245f…`**. The ES content-module import crashed before any save (ES file mtimes/hashes/content unchanged; the ES proofread above was performed on the shipped state).

## 10. D5 rebuild (2026-11-13)

D5 rebuild (2026-11-13–14；builder：W43 ko 家三任；不 commit、不 push；独立重校另派他人；入仓由 closer 做）。D5 报告：`production/notes/2026-w43/g-ko/scratch-d5-rebuild-ko/D5-REPORT-2026-w43-ko-es.md`；门禁日志：`hidden_files/d5-redo/scratch-2026-w43-ko/logs/2026-w43-ko-es-run2/GATES-SUMMARY.txt`。

- 装机：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样装为版内 `svglib.py`，仅改写 `_D5_READER = "latin"`；core-ko 落盘同模板（`production/2026-w43/core-ko/svglib.py`，+333/−40）。路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 保留（`_QUOTE_CLS` 在位）。ko-ru 无 fix-xru（W43 重建标准，见家族报告 §0）。
- 基线：`run.py` TOTAL 150、0 警告（fr 例外：基线唯一警告为 port 已知良性 HEAD TOO WIDE，见 D5 报告 §二）；修前普查 D5 拉丁 427、西里尔 0、弯引号在 CJK 0；基线印 PDF 34,436,845 B、sha256 `cf4e8a245e8b7964a6e74e629394a5b1ea1c934fa3010faf310272d3080ede0c`；基线网 PDF 2,111,245 B、sha256 `bdd246917c34df700c48cee9cf3408c2b08a79c2be5a2ee086bc3010ab7af740`。
- 缺陷与修复（只动字号，文字内容未动）：
- run1 无真缺陷；唯一 FAIL 为门 17 缺脚本 SKIP（production 与 fanout 均无 `audit_ko_es.py`），不是 FAIL，不阻塞。
- 门禁 run2：PASS=18 FAIL=1（run1：PASS=18 FAIL=1）。run TOTAL 150；head_check PASS 0 defects；d5 census 0/0/0；render RC=0；webpdf RC=0（2014558 B <7MB）；occlusion 0；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff vs base 新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0 defects（ratios n=378，中位 1.008，粗体 1.04，常规 0.988；P8 237→238 行，距页脚线余量 45.6px）；文字层 print=web 多重集差 0（各 29380 字符）；census_quotes 0 defective；D18 刊头间距 GAP=336.1；门 17：SKIP（无此脚本）。
- 新交付物（实测发运值）：印 PDF `Lucerna-VOL1-ES.pdf` 32,299,760 B、sha256 `04f39f85e127ff2f371a48d7673d112bd615cb48385c1dfc99f959784b488eb7`；网 PDF `Lucerna-VOL1-ES-web.pdf` 2,014,558 B、sha256 `149e7eb96c061158820ca5dcf5b6be65e831b6f1a4869ed9b0dc79eca422a409`（<7MB，待 closer 换入 `issues/2026-w43/2026-w43-ko-es/2026-w43-ko-es.pdf` 并更新 pin）；新建 text.md `2026-w43-ko-es.text.md` 21,826 B、sha256 `b1030867277595f89a8aa157e60ea205873dcfb49d9973ff5455d443da09e656`，与 fanout `.text.md.new` BYTE-IDENTICAL，`verify_textexp_ko.py --edition` ADOPT。
- KIT 旧值（印 34,453,333 B / 网 3,115,958 B，旧配方）已过期——基线实测印 34,436,845 B。本节交付物行已更新为上述 D5 新值。
