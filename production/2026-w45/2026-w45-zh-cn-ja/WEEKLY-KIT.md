# WEEKLY KIT — W45 Simplified Chinese × Japanese reader edition

**Status: BUILT, not finalized.** Independent proofread by the coordinator
is still owed. Nothing in this file claims shipment to Discord, the GitHub
weekly repo, or main chat.

- Slug: `2026-w45-zh-cn-ja`
- Pairing: TARGET Simplified Chinese (zh-cn) · reader native Japanese (ja)
- Issue week: Monday 2026-11-02 to Sunday 2026-11-08 (VOL.2, issue 2)
- Masthead: bare `Lucerna` (Chinese is article-less; no article prefix)
- Pages: 8, 1950×2700 px cards, 4 columns, ivory `#f7f1e2`, deep olive
  accents, brick `#a4553a` for the pairing badge
- Exercises: 150 total, unified numbering 1–150, no gaps or duplicates
- Levels: A2 56 / B1 69 / B2 25 (A2→B2 ramp, free per-item mixing)
- By type: 完成句子 68, 单选 50, 词语配对 20, 完形单选 11, 写作 1
- Deliverables in this directory: `svg/` ×8, `cards/` ×8 (1950×2700 PNG),
  `Lucerna-VOL2-JA.pdf` (print, 8 pp), `Lucerna-VOL2-JA-web.pdf` (web,
  8 pp, <10 MB), `WEEKLY-KIT.md` (this file), `ABSTRACT.txt`

## 1. Per-page content

- P1 头版 (1–10): Double 11 × Start of Winter lead, calendar box, word of
  the week 「立冬」, parcel-locker photo, briefs, quick quiz.
- P2 生活 (11–28): Double 11 shopping life — spot goods, direct cuts,
  old vs new rules, winter life, shopping word cards, calendar.
- P3 文化 (29–46): Start of Winter — the 19th solar term, three
  micro-seasons, regional eating customs, Journalists' Day (Nov 8).
- P4 体育 (47–64): S16 — Swiss stage through the 2026-10-27 cutoff, fourth
  round draw, quarter-finals Nov 4–7, final Beijing Nov 15 03:00.
- P5 青年 (65–82): AI film 《三星堆：未来往事》 + Start-of-Winter film
  《我们仅有一次的人生》 (nationwide Nov 7).
- P6 深读 (83–100): why Double 11 rules got simpler; practice-data bar
  chart only (no photo page by design, as in W43).
- P7 词语精讲 (101–112): shopping/winter words, time-and-date grammar,
  news-reading B2 frame, error clinic, sentence frame, readers' corner,
  phrase bank, next-issue teaser.
- P8 测验与答案 (113–150): full test (A 判断对错, B 综合 quiz,
  C 完成句子, D 读一读答一答, E 情景说话, F 写作) + all 150 answer keys
  with a note on every answer. Writing topic 《我的立冬周末》, model
  answer 172 characters (see §7).

## 2. Measured quantities (this edition, measured — not copied)

- Print PDF: 8 pages, 41,688,105 bytes,
  SHA-256 `239fc08d022d90481a80a7f7bfc1da23f31916e62f3838af0b64421b1083f32c`
- Web PDF: 8 pages, 3,118,383 bytes (<10 MB),
  SHA-256 `d783b566028a6c43e90b2b2dc95ae9d657791f4ceea4c5dffd89760764a7df5d`
- Cards: 8 PNG, each 1950×2700 (verified with Pillow).
- Visible text extracted from the 8 shipped SVGs (`<text>` node strings):
  18,130 characters without whitespace / 19,948 with whitespace, per page
  1744 / 2066 / 1518 / 1768 / 1724 / 1756 / 2128 / 5426 (no-space).
  NOTE: the core KIT's figures (23,038 / 26,765) use an unrecorded method
  and are NOT directly comparable — they plausibly count stored exercise
  notes a second time on top of the printed keys area (the gap ≈ one full
  note set). Do not present either figure as a parity check; the binding
  conservation proof is §7 (0 missing core Chinese runs).
