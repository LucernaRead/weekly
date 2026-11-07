# Fix report — W46 ZH-CN family, Round 2 defects D3 + D4

**Issue:** Lucerna Weekly VOL.3, dated Mon 2026-11-09 to Sun 2026-11-15 (Beijing time).
**Scope:** all 10 ZH-CN-target editions: `2026-w46-zh-cn-en` (core, `files/weekly-report-w46-zh-cn-core/`),
`-de`, `-es`, `-fr`, `-it`, `-ja`, `-ko`, `-nl`, `-pt`, `-ru`.
**Trigger:** Round 2 proofreader verdict D3 + D4
(`hidden_files/w46/zh-cn-proofread-gates-round2/proofreader-verdict-round2.md`) —
frozen-core answer-key registry errors affecting all 10 editions.
**Worker:** fix worker, 2026-11-02/03. Worked locally only: no push, no insert,
no `index.json` edit, no Discord post, no chat dump. No rendered SVG/PDF was
hand-edited; every change went through source content files + full re-render,
with `.text.md` regenerated from the source manuscript.
**Status:** both defects fixed at the source, all 10 editions re-rendered and
re-gated clean. A full Round 3 independent proofread of all 10 editions follows;
this re-gating does not replace it.

## 1. Defect D3 — P2 matching keys 25, 26, 27 (BLOCKING, frozen core)

**Source file:** core build `hidden_files/weekly-report-w46-zhcn-build/content12.py:282`
(list order verified from source: 25–28).

**Rendered right column (P2 SVG, unchanged by this fix — definitions were never wrong):**

| Letter | Definition | Means |
|---|---|---|
| a. | 北方冬天家里暖和，靠它 | 供暖 |
| b. | 打开快递柜要用的号码 | 取件码 |
| c. | 买的东西，装在里面送来 | 包裹 |
| d. | 双11最忙的卖货时间 | 高潮场 |

Left column: 25. 高潮场 / 26. 包裹 / 27. 取件码 / 28. 供暖.

**Semantic derivation:** 25 高潮场 → d (the busiest selling period of Double 11);
26 包裹 → c (the thing bought, packed inside and delivered); 27 取件码 → b (the
code needed to open a parcel locker); 28 供暖 → a (heating keeps a northern home
warm in winter).

**Before (printed P8 keys + note letters):**

```
25. c — 高潮场 = the peak sale period, c
26. b — 包裹 = a parcel, b
27. d — 取件码 = a pick-up code, d
28. a — 供暖 = central heating, a
```

Registry keys: `["c","b","d","a"]` — a rotation of the first three: 25.c was
包裹's definition, 26.b was 取件码's, 27.d was 高潮场's. 28.a was already correct.

**After:**

```
25. d — 高潮场 = the peak sale period, d
26. c — 包裹 = a parcel, c
27. b — 取件码 = a pick-up code, b
28. a — 供暖 = central heating, a
```

Registry keys: `["d","c","b","a"]`, and the four P8 note trailing letters
re-lettered d/c/b/a. Keys and note letters had to change together: P8 prints
`"{n}. {key} — {note}"` (`content8.py:118`; `match_set` in `bslib4.py:220-245`
zips keys with notes in left-word order), so fixing only the keys list would
have left self-contradictory P8 lines.

## 2. Defect D4 — P6 matching keys 99, 100 (BLOCKING, frozen core)

**Source file:** core build `hidden_files/weekly-report-w46-zhcn-build/content56.py:226`
(list order verified from source: 97–100).

**Rendered right column (P6 SVG, unchanged by this fix):**

| Letter | Definition | Means |
|---|---|---|
| a. | 还没发生的事，先猜一猜 | 预报 |
| b. | 提前放到离买家近的地方 | 前置 |
| c. | 别人说的话，不一定是真的 | 说法 |
| d. | 量出来的数字 | 数据 |

Left column: 97. 说法 / 98. 数据 / 99. 预报 / 100. 前置.

**Semantic derivation:** 97 说法 → c (a claim, what someone says, not necessarily
true); 98 数据 → d (measured numbers); 99 预报 → a (a forecast guesses what has
not happened yet); 100 前置 → b (placed in advance near the buyer; cf. the P6
article: 付定金的时候，包裹就先送到离你近的地方).

**Before (printed P8 keys + note letters):**

```
97. c — 说法 = a claim, c
98. d — 数据 = measured numbers, d
99. b — 预报 = a forecast, b
100. a — 前置 = placed in advance, a
```

Registry keys: `["c","d","b","a"]` — 99 and 100 swapped: 99.b was 前置's
definition, 100.a was 预报's. 97.c / 98.d were already correct.

**After:**

```
97. c — 说法 = a claim, c
98. d — 数据 = measured numbers, d
99. a — 预报 = a forecast, a
100. b — 前置 = placed in advance, b
```

