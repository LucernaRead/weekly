# 独立校对报告 — Lucerna Weekly W45 · IT × RU（意大利语 × 俄语）

**结论：ZERO PROBLEMS** — 12 门禁全部通过，无编号阻塞项。
本报告为从头独立重测（未采信构建员自述代替重测；凡构建员自述与实测不符处，即使非阻塞，也列入第 13 节）。

- **待审版**：`files/weekly-report-w45-it-ru/`（svg × 8、cards × 8、print PDF、web PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- **对照核心**（只读）：`files/weekly-report-w45-it-core/`；W43 同配对对照（只读）：`files/weekly-report-it-ru/`
- **校对约束遵守**：未改源码、未宣布上架、未派生下级代理、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未清理共享 scratch 目录。
- **开工查重**：开工时 `files/weekly-report-w45-it-ru/` 与构建树 90 秒复查零新写盘，安全开工。在跑的 `render.py` 进程经查属于 IT×KO 构建树（cwd `hidden_files/weekly-report-w45-it-ko-build`），与本版无关。
- **校对前后哈希**：交付物（2 PDF + 8 SVG + 8 PNG）与核心 8 SVG 校对前后 sha256 全部不变（`scratch/deliver-core-hashes-before.txt` vs `…-after.txt`，仅路径写法不同，哈希值逐项一致）。

## 0. 交付物核验（与 KIT §15 逐项比对）

| 文件 | 字节 | sha256（实测） | 与 KIT 一致 |
|---|---|---|---|
| `La-Lucerna-VOL2-RU.pdf`（print） | 7,094,801 | `4de5a0668e071dff344a68edba8cf5c6b0df56b5ab740b043273385459826b04` | ✓ |
| `La-Lucerna-VOL2-RU-web.pdf`（web） | 3,655,383 | `59ce56805a236fbacc900d146dba42cf0dd8d36dff141842fae4cd9600e914c9` | ✓ |
| svg × 8、cards × 8 | — | 16 个哈希全部与 KIT §15 逐项一致（见 `scratch/deliver-core-hashes-before.txt`） | ✓ |
| print PDF | 8 页，mediabox 1462.5 × 2025；web PDF 8 页，mediabox 1400 × 1938 | pypdf 逐页提取 print：4239/4220/3623/3635/3562/4244/3827/11322 字；P1 徽章与页脚提取确认 | ✓ |

## 1. 冻结门

- **基线复现**：`tools/freeze.py baseline --build hidden_files/weekly-report-w45-it-build`（核心构建树）
  → **8/8 逐字节复现**（p1 `81051bbb…`、p2 `d42ce9ae…`、p3 `9e45586d…`、p4 `62f75269…`、p5 `c907b869…`、p6 `5545f8dd…`、p7 `9fc999f4…`、p8 `3b87e54f…`），且运行后核心 8 SVG 重哈希不变。
  （方法注：第一次误指构建树为 RU fan-out 目录，得 0/8——那是复现了 fan-out 本身，不是核心；改指核心构建树后 8/8。此为校对过程注记，非交付问题。）
- **冻结差分**（`tools/freeze.py diff` 独立重跑，`freeze-diff-proof.json/.txt`）：与 KIT §2 表格逐项一致（多重集计数）：
  p1 +27/−26、p2 +35/−29、p3 +34/−31、p4 +29/−25、p5 +46/−35、p6 +31/−24、p7 +44/−41、p8 +175/−174；**新增 CJK 8 页均为 0**（核心 CJK 总量 193/179/169/145/215/149/319/1034 → 版内 0）。
