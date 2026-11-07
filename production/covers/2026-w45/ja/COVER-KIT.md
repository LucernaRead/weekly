# W45 Weekly Cover — Japanese readers (cover-w45-ja)

- Week: November 2–8, 2026 (plain Japanese date label on pages:
  2026年11月2日～8日). Reader language: Japanese (ja).
- Masthead: "Lucerna" (bare, no article — Japanese convention per
  tools/tables.json). The cover itself carries NO VOL number; it is
  marked COVER with a visible olive COVER badge on P1.
- Spec: SOP appendix five — 8 pages, 1950×2700, weekly visual system:
  warm ivory #f7f1e2, deep olive accents, serif.
- Build: `hidden_files/cover-w45-ja-build/` (`build.py` + verbatim copy
  `svglib_ja_core.py` (md5 d73e23b3…, canonical JA core svglib, never
  imported, never edited) + `svg/` + rendered `png/` proofs). No content
  module from any core build dir was imported; only the svglib wrap
  mechanism was followed, parameterized per font family (as in the
  W43 JA cover precedent) with the NO_START set extended by the ASCII
  closer set per tools/README rule 19.
- Final PDF built ONLY with `tools/webpdf.py` (text-layer web PDF).

## The 12 sources (fixed order, verbatim from cover-backfill/headlines-w45.json)

Headlines and excerpts are used character-for-character from the shared
source; all 12 headlines were confirmed present in their W45 core P1
SVGs before building, so no discrepancy was found, none was corrected,
and none was made. (Verbatim check: all 12 headlines + all 12 excerpts
confirmed present in the edition SVGs — whitespace-insensitive match,
12/12 + 12/12. The two earlier "MISS" readings were check artifacts:
adjacent <text> lines joined without a separator, then CJK lines joined
with a spurious space; the whitespace-stripped comparison passes all.)
Simplified and Traditional Chinese items are NOT converted between
scripts: the zh-cn item stays Simplified, the zh-tw item stays
Traditional, and explanations are native Japanese throughout.

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

W45 VOLs per task: FR is VOL.3; all other 11 cores are VOL.2. These
appear only on P8 (the cover itself has no VOL; P1 grep for "VOL"
returns 0). VOLs are also asserted from the JSON itself in build.py.

## Layout (binding, 8 pages)

- P1: masthead "Lucerna" + COVER badge + week label
  (2026年11月2日～8日) + cover title 「今週の十二の見出し」 +
  generic framing intro (no new facts) + 12 headline teasers in fixed
  order, two columns 01–06 / 07–12, each with a Japanese language name
  (英語, ドイツ語, フランス語, スペイン語, イタリア語, ポルトガル語,
  オランダ語, ロシア語, 日本語, 韓国語, 中国語（簡体字）,
  中国語（繁体字）) + verbatim headline, smaller type.
- P2–P7, 2 items per page in fixed order: P2 EN, DE · P3 FR, ES ·
  P4 IT, PT · P5 NL, RU · P6 JA, KO · P7 zh-cn, zh-tw. Each item:
  Japanese language tag + source masthead, verbatim headline, verbatim
  excerpt (max 4 sentences each; DE/IT naive period counts of 6/5 are
  time/number formats — 21.00 Uhr, 18.45 Uhr, 1.300–1.500 — actual
  sentence counts are 3 each), then a 1–2 sentence 「解説」 explanation
  IN JAPANESE. Every explanation claim is traceable to that item's
  headline + excerpt only; weekdays were cross-checked against the
  2026 calendar (Nov 2 Mon, Nov 3 Tue, Nov 4 Wed, Nov 6 Fri, Nov 7 Sat,
  Nov 8 Sun) and match the excerpts.
- P8: 「今週の十二紙——一覧」 — the 12 core papers at a glance in fixed
  order, each with masthead + VOL + verbatim headline, nothing invented.
- Fonts: Noto Serif/Sans CJK, per-script faces (SC for Latin/Cyrillic/
  zh-cn, JP for Japanese, KR for Korean, TC for Traditional Chinese)
  so all 12 scripts render with real glyphs. TTC face indices per
  tables.json: JP=0 / KR=1 / SC=2 / TC=3.
- Cover-original text uses no U+2019 (SVG grep count: 0). No week code
  (W45) and no language codes appear anywhere on the pages; language
  tags are full Japanese names and the week label is a plain date.

## Verification outputs

- Visual eyeball: all 8 pages rendered to PNG (CairoSVG) and inspected
  — no overflow, no cut-off text, no tofu/missing glyphs in any of the
  12 scripts, no overlapping elements, no line starting with closing
  punctuation. (Pages carry generous bottom whitespace; content ends
  well above the footer, as in the W43 JA cover.)
- Occlusion audit (`tools/occlusion_audit.py` on the SVG dir): selftest
  OK (all 6 planted classes fired, clean controls silent); final run
  **0 flags**.
- Build asserts (all passed): fixed order, VOLs from JSON, P1 teaser
  bounds, P2–P7 block bounds (all end y ≤ 2120 vs limit 2540), P8 bound
  (ends y 2011), per-line final-width re-check (≤ max_w + SEAM_SLACK 28)
  and kinsoku re-check on every wrapped line.
- Final PDF: `cover-w45-ja.pdf`, 8 pages, **647,029 bytes** (< 7 MB
  target), built with `tools/webpdf.py` (8 pages, 512 distinct chars,
  10 subset fonts: JP/KR/SC/TC serif + JP sans, regular + bold).
- Text layer: `pdftotext` returns **10,919 bytes** (non-empty). All 12
  headlines extract verbatim (12/12); all 12 excerpts extract (12/12).
  P8 VOL check: VOL.2 × 11, VOL.3 × 1 (FR). COVER badge text present;
  P1 page text contains VOL 0 times and W45 0 times.

## Issues found + fixed

1. None in layout. First build passed every assert; occlusion audit
   passed on first run (0 flags); visual inspection found no defects.
2. Check-script artifacts only (see verbatim note above): two naive
   excerpt comparisons "missed" before the whitespace handling was
   corrected; the SVGs themselves were verbatim throughout.
3. OPEN FLAG FOR PARENT (not a build defect): the 2026-10-28 standing
   rule "public pages must not carry internal structure semantics"
   names the word "cover" as internal product language, but this task's
   binding layout explicitly requires the COVER badge and "mark it
   COVER", and P8 VOLs are likewise task-required. This edition follows
   the task (COVER badge + footers, P8 VOLs) and follows the new rule
   everywhere the task leaves discretion (no W45 code, no language
   codes, Japanese language names, plain-date week label, reader-facing
   P1 subtitle and P8 title with no "カバー" wording). If the parent
   wants the badge renamed to a reader-facing label, it is a one-line
   change in build.py (badge text + footers) plus a rebuild.
