# Le Lucerna · 法语周报 VOL.3 — 荷兰语讲解版（FR × NL）WEEKLY KIT

**状态：builder-complete，NOT finalized**——定稿由独立校对决定，本构建不宣布上架。

**版本定位**：VOL.3「决赛周末」（2026 年 11 月 2–8 日，2026-W45）的**荷兰语母语读者版**。同一法语核心（`files/weekly-report-w45-fr-core/`，VOL.3），讲解层换成荷兰语——生产矩阵中的 FR × NL 一格。法语核心定稿结论直接继承；本文件只记录本版的规格、改动边界与验证。开工查重：本版构建目录与交付目录均不存在、无属于本版树的在途进程，安全开工（一个已完工交付物的新鲜 mtime + 静默复查无变化不构成 stand down，本版无此情形）。

## 一、本版规格

| 项 | 内容 |
|---|---|
| 版数 / 版面 | 8 版，1950 × 2700，四栏，暖象牙纸色——与核心版完全相同 |
| 配对 | **法语正文 × 荷兰语讲解**（目标语 = Français，读者母语 = Nederlands） |
| 刊头配对徽标（第 1 版，深色横幅下方，砖红色居中） | **"TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS"**（x=975，y=574，22pt BRICK #a4553a，加粗，居中——与 W43 同配对版、W45 核心实测三方一致，见第三节） |
| 刊头冠词 | Le（法语专用） |
| 每版页脚 | 左：`Le Lucerna · FRANS WEEKBLAD VOL.3 · TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS`；右：`Pagina N van 8` |
| 讲解层 | 全部译注（Uitleg — 前缀）、词表注释、题干说明（Vul in / Herschrijf / Combineer / Corrigeer）、栏目说明、易错诊所说明、读者园地荷兰语点评与说明、下期预告附注、第 8 版全部答案简析——**100% 荷兰语**（渲染 SVG 文本节点 CJK = 0；登记表题型名等不出报的内部元数据沿 W43 先例保留中文原样） |
| 栏目头 | 法语 + 荷兰语双语（与 W43 同配对版体例一致），如 `À VOUS ! · JOUW BEURT`、`DIRE LA DATE · ZO ZEG JE DE DATUM`、`LANGUE EN MAIN · TAAL IN DE PRAKTIJK` |
| P8 形式 | 分隔 `— PAGINA n —`；简析括号半角加空格 ` (note)`（W43 同配对版形式）；印出简析集合 = 核心集合的显式复现（见第四节） |

## 二、实测量化（与核心 KIT 同一口径，登记表实测）

- **练习总量：150 题**，与核心逐题一致：编号 1–150 连续、逐版分布 **10/15/18/18/17/18/12/42**（P2 15、P5 17、P8 42——FR 串，与通用串不同）、级别分布 **A2 53 · B1 75 · B2 22**、题型分布（完成句子 49 · 单选 26 · 词汇配对 21 · 完形填空 8 · 句型转换 7 · 图表读数 6 · 阅读判断 5 · 阅读理解 5 · 翻译 5 · 对话补全 5 · 跟练 8 · 改错 4 · 写作 1）均与核心登记表一致（scratch 登记表复核：NL 与核心两树 Counter 全等）。
- **范文逐字 = 核心**：P8 MODÈLE 范文（86 词，`Mon week-end du 7–8 novembre`）未触动（transform 无此目标串；P8 渲染与核心同源）。
- **Gloss 逐项计数**（README #21：gloss() 调用串按 `·` 切分）：P1 7 · P2 6 · P3 6 · P4 7 · P5 6 · P6 6，**合计 38 = 核心 38**，逐盒相等。
- **全文 CJK**：8 个 SVG 文本节点 CJK = 0；freeze diff 新增 CJK = 0（全部 8 版）。
- **构建警告**：最终驱动**零 FLOW OVERFLOW / HEAD TOO WIDE**（P1-hiver 2298 与 P6-ex 2557 两处 flow 终值与核心逐字相同，属核心继承余量：距页脚线 2580 分别 282px / 23px，卡面确认无压线）。

