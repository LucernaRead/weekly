# W45 PT×EN 独立校对报告 — ZERO PROBLEMS（可定稿）

- 对象：`files/weekly-report-w45-pt-en/`（svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照：W45 葡萄牙语核心 `files/weekly-report-w45-pt-core/`；W43 同配对版 `files/weekly-report-pt-en/`（家具以 W43 实测为准）
- 校对员：独立校对（只校对，不改源码；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录；核心与 W43 仅只读对照）
- 工具：`tools/`（`freeze.py`、`p8.py`、`occlusion_audit.py`，均用 `tools/venv/bin/python`）
- 本报告证据目录：`hidden_files/w45/pt-en-proof/scratch/`（freeze/p8/occlusion 输出、逐项分析脚本与输出、独立复现目录 `repro/` + `repro-svg/`、撇号放大裁切 `crops/`）。共享 `tools/scratch/` 全程未清理、未写入。

## 开工查重

- 首次检查（22:17 UTC）：交付目录最新写盘 22:15（ABSTRACT.txt、WEEKLY-KIT.md），构建目录最新写盘 22:15，无进行中的渲染进程。
- 90 秒后复查（22:19 UTC）：零新写盘、无相关进程 → 安全开工，非 stand down。
- 校对结束复核：交付目录 mtime 仍为构建员的 22:12/22:15，校对未改动任何交付文件；核心哈希校对前后不变（见 §1）。

## 结论：ZERO PROBLEMS

11 门逐项独立重测全部通过，无阻塞项。下文“与构建员自述不符处”列出的均为非阻塞观察（记录口径/计数口径差异，或已裁定不构成缺陷的项），纸面门禁仍以交付 SVG 为准。

## 1. 冻结

- `freeze.py baseline`（核心构建目录重跑）：**8/8 字节复现**，与构建员记录的基线哈希逐一一致（p1 `0dc8089d…`、p2 `56db3aa8…`、p3 `82f6fc3a…`、p4 `c5647cf6…`、p5 `92e86020…`、p6 `e6097473…`、p7 `a72cb75a…`、p8 `82630480…`）；运行前后核心 SVG 哈希不变，校对结束时再次复核仍不变。
- `freeze.py diff`（核心 vs 分版）：每页新增 CJK 均为 **0**；核心 CJK 总量 156/177/153/148/223/118/357/1123 → 分版 **0/0/0/0/0/0/0/0**，分版 CJK 总量 **0**。
- 源码删串逐项核实（核心构建目录 vs 分版构建目录，`bslib4.py` + `content*.py` + `render.py` 全量 diff）：
  - 所有改动行或含中文装置（被替换的中文讲解/注释/标题），或属于已备案家具清单：OUT/BASE 路径重定向、P1 徽章行（975/330 + 975/372）、`disc_cn`→`disc_en`、P7 引言间距、`word-box` 内边距、P8 键字号、P1 数字框 `tsize`、页脚/页码行、`gloss` 前缀、题型/指令标签英译。
  - 两处“删除”表象实为替换块附带物，不构成葡语丢失：`content12.py` 的 `])`（数字框旧块的闭合括号，整块被新数字框替换）、`content7.py` 的 `cyq` 间距行（128→104，见 §8）。
  - 字面存活复查（核心长字面去 CJK 后逐项核对）：葡语句子/词条均在分版存活，唯一例外是三处备案家具英译（见“非阻塞观察 5”），不是冻结内容丢失。**结论：0 条冻结葡萄牙语句丢失。**

## 2. P7 词框冻结 — 通过

- 词框葡语定义句逐字保留：`« feriadão »: sábado, domingo e segunda — três dias de descanso.`（源码 line 80 核心与分版完全相同；渲染后 P7 上亦逐字在位）。
- 仅 gloss 本地化：核心 `feriadão = 连休长周末，共三天。` → 分版 `feriadão = the long holiday weekend.`；词框高度实测 +10px（184.0→194.0），与内边距 20→30 一致。
- P7 错误诊所 4 项的葡语错句与纠正句亦逐字未动，仅第 3 列英文注释本地化。

