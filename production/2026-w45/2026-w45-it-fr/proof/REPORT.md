# W45 IT × FR 独立校对报告 — 结论：ZERO PROBLEMS

- 配对：意大利语目标文本（W45 IT 核心冻结）× 法语讲解层，读者为法语母语者。
- 交付待审：`files/weekly-report-w45-it-fr/`（SVG×8、卡片×8、印刷 PDF、web PDF、WEEKLY-KIT.md、ABSTRACT.txt）。
- 校对方式：全部从头独立重测，未采信构建员自述；共享工具（freeze.py / p8.py / occlusion_audit.py）由校对方另行实跑；几何、右缘、P6 覆盖、题量/级别、gloss、范文、图片、家具均用校对方自写脚本复测。
- 开工查重：开工时无进行中渲染进程；交付目录最后写盘 23:27:30 UTC，90 秒复查零新写盘后开工（新鲜已完成交付，非进行中写盘，不 stand down）。
- 未做事项：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录（只读对照）、未清理共享 scratch。

## 1. 冻结与语言层

- `freeze.py baseline`（W45 IT 核心构建）：**8/8 逐字节复现**，核心事后重哈希不变。
  - p1 `81051bbb…`、p2 `d42ce9ae…`、p3 `9e45586d…`、p4 `62f75269…`、p5 `c907b869…`、p6 `5545f8dd…`、p7 `9fc999f4…`、p8 `3b87e54f…`（全长见 `core-hashes-before.txt`）。
- `freeze.py diff` 核心→本版（多重集出现次数，与 KIT §7 一致）：p1 +28/−26、p2 +35/−29、p3 +33/−31、p4 +30/−25、p5 +43/−35、p6 +29/−24、p7 +45/−41、p8 +171/−168；**新增 CJK 8 页均为 0**（`cjk_added` 全空，版面 CJK 0）。
- 纯意大利语移除项（不含任何汉字的移除串）全量只有 3 组，与 KIT §7 裁定逐项吻合：
  - p6 `bollettino · modello`（中文讲解桥的换行碎片）；
  - p7 `è probabile che / è possibile che / bisogna`（同上）；
  - p8 9 项：17、18、19、20、60、61、85、86、103（均为答案注侧改动，印刷 key 不变，见 §3）。
  - 其余全部移除串均含中文讲解层内容。意大利语正文冻结成立。
- SVG 原始字节扫描（8 页，含非文本节点）：CJK 0、全角标点 0、`桥接` 0；ABSTRACT `桥接` 0。
- 残留中文核实（构建员称“仅不印刷的注册表类型名”，已证实）：
  - 本版构建 `content*.py` 中残留中文全部为 `ex()` 注册第 2 参数的裸类型名，共 142 处：完成句子×61、单选×48、词汇配对×3、造句×7、句型转换×1、判断对错×3、完形单选×13、翻译×4、写作×2；无其他中文串。
  - `bslib4.py`、`svglib.py`、`render.py`、`run.py` 中文 0；`transform.py` 的 252 行中文均为替换源串（旧中文讲解），不印刷。
  - 本版 SVG 文本节点中文 0，卡片由 SVG 渲染而来，8 张卡片目视亦无中文像素。残留中文确实不在任何 SVG 文本节点与卡片像素中出现。

## 2. P7 词框（硬性门）

- 定义句 4 行与核心逐行逐字节一致（同 y、同字号）：
  - `« l'assaggio » è la prova di un cibo:`（y=1128.5）
  - `un piccolo pezzo per decidere se`（y=1159.03）
  - `piace. Questa settimana vive a`（y=1189.56）
  - `pagina 3, alla finale del Panettone.`（y=1220.09）
  - 定义句未本地化；仅其下 gloss 本地化为法语。
- gloss（法语，2 行）：
  - `assaggio = dégustation. Voir page 3, finale`（y=1280.62）
  - `du Panettone.`（y=1309.02）
