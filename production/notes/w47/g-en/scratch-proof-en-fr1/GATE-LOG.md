# GATE-LOG — 2026-W47 en-fr proof1（重建版，2026-11-11，复校员独立重跑，盘上实测）

Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-fr1/`
（`probe.txt`、`run-copy.log`、`occlusion.log/.json`、`occlusion-selftest.log`、`p8-extract.log/.json`、`p8-compare.log/.json`、`freeze.log`、`freeze-diff.log/.json`、`freeze-final/`、`print.txt`、`web.txt`、`print-nl.txt`、`web-nl.txt`、`scan.py`、`scan.log`、`check_s11.log`、`creambox-all.log`、`creambox-check.log`、`creambox-core.log`、`creambox-check-core.log`、`creambox.py`（引自上轮 `r1-old-build/` 原样复制）、`creambox_check.py`（同前）、`render/print/p-1..8.png`、`render/print/p1-200-1.png`、`render/print/p2-200-2.png`、`render/web/p1-1.png`、`render/web/p8-8.png`、`render/crop-p1-searches-2.png`、`render/crop-p2-didyouknow-2.png`、`render/diff-p{1,2,5,6,7,8}.png`、`render/cmp-p1-searches-{old,new}.png`、`render/cmp-p1-inbrief-{old,new}.png`、`render/cmp-p2-band-{old,new}.png`、`render/cmp-p5-{old,new}.png`、`render/cmp-p7-top-{old,new}.png`、`render/cmp-p7-bot-{old,new}.png`）
工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`。`TMPDIR=<scratch>/tmp`。`/dev/null` 开工检查正常。未写 /tmp，未改生产文件（收工 SHA 复核与开工一致），未 commit、未 push。

## 0. 对象核对（任务书 + KIT §7 + 盘上 sha256sum，2026-11-11 13:30 UTC 实测）