Registry keys: `["c","d","a","b"]`, and the two P8 note trailing letters
re-lettered a/b.

## 3. Where the fixes were applied

- **All 10 build dirs** — `weekly-report-w46-zhcn-build` (core) plus
  `weekly-report-w46-zh-cn-{de,es,fr,it,ja,ko,nl,pt,ru}-build`: `content12.py`
  and `content56.py` in each (keys + note letters). Post-fix hash diff: exactly
  these 20 files changed; grep confirms no old key list
  `["c","b","d","a"]` / `["c","d","b","a"]` remains in any build dir.
  Scripts: `apply_fixes.py` / `apply_fixes.log` (first run's regex missed the
  space in `, c` and its assertion fired before any write — nothing was
  partially changed; regex fixed, rerun applied all 20 files).
- **All 9 transform maps** — `hidden_files/w46/maps/{de,es,fr,it,ja,ko,nl,pt,ru}.json`:
  exactly 5 note key/value pairs re-lettered per map (282 keys preserved;
  fr 275). Required for rebuild-from-core reproducibility: `transform.py`
  exits 1 if any map key is missing, and the old English note strings no longer
  occur after the core fix. Script: `apply_map_fixes.py` / `apply_map_fixes.log`.
- **Reproducibility test (passed, 2026-11-03, in `/tmp/fixkeys-repro`):** copy of
  the fixed core build + updated `maps/es.json` via `transform.py` →
  "transform OK: 282 keys", match_set blocks byte-identical to the fixed ES
  build dir.
- **Snapshots:** `pre-fix-edition-hashes.txt` (210 files), `pre-fix-build-hashes.txt`,
  `textmd-before/` (all 10 `.text.md` copies), `/tmp/maps-backup-fixkeys/` (maps copy).

## 4. Full 150-key verification (mandatory — this defect class is p8-blind)

Static AST dump of the core registry, no import, build order
content12 → content34 → content56 → content7 → content8: 130 `ex` + 5
`match_set` = 150 keys. Script: `dump_registry.py`; dumps
`registry-dump-pre-fix.txt` / `registry-dump-post-fix.txt` — their diff is
exactly the 5 corrected keys + 5 note trailing letters. Full log:
`key-verification-log.md`. Levels re-derived: A2 56 / B1 69 / B2 25.
Per-page: 10/18/18/18/18/18/12/38. Arithmetic recomputed: 260+90=350;
350−60=290. Writing model: 164 characters.

**Result: pre-fix 5 wrong (25, 26, 27, 99, 100). Post-fix 0 wrong. The other
145 keys match the Round 2 proofreader's read.**

### Matching sets (option-by-option)

- **P2 25–28 — D3, CORRECTED.** See §1. Post-fix keys `["d","c","b","a"]`.
- **P3 43–46 — correct, unchanged.** Rights: a. 自己救自己，先保护自己
  (= 自救); b. 火警电话119，防火的事 (= 消防); c. 大家按逃生路线离开
  (= 疏散); d. 楼里的走道，逃生路要通 (= 楼道). Keys 43.b / 44.c / 45.a /
  46.d. CONFIRMED.
- **P4 61–64 — correct, unchanged.** Rights: a. 最后一场比赛，决定冠军
  (= 总决赛); b. 输一场就回家的赛制 (= 单败); c. 同一个赛区的两支队打
  (= 内战); d. 按胜负分组打的比赛 (= 瑞士轮). Keys 61.d / 62.c / 63.b /
  64.a. CONFIRMED.
- **P5 79–82 — correct, unchanged.** Rights: a. 办活动的地方，美术馆、图书馆
  (= 场馆); b. 听人讲，学东西的活动 (= 讲座); c. 把老电影修好，画面更清楚
  (= 修复); d. 老电影再上映一次 (= 重映). Keys 79.d / 80.c / 81.b / 82.a.
  CONFIRMED.
- **P6 97–100 — D4, CORRECTED.** See §2. Post-fix keys `["c","d","a","b"]`.

### Non-matching keys (stem/option/fact check, in order)

