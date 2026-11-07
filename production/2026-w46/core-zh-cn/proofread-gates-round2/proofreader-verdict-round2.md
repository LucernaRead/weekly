# Proofreader Verdict — Round 2 (FULL round, all 10 editions)

**Issue:** Lucerna Weekly VOL.3, ZH-CN target, dated Mon 2026-11-09 – Sun 2026-11-15 (Beijing time).
**Proofreader:** independent, did not build or fix these editions. No edition file was edited, no re-render was performed, no push/insert/Discord post was made. The fix worker's gate JSONs were NOT accepted; every gate below was re-run independently in this directory.
**Gate directory:** `hidden_files/w46/zh-cn-proofread-gates-round2/` (fresh; the ES-only Round 2 verdict lives separately in `hidden_files/w46/zh-cn-proofread-gates-round2-es/` and was read from there).
**Scope:** all 10 editions — `2026-w46-zh-cn-{de,en,es,fr,it,ja,ko,nl,pt,ru}`. There is no `zh-cn-zh-cn` and no `zh-cn-zh-tw` edition (cross-script exclusions).

## Final verdict

**ROUND 2 FAIL — one blocking defect, D5 (ex. 101 stem), family-wide, all 10 editions.**

Every other check passes: D1, D3 and D4 are CONFIRMED fixed; all 150 key letters verify correct; all geometric, freeze, P8, PDF, abstract and reader-facing gates pass in all 10 editions. The single blocker is a frozen-core stem defect (D5) that makes the correctly answered sentence ungrammatical — on the very page whose own error clinic condemns the identical error. No edition is shippable until D5 is fixed and re-proofread (see §5 for the required fix and re-proofread scope).

## Per-edition verdicts

| Edition | Verdict | Blocking defects | All other gates |
|---|---|---|---|
| zh-cn-en (core) | **FAIL** | D5 only | PASS |
| zh-cn-de | **FAIL** | D5 only | PASS |
| zh-cn-es | **FAIL** | D5 only | PASS |
| zh-cn-fr | **FAIL** | D5 only | PASS |
| zh-cn-it | **FAIL** | D5 only | PASS |
| zh-cn-ja | **FAIL** | D5 only | PASS |
| zh-cn-ko | **FAIL** | D5 only | PASS |
| zh-cn-nl | **FAIL** | D5 only | PASS |
| zh-cn-pt | **FAIL** | D5 only | PASS |
| zh-cn-ru | **FAIL** | D5 only | PASS |

## 1. Fix verification

### D1 (ES-only wrap orphan, Round 1) — CONFIRMED fixed, survives

| Check | Evidence | Result |
|---|---|---|
| ES `.text.md` line 623 | `Responde con fechas y números de la p. 3.` | PASS |
| ES `.text.md` line 1063 | `Responde con fechas y números de la p. 5.` | PASS |
| Old instruction, all 10 `.text.md` exports | 0 occurrences of `Responde con fechas y números de la página` | PASS |
| ES build sources | `content34.py:96` glossline `…de la p. 3.`; `content56.py:91` `…de la p. 5.`; both still carry the `p.` strings (untouched by the key fix) | PASS |
| Visual | ES P3 card: instruction on one line, ex. 39 directly below, no orphan; ES P5 card: same for `p. 5.` / ex. 75 | PASS |
| Orphan scan, all 10 editions | 0 column-start single-digit `N.` candidates; 0 digit-dot nodes outside exercise-number x positions | PASS |

### D3 (P2 matching keys 25/26/27) — CONFIRMED fixed, all 10 editions

