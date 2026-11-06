# Le Lucerna · 法语周报 VOL.3 — 英语讲解版（FR × EN）WEEKLY KIT

**状态：builder-complete，NOT finalized**——定稿由独立校对决定，本构建不宣布上架。

**版本定位**：VOL.3「决赛周末」（2026 年 11 月 2–8 日，2026-W45）的**英语母语读者版**。同一法语核心（`files/weekly-report-w45-fr-core/`，VOL.3），讲解层换成英语——生产矩阵中的 FR × EN 一格。法语核心定稿结论（四轮校对 + 第二轮复校零问题，见核心 KIT §8）直接继承；本文件只记录本版的规格、改动边界与验证。

## 一、本版规格

| 项 | 内容 |
|---|---|
| 版数 / 版面 | 8 版，1950 × 2700，四栏，暖象牙纸色——与核心版完全相同 |
| 配对 | **法语正文 × 英语讲解**（目标语 = Français，读者母语 = English） |
| 刊头配对徽标（第 1 版，深色横幅下方，砖红色居中） | **"Text in French · Explanations in English — the edition for English-speaking readers"**（y=574，22pt BRICK #a4553a，加粗，居中——与 W43 同配对版、W45 核心实测三方一致，见第三节） |
| 每版页脚 | 左：`Le Lucerna · FRENCH WEEKLY VOL.3 · TEXT IN FRENCH · EXPLANATIONS IN ENGLISH`；右：`Page N of 8` |
| 讲解层 | 全部译注（NOTE · 前缀）、词表注释、题干说明（Fill in / Rewrite / Match / Correct it）、栏目说明、易错诊所说明、读者园地英文点评与说明、下期预告附注、第 8 版全部答案简析——**100% 英语**（渲染 SVG 文本节点 CJK = 0；登记表题型名等不出报的内部元数据沿 W43 先例保留中文原样） |
| 栏目头 | 法语 + 英语双语（与 W43 同配对版体例一致），如 `À VOUS ! · YOUR TURN`、`DIRE LA DATE · SAYING THE DATE`、`LANGUE EN MAIN · LANGUAGE IN DEPTH` |
| P8 形式 | 分隔 `— PAGE n —`；简析括号半角加空格 ` (note)`（W43 校对修正形式）；印出简析集合 = 核心集合的显式复现（见第四节） |

## 二、实测量化（与核心 KIT 同一口径）

- **练习总量：150 题**，与核心逐题一致：编号 1–150 连续、逐版分布 **10/15/18/18/17/18/12/42**（P2 15、P5 17、P8 42——FR 串，与通用串不同）、级别分布 **A2 53 · B1 75 · B2 22**、题型分布（完成句子 49 · 单选 26 · 词汇配对 21 · 完形填空 8 · 句型转换 7 · 图表读数 6 · 阅读判断 5 · 阅读理解 5 · 翻译 5 · 对话补全 5 · 跟练 8 · 改错 4 · 写作 1）均与核心登记表一致（构建驱动 REG 实测）。
- **范文逐字 = 核心**：P8 MODÈLE 范文（86 词，`Mon week-end du 7–8 novembre`）经 joined-text 比对与核心逐字相同。
- **Gloss 逐项计数**（README #21：gloss() 调用串按 `·` 切分）：P1 7 · P2 6 · P3 6 · P4 7 · P5 6 · P6 6，**合计 38 = 核心 38**，逐盒相等。
- **全文 CJK**：8 个 SVG 文本节点 CJK = 0。

## 三、家具三方对照（W43 同配对版优先于 #20 泛化）

