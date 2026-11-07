# W45 FR×NL 第二轮独立校对报告（目标语言法语 · 读者母语荷兰语 · VOL.3）

## 结论：ZERO PROBLEMS

本轮为 SOP §8.4 要求的全新完整第二轮校对，从头全部重测，未复用第一轮结论（第一轮报告仅作阻塞项来源参考）。第一轮唯一阻塞项（P4 行首孤悬 `!`）经修复验证已消除，其余 12 门全部通过，**无编号阻塞项**。本报告不宣布上架；上架由协调员串行做。

**校对方式与边界：** 未派生任何下级代理；未碰 `weekly-git`；未改核心目录、交付目录、`tools/` 下任何文件；未清理共享 scratch；未发 Discord；未往主聊天发卡片/PDF；未建 cron；未宣布上架。所有重跑均在自有 scratch（`hidden_files/w45/fr-nl-proof2/work/`）内完成；构建树脚本凡含写回交付/核心目录的 OUT 路径者，一律先拷到自有 scratch 并重定向 OUT 后再运行。工具版本：`tools/p8.py` sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`（与任务书所称已验证新版一致）；渲染/审计解释器一律 `tools/venv/bin/python`。

## 开工查重（硬性）

- 交付目录 mtime：SVG 2026-10-28 06:17:25 UTC、卡片/PDF 06:17:28–51 UTC、KIT 06:20:11 UTC；开工前两轮 60 秒以上静默复查：20/20 文件 sha256 无变化（开工哈希 `work/delivery-sha-t0.txt`），无属于本版树的在途进程（同期在跑的 `insert.py` 属 fr-pt 版，与本版无关，未触碰）。结论：已完工交付物 + 静默复查无变化 = 安全开工，非 stand down。
- 校对全程结束复查：交付 20/20 哈希与开工时逐字相同；核心 8 SVG 哈希与开工前逐字相同。核心与交付均未被本校对改动。

## 交付 pin 独立重测

| 文件 | 实测 | 任务书 pin | 结论 |
|---|---|---|---|
| 印刷 PDF `Le-Lucerna-VOL3-NL.pdf` | 9,746,757 字节，sha256 `1fe9cc20…adbb56`，8 页，1462.5×2025 pts，Producer pypdf | 相同 | ✓ |
| 网页 PDF `Le-Lucerna-VOL3-NL-web.pdf` | 5,291,771 字节，sha256 `1a579fff…d836711`，8 页，936×1296 pts，Title `Le-Lucerna-VOL3-NL-web` | 相同 | ✓ |
| `ABSTRACT.txt` | 427 字节，sha256 `da96d172…b81b` | 相同 | ✓ |
| `svg/p4-sport.svg` | 33,178 字节，sha256 `87f21ae3…377c9db` | 相同 | ✓ |
| `cards/p4-sport.png` | 847,023 字节，sha256 `bd5730e9…d329940` | 相同 | ✓ |
| 其余 7 SVG + 7 卡片 | sha256 与 KIT 表逐项一致（p1 `be470c26…`、p2 `a4f58e2d…`、p3 `b7da0abf…`、p5 `03099928…`、p6 `423f7113…`、p7 `c7464eeb…`、p8 `876c268e…`） | — | ✓ |
| KIT `WEEKLY-KIT.md` | sha256 `cdd6c9c4…`，内载新 pins 与修复前 pins（印刷 9,746,750 / `be303278…`、网页 5,292,087 / `fe33b3b9…`）均与实测/第一轮一致 | — | ✓ |

## 门 1 — 修复验证（首要）：通过

- **P4 卡面目视（裁切 + 整卡）：** 解说员框首行 `« Allez ! » — Kom! · « Quelle action ! »` 完整在首行，次行以 `— Wat een actie!` 起头；`!` 不再行首孤悬。整卡 P4 其余部分无缺陷。
- **P4 文本节点（交付 SVG 实测）：** 框内行 y=902.095 `« Allez ! » — Kom! · « Quelle action ! »`（墨迹宽 388.00px，框内宽 398px，余量 10px；修复员所称 387.94px 为 advance 口径，0.06px 口径差，无实质差异）、y=932.625 `— Wat een actie!`；框内无任何行以 `!` 起头（全版安全网扫描：无任何文本节点以 `!` 或 `?` 起头）。
- **新旧 P4 逐节点 diff（自有重渲染，不依赖修复员旧文件）：** 自有 scratch 内 ROUND=1+2（修复前）与 ROUND=1+2+3（修复后）两版渲染的 P4 各 202 节点，**仅 2 节点不同**，且 x/字体/字号/y 全同：旧 y=902.095 `« Allez ! » — Kom op! · « Quelle action` / y=932.625 `! » — Wat een actie!` → 新 y=902.095 `« Allez ! » — Kom! · « Quelle action ! »` / y=932.625 `— Wat een actie!`。下游行（y=989.655 起）逐字逐坐标不变，行数、框高、下游 y 全不变，与修复员声称一致（独立实测）。
- **法语措辞零改动（字节级）：** 新旧两行中法语段 `« Allez ! »` 与 `« Quelle action ! »` 的 UTF-8 字节与核心同句逐字节相同（`!` 前为空格 U+0020，两树一致）；transform §3 仅 1 处替换（`Kom op!` → `Kom!`），未引入不换行空格；全版法语节点冻结见门 2。
- **改动范围（修复前基线 `fr-nl-fix/delivery-baseline.sha` 逐项比对）：** 仅 `svg/p4`、`cards/p4`、双 PDF、KIT 变化；其余 7 SVG + 7 卡片 + ABSTRACT 字节不变。ABSTRACT sha `da96d172…` 与修复前相同。

## 门 2 — 冻结：通过

- 核心基线自有 scratch 重跑：`tools/freeze.py baseline`（核心构建 `hidden_files/weekly-report-w45-fr-build`）**8/8 逐字节**：p1 `f02e628e…`、p2 `b192c192…`、p3 `5f332e9f…`、p4 `240f379d…`、p5 `a4d64e3e…`、p6 `47e4346d…`、p7 `e997123f…`、p8 `822dbe3d…`；运行前后核心 SVG 重哈希不变。
- `freeze.py diff` 核心→本版：新增 CJK 字符 **8 页均为 0**（核心 CJK 计数 202/244/179/197/177/198/390/1030 → 本版 0）；新增串含 CJK 0 处。
- 冻结串逐项（拼接文本核对）：P4 `41e édition en 2026 (40e anniversaire)` 在位，全版 `40e` 仅 1 处、`41e` 仅 1 处（本版 = 核心）；Q120 题干 `Si j'étais libre dimanche, j'___ à Nanterre.` + 选项 `A. irai · B. irais · C. vais` 在位，键 B（全键比对无 mismatch），P8 注 `si + imparfait → conditionnel; j' = je geëlideerd` 在位（核心注为中文原文，核心侧查无属正常——注为讲解层本地化，法语键与条件结构不动）；Q119 题干 `Elle s'intéresse ___ festivals. A. à les · B. aux · C. des`、Q121 题干 `À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant` 两树逐字相同，键无 mismatch（即 Q119 B、Q121 A 不动）；P7 #4 verbatim comparatif `plus excitante ou plus frustrante ?`、#8 + Q106 `Les jeunes créateurs y rencontrent leur public, en vrai.`（Q106 键 `rencontrent` 无 mismatch）、P6 `Ce calendrier peut encore bouger.`（P6 词句对 + P7 金句表 + 深读段同坐标 y=984.46 两树一致）；P7 法语定义栏头 REPRENDRE / FUTUR PROCHE / PASSÉ COMPOSÉ / COMPARATIF / SUBJONCTIF / ATTENTE 全部在位。
- 冻结串多重集差分：P1–P7 被删节点中**不含 CJK 者为 0**（即无任何纯法语节点被删）；P8 被删无 CJK 节点 8 处，逐项核实均为答案流重绕排的法语键行边界变化（荷兰语注更长所致），其中 135 项法语原文以 `→ NL: « Lire un programme, c'est déjà comprendre la France. »` 方向标形式完整保留（拼接文本命中），其余 7 处法语键行在拼接文本中逐字命中。

