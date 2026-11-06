# 独立校对报告 — Lucerna Weekly W45 KO×IT（目标韩语 × 读者母语意大利语）

**结论：ZERO PROBLEMS — 可交付协调员串行上架，阻塞项：无。**

- 交付目录：`files/weekly-report-w45-ko-it/`（svg ×8、cards ×8、print `Lucerna-VOL2-IT.pdf`、web `Lucerna-VOL2-IT-web.pdf`、`WEEKLY-KIT.md`、`ABSTRACT.txt`）
- 核心对照：`files/weekly-report-w45-ko-core/`（VOL.2）
- W43 同配对对照：`files/weekly-report-ko-it/`（VOL.1）
- 校对窗口：2026-10-28 04:34–04:55 UTC（快照 04:34，终态复核 04:55）
- 校对员约束遵守：未派生任何下级代理；未碰 `weekly-git`；未改核心 / W43 / 交付目录 / `tools/` 下任何文件；未清理共享 scratch；未发 Discord；未往主聊天发卡片 / PDF；未建 cron；未宣布上架（上架由协调员串行做）。所有重跑均在校对员自有 scratch（本报告同目录 `work/` 下的 `freeze-baseline/`、`edition-rerun/` 及 wrap-spy 副本）中完成并重定向 OUT；交付 / 核心目录从未原地跑过 build 树脚本。
- 门输出不截断：本报告逐门给出实测值与结论；原始日志全部保留在 `work/`。

## 0. 查重、快照与终态复核