- Registry on every render: TOTAL 150, levels A2 56 / B1 69 / B2 25,
  pages 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38 — identical to the core.
- Gloss count (rendered `gloss()` string split on `·` itself, per tools
  README #21): core 10 calls, counts [4,4,4,3,3,3,3,3,3,3], total 33;
  this edition 10 calls, same counts, total 33 — equal item by item.
- Photos embedded per page: 1 / 1 / 2 / 1 / 1 / 0 / 0 / 0 = 6 total.

## 3. Trend and fact sources (inherited from the core KIT)

The core's sourcing, reused with attribution; no fact was re-reported
without the core's chain:

- Double 11: JD spot sales from 20:00 2026-10-12; 开门红 20:00
  2026-10-20; activity to 2026-11-13. Taobao/Tmall presale from 20:00
  2026-10-15; tail-payment + spot from 20:00 2026-10-20 to 23:59
  2026-11-13 (source: 2026-10-08 Sina Finance platform timetable).
  Peak sale 20:00 2026-11-10 to 24:00 2026-11-11 is NEXT week and is
  mentioned only as such. WeChat shop first Double 11, 2026-10-12 to
  2026-11-15, 35 days. 18th Double 11.
- Start of Winter: Saturday 2026-11-07 17:52 交节 Beijing time, 19th solar
  term (source chain via Batch D trend pool citing jieri8.com + Hong Kong
  Observatory almanac — NOT independently second-confirmed by direct
  search, per the core KIT honesty note). Three micro-seasons 一候水始冰,
  二候地始冻, 三候雉入大水为蜃.
- S16: venue/stages, Swiss format, verified results through the 2026-10-27
  cutoff (LPL 0–4 round 1; 2026-10-26 IG beat HLE, TES beat G2, BLG beat KC,
  all 2–1; GEN/DK 3–0 through; AL/TSW 0–3 out; AL lost to KC, then to TES,
  then 0–2 to TL on 2026-10-27, 0–3 series / 0–4 games). Fourth-round draw
  BO3 2026-10-29–31. Quarter-finals Nov 4–7, semi-finals Nov 8–9, final
  Beijing Nov 15 03:00 Beijing time.
- Films: 《三星堆：未来往事》 released 2026-10-23, Bona, 100 min, Maoyan
  ~1.192M yuan cumulative by noon 2026-10-26 over 4 days, 24–25 Oct
  averaging 2 viewers/screening (conflicting first-day figures
  deliberately not printed). 《我们仅有一次的人生》 nationwide Sat
  2026-11-07, dir/writer Sun Aoqian, Song Jia as Huang Yan, Wen Qi as
  Yao Xue, original title 《余烬》, Beijing International Film Festival
  Tiantan Best Cinematography, 114 min, slogan “别以后，就现在”.
- Journalists' Day Sunday 2026-11-08. Mid-term exams in some schools early
  Nov (not a national date — printed as such).
- Editorial red lines honored (inherited): no international politics; no
  Chinese domestic politics (target country is China); no anniversary
  material (长征胜利90周年 was rejected at core stage).
- Honesty limits carried from the core: P4 has no score chart (final Swiss
  scores not knowable at the 2026-10-27 cutoff); 6 photos vs W43's 9 (P6
  chart page + P7/P8 text pages carry no photo, as in the W43 pattern);
  B2 share 25/150 by design; P8 top rule proximity (test flow ends y=1262
  vs bottom 1252, keys rule y=1264 — canonical audit reports no flag,
  builder visually checked clean); `opencc` not installed on the VM, so no
  OpenCC t2s diff was possible (manual traditional-only scan found none
  at core stage; this edition adds no new target text at all, so the
  question does not re-arise).

## 4. Images and licences

All 6 photos are CC0/public domain, credits taken from the Wikimedia
Commons API Artist field directly (core `assets/CREDITS.md`, verified
2026-10-27). The same asset files are embedded here (copied with the
build); per-page embedded-image counts verified on the shipped SVGs:
1 / 1 / 2 / 1 / 1 / 0 / 0 / 0.

