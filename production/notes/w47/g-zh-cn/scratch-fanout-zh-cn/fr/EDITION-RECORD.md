# EDITION-RECORD — 2026-w47-zh-cn-fr (French explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Builder handoff, NOT a
finalisation claim: independent proofreading is still owed by the parent
line. No commit, no push, no insert, no lint run by this builder.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-FR.pdf` (print) | 42,504,783 | `f00a276e9d3366f6220df0acfc7e3f7b5573209f349d8fb380dc7a42252027f4` |
| `Lucerna-VOL4-FR-web.pdf` (web) | 2,663,754 | `b7e43796dbe39674e42910eb37c56b20e45bd223e797bb3999560ee8d516845c` |
| `2026-w47-zh-cn-fr.text.md` | 51,829 | `fb72ed2964225edb7f51599047012d0501499f41cb80543ec67d01753473080b` |
| `ABSTRACT.txt` | 332 | matches `tables.py` ABSTRACT['fr'] |

## Fixes applied in #3 (all in the table first, then the edition files)

First `run.py` (run-fr.log): RC=0 TOTAL 150, but 4 defects — 3 HEAD TOO
WIDE (P4-ex, P5-ex, P8-ex) + FLOW OVERFLOW [P8-keys] ending 2604.2.

1. Heads (sizes are the core's: P4/P5 @25, P8 @24 — the first measurement
   at size 30 overstated the overflow): P4 “Travail sur le calendrier”
   (429.5) → “Lire le calendrier” (348.5); P5 “Heures et nombres” (423.8)
   → “Heures, nombres” (401.5); P8 “Lire et répondre” (422.7) → “Lire &
   répondre” (416.7).
2. P8 notes (8 values → 2-line to 1-line, `p8sim.py` what-if verified
   before applying): Q11, Q15+Q92 (shared note), Q20, Q24, Q56, Q109,
   Q121 (harvested entry), Q149 (harvested entry). Keys 2604.2 → 2537.2.
   Table diff = exactly the 11 changed fr lines.
3. P4 gloss (found by gates, not by run): Notes box wrapped to 7 lines,
   bottom 821.9 covering “GEN，” (occlusion flagged 93%). Dropped
   “, les demi-finalistes” → 6 lines, box bottom 792.2.
4. P2 calendar title (found by gates): “Les dates de la semaine” reached
   16.7 px into the valley photo → “Dates de la semaine”, ends x=1414.9.
5. P2 word card (found by eye in the visual pass): 价保 example
   2 lines, 2nd line 8.76 px below the fixed 150 px card bottom →
   “pas automatique : demande-le toi-même”, 1 line, inside the card.
   No gate covers fixed-height card overflow (tool gap — see KIT).

`WEEKLY-KIT.md` rewritten for fr (was an untranslated copy of the core
KIT, pairing zh-cn × en).

## Gates (final files)

`gates-zhcn.py` (`gates-fr-3.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 395/395 … P8 1897/1897) |
| pdftotext_nonempty | print 45,551 B, web 45,551 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75) |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

Plus: `run.py` RC=0 TOTAL 150 (A2 56 / B1 69 / B2 25; pages
10/18/18/18/18/18/12/38), 0 overflow; `freeze.py baseline` core 8/8
byte-identical (venv Pillow 13.0.0 / FreeType 2.14.3, core integrity
confirmed); `freeze.py diff --strict-cjk` TOTAL added CJK **0**, exit 0
(`freeze-diff-fr-2.log`); leak scan over all 275 translate sources vs
final SVG + text.md: **0 real leaks** (`leak-fr-2.log` — “体育　Sport”
is a covered entry whose French rendering is identically “Sport”; the
welcome line is the documented EXCLUDE; “Notes｜”, “文化　Culture”,
“悬疑 = suspense, b” are IDENTICAL renderings, not leaks).

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (`p8-extract-fr.json`).
- `p8.py compare` core vs edition: **CLEAN**, missing=[], extra=[],
  uncertain=[], keydiff=[] (`p8compare-fr.json`). Keys 137–140
  (7.77 / 14 / GEN / 冷) print identically to the core by design; E-group
  keys are the option letters with French notes.
- Registry: `run.py` TOTAL 150, same level/page/type split as the core.

## Visual

- P1: badge Latin-only on the masthead rule; press-time line visible.
  PASS.
- P2: “Dates de la semaine” fully visible, 24.6 px clear of the valley
  photo; all 4 word cards inside their boxes (价保 1 line);
  “Exemple d'exercice　练习例子” fits. PASS.
- P4: Notes box 6 lines, bottom clear of “GEN，” below; C head “Lire le
  calendrier”. PASS.
- P5: C head “Heures, nombres”. PASS.
- P7: teaser band ends 2588.78, clear of footer. PASS.
- P8: D head “Lire & répondre”; test sections A–F (113–150), keys with
  “— Page N —” separators, photo + credit, footer clear. PASS.
- P3/P6: unchanged since the transform (no fr change touches them).

## Logs (this dir)

`run-fr-4.log`, `render-fr-4.log`, `webpdf-fr-4.log`, `gates-fr-3.log`,
`gates-fr.json`, `freeze-diff-fr-2.log`, `freeze-diff-fr-2.json`,
`leak-fr-2.log`, `p8-extract-fr.json`, `p8compare-fr.json`,
`measure` output in `run-fr-4.log`. Earlier runs retained
(`run-fr-2.log`, `run-fr-3.log`, `gates-fr.log`, `gates-fr-2.log`,
`freeze-diff-fr.log`, `leak-fr.log`, `p8sim-fr.log`).
