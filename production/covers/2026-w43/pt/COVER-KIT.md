# COVER-KIT — W43 Cover for Portuguese readers (A Lucerna · COVER)

## Spec
- SOP附则五 (weekly-report-SOP.md): weekly cover, one per reader language; NOT
  a 131st regular edition. Reader language: **Portuguese (pt)** — all
  cover-original writing (title, intro, explanations, labels, footers) is in
  Portuguese. Headlines and excerpts stay in their ORIGINAL languages, verbatim.
- Masthead: **A Lucerna** (Portuguese article convention). **No VOL number for
  the cover itself** — marked **COVER** (visible COVER badge on P1 + COVER in
  every footer). The VOL numbers on P8 are the twelve core papers' own VOLs,
  as required by the layout spec.
- 8 pages, 1950×2700, weekly visual system: warm ivory #f7f1e2, deep olive
  accents, serif. Text-layer PDF built with tools/webpdf.py.

## Sources (verbatim, fixed order)
All headlines + excerpts loaded programmatically from
`hidden_files/cover-backfill/headlines-w43.json` (never re-typed), so they are
character-for-character identical to the shared extraction. No discrepancy
between the JSON and the task brief was found; no source core was re-read
(per task: use the inputs, do not re-extract).

| # | Lang | Core dir | Masthead | VOL | Headline (verbatim) |
|---|------|----------|----------|-----|--------------------|
| 01 | en | weekly-report-en-vol1 | The Lucerna | 1 | First Votes, First Games : America's Biggest Week of the Autumn |
| 02 | de | weekly-report-de-vol1 | Die Lucerna | 1 | Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien |
| 03 | fr | weekly-report-vol4 | Le Lucerna | 2 | Présidentielle 2027 : les Français regardent déjà les sondages |
| 04 | es | weekly-report-es-vol1 | La Lucerna | 1 | Este domingo: dormimos una hora más… ¡y se juega el Clásico! |
| 05 | it | weekly-report-it-vol1 | La Lucerna | 1 | Un'ora in più di sonno: domenica torna l'ora solare |
| 06 | pt | weekly-report-pt-vol1 | A Lucerna | 1 | Domingo é dia de decisão: o Brasil volta às urnas |
| 07 | nl | weekly-report-nl-vol1 | De Lucerna | 1 | Een volle week: vakantie, design, dance — en een uur extra slaap |
| 08 | ru | weekly-report-ru-vol1 | Lucerna | 1 | Первый снег — уже на этой неделе! |
| 09 | ja | weekly-report-ja-vol1 | Lucerna | 1 | 土よう日、日本シリーズが始まる！ |
| 10 | ko | weekly-report-ko-vol1 | Lucerna | 1 | 태풍 참피가 오고 있어요 |
| 11 | zh-cn | weekly-report-zhcn-vol1 | Lucerna | 1 | 双11到了「付尾款」的这一周 |
| 12 | zh-tw | weekly-report-zhtw-vol1 | Lucerna | 1 | 強颱薔琵壓境！週五、週六風雨最大 |

Excerpts: the JSON `excerpt` field for each item, reproduced in full on P2–P7
(≤4 sentences each, as supplied). Explanations (1–2 sentences, Portuguese,
headed "O que isto quer dizer") restate only what each item's headline +
excerpt say; no fact beyond the source article was introduced.

## Layout (8 pages)
- **P1**: COVER badge + masthead "A Lucerna" + week label "19 a 25 de outubro
  de 2026 · Semana 43" + cover title "Uma semana, doze manchetes" + generic
  framing intro (no new facts) + 12 headline teasers in fixed order, two-column
  grid (left 01–06, right 07–12), source-language label + verbatim headline +
  closing line "Boa leitura em doze línguas."
- **P2–P7**: the 12 items in full, 2 per page, fixed order (P2 EN/DE, P3 FR/ES,
  P4 IT/PT, P5 NL/RU, P6 JA/KO, P7 zh-cn/zh-tw). Each item: source-language tag
  + core masthead, verbatim headline, verbatim excerpt, Portuguese explanation.
- **P8**: the week's 12 core papers at a glance, fixed order: masthead + VOL +
  verbatim headline per core.