| Page | Asset | Subject as captioned | Artist (Commons API) | Licence |
|---|---|---|---|---|
| 1 | locker.jpg | Parcel locker, labelled 资料图 (file photo) | Map hobby | CC0 |
| 2 | valley.jpg | Autumn valley, red leaves in season | Paul Gilmore | CC0 |
| 3 | frost.jpg | Frosted red leaves | Gerda Arendt | CC0 |
| 3 | dumplings.jpg | Dumplings, labelled 资料图 (file photo) | Syced | CC0 |
| 4 | lanparty.jpg | LAN-party file photo, France, 2003 | Syced | CC0 |
| 5 | popcorn.jpg | Cinema popcorn bucket, labelled 资料图 (file photo) | Based5290 | Public domain |

File photos are captioned 资料图 and never presented as this week's event.
The P4 LAN-party caption states its real date (2003) and place (France).

## 5. Reproduction build

- Build dir: `hidden_files/weekly-report-w45-zh-cn-ja-build/` (copy of the
  core build `hidden_files/weekly-report-w45-zhcn-build/`).
- Step 1 baseline: `tools/freeze.py baseline` reproduced the core's shipped
  SVGs **8/8 byte-identical** before any change. Core SVG hash prefixes
  (recorded in `core-svg-hashes-before.txt`): p1 e057bbfcdfcd6fca, p2
  c87aa67eb6785a58, p3 d50f09e1a72b6fd3, p4 dd3b1b0fdc80627a, p5
  c71ef3153d70701c, p6 b06a85d276db8a53, p7 f2319cb8997f8d36, p8
  eaf368f8dca48dff. The baseline run itself left the core SVGs unchanged.
  One false start: `--out` inside the build dir caused a `freeze.py`
  copytree recursion; rerun with a sibling scratch dir.
