# INDEPENDENT PROOFREAD — W45 ZH-TW × KO (Traditional Chinese target · Korean reader)

## VERDICT: PASS with ZERO PROBLEMS

All 17 gates pass, including Gate 10 reproduction (8/8 byte-identical, exit 0)
and Traditional independence (outside = [], Hanzi added = 0). This report is
the finalization evidence for the coordinator to insert. Nothing here declares
the edition shipped, and no insert, Discord post, chat dump, cron, or
weekly-git action was taken by this proofreader.

- Delivery: `files/weekly-report-w45-zh-tw-ko/` — svg×8, cards×8 (1950×2700),
  print + web PDFs, WEEKLY-KIT.md, ABSTRACT.txt
- Build dir: `hidden_files/weekly-report-w45-zh-tw-ko-build/`
- Canonical transform: `hidden_files/weekly-report-w45-zh-tw-ko-transform.py`
  (280 pairs verified by AST: BSLIB 3 + C12 52 + C34 61 + C56 62 + C7 50 + C8 52)
- Core: `files/weekly-report-w45-zhtw-core/` (KIT read first)
- Proof work: this dir (`hidden_files/w45/zh-tw-ko-proof/`, `work/` scripts +
  outputs, `work/regen/` re-rendered cards/PDFs)

## PRE-FLIGHT (no concurrent writer) — PASS

- (a) No live worker/process writing to delivery/build dirs (ps check, twice).
- (b) Two mtime snapshots of BOTH dirs a few minutes apart (09:34 → 09:38 UTC)
  showed ZERO changes (snapA == snapB); delivery files also re-verified
  unchanged after all proof runs (only artifact: the directory-entry line
  itself, which has no trailing slash in the grep pattern — all 21 file
  entries identical).
- (c) Builder session completed: last builder write 09:33 UTC, KIT delivered
  as BUILT, gate10 log complete, no processes.
- PDF pins re-verified at start (see §15 below).

## GATE-BY-GATE EVIDENCE

### 1. Freeze baseline + Hanzi accounting — PASS
- `tools/freeze.py baseline` on the zh-tw core: **8/8 byte-identical**,
  core SHAs match the builder KIT exactly (p1 4672c972…, p2 889fb533…,
  p3 508703c2…, p4 e04b62ea…, p5 4dfce72d…, p6 06ba4c66…, p7 00ac7f57…,
  p8 e6e97d02…), shipped core SVGs unchanged by the run.
- `freeze.py diff --strict-cjk`: FAIL label is EXPECTED for a KO edition
  (Hangul falls in the CJK range by design); added CJK total 5442, matching
  the builder per-page exactly (343/325/355/316/360/352/1028/2363).
- Character-level Hanzi accounting (my own re-run, U+4E00–U+9FFF /
  U+3400–U+4DBF / U+F900–U+FAFF): **Hanzi ADDED = 0 on all 8 pages**.
  Hanzi REMOVED = furniture only, reconciled item by item: P1 −30
  (badge 10 繁體中文正文·英語講解 + footer 16 繁體中文週報·繁體中文正文·
  英語講解 + page line 4 第/版/共/版); P2–P8 −20 each (footer 16 + page
  line 4). Every removed char is inside the furniture alphabet
  {繁體中文正文英語講解週報第版共}; removed-not-in-furniture = {} on all pages.
- Zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the Gate 10 replay log.

### 2. Traditional independence — HARD GATE — PASS
- Re-extraction from the shipped SVGs: edition Hanzi set 766 chars,
  core 767, W43 zh-tw-ko 784; **edition set outside (W43 ∪ core) = []**
  (judged by outside=[], counts happen to match the builder too).
  Core-only char: 解 (appears in the core only inside furniture 英語講解) —
  no other gap; edition-only vs core: [].
- Simplified-only spot list over target text (builder list + expanded list
  incl. 汉说国龙发对东车门见长马鸟鱼气电为让认议论设访证评读课谚艳艺节艰难
  风时实万与写军农冲决况冻净凛凝爱亲亿仅仪义尔发会个这进远运选录识观现头
  买卖里劳疗怜邻龙): **0 hits on all 8 pages**.
- Transform audit: no OpenCC / conversion / s2t / t2s / mapping-table logic
  anywhere in the canonical transform (grep clean); every pair replaces an
  English explanation string with Korean, or furniture, or the documented
  P7 geometry fix. No conversion was used.

