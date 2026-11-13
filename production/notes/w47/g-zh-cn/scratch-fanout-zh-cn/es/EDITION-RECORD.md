# EDITION-RECORD — 2026-w47-zh-cn-es (Spanish explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Builder handoff, NOT a
finalisation claim: independent proofreading is still owed by the parent
line. No commit, no push, no insert, no lint run by this builder.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-ES.pdf` (print) | 44,799,104 | `f05d6126a7f55564787be64e370de7ce05ade6abb38b18fbecc9cb2d070a2508` |
| `Lucerna-VOL4-ES-web.pdf` (web) | 2,723,559 | `249ee578617c1c584f11ef2436d2438a41cf8c8b10b3e24baf3ff45b8396d437` |
| `2026-w47-zh-cn-es.text.md` | 51,175 | `edc045da1f0cc5267ec18046a193e055dfbf90e70421d79bcf0ba93f2497f482` |
| `ABSTRACT.txt` | 335 | matches `tables.py` ABSTRACT['es'] |

## Fixes applied in #3 (all in the table first, then the edition files)

First `run.py` (run-es.log): RC=0 TOTAL 150, but 4 defects — 2 HEAD TOO
WIDE (P4-ex, P8-ex) + FLOW OVERFLOW [P8-keys] ending 2604.2 + P7 teaser
ending 2617.78, pressing the footer rule (2596).

1. Heads: P4 “Trabajo con el calendario” (449.2 @25) → “Leer el
   calendario” (360.3); P8 “Leer y responder” (431.4 @24) → “Leer,
   responder” (417.8 — the “&” form measured wider, 435.4, so the comma
   form was used). P5 “Horas y números” fits as-is (398.0 @25).
2. P7 teaser: letters-box note (lcn) wrapped to 7 lines, pushing the
   col-3 stack ~29 px taller than the core. Dropped the redundant
   “en VOL.4” (“VOL.3 prometió cartas reales en VOL.4; …” → “VOL.3
   prometió cartas reales; …”; the Chinese half already says 本期).
   Note now 6 lines; teaser 2617.78 → 2588.78. No layout change.
3. P4 gloss: dropped “, los semifinalistas” (7 lines → 6; the 7-line
   box would have covered “GEN，” — the fr edition hit the same defect
   class, occlusion-flagged at 93%).
4. P2 calendar title: “Las fechas de la semana” (454.5 px, 22 px into
   the valley photo) → “Fechas de la semana”, ends x=1422.7.
5. P8 notes (7 values → 2-line to 1-line, `p8sim.py` what-if verified
   before applying): Q13, Q17 (kept the advice, “pronto” → “ya”), Q18,
   Q20, Q24, Q109, Q150. Q150 is an f-string in `gen_tables.py`, not a
   table entry — fixed in the generator and in `content8.py:102`.
   Keys 2604.2 → 2475.7. Table diff = exactly the 12 changed es lines.
6. P2 word cards: measured before the gates — all 4 example sentences
   1 line; no fix needed (fr's equivalent card overflowed).

`WEEKLY-KIT.md` rewritten for es (was an untranslated copy of the core
KIT, pairing zh-cn × en).

## Gates (final files)

`gates-zhcn.py` (`gates-es.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 390/390 … P8 1895/1895) |
| pdftotext_nonempty | print 45,062 B, web 45,062 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75) |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

Plus: `run.py` RC=0 TOTAL 150 (A2 56 / B1 69 / B2 25; pages
10/18/18/18/18/18/12/38), 0 overflow; `freeze.py baseline` core 8/8
byte-identical (venv Pillow 13.0.0 / FreeType 2.14.3, core integrity
confirmed); `freeze.py diff --strict-cjk` TOTAL added CJK **0**, exit 0
(`freeze-diff-es.log`); leak scan over all 275 translate sources vs
final SVG + text.md: **0 real leaks** (`leak-es.log` — only hit is the
IDENTICAL rendering “悬疑 = suspense, b”).

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (`p8-extract-es.json`).
- `p8.py compare` core vs edition: **CLEAN**, missing=[], extra=[],
  uncertain=[], keydiff=[] (`p8compare-es.json`). Keys 137–140
  (7.77 / 14 / GEN / 冷) print identically to the core by design; E-group
  keys are the option letters with Spanish notes.
- Registry: `run.py` TOTAL 150, same level/page/type split as the core.

## Visual

- P1: badge Latin-only on the masthead rule; press-time line visible.
  PASS.
- P2: “Fechas de la semana” fully visible, 16.8 px clear of the valley
  photo; all 4 word cards inside their boxes;
  “Ejemplo de práctica　练习例子” fits. PASS.
- P4: Notas box 6 lines, bottom clear of “GEN，” below; C head “Leer el
  calendario”. PASS.
- P5: C head “Horas y números”. PASS.
- P7: teaser band ends 2588.78, clear of footer. PASS.
- P8: D head “Leer, responder”; test sections A–F (113–150), keys with
  “— Página N —” separators, photo + credit, footer clear. PASS.
- P3/P6: unchanged since the transform (no es change touches them).

## Logs (this dir)

`run-es-2.log`, `render-es.log`, `webpdf-es.log`, `gates-es.log`,
`gates-es.json`, `freeze-diff-es.log`, `freeze-diff-es.json`,
`leak-es.log`, `p8-extract-es.json`, `p8compare-es.json`. Earlier run
retained (`run-es.log`).
