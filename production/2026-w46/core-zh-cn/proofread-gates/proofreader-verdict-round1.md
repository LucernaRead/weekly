# Proofreader Verdict — Round 1 — Lucerna Weekly W46, ZH-CN family

- Issue: 2026-W46, dated Mon 2026-11-09 – Sun 2026-11-15 (Beijing time).
- Scope: all 10 ZH-CN-target editions (reader-native en/de/es/fr/it/ja/ko/nl/pt/ru).
  The zh-cn-en edition lives in `files/weekly-report-w46-zh-cn-core/`; the other nine in
  `files/weekly-report-w46-zh-cn-{de,es,fr,it,ja,ko,nl,pt,ru}/`.
- Proofreader: independent (did not build these editions). No edition file was modified.
  No re-render, no push, no insert, no Discord post, no chat dump.
- Gate artefacts: `hidden_files/w46/zh-cn-proofread-gates/` (occlusion/freeze/p8 JSONs+logs,
  rowcheck logs, masthead-pixel.json, text-analysis.json, pdftotext outputs, ES crops).
- SOP: `files/weekly-report-SOP.md` read in full before any check. All 10 KITs read.

## Final verdict line

**ROUND 1 FAIL — blocking defect D1 in 2026-w46-zh-cn-es only (P3 + P5 stray wrap-orphan
lines). The other 9 editions PASS Round 1 and are shippable. zh-cn-es must be fixed,
re-rendered (P3/P5 only), re-gated, and re-proofread (Round 2, ES only) before it ships.**

## Per-edition verdicts

| Edition | Verdict | Basis |
|---|---|---|
| 2026-w46-zh-cn-en (core dir) | PASS | All gates re-run clean; P1/P8 full-frame clean; keys spot-checked. |
| 2026-w46-zh-cn-de | PASS | All gates re-run clean; P1/P8 full-frame clean. |
| 2026-w46-zh-cn-es | **FAIL** | Blocking defect D1 (P3, P5). All other gates clean; P1/P8 clean. |
| 2026-w46-zh-cn-fr | PASS | All gates re-run clean; P1/P8 full-frame clean. |
| 2026-w46-zh-cn-it | PASS | All gates re-run clean; P1/P8 full-frame clean. |
| 2026-w46-zh-cn-ja | PASS | All gates re-run clean; P1/P8 full-frame clean. |
| 2026-w46-zh-cn-ko | PASS | All gates re-run clean; P1/P8 full-frame clean. |
| 2026-w46-zh-cn-nl | PASS | All gates re-run clean; P1/P8 full-frame clean. |
| 2026-w46-zh-cn-pt | PASS | All gates re-run clean; P1/P8 full-frame clean. |
| 2026-w46-zh-cn-ru | PASS | All gates re-run clean; P1/P8 full-frame clean. |

## Defect list

### A. Frozen-core defects

**None found.** Freeze conservation, strict-CJK, P8 set equality, chart geometry, badge/footer
strings, kinsoku, Traditional-character, politics and reader-facing scans are clean in all 10
editions (see Gate summary). No frozen Simplified body string is lost or changed in any edition.

### B. Edition-specific defects

#### D1 — BLOCKING — zh-cn-es only: stray wrap-orphan lines on P3 and P5

- **Files:**
  - `files/weekly-report-w46-zh-cn-es/svg/p3-wenhua.svg` — `<text x="527" y="2115.4249999999997">3.</text>`
  - `files/weekly-report-w46-zh-cn-es/svg/p5-qingnian.svg` — `<text x="527" y="2115.4249999999997">5.</text>`
- **Wrong text (rendered):** the section-C instruction wraps and orphans the trailing page
  number onto its own line:
  - P3: line 1 `Responde con fechas y números de la página` / line 2 `3.`
  - P5: line 1 `Responde con fechas y números de la página` / line 2 `5.`
- **Correct text:** the instruction must sit on one line with its page number, as in every
  other edition, e.g. core P3 `Answer with dates and numbers from page 3.` The lone `3.`/`5.`
  reads as a phantom exercise number.