- 金句 8 句：内文（去 «»）在全版 joined 文本中**每句恰 2 次**（文章 1 次 + P7 1 次），与核心标签页一致：
  - `arriva il primo freddo vero della stagione`、`Non è una certezza, è una probabilità`、`il 2 novembre è la Commemorazione dei defunti`、`Fa freddo, copriti bene!`、`il pubblico può assaggiare gratis`、`il calcio non si ferma per il primo freddo`、`la cultura continua`、`Una probabilità alta non è una certezza`。
  - 说明：带 «» 的整串计数多为 1 次，因文章中出现处嵌在更长行内；内文 2 次才是“摘自本期文章”的正确检验，构建员“2×”结论在此口径下成立。

## 3. P8

- `p8.py compare`：**CLEAN 150=150**，missing=[]、extra_count=0、uncertain=[]。
- `p8.py extract`：核心与本版印刷注释集均为 150/150。
- keydiff `[6,13,14,15,16,20,38,58,71,74,77,137,138,139]` 逐项印刷行对照（key = ` — ` 之前段）：

| 题 | 核心印刷行 | 本版印刷行 | 判定 |
|---|---|---|---|
| 6 | `6. previsioni — previsioni = 预报（复数）` | `6. previsioni — previsioni = prévisions (pluriel)` | 括号分支伪影，key `previsioni` 逐字节同 |
| 13 | `13. guanti — guanti = 手套（复数）` | `13. guanti — guanti = gants (pluriel)` | 伪影，key `guanti` 同 |
| 14 | `14. crisantemi — crisantemi = 菊花（复数）` | `14. crisantemi — crisantemi = chrysanthèmes (pluriel)` | 伪影，key `crisantemi` 同 |
| 15 | `15. termosifoni — termosifoni = 暖气片（复数）` | `15. termosifoni — termosifoni = radiateurs (pluriel)` | 伪影，key `termosifoni` 同 |
| 16 | `16. fa — fare freddo：fa freddo（天气）` | `16. fa — fare freddo : fa freddo (météo)` | 伪影，key `fa` 同（全角冒号→半角为注侧） |
| 20 | `20. resta — restare：la scuola → resta（lei）` | `20. resta — restare : la scuola donne resta (lei)` | 伪影，key `resta` 同 |
| 38 | `38. mandorle — mandorle = 杏仁（复数）` | `38. mandorle — mandorle = amandes (pluriel)` | 伪影，key `mandorle` 同 |
| 58 | `58. più bella — più + bella 周日晚最美（主观评价）` | `58. più bella — più + bella : le dimanche soir est le plus beau` | 伪影，key `più bella` 同 |
| 71 | `71. gratuiti — gratuiti = 免费的（阳性复数）` | `71. gratuiti — gratuits (masculin pluriel)` | 伪影，key `gratuiti` 同 |
| 74 | `74. castagne — castagne arrosto 烤栗子（复数）` | `74. castagne — castagne arrosto = marrons grillés (pluriel)` | 伪影，key `castagne` 同 |
| 77 | `77. ci sarà — esserci 将来时：ci sarà（将有）` | `77. ci sarà — esserci, futur : ci sarà (il y aura)` | 伪影，key `ci sarà` 同 |
| 137 | `137. 周一第一场寒冷来了。 — 对照原文` | `137. Lundi, le premier froid arrive. — Comparer avec l’original.` | 真重定向（IT→FR，W43 裁定合法） |
| 138 | `138. 观众可以免费品尝。 — assaggiare gratis = 免费品尝` | `138. Le public peut déguster gratuitement. — assaggiare gratis =` + 续行 `déguster gratuitement` | 真重定向（IT→FR）；2 行体，续行实测存在 |
| 139 | `139. 周日晚上，佛罗伦萨对尤文图斯。 — si gioca = 进行比赛` | `139. Dimanche soir, on joue Fiorentina–Juventus. — si gioca = on` + 续行 `joue` | 真重定向（IT→FR）；2 行体，续行实测存在 |
| 140 | `140. Ogni previsione deve essere chiara. — dovere = 必须` | `140. Ogni previsione deve essere chiara. — dovere = devoir` | 意大利语 key 逐字节不变 |

