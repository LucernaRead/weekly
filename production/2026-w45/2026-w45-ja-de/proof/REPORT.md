# 独立校对报告 — Lucerna Weekly W45 JA×DE（日语×德语，VOL.2）

- 校对对象：`files/weekly-report-w45-ja-de/`（SVG×8、卡片×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 构建树（只读核对，未改）：`hidden_files/weekly-report-w45-ja-de-build/`
- 核心对照（只读）：`files/weekly-report-w45-ja-core/`（JA VOL.2）；W43 同配对对照（只读）：`files/weekly-report-ja-de/`
- 校对员权限边界：只校对，不改源码；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未清理共享 scratch 目录。
- **本报告不宣布上架**（上架由主线串行执行）。

## 结论：不是 ZERO PROBLEMS — 阻塞项 1 项

### 阻塞项清单

**B1（唯一阻塞项）— P8 第 37 题答案提示仍为中文，未德化。**

- 印刷行（本版 P8，— Seite 3 — 栏，卡片上亦可见）：`37. 8 — 工艺展到11月8日`
- 核心同题：`37. 8 — 工艺展到11月8日`（逐字相同；全 150 段中唯一一段核心与本版逐字相同，见 `p8-keydiff-table.md`）。
- 应为（与 #122 同义的无星期版德语提示）：`37. 8 — Die Ausstellung läuft bis zum 8. November`。
  对照：#122 核心 `B — 传统工艺展到11月8日` → 本版 `B — Die Ausstellung läuft bis zum 8. November`（已正确德化）；
  #32 核心 `B — 工艺展到11月8日（周日）` → 本版 `B — Die Ausstellung läuft bis zum 8. November (Sonntag)`（已正确德化）。
- 根因（构建树核查，非猜测）：核心构建 `content34.py` 登记的该题提示为无星期的裸串 `工艺展到11月8日`；
  本版 `transform.py` 的 NOTES 只有带星期的 `工艺展到11月8日（周日）`（第 94、125 行）与 `传统工艺展到11月8日`
  （第 89 行），没有裸串条目，故该串原样穿透。EN 版同题已正确译为 `8 — The exhibition runs to November 8`，
  证明这不是核心本身的问题，而是 DE 映射缺口。
- 违反的门禁：讲解层须全为读者母语（德语）；中文装置词残留须为 0；P8 提示纯德语。
  本项修复后须重跑 P8 对照与本校对（P8 SVG、卡片、双 PDF 随之变化）。
- 修复建议（供主线/构建员执行，本校对未动手）：在 `transform.py` NOTES 中补一条
  `("工艺展到11月8日", "Die Ausstellung läuft bis zum 8. November")`，重建并重验；
  同时更正 KIT 中“P8 提示纯德语 / 150 条皆为德语提示”的表述（见非阻塞观察 O1）。

除 B1 外，以下 11 项全部独立重测通过（或如注明的局部通过）。B1 修复前不得按 ZERO PROBLEMS 放行。

### 跨版干扰注记（结论中单列，第 11 项末尾亦有）

JA×EN 的 `transform.py` 在构建中途改了两处英文措辞，对本版德语文本**无影响**。
证据：本版 SVG 文本集与 JA×EN 终版 SVG 文本集的交集减去核心集仅剩 2 条中性串
（`45. d — オーケストラ = Suginami d`，地名+字母；`92. 65 — 38 + 27 = 65`，算式），
无任何英文讲解串泄漏；`(Sunday)` 为 0，`(Sonntag)` 正确出现 2 处（#32、#69）；
本版 SVG 与第 2 轮哈希一致，且与我方在 proof 内重跑的构建逐字节一致（见第 6、11 项）。

## 开工查重与无变动证明

- 开工时唯一在途渲染进程的 cwd 为 `hidden_files/weekly-report-w45-ja-es-build`（JA×ES 版），不属于本版，
  故不 stand down；本版目录在开工前已新鲜交付，且 90 秒静默复查哈希无变化，安全开工。
- 校对前后交付物哈希 diff 为空：`sha256-before.txt` = `sha256-after.txt`（SVG×8、卡片×8、双 PDF、
  ABSTRACT.txt、WEEKLY-KIT.md，18/18 一致）；核心全文件哈希校对前后一致（`sha256-core.txt` =
  `sha256-core-after.txt`）。即：校对过程零改动。
- 交付物终态 = 第 2 轮哈希（`sha256-round2.txt`，18/18 一致，见第 6 项）。

## 1. 冻结与语言层（全部独立重测）

