# WEEKLY-KIT — Lucerna 日本語版 VOL.4, Russian-reader edition (W47, 16–22 Nov 2026)

Slug: `2026-w47-ja-ru`. Target language: Japanese. Reader language:
Russian. Built by fan-out from the re-settled core `2026-w47-ja-zh-cn`
(core-ja, frozen; only the explanation layer was rewritten).

## §1 Specification — SOP §1.1 visual system

- 8 pages, 1950×2700, 4 columns. Paper `#fbfaf6`, ink `#302c28`,
  caption `#6f675d`, fine line `#d8d2c4`, book-green cloth `#37402f`,
  olive `#46581f`, goose-yellow `#f6e08e`, on-cloth `#f4efe1`.
  Level badges: A2 `#5c6e30`, B1 `#46581f`, B2 `#37402f`, white text.
  No gold, no brick-red, no near-black backgrounds; no double outer
  frame; no `·` separator anywhere (8/8 SVGs: `·` 0×, `#fbfaf6`
  1×/page, old `#f7f1e2` 0×).
- Masthead `Lucerna` (no article for Japanese; UnifrakturMaguntia
  196px = 147pt). P1 headline 56px = 42pt. Margins MX=88px = 66pt.
  Footer every page: `Lucerna　ЯПОНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4　Текст
  на японском　Объяснения на русском`, page line `Страница N из 8`
  (Russian, per reader language). VOL.4 everywhere it is an issue
  number; VOL.5 appears 3× (P4 previous-issue note, P7 disclosure
  merged single mention, P7 next-issue teaser — same pattern as de).
- Exercises: 150 total, continuous numbering 1–150, registry-generated
  P8 answers. Measured: A2 48 · B1 73 · B2 29. By page:
  10/18/18/18/18/18/12/38. By type (registry): дополнить предложение
  50 · выбор ответа 51 · сопоставление 12 · построение предложений 8 ·
  верно/неверно 11 · текст с пропуском 13 · перевод 4 · Написать 1.
  P8 model text 154 characters.
- Practice section heads stay in Japanese, frozen (A　理解,
  B　ことば, C　数字と日付, C　文を作りましょう,
  D　ペアにしましょう, D　正しい・正しくない, B　グラフ,
  C　数字と事実, D　文を完成しましょう, B　一般問題,
  スポーツ　体育); exercise-type labels are Russian (Вставить,
  выбор ответа, текст с пропуском, Соотнесите,
  Составить предложение, Верно или неверно?, Перевести,
  Написать). `match_set` instruction is `Соотнесите`.
- `りくりゅう`: romaji `rikuryuu` in the P7 gloss and P8 answers.
  `ちいかわ`: `Чикава` (never the Chinese name 吉伊卡哇).