- **全文 桥接**：8 SVG + KIT + ABSTRACT + 两 PDF 二进制检索 `桥接` 均为 0；`bridge`（不区分大小写）8 SVG 均为 0。
- **意大利语正文冻结**：删除串逐项裁定（distinct 串清单，见 `freeze-diff-proof.json`）——
  - p1–p5 删除串全部含 CJK（讲解层），非 CJK 删除 = 0；
  - p6 唯一非 CJK 删除 `bollettino · modello`：换行碎片，两词头均在版内 gloss 串现身（`il modello = прогностическая модель · il bollettino = сводка погоды`），内容未丢；
  - p7 唯一非 CJK 删除 `è probabile che / è possibile che / bisogna`：换行碎片，该句仍为 P7 B2 栏意大利语正文（`Con «è probabile che», «è possibile che» e «bisogna che»…`），内容未丢；
  - p8 非 CJK 删除 15 项 = 7 条全角标点形式行（103、17、18、19、20、60、61，key 逐字相同，仅 `：`→`:` / `（）`→`()`，见 §3）+ `— PAGINA N —` × 8；
  - `— PAGINA N —` × 8 被 `— СТРАНИЦА N —` × 8 替换：W43 已上架版 P8 实测已是 `— СТРАНИЦА` 式 8/8、`— PAGINA` 式 0/8（见 §9），替换符合 W43 同配对先例。
  - **结论：无意大利语正文串被删除；讲解层全部为俄语**（版内 CJK = 0，俄语讲解层逐页现身）。

## 2. P7 词框硬性门 — 通过

- 定义句 4 个节点核心与版内**逐字、逐坐标一致**（x=1473；y=1128.5/1159.03/1189.56/1220.09）：
  `« l'assaggio » è la prova di un cibo:` / `un piccolo pezzo per decidere se` / `piace. Questa settimana vive a` / `pagina 3, alla finale del Panettone.`
  **定义句未本地化。**
- 仅 gloss 本地化为俄语，终版 1 行（y=1280.62）：`assaggio = дегустация (стр. 3).` 与构建员自述逐字一致。
- P7 全部 `«…»` 起首节点核心与版内一致（词框、诊所 4 条、信件、金句 8 句位置与文本均同）。
- 金句：空白归一化全刊 joined-stream 计数，8 句核心与版内**均为 2×**（1×正文 + 1× P7）：
  `arriva il primo freddo vero della stagione`、`Non è una certezza, è una probabilità`、`il 2 novembre è la Commemorazione dei defunti`、
  `Fa freddo, copriti bene!`（该句正文出现亦带引号，故 quoted 2×，其余 7 句 quoted 1×）、`il pubblico può assaggiare gratis`、
  `il calcio non si ferma per il primo freddo`、`la cultura continua`、`Una probabilità alta non è una certezza`。
- 金句标签：版内 P7 节点顺序实测 **(Страница 1, 1, 2, 2, 3, 4, 5, 6)**，与核心标签页码序列（核心用 `(Pagina N)` 形式，同一序列）一致。

## 3. P8 门 — 通过

- `tools/p8.py compare`（显式核心/版内 P8 路径，total 150）独立重跑：
  **CLEAN — 150 noted = 150 noted，missing=[]，extra_count=0，uncertain=[]，keydiff=[6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 102, 137, 138, 139]**，与构建员自述集合逐项一致。
