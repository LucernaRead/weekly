# PROOF-NOTE — Lucerna Weekly 2026-W47 **de-nl**（proof2，独立全量复校）

- 版次：2026-W47，德语目标 × 荷兰语讲解（de-nl），VOL.4
- 复校员：proof2（独立复校，只读：未修版、未 commit、未 push）
- 日期：2026-11-11
- 交付件（sha256sum 已核对，与任务书/KIT 一致）：
  - 印刷 PDF `Die-Lucerna-VOL4-de-nl.pdf` — 10,964,697 B — `c8a5f5e2ea2affc15df0aef472ce08f74e3ae5cc826d2ef49d636c866c083521`
  - 网页 PDF `Die-Lucerna-VOL4-de-nl-web.pdf` — 1,596,830 B — `4ed5b46e385815a4358cb01407e0a476f69cdc9885801756998410fd5e336d8a`
  - 文本导出 `2026-w47-de-nl.text.md` — 49,403 B — `e904fb3d7ee18a72c1316f8693f39436ff9390648261d6fbad18afcfb7fc848e`
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…`，rc=0；scratch 目录真实写文件通过。`TMPDIR=<scratch>/tmp`，全程未写 /tmp。
- 先读：SOP.md §1.1/§8/§9、proof1 PROOF-NOTE（verdict (a)）、FIX-LOG §4 de-nl 行、de-nl WEEKLY-KIT 全文、de-en proof2 D1/D2 方法、de-zh-tw proof2 §5 + `quote_pixel.py`。

## §1 本次重点 A — P7 工具盒 family fix 独立复测 ✅ 通过

复测方法：canonical `tools/creambox.py` 全版 8 页 SVG 扫描 + 200dpi 像素/裁切目视。日志 `gates/creambox-all.log`（350 行）。

- **DER WERKZEUGKASTEN**：盒 y=310，盒底 813.0，末行基线 793.0，**盒内清除 +20.0，下行字母清除 +13.9**——FIX-LOG 宣称「清除 +20.0」实测验证。末条 `Es ist fraglich, ob... = nog onzeker` 完整在盒内，下行字母 g 下方有干净奶油。
- **LESERBRIEFE**：清除 +10.4（下行字母清除 +4.5）——宣称验证。
- **NOCH EIN WORT**：盒底 1547.5，末行基线 1504.6，清除 +42.9——「止于 1547.5（距 1548 线 0.5px）」验证。
- P7-TOOLBOX 汇总：6 盒，盒内最小清除 +10.4，下行字母最小清除 +4.5。
- 其余各页盒：盒内清除 ≥ +14.0，下行字母清除 ≥ +8.3。
- 仅 4 处负清除，均为已记录的误报：P1 −24.0（盒内 +16.0；`DAS WORT DER WOCHE` 标题在盒底下 24px——下一标题样式）与 P7 BEISPIELE ×3 −35.0（盒内 +47.4；练习号 101/105/109 在下方，同 FIX-LOG §1 的已知误报类）。
- 200dpi 裁切目视干净：`render/crop-p7-toolbox.png`（末条完整在盒内，盒顶与导语间隙干净）、`render/crop-p7-leserbriefe.png`（末行在盒内，NOCH EIN WORT 盒干净）。

## §2 本次重点 B — P8 H-box / Q67 宽引号测量（de-en D1/D2 方法）✅ 未复现

方法：de-zh-tw proof2 的 `quote_pixel.py` 原样复用（md5 `62172cbcf525ef8f9790e55e4d1c1f28`），200dpi 墨列测量；阈值：闭引号前空隙 >0.2em 为缺陷。日志 `gates/quote-pixel.log`，测点 `gates/quote-spots.json`。

本版 P8 共 4 个 »（全为 U+00BB guillemet；**U+201D 全版为 0**，故 de-en D1/D2 的 U+201C/U+201D 类在本版不可能出现）：

| 位置 | 文本 | 字体/字号 | 空隙 | 结论 |
|---|---|---|---|---|
| H-DE-1 | `«Meine Novemberwoche»` | Newsreader 16.12pt | 1.8pt = 0.11em | 通过 |
| H-DE-2 | `«Leserbriefe»` | Newsreader 16.12pt | 1.8pt = 0.11em | 通过 |
| H-NL | `«Mijn week in november»` | NotoSansCJKsc 15.0pt | 1.44pt = 0.10em | 通过 |
| Q67 | `«Im Lande des Christkinds»` | NotoSansCJKsc 9.94pt | 0.72pt = 0.07em | 通过 |

200dpi 裁切目视：`render/crop-p8-hbox.png`（三处 » 均紧贴前字母与后标点）、`render/crop-p8-key67.png`（`Christkinds» (1903))` 紧贴）。**de-en D1/D2 缺陷类在 de-nl 未复现。**

## §3 机械门禁（全部独立重跑，日志在 `gates/`）

| 门禁 | 结果 |
|---|---|
| `occlusion_audit.py`（repo tools，venv python） | **0 flags**；自检 6 类植入缺陷全部触发 |
| `p8.py extract` | **150/150** |
| `p8.py compare` vs core-de | **CLEAN**；missing=[]；keydiff=[137,138,139,150]（预期：137–139 前向翻译、150 开放写作） |
| `freeze.py diff`（--core-svg 指 core-de/svg） | **+7 CJK，全为 U+3000**（P2–P8 各 1，P1 为 0） |
| `freeze_direct.py`（rebuild-A 副本，md5 校验与 scratch-fanout-de 副本一致 `e94fdfbd…`；另原样取 `tr_nl.py` 与 `cjk_inventory.json` md5 `321523d5…`） | 源码 PASS（0 未说明的删/增；521 删 / 529 增）；渲染 8/8；冻结局 SHA 与 rebuild-B 完全一致（083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7）——证明 fix1 未改动任何正文 |
| `keycheck.py`（rebuild-A 副本 md5 `6865002b…`） | **149/150 精确**；唯一 Q150 差异为提取器截断 "Open opdracht — volg de punten in het schrijfblok" → "Open opdracht"（预期） |
| `boxtitle.py`（rebuild-A 副本 md5 `f4ad3569…`） | **7/7 适配**（advance 宽；最宽 DER WERKZEUGKASTEN `Werktuig` 395.5/400.5）；**真墨迹重测**（PIL getbbox）：7/7 通过，最宽墨迹右缘 396.0，余量 4.5px。日志 `gates/boxtitle-ink.log` |
| `d2scan.py`（abutting） | 54 对，**0 处网页空隙 >0.5pt** |
| 印/网 text layer（pdftotext） | 默认模式**字节一致**（各 50,192 B）；`-raw` 归一化后一致 |
| P8 最小字号（PyMuPDF 渲染 pt，两版 PDF） | **9.94pt** ≥ 9.75pt 地板（SOP §1.1 让步第 4 步） |
| 难度芯片（SVG 中 rx="2.7" 独立重数） | **141**（10/15/18/15/18/18/12/35）= KIT 宣称 |
| `verify.py` 独立重跑（edition 目录，rc=0） | TOTAL 150；按页 10/18/18/18/18/18/12/38；按级 A2 69 / B1 67 / B2 14；编号连续 1..150；SVG 重跑后字节一致；SOP 1.1 style audit True，旧色值无；P8 地板 9.9375pt；P7 逐字核对 8 句各 2×；禁词（桥接/Le Lucerna/The Lucerna/VOL.3/VOL.2/Geisterspiel/Karneval/Volkstrauertag/NFL/American Football/11.11/Tankrabatt/14,04/Hart aber fair/Klassiker/Allerheiligen/8,35/ZEW）全 0；P1 头条去标点 40 字符（限 56）；图 44+33+23=100；日期算术 18 Nov+11d、15 Nov+7d、16 Nov+6d 均 True；P7 col3 止于 1547.5。日志 `gates/verify.log` |

## §4 内容事实逐条网查（2026-11-11，全部核实无误）

- **德甲 MD9（11 月 6–8 日）**：美因茨 1:2 拜仁（Kimmich 14'、Karl 57'）、莱比锡 5:2 奥格斯堡、多特 2:1 埃尔弗斯贝格、汉堡 3:1 门兴、科隆 1:2 勒沃库森、弗赖堡 2:0 柏林联、霍芬海姆 2:1 沙尔克、帕德博恩 2:2 法兰克福、斯图加特 1:0 不来梅；**30 球**；科隆 MD9 后**第 15 位**（9 分，10:14）；拜仁/多特 21 分并列榜首。
- **欧冠 MD4（11 月 3–4 日）**：马竞 0:2 拜仁（**Karl 54'、Laimer 74'**，fcbayern.com）、多特 2:1 贝蒂斯、莱比锡 2:3 曼城、斯图加特 0:2 加拉塔萨雷（伊斯坦布尔）。
- **欧联/欧协 11 月 5 日**：勒沃库森 0:1 马赛、水晶宫 1:1 霍芬海姆、特拉布宗 0:1 弗赖堡（Kübler 14'）。
- **欧国联**：塞尔维亚—德国 周五 13.11 20:45，Rajko Mitić 球场；UEFA 观众禁令，U15 以下儿童 + **50 名指定德国球迷**入场，约 5,000 人到场（kicker/bundesliga.com，2026-11-10）；4 轮后德国 5 分、荷兰 8 分、希腊 8 分；德国—荷兰 周一 16.11 20:45 柏林；「仅前二晋级」属实。
- **科隆圣诞市场**：Dom 市场 16.11.–23.12.2026 Roncalliplatz，22.11（Totensonntag）关闭；Markt der Engel（Neumarkt）同期，22.11 关闭；Hafen-Weihnachtsmarkt（Schokoladenmuseum）自 13.11；官方 Dom 开幕 周二 17.11 19:00；亚琛市场 20.11.–23.12.2026。
- **Stromsteuer**：家庭 **2.05 ct/kWh**、工业 0.05 ct（自 2026 年起），Merz 欲全员下调、尚未决定；2027 预算表决定于**周五 27.11.2026**（bundestag.de）。
- **Buß- und Bettag**：1995 年废除（仅萨克森保留，为 Pflegeversicherung 筹资；萨克森职工多缴 +0.5%）；拜仁学校停课；2026 年 11 月 18 日（周三，首个 Advent 11 月 29 日前 11 天）；萨克森禁舞 **3:00–24:00**，SächsSFG §6 原文核实。
- **Adventskalender**：首版《Im Lande des Christkinds》1903 年，插画 **Richard Ernst Kepler**，Gerhard Lang / Reichhold & Lang（de.wikipedia 等）。
- **MD10 赛程（11 月 20–22 日）**：拜仁—科隆 周五 20:30；周六 5 场 15:30 + 沙尔克—斯图加特 18:30；周日 奥格斯堡—美因茨 15:30、不来梅—汉堡 17:30。
- **欧冠 MD5（11 月 24–25 日）**：阿森纳—多特、莱比锡—朗斯（24 日）；国米—斯图加特、里尔—拜仁（25 日）。
- **Wilhelm Ritter 1930（P3 图注）**：de.wikipedia「Wilhelm Ritter (Maler)」：1860 年 8 月 24 日生于纽伦堡，1948 年卒于 Eschenbach；作品录含 *Weihnachtsmarkt auf der vorderen Insel Schütt* (1930)；fr.wikipedia 与 wikidata Q2574698 佐证（German painter 1860–1948）。图注「Weihnachtsmarkt in Nürnberg im Jahr 1930 — Gemälde von Wilhelm Ritter (1860–1948) — public domain」属实。
- **日期**（`date -d`，Europe/Berlin 核对）：13.11 周五、16.11 周一、17.11 周二、18.11 周三、20.11 周五、22.11 周日、27.11 周五、29.11 周日、3.11 周二、8.11 周日、6.11 周五、7.11 周六——与纸面全部一致。

## §5 150 题逐题语义核对

方法：题干 + 选项 + 答案逐题读；keycheck 149/150（Q150 为提取器截断，预期）；另对全部关键题做人工题干—答案一致性核对。抽检要点（全部通过）：
- P1 BLITZQUIZ Q7–10：Q7 B 荷兰、Q8 A 20.30、Q9 B 仅萨克森、Q10 B 16.11。
- P2 Q11–28：日期/星期/州/动词变位（wurde abgeschafft、bleiben、gehen、behält）与配对 25-d / 26-c / 27-a / 28-b 均对。
- P3 Q29–46：Q32 Falsch（Ritter 画的是纽伦堡非科隆）；Q34 新题干 `Am Montag öffnet in Köln der erste ___.` 已见，旧复数题干 0 次；Q39 B 港口市场、Q40 B 23.12、Q41 A、Q45 `Vor dem Dom steht ein großer Weihnachtsbaum`、Q46 `Die Lichter leuchten schon vor dem ersten Advent`。
- P4 Q47–64：Q47 B 2:0、Q48 B 2:3、Q50 A 30 球、Q51 B（荷兰 8、德国 5）、配对 52-d / 53-b / 54-c / 55-a；Q56–58 比较级 mehr / später / früher；Q60 A 20.45、Q61 B 20.30、Q62 C 18.30、Q63 A 17.30、Q64 B 3:1。
- P5 Q65–82：Q67 B（首版 1903《Im Lande des Christkinds》）；weil 从句 Q76–79 动词置尾均对。
- P6 Q83–100：图表 44+33+23=100；Q83 A、Q84 B、Q85 B（44+33=77）、Q86 B、Q87 A 23%、Q88 B 100%；Q91 B 2,05、Q92 B 27.11、Q93 wird、Q94 ob、Q96 beginnt、Q98 Kirchenjahr、Q99 Friedhof、Q100 Einigung。
- P7 Q101–112：Q104 A Passiv、Q108 A（stiller dan anders）、Q109 ob、Q110 fraglich、Q111 dass 从句动词置尾、Q112 B。FEHLERKLINIK 四组正误均对（"Halb neun ist 8.30 Uhr" 正确）。
- P8 Q113–150：完形 Q113–120（schaut / bastelt / schreibt / sieht / beginnt / liest / denkt / ist）；对话 Q145–149（öffne / machst / schaue / schaue / lese）；配对 141-c / 142-a / 143-d / 144-b；翻译 Q137–140 双向均对；Q150 开放写作题干完整。
- 德语正文与荷兰语讲解层逐句通读：荷兰语注释语义准确（如 `Opgelet` 仅 P2 一处用法正确；`halb neun = half negen (vóór neun)`；`In de Perfekt staat het deelwoord achteraan`；`In de bijzin met ob staat het werkwoord achteraan`；`beginnen → begint` Q96 注）；未发现荷兰语误译或德语语法错误。

## §6 文本导出 / ABSTRACT / MUSTER

- `2026-w47-de-nl.text.md`：47,761 字符，1185 行，591 条；**0 个 CJK 字符**；U+3000 ×122（仅家具）；U+201C 33 / U+201E 33 成对，U+201D 0，U+2019 0，«» 7/7；直引号 0。
- 与 core-de 文本导出 diff：235 个变更块，全部为讲解/家具层；启发式检查德语正文改动仅 6 处误报（家具标语、NOCH EIN WORT 释义、动词注释括号、MUSTER "(84 Wörter)" → "(84 woorden)"）；仅 3 个变音词「缺失」（FÜR、Türchen、Wörter——均为家具/释义）。Q150 在场（行 1185）；Q34 新题干 1 次、旧题干 0 次。
- MUSTER 独立重数：**84 词** ✓。
- ABSTRACT.txt：362 B，单行荷兰语，无 ASCII 双引号，含刊名、目标语言、A2–B2、150 oefeningen、真实话题 ✓（SOP §9）。

## §7 网页版对照（proof1 §7 修复验证）

- P1 头条宽度：印刷 Newsreader Regular 39.75pt 宽 966.16；网页 LucernaNewsreader-Bold 39.75pt 宽 **966.16——完全一致**。斜体 `« der Adventskalender »`：印刷 173.44 / 网页 **173.44——完全一致**。**proof1 §7 的 61 行行宽差已消除**（重建后的网页版内嵌 LucernaNewsreader-Bold/Italic 子集）。
- 印/网文字层：逐页 span 数一致（P1 230、P2 210、P3 250、P4 206、P5 226、P6 227、P7 227、P8 351），文本全同；配对 span 坐标最大偏差 **0.2pt**（P1 masthead 黑体字）——无重排。
- 100dpi 像素差：P2/P6 近乎字节一致（maxdiff ≤6，>30 的像素为 0）；其余页 0.035%–0.361%，差异带全部落在光栅图片矩形内（P3 画作、P4 kopfball、P5 1903 日历、P7 lesesaal、P8 1905 足球照、P1 照片）+ P1 masthead/头条粗斜体光栅化差异——仅图片 JPEG 再压缩与字体子集光栅化差异，无任何文字重排。
- 目视：网页版 P1、P7 100dpi 全页与印刷版一致（头条粗体、斜体周词、工具盒、LESERBRIEFE、FEHLERKLINIK 均在位）。日志 `gates/extra-checks.log`。

## §8 版式目视（8 页印刷 100dpi + P7/P8 200dpi）

P1–P8 全部目视通过：无溢出、重叠、页脚侵入、缺字。已核实的要点：P1 头条、FRAGEN DER WOCHE、DAS WORT DER WOCHE `« der Adventskalender »`、BLITZQUIZ Q7–10；P2 RECHNEN（18+11=29、15+7=22、16+6=22）、Opgelet 警告；P3 Q34 新题干；P4 成绩表、MD9 九场 30 球；P5 Wochenplan、Q67 选项；P6 图表 44+33+23=100、Q85（44+33=77 → B）、Q88（100 → B）；P7 全部栏目；P8 完形键、对话键、配对键、MUSTER 框完整。

## §9 未核实 / 局限

- 图片的 public-domain 来源未逐张独立复核：以 KIT 与 verify.py 的图注署名（Wikimedia PD、Library of Congress、U.S. Air Force 等）为准。Ritter 画作的作者与年份已独立网查（§4）。
- 荷兰语讲解层逐句通读并语义核对，未逐词查词典；德语正文逐句通读，未逐词查 Duden。
- 其余事实、题键、几何、门禁均已按上文独立核实。

## Verdict

**(a) 零问题，可定稿。**

本次重点两项均已独立实测通过：P7 工具盒清除 +20.0 / LESERBRIEFE +10.4 / NOCH EIN WORT 止于 1547.5（FIX-LOG 宣称全部验证）；P8 H-box/Q67 宽引号 4 处均 ≤0.11em，de-en D1/D2 缺陷类未复现。全套机械门禁绿灯，150 题逐题核对无误，事实逐条网查无误，印/网两版一致（proof1 §7 已修复验证）。无缺陷清单。