| 家具 | README #20 泛化 | W43 FR×EN 实测 | W45 核心实测 | 本版采用（实测） |
|---|---|---|---|---|
| 配对徽标 | FR 族：INSERTED y=574、22pt BRICK | y=574、22pt、#a4553a、bold、middle，英文串 | y=574、22pt、#a4553a、bold、middle，中文串 | y=574、22pt、#a4553a、bold、middle，英文串——**三方几何一致**，仅读者母语文字不同 |
| 页脚左 | — | `Le Lucerna · FRENCH WEEKLY VOL.2 · TEXT IN FRENCH · EXPLANATIONS IN ENGLISH` | `Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文` | VOL.3 的英文同构串，8 版实测一致 |
| 页脚右 | — | `Page N of 8` | `第 N 版 / 共 8 版` | `Page N of 8`，8 版实测一致 |
| Gloss 前缀 | — | `NOTE · ` | `译注｜` | `NOTE · `（bslib4 gloss()，与 W43 一致） |
| P1 顶栏 | — | 左 `VOL. 2 · ISSUE NO. 2`；中 `HEBDOMADAIRE EN FRANÇAIS · EVERY WEEK · READ THE FRENCH THE FRENCH READ` | 左 `VOL. 3 · 总第 3 期`；中 `HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语` | 左 `VOL. 3 · ISSUE NO. 3`；中沿用 W43 英文串 |
| P1 副标题 | — | `FRENCH WEEKLY · VOL.2 · DEEP AUTUMN & FESTIVALS` | `法 语 周 报 · VOL.3 · 决 赛 周 末` | `FRENCH WEEKLY · VOL.3 · FINALS WEEKEND` |
| P1 顶栏同基线间距 | — | — | — | 左/中/右三段同基线 y=92 间距分别为 246.5px / 95.7px，无重叠（canonical ink_box 实测） |
| P8 分隔 / 括号 | — | `— PAGE n —` / ` (note)` | `— 第 n 版 —` / `（note）` | W43 形式 |

## 四、零差异验证与 P8 双门

1. **核心完整性**：核心版全部无 CJK 文本节点在本版中逐字出现，唯一例外 15 个节点全部为 (a) 中文讲解段落的换行尾标点 `）。`（P3/P7 各 1，属已替换的讲解层）或 (b) P8 答案串因英语简析较长而换行点移动的重排片段（13 个）——无一法语键丢失。核心 SVG 在构建前后 sha256 8/8 不变（`core-prebuild.sha` 全 OK）。
2. **冻结**：全部法语正文零删失、零改写。FR 族已裁定事实逐项在位：P4 `41e édition en 2026 (40e anniversaire)`（全文唯一版次主张；`40e` 其余出现：P3/P7/P8 的 `anniversaire` 生日语境 6 处、题号 `40.`/`140–144.`、22e 扇贝节、15e Pitchfork 均保留）；P7 引文 #4 为 P4 辩论框逐字 `plus excitante ou plus frustrante ?`；#8 用 P5 逐字 `Les jeunes créateurs y rencontrent leur public, en vrai.` + Q106 改写（error `rencontre`，key `rencontrent`）；P6 同步为 `Ce calendrier peut encore bouger.`（P6 深读小写形与微习题键 `peut` 非引文、未动）；Q120 题干 `Si j'étais libre dimanche, j'___ à Nanterre.`、选项 `irai / irais / vais`、键 B、P8 注释 `si + imparfait → conditionnel; j' = je elided`；Q119/Q121 不动；P7 `2×` 指源文章 + P7 表格对（教学栏/工具箱重复 #1/#2/#4/#6 是 KIT 设计、非缺陷）。
3. **P8 双门（FR 族专属，BINDING）**：
   - ① plain `tools/p8.py compare`（显式 `--core-p8/--edition-p8`，`--total 150`）：**CLEAN，noted 97 = 97**，missing=[]，extra=0，keydiff=[135, 150]。
   - ② `hidden_files/w45/p8-fr-gap-fix/keycompare.py`（全 150 键）：mismatch 2 项，恰为上述 [135, 150]，**裸键 53 条零 mismatch**。
   - 裁定：135（法译中题答案键：中文译文 → 英语译文 `Reading a programme is already a way of understanding France.`）与 150（写作题答案键：中文指引 → 英语指引）均为读者语言层重定向，沿 W43 先例（该版 5 项）合法；其余 148 键逐字相同。**双门通过**（plain ∈ {CLEAN} 且零裸键 mismatch）。
   - 裸键清单（53 条，与核心渲染独立核对一致）：2, 5, 6, 9, 12, 15, 16, 18, 20, 22–26, 29, 30, 35–41, 43, 45–52, 54, 61, 62, 64–66, 73, 75, 76, 85, 86, 88, 89, 91, 97–99, 101–104。
   - 实现：本版 P8 以显式 `PRINT_NOTES` 集合（核心 noted 集，`tools/p8.py extract --json` 实测 97 项）印出简析，不依赖英语简析长度规则——否则英语简析普遍 >10 字符会使印出集缩水（W43 同法）。