- 1–6 (P1 fills): 10 / 三 / 11 / 消防 / 15 / 13. CONFIRMED.
- 7–10 (P1 choose): A Nov 10 / B Nov 9 / C 三波 / A 凌晨3点. CONFIRMED.
- 11–15 (P2 choose): A Nov 10 / B Nov 13 / A Nov 11 / A Nov 4–7 / B 取件码. CONFIRMED.
- 16–20 (P2 fills): 包裹 / 取件码 / 供暖 / 高潮场 / 卖家. CONFIRMED.
- 21–24 (P2 arithmetic): 260 / 350 / 290 / 60. Recomputed. CONFIRMED.
- 29–33 (P3 choose): A 第35个 / B Nov 9 / A 先离开再求救 / B Nov 14 / A 逃生路一直通着. CONFIRMED.
- 34–42 (P3 fills): 消防 / 119 / 楼梯 / 疏散 / 古籍 / 35 / 9 / 14 / 1. CONFIRMED.
- 47–51 (P4 choose): A Swiss ended Nov 1 / A 三支 LPL teams in QF / B HLE / B 06:00 / B Nov 15 03:00. CONFIRMED.
- 52–60 (P4 fills): 八强 / 内战 / 单败 / 出炉 / 半夜 / 3 / 6 / 0 / 4. CONFIRMED.
- 65–69 (P5 choose): A pianist never left the ship / B Nov 13 / A 1998 / B Nov 1 / B Nov 14. CONFIRMED.
- 70–78 (P5 fills): 重映 / 修复 / 选择 / 讲座 / 场馆 / 1998 / 9.3 / 190 / 7. CONFIRMED.
- 83–87 (P6 choose): A 三波 / A Oct 20–21 / B Nov 11 / B 35% / B 先打开看一看. CONFIRMED.
- 88–96 (P6 fills): 三波 / 前置 / 末端 / 排队 / 预报 / 1.5 / 2.5 / 3.5 / 20. CONFIRMED.
- 101–112 (P7): 101 个 / 102 A / 103 消防 / 104 A / 105 B / 106 早上 / 107 A /
  108 周一 / 109 C / 110 数据 / 111 B / 112 预报. CONFIRMED (see the ex. 101
  stem flag in §8 — the KEY is correct).
- 113–120 (P8 T/F): A / B / B / B / A / B / A / B. CONFIRMED.
- 121–130 (P8 quiz): B Nov 10 / A 119 / B Oct 20–21 / C Nov 4 / B Nov 6 / A 9.3 /
  B Nov 14 / A 1.5× / A 35% / B Nov 15 03:00. CONFIRMED.
- 131–140 (P8 fills): 消防 / 包裹 / 取件码 / 高潮场 / 重映 / 修复 / 预报 / 供暖 /
  疏散 / 前置. CONFIRMED.
- 141–146 (P8 Xiao Lin passage): A 深圳 / A 消防演练 / B 书 / B 妈妈 /
  A drill → parcel → culture centre / 深圳. CONFIRMED.
- 147–149 (P8 conversation cloze): A 取件码 / A 楼梯 / A 数据. CONFIRMED.
- 150 (writing): open task, model answer 164 characters. CONFIRMED.

## 5. Re-render

Full re-render of all 10 editions from source (render driver logs
`render-{en,de,es,fr,it,ja,ko,nl,pt,ru}-run.log`; resume log
`render_resume.log` for ko webpdf/textmd + nl/pt/ru after the first exec
session dropped mid-KO-webpdf — the KO run/render had already completed and
the old KO web PDF was intact, no partial overwrite). Every driver log:
TOTAL 150, levels A2 56 / B1 69 / B2 25, per-page 10/18/18/18/18/18/12/38,
writing model 164, **zero** FLOW OVERFLOW / HEAD TOO WIDE.

`.text.md` regenerated from the source manuscript in every edition; diff vs the
pre-fix copies is exactly 5 changed lines per edition (core lines 463, 465,
467, 1353, 1355; 10 `<`/`>` lines each), headers preserved verbatim.

**Change footprint vs the pre-fix snapshot** (`pre-fix-edition-hashes.txt` vs
`post-fix-edition-hashes.txt`, 210 files, none added/removed): exactly **5 files
per edition** changed — `.text.md`, print PDF, web PDF, `svg/p8-ceyan.svg`,
`cards/p8-ceyan.png`. P2/P6 SVGs and cards are byte-identical because matching
keys print only on P8; ABSTRACT.txt unchanged in all editions.

## 6. Re-gate results (final artifacts, all 10 editions)

Gate scripts: `run_gates.sh` + `run_gates2.sh` (+ `measure_gates.py`).
Evidence: `gates/` (summary.txt, summary-part2.txt, per-edition occlusion /
freeze / p8 JSON+logs, `counts-phrases-chart.json`, `kinsoku.log`,
`p8-corrected-keys.txt`, `pdf-checks.txt`, pdftotext extracts, rowcheck logs,
`freeze-baseline.json`/`.log`).