- **Evidence:** SVG text-node dumps (ES P3/P5 vs core at y 2030–2200); rendered crops
  `zh-cn-proofread-gates/crop-zh-cn-es-p3-wenhua-secC.png` and
  `crop-zh-cn-es-p5-qingnian-secC.png` (orphan plainly visible; core control crop
  `crop-zh-cn-en-p3-wenhua-secC.png` shows the single-line form). A scan of all 10 editions
  found no other standalone single-digit `"N."` node. The first section-C exercise is
  displaced ~30 px down in ES (39. at y=2177.1 vs 2147.4 in core; same for 75.). The
  occlusion audit does not flag it (no overlap) and rowcheck §1 is CLEAN (different baselines);
  it was caught only by the text-node scan + visual check. The builder's ES visual check
  covered only P1/P2 (per ES KIT).
- **Scope:** ES only. No overflow results from the displacement (occlusion 0 flags; keys
  budget/column bottoms clean on the rendered cards).
- **Fix (for builder/coordinator; proofreader does not fix):** shorten the Spanish instruction
  so the number stays on line 1 (e.g. use `p. 3` / `p. 5` or a shorter rewording), touching
  only the Spanish explanation string — no frozen Chinese string may change. Re-render ES
  P3/P5, re-run occlusion + freeze + p8 on ES, and re-proofread ES P3/P5 (Round 2, ES only).

#### D2 — NON-BLOCKING, KIT-record inaccuracies (frozen-core/record class; no edition defect)

- **KO KIT total added CJK 4300 — REFUTED.** Measured independently twice: freeze.py
  strict-CJK total **4304**, and an independent Hangul-character count **4304** (per-page
  362/420/269/279/246/344/664/1720). Corrected figure: 4304. No edition consequence:
  KO Hanzi-added = 0 on all 8 pages (CONFIRMED), so the Korean layer adds no Chinese.
- **JA KIT per-page figures — REFUTED in part.** JA KIT per-page figures sum to 4910, not the
  claimed total 4908. Measured: total **4908** (CONFIRMED) with per-page
  398/**477**/306/342/283/397/783/1922 — p2 is 477, not the KIT's 479. Corrected p2: 477.
- **JA KIT conservation wording — REFUTED as worded (D3).** The KIT claims "only 6 missing
  runs, identical to the other 7 shipped fan-outs". Under maximal-run segmentation the other
  7 editions have **5** unique missing runs and JA/KO have **6**; the 6th JA/KO run is the P6
  attribution punctuation `第一财经，` (the full-width `，` was rewritten to `—` in the
  explanation-layer chart note; the attribution itself is preserved in JA and KO). The
  substantive conclusion — no frozen Simplified body string is lost in any edition — is
  CONFIRMED. Only the word "identical" is wrong.

No other defects were established.

## Gate outputs summary (all re-run independently by the proofreader)

