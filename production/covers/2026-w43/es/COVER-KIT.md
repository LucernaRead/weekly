# COVER-KIT — Weekly Cover W43, reader language SPANISH (es)

## 1. Spec (SOP 附则五)

- Weekly cover for W43 (19–25 October 2026), reader language **Spanish**.
  All cover-original writing (title, intro, explanations, furniture) is in
  Spanish. Headlines and excerpts stay in their original languages, verbatim.
- Masthead: **La Lucerna** (Spanish article convention). **No VOL number
  anywhere on P1**; P1 carries a visible **COVER** badge (top-right).
- 8 pages, 1950 × 2700, weekly visual system: warm ivory `#f7f1e2`,
  deep olive `#3e4c2a` accents, serif (Noto Serif CJK / Noto Sans CJK).
- No git operations were performed (per task brief); deliverables are local
  files only. No other edition was built.

## 2. The 12 sources (fixed order, from cover-backfill/headlines-w43.json)

All headlines/excerpts used character-for-character from that file; no
re-extraction, no silent fixes. No discrepancy between JSON and any source
was investigated (per brief: JSON is the input). Order and VOL (P8 only):

| # | Lang | Core dir | Masthead | VOL | Headline (verbatim) |
|---|------|----------|----------|-----|--------------------|
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

Excerpts: verbatim from the same JSON (≤4 sentences each), reproduced in
full on P2–P7. Spanish explanations (1–2 sentences each, under "EN ESPAÑOL")
restate headline + excerpt only; every claim is traceable to that item's
headline + excerpt, no facts beyond the source article. Weekday/date claims
in explanations were calendar-checked (19 Oct 2026 = Monday, 20 Oct = Tuesday,
25 Oct = Sunday, America/Toronto).

## 3. Layout

- P1: masthead "La Lucerna" + COVER badge + week label
  "Semana del 19 al 25 de octubre de 2026" + cover title
  "Doce idiomas, una semana" + 2-sentence generic framing intro (no new
  facts) + 12 headline teasers in fixed order (Spanish language label +
  source masthead + verbatim headline).
- P2: EN, DE. P3: FR, ES. P4: IT, PT. P5: NL, RU. P6: JA, KO. P7: zh-cn, zh-tw.
  Each item: source-language tag, verbatim headline, verbatim excerpt, then
  "EN ESPAÑOL" explanation in Spanish.
- P8: the week's 12 core papers at a glance, fixed order: masthead + VOL +
  verbatim headline (same extracted material only, nothing invented).