- **核心基线复现 8/8**：`tools/freeze.py baseline`（核心构建 `hidden_files/weekly-report-w45-ja-build`，
  输出重定向至 proof 内）逐字节复现核心 SVG 8/8；核心 SVG 在运行前后重哈希无变化。
  另：我方在 proof 内重跑本版构建（输出重定向至 proof 内）亦逐字节复现本版 SVG 8/8（见第 11 项）。
- **新增 CJK 逐页 = 0（8 页全 0）**：`freeze.py diff` 核心→本版，新增 CJK 字符数 P1–P8 皆为 0；
  CJK 总量变化仅为中文装置删除所致：P1 1406→1275、P2 1312→1161、P3 1172→1051、P4 1263→1169、
  P5 1247→1132、P6 1186→1101、P7 1676→1308、P8 2721→1454。
- **日语正文无丢失**：被删串逐页计数 P1 18、P2 20、P3 15、P4 13、P5 14、P6 11、P7 35、P8 170（新增串
  P1 20、P2 25、P3 17、P4 14、P5 16、P6 12、P7 36、P8 172；差额为换行重排所致）。
  上述增删数为 distinct 串种数；计重复时 freeze 总量为 P1 +20/-18、P2 +33/-28、P3 +24/-22、P4 +21/-20、
  P5 +27/-25、P6 +23/-22、P7 +41/-40、P8 +178/-176（差额来自 `填空`×9、`翻译`×4 等重复串与换行重排）。
  裁定：全部被删串均属以下四类之一，无一篇日语文章正文丢失——
  (a) 纯中文装置（刊头、栏名、指令、译注、答案提示）；(b) 日中混合栏名/词头，其中日语词头在本版对应串中
  逐字保留（如 `この号の内容`、`毎週、日本語で · … · 日本人が読んでいる日本語を読む`、`レベル A2 · ゆる整え食と暖かい11月`）；
  (c) 混合串的换行碎片，重组后日语部分不变（如 `しむ 享受。`→`楽しむ genießen.`、`る 核实。`→`確認する bestätigen.`）；
  (d) P8 中文提示 1:1 替换为德语提示（149/150；唯一例外即阻塞项 B1 的 #37，它根本未进入被删集，
  因为它未被替换）。P7 的日语披露句（`※この手紙は編集部の例です。…`）被删属于装置替换：
  按既定规则，日语披露句不作为德语读者的 operative 披露，其事实由德语披露句 1:1 承接（见第 9 项），
  不计为正文丢失。
- **中文装置词残留**：在版 SVG 中扩大词表扫描后，仅剩 1 处真残留，即 B1 的 #37；
  其余命中均为日语正文词（如 P3 的 `漆器`，核心日语文章与词头中原有，非装置）。
  词表含：练习/答案/对照第/范文/本期目录/头条/即学即练/本周单词/数字看本周/说说你自己/闪电问答/
  快讯/译注/第 N 版/共 8 版/练习与答案/中文简析/按版面分页/下期预告/本周金句/本周句式/易错诊所/
  三个级别/练习数据/读图表/把词和释义配对/填空/造句/判断/翻译/写作/一锅菜/蒸笼/集市/工艺/陶瓷/
  染色/罚款/变装/雕像/节日/周末/话题/预算/满足/观测等，P7 预告与披露中的 `第8版` 出现于
  逐字保留的日语句子内（核心日语预告句与披露句原句），不属中文讲解层残留。
- **共享汉字逐词裁定**：新增串中出现的全部 CJK 字符（P1 50、P2 44、P3 30、P4 38、P5 37、P6 33、
  P7 61、P8 129 个 distinct 字符）无一不在核心中出现，且均为合法日语用法：
  日语词头（見頃、立冬、練習、暦、紅葉狩り、落葉、予算 等）与日语文章词，配德语释义；
  未发现以中文词义使用的共享汉字（如把 `工艺` 作中文词用——唯一中文 `工艺展到11月8日` 即 B1）。
- **违禁词**：`桥接` 与 `橋接` 在 SVG×8 + WEEKLY-KIT.md + ABSTRACT.txt 中均为 0（grep 逐文件计数全 0）。
- **规范 svglib**：本版构建 `svglib.py` md5 = `d73e23b365676c3618d7e060b835eb4d`，与规范值一致，
  且与核心构建、EN 构建的 `svglib.py` md5 相同，未被编辑。

## 2. 日语专项

