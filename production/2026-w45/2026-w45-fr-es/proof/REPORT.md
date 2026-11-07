# W45 FR×ES 独立校对报告 — 结论：ZERO PROBLEMS

- **对象**：W45 FR×ES（目标语言法语，读者母语西班牙语），刊头 Le Lucerna，VOL.3，刊期 2026 年 11 月 2–8 日，8 页。
- **交付目录**：`files/weekly-report-w45-fr-es/`（svg×8、cards×8、print PDF、web PDF、WEEKLY-KIT.md、ABSTRACT.txt）。
- **结论**：**ZERO PROBLEMS（可交付上架，阻塞项无）**。13 门全部独立重测通过；下文“非阻塞观察”仅为如实记录的措辞/口径说明，不构成阻塞项，不需修复即可上架。
- **校对员遵守**：未派生下级代理；未碰 `weekly-git`、未改核心/W43/交付目录、未改 `tools/` 下任何文件、未清理共享 scratch、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未宣布上架。
- **证据目录**：本报告同目录 `work/` 下（见文末证据清单）。

## 0. 开工查重与冻结快照（硬性）

- 进程检查（2026-10-28 04:53 UTC）：无任何进程 cwd 属于本版树（`fr-es`/`fr-core`）；当时唯一在途的另一代理任务是 ko-zh-tw 版，与本版无关。**不存在 genuinely in-progress 的写入，不 stand down。**
- 静默复查：交付最后写入为 04:52:20（WEEKLY-KIT.md），90 秒静默后复核交付哈希无变化，方可开工。
- 校对前快照 `work/snapshot-before.txt`（交付 + 核心全部文件 sha256）；校对后复核 `work/snapshot-after.txt`，**diff 为空：内容哈希全部不变**；交付文件 mtime 与开工时逐项相同（svg 04:43:06–07、cards 04:43:22–30、print PDF 04:43:46、web PDF 04:43:53、ABSTRACT 04:49:29、KIT 04:52:20），**无 mtime 刷新**。
- 操作禁令遵守：全部重跑均在自有 scratch（`work/scratch/`、`work/replay/`、`work/out-svg/`、`work/webcheck/`）内完成并重定向 OUT；从未在 build 树原地跑脚本，从未在交付/核心目录原地跑 build 树脚本。`tools/p8.py`、`tools/occlusion_audit.py`、`tools/freeze.py`、`tools/tables.py`、`tools/tables.json`、`hidden_files/w45/p8-fr-gap-fix/keycompare.py` 均以 sha256 验证与原版逐字节一致的 scratch 副本运行（p8 副本 sha `96fc2cfe…`、occlusion 副本 sha `e1f92b42…`、freeze 副本 sha `d9adfa48…`，与建造员 KIT 注明的工具版本一致）。keycompare 调用时显式 `--p8 <scratch 副本>`，不依赖原版路径。

## 对象实测值（建造员声称值全部视为待验证声称，本节为校对实测）

| 文件 | 字节数 | sha256（实测） |
|---|---|---|
| svg/p1-une.svg | 475,327 | `8f821595b01d90c83384078c1bddce478307dd9c86d109d6d80356fabb81f1ac` |
| svg/p2-vie.svg | 891,309 | `f9161ee2038aa85cb413a86cfd3c31bb82172c75e6c730efa84ef870edd018a8` |
| svg/p3-culture.svg | 220,831 | `dfcd8a045c9fef451dedccab76d6fd24839a754496af46c9ad1e18e52ddf9f67` |
| svg/p4-sport.svg | 33,077 | `dd58f4aca5224fe8750e8a322f8a8edd4d513da91a9d8e72ad6e29cb160ee66b` |
| svg/p5-jeunesse.svg | 26,855 | `49df19bb0c934d7999f1dfc8ca458538183ced6c76e606aa07dcf89a5ee5fc6f` |
| svg/p6-politique.svg | 28,889 | `9078e074730e28732f8cf347890fff0bc3dc6b1ac9bdacf43e0b24d41d63b4c2` |
| svg/p7-langue.svg | 30,332 | `a3c534f01492d20e3f4c166c0393e7a0e6ec75a1f72af98013bf66be4b9eed19` |
| svg/p8-exercices.svg | 49,176 | `077a336a73422b35bf30175fa0c00ff421e9b079f64ea728e41df26dded262cc` |
| cards/p1–p8.png | 1,037,545 / 1,184,413 / 931,705 / 843,501 / 692,141 / 740,506 / 722,000 / 1,019,342 | `9f8eeb7d…` / `c19f00a6…` / `57ba2746…` / `f92b6aa9…` / `2a333c59…` / `d87b4194…` / `320fb2f0…` / `5ddb881e…`（全值见 `work/snapshot-before.txt`） |
| Le-Lucerna-VOL3-ES.pdf（print） | 9,747,438 | `973d46380e1469750499ac3a6309b172b12ac50e858ccc8929ce7cb6f2a488ca` |
| Le-Lucerna-VOL3-ES-web.pdf（web） | 5,206,069 | `db79fb5c1c01746ebb84a184cc611c3bdeb2e24f23e4b8c014a5ec52ee35640b` |
| ABSTRACT.txt | 531 字节 / 524 字符（去尾换行后，见门 12） | `3ca65bb770840239c15b9211c25ae6fe6e6f33b14d9badd7cb65480e2461ee36` |

