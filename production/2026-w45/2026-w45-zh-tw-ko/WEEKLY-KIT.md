# WEEKLY-KIT — 2026-W45 zh-tw × ko (BUILT, NOT finalized)

- **Slug:** `2026-w45-zh-tw-ko` · **Issue week:** Nov 2–8, 2026 · **VOL.2**
- **Pairing:** Traditional Chinese target text · Korean explanation layer
- **Status: BUILT (NOT finalized).** An independent proofread follows; the
  coordinator inserts only on ZERO PROBLEMS. Nothing here is shipped,
  inserted, or posted.
- **Delivery dir:** `files/weekly-report-w45-zh-tw-ko/` (svg×8, cards×8,
  print + web PDFs, this KIT, ABSTRACT.txt)
- **Build dir:** `hidden_files/weekly-report-w45-zh-tw-ko-build/`
- **Canonical transform (self-contained, outside the build dir):**
  `hidden_files/weekly-report-w45-zh-tw-ko-transform.py` (280 pairs; every
  `rep()` count assertion passed at apply time)
- **Authoring aids (NOT the deliverable):**
  `hidden_files/w45-zh-tw-ko-src/` (`ko_map.py`, `gen_transform.py`,
  `transform_header.py`, `transform_footer.py`, `es_pairs.json`)
- **Gate 10 replay dir:** `hidden_files/w45-zh-tw-ko-gate10/`

## 0. Pre-flight (NO CONCURRENT WRITER)