- **查重（2026-10-28 ~04:33 UTC）：** 无任何进程的 cwd 属于本版树。当时在跑的两个无关 build（ko-ja、ko-zh-tw 的 `render.py`，04:32 UTC 启动）不触发 stand down。交付 mtime 最后为 04:28:43–04:32:09 UTC；经 90 秒静默复查（04:34:57 UTC 复查，mtime 未变）后开工。
- **快照（04:34 UTC）：** `work/delivery-before.sha256`、`work/delivery-before.stat`、`work/core-before.sha256`、`work/w43-before.sha256`。
- **交付哈希 = 建造员声称值：** print PDF 32,551,109 字节，sha256 `3daf94d0d8ab500b86a221bd6bab737fa8a0bc5244d4d13773af86e1f9daa54c`；web PDF 3,558,396 字节，sha256 `ce556beff78568f82afca371c9f2f3eca58d7473250cd4ae10f6855e4f054e1f`；8 个 SVG 哈希与 KIT 一致（p1 `67593753f48125…`、p2 `13fa9b3e25cb…`、p3 `a1804d1de003…`、p4 `429af0356052…`、p5 `5b9d433b0d74…`、p6 `9d5a67c7c057…`、p7 `02ed62e4b9f6…`、p8 `63896ee51b9e…`）。
- **工具版本 = KIT 声称值：** `tools/p8.py` sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`；`tools/occlusion_audit.py` sha256 `e1f92b42eb8996fe04c5ffb60c4ec23e1911239a5f94b76808f01ed9414addf2`；`tools/freeze.py` sha256 `d9adfa486a788e57e15805d383f5691094067d26f1884c127dea4d1a1e587d54`。
- **终态复核（04:55 UTC，全部工作完成后）：** 交付、核心、W43 三组内容哈希与 04:34 快照逐项 diff，**全部为空**（`DELIVERY HASHES UNCHANGED` / `CORE HASHES UNCHANGED` / `W43 HASHES UNCHANGED`）。交付 SVG mtime 仍为 04:28:43–04:28:47（校对前），**无任何 mtime 刷新**，无需披露刷新项。

## 1. 冻结（Freeze）— 通过

- **自有 scratch 核心基线重跑（`work/freeze-baseline/`，`work/freeze-baseline.log`）：8/8 逐字节一致。** 重跑产出核心 SVG 哈希：p1 `f1e6913d5fbcc098`、p2 `839dcdd0ae4d603f`、p3 `7437117949a3da0a`、p4 `7f0aed9bec64dbb`、p5 `68e6ead94a42ec4`、p6 `e7f53e421500d0a`、p7 `ddb4e76cf4e97815`、p8 `1703151409819875`；重跑后核心完整性再哈希确认未变。
- **freeze diff（`work/freeze-diff.json`、`work/freeze-diff.log`），逐页新增 / 删除串数：** p1 +21/−20、p2 +44/−39、p3 +33/−31、p4 +29/−25、p5 +38/−35、p6 +24/−19、p7 +38/−36、p8 +174/−169；合计新增 401 串、删除 374 串。每一删除串均为中文讲解层或中文家具，每一新增串均为其意大利语对应项或登记项；**串多集层面韩语目标文本零改动**。
- **新增 CJK：** p1–p7 各为 0；p8 = 1 字 {절}，合计 1。唯一新增 CJK 出现在 P8-104 注释引用韩语词头 절기，见门 2 逐字核实。
- **纯 Hangul 新增串分类（恰 3 条）：** P6 `«틀리다».`、P7 `«〜부터 〜까지예요?»`、P8 `바뀌었어요`——三者均为意大利语注释中的完整词换行（门 6 逐一验证），非新增韩语散文。纯 Hangul 删除串均为合法替换：页码行（`제 N 면 / 총 8 면`）、练习说明、P7 框尾片段 `〜까지예요?」`、P8 H 说明行（`157자의 예가 있어요.`、`쓰기 문제예요 (정답은 하나가 아니에요). 아래에`）。**无纯韩语散文串新增或删除。**
- **P7 词框定义句冻结：** P7 col 4 两行 y=1086.5 `말할 때 쓰는 틀이에요. 물어볼 때는` 与 y=1117.03 `'〜부터 〜까지예요?'라고 해요.` 与核心逐字相同；仅框内讲解行本地化（核心中文 `句式拆解：「从〜到〜」。提问：「〜부터` / `〜까지예요?」` → 本版意语 `La struttura: «da ~ a ~». Per chiedere:` / `«〜부터 〜까지예요?»`）。
- **P1/P7 改动范围（过程记录缺口，如实记录）：** `round-baselines/` 仅含哈希文件、无二轮 SVG，故二轮→终版的逐串 diff 不可复现。哈希层面：与二轮基线 `round2-sha256.txt` 比对，**仅 p1 与 p7 不同**，p2–p6 与 p8 与二轮逐字节一致；与一轮比对，p1、p5、p7 不同。P1/P7 范围声称因此以哈希范围 + 最终全量重测为准，不编造串级 diff。终版中 P1 日历单行与 P7 两行披露 + 框高变化均已实测确认（门 5、门 7）。
- **结论：冻结通过。**

## 2. P8 — 通过（CLEAN）

- **工具与调用：** 当前 `tools/p8.py`（sha 见门 0，与 KIT 一致），`--total 150`，显式双路径调用（`work/p8-dircompare.log`、`work/p8-filecompare.log`）。两路径一致：核心 150 题记入、本版 150 题记入，状态 **CLEAN**，missing=[]、extra_count=0、keydiff=[137, 138]。印刷行提取见 `work/p8-edition-extract.log`、`work/p8-core-extract.log`。
- **keydiff 逐项印刷行 adjudication（以渲染 P8 SVG 为准，非仅工具输出）：**
  - 104：本版 `104. A — 절기 = i 24 periodi dell'anno` vs 核心 `104. A — 节气＝一年24个时节`——韩语词头 절기 引用后接意语 gloss；这是唯一新增 CJK 案例，格式与 W43 同款引用一致（韩语词头 + 读者语 gloss，见门 10 的 W43 格式证据）。**通过。**
  - 137：本版 `137. Il 7 novembre è l'ipdong. — Confronta con pag. 1` vs 核心 `137. 11月7日是立冬。 — 对照第 1 版`——键改为意语译文，注释改为意语，页码引用 1 = 核心引用。**通过。**
  - 138：本版 `138. Mancano 12 giorni all'esame. — Confronta con pag. 5` vs 核心 `138. 离高考还剩 12 天。 — 对照第 5 版`——同上，页码引用 5 = 核心引用。**通过。**
  - 139：韩语键不变 `139. 특별 조치는 11월 19일에만 적용돼요. — Confronta con pag. 6`（核心注释 对照第 6 版）。**通过。**
  - 140：韩语键不变 `140. 저는 토요일에 내장산에 단풍을 보러 가요. — Confronta con pag. 3`（核心注释 对照第 3 版）。**通过。**
  - 150：本版 `150. ✓ Il modello è nella sezione H di questa pagina (157 caratteri)` vs 核心 `150. ✓ 范文见本版 H 区（157 字）`——apparatus 意语化。**通过。**
  - 分隔符：8 条韩语分隔符 `— 제1면 —` … `— 제8면 —` 两版完全一致保留（注：startswith 过滤另命中 5 条以 `— ` 开头的冻结 G 对话题干，属练习正文而非分隔符，报告中不混淆）。
- **P8 注释语言：** 本版 P8 Han 表意字 = 0（`work/analyze.json` 的 `p8_han_edition` 为空）；注释纯意语，跨族残留 0。
- **P8 流末端三口径同报（上限 2540）：**
  - 流光标（自有 scratch 重跑日志）：**2366**（bottom 2540），与建造员声称一致。
  - 末列（x=1451）末基线 **2350.48**（150 题 apparatus 行），墨迹底 **2353.98**。
  - 已填列末基线 / 墨迹底：x=65 列 2530.35 / 2533.85（38 题）、x=527 列 2528.85 / 2532.35（77 题）、x=989 列 2530.35 / 2530.60（115 题）。
  - 三口径全部 < 2540；最紧余量为已填列墨迹底 2533.85（余 6.15 px）/ 基线 2530.35（余 9.65 px）——与 ko-pt 校对中同类 9.65 px 数值一致。P8 keys 各列行数 42/42/42/36（含 8 条分隔符与 apparatus 处理；p8.py 记入集仍为 150/150）。
- **结论：P8 通过。**

## 3. gloss 口径裁决 — 通过（本版 = 核心，逐页相等；66≠84 不是缺陷）