- **行首禁则扫描 8 页全 0**：禁则集取自本版 `svglib.py` 的 JA NO_START
  `。、，．！？：；）」』】ー…‥・` 加小假名 `ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ`，
  对核心与本版全部 `<text>` 首字扫描：核心 8 页 0、本版 8 页 0。
  补扫扩展集（上述集 + ASCII 闭符 `)]}.,!?%:;"'` + `ヵヶ`，含去前导空格变体）：本版 8 页亦为 0。
- **P1 顶栏同基线间距（y=92，独立墨迹实测）**：左 `VOL. 2 · 第2号` 墨迹右止 219.8；
  中 `毎週、日本語で · Jede Woche neu · 日本人が読んでいる日本語を読む` 墨迹 643.2–1306.9
  （构建员称 643.1，0.1 为取整差异，无实质影响）；右 `2026年11月2日（月）〜8日（日）`
  为 end 锚定、锚点 x=1885、墨迹 1529.9–1885.1。间隙：左→中 423.4、中→右墨迹起 223.0，
  **无碰撞**。核心中栏墨迹为 681.3–1268.6（中文版较短），本版中栏虽变宽仍有充分间隙。

## 3. P8 keydiff 计数口径专项（逐项对照见 `p8-keydiff-table.md`）

- 口径独立确立：`tools/p8.py compare --total 150`（lines 口径，显式双文件形式）结果：
  核心 noted 150、本版 noted 150、状态 **CLEAN**、missing=[]、extra=[]、uncertain=[]、
  keydiff = [1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113, 115, 117, 118, 137, 138, 140, 146, 147]（21 项）。
  该 150=150 口径来自核心 P8 渲染内容本身（核心 150 条答案全部带提示），既未照搬 EN 核心的 78 口径，
  亦未照搬 JA×EN 的 150 口径——是本版核心实测值。
- **无歧义计数：21 = 2 真重定向 + 1 提示本地化落入 keydiff + 18 括号分支伪影**：
  - 真重定向 2 项（E 区翻译题答案语言 ZH→DE，合法）：#137 `文化日是11月3日。` →
    `Der Kulturtag ist am 3. November.`（提示 `对照第3版` → `Siehe Seite 3`）；
    #138 `乱扔垃圾，要罚2,000日元。` → `Wer Müll wegwirft, zahlt 2.000 Yen Strafe.`
    （提示 `对照第5版` → `Siehe Seite 5`）。
  - 提示本地化落入 keydiff 1 项：#140，键 `神戸の紅葉のライトアップを見に行きたいです。` 日语原样，
    提示 `对照第6版（神户的灯光秀）` → `Siehe Seite 6 (Kobe-Beleuchtung)`；因 p8.py 括号分支把提示前缀
    并入提取键，故被计入 keydiff，但真键未变。
  - 括号分支伪影 18 项：#1、#2、#5、#7、#8、#9、#29、#32、#65、#69、#78、#101、#113、#115、#117、
    #118、#146、#147；真键（首个 ` — ` 之前部分，如 3、9、7、B、C、A、27、○）与核心逐字相同，
    提取键差异仅因提示译文（含星期括号）被并入提取键；其中 #5、#101 还伴随 dash→paren 方法翻转
    （德语提示括号居行末，中文全角括号不居行末），真键仍不变。
  - 由此澄清构建员“2 + 19”的含糊处：提示本地化总数为 2 项（#139 与 #140），其中 #139 不在 keydiff
    （无括号、dash 分支键相等：键 `読書週間は10月27日から始まります。` 原样，提示 `对照第7版` →
    `Siehe Seite 7`）；#140 是第 2 项提示本地化，不应被笼统计为纯伪影。
    KIT 中“伪影 17 项”与所列 18 项亦不一致，且 #140 被双重计数（见观察 O1）。
- **P8 提示纯德语：不通过，唯一例外 B1**：除 #37 为中文外，其余 149 条提示均为德语
  （或按设计为日语词头 + 德语释义，如 `見頃 = beste Laubzeit`）；无英文提示。
- **印刷提示集合按题号相等**：核心 noted 集 = 本版 noted 集 = 1–150 全集，无 EXTRA_ONLY、无缺失；
  p8.py 状态 CLEAN（集合相等不掩盖 #37 的语言问题——集合只计提示存在性，不计提示语言，
  故 B1 须由逐段语言核查发现，且已被发现）。
- **P8 答式**：破折号体，与 W45 核心一致（编号行含 ` — ` 者 149 行 + ✓ 行 1 行；核心亦为 149 行；
  分隔行 `— Seite N —` 8 行与核心 `— 第N面 —` 逐一对应翻译）。见第 10 项。

