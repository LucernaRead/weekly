# 独立校对报告 — Lucerna Weekly W45 EN × PT（VOL.2）

- 校对对象：`files/weekly-report-w45-en-pt/`（SVG×8、卡片×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-en-core/`（VOL.2，刊头 The Lucerna）
- W43 家具对照：`files/weekly-report-en-pt/`（已上架 SVG）
- 校对方式：只校对、不改源码；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）、未清理共享 scratch。
- 开工查重：files/weekly-report-w45-en-pt/ 与 hidden_files/weekly-report-w45-en-pt-build/ 在 75 秒复查内零新写盘（当时唯一活动进程是另一分版 EN×NL 的几何脚本，与本版无关），判定为已完成交付、可以开工，非 stand down。
- 证据目录：本目录（`hidden_files/w45/en-pt-proof/`）内全部日志与 JSON；校对前后哈希 `hashes-before.txt` / `hashes-after.txt` 经 diff 确认**完全一致**（交付物与核心均未变）。

## 结论：ZERO PROBLEMS

全部 10 项必查均通过；阻塞项 0 项。下列 3 条为**非阻塞观察**（均不在版面正文内，不影响上架判断；上架本身由主线串行执行，本报告不宣布上架）：

1. **KIT §4 金句级别 tally 笔误（非版面缺陷）**：KIT 写金句级别为 A2×3、B1×3、B2×2；本校对从核心与本版 P7 实测的 8 句级别序列均为 [A2, A2, B1, B1, B2, B2, A2, B1]，即 **A2×3、B1×4、B2×2**，本版与核心逐项一致。属构建员计数/交接笔误，版面无错标。建议主线在 KIT §4 更正 B1×3 → B1×4（不改版面）。
2. **KIT §8 round-4 基线文件措辞不精确（非版面缺陷）**：`baseline-round4.txt` 的哈希与终态交付物 8/8 相同，实为 round-4 完成后的记录；round-4 真正的修复前基线是 `baseline-round3.txt`（与终态仅 P1 不同，见第 5 项）。实质链条完整，仅 KIT 措辞应为“round-4 完成记录”，修复前基线应指 baseline-round3。
3. **P8 H 组栏头与 W43 有一字之差，但跟核心**：本版 `H · WRITING · Escrita [B1]`，W43 为 `H · WRITING · Escrita`（无 [B1]）；核心 H 组栏头为 `H · WRITING · 写作 [B1]`，故 [B1] 是核心冻结形式，本版跟核心正确，不视为 W43 偏差。

## 1. 冻结

- **标准 freeze.py baseline 字面跑法说明**：直接以 `freeze.py baseline --build …-coreproof/build-copy` 跑出 0/8，原因是该工具的重定向正则只匹配 `files/` 路径，而构建员的 coreproof 副本 OUT 指向 `hidden_files/…/svg`，工具无文件可重定向、产出写回了 coreproof 目录而非 scratch 目录。这是工具正则局限，不是核心不符。
- **同方法新鲜 scratch 独立重跑**：将 coreproof/build-copy 拷入本校对 scratch、OUT 重定向到全新目录后运行 `run.py`，产出与 shipped 核心 SVG **8/8 逐字节相同**（`freeze-manual/`，逐页 OK；核心事后重哈希不变）。冻结基线成立。
- **freeze.py diff**（`freeze-diff.json` / `freeze-diff.log`）：P1 +26/−26、P2 +33/−33、P3 +25/−23、P4 +24/−22、P5 +27/−23、P6 +25/−21、P7 +48/−39、P8 +113/−97；**新增 CJK 全版 0**（核心 CJK 183/197/119/139/134/136/347/776 → 本版每页 0；另用正则直数 8 页 SVG CJK 均为 0）。
- **diff 逐项裁定**（`freeze-diff-adjud.txt` 全量清单）：新增串只分三类——(a) 葡萄牙语家具/讲解串；(b) 短类型/指令 token（Complete、Combine、Reescreva、Corrija 等）；(c) 因葡语括号改变断行位置而产生的冻结英语正文重断行碎片（如 `435 — seats in the House, all on the`，核心同句以不同断行存在；P8 答案行同理，英语 key 句本身冻结、差异在注释语言）。无任何长段新增纯英语正文；删除串镜像对称（中文讲解串 + 同类断行碎片）。冻结成立。
- **违禁词**：`桥接`在全部交付物（SVG、KIT、ABSTRACT）中 0 次；PDF 二进制全文检索 0 次。英语正文冻结、讲解层全葡萄牙语。

## 2. P8

- `tools/p8.py compare` 独立重跑（`p8-compare.log` / `p8-compare.json`）：**CLEAN，noted 78 = 78，missing [] extra 0 uncertain []，keydiff 恰为 [137, 138, 139, 140, 150]**。
- **78 口径独立确立（非采信构建员）**：核心 P8 印刷笔记集实测 78 项 = NOTAS_EXTRA 39 项（≤111，即 P1–P7 题号段）+ P8 本页题 112–150 连续 39 项；P8 页分布 39 与之一致。`content8.py` 钉住规则 `pg == 8 or n in NOTAS_EXTRA` 与该实测集合精确吻合；本版印刷笔记集与核心逐项相等（EXTRA_ONLY 未出现）。
- **keydiff 逐项印刷行对照**（键值取自 p8 extract 的跨行拼接键，与卡片目视一致；P8 印刷 key 1–150 连续无缺）：
  - 137：核心 `耐心是制度的一部分，而不是制度的失败。` → 本版 `A paciência faz parte do sistema, não é uma falha do sistema.`（英句 `Patience is part of the system, not a failure of it.` 的葡译）——合法重定向；
  - 138：核心 `11 月 3日周二是美国的选举日。` → 本版 `Terça-feira, 3 de novembro, é o dia das eleições nos Estados Unidos.`（英句 `Tuesday, November 3, is Election Day in the United States.` 的葡译）——合法；
  - 139：核心 `这周日，NFL 在马德里比赛。` → 本版 `Neste domingo, a NFL joga em Madri.`（英句 `On Sunday, the NFL plays in Madrid.` 的葡译）——合法；
  - 140：核心 `并非每处都拨回时钟。` → 本版 `Nem todos os lugares mudam.`（英句 `Not every place changes.` 的葡译；`Nem todos os lugares mudam.` 较英句略省“时钟”二字，但与 P7 金句 7 及 P2 正文 `Not every place changes.` 的葡语讲解口径一致，且为翻译重定向而非新增事实）——合法；
  - 150：核心 `开放题 — 要点见写作框，范文在第8 版写作框内` → 本版 `Questão aberta: veja os pontos no quadro de redação; o modelo está no quadro desta página`（讲解层写作键）——合法。
  - 无括号分支伪影：五键均为完整印刷键（p8 extract 拼接键与卡片 P8 答案区逐行可对上），非 paren/dash 误切。
- **P8 指令分流与卡片一致**：137 `Translate :`、138 `Traduza:`、139 `Traduza:`、140 `Translate :`，与 KIT 所述分流一致（卡片目视确认）。
- **P8 注释语言裁定**：P8 全页 CJK 0；注释讲解层为葡萄牙语，英语仅以被讲解的词条原文出现（如 `not every = nem todo`、`part of = parte de`），与核心注释“引英语词条 + 中文讲解”的体例功能相同，不视为英语注释层残留。

## 3. 金句级别分布差异专项（已裁定：构建员笔误，非阻塞）

- 从核心 P7 实测 8 句金句（按题号 100–107 顺序）级别序列：100 A2（page 1）、101 A2（page 2）、102 B1（page 3）、103 B1（page 4）、104 B2（page 5）、105 B2（page 6）、106 A2（page 2）、107 B1（page 4）= **[A2, A2, B1, B1, B2, B2, A2, B1]，A2×3、B1×4、B2×2**。
- 本版 P7 同 8 句级别与页标签逐项相同：页标签 page 1×1、page 2×2、page 3×1、page 4×2、page 5×1、page 6×1，级别 A2×3、B1×4、B2×2。
- 结论：差异来源是构建员 KIT/交接中的计数笔误（B1×3），**本版无真实级别错标**，记为非阻塞观察 1。

## 4. 几何

- `tools/occlusion_audit.py` 自检先行通过（六类合成正例全触发、干净对照静默）；分版 0 flags、核心 0 flags、**NEW 0**（`occlusion.log` / `occlusion.json`；核心单跑亦 0，`occlusion-core.log`）。
- 补充扫描（构建员 supplemental.py 在交付物上重跑，`supplemental-rerun.txt`）：rowcheck **0**；P6 图表标签基线锚定（PIL getmetrics，anchor ls）覆盖 **0.0%**（门限 <30%；四条标签 38/29/21/12% 逐条 0.0%）；edgescan flags **0**（P1–P7 最大 advance-right 均为 1885.0 即框线本身）。
- **P8 1899.4 / 1903.8 两处**：与核心逐字逐值相同——`b. an election in the middle of a term`（1899.4）、`d. the paper you mark your choice on`（1903.8），为核心原有冻结英文匹配项，非新增（核心补充扫描输出完全相同）。
- **第 3 轮词标/副标 TEXTX 伪旗终态消除**：终态 occlusion 0 旗（含 TEXTX 类）即为消除证明；另见第 5 项像素复核（词标墨迹止于 y=301，副标墨迹起于 y=303，中间 y=302 为空行，无触碰）。

## 5. 第 4 轮副标位移专项

- 副标确为家具非冻结文本：核心同槽为中文家具串 `英 语 周 报 · VOL.2 · 选 票 · 足 球 · 电 影`（y=330）；本版副标 `SEMANÁRIO EM INGLÊS · VOL.2 · VOTOS · FUTEBOL · CINEMA` 为其葡语家具化，**y=338（+8px）** 已在交付 SVG 中确认。
- 位移后上下净空（卡片像素实测，`p1-subtitle-pixel.txt`）：词标墨迹止于 y=301、副标墨迹起于 y=303（空行 y=302）；副标墨迹止于 y=338、徽章墨迹起于 y=353；徽章墨迹止于 y=371、横线 y=390–393——均无压线。
- 词标/横线/徽章不动：词标 `The Lucerna` y=262、徽章 y=372、横线 y=392/401 与 W43 同槽坐标一致；transform.py 第 4 轮配对仅改副标一行（330→338）。
- **变化范围确仅 P1**：`baseline-round3.txt`（round-4 修复前）与终态对比，仅 p1-front.svg 不同，其余 7 页字节不变（见非阻塞观察 2 关于 baseline-round4 文件措辞的说明）。

## 6. gloss

- 渲染后按 `·` 拆分、跨行拼接逐项重数（`gloss2.txt`，方法：以 `Nota —` 起始行起连续同 x/字号行拼接；核心以 `译注｜讲解｜` 同法拼接）：
  - 核心：P2 3、P3 4、P4 4、P5 3、P6 4，合计 18；
  - 本版：P2 3、P3 4、P4 4、P5 3、P6 4，合计 **18 = 18**；
  - 英语词头逐项 1:1：fall back / costume / trick or treat；open / monster / catchphrase / series；fixture / title / defend / fan；map / too close to call / second screen；register / governor / shape laws / patience。
- 分布数字为本校对从核心独立实测所得，非照搬构建员数字（结果与之一致）。

## 7. P7

- 定义句逐字保留：A2 FALLING BACK / GOING TO + VERB、B1 COMPARATIVES / THE PAST SIMPLE、B2 HEADLINE PRESENT / WHETHER = IF ? 六栏定义句在核心与本版逐行相同；唯一本地化为 B2 例框 gloss `part of = uma parte (page 6)`（核心 `part of = 一部分 (page 6)`），其余例框句（A2 `— the election story, from page 1.`、B1 `— fall → fell (page 2).`）逐字相同。
- 金句 8 句原文逐字 + 页标签 + 级别：见第 3 项，全部与核心逐项一致。
- 作用域计数（`gloss-phrases.txt`）：8 句在正文页（P1–P6）各出现 1 次 + P7 句槽 1 次 = **各 2×**；第 6 句 `Patience is part of the system, not a failure of it.` 在 P7 内另有 B2 例框引用（P7 内计 2 次），与核心完全一致。
- P7 结构与核心一致：3 级栏 + 例框 + TOOLBOX（3 句按级各一）+ PHRASES（8）+ ERROR CLINIC（4，108–111）+ READERS' CORNER + VOL.3 预告；P7 CJK 0。

## 8. 读者园地

- 核心英语信件段落逐字保留（含自带披露从句与署名），核心与本版三行完全相同：
  - `« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader`
  - `in Chicago (editor's example : no real reader letters had arrived when this issue`
  - `went to press, so the example stays, honestly labeled)`
- 葡萄牙语披露句逐字摘录（P7）：
  - `Nota da redação: a VOL.1 prometeu cartas reais na VOL.2, mas não chegou nenhuma carta real nem o melhor texto da página 8 da VOL.1; não inventamos nada e o exemplo segue marcado. Envie sua carta e seu texto! Na VOL.3 publicaremos as cartas recebidas.`
- 逐项核实：3 事实齐全——(1) 未收到真实来信；(2) 未收到 VOL.1 第 8 页最佳文本；(3) 未编造、示例保持标记；显性祈使邀请 `Envie sua carta e seu texto!` 存在（内容预告行 NEXT WEEK 未计入邀请）；VOL.3 刊登承诺 `Na VOL.3 publicaremos as cartas recebidas.` 存在。
- **最佳 P8 作文覆盖范围裁定**：披露句的 `o melhor texto da página 8 da VOL.1` 覆盖“VOL.1 第 8 页写作（H 组）投稿中的最佳文本”，与核心中文披露句 `VOL.1 写作投稿` 的范围对应（VOL.1 的写作投稿即其 P8 H 组作文），无缩小、无扩大。
- 无编造、无凭空新写英语披露句：本版无核心之外的英语披露句；P7 内英语除冻结正文/词条外无新增披露内容。

## 9. 家具（W43 偏差清单逐项核实）

- 刊头副标：`SEMANÁRIO EM INGLÊS · VOL.2 · VOTOS · FUTEBOL · CINEMA`（VOL.2 + 本周主题），y=338（见第 5 项）；词标 y=262 与 W43 一致。
- 徽章：`TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`，y=372，与 W43 逐字同坐标。
- 页脚：`The Lucerna · SEMANÁRIO INGLÊS VOL.2 · TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS` + `Página {n} de 8`，除 VOL.2（期次推进）外与 W43 形式一致；顶条 `WEEKLY IN ENGLISH · UM NÚMERO POR SEMANA · O INGLÊS QUE A AMÉRICA LÊ` 与 W43 逐字一致。
- P6 栏：左部跟 W45 核心 `DEEP READ`，右部保留 W43 的 `Leitura profunda`（W43 左部为 `IN DEPTH`，属核心跟随项，非偏差）。
- NEXT WEEK：`NEXT WEEK · Na próxima semana, o VOL.3`（W43 为 VOL.2，期次推进正确）。
- PDF 名：`The-Lucerna-VOL2-PT.pdf` / `The-Lucerna-VOL2-PT-web.pdf`，跟 W45 英族命名（W43 为 `Lucerna-VOL1-PT.pdf`）。
- 五处家具缩短在框验证（`furniture2.txt`）：数字框标题 `THE WEEK IN NUMBERS · Números` 止于 946.3、框右缘 961（内收约 14.7px）；P5 框 `TOO CLOSE TO CALL · Disputado` 止于 458.9、框右缘 499（内收约 40.1px）；P6 框 `A PRACTICE BALLOT · Cédula` 止于 881.1、框右缘 961（内收约 79.9px）；暗带行 1 `Terça de eleições · Relógios atrasados` 与左串间隔 154.2px（左串止于 1243.9、右串起于 1398.1）；搜索脚注 `Interesse relativo, não números exatos.` advance-right 1818.1（< 1885 内框）；P1 数字括号 `ballot (todos em disputa)` / `in São Paulo (dois eventos no domingo)`、P2 桥接句 A `Complete em inglês conforme o horário.` / C `Leia o artigo da página 2 e responda.` 均为单行且在框内；语义未变。
- 其余家具与 W43 形式一致：gloss 前缀 `Nota — ` + 逗号式（`word, explicação · …`）；P7 栏头（LEVEL A2 · Base / B1 · Avançando / B2 · Desafio；THE EXAMPLE · O exemplo；THE TOOLBOX · Ferramentas；PHRASES OF THE WEEK · Frases da semana；THE ERROR CLINIC · Clínica；READERS' CORNER · Cantinho dos leitores）与 `Gramática — ` 前缀（8 句全有）；P8 栏头（A Complete o texto / B Escolha / C Compreensão / D Frases / E Tradução / F Associação / G Diálogo / H Escrita [B1]，其中 [B1] 跟核心，见非阻塞观察 3）、分隔符 `— Página {n} —`（8 个齐全）、半角括号注释式（核心为全角）。
- P6 `☐`、P7 `✗`：核心与本版计数均为 ☐×4、✗×4，属核心冻结字符的字体渲染原样（卡片上均呈空心框形），非新缺陷。

## 10. 图片、ABSTRACT、卡片目视、题量、范文、PDF

- 图片载荷：5 图逐页 base64 载荷哈希与核心逐页相等（P1 投票亭、P2 万圣节明信片、P3 马奈猫图、P4 1910 橄榄球、P6 国会大厦）；署名行与核心逐字相同（Kenneth C. Zirkel — CC0；Édouard Manet — CC0；Frank R. Snyder — public domain；P2/P6 Public domain，均注 via Wikimedia Commons；P3 图注含“非电影美术”说明与核心一致）。
- ABSTRACT（`ABSTRACT.txt`，421 字节，单行、无 ASCII 双引号）：含 11 月 3 日中期选举、11 月 1 日拨钟、万圣节、11 月 6 日两部电影（The Cat in the Hat、Godzilla Minus Zero）、11 月 8 日 NFL 马德里与 F1 圣保罗、美国如何投票（`como a América vota`）等真实主题关键词 + 学习者搜索短语 `aprenda inglês lendo notícias dos EUA` + A2–B2 + `150 exercícios`，逐项核对全有（`essay-abstract-pdfs.txt`）。
- 8 卡片全部逐页目视（非抽查）：P1 刊头/暗带/数字框/图片/页脚干净；P2 时钟图/Nota 框/练习区干净；P3 马奈图/Nota 框/练习区干净；P4 1910 球赛图/Nota 框/练习区干净；P5 Nota 框/Disputado 框/练习区干净；P6 选票框（☐ 原样）/图表/练习区干净；P7 三级栏/金句/诊所（✗ 原样）/读者园地/预告干净；P8 终测/范文框/答案区干净。无溢出、重叠、压页脚、裁切。
- 题量独立展开计数：本校对在 scratch 中重跑已变换的 PT 构建源（`pt-rerun/`，OUT 重定向，交付物未动），产出 SVG 与交付物 8/8 字节相同，且注册表统计为 **150 题、A2 60 / B1 69 / B2 21、页分布 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39**、类型分布与 KIT 一致；重跑日志零 FLOW OVERFLOW、零 HEAD TOO WIDE（构建员 round-4 日志亦同为零）。
- 范文：`My Tuesday, November 3` 在 P8 MODEL 框逐字出现（核心与本版各 1 次），范文正文 85 词（`On Tuesday, November 3, … and a very American one.`），与核心逐字相同。
- 双 PDF：均为 8 页；print PDF 17,295,650 B、sha256 `ed231eafd83df10cd62dc3cfd7a595263099efdda98c7086d42c9bf1079ae5c9`；web PDF 4,008,688 B、sha256 `a91be6abb1e0adb8a8c1850ab3f34114748fbef86394453ffc111a5c56fc93c9`；与任务书及 KIT §7 一致。
- 解释器：`tools/venv/bin/python` = Python 3.12.3、Pillow 13.0.0、cairosvg 2.9.1、pypdf 6.21.2，与 KIT 记录一致（本校对全部工具运行均用该 venv）。
- 校对前后哈希：交付物 + 核心 `hashes-before.txt` vs `hashes-after.txt` diff 为空，**校对前后不变**。

## 非阻塞观察汇总（重申，不阻塞）

1. KIT §4 金句级别 B1×3 应为 B1×4（版面正确，仅 KIT 笔误）。
2. KIT §8 中 `baseline-round4.txt` 实为 round-4 完成记录，round-4 修复前基线是 `baseline-round3.txt`（实质链条完整）。
3. P8 H 组栏头 `[B1]` 与 W43 差一字但跟核心冻结形式，正确。

## 未做事项（按任务约束）

未宣布上架；未发 Discord；未往主聊天发卡片/PDF；未建 cron；未碰 weekly-git；未改核心/W43 目录；未派生下级代理；未清理共享 scratch 目录。