- **方法（以渲染 SVG 为准，非源码推测）：** GREY #57523f、20.5 pt 行按同 x、20–35 px 间距在文档顺序中链成组；P8 排除（content8 的 H f-string 行不是 gloss 项，遵 ko-pt 前例）。词汇项按**词头**计数：意语按 Hangul 词头 + `=` 模式；中文按 `·` 切分且不要求 `·` 前有空格（换行会剥掉 `·` 前空格，如 `围裙 ·목록` 计 2 项）。
- **口径 V（词汇口径 = gloss 盒 + P7 词框）：本版 = 核心 = 67，逐页 [5, 16, 13, 7, 12, 8, 6, 0]。** 源码交叉核对一致：两版 `gloss()` 盒串合计均为 61（content12 21、content34 20、content56 20），P7 `expl()`/`glossline()` 词框均为 6（2+2+2），61+6=67。
  - **建造员 KIT 的 66 为算术笔误，非阻塞观察（KIT 未由校对员改动）：** 其逐页 5/16/13/**6**/12/8/6 漏计 P4 单项盒 `Nota — 예상 = previsione` / 核心 `译注｜예상 预测。`（content34：P3 盒 4+3+3+3=13，P4 盒 4+2+1=7，非 4+2）。同类笔误在 ko-pt 校对中已裁定为非阻塞。纸面（核心 = 本版、逐项相等）正确，故不构成阻塞；协调员可转告建造员在下次 KIT 修订中把 66 改为 67，**本报告不擅自“纠正”他版 KIT**。
- **口径 F（渲染页口径，ko-pt 定义 = gloss 盒分组 61 + P7 词框 6 + 说明行 17）：本版 = 核心 = 84，逐页 [5, 19, 16, 10, 16, 12, 6, 0]。** 简报的 84 即此口径，与 66/67 不矛盾。17 条说明行分布：P2 3、P3 3、P4 3、P5 4、P6 4。
- **完整性口径（SVG GREY 段计数）：本版 = 核心 = 85，逐页 [5, 19, 16, 11, 16, 12, 6, 0]**——较 F 多 1，为冻结的 P4 图注 `위 그림은 가을야구의 순서예요. 지금은 세 번째 칸, 플레이오프예요.`（GREY 20.5，两版完全一致，非 `glossline()` 说明调用）。
- **渲染 gloss 行数（换行产物，非门指标）：** 本版 [3, 11, 8, 7, 8, 6, 6, 0] = 49 行 vs 核心 [3, 9, 8, 4, 8, 4, 3, 0] = 39 行。意语 gloss 更长、换行更多，行数差异合法，项数相等。注：本轮早期一次有缺陷的分组（遇含 ` = ` 的续行即切组；中文 `·` 切分要求前导空格）曾得出本版片段 81 / 核心 60，已废弃，不可复用。
- **结论：gloss 门通过——同一口径下本版与核心逐页相等。**

## 4. 金句、短语、范文、登记、溢出 — 通过

- **金句 8 句（P7 本周短语，韩语逐字 = 核心，意语译文 + 页签，整刊频次 = 核心）：**

  | 韩语金句 | 意语译文 | 页签 | 整刊频次（本版 = 核心） |
  |---|---|---|---|
  | 11월 7일은 입동이에요 | Il 7 novembre è l'ipdong. | 1면 | 5 |
  | 절정에 가까운 주말이라고만 말할 수 있어요 | Si può solo dire che è un weekend vicino al picco. | 1면 | 2 |
  | 김장은 겨울 내내 먹는 김치를 담그는 일이에요 | La stagione del kimchi è preparare il kimchi per l'inverno. | 1면 | 4 |
  | 수능까지 17일 남았어요. 오늘이 D-17예요 | Mancano 17 giorni all'esame, oggi è D-17. | 2면 | 2 |
  | 낮은 길은 더 늦게 물들어요 | I sentieri bassi si colorano più tardi. | 3면 | 2 |
  | KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요 | I KIA Tigers hanno battuto gli LG Twins con tre vittorie consecutive. | 4면 | 2 |
  | 온 나라가 수험생을 응원해요 | Tutto il paese incoraggia i candidati. | 5면 | 2 |
  | 날짜를 먼저 보세요 | Guarda prima la data. | 6면 | 2 |

  频次为去空格子串计数（8 页全部行拼接），本版 = 核心 = **5 / 2 / 4 / 2 / 2 / 2 / 2 / 2**；8 句均在其页签文章页出现。