| Gate | Result (every edition) |
|---|---|
| Occlusion audit (`occlusion_audit.py`, selftest OK) | 0 flags, exit 0 |
| Freeze (`freeze.py --strict-cjk`) | Added CJK 0 every page for en/de/es/fr/it/nl/pt/ru (exit 0). JA total added 4908 (per-page 398/477/306/342/283/397/783/1922), KO total added 4304 (362/420/269/279/246/344/664/1720) with KO Hanzi-added 0 — identical to the Round 1 adjudicated figures; the `--strict-cjk` exit 1 for JA/KO is the expected CJK-script-layer behaviour, not a freeze failure. Core CJK totals per page unchanged: 932/968/877/787/901/1019/741/1084. RU P8 edition total 1064 vs 1063 in the other Latin editions is pre-existing (1 more retained core CJK char; added = 0, and key letters are ASCII, so this fix cannot change CJK counts). |
| p8.py extract + compare | 150/150 noted, CLEAN, keydiff `[]`, exit 0 |
| Corrected keys in native P8 rendering | 25.d / 26.c / 27.b / 99.a / 100.b in all 10, key and note trailing letter consistent (fragments in `gates/p8-corrected-keys.txt`) |
| Rowcheck §1 (same-baseline collisions) | CLEAN, all 8 pages × 10. §2 crash on hardcoded `p6-verdieping.svg` is the known N/A (identical to Rounds 1–2). |
| Counts | 150; A2 56 / B1 69 / B2 25; per-page 10/18/18/18/18/18/12/38 |
| P7 phrases | All 8 phrases ×2, unchanged |
| P6 chart | Rects exactly (325,1274,220,30,#3e4c2a), (325,1324,330,30,#b3a06a), (325,1374,550,30,#b3a06a), (325,1424,770,30,#b3a06a) |
| Kinsoku | 0 flags, all editions |
| Web PDFs | 8 pages, ≤ 7 MB, pdftotext bytes > 0 and byte-identical web vs print (see §7) |
| Freeze baseline (core) | Exit 0, 8/8 SHA-identical; shipped core SVGs unchanged by the run |
| Visual | P1 + P2 + P6 + P8 at full frame in all 10 editions (40 cards), zero defects; corrected keys read directly off every P8 |

## 7. Final per-edition file inventory

Text-layer bytes are `pdftotext` output bytes (identical web vs print in every
edition). Print PDFs are 8 pages each; web PDFs are 8 pages each.

| Edition | `.text.md` bytes | Web PDF bytes | pdftotext bytes | Print PDF bytes |
|---|---|---:|---:|---:|---:|
| en (core) | 41,894 | 2,390,819 | 45,077 | 36,740,408 |
| de | 43,172 | 2,512,304 | 46,148 | 41,752,795 |
| es | 42,763 | 2,497,485 | 45,801 | 42,127,052 |
| fr | 44,196 | 2,405,806 | 47,170 | 38,266,462 |
| it | 42,854 | 2,420,621 | 45,878 | 39,035,701 |
| ja | 44,074 | 2,730,430 | 47,271 | 33,921,298 |
| ko | 43,881 | 2,526,539 | 46,858 | 32,301,884 |
| nl | 42,177 | 2,484,971 | 45,191 | 40,971,321 |
| pt | 42,561 | 2,450,699 | 45,683 | 39,429,625 |
| ru | 51,680 | 2,275,738 | 55,440 | 30,430,915 |

pdftotext byte counts match the Round 1 KIT figures exactly in every edition.
ES web PDF is 2,497,485 bytes (Round 2: 2,497,482) with identical 45,801
text bytes — the +3 bytes are PDF container churn from the re-render, not
content.

## 8. ES `p.` fix survival + flagged-but-unchanged item

**ES D1 fix survived the re-render.** `.text.md` lines 623
(`Responde con fechas y números de la p. 3.`) and 1063
(`... la p. 5.`); 0 occurrences of the old instruction
`Responde con fechas y números de la página`; build sources unchanged at
`content34.py:96` / `content56.py:91`. The Spanish instruction strings were
not touched by this fix (benign `de la página N` strings elsewhere, e.g.
`Lee el calendario de la página 4.`, remain as authored).

**Flagged, NOT changed:** ex. 101 stem reads 「我拿了一个___包裹。」 with key 个.
The key is the correct measure word for 包裹 (P7 glossline: 一个包裹), but the
stem already contains 一个 before the blank — a pre-existing stem awkwardness
that the Round 2 proofreader passed. Left untouched per the fix-only-D3/D4
scope; for the Round 3 proofreader / coordinator to decide. No other
unapplied fix: **nothing specified in the task could not be applied.**

## 9. Records

- Fix record appended to all 10 KITs (`WEEKLY-KIT.md` in each edition dir;
  ES as Fix 2 after its Fix 1 D1 record; the other 9 replace their
  "None yet" post-proof section). No other KIT content altered.
- This report: `hidden_files/w46/zh-cn-fix-keys/FIX-REPORT.md`.
- Evidence under `hidden_files/w46/zh-cn-fix-keys/`: fix scripts + logs,
  registry dumps, key verification log, render logs, gate JSONs/logs,
  pre/post hash snapshots, `textmd-before/` copies.
