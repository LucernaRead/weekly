# W47 ko 家庭独立重校记录（第三轮，PROOF-NOTE-3）

- 任务：SOP §8/§8.4 独立重校（第三轮），目标语 ko，core-ko + fan-out 10 版（ko-de/en/es/fr/it/ja/nl/pt/ru/zh-tw），共 11 版。校对员与建造者、第一轮校对员、第一轮修复者、第二轮校对员、第二轮修复者均不同，满足“另派”要求。只校对，不修复、不重建、不 commit、不 push、不跑 lint；只读 `production/2026-w47/` 内 ko 家生产文件。
- 校对日期：2026-11-12。刊期：2026 年 11 月 16–22 日，VOL.4。
- 磁盘：开工 95G 已用 / 55G 可用；收尾 95G 已用 / 55G 可用（<100G 门限，未触发停手）。
- 运行环境：`~/workspace/weekly-git/tools/venv/bin/python`。
- 前置阅读：SOP.md 全文（重点 §8/§8.4）、第二轮记录 `scratch-reproof2-w47-ko/PROOF-NOTE-2.md`、第二轮修复记录 `scratch-fix2-w47-ko/FIX-LOG-2.md`、第一轮修复记录 `scratch-fix-ko/FIX-LOG.md` 已全文读完；`weekly-git/AGENTS.md` 已读。

## 结论：(a) 干净 —— 零问题轮次

本轮从头全量重校，**发现 0 条**（无 MAJOR、无 MEDIUM、无 low）。第二轮 3 条（R2-1 MEDIUM + R2-2/R2-3 low）已全部核实修复到位（见“R2-1/R2-2/R2-3 修复核实”）；第一轮 5 条（F1–F5）已全部核实仍在版、无回归（见“F1–F5 复核”）。机械门禁 87 门全部 RC=0，按页 inventory 11 版全部 150/150、配对词 16/16。按 SOP §8 与 `weekly-git/AGENTS.md`“一轮独立重校零问题 + 几何遮挡审计零 flag 方可入库”的门槛，**本期 ko 家庭达到定稿条件**。

发现总数与严重度分布：**0 条**。第一轮 5 条修复验证：5/5 通过，0 回归；第二轮 3 条修复验证：3/3 通过，0 回归。

## 每版指纹（本次校对的文件，与 FIX-LOG-2 SHA 表逐版一致）

| 版 | text.md（字节 / SHA 前 12） | web PDF（字节 / SHA 前 12） | print PDF（字节 / SHA 前 12） |
|---|---|---|---|
| ko-zh-cn（core-ko） | 35,456 / `044001ac2f14` | 4,226,882 / `ac97b284fe16` | 45,181,315 / `7248314a5ae2` |
| ko-de | 36,012 / `4f6945d36115` | 3,956,937 / `4b1a54ce3040` | 43,754,319 / `8d217beb86ae` |
| ko-en | 35,781 / `f5e5bb278704` | 3,951,102 / `59bb38b0bc77` | 43,748,448 / `f10c5065bb5b` |
| ko-es | 36,065 / `a24bd9ffaa09` | 3,955,583 / `e1ae9fcc033b` | 43,752,821 / `637bcb1b1b22` |
| ko-fr | 36,131 / `661b391e24d3` | 3,954,158 / `dc933cc18cfe` | 43,751,522 / `1f6add20c07d` |
| ko-it | 36,068 / `4e7926e4ffa7` | 3,949,052 / `f0efba8a29ab` | 43,746,645 / `edfda4420e46` |
| ko-ja | 36,275 / `be048d7d4164` | 4,373,107 / `f9bb1d3a3929` | 50,279,548 / `f8c7508f9be8` |
| ko-nl | 35,904 / `55abafb3fee8` | 3,950,671 / `5f84566e41de` | 43,748,187 / `662eb3e3e3f2` |
| ko-pt | 35,935 / `059743986a52` | 3,956,638 / `e4028beb886a` | 43,753,908 / `70047cd27b8d` |
| ko-ru | 38,039 / `e439f6a60a13` | 4,126,934 / `ee36501822d1` | 43,926,367 / `4c0c80b6b6bf` |
| ko-zh-tw | 35,487 / `841a26658cb7` | 4,323,857 / `189fde45fc9e` | 45,219,886 / `65118aabee9f` |