4. **翻译题重定向**（读者语言面，法语键不变）：135 题键改为英语译文；136–139 题题面中文待译句改为英语待译句（`He runs faster than his brother.` / `The pupils have been on holiday since 17 October.` / `Tonight, we are going to prepare our schoolbags.` / `People do not know who the finalists are yet.`），法语键逐字不变；150 题写作指引英文化。以上即 keydiff 的全部内容。
5. **讲解语言审计**：渲染 SVG 全文 CJK = 0；逐版看图复核讲解层无中文残留；报纸版面（8 SVG）无任何中介措辞——“桥接”一词不出报（SVG grep = 0；本 KIT 此句仅为合规记录，不属于版面）。

## 五、几何门禁（全部实测值）

- **构建警告**：最终驱动**零 FLOW OVERFLOW / HEAD TOO WIDE**（P1-hiver 2298 与 P6-ex 2557 两处 flow 终值与核心逐字相同，属核心继承余量：距页脚线 2580 分别 282px / 23px，卡面确认无压线）。
- **Canonical 遮挡审计**（`tools/occlusion_audit.py`，自检先行通过）：本版 **0 flags**，核心 0 flags，**NEW vs core = 0**。首轮实测 12 NEW flags 全部为英语标题过宽的真缺陷，已逐项修复（见第七节）。
- **同基线行首检查**（FR×RU 教训）：P1 顶栏三段与 8 版页脚左右段同基线间距全部 >0（最小 95.7px），无重叠。
- **ADVANCE 全页右缘扫描 + 全页框线扫描**（nl-pt B1 教训）：右缘（>1885）仅 P8 F 组 3 行法国原文配对行（ink right 1891.2/1899.5），与核心**逐字节相同的墨迹值**（核心同行同值），属核心继承几何、非本版缺陷，框线扫描 0 穿越（外框 1922 内无墨）。
- **P6 图表标签基线锚定覆盖**（getmetrics 基线锚定法，非 getbbox 法）：全部 12 个图表文本元素覆盖 **0.0%**（<30% 门）；图表为纯文字行、无柱体遮挡。
- **行首 kinsoku**：本版新增行首孤儿标点 **0**；4 处行首 `:`（P3 图说、P4 微练习、P5 指南、P7 B1 栏）与核心同页同 y 逐字相同，属冻结法语换行继承。
- **P8 答案流末端 2489**（<2540 门，底线 2545 内）；P7 预告末端：读者园地框 + 预告条均在页内（P7 卡面确认，预告条 2270–2540，页脚线 2580 之前）；P5 主流末端 2532（<2540）；P2 练习流 2365；P7 金句流 1574（<1830）、诊所流 2140（<2268）。
- **全 8 卡目视**：P1–P8 整版逐版看图，无重叠、无压线、无出框；另有 9 处裁图复核（P1 顶栏、P1 图文交界、P2 ET VOUS/日期行、P6 图表、P7 读者园地、P8 电池/写作条、P8 配对行、P8 答案末端、P5 页底）。

## 六、图片

仅明确公有领域图片，与核心同 3 张、同法语图说与出处、同 base64 内嵌，载荷哈希双口径一致（base64 文本 sha256 前 16 位与解码 JPEG sha256 前 16 位均与核心相同）：