以上与建造员声称的字节数/sha 前缀全部一致。

## 门 1 — 冻结与法语核对串：通过

### 1a. 核心基线自有 scratch 重跑：8/8 逐字节

`freeze.py baseline`（scratch 副本，OUT 重定向至 `work/freeze-baseline/`，核心完整性前后复核）：

```
baseline: 8/8 SVGs byte-identical
OK p1 f02e628e… / p2 b192c192… / p3 5f332e9f… / p4 240f379d… /
   p5 a4d64e3e… / p6 47e4346d… / p7 e997123f… / p8 822dbe3d…
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```

### 1b. freeze diff：新增 CJK = 0，Han = 0，全角括号 = 0

`freeze.py diff`（scratch 副本，全量见 `work/freeze-diff-proof.json`、`work/gate1-freeze-analysis.txt`；下表“串数”为出现次数合计，JSON 仅列唯一串故条目数较少，两者合计一致）：

| 页 | +串 / −串 | 核心 CJK → 本版 CJK | 新增 CJK 字符 |
|---|---|---|---|
| P1 | +46 / −45 | 202 → 0 | 0 |
| P2 | +37 / −34 | 244 → 0 | 0 |
| P3 | +37 / −34 | 179 → 0 | 0 |
| P4 | +41 / −37 | 197 → 0 | 0 |
| P5 | +36 / −30 | 177 → 0 | 0 |
| P6 | +30 / −27 | 198 → 0 | 0 |
| P7 | +43 / −35 | 390 → 0 | 0 |
| P8 | +156 / −138 | 1030 → 0 | 0 |
| **合计** | — | — | **0** |

渲染 SVG 文本节点逐页复核：本版 8 页 Han 均为 0、全角括号均为 0；页脚 ES 串 8 页全 True、中文页脚全 False；“桥接”一词全版不出报（False）。

### 1c. 移除串逐项验证：P1 22 项、P8 33 项、P3/P7 各 1 项

- **P1 无 CJK 移除 22 项**（全量见证据文件）：全部为 5 段冻结法语头条段在 24pt 下的重排碎片，如 `Le Goût du Large », samedi 7 et`、`Masters, le dernier grand tournoi`、`ne connaît pas encore les finalistes` 等。词保留实测：对 22 项碎片做词多重集计数（81 个不同词、119 个词例），**本版 P1 文本中每个词的出现次数均 ≥ 移除碎片中的次数，缺失词 = 无**。另有独立旁证：transform 全量重放（门 3）证明头条段仅改字号/行高参数，文本字节未动。
- **P3、P7 无 CJK 移除各 1 项**：均为 `）。`（中文讲解段删除的残留标点），非法语。
- **P8 无 CJK 移除 33 项**（全量见证据文件）：区分为两类——(a) 电池段 20pt / 答案流 14.5pt 重排碎片（法语句子本身在本版重排后完整重现，键经门 2 全 150 核对无改动）；(b) E 区改向项：`Traduisez : « Lire un programme, c'est déjà` + `comprendre la France. »`（E1 题干翻转，法语句子原样保留于新西班牙语题干内）、`vacances depuis le 17 octobre.（être en vacances + depuis）`、`· 138. Ce soir, nous allons préparer nos cartables.（futur…`、`proche + préparer） · 139. On ne connaît pas encore les…` 等答案流重排 + 注记语言更换碎片。词保留实测：P8 移除碎片 126 个不同词、210 个词例中，**唯一缺失词为 `traduisez`（1 例）**——即 E1 指令动词本身由法语 `Traduisez` 翻转为西班牙语 `Traduce`，属已备案的改向；该指令所引入的法语句子 `Lire un programme, c'est déjà comprendre la France.` 在本版 P8 联合文本中完整在位。**无一法语目标词丢失。**
- 其余全部移除串均含 CJK（中文讲解层替换），非法语。

### 1d. 法语冻结串（建造员报告未明确提及，本校对补核，全部以核心 SVG 为准）

