# INDEPENDENT PROOFREAD — W45 Simplified Chinese × Japanese (zh-cn × ja)

**Verdict: NOT PASS — one blocking item (Gate 10, standalone reproduction).**
**Nothing is declared shipped.** All content/layout gates pass; the single
blocker is that the standalone reproduction record does not reproduce the
delivered SVGs (6/8, not 8/8). The builder's fix is mechanical and the
reproof is cheap — see §Blocking.

- Edition dir: `files/weekly-report-w45-zh-cn-ja/` — svg ×8, cards ×8
  (1950×2700 PNG), `Lucerna-VOL2-JA.pdf`, `Lucerna-VOL2-JA-web.pdf`,
  `WEEKLY-KIT.md`, `ABSTRACT.txt`
- Build dir: `hidden_files/weekly-report-w45-zh-cn-ja-build/`
- Core: `files/weekly-report-w45-zhcn-core/` (150 exercises, A2 56 / B1 69 / B2 25)
- W43 same-pairing reference: `files/weekly-report-zh-cn-ja/`
- Proof work (this report's evidence): `hidden_files/w45/zh-cn-ja-proof/work/`
  (`decompose.py`, `conserve.py`, `orphan.py`, `rowcheck.py`,
  `freeze-diff.json`, `occlusion.json`, `repro-build/`, `repro-core/`,
  `regen/`, logs)
- Method note: no subagents were spawned; nothing was written to
  `~/workspace/weekly-git`; `insert.py` was not run; nothing was posted
  to Discord or main chat; no cron jobs created; no shared scratch dirs
  cleaned. No content module was ever imported inside the core build dir
  — all re-renders ran on fresh copies under this proof dir with OUT
  repointed to the copy.

## Pre-flight duplicate check — PASS (proceed)

- (a) No live worker/process writing to the delivery/build dirs
  (`ps aux | grep weekly|zh-cn-ja|w45` empty at start).
- (b) Two mtime snapshots of both dirs, minutes apart, ZERO changes
  (`mtime1.txt` vs `mtime2.txt` identical).
- (c) Builder session completed: delivery files all dated Oct 28 07:52–07:59,
  KIT states "BUILT, not finalized", no writes since.

## PDF pins re-verified (coordinator pins match exactly)

- Print `Lucerna-VOL2-JA.pdf`: 41,688,105 B,
  SHA-256 `239fc08d022d90481a80a7f7bfc1da23f31916e62f3838af0b64421b1083f32c` ✓
- Web `Lucerna-VOL2-JA-web.pdf`: 3,118,383 B (<10 MB),
  SHA-256 `d783b566028a6c43e90b2b2dc95ae9d657791f4ceea4c5dffd89760764a7df5d` ✓
- Regen of the print PDF from the delivered SVGs (same render code) is
  byte-identical to the delivered print PDF (same SHA, same size) — see Gate 12.

## Gate 1 — Freeze baseline + diff decomposition — PASS

- `tools/freeze.py baseline` on the core build: **8/8 byte-identical**,
  core SVGs re-hashed unchanged afterwards. Core hash prefixes match the
  builder's `core-svg-hashes-before.txt` exactly
  (p1 e057bbfc…, p2 c87aa67e…, p3 d50f09e1…, p4 dd3b1b0f…, p5 c71ef315…,
  p6 b06a85d2…, p7 f2319cb8…, p8 eaf368f8…).
- `tools/freeze.py diff` core vs edition (my run): p1 +43/−45, p2 +58/−59,
  p3 +36/−36, p4 +40/−40, p5 +39/−40, p6 +38/−38, p7 +78/−83, p8 +190/−198;
  total added CJK 5408 — identical to the builder's KIT §6 figures.
- String-level decomposition (own script `decompose.py`, own run):
  every removed string is an English explanation string, a replaced
  furniture string (Chinese head kept in the edition's corresponding
  line), a wrapped-explanation line quoting Chinese terms, or one of the
  6 adjudicated items in Gate 2. Every added string is Japanese
  explanation (kana-bearing) or one of the 45 kana-less items in Gate 2.
- Chinese-run conservation (own script `conserve.py`, substring method):
  **0 missing unique core Han runs on all 8 pages** after removing the
  10 replaced furniture strings (footer ×8 pages + page-line form + badge
  line). Without furniture removal, the only misses on any page are the
  furniture runs themselves (`简体中文正文`, `英语讲解`, `简体中文周报`,
  and `共` from the page-line form). No Simplified target string was
  added or removed. (A first count-based attempt produced phantom
  "misses" — e.g. P4 `通宵`, P1 `双` — which I traced to joined-text
  line-boundary merge artefacts: e.g. edition `観戦の中国語通宵` merges
  the run across a line break. Raw substring counts for every suspect
  are equal core vs edition; the substring method is the correct one
  and it reports 0.)

## Gate 2 — Builder's flagged items, adjudicated one by one — PASS

### The 6 removed strings (exact match to the builder's list)

1. P1 `「立冬那天，我们吃饺子。」` — reflow, not loss. Delivered P1
   carries it across two lines (`立冬到了，冬天要来了。例文：「立冬那天，` /
   `我们吃饺子。」`), visible on the P1 card; joined sentence intact.
2. P7 `件.` — tail fragment of the English error-clinic sentence
   ("sweaters take 件."). The clinic's Chinese content is conserved in
   the Japanese clinic note (`一件毛衣`, `一条围巾`, `一部电影` all
   present on delivered P7).
3.–6. Four P8 MODELO reflow lines (`子，吃了…现` / `货第二天…冬天` /
   `赛，早上…直` / `降以后…不着`) — joined model-answer text is
   **identical raw, 172 chars**, core vs edition (own extraction from
   the delivered P8 SVGs: core 7 lines → edition 6 lines, only line-break
   positions differ; the head line `Model answer:` → `モデル解答：`
   accounts for the re-break). The two further removed model lines
   (`Model answer: …包饺` head, `凉。` closer) are explained by the head
   replacement and the same reflow, and are covered by the joined-text
   identity above.

### The kana-less added strings — 45, each proven (not batch-approved)

My independent count is **45, not the builder's 44**. Set-diff against
the builder's `attribute-out.txt` list: the builder's 44 are all present
in mine, and the single extra is exactly the fix-3 line
`94. 179 — 199 − 20 = 179元。` — the builder's list predates fix 3 and
was never refreshed (KIT §7's "44" is stale by exactly that line; the
line itself is correct — 元 unit matching all sibling basket notes and
the P6 chart labels). The 45 break down as:

- Wrapped gloss-line fragments (e.g. `解説 — xiànhuò 现货 —`,
  `解説 — cāngkù 仓库 — 倉庫 · píngjià 评价`,
  `· qīzhōng 期中 — 中間試験。`, `guǎnggào 广告 — 広告。`) — tails/heads
  of kana-bearing Japanese gloss lines, split by wrapping.
- Wrapped note fragments (`来週開始`, `援）。`, `本）。`, `最後。`,
  `气，再出门。」`, P7 time-example fragments) — tails of kana-bearing
  Japanese sentences.
- Bilingual furniture heads, Chinese head kept + kanji-only Japanese
  half: `本期目录 · 目次`, `练习 · 練習問題` (×5 pages),
  `文化 · 文化特集`, `青年 · 若者`, `S16 赛程 · S16日程（北京時間）`,
  `下期预告 · 来週（VOL.3）`, P8 writing label `作文`.
- Kanji-only Japanese glosses in P8 notes: `決勝`, `興行収入`, `主張`,
  `決済画面`, `配送料`, date notes `立冬、11月7日。` (items 34/103),
  `約119.2万元` (article's 万元 unit).
- Reflowed frozen example lines (`立冬到了，冬天要来了。例文：「立冬那天，` /
  `我们吃饺子。」`) and the date line `11月2日—8日 · 11月2～8日`.
- MODELO reflow lines (5 delivered lines, joined text identical per above).
- Fix-3 line `94. 179 — 199 − 20 = 179元。` (see above).
- MODELO text identical raw, **172 chars** (verified above).

No added string is a new Simplified target sentence; no added string is
an English explanation string.

## Gate 3 — Japanese orphan scan — PASS

Own scan over ALL `<text>` lines of all 8 delivered SVGs (own script
`orphan.py`, stricter than a prose-only scan since it covers heads,
notes and glosses too):

- Line-start closers (core NO_START set + small-kana extension): **0**
- Line-end openers (NO_END set): **0**
- Line-start small kana (the fixed class, incl. `って`): **0**
- Core SVGs contain **0 kana characters**, so the NO_START extension
  cannot trigger on any frozen Chinese line (verified by count, not by
  assertion).
- svglib diff core vs build copy: the ONLY change is the 5 added lines
  (comment + `NO_START += "ぁぃぅぇぉゃゅょゎっァィゥェォャュョヮッ"`).
  Mechanism (oidashi pull-down, guard ≤8, line count unchanged) is
  byte-identical otherwise. The extension is sound: small kana are
  phonetically incapable of starting a Japanese line, and no Chinese
  text contains them.
- The fixed P7 disclosure lines read `…掲載します。延期で` /
  `あって中止ではありません。中国語の手紙を` on the delivered P7 card —
  no small-kana start, no orphan.

## Gate 4 — Builder's three self-fixes, re-verified on the final render — PASS

(a) P7 disclosure shortening: delivered P7 teaser box rect is
    `x=65 y=2436.1 width=1820 height=118` → bottom **2554.1**, exactly
    the core's value; build-dir reproduction log (Gate 10, Test A)
    prints `P7 col3 ends 1708.1` / `P7 teaser ends 2554.1` — exactly the
    core's values. Footer line is 2580; the teaser clears it.
(b) Small-kana NO_START fix: see Gate 3 (0 orphans, sound extension).
(c) Basket-B note unit: delivered P8 SVG line is
    `94. 179 — 199 − 20 = 179元。` (visible on the P8 card in the keys
    area); `yuan` occurs **0 times** in all 8 delivered SVGs; English
    -explanation markers (` means `, `Fill in`, `Choose the`,
    `Write two`, `discount`, `example`, ` yuan`, `sweater`, ` dumpling`)
    all occur 0 times. Residual-Latin classes spot-checked against the
    builder's 441-line list: frozen Chinese Latin tokens (VOL/S16/AI/
    JD.com/Maoyan/team codes, level badges A2/B1/B2, option letters,
    `(p. N)` tags as in W43 ja), pinyin in frozen gloss format, `Lucerna`,
    English `Photo:` credits (precedent, Gate 9), JA furniture with
    VOL.2, proper-name citations (Sina Sports, Worlds S16). No other
    English residue found.

## Gate 5 — Gate 10, REPRODUCTION — NOT PASS (the single blocking item)

See §Blocking. Summary: build-dir reproduction 8/8 ✓; standalone
transform reproduction 6/8 ✗ (P7 + P8 differ, for exactly the three
self-fixes, which live only in the build copy).

## Gate 6 — p8.py compare, gloss, registry — PASS

- `tools/p8.py compare` core vs edition (target zh-cn):
  **CLEAN, 150 noted = 150 noted, missing=[], extra_count=0,
  uncertain=[], keydiff=[]** (own run).
- Gloss counts (own extraction from core-build vs ja-build sources,
  split on `·` per tools README #21): **10 calls, counts
  [4,4,4,3,3,3,3,3,3,3], total 33, item-by-item equal** to the core.
- Registry (build-dir reproduction log, Test A): TOTAL 150,
  levels A2 56 / B1 69 / B2 25, pages 10/18/18/18/18/18/12/38 — identical
  to the core; exercise numbering 1–150 with no gaps (p8 CLEAN + registry
  + per-page counts agree).

## Gate 7 — Occlusion audit + chart element check — PASS

- `tools/occlusion_audit.py`: selftest OK (all 6 planted classes fire,
  clean controls silent); edition **0 flags**; core **0 flags**;
  **NEW vs core: 0** (own run, exit 0).
- Own same-baseline ink-collision scan (`rowcheck.py`, PIL/FreeType true
  ink at 4×, SC face, gap criterion <6 incl. overlaps, all 8 pages
  incl. P1 top band): **collisions: 0**.
- P6 chart-label element check: bars identical to core —
  (325, 1282, 810×34), (325, 1340, 537×34), (325, 1398, 480×34);
  row labels at x=65 (`A: 毛衣+围巾`, `B: 耳机`, `C: 书+本子`), i.e.
  entirely left of bar start 325; value labels at bar end +16
  (x=1151 / 878 / 821 for `270 元` / `179 元` / `160 元`). No label/bar/
  text overlap; confirmed on the P6 card.

## Gate 8 — P7 golden sentences — PASS

All 8 phrases verbatim from this issue's own articles, exactly 2
occurrences each (article page + P7 bank), correct page tags:

| Phrase | Tag | Found on pages |
|---|---|---|
| 不用等11月11日 | p.1 | 1, 7 |
| 下单就能发货 | p.2 | 2, 7 |
| 先看结算页，再付款 | p.2 | 2, 7 |
| 水开始结冰 | p.3 | 3, 7 |
| 三场都输了 | p.4 | 4, 7 |
| 小局一场没赢 | p.4 | 4, 7 |
| 故事够不够好 | p.5 | 5, 7 |
| 别以后，就现在 | p.5 | 5, 7 |

P7 head states the provenance in Japanese
(`今週のフレーズ（今号の記事からそのまま抜粋）`).

## Gate 9 — Images + credits — PASS

- Embedded payloads: all 6 byte-identical to the core, per page
  (SHA-prefix + length match): P1 locker, P2 valley, P3 frost + dumplings,
  P4 lanparty, P5 popcorn; P6/P7/P8 carry no photo, as designed.
  Counts 1/1/2/1/1/0/0/0 match the core and KIT §4.
- Credit lines in the delivered SVGs are byte-identical to the core's:
  `Photo: Map hobby — CC0`, `Photo: Paul Gilmore — CC0`,
  `Photo: Gerda Arendt — CC0`, `Photo: Syced — CC0` (×2),
  `Photo: Based5290 — Public domain`, all `(Wikimedia Commons)`.
  They match the core `assets/CREDITS.md` Artist column, which records
  verification via the Commons API (`extmetadata` Artist +
  LicenseShortName) on 2026-10-27.
- English credits are precedent-consistent, NOT a defect: the shipped
  W43 zh-cn-ja SVGs also carry credits in English (`Photo: …` form).
  The builder's choice (keep English, unlike the nl build's `Foto:`)
  matches the same-pairing precedent.
- Limitation (honest): I did not re-query the Commons API myself — no
  live-browser/API route for that check is available to this subagent,
  and the edition-level gate (conservation + precedent) is fully covered
  without it. The underlying Artist-field claim rests on the core's
  2026-10-27 verification record.

## Gate 10 — Readers' corner — PASS

- On-page disclosure (delivered P7, joined text verified verbatim):
  `編集部注：VOL.1で予告した本物の手紙と最優秀作文はまだ届いていません。今号も編集部の例文を掲載します。延期であって中止ではありません。中国語の手紙をぜひお寄せください！`
  This discloses that no genuine letters exist (VOL.1 promise, none
  arrived, still the editor's example) and that it is a deferral, not a
  cancellation — and it is paired with the frozen Chinese letter above
  it, labelled editor's example (`编辑部示例信,不是真实来信`).
- Explicit open invitation, verbatim on the P7 card (wrapping across two
  rendered lines `…中国語の手紙を` / `ぜひお寄せください！`, continuous
  in reading): `中国語の手紙をぜひお寄せください！` ✓
  (A teaser line or another page's exercise prompt was not counted.)

## Gate 11 — Furniture three-way (core EN · W43 ja · this edition) — PASS

Measured from the shipped SVGs (x/y/size/fill), not from memory:

- **Badge slot — builder's claim CONFIRMED.** Core: (975, 434), 19.5pt,
  OLIVE #3e4c2a, long EN form. W43 ja: (975, 434), 19.5pt, BRICK #a4553a,
  `中国語（簡体字）テキスト · 日本語の解説 — 日本語読者のための版`.
  This edition: **identical to W43 ja in coords, size, colour and text,
  verbatim**. y=372 is the frozen bilingual strapline in ALL THREE
  (`给学中文的人的周报 — …`, y=372 unchanged) — not a free slot. This is
  the zh-cn core family's own in-place slot, neither the EN/DE/ES
  subtitle-slot case (y≈372) nor the FR/IT inserted-badge case (y=574,
  22pt). Shipped W43 wins over tables.json; tables.json was not edited.
- P8 separators: core `— Page N —` → W43 ja `— N ページ —` → this
  edition identical to W43 ja (all 8).
- Footer: core EN form → W43 ja
  `Lucerna · 中国語（簡体字）週刊 VOL.1 · 本文は中国語（簡体字） · 解説は日本語`
  → this edition the W43 pattern with VOL.2, verbatim otherwise.
- Page line: core `第 N 版 / 共 8 版` → W43 ja `N ページ（全 8 ページ）`
  → this edition identical to W43 ja.
- Gloss prefix `解説 —` (W43 ja form, vs core `Notes｜`) — present on
  all delivered gloss lines. P8 answer head
  `答案 · 全解答と解説（1–8ページ）`, P8 right note
  `解説はすべて日本語 · ✓ = 作文の課題`, dash answer style — all W43 ja
  forms, verified from the delivered P8 SVG.

## Gate 12 — Web regen — PASS

- Delivered cards are 1950×2700 RGB, ×8 (Pillow check).
- Cards regen from the delivered SVGs (same render code, proof scratch):
  **8/8 byte-identical** to the delivery cards (SHA match on all 8).
  This also proves the first-pass in-place re-render (see observation 3)
  did not change card bytes — the renderer is deterministic.
- Print PDF regen from the delivered SVGs: **byte-identical** to the
  delivered print PDF (SHA `239fc08d…1083f32c`, 41,688,105 B both).
- Web PDF regen: same length 3,118,383 B; only **8 differing bytes** in
  the whole file, all inside the `/CreationDate` and `/ModDate` strings
  (regen `D:20261028081752Z` vs delivered `D:20261028075456Z`).
  Every embedded stream is identical except the final 781-byte metadata
  stream, which differs only because it carries those two date strings.
  All 8 page-image JPEG streams match exactly. Web PDF is therefore
  **content-identical, timestamp bytes excepted — stated explicitly,
  as required**.

## Gate 13 — Eyeball all 8 cards — PASS

All 8 delivered cards read in full: layout clean, no overflow, no
overlap, no missing glyphs (Japanese kana/kanji render correctly
throughout). Masthead/badge (P1), P6 chart, P7 corner/teaser, P8 keys
top rule all clean. P4 shows the core's post-proof fix sentence in the
article (`TES一度落后，后来翻盘打赢了G2`); P5's mid-page white space
matches the frozen article flow (not a defect); P8's test-flow/keys
boundary is clean with the keys rule below the test flow.

## Gate 14 — Non-printing items + ABSTRACT — PASS

- P8 writing registry key `(开放题，范文如下)`: kept in Chinese in the
  build source, **0 occurrences in the delivered P8 SVG** — it never
  prints (writing items print as `N. ✓ note`, e.g. item 150). ✓
- `ABSTRACT.txt`: single line, **0 ASCII double quotes**, Japanese,
  names the paper (`Lucerna`), target language (`中国語（簡体字）`),
  levels (`A2からB2`), exercise count (`全150問`), real topic keywords
  (`双11の現物販売`, `立冬`, `S16スイスステージ`), and a learner search
  phrase (`中国語をニュースで学びたい人へ`). ✓
  Full text: `Lucerna中国語（簡体字）週刊VOL.2：双11の現物販売と立冬、S16スイスステージを中国語で読む、日本語解説付きのA2からB2まで全150問の中国語学習週報。中国語をニュースで学びたい人へ。`

## Gate 15 — Inherited core honesty limit — NOT a JA defect (recorded)

- The Start-of-Winter 17:52交节 source chain was not second-confirmed
  (core KIT honesty note, carried into this edition's KIT §3).
- JA-layer check: the Japanese notes that mention 17:52 are direct
  translations of the core's own notes at the same item numbers
  (P8 items 41 `節気の瞬間は17時52分。` ← core `The solar-term moment
  is 17:52.`; 107 time-order note ← core `Big → small order: Nov 7,
  Saturday, 17:52.`; 122 same as 41), and the P7 time-format example
  quotes the article's own time expression as teaching material. The JA
  layer does **not** independently assert the 17:52 time as a newly
  verified fact — it inherits/translates frozen core content. Recorded
  here as a **core-line item, not a JA blocking item**.

## §Blocking — the single blocking item

**Gate 10 (standalone reproduction) FAILS: 6/8, not 8/8.**

- What reproduces: the build dir's own one-process driver, repointed to
  a fresh copy (Test A): **8/8 byte-identical** to the delivered SVGs,
  0 FLOW OVERFLOW / 0 HEAD TOO WIDE warnings, P7 col3 1708.1 / teaser
  2554.1, registry identical. The delivered files are therefore
  reproducible from the build copy.
- What does NOT reproduce: the standalone transform record
  (`scratch/transform_ja.py` + `scratch/patch_ja_4.py`) run alone from a
  fresh copy of the core build via the one-process driver (Test B):
  transform applies cleanly (267 + 4 pairs, exit 0), the run succeeds
  with 0 warnings and an identical registry, but only **6/8 SVGs match**
  the delivered files (P1–P5 + P6 match; **P7 and P8 differ**).
- Root cause, proven by string-diff: **none of the three self-fixes is
  inside the reproduction record — all three live only in the build
  copy.**
  1. Fix 1 (P7 disclosure shortening): the transform maps the English
     disclosure to the LONG Japanese version
     (`VOL.1では本号（VOL.2）に本物の読者の手紙と…引き続き募集します。…`),
     while the build copy's `content7.py:91` carries the SHORT version
     (`VOL.1で予告した本物の手紙と最優秀作文はまだ届いていません。…`).
     The transform output's P7 therefore has col3 ending **1795.1** and
     the teaser ending **2641.1 — into the footer band** (footer line
     2580), i.e. it reproduces the builder's known-defective first
     render, not the delivered file. The P7 string-diff is ONLY the
     disclosure block (8 transform lines vs 5 delivered lines).
  2. Fix 2 (small-kana NO_START extension): the transform's FILES list
     excludes `svglib.py` and its header states "svglib.py — core
     version kept for the first render". The fresh-core run therefore
     uses the core svglib with no extension. In THIS run it produces no
     visible difference (the long disclosure happens to wrap without a
     small-kana start, so no `って`-start line appears in the transform
     output either) — but it is load-bearing the moment fix 1 is folded
     in, because the short disclosure's wrap is exactly what produced
     the `って…` orphan. All three fixes must be folded together.
  3. Fix 3 (basket-B note unit): the transform contains NO pair for the
     core's `199 − 20 = 179 yuan.` (grep: 0 hits); the build copy's
     `content56.py:221` carries `199 − 20 = 179元。`. The P8
     string-diff is ONLY key 94 (`…179 yuan.` vs `…179元。`) — i.e.
     the transform output reintroduces the single genuine English
     residue the builder fixed. (P6 matches despite this because the
     note text prints only in the P8 keys, not on P6.)
- Why this blocks: Gate 10's standalone rule is explicit ("must yield
  8/8 byte-identical … with zero warnings"), and the transform output
  is not merely different — on P7 it is defective by the builder's own
  pre-fix diagnosis (teaser in the footer band), and on P8 it carries
  English residue. This is not silently waivable, and no waiver is
  invented here: the coordinator must rule, or the builder must repair
  the record (see remedy).
- Concrete remedy (mechanical, no editorial judgement needed):
  1. In `transform_ja.py`, replace the disclosure pair's Japanese target
     with the delivered short version (identical to build
     `content7.py:91`'s Japanese tail).
  2. In `transform_ja.py`, add the pair
     (`199 − 20 = 179 yuan.` → `199 − 20 = 179元。`).
  3. In the reproduction record, add the svglib NO_START small-kana
     extension step (same 5 lines as the build copy's svglib diff), so
     a fresh-core run applies it before rendering.
  4. Re-run the standalone reproduction from a fresh core copy via the
     one-process driver; it must yield 8/8 byte-identical to the
     delivered SVGs with 0 warnings, including P7 col3 1708.1 / teaser
     2554.1 and P8 key 94 `179元。`. Then this proofread's Gate 10 can
     be re-verified (a reproof of Gate 10 only; all other gates above
     are unaffected by these three record changes, but the reproof must
     confirm the delivered SVGs themselves are unchanged by the repair
     — i.e. the repair changes the RECORD, not the delivered files).
- Note on scope: the delivered edition itself passes every content,
  layout, furniture, image, and audit gate above. The blocker is purely
  the reproducibility of the record. If the coordinator rules that
  build-copy reproduction (8/8, proven) suffices for this edition, that
  ruling — not this report — is what would clear it; this report does
  not grant it.

## Non-blocking observations (do NOT affect the verdict)

1. KIT §7's "44 kana-less added strings" is stale by exactly one line
   (the fix-3 P8 key 94 line; true count on the delivered SVGs is 45).
   Content is correct; only the KIT number needs a one-line refresh.
2. A first count-based run-conservation attempt produced phantom misses
   from joined-text merge artefacts; the substring method (used for the
   verdict) reports 0. Future proofreads should use the substring method
   and treat count-based run diffs as suspect.
3. The proof's web-regen run initially wrote re-rendered cards into the
   delivery `cards/` dir (a regen-script path bug: the `out =`
   replacement was missed on the first pass). The re-render uses the
   same code and SVGs as the original build, and determinism was then
   proven by a second render into proof scratch matching the delivery
   cards 8/8 — so the in-place re-render did not change card bytes.
   Delivery SVGs and PDFs were never written by the proof (both PDF pins
   still match the coordinator's pins); delivery mtimes changed only on
   the 8 cards, by the re-render itself. This is disclosed here rather
   than hidden.
4. Commons API Artist-field verification was not re-performed by this
   proof (see Gate 9 limitation); the edition-level conservation +
   precedent checks pass.
5. The 17:52交节 source chain remains unsecond-confirmed at the core
   level (Gate 15); it is not a JA-layer defect.

## §Regen note — complete

- Cards regen (second render, proof scratch) vs delivery cards: 8/8 MATCH.
- Web PDF regen vs delivered: same size 3,118,383 B; 8 differing bytes,
  all in `/CreationDate` + `/ModDate` strings; all page-image streams
  identical. Content-identical, timestamp bytes excepted.
- Print PDF regen vs delivered: byte-identical (SHA match).

## Limitations

- No OpenCC relevance here (no script conversion in this edition; no
  new Simplified target text was added at all).
- No live-browser checks were available to this subagent; all web-facing
  claims (Commons credits) rest on the core's recorded verification, as
  stated in Gate 9.
- The P7 col3/teaser values for the delivered files are transferred from
  the byte-identical build-dir reproduction log plus the directly
  measured teaser rect bottom (2554.1) on the delivered P7 SVG.
