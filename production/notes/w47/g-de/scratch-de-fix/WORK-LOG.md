# W47 DE 返修工作日志（D1–D5，2026-11-10，返修 builder）

任务书：PROOF-NOTE-de.md 缺陷清单 (b)，5 项。只改 production/2026-w47/core-de/ 内文件。
不改 tools/p8.py；不跑 insert.py / lint --write / git push/add/reset/stash；不提交；不碰 W43/W45/W46。

## 读过
- SOP.md §1.1 全文、§8 全文；AGENTS.md；PROOF-NOTE-de.md 全文。
- core-de 全部源码：bslib4.py、content12/34/56/7/8.py、verify.py、render.py、run.py、WEEKLY-KIT.md。

## D4 事实再核实（改前，2026-11-10 晚，任务书要求）
- 日期/时间：塞尔维亚–德国，**2026-11-13 周五 20:45**，贝尔格莱德 Rajko-Mitić 球场，欧国联。
  来源：bundesliga.com（2026-11-10 官方文 "Nations League: In 'Serbiens Marakana' unter Zugzwang"）、
  fussballnationalmannschaft.net、sportsdelulu、kicker.ch 一致。`date -d`：2026-11-13 = Friday ✓。
- 空场事实**与任务书口径有出入**：校对笔记称"全场空场、零观众"；2026-11-10 新报道（dpa 经
  bavarianfootballworks、fussballnationalmannschaft.net、kicker、bundesliga.com）一致称：
  UEFA 确因塞尔维亚球迷此前种族歧视/歧视行为判了 Zuschauerausschluss（另罚 50,000 欧），
  但按 UEFA 规则例外，**15 岁以下儿童（有老师/教练陪同）+ 50 名德国球迷可入场，预计约 5,000 人**，
  55,000 座球场"weitestgehend leer"（基本空着）。即：不是零观众。
  → 因此不采用任务书"全场空场、零观众"写法；保留"vor fast leeren Rängen"（约 5,000/55,000，
  "几乎空场"属实），括号内写明 UEFA 处罚 + 例外。详见 KIT §7 D4 条。

## 修复方案（已定）
- D1：题干字号提至 SOP 阶梯。bslib4.py ex() 加模板级下限钳制（P1–P7 下限 22 单位=16.5pt；
  P8 下限 20.5 单位=15.375pt≈SOP §1.1 15.4pt 让步值，见下）；各 content 文件显式 size= 改写：
  content12/34/56/7：19/20/20.5/21 → 22；content8：18.5 → 20.5。
  P8 用 15.4pt 让步值的理由：SOP §1.1「版数」让步顺序第 3 步明文允许 P8 题干降到 15.4pt
  （W46 现行值）；先以 22 单位试跑 P8，若实测溢出即以该让步值为终值并附实测证据。
- D2：P4 文章第 1 段 "ihren 4. Spieltag" → "ihren 4. Spieltag der Ligaphase"（属格，§8.1 屈折形先例可接受）。
- D3：P6 文章第 2 段 "Er lädt ein zum Nachdenken:" → "Er lädt zur Buße und zum Nachdenken ein:"
  （与 P6 练习 D 填空 "Der Buß- und Bettag lädt zur ___ ein" 亦对齐）。
- D4：P1 导语第 2 段改写（过去时 + 日期 + UEFA 处罚括号）；P7 工具箱 "vor fast leeren Rängen =
  几乎空场" 同步加括号说明；KIT §2 塞尔维亚行同步改。
- D5：P3 Q42 题干 "Warum beginnen die Märkte vor dem ersten Advent?" → "Wie viel früher als der
  erste Advent beginnen die Märkte?"（键 A 与注记不变；B/C 不是时间跨度，仍仅一解）。

## 构建命令（基线 = build9）
- cd core-de && tools/venv/bin/python run.py > scratch-de-fix/build10.log 2>&1
- tools/venv/bin/python render.py
- tools/venv/bin/python ../../tools/webpdf.py svg/ Die-Lucerna-VOL4-de-web.pdf
  （注：webpdf.py 在仓库 tools/，从 core-de 内以相对路径调用）
- W47_BUILD_DIR=<core-de> W47_OUT_MD=<core-de>/2026-w47-de-zh-cn.text.md tools/venv/bin/python \
    ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-de/export_text.py