- 139 与 140 的区别机制（已核实 P8 E 区题面）：139 题面为意大利语句 `Domenica sera si gioca Fiorentina–Juventus.`，指令 `Traduire en français`，故 key 为法语译文；140 题面为法语句 `Chaque prévision doit être claire.`，指令 `Traduire en italien`，故 key 本就是意大利语句子，只需把注本地化。两者方向相反，处理不同是正确的，不是 139 的遗漏也不是 140 的未重定向。
- §1 的 9 项注侧改动印刷行（key 均不变）：17 `metto`、18 `portano`、19 `guardano`、20 `resta`、60 `ha vinto`、61 `ha pareggiato`、85 `B — 12 moins 9 = 3`、86 `A — 4 plus 5 = 9`、103 `nevica`；其中 85/86 为语言中立算术的法语表述。
- P8 注释纯法语（除意大利语 key、语言中立算术与 `Page`/`PAGINA` 家具外）；P8 注标题 `RISPOSTE · CORRIGÉS — classés par page, cherchez le numéro`，分隔符意大利语 `— PAGINA n —`（8 个全量）。

## 4. 几何

- `occlusion_audit.py`（自检 6 类全触发、干净对照静默）：**本版 0 / 核心 0 / NEW 0**。
- 同基线行距扫描（家具带 y<600 或 y>2550，间隙<2px）：本版 0、核心 0。
- 全 8 页框线压框 + 右缘扫描：
  - ADVANCE 法右缘旗标（>1885）恰 4 项，与构建员自述逐项一致，且核心扫描同串同 advance：
    - P1 y=1728.0，right 1889.3，`« il primo freddo » : il primo freddo serio`（冻结意大利语行）
    - P1 y=1758.1，right 1888.8，`dopo un autunno mite. Questa settimana`（冻结意大利语行）
    - P2 y=2195.0，right 1902.5，`b. il calorifero di casa, che si accende`（冻结意大利语行）
    - P8 y=662.8，right 1898.6，`«La tua settimana del primo freddo» Scrivi 80–100 parole:`（核心同串同 advance，核心 y=633.1；y 位移因法语 E 区题体多绕一行，P8-ex 流止 965、底 1332，松弛充足）
  - 4 项均 <1950 页边，且均未压任何绘制框线（P1 两行所跨矩形仅为页背景与页框 x2=1910/1922；P2/P8 行亦在 1910 内框内）；canonical 真墨审计 EDGE 旗标 0。advance 宽容差解释成立，非本版缺陷。
  - 页脚带（2580<y<2624）文本节点：8 页均为 0；页脚基线 2624 本身除外。
- 流程终值（构建日志 round 5 实测，与 KIT 一致）：
  - P7 col3 止 1673.0；FRASI 规则线实测 y=1686.0（P7 SVG 直线），**净空 13px**。说明：col3 末基线为 1667.95，1673.0 为流程游标（含末行余量），13px 按游标计成立。
  - P8-keys 流止 y=2514（底 2552）；P8-ex 流止 y=965（底 1332）。说明：P8 答案 4 列中前 3 列末基线最高 2536.4（37 题），墨迹约止 2542，距框底 2552 约 10px、距页脚带 2580 约 38px，无侵入；KIT“38px”按游标计，严格墨迹口径见本条（非阻塞澄清，见 §12）。