- **P7 短语来源：** 8 句均逐字出自本刊文章并带正确页签（上表）；P7 词框例句 `11월 1일부터 12월 15일까지 산불조심기간이에요.` 的核心短语出自 P2 文章；P7 全部韩语串冻结 = 核心，故核心侧来源关系原样继承。
- **范文：** P8 col 4（x=1451）14.5 pt `예:` 例文，6 渲染行，拼接文本核心 = 本版（sha 前缀 `10cda14a9af4e8c2` 两版一致）；去空格长度 **157** 两版一致；首句 `나의 겨울 준비는 김장부터 시작해요.`；末句 `겨울 준비가 끝나면 마음이 든든해져요.`；印刷说明范围 150–200字 满足；P8-150 apparatus 亦称 157 caratteri。注：H 区意语说明跨列换行——col 3 行 `È un esercizio di scrittura (non c'è un'unica risposta giusta). Qui sotto c'è un esempio di` + col 4 首行 `157 caratteri.`（x=1451, y=200.5）组成完整句；H 题干因此在本版起笔更低（y=285.025）于核心（y=225.8）。
- **登记（自有 scratch `work/regdump.py`，`work/reg-edition.json` vs `work/reg-core.json`）：** 题号 1–150 连续；页分布 10/18/18/18/18/18/12/38 两版一致；级别 A2 51 / B1 72 / B2 27 两版一致；页差 0、级别差 0；键差仅 137、138（意语重定向，门 2）与 150 开放题占位串（本版 `(domanda aperta — il modello è qui sotto)` vs 核心 `(开放题，范文如下)`，属讲解层文本，印刷 P8-150 行见门 2）；题型标签意↔中 1:1 映射且计数一致（Completa la frase 48、Scelta multipla 52、Abbinamento 16、Cloze 13、Costruisci la frase 8、Trasforma la frase 4、Vero o falso 4、Traduzione 4、Scrittura 1）。注：本轮早期一次比较脚本变量 bug 曾把题型标签误印为页 / 级别差，已由干净重跑取代，不可复用。渲染 SVG 练习标签序列（含范围头如 `25–28.` 加单项）逐页：p1 1–10、p2 11–28、p3 29–46、p4 47–64、p5 65–82、p6 83–100、p7 101–112、p8 113–150，总体连续 1–150。
- **溢出：** 自有 scratch 本版重跑（`work/edition-rerun/`，`work/edition-rerun.log`）**8/8 SVG 逐字节 = 交付**；日志中 **FLOW OVERFLOW / HEAD TOO WIDE = 0**。流末端均 < 各自 bottom：P1 头条列 2/2 y=1413（bottom 1828）、P1 测验列 3/3 y=2521（bottom 2540）、P8 练习列 3/3 y=463（bottom 1252）、P8 keys 列 3/3 y=2366（bottom 2540）、P7 各列（a2 y=1092、b1 y=1059、b2 y=1089；bottom 1560）。
- **结论：门 4 通过。**

## 5. 几何 — 通过

- **canonical `tools/occlusion_audit.py`（`work/occlusion-*.log/json`）：** 自检 OK（6 类植入全部触发、干净对照静默）；本版 0 标记；核心 0 标记；NEW vs 核心 0。
- **补充扫描（自有脚本 `work/analyze.py`，`work/analyze.json` + `work/analyze.log`）：**
  - 全页右缘 ADVANCE 扫描：本版每页最大值均为 1885.0（页码行锚定终点，距 1950 页缘 65 px）；核心亦每页 1885.0。
  - 框线扫描：两版页外图形均为 0。
  - 同基线墨迹碰撞扫描（0.6 px 容差分组、真实墨迹框）：本版 0、核心 0。
  - P6 标签覆盖（基线锚定墨迹法，门 <30%）：后绘矩形最差覆盖本版 = 核心 = **0.0%**；任意顺序最差 100% 的是带标题 `깊이 읽기 · Lettura approfondita`（本版）/ `깊이 읽기 · 深读`（核心）——深色带矩形绘于标题之下，与核心完全相同，非覆盖。
- **P1 日历修复（三轮修复重测）：** 本版 P1 单行 y=1190.10（18.5 pt）`Cinque date: l'ossatura di questo numero.`；上方韩语源行 y=1162.10（19 pt）`이 다섯 가지 날짜가 이번 주 신문의 뼈대예요.`；下方固定源行 y=1216.00（18.5 pt）`자료: 국사편찬위원회 공지 (10월 19일)`；至源行的基线间距 25.90 px、**墨迹间距 6.15 px**（`work/analyze.json` 的 `p1_calendar`：日历行墨迹框 [1473.0, 1175.35, 1831.0, 1194.35] vs 源行墨迹框 [1473.0, 1200.5, 1770.5, 1219.75]）。无压字、无碰撞。
- **P1 黑带左右行间隙（补充）：** 左行 2 右缘 868.22 vs 右行左缘 1272.36（`L'IPDONG` 24 pt bold advance 112.97 px = KIT 声称；第二行 21 pt advance 实测 582.64 px vs KIT 582.77 px，差 0.13 px，属字体度量舍入，见末尾非阻塞观察 3），间隙 404.14 px。
- **结论：几何通过。**

## 6. 孤儿扫描 — 通过（新增孤儿点 = 0）