## Build
- Build dir: `hidden_files/cover-w43-pt-build/` — `build.py` + `svglib.py`
  (copied from the PT core build dir, NOT imported: frame rects rescaled for
  1950×2700, `para()` gained a `family` parameter). Per-language serif faces:
  JP → Noto Serif CJK JP, KR → KR, zh-tw → TC, all others → SC.
- Pre-flight: the build dir did not exist — no other worker was active.
- No git operations performed (per task).

## Verification
- **Eyeball (CairoSVG PNGs, all 8 pages)**: no overflow, no cut-off text, no
  overlapping elements, no tofu — Latin, Cyrillic, Japanese, Korean,
  Simplified + Traditional Chinese all render.
- **Occlusion audit** (`tools/venv/bin/python tools/occlusion_audit.py svg/`):
  selftest OK, **`svg/: 0 flags`** — CLEAN.
- **Final PDF** (built ONLY with
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`):
  `A-Lucerna-COVER-W43-web.pdf`, **392,748 bytes** (target < 7 MB), 8 pages,
  **9,445 text bytes** from pdftotext (non-empty) — updated by the 2026-10-28
  P6 fix below (was 392,746 bytes before the fix; text bytes unchanged
  because the corrected name has the same length).
- **Headline extraction**: all 12 headlines extract from the PDF. All 12
  excerpts also extract; three CJK excerpts (ja, zh-cn, zh-tw) only match after
  whitespace-insensitive comparison because pdftotext inserts a line-break
  inside a CJK word at wrap points (e.g. "2年 / ぶり") — characters present in
  order, no content missing.

## Issues found + fixed
1. `svglib.py` `para()` had no font-family parameter, so CJK-variant faces
   could not be selected for excerpts — added `family` parameter to the local
   copy (core build dir untouched).
2. Draft build.py contained a leftover no-op placeholder line in the P2–P7
   loop — removed before first run; it never drew anything.
3. zh-tw explanation draft missed a space ("tufão薔琵") — fixed to "tufão 薔琵".
4. P1 bottom third was empty — added a gold rule + closing line
   "Boa leitura em doze línguas." above the footer (generic, no new facts).
5. First pdftotext check flagged 3 CJK excerpts as MISS — diagnosed as
   pdftotext line-wrap artefacts, confirmed present via whitespace-insensitive
   match; not a PDF defect, no rebuild needed.
6. **Fix 2026-10-28 (P6, KO explanation — wrong typhoon name, single-string
   fix, no git operations)**: the Portuguese explanation for the Korean item
   misspelled the typhoon name. Fixed in the build source
   (`hidden_files/cover-w43-pt-build/build.py`, EXPL["ko"]), SVGs regenerated
   with `build.py` and copied to `svg/`, PDF rebuilt ONLY with
   `tools/venv/bin/python tools/webpdf.py svg/ A-Lucerna-COVER-W43-web.pdf`.
   - OLD: "O tufão Chanpi, o 30.º da temporada, avança para norte"
   - NEW: "O tufão Champi, o 30.º da temporada, avança para norte"
   - Authority: the ko core's storm is Champi (Korean 참피, Laos-contributed
     name meaning "flower"; ko excerpt "제30호 태풍 '참피'"). The rest of the
     explanation ("e foi classificado como muito forte na manhã do dia 21; o
     nome, dado pelo Laos, significa flor.") is unchanged. No headline,
     excerpt, or other explanation was touched — including the zh-tw
     explanation, which correctly uses 薔琵 with no Latin name.
   - Re-verification: occlusion audit selftest OK, **`svg/: 0 flags`**;
     PDF **392,748 bytes** (< 7 MB), 8 pages, **9,445 pdftotext bytes**
     (non-empty); all 12 headlines AND all 12 excerpts extract
     (whitespace-insensitive match, as before); "Chanpi" count 0 across
     build.py + SVGs + PDF text, "Champi" present in P6. Before/after SHA-256
     comparison: exactly 4 files changed — `build.py`, build `svg/p6.svg`,
     edition `svg/p6.svg`, and the PDF; the other 7 SVGs are byte-identical.