- 修复范围 round 4：
  - `transform.py` round 4 区仅含 1 处替换：徽章 `L’ÉDITION`（U+2019）→ `L'ÉDITION`（ASCII），无其他改动。
  - 终版 vs `baseline-round4.txt`（即 round 3 修复后状态）：**仅 P1 SVG 哈希变化**（`f1d854…`→`a5516115…`），P2–P8 SVG 哈希完全相同。说明：baseline 文件按“修复前状态”命名，round 3 文件的 P7（`afba4b5e…`）与 round 4 文件的 P7（`f4a80672…`）之差正是 round 3 词框修复；KIT §6“P2–P8 与 round-3 run 相同”的严格表述应为“与 baseline-round4（round 3 修复后状态）相同”（非阻塞措辞澄清，见 §12）。
  - 终版 SVG 哈希与 KIT §6 全量一致；PDF 哈希与 KIT §6 全量一致（baseline 文件中的 PDF 哈希不同是 round 5 重渲染的时间戳所致，SVG 才是稳定比较口径）。
- Round 3 词框修复真实消除（独立实测 + 像素佐证）：
  - P7 词框矩形 (1451, 1039.5, 434×274)，底边 1313.5；终版 gloss 末行 `du Panettone.`（基线 1309.02，fs 20）：含降部字符 0 个（g/j/p/q/y 均无），墨迹底 = 基线 1309.02，**净空 4.48px**。
  - 旧行降部墨迹底约 1314.0、擦框 0.5px 的说法与几何一致（基线 1309.02 + 约 5px 降部）。
  - 终版 P7 卡片词框裁图（`p7-parola-crop.png`）像素目视：末行与框底线间有清晰空隙，无接触。

## 5. P6 图表标签覆盖（重点口径复核）

- 构建员 scans.py 用的是 `PIL getbbox + anchor ls` 法；按 NL 族既定裁定，权威口径为**基线锚定墨迹法：`PIL getmetrics` 上升/下降量 + anchor ls**（墨迹框 = [x0, 基线−ascent, x0+advance, 基线+descent]）。校对以 getmetrics 法独立重测，并同时跑 getbbox 法对照：
  - getmetrics 法：P6 全部文本 vs 后绘矩形，**最大覆盖 0%，>0 项 0 个**；图表标签单列亦全部 0%。
  - getbbox 法：同样 **最大覆盖 0%，>0 项 0 个**。
  - 图表标签实测（基线 y / 两法覆盖）：Torino 1686.0、3° 1686.0、Milano 1724.0、4° 1724.0、Bologna 1762.0、5° 1762.0、Roma 1800.0、9° 1800.0、Napoli 1838.0、12° 1838.0，全部 0.00% / 0.00%。
- 裁定：构建员的 0% 结论在正确方法下成立（getmetrics 墨迹框比 getbbox 框更大，仍为 0，证据更强）；门限 <30% 通过。构建员的方法标注错误不构成阻塞，但须在本报告中记录两种口径实测值（已记录）。

## 6. gloss

- 渲染后 `gloss()` 串按 `·` 拆分（非 ` · `）：核心 24 = 本版 24，分布从核心独立实测 **P2 6 / P3 5 / P4 4 / P5 4 / P6 5**，与本版逐盒一致。
- 词头逐项一致：P2 `il cappotto, la sciarpa, i guanti, a strati, il termosifone, il crisantemo`；P3 `il panettone, il torrone, l'assaggio, la bancarella, il cantiere`；P4 `la giornata, la presentazione, gli spalti, la sera`；P5 `il cosplay, gratuito, il documentario, lo schermo`；P6 `la probabilità, la media, il modello, il bollettino, aggiornare`。
- 本版 gloss 前缀 `Note — `（P2–P6 全量），与 W43 一致；P1 桥接注用 `Notes :`（核心同结构，见 P1 卡片）。

## 7. 读者园地（协调员裁定已适用）

- 意大利语信件逐字保留（4 行，与核心同 y、同字号）：
  - `«Ciao! Sono Li, studio italiano a` / `Pechino. Lunedì metto il cappotto e` / `la sciarpa, sabato assaggio il` / `panettone — almeno in foto!» — Li`
  - 标签冻结：`(esempio della redazione)`（y=1550.62，与核心一致）。
