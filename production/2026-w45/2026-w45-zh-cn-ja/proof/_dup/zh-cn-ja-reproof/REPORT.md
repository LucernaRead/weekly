# INDEPENDENT RE-PROOFREAD — W45 Simplified Chinese × Japanese (zh-cn × ja)

**Verdict: PASS — ZERO PROBLEMS across all gates, including Gate 10.**
**This report is the finalization evidence for the coordinator's insert step.**
This agent did NOT fix anything, did NOT run insert.py, did NOT touch
`~/workspace/weekly-git`, did NOT post to Discord or main chat, did NOT
create cron jobs, did NOT clean shared scratch dirs, and spawned NO
subagents. No content module was ever imported inside the core build dir
— all re-renders ran on fresh copies under this proof dir.

- Edition dir: `files/weekly-report-w45-zh-cn-ja/` — svg ×8, cards ×8
  (1950×2700 RGB PNG), `Lucerna-VOL2-JA.pdf`, `Lucerna-VOL2-JA-web.pdf`,
  `WEEKLY-KIT.md`, `ABSTRACT.txt`
- Build dir: `hidden_files/weekly-report-w45-zh-cn-ja-build/`
  (standalone record: `scratch/transform_ja.py` + `scratch/patch_ja_4.py`)
- Core: `files/weekly-report-w45-zhcn-core/` (150 exercises,
  A2 56 / B1 69 / B2 25); core build: `hidden_files/weekly-report-w45-zhcn-build/`
