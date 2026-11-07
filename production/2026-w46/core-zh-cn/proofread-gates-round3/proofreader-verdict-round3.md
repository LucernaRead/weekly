# Proofreader Verdict — Round 3 (P7 scope + regression gates)

**Issue:** Lucerna Weekly VOL.3, ZH-CN target, dated Mon 2026-11-09 – Sun 2026-11-15 (Beijing time).
**Proofreader:** independent, did not build or fix these editions. No edition file was edited, no re-render was performed, no push/insert/Discord post was made, `~/workspace/weekly-git` was never touched, `index.json` was never touched. The fix worker's gate JSONs were NOT accepted; every gate below was re-run independently in this directory.
**Gate directory:** `hidden_files/w46/zh-cn-proofread-gates-round3/` (fresh; rebuild copies used for the pre/post multiset diff were deleted after comparison — the diff log, run logs and hash guards are retained).
**Scope (per the Round 2 verdict §5):** P7 only in all 10 editions — `2026-w46-zh-cn-{de,en,es,fr,it,ja,ko,nl,pt,ru}` — plus the p8.py compare regression gate and the P8-untouched hash confirmation, plus adjudication of the RU observation referred by the fix worker. No re-verification of the other 149 keys was required or performed beyond the p8 regression gate and the D3/D4 spot-confirmation in §2; no full semantic re-verification of native-language prose beyond the scans in §5 was performed (same caveat as Round 2).

## Final verdict

**ROUND 3 FAIL — one blocking defect, D6 (RU P7 footer rendered on the dark teaser band, effectively illegible), RU edition only.**

D5 is CONFIRMED fixed in all 10 editions. Every other P7-scope and regression gate passes in all 10 editions, including P8-untouched (20/20 hashes), p8 compare CLEAN 150/150, occlusion 0 flags, freeze, counts, phrases, kinsoku, PDF text layer and change isolation. Nine editions are shippable as they stand; the RU edition is not, until D6 is fixed and re-proofread at RU-P7 scope (see §4 for the required fix and re-proofread scope).

## Per-edition verdicts

| Edition | Verdict | Blocking defects | All other gates |
|---|---|---|---|
| zh-cn-en (core) | **PASS** | none | PASS |
| zh-cn-de | **PASS** | none | PASS |
| zh-cn-es | **PASS** | none | PASS |
| zh-cn-fr | **PASS** | none | PASS |
| zh-cn-it | **PASS** | none | PASS |
| zh-cn-ja | **PASS** | none | PASS |
| zh-cn-ko | **PASS** | none | PASS |
| zh-cn-nl | **PASS** | none | PASS (NL band/footer graze observed and accepted — see §4.4) |
| zh-cn-pt | **PASS** | none | PASS |
| zh-cn-ru | **FAIL** | D6 only | PASS |

## 1. D5 fix verification — CONFIRMED

**Ruling: CONFIRMED.** The fix is exactly as specified in the Round 2 verdict §5, in all 10 editions, at the source and in every rendered artifact.

### 1.1 Stem in all 10 P7 SVGs (independent SVG text extraction, `analyze_r3.py`)

Exactly one stem node per edition, identical in all 10:

| Edition | P7 stem node (svg/p7-ciyu.svg) |
|---|---|
| en | `我拿了___包裹。` |
| de | `我拿了___包裹。` |
| es | `我拿了___包裹。` |
| fr | `我拿了___包裹。` |
| it | `我拿了___包裹。` |
| ja | `我拿了___包裹。` |
| ko | `我拿了___包裹。` |
| nl | `我拿了___包裹。` |
| pt | `我拿了___包裹。` |
| ru | `我拿了___包裹。` |

Old stem `我拿了一个___包裹。` = **0 occurrences** in: all 80 edition SVGs, all 10 `.text.md` files, all 10 build dirs' sources, and all 20 PDF text layers (web + print). Doubled completed sentence `我拿了一个个包裹` = 0 in all SVGs and all PDF text layers. New stem = 1× in each `.text.md` (line 1379 in every edition, verified line-by-line) and 1× in each web-PDF text layer. Completed with the key, the sentence reads `我拿了个包裹。` — grammatical, no classifier doubling.