## 三、家具三方对照（W43 同配对版优先于 #20 泛化）

| 家具 | W43 FR×NL 实测 | W45 核心实测 | 本版采用（实测） |
|---|---|---|---|
| 配对徽标 | (975, 574)、22pt、#a4553a、bold、middle，荷兰语串 | (975, 574)、22pt、#a4553a、bold、middle，中文串 | (975, 574)、22pt、#a4553a、bold、middle，荷兰语串——**三方几何一致**，仅读者母语文字不同 |
| 页脚左 | `Le Lucerna · FRANS WEEKBLAD VOL.2 · TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS` | `Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文` | VOL.3 的荷兰语同构串，8 版实测一致 |
| 页脚右 | `Pagina N van 8` | `第 N 版 / 共 8 版` | `Pagina N van 8`，8 版实测一致 |
| Gloss 前缀 | `Uitleg — ` | `译注｜` | `Uitleg — `（bslib4 gloss()，与 W43 一致） |
| P1 顶栏 | 左 `VOL. 2 · NR. 2`；中 `HEBDOMADAIRE EN FRANÇAIS · ELKE WEEK · HET FRANS DAT DE FRANSEN LEZEN` | 左 `VOL. 3 · 总第 3 期`；中 `HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语` | 左 `VOL. 3 · NR. 3`；中沿用 W43 荷兰语串 |
| P1 副标题 | `WEEKBLAD IN HET FRANS · VOL.2 · HERFST EN FEESTEN` | `法 语 周 报 · VOL.3 · 决 赛 周 末` | `WEEKBLAD IN HET FRANS · VOL.3 · FINALEWEEKEND` |
| P1 顶栏同基线间距 | — | — | 左/中/右三段同基线 y=92 墨迹间距分别为 337.4px / 112.0px，无重叠（canonical ink_box 实测） |
| P8 分隔 / 括号 | `— PAGINA n —` / ` (note)` | `— 第 n 版 —` / `（note）` | W43 形式 |
| 词表头后缀 | `· WOORDEN` | `· 节日词表 / 网球词表 / 音乐词表 / 词汇` | `· WOORDEN`（P3/P4/P5/P6，实测框内：+22px 后最宽 421.6px < 434px 框宽） |
| 诊所头 / 工具箱头 | `CLINIQUE DES ERREURS · PAS OP!` / `BOÎTE À OUTILS · OP ZAK` | `CLINIQUE DES ERREURS · 易错诊所` / `BOÎTE À OUTILS · 工具箱` | W43 形式（诊所头 429.4px < 434px；工具箱头 346.0px） |
| P6 读日程头 | — | `LIRE LE CALENDRIER · 读日程` | `LIRE LE CALENDRIER · KALENDER`（420.9px < 434px） |
| P6 图表题 | — | `LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）` | `LE CALENDRIER PRÉVU · GEPLANDE KALENDER (NOG GEEN RESULTATEN)`（866.1px，框内 896px，余量 8px，卡面确认在框内） |

## 四、零差异验证与 P8 双门

