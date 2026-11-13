# EDITION-RECORD — 2026-w47-zh-cn-ru (Russian explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Builder handoff, NOT a
finalisation claim: independent proofreading is still owed by the parent
line. No commit, no push, no insert, no lint run by this builder.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-RU.pdf` (print) | 33,572,611 | `7cd883dd1b5311e878abc0d8a2a899864c69cdae6b03aed740d738a3a9b19b93` |
| `Lucerna-VOL4-RU-web.pdf` (web) | 2,486,444 | `ab0aaf106dba13e9b329550b560ad59757d71e528793fdceeb75bbf8955634f6` |
| `2026-w47-zh-cn-ru.text.md` | 60,515 | `f722ad0fb0f617bcb54c76afb2163b00f6fc7b9c7af79bc46e3476214717cd3d` |
| `ABSTRACT.txt` | 426 | matches `tables.py` ABSTRACT['ru'] + newline |

## Fixes applied in #3 (2026-11-11)

First `run.py`: RC=0 TOTAL 150 with 7 HEAD TOO WIDE + 6 P8-keys overflows
+ P7 teaser at 2670.82 (worst of the week). Round 1: 16 table values
(heads, wcn, 2 error-clinic notes, word card, 9 P8 notes) into
`fresh.py` / `harvested.json` / `gen_tables.py` f-string + the edition
files; table diff vs pre-ru state = 16 ru lines. Round 2: 5 more P8
notes (see packing note below); total table diff = 21 ru lines. Then a
P4 gloss fix found by the gates (1 more table line, 22 total).

Round 1:

1. A-head ×5 (P2–P6): “Прочитать и выбрать” (490.8 px at 25 pt) →
   “Читай, выбери” (406.3 px).
2. P4 C-head: “Работа с расписанием” (424.7 px) → “Читай расписание”
   (376.6 px).
3. P8 D-head: “Прочитать и ответить” (503.3 px at 24 pt) → “Читай и
   ответь” (417.4 px).
4. P7 wcn: the harvested value is “Конструкция: …”, not “Структура:
   …” — the first fix attempt targeted the wrong string and applied
   nothing (SKIP in both sources); corrected to “Конструкция: 先 …
   再 … — X, потом Y.” (2 → 1 line, −29 px).
5. P7 error-clinic rows 1–2: “地 (de) показывает, как совершается
   действие.” → “地 (de) — как совершается действие.”;
   “得 (de) связывает глагол + степень: 来得快.” → “得 (de): глагол +
   степень.” (each 2 → 1 line, −26.52 px). Teaser 2670.82 → 2588.78.
6. P2 word card: 退换货 example “не подошло? отправь обратно
   пораньше” (2L, second line below the card) → “не подошло? верни
   пораньше” (1L).
7. P8 notes 2L→1L (9): Q3 “Финал — в «Барклайс-центре», Бруклин.”;
   Q17 “tuìhuànhuò — возврат и обмен; верни пораньше.”; Q18
   “shēnqǐng — защита цены не сама; подай заявление.”; Q20
   “«SF Express» Хунани: +20 % персонала и мощностей.”; Q83 “Ни один
   день не взорвался; все дни напряжённые.”; Q95 “Столбец 1: итог 22
   дней; столбец 2: пик дня.”; Q109 “「139.38亿件」 — итог почты, уже
   подсчитано.”; Q111 “Данные и оплата сначала, заголовок —
   последним.”; Q148 “После Малого снега — теплее, не простужайся.”

Round 2 — P8 packing (the key finding of this edition): the 9 round-1
notes saved 138.9 px of total height but the flow still ended at
2604.2. The flow walk resets y to BOTTOM when a para overflows the
last column, so the end y is BOTTOM + h(Q150) while Q150 overflows —
height saved in cols 0–2 cannot move it. What-if simulation with
`p8sim.py` overrides (absolute path required — `p8sim.py` chdirs into
the edition, so relative override paths die with FileNotFoundError
after the content run) showed 5 more 1L notes fix it: Q88/Q107 in col 2
(shift the col-2→col-3 break), Q145/Q149/Q150 in col 3 (Q150 is the
`gen_tables.py` f-string). Applied: Q88 “dǎsàn — пик распределился, не
на один день.”; Q107 “От большего к меньшему: 22 нояб., воскресенье.”;
Q145 “Порядок: полуфинал, посылка, культурный центр.”; Q149 “Стр. 6:
данные сначала, реклама — последней.”; Q150 “Открытое задание —
образец в разделе F (138 знаков).” Keys 2604.2 → 2535.1, 0 overflow
paras (exactly as simulated).

Gates round 1 then failed occlusion: the P4 gloss is 7 lines under the
long “Примечания｜” prefix (the first measurement used the English
“Notes｜” and wrongly read 6) — the box bottom reached 821.9 and
covered “GEN，” at 93%. Fix: gloss “последние четыре команды,
полуфиналисты” → “последние четыре команды” (6 lines, box bottom
792.25). Re-ran to ALL PASS; re-rendered, rebuilt the web PDF with the
patched `webpdf.py`, re-exported, re-gated (round 2: 11/11 PASS). The
rebuild chain was interrupted once by a VM restart after the re-render
(the webpdf step died mid-run — log stops at the font list, no WROTE
line); the web PDF / export / gates steps were re-run from the verified
on-disk state (print PDF SHA already matched the post-fix render).

`WEEKLY-KIT.md` rewritten for ru (was an untranslated copy of the core
KIT, pairing zh-cn × en).

## Gates (final files)

`gates-zhcn.py` (`gates-ru-2.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK; round 1 failed with 1 flag, the P4 GEN cover) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 356, P2 350, P3 259, P4 336, P5 267, P6 315, P7 478, P8 1566) |
| pdftotext_nonempty | print 52,561 B, web 52,561 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75), spans 906 |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