- W43 same-pairing reference: `files/weekly-report-zh-cn-ja/`
- Proof work (this report's evidence):
  `hidden_files/w45/zh-cn-ja-reproof/work/` (snapshots, delivery hashes
  start/close, `repro/` fresh-core standalone run + driver logs,
  freeze/p8/occlusion/conserve/orphan/rowcheck/adjudicate/gloss logs,
  `webregen/` scratch-only render, `REPORT.md` here)
- Prior round: first proof `hidden_files/w45/zh-cn-ja-proof/REPORT.md`
  (NOT PASS on Gate 10 only); fix log
  `hidden_files/weekly-report-w45-zh-cn-ja-build/scratch/fix-gate10-log.md`.
  This reproof re-verified EVERYTHING from scratch; nothing was copied
  from the first proof's verdicts — its scripts were re-run and its
  figures independently reproduced (see §Incident note on one script's
  hardcoded output path).

## Pre-flight duplicate check — PASS (proceed)

- (a) No live worker/process writing to the delivery/build dirs. One
  unrelated process was visible (`insert.py` for zh-cn×ru into
  `weekly-git`); it touches neither the ja delivery nor the ja build
  dir, and the snapshots below prove it wrote nothing there.
- (b) Two mtime snapshots of both dirs, minutes apart, ZERO changes
  (`snap1.txt` vs `snap2.txt` identical).
- (c) Fix session completed: fix log filed, delivery files dated
  Oct 28 07:52–07:54 (SVGs/PDFs) with cards at 08:12–08:13 (first-proof
  re-render mtimes, bytes proven unchanged), KIT refreshed to "45".

## PDF pins re-verified (coordinator pins match exactly, start AND close)

- Print `Lucerna-VOL2-JA.pdf`: 41,688,105 B,
  SHA-256 `239fc08d022d90481a80a7f7bfc1da23f31916e62f3838af0b64421b1083f32c`
- Web `Lucerna-VOL2-JA-web.pdf`: 3,118,383 B (<10 MB),
  SHA-256 `d783b566028a6c43e90b2b2dc95ae9d657791f4ceea4c5dffd89760764a7df5d`
- `ABSTRACT.txt` SHA-256 `36788ba952339bcbd20e73a14f31a9f1f2f4596c0c0217bc52285c9dfedfc851`
  (unchanged by the fix round, as claimed).
- `WEEKLY-KIT.md` SHA-256 `c652c12251eed70996cf3c2272b479c77ca0000f3c7e5bd5ca6f26fb63e227c5`
  (the fix log's post-refresh hash, i.e. the authorized "44"→"45" edit).
- Delivery bytes at close are byte-identical to delivery bytes at start
  (20/20: 8 SVGs, 8 cards, 2 PDFs, ABSTRACT.txt, WEEKLY-KIT.md).

## Gate 1 — Pre-flight + delivery hash verification — PASS

Start hashes recorded before any proof work; close hashes after all
proof work; diff empty. No byte changed during this round. Card bytes
(not mtimes) were the comparison basis throughout, per the caution
about the first proof's in-place card re-render.

## Gate 2 — Gate 10, DOCUMENTATION CHAIN (the fixed item) — PASS

Fresh core copy (`hidden_files/weekly-report-w45-zhcn-build/` → my
`work/repro/`), fixed standalone record (`transform_ja.py` +
`patch_ja_4.py`) alone, one-process driver (`run.py`), OUT repointed
to my repro scratch (never the delivery dir):

- Transform exit 0: **268 pairs** (267 + basket pair); patch exit 0
  (4 pairs); driver exit 0 (re-run captured explicitly: `DRIVER_EXIT=0`,
  `ALL DONE`).
- **8/8 SVGs byte-identical** to the delivered SVGs (two driver runs,
  both 8/8).
- Zero warnings: `FLOW OVERFLOW` 0, `HEAD TOO WIDE` 0 in driver log.
- Registry: TOTAL 150, A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38 — identical to core.
- P7 col3 **1708.1** / teaser **2554.1** (rect y=2436.1, h=118).
- P8 key 94: `94. 179 — 199 − 20 = 179元。`
- Repro `svglib.py` byte-identical to the build copy's `svglib.py`.

Three record changes verified in the fixed record itself (not trusted
from the fix log):

1. Disclosure pair target is the SHORT version, extracted
   programmatically from build `content7.py:91`'s tail (after `取消。`)
   and confirmed character-for-character identical to the string in
   `transform_ja.py` and present verbatim in the delivered P7 joined
   text: `編集部注：VOL.1で予告した本物の手紙と最優秀作文はまだ届いていません。今号も編集部の例文を掲載します。延期であって中止ではありません。中国語の手紙をぜひお寄せください！`
   The LONG version (`VOL.1では本号…`) occurs 0× in the fixed record.
2. Basket pair present: `("199 − 20 = 179 yuan." → "199 − 20 = 179元。")`
   after the Basket-A pair; core occurrence exactly 1×
   (build `content56.py:221` carries the `元。` form).
3. svglib NO_START small-kana extension step present in `main()` (same
   5 lines as the build copy's svglib diff, anchor + comment + extension
   line) + header bullet updated to "NO_START small-kana extension
   applied by main() (fix 2)". `py_compile` OK on both record files.

Limitation (honest, not blocking): the pre-fix original transform was
overwritten by the fix agent, so a literal diff of "fixed vs original
record" cannot be re-derived from a preserved original. What was
verified instead: the fixed record contains exactly the three claimed
changes plus the header bullet (pair count 268 = 267+1, LONG absent,
no other pair-count anomaly), `apply_fixes.py` performs only those
edits, and the fixed record reproduces 8/8. The 8/8 reproduction is
the substantive proof that no fourth record item is missing.

## Gate 3 — Freeze baseline + diff decomposition — PASS

- `tools/freeze.py baseline` on the core build: **8/8 byte-identical**,
  core SVGs re-hashed unchanged afterwards. Core hash prefixes match
  the first proof's record exactly (p1 e057bbfc…, p2 c87aa67e…,
  p3 d50f09e1…, p4 dd3b1b0f…, p5 c71ef315…, p6 b06a85d2…,
  p7 f2319cb8…, p8 eaf368f8…).
- `tools/freeze.py diff` core vs edition (own run): p1 +43/−45,
  p2 +58/−59, p3 +36/−36, p4 +40/−40, p5 +39/−40, p6 +38/−38,
  p7 +78/−83, p8 +190/−198; total added CJK 5408 — identical to the
  KIT §6 figures. (Strict-CJK does NOT apply to the Japanese
  explanation layer per the task; the added CJK is Japanese kana/kanji
  in the explanation layer, adjudicated at string level below.)
- String-level decomposition (own run, `decompose.py` + `adjudicate.log`):
  every removed Han-bearing string is either a replaced furniture
  string (Chinese head kept in the edition's corresponding line), a
  wrapped English-explanation line quoting Chinese terms, or one of
  the 6 adjudicated items in Gate 4. Proof: for every removed
  Han-bearing string, all its Han runs occur in the edition joined
  text — EXCEPT the furniture runs `简体中文周报` / `简体中文正文` /
  `英语讲解` / `共` (page-line form), which are the replaced furniture
  itself. No Simplified target string was added or removed.
- Chinese-run conservation (substring method, own run): **0 missing
  unique core Han runs on all 8 pages** after removing the 10 replaced
  furniture strings. (Count-based run diffs were NOT used for the
  verdict — they produce the known joined-text merge artefacts.)

## Gate 4 — Adjudication: 6 removed + 45 kana-less added — PASS

### The 6 removed strings (each verified in the delivered diff)

1. P1 `「立冬那天，我们吃饺子。」` — reflow, not loss. Delivered P1
   carries it across two lines (`立冬到了，冬天要来了。例文：「立冬那天，` /
   `我们吃饺子。」`); joined sentence intact (also confirmed on the
   P1 card).
2. P7 `件.` — tail fragment of the English error-clinic sentence
   ("sweaters take 件."). The clinic's Chinese content is conserved in
   the Japanese clinic note (`一件毛衣`, `一条围巾`, `一部电影` all
   present on delivered P7).
3.–6. Four P8 MODELO reflow lines (`子，吃了…现` / `货第二天…冬天` /
   `赛，早上…直` / `降以后…不着`) — joined model-answer text is
   **identical raw, 172 chars**, core vs edition (own extraction:
   core 7 lines → edition 6 lines, only line-break positions differ;
   head `Model answer:` → `モデル解答：` accounts for the re-break).
   The two further removed model lines (`Model answer: …包饺` head,
   `凉。` closer) are explained by the head replacement and the same
   reflow, covered by the joined-text identity.

### The kana-less added strings — 45, each proven (not batch-approved)

Own independent set count is **45**; set-diff vs the builder's old
`attribute-out.txt` list: the builder's 44 are all present, and the
single extra is exactly the fix-3 line
`94. 179 — 199 − 20 = 179元。`. KIT §7 now reads "45" (line 265),
matching this count. The 45 break down as:

- Bilingual furniture heads, Chinese head kept + kanji-only Japanese
  half (12 incl. per-page repeats): `本期目录 · 目次`,
  `练习 · 練習問題` (×5 pages), `文化 · 文化特集`,
  `S16 赛程 · S16日程（北京時間）`, `青年 · 若者`,
  `下期预告 · 来週（VOL.3）`, P8 writing label `作文`,
  date line `11月2日—8日 · 11月2～8日`.
- Wrapped gloss-line fragments, tails/heads of kana-bearing Japanese
  gloss lines: `解説 — xiànhuò 现货 —`,
  `解説 — cāngkù 仓库 — 倉庫 · píngjià 评价`,
  `解説 — bǔdōng 补冬 —`, `解説 — shùzì xíngxiàng 数字形象 —`,
  `解説 — huǒhuà 火化 — 火葬 · jiùshú 救赎`,
  `· qīzhōng 期中 — 中間試験。`, `guǎnggào 广告 — 広告。`,
  `一般公開 · piàofáng 票房 — 興行収入。`.
- Wrapped note fragments, tails of kana-bearing Japanese sentences:
  `来週開始`, `援）。`, `本）。`, `最後。`, `气，再出门。」`,
  P7 time-example fragments (`例：「11月7日星期六17点52分」（11月7日`,
  `（土）17時52分）、「11月10日星期二20点」`,
  `（11月10日（火）20時）、「11月15日凌晨3`).
- Kanji-only Japanese glosses in P8 notes: `100. a — 运费 = 配送料、a`,
  `34. / 103. 立冬 — lìdōng — 立冬、11月7日。`,
  `64. a — 总决赛 = 決勝、a`, `71. 票房 — piàofáng — 興行収入、約119.2万元。`,
  `80. a — 票房 = 興行収入、a`, `97. c — 说法 = 主張、c`,
  `99. b — 结算页 = 決済画面、b`, `136. 票房 — piàofáng — 興行収入。`.
- Reflowed frozen lines (present in core joined text):
  `我们吃饺子。」`, `立冬到了，冬天要来了。例文：「立冬那天，`,
  and the 5 MODELO reflow lines (joined text identical per above).
- Fix-3 line: `94. 179 — 199 − 20 = 179元。` (元 unit matching all
  sibling basket notes and the P6 chart labels).

No added string is a new Simplified target sentence; no added string
is an English explanation string.

## Gate 5 — Japanese orphan scan — PASS

Own scan over ALL `<text>` lines of all 8 delivered SVGs (own run,
stricter than prose-only since it covers heads, notes and glosses):

- Line-start closers (core NO_START set + small-kana extension): **0**
- Line-end openers (NO_END set): **0**
- Line-start small kana (the fixed class, incl. `って`): **0**
- Core SVGs contain **0 kana characters**, so the NO_START extension
  cannot trigger on any frozen Chinese line (verified by count).
- The extension holds WITH the short disclosure (the load-bearing
  case): delivered P7 disclosure lines read
  `…掲載します。延期で` / `あって中止ではありません。中国語の手紙を`
  / `ぜひお寄せください！` — no small-kana start, no orphan.
  The fixed-record reproduction (Gate 2) produces this wrap
  byte-identically, proving the extension step in the record is the
  operative one.

## Gate 6 — p8.py CLEAN + gloss counts — PASS

- `tools/p8.py compare` core vs edition (target zh-cn, own run):
  **CLEAN, 150 noted = 150 noted, missing=[], extra_count=0,
  uncertain=[], keydiff=[]**.
- Gloss counts (own extraction from core-build vs ja-build sources,
  split on `·` per tools README #21): **10 calls, counts
  [4,4,4,3,3,3,3,3,3,3], total 33, item-by-item equal** to the core.

## Gate 7 — Occlusion audit + chart element check — PASS

- `tools/occlusion_audit.py`: selftest OK (all 6 planted classes fire,
  clean controls silent); edition **0 flags**; core **0 flags**;
  **NEW vs core: 0** (own run, exit 0).
- Own same-baseline ink-collision scan (`rowcheck.py`, PIL/FreeType
  true ink at 4×, SC face, gap criterion <6 incl. overlaps, all 8
  pages incl. P1 top band): **collisions: 0**.
- P6 chart-label element check: bars identical to core —
  (325, 1282, 810×34), (325, 1340, 537×34), (325, 1398, 480×34);
  row labels at x=65 (`A: 毛衣+围巾`, `B: 耳机`, `C: 书+本子`),
  entirely left of bar start 325; value labels at bar end +16
  (x=1151 / 878 / 821 for `270 元` / `179 元` / `160 元`).
  No label/bar/text overlap; confirmed on the P6 card.

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
  (SHA-prefix + length match): P1 locker, P2 valley, P3 frost +
  dumplings, P4 lanparty, P5 popcorn; P6/P7/P8 carry no photo, as
  designed. Counts 1/1/2/1/1/0/0/0 match the core and KIT §4.
- Credit lines in the delivered SVGs are byte-identical to the core's:
  `Photo: Map hobby — CC0`, `Photo: Paul Gilmore — CC0`,
  `Photo: Gerda Arendt — CC0`, `Photo: Syced — CC0` (×2),
  `Photo: Based5290 — Public domain`, all `(Wikimedia Commons)`.
  They match the core `assets/CREDITS.md` Artist column, which records
  verification via the Commons API (`extmetadata` Artist +
  LicenseShortName) on 2026-10-27.
- English credits are precedent-consistent, NOT a defect: the shipped
  W43 zh-cn-ja SVGs also carry credits in English (`Photo: …` form).
- Limitation (honest): the Commons API was not re-queried by this
  proof (no live-browser/API route for that check is available to this
  subagent); the edition-level gate (payload conservation + Artist
  column match + precedent) is fully covered without it.

## Gate 10 — Readers' corner — PASS

- On-page disclosure (delivered P7, joined text verified verbatim):
  `編集部注：VOL.1で予告した本物の手紙と最優秀作文はまだ届いていません。今号も編集部の例文を掲載します。延期であって中止ではありません。中国語の手紙をぜひお寄せください！`
  This discloses that no genuine letters exist (VOL.1 promise, none
  arrived, still the editor's example) and that it is a deferral, not a
  cancellation — paired with the frozen Chinese letter above it,
  labelled editor's example (`编辑部示例信,不是真实来信`).
- Explicit open invitation, verbatim on the P7 card (wrapping across
  rendered lines `…中国語の手紙を` / `ぜひお寄せください！`,
  continuous in reading): `中国語の手紙をぜひお寄せください！`
- P7 teaser rect `x=65 y=2436.1 width=1820 height=118` → bottom
  **2554.1**, exactly the core's value; footer line 2580 clear.

## Gate 11 — Furniture three-way (core EN · W43 ja · this edition) — PASS

Measured from the shipped SVGs (x/y/size/fill), not from memory:

- **Badge slot — CONFIRMED.** Core: (975, 434), 19.5pt, OLIVE #3e4c2a,
  long EN form. W43 ja: (975, 434), 19.5pt, BRICK #a4553a,
  `中国語（簡体字）テキスト · 日本語の解説 — 日本語読者のための版`.
  This edition: **identical to W43 ja in coords, size, colour and text,
  verbatim**. y=372 is the frozen bilingual strapline in ALL THREE
  (`给学中文的人的周报 — …`, y=372 unchanged) — not a free slot.
  This is the zh-cn core family's own in-place slot, neither the
  EN/DE/ES subtitle-slot case (y≈372) nor the FR/IT inserted-badge case
  (y=574, 22pt). Shipped W43 wins over tables.json; tables.json was not
  edited.
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

Regen output written ONLY to this proof's scratch (`work/webregen/`),
never into the delivery `cards/` dir (the first proof's path bug did
not recur; the repointed render script's BASE was verified to point at
the scratch dir before running):

- Delivered cards are 1950×2700 RGB, ×8.
- Cards regen from the delivered SVGs (same render code, proof scratch):
  **8/8 byte-identical** to the delivery cards (SHA match on all 8).
- Print PDF regen from the delivered SVGs: **byte-identical** to the
  delivered print PDF (SHA `239fc08d…1083f32c`, 41,688,105 B both).
- Web PDF regen: same length 3,118,383 B; after normalizing only the
  two date fields, the files are **identical** — the only differing
  bytes are inside `/CreationDate` and `/ModDate`
  (regen `D:20261028085447Z` vs delivered `D:20261028075456Z`).
  Web PDF is therefore **content-identical, timestamp bytes excepted
  — stated explicitly, as required**.
- Process note: the first regen exec was interrupted by the runtime
  after the 8 cards (sizes already matching delivery); the rerun
  completed all outputs. No delivery file was touched by either run.

## Gate 13 — Eyeball all 8 cards — PASS

All 8 delivered cards read in full: layout clean, no overflow, no
overlap, no missing glyphs (Japanese kana/kanji render correctly
throughout). Masthead/badge (P1), P6 chart, P7 corner/teaser, P8 keys
top rule all clean. P4 shows the core's post-proof fix sentence in the
article (`TES一度落后，后来翻盘打赢了G2`); P5's mid-page white space
matches the frozen article flow (not a defect); P8's test-flow/keys
boundary is clean with the keys rule below the test flow. P8 key 94
`179元。` visible in the keys area.

## Gate 14 — Non-printing items + ABSTRACT — PASS

- P8 writing registry key `(开放题，范文如下)`: kept in Chinese in the
  build source, **0 occurrences in the delivered P8 SVG** — it never
  prints (writing items print as `N. ✓ note`, e.g. item 150).
- `yuan` occurs **0 times** in all 8 delivered SVGs.
- `ABSTRACT.txt`: single line, **0 ASCII double quotes**, Japanese,
  names the paper (`Lucerna`), target language (`中国語（簡体字）`),
  levels (`A2からB2`), exercise count (`全150問`), real topic keywords
  (`双11の現物販売`, `立冬`, `S16スイスステージ`), and a learner search
  phrase (`中国語をニュースで学びたい人へ`).

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
- Minor note (not a defect): a bare `122.` line appears in both the
  core and the edition P8 SVGs (column-break artefact of the shared
  layout); it is identical in both and is not a JA-layer change.

## Non-blocking observations (do NOT affect the verdict)

1. None concerning the edition itself. The items below are process
   notes for the coordinator, not edition defects.
2. Commons API Artist-field verification was not re-performed by this
   proof (see Gate 9 limitation).
3. The 17:52交节 source chain remains unsecond-confirmed at the core
   level (Gate 15); it is not a JA-layer defect.

## §Incident note — proof-side path bug, disclosed (no edition impact)

The copied `decompose.py` from the first proof hardcoded its output
paths to the first proof's work dir, so this reproof's first decompose
run overwrote the first proof's derived `decompose-summary.json` /
`decompose-full.txt` with this round's outputs. The script was then
patched to write only to this reproof's dir and re-run; the outputs
now live at `work/decompose-summary.json` / `work/decompose-full.txt`.
Delivery files, build files, and the first proof's `REPORT.md` were
never touched, and the overwritten files were deterministic derivations
of unchanged inputs, so no evidence was lost — but the overwrite is
disclosed here rather than hidden, and future reproofs should patch
copied scripts' output paths before the first run.

## §Regen note — complete

- Cards regen (proof scratch) vs delivery cards: 8/8 MATCH.
- Web PDF regen vs delivered: same size 3,118,383 B; content-identical,
  timestamp bytes excepted (dates above).
- Print PDF regen vs delivered: byte-identical (SHA match).
- Delivery hashes at close = delivery hashes at start (20/20).

## Limitations

- No live-browser checks were available to this subagent; all
  web-facing claims (Commons credits) rest on the core's recorded
  verification, as stated in Gate 9.
- Record-diff-vs-original limitation: see Gate 2 (pre-fix original
  overwritten; 8/8 reproduction is the substantive proof).
- KIT §7's "45" was verified against the delivered SVGs and the fix
  log's post-refresh hash; no pre-fix KIT copy was available to diff
  line-by-line, so the "line 265 only" claim is taken from the fix log
  and corroborated by the hash match, not independently diffed.