- **41e 形式**：本版 P4 联合文本含精确串 `41e édition en 2026 (40e anniversaire)`（跨两个文本节点：`41e édition en 2026 (40e` @ y=278.0 + `anniversaire). Dernier Masters 1000` @ y=308.53），与核心逐字节相同。全版 `40e` 子串出现次数：核心 1、本版 1（仅此一处）。保留项实测：生日语境 `anniversaire` 节点（P3、P4、P7、P8）均在位；编号 `40.`（P3）、`140–144.`/`140.`/`141.`/`144.`（P8）均在位；他版 `22e édition`（P1：`dimanche 8 novembre, 22e édition.`）、`15e`（P5：`c'est la 15e`、`15e édition`）均在位。**无 40e 误改。**
- **Q120**：题干节点（P8 电池，y=246.0）`Si j'étais libre dimanche, j'___ à Nanterre. A.`；选项节点（y=275.0）`irai · B. irais · C. vais`，即 A. irai / B. irais / C. vais；key 提取值核心 = B、本版 = B；P8 注记同步：本版 `120. B (si + imparfait → conditionnel présent; j' es je ante vocal (elisión))`，含 si + imparfait → conditionnel 与 elision j' 两要素。邻题 Q119（`Elle s'intéresse ___ festivals. A. à les · B. aux · C. des`，key B）与 Q121（`À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant`，key A）题干、选项、key 与核心逐字相同，**未动**。
- **P7 引用 #4**：P4 辩论框逐字 `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?`（含 ` : ` 前空格，P4 联合文本核实 True；无空格变体 False），P7 内同串在位；B1 同步题 key `plus excitante`（P7 表格 100 题 `La finale est ___ (excitante) !`，P8 key 100 = `plus excitante`）。
- **#8**：P5 逐字 `Les jeunes créateurs y rencontrent leur public, en vrai.` 在位；P7 诊所错误形 `✗ « Les jeunes créateurs y rencontre leur public, en vrai. »` 在位；Q106 key 核心 = 本版 = `Les jeunes créateurs y rencontrent leur public, en vrai.`。
- **P6 同步**：`Ce calendrier peut encore bouger.` 在 P6 与 P7 均在位。
- **任一法语串与核心不符即冻结失败——本门无不符。**

## 门 2 — P8 双门（FR 族硬性，两门缺一不可）：通过

### 2a. plain `tools/p8.py`（scratch 副本，sha `96fc2cfe…`，`--total 150`）

```
core: 97 noted / edition: 97 noted
status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[135, 150]
```

注记集逐项相等（97 项，与 KIT 所列集合一致）：[1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]。SHORT/UNCERTAIN 皆无；FR 核心只印 97 注记是设计，非缺陷。状态 ∈ {CLEAN, EXTRA_ONLY} 要求满足（实为 CLEAN）。

### 2b. `keycompare.py`（scratch 副本，复用 scratch 版 p8.py extract --json 输出）

```
core 150 keys / edition 150 keys
key-mismatches: 2 [135, 150]
  135: core='读一份日程，本身就是在了解法国。' edition='Leer un programa ya es entender Francia.' (core_noted=True, edition_noted=True)
  150: core='开放题' edition='Pregunta abierta' (core_noted=True, edition_noted=True)
```

**裸键错配 = 0**（全部 148 个非错配键逐字相等；错配仅 2 项且两侧均为 noted 项）。plain 单用对裸键篡改是盲的，本校对绝未只用 plain。

### 2c. 改向逐项从印刷行核实（非照抄 fr-de/fr-en）

- **E1（#135）法→西翻转**：电池印刷题干 `Traduce al español: « Lire un programme, c'est déjà comprendre la France. »`（y=1332.0）；key `Leer un programa ya es entender Francia.`；注 `lire un programme = leer un programa`。法语句子原样保留于题干内。
- **E2–E5 题干改为西班牙语、法语键不变**（keycompare 136–139 无错配）：136 `Traduce al francés: Corre más rápido que su hermano.` → key `Il court plus vite que son frère.`；137 `Traduce al francés: Los alumnos están de vacaciones desde el 17 de octubre.` → key `Les élèves sont en vacances depuis le 17 octobre.`；138 `Traduce al francés: Esta noche vamos a preparar nuestras mochilas.` → key `Ce soir, nous allons préparer nos cartables.`；139 `Traduce al francés: Todavía no se sabe quiénes son los finalistas.` → key `On ne connaît pas encore les finalistes.`（联合文本核实四句西班牙语题干全句在位；先前按单节点检索漏检 137/138 仅因题干跨节点换行，非缺失）。
- **#150 写作指南**：key `Pregunta abierta — los puntos están en el recuadro de escritura y el modelo, en el recuadro MODÈLE de esta página`，注 `se puntúa según los puntos`（REG 与印刷行一致）。

## 门 3 — gloss：通过

方法： programme 方法（README #21）：gloss() 调用串按 `·` 切分，Nota 前缀先去前缀再切分（否则每页多计 1 项假象）；`gloss_count.py` scratch 副本实测（`work/gate3-gloss.txt`），核心与本版逐页相等：

| 页 | gloss | Nota 类 | 词表 |
|---|---|---|---|
| P1 | 7 | 0 | 0 |
| P2 | 6 | 3 | 0 |
| P3 | 6 | 0 | 10 |
| P4 | 7 | 3 | 8 |
| P5 | 6 | 0 | 8 |
| P6 | 6 | 3 | 0 |
| P7 | 0 | 0 | 0 |
| P8 | 0 | 0 | 0 |
| **合计** | **38** | **9** | **26** |

- 口径声明：三类分项计数、**勿混算**——gloss 38 为 gloss() 项；Nota 类 9 为 bridge 项（P2 3 / P4 3 / P6 3）；词表 26 为 mots 列表项（P3 10 / P4 8 / P5 8）。渲染面 `Nota — ` 出现次数（P1 1 / P2 2 / P3 1 / P4 2 / P5 1 / P6 2）与 bridge 项数不同属正常（一条 Nota 行可含多项），不作混淆。
- P8 注纯西班牙语：P8 Han 0、全角括号 0；P8 无 `译注`/`HINWEIS`/`法语周报`/`桥接`/`（`/`）`；跨族残留 0。
- fix 轮改动在 transform.py 内：P1 gloss 单字化替换串在 transform.py 第 74 行（初译）与第 515–516 行（round-2 定稿 `se jouer decidirse · une finale final · une demi-finale semifinal · un quart de finale cuartos · une nocturne velada · un frisson emoción · la coquille Saint-Jacques vieira.`）在位；且 transform 单独重放（见门 1c / 下文重放）逐字节复现交付 SVG，证明全部 fix 改动均由 transform.py 单源头产生。
- **transform 单独复现（抽查结果）**：新鲜核心 build 拷贝 + transform.py（scratch 内）→ 计数 `340 → 354（round-2）→ 355（round-3）→ 359（round-4）`，与 KIT 声称的 359 项一致；OUT 仅重定向至 scratch `work/out-svg/`；重放 SVG 与交付 SVG **8/8 逐字节相同**；重放后 content 文件与交付 build 树 content 文件的差异仅为 5 处 OUT 重定向行。

