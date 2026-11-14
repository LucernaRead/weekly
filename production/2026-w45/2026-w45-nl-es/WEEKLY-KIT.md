# WEEKLY KIT — De Lucerna, VOL.2 (NL × ES, W45)

## 1. Identity and pairing (as printed)

- **Issue week:** Monday 2 November – Sunday 8 November 2026; issue dated Monday 2 November 2026.
- **Volume:** VOL.2 for Nederlands (sequel to W43 VOL.1).
- **Masthead:** De Lucerna (frozen from the NL core).
- **Pairing badge (P1, measured from the rendered SVG):** y=568, 20pt bold BRICK (#a4553a), centred —
  «TEXTOS EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES»
  (advance width 1116px, limit 1820px). Slot follows the W43 NL×ES precedent: inserted between the
  band (ends y=542) and the headline label (y=606); the y=372 strapline stays frozen body text.
- **Footer (every page, measured):** «De Lucerna · SEMANARIO NEERLANDÉS VOL.2 · TEXTO EN NEERLANDÉS ·
  EXPLICACIONES EN ESPAÑOL» (20pt, advance 985px) / «Página N de 8».
- **Top strip:** «ELKE WEEK IN HET NEDERLANDS · CADA SEMANA EN NEERLANDÉS» (21pt, 661px).
- **P1 subtitle line:** «SEMANARIO NEERLANDÉS · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12»,
  kept at the core's 40pt serif bold — measured 1811px against the 1820px page width (fits by 9px;
  the W43 36pt fallback was NOT needed here).
- **Gloss prefix:** «Nota — » (W43 NL×ES precedent).
- **P8 separators:** «— PAGINA N —» — the W43 NL×ES shipped form (measured from its P8 SVG), kept
  verbatim; tables.json's «— PÁGINA N —» variant was NOT used (W43 measured wins over the table).
- **Format:** 8 pages (multiple of 4), page size 1950 × 2700, 4 columns, warm ivory paper, dark olive-green accents.
- **Lead topic (from the core, unchanged):** «Nederland in de Klimaatweek» — Klimaatweek (2–8 Nov),
  Museumnacht Amsterdam (7 Nov), Crossing Border Festival (3–8 Nov), Eredivisie matchday 12 (6–8 Nov).

## 2. Core measured values (W45 NL core, verified, not assumed from other families)

- **Total: 150 exercises.** By page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- By level: A2 47, B1 72, B2 31.
- By registry type (core): 完成句子 65, 单选 44, 词汇配对 8, 判断对错 7, 造句 8, 完形单选 13, 翻译 4, 写作 1.
- Model essay (P8 H, ex. 150): 87 words (requirement 80–100).
- Numbering continuous 1–150; P8 printed answers verified against the registry (p8.py extract: noted set = 150 of 150).
- Images (frozen from the core, all reused W43 NL build assets, Commons API Artist credits):
  P1 herfstbos — Vovogov90, CC0; P2 kinderdijk — Nationaal Archief, CC0;
  P3 gracht — W. Punt / Anefo, Nationaal Archief, CC0; P4 elftal1912 — Spaarnestad Photo, public domain.
  Every credited image is laid out on its page (verified in the rendered cards); no new images were added.

## 3. Baseline proof (before any explanation-layer change)

- The W45 NL core build was copied to `hidden_files/weekly-report-w45-nl-es-build/` with OUT repointed
  to the new edition dir, then run unmodified: **all 8 SVGs byte-identical to the shipped core (8/8 cmp)**.
- The proof was re-established a second time from an isolated scratch copy (HOME-redirected run):
  scratch core build reproduces the shipped core SVGs **8/8 byte-identical**.
- The shipped core SVGs were verified untouched at the end of the build: sha256 values match the
  baseline record exactly (p1 5424557b…, p2 78e6fcd2…, p3 5b9854e3…, p4 cc227fd9…, p5 e58064c9…,
  p6 6583fe28…, p7 65cfe2b3…, p8 fe22a151… — full values in the build log).

## 4. Freeze verification (builder self-gates, all measured)

- **freeze.py diff (core vs edition SVG text nodes):** p1 +29/−28, p2 +39/−33, p3 +32/−27, p4 +28/−25,
  p5 +38/−33, p6 +36/−32, p7 +51/−49, p8 +178/−166; **added CJK characters: 0 on every page, 0 total**.
  Edition SVGs contain **0 CJK characters and 0 full-width parentheses** on all 8 pages.
