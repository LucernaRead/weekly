# W45 EN × ES 独立校对报告

**结论：ZERO PROBLEMS（阻塞项 0 项）**

本报告只校对、不改源码、不宣布上架。未发 Discord、未往主聊天发卡片/PDF、未建 cron、
未碰 weekly-git、未改核心/W43 目录（只读对照）、未清理共享 scratch 目录。
构建员自述全部独立重测，未采信任何一项；下文每项均给出本轮实测值。

## 0. 开工查重与哈希

- 开工前：`files/weekly-report-w45-en-es/` 与 `hidden_files/weekly-report-w45-en-es-build/` 无进行中
  写盘进程；90 秒复查零新写盘，判定为已完成交付的安全开工（非 stand down）。
- 交付物与核心全部 sha256 校对前记录（`pre-deliver-sha256.txt` / `pre-core-sha256.txt`），
  校对后复核（`post-deliver-sha256.txt` / `post-core-sha256.txt`）：
  **交付物全部不变、核心全部不变**（diff 干净）。
- 交付 PDF 与任务书一致：印刷 PDF 17,292,956 B，
  sha256 `382f1e81b1249123b1ca2d28ebb53d825f82c55ece01f822f576e27fd9b733f1`；
  web PDF 4,004,747 B，sha256 `6282726a0a79ee6ce72131372e4ccc4c5243015c8e087e9853903dc2b4f23e13`；
  两 PDF 均为 8 页；KIT 中记载的字节数与 sha 全部吻合。

## 1. 冻结（freeze）

- `freeze.py baseline`（核心构建目录 `hidden_files/weekly-report-w45-en-build` 重跑）：
  **8/8 逐字节一致**；构建后核心 SVG 重哈希与基线一致，核心未动。
- 分版构建复现（`freeze.py baseline`，分版构建目录重跑）：**8/8 逐字节一致**。
- `freeze.py diff`（本轮重跑，`freeze-diff.json`）：新增 CJK 0（8 版全 0），版面 CJK 全 0
  （核心 CJK 总计 2031：P1 183 / P2 197 / P3 119 / P4 139 / P5 134 / P6 136 / P7 347 / P8 776；
  分版每版 0）。注：diff 计数按去重字符串计，与构建员按出现次数计的 +28/−26 等
  总数口径不同，属计数口径差异，非不一致。
- 被删英语逐项裁定（`proof_checks.py` 对全部 removed 串分类，problems = []）：
  - 唯一纯英语整串删除：P1 刊头标语（核心 y=372
    `THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA`），属徽章替换（见 §7）。
  - 其余被删串：全部含 CJK（中文讲解层替换，含中英双语栏头的中文半句，其英文半句
    均在新增串中以西语双语栏头重现）或重排伪影——重排类共 16 串
    （P1 数字框行、P7 例句框 `(page 6).` 断行、P8 键区行段），其全部单词均在同版
    新增串中重排出现，无内容丢失。
  - 新增侧 ASCII 串核查：全部为西语标签/指令/注释断行或含英语词头的西语行
    （如 `Traduce: …` + 英语题干），无凭空新增英语句。
- 违禁词：svg 8 版 + KIT + ABSTRACT 全量 grep **0 命中**（本报告亦不拼写该词）。

## 2. P8（p8.py compare 独立重跑 + 自写分段器交叉验证）

- **78 口径的独立确立**：P8 键区自写分段器（ANSWERS 刊头后文本按 `· N.` 切分，
  与工具不同的实现）切出核心与分版各 **150 段、编号 1–150 连续**；
  其中带印刷注释（尾随括号注释或破折号注释）的段核心 78 段、分版 78 段，
  其余 72 段为无注释裸键（如 `7. B`）。故 78 是“带注释键数”，不是题数；
  150 题本身由键区 150 段连续编号保证。`p8.py compare` 本轮重跑：
  **CLEAN，78 = 78，missing=[]，extra=0，uncertain=[]**，与自写分段器集合逐项相等。
