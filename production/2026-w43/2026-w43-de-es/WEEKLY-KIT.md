# Die Lucerna VOL.1 — DE × ES Edition KIT

**Edition:** German target text + explanations in Spanish (edición para lectores hispanohablantes)
**Masthead:** Die Lucerna · SEMANARIO ALEMÁN VOL.1
**Week:** Monday 2026-10-19 → Sunday 2026-10-25 (W43) · Lead: „Eine Stunde geschenkt" — Zeitumstellung Sun Oct 25, 03:00→02:00; Herbstferien peak, 11 Länder.
**Pairing badge (P1):** «TEXTOS EN ALEMÁN · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES» (brick #a4553a, bold)
**Footers:** «Die Lucerna · SEMANARIO ALEMÁN VOL.1 · TEXTO EN ALEMÁN · EXPLICACIONES EN ESPAÑOL» / «Página N de 8»
**Gloss prefix:** «Nota — »

## Method (fan-out from the finalized DE core)
- Build dir: `hidden_files/weekly-report-de-es-build/` (copy of the core build dir `hidden_files/weekly-report-de-build/`).
- **Baseline proof:** the unmodified copy, with output redirected to /tmp, reproduced all 8 shipped core SVGs **byte-identically** (sha256 diff clean) before any edit. Registry total of the baseline: 150.
- Only the explanation layer was rewritten, into native Spanish: every definition, grammar note, instruction, exercise rubric and **all P8 answer notes**. The core's explanation helper was renamed `expl()` in this build; no intermediary-layer terminology appears anywhere in paper, KIT or code.
- All diffs/registries below are against the **core** (`files/weekly-report-de-vol1/`), never a sibling.

## Totals (identical to core)
- **150 exercises — A2 67 · B1 69 · B2 14**; per page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- Final build log: zero `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings; P8 keys end y=2361 (limit 2560).

## Freeze verification (German target text)
- SVG text-multiset diff vs core: every non-Chinese core text element survives except (a) the P1 tagline, replaced by the ES pairing badge by design; (b) P8 key lines whose Chinese notes were re-parenthesized (full-width → half-width, space before the note parenthesis) and re-wrapped at the smaller key size — the keys themselves are registry-proven identical (below); (c) fragments of Chinese gloss elements replaced by their Spanish versions. **Zero CJK characters remain in the ES SVGs.**
- P7 verbatim check: all 8 German phrases of the week occur exactly 2× in the issue text (article + P7), same as core.
- Registry diff vs core: levels and keys identical for 147/150 items. **Key-diff registry (documented reader-language items only):**
  - **#137** (Traduce al español): key „La noche tiene 25 horas." (core key was the Chinese translation of the same German stem).
  - **#138** (Traduce al español): key „El sábado por la noche ajusto el reloj."
  - **#150** (writing, apparatus key): „Pregunta abierta — sigue los puntos del cuadro de escritura; el texto modelo está en el cuadro de esta página" (note: „Se califica según los puntos indicados").
  - **#139/#140** stems re-aimed into Spanish („El domingo duermo una hora más." / „En la biblioteca se pueden prestar libros."); their German keys are byte-identical to core.
  - 135/150 answer notes translated into Spanish; the 15 identical notes are language-neutral (e.g. „trennbar: um-ge-stellt", „46 + 18 = 64", „halb vier = 3:30"). One consistency fix during proofread: #123's note gloss aligned to „O bis O = de octubre a Pascua" (Pascua, matching the P7 toolbox).

## Layout adjudications (wording-only fixes; geometry never changed)
Spanish runs longer than the core's Chinese; the following explanation strings were shortened so every box, title and column ends inside its core geometry (all measured with production glyph metrics before rebuilding):
- P1 FRAGEN box line → „Las guías de todo el país las responden." (the slot is a single unwrapped line; the first version in
...[truncated 5016 chars]
---

## KIT completion + INDEPENDENT PROOFREAD RECORD (2026-10-21)

**⚠ KIT truncation found by the proofreader:** this file as delivered by the build ends mid-sentence in "Layout adjudications" — its final bytes are the literal marker `...[truncated 5016 chars]` (file was 3,833 B). The tail of the adjudication list, the builder's audit record, the deliverables/PDF pins and the PENDING proofread marker were therefore not present in the file. The paper itself is unaffected. Rather than reconstruct the builder's missing prose, this record (a) flags the truncation, and (b) supplies the verified final-state data those sections would have carried, all measured independently by the proofreader. The builder's surviving claims were each re-verified against the shipped artifacts; every claim checked out (see below), except that the full list of 10 in-build wording fixes is only partially recoverable from the truncated KIT (first bullet survives) — the final state itself passes every gate check on the proofreader's own measurements.

**Baselines (proofreader, independent rebuilds in an isolated copy):** the core build reproduces all 8 shipped core SVGs byte-identically; the DE×ES build reproduces all 8 shipped ES SVGs byte-identically. Registry totals identical: **150 exercises — A2 67 · B1 69 · B2 14**; per page 10/18/18/18/18/18/12/38; numbering 1–150 continuous in both registries and in the printed P8 keys.

**Freeze / key-diff verification:** registry keys differ from the core at exactly the three documented items — #137 key „La noche tiene 25 horas." (faithful to the printed stem „Die Nacht hat 25 Stunden."), #138 key „El sábado por la noche ajusto el reloj." (faithful to „Ich stelle die Uhr am Samstagabend um."), #150 apparatus in Spanish; #139/#140 stems re-aimed into Spanish with German keys byte-identical (and faithful to the Spanish stems). All other 147 keys byte-identical. Notes: 135 translated into Spanish; the 15 identical notes verified one by one as genuinely language-neutral (German verb forms, „trennbar: um-ge-stellt", arithmetic „46 + 18 = 64", „halb vier = 3:30" etc.). All 150 keys appear verbatim in the printed P8 answers. **All 150 exercises re-solved independently** by the proofreader against the printed stems, articles, fixture table and chart (46+22+18+14=100; the chart is labelled practice data in both languages): 150/150 keys correct. Writing model = 87 words, as printed.

**Spanish completeness:** zero CJK characters in the final SVGs (text layer and raw bytes). Full read of all 8 pages: every definition, rubric, instruction and all 150 P8 answer notes in Spanish. Pairing badge on P1; pairing footers + «Página N de 8» on all 8 pages; masthead «Die Lucerna». P7: all 8 phrases verbatim from this issue's articles, each exactly 2× in the issue text, page tags correct; visual check of the P7 card — no phrase tag struck through by a neighbouring quote (the in-build fix holds). Weekday/date claims all verified against the real 2026 calendar (Zeitumstellung Sun Oct 25, 03:00→02:00; Oct 24 Sat; Oct 31 Sat; Nov 1 Sun; Oct 26 Mon; Winterzeit ends Sun Mar 28, 2027). Banned intermediary-layer term: 0 hits in paper, KIT and build code. Images: payloads byte-identical to the core on every page; credits match the placed images (P1 Courtney Celley / U.S. Fish & Wildlife Service, P2 NIST, P3 Lucas Cranach d. Ä. 1528, P5 U.S. Department of Agriculture — all public domain).

**Geometric occlusion audit — flag-set diff (the decisive test):** the build's audit script (`audit_de_es.py`, family method: paint order, production font metrics, ink band baseline −0.88em…+0.30em, line boxes stroke-expanded, synthetic-control lineage) was run by the proofreader on BOTH editions' shipped SVGs:
- **DE×ES: 21 flags** — P2 ×1, P3 ×1, P4 ×18, P5 ×1, all BOXTITLE class.
- **Core: 26 flags** — the same 21 elements with identical measured values, plus 5 further flags on Chinese gloss lines (P1 Fragen head, P2/P3/P5 «Und Sie?» lines, P4 reader line) that the Spanish text renders without flagging.
- **Every one of the 21 ES flags has an identical core counterpart at the same element — ES-only flags: ZERO.**
- The supplementary text–text scan reports exactly 1 overlap in each edition: the P1 masthead pair («Die Lucerna» @262 vs the edition line @330).
- The proofreader's own independent audit (separate implementation, positive control validated — COVER/LINEX/FOOTER/EDGE/TEXTX all fire on synthetic defects): **COVER 0, LINEX 0, EDGE 0, FOOTER-crossing 0 on both editions**; TEXTX only the shared P1 masthead pair.
- Pixel adjudications on the shipped cards: P1 masthead — wordmark ink rows 141–264, edition-line ink from row 295, ≈30 rows of clear air (band-model artefact, non-defect). P4 fixture table — all 7 rows render cleanly inside their zebra bands (the 18 flags are the audit matching each row's text to the previous row's rect; identical in the core). P2/P3/P5 facts boxes — the flagged last lines („besser, sagen die Reifenexperten." / „(Kappel-Grafenhausen)." / „die Ferien.") render fully visible below the box border with the following box clear beneath: the cosmetic border-crossing class documented in the core KIT (sweep observations, deliberately not fixed), no information hidden, nothing struck through.

**Deliverables (D5 重建，2026-11-13):** svg/ ×8, cards/ ×8 (1950×2700), print PDF `The-Lucerna-VOL1-de-es.pdf` 9,357,158 B sha256 `661e99b2d2c14cf9b29035dd5c1f33b253290010a3ba71b3cd66abcfaad4280c`, web PDF `2026-w43-de-es.web.pdf` **1,469,088 B (< 7 MB)** sha256 `01c044ea24c90d9d7e0aa59620b66d7986db7e0b46cafdfb180847d93725f62e`. 旧配方值 10,503,920 B / 4,283,213 B 已过期，见末节 D5 记录。

**VERDICT: PASS** — one complete independent pass, zero problems in the paper. No fixes were needed and nothing was re-rendered; the only repair made by the proofreader is this KIT completion record. This edition is clear for repo insert by the parent line. (Discord delivery is paused; nothing posted.)
## D5 重建记录（2026-11-13，W43/W45/W46 D5+§1.1 合并重修 Phase 1）

- **原因**：D5 缺陷——sans 层拉丁/西里尔字符落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者）。本版修前 census：D5 拉丁 670、西里尔 0、弯引号 CJK 0。
- **安装**：`tools/mechanism-w47/apply_variant.py --svglib <版>/svglib.py --target de --reader es --week 2026-w43`（先 `--check` dry-run 通过）。`_D5_READER = "latin"`。路由单元测试 `test_d5_routing.py` FAILURES: 0。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 33 个全在 Newsreader。
- **基线**：重建前先证基线干净——`run.py` TOTAL 150、0 警告；重建 SVG 8/8 与 port fanout 逐字节相同；印 PDF 与 fanout BYTE-IDENTICAL。基线实测（§1.1 组装版）：印 PDF `91932d71e114b89a7638efa5d221402ee820eb2ce3576bd8f1313139454d592d`（9947962 B）、网 PDF `e14539b0d2f81ccfe0dcf3ba1197739d0ee3f104757d3dec05b4f9d1e8995db9`（1556483 B）。本 KIT 上方旧值（更旧配方）已过期，以上两值为准。
- **二次修复（只动字号与断行，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 两 p.text 标题内宽 400.5）**：
  1. `content12.py:25` P1 band 标题 36→31pt（与最紧 band-right 左界 ru 1542.0 间隙 76.7px）。
  2. `content12.py:124` herbst 头 25→22pt（框宽 422.5；25pt 430.2 超 7.7px，22pt 378.6）。
  3. `content12.py:47` numbers 盒 `f.box` 加 tsize=21（最差 +25.8；21pt 最大 392.8 < 404.5）。
  4. `content12.py:89` contents `IN DIESER AUSGABE` 24→22pt（最差 +9.0）。
  5. `content12.py:175` merksatz 盒 `f.box` 加 tsize=21（最差 +25.5；21pt 最大 392.5 < 404.5）。
  6. `content34.py:35` / `content56.py:34` P3/P5 facts 盒 +14→+34（末行溢出约 12.7px；en 家先例）。
  7. `content56.py:56` P5 Saturday-plan 头 24→22pt（nl +55.3；22pt 829.3 < 849.4）。
  8. `content56.py:155` P6 timeline 头 24→22pt（pt +10.3；22pt 376.1 < 400.5）。
  9. `content7.py:72` Toolbox 23→21pt（最差 +23.0；21pt 最大 386.4 < 400.5；22pt en 404.7 仍超）。
  10. `content7.py:92` NOCH EIN WORT 22→21pt（最差 +11.6；21pt 393.0 < 400.5）。
  11. `content8.py:74` P8 D 组头 24→22pt（it 428.3、nl 431.5 均超 422.5；22pt 最大 395.6）。
  12. `content56.py:204` P6 图注 19.5→18pt（es 仅有；18pt 右界 1795.7 < 1832）。
- P2 例外（run2b）：P2 facts 盒改回 +14（高度不变），facts 正文 21.5→21pt（wrap 8→7 行，盒底 356，余 22.1px）；P3/P5 保持 +34。
- **P8**：行数 225→229，距页脚线余量 33.3px；p8 compare CLEAN（keydiff [137, 138, 150]）。
- **新交付物（D5 重建，2026-11-13）**：印 PDF `661e99b2d2c14cf9b29035dd5c1f33b253290010a3ba71b3cd66abcfaad4280c`（9357158 B）；网 PDF `01c044ea24c90d9d7e0aa59620b66d7986db7e0b46cafdfb180847d93725f62e`（1469088 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差 1 字节），以最终实测值为准。
- **text.md**：D5 不改文字内容；交付件为 port `.text.md.new` 原样沿用（BYTE-IDENTICAL，51137 B，sha256 `8f3547d131244e2c441f460d62785d59bdd57f4adcc97d00a8f40e016b418782`，570 条目 / 150 习题）；重建后重出 token-identical（rewrap RC=0）。本家 `issues/` 无已发 `.text.md`，基线以 port fanout 为准。
- **D5 门禁（17 门，run2b，全绿 ALL-GREEN）**：run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1469088 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=575，中位 1.003）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A；D18 刊头间距 44.6px。日志：`hidden_files/d5-redo/scratch-2026-w43-de/logs/2026-w43-de-es/`（`GATES-SUMMARY.txt` 为总表）。D5 报告：`production/notes/2026-w43/g-de/scratch-d5-rebuild-de/D5-REPORT-2026-w43-de-es.md`。
