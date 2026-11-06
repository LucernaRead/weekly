# WEEKLY-KIT — Lucerna Russian Weekly, VOL.3 (W46 zh-cn)

## 1. Spec

- **Edition:** Русский (Russian) target-language core, VOL.3; reader language Simplified Chinese (zh-cn).
- **Issue week:** Monday 9 November – Sunday 15 November 2026. **Issue date:** Monday 9 November 2026.
- **Pairing:** target language Russian × reader native language Simplified Chinese (zh-cn).
  Masthead carries no article (Russian is article-less per `tools/tables.py`): masthead is `Lucerna`; the top strip reads `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 俄语正文 · 中文讲解`; the footer on every page reads `Lucerna · 俄语周报 VOL.3 · LUCERNA RUSSIAN WEEKLY` and the page number in Chinese (`第 N 版 / 共 8 版`).
- **Explanation-layer convention:** all explanation is in Simplified Chinese — glosses, exercise instructions, answer notes, section furniture and footers. Russian is the only target-language text. This core IS the zh-cn edition for abstract purposes, so `ABSTRACT.txt` is one Simplified Chinese line (see §8).
- **Format:** 8 pages (multiple of 4), 1950×2700 px per page, 4 columns, warm ivory paper, dark olive-green accents. Pipeline: Python → SVG → CairoSVG → PNG/PDF.
- **Exercises:** **150 total, continuously numbered 1–150**, registered in code and rendered as the P8 answer key. By page: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38. By level: A2 51, B1 75, B2 24. By type: 完成句子 54, 单选 42, 词汇配对 20, 完形单选 13, 造句 12, 句型转换 4, 翻译 4, 写作 1.
  P8 model writing text (“Моя обычная неделя в ноябре”) = **87 words** (brief: 80–100).
- **P7 golden sentences:** 8 sentences, each occurring exactly twice in the issue — once in its own article, once in the P7 “ФРАЗЫ НЕДЕЛИ” list (verified programmatically on page-joined SVG text, §7). All 8 come from this issue's own articles: P1 ×2, P2 ×1, P3 ×1, P4 ×1, P5 ×1, P6 ×2. Page references on P7 are kept in Russian (`Страница N`) in every edition.
- **No invented facts.** No standings are printed (the trend pool gives none). No invented poll, quote or account data. Round-14 results are explicitly unknown at press time (see §3). The P6 chart is labeled practice data (УЧЕБНЫЕ ДАННЫЕ + “not real statistics” line) and sums to 100% (42/24/20/14) with proportional bars.

## 2. Content per page

