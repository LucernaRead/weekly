# Fix round — W45 DE×PT (proof REPORT.md, 2 blocking issues)

Scope: ONLY the 2 blocking issues + related KIT text. No Discord post, no
main-chat card/PDF dump, no cron, no weekly-git touch, no core/W43 change.
NOT finalized: per SOP §8.4 a render change requires a separate independent
full re-proofread; this round does not claim finalization.

## Stand-down check
- 90 s re-check before starting: zero new writes in
  files/weekly-report-w45-de-pt/ and hidden_files/weekly-report-w45-de-pt-build/,
  no running render process. Fresh mtimes were completed deliveries only.
- Pre-fix baseline hashes (8 SVG + 8 cards + 2 PDFs) saved in full in
  fix-baseline-hashes.txt in this dir before any re-render.

## Fix 1 — P7 NOCH EIN WORT word box (gate 1 freeze)
- Before (SVG text elements, x=1473): `«der Tankrabatt» (página 2): o imposto`
  / `reduzido sobre a gasolina e o diesel.` / `Desconto no combustível.`
- After: `«der Tankrabatt» (Seite 2): die`
  / `gesenkte Steuer auf Benzin und Diesel.` / `Desconto no combustível.`
- Geometry after: baselines y=1432.5 / 1461.61 / 1490.72 — identical to the
  old PT render AND to DE×EN / DE×IT. Ink (venv PIL): line 1 right 1772.0,
  line 2 right 1861.25 (23.8 px clear of the box right edge 1885),
  gloss ink bottom 1490.97, 17.0 px clear of the phrases rule at y=1508.
  P7 col3 ends still 1504.5.
- Source changes (both, to prevent regression):
  - transform.py C7 mapping: old core string (full-width paren form) now maps
    to `«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und
    Diesel. Desconto no combustível.` (was: PT-localized definition).
  - content7.py line 106: same string, verbatim.
- Freeze effect: P7 diff +61/-54 → +60/-53. `gesenkte Steuer auf Benzin und
  Diesel.` now appears in NEITHER the removed nor the added set (frozen,
  identical in core and edition). The only remaining Tankrabatt line-1 diff
  is paren form only: core `«der Tankrabatt»（Seite 2）: die` (full-width)
  vs edition `«der Tankrabatt» (Seite 2): die` (half-width) — the
  half-width form the brief prescribes, identical to DE×EN / DE×ES / DE×IT.

## Fix 2 — P8 answer note item 5 (gates 2/9 explanation-layer purity)
- Before (P8 SVG texts 186–187): `5. neun(9 matches on matchday 9)`.
- After (texts 186–187): `5. neun(9 jogos na 9ª rodada)`.
- Key unchanged (`neun`); stem unchanged (`Der 9. Spieltag hat ___ Spiele.`,
  P1, B1, Completar frases). New note matches the P1 Zahlen box
  parenthetical `(9 jogos na 9ª rodada)` verbatim.
- Source changes (both, to prevent regression):
  - transform.py C12 mapping: `第 9 轮共 9 场` now maps to
    `9 jogos na 9ª rodada` (was: `9 matches on matchday 9`, an English
    leftover from the DE×EN adaptation).
  - content12.py line 57 (item 5 registry note): same replacement.
  - No other `.py` source contained `matches on matchday` or the localized
    P7 string after the fix (grep-verified).

## Re-render (single process, tools venv)
- `tools/venv/bin/python run.py` exit 0, TOTAL 150, zero FLOW OVERFLOW /
  HEAD TOO WIDE warnings. Flow ends unchanged except P8 keys
  2369 → 2352 (shorter note, still within bottom 2560); P7 col3 1504.5.
- `tools/venv/bin/python render.py` (cairosvg) exit 0.
- Toolchain (re-verified this round): run.py and render.py both under
  tools/venv/bin/python — Python 3.12.3, PIL 13.0.0; render.py additionally
  cairosvg 2.9.1 (system python3 lacks cairosvg; venv mandatory).

## Change-scope verification (fix-baseline vs fix-after hashes)
- CHANGED, exactly as expected: svg/p7-sprache.svg, svg/p8-uebungen.svg,
  cards/p7-sprache.png, cards/p8-uebungen.png, both PDFs.