1. **核心完整性**：核心版全部无 CJK 文本节点在本版中逐字出现（freeze diff：新增 CJK = 0；核心 SVG 在构建前后 sha256 8/8 不变，见 `scratch/core-prebuild.sha` 全 OK）。单节点字符串检索对换行切分的 4 项呈假阴性，拼接文本（全部文本节点以空格连接）复核全部通过，见第五节末。
2. **冻结**：全部法语正文零删失、零改写。FR 族已裁定事实逐项在位：P4 `41e édition en 2026 (40e anniversaire)`（全文 `40e` 仅此 1 处、`41e` 仅此 1 处；41e 是届数、40e 是周年数）；P7 引文 #4 为 P4 辩论框逐字 `plus excitante ou plus frustrante ?`；#8 用 P5 逐字 `Les jeunes créateurs y rencontrent leur public, en vrai.` + Q106 改写（error `rencontre`，key `rencontrent`）；P6 同步为 `Ce calendrier peut encore bouger.`（P6 深读小写形与微习题键 `peut` 非引文、未动）；Q120 题干 `Si j'étais libre dimanche, j'___ à Nanterre.`、选项 `irai / irais / vais`、键 B、P8 注释 `si + imparfait → conditionnel; j' = je geëlideerd`；Q119/Q121 不动（transform 无此目标串，P8 卡面 119/121 题面与核心一致）；P7 法语定义句冻结——仅本地化讲解行（语法点行、工具箱说明、诊所注、读者园地荷兰语段、栏目头荷兰语后缀），P7 三级专栏法语定义段逐字未动。
3. **P8 双门（FR 族专属，BINDING）**：
   - ① plain `tools/p8.py compare`（显式 `--core-p8/--edition-p8`，`--total 150`；`--target` 形式会走错 P8 文件名、默认 total 取 W43 的 149 而错分段，两者皆禁）：**CLEAN，noted 97 = 97**，missing=[]，extra=0，keydiff=[135, 150]。
   - ② `hidden_files/w45/p8-fr-gap-fix/keycompare.py`（全 150 键）：mismatch 2 项，恰为上述 [135, 150]，**裸键 53 条零 mismatch**（两项均为 noted 重定向项，故裸键集无一不符）。
   - 裁定：135（法译荷题答案键：中文译文 → 荷兰语译文 `Een programma lezen is al Frankrijk begrijpen.`）与 150（写作题答案键：中文指引 → 荷兰语指引 `Open opdracht — punten in schrijfkader, voorbeeld in MODÈLE-kader`）均为读者语言层重定向，沿 W43 先例（该版 5 项）合法；其余 148 键逐字相同。**双门通过**（plain ∈ {CLEAN} 且零裸键 mismatch）。
   - 实现：本版 P8 以显式 `PRINT_NOTES` 集合（核心 noted 集，`tools/p8.py extract --json` 实测 97 项）印出简析，不依赖荷兰语简析长度规则——否则荷兰语简析普遍 >10 字符会使印出集缩水（W43 同法）。
4. **翻译题重定向**（读者语言面，法语键不变）：135 题键改为荷兰语译文，题面方向标改为 `→ NL:`；136–139 题题面改为荷兰语待译句并标 `→ FR:`（`Hij rent sneller dan zijn broer.` / `De leerlingen zijn sinds 17 oktober op vakantie.` / `Vanavond gaan we onze schooltassen klaarmaken.` / `Men kent de finalisten nog niet.`），法语键逐字不变；150 题写作指引荷兰语化。箭头方向标约定：135 项示范“译入荷兰语”，136–139 项示范“译入法语”，E 节首项即确立该约定。以上即 keydiff 的全部内容。
5. **讲解语言审计**：渲染 SVG 全文 CJK = 0；逐版看图复核讲解层无中文残留；报纸版面（8 SVG）与构建代码中该中介措辞 grep = 0。

## 五、几何门禁（全部实测值）