The old stem still occurs **3× per WEEKLY-KIT.md** (all 10 KITs) — all three in fix-record documentation only: the D3/D4 record's "Flagged, NOT changed" line (EN KIT line 325), the D5 defect quote (line 333) and the D5 before→after quote (line 334), with the same pattern in the RU KIT (lines 136/144/145). KITs are documentation, not edition content. Per the task instruction, KIT quotations are NOT raised as a defect. No other file in any edition dir contains the old stem.

### 1.2 Build sources

`content7.py:19–20` in all 10 build dirs: line 19 carries the key `个` with the reader-language note (e.g. core `包裹 takes the measure word 个 gè.`; RU `包裹 берёт счётное слово 个 gè.`), line 20 carries the new stem `我拿了___包裹。`. Old stem 0 / new stem 1 per build dir; no other `.py` file in any build dir contains either string. Old D3/D4 key lists occur 0 times in all 10 build dirs; the fixed lists survive (`["d", "c", "b", "a"]` and `["c", "d", "a", "b"]` — per-dir counts 3 and 1 respectively, the D3 count including the two unrelated match_sets that share the list shape, as in Round 2).

### 1.3 Error clinic + A2 column unchanged and consistent

In every edition's P7 SVG: clinic pair exactly `「我拿了两个包裹个」` (1 node) → `→ 「我拿了两个包裹。」` (1 node), gloss `Order: number + measure word + noun` in the reader's language; A2 glossline still teaches `一个包裹` (wrapped across text nodes as before, e.g. core `Measure words still matter: 一个包裹 (a …`). The page is now internally consistent: the clinic condemns the doubled-classifier construction that the exercise no longer produces, and ex. 104 (`哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹`) still teaches the correct form. The completed ex. 101 answer (`我拿了个包裹。`) does not contradict any clinic or gloss line.

### 1.4 Visual (P7 at full frame, all 10 editions)

In every edition the fixed stem renders as `我拿了___包裹。` on a single line under `101.` with the blank gap intact, followed directly by ex. 102 — no overflow, no re-wrap orphan, no shift of any neighbouring block, clinic + A2 column consistent. (RU P7 is otherwise clean at full frame; its sole defect is the footer/band issue D6 in §4, unrelated to the stem.)

## 2. P8-untouched hash confirmation + p8 regression gate + D3/D4 spot-confirmation

### 2.1 P8-untouched: CONFIRMED — 20/20 byte-identical to the Round 2 state

Current SHA-256 of all 10 P8 SVGs + all 10 P8 cards was re-hashed independently and compared against the fix worker's retained pre-fix snapshot (`zh-cn-fix-round3/pre-fix-p8-hashes.txt`, taken before any D5 edit — i.e. the Round 2 state). **All 20 match exactly.** (The fix report's tabulated hashes were verified, not trusted: each hash below is this round's own computation.)

