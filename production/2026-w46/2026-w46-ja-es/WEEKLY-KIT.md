# WEEKLY-KIT — Lucerna Japanese × Spanish (JA×ES), VOL.3, W46, 9–15 Nov 2026

Slug: `2026-w46-ja-es`. Target language: Japanese (articles frozen
byte-identical from the W46 JA core). Reader language: español (the
entire explanation layer). Source: the pristine W46 core build
`hidden_files/weekly-report-w46-ja-build/` (never modified); this
edition was produced by `transform.py   # from the pristine W46 core build` in
`hidden_files/weekly-report-w46-ja-es-build/` (exact-literal
replacements only; re-runnable).

## §1 Pairing badge and footers

- Masthead geometry (task + tools/README lesson 20): wordmark baseline
  y=262 (core position, kept), subtitle y=316, badge inserted at
  (975,356) 19pt BRICK `#a4553a`, strapline y=390, double rules 406/413,
  dark band y=424.
- Badge: `TEXTOS EN JAPONÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`.
- Footer every page: `Lucerna · SEMANARIO JAPONÉS VOL.3 · TEXTO EN JAPONÉS · EXPLICACIONES EN ESPAÑOL`; page line `Página N de 8`.
- Top strip middle segment: `Cada semana` (replacing the core's Chinese).
- Gloss prefix: `Nota — `. P8 separators: `— PÁGINA N —`.
- Registry type names: cloze / opción múltiple / relacionar / construcción de frases / verdadero/falso / traducción / redacción; instructions: Completa, etc..
- P1 dark-band right lines (español, short form): `El domingo es Shichi-Go-San` /
  `La temporada de hojas va hacia el sur · Ver página 6`.

## §2 What changed vs the core

Only the explanation layer: glosses, notes, answer notes, furniture
halves, band subtitles, the P2 season-word glosses, the P7 error-clinic
notes, frame breakdown, readers'-corner disclosure (ONE español
disclosure replacing both the Japanese and Chinese lines, per the W45
coordinator ruling: "Ejemplo de la redacción, no una carta real. Hasta la fecha límite no llegaron cartas ni composiciones; ambas aparecerán en el VOL.4. ¡Enviadnos vuestra carta en japonés: las elegidas se publicarán en el VOL.4!"), phrase
translations + page tags, teaser head, and the P8 E-zone re-aiming:
items 137–138 keep their Japanese stems with español keys;
items 139–140 have español stems with the Japanese keys byte-identical
to the core. All Japanese article/stem/option/letter/figure strings are
frozen; all facts and sources are the core's (§3 of the core KIT).

## §3 Content and counts

Same 8 pages and 150 exercises as the core (A2 46 · B1 75 · B2 29;
by page 10/18/18/18/18/18/12/38). P8 model text 154 characters.
Images: same 3 reused PD/CC0 images as the core (maple P1, Hiroshige
III print P3, stadium P4); credits in the core build's
`assets/CREDITS.md`.

## §4 Gates (recorded in hidden_files/w46/ja-gates.log)

- Builder self-check: no FLOW OVERFLOW / HEAD TOO WIDE warnings.
  P7 teaser ends y=2524.12 (< 2540); P8 keys-flow last baseline
  y=2536.19 (< 2540).
- Occlusion audit: 0 flags (`hidden_files/w46/ja-es-occlusion.json`;
  selftest OK).
- P8 compare: CLEAN, 150/150 noted, keydiff=[137, 138] — exactly the re-aimed E-zone keys (expected;
  see §2). (`hidden_files/w46/ja-es-p8compare.json`).
- Freeze diff --strict-cjk: 0 added CJK characters
  (`hidden_files/w46/ja-es-freeze.json`).
- Web PDF: `Lucerna-VOL3-ES-web.pdf`, 2,346,159 bytes (< 7 MB),
  47,774 pdftotext bytes, identical to the print PDF text. Print PDF
  kept: `Lucerna-VOL3-ES.pdf` (28,725,840 bytes).
- Visual pass: P1 card checked (badge geometry, gloss, numbers box);
  P7/P8 cards checked for this edition's risk areas (disclosure,
  keys fit). Kinsoku: the Japanese body text is the core's (0 line-start
  hits).
- `.text.md` exported from the builder SVG manuscript with
  `hidden_files/w46/make_textmd.py` (never from PDF).
- Proofread status: builder-complete; finalisation requires the
  independent proofread per SOP §8.4. This KIT does not declare the
  edition final. Nothing posted to Discord, nothing sent to chat,
  weekly repo untouched.

## §5 Reproduction

```
cd hidden_files/weekly-report-w46-ja-es-build
tools/venv/bin/python transform.py   # from the pristine W46 core build
tools/venv/bin/python run.py         # one process, shared registry
tools/venv/bin/python render.py      # cards + print PDF
tools/venv/bin/python webpdf.py <svg dir> <web pdf>   # from tools/
```

