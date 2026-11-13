# GATE-LOG — 2026-W47 it-en, independent re-proof after re-fan-out 2 (core D-2 fix)

- Proofer: independent re-proof (SOP §8.4); scratch
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-en/`
- Date: 2026-11-11 UTC. Interpreter: `~/workspace/weekly-git/tools/venv/bin/python`
  (Pillow 13.0.0). `TMPDIR=<scratch>/tmp`; `PYTHONDONTWRITEBYTECODE=1` throughout.
- Probe (before work): `git -C ~/workspace/weekly-git hash-object -w /dev/null` →
  `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`, RC=0 (`probe.txt`); real file write
  in scratch OK.
- Identity (start and end of round, identical): print `La-Lucerna-VOL4-EN.pdf`
  14,032,910 B `b0444f8a89fcd1df53941dd0e3774777f17cd238fc0f93fd519c8c680c468b17` /
  web `La-Lucerna-VOL4-EN-web.pdf` 1,291,136 B
  `b99776c00ae69f7b0b93264769677d9bd536bcd2993c8225c092b4614581e227` / text
  `2026-w47-it-en.text.md` 55,183 B
  `ad311b5bf59ae9eafc996834abba95d1f4bd899874043c605735d57cbbd7f917`.

## 1. Gates suite (my own run of the fan-out gates, repointed at my scratch)

`gates.py en` → **20 PASS, 0 FAIL ("GATES ALL PASS")** — log `gates-en.log`:

| # | gate | result |
|---|---|---|
| 1 | occlusion 0 flags | PASS — `…/it-en/svg: 0 flags` |
| 2 | p8 extract noted count | PASS — noted=150 rc=0 |
| 3 | p8 compare vs core | PASS — verdict=CLEAN keydiffs=[137, 138, 139] |
| 4 | freeze diff fragments explained by translations/furniture (P1–7) | PASS — unexplained_add=[] unexplained_rem=[] |
| 5 | freeze diff report present | PASS — pages=['1'..'8'] |
| 6 | freeze strict-cjk (no added CJK except U+3000) | PASS — rc=1 (tool exit code on the U+3000-only report), added_cjk={'\\u3000': 13} non_space={} |
| 7 | print/web text multiset identical | PASS — print_words=7928 web_words=7928 chars_equal=True word_diff=[] |
| 8 | web PDF < 7MB | PASS — 1,291,136 bytes |
| 9 | print PDF size sane | PASS — 14,032,910 bytes |
| 10 | P8 min font >= 13px (9.75pt) | PASS — min=13.0 |
| 11 | paper #fbfaf6 present | PASS |
| 12 | no gold/brick/near-black | PASS — hits=[] |
| 13 | no VOL.5 in furniture (only preview/disclosure) | PASS — VOL.5 text nodes=3 |
| 14 | VOL.4 present | PASS — count=9 |
| 15 | badge colours A2/B1/B2 | PASS |
| 16 | no double outer frame | PASS — full-page rects=0 |
| 17 | textmd validate | PASS — forward-miss: 0 reverse-miss: 0 |
| 18 | answers count 150 | PASS — edition=150 core=150 |
| 19 | keys 1–150 match core (except 137–139 re-aimed, writing) | PASS — mismatches=[] |
| 20 | notes match translations.py (except 137–140 + writing) | PASS — mismatches=[] table_gaps=[] |
| — | INFO '·' total occurrences in SVGs: 149 (core had them only in options/gloss lists) | info only |

## 2. D-2 regression (my own checks; see PROOF-NOTE §A for the table)

- `text.md:775/:777` new strings ×1 each; diff vs
  `scratch-refanout-it2/backup/2026-w47-it-en/2026-w47-it-en.text.md` = exactly
  lines 775/777; byte delta −21 (55,204 → 55,183).
- Old strings `Le forme sono regolari: andare` and `irregolare al futuro: leggerò`
  = 0 in text.md, content7.py, p7 SVG, and both PDF P7 text layers.
- New strings ×1 each in p7 SVG (tag-stripped) and in both PDFs' P7 text layers
  (L17 arrow-normalised: the layer glues `→` to its neighbours).
- Edition `content7.py:17/:18` byte-identical to core-it `content7.py:17/:18`.
- SVG/cards diff vs backup: only p7 differs; content diff: only `content7.py`
  lines 17–18.
- Semantic check: FlexiClasses (leggere regular / andare irregular andrò),
  LibreTexts *Indicativo futuro* (leggere regular example; andare → andr- irregular
  stem), FluentU (andare andrò irregular) — labels now correct.

## 3. fix1 regression (triple measurement; log `verify-triple.log`)

| item | ① PIL ink | ② render pixels (96 dpi, delivered print PDF) | ③ text-layer bbox (print / web) |
|---|---|---|---|
| D-1 `LA SETTIMANA IN CIFRE　FIGURES` | +17.0 px (556.5..944.0 vs 538.5..961.0) | +19 px (x=942 vs 961) | +16.9 / +16.9 px |
| D-2 `LA FRASE PER RICORDARE　LEARN` | +13.8 px (556.5..947.2 vs 961.0) | +16 px (x=945 vs 961) | +12.4 / +12.4 px |
| D-3 `ERRORI TIPICI　TYPICAL ERRORS` | +26.8 px (1461.5..1835.2 vs 1439.5..1862.0) | +28 px (x=1834 vs 1862) | +25.9 / +25.9 px |

All ≥ +5 px on all methods. Old strings 0× everywhere; new titles 1× each in
text.md:45/:205/:825. 2× crops viewed: `pages/crop-p1-cifre.png`,
`pages/crop-p2-frase.png`, `pages/crop-p7-errori.png`, `pages/crop-p7-a2.png`.
Method note: method-② differs from fix1's +20/+29 by 1 px on D-1/D-3
(dark-pixel band bounds, ±1 px variance); all other cells reproduce exactly.

## 4. Freeze (canonical tool — TRUE core build, NOT self-comparison)

- `tools/freeze.py baseline --build production/2026-w47/core-it --core-svg
  production/2026-w47/core-it/svg --out <scratch>/freeze-baseline` → RC=0,
  **8/8 SVGs byte-identical** (log `freeze-baseline.log`):
  p1 `d301b886…`, p2 `a744e5d2…`, p3 `fe0a0e65…`, p4 `12ddd86c…`, p5 `08929554…`,
  p6 `621054ee…`, p7 `a7e6afa4…` (= D-2 fix log's stated new core p7 hash),
  p8 `779aa98c…`. The `--core-svg` points at **core-it's own `svg/`** and the
  `--build` copies **core-it itself**, so the build-copy is core-it, not the
  edition posing as core. Core integrity: shipped core SVGs unchanged by the run
  (8 files re-hashed).
- `tools/freeze.py diff --core-svg core-it/svg --edition-svg it-en/svg --json
  en/freeze-diff.json` → RC=0; TOTAL added CJK characters: **13** (all U+3000,
  furniture separators, exempt); per-page added CJK: p2–p6 ×2, p7 ×1, p8 ×1
  (log `freeze-diff.log`).
- Rebuild check: edition copied to `<scratch>/rerun/`, OUT/BASE repointed in the
  COPIES only (verified zero `weekly-git/production` strings left), `run.py` RC=0
  TOTAL 150 (A2 47 / B1 70 / B2 33; pages 10/18/18/18/18/18/12/38) → rebuilt SVGs
  **8/8 byte-identical** to the shipped SVGs (log `rerun.log`).

## 5. Occlusion audit + print re-render + text layers

- `tools/occlusion_audit.py --selftest` → OK: planted classes fired
  {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX: 1 each}; clean controls silent
  (log `occlusion-selftest.log`).
- `tools/occlusion_audit.py production/2026-w47/2026-w47-it-en/svg` → **0 flags**
  (log `occlusion.log`).
- Print PDF re-render from the shipped SVGs (`rerender.py`, CairoSVG + pypdf) →
  **BYTE-IDENTICAL** to the delivered print PDF (14,032,910 B,
  `b0444f8a…468b17`; log `rerender.log`).
- `pdftotext` print vs web: 45,129 bytes each, `cmp` identical (files
  `print.txt`, `web.txt`); word count 7,928 each.

## 6. Cream-box / STRADDLE sweep (29 rects, backup comparison)

- `cream_spill_orphan.py` on the edition: 29 cream rects, **0 CREAM-X, 0 CREAM-Y,
  0 SPILL-PAGE, 0 SPILL-FOOTER**; 3 ORPHAN flags only (log `cream-scan.log`).
- Same script on the pre-refanout backup (`cream_backup.py`,
  `cream-scan-backup.log`): identical output except P7 text-node count 157 vs 161
  (the D-2 shortening) — no overflow regression.
- STRADDLE per-title ink table (`straddle.py`, `straddle-titles.log`, 213 nodes
  starting inside cream boxes, current vs backup): title-set diffs NONE;
  ink-box diffs among shared titles NONE; zero nodes with ink beyond the right
  box edge. Tightest title: P1 `IN QUESTO NUMERO　CONTENTS` PIL spare +7.2 px
  (render pixels +6 px) — inside, above the +5 floor, unchanged from backup
  (PROOF-NOTE O-13).
- The 3 orphans are byte-identical nodes (same text, x, y, font) in core-it:
  P6 "18." (1603.5, 641.6), P8 "due" (538.5, 818.975), P8 Q137 "___"
  (773.3, 1187.825). Frozen Italian wraps, inherited — not defects (O-10).

## 7. p8 extract + compare (standalone runs)

- `tools/p8.py extract --p8 …/svg/p8-valutazione.svg --total 150 --json
  en/p8-extract.json` → noted set = 150 of 150 (log `p8-extract.log`).
- `tools/p8.py compare --core-p8 core-it/svg/p8-valutazione.svg --edition-p8
  …/svg/p8-valutazione.svg --total 150 --json en/p8-compare.json` →
  **status: CLEAN**, missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139]
  (log `p8-compare.log`, json `en/p8-compare.json`). Keydiff is the expected
  re-aim: Q137–139 keys are the English translations in this edition vs the
  Italian sentences in the core; Q140's key is the Italian sentence in both.
- Three-source key audit (my own script, inline stems vs RISPOSTE vs P8 printed
  keys): 149/149 agree + Q150 open writing task; match-word letters
  25–28/52–55/141–144 all agree; RISPOSTE-vs-P8: 0 mismatches.

## 8. Visual inspection (200 dpi renders of the DELIVERED print PDF)

Rendered with PyMuPDF at 200 dpi into `pages/p200-1.png` … `pages/p200-8.png`
(plus 96 dpi `pages/p-1.png` … `pages/p-8.png` for the pixel scans and
`pages/web-p1.png` / `pages/web-p8.png` for the web PDF). All 8 pages viewed:
no overflow, no overlap, no clipped glyph, no tofu, no footer intrusion.
P7 A2 crop viewed: both D-2 sentences render cleanly; Q101–104 intact.
Web P1/P8 viewed: identical to print.

## 9. Content checks (from the full 1317-line read)

- 150 exercises, keys 1–150 continuous, no gaps/duplicates; levels A2 47 /
  B1 70 / B2 33; model text 99 words (80–100).
- 8 golden sentences verbatim in articles and on P7 FRASI with correct page refs.
- NOTE-box headwords: 29/29 occur in their articles.
- Arithmetic: MD11 goals 24 in 10 matches; Q85 13−11=2; Q86 6+7=13; chart
  Torino 5° / Napoli 13° extremes match bars.
- Dates/weekdays verified with `TZ=Europe/Rome date` for Nov 6/7/8/9/12/15/16/17/
  19/20/21/22/23/24, Dec 2/6/31, Oct 15/28, Oct 25 1441 — all match the paper.
- Banned terms 0; U+2019 0 in all 8 SVGs and text.md; CJK ideographs 0 in text.md
  (106 × U+3000, 14 × U+FF1A furniture/fullwidth colons).
- P8 min font 13.0 SVG px = 9.75 pt (SOP §1.1 floor, exact).
- KIT verified by grep: §7 new triple SHAs; §12 fix1 SHAs retained; §13
  re-fan-out 2 SHAs with pre-refanout SHAs as "was".
- ABSTRACT.txt: one line, English, no ASCII double quotes, facts match.

## 10. Production integrity

- No production file written by me. Edition SVGs re-hashed after all work:
  8/8 identical to pre-work hashes (only the path prefix differs between the
  two hash files, `prod-svg.sha256` vs `svg-sha-after.txt`). Three delivered SHAs
  re-verified at the end of the round. No commit, no push.
- Tool limitation recorded: `freeze.py diff` and `p8.py compare` cannot see
  pure-Latin text drift (both blind to the D-2 change); D-2 verification rests on
  the text-layer checks, text.md diff and freeze baseline SVG byte comparison.
