# 独立复校记录（re-proof）— 2026-W47 nl-de（fix1 版）

- 复校员：独立复校员（与 fix1 修复员、delta 重建者、proof1 均不同人）
- 复校对象：`production/2026-w47/2026-w47-nl-de/`（荷兰语目标语 × 德语读者母语）
- 核心对照：`production/2026-w47/core-nl/`（fix5 已定稿）
- 依据：仓库根 `SOP.md` §1.1、§8（全量复校 §8.4），以及任务书；`hidden_files/w47/briefs/brief-coordinator.md`
  在给定路径不存在（全仓 `find` 无此文件），复校按 SOP + 任务书执行，不构成阻塞。
- 工作区（独占新目录）：`hidden_files/w47/scratch-reproof-nl-de1/`；脚本、日志、渲染件全在其中，
  未写任何他人 scratch，未改任何生产文件，未 commit、未 push。

## 0. 开工核对（三 SHA）

| 交付物 | 盘上 SHA-256（开工实测） | 任务书先验值 | 字节 | 结论 |
|---|---|---|---|---|
| 印 PDF `De-Lucerna-VOL4-nl-de.pdf` | `4eacaa18f98f4e8ebdba3608da8e0ec0441f70d94533fdf8efa9234daf0188bb` | 相同 | 12,669,892 | ✓ |
| 网 PDF `De-Lucerna-VOL4-nl-de-web.pdf` | `aba38eecd9e18499438a5f32e6f6469c3aa590ef9ed5420061f5b6bd76730953` | 相同 | 1,617,817 | ✓ |
| 文 `2026-w47-nl-de.text.md` | `c1342c3fe20d7a26df33d604285a9a1fc746ea8ae1c62ef1c66e6211dd908aeb` | 相同 | 46,226 | ✓ |

开工探针：`echo test | git hash-object -w --stdin` 成功（`9daeafb9…`），scratch 内真实写文件成功。
收工三 SHA 与开工完全一致（见 §7）。

## 结论：(a) 零缺陷

本轮全量复校（SOP §8.4）**零缺陷**。fix1 声称的全部修复与存活项逐项独立重测，全部属实；
150 题逐题手验 key–题干配对全部通过；全部机械门自跑通过。无 (b) 缺陷清单。

一项**观察**（非缺陷、不阻塞，见 §6）：Q139 题干与键的时态不对称，属核心原文固有、
本版与核心逐字节一致，超出本版复校范围，留待核心下一轮处理。

## 1. D12（fix1 唯一缺陷）— 已修复，复活路径 0

- 源码：`content8.py:75` 键 `Ik maak een surprise met een kort gedicht.` 未动；
  `content8.py:76` 题干现为 `Ich mache eine Surprise mit einem kurzen Gedicht. → ___`（`kurzen` 在位）。
- `text.md:415`：`140. [B2 · übersetzen] Ich mache eine Surprise mit einem kurzen Gedicht. → ___ — Antwort: Ik maak een surprise met een kort gedicht.（surprise ist eine feste Wendung） [Ins Niederländische übersetzen]`。
- 旧句 `einem Gedicht`（无 kurzen）：全版 `.py` / `.md` / `.svg` 检索 0 处。
- `+7 B` 自洽：补入 `kurzen `（含尾空格）恰为 7 字节。
- 键 `kort` 正确（核心中文题干「带小诗」+ text.md P2 `kort is ook goed` 均要求它），错在德语题干丢「小」，
  属 fan-out 翻译层遗漏——裁定不变，不重开。
- 渲染目检（交付印 PDF 第 8 页 200 dpi 裁图 `crop-p8-q140.png`）：题干单行，行末 SVG x≈1351.3（PIL 实测）
  / 1351.5（光栅实测），栏右界 1411.5，余量 ≈60px，无溢出、无折行。
- 修复封闭性：`content8.py` 全文件唯一 `p.save()` 目标是 `p8-toets.svg`（:147），其余 7 页由
  content12/34/56/7 生成，不受 content8.py 影响；p8 SVG 现哈希 `83c3cc7aa0a5…` 与声称的 fix1 值一致，
  其余 7 页自源码重建 8/8 字节一致（见 §2）。

## 2. D11（P4 HET PROGRAMMA 盒）— 存活，在位

- 盒：P4 SVG `rect x=1439.5 y=591.6 w=422.5 h=638.0`，盒底 1229.60。
- SVG 量测：盒内末基线 y=1209.49（末行 `18:45 uur.`），余量 **+20.11**；盒底下方 40px 带内无文本基线。
- 交付印 PDF 200 dpi 光栅双量测（`render-p4-print.png`）：盒底下方 7px 带（SVG y 1229.6–1236.6）
  真墨像素（灰度 <200）= **0**，带内最小灰度 241（= 盒底色 `#f0eee5`）；带内对照区（盒内末行区域）
  真墨像素 2000，探针有效。裁图 `crop-p4-programma.png` 目视末行在框内有余量。