- **定义：** 窗口 10–45、≥3 音节尾、全部散文栏 + P8 行；孤儿点 = 严格真词中断裂（空格感知 wrap spy：TOKEN 断裂、前行不以空格结尾、溢出 token 本身不是空格、前行尾为 Hangul、次行首为 Hangul、次行首 token ≥3 Hangul 音节）或行首孤儿标点（渲染行扫描 START-PUNCT）或括号化末行碎片。
- **朴素渲染行扫描（建造员 `orphan_scan.py` 复制到自有 scratch，`work/orphan_scan_copy.py`，`work/orphan-full.log`，窗口 10–45、≥3 音节尾、全部含 Hangul 节点含 P8）：** 核心 175 处、本版 176 处，行首孤儿标点 **两版均为 0**。朴素 SPLIT 对正常词界换行亦触发，故原始计数不是缺陷计数。
- **片段级 diff（忽略 y）：** 本版独有 3 处、核心独有 2 处，均为重排 / 分组产物，无一为新词中断裂或孤儿标点：本版独有 P2 FINAL-SHORT `'토요일, 심화만 봐요'`（组中位产物）、P2 SPLIT `' 물려주고, 낡은 옷은 | 깨끗이'`（意语重排后新分组的正常词界换行）、P8 FINAL-SHORT `'H · 써 보기'`（H 标题因组成变化被标为组末短行）；核心独有 P2 SPLIT `' 갈 때는 정해진 길로 | 다니세요.'`、P4 SPLIT `'(바꾼 문장은 모두 이 | 신문에'`（同类，分组漂移所致）。
- **Wrap spy（强方法；`svglib.py` 仅在两个自有 scratch 副本中插装日志，`work/wrap-edition.log`、`work/wrap-core.log`；spy 产物 SVG 仍与交付 / 核心 8/8 + 8/8 逐字节一致）：** 两版 wrap 调用均为 **943 次**。SPACE 断裂：本版 269、核心 279；TOKEN 断裂：本版 294（空格处 234 + 词中候选 60）、核心 245（空格处 187 + 词中候选 58）。**严格真词中断裂 ≥3 音节：本版 0、核心 0。** 注：早期未做空格感知的计数 49/50 均为行尾带尾空格或溢出 token 本身就是空格的词界断裂，已废弃。
- **建造员声称的 3 条新增纯韩文行，逐一验证为意语注释中完整词的正常换行：**
  - P6 `«틀리다».`——渲染 P6 SVG：前行 y=1775.5 `Se la frase è giusta scegli «맞다», se è sbagliata` → 本行 y=1805.225 `«틀리다».`：完整引号词在空格后换行，前行以完整意语词结尾。
  - P7 `«〜부터 〜까지예요?»`——spy SPACE 断裂：前行 `La struttura: «da ~ a ~». Per chiedere:` → `«〜부터 〜까지예요?»`：完整冻结句式短语。
  - P8 第 60 题注释 `바뀌었어요`——spy SPACE 断裂：[`60. 참피가 온대저기압으로 바뀌었어요. — Il passato di 바뀌다 è`, `바뀌었어요`]：空格后完整词续行。注：早期针检索曾误中 P1 文章冻结换行 `바다를 지나 10월 26일에 온대저기압으로 | 바뀌었어요. 야구에서는 KIA가`（另一冻结行），已由第 60 题调用取代。
- **结论：孤儿门通过，新增孤儿点 = 0。**

## 7. 来信框几何 — 通过（余量 3.11 px，末行确在框内）

- **本版来信框矩形（P7 x=1451 列）：**(1451, 1230.44, 434×513.5) → 框底 **1743.94**。
- **意语披露行（x=1473，GREY 20 pt）：** y=1707.93 `Nessuna lettera vera né tema di pag. 8: la` 与 y=1736.33 `promessa passa al VOL.3. Scriveteci!`。末行基线 1736.33，墨迹底 **1740.83**（= 基线 + 4.50 下降部，与建造员声称一致），**框底余量 3.11 px**。无压字、无越框。
- **金句规则线：** y=**1773.94**（x 65→1885）；距末行墨迹底间隙 **33.11 px**。
- **核心侧公式少算声称（只报告，不重开核心）：** 核心来信框矩形 (1451, 1230.44, 434×508.5) → 框底 1738.94；核心中文披露末行基线 1764.73、墨迹底 1766.73，**超出框底 27.79 px**（建造员“约 26 px”为同一量级；ko-pt 校对同法测得 27.8 px）；核心规则线 y=1768.94，距核心末行墨迹底仅 2.21 px，无行被压。本版框高 508.5→513.5（+5 px）与披露 2 行布局的净效应（尾常量 +26→+60 为 +34，少一行 −29）共同产出 1743.94 框底；核心公式本身的少算为核心侧观察，本版不因此扣分。
- **结论：来信框几何通过。**

## 8. 读者来信角 — 通过（适用组合门，第 2 分支，明确裁决）

- **页上原文（逐字，P7 x=1473 列）：**
  - 框标题 y=1272.44：`독자의 편지 · Lettere dei lettori`
  - 例信行 y=1319.44–1441.56（冻结韩语）：`「안녕하세요. 저는 대학생이에요.` … `와도 따뜻하게 지내고 싶어요.」 — 독자 편지의 예`
  - 例信标注行 y=1502.09：`Esempio della redazione, non vera.`
  - 冻结韩语披露行 y=1561.49–1648.82：`알려요: 이 편지는 편집부가 쓴 예예요. 마감` / `때까지 진짜 독자 편지와 8면 쓰기 우수작이` / `도착하지 않았어요. 그래서 예가 실렸고,` / `지난 호의 약속은 VOL.3으로 이어져요.`
  - **披露句（意语，2 行，拼接 79 字 / 去空格 66 字）：** `Nessuna lettera vera né tema di pag. 8: la promessa passa al VOL.3. Scriveteci!`
  - **征集句（页上唯一祈使征集）：** 披露句内的 `Scriveteci!`（P7 全页检索无其他征集祈使，如 inviate / mandate 均无）。
  - **预告行（VOL.3 预告带，矩形 (65, 2399.94, 1820×118)，标题 y=2443.94 `다음 주 · La prossima settimana (VOL.3)`，正文 y=2483.94，墨迹底 2486.69，+34 约定末端 2517.94 < 2540）：** `다음 주에는 김장이 한창이에요. 수능까지 일주일이 남았어요. 한능검 시험이 가까워져요. 플레이오프와 한국시리즈 소식도 전해요. 여러분의 편지와 8면 쓰기 우수작도 실어요. 기대해 주세요!`（与核心逐字一致，仅 y 平移 +5，源于来信框变化。）