- Snapshot 1: 2026-10-28T09:15:44Z; snapshot 2: 2026-10-28T09:17:22Z
  (delivery dir empty, build dir holding only this builder's own files).
  Snap1→snap2 was ~98 s, shorter than a full few minutes — closed by
  snapshot 3 at delivery time plus a live process check (no process
  writing to the delivery/build dirs; no sibling works this pairing — a
  sibling zh-tw-ja builder ran concurrently on a DIFFERENT pairing only).
  All changes between snap2 and snap3 are this builder's own build
  outputs (render1, gate10, checks, KIT, ABSTRACT).
- Core SVGs re-hashed at delivery: all 8 identical to the pre-build
  hashes (see §1). No other writer touched the dirs.

## 1. Baseline — 8/8 byte-identical to the zh-tw core

`tools/freeze.py baseline` on the zh-tw core passed 8/8 before any edit.
Core SHA-256 (unchanged at delivery):

| page | SHA-256 |
|---|---|
| p1-front | `4672c972763b0eaf249bff952cd777d9941cc2a801928bfb1edd1e0e4558d047` |
| p2-life | `889fb533ef3ff62ecc820d3d92dc4aed10e353f5dcf9487c9d844fd2dad3cee3` |
| p3-culture | `508703c2b3c313c6853a17e452e2d55629e0933a94905211f5f53425619bab42` |
| p4-sport | `e04b62ea6211c9ffabeb90a1a94faa5b3bcea3503b19a7fbd6473546a88f86f1` |
| p5-youth | `4dfce72d88000fbc9d4f43f441a9f7525ec05165e812ab2df0b6a8bac6eea30f` |
| p6-deep | `06ba4c6627cb81655e02b8ad7656676e3b258e3b0763dfde7e5ec29e7174c838` |
| p7-lang | `00ac7f57125fcc094ce850712a5d302df891600062fa8cbc0c47bd7a5243192c` |
| p8-test | `e6e97d02595aef3bb1a3c60dd852d190e387f647a547527cc24153eeea0b41ed` |

## 2. Registry — exact zh-tw core split (NOT the zh-cn core's)

**TOTAL 150** · by level **A2 44 / B1 74 / B2 32** · by type
**單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1** · by page
**P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38**.
One-process driver run: zero FLOW OVERFLOW, zero HEAD TOO WIDE warnings
(log `build/render1.log`; Gate 10 replay reproduced the same registry).

## 3. Traditional independence — HARD GATE (passed)

- Target text comes ONLY from the frozen zh-tw core + W43 zh-tw-ko
  precedent furniture. No OpenCC, no conversion table, no conversion
  logic anywhere in the transform.
- CJK-set accounting: edition Hanzi set 766 chars; W43 zh-tw-ko set 784;
  core set 767; **edition set outside (W43 ∪ core) = []**.
  Simplified-only spot list over edition SVGs and build sources = **0 hits**.
- `freeze.py diff --strict-cjk`: strict-CJK FAIL is EXPECTED for a KO
  edition (Hangul falls in the CJK range by design; README #3 says
  adjudicate ko by the per-char list). Added CJK total 5442, all Hangul
  explanation layer (p1 343, p2 325, p3 355, p4 316, p5 360, p6 352,
  p7 1028, p8 2363).
- Character-level Hanzi accounting (Hanzi = U+4E00–U+9FFF, U+3400–U+4DBF,
  U+F900–U+FAFF): **Hanzi ADDED = 0 on all 8 pages.**
  Hanzi REMOVED = furniture vocabulary only — P1 −30, P2–P8 −20 each,
  chars only from {繁體中文正文英語講解週報第版共}.
  P1 −30 reconciled exactly: badge 10 (繁體中文正文·英語講解) + footer 16
  (繁體中文週報·繁體中文正文·英語講解) + page line 4 (第 1 版 / 共 8 版).
  P2–P8 −20 = footer 16 + page line 4. Furniture-corrected Hanzi delta
  = 0 on P1–P7 and on P8.
- Core-only Hanzi char: 解 (appears in the core ONLY inside the furniture
  strings 英語講解; no article uses it). Edition set has no other gap.
- Outputs: `build/freeze-diff1.json`, `build/checks1.py`, `build/checks2.py`.

## 4. Gate 10 self-run (transform-first discipline)

`python hidden_files/weekly-report-w45-zh-tw-ko-transform.py --gate10`
(fresh core copy under `hidden_files/w45-zh-tw-ko-gate10`, transform
ALONE + one-process driver):

- **GATE10: 8/8 byte-identical, warnings=0, exit 0** (log
  `build/gate10.log`). No hand-patched render was delivered.
- Repoint hygiene: whole path-segment replacement only (OUT assignment
  replaced wholesale by regex; no absolute temp dir spliced inside the
  `~/workspace/...` prefix). No stray nested tree under `files/` or the
  delivery dir after replay; the gate10 temp dir lives under
  `hidden_files/` as intended.

## 5. P8 — CLEAN (both invocations)

- `tools/p8.py compare --core-dir …/files/weekly-report-w45-zhtw-core
  --edition-dir …/files/weekly-report-w45-zh-tw-ko --target zh-tw`
- `tools/p8.py compare --core-p8 …/p8-test.svg --edition-p8 …/p8-test.svg
  --total 150` (explicit-path form; tables.json's default P8 filename
  matched this core's `p8-test.svg`, so no workaround was needed)
- Result both times: **CLEAN: 150=150, missing=[], extra_count=0,
  keydiff=[]**. Style is DASH per W43 zh-tw-ko's own shipped build code
  (`N. key — note`; writing: `N. ✓ note`), separator `— 제 {pg} 면 —`.
  No keys-code change and no `_fw` bypass were needed (unlike the
  es/pt paren families). Writing model verbatim, band-checked; writing
  glossline: `쓰기 — 정답은 하나만 있는 게 아니에요. 총 {NCHARS}자의 모범
  답안이 이어져요.`; writing note: `열린 문제 — 모범 답안은 위 F 섹션에
  있어요 ({NCHARS}자)`; model label `모범 답안: `.
  Writing key `(開放題,範文如下)` is deliberately KEPT verbatim per W43
  zh-tw-ko shipped code — it is never printed (writing keys render as
  `150. ✓ note`).

## 6. Occlusion + ink-collision + chart checks — 0 defects

- `tools/occlusion_audit.py --selftest` OK (all 6 planted classes fired,
  clean controls silent); edition **0 flags**, core 0 flags, **NEW vs
  core 0** (`build/occlusion1.json`, `build/occlusion-core.json`).
- Same-baseline ink-collision scan (`build/rowcheck.py`, PIL true-ink):
  edition **0 collisions**. Core shows 1 flag (P7 y=224, B1 head vs B2
  head) adjudicated as a MEASUREMENT ARTIFACT, not a defect: rowcheck
  measures the raw XML-escaped string `Games &amp; seasons` (extra
  `amp;` chars inflate width to ~483.8), while true `text_w` for
  `B1 · 球賽與節氣 · Games & seasons` is 423.16 < column 434, so no HEAD
  TOO WIDE and no real overlap. This edition's Korean B1 head
  `B1 · 球賽與節氣 · 경기와 절기` measures 337.42 — no head-width fix
  was needed (es had to shorten its Spanish head).
- Chart-label graze / element check: P4 brick bars identical (120.0 and
  600.0 px = 1 and 5 runs × 120); P6 olive bars identical (600.0, 800.0,
  800.0, 800.0 px = 6, 8, 8, 8 hours × 100). Full rect multisets differ
  ONLY in gloss-box heights (Korean glosses are shorter, e.g. P4
  x=527 y=357.0 height 294.3→264.575; P6 x=989 y=208 height
  353.75→294.3) — text-driven boxes, not chart bars.

## 7. ×KO orphan scan (README #16, window 10–45) — 0 defects

Scan: `build/orphan_scan2.py` over the delivered SVGs. Lines = rendered
`<text>` nodes containing Hangul (the Korean explanation layer; frozen
Traditional lines follow CJK wrap norms and are out of scope). Blocks
segmented by (x, font-size) + y-gap > 45 (the window's upper bound;
in-block pitches are 14–35) + P8 item boundaries (a line matching
`^\d+\. ` starts a new key-item block). Flags: (a) final-line
single-syllable, (b) final-line bracket-tail, (c) line-head orphan
punctuation from `[.!?…)\]»」』】％]`, (d) ≥3-syllable-tail split
candidates, (e) standalone single-syllable lines. A complete standalone
key item is NOT an orphan.

Result: **38 candidates, 0 defects.**

- S1 (single-syllable final line): **0**. HEADP (line-head orphan
  punctuation): **0**. BRACKET (dangling `)` tail): **0**.
- SHORT2 (≤2-syllable final lines): all furniture/labels, not prose
  orphans — P2/P3/P5/P7 band heads (`生活 · 생활`, `文化 · 문화`,
  `青年 · 청년`, `語言 · 언어`), P6 byline tail (`행사 FAQ`), P8 section
  head (`F · 寫一寫 · 쓰기`), P8 writing label (`쓰기`), P8 separators
  (`— 제 N 면 —`), and one complete arithmetic result line
  (`26일 = 151일.`, the tail of P8 key 41's note — a complete unit, not
  a word fragment).
- TAIL3? (24 candidates): every one inspected — in each case the final
  line is a COMPLETE word/phrase and the previous line ends with a
  complete word (e.g. `전시업체와` → `스타트업 800개 이상이 참여할
  예정이에요.`; `기술로 금융` → `서비스를 운영하는 것이에요.`;
  `속 예술에 관한 국제 포럼도` → `열려요.`; `가격을` → `비교하고,
  그다음 결제해요).`). No candidate shows a word fragment split across
  the boundary (no `자치|주예요`-class split). Note: this build's
  `svglib.wrap()` tokenizes Hangul syllables individually and wraps
  per-syllable with kinsoku NO_START/NO_END repair, so word-boundary
  wraps are structural in full-width columns; the proofreaders'
  criterion is the word-fragment tail, and none occurs.
- An earlier loose adjacency scan (grouping by (x, size) across whole
  columns, no block segmentation) was discarded as flawed — it never
  tested paragraph-final lines and its SPLIT≥3 heuristic over-flagged
  normal word-boundary wraps. The segmented scan above supersedes it.
- Cross-check with the W43 column's OWN proofreader scan
  (`hidden_files/proof-zh-tw-ko/orphan.py`, repointed at this edition
  as `build/orphan_w43col.py`; blocks by (x, size, kind, bold) split
  at dy > size×2.05, Hangul-bearing blocks only): **42 blocks, 7
  candidates, 0 defects.** Candidates and adjudications:
  - p3 final-3syll-short `열려요.` — complete predicate verb, not a
    word fragment. Non-defect.
  - p6 final<=2syll-tail `행사 FAQ` — complete byline tail unit
    (행사 + source type), not a fragment. Non-defect.
  - p7 final-line-no-hangul-after-korean ×3 — final lines are complete
    Traditional vocabulary items by design: `吉祥物大遊行.` (last item
    of the A2 word list), `（立冬/進補）.` (closing grouped item),
    `泡湯.` (last item of the regional-expression list). The Korean
    intro precedes each list; the list items themselves are Traditional
    words. Non-defects.
  - p8 final<=1syll — final line of the frozen Traditional writing
    model (`之前，我先列好購物清單，不亂買。`), a complete Traditional
    sentence identical to the core; the block was included only because
    its label line (`모범 답안: `) contains Hangul. Not a Korean
    orphan. Non-defect.
  - p8 final<=2syll-tail `26일 = 151일.` — complete arithmetic result
    tail of key 41's note (see above). Non-defect.
  - The W43-column scan also confirms: no continuation-start-punct and
    no block-start-punct candidates, and no final-dangling-paren
    candidates on this edition.

## 8. Furniture — three-way measurements (core · W43 zh-tw-ko · this edition)

Measured from shipped SVGs, not assumed. The KO column's own shipped P1
decides the badge: **BRICK** (zh-tw-ru's column precedent is OLIVE;
de/fr/es/pt/it are BRICK — the KO column is BRICK).

| item | zh-tw core (W45) | W43 zh-tw-ko | this edition |
|---|---|---|---|
| P1 badge slot | y=378, 21pt, OLIVE #3e4c2a | y=378, 19.5pt, BRICK #a4553a | y=378, 19.5pt, BRICK #a4553a |
| P1 badge text | `繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers` | `중국어 번체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판` | same as W43 KO |
| Footer | `Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations` | `Lucerna · 중국어 번체 주간지 VOL.1 · 텍스트는 중국어 번체 · 해설은 한국어` | `Lucerna · 중국어 번체 주간지 VOL.2 · 텍스트는 중국어 번체 · 해설은 한국어` |
| Page line | `第 {n} 版 / 共 {total} 版` | `제 {n} 면 / 총 {total} 면` | same as W43 KO |
| Gloss prefix | `Notes｜` | `해설 — ` | same as W43 KO |
| P8 separator | `— Page {pg} —` | `— 제 {pg} 면 —` | same as W43 KO |
| P8 style | dash | DASH | DASH (no change needed) |

P8 heads (W43 KO forms): left `答案 · 모든 정답과 해설 — 페이지
순서대로, 문제마다 짧은 해설과 함께`, right `모든 해설은 한국어 · ✓ =
쓰기 모범 답안`; band `測驗與答案 · 시험과 정답`, sub
`第 8 版 · 本週大測驗 + 全部答案 · 이번 주 시험과 모든 정답`;
sections A 判斷對錯 · 참 / 거짓, B 本週大測驗 · 이번 주 종합 퀴즈,
C 完成句子 · 빈칸 채우기, D 讀一讀，答一答 · 읽고 답하기,
E 情景說話 · 상황 말하기, F 寫一寫 · 쓰기.
Match instruction: single W43-column form `단어와 뜻 짝짓기` for all 4
match sets (W43 KO used it ×5). Fill in → `빈칸 채우기` (54 total:
C12×12 + C34×12 + C56×14 + C7×6 + C8×10). Writing → `쓰기`.

## 9. Explanation layer fully in Korean — rendered-output sweep

Sweep over ALL rendered text nodes (added-strings scan alone was proven
insufficient by zh-tw-es/pt missing `算一算 · Work it out`):

- Every bilingual head is Korean on the card, including **算一算 ·
  계산해 봐요 ×3 (P2, P3, P5)**.
- English-explanation blocklist = **zero matches**: Fill in, Work it
  out, Did you get it, Over to you, Read the chart, Test & keys, True
  or false, Readers' corner, Phrases of the week, Next week, Error
  clinic, Sentence frame, Language focus, Word of the week, Quick quiz,
  Headline words, This week's facts, Champion deals, Model answer,
  Answer keys, All notes in English, Writing —, Open task.
- Remaining Latin adjudicated as frozen proper names/credits/codes, NOT
  explanation prose: masthead `Lucerna`; VOL.2/VOL.1/VOL.3 volume refs;
  level chips A2/B1/B2; option letters A./B./C./a./b./c./d.; page tags
  `(p. N)` (W43 KO precedent keeps them); frozen Traditional-text proper
  names StartmeupHK, `Fintech Nexus: Bridging the World, Building the
  Future`, ITF, SUPER STAGE, SOLID TIDES, MVP, CTBC, C.C., JUMP,
  Trick or Treat, TSNA; currency code NT$; abbreviation AI (the topic
  term itself) and FAQ; warehouse code B3; photo credits in English
  verbatim from the Commons Artist field (W43 KO precedent: photo
  credits stay English).
- Rendered gloss prefix: core `Notes｜` ×12; edition `해설 — ` ×14 = 12
  gloss + badge 1 + P8 key-head 1 (same pattern as W43 KO's 13 = 11 + 1 + 1).
- Gloss/match counts item-identical to the zh-tw core: `gloss()` calls
  core 12 = edition 12 (content12: 4, content34: 5, content56: 3);
  gloss strings split on `·` (README #21): core 12 = edition 12.
- AI-variant trap (bit zh-cn-es, zh-cn-it, zh-tw-it, zh-tw-es,
  zh-tw-pt): the P8-key AI form is a SEPARATE string from the P5/P6
  form, and BOTH are translated. P5/P6 form `AI helps read data, spot
  risks and answer clients.` → `AI는 데이터를 읽고, 위험을 포착하고,
  고객에게 답하는 것을 도와요.`; P8-key form `AI inside finance is
  人工智慧＋.` → `금융 안의 AI는 人工智慧＋예요.` W43 zh-tw-ko had no AI
  topic, so no direct P8-AI precedent exists; the verbatim-term route
  is used because 人工智慧 is already the frozen core key for that
  item, so Hanzi added for the item = 0 (key ×1 + note citation ×1 on
  both sides). P8 key 138 renders as
  `138. 人工智慧 — 금융 안의 AI는 人工智慧＋예요.`
- `svglib.py` in this build is byte-identical to the core's, md5
  `a269e147529bcb0a1f2dd3aa22fa5658` (same md5 as W43 zh-tw-ko's
  svglib). No svglib change was needed: the core's NO_START already
  covers ASCII closers, and Korean renders on the TC face.

## 10. P7 golden sentences — all 8 verbatim, exactly 2× each

All 8 Traditional quotes are verbatim from this issue's own articles
(article + P7 = 2× each, confirmed by concatenated-node counts, core=2
and edition=2 for all 8). Page tags use the ZH-TW core's form `(p. N)`
(same as W43 zh-tw-ko), NOT zh-tw-de's S. form. Tag distribution,
core = edition: `(p. 1)×2, (p. 2)×1, (p. 3)×2, (p. 4)×1, (p. 5)×1,
(p. 6)×1`.

| quote | tag |
|---|---|
| 用手機轉帳、掃碼付款、網上買保險，都是金融科技 | p. 1 |
| 123個國家及城市、1,600個攤位 | p. 1 |
| 需要才買，不要為了折扣買一堆用不到的東西 | p. 2 |
| 在高雄，鋼鐵也能變成舞台 | p. 3 |
| 福隆的夏天，在10月26日畫下句點 | p. 3 |
| 6比0完封兄弟，龍隊拋下紅色彩帶 | p. 4 |
| 250家店家一起討糖 | p. 5 |
| 旅展首日中午12點才開門 | p. 6 |

P7 geometry deviation from core (documented): readers-box `lh` formula
`+26` → `+46` (+20px padding), the same fix zh-tw-es used for the
core's known ~11px lh underestimate. Siblings varied (es +46, ru +36,
de +40, pt kept +26); this edition uses +46. No other geometry
deviation: phrase-strip row pitch kept at core's 138 (W43 KO used 146,
but W45 core/siblings use 138). Measured: readers box rect y=1184.86,
height 551.5 → bottom 1736.36; last text baseline y=1723.23 (20pt), so
the last line is fully inside the box (verified on the card crop).
P7 teaser ends 2534.36 (< 2580 footer rule, margin 45.64). P7 col3 ends
1736.36. P8-ex ends col 2/3 y=1250 (< 1252), P8-keys ends col 3/3
y=2144 (< 2540).

## 11. Readers' corner

- Frozen Traditional letter `lt` and frozen Traditional disclosure `lt2`
  (`延期披露：VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，
  本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。
  你的來信，下一期見。`) are line-for-line identical to the core.
- English `lcn` replaced with the Korean disclosure + verbatim open
  invitation (exact form): `편집부가 쓴 예시 편지예요 — 진짜 독자 편지는
  아니에요. VOL.1에서 약속한 진짜 독자 편지와 8면 최우수 작문은 아직
  도착하지 않아서, 이번 호에도 예시를 싣고 공개 모집을 계속해요. 여러분의
  편지를 기다릴게요!` — Korean disclosure stating no genuine letters
  exist + open invitation, per the W43 zh-tw-ko precedent form.
  Head: `讀者園地 · 독자 코너`.

## 12. Images — payloads byte-identical to the core

Per-page base64 payloads byte-identical to the core (SHA-256 prefixes:
P1 `af71609d2dd50bca`, P2 `c43d2e269e7d1061`, P4 `1a7e7d6d5ffcede7`,
P5 `7fe6f82082ed5dd9`; P3/P6/P7/P8 have no photos, as in the core).
Credits verbatim from the Commons Artist field: P1 Wilfredor — CC0;
P2 CorraleH — CC0; P4 Bain News Service — Public domain (Washington
baseball team, 1908,
`https://commons.wikimedia.org/wiki/File:Washington_team,_Washington_AL_(baseball)_LCCN2014680242.jpg`);
P5 Benjamin Balazs — CC0.
P4 provenance is CLOSED per the core KIT's coordinator adjudication
dated 2026-10-27: placed bytes and credit unchanged means provenance
is NOT re-litigated.

## 13. Cards eyeballed — all 8

`cards/*.png` (1950×2700) eyeballed: no overflow, no overlap, no footer
collision, image/credit placement clean on every page; P7 readers-box
last line inside the box on the card crop; P7 teaser clear of the 2580
footer rule; P1 badge vs frozen subtitle hierarchy at y=378/434 clean.
Note: two tool-output display artifacts seen during the Latin sweep are
NOT file defects — `穿` in a P7 option and `고객` in P8 key 88 rendered
as replacement characters in the tool result text; byte/ord check
confirms both are present in the delivered SVGs (穿 = U+7A7F).

## 14. PDF pins (8 pages each, verified)

| file | pages | bytes | SHA-256 |
|---|---|---|---|
| `Lucerna-VOL2-KO.pdf` (print) | 8 | 15,287,199 | `bc5573a559188fb59e8676953df3b521504a071dbf6994e0470c26ce38bcc494` |
| `Lucerna-VOL2-KO-web.pdf` (web) | 8 | 3,281,709 | `685b612f248f3372f882e32de0003baf10e7f0541e5abe515ad54a7b82799a68` |

Web PDF is under 10 MB. PDF naming follows the W45 sibling convention
(suffixed, unlike W43's plain names). Render log `build/render1-cards.log`.

## 15. Transform notes (for the next builder of this column)

- The W45 zh-tw-es transform was used ONLY as the source list of the
  core's English explanation strings (its OLD strings are verbatim core
  strings). Extracted pair counts: BSLIB 3, C12 53, C34 61, C56 64,
  C7 54, C8 53 = 288. This edition's transform has **280 pairs** after
  skipping es second-pass Spanish OLDs (not core strings), because the
  Korean equivalents were written concise from the start: C12[52],
  C34[58], C56[62], C56[63] (es shortenings), C7[49] (es head-width
  shortening), C7[50] (es lcn shortening), C7[51] (es wt shortening),
  C7[52] (es memory-trick comma fix), C8[45] (writing key, identity).
- C7[34] is the sentence-frame TAIL only
  (` — the frame 先…再…...`); the quoted head
  `「先去集章，再去看表演。」` is frozen Traditional text and untouched.
  Korean tail: ` — 문형 先…再…는 두 동작의 순서를 나타내요: 먼저 X,
  그다음 Y예요. 직접 만들어 보세요: 先比價，再結帳 (먼저 가격을 비교하고,
  그다음 결제해요).`
- LESSON RE-LEARNED: the transform's `fresh_copy()` wipes the build dir
  (preserving only `preflight-snap*`). The first copies of
  `transform.py`/`ko_map.py`/`gen_transform.py` placed INSIDE the build
  dir were deleted on the first transform run. They were recreated
  outside the build dir; the transform itself must stay outside the
  build dir. The already-transformed build copies survived and were
  regenerated identically from the recreated transform.

## 16. Notes for the proofreader (non-blocking)

- P7 B1 head `B1 · 球賽與節氣 · 경기와 절기` (337.42) is well inside
  the column; no head-width fix was needed.
- The P8 key-41 tail line `26일 = 151일.` and the P8 separators are
  furniture/labels, not orphans (see §7).
- If the proofreader's orphan scan groups by (x, size) across whole
  columns without block segmentation, it will over-flag normal
  word-boundary wraps — use the segmented scan in §7 as the reference.
- P4 provenance: CLOSED per §12; do not re-litigate.