- Per-language font faces so PIL measurement matches the audit's face index:
  Latin + RU → SC (2), JA → JP (0), KO → KR (1), zh-tw → TC (3). No images
  (text-only digest cover; SOP §6's picture rule targets the news issues,
  and no public-domain image was in the cover brief's inputs).

## 4. Build

- Build dir: `hidden_files/cover-w43-es-build/` — `build.py` (self-contained;
  the ES core's `svglib.py` was copied for reference only as
  `svglib_copy_reference.py` and NOT imported, per the module-execution
  warning), `svg/` (8 SVGs), `png/` (8 eyeball renders).
- Edition dir: `files/cover-w43-es/` — `svg/` (copies of the 8 SVGs),
  `cover-w43-es.pdf`, this `COVER-KIT.md`.
- PDF built ONLY with:
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`.

## 5. Verification outputs

- Eyeball: all 8 PNG renders inspected. No overflow, no cut-off text,
  no overlapping elements, no tofu/missing glyphs — Latin, Cyrillic,
  Japanese, Korean, Simplified and Traditional Chinese all render.
- Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py svg`
  → selftest OK (all 6 planted classes fired, clean controls silent);
  **`svg: 0 flags`**, exit 0.
- Web PDF: `cover-w43-es.pdf`, **421,081 bytes** (< 7 MB target),
  8 pages, **pdftotext = 9,408 bytes** (non-empty text layer).
- Headline extraction: **all 12 headlines extract** from the PDF
  (whitespace-normalized match), and **all 12 excerpts extract**
  (whitespace-stripped match; CJK excerpts need the stripped comparison
  because pdftotext line breaks fall inside spaceless CJK text).
- SVG verbatim check: all 12 headlines + all 12 excerpts present
  character-for-character in the SVG sources.
- P1 check: contains the COVER badge, contains no "VOL" string.

## 6. Issues found + fixed

1. **Tag-label overlap (all pages, first render):** `Page.text()` returns the
   baseline unchanged, so the +12/+16 px gaps after tag lines put the next
   paragraph's first line on top of the tag. Found on eyeball of all 8 PNGs.
   Fix: tag → next-block gaps raised to 42–50 px ("EN ESPAÑOL" label to
   48 px); P1/P8 teaser gaps computed dynamically from measured headline
   heights so pages fill to y≈2500 without crossing the 2560 footer rule.
   Re-rendered and re-eyeballed: clean.
2. **False "excerpt missing" flags (verification, not content):** the first
   SVG verbatim script left `|` separators between wrapped lines, and the
   first PDF excerpt check joined pdftotext lines with spaces, both of which
   break spaceless CJK matching. Both checks were corrected (strip
   separators / strip all whitespace for CJK); content was unchanged and
   all 12 excerpts then verified present in both SVG and PDF.
3. No content defects found: no headline/excerpt discrepancy, no overflow,
   no audit flags, no tofu. No proofread round was required beyond the
   verbatim + explanation-traceability checks above (cover brief's gate is
   the occlusion audit + text-layer verification, both passed).

## 7. Fix record — independent proofread corrections (2026-10-28)

Three strings only, all in cover-original Spanish explanations; all verbatim
headlines/excerpts and all other checks had passed. Fixed in the build source
(`hidden_files/cover-w43-es-build/build.py`, EXPL dict), then the 8 SVGs were
regenerated, copied to the edition `svg/` dir, and the PDF rebuilt. No git
operations; no other file changed (diff vs prior SVGs: only p6 + p7 lines).

1. P6, item COREANO (ko), Spanish explanation: "Chanpi" → "Champi"
   (typhoon name; Korean 참피, Laos, "flower"). All other facts untouched.
2. P7, item CHINO TRADICIONAL (zh-tw), Spanish explanation: "Changpi" →
   "Jangmi" (typhoon 薔琵; per the zh-tw core's own P1 note, "Typhoon Jangmi
   is approaching the sea east of Taiwan"). All other facts untouched
   apart from fix 3.
3. P7, item CHINO TRADICIONAL (zh-tw), Spanish explanation, same sentence:
   "al sureste" → "al este-sureste" (east-southeast, per the excerpt
   東南東方約1,390公里). Only this occurrence changed; no other direction
   word elsewhere in the edition was altered.

- Layout: NO adjustment needed. The builder's rewrap kept the same line
  counts (ko explanation still 3 lines, zh-tw still 4 lines; last baselines
  unchanged at y=1409.0 / y=1535.0, far above the footer). Re-rendered P6/P7
  PNGs eyeballed: no overflow, no overlap, no cut-off text.
- Re-verification (grep on edition SVGs): zero occurrences of "Chanpi" or
  "Changpi" anywhere; "Champi" in the P6 ko explanation, "Jangmi" and
  "al este-sureste" in the P7 zh-tw explanation; no standalone "al sureste"
  remains.
- Re-audit: `tools/venv/bin/python tools/occlusion_audit.py
  files/cover-w43-es/svg` → selftest OK, **`svg: 0 flags`**, exit 0.
- Rebuilt PDF ONLY with `tools/venv/bin/python tools/webpdf.py
  files/cover-w43-es/svg files/cover-w43-es/cover-w43-es.pdf`:
  **421,089 bytes** (< 7 MB), 8 pages, **pdftotext = 9,412 bytes**
  (non-empty text layer); **all 12 headlines extract**; "Champi",
  "Jangmi" and "este-sureste" present in PDF text, "Chanpi"/"Changpi"
  absent.