- **Adjudication 范围与分支（明确，不含糊）：**
  - **第 1 分支（征集句字面双覆盖）不成立：** `Scriveteci!` 字面既不点名“来信”也不点名“最佳 P8 文本”，是置于来信框内的通用“写信给我们”；按其直接字面范围至多覆盖来信一侧，不覆盖 P8 最佳文本。与 ko-pt 的显式双覆盖句（`Envie sua carta e seu melhor texto da pág. 8!`）形成对照，本版无此句。
  - **第 2 分支（组合门）成立并通过：** 同页披露句将最佳 P8 文本成分延至 VOL.3（意语 `né tema di pag. 8: la promessa passa al VOL.3`；冻结韩语 `8면 쓰기 우수작이 도착하지 않았어요… 지난 호의 약속은 VOL.3으로 이어져요`），**且**预告行明确点名 p.8 最佳文本（`여러분의 편지와 8면 쓰기 우수작도 실어요`，同时点名来信与 8面 쓰기 우수작）。按 pt-en / de / nl / es / ja / ru 前例裁决，该组合满足门。预告行本身不计为征集句（与建造员 KIT 表述及 ko-pt 裁决一致：预告与框内征集分别计数）。
  - 披露的三事实齐全：无真信到截稿、无 P8 最佳作品到截稿、例信刊登且上期承诺延至 VOL.3（冻结韩语披露 + 意语披露共同覆盖）；例信身份由标注行 `Esempio della redazione, non vera.` 加冻结韩语披露共同覆盖。
  - **结论：读者来信角通过，适用第 2 分支（组合门），非第 1 分支。**

## 9. 家具三方对照（核心 / W43 / 本版）— 通过

- **刊头：** `Lucerna`，无冠词，168 pt，(975, 262)——核心 = W43 = 本版完全一致。
- **徽章：** 字符串 `TESTI IN COREANO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`，y=394，20 pt bold，BRICK #a4553a，advance 跨度 (563.21, 1386.79) → 宽度 **823.58 px**，本版 = W43（核心无徽章）。**= W43，通过。**
- **副标（y=330，40 pt bold）：** 本版 `SETTIMANALE COREANO · VOL.2 · 입동 · 단풍 · 김장`（advance 1009.83 px = KIT 声称）；W43 `SETTIMANALE COREANO · VOL.1 · 태풍 참피 · 가을야구 · 단풍`（1176.79 px）；核心 `한국어판 · VOL.2 · 입동 · 단풍 · 김장`（640.91 px）。差异恰为 VOL.1→VOL.2 与主题词更换。**通过。**
- **标语：** y=366，本版 = W43（`한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로`，advance 503.97）vs 核心 y=372——W43 前例位移。**通过。**
- **规则线与黑带：** 规则 y=412/421，本版 = W43；核心 392/401。黑带矩形 y=433，本版 = W43 vs 核心 y=424（高均为 118）。**通过。**
- **页脚（y=2624，20 pt，8 页全）：** 本版 `Lucerna · SETTIMANALE COREANO VOL.2 · TESTI IN COREANO · SPIEGAZIONI IN ITALIANO`，advance 跨度 (65.0, 899.86) → 宽度 834.86 px（= KIT 声称）；W43 同串仅 VOL.1，宽度同为 834.86；核心中文页脚仅语言不同。**通过。**
- **页码行（y=2624，锚定终点 x=1885，8 页全）：** 本版 = W43 `Pagina N di 8`，advance 跨度 (1768.25, 1885.0) → 宽度 116.75 px（= KIT 声称）；核心 `제 N 면 / 총 8 면`。**通过。**
- **gloss 前缀：** `Nota — `，本版 = W43（核心 `译注｜`）。**通过。**
- **韩语 credit 行保留确为 W43 ko-it 前例（实测 W43 同页 credit 行）：** W43 P1 `사진: NASA — Public domain (Wikimedia Commons)`、P2 `사진: Gary Todd — CC0 (Wikimedia Commons) · 자료 사진`、P3 `그림: Paul Cézanne — Public domain (Wikimedia Commons)`、P4 `사진: Bain News Service — Public domain (Wikimedia…`、P5 两条（US Army、Elijah Flores）、P6 `사진: lumoplank — CC0 (Wikimedia Commons) · 자료 사진`——韩语 credit 格式为 W43 ko-it 已确立格式，故 W45 ko-it 保留韩语 credit 是前例而非偏离。**通过。**
- **结论：家具三方对照通过。**

## 10. 图片、credit、ABSTRACT、禁词与 Han 残留 — 通过

