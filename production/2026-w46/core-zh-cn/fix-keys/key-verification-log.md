# Full 150-key verification log — W46 zh-cn core (fix worker, post-fix registry)

Source: static AST dump of the core build registry (`dump_registry.py`,
no import, build order content12 → content34 → content56 → content7 →
content8). Pre-fix dump: `registry-dump-pre-fix.txt`; post-fix dump:
`registry-dump-post-fix.txt` — the diff between the two dumps is exactly
the 5 corrected keys + their 5 note trailing letters (25–27, 99–100).
Levels re-derived from the dump: A2 56 / B1 69 / B2 25. Per-page:
10/18/18/18/18/18/12/38. Arithmetic recomputed: 260 + 90 = 350;
350 − 60 = 290.

## Matching sets (option-by-option; rights lettered a–d in list order)

### P2 D 25–28 — D3, WRONG pre-fix, CORRECTED
Lefts: 高潮场 / 包裹 / 取件码 / 供暖.
Rights: a. 北方冬天家里暖和，靠它 (= 供暖 — heating keeps a northern
home warm in winter); b. 打开快递柜要用的号码 (= 取件码 — the code
needed to open a parcel locker); c. 买的东西，装在里面送来 (= 包裹 —
the thing bought, packed inside and delivered); d. 双11最忙的卖货时间
(= 高潮场 — the busiest selling period of Double 11).
Derivation: 25 高潮场 → d; 26 包裹 → c; 27 取件码 → b; 28 供暖 → a.
Pre-fix keys ["c","b","d","a"] gave 25.c (包裹's definition), 26.b
(取件码's), 27.d (高潮场's) — a rotation of the first three. 28.a was
already correct. Post-fix keys ["d","c","b","a"] + note letters d/c/b/a.

### P3 D 43–46 — correct, unchanged
Rights: a. 自己救自己，先保护自己 (= 自救); b. 火警电话119，防火的事
(= 消防); c. 大家按逃生路线离开 (= 疏散); d. 楼里的走道，逃生路要通
(= 楼道). Keys 43.b / 44.c / 45.a / 46.d — all match. CONFIRMED.

### P4 D 61–64 — correct, unchanged
Rights: a. 最后一场比赛，决定冠军 (= 总决赛); b. 输一场就回家的赛制
(= 单败); c. 同一个赛区的两支队打 (= 内战); d. 按胜负分组打的比赛
(= 瑞士轮). Keys 61.d / 62.c / 63.b / 64.a — all match. CONFIRMED.

### P5 D 79–82 — correct, unchanged
Rights: a. 办活动的地方，美术馆、图书馆 (= 场馆); b. 听人讲，学东西
的活动 (= 讲座); c. 把老电影修好，画面更清楚 (= 修复); d. 老电影再
上映一次 (= 重映). Keys 79.d / 80.c / 81.b / 82.a — all match. CONFIRMED.

### P6 D 97–100 — D4, WRONG pre-fix (99, 100), CORRECTED
Lefts: 说法 / 数据 / 预报 / 前置.
Rights: a. 还没发生的事，先猜一猜 (= 预报 — a forecast guesses what
has not happened yet); b. 提前放到离买家近的地方 (= 前置 — placed in
advance near the buyer; cf. P6 article: 付定金的时候，包裹就先送到离你
近的地方); c. 别人说的话，不一定是真的 (= 说法 — a claim, what someone
says, not necessarily true); d. 量出来的数字 (= 数据 — measured numbers).
Derivation: 97 说法 → c; 98 数据 → d; 99 预报 → a; 100 前置 → b.
Pre-fix keys ["c","d","b","a"] gave 99.b (前置's definition) and 100.a
(预报's) — the two swapped. 97.c / 98.d were already correct. Post-fix
keys ["c","d","a","b"] + note letters c/d/a/b.

## Non-matching keys (stem/option/fact check, in order)

- 1–6 (P1 fills): 10 (Nov 10 peak sale 20:00) / 三 (three waves) / 11
  (Nov 11) / 消防 (Nov 9 National Fire Day) / 15 (final Nov 15, 03:00) /
  13 (spot sales to Nov 13). All match stems + KIT fact sources. CONFIRMED.
- 7–10 (P1 choose): A Nov 10 / B Nov 9 / C 三波 / A 凌晨3点. CONFIRMED.
- 11–15 (P2 choose): A Nov 10 / B Nov 13 / A Nov 11 (third wave) /
  A Nov 4–7 (cold air) / B 取件码. CONFIRMED.
- 16–20 (P2 fills): 包裹 / 取件码 / 供暖 / 高潮场 / 卖家. Each word
  is the only word that completes its sentence. CONFIRMED.
- 21–24 (P2 arithmetic): 260 / 350 (= 260+90) / 290 (= 350−60) / 60.
  Recomputed. CONFIRMED.
- 29–33 (P3 choose): A 第35个 / B Nov 9 / A 先离开再求救 / B Nov 14
  culture night / A 逃生路一直通着. CONFIRMED.
- 34–42 (P3 fills): 消防 / 119 / 楼梯 / 疏散 / 古籍 / 35 / 9 / 14 / 1
  (Reading Month from Nov 1). CONFIRMED.
- 47–51 (P4 choose): A Swiss ended Nov 1 / A 三支 LPL teams in QF
  (TES, IG, BLG; AL out) / B HLE (BLG beat HLE 2–0) / B 06:00 /
  B Nov 15 03:00 final. CONFIRMED.
- 52–60 (P4 fills): 八强 / 内战 / 单败 / 出炉 / 半夜 / 3 (GEN, DK
  3–0) / 6 (06:00) / 0 (AL 0–3) / 4 (TES–IG Nov 4). CONFIRMED.
- 65–69 (P5 choose): A pianist who never left the ship / B Nov 13
  re-release / A 1998 / B Nov 1 Reading Month opening / B Nov 14 culture
  night. CONFIRMED.
- 70–78 (P5 fills): 重映 / 修复 / 选择 / 讲座 / 场馆 / 1998 / 9.3 /
  190 (1.9m+ ratings → 190多万) / 7 venues. CONFIRMED.
- 83–87 (P6 choose): A 三波 / A Oct 20–21 first wave / B Nov 11 biggest
  / B 35% front-loaded / B 先打开看一看. CONFIRMED.
- 88–96 (P6 fills): 三波 / 前置 / 末端 / 排队 / 预报 / 1.5 / 2.5 /
  3.5 (chart drawn at the middle of 3–4) / 20 (%). CONFIRMED.
- 101–112 (P7): 101 个 (measure word for 包裹 — see stem note below) /
  102 A 高潮场 = busiest selling time / 103 消防 / 104 A 一个包裹 /
  105 B 半夜3点 / 106 早上 / 107 A big→small date order /
  108 周一 (= 星期一) / 109 C 「最大的一波」 is a 说法 (claim) /
  110 数据 / 111 B data + checkout page first / 112 预报. CONFIRMED
  (key 101: the KEY is the correct measure word; the stem as authored
  reads 「我拿了一个___包裹。」, i.e. the stem already contains 一个
  before the blank — a pre-existing stem awkwardness, NOT a key error.
  Left untouched: the Round 2 proofreader passed it, and this fix is
  scoped to D3/D4 only. Flagged here for the Round 3 proofreader /
  coordinator; no change made.)
- 113–120 (P8 T/F): A (Nov 9 true) / B (35th, not 34th) / B (three
  waves, not one) / B (AL did not reach QF) / A (06:00 true) /
  B (1998, not 2019) / A (Nov 13 true) / B (Nov 1, not Nov 9).
  Matches the Round 1/2 spot check (113–125). CONFIRMED.
- 121–130 (P8 quiz): B Nov 10 / A 119 / B Oct 20–21 / C Nov 4 /
  B Nov 6 (DK–BLG) / A 9.3 / B Nov 14 / A 1.5× / A 35% / B Nov 15
  03:00. CONFIRMED.
- 131–140 (P8 fills): 消防 / 包裹 / 取件码 / 高潮场 / 重映 / 修复 /
  预报 / 供暖 / 疏散 / 前置. Each completes its sentence; identical
  words already verified above. CONFIRMED.
- 141–146 (P8 read-and-answer, Xiao Lin passage): A 深圳 / A 消防演练 /
  B 书 / B 妈妈 / A order drill → parcel → culture centre (passage
  order Nov 9 / Nov 11 / Nov 14) / 深圳. CONFIRMED.
- 147–149 (P8 conversation cloze): A 取件码 / A 楼梯 / A 数据.
  CONFIRMED.
- 150 (writing): open task, model answer 164 characters (recounted by
  the builder; Round 2 proofreader recounted exactly 164). No single
  key. CONFIRMED.

## Result

150/150 keys verified against stems, options, matching definitions,
articles and KIT facts. Pre-fix: 5 wrong (25, 26, 27, 99, 100).
Post-fix: 0 wrong. The other 145 match the Round 2 proofreader's read.