- Core registry post-fix, `hidden_files/weekly-report-w46-zhcn-build/content12.py:282`: keys `["d", "c", "b", "a"]`, notes `高潮场 = the peak sale period, d / 包裹 = a parcel, c / 取件码 = a pick-up code, b / 供暖 = central heating, a`.
- Rendered P8 keys in **all 10** editions (SVG text extraction via `p8.py`, cross-checked against the independent registry re-derivation): **25.d / 26.c / 27.b / 28.a**, with trailing note letters matching the key letters in every edition (JA uses the full-width separator `、` — e.g. `25. d — 高潮场 = ピークセール期間、d` — letters match).
- P2 matching block itself unchanged and correct (see §2 block table); P2 SVGs byte-identical to the pre-fix state (see §3).
- Old key list `"c", "b", "d", "a"` occurs 0 times in all 10 build dirs and all 9 transform maps (`oldkey-grep.log`, exit 1 = no match). (The list shape `"d", "c", "b", "a"` also occurs in the P3 43–46 and P5 79–82 match_sets — expected, different sets, not residual.)

### D4 (P6 matching keys 99/100) — CONFIRMED fixed, all 10 editions

- Core registry post-fix, `hidden_files/weekly-report-w46-zhcn-build/content56.py:226`: keys `["c", "d", "a", "b"]`, notes `说法 = a claim, c / 数据 = measured numbers, d / 预报 = a forecast, a / 前置 = placed in advance, b`.
- Rendered P8 keys in **all 10** editions: **97.c / 98.d / 99.a / 100.b**, note letters matching in every edition (JA `、` separator likewise).
- P6 matching block itself unchanged and correct (see §2 block table); P6 SVGs byte-identical to the pre-fix state (see §3).
- Old key list `"c", "d", "b", "a"` occurs 0 times in all 10 build dirs and all 9 transform maps (`oldkey-grep2.log`, exit 1 = no match).

### Fix-verification table (summary)

| Fix | en | de | es | fr | it | ja | ko | nl | pt | ru |
|---|---|---|---|---|---|---|---|---|---|---|
| D1 (ES only) | n/a | n/a | CONFIRMED | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| D3 (25.d/26.c/27.b) | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED |
| D4 (99.a/100.b) | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED | CONFIRMED |

### D2 (Round 1 record-only KIT inaccuracies) — NOT re-raised

- KO KIT total 4300 (REFUTED in Round 1): this round's freeze re-measurement gives KO total added **4304** — the adjudicated figure stands. JA KIT per-page figures: this round's freeze gives per-page 398/477/306/342/283/397/783/1922, total **4908** (p2 477, not 479) — the adjudicated figures stand. The JA "identical to the other 7" conservation wording remains a record-only wording matter; the substantive conclusion (no frozen string lost) is CONFIRMED by freeze set-equality (0 removed/mutated core strings in every edition). No D2 item is re-raised as a defect.

## 2. Full key-letter verification — 150/150 correct

Method: independent AST re-derivation of the registry (`dump_numbered.py`, no import) from `content12.py → content34.py → content56.py → content7.py → content8.py` in source order, assigning numbers 1–150 (130 `ex` calls + 5 `match_set` × 4 = 135 calls). Result: **TOTAL = 150, A2 56 / B1 69 / B2 25**, per-page 10/18/18/18/18/18/12/38. Every key was read against its stem/options and the article text. Rendered P8 keys (`p8.py extract`, keys 1–149 + key 150 rendering as `✓`) compared against the registry: **0 mismatches in every edition**; `p8.py compare` CLEAN 150/150, `keydiff []`, all 10 editions.

### Matching blocks (all five, option-by-option; list order verified before trusting any registry)