- 法语披露句逐字摘录（3 行，同一注块）：
  - `Exemple de rédaction, pas une vraie lettre`（y=1611.15）
  - `: pas encore de lettres ni de meilleur texte`（y=1639.55）
  - `page 8, promis au VOL.3. Écrivez-nous !`（y=1667.95）
  - 3 事实齐全：①非真实来信（示例信）；②尚无真实来信；③尚无最佳 P8 作文；两者均承诺于 VOL.3。
- 显性邀请逐字：祈使句 **`Écrivez-nous !`**（注块末行）+ VOL.3 刊登承诺 `promis au VOL.3`。
- 协调员裁定适用说明：IT 核心 P7 上意大利语元素只有信件逐字 + `(esempio della redazione)` 标签 + 预告承诺，延期披露句本身在核心是中文（核心 3 行：`这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！`）；本版法语披露句即该中文披露的读者母语化，不以“无意大利语披露句”为由判 NOT PASS（IT×EN 同类阻塞项 B1 已据此裁定为非阻塞，IT×DE 同结构已上架）。
- 最佳 P8 作文覆盖范围裁定（PT/IT 族先例：W45 PT×IT 校对 §7——显性邀请 = 祈使句 + VOL.3 刊登承诺，**下期预告行不计入邀请**）：
  - 本版邀请门由**同一 3 行法语注块整体**满足：祈使句 `Écrivez-nous !` 在注块末行，承诺 `promis au VOL.3` 与两类对象（`lettres`、`meilleur texte page 8`）在注块前两行，行行相邻、同一注块，功能上等价于 PT×IT 邀请句内含承诺的情形。
  - 严格界定：裸 `Écrivez-nous !` 一句本身未点名任何一类对象，若无披露句的承诺与对象列举，最佳作文覆盖将不成立；本版成立靠的是注块整体，不是裸祈使句。
  - 预告行不计入邀请，仅作佐证：P7 底预告（意大利语，冻结）`Lunedì 9 novembre: chiude il Festival dei Popoli a Firenze. La Festa del Torrone continua a Cremona fino al 22 novembre. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!`——点名两类对象（真实来信 + P8 最佳文本），与披露承诺一致，但按先例不计入邀请门。
  - 零编造：无虚构读者、人名、引语；Li、Pechino 均为核心冻结的示例信内容。

## 8. 家具（与 W43 同配对实测对照）

| 家具 | W43 IT×FR 实测 | W45 IT×FR 实测 | 结论 |
|---|---|---|---|
| 徽章字符串 | `TEXTES EN ITALIEN · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`（撇号 0x27） | 同串逐字节一致（撇号 0x27） | 一致 ✓（round 4 的 ’→' 纠正已验证） |
| 徽章槽位/字号 | y=372、20pt、BRICK #a4553a、居中 x=975 | y=574、22pt、BRICK #a4553a、居中 x=975（text-anchor=middle） | 几何不同但合法，见下 |
| P1 y=372 槽 | 徽章占位 | 冻结意大利语标语 `IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA`（fs 19，与核心逐字节同） | 槽位被占，574 插入为唯一合法解 |
| 徽章墨迹净空 | — | 基线 574，墨迹底约 580；上方标语 372、下方 LA NOTIZIA 带 606，无交叠；审计 0 | 合格 ✓ |
| 徽章规则依据 | — | README #20 FR/IT 族规则：FR/IT 核心无空闲槽（y=372 为冻结正文标语）→ y=574、22pt BRICK 居中插入，与 W45 IT×EN 先例一致 | 符合族规则 ✓ |
| 版头行 | `JOURNAL ITALIEN · VOL.1 · …`（46pt） | `JOURNAL ITALIEN · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A`（46pt） | JOURNAL 短式一致，仅期号/主题随核心 ✓ |
| 页脚 | `La Lucerna · HEBDOMADAIRE ITALIEN VOL.1 · TEXTE EN ITALIEN · EXPLICATIONS EN FRANÇAIS` + `Page N sur 8` | 同式，VOL.1→VOL.2，8 页全量 | 一致 ✓ |
| gloss 前缀 | `Note — ` | `Note — ` | 一致 ✓ |
| P8 分隔符 | `— PAGINA n —`（意大利语） | `— PAGINA n —`（8 个全量） | 一致 ✓ |
| P8 答案体 | 破折号式 `N. key — note` | 破折号式（IT 族 dash-style，核心同体） | 一致 ✓ |
| 指令标签 | Compléter / Former une phrase / Vrai ou faux / Associer / Traduire en français / Traduire en italien / Écrire | 同套（卡片全量目视） | 一致 ✓ |
| 级别分布 | A2 46 / B1 71 / B2 33（校对重测 W43 本版，见下） | A2 47 / B1 70 / B2 33 | 差异核心驱动，见下 |
| P7 词 | `anteprima` | `l'assaggio` | 核心驱动（核心 P7 词即 l'assaggio） ✓ |
| CIFRE 框题 | fs 20（`LA SETTIMANA IN CIFRE · EN CHIFFRES`） | fs 20；实测墨迹 388.5px（23pt 时 446.8px），框宽 434、槽 412 | W43 先例实测核对一致 ✓ |

