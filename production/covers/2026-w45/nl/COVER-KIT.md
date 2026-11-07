# W45 Weekly Cover — Dutch readers (cover-w45-nl)

- Week: 2–8 november 2026 (W45). Reader language: Dutch (nl).
- Masthead: "De Lucerna" (Dutch article convention). The cover itself carries
  NO VOL number of its own; it is marked COVER with a visible olive COVER
  badge on P1.
- Spec: SOP appendix five — 8 pages, 1950×2700, weekly visual system:
  warm ivory #f7f1e2, deep olive accents, serif.
- Build: `hidden_files/cover-w45-nl-build/` (`build_cover.py` + copied
  `svglib.py` + `svg/` + rendered `png/` proofs). No content module from any
  core build dir was imported; only the svglib library code was copied into
  the build dir. Headlines/excerpts were loaded from
  `hidden_files/cover-backfill/headlines-w45.json` at build time, never
  retyped.
- Final PDF built ONLY with `tools/webpdf.py` (text-layer web PDF).

## The 12 sources (fixed order, verbatim from headlines-w45.json)

No JSON-vs-core discrepancy was found (spot-checked distinctive strings in
each core's P1 SVG: en "America Votes", de "Englische Woche", fr
"Port-en-Bessin", nl "Klimaatweek", zh-cn "双11", zh-tw "金融科技週" — all
present), so no correction was made. Verbatim items were never converted
between scripts: the zh-cn item stays Simplified, the zh-tw item stays
Traditional. Cover-original text uses ASCII apostrophes only (no U+2019).

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
only on P8 (P1 grep for "VOL" returns 0).

## Layout (binding, 8 pages)

- P1: masthead "De Lucerna" + COVER badge + week label (2-8 november 2026)
  + cover title "Twaalf voorpagina's, een week" + 1-sentence generic framing
  intro (no new facts) + 12 headline teasers in fixed order (Dutch language
  name + native label + verbatim headline, smaller type).
- P2–P7, 2 items per page in fixed order: P2 EN, DE · P3 FR, ES · P4 IT, PT ·
  P5 NL, RU · P6 JA, KO · P7 zh-cn, zh-tw. Each item: source-language tag,
  verbatim headline, verbatim excerpt (max 4 sentences each, as supplied),
  then a 1–2 sentence "WAT DIT BETEKENT" explanation IN DUTCH. Every
  explanation claim is traceable to that item's headline + excerpt only;
  directions, numbers, dates and proper names match the excerpt exactly.
- P8: "De twaalf kranten van deze week" — the 12 core papers at a glance in
  fixed order, each with masthead + VOL + verbatim headline, nothing
  invented.
- Fonts: Noto Serif/Sans CJK, per-script faces (SC for Latin/Cyrillic/zh-cn,
  JP for Japanese, KR for Korean, TC for Traditional Chinese) so all 12
  scripts render with real glyphs.

## Verification outputs

- Visual eyeball: all 8 pages rendered to PNG (CairoSVG) and inspected — no
  overflow, no cut-off text, no tofu/missing glyphs, no overlapping elements.
  (Pages carry generous bottom whitespace; content ends well above the
  footer.)
- Occlusion audit (`tools/occlusion_audit.py` on the edition SVGs): selftest
  OK (all 6 planted classes fired, clean controls silent); final run
  **0 flags**.
- Final PDF: `cover-w45-nl.pdf`, 8 pages, **410,201 bytes** (< 7 MB target),
  built with `tools/webpdf.py`.
- Text layer: `pdftotext` returns **9,616 bytes** (non-empty). All 12
  headlines extract verbatim (12/12 OK); all 12 excerpt openings extract
  (12/12 OK — the three CJK openings only match after stripping pdftotext
  line breaks, which is a line-wrap artefact, not missing text). P8 VOL
  check: VOL.2 × 11, VOL.3 × 1 (FR). COVER badge text present.

## Issues found + fixed

1. P1 overflow on first build: teaser stack reached y=2522.2 at the zh-tw
   item (assert limit 2520). Fixed by tightening P1 teasers (tag step 40→38,
   trailing gap 18→14). No content changed.
2. Occlusion audit TEXTX × 1 (second run): P1 French tag ink touched the
   headline (cedilla descender). Fixed by widening the P1 tag-to-headline
   step 38→44 and compensating with trailing gap 14→10. Re-run: 0 flags.
3. No other issues. No JSON/source discrepancy, no tofu, no footer/edge
   flags.

## FLAG for parent — new standing rule vs this task's spec

During this build, MEMORY.md gained a new user rule (2026-10-28): public
pages (cover pages named explicitly) must NOT carry internal production
structure — week codes, language codes, placeholder tags, repo links,
internal column names, or "cover" as an internal product name; externally
only reader-understandable content (real headlines, plain dates, clean
navigation). This edition was built to the task's binding spec, which
explicitly requires the COVER badge, so the badge and "COVER" header/footer
labels are still present. This edition contains no week codes (no "W45" on
any page) and no language codes (tags use full Dutch names + native
labels). Whether the COVER badge/labels should be renamed or dropped under
the new rule is a decision for the parent/user — it was NOT changed
unilaterally here, since the task's verification criteria explicitly
require the masthead + COVER badge on P1.
