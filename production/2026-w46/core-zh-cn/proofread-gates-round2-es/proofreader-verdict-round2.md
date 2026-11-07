# Proofreader Verdict — Round 2 — Lucerna Weekly W46, 2026-w46-zh-cn-es ONLY

- Issue: 2026-W46, dated Mon 2026-11-09 – Sun 2026-11-15 (Beijing time), VOL.3.
- Scope: ONE edition only: 2026-w46-zh-cn-es
  (`files/weekly-report-w46-zh-cn-es/`). The other 9 ZH-CN editions PASSED
  Round 1 and were NOT re-proofread.
- Proofreader: independent (did not build or fix this edition). No edition
  file was modified. No re-render, no push, no insert, no Discord post, no
  chat dump, no edit to `~/workspace/weekly-git` or `index.json`.
- Gate artefacts: `hidden_files/w46/zh-cn-proofread-gates-round2/` (this
  directory — all gates re-run independently on the final artifacts; the fix
  worker's gate JSONs were not accepted).
- SOP: `files/weekly-report-SOP.md` read in full before any check (Round 1
  verdict + fix report + ES WEEKLY-KIT.md also read). Per SOP §8.4 this is a
  FULL proofread round for the affected edition, not a sample.

## Final verdict line

**ROUND 2 FAIL — Round 1 defect D1 is FIXED and verified clean, but this
full round found NEW blocking defects D3 + D4 (wrong answer keys: 5
matching-exercise letters, ex. 25–27 and 99–100). The edition must NOT ship
until the keys are corrected, re-rendered, re-gated, and re-proofread.
zh-cn-es is NOT shippable on this round.**

## Fix verification (Round 1 D1) — PASS, fully verified

D1 (stray wrap-orphan lines on P3/P5) is gone:

- SVG text-node inspection: P3 carries ONE text node
  (`x=527 y=2085.7`, `Responde con fechas y números de la p. 3.`); P5 the
  same with `p. 5.` No second line, no standalone `3.`/`5.` node anywhere.
- Discriminated orphan scan (all 8 SVGs, re-run): orphan candidates
  (single-digit `"N."` at a column-start x = 65/527/989/1451): **[] — zero**.
  Digit-dot nodes (`N.`/`NN.`/ranges) outside exercise-number x positions
  (137/599/1061/1523): **[] — zero**. The only single-digit `"N."` nodes are
  the 9 legitimate P1 exercise numbers (`1.`–`9.`). Old wording
  `de la página 3.` / `de la página 5.`: 0 occurrences in SVGs, build
  sources, `maps/es.json`, and PDF text. The `p.` abbreviation occurs in
  exactly the 2 fixed strings and nowhere else.
- First section-C exercises sit at the core's y: 39. ES y=2147.425 =
  core y=2147.425; 75. likewise (was 2177.1 pre-fix; the ~30 px displacement
  is gone).
- Visual: P3 and P5 cards read at full frame — the instruction is complete
  on one line with its page number, exercise 39/75 directly below at the
  same level as the neighbouring columns; no orphan, overflow, or overlap
  on either page.
- Fix-source check: `content34.py:96` and `content56.py:91` carry the new
  strings; `maps/es.json` (282 keys) maps both English keys to the new
  Spanish strings; no other string changed. Freeze diff P3/P5 `+39`
  (Round 1: `+40`) is exactly the expected one-string consequence of the
  two-line instruction becoming one string; all per-page CJK core→edition
  counts are unchanged from Round 1 (932→882, 968→946, 877→855, 787→766,
  901→879, 1019→997, 741→721, 1084→1063) — **no frozen Chinese string
  changed**.
- Change footprint verified by sha256: current files are byte-identical to
  the fix worker's post-fix hashes; vs the pre-fix snapshot ONLY
  `svg/p3-wenhua.svg`, `svg/p5-qingnian.svg`, their 2 cards, both PDFs, and
  `.text.md` changed. The other 6 SVGs/cards and `ABSTRACT.txt` are
  byte-identical to pre-fix. The KIT diff vs `KIT-before.md` is only the
  appended fix record (one placeholder line replaced). `.text.md` diff vs
  pre-fix export is exactly lines 623/1063.
- No new orphan/overflow on any page: occlusion 0 flags + rowcheck §1
  CLEAN on all 8 pages (below), and the 6 unchanged pages are byte-identical.

## Defect list

### D3 — BLOCKING, frozen-core — P2 matching keys 25, 26, 27 wrong

- Files: `svg/p2-shenghuo.svg` (exercise D, header `25–28.`) and
  `svg/p8-ceyan.svg` (answer section `— Página 2 —`).
- Rendered right column (P2, x=1485, y=2092/2130/2168/2206):
  a. 北方冬天家里暖和，靠它 (= 供暖)
  b. 打开快递柜要用的号码 (= 取件码)
  c. 买的东西，装在里面送来 (= 包裹)
  d. 双11最忙的卖货时间 (= 高潮场)
- Wrong keys printed (P8): `25. c — 高潮场`, `26. b — 包裹`,
  `27. d — 取件码` (28. a — 供暖 is correct).
- Correct keys: **25. d / 26. c / 27. b** / 28. a.
- Evidence: source call `content12.py:282` (`match_set`, rights in the
  order above, keys `["c","b","d","a"]`); `match_set` prints rights in list
  order lettered a–d (verified in `bslib4.py:220-245`); P8 answer-section
  extraction (see `matching-audit.log`); P2 card at full frame shows the
  same a–d definitions. The core P8 prints the identical wrong keys
  (25. c, 26. b, 27. d), so this is a frozen-core defect, not an
  ES-layer error.

### D4 — BLOCKING, frozen-core — P6 matching keys 99, 100 wrong

- Files: `svg/p6-shendu.svg` (exercise D, header `97–100.`) and
  `svg/p8-ceyan.svg` (answer section `— Página 6 —`).
- Rendered right column (P6, x=1023, y=1836/1874/1912/1950):
  a. 还没发生的事，先猜一猜 (= 预报 — a forecast, not yet fact)
  b. 提前放到离买家近的地方 (= 前置 — placed in advance; cf. article:
  「顺丰今年推了预售极速达：付定金的时候，包裹就先送到离你近的地方」)
  c. 别人说的话，不一定是真的 (= 说法)
  d. 量出来的数字 (= 数据)
- Wrong keys printed (P8): `99. b — 预报 = un pronóstico, b`,
  `100. a — 前置 = colocado por adelantado, a` (97. c, 98. d correct).
- Correct keys: **99. a / 100. b**.
- Evidence: source call `content56.py:226` (keys `["c","d","b","a"]`);
  P6 card at full frame shows the same a–d definitions; core P8 prints the
  identical wrong keys; DE and FR P8 spot-checked (read-only, scope check
  only) print the same wrong 99. b / 100. a. Frozen-core defect.

### Scope note on D3/D4 (for the coordinator)

D3/D4 live in the shared core registry (key letters), faithfully carried
into every fan-out: the core itself and at least DE/FR print the same wrong
keys. Correcting them means fixing the core registry and re-rendering the
affected editions — an ES-only Spanish-layer edit cannot fix them, and this
proofreader fixed nothing. The other 9 editions were NOT re-proofread in
this round (out of scope); their Round 1 PASS verdicts did not cover these
items (Round 1's key spot check was 113–125; P8 set-equality cannot catch
wrong letters when core and edition agree). Whether those PASSes stand is
the coordinator's decision; the evidence here establishes the defect is
family-wide, not ES-specific.

### D2 (Round 1, record-only) — unchanged, no edition consequence

The Round 1 record-only KIT inaccuracies (KO total 4300→4304, JA p2
479→477, JA "identical" wording) were deliberately not applied to edition
content, per instruction. The ES KIT does not repeat the refuted figures.
Not a defect in this edition.

### No other defects found

The remaining 3 matching sets (P3 D 43–46, P4 D 61–64, P5 D 79–82) are
all correct, and all other 145 P8 keys (1–150 audit in full, reading order;
see `p8-answers-reading-order.txt` + `matching-audit.log`) are correct
against stems and articles, including T/F 113–120 and the 164-character
writing model (recounted: exactly 164 characters incl. punctuation).

## Gate outputs summary (all re-run independently by the proofreader)

| Gate | Result |
|---|---|
| Occlusion (`tools/occlusion_audit.py`, selftest OK first) | **0 flags, all 8 pages**, exit 0. Saved: `occlusion-selftest.log`, `occlusion-zh-cn-es.json/.log`. |
| Freeze (`tools/freeze.py diff --strict-cjk`) | **Added CJK 0 on every page** (exit 0; per-page +47/+61/+39/+40/+39/+42/+85/+193). Saved: `freeze-zh-cn-es.json/.log`. |
| P8 (`tools/p8.py` extract + compare, `--total 150`) | Extract **150/150**. Compare core vs ES: **CLEAN, missing=[], extra_count=0, keydiff=[]** — note: this gate proves set equality only; it cannot catch D3/D4, where core and edition share the wrong letters. Saved: `p8-extract-es.json/.log`, `p8-zh-cn-es.json/.log`. |
| Rowcheck §1 (same-baseline collisions) | **CLEAN, all 8 pages**. §2 N/A (crashes on hardcoded NL P6 filename, as in Round 1). Saved: `rowcheck-zh-cn-es.log`. |
| Counts (re-derived) | **150 unique exercise numbers 1–150**, no gaps/duplicates (bare chips + range headers expanded); per-page **10/18/18/18/18/18/12/38**. Level split re-derived from registry calls (static parse of `ex`/`match_set` in content files): **A2 56 / B1 69 / B2 25**; SVG chip/level pairing accounts for 130 individually tagged exercises (A2 48/B1 61/B2 21) + 20 range-grouped P8 items. Saved: `counts-phrases-chart.json`, `level-pairing.log`, `level-registry-static.log`. |
| P7 phrases | All 8 exactly **2×**: each 1× contiguous in its source article page (3 split only across consecutive wrapped lines, verified node-by-node) + 1× on P7 with the correct source-page tag. |
| P6 chart | Bars x=325, widths **220/330/550/770**, h=30, y=1274/1324/1374/1424; first fill `#3e4c2a`, rest `#b3a06a` — matches the 1/1.5/2.5/3.5 scale and the chart note. |
| Kinsoku | **0 flags** (NO_START/NO_END). |
| Badge / footer / masthead | Badge verbatim (`TEXTOS EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`), `<text>` fill **`#3e4c2a`**, centred (x=975 middle anchor). Footer line verbatim on all 8 pages + `Página {n} de 8`. Masthead bare `Lucerna`. Pixel measurement (P1 card): Lucerna ink x 716–1233 (margins 651/652, centred within 1 px), subtitle 617–1332 — matching Round 1 within 1 px (naive band scan also catches rules/frame border; glyph bands agree). Saved: `masthead-pixel.json/.log`. |
| Images | 5 `<image>` elements, 1 each on P1–P5, 0 on P6–P8. Credits present on all 5 (English, CC0/Public domain, Wikimedia Commons). Embedded payloads **byte-identical (MD5) to the core's** on all 5 pages. |
| Scripts / residue | Hangul 0, kana 0, Cyrillic 0 on all pages. **Zero strict Traditional-only forms** (shared-form chars 快/忙/怎/想/意/急/思 only; see `trad-strict.log`). No wrong-script residue. |
| Politics scan | **0 hits** (战争/地缘/外交/政治/选举/民调/政党/政府/领导人/主席/总理/人大/政协/台独/六四). No Chinese domestic politics content. |
| Reader-facing sweep | **0 hits** (W46, w46, zh-cn, 2026-w46, SOP, proofread, occlusion, audit, GitHub, insert.py, freeze, lint). |
| PDFs | Web PDF **2,497,482 bytes (≤ 7 MB), 8 pages**; print PDF 42,127,051 bytes, 8 pages. `pdftotext` **45,801 bytes both, byte-identical** web vs print. Remaining `de la página` hits (4) are all benign (`Lee el calendario/gráfico de la página N`, etc.); old D1 wording 0. Saved: `pdftext-web-es.txt`, `pdftext-print-es.txt`. |
| ABSTRACT.txt | Present, **single line, 579 bytes, 0 ASCII double-quotes**, Spanish, with Lucerna, VOL.3, A2–B2, 150, real topics (Double 11, Día Nacional de la Prevención de Incendios Mon 9 Nov, S16, The Legend of 1900 4K, Shenzhen Reading Month). Practice framing: PASS under the Round 1 adjudication (product front-and-centre; generic closing slogan of the SOP-blessed kind). |
| `.text.md` exports | 1883 lines; diff vs pre-fix export exactly the 2 fixed lines (623/1063). Full text read (all 8 pages, core `.text.md` + ES explanation layer): Spanish spelling/accents/agreement clean; explanation layer faithful to the Chinese body; glossed words occur in their articles; no untranslated strings beyond adjudicated keeps (Level kickers, `Quiz`, P7 B1 English example sentence, photo credits, proper names); `p.` abbreviation only in the 2 fixed strings; no double spaces, no repeated words. Saved: `spanish-hygiene.log`. |
| Dates/weekdays | Verified with `TZ='Asia/Shanghai' date -d`: 2026-11-09 Mon, 11-10 Tue, 11-11 Wed, 11-13 Fri, 11-15 Sun, 11-02 Mon (press time), 11-07 Sat — all match issue claims (11-14 Sat follows from 11-07 Sat). |
| Visuals | **All 8 cards read at full frame** (P1+P8 mandatory + P2–P7). No overflow, overlap, missing glyphs/tofu, or missing image credits on any card. P3/P5 fix visually confirmed (see above). P8 keys end well above the footer rule. The D-section header sitting at a column foot with its items in the next column (P3/P5) is the frozen flow layout, occlusion-clean — observed, not a defect. |
| W45 promises | As Round 1 (re-confirmed in this read): Double 11/parcels honoured; S16 press-time disclosure present, no semi-final pairing stated; reader letters honestly disclosed as editor's example with VOL.4 carry-over; 立冬 referenced only as past. |

## Caveats

- OpenCC is not installed on the VM: the Traditional-character check is a
  strict-form list + freeze-conservation method, not an OpenCC t2s diff.
  Within that method the result is zero Traditional-only forms.
- Rowcheck §3 was not run (needs build dirs; covered by freeze + P8, as in
  Round 1). Rowcheck §2 crashes on the hardcoded Dutch P6 filename (N/A).
- The `p8.py compare` CLEAN verdict does not cover key correctness where
  core and edition agree — D3/D4 were caught only by the semantic
  matching-set audit + full 1–150 key read, which is why they survived
  Round 1.
- Photo-payload provenance vs original source files was not re-verified
  (payload identity vs the core confirmed); builder driver warnings were
  not re-run (no build re-run is permitted to a proofreader).

## Required fix (for builder/coordinator; proofreader does not fix)

Correct the 5 registry key letters at the core source (the `match_set`
`keys` lists): P2 D keys `["c","b","d","a"]` → `["d","c","b","a"]`
(ex. 25→d, 26→c, 27→b); P6 D keys `["c","d","b","a"]` →
`["c","d","a","b"]` (ex. 99→a, 100→b). Re-render the affected editions,
re-run occlusion + freeze + p8, and re-proofread (Round 3) — the fix
touches frozen-core content, so the coordinator must decide the family
scope; at minimum this edition must be fixed and re-proofread before it
ships. D1 needs no further work.