- **Canonical 遮挡审计**（`tools/occlusion_audit.py`，自检先行通过）：本版 **0 flags**，核心 0 flags，**NEW vs core = 0**。首轮实测 4 NEW flags 全部为真缺陷，已逐项修复（见第七节）。
- **同基线行首检查**（FR×RU 教训）：P1 顶栏三段与 8 版页脚左右段同基线墨迹间距全部 >0（最小 112.0px），无重叠。
- **ADVANCE 全页右缘扫描 + 全页框线扫描**：右缘（>1885）仅 P8 F 组 3 行法国原文配对行（ink right 1891.2/1891.3/1899.5），与核心**逐字节相同的墨迹值**（核心同行同值），属核心继承几何、非本版缺陷；P2 两行右对齐荷兰语行 advance 恰为 1885.0、ink 仅超 0.04/0.15px（PIL 取框舍入量级，卡面在框内）；框线扫描与审计 LINEX 一致为 0 穿越。
- **P6 图表标签基线锚定覆盖**（getbbox 墨迹盒 vs 除图表自有框外全部不透明框）：全部 12 个图表文本元素覆盖 **0.0%**（<30% 门）；图表为纯文字行、无柱体遮挡。
- **孤儿扫描（窗口 10–45，定义先行）**：分块规则 = 同页/同 x/同字号/同字体、连续 y 间距 ∈ [10,45] 的文本行为同一绕排块；旗标 = (i) 行首标点 `.,;:!?%)]}` (ii) 末行单 token ≤3 字符。结果：本版行首标点新增 **0**；末行短 token 旗标 4 处（P1 `p.8`、P2 `___` ×2、P3 `7).`）与核心**同页同 y 逐字相同**，属目录标签/填空横线/冻结法语换行继承，非本版缺陷；核心对照扫描另有中文讲解行末标点旗标（本版荷兰语化后消失）。
- **流末端**：P8 电池流 1468（<1485 写作条底线）；P8 答案流 2509（<2545 门，距页脚线 2580 余 71px）；P7 预告末端：读者园地框 + 预告条均在页内（P7 卡面确认）；P5 主流末端 2532（<2540，与 EN 版同值）；P2 练习流 2365；P7 金句流 1574（<1830）、诊所流 2140（<2268）。
- **全 8 卡目视**：P1–P8 整版逐版看图，无重叠、无压线、无出框；另核 P1 徽标/议程框、P2 ET VOUS 框、P6 图表、P7 读者园地、P8 电池/写作条/答案末端均在位。
- **单节点检索假阴性说明**：`41e édition en 2026 (40e anniversaire)`、P7 #4/#8 引文、Q120 P8 注在 SVG 中均被绕排切为多节点，单节点 grep 呈 MISSING；拼接全部文本节点后 4 项全部 FOUND，Q120 选项 `irai / irais / vais` 拼接文本亦在位。

## 六、图片

仅明确公有领域图片，与核心同 3 张、同法语图说与出处、同 base64 内嵌，载荷哈希双口径一致（base64 文本 sha256 前 16 位与解码 JPEG sha256 前 16 位均与核心相同）：

| 版 | 内容 | 作者/出处（Commons Artist 字段原文） | 授权 | 解码字节 |
|---|---|---|---|---|
| P1 | 巴黎街道老照片 | Eugène Atget (1857-1927), photographie | Public domain | 334,674 |
| P2 | 浮世绘《真间川红叶》 | Utagawa Hiroshige (1797-1858), estampe · LACMA | Public domain | 646,242 |
| P3 | 菊花植物图谱 | Flora de Filipinas (Blanco), XIXe siècle | Public domain | 142,340 |

三图均已在 SVG 中核实放置（`<image>` 元素 + 图说 + credit 行齐全）；授权明细随核心 KIT 第六节（W43 素材库 Commons 元数据核过）。

## 七、修复轮记录（fix-round 编辑全部进 transform.py，单源头）