### 3. Target text zero difference — PASS (run level, not by eye)
- Strongest form: per page, the core's Hanzi-only character string with
  furniture Hanzi substrings removed (badge/footer/page line) is
  **exactly equal** to the edition's Hanzi-only string, all 8 pages
  (lengths 811/848/936/710/958/799/673/970). Target text is identical in
  character order, not just in counts. Node-skeleton diffs are solely
  English→Korean explanation swaps, furniture, and re-wrapping of the
  same characters.

### 4. Gate 10 reproduction — MANDATORY, BLOCKING — PASS
- My own run: `tools/venv/bin/python
  hidden_files/weekly-report-w45-zh-tw-ko-transform.py --gate10`
  (fresh core copy + transform ALONE + one-process driver):
  **8/8 byte-identical, warnings=0, exit 0**, registry TOTAL 150
  (A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38;
  types 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1).
  Log: `work/gate10-proof.log`.
- Repoint hygiene verified in the transform source: whole path-segment
  replacement plus whole-OUT-assignment regex repoint; no stray nested
  tree in or under the delivery/build dirs (find shows only svg/, cards/
  and the builder's own files); the gate10 replay dir lives under
  `hidden_files/` as intended. Delivery files unchanged by my replay.

### 5. p8.py — PASS
- Explicit-path form (exact invocation):
  `tools/venv/bin/python p8.py compare --core-p8
  ../files/weekly-report-w45-zhtw-core/svg/p8-test.svg --edition-p8
  ../files/weekly-report-w45-zh-tw-ko/svg/p8-test.svg --total 150`
  → **CLEAN: 150=150, missing=[], extra_count=0, keydiff=[]**.
  Dir form (`--core-dir … --edition-dir … --target zh-tw`) identical.
- Notediff 150/150 (core extract 150, edition extract 150). Writing item:
  key `(開放題,範文如下)` kept verbatim in both builds (never printed;
  renders as `150. ✓ …`), note translated to Korean; writing glossline
  `쓰기 — 정답은 하나만 있는 게 아니에요. 총 138자의 모범 답안이 이어져요.`,
  note `열린 문제 — 모범 답안은 위 F 섹션에 있어요 (138자)`, label
  `모범 답안: ` — all verified in the rendered P8 and the card.

### 6. P8 dash style + AI-variant trap — PASS
- Dash verified from the W43 zh-tw-ko column's OWN shipped build code
  (`hidden_files/weekly-report-zh-tw-ko-build/content8.py` line 118:
  `txt = f"{e_['n']}. {e_['key']} — {e_['note']}"`) AND its shipped SVG
  (`1. B — 장미는…`, `150. ✓ 열린 문제 — … (134자)`). This edition's
  shipped P8 uses the same dash forms (`1. B — 핀테크 위크는…`,
  `150. ✓ 열린 문제 — … (138자)`). No keys-code change needed; the
  family split (es/pt/it paren vs fr/de/nl/ru/ko/ja dash) holds for KO.
- AI forms, BOTH verified Korean in the final render:
  - P5/P6 form: core `AI helps read data, spot risks and answer clients.`
    → P8 key 88 `88. A — AI는 데이터를 읽고, 위험을 포착하고, 고객에게
    답하는 것을 도와요.` (the P6 exercise's key; the P6 article gloss
    likewise renders the AI+ explanation in Korean).
  - P8-key form: core `AI inside finance is 人工智慧＋.` → key 138
    `138. 人工智慧 — 금융 안의 AI는 人工智慧＋예요.` — verbatim-term
    route, adjudicated against THIS column: W43 zh-tw-ko has NO AI topic
    (searched all 8 W43 SVGs for 人工智慧 — zero hits), so there is no
    direct W43 P8-AI precedent; the verbatim route is correct here
    because 人工智慧 is already the frozen core key for that item, and
    Hanzi accounting stays clean (added = 0; the term appears in the
    key and its note citation on both sides). The zh-tw-it pinyin-only
    rule and zh-tw-pt pinyin rule were NOT imported.

### 7. ×KO orphan scan, window 10–45 — PASS (0 defects)
- My own segmented scan (`work/orphan_proof.py`: blocks by (x, size) +
  y-gap > 45 + P8 item boundaries; flags = single-syllable final line,
  bracket tail, line-head orphan punctuation, ≥3-syllable-tail splits,
  standalone single-syllable lines): **49 Hangul-bearing blocks,
  14 candidates, 0 defects.** Candidates adjudicated: p3 `열려요.`
  (complete predicate); p6 `행사 FAQ` (complete byline tail); p7 ×3
  complete Traditional list items (`吉祥物大遊行.`, `（立冬/進補）.`,
  `泡湯.`); p8 frozen Traditional writing-model last line (complete
  sentence, not a Korean orphan); p8 separators `— 제 N 면 —`
  (furniture labels); p8 `26일 = 151일.` (complete arithmetic result).
  No continuation-start-punct, no dangling paren, no single-syllable
  prose final line.
- Cross-check with the W43 column's own proofreader scan repointed by me
  (`work/orphan_w43col_proof.py`, fresh copy of
  `hidden_files/proof-zh-tw-ko/orphan.py`): **42 blocks, 7 candidates,
  0 defects** — exactly reproducing the builder's cross-check numbers
  and adjudications.
- Full final-line read: all 49 blocks' prev-tail → last-line boundaries
  inspected; every boundary is a clean word boundary (prev ends with a
  complete word, last starts with a complete word). No word-fragment
  split (no 자치|주예요 / 메트로폴|리타노 class). A complete standalone
  key item was not counted as an orphan.

### 8. Occlusion audit + letter-box direct measurement — PASS
- `tools/occlusion_audit.py --selftest` OK (all 6 planted classes fired,
  clean controls silent); edition **0 flags**, core **0 flags**,
  **NEW vs core 0** (`work/occlusion-proof.json`,
  `work/occlusion-core-proof.json`).
- Same-baseline ink scan (my own, PIL true ink, all pages): CORE 0,
  ED 0 overlaps.
- Core's 1 ink-collision flag adjudication VERIFIED as a measurement
  artifact, non-blocking: core P7 y=224 B1 head
  `B1 · 球賽與節氣 · Games & seasons` measures **423.25px true width**
  (builder: 423.16; difference is 4× rounding) — starts x=527, ends
  950.25, inside column 527–961, next head at x=989, so NO real overlap;
  measuring the raw XML-escaped string `Games &amp; seasons` gives
  **483.75px** (builder: 483.8), which would falsely overlap — exactly the
  artifact claimed. This edition's Korean B1 head
  `B1 · 球賽與節氣 · 경기와 절기` measures **337.50px** (< 434), no
  head-width fix needed.
- Chart-label element check: text ink vs later-drawn bar rects —
  P4 0 grazes, P6 0 grazes. Chart bars byte-identical to core:
  P4 brick 120.0 + 600.0 (= 1 and 5 runs × 120); P6 olive 600.0, 800.0,
  800.0, 800.0 (= 6, 8, 8, 8 hours × 100).
- Rect diffs core→edition are gloss-box heights ONLY: P4 x=527
  h 294.3→264.575, P4 x=989 h 145.675→115.95, P6 x=989 h 353.75→294.3
  (same x/y/w/fill/stroke) — text-driven boxes, not chart bars.
- LETTER-BOX DIRECT MEASUREMENT (audit blind spot, not accepted on audit
  0 alone): readers box rect x=1451 y=1184.86 w=434 h=551.5 → bottom
  1736.36 (the +26→+46 lh fix, same as zh-tw-es). Last line
  `여러분의 편지를 기다릴게요!` baseline 1723.23, 20pt, Noto Sans CJK TC:
  PIL true-ink bottom = **1725.23** → **10.43px clearance** to the inner
  border (1735.66), 11.83px to the outer border. On the delivered P7 card
  (1:1 scale): last text-ink row **1724**, box bottom border row **1736**
  → **12px clearance** (the row-1766 dark line in the same column is the
  full-width rule at y=1766.36, not text ink — verified against the SVG).
  The last line is FULLY INSIDE with clear space on both SVG and card.
- P7 teaser: last ink row **2533** on the card (< 2580 footer rule,
  margin 47px); flow-end 2534.36 in the build log is consistent.

### 9. Gloss/match counts — PASS (reconciled)
- `gloss()` calls by AST: core 12 = edition 12 (content12 4, content34 5,
  content56 3). `·`-split items: core 12 = edition 12 (same split).
- Rendered `해설 — ` ×14 = **12 gloss + 1 badge + 1 P8 key-head**,
  identified exactly: badge node
  `중국어 번체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판` (P1, the
  `해설 — ` substring) and P8 head `答案 · 모든 정답과 해설 — 페이지
  순서대로, 문제마다 짧은 해설과 함께`. Per-page rendered: P1 3 (= 2
  gloss + badge), P2 2, P3 3, P4 2, P5 2, P6 1, P7 0, P8 1 (= 0 gloss +
  key-head) → gloss-only 12. No unexplained extra.
- Match sets: single W43-column form `단어와 뜻 짝짓기` rendered ×4
  (P2, P3, P4, P5 — one per set), matching the core's 4 match sets;
  transform instr counts: C12 ×1, C34 ×2, C56 ×1.
- Fill-in: transform instr counts C12 ×12 + C34 ×12 + C56 ×14 + C7 ×6 +
  C8 ×10 = **54**; rendered `빈칸 채우기` per-page counts identical to
  the core's `Fill in` per-page counts (60 total rendered occurrences
  both sides — the 60 vs 54 difference is section-head occurrences,
  identical on both sides).