| Edition | `svg/p8-ceyan.svg` | `cards/p8-ceyan.png` |
|---|---|---|
| en | `937871c262133e316b40dcc33e95f786a5c21f3a13e9e08c361d339efca4f92d` | `b5c7a50d0cf4feab9086511a1fb81427d2fc73ac0423d02691c8bbb2e76d1314` |
| de | `a062bbe269f7cd863e1f843de6244b129641b271620c9fe4273ed1eb72a2a66a` | `268e4aa5cee9c5e4c5716838513af41d2bc2781b552caf3a70d6c28a8c1fda40` |
| es | `8b9e73b94ad8c7539dc13fc469806f5a8ecb6b801780f1967322cc4fadc152c0` | `2ae73144eef68580fa5b61df9f203a458d17338023e4ced45f964a3492c3e9b2` |
| fr | `8f42782927883a279ecaa2f33956cd9e097aceb14f5e10b9b555f850ba17eb32` | `63b496b3519d46c5e628d2e124f06033fd0547a3c9adf3db6f02670b3c9f3e90` |
| it | `26965d102b2dce9773ffd2cbd2bc647aabcc9aa0326b2226f83d2dcfb403b6c9` | `0a46641b8e95f0f695b9d93932248be4736086ebfd64ffbdfbd01be7cedace0b` |
| ja | `899ba552c851db91368e65927004fc0e2efb56952ddd0bb25ac375af84ff3e8f` | `90827a560139d1f54fc203251c595664a8b5819ed90569079abeee97ea702051` |
| ko | `981d8898035d9727ffea1e565d97d0762bd15d8f6f47003adbe4fd4bed646699` | `099432f580df4ee025fbaf7d3a166097259073917435d0904f0b4c90eee866d4` |
| nl | `062c08dedb5410645b9ac4ad983ea6cee334786f9273540dca23b26847c56077` | `b0c84242f601a55daf8f9bd02db34691f83f1f0709a3f312541648099792a85c` |
| pt | `95b42d0a05dfdec591d10192a58bd8e84c1781547db94d67a1664587fc7f4e85` | `46544e4f73dd6559a77894c5dc6a15ad8b62bd7d1c7a9ed47f5c3d1f727bacde` |
| ru | `cdf804c1c97bc62bc74e9f044a65c568909895df1f5cc94c4353a429e958a116` | `21daa9b9a25cf9d0477c7e95fe10144031663db85c74b1b6cab7db54bddd4495` |

### 2.2 P8 note 101 byte-identical (independent extraction + retained pre-fix evidence)

Each edition's current P8 note 101 (from this round's own SVG extraction) is present verbatim in BOTH the retained pre-fix evidence (`before-quotes.txt`) and the post-fix quotes (`after-quotes.txt`) — before = after, unchanged:

| Edition | P8 note 101 (before = after) |
|---|---|
| en | `101. 个 — 包裹 takes the measure word 个 gè.` |
| de | `101. 个 — 包裹 nimmt das Zählwort 个 gè.` |
| es | `101. 个 — 包裹 lleva el clasificador 个 gè.` |
| fr | `101. 个 — 包裹 prend le classificateur 个 gè.` |
| it | `101. 个 — 包裹 prende il classificatore 个 gè.` |
| ja | `101. 个 — 包裹 は量詞 个 gè を取る。` |
| ko | `101. 个 — 包裹 는 양사 个 gè 를 써요.` |
| nl | `101. 个 — 包裹 neemt het telwoord 个 gè.` |
| pt | `101. 个 — 包裹 leva o classificador 个 gè.` |
| ru | `101. 个 — 包裹 берёт счётное слово 个 gè.` |

Key 101 stays `个` in every edition; the note remains valid for the fixed stem.

### 2.3 p8.py regression gate: CLEAN 150/150, all 10 editions

`tools/p8.py extract --total 150` + `compare` vs core, re-run independently: extract 150/150 every edition; compare **CLEAN, missing=[], extra_count=0, keydiff=[]**, exit 0, all 10 editions. No p8 failure; no regression.

### 2.4 D3/D4 keys spot-confirmed in native P8 rendering (all 10 editions)

From this round's own P8 SVG text extraction, key letter + trailing note letter agree in every edition (JA uses the full-width separator `、`):

- **25.d / 26.c / 27.b** — e.g. EN `25. d — 高潮场 = the peak sale period, d`, `26. c — 包裹 = a parcel, c`, `27. b — 取件码 = a pick-up code, b`; JA `25. d — 高潮场 = ピークセール期間、d`; RU `27. b — 取件码 = код получения, b`.
- **99.a / 100.b** — e.g. EN `99. a — 预报 = a forecast, a`, `100. b — 前置 = placed in advance, b`; RU `99. a — 预报 = прогноз, a`, `100. b — 前置 = размещено заранее, b`.

D1 (ES `p.` fix) survives: ES `.text.md` line 623 `Responde con fechas y números de la p. 3.` and line 1063 `…de la p. 5.`; old instruction `Responde con fechas y números de la página` = 0 in all 10 `.text.md` files. D1/D3/D4 are NOT re-raised.