## 门 3 — P8 双门：通过

- plain 门（显式双路径 + `--total 150`）：`tools/p8.py compare --core-p8 <核心P8> --edition-p8 <本版P8> --total 150` → **CLEAN，noted 97 = 97，missing=[]，extra_count=0，keydiff=[135, 150]**。
- 全键门：`hidden_files/w45/p8-fr-gap-fix/keycompare.py --total 150` → 全 150 键 mismatch 恰 2 项 **[135, 150]，且两项均为 noted 项，裸键 53 条 mismatch 为 0**（plain CLEAN 对裸键是盲的，本门补齐了该盲区；keycompare 进程 exit 1 系该工具“任一 mismatch 即 exit 1”的设计，非门失败）。
- 135：核心键 `读一份日程，本身就是在了解法国。` → 本版键 `Een programma lezen is al Frankrijk begrijpen.`，题面方向标 `→ NL: « Lire un programme, c'est déjà comprendre la France. »`；150：核心键 `开放题` → 本版键 `Open opdracht`（完整印刷行 `150. Open opdracht — punten in schrijfkader, voorbeeld in MODÈLE-kader (beoordeeld op de punten)`）；两项均为读者语言层重定向，法语键体系不动，沿 W43 先例合法。

## 门 4 — 登记 / gloss / 金句 / 范文：通过