## 3. P8 — 通过

- `tools/p8.py compare`（核心 vs 分版，total=150）：**CLEAN，150 = 150，missing=[]，extra=0，uncertain=[]**；keydiff 与构建员所列完全一致：`[2, 4, 25, 26, 27, 28, 52, 53, 54, 55, 101, 137, 138, 141, 142, 143, 144, 146]`。
- 18 项逐项对照印刷 P8 行（印刷 key token = “ — ”之前的第一 token）：
  - **16 项括号分支提取伪影，印刷答案 token 与核心逐字节相同：**
    - `#2`（`portões`）、`#4`（`13h30`）、`#101`（`confiro`）、`#146`（`A`）：括号式。p8.py 的 key 取“尾括号注释之前的整段”，故中→英 gloss 文本变化（及 `#2/#4/#101/#146` 的全角括号→半角括号）使 key 字符串变化，但答案 token 本身未变。如 `#2`：核心 `portões — portões = 大门（考场大门）` vs 分版 `portões — portões = the gates (the exam venue gates)`，首 token 均为 `portões`。
    - `#25–28`（`c/b/d/a`）、`#52–55`（`b/c/a/d`）、`#141–144`（`b/d/a/c`）：配对集。核心为破折号式 + 尾部裸字母（如 `c — feriadão=连着周末的假期 c`），分版改为 W43 式括号式 `term = English gloss (letter)`（如 `c — feriadão = a holiday joined to the weekend (c)`）。p8.py 对括号式取括号前整段为 key，故含本地化 gloss 的 key 字符串变化；但答案字母与葡语词条（feriadão / cemitério / vela / crisântemo；finalista / ida / volta / rodada；feriadão / portão / reta final / segunda chamada）逐字节相同。成簇出现正是因为三组配对集共用同一版式切换机制，非单项异常。
    - 由此，key 规范化后相同数为 132/150（150−18），与 18 项 keydiff 自洽；不能按“仅 2 项真改动故应为 148”理解，因为伪影项的 key 字符串本身就含 gloss 文本。
  - **2 项真重定向，逐字核实与任务书一致：**
    - `#137` → `Sunday, November 8, is the first day of the Enem.`（注：See the page 6 headline）
    - `#138` → `Check your card before Sunday.`（注：Confira = check, confirm）
  - `#139/#140`：葡语 key 逐字节未变（`O feriadão é de 31 de outubro a 2 de novembro.` / `Quando você chegar, apresente o documento com foto.`），仅注释中→英，故正确不在 keydiff 列。
- P8 答案注释纯英语：分版 P8 全部 150 段含 CJK 的段数为 **0**（CJK + 全角标点范围全扫）；注释中仅作为被引词条出现的葡语词本身（如 `feriadão = …`）属于答案内容，不是讲解语言残留。

## 4. 几何遮挡 — 通过

- `tools/occlusion_audit.py`（自检全部通过）：分版 **0 flags**、核心 **0 flags**、NEW vs 核心 **0**。
- 同基线墨迹碰撞扫描（全部 8 页，真墨盒）：**0 碰撞**；同基线（same-baseline）墨迹重叠扫描：**0 碰撞**。
- 页框压线扫描（内框 40..1910 × 40..2660）：**0 穿越**；按页边距换算的框相对最小边距见“非阻塞观察 4”（框相对值与构建员所称一致，T 差 0.2px 为取整/超采样口径）。
- 右缘扫描（ADVANCE 法为准）：8 页 advance 右缘最大值均 ≤1910 框线（最紧为 P2 的 `d. o objeto que dá luz e se acende em…`，advance 右缘 1897.26，框内 12.7px）；**超框 0 处**，故不存在需按 ≤0.5px 取整伪影规则豁免的行。
- P6 图表标签覆盖（基线锚定墨迹法：PIL `getbbox(anchor="ls")` + `getmetrics` 上升/下降，标签墨迹 vs 其后绘制的条形）：7 个标签全部 **0.0%**（`portões abertos`、`espera`、`prova`×2、`60 min`、`30 min`、`330 min`），均 <30% 通过。卡片目视亦确认三条 bar 未压标签文字。