- keydiff 15 项逐项印刷行对照（`p8-core.json` / `p8-ed.json` 提取的完整 seg，方法：p8.py `extract`）：
  - 12 项伪影（6、13、14、15、16、20、38、58、71、74、77、102）：**首词答案词头与核心逐字相同**
    （`previsioni`、`guanti`、`crisantemi`、`termosifoni`、`fa`、`resta`、`mandorle`、`più bella`、`gratuiti`、`castagne`、`ci sarà`、`fa`）。
    工具 key 差异的来源只是：破折号后讲解性 gloss 被译成俄语（如 6：核心 `previsioni — previsioni = 预报（复数）` → 版内 `previsioni — previsioni = прогнозы (мн. ч.)`），
    或全角→半角标点形式（16、20 仅 `：`→`:`），或排版分支切换（58 核心 paren 式 → 版内 dash 式；102 核心 dash 式 → 版内 paren 式）。
    构建员“printed keys byte-identical”的说法按工具 key 定义并不精确（见 §13 D1），但按答案词头口径成立，属信息性差异，非阻塞。
  - 3 项真重定向（E 区意→俄翻译题，合法重定向）：
    - 137：核心 `周一第一场寒冷来了。 — 对照原文` → 版内 `В понедельник приходит первый холод. — См. оригинал`；
    - 138：核心 `观众可以免费品尝。 — assaggiare gratis = 免费品尝` → 版内 `Публика может пробовать бесплатно. — gratis = бесплатно`；
    - 139：核心 `周日晚上，佛罗伦萨对尤文图斯。 — si gioca = 进行比赛` → 版内完整印刷段 `«Фиорентина» — «Ювентус» в воскр. веч. — si gioca = играют`
      （工具 key 截断为 `«Фиорентина»` 系第二破折号切分伪影，完整 seg 与构建员引文逐字一致）；
    - 与构建员所谓“同 DE 族”说法无关：本项系逐项贴出对照后独立裁定，未因同族说法跳过。
  - 140 **不在 keydiff 内**：key `Ogni previsione deve essere chiara.` 两版逐字相同，仅注释译为 `dovere = должен, нужно` ✓。
  - 150：`✓ Образец — в разделе H этой страницы (81 слово)` ✓。
- P8 注释纯俄语：版内 P8 SVG CJK = 0（§1）；注释层俄语逐页核查无中文残留。

## 4. 跨族残留复查 — 通过（无一处跨族残留）

- 全 8 页独立复扫：德语 `Mailand`、`Kostprobe`、`Seite `、`HINWEIS`、`ÜBUNGEN`、`MERK`、`LÖSUNGEN`、`Wochenzeitung`、`Erklärungen`、`Leser`、`Übung`、`Antworten`、
  他族 gloss 前缀/分隔符/指令词 `Note — `、`Nota — `、`Uitleg — `、`— Page`、`— Página`、`— SEITE`、`PAGINA`、`Exercises`、`Exercices`、`Ejercicios`、`Exercícios`、`Oefeningen`
  **全部 0 命中**。构建员自述“德语残留 0”属实。
- 箭头串（如 P8 `mettere: io → metto`、`vincere: ha vinto`）为意大利语动词变位，核心同款，非德语残留（freeze 差分中仅标点形式变化，key 相同）。
- 范文计口径（与核心同一口径独立计数）：
  - 本体 81 词：核心与版内范文文本**逐字相同**（`Lunedì 2 novembre metto il cappotto e la sciarpa: … con le parole nuove del freddo.`）；
  - 含标签口径 83 词 = 81 + `Testo modello:` 两词。两种口径均列出，81 词本体与核心一致，构建员“含标签计 83”属实。

## 5. 几何门 — 通过

- `tools/occlusion_audit.py`（自检先行：6 类 planted 全部触发、clean 对照静默）独立重跑：
  **版内 0 flags / 核心 0 flags / NEW vs 核心 0**（`occlusion-proof.json/.txt`）。
- 补充扫描（校对自写，仅作补充，不替代工具结论）：
  - 右缘 ADVANCE 扫描（带 [40, 1910]，masthead 黑体豁免）：8 页 **0 flags**；
  - 框线扫描：8 页均有 28/40 双框 + 2580 页脚线各 1 条；
  - 同基线碰撞扫描（解码后文本节点，全部基线，不只家具带）：8 页 **0 重叠**；
  - P6 图表标签覆盖：按构建员基线锚定墨迹法（PIL `getmetrics`，anchor `ls`，后绘实心 rect）**逐字复现：最大 0.0%**（门限 <30%），与构建员自述一致；
    （注：校对第一版紧墨迹法曾得 27.0%，系校对方法锚点错误——把 ascender 原点当基线，墨迹盒整体下偏约一个 ascent；修正后 0.0%，并经 P6 卡片目视确认标签与柱条无接触。见 §13 D4。）