- 级别差异核心驱动证明：同一展开法重测 W45 IT 核心 = A2 47 / B1 70 / B2 33（逐页与本版完全相同）；重测 W43 IT×FR = A2 46 / B1 71 / B2 33，差异仅在 P2（W43 A2 16/B1 2，W45 A2 17/B1 1），即核心一题级别重定，非本版重分类。
- 修复轮 1 逐项核实（均为法语长度所迫的纯措辞收紧，无内容丢失）：
  - (a) P1 桥注：删 `la`/`le`、复数 `dégustations`→单数 `dégustation`，4 个 gloss 项全保留；
  - (b) cifre #2：括号 `(plus de 50 événements du Forum Cultura à Milan, du 3 au 8 novembre)`→`(50+ événements à Milan du 3 au 8 novembre)`，主行仍有 `il Forum Cultura, con più di 50` 与 `50+ — gli eventi del Forum Cultura di Milano`，Forum Cultura 未丢失；
  - (c) cifre 11ª 项法语 gloss 删 `ce week-end`（意大利语行保留 `del fine settimana`）+ 框题 tsize 23→20（W43 先例）；
  - (d) 日程副题 `Cette semaine`→`Semaine`（墨迹 436.2→387.8px ≤412px 槽）；
  - (e) 日程周注 `Dates selon les calendriers des événements ; les horaires peuvent changer.`→`Dates selon les calendriers ; horaires modifiables.`（墨迹 569.0→377.5px），“按日历/时间可变”两义全保留；
  - (f) P1 parola gloss 删 `le`（`le froid`→`froid`），避 row-B 规则线；
  - (g) P7 errori #2 `3e personne du singulier seulement`→`3e personne seulement`（删 `du singulier`；栏上文已立三单规则，属提醒性收紧，非阻塞）；
  - (h→round 3) P7 词框 gloss：round 1 `dégustation gratuite à la finale du Panettone`→`dégustation gratuite au Panettone`，round 3 →`finale du Panettone`（`gratuite` 让位于降部净空；词义 `dégustation` + 第 3 版/决赛指向全保留，免费细节在正文与 FRASI `assaggiare gratis / déguster gratuitement` 中仍在）；
  - (i) 读者注 5→3 行：旧版明示句 `pas encore de vraies lettres, pas encore de meilleur texte de la page 8 — les deux sont promis pour le VOL.3`→`pas encore de lettres ni de meilleur texte page 8, promis au VOL.3`，3 事实 + 承诺 + 祈使全保留。