- **Round 0（基线）**：核心构建未改动拷贝 + OUT 重定向至 scratch，8 SVG 与 shipped 核心 **8/8 字节复现**，核心构建前后 sha256 8/8 不变。
- **Round 1（初译）**：transform.py §1：核心构建复制 + OUT 重定向 + 讲解层中→荷全量映射（297 对断言替换：bslib4 3 + content12 57 + content34 81 + content56 68 + content7 30 + content8 58，另 OUT 重定向 5 处；此前误写 298 项/content8 59，2026-10-28 按独立校对实测订正）+ bslib4 页脚/gloss 前缀 + P8 显式 PRINT_NOTES。首轮渲染：150 题、零警告；但 P8 电池流 1526、答案流 2646 超限，遮挡 4 NEW 旗。
- **Round 2**：P1 议程荷兰语行缩短为单行短式（19pt 实测 398.0px ≤ 412px 预算）；P8 翻译题改用箭头方向标（135 回 2 行、136/139 回 1 行，电池 1526 → 1468）；长印刷注批量缩短约 430 字符（P1–P8 各组 + 150 题键，键不变），答案流 2646 → 2509。复审：遮挡 0 flags，NEW 0；P8 CLEAN；双门通过。
  - 过程注：Round 2 首跑因 content34 一处 `\'s` 转义断在中途（content12 已先写盘 7 处）；按单源头原则逆向复原 content12 的 7 处、修正转义后完整重跑，应用计数 7/6/8/4/14，全量通过；部分状态的中间渲染未作交付基线（交付基线为 Round 1 的 `scratch/pre-fix-round2.sha`）。
- **每轮基线**：修复前均存全量 SVG 基线（`scratch/pre-fix-round2.sha`；Round 2 后 SVG 仅 P1/P8 变化，P2–P7 与 Round 1 逐字节相同——Round 2 其余改动均为登记表注，只印在 P8）。
- **单源头复现验证**：全新核心拷贝 + transform.py（ROUND=1 → 2 顺序执行）所得 7 个源码文件与本构建树逐字节相同，渲染后 8 SVG 与交付 **8/8 逐字节相同**（`scratch/repro-build/`、`scratch/repro-svg/`）。
- **Round 3（P4 独立校对阻塞项修复，2026-10-28）**：P4 `LES PHRASES DU COMMENTATEUR` 框（框内宽 398px，serif 21.5pt）首行止于 `« Quelle action`、次行以 `! »` 起头——荷兰语释义 `Kom op!` 长于核心中文释义，绕排在法语空格标点 `action !` 间断开，卡面目视确认。修复只进 transform.py §3（单源头），荷兰语侧缩短：`Kom op!` → `Kom!`（真实荷兰语喝彩词）；法语字节零改动（不改措辞、不用不换行空格等取巧办法）。实测：首行 `« Allez ! » — Kom! · « Quelle action ! »` = 387.94px（整句在首行）、次行 `— Wat een actie!`（与核心次行破折号起头同式）；行数、框高、下游 y 全不变。改动范围证明（修复前基线 `hidden_files/w45/fr-nl-fix/delivery-baseline.sha`）：仅 svg/p4、cards/p4、双 PDF、KIT 变化，其余 7 SVG + 7 卡片 + ABSTRACT 字节不变。修复后自测（证据 `hidden_files/w45/fr-nl-fix/`）：严格孤儿扫描（窗口 10–45，逐行行首标点 + 末行短 token）全版 8 旗全部为核心同页同 y 同文继承，**新增行首标点 0、新增短尾 0**（此次为实测值，非沿用旧自述）；canonical 遮挡审计新版 0 旗、核心 0 旗、NEW 0；P8 双门：plain CLEAN（noted 97 = 97，keydiff [135, 150]）、keycompare 全 150 键 mismatch 恰 [135, 150] 且均为 noted 项、裸键 0；P8 三口径：流光标电池 1468 < 1485、答案 2509 < 2545，最大基线电池 1455.83（= 核心）、答案 2537.73（核心 2539.19），墨迹底电池 1456.08（= 核心）、答案 2540.73（核心 2541.23）、距页脚线墨迹间隙 39.27px；网页版 PDF 从新卡片新鲜生成、逐页渲染 1950×2700 下采样差 1.195–1.607（~1 量级，无噪声页）、内嵌流除 p4 外 7/8 与修复前逐字节相同；全新核心拷贝 + transform.py（ROUND=1 → 2 → 3）所得 8 个源码文件与建造树逐字节相同、渲染 8 SVG 与新交付 **8/8 逐字节相同**。本修复不宣布定稿，待第二轮全新完整校对。