- Registry 150 (A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38;
  types 67/54/16/12/1) re-verified in the Gate 10 replay; writing model
  verbatim (Hanzi-order P8 check + card: 138 characters, band 120–180).

### 10. P7 golden sentences — PASS (sentence-by-sentence)
All 8 verbatim from this issue's own articles, exactly 2× each issue-wide
(core = 2, edition = 2 for all 8), tags in the ZH-TW core's `(p. N)` form,
distribution core = edition = (p. 1)×2, (p. 2)×1, (p. 3)×2, (p. 4)×1,
(p. 5)×1, (p. 6)×1, matched sentence-by-sentence (quote → its own
translation node's tag, not just the distribution):
- 用手機轉帳、掃碼付款、網上買保險，都是金融科技 → (p. 1)
- 123個國家及城市、1,600個攤位 → (p. 1)
- 需要才買，不要為了折扣買一堆用不到的東西 → (p. 2)
- 在高雄，鋼鐵也能變成舞台 → (p. 3)
- 福隆的夏天，在10月26日畫下句點 → (p. 3)
- 6比0完封兄弟，龍隊拋下紅色彩帶 → (p. 4)
- 250家店家一起討糖 → (p. 5)
- 旅展首日中午12點才開門 → (p. 6)
No zh-tw-ja-style tag-distribution discrepancy. Teaser Traditional text
identical to core.

### 11. Images — PASS (provenance NOT re-litigated)
- Per-page base64 payloads byte-identical to the ZH-TW core (SHA-256
  prefixes: P1 af71609d2dd50bca, P2 c43d2e269e7d1061, P4 1a7e7d6d5ffcede7,
  P5 7fe6f82082ed5dd9; P3/P6/P7/P8 no photos, as in the core).
- Credits verbatim from the Commons Artist field, as rendered: P1
  `Photo: Wilfredor — CC0 (Wikimedia Commons)`; P2 `Photo: CorraleH —
  CC0 (Wikimedia Commons)`; P4 `Photo: Bain News Service — Public domain
  (Wikimedia Commons)` (fully visible on the P4 card, wrapping to two
  lines); P5 `Photo: Benjamin Balazs — CC0 (Wikimedia Commons)`.
- Binding: the core KIT's P4 provenance adjudication (2026-10-27, CLOSED)
  is respected — placed bytes and credit line are unchanged, so
  provenance is NOT re-flagged.

### 12. Readers' corner — PASS
- Frozen Traditional letter (4 nodes, y=1273.86–1365.45) and frozen
  Traditional disclosure (5 nodes, y=1426.98–1549.10) are line-for-line
  identical to the core at identical positions.
- Korean disclosure replaces the English lcn at the same 5 y-positions
  (1609.63–1723.23), exact form: `편집부가 쓴 예시 편지예요 — 진짜 독자
  편지는 아니에요. VOL.1에서 약속한 진짜 독자 편지와 8면 최우수 작문은
  아직 도착하지 않아서, 이번 호에도 예시를 싣고 공개 모집을 계속해요.
  여러분의 편지를 기다릴게요!` — states no genuine letters exist +
  verbatim open invitation. Form matches the W43 zh-tw-ko precedent
  structure (Korean disclosure + invitation; W43's own text was a VOL.2
  forward promise, so its wording differs by design — the VOL.1-deferral
  wording here is the correct VOL.2 adaptation). Head:
  `讀者園地 · 독자 코너`.

### 13. Furniture three-way — PASS (size difference = column precedent)
Measured from shipped SVGs (size AND color AND text):
| item | zh-tw core (W45) | W43 zh-tw-ko | this edition |
|---|---|---|---|
| P1 badge | y=378, 21pt, OLIVE #3e4c2a | y=378, 19.5pt, BRICK #a4553a | y=378, 19.5pt, BRICK #a4553a |
| P1 badge text | 繁體中文正文 · 英語講解 — Traditional… | 중국어 번체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판 | identical to W43 KO |
| Footer | …VOL.2 · 繁體中文正文 · 英語講解… | …VOL.1 · 텍스트는 중국어 번체 · 해설은 한국어 | VOL.2-adapted Korean form: `Lucerna · 중국어 번체 주간지 VOL.2 · 텍스트는 중국어 번체 · 해설은 한국어` |
| Page line | 第 {n} 版 / 共 8 版 | 제 {n} 면 / 총 8 면 | same as W43 KO |
| Gloss prefix | Notes｜ | 해설 — | same as W43 KO |
| P8 separator | — Page {pg} — | — 제 {pg} 면 — | same as W43 KO (×8) |
- The 19.5pt vs 21pt difference: W43 KO itself measures 19.5pt BRICK, so
  the edition is correct and the size difference is column precedent,
  NOT a defect. Shipped W43 wins over the brief and over tables.json;
  tables.json was NOT edited by this proof.
- P8 heads verified full-form identical to W43 KO: left
  `答案 · 모든 정답과 해설 — 페이지 순서대로, 문제마다 짧은 해설과 함께`,
  right `모든 해설은 한국어 · ✓ = 쓰기 모범 답안`, band
  `測驗與答案 · 시험과 정답`, sub
  `第 8 版 · 本週大測驗 + 全部答案 · 이번 주 시험과 모든 정답`.

### 14. Residual Latin — rendered-output sweep — PASS
- Every bilingual head Korean on the card, including 算一算 · 계산해 봐요
  ×3 (P2, P3, P5 — P3 visually confirmed on the card).
- English-explanation blocklist (Fill in, Work it out, Did you get it,
  Over to you, Read the chart, Test & keys, True or false, Readers'
  corner, Phrases of the week, Next week, Error clinic, Sentence frame,
  Language focus, Word of the week, Quick quiz, Headline words, This
  week's facts, Champion deals, Model answer, Answer keys, All notes in
  English, Writing —, Open task): **zero matches** in rendered text.
- Stronger: ED-only Latin words vs core = **[]** — the edition introduces
  NO new Latin word at all. Remaining Latin is frozen proper names /
  credits / codes also present in the core: masthead Lucerna, VOL.2,
  level chips A2/B1/B2, option letters, page tags (p. N), StartmeupHK,
  `Fintech Nexus: Bridging the World, Building the Future`, ITF, SUPER
  STAGE, SOLID TIDES, MVP, CTBC, C.C., JUMP, Trick or Treat, TSNA, NT$,
  AI (topic term), FAQ, B3, photo credits in English verbatim.
- Display artifacts verified by byte, not by eye: 穿 (U+7A7F) present in
  the delivered SVGs (P5 and P7; P7 option confirmed), 고객 (U+ACE0
  U+AC1D) present in P8; U+FFFD count = 0 in all 8 SVGs. Tool-display
  replacement glyphs are NOT evidence of absence.

### 15. Web regen + PDF pins — PASS
- Cards re-rendered from the delivered SVGs (cairosvg, 1950×2700) in
  `work/regen/`: **8/8 byte-identical** to delivered cards.
- Print PDF re-rendered (cairosvg svg2pdf + pypdf): **byte-identical**,
  15,287,199 B, 8 pages.
- Web PDF re-rendered: same byte size (3,281,709 B), 8 pages, all 8 page
  JPEGs byte-equal; file bytes differ in **exactly 8 bytes, all inside
  CreationDate/ModDate timestamps** (regen 20261028094417Z vs delivered
  20261028092335Z) — content-identical, timestamp bytes excepted, as
  specified.
- Pins re-verified (sha256sum, this proof):
  - print `Lucerna-VOL2-KO.pdf`: 15,287,199 B,
    `bc5573a559188fb59e8676953df3b521504a071dbf6994e0470c26ce38bcc494`, 8 pages
  - web `Lucerna-VOL2-KO-web.pdf`: 3,281,709 B,
    `685b612f248f3372f882e32de0003baf10e7f0541e5abe515ad54a7b82799a68`, 8 pages
    (under 10 MB)

### 16. Eyeball all 8 cards — PASS
All 8 delivered cards (1950×2700) viewed: layout clean, no overflow, no
overlap, no footer collision, no missing content. Notes per page: P1 badge
vs frozen subtitle hierarchy at y=378/434 clean; P2 算一算 head Korean;
P3 gloss boxes inside borders; P4 chart bars clear of labels, baseball
photo + caption + credit fully visible; P5 pumpkin photo + credit clean;
P6 chart + glosses clean; P7 readers-box last line inside with space,
golden phrases + tags clean, teaser clear of footer; P8 keys dense but
clean, separators visible, writing model visible, footer clean.

### 17. ABSTRACT.txt — PASS
- Korean single line, no ASCII double quotes (verified by byte check),
  names the paper (`Lucerna 중국어 번체 주간지 VOL.2`), target language
  (중국어 번체), A2–B2, 150 exercises, a learner search phrase
  (중국어 번체 신문으로 공부하기), and real topic keywords: 홍콩 핀테크
  위크, 타이베이 국제 여행 박람회, 입동, 가오슝 강철 조각 축제, 푸룽 모래
  조각 축제 폐막, 타이완 시리즈, 톈무 핼러윈, 11.11 쇼핑 미리보기.
- Cross-checked against the zh-tw core's actual contents (core KIT
  per-page contents): every named topic is in the core; no invented
  topic. No blocking item.

