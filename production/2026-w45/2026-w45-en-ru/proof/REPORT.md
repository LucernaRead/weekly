# 独立校对报告 — Lucerna Weekly W45 EN×RU 分版

- 校对对象：`files/weekly-report-w45-en-ru/`（svg×8、cards×8、print/web 双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照基底：`files/weekly-report-w45-en-core/`（VOL.2，刊头 The Lucerna）
- 家具对照：`files/weekly-report-en-ru/`（W43 EN×RU 已上架版）、`files/weekly-report-w45-en-es/`（W45 EN×ES）
- 校对方式：只读校对。未改任何源码/交付物，未发 Discord，未往主聊天发卡片/PDF，未建 cron，未碰 weekly-git，未改核心与 W43 目录，未清理共享 scratch。未派生下级代理。
- 证据目录（本目录）：`diff-proof.json/txt`、`p8-compare.json/txt`、`p8-core-extract.json/txt`、`p8-edition-extract.json/txt`、`occlusion-proof.json/txt`、`occlusion-core.json/txt`、`freeze-baseline/`（基线复现输出）。其余过程输出见校对员 /tmp 过程文件（diff-adjudge、pixel-textx、freq-counts、gloss-counts、svg-ex-counts、r1-flags、w43-furniture、shortforms-credits），关键结论均摘录于下。

## 结论：ZERO PROBLEMS（版面零阻塞项）

非阻塞观察 2 项（见文末），均不涉及版面本身；上架与否由主线串行决定，本报告不宣布上架。

## 0. 开工查重与哈希基线

- 开工时无进行中的渲染/写盘进程（`ps` 无 python/render/transform 进程）；交付物 mtime 在 75 秒复查窗口内零变化，属已完成交付的新鲜 mtime，安全开工，未 stand down。
- 校对前记录全部交付物 + 核心 sha256；校对后复核：**交付物不变、核心不变**（两次 diff 均无差异）。
- 交付物哈希（校对前后一致）：
  - print PDF `The-Lucerna-VOL2-RU.pdf`：17,213,550 B，`6e2d9a37cd638df74ef356db835b29a3ce3ed486cdb9e6afada84c3105e55938`（与任务书/KIT 一致）
  - web PDF `The-Lucerna-VOL2-RU-web.pdf`：4,026,624 B，`e6d78a24f161218885a21860c246cd6351cfadd439acd7054db97fc9d5b0456d`（与任务书/KIT 一致）
  - svg：p1 `d77860b7…fb2ea66e`、p2 `81c7d8d5…6d9c`、p3 `0e2440e8…11ef88`、p4 `017b588c…45651`、p5 `c36f71da…fe816`、p6 `a28a5f98…b169b`、p7 `8ae02622…3a56f`、p8 `9a6450a5…83dfa5f`（完整值见校对前记录）
  - cards：p1 `1f8fbbe1…`、p2 `56742143…`、p3 `901ee242…`、p4 `4cf5cb9a…`、p5 `343a1efa…`、p6 `3afa0144…`、p7 `bf98b4e1…`、p8 `5f3990ad…`（完整值见校对前记录）
- 当前交付物 = R3-post 基线 18/18 OK；R3-pre 基线复核：恰 4 项 FAILED（p1 svg、p1 card、双 PDF），其余 14 项 OK。

## 1. 冻结