| Block | Lefts (in order) | Rights (in order, lettered a–d) | Keys | Verdict |
|---|---|---|---|---|
| P2 25–28 | 高潮场 / 包裹 / 取件码 / 供暖 | a. 北方冬天家里暖和，靠它 = 供暖 · b. 打开快递柜要用的号码 = 取件码 · c. 买的东西，装在里面送来 = 包裹 · d. 双11最忙的卖货时间 = 高潮场 | 25.d / 26.c / 27.b / 28.a | CORRECT |
| P3 43–46 | 消防 / 疏散 / 自救 / 楼道 | a. 自己救自己，先保护自己 = 自救 · b. 火警电话119，防火的事 = 消防 · c. 大家按逃生路线离开 = 疏散 · d. 楼里的走道，逃生路要通 = 楼道 | 43.b / 44.c / 45.a / 46.d | CORRECT |
| P4 61–64 | 瑞士轮 / 内战 / 单败 / 总决赛 | a. 最后一场比赛，决定冠军 = 总决赛 · b. 输一场就回家的赛制 = 单败 · c. 同一个赛区的两支队打 = 内战 · d. 按胜负分组打的比赛 = 瑞士轮 | 61.d / 62.c / 63.b / 64.a | CORRECT |
| P5 79–82 | 重映 / 修复 / 讲座 / 场馆 | a. 办活动的地方，美术馆、图书馆 = 场馆 · b. 听人讲，学东西的活动 = 讲座 · c. 把老电影修好，画面更清楚 = 修复 · d. 老电影再上映一次 = 重映 | 79.d / 80.c / 81.b / 82.a | CORRECT |
| P6 97–100 | 说法 / 数据 / 预报 / 前置 | a. 还没发生的事，先猜一猜 = 预报 · b. 提前放到离买家近的地方 = 前置 · c. 别人说的话，不一定是真的 = 说法 · d. 量出来的数字 = 数据 | 97.c / 98.d / 99.a / 100.b | CORRECT |

Note on the fix record's "rights order" wording: the fix record described the P2 rights as ordered a.供暖/b.取件码/c.包裹/d.高潮场. The rendered rights are as tabled above (a.供暖-definition / b.取件码-definition / c.包裹-definition / d.高潮场-definition) — the same pairing, and the rendered block matches it. The P6 rights are likewise as tabled. No discrepancy.

### Non-matching keys (130)

All 130 cloze/fill/choice keys verified against grammar and the article facts in the core `.text.md` articles (P1–P6), P7 columns and the P8 Xiao Lin passage, and in all 10 P8 renderings. Arithmetic recomputed: 260+90=350; 350−60=290. Writing model recounted at exactly **164 characters** (no spaces in the model; `len == 164` both directions; model in `content8.py`). Weekdays verified with `datetime`: 2026-11-02 Mon (press time), 11-04 Wed, 11-06 Fri, 11-07 Sat, 11-09 Mon, 11-10 Tue, 11-11 Wed, 11-13 Fri, 11-14 Sat, 11-15 Sun — all date/weekday claims in the issue agree. Article facts confirmed: 35th National Fire Day; Swiss stage ended Nov 1 (GEN/DK 3–0, AL 0–3, BLG beat HLE 2–0, quarter-finals 06:00, final Nov 15 03:00); film 1998, re-release Nov 13, Douban 9.3 / 190多万人, 7 venues, Reading Month from Nov 1, culture night Nov 14; P6 three waves, 1.5×/2.5×/3–4×, 35% front-loaded, ~20% last-mile.

Borderline stems examined and ACCEPTED (not defects): ex. 92 (`天气预报是预报` — tautological on its face, but a definition-check fill whose key 预报 is unambiguous); ex. 89/140 (`包裹先前置了` — logistics-jargon compression, key unambiguous); repeated stems with different distractors (e.g. ex. 7/11, 29/39, 34/103/131) — spiral review, not duplication. A mechanical stem-duplication scan flagged only ex. 101 as a genuine doubled-classifier case (see §5).

**Key-verification count: 150/150 key letters correct.** The ex. 101 KEY (个) is itself correct; D5 is a defect of the STEM, recorded separately in §5 — it does not change the 150/150 key count.

## 3. Change isolation

Hash comparison of all 210 edition files (21 per edition × 10) against the fix-keys pre-fix snapshot (`current-edition-hashes.txt`, `hash-diff-pre-vs-current.txt`, `changed-vs-pre.txt`):