## 5. gloss 计数与 P7 金句 — 通过

- 按渲染后 `gloss()` 字符串本身拆 `·` 逐项计数（README #21 方法，拆 `·` 本身而非 ` · `）：
  - 核心：P2 6、P3 6、P4 5、P5 5、P6 4，合计 26；分版：P2 6、P3 6、P4 5、P5 5、P6 4，合计 **26 = 26**，1:1。
  - 26 项的葡语词条全部在渲染后 SVG 中实测存活（`o feriadão`、`o cemitério`、`a vela`、`o crisântemo`、`a missa`、`conferir`；`o túmulo`、`a flor`、`acender`、`rezar`、`o silêncio`、`a lembrança`；`a ida`、`a volta`、`o finalista`、`a decisão`、`a rodada`；`a reta final`、`a véspera`、`a maratona`、`separar`、`a cabeça`；`os portões`、`a segunda chamada`、`conferir`、`a correria`）。
- P7 金句 8 条：每条在全刊裸文本（去空白折叠）中恰好出现 **2×**（源文章 + P7），页码标签与核心一致（P1×2、P2×2、P3、P4、P5、P6），且每句在其标注页上实测存在、P7 上附英语译文 + `(Página N)`。
  - 8 条：`Do feriadão à prova: a semana do Enem`（P1）、`Muita gente viaja, visita a família e vai ao cemitério levar flores`（P1）、`Finados é o dia da memória`（P2）、`lembrar é um jeito de continuar perto`（P3）、`cada ponto vale uma posição, cada gol vale uma história`（P4）、`quem dorme bem lembra melhor`（P5）、`primeiro as fáceis, depois as difíceis`（P6）、`Confira o cartão, durma bem, chegue cedo`（P2）。

## 6. 读者园地 — 通过（零编造；邀请范围裁定见下）

- 页上同时有三事实：
  1. 截稿时无真实来信：葡语披露句原文保留 — `Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3.`；英语披露句同义 — `Editor's note: the real letters and best texts promised in VOL.1 had not arrived by press time — the example stands, and the promise carries over to VOL.3.`
  2. 无最佳 P8 作文：同一披露句中的 `os melhores textos` / `best texts` 即指此（与 VOL.1 承诺的“最佳文本”对应），英语句同义覆盖。
  3. 示例 + VOL.3 承诺：示例逐字保留并标注 — `«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO`；承诺见披露句与邀请句。
- 显性英语邀请（逐字摘录，P7 读者园地独立成行，非内容预告行）：
  > `Editor's example — not a real letter. Send your letters to the editors: the best will be printed in VOL.3!`
  - 祈使句 ✓（`Send your letters to the editors`）+ 刊登承诺 ✓（`the best will be printed in VOL.3`），满足现行邀请门。
  - **范围裁定（独立判定）：该邀请句字面范围仅为来信。** 理由：祈使动词的宾语是 `your letters`，`the best` 最自然的回指就是“最佳来信”；句中未点名 P8 作文。最佳 P8 作文的征集覆盖不来自该邀请句本身，而来自披露句（“最佳文本承诺顺延至 VOL.3”）与 P7 末 VOL.3 预告行（`as suas cartas e os melhores textos da página 8`）。此口径与核心中文邀请（`真实来信请寄编辑部`，同样仅言来信）完全对应，不构成编造或遗漏，故不阻塞。内容预告行未被计为邀请。
- P5 的 E VOCÊ? 英文注释经核实为 `Write two sentences in Portuguese.`，无“寄来”语义，与 KIT 说明一致（核心葡语行本身无投稿语，故不从中文注释导入 寄来）。

## 7. 图片/署名 — 通过

- 仅 1 张照片：P1 `estudo.jpg`（图书馆学习照），其余为自制图表/表格；P2–P8 的 SVG 中 `<image>` 均为 False。
- 嵌入 payload 哈希：核心与分版均为 `cc351a4d…a83771c`（256,737 B），**与核心一致**；署名行已排版在 P1 照片下方，卡片目视在位：`Foto: Gary Todd / Wikimedia Commons — CC0`（CC0，Gary Todd）。

