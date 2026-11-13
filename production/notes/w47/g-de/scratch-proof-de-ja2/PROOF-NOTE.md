# PROOF-NOTE — 2026-W47 de-ja · proof2（独立复校，全量）

- 复校员：独立复校（与 proof1、fix1 builder 均非同一人）
- 日期：2026-11-11（EST 05:37 开工，UTC 10:37–约 11:20）
- 版：`2026-w47-de-ja`（德语目标 · 日语读者），fix1 重建版（P7 工具盒 pad 90→110）
- 结论：**(a) 零问题可定稿**
- 缺陷清单：无（D1/D2/… 共 0 条）
- 门禁日志：`GATE-LOG.md`（同目录；每道门禁的命令与 RC 全数记录）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-ja2/`（png/ 渲染、txt/ 文字层、gates/ 门禁输出、fd/ rebuild-A 脚本副本 + tr_ja 数据、verify-copy/ verify 副本、creambox.py canonical 副本、quote_pixel.py + quote-spots.json）

## 0. 探针与 SHA 核对（先核对，通过后才开工）

| 文件 | 实测 | 任务给定 | 结果 |
|---|---|---|---|
| 印刷 PDF `Die-Lucerna-VOL4-de-ja.pdf` | 23,901,741 B，`2638a6e62c00da39933a3e921bb74d0d81d6cc00ddf2eff50000c182554f98e1` | 同左 | ✓ 符 |
| 网页 PDF `Die-Lucerna-VOL4-de-ja-web.pdf` | 2,155,095 B，`161f2dd0bdfefecffe06944ded2d22f22410daeb321e7bc387c745da9cbcce16` | 同左 | ✓ 符 |
| text.md `2026-w47-de-ja.text.md` | 51,913 B，`a59f784705bec4329b7dfa19321256c2469ab7680212302481876fc96f957f69` | 同左 | ✓ 符 |

探针：开工前 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功（`9daeafb…`，RC=0），并在本科目录真实写盘；全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。复校结束复核三件 SHA/字节/mtime 均未变；`git status` 仅显示该版目录为未追踪（`??`），未改动 repo 任何文件。未改源、未重建、未 commit、未 push、未派 subagent。

## 1. 本次重点①：P7 工具盒修复独立重测（fix1 宣称值逐项实测）

方法：canonical 工具 `hidden_files/w47/tools/creambox.py`（本 scratch 内逐字节副本）扫全部 8 个 SVG（`gates/creambox-all.log`），不是窄带 creambox_check.py；200 dpi 工具盒裁切目视（`png/crop-p7-toolbox-200dpi.png`）。

| 宣称（FIX-LOG §4 / KIT §6） | 独立实测 | 结果 |
|---|---|---|
| 工具盒清除 +19.2、盒底 774.0 | 盒 y=330 bottom=**774.0**，末基线 754.8，clearance **+19.2**，desc-clear **+13.1**（末行 `Es ist fraglich, ob ... = まだ不明`，8 行 Σlines=8） | ✓ 符 |
| LESERBRIEFE +10.4 不变 | 盒底 1342.5，末基线 1332.1，clearance **+10.4**，desc-clear +4.5 | ✓ 符 |
| NOCH EIN WORT 止于 1508.5 | 盒底 1508.5，末基线 1465.6，clearance +42.9（1548 规则前 39.5px 以上） | ✓ 符 |
| 200 dpi 目视末行在盒内 | 裁切显示末行完整在奶油盒内，盒底留白清晰 | ✓ 符 |

全版扫描 32 个奶油盒：最小 inside-only clearance **+10.4**（LESERBRIEFE），最小 desc-clear **+4.5**，无一真溢出。6 处负 clearance 全部裁定为误报（inside-only 明细为凭）：

- P1 ZAHLEN 盒（bottom 1719.2，−37.0）：盒内末行 +45.7，−37.0 是下一盒标题 `JETZT ÜBEN`（盒下 +37.0）。
- P1 IN DIESER AUSGABE 盒（bottom 1652.0，−24.0）：盒内末行 +16.0，−24.0 是下一标题 `DAS WORT DER WOCHE`（盒下 +24.0）。
- P2 DIE STILLE WOCHE 盒（bottom 1549.1，−44.9）：盒内末行 +19.5，−44.9 是下一标题 `Die Daten der Woche`（盒下 +44.9）。
- P7 三处 BEISPIELE 盒（−35.0）：盒内末行均 +47.4（desc-clear +41.1），−35.0 是盒下练习题号 `101.`/`105.`/`109.`（+34/+35）——FIX-LOG §1 已载明的 matcher 已知误报。
- P8 MUSTER 盒：clearance +47.1，末行 `bleibe zu Hause. Die Woche macht Spaß!` 在盒内。

## 2. 本次重点②：P8 H-box / Q67 宽引号测量（de-en D1/D2 方法，200 dpi 墨列）

方法：复用 de-zh-tw proof2 的 `quote_pixel.py`（同法：200 dpi 印刷 PDF 单连续窗口像素墨列分析，阈值 <128；闭引号墨迹以其墨列起点落在该字符 advance 框内为准）；闭引号前空隙 >0.2em 为缺陷。位置取自 PyMuPDF rawdict 逐字符 bbox。

| 处 | 字体/字号 | 闭引号 advance | 闭引号前空隙 | 结论 |
|---|---|---|---|---|
| P8 H 框指示行 `«Meine Novemberwoche»` | Newsreader16pt-Regular 16.12pt（**不是 sans**） | » [653.05, 662.16]，墨起 653.84 | **1.80pt = 0.11em**（后隙亦 1.8pt） | PASS |
| P8 Q67 键注 `«Im Lande des Christkinds» (1903)` | NotoSansCJKjp-Regular 9.94pt | » [505.81, 510.57]（仅 4.76pt 宽），墨起 506.64（框内 0.83pt） | **0.72pt = 0.07em**（后隙 1.8pt） | PASS |
| 全版弯引号计数 | U+201C ×33 / U+201E ×33（德文 „…" 成对）;U+00AB ×6 / U+00BB ×6（«…» 成对）;U+201D 0、U+2019 0（8 SVG + text.md 全扫） | — | — | — |

**de-en proof2 D1/D2 缺陷类在本版不复现**：两处闭引号均非 de-en 的 U+201C（全宽字元、墨迹贴右缘），而是 U+00BB »（窄 advance、墨迹贴其字元左缘）；空隙与 Newsreader 对照组同量级（H 0.11em 与 zh-tw 同值；Q67 0.07em，比 zh-tw 的 0.11em 更紧），远低于 0.2em 阈值。200 dpi 裁切目视（`png/crop-p8-hbox-200dpi.png`、`png/crop-p8-key67-200dpi.png`）：两处闭引号均贴紧前一字母，与开引号对称，无可见断开。

## 3. 内容复校（全文重读 + 150 键逐题 + 事实逐条网查）

- `.text.md` 全文 1,187 行逐行读完；练习 1–150 连续编号、题题有键；P7 金句 8/8 与正文逐字一致（页码 Seite 1/1/2/3/5/4/6/6 正确）；MUSTER 实测 84 词（verify 计数）。
- 键逐题人工验算：配对 25–28（d/c/a/b）、52–55（d/b/c/a）、141–144（c/a/d/b）与词框顺序一致；比较级 56–59（mehr/später/früher/mehr）与比分/时间/积分一致（Leipzig 5 球 vs Dortmund 2 球；20:30 晚于 15:30；欧冠 11 月 3–4 日早于 11 月 8 日；荷兰 8 分 vs 德国 5 分）；被动/将来 101–103、weil/dass/ob 106/107/109–111、113–120 变位、121–128、129–136、137–140 翻译（日译 3 题 + 德译 1 题）、145–149 对话变位（öffne/machst/schaue/schaue/lese）全部正确；Q51 键 B（8 und 5：荷兰 8、德国 5）与网查积分一致；Q150 键 `自由課題 — 枠のポイントに従おう`。
- Q34 新题干：`"Am Montag öffnet in Köln der erste ___."` 各 1×（text.md、P3 SVG、双 PDF 文字层）；旧题干 0×。P3 目视确认单行在位；与键 `Weihnachtsmarkt`（单数）吻合。
- 日期/星期：`date` 核实 2026-11-03（二）、11-04（三）、11-05（四）、11-13（五）、11-16（一）、11-17（二）、11-18（三）、11-20（五）、11-22（日）、11-23（一）、11-27（五）、11-29（日）——文中所有"星期×+日期"搭配正确；18+11=29、15+7=22、16+6=22 均正确；图表 44+33+23=100。

### 事实逐条网查（全部实测有来源）

- Buß- und Bettag 2026：周三 11 月 18 日，仅 Sachsen 法定假日；Bayern 当天停课、家长照常上班；1995 年起除 Sachsen 外废止；总在第一 Advent 前 11 天（feiertagskalender-deutschland.de；SächsSFG §6：Sachsen 该日公开舞会禁令 3:00–24:00 原文核实）。
- Totensonntag 11 月 22 日（周日）、第一 Advent 11 月 29 日（周日）、Volkstrauertag 11 月 15 日。
- 欧冠第 4 轮（11 月 3–4 日）：Bayern 客场 2:0 Atlético（进球 Karl 54'、Laimer 74'，与正文"die Tore schossen Lennart Karl und Konrad Laimer"一致）；Dortmund 2:1 Betis；Leipzig 2:3 Man City；Stuttgart 客场 0:2 Galatasaray（UEFA 官网 + Sportradar）。
- 欧联/欧协 11 月 5 日：Leverkusen 0:1 Marseille；Crystal Palace 1:1 Hoffenheim；Trabzonspor 0:1 Freiburg。
- 德甲第 9 轮（11 月 6–8 日）9 场比分全符：HSV 3:1 Gladbach、Dortmund 2:1 Elversberg、Leipzig 5:2 Augsburg、Mainz 1:2 Bayern、Stuttgart 1:0 Bremen、Köln 1:2 Leverkusen、Freiburg 2:0 Union、Hoffenheim 2:1 Schalke、Paderborn 2:2 Frankfurt；9 场 30 球。积分榜：Bayern 第 1（21 分）、Köln 第 15（9 分）。
- 国家队：Serbien–Deutschland 周五 11 月 13 日 20:45 贝尔格莱德（UEFA 空场处罚，仅 15 岁以下儿童 + 50 名德国球迷入场——与正文"nur Kinder und 50 deutsche Fans"逐字相符）；Deutschland–Niederlande 周一 11 月 16 日 20:45 柏林奥林匹克、ARD；德国 5 分、荷兰 8 分，争四分之一决赛；小组 A2。Bayern–Köln 周五 11 月 20 日 20:30 安联。
- 圣诞市：Dom 市 11 月 16 日–12 月 23 日（Roncalliplatz），正式开场 11 月 17 日 19:00，11 月 22 日（Totensonntag）关闭；Engel 市 Neumarkt 同期、同日关闭；Hafen 市 11 月 13 日起；Aachen 市 11 月 20 日–12 月 23 日；入场免费。
- 1903 日历：Richard Ernst Kepler 作画、Gerhard Lang 作诗，Reichhold & Lang 慕尼黑 1903 年首版印刷 Adventskalender《Im Lande des Christkinds》，儿童剪贴画（de.wikipedia.org）；1930 年画：Wilhelm Ritter（1860–1948）《Weihnachtsmarkt auf der vorderen Insel Schütt》（1930）原题核实。
- P6 时政：家庭 Stromsteuer 2.05 Cent/kWh（自 2003 年未变）；Merz 要求全民下调、结果未定（与正文"Ob eine Einigung gelingt, ist offen"一致）；Bundeshaushalt 2027 定于周五 11 月 27 日表决（bundestag.de 原文："die Verabschiedung ist für Freitag, 27. November 2026, geplant"）。
- 欧冠第 5 轮预告（IN DER NÄCHSTEN AUSGABE）：Arsenal–Dortmund、Leipzig–Lens（11 月 24 日），Inter–Stuttgart、Lille–Bayern（11 月 25 日）——UEFA 赛程核实；欧联 11 月 26 日（Dinamo Zagreb–Leverkusen、Hoffenheim–Sturm Graz）亦核实。

## 4. 几何与冻结门禁（独立重跑，见 GATE-LOG.md）

| 门禁 | 命令 | RC | 结果 |
|---|---|---|---|
| occlusion | `tools/venv/bin/python tools/occlusion_audit.py <edition>/svg --json occlusion.json` | 0 | **0 flags**，selftest 6 类 planted 全触发、clean 对照静默 |
| creambox（canonical 全版） | `tools/venv/bin/python creambox.py <edition>/svg/*.svg` | — | 见 §1：32 盒最小 inside +10.4 / desc +4.5，无真溢出 |
| p8 extract | `tools/p8.py extract --p8 …/p8-uebungen.svg --total 150` | 0 | noted 150/150（joined） |
| p8 compare | `tools/p8.py compare --core-p8 … --edition-p8 … --total 150` | 0 | **CLEAN**，missing=[]，extra=0，keydiff=[137, 138, 139, 150]（预期：137–139 日译题 + 150 Q150 PREFIX） |
| freeze diff | `tools/freeze.py diff --core-svg … --edition-svg …` | 0 | TOTAL added CJK **2,994**（P1 243 / P2 229 / P3 312 / P4 180 / P5 269 / P6 237 / P7 412 / P8 1,112） |
| freeze_direct（rebuild-A 脚本字节） | `fd/freeze_direct.py ja <edition> <gates>`（脚本与 rebuild-A 逐字节同；tr_ja.py + stub_* 引自 scratch-fanout-de 数据） | 1* | rendered **8/8**：frozen 144/164/200/166/179/173/163/183，sha8 `b01ba1b1/2db0dd83/2dd3b3f2/df1bebf7/e7b235f9/89156519/b854370f/1c855c30` 全部命中；source removed 516 / added 524，unaccounted 仅 JP 字体开关 4 串 |
| boxtitle（rebuild-A 脚本字节） | `fd/boxtitle.py ja` | 0 | **7/7 fit**（387.6/333.4/300.7/379.4/361.9/290.3/286.5 ≤ 400.5） |
| keycheck（rebuild-A 脚本字节） | `fd/keycheck.py ja <edition> <gates>` | 0 | **149/150**，唯一 mismatch 为 Q150 PREFIX（key `自由課題 — 枠のポイントに従おう` vs extracted `自由課題`），与拉丁版一致的预期结果 |
| verify.py（副本上跑，未动原版） | `verify-copy/verify.py`（仅 BUILD 路径指向副本） | 0 | TOTAL 150、编号连续、SVGs byte-identical、§1.1 audit True、verbatim OK、P8 floor True（9.9375pt）、17 禁用词全无、chart 748/561/391、MUSTER 84 词；P7 col3 ends 1508.5 |
| text layer 印/网 | `pdftotext -layout` 双版 + diff | — | **逐字节相同**（各 112,955 B，diff 为空） |
| d2scan（abutting） | `d2scan.py ja d2-scan.json`（fix scratch 工具） | 0 | 67 对，web gap >0.5pt：**0** |
| P8 最小字号 | PyMuPDF span 实测 | — | 印刷/网页均为 **9.94pt**（≥9.75pt 门槛） |
| chips | builder 日志交叉核对（rebuild1/2/3.log） | — | 141（P1 10 / P2 15 / P3 18 / P4 15 / P5 18 / P6 18 / P7 12 / P8 35；P8 A2 22 / B1 13），与 KIT §1 一致；fix 未改文字，text.md SHA 不变 |

\* 注：`freeze_direct` RC=1 为日语版**按设计**的结果（KIT §5 已载明）：source level 仅因子 JP 字体开关 4 串（`Noto Serif CJK SC` 删；`JP`、`Noto Sans CJK JP`、`Noto Serif CJK JP` 增，transform.py 198–202 行 SC→JP 切换）而不通过——与 proof1 / builder 逐值相同，是既存工具记账缺口（svglib.py 日文字体名），非缺陷，不拦停定稿；rendered 8/8（逐页 frozen 计数 + sha8 与 proof1 逐值复现）已覆盖冻结核对。`freeze.py diff --strict-cjk` 不适用（读者语解说层本身新增 CJK 2,994 字），按 KIT §5 记录总量。

## 5. 目视复校（印刷 8 页 + 网页 P1/P7/P8 + 200 dpi 裁切 + 印网像素差）

- 印刷 P1–P8 100 dpi 逐页看完，**零发现**：版式、标题、图片、图注、盒子、练习题、页脚（`n / 8 ページ`）、图表均无遮挡、无溢出、无错字。P1 ZAHLEN 盒与 word-of-week 单行盒内；P3 Q34 新题干单行在位；P6 图表标签与柱条无接触；P8 MUSTER 盒完整、ANTWORTEN 在页脚上方结束。
- 网页 P1/P7/P8 逐页看完，与印刷页逐页一致；印/网 8 页像素差：mean|diff| ≤0.53，P2/P6 近乎相同（max 6/4，仅抗锯齿），无版式漂移。
- proof1 的工具层 T1/T2 在 fix1 网页 PDF 中**已消失**：P1 刊别行三 span 在网页版确为 Bold（`LucernaNewsreader-Bold` 子集嵌入后，`LucernaNotoSerifCJKJP-Bo` 27.0pt）；P1 `« der Adventskalender »` 在网页版确为斜体（`LucernaNewsreader-Italic`）。flags 法统计全页 bold 数：网页 ≥ 印刷（P1 71/64、P2 56/50、P3 61/57、P4 59/55、P5 66/62、P6 74/67、P7 91/67、P8 100/99），无字重丢失。T3（词 x 位置累计漂移）随新 webpdf 字体度量变化，d2scan 词间距 0 缺口 + 文字层逐字节相同 + 像素差佐证视觉无错位。
- Q87 选项 `C. 44 %` 的 `%` 折到下一行——正常换行，无溢出，核心版同式（proof1 O2 同）。

## 6. ABSTRACT（SOP §9 核对）

`ABSTRACT.txt` 426 B，日语单行，无 ASCII 双引号；含刊名（Die Lucerna ドイツ語週刊 VOL.4）、目标语名、A2～B2、150 問与本期真实主题（ブンデスリーガ復帰、オランダとのネーションズリーグ決戦、悔い改めと祈りの日と死者の日曜日、ケルンのクリスマス市、11 月 3～8 日欧州戦与德甲结果）——事实只取本期内容，无模板套话。✓

## 7. 观察（非缺陷，不影响定稿）

- O1（proof1 同）：版内 `verify.py` 打印 `MUSTER label: MISSING`，但 P8 页面上 `MUSTER　模範文（84語）` 标签实际存在——脚本按独立 `MUSTER` 元素精确匹配，而本版标签为合并元素；verify RC=0。属脚本匹配口径问题，非版面问题。
- O2：`tr_ja.py` 201 行仍含 Q108 中文选项旧变体（作为翻译对照表的源键 `'„Stiller als sonst“ heißt... A. 比平时更安静 …'`）；本版全部文件（.py/.md/.svg/.txt）中 0×，Q108 实际选项为日语（`A. いつもより静か · B. いつもと同じ · C. いつもよりうるさい`）。建议下次 fan-out 时清理对照表残留（不影响本版）。

## 8. 未做事项

- 未改源、未重建、未 commit、未 push（按任务要求）；verify.py 只在副本上跑，原版 SVG 未触动（复校后 SHA 逐值复核未变）。
- `freeze.py baseline`（核心重建 8/8）未重跑：freeze_direct 的 rendered 8/8（逐页 frozen 计数 + sha8 与 proof1 逐值复现）已覆盖冻结核对；baseline 属于构建者门禁，非 proof2 必须项。
- 本版不含网站封面块（cover.json / lint 规则 14 属整周门禁，非单版 proof 范围）。
- 网页 P2–P6 未逐页目视全读：以印/网文字层逐字节相同 + d2scan 0 缺口 + 8 页像素差（mean ≤0.53）+ proof1 对同内容网页版的 8/8 目视作交叉佐证；P7（本次改动页）与 P1/P8 已逐页目视。

## 结论

**(a) 零缺陷可定稿。** P7 工具盒 fix1 宣称值独立实测全部命中（清除 +19.2、盒底 774.0、LESERBRIEFE +10.4、NOCH EIN WORT 止于 1508.5）；de-en D1/D2 宽引号类在两处实测均不复现（H 0.11em、Q67 0.07em，均 ≤0.2em）；内容、事实（逐条网查）、几何、冻结、印/网文字层、目视全部通过；proof1 的 T1/T2 网页字重差异已随新 webpdf 消除。freeze_direct source level 的 4 串 JP 字体开关为 KIT 已载明的既存项，按任务要求如实记录、不拦停。