| 文件 | 字节 | SHA-256（完整） | 结果 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-fr.pdf` | 29,330,979 | `76b4522c53a2fcad0a92f9b02180ff353dc73845ce57080cb7c1d2b0d263dd2f` | 与任务书/KIT 一致 ✓（8 页，1462.5×2025 pt） |
| `The-Lucerna-VOL4-en-fr.web.pdf` | 2,413,670 | `dd68f929b86af917626769bb52cad6ba34a0b6fe4e959a43279de4e319f83266` | 与任务书/KIT 一致 ✓（8 页，< 7 MB） |
| `2026-w47-en-fr.text.md` | 53,809 | `2d832a170a229817af36c1c5378db7ef2030abd54bec54ab5cf019a6f0364855` | 与任务书/KIT 一致 ✓（1305 行） |

核心 en 复核（只读）：印 PDF `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566`（41,407,278 B）、text.md `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b`（51,405 B），与 core-en KIT §7 记录的 fix1 后定稿值一致；网 PDF `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8`（2,804,271 B，fix1 前为 `2ee5391f…`，已变）；核心 registry `05d412f9d55b1919a928ef4b6a5f5d50fe3f2630096802d48a201648a7fbc6f8`；本版 registry `58f67e95eca854e7506c9a2bd29a908e4ef81257ef658288c831fbf9ecbc51d9`。收工三件 SHA 与开工一致，未变。

## 1. 机械门（逐门重跑）

| 门 | 命令 / 位置 | 结果 |
|---|---|---|
| 探针 | `echo probe \| git -C <repo> hash-object -w --stdin` + scratch 写文件 | hash `c4b82938…`，RC=0；`probe.txt` 写入成功 ✓ |
| run.py（scratch 副本） | 复制整版到 `<scratch>/build-copy`（副本内跑，不碰生产），`tools/venv/bin/python run.py` | **RC=0**，0 OVERFLOW / 0 TOO WIDE，TOTAL 150，MODEL 82；副本随后删除 ✓（注：首次复跑因误删 `assets/` 致 moth 文件缺失而失败，属复校员操作失误，重拷完整版后一次通过；生产文件未受影响） |
| occlusion 审计 | `tools/venv/bin/python tools/occlusion_audit.py <ed>/svg --json occlusion.json` | **0 flags** ✓ |
| occlusion 自检 | `... occlusion_audit.py <ed>/svg --selftest` | 自检 OK：6 类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 阳性对照全触发，干净对照静默 ✓ |
| p8 extract | `tools/p8.py extract --p8 <ed>/svg/p8-test.svg --total 150` | **150/150**，noted set 60/150：[3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82–87, 89, 108–150]（与核心 noted 集相同）✓ |
| p8 compare | `tools/p8.py compare --core-p8 core-en/svg/p8-test.svg --edition-p8 <ed>/svg/p8-test.svg --total 150` | **CLEAN**，missing=[] extra_count=0 uncertain=[]；keydiff=[137, 138, 139, 140, 150]（读者语翻译键 + 写作键，预期内，与 W46 en-fr 同）✓；抽出键 38=b、39=a、40=d、41=c |
| p8 extract vs registry | 抽出键逐项对 `registry.json` | 150/150；仅 Q150 差异（registry 长式 vs 提取短标 `Tâche ouverte`，与核心同 pattern）✓ |
| registry keys vs core | registry 逐项对 core-en `registry.json` | 键差异仅 137–140、150（读者语键），其余 145/150 键相同；注记差异为中↔法翻译 ✓ |
| freeze 渲染 | `tools/freeze.py baseline --build <ed> --core-svg <ed>/svg --out freeze-final` | **8/8 SVGs byte-identical**：p1 `1b1a791f…`、p2 `dd332b9c…`、p3 `9d64511a…`、p4 `049cbf23…`、p5 `e944be19…`、p6 `0f6f06dd…`、p7 `715db784…`、p8 `4978f960…`；core integrity 8 文件未变 ✓ |
| freeze diff vs core | `tools/freeze.py diff --core-svg core-en/svg --edition-svg <ed>/svg` | p1 +34/−34、p2 +43/−54、p3 +26/−23、p4 +26/−22、p5 +25/−22、p6 +26/−21、p7 +66/−55、p8 +103/−98；新增 CJK 共 9 个，全为 U+3000（每页 1–2 个）；新增串均为法语讲解/家具，删去串均为中文讲解层/W46 惯例词表行/重排 P8 键行/家具 ✓ |
| 印/网文字层 | `pdftotext [-layout] print/web` + token 多重集 + 逐页比较 | -layout：印=网=108,899 B；无 layout：印=网=49,439 B；token 多重集差 0/0；逐页 byte-identical 8/8（每页字符数 12558/13916/11369/12422/10819/11388/13968/21088）✓；网 < 7 MB ✓ |
| P8 最小字号 | PyMuPDF 读印/网版 spans + SVG 属性（`scan.py`） | PDF 有效最小 **10.12 pt**（P8 答案键块，0.75 缩放组内，73 个 span；其余页最小 11.62 pt）；SVG 属性最小 13.5 pt（全版与 P8 同）；印/网逐页 span 数与最小值完全一致；均 ≥ §1.1 下限 9.75 pt ✓。备注：KIT “13.5 pt” 为属性值，非渲染有效值（仅记录，不计入判定） |
| §1.1 / P8 检查 | `check_s11.py fr`（`scratch-fanout-en2/fanout/check_s11.py`） | **RC=0，ALL §1.1/P8 CHECKS PASS**：色集 core 19 / edition 19，无多无少；徽章色 A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` 齐全；P8 min font 13.5；Q113–120 选项行 [A2] 标签、Levels 145–149 [A2]、Q120 [A2] chip、H WRITING `Écriture [B1]` 均在 ✓ |
| boxtitle 宽度 | occlusion BOXTITLE 类 + P7 目视 | 审计 0 flags；P7 三处旧 HEAD TOO WIDE 节头（ERROR CLINIC / READERS' CORNER / AN EXAMPLE LETTER）渲染中均在栏宽内 ✓ |
| keycheck | p8 extract vs registry（上）+ 150 题人工逐题核对（§3） | 机械 150/150；人工 150/150，零问题 ✓ |
| 引号/字符 | 8 页 SVG 可见文本正则统计（`scan.py`） | “ 82 / ” 82 成对 ✓；U+2019 0 ✓；ASCII 撇号 73；U+00B7 282（与核心完全一致）；U+3000 141；可见文字真实 CJK 0；原始 SVG 内 CJK 仅蛾标 `<title>Lucerna 三色蛾</title>`（与核心共有）；“Note \| Note \|” 0；禁词（TODO/FIXME/Lorem/占位/SOP/proofread/cover/bridge/XXXX/TBD）0 ✓ |
| VOL 计数 | 8 页 SVG 逐页统计，与 core-en 逐页对照 | VOL.4 12、VOL.5 8、VOL.3 3，逐页与核心完全一致 ✓（P1 3/0/0、P2 1/1/0、P3 1/1/0、P4 1/0/0、P5 1/0/0、P6 1/2/1、P7 3/3/2、P8 1/1/0） |
| ABSTRACT | `ABSTRACT.txt` | 一行 + 结尾换行，775 B，法语，无 ASCII 双引号 ✓ |

