# W45 Weekly Cover — Traditional Chinese readers (cover-w45-zh-tw)

- Week: November 2–8, 2026 (W45). Reader language: Traditional Chinese (zh-tw).
- Masthead: bare "Lucerna" (Traditional Chinese takes no article, per
  tables.json). The cover itself carries NO VOL number; it is marked COVER
  with a visible olive COVER badge on P1.
- Spec: SOP 附则五 (weekly-report-SOP.md) — 8 pages, 1950×2700, weekly visual
  system: warm ivory #f7f1e2, deep olive accents, serif.
- Build: `hidden_files/cover-w45-zh-tw-build/` (`build_cover.py` + COPIED
  `svglib.py` from the W45 zh-tw core build dir + `svg/` + rendered `png/`
  proofs). No content module from any core build dir was imported; only the
  zh-tw core's svglib library code was copied into the build dir (TC face
  index 3, full-width punctuation typesetting, kinsoku + width repair).
- Final PDF built ONLY with `tools/webpdf.py` (text-layer web PDF).

## The 12 sources (fixed order, verbatim from cover-backfill/headlines-w45.json)

Headlines and excerpts are loaded from the JSON at build time, never retyped.
JSON-vs-core check: all 12 headlines and all 12 excerpts confirmed present in
their core P1 SVGs. (Two first-pass excerpt checks, ja and zh-cn, failed only
because my space-joined extraction split CJK words across wrapped SVG lines;
re-checking with a no-space join, both excerpts match character-for-character.
No JSON/source discrepancy exists, so no correction was needed and none was
made.) Verbatim items are NEVER converted between scripts: the zh-cn item
stays Simplified in this cover, the zh-tw item stays Traditional, and all
explanations are written natively in Traditional Chinese.

| # | Source | Core paper masthead / VOL (P8) | Headline (verbatim) |
|---|--------|-------------------------------|---------------------|
| 1 | en | The Lucerna · VOL.2 | America Votes : Election Day Comes on Tuesday, November 3 |
| 2 | de | Die Lucerna · VOL.2 | Englische Woche in Deutschland: Vier Nächte Fußball, dann der 9. Spieltag |
| 3 | fr | Le Lucerna · VOL.3 | Paris, Plailly, Port-en-Bessin : le week-end où tout se joue |
| 4 | es | La Lucerna · VOL.2 | La cuenta atrás del 29-N: la vivienda decide la campaña |
| 5 | it | La Lucerna · VOL.2 | Arriva il primo freddo: l'Italia si copre e si mette a tavola |
| 6 | pt | A Lucerna · VOL.2 | Do feriadão à prova: a semana do Enem |
| 7 | nl | De Lucerna · VOL.2 | Nederland in de Klimaatweek: bomen, musea en voetbal |
| 8 | ru | Lucerna · VOL.2 | Одна среда посреди недели |
| 9 | ja | Lucerna · VOL.2 | 文化の日と紅葉の週末 |
| 10 | ko | Lucerna · VOL.2 | 겨울이 오는 주간 — 단풍의 끝, 김장의 시작 |
| 11 | zh-cn | Lucerna · VOL.2 | 双11还在进行，冬天也要来了 |
| 12 | zh-tw | Lucerna · VOL.2 | 金融科技週開幕！香港迎四萬五千人 |

W45 VOLs per task: FR is VOL.3; all other 11 cores are VOL.2. These appear
only on P8 (the cover itself has no VOL; P1 grep for "VOL" returns 0).

## Layout (binding, 8 pages)

- P1: masthead "Lucerna" + COVER badge + week label in Traditional Chinese
  (2026年11月2日至11月8日） + cover title "十二張頭版，同一個星期" +
  1-sentence generic framing intro (no new facts) + 12 headline teasers in
  fixed order (Traditional Chinese language name + native label + verbatim
  headline, smaller type).
- P2–P7, 2 items per page in fixed order: P2 EN, DE · P3 FR, ES · P4 IT, PT ·
  P5 NL, RU · P6 JA, KO · P7 zh-cn, zh-tw. Each item: source-language tag,
  verbatim headline, verbatim excerpt, then a 1–2 sentence "解說"
  explanation IN TRADITIONAL CHINESE. Every explanation claim is traceable
  to that item's headline + excerpt only (numbers, dates and proper names
  checked against the excerpt: e.g. 435 House seats, Bayern 21:00 /
  Stuttgart 18:45, Nanterre Rolex Paris Masters final Nov 8, Spain Nov 29,
  Italy 1,300–1,500 m snow, Enem Nov 8, Climate Week Nov 2–8, Russia
  Nov 4 Wednesday off, Culture Day Nov 3, Ip-dong Nov 7, Double 11 dates
  Oct 12 / Oct 15 / Oct 20 / Nov 13, Hong Kong FinTech Week 45,000+ /
  120+ economies / 1,000+ speakers / 800+ exhibitors / 30+ delegations).
- P8: "本週十二份報紙一覽" — the 12 core papers at a glance in fixed
  order, each with masthead + VOL + verbatim headline, nothing invented.
- Fonts: per-script serif faces (SC for Latin/Cyrillic/zh-cn, JP for
  Japanese, KR for Korean, TC for Traditional Chinese and all cover-original
  Traditional Chinese text) so all 12 scripts render with real glyphs.
  Cover-original text uses ASCII apostrophes only; no U+2019 anywhere.

## Verification outputs

- Visual eyeball: all 8 pages rendered to PNG (CairoSVG) and inspected — no
  overflow, no cut-off text, no tofu/missing glyphs, no overlapping elements.
  Simplified vs Traditional forms correct per item (P7: zh-cn headline and
  excerpt in Simplified, its explanation in Traditional; zh-tw item fully
  Traditional). Pages carry generous bottom whitespace; content ends well
  above the footer.
- Occlusion audit (`tools/occlusion_audit.py` on the edition SVGs): selftest
  OK (all 6 planted classes fired, clean controls silent); final run
  **0 flags**.
- Final PDF: `cover-w45-zh-tw.pdf`, 8 pages, **654,097 bytes** (< 7 MB
  target), built with `tools/webpdf.py` (10 subset fonts: Sans TC, Serif
  JP/KR/SC/TC, regular + bold; 532 distinct chars).
- Text layer: `pdftotext` returns **9,964 bytes** (non-empty). All 12 headlines
  extract verbatim (12/12 OK); all 12 excerpt openings extract (12/12 OK).
  P8 VOL check: VOL.2 × 11, VOL.3 × 1 (FR). COVER badge text present on P1
  (extracts as "COVER"; the SVG carries it letter-spaced as "C O V E R").
  P1 PDF text contains no "VOL".

## Issues found + fixed

1. None in layout: first build passed all overflow asserts, occlusion audit
   returned 0 flags on the first run (no tag-to-headline step change needed,
   unlike the en cover), and all 8 rendered pages passed eyeball.
2. Apparent JSON-vs-core mismatches on ja and zh-cn excerpt starts were
   extraction artifacts (wrapped SVG lines split CJK words; space-joined
   search missed them). No-space-join re-check confirmed both excerpts
   verbatim in their core P1 SVGs — not a discrepancy, no fix made.
