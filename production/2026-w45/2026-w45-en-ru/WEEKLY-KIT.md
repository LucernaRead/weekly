# WEEKLY KIT — The Lucerna · ENGLISH WEEKLY VOL.2 · EN × RU edition (W45)

**Status: builder-complete, NOT finalized.** All builder gates below are measured
green. Finalization requires an independent proofread round (zero problems) by a
separate proofer — this report does not claim it. No Discord post, no chat
delivery, no repo insert, no cron was made under this task.

## 一、交付物

`files/weekly-report-w45-en-ru/`：

- `svg/` — 8 pages of SVG sources (p1-front … p8-exercices)
- `cards/` — 8 full-page PNGs, 1950×2700 (all 8 visually inspected, §八）
- `The-Lucerna-VOL2-RU.pdf` — merged 8-page print PDF, **17,213,550 bytes**,
  sha256 `6e2d9a37cd638df74ef356db835b29a3ce3ed486cdb9e6afada84c3105e55938`
- `The-Lucerna-VOL2-RU-web.pdf` — compressed 8-page PDF, **4,026,624 bytes**
  (< 10 MB), sha256 `e6d78a24f161218885a21860c246cd6351cfadd439acd7054db97fc9d5b0456d`
- 本文件 + `ABSTRACT.txt`（俄语单行、无 ASCII 双引号，见 §九）

构建代码在 `hidden_files/weekly-report-w45-en-ru-build/`：`transform.py`
（核心 → 分版的全部替换，逐项断言出现次数；修复轮只改它，不手改 content）、
`run.py`（单进程 driver）、`render.py`（核心配方）、`supplemental.py`
（同基线行查 + P6 图表查 + 右缘/框线查）、各轮基线与审计输出（另有
`hidden_files/w45-en-ru-round-baselines/` 存各轮前后 sha256）。

## 二、基底与规格

- 基底：W45 EN 核心 `files/weekly-report-w45-en-core/`（VOL.2，刊头
  The Lucerna，2026 年 11 月 2–8 日当周，刊期 2026-w45）。
- 8 版，1950×2700，四栏，暖象牙底、深橄榄点缀，哥特体刊头 The Lucerna。
- 英语正文冻结；讲解层全部俄语；全文 CJK 字符 0（§七）。
- 家具以 W43 EN×RU 已上架版为准（胜过 README #20 的泛化规则），登记见 §三。

## 三、家具登记（W43 EN×RU 已上架版实测）

- 刊头标语位（y=372，19.5pt 粗体砖红，替换核心 strapline）：
  `ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`
- 刊头行：`АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · ВЫБОРЫ · ФУТБОЛ · КИНО`
- 顶栏：`WEEKLY IN ENGLISH · КАЖДУЮ НЕДЕЛЮ · АНГЛИЙСКИЙ, КОТОРЫЙ ЧИТАЕТ АМЕРИКА`
- 页脚（8 版）：`The Lucerna · АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА
  АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ`
- 页码行：`Страница N из 8`
- 词框前缀：`Пояснение — `（bslib4 gloss，核心 `译注｜` + 内容层 `讲解｜` 均已去除）
- P7 语法点前缀：`Грамматика — `（W43 EN×RU 栏标准，见 §十 D3；非西语族的 `Nota — `）
- P8 分隔：`— СТРАНИЦА N —`（全大写，W43 RU 栏标准）；P8 印刷键括号：半角
  ` (note)`（空格 + 半角括号，W43 EN×RU 家族写法；核心为全角）
- P7 栏头：`LEVEL A2 · База` / `LEVEL B1 · Средний` / `LEVEL B2 · Сложный` /
  `THE EXAMPLE · Пример` / `THE TOOLBOX · Инструменты` /
  `PHRASES OF THE WEEK · Фразы недели` / `THE ERROR CLINIC · Ошибки` /
  `READERS' CORNER · Уголок читателя` / `NEXT WEEK · VOL.3 · Анонс` /
  band `LANGUAGE IN HAND · Разбор`
- P8 栏头（W43 短式）：`A · CLOZE · Пропуски` / `B · MULTIPLE CHOICE · Выбор` /
  `C · READING · Понимание текста` / `D · SENTENCES · Предложения` /
  `E · TRANSLATION · Перевод` / `F · WORDS · Пары слов` /
  `G · DIALOGUE · Диалог` / `H · WRITING · Письмо [B1]`（[B1] 为核心原有标记，保留）
- 练习内小标签：`Заполни` / `Перепиши` / `Подбери пары` / `Исправь`
- 类型登记（仅登记表，不印版面）：完成句子→Дополнить предложения，单选→Выбрать
  ответ，句型转换→Перестроить，词汇配对→Подобрать пары，完形填空→Заполнить
  пропуски，阅读理解→Понять текст，翻译→Перевести，对话补全→Дополнить диалог，
  写作→Сочинение，改错→Исправить，图表读数→Прочитать диаграмму，跟练→Потренироваться
- 俄语目标语名表（W43 EN×RU KIT §3，唯 nl 一项按 NL×RU 裁定用 ГОЛЛАНДСКИЙ，
  本版目标语为英语，不受影响）：en АНГЛИЙСКИЙ / НА АНГЛИЙСКОМ。

## 四、八版内容（英语正文与核心一致，仅讲解层本地化）

| 版 | 内容 |
|---|---|
| P1 头版 | 头条中期选举日预览（众议院 435 席全改选、参议院约三分之一、州长；提前投票、计票需时）；本周热搜图（10 月下旬快照、非精确搜索量）；目录；本周词 midterm；投票亭照片；快讯；闪电问答。10 题 |
| P2 生活 | 11 月 1 日周日拨回时钟（25 小时之夜；亚利桑那与夏威夷不拨钟）；10 月 31 日周六万圣节（已过去事件）；11 月 6 日电影预告；报时专栏（1:00 / 1:30 / 7:45）；1912 万圣节明信片图。17 题 |
| P3 文化 | 11 月 6 日周五上映 « The Cat in the Hat » 与 « Godzilla Minus Zero »；居家一周（Netflix 11 月 4/5/6/8 日档期）；五句影评法；Manet 猫插画图（图注说明不是电影剧照）。18 题 |
| P4 体育 | 11 月 8 日周日 NFL 第 9 周马德里赛 + 海豚–雄狮；F1 圣保罗大奖赛；NASCAR Homestead-Miami；WTA 年终总决赛印第安维尔斯开赛；拳击阿灵顿；11 月 7 日周六 MLS 赛程；1910 年橄榄球照片。18 题 |
| P5 青年 | 选举之夜在家（地图、手机第二屏、披萨）；« Too close to call » 教学；11 月 7 日 MLS 预热。18 题 |
| P6 深读 | 美国投票制度（一国五十套选举制度；众议员 2 年、参议员 6 年约三分之一改选、州长）；模拟选票（候选人仅用代号）；教学图表 « WHY DO VOTERS VOTE EARLY ? »（38/29/21/12，合计 100，版面明确标注为教学数据、非真实民调）；国会大厦图。18 题 |
| P7 精讲 | A2/B1/B2 三级专栏 + 工具箱 + 本周金句 8 句 + 易错诊所 4 题 + 读者园地 + VOL.3 预告（11 月 11 日退伍军人节、11 月 15 日 NFL 慕尼黑赛、中期选举结果报道）。12 题 |
| P8 评估 | 完形 8 + 单选 9 + 阅读 4 + 完成句子 4 + 翻译 4（英↔俄，见 §六）+ 词汇配对 4 + 对话补全 5 + 写作 1（« My Tuesday, November 3 »，80–100 词，范文 85 词）。39 题 + 全部 150 题答案与简析 |

图片：assets/ 自核心构建目录原样复制（5 张 Wikimedia Commons 公版/CC0 图，
出处图注为冻结英语，与核心一致）；卡片目视已核对 5 图均在位。

## 五、实测体量（登记表独立展开计数，与核心一致）

- **练习总量：150 题**（统一编号 1–150，连续无缺重）
  - 按难度：**A2 60 · B1 69 · B2 21**
  - 按版：P1 10 · P2 17 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 39
    （P2 17、P8 39 为本核心实测值，不同于通用 10/18/18/18/18/18/12/38）
  - 按题型（俄语登记标签）：Дополнить предложения 33 · Выбрать ответ 41 ·
    Перестроить 16 · Подобрать пары 20（5 组）· Прочитать диаграмму 6 ·
    Потренироваться 8 · Исправить 4 · Заполнить пропуски 8 · Понять текст 4 ·
    Перевести 4 · Дополнить диалог 5 · Сочинение 1
  - P8 正式评估 39 题，其余 111 题为 P1–P7 即学即练。
- 范文 85 词（冻结 MODEL 段实测分词计数，与核心一致）。
- 词框：gloss() 串按 `·` 拆分，核心 18 = 本版 18，逐框分布 3/4/4/3/4
  （P2/P3/P4/P5/P6），英语词头逐项一致，仅释义本地化。

## 六、P8 门禁（tools/p8.py compare，显式双路径形式）

- 印刷笔记集合：**CLEAN，78 = 78**，missing=[]，extra=0，uncertain=[]。
  （注：78 是核心 P8 实际印刷笔记数，非全期题数 150；任务书的 “150=150”
  系把全期题数与印刷笔记数混淆，实测门禁为印刷集与核心逐项相等，见 §七。）
- 印刷集相等靠显式 `NOTAS_EXTRA` 钉住（P1–P7 练习题的印刷笔记集；W43 EN×RU
  PRINT_NOTES 同类修复先例，39 个题号与 EN×ES 版钉住的集合完全一致）：
  俄语笔记长于中文笔记适用的 `len ≤ 10` 规则，若沿用原规则将漏印——本版条件改为
  `pg == 8 或题号 ∈ NOTAS_EXTRA`，集合与核心逐项相等。
- keydiff = **[137, 138, 139, 140, 150]**，逐项裁定如下（其余 145 键与核心
  逐字节一致；键按题号提取比对，不按行位置比对，故键区重排只产生伪影，
  不产生 keydiff）：
  - 137：核心键为英文句 « Patience is part of the system, not a failure of
    it. » 的中文译文 → 本版俄语译文 « Терпение — часть системы, а не её
    провал. »；题面英语指令 `Translate :` 保留（与核心一致）。
  - 138：核心键为 “Tuesday, November 3, is Election Day in the United States.”
    的中文译文 → 本版 « Вторник, 3 ноября, — день выборов в США. »；母语指令
    `翻译：` → `Переведи:`。
  - 139：核心键为 “On Sunday, the NFL plays in Madrid.” 的中文译文 → 本版
    « В это воскресенье NFL играет в Мадриде. »；母语指令 `翻译：` →
    `Переведи:`。
  - 140：核心键为 « Not every place changes. » 的中文译文 → 本版
    « Не везде часы переводят назад. »；题面英语指令 `Translate :` 保留。
  - 150：写作题键为讲解层文字（非冻结英语）：核心 « 开放题 — 要点见写作框，
    范文在第 8 版写作框内 » → 本版 « Открытый вопрос: критерии — в рамке
    сочинения; образец — в рамке на этой странице »。
    （同 W43 EN×RU keydiff 中写作题键重定向一类。）
- 核心 P8 含英↔中双向翻译题：137/140 题面为英语指令（冻结保留），138/139
  题面为母语指令（本地化为俄语）；本版方向改为英↔俄，4 项键重定向均合法，
  137/138/139/140 的题干英语句本身逐字冻结。
- P8 注释纯俄语（P8 SVG grep：CJK 0；半角括号体）。

## 七、冻结与全部门禁实测值

| 门禁 | 实测 |
|---|---|
| 核心基线复现（tools/freeze.py baseline） | **8/8 逐字节一致**（`tools/scratch/baseline-w45-en-ru`，8 个 sha256 逐项 OK）；构建后核心 SVG 重哈希与基线完全一致，核心未动 |
| 冻结差分（tools/freeze.py diff，终轮 diff-final.json） | 新增 CJK 0（8 版全 0）；版面 CJK 0；被删英语串仅三类：(a) P1 刊头标语（徽章替换，W43 家具）；(b) 重排伪影（P1 数字框行、P8 键区行段——内容均在新增串中重排出现，键经 p8 逐题号证实）；(c) P7 一个中文句号残片（讲解层标点） |
| 违禁词检查 | svg/ 全量 grep 均为 0 命中（该词按任务要求不在本文中拼写）；transform 后源码 CJK 0、全角竖线 0 |
| 英语正文冻结 | 除上表三类外无英语串被删；P7 词框英语定义句与金句原文逐字保留（见 §八） |
| P8 compare | CLEAN 78=78，keydiff [137, 138, 139, 140, 150]（§六逐项合法） |
| 几何审计（tools/occlusion_audit.py，自检先行） | 分版 1 标记 / 核心 0 / NEW 1——唯一标记为 P1 刊头 TEXTX，裁定为非缺陷（见 §八像素证据）；其余 0 |
| 同基线行查（supplemental.py rowcheck，解码后测量） | **0 碰撞**（分版 = 核心） |
| P6 图表标签覆盖（基线锚定墨迹法，PIL getmetrics，anchor ls） | 最差 **0.0%**（门限 <30%；4 条标签行 + 导读行均 0；分版 = 核心） |
| 全 8 页框线压框 + 右缘扫描（ADVANCE 法） | 0 标记；P1–P7 最大 advance 右缘 1885.0（恰为页边）；P8 1903.8 仅来自两条冻结 F 配对右项（核心同款，墨迹未触内框线 1910） |
| 词框 gloss | 18 = 18（§五） |
| P7 金句 | 8 句原文逐字保留；级别标签 [A2, A2, B1, B1, B2, B2, A2, B1] 与核心一致（2026-10-28 校对后修正：原 7 项漏第 6 项 B2，版面不动）；句频核心 = 分版（见 §八） |
| 题量与级别 | 150；A2 60 / B1 69 / B2 21；分版 10/17/18/18/18/18/12/39（登记表展开计数） |
| 范文 | 85 词，与核心一致 |
| 构建警告（终轮） | FLOW OVERFLOW 0 · HEAD TOO WIDE 0 |
| 卡片目视 | 8/8 逐页目视（§八） |
| ABSTRACT | 俄语单行、无 ASCII 双引号、含真实主题关键词 + 学习者搜索短语 + 刊名 + 目标语名 + A2–B2 + 150 题 |

## 八、P7 专项与目视记录

- **词框硬性门**：三级例句框英语定义句逐字保留，仅释义本地化——B2 框
  « Patience is part of the system, not a failure of it. » — part of = часть
  (page 6).（定义句本地化 = 阻塞性失败，本版无此情况。）
- **金句**：8 句全部出自本期文章，P7 内各 1 次（Patience 句另在 B2 例句框
  出现 1 次，与核心一致）；全期句频核心 = 分版（5 句 2×；Tuesday 句 3×，另
  1 次在 P8 E-138 题干；Not every 句 3×，另 1 次在 P8 E-140 题干；
  Patience 句 4×，另 2 次在 P7 例句框与 P8 E-137 题干）——“2×”指文章 + P7
  的基准出现，分版与核心逐句相等。
- **P7 结构（核心实测）**：四栏 A2 / B1 / B2 / 工具箱；金句区（句 + 语法点
  + 跟练）；易错诊所 4 题；读者园地；VOL.3 预告。语法点用 W43 EN×RU 金句槽
  的 `Грамматика — ` 前缀；诊所桥段 plain（W43 同款句式）。
- **读者园地（协调员裁定执行）**：绝无编造读者/来信/姓名/引言。核心已有的
  英语元素（信件段 + 标注 + 预告承诺）逐字不动；披露句用俄语写明 3
  事实（未收到真实来信；未收到 VOL.1 第 8 版最佳作文；示例保留标注、
  刊登承诺顺延至 VOL.3）+ 显性俄语公开征集邀请（祈使句
  « Присылайте ваши письма и сочинения! » + VOL.3 刊登承诺）；预告行仅为内容预告，
  不计入邀请。披露句实测盒内无溢出。未为核心没有的英语披露句凭空
  新写英语披露句。
- **刊头 TEXTX 裁定（非缺陷）**：P1 刊头 TEXTX（黑体刊名墨迹框与刊头行墨迹框
  y 向交叠 6.0px）经 PIL 双串像素级重绘验证：**重叠像素 0**（刊名最低墨迹
  y=291，刊头行最高墨迹 y=285，但两者墨迹 x 位置在共享带内无交集；卡片裁图目视亦有
  明显空隙）。属框级伪报，与 W43 EN×RU / W45 EN×ES 刊头裁定同类。
- **卡片目视 8/8**：P1 刊头/暗带/数字框/热搜框/词框/快讯/闪电问答均干净；
  P2 AND YOU 盒俄语 2 行盒内、时钟栏、练习区干净；P3 居家框/猫帽框/影评桥段
  干净；P4 周日赛程框/马德里框/词框干净；P5 难分胜负框/词框/投票结束桥段干净；P6 模拟选票框/图表标签 4 行/教学数据声明/任期框干净；P7 四栏/金句/诊所/
  园地/预告干净；P8 电池 A–H/写作框/范文/Levels 行（与金线有空隙）/键区
  1–150 干净，键区末行距页脚线有空隙。
- **继承 quirk（非本版缺陷）**：P3 “C · THE WORDS” 栏头孤悬于第 2 栏底（配对
  项流至第 3 栏）——核心同款布局，无重叠，审计 0 标记（EN×ES 版已登记同类项）；
  P5 同款。P8 两条 F 配对右项 advance 右缘 1903.8 为冻结英语原文（核心同款）。

## 九、ABSTRACT.txt

俄语单行（刊名 The Lucerna、目标语 английский、读者 русскоязычные、
真实主题：11 月 3 日中期选举、11 月 1 日拨钟、万圣节、电影上映、NFL 马德里赛、
美国投票制度；学习者搜索短语：учи английский по настоящим новостям；
A2–B2；150 упражнений；无 ASCII 双引号）。

## 十、修复轮记录（每轮修复前均有全部 svg/card/PDF sha256 基线）

- **R1**：登记表完美（150 / 60-69-21 / 分版正确），P8 CLEAN 78=78 已绿，但
  2 处 FLOW OVERFLOW（P1-headline +93、P2-ex +386）+ 1 处 HEAD TOO WIDE
  （P6 READ THE CHART）+ 几何审计 NEW 27 标记（多为上述溢出的级联 + 俄语
  框题超宽）。根因已实测：P1 数字框因俄语过长挤出第 2 栏致 TRY IT NOW
  整体下移；P2 因 A/C 桥段由 1 行变 2 行致逐栏丢 1 题位、配对组冲出页脚。
- **R2**：全部修复进 transform.py 后重跑（非手改 content）：P1 暗带副题缩短
  （同基线碰撞类，PIL 量宽 492.7，净空 118px）；数字框标题改短式 + 第 1 行
  注释压缩（4 行→3 行，盒高 336.4→308.7，回归第 2 栏，P1-headline 流终点
  回到核心的 1502）；热搜副题去 “Снимок”；P2 A 桥段缩短至 1 行、C 桥段
  5 版统一缩短至 1 行（P2-ex 流终点回到核心的 2532）；6 个框题/栏头按
  23pt 粗体 PIL 量宽定稿（P3 Дома、P4 Воскрес.、P5 Равная / Пять фраз、
  P6 Бюллетень / График）；P8 §E 间距 11→4（电池区回到 1485 底线内）。
  R2 终轮：0 警告；审计仅剩刊头 TEXTX（§八像素裁定为非缺陷）；补充扫描全清。
- **R3**：edgescan 发现 P1 热搜注释行 advance 右缘 1897 越过栏框线 1885
  （12px）→ 删一虚词（1897→~1877）；R3 差分证实仅 P1 svg/card + 双 PDF
  变化，其余 7 页字节不变；全部 §七门禁复测通过。

## 十一、与 W43 EN×RU 的偏差清单（有意改动，均有依据）

1. P7 金句语法点前缀用 `Грамматика — `（W43 EN×RU 栏标准；西语族用
   `Nota — `，本版不取）。
2. P8 栏头用 W43 短式（长式在 24pt 粗体 434px 栏内超宽，W43 形式已验证可容）；
   H 栏头保留核心 [B1] 标记。
3. 8 个框题/栏头 + 热搜副题 + P1 暗带副题 + P1 数字框注释的俄语半句短于直译
   （23pt 粗体栏宽 398px / 24pt 暗带同基线所限，逐项 PIL 量宽留白后定稿，§十）。
4. P8 §E 间距 11→4（§十 R2 原因；EN×ES 版同类修复）。
5. P2 AND YOU 盒无需 EN×ES 版的 +20→+24 尾长（俄语 2 行与核心流终点一致，
   P2-feature 818 = 核心）。
6. P8 band 副题保留核心英语句 + 俄语译文（W43 为纯俄语；英语句为冻结核心
   文本，量宽后 band 内可容）。
7. 读者园地披露句按协调员裁定重写（§八）；英语信件段逐字冻结。
8. 徽章几何 = W43 EN×RU：标语槽 y=372，19.5pt 粗体砖红（README #20 的
   EN 族情形与 W43 同族先例一致）。
9. P8 印刷集钉住方式沿用 W43 PRINT_NOTES 显式集合（39 题号与 EN×ES 版一致，
   核心印刷集相同）。

## 十二、复现

```bash
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-en-ru-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python transform.py   # 核心构建副本 → 分版源码（断言全部替换）
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py          # 单进程：content12 → 34 → 56 → 7 → 8（登记表顺序不可变）
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py       # cards + print PDF + web PDF
cd ~/workspace/goals/lucernaread-social-media-operations/tools
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-en-core/svg --edition-svg ../files/weekly-report-w45-en-ru/svg
./venv/bin/python p8.py compare --core-p8 ../files/weekly-report-w45-en-core/svg/p8-exercices.svg --edition-p8 ../files/weekly-report-w45-en-ru/svg/p8-exercices.svg --total 150
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-en-ru --core ../files/weekly-report-w45-en-core
```

- run.py 解释器：tools/venv/bin/python（Python 3.12.3，PIL 13.0.0）；
  render.py 解释器：tools/venv/bin/python（同 venv；系统 python3 无 cairosvg，
  未用）。run.py 解释器/PIL 选择自由，但本版即以该 venv 字节复现核心基线
  8/8（freeze baseline），故沿用。
- 本构建不推 git、不发 Discord（按任务指令，入仓由上级主线串行完成）。
- 附记：本报告不自认终审——仍需新一轮完整独立校对零问题后方可定稿。
