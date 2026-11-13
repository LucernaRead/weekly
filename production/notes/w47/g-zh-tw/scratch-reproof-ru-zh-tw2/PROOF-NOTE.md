# PROOF NOTE — W47 ru-zh-tw, ROUND-2 re-proof (independent)

- Edition: `2026-w47-ru-zh-tw`
- Production dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-zh-tw/`
- Proofer: independent round-2 (did NOT build the edition, did NOT do the fix)
- Date: 2026-11-11 (read 23:05–23:10 UTC)
- Scope: full read of the print PDF (all 8 pages, text + visual), the full
  `text.md` (839 lines), and the web PDF (text comparison).

## VERDICT: (a) ZERO FINDINGS

## SHA-256 (start and end of read — identical; no file changed mid-read)

| File | Bytes | SHA-256 (start = end) |
|---|---|---|
| `2026-w47-ru-zh-tw.text.md` | 60,850 | `277a24f8a1674c970a367bf4fc8cccdd85d3f88941f85d633713a0e525ee6c83` |
| `Lucerna-VOL4-ru-zh-tw.pdf` (print) | 24,784,332 | `094b6a3b17cb34d7b0760a2bc1775cd9e59aadedb5f906ce51e103254ad537ca` |
| `Lucerna-VOL4-ru-zh-tw-web.pdf` (web) | 3,994,661 | `eba60ec2f70f220cecf42d633976ce146c1276603000b046c1f23ff0dd07c3c2` |

All three match the brief's expected SHAs exactly, and match KIT §1
(`WEEKLY-KIT.md` L13–15) exactly. The pre-insert web-PDF rebuild job did NOT
rewrite the web PDF during this read (SHA stable start→end); no web verdict
deferral needed. Print SHA never changed — no stop condition triggered.

## F1 fix verification (round-1 finding: Q58 Krasnodar misspelled 克拉斯諾輔達爾)

- `輔達爾` hits: `content34.py` 0 · `text.md` 0 · print PDF text 0 · web PDF text 0.
- Character `輔` anywhere: `text.md` 0 · print PDF text 0 · web PDF text 0.
- Print P8 (text extract + 150-dpi visual crop): `58. a — 克拉斯諾達爾 a` — correct,
  no extra character. Visually confirmed.
- `text.md` L335: `58. «Краснодар» — победил ЦСКА 4:2 (key a · 克拉斯諾達爾 a)` ✓
- `text.md` L736 (appendix 58): `58. a — 克拉斯諾達爾 a` ✓
- `text.md` L836 (Fix 1, untouched): `150. ✓ 範文見本版 H 區（97 詞）` — exact ✓
  (also confirmed on print P8 by extract + visual crop).
- All other Krasnodar mentions use `克拉斯諾達爾` (text.md L83, L303, L316, L319,
  L614, L680, L726, L729, L810; P4 section head; P8 keys 48/51/124).

## Page-by-page notes (print PDF, visual + text)

- **P1** — Clean. Masthead `VOL.4`, week `16–22 ноября 2026`, lead
  `14-й тур: «Зенит» и «Динамо» — по 31 очку`; contents box (Стр. 2–8 all match
  the actual pages); word of the week `«чёрная пятница»`; weather box;
  park photo + caption with CC0 credit; exercises 1–10. Lead facts consistent
  with P4 (31/29/26 points, 4:2, 0:1, 21 goals, 8 matches). Footer `第1版／共8版`.
- **P2** — Clean. `Студенты и Дед Мороз: 17 и 18 ноября`; holidays sidebar
  16–22 Nov; `А вы?` box (VOL.5 p.7 reader letters); Yuon `«Зима. Ростов»`
  painting + caption/credit; 4 word cards (оттепель / мокрый снег /
  ледяной дождь / гололедица); exercises 11–28. No overflow/overlap.
- **P3** — Clean. `Кино 19 ноября: пять премьер`; `А ЧТО УЖЕ В КИНО?`,
  `ГЛАВНОЕ — КОРОТКО`, `КАК ПРОВЕСТИ ВЕЧЕР` side boxes; exercises 29–46.
  (Layout whitespace band mid-page between article and exercises — empty
  space, not overflow; same pattern on P5/P6.)
- **P4** — Clean. All 8 round-14 results in the table, verified:
  Локомотив–Рубин 0:1, Факел–Динамо 1:2, Ахмат–Родина 1:0,
  Краснодар–ЦСКА 4:2, Крылья Советов–Оренбург 2:0, Спартак–Акрон 2:1,
  Зенит–Ростов 2:2, Балтика–Динамо Мх 0:1 — this sources Q52–Q56 and Q59,
  all consistent with the article text and the answer keys. 1912 national-team
  photo + caption; TOP-5 table; national-team box (Tashkent/Krasnodar);
  8 round-15 fixtures; exercises 47–64. VOL.3 correction (8th match
  Балтика–Динамо Мх 0:1, 8 Nov 20:45) present and consistent.
- **P5** — Clean. `«Чёрная пятница»: скидки с 16 ноября`; `А ЧТО С 11.11?`
  box (14.4M Ozon orders 11 Nov 2025); dates sidebar; market photo
  (corn) captioned `На рынке: свежие овощи и фрукты…` + USDA credit;
  exercises 65–82. Sale dates consistent across article/sidebar/Q65–69.
- **P6** — Clean. `Неделя 16–22 ноября: как её прожить`; day-by-day strip
  16 пн – 17 вт – 18 ср – 19 чт – 20 пт – 21 сб – 22 вс (correct: 16 Nov 2026
  is a Monday); practice-data chart 38/26/18/18 = 100 with the
  `учебный опрос … не настоящая статистика` disclaimer; `ЗА И ПРОТИВ` box;
  exercises 83–100.
- **P7** — Clean. Three levels (A2 weather words / B1 shopping words /
  B2 citing sources); `ОШИБКИ` correction box (4 items, all grammatically
  correct corrections); Pushkin portrait + caption/credit; `ПИСЬМА ЧИТАТЕЛЕЙ`
  (editorial sample, honestly labelled, promise carried to VOL.5);
  `ФРАЗЫ НЕДЕЛИ` — all 8 quotes verified verbatim against their cited pages
  (P1 ×2, P2, P3, P4, P5, P6 ×2) with correct page numbers; VOL.5 preview;
  exercises 101–112. Weekly-word box `«распродажа»` (P7 language-page word;
  P1 cover word is `«чёрная пятница»`).
- **P8** — Clean. Big test 113–150 (A ХРОНИКА · B ОБЩИЕ · C Маша reading ·
  D sentences · E translation · F words · G shop dialogue · H writing);
  model essay for Q150 printed in full; answers section with
  `— СТРАНИЦА 1 —` … `— СТРАНИЦА 8 —` markers; Bilibin `«Морозко»`
  illustration + caption/credit. No overflow/overlap/clipping/tofu.

## Cross-checks (programmatic)

- Appendix keys: 1–150 present, contiguous, none missing.
- Inline questions: 1–150 present, none missing; inline↔appendix key values
  agree for all 150 (only Q150 differs by design: open writing question,
  inline key `（開放題，範文如下）` vs appendix `150. ✓ 範文見本版 H 區（97 詞）`).
- Printed P8 answer keys (extract): 1–150 all present, none missing.
- Q150 model essay: exactly 97 words as claimed (whitespace-token count).
- Web PDF: 8 pages, same page size as print; extracted text identical to
  print (whitespace-normalized, 25,852 chars, similarity 1.0); 0 `輔` hits.
- Dates/weekdays verified: 12 Nov = Thursday, 16 Nov = Monday, 17 Nov = Tuesday,
  27 Nov = Friday (2026); 20 Nov 15th round, 30 Nov Cyber Monday, all consistent
  across article, sidebars, questions and keys.
- Scores consistent P1 ↔ P4 table ↔ keys (31/29/26; 4:2; 2:2; 2:1; 0:1; 2:0).

## Observation (NOT a finding — for the coordinator to decide)

- `text.md` L668 contains a literal line `— СТРАНИЦА ? —` directly above
  `## Answers`. It is a template/exporter artifact, identical in ALL
  ru-target `text.md` files of W47 (checked: ru-de, ru-en, ru-es, ru-fr,
  ru-it, ru-ja, ru-ko, ru-nl, ru-pt, ru-zh-tw), present in the pre-fix file
  too, and the print PDF renders the correct `— СТРАНИЦА 1 —` … `— СТРАНИЦА 8 —`
  markers. It is generator-wide (ru_textmd.py), not specific to this edition,
  and the answers remain grouped under per-page headers. Recorded here so the
  coordinator can decide whether the exporter should drop the line; it does
  not block this edition.

## Method / files

- Read-only. No production file modified, no re-render, no commit/push/lint.
- Extracts + page renders were made in `/tmp/reproof2/` and deleted after
  the note was written (disk is tight); this note is the only file written.
- Tools: `pdftotext -layout` (per-page + whole-file), `pdftoppm` (70 dpi full
  pages + 150 dpi P8 crops), `sha256sum`, `grep`, Python key/word-count checks.
