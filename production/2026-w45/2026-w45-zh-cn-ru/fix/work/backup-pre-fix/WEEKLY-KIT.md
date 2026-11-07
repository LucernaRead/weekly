# WEEKLY-KIT — Lucerna 简体中文周报 VOL.2 · 俄语讲解版 (W45 zh-cn × ru)

## Identity and spec

- **Issue week:** Monday 2026-11-02 to Sunday 2026-11-08 (magazine model).
  Issue number: VOL.2, the second Simplified Chinese issue.
- **Pairing:** zh-cn × ru — Simplified Chinese body text (frozen W45 core)
  with a Russian explanation layer, the edition for Russian-speaking
  readers. Slug: `2026-w45-zh-cn-ru`.
- **Masthead:** bare `Lucerna` in blackletter (UnifrakturMaguntia). Chinese
  is article-less per the SOP, so there is no article.
- **Format:** 8 pages, 1950×2700 px, 4 columns, warm ivory paper `#f7f1e2`,
  deep olive accents. A2→B2 ramp; every exercise individually level-badged.
  One unified numbering sequence, 1–150, no gaps or duplicates; P8 answer
  keys are generated from the exercise registry.
- **Native Simplified Chinese:** written natively from the mainland-China
  ecosystem in the core. This edition does NOT convert or transcode
  anything between scripts: the target text stays Simplified exactly as
  in the core (freeze diff `--strict-cjk`: added CJK = 0 on all 8 pages).
  It is NOT a Traditional edition.
- **Status:** builder self-check complete (see “Builder's proof log”
  below). This is a builder handoff, NOT a finalisation claim —
  independent proofreading is still owed by the coordinator line. No
  Discord delivery, no main-chat card/PDF delivery, no cron, no repo
  push, no weekly-git touch was done by this builder.

## Contents, page by page (inherited from the core; only the explanation layer changed)