- **Exactly 6 files changed per edition:** `.text.md`, print PDF, web PDF, `svg/p8-ceyan.svg`, `cards/p8-ceyan.png`, and `WEEKLY-KIT.md` (fix-record append). The fix record's "exactly 5 files" counts the 5 content artifacts; the 6th file is the KIT fix-record append — adjudication of that claim: CONFIRMED for the content footprint, with the KIT append disclosed here. No other file changed in any edition.
- **P2 and P6 SVGs and cards: 0 changed — byte-identical** in all 10 editions, as required (matching keys print only on P8).
- `.text.md` diffs vs the pre-fix `textmd-before/` copies: exactly 5 changed lines (10 diff lines) in every edition — the 5 corrected note lines (core lines 463/465/467/1353/1355: `c→d`, `b→c`, `d→b`, `b→a`, `a→b`).
- Against the post-fix snapshot: 200/210 files identical; only the 10 KITs differ (fix records appended after that snapshot).
- ES `p.` fix survives unchanged: ES `.text.md` lines 623/1063 and build sources `content34.py:96` / `content56.py:91` unchanged by the key fix (see §1 D1).

## 4. Gate outputs summary (all re-run independently; fix worker's gate JSONs not accepted)

| Gate | Result, all 10 editions |
|---|---|
| Occlusion audit (`occlusion_audit.py`, selftest OK: planted classes BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired 1 each, clean controls silent) | **0 flags, all 8 pages × 10 editions**, exit 0 |
| Freeze (`freeze.py diff --strict-cjk`, core vs each edition) | Latin/RU editions: added CJK 0 on every page. JA total added **4908** (per-page 398/477/306/342/283/397/783/1922). KO total added **4304** (per-page 362/420/269/279/246/344/664/1720), KO Hanzi-added 0. Core CJK totals per page unchanged 932/968/877/787/901/1019/741/1084. 0 removed / 0 mutated core strings everywhere. (JA/KO `--strict-cjk` exit 1 is the expected CJK-script-layer behaviour, not a freeze failure.) |
| P8 (`p8.py extract --total 150` + `compare` vs core) | Extract 150/150 every edition; compare CLEAN, missing=[], extra_count=0, keydiff=[] |
| Rowcheck §1 | CLEAN, all 8 pages × 10 editions (80/80). (Exit code 1 is the known §2 crash on hardcoded `p6-verdieping.svg`, FileNotFoundError, N/A — identical in Rounds 1–2. §3 not run; covered by freeze + P8.) |
| Counts | Per-page 10/18/18/18/18/18/12/38; union exactly 1–150, no duplicates/gaps; levels A2 56 / B1 69 / B2 25 |
| P6 chart | Bars identical all 10: (325,1274,220,30,#3e4c2a), (325,1324,330,30,#b3a06a), (325,1374,550,30,#b3a06a), (325,1424,770,30,#b3a06a) |
| P7 phrases | All 8 phrases exactly 2× in all 10 editions, each 1× on its source article page + 1× on P7, identical in all editions: 「双11的正日子」(P1), 「先看结算页，再决定买不买」(P2), 「提高自防自救能力」(P3), 「三支队进了八强」(P4), 「输了就回家」(P4), 「老电影，新画面」(P5), 「快递的高峰分三波」(P6), 「着火了不坐电梯」(P3) |
| Kinsoku | 0 line-start / line-end flags, all 10 editions |
| Masthead pixel clearance | Wordmark ink x 716–1233 in all 10 (margins 259/258 vs centre 975 — centred within 1 px); subtitle 617–1332 identical; badge lines centred within 1 px; 0 rows with ink outside the frame (x<25 or x>1924). Saved `masthead-pixel-r3.json` |
| Badge + footer | Pairing badge present in the P1 masthead of all 10 (fill `#3e4c2a`, centred; e.g. EN `简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers`; JA/KO likewise native). Footer line with Lucerna + VOL.3 + pairing on all 8 pages × 10, in the reader's language, with native page labels (e.g. `第 8 版 / 共 8 版`, `Seite 8 von 8`, `8 ページ（全 8 ページ）`) |
| PDF text layer | All 10 web PDFs 8 pages, ≤ 7 MB (en 2,390,819; de 2,512,304; es 2,497,485; fr 2,405,806; it 2,420,621; ja 2,730,430; ko 2,526,539; nl 2,484,971; pt 2,450,699; ru 2,275,738 bytes). Text bytes > 0 and **byte-identical web vs print** in every edition (en 45,077; de 46,148; es 45,801; fr 47,170; it 45,878; ja 47,271; ko 46,858; nl 45,191; pt 45,683; ru 55,440) |
| ABSTRACT.txt | All 10 present, single line + trailing newline, 0 ASCII double-quotes, Lucerna + VOL.3 + A2–B2 + 150 present, each reader-native with real topics (Double 11, Fire Day Mon Nov 9, S16, The Legend of 1900 4K, Shenzhen Reading Month). Practice framing PASS under the Round 1 adjudication (product front-loaded, topics as material; the SOP-blessed generic closing slogan is not re-raised) |
| Images | 5 `<image>` elements per edition, 1 each on P1–P5, 0 on P6–P8; credits present on all 5. Embedded payload MD5s identical across all 10 editions, same 5 in page order: `420c6150…`, `550e463b…`, `d0b015bc…`, `6b8e9037…`, `a903e35f…`. (Payload provenance vs original source files: not verified, as in prior rounds.) |
| Scripts / residue | Latin/RU editions Hangul 0, kana 0; JA hiragana 1752, katakana 641, Hangul 0; KO Hangul 4304, kana/Cyrillic 0; RU Cyrillic 10,563; Traditional-only strict-form hits 0 in all 10 |
| Politics scan | 0 hits, all 10 editions |
| Reader-facing sweep | 0 hits, all 10 editions (no W46/w46/zh-cn/2026-w46/SOP/proofread/occlusion/audit/GitHub/insert.py/freeze/lint) |
| Native-language layer | Added-string layer per edition read via freeze `added_strings`; targeted cross-language marker scan (EN/ES/FR/DE/IT/NL/PT/JA/KO/RU instruction markers in the wrong editions): clean — all hits are shared cognates in the edition's own language (`Completa` in IT/PT, `Página` in PT). No English sentences, no wrong-language instruction residue. Abstracts, badges, footers, P8 notes read in all 10. **Caveat, stated honestly:** a line-by-line native read of P2–P7 explanation prose in all 9 fan-outs was not performed (same caveat as Round 1); the scans above are the extent of the native-language check beyond the core and ES article pages, which were read in full. |
| W45 promise handling | S16/finalists disclosure present on P1 + P4 (press time Nov 2, finalists not yet known); VOL.2 readers'-letter promise disclosed in the P7 readers' corner of all 10 editions (editor's example, deferred not cancelled; VOL.2 mention present in all 10 P7 SVGs); VOL.4 teaser on P7 |

### Cards viewed at full frame

P8 of all 10 editions; P1 of EN and JA; P2 of EN and DE; P6 of EN and FR; P3 and P5 of ES (D1); P7 of EN (ex. 101 + clinic). No overflow, overlap, missing glyphs/tofu, or missing image credits in any card viewed. The remaining P1/P2/P6 cards were not read at full frame in this round; they are covered by the occlusion audit (0 flags), rowcheck §1 (CLEAN), freeze set-equality, the masthead pixel scan (identical geometry in all 10), and P2/P6 SVG byte-identity to the pre-fix state. This sampling is recorded here rather than claimed as full-frame coverage of all 40 cards.

Not run / not claimed: freeze baseline reproduction (re-running the core build) — consistent with Rounds 1–2.

## 5. Residual defects

### D5 — ex. 101 stem produces an ungrammatical sentence when answered correctly. BLOCKING. Family-wide, frozen-core, all 10 editions.

**Evidence.**

1. Stem (identical in all 10 build dirs, `content7.py:20`, and in all 10 P7 SVGs):
   `我拿了一个___包裹。` — key `个` (registry `content8.py`; P8 note 101 in all 10 editions: `包裹 takes the measure word 个 gè.`).
2. Completed with the key, the sentence reads: `我拿了一个个包裹。` — a doubled classifier: 一个 + 个 before the same noun. Ungrammatical Mandarin.
3. The issue's own P7 error clinic — on the SAME page, in all 10 editions — corrects exactly this error:
   wrong `我拿了两个包裹个` → `我拿了两个包裹。`, glossed "Order: number + measure word + noun."
   The P7 A2 column immediately above ex. 101 itself teaches `一个包裹 (a parcel)`. A learner who answers ex. 101 correctly produces a sentence the same page teaches is wrong.
4. Confirmed visually on the EN P7 card (stem renders `我拿了一个___包裹。`; clinic pair renders as quoted above).

**Ruling: DEFECT (blocking).** The key is the correct measure word for 包裹 — that is not in dispute, and the key must NOT change. The defect is the stem as authored: it already contains 一个 before the blank, so the blank cannot be filled with 个 without duplicating the classifier. The ES-only Round 2 verdict passed this item and the fix record framed it as "stem awkwardness, NOT a key error"; this round respectfully departs from that framing because the completed sentence is not merely awkward — it is ungrammatical, and the issue itself marks the identical construction as an error on the same page. In a language-learning product under proofread-until-zero, a stem whose correct answer yields an ungrammatical sentence is a blocking content defect, not a matter of taste.

**Required fix (minimal, key unchanged):** remove 一个 from the stem in the frozen core registry (`content7.py:20` in the core build dir) and fan out to all 10 editions:
`我拿了一个___包裹。` → `我拿了___包裹。`
Key stays 个; P8 note 101 stays valid as written. No other stem, key, or note changes.

**Re-proofread scope after the fix:** P7 SVG/card/PDF/`.text.md` in all 10 editions (confirm the new stem renders, no reflow/overflow, `.text.md` diff is exactly the stem line per edition); confirm P8 keys/notes untouched (hash-compare P8 SVG/card vs current state); re-run the PDF text-layer check (web == print) since the PDFs embed P7. No re-verification of the other 149 keys is needed — the key set is unchanged.

### Complete residual defect list

D5 is the ONLY residual defect. No other new or residual defects were found in this round. D1, D3, D4 are fixed and verified; D2 items stay record-only and are not re-raised.

## 6. Seed record (for the next round)

VOL.3; 150 exercises; A2 56 / B1 69 / B2 25; per-page 10/18/18/18/18/18/12/38. Core P1 opening (verified from the rendered P1 card): article 「双11到了，包裹也要到了」; opening sentences: 「今年的双11，现货从10月12日就开始卖了。京东10月12日晚上8点开始卖现货，淘宝和天猫10月20日晚上8点现货开售，现货一直卖到11月13日。11月10日星期二晚上8点，高潮场开始。11月11日星期三，是双11的正日子。」

## Gate artifacts saved in this directory

`dump_registry_r3.py`, `dump_registry_r3.log`, `registry-dump-r3.json`, `dump_numbered.py`, `numbered-keys-r3.txt`, `registry-numbered-r3.json`, `run_gates_r3.sh`, `run_gates_r3.out`, `gates-summary.txt`, `occlusion-selftest.log`, `occlusion-{en,de,es,fr,it,ja,ko,nl,pt,ru}.json/.log`, `freeze-{en,de,es,fr,it,ja,ko,nl,pt,ru}.json/.log`, `p8-extract-{en,de,es,fr,it,ja,ko,nl,pt,ru}.json/.log`, `p8-{en,de,es,fr,it,ja,ko,nl,pt,ru}.json/.log`, `analyze_r3.py`, `analyze-r3.log`, `counts-phrases-chart-r3.json`, `rowcheck-{en,de,es,fr,it,ja,ko,nl,pt,ru}.log`, `pdftext-web/print-{en,de,es,fr,it,ja,ko,nl,pt,ru}.txt`, `oldkey-grep.log`, `oldkey-grep2.log`, `current-edition-hashes.txt`, `hash-diff-pre-vs-current.txt`, `hash-diff-post-vs-current.txt`, `changed-vs-pre.txt`, `badge-textmd-evidence.log`, `native-layer-scan.log`, `crosslang-scan.log`, `masthead-pixel-r3.json`, `proofreader-verdict-round2.md` (this file).

## Final verdict line

**ROUND 2 FAIL (blocking defect D5 — ex. 101 stem, all 10 editions; fix: remove 一个 from the stem, key 个 unchanged; re-proofread P7 only per §5).**