- Trend-box source line (P1): `Источники и даты — в статьях`
  (278px at 19px sans, fits the 400px box, one line). P7 disclosure
  (readers' corner) is Russian, 5 lines: "Пример редакции, а не
  настоящее письмо. К сроку не пришло ни писем, ни лучших
  сочинений со страницы 8; и то и другое появится в VOL.5.
  Пришлите нам письмо на японском!" No real letters were
  fabricated; nothing was fetched from any mailbox.

## §2 Lead and page contents

Same as the core (frozen Japanese text, facts, dates, pictures).
P1 lead: Ni-no-tori + Beaujolais Nouveau release, Thu 19 Nov.
P2 life (Tori-no-ichi + kumade). P3 culture (Beaujolais + stalls).
P4 sport (sumo Kyushu basho days 1–3, champion undecided, final
result promised in VOL.5). P5 youth (30 buzzword nominees +
Arashiyama photo). P6 deep read (foliage moving to Kyoto + labelled
practice-data chart, 38/24/22/16 = 100%). P7 language focus
(A2/B1/B2 columns + error clinic ×4 + frame 「福をかき込む」 +
readers' corner + 8 golden phrases + VOL.5 teaser). P8 assessment
+ writing + all keys.

## §3 Trend sources

Unchanged from the core — see `core-ja/WEEKLY-KIT.md` §3 (sumo
day 1–3 results, Tori-no-ichi, Weathernews foliage forecast,
Beaujolais Nouveau 19 Nov, buzzword nominees 5 Nov, calendar).
No new research was done for the fan-out; no fact was changed.

## §4 Promises honoured

Same as the core (KIT §4): sumo final in VOL.5, buzzword top 10 +
grand prize 1 Dec, readers' letters + best P8 writing carried
forward (disclosure re-printed in Russian), foliage continuation.

## §5 Golden phrases

The core's 8 phrases, verbatim Japanese + Russian glosses on P7
(Russian glosses translated from the core's Chinese glosses; the
Japanese sentences are byte-identical to the core).

## §6 Images

Same five PD/CC0 images as the core (P1 maple, P3 beaujolais,
P5 Arashiyama pond, P7 tori 2025, P8 Arashiyama temple). Credits
in `assets/CREDITS.md` (copied from the core). Russian captions
are the translated map values (e.g. `Фото: Poliphilo — CC0
(Wikimedia Commons)`).

## §7 Proofread record (builder self-check, this edition)

- Full text read: `2026-w47-ja-ru.text.md` (1380 lines) +
  all 8 card PNGs visually checked. No overflow, overlap, footer
  strike or tofu found in the final artifacts. Cyrillic renders
  in Noto Serif/Sans CJK JP (verified: U+0427 and Hangul U+CE58
  in the CJK faces; no font change needed).
- Simplified-Chinese residue scan over the text dump and the SVGs:
  0 hits (`吉伊卡哇` 0×, `参考答案` 0×, `酉之市` 0×, `提名` 0×).
  `ryuuryuu` / `Чикава` as specified.
- 150 keys re-verified key-by-key against the core extract:
  only [137, 138, 139, 140] differ — the E-group translation
  answers, translated JA→RU as ruled: 137 `Ни-но-тори
  19 ноября.`, 138 `Молодое вино выходит 19 ноября.`,
  139 `Номинации на модное слово объявлены 5 ноября.`,
  140 `Кто пойдёт смотреть листья, должен проверить и прогноз
  дат, и нынешнее состояние.` All other 146 keys byte-identical
  to the core.
- P7 teaser ends 2525.62 (footer 2580, 54px clear); P7 col3 ends
  1751.62. P8 exercise flow ends col 3 y=561 (bottom 1252); P8-keys
  flow ends col 3 y=2428 (bottom 2540, 112px slack).
- Fix1 re-measurement (2026-11-11, see §11 F3): P7 disclosure last
  baseline 2546.70 (footer band 2580, 33px clear; D4 note now wraps
  to 2 lines, clinic box intact, occlusion 0 flags); P8 keys max
  baseline 2530.35 (#115, bottom 2540, 10px slack; D3 note now
  wraps to 2 lines). P8 minimum font size unchanged at 9.975pt.

## §8 Gates (all recorded in scratch-fanout-ja/)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE
  (`build-ru-run2.log`; run1 had 2 P8-keys overflows, fixed —
  see §11; run3 is the identical re-run for the freeze check).
- Occlusion audit: `tools/occlusion_audit.py` — 0 flags
  (`ru-occlusion.json`; selftest OK, all 6 classes fired on
  planted controls, clean controls silent).
- P8 extract: `tools/p8.py extract --total 150` — noted set 150/150
  (`ru-p8.json`).
- P8 compare: `tools/p8.py compare` vs the core — status CLEAN,
  missing=[] extra_count=0 uncertain=[], keydiff=[137, 138, 139, 140]
  (`ru-p8compare.json`).
- Freeze: direct sha256 of the 8 SVGs, two consecutive builds
  (run2 vs run3) — 8/8 byte-identical (`ru-sha-run2.txt`,
  `ru-sha-run3.txt`).
- Web PDF: `tools/webpdf.py` — `Lucerna-VOL4-JA-RU-web.pdf`,
  4,469,712 bytes (< 7 MB), 53,256 text bytes, text
  byte-identical to the print PDF.
  Print PDF: `Lucerna-VOL4-JA-RU.pdf`, 25,898,158 bytes, 8 pages.
  Print sha256:
  `44d884ac6b543a6be3f4186ffe8ce22899a5ba90bc1f951539e0a3176af822a4`.
  Web sha256:
  `d130ae325fedb8325a724aef3ee3889b1db01c9ee0d5091b74644a9ab388dbd5`.
  (fix-xru 后现值，见 §12。)
  (Fix-1, 2026-11-11: print 25,858,387 bytes
  `86af0bb5…f2a1592`, web 4,396,966 bytes
  `dd5fdc63…6ef57`, 53,363 pdftotext bytes.)
  NOTE: the print PDF is ~3 MB smaller than the Latin editions
  (29.1 MB) — verified NOT a missing image: all 5 images present
  (P1/P3/P5/P7/P8, ~15.3 MB total), 8 pages, and the same 33
  embedded fonts as the pt print PDF — the difference is font-subset
  size (Cyrillic + fewer Latin glyphs).
- Text: `2026-w47-ja-ru.text.md`, 53,004 bytes, 1382 lines (D5 fix,
  2026-11-12; pre-fix 53,029 bytes, 1382 lines),
  exported from the final SVGs (`export-textmd-ru.py`).
- P8 minimum font size: 9.975pt (answers, 13.3 SVG px; PyMuPDF
  measurement of print PDF p.8; next size 10.35pt = exercises).
  P8 stems stay at 13.8px / 10.35pt per the core (Round 6 rollback).
- §1.1 grep audit on the final SVGs: paper `#fbfaf6` 1×/page,
  old `#f7f1e2` 0×, banned colours 0×, `·` 0×, badges A2 `#5c6e30`
  / B1 `#46581f` / B2 `#37402f`, masthead 196px on P1, page line
  `Страница N из 8` 1×/page, VOL.4 as the issue number.

### D5 rebuild (2026-11-12; evidence in `hidden_files/w47/scratch-d5-ja/ja-ru/`)

- Production svglib.py replaced verbatim with the ja D5 template (`svglib-ja-d5.py`, `_D5_READER = "ru"`, 1 line diff vs template — the `_D5_READER` line only); old svglib md5 `b8bca01f…`, new `1aca3b74…`. U+201C fix2 routing preserved; quotes census 0 defective.
- Production census before → after: Latin 207 + Cyrillic 226 = 433 → 0 (RC=0). After the patch, 712 elements render Latin/Cyrillic in Noto Sans (as designed for ru mode).
- Gates (all green after the fix below): `run.py` TOTAL 150, 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; `head_check.py` PASS; occlusion 0 flags; p8 extract 150/150, compare vs core-ja CLEAN, keydiff=[137, 138, 139, 140]; freeze baseline 8/8 byte-identical; freeze diff vs base added CJK 2 (all U+3000); spill 0; boxtitle 38 titles, 499 body lines, 0 DEFECT (1 marginal); edge 0 TOUCH / 0 NEAR; creambox PASS 0 defects (n=383 median 1.000 boldT 0.956 boldF 1.023 — the sub-1.0 bold ratio is the narrower Noto Sans Cyrillic; P8 217→217 lines, slack 61.7→61.7 px, no tightening vs the en-ru precedent); text layers print/web identical (26,114 chars); patched-vs-delivered multiset −12 chars, exactly the two intentional content edits below.
- **D5-induced layout defect found and fixed (first build):** the first D5 build failed occlusion with 1 LINEX flag — P7 `す。お楽しみに！` (the `来週` box's second line, baseline 2602.2) crossed the footer rule at y=2596. Root cause, measured: the D5 font routing measures Cyrillic/Latin with their real faces (Noto Sans Medium / Newsreader) instead of the old CJK-face metrics, so two P7 col-3 Russian strings wrapped to one more line each (clinic item 3 gloss 1→2 lines, reader-letter gloss 5→6 lines), pushing the `来週` box down 55.5 px (box y 2434.14→2489.66). Fix in production `content7.py` (layout only, no words added): clinic item 3 gloss dropped its trailing `.` (measured 383.0→377.6 px, back to 1 line); reader-letter gloss dropped `со страницы 8` (back to 5 lines). Rebuilt and re-gated from scratch: occlusion 0 flags, `来週` box back at y=2434.14, teaser ends 2552.14. Note the first (defective) build was briefly synced to production (10:59) before the defect was caught on the full log read; it was overwritten by the fixed build in the same session — no KIT entry was written for it.
- Print PDF `Lucerna-VOL4-JA-RU.pdf`: 25,970,245 bytes, sha256 `2ab6a7d2d740f34834b36ee753c62eafb2e09785c1e212f08f8c2f3c5752268a`.
- Web PDF `Lucerna-VOL4-JA-RU-web.pdf`: 4,540,692 bytes, sha256 `f70444a63e48b76298fb40493203a4b3f83a43f6ef559e0026a2fd7a9d7d525f`.
- text.md updated for the two edits only (53,004 bytes, sha `88e3680b…`; diff vs pre-fix = exactly the 5 changed lines, verified against the new SVG lines grouped by y). NOTE: `export-textmd-ru.py` as shipped is D5-unaware — run against D5 SVGs it emits one line per font run (4,822 lines). Do NOT blindly re-export under D5; the text.md was updated surgically and verified line-by-line against the production SVG. The script's hardcoded ED path (`production/2026-w47/fanout-ja/...`) is also stale; that directory no longer exists.
- Synced to production and re-verified there (freeze baseline 8/8, census 0, quotes 0).

### Fix round — D1 romaji fix (2026-11-12; independent reproof PROOF-NOTE.md)

- D1 (all 11 ja editions): `りくりゅう` romaji `ryuuryuu` → `rikuryuu` (5× per edition: P7 gloss + P8 answers 66/77/80/105). Sources: `content7.py` (2×) + `content56.py` (3×). Japanese core text `りくりゅう` untouched; answer letters untouched.
- Changed SVGs vs pre-fix: p7-kotoba.svg, p8-tesuto.svg; unchanged: p1-hyoushi.svg, p2-kurashi.svg, p3-bunka.svg, p4-supotsu.svg, p5-wakamono.svg, p6-fukayomi.svg.
- Print PDF `Lucerna-VOL4-JA-RU.pdf`: 25,970,343 bytes, sha256 `04b2f315e267d8cf665f07da2c45cf64b80e3ae9f17e8bd8babff6c714636510`.
- Web PDF `Lucerna-VOL4-JA-RU-web.pdf`: 4,540,808 bytes, sha256 `0726eda64903e4b765ef25b3d759b96e806fed13b076e4b13e89108e4c957f8d`.
- Text `2026-w47-ja-ru.text.md`: 53,004 bytes, sha256 `f934bcf1d9f4611d094ed6f55a1f76fc8da74663cfe647c9fed17025af3d4eec` (surgical replacement, exactly 5 lines changed, each only by the fix substitution).
- Full re-gates (all green):
  - run.py: P8 saved, TOTAL exercises: 150
  - head_check: HEAD CHECK PASS 0 defects
  - D5 census: CENSUS PASS
  - quotes: GRAND TOTAL defective: 0
  - occlusion: /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-ru/2026-w47-ja-ru/svg: 0 flags 
  - p8 extract:   set: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
  - p8 compare: status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140] {'status': 'CLEAN', 'total': 150, 'how': 'lines', 'ref_how': 'lines', 'core_count': 150, 'edition_count': 150, 'core_set': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 4
  - freeze baseline: core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
  - freeze diff vs pre-fix base: p8: +4 strings / -4 strings; CJK core 1422 -> edition 1422; added CJK chars: 0 ; added Latin strings: 4 (unexpected 4) | TOTAL added CJK characters: 0 | TOTAL added Latin strings: 5 (unexpected 5)
  - spill: SPILL_SWEEP 2026-w47-ja-ru: 35 boxes, 83 candidates, 0 SPILL, 83 OBSERVE
  - boxtitle: BOXTITLE 2026-w47-ja-ru: 38 titles, 499 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal
  - edge: EDGE_SCAN 2026-w47-ja-ru: 8 pages, 0 TOUCH, 0 NEAR
  - creambox: CREAMBOX PASS 0 defects
  - text layer: print-vs-web multiset diff: +0 -0 IDENTICAL
  - PDF text: /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-ru/2026-w47-ja-ru/Lucerna-VOL4-JA-RU.pdf ryuuryuu: 0; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-ru/2026-w47-ja-ru/Lucerna-VOL4-JA-RU.pdf rikuryuu: 5; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-ru/2026-w47-ja-ru/Lucerna-VOL4-JA-RU-web.pdf ryuuryuu: 0; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-ru/2026-w47-ja-ru/Lucerna-VOL4-JA-RU-web.pdf rikuryuu: 5; 
- Post-sync verification on the production dir: freeze baseline 8/8, D5 census PASS, quotes census 0; production svg/text.md `ryuuryuu` 0×, `rikuryuu` 5×.
  Evidence in `hidden_files/w47/scratch-fix-ja/ja-ru/` (fix log + gate logs + JSONs).

## §9 Reproduction

Build dir:
`production/2026-w47/fanout-ja/2026-w47-ja-ru/` (copied from
`core-ja/` by `scratch-fanout-ja/apply.py ru`, map
`scratch-fanout-ja/map-ru.json`, 221 map keys + 6 instr + meta;
map written from scratch for this edition, key set verified
identical to map-en by `build-map-ru.py`).
`tools/venv/bin/python run.py`, then `render.py` (cards PNG +
print PDF), then `tools/webpdf.py svg Lucerna-VOL4-JA-RU-web.pdf`,
then `export-textmd-ru.py`. Never run a build module standalone;
never import a content module inside a build dir. Scratch (logs,
probes, gate JSONs, maps) lives in
`hidden_files/w47/scratch-fanout-ja/`.

## §10 VOL.5 promises registered

Same as the core (KIT §10).

## §11 Fix record — fan-out fixes (builder, 2026-11-11)

- F1 (P8-keys overflow, run1): keys flow ended col 3 y=2585
  (bottom 2540), 2 FLOW OVERFLOW lines; simulation
  (`probe-p8sim.py ru`) listed 19 two-line entries. Fix (SOP §1.1
  step 2, notes only — keys untouched): shortened 9 distinct
  answer notes in `map-ru.json` (verified one line each with
  `svglib.wrap()` before editing: #1 `Ни-но-тори и молодое вино:
  чт. 19 ноября`, #31/#123 `Виноград собирают около сентября`,
  #32 `Япония первая благодаря разнице во времени`, #33/#37
  `Hanshin Umeda: около 40 видов вина`, #60 `Хосёрю вернулся
  после трёх пропусков`, #79 `30 слов отражают общество года`,
  #81 `Многие постят фото красных клёнов`, #87/#126 `Прогнозы
  различаются: определение разное`, #119 `Номинации объявлены в
  чт. 5 нояб.`), plus the `writing_note` meta (2→1 line:
  `Образцовый текст — в разделе H (154 знаков)`). 13 entries
  affected (1, 31, 32, 33, 37, 60, 79, 81, 87, 119, 123, 126,
  150). Result: keys flow ends y=2428, zero overflow. E-keys
  #139/#140 stay two lines (keys themselves untouched, as in fr).
  #39/#133/#134 stay two lines (long Japanese stems, as in de).
  #132 stays two lines (candidate still 2 lines after shortening;
  left as-is — enough slack was already saved).
- F2 (pre-build, no run needed): the P7 disclosure was written at
  5 lines from the start (167 chars, wrap-verified 5 lines; single
  VOL.5 mention, as in de); the P1 word gloss was written short
  from the start (2 lines, wrap-verified at 19px sans / 422.5px),
  so neither the pt F2 occlusion nor a P7 teaser overflow ever
  occurred. Teaser ends 2525.62 — the best margin of the four
  editions built this baton.
- Map accounting: `map-ru.json` 221 map keys + 6 instr + meta;
  same 221-key set as map-en (asserted by `build-map-ru.py`).
  Wrestler names use standard Russian transliteration (Оносато,
  Хосёрю, Фудзирёга, Ёсинофудзи, Чура-но-уми — corrected in fix1
  §11 F3; the pre-fix1 forms Фудзирюга / Уми-но-уми were wrong
  readings, see proof1 D1); Тори-но-ити / Ни-но-тори / кумадэ
  reuse the W46 ru forms. Gloss prefix `Пояснение — ` and page
  line `Страница N из 8` reuse the W46 ru KIT conventions; the
  P8 separator is `— Страница {pg} —` (title case, matching the
  W47 siblings, where W46 used all-caps `— СТРАНИЦА N —`).
- F3 (fix1, proof1 (b) defects D1–D4, 2026-11-11): 8 map values in
  `map-ru.json` changed, re-apply (`apply.py ru`, 3rd run green),
  full rebuild + full gate re-run (see §7/§8):
  D1 (serious, 6 rendered sites, 5 map values) — 美ノ海
  `Уми-но-уми` → `Чура-но-уми` (#48 note); 藤凌駕 `Фудзирюга`
  → `Фудзирёга` / `Фудзирёги` / `Фудзирёге` by case (#49/#54/#63/
  #111/#116; the #54/#111 pair shares one map value). Evidence:
  凌=りょう (Fujiryōga in all 7 Latin editions), 美ノ海=
  ちゅらのうみ (琉球新報, Daily Sports). D2 — P8 H bridge
  `единственно правильного` → `единственного правильного`
  (genitive agreement, meta `p8_bridge`). D3 — #86 note
  `Прогноз Японии` → `Прогноз Японской метеорологической
  ассоциации` (institution name restored, as en/fr). D4 — P7
  clinic #4 `Оканчивайте глагол формой ます.` → `Глагол должен
  оканчиваться формой ます.` (natural Russian; now wraps to 2
  lines inside the clinic box, geometry still 0 flags).
  Incidental find during re-apply: core-ja had meanwhile fixed
  `一之富士` → `义之富士` (content34.py:186, #47 note), so the
  old map key `首日战胜大之里的是一之富士` no longer occurred
  in the core and the first re-apply left the note untranslated
  (Chinese literal in the Russian edition) — the map KEY was
  updated to `首日战胜大之里的义之富士` (value unchanged:
  `Ёсинофудзи победил Оносато в 1-й день`); 2nd re-apply green,
  221 keys intact, no Chinese residue. All fix1 gate logs in
  `hidden_files/w47/scratch-fix-ja-ru1/` (FIX-LOG.md,
  GATE-LOG.md, apply/build/render/webpdf/export logs, freeze
  SHAs, occlusion/p8 JSONs, print/web text layers).
  One transient EDQUOT during page-render staging: concurrent
  sibling renders spiked the shared quota; small writes still
  worked, retry to /tmp succeeded — no files deleted, no work
  lost.

- Fix round (2026-11-12, D1 romaji fix; see §8 fix subsection for gates + SHAs): D1 `ryuuryuu` → `rikuryuu` in `content7.py` + `content56.py` (5×, P7 gloss + P8 answers 66/77/80/105). Full rebuild + re-gates; print/web/text.md re-synced with new SHAs recorded in §8.

## §12 fix-xru — Latin font routing (2026-11-12; this build supersedes the §8 D1 deliverables)

- Fix (`svglib.py` only, this edition's own copy; patch applied by the previous worker, verified in place before rebuilding — marker `[removed 2026-11-12 fix-xru]` present): the `_D5_READER == "ru"` branch that routed Latin text to Noto Sans CJK was removed; the edition now always takes the else logic (Latin → Newsreader, Cyrillic → Noto Sans), per SOP §1.1. No content, no `text.md`, no other file changed by the fix itself.
- Build: `bash driver.sh ja` (`hidden_files/w47/scratch-fix-xru-w47/`), run.py rc=0 TOTAL 150, 0 FLOW OVERFLOW / 0 HEAD TOO WIDE, probe rc=0, render.py rc=0 (no retry), text-layer multiset gate IDENTICAL (21,342 non-space chars pre/post), webpdf.py rc=0. Logs: `scratch-fix-xru-w47/logs/ja-{run,probe,render,webpdf}.log`, `summary-ja.txt`.
- Probe (before → after): LAT@NotoSans 464 → **0**; LAT@Newsreader 433 → 897; CYR@NotoSans 3925 → 3925 (unchanged); CYR@Newsreader 0 → 0; CJK+CYR 732 → 732 (unchanged); runs 3982 → 4556.
- Deliverables (this build; §8 D1 SHAs retained for the record):
  - Print PDF: `Lucerna-VOL4-JA-RU.pdf` — 25,898,158 bytes, 8 pages, sha256 `44d884ac6b543a6be3f4186ffe8ce22899a5ba90bc1f951539e0a3176af822a4` (was 25,970,343 bytes, `04b2f315e267d8cf665f07da2c45cf64b80e3ae9f17e8bd8babff6c714636510`)
  - Web PDF: `Lucerna-VOL4-JA-RU-web.pdf` — 4,469,712 bytes (< 7 MB), 8 pages, sha256 `d130ae325fedb8325a724aef3ee3889b1db01c9ee0d5091b74644a9ab388dbd5` (was 4,540,808 bytes, `0726eda64903e4b765ef25b3d759b96e806fed13b076e4b13e89108e4c957f8d`)
  - Text export: `2026-w47-ja-ru.text.md` — 53,004 bytes, sha256 `f934bcf1d9f4611d094ed6f55a1f76fc8da74663cfe647c9fed17025af3d4eec` — UNCHANGED.
- All 8 SVGs differ from pre-fix (verified manually with `sha256sum -c` against `scratch-fix-xru-w47/pre-svg/`; the driver's own "SVG diff vs pre" step mis-fires because it runs `sha256sum -c` from inside `svg/` against `svg/`-prefixed paths — diagnostic only, build unaffected).
- No commit, no push, no lint (per task). Core-ja untouched; no other edition touched.