| Gate | Result |
|---|---|
| Occlusion (`tools/occlusion_audit.py`, selftest OK first) | **0 flags, all 8 pages × 10 editions**, exit 0. Saved: `occlusion-zh-cn-<lang>.json/.log`, `selftest.log`. |
| Freeze (`tools/freeze.py diff --strict-cjk`) | de/es/fr/it/nl/pt/ru: **added CJK 0 on every page**. JA total 4908. KO total 4304, Hanzi-added 0 all pages. Saved: `freeze-zh-cn-<lang>.json/.log`. |
| P8 (`tools/p8.py` extract + compare, `--total 150`) | Core extract 150/150. All 9 compares **CLEAN, missing=[], extra_count=0, keydiff=[]**. Saved: `p8-*.json/.log`, `p8-extract-*.log`. |
| Rowcheck §1 (same-baseline collisions) | **CLEAN, all 8 pages × 10 editions**. §2 N/A (no `p6-verdieping.svg` in any zh-cn dir). §3 not re-run (needs build dirs; covered by freeze+P8). Saved: `rowcheck-zh-cn-<lang>.log`. |
| Counts | **150 unique exercise chips 1–150, no gaps/duplicates** (range headers `25–28.` etc. expanded) in 9 editions; ES naive 152 is only the 2 D1 stray nodes. **Level split A2 56 / B1 69 / B2 25**, per-page splits exactly as KIT (10/18/18/18/18/18/12/38). |
| P7 phrases | All 8 phrases exactly **2× in all 10 editions**, each 1× contiguous in its source article page + 1× on P7: 「双11的正日子」「先看结算页，再决定买不买」「提高自防自救能力」「三支队进了八强」「输了就回家」「老电影，新画面」「快递的高峰分三波」「着火了不坐电梯」. |
| P6 chart | Bars x=325, widths **220/330/550/770**, h=30, y=1274/1324/1374/1424; first fill `#3e4c2a`, rest `#b3a06a` — all 10 editions. |
| Kinsoku | **0 line-start/line-end orphan flags** in all 10 editions (NO_START incl. small kana, NO_END). |
| Badge / footer / masthead | Badge strings verbatim as KITs in all 10; badge `<text>` fill measured **`#3e4c2a`** (dark olive) in all 10, no badge background rect. Masthead bare `Lucerna` in all 10. Footer line (VOL.3 + Lucerna) on all 8 pages × 10 editions, native-language, verbatim as KITs. |
| Masthead pixels (P1 cards, interior x 65–1885) | Lucerna ink x 715–1234 (margins 650/651) identical in all 10; subtitle 616–1333 (551/552); taglines centred within 1 px; badge lines centred within 1 px, smallest clearance NL 317/318 px, PT 315/316 px; **0 ink outside the frame**. Saved: `masthead-pixel.json`. |
| Images | 5 `<image>` elements per edition, 1 each on P1–P5, 0 on P6–P8. Credits present, identical English strings in all editions. Embedded payloads **byte-identical across all 10 editions** (same 5 MD5s in page order). Provenance MD5s vs source files: UNVERIFIABLE (not re-run; see adjudications). |
| Scripts / residue | Latin/RU editions: Hangul 0, kana 0, Cyrillic 0 except RU 10,563. JA: hiragana 1,752, katakana 641, Hangul 0. KO: Hangul 4,304, kana 0, Cyrillic 0. No wrong-script residue. Added-string English-word scan: only false positives (frozen `Level A2/B1` kickers, loanwords `Quiz/Test`, French `page`, Dutch `week`, `Worlds S16`). FR P8 separator `— Page {n} —` is an adjudicated keep per tables.json/W45 FR (FR KIT). |
| Traditional characters | **Zero** Traditional-only forms in core + de/es/fr/it/nl/pt/ru/ko (clean-list + freeze-conservation method; opencc unavailable on the VM, so no OpenCC t2s diff — see caveat). JA hits inspected in context — all standard Japanese usage (中国語, 今週, 時間, 読書, 避難, 修復, 確認); no 學/讀/雙/讓/還/為/與/來/東/長/門/關/發/對/說/國/親/觀/歡/灣/臺/議/論/權/機/歲/處/帳/陽/陰/雲/靈/龍/龜/點/麵 forms. |
| Politics scan | **0 hits** in all 10 editions (战争/地缘/外交/政治/选举/民调/政党/政府/领导人/主席/总理/人大/政协/台独/六四). No Chinese domestic politics content. |
| Reader-facing sweep | **0 hits** in all 10 editions (W46, w46, zh-cn, 2026-w46, SOP, proofread, occlusion, audit, GitHub, insert.py, freeze, lint over SVG text). |
| PDFs | All 10 web PDFs 8 pages, text layer > 0, **byte-identical to print PDFs**. Text bytes: core 45,077; de 46,148; es 45,811; fr 47,170; it 45,878; ja 47,271; ko 46,858; nl 45,191; pt 45,683; ru 55,440 — matching every KIT byte count. Sizes 2,275,745–2,730,433 bytes, all ≤ 7 MB. Saved: `pdftext-web-*/pdftext-print-*`. |
| ABSTRACT.txt | All 10 present, single line, 0 ASCII double-quotes, reader-native (EN abstract in English), each with Lucerna, VOL.3, A2–B2, 150, real topics. Framing adjudication: PASS (see below). |
| `.text.md` exports | All 10 present, 8 `## ` sections, 1867 lines (es/it/pt/ru 1883 — extra wrapped lines in native layers). Core export cross-checked against SVG for the seed excerpt (same sentences; export uses ASCII punctuation). |
| Dates/weekdays | Verified with `TZ='Asia/Shanghai' date -d`: 2026-11-09 Mon, 11-10 Tue, 11-11 Wed, 11-13 Fri, 11-15 Sun, 11-02 Mon (press time), 11-07 Sat (立冬) — all match issue claims. |
| Visuals | P1 + P8 cards read at full frame for **all 10 editions**; ES P3/P5 crops; core P3 control crop. Clean except D1. P8 top-rule proximity visually clean on all P8 cards (test flow and keys rule do not touch; keys end well above the footer rule). No overflow, overlap, missing glyphs/tofu, or missing credits on any P1/P8 card. |
| Answer-key spot check | P8 keys 113–125 re-derived against stems + KIT facts — all correct (113 A Nov 9; 114 B 35th not 34th; 115 B three waves; 116 B AL out/BLG in; 117 A 06:00; 118 B 1998 not 2019; 119 A Nov 13; 120 B Nov 1; 121 B Nov 10 20:00; 122 A 119; 123 B Oct 20–21; 124 C TES–IG Nov 4; 125 B DK–BLG Nov 6). P8 set equality (above) proves the full set; this checks key correctness on the sample. |