- 修复轮 2：14 处 P8 注措辞收紧（3、22、122、24、41、50、56、57、58、83、84、87、90、135；其中 22/122 共用一串），key 均不在 keydiff 真重定向之列（58 为括号伪影，key 不变）；138/139 故意留 2 行（key/注已极简，不可再压）。

## 9. 图片

- 嵌入载荷与核心逐字节一致：P3 tartufo（base64 长 346864，sha 前缀 `9ea4244b…`）、P5 castagne（627056，`d6bc00b1…`），其余 6 页无嵌入照片（与核心一致）。
- 署名在版且与核心一致：P3 `Foto: Wikimedia Commons — dominio pubblico`、P5 `Foto: Wikimedia Commons — CC0`；P1 霜花绘图 `Disegno della redazione`、P2 时钟、P6 图表均为程序化图形（与核心一致）。
- 卡片目视：P3 松露照片、P5 栗子照片清晰完整，图说与署名无压盖。

## 10. ABSTRACT

- 全文（单行 + 末尾换行，ASCII 双引号 0 个）：
  - `La Lucerna, hebdomadaire pour apprendre l’italien en lisant : cette semaine, le premier froid, la commémoration du 2 novembre, la finale de la Coupe du Monde du Panettone à Milan les 7 et 8 novembre, la Festa del Torrone à Crémone et la Serie A, avec le mot l’assaggio, 150 exercices du niveau A2 au niveau B2 et leurs corrigés pour les lecteurs francophones qui apprennent l’italien par la lecture.`
- 核查：法语单行 ✓；无 ASCII `"` ✓（撇号为 U+2019，合法）；真实主题关键词：第一场寒冷、11 月 2 日追思、米兰潘妮托尼世界杯决赛 11 月 7–8 日、克雷莫纳牛轧糖节、意甲 ✓；学习者搜索短语：`apprendre l’italien en lisant` / `apprennent l’italien par la lecture` ✓；刊名 La Lucerna、目标语 italien、A2–B2 分级、150 题 ✓；事实均取本期内容，无模板套词。

## 11. 卡片目视、题量、范文、哈希

- 8 张卡片全部逐页目视：P1 徽章/版头行/头条/数字框/霜花图/快讯/闪电问答；P2 生活/追思日宽框/练习；P3 文化/松露照片/练习；P4 体育/赛程全宽表/练习；P5 青年/栗子照片/周计划/练习；P6 深读/图表/练习；P7 三级语言栏/易错诊所/词框/读者园地/金句/预告；P8 综合评估/写作/全部答案。结论：无溢出、无重叠、无压页脚、无缺图、无缺项。
- 题量与级别独立展开计数（题号节点 fs 24 + 同基线级别徽章配对，范围题 25–28、52–55、141–144 按徽章级别展开）：
  - 逐页：P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38，合计 **150**，编号 1–150 连续无缺重，全量配对、无未配对题。
  - 级别：**A2 47 / B1 70 / B2 33**，与任务给定数与 KIT 一致。
- 范文：P8 H 区范文 10 行与核心逐字一致，**81 词**（构建日志 `model words: 81` 佐证），在 80–100 词区间内；题面 `«La tua settimana del primo freddo» Scrivi 80–100 parole:` 与核心同串。
- 印刷 PDF 7,207,873 B、sha256 `5abb80f209355a3b43033b14008207b5f12e6305626551d6d216d9c78410af27`，8 页；web PDF 3,644,909 B（<10 MB）、sha256 `d154fc10ec78839453d34b2de7af57e5b8b4b3700683fdb4e83f803857b69f6a`，8 页；SVG 哈希与 KIT §6 全量一致。
- 校对前后哈希不变：核心 8 SVG 与本版 8 SVG + 2 PDF 在校对前/后逐字节哈希完全相同（`core-hashes-before/after.txt`、`edition-hashes-before/after.txt` diff 为空）。

## 12. 与构建员自述不符处（即使非阻塞）与非阻塞观察