## 4. gloss 口径专项（渲染实测，见 `gloss.json`）

- 方法：从渲染后 SVG 中按 gloss 框（前缀 `译注｜` / `Anm. — ` 起始的连续碎片）重组 gloss 串，
  按 `·` 拆分计数，并与核心逐项 1:1 对照词头。
- 渲染结果（核心 = 本版）：P1 4、P2 9、P3 8、P4 7、P5 7、P6 4、P7 0、P8 0，**合计 39 = 39**；
  词头 39 项全部 1:1 相同（如 P1 祝日/見頃/暦/お届けします，P2 蒸す/並ぶ/食卓/超える/予報/平年/
  季節風/話題/値上がり，余类推），释义由中文换为德语。
- 换算关系（说明为何其他计数法不等于 39，均非内容差异）：
  - 按源码文件分组：content12.py（P1+P2）13 项、content34.py（P3+P4）15 项、content56.py（P5+P6）
    11 项、content7.py 0 项，合计 13+15+11+0 = **39**，与渲染口径一致。
    构建员源码文件口径若合计不为 39，必是数了别的单位，不得直接引用为渲染结论。
  - 按 gloss() 调用次数：10 次（P1 1、P2 2、P3 2、P4 2、P5 2、P6 1），≠39。
  - 按渲染 `<text>` 碎片数：核心 19、 本版 26（德语换行更多），≠39。
  - 按去重词头数：38（`話題` 在 P2 与 P5 各出现 1 次，重复计 2 项），≠39。
  - 本报告的 39 是渲染串按 `·` 拆分的条目数，与 JA×EN 渲染口径 39 项的单位相同。
- 附注：重组串在 CJK 换行边界处会出现词头与释义拼接（如 `超えるübersteigen.`、`平年Durchschnittsjahr`），
  这是拼接计数的假象，不是印刷合并——碎片在 SVG 中为各自定位的 `<text>`，卡片上词头与释义
  视觉分离（P2/P4/P5 gloss 框目视确认），且按 `·` 计数不受影响；核心亦有同类现象（如 `暦历法`、`季節風季风`）。

## 5. 第 1 轮英语残留专项

- `(Sunday)`：本版 SVG 中 **0 处**；第 1 轮残留已消除。
- 替代确认：`(Sonntag)` 出现 2 处，恰为应德化的两处星期日提示：#32
  `Die Ausstellung läuft bis zum 8. November (Sonntag)`、#69
  `Bürgerfest Naka, Yokohama, 8. November (Sonntag)`；其余星期均已德化
  （Dienstag×8、Montag×2、Samstag×9，含提示括号内）。
- 全册德语讲解层英语残留扫描：拉丁词表 471 个 distinct 词逐项过筛，无英文讲解词残留。
  剩余拉丁词均有合法归属，逐项说明如下（任务键/被讲解的日英语词条本身除外项亦列明）：
  - 德语词本身：全部讲解、栏名、指令、提示用词（如 Ausfüllen、Übungen、Siehe Seite、Antworten）。
  - 专有名词：SoftBank、DeNA、Kanazawa、Kobe、Suginami、Ikebukuro、Yokohama、Mika、Aikawa、
    Petr Kratochvil、Poliphilo、Syced、Wikimedia Commons、CC0（图片署名，核心原有）。
  - 赛事专名 `Japan Series`（P4 栏名 `Die Japan Series: zwei Spiele in Yokohama` 及 #115 等）：
    为赛事官方英文名，W43 JA×DE 亦用 `Die Japan Series im Detail`，非残留。
  - 棒球/借词：`Teams`（德语复数亦作 Teams）、`Innings`（棒球术语），与 W43 的 `Climax Series` 同类。
  - 平台名 `note`（日本平台 note，出现在日语文章与 `note-Rundschau` 中，非讲解层英文）。
  - 日语商品名 `サクサクdeコパン` 中的 `de` 为商品名组成部分。
  - 缩写 `JMA`（気象庁）、`SNS`（日语文章中的 SNS 一词）、货币名 `Yen`（德语亦用 Yen）。
  - 英文星期/月份名全册为 0；英文讲解短语（如 relaxed、steamer、your turn、multiple choice 等）为 0；
    一处形似命中 `Festival ist` 实为德语 `Festival ist`（动词 ist），非英文 is。
- KIT 中的 `Sunday` 两处（刊期行 `Monday 2 – Sunday 8 November 2026` 与第 1 轮修复日志）为
  工作文档记述，非本版讲解层文本，不计为残留。

