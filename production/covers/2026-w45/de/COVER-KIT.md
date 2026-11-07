# COVER-KIT — W45 Weekly Cover, reader language GERMAN (de)

## Spec (SOP附则五)
- Week W45: 2.–8. November 2026. Reader language: German. All cover-original
  writing (cover title, intro, per-item explanations, P8 headings) is in German.
- Headlines and excerpts stay in their ORIGINAL languages, verbatim, taken from
  `hidden_files/cover-backfill/headlines-w45.json` (+ `.md`) — NOT re-extracted.
  The build script loads the JSON directly, so no hand retyping of source text.
- Masthead: "Die Lucerna" (German article convention). The cover itself carries
  NO vol number; it is marked COVER (olive COVER badge on P1, COVER in every
  footer). P8 lists each core paper's own VOL (see below) — that is the cores'
  numbering, not the cover's.
- 8 pages, 1950×2700, weekly visual system: warm ivory #f7f1e2, deep olive
  accents, serif. Built with the DE core's build patterns (svglib.py COPIED into
  the build dir, not imported from a core dir).
- Explanation rule: every claim in the German "WAS DAS BEDEUTET" notes is
  traceable to that item's headline + excerpt ONLY — no facts beyond the source
  article. Keyword glosses only (e.g. Ip-dong romanization of 입동, Enem/Finados
  kept as names).

## The 12 sources (fixed order, verbatim)
Source file: `hidden_files/cover-backfill/headlines-w45.json`. Order:
en, de, fr, es, it, pt, nl, ru, ja, ko, zh-cn, zh-tw.

| # | Lang | Core masthead | VOL (P8) | Headline (verbatim) |
|---|------|---------------|----------|---------------------|
| 1 | en | The Lucerna | VOL.2 | America Votes : Election Day Comes on Tuesday, November 3 |
| 2 | de | Die Lucerna | VOL.2 | Englische Woche in Deutschland: Vier Nächte Fußball, dann der 9. Spieltag |
| 3 | fr | Le Lucerna | VOL.3 | Paris, Plailly, Port-en-Bessin : le week-end où tout se joue |
| 4 | es | La Lucerna | VOL.2 | La cuenta atrás del 29-N: la vivienda decide la campaña |
| 5 | it | La Lucerna | VOL.2 | Arriva il primo freddo: l'Italia si copre e si mette a tavola |
| 6 | pt | A Lucerna | VOL.2 | Do feriadão à prova: a semana do Enem |
| 7 | nl | De Lucerna | VOL.2 | Nederland in de Klimaatweek: bomen, musea en voetbal |
| 8 | ru | Lucerna | VOL.2 | Одна среда посреди недели |
| 9 | ja | Lucerna | VOL.2 | 文化の日と紅葉の週末 |
| 10 | ko | Lucerna | VOL.2 | 겨울이 오는 주간 — 단풍의 끝, 김장의 시작 |
| 11 | zh-cn | Lucerna | VOL.2 | 双11还在进行，冬天也要来了 |
| 12 | zh-tw | Lucerna | VOL.2 | 金融科技週開幕！香港迎四萬五千人 |

W45 VOLs verified per task: FR is VOL.3; all other 11 cores are VOL.2.
The build script asserts this against the JSON before building.
No discrepancy between the JSON and the task's VOL statement was found.
(Core build dirs were not present on this VM, so no independent re-check
against core SVGs was possible; the JSON .md states headlines were
cross-checked against the print PDF page 1.)

## Layout (binding, 8 pages)
- P1: "Die Lucerna" masthead + COVER badge + week label "2.-8. November 2026"
  + cover title "Zwölf Titelseiten, eine Woche" + 2-sentence generic framing
  intro in German (no new facts) + 12 headline teasers in fixed order
  (German source-language label + native label + verbatim headline).
- P2–P7: the 12 items in full, 2 per page, fixed order: P2 EN/DE, P3 FR/ES,
  P4 IT/PT, P5 NL/RU, P6 JA/KO, P7 zh-cn/zh-tw. Each item: source-language tag,
  verbatim headline, verbatim excerpt, then "WAS DAS BEDEUTET" — a 1–2 sentence
  explanation IN GERMAN.
- P8: "Die zwölf Zeitungen dieser Woche" — the week's 12 core papers at a
  glance, fixed order: masthead + VOL + verbatim headline each.
- Fonts: Noto Serif/Sans CJK (SC/JP/KR/TC faces per source language), so all 12
  scripts render: Latin, Cyrillic, Japanese, Korean, Simplified + Traditional
  Chinese.

## Build
- Build dir: `hidden_files/cover-w45-de-build/` — `build_cover.py` + `svglib.py`
  (copied) + `svg/` (8 SVGs) + `png/` (8 eyeball renders).
- Edition dir: `files/cover-w45-de/` — `svg/` + `cover-w45-de.pdf` + this kit.
- PDF built ONLY with:
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`

## Verification outputs
- Eyeball: all 8 PNGs reviewed at 780 px wide — no overflow, no cut-off text,
  no tofu/missing glyphs (all 12 scripts render), no overlapping elements
  visible. P3 and P7 re-checked after the spacing fix below.
- Occlusion audit (`tools/occlusion_audit.py` on the SVGs): final run CLEAN —
  `svg/: 0 flags` (selftest OK: all 6 planted classes fired, clean controls
  silent).
- Web PDF: `cover-w45-de.pdf`, 425,611 bytes (< 7 MB target), 8 pages,
  pdftotext 9,960 bytes (non-empty).
- Headline extraction: ALL 12 headlines extract from the PDF (whitespace-
  normalized search).
- Excerpt extraction: ALL 12 excerpts extract as well (whitespace-stripped
  comparison; see issue note below about CJK line-wrap spaces).
- VOL check: pages 1–7 of the PDF contain no "VOL" string (cover carries no
  vol); VOL appears only on P8, per core.
- SHA-256: 723289d3d1911d93136b2a6669667588e9ea6bb2760a179a2e23ad7e023fa7b5

## Issues found + fixed
1. P1 overflow (build assert): first build ended at y=2522.2 at the zh-tw
   teaser, past the 2520 limit. Fixed by tightening P1 teasers: tag gap 40→38,
   headline 40→38 pt, post-headline gap 18→14. Rebuilt clean.
2. Occlusion audit TEXTX ×4 (first audit run): tag-line ink touched headline
   ink on P3 (FR tag, 8.8 px), P6 (KO tag, 3.0 px), P7 (zh-cn tag, 6.5 px;
   zh-tw tag, 6.5 px) — the 52 px tag→headline gap was too tight at 34 pt tag /
   60 pt headline. Fixed by widening the P2–P7 tag→headline gap 52→64 px.
   Re-audit: 0 flags. Re-rendered PNGs confirm comfortable spacing.
3. Excerpt check artifact (NOT a defect): whitespace-normalized pdftotext
   search initially "missed" the ja/ko/zh-cn/zh-tw excerpts because pdftotext
   joins wrapped CJK lines with a space. Whitespace-stripped comparison
   confirms all 12 excerpts are present verbatim. Headlines (single-line)
   matched under both comparisons.
4. Pre-flight: no `cover-w45-de-build/` dir existed and no recent activity —
   proceeded (did not stand down).
