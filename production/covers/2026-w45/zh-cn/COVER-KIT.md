# COVER-KIT — Weekly cover, W45, Simplified Chinese readers

## Spec
- Week: W45 = November 2–8, 2026. Reader: Simplified Chinese (native writing,
  never converted from Traditional).
- Pages: 8, 1950×2700, warm ivory #f7f1e2, deep olive accents, serif headlines
  (the weekly visual system).
- Masthead: bare "Lucerna" (no article — tables.json zh-cn entry).
- The cover carries NO VOL number of its own; it is marked COVER.
- P8 VOLs: FR VOL.3, all other 11 cores VOL.2.

## Sources
- Headlines + excerpts loaded VERBATIM at build time from
  `hidden_files/cover-backfill/headlines-w45.json` (12 items, fixed order
  EN DE FR ES IT PT NL RU JA KO zh-cn zh-tw). Never retyped, re-punctuated,
  or converted between scripts. Note: the JSON spellings are authoritative,
  including the spaced colons in the EN and FR headlines
  ("America Votes : …", "… Port-en-Bessin : …").
- W45 cores under `files/`: weekly-report-w45-<lang>-core (en/de/fr/es/it/
  pt/nl/ru/ja/ko), weekly-report-w45-zhcn-core, weekly-report-w45-zhtw-core.
  Existence of each core dir + P1 SVG source was checked; no JSON-vs-core
  discrepancy was found (no re-extraction, per task).
- Build method: the Simplified Chinese core's build patterns, COPIED into the
  build script (never imported): PIL-measured wrap, SC face index 2
  (JP=0 / KR=1 / SC=2 / TC=3), kinsoku post-processing with final line widths
  re-checked (build asserts on any violation). Cover-original text uses ASCII
  apostrophes only; no U+2019 anywhere in the builder.
- Explanations: newly written in Simplified Chinese, 1–2 sentences each, every
  direction/number/date/proper name matching its item's excerpt exactly, no
  facts beyond the source article. The zh-tw item's headline/excerpt stay
  Traditional verbatim; the zh-cn item stays Simplified; explanations are
  native Simplified.

## Layout
- P1: masthead "Lucerna" + COVER badge + week label "2026年11月2日至8日" +
  cover title "一周十二条头条" + generic framing intro (no new facts) +
  12 headline teasers in fixed order (source-language label + verbatim
  headline, numbered 01–12, left column 1–6, right column 7–12).
- P2–P7, 2 items per page: P2 EN+DE, P3 FR+ES, P4 IT+PT, P5 NL+RU, P6 JA+KO,
  P7 zh-cn+zh-tw. Each item: source-language tag + verbatim headline +
  verbatim excerpt (all ≤ 4 sentences) + Simplified Chinese explanation box.
- P8: "本周十二篇核心报纸一览" — masthead + VOL + verbatim headline for all
  12 cores, from the same extracted material only.

## Build
- Build dir: `hidden_files/cover-w45-zh-cn-build/` (build.py, copied HYBRID
  svglib measurement/wrap/kinsoku code inside it, svg/, png/ renders).
  Builder adapted from the proven `cover-w43-zh-cn-build/build.py`.
- Edition dir: `files/cover-w45-zh-cn/` (svg/ + cover-w45-zh-cn.pdf + this file).
- Final PDF produced ONLY via `tools/webpdf.py` run with `tools/venv/bin/python`
  (text-layer web PDF: vector text + subset fonts).

## Verification outputs
- PDF: `files/cover-w45-zh-cn/cover-w45-zh-cn.pdf` — 588,393 bytes (< 7 MB),
  8 pages, page size 1462.5 × 2025 pts.
- Text layer: `pdftotext` on the final PDF returns 10,053 bytes (non-empty).
  All 12 headlines extract verbatim; all 12 excerpt starts extract.
- Occlusion audit: `tools/occlusion_audit.py` on the edition SVGs — CLEAN,
  0 flags (selftest OK: all 6 planted classes fired, clean controls silent).
  Same result on the build SVGs before copying.
- Visual eyeball: all 8 rendered pages reviewed (png/ in the build dir).
  No overflow, cut-off, overlap, or tofu in any of the 12 scripts.
  Simplified vs Traditional forms correct per item: P7 zh-cn item in
  Simplified, zh-tw item in Traditional verbatim, explanations in Simplified.
- Structure checks: exactly 8 pages; fixed order EN DE FR ES IT PT NL RU JA KO
  zh-cn zh-tw; P2–P7 pairings as specified; masthead + COVER badge on P1;
  P1 contains no VOL; P8 masthead + VOL correct (FR VOL.3, others VOL.2).
  Build-time asserts passed: all item blocks end ≤ y 2540 (max observed
  2096), P8 ends y 2011, all kinsoku-adjusted line widths within max width.

## Issues found / fixed
- PNG render first attempt failed with system python3 (cairosvg not
  installed there); re-rendered with `tools/venv/bin/python` — all 8 pages
  rendered. Not a defect in the edition.
- One stale W43 comment in the adapted builder (a gloss note about Clásico /
  a typhoon name) was corrected; W45 needs no name glosses — all proper
  names are carried verbatim from the excerpts.
- DE/IT excerpt "sentence-mark" counts look high on a naive count only
  because of decimal times/altitudes (21.00, 18.45, 1.300–1.500); each
  excerpt is 3 real sentences, within the max-4 rule. No change needed.
- No other issues. No content was silently fixed: headlines/excerpts are
  byte-identical to the JSON (verbatim guard in the builder).