- 流程终值复测（ls-anchor 修正墨迹法，`scan4.txt`）：
  - P7 col3：流游标 1646.0；实测墨迹底 **1645.7**；FRASI 规则线 y=1686（线宽 2，上缘 1685）→ **净空 39.3px**，构建员“40px”成立（口径：流游标/墨迹底均距线约 40px）；
  - P8-keys：流游标 2484 / 流底 2552；实测最大基线 2536.4、最大墨迹底 **2539.9**；页脚线 2580 → **净空 40.1px**，且墨迹底在流底 2552 之内。
    2484 只是末列流游标，不是最低墨迹——口径差异已说明，无阈值被穿越（见 §13 D3）；
  - P1 parola 注释（R1 余旗 1）：终版 1 行，基线 1846.3，墨迹底 1850.5，row-B 线 1864 → **净空 13.5px，全消除**；
  - P7 parola gloss（R1 余旗 2）：墨迹底 1285.6，词框底 1286.5 → **框内 0.9px，全消除**（极紧，见 §14 O1）；
  - P7 信件框披露末行墨迹底 1645.7，信件框底 1646.0 → 框内 0.3px（极紧，见 §14 O1）；工具 BOXTITLE 0 + 目视框内。
- 修复范围哈希差分验证（构建树 `sha256-r*.txt`）：
  - R0→R1 变化恰 10 个文件：p1/p2/p7/p8 的 SVG + cards + 两 PDF，p3–p6 字节不变 ✓；
  - R1→R2 变化恰 6 个文件：p1/p7 的 SVG + cards + 两 PDF ✓；
  - 与构建员所述修复范围精确一致；R1 余 2 旗标终版全消除（上两项）。

## 6. gloss 门 — 通过

- 核心源独立实测（核心构建树 `content*.py` 的 `gloss()` 串，按 `·` 拆分，非借他族数字）：
  P2 6（il cappotto、la sciarpa、i guanti、a strati、il termosifone、il crisantemo）、
  P3 5（il panettone、il torrone、l'assaggio、la bancarella、il cantiere）、
  P4 4（la giornata、la presentazione、gli spalti、la sera）、
  P5 4（il cosplay、gratuito、il documentario、lo schermo）、
  P6 5（la probabilità、la media、il modello、il bollettino、aggiornare），**合计 24**。
- 版内渲染后 gloss 串同法计数：P2 6、P3 5、P4 4、P5 4、P6 5，**合计 24，与核心 1:1**；
  24 个意大利语词头全部在渲染 SVG gloss 串中现身；渲染前缀均为 `Пояснение — `；
  分布按页：P1 另有桥接词表（下项），P2–P6 各一框，P7/P8 无 gloss 前缀——与 W43 同配对 pattern 一致（§9）。
- P1 桥接词表 4 项 1:1：`primo freddo`、`versante adriatico`、`previsione`、`assaggi`
  （核心 `讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。`
   → 版内 `Пояснение — primo freddo = первый холод · versante adriatico = Адриатика · previsione = прогноз · assaggi = пробы.`）。

## 7. 读者园地 — 通过（按协调员裁定执行）

- 保留的核心意大利语元素逐字核实：
  - 信件逐字：`«Ciao! Sono Li, studio italiano a Pechino. Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone — almeno in foto!» — Li`（版内 P7 y=1401.5–1493.09 四行）；
  - 标签 `(esempio della redazione)` 保留（y=1523.62）；
  - 预告带意大利语承诺保留（y=2488/2516.56：`…E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!`），**预告行不计入邀请**。
- 披露句终版逐字摘录（P7 信件框，3 行，20pt，y=1584.15/1612.55/1640.95）：
  `Пример редакции, а не настоящие письма; лучшего текста со страницы 8 нет. Напишите нам — лучшие в VOL.3!`
  三事实齐全：(1) `Пример редакции` = 系编辑部示例；(2) `а не настоящие письма` = 非真实来信；(3) `лучшего текста со страницы 8 нет` = 尚无最佳 P8 作文；
  显性祈使 `Напишите нам` + VOL.3 刊登承诺 `лучшие в VOL.3!` 齐全。
