# COVER-KIT — W45 Weekly Cover, reader language RUSSIAN (ru)

## Spec (SOP appendix five)
- Week W45: 2–8 November 2026. Reader language: Russian. All cover-original
  writing (cover title, intro, per-item explanations, P8 headings) is in Russian.
- Headlines and excerpts stay in their ORIGINAL languages, verbatim, loaded
  from `hidden_files/cover-backfill/headlines-w45.json` AT BUILD TIME by
  `build_cover.py` — NOT retyped. The build script asserts the fixed order
  and the VOL rule before building.
- Masthead: "Lucerna" (Russian: bare, no article). The cover itself carries
  NO vol number; it is marked COVER (olive COVER badge on P1, COVER in every
  header/footer). P8 lists each core paper's own VOL (see below) — that is
  the cores' numbering, not the cover's.
- 8 pages, 1950×2700, weekly visual system: warm ivory #f7f1e2, deep olive
  accents, serif. Built with the W45 DE cover's build patterns (svglib.py
  COPIED into the build dir, not imported from any core dir).
- Explanation rule: every claim in the Russian "ЧТО ЭТО ЗНАЧИТ" notes is
  traceable to that item's headline + excerpt ONLY — no facts beyond the
  source article. No country or place added that the source does not name.
- Script rule: verbatim items are NEVER converted between scripts — the
  zh-tw item stays Traditional, the zh-cn item stays Simplified.
- Cover-original text uses ASCII apostrophes only, never U+2019.

## Source verification (done before building)
- All 12 JSON headlines match the corresponding core P1 SVG text verbatim
  (whitespace-normalized): EN DE FR ES IT PT NL RU JA KO zh-cn zh-tw.
- All 12 JSON excerpts match the corresponding core P1 SVG text verbatim
  (whitespace-stripped comparison, to allow for CJK line-wrap spaces).
- No JSON-vs-core discrepancy found; nothing was silently fixed.
- Pre-flight: no `cover-w45-ru-build/` dir existed and no recent activity —
  proceeded (did not stand down).

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

## Layout (binding, 8 pages)
- P1: "Lucerna" masthead + COVER badge + week label "2–8 ноября 2026 года"
  + cover title "Двенадцать первых полос, одна неделя" + 2-sentence generic
  framing intro in Russian (no new facts) + 12 headline teasers in fixed
  order (Russian source-language name + native label + verbatim headline).
- P2–P7: the 12 items in full, 2 per page, fixed order: P2 EN/DE, P3 FR/ES,
  P4 IT/PT, P5 NL/RU, P6 JA/KO, P7 zh-cn/zh-tw. Each item: source-language
  tag, verbatim headline, verbatim excerpt, then "ЧТО ЭТО ЗНАЧИТ" — a 1–2
  sentence explanation IN RUSSIAN.
- P8: "Двенадцать газет этой недели" — the week's 12 core papers at a
  glance, fixed order: masthead + VOL + verbatim headline each.
- Fonts: Noto Serif/Sans CJK (SC/JP/KR/TC faces per source language), so all
  12 scripts render: Latin, Cyrillic, Japanese, Korean, Simplified +
  Traditional Chinese.

## Build
- Build dir: `hidden_files/cover-w45-ru-build/` — `build_cover.py` +
  `svglib.py` (copied) + `svg/` (8 SVGs) + `png/` (8 eyeball renders).
- Edition dir: `files/cover-w45-ru/` — `svg/` + `cover-w45-ru.pdf` + this kit.
- PDF built ONLY with:
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`

## Verification outputs
- Eyeball: all 8 PNGs reviewed at 780 px wide — no overflow, no cut-off
  text, no tofu/missing glyphs (all 12 scripts render), no overlapping
  elements visible.
- Occlusion audit (`tools/occlusion_audit.py` on the edition SVGs): final
  run CLEAN — `svg/: 0 flags` (selftest OK: all 6 planted classes fired,
  clean controls silent).
- Web PDF: `cover-w45-ru.pdf`, 419,563 bytes (< 7 MB target), 8 pages,
  page size 1462.5 x 2025 pts, pdftotext 12,003 bytes (non-empty).
- Headline extraction: ALL 12 headlines extract from the PDF
  (whitespace-normalized search).
- Excerpt extraction: ALL 12 excerpts extract as well
  (whitespace-stripped comparison, same CJK line-wrap artifact as the DE
  cover: pdftotext joins wrapped CJK lines with a space).
- VOL check: pages 1–7 of the PDF contain no "VOL" string (cover carries no
  vol); VOL appears only on P8 — 12 occurrences, FR VOL.3, others VOL.2.
- SHA-256: 63a05ea83d4570c01e39595c2b6ec05afa99fa9ba444d8fd6d4f9bf474504898

## Issues found + fixed
1. P1 title overflow (pre-build measurement): "Двенадцать первых полос,
   одна неделя" at 84 pt measures 1784 px, wider than the 1690 px content
   column. Fixed by setting the P1 title to 76 pt before building; the
   build's overflow asserts then passed on all 8 pages.
2. No other issues. The 64 px tag→headline gap inherited from the DE cover
   (which fixed its TEXTX flags) produced a clean audit here on the first
   run — no rework needed.
3. Pre-flight: no `cover-w45-ru-build/` dir existed — proceeded.

## Open flag for the parent (NOT fixed unilaterally)
- During this build, MEMORY.md gained a new user rule (2026-10-28):
  public-facing pages must not carry internal production structure —
  week codes, language codes, placeholder tags, repo links, internal
  column names, or "cover" as an internal product name; only
  reader-understandable content (real headlines, plain dates, clean
  navigation). This cover was built per the task's binding layout, which
  explicitly requires the COVER badge/marking and P8 VOLs, so those were
  kept and this conflict is flagged rather than silently redesigned:
  applying the new rule here (dropping COVER markings, and possibly the
  P8 VOLs) would change the format across all W45 covers consistently
  and needs a parent/user decision, not a single-language deviation.