## 八、复现构建与工具链

构建树：`hidden_files/weekly-report-w45-fr-nl-build/`（`transform.py` 单源头 + 内容模块 + `build1/2.log`、`checks.py`/`checks-final.txt`、`chartcheck.py`、`occlusion*.json`、`p8-final.txt`、`keycompare-final.txt`、`freeze-diff-final.json`、基线与复现 scratch）。

```bash
# 1. 从核心构建复制（禁在核心构建目录内 import 内容模块）
cp hidden_files/weekly-report-w45-fr-build/*.py hidden_files/weekly-report-w45-fr-nl-build/
cp -r hidden_files/weekly-report-w45-fr-build/assets hidden_files/weekly-report-w45-fr-nl-build/
# 2. OUT 重定向 + transform（round 1→2 顺序执行；单进程驱动是唯一渲染入口）
cd hidden_files/weekly-report-w45-fr-nl-build
TRANSFORM_ROUND=1 ../../tools/venv/bin/python transform.py
TRANSFORM_ROUND=2 ../../tools/venv/bin/python transform.py
TRANSFORM_ROUND=3 ../../tools/venv/bin/python transform.py   # Round 3：P4 解说员框荷兰语缩短（Kom op! → Kom!），法语不动
../../tools/venv/bin/python -c "import content12, content34, content56, content7, content8"   # 生成 8 个 SVG，零警告
# 3. 卡片 + 双 PDF（与核心 KIT 同法；网页版 Pillow 默认质量，实测 = q75，见第十节）
#    cairosvg svg2png (1950宽) → svg2pdf + pypdf 合并为大报版；整版 PNG 转 JPEG 封装为网页版
```

工具链裁定：渲染 SVG 的驱动解释器与卡片/PDF 渲染解释器**均为 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）**；系统 python3（同为 3.12.3，Pillow 10.2.0）无 cairosvg，不可用于 render.py。审计测量用 venv PIL（与渲染同一 venv）。run.py 解释器/PIL 由建造员自选但须字节复现家族基线 SVG——本版基线复现 8/8 已证；render.py（cairosvg）恒用 venv。

## 九、交付物

交付目录 `files/weekly-report-w45-fr-nl/`：`svg/` 8 个源文件 · `cards/` 8 张整版 PNG（1950×2700）· `Le-Lucerna-VOL3-NL.pdf`（8 页大报版，**9,746,757 字节**，SHA-256 `1fe9cc20c620ad7a9a509718dde73c5e4b9e1a8ff07209047b09038ab2adbb56`，8 页，1462.5×2025 pts）· `Le-Lucerna-VOL3-NL-web.pdf`（8 页网页版，**5,291,771 字节**，SHA-256 `1a579fffd05874e166cee1d99ea0227a20660e16266c97f536ed41b34d836711`，Title `Le-Lucerna-VOL3-NL-web`）· `ABSTRACT.txt`（荷兰语单行，无 ASCII 双引号）· 本文件。修复前 pins：印刷 9,746,750 B / `be303278…`、网页 5,292,087 B / `fe33b3b9…`（见 Round 3 记录）。

