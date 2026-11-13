# PROOF-NOTE — 2026-W47 zh-cn × nl · 独立校对 proof1

- 校对员：proof1（独立校对，只复校，不改生产文件，不 commit、不 push）
- 对象：`production/2026-w47/2026-w47-zh-cn-nl/`（fan-out #3，2026-11-11）
- 核心对照：`production/2026-w47/core-zh-cn/`（已定稿，proof3 (a)）
- 工作区：`hidden_files/w47/scratch-proof-zh-cn-nl1/`（独占；脚本、日志、渲染件全在此）
- 结论：**(b) —— 发现 4 处缺陷，需修后按 SOP §8 循环规则整期重渲染、从头再做一轮全量校对。**

## 三 SHA 先验（开工 / 收工两次核对，一致）

| 文件 | SHA-256 | 大小 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-NL.pdf` | `f660072c047e1b5bab5a13956ec871db6976a47ddff49cc855615a8f55b42e4b` | 44,049,080 B |
| 网 PDF `Lucerna-VOL4-NL-web.pdf` | `495594dc8d712268b336c6bcfb39dc0286f45ce20624cb163d02e9f5e9aeefac` | 2,703,048 B |
| 文 `2026-w47-zh-cn-nl.text.md` | `41aa9a39371ab7dc75f828b24bb038f0f1b4f6e2f1a1fbe04cd9513eff09df2c` | 50,082 B |

开工探针：`echo test | git hash-object -w --stdin` 成功 + scratch 内真实写文件成功后才动手。
生产零写入：收工时全版 41 个文件 SHA 与开工快照逐一比对，0 差异；三 SHA 与开工值相同。
注：任务所称 `hidden_files/w47/briefs/brief-coordinator.md` 在仓内不存在，
也没有可找到的 fan-out #3 专项报告文件；#3 报告即本版 `WEEKLY-KIT.md`
“Build history #3”一节，以下按 KIT 所称修复点逐项实测。

## 缺陷清单（4 项，全部为 fan-out 引入；核心对照同位置干净）

### (b1) P5「这一周的高频词 Woorden van de week」标题越出奶油盒右缘 —— 重
- 位置：P5 中栏奶油盒（SVG rect x=538.5..961.0, y=648..816），盒标题
  `这一周的高频词　Woorden van de week`。
- 实测（三重一致）：PIL 真墨扫（`ink_sweep.py`，复用 `tools/occlusion_audit.py`
  的 `parse_svg` 真墨盒）：墨右缘 x=988.25，越盒边 **27.25 px**；
  交付 PDF 文字层：`Woorden van de week` span bbox 右缘 741.9pt，盒边
  720.75pt，越 **21.15pt**；交付 PDF 100dpi 渲染像素：最右墨点 740.2pt，
  越 **19.4pt**。放大裁图 `render/p5-title-zoom.png`：`week` 的 `k`
  完全落在白纸上，盒边从词中穿过。
- 对照：核心同盒最紧余量 +12.50px；核心 P5 该标题为英文短串，无越边。
- 类别：es D-2/D-3 同类（盒标题越边）。#3 KIT 未提及此点——漏检。

### (b2) P2「本周生活小日历 Data van deze week」标题越出奶油盒右缘 —— 轻
- 位置：P2 中右栏奶油盒（rect x=989.0..1411.5, y=200..447），盒标题。
- 实测（三重一致）：PIL 真墨：墨右缘 x=1413.25，越盒边 **1.75 px**；
  交付 PDF 文字层：`Data van deze week` span 右缘 1061.5pt，盒边 1058.6pt，
  越 2.9pt（advance）；交付 PDF 100dpi 渲染像素：最右墨点 1059.8pt，
  越 **1.2pt**。放大裁图 `render/p2-title-zoom.png`：末尾 `k` 贴在盒边外。
- **KIT 的“已修”说法不成立**：KIT 称该标题“ends x = 1413.2, 26.3 px clear”——
  1413.2 恰与我实测墨右缘一致，但 26.3px 是到**照片**（x=1439.5）的距离，
  不是到盒边（1411.5）的距离；以盒边为准，它仍越边 1.75px。
  这正是 de D-1 的前车：报告称“距照片多少 px”不等于盒边。
- 对照：核心同盒最紧余量 +20.25px。

### (b3) P1 截稿线越出日历盒右缘 —— 轻
- 位置：P1 右栏「本周日历」奶油盒（rect x=1439.5..1862.0, y=588..1288）内
  末行 `Sluiting: 10 nov. — de finale nog niet gespeeld`。
- 实测：PIL 真墨：墨右缘 x=1864.5，越盒边 2.5px；交付 PDF 300dpi 渲染像素：
  最右墨点 1397.52pt，盒边 1396.5pt，越 **1.02pt**（100dpi 下为 +0.3pt，
  属量化噪声，故用 300dpi 复测为准）。放大裁图
  `render/p1-sluiting-zoom.png`：`gespeeld` 的末字母 `d` 被盒边从中切过，
  右半落在白纸上。
- 对照：核心同盒最紧余量 +10.25px。

### (b4) P1 数字框内引用收尾引号孤儿行首 —— 中
- 位置：P1 中栏「数字看本周」奶油盒第 3 行：
  `21 nov., zaterdag — de nieuwe film 《试探》 gaat in première`
  折为两行，`》` 独占第二行行首。
- 实测：交付 PDF 文字层逐行扫描（全 8 版唯一一起）：P1 有行以 `》` 起首，
  `》gaat in première`，bbox x=417.4–549.5pt, y=1007.4–1029.0pt；
  100dpi 渲染图 P1 同位置目视确认；核心 0 孤儿行。
  `.text.md` 该行为完整单行——缺陷纯属渲染折行，与源码文本无关。
- P8 范文书名号检查通过：全版扫描无行以 `》`/`」`/`）`/`”` 起首，
  范文《试探》均在行中。

## 通过项（逐项实测值）

- **D4（BO5 首胜 vs T1 加「全球总决赛」限定）**：3 处 + Q56 + 键注 56 全部落地。
  P4 正文 `content34.py:130`「这是中国队第一次在全球总决赛的BO5里打赢T1」；
  Q56 题干 `content34.py:211`「BLG是第一次在全球总决赛的BO5里打赢___」key=T1；
  键注 56（P8 印出）「BLG versloeg T1 voor het eerst in een Worlds-BO5」。
  事实核对（公开来源）：BLG 半决赛 3–1 胜 T1；此前中国队从未在全球总决赛 BO5
  胜 T1（2024 决赛 T1 3–2 胜 BLG；2023/2022 半决赛 T1 均胜 JDG）。
- **D5（GEN「今年一场没输」为假）**：P1 `content12.py:42` 与 P4 `content34.py:131`
  均已为 S16 限定表述「GEN在S16一场没输，只丢了一小局：瑞士轮3胜0负
  （对LYON 2比1），八强3比0，半决赛3比0」；全文无「GEN今年一场没输」。
  公开来源核实：瑞士轮 GEN 2–1 胜 LYON（10月25日，LYON 先下一局，GEN 连扳两局；
  这是 GEN 瑞士轮唯一丢的一局），瑞士轮 3–0；淘汰赛 QF 3–0 LYON、SF 3–0 IG，
  故「淘汰赛一局没输」为真，P4 事实框「GEN今年 — 淘汰赛一局没输」保留正确。
  四分之一决赛 IG 3–1 TES、GEN 3–0 LYON、BLG 3–0 DK、T1 3–1 KC 与半决赛
  GEN 3–0 IG、BLG 3–1 T1 亦与公开赛果逐项相符；决赛 11月15日 03:00 北京时间
  = 11月14日 14:00 美东，巴克莱中心，相符。
- **P1 数字框标题**：`数字看本周 Deze week in cijfers`，盒内最紧余量 21.0px，通过。
- **P4 盒标题**：`体育小日历 Sportdata` 余量 32.2px；`看比赛的中文 Wedstrijdwoorden`
  余量 13.5px，通过。P5 `电影小日历 Filmdata` 余量 56.8px，通过。
- **P4 gloss（荷兰语前缀实测）**：P4 注释盒前缀确为 `Notities｜`（荷兰语），
  6 行，`GEN，`行无遮挡，通过。
- **freeze**：`freeze.py baseline` 核心 8/8 SVG 字节一致；
  `freeze.py diff --strict-cjk` 新增汉字 0，rc=0（badge 拉丁-only）。
- **版本重建**：scratch 副本重定向 OUT 后 `run.py` 重跑，8/8 SVG 与交付版
  sha256 一致；REG 150 题（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38）。
- **P8**：`p8.py extract` 150/150；`p8.py compare` CLEAN（missing=[] extra=0
  keydiff=[]）；P8 最小字号 **9.98pt**（≥ SOP §1.1 底线 9.75pt，通过；
  不是 10pt）；P8 芯片 A2 11 / B1 24 / B2 3 = 核心。
- **150 题逐题手验**：REG key 与 P8 印出 key 仅 Q150 一处差异（开放写作题，
  REG key `(开放题，范文如下)` vs 印出 `✓`，为截断式印法，预期内）；
  其余 149 题 key 与题干逐题配对无误（手验表 `keycheck-150.txt` 全 150 行已读；
  另核对题干事实与正文：139.38亿件/22天、7.77亿件单日最高、320−80=240、
  湖南顺丰 +20%、高铁急送 196 城 4 小时、读书月 7 场馆、11月1日开幕、
  文化馆之夜 11月14日、《试探》11月21日冯绍峰主演、小林短文 D 节与 Q141–146、
  Q147–149 情景题，均与正文一致；Q56 见 D4）。
  Q150 范文实测 **138 字**，在 120–180 字要求内；范文内星期与日期自洽
  （周日决赛 15日、周一包裹 16日、周六电影 21日、周日小雪 22日）。
- **日期/星期**：`date` 核验 11月1日周日、4日周三、5日周四、6日周五、7日周六、
  8日周日、9日周一、14日周六、15日周日、21日周六、22日周日，与文中全部一致；
  小雪 2026年11月22日 15:23、农历十月十四、第20个节气、冬天第2个、
  三候首候虹藏不见、引文「小雪气寒而将雪矣，地寒未甚而雪未大也」均与公开
  历法/典籍相符；深圳读书月第27届、主题「悦读深圳、阅连世界」、七场馆、
  11月7日国际美术馆日、文化馆之夜，均与公开报道相符；
  《试探》11月21日上映、冯绍峰/陈雨锶/李梦、钢琴家女友失踪、山间别墅，
  与公开定档报道相符。
- **网 PDF 文字层**：`pdftotext` 44,234 B，与印版去空白后逐字一致；8 页。
- **occlusion**：自检阳性对照全过；本版 0 flags，核心 0 flags，新旧差 0。
  （但 occlusion 对纯填充奶油盒标题越边是空信号——本次 3 处越边均由
  真墨横扫 + 渲染像素检出，occlusion 未报。）
- **#3 KIT 其余所称修复点**：P4 C-head「Lees het programma」✓；P8 D-head
  「Lees, antwoord」✓；P7 teaser 末端 2586.3 ✓；P8 keys 末端 2491.1 ✓；
  P4 gloss 不缩短 ✓；P2 词语卡 4 句均为单行 ✓；8 条本周金句各出现恰 2 次 ✓；
  U+2019 为 0 ✓；“Double 11”核心 P6 亦有 2 处，属继承非泄漏 ✓；
  P8 键注缩短 7 处 ✓（Q14/Q18/Q20/Q68/Q87/Q95/Q118 均为单行）。
  唯 P2 日历标题“已修”不成立（见 b2），P5 高频词标题为 #3 漏检（见 b1）。
- **荷兰语层通读**：P1–P8 全部荷兰语串已逐行读过，拼写与语法无硬错；
  仅文体小点见“观察”。

## 观察（非阻塞，不计入 b 项；多为核心继承）

- Q37（P3）与 Q74（P5）为同一题（读书月 7 场馆），跨版重复；key 一致，核心亦然。
- P1 日历盒内有两条截稿线：长段「Sluiting: 10 nov. De finale is op 15 nov. …」与
  短行「Sluiting: 10 nov. — de finale nog niet gespeeld」内容重复；短行即 b3 越边行。
- P1 快递柜配图为俄语文字储物柜（「ТУТ ПОСЫЛКИ 24/7」），标为（资料图），核心亦然。
- KIT 称“Photo credits kept in English”，实际各页均为 `Foto:` 且 P5 为
  `Publiek domein`——版面本身前后一致的荷兰语化，无问题，唯 KIT 表述不准。
- P7「Zo wordt het Engelse «Sunday, Nov 22» 11月22日星期日」以法语引号标英文例；
  P1 副标「De finale ontmoet de pakketten」措辞生硬但可懂；
  P4 C-head「Lees het programma」与 glossline「Lees het schema op pagina 4」
  对同一赛程表用词不一（programma/schema）；P1 用「Vul de zin in」，
  其余各版用「Vul in」——与核心自身的 Fill in the blank / Fill in 差异同构。

## 修法建议（供生产方参考，不由校对改动）

- b1：把 P5 盒标题荷兰语缩短（如 `Woorden van de week` → `Woorden`，或
  `这一周的高频词　Woorden`），或降字号，复测墨右缘 ≤ 盒边。
- b2：把 P2 日历标题再缩短（如 `Data van deze week` → `Deze week`），
  复测须以盒边（x=1411.5）为准，不以照片为准。
- b3：把 P1 截稿短行缩短（如删「— de finale nog niet gespeeld」后半，
  或并入长段后删除短行——两行本就重复），复测墨右缘 ≤ 盒边。
- b4：把 P1 数字框第 3 行改写/断行，使 `》` 不落行首（如「21 nov., zaterdag —
  de nieuwe film 《试探》」断句前移，或缩短为「21 nov. — film 《试探》」）。
- 修后整期重渲染，按 SOP §8 从头再做一轮全量校对（含真墨横扫 + 渲染目视），
  零问题方能定稿。

## 证据文件（均在 scratch-proof-zh-cn-nl1/ 内）

- `GATE-LOG.md`：全部机械门自跑结果汇总。
- `keycheck-150.json` / `keycheck-150.txt`：150 题逐题手验表。
- `ink-sweep.json` / `ink-sweep.log`：奶油盒真墨横扫（本版 + 核心对照
  `ink-sweep-core.json`：核心最紧余量 +10.25px，无负值）。
- `render/p-1.png` … `render/p-8.png`：交付印 PDF 100dpi 全版渲染；
  `render/p5-title-zoom.png`、`render/p2-title-zoom.png`、
  `render/p1-sluiting-zoom.png`：三处越边放大证据；
  `render/p1-300-1.png`：P1 300dpi 渲染（b3 复测用）。
- `texts-p*.svg.txt`：8 版可见文本逐行抽取（精读底本）。
- `freeze-baseline.log`、`freeze-diff.log`、`p8extract.json`、`p8compare.json`、
  `occlusion.log`、`run-rebuild.log`、`rebuild-svg-compare.txt`、`web.txt`、`print.txt`。