## 6. 修复轮范围验证

- 两轮哈希对照（`sha256-round1.txt` vs `sha256-round2.txt`）：变化的恰为 P1、P2、P7、P8 的 SVG 与卡片
  及由此派生的双 PDF；**P3–P6 的 SVG 与卡片两轮字节一致**（P3 `6e7dec92…`、P4 `8c4752b4…`、
  P5 `b2093e83…`、P6 `655430d6…` 两轮相同），与第 1 轮 5 项 NEW 的修复范围（P1 趋势框、P2/P8 配对指令、
  P7 预告、P8 键流）相符，无超范围改动。
- 两轮串 diff 对照：P1 由长句改为短句（趋势框德语注）、P2 配对指令由 `Wörter den Bedeutungen zuordnen`
  改为 `Wörter zuordnen`、P7 披露句重写并缩短、P8 大量长提示改为短式并含 `(Sunday)`→`(Sonntag)`；
  P3–P6 两轮串集完全相同。
- 终态验证：P7 预告带（深色 rect x=65 y=2382.08 宽 1820 高 118）底止 = **2500.08 < 2540**（余量 39.92），
  带内预告文墨迹底 2468.58，页脚线 2580 无压线；P8 键流终态：答案流末行 y=2350.48（#150），
  非页脚文本墨迹底最大值 2518.42（< 2580 页脚规则线），且 occlusion 0 旗（见第 8 项），**无溢出**。
  构建日志亦印证：`P7 teaser ends 2500.08`、`P8-keys ended col 3/3 y=2366 (bottom 2540)`。

## 7. P7

- **定义句与金句原文逐字保留**：P7 定义句（`『ゆるく整える』` 框架段 4 行）与诊所日语例/正句
  全部位于核心与本版的公共串集中，逐字相同；**定义句本地化 0 处**（定义句本身仍为日语；
  本地化的是其讲解句：诊所讲解 4 句 + 框架讲解 `Zerlegung: Körper und Geist sanft in Ordnung bringen.`，
  共 5 句讲解德化，属正常装置替换，不计入定义句本地化）。
- **金句 8 句全册计数各恰 2×**（去空白拼接计数，核心与本版皆然）：
  文化の日は、11月3日（火よう日）です。/ ゆっくり、ゆるく整える日本の11月です。/
  『ゆる』は、無理をしない、ゆっくり、という意味です。/ 鍋の材料が1か月早く並び始めました。/
  伝統工芸と紅葉と光を、いっしょに楽しむことができます。/ ソフトバンクが2連勝でスタートしました。/
  ルールを守って、楽しいハロウィンにしましょう。/ 紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。
  每句在核心与本版的去空白全册拼接串中均恰出现 2 次（文章页 1 次 + P7 金句栏 1 次）。
- **页标签映射（以我方核心实测为准，与构建员称一致）**：核心 `(第1面)、(第1面)、(第2面)、(第2面)、
  (第3面)、(第4面)、(第5面)、(第6面)` → 本版 `(S.1)、(S.1)、(S.2)、(S.2)、(S.3)、(S.4)、(S.5)、(S.6)`，
  顺序与金句顺序一一对应。
- **P7 结构**：A2 本と読書のことば / B1 紅葉のことば / B2 数字を読む + 诊所 4 项 + 框架 +
  读者园地 + VOL.3 预告，与核心结构一致；P7 练习 101–112 共 12 题（见第 11 项）。

## 8. 几何

- **canonical 自检先行**：`tools/occlusion_audit.py --selftest` 通过
  （6 类 planted flags 全触发，clean 对照静默）；每次正式运行亦先自检通过。
- **分版/核心/NEW 三数**：本版 0 flags、核心 0 flags、**NEW vs 核心 0**（`occlusion-ed.json`、
  `occlusion-core.json`）。即几何门禁全过，无新增几何问题。
- **同基线墨迹碰撞扫描**：按基线分组、以墨迹盒重叠 ≥9px 且 ≥3×3 计，8 页全部 0 处。
- **P6 图表标签基线锚定墨迹法**：图表标签 8 串（类名 近場の満足/温泉/紅葉/グルメ + 百分比 38%/27%/21%/14%）
  及说明句，用 occlusion_audit 的基线锚定墨迹盒（getmetrics 上升量定位）与 PIL anchor="ls"
  交叉核对，两法墨迹盒逐项完全一致（至 0.1）；其后绘制的不透明图形覆盖率**全部为 0%**
  （条形 x 起 315，与类名墨迹右止 ≤175.0 无交叠；百分比位于条形末端之外），
  既 <30% 门禁，亦满足构建员称“无一高于 5%”（实测为 0%，更强）。
  注：getbbox 法若不作基线锚定会错位，为错误口径，本报告未采用。