Plus: `run.py` RC=0 TOTAL 150 (A2 56 / B1 69 / B2 25; pages
10/18/18/18/18/18/12/38), 0 overflow; P7 teaser ends 2588.78; P8 keys
end 2535.1; `freeze.py baseline` core 8/8 byte-identical (venv Pillow
13.0.0 / FreeType 2.14.3, core integrity confirmed); `freeze.py diff
--strict-cjk` TOTAL added CJK **0**, exit 0 (`freeze-diff-ru.log`);
leak scan over all 275 translate sources vs final SVG + text.md:
**0 real leaks** (`leak-ru-2.log`, re-run on the re-exported text.md);
phrases of the week all 8 exactly 2×.

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (gates log `p8_extract`).
- `p8.py compare` core vs edition: **CLEAN**, keydiffs 0 (gates log
  `p8_compare`).
- Registry: `run.py` TOTAL 150, same level/page/type split as the core.

## Visual

- P1: badge Cyrillic-only on the masthead rule; press-time line
  visible. PASS.
- P2: calendar title “Даты этой недели” fully visible, clear of the
  valley photo; all 4 word cards inside their boxes, examples 1 line.
  PASS.
- P4: Примечания box 6 lines, bottom clear of “GEN，” below; C head
  “Читай расписание” fits. PASS.
- P5: C head “Время и числа” fits. PASS.
- P7: error-clinic rows 1–2 shortened, wcn 1 line; teaser band ends
  2588.78, clear of footer. PASS.
- P8: D head “Читай и ответь” fits; test sections A–F, keys 1–150 +
  footer clear. PASS.
- P3/P6: unchanged since transform.

## Logs (this dir)

`transform-ru.log`, `run-ru.log`, `run-ru-2.log`, `run-ru-3.log`,
`run-ru-4.log`, `p8sim-ru.log`, `p8sim-ru-2.log`, `p8sim-ru-5.log`
(what-if, absolute-path overrides), `p8-overrides-ru2.json`,
`render-ru.log`, `render-ru-2.log`, `webpdf-ru.log`, `webpdf-ru-3.log`,
`gates-ru.log`, `gates-ru-2.log`, `freeze-diff-ru.log`,
`leak-ru.log`, `leak-ru-2.log`, `vis-ru-p1/p2/p4/p5/p7/p8.png`.
(`p8sim-ru-3.log` / `p8sim-ru-4.log` are the two what-if runs whose
relative override paths were never applied — see packing note above.)