## 3. Change isolation — exact

- **File-hash diff** (all 210 edition files, current vs the retained pre-fix snapshot): exactly **6 files changed per edition** — `.text.md`, print PDF, web PDF, `svg/p7-ciyu.svg`, `cards/p7-ciyu.png`, and `WEEKLY-KIT.md` (fix-record append). The 5 content files are the D5 footprint; the 6th is the KIT append. All other 15 files per edition byte-identical, including all P8 SVGs/cards (see §2.1).
- **SVG-text multiset diff** (genuine pre/post comparison, independently rebuilt): each build dir was copied into this gate directory, ONLY the stem in `content7.py:20` was reverted, `OUT` was redirected to the copy, and `run.py` was executed there (shipped files hash-guarded before/after: UNCHANGED). Text-node multisets of the rebuilt pre-fix SVGs vs the shipped post-fix SVGs: **70/80 pages identical; the other 10 are the P7 pages, each differing by exactly one node** — `我拿了一个___包裹。` (pre) → `我拿了___包裹。` (post). Rebuild registry stats in all 10 copies: TOTAL 150, A2 56 / B1 69 / B2 25, per-page 10/18/18/18/18/18/12/38, writing model 164 — the key set is unchanged by the fix.
- **`.text.md` diffs:** exactly line 1379 per edition (verified against the fix worker's retained `textmd-before/` copies and by this round's own line-1379 read).
- **RU geometry-only comparison** (pre-fix rebuild vs shipped, §4.2): 0 geometry diffs across all 189 P7 elements — the single differing element is the stem text node itself (same x/y/size/fill).

## 4. RU observation — adjudication: DEFECT (D6, blocking, RU only)

### 4.1 What was observed

On the RU P7 card, the dark VOL.4 teaser band and the footer line overlap: the footer string is rendered in dark type on the dark band and is effectively illegible.

### 4.2 Geometry (independent SVG measurement, all 10 P7 editions)

RU P7 (`svg/p7-ciyu.svg`, document order):

- `[183] rect x=65 y=2518.52 w=1820 h=118 fill=#2c2822` — teaser band, y 2518.52–2636.52.
- `[184] text x=93 y=2562.52 fill=#e8dfc8` — teaser title `下期预告 · На следующей неделе (VOL.4)` (light on dark, by design).
- `[185] text x=93 y=2602.52 fill=#f3edda` — teaser sentence (light on dark, by design).
- `[186] line y1=2580` — footer rule, painted after the band, crossing the band interior.
- `[187] text x=65 y=2624 fill=#57523f` — footer `Lucerna · КИТАЙСКИЙ (УПРОЩЁННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ`.
- `[188] text x=1885 y=2624 fill=#57523f anchor=end` — `Страница 7 из 8`.

The footer baseline (2624) lies **12.52 px INSIDE the band** (band bottom 2636.52); the entire footer ink band (~2606–2629) sits on the dark band, across its full width (band x 65–1885 = footer x-range). Contrast (WCAG, computed from the SVG fills): footer `#57523f` on band `#2c2822` = **1.87:1**; the same footer on the paper `#f7f1e2` = **6.94:1**; the teaser light texts on the band = 11.03:1 / 12.51:1. The footer on the band has roughly a quarter of its intended contrast.

**RU-only.** Teaser-band bottoms on P7 in the other 9 editions: EN/FR/IT/JA/KO 2514.00 (110.00 px above the footer baseline), ES 2527.96, PT 2523.98, DE 2554.48, NL 2607.52 (16.48 px above the baseline — footer ink clears it; see §4.4). RU is the ONLY edition whose band bottom (2636.52) passes the footer baseline. The other 7 RU pages have no dark band near the footer (footer on paper everywhere else; RU P8 footer legible at full frame). Cause: RU P7 content above the band runs ~122 px taller than the core, pushing the flow-placed band down into the footer zone. This is a layout-overflow consequence in one edition, not a family design.