- **Registry-level diff (isolated scratch runs of both builds, REG dumped to JSON):**
  page and level identical for all 150 items; **key diffs: exactly 3 — #137, #138, #150** (see §5);
  type diffs: exactly 38, all P8 items #113–150 (Huecos 13, Elección 12, Frases 4, Traducción 4,
  Relacionar 4, Redacción 1 — the W43 NL×ES precedent: P1–P7 registry type names stay as the core's,
  since type names are never printed on P1–P7 pages); note diffs: 144 translated, 6 unchanged
  language-neutral notes (wij → planten; je → bespaar; rood = blijf binnen; ik → doe mee;
  hij → gaat praten; 45 + 25 = 70).
- **Dutch target text frozen:** all articles, prompts, options, chart data, captions, credits and
  golden sentences are byte-identical to the core, except the documented exceptions in §5 and the
  readers'-corner persona entry in §7 (W43 NL×ES precedent).
- **Banned string:** the banned intermediary term appears 0 times in the edition SVGs, the KIT and
  the edition build code (content modules + bslib; the gate script holds it only as its search needle).

## 5. P8 gate (tools/p8.py compare, dash style, total 150)

- **Status: CLEAN — core 150 noted, edition 150 noted, missing=[], extra_count=0, uncertain=[].**
- **Reported keydiff: [7, 17, 70, 71, 76, 96, 137, 138, 148] — adjudicated item by item:**
  - **True redirections (2):** #137 core key «气候周持续七天。» → «La Semana del Clima dura siete días.»
    (E translation NL→ES); #138 core key «橙色预警意味着：做好准备。» → «El código naranja significa:
    prepárate.» (E translation NL→ES). #139/#140 prompts were flipped ES→NL with Dutch keys unchanged
    (W43 precedent), so they correctly do NOT appear in keydiff.
  - **Extraction artifacts (7):** #7, #17, #70, #71, #76, #96, #148. For each, the printed key is verified
    identical from the raw P8 SVG answer lines (7: B; 17: wortelen; 70: eiland; 71: proef;
    76: gaat winnen; 96: advies; 148: B). The tool's paren branch misclassifies these dash-style lines
    because their (translated) notes end in a parenthesised fragment — e.g. «wortelen = echar raíces
    (sujeto plural)» — and returns key+note-minus-fragment as the pseudo-key, so the pseudo-key
    differs exactly because the note was translated. This is the documented p8.py paren-branch
    artifact class (key candidate must contain no parenthesis); the tool was NOT modified, since the
    shared tool's paren handling is validated for paren-style families and the artifact is fully
    explained and verified here from the raw lines.
  - **#150 (not in keydiff, real change, recorded):** the H key is explanation language by design:
    «（开放题，范文如下）» → «(Pregunta abierta — modelo a continuación)», with the note
    «El modelo está en la sección H de esta página (87 palabras)» (W43 precedent). Both sides extract
    to the check mark «✓», so the tool does not flag it.
- **EXTRA_ONLY does not apply:** status is CLEAN, not EXTRA_ONLY.

## 6. Gloss counts (split on · in the rendered gloss() string itself, per README #21)

- P2: core 6 → edition 6 (het klimaat / wortelen / besparen / de verwarming / de waarschuwing / lokaal).
- P3: core 5 → edition 5 (het museum / de rondleiding / het tijdslot / tweedehands / de beurs).
- P4: core 5 → edition 5 (de balans / gelijkspelen / de speelronde / de topper / de stand).
- P5: core 5 → edition 5 (het eiland / de proef / stemmen / de aflevering / voorbij).
- P6: core 5 → edition 5 (de meteoroloog / waarschuwingsmoeheid / vastzetten / het advies / de voorstander).
- **All five gloss boxes match the core 1:1.**

## 7. P7 gates

- **Word-box definition sentence (verbatim retention, measured):** ««meedoen» betekent: deelnemen,
  erbij zijn. In de Klimaatweek doet heel Nederland mee.» — core count 1, edition count 1, byte-identical.
  Only the gloss line below it was localised («meedoen = participar: en la Semana del Clima participa
  todo el país.»). No definition sentence was translated or edited.
- **Golden sentences:** all 8 core Dutch sentences appear exactly 2× in the edition (article + P7),
  with page labels matching the core: Pagina 1 ×2, Pagina 2 ×1, Pagina 3 ×1, Pagina 4 ×1, Pagina 5 ×1,
  Pagina 6 ×2; each quote was additionally verified to occur on its labelled page's article.
- **P7 teaching phrases:** all Dutch example/clinic phrases are core-frozen and unchanged; only their
  Spanish notes were localised.