- tools/venv/bin/python verify.py
- tools/venv/bin/python ../../tools/occlusion_audit.py （参数见 tools/README）
- tools/venv/bin/python ../../tools/p8.py extract --p8 svg/p8-uebungen.svg --total 150
- tools/venv/bin/python ../../tools/p8.py compare ...
- freeze：整 core-de 复制到 scratch 副本跑 run.py，sha256 逐个比对 8 个 SVG。

## 基线 flow 余量（build9.log）
- P1-headline col2 y=1494/1828（余 334）；P1-quiz col3 y=2521/2560（余 39）；P2-ex col3 y=2323/2560（余 237）；
- P3-ex y=1912（余 648）；P4-ex y=2268（余 292）；P5-ex y=2300（余 260）；P6-ex y=2214（余 346）；
- P7 A2/B1/B2 y≈1266/1480（余 ~214），P7 图 ends 1529.5（Sätze hline 在 1548，余 18.5）；
- P8-battery col3 y=1345/1505（余 160）；P8-keys y=2328/2560（余 232）。

## D1 试跑记录（决定 22 / P8 20.5 的实测依据）
- 22 单位全版试跑（build10-trial.log）：FLOW OVERFLOW 三处——P2-ex（end 2979 vs bottom 2560）、
  P5-ex（2686）、P8-battery（1767，图高 −264.8 = 压坏）；P7 图 ends 1557.8 vs Sätze 横线 1548（撞线）；
  P6-ex 仅余 17px。→ 须调栏高，非字号问题。
- 21.5 试跑第一轮无效（钳制把 21.5 抬回 22，输出与 22 完全相同）；修正后真 21.5 试跑
  （build10-trial215.log）与 22 完全相同的 P2/P5/P8 终点（换行驱动、非字号驱动）——21.5 与 22
  对适配无差别，故取 22（真阶梯下限），不取中间值。
- 22 + P8 20.5 试跑（build10-trial-final-sizes.log）：P8 battery 适配（ends 1484/1505），但图被压到 18.33px 高。
- 真实缺口（22 单位下）：P2 ~127px、P5 ~124px、P8 ~256px。栏高调整（"调整栏高"，任务书授权）：
  P2 ey dy+282 → dy+240（Rechnen 纸条墨迹实测 ends ~1778，新横线 1794 清出）；
  P5 ey 1780 → 1756（col-3 图 ends 1732.93，新横线 1744 清出 ~11px）；
  P7 阅读室图高 150 → 145（A2 流因 16.5pt 题干变长）；
  P8 battery 流底 1505 → 1555；wy 1600 → 1650（写作条 + 答案键整体下移，间隔仍 81px 如基线；键 ends ~2378 vs bottom 2560）。
- D1 另：`hh` 36 → 32（chip 高 30）。match_set 左栏 24 单位 = 18.0pt 未动（bslib4 固定值，校对未指摘）。

## 终版构建 build10（2026-11-10 晚）
- 命令同"构建命令"一节；build10.log：**零 FLOW OVERFLOW / HEAD TOO WIDE**。
- Flow 终点：P1-headline 1554/1828；P1-quiz 2523/2560；P2-ex 2332/2560；P3-ex 2041；P4-ex 2315；
  P5-ex 2441；P6-ex 2523（余 37px，全期最紧）；P7 A2 1278 / 图 ends 1541.8（Sätze 横线 1548，余 6.2px）/
  B1 1310 / B2 1306 / col3 1479；P8-battery 1395/1555，图高 140 完整，图 ends 1619.2 vs 写作横线 1636；
  P8-keys 2504/2560（余 56）。
- 交付物：print PDF 22,963,572 bytes，sha256 `ea41866fd6669f3cf3380c8c53d66ef3a0da4b30a6ccddee9b786711b112801b`；
  web PDF 2,043,235 bytes（<7MB），sha256 `7394de6113d9a045cdd871b1c01e5d9942f4bcebbcc9bd81fef0f87ba749f522`，
  文字层 50,180 bytes（基线 49,924）；`.text.md` 49,578 bytes，sha256
  `e7ba369b1ea94b747c062d9ecbaf802d937c694ec8ce80efeff838c190b26bae`，42,176 chars，591 entries，150 题。
  （基线 build9 SHAs 已废：print b7b6b8a2…09ce5d / web fc1a2052…85964 / text.md 88c0c0f6…）