- keydiff = **[137, 138, 139, 140, 150]**，印刷行逐项对照（括号内为注释）：
  - 137：核心 `耐心是制度的一部分，而不是制度的失败。（part of 一部分；not a failure 不是失败）`
    → 分版 `La paciencia es parte del sistema, no un fallo del sistema. (part of = parte de; not a failure = no un fallo)`；
    题面英语指令 `Translate :` 保留。**合法**（译文英→西重定向）。
  - 138：核心 `11 月 3日周二是美国的选举日。（Election Day 选举日；on Tuesday）`
    → 分版 `El martes 3 de noviembre es el día de las elecciones en Estados Unidos. (Election Day = día de elecciones; on Tuesday)`；
    母语指令 `翻译：` → `Traduce:`。**合法**。
  - 139：核心 `这周日，NFL 在马德里比赛。（on Sunday；in Madrid）`
    → 分版 `El domingo, la NFL juega en Madrid. (on Sunday; in Madrid)`；
    母语指令 `翻译：` → `Traduce:`。**合法**。
  - 140：核心 `并非每处都拨回时钟。（not every 并非每处；change 变化）`
    → 分版 `No todos los lugares cambian. (not every = no todo; change = cambiar)`；
    题面英语指令 `Translate :` 保留。**合法**（见裁定说明：核心中文把题干省略的
    “时钟”宾语显化，分版西语贴英语原文作省略处理；题干
    `Not every place changes.` 两版冻结一致，两种译法均正确，属翻译重定向）。
  - 150：核心 `开放题 — 要点见写作框，范文在第8 版写作框内（按要点给分）`
    → 分版 `Pregunta abierta: véanse los puntos en el recuadro de redacción; el modelo está en el recuadro de esta página (Se puntúa por puntos)`。
    **合法**：写作题键本就是讲解层文字（非冻结英语）；W43 EN×ES 同类先例已核实
    （W43 末键 149：`(pregunta abierta — el modelo está en el recuadro de escritura) (se puntúa por puntos)`，
    同为写作框重定向 + 西语评分注）。
- P8 注释纯西语：分版键区文本 CJK 0；半角括号 79 处、全角括号 0 处
  （核心：半角 0、全角 82）；E 节指令 137/140 英语指令保留、138/139 改 `Traduce:`，与上表一致。
- P8 印刷笔记集合相等靠显式钉住一节：CLEAN 本身已证明集合逐项相等；
  EXTRA_ONLY 未出现，不适用。

## 3. 几何

- `occlusion_audit.py` 自检先行通过（6 类 planted 全部触发，clean 对照静默）。
  本轮重跑：**分版 1 标记 / 核心 0 / NEW 1**，与构建员一致。
- **P1 刊头 TEXTX 独立像素级验证（未采信构建员结论）**：用审计同款 TTF
  （UnifrakturMaguntia 168pt 刊名 + Noto Serif CJK SC 46pt 粗体刊头行）分别重绘
  两串掩码。刊名墨迹框 (562,141)–(1389,290)，刊头行墨迹框 (309,285)–(1642,331)；
  墨迹行交集仅 y=285–289 共 5 行，且每行两串墨迹 x 集无交集
  （如 y=289：刊名墨迹 x=704 仅 1 像素，刊头行墨迹 x=832–1345）；
  **重叠像素 = 0**。裁定：**框级伪报，非缺陷**。W43 同配对对照亦支持同类裁定：
  W43 EN×ES 本轮审计同样带此 TEXTX（交叠框尺寸同为 834.2×6.2px），且 W43 已上架。
- 同基线碰撞（解码后测量，本轮自写实现 + 构建员 supplemental 双路）：
  **分版 0、核心 0**。原 −30.5 伪影对已精确定位并复现：
  P1 y=1404 `A cat, a monster & screens` <> `A2→B1`——未解码（`&amp;` 按 5 字符计宽）
  间隙 −30.5px，解码后间隙 **+19.0px**，与构建员数值逐位一致，伪影不复现。
- P6 图表覆盖（基线锚定墨迹法，PIL getmetrics，anchor ls，本轮自写实现 +
  supplemental 双路）：4 条标签行 + 导读行**最差 0.0%**（门限 <30%），分版 = 核心。
- 全 8 页框线压框 + 右缘扫描（ADVANCE 法，本轮自写实现 + supplemental 双路）：
  框线/内框标记 **0**；P1–P7 最大 advance 右缘 1885.0（恰为页边）；
  P8 1903.8 仅来自两条冻结 F 配对右项（`b. an election in the middle of a term` 1899.4、
  `d. the paper you mark your choice on` 1903.8），核心同款同值，墨迹未触内框线 1910。
