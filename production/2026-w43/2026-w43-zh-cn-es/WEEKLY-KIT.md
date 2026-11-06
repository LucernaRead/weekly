# WEEKLY-KIT — Lucerna VOL.1 · 简体中文正文 + 西班牙语讲解 (zh-CN × ES)

**Edition:** Simplified Chinese target text (frozen VOL.1 core) · explanations in Spanish
for Spanish-speaking readers · W43 (2026-10-19 → 2026-10-25) · 8 pages, 1950×2700, 4 columns.
**Masthead:** Lucerna (no article — Chinese convention, exactly as the core ships).
**Pairing badge (P1):** «TEXTOS EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN
PARA LOS LECTORES HISPANOHABLANTES» (measured 1166px at 19.5px bold sans — fits one line).
**Footers (all pages):** «Lucerna · SEMANARIO CHINO SIMPLIFICADO VOL.1 · TEXTO EN CHINO
SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL» (1106px at 20px) / «Página N de 8».
**Build:** `hidden_files/weekly-report-zhcn-es-build/` (copy of the core build; only the
explanation layer, the pairing furniture and the P8 key-line format were changed).
**Deliverables:** `files/weekly-report-zh-cn-es/` — svg/ ×8, cards/ ×8, print + web PDFs, this KIT.

---

## 1. Baseline proof (frozen core reproduction)

The copied core build was run **unmodified** before any edit. Its 8 output SVGs matched the
shipped core SVGs (`files/weekly-report-zhcn-vol1/svg/`) byte-for-byte — sha256 verified 8/8:

| Page | Core SVG sha256 (prefix) |
|---|---|
| p1-touiban | d75ee1bc4a7fb5eb |
| p2-shenghuo | 0addf9e73c6d43c6 |
| p3-wenhua | c1fc3edac48f94c0 |
| p4-tiyu | 84233560911efd20 |
| p5-qingnian | db594dd2b45da451 |
| p6-shendu | 2987188a300ac125 |
| p7-ciyu | 4f598f285fdc878d6 |
| p8-ceyan | 8ac2807b67737cfa |

Registry at baseline: 150 exercises, A2 56 · B1 65 · B2 29 — identical to the core.

## 2. Totals (final, = core)

- **150 exercises** — A2 56 · B1 65 · B2 29; per page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- Types (registry labels localized): Completar 68 · Opción múltiple 50 · Relacionar 20 ·
  Opción en contexto 11 · Escritura 1.