- **登记（单进程渲染 REG 实测，核心 = 本版逐项相同）：** 总量 **150 题**；分页 **10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**（P1–P8）；级别分布 **A2 53 / B1 75 / B2 22**。
- **级别口径裁决（任务书核查点）：** 任务书所给核心分布 53/75/22 经 REG 实测成立。修复员报告中的“注册表 multiset（A2 51 / B1 67 / B2 20）”**不是题数口径**：本轮独立复算，该组数字是源码字面量 `"A2"/"B1"/"B2"` 的出现次数（两树均为 138 次）。字面量计数与题数不等的原因已查实：5 个 `match_set` 调用以 5 个字面量登记 21 题（4+4+4+4+5），另有 P7 跟练数据表等字面量不直接对应单题登记；REG（每题一次 `reg_ex`）才是登记表口径。修复员数字不得用作级别分布；本门以 53/75/22 为准。
- **gloss（`·` 切分口径，README #21）：** 核心构建与分版构建逐文件计数相同：content12 [7, 6]、content34 [6, 7]、content56 [6, 6]，**合计 38 = 7/6/6/7/6/6 = 核心**；法语词头逐项相同（P1 7 项无丢失）。
- **金句：** P7 金句表 8 句逐字 + 页签全对（#1 p2、#2 p1、#3 p3、#4 p4、#5 p5、#6 p6、#7 p1、#8 p5）；联合计数 **本版 = 核心 = 5 / 3 / 1 / 5 / 1 / 3 / 1 / 3**；所标源文章页命中口径：#1、#4、#6、#8 源页逐字连续命中；#2 源页为子句 `ne connaît pas encore les finalistes`（P7 表加主语 On）、#3 源页为 `Les cimetières se sont / remplis de chrysanthèmes —`（表内加句号）、#5 源页为跨节点 `Le / festival se promène dans Paris :`（表内加句号）、#7 源页为 `« se jouer » : se décider. Ce week-end, / tout se joue` 词框句（表内作句）——四项均为 P7 表的既有规范化形式，且本版与核心行为逐项一致，非分版偏差。
- **范文：** P8 MODÈLE 范文 7 行逐字 = 核心，空白分词 **86 词**（含法语冒号/感叹号独立 token；连字符计 1 词亦为 86），在 80–100 范围内。

## 门 5 — 几何：通过