## §6 Fix history

Round history: the disclosure was trimmed twice (final ~200 chars,
  6 wrap lines) and error-clinic note 4 shortened to "Usa 「で」 para el
  lugar de mirar." (P7 teaser fit, col3 ends 1750.12). The frame title
  was shortened to "Estructura semanal", the F instruction to "Une
  palabras y sentidos", and two golden-phrase translations were
  shortened to month-less forms faithful to the Japanese originals. A
  BOXTITLE flag (P4 box title ink 991.5 > border 961.0) was fixed by
  shortening "Historial de la serie" to "Serie de Japón"; a LINEX flag
  (word-of-week gloss wrapped) was fixed by shortening the gloss to
  "千歳飴 = caramelo de Shichi-Go-San." The 12.9pt / lh 1.13 keys-font
  patch (map EXTRA) was applied. Re-rendered and re-gated clean.

Fix record — Round 1 proofread defects (fix worker, 2026-11-02/03).
Round 1 verdict: FAIL on inherited D-CORE-01 + D-CORE-02. Both fixed
at the source in the core build / this edition's ABSTRACT.txt; this
edition was fully re-rendered through the pipeline in §5 and re-gated
on the final artifacts (gate JSONs/logs under
`hidden_files/w46/ja-fix/`). Round 2 independent proofread still
required.

- D-CORE-01: core `svglib.py` `wrap()` gained a NO_END kinsoku block
  (opening brackets `（「『〔【《〈([` never end a line); md5
  d73e23b365676c3618d7e060b835eb4d →
  74177544422fe677639d769cd80499fb, and `CANON_SVGLIB_MD5` in this
  edition's `transform.py` was updated to the new value. The §5
  "pristine core build" wording now refers to the pre-fix state; the
  current build carries the NO_END fix. P1 item 8 and P3 item 32 now
  keep `（月）` / `（土）` intact on one line (see core KIT §11 for the
  line-split quotes); no other text moved.
- D-CORE-02: `ABSTRACT.txt` closing rewritten to practice framing,
  rest verbatim. Before tail: `150 ejercicios para aprender japonés con noticias japonesas reales.` After tail:
  `150 ejercicios construidos a partir de los temas de esta semana.` (Full before/after in
  `hidden_files/w46/ja-fix/abstracts-before-after.txt`.)
- Re-gate (final artifacts): freeze diff exit 0, 0 added CJK; p8 compare CLEAN
  150/150, keydiff [137, 138]; occlusion 0 flags; kinsoku scan
  (proofreader's definitions) start 0 / end 0 / orphan 0; counts 150
  (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38), stems
  and keys 1–150 complete, P6 bars 1020/780/720/480 with all labels
  + practice-data label, P7 phrases 2× verbatim, keys-flow end-y
  2536.2; web PDF 2,346,157 bytes (< 7 MB), 47,774 pdftotext bytes,
  byte-identical to the print PDF (28,725,836 bytes); text.md 47,116 bytes.
  P1 and P3 cards visually checked at full frame: both rewraps
  correct, no overflow/overlap.

Fix record — Round 3 proofread defect D-KEY-42 (fix worker, 2026-11-03).
Round 2 verdict: FAIL on D-KEY-42 only (all Round 1 defects confirmed
fixed). Fix applied at the source in the core build and propagated by
regeneration; this edition was fully re-rendered through the pipeline
in §5 and re-gated on the final artifacts (gate JSONs/logs under
`hidden_files/w46/ja-fix-round3/`). Round 3 independent proofread
still required.

- D-KEY-42 (P8 key 42 omits a stem piece, BLOCKING, all 11 editions):
  P3 stem item 42 is `酉の市で / 熊手を / 買います → ___` (造句).
  The printed P8 key omitted the location piece `酉の市で`, while
  all 7 sibling 造句 keys (39, 40, 41, 133, 134, 135, 136) include
  every stem piece. Source: regenerated by this edition's `transform.py` from the fixed core (no transform-table edit); this build's `content34.py:95` carries the new key with the unchanged ES note.
  Before (P8 key 42): `42. 熊手を買います。 — Comprar un kumade en Tori-no-ichi`
  After (P8 key 42): `42. 酉の市で熊手を買います。 — Comprar un kumade en Tori-no-ichi`
  The reader-language note is UNCHANGED. The P3 stem is unchanged.
  No SVG/PDF was hand-edited; no other string was reworded.
  Fit: single line, width 421.2 of 434 (slack 12.8), y unchanged 1396.854.
- Change isolation: SVG text-multiset diff vs the pre-fix snapshot
  shows exactly one changed text in this edition (the key-42 line
  );
  hash check over the 132 edition files shows only the P8 SVG, both
  PDFs, and the .text.md changed in this edition (P1–P7 SVGs and
  ABSTRACT.txt byte-identical). Round 1 fixes survive (kinsoku 0/0/0,
  abstracts unchanged, zh-tw conversions intact where applicable).
- Re-gate (final artifacts): freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2); occlusion audit 0 flags
  (synthetic selftest passed); kinsoku scan start 0 / end 0 / orphan 0;
  counts 150 (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38),
  stems and keys 1–150 complete, sibling 造句 keys unchanged and
  complete, P6 bars 480/720/780/1020 with all labels + practice-data
  label, P7 phrases 2× verbatim, keys-flow end-y 2536.2;
  web PDF 2,346,165 bytes (< 7 MB), 47,786 pdftotext bytes, byte-identical to the print PDF (28,725,845 bytes); text.md 47,128 bytes. P8 card visually checked at full frame: key 42
  correct, no overflow, overlap, or tofu.