- P3 SINTERKLAAS IN CIJFERS 盒未动：本版与核心逐项一致——12 条文本、末基线同为 1090.40、盒底同为
  1106.60、余量同为 16.20、末行同为 `november.`。

## 3. 其余声称存活 — 全部复核属实

- D9 keydiff：`tools/p8.py compare` 得 `[137, 138]`，140 已不在 diff 中（见 §2 机械门）。
  137/138 为翻译题键按读者语重定向（德语句 vs 核心中文句），双向翻译均正确（§5）。
- 150 键三源复核：text.md 键与核心键 147/150 逐字节一致；差异仅 137、138（读者语重定向）与
  Q150（开放写作例外）；本版 text.md 键与本版 P8 印键 0 不符（Q150 除外，P8 印 `✓`）。
- freeze core 8/8 + 本版 8/8（见 GATE-LOG）；occlusion 0；p8 extract 150/150、compare CLEAN；
  印/网文字层逐页一致；P8 最小字号 10.12pt（≥ SOP §1.1 底线 9.75pt，印/网同值）。

## 4. 全量复校（SOP §8.4）

1. **全量 proofread**：150 题逐题手验（§5）+ 8 版逐版看图（渲染 `view-p1.png`…`view-p8.png`，
   交付印 PDF 110 dpi）。溢出、重叠、压页脚、图片与出处均无异常；刊头、页眉/页脚、VOL.4、日期
   `WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026`、页码 `Seite N von 8` 齐全。
2. **全部答案逐题复核**：见 §5；编号 1–150 连续无缺重（run.py 注册表 + p8 extract 双重确认）；
   图表题 83–87 算术自洽（35+30=65，35+30+20+15=100）；日期/星期与正文一致（11 月 16 日周一、
   11 月 22 日周日、12 月 5 日周六等均与题干相符）；级别徽章与登记表一致。
3. **8 版逐版看图**：见上；另附三张裁图证据（P8-Q140、P4-PROGRAMMA、P6 最紧盒标题）。
4. **循环规则**：本轮零缺陷，无需修复轮次。
5. **机械门**：全部用共享工具自跑，见 GATE-LOG.md；自写脚本仅作补充（盒标题/孤儿/溢出扫描），
   结论与共享工具一致。

## 5. 150 题逐题手验（key–题干配对，三源）

方法：解析本版 text.md 与核心 text.md 各 150 条（题干 + 键），并取两版 P8 SVG 印键
（`tools/p8.py extract`）三方对齐；逐题核对题干⇄键的语义配对（不只比三源一致）。
结果：**150/150 通过**。分项结论：

- Q1–Q6 填空（时间/地点/数字/动词变位）：键与正文一致（20:45、Berlijn、8、15、5、maakte）。
- Q7–Q15 单选：选项键位正确（B/B/C/B/B/B/C/A/B）。
- Q16–Q24 填空：schoen / wortel / verlanglijstje / gedicht / 5 / Ozosnel / 19（11 月 16 日→12 月 5 日
  = 19 天）/ 18:00 / december，均与正文一致。
- Q25–Q28 配对：d/c/a/b，与 P2 词卡选项逐项对应（schoen→d，wortel→c，verlanglijstje→a，gedicht→b）。
- Q29–Q33 单选：B/B/C/A/B，与 P3 正一致（Grave、12:00、10:15、88e、bibliotheek）。
- Q34–Q38 填空：vestingstad / ontving / sleutel / editie / leeskring。
- Q39–Q42 完成时：is aangekomen / heeft ontvangen / is gevaren / hebben gelezen（zijn/hebben 助动词正确）。
- Q43–Q46 数字：1（14→15 日）/ 4（12:00–16:00）/ 19 / 17（2026−2009）。
- Q47–Q51 单选：C/B/B/B/B（16 november、8 punten、Griekenland、21 en 22 november、Cambuur）。
- Q52–Q56 填空：groepswinst / kwartfinales / ongeslagen / stand / interland。
- Q57–Q60 过去时：speelde / won / verloor / speelden（单复数一致）。
- Q61–Q64 正误：Waar / Niet waar（Servië 0 分非 8 分）/ Niet waar（PSV 榜首非榜尾）/ Waar
  （Heerenveen 5–3 胜 Feyenoord，与正文“werd het 5–3 bij Heerenveen – Feyenoord”一致）。