- Step 2 method: the explanation-slot inventory was taken by diffing the
  W45 core build against the sibling W45 zh-cn-nl build (the nl diff is the
  complete explanation-slot inventory for W45 content). Transform script
  `scratch/transform_ja.py`: exact-literal substring replacements,
  longest-first, each asserted to match ≥1 time; no AST byte-offset
  splicing (tools README #17/#18). 267 pairs applied, log in
  `scratch/transform-log.txt`. A cross-check against the nl diff found 4
  missed pairs, applied as a second pass (`scratch/patch_ja_4.py`, also
  appended to `transform_ja.py` as PAIRS2). After the patch, the
  changed-line set vs the core equals the nl changed-line set minus only
  the 6 deliberately kept "Photo:" lines, and mine-only changed lines = 0
  in all six files (content12/34/56/7/8, bslib4).
- OUT repoint verified: content files point to
  `files/weekly-report-w45-zh-cn-ja/svg`; no `weekly-report-w45-zhcn-core`
  references remain in the build `*.py`. `render.py` BASE repointed to
  this edition dir; PDF names `Lucerna-VOL2-JA.pdf` /
  `Lucerna-VOL2-JA-web.pdf` (mirroring the nl build's naming pattern).
- The core build dir was never imported from and never written to: all
  execution went through `freeze.py` or the build's single one-process
  driver `run.py`. Every content change below was a source change followed
  by a full one-process re-render — no SVG was ever patched in output.
- Baseline inherited: this edition reproduces the core AFTER its single
  post-proof fix (2026-10-27: P4 exercise 55 key support gap fixed by
  adding 9 characters （一度落后,后来翻盘） in `content34.py:124`; P8
  keys byte-identical to the proof round). The fixed sentence is visible
  on the shipped P4 card.

## 6. Proof log (builder self-checks; coordinator proof still owed)

- Baseline: 8/8 byte-identical (see §5).
- Freeze diff (final render, no `--strict-cjk` — meaningless for a
  Japanese explanation layer): per-page added/removed strings — p1
  +43/−45, p2 +58/−59, p3 +36/−36, p4 +40/−40, p5 +39/−40, p6 +38/−38,
  p7 +78/−83, p8 +190/−198. Total added CJK characters 5408 (comparable
  to W43 ja's 5073; expected for a Japanese explanation layer). JSON in
  `scratch/freeze-diff.json`.
- `p8.py compare` vs the core (target zh-cn): **CLEAN, 150 noted = 150
  noted, missing=[], extra_count=0, uncertain=[], keydiff=[]** — printed
  note set EQUAL, passing the hard gate.
- `occlusion_audit.py`: selftest OK (all 6 planted classes fire, clean
  controls silent). Edition audit **0 flags**; with `--core`: core 0
  flags, **NEW vs core: 0**. JSON in `scratch/occlusion.json`.
- Same-baseline ink-collision scan (adapted W43 `rowcheck.py`, with
  `html.unescape` on node text to avoid the known `&amp;` 5-glyph
  measurement artefact): **collisions: 0** across all 8 pages, including
  the P1 top band.
- P6 chart-label element check: bars identical to the core — (325, 1282,
  810×34), (325, 1340, 537×34), (325, 1398, 480×34). Row-label ink right
  edges 201.0 / 140.8 / 177.8, all < 325 (bar start). Value labels at bar
  end +16 (x=1151 / 878 / 821 for 270元 / 179元 / 160元). No label/bar/text
  overlap; confirmed on the P6 card.
- Render warnings: **0 FLOW OVERFLOW / 0 HEAD TOO WIDE** on the final
  render (and on every render after the first fix round).
- Cards eyeballed by the builder, all 8: no overflow, no overlap, no
  missing glyphs, footer + page line on every page, P1 masthead/badge,
  P6 chart, P7 corner/teaser, P8 keys top rule all clean.

### Self-fixed defects (source change + full re-render each time)

1. **P7 teaser pushed into the footer band (first render).** P7 col3 ended
   1795.1 (core: 1708.1) because the first Japanese readers'-corner
   disclosure wrapped to 13 lines vs the core's 10, pushing the P7 teaser
   box to end at 2641.1, i.e. into the footer band (core teaser ends
   2554.1; footer line 2580). Pre-fix P7 SVG preserved at
   `scratch/p7-prefixed.svg`. Fix: shortened the Japanese tail of the
   `lcn` disclosure in content7.py to: `編集部注：VOL.1で予告した本物の手紙と最優秀作文はまだ届いていません。今号も編集部の例文を掲載します。延期であって中止ではありません。中国語の手紙をぜひお寄せください！`
   Wrap-verified with a scratch copy of svglib (`scratch/wrapcheck_svglib.py`):
   10 lines, exactly the core's count. After re-render: P7 col3 ends
   1708.1, teaser ends 2554.1 — exactly the core's values, registry
   identical.
2. **Japanese line-start small kana orphan (orphan scan, second render).**
   1 flag: P7 line starting with って (`って中止ではありません。中国語の手紙を`),
   inside the readers'-corner disclosure. Fix: extended NO_START in MY
   copy's svglib ONLY with the small-kana set
   (ぁぃぅぇぉゃゅょゎっ and katakana equivalents), with a comment citing
   this scan. Rationale: the JA-target NO_START precedent does not
   automatically apply to a zh-cn target, but small kana never occur in
   Chinese target text, so frozen lines cannot be affected — and the
   mechanism is the codebase's own oidashi (pull previous line's last
   character down; line count unchanged). After full re-render: orphan
   scan **0 flags**, NO_START/NO_END line-start closers 0 / line-end
   openers 0, P7 col3/teaser unchanged (1708.1 / 2554.1), registry
   identical, and the lcn lines now read `…掲載します。延期で` /
   `あって中止ではありません。中国語の手紙を` — confirmed on the P7 card.
   The core's svglib was not touched: diff vs the core's svglib is ONLY
   this extension + its comment (5 added lines).
3. **Basket-B note unit (residual-Latin adjudication, final render).**
   The P6 C-group basket-B note read `199 − 20 = 179 yuan.` — carried
   over untouched because the nl diff (Dutch "yuan" = English "yuan")
   gave no signal, while every sibling basket note uses 元. Fix:
   `content56.py:221` → `199 − 20 = 179元。`, matching the sibling notes
   and the P6 chart value labels. After re-render: registry identical,
   p8 still CLEAN, P8 key 94 now reads `94. 179 — 199 − 20 = 179元。`
   (confirmed on the P8 card). This was the only genuine English residue
   found in the full 441-line residual-Latin adjudication (see §7).

### Readers'-corner compliance

The core P7 corner (Chinese letter, frozen target text) is kept, and its
mixed Chinese/English disclosure `lcn` keeps the Chinese half frozen while
the English tail is replaced by the Japanese disclosure above, which (a)
discloses on-page that no genuine reader letters exist (labelled editor's
example + deferral: VOL.1 promise, none arrived, still editor's example,
deferred not cancelled) and (b) contains an EXPLICIT open invitation:
`中国語の手紙をぜひお寄せください！` A teaser line or another page's
exercise prompt was not counted as the invitation.

## 7. String-level CJK gate evidence (the binding target-text proof)

The literal `--strict-cjk added = 0` char gate was NOT applied: it is
meaningless when the reader language is Japanese, because the explanation
layer itself is CJK. The gate applied instead, at STRING level:

- **Chinese-run conservation: 0 missing core Chinese runs on all 8 pages**
  (121 / 140 / 109 / 130 / 124 / 144 / 135 / 180 runs per page, after
  removing replaced furniture strings). This is the zero-diff proof for
  Simplified target text. Script `scratch/attribute_ja.py`, full output
  `scratch/attribute-out.txt`.
- **Removed strings needing manual adjudication: only 6, all explained** —
  P1 word-of-week example sentence `「立冬那天，我们吃饺子。」`
  (reflowed across two lines in this edition, sentence intact per
  conservation); P7 `件.` (tail fragment of the English error-clinic
  sentence "sweaters take 件."); 4 P8 MODELO reflow lines
  (punctuation-normalised joined MODELO text verified separately below).
- **Added strings without kana: 45, all adjudicated** (full list in
  `scratch/attribute-out.txt`): wrapped gloss-line fragments (e.g.
  `解説 — xiànhuò 现货 —`, `解説 — cāngkù 仓库 — 倉庫 · píngjià 评价`,
  `· qīzhōng 期中 — 中間試験。`, `guǎnggào 广告 — 広告。`); wrapped note
  fragments (`来週開始`, `援）。`, `本）。` — the last confirmed as the
  tail of the P7 A2 glossline `量詞は今も大切：一件毛衣（セーター1着）、一条围巾（マフラー1本）、一部电影（映画1本）。`;
  `最後。`, `气，再出门。」`); B1-para example fragments; kana-less
  Japanese furniture/words in bilingual heads — `本期目录 · 目次`,
  `练习 · 練習問題` (×5), `文化 · 文化特集`, `青年 · 若者`,
  `S16 赛程 · S16日程（北京時間）`, `下期预告 · 来週（VOL.3）`, P8 writing
  instruction label `作文`; kana-less single-word Japanese glosses in P8
  notes (`決勝`, `興行収入`, `主張`, `決済画面`, `配送料`, date notes
  `立冬、11月7日。` on items 34/103, and `約119.2万元` keeping the article's
  万元 unit); date line `11月2日—8日 · 11月2～8日`; reflowed frozen
  example lines (`立冬到了，冬天要来了。例文：「立冬那天，` /
  `我们吃饺子。」`).
- **Edition-only Chinese runs: 552 total** across pages (p1 52, p2 56, p3
  42, p4 48, p5 42, p6 43, p7 96, p8 173). These are Japanese
  furniture/notes words plus quoted Chinese terms. NOTE: the run list
  joins lines without separators, so some entries are line-boundary
  concatenation artefacts (e.g. `本物の中国を、中国語で読む中国語`) —
  not real strings. No entry is a new Simplified target sentence.
- **MODELO check:** joined model-answer text is **identical raw, 172
  chars**, core vs edition — only line-break positions differ (narrower
  Japanese prefix `モデル解答：` vs `Model answer: `). An earlier "not
  equal" result was an extractor bug (it ran past the answers head);
  corrected extractor stops at the `答案` head line.
- **Residual-Latin adjudication (full, 441 lines in
  `scratch/residual-latin.txt`):** every Latin-bearing line falls in an
  expected class only — frozen Chinese text with Latin tokens (VOL / S16
  / AI / JD.com / Maoyan / AL / IG / TES / BLG / team codes, level badges
  A2/B1/B2, option letters A/B/C, `(p. N)` phrase tags kept from the core
  as in W43 ja), pinyin in the frozen gloss format, `Lucerna`,
  Photo/Wikimedia/Commons credits (kept in English per §8), JA furniture
  with VOL.2, and proper-name citations (Sina Sports, Worlds S16). An
  ASCII word-run census found no English explanation words; the single
  genuine residue (`yuan` in the basket-B note) was fixed (§6 defect 3).
- **No new Simplified target text was added and none was removed.**
  This is a zh-cn TARGET edition: nothing was converted between scripts.

## 8. Furniture three-way (verified from shipped SVGs, never from memory)

Badge slot/size case: **in-place replacement at the zh-cn core family's
own badge slot** — (975, 434), 19.5pt, BRICK `#a4553a` — because y=372 is
the frozen bilingual strapline, not a free slot. This is NOT the EN/DE/ES
subtitle-slot case (y≈372) and NOT the FR/IT inserted-badge case (y=574,
22pt). The core family itself carries a badge line at y=434 (long English
form); the JA badge replaces that whole line including the OLIVE → BRICK
colour change.

| Element | W45 core (EN) | W43 shipped same-pairing (zh-cn×ja, VOL.1) | This edition (W45, VOL.2) |
|---|---|---|---|
| Pairing badge (975, 434, 19.5pt) | 简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers | 中国語（簡体字）テキスト · 日本語の解説 — 日本語読者のための版 | Same as W43, verbatim |
| Top strip y=92 | 每周读中文 · Read real Chinese, every week | 每周读中文 · 本物の中国語を、毎週読もう | Same as W43, verbatim |
| Strapline y=372 | 给学中文的人的周报 — Read the real China, in Chinese | 给学中文的人的周报 — 本物の中国を、中国語で読む | Same as W43, verbatim |
| Edition line y=330 | 简体中文版 · VOL.2 · 双11 · 立冬 · S16 | 简体中文版 · VOL.1 · 双11 · 大闸蟹 · 霜降 | Frozen Chinese (core's line, kept) |
| Footer | Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations | Lucerna · 中国語（簡体字）週刊 VOL.1 · 本文は中国語（簡体字） · 解説は日本語 | W43 pattern with VOL.2: Lucerna · 中国語（簡体字）週刊 VOL.2 · 本文は中国語（簡体字） · 解説は日本語 |
| Page line | 第 {n} 版 / 共 8 版 | {n} ページ（全 8 ページ） | Same as W43, verbatim |
| Gloss prefix (bslib4) | Notes｜ | 解説 — | Same as W43, verbatim |
| P8 separators | — Page {n} — | — {n} ページ — | Same as W43, verbatim |
| P8 answer head | 答案 · Answer keys — by page, with a note on every answer | 答案 · 全解答と解説（1–8ページ） | Same as W43, verbatim |
| P8 right note | All notes in English · ✓ = the writing task | 解説はすべて日本語 · ✓ = 作文の課題 | Same as W43, verbatim |
| P8 answer style | Dash: `{n}. {key} — {note}`; writing `{n}. ✓ {note}` | Same (dash style) | Same — kept byte-identical from the core's shipped P8 SVG code path |

Recurring W43-ja Japanese halves reused verbatim where the Chinese head
matches: 头条 · トップ記事, 生活 · 暮らし, 体育 · スポーツ, 深读 ·
深く読む, 词语 · 言葉の焦点, 测验与答案 · テストと答え, bylines
`Lucerna 編集部 · 読解レベル A2/A2→B1/B1/B2`, band prefix `レベル …`,
说说你自己 · あなたは？, 你知道吗 · 知ってた？, 即学即练 · すぐ練習,
闪电问答 · クイッククイズ, 本周词 · 今週の言葉, 数字看本周 · 数字で見る今週,
本周金句 · 今週のフレーズ（今号の記事からそのまま抜粋）, 购物词语卡 ·
買い物言葉カード, 本周生活小日历 · 今週の日付, 节日小日历 · 祭りの日付,
体育小日历 · スポーツ日程, 这一周的高频词 · 今週の頻出語, 练习例子 pattern,
A/B/C/D/E/F exercise heads (読んで選ぼう / 単語を入れよう / ペアにしよう /
正しいか間違いか / 総合クイズ / 文を完成させよう / 読んで答えよう /
会話の場面 / 書いてみよう), `1ページを読んで選ぼう · 答案见第 8 版`,
`答えは8ページ · 答案见第 8 版`. Fresh translations (no W43 precedent):
文化 · 文化特集, 青年 · 若者, 练习 · 練習問題, 本期目录 · 目次,
下期预告 · 来週（VOL.3）.

### Deliberate non-changes (W43 same-pairing precedent)

- "Photo:..." credit lines kept in English (attribution, not explanation)
  — unlike the nl build, which used "Foto:". 6 Photo lines total across
  content12/34/56.
- P8 writing registry key `(开放题，范文如下)` kept in Chinese. It never
  prints: content8.py prints writing items as `{n}. ✓ {note}`. W43 ja
  precedent had keydiff=[] with the key kept Chinese.
- P8 answer-format code in content8.py left byte-identical (dash style;
  see table). Verified from the core's shipped P8 SVG code path, not from
  memory.
- svglib.py kept byte-identical to the core for the first renders (SC face
  index, existing NO_START/NO_END). W43 ja used a JP-face hybrid, but
  switching face would reflow all frozen text; SC face renders kana. The
  only svglib change in the shipped edition is the NO_START small-kana
  extension (§6 defect 2), which cannot affect frozen Chinese lines.

## 9. Toolchain

- Interpreter: `tools/venv/bin/python` — Python 3.12.3
- Pillow 13.0.0, cairosvg 2.9.1, pypdf 6.21.2
- Canonical tools: `tools/freeze.py`, `tools/p8.py`,
  `tools/occlusion_audit.py` (selftest first, every run)
- Builder scratch (not deliverables): `hidden_files/weekly-report-w45-zh-cn-ja-build/scratch/`
  — transform_ja.py (+ PAIRS2), patch_ja_4.py, transform-log.txt,
  attribute_ja.py → attribute-out.txt, rowcheck.py, checks_ja.py →
  checks-out.txt, residual-latin.txt, wrapcheck_svglib.py, occlusion.json,
  freeze-diff.json, run1–run5.log, p7-prefixed.svg (pre-fix P7),
  core-svg-hashes-before.txt

## 10. Open notes for the coordinator

- This edition is BUILT, not finalized: independent proofread is owed
  before any repo insert. No Discord post, no repo action, no chat dump
  was made by the builder (per task iron rules).
- `ABSTRACT.txt` is present in the edition dir (Japanese single line, no
  ASCII double quotes: masthead + target language name + A2–B2 + 150
  exercises + real topics + learner search phrase).
- Known inherited limitation (from the core KIT, not introduced here):
  the Start-of-Winter 17:52交节 source chain was not independently
  second-confirmed by direct search.
- If the coordinator's proof changes any note text, the change must go
  through source + a full one-process re-render, never a patched SVG.