- 最佳 P8 作文覆盖范围裁定：**覆盖充分**。依据：
  - 单数 `лучшего текста со страницы 8` 与 IT×PT 同类裁定先例的单数最佳作文槽位一致（PT：`o melhor texto da página 8`；EN：`no best page-8 essay yet`；DE：`bester Seite-8-Text`）；
  - W43 同配对披露句同结构（`Письмо-образец от редакции. В VOL.2 — письма и лучшие сочинения (стр. 8). Пишите!`）；
  - 预告带的复数 `i testi migliori della pagina 8` 系核心冻结原文，非披露句的承诺口径，二者并存不构成欠覆盖（PT 先例同理裁定）。
  - P8 写作题唯一：H 区 150 题（`«La tua settimana del primo freddo»`，80–100 词），披露句所指即该题的最佳作文槽位。
- IT 核心 P7 并无意大利语披露句可供保留（核心信件框仅有信件 + 标签 + 中文披露句 3 行，y=1611.15/1639.55/1667.95）；
  版内全文检索意大利语披露句变体（`lettera vera` / `Non è una lettera` / `Esempio della redazione: non`）**0 命中**，未新造意大利语披露句。
  故不以“无意大利语披露句”判 NOT PASS（与 IT×EN 同类项 B1 非阻塞裁定、IT×DE 同结构已上架一致）。
- 零编造：Li / 北京均为核心自带标注示例，未新增任何读者、信件、姓名或引言。

## 8. 徽章槽位专项裁定 — 偏离 W43 同配对槽位，但非阻塞（SOP 合规）

三方实测值：

| 方 | 徽章串 | 槽位 / 字号 | strapline 处理 |
|---|---|---|---|
| (a) W43 IT×RU 已上架版 P1 | `ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`（逐字） | y=372，20pt，bold，居中 x=975 | **被替换**：W43 全刊 8 页检索 `ITALIA VERA` / `GIORNALE SETTIMANALE` 均为 0 命中，strapline 未见于任何位置 |
| (b) W45 核心 P1 | 无配对徽章（核心无徽章槽） | — | y=372，19pt，居中 x=975：`IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA`（与 W43 核心同串） |
| (c) 本版 P1 | 与 W43 逐字相同的徽章串 | **y=574，22pt，bold，居中 x=975**；墨迹宽 1164.09px（框内，左右余量约 393px） | **保留**：y=372、19pt strapline 与核心逐字一致 |

净空实测（本版 P1）：深色带底 542（rect y=424 h=118）→ 徽章墨迹顶 553.0（**11.0px**）；徽章墨迹底 578.8 → `LA NOTIZIA` 墨迹顶 589.5（**10.7px**）；几何审计 0 旗标；P1 卡片目视徽章醒目、居中、位于深色带与头条之间，配对标识清晰可辨。

裁定：
- **事实**：W43 同配对在 372 时 strapline 被替换（与任务书所指 IT×ES 已证情形同类），本版 574 插入**偏离 W43 同配对槽位**，此点 KIT §3/§14 已明文记录，非暗改。
- **但非阻塞**，理由四项：(1) SOP 要求的是配对标识在 P1 报头区清晰可辨，未规定 y=372 槽位；574 仍在报头区、字号更大（22pt > 20pt）、字符串逐字，标识功能完整保留，且 strapline 与徽章并存，信息量反增；
  (2) 按现行冻结门实测，删除 strapline 将表现为一条非 CJK 删除串，需另行裁定——构建员选择保冻结、移徽章的保守路线，冻结门与标识门两全，而非为槽位牺牲其一；
  (3) 574 槽为 W45 IT 族本周期惯例：IT×DE（`ITALIENISCHER TEXT · DEUTSCHE ERKLÄRUNGEN…`，y=574，22pt，bold）与 IT×FR（y=574，22pt，bold）已实测同槽；
  (4) 插入零位移：核心 P1 该处为空（带底 542 → 头条 `LA NOTIZIA` 基线 606 之间无核心文本），几何全绿。
