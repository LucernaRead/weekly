# WEEKLY-KIT · 2026-w46-es-ru — La Lucerna, Spanish Weekly VOL.3, explanations in Russian

Slug: `2026-w46-es-ru`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Russian, written natively.
Build dir: `hidden_files/weekly-report-w46-es-ru-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_ru.py` + `t_ru2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-es-ru.pdf` 3,776,995 B; web PDF `2026-w46-es-ru.web.pdf` 664,679 B (<7 MB), text layer 54,419 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Furniture (W45 ES×RU KIT §2, VOL.1→VOL.3 only)

- Badge replaces the y=372 subtitle slot, 19.5pt BRICK: `ТЕКСТЫ НА ИСПАНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`.
- Edition line (name line, y=330): `ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA` at **40pt** (not the core 46pt — see §5).
- Top strip: `CADA SEMANA EN ESPAÑOL · ИСПАНСКИЙ ГЛАЗАМИ ИСПАНИИ` (middle segment dropped — see §5).
- Band right: `КАМПАНИЯ НАЧИНАЕТСЯ В ПЯТНИЦУ, 13 · ЗАБАСТОВКА В СРЕДУ, 11` / `ГЛАВНАЯ ТЕМА · СМ. СТРАНИЦЫ 2 И 6`.
- Footer: `La Lucerna · ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА ИСПАНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ` / `Страница N из 8`.
- Gloss prefix `Пояснение — `; `bridge()` → `expl()` (definition and all call sites).
- Bands: VIDA · Жизнь / CULTURA · Культура / DEPORTE · Спорт / JUVENTUD · Молодёжь / A FONDO · Разбор / LENGUA · Язык / EJERCICIOS Y RESPUESTAS · Упражнения и ответы.
- P8 separator `— СТРАНИЦА N — `; P7 phrase tags `(Страница N)`.
- P8 header left/right in Russian; exercise headers and right note in Russian; instruction chips: Вставьте / В/НВ / Составьте предложение / Перепишите / Перевод / Письмо / Соотнесите.
- Type names translated: Выбор в тексте / Дополните предложение / Выбор ответа / Верно или неверно / Составьте предложение / Преобразуйте предложение / Соотнесите слова / Перевод / Письмо. P8 check `== "Письмо"`.
- Section-H text in Russian; keys 137/138 re-aimed to Russian source sentences; notes 139/140 in Russian; key 150 note `(открытый вопрос — образец ниже)`.
- Word note (one line): `«La huelga general»: всеобщая забастовка.`
- Disclosure: `Примечание: писем нет; печатаем пример. Обещание — на VOL.4.` (the no-best-P8-texts fact stands in the Spanish disclosure above — DE/NL precedent; shortened for fit, see §5).

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] — the two translation keys re-aimed to Russian; all other keys byte-identical. `freeze.py diff` vs core SVGs: added CJK 0 on every page; edition CJK 0.

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-ru-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer: 54,733 B, identical to print text; <7 MB.
- Visual + pixel measurement: P1 header verified by ink-run measurement of the rendered card (top strip ends x=1291, date line starts x=1406; name-line ink x=157–1792, inside the 65–1885 content area); P7 inspected — disclosure inside its box, preview band clear of the footer rule.

## 5. Fixups (Russian apparatus only; core geometry and Spanish text untouched)