## 2. creambox 逐盒裁定（原版 +45 px 窗口，本版 23 行负值全裁定；精炼版 NO OVERFLOW）

原版 `creambox.py` 全版扫描（本版 8 页 SVG）逐行：

| 页 | 盒 y / 盒底 | 末基线 / 余量 | 末行 | 裁定 |
|---|---|---|---|---|
| P1 | y=786 / 1067.2 | 1104.2 / −37.0 | `TRY IT NOW　À vous de jouer` | 下块标题，盒底下 37 px，假阳性 |
| P1 | **y=588 / 1256.0** | **1244.0 / +12.0** | `Intérêt relatif, pas des volumes exacts.` | **SEARCHES 盒内，D2 已修**（旧 −18.0） |
| P1 | y=1280 / 1652.0 | 1676.0 / −24.0 | `THE WORD OF THE WEEK` | 下块标题，盒底下 24 px，假阳性 |
| P1 | y=1874 / 2290.0 | 2246.0 / +44.0 | `in the 2025–26 Ashes. (p. 4)` | 盒内 ✓ |
| P2 | y=526 / 706.6 | 742.6 / −36.0 | `Life goes on around the politics. Next` | 盒后流文，假阳性 |
| P2 | y=200 / 497.6 | 534.6 / −37.0 | `WHAT IS ON THIS WEEK?` | 下块标题，假阳性 |
| P2 | y=1340 / 1485.5 | 1437.7 / +47.7 | `tour.` | 盒内 ✓ |
| P2 | **y=833 / 1185.4** | **1171.1 / +14.3** | `November 3.` | **DID YOU KNOW 盒内，D3 已修**（旧 −12.7；盒高 325.5→352.5） |
| P2 | y=1211 / 1544.9 | 1539.8 / +5.0 | `anglais à la rédaction.` | 盒内，紧但未出 ✓ |
| P2 | y=1636 / 1768.0 | 1738.0 / +30.0 | `Le dépouillement continue.` 等 ×3 | 盒内 ✓（三格同 rect） |
| P3 | y=200 / 644.5 | 680.0 / −35.5 | `A film is not only a story — it is also` | 盒后流文，假阳性 |
| P3 | y=1224 / 1399.0 | 1436.0 / −37.0 | `A　COMPREHENSION` | 下块标题，假阳性 |
| P3 | y=856 / 1068.6 | 1105.6 / −37.0 | `FIVE SENTENCES` | 下块标题，假阳性 |
| P4 | y=489 / 820.7 | 856.2 / −35.5 | `How do you follow three sports in one` | 盒后流文，假阳性 |
| P4 | y=1435 / 1610.9 | 1647.9 / −37.0 | `A　COMPREHENSION` | 下块标题，假阳性 |
| P4 | y=856 / 1274.3 | 1311.3 / −37.0 | `ONE SCREEN, TWO SCREENS` | 下块标题，假阳性 |
| P5 | y=2034 / 2244.8 | 2280.3 / −35.5 | `If you want to practise` | 盒后流文，假阳性 |
| P5 | y=200 / 345.7 | 382.7 / −37.0 | `A　COMPREHENSION` | 下块标题，假阳性 |
| P5 | y=852 / 1064.6 | 1101.6 / −37.0 | `FRIDAY'S WORDS` | 下块标题，假阳性 |
| P6 | y=200 / 441.0 | 477.0 / −36.0 | `A note on numbers in this issue: this` | 盒后流文，假阳性 |
| P6 | y=779 / 954.2 | 991.2 / −37.0 | `READ THE CHART　Graphique` | 下块标题，假阳性 |
| P6 | y=666 / 878.6 | 915.6 / −37.0 | `FIFTY ELECTIONS` | 下块标题，假阳性 |
| P7 | y=254 / 429.4 | 464.9 / −35.5 | `win = to get first place. won = the past` | 下块说明文，假阳性 |
| P7 | y=953 / 1098.8 | 1134.3 / −35.5 | `more than = a bigger number than. In` | 下块说明文，假阳性 |
| P7 | y=1658 / 1803.9 | 1839.4 / −35.5 | `The counting will continue. The new` | 下块说明文，假阳性 |
| P7 | y=2151 / 2296.9 | 2332.4 / −35.5 | `Use the past for the past: Collins` | 下块说明文，假阳性 |
| P7 | y=359 / 504.6 | 540.1 / −35.5 | `Newspapers use the present in` | 下块说明文，假阳性 |
| P7 | y=818 / 964.1 | 999.6 / −35.5 | `Nobody knows whether the count will` | 下块说明文，假阳性 |
| P7 | y=651 / 1038.7 | 1075.7 / −37.0 | `READERS' CORNER　Courrier` | 下块标题，假阳性 |
| P8 | y=1720 / 2000.0 | 1907.6 / +92.4 | `a busy week of votes, socks and stories — an` | MODEL 盒内 ✓ |

