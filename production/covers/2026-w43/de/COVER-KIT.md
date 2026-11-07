# COVER-KIT — W43 Weekly Cover, German readers (cover-w43-de)

## Spec
- Source spec: SOP 附则五 (weekly cover), `files/weekly-report-SOP.md`.
- Reader language: **German (de)**. All cover-original writing (cover title,
  framing intro, per-item explanations, furniture) is in German.
- Masthead: **Die Lucerna** (German article convention).
- Week: **19.-25. Oktober 2026** (W43, 19–25 October 2026).
- The cover itself carries **NO vol number** and is marked **COVER**
  (olive COVER badge on P1, "Die Lucerna · COVER" band + footer on every
  page). VOL numbers appear ONLY on P8, where they belong to the 12 core
  papers being listed (one VOL mention per P8 row = 12 total in the PDF
  text layer; P1–P7 contain zero VOL mentions — verified by count).
- 8 pages, 1950×2700, weekly visual system: warm ivory #f7f1e2, deep olive
  accents, serif (Noto Serif/Sans CJK SC via the DE core's copied `svglib.py`;
  no content module from any core build dir was imported — code was copied
  into the build dir instead, per the task rule).

## The 12 sources (fixed order, verbatim from the shared source)
Source file: `hidden_files/cover-backfill/headlines-w43.json` (cross-checked
against `headlines-w43.md`: all 12 headlines and excerpts match character
for character; no discrepancy with the shared source was found, so no
stop-and-report was triggered). Headlines and excerpts are loaded from the
JSON at build time, never retyped.

| # | Lang | Core dir | Masthead | VOL (P8 only) | Headline (verbatim) |
|---|------|----------|----------|---------------|---------------------|
| 1 | en | weekly-report-en-vol1 | The Lucerna | 1 | First Votes, First Games : America's Biggest Week of the Autumn |
| 2 | de | weekly-report-de-vol1 | Die Lucerna | 1 | Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien |
| 3 | fr | weekly-report-vol4 | Le Lucerna | 2 | Présidentielle 2027 : les Français regardent déjà les sondages |
| 4 | es | weekly-report-es-vol1 | La Lucerna | 1 | Este domingo: dormimos una hora más… ¡y se juega el Clásico! |
| 5 | it | weekly-report-it-vol1 | La Lucerna | 1 | Un'ora in più di sonno: domenica torna l'ora solare |
| 6 | pt | weekly-report-pt-vol1 | A Lucerna | 1 | Domingo é dia de decisão: o Brasil volta às urnas |
| 7 | nl | weekly-report-nl-vol1 | De Lucerna | 1 | Een volle week: vakantie, design, dance — en een uur extra slaap |
| 8 | ru | weekly-report-ru-vol1 | Lucerna | 1 | Первый снег — уже на этой неделе! |
| 9 | ja | weekly-report-ja-vol1 | Lucerna | 1 | 土よう日、日本シリーズが始まる！ |
| 10 | ko | weekly-report-ko-vol1 | Lucerna | 1 | 태풍 참피가 오고 있어요 |
| 11 | zh-cn | weekly-report-zhcn-vol1 | Lucerna | 1 | 双11到了「付尾款」的这一周 |
| 12 | zh-tw | weekly-report-zhtw-vol1 | Lucerna | 1 | 強颱薔琵壓境！週五、週六風雨最大 |

Excerpts: each item's P1 article-opening excerpt from the same JSON, used
verbatim (≤4 sentences each; the DE excerpt's "3.00"/"2.00" decimals are
not sentence breaks). German explanations (1–2 sentences each, in
`build.py` `EXPL`) restate only what the item's headline + excerpt say —
no facts beyond the source article. Keyword glosses keep the source term
(e.g. 「开门红」, 「共伴效應」, 참피, 鵝鑾鼻 as Kap Eluanbi) rather than
inventing translations.