| 文件 | 字节 | SHA-256 |
|---|---|---|
| svg/p1-une.svg | 475,129 | be470c2605b47b1a79bb412b7e35ea8253d4d0808a3e66e9ee95dc13138df74d |
| svg/p2-vie.svg | 891,327 | a4f58e2d14d27638980f5dc74e527a10907e53ef374f9021ac1f1ff47dc9784c |
| svg/p3-culture.svg | 220,993 | b7da0abfbdd35a823e5756c7fbfd9b2d41ca3774ab4e94f25a484df76a266b55 |
| svg/p4-sport.svg | 33,178 | 87f21ae35a96db35ba8a2ef83c3e2ccb86d981d010510c7d28906b039377c9db |
| svg/p5-jeunesse.svg | 26,639 | 03099928659fab3b6ca21b54a1803481f6053da6d75f03a170eb25b782619559 |
| svg/p6-politique.svg | 29,046 | 423f711318a87fdc70e4dadf4e1b2cc707e37b068c9f4569066f7a58e8d3526e |
| svg/p7-langue.svg | 30,650 | c7464eeb615020de0befdc3b084e20392d0a2c2532a18750cba768636bd450b2 |
| svg/p8-exercices.svg | 48,489 | 876c268e2f03a73b433335ef7a72ff43cef6e9a87693816747bdc2cb81d36f35 |
| cards/p1-une.png | 1,048,649 | 2160bd5799c1abaa164186e43eaad143196eb3897369dba3285b99ade8c6ba0a |
| cards/p2-vie.png | 1,183,997 | 7144bfcd70c05097ee23278b46b57909200c6c221ee6617360d0d253e9842cca |
| cards/p3-culture.png | 938,602 | 4e7aaa873401ef8ba32706879a6a8c868c90e0f2295b3444c15cc92547dd816c |
| cards/p4-sport.png | 847,023 | bd5730e9520a107be3c758d48d827f09c074195025f05aac5c7fb3e27d329940 |
| cards/p5-jeunesse.png | 695,231 | b63afd0d1f2873b89ada2418eb7aae2c36077fbaaa6a057b0df6663833856ebf |
| cards/p6-politique.png | 746,838 | addc0e6daaa317fc9d8091b1ab302686d5f41c1df2af282dae9d466a8986231c |
| cards/p7-langue.png | 738,256 | f1dce0be1b0e9e23ee9099147b72008a6ba7849ed3da6b79b04985a27ab41899 |
| cards/p8-exercices.png | 1,128,618 | 8867bbb149c999a403d0d0bdf04ba5e2a1912ed3650438d21d760a4e5277e457 |
| Le-Lucerna-VOL3-NL.pdf | 9,746,757 | 1fe9cc20c620ad7a9a509718dde73c5e4b9e1a8ff07209047b09038ab2adbb56 |
| Le-Lucerna-VOL3-NL-web.pdf | 5,291,771 | 1a579fffd05874e166cee1d99ea0227a20660e16266c97f536ed41b34d836711 |
| ABSTRACT.txt | 427 | da96d172e93cf84d580de78816269c34f18ece209630ff5aa8a229598e55b81b |

## 十、网页版 PDF 验证（从本版卡片新鲜生成，非复用核心网页版）

