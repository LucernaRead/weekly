# WEEKLY-KIT — Lucerna 简体中文周报 VOL.2 (W45)

## Identity and spec

- **Issue week:** Monday 2026-11-02 to Sunday 2026-11-08 (magazine model:
  the cycle starting Monday 2026-10-26 produces the issue dated the following
  Monday). Issue number: VOL.2, the second Simplified Chinese issue.
- **Pairing:** zh-cn × en — Simplified Chinese body text with an English
  explanation layer, the edition for English-speaking readers. The pairing
  badge is printed on P1: “简体中文正文 · 英语讲解 — Simplified Chinese
  text · Explanations in English · the edition for English-speaking
  readers”.
- **Masthead:** bare `Lucerna` in blackletter (UnifrakturMaguntia). Chinese
  is article-less per the SOP, so there is no “The”/“Le” article. Every page
  footer reads “Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 ·
  Simplified Chinese text · English explanations”.
- **Format:** 8 pages (a multiple of 4), 1950×2700 px, 4 columns, warm
  ivory paper `#f7f1e2`, deep olive accents. A2→B2 ramp; every exercise is
  individually level-badged. One unified numbering sequence, 1–150, with no
  gaps or duplicates; P8 answer keys are generated from the exercise
  registry.
- **Native Simplified Chinese:** written natively from the mainland-China
  ecosystem. Not converted or transcoded from any Traditional Chinese
  edition. The explanation layer is entirely in English; remaining Chinese
  strings classify as content (article bodies, stems/options, quoted
  examples, bilingual headers, data labels, captions, answer tokens,
  readers'-corner letter, teaser, pinyin).
- **Status:** builder self-check complete (see “Builder's proofread record”
  below). This is a builder handoff, NOT a finalisation claim — independent
  proofreading is still owed by the parent line. No Discord delivery, no
  main-chat card/PDF delivery, no cron, no repo push was done by this
  builder.

## Contents, page by page

| Page | Section | Level | Exercises | Content |
|---|---|---|---|---|
| 1 | 头版 Top story (A2) | A2 | 10 (1–10) | Lead: Double 11 still running × Start of Winter on Saturday. This-week calendar box (Mon 11-02 Double 11 spot-sale period; Wed–Sat 06:00 S16 quarter-finals; Sat 11-07 Start of Winter + new film; Sun 11-08 Journalists' Day + S16 semi-final). Contents, word of the week 「立冬」, parcel-locker photo, briefs, quick quiz. |
| 2 | 生活 Life (A2) | A2 15 / B1 3 | 18 (11–28) | Double 11 shopping life (spot sales, direct cuts, AI help, WeChat shop) + Start-of-Winter life (layering, regional winter food, some schools' mid-term exams). Practice example labelled as practice numbers (sweater 240 + scarf 80 = 320, direct cut 50 → payable 270). Shopping word cards 现货 / 直降 / 立减 / 补冬. This-week dates box. Autumn-valley photo. |
| 3 | 文化 Culture (A2→B1) | A2 15 / B1 3 | 18 (29–46) | Start of Winter feature (19th solar term, 17:52 moment, three micro-seasons, regional food differences, uneven cooling, Journalists' Day paragraph). Frost + dumpling photos. Festival-dates box. |
| 4 | 体育 Sport (B1) | B1 | 18 (47–64) | S16 feature (AL out, IG/TES/BLG chasing the quarter-finals, Swiss format, fourth-round preview, 2026-10-27 cutoff stated on the page, final Beijing 2026-11-15 03:00). S16 schedule box (no score chart — final Swiss scores were not yet knowable). LAN-party file photo. Sports-dates box. Match-words box. |
| 5 | 青年 Youth (B1) | A2 1 / B1 17 | 18 (65–82) | AI film 《三星堆：未来往事》 (release, licence, 100 minutes, Maoyan 4-day figure, debate) + Start-of-Winter new film 《我们仅有一次的人生》 (cast, public synopsis, original title, festival prize, 114 minutes). Popcorn photo. Film-dates box. |
| 6 | 深读 Deep read (B2) | B2 | 18 (83–100) | Double 11 deep read (why the rules got simpler: more spot sales, more direct cuts, AI help, new platform; but “lowest price” claims must be checked against the checkout page, delivery cost, and returns rules). Practice-data bar chart only (see below). Key-points box. “Three questions for reading news” box. |
| 7 | 词语精讲 Language focus (A2/B1/B2 columns + error clinic + sentence frame + readers' corner + phrases + VOL.3 teaser) | A2 4 / B1 4 / B2 4 | 12 (101–112) | A2 shopping/winter words; B1 time-and-date order (big → small, e.g. 11月7日星期六17点52分); B2 reading news (说法 / 数据 / 广告); error clinic (的/地/得, measure-word order, date order); frame 先…再…; readers' corner (labelled editor's example + on-page deferral disclosure, see below); 8 phrases; VOL.3 teaser. |
| 8 | 测验与答案 Test & keys | A2 11 / B1 24 / B2 3 | 38 (113–150) | A true/false (8) + B big quiz (10) + C complete-the-sentence (10) + D read-and-answer passage about Xiao Hong in Beijing (6) + E in-conversation (3) + F writing (1). Then all 150 answer keys with brief English notes, generated from the registry, grouped by page with “— Page N —” headers for pages 1–8. Writing topic 《我的立冬周末》, 120–180 characters; model answer programmatically counted at 172 characters. |

## Measured totals

- **Exercises: 150 total** — A2 56 · B1 69 · B2 25. By page: 10 / 18 / 18 /
  18 / 18 / 18 / 12 / 38.
- **By type:** 完成句子 (fill in) 68 · 单选 (choose) 50 · 词语配对
  (matching) 20 · 完形单选 (cloze choose) 11 · 写作 (writing) 1.
- **Visible text** (concatenated `<text>` nodes of the final SVGs):
  23,038 characters without spaces / 26,765 characters with spaces.
- **Benchmark comparison:** 150 exercises against the 《英语周报》 counted
  benchmark of 154, at the SOP's ~150 target. No padding was added to reach
  a higher number; the issue ships at 150.
- **P6 practice chart** (cols 0–2): rows A 毛衣+围巾 270 yuan, B 耳机
  179 yuan, C 书+本子 160 yuan; bars drawn from zero at exactly 3.0 px per
  yuan, i.e. widths 810 / 537 / 480 px, starting at x = 325, verified in
  the SVG rects. Basket maths printed in the article: A 240 + 80 = 320 −
  50 = 270; B 199 − 20 = 179; C 120 + 40 = 160 with no cut. The chart note
  reads “Practice data only — not real shop prices” (plus the Chinese
  equivalent in the article paragraph). P4 has no score chart, for the
  reason given under “Honesty limits” below.
- **Files:** 8 SVGs in `svg/`, 8 full-page PNG cards at 1950×2700 in
  `cards/`, print PDF `Lucerna-VOL2.pdf` (44,361,569 bytes, 8 pages),
  web PDF `Lucerna-VOL2-web.pdf` (3,141,620 bytes, 8 pages, JPEG pages
  q85 @1400 px — under the 10 MB Discord ceiling, though this builder does
  not deliver via Discord).
- **Phrases of the week (P7):** 8 phrases, each verbatim from this issue's
  own articles and each occurring exactly twice in the final SVGs (article
  + P7): 「不用等11月11日」 p. 1; 「下单就能发货」 p. 2; 「先看结算页，再付
  款」 p. 2; 「水开始结冰」 p. 3; 「三场都输了」 p. 4; 「小局一场没赢」 p. 4;
  「故事够不够好」 p. 5; 「别以后，就现在」 p. 5.

## Trend and fact sources

Trend-first sourcing from the mainland-China ecosystem (Batch D trend pool
for the Chinese editions + web verification on 2026-10-27). No anniversary
material, no international politics, and no Chinese domestic politics (the
target country is China) were used.

### Double 11 (Double 11) — in-progress week, not the day itself

- JD.com: spot sales from 20:00 on 2026-10-12; “开门红” 20:00 on
  2026-10-20; overall activity 2026-10-12 to 2026-11-13. Taobao/Tmall:
  presale from 20:00 on 2026-10-15; tail-payment + spot sales from 20:00 on
  2026-10-20; spot period to 23:59 on 2026-11-13. Source: 2026-10-08 Sina
  Finance platform timetable, found by web search.
- Peak sale （高潮场）: 20:00 on 2026-11-10 to 24:00 on 2026-11-11 — in the
  following week, so W45 mentions it only as next week's event (P1 numbers
  box, P2 calendar “下周二 11月10日 20:00”, VOL.3 teaser).
- WeChat shop （微信小店）: first Double 11 participation, 2026-10-12 to
  2026-11-15, 35 days in total. Trend pool (Blue Whale Finance via
  21jingji, 2026-10-13).
- This is the 18th Double 11. Reported trend changes: spot sales replacing
  presales, simpler rules (official instant discounts 官方立减 and direct
  price cuts 直降 continuing; cross-shop 满300减50-style spend-and-save
  receding), and AI entry points including Doubao's 买前问豆包 and Qianwen
  joining the shopping flow. Trend pool (Beijing Business Daily via
  jiangshouff.com, 2026-10-14; Blue Whale Finance via 21jingji,
  2026-10-13).
- No Double 11 sales totals, platform quotations, or consumer quotations
  were invented. All basket arithmetic in the issue is explicitly labelled
  practice data.

### Start of Winter （立冬）

- Saturday 2026-11-07, 17:52交节 (Beijing time), the 19th of the 24 solar
  terms and the first solar term of winter. Source chain (disclosed
  honestly): the Batch D trend pool, which cites jieri8.com (2026-10-14/15)
  and the Hong Kong Observatory 2026 almanac. A direct web search for the
  17:52 time on 2026-10-27 returned only unrelated calculator pages, so
  this KIT does **not** claim an independent second confirmation.
- Three micro-seasons （三候）: 一候水始冰, 二候地始冻, 三候雉入大水为蜃.
  Verified by web search.
- Customs are regionally varied, not nationally uniform: dumplings in many
  northern places (homophone with 交子， autumn–winter handover);
  chicken/duck/fish, tangyuan, ciba, and mutton soup in various
  southern/other places; 补冬 (eating well before winter). The issue states
  explicitly that no single custom is national.
- Start of Winter does not mean simultaneous cooling everywhere: southern
  places can still be warm while northern places are already cold/snowy.
  Stated generally, without invented temperatures.

### S16 (League of Legends Worlds 2026) — cutoff honestly dated 2026-10-27

- Venue/stages (Beijing times, from the Sina Sports S16 guide found by
  search): play-ins 2026-10-16–19 Los Angeles; Swiss stage 2026-10-24–27
  at 01:00, 2026-10-29–31 at 04:00, and 2026-11-01 at 01:00, all in Allen,
  Texas (Credit Union of Texas Event Center); quarter-finals 2026-11-04–07
  at 06:00; semi-finals 2026-11-08–09 at 06:00; final 03:00 Beijing time on
  2026-11-15 at Barclays Center, New York (14 Nov US date).
- Swiss format: win-group plays win-group, loss-group plays loss-group;
  first to 3 wins advances, first to 3 losses is out; promotion/elimination
  rounds are best-of-3 (BO3).
- Verified results through the 2026-10-27 cutoff: LPL opened 0–4 in round 1
  (2026-10-24 reports); on 2026-10-26 IG beat HLE and TES beat G2, both
  reaching 2–1; BLG beat KC, also reaching 2–1; GEN and DK were already
  3–0 and through; AL and TSW were 0–3 and out. AL's exit: lost to KC in
  round 1, lost the all-LPL match to TES in round 2, then lost 0–2 to
  North American TL on 2026-10-27, finishing 0–3 in series and 0–4 in
  games, stopping at the round of 16.
- Fourth-round draw (BO3, Beijing times, announced 2026-10-27): 2026-10-29
  04:00 MKOI–T1 and about 07:00 LYON–IG; 2026-10-30 04:00 CFO–KC and about
  07:00 BLG–TES (LPL internal match); 2026-10-31 04:00 LOS–TLAW and about
  07:00 G2–HLE.
- **Honesty limit:** at the build date (2026-10-27), the fourth round
  (2026-10-29–31) and the rest of the Swiss stage (to 2026-11-01) had not
  been played. P4 therefore prints standings “as of Oct 27, 2026”, labels
  the quarter-final teams as not yet known at press time, previews the
  fourth round and the in-week quarter-finals/semi-final, and does not
  fabricate any later Swiss result. The P7 VOL.3 teaser promises the
  completed Swiss/knockout report.

### Films (P5)

- 《三星堆：未来往事》 (Sanxingdui: Future Past): released 2026-10-23;
  produced by Bona Film Group; 100 minutes; no live actors — all
  characters are original digital images, with picture and some sound
  AI-generated; described in reporting as the first domestic AI feature
  film to obtain a public screening licence. Box-office anchor used: by
  noon on 2026-10-26, Maoyan Professional showed about 1.192 million yuan
  cumulative over 4 days, with 24 and 25 October each averaging 2 viewers
  per screening (via 每日经济新闻， 2026-10-26). Conflicting first-day
  figures across sources (about 80,000+ yuan vs about 301,500 yuan) were
  deliberately **not** printed; only the Maoyan 4-day cumulative figure is
  used, dated and sourced on the page. The discussion point printed is
  whether AI can make a film / whether audiences come for story or
  technology — no invented critic quotations.
- 《我们仅有一次的人生》 (We Only Have One Life): nationwide release
  Saturday 2026-11-07 (Start of Winter day); directed/written by Sun
  Aoqian; Song Jia as Huang Yan, a terminally ill female crematory
  worker; Wen Qi as Yao Xue, a girl who has lost her mother; plot from
  the public synopsis only (a bone-ash mix-up, both families unwilling to
  swap back, only Yao Xue believing Huang Yan, the two travelling
  together to return the ashes, moving from opposition to mutual
  redemption); original title 《余烬》; entered the Beijing International
  Film Festival Tiantan Award competition and won Best Cinematography;
  114 minutes; release slogan “别以后，就现在”. Sources: Batch D trend
  pool (Sina Movie, 2026-10-21) plus web search (including a 2026-10-20
  consumer-news report). Some Sina summary pages found by search were
  marked AI-generated, so they are **not** cited as primary sources here.

### Other calendar items

- 中国记者节 (Journalists' Day): Sunday 2026-11-08; approved in 2000 with
  the date set to the founding date of the All-China Journalists
  Association (8 November). Verified by web search. Used only as a
  calendar item plus a language angle (a journalist interviews people and
  writes news; dates, places, and figures must be written correctly). No
  media-management or opinion-guidance angle is used.
- Mid-term exams: some schools hold them in early November, on differing
  dates — not a national unified date (Batch D trend pool: Nanjing-area
  reports and a Wuhan school notice dated 2026-10-12). Printed only in
  that qualified form. Autumn breaks in mid-to-late November are outside
  the issue week and were not written in as this week's events.

### Explicitly rejected material

- “长征胜利 90 周年” anniversary content (seen in a 2026-10-21 Sina
  report): rejected — an anniversary is commemorative marketing, not a
  living trend, and the subject touches historical-political narrative.
- All political search hits (including Fifth Plenum commentary): excluded
  under the China-domestic-politics red line; no international-politics
  topics were used.
- Double 11 day itself (2026-11-11), mid-to-late-November autumn breaks,
  and the 2026-11-22 Golden Horse awards (Traditional-Chinese edition
  matter, not this edition) were not presented as in-week events.

## W43 promises: how each was handled

- **立冬 Saturday 2026-11-07 — in the W45 week.** Honoured as a lead (P1
  headline, P3 feature, P7 word of the week).
- **S16 Swiss-stage results — W44 just-passed.** Reported only as far as
  verifiable at build time (see “Honesty limit” above); final Swiss rounds
  were not yet played at the build cutoff, so they are not reported as
  results. The completed Swiss/knockout report is a VOL.3 teaser item.
- **双11 parcel arrivals — beyond W45.** 双11 itself is Wednesday
  2026-11-11, outside the issue week. W45 writes only the buildup /
  in-progress sale, never arrivals as done. The arrivals follow-up is a
  VOL.3 teaser item.
- **Real reader letters + best VOL.1 P8 writing (topic 《我的双11购物车》) —
  overdue from VOL.2.** No genuine letters are on record, so no reader,
  letter, name, or quotation was invented. Instead, the P7 readers' corner
  prints a clearly labelled editor's example plus an open invitation, and
  discloses the deferral **on the page** in both Chinese and English:
  VOL.1 promised real reader letters and the best VOL.1 writing in VOL.2;
  none have arrived and there is no publishable submission, so this corner
  still prints an editor's example and keeps the invitation open;
  “延期不是取消 / Deferred, not cancelled.” KIT-only disclosure would not
  have passed, and fabrication never passes.

## VOL.3 promises printed in this issue (P7 teaser)

“双11当天11月11日星期三，包裹到了吗？S16淘汰赛打完了，谁进了决赛？
总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周
见！” — 2026-11-11 is a Wednesday and the final's Beijing time is
2026-11-15 03:00, both verified.

## Image authorisations

6 photos, all CC0 / public domain, credit taken directly from the Commons
API Artist field. Full table with Commons file titles and the 2026-10-27
verification date: `hidden_files/weekly-report-w45-zhcn-build/assets/CREDITS.md`.
Placement and image-element counts in the final SVGs: P1 1, P2 1, P3 2,
P4 1, P5 1, P6 0, P7 0, P8 0 — 6 photos total. P6's visual is the
practice-data chart plus boxes; P7/P8 are text pages, as in the W43
pattern. Embedded payloads were MD5-verified against the asset files
(locker, valley, frost, dumplings, lanparty, popcorn — all match). File
photos are captioned 资料图 and never presented as this week's event.

## Adjudications and shortfalls (for the independent proofreader)

- **P4 has no score chart:** deliberate. Final Swiss scores were not yet
  knowable at the 2026-10-27 build cutoff; a chart would have required
  invention. The S16 schedule box + standings note carry the page.
- **6 photos vs W43's 9:** the P6 chart page and the two text pages (P7,
  P8) carry no photo, as in the W43 pattern. The chart plus boxes were
  judged sufficient for P6; whether P6 gains a second visual in a later
  fix round is undecided.
- **B2 share is 25 of 150** (P6 18 + P7 4 + P8 3): the ramp is A2-heavy by
  design for this target; B2 is concentrated in the deep-read page.
- **P8 top rule proximity:** the P8 test flow ends at y = 1262 against a
  bottom of 1252, with the keys rule at y = 1264. The canonical occlusion
  audit reports no flag there (the last ink sits above the rule), but the
  independent proofreader should still eyeball the P8 top rule in the
  final render. Visually checked by the builder: clean.
- **Traditional-character audit method:** `opencc` is **not installed** on
  this VM, so no OpenCC t2s diff was possible. A manual scan for
  traditional-only characters found none (麼 0; the character 鱼 found
  twice is the simplified form in “鸡鸭鱼肉”, not traditional 魚).
- **Start of Winter 17:52 source chain:** see “Trend and fact sources” —
  via the trend pool (jieri8.com + Hong Kong Observatory almanac), not
  independently second-confirmed by direct search.
- **S16 cutoff:** all S16 results are as of 2026-10-27; anything later is
  preview, not result (see “Honesty limit”).

## Builder's proofread record (self-check, final render)

- Driver (single process, content12 → content34 → content56 → content7 →
  content8): TOTAL 150, levels A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, writing model 172 characters, **zero**
  `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings.
- Geometric occlusion audit (`tools/occlusion_audit.py`, selftest first):
  selftest OK (all 6 planted classes fire, clean controls silent);
  **0 flags** on the final SVGs.
- Same-baseline ink-collision scan (furniture-band class the canonical
  audit does not cover): **0 flags** after unescaping `&amp;` in extracted
  SVG text (an initial flag proved to be a measurement artefact: 5 glyphs
  measured instead of 1 for “&”).
- Full text read-through of all 8 pages from extracted SVG text; every
  answer key re-derived against its stem (all 150 match, including all
  five matching sets); dates and weekdays checked with `date -d` (Asia/
  Shanghai): 2026-11-02 Mon … 2026-11-08 Sun, 2026-11-10 Tue, 2026-11-11
  Wed, 2026-11-15 Sun.
- Phrases of the week: all 8 exactly 2× (article + P7) in the final SVGs
  (rendered full-width punctuation). Two collisions found in exercise
  stems during the build were fixed in source and re-rendered (P2 stem
  “下单就能发货的货，叫___。” → “已经在仓库里的货，叫___。”; P4 stem
  “AL三场都输了，战绩是___胜3负。” → “AL一场都没赢，战绩是___胜3负。”).
- Exercise chips contiguous 1–150 across pages (P1 1–10, P2 11–28, P3
  29–46, P4 47–64, P5 65–82, P6 83–100, P7 101–112, P8 113–150). One apparent
  anomaly was a wrapped glossline fragment (a lone “6.” on P6, the second
  line of “Compute from the practice baskets on page 6.”), not a chip;
  the glossline was shortened to “Compute from the practice baskets.” and
  the issue re-rendered.
- P6 bar widths verified in SVG rects: 810 / 537 / 480 px at 3.0 px per
  yuan from zero.
- Kinsoku line-start scan: 0 suspects. Banned intermediary term: 0
  occurrences. Politics scan （战争， 地缘， 外交， 政治， 选举， 民调）: all
  0. Masthead “Lucerna”: 23 occurrences; “The Lucerna” and “Le Lucerna”:
  both 0. P8 “— Page N —” headers present for pages 1–8; P8 key numbers
  1–150 all present in the keys area.
- Visual check of the final cards: P1, P6 (chart page), P7, P8 read
  in full, plus the three previously fixed crops (P1 contents, P2 rule
  area, P4 rule area) — all clean.
- Fixes applied during the build, each followed by a full re-render (never
  patched in output): two `HEAD TOO WIDE` heads shortened (P2 feature head,
  P7 A2 head); P7 column-3 overflow fixed by shortening the disclosure
  note, three error-clinic rules, and the sentence-frame tail (column 3
  ends at y = 1708.1, teaser ends at y = 2554.1, above the 2580 footer
  line); three occlusion flags fixed (P1 contents title shortened; P2
  gold-rule paragraph moved; P4 exercises block moved down); P6 contents
  title shortened as a 2 px precaution.

## Reproduction

Build code lives in
`hidden_files/weekly-report-w45-zhcn-build/` (bslib4.py, svglib.py,
run.py, render.py, content12.py, content34.py, content56.py, content7.py,
content8.py, assets/). Content modules run only through the single
one-process driver; never run a module standalone and never import one
inside a core build directory (their module-level code executes on import
and their OUT paths point at a shipped edition directory).

```bash
cd hidden_files/weekly-report-w45-zhcn-build
../../tools/venv/bin/python run.py        # single-process driver
../../tools/venv/bin/python render.py     # svg -> cards PNG -> print + web PDF
cd ../../tools
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-zhcn-core
```

(Use `tools/venv/bin/python` — never the ephemeral `/tmp/wp-venv`.)

## Post-proof fix record (2026-10-27, finisher — the ONLY post-proof change)

- **Trigger:** independent proof report
  `hidden_files/w45/zhcn-core-proof/PROOF-REPORT.md` — NOT ZERO-PROBLEMS
  on exactly 1 numbered item; every other SOP §8 item passed (occlusion 0,
  P8 150/150, levels A2 56 / B1 69 / B2 25, P7 phrases ×2, facts/dates/
  weekdays, Double 11 schedule, Start of Winter 17:52, S16 cutoff
  statement, films, red line, W43 commitments, image credits, Simplified
  purity, abstract). Nothing else in this record re-opens those items.
- **The item:** P4 exercise 55's key could not be derived from the page
  alone. Stem (P4 B group): “TES打赢G2，是一场___。” Key (P8 key 55):
  翻盘, note “TES turned the game against G2 around”. The old P4 body
  only said “TES打赢了G2” — a win is not necessarily a comeback, so the
  key was under-supported on paper (the key's fact itself is true per the
  Sina Oct 26 recap; this was a support gap, not a factual error).
- **Fix (source change, exactly one line in
  `hidden_files/weekly-report-w45-zhcn-build/content34.py:124`):**
  - Before: “再说好消息:IG和TES在10月26日都赢了。IG打赢了HLE,TES打赢了G2,两支队都是2胜1负,进了2胜1负组。……”
  - After: “再说好消息:IG和TES在10月26日都赢了。IG打赢了HLE,TES一度落后,后来翻盘打赢了G2,两支队都是2胜1负,进了2胜1负组。……”
  - Added 9 characters （一度落后,后来翻盘） establishing the
    落后→翻盘 chain in the Q55 context, before the exercise block.
  - NOT changed: the Q55 stem, the key 翻盘, the P8 note, and every other
    stem/key/note in the issue (verified: P8 keys and noted set are
    byte-identical to the proof-round extract).
- **Rebuild (single process, never patched in output):**
  `run.py` (one-process driver, no FLOW OVERFLOW warnings; P4-feature
  ended col 1/2 y=902, bottom 1180) then `render.py` (cards + both PDFs).
  Registry re-verified: TOTAL 150, A2 56 / B1 69 / B2 25, by page
  10/18/18/18/18/18/12/38, writing model 172 characters — all identical
  to the proof round.
- **P4 layout check:** text-node diff old-vs-new P4 SVG shows ONLY that
  paragraph reflowed (137 → 138 text nodes, +1 line, +9 characters);
  every other P4 line is identical. Full-page visual check of the new
  `cards/p4-tiyu.png`: feature columns, schedule box, col-3 boxes and
  exercise block all clean, no overlap, no overflow; Q55 stem visible
  in place.
- **Gates re-run on the rebuilt files:** `occlusion_audit.py --selftest`
  OK (6 planted classes fire, clean controls silent); full audit on the
  core dir: **0 flags**. `p8.py extract --total 150`: **noted set
  150/150**, key 55 = 翻盘; chain re-verified end to end — new body
  （TES一度落后,后来翻盘打赢了G2) → stem “TES打赢G2，是一场___。” →
  key 翻盘 → note “TES turned the game against G2 around”.
- **P8 rule line visual:** new `cards/p8-ceyan.png` cropped around the
  rule: last test-flow baseline 1232.7 (“凉。”), rule line y=1264
  unchanged, clean gap above and below the line, no text touching it.
- **Files after this fix (measured, not carried over):** print PDF
  `Lucerna-VOL2.pdf` 44,361,569 bytes, 8 pages (was 44,360,790);
  web PDF `Lucerna-VOL2-web.pdf` 3,141,620 bytes, 8 pages (was
  3,140,556). Visible text 23,038 / 26,765 characters (was 23,029 /
  26,756; delta exactly +9, confirming no other page's text changed).
- **Status after this fix:** NOT finalised. The pre-fix proof does not
  automatically carry over; an independent re-proof of this new round
  is still owed (separately assigned). No Discord delivery, no main-chat
  card/PDF delivery, no cron, no weekly-git touch was made by this
  finisher.