## 门 4 — 金句、P7、登记、范文：通过

### 金句 8 句（联合文本计数：全 8 页渲染 SVG 文本节点拼接，核心 = 本版）

| # | 金句（逐字） | 页签 | 频次（核心 / 本版） |
|---|---|---|---|
| 1 | Le lundi 2 novembre, on reprend les cours. | p2 | 5 / 5 |
| 2 | On ne connaît pas encore les finalistes. | p1 | 3 / 3 |
| 3 | Les cimetières se sont remplis de chrysanthèmes. | p3 | 1 / 1 |
| 4 | Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? | p4 | 5 / 5 |
| 5 | Le festival se promène dans Paris. | p5 | 1 / 1 |
| 6 | Ce calendrier peut encore bouger. | p6 | 3 / 3 |
| 7 | Ce week-end, tout se joue. | p1 | 1 / 1 |
| 8 | Les jeunes créateurs y rencontrent leur public, en vrai. | p5 | 3 / 3 |

- P7 短语栏 8 句逐字出自本刊文章并带正确页签：P7 表格区实测 8 句均带 `(page N)` 且 N 与上表页签一一对应（#1 page 2、#2 page 1、#3 page 3、#4 page 4、#5 page 5、#6 page 6、#7 page 1、#8 page 5）。
- P7 内部频次（仅 P7 页）：核心 = 本版 = [4, 2, 1, 4, 1, 2, 1, 1]（#1–#8 顺序）。P7 “2×”指原文 + P7 表格对：教学栏/工具箱重复（#1/#2/#4/#6 在 P7 内多次出现）是 KIT 设计，与核心频次结构完全相同，**非缺陷**。
- P7 词框定义句冻结：P7 y<1200 区域核心 vs 本版节点差集仅为栏头（NIVEAU/BOÎTE/LANGUE EN MAIN 西班牙语形）、工具箱说明段（西班牙语 vs 中文讲解）与金句栏副标；全部法语定义句、例句、语法句逐字未动，**仅 gloss/讲解本地化**。

### 登记（scratch REG dump，`work/reg-dump.txt` / `reg-dump.json`）

- 总题 **150**，连续编号 1–150（sequential True）；页分布 **10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**（P1–P8；P2=15、P5=17、P8=42，与 KIT 一致，通用串对 FR 是错的）。
- 级别：**A2 53 / B1 75 / B2 22**。
- 题型（西班牙语登记标签，合计 150）：Completar 49、Opción múltiple 26、Reescribir 7、Emparejar 21、Verdadero/Falso 5、Leer gráfico 6、Practicar 8、Corregir 4、Completar texto 8、Comprensión 5、Traducir 5、Completar diálogo 5、Escribir 1。
- 范文（P8 MODÈLE，空格切分）：核心与本版 7 行文本逐字相同，**86 词**（实测）。

## 门 5 — 几何：通过

### canonical `tools/occlusion_audit.py`（scratch 副本）

```
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
edition: 0 flags / core: 0 flags; NEW vs core: 0
```

本版 / 核心 / NEW **全 0**（`work/occlusion-proof.json` 与建造员 r4 结果一致；r4 前版 4 项 NEW BOXTITLE 已修复，复测为 0）。

### 补充扫描（`scans.py` scratch 副本，`work/gate5-scans.txt`）

- **全页右缘 ADVANCE 扫描（限 1885）**：仅 P8 F 配对右侧 3 行超限，b/d/e 的 x1 = **1891.2 / 1891.3 / 1899.5**，与建造员声称一致；核心同文同 x 同 x1（核心 y = 940.0 / 1016.0 / 1054.0，本版 y = 1036.0 / 1112.0 / 1150.0，y 不同只因电池流位置不同），**属冻结法语继承**，且 3 值均在内框线 1910 以内。
- **框线扫描**：0 命中（无框线切字）；**同基线行检查**（P1 顶栏 y=92、徽记 y=574、各页页脚 y=2624）：0 重叠。
- **P6 标签覆盖（基线锚定墨迹法，getmetrics）**：**0.0% < 30%**，通过。
- **行首孤儿标点**：4 项行首 `:`，与核心同页同 y 同文本逐字节相同（P3 y=789.65、P4 y=837.12、P5 y=430.65、P7 y=428.1），属冻结法语换行继承；西班牙语自有行首违规 0。行末连字符扫描为建造员 KIT 声称值（0），本校对未将其列为门 5 必测项（门 5 必测为 canonical 审计 + 右缘 ADVANCE + 框线 + 同基线 + P6 覆盖，均已独立重测）；canonical 墨迹审计对切词溢出同样敏感，且右缘扫描仅 3 项继承值，故不影响几何结论。
- **流光标继承值**：重放日志实测 P1-hiver 终 2298、P6-ex 终 2557，与建造员声称一致；卡片目视（见下）P1 hiver 块与 P6 习题末行均距页脚有明显空隙，**无压线、无溢出**。
- **卡片目视（8 张全查）**：P1 徽记/Atget 图/quiz 末端、P2 ET VOUS 框底、P3 Blanco 图、P4 41e 框与辩论框、P5 PARIS CREATOR WEEK 单名框、P6 日历表与习题末端、P7 读者园地框与预告暗带、P8 电池/写作条/答案末端，**全部干净，无溢出、无重叠、无压页脚**。