## 三工具 + 冻结（build10，日志均在 scratch-de-fix）
- verify.py（verify10.log）：TOTAL 150；分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；
  级别 A2 69 / B1 67 / B2 14；题型 单选 52 / 完成句子 41 / 句型转换 11 / 判断对错 8 / 完形 8 / 造句 8 /
  词汇配对 12 / 翻译 4 / 对话补全 5 / 写作 1；编号连续；SVG 重跑后字节相同；§1.1 风格审计 True，
  无旧式 hex；8 金句各恰 2×；禁用词全空（含无 "Geisterspiel"）；页脚/页码行 8/8；P6 图柱 748/561/391；
  MUSTER 84 词；P8 最小字号 13.5 单位 = 10.125pt（≥9.75pt 下限）；其余版最小 11.625–12.75pt。
- occlusion_audit.py（occlusion10.log/json）：自测 OK（6 类植入全触发、干净对照静默）；**0 flags**。
- p8.py（p8extract10.log / p8compare10.log）：extract **150/150**；compare core-vs-itself
  **status: CLEAN, missing=[] extra_count=0 uncertain=[] keydiff=[]**。
- freeze（freeze10.log）：core-de 复制到 scratch 副本重跑 run.py，sha256 逐版比对：**8/8 字节相同**。

## D1 题干字号实测（check_d1_d5.py / check_stems.py / check_final.py）
方法：AST 提取全部 124 个 ex() 体，与 SVG 首行渲染匹配；6 处 24/21.5 单位的疑似命中经 debug
证实为共用题干首词的文章/三栏盒文字，真正题干行均在 22.0 单位。
**P1–P7 全部题干 22.0 单位 = 16.5pt**（10/10、14/14、18/18、14/14、18/18、18/18、12/12）；
**P8 全部 20 题 20.5 单位 = 15.375pt**（20/20，SOP §1.1 P8 让步 15.4pt，见 KIT §7/§8）。

## D2–D5 实测复核（SVG + .text.md）
- D2：P4 SVG 内 "Ligaphase" 2×（文章 "4. Spieltag der Ligaphase" + 译注）；.text.md 同。
- D3：P6 SVG 内 "Buße" 3×（文章 "lädt zur Buße" + 译注 + 练习 D 词框）；P6 Q97 填空
  "Der Buß- und Bettag lädt zur ___ ein" 现与文章直接对齐（旧文 "lädt ein zum Nachdenken" 不含答案）。
- D4：P1 含 "13. November"、"Deutschland traf in Belgrad auf Serbien"、"nur Kinder und 50 deutsche Fans"、
  "vor fast leeren Rängen"；旧句 "trifft Deutschland in Belgrad"、"Am Freitag (20.45 Uhr)" 已无；
  P7 工具箱整句已确认（去空白匹配，跨两行渲染）；P4/P5 全文无 "Serbien"。
  P1 KURZ & GUT "Serbien auswärts" 与 Q7 干扰项 "A. Serbien" 未动（无日期/时态主张）。
- D5：P3 新题干在位、旧题干已无、选项 A 在位；P8 答案键 42 = "42. A（市场比将临期早近两周开市）"。
- §8.1 注释词逐词计数（count_gloss.py / count-gloss.log，正文段内、屈折/可分动词拆分形计入）：
  P4：das Tor 2、der Spieltag 3、torreich 1（torreichste）、die Ligaphase 1、weiterkommen 1（kommen weiter）；
  P6：die Buße 1、das Kirchenjahr 2、der Verstorbene 1、der Friedhof 1、der Haushalt 1、die Einigung 1。
  11/11 均在正文出现。练习 D 词框与 P8 答案中的出现不计（任务书所指）。

## 文字层比对（pdftotext，build10）
- print vs web（默认模式）：同为 50,180 bytes，归一化后 41,779 字符，**字符多集相同，仅 P6 图表区
  token 顺序不同**（print："WAS INTERESSIERT DIE LESER? 读者最关心什么？ 44 % …"；web：标题的中文部分
  后移，与 "44 % 33 % 23 %" 汇合）。`-raw` 模式：**完全相同**（49,094 bytes，41,816 字符）。
