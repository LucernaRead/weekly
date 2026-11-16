# WEEKLY-KIT — Lucerna Japanese × French (JA×FR), VOL.3, W46, 9–15 Nov 2026

Slug: `2026-w46-ja-fr`. Target language: Japanese (articles frozen
byte-identical from the W46 JA core). Reader language: français (the
entire explanation layer). Source: the pristine W46 core build
`hidden_files/weekly-report-w46-ja-build/` (never modified); this
edition was produced by `transform.py   # from the pristine W46 core build` in
`hidden_files/weekly-report-w46-ja-fr-build/` (exact-literal
replacements only; re-runnable).

## §1 Pairing badge and footers

- Masthead geometry (task + tools/README lesson 20): wordmark baseline
  y=262 (core position, kept), subtitle y=316, badge inserted at
  (975,356) 19pt BRICK `#a4553a`, strapline y=390, double rules 406/413,
  dark band y=424.
- Badge: `TEXTES EN JAPONAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`.
- Footer every page: `Lucerna · HEBDOMADAIRE JAPONAIS VOL.3 · TEXTE EN JAPONAIS · EXPLICATIONS EN FRANÇAIS`; page line `Page N sur 8`.
- Top strip middle segment: `Chaque semaine` (replacing the core's Chinese).
- Gloss prefix: `Note — `. P8 separators: `— Page N —`.
- Registry type names: texte à trous / choix multiple / association / construction de phrases / vrai/faux / traduction / rédaction; instructions: Compléter, etc..
- P1 dark-band right lines (français, short form): `Dimanche, c'est Shichi-Go-San` /
  `La saison des feuilles va vers le sud · Voir page 6`.

## §2 What changed vs the core

Only the explanation layer: glosses, notes, answer notes, furniture
halves, band subtitles, the P2 season-word glosses, the P7 error-clinic
notes, frame breakdown, readers'-corner disclosure (ONE français
disclosure replacing both the Japanese and Chinese lines, per the W45
coordinator ruling: "Exemple de la rédaction, pas une vraie lettre. À la date limite, aucune lettre ni composition n'était arrivée ; les deux paraîtront dans le VOL.4. Envoyez-nous votre lettre en japonais — les lettres choisies seront publiées dans le VOL.4 !"), phrase
translations + page tags, teaser head, and the P8 E-zone re-aiming:
items 137–138 keep their Japanese stems with français keys;
items 139–140 have français stems with the Japanese keys byte-identical
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
  P7 teaser ends y=2526.6 (< 2540); P8 keys-flow last baseline
  y=2535.01 (< 2540).
- Occlusion audit: 0 flags (`hidden_files/w46/ja-fr-occlusion.json`;
  selftest OK).
- P8 compare: CLEAN, 150/150 noted, keydiff=[137, 138] — exactly the re-aimed E-zone keys (expected;
  see §2). (`hidden_files/w46/ja-fr-p8compare.json`).
- Freeze diff --strict-cjk: 0 added CJK characters
  (`hidden_files/w46/ja-fr-freeze.json`).