- Writing model (P8 §F): 148 characters, unchanged Chinese text; arithmetic re-verified
  (260 + 60 + 40 = 360; 360 − 50 = 310; 310 − 30 = 280 尾款）.
- Levels ramp A2 (P1–P2) → A2→B1 (P3) → B1 (P4–P5) → B2 (P6) → mixed (P7) → mixed (P8), as core.

## 3. Key-diff registry (complete)

**Derivation:** this core contains **no translation-type exercises** — its registry types are
sentence completion / multiple choice / matching / cloze-MCQ / writing only, and every answer
key is a Chinese word, a numeral, or a letter. No key is expressed in the reader's language,
so no key can legitimately re-aim at Spanish. The single exception is the writing item's
apparatus line, whose core key is a Chinese apparatus string rather than an answer.

| # | Core key | ES key | Why |
|---|---|---|---|
| 150 | （开放题，范文如下） | (pregunta abierta — modelo a continuación) | Writing-item apparatus line, not an answer; its note → «Pregunta abierta — el modelo está en la sección F de esta página, 148 caracteres» |

**Verification:** both registries were dumped from source and diffed programmatically —
**149/150 keys byte-identical**, page and level of every item identical, all 150 notes
translated (0 notes identical to the core's English). A numeric-fidelity pass over all 150
notes found every figure preserved; the only differences are Spanish number formats
(57.5 → 57,5 · 25.8 % → 25,8 % · 10,100 → 10.100) and ordinals written as words (10th → décima).

**P8 key-line format** (this edition's rule): `n. key (note)` — space before the parenthesis,
half-width parentheses only; writing item `150. ✓ (note)`. Because the typesetting helper
converts a parenthesis pair to full width when the enclosed text contains Chinese characters,
all notes are kept Chinese-free (Chinese terms appear as pinyin) — the same solution as the
shipped zh-CN×FR edition. Verified on the final SVG: 150 key lines, **0 full-width
parentheses, 0 Chinese characters inside note parentheses**.

## 4. Furniture inventory (every replaced furniture string)

- P1 badge → §header above (whole-string replacement).
- P1 strap «简体中文版 · VOL.1 · …» → «SEMANARIO CHINO SIMPLIFICADO · VOL.1 · 双11 · 大闸蟹 · 霜降»
  (Chinese topic words kept; measured 1266px serif bold 40px — fits).
- Footer left/right on all 8 pages → §header above.
- Gloss-box prefix «Notes｜» → «Nota — » (bslib4 `gloss()`).
- Bilingual section heads keep their Chinese half; the English half is now Spanish
  (e.g. 头条 · Titular · 本周热搜 · Lo más buscado · 数字看本周 · La semana en cifras ·
  易错诊所 · Clínica de errores). Bylines → «Redacción Lucerna · Nivel de lectura …».
- Exercise instructions: «Completa» / «Relaciona las palabras» (202px — fits the match
  header slot) / «Escritura». Section glosslines all in Spanish.
- P7 phrase page tags «p. N» → «Página N». P8 page separators «— Página N —».
- Image credit labels «Photo:» → «Foto:» (artist names and licenses unchanged, §7).
- Registry type labels localized (§2); the writing-type check in content8 updated to match.

**CJK accounting (character multiset, final SVGs vs core): ZERO Chinese characters added on
any page.** Removals, all inside explanation layer / furniture: P1 −36 (badge 10 + footer 20 +
strap 5 + gloss ｜ 1) · P2–P6 −22 each (footer 20 + gloss ｜ ×2) · P7 −20 (footer) · P8 −169
(footer 20 + writing key 8 + Chinese words embedded in the core's English answer notes,
replaced by pinyin per §3). Target-layer Chinese text is byte-identical throughout.

## 5. Facts, dates, arithmetic (re-verified for this edition)

- Calendar (checked against the real 2026 calendar): 重阳 Sun Oct 18 (retrospective) ·
  issue week Mon Oct 19 – Sun Oct 25 · fashion show Mon Oct 19 07:30 Beijing · Tmall tail
  payments **Tue Oct 20, 20:00** · gymnastics men's final early Oct 21, women's final
  Oct 22 01:30 Beijing · 霜降 **Fri Oct 23** · S16 Swiss round first match Sat Oct 24 01:00
  Beijing · S16 final Nov 14 New York = Sun Nov 15 03:00 Beijing · 立冬 Nov 7.
- Hairy-crab figures (P6, target layer frozen): Xinfadi ~3两 females ¥77.5/斤 (Mid-Autumn)
  → ¥57.5/斤 on Oct 6; drop = 20 ÷ 77.5 = **25.8 %**, printed in the text as 约25.8% and
  glossed in the notes as the computed figure — never the online «暴跌40%» claim.
- Gymnastics chart: 251.928 − 249.193 = 2.735 ✓, bars drawn from 0 in exact proportion.
- Practice example (P2): 260 + 60 = 320; 320 − 50 = 270; 270 − 30 = 240 ✓.
- P7 phrases of the week: all 8 verified verbatim contiguous excerpts of this issue's own
  articles, each occurring exactly 2× in the full-issue text, page tags (Página 1, 1, 2, 3,
  4, 4, 5, 6) all correct.
- Zero politics, per the China-target rule (identical to core).

## 6. Geometric occlusion audit (mandatory gate — builder's run)

Method: SVG paint-order parse; glyph boxes from PIL metrics with the build's own fonts
(Noto Serif/Sans CJK, SC index); ink band = baseline −0.88em … +0.30em; line boxes expanded
by half the stroke width. Classes: ≥30% coverage by a later opaque rect/image · later line
crossing an ink band · footer-band intrusion (y > 2580) · page-edge spill · text crossing
its own box's border. **The script was validated on a synthetic positive control first —
all five classes fired and a clean line stayed silent.**

Result on the final SVGs: **1 raw flag, adjudicated a non-defect; 0 unresolved.**

- P2, «Recuerda la frase: …» vs the gold rule above the exercises: the audit's modelled ink
  band (baseline +0.30em) overlaps the rule rows, but pixel measurement of the rendered card
  shows the sentence's actual ink ends at row **1800** and the rule occupies rows **1803–1804**
  (4 dark pixels = anti-aliasing noise). The identical flag fires on the shipped core's own
  P2 (same geometry, same pixel rows) — inherited, frozen, not a defect.

Defects found and fixed during the build (wording only, geometry never touched):

1. Section head «B · 词语填空 · Completa con palabras» measured 470.8px > 434px column
   (HEAD TOO WIDE on P2–P6) → shortened to «Completa huecos» (401.3px).
2. «C · 数字与计算 · Números y cálculo» 439.7px > 434px (P6) → «Cálculo» (305.8px).
3. P8 keys FLOW OVERFLOW: the parenthetical key format plus longer Spanish notes pushed the
   key flow past y=2540 (last column clamped). 22 notes were tightened so each wraps in the
   same number of lines as its core counterpart, and 55 notes were rewritten Chinese-free
   (§3). Final key flow ends at col 4, y=2471 < 2540; final build log: zero FLOW OVERFLOW,
   zero HEAD TOO WIDE.

## 7. Images (identical to core — payloads byte-identical per page, verified by hash)

All Public Domain / CC0, verified against the Wikimedia Commons API (Artist field) in the
core's production; credit labels on the pages match this table exactly.

| File | Page | Author (Commons API) | License |
|---|---|---|---|
| locker.jpg | P1 | Map hobby | CC0 |
| valley.jpg | P2 | Paul Gilmore | CC0 |
| chrysanthemum.jpg | P3 | PushpaKhan | CC0 |
| frost.jpg | P3 | Gerda Arendt | CC0 |
| basketball.jpg | P4 | noahsilliman | CC0 |
| gymnastics1896.jpg | P4 | unknown author, 1896 | Public domain |
| lanparty.jpg | P5 | Syced | CC0 |
| crab.jpg | P6 | Fumikas Sagisavas | CC0 |
| minicrabs.jpg | P6 | Fumikas Sagisavas | CC0 |

Full table in the core build's `assets/CREDITS.md` (copied with this build's assets).

## 8. PDFs (final render)

| File | Bytes | sha256 |
|---|---|---|
| Lucerna-VOL1-ES.pdf (print) | 68,841,777 | 9c7fe77961bf8c66cf16d816ee29ce3b78dc20c8086ece7f5fd7ca9e859bbc71 |
| Lucerna-VOL1-ES-web.pdf (web) | 3,269,256 | 7063569373e2a09aae1064a504ea2e5598a43e24f2fe05ceaee26208091ecfa6 |

Web PDF 3.27 MB < 10 MB ✓ (JPEG pages q85 @1400px, same recipe as the core).

## 9. Reproduction

```bash
cd hidden_files/weekly-report-zhcn-es-build
/tmp/wp-venv/bin/python run.py      # writes svg/ into files/weekly-report-zh-cn-es/svg/
/tmp/wp-venv/bin/python render.py   # cards/ PNG + print PDF + web PDF
```

## 10. Proofread record

- **Builder's full pass (this build): DONE.** All 8 pages read end-to-end in the final SVG
  text and on the rendered cards (P1/P8 inspected as images; all pages read as text);
  all 150 keys re-derived by registry diff against the frozen core (§3); all 150 notes
  read in Spanish and checked for numeric fidelity (§3); every weekday/date claim checked
  against the 2026 calendar (§5); chart bars and all arithmetic recomputed (§5); P7 phrases
  verified programmatically (§5); English-residue scan over all rendered text nodes: **0**;
  banned intermediary-layer term scan over paper, this KIT and the build code: **0**;
  geometric audit per §6. Problems found were fixed and the edition re-rendered; the final
  pass over the shipped artifacts found zero problems.
- **Independent proofread: PASS — completed 2026-10-21 (America/Toronto), after fixes
  below.** Fresh independent pass over the frozen core
  (`files/weekly-report-zhcn-vol1/`) and this edition; the proofreader did not build the
  edition. Baseline gate: an unmodified core build reproduces the shipped core SVGs 8/8
  byte-identical, and the ES build reproduces the shipped ES SVGs 8/8 byte-identical, so
  every comparison below is against the true artifacts. Gate results:
  1. **Freeze vs core — PASS.** All 150 exercise stems (body + options, AST-extracted in
     call order) byte-identical core vs ES. CJK character multiset per page: ZERO added on
     all 8 pages; removals only the enumerated pairing furniture (P1 −35 ideographs +1 ｜;
     P2–P6 −20 +2 ｜ each; P7 −20; P8 −162 = footer + the Chinese writing key + note-embedded
     words replaced by pinyin). No Simplified target-text change outside the registry.
  2. **Spanish completeness — PASS.** Every explanation element is Spanish. Residual-English
     scan over all SVG text and raw bytes: the only English in the edition is the frozen
     proper-noun source name «(The Beijing News)» in the P4 chart source line, identical in
     the core. All 150 notes are Spanish, none empty, ZERO CJK in notes; every Chinese word
     cited inside a note was converted to pinyin and each conversion was verified accurate
     and the note still semantically correct (dìngjīn, wěikuǎn, mǎnjiǎn, shuāngjiàng,
     biàn chā zhūyú shǎo yì rén, bǔdōng bùrú bǔ shuāngjiàng, etc.). Numeric localization
     verified (57,5 / 25,8 % / 10.100; «décima»).
  3. **Keys — PASS.** All 150 keys independently re-derived from the Chinese text and
     article facts: all correct. Key diff vs core = EXACTLY ONE item, #150 (the writing
     apparatus line); 149/150 byte-identical. Crab arithmetic (77.5−57.5)/77.5 = 25.8% ✓;
     gymnastics 251.928−249.193 = 2.735 ✓ (ES notes mirror the scores' printed notation).
  4. **Printed-note set equality — PASS.** The core build's print rule prints every
     registry entry (no filter in either build's content8). Sets extracted from the printed
     P8 SVGs: core 150/150, ES 150/150 — EQUAL by number, numbering continuous 1–150.
  5. **Totals — PASS.** 150 exercises (A2 56 · B1 65 · B2 29; per page 10/18/18/18/18/18/12/38;
     types Completar 68 · Opción múltiple 50 · Relacionar 20 · Opción en contexto 11 ·
     Escritura 1), re-added from the registry.
  6. **P7 phrases — PASS.** All 8 phrases are verbatim contiguous excerpts, each occurring
     exactly 2× in the full-issue text (once on its tagged page, once on P7); tags
     (Página 1, 1, 2, 3, 4, 4, 5, 6) all correct; Spanish glosses correct.
  7. **Calendar / politics — PASS.** Verified against the real 2026 calendar:
     重阳 Sun 2026-10-18 (retrospective) ✓; fashion show Mon 10-19 ✓; 付尾款 Tue 10-20 20:00 ✓;
     霜降 Fri 10-23 ✓; S16 first Swiss match Sat 10-24 (01:00 Beijing) ✓; 立冬 Nov 7 ✓;
     final Sun Nov 15 03:00 Beijing ✓. Politics-term scan: zero.
  8. **Furniture — PASS.** P1 badge verbatim «TEXTOS EN CHINO SIMPLIFICADO · EXPLICACIONES
     EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES»; all 8 pages carry
     «Lucerna · SEMANARIO CHINO SIMPLIFICADO VOL.1 · TEXTO EN CHINO SIMPLIFICADO ·
     EXPLICACIONES EN ESPAÑOL» and «Página N de 8»; masthead «Lucerna», no article.
  9. **Geometric occlusion audit (independent run) — PASS after fixes.** Own audit
     (paint-order; PIL glyph metrics with the build's own fonts, SC index; ink band
     baseline −0.88em…+0.30em; line boxes expanded by half stroke width), validated first
     on a synthetic positive control (all six classes fire; clean control silent).
     **Correction to §6: the builder's "1 raw flag" claim is wrong.** The independent audit
     found **13 raw flags** on the shipped render, of which **5 were REAL defects**, all
     ES-introduced explanation-layer overflows (pixel-adjudicated against the rendered
     cards; the builder's audit evidently did not test titles against their own boxes):
     (a) P6 sidebar head «蟹的小知识 · Curiosidades del cangrejo» — glyph box to x=1932,
     ink past the content edge (1885) and both page-frame lines (1910/1922);
     (b) P2 calendar box title «本周生活小日历 · Fechas de esta semana» — overflowed its box
     (right edge 1423) to x=1459, the final letter's tail covered by the P2 photo;
     (c) P5 box title «这一周的高频词 · Palabras de la semana» — ink to x=988, the final «a»
     straddling its box's right border (961);
     (d) P1 sidebar caption «Instantánea del espejo de búsquedas de Weibo» — final «o»
     (ink x 1886–1894) straddling the sidebar box's right border (1885);
     (e) P2 定金 vocab gloss — the Spanish gloss wrapped to a second line («primero»,
     baseline 1776.8) printed below its box's bottom border (1768); the core's English
     gloss fits on one line.
     **Fixes (Spanish wording only; no geometry, no Chinese, no keys/notes touched):**
     (a) → «蟹的小知识 · Datos del cangrejo» (ink now ends x=1842);
     (b) → «本周生活小日历 · Fechas clave» (ink ends 1341);
     (c) → «这一周的高频词 · Palabras clave» (ink ends 901);
     (d) → «Instantánea: espejo de búsquedas de Weibo» (ink ends 1867);
     (e) → «pequeña parte del precio, pagada primero» (one line, baseline 1752, inside the
     box; zero ink in rows 1758–1781).
     Edition re-rendered from the corrected build; the SVG diff vs the pre-fix edition is
     exactly these five elements (P3/P4/P7/P8 byte-identical; no element moved). The FULL
     pass was then re-run from the top on the final artifacts: registry/stems/CJK/printed-
     set/P7/furniture/image checks all re-verified green, and the audit re-run returns
     **5 flags, every one pixel-adjudicated a non-defect**: the P2 «Recuerda la frase»
     LINEX (ink ends row 1800, gold rule rows 1803–1804 — the builder's claim here is
     TRUE, and the identical flag fires on the shipped core); the P2/P3/P5 «frases en
     chino.» box-top grazes (actual ink ends 6–7px above each border; identical geometry
     in the core); the P1 «Fuente: …» caption (advance-width false positive — actual ink
     ends x=1879 < 1885).
  10. **Images / PDFs — PASS.** Image payloads byte-identical to the core on all 8 pages
      (counts 1/1/2/2/1/2/0/0 = 9); on-page credits match §7's Commons-API table exactly.
  11. **Banned intermediary-layer term — PASS.** Zero occurrences (Chinese and English
      forms) across the paper, this KIT, and the build code.

  **Final pins (supersede §8, which records the pre-fix render):**
  print PDF 68,841,812 B, sha256 bc92cead59147f8f8955a92b5499e94b7968c78aaae994e5086c5663a160295b;
  **web PDF 3,266,898 B (< 10 MB), sha256 53ba3cfbcf867c6dbdbfc840f8798ea0eb7e544b22119d380d2389ba7c8b26f3.**
  Verdict: **PASS — cleared for repo insert with these pins.**
