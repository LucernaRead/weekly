# WEEKLY KIT — The Lucerna · ENGLISH WEEKLY VOL.2 · EN × ES edition (W45)

**Status: builder-complete, NOT finalized.** All builder gates below are measured
green. Finalization requires an independent proofread round (zero problems) by a
separate proofer — this report does not claim it. No Discord post, no chat
delivery, no repo insert, no cron was made under this task.

## 一、交付物

`files/weekly-report-w45-en-es/`：

- `svg/` — 8 pages of SVG sources (p1-front … p8-exercices)
- `cards/` — 8 full-page PNGs, 1950×2700 (all 8 visually inspected, §八）
- `The-Lucerna-VOL2-ES.pdf` — merged 8-page print PDF, **17,292,956 bytes**,
  sha256 `382f1e81b1249123b1ca2d28ebb53d825f82c55ece01f822f576e27fd9b733f1`
- `The-Lucerna-VOL2-ES-web.pdf` — compressed 8-page PDF, **4,004,747 bytes**
  (< 10 MB), sha256 `6282726a0a79ee6ce72131372e4ccc4c5243015c8e087e9853903dc2b4f23e13`
- 本文件 + `ABSTRACT.txt`（西班牙语单行、无 ASCII 双引号，见 §九）

构建代码在 `hidden_files/weekly-report-w45-en-es-build/`：`transform.py`
（核心 → 分版的全部替换，逐项断言出现次数；修复轮只改它，不手改 content）、
`run.py`（单进程 driver）、`render.py`（核心配方）、`supplemental.py`
（同基线行查 + P6 图表查 + 右缘/框线查）、各轮基线与审计输出。

## 二、基底与规格

- 基底：W45 EN 核心 `files/weekly-report-w45-en-core/`（VOL.2，刊头
  The Lucerna，2026 年 11 月 2–8 日当周，刊期 2026-w45）。
- 8 版，1950×2700，四栏，暖象牙底、深橄榄点缀，哥特体刊头 The Lucerna。
- 英语正文冻结；讲解层全部西班牙语；全文 CJK 字符 0（§七）。
- 家具以 W43 EN×ES 已上架版为准（胜过 README #20 的泛化规则），登记见 §三。

## 三、家具登记（W43 EN×ES 已上架版实测）

- 刊头标语位（y=372，19.5pt 粗体砖红，替换核心 strapline）：
  `TEXTOS EN INGLÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`
- 刊头行：`SEMANARIO EN INGLÉS · VOL.2 · VOTOS · FÚTBOL · CINE`
- 顶栏：`WEEKLY IN ENGLISH · UNA EDICIÓN CADA SEMANA · EL INGLÉS QUE LEE AMÉRICA`
- 页脚（8 版）：`The Lucerna · SEMANARIO INGLÉS VOL.2 · TEXTO EN INGLÉS · EXPLICACIONES EN ESPAÑOL`
- 页码行：`Página N de 8`
- 词框前缀：`Nota — `（bslib4 gloss，核心 `译注｜` + 内容层 `讲解｜` 均已去除）
- P8 分隔：`— Página N —`；P8 印刷键括号：半角 ` (nota)`（W43 EN×ES 家族写法；核心为全角）
- P7 栏头：`LEVEL A2 · Base` / `LEVEL B1 · Intermedio` / `LEVEL B2 · Desafío` /
  `THE EXAMPLE · El ejemplo` / `THE TOOLBOX · Herramientas` /
  `PHRASES OF THE WEEK · Frases de la semana` / `THE ERROR CLINIC · Errores` /
  `READERS' CORNER · Rincón de los lectores` / `NEXT WEEK · VOL.3 · Avance` /
  band `LANGUAGE IN HAND · A fondo`
- P8 栏头（W43 短式，见 §十 R1）：`A · CLOZE · Completa el texto` /
  `B · MULTIPLE CHOICE · Opción` / `C · READING · Comprensión` /
  `D · SENTENCES · A completar` / `E · TRANSLATION · Traducción` /
  `F · WORDS · Empareja` / `G · DIALOGUE · El diálogo` /
  `H · WRITING · Escritura [B1]`（[B1] 为核心原有标记，保留）
- 练习内小标签：`Completa` / `Reescribe` / `Empareja` / `Corrige`
- 类型登记（仅登记表，不印版面）：完成句子→Completar frases，单选→Opción
  múltiple，句型转换→Reescribir，词汇配对→Emparejar，完形填空→Completar el
  texto，阅读理解→Comprensión lectora，翻译→Traducir，对话补全→Completar el
  diálogo，写作→Redacción，改错→Corregir，图表读数→Lectura de gráfico，跟练→Practicar

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
| P8 评估 | 完形 8 + 单选 9 + 阅读 4 + 完成句子 4 + 翻译 4（英↔西，见 §六）+ 词汇配对 4 + 对话补全 5 + 写作 1（« My Tuesday, November 3 »，80–100 词，范文 85 词）。39 题 + 全部 150 题答案与简析 |

图片：assets/ 自核心构建目录原样复制（5 张 Wikimedia Commons 公版/CC0 图，
出处图注为冻结英语，与核心一致）；卡片目视已核对 5 图均在位。

## 五、实测体量（登记表独立展开计数，与核心一致）

- **练习总量：150 题**（统一编号 1–150，连续无缺重）
  - 按难度：**A2 60 · B1 69 · B2 21**
  - 按版：P1 10 · P2 17 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 39
    （P2 17、P8 39 为本核心实测值，不同于通用 10/18/18/18/18/18/12/38）
  - 按题型（西班牙语登记标签）：Completar frases 33 · Opción múltiple 41 ·
    Reescribir 16 · Emparejar 20（5 组）· Lectura de gráfico 6 · Practicar 8 ·
    Corregir 4 · Completar el texto 8 · Comprensión lectora 4 · Traducir 4 ·
    Completar el diálogo 5 · Redacción 1
  - P8 正式评估 39 题，其余 111 题为 P1–P7 即学即练。
- 范文 85 词（冻结 MODEL 段实测分词计数，与核心一致）。
- 词框：gloss() 串按 `·` 拆分，核心 18 = 本版 18，逐框分布 3/4/4/3/4
  （P2/P3/P4/P5/P6），英语词头逐项一致，仅释义本地化。

## 六、P8 门禁（tools/p8.py compare，显式路径）

- 印刷笔记集合：**CLEAN，78 = 78**，missing=[]，extra=0，uncertain=[]。
- 印刷集相等靠显式 `NOTAS_EXTRA` 钉住（P1–P7 练习题的印刷笔记集；W43 EN×ES
  同类修复先例）：西班牙语笔记长于中文笔记适用的 `len ≤ 10` 规则，若沿用
  原规则将漏印——本版条件改为 `pg == 8 或题号 ∈ NOTAS_EXTRA`，集合与核心
  逐项相等。
- keydiff = **[137, 138, 139, 140, 150]**，逐项裁定如下（其余 145 键与核心
  逐字节一致；键按题号提取比对，不按行位置比对，故键区重排只产生伪影，
  不产生 keydiff）：
  - 137：核心键为英文句 « Patience is part of the system, not a failure of
    it. » 的中文译文 → 本版西班牙语译文 « La paciencia es parte del sistema,
    no un fallo del sistema. »；题面英语指令 `Translate :` 保留（与核心一致）。
  - 138：核心键为 “Tuesday, November 3, is Election Day in the United States.”
    的中文译文 → 本版 « El martes 3 de noviembre es el día de las elecciones
    en Estados Unidos. »；母语指令 `翻译：` → `Traduce:`。
  - 139：核心键为 “On Sunday, the NFL plays in Madrid.” 的中文译文 → 本版
    « El domingo, la NFL juega en Madrid. »；母语指令 `翻译：` → `Traduce:`。
  - 140：核心键为 « Not every place changes. » 的中文译文 → 本版 « No todos
    los lugares cambian. »；题面英语指令 `Translate :` 保留。
  - 150：写作题键为讲解层文字（非冻结英语）：核心 « 开放题 — 要点见写作框，
    范文在第 8 版写作框内 » → 本版 « Pregunta abierta: véanse los puntos en
    el recuadro de redacción; el modelo está en el recuadro de esta página »。
    （同 W43 EN×ES keydiff 中写作题键重定向一类。）
- P8 注释纯西班牙语（印刷键区 grep：CJK 0；半角括号体）。

## 七、冻结与全部门禁实测值

| 门禁 | 实测 |
|---|---|
| 核心基线复现（tools/freeze.py baseline） | **8/8 逐字节一致**（`tools/scratch/baseline-w45-en`）；构建后核心 SVG 重哈希与基线完全一致，核心未动 |
| 冻结差分（tools/freeze.py diff，终轮 diff3.json） | 新增 CJK 0（8 版全 0）；版面 CJK 0；被删英语串仅两类：(a) P1 刊头标语（徽章替换，W43 家具）；(b) 重排伪影（P1 数字框行、P7 例句框 `(page 6).`、P8 键区行段——内容均在新增串中重排出现，键经 p8 逐题号证实） |
| 违禁词检查 | svg/ + KIT + ABSTRACT 全量 grep 均为 0 命中（该词按任务要求不在本文中拼写） |
| 英语正文冻结 | 除上表两类外无英语串被删；P7 词框英语定义句与金句原文逐字保留（见 §八） |
| P8 compare | CLEAN 78=78，keydiff [137, 138, 139, 140, 150]（§六逐项合法） |
| 几何审计（tools/occlusion_audit.py，自检先行） | 分版 1 标记 / 核心 0 / NEW 1——唯一标记为 P1 刊头 TEXTX，裁定为非缺陷（见 §八像素证据）；其余 0 |
| 同基线行查（supplemental.py rowcheck，解码后测量） | **0 碰撞**（分版 = 核心；初版 -30.5 伪影系 `&amp;` 未解码所致，解码后 +19.0px 空隙，与卡片目视一致） |
| P6 图表标签覆盖（基线锚定墨迹法，PIL getmetrics，anchor ls） | 最差 **0.0%**（门限 <30%；4 条标签行 + 导读行均 0；分版 = 核心） |
| 全 8 页框线压框 + 右缘扫描（ADVANCE 法） | 0 标记；P1–P7 最大 advance 右缘 1885.0（恰为页边）；P8 1903.8 仅来自两条冻结 F 配对右项（核心同款，墨迹未触内框线 1910） |
| 词框 gloss | 18 = 18（§五） |
| P7 金句 | 8 句原文逐字保留；级别标签 [A2, A2, B1, B1, B2, B2, A2, B1] 与核心一致；句频核心 = 分版（见 §八） |
| 题量与级别 | 150；A2 60 / B1 69 / B2 21；分版 10/17/18/18/18/18/12/39（登记表展开计数） |
| 范文 | 85 词，与核心一致 |
| 构建警告（终轮） | FLOW OVERFLOW 0 · HEAD TOO WIDE 0 |
| 卡片目视 | 8/8 逐页目视（§八） |
| ABSTRACT | 西班牙语单行、无 ASCII 双引号、含真实主题关键词 + 学习者搜索短语 + 刊名 + 目标语名 + A2–B2 + 150 题 |

## 八、P7 专项与目视记录

- **词框硬性门**：三级例句框英语定义句逐字保留，仅释义本地化——B2 框
  « Patience is part of the system, not a failure of it. » — part of = una
  parte (page 6).（定义句本地化 = 阻塞性失败，本版无此情况。）
- **金句**：8 句全部出自本期文章，P7 内各 1 次（Patience 句另在 B2 例句框
  出现 1 次，与核心一致）；全期句频核心 = 分版（5 句 2×；Tuesday 句 3×，
  另 1 次在 P8 E-138 题干；Not every 句 3×，另 1 次在 P8 E-140 题干；
  Patience 句 4×，另 2 次在 P7 例句框与 P8 E-137 题干）——“2×”指文章 + P7
  的基准出现，分版与核心逐句相等。
- **P7 结构（核心实测）**：四栏 A2 / B1 / B2 / 工具箱；金句区（句 + 语法点
  + 跟练）；易错诊所 4 题；读者园地；VOL.3 预告。语法点用 W43 EN×ES 金句槽
  的 `Nota — ` 前缀；诊所桥段 plain（W43 同款句式）。
- **读者园地（协调员裁定执行）**：绝无编造读者/来信/姓名/引言。核心已有的
  英语元素（信件段 + 标注 + 预告承诺）逐字不动；披露句用西班牙语写明 3
  事实（未收到真实来信；未收到 VOL.1 第 8 版最佳作文；示例保留标注、
  刊登承诺顺延至 VOL.3）+ 显性西班牙语公开征集邀请（祈使句
  « ¡Envíanos tu carta y tu texto! » + VOL.3 刊登承诺）；预告行仅为内容预告，
  不计入邀请。披露句实测 3 行，盒内无溢出。未为核心没有的英语披露句凭空
  新写英语披露句。
- **刊头 TEXTX 裁定（非缺陷）**：P1 刊头 TEXTX（黑体刊名墨迹框与刊头行墨迹框
  y 向交叠 6.2px）经 PIL 双串像素级重绘验证：**重叠像素 0**（刊名最低墨迹
  y=290，刊头行最高墨迹 y=285，但两者墨迹 x 位置无交集；卡片裁图目视亦有
  明显空隙）。属框级伪报，与 W43 EN×ES 刊头裁定同类。
- **卡片目视 8/8**：P1 刊头/暗带/数字框/热搜框/词框/快讯/闪电问答均干净；
  P2 AND YOU 盒西语 2 行盒内、时钟栏、练习区干净；P3 居家框/猫帽框/影评桥段
  干净；P4 周日赛程框/马德里框/词框干净；P5 难分胜负框/词框/投票结束桥段干净；
  P6 模拟选票框/图表标签 4 行/教学数据声明/任期框干净；P7 四栏/金句/诊所/
  园地/预告干净；P8 电池 A–H/写作框/范文/Levels 行（与金线有空隙）/键区
  1–150 干净，键区末行距页脚线有空隙。
- **继承 quirk（非本版缺陷）**：P3 “C · THE WORDS” 栏头孤悬于第 2 栏底（配对
  项流至第 3 栏）——核心同款布局（核心 y=2275.2，本版 y=2305.0，随西语流微移），
  无重叠，审计 0 标记。

## 九、ABSTRACT.txt

西班牙语单行（刊名 The Lucerna、目标语 inglés、读者 hispanohablantes、
真实主题：11 月 3 日中期选举、11 月 1 日拨钟、万圣节、电影上映、NFL 马德里赛、
美国投票制度；学习者搜索短语：aprende inglés leyendo noticias reales；
A2–B2；150 ejercicios；无 ASCII 双引号）。

## 十、修复轮记录（每轮修复前均有全部 svg/card/PDF sha256 基线）

- **R1**：登记表完美（150 / 60-69-21 / 分版正确），但 P8 出现 4 个 HEAD TOO
  WIDE（B/C/D/G 西语栏头超 434px 栏宽）→ 改用 W43 短式栏头（§三）。
- **R2**：0 警告；渲染后几何审计 NEW 19 标记——18 项真缺陷 + 1 项刊头伪报：
  标题类缩短（AT HOME→En casa、CAT'S HAT→El sombrero、SUNDAY→Domingo、
  TOO CLOSE→Muy reñido、PRACTICE BALLOT→Papeleta、HOW LONG→El mandato、
  热搜副题、暗带右行 2、P1 词框改为单行、P7 金句栏头去括号）；P2 AND YOU
  盒尾 +20→+24（0.6px 取整）；P8 §E 间距 11→4（Traduce: 致 E-139 多 1 行，
  Levels 行压金线，收回 28px 后 Levels 基线 1485→~1457，金线 1486 净空）。
- **R3**：0 警告；终轮审计仅剩刊头 TEXTX（§八像素裁定为非缺陷）；补充扫描
  全清；全部 §七门禁复测通过。R3 全部 8 页均有改动（标题/桥段/间距），除
  有意改动外无其他变化，与 `baseline-round3-pre.txt` → `baseline-final.txt`
  的哈希差分一致。

## 十一、与 W43 EN×ES 的偏差清单（有意改动，均有依据）

1. P8 栏头用 W43 短式（R1 长式超宽，§十）；H 栏头保留核心 [B1] 标记。
2. P7 金句栏头去括号（长式与右侧说明行重叠）→ W43 原文。
3. 6 个框题 + 热搜副题 + 暗带右行 2 + P1 词框的西语半句短于直译（23pt 粗体
   栏宽 434px 所限，逐项 PIL 量宽留白后定稿，§十）。
4. P8 §E 间距 11→4（§十 R2 原因）。
5. P2 AND YOU 盒尾 +20→+24（§十 R2 原因）。
6. P8 band 副题保留核心英语句 + 西语译文（W43 为纯西语；英语句为冻结核心
   文本，量宽后 band 内可容）。
7. P7 金句语法点用 `Nota — ` 前缀（W43 金句槽先例）；诊所桥段 plain。
8. P8 键区半角括号（W43 家族写法；核心全角）。
9. 读者园地披露句按协调员裁定重写（§八）；英语信件段逐字冻结。
10. 徽章几何 = W43 EN×ES：标语槽 y=372，19.5pt 粗体砖红（README #20 的
    EN 族情形）。

## 十二、复现

```bash
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-en-es-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python transform.py   # 核心构建副本 → 分版源码（断言全部替换）
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py          # 单进程：content12 → 34 → 56 → 7 → 8（登记表顺序不可变）
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py       # cards + print PDF + web PDF
cd ~/workspace/goals/lucernaread-social-media-operations/tools
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-en-core/svg --edition-svg ../files/weekly-report-w45-en-es/svg
./venv/bin/python p8.py compare --core-p8 ../files/weekly-report-w45-en-core/svg/p8-exercices.svg --edition-p8 ../files/weekly-report-w45-en-es/svg/p8-exercices.svg --total 150
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-en-es --core ../files/weekly-report-w45-en-core
```

- run.py 解释器：tools/venv/bin/python（Python 3.12.3，PIL 13.0.0）；
  render.py 解释器：tools/venv/bin/python（同 venv；系统 python3 无 cairosvg，
  未用）。run.py 解释器/PIL 选择自由，但本版即以该 venv 字节复现核心基线
  8/8（freeze baseline），故沿用。
- 本构建不推 git、不发 Discord（按任务指令，入仓由上级主线串行完成）。
- 附记：本报告不自认终审——仍需新一轮完整独立校对零问题后方可定稿。