- Q65–Q69 单选：B/A/C/B/A（20:00、19、Maleisië、34、een gedicht）。
- Q70–Q75 填空：surprise / verslaggever / proef / gedicht / aflevering / kandidaten。
- Q76–Q79 将来时（gaan + 不定式）：gaat winnen / gaan kijken / gaat maken / gaan schrijven（单复数一致）。
- Q80–Q82 正误：Waar（11 月 1 日开播）/ Niet waar（Maleisië 非西班牙）/ Niet waar（四行足够，
  “至少二十行”为假）。
- Q83–Q87 图表读数：35 / 30 / 65 / 15 / 100，与 P6 柱状图（35/30/20/15）逐项相符。
- Q88–Q92 单选：B/B/C/A/B（verlanglijstje、verstopt in iets geks、18:00、mensen haar blijven vieren、
  vorige week woensdag）。
- Q93–Q96 填空：verlanglijstje / surprise / gedicht / verandert。
- Q97–Q100 造句：Sinterklaas is een oud feest in Nederland. / De kinderen zetten hun schoen bij de deur. /
  Een traditie leeft als mensen haar blijven vieren. / Het feest verandert, maar het verdwijnt niet.
  （词序、大小写、标点均正确。）
- Q101–Q104：wedstrijd / groepswinst / B（de eerste plaats in de groep）/ scoorde。
- Q105–Q108：won / verloor / speelde / B（winnen；«Won» 为 winnen 的过去时）。
- Q109–Q112：omdat / B（een reden；omdat 从句表原因，非疑问非命令）/ wil / maakte。
- Q113–Q120 完形单选：B/B/A/B/B/B/B/B（Berlijn、8、7、december、18:00、RTL 4、gedicht、de eerste plaats）。
- Q121–Q128 单选：A/B/B/A/B/B/B/C（18:00、de Maas、88e、2009、Griekenland、26、
  mensen haar blijven vieren、21 en 22 november）。
- Q129–Q132 阅读理解（Daan，P8 C 节短文）：B（Rotterdam）/ B（Duitsland – Nederland）/
  B（een wortel en een verlanglijstje）/ B（18:00），与短文逐句相符。
- Q133–Q136 造句：Het Sinterklaasjournaal begint om 18:00 uur. / Wij zetten onze schoen bij de deur. /
  Oranje speelt maandag in Berlijn. / Ik zet mijn schoen met een wortel.（词序正确。）
- Q137–Q140 翻译：137 荷→德 `Das Sinterklaasjournaal läuft jeden Tag um 18:00 Uhr.`（电视节目用 laufen，
  地道）；138 荷→德 `Die ersten beiden ziehen ins Viertelfinale ein.` 正确；139 德→荷
  `De intocht in Amsterdam was de 88e editie.` 为正文原句（见 §6 观察）；140 德→荷
  `Ik maak een surprise met een kort gedicht.` 正确（kurzen=kort，D12 已修）。
- Q141–Q144 配对：b/c/d/a，与 P8 选项逐项对应（journaal→b，groepswinst→c，schoen→d，gedicht→a）。
- Q145–Q149 对话完形：A/A/A/B/A（schoen、wortel、verlanglijstje、cadeautje、18:00），对话逻辑连贯。
- Q150 开放写作：范文逐词数 81 词（`Tekstmodel:` 起，含 `–` 分词符按空白分词计 81），在 80–100 词
  任务区间内；P8 印 `✓`（开放题例外）。

## 6. 观察（非缺陷，不阻塞）

- **Q139 时态不对称（核心固有，本版忠实继承）**：德语题干现在时 `Der Einzug in Amsterdam ist die 88. Ausgabe.`
  对荷兰语键过去时 `De intocht in Amsterdam was de 88e editie.`。该键与核心键逐字节一致，且为 P3
  正文原句（`Het was de 88e editie van de Amsterdamse intocht.`）。不对称在核心已定稿（fix5）中即存在，
  本版 fan-out 未引入、也无权单方面改核心键。记为观察，留待核心下一轮裁定；不计入本版缺陷，
  不影响本版 (a) 结论。

## 7. 生产零写入核对

- 开工快照 `opening-snapshot.sha256`（85 个生产文件，`production/2026-w47/2026-w47-nl-de/` +
  `production/2026-w47/core-nl/`，`__pycache__` 除外）与收工快照 `closing-snapshot.sha256` 逐项比对：
  **全部一致，零写入**。
- 三交付物 SHA 收工复测与开工相同（印 `4eacaa18…`、网 `aba38eec…`、文 `c1342c3f…`）。
- run.py 直接重建在 scratch 副本（`run-copy/`）内执行，事前验明 OUT 指向 scratch 内绝对路径
  （`…/scratch-reproof-nl-de1/run-copy/svg`）；freeze 工具在自带守卫下于 scratch 内重建，
  两次均验明生产 SVG 哈希在跑前跑后不变。
- 未 commit、未 push、未改生产文件。工作树中 `core-nl` 的 M 标记为开工前已存在状态，与本轮无关。