- **Readers' corner — no fabrication, all three facts on the page, explicit invitation:**
  - No real reader letter exists for this issue; no reader, letter, name or quote was invented.
  - The box prints a clearly labelled editor's example: ««Hallo! Ik ben Lucía en ik leer Nederlands in
    Madrid. In de Klimaatweek plant ik een boom op mijn balkon!» — Lucía (voorbeeldbrief van de redactie)».
    Persona adaptation Li/Shanghai → Lucía/Madrid is the W43 NL×ES documented reader-language entry
    (the example sentence is Dutch, adapted only in name/city); it remains labelled as an editor's example.
  - The three facts are on the page in Dutch (frozen disclosure) and in Spanish:
    «Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte
    naar VOL.3.» / «Sin cartas reales ni mejores textos de la página 8 al cierre: publicamos este ejemplo;
    los prometemos para el VOL.3.»
  - **Explicit Spanish invitation, verbatim (imperative + publication promise):**
    «Ejemplo de la redacción, no una carta real. ¡Envíanos tu carta real y tu mejor texto! Los publicaremos
    en el VOL.3!»
    (Content-preview lines and exercise hints elsewhere were NOT counted as the invitation.)
  - P7 column-3 stack ends at y=1925.5, above the golden-sentences rule (y=1937) — 11.5px clearance.

## 8. Geometric occlusion audit (tools/occlusion_audit.py, selftest OK)