- `freeze.py baseline` 独立重跑：**8/8 逐字节复现**（p1 `c7e7d019…`、p2 `07f5df7e…`、p3 `d9f7cc37…`、p4 `3b8be517…`、p5 `73486e2f…`、p6 `3e2187b3…`、p7 `5a268409…`、p8 `4de34a13…`，与 shipped 核心一致；运行前后核心重哈希不变，核心未动）。
- `freeze.py diff` 独立重跑：8 版新增 CJK 字符均为 0（版面 CJK 全 0）；核心 CJK 逐版清零（P1 183→0、P2 197→0、P3 119→0、P4 139→0、P5 134→0、P6 136→0、P7 347→0、P8 776→0，按 diff 口径）；我方第二种口径（text 元素内 CJK 计数）亦为 8 版全 0。
- 被删串逐项裁定（diff 多重集，纯拉丁无 CJK 的被删串）：
  - P1：仅 2 条——刊头标语 `THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA`（徽章替换，W43 家具）与数字框行段 `· Nov 8 — NFL in Madrid + F1 in São`（重排伪影：内容以 `F1 in São Paulo (два больших матча в…)` + `премьеры) · Nov 8 — NFL in Madrid +` 两段在新增串中重排出现）。
  - P2–P6：纯拉丁被删串 0 条。
  - P7：纯拉丁被删串仅 `。` 1 条（中文句号残片，讲解层标点）。
  - P8：纯拉丁被删串 14 条，全部为键区行段重排伪影（词级重现率 8–10/10；p8.py 按题号比对证实键内容除 5 项 keydiff 外逐项相等，见 §2）。
  - 其余被删串均为含 CJK 的讲解层（纯中文或中英混合），属中→俄讲解替换，合法。
  - 结论：被删英语串确仅三类（徽章替换 + 重排伪影 + P7 中文句号残片），构建员自述属实。
- 违禁词：svg/ + KIT + ABSTRACT 全量 grep **0 命中**（任务书指定词，本文不拼写）；transform 后源码 CJK 0、全角竖线 0 的自述与交付物实测一致（交付物侧已验证）。

## 2. P8（显式双路径 compare 独立重跑）

- 核心 P8 印刷笔记计数口径独立确立：`p8.py extract --p8 核心` 实测 **78 noted**（非 150；150 为全期题数，任务书“150=150”确为口径混淆，构建员的口径修正正确）。
  - 核心印刷集（78）：[11, 12, 14, 19, 29, 30, 31, 33, 41, 44, 47, 48, 51, 58, 64, 66, 67, 68, 69, 71, 74, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 100, 102, 107, 108, 109, 110, 111, 112–150]。
  - 其中 P1–P7 印刷笔记 39 项（= W43 PRINT_NOTES 显式集合）；P8 自身电池 112–150 共 39 项；39 + 39 = 78。
  - W45 EN×ES 实测印刷集与上述 78 项逐项相同，钉住集一致性属实。
- `p8.py compare`（显式双路径）：**CLEAN，78 = 78，missing=[]，extra=0，uncertain=[]，keydiff=[137, 138, 139, 140, 150]**。
- keydiff 逐项印刷行对照与合法性裁定（键按 p8 extract 提取值）：
  - 137：题面英语指令 `Translate : « Patience is part of the system, … »` 冻结保留；键 核心中文译文 → 本版 `Терпение — часть системы, а не её провал.`。合法（英→俄方向重定向）。
  - 138：题面母语指令 `翻译：` → `Переведи:`；题干英语句 `Tuesday, November 3, is Election Day in the United States.` 逐字冻结；键 → `Вторник, 3 ноября, — день выборов в США.`。合法。
  - 139：题面母语指令 `翻译：` → `Переведи:`；题干英语句 `On Sunday, the NFL plays in Madrid.` 逐字冻结；键 → `В это воскресенье NFL играет в Мадриде.`。合法。
  - 140：题面英语指令 `Translate : « Not every place changes. »` 冻结保留；键 → `Не везде часы переводят назад.`。合法。
  - 150：写作题键为讲解层文字：核心 `开放题 — 要点见写作框，范文在第8 版写作框内` → 本版 `Открытый вопрос: критерии — в рамке сочинения; образец — в рамке на этой странице`。合法（同 W43 EN×RU 写作题键重定向一类）。
  - 其余 145 键与核心逐项一致（extract 键表比对）。
- P8 注释纯俄语：P8 SVG 全量 CJK 0；键区 102 行 CJK 0、西里尔字母存在；括号体：本版 P8 全角括号 0、半角括号 194（核心为全角 164），与 W43 RU 家族写法一致。
- P8 印刷笔记集合相等：是（compare CLEAN + 两侧 extract 集合逐项相同）。

## 3. 金句级别清单 7-vs-8 差异专项（裁定：交接笔误，非阻塞）