## 8. 家具偏差（W43 实测对照）— 通过

- P1 数字框题：核心 23pt → 分版 **20pt**（SVG 实测 `font-size=20`）；W43 同配对版 P1 数字框题实测同样为 **20pt**，构建员“W43 同样改动”属实。
- P7 引言间距：核心 128 → 分版 **104**（SVG 金句行基线间距实测：2021.5→2125.5→2229.5→2333.5，间隔恰 104.0；核心对应间隔恰 128.0）。W43 本刊为 158（该刊版式不同，此项 KIT 未称 W43 先例，仅称英文读者园地堆叠下沉后的避让理由；实测分版末条译文基线与 VOL.3 预告框留有净空，卡片目视无压框）。
- P7 词框内边距 20→30：词框高实测 184.0→194.0（+10px），与垫高一致；遮挡 0 印证 descender 不再压框。
- P8 键 13pt/1.12（核心 13.5/1.16，W43 14/1.21）：SVG 实测分版键号字号 150 项均为 **13**，核心 150 项均为 13.5，W43 150 项均为 14；源码 `af.para(txt, 13, lh=1.12)`；流底边距安全：P8 键区最大基线 **2546.62**，距页脚金线 2580 有 **33.38px** 净空，卡片目视键区与页脚线之间留白清晰。
- P1 词 gloss 缩短为一行：渲染后为单一文本节点 `“Long weekend”: a holiday plus the weekend.`，卡片目视一行在位、无截断；内容无丢失（见“非阻塞观察 3”）。

## 9. 撇号渲染专项（round-6 修复）— 通过

- 英语 apparatus 全程 ASCII 撇号：8 页 SVG 中 U+2019 计数 **0/0/0/0/0/0/0/0**；ASCII 撇号分布 P2 1、P7 3、P8 1，合计 5 处，与构建员所称 5 处一致（`SUNDAY'S`、`week's`、`Editor's`×2、`exam's`）。
- 卡片目视 + 放大裁切（`scratch/crops/`）：`SUNDAY'S TIMETABLE`（P2）、`week's story`（P7 B1 桥）、`Editor's example` 与 `Editor's note`（P7 读者园地）、`exam's length`（P8 #127）5 处均紧密、无缺字、无可见间隙、无错位。
- 独立 scratch 注册表重渲染核实复现说法：干净核心复制品 + `transform.py` → **7 个构建源逐字节复现分版构建源**；随后在 scratch 重定向 OUT 后重渲染 → **8 张 SVG 逐字节复现交付版**。复现说法属实（字节一致）。构建记录口径问题见“非阻塞观察 1”，不影响纸面。

## 10. 其他 — 通过

- 独立登记表（scratch 重跑 `run.py` 的 REGISTRY，非采信构建员自述）：总量 **150**；等级 **A2 49 / B1 70 / B2 31**；分页 **10/18/18/18/18/18/12/38**；题型 **完成句子 61 / 单选 49 / 配对 12 / 造句 7 / 判断 3 / 完形 13 / 翻译 4 / 写作 1**。
  - 分页计数说明：P2 印刷独立编号 14 个 + 配对集 inline 编号 4 个（25–28）= 18；P4 同理（52–55）= 18；P8 独立编号 34 个 + 配对集 4 个（141–144）= 38；P8 另有一处裸 `15.` 文本节点，实为阅读文本换行残影（`…no domingo / 15.`），非题号。
