# PROOF-NOTE — 2026-W47 · nl → de（荷兰语目标语 × 德语读者）· proof1 独立复校（delta 重建版）

- 版：`2026-w47-nl-de`，VOL.4，8 页，150 题（A2 46 / B1 73 / B2 31；分页面 10/18/18/18/18/18/12/38）
- 复校员：独立校对员 proof1（与 delta 重建者不同人）· 2026-11-11
- 复校对象：delta 重建版（core-nl fix3 + fix4 + fix5 同步，build 7），规范路径 `production/2026-w47/2026-w47-nl-de/`
- 依据：core-nl `FIX-LOG.md`（fix3 第 412 行起、fix4 第 185 行起、fix5 第 3 行起，全文已读）、delta `DELTA-LOG.md`（全文已读）、仓库根 `SOP.md`（proofread-until-zero；几何遮挡扫描必过；p8 compare 必跑）
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-de1-delta/`（本轮专用；任务所称的 `scratch-proof-nl-de1` 在开工前已存在——上一轮 proof1（11:30，结论 (b)，D1–D5）的工作区，故本轮另建新目录，旧目录原样保留，只在开工探针时写入了一个 `probe.txt`）
- 原则：只做复校，不改任何生产文件；生产目录零写入——全部重建、重渲染、比对均在自有 scratch 的 `rebuild/` 副本中进行；core-nl 与 staging 只读

## 结论：(b) 有缺陷，不能定稿

全轮只发现 **1 项缺陷（一般）：D12——Q140 德语题干漏译核心词“小”**（见下）。D6、D7、D8、D9、D10、D11 六处 delta 同步点**全部独立验证通过**；150 题 key-vs-stem 逐题手验 150/150 通过（手验本身不含 D12——D12 是题干与 key 的跨源不一致，手验覆盖时发现）；8 页逐页目检通过；16 项机械门全部通过（详见 `GATE-LOG.md`）。

**定稿条件**：D12 一处修完即可——德语题干加一词 `kurzen`（`Ich mache eine Surprise mit einem kurzen Gedicht.`），归 fanout 翻译层（协调员負責），重导 text.md + 重建本版 PDF/SVG 后，对 Q140 做针对性再校（题干行 + text.md:415 + P8 节点三源一致）即可定稿，无需全轮重做（其余 149 题、8 页、全部机械门均已通过且与该改动无关；但按 SOP §8 循环规则，改动后的 Q140 须再校一轮）。

## 三 SHA 实测（开工核对，与任务给定值逐字节一致）

| 文件 | 字节 | SHA-256（实测） |
|---|---|---|
| `De-Lucerna-VOL4-nl-de.pdf`（印） | 12,669,889 | `26faddf46acd8db2ec36999d5734ccff88835a554447b57526db5062f2c244ef` |
| `De-Lucerna-VOL4-nl-de-web.pdf`（网） | 1,617,811 | `74f10eefe797397b8e3e5eacc636208ebba2a73919848a1ad7c698043de97aa0` |
| `2026-w47-nl-de.text.md`（文） | 46,219 | `ac56f6f91c644dc0d9a86c9d6d8748bca2721c507c255efd47ff612f2170117c` |

修前 staging 版三 SHA 与 DELTA-LOG 所记 build-6 值一致（印 `f87d3f4d…341ab59` / 12,669,890 B；网 `44d15508…f3ab6` / 1,617,821 B；文 `7d6eee03…fd873` / 46,214 B）。SVG 哈希 vs 修前：仅 `p4-sport.svg`（D11）与 `p8-toets.svg`（D9）变化，其余 6 个字节一致；`diff -rq` staging vs 规范路径：仅 5 个源文件 + KIT + text.md:415 一行 + 2 个 SVG + 2 张卡片 + 2 个 PDF 不同，无任何计划外改动。

## 缺陷清单

### D12（一般）— Q140 德语题干漏译核心词“小”，题干与 key 不一致

- **位置**：text.md:415 题干、`content8.py` 译题行（P8 印 `140. Ins Niederländische übersetzen / Ich mache eine Surprise mit einem Gedicht. → ___`）；key（registry / text.md:415 答案 / P8 节点）均为 `Ik maak een surprise met een kort gedicht.`
- **实测证据**：
  1. 核心中文题干（core text.md:416）：`我做一个带小诗的伪装礼物。`——含“小”字；核心 key（fix4 定稿）`Ik maak een surprise met een kort gedicht.` 与之一致。
  2. 本版正文 text.md:73：`Twee: schrijf een gedicht — kort is ook goed.`——“kort”在正文中有据。
  3. 本版德语题干：`Ich mache eine Surprise mit einem Gedicht.`——无 `klein` / `kurz`（与核心相比丢了“小”）。
  4. 横向对照其余 8 个 nl fanout 版 Q140 题干：en `a little poem`、es `un poema corto`、fr `un petit poème`、ja `小さな詩`、ko `작은 시`、pt `um poema curto`——6 版保留“小”；只有 de、it（`una poesia`）、ru（`со стихотворением`）丢了它。
- **判定（明确结论，不含糊）**：**key 没有错**——`kort` 是核心题干与正文共同要求的正确答案，delta 按 fix4 同步 key 是对的；**错的是德语题干本身**，属于 fanout 翻译层漏译（把核心的“小”翻丢了），不是 delta 的错，也不是 key 的错。读者只看题干无法推出 `kort`：把 `mit einem Gedicht` 忠实译出得到的是 `met een gedicht`，按 key 会被判错——这道翻译题按印出来的样子是做不对的。严重程度为一般（key 正确、正文有据、只缺一词），但它是不折不扣的题干/key 不一致，按 proofread-until-zero 不能放过。
- **修法与归属**：题干改为 `Ich mache eine Surprise mit einem kurzen Gedicht.`（只加一词），由**协调员 / fanout 翻译层**修（与 fix2 D4 的 marker 本地化同类——都是 fanout 层问题，不在 delta 的 5 个源文件范围内）。修后重导 text.md、重建本版，针对性再校 Q140 三源（题干行 + text.md 答案 + P8 节点）。
- **跨版观察（非本版缺陷，报协调员）**：nl-it、nl-ru 的 Q140 题干同样丢了“小”（且它们的 key 仍是旧的无 `kort` 版——core fix4 未同步到它们，不在本轮复校范围内）。

## D9 裁定（任务要求的明确结论）

**key 正确，德语题干漏译——这是 fanout 翻译层措辞/漏译问题，不是 key 错误。** 证据链见 D12 第 1–4 条。三源一致性本身通过：registry 键 = text.md:415 答案 = P8 节点（y=2236.28），均为 `Ik maak een surprise met een kort gedicht.`；三源比对 149/149 MATCH（Q150 开放写作例外）；p8 keydiff 由修前 [137, 138, 140] 变为 [137, 138]，140 已移出。`content8.py:75` 一行改动正确，注记 `surprise ist eine feste Wendung` 不动亦正确。

## D11 复核结果（真修，验证通过）

- 源码行：`content34.py:130`，顶留 62→89；P3 SINTERKLAAS 盒（同文件约第 37 行，`sh = 62 + … + 64`）未动；P3 SVG 与修前字节一致。
- SVG 实测：盒 `<rect x=1439.5 y=591.6 w=422.5 h=638.0>`，盒底 **1229.6**；末行 `18:45 uur.` 基线 **1209.49**，盒内余量 **+20.11px**（≥20px 门限）；事实句 14 行，断行 3/3/3/2/3，与核心一致；`P4 col3 ends 1229.6`。
- PIL 真墨（4× Newsreader 掩膜，独立重做）：墨底恰在基线（+0.00px），真墨余量 **+20.11px**。
- 交付 PDF 渲染像素（150 dpi，独立重渲染）：墨底 1209.53，真墨余量 **+20.07px**；卡片 PNG：墨底 1209.00，余量 **+20.60px**。三法一致。
- 盒底下 7px 条带：纸灰约 249、奶油灰约 238——以真墨阈值（<200 / <240）计，**0 非纸像素**（<250 的计数全是纸色本身，见 GATE-LOG 注记）。
- 目检：`crop-p4-programma.png`（交付 PDF 渲染裁图）：末行在盒内，下有明显留白。D11 **通过**。

## D6 / D7 / D8 / D10 复核结果（结构同步，验证通过）

- 机制：本版 `bslib4.py:119,155` 的 `Flow.para` / `Flow.bridge` `w=None` 参数与核心 fix3 机制一致（默认 = 列宽，现有调用不受影响）；D8 `content56.py:144,145,157`、D10 `content7.py:92,93,101` 的盒高公式与渲染调用同用新 w 值（与核心 fix4 的写法一致）。
- 逐项：D6 `content34.py:78` w=368.75；D7 `content7.py:19` w=412.25；D8 `content56.py` capcn_w=374.25；D10 `content7.py` dt_zh_w=353.25——四值均在本版 `svglib.wrap()` 独立重扫的实测区间内，且选值落在区间内部（见 GATE-LOG；D7/D10 的 DELTA-LOG 区间端点较我方重扫略窄，属注记 N1，非缺陷）。
- SVG 线行实测（交付版，与修前逐字逐基线相同）：D6 P3 2 行（2303.5 / 2333.225）；D7 P7 3 行（725.66 / 755.385 / 785.11）；D8 P6 图注 4 行（635.02 / 659.44 / 683.86 / 708.28）；D10 P7 来信 2 行（1783.77 / 1812.17）。p3/p6/p7 SVG 与 staging 字节一致，p4/p8 仅含 D11/D9 变化；`P6 chart ends 717`、`P7 col3 ends 1927.5` 与修前一致，零 y 位移。
- 孤儿横扫独立重跑（自写脚本，PIL + svglib 双 advance，1462 行级；另暴力检查）：(a) 独行标点 **0**，(b) 行首标点 **0**，双法 8 页全 0；以标点开头的 `<text>` 元素 **0 个**。
- 裁图目检：`crop-p3-d6.png`、`crop-p7-d7.png`、`crop-p6-d8.png`、`crop-p7-d10.png` 均确认断行与句末标点无误。D6–D10 **全部通过**。

## 150 题 key-vs-stem 逐题手验（`keytable-150.txt`，非仅三源比对）

逐题核对题干、选项、key、注记与正文依据，150/150 通过。要点记录：

- 数字全部可验算：Q22/Q45（16 Nov→5 Dec = 19 天）、Q43（14→15 Nov = 1 天）、Q44（12:00–16:00 = 4 小时）、Q46（2009→2026 = 17 年）、Q83–87 图表数 35/30/65/15/100（35+30+20+15=100）、Q30（12:00 到码头）与 P3 正文一致、Q57（Oranje 1–1 主场对德国）与 P4 正文逐句一致（`1–1 thuis tegen Duitsland, 2–1 uit bij Servië, 2–2 uit bij Griekenland en 2–1 thuis tegen Servië`，8 分 = 2 胜 2 平，与 Q3/Q48 的 8 分自洽）。
- Q49/Q125（德国主场 0–1 负希腊）P4 正文有原句；Q51/Q58（PSV 2–5 胜 Cambuur）、Q59/Q64（Heerenveen 5–3 胜 Feyenoord）、Q63/Q126（PSV 26 分领跑）均在 P4 正文/盒子中有原句——D5 的 26 分事实已在盒内可验。
- Q65–82（Robinson：周日 20:00、RTL 4、19 人、马来西亚、34 天、11 月 1 日开播、四行诗足够）与 P5 正文逐项一致；Q92（Sint-Maarten 上周三）与 P2 正文一致。
- 配对题手验：25–28 = d/c/a/b（schoen→门边、wortel→马食、verlanglijstje→愿望单、gedicht→小诗，均与 P2 选项逐项对上）；141–144 = b/c/d/a（journaal→每日新闻、groepswinst→小组头名、schoen→门边、gedicht→小诗，与 P8 选项逐项对上）。
- Q129–132（Daan：住鹿特丹、周一看德荷大战、鞋里胡萝卜+愿望单、每天 18:00 看 Sinterklaasjournaal）与 text.md:401 Daan 短文逐句一致；Q145–149 对话填空与短文一致。
- Q137/Q138 翻译键逐字核对无误（即 p8-compare keydiff 的两项，按设计与核心中文键不同，非缺陷）。
- Q150 开放写作例外：Tekstmodel 实数 81 词（80–100 范围内，含独立破折号计 81、去破折号计 80），P8 键 `✓`。
- 金句 8/8：text.md 与印 PDF 中逐字一致；星期核对（`date`）：2026-11-01 周日、11-14 周六、11-15 周日、11-16 周一、11-22 周日、11-24 周二、11-29 周日、12-05 周六——与版内星期表述全部一致。
- 引号横扫：ASCII `"` 0、反引号 0、`« »` 35/35、德语 `„ “` 1/1（P1 词中词 gloss，配对正确）。

