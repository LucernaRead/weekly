# PROOF-NOTE — 2026-W47 de-it · proof2（独立复校，rebuild 4）

- 版：`2026-w47-de-it`（德语正文，意大利语讲解）· VOL.4 · 刊期 2026-11-16–22
- 复校员：独立 proof2（与重建者、fix1 修复者、proof1 均非同一人）· 2026-11-11
- 结论：**(b) 有问题 1 项（D1，仅 KIT 文档，非内容/几何缺陷），修后可定稿** ——
  交付件三件（印版 + 网页 + 文本导出）内容与几何零缺陷；
  唯一问题是 KIT §5/§6 仍登记 rebuild 3 的旧 SHA/字节数（见 D1），
  改两行 KIT 文字即可，不动任何交付件、不重建。
- 未改源、未重建、未 commit、未 push。复校前后三件 SHA-256 逐一复核，全部未变
  （见 GATE-LOG 末尾）；`git status` 仅显示该版目录为未追踪（`??`），我未改动。

## §1 SHA 核对（开工第一步，全部相符；收尾再核一次，未变）

| 文件 | 字节 | SHA-256 | 结果 |
|---|---|---|---|
| `Die-Lucerna-VOL4-de-it.pdf`（印版） | 10,965,087 | `ca802fb853eb3f18c61cddd5da406c72c9c0471cabd84c76731478f4cdf6f2c0` | ✓ 与任务简报一致 |
| `Die-Lucerna-VOL4-de-it-web.pdf`（网页） | 1,596,994 | `09fb247059a96c37c0fa1fe0178b7dacf35cd1e5500fe6f089b929c722c82300` | ✓ 与任务简报一致 |
| `2026-w47-de-it.text.md` | 49,712 | `1594ba080bece8b9a947cf011a64a355125b8869f82413ccdb03ae31a269f255` | ✓ 与任务简报一致（与 proof1 核对的文本 SHA 完全相同，文本零改动） |

两份 PDF 均为 8 页，1462.5 × 2025 pt。探针：开工前 `git hash-object -w` rc=0
+ 真实写文件均通过；全程 `TMPDIR=<scratch>/tmp`，未写 /tmp；未遇配额问题
（/home/hatch 75G 可用）。

## §2 本次重点复测（任务专项，全部独立重测通过）

### §2.1 P7 工具盒清除量 —— fix1 宣称全部实测属实

canonical 全版扫描 `hidden_files/w47/tools/creambox.py`（8 份 SVG 全扫，
32 个奶油盒，见 `gates/creambox-all.log`）：

| 量 | FIX-LOG 宣称 | proof2 实测 | 结论 |
|---|---|---|---|
| 工具盒底（y + height） | 803.5 | 803.5（rect y=330 h=473.5） | ✓ |
| 末条基线（`Es ist fraglich, ob ...`） | 783.9 | 783.9 | ✓ |
| 清除量 clearance | **+19.6** | **+19.6**（desc-clear +13.5） | ✓ |
| LESERBRIEFE y / 清除量 | 819.5 / +10.4 | y=819.5（rect），末基线 1361.6，clearance +10.4（desc-clear +4.5） | ✓ |
| NOCH EIN WORT 止 | 1538.0 | 底 1538.0，末基线 1495.1，clearance +42.9 | ✓（1548 规则前 10px） |

200 dpi 工具盒裁切目视（`render/crop-p7-toolbox-print.png`，另有网页版同裁切）：
末条 `Es ist fraglich, ob ... = ancora dubbio` 完整在奶油盒内，`g` 下行字母下方
留有清晰奶油空隙，盒底边线在其下；与 LESERBRIEFE 盒间距正常。
印/网工具盒裁切像素一致（P7 整页印/网差异仅 0.03%）。

**全版其余 31 个奶油盒**：inside-only 最小清除量 +10.4（即 LESERBRIEFE 本身，
与 fix 前相同、fix 未动）；其余全部 ≥ +14.0。4 处窗口 clearance 为负
（P1 IN DIESER AUSGABE 盒 −24.0、P7 三个 BEISPIELE 盒各 −35.0）均为已知的
匹配器假阳性：inside-only 清除量分别为 +16.0 / +47.4 / +47.4 / +47.4，
负值来自盒下相邻元素（下一标题 / 下方练习题号）的基线落在 +45px 窗口内，
非漫出——与 FIX-LOG §1 记载的假阳性类完全一致。**全版真漫出：0。**

