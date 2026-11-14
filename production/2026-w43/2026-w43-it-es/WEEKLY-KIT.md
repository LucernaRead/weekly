# WEEKLY KIT — Lucerna Weekly · IT × ES (W43 · VOL.1)

- **Edition**: Italian target text (frozen core) + explanations written natively in Spanish.
- **Pairing**: target `it` × reader native `es` — masthead «La Lucerna» (as shipped by the core); week Mon 19 – Sun 25 Oct 2026 (W43).
- **Deliverables dir**: `files/weekly-report-it-es/` — `svg/` ×8, `cards/` ×8 (1950×2700), `Lucerna-VOL1-ES.pdf` (print), `Lucerna-VOL1-ES-web.pdf` (web, < 10 MB).
- **Build dir**: `hidden_files/weekly-report-it-es-build/` (copy of the core build; baseline proven byte-identical before any edit).

## Totals (= core, re-counted from the registry)

- **150 exercises**: A2 46 · B1 71 · B2 33.
- Per page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38. Writing model: 90 words (#150, section H).
- Type mix (labels localized in Spanish): Completar 60 · Opción múltiple 49 · Emparejar 12 · Formar frases 7 · Transformación 1 · Verdadero o falso 3 · Cloze 13 · Traducción 4 · Escritura 1.

## Method

1. Copied the core build dir; proved the unmodified copy reproduces all 8 shipped core SVGs **byte-identically** (sha256 vs the shipped files), registry identical (150; page/level/type splits; 90-word model).
2. Rewrote ONLY the explanation layer into native Spanish: every definition, grammar note, instruction, furniture gloss and **all 150 P8 answer notes** — format `key (nota)` with half-width parentheses and a space before each note parenthesis. The inherited explanation helper was renamed (`expl()`); the banned intermediary-layer term appears nowhere in paper, KIT or code (final scan: 0 hits; CJK characters in the final SVGs: 0).
3. Furniture (ES column pattern, every line measured with the build's own real-font metrics):
   - P1 badge (brick #a4553a, bold, one line, 1077px): «TEXTOS EN ITALIANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES»; edition line «SEMANARIO ITALIANO · VOL.1 · L'ORA SOLARE · IL MALTEMPO · IL CINEMA» (1782px) at y=330, badge at y=372.
   - Footers: «La Lucerna · SEMANARIO ITALIANO VOL.1 · TEXTO EN ITALIANO · EXPLICACIONES EN ESPAÑOL» / «Página N de 8».
   - Gloss prefix «Nota — » everywhere the core used the Chinese gloss label.

## Freeze verification (vs the CORE, never a sibling)

- Source diff classified line-by-line: every change is explanation layer, furniture, output paths, the P8 key-format, or a box title size — the Italian target text was never retyped (all replacements were exact-match anchored).
- **Image payloads byte-identical on all 8 pages** (base64 data URIs compared core vs ES).
- Registry diff (machine-generated dumps): number / page / level / type identical for all 150 items.

## Key-diff registry (only these keys differ from the core — the reader-language items)

| # | Core key | ES key | Why |
|---|---|---|---|
| 137 | Italian→Chinese translation | «El domingo dormimos una hora más.» | Traducción re-aimed: Italian → Spanish |
| 138 | Italian→Chinese translation | «La exposición sigue abierta hasta abril.» | Traducción re-aimed: Italian → Spanish |
| 150 | ✓ + Chinese note | «✓ El modelo está en la sección H (90 palabras)» | Writing note in Spanish |
| 139 | Italian key (unchanged) | stem re-aimed: Spanish sentence given, translate into Italian | Key stays Italian, byte-identical to core |
| 140 | Italian key (unchanged) | stem re-aimed: Spanish sentence given, translate into Italian | Key stays Italian, byte-identical to core |

Every other note was re-authored in Spanish from the core's note; the only note textually identical to the core is #86 «5 − 3,4 = 1,6» (language-neutral arithmetic, by design).

## Layout adjudications (wording-only trims; no geometry moved vs the core)

- P6 §A instruction shortened to «Mira los gráficos y elige la respuesta.» — the P6 exercise flow now ends at y=2569, exactly the core parity.
- P8 keys: 12 notes shortened so every key line wraps to exactly one line (keys flow ends y=2396; core 2366; bottom 2552) — e.g. #23 «semana normal: no hay fiesta nacional de otoño», #58 «più + bella, opinión subjetiva».
- P7 col-3 parola/lettere Spanish notes shortened (column ends y=1645 vs core 1674; clears the frasi rule at y=1686).
- P1 headline expl kept at 4 lines (flow ends y=1837; hard rule at 1864).
- **P1 CIFRE box title**: the bilingual title crossed its box border by 133.6px at the core's size — fixed by shortening the title to «LA SETTIMANA IN CIFRE · EN CIFRAS» and setting that box's title size to 20 (title ink 362px, inside the border).
- **P1 word-of-week gloss**: the first Spanish draft wrapped to 2 lines and its second line was struck through by the rule at y=1864 (pixel-confirmed on the rendered card) — fixed by shortening the gloss to one line: ««Mal tiempo»: lluvia, viento y tormentas: Adam.»
- P8 #126 note: «partió» → «se envió a Bruselas» for faithfulness to the core's note.

## Geometric occlusion audit (builder pass, on the final SVGs)

- Scripts: `audit_it_es.py` (paint-order coverage with real-font PIL glyph metrics; line boxes expanded by half the stroke width; footer band y>2580; page-edge spill), `audit_titles.py` (box titles vs their own borders), `audit_texttext.py`.
- **Synthetic positive control passed first**: a crafted SVG with planted cover/line/footer/edge defects fired COVER 100%, LINEX, FOOTER and EDGE; clean text stayed silent.
- Final results: main audit **0 flags on all 8 pages**; box titles **0 crossings**; text-text overlaps: 1 — the masthead wordmark's 168pt blackletter bounding band vs the edition line (bounding-box artifact; visually confirmed clear air between the wordmark ink and the edition line on the rendered card — same adjudication as the core and all sibling editions).
- All 8 card PNGs viewed by the builder; the P1 trends footnote area and the word-of-week gloss read clean.

## Content verification (builder pass)

- Full visible text of all 8 pages extracted and read: Spanish apparatus is native and consistent (accents, agreement, ordinal abbreviations n.º / ª); every glossed term appears in the Italian text it glosses.
- All 150 keys re-checked against their stems and articles.
- Weekday/date claims verified against the real 2026 calendar: ora solare night Sat Oct 24 → Sun Oct 25, 03:00→02:00; matches Wed Oct 21 / Thu Oct 22 / Sat Oct 24 / Sun Oct 25; Lucca Comics opens Wed Oct 28; Ognissanti Sun Nov 1; Alba fair Oct 10 – Dec 6 (Sun); Manovra vote slips to ~Wed Oct 28; DPB sent Oct 15.
- Manovra honesty kept: the chart caption (Italian, frozen) states the three published components are not the total (~23,5), and P8 note #85 carries it in Spanish: «5 + 5 + 3,4 = 13,4: no es el total». Chart bars measure 5,0 / 5,0 / 3,4 (v×34, frozen from the core).
- P7 «Frasi della settimana» quotes are verbatim excerpts from this issue's own articles, with correct page tags (verified against the pages) and Spanish translations.

## PDFs (final render)

- Print: `The-Lucerna-VOL1-it-es.pdf` — 7991011 bytes, sha256 `8f49af4796d81839d3643b31f7ee85e046cfa9272fee3d362b5ab2d4254ea1dc` (D5 rebuild).
- Web: `2026-w43-it-es.web.pdf` — 1138034 bytes (< 7 MB), sha256 `7c8d9095bee4595135075cc8bb1eed10ee7ef3fceddaf4d1e1487ec412baa01f` (D5 rebuild, tools/webpdf.py shipped file; old 3,634,329 B value was the render.py-era web PDF).

## Proofread status

- Builder's own full proofread + geometric audit: **done** (this KIT).
- Independent proofread: **PASS — one complete independent pass, zero problems; no fixes needed, nothing re-rendered, core untouched** (fresh proofreader, 2026-10-21). Evidence:
  - **Reproducibility**: an isolated copy of the core build (paths redirected) reproduces all 8 shipped core SVGs byte-identically; an isolated copy of this ES build likewise reproduces all 8 shipped ES SVGs byte-identically.
  - **Registry diff (machine-generated dumps, core vs ES)**: n / page / level identical for all 150; types identical modulo the Spanish localization; **key diffs exactly {#137, #138, #150}**; notes differ at 149/150, the only identical note being #86 «5 − 3,4 = 1,6» (language-neutral) — the builder's registry claims are exact.
  - **Freeze diff**: per-page text-element multiset diff vs the core — every differing string classifies as Spanish explanation layer, pairing furniture (badge, «La Lucerna · SEMANARIO ITALIANO VOL.1 · TEXTO EN ITALIANO · EXPLICACIONES EN ESPAÑOL» footers, «Página N de 8»), or a registry item; source-literal diff (AST) shows no Italian article literal changed; `svglib.py` byte-identical; `bslib4.py` diff = footers + `bridge()`→`expl()` rename + «Nota — » gloss prefix only. Shape counts per page identical to the core; geometry deltas are flow reflow from the translated explanations only. The P1 strap line was replaced by the pairing badge (the established sibling-edition pattern). No Italian target-text change outside the registry.
  - **Keys re-derived independently**: all 150 keys re-solved from the printed Italian stems/articles/tables and compared — all correct, including the matching sets (25–28, 52–55, 141–144), the comparatives #56–58 (schedule-table times), the congiuntivo set #93–96/#109–112, and the 90-word model (recounted: 90). #137 «El domingo dormimos una hora más.» and #138 «La exposición sigue abierta hasta abril.» are faithful to the printed Italian stems; #139/#140 stems re-aimed into Spanish with Italian keys byte-identical to the core.
  - **Totals/numbering**: 150 exercises, A2 46 · B1 71 · B2 33, pages 10/18/18/18/18/18/12/38; numbering 1–150 continuous on the pages and in the P8 key list.
  - **P7 phrases**: all 8 quotes verified programmatically in the ES render — verbatim contiguous excerpts, each occurring exactly 2× issue-wide (article + P7 box), each on its tagged page (1,1,2,2,3,4,5,6).
  - **Dates/weekdays**: every claim checked against the real 2026 calendar — ora solare night Sat 24 → Sun 25 Oct, 03:00→02:00; Lucca opens Wed 28 Oct, closes Sun 1 Nov (Ognissanti); Artemisia opens Wed 21 Oct; Alba fair Sat 10 Oct – Sun 6 Dec; DPB sent Thu 15 Oct; braccialetto deadline Fri 16 Oct; manovra vote Wed 23 Oct → ~Wed 28 Oct; last Sunday of March 2027 = 28 Mar. Manovra arithmetic verified: 5 + 5 + 3,4 = 13,4 ≠ total 23,5; 5 − 3,4 = 1,6; chart bars measured in the SVG at 170.0 / 170.0 / 115.6 px = values × 34, byte-identical to the core; the frozen Italian caption («non è il totale della manovra (circa 23,5 miliardi)») and the Spanish #85 note both carry the honesty note.
  - **Spanish apparatus**: read in full on all 8 pages — native and complete (all instructions, glosses, section heads, and all 150 P8 notes in Spanish, `key (nota)` format, half-width parentheses); CJK characters in the final SVGs: **0** (decoded scan); residual Chinese/English apparatus: none (the P1 Trends footnote's date lives in the frozen Italian line directly above it).
  - **Geometric occlusion audit (proofreader's own implementation)**: paint-order scan with PIL real-font glyph metrics, line boxes expanded by half the stroke width; synthetic positive control fired all five defect classes (COVER 100%, LINEX, FOOTER, EDGE, TITLE) and stayed silent on clean text. On the shipped ES SVGs: COVER 0, LINEX 0, EDGE 0, TITLE 0 on all 8 pages; the only FOOTER hits are the pages' own footer lines at baseline 2624 (by design; identical 16-hit profile on the frozen core). The P1 word-of-week gloss was pixel-measured on the rendered card: ink rows 1831–1850, rule at y=1864 — 13 rows of clear air, no contact (the builder's one-line fix confirmed). The P1 CIFRE box title sits inside its border (builder's fix confirmed geometrically and visually). All 8 cards viewed: no covered, clipped or struck-through text.
  - **Images/credits**: embedded payloads byte-identical to the core on every page (P1×1, P3×2, P5×1); credit lines identical to the core and matching the placed images and `assets/CREDITS.md` (NIST PD; tartufo PD; Artemisia PD; Chaplin PD).
  - **Banned-term scan**: the intermediary-layer term (Chinese and English forms) = 0 hits in the paper SVGs, this KIT, and the build code.
  - **PDFs (measured by the proofreader)**: web `Lucerna-VOL1-ES-web.pdf` = 3,634,329 bytes (< 10 MB), 8 pages, sha256 `074f9f5cfe56df0b75fca1a19b03862a164496a1bc08f08d931621bf72c61095`; print = 9,078,493 bytes, sha256 `6aefc9a1574fb297f6d8bfc24fbd79a04a464157aff1cf29c4279c5370e47840` — both match the values pinned above.
  - Cleared for repo insert by the parent line (no Discord delivery — paused; no insert performed by the proofreader).

## Reproduction

```
cd hidden_files/weekly-report-it-es-build
/tmp/wp-venv/bin/python run.py      # build SVGs (registry: 150)
/tmp/wp-venv/bin/python render.py   # cards + print/web PDFs
/tmp/wp-venv/bin/python audit_it_es.py ../../files/weekly-report-it-es/svg
/tmp/wp-venv/bin/python audit_titles.py ../../files/weekly-report-it-es/svg
```

---

## D5 rebuild (2026-11-13)

D5 + §1.1 合并重建记录（2026-11-13；一任 builder 至 run2 循环，二任 builder 接手核实 + gate 2 补跑；不 commit、不 push；独立重校另派他人）。

- 装机：`apply_variant.py --patch-core it --week 2026-w43 --i-understand-this-writes-production`（core-it 落盘 `_D5_READER = "latin"`）；本版 `apply_variant.py --svglib <版>/svglib.py --target it --reader es --week 2026-w43`，`_D5_READER = "latin"`；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2（U+201C/U+201D/U+2019 → serif）保留。
- 基线：run TOTAL 150、0 警告；SVG 8/8 与 fanout 逐字节相同；印 PDF 与 fanout SHA 一致（8502651 B）；修前普查 D5 拉丁 487 / 西里尔 0 / 弯引号 CJK 0。
- 二次修复（只动字号，文字零改动；盒修法行号指 tsize 行，D19）：`content34.py:22` P3 头 25→22; `content12.py:181` P2 盒 `LA FRASE PER RICORDARE　LA CLAVE` tsize 20→19（394.5，余 10.0px）; `content7.py:73` P7 `ERRORI TIPICI　ERRORES TÍPICOS` p.text 23→21（390.3，余 10.2px）。
- P8：行数 231→231，距页脚线余量 44.3 px；p8 compare CLEAN（keydiff [137, 138]）。
- 新交付物：印 PDF `The-Lucerna-VOL1-it-es.pdf` `8f49af4796d81839d3643b31f7ee85e046cfa9272fee3d362b5ab2d4254ea1dc`（7991011 B；修前 `b60d8ffc5839705d47633ae085fd1886ac0f6c35ed834aa07e6d07ab17427b36`，8502651 B）；网 PDF（tools/webpdf.py）`7c8d9095bee4595135075cc8bb1eed10ee7ef3fceddaf4d1e1487ec412baa01f`（1138034 B；已发版 `58ccf156c60e7e3bf86fc081994d8126300b7aa1cf22575fffbd1f999049da05`，1248878 B）；text.md 与 fanout `.text.md.new` BYTE-IDENTICAL（55439 B，SHA `5885318af21eccc8bf7127d1b156df2bb33696de2275f8a9f85610f6cf16affc`），W43 it issues/ 内无已发 `.text.md`，closer 落仓时新建补入。
- 门禁 run2 ALL-GREEN（18 门：run TOTAL 150 / head_check 0 / d5 census 0/0/0 / render RC=0 / webpdf RC=0 / occlusion 0 / p8 extract 150/150 / p8 compare CLEAN / freeze baseline 8/8 / freeze diff 新增 CJK TOTAL 0 / spill 0 / boxtitle 0 DEFECT（24 titles、239 body lines）/ edge 0/0 / creambox PASS 0 defects（n=395）/ 文字层 print=web 多重集差 0 / census_quotes 0 defective / 家族 gates.py N/A / 刊头间距 279.4 px PASS）。日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-es/GATES-SUMMARY.txt`；D5 报告：`production/notes/2026-w43/g-it/scratch-d5-rebuild-it/D5-REPORT-2026-w43-it-es.md`。
- 本 KIT 交付物行已更新为以上 D5 新值；旧针脚为旧配方值，已过期，以上实测发运值为准。