- R2→R3 消除核查：构建员 R2 审计文件（`occlusion.json`）共 19 标记；
  本轮终态审计仅剩刊头 TEXTX，**其余 18 项（P1 热搜 EDGE/BOXTITLE、P1 暗带行 TEXTX、
  P2 AND YOU 盒底 0.6px、P3/P4/P5/P6 标题 BOXTITLE/TEXTX、P7 金句栏头 TEXTX、
  P8 Levels 压金线 LINEX）在终态全部消失**，逐项确认消除。
  R1 的 4 个 HEAD TOO WIDE（P8 B/C/D/G）见 R1 日志原文；R2/R3 日志警告 0。

## 4. gloss（渲染后实测，非照搬）

- 以 #f1ead6 词框矩形为界（框内首行须为词框前缀，分版 `Nota — ` / 核心 `译注｜`），
  框内文本按 `·` 拆分，从渲染 SVG 独立实测：
  **P2 3 = 核心 3、P3 4 = 核心 4、P4 4 = 核心 4、P5 3 = 核心 3、P6 4 = 核心 4，
  合计 18 = 18**；P1/P7/P8 两版均为 0 框。
- 英语词头：核心词框 ASCII 词序列为分版词框 ASCII 词序列的子序列（顺序一致，
  分版仅插入西语释义/提示词），逐页 subsequence 检查全部通过；
  例 P2：核心 `to fall back / a costume / trick or treat` → 分版同词头 + 西语释义。

## 5. P7

- 例句框：A2/B1/B2 三框英语定义句逐字保留，仅释义本地化——
  A2 `Americans are going to vote on Tuesday.`、B1 `The clocks fell back on Sunday, November 1.`、
  B2 `Patience is part of the system, not a failure of it.`（B2 尾注由 `part of = 一部分 (page 6)`
  改为 `part of = una parte (page 6)`）。定义句本地化 = 阻塞性失败，本版无此情况。
- 金句 8 句原文逐字保留（核心 = 分版，顺序一致）：
  ① Tuesday, November 3, is Election Day in the United States. ② The hour from 1 to 2 happened twice.
  ③ Which film would you choose ? ④ Two games, two continents, one league — that is the modern NFL.
  ⑤ The results will still be there in the morning. ⑥ Patience is part of the system, not a failure of it.
  ⑦ Not every place changes. ⑧ One Sunday is not enough — good thing the week has seven days.
  级别序列 [A2, A2, B1, B1, B2, B2, A2, B1]（100–107）与核心一致。
- 全期句频（全 8 版合成为本逐句计数）：核心 = 分版——
  ②③④⑤⑧ 各 2×；① 3×（另 1 次在 P8 E-138 题干）；⑦ 3×（另 1 次在 P8 E-140 题干）；
  ⑥ 4×（另 2 次在 P7 例句框与 P8 E-137 题干）。
- P7 结构语言归属与核心一致：四栏 A2/B1/B2/工具箱、金句区、易错诊所、读者园地、
  VOL.3 预告；金句语法点 8 条全部用 `Nota — ` 前缀（W43 金句槽先例），
  诊所桥段为 plain 西语句（与 W43 诊所引言逐字一致：
  `Cada frase tiene un error: búscalo y corrígelo.`），无 `Nota — ` 前缀。

## 6. 读者园地

- 英语信件段 3 行逐字冻结（与核心逐行一致，含 `(editor's example : … honestly labeled)` 标注）。
- 西语披露句逐字摘录（3 行，位于读者园地框 (989,1878,896,300) 内，末行底约 2160 < 框底 2178，无溢出）：
  1. `Nota de la redacción: VOL.1 prometió cartas reales en VOL.2, pero no llegó ninguna carta ni`
  2. `el mejor texto de la página 8 de VOL.1; no inventamos nada y el ejemplo sigue marcado.`
  3. `¡Envíanos tu carta y tu texto! En VOL.3 publicaremos las cartas recibidas.`
- 逐项核实：事实 1（未收到真实来信）✓、事实 2（未收到 VOL.1 第 8 版最佳作文）✓、
  事实 3（未编造 + 示例保留标注）✓、显性祈使邀请（`¡Envíanos tu carta y tu texto!`）✓、
  VOL.3 刊登承诺 ✓。内容预告行（NEXT WEEK 英/西行）未计入邀请。
- **最佳 P8 作文覆盖范围裁定**：披露句的 VOL.3 承诺措辞覆盖“收到的来信”；
  最佳 P8 作文另由冻结的 P8 写作框英语句明确保障——
  `The best texts will appear in VOL.3 (page 7, « Readers' Corner »).`（核心 = 分版逐字一致，
  另有西语写作指令 2 行）。两者合计：来信与最佳作文均指向 VOL.3 读者园地，覆盖完整。