精炼版 `creambox_check.py`：全部盒内余量为正（P1 +12.0/+44.0/+45.7、P2 +47.7/+14.3/+5.0/+30.0、P3–P7 各盒 +47.7/+48.1/+48.5、P8 +92.4），**NO OVERFLOW，RC=0**。
对照 core-en：两脚本均跑核心 8 页 SVG——原版负值 pattern 与本版一致（同为下块标题/流文 −35.5…−37.0），核心 P1 SEARCHES 同样 +12.0、P2 DID YOU KNOW 同样 +14.3；精炼版核心同样 NO OVERFLOW（核心最紧盒 +4.5，本版 +5.0）。200 dpi 裁图证据：`render/crop-p1-searches-2.png`、`render/crop-p2-didyouknow-2.png`（末行在盒内，下方留白）。

## 3. 150 题逐题核对（text.md 全文通读 + SVG 题面核对 + registry 对照）

- 编号连续 1–150；每页 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；级别 A2 62 / B1 66 / B2 22。
- text.md 附录 150 行与 registry 逐项一致（137–140 为键句 + 注记括号，键句本身一致；112–119 在正文另有同号词干行，附录本身 150 行连续）。
- 逐题核对题面、原文、图表、算术：全部正确。抽查要点：Q7 B 254、Q9 C 218、Q46 A（2025-11-21 周五珀斯）、Q47 C 背伤、Q48 B、Q49 A 2010–11、Q50 C 12:30、Q51 B 膝伤、Q52 hosted、Q53 lasts、Q54 eight、Q55 won、Q83 C 19、Q84 A 33/35、Q87 C 435（254+162+19）、Q97 takes、Q100–107 演练（won/more/lost/will/published/whether/chose/win）、Q108–111 改错、Q112–119 完形（Tuesday/call/continues/will meet/writes/will certify/wears/will watch）、Q120–132 选择/阅读、Q133–136 句型、Q137–140 翻译（法译准确）、Q141–144 配对（b/c/d/a 全对）、Q145–149 对话（row/film/popcorn/show/Friday）、Q150 开放写作；模型文 82 词（字母数字 token 计）。
- 五组配对题逐组对 SVG 渲染核对：P2（24b/25c/26a/27d ✓）、P3（38b、**39a、40d**、41c ✓；SVG 渲染选项 a. teaches and guides / b. chosen to take part / c. lives with you in the jungle camp / d. place where the Games are fought）、P4（56b/57c/58d/59a ✓）、P5（74d/75a/76b/77c ✓）、P8（141b/142c/143d/144a ✓）。
- 金句：P7 8 句逐字出自本期正文，页码标注（P1/P2/P3/P4/P5/P6）正确。