- 非阻塞建议（不改本版）：将 W45 IT 族 574 徽章槽规则写入工具表或 SOP，避免后周期重复裁定；**不要**为追 W43 槽位而把徽章移回 372（那将破坏冻结门）。

## 9. 家具门 — 通过（与 W43 同配对逐项对照）

| 家具 | 版内实测 | W43 对照 | 结论 |
|---|---|---|---|
| 页脚（8 页） | `La Lucerna · ИТАЛЬЯНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ИТАЛЬЯНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ` 8/8 | 同式 VOL.1 8/8 | 仅 VOL.2 替换 ✓ |
| 页码行 | `Страница N из 8`，N=1–8 各 1 页 | 同式 8/8 | ✓ |
| gloss 前缀 | `Пояснение — `：P1–P6 有，P7/P8 无 | 同 pattern（P1–P6 有，P7/P8 无） | ✓ |
| P8 分隔符 | `— СТРАНИЦА N —` 8/8；`— PAGINA` 0/8 | `— СТРАНИЦА` 8/8；`— PAGINA` 0/8 | ✓（KIT“W43 已是 СТРАНИЦА 式”属实） |
| 栏头 | VITA · ЖИЗНЬ、CULTURA · КУЛЬТУРА、SPORT · СПОРТ、GIOVANI · МОЛОДЁЖЬ、APPROFONDIMENTO · РАЗБОР、LINGUA · ЯЗЫК 等 | 同式各 1 页 | ✓ |
| 指令词 | Вставьте、Составьте предложение、Переведите、Верно или нет、Напишите、Соедините пары、`E TU? · А ВЫ?`（词形均为 W43 式） | 词形同 | ✓（计数差异见 §13 D9，内容驱动） |
| P1 strap | `OGNI SETTIMANA IN ITALIANO · ИТАЛЬЯНСКИЙ, КОТОРЫЙ ЧИТАЮТ ИТАЛЬЯНЦЫ` | W43 全文逐字命中 | ✓ |
| P1 band/330 行 | 右 `НА ЭТОЙ НЕДЕЛЕ ПРИХОДИТ ПЕРВЫЙ ХОЛОД` / `Неделя первого холода · см. страницу 2`；330 行 `ИТАЛЬЯНСКИЙ · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A` | W43 式，VOL.2 + 本期主题替换 | ✓ |
| KIT §14 偏差 | VOL.2；计数 A2 47/B1 70/B2 33 与范文 81 词（W43：46/71/33 与 90 词）；徽章槽（§8）；其余逐字 | 计数/范文差异均为核心驱动（核心 KIT：150 题、A2 47/B1 70/B2 33、范文 81 词） | ✓ |
| 修复轮措辞 | R1/R2 均为措辞收紧 + 两处尺寸修正（P2 诊所标题 21pt、P7 词框高 +2px），无结构改动；哈希差分范围与所述精确一致（§5） | — | 无内容丢失（§1 碎片裁定佐证） |

## 10. 图片门 — 通过

- 光栅载荷：仅 P3、P5 各含 1 个 `<image>`（base64 内嵌），载荷哈希核心与版内**逐项相等**
  （P3 `9ea4244b4d216b67…` 长 346,864；P5 `d6bc00b109d273c4…` 长 627,056；位置尺寸亦同：P3 x=1451 y=200 434×265；P5 x=1451 y=200 434×300）。
- 署名在版：P3 `Foto: Wikimedia Commons — dominio pubblico`（y=593.6，与核心同位）；P5 `Foto: Wikimedia Commons — CC0`（y=628.6，与核心同位）；卡片目视均清晰。
- 其余 6 页核心与版内均无 `<image>` 元素（P1 雪花线描、P4 赛程表、P6 图表为 SVG 绘制图形，随冻结差分覆盖，无正文删除）。

## 11. ABSTRACT 门 — 通过