**Predates the D5 fix: CONFIRMED.** The fix worker's claim was re-verified independently (§3): geometry-only element comparison of the rebuilt pre-fix RU P7 vs the shipped RU P7 shows 0 diffs (189 elements; the fix worker's "188" is the same count excluding the SVG root). The stem change moved nothing.

### 4.3 Visual evidence (viewed, not inferred)

- **RU P7 band/footer crop** (y 2480–2680, 2×, `ru-p7-band-footer-crop.png`): the footer string is faint dark-on-dark type sunk into the band's lower edge — decipherable at 2× only because the string is known; the right-hand `Страница 7 из 8` is likewise faint. The gold footer rule strikes through the band between the two teaser lines.
- **RU P7 at full frame**: the footer line at the bottom of the page is barely visible — a dark smudge on the dark band — while every other line on the page, including the light teaser text, is crisp. A reader at normal size cannot read the footer (刊名/版次 identification + page number).
- **Controls, same crops:** EN footer crisp dark-on-paper with the band well clear; NL footer fully legible on paper (§4.4).

The footer text is therefore NOT merely "on the band's lower edge" in a cosmetic sense, and NOT legible in any practical sense. The fix worker's description understates the effect: the footer is fully inside the band, at 1.87:1 contrast.

### 4.4 Occlusion audit: 0 flags — agreed as a gate result, not as a readability verdict

The canonical audit re-run in this round reports **0 flags for RU** (all 8 pages × 10 editions, selftest OK). That result is correct under the tool's definitions and is NOT disputed: the footer text is painted AFTER the band (so it is not "covered" by the audit's COVER rule), and footer-baseline texts are exempt from the FOOTER rule by design. But the audit is **blind to this defect class**: it does not measure foreground/background contrast of a later-painted text against an earlier-painted dark shape. The 0-flag result therefore does not settle readability, and I do not treat it as doing so. This is the same class of blind spot the SOP itself records for thin lines (附则一补注) — a gate passing does not end visual adjudication. The pixel + contrast + geometry evidence above is the basis of this ruling.

### 4.5 NL near-graze: observed, ACCEPTABLE, not raised

NL's band bottom (2607.52) passes just above the footer ink: at full frame and in the matching crop, the NL footer is fully legible on paper, and the gold rule's crossing of the band's lower portion does not touch footer ink. The NL teaser line 2 descenders graze the gold rule cosmetically; the text stays legible. No action. (This distinction — NL footer ink clears the band, RU footer ink is inside it — is exactly the line between acceptable and defect here.)

### 4.6 Ruling: DEFECT (blocking, RU edition only)

**D6 — RU P7 footer illegible: the footer furniture (pairing line + page number, present and legible on all other 79 pages) is rendered dark-on-dark inside the teaser band on RU P7 only, at 1.87:1 contrast, effectively unreadable.** Under proofread-until-zero and the SOP's "逐版看图：查溢出、重叠" rule, a page whose footer cannot be read is a blocking defect for that edition. It does not affect the other 9 editions, any key, or any other RU page.

**Required fix (RU P7 only; no stem/key/note changes):** reposition the RU P7 teaser band (with its two teaser lines) upward so that the band bottom clears BOTH the footer rule line (y=2580) with clearance AND the footer ink top (~2606) — i.e. band bottom ≤ ~2570, restoring the footer to paper at its intended contrast — by tightening/compressing the RU P7 flow above the band as needed (the fix worker determines the layout mechanics; the end-state requirement is the band/footer clearance above). Do NOT fix by recolouring the RU P7 footer text (breaks furniture consistency across the issue) or by moving the footer (furniture is fixed at y=2624 on all pages). No other page, edition, stem, key, or note may change.

**Re-proofread scope after the D6 fix (RU only):** RU P7 SVG/card/PDF + `.text.md` (confirm band/footer clearance in SVG geometry, full-frame card + band/footer crop, PDF text layer web==print); re-run the occlusion audit on RU; hash-confirm P8 SVG/card unchanged vs the current state (§2.1 hashes) and change isolation (only RU P7 files differ vs current state). No re-verification of the other 9 editions is needed — they are PASS in this round and the fix is RU-scoped.