- canonical 审计（自检先行通过，6 类 planted flag 全部触发、clean 对照静默）：**本版 0 flags、核心 0 flags、NEW vs core 0**。
- 同基线墨迹间距：P1 顶栏 y=92 三段间隙 **337.4px / 112.0px**（核心 387.5/196.2，均为串长差异，无重叠）；8 版页脚 y=2624 左右段间隙均为 **782.2px**（核心 1157.1px，系页脚右串 `Pagina N van 8` 长于中文串，无重叠）。
- 全页右缘扫描：本版仅 5 行超 1885——P2 两行荷兰语行 advance 恰 1885.0、墨迹仅 **1885.04 / 1885.15**（PIL 取框舍入量级；P2 右缘行裁切放大确认 `hoofdtelwoorden` 全词在框内，见 OBS-1）；P8 F 组 3 行法语原文配对行墨迹 **1891.25 / 1891.25 / 1899.5**，与核心同行墨迹值逐字相同（核心 y 为 940/1016/1054，本版 y 为 998/1074/1112，系版式流位移，墨迹值不变），属核心继承几何。
- P6 图表标签覆盖（绘制顺序法：仅计文本之后绘制的矩形，排除图表自有先绘容器框；此前一版误计容器框得 100% 已纠正）：图表文本 **12 个，最大覆盖 0.0% < 30%**（核心同口径亦 0.0%）；图表为纯文字行、无柱体遮挡。
- P8 三口径（本版 vs 核心同口径对照）：
  - 流光标（自有 scratch 复现渲染日志）：电池流 **1468 < 1485**；答案流 **2509 < 2545**。
  - 最大基线：电池 **1455.83（= 核心）**；答案 **2537.73（核心 2539.19）**。
  - 墨迹底：电池 **1456.08（= 核心）**；答案 **2540.73（核心 2541.23）**，距页脚线 2580 墨迹间隙 **39.27px**（核心 38.77px）；审计 FOOTER 旗 0。
  - **裁决依据（明确记录）：** 通过的依据是“墨迹底 < 页脚线 2580 + 审计 FOOTER 0 + 流光标 < 各自 Flow 底线”，而非单看 2509。必须说明：2509 是答案流最后一栏（x=1451）的光标，不是全页最大墨迹；全页最大墨迹在 x=527 栏（2540.73）。“距页脚线 71px”仅是 2580−2509 的流光标间隙，真实墨迹间隙为 39.27px——两者均通过，但不得把 71px 引用为墨迹间隙。
- P7 预告墨迹底 **2499.00**，预告条底 2540，余量 **41.00px**；读者框墨迹底 **2238.30**，框底 2258，余量 **19.70px**；P1 gloss 框 5 行墨迹最右 **939.00**，框右 961，余量 22px。
- 零 OVERFLOW：自有复现渲染日志与核心渲染日志均无 FLOW OVERFLOW / HEAD TOO WIDE 警告；P1-hiver 流 2298（底线 2290）、P6-ex 流 2557（底线 2540）两处软底超限与核心渲染逐字相同，墨迹均未越页脚线（审计 FOOTER 0），属核心继承余量（OBS-5）。

## 门 6 — 换行/孤儿：通过（第一轮阻塞项已消除）

- 孤儿扫描（窗口 10–45，行首标点 + 末行短 token，自有实现，双树同口径）：本版旗标 **8 处**，逐项核对核心同页同 y 同文，**新增行首标点 0、新增短尾 0**：
  - 短尾 4 处：P1 `p.8`（y=1604.0）、P2 `___`（y=2140.9）、P2 `___`（y=2459.1）、P3 `7).`（y=2405.35）——全部核心同页同 y 同文；
  - 行首标点 4 处：P3 y=789.65 `: on le pose…`、P4 y=837.12 `: quarts de finale vendredi 6`、P5 y=430.65 `: clôture du festival.`、P7 y=428.1 `: attention à l'accord…`——全部为冻结法语冒号引出句，核心同 y 同文；
  - 核心对照另有 5 处中文讲解行旗标（本版荷兰语化后消失），不属新增。