## 4. 8 页目视（印版 P1–P8 全页 + 网版 P1/P8，72 dpi；D2/D3 盒 200 dpi 裁图）

- 渲染：`pdftoppm -r 72` 自印版 PDF（`render/print/p-1..8.png`）与网版 PDF（`render/web/p1-1.png`、`render/web/p8-8.png`）；网版与印版视觉一致。
- 结果：除修复处外，无溢出、重叠、压页脚、图片与出处问题；页脚 `Page N sur 8` 全 8 页正确；刊头/徽章/栏目条齐全；P8 答案块在页内，未压页脚。
- P7 工具盒目视：A2/B1/B2 三行均在奶油盒内，B2 行无 `encore`，盒底留白充足（与 +48.5 px 实测一致）。

## 5. 必验项专项证据

### fr fix1（D5 “encore”）
- `encore changer`：content*.py / SVG / text.md / registry 全版 0 命中。
- P7 工具盒 B2：`content7.py:99`、`text.md:865`、SVG `p7-lang.svg`、印/网 PDF 文字层四源同文 `Personne ne sait si le décompte va changer.`。
- 全版剩余 `encore` 2 处，均合法：Q138 注 `continues = continue encore`（SVG P8 `y=2178.6`、text.md:1281）；P7 读者来信注 `aucune vraie lettre n'est encore arrivée`（SVG P7 `y=2196.9`、text.md:879）。

### Q39/Q40 与 Ashes 回顾
- 见 PROOF-NOTE“必验项逐项结果”；外部事实检索：cricbuzz（Perth 847 球、史上第三少、自 1888 年最少）、cricket.com.au（8 wicket、2 天、系列赛程至 2026-01-08、第四场墨尔本 4 wicket、第五场悉尼 5 wicket、4–1）、Sky Sports（首三场珀斯/布里斯班/阿德莱德、第四场 2 天内结束、英格兰自 2011 年悉尼以来首胜）、TNT Sports（847 球、137 年来最少）。
- 禁串：`Perth is winning!` / `second week in Perth` / `Ashes begin` 全版可见文本 0 命中；`Arsenal are winning!` 1 命中（P4）。

### 旧版对比（旧版 = 上轮 proof1 建版，印 SHA `14da9810fa348a577d16927d90c7c2c05e67c537c533266ff81860486b7c11a5`）
- 文字层 token 多重集差（旧 `r1-old-build/print.txt` vs 新 `print-nl.txt`，同为无 layout 抽取，旧 8781 / 新 8891 token）：全部差异在修复集内，见 PROOF-NOTE；单 token 已逐项定位（`19` 17→16：旧 Q125 词干 `Thu, Nov 19`；`Turin` 7→6：旧 Q46 干扰项 `Sunday, November 22, in Turin`；`Day` 12→10：旧 Q55 词干 `Day one is already sold out`；`1st` 1→0：旧 `1st Test`；旧键 `C` ×1：旧 Q125 键 C→新键 A）。
- 像素差（72 dpi 旧渲染 vs 新渲染，阈值 >10）：P1 33,905 / P2 53,846 / P3 **0** / P4 587,776 / P5 6,275 / P6 536 / P7 294,029 / P8 17,366；逐页定位见 PROOF-NOTE；对比裁图：`render/cmp-*`（P1 SEARCHES、P1 IN BRIEF、P2 段、P5、P7 上/下，新旧各一）。

## 6. 结论

机械门除（无）外全绿；全文、150 题、8 页目视、外部事实已全量复校。结论 **(a)：定稿，零缺陷**。仅记录、不计入判定：D5 字体（P8 渲染有效最小字号 10.12 pt vs 属性 13.5 pt，仍 ≥ 9.75 pt 下限；见 PROOF-NOTE）。