`ABSTRACT.txt`：单行（338 字，末尾换行 1 个），**ASCII 双引号 0 个**，俄语原生。
含：刊名 `La Lucerna`、VOL.2、目标语名（итальянский）、读者语（русскоязычных читателей）、
真实主题关键词（первый холод ноября、День поминовения 2 ноября、чемпионат мира по панеттоне в Милане 7–8 ноября、фестиваль торроне в Кремоне、11-й тур Серии А）、
学习者搜索短语（`учите итальянский по настоящим текстам`）、分级 A2–B2、150  упражнения。事实均取本期内容，无模板套词。

## 12. 卡片目视 + 题量/级别独立展开计数 — 通过

- 8 张卡片逐页目视：P1（徽章、strapline、雪花图、练习 1–10、测验 7–10）✓；P2（练习 11–28）✓；P3（照片+署名、练习 29–46）✓；
  P4（赛程表、练习 47–64）✓；P5（照片+署名、练习 65–82）✓；P6（图表+练习 83–100，图表注“数据为练习所编”）✓；
  P7（诊所、词框、金句 8 句、信件+披露、预告带、练习 101–112）✓；P8（评估 113–150、全部答案、范文）✓。
  无溢出、重叠、压页脚、压框线、图表标签遮盖、答案区侵入页脚问题。
- 题量与级别**从渲染 SVG 独立展开计数**（chip 级别节点配对后随 `N.` / `N–M.` 节点，区间展开；核心与版内 chip 序列 147 节点逐项相同）：
  **总数 150，无缺号、无重号**；按页 **10 / 18 / 18 / 18 / 18 / 18 / 12 / 38**；
  按级别 **A2 47 / B1 70 / B2 33**（纯 chip 展开：A2 47 题、B1 70 题、B2 33 题；另有 2 个页导览混合 chip `A2→B1`、`A2→B2` 不配对任何题号，不计入）。
  与核心 KIT、构建员自述、P8 compare 三方一致。
- 范文 81 词与核心逐字一致（§4）；校对前后交付与核心哈希不变（§0）。

## 13. 与构建员自述不符处（即使非阻塞，亦列出）

- **D1 — P8 keydiff“12 项 printed keys byte-identical”表述不精确**：按 p8.py 自身的 key 定义，12 项的工具 key 均与核心不同——差异来自破折号后讲解 gloss 的俄语化（10 项）、全角→半角标点（16、20）或排版分支切换（58、102）。
  成立的是**首词答案词头逐字相同**。裁定不变（信息性差异，非阻塞），但 KIT §7 的措辞应改为“答案词头相同”以免后人误读。
- **D2 — P7 col3“40px”**：经修正墨迹法实测成立（墨迹底 1645.7，距规则线上缘 1685 为 39.3px；流游标 1646.0）。校对第一版紧墨迹法曾得 16px，系校对锚点错误（见 §5 注），已修正——错在校对方法，不在构建员。
- **D3 — P8-keys“2484/2552”**：2484 为末列流游标、2552 为该列流底，不是全区最低墨迹；实测最大基线 2536.4、最大墨迹底 2539.9，距页脚线 40.1px，仍在流底之内。无阈值穿越，但单看 2484 会低估最低墨迹约 56px。
- **D4 — P6 图表“最大 0.0%”**：按构建员 ls-box 法逐字复现确为 0.0%。校对第一版紧墨迹法曾得 27.0%，系同一锚点错误所致的伪影（次行柱条与错位墨迹盒相交），已修正——错在校对方法，不在构建员。
- **D5 — 徽章宽 1164.25px**：实测 1164.09px，差 0.16px（字体度量取整口径），可忽略。
- **D6 — 冻结差分计数口径**：KIT 表格为多重集计数（如 p2 −29），`freeze-diff-proof.json` 的 `removed_strings` 为去重串计数（如 p2 −20）；两套数字均复现且一致，裁定以去重清单 + 多重集总量双重核对完成。
- **D7 — “IT×DE / IT×EN / IT×FR 三族同槽”仅 2/3 实测**：DE、FR 已实测 y=574/22pt/bold；EN 族徽章串/槽位未被校对搜索定位（EN 栏徽章式不同），§8 裁定不依赖 EN 族，仅以 DE、FR 佐证族惯例。
- **D8 — web PDF 文本不可提取**：pypdf 与 pdftotext 对 web PDF 8 页均提取 0 字；但核心 web PDF 与 W43 web PDF 同样 0 字，属该管线 web 渲染的共性，非本版缺陷；print PDF 提取完整。
- **D9 — 指令词计数与 W43 不同**：`Переведите` 版内 1 页 / W43 0 页；`Напишите` 版内 6 页 / W43 4 页。词形均为 W43 式，计数差异由 W45 核心题型分布驱动，非家具偏离。
- **D10 — KIT §12 措辞**：“P7 letter note replaced”与“parola gloss to 1 line”等 R1 描述与终版 SVG 一致；R2 所述 `rep2` 依赖 R1 节定义——校对未重跑 transform.py（只读），该依赖关系未独立验证，但终版 SVG 即最终证据，不影响结论。