- **全页右缘 ADVANCE 扫描**：每页最大 advance 右止恰为 1885.00（end 锚定文本的锚点），
  8 页均无 advance 右止 >1885.5 者；墨迹右止最大值 1885.12（页脚/顶栏 end 锚定文本的字形微超 0.12，
  在 occlusion EDGE 容差 0.5 内，不构成溢出）。
- **框线压框扫描**：BOXTITLE 类 0 旗（含于 occlusion 0 旗内）；另核 P1 趋势框、P2–P6 gloss 框、
  P7 各栏框、P8 各栏框，墨迹均未压框线。
- **8 张卡片全部目视（无抽查）**：P1–P8 逐张目视。版面干净、无重叠、无压框、无缺图；
  P1 砖红徽章、P6 图表条形与百分比、P7 披露/邀请/预告带、P8 答案流与页脚均清晰；
  P8 卡片上亦可直接看到 B1 的中文行 `37. 8 — 工艺展到11月8日` 混在德语答案列中（视觉佐证）。

## 9. 读者园地

- **日语示例信逐字不动、零编造**：核心与本版共 4 行逐字相同——
  `「こんにちは。私は中学生です。読書週` / `間には、図書館で本を2冊読みたいで` /
  `す。文化の日には、家族と金沢へ行きたい` / `です。」— 読者の手紙の例`；
  未增删任何读者、姓名、引文；信末 `— 読者の手紙の例`（示例标记）原样保留。
- **德语披露句逐字摘录**（P7 披露段重组，换行连接）：
  > „Beispielbrief, kein echter Brief. Bis zum Redaktionsschluss keine echten Briefe und keine besten
  > Seite-8-Aufsätze; beides erscheint in VOL.3. Schickt uns eure Briefe auf Japanisch — ausgewählte
  > Briefe erscheinen in VOL.3!“
- **逐项核实（核心日语披露句与中文披露句双源对照）**：
  1. 示例非真信：`Beispielbrief, kein echter Brief.` ✓（核心 JP `編集部の例`、ZH `示例信，非真实来信`）。
  2. 无真信：`Bis zum Redaktionsschluss keine echten Briefe` ✓（核心 JP `本当の読者の手紙…は届きませんでした`、
     ZH `未收到真实来信`）。
  3. 无最佳 P8 作文：`keine besten Seite-8-Aufsätze` ✓（核心 JP `第8版の作文の優秀作は届きませんでした`、
     ZH `第8版最佳作文`）。
  4. 顺延 VOL.3：`beides erscheint in VOL.3` ✓（核心 JP `VOL.3に載せます`、ZH `VOL.3将刊登…`）。
  （任务称“3 事实”所列实为上述 4 项可核 claim，含顺延承诺在内，4 项全部核实通过。）
- **显性祈使邀请 + VOL.3 刊登承诺**：邀请句 `Schickt uns eure Briefe auf Japanisch` 为显性祈使；
  承诺句 `ausgewählte Briefe erscheinen in VOL.3!` 明确承诺入选来信刊于 VOL.3。
- **最佳 P8 作文覆盖范围裁定（按 pt 族既定范围）**：邀请句字面仅覆盖来信
  （`Schickt uns eure Briefe auf Japanisch — ausgewählte Briefe erscheinen in VOL.3!`，只提 Briefe，
  未提 P8 作文）；但同页披露句将最佳 P8 文本顺延 VOL.3
  （`keine besten Seite-8-Aufsätze; beides erscheint in VOL.3`），故**组合满足门禁**；
  预告行（P7 末 `読書週間が終わります…読者の手紙と第8版の作文の優秀作も載せます。お楽しみに！`）
  本身**不计入邀请**（其为日语预告段，非祈使邀请，且核心原有）。本校对未凭空新写核心没有的披露句：
  德语披露句的全部事实 claim 均映射到核心日/中披露句，邀请句的 VOL.3 承诺亦有核心预告句为据。
  W43 JA×DE 披露句（`Beispiel der Redaktion — kein echter Brief. VOL.2 bringt echte Briefe und den
  besten Aufsatz von Seite 8!`）为同族先例形式参考，不作为本版事实来源。

## 10. 家具 / W43 三方测量

