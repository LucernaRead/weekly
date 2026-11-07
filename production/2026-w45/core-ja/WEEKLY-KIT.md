# Lucerna 日本語版 · Japanese Weekly — VOL.2 Production Kit (W45)

Week: **Monday 2 – Sunday 8 November 2026** · Issue dated **Monday 2 November 2026** · Core edition: **Japanese text + explanations in the reader's native language (Chinese)** — the same convention as the VOL.1 core (Japanese articles, small gray Chinese glosses/notes/answer explanations only). For abstract purposes this core IS the zh-cn edition: ABSTRACT.txt is written in Simplified Chinese.

Build directory: `hidden_files/weekly-report-w45-ja-build/` (content12.py, content34.py, content56.py, content7.py, content8.py, bslib4.py, svglib.py, render.py, run.py, assets/ + CREDITS.md). The build is the VOL.1 pipeline copied and repointed (same Python → SVG → CairoSVG → PNG/PDF code, same patched svglib md5 d73e23b3… with SEAM_SLACK repair); no new pipeline was invented.
Deliverables here: `svg/` (8), `cards/` (8 PNG @1950×2700), `Lucerna-VOL2.pdf` (print, 8 pp, 24,935,301 B), `Lucerna-VOL2-web.pdf` (web, 8 pp, **2,912,339 B**, sha256 `3c7ddf70d0374d03c5440fff371eb93c788391587733bb5908564b95b8a49e6d`, under the measured ~10 MB server limit), `ABSTRACT.txt`.

## Spec (per SOP)

- 8 pages (multiple of 4 ✓), 1950×2700 units, 4 columns, warm ivory `#f7f1e2`, deep olive accents (`#3e4c2a`), brick chips.
- Masthead: blackletter **Lucerna** with **NO article** — Japanese is an article-less language per the SOP masthead rule (tables.json: article null). The paper's name inside the text: 『Lucerna』日本語版.
- Ramp, not silos: P1 front A2 · P2 life A2 · P3 culture A2→B1 · P4 sport B1 · P5 youth B1 · P6 deep read B2 · P7 language focus (A2/B1/B2 columns) · P8 assessment + writing + ALL keys. Every exercise individually level-badged; levels mix inside pages.
- House style: です・ます throughout; weekday notation 土よう日・日よう日 (full forms, unambiguous for learners); no ruby/furigana (the pipeline cannot render ruby) — readings are given parenthetically for a few words only （見頃（みごろ）is not repeated this issue; new parenthetical readings: 鍋（なべ）, 蒸し器（せいろ）on P2).
- Sources: ONLY the 日本語 section of `hidden_files/w45/trend-batch-C.md` (W45 pool) + the two verified just-passed facts below (Japan Series G1/G2, 2–0-start title rate 73% (past 40 seasons, 29 titles)). Written natively in Japanese from that pool — never translated from another edition.
- Red lines: no international politics (none appears); no invented polls/quotes/stats; lifestyle buzz items are attributed to the note.com Oct 22 X-buzz roundup and explicitly NOT presented as survey data (on P1, P2, P5, P6); all forecasts stay forecasts (JMA Oct 20 3-month forecast, Naruko Gorge forecaster blog Oct 18 from observations to Oct 17, both labeled as such); the P6 chart is labeled 練習用データ (practice data) on the chart itself.
- Terminology rule: the SOP-banned term appears NOWHERE in the pages or in this KIT (checked programmatically, 0 occurrences).

## Lead story

**文化の日と紅葉の週末 — ゆるく整える日本の11月** — Culture Day (Tue Nov 3, national holiday) + peak autumn leaves over the Nov 7–8 weekend (Naruko Gorge peak across the Oct 31 – Nov 8 weekends; Kobe Nunobiki Herb Garden light-up from Sat Nov 7) + the ゆる整え食 winter food trend (Ajinomoto, Oct 21) as the food hook + Reading Week in progress (ends Mon Nov 9) + 立冬 (Sat Nov 7) in the traditional calendar. No anniversary framing anywhere.

## W43 promises honored (per `hidden_files/w45/w43-promises.md`, JA section)