- **P1 · Первая (A2) — “Обычная неделя: пять рабочих дней”.** Lead: the ordinary week — five working days in a row, Police Day, the 11.11 sale, the national team. Numbers box, media-topics box, contents, word of the week “предзимье”, autumn-park photo, “Первый снег?” box, blitz quiz (ex. 1–10).
- **P2 · Жизнь (A2) — “10 ноября: День полиции”.** Police Day history (1962; the 10 November 1917 militia decree), Economist Day, professional holidays add no days off; holidays-of-the-week box; “А вы?” letter call for VOL.4; Bentley snowflake photo; weather words — предзимье, мокрый снег, гололедица, заморозки (ex. 11–28).
- **P3 · Культура (A2→B1) — “Кино в середине ноября”.** “Лиля” (from 12 Nov), “Эбенезер” (mid-November, no exact date claimed), “В сердце Нэшвилла” (streaming 13 Nov) (ex. 29–46).
- **P4 · Спорт (B1) — “14-й тур: итоги неизвестны”.** Honest press-time disclosure: round-14 results were unknown when the issue was built (2 Nov); verified 7-fixture table only, round-13 results box, 1912 football photo, national-team note (Uzbekistan–Russia, Thu 12 Nov, Tashkent; no kickoff time printed — sources conflicted) (ex. 47–64).
- **P5 · Молодёжь (B1) — “11 ноября: день покупок и посылок”.** Sale facts (Ozon 11.11, 22 Oct – 12 Nov; 600,000+ sellers, +16% YoY; 14.4m orders on 11 Nov 2025), parcels/returns/promo codes, Black Friday ahead; market photo (ex. 65–82).
- **P6 · Разбор (B2) — “Обычная неделя: как её прожить”.** Rhythm of an ordinary week, 9–15 Nov day strip, labelled PRACTICE-DATA chart (Работа и учёба 42, Покупки 24, Кино и книги 20, Спорт 14; sums to 100%), pro/contra box (ex. 83–100).
- **P7 · Язык (A2/B1/B2 + error clinic + word box + readers' corner + golden sentences + VOL.4 teaser) (ex. 101–112).** Three level columns (weather words, parcel words, attribution: “синоптики обещают”, “по данным”, “может быть”), four-item error clinic, word box “посылка”, readers' corner (see §6), 8 golden sentences with page references, teaser: full round-14 results, Uzbekistan–Russia result, Black Friday, readers' letters.
- **P8 · Тест (ex. 113–150 + all 150 keys).** A chronicle cloze 8, B general questions 8, C reading about Masha 4, D sentence building 4, E RU→reader-language translation 4, F word matching 4, G pickup-point dialogue cloze 5, H writing 1 + 87-word model text (“Моя обычная неделя в ноябре”, brief 80–100).

## 3. Trend / fact sources (all in-week or just-passed reports)

- **Trend research (browser.search, Russian-language ecosystem, 2026-11-02):** trend-first selection from Russian-language media/social heat + calendar nodes for 9–15 Nov 2026. Anniversaries/commemorations were NOT used as living trends.
- **RPL round 14 fixtures (7 verified, rusfootball.info matchcenter crawled 2026-11-02 11:55 UTC + Sportradar/Sports.ru listings):** Fri 6 Nov Lokomotiv–Rubin 19:30; Sat 7 Nov Fakel–Dinamo 14:00, Akhmat–Rodina 16:30, Krasnodar–CSKA 19:30 (Ozon Arena); Sun 8 Nov Spartak–Akron 16:15, Zenit–Rostov (time unverified), Krylia Sovetov–Orenburg (time unverified). Moscow time. No 8th fixture verified — only these 7 are printed. Results UNKNOWN at press time (2 Nov); the issue says so on the page and carries full results to VOL.4. Never invented.
- **RPL round 13 verified results (rusfootball.info matchcenter, 2026-11-02):** Rubin 1–0 Fakel (31 Oct), Krasnodar 1–2 Rodina (31 Oct, via Regnum), Orenburg 0–0 CSKA (1 Nov), Dynamo Makhachkala 0–3 Rostov (1 Nov), Baltika 2–1 Akron (1 Nov), Lokomotiv 0–4 Spartak (1 Nov). Krylia Sovetov–Zenit (Mon 2 Nov 18:00) was still to be played at build time — stated as played after press time, result unknown. Next round: 15th round only 20 Nov 2026 (pause after round 14; carried from the W45 KIT).
- **11.11 sale:** Ozon 11.11 sale 22 Oct – 12 Nov 2026; >600,000 sellers joined, +16% year-on-year (Ozon press service via RIA/vc.ru, Oct 2026). 11 Nov 2025: >14.4m orders in one day on Ozon (Retail.ru via vc.ru). Top categories: smartphones, laptops, large appliances (wek.ru). Returns peak 11–30 Nov; promo codes on electronics typically valid 4–7 days (wek.ru advice). Black Friday: Ozon 13 Nov–2 Dec; M.Video from 12 Nov; Wildberries 16–30 Nov; Yandex Market provisionally 25–27 Nov.
- **Calendar nodes 9–15 Nov 2026 (weekdays verified with `date -d`, Europe/Moscow: 9 Mon, 10 Tue, 11 Wed, 12 Thu, 13 Fri, 14 Sat, 15 Sun):** 10 Nov Day of Police / internal-affairs officers (professional holiday, working day; history since 1962, date from the 10 Nov 1917 decree on workers' militia — Tolk); 11 Nov Economist Day; 13 Nov Day of RCB protection troops; 14 Nov Day of Sociologist; 15 Nov All-Russian Conscript Day. November overall: 20 working days, 10 days off (mk.ru / regions.ru). Professional holidays give no extra day off.
- **Weather (forecast only, never claimed as fallen):** Forecasters (Fobos: Leus/Tishkovets, via MK/regions.ru, 1–2 Nov 2026) promised first wet snow 3–4 Nov, ~1 cm temporary cover melting quickly; stable snow only end of Nov. Moscow sunset ~16:30–16:48. October 2026 was the 2nd warmest on record in Moscow (Fobos via mentoday.ru).
- **Cinema:** “Лиля” (Lilya Brik / Mayakovsky biopic, dir. Vera Storozheva) from 12 Nov (rss.plus listing); “Эбенезер” (Dickens retelling, Johnny Depp as young Scrooge) mid-November (MAXIM/respawn — exact date conflicts 12 vs 13 Nov, so the issue says “in mid-November” only); “В сердце Нэшвилла” (Jessica Chastain) streaming 13 Nov (vtomske.ru).
- **National team:** Friendly Uzbekistan–Russia, Thu 12 Nov, Tashkent, Pakhtakor stadium (Sport-Express / sports.ru, RFU 26 Oct). Extended squad 36 players incl. Golovin, Zakharyan, Batrakov. Venezuela–Russia 17 Nov in Krasnodar is OUTSIDE the week — mentioned only as the next match. Kickoff time OMITTED: Sport-Express gave 13:00 but sports.ru said the time was unannounced — conflict, so no time printed.
- **W45 promises honored (cross-checked against the W45 RU core KIT, which wins over the extractor file `hidden_files/w46/w45-promises.md` — no conflicts found):** 11.11 sale day (P1/P5 lead); round-14 results handled honestly (unknown at press time, schedule only, full results carried to VOL.4); reader letters — no fabrication, editor's example + on-page disclosure, promise carried forward (see §6). Handover items for OTHER targets found in the extractor file (DE Volkstrauertag/St. Martin, EN Veterans Day/NFL Munich, ES campaign, FR Senate/Armistice, IT Festival dei Popoli, JA Reading Week/Japan Series, NL Sinterklaas, PT Enem, ZH S16 final, ZHTW ITF) were NOT imported into the Russian family.
- **Editorial red lines observed:** no international politics, wars or geopolitics anywhere; Russian domestic life/culture/sport only.

## 4. Images (public-domain / CC0 only; credit from the Wikimedia Commons Artist field)

- **P1 autumn park photo** (`autumn_path.jpg`, reused from the W43/W45 builds): Toxer427, CC0, Wikimedia Commons. Captioned as a November park scene.
- **P2 snowflake photo** (`snowflake.jpg`, reused from the W45 build): Wilson Bentley, c.1890–1920s, public domain.
- **P4 1912 football photo** (`football1912.jpg`, reused from the W43/W45 builds): Russia 1912 Olympics squad, unknown author, public domain.
- **P5 market photo** (`market.jpg`, reused from the W45 build): USDA farmers-market stand photo, Artist field Preston Keres (USDA), public domain (“Please credit: USDA Photo by Preston Keres”). Captioned honestly as a market scene, NOT claimed to be Moscow.

## 5. Build / reproduce

Build code (copied from the W46 RU core build and repointed; fan-out transform via `hidden_files/w46/ru-transform.py` + `ru_maps.py`, which asserts every translation-map key occurs, no source-language explanation string remains, and Cyrillic content is unchanged except whitelisted furniture/badge lines):
`hidden_files/weekly-report-w46-ru-build/` — `content12.py` (P1+P2), `content34.py` (P3+P4), `content56.py` (P5+P6), `content7.py` (P7), `content8.py` (P8 + registry). One process only (never run content modules standalone):

```
cd hidden_files/weekly-report-w46-ru-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py
```

Outputs in this dir: `svg/` (8 SVGs), `cards/` (8 page PNGs),
`Lucerna-VOL3.pdf` (24,590,689 bytes, print), `Lucerna-VOL3-web.pdf`
(2,719,071 bytes, web, under the 7 MB limit).
Final build: core build run6: exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE warnings; TOTAL 150; model words 87.
Web PDF built with `tools/webpdf.py` (real text layer, never a PIL whole-page JPEG拼合): pdftotext bytes 53,549; print-vs-web text identical after whitespace normalisation (52,665 chars each).

## 6. Readers' corner — no fabrication (on-page disclosure, not KIT-only)

No real reader, letter, name or quote is fabricated. P7 prints a clearly labeled editor's example (“— М. (пример от редакции)”) AND an on-page disclosure in Russian and in the reader language stating plainly that no real reader letters or best P8 texts had arrived by press time, so the example stands and the promise carries to VOL.4. The disclosure is rendered inside the letters box on P7 (verified visually: box fully inside its border, clear of the “ФРАЗЫ НЕДЕЛИ” rule). The VOL.4 teaser repeats the call for letters.

## 7. Self-proofread record (full pass, 2026-11-02)

- **Defects found and fixed during the core build (all re-rendered and re-verified):**
  1. P7 letters-box LINEX: the disclosure's last line crossed the box rule — letter/disclosure text shortened, golden section moved down (`fy` 1770→1816), quote pitch 145→140, teaser moved to y=2420, box-height formula +34; the disclosure text now ends above the rule at 1802 in every edition (box bottom 1789.46 in the core, at most 1818 in the fan-outs where the rule passes only through empty box padding — verified on the rendered cards).
  2. P8 translation stem reused golden sentence #6 (“Посылку надо отследить…”) — reworded to “Посылку нужно отследить, получить и проверить.” so each golden sentence occurs exactly 2×.
  3. E3 translation key carried a stray “→ ___” (visible in the printed answer key) — removed; the key is now the plain translated sentence.
- **Programmatic checks after the final build (all pass):**
  - Golden sentences: 8/8 exactly 2×, each on its article page + P7 (check_core.py).
  - Gloss headwords: 0 fails; orphan line-starts: 0; same-baseline collisions: 0.
  - P8 keys: all 150 present in the rendered P8 (`p8.py extract` 150/150).
  - Exercise counts verified from the registry: TOTAL 150; by page P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38; by level A2 51, B1 75, B2 24; model text 87 words.
- **Occlusion audit (mandatory gate):** `tools/occlusion_audit.py`, selftest first (planted classes fired, clean controls silent). Final run: **0 flags** (`ru-core-occlusion.json`).
- **P8 compare (mandatory gate):** `tools/p8.py compare` vs the core edition: **n/a — this IS the core edition (p8.py extract: 150/150 noted by the self-check)**.
- **Freeze diff (mandatory gate):** `tools/freeze.py diff` vs the core edition: **n/a — this IS the core edition**.
- **Visual check:** P1 + P7 cards read in full; P4 exercise block ends clear of the footer line; P6 chart labels clear of bars (GRAZE element-check clean). P1, P2, P4, P6, P7, P8 cards read in full (run6): E3 key verified without the stray arrow; P4 exercise block ends clear of the footer; P6 chart labels clear of bars; P7 disclosure inside the letters box.
- **Accepted disclosed pattern (not a defect):** feature-column whitespace on P1–P6 (third column partly empty below the gloss box) matches the shipped W43/W45 pattern. No filler prose was added to fill columns.

## 8. Abstract

`ABSTRACT.txt` in this dir: one Simplified Chinese line, no ASCII double quotes, naming the real W46 topics (ordinary week 9–15 Nov, Police Day 10 Nov, 11.11 sale + Economist Day, round-14 results unknown, Uzbekistan–Russia 12 Nov) + masthead (Lucerna VOL.3), levels (A2–B2) and exercise count (150).

## 9. Delivery status

Finalized, NOT pushed, NOT posted: per the task brief, repo insertion is done by the coordinator (serialized). No git push, no Discord post, no user message was made from this build. `<slug>.text.md` in this dir is exported from the source manuscript via `hidden_files/w46/ru_textmd.py` (AST walk of `content*.py`, never from a PDF), with the P8 answer key reconstructed from the collected exercise registry.

## 10. Fix record — Round 1 proofread defects D1–D3 (2026-11-02/03, fix worker)

Source of the defects: independent proofreader Round 1 verdict (`hidden_files/w46/ru-proofread-gates/proofreader-verdict-round1.md`, ROUND 1 FAIL). All fixes were made at the source and fully re-rendered; no rendered SVG/PDF was hand-edited. Sections 1–9 above are untouched by this record.

### D1 (BLOCKING, all 11 editions) — P5 matching block C, P8 key letters 76/77 transposed

P5 block C prints words 75 посылка, 76 возврат, 77 промокод, 78 пик with options a. код со скидкой (= promo code), b. товар возвращают в магазин (= return), c. самое большое число заказов, d. товар, который прислали по почте. Correct matches: 75→d, 76→b, 77→a, 78→c. The P5 block itself was correct and is unchanged.

- Core build source `hidden_files/weekly-report-w46-ru-build/content56.py`: before content56.py match_set keys ["d", "a", "b", "c"], notes ["包裹 d", "退货 a", "促销码 b", "高峰 c"]; after content56.py match_set keys ["d", "b", "a", "c"], notes ["包裹 d", "退货 b", "促销码 a", "高峰 c"].
- Fan-out map `hidden_files/w46/ru_maps.py` (all 10 specs): the same transposition in the P8-key note pairs was fixed in every spec, e.g. en `('退货 a', 'return a')` → `('退货 b', 'return b')` and `('促销码 b', 'promo code b')` → `('促销码 a', 'promo code a')`; this edition's own rendering comes from the core source above.
- Rendered P8 key, before: `76. a — 退货 a`, `77. b — 促销码 b`; after (verified in this edition's p8-test.svg): `76. b — 退货 b`, `77. a — 促销码 a`.
- Manuscript registry (`.text.md` §C + Answers, regenerated from source): before `76. возврат — код со скидкой (key a · 退货 a)` / `77. промокод — товар возвращают в магазин (key b · 促销码 b)`; after `76. возврат — товар возвращают в магазин (key b · 退货 b)` / `77. промокод — код со скидкой (key a · 促销码 a)`.
- All five matching blocks were semantically re-verified option-by-option in the build sources (25–28, 39–42, 57–60, 75–78, 141–144) and the rendered P8 keys were extracted per edition: all correct; only 76/77 changed. See `hidden_files/w46/ru-fix/verify_matching.py` output and `logs/p8-keys-printed.txt`.

Core edition; the same fix record covers the zh-cn edition, whose .text.md is byte-identical to the core file (52,661 bytes, cmp-verified).

### Re-render + re-gate evidence (final artifacts, 2026-11-03)

- Rebuild: `hidden_files/w46/ru-fix/rebuild.sh` (core + all 10 fan-outs, sequential); every run log: exit 0, TOTAL 150, A2 51 / B1 75 / B2 24, pages 10/18/18/18/18/18/12/38, model words 87, 0 FLOW OVERFLOW / HEAD TOO WIDE. Logs: `hidden_files/w46/ru-fix/logs/ru-*-run.log`, `ru-*-transform.log`.
- Web PDF via `tools/webpdf.py`: 2719077 bytes (≤ 7 MB), 8 pages, print-vs-web text identical after whitespace normalisation, pdftotext bytes > 0. `.text.md` regenerated from the source manuscript (headers verbatim; only the D1/D2/D3 lines differ from the pre-fix file): 52661 bytes.
- Occlusion audit: 0 flags, selftest OK. `check_core.py`: golden BAD 0, gloss fails 0, orphan line-starts [], same-baseline collisions 0. `p8.py extract`: 150/150 noted. Freeze self-diff control: 0 added/removed strings, 0 added CJK characters.
- Freeze diff vs core: zero added Cyrillic words (per-page word-level analysis, TOTAL ADD {}); char totals cyr=17049 han=1972 kana=0 hangul=0 (core self-diff control).
- Orphan-fragment scan (`ru-fix/orphan_scan.py`, all 8 pages of all 11 editions): TOTAL ORPHANS 0; only the legitimate pre-existing P5 D-head bridge band-hits directly under their heads. Kinsoku scan (`ru-fix/kinsoku_scan.py`, all editions): 0 hits.
- P6 chart re-measured: bars at x=685 widths 600/343/286/200 for 42/24/20/14%, labels sum to 100%. P7 phrases: per-page freeze ADD {} on p7 in every edition (Russian text verbatim).
- Visual checks at full frame: P5 card (this edition), plus the D2/D3 pages where applicable (P3/P4 in D2 editions, P8 in ja) — instructions complete at home positions, no stray fragments, no overflow, footer clear.
- Full fix report + gate JSONs/logs: `hidden_files/w46/ru-fix/FIX-REPORT.md` and `hidden_files/w46/ru-fix/`. A Round 2 independent proofread follows; re-gating does not replace it.
- Delivery: still finalized, NOT pushed, NOT posted — repo insertion remains the coordinator's (serialized) step. No git push, no Discord post, no user message was made from this fix work.
