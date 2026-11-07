# COVER-KIT — W43 Weekly Cover, Russian readers (cover-w43-ru)

## Spec
- Source spec: SOP 附则五 (weekly cover), `files/weekly-report-SOP.md`.
- Reader language: **Russian (ru)**. All cover-original writing (cover title,
  framing intro, per-item explanations, furniture) is in Russian.
- Masthead: **Lucerna** with NO article (Russian takes no article —
  `tools/tables.json` ru entry: `article: null`, `masthead: "Lucerna"`).
- Week: **19–25 октября 2026** (W43, 19–25 October 2026).
- The cover itself carries **NO vol number** and is marked **COVER**
  (olive COVER badge on P1, "Lucerna · COVER" band + footer on every
  page). VOL numbers appear ONLY on P8, where they belong to the 12 core
  papers being listed (12 VOL mentions total in the PDF text layer;
  P1 contains zero VOL mentions — verified by count).
- 8 pages, 1950×2700, weekly visual system: warm ivory #f7f1e2, deep olive
  accents, serif (Noto Serif/Sans CJK SC via the RU core's copied
  `svglib.py`; no content module from any core build dir was imported —
  code was copied into the build dir instead, per the task rule).
  Geometry follows the proven DE-cover build (70px tag→headline gap,
  78px rule→excerpt gap — inherited fixes, see §Issues).

## The 12 sources (fixed order, verbatim from the shared source)
Source file: `hidden_files/cover-backfill/headlines-w43.json` (cross-checked
programmatically against `headlines-w43.md`: all 12 headlines and excerpts
match character for character; no discrepancy with the shared source was
found, so no stop-and-report was triggered). Headlines and excerpts are
loaded from the JSON at build time, never retyped.

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
verbatim (≤4 sentences each). Russian explanations (1–2 sentences each, in
`build.py` `EXPL`) restate only what the item's headline + excerpt say —
no facts beyond the source article. Source terms are kept verbatim in
quotes (참피, 双11, 开门红, 薔琵, 共伴效應) rather than re-transliterated,
except 鵝鑾鼻 glossed as мыс Элуаньби following the DE cover's
Kap Eluanbi precedent; Japanese team names are quoted in their original
Latin spelling from the excerpt (Yokohama DeNA BayStars, Fukuoka SoftBank
Hawks).

## Layout
- **P1**: COVER badge + "Lucerna" + week label "19–25 октября 2026" +
  cover title "Двенадцать языков, двенадцать заголовков — неделя чтения"
  + generic framing intro (no new facts) + 12 headline teasers in fixed
  order (Russian language label + verbatim headline).
- **P2–P7**: 2 items per page in fixed order — P2: EN, DE. P3: FR, ES.
  P4: IT, PT. P5: NL, RU. P6: JA, KO. P7: zh-cn, zh-tw. Each item:
  Russian source-language tag + original masthead, verbatim headline,
  verbatim excerpt, "ПОЯСНЕНИЕ НА РУССКОМ" box with the Russian explanation.
  Footer note: "Все двенадцать заголовков — обзор на страницах 1 и 8."
- **P8**: "Все двенадцать центральных газет — одним взглядом" — per core,
  masthead + VOL + verbatim headline, in fixed order (FR VOL.2, all
  others VOL.1).

## Build
- Build dir: `hidden_files/cover-w43-ru-build/` (`build.py`, copied
  `svglib.py`, `svg/`, `png/`).
- Edition dir: `files/cover-w43-ru/` (`svg/` + `cover-w43-ru.pdf`).
- Build command: `tools/venv/bin/python build.py` (8 SVGs, all pages end
  y≤2237, under the 2540 overflow limit).