## 门 6 — P8 流末端口径裁决（重点）：通过（adjudicate：过）

口径声明：本校对墨迹底口径 = 文本节点最大基线 + 该节点字号下 PIL `getmetrics` descent（与建造员数值可逐项复算，见 `work/gate-ink.txt`）。

| 口径 | 本版实测 | 核心同口径实测 | 对照 |
|---|---|---|---|
| 电池流末基线（Merci!） | 1446.4（20pt，descent 6） | —（核心电池流布局不同，不作同值要求） | — |
| 电池流墨迹底 | **1452.4** | — | 距写作条规则线 1526：墨迹隙 73.6px（基线隙 79.6px）；距 MODÈLE 顶 1540：墨迹隙 87.6px |
| 答案流最大基线 | **2539.18**（14.5pt，descent 5） | **2539.19**（15.5pt，descent 5） | 基线差 0.01（SVG 坐标舍入量级） |
| 答案流墨迹底 | **2544.2** | **2544.2** | **逐值相同** |
| 距页脚规则线 2580 | **35.8px** | **35.8px** | 相同 |
| 距页脚基线 2624 | 79.8px | 79.8px | 相同 |
| canonical FOOTER 旗标 | **0**（occlusion 总旗标 0，含 FOOTER 类） | 0 | — |

裁决（沿 fr-de 前例）：墨迹底 2544.2 超出名义 2540 仅 4.2px，但 **2540 不是 canonical 审计限值**（canonical 审计的页脚带规则为 y=2580，页脚基线 2624 豁免在外；bslib4 的 CONTENT_BOTTOM=2540 仅为流 nominal）；本版与核心同口径三值（最大基线、墨迹底、页脚间隙）实质相同、FOOTER 旗标为 0、卡片目视答案末端距页脚有空隙。**口径一致 + 无页脚压线 + FOOTER 0，裁决为过。** 不得只写“与核心同值”——上表即为完整对照。

## 门 7 — P7 几何：通过

- **预告墨迹底**：本版预告末基线 **2494.0**（20pt，descent 6）→ 墨迹底 **2500.0 < 2540**，与建造员声称一致；预告暗带 rect 实测 (989, 2270, 896×270)，底 = **2540**，预告文本全部位于暗带内。
- **读者框墨迹底**：读者园地框 rect 实测 (989, 1878, 896×380)，框底 = **2258**；框区最大基线 **2235.825**（22.5pt 诊所句末行，descent 7）→ 墨迹底 **2242.8 < 框底 2258，余 15.2px**；披露 2 行（y=2206.0 / 2233.3，x=1013）在框内（框 x 989–1885）。金句规则线间隙：P7 短语栏终 1574（限 1830）、诊所终 2140（限 2268），均见重放日志，无压线。
- 卡片目视：披露 2 行在框内距框底有空隙；预告暗带内西班牙语 2 行距带底与页脚均有空隙。

## 门 8 — 读者来信角：通过

逐字摘录（P7，x=1013 栏，`work/gate-reader.txt`）：

- **编辑示例标注**：法语示例段逐字保留（y=1956.0 / 1985.82 / 2015.64）：`« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)`，与核心逐字相同。
- **西班牙语点评**：`Comentario de Xiao Mo (ejemplo): el passé composé es seguro; el punto y coma une ambos días. El próximo rincón comentará textos reales.`
- **披露（2 行，177 字，实测）**：`Nota de la redacción: ningún texto del VOL.2 llegó a tiempo (no hubo W44); aquí un ejemplo. El VOL.4 comentará textos reales. ¡Envíanos tu carta o tu mejor texto de la página 8!`——字符数（单空格归一化后）**177**，与 KIT 字符串逐字相等。
- **征集句字面覆盖裁决**：`¡Envíanos tu carta o tu mejor texto de la página 8!` 字面同时含 `carta`（来信）与 `mejor texto de la página 8`（最佳 P8 文本），**双覆盖成立**。
- **披露 3 事实 + VOL.4 承诺齐全**：事实 (1) ningún texto del VOL.2 llegó a tiempo；(2) no hubo W44；(3) aquí un ejemplo（本期登的是标注示例而非读者来信）；承诺：El VOL.4 comentará textos reales。法语冻结披露句同页在位（`Note de la rédaction : aucun texte du VOL.2 n'était arrivé… Le VOL.4 reprendra la promesse.`）。
- **P8 写作 VOL.4 指向**：法语 `Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »).`；西班牙语 `Los mejores textos aparecerán en el VOL.4 (página 7, « Le courrier des lecteurs »).`——双语一致。
- **预告行**：`La semana que viene: … ¡y por fin vuestras cartas!` 在位，**不计作征集**（征集成立不依赖预告行）。
- **卷期一致性**：FR 核心是 VOL.3，下期为 VOL.4；披露、征集、P8 写作、P7 预告栏头（`LA SEMAINE PROCHAINE · VOL.4 LA SEMANA QUE VIENE`）四处 VOL.4 指向一致。