- 无编造、无凭空新写英语披露句：读者园地区域英语行核心 = 分版（仅信件段 3 行）。

## 7. 家具与 W43 偏差 10 项

- 徽章几何三方实测（P1 y=372 槽）：
  - W43 EN×ES：`TEXTOS EN INGLÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`，
    19.5pt 粗体，砖红 #a4553a，居中。
  - W45 核心同槽：`THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA`，19pt 非粗体，#57523f。
  - W45 本版：与 W43 **逐字、字号、粗细、颜色全部一致**。徽章几何 = W43 ✓。
- W43 偏差 10 项逐项核实（全部通过）：
  1. P8 栏头用 W43 短式：A–H 与 W43 逐字一致，唯一差别是 H 栏头保留核心 `[B1]` 标记（`Escritura [B1]`）。
  2. P7 金句栏头去括号 → W43 原文：分版 = W43 = `PHRASES OF THE WEEK · Frases de la semana`。
  3. 6 框题 + 热搜副题 + 暗带右行 2 + P1 词框西语半句短于直译：6 个 23pt 框题实测宽
     304.4–386.5px（< 434px 栏宽：En casa 348.7、El sombrero 335.2、Domingo 385.3、
     Muy reñido 386.5、Papeleta 356.6、El mandato 304.4）；P1 词框行
     `A mitad de mandato: midterm election.` 346.6px；暗带右行 2 为 end-anchor 带行
     （444.2px，止于 1855，与左侧标题同基线无碰撞，rowcheck 0）；“短于直译”为构建
     设计陈述，交付物侧以“全部入框 + 审计 0 标记”验证通过。
  4. P8 §E 间距 11→4：源码核实——核心 E 题 `bf.ex` 无 gap 参数（默认值 11），
     分版 `gap=4`；渲染后果：R2 电池流 y=1513（超底线 1485、Levels 压金线）→
     R3 电池流 y=1376，Levels 行 y=1348.015，金线 y=1486，净空 138px。
     （KIT §十 R2 文本所记 Levels ~1457 为 R2 修复中间态数值，终态为 1348.015，
     方向一致且净空更大；见非阻塞观察 2。）
  5. P2 AND YOU 盒尾 +20→+24：源码核实——分版 content12 盒高公式末项 `+ 24`；
     渲染：盒 (1451,1225.25,434,278)，底 1503.25，7 行盒内文本全部在内，
     下一同栏文本 y=1598，R2 的 0.6px 盒底溢出消失。
  6. P8 band 副题保留核心英语句 + 西语译文：分版
     `FINAL TEST · Evaluación final · Answers at the bottom of this page · Las respuestas están al final de esta página`；
     W43 为纯西语行，核心为英语句 + 中文半句——分版组合合法（冻结英语句保留）。
  7. P7 金句语法点用 `Nota — ` 前缀（8/8），诊所桥段 plain（见 §5）。
  8. P8 键区半角括号（见 §2：半角 79、全角 0；核心反之）。
  9. 读者园地披露句按协调员裁定重写（见 §6）。
  10. 徽章几何 = W43（见本节首段）。
- 继承 quirk：P3 `C · THE WORDS` 栏头孤悬第 2 栏底（y=2305.0，配对项流至第 3 栏）——
  核心同款（y=2275.2，配对项同样流至第 3 栏），核心卡片目视对照一致，审计 0 标记，
  非本版缺陷。另：P4 同款孤悬在核心与分版均存在（核心 y=2220.0，分版 y=2250.0），同类。
- 其余家具：页脚 8 版、页码行 `Página N de 8`、词框前缀 `Nota — `、P8 分隔 `— Página N —`、
  练习内小标签（Completa/Reescribe/Empareja/Corrige）均与 W43 登记一致。

## 8. 图片、ABSTRACT、卡片、体量、PDF

- 图片载荷逐页相等：5 张嵌入图（P1/P2/P3/P4/P6）base64 载荷 sha（前 16 位）与
  几何（x/y/w/h）核心 = 分版；P5/P7/P8 两版均无图。
  署名在版且与核心逐字一致：P1 `Kenneth C. Zirkel — CC0, via Wikimedia Commons`、
  P2/P6 `Public domain, via Wikimedia Commons`、P3 `Édouard Manet — CC0, via Wikimedia Commons`、
  P4 `Frank R. Snyder — public domain, via Wikimedia Commons`。
  （P6 模拟选票中的 ☐ 为核心冻结字符，两版渲染一致，非本版问题。）