| 版 | 内容 | 作者/出处（Commons Artist 字段原文） | 授权 | 解码字节 |
|---|---|---|---|---|
| P1 | 巴黎街道老照片 | Eugène Atget (1857-1927), photographie | Public domain | 334,674 |
| P2 | 浮世绘《真间川红叶》 | Utagawa Hiroshige (1797-1858), estampe · LACMA | Public domain | 646,242 |
| P3 | 菊花植物图谱 | Flora de Filipinas (Blanco), XIXe siècle | Public domain | 142,340 |

三图均已在 SVG 中核实放置（`<image>` 元素 + 图说 + credit 行齐全）；授权明细随核心 KIT 第六节（W43 素材库 Commons 元数据核过）。

## 七、修复轮记录（fix-round 编辑全部进 transform.py，单源头）

- **Round 1（初译）**：transform.py §1：核心构建复制 + OUT 重定向 + 讲解层中→英全量映射（298 项断言替换：bslib4 3 + content12 57 + content34 81 + content56 68 + content7 30 + content8 59）+ bslib4 页脚/gloss 前缀 + P8 显式 PRINT_NOTES。首轮渲染：150 题；P1 溢出、P6/P8 宽头警告、P8 keys 2570。
- **Round 2**：P1 gloss 缩短（未计 `NOTE · ` 前缀，仍 6 行——无效轮，见 Round 3）；P6 读日程头改为 `LIRE LE CALENDRIER · SCHEDULE`（text_w 422 ≤ 434）；P8 电池头改为 W43 短式（MCQ / SENTENCES / COMPLETION）；P8 keys 长注缩短 9 处 → keys 2489。
- **Round 3**：P1 gloss 再缩短为 bare 式，**含 `NOTE · ` 前缀实测 5 行** → P1 headline 流 1939 → 1588，溢出消除。
- **Round 4（遮挡审计 12 NEW flags 全修）**：P1 日期框题 `LES DATES · FINALS WEEKEND`；P2 ET VOUS 英文注由 5 行缩为 2 行（`Where were you Monday morning? What did you read? Write two sentences.`），col3 末端 1625.6 → 1538.6（<1558 规则线）；P3 词表题 `LES MOTS DES FÊTES · FESTIVAL`、日历题 `DATES À RETENIR · TO REMEMBER`；P4 `LES MOTS DU TENNIS · TENNIS`；P5 `MOTS DE LA MUSIQUE · MUSIC`、`PARIS CREATOR WEEK`（单名）；P6 图表题 `LE CALENDRIER PRÉVU · PLANNED SCHEDULE (NO RESULTS YET)`（text_w 856 ≤ 961）。复审：审计 0 flags，NEW 0。
- 每轮修复前均存全量 pre-fix SVG sha256 基线（`pre-fix-round2/3/4.sha`）；构建树未 reset；仅 P1/P2/P3/P4/P5/P6/P8 的 SVG 哈希在各轮中变化，P7 SVG 自首轮后未变。

## 八、复现构建与工具链

构建树：`hidden_files/weekly-report-w45-fr-en-build/`（`transform.py` 单源头 + 内容模块 + `build1/2.log`、`occlusion*.json`、`keycompare.json`、`freeze-diff.json`、`checks2.py`、裁图）。

```bash
# 1. 从核心构建复制（禁在核心构建目录内 import 内容模块）
cp hidden_files/weekly-report-w45-fr-build/*.py hidden_files/weekly-report-w45-fr-en-build/
# 2. OUT 重定向 + transform（round 1→4 顺序执行；单进程驱动是唯一渲染入口）
cd hidden_files/weekly-report-w45-fr-en-build
TRANSFORM_ROUND=1 ../../tools/venv/bin/python transform.py
TRANSFORM_ROUND=2 ../../tools/venv/bin/python transform.py
TRANSFORM_ROUND=3 ../../tools/venv/bin/python transform.py
TRANSFORM_ROUND=4 ../../tools/venv/bin/python transform.py
../../tools/venv/bin/python -c "import content12, content34, content56, content7, content8"   # 生成 8 个 SVG，零警告
# 3. 卡片 + 双 PDF（与核心 KIT 同法；网页版 JPEG q75，Pillow 默认质量——原 KIT 误记 q72，2026-10-27 网页版重建时订正，见第十三节）
#    cairosvg svg2png (1950宽) → svg2pdf + pypdf 合并为大报版；整版 PNG 转 JPEG q75 封装为网页版
```