- **图片 payload = 核心（双口径，逐页按序一致）：**

  | 页 | 张数 | base64 文本 sha 前缀 | 解码 JPEG sha 前缀 | JPEG 尺寸 |
  |---|---|---|---|---|
  | P1（lumoplank，CC0） | 1 | `535fff46b7ce` | `6f7f33ed8f40` | 1920×1280 |
  | P2（wizdata，CC0） | 1 | `e66d2b455ec6` | `96a6a19b612a` | 1920×1301 |
  | P3（Udonhan1992，CC0 + Paul Cézanne，PD） | 2 | `e266b6ee1a87` / `5bea45d1f81e` | `158ea3a0e81f` / `214cc390ac7c` | 1920×1080 / 1920×1535 |
  | P4（Bain News Service，PD） | 1 | `1a7e7d6d5ffc` | `18ad8ae06fac` | 1024×743 |
  | P5（Gary Todd，CC0） | 1 | `6a1bab177d54` | `35e7dc69d417` | 1920×1280 |
  | P6–P8 | 0 | — | — | — |

  计数 1/1/2/1/1/0/0/0 = 核心；两口径哈希本版 = 核心，逐页按序一致。
- **credit 行（韩语 `사진:/그림:` + Artist + 许可 + Commons 格式，与核心逐字一致且确已放置）：**
  - P1：`사진: lumoplank — CC0 (Wikimedia Commons) · 자료 사진`
  - P2：`사진: wizdata — CC0 (Wikimedia Commons) · 자료 사진`
  - P3：`사진: Udonhan1992 — CC0 (Wikimedia Commons) · 자료 사진`；`그림: Paul Cézanne — Public domain (Wikimedia Commons)`（两行，第二行续 `Commons)`）
  - P4：`사진: Bain News Service — Public domain (Wikimedia Commons)`（两行，第二行续 `Commons)`）
  - P5：`사진: Gary Todd — CC0 (Wikimedia Commons) · 자료 사진`
  - Artist 名与 Commons API Artist 字段一致（lumoplank、wizdata、Udonhan1992、Paul Cézanne、Bain News Service、Gary Todd）；W43 ko-it 前例见门 9。Commons 图像缺口等核心侧事实债按门 12 继承，不判本版阻塞。
- **ABSTRACT（`files/weekly-report-w45-ko-it/ABSTRACT.txt`，实测）：** 意语单行（293 字节，1 行 + 末尾换行），无 ASCII 双引号：`Il settimanale coreano VOL.2 per lettori italiani: ipdong il 7 novembre, l'ultimo weekend delle foglie d'autunno, l'apertura della stagione del kimchi e il conto alla rovescia per l'esame di maturità coreano, con 150 esercizi dal livello A2 al B2 — impara il coreano leggendo notizie vere.` 真实主题关键词（ipdong 11 月 7 日、最后秋叶周末、泡菜季开季、考试倒计时）+ 学习者搜索短语（`impara il coreano leggendo notizie vere`）+ VOL.2、意大利读者、150 题、A2–B2 分级齐全。**通过。**
- **禁词扫描（中 / 英 / 意三语形式：桥接、bridge/Bridge、intermediario、intermediazione、intermediary、中介、橋接，全 8 页 SVG 文本）：0 命中。**
- **Han 表意字残留（U+4E00–U+9FFF 等口径，全 8 页 SVG）：本版 = 0，核心 = 2136（中文讲解层）。** 韩语 Hangul（含冻结 credit 行与 절기 引用）不是 Han 表意字残留；任务的例外条款（冻结词头引用 + 韩语 credit 行）因此无需为任何 Han 计数开脱，因为 Han 计数本身已为 0。
- **结论：门 10 通过。**

## 11. 网页版 PDF 与 8 张卡目视 — 通过

- **网页版 PDF：** 8 页，页尺寸 1400×1938 pts（print 版 1462.5×2025 pts，8 页），与卡片渲染同源。方法：`pdftoppm -png -r 72` 逐页渲染（1400×1938 px）对卡片 PNG（LANCZOS 缩至同尺寸）做 PIL 差分；数值见 `work/webpdf-compare.log`。

  | 页 | meanAbs | >30 像素占比 | 空白区 mean | 空白区 >30 占比 | 8×8 块均值范围 |
  |---|---|---|---|---|---|
  | p1-pyoji | 6.82 | 6.90% | 1.37 | 0.06% | 0.39–17.15 |
  | p2-saenghwal | 6.50 | 6.90% | 1.33 | 0.05% | 2.04–14.78 |
  | p3-munhwa | 6.22 | 6.60% | 1.13 | 0.03% | 0.00–12.90 |
  | p4-seupocheu | 5.41 | 5.79% | 0.99 | 0.05% | 0.00–12.44 |
  | p5-cheongnyeon | 5.81 | 6.20% | 0.98 | 0.02% | 0.00–13.19 |
  | p6-gipi | 5.40 | 5.79% | 1.05 | 0.02% | 0.00–12.03 |
  | p7-mal | 5.40 | 5.46% | 1.04 | 0.05% | 0.00–16.59 |
  | p8-siheom | 6.42 | 7.15% | 1.43 | 0.01% | 0.00–16.69 |

  8 页均匀的 JPEG q85 + 重采样噪声，无离群页，**无噪声页**（fr-en 教训所指的噪声页不存在）。
