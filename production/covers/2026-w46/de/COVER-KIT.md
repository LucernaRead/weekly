# W46 Weekly Cover — German readers (cover-w46-de)

- Week: November 9–15, 2026 (W46). Reader language: German (de).
- Masthead: "Die Lucerna" (cover-language article convention). The cover itself carries
  NO VOL number; it is marked COVER with a visible olive COVER badge on P1 and
  COVER in every header/footer.
- Spec: SOP 附则五 (weekly-report-SOP.md) — 8 pages, 1950×2700, weekly visual
  system: warm ivory #f7f1e2, deep olive accents, serif.
- Build: `hidden_files/w46/cover-w46-build/` (`build_covers.py` + copied `svglib.py`
  + `headlines-w46.json` + `cover_data.py` + `svg/` per cover). No content module
  from any core build dir was imported; only the svglib library code was copied
  into the build dir. All 12 covers share one builder; per-reader furniture and
  explanations live in `cover_data.py`.
- Final PDF built ONLY with `tools/webpdf.py` (text-layer web PDF).

## The 12 sources (fixed order, verbatim from the frozen W46 cores)

Headlines and excerpts were extracted from each core's P1 main story and
cross-checked character-for-character (whitespace-normalized) against the
core's P1 SVG joined text; all 12 headlines + all 12 excerpts matched, so no
correction was needed and none was made. Excerpt = first 3 sentences of the
P1 main article body. The zh-cn core's printed SVG uses full-width punctuation;
the cover uses the printed form (e.g. full-width ， in the zh-cn headline and
excerpt). The RU core's P1 carries a short display title plus a longer deck
line; the cover uses the large-type display title as the headline, per the
W45 rule (largest P1 headline line), and the deck is not quoted.

| # | Source | Core paper masthead / VOL (P8) | Headline (verbatim) |
|---|--------|-------------------------------|---------------------|
| 1 | en | The Lucerna · VOL.3 | Eleven Eleven : The Two Minutes When the English-Speaking World Stops |
| 2 | de | Die Lucerna · VOL.3 | Länderspielpause in Deutschland: Kampf ums Viertelfinale, dann die NFL in München |
| 3 | fr | Le Lucerna · VOL.4 | Le Sénat débat, la France se souvient, Dieppe fait la fête |
| 4 | es | La Lucerna · VOL.3 | Del 11-N a la campaña: España vota en 20 días |
| 5 | it | La Lucerna · VOL.3 | San Martino porta il vino nuovo: l'Italia assaggia l'autunno |
| 6 | pt | A Lucerna · VOL.3 | Dois domingos, um feriado: o Brasil faz o segundo dia do Enem |
| 7 | nl | De Lucerna · VOL.3 | Sinterklaas komt eraan: eerst Grave, dan Amsterdam |
| 8 | ru | Lucerna · VOL.3 | Обычная неделя: пять рабочих дней |
| 9 | ja | Lucerna · VOL.3 | 七五三の週と、読書週間の終わり |
| 10 | ko | Lucerna · VOL.3 | 김장 한창, 수능 D-7 — 11월 11일은 세 가지 이름의 날 |
| 11 | zh-cn | Lucerna · VOL.3 | 双11到了，包裹也要到了 |
| 12 | zh-tw | Lucerna · VOL.3 | 雙11來了！旅展落幕，購物車先列好 |

W46 VOLs: FR is VOL.4; all other 11 cores are VOL.3. These appear only on P8
(the cover itself has no VOL; P1 grep for "VOL" returns 0).

## Layout (binding, 8 pages)

- P1: masthead + COVER badge + week label + cover title + 1–2 sentence generic
  framing intro (no new facts) + 12 headline teasers in fixed order (reader-
  language name + native label + verbatim headline).
- P2–P7, 2 items per page in fixed order: P2 EN, DE · P3 FR, ES · P4 IT, PT ·
  P5 NL, RU · P6 JA, KO · P7 zh-cn, zh-tw. Each item: source-language tag,
  verbatim headline, verbatim excerpt, then a 1–2 sentence explanation IN
  GERMAN (label: "WAS DAS BEDEUTET"). Every explanation
  claim is traceable to that item's headline + excerpt only; keyword glosses
  introduce no new facts.
- P8: "Die zwölf Zeitungen dieser Woche" — the 12 core papers at a glance in fixed order, each
  with masthead + VOL + verbatim headline, nothing invented.
- Fonts: Noto Serif/Sans CJK, per-script faces (SC for Latin/Cyrillic/zh-cn,
  JP for Japanese, KR for Korean, TC for Traditional Chinese) so all 12 scripts
  render with real glyphs. Kinsoku: no rendered line starts with closing
  punctuation (build_covers.py para()).

## Verification outputs

- Source verification (script `verify_svgs.py` + core cross-check): all 12
  headlines + all 12 excerpts extract verbatim from the cover SVGs (12/12 OK);
  no forbidden strings (week codes, URLs, scripts, SOP/proofread language) in
  any SVG; COVER marking present on all 8 pages; VOL absent from P1, VOL.3 × 11
  + VOL.4 × 1 on P8.
- Visual eyeball: all 8 pages rendered to PNG (CairoSVG) and inspected at
  contact-sheet scale plus full-frame reads of P1, P3, P6, P7 and the changed
  pages after the kinsoku fix — no overflow, no cut-off text, no tofu/missing
  glyphs, no overlapping elements.
- Occlusion audit (`tools/occlusion_audit.py` on the SVG dir): selftest OK
  (all 6 planted classes fired, clean controls silent); final run **0 flags**.
- Final PDF: `cover-w46-de.pdf`, 8 pages, **418,165 bytes**
  (< 7 MB target), built with `tools/webpdf.py`.
- Text layer: `pdftotext` returns **11,468 bytes** (non-empty). All 12
  headlines extract verbatim (12/12 OK); all 12 excerpt openings extract
  (12/12 OK). SHA-256: `33064fd29c08921a419f0626534d4dcf10c6e55d9d3a33c850639d6789401996`.

## Issues found + fixed

1. P1 overflow on first build (DE reader): intro + teasers reached y=2573.
   Fixed by adaptive P1 tightening (teaser 40→38 pt, step 40→38, gap 18→14,
   intro 46→44 pt) applied only where needed. No content changed.
2. P2–P7 overflow on first build (DE reader, P4): y=2545. Fixed by adaptive
   per-page tightening (headline/excerpt/explanation sizes + gaps) applied
   only where needed. No content changed.
3. Kinsoku defects found on visual read (round 2): dangling closing
   punctuation at a line start — zh-tw P7 explanation (」。 alone) and the JA
   excerpt/explanations (」/）。 dangles) on P6 of all covers, JA P1/P3 and
   zh-cn P2. Fixed once in the builder (kinsoku rule in para(): a line never
   starts with closing punctuation; the previous CJK character moves down).
   16 pages re-rendered; verbatim + occlusion gates re-run clean (0 flags),
   changed pages re-eyeballed.
4. No other issues. No source discrepancy, no tofu, no footer/edge flags.