工具链裁定：渲染 SVG 的驱动解释器与卡片/PDF 渲染解释器**均为 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）**；系统 python3（同为 3.12.3）无 cairosvg，不可用于 render.py。审计测量用 venv PIL（与渲染同一 venv）。

## 九、交付物

交付目录 `files/weekly-report-w45-fr-en/`：`svg/` 8 个源文件 · `cards/` 8 张整版 PNG（1950×2700）· `Le-Lucerna-VOL3-EN.pdf`（8 页大报版，**9,746,058 字节**，SHA-256 `e9fb978109ddfea4874083bc210f1e34fc378d7845b09b1c6bf248d713a7e45b`) · `Le-Lucerna-VOL3-EN-web.pdf`（8 页网页版，**5,249,227 字节**，SHA-256 `16d77b11fe93a5108cbbfc616d8864aab96c97ccfece5b6f3c0afbd6e5929d7d`；2026-10-27 网页版重建后，旧值见第十三节）· `ABSTRACT.txt`（英语单行，无 ASCII 双引号）· 本文件。

## 十、与 W43 同配对版的偏差清单（非缺陷，均为本期/语言层事实）

1. 期次与内容：VOL.3（11 月 2–8 日决赛周末）vs VOL.2（10 月 19–25 日深秋与节日）；题量 150 vs 145；逐版分布 10/15/18/18/17/18/12/42 vs 10/16/18/18/17/18/11/37；级别 A2 53/B1 75/B2 22 vs A2 55/B1 65/B2 25；P8 noted 集 97 vs 67（核心决定）。
2. 家具：徽标串、页脚式、gloss 前缀、P8 分隔/括号式与 W43 逐字同构，仅 VOL 号不同；P1 副标题主题词不同（FINALS WEEKEND vs DEEP AUTUMN & FESTIVALS）。
3. 读者园地状态不同：W43 刊登真实读者投稿（L. M.）；本期核心因 W44 未出刊、未收到 VOL.2 投稿，刊登标注明确的编辑部示例 + 法英双语延期披露 + 明确征集句（见十一节）——此为核心继承状态，非本版改动。
4. 翻译重定向项数：本版 2 项（135、150）vs W43 的 5 项（核心题型结构不同）。
5. 版面适配缩短（仅讲解层措辞）：P1 gloss、P1/P3/P4/P5/P6 框题、P6 读日程头、P8 电池头、P2 ET VOUS 注、P8 长注——均由英语较长引起，法语与版式参数不动（见第七节）。
6. 网页版压缩：JPEG q75（Pillow 默认质量；原 KIT 误记 q72，2026-10-27 重建时订正，见第十三节）；W43 英文版 KIT 记录为 q85——方法差异，不影响内容。

## 十一、P7 读者园地核查（逐字摘录）

- **标注的编辑示例**（法语，冻结）：“« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).”
- **无真信/无最佳 P8 作文的延期披露**（法语 + 英语双语，均印在园地框内）：
  - FR：“Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.”
  - EN：“Editor's note: no VOL.2 texts had arrived by press time (no W44 issue), so this issue prints a labelled editorial example; VOL.4 will comment on real submissions.”
- **明确的公开征集祈使句**（逐字，园地框英文点评末句）：“Send us your letter for VOL.4!”
- **范围裁定**：征集句本身即在 P7 园地框内、字面覆盖读者来信，无需借助他页提示或 teaser 组合；P8 写作条“Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »)”与预告条“Et vos lettres, enfin !”与之同向，均指向 VOL.4——VOL.4 承诺覆盖范围 = VOL.2 投稿（如收到）+ 本期 P8 写作投稿的真实点评；本期示例不得冒充。
- **VOL.4 兑现清单**（核心交接，本版原样继承）：巴黎大师赛周末结果、国民议会预算周表决结果与参议院社保预算审议、读者园地真实投稿点评。