1. **Reading Week in progress Nov 2–8 (ends Nov 9)** — honored as a live thread: P1 lead, P1 mini-feature, P3-adjacent P7 A2 column, P8 reading, VOL.3 preview notes its Nov 9 end.
2. **Japan Series results** — honored PARTIALLY, with the gap stated on the page (see "Verification debt" below): P4 reports the two verified Yokohama games (G1/G2) in full; G3–G7 are listed as schedule only, with the printed note that their results were not verifiable by press time and will be summed up in VOL.3.
3. **Oct 31 Halloween** — covered as a just-passed report framed on the standing rules (Shibuya year-round 18:00–5:00 street-drinking ban, ¥2,000 littering fine since June 2026, Hachiko fenced Oct 30 – Nov 1, Ikebukuro festival Oct 30 – Nov 1 as scheduled). No attendance, arrest, or crowd outcome is claimed anywhere, because no verified outcome source was available.
4. **Readers' corner milestone** — honored HONESTLY, not by fabrication: no real reader letters or best P8 texts had arrived by press time, so P7 prints a clearly labeled editor's example PLUS an on-page disclosure in Japanese and Chinese stating exactly that, with the W43 promise carried to VOL.3 (also printed in the VOL.3 preview box). A KIT-only disclosure would not have passed; the disclosure is on the rendered P7 card.

## Measured totals (one consistent method: visible-text extraction from the final SVGs, tags stripped)

- **Exercises: 150 exactly** (benchmark ~150 met).
  - By level: **A2 46 · B1 75 · B2 29**.
  - By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38.
  - By type: 完成句子 (fill) 50 · 单选 (MC) 51 · 完形单选 (cloze MC) 13 · 词汇配对 (matching, counted per item) 12 · 判断对错 (true/false) 11 · 造句 (sentence building) 8 · 翻译 (translation) 4 · 写作 (writing) 1.
- P8 writing model: 『私の11月の週末』, **167 characters** (counted programmatically, inside the printed 150–200 range).
- P6 practice chart: 近場の満足 38% · 温泉 27% · 紅葉 21% · グルメ 14% = 100%; bar widths measured in code = 30× the values (same formula as VOL.1).

## Per-page contents