- 范文：源码 MODELO 与核心逐字相同，`split()` 计 **93 词**；P8 写作题面亦标注 `(93 words)`。
- 全文 `桥接`：**0**（且全刊 CJK 为 0，见 §1）。
- ABSTRACT.txt：英语单行（352 字符），无 ASCII 双引号，含真实主题关键词（Enem、November 2 Finados、November 8 first Enem day、essay/languages/humanities、Copa do Brasil semifinal second legs）+ 学习者搜索短语（`learn Portuguese through real Brazilian news`、`Portuguese text with English explanations`、A2 to B2、150 exercises）。
- 8 张卡片逐页目视（已看全部 8 张）：无重叠、无截断、无压框；徽章与配对页脚每页在位；P8 键区完整清晰。
- 终版构建警告：scratch 重跑日志中 **FLOW OVERFLOW 0、HEAD TOO WIDE 0**。
- PDF：印刷 PDF 3,471,726 B、SHA-256 `b0d063255527208917a9c0248781a13bb9926f3e0a8bfb001505fc4e4fdef7c7`；网页 PDF 3,425,058 B、SHA-256 `04aec5b5aca654f39d3ded6778085a80c94f8696d0e434a00e277fe1276bcda8`；与任务书一致；两 PDF 均为 8 页；卡片均为 1950×2700。

## 与构建员自述不符处（均为非阻塞观察，不阻塞）

1. **`build-final-svg.sha` 为 round-6 前旧值（记录口径问题，非纸面问题）。** 该文件所列 p2/p7/p8 哈希（`821e5e5b…`、`cf07d5ea…`、`b36f1489…`）与交付版（`84c0b147…`、`98a81cc6…`、`7c0509b3…`）不符，恰为 round-6 改动的 3 页（撇号页）。交付版 SVG 经本校对独立复现逐字节证实为 round-6 终版；仅构建目录的 sha 记录文件未随终版重渲染更新。建议构建员更新该文件，但不影响定稿。
2. **KIT 可见文本总量差 6 字（计数口径问题，非纸面问题）。** 本校对同法（全部 SVG 文本、去空白）复测：P1–P7 与 KIT 逐页完全一致（3526/3496/3073/3183/3179/3101/3637），P8 为 9241（KIT 称 9247），总量 32436（KIT 称 32442）。6 字差全在 P8，疑为计数口径/版本 vintage 差异；不属于任何一门，且纸面以交付 SVG 为准。
3. **P1 词 gloss 省略“三天”限定词（页面级无丢失）。** 核心中文 gloss 含“一共三天”，分版英文 gloss `a holiday plus the weekend` 未重复该限定；但同一词框内葡语定义句 `… — três dias.` 完整保留，读者在同一框内即可获得该信息，故不构成内容丢失。
4. **边距口径澄清（实测与构建员所称一致）。** 构建员的 L 23.0 / R 13.0 / T 30.0 / B 31.0 px 是相对内框（40..1910 × 40..2660）的全局最小值，而非页边距。本校对页边距实测（L 63.0 / R 52.8 / T 69.8 / B 71.0）换算为框相对值即 L 23.0（P3）、R 12.8≈13.0（P2）、T 29.8≈30.0（P1，0.2px 为超采样取整差异）、B 31.0；页框穿越 0 与此口径下一致。
5. **备案家具英译清单（非冻结内容丢失，逐项列明）。** 除 §1 所述装置外，三处葡语句子被译为英语家具，均合 W43 先例：核心 P1 副标题 `O JORNAL SEMANAL PARA APRENDER — …` 被配对徽章取代（W43 同版式亦以徽章取代副标题）；各版 band 副标题译为英语描述（如 `LEVEL A2 · …`，W43 同式）；P8 页眉行 `第 8 版 · A grande prova da semana + todas as respostas` → `PAGE 8 · The big test of the week + all the answers`（与 W43 P8 页眉行逐字相同）。其余所有葡语文章、练习体、选项、词库、P8 阅读文本与范文均未动。
6. **继承版式观察（核心同位，非分版缺陷）。** P2 末 `D · AS PALAVRAS` 栏目标题位于页底、其配对题在第 4 栏顶部；P4 `B · AS PALAVRAS` 同式。两处坐标与核心逐字节相同，属核心继承版式，无重叠无截断，不阻塞。
7. **P8 key 规范化相同数说明。** 132/150 而非直觉的 148，原因见 §3（伪影项 key 字符串含本地化 gloss 文本）；答案 token 本身 16 项全部相同，不存在额外改动。

## 未做事项（遵任务书）

未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未派生下级代理、未清理共享 scratch 目录；校对全程仅在 `hidden_files/w45/pt-en-proof/` 内写盘。