- 目录核对：盘上 fan-out 10 个 + core-ko，共 11，与任务清单一致，无多无少。每版均含 print PDF、web PDF、text.md、8 个 SVG、8 张整页 PNG。
- KIT 核对：11 版 WEEKLY-KIT.md 所载印/网/text 三组完整 SHA-256 与盘上实测逐版一致；字节数（千分位格式）逐版一致；标记 `fix rebuild 2, 2026-11-12`：ru/es 各 3 处、其余 9 版各 1 处，`fix rebuild 2026-11-12` 各 3 处，与 FIX-LOG-2 一致。

## R2-1/R2-2/R2-3 修复核实（全部通过）

### R2-1 —— text.md 导出丢题已修（11 版全家）

- **导出器**：11 份 `textmd.py` md5 均为改后值 `00d8f52d96ecad396cbc03603d98fa9b`（改前 `bc6394a3…` 已无残留）。
- **逐项在版（core-ko 行号；其余 10 版同法逐版核对，见下表）**：P2 D 块 L293 独立行 `김치의 날`（Q26）；P4 D 块 L509 `준플레이오프`、L511 `플레이오프`、L513 `한국시리즈`（Q61–Q63）；P8 B 块 L865 Q121 题干整行、L875 Q126 题干整行；P8 F 块 L917 独立行 `김치의 날`（Q142）；P6 对照表行标签 `김장비용`（L663 附近，行标签 + `10월 16일 가격` + `11월 9일 조사 199,456원` 三行齐全）。
- **按页 inventory 复核表**（重校员同款方法，复用 `scratch-reproof2-w47-ko/inventory_textmd.py` / `inventory_textmd2.py` / `inventory_match.py`；结果存 `inventory-all.log`）：

| 版 | 全书查（150 项） | 按页查（150 项） | 配对词独立行（16 项） | 7 编号项 + P6 行标签逐块核对 |
|---|---|---|---|---|
| ko-zh-cn（core-ko） | 150/150，0 缺 | 150/150，0 缺 | 16/16，0 缺 | 全过 |
| ko-de | 150/150 | 150/150 | 16/16 | 全过 |
| ko-en | 150/150 | 150/150 | 16/16 | 全过 |
| ko-es | 150/150 | 150/150 | 16/16 | 全过 |
| ko-fr | 150/150 | 150/150 | 16/16 | 全过 |
| ko-it | 150/150 | 150/150 | 16/16 | 全过 |
| ko-ja | 150/150 | 150/150 | 16/16 | 全过 |
| ko-nl | 150/150 | 150/150 | 16/16 | 全过 |
| ko-pt | 150/150 | 150/150 | 16/16 | 全过 |
| ko-ru | 150/150 | 150/150 | 16/16 | 全过 |
| ko-zh-tw | 150/150 | 150/150 | 16/16 | 全过 |

### R2-2 —— ko-ru `조사하다 = обследовать`（通过）

- 源码：`2026-w47-ko-ru/content12.py:45`（P1 词表）与 `:174`（P2 词注）两处均为 `조사하다 = обследовать`；`content*.py` 全家 `опрашивать` 0 处。
- text.md：`обследовать` 2 处、`опрашивать` 0 处。
- 印/网 PDF（pdftotext）：`обследовать` 各 2 次、`опрашивать` 0 次（印 59,178 字节、网 59,178 字节，plain 提取逐字节一致）。
- 目检：ru P1 词注框与 P2 词注框在半分辨率整页图上均见 `조사하다 = обследовать`，无溢出、无重叠。