- 从核心独立实测 8 句金句（P7 顺序）及级别：
  1. `Tuesday, November 3, is Election Day in the United States.` (page 1) — A2
  2. `The hour from 1 to 2 happened twice.` (page 2) — A2
  3. `Which film would you choose ?` (page 3) — B1
  4. `Two games, two continents, one league — that is the modern NFL.` (page 4) — B1
  5. `The results will still be there in the morning.` (page 5) — B2
  6. `Patience is part of the system, not a failure of it.` (page 6) — B2
  7. `Not every place changes.` (page 2) — A2
  8. `One Sunday is not enough — good thing the week has seven days.` (page 4) — B1
- 核心级别序列（8 项）：**[A2, A2, B1, B1, B2, B2, A2, B1]**。
- 本版级别序列（8 项，逐项核对 P7 金句区级别标签）：**[A2, A2, B1, B1, B2, B2, A2, B1]，与核心逐项一致**。
- 构建员 KIT §七所列 7 项 `[A2, A2, B1, B1, B2, A2, B1]` 漏掉了第 6 项 B2（Patience 句）。版面本身 8 句齐全（P7 金句区 105. Patience 项在位，级别 B2），故为 **KIT 文字交接笔误，非真实缺失，非阻塞**（见文末观察 1：定稿时 KIT 该行应补为 8 项，版面不动）。

## 4. 几何

- `occlusion_audit.py` 自检先行通过（planted 6 类全触发，clean 对照静默）。
- 独立重跑：**分版 1 / 核心 0 / NEW 1**，唯一标记 P1 刊头 TEXTX（`The Lucerna` 墨迹框 [557.9, 141.8, 1392.1, 291.2] 与刊头行墨迹框 y 向交叠 6.0px），与构建员自述逐字一致。
- P1 刊头 TEXTX 独立像素级验证（自写 PIL 双串重绘，未采信构建员结论）：
  - 审计式墨迹框复现：刊名 [557.9, 141.8, 1392.1, 291.2]；刊头行 [135.1, 285.2, 1814.9, 340.0]；框级 y 交叠带 285.2–291.2。
  - 2× 像素掩码 AND：**重叠像素 0**；共享带内逐行核查：刊名墨迹仅为 x≈702–711 的单笔竖画（y 285.5–289.5），刊头行墨迹在同行仅位于 x≤487，两者 x 向间隔约 215px，无交集。
  - 实际渲染卡片 p1-front.png 地面实况一致：y=286–289 行刊名笔触 x≈702–707、刊头行笔触 x≤483，互不相交；y=294 为空行。
  - 裁定：**框级伪报，非缺陷**。同类先例已验证：W45 EN×ES 亦仅此 1 项 TEXTX（834.2×6.2px）；W43 EN×RU 已上架版亦含同款刊头 TEXTX（834.2×6.0px）。
- 同基线行查（supplemental.py rowcheck，解码后测量）：**0 碰撞**。
- P6 图表覆盖（基线锚定墨迹法，PIL getmetrics，anchor ls）：4 条标签行 + 导读行覆盖均为 **0.0%**，最差 0.0%（门限 <30%）。
- 全 8 页框线压框 + 右缘扫描（ADVANCE 法，supplemental.py edgescan）：**0 标记**；P1–P7 最大 advance 右缘均为 1885.0；P8 1903.8 仅来自两条冻结 F 配对右项（`b. an election in the middle of a term` 1899.4、`d. the paper you mark your choice on` 1903.8），与核心同款（核心 edgescan 行为一致，墨迹未触内框线 1910）。
- R1 的 27 NEW 旗标终态核查（逐项对照 occlusion-round1.json 与终态审计）：
  - 26 项已消除（含 P2 FOOTER/LINEX/EDGE 级联、P3/P4/P5/P6 BOXTITLE、P6 TEXTX 级联、P8 LINEX、P1 暗带 TEXTX 与数字框 LINEX 等）。
  - 剩余 1 项即 P1 刊头 TEXTX——它本身就是 R1 27 项之一，终态未“消除”而是经像素级验证裁定为伪报（见上）。表述修正：26 消除 + 1 伪报裁定，非 27 项全部消除；不构成阻塞。
