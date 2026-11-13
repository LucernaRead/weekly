# EDITION-RECORD — 2026-w47-zh-cn-nl (Dutch explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Builder handoff, NOT a
finalisation claim: independent proofreading is still owed by the parent
line. No commit, no push, no insert, no lint run by this builder.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-NL.pdf` (print) | 44,049,080 | `f660072c047e1b5bab5a13956ec871db6976a47ddff49cc855615a8f55b42e4b` |
| `Lucerna-VOL4-NL-web.pdf` (web) | 2,703,048 | `495594dc8d712268b336c6bcfb39dc0286f45ce20624cb163d02e9f5e9aeefac` |
| `2026-w47-zh-cn-nl.text.md` | 50,082 | `41aa9a39371ab7dc75f828b24bb038f0f1b4f6e2f1a1fbe04cd9513eff09df2c` |
| `ABSTRACT.txt` | 316 | matches `tables.py` ABSTRACT['nl'] + newline |

## Fixes applied in #3 (2026-11-11)

First `run.py`: RC=0 TOTAL 150 with 2 HEAD TOO WIDE + 4 P8-keys overflows
+ P7 teaser at 2641.82 (worst of the week). All 12 fixes went into the
table sources (`fresh.py` / `harvested.json` — the error-clinic note and
the Q14/Q87 note live in `harvested.json` — / `gen_tables.py` f-string)
AND the edition files; `gen_tables.py` re-run: 276 ENTRIES, 0 missing,
0 extra, 0 unconsumed; table diff = exactly the 12 changed nl lines.

1. P4 C-head: “Werken met het programma” → “Lees het programma”
   (394.2 px at 25 pt).
2. P8 D-head: “Lezen en antwoorden” (442.6 px at 24 pt) → “Lees,
   antwoord” (415.6 px).
3. P2 calendar title: “De data van deze week” (ends x = 1446.6, 7.1 px
   into the valley photo) → “Data van deze week” (ends x = 1413.2).
4. P7 letters-box note: dropped “in VOL.4” (“VOL.3 beloofde echte
   brieven in VOL.4; …” → “VOL.3 beloofde echte brieven; …”), 7 → 6
   lines (−29 px).
5. P7 error-clinic row 3 note: “Volgorde: getal + telwoord +
   zelfstandig naamwoord.” → “Volgorde: getal + telwoord + naamwoord.”
   (2 → 1 line, −26.52 px). Teaser 2641.82 → 2586.30. Root cause: the
   four Dutch error-clinic notes all wrap to 2 lines, so the col-3
   error box is taller than in every other edition; the
   pattern/structure/letters boxes are the same height everywhere
   (stack 659.5).
6. P8 notes 2L→1L (7): Q14/Q87 (shared note) “Open het pakket en
   controleer het vóór de ontvangst.”; Q18 “shēnqǐng —
   prijsbescherming niet vanzelf; vraag hem aan.”; Q20 “Hunan SF
   Express: +20 % personeel en capaciteit.”; Q68 “《白衣逆行者》 vóór
   de première van 6 nov. teruggetrokken.”; Q95 “Eén balk: totaal 22
   dagen; de andere: dagpiek.”; Q118 “《试探》 in première op 21 nov.
   2026; een nieuwe film.” Keys 2604.2 → 2491.1 (= core). Q150 f-string
   shortened too (“Open opdracht — modelantwoord hierboven, sectie F
   (138 tekens).”) but stayed 2L; not needed.
7. Proactively measured, no fix needed: P4 gloss 6 lines under
   “Notities｜”; all 4 P2 word-card examples 1L at 19 pt.
8. `WEEKLY-KIT.md` rewritten for nl (was an untranslated copy of the
   core KIT, pairing zh-cn × en).

## Gates (final files)

`gates-zhcn.py` (`gates-nl.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 382, P2 365, P3 280, P4 348, P5 285, P6 347, P7 519, P8 1796) |
| pdftotext_nonempty | print 44,234 B, web 44,234 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75), spans 370 |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

Plus: `run.py` RC=0 TOTAL 150 (A2 56 / B1 69 / B2 25; pages
10/18/18/18/18/18/12/38), 0 overflow; P7 teaser ends 2586.3; P8 keys
end 2491.1; `freeze.py baseline` core 8/8 byte-identical (venv Pillow
13.0.0 / FreeType 2.14.3, core integrity confirmed); `freeze.py diff
--strict-cjk` TOTAL added CJK **0**, exit 0 (`freeze-diff-nl.log`);
leak scan over all 275 translate sources vs final SVG + text.md:
**0 real leaks** (`leak-nl.log` — IDENTICAL only: “体育　Sport”);
phrases of the week all 8 exactly 2×.

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (gates log `p8_extract`).
- `p8.py compare` core vs edition: **CLEAN**, keydiffs 0 (gates log
  `p8_compare`).
- Registry: `run.py` TOTAL 150, same level/page/type split as the core.

## Visual

- P1: badge Latin-only on the masthead rule; press-time line visible.
  PASS.
- P2: calendar title “Data van deze week” fully visible, clear of the
  valley photo; all 4 word cards inside their boxes, examples 1 line.
  PASS.
- P4: Notities box 6 lines, bottom clear of “GEN，” below; C head “Lees
  het programma” fits. PASS.
- P5: C head “Tijden en getallen” fits. PASS.
- P7: error-clinic row 3 shortened; teaser band ends 2586.3, clear of
  footer. PASS.
- P8: D head “Lees, antwoord” fits; test sections A–F, keys 1–150 +
  footer clear. PASS.
- P3/P6: unchanged since transform.

## Logs (this dir)

`transform-nl.log`, `run-nl.log`, `run-nl-2.log`, `p8sim-nl.log`,
`render-nl.log`, `webpdf-nl.log`, `gates-nl.log`, `freeze-diff-nl.log`,
`leak-nl.log`, `vis-nl-p1/p2/p4/p5/p7/p8.png`.