### §2.2 P8 H 框 / Q67 宽引号测量 —— de-en D1/D2 类不复现

方法与 de-en proof2 同法、与 de-zh-tw proof2 同法：200 dpi 印刷 PDF
单连续窗口像素墨列测量（`quote_pixel.py`，阈值 <128；闭引号墨迹以其墨列起点
落在该字符 advance 框内为准；见 `gates/quote-pixel.log`、`gates/spots.json`）：

| 处 | 字体/字号 | 闭引号前空隙 | 结论 |
|---|---|---|---|
| P8 H 框指示行 `«La mia settimana di novembre».` | NotoSansCJKsc-Regular 15.0pt | **1.8pt = 0.12em** | PASS（≤0.2em） |
| P8 Q67 键注 `«Im Lande des Christkinds» (1903)` | NotoSansCJKsc-Regular 9.94pt | **0.72pt = 0.07em** | PASS（≤0.2em） |

200 dpi 裁切目视（`render/crop-p8-hbox.png`、`render/crop-p8-key67.png`）：
两处闭引号 `»` 均贴紧前一字母，与开引号对称，无可见断开。
根本原因：本版无 U+201C/U+201D（全版 0 处，见 §5），H 框与 Q67 用的均是
意语 guillemet «»（U+00AB/U+00BB 各 7 处），» 的 advance 仅 4.76pt、墨迹贴
在其字元左缘；de-en 的宽体 U+201C 在本版不存在，缺陷类无从复现。
（de-zh-tw proof2 同类加测结论相同。）

## §3 proof1 的工具层问题 T1/T2 —— 本重建已修，目视+字体双重确认

- **T1（网页 PDF 衬线粗体丢失）已修**：`pdffonts` 核实网页 PDF 现嵌
  `LucernaNewsreader-Bold`（多处子集）与 `LucernaNewsreader-Italic`；
  200 dpi 标题栏并排对照（`render/crop-p1-head-print.png` /
  `crop-p1-head-web20.png`）：网页 "Die Bundesliga kehrt zurück – Bayern
  gegen Köln" 为粗衬线，与印版同字重。
- **T2（网页 PDF 斜体丢失）已修**：200 dpi 本周词并排对照
  （`render/crop-p1-word-print.png` / `crop-p1-word-web20.png`）：
  网页 `« der Adventskalender »` 为斜体，与印版一致。
- 印/网整页像素差异（100 dpi，灰度 >40 的像素占比）：P1 0.26% / P2 0.00% /
  P3 0.06% / P4 0.14% / P5 0.10% / P6 0.00% / P7 0.03% / P8 0.01%
  （proof1 时 P1 为 1.22%）；残余差异位于图片重压缩带，无内容差异。
- 印/网文字层：`pdftotext` 默认模式均为 50,592B、**逐字节相同**；
  `-raw` 均为 49,392B、归一化文本完全相同（proof1 时尚有 4–5B 差异，现已消除）。

## §4 逐页目视（印版 100 dpi，P1–P8 全看；网页 100 dpi，P1–P8 全看）

- **P1**：刊头、版别行、主标题、导语、FRAGEN DER WOCHE、IN DIESER AUSGABE、
  DAS WORT DER WOCHE（斜体 ✓）、ZAHLEN 盒（`"(Bayern-Colonia 20.30)"` 两行、
  在栏内）、JETZT ÜBEN 1–6、足球图+图注、KURZ & GUT、BLITZQUIZ 7–10、
  页脚 `Pagina 1 di 8`。无溢出、无遮挡。
- **P2**：正文、Nota 盒、四侧栏（标题均在盒内）、RECHNEN 表
  （18.11.+11 天=29.11.、15.11.+7 天=22.11.、16.11.+6 天=22.11.，全对）、
  练习 A–D（11–28）。`DIE STILLE WOCHE　Tranquilla` 在盒内。
- **P3**：正文、Nota 盒、1930 年市场画+图注（Wilhelm Ritter，public domain）、
  `WEIHNACHTSWÖRTER　Parole` 在盒内、`DER TIPP　Consiglio` 在盒内、
  练习 A–D（29–46）。Q34 新题干可见（见 §6）。
- **P4**：正文、Nota 盒、头球图+图注、UND SIE? 盒、9 行结果表、
  练习 A–D（47–64）。表与正文比分逐项一致；9 场进球和 4+3+3+7+4+1+3+2+3=30 ✓。