1. **P6 测量方法标注错误（非阻塞，结论不变）**：构建员 scans.py 与 KIT §7 写的是 getbbox 法；按 NL 族裁定权威口径为 getmetrics 法。校对以 getmetrics 法重测仍为 0%，且 getbbox 法亦为 0%（§5）。方法错、结论对。
2. **KIT §4 “no 桥接 anywhere in delivered files”按字面不成立（非阻塞，非纸面缺陷）**：纸面 SVG 8 页与 ABSTRACT 的 `桥接` 确为 0，但 KIT §4 自身在否认句中含 `桥接` 1 次（“no 桥接 anywhere”）。建议主线在入仓时顺手改写该句措辞；不影响本版纸面结论，校对方未改动 KIT。
3. **KIT §6 round 措辞不精确（非阻塞）**：终版 P2–P8 与 baseline-round4（round 3 修复后状态）相同，而非与 baseline-round3 文件相同（后者 P7 仍为修复前哈希）；round 4 仅改 P1 的实质结论正确（§4）。
4. **KIT §7 P8-keys“38px 净空”口径说明（非阻塞）**：2514 为流程游标；严格墨迹口径下前列末基线 2536.4、墨迹约 2542，距框底约 10px、距页脚带约 38px，仍无侵入，审计 0。
5. **KIT §7 P7 col3 终值口径说明（非阻塞）**：1673.0 为流程游标，末基线 1667.95；距 FRASI 规则线 1686.0 的 13px 按游标计成立。
6. **核心 CJK 总数两种计数口径不同（非阻塞）**：freeze 工具报核心 193/179/169/145/215/149/319/1034，校对文本节点计数为 178/167/156/134/186/139/281/966；门禁值（新增 0、本版 0）在两种口径下一致，不影响结论。
7. **卡片缩略图上的法语撇号后“间隙”观感（已排除，非缺陷）**：SVG 文本中无 `' `（撇号+空格）节点；`l’article`、`d’avant-match`、`L’ITALIEN` 均为 U+2019 直连，间隙为小字号渲染观感。
8. **终版词框 gloss 删 `gratuite`（非阻塞，权衡合理）**：round 1 版含 `gratuite`，round 3 为降部净空改写后不再含该词；词义与第 3 版/决赛指向完整，免费细节在正文与金句中仍在。
9. **KIT §9 round 1 (c) 未单列的法语 gloss 收紧（非阻塞）**：cifre 11ª 项法语 gloss 删 `ce week-end`，意大利语行保留 `del fine settimana`，纯注侧收紧，无内容丢失。
10. **P7 errori #2 注删 `du singulier`（非阻塞）**：栏上文已立三单规则，提醒性收紧，未改变规则实质。
11. **P8 栏目基线细节（非阻塞）**：P8 答案列末基线分布见 §4，与流程游标口径不同但均在安全区内。

## 证据文件（本目录）

- `REPORT.md`（本报告）
- `core-hashes-before.txt` / `core-hashes-after.txt`（核心 8 SVG 校对前后哈希）
- `edition-hashes-before.txt` / `edition-hashes-after.txt`（本版 8 SVG + 2 PDF 校对前后哈希）
- `freeze-diff.json`（freeze.py diff 全量输出）
- `occlusion-ed.json` / `occlusion-core.json` / `occlusion-new.json`（几何审计三份输出，均为 0）
- `p8-extract-core.txt` / `p8-extract-ed.txt`（p8.py extract 输出，均为 150/150）
- `extract.py` / `extract-out.txt`、`checks2.py` / `checks2-out.txt`、`checks3.py`（校对脚本与输出）
- `p6_edge.py` / `p6_edge-out.txt`（P6 覆盖双口径 + 右缘 ADVANCE + 同基线行距扫描）
- `edition-alltext.txt` / `core-alltext.txt`（全版文本节点提取）
- `p7-parola-crop.png`（终版 P7 词框像素裁图，末行无降部接触框线）

## 阻塞项

无。结论：**ZERO PROBLEMS**。