## 补记：D5 字体重建（2026-11-15）

D5 字体重建：日语目标版的拉丁/西里尔字母由 Noto Sans/Serif CJK JP 改为 Newsreader（拉丁）/ Noto Sans（西里尔），弯引号归 Newsreader（fix2）；其余内容、字号、版式逐字节复现已发版。重建在 `hidden_files/d5-redo/scratch-2026-w46-ja/` 内完成，只改 `patched/`，由 closer 同步进 production。

### D5 交付物 pin（run2 终轮实测）

- 印 PDF：`Lucerna-VOL3-ES.pdf 24213421B sha=6e90549cfa069624`
- 网 PDF：`Lucerna-VOL3-ES-web.pdf 2166705B sha=fefeb243aa713265`
- text.md：`46996B sha=7bd9da146865e6b3e6be30d724eb4a9a626e560753fe9b84307c663219778a68`
- text.md 全 SHA-256：`7bd9da146865e6b3e6be30d724eb4a9a626e560753fe9b84307c663219778a68`
- 印 PDF 全 SHA-256：`6e90549cfa069624756400e9f3eb039b9fa28b8fb618e885e1946ab2e7e4206c`
- 网 PDF 全 SHA-256：`fefeb243aa71326520eb2e1e78070e858563945f1eb94e0fd00de6a866e24b5a`

### D5 重建节

- 装机：`bin/install.py`（模板 `tools/mechanism-w47/svglib-ja-d5.py`，与 W47 production `core-ja/svglib.py` 逐字节相同；`_D5_READER = "latin"`，`svglib.py:122`；fix2 提及 6 处，`_QUOTE_CLS` 4 处，kinsoku `NO_START` 在位；`test_d5_routing.py` FAILURES: 0）。
- 修前普查（基线）：Latin in CJK 400、Cyrillic in CJK 0、curly_total 0、curly_in_CJK 0；修后普查 0（G3 PASS）。
- 逐条修复（只降字号，不改文案；探针余量见家族报告 §1–§6）：
  - `content12.py:86` 18.5→18.0：F1 P1 credit line boxtitle +6.5px (W45 F1 precedent)
  - `content7.py:85` 23→22.5：F2 P7 box title boxtitle +2.8px; probe margin +6.0px at 22.5
- run2 门禁：
  - G1: PASS rc=0 TOTAL=150 FLOW=0 HEAD=0
  - G2: PASS rc=0 defects=0
  - G3: PASS rc=0 latin=0 cyr=0 curly_cjk=0 curly_total=0 noto_sans=0
  - G4: PASS Lucerna-VOL3-ES.pdf 24213421B sha=6e90549cfa069624
  - G5: PASS Lucerna-VOL3-ES-web.pdf 2166705B sha=fefeb243aa713265
  - G6: PASS rc=0 flags=[]
  - G7: PASS rc=0 noted=150/150
  - G8: PASS rc=0 CLEAN keydiff=[137, 138]
  - G9: PASS rc=0 8/8
  - G10: PASS rc=0 cjk_added={} latin_added=207 keys=['cjk_added_total', 'core_svg', 'edition_svg', 'latin_added_total', 'latin_added_unexpected_total', 'pages', 'runtime']
  - G11: PASS rc=1 SPILL=1 OBSERVE=89 vs baseline 1: same set
  - G12: PASS rc=0 DEFECT=0
  - G13: PASS rc=0 EDGE_SCAN 2026-w46-ja-es: 8 pages, 0 TOUCH, 0 NEAR
  - G14: PASS rc=0 defects=0 observes=0 p8rows=848->867 slack_footer=41.1->41.1 ratio_med=1.012 bold_med=1.04 reg_med=0.994
  - G16: PASS rc=0 defective=0
  - D18: PASS gap=291.3px
  - D37: PASS y612 over=-1076.4pt end=363.1 | sub over=-8.0pt end=1431.5
  - G15b：仅记录（D27，共享校验器对 ja 格式未校准）
  - ALL-GREEN=True (G15b excluded per D27)