## 8 页逐页目检（交付印 PDF，200 dpi 渲染 `read-p1..p8.png`）

- P1：干净。旧 proof1 D1 已在 build-6 修复：标题现为 `IN DEZE EDITIE　AUSGABE`（删去 `IN DIESER`），真墨余量 +91.2px（PDF 渲染 +91.0px）。
- P2：干净。D3 回归实测：c 选项 `c. eten voor Sinterklaas' paard` 真墨右缘 1789.5，余量 +72.5px；a +98.5 / b +46.2 / d +56.0。`EN JIJ?` 盒底 7px 条带 0 真墨。
- P3：干净。SINTERKLAAS 盒未动（rect 与 staging 完全相同，盒底 1106.6）；桥接 D6 两行无误。
- P4：干净。HET PROGRAMMA 盒 D11 已验；其余内容与修前一致。
- P5：干净。Robinson 各事实与练习一致；`JONGEREN IN CIJFERS` 盒“距 11 月 22 日还有 13 天到 12 月 5 日”算数正确。
- P6：干净。图表 35/30/20/15 与练习一致；图注 D8 四行无误。注：正文结束后半页留白较大（版式固有，与核心同形，非缺陷）。
- P7：干净。桥接 D7、来信 D10 均无误；8 条金句页码标注逐一核对无误（P1/P1/P2/P3/P4/P5/P6/P6）；`VOLGENDE WEEK` 日期星期全部正确。
- P8：干净。140 题印 `kort gedicht`；141–144 选项与 key 一致；答案区 150 题全印；Tekstmodel 在位。