- **P5**：正文、Nota 盒、ADVENTSKALENDER 盒、`ADVENTSWÖRTER　Avvento` 在盒内、
  UND SIE? 盒、1903 年日历图+图注（Richard Ernst Kepler，public domain）、
  周计划表（Mo 16.11. 国家队 20.45、Di 17.11. 开幕 19 点、Mi 18.11. 忏悔祈祷日、
  Do 19.11. 做日历、Fr 20.11. 拜仁–科隆 20.30）、练习 A–D（65–82）。
- **P6**：正文、Nota 盒、DIE ZAHLEN 盒（18.11./22.11./29.11./2,05/27.11./1995）、
  DIE STILLE WOCHE 通栏盒、DIE DEBATTE 盒、柱条 44/33/23（标签清晰）、
  ÜBUNGSDATEN 单行、练习 A–D（83–100）。44+33=77、44+33+23=100 ✓。
- **P7**：三课 A2/B1/B2、BEISPIELE 三盒、工具箱 6 条（末条在盒内，§2.1）、
  LESERBRIEFE（编辑部示例 + 意大利语披露）、NOCH EIN WORT、
  阅览室图+图注（Carol M. Highsmith，public domain）、Sätze der Woche 8 句、
  FEHLERKLINIK 4 组、VOL.5 通栏。无溢出。
- **P8**：A 完形（113–120）/ B 问答（121–128）/ C 阅读（129–132）/
  D 造句（133–136）/ E 翻译（137–140）/ F 配对（141–144）/
  G 对话（145–149，5 枚徽章）/ H 写作（MUSTER 84 词，独立计数 84 ✓）/
  ANTWORTEN 8 组齐全、1905 足球图。键区末行距底边充足，无溢出。
- 网页 8 页：内容、版式、几何与印版逐页一致（像素差异见 §3）。

## §5 事实逐条网查（全部有公开来源；日期星期另用日历核验）

- **日期星期**（Europe/Berlin 实测）：3.11.二、4.11.三、5.11.四、6.11.五、
  7.11.六、8.11.日、13.11.五、16.11.一、17.11.二、18.11.三、20.11.五、
  22.11.日、27.11.五、29.11.日——与表内 Di/Mi/Do/Fr/Sa/So 及正文
  “Freitag, dem 13.”、“Montag, dem 16.”、“Dienstag, 17.”、“Mittwoch, 18.”、
  “Freitag, 20.”、“Sonntag, 22.”、“Sonntag, 29.” 全部一致。
- **Buß- und Bettag**：2026 年 11 月 18 日星期三，仅萨克森法定假日；
  巴伐利亚停课、家长照常上班；1995 年为筹措护理保险费在全德其余各州废止，
  萨克森雇员护理保险缴费高 0.5 个百分点；萨克森该日 3–24 时禁公共舞会
  （§6 SächsSFG）。与 P2/P6 全文一致。
- **Totensonntag / Advent**：Totensonntag 2026 年 11 月 22 日（第一待降节前
  最后一个主日、教会年最后一个主日）；第一待降节 2026 年 11 月 29 日。✓
- **科隆圣诞市场**：大教堂市场（Roncalliplatz）与天使市场（Neumarkt）
  均 11 月 16 日–12 月 23 日；港口圣诞市场（巧克力博物馆）11 月 13 日起；
  Totensonntag（11 月 22 日）大教堂与 Neumarkt 市场关闭。✓
  （见观察项 O2：港口市场当晚开市的细节。）
- **亚琛圣诞市场**：2026 年 11 月 20 日–12 月 23 日。✓
- **Wilhelm Ritter**：1860–1948；《Weihnachtsmarkt auf der vorderen Insel
  Schütt》（1930，纽伦堡）。✓（德语维基；画题与报内完全一致。）
- **1903 日历**：Gerhard Lang《Im Lande des Christkinds》，Richard Ernst
  Kepler 绘图，1903 年出版；24 首小诗 + 24 幅彩图，儿童剪下贴上。
  ✓（见观察项 O3：“Fenster”一词的简化。）
- **德甲第 9 轮（11 月 6–8 日）**：9 场比分与报内结果表逐项一致——
  汉堡 3:1 门兴、多特 2:1 埃尔弗斯贝格、莱比锡 5:2 奥格斯堡、美因茨 1:2 拜仁、
  帕德博恩 2:2 法兰克福、斯图加特 1:0 不来梅、科隆 1:2 勒沃库森、
  弗赖堡 2:0 联合、霍芬海姆 2:1 沙尔克；共 30 球。✓
  第 10 轮：拜仁–科隆 11 月 20 日 20:30；周六 5 场 15:30，沙尔克–斯图加特
  18:30；周日奥格斯堡–美因茨 15:30、不来梅–汉堡 17:30。✓
