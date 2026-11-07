# COVER-KIT — W45 Weekly Cover, reader language PORTUGUESE (pt)

## Spec (SOP appendix five)
- Week W45: 2 a 8 de novembro de 2026. Reader language: Portuguese. All
  cover-original writing (cover title, intro, per-item explanations, P8
  headings) is in Portuguese.
- Headlines and excerpts stay in their ORIGINAL languages, verbatim, loaded
  at build time from `hidden_files/cover-backfill/headlines-w45.json` — NOT
  retyped, NOT re-extracted. The build script asserts the fixed order and
  the VOLs before building.
- Masthead: "A Lucerna" (Portuguese article convention). The cover itself
  carries NO vol number; it is marked COVER (olive COVER badge on P1, COVER
  in every header/footer). P8 lists each core paper's own VOL (see below) —
  that is the cores' numbering, not the cover's.
- 8 pages, 1950×2700, weekly visual system: warm ivory #f7f1e2, deep olive
  accents, serif. Built with the PT core's build patterns (svglib.py COPIED
  into the build dir from the W45 DE cover build, not imported from any
  core build dir).
- Explanation rule: every claim in the Portuguese "O QUE ISTO SIGNIFICA"
  notes is traceable to that item's headline + excerpt ONLY — no facts
  beyond the source article. Keyword glosses only (e.g. Ip-dong
  romanization of 입동, Enem/Finados kept as names).
- Cover-original text uses ASCII apostrophes only (no U+2019: it renders
  fullwidth in Noto CJK). This cover's Portuguese text needs no apostrophes.
- Verbatim items are NEVER converted between scripts: the zh-tw item stays
  Traditional, the zh-cn item stays Simplified.

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

## JSON-vs-core cross-check (no discrepancy)
Before building, every JSON headline was checked against its core's P1 SVG
(`svg_sources` file in the core dir): all 12 headlines found verbatim
(whitespace-normalized; CJK also space-stripped). Every excerpt's first
sentence was likewise found in its core's P1 SVG. No JSON-vs-core
discrepancy was found, so no stop was needed.

## Layout (binding, 8 pages)
- P1: "A Lucerna" masthead + COVER badge + week label "2 a 8 de novembro
  de 2026" + cover title "Doze capas, uma semana" + 2-sentence generic
  framing intro in Portuguese (no new facts) + 12 headline teasers in fixed
  order (Portuguese source-language name + native label + verbatim headline).
- P2–P7: the 12 items in full, 2 per page, fixed order: P2 EN/DE, P3 FR/ES,
  P4 IT/PT, P5 NL/RU, P6 JA/KO, P7 zh-cn/zh-tw. Each item: source-language
  tag, verbatim headline, verbatim excerpt, then "O QUE ISTO SIGNIFICA" —
  a 1–2 sentence explanation IN PORTUGUESE.
- P8: "Os doze jornais desta semana" — the week's 12 core papers at a
  glance, fixed order: masthead + VOL + verbatim headline each.
- Fonts: Noto Serif/Sans CJK (SC/JP/KR/TC faces per source language), so all
  12 scripts render: Latin, Cyrillic, Japanese, Korean, Simplified +
  Traditional Chinese.

## Build
- Build dir: `hidden_files/cover-w45-pt-build/` — `build_cover.py` +
  `svglib.py` (copied) + `svg/` (8 SVGs) + `png/` (8 eyeball renders).
- Edition dir: `files/cover-w45-pt/` — `svg/` + `cover-w45-pt.pdf` + this kit.
- PDF built ONLY with:
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`

## Verification outputs
- Eyeball: all 8 PNGs reviewed at 780 px wide — no overflow, no cut-off text,
  no tofu/missing glyphs (all 12 scripts render), no overlapping elements
  visible. P1 and P4 re-checked after the tag-dedupe fix below.
- Occlusion audit (`tools/occlusion_audit.py` on the edition SVGs): final
  run CLEAN — `files/cover-w45-pt/svg: 0 flags` (selftest OK: all 6 planted
  classes fired, clean controls silent).
- Web PDF: `cover-w45-pt.pdf`, 426,351 bytes (< 7 MB target), 8 pages,
  pdftotext 9,827 bytes (non-empty).
- Headline extraction: ALL 12 headlines extract from the PDF
  (whitespace-normalized search; CJK also space-stripped).
- Excerpt extraction: ALL 12 excerpts extract as well (same comparison).
- VOL check: pages 1–7 of the PDF contain no "VOL" string (cover carries no
  vol); VOL appears only on P8, per core (FR VOL.3, others VOL.2).
- SHA-256: 5d76593986616e3a0867f8485d5d5dae9b4fa24f22aecb7806899b6d131820e0

## Issues found + fixed
1. Duplicate source-language tags: the Portuguese name and the native label
   coincide for Italian ("ITALIANO · ITALIANO") and Portuguese
   ("PORTUGUÊS · PORTUGUÊS"), which read as a stutter on P1 and P4. Fixed by
   deduping the tag when both names are equal after uppercasing (tag_of in
   build_cover.py). Rebuilt, re-audited (0 flags), re-rendered P1/P4 and
   confirmed single tags. Final PDF rebuilt from the fixed SVGs.
2. Pre-flight: no `cover-w45-pt-build/` dir existed and no recent activity —
   no other builder was active, so this build proceeded.

## Open flag for the parent (not changed unilaterally)
- During this build, a new standing rule landed in MEMORY.md (2026-10-28):
  public-facing pages must not carry internal production structure —
  including the internal product name "cover". This edition follows the
  task's binding layout, which explicitly requires the COVER badge and
  COVER marking (P1 badge + COVER in every header/footer). The cover
  otherwise complies with that rule: no week codes (only plain dates
  "2 a 8 de novembro de 2026"), no language codes (full language names
  only), no repo links, no internal column names. If the parent wants the
  COVER markings stripped to comply with the new rule, that is a layout
  change to the task spec, not a build fix — say so and it can be rebuilt
  without them.
