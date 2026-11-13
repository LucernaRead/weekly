# EDITION-RECORD — 2026-w47-zh-cn-pt (Portuguese explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Builder handoff, NOT a
finalisation claim: independent proofreading is still owed by the parent
line. No commit, no push, no insert, no lint run by this builder.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-PT.pdf` (print) | 41,734,759 | `2286485f2608d2a144d37e9451f7a1945313e54e1f6ba1b540aec1ab5484859c` |
| `Lucerna-VOL4-PT-web.pdf` (web) | 2,647,093 | `030f52fb82087f8fe13f3465b74ee61b8c02b6e7d8a4740280ff7fa66cac76fa` |
| `2026-w47-zh-cn-pt.text.md` | 50,846 | `9207974bed3d5d16c4312752ad22a4219f0033e33d9264c29c07adfe3d44cb71` |
| `ABSTRACT.txt` | 331 | matches `tables.py` ABSTRACT['pt'] + newline |

## Fixes applied in #3 (2026-11-11)

First `run.py`: RC=0 TOTAL 150 with 2 HEAD TOO WIDE + 1 P7-teaser overflow.
All 4 fixes went into the table sources (`fresh.py`) AND the edition
files; `gen_tables.py` re-run: 276 ENTRIES, 0 missing, 0 extra,
0 unconsumed; table diff = exactly the 4 changed pt lines.

1. P4 C-head: “Trabalho com o calendário” (466.8 px at 25 pt) → “Ler o
   calendário” (339.0 px).
2. P7 A2-head: “Final e encomendas” (431.1 px at 24 pt) → “Final e
   pacotes” (371.9 px). B1 “Hora e datas” (345.3 px) and B2 “Ler as
   notícias” (318.5 px) fit as-is.
3. P7 letters-box note: dropped the redundant “em VOL.4” (“VOL.3
   prometeu cartas reais em VOL.4; nenhuma chegou até 10 nov.” →
   “VOL.3 prometeu cartas reais; nenhuma chegou até 10 nov.”), 7 lines
   → 6; teaser 2617.78 → 2588.78.
4. P2 calendar title: “As datas desta semana” (ends x = 1446.0, 6.5 px
   into the valley photo) → “Datas desta semana” (ends x = 1415.8).
5. Proactively measured, no fix needed: P4 gloss 6 lines under “Notas｜”;
   all 4 P2 word-card examples 1L at 19 pt; P8 keys end 2552.7 as built
   (7 two-line notes left alone).
6. `WEEKLY-KIT.md` rewritten for pt (was an untranslated copy of the
   core KIT, pairing zh-cn × en).

## Gates (final files)

`gates-zhcn.py` (`gates-pt.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 386, P2 366, P3 282, P4 358, P5 285, P6 352, P7 532, P8 1879) |
| pdftotext_nonempty | print 44,820 B, web 44,820 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75), spans 371 |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

Plus: `run.py` RC=0 TOTAL 150 (A2 56 / B1 69 / B2 25; pages
10/18/18/18/18/18/12/38), 0 overflow; P7 teaser ends 2588.78; P8 keys
end 2552.7; `freeze.py baseline` core 8/8 byte-identical (venv Pillow
13.0.0 / FreeType 2.14.3, core integrity confirmed); `freeze.py diff
--strict-cjk` TOTAL added CJK **0**, exit 0 (`freeze-diff-pt.log`);
leak scan over all 275 translate sources vs final SVG + text.md:
**0 real leaks** (`leak-pt.log` — IDENTICAL only: “悬疑 = suspense,
b”); phrases of the week all 8 exactly 2×.

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (gates log `p8_extract`).
- `p8.py compare` core vs edition: **CLEAN**, keydiffs 0 (gates log
  `p8_compare`).
- Registry: `run.py` TOTAL 150, same level/page/type split as the core.

## Visual

- P1: badge Latin-only on the masthead rule; press-time line visible.
  PASS.
- P2: calendar title “Datas desta semana” fully visible, clear of the
  valley photo; all 4 word cards inside their boxes, examples 1 line.
  PASS.
- P4: Notas box 6 lines, bottom clear of “GEN，” below; C head “Ler o
  calendário” fits. PASS.
- P5: C head “Horas e números” fits. PASS.
- P7: A2 head “Final e pacotes” fits; teaser band ends 2588.78, clear
  of footer. PASS.
- P8: D head “Ler e responder” fits; test sections A–F, keys 1–150 +
  footer clear. PASS.
- P3/P6: unchanged since transform.

## Logs (this dir)

`transform-pt.log`, `run-pt.log`, `run-pt-2.log`, `p8sim-pt.log`,
`render-pt.log`, `webpdf-pt.log`, `gates-pt.log`, `freeze-diff-pt.log`,
`leak-pt.log`, `vis-pt-p1/p2/p4/p5/p7/p8.png`.