- **欧冠第 4 轮（11 月 3–4 日）**：马竞 0:2 拜仁（Karl 54'、Laimer 74'）、
  多特 2:1 贝蒂斯、莱比锡 2:3 曼城、加拉塔萨雷 2:0 斯图加特。✓（UEFA 官方。）
- **欧联/欧协联（11 月 5 日）**：勒沃库森 0:1 马赛、水晶宫 1:1 霍芬海姆、
  特拉布宗 0:1 弗赖堡。✓
- **国家队**：塞尔维亚–德国 11 月 13 日 20:45 贝尔格莱德（RTL），
  德国–荷兰 11 月 16 日 20:45 柏林奥林匹克体育场（ARD）；德国 5 分、
  荷兰 8 分；欧足联观众禁令但儿童（15 岁以下）及 50 名德国球迷可入场。✓
- **欧战 11 月 24–26 日**：欧冠 24 日阿森纳–多特、莱比锡–朗斯；
  25 日国米–斯图加特、里尔–拜仁；欧联 26 日萨格勒布迪纳摩–勒沃库森、
  霍芬海姆–格拉茨风暴。✓
- **预算与电税**：联邦议院定于 2026 年 11 月 27 日星期五表决 2027 预算
  （bundestag.de）；总理 Friedrich Merz 推动电税降至欧盟最低标准，
  家庭现行 2,05 欧分/千瓦时（自 2003 年未变），联盟党与社民党能否达成
  一致仍未定。✓ 与 P6 “Ob eine Einigung gelingt, ist offen”一致。
- **内政说明**：P1 称 11 月 13 日塞尔维亚之战用过去时、而截稿日为 11 月 9 日——
  属该系列已披露的惯例（KIT §8：11 月 13/15/16 日赛事在截稿时仅为预告），
  非本版新问题。

## §6 核对项（数字、日期、金句、答案键、冻结）

- **Q34 新题干** `"Am Montag öffnet in Köln der erste ___."`：
  content34.py、text.md、P3 SVG、印版文字层、网页文字层各 1×；
  旧题干 `"Am Montag öffnen in Köln die ersten ___."` 五处均为 0×。
  键 `Weihnachtsmarkt` 不变；P3 目视新题干在位。
- **P7 金句 8 句**：在 text.md 中每句恰出现 2 次（正文 + P7），
  出处页码全对（S.1×2、S.2、S.3、S.5、S.4、S.6×2）；
  verify.py verbatim OK 亦同。
- **MUSTER 84 词**：独立空白切分计数 84 ✓。
- **150 题答案键**：p8 extract 150/150；compare CLEAN，
  keydiff `[137, 138, 139, 150]` 为预期（137–139 为意译键、150 为开放写作题；
  Q140 为反向题、键即德语句子，故不 diff）；keycheck 149/150 精确，
  唯一非精确项为 Q150（抽取器截断，预期）。键区编号 1–150 齐全无缺。
  逐键人工复核要点：Q8 A=20.30、Q14 Mittwoch、Q16–20 Perfekt
  （worden/geblieben/gegangen/behalten/geblieben）、Q25–28 d/c/a/b、
  Q34 Weihnachtsmarkt、Q43–46 造句（动词第二位）、Q47–51 比分、
  Q52–55 配对（d/b/c/a）、Q56–59 比较级（mehr/später/früher/mehr）、
  Q60–64 时间（20.45/20.30/18.30/17.30/3:1）、Q65–69、Q70–75 词汇、
  Q76–79 weil 句（动词末位）、Q80–82 判断、Q83–88 图表（44/33/23，
  44+33=77、和=100）、Q89–92、Q93–96（wird/ob/geht/beginnt）、
  Q97–100（Buße/Kirchenjahr/Friedhof/Einigung）、Q101–104
  （wird/werden/wird/A）、Q105–108（stiller/weil/…/A）、Q109–112
  （ob/fraglich/dass 句/B）、Q113–120 完形
  （schaut/bastelt/schreibt/sieht/beginnt/liest/denkt…nach/ist）、
  Q121–132、Q133–136、Q137–140 翻译（137 "La Bundesliga torna venerdì."、
  138 "I mercatini chiudono la domenica."、139 "Sto facendo un calendario
  dell'Avvento."、140 反向德语句）、Q141–144（c/a/d/b）、Q145–149
  （öffne/machst/schaue/schaue/lese）、Q150 开放题——全部与题面/原文/图表一致，
  意语键翻译准确。Q51 B（荷兰 8、德国 5，题干先问荷兰）✓；
  Q58 früher（欧冠 11 月 3 日早于德甲 11 月 8 日）✓。