## NON-BLOCKING OBSERVATIONS (not part of the verdict)

1. The builder's `checks2.py` trailing comment miscounts the P1 badge as
   9 Hanzi (footer 16 + page line 4 + badge 9 = 29 vs observed 30); the
   correct badge count is 10 (繁體中文正文 6 + 英語講解 4), giving exactly
   30. Comment-only; my independent accounting closes at 30.
2. Builder's freeze-diff per-page added-CJK totals and my PIL head-width
   measurements differ from the builder's by ≤0.1px (423.25 vs 423.16;
   337.50 vs 337.42) — 4× supersampling rounding only; all conclusions
   unchanged.
3. My orphan scan's block count (49) differs from the builder's segmented
   scan (38) and the W43-column scan (42) because block segmentation
   differs (notably P8 separator attachment); all three scans agree on
   the verdict: 0 defects.
4. The W43 zh-tw-ko Korean disclosure is a forward VOL.2 promise, not a
   deferral — the W45 deferral wording is new but correctly adapted
   (see gate 12); this is a precedent-form match, not a verbatim match.

## LIMITATIONS (stated honestly)

- Korean was checked by full reading of every rendered Korean string, not
  by a native speaker.
- Commons was NOT re-queried live for image credits: credits were verified
  verbatim against the core's shipped credit lines and byte-identical
  payloads (P4 provenance is binding-closed per the core KIT); a live
  Commons fetch previously returned HTTP 403 for this file and was not
  treated as evidence either way.
- The same-baseline ink scan assumes start-anchored text for overlap
  intervals; centered masthead/badge elements were additionally confirmed
  by the occlusion audit (0 flags) and by eye on the cards.
- This proof did not touch `~/workspace/weekly-git`, did not run
  `insert.py`, posted nothing to Discord or to main chat, created no cron
  jobs, and cleaned no shared scratch dirs. All proof work is under
  `hidden_files/w45/zh-tw-ko-proof/`; `/tmp` was used only for one
  transient mtime comparison (not a proof artifact).

## BLOCKING LIST

None. Verdict: **PASS with ZERO PROBLEMS** — ready for coordinator insert.