1. P6 exercises 18.5pt/gap2 + P8 answers 13.2pt/1.12 pre-applied (W45 RU fixups).
2. P1 word note wrapped to 2 lines and crossed the y=1844 rule (`день.` LINEX flag) — shortened to the one-line `«La huelga general»: всеобщая забастовка.` (verified 1 line at the true 434px/19pt-sans width).
3. P7 col-3 ran 50px long (1884.14 vs core 1834), pushing the preview band onto the footer rule (FOOTER/LINEX flags) — palabra note shortened to one line (`huelga general = всеобщая забастовка.`) and disclosure shortened by one line (see §2); col-3 now 1826.14.
4. Header geometry (caught visually; the canonical audit does not flag header-zone text/text grazes or centered-line edge overflow): the edition name line at the core 46pt rendered ink x=26–1923, overflowing the content area on both sides — reduced to 40pt (ink now 157–1792, measured on the rendered card). The top strip (`… КАЖДУЮ НЕДЕЛЮ · ИСПАНСКИЙ ГЛАЗАМИ ИСПАНИИ`) collided with the date line (`ИСПАНИИSEMANA`, nominal gap 5.6px) — middle segment dropped; strip now ends x=1291, 115px clear of the date. Rebuilt and re-gated: 0 flags, header verified by pixel measurement.
5. Core letters-box fix inherited via rebuild from the fixed core build.
6. Note: the W45 RU build shipped the same 46pt name line and three-segment strip (verified in `hidden_files/weekly-report-w45-es-ru-build/content12.py`); the W46 fixes above correct that inherited geometry. W45 is out of scope and was not touched.

## 6. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py ru t_ru` (copies the fixed core build, applies `t_ru.py` + `t_ru2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-ru-diff.json`, `es-ru-p8-compare.json`, `es-ru-occlusion.json`, `es-ru-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.

## D5 rebuild (2026-11-15)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target es --reader ru --week 2026-w46` (`--check` dry-run clean first). Mode ru (old branch, D26); `_D5_READER = "ru"`. Routing test `test_d5_routing.py` FAILURES: 0. fix2 retained (`_QUOTE_CLS` x4).
- Pre-fix census (baseline build): D5 Latin-in-CJK 345, D5 Cyrillic-in-CJK 253, curly-in-CJK 0, curly total 0 (all Newsreader). Run2 census: Latin 0 / Cyrillic 0 / curly-in-CJK 0; curly total 0 all Newsreader; Noto Sans 789 (ru Cyrillic correctly in Noto Sans, D26 old branch).
- run1 gates 17/19; run1 -> run2 fixes (font-size reduction only, no copy changes):
- `content12.py:71` — P1 guide 19 -> 18 (margin 5.8px)
- run2 gates 19/19 ALL-GREEN. G8 CLEAN (core-es P8 compare; keydiff [137, 138]). G10 CJK added 1 (P6 U+3000 run-split, as W45 es); Latin added 165 (run-split). G12 26 titles, 376 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal. G14 0 defects; P8 234 rows, slack 42.7px. G15a text-layer diff 0; text.md DIFF 94 lines, native verifier ADOPT (REWRAP 22, 0 UNEXPECTED). G15b CARRYOVER FAIL svg=5491 md=6883 (record-only, D27).
- D18 gap 150.0px; D37 N/A (no badge line in the box zone; strapline y=372 above box top 588); D39(4) P7 band bottom vs footer 2596: -6.8px.
- Old (baseline build) print `La-Lucerna-VOL3-es-ru.pdf` 4,111,508 B SHA256 `fb75fd94164845c1b922f5f8544eb56d00e26cb16f7ebb249e288e33ae9a5e4e`; web 543,432 B SHA256 `868a3ab3898ce1633dcd2f30be09ef7186659ed34e142ae6ae34d21452b1ab4c`.
- New (run2) print `La-Lucerna-VOL3-es-ru.pdf` 3,776,995 B SHA256 `90665b4d609dc9d478d22c10678053adce89d0b9e6837feb06e6b421b660f0e8`; web `2026-w46-es-ru.web.pdf` 664,679 B SHA256 `3c0e1155dbf7f93ff2f3ca2852c14e058776b7e79eee8caaaa3d3ccc48abcf57`; text.md 54,065 B SHA256 `1659e089e12b78806eb28fad85b25259bf599d8099b1a25475a662d22b64f90c` (textexp output, `logs/2026-w46-es-ru/2026-w46-es-ru.text.md.run2`; the `<slug>.text.md` in the edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it).
- Logs: `logs/2026-w46-es-ru/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-ru/g*-run2.log`, `logs/2026-w46-es-ru/census-run2.json`, `logs/2026-w46-es-ru/freeze-diff-run2.json`. D5 report: `notes/g-es/scratch-d5-rebuild-es/2026-w46-es-ru-D5-REPORT.md`.