- **8 张卡目视（逐张读卡）：**
  - P1：刊头、徽章、副标、黑带左右行、日历单行 `Cinque date: l'ossatura di questo numero.` 清晰且与上下源行无碰撞；秋叶图 + credit 齐全；测验 7–10 题齐全。
  - P2：泡菜图 + credit、gloss 盒、D-day 四格、练习 11–28 齐全，无溢出。
  - P3：地铁图与 Cézanne 静物图 + credit 齐全；gloss 盒、练习 29–46 齐全。
  - P4：棒球队老照片 + credit、秋棒时间线图、单项盒 `Nota — 예상 = previsione`、练习 47–64 齐全；表标签完整。
  - P5：图书馆图 + credit、gloss 盒、练习 65–82 齐全。
  - P6：对照表四行标签完整；D 组说明换行 `«틀리다».` 独行清晰，无截断；练习 83–100 齐全。
  - P7：词框、实错诊所、来信框（两行意语披露完整在框内，与金句规则线间隙清晰）、本周短语 8 句、VOL.3 预告带齐全；练习 101–112 齐全。
  - P8：练习 113–150、E 组意语重定向（137/138）、150 apparatus、答案集 150 条、H 范文齐全；末列距页脚余量充足。
  - 无空白页、无缺图、无溢出、无可见碰撞。
- **结论：门 11 通过。**

## 12. 核心事实债（只继承，不判本版阻塞）与新增主张 — 通过

- **继承债（韩语目标文本冻结 = 核心，故原样继承，逐项见核心）：** 韩国系列赛 11 月 2 日雨延 caveat（G1 10 月 26 日结果未知，纸面以“宣布日 11 月 2 日”与“可能变更”表述）；G1 10 月 26 日结果未知；Champi 已删（纸面称未登陆、转为温带气旋）；立冬 / 小雪来源（国史编纂委员会 10 月 19 日公告、山林厅 / 国立公园公团预报）；韩史细节二手；Commons 图像缺口；ssam 诚实标注。以上均未在本版中被改动或加重。
- **新增主张 = 0：** 新增 401 串的审计——含数字新增串逐条核对（门 0 终态核查附带的数字串清单），其全部数字（日期、人数、页码引用、题号、157 caratteri）均为对应核心中文串数字的直接意语翻译（意语千分位 `.` 如 551.864 对应核心 551,864）；无新增人名、地名、日期、数据或事实断言。新增内容仅为：意语讲解层、家具（徽章 / 页脚 / 页码行）、P7 意语披露 + `Scriveteci!` 祈使、P8 E 项重定向（137/138 键译文，页码引用沿本刊内容 1/5/6/3，非照抄 W43 的 1/2 模式——已对核心引用核实）。
- **结论：门 12 通过。**

## 非阻塞观察（不构成阻塞，KIT 未由校对员改动）

1. **建造员 KIT gloss 数 66 应为 67（算术笔误，见门 3）：** 纸面正确，KIT 文字有误。协调员可转告建造员在下次 KIT 修订中更正；本报告不改动任何 KIT。
2. **核心来信框公式少算约 27.8 px（见门 7）：** 核心侧观察，只报告，不重开核心；本版框几何本身通过。
3. **P1 黑带第二行 advance 实测 582.64 px vs KIT 582.77 px（差 0.13 px）：** 字体度量舍入量级，左行间隙仍有 404.14 px，不构成缺陷。

## 总结论

**ZERO PROBLEMS。** 12 门全部通过：冻结（新增 CJK 仅 P8-104 절기 引用）、P8 CLEAN（keydiff 仅 137/138）、gloss 双口径本版 = 核心（V 67、F 84）、金句 / 短语 / 范文 / 登记 = 核心、几何全 0、孤儿新增 0、来信框余量 3.11 px、读者来信角适用第 2 分支组合门通过、家具三方 = W43、图片双口径 = 核心、ABSTRACT 与禁词 / Han 全过、网页版 PDF 无噪声页且 8 卡目视干净、新增主张 0。可交付协调员串行上架；阻塞项：无。

## 证据索引（`hidden_files/w45/ko-it-proof/work/`）

- 快照与终态：`delivery-before.sha256`、`delivery-before.stat`、`core-before.sha256`、`w43-before.sha256`、`delivery-after.sha256`、`core-after.sha256`、`w43-after.sha256`
- 冻结：`freeze-baseline/`、`freeze-baseline.log`、`freeze-diff.json`、`freeze-diff.log`
- P8：`p8-dircompare.log`、`p8-filecompare.log`、`p8-edition-extract.log`、`p8-core-extract.log`
- 登记：`regdump.py`、`reg-edition.json`、`reg-core.json`、`reg-edition.log`、`reg-core.log`
- 本版重跑：`edition-rerun/`、`edition-rerun.log`、`edition-rerun.sha256`
- 几何：`occlusion-selftest.log`、`occlusion-edition/core/new.log` + `.json`、`analyze.py`、`analyze.log`、`analyze.json`
- 孤儿：`orphan_scan_copy.py`、`orphan-full.log`、`orphan-summary.log`、`wrap-edition.log`、`wrap-core.log`、`wrap-edition-run.log`、`wrap-core-run.log`、`wrap-edition.sha`、`wrap-core.sha`
- 网页版：`webpdf/`（8 页渲染）、`webpdf-compare.log`
