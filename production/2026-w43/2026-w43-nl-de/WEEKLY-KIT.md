# De Lucerna VOL.1 — NL × DE 版（荷兰语正文 + 德语讲解）制作记录（WEEKLY-KIT）

版本：De Lucerna · Niederländische Wochenzeitung VOL.1（NL 正文 × DE 讲解）
周次：2026-10-19（一）至 2026-10-25（日），与核心版同周
定位：Lucerna 多语周报矩阵中的 **NL × DE** 一格：正文荷兰语（目标语），讲解层全部德语（读者母语）。与核心版（NL × ZH-CN）同一内容骨架，讲解层按读者母语整体重写。
构建目录：`hidden_files/weekly-report-nl-de-build/`（核心版 `weekly-report-nl-build/` 的副本改写；核心版目录未动）
交付目录：`files/weekly-report-nl-de/`（svg/ 8 页、cards/ 8 张、印刷 PDF、网络 PDF、本文件）
状态：构建方完成 + 几何审计通过（见 §九），待独立校对。本文如实记录，不预支「已通过」。

---

## 一、规格（同核心版/同 SOP）

版面 1950×2700，8 页（4 的倍数），4 栏，暖象牙底 #f7f1e2，深橄榄点缀，栏目头双语（荷兰语 + 德语）。本版可见字符 **35,636（不含空格）/ 41,970（含空格）**（提取 8 个 SVG 全部文本元素汇总；核心版同口径 29,851 / 35,308——DE 版较大，源于德语讲解层）。

## 二、配对与页眉页脚（实测原文）

- P1 配对徽章（砖红 #a4553a、粗体、独立成行，位于头条黑带之下、栏目头之上）：**「NIEDERLÄNDISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER」**（20pt 居中，实测宽 1,025px，上下各留 12px+，渲染目检无接触）。
- 页脚左（每页）：**「De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.1 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH」**；页脚右：**「Seite N von 8」**。
- 报头沿用核心版 **De Lucerna**（荷兰语带冠词，符合 SOP 冠词规则）。
- P1 顶部通栏中行改德语 **「ELKE WEEK IN HET NEDERLANDS · JEDE WOCHE AUF NIEDERLÄNDISCH」**（见 §七裁定 2 的碰撞修复）。

## 三、结构（与核心版逐页一致）

| 页 | 栏目（荷 + 德） | 内容 |
|---|---|---|
| P1 | HET NIEUWS · SCHLAGZEILE | 头条「Een volle week」；趋势榜（源行改德语，见 §七裁定 3）；数字周；IN DEZE EDITIE · INHALT；本周词；短讯三则；DE WEEK OP TV；Blitzquiz（题 1–10） |
| P2 | LEVEN · LEBEN | 冬令时特稿 + 时间卡四张（德语等值说法）+ 读者角提示（德语） |
| P3 | CULTUUR · KULTUR | DDW + 秋假博物馆；两图 |
| P4 | SPORT · SPORT | 欧战周 + 周日双赛；1912 国家队图 |
| P5 | JONGEREN · JUGEND | ADE 30 年 + Hanslers + Robinson（开播预告） |
| P6 | VERDIEPING · VERTIEFUNG | Wristler 图表深读（条长与核心版同源数据）+ 正反框 |
| P7 | TAAL · SPRACHE | 三级工具栏 + PAS OP! · FEHLERKLINIK + 本周词 + 读者来信（本地化，见 §7）+ 本周句（德语译文）+ VOL.2 预告 |
| P8 | TOETS EN ANTOORDEN · TEST UND ANTWORTEN | 综合卷（题 113–150）+ 全部 150 题答案（德语简析） |

## 四、练习与答案（与核心版逐项对账）

练习 **150 题**，与核心版逐项编号、页、级别、题型全等：A2 42 · B1 76 · B2 32；每页 10/18/18/18/18/18/12/38。题型分布与核心版一致（完成句子 66 · 单选 45 · 完形单选 13 · 词汇配对 8 · 造句 7 · 判断对错 6 · 翻译 4 · 写作 1）。作文范文恰 **87 词**（`model words: 87` 程序断言）。

