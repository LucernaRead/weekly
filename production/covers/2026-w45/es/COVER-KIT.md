# La Lucerna · Weekly Cover W45 — Spanish-reader edition — COVER KIT

**Edition:** weekly cover, W45 = November 2–8, 2026 · **Reader language:** Spanish (explanations in Spanish) · **Cover VOL:** none — marked COVER only
**Masthead (P1):** La Lucerna · **Cover title:** Doce portadas, una semana · **Week label:** 2-8 de noviembre de 2026
**Build dir:** `hidden_files/cover-w45-es-build/` (build_cover.py + copied svglib.py + svg/ + png/ + occlusion.json)
**Edition dir:** `files/cover-w45-es/` (svg/ + cover-w45-es.pdf + this file)

## 1. Spec

- 8 pages, 1950×2700, warm ivory #f7f1e2, deep olive accents, serif — the weekly visual system (same builder pattern as the W45 EN/DE cover builds; svglib.py copied, never imported from a core build dir).
- P1 = masthead "La Lucerna" + COVER badge + week label + cover title + 1-sentence generic framing intro (no new facts) + 12 headline teasers in fixed order (source-language label + verbatim headline, smaller type).
- P2–P7 = the 12 items in full, 2 per page: P2 EN+DE, P3 FR+ES, P4 IT+PT, P5 NL+RU, P6 JA+KO, P7 zh-cn+zh-tw. Each item: source-language tag + verbatim headline + verbatim excerpt + 1–2 sentence explanation in Spanish under "QUÉ SIGNIFICA" (what happened + why it matters; no facts beyond that item's headline + excerpt).
- P8 = that week's 12 core papers at a glance (masthead + VOL + verbatim headline). VOLs: FR VOL.3, all other 11 cores VOL.2. The cover itself carries NO VOL number.
- Fixed order throughout: EN DE FR ES IT PT NL RU JA KO zh-cn zh-tw.
- Script rule: verbatim items are never converted between scripts — the zh-tw item stays Traditional, the zh-cn item stays Simplified; explanations are native Spanish. Cover-original Spanish text uses ASCII apostrophes only (no U+2019 anywhere in the edition SVGs — programmatically verified).

## 2. Sources

- Headlines + excerpts loaded at build time from `hidden_files/cover-backfill/headlines-w45.json` (12 items, fixed order), never retyped. Build asserts the order and the VOL mapping (FR 3, others 2).
- JSON-vs-core spot check before building: all 12 headlines' head and tail strings found verbatim in the corresponding core P1 SVGs, and all 12 excerpts confirmed verbatim modulo line-wrap (the two apparent mismatches in a naive check — JA and zh-cn — were line-wrap artifacts only: rejoining wrapped lines reproduces the JSON excerpt exactly). No discrepancy found; nothing silently fixed.
- Language/font data: `tools/tables.json` (Spanish masthead article "La"; TTC face indices JP=0 / KR=1 / SC=2 / TC=3; Noto CJK TTCs at /usr/share/fonts/opentype/noto/).
- Spanish explanations written fresh for this cover from each item's headline + excerpt only (see §4 for the traceability note on headline-derived details).

## 3. Layout / build notes

- P1 build ends y=2419 (limit 2520); P2 2327, P3 2184, P4 2250, P5 1920, P6 1712, P7 2042, P8 2297 (limit 2540). No build overflow asserts tripped.
- P2–P7 tag-to-headline gap is 64px, carrying the DE-build audit fix (tag ink must clear headline ink).
- P5/P6 lower halves are empty by design (two short items per page) — same as the sibling cover builds; no filler added.
- Final PDF built ONLY via `tools/webpdf.py` run with `tools/venv/bin/python` (vector text + subset fonts).

## 4. Explanations (Spanish, 2 sentences each)

Each explanation restates only its item's headline + excerpt. Two details come from headlines rather than excerpts, both legitimate (headline is part of the source item): JA "fin de semana de las hojas de otoño" (from 文化の日と紅葉の週末）; KO "final de las hojas de otoño y el inicio del kimjang" (from 단풍의 끝, 김장의 시작）; zh-cn "llegada del invierno" (from 冬天也要来了）. The ES explanation's "según la portada la vivienda decide la campaña" is the ES headline itself.

## 5. Verification outputs (all required gates)

- **PDF:** `files/cover-w45-es/cover-w45-es.pdf` — **432,271 bytes** (< 7 MB), **8 pages**, page size 1462.5 × 2025 pts. webpdf report: 309 distinct chars, 10 subset fonts, **10,818 text bytes** (pdftotext on the final PDF, non-empty).
- **Headlines in PDF text layer:** all 12 extract via pdftotext (verified programmatically, whitespace-normalized; CJK also verified space-stripped).
- **Occlusion audit:** `tools/occlusion_audit.py` run on the edition SVGs — **0 flags** (selftest OK: all 6 planted classes fired, clean controls silent). Same 0-flag result on the build SVGs before copying; audit files in the build dir (`occlusion.json`, `occlusion-edition.json`).
- **SVG content checks (programmatic):** P1 teaser order strictly increasing; P1 has COVER badge and NO "VOL." string; P2–P7 pairings exactly as specified and every headline + excerpt verbatim (whitespace-stripped comparison, to allow line-wrap); P8 masthead + VOL correct for all 12 (FR VOL.3, rest VOL.2); no U+2019 in any edition SVG.
- **Visual review:** all 8 rendered pages (975×1350 PNGs in the build dir) eyeballed — no overflow, cut-off, overlap, or tofu in any of the 12 scripts (Latin, Cyrillic, Japanese, Korean, Simplified and Traditional Chinese all render).
- **Issues found/fixed:** none during this build. First build passed the occlusion audit with 0 flags and all visual pages clean; no rebuild was needed.

## 6. What was NOT done (per task)

- No git operations. No Discord posts. No PDFs or edition dumps into chat. No subagents spawned.