## Layout
- **P1**: COVER badge + "Die Lucerna" + week label "19.-25. Oktober 2026" +
  cover title "Zwölf Sprachen, zwölf Schlagzeilen — eine Woche zum Lesen"
  + generic framing intro (no new facts) + 12 headline teasers in fixed
  order (German language label + verbatim headline).
- **P2–P7**: 2 items per page in fixed order — P2: EN, DE. P3: FR, ES.
  P4: IT, PT. P5: NL, RU. P6: JA, KO. P7: zh-cn, zh-tw. Each item:
  German source-language tag + original masthead, verbatim headline,
  verbatim excerpt, "ERKLÄRUNG AUF DEUTSCH" box with the German explanation.
  Footer note: "Alle zwölf Schlagzeilen im Überblick: Seite 1 und Seite 8."
- **P8**: "Alle zwölf Kernzeitungen auf einen Blick" — per core, masthead +
  VOL + verbatim headline, in fixed order.

## Verification outputs
- Build: `hidden_files/cover-w43-de-build/build.py` (+ copied `svglib.py`) →
  8 SVGs in `hidden_files/cover-w43-de-build/svg/`, copied to `files/cover-w43-de/svg/`.
  Measured content bottoms: P1 y=2236, P2/P3 y=2147, P4 y=2006, P5 y=2013,
  P6 y=1795, P7 y=1980, P8 y=2108 (all < 2540 content limit; footer at 2580+).
- Occlusion audit: `tools/occlusion_audit.py` on the final SVGs —
  **0 flags** (selftest OK: all 6 planted classes fired, clean controls silent).
- Eyeball: all 8 pages rendered to PNG with CairoSVG and visually checked —
  no overflow, no cut-off text, no tofu/missing glyphs (Latin, Cyrillic,
  Japanese, Korean, Simplified + Traditional Chinese all render), no
  overlapping elements.
- Final PDF: built ONLY with
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>` —
  `files/cover-w43-de/cover-w43-de.pdf`, **398,484 bytes** (target < 7 MB),
  8 pages, **10,850 pdftotext text bytes** (non-empty text layer).
- Headline extraction: **all 12 headlines extract from the PDF**
  (whitespace-normalized match). All 12 excerpts also extract
  (whitespace-stripped match; the first check's CJK misses were a
  check artifact — pdftotext line-breaks inside CJK strings, not missing text).
- SVG text check: all 12 headlines present in the SVG text layer
  (whitespace-stripped match).

## Issues found + fixed
1. **Occlusion audit TEXTX (first run, 3 flags)**: the 28 pt language tag
   line overlapped tall CJK headline ink at 54 pt on P6 (Korean) and P7
   (both Chinese items). Fix: tag-to-headline gap 44 → 70 in `item_block`.
   Re-audit: 0 flags.
2. **Gold rule grazing excerpt tops (eyeball, P2/P3)**: the rule under each
   headline sat only 22 px above the excerpt baseline, so it touched the
   tops of tall glyphs (visible in the render even though the audit's LINEX
   class only fires for lines painted AFTER the text they cross — this rule
   is painted before the excerpt). Fix: rule-to-excerpt-baseline gap
   22 → 70 px (`y += 30` → `y += 78` after the headline rule). Re-rendered
   and re-eyeballed: clear separation on all item pages; re-audit still
   0 flags.
3. **Sparse item pages (eyeball)**: first build ended P2–P7 around y≈1500–
   1700, leaving a large empty bottom. Fix: headline 54→60 pt, excerpt
   40→44 pt at 1.6 line height, explanation 34→38 pt, inter-item gap
   110→170, P8 headline 34→38 pt with wider row gaps. Final bottoms
   y≈1800–2150; remaining whitespace is even page-bottom margin.
4. **No other issues.** No discrepancy between `headlines-w43.json` and
   `headlines-w43.md`; font cmap check confirmed Noto Serif/Sans CJK SC
   covers every tested character (Latin accents, Cyrillic, kana, Hangul,
   SC/TC ideographs, dashes, quotes) before building.