三方：W43 同配对版（`files/weekly-report-ja-de/`，VOL.1）、W45 核心（VOL.2）、本版（VOL.2 DE）。
结论：**本版家具 = W43 同配对版**（VOL 号除外），W43 同配对家具胜过 README #20 泛化规则
（#20 原则为“族先例胜于固定泛化值”；此处同配对已出货形式即为准）与 tables.json 通用值。

- **刊头几何**：本版与 W43 逐值相同——wordmark y=248、版次行 y=316、徽章行 y=356、
  标语行 y=390、规则线 y=406/413、深色带 y=424（带高 118，P7 预告带同此带高算法得 2500.08）。
  核心不同：wordmark y=262、版次行 y=330、无徽章行、标语行 y=372、规则线 y=392/401、带 y=424。
  本版未沿用核心几何，正确沿用了 W43 同配对几何。
- **砖红徽章 #a4553a**：本版 P1 徽章文本 `JAPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE
  FÜR DEUTSCHSPRACHIGE LESER`（y=356，bold，fill #a4553a）与 W43 P1 徽章文本逐字相同；
  核心无此徽章行。P1 SVG 中 #a4553a 出现 12 次（本版与 W43 相同计数，含各栏徽章色）。
- **页脚**：本版 8 页均为 `Lucerna · JAPANISCHE WOCHENZEITUNG VOL.2 · TEXT AUF JAPANISCH ·
  ERKLÄRUNGEN AUF DEUTSCH` + `Seite N von 8`，与 W43 形式一致（仅 VOL.1→VOL.2）；
  核心为中文式 `Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY` + `第 N 版 / 共 8 版`，已被替换。
- **S.N 标签**：金句栏 S.1、S.1、S.2、S.2、S.3、S.4、S.5、S.6（见第 7 项）；另 `Siehe Seite N`
 （P1 `Siehe Seite 3`、P8 E 区 `Siehe Seite 3/5/7/6`）与 W43 的 `Seite N` 形式一致。
- **„Übungen Seite N"**：本版 P2–P6 逐页为 `練習 · Übungen Seite 2/3/4/5/6`，与核心练习栏结构一致；
  P1（头版）、P7（语言栏）、P8（测试页）无此栏名，属结构固有，非缺失。
- **gloss 前缀**：本版 10 框全部为 `Anm. — `，与 W43 JA×DE 全部 gloss 框一致；
  **不用** tables.json 通用德语前缀 `HINWEIS · `（tables.json `columns.de.gloss_prefix` 即此值，
  但无已出货 JA×DE 版使用它；KIT 亦明言此覆盖关系）。三方核实完成。
- **P8 答式**：随 W45 核心破折号体（`N. key — note`，149 行 + ✓ 行），非 W43 括号体；
  KIT 对此的表述（W43 括号体为 W43 族属性、非本核心规则）与实测一致：
  本版与核心的 dash 行数均为 149，分隔行均为 `— Seite N —`（核心为 `— 第N面 —` 的翻译对应）。

## 11. 题量 / 范文 / ABSTRACT / 图片

- **登记展开独立计数**：我方在 proof 内重跑本版构建（输出重定向，REG 统计为我方运行结果，
  非构建员自述）——总数 **150**，级别 **A2 46 / B1 75 / B2 29**，页分布 **10 / 18 / 18 / 18 / 18 / 18 /
  12 / 38**（P1–P8），与核心规格逐值一致；题型：Ausfüllen 50、Multiple Choice 51、Zuordnen 12、
  Satzbau 8、Richtig/Falsch 11、Lückentext 13、Übersetzen 4、Schreiben 1。
  另以 P8 印刷答案 1–150 连续编号交叉验证总数 150，无断号、无重号。
- **范文 167 字（从印刷范文复数，非只信源码）**：P8 H 区印刷范文 6 行（`例：` 起）重组后，
  去 `例：` 前缀的正文为：
  > 私の11月の週末は、文化と紅葉の週末です。火よう日は、家族と金沢へ行きます。伝統工芸展とライトアップを
  > 見たいです。土よう日は、友達と神戸へ紅葉を見に行きます。夜は、ライトアップを見ます。日よう日は、図書館で
  > 借りた本を読みます。読書週間も終わりますから、静かな場所で大きな冒険をしたいです。11月は短いですが、
  > 楽しいことが多い季節です。
  字符数（含标点）= **167**（含 `例：` 则为 169；去标点则为 152，均非 167 的口径——167 口径为
  正文含标点字符数）；6 行在核心与本版中逐字相同；题干 `『私の11月の週末』について、150〜200字で書いてください。`
  亦逐字相同，167 落在 150–200 范围内。
- **ABSTRACT**：德语单行（329 字符，末尾换行符 1 个，无 ASCII 双引号 `"`）：
  > Lucerna Japanisch lernen: Die VOL.2-Ausgabe für deutschsprachige Leser mit 150 Übungen auf A2–B2 —
  > Kulturtag am 3. November, Herbstlaub am Wochenende vom 7. bis 8. November, Lesewoche bis 9. November,
  > Japan Series in Yokohama und sanftes Winteressen: Japanisch lesen und üben mit Texten auf Japanisch
  > und Erklärungen auf Deutsch.
  含刊名 Lucerna、VOL.2、目标语 Japanisch、读者母语 deutschsprachig、级别 A2–B2、题量 150；
  真实主题关键词（Kulturtag、Herbstlaub、Lesewoche、Japan Series）与学习者搜索短语
  （`Lucerna Japanisch lernen`、`Japanisch lesen und üben`）齐备。