## W45 promises — verified

- **Double 11 / parcels: HONOURED.** P1 lead article, P2, P6 chart and exercises throughout; counts per edition: 双11 32–36, 包裹 68–69.
- **S16 knockout: PARTIALLY HONOURED with an honest press-time limit (as KIT records).**
  Press-time disclosure present on P1 (paragraph + short line) and in the P4 article in **all
  10 editions** (e.g. EN "At press time (Nov 2) the finalists are not yet known.";
  DE "Redaktionsschluss: 2. Nov. — noch offen"; JA "締切 11月2日 — 結果は未定";
  RU "Сдача: 2 нояб. — результатов ещё нет"). The only 半决赛 mentions (core P4, 3×) give
  dates/times and state pairings depend on the quarter-final results
  ("对阵看四分之一决赛结果") — **no semi-final pairing is stated anywhere**. Quarter-final
  draw (TES–IG Nov 4, GEN–LYON Nov 5, DK–BLG Nov 6, T1–KC Nov 7, 06:00, BO5) is stated.
  VOL.4 teaser present on P7 in all editions (VOL.4 + 冠军 markers; core text:
  "S16总决赛打完了，谁是冠军？包裹都到了吗？还有你们的来信和第8版最佳作文。下周见！").
- **Reader letters / best writing: NOT honoured as content because none arrived — disclosed
  honestly (as KIT records).** P7 carries a labelled editor's example plus on-page disclosure
  (core: "编辑部示例信，不是真实来信。VOL.2曾预告本期刊登真实来信和最佳作文；截至11月…征集。
  延期不是取消。" + "读者园地 · Readers' corner"). No fabricated reader name, letter, or
  quotation exists. Promise carried to VOL.4 ("延期不是取消 / Deferred, not cancelled").
- **立冬: already honoured in W45;** in W46 only referenced as past ("立冬已经过了", once per
  edition). Correct per KIT.

## Abstract framing — adjudication: PASS (tension noted)

All 10 abstracts front-load the product (150 A2–B2 exercises) with the week's topics as
material, and none uses the banned "this week's news" framing. The closing slogans
("learn Chinese by reading real Chinese news", "Chinesisch lernen, indem man echte
chinesische Nachrichten liest", "aprender chino leyendo noticias chinas reales", etc.) are
generic brand-level search phrases of exactly the kind SOP §9 blesses ("learn French by
reading"). Tension with the strict 2026-10-28 practice-framing rule is acknowledged: the
slogans do say "learn … by reading … news" in generic form. Adjudicated PASS because (a) the
banned set is specific ("用一周新闻学X" / "this week's news" equivalents — absent here),
(b) the exercise product is front-and-centre in every abstract, and (c) SOP §9 explicitly
blesses the generic phrase for abstracts. Flagged here so the coordinator can see the
reasoning; no change required.

## Seed record (for the coordinator's insert step)

- **Target VOL number:** VOL.3 (第 3 号).
- **Re-measured exercise total + level split:** 150 total; A2 56 / B1 69 / B2 25.
  Per-page: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38.
- **Core P1 article opening, verbatim (Simplified Chinese, from the SVG — full-width
  punctuation authoritative):** article 「双11到了，包裹也要到了」 (A2 head), opening
  3 sentences:
  > 今年的双11，现货从10月12日就开始卖了。京东10月12日晚上8点开始卖现货，淘宝和天猫10月20日晚上8点现货开售，现货一直卖到11月13日。11月10日星期二晚上8点，高潮场开始。11月11日星期三，是双11的正日子。
  (Cross-checked against `2026-w46-zh-cn-en.text.md`, same sentences with ASCII punctuation
  in the export. The P1 deck line above the article is: 「11月10日晚上8点高潮场开始，11月11日是双11，周日凌晨3点是S16总决赛。」)

## KIT-claim adjudications

- **CONFIRMED:** occlusion 0 flags (all 10, re-run); freeze strict-CJK 0 (7 Latin/RU editions);
  P8 extract 150/150 and compare CLEAN (all 9); exercise total 150 and level split 56/69/25
  with per-page splits; phrases 8×2 with article+P7 contiguity; P6 chart rects; badge/footer
  strings verbatim; 5 photos with credits P1–P5; web PDF sizes and pdftotext byte-identity;
  JA total added CJK 4908; KO Hanzi-added 0 and clean kana scan; comma-after-CJK treatment
  (the `个，` run is the only punctuation-level loss, attested); dates/weekdays; W45-promise
  handling as recorded; rowcheck §1 CLEAN (re-run); driver-warning-free builds are consistent
  with all shipped-artifact gates (see UNVERIFIABLE); photo payload identity across editions.
- **REFUTED (record-only, no edition consequence):** KO total 4300 → 4304; JA p2 479 → 477
  (per-page sum 4910 ≠ total 4908); JA "identical to the other 7" conservation wording (5 vs 6
  runs; see D2/D3).
- **UNVERIFIABLE:** embedded-photo MD5s vs source files (payload identity across editions
  confirmed, provenance not re-verified; CREDITS.md MD5 claim not re-checked against source
  assets); builder driver warnings ("0 FLOW OVERFLOW / HEAD TOO WIDE" — no build re-run is
  permitted to a proofreader; shipped artifacts show no overflow by any geometric or visual
  gate except D1, which is a wrap orphan, not an overflow); full native-language prose
  correctness beyond the sampled/read layers (P1/P8 fully read in all 10 editions, added-string
  scans clean, JA/KO layers read and correct — a line-by-line native read of P2–P7 in all 9
  fan-outs was not performed); answer-key correctness beyond P8 set equality + the 113–125
  spot check.

## Caveats

- OpenCC is not installed on the VM: the Traditional-character check is a clean-list +
  freeze-conservation method, not an OpenCC t2s diff. Within that method the result is zero
  Traditional-only forms in all 10 editions.
- The `freeze` field inside `text-analysis.json` uses whole-string multiset diffs and is
  misleading for Latin editions; the authoritative freeze results are the `freeze.py` JSONs.
- `rowcheck.py` §2 crashes on the hardcoded Dutch P6 filename for every zh-cn edition
  (expected; N/A). §1 output was captured before the crash in each log.