- `pdftotext -bbox` 第 6 页：两 PDF 词位完全相同（标题 yMin 1063.4；"44" 在 1108.9 与 1405.3 处均同）——
  无渲染位移，是 poppler 布局分组启发式差异，文字内容相同。
- 基线 proof 轮的 print.txt/web.txt 在默认模式归一化下完全相同（41,682 字符），故默认模式的顺序差异
  是本次重渲新出现的（练习区变长改变了分块），非内容改动。
- 新 print vs 基线 print token 多集差：仅预期的 5 处改动 + pdftotext 分词噪声（如 "德语周报 VOL.4"
  基线按字符切分、新版按词切分；"— 第 N 版 —" 分隔符切分不同）。无意外内容词。
- 结论：文字层实质一致（-raw 相同 + 字符多集相同 + 词位相同）；默认模式的 P6 图表区顺序差异已记入 KIT §6，
  供下轮校对知悉，不作内容差异。

## 全量重自查轮（SOP §8.4，2026-11-10 晚）— 零发现
- 全文精读：重导出 .text.md 42,176 字符逐行读完（P1–P8 全文，见上文逐页要点）；150 题逐题复核——
  依据：verify.py 注册表 150 题、编号连续、分版与题型分布与基线一致；除 Q42 题干改写外其余题目文本
  与 build9 字节相同（token 多集差证明），而 build9 已由第一轮独立校对逐题核过 150/150；
  Q42 重写后仅一解（A 为唯一时间跨度答案，B/C 非时间跨度），键与注记未变；P6 Q97 现由文章直接支持；
  P4 赛程表与 P5 周计划均无塞尔维亚场；P8 Q121 干扰项 "13. November"、Q123 干扰项 "13. November"
  均为合理干扰项（德甲回归 20 日、对荷兰 16 日，键未变）。
- 金句：8 句各恰 2×，逐字与原文一致（verify.py）；目录/交叉引用：P1 目录页码与各版一致；
  Sätze der Woche 出处页码与文章一致（P7 卡片目检）。
- §1.1 逐项：verify.py 风格审计 True；纸张/调色板/徽章/页边距/头条 40 字符（限 56）/P8 ≥9.75pt 均绿；
  题干字号见上（P1–P7 16.5pt、P8 15.375pt）。
- 8 卡看图：cards/p1-front.png … p8-uebungen.png 逐张目检——P1 新导语完整无溢出；P2 练习区完整、
  配对块落位、Rechnen 横线间隔清晰；P3 Q42 新题干无误；P4 "Spieltag der Ligaphase" 在位、赛程表
  仅 Mo 16.11. 荷兰场；P5 周计划从 11 月 16 日起、图注与练习横线间隔清晰；P6 图表 44/33/23 完整、
  Q100 落在页脚上方留空处；P7 工具箱新译注完整、图注与 Sätze 横线间隔 6.2px（视觉清晰）；
  P8 电池题完整、1905 图 + 图注与写作横线间隔清晰、写作条 + MUSTER 清晰、答案键四栏完整、
  均在页脚上方结束。**8/8 目检零发现。**
- 教训：`difflib.SequenceMatcher`（autojunk=False）在 ~41k 字符上极慢（一次跑 >4 分钟被 SIGTERM 杀掉，
  会话 proc_0be49005bf36）；改用词级或线性扫描。

## 待办（本轮内已完成，留档）
- [x] 8 卡目检 — 零发现
- [x] 全文精读 + 150 题复核 — 零发现
- [x] KIT 更新（§2 塞尔维亚行、§5 交付物、§6 门控 build10、§7 D1–D5 + 更正 "same as FR"、§8 P8 让步）
- [x] 本日志更新
- [x] 向 parent 汇报（逐条修复 + 证据 + D4 偏差 + 文字层观察）
- P1-headline col2 y=1494/1828（余 334）；P1-quiz col3 y=2521/2560（余 39）；P2-ex col3 y=2323/2560（余 237）；
- P3-ex y=1912（余 648）；P4-ex y=2268（余 292）；P5-ex y=2300（余 260）；P6-ex y=2214（余 346）；
- P7 A2/B1/B2 y≈1266/1480（余 ~214），P7 图 ends 1529.5（Sätze hline 在 1548，余 18.5）；
- P8-battery col3 y=1345/1505（余 160）；P8-keys y=2328/2560（余 232）。
