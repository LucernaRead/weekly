# EDITION-RECORD — 2026-w47-zh-cn-it (Italian explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Builder handoff, NOT a
finalisation claim: independent proofreading is still owed by the parent
line. No commit, no push, no insert, no lint run by this builder.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-IT.pdf` (print) | 41,730,134 | `d1ae6f877573b068e757e12b69a9dcb67dd8fd5242e02d5c10b17b95fd52a001` |
| `Lucerna-VOL4-IT-web.pdf` (web) | 2,641,804 | `75dec91ac806b884bdd4b7cdbdccc39e2c445ff7f668d24ff4365f21f233a512` |
| `2026-w47-zh-cn-it.text.md` | 50,958 | `f954151fb204030d9d273e0f0032d9674509fd9bb170c7fc460c062eec46ecc4` |
| `ABSTRACT.txt` | 319 | matches `tables.py` ABSTRACT['it'] + newline |

## Fixes applied in #3 (2026-11-11)

First `run.py`: RC=0 TOTAL 150 with 6 HEAD TOO WIDE + 1 P8-keys overflow.
All 9 fixes went into the table sources (`fresh.py` / `gen_tables.py`
f-string) AND the edition files; `gen_tables.py` re-run: 276 ENTRIES,
0 missing, 0 extra, 0 unconsumed; table diff = exactly the 9 changed it
lines.

1. A-head ×5 (P2–P6): “Leggere e scegliere” → “Leggi e scegli”
   (377.1 px at 25 pt).
2. P8 D-head: “Leggere e rispondere” → “Leggi, rispondi” (407.8 px
   at 24 pt).
3. P2 calendar title: “Le date di questa settimana” → “Date della
   settimana” (ends x = 1424.3, clear of the valley photo).
4. P8 notes 2L→1L (6): Q20 “SF Express dello Hunan: +20 % di personale
   e capacità.”; Q24 “L'anno scorso, giorno migliore: 777 milioni di
   articoli.”; Q95 “Una barra: totale 22 giorni; l'altra: picco di un
   giorno.”; Q109 “「139.38亿件」: conteggio finale delle Poste, già
   contato.”; Q148 “Dopo la Piccola Neve, vestiti pesante, non prendere
   freddo.”; Q150 (f-string) “Esercizio aperto — modello sopra, sezione
   F (138 caratteri).” Keys 2604.2 → 2506.4.
5. Proactively measured, no fix needed: P4 gloss 6 lines under “Note｜”;
   all 4 P2 word-card examples 1L at 19 pt.
6. `WEEKLY-KIT.md` rewritten for it (was an untranslated copy of the
   core KIT, pairing zh-cn × en).

## Gates (final files)

`gates-zhcn.py` (`gates-it.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 383, P2 377, P3 280, P4 353, P5 279, P6 355, P7 527, P8 1837) |
| pdftotext_nonempty | print 44,907 B, web 44,907 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75), spans 369 |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

Plus: `run.py` RC=0 TOTAL 150 (A2 56 / B1 69 / B2 25; pages
10/18/18/18/18/18/12/38), 0 overflow; P7 teaser ends 2562.26; P8 keys
end 2506.4; `freeze.py baseline` core 8/8 byte-identical (venv Pillow
13.0.0 / FreeType 2.14.3, core integrity confirmed); `freeze.py diff
--strict-cjk` TOTAL added CJK **0**, exit 0 (`freeze-diff-it.log`);
leak scan over all 275 translate sources vs final SVG + text.md:
**0 real leaks** (`leak-it.log` — IDENTICAL only: “体育　Sport”,
“悬疑 = suspense, b”); phrases of the week all 8 exactly 2×.

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (gates log `p8_extract`).
- `p8.py compare` core vs edition: **CLEAN**, keydiffs 0 (gates log
  `p8_compare`).
- Registry: `run.py` TOTAL 150, same level/page/type split as the core.

## Visual

- P1: badge Latin-only on the masthead rule; press-time line visible.
  PASS.
- P2: calendar title “Date della settimana” fully visible, clear of the
  valley photo; all 4 word cards inside their boxes, examples 1 line.
  PASS.
- P4: Notes box 6 lines, bottom clear of “GEN，” below; C head “Lavoro
  sul calendario” fits. PASS.
- P5: C head “Ore e numeri” fits. PASS.
- P7: teaser band ends 2562.26, clear of footer. PASS.
- P8: D head “Leggi, rispondi” fits; test sections A–F, keys 1–150 +
  footer clear. PASS.
- P3/P6: unchanged since transform.

## Logs (this dir)

`transform-it.log`, `run-it.log`, `run-it-2.log`, `p8sim-it.log`,
`render-it.log`, `webpdf-it.log`, `gates-it.log`, `freeze-diff-it.log`,
`leak-it.log`, `vis-it-p1/p2/p4/p5/p7/p8.png`.
