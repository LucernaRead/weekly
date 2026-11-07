# COVER-KIT — W45 Weekly Cover, reader language KOREAN (ko)

## Spec
- SOP appendix five (weekly cover): 8 pages, 1950×2700, weekly visual system
  (warm ivory #f7f1e2, deep olive #3e4c2a accents, serif).
- Reader language: Korean. All cover-original writing (title, intro,
  explanations, labels) is in Korean, 해요체 (polite informal style).
  Headlines and excerpts stay in their ORIGINAL languages, verbatim.
- Masthead: `Lucerna` with NO article (tables.json `languages.ko`:
  `article: null`, `masthead: "Lucerna"`). NO VOL number of its own:
  the cover is marked COVER (olive COVER badge under the masthead on
  P1, plus `Lucerna · COVER` footers on every page). VOLs appear ONLY
  on P8, per core.
- Week label: 2026년 11월 2일~8일 (W45, November 2–8, 2026).

## Sources (the 12 items, FIXED order)
Loaded verbatim from the shared source
`hidden_files/cover-backfill/headlines-w45.json` at build time
(`build.py` inserts headlines/excerpts programmatically, never
re-typed — no transcription drift is possible by construction).
JSON-vs-core cross-check performed before building: for every item,
the headline AND the excerpt were found (whitespace-insensitive) in
that core's P1 SVG named in `svg_sources`. NO discrepancy found;
nothing was silently fixed. Note: the JSON's spacing is authoritative
(e.g. EN `America Votes : Election Day...`, FR `...-Bessin : le...`
carry a space before the colon, as in the cores).

| # | Lang | Core dir | Masthead | VOL (P8 only) | Headline (verbatim) |
|---|------|----------|----------|---------------|---------------------|
| 1 | en | weekly-report-w45-en-core | The Lucerna | VOL.2 | America Votes : Election Day Comes on Tuesday, November 3 |
| 2 | de | weekly-report-w45-de-core | Die Lucerna | VOL.2 | Englische Woche in Deutschland: Vier Nächte Fußball, dann der 9. Spieltag |
| 3 | fr | weekly-report-w45-fr-core | Le Lucerna | VOL.3 | Paris, Plailly, Port-en-Bessin : le week-end où tout se joue |
| 4 | es | weekly-report-w45-es-core | La Lucerna | VOL.2 | La cuenta atrás del 29-N: la vivienda decide la campaña |
| 5 | it | weekly-report-w45-it-core | La Lucerna | VOL.2 | Arriva il primo freddo: l'Italia si copre e si mette a tavola |
| 6 | pt | weekly-report-w45-pt-core | A Lucerna | VOL.2 | Do feriadão à prova: a semana do Enem |
| 7 | nl | weekly-report-w45-nl-core | De Lucerna | VOL.2 | Nederland in de Klimaatweek: bomen, musea en voetbal |
| 8 | ru | weekly-report-w45-ru-core | Lucerna | VOL.2 | Одна среда посреди недели |
| 9 | ja | weekly-report-w45-ja-core | Lucerna | VOL.2 | 文化の日と紅葉の週末 |
| 10 | ko | weekly-report-w45-ko-core | Lucerna | VOL.2 | 겨울이 오는 주간 — 단풍의 끝, 김장의 시작 |
| 11 | zh-cn | weekly-report-w45-zhcn-core | Lucerna | VOL.2 | 双11还在进行，冬天也要来了 |
| 12 | zh-tw | weekly-report-w45-zhtw-core | Lucerna | VOL.2 | 金融科技週開幕！香港迎四萬五千人 |

Excerpts are the same JSON `excerpt` fields (max 4 sentences each),
used verbatim on P2–P7. Verbatim items are NEVER converted between
scripts: the zh-tw item stays Traditional and the zh-cn item stays
Simplified throughout; explanations are native Korean. P8 VOLs:
FR VOL.3, all other 11 cores VOL.2.

## Layout (8 pages)
- P1: masthead `Lucerna` + olive COVER badge + week label
  (2026년 11월 2일~8일) + cover title `열두 개의 언어로 읽는 한 주`
  + 2-sentence generic framing intro (no new facts) + 12 headline
  teasers in fixed order (source-language code + Korean language name +
  verbatim headline).
- P2: EN, DE. P3: FR, ES. P4: IT, PT. P5: NL, RU. P6: JA, KO.
  P7: zh-cn, zh-tw. Each item: source-language tag, verbatim headline,
  verbatim excerpt, then a 1–2 sentence explanation in Korean
  (해요체) stating what happened + why it matters. Every explanation
  claim is traceable to that item's headline + excerpt only; no facts
  beyond the source article. Terms quoted in their original form
  (e.g. 에넴 for Enem, 쌍11) rather than transliterated away.
- P8: the week's 12 core papers at a glance, fixed order: per core,
  masthead + VOL + verbatim headline (same extracted material only,
  nothing invented).

## Build
- Build dir: `hidden_files/cover-w45-ko-build/` — `build.py`,
  `svglib.py` (COPIED from the W43-ko cover build dir, which copied
  it from the KO core build dir; no core content module was
  imported), `orphan_scan.py`, `svg/`, `png/` (eyeball renders).
- Fonts: Noto Serif/Sans CJK (KR face for measurement; SC face for
  zh-cn, TC for zh-tw, JP for ja headlines/excerpts so each script
  renders in its own variant).
- Cover-original text uses ASCII apostrophes only; no U+2019 occurs
  in any SVG (grep-verified).
- PDF built ONLY with:
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`
  (text-layer web PDF).

## Verification outputs
- Occlusion audit:
  `tools/venv/bin/python tools/occlusion_audit.py files/cover-w45-ko/svg`
  → selftest OK (all 6 planted classes fired), `svg: 0 flags`, exit 0.
- Orphan scan (`orphan_scan.py`, task definition: covers EVERY
  final-line text element — P1 teasers, P2–P7 headlines/excerpts/
  explanations, P8 headlines, plus P1 title/intro and P8 title/intro
  — trailing punctuation `[.!?…)\\]»」]` etc. stripped before
  measuring; flags a stripped final line of ≤3 chars or a final line
  starting with closing punctuation; all printed final lines also
  eyeballed for mid-word-split tails and line-start orphan
  punctuation):
  → `PROSE ORPHAN FLAGS: 0`, exit 0 (64 checks). Headline
  single-word finals (e.g. FR `joue`, IT `tavola`, NL `voetbal`)
  are headline wraps, not prose orphans, reported separately.
  Korean sentence-final verb endings on a final line (e.g.
  `결승전이에요.`, `행사가 열려요.`) are complete predicates, not
  stranded fragments, and were reviewed as such.
- Eyeball: all 8 pages rendered to PNG (CairoSVG, tools venv) and
  visually inspected — no overflow, no cut-off text, no overlapping
  elements, no tofu/missing glyphs; all 12 scripts render (Latin,
  Cyrillic, Japanese, Korean, Simplified + Traditional Chinese).
  P6 (JA+KO, short items) ends higher on the page (y≈1606) with
  empty space below — layout slack, not a defect.
- PDF text layer: `pdftotext` returns 10,269 bytes (non-empty).
  Whitespace-insensitive check: ALL 12 headlines AND ALL 12 excerpts
  extract from the PDF.
- VOL check: `VOL` occurs exactly 12 times in the PDF text, all on
  P8 (P8-only extraction: 12; P1–P7 extraction: 0); SVGs p1–p7
  contain zero `VOL` strings; P8 SVG contains exactly 12.
- Structure check: exactly 8 pages; fixed order EN DE FR ES IT PT NL
  RU JA KO zh-cn zh-tw; P2–P7 pairings as specified; P1 masthead
  `Lucerna` + COVER badge present; no own VOL on the cover.
- File: `cover-w45-ko.pdf`, 622,119 bytes (< 7 MB target), 8 pages,
  1462.5 × 2025 pts.
- Edition SVGs verified byte-identical to the build-dir SVGs
  (`diff -r` clean).

## Issues found + fixed
1. ZH-CN excerpt orphan (real defect): at 46 pt the zh-cn excerpt's
   final line was the lone character `日。` — caught by the orphan
   scan. Fixed by rendering the zh-cn excerpt only at 45 pt, which
   pulls the full clause (`...现货会一直卖到11月13日。`) onto the
   final line in 2 lines total. Excerpt text itself untouched
   (verbatim).
2. No other defects: occlusion audit clean on first run; no
   discrepancies between the JSON source and the core P1 SVGs;
   no U+2019; no VOL leakage off P8.

## Fix record — independent proofread problem 1 (P3 FR explanation orphan)
- Problem: at the standard 1650 pt wrap width, the FR explanation's
  final printed line was the single token `결승전이에요.` — a FAIL
  under the assigned Korean prose 1-token-final-line rule (the
  builder's ≤3-character scan does not catch it, since the token is
  longer than 3 characters).
- Fix — REFLOW ONLY, no rephrasing: in `build.py` (P2–P7 loop) the
  FR explanation block alone now wraps at 1600 pt instead of 1650 pt
  (`expl_w = 1600 if lang == "fr" else CW`), type size unchanged at
  46 pt. The explanation wording is verbatim — no word changed, no
  fact changed (Nov 7–8 weekend, three finals, Nov 8 Sunday Nanterre
  Rolex Paris Masters final all intact). The block still occupies
  4 lines, so P3 end y (2312.8) and every following element's
  position are unchanged; only the 4 FR explanation lines
  re-distribute. The zh-cn excerpt's 45 pt rendering is untouched
  (P7 SVG byte-identical to pre-fix).
- New final line (verbatim, 3 tokens): `파리 마스터스 결승전이에요.`
- Re-verification (post-fix):
  - 1-token-rule scan across ALL Korean prose paragraphs (12
    explanations + P1 title/intro/footnote + P8 title/intro, using
    the build's actual parameters incl. FR 1600 pt): 0 flags.
    Note: the legacy `orphan_scan.py` hard-codes 1650 pt for every
    explanation, so it still prints the old FR final line; it is
    not the authority for this rule — the 1-token scan above is.
    Legacy scan otherwise still reports `PROSE ORPHAN FLAGS: 0`.
  - Occlusion audit on the edition SVGs: selftest OK (all 6 planted
    classes fired), `svg: 0 flags`, exit 0.
  - Content-diff vs pre-fix set: ONLY `p3-cover.svg` differs
    (SHA-256 b190c07e… → a79feed2…); p1, p2, p4–p8 SVGs
    byte-identical. Edition SVGs verified byte-identical to the
    build-dir SVGs (`diff -r` clean).
  - PDF rebuilt ONLY via
    `tools/venv/bin/python tools/webpdf.py <edition-svg-dir> <edition-pdf-path>`:
    8 pages, 1462.5 × 2025 pts, 622,110 bytes (< 7 MB),
    SHA-256 c9ad3b3a940cd16a87576d857abd42ecf88e17aa69440574decacde8663477c0
    (pre-fix: 622,119 bytes,
    348fe99dda5cd864630f1f6f2006f25baf9ac9c7a70a14078bf1bd87ca1143bc),
    pdftotext 10,269 bytes (non-empty); whitespace-insensitive
    check: ALL 12 headlines AND ALL 12 excerpts extract; `VOL`
    occurs exactly 12 times. This record supersedes the `File:`
    byte/SHA line above.