## 门 9 — 家具三方对照（核心 / W43 / 本版）：通过（附两项非阻塞说明）

- **徽章**：本版 = W43 逐项相同：(975, 574)、22pt、粗体、#a4553a、居中，串 `TEXTOS EN FRANCÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`（W43 同串同坐标同字号同颜色）；核心徽章同坐标/字号/颜色，仅串为中文（本地化所致）。符合 FR-as-target 一般形（fr-de/fr-en 实测 (975,574) 22pt #a4553a = W43）。
- **页脚**：本版 8 页左 `Le Lucerna · SEMANARIO FRANCÉS VOL.3 · TEXTO EN FRANCÉS · EXPLICACIONES EN ESPAÑOL`（65, 2624，20pt，#57523f，start）、右 `Página N de 8`（1885, 2624，20pt，end），与 W43 形式逐项相同，**唯一差别为 VOL.2→VOL.3（预期卷期更新）**。
- **副标槽**：P1 顶栏中串 = W43 逐字相同（`HEBDOMADAIRE EN FRANÇAIS · CADA SEMANA · EL FRANCÉS QUE LEEN LOS FRANCESES`，(975,92)，21pt）；左 `VOL. 3 · N.º 3`（卷期更新）；右日期为核心刊期（`SEMAINE DU 2 AU 8 NOVEMBRE 2026`）；刊头 `Le Lucerna` 三方一致（(975,262)，178pt UnifrakturMaguntia）；副标题西班牙语形 + VOL.3 + 本期主题（预期更新）。
- **规则线**：P1 金线 (65,112)–(1885,112) #b3a06a、双暗线 y=392/401，三方一致；页框 rect (28,28,1894×2644) 与 (40,40,1870×2620)、底色 #f7f1e2，三方一致。
- **栏头**：P7 栏头 = W43 形（`LANGUE EN MAIN · LA LENGUA EN MANO`、`NIVEAU A2 · NIVEL BÁSICO`、`NIVEAU B1 · NIVEL INTERMEDIO`、`BOÎTE À OUTILS · RECURSOS`、`LES PHRASES DE LA SEMAINE · FRASES DE LA SEMANA`、`CLINIQUE DES ERREURS · CLÍNICA`、`LE COURRIER DES LECTEURS · EL RINCÓN DE LOS LECTORES`，坐标/字号与 W43 相同；预告栏头 VOL.4 为卷期更新，y=2316 继承核心布局）；P8 栏头 = W43 形（A COMPLETAR、B OPCIONES、C LECTURA、D CONSTRUIR FRASES、E TRADUCCIÓN、F VOCABULARIO、G DIÁLOGO、MODÈLE · MODELO、RÉPONSES 西班牙语形；栏头 y 坐标为流位置决定，与 W43 的 y 差属正常流位移，串/形一致）。
- **非阻塞说明 1（暗带几何）**：P7 预告暗带 rect 本版 = 核心 (989, 2270, 896×270)，≠ W43 (989, 2202, 896×338)。此为**继承核心几何**（本期读者框底为 2258，暗带必须位于其下），非本版偏差；暗带串/色/形符合 W43 形。不阻塞。
- **非阻塞说明 2（P8 H 栏头一词）**：本版 `H · ÉCRITURE · ESCRIBIR`，W43 实测为 `H · ÉCRITURE · ESCRITURA`。ESCRIBIR（动词“写”）与 ESCRITURA（名词“写作”）同义，且与本版登记类型标签 `Escribir`（#150）一致；KIT 称“写作栏 ESCRIBIR”为本版自有形式，其“W43 形”表述对该词不精确，特此记录。**措辞同义、无内容影响，不阻塞。**

## 门 10 — 图片 payload = 核心：通过（全值实测）

3 张均有 `<image>` 元素 + 法语图说 + credit 行，卡片目视全部确认。

| 页 | 放置 (x, y, w×h) | base64 文本 sha256（全值） | 解码 JPEG sha256（全值） | 字节数 |
|---|---|---|---|---|
| P1 Atget | (65, 1874, 896×320) | `ff20bc2bd2654cdc075f7e09bcb5a96622650c7cb5921fe07384703067fa8e5d` | `f3705af28f175ce48d8abad95944accb7aacc45d6a8a50c47b24af5c5144595f` | 334,674 |
| P2 Hiroshige / LACMA | (1451, 200, 434×480) | `6918cb8bbe4b4bec2d6dd9bafb1636901ed2a46f9df8e49566749e404d1664ae` | `5b772facb5db886c18fa96c05b9c8fb1a459eaaff931a4a8c121896edf970ee2` | 646,242 |
| P3 Blanco《Flora de Filipinas》 | (1451, 200, 434×540) | `bfaadf5b6b912416f770c1bf579c3467e47c662efd130b5656292bb86171eca9` | `be071fdae81a71b48d76383bd33147371968f44e37eef4312102d52dea6d0c94` | 142,340 |

