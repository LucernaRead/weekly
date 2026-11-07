# W45 FR×NL 独立校对报告（目标语言法语 · 读者母语荷兰语 · VOL.3）

## 结论：NOT PASS

**阻塞项（1 项）：**

1. **P4 解说员短语框行首孤悬感叹号（新增，非核心继承）。** P4 `LES PHRASES DU COMMENTATEUR` 框内，法语喝彩句 `« Quelle action ! »` 被断行拆开：首行止于 `Quelle action`，次行以 `!` 起头。核心同框同句不断在 `!` 前（核心首行即含完整 `« Quelle action ! »`）。建造员“行首标点新增 0”的自述与此实测不符。详见门 6。

除阻塞项 1 外，其余 13 门全部通过（实测值见下）。本报告不宣布上架；修复后须对 P4 重校（孤儿重扫 + P4 卡面）方可改判。

**校对方式与边界：** 本校对未派生下级代理；未碰 `weekly-git`；未改核心目录、交付目录、`tools/` 下任何文件；未清理共享 scratch；未发 Discord；未往主聊天发卡片/PDF；未建 cron；未宣布上架。所有重跑均在自有 scratch（`hidden_files/w45/fr-nl-proof/work/`）内完成，构建树脚本凡含写回交付/核心目录的 OUT 路径者，一律先拷到自有 scratch 并重定向 OUT 后再运行。工具版本：`tools/p8.py` sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`（与任务书所称已验证新版一致）；渲染/审计解释器一律 `tools/venv/bin/python`。

## 开工查重（硬性）

- 交付目录 mtime：SVG 2026-10-28 05:49 UTC、卡片/PDF 05:53 UTC、KIT 05:56 UTC；开工前 90 秒静默复查（05:59:06 → 06:00:36 UTC）：16/16 文件 sha256 无变化，无属于本版树的在途进程。结论：已完工交付物 + 静默复查无变化 = 安全开工，非 stand down。
- 校对全程结束复查：交付 16/16 哈希仍与开工时一致；核心 8 SVG 哈希值与开工前一致（仅路径前缀写法不同，哈希值逐字相同）。核心与交付均未被本校对改动。

## 交付 pin 独立重测（不采信建造员声称）

| 文件 | 实测 | 建造员声称 | 结论 |
|---|---|---|---|
| 印刷 PDF `Le-Lucerna-VOL3-NL.pdf` | 9,746,750 字节，sha256 `be303278099e439f38de8548dd04174e3a8237dc2b69176a9fcbd7c3581acaeb`，8 页，1462.5×2025 pts | 相同 | ✓ |
| 网页 PDF `Le-Lucerna-VOL3-NL-web.pdf` | 5,292,087 字节，sha256 `fe33b3b97d63cc171c89e85e512d56e0e72172ccd44b9378c6af1a489faa3148`，8 页，936×1296 pts，Title `Le-Lucerna-VOL3-NL-web` | 相同 | ✓ |
| `ABSTRACT.txt` | 427 字节，sha256 `da96d172e93cf84d580de78816269c34f18ece209630ff5aa8a229598e55b81b` | 427 字节 | ✓ |
| SVG 8 张 | sha256 与 KIT 表逐项一致（p1 `be470c26…`、p2 `a4f58e2d…`、p3 `b7da0abf…`、p4 `c02caace…`、p5 `03099928…`、p6 `423f7113…`、p7 `c7464eeb…`、p8 `876c268e…`） | 相同 | ✓ |
| 卡片 8 张 | sha256 与 KIT 表逐项一致（1950×2700 PNG） | 相同 | ✓ |

## 门 1 — 冻结：通过（阻塞项 1 不属于冻结串本身，见门 6）

- 核心基线自有 scratch 重跑：`tools/freeze.py baseline`（核心构建 `hidden_files/weekly-report-w45-fr-build`）**8/8 逐字节**：p1 `f02e628e…`、p2 `b192c192…`、p3 `5f332e9f…`、p4 `240f379d…`、p5 `a4d64e3e…`、p6 `47e4346d…`、p7 `e997123f…`、p8 `822dbe3d…`；运行前后核心 SVG 重哈希不变。
- `freeze.py diff` 核心→本版：新增 CJK 字符 **8 页均为 0**；本版 8 SVG 文本节点 CJK 均为 0（核心对应页 CJK 为 192/219/156/171/159/170/328/788，全部被讲解层替换，无残留）。
- P4 `41e édition en 2026 (40e anniversaire)`：拼接文本核对在位；全文 `40e` 仅 1 处、`41e` 仅 1 处（本版与核心一致；单节点检索呈切分假阴性，节点为 `41e édition en 2026 (40e` + 续行，拼接后完整）。
- Q120：题干 `Si j'étais libre dimanche, j'___ à Nanterre.`（P8 电池，B2·120.）+ 选项 `A. irai · B. irais · C. vais`（源文件 content8.py:49 两树题干逐字相同）；键 B（keycompare 120 core=ed=`B`）；P8 注 `si + imparfait → conditionnel; j' = je geëlideerd`（仅讲解层本地化，法语键与条件结构不动）。Q119 题干 `Elle s'intéresse ___ festivals. A. à les · B. aux · C. des`、Q121 题干 `À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant` 两树源文件逐字相同，键分别为 B、A（keycompare 无 mismatch）。
- P7 引用 #4：P4 辩论框 verbatim `plus excitante ou plus frustrante ?` 与 P7 比较级定义段、工具箱 B1 句逐字一致；#8：P5 verbatim `Les jeunes créateurs y rencontrent leur public, en vrai.` 与 P7 金句表、Q106 改写（error `rencontre`，键 `rencontrent`，keycompare 106 两树键逐字相同）一致。
- P6 同步：`Ce calendrier peut encore bouger.`（P6 词句对 + P7 金句表 + 深读段小写形 `peut encore bouger,` y=984.46 两树同坐标）；P6 微习题键 `peut`（95、102 两树键逐字相同）。
- P7 法语定义句冻结：核心 P7 文本节点多重集差分中，被删节点全部含 CJK（讲解行），唯一非 CJK 被删节点 `）。` 是中文讲解行绕排尾巴；**没有任何纯法语定义节点被删**，上层语法定义段（REPRENDRE / FUTUR PROCHE / PASSÉ COMPOSÉ / COMPARATIF / SUBJONCTIF / ATTENTE）逐字未动，仅讲解行、栏目头荷兰语后缀、诊所注、读者园地荷兰语段被本地化。

## 门 2 — P8 双门：通过

- plain 门（显式双路径 + `--total 150`，未用禁用的 `--target` 形式与默认 total）：`tools/p8.py compare --core-p8 <核心P8> --edition-p8 <本版P8> --total 150` → **CLEAN，noted 97 = 97，missing=[]，extra_count=0，keydiff=[135, 150]**。p8.py 版本 sha 见报告头。
- 全键门：`hidden_files/w45/p8-fr-gap-fix/keycompare.py --total 150` → 全 150 键 mismatch 恰 2 项 **[135, 150]，且两项均为 noted 项，裸键 53 条 mismatch 为 0**（plain CLEAN 对裸键是盲的，本门补齐了该盲区）。
- 135：核心键 `读一份日程，本身就是在了解法国。` → 本版键 `Een programma lezen is al Frankrijk begrijpen.`；题面方向标 `→ NL: « Lire un programme, c'est déjà comprendre la France. »`。150：核心键 `开放题` → 本版键 `Open opdracht`（完整印刷行 `150. Open opdracht — punten in schrijfkader, voorbeeld in MODÈLE-kader (beoordeeld op de punten)`）；两项均为读者语言层重定向，法语键体系不动，沿 W43 先例合法。
- 136–139 逐项核对（题面改向、法语键不动）：136 题面 `→ FR: Hij rent sneller dan zijn broer.`，键 `Il court plus vite que son frère.`；137 题面 `→ FR: De leerlingen zijn sinds 17 oktober op vakantie.`，键 `Les élèves sont en vacances depuis le 17 octobre.`；138 题面 `→ FR: Vanavond gaan we onze schooltassen klaarmaken.`，键 `Ce soir, nous allons préparer nos cartables.`；139 题面 `→ FR: Men kent de finalisten nog niet.`，键 `On ne connaît pas encore les finalistes.`。四键与核心逐字相同（keycompare 无 mismatch）；P8 拼接文本中 `→ NL:` 1 次、`→ FR:` 4 次，方向标约定自 E 节首项确立。

## 门 3 — gloss 逐项计数：通过

渲染口径（gloss() 调用串按 `·` 切分，源文件实测，两树对照）：content12：P1 **7**、P2 **6**；content34：P3 **6**、P4 **7**；content56：P5 **6**、P6 **6**；**合计 38 = 核心 38，逐页 = 核心**（P1 7 / P2 6 / P3 6 / P4 7 / P5 6 / P6 6）。P1 词表 7 项（se jouer / une finale / une demi-finale / un quart de finale / une nocturne / un frisson / la coquille Saint-Jacques）无丢失。

## 门 4 — 金句：通过

P7 金句表 8 句逐字 + 页签全对（页签：#1 p2、#2 p1、#3 p3、#4 p4、#5 p5、#6 p6、#7 p1、#8 p5）：

| # | 金句 | 联合计数（本版 = 核心） | 所标源文章页实测命中 |
|---|---|---|---|
| 1 | Le lundi 2 novembre, on reprend les cours. | 5 | P2 `on reprend les cours` ✓ |
| 2 | On ne connaît pas encore les finalistes. | 3 | P1 `ne connaît pas encore les finalistes` ✓（P1 文章行为该分句，P7 表加主语 On） |
| 3 | Les cimetières se sont remplis de chrysanthèmes. | 1 | P3 `se sont remplis de … chrysanthèmes` ✓ |
| 4 | Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? | 5 | P4 辩论框 verbatim ✓ |
| 5 | Le festival se promène dans Paris. | 1 | P5 `festival se promène dans Paris` ✓ |
| 6 | Ce calendrier peut encore bouger. | 3 | P6 verbatim ✓ |
| 7 | Ce week-end, tout se joue. | 1 | P1 `Ce week-end, tout se joue`（跨节点拼接）✓ |
| 8 | Les jeunes créateurs y rencontrent leur public, en vrai. | 3 | P5 verbatim ✓ |

联合计数与任务书所给核心计数（5/3/1/5/1/3/1/3）逐项一致。

## 门 5 — 几何：通过（P8 裁决依据见本节末，不以“per fr-de 前例”带过）

- canonical 审计（自检先行通过，6 类 planted flag 全部触发、clean 对照静默）：**本版 0 flags、核心 0 flags、NEW vs core 0**。
- 同基线墨迹间距：P1 顶栏 y=92 三段间隙 **337.4px / 112.0px**（核心对应间隙 387.5/196.2，均为荷兰语/中文串长差异，无重叠）；8 版页脚 y=2624 左右段间隙均为 **782.2px**（核心 1157.1px，系页脚右串 `Pagina N van 8` 长于中文串，无重叠）。
- 全页右缘扫描（墨迹口径，审计工具不抓框线切字故另行扫描）：本版仅 5 行超 1885——P2 两行荷兰语行 advance 恰 1885.0、墨迹仅 **1885.04 / 1885.15**（PIL 取框舍入量级，卡面在框内，见非阻塞观察 OBS-2）；P8 F 组 3 行法语原文配对行墨迹 **1891.25 / 1891.25 / 1899.5**，与核心同行墨迹值逐字相同（核心 y 为 940/1016/1054，本版 y 为 998/1074/1112，系版式流位移，墨迹值不变），属核心继承几何（OBS-3）。
- P6 图表标签覆盖（基线锚定墨迹法，排除图表自有框；getbbox 法已弃用）：图表文本 **12 个，最大覆盖 0.0% < 30%**（核心同口径亦 0.0%）；图表为纯文字行、无柱体遮挡。
- P8 三口径（本版 vs 核心同口径对照）：
  - 流光标（独立复现渲染日志，见门 11）：电池流 **1468 < 1485**（写作条底线，H 头 y=1526、MODÈLE 框顶 y=1500 之前）；答案流 **2509 < 2545**（Flow 设定底线）。两值均由自有 scratch 复现渲染独立打出，非抄建造员日志。
  - 最大基线：电池 **1455.83（= 核心）**；答案 **2537.73（核心 2539.19）**。
  - 墨迹底：电池 **1456.08（= 核心）**；答案 **2540.73（核心 2541.23）**，距页脚线 2580 余 **39.27px**（核心 38.77px）；审计 FOOTER 旗 0（除页脚基线 2624 豁免外无墨迹越 2580）。
  - **裁决依据（明确记录）：** 通过的依据是“墨迹底 < 页脚线 2580 + 审计 FOOTER 0 + 流光标 < 各自 Flow 底线”，而非单看 2509。必须说明：2509 是答案流最后一栏（x=1451）的光标，不是全页最大墨迹；全页最大墨迹在 x=527 栏（2540.73）。建造员所称“距页脚线 71px”仅是 2580−2509 的流光标间隙，真实墨迹间隙为 39.27px——两者均通过，但不得把 71px 引用为墨迹间隙。
- P7 预告墨迹底 **2499.00**，预告条底 2540，余量 **41.00px**；读者框墨迹底 **2238.30**，框底 2258，余量 **19.70px**；两者均在框内且低于页脚线。

## 门 6 — 换行/孤儿：NOT PASS（阻塞项 1 在此门）

- 零 OVERFLOW：自有复现渲染日志（R1 与最终轮）无 FLOW OVERFLOW / HEAD TOO WIDE 警告；P1-hiver、P6-ex 两处流终值与核心逐字相同（见 OBS-6）。
- 末行短 token：本版旗标 **4 处，均核心同页同 y 逐字继承**：P1 `p.8`（y=1604.0）、P2 `___`（y=2140.9）、P2 `___`（y=2459.1）、P3 `7).`（y=2405.35）。核心对照扫描另有中文讲解行末标点旗标（本版荷兰语化后消失），不属新增。
- 行首标点：继承项 3 处与核心同坐标同结构——P3 y=789.65 `: on le pose…`、P5 y=430.65 `: clôture du festival.`、P7 y=428.1 `: attention à l'accord…`（均为冻结法语冒号引出句，核心同 y 同文）；P4 y=837.12 `: quarts de finale vendredi 6` 亦为核心同文继承。
- **阻塞项 1（新增行首标点，核心无此结构）：P4 解说员短语框（x=1007，serif 21.5pt）：**
  - 本版首行 y=902.095：`« Allez ! » — Kom op! · « Quelle action`（止于 `action`，引语未闭合）；
  - 本版次行 y=932.625：`! » — Wat een actie!`（**以 `!` 起头**，感叹号与其短语 `Quelle action !` 分离）；
  - 核心同框：首行 y=872.37：`« Allez ! » — 加油！ · « Quelle action ! »`（完整闭合），次行 y=902.90：`— 好球！`（以破折号起头，非 `!`）；
  - 成因：荷兰语释义 `Kom op!` 长于中文 `加油！`，绕排在法语空格标点 `action !` 之间断开（法语 `!` 前有空格，排版器将其视为独立 token）；
  - 卡面确认：P4 卡 `LES PHRASES DU COMMENTATEUR` 框内次行确以 `! »` 起头，非测量假阳性；
  - 判定：本版新增的孤悬标点，拆开的是冻结法语喝彩句本身；建造员“行首标点新增 0”与此实测不符。按行首孤悬标点在扫描内的既有口径（×KO 诸版已将行首孤悬标点列入扫描），此项为阻塞。修复方向由建造员/协调员定（调整荷兰语释义长度或法语空格标点的不断行处理均可），修复后须重扫孤儿 + 重看 P4 卡面。
- 跨栏换行：同 x/同字号/同字体分块扫描未见新增跨栏断裂；P8 电池与答案栏位移均为流内正常换行。

## 门 7 — 读者角：通过（零编造）

- 标注编辑示例（法语，冻结）：`« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).`
- 三事实披露（荷兰语，园地框内，逐字）：`Opmerking van de redactie: geen echte brieven en geen beste VOL.2-pagina-8-tekst binnen (geen W44-nummer); beide volgen in VOL.4.`——同时覆盖：(i) 无真实来信（geen echte brieven）、(ii) 无 VOL.2 P8 最佳作文（geen beste VOL.2-pagina-8-tekst）、(iii) 均延至 VOL.4（beide volgen in VOL.4）。法语编辑部说明（冻结）亦在位：`Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.`（FR 族核心为 VOL.3，披露所指 VOL.2 为上一期号，正确）。
- 显式祈使征集句（逐字，园地框荷兰语点评末句）：`Stuur je brief én je beste pagina-8-tekst in voor VOL.4!`——字面覆盖范围裁决：`Stuur … in` 为祈使征集；`je brief` = 来信；`én je beste pagina-8-tekst` = 最佳 P8 文本；`voor VOL.4` = 指向 VOL.4。**一句之内同时覆盖来信与最佳 P8 文本**，无需借助他页或预告组合。预告条 `en jullie brieven!` 不计作征集（本句本身已完整，本节不依赖它）。
- 无任何真实投稿冒充：本期示例已标注，延期披露完整，VOL.4 兑现清单（大师赛周末结果、预算周表决与参议院社保审议、真实投稿点评）为核心交接原样继承。

## 门 8 — 家具三方对照（核心 / W43 同配对版 / 本版）：通过

- 配对徽标：串逐字节 = W43：`TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`；几何 **(975, 574)、22pt、BRICK #a4553a、bold、middle**，W43 与本版逐项相同（核心同位置为中文串，几何相同）。FR 族无空闲副标题槽、徽标插入 y=574 的家族先例（#20 FR 情形）得到遵守。
- 页脚：左串 `Le Lucerna · FRANS WEEKBLAD VOL.3 · TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS` 8/8；右串 `Pagina N van 8` 8/8；W43 对应串仅 VOL.2 不同（VOL 号差异合法）。
- 副标/标语/顶栏：P1 顶栏中段荷兰语串与 W43 逐字相同（`HEBDOMADAIRE EN FRANÇAIS · ELKE WEEK · HET FRANS DAT DE FRANSEN LEZEN`）；副标题 `WEEKBLAD IN HET FRANS · VOL.3 · FINALEWEEKEND`（主题词 FINALEWEEKEND 为本期事实，W43 为 HERFST EN FEESTEN）；y=372 法语 strapline 两树/W43 逐字相同；左 `VOL. 3 · NR. 3`（W43 为 `VOL. 2 · NR. 2`）。
- 暗带/规则线：P1 矩形多重集与核心逐字相同；其余各页矩形总数与核心相等，差异项仅为流驱动的框高/标记位移（如 gloss 框高 205.125 vs 175.4、60×30 标记 y 位移），无暗带/规则线几何改动。
- 栏头：法语 + 荷兰语双语体例全版一致（如 `À VOUS ! · JOUW BEURT`、`DIRE LA DATE · ZO ZEG JE DE DATUM`、`LANGUE EN MAIN · TAAL IN DE PRAKTIJK`、`CLINIQUE DES ERREURS · PAS OP!`、`BOÎTE À OUTILS · OP ZAK`、`LE CALENDRIER PRÉVU · GEPLANDE KALENDER (NOG GEEN RESULTATEN)`（卡面确认在 896px 宽图表框内）。
- gloss 前缀：`Uitleg — `（bslib4 gloss()，与 W43 一致；P1 词表含前缀实测 5 行，见门 12）。
- P8 分隔与栏头：分隔 `— PAGINA n —` ×8（n=1–8）与 W43 形式逐字相同；keys 头 `RÉPONSES · ALLE ANTWOORDEN MET NOTEN (PAGINA 1–8)` 与 W43 逐字节相同；答案括号为半角加空格 ` (note)`（W43 形式，核心为全角 `（note）`，家族转换正确）。

## 门 9 — 图片：通过

3 张 payload 双口径（base64 文本 sha256 前 16 位 + 解码 JPEG sha256 前 16 位）与核心逐项相同，放置坐标与核心逐项相同：

| 版 | 放置 (x, y, w×h) | base64 sha16 | 解码 JPEG sha16 | 解码字节 | credit 行（Commons Artist 原文，同坐标） |
|---|---|---|---|---|---|
| P1 | 65, 1874, 896×320 | `ff20bc2bd2654cdc` | `f3705af28f175ce4` | 334,674 | `Eugène Atget (1857-1927), photographie, domaine public`（y=2271.3） |
| P2 | 1451, 200, 434×480 | `6918cb8bbe4b4bec` | `5b772facb5db886c` | 646,242 | `Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA`（y=757.3 / 777.45） |
| P3 | 1451, 200, 434×540 | `bfaadf5b6b912416` | `be071fdae81a71b4` | 142,340 | `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public`（y=842.95） |

三图 `<image>` 元素 + 图说 + credit 行齐全；均为明确公有领域素材（Atget 1857–1927、Hiroshige 1797–1858/LACMA、Blanco《Flora de Filipinas》19 世纪）。

## 门 10 — 网页版 PDF：通过

- 8 页 JPEG 流（pdfimages 提取，1950×2700，150ppi）与自有配方（tools venv Pillow 13.0.0，交付卡片转 RGB）重建流逐字节比对：**q75 8/8 相同**（676,446 / 656,710 / 607,244 / 654,518 / 545,717 / 584,891 / 669,621 / 892,500 字节）、**q72 8/8 不同**、**不传 quality 的默认编码 8/8 相同**。结论：默认质量 = q75（与建造员一致）；质量参数本身按任务书不阻塞。流 = 卡片编码这一门通过，故不存在 fr-en 式旧噪声根源（旧文件流非新鲜卡片编码）。
- pdftoppm -r 150 逐页渲染（1950×2700，与卡片同尺寸）vs 卡片：195×270 下采样均值绝对差 p1–p8 为 **0.50 / 0.45 / 0.43 / 0.45 / 0.38 / 0.43 / 0.50 / 0.65**（建造员同法测得 1.48/1.36/1.29/1.32/1.20/1.26/1.42/1.61——resize 滤波差异所致，量级结论相同，均远非噪声页的 100 量级）；纸色均值与 KIT 逐页一致到 0.1（p1 (219.2, 213.8, 198.9) 等）；逐像素均值差 5.2–9.7 系 JPEG q75 重压缩正常值，非噪声。**无噪声页、无离群页。**
- 印刷 PDF 抽查：p1 pdftoppm 渲染（3047×4219）下采样均值与卡片差 **0.016**，干净。

## 门 11 — transform 单独复现：通过（阻塞级门，复现成功）

自有 scratch 内全新核心拷贝 + 建造树 `transform.py` 单文件运行（未在原地运行建造树；transform 自身 OUT 指向交付目录，故复现渲染前先把 scratch 拷贝内 content 文件的 OUT 重定向到自有 scratch——transform 逻辑本身未改）：

- Round 1：OUT 各 1 + 断言替换 bslib4 3 / content12 57 / content34 81 / content56 68 / content7 30 / content8 58，CJK 门 clean，`TRANSFORM OK`；渲染流日志 **P8-battery 1526（>1485）、P8-keys 2646（>2545）**，与建造员披露的 Round 1 超限值逐字复现；Round 1 渲染 SVG 与建造员 `scratch/pre-fix-round2.sha` **8/8 逐字节相同**（含 P1 `a6f425d6…`、P8 `6ec21f09…`）。
- Round 2：应用计数 **7 / 6 / 8 / 4 / 14**（content12/34/56/7/8），与建造员披露的轮次计数一致；含 content34 `\'s` 转义修正后的完整重跑（Round 2 首跑中途断裂、content12 已先写盘 7 处一事，经源码比对 + 下述复现验证，**最终交付无残留部分状态**）。
- 源码比对：Round 1→2 顺序执行后的 8 个文件（bslib4、content12/34/56/7/8、svglib、transform.py）与建造树**逐字节相同**。
- 最终渲染（单进程驱动）：**8 SVG 与交付 8/8 逐字节相同**；流日志独立打出 **P8-battery 1468、P8-keys 2509**；Round 2 后仅 P1/P8 相对 Round 1 变化，P2–P7 与 Round 1 逐字节相同——与建造员轮次基线链声称一致。
- 结论：交付确为 transform.py 两轮完整应用的结果，不存在部分状态残留。本门通过。

## 门 12 — 建造员另两项约定：逐项裁决，均通过

- (a) P8 翻译题方向标箭头式（`→ NL:` / `→ FR:`）：法语键除 135/150 两项读者语言重定向外全部不变（门 2 全键比对）；136–139 法语键逐字不变；电池流 1468 < 1485（门 5/11 复现）；约定自 E 节首项（135）确立，136–139 各题方向标自明。**裁决：通过。** 另注：Round 2 中 137 题面删 `al`（`al sinds` → `sinds`）、139 题面改写（`Mensen weten nog niet wie de finalisten zijn.` → `Men kent de finalisten nog niet.`）仍为荷兰语待译句，法语键未动，合法。
- (b) P1 词表裸短式（含 `Uitleg — ` 前缀实测 5 行）：5 行墨迹最右 **939.0**，框右 961（框 x=527、宽 434），余量 22px；7 项无丢失（门 3）；头条流无溢出（门 6 零 OVERFLOW；P1 gloss 框矩形与核心逐字相同）。**裁决：通过。**

## 门 13 — ABSTRACT：通过

- 荷兰语单行（1 逻辑行，427 字节），无 ASCII 双引号；含刊头 `Le Lucerna`、目标语名 `Frans`、级别 `A2 tot B2`、题量 `150 oefeningen`、荷兰语讲解说明。
- 真实主题关键词逐词在刊内找出处（拼接文本计数）：`Rolex Paris Masters` 2、`Nanterre` 10、`Peur sur le Parc` 5、`Plailly` 11、`Le Goût du Large` 6、`Port-en-Bessin` 14、`Pitchfork` 11、`Assemblée` 11；学习者短语 `leer Frans door te lezen`（+ `Franse grammatica`、`woordenschat`）为真实学习者检索表述，非模板换词。
- “桥接”一词：交付纸面（8 SVG）、ABSTRACT、构建代码（*.py，含 transform.py）及 KIT 中 **出现 0 次**（KIT 以“该中介措辞”代指，未写出该词；任务书所称 KIT 自述元语言句例外在本版无适用对象）。**不阻塞。**

## 门 14 — 全部 8 张卡目视检查：通过（阻塞项 1 除外）

逐版看图（卡片即交付卡片，1950×2700）：P1 徽标/议程框/Atget 照片与 credit 在位，无重叠；P2 Hiroshige 图与 credit、右缘两行荷兰语行字迹完整在框内；P3 Blanco 图谱与节日词表在位；P4 chiffres 框 `41e édition en 2026 (40e anniversaire)` 在位、解说员框除阻塞项 1 的 `! »` 起头行外无其他缺陷；P5 Creator Week 框含 #8  verbatim 句；P6 日历图表标签清晰无遮挡、来源行在位；P7 金句表/诊所/读者园地/预告条均在位，读者框与预告条余量见门 5；P8 电池 Q120 题干选项、135–139 箭头题、150 写作题、写作条、MODÈLE 范文（86 词核心范文未动）、答案流末端均在页脚线之上。**除门 6 阻塞项 1 外，目视无重叠、无压线、无出框。**

## 非阻塞观察（单列，不得混入阻塞项）

- OBS-1（KIT 算术小 slip，仅文档）：transform 断言替换实测为 bslib4 3 + content12 57 + content34 81 + content56 68 + content7 30 + content8 58 = 297 对，另 OUT 重定向 5 处，合计 302；KIT §7 所写“298 项、content8 59”与实测差 1。transform 本身逐项断言且复现 8/8，交付不受影响；KIT 数字建议随手订正。
- OBS-2：P2 两行右缘墨迹超 0.04/0.15px 为 PIL 取框舍入量级，advance 恰 1885.0，卡面字迹完整，非缺陷。
- OBS-3：P8 F 组 3 行墨迹至 1899.5 与核心同行值逐字相同，属核心继承几何，非本版缺陷。
- OBS-4：网页版下采样均值差实测 0.38–0.65 vs 建造员 1.19–1.61，系 resize 滤波/均值口径差异，结论相同（干净、无噪声页）。
- OBS-5：P8 答案流光标 2509 与全页最大墨迹 2540.73 的区别已在门 5 明确裁决；今后引用“距页脚线”须注明是流光标间隙（71px）还是墨迹间隙（39.27px）。
- OBS-6：P1-hiver 流 2298（底线 2290）、P6-ex 流 2557（底线 2540）两处软底超限，经自有 scratch 核心渲染独立复现为核心同值（核心 P1-hiver 2298、P6-ex 2557），墨迹均未越页脚线（审计 FOOTER 0），属核心继承余量，非本版缺陷。
- OBS-7：P5 主流 ED 2532 vs 核心 2502（荷兰语较长所致），仍在底线 2540 与页脚线 2580 内，非缺陷。
- OBS-8：各页矩形差异项均为流驱动框高/标记位移，矩形总数与核心相等，无家具几何改动。

## 证据（同目录 work/ 下）

- `work/delivery-sha-t0.txt`（开工哈希）、`work/baseline-fr-core/`（核心基线重跑）、`work/freeze-diff.txt` + `freeze-diff.json`、`work/occlusion-ed.txt` / `occlusion-core.txt` / `occlusion-new.txt`（+ 同名 .json）、`work/p8-plain.txt` + `p8-plain.json`、`work/keycompare.txt` + `keycompare.json`、`work/p8-core-extract.txt` / `p8-ed-extract.txt`、`work/check_text.txt` / `check_text2.txt`（冻结串、页脚、徽标、P8 行）、`work/check_gloss_golden.txt`（gloss 计数 + 金句联合计数）、`work/check_gold_src.py`（源文章页命中）、`work/check_geom.txt`（右缘/同基线/孤儿/P8 三口径/P7 框/P6 图表/P1 gloss）、`work/p8_structure.txt`（P8 版式分区）、`work/p4_lines.py`（P4 框逐行对照）、`work/p1_gloss.py`（P1 gloss 5 行）、`work/check_furn.py`（徽标三方）、`work/check_img_furn.txt`（图片双哈希、credit、P7 框、栏头、题号结构）、`work/webcheck/`（pdfimages 提取流、pdftoppm 渲染、印刷 P1 对照）、`work/repro-r1/`（Round 1 复现：transform 日志、渲染日志、REG dump、SVG）、`work/repro/`（Round 1→2 完整复现：transform 日志、渲染日志、8/8 交付比对）、`work/repro-r1.sha`、`work/core-render.log`（核心流光标对照）、`work/crop-p4-cheer.png` / `crop-p7-reader-preview.png` / `crop-p8-battery-end.png` / `crop-p1-top.png`（局部放大裁切）、`work/check_text.py` / `check_text2.py` / `check_gloss_golden.py` / `check_geom.py` / `check_img_furn.py` / `p8_structure.py` / `p4_lines.py` / `p1_gloss.py` / `check_furn.py`（自有检查脚本）。

## 交回

结论：**NOT PASS，阻塞项 1 项（P4 行首孤悬 `!`，门 6）**。其余门全部通过；修复该 1 项并重校 P4 后可改判。未上架、未发 Discord、未动 weekly-git/核心/交付/tools。