## 14. 非阻塞观察

- **O1 — 极紧边距（建议后周期留意，不阻塞）**：P7 词框 gloss 墨迹底距框底 0.9px；P7 信件框披露末行墨迹底距框底 0.3px。两者均在框内（工具 BOXTITLE 0 + 目视框内），但余量已近度量误差；若后周期 gloss/披露加长，需优先复测这两处。
- **O2 — 徽章竖向槽位较紧**：带底→徽章 11.0px、徽章→头条 10.7px，均无重叠，目视分隔清晰；574 槽本身无富余，若徽章串加长需重测宽度（现宽 1164.09px，框内余量约 393px/侧，宽度无忧）。
- **O3 — P8 答案区底缘**：最低墨迹距页脚线 40.1px，余量充足。
- **O4 — 核心 P7 金句标签用意大利语 `(Pagina N)`**：系核心自带惯例（译文为中文时标签仍用 Pagina）；版内按 RU 栏规范用 `(Страница N)`，正确。
- **O5 — W43 P1 页脚外另有一行主题行**（`ИТАЛЬЯНСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.1 · L'ORA SOLARE · IL CINEMA`）：W45 对应位置为本期 330 行，主题不同属正常期次差异。
- **O6 — 早期 Cyrillic 显示乱码系通道渲染伪影**：校对初版输出中个别 `Пояснение` / `вероятность` 显示为 `��`，经码点级核查文件内容正确（U+041F 等无误），非文件问题。

## 证据文件（本目录）

- `REPORT.md`（本报告）
- `freeze-diff-proof.json` / `freeze-diff-proof.txt`（冻结差分独立重跑）
- `occlusion-proof.json` / `occlusion-proof.txt`（几何审计独立重跑，自检通过）
- `p8-compare-proof.txt` / `p8-core.json` / `p8-ed.json` / `p8-extract-core.txt` / `p8-extract-ed.txt`（P8 compare 与 key 提取）
- `scan1.txt`（禁词/CJK/词框/金句标签/读者园地/残留/徽章三方/家具/图片/范文）
- `scan2.txt`（删除串裁定/FRASI 节点/金句 joined-stream 计数/gloss 源串/渲染 gloss 重建/家具分页面/W43 核心 strapline/轮次哈希差分/范文双口径）
- `scan3.txt`（首版补充几何扫描，含已修正的锚点误差——以 `scan4.txt` 为准）
- `scan4.txt` + `scan4_corrected_ink.py`（修正后 ls-anchor 墨迹测量：P7 col3、P7 词框/信件框、P1 parola 注释、P8 keys、徽章净空、P6 图表覆盖）
- `proof_scan.py` / `proof_scan2.py` / `proof_scan3.py`（校对扫描脚本）
- `scratch/`（基线复现工作区、校对前后哈希清单）

**最终结论：ZERO PROBLEMS。本版可交付（按既有流程入 LucernaRead/weekly 仓；Discord 仍暂停，不发 Discord、不入主聊天）。**