### R2-3 —— ko-es P2 栏目标题 `과`（通过）

- 源码：`2026-w47-ko-es/content12.py:166` 的 `p.band` 行为 `레벨 A2　김장비용과 김치의 날, 한능검　Coste del kimjang, Día del Kimchi y examen de historia`，与 core-ko 同行及其他 9 版一致。
- text.md：11 版 band 行均为 `김장비용과 김치의 날, 한능검`（各版读者语译文后缀不同）。
- 印/网 PDF：ko-es P2 band 行各出现 2 次（栏目条 + 目录行），逗号旧式 0 次；半分辨率 P2 整页图目视确认 band 行为 `과` 式。
- 唯一残留 `김장비용, 김치의 날` 字符串在 ko-es `WEEKLY-KIT.md:92` 的 Fixes log 行内，是对旧式的引用记录（修复说明本身），非正文内容，不作缺陷。

## F1–F5 复核（全部通过，0 回归）

### F1 —— 6 道新题（逐版核实，全部通过）

- 印 PDF 全文核实（11 版）：新题干 Q12/Q13/Q47/Q102 各出现 1 次；Q22/Q74 题干各 2 处（正文 + 题面）；旧重复题干除 P1 Q8/Q9/Q10 首次出现保留外 0 残留。
- 答案键逐版核对（`p8.py extract`，11 版各 150 号齐全）：12. A / 13. A / 22. 1.8 / 47. A / 74. 8 / 102. A，11 版一致。
- 6 道新题事实复核（逐题对照同页文章原文）：
  - Q12：P2 正文“지난해 11월 상순 평균 219,071원보다 9.0% 내렸어요. 평년보다도 13.4% 낮아요”——答案 A 正确。算术：199,456/219,071 = 0.9105，降 9.0%（四舍五入）✓。
  - Q13：P2 正文“하나로마트 18곳에서 김장 재료 6종을 최대 반값에 팔아요”——答案 A（6종）正确。
  - Q22：P2 正文“고춧가루는 1.8%, 무는 5.6% 내렸어요”——答案 1.8 正确。
  - Q47：P4 正文“통산 아홉 번째 우승이에요”——答案 A（아홉 번째）正确。
  - Q74：P5 正文“수험표를 잃어버리면 당일 아침 8시까지 시험장 관리본부에 신고하면 다시 받을 수 있어요”——答案 8 正确。
  - Q102：P7 A2 栏正文“김치의 날은 2020년 2월에 법으로 정한 기념일이에요”——答案 A（2020년 2월）正确。

### F2 —— P1 导语末句「다른 날의」（11 版通过）

- 源码与 text.md：P1 句（`content12.py:40`，text.md L29）与 P5 句（`content56.py:19`，text.md L537）均在版；旧句 11 版均为 0 次。
- 核实方法说明：plain pdftotext 因双栏交错切断该句，连续字符串查不到——改以 SVG 文本流顺序核实：P1 式 `이번 주의 다른 날의 조치가 아니에요` 每版 1 次、P5 式 `이번 주(11월 16~22일)의 다른 날의 조치가 아니에요` 每版 1 次，共 2 次，与 PROOF-NOTE-2 一致；ru P1 半分辨率图上该句完整可见。

### F3 —— core-ko P8 Q125 注释「头轮山」（通过）

- core 印 PDF：`125. B — 头轮山林业厅预报峰值11月11日`；全家「杜鹃山」0 残留；其余 10 版 Q125 注均为 Duryunsan/頭輪山/Турюнсан，峰值 11 月 11 日，与 P3 正文「두륜산 절정은 11월 11일이었어요」一致。

### F4 —— P7 金句第 6 条 7 版过去时（通过）