- 本轮对此项格外严格：除上述扫描外，另设安全网——全版所有文本节点逐个检查行首字符，**无任何节点以 `!` 或 `?` 起头**；P4 修复行经卡面裁切与整卡双重目视确认（门 1）。第一轮阻塞项（P4 次行 `! »` 起头）已不存在。

## 门 7 — 读者角：通过（零编造）

- 标注编辑示例（法语，冻结）：`« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).`
- 三事实披露（荷兰语，园地框内，逐字）：`Opmerking van de redactie: geen echte brieven en geen beste VOL.2-pagina-8-tekst binnen (geen W44-nummer); beide volgen in VOL.4.`——同时覆盖：(i) 无真实来信、(ii) 无 VOL.2 P8 最佳作文、(iii) 均延至 VOL.4。法语编辑部说明（冻结）亦在位：`Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.`
- 显式祈使征集句（逐字，园地框荷兰语点评末句）：`Stuur je brief én je beste pagina-8-tekst in voor VOL.4!`——字面覆盖范围裁决：`Stuur … in` 为祈使征集；`je brief` = 来信；`én je beste pagina-8-tekst` = 最佳 P8 文本；`voor VOL.4` = 指向 VOL.4。**一句之内同时覆盖来信与最佳 P8 文本**，无需借助他页或预告组合。预告条 `en jullie brieven!` 不计作征集（本句本身已完整，本节不依赖它）。
- 无任何真实投稿冒充：本期示例已标注，延期披露完整，VOL.4 兑现清单（大师赛周末结果、预算周表决与参议院社保审议、真实投稿点评）为核心交接原样继承。

## 门 8 — 家具三方对照（核心 / W43 同配对版 / 本版）：通过