- UNCHANGED byte-for-byte: svg p1–p6, cards p1–p6. No unrelated changes.
- New edition SVG hashes: p7
  171e37ce40f4a697068cbfad4129037c31cb2abd4c196fc39f174d3c56f18089,
  p8 e79f51f4de864d8f496a78f3f4f4ac86bc81338b8b966abb1ae0a8e8904bfc37
  (full post-fix set in fix-after-hashes.txt / svg-hashes.txt).
- Core SVGs re-verified: all 8 hashes identical to core-hashes-before.txt
  (KIT §2 "before" values) — core untouched.

## Gates re-run (all outputs saved as fix-* in this dir)
- freeze diff (tools/freeze.py diff): P1 +24/-23, P2 +36/-32, P3 +40/-40,
  P4 +25/-22, P5 +42/-39, P6 +37/-33, P7 +60/-53, P8 +160/-141;
  added CJK = 0 on all 8 pages, TOTAL added CJK characters 0.
- p8 compare (explicit SVG paths): CLEAN, core 150 noted = edition 150
  noted, missing=[], extra=0, keydiff=[137, 138, 139, 150] (unchanged).
- occlusion audit (selftest OK, all 6 classes fired): edition 0 flags,
  core 0 flags, NEW vs core 0.
- rowcheck: same-baseline collisions 1 — the known P1 sommaire S.3
  `&amp;` measurement pseudo-hit (ink 1804.5 vs tag 1799.7), already
  adjudicated in the proof report as a core-inherited artifact with a
  real ~43 px gap on the card; unchanged by this round.
- chartcheck: chart-band text-vs-later-rect overlaps 0.
- gloss (source-grep method, split on `·`): 5 calls, 25 items = core 25.
- P7 golden sentences: all 8 German quotes exactly 2× in rendered text.
- P7 right rail: gloss ink bottom 1490.97, 17.0 px above the y=1508 rule.
- English-residue rescan, all 8 pages (expanded list: matches on matchday,
  matchday, care home, "This week's big questions",
  "Germany's five hot questions", goes to the end, leftover, matches,
  This week, the match): 0 hits. Also CJK 0, full-width parens 0,
  full-width ｜/。 0, …… 0, 桥接 0, Le/The Lucerna 0, VOL.1 0.
- Registry dump re-run (dump_reg.py): TOTAL 150, continuous 1–150,
  per-page 10/18/18/18/18/18/12/38, levels A2 66 / B1 70 / B2 14,
  item 5 = {key: neun, note: 9 jogos na 9ª rodada}; SVGs/cards/PDFs
  hash-verified UNCHANGED by the dump run.
- PDFs (venv pypdf): print Die-Lucerna-VOL2-PT.pdf — 8 pages,
  1462.5×2025 pt, 4,144,470 bytes, sha256
  313ff7635f3cde5bcef10c08119bdec1d89c7c531d6280bd433f6c7eecd748d2;
  web Die-Lucerna-VOL2-PT-web.pdf — 8 pages, 1400×1938 pt,
  4,167,866 bytes (< 10 MB), sha256
  58e7294ca04d4f722cf5664038ac73f31f352de241ab1ba04d8f98cbeac04f42.
- Cards: 8 PNG, all 1950×2700, all 8 viewed end to end after the fix;
  no defect found (P7 word box and P8 answer area specifically confirmed).

## KIT updates made with this round
- Status header → fix round complete, still NOT finalized, awaiting
  independent full re-proofread (SOP §8.4).
- §1(c): false "as in DE×EN" claim replaced by the fix-round restoration
  record (German sentence restored verbatim, PT gloss kept).
- §2: edition SVG hashes for p7/p8 updated to post-fix values.
- §10: PDF sizes/SHAs updated to post-fix values; residue-scan assertion
  corrected (pre-fix 1 hit at P8 item 5, fixed; post-fix rescan 0 hits);
  cards re-viewed note updated.
- §12: this fix round appended as item 9.
- Note on section numbering: in this KIT the PDF/SVG pins live in §2
  (edition SVG hashes) and §10 (PDFs/cards), not §11 (§11 is terseness
  decisions); both pin locations were updated.