- 印 PDF P7 核实：en “It reported the results with the scores.” / fr “Il a rapporté les résultats avec les scores.” / es “Informó los resultados con los marcadores.” / it “Ha riportato i risultati con i punteggi.” / pt “Reportou os resultados com os marcadores.” / nl “De krant vermeldde de uitslagen met de scores.” / ru “Газета сообщила результаты вместе со счётом.”——7 版均为过去时，旧祈使句 11 版均为 0 次。de（过去时被动）、ja（plain form）、zh-cn/zh-tw（无时态标记）未动，正确。

### F5 —— ko-es P1 顶行标语（通过）

- ko-es 印 PDF P1 顶行含「한국 사람이 읽는 한국어를 읽어요」；旧标语「Aprende coreano con las noticias más recientes」0 残留；其余 10 版顶行一致。

## 第三轮全量重校（新发现：0 条）

### 文本通读

- core-ko text.md 全文已读（P1–P8，951 行）。练习登记 TOTAL 150；P1:10、P2:18、P3:18、P4:18、P5:18、P6:18、P7:12、P8:38。
- P8 答案 1–150 逐题复核（独立重算）：源码 AST 提取 150 项登记键 vs `p8.py extract` 印版键，**149/150 逐字一致**，唯一差异为 Q150：源码登记键为“（开放题，范文如下）”，印版键为“✓”（H 写作题范文标记，属正常渲染，非缺陷；与第二轮一致）。另按题面/原文/图表独立重算全部 150 道答案：**答案字母/填空全部正确**，编号连续 1–150。核对要点：P1 Q2 键为「김장」（「이번 주는 김장이 한창인 주간이에요」）；P6 判断题 Q97–Q100 印版键为文字（틀리다/맞다/틀리다/맞다），与题意一致；P3 配对 Q43–Q46 键 b/a/d/c（내장산→웨더아이 11/11、월출산→산림청 11/9、두륜산→산림청 11/11、설악산→실제 관측 10/16），各释义仅一解；P8 B 区 Q121（551,864 名，A）与 Q126（1차전 kt 8대 7 胜利，A）为 P8 版内重测题，答案正确。全 150 题键表见 `p8key-compare-core.log`。
- P7“本周金句”8 条均逐字出自本期文章（SOP §4），已逐条核对原文出处（P1/P2/P3/P6）；P7 易错诊所 4 条（김치의 날 띄어쓰기、삼성는→삼성은、담궈요→담가요、날예요→날이에요）均正确。
- 11 版讲解层全部读完（core text.md 全文 + 10 版与 core 的 diff 逐行读完，共约 360 行/版）：词汇注释、标题译文、提示语、P8 E 区译文、P7 金句译文均正确；韩文核心层跨版一致（除下述“全部”徽章导出差异外，diff 中无韩文正文差异）。
- 摘要：11 版均有 `ABSTRACT.txt`（单行、无 ASCII 双引号、事实正确、含刊名、分级 A2–B2、150 题、读者母语撰写；全文已读）。
- 刊头与页脚：11 版刊头结构一致（VOL.4 제4호 / Lucerna / 한국어판 VOL.4 수능 김치의 날 한국시리즈 / 副标），中间标语按读者语翻译，均正确；core 页脚 8 版均有「正文韩语　讲解简体中文」。

### 事实核验（本轮复核第一轮/第二轮结论，未发现新事实错误）