- **德语冻结**：text.md 与 core-de text.md 的德语引文 „…" 多重集 25/25
  完全相同；freeze_direct 源码级 0 未 accounted（520 删 / 528 增，全部有据），
  渲染级 8/8（147/163/195/166/173/175/150/186；
  sha 083e2a2a/689045ad/fc88f676/df1bebf7/86fa4421/2bbe05f9/b7aa0771/57e118e7，
  与 rebuild 3 一致——fix1 未改任何文字）。
  freeze diff：新增 CJK 7 个，全为 U+3000（P2–P8 各 1，P1 为 0）。
- **弯标点**：U+2019 全版 0、U+201D 全版 0；U+201C 33 处、U+201E 33 处，
  逐处核对全部为德语正文引文的右/左引号（„…" 成对），无一处落在意大利语值里；
  意语引文用 «»（U+00AB/U+00BB 各 7 处）。直撇号 U+0027（如 l'Avvento、c'è）
  17 处，渲染紧凑。U+FFFD 0；text.md 无 CJK 表意字；
  SVG 唯一 CJK 残留为 P1 logo 内嵌 `<title>Lucerna 三色蛾</title>`（非渲染文本，
  与 core 逐字节相同，见 O5）。
- **box-title 7/7**：boxtitle.py 全过（DIE STILLE WOCHE Tranquilla 364.1、
  WEIHNACHTSWÖRTER Parole 361.3、DER TIPP Consiglio 242.2、ADVENTSWÖRTER
  Avvento 331.9、DER WERKZEUGKASTEN Attrezzi 379.5、LESERBRIEFE Lettere dei
  lettori 371.9、NOCH EIN WORT Ancora una parola 395.0，预算 400.5px）；
  目视 8 版确认 7 个标题全部收进奶油盒内（最紧为 NOCH EIN WORT，余 5.5px）。
- **ABSTRACT（SOP §9）**：`ABSTRACT.txt` 393 B、一行、意大利语、无 ASCII
  双引号；含本期真实主题（Bundesliga 回归、荷兰决战、忏悔祈祷日、亡者主日、
  科隆市场开市、11 月 3–8 日欧战与德甲结果）、刊名、目标语名、A2–B2 分级
  与 150 题。✓
- **SOP §1.1**：verify.py 样式审计 True；P8 最小字号印版/网页均为 9.94pt
  （≥ 9.75pt 底线）；chips 总数 141（每页 10/15/18/15/18/18/12/35；
  P8 A2 22 / B1 13 / B2 0）；17 禁词全无。

## §7 门禁（独立重跑，全部绿；命令与 RC 见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| occlusion_audit.py | RC 0，**0 flags**，selftest 6 类全触发、干净对照静默 |
| p8.py extract | RC 0，**150/150** |
| p8.py compare | RC 0，**CLEAN**，keydiff `[137, 138, 139, 150]`（预期） |
| freeze.py diff | RC 0，新增 CJK 7，全 U+3000 |
| freeze_direct.py（rebuild-A 新副本） | RC 0，源码级 PASS；渲染级 **8/8**（sha 见 §6） |
| keycheck.py（rebuild-A 新副本） | RC 0，**149/150** 精确，仅 Q150 抽取器截断（预期） |
| boxtitle.py（rebuild-A 新副本） | RC 0，**7/7** |
| measure.py（rebuild-A 新副本） | RC 0，**24/24 PASS**，0 FAIL |
| verify.py（重跑，venv python 显式调用——该文件不可执行，见 GATE-LOG） | RC 0，TOTAL 150、编号连续、SVG 重跑后逐字节相同、SOP 1.1 审计 True、verbatim OK、P8 字号底线 True、17 禁词全无 |
| pdftotext 文字层 | 默认模式印/网各 50,592B **逐字节相同**；-raw 各 49,392B，归一化文本完全相同 |
| abutting 扫描 | 印版/网页各 **23 处、逐处相同**，全部为练习 "→ ___" 的设计间距（SVG 中空格为独立文本元素，宽 5.4 SVG 单位 ≈ 4.05pt）；**真实缺口 0** |
| creambox.py（canonical 全版） | 32 盒全扫，**真漫出 0**（4 处负值均为已知假阳性，见 §2.1） |
| quote_pixel.py（H 框 / Q67） | 0.12em / 0.07em，**均 PASS**（≤0.2em） |
| chips / P8 最小字号 | 141 / 9.94pt（印/网同） |