- **P1 表紙 (A2)** — masthead (no article, see Spec); date band 2026年11月2日（月）〜8日（日）; headline 文化の日と紅葉の週末; lead article (Culture Day Nov 3, Reading Week to Nov 9, Naruko Gorge peak, Kobe light-up from Nov 7, 立冬 Nov 7); 「数字で見る今週」 (3 / 7 / 9 / 1.5); 6 headline fills; col-3: 今週のトレンド box (ゆる整え食 / 紅葉の週末 / 読書週間 / 暖かい11月, with the note.com attribution caveat), contents, word of the week ゆる; maple photo; 読書週間の今週 mini-feature; 短いニュース (Culture Day / 立冬 / light-up briefs); 4-item blitz quiz. Exercises 1–10.
- **P2 くらし (A2)** — ゆる整え食 feature (Ajinomoto Oct 21: steam baskets, mala-tang, one-pot soups; nabe tables 1.5× vs last year Aug–Oct; nabe ingredients in supermarkets a month early; サクサクdeコパン past 13 million servings in ~1 year) + warm November (JMA Oct 20 3-month forecast: above-average temps Nov–Jan, weak seasonal winds, more rain Pacific side) + attributed lifestyle buzz (peplum knits, check/tweed jackets, no-think consumption, one-dish meals — note.com Oct 22 roundup, explicitly not a survey); numbers boxes; あなたは？ prompt; season-words strip (鍋 / 蒸し器 / ゆる / 整える + model sentence); 18 exercises (11–28).
- **P3 ぶんか (A2→B1)** — Culture Day feature (Nov 3; Suginami family orchestra; Kanazawa 市民美術の日 オープンまるびぃ2026 + 加賀カランコロン market; 第73回日本伝統工芸展金沢展 Oct 30 – Nov 8, 石川県立美術館； 金沢城・兼六園 light-up week incl Nov 7) with a second block 伝統工芸展の見方 (pottery, lacquer, dyeing, metalwork; Kaga Yuzen, gold leaf); Hiroshige III print; culture calendar box; あなたは？ prompt; 18 exercises (29–46).
- **P4 スポーツ (B1)** — Japan Series Yokohama two-game retrospective (G1 Sat Oct 24, SoftBank 3–1 DeNA, 11 innings, 4h12m, 33,388; G2 Sun Oct 25, SoftBank 4–3 DeNA, 10 innings, 3h36m, 33,432; Tsutsugo 3-run HR in the 8th, Yamakawa tying HR in the 9th, Kawamura debut HR in the 10th; SoftBank 2–0 start; 73% stat for 2–0 starts (past 40 seasons, 29 titles); 2024 parallel — DeNA lost two at home then won 4 straight; manager Aikawa quote 「4つ勝つかどうかの戦いなので」 with attribution) + full G1–G7 schedule box (G3–G7 results explicitly deferred to VOL.3, see Verification debt) + two-game record table + 73% explainer box + stadium photo; 18 exercises (47–64).
- **P5 若者・エンタメ (B1)** — Halloween just-passed report (Oct 31; Shibuya rules as above; Ikebukuro festival Oct 30 – Nov 1 as scheduled) + autumn-festival weekend (さがみはらフェスタ2026, 埼玉わんわん秋まつり Nov 7–8, 中区民祭り ハローよこはま2026 Nov 8) + attributed fashion buzz (peplum/check/tweed, note.com Oct 22); pumpkin photo; ハロウィンのことば box; あなたは？ prompt; 18 exercises (65–82).
- **P6 深読み (B2)** — Warm November + autumn travel deep read (JMA forecast; Kyushu travel searches nearly doubling year-on-year with budgets down and 「近くの満足」 — attributed to the note.com roundup, not a survey; Naruko Gorge peak; Kobe light-up Nov 7 – Dec 28) + practice chart （練習用データ）; numbers + travel-words boxes; 18 exercises (83–100).
- **P7 ことば** — A2 column 本と読書のことば (Reading Week in progress, Oct 27 – Nov 9, slogan 「静かだけど、冒険中。」); B1 column 紅葉のことば (見頃 / 紅葉狩り / ライトアップ / 落葉）; B2 column 数字を読む (1.5倍 = 去年より50%多い; 73% ≈ 4人のうち3人; 1,300万食）; error clinic (4: 昨日＋present → past; 趣味は〜です → ことです; 三本 → 三か所 for places; 金沢に → 金沢で for the place of action); frame box 『ゆるく整える』 breakdown; readers' corner (editor's example + on-page Japanese/Chinese no-real-letters disclosure, promise carried to VOL.3); phrases of the week (below); VOL.3 teaser. 12 exercises (101–112).
- **P8 テストと答え** — A week-chronicle cloze (8) · B general MC (8) · C short reading about ミカ + 4 MC · D sentence building (4) · E translation JA↔ZH (4) · F vocabulary matching (4: 見頃/鍋/落葉/予算 → b,d,a,c) · G library-desk dialogue cloze (5) · H writing 『私の11月の週末』 with the 167-character model. 38 exercises (113–150) + ALL 150 keys with a one-line Chinese explanation each, registry-generated.

## P7 phrases of the week — verbatim check

Each phrase occurs **exactly 2×** in the whitespace-stripped concatenation of all SVG text (once in its article, once on P7) — verified programmatically after the final render:

1. 「文化の日は、11月3日（火よう日）です。」(P1) 2. 「ゆっくり、ゆるく整える日本の11月です。」(P1) 3. 「『ゆる』は、無理をしない、ゆっくり、という意味です。」(P2) 4. 「鍋の材料が1か月早く並び始めました。」(P2) 5. 「伝統工芸と紅葉と光を、いっしょに楽しむことができます。」(P3) 6. 「ソフトバンクが2連勝でスタートしました。」(P4) 7. 「ルールを守って、楽しいハロウィンにしましょう。」(P5) 8. 「紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。」(P6)

## Images (4, all reused from the VOL.1 verified set; full record in build `assets/CREDITS.md`; every image confirmed present in the final render)

| Page | File | Subject | Author | License |
|---|---|---|---|---|
| P1 | maple.jpg | autumn maple leaves | Poliphilo | CC0 |
| P3 | hiroshige.jpg | Utagawa Hiroshige III, 1876 imperial-inspection procession print (captioned as a Meiji-era art print for Culture Day arts, NOT as a W45 event photo) | Hiroshige III | Public domain |
| P4 | stadium.jpg | Yokohama Stadium "Dream Gate" — the actual Games 1–2 venue | Syced | CC0 |
| P5 | pumpkin.jpg | jack-o'-lantern pumpkins | Petr Kratochvil | Public domain |

One chart (P6, practice data, labeled) and the P4 two-game record table are drawn in code. No copyrighted modern photography anywhere. No new image was downloaded: the only nabe candidate found (File:Motsunabe.jpg) is CC-BY-SA 3.0 and was rejected under the SOP's PD/CC0-only rule; P2 and P6 therefore carry no photo (same pattern as VOL.1's photo-less P7).

## Sources (all from the approved pool, plus two verified just-passed facts)