## 非缺陷注记

- **N1（区间端点小差异）**：我方 0.25px 重扫的 D7 区间为 394.25–450.00（DELTA-LOG 称 394.5–430.0），D10 为 286.75–406.75（称 300.0–406.5）；D6（312.00–425.50）与 D8（358.25–390.00）与称值基本一致（0.25px 步进内）。选值均在区间深处（D7 距下缘 18.0px、距上缘 37.75px；D10 距下缘 66.5px），且 p3/p6/p7 SVG 字节一致是决定性证据——不是缺陷，DELTA-LOG 的端点应为较粗步进或不同收窄口径所致。
- **N2（两种计数口径）**：`gates.py` 日志的 `p8_compare keydiffs=0` 是对 stdout 中 `key diff` 行的计数，权威 JSON 本体 keydiff=[137,138]（翻译题，按设计不同）；我方 span 级印/网比对在 P1 有 1 个位置微差（masthead `De Lucerna` x 394.0 vs 393.8，0.2pt），与核心 fix5 记录的已知字体子集微移同一回事，词级比对 0/0——均非缺陷。
- **N3（D9 注记）**：`surprise ist eine feste Wendung` 不动是正确的——`kort` 由题干“小”与正文 `kort is ook goed` 共同说明，无需改注记。

## 证据文件（本 scratch）

`PROOF-NOTE.md`（本文件）、`GATE-LOG.md`（16 门 + 框标题 clear 表 + D6–D11 逐项）、`keytable-150.txt`（150 题手验表）、`p8-compare-3way.json`（149/149）、`p8-compare.json`（CLEAN）、`orphan-sweep.log`（0/0）、`gates.log` + `gates-de.json`（9/9 ALL PASS）、`occlusion.json`（0 flags）、`freeze-core.log`（8/8）、`textlayer.py` 输出（见 GATE-LOG）、`read-p1..p8.png`（200 dpi 通读渲染）、`crop-p3-d6.png`、`crop-p7-d7.png`、`crop-p6-d8.png`、`crop-p7-d10.png`、`crop-p8-q140.png`、`crop-p4-programma.png`（交付 PDF 渲染）、`crop-p4-programma-card.png`（卡片）、`run.log` / `render.log` / `webpdf.log` / `d11_measure.py` / `width_scan.py` / `boxtitle.log` / `check_s11.log` / `creambox.log` / `spill-sweep.log` / `svg-sha-rebuilt.txt` / `registry-new.json`（自有 rebuild 副本的 registry）。