- 第一轮/第二轮事实核验逐项复核（韩国大赛 5 场比分与 4–1、12 年首冠、通算第 9 冠；CSAT 2027 报考 551,864 人、85 考区、1,312 考点、08:40–17:45、08:10 前入场、成绩 12/11；泡菜成本 199,456 韩元、降 9.0%/平年 13.4%、白菜 54,980 韩元降 26.5%、辣椒粉 −1.8%、萝卜 −5.6%；山火注意期 11/1–12/15；红叶预报内藏山 11/4、月出山 11/9、头轮山 11/11、雪岳山实测 10/16；韩史检定第 81 届 11/28、费用 27,000 韩元、报名/取消/照片/准考证/成绩节点；FC 首尔第 33 轮提前夺冠、36 轮 11/21–22、最终轮 12/5–6；泡菜日 11/22、2020 年 2 月法定、UNESCO 2013；LA 泡菜节 11/21、首尔折扣 11/5–11、Hanaro Mart 18 店 6 种食材；WiKim 庆典 11/20 周五 14:00–17:30 aT 中心——仍按 KIT builder 来源，未由我独立核实，不作缺陷；星期与报纸全部一致）——本轮通读未发现与之冲突的新事实错误。
- 日期/星期：`date` 逐日核验——11/16 周一、11/18 周三、11/19 周四、11/20 周五、11/21 周六、11/22 周日、11/24 周二、11/28 周六、12/5 周六、12/6 周日、12/11 周五、11/4 周三、11/7 周六、11/8 周日、11/9 周一、11/10 周二、11/11 周三、10/16 周五，全部与正文一致。
- 算术：199,456 vs 219,071 降 8.95%→9.0% ✓；54,980 vs 74,800 降 26.5% ✓；551,864 + 2,310 = 554,174（去年报考数，未在正文印出，仅内部一致）✓。

### 版式目检

- 重渲两版改动页半分辨率逐页看过：ko-ru P1（P1 词注 `조사하다 = обследовать`）、ko-ru P2（P2 词注同）、ko-ru P8（答案 1–150 齐全，键抽查 12/13/22/47/74/102/121/125/126/141–144 均正确）、ko-es P2（band 行 `과` 式、D 块 25–28 齐全）：无溢出、无重叠、无压页脚、无豆腐块、无截断句。
- fan-out 其余页面未逐像素看图，改以 SVG 文本提取 + 遮挡审计 + spill/boxtitle/edge 三门覆盖：韩文正文与 core 一致，讲解层字符串已全文读过，几何门禁 0 缺陷（见下）。

## 观察（非缺陷，记录备查）

- **答案字母连号（沿用第一轮/第二轮观察）**：P1 Q7–Q10 全 A；P2 A 区 Q11–Q15 全 A；P8 A 区 Q113–Q120 全 A。答案均正确，不作缺陷。
- **闪电问答标题标点（沿用第一轮/第二轮观察）**：11 版均两句并列无句号（例 en “Read page 1, pick the right answer Answers on page 8”）。印为单行小字标题，可接受。
- **“全部”徽章 text.md 行差异（更正第二轮观察）**：PROOF-NOTE-2 称“de/en/es/fr/it/ja/nl/pt/zh-tw 9 版无此行”，本轮实测为——core 与 zh-tw 有「全部」行（L119）、ja 有「すべて」行、ru 有「Всё」行；仅 de/en/es/fr/it/nl/pt 7 版 text.md 无此行。11 版印版 P1 目录徽章齐全（R2 半分辨率图核实；本轮 ru P1 图亦见「Всё」），仅为导出口径不同，非缺陷。
- **core 摘要措辞（沿用第一轮/第二轮观察）**：“适合用韩语学韩语的你搜索韩语阅读周报”一句别扭、带 SEO 堆砌感；事实正确，不作缺陷。
- **P7/P8 共用一张泡菜制作照**：不同裁切，均 CC0（Anattadairy），两处均注明出处；属复用，非缺陷。
- **P5 右下、P6 右上留白**：正常版面空白，非缺陷。
- **WiKim 庆典**：见事实核验节——未独立证实，不作缺陷。
- **P6 10月16日 배추单价 5,557원**：正文（content56.py:120）与 Q94 键 A 一致，但 KIT 事实来源节未单列该数出处（KIT 只载 aT 11月9日调查总价与分项价）；未发现与之矛盾的证据，两轮前序校对亦通过，不作缺陷，仅记录备查。
- **编辑按语译文附加邀请句**：en/de/fr/es/it/pt/nl/ru/ja/zh-tw 10 版 P7 编辑按语译文在忠实转述“示例信、截稿前无来信、顺延 VOL.5”之外，各加一句投稿邀请（如 en “Send us yours — two sentences in Korean!”）；属讲解层附加邀请，与各版“당신은? 写两句寄来”一致，披露内容完整，不作缺陷。
- **ko-ru 拉丁标题字体问题（任务指定不重报）**：ko-ru 版拉丁标题用 Noto Sans 而非 Newsreader，系已知的跨家 D5 系统性问题，另有跨家工人统一修 svglib.py；ko-ru 版内容已照常全校，本轮未将其计为发现。
- **freeze baseline 7/8（任务指定不重报）**：P1 已知解释器 artefact（大字 "1" 185 vs 183pt，文本多重集差 0），D5 已裁定非缺陷；本轮任务为只读重校，未重建生产文件，故 freeze baseline/diff 未重跑，未将其计为发现。
- **FIX-LOG 裁定不修项**：近似重复题（Q29、Q67/Q92/Q120/Q121、Q68/Q86、Q33/Q89/Q110、Q15/Q31）按裁定不动，本轮未重报。