- Pool: `hidden_files/w45/trend-batch-C.md`, 日本語 section (lead + items 1–5 + calendar nodes).
- Promises register: `hidden_files/w45/w43-promises.md`, JA section (see "W43 promises honored" above).
- Japan Series G1/G2 scores, innings, durations, attendances, home-run sequence: zh.wikipedia 2026年日本大賽 match table + Daily Sports Oct 25–26 game reports + baseballchannel.jp Oct 25 results page (all crawled Oct 25–26, all agreeing on G1 3–1/11回 and G2 4–3/10回）. The 73% stat (past 40 seasons, 29 titles) and the 2024 parallel (DeNA lost two at home, then won 4 straight) and the Aikawa quote are from Daily Sports, Oct 25–26, attributed on the page; the 73% figure replaces an unverifiable Daily Sports 76% claim corrected in proof on 2026-10-27.
- Arithmetic re-checked in proofread: chart 38+27+21+14 = 100; chart-derived keys 21−14 = 7, 38+27 = 65; 1.5倍 = 去年より50%多い; G1 3–1, G2 4–3; 33,388 / 33,432 attendances as reported.
- Weekdays machine-checked against the 2026 calendar (Nov 2 Mon, 3 Tue, 7 Sat, 8 Sun, 9 Mon; Oct 24 Sat, 25 Sun, 27 Tue, 28 Wed, 29 Thu, 30 Fri, 31 Sat, Nov 1 Sun).

## Builder's proofread (full pass over rendered pages + programmatic suite)

All 150 keys re-derived from the printed stems and article text (registry dumped and reviewed line by line); every gloss glosses a word that appears on its own page (checked against page text); cross-references (（面） tags, contents list, quiz notes) checked; all 8 card PNGs viewed; the following defects were found and fixed in the sources, then re-rendered and re-verified in the final output:

1. P7 teaser band ended below the content limit (2597 > 2540) — quote-row pitch tightened 150 → 140 → 132 and the readers'-corner disclosure shortened; band now ends at 2512.
2. Geometric audit flags (first run, 2 BOXTITLE): P4 73% box note ink 0.7 past its border (box corrected from 76% in proof fix 2026-10-27); P7 letters-box Chinese note ink 9.3 past its border — both box heights padded (+8 / +16); audit now reads 0 flags.
3. P7 phrase over-counts (2 phrases at 3×, not 2×): the P1 lead sentence was repeated verbatim as the P3 feature opener, and the P6 golden sentence was repeated verbatim in the P7 B1 column — both reworded; all 8 phrases now exactly 2×.
4. P3 kinsoku violation: a wrapped line began with the small kana っ (「…作った作品…」 breaking as 「った作品…」) — the sentence was reworded to 「伝統の技による作品」 (same meaning, no っ at the break); kinsoku scan now zero hits anywhere.
5. P4 wording redundancy in the results-gap note — tightened to two sentences; the gap itself is kept and stated, not papered over.

Residual, disclosed: feature-column whitespace remains on P2/P4/P5/P6 (same pattern as VOL.1); P2 and P6 carry no photo (see Images); the P5 Halloween block claims no event outcome (see Verification debt).

## Geometric occlusion audit (tools/occlusion_audit.py, selftest first)

- Selftest: all 6 planted classes fire exactly once; clean controls silent.
- Final run on this edition: **0 flags** (record: `hidden_files/w45/ja-core/occlusion4.json`; earlier runs occlusion1–3.json show the 2-flag → 0-flag fix trail).
- Same-baseline furniture-band scan (P1 top band, PIL widths): left ends 220, center strapline 681–1269, right date starts 1530 — no collisions.

## Verification debt (unresolved, for the parent line — NOT hidden)

1. **Japan Series G3–G7 results (Oct 27 – Nov 1) are NOT in this issue.** All web sources available at build time (Oct 26) stopped at G2 (Oct 25); the series winner and the G3–G7 scores could not be verified and were NOT invented. P4 states the gap on the page and promises the full roundup in VOL.3. If verified G3–G7 results reach the parent line before the Nov 2 ship deadline, P4's schedule box + exercises 47–64's scope can be extended — but as built, the issue is shippable as-is (it never claims a winner).
2. **Halloween Oct 31 outcomes** (attendance, enforcement numbers, festival turnout) are likewise unclaimed on P5 for lack of a verified source; only the standing rules and the scheduled dates are printed.
3. **Lifestyle buzz items** (fashion, Kyushu travel) rest on the note.com Oct 22 X-buzz roundup, not survey data — attributed as such on every page that uses them, per the pool's caveat.

## VOL.3 promises registered (printed on P7; must be honored next issue)

1. Reading Week ends (Mon Nov 9) — closing report.
2. Japan Series final-result roundup (the G3–G7 gap from this issue).
3. 紅葉の見頃の続き (foliage-peak continuation).
4. Real readers' letters + the best P8 『私の11月の週末』 writing (the W43 promise, carried from VOL.2's honest disclosure — VOL.3 must print them if they arrive, or disclose again if they have not).

## Reproduction

```bash
cd hidden_files/weekly-report-w45-ja-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py     # content12+34+56+7+8 in ONE process (registry order = numbering)
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py  # svg -> cards PNG -> Lucerna-VOL2.pdf + Lucerna-VOL2-web.pdf
```

Fonts: Noto Serif/Sans CJK (JP face) + UnifrakturMaguntia (masthead). Never use /opt/meta-chromium (hangs in this VM).