- 配方：`tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）打开 8 张交付卡片转 RGB，按 p1–p8 顺序 `Image.save(..., "PDF", save_all=True, append_images=[p2–p8], resolution=150.0, title="Le-Lucerna-VOL3-NL-web")`；未显式传 quality，即 Pillow 默认质量。
- **q72/q75 实测结论：默认质量 = q75**——交付文件内嵌 JPEG 流（pdfimages 提取，pg-000…pg-007）与新鲜卡片 q75 编码**8/8 逐字节相同**（p1 676,446 / p2 656,710 / p3 607,244 / p4 654,202 / p5 545,717 / p6 584,891 / p7 669,621 / p8 892,500 字节；Round 3 后 p4 流 654,518 → 654,202，其余 7 流与修复前逐字节相同），与 q72 编码 8/8 均不同。故不存在 FR 核心网页版的旧噪声问题根源（旧文件流非新鲜卡片编码）；本版网页版直接由卡片生成，无噪声页。
- pdftoppm -r 150 全页渲染（1950×2700，与卡片同尺寸）：8 页均值 RGB 全部纸色（p1 (219.3, 213.8, 198.9) / p2 (226.8, 221.3, 205.7) / p3 (229.9, 224.4, 208.9) / p4 (229.5, 223.9, 208.1) / p5 (232.3, 226.8, 211.5) / p6 (231.7, 226.0, 210.6) / p7 (221.9, 216.7, 201.4) / p8 (226.6, 221.1, 205.4)）；195×270 下采样与卡片均值绝对差 p1–p8 为 1.483 / 1.355 / 1.293 / 1.318 / 1.195 / 1.255 / 1.419 / 1.607——全部 ~1 量级（噪声页为 100 量级），8 页全部干净。
- 印刷 PDF p1 下采样对照（pdftoppm vs 卡片）：均值绝对差 1.44，同级干净。

## 十一、P7 读者园地核查（逐字摘录）

- **标注的编辑示例**（法语，冻结）：“« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).”
- **三事实披露**（荷兰语，园地框内）：“Opmerking van de redactie: geen echte brieven en geen beste VOL.2-pagina-8-tekst binnen (geen W44-nummer); beide volgen in VOL.4.”——同时覆盖：无真实来信、无 VOL.2 P8 最佳作文、均延至 VOL.4。法语编辑部说明（冻结）：“Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.”
- **明确的公开征集祈使句**（逐字，园地框荷兰语点评末句，字面同时覆盖来信与最佳 P8 文本）：“Stuur je brief én je beste pagina-8-tekst in voor VOL.4!”——预告条（“en jullie brieven!”）不计作征集，本句本身已完整覆盖两者。
- **范围裁定**：征集句本身即在 P7 园地框内，无需借助他页提示或预告组合；P8 写作条“Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »)”与预告条同向，均指向 VOL.4——VOL.4 承诺覆盖范围 = VOL.2 投稿（如收到）+ 本期 P8 写作投稿的真实点评；本期示例不得冒充。
- **VOL.4 兑现清单**（核心交接，本版原样继承）：巴黎大师赛周末结果、国民议会预算周表决结果与参议院社保预算审议、读者园地真实投稿点评。

## 十二、与 W43 同配对版的偏差清单（非缺陷，均为本期/语言层事实）

1. 期次与内容：VOL.3（11 月 2–8 日决赛周末）vs VOL.2（10 月 19–25 日深秋与节日）；题量 150 vs 145；逐版分布 10/15/18/18/17/18/12/42 vs 10/16/18/18/17/18/11/37；级别 A2 53/B1 75/B2 22 vs A2 55/B1 65/B2 25；P8 noted 集 97 vs 67（核心决定）。
2. 家具：徽标串、页脚式、gloss 前缀、P8 分隔/括号式与 W43 逐字同构，仅 VOL 号不同；P1 副标题主题词不同（FINALEWEEKEND vs HERFST EN FEESTEN）；顶栏中段沿用 W43 荷兰语串。
3. 读者园地状态不同：W43 刊登真实读者投稿（L. M.）；本期核心因 W44 未出刊、未收到 VOL.2 投稿，刊登标注明确的编辑部示例 + 荷法双语延期披露 + 明确征集句（见十一节）——此为核心继承状态，非本版改动。
4. 翻译重定向项数：本版 2 项（135、150）vs W43 的 5 项（核心题型结构不同）；另 136–139 题面方向标由 W43 的文字式改为箭头式（`→ NL:` / `→ FR:`），以保 P8 电池流行数与核心一致（见第四节第 4 项、第七节 Round 2）。
5. 版面适配缩短（仅讲解层措辞）：P1 议程行、P1 词表短式（`schelp` 裸式，含 `Uitleg — ` 前缀实测 5 行）、P8 长注与 150 题键——均由荷兰语较长引起，法语与版式参数不动（见第七节）。
6. 网页版压缩：JPEG q75（Pillow 默认质量；实测流逐字节证实）；W43 荷兰语版 KIT 记录为 q85——方法差异，不影响内容；入仓时以本版实测 pin 为准。