- R3 变化范围验证：R3-pre→R3-post 基线复核恰 4 项变化（p1 svg、p1 card、双 PDF），其余 7 页 svg/card 字节不变；当前交付物 = R3-post 18/18 OK。构建员“仅 P1 svg/card + 双 PDF 变化”属实。

## 5. gloss（渲染后 · 拆分，独立实测，不照搬构建员分布）

- 从核心 content 源码 gloss() 串实测：P2 3 项、P3 4 项、P4 4 项、P5 3 项、P6 4 项，合计 18。
- 从本版 content 源码 gloss() 串实测：P2 3 项、P3 4 项、P4 4 项、P5 3 项、P6 4 项，合计 18。
- 分布 **3/4/4/3/4（P2/P3/P4/P5/P6），核心 = 本版 1:1**；英语词头逐项同序一致（to fall back、a costume、trick or treat；to open、a monster、a catchphrase、a series；a fixture、a title、to defend、a fan；a map、too close to call、a second screen；to register、a governor、to shape laws、patience），仅释义本地化 + 前缀 `讲解｜`/`译注｜` → `Пояснение — `。
- 渲染侧佐证：5 版词框首行均以 `Пояснение — ` 起始。

## 6. P7

- 定义句逐字保留：P7 四栏（A2 FALLING BACK / GOING TO + VERB、B1 COMPARATIVES / THE PAST SIMPLE、B2 HEADLINE PRESENT / WHETHER = IF ?）及三级例句框英语正文与核心逐行一致；B2 例句框定义句 `« Patience is part of the system, not a failure of it. » — part of = часть (page 6).` 仅释义本地化（核心为 `一部分`），定义句原文逐字保留。
- 金句 8 句原文逐字保留（见 §3 清单），级别序列核心 = 本版（8 项）。
- P7 内句频：7 句各 1 次，Patience 句 2 次（金句区 + B2 例句框），与核心一致。
- 全期句频（8 版全文归一化检索，核心 = 本版逐句相等）：5 句 2×（hour-twice、which-film、two-games、results-morning、one-sunday，文章 + P7）；Tuesday 句 3×（P1 文章 + P7 + P8 E-138 题干）；Not every 句 3×（P2 文章 + P7 + P8 E-140 题干）；Patience 句 4×（P6 文章 + P7 金句区 + P7 例句框 + P8 E-137 题干）。
- P7 结构：栏序与核心一致——A2/B1/B2/工具箱、金句区（句 + 语法点 + 跟练 100–107）、易错诊所 4 题（108–111）、读者园地、VOL.3 预告；栏头序列 13 项同序（仅后缀本地化）。

## 7. 读者园地

- 英语信件段逐字冻结（核心 P7 147–149 行 = 本版 156–158 行）：
  - `« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)`——逐字一致，无改动。
- 俄语披露句逐字摘录（本版 P7 159–163 行）：
  - `Примечание редакции: в VOL.1 было обещано публиковать настоящие письма в VOL.2, но к сдаче номера редакция не получила ни настоящих писем, ни лучшего сочинения с 8-й страницы VOL.1; мы ничего не выдумываем, а пример остаётся помеченным. Присылайте ваши письма и сочинения! В VOL.3 мы опубликуем полученные письма.`
- 逐项核实：
  - 事实 1（无真实来信）：`не получила ни настоящих писем` ✓
  - 事实 2（无 VOL.1 第 8 版最佳作文）：`ни лучшего сочинения с 8-й страницы VOL.1` ✓（覆盖范围显式裁定：指 VOL.1 当期第 8 版写作栏的最佳作文，与协调员裁定措辞一致）
  - 事实 3（示例保留标注 + 刊登承诺顺延 VOL.3）：`пример остаётся помеченным` + `В VOL.3 мы опубликуем полученные письма` ✓
  - 显性祈使句征集邀请：`Присылайте ваши письма и сочинения!` ✓（祈使句；内容预告行 NEXT WEEK 未计入邀请）
  - VOL.3 刊登承诺：`В VOL.3 мы опубликуем полученные письма` ✓
  - 无编造：未新增读者/来信/姓名/引言；未凭空新写英语披露句（本版无新增英语披露句，英语部分仅冻结信件段）。