- **图片**：`<image>` 载荷逐页 = 核心——P1 1 张、P3 1 张、P4 1 张、P5 1 张，其余页 0 张，共 4 张；
  每张的 href base64 载荷 SHA-16 与核心逐一相同，x/y/宽/高亦相同（P1 65/1874/896×320、
  P3 1451/200/434×222、P4 1451/200/434×290、P5 1451/200/434×262）。
  署名在版且与核心逐字相同：P1 `写真：Poliphilo — CC0（Wikimedia Commons）`、
  P3 `版画：歌川広重（三代）— パブリックドメイン（Wikimedia Commons）`、
  P4 `写真：Syced — CC0（Wikimedia Commons）`、P5 `写真：Petr Kratochvil — パブリックドメイン
  （Wikimedia Commons）`。均为公有领域/CC0，无版权问题。
- **PDF**：印刷 PDF 8 页（28,803,270 字节）、web PDF 8 页（3,099,512 字节，<10 MB），页数与 SVG 一致。
- **跨版干扰**：见结论末尾单列注记（JA×EN 英文措辞变动对本版无影响）。

## 非阻塞观察（单列，不构成放行障碍）

- **O1 — KIT 表述须随 B1 一并更正**：KIT 现称“P8 提示纯德语”“150 条皆为德语提示”，
  与实测（149 德语 + #37 中文）不符；KIT 的 keydiff 小节称“伪影 17 项”但实际列出 18 项，
  且 #140 被双重计数（既列入“提示本地化 2 项”又列入伪影）。KIT 本身为工作文档，
  不单独构成版面阻塞，但 B1 修复时须同步更正上述表述，否则 KIT 将继续作伪证。
- **O2 — P1 中栏墨迹左止 643.2 vs 构建员称 643.1**：0.1 取整差异，无碰撞、无影响。
- **O3 — gloss 重组拼接假象**：见第 4 项附注；卡片目视已确认词头与释义视觉分离。
- **O4 — KIT 的 Sunday 字样**：见第 5 项末尾；属文档记述，非版面残留。
- **O5 — W43“括号体”措辞**：见第 10 项末尾；本版答式以核心破折号体实测为准，无问题。
- **O6 — 换行碎片**：P7/P8 的个别换行碎片（如 P8 #140 的 `(Kobe-Beleuchtung)` 续行）在卡片上
  位置正常，无溢出（occlusion 0 旗佐证）。

## 证据文件（本目录）

- `REPORT.md`（本文件）
- `p8-keydiff-table.md`（P8 keydiff 21 项逐项印刷行对照 + 唯一相同段 #37）
- `gloss.json`（渲染 gloss 39 项逐页 1:1 对照）
- `freeze-baseline.json`（核心基线 8/8）、`freeze-diff.json`（核心→本版逐页增删串 + CJK 计数）
- `p8-compare.json`（P8 CLEAN 150=150 + keydiff 21 项）、`occlusion-ed.json`（本版 0 / 核心 0 / NEW 0）、
  `occlusion-core.json`（核心 0）
- `sha256-before.txt`、`sha256-before2.txt`（90 秒静默复查）、`sha256-after.txt`（校对后，diff 为空）、
  `sha256-core.txt`、`sha256-core-after.txt`（核心无变动）、`sha256-w43.txt`（W43 对照哈希）
- `ed-scratch-sha.txt`（proof 内重跑本版构建的 SVG 哈希，与终态逐字节一致）
- `freeze-out/`、`ed-build-copy/`、`ed-scratch-svg/`（proof 内重跑产物，未写入交付目录）