## 5. Gate outputs summary (all re-run independently; fix worker's gate JSONs not accepted)

| Gate | Result, all 10 editions |
|---|---|
| Occlusion audit (`tools/occlusion_audit.py`, selftest OK: planted classes BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired 1 each, clean controls silent) | **0 flags, all 8 pages × 10 editions**, exit 0. (RU D6 is outside the tool's contrast-blind classes — see §4.4.) |
| Freeze (`tools/freeze.py diff --strict-cjk`, core vs each edition) | Core CJK totals per page: 932/968/877/787/901/1019/**739**/1084 — P7 741 → 739 is exactly the 2 removed characters (`一个`); all other pages unchanged. Latin/RU editions: added CJK 0 on every page. JA total added **4908** (per-page 398/477/306/342/283/397/783/1922) — the adjudicated Japanese-script-layer figures. KO total added **4304** (per-page 362/420/269/279/246/344/664/1720), 100% Hangul, Hanzi-added 0. 0 removed / 0 mutated core strings everywhere. (JA/KO `--strict-cjk` exit 1 is the expected CJK-script-layer behaviour, not a freeze failure.) |
| P8 (`tools/p8.py extract --total 150` + `compare` vs core) | Extract 150/150 every edition; compare CLEAN, missing=[], extra_count=0, keydiff=[] (see §2.3) |
| Rowcheck §1 (same-baseline true-ink collisions, `rowcheck.py`) | CLEAN, all 8 pages × 10 editions (80/80). Exit 1 is the known §2 crash on the hardcoded `p6-verdieping.svg` filename, N/A. (A supplementary advance-width scan run with the wrong script flagged 2 EN/DE P2 column-head pairs; true-ink §1 + occlusion TEXTX both find no ink collision — advance-box overlap between separate columns, discarded as a measurement artifact.) |
| Counts (independent rebuild registry stats, §3) | 150; A2 56 / B1 69 / B2 25; per-page 10/18/18/18/18/18/12/38; writing model 164 |
| P6 chart | Bars identical all 10: (325,1274,220,30,#3e4c2a), (325,1324,330,30,#b3a06a), (325,1374,550,30,#b3a06a), (325,1424,770,30,#b3a06a) |
| P7 phrases (raw-SVG contiguous text, per-page located) | All 8 phrases exactly 2× in all 10 editions, each 1× on its source article page + 1× on P7: 「双11的正日子」(P1), 「先看结算页，再决定买不买」(P2), 「提高自防自救能力」(P3), 「三支队进了八强」(P4), 「输了就回家」(P4), 「老电影，新画面」(P5), 「快递的高峰分三波」(P6), 「着火了不坐电梯」(P3). (A per-text-node join undercounts 3 wrapped phrases; the contiguous raw-text count is the correct measure and is 2× throughout.) |
| Kinsoku | 0 line-start / line-end flags, all 10 editions |
| PDF text layer | All 10 web PDFs 8 pages, ≤ 7 MB (en 2,390,807; de 2,512,298; es 2,497,476; fr 2,405,830; it 2,420,595; ja 2,730,428; ko 2,526,513; nl 2,484,968; pt 2,450,694; ru 2,275,750 bytes). Text bytes > 0 and **byte-identical web vs print** in every edition (en 45,071; de 46,142; es 45,795; fr 47,164; it 45,872; ja 47,265; ko 46,852; nl 45,185; pt 45,677; ru 55,434) — each exactly **−6 bytes vs its Round 2 figure**, i.e. the 2 removed CJK characters, arithmetic verified. Old stem 0 / new stem 1 / doubled sentence 0 in every web text layer. |
| ABSTRACT.txt | All 10 present, single line + trailing newline, 0 ASCII double-quotes, Lucerna + VOL.3 + A2–B2 + 150 present, each reader-native with real topics. |
| Images / credits | Not re-audited beyond scope: P8/P1 spot cards viewed show image + credit present (EN P1 locker photo + `Photo: Map hobby — CC0 (Wikimedia Commons)`); P8 SVGs/cards byte-identical to the Round 2-verified state, so the Round 2 image-payload findings stand. No missing-glyph/tofu observed on any card viewed. |

### Cards viewed at full frame

P7 of all 10 editions; P1 of EN; P8 of EN and RU. No overflow, overlap (other than D6, adjudicated separately), missing glyphs/tofu, or missing image credits in any card viewed, except D6 on RU P7. Band/footer crops viewed for RU, NL (comparator) and EN (control). The remaining P1–P6/P8 cards were not read at full frame in this round; they are covered by the occlusion audit (0 flags), rowcheck §1 (CLEAN), freeze set-equality, the P8 hash proof, and the pre/post multiset diff (70/80 pages identical). This sampling is recorded here rather than claimed as full-frame coverage of all 80 cards.

Not run / not claimed: freeze baseline reproduction (re-running the core build) — consistent with Rounds 1–2; the pre/post rebuild in §3 serves as the change-isolation baseline for this round.

## 6. Complete residual defect list

- **D6 (NEW, BLOCKING, RU only):** RU P7 footer rendered on the dark teaser band at 1.87:1 contrast, effectively illegible. Evidence in §4 (SVG elements [183]–[188] in `weekly-report-w46-zh-cn-ru/svg/p7-ciyu.svg`; band bottom 2636.52 vs footer baseline 2624; crops `ru-p7-band-footer-crop.png` / `ru-p7-footer-strip.png`; full-frame RU P7 card). Required fix and re-proofread scope in §4.6.
- **D5: FIXED (CONFIRMED, §1).** D1/D3/D4: fixed and verified, not re-raised (§2.4). D2 items: record-only, not re-raised. KIT quoted history of the old stem: documentation, not a defect (§1.1). NL band/footer graze: observed, acceptable, not raised (§4.5).

No other new or residual defects were found in this round's P7 + regression scope.

## 7. Gate artifacts saved in this directory

`run_gates_r3.sh`, `run_gates_r3.out`, `occlusion-{en,de,es,fr,it,ja,ko,nl,pt,ru}.json/.log`, `freeze-{en,de,es,fr,it,ja,ko,nl,pt,ru}.json/.log`, `p8-extract-{en,de,es,fr,it,ja,ko,nl,pt,ru}.json/.log`, `p8-{en,de,es,fr,it,ja,ko,nl,pt,ru}.json/.log`, `analyze_r3.py`, `analyze-r3.log`, `phrases-r3.log`, `rowcheck-{en,de,es,fr,it,ja,ko,nl,pt,ru}.log`, `rowcheck-summary-r3.txt`, `rowcheck-r3.log` (superseded mis-invocation, retained for transparency), `pdftext-web/print-{en,de,es,fr,it,ja,ko,nl,pt,ru}.txt`, `current-edition-hashes.txt`, `hash-diff-pre-vs-current.txt`, `rebuild_pre.sh`, `rebuild_pre.log`, `rebuild-pre-{en,de,es,fr,it,ja,ko,nl,pt,ru}-run.log`, `rebuild-guard-before.txt`, `rebuild-guard-after.txt`, `svg-multiset-diff-r3.log`, `ru-band-geometry.log`, `ru-band-allpages.log`, `ru/nl/en-p7-band-footer-crop.png`, `ru/nl/en-p7-footer-strip.png`, `proofreader-verdict-round3.md` (this file). (The `rebuild-pre/` build copies were deleted after the multiset comparison; their run logs, guard hashes and diff log are retained.)

## Final verdict line

**ROUND 3 FAIL (blocking defect D6 — RU P7 footer on the dark teaser band, RU edition only; fix: move the RU P7 teaser band clear of the footer rule line and footer ink, RU-P7-only re-proofread per §4.6; the other 9 editions PASS and D5 is CONFIRMED fixed).**
