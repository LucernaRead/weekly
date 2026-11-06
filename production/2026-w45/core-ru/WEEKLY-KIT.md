# WEEKLY-KIT — Lucerna Russian Weekly, VOL.2 (W45 core)

## 1. Spec

- **Edition:** Русский (Russian) target-language core, VOL.2.
- **Issue week:** Monday 2 November – Sunday 8 November 2026. **Issue date:** Monday 2 November 2026.
- **Pairing:** target language Russian × reader native language Simplified Chinese (zh-cn).
  Masthead carries no article (Russian is article-less per `tools/tables.py`): masthead is
  `Lucerna`; the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 俄语正文 · 中文讲解`;
  the footer on every page reads `Lucerna · 俄语周报 VOL.2 · LUCERNA RUSSIAN WEEKLY`
  and the page number in Chinese (`第 N 版 / 共 8 版`).
- **Explanation-layer convention (same as the W43 RU core):** all explanation is in
  Simplified Chinese — glosses, exercise instructions, answer notes, section furniture
  and footers. Russian is the only target-language text. This core IS the zh-cn edition
  for abstract purposes, so `ABSTRACT.txt` is one Simplified Chinese line (see §8).
- **Format:** 8 pages (multiple of 4), 1950×2700 px per page, 4 columns, warm ivory
  paper, dark olive-green accents. Pipeline: Python → SVG → CairoSVG → PNG/PDF
  (the W43 RU pipeline, reused unchanged in structure).
- **Exercises:** **150 total, continuously numbered 1–150**, registered in code and
  rendered as the P8 answer key. By page: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18,
  P7 12, P8 38. By level: A2 51, B1 75, B2 24. By type: 完成句子 54, 单选 42,
  词汇配对 20, 完形单选 13, 造句 12, 句型转换 4, 翻译 4, 写作 1.
  P8 model writing text (“Моя неделя с праздником посреди недели”) = **84 words**
  (brief: 80–100).
- **P7 golden sentences:** 8 sentences, each occurring exactly twice in the issue —
  once in its own article, once in the P7 “ФРАЗЫ НЕДЕЛИ” list (verified
  programmatically on page-joined SVG text, §7). All 8 come from this issue's own
  articles: P1 ×2, P2 ×1, P3 ×1, P4 ×1, P5 ×1, P6 ×2.
- **No invented facts.** No standings are printed (the trend pool gives none). No
  invented poll, quote or account data. The P6 “week plans” chart is labeled
  practice data (УЧЕБНЫЕ ДАННЫЕ + “not real statistics” line) and sums to 100%
  (34/28/22/16) with proportional bars.

## 2. Content per page

- **P1 · Первая (A2) — “Одна среда посреди недели”.** Lead: the split week — the
  lone Wednesday holiday, the shortened Tuesday, school-holiday tail, the 11.11
  sale running through the week, RPL round 14 at the weekend. Media-topics box,
  contents, “НЕДЕЛЯ В ЦИФРАХ” box, word of the week “сокращённый день”,
  November-park photo, “последние дни каникул” box, blitz quiz (ex. 7–10).
- **P2 · Жизнь (A2) — “Вторник короче на час”.** The one-hour-shorter Tuesday rule,
  what changes from 1 November (described only generically: taxes, rentals,
  payments; pension payments due 4 November arrive 3 November because of the
  holiday), a “прошлая неделя” report box (derby result, failed snow forecast,
  28 October Grandparents Day, 31 October Halloween — all reports, never previews),
  a “А вы?” letter call for VOL.3, weather-word strip (ex. 11–28).
- **P3 · Культура (A2→B1) — “4 ноября: один день праздника”.** Unity Day as an
  everyday-life holiday (one background sentence only: the holiday appeared in
  2005 and recalls the 1612 events — background, never a commemorative lead),
  “среда в городе” (fairs and concerts), facts/ideas boxes (ex. 29–46).
- **P4 · Спорт (B1) — “14-й тур: последний перед паузой”.** RPL round 14 preview:
  full fixtures table (6 Nov Локомотив–Рубин; 7 Nov Краснодар–ЦСКА 19:30 MSK at
  Ozon Арена; 8 Nov Спартак–Акрон 16:15, Зенит–Ростов, Крылья Советов–Оренбург),
  1912 football photo, “тур в цифрах” box, round-13 closer on Mon 2 Nov
  (Крылья Советов–Зенит 18:00) and the post-round pause until 20 Nov (ex. 47–64).
- **P5 · Молодёжь (B1) — “11.11: как покупать умно”.** Consumer angle only:
  promo codes, list-first shopping, price-checking. The trade-press note is
  attributed (“торговая пресса пишет: скидок может быть меньше, а выбор — уже”)
  and never stated as a bare verified fact; no warehouse-fire cause discussion.
  Market photo, “11.11 в цифрах” box (ex. 65–82).
- **P6 · Разбор (B2) — “Неделя с праздником посреди: как её прожить”.**
  Leave-bridging (Thursday+Friday off), day-trip and stay-home strategies,
  2–8 November day strip (light = work days 2/5/6, yellow = short Tuesday 3 +
  weekend 7/8, pink = holiday 4), pro/contra box, labeled practice chart
  (ex. 83–100).
- **P7 · Язык (A2/B1/B2 + error clinic + word box + readers' corner + golden
  sentences + VOL.3 teaser) (ex. 101–112).** Three level columns (week words,
  shopping words, attribution/hedging), four-clinic error box, word of the week
  “промокод”, readers' corner (see §6), 8 golden sentences with page references,
  teaser: 11 November sale day, round-14 results, readers' letters.
- **P8 · Тест (ex. 113–150 + all 150 keys).** A chronicle cloze 8, B general
  questions 8, C reading about Маша 4, D sentence building 4, E RU↔ZH translation
  4, F word matching 4, G shop-dialogue cloze 5, H writing 1 + 84-word model.
  Key spot-checks re-derived against stems/articles: P2 D 25–28 = c/d/a/b,
  P3 C 39–42 = b/d/a/c, P4 C 57–60 = b/a/c/d, P5 C 75–78 = d/a/c/b,
  P8 F 141–144 = d/a/c/b. All 150 keys present in the rendered P8 (131 letter
  answers + 19 number/word answers).

## 3. Trend / fact sources (all in-week or just-passed reports)

- **Trend pool:** `hidden_files/w45/trend-batch-C.md` (RU section), researched
  2026-10-26. Lead topics follow it exactly: split week, Ozon 11.11 sale
  (22 Oct – 12 Nov 2026), RPL round 14 (6–8 Nov) as the last round before the
  November break.
- **Derby result (verified 2026-10-26, two independent web sources):** ЦСКА beat
  «Спартак» 2:0 on Sunday 25 October 2026 (matips.net H2H table: 25-10-2026,
  CSKA 2-0, HT 2-0; Sportradar match record: winner CSKA Moscow 2-0, goals
  Kirill Glebov 1′, Tamerlan Musaev header 24′). Printed as ЦСКА–«Спартак» 2:0,
  both goals in the first half, scorers Glebov and Musaev.
- **First snow (verified 2026-10-26, weather.com Moscow 10-day page):** first snow
  did NOT fall in Moscow in the forecast window; 26 October 2026 in Moscow was
  +12 °C and fair. Printed honestly as a failed forecast (“Прогнозы не сбылись”).
- **28 October / 31 October:** passed calendar dates only, no invented
  attendance/detail claims. 28 Oct = Wednesday, 31 Oct = Saturday, 25 Oct =
  Sunday (verified with `date -d`).
- **Weekdays (verified with `date -d`, Europe/Moscow):** 2 Nov Mon, 3 Nov Tue,
  4 Nov Wed, 5 Nov Thu, 6 Nov Fri, 7 Nov Sat, 8 Nov Sun.
- **Sale/stock attribution:** Ozon 11.11 sale 22 Oct – 12 Nov 2026 (Ozon
  announcement via vc.ru, Oct 2026); sellers publicly disputing new promo rules
  (appeal to ФАС/Минпромторг dated 15 Oct 2026, reported by Коммерсантъ via
  vc.ru); Retail.ru 26 Oct 2026 (citing Forbes + Data Insight) reporting
  sellers scaling back November sales. Printed only in the attributed form
  above. The sanctions/“peace talks” market story and November international
  friendlies were NOT used (geopolitics / outside the week).
- **W43 promises honored:** school-holiday tail Mon 2 – Wed 4 Nov (holidays end
  4 Nov) is live in-week; derby / first snow / 28 Oct / 31 Oct are reports only.
- **Editorial red lines observed:** no international politics, wars or
  geopolitics anywhere; Russian domestic life/culture/sport only; Unity Day is
  presented as everyday life, not as commemoration.

## 4. Images (public-domain / CC0 only; credit from the Wikimedia Commons API Artist field)

- **P1 November park photo** (`autumn_path.jpg`, reused from the W43 build):
  Toxer427, CC0, Wikimedia Commons. Captioned as a November park scene.
- **P4 1912 football photo** (`football1912.jpg`, reused from the W43 build):
  Russia 1912 Olympics squad, unknown author, public domain.
- **P5 market photo** (`market.jpg`, downloaded 2026-10-26 via Commons
  Special:FilePath, verified JPEG 1920×1280): USDA farmers-market stand photo,
  Artist field Preston Keres (USDA), usage terms Public Domain
  (“Please credit: USDA Photo by Preston Keres”). Captioned honestly as a
  market scene, NOT claimed to be Moscow.

## 5. Build / reproduce

Build code (new, copied from the W43 RU build and repointed):
`hidden_files/weekly-report-w45-ru-build/` — `content12.py` (P1+P2),
`content34.py` (P3+P4), `content56.py` (P5+P6), `content7.py` (P7),
`content8.py` (P8 + registry). One process only (never run content modules
standalone):

```
cd hidden_files/weekly-report-w45-ru-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py
```

Outputs in this dir: `svg/` (8 SVGs), `cards/` (8 page PNGs),
`Lucerna-VOL2.pdf` (23,191,026 bytes, print), `Lucerna-VOL2-web.pdf`
(3,035,942 bytes, web, under the 10 MB Discord server limit).
Final build: zero FLOW OVERFLOW / HEAD TOO WIDE warnings; TOTAL 150;
model words 84.

## 6. Readers' corner — no fabrication (on-page disclosure, not KIT-only)

No real reader, letter, name or quote is fabricated. P7 prints a clearly labeled
editor's example (“— М. (пример от редакции)”) AND an on-page disclosure in
Russian and in Chinese stating plainly that no real reader letters or best P8
texts had arrived by press time, so the example stands and the W43 promise
carries to VOL.3. The disclosure is rendered inside the letters box on P7
(verified visually: box fully inside its border, clear of the “ФРАЗЫ НЕДЕЛИ”
rule). The VOL.3 teaser repeats the call for letters.

## 7. Self-proofread record (full pass over rendered pages, 2026-10-26)

- **P1–P8 read in full on the rendered cards.** P2, P3, P4, P6, P8 clean on first
  pass except as noted below; P1, P5, P7 defects found and fixed (see below).
- **Defects found and fixed (all re-rendered and re-verified):**
  1. P1 contents box: all 7 rows printed on one baseline (missing line increment
     in the contents loop) — fixed; rows now read cleanly.
  2. P1 word-of-the-week Chinese line wrapped with a lone “。” — shortened to
     “сокращённый день = 缩短的工作日。” (1 line, wrap-verified).
  3. P5 gloss orphans (2): first gloss wrapped with “）。” alone; second gloss
     wrapped with “。” alone — both reworded and wrap-verified (first gloss now
     ends “· хватает 抓取。” on its second line, a list-separator line of the
     same class the W43 core's independent proofread kept).
  4. P7 A2 bridge wrapped with a lone “假。” — reworded to a clean two-line
     break (“выходной 休息日；будни 工作日；/ сокращённый день 缩短工作日。”).
  5. P7 readers'-corner box overflowed its border over the “ФРАЗЫ НЕДЕЛИ”
     heading — box contents shortened and the phrases section moved down
     (rule now at y=1756, box ends 1727.58, 28 units clear); verified visually.
  6. P2 exercises gold rule struck through the descenders of the “Запомните:”
     line (LINEX, confirmed on a pixel crop) — exercises block moved down 32
     units; rule now clearly clear of the text (verified on a second crop).
  7. P1 numbers box wrapped with a lone “）” — parenthetical shortened to
     “（11月3日短一小时）” (wrap-verified, visually confirmed).
  8. Golden-sentence count: one sentence occurred 3× (identical sentence in
     both the P1 and P2 leads + P7). P1's instance reworded (“день короче на
     час”); all 8 sentences now occur exactly 2× (article + P7), verified on
     page-joined SVG text.
- **Programmatic checks after the final build (all pass):**
  - Golden sentences: 8/8 exactly 2×, each on its article page + P7.
  - Orphan scan: zero SVG text lines beginning with closing CJK punctuation.
  - P8 keys: all 150 present in the rendered P8 (131 letter + 19 number/word).
  - Match sets re-derived: 25–28 c/d/a/b, 39–42 b/d/a/c, 57–60 b/a/c/d,
    75–78 d/a/c/b, 141–144 d/a/c/b.
  - Gloss check: every gloss headword occurs on its own page (stem match).
  - Same-baseline scan: one crude-width flag on P8 (key 82 vs key 121)
    adjudicated false — real gap ≈462 units vs ≈400 units of ink; the
    occlusion audit (real PIL widths) reports no overlap.
  - Banned intermediary term: zero occurrences in page text (checked by scan;
    referred to here only by description, never printed).
  - Dates/weekdays: re-verified with `date -d` (see §3).
- **Occlusion audit (mandatory gate):** `tools/occlusion_audit.py`, selftest
  first (planted classes fired, clean controls silent). Run 1 found 67 flags
  (65 P1 TEXTX = the contents-box overprint, 2 LINEX = the P2 rule graze and
  the P7 overflow). Final run: **0 flags** over all 8 SVGs
  (`hidden_files/w45/ru-core/occlusion-3.json`; earlier runs
  `occlusion-1.json`, `occlusion-2.json` in the same dir).
- **Accepted disclosed pattern (not a defect):** feature-column whitespace on
  P1–P6 (third column partly empty below the gloss box) matches the shipped
  W43 pattern, which the W43 KIT §3 explicitly disclosed as accepted. No
  filler prose was added to fill columns.
- **Known remaining nit (adjudicated, not a defect):** Chinese line breaks can
  fall between two characters of a two-character word (e.g. the P7 disclosure
  breaks between 仍 and 为). Chinese typesetting breaks between characters as
  a matter of course; no line begins or ends with lone punctuation, which is
  the actual defect class. Left as is.

## 8. Abstract

`ABSTRACT.txt` in this dir: one Simplified Chinese line, no ASCII double
quotes, naming the real W45 topics (4 Nov Wednesday holiday, 3 Nov short day,
11.11 smart shopping, 6–8 Nov RPL round 14) + a learner search phrase
(用俄语新闻学俄语） + masthead (Lucerna VOL.2), levels (A2–B2) and exercise
count (150).

## 9. Delivery status

Finalized, NOT pushed, NOT posted: per the task brief, repo insertion is done
by the parent line (serialized) and inserts are currently BLOCKED behind an
unrelated push outage, so this core queues for insert after finalization.
No git push, no Discord post, no user message was made from this build.