- Web PDF: `Lucerna-VOL3-FR-web.pdf`, 2,344,132 bytes (< 7 MB),
  47,669 pdftotext bytes, identical to the print PDF text. Print PDF
  kept: `Lucerna-VOL3-FR.pdf` (28,745,818 bytes).
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
cd hidden_files/weekly-report-w46-ja-fr-build
tools/venv/bin/python transform.py   # from the pristine W46 core build
tools/venv/bin/python run.py         # one process, shared registry
tools/venv/bin/python render.py      # cards + print PDF
tools/venv/bin/python webpdf.py <svg dir> <web pdf>   # from tools/
```

## §6 Fix history

Round history: round 1 showed a LINEX flag (P1 word-of-week gloss
  wrapped across the rule below); fixed by shortening the gloss to
  "千歳飴 = bonbon de Shichi-Go-San." The disclosure was trimmed to 6
  wrap lines (P7 teaser fit), the frame title shortened to "Structure
  hebdo", and the F matching instruction shortened to "Associer mots et
  sens". The 12.9pt / lh 1.13 keys-font patch (map EXTRA) was applied
  because French notes run long. Re-rendered and re-gated clean.

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
  rest verbatim. Before tail: `150 exercices pour apprendre le japonais à travers de vraies nouvelles japonaises.` After tail:
  `150 exercices construits à partir des sujets de cette semaine.` (Full before/after in
  `hidden_files/w46/ja-fix/abstracts-before-after.txt`.)
- Re-gate (final artifacts): freeze diff exit 0, 0 added CJK; p8 compare CLEAN
  150/150, keydiff [137, 138]; occlusion 0 flags; kinsoku scan
  (proofreader's definitions) start 0 / end 0 / orphan 0; counts 150
  (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38), stems
  and keys 1–150 complete, P6 bars 1020/780/720/480 with all labels
  + practice-data label, P7 phrases 2× verbatim, keys-flow end-y
  2535.0; web PDF 2,344,131 bytes (< 7 MB), 47,669 pdftotext bytes,
  byte-identical to the print PDF (28,745,814 bytes); text.md 47,029 bytes.
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
  every stem piece. Source: regenerated by this edition's `transform.py` from the fixed core (no transform-table edit); this build's `content34.py:95` carries the new key with the unchanged FR note.
  Before (P8 key 42): `42. 熊手を買います。 — Acheter un kumade à Tori-no-ichi`
  After (P8 key 42): `42. 酉の市で熊手を買います。 — Acheter un kumade à Tori-no-ichi`
  The reader-language note is UNCHANGED. The P3 stem is unchanged.
  No SVG/PDF was hand-edited; no other string was reworded.
  Fit: single line, width 405.8 of 434 (slack 28.2), y unchanged 1368.877.
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
  label, P7 phrases 2× verbatim, keys-flow end-y 2535.0;
  web PDF 2,344,133 bytes (< 7 MB), 47,681 pdftotext bytes, byte-identical to the print PDF (28,745,818 bytes); text.md 47,041 bytes. P8 card visually checked at full frame: key 42
  correct, no overflow, overlap, or tofu.

## 补记：D5 字体重建（2026-11-15）

D5 字体重建：日语目标版的拉丁/西里尔字母由 Noto Sans/Serif CJK JP 改为 Newsreader（拉丁）/ Noto Sans（西里尔），弯引号归 Newsreader（fix2）；其余内容、字号、版式逐字节复现已发版。重建在 `hidden_files/d5-redo/scratch-2026-w46-ja/` 内完成，只改 `patched/`，由 closer 同步进 production。

### D5 交付物 pin（run2 终轮实测）

- 印 PDF：`Lucerna-VOL3-FR.pdf 24211949B sha=ac61b957c7847f0a`
- 网 PDF：`Lucerna-VOL3-FR-web.pdf 2165544B sha=ed14b8745d5cebd4`
- text.md：`46910B sha=cfb0950754e092900bcc0d411410de48c262c301143950541e66390f00395712`
- text.md 全 SHA-256：`cfb0950754e092900bcc0d411410de48c262c301143950541e66390f00395712`
- 印 PDF 全 SHA-256：`ac61b957c7847f0a21d7ec91259242a57cb00fd241a011f7044576f2f64916ec`
- 网 PDF 全 SHA-256：`ed14b8745d5cebd43cec613f7f576179f374d8ca35df5bd9858def4f63f1db98`

### D5 重建节

- 装机：`bin/install.py`（模板 `tools/mechanism-w47/svglib-ja-d5.py`，与 W47 production `core-ja/svglib.py` 逐字节相同；`_D5_READER = "latin"`，`svglib.py:122`；fix2 提及 6 处，`_QUOTE_CLS` 4 处，kinsoku `NO_START` 在位；`test_d5_routing.py` FAILURES: 0）。
- 修前普查（基线）：Latin in CJK 400、Cyrillic in CJK 0、curly_total 0、curly_in_CJK 0；修后普查 0（G3 PASS）。
- 逐条修复（只降字号，不改文案；探针余量见家族报告 §1–§6）：
  - `content12.py:86` 18.5→18.0：F1 P1 credit line boxtitle +6.5px (W45 F1 precedent)
  - `content7.py:73` 23→22：F3 P7 box title boxtitle +9.5px; probe margin +8.3px at 22 (22.5 still -0.6)
- run2 门禁：
  - G1: PASS rc=0 TOTAL=150 FLOW=0 HEAD=0
  - G2: PASS rc=0 defects=0
  - G3: PASS rc=0 latin=0 cyr=0 curly_cjk=0 curly_total=0 noto_sans=0
  - G4: PASS Lucerna-VOL3-FR.pdf 24211949B sha=ac61b957c7847f0a
  - G5: PASS Lucerna-VOL3-FR-web.pdf 2165544B sha=ed14b8745d5cebd4
  - G6: PASS rc=0 flags=[]
  - G7: PASS rc=0 noted=150/150
  - G8: PASS rc=0 CLEAN keydiff=[137, 138]
  - G9: PASS rc=0 8/8
  - G10: PASS rc=0 cjk_added={} latin_added=210 keys=['cjk_added_total', 'core_svg', 'edition_svg', 'latin_added_total', 'latin_added_unexpected_total', 'pages', 'runtime']
  - G11: PASS rc=1 SPILL=1 OBSERVE=92 vs baseline 1: same set
  - G12: PASS rc=0 DEFECT=0
  - G13: PASS rc=0 EDGE_SCAN 2026-w46-ja-fr: 8 pages, 0 TOUCH, 0 NEAR
  - G14: PASS rc=0 defects=0 observes=0 p8rows=842->860 slack_footer=45.9->45.9 ratio_med=1.011 bold_med=1.04 reg_med=0.994
  - G16: PASS rc=0 defective=0
  - D18: PASS gap=276.3px
  - D37: PASS y612 over=-1149.5pt end=289.9 | sub over=-33.2pt end=1406.3
  - G15b：仅记录（D27，共享校验器对 ja 格式未校准）
  - ALL-GREEN=True (G15b excluded per D27)