- 配对徽标：串逐字节 = W43：`TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`；几何 **(975, 574)、22pt、BRICK #a4553a、bold、middle**，W43 与本版逐项相同（含 fill 属性；核心同位置为中文串，几何相同）。FR 族无空闲副标题槽、徽标插入 y=574 的家族先例（#20 FR 情形）得到遵守。
- 页脚：左串 `Le Lucerna · FRANS WEEKBLAD VOL.3 · TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS` 8/8；右串 `Pagina N van 8` 8/8；W43 对应串仅 VOL.2 不同（VOL 号差异合法）。
- 副标/标语/顶栏：P1 顶栏中段荷兰语串与 W43 逐字相同（`HEBDOMADAIRE EN FRANÇAIS · ELKE WEEK · HET FRANS DAT DE FRANSEN LEZEN`）；副标题 `WEEKBLAD IN HET FRANS · VOL.3 · FINALEWEEKEND`（主题词 FINALEWEEKEND 为本期事实，W43 为 HERFST EN FEESTEN）；y=372 法语 strapline 两树/W43 逐字相同；左 `VOL. 3 · NR. 3`（W43 为 `VOL. 2 · NR. 2`）；暗带矩形 (65, 424, 1820×118, #2c2822) 三树相同。
- 规则线：每页 `<line>` 数量与核心相等（P1 9、P2 8、P3 4、P4 5、P5 2、P6 8、P7 14、P8 10）；P1/P6/P7 线多重集与核心逐字节相同，其余页差异项仅为流驱动的同规格规则线 y 位移（同 x 跨度、同 stroke、同线宽），无规则线增删或几何改动。
- 矩形：P1 矩形多重集与核心逐字相同；其余各页矩形总数与核心相等，差异项仅为流驱动的框高/标记位移（如 gloss 框高 205.125 vs 175.4、60×30 级别标记 y 位移），无暗带/规则线几何改动。
- 栏头：法语 + 荷兰语双语体例全版一致（如 `À VOUS ! · JOUW BEURT`、`DIRE LA DATE · ZO ZEG JE DE DATUM`、`LANGUE EN MAIN · TAAL IN DE PRAKTIJK`、`CLINIQUE DES ERREURS · PAS OP!`、`BOÎTE À OUTILS · OP ZAK`、`LE CALENDRIER PRÉVU · GEPLANDE KALENDER (NOG GEEN RESULTATEN)`（卡面确认在 896px 宽图表框内））。
- gloss 前缀：`Uitleg — `（bslib4 gloss()，与 W43 一致；P1 词表 5 行见门 5）。
- P8 分隔与栏头：分隔 `— PAGINA n —` ×8（n=1–8）与 W43 形式逐字相同（含字节）；keys 头 `RÉPONSES · ALLE ANTWOORDEN MET NOTEN (PAGINA 1–8)` 与 W43 逐字节相同；答案括号为半角加空格 ` (note)`（W43 形式，核心为全角 `（note）`，家族转换正确）；P8 栏头法语 + 荷兰语双语（如 `A · TEXTE À TROUS · GATENTEKST`，为核心 `完形填空` 后缀的荷兰语替换，见 OBS-2）。

## 门 9 — 图片：通过

3 张 payload 双口径（base64 文本 sha256 前 16 位 + 解码 JPEG sha256 前 16 位）与核心逐项相同，放置坐标与核心逐项相同：

| 版 | 放置 (x, y, w×h) | base64 sha16 | 解码 JPEG sha16 | 解码字节 | credit 行（Commons Artist 原文，同坐标） |
|---|---|---|---|---|---|
| P1 | 65, 1874, 896×320 | `ff20bc2bd2654cdc` | `f3705af28f175ce4` | 334,674 | `Eugène Atget (1857-1927), photographie, domaine public`（y=2271.3） |
| P2 | 1451, 200, 434×480 | `6918cb8bbe4b4bec` | `5b772facb5db886c` | 646,242 | `Utagawa Hiroshige (1797-1858), estampe, domaine public ·`（y=757.3）+ `LACMA`（y=777.45） |
| P3 | 1451, 200, 434×540 | `bfaadf5b6b912416` | `be071fdae81a71b4` | 142,340 | `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle,`（y=842.95）+ `domaine public`（y=863.1） |

三图 `<image>` 元素 + 图说 + credit 行齐全；均为明确公有领域素材（Atget 1857–1927、Hiroshige 1797–1858/LACMA、Blanco《Flora de Filipinas》19 世纪）。P2/P3 credit 为跨行节点拼接，拼接后与核心 credit 逐字相同（P2/P3 被删无 CJK 节点为 0 亦佐证）。

## 门 10 — 网页版 PDF：通过

- 8 页 JPEG 流（pdfimages 提取，1950×2700，150ppi）与自有配方（tools venv Pillow，交付卡片转 RGB）重建流逐字节比对：**默认编码 8/8 相同、q75 8/8 相同**（676,446 / 656,710 / 607,244 / 654,202 / 545,717 / 584,891 / 669,621 / 892,500 字节）、**q72 8/8 不同**。结论：默认质量 = q75；流 = 卡片编码这一门通过，故不存在 fr-en 式旧噪声根源。
- 与修复前流比对（修复员 `recipe-check/oldstreams`，本轮独立提取交付 PDF）：**7/8 逐字节相同，仅 p4（pg-003）变化**（654,202 vs 修复前 654,518），与修复范围一致。
- pdftoppm -r 150 逐页渲染（1950×2700，与卡片同尺寸）vs 卡片：LANCZOS 下采样至 195×270 的 L 通道均值绝对差 p1–p8 为 **1.35 / 1.15 / 1.07 / 1.13 / 0.97 / 1.04 / 1.26 / 1.46**（RGB 三通道均值口径下 p1/p4/p8 为 1.55 / 1.39 / 1.69，与修复员 1.48 / 1.32 / 1.61 同量级，滤波/口径差而已）；全分辨率 L 均值差 4.6–9.0 系 JPEG q75 重压缩正常值；纸色渲染 (248, 241, 225) vs 卡片 (247, 241, 226)，差 1 级。**无噪声页、无离群页。**
- 印刷 PDF 抽查：p1 pdftoppm 渲染（3047×4219）下采样 L 均值差 vs 卡片 **1.558**；印刷 p1 渲染 vs 网页 p1 渲染下采样 L 均值差 2.42（高分辨率光栅化差异量级），同页无内容差异，干净。

## 门 11 — transform 单独复现：通过（阻塞级门，复现成功）

自有 scratch 内全新核心拷贝 + 建造树 `transform.py` 单文件运行（transform.py sha256 `a9ecb2bd…`，与修复员 repro 用文件相同；未在原地运行建造树；transform 自身 OUT 指向交付目录，故渲染前先把 scratch 拷贝内 content 文件的 OUT 重定向到自有 scratch——transform 逻辑本身未改）：

- ROUND=1、2、3 顺序执行均 exit 0；ROUND=3 仅 `content34.py: 1 replacements applied`（即 §3 单处 `Kom op!` → `Kom!`）；ROUND=1/2 的替换计数与建造员轮次一致（ROUND=2 含 content8 14 处）。
- 最终渲染（单进程驱动，`import content12, content34, content56, content7, content8` + REG 导出）：**8 SVG 与交付 8/8 逐字节相同**；流日志独立打出 **P8-battery 1468、P8-keys 2509**；零 OVERFLOW / TOO WIDE；REG 导出总量 150、分页与级别分布见门 4。
- 结论：交付确为 transform.py 三轮完整应用的结果，不存在部分状态残留。本门通过。（复现中两次自有 scratch 操作失误——多目标 cp 致 assets 漏拷、驱动脚本 REG 键名笔误——均在自有 scratch 内纠正后重跑成功，与交付无关，不影响结论；最终三路渲染——分版新、分版旧、核心——均 exit 0。）

## 门 12 — ABSTRACT：通过

- 荷兰语单行（1 逻辑行，427 字节），无 ASCII 双引号；含刊头 `Le Lucerna`、目标语名 `Frans`、级别 `A2 tot B2`、题量 `150 oefeningen`、荷兰语讲解说明。
- 真实主题关键词逐词在刊内找出处（全版拼接文本计数）：`Rolex Paris Masters` 2、`Nanterre` 10、`Peur sur le Parc` 5、`Plailly` 11、`Le Goût du Large` 3、`Port-en-Bessin` 14、`Pitchfork` 11、`Assemblée` 11；学习者短语 `leer Frans door te lezen`、`Franse grammatica`、`woordenschat` 均在 ABSTRACT 内，均为真实学习者检索表述，非模板换词。
- “桥接”一词：交付纸面（8 SVG）、ABSTRACT、KIT、构建代码（bslib4、content12/34/56/7/8、svglib、transform.py）中 **出现 0 次**。KIT 以 Round 记录叙述修复过程，未写出该词；任务书所称 KIT 自述元语言句例外在本版无适用对象。**不阻塞。**

## 门 13 — 全部 8 张卡目视检查：通过

逐版看图（卡片即交付卡片，1950×2700）：P1 徽标/议程框/Atget 照片与 credit 在位，无重叠；P2 Hiroshige 图与 credit、右缘两行荷兰语行字迹完整在框内（`hoofdtelwoorden` 全词经裁切放大确认）；P3 Blanco 图谱与节日词表在位；P4 chiffres 框 `41e édition en 2026 (40e anniversaire)` 在位、解说员框修复行在位无其他缺陷；P5 Creator Week 框含 #8 verbatim 句；P6 日历图表标签清晰无遮挡、来源行在位；P7 金句表/诊所/读者园地/预告条均在位，读者框与预告条余量见门 5；P8 电池 Q120 题干选项、135–139 箭头题、150 写作题、写作条、MODÈLE 范文、答案流末端均在页脚线之上。**目视无重叠、无压线、无出框。**

## 非阻塞观察（单列，不得混入阻塞项）

- OBS-1：P2 两行右缘墨迹超 0.04/0.15px 为 PIL 取框舍入量级，advance 恰 1885.0，卡面裁切确认字迹完整，非缺陷。
- OBS-2：P8 电池栏头本版为 `ÉVALUATION · ANTWOORDEN ONDERAAN DEZE PAGINA`，W43 为 `TOETS · DE ANTWOORDEN ONDERAAN DEZE PAGINA`。本版形式为核心栏头（`综合评估 ÉVALUATION · 答案在本版下方`）的法语头保留 + 荷兰语后缀替换，与 keys 头、分隔符的 W43 一致性无冲突，非缺陷；栏目头荷兰语后缀个别措辞与 W43 不同（如 `TAAL IN DE PRAKTIJK` vs W43 `TAAL IN DE HAND`、`GATENTEKST` vs W43 `VUL IN`），均为同一双语体例下的本期措辞，且与核心栏目结构对应，非缺陷。
- OBS-3：修复员 `recipe-check/newstreams/pg-003.jpg` 经比对与修复前旧流逐字节相同（654,518 字节），属陈旧副本，非交付物；交付网页 PDF 本轮独立提取的 p4 流为 654,202 字节，与修复员 `webcheck-new.txt` 所载“pg-3 CHANGED”一致。交付本身无误，此项仅提示证据目录有陈旧文件。
- OBS-4：P8 F 组 3 行墨迹至 1899.5 与核心同行值逐字相同，属核心继承几何，非本版缺陷。
- OBS-5：P1-hiver 流 2298（底线 2290）、P6-ex 流 2557（底线 2540）两处软底超限，经自有 scratch 核心渲染独立复现为核心同值，墨迹均未越页脚线（审计 FOOTER 0），属核心继承余量，非本版缺陷。
- OBS-6：P8 答案流光标 2509 与全页最大墨迹 2540.73 的区别已在门 5 明确裁决；今后引用“距页脚线”须注明是流光标间隙（71px）还是墨迹间隙（39.27px）。

## 证据（同目录 work/ 下）

- `work/delivery-sha-t0.txt`（开工哈希）、`work/delivery-sha-final.txt`（终态哈希，20/20 与开工相同）、`work/core-sha-before.txt` / `core-sha-after.txt`（核心未动）
- `work/baseline-fr-core/`（核心基线重跑）、`work/freeze-diff.txt` + `freeze-diff.json`、`work/occlusion-ed.txt` / `occlusion-core.txt` / `occlusion-new.txt`（+ 同名 .json）
- `work/p8-plain.txt` + `p8-plain.json`、`work/keycompare.txt` + `keycompare.json`
- `work/check2.py` + `check2.txt`（P4 框/冻结串/右缘/同基线/孤儿/P8 口径/读者角/家具/图片/ABSTRACT）、`work/check2b.txt`（冻结差分分类/credit 节点/W43 分隔字节/P7 框）、`work/check2c.txt`（P8 重绕排片段/P8 栏头/P7 框域/P1 gloss 框）、`work/check_gloss.txt`（gloss 计数 + 金句联合计数 + 范文定位）、`work/check_furn2.txt`（刊头三方/矩形多重集/栏头）
- `work/repro/`（ROUND=1→2→3 全新复现：transform 日志 `repro-transform-r1/2/3.log`、渲染日志 `repro-render.log`、REG `reg.json`、8/8 交付比对）、`work/repro-old/`（ROUND=1→2 修复前对照：P4 新旧 2 节点 diff 依据）、`work/core-render/` + `core-render.log`（核心单进程渲染对照：8/8 命中、P1-hiver/P6-ex 核心同值）
- `work/webcheck/`（pdfimages 提取流、Pillow 重建比对 `rebuild.txt`、pdftoppm 渲染 `render-*.png` / `print-p1-1.png`、像素比对 `pixel.txt`）
- `work/crop-p4-cheer.png`（P4 解说员框放大裁切）、`work/crop-p2-edge.png`（P2 右缘行放大裁切）

## 交回

结论：**ZERO PROBLEMS**。第一轮阻塞项已修复并经本轮从头验证消除；其余门全部通过。未上架、未发 Discord、未动 weekly-git/核心/交付/tools。