- 披露句盒内无溢出：卡片目视读者园地框完整，披露句末行距框底有空隙；occlusion 全页 0 追加标记。

## 8. 家具（W43 偏差清单逐项核实）

- 徽章标语槽：本版 P1 `y=372、19.5pt、粗体、砖红 #a4553a、居中`，与 W43 EN×RU 同槽同属性逐项一致（W43 同槽文本亦为 `ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`）；刊头行 `АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · ВЫБОРЫ · ФУТБОЛ · КИНО`（VOL.1→VOL.2 为刊期更替）。
- 页脚：8 版 `The Lucerna · АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ`，与 W43 同式（仅 VOL.1→VOL.2）。
- 页码行：8 版 `Страница N из 8`，与 W43 同式。
- 词框前缀：5 版均为 `Пояснение — `，与 W43 同式；核心 `译注｜`/`讲解｜` 已去除。
- P8 分隔：8 项 `— СТРАНИЦА N —`（全大写），与 W43 同式。
- 半角括号键体：本版 P8 全角括号 0、半角括号 194，见 §2。
- P7 语法点前缀：本版 8/8 为 `Грамматика — `；W43 EN×RU 金句槽亦为 `Грамматика — `（8 项实测）；族内依据：W45 EN×ES 同槽用 `Nota — `（实测 3+ 项，零 `Грамматика`），故俄语族取 `Грамматика — `、不用西语族 `Nota — `，成立。
- P8 栏头 W43 短式：A–H 与 W43 逐项相同，唯 H 栏头保留核心原有 `[B1]` 标记（`H · WRITING · Письмо [B1]`，核心同款标记）。
- P8 PRINT_NOTES 显式集合：39 个 P1–P7 题号与 EN×ES 钉住集逐项一致（见 §2）。
- 其余俄语短式化（在框验证：occlusion BOXTITLE 0 标记 + edgescan 0 标记 + 卡片目视在框）：
  - P1 数字框题 `THE WEEK IN NUMBERS · Цифры`、热搜副题 `Что ищут в США · Google Trends`（去 `Снимок…`）、暗带副题 `Вторник — выборы · Часы переведены`、P3 `AT HOME THIS WEEK · Дома`、P4 `SUNDAY, NOVEMBER 8 · Воскрес.`、P5 `TOO CLOSE TO CALL · Равная` 与 `FIVE SENTENCES · Пять фраз`、P6 `A PRACTICE BALLOT · Бюллетень` 与 `READ THE CHART · График`、P1 数字框注释短句——均在框，无 BOXTITLE/EDGE 标记。
  - 注：P5 `Равная` 为 `Равная борьба` 的截短式；完整短语 `слишком равная борьба, итог неясен` 在同版词框释义中完整出现，语义未丢失。
- P8 §E 间距 11→4：终态 P8 电池区底线 1376（< 1485 底线，build-round3.log 实测），P8 卡片目视电池区与键区之间有空隙，无 LINEX 残留。

## 9. 图片、ABSTRACT、卡片、题量、PDF