## 十二、未决观察（供独立校对，不 blocking 本构建结论）

1. P8 F 组 3 行法国原文配对行墨迹右缘 1891.2/1899.5，超出名义栏右缘 1885 但在页框（1922）内，且与核心逐字节同值——属核心继承几何，canonical 审计 0 flags；若校对坚持栏右缘为硬门，需动法语原文换行（冻结层，构建员无权擅动）。
2. P1-hiver 2298 / P6-ex 2557 / P5-main 2532 / P8-battery 1497 四处 flow 终值超名义底线但未超页脚线，卡面确认无压线；其中前两处与核心逐字相同，P8-battery 超 12px 经裁图确认为末行基线仍在写作条规则线（1486）之上。
3. 4 处行首 `:` 为冻结法语换行继承（与核心同页同 y），非本版新增。
4. 网页版 PDF 以 q75 封装（Pillow 默认质量；原 KIT 误记 q72，2026-10-27 重建时订正，见第十三节）；若入仓要求与 W43 英文版一致的 q85，需主线裁定后重渲（内容不变，仅 pdfBytes/pdfSha256 变化）。

## 十三、修复轮记录 Round 5（2026-10-27，仅网页版 PDF 重建——校对 NOT PASS 阻塞项修复）

- **触发**：独立校对报告（`hidden_files/w45/fr-en-proof/REPORT.md`）结论 NOT PASS，唯一阻塞项 §1：旧网页版 PDF 第 1–7 页为红/黄/绿/蓝横向块状噪声、无文字结构（pdftoppm / pdfimages+PIL / ffmpeg 三路径一致；p1 与卡片 p1 像素差 115.67；p1 流与新鲜 q75 卡片编码相比仅头部 + 前约 500 扫描字节相同、其后 99.23% 字节不同），第 8 页正常；其余全部校对门已通过。
- **Pre-fix 基线**：重建前已存交付目录全部 20 项 sha256 到构建树新文件 `hidden_files/weekly-report-w45-fr-en-build/pre-fix-webpdf-round5.sha`（旧 `pre-fix-round2/3/4.sha`、`core-prebuild.sha` 未动、未 reset）。
- **修复范围**：仅用交付卡片（`cards/` 8 张 PNG，1950×2700 RGB，未动）重建网页版 PDF；SVG×8、卡片×8、印刷 PDF、ABSTRACT 均未触动（修复后逐项比对 pre-fix 基线全部 OK，见下）；本 KIT 仅增加本节 + 订正 q72→q75（第八节、第九节网页版行、第十节第 6 项、第十二节第 4 项）。
- **旧网页版 PDF**：`Le-Lucerna-VOL3-EN-web.pdf`，**5,310,932 字节**，SHA-256 `e390000bec5b31c63023803233abd1b13fe7703028cd0a2bc342506034554917`，8 页，936×1296 pts。
- **新网页版 PDF**：`Le-Lucerna-VOL3-EN-web.pdf`，**5,249,227 字节**，SHA-256 `16d77b11fe93a5108cbbfc616d8864aab96c97ccfece5b6f3c0afbd6e5929d7d`，8 页，936×1296 pts，PDF 1.4，Title `Le-Lucerna-VOL3-EN-web`。入仓时重 pin 此 pdfBytes/pdfSha256；印刷 PDF 哈希不变。
- **配方（实际采用，非虚构）**：`tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）打开 8 张交付卡片转 RGB，按 p1–p8 顺序 `Image.save(..., "PDF", save_all=True, append_images=[p2–p8], resolution=150.0, title="Le-Lucerna-VOL3-EN-web")`；未显式传 quality，即 Pillow 默认质量。实测默认质量 = q75：默认编码的卡片 p1 JPEG 与显式 q75 编码、与校对 `scratch/card1-q75.jpg` 三者逐字节相同（SHA-256 `da5e155cf950ac790457fd6fdee570521c6a15cedf56dcb5aaf38a123e49033f`，668,716 字节）。另以系统 python（Pillow 10.2.0）同配方重建对照：8 页 JPEG 流逐字节相同，仅 PDF 头版本串差 7 字节（文件 5,249,212 vs 5,249,205 字节，未交付版），故交付的 venv 版与校对验证过的配方输出一致。
- **验证值（新网页版 PDF，交付文件实测）**：
  - pdfinfo：8 页，936×1296 pts，与原版一致；8 页内嵌图像均为 JPEG baseline DCT（SOF0）、1950×2700，与原版规格一致；页内 JPEG 流字节数：p1 668,716 / p2 652,975 / p3 601,207 / p4 650,731 / p5 540,507 / p6 578,319 / p7 663,693 / p8 888,639。
  - pdftoppm -r 150 全页渲染（1950×2700，与卡片同尺寸直接比对）均值 RGB 全部纸色：p1 (219.4, 214.0, 199.1) / p2 (226.9, 221.4, 205.8) / p3 (230.0, 224.5, 209.1) / p4 (229.6, 224.0, 208.2) / p5 (232.4, 226.9, 211.6) / p6 (231.9, 226.2, 210.8) / p7 (222.0, 216.7, 201.5) / p8 (226.7, 221.1, 205.5)；全分辨率与卡片均值绝对差：p1 6.388 / p2 6.228 / p3 5.773 / p4 6.335 / p5 5.141 / p6 5.452 / p7 6.562 / p8 9.597——p1–p7 与已知干净的 p8 同级，旧版 p1–p7 同口径为 100.5–132.0（噪声）。
  - 校对口径下采样比对（pdfimages 提取 JPEG vs 卡片，均缩至 195×270 下采样均值绝对差）：p1 0.687 / p2 0.689 / p3 0.687 / p4 0.700 / p5 0.710 / p6 0.715 / p7 0.716 / p8 0.730——全部 ~1 量级，与旧版 p8（1.755，同口径）同级，绝非旧版 p1–p7 的 94–127（100 量级噪声）；交付文件提取流与候选流逐字节相同，故渲染差值直接适用于交付文件。
  - 未改动文件比对（vs `pre-fix-webpdf-round5.sha`）：SVG×8 全部 OK、卡片×8 全部 OK、印刷 PDF OK（SHA-256 `e9fb978109ddfea4874083bc210f1e34fc378d7845b09b1c6bf248d713a7e45b` 不变）、ABSTRACT OK；仅网页版 PDF 一项变化（预期内替换）。
- **根因结论（未查明，如实记录）**：构建树（`hidden_files/weekly-report-w45-fr-en-build/`、核心构建树）与 `tools/` 均无网页版 PDF 生成脚本，构建日志（`build1/2.log`）只记录 SVG 流，KIT 第八节仅一句话描述方法，故原始生成命令与输入无法从产物反推。已证实：旧文件头为 Pillow 产物、嵌入 JPEG 量化表确为 q75、p1 流与新鲜卡片 q75 编码公共前缀 1,124 字节（头部 + 约 500 扫描字节）后即分叉；旧 p8 虽像素干净、其流字节数（855,389）亦不同于新鲜编码（888,639），即旧文件各页流普遍非新鲜卡片编码。p1–p7 流为何不是卡片编码，未查明——不编造原因；重建自卡片为本次修复，不依赖根因查明。另：校对报告 O7 指出 FR 核心网页版同患此缺陷，本修复不重开核心，仅提请主线复查。
- **状态**：本构建仍为 **builder-complete，NOT finalized**——修复完成 ≠ 定稿；定稿须由独立校对做 SOP §8.4 全新完整二轮校对，本构建不宣布上架、不派发校对。