## §8 观察项（非缺陷，不阻塞；O1/O2/O5 为 proof1 遗留、复核仍在）

- **O1**：P5 UND SIE 意语提示只转述了德语提问的后半句——"Cosa c'è nella
  tua lista dei desideri? Scrivi in tedesco!"（德语原文另问 "Basteln Sie
  einen Adventskalender?"）。意语提示本身通顺、任务明确，属讲解层节略。
- **O2**：科隆市场 Totensonntag 闭市的表述为全称——P2 “Am Totensonntag
  bleiben die Weihnachtsmärkte in Köln geschlossen”、P1 “am 22. November
  bleiben sie zu”。核实：大教堂市场、天使市场、Nikolausdorf 当日关闭；
  港口市场当晚 18:00–21:00 开市。报内 P3 正文的语境是 Dom/Engel 两市，
  该处表述准确；P1/P2 的全称写法是 A2 级简化，未点名港口市场。
  若后版求精确，可写“die großen Märkte am Dom und auf dem Neumarkt”。
- **O3**：P5 “Die Kinder konnten die Fenster mit Bildern überkleben”——
  1903 年原版并无可开的小窗/小门（约 1920 年才出现），儿童是把剪下的
  24 幅彩图贴到 24 首小诗的格子上。主要事实（1903 年、题名、Kepler、
  剪贴）均准确，此处为 A2 级简化。
- **O4**：P1 本周词意语注 "Calendario d'Avvento (24 porte)" 用 `porte`，
  其余各处用 `finestrelle`（P5、P7、Q66 键等）。两词读者均可懂，
  属术语小波动。
- **O5**：P1 母版 logo 内嵌 `<title>Lucerna 三色蛾</title>`（与 core 逐字节相同；
  `<title>` 为非渲染元数据，读者不可见）。
- **O6**：Q18/Q35/Q77 等 "→ ___" 空格换行到下一行（与 core 版式相同，属
  源版式，非缺陷）。

## §9 缺陷清单

### D1 — KIT §5/§6 仍登记 rebuild 3 的旧交付件 SHA 与字节数（文档问题，低严重度）

- 位置：`production/2026-w47/2026-w47-de-it/WEEKLY-KIT.md` §5
  “Deliverables (rebuild 3, 2026-11-11, final; rebuild 2 superseded)”与 §6
  “Gates (rebuild 3, 2026-11-11 — final)”。
- 证据：§5 登记印版 10,965,095 B / sha `0d7be581…`、网页 1,553,872 B /
  sha `dbbe5880…`；盘上实际交付件（本复校开工与收尾两次核对）为
  印版 10,965,087 B / sha `ca802fb8…`、网页 1,596,994 B / sha `09fb2470…`。
  只有 §7 “Rebuild 4”一段登记了新值；§5/§6 的 “final” 已不成立。
  文本导出 SHA（`1594ba08…`）三处一致，无问题。
- 严重度：低。**不影响任何交付件**（三件本身零缺陷）；`insert.py`
  以实测 PDF 计量写 index，不读 KIT，故不阻塞入仓；但 KIT 是当期生产记录
  正本（SOP §8.5），旧 SHA 留在 “final” 标题下会误导后人手核。
- 修法建议：只改 KIT §5 一段（印版 10,965,087 B / sha
  `ca802fb853eb3f18c61cddd5da406c72c9c0471cabd84c76731478f4cdf6f2c0`；
  网页 1,596,994 B / sha
  `09fb247059a96c37c0fa1fe0178b7dacf35cd1e5500fe6f089b929c722c82300`；
  标题改为 rebuild 4 final）与 §6 标题（rebuild 4）。**不重建、不改交付件。**

**D 项合计：1 项（D1，仅 KIT 文档）。内容与几何缺陷：0。**

---
*门禁命令与 RC 详见同目录 GATE-LOG.md；日志与 JSON 在同目录 gates/；
渲染在 render/（100 dpi 全页印/网、200 dpi 重点裁切）。*