- 双口径（base64 文本哈希与解码 JPEG 哈希）**核心 = 本版逐项相等**；解码值同时等于 build 资产文件字节（atget-paris.jpg / hiroshige-maple.jpg / chrysanthemum-blanco.jpg，sha 与上表解码值相同），JPEG 魔数 `\xff\xd8\xff`。
- 其余 5 页（P4–P8）核心与本版均无内嵌图片（0 张）。
- credit 行（Artist 原文，核心 = 本版逐字相同，已放置）：P1 `Eugène Atget (1857-1927), photographie, domaine public`（y=2271.3）；P2 `Utagawa Hiroshige (1797-1858), estampe, domaine public ·` + `LACMA`（y=757.3 / 777.45）；P3 `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle,` + `domaine public`（y=842.95 / 863.1）。

## 门 11 — 网页版 PDF：通过（新鲜性独立证实，无噪声页）

- **页数/规格**：web PDF 8 页、936×1296 pts；print PDF 8 页、1462.5×2025 pts。web PDF 每页 1 个 1950×2700 JPEG 流（baseline DCT），pdfimages 列表尺寸 p1 657K / p2 638K / p3 584K / p4 631K / p5 527K / p6 560K / p7 644K / p8 839K；提取流字节数 p1 673,229 / p2 652,839 / p3 597,984 / p4 645,873 / p5 539,714 / p6 573,655 / p7 659,185 / p8 859,150，与建造员声称一致。
- **新鲜性证明（本校对独立重建，非照抄建造员候选）**：以 render.py 配方（Pillow 默认质量，不传 quality 参数，optimize=True，中转 JPEG 再入 PDF）在 scratch 内从**交付卡片**重建候选 PDF（`work/webcheck/Le-Lucerna-VOL3-ES-web.pdf`，同名输出）——8 页 JPEG 流与交付 web PDF 流**逐字节相同**；两文件同为 5,206,069 字节，**仅差 8 字节，全部位于 CreationDate/ModDate 时间戳**（交付 20261028044352Z vs 重建 20261028050316Z）。建造员声称的“仅差 26 字节标题元数据”源于其候选文件异名（标题含文件名）；本校对同名重建下标题亦相同，故只剩时间戳差。**交付 web PDF 确为从本版卡片新鲜生成，fr-en 式旧噪声版问题不存在。**
- **逐页渲染比对（pdftoppm -r 150，1950×2700，与卡片比对）**：195×270 下采样均值差本校对实测 p1 1.586 / p2 1.456 / p3 1.376 / p4 1.407 / p5 1.264 / p6 1.333 / p7 1.522 / p8 1.623（建造员值 1.511 / 1.378 / 1.310 / 1.340 / 1.216 / 1.273 / 1.444 / 1.572；约 0.05–0.08 的系统差为下采样滤波方法差，量级一致）；下采样最大单点差 17–26（JPEG 边缘伪影量级）。**个位数均值差，无红黄绿蓝块噪声页。** 四分之一分辨率均值差 2.458–3.640，同样为 JPEG 压缩量级。
- **质量参数结论（不阻塞）**：交付流确为卡片经 Pillow 默认质量配方编码（全配方重建流逐字节相同为证）。本环境 Pillow 默认值的数值验证：单步编码中默认（不传 quality）与 quality=75 字节完全相同（634,481 B），quality=72 则不同（602,231 B），故默认 = q75；q72/q75 数值争议本身按任务要求**不判阻塞**，且本版实测支持默认/q75 配方。

## 门 12 — ABSTRACT：通过（附一处口径说明）

- **形式**：西班牙语单行（splitlines = 1）、无 ASCII 双引号（0 个）、去尾换行后 **524 字符**（文件 531 字节含尾换行；解码含换行 525 字符），与建造员声称的 524 字符一致。
- **全文**：`Le Lucerna VOL.3, semana del 2 al 8 de noviembre de 2026: semanario en francés para lectores hispanohablantes — fin de semana de finales con el Rolex Paris Masters en Nanterre, Peur sur le Parc en Plailly y Le Goût du Large en Port-en-Bessin, vuelta al cole el 2 de noviembre, Halloween y Toussaint, Pitchfork Paris y el presupuesto 2027 en la Asamblea Nacional, con 150 ejercicios de A2 a B2, vocabulario, gramática y texto modelo. Aprender francés leyendo noticias reales: finales, horario de invierno y fiestas francesas.`
- **关键词刊内出处（逐项核对刊内页）**：Rolex Paris Masters → P1、P4；Nanterre → P1、P4、P5、P8；Peur sur le Parc → P1、P3；Plailly → P1、P3、P8；Le Goût du Large → P1、P8；Port-en-Bessin → P1、P8；vuelta al cole / 2 de noviembre → P2（`Lunes 2 de noviembre · la rentrée`、`vuelta al cole`）及 P1/P3/P5/P7/P8；Halloween → P1、P2、P3、P8；Toussaint → P1、P2、P3、P8；Pitchfork Paris → P1、P5；presupuesto 2027 → P1（`budget 2027`）、P6、P8；Asamblea Nacional → P8（`La Asamblea Nacional examina el presupuesto`）及 P1/P2/P6/P7 的 `Assemblée`；150 ejercicios de A2 a B2 → 登记实测 150 题、A2 53 / B1 75 / B2 22（门 4）。
- **口径说明（非阻塞）**：结尾概括语 `horario de invierno` 的精确西班牙语双词未以印刷文本出现在 SVG 中——它仅见于 REG #20 的注记（`El horario de invierno empezó el 25 de octubre`；#20 为裸键，按 FR 注记集设计不印刷），而其法语主题 `l'heure d'hiver` 印刷在位（P1 y=1947.5 `La France est passée à l'heure d'hiver`、P2 y=1129.25/1214.12，起自 10 月 25 日星期日）；`fiestas francesas` 为对刊内 Halloween / Toussaint / 节庆主题的概括语；末句 `Aprender francés leyendo noticias reales` 为学习者搜索短语（按设计即为 ABSTRACT 自有表述，非刊内引文）。**无新增事实主张**（冬令时自 10 月 25 日起为核心法语文本事实）。