**冻结对账（程序化 registry diff，核心版 vs 本版）**：150 项 page/level/type 全等；**key 差异仅 3 项**（下表，均为任务书允许的读者语言项）；其余 key **逐字节同核心版**；note 差异 141 项 = 全部译为德语，另 9 项 note 本为语言中立（数字/公式，如「03:00 → 02:00」「kwart over twee = 2:15」）核心版即无中文、保持不变。

| 题号 | 核心版 | 本版 | 说明 |
|---|---|---|---|
| 137 | key 为荷兰语答案句 | key = 德语 „Am Sonntag geht die Uhr zurück: eine Stunde länger schlafen!"，note 德语 | NL→读者语方向，译文题按 SOP 重瞄准 |
| 138 | key 为荷兰语答案句 | key = 德语 „Dein Telefon und dein Computer stellen die Zeit von selbst um."，note 德语 | 同上 |
| 139 | 题面荷兰语→中文，key 为荷兰语句 | 题面改德语 „Die Dutch Design Week ist in Eindhoven. → ___"，**key 保持荷兰语 „De Dutch Design Week is in Eindhoven." 逐字节不变** | 读者语→NL 方向：只改题面语言 |
| 140 | 同上结构 | 题面改德语 „Am Sonntag habe ich eine Stunde länger geschlafen. → ___"，**key 保持荷兰语 „Zondag heb ik een uur langer geslapen." 逐字节不变** | 同上 |
| 150 | registry 行为中文讲解 | 改为德语 apparatus „(Offene Aufgabe — Mustertext unten)" + note „Mustertext in Abschnitt H auf dieser Seite (87 Wörter)"；范文（荷兰语正文）冻结 | 写作题讲解行按读者语言 |

**#139/#140 特别核验**（吸取 NL×EN 版校对教训：其构建方曾误印题面而非荷兰语答案）：本版构建后由 registry diff 程序化证实两题 key 与核心版**逐字节相同**，且在 P8 渲染图上目检复核（„139. De Dutch Design Week is in Eindhoven." / „140. Zondag heb ik een uur langer geslapen."）。

构建方抽查重解 ≥30 题与讲解一致性（答案与核心版同源、核心版已经独立校对；此处核对德语简析与 key/正文事实相符）：P1 数字题（9 天/25 日/30 年/2.500 人）；P2 配对 25–28（b/a/d/c 与词义逐项对）；时间题 16–18（kwart over twee / half drie / kwart voor drie）与 half-drie 陷阱简析；P3 完成时 40–43（hebben/zijn 分工：heeft gemaakt / zijn gegaan / heeft gezien / zijn gekomen）+ #44「9 天」+ #46 算术 19,50×2+32,50=71,50；P6 图表题 83–87：301.000+246.000=547.000、750.000−547.000≈203.000（标 gerundet）、60.500÷6.600≈9,2 → „gut 9 Mal"；#89–92 与正文（只有意大利人均更高/16 国/方向难记/eine feste Zeit）；造句 98–100 词序简析（zoeken 第二位、alleen 提前、trennbares Präfix terug 句末）；P7 时间 101–104（3:15/3:30/half vijf=4:30 Fangfrage/Oktober zurück）；翻译 137–140（见上表）；配对 141–144（d/c/b/a）；写作 150 范文 87 词。

## 五、SOP 合规清单