| Page | Section | Level | Exercises | Content |
|---|---|---|---|---|
| 1 | 头版 Top story (A2) | A2 | 10 (1–10) | Lead: Double 11 still running × Start of Winter on Saturday. This-week calendar box, contents, word of the week 「立冬」, parcel-locker photo, briefs, quick quiz. |
| 2 | 生活 Life (A2) | A2 15 / B1 3 | 18 (11–28) | Double 11 shopping life + Start-of-Winter life. Practice example (sweater 240 + scarf 80 = 320, direct cut 50 → payable 270). Shopping word cards 现货 / 直降 / 立减 / 补冬. Autumn-valley photo. |
| 3 | 文化 Culture (A2→B1) | A2 15 / B1 3 | 18 (29–46) | Start of Winter feature (19th solar term, 17:52 moment, three micro-seasons, regional food differences, uneven cooling, Journalists' Day paragraph). Frost + dumpling photos. |
| 4 | 体育 Sport (B1) | B1 | 18 (47–64) | S16 feature (AL out, IG/TES/BLG chasing the quarter-finals, Swiss format, fourth-round preview, 2026-10-27 cutoff stated on the page, final Beijing 2026-11-15 03:00). S16 schedule box. LAN-party file photo. |
| 5 | 青年 Youth (B1) | A2 1 / B1 17 | 18 (65–82) | AI film 《三星堆：未来往事》 + Start-of-Winter new film 《我们仅有一次的人生》. Popcorn photo. Film-dates box. |
| 6 | 深读 Deep read (B2) | B2 | 18 (83–100) | Double 11 deep read (why the rules got simpler; “lowest price” claims checked against the checkout page, delivery cost, returns rules). Practice-data bar chart only. |
| 7 | 词语精讲 Language focus (A2/B1/B2 columns + error clinic + sentence frame + readers' corner + phrases + VOL.3 teaser) | A2 4 / B1 4 / B2 4 | 12 (101–112) | A2 shopping/winter words; B1 time-and-date order (big → small); B2 reading news (说法 / 数据 / 广告); error clinic (的/地/得, measure-word order, date order); frame 先…再…; readers' corner (see below); 8 phrases; VOL.3 teaser. |
| 8 | 测验与答案 Test & keys | A2 11 / B1 24 / B2 3 | 38 (113–150) | A true/false (8) + B big quiz (10) + C complete-the-sentence (10) + D read-and-answer passage about Xiao Hong in Beijing (6) + E in-conversation (3) + F writing (1). Then all 150 answer keys with brief Russian notes, grouped by page with “— СТРАНИЦА N —” headers for pages 1–8. Writing topic 《我的立冬周末》, 120–180 characters; model answer programmatically counted at 172 characters. |

## Measured totals

- **Exercises: 150 total** — A2 56 · B1 69 · B2 25. By page: 10 / 18 / 18 /
  18 / 18 / 18 / 12 / 38. By type: 完成句子 68 · 单选 50 · 词汇配对 20 ·
  完形单选 11 · 写作 1. Identical to the core registry (verified in the
  single-process driver log: TOTAL 150, same levels/pages/types).
- **Writing model:** 172 characters (unchanged, frozen Chinese text).
- **P6 practice chart** (cols 0–2): rows A 毛衣+围巾 270 yuan, B 耳机
  179 yuan, C 书+本子 160 yuan; bars drawn from zero at exactly 3.0 px per
  yuan, i.e. widths 810 / 537 / 480 px, starting at x = 325 — rects and
  label positions/text verified byte-identical to the core SVG.
- **Files:** 8 SVGs in `svg/`, 8 full-page PNG cards at 1950×2700 in
  `cards/`, print PDF `Lucerna-VOL2.pdf` (38,103,379 bytes, 8 pages,
  sha256 `a938d5a679a88bc675d347ab60644fd0bcc41ac7d73c3f4584610843176190c1`),
  web PDF `Lucerna-VOL2-web.pdf` (3,252,467 bytes, 8 pages, JPEG pages
  q85 @1400 px — under the 10 MB ceiling, sha256
  `cf7fbef3ebbd30392abbd847250a22464d043db5da150841b98459f9fe7db634`).
- **Phrases of the week (P7):** 8 phrases, each verbatim from this issue's
  own articles, with Russian translations and (Страница N) tags:
  「不用等11月11日」 p. 1; 「下单就能发货」 p. 2; 「先看结算页,再付款」 p. 2;
  「水开始结冰」 p. 3; 「三场都输了」 p. 4; 「小局一场没赢」 p. 4;
  「故事够不够好」 p. 5; 「别以后,就现在」 p. 5.

## Furniture three-way (core EN · W43 same-pairing RU · this edition)

All furniture strings below were copied VERBATIM from the shipped W43
same-pairing edition (`files/weekly-report-zh-cn-ru/`, SVG-verified),
except VOL.1 → VOL.2. The W43 zh-cn fan-outs live under hyphenated
`files/weekly-report-zh-cn-ru/` (not unhyphenated `zhcn`).

| Element | Core (zh-cn × en) | W43 zh-cn × ru (shipped) | This edition (W45 zh-cn × ru) |
|---|---|---|---|
| P1 badge | 简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers (19.5pt, olive) | ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ (19.5pt, BRICK) | Same as W43, verbatim (19.5pt, BRICK) |
| Badge slot/size case | (975, 434), 19.5pt | (975, 434), 19.5pt, weight 700, fill #a4553a | Same slot/size as W43 shipped SVG, measured from that SVG. Family case: the zh-cn core's y=372 is the FROZEN bilingual strapline (给学中文的人的周报 — …), so the badge does NOT take the subtitle slot (unlike the EN core family); it sits at y=434 below the rules, exactly as in W43 zh-cn × ru and as noted from the zh-cn × nl build. The core's own badge is also at (975, 434), 19.5pt (olive) — slot identical, only colour/text change. |
| P1 top line | 每周读中文 · Read real Chinese, every week | 每周读中文 · Читайте настоящий китайский — каждую неделю | Same as W43, verbatim |
| P1 subtitle (y=372) | 给学中文的人的周报 — Read the real China, in Chinese | 给学中文的人的周报 — Настоящий Китай — по-китайски | Same as W43, verbatim |
| Footer left | Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations | Lucerna · КИТАЙСКИЙ (УПРОЩЁННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.1 · ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ | W43 form with VOL.2: Lucerna · КИТАЙСКИЙ (УПРОЩЁННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ |
| Page line | 第 N 版 / 共 8 版 | Страница N из 8 | Same as W43, verbatim |
| Gloss prefix (bslib4 `gloss()`) | Notes｜ | Пояснение — | Same as W43, verbatim |
| P8 separators | — Page N — | — СТРАНИЦА N — | Same as W43, verbatim |
| P8 note style | Dash: `N. key — note`, writing `N. ✓ note` (verified from the core's own build code `content8.py` keys generation, NOT from memory) | Dash, same (W43 KIT §6) | Dash, unchanged code path (README #8/#14: keep the family's style; the code line is byte-identical to the core's) |
| Section heads | Chinese · English (e.g. 生活 · Life, 词语填空 · Word blanks) | Chinese · Russian (e.g. 生活 · Жизнь, 词语填空 · Впишите слово) | W43 Russian head forms reused where the Chinese head matches (Жизнь / Культура / Спорт / Молодёжь / Глубокое чтение / Языковой фокус / Тест и ответы; Выбор ответа / Впишите слово / Числа и даты / Сопоставьте пары; Верно или неверно / Большой опрос / Закончите фразы / Читаем и отвечаем / В разговоре / Письмо); new heads translated in the same short style (Главная тема, Сразу к практике, Содержание, Слово недели, Коротко, Быстрый опрос, Слова для покупок, Упражнения, Расписание S16, Слова матча, Даты фильмов, Главное, Три вопроса, Учебные корзины, Покупки, Время и даты, Читаем новости, Клиника ошибок, Конструкция недели, Уголок читателей, Фразы недели, На следующей неделе (VOL.3)) |
| Instr labels | Fill in the blank / Fill in / Match the words / Writing | Впишите слово / Впишите / Сопоставьте / Письмо | Same mapping as W43 (blank-form → Впишите слово, bare → Впишите) |
| Photo credits | Photo: X — CC0 / Public domain (Wikimedia Commons) | Фото: X — CC0 / общественное достояние (Wikimedia Commons) | Same as W43 (only the `Photo:`/`Public domain` words localised; artist names byte-identical) |
| Bylines | Lucerna editors · Reading level A2/B1/B2/A2→B1 | Редакция Lucerna · Уровень чтения … | Same as W43 |
| Answers line | Answers on page 8 · 答案见第 8 版 | Ответы на странице 8 · 答案见第 8 版 | Same as W43 |
| P7 page tags | (p. N) | (Страница N) | Same as W43 (counts per page = core) |
| P8 keys head | 答案 · Answer keys — by page, with a note on every answer / All notes in English · ✓ = the writing task | 答案 · Ответы — по страницам, с примечанием к каждому ответу / Все примечания на русском · ✓ = письменное задание | Same as W43 |
| Writing glossline + model prefix | Writing — there is no single right answer. A N-character model follows. / Model answer: | Письмо — единственно верного ответа нет. Ниже — образец из N иероглифов. / Образец: | Same as W43 |

## Translation rules applied (family precedent, W43 zh-cn × ru KIT §5)

- Page gloss boxes keep the `pinyin 汉字 — Russian` form (e.g.
  `xiànhuò 现货 — товар в наличии, готов к отправке`); gloss item
  counts equal the core's item by item (see below).
- Registry notes (the notes printed on P8) carry tone-marked pinyin and
  NO Chinese characters, NO full-width parentheses (verified: 150/150
  notes scanned — 149 AST-extracted + the #150 f-string checked by hand —
  0 CJK, 0 full-width parens). Chinese words cited in notes were
  converted to pinyin (e.g. `立冬 is the 19th…` → `lìdōng — 19-й…`;
  `瑞士轮 = …` → `ruìshìlún = …`). Two P7 measure-word notes were
  rephrased to pinyin-only for the same rule (`jiàn` / `jiàn, а не gè
  или tiáo` — the characters remain visible in the stems/options).
- Error-clinic notes keep the particle characters 地/得/个/件: they are
  the teaching point itself (already present in the core's note strings,
  so added CJK = 0 there too), and the wrong/right example lines are
  frozen Chinese.
- Brand/team/platform names stay in Latin original (JD.com, Taobao,
  Tmall, WeChat, S16, LPL, GEN, DK, AL, IG, TES, BLG, Maoyan, Sina
  Sports); dates use the Russian form (7 ноября, в 06:00 по пекинскому
  времени); decimals in Russian prose use the comma (1,192 млн юаней in
  the shortened note form); frozen printed data keep their original
  digits unchanged.

## Gloss counts (split on `·` itself, rendered gloss() text)

| Page | Core items | This edition items |
|---|---|---|
| P1 | 4 | 4 |
| P2 | 8 | 8 |
| P3 | 6 | 6 |
| P4 | 3 | 3 |
| P5 | 6 | 6 |
| P6 | 6 | 6 |
| P7 | 0 (no gloss() boxes; glosslines only) | 0 |
| P8 | 0 | 0 |

## Readers' corner (P7) — disclosure + invitation

Inherited from the core's corner disclosure (VOL.1 promised real reader
letters and the best VOL.1 P8 writing in VOL.2; none have arrived; the
corner still prints an editor's example; deferred, not cancelled),
rendered in Russian on the page:

> Пример письма от редакции — не настоящее письмо. В VOL.1 было обещано
> напечатать здесь настоящие письма и лучшее сочинение VOL.1, но писем
> пока нет — это отсрочка, а не отмена. Присылайте ваши письма! Напишите
> два предложения по-китайски и отправьте их нам: лучшие появятся в VOL.3.

This satisfies both limbs: (a) on-page disclosure that no genuine reader
letters exist (labelled editor's example, no fabrication — the letter
itself is the core's frozen Chinese example letter, unchanged); (b) an
EXPLICIT open invitation for real letters (Присылайте ваши письма! …),
not a facts-only disclosure and not a teaser/exercise prompt. The
VOL.3 teaser promise (“还有你们的来信…”) is consistent with the
invitation. No reader, letter, name, or quotation was invented.

## Trend and fact sources (inherited from the core — not re-derived)

Full sourcing is in the core KIT
(`files/weekly-report-w45-zhcn-core/WEEKLY-KIT.md`); the facts below are
the core's, unchanged by this edition (no fact was altered in
translation):

- **Double 11:** JD.com spot sales from 20:00 2026-10-12; Taobao/Tmall
  presale from 20:00 2026-10-15, tail-payment + spot sales from 20:00
  2026-10-20; spot period to 23:59 2026-11-13; peak sale 20:00 2026-11-10
  to 24:00 2026-11-11 (next week, mentioned only as next week's event);
  WeChat shop first Double 11, 2026-10-12 to 2026-11-15 (35 days); 18th
  Double 11; trend changes: spot sales replacing presales, simpler rules
  (官方立减 / 直降 continuing, 满300减50-style receding), AI entry points
  (豆包 “买前问豆包”, Qianwen). All basket arithmetic is labelled
  practice data.
- **Start of Winter:** Saturday 2026-11-07, 17:52交节 (Beijing time), 19th
  of the 24 solar terms, first of winter; three micro-seasons
  一候水始冰 / 二候地始冻 / 三候雉入大水为蜃; customs regionally varied,
  no single national custom; cooling not simultaneous nationwide.
  (Source chain per core KIT: trend pool citing jieri8.com + Hong Kong
  Observatory 2026 almanac; not independently second-confirmed.)
- **S16:** cutoff honestly dated 2026-10-27. Venues/stages, Swiss format,
  verified results through the cutoff (LPL 0–4 round 1; 2026-10-26 IG beat
  HLE, TES beat G2, BLG beat KC, all 2–1; GEN/DK 3–0 through; AL/TSW 0–3
  out; AL lost to KC, then to TES, then 0–2 to TL on 2026-10-27),
  fourth-round draw 2026-10-29–31, quarter-finals 2026-11-04–07 06:00,
  semi-finals 2026-11-08–09 06:00, final Beijing 2026-11-15 03:00
  (Barclays Center, New York). No later Swiss result is fabricated;
  quarter-final teams are labelled not yet known at press time.
- **Films:** 《三星堆：未来往事》 released 2026-10-23, Bona, 100 minutes,
  no live actors, first domestic AI feature with a public screening
  licence; Maoyan 4-day figure ~1.192 million yuan by noon 2026-10-26,
  24–25 Oct averaging 2 viewers per screening (conflicting first-day
  figures deliberately not printed). 《我们仅有一次的人生》 nationwide
  release Saturday 2026-11-07, Sun Aoqian, Song Jia / Wen Qi, original
  title 《余烬》, Beijing International Film Festival Tiantan Award
  competition, Best Cinematography, 114 minutes, slogan “别以后，就现在”.
- **Other calendar:** 中国记者节 Sunday 2026-11-08; mid-term exams in
  some schools in early November, dates differing, not nationally
  unified.
- **Red line:** no international politics; no Chinese domestic politics
  (target country is China); no anniversary-as-trend material. The
  explanation layer introduces no politics.

## Image authorisations (inherited from the core)

6 photos, all CC0 / public domain, credit taken directly from the
Commons API Artist field, verified 2026-10-27 (core build
`assets/CREDITS.md`). Placement in the final SVGs: P1 1, P2 1, P3 2,
P4 1, P5 1, P6 0, P7 0, P8 0 — 6 photos total. Embedded payloads are the
core's asset files (copied with the build); only the `Photo:`/`Public
domain` credit words were localised to Russian.

| Page | Asset | Artist (Commons API) | Licence |
|---|---|---|---|
| 1 | locker.jpg (parcel lockers, 资料图) | Map hobby | CC0 |
| 2 | valley.jpg (autumn valley) | Paul Gilmore | CC0 |
| 3 | frost.jpg (frosted leaves) | Gerda Arendt | CC0 |
| 3 | dumplings.jpg (dumplings, 资料图) | Syced | CC0 |
| 4 | lanparty.jpg (LAN party, France 2003, file photo) | Syced | CC0 |
| 5 | popcorn.jpg (cinema popcorn bucket, 资料图) | Based5290 | Public domain |

File photos are captioned 资料图 and never presented as this week's
event; the P4 LAN-party caption states its real date (2003) and place
(France).

## Reproduction build

Build code lives in `hidden_files/weekly-report-w45-zh-cn-ru-build/`
(bslib4.py, svglib.py, run.py, render.py, content12.py, content34.py,
content56.py, content7.py, content8.py, assets/, plus `scratch/` with
the one-shot transform `transform_ru_w45.py`, the trim script
`apply_trims.py`, and the audit helpers `residual_en.py`,
`rowcheck.py` (copied from the sibling zh-cn × fr build, ED repointed),
`p8lines.py`, `p8texts.py`, `trimtest.py`, `trimtest2.py`, `checks.py`,
`purity.py`). Content modules run ONLY through the single one-process
driver; nothing was ever imported inside the core build directory, and
no core file was touched (core SVG hashes re-verified 8/8 at the end).

```bash
cd hidden_files/weekly-report-w45-zh-cn-ru-build
../../tools/venv/bin/python run.py        # single-process driver
../../tools/venv/bin/python render.py     # svg -> cards PNG -> print + web PDF
cd ../../tools
./venv/bin/python freeze.py baseline --build ../hidden_files/weekly-report-w45-zh-cn-ru-build \
    --core-svg ../files/weekly-report-w45-zhcn-core/svg --out scratch/baseline-w45-zh-cn-ru
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-zhcn-core/svg \
    --edition-svg ../files/weekly-report-w45-zh-cn-ru/svg --strict-cjk \
    --json ../hidden_files/w45-zh-cn-ru-diff.json
./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-zhcn-core \
    --edition-dir ../files/weekly-report-w45-zh-cn-ru --target zh-cn
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-zh-cn-ru \
    --core ../files/weekly-report-w45-zhcn-core --json ../hidden_files/w45-zh-cn-ru-occlusion.json
./venv/bin/python ../hidden_files/weekly-report-w45-zh-cn-ru-build/scratch/rowcheck.py
```

Toolchain (measured): `tools/venv/bin/python` = Python 3.12.3, PIL 13.0.0.
`run.py` and `svglib.py` are byte-identical to the core's; `bslib4.py`
differs in exactly 3 lines (footer left, footer right, gloss prefix);
`render.py` differs only in its BASE path. All other build diffs are
explanation-layer strings, instr labels, the OUT path, or the single
#150 device key below.

## Registry key difference (core vs this edition)

Exactly ONE registry key differs, and it is a device item (same category
as W43 zh-cn × ru KIT §4):

| # | Core key | This edition key | Category |
|---|---|---|---|
| 150 | (开放题，范文如下) | (открытый вопрос — образец ниже) | Device item (open-task marker translation) |

Its note is likewise translated (core: “Open task - the model answer is
printed in section F above (172 characters)” → “Открытый вопрос —
образец напечатан выше, в разделе F (172 иероглифов)”). The other 149
keys are byte-identical to the core (verified by build diff: the only
key-arg change in the whole build diff is #150; stems/options/article
paragraphs/captions are untouched — changed diff lines are explanation
strings or instr labels only). The printed P8 key set is EQUAL
(`p8.py compare`: CLEAN, keydiff []).

## Builder's proof log (self-check, final render)

- **Baseline (STEP 1, before any change):** `freeze.py baseline` on the
  unmodified copy: **8/8 byte-identical** reproduction of the core's
  shipped SVGs; core SVGs re-hashed unchanged after the run. (One
  self-inflicted false start: the first baseline `--out` was nested
  inside the build dir, which made `copytree` recurse; it was deleted
  and re-run with `--out` in `tools/scratch/` — no core or edition file
  was affected.)
- **Freeze diff (final render):** per page +strings/−strings and CJK
  core→edition: P1 851→820, P2 1053→1031, P3 812→790, P4 810→789,
  P5 944→922, P6 1005→983, P7 760→647, P8 1102→985; **added CJK = 0 on
  every page, total 0** (`--strict-cjk` gate passes). Removed-CJK
  strings were audited: every one is a bilingual furniture string, a
  gloss line, an English explanation sentence citing Chinese words, or
  the P7 Chinese disclosure text replaced by its Russian version — no
  article sentence, stem, option, or caption is among them. P7's larger
  drop (113) is the Chinese disclosure paragraph translated to Russian.
- **P8:** `p8.py compare`: **CLEAN** — core 150 noted, edition 150
  noted, missing [], extra 0, keydiff [].
- **Geometry:** `occlusion_audit.py` (selftest OK, all 6 planted classes
  fire, clean controls silent): **0 flags, NEW vs core 0** on the final
  SVGs. Same-baseline ink-collision scan (`scratch/rowcheck.py`, true
  ink boxes): **0 flags**. P6 chart-label element check: bars
  810/537/480 px at x=325 and all six labels identical to the core in
  position and text. **0 FLOW OVERFLOW / 0 HEAD TOO WIDE** warnings in
  the final driver log.
- **Notes purity:** 150/150 registry notes contain Cyrillic (Russian) or
  pinyin; 0 contain Chinese characters; 0 contain full-width
  parentheses (see “Translation rules” for the two measure-word notes
  rephrased to pinyin-only).
- **English residue:** visible-text scan of the final SVGs for English
  explanation words (the/and/page/Nov/Oct/English/Notes/Photo/Fill/
  Match/Read/Choose/Answers/…) returns **zero hits**; remaining Latin
  is frozen brands (JD.com, Taobao, Tmall, S16, LPL, Maoyan), pinyin,
  option letters, and level codes.
- **Visual check:** all 8 final cards read in full (P1–P8) — masthead
  furniture, badge, footers, gloss boxes, photos + credits, schedule
  and chart, clinic/frame/readers'-corner boxes, phrases, teaser band,
  test sections, and the full keys area are clean: no overflow, no
  overlap, no footer intrusion. P8 keys end well above the footer line;
  P7 teaser ends at y = 2555.6, above the 2580 footer line (core:
  2554.1).
- **Core integrity (final):** core SVG sha256 re-verified 8/8 against
  the pre-build hashes (`core-svg-hashes-before.txt` in the build dir).

## Pre-fix baselines and fixes (each followed by a full re-render, never patched in output)

1. **P1 BOXTITLE (occlusion audit, NEW vs core = 1):** the translated
   calendar-box line “Команды S16 зависят от швейцарского этапа” had
   right ink 1892.2 > box border 1885.0. Per README #15 (a fan-out's own
   text must be shortened even when the core shows an analogous shape),
   shortened to “Команды S16 зависят от этапа” (the box's own note above
   already names the Swiss stage). Re-audit: 0 flags, NEW 0.
2. **P7 teaser overflow (first full render):** the first Russian
   disclosure pushed col3_end to 2021.2 and the teaser end to 2867.2
   (past the page). Fixed by shortening the disclosure to its current
   form plus wrap-tested one-line clinic/frame trims (clinic notes 1, 2,
   4 and the frame note, each verified with `wrap()` to drop exactly
   one line; facts/rules unchanged). Final: col3_end 1709.6, teaser
   ends 2555.6.
3. **P8 keys FLOW OVERFLOW (first full render):** Russian notes wrapped
   to more lines than the English notes (35 multi-line keys vs the
   core's ~11 true multi-liners; the raw count was inflated by
   page-header attribution artefacts, adjudicated line by line).
   Fixed W43-style by tersening 24+ note wordings (each wrap-tested at
   13.3pt/434 px to drop exactly one line; facts, keys, and levels
   untouched — e.g. “Четвертьфиналы начинаются…” → “Четвертьфиналы —…”,
   “К полудню 26 октября Maoyan показывал около 1,192 миллиона юаней.”
   → “Maoyan к полудню 26 октября: около 1,192 млн юаней.”).
   Final: 0 overflow warnings, keys end inside the page.
4. **Notes CJK × 2 (purity scan):** two P7 measure-word notes still
   contained 件/个/条; rephrased to pinyin-only (`jiàn` /
   `jiàn, а не gè или tiáo`). Final: 0 CJK, 0 full-width parens.
5. **P6 C head (pre-render measurement):** “Считаем корзины” measured
   489.8 px > 434 px column at 25pt (HEAD TOO WIDE risk), so the head
   ships as “Считаем” (372.0 px); the Chinese head already says
   练习篮子算一算. No warning in the final log.
6. **Missed head (residual scan):** P4 section C “Schedule work” was
   initially untranslated; caught by the bilingual-head scan and
   translated to “Читаем расписание” (415.9 px at 25pt, fits).

## Adjudications and shortfalls (for the independent proofreader)

- **P7 disclosure length vs the core's:** the Russian disclosure is
  shorter than the core's Chinese+English disclosure (the core prints
  the disclosure in two languages; this edition prints it once, in
  Russian, plus the explicit invitation). Content is inherited, not
  abridged in substance: VOL.1 promise, none arrived, editor's example,
  deferred-not-cancelled, invitation.
- **“Команды S16 зависят от этапа”:** the shortened calendar line drops
  the word “швейцарского”; the full term appears in the same box's
  note directly above, so no information is lost on the page.
- **“млн” abbreviation:** used once in a shortened P8 note (#67/#126)
  to fit one line; standard Russian abbreviation, same figure.
- **“южное блюдо” (tangyuan note):** shortened from “eaten in some
  southern places”; the stem already says 南方有的地方吃___, so the
  southern link is preserved on the page.
- **Start of Winter 17:52 source chain and S16 cutoff:** inherited from
  the core KIT without re-verification (see “Trend and fact sources”);
  the proofreader should apply the core's own caveats.
- **Traditional-character scan:** not separately run for this edition
  because the target text is byte-identical to the core (added CJK = 0
  is the stronger gate); the core's own scan (no traditional-only
  characters) therefore carries over.
- **What this builder did NOT do:** no independent proofread claim, no
  repo insert, no Discord delivery, no main-chat delivery, no cron, no
  weekly-git touch, no subagent spawned. The edition awaits the
  coordinator's independent proofread.
