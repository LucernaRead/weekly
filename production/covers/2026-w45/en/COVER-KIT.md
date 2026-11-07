# W45 Weekly Cover — English readers (cover-w45-en)

- Week: November 2–8, 2026 (W45). Reader language: English (en).
- Masthead: "The Lucerna" (English article convention). The cover itself carries
  NO VOL number; it is marked COVER with a visible olive COVER badge on P1.
- Spec: SOP 附则五 (weekly-report-SOP.md) — 8 pages, 1950×2700, weekly visual
  system: warm ivory #f7f1e2, deep olive accents, serif.
- Build: `hidden_files/cover-w45-en-build/` (`build_cover.py` + copied `svglib.py`
  + `svg/` + rendered `png/` proofs). No content module from any core build dir
  was imported; only the svglib library code was copied into the build dir.
- Final PDF built ONLY with `tools/webpdf.py` (text-layer web PDF).

## The 12 sources (fixed order, verbatim from cover-backfill/headlines-w45.json)

Headlines and excerpts are used character-for-character from the shared source;
no discrepancy against the JSON was found, so no correction was needed and none
was made. (Verbatim check: all 12 headlines + all 12 excerpt openings confirmed
present in both the SVGs and the extracted PDF text — see Verification.)

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

- P1: masthead "The Lucerna" + COVER badge + week label (November 2–8, 2026) +
  cover title "Twelve Front Pages, One Week" + 1-sentence generic framing intro
  (no new facts) + 12 headline teasers in fixed order (English name + native
  label + verbatim headline, smaller type).
- P2–P7, 2 items per page in fixed order: P2 EN, DE · P3 FR, ES · P4 IT, PT ·
  P5 NL, RU · P6 JA, KO · P7 zh-cn, zh-tw. Each item: source-language tag,
  verbatim headline, verbatim excerpt, then a 1–2 sentence "WHAT THIS MEANS"
  explanation IN ENGLISH. Every explanation claim is traceable to that item's
  headline + excerpt only; keyword glosses (Culture Day, Ip-dong, Double 11,
  Finados, Enem) introduce no new facts.
- P8: "This Week's Twelve Papers" — the 12 core papers at a glance in fixed
  order, each with masthead + VOL + verbatim headline, nothing invented.
- Fonts: Noto Serif/Sans CJK, per-script faces (SC for Latin/Cyrillic/zh-cn,
  JP for Japanese, KR for Korean, TC for Traditional Chinese) so all 12 scripts
  render with real glyphs.

## Verification outputs

- Visual eyeball: all 8 pages rendered to PNG (CairoSVG) and inspected — no
  overflow, no cut-off text, no tofu/missing glyphs, no overlapping elements.
  (Pages carry generous bottom whitespace; content ends well above the footer.)
- Occlusion audit (`tools/occlusion_audit.py` on the SVG dir): selftest OK
  (all 6 planted classes fired, clean controls silent); final run **0 flags**.
- Final PDF: `cover-w45-en.pdf`, 8 pages, **413,412 bytes** (< 7 MB target),
  built with `tools/webpdf.py`.
- Text layer: `pdftotext` returns **9,326 bytes** (non-empty). All 12 headlines
  extract verbatim (12/12 OK); all 12 excerpt openings extract (12/12 OK).
  P8 VOL check: VOL.2 × 11, VOL.3 × 1 (FR). COVER badge text present.

## Issues found + fixed

1. P1 overflow on first build: teaser stack reached y=2525 at the zh-cn item
   (assert limit 2520). Fixed by tightening P1 teasers (tag 30→28 pt, step
   44→40; headline 42→40 pt, line-height 1.32→1.28, trailing gap 26→18). No
   content changed.
2. Occlusion audit TEXTX × 3 (first run): language-tag ink touched headline
   ascenders on P3 (FR — cedilla descender), P6 (KO), P7 (zh-tw). Fixed by
   increasing the tag-to-headline step on P2–P7 from 52 to 74 units. Re-run:
   0 flags. Re-rendered P3/P6/P7 and re-eyeballed (P6 confirmed clean).
3. No other issues. No JSON/source discrepancy, no tofu, no footer/edge flags.