- [x] 页数 8（4 的倍数），1950×2700，4 栏，暖象牙 + 深橄榄
- [x] 趋势源：同核心版（荷兰生态本周实测热度；内容骨架冻结）
- [x] 红线：无国际政治（同核心版，骨架冻结）
- [x] 讲解层**全德语**：释义、语法讲解、指令、栏目头注、图表注、P7 门诊注、读者角注、**全部 150 条答案简析**均为完整德语（非「中文为主加一行德语」）
- [x] 配对徽章上 P1（§二原文）+ 页脚每页标注配对
- [x] 每题级别徽章；A2→B2 递进同核心版
- [x] ~150 题（实 150），统一编号，P8 按页分组答案 + 德语简析；答案括号前空格（半角）：程序扫描 registry note——全角括号 0、无空格粘连「(」0
- [x] 图片 6 张与核心版**逐字节相同**（SVG 内嵌 payload 逐页比对全等：westertoren P1、zakhorloge P2、kinderdijk + herfstbos P3、elftal1912 P4、gracht P5）；署名保持荷兰语、与核心版一致（Foto: Wim van Rossem / Anefo, Nationaal Archief — CC0 等）
- [x] P7 本周句：8 句荷兰语原句与源文章逐字一致（空格归一化计数：每句在全文恰出现 **2 次**，核心版同为 2 次）；德语译文与 (Pagina N) 页码标对应源页
- [x] 最终 SVG 中文字符 = **0**（逐页扫描实测）
- [x] 中间语术语：全文（报纸/KIT/构建代码）**0 次**；构建代码中核心版的同名方法已按同矩阵先例改名为 `note_line` 注解线
- [x] 印刷承诺：P7 VOL.2 预告为冻结荷兰语正文（与核心版同字，VOL.2 兑现义务不变：11 月 1 日 Robinson 开播追踪、欧战结果、ADE/DDW 收官、真实读者信 + P8 最佳写作）

## 六、读者来信本地化（§任务书第 8 条）

核心版示例信人物为 Chen（北京）。本版按 NL×EN 版先例本地化为德国读者：**Emma（Berlin）**，信件荷兰语正文冻结、仅人物名与城市替换（属人物设定，非正文改动）：«Hallo! Ik ben Emma en ik leer Nederlands in Berlijn. In oktober slaap ik één uur langer — net als jullie!» — Emma (voorbeeldbrief van de redactie)。信下讲解行改德语 „Beispielbrief der Redaktion. VOL.2: echte Briefe + die beste Arbeit von Seite 8!"（2 行，与核心版行数相同，框高不变）。

## 七、版式裁定（如实记录构建中四处处理）

1. **P1 副标题栏**：核心版为「中文标签 + 荷兰语主题词」混合行。整行改纯荷兰语主题词行 „NIEDERLÄNDISCH · VOL.1 · DE KLOK GAAT TERUG · ADE WORDT 30"——付费取舍：丢弃一个主题词（HERFSTVAKANTIE；该词仍见于头条、P2、P3 正文）。实测宽 1,385px（栏宽 1,820）。
2. **P1 顶部通栏中行碰撞修复（构建目检发现）**：初版中行 „…LESEN, WAS DIE NIEDERLANDE LESEN"（实测 881px，居中跨 535–1415）与右对齐周次行（起于 x=1411.5）发生字距碰撞（渲染中 „LESENWEEK" 粘连）。改短为 „ELKE WEEK IN HET NEDERLANDS · JEDE WOCHE AUF NIEDERLÄNDISCH"（705px，跨 622–1328，与右侧净距 83px），复检渲染干净。仅 P1 SVG 因此变更（其余 7 页 md5 不变）。
3. **趋势榜注行**：图中趋势词与数字为荷兰语冻结内容；核心版中文源行替换为德语行 „Google Trends, Dienstag, 20. Oktober: Momentaufnahme; nur Schätzungen."，与保留的荷兰语源行并列（框高计算不变）。
4. **P6 正反框标题**：双语题 „AFSCHAFFEN OF NIET? · ABSCHAFFEN?" 实测 410px 超框内题栏 390px（正文标题为页内栏目头、宽 462px，不受影响）；按房规「测宽、必要时缩短并记录」缩为 „AFSCHAFFEN OF NIET? · ABSCHAFFEN"（399px，框题左对齐起排不裁切，渲染目检完整）。
5. **P8 答案字号（重要）**：核心版补丁基线为 13.5pt/1.16。德语简析较长，同参数下答案流在末栏溢出（clamp 于 y=2582，压页脚线）。两步收紧（均为字型层、不动内容）：先 13.0pt/1.14，再 **13.0pt / lh 1.12 / gap 0.4**，并将 #66 简析略缩一行（„Über 3.000 Künstler (250 = nur die erste Liste)"，key 不变）。最终逐栏最低基线 = **2528.2 / 2525.0 / 2531.6 / 2337.6**，距页脚线（2580）净距 **51.8 / 55.0 / 48.4 / 242.4 px**，全部 ≥40px（SVG 坐标程序实测，非流光标推测）。

## 八、校对记录（构建方）

- 基线：动工前在副本上重建未改动核心版，8 张 SVG 与已交付核心版**逐字节全等**，registry 150 项全等——翻译只发生在该已验证基线上。
- 冻结 diff（源码级）：副本与原始核心版构建全量 diff 逐行分诊——除路径/文件名/方法改名外，所有改动行均为讲解层字符串；唯一无中文的非管道改动行是 `note_line` 的方法定义本身。无任一荷兰语串被误触。
- 构建日志：最终构建零警告（零 FLOW OVERFLOW、零 HEAD TOO WIDE）；P7 三栏堆叠收尾 1678.5 与核心版逐点相同；P8 答案流收尾 col 3 y=2353（底界 2552）。
- 渲染目检：8 张卡逐页看过；重点复核 P1 徽章/通栏、P2 时间卡德语说法、P6 图表条长、P7 读者信与预告黑带、P8 第 137–140 题与答案区底部留白。

## 九、几何遮挡审计（SOP 附则 + 细线补充，构建方）

方法：按绘制顺序解析最终 8 个 SVG；文本墨迹盒用生产字体（PIL 实测字宽）×[基线−0.88em, 基线+0.30em]；查 (a) 后绘不透明形状覆盖 ≥30%、(b) 墨迹入页脚带（y>2580）、(c) 墨迹出纸面、(d) 后绘细线（≤3.4px rect/line）穿墨迹带、(e) 文本—文本盒重叠。

结果：**(a)–(d) 全部 8 页零 flag**。(e) 余 9 处文本—文本盒重叠，逐处裁图裁定均为**度量模型假阳性**，与核心版同几何：
- 每页带题/副题一对（318px²）与 P1 报头/副题一对（7856px²，Unifraktur 实测度量）：裁图示两行渲染分离干净——带与报头均为核心版原样家具。
- P8 答案 #100/#137/#138/#139 的换行行对（134–294px²）：同一答案条目内相邻换行行的墨迹带模型重叠（带高 0.88+0.30em > 行距 1.12em 的模型伪影）；裁图（答案区右半页）示行间分离干净、无字形接触。

P8 逐栏最低基线与净距见 §七.5，全部 ≥40px。**构建方审计零未决 flag**；独立校对方须按同法复跑。

## 十、交付物与校验值

| 文件 | 字节 | 备注 |
|---|---|---|
| De-Lucerna-VOL1-DE.pdf（印刷版） | 9,676,577 | md5 4afd0913bafc… |
| De-Lucerna-VOL1-DE-web.pdf（网络版） | 3,340,246 | md5 3e18dfef3dd0…；<10MB，可直接上传 Discord |
| cards/*.png ×8 | — | 1950×2700 |
| svg/*.svg ×8 | — | 最终版面源 |

Discord 交付（投 Nederlands 串、禁 #general）与 weekly 仓入库由主代理在本版独立校对零问题后执行。

---

## 十一、独立校对记录（2026-10-21，校对方独立复核，非构建方自检）

方法：双版 SVG 全量文本提取逐项 diff + 注册表双跑逐项比对 + PIL 实测字宽几何审计（绘制序覆盖 ≥30% / 页脚带 / 出页边 / 细线穿墨迹带 / 文本—文本盒）+ 关键区域裁图目检 + 全部 150 条德语简析通读并与核心版简析逐项对照 + ≥30 题对着印出题面重解。基线先行验证：核心版与本版构建在沙箱重跑均与已交付 SVG **逐字节全等**，后续结论都建立在该基线上。

**发现并修复 2 处缺陷（均只动本版构建源 content12.py，仅 P1 SVG 变化，P2–P8 逐字节不变，注册表复跑全等）：**

1. **§七裁定 1 复核不成立——P1 副标题丢词（核心层内容缺失，已修复）**。副标题行中仅行首标签是读者语言成分（核心版「荷 兰 语 周 报」，本版作 NIEDERLÄNDISCH 正确）；其后 VOL.1 与三个主题词是荷兰语正文层内容。HERFSTVAKANTIE 是本期头条首个主题词（头条正文与第 2、3 版均以此为纲），删之属正文改动，不属任务书允许的读者语言项，也与「徽章替换标语行」的同矩阵先例不同——本版徽章是新增行（y=568），荷兰语标语行（y=372）并未被顶替，无物被置换。且「放不下」的理由经实测不成立：恢复全行（NIEDERLÄNDISCH · VOL.1 · DE KLOK GAAT TERUG · HERFSTVAKANTIE · ADE WORDT 30）以同字号（40pt 粗衬线）实测宽 **1761.4px**，居中跨 94.3–1855.7，在构建方自述的 1820px 栏宽与版心内均放得下（核心版同槽位原行实测 1647.8px）。**裁定：缺陷。已恢复该词**，重渲染后裁图复核：与报头、标语行均留白干净。（旁注：NL×EN 版同行处理相同，但其标签 WEEKBLAD IN HET NEDERLANDS 较长，同字号恢复约 2050px 确实超版——彼版是否处理由其校对线另行裁定，不影响本版结论。）
2. **P1 全宽细线划穿德语讲解行（细线穿字，已修复）**。词条讲解首行 „»Die Uhr verstellen«: die Zeit an der Uhr ändern" 基线 1846.3，其后绘全宽线 y=1844 位于基线之上 2.3px，裁图坐实线体横穿拉丁字干下段（非下划线式贴边）。核心版同线对中文讲解只是贴字脚下缘（汉字墨迹底边与之相切，属另一状态，核心版冻结不动，此处仅登记报告主线）。本版修法同 IT 核心 P1 先例（移线）：线 1844 → **1853**（讲解行 1 无降部字母、墨迹底 ≈1847；行 2 升部顶 ≈1857.7；新位置上下各留约 5px，全版宽内该横带经程序核查无任何墨迹带交叠）。重渲染后审计该标记消失，裁图复核两行均与线留白。

**§七其余裁定复核：**

- 裁定 2（顶部通栏中行）：实测中行宽 705.1px，跨 622.5–1327.5；周次行起于 1411.5，净距 **83.9px**（构建方记 83px，合）。通过。
- 裁定 3（趋势榜源行改德语）：德语源行在版且与荷兰语源行并列，趋势词与数字（荷兰语）与核心版全等。**附带裁定**：趋势框题由核心版「中文问句 · 荷兰语 zoeken op Google」改为纯德语 «Was die Niederlande googeln»——荷兰语尾巴的语义（在谷歌上搜）已被 «googeln» 完整承载，无内容损失，属讲解层家具重构，可接受。
- 裁定 4（P6 正反框题去「?」）：**可接受**，但构建方数字需更正——框实测 x=1451、宽 434（右缘 1885），题起排 x=1473；现行题宽 399.5px，墨迹右缘 1872.5，距框边 12.5px，裁图完整不裁切；若保留「?」宽 410.3px、右缘 1883.3，距框边仅 1.7px。故去「?」是框内排版的正当取舍（荷兰语半题 «AFSCHAFFEN OF NIET?» 含问号原样未动，属纯德语讲解半题的标点省略），其所据「390px 题栏」一数与实测不符，以本条实测为准。
- 裁定 5（P8 字号收紧）：逐栏最低基线独立实测 **2528.2 / 2525.0 / 2531.6 / 2337.6**，与构建方所记逐一吻合，距页脚线净距 51.8 / 55.0 / 48.4 / 242.4px，全部 ≥40px。通过。

**其余全量核查结论（均独立复测，非转述）：**

- 注册表：150 题，级别 A2 42 · B1 76 · B2 32、逐版 10/18/18/18/18/18/12/38、题型分布与核心版全等；**key 差异仅 #137/#138/#150**（与 §四表一致）；#139/#140 在注册表与 P8 渲染图上双证：题面德语、**答案荷兰语逐字节同核心版**（NL×EN 版的坑未重演）；简析 141 条全德语、9 条语言中立与核心版同，**无一条残留中文**。
- 简析语言：150 条通读，德语语法/格/习语无误，与 key 及正文事实逐项相符；括号均为半角且前置空格。图表算术复验：301.000+246.000=547.000；750.000−547.000≈203.000（标 gerundet）；60.500÷6.600≈9,2 → «gut 9 Mal»；#46：19,50×2+32,50=71,50。作文范文与核心版逐字节相同，独立点词 **87 词**。
- P7 本周句：8 句在全期（空格归一化）各出现恰 **2 次**，德语译文与 (Pagina N) 页标与源版对应无误；VOL.2 预告（荷兰语正文）冻结未动。读者信 Emma/Berlijn 本地化与 §六所记一致，信体荷兰语除人名/城市外未动。
- 图片 6 张与核心版逐页 payload 哈希全等，署名（荷兰语）未动；最终 SVG 中文字符 **0**；页脚每页标注配对，P1 徽章渲染可见（砖红行，黑带之下）。
- 几何审计（修复后复跑）：(a) 覆盖 ≥30% 零标记；(b) 页脚带仅页脚元素自身（基线 2624，版式固有，与核心版同）；(c) 出页边零；(d) 细线穿带仅修复前的 P1 一处，修复后零；(e) 文本—文本盒重叠余 P1 报头/副标题一对（裁图示两行分离干净，Unifraktur 带模型伪报，几何与核心版同）、各版带题/副题一对（318px²，同上）、P8 同条目折行对 15 处（逐处裁图复核 #91/#98/#99/#100/#137/#138/#139/#140 等，行间留白干净，系 1.12 行距 < 1.18 带高的模型伪影）。**零未决标记。**
- 两处文字通读裁定（记录备查，不构成问题）：P7 译句 «Mehr als 3.000 Künstler kommen zu mehr als 200 Orten in der Stadt» —— «kommen zu + 地点» 语义准确、语法可立，与荷兰语原句逐词对应，从严可作 «an … Orten auftreten»，属风格层，不改；PAS OP! 诊所 «Verkleiningswoorden: immer »het«!» 未复述例句 «het huisje»——该例句在同条荷兰语纠正行 ««het huisje»» 中原样在版，讲解无缺失，不改。

**修复后交付物（取代 §十中两份 PDF 的数值）：** 印刷版 De-Lucerna-VOL1-DE.pdf **10,631,705 B**（md5 8fee5c3840305b3c9…）；网络版 De-Lucerna-VOL1-DE-web.pdf **3,732,695 B**（md5 03444b5c1d6adb6e…，<10MB）。第 2–8 版 SVG 与卡片未变。

**最终结论：独立校对完整一轮零问题，本版定稿（PASS）。** 构建方陈述除 §七裁定 1 的取舍理由与裁定 4 的栏宽数字外，余皆经复测成立。

## D5 rebuild (13 Nov 2026; this build supersedes all earlier deliverable figures in this KIT)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib 2026-w43-nl-de/svglib.py --target nl --reader latin --week 2026-w43` (`--check` dry-run first, RC=0). `_D5_READER = "latin"`. Routing unit test `test_d5_routing.py`: FAILURES: 0. D1 fix2 retained.
- Pre-rebuild census (`d5_census.py`, D5 elements in the pre-D5 SVGs): 490.
- Baseline (pre-D5 rebuild, venv, disk-measured): run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; print `De-Lucerna-VOL1-DE.pdf` 10,265,829 B (sha256 `de308988d6d0b70c4ade6091ff5d6e299d16caa94dfd62adbfcd1a1a99c283d5` — pre-D5 build, superseded); web `De-Lucerna-VOL1-DE-web.pdf` 990,108 B (sha256 `bb5e668e26f32f140e424961104849ce1ba4979971176b58323cc50d7ffce7d8`). Text layer print vs shipped web PDF multiset diff 0 (Python `len()` chars). The KIT-recorded print/web figures predate the §1.1 style port and the D1 re-render and are superseded by the disk-measured baselines above.
- Defects found by the 17 gates (run 1) and fixed by size only — text unchanged throughout:
  - Feature heads `ETEN BESTELLEN WORDT HELDER` (P2) / `EROPUIT IN DE HERFSTVAKANTIE` (P3) HEAD TOO WIDE at 25 pt (advance 472.2/466.0 px vs column 422.5 px) → head size 25 → 22 (`content12.py` P2 head, `content34.py:20`).
  - P1 box title `DE WEEK IN CIJFERS　IN ZAHLEN` over +17.2 px (right) → f.box tsize 23 → 21 (`content12.py:50`).
  - P2 box title `ZO ONTHOUD JE HET　MERKREIM` over +29.0 px (right) → f.box tsize 23 → 21 (`content12.py:185`).
  - P6 p.text `AFSCHAFFEN OF NIET?　ABSCHAFFEN` over +43.6 px (right) → size 21 → 18 (`content56.py:166`).
  - P7 p.text `HET WOORD　WORT DER WOCHE` over +17.1 px (right) → size 23 → 21 (`content7.py:84`).
- P8: 255 → 255 lines, slack to footer rule 35.9 → 35.9 px (unchanged by §4; `content8.py` untouched).
- Gates (full re-run after fixes, run 2): **ALL-GREEN** — run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; head_check 0; d5 census 0; render RC=0; webpdf RC=0, web < 7 MB; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8 byte-identical; freeze diff vs baseline added CJK 0; spill 0 SPILL; boxtitle 0 DEFECT; edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web multiset 0, text.md BYTE-IDENTICAL; census_quotes 0 defective. Logs: `hidden_files/d5-redo/scratch-2026-w43-nl/gates/2026-w43-nl-de/` (`GATES-SUMMARY.txt` master). Full record: `production/notes/2026-w43/g-nl/scratch-d5-rebuild-nl/D5-REPORT-2026-w43-nl-de.md`.
- New deliverables (rebuilt 13 Nov 2026): print `De-Lucerna-VOL1-DE.pdf` 9,676,577 B, sha256 `471c9a64b0b5b254c3932cd910467819763ae6a09420bd44146726c3c6ed9e2e`; web `De-Lucerna-VOL1-DE-web.pdf` 3,340,246 B, sha256 `d01f2a0161b1d771d9240bc5b7ae7c70f7d29a924fc9ff2236cb4d78558925dd` (< 10 MB); text-layer web `2026-w43-nl-de.web.pdf` 908,573 B, sha256 `afa14aa221556ceb7d8189c54a56c2c854411b3e2141adab03234ba23bc0160c` (< 7 MB); `2026-w43-nl-de.text.md` 39,856 B, sha256 `deed3a5a9cae537f1998710c8126f600b10cabdaea7d5c2c2f36c87251360186`, **BYTE-IDENTICAL** to the shipped `issues/2026-w43/2026-w43-nl-de/2026-w43-nl-de.text.md` (exported from the build source with the scratch exporter `hidden_files/d5-redo/scratch-2026-w43-nl/export_text_w43nl.py`, W46 generic AST exporter + W43-nl italic-serif fix + `IN DEZE EDITIE` heading fix).
- Status: builder DONE, all gates green. Independent re-proof (SOP §8) is the coordinator's separate step; no commit, no push by the builder.