- 图片载荷：5 张图逐页相等（载荷 sha16 与几何 x/y/w/h 均与核心一致）——P1 投票亭、P2 1912 万圣节明信片、P3 Manet 猫插画、P4 1910 橄榄球、P6 国会大厦；P5/P7/P8 无图（与核心一致）。
- 署名在版：图注署名行核心 = 本版逐行一致——P1 `Kenneth C. Zirkel — CC0, via Wikimedia Commons`、P2 `Public domain, via Wikimedia Commons`、P3 `Édouard Manet — CC0, via Wikimedia Commons`（+ `illustration by Édouard Manet for « The Cats »`，含“不是电影剧照”说明）、P4 `Frank R. Snyder — public domain, via Wikimedia Commons`、P6 `Public domain, via Wikimedia Commons`。
- ABSTRACT.txt：俄语单行（319 字符，1 个换行符为行尾符），无 ASCII 双引号；含刊名 The Lucerna、目标语 английский、读者 русскоязычные、真实主题关键词（3 ноября中期选举、1 ноября拨钟、Хэллоуин、6 ноября电影首映、8 ноября NFL 马德里赛、美国投票制度）、学习者搜索短语 `учи английский по настоящим новостям`、A2–B2、150 упражнений。
- 8 卡片逐页目视：P1 刊头/暗带/数字框/热搜框/词框/快讯/闪电问答干净；P2 AND YOU 盒俄语 2 行盒内、时钟栏、练习区干净；P3 居家框/猫帽框/影评桥段干净，C 栏头孤悬第 2 栏底为核心同款继承布局（无重叠，审计 0 标记）；P4 周日赛程框/马德里框/词框干净；P5 难分胜负框/词框/投票结束桥段干净；P6 模拟选票框（☐ 为与核心一致的选票框选字符，非缺字）/图表标签 4 行/教学数据声明/任期框干净；P7 四栏/金句/诊所/园地/预告干净；P8 电池 A–H/写作框/范文/Levels 行/键区 1–150 干净，键区末行距页脚线有空隙。
- 题量与级别（从 shipped SVG 独立展开计数，非照搬登记表）：
  - 练习头标配对计数：P1–P7 + P8 头标 = 136 项（P1 10、P2 17、P3 18、P4 18、P5 18、P6 18、P7 12、P8 头标 25），编号连续无缺重；
  - 无头标的 14 项以电池定义核实：A 完形 112–119（A2×5 + B1×3）、G 对话 145–149（A2×4 + B1×1，Levels 行明示）、H 写作 150（B1）；136 + 14 = **150 题**；
  - 级别合计：**A2 60（头标 51 + 9）、B1 69（头标 64 + 5）、B2 21（头标 21 + 0）**；页分布 **10/17/18/18/18/18/12/39**；与核心 shipped SVG 计数逐页逐级相同。
- 范文 85 词：MODEL 段核心 = 本版逐字相同，分词计数 85（`On Tuesday, November 3, our family watched … and a very American one.`）；渲染侧 MODEL 行与核心同断行。
- 双 PDF：各 8 页（/Count 8，页面对象 8 个），字节数与 sha256 与 KIT 一致（见 §0）；web 版 4,026,624 B < 10 MB。
- 构建警告终轮：build-round3.log FLOW OVERFLOW 0 语义（各流终点：P1-headline 1502、P2-ex 2532、P8-battery 底线 1376、P8-keys 2167，均在底线内）；HEAD TOO WIDE 未出现。
- 解释器：未重跑构建（只读校对），但核查 run.py/render.py 均指向 tools/venv/bin/python（Python 3.12.3，PIL 13.0.0，实测）；系统 python3 无 cairosvg 的自述与本机环境一致（未使用系统解释器）。

## 非阻塞观察（不构成阻塞项）

1. **KIT §七金句级别清单笔误**：KIT 写 `[A2, A2, B1, B1, B2, A2, B1]`（7 项），漏第 6 项 B2；版面实测为 8 项且与核心逐项一致。定稿时 KIT 该行应补为 `[A2, A2, B1, B1, B2, B2, A2, B1]`；版面不动。
2. **R1 27 旗标表述修正**：终态为 26 项消除 + 1 项（P1 刊头 TEXTX）像素级伪报裁定，而非 27 项全部消除；KIT §十 R2 句“仅剩刊头 TEXTX（像素裁定为非缺陷）”本身已准确，本观察仅针对任务书“逐项确认消除”的措辞作精确化，不影响 verdict。
3. （说明，非问题）P5 `TOO CLOSE TO CALL · Равная` 为截短式，完整语义在同版词框中保留；P3/P5 栏头孤悬为核心同款继承布局；P8 两条 F 配对右项 advance 1903.8 为冻结英语原文核心同款；三者均非本版缺陷。

## 未做事项（按任务约束）

未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未清理共享 scratch 目录、未派生下级代理、未宣布上架。
