# COVER-KIT — W43 Weekly Cover, Dutch readers (cover-w43-nl)

## Spec
- Source spec: SOP 附则五 (weekly cover), `files/weekly-report-SOP.md`.
- Reader language: **Dutch (nl)**. All cover-original writing (cover title,
  framing intro, per-item explanations, furniture) is in Dutch.
- Masthead: **De Lucerna** (Dutch article convention, confirmed from
  `tools/tables.json` languages.nl: article "De", masthead "De Lucerna").
- Week: **19-25 oktober 2026** (W43, 19–25 October 2026).
- The cover itself carries **NO vol number** and is marked **COVER**
  (olive COVER badge on P1, "De Lucerna · COVER" band + footer on every
  page). VOL numbers appear ONLY on P8, where they belong to the 12 core
  papers being listed (12 VOL mentions total in the PDF text layer, all on
  P8; P1–P7 contain zero VOL mentions — verified per page).
- 8 pages, 1950×2700, weekly visual system: warm ivory #f7f1e2, deep olive
  accents, serif (Noto Serif/Sans CJK SC via the NL core's `svglib.py`
  copied into the build dir; no content module from any core build dir was
  imported — code was copied instead, per the task rule). Build geometry
  adapted from the proven cover-w43-de build, including its two gap fixes
  (tag-to-headline 70 px, headline-rule-to-excerpt-baseline 78 px).

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
verbatim (≤4 sentences each). Dutch explanations (1–2 sentences each, in
`build.py` `EXPL`) restate only what the item's headline + excerpt say —
no facts beyond the source article. Keyword glosses keep the source term
(e.g. 「双11」, 「开门红」, 참피, 「薔琵」, 「共伴效應」, 鵝鑾鼻) rather
than inventing translations.

## Layout
- **P1**: COVER badge + "De Lucerna" + week label "19-25 oktober 2026" +
  cover title "Twaalf talen, twaalf krantenkoppen — één week om te lezen"
  + generic framing intro (no new facts) + 12 headline teasers in fixed
  order (Dutch language label + verbatim headline).
- **P2–P7**: 2 items per page in fixed order — P2: EN, DE. P3: FR, ES.
  P4: IT, PT. P5: NL, RU. P6: JA, KO. P7: zh-cn, zh-tw. Each item:
  Dutch source-language tag + original masthead, verbatim headline,
  verbatim excerpt, "UITLEG IN HET NEDERLANDS" box with the Dutch
  explanation. Footer note: "Alle twaalf krantenkoppen in overzicht:
  pagina 1 en pagina 8."
- **P8**: "Alle twaalf kernkranten in één oogopslag" — per core, masthead +
  VOL + verbatim headline, in fixed order. W43 VOLs: FR VOL.2, all others
  VOL.1.

## Verification outputs
- Build: `hidden_files/cover-w43-nl-build/build.py` (+ copied `svglib.py`)
  → 8 SVGs in `hidden_files/cover-w43-nl-build/svg/`, copied to
  `files/cover-w43-nl/svg/`. Measured content bottoms: P1 y=2236,
  P2 y=2147, P3 y=2090, P4 y=2006, P5 y=2013, P6 y=1738, P7 y=1923,
  P8 y=2108 (all < 2540 content limit; footer at 2580+).
- Occlusion audit: `tools/occlusion_audit.py` on the final SVGs —
  **0 flags** (selftest OK: all 6 planted classes fired, clean controls
  silent).
- Eyeball: all 8 pages rendered to PNG with CairoSVG and visually checked
  — no overflow, no cut-off text, no tofu/missing glyphs (Latin,
  Cyrillic, Japanese, Korean, Simplified + Traditional Chinese all
  render), no overlapping elements.
- Final PDF: built ONLY with
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>` —
  `files/cover-w43-nl/cover-w43-nl.pdf`, **376,514 bytes** (target < 7 MB),
  8 pages, **10,611 pdftotext text bytes** (non-empty text layer)
  (updated by fix #3 below; was 376,513 bytes / 10,606 text bytes).
- Headline extraction: **all 12 headlines extract from the PDF**
  (whitespace-normalized match). All 12 excerpts also extract
  (whitespace-stripped match).
- VOL check: exactly 12 "VOL." mentions in the PDF text layer, all on P8;
  P1–P7 zero.
- Cross-check: all 12 headlines and excerpts in `headlines-w43.json` also
  appear verbatim in `headlines-w43.md`; no JSON-vs-source discrepancy.

## Issues found + fixed
1. **No issues found.** First build passed the occlusion audit with 0
   flags and all 8 eyeballed pages were clean, because the build inherited
   the DE cover's proven geometry and gap fixes (tag-to-headline 70 px,
   headline-rule-to-excerpt-baseline 78 px). No re-render cycle was needed.
2. **No discrepancy** between `headlines-w43.json` and `headlines-w43.md`;
   no stop-and-report triggered.
3. **P7 fix (2026-10-28, zh-tw item, Dutch explanation only): wrong
   compass direction.** Authority: the zh-tw excerpt (headlines-w43.json
   and the zh-tw core P1) reads "颱風中心在鵝鑾鼻東南東方約1,390公里" —
   東南東 = EAST-southeast, not southeast.
   - OLD (wrong): "op de avond van 20 oktober lag het centrum ongeveer
     1.390 kilometer ten zuidoosten van 鵝鑾鼻"
   - NEW (correct): "op de avond van 20 oktober lag het centrum ongeveer
     1.390 kilometer ten oost-zuidoosten van 鵝鑾鼻"
   - Changed in the build source (`hidden_files/cover-w43-nl-build/build.py`
     line 97, `EXPL["zh-tw"]`) so the build stays reproducible, then all
     8 SVGs were regenerated and copied to `files/cover-w43-nl/svg/`.
     Regeneration diff: ONLY p7-cover.svg changed (p1–p6, p8 byte-identical
     to before); P7 content bottom unchanged at y=1922.6 (< 2540 limit).
   - Nothing else touched: no headline, no excerpt (the verbatim zh-tw
     headline/excerpt with Traditional characters are unchanged), no
     storm name (ko item still Champi/참피, zh-tw item still Jangmi/薔琵),
     and the rest of the zh-tw explanation (date, 1,390 km, ~60 m/s winds,
     northeast monsoon, heavier/longer rain) is unchanged.
   - Re-verification after the fix: occlusion audit on the final SVGs =
     **0 flags** (selftest OK: all 6 planted classes fired, clean controls
     silent); PDF rebuilt ONLY via
     `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>` =
     **376,514 bytes** (< 7 MB), **8 pages**, **10,611 pdftotext text
     bytes** (was 10,606; +5 = the added "oost-" characters); all 12
     headlines AND all 12 excerpts extract; VOL mentions still exactly 12,
     all on P8 (P1–P7 zero); old string absent from build.py, all SVGs
     and the PDF text layer; new string present in all three.