## 机械门（逐版）

`run_gates3.sh`（本 scratch 目录，只读生产文件）共 87 门，**全部 RC=0**：core 7 门（无 p8-compare，core 为参照基准）+ 10 个 fan-out 各 8 门。逐版汇总：

| 版 | D5 census | 引号 defective | 遮挡 flag | p8 extract | p8 compare | spill | boxtitle | edge |
|---|---|---|---|---|---|---|---|---|
| ko-zh-cn（core） | PASS（latin=0、cyrillic=0、curly=0、noto=0） | 0 | 0 | 150/150 noted | —（基准） | 0 SPILL / 49 boxes, 323 OBSERVE | 63 titles, 0 DEFECT | 8 页, 0 TOUCH / 0 NEAR |
| ko-de | PASS（0/0/0/0） | 0 | 0 | 150/150 noted | CLEAN, keydiff [137,138] | 0 SPILL / 49 boxes, 358 OBSERVE | 73 titles, 0 DEFECT | 0 / 0 |
| ko-en | PASS（0/0/0/0） | 0 | 0 | 150/150 noted | CLEAN, keydiff [137,138] | 0 SPILL / 49 boxes, 352 OBSERVE | 73 titles, 0 DEFECT | 0 / 0 |
| ko-es | PASS（0/0/0/0） | 0 | 0 | 150/150 noted | CLEAN, keydiff [137,138] | 0 SPILL / 49 boxes, 358 OBSERVE | 73 titles, 0 DEFECT | 0 / 0 |
| ko-fr | PASS（0/0/0/0） | 0 | 0 | 150/150 noted | CLEAN, keydiff [137,138] | 0 SPILL / 49 boxes, 360 OBSERVE | 73 titles, 0 DEFECT | 0 / 0 |
| ko-it | PASS（0/0/0/0） | 0 | 0 | 150/150 noted | CLEAN, keydiff [137,138] | 0 SPILL / 49 boxes, 359 OBSERVE | 73 titles, 0 DEFECT | 0 / 0 |
| ko-ja | PASS（0/0/0/0） | 0 | 0 | 150/150 noted | CLEAN, keydiff [137,138] | 0 SPILL / 49 boxes, 348 OBSERVE | 63 titles, 0 DEFECT | 0 / 0 |
| ko-nl | PASS（0/0/0/0） | 0 | 0 | 150/150 noted | CLEAN, keydiff [137,138] | 0 SPILL / 49 boxes, 357 OBSERVE | 73 titles, 0 DEFECT | 0 / 0 |
| ko-pt | PASS（0/0/0/0） | 0 | 0 | 150/150 noted | CLEAN, keydiff [137,138] | 0 SPILL / 49 boxes, 359 OBSERVE | 73 titles, 0 DEFECT | 0 / 0 |
| ko-ru | PASS（0/0/0；noto_sans_elements=1107，俄语讲解层预期值） | 0 | 0 | 150/150 noted | CLEAN, keydiff [137,138] | 0 SPILL / 49 boxes, 365 OBSERVE | 73 titles, 0 DEFECT | 0 / 0 |
| ko-zh-tw | PASS（0/0/0/0） | 0 | 0 | 150/150 noted | CLEAN, keydiff [138] | 0 SPILL / 49 boxes, 335 OBSERVE | 63 titles, 0 DEFECT | 0 / 0 |