## 门 13 — 核心事实债与本版新增主张：通过

- **本版新增主张 = 0**：对 freeze 新增串中全部含数字串逐项审查（`work/gate-newclaims.txt`）——所含日期/数字均为：法语目标文本重排碎片、核心注记的西班牙语翻译、家具（VOL.3、Página N、PLAN SEMANAL 2–8 日）、读者角披露与 VOL.4 指向（编辑承诺，继承核心 VOL.4 承诺）、P8 注记翻译的核心事实（10 月 23 日社保收入 115–1 否决、参议院自 11 月 9 日起、第 15 届 Pitchfork、11 月 3–6 日预算使命日程等，均见 KIT §2 与核心文本）。无一新增世界事实。
- **核心事实债只继承、不判本版阻塞**：本校对未发现需转交核心的新事实债；核心文本事实（如 2027 预算日程标注为“预定、无结果”）均按核心原样继承。

## 非阻塞观察汇总（明确不阻塞上架）

1. P8 H 栏头一词：本版 ESCRIBIR vs W43 ESCRITURA（同义，见门 9 说明 2）。
2. P7 预告暗带几何继承核心（989, 2270, 896×270）≠ W43（见门 9 说明 1）。
3. ABSTRACT 结尾概括语口径（见门 12 说明）：主题均有刊内出处，精确西班牙语双词 `horario de invierno` 仅见于裸键注记。
4. 网页版质量数值：默认 = q75（见门 11），q72/q75 之争本身不阻塞。
5. 继承值（卡片目视均干净）：P8 F 行右缘 1891.2/1891.3/1899.5、行首 `:` 4 项、P1 hiver 流光标 2298、P6 习题流光标 2557、P8 墨迹底 2544.2——全部为核心继承或与核心同口径同值，已在各门中 adjudicate。

## 修复指引

无。阻塞项为 0，无需修复。

## 证据清单（`hidden_files/w45/fr-es-proof/work/`）

- `snapshot-before.txt`、`snapshot-after.txt`（交付 + 核心哈希快照与复核，diff 为空）
- `gate1-baseline.txt`（freeze 基线 8/8）、`freeze-diff-proof.json`、`gate1-freeze-analysis.txt`（P1 22 / P8 33 / P3·P7 各 1 移除串全量）
- `gate2-plain.txt`、`p8-plain-proof.json`、`gate2-keycompare.txt`、`keycompare-proof.json`、`p8-core-extract.json`、`p8-ed-extract.json`
- `replay-transform.log`（340→354→355→359）、`replay-run.log`、`replay-compare.txt`（重放 8/8 逐字节）、`replay-vs-build.diff`（仅 OUT 行差）、`reg-dump.txt`、`reg-dump.json`
- `gate-text-analysis.txt`（Han/页脚/41e/Q120/金句/P7 页签）、`gate-followup1.txt`（41e 全串、Q120 注记全段、P7 表格区）、`gate-wordpreserve.txt`、`gate-p8e.txt`（E 区印刷行）
- `gate3-gloss.txt`、`gate3-notes.txt`、`gate-model.txt`
- `gate5-occlusion.txt`、`occlusion-proof.json`、`gate5-scans.txt`、`gate-ink.txt`（P8/P7 墨迹口径实测）
- `gate-furniture.txt`、`gate-furniture2.txt`、`gate-furniture3.txt`（徽章/页脚/栏头/暗带三方对照）
- `gate-images.txt`（图片双口径全值哈希、credit 行、资产对照）
- `gate-reader.txt`（读者角逐字摘录、177 字、VOL.4 指向）
- `gate-abstract.txt`（ABSTRACT 524 字、关键词刊内页）
- `gate-web-compare.txt`、`gate-web-q.txt`、`webcheck/`（候选 PDF、交付/候选 JPEG 流、渲染比对）、`webcheck-render.log`
- `gate-newclaims.txt`（新增主张扫描）、`core-vs-edition-build.diff`（核心与本版 build 树差）
- `scratch/`（工具与 keycompare 的 sha 验证副本、build 副本）、`replay/`（transform 重放树）、`out-svg/`（重放 SVG，8/8 = 交付）