- ABSTRACT：西语单行（1 行 + 末尾换行），ASCII 双引号 0 个；
  含刊名、目标语、读者、真实主题关键词（11 月 3 日中期选举、11 月 1 日拨钟、万圣节、
  电影上映、NFL 马德里赛、美国投票制度）、学习者搜索短语
  `aprende inglés leyendo noticias reales`、A2–B2、150 ejercicios。
- 8 张卡片逐页目视（1950×2700）：P1 刊头/暗带/数字框/热搜框/词框/快讯/闪电问答干净；
  P2 AND YOU 盒西语 2 行盒内、时钟栏、练习区干净；P3 居家框/猫帽框/影评桥段干净，
  栏头孤悬见 §7；P4 周日赛程框/马德里框/词框干净；P5 难分胜负框/词框/投票结束桥段干净；
  P6 模拟选票框/图表标签 4 行/教学数据声明/任期框干净；P7 四栏/金句/诊所/园地/预告干净；
  P8 电池 A–H/写作框/范文/Levels 行（与金线有空隙）/键区 1–150 干净，键区末行距页脚线有空隙。
- 体量（分版构建 scratch 重跑登记表 + 核心登记表双路）：
  **150 题；A2 60 / B1 69 / B2 21；页分布 10/17/18/18/18/18/12/39**；
  核心登记表同值（题型标签中→西 1:1：完成句子 33、单选 41、句型转换 16、词汇配对 20、
  图表读数 6、跟练 8、改错 4、完形填空 8、阅读理解 4、翻译 4、对话补全 5、写作 1）。
  范文 85 词，核心 = 分版逐字一致。终轮构建警告 0（R1 4 个 HEAD TOO WIDE 已修，R2/R3 0）。
- 双 PDF 8 页、字节数与 sha 与 KIT 一致（见 §0）。
- R2→R3：8 页 SVG 哈希全部变化（R3 8 页均有改动属实）；R3 渲染后至终审无 SVG 变化
  （round3-pre 与 final 的 SVG 哈希一致，final 仅补 cards/PDF 行）。

## 非阻塞观察（单列，不构成阻塞项）

1. **P5 `C · THE WORDS` 栏头孤悬为本版新增（同类视觉，非缺陷）**：
   分版 P5 栏头位于第 2 栏 y=2116，配对项流至第 3 栏顶；核心 P5 栏头（y=2056.5）
   与配对项同在第 2 栏。分版属西语文本变长导致的流式换栏：内容完整、阅读顺序连续
   （第 2 栏末 → 第 3 栏顶）、审计 0 标记；且与 §7 中核心同款的 P3/P4 孤悬视觉同类，
   故列为观察而非阻塞。若主线要求与核心完全对齐，可在后续周期调整该栏流式断栏，
   但不影响本期内容正确性。
2. **KIT §十 R2 文本的 Levels 数值为中间态**：KIT 记“Levels 基线 1485→~1457”，
   终态实测为 1348.015（金线 1486，净空 138px）。方向一致且终态更安全，
   仅 KIT 叙述未更新至 R3 终态；交付物本身无问题。

## 证据文件（本校对全部输出）

- `hidden_files/w45/en-es-proof/REPORT.md`（本报告）
- `hidden_files/w45/en-es-proof/proof_checks.py`（独立校对脚本：冻结裁定、P8 自写分段器、
  像素重绘、rowcheck/edgescan/chartcheck、gloss、P7、读者园地、家具、图片、ABSTRACT、PDF）
- `hidden_files/w45/en-es-proof/proof_checks.log`（脚本全量输出）
- `hidden_files/w45/en-es-proof/freeze-baseline.log`、`freeze-baseline-ed.log`、
  `freeze-diff.json`、`freeze-diff.log`、`p8-compare.log`、`p8-compare.json`、
  `occlusion-selftest.log`、`occlusion-ed.json`、`occlusion-core.json`、`occlusion-new.json`、
  `occlusion-w43.json`、`supplemental-ed-rerun.log`、`supplemental-core-rerun.log`
- `hidden_files/w45/en-es-proof/pre-deliver-sha256.txt`、`post-deliver-sha256.txt`、
  `pre-core-sha256.txt`、`post-core-sha256.txt`
- `hidden_files/w45/en-es-proof/baseline/`、`baseline-ed/`、`reg-ed/`、`reg-core/`（scratch 复现树）