- PNG render: CairoSVG at 975×1350 for visual review.
- Final PDF ONLY via:
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`
  (text-layer web PDF per SOP 附则四).

## Verification outputs
- **Visual review (all 8 PNGs eyeballed)**: no overflow, no cut-off text,
  no tofu/missing glyphs (Latin, Cyrillic, Japanese, Korean, Simplified
  and Traditional Chinese all render), no overlapping elements.
- **Occlusion audit** (`tools/occlusion_audit.py` on the SVG dir):
  selftest OK (all 6 planted classes fired, clean controls silent);
  **`svg: 0 flags`** — CLEAN, exit 0.
- **PDF text layer**: `pdftotext` returns **13,542 bytes** (non-empty);
  file **398,541 bytes** (< 7 MB target), 8 pages.
  (Pre-fix values were 13,543 text bytes / 398,644 file bytes —
  see §Issues, proofreader-fix entry 2026-10-28.)
- **Headline extraction**: all 12 verbatim headlines found in the PDF
  text layer (whitespace-normalized match).
- **Excerpt extraction**: all 12 verbatim excerpts found in the PDF text
  layer (whitespace-stripped match — see §Issues for the wrap artifact).
- **VOL audit**: P1 contains 0 VOL mentions; total VOL mentions = 12
  (the P8 rows only). COVER badge present on every page.
- **SVG audit**: all 12 verbatim headlines present in the edition SVGs;
  JSON-vs-MD cross-check passed for all 12 headlines + excerpts.

## Issues found + fixed
- **None found in this build.** The layout inherited the DE cover's two
  proven geometry fixes (70px tag→headline gap for tall CJK headline ink;
  78px gold-rule→excerpt gap so the rule clears tall glyph tops), and
  the audit came back clean on the first run — no fix-and-rerender cycle
  was needed.
- **Verification artifact (not a defect)**: a first whitespace-normalized
  pdftotext comparison reported the 4 CJK excerpts (ja, ko, zh-cn,
  zh-tw) as MISSING. Cause: pdftotext inserts a line break mid-string
  when a CJK excerpt wraps, which normalizes to a space that the
  space-free original does not contain. Re-checking with all whitespace
  stripped from both sides found all 12 excerpts verbatim, and the raw
  P6 dump shows the Japanese and Korean excerpts intact. No build change
  was made.
- **Pre-flight**: `hidden_files/cover-w43-ru-build/` did not exist at
  task start — no active work by another worker, so no stand-down was
  triggered. No git operations were performed, per the task rule.
- **Proofreader fix (2026-10-28, exactly 2 strings, nothing else
  changed)**: an independent proofreader found exactly these 2 problems
  in Russian explanations; everything else passed. Both fixes were made
  in the build source (`hidden_files/cover-w43-ru-build/build.py`,
  `EXPL`), all 8 SVGs regenerated with `tools/venv/bin/python build.py`
  (all pages end y≤2237), copied to the edition `svg/`, and the PDF
  rebuilt ONLY via `tools/venv/bin/python tools/webpdf.py <svg-dir>
  <out.pdf>`. No headline, excerpt, or other explanation was touched;
  storm names untouched (zh-tw 薔琵, ko 참피 verified present, zero
  wrong variants).
  1. P7, zh-tw explanation — wrong compass direction (excerpt says
     鵝鑾鼻東南東方, east-southeast, not southeast).
     OLD: "его центр был примерно в 1 390 километрах к юго-востоку
     от мыса Элуаньби"
     NEW: "его центр был примерно в 1 390 километрах к
     востоку-юго-востоку от мыса Элуаньби"
     (Rest of that explanation unchanged; storm name 薔琵 untouched.)
  2. P5, RU explanation — invented place word (neither the RU headline
     "Первый снег — уже на этой неделе!" nor the RU excerpt names
     Russia).
     OLD: "В России первый снег может выпасть уже на этой неделе."
     NEW: "Первый снег может выпасть уже на этой неделе."
     (Only "В России" deleted; forecast Wed/Thu/Fri 21–23 Oct, ~0 °C
     unchanged.)
  Re-verification after the fix: occlusion audit
  (`tools/occlusion_audit.py` on the edition SVGs) selftest OK,
  **`svg: 0 flags`**, exit 0; `pdftotext` on the new PDF non-empty
  (**13,542 bytes**); **8 pages**; file **398,541 bytes** (< 7 MB);
  all **12/12 headlines** extract verbatim (whitespace-normalized);
  new strings present in PDF text layer, both old strings absent;
  VOL mentions = 12. No git operations, no Discord post, no chat dump.