- **Final: edition 0 flags, core 0 flags, NEW vs core 0 flags.**
- **Same-baseline ink scan (additional, README #10):** 8 advance-width flags, all in the P1
  «IN DEZE EDITIE» contents rows (Pag. N / title / level) — byte-identical to the core's own 8 flags
  for the same frozen rows (advance-width artifacts; true-ink audit reports 0). The P1 top band
  (VOL.2 / strip / date, y=92) is clean.
- **Chart-label coverage (additional, README #12):** P6 chart labels vs later-drawn bars — 0% coverage
  on all 4 rows (label ink bottom to bar top clearance 4px each; no clipping, below the 30% COVER
  threshold and below any graze).
- **Fix history (each re-render preceded by a full sha256 record of the current SVGs/cards/PDFs):**
  - Fix-0: P1 headline flow and P2 exercise flow overflowed (bridge/box Spanish lines added lines and
    pushed blocks across column boundaries). Fixed by shortening only Spanish explanation text to restore
    the core's line counts: P1 bridge (4→3 lines), P1 cijfers lines 200 (4→3) and 9 (3→2),
    P2 bridges A and C (2→1 lines each). After the fix, P1-headline ends at the core's y=1452 and
    P2-ex at the core's y=2407, with zero FLOW OVERFLOW / HEAD TOO WIDE warnings.
  - Fix-1: occlusion audit found 2 NEW flags — P1 word-of-week Spanish note covered by the IN HET KORT
    box, and P7 BRIEVEN box overlapping the golden-sentences rows (Spanish notes added lines to the
    PAS OP and BRIEVEN boxes; col-3 stack ended at y=2101.5 vs the 1937 rule). Fixed by shortening only
    Spanish notes (PAS OP notes to 1/1/1/2 lines; BRIEVEN disclosure and invitation to 3 lines each;
    P1 word-of-week note to 2 lines). After the fix, occlusion reads 0/0/0 and P7 col-3 ends at 1925.5.
  - Final build: **zero FLOW OVERFLOW / HEAD TOO WIDE warnings** in the full one-process run.

## 9. Furniture comparison vs W43 NL×ES (measured, not README #20 generic)

- Badge: same slot/geometry as W43 (y=568, 20pt bold BRICK, centred, full badge string) — W43 measured wins.
- Footer: W43 form with VOL.1 → VOL.2 (target core's volume).
- Gloss prefix «Nota — », P8 answer flow 13.0pt/1.12/0.4, P8 separators «— PAGINA N —»,
  P8 type renames (38 items), E-section 2-keys-translated + 2-prompts-flipped, H key in the reader
  language — all copied from the W43 NL×ES shipped build/code, not from generic tables.
- Deviations from W43 (recorded, with reason): P1 subtitle kept at 40pt (measured 1811px fits; W43
  needed 36pt because its string measured 1972px); P6 chart title shortened to «DE GRAFIEK · EL GRÁFICO»
  and the pro/contra title to «VOOR OF TEGEN? · PROS Y CONTRAS» (both measured over the 390px box-inner
  width in their long forms: 574px and 458px); P1 cijfers title kept in the W43 short form
  «DE WEEK IN CIJFERS · EN CIFRAS» (380px vs the 390px limit).
- W43-measured values that overrode tables.json: P8 separator «PAGINA» (not «PÁGINA»); badge slot
  y=568 inserted (not a subtitle-slot replacement — the NL family has no free subtitle slot).

## 10. Toolchain

- **run.py:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0 (measured in the venv).
- **render.py (CairoSVG):** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0, cairosvg installed
  (system python3 is 3.12.3 / Pillow 10.2.0 but lacks cairosvg, so it was NOT used for rendering).
- **Byte-reproduction:** the unmodified core build copy reproduced the shipped core SVGs 8/8
  byte-identical under the venv interpreter (see §3); the edition build uses the same interpreter.
- **Line-width measurement:** all widths in this KIT are rendered-SVG/PIL measurements (svglib text_w
  on the production fonts), never advance-width guesses from other families.

## 11. Delivery (files only — NOT pushed to git, NOT posted to Discord, NOT messaged anywhere)

- `files/weekly-report-w45-nl-es/` — `svg/` (8 SVGs), `cards/` (8 PNGs, 1950×2700),
  `De-Lucerna-VOL2-nl-es.pdf` (print, 8 pages, 6,941,183 bytes,
  sha256 9976e67b8a809e58d1f1f4e799657dd0421881af849e2d46c9a424b79fc37d28),
  `De-Lucerna-VOL2-web.pdf` (web, 8 pages, 1,019,584 bytes < 10 MB,
  sha256 708b9f5fbd2e6b203aedfc23a649fd5a144c38fb66d55831cd48d27bd972112d),
  `WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (Spanish, one line, no ASCII double quotes).
- SVG sha256 (final): p1 b1737f90…, p2 7e39848d…, p3 80ba540e…, p4 3cce6dff…, p5 3b984901…,
  p6 e9daa31b…, p7 6131d67a…, p8 0b23b55f… (full values in the build log).
- Build tree: `hidden_files/weekly-report-w45-nl-es-build/` — build log (build-log-fix1.txt),
  pre-render sha256 records, transform_es.py, gates.py + gates-out.txt, freeze-diff.txt,
  p8-compare.txt, occlusion.txt / occlusion-fix1.txt, rowcheck.py + rowcheck-out.txt.
- **Builder status: builder-complete on all self-gates above. NOT finalised — independent proofread
  is still required before finalisation (per task instruction, no finalisation is claimed here).**

## 12. Visual inspection record (builder's own pass over rendered cards, 8/8)

- All 8 cards read end to end: no overlaps, no cut-off text, no defects. P1 badge/subtitle/word-note
  clear of the IN HET KORT box; P7 BRIEVEN box clear of the golden-sentences rule; P6 chart labels
  clear of bars; P8 answer flow ends well above the footer; footers read «Página N de 8» on all pages.

## 13. D5 rebuild (2026-11-14, builder run; not a proofread round)

D5: 讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK（SOP §1.1 字体修复）。D5-only 家族：新样式已在仓，单版施工只装 D5、重渲一次。

- Core 落盘（全家共用一次，v1 执行）：`apply_variant.py --patch-core nl --week 2026-w45 --i-understand-this-writes-production` → `production/2026-w45/core-nl/svglib.py` +95/−3 行，`_D5_READER = "latin"`（D24：按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-nl-es/svglib.py --target nl --reader es --week 2026-w45`（先 `--check` dry-run，mode=latin）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（svglib.py 含 fix2 标记 13 处，安装器日志 "added fix2 block"）。
- 基线（修前生产版，venv 重建）：`run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；印 PDF 7,526,083 字节；印/网文字层 vs issues 已发 web PDF 字符多重集差 **0**；修前普查 D5 违规 **拉丁 494**（>0，符合装机前提）。旧 pin 与基线实测不符（de 例：KIT 印 7,918,211 B，基线实测 7,526,971 B）——KIT SHA 滞后（PLAN 修正案：基线永不以 KIT SHA 为准），本节 pin 以实测发运值订正，旧 §11 pin 已同步更新为本次值。
- 导出器（第 0 步自验）：`scratch-2026-w45-nl/export_text_w45nl.py`（AST 导出，源自 content*.py 字面量，绝不从 PDF 反提；无 hardcode，标题由参数传入）。基线试跑 vs issues 已发 `.text.md` **11/11 BYTE-IDENTICAL**；patched 导出同样 BYTE-IDENTICAL（门 15）。
- 修复（run1 → run2）：共 **8 处**，只动字号，零文字改动。run1 缺陷：栏头超宽 3 处（ru 除外，ru 栏头未超）、occlusion TEXTX 1 处（P7 B1 栏头 'SCHEIDBARE WERKWOORDEN' 与 'B2' 重叠 5.2×17.8px；ru 除外）、boxtitle/creambox 5 处（ru/zh-cn/zh-tw 为 0），ru 另有 spill 1 处（codes 行注 'внимательны' 框底溢出 BELOW +13.34px）。
  - `content12.py:49` 奶油框标题 DE WEEK IN CIJFERS　EN CIFRAS：tsize — → **tsize=22**（宽 415.0px，超框 10.2px；修后 396.9px，余量 5.9px）。
  - `content12.py:180` 奶油框标题 ZO ONTHOUD JE HET　EL TRUCO：tsize — → **tsize=22**（宽 412.8px，超框 8.0px；修后 394.8px，余量 8.0px）。
  - `content56.py:162` p.text VOOR OF TEGEN?　PROS Y CONTRAS：21 → **20**（宽 415.7px，超 15.1px；修后 395.9px，余量 2.7px）。
  - `content7.py:73` p.text PAS OP!　ERRORES FRECUENTES：23 → **22**（宽 410.7px，超 10.1px；修后 392.8px，余量 5.8px）。
  - `content7.py:84` p.text HET WOORD　PALABRA SEMANAL：23 → **21**（宽 432.1px，超 32.1px；修后 394.5px，余量 3.5px）。
  - `content12.py:176` 栏头 DRIE ACTIES VOOR DEZE WEEK：25 → **24**（宽 425.0px；修后 408.0px）。
  - `content34.py:21` 栏头 TWEEDEHANDS IS OOK CULTUUR：25 → **23**（宽 456.7px；修后 420.1px）。
  - `content7.py:32` 栏头 B1　SCHEIDBARE WERKWOORDEN：24 → **22**（宽 455.7px；修后 417.8px）。
- 门禁（run2，全套 16 门 + D18）：**ALL-GREEN**。run TOTAL 150 / head_check 0 defects / d5 census 拉丁 0、西里尔 0、CJK 内花括号 0 / render RC=0 / webpdf RC=0（网 PDF 1,019,584 B < 7 MB）/ occlusion 0 flags（selftest 6 类全触发）/ p8 extract 150/150 / p8 compare CLEAN（missing=[] extra=0，keydiff=[137, 138]，137/138 为读者语重定向真重 aim，已裁定，非缺陷) / freeze baseline 8/8 / freeze diff vs base 新增 CJK 字符 **0**（新增拉丁 strings 466，D5 run 拆分所致；对照是 base 修前生产版，不是 core）/ spill 0（1 OBSERVE）/ boxtitle 0 / edge 0 TOUCH 0 NEAR / creambox 0 defects（P8 232 → 232 行，距页脚线余量 36.9px）/ 文字层 print=web 字符多重集差 **0**（34,543 字符），text.md BYTE-IDENTICAL / census_quotes 0 defective / D18 刊头 gap **89.7px** > 0。
- 补充校验 G15b（carryover，诊断性，不计入 verdict）：共享 `verify_textmd.py` 对 nl 目标家族未标定（表按 pt 目标语格式标定），patched 与基线同态 FAIL（de 例：SVG-only 711 / MD-only 1119，基线 711 / 1121；ru、zh-cn 基线与 patched 残差完全相同）——D27 类已知工具口径差，非 D5 回归；内容不变的证据以门 15（AST 导出器 BYTE-IDENTICAL + print=web 差 0）为准。
- 最终 pin（builder 原件；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）：印 PDF `De-Lucerna-VOL2-nl-es.pdf` 6,941,183 B，SHA-256 `9976e67b8a809e58d1f1f4e799657dd0421881af849e2d46c9a424b79fc37d28`；网 PDF `2026-w45-nl-es.web.pdf` 1,019,584 B，SHA-256 `708b9f5fbd2e6b203aedfc23a649fd5a144c38fb66d55831cd48d27bd972112d`；text.md 39,823 B，SHA-256 `229b307b1b559f92f88f328058b2b48c0babab53f4522235d26474ae8edd2ad0`（与 issues 已发版 BYTE-IDENTICAL）。
- Builder scratch：`hidden_files/d5-redo/scratch-2026-w45-nl/patched/2026-w45-nl-es/`；门禁总表复本（D29）：`production/notes/2026-w45/g-nl/scratch-d5-rebuild-nl/logs/2026-w45-nl-es/GATES-SUMMARY.txt`。