- **D5 census**（`scratch-d5-plan/mechanism/d5_census.py`）：11 版全部 PASS——`D5_latin_in_cjk=0`、`D5_cyrillic_in_cjk=0`、`curly_in_cjk=0`，弯引号 U+201C/U+201D/U+2019 在 11 版全部 SVG 与 text.md 中出现 0 次。ko-ru 有 1107 个 Noto Sans 元素，系俄语读者讲解层，符合预期。
- **引号普查**（`scratch-gatefix-u201c-ru/census_quotes.py`）：11 版全部 0 defective。
- **Occlusion audit**（`tools/occlusion_audit.py`，含 selftest：6 类 planted 全部触发、clean 对照静默）：11 版 **0 flag**。
- **p8.py extract/compare**（`--total 150`）：11 版 extract 各 150/150 noted；10 版 compare 全部 **CLEAN**（missing=[]，extra=[]，uncertain=[]；keydiff：9 版 `[137, 138]`、zh-tw `[138]`——P8 E 区翻译题合法翻译差异；ko-ru 的 137 提取为 “22 ноября”系 p8.py 提取器在 `—` 处切分 artefact，SVG 原行完整）。
- **spill_sweep / boxtitle_check / pdf_edge_scan**：11 版全部 0 SPILL / 0 DEFECT / 0 TOUCH（boxtitle：core/ja/zh-tw 63 titles、其余 73 titles；edge：8 页 0 NEAR）。
- **文字层**：11 版印/网 PDF pdftotext（plain）逐字节一致（ko-ru 网版 `-layout` 提取仅少 1 字节空白字符，为 PROOF-NOTE-2 已记录的 ru 已知现象，不影响文字层门禁）；印/网 PDF 字节数与 FIX-LOG-2 SHA 表逐版一致（见上表）。
- **freeze 未重跑**：本轮任务为只读重校，未重建生产文件，故 freeze baseline/diff 未重跑；沿用 FIX-LOG-2 改后值（baseline 7/8 P1 artefact、diff +0/−0、新增 CJK 0）。

## 工作底稿与覆盖口径

- 工作文件：`scratch-reproof3-w47-ko/`（PROOF-NOTE-3.md、run_gates3.sh、inventory_textmd.py、inventory_textmd2.py、inventory_match.py、inventory-all.log、p8key-compare-core.log、fingerprints3.txt、mech/ 门禁 JSON 与日志、pdftext/ 印网提取文本、diffs/ 10 版讲解层 diff、half/ 4 张半分辨率目检图）。
- 文本覆盖：core text.md 全文（951 行）；10 版讲解层全文（与 core 的 diff 逐行读完）；P8 答案 1–150 逐题复核（源码登记键 vs 印版键逐项比对 + 题面/原文独立重算）；F1–F5 逐版在印 PDF 全文核实；text.md 与印版一致性按源码 150 项逐项按页核对（R2-1 同款方法）；ABSTRACT 11 版全文读完；KIT 11 版 SHA/字节数逐版核对。
- 图像覆盖：ko-ru P1/P2/P8、ko-es P2 半分辨率（4 页）；fan-out 其余页面以 SVG 文本提取 + 几何门禁覆盖。
- 未做：不修复、不重建、不 commit、不 push、不跑 lint、不跑 freeze、不碰其他周；未动 production/2026-w47/ 与 hidden_files/w47/ 之外的任何文件；未改任何生产文件（全程只读，门禁输出均写本 scratch 目录）。
