# W45 FR×KO 独立校对报告 — 结论：ZERO PROBLEMS

- 分版：目标语言法语（FR），读者母语韩语（KO），VOL.3，`files/weekly-report-w45-fr-ko/`
- 对照：W45 FR 核心 `files/weekly-report-w45-fr-core/`（VOL.3）与 W43 同配对版 `files/weekly-report-fr-ko/`（VOL.2）
- 校对员：独立校对（深度 2），未派生下级代理；未碰 `weekly-git`、未改核心/W43/交付目录、未改 `tools/` 下任何文件、未清理共享 scratch、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未宣布上架。
- 工具版本：`tools/p8.py` sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`（与任务书所述已验证新版前缀一致）；`tools/occlusion_audit.py` `e1f92b42…`；`tools/freeze.py` `d9adfa48…`。全部渲染/扫描均用 `tools/venv/bin/python`。
- 证据目录：本报告同目录 `work/`（日志、JSON、复现树 `repro-build/`、`repro-edition/`、`repro-r3-build/`、`repro-r3-edition/`、卡面预览 `preview/`、pdftoppm 输出）。

## 开工查重

- 开工时无任何 `fr-ko` 进程在跑（仅见无关的 `fr-ja-proof` 进程）；交付物最后 mtime 2026-10-28 06:28:54 UTC（ABSTRACT/KIT），复查时 154 秒静默无变化，判定为已完工交付物，非 in-progress 写入，安全开工。
- 交付物终态复核（校对结束时重测）：交付 SVG/卡片哈希与开工时一致（DELIVERY-UNTOUCHED、CARDS-UNTOUCHED）；核心 SVG 8/8 与 `w45-fr-core-prebuild.sha` 一致（CORE-UNTOUCHED）。

## 交付 pins（独立重测，与建造员声称一致）

- 印刷 PDF `Le-Lucerna-VOL3-KO.pdf`：15,453,079 字节，sha256 `994fff4df860893094a6e83b6acfb800b355fdf9d8633f595120c10c93514e26` ✓
- 网页 PDF `Le-Lucerna-VOL3-KO-web.pdf`：5,098,770 字节，sha256 `6aca62a37060a7c21b8573c953e9592203a95df03f154e91c48dbf5da451881c` ✓
- 交付 SVG 8/8 与建造树 `final-round4.sha` 的 SVG 行一致；卡片 8/8 与其 cards 行一致。

## 门 1 — 冻结

- 核心基线：`tools/freeze.py baseline`（核心建造树 `hidden_files/weekly-report-w45-fr-build`，OUT 重定向至自有 scratch）结果 **8/8 逐字节一致**，且 freeze 自带的核心完整性复核确认 shipped 核心未被改动。
- CJK 口径（韩语版说明）：`freeze.py diff` 的 added-CJK 计数含 Hangul（解释层本身就是韩语），故不按 zh/ja 的 added-CJK=0 设门；改按 Han 表意字设门——渲染文本节点中 Han（U+4E00–U+9FFF）节点 **8 页全部为 0**，与核心的中文解释层已完全替换一致；建造代码中仅登记表类型名保留 Han（transform.py `ALLOWED` 表内，从不印出），与 W43 FR×KO 先例一致。
- 法语冻结串（joined 文本法，跨行换行安全）核心 vs 分版：
  - P4 `41e édition en 2026 (40e anniversaire)`：P4 各 1 处；独立 `40e` 1 处、`41e` 1 处，两版相同 ✓
  - P7 #4 金句 `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?`：句终计数 5×（P4 1 + P7 4），两版相同 ✓
  - P7 #8 金句 `Les jeunes créateurs y rencontrent leur public, en vrai.`：句终计数 3×（P5 1 + P7 1 + P8 1），两版相同；Q106 键与该句逐字一致 ✓
  - P6 同步句 `Ce calendrier peut encore bouger.`：句终计数 3×（P6 1 + P7 2），两版相同 ✓
  - P7 定义句/法语例句：P7 法语词多重集除下述解释层拉丁 token 外全部相同（见本门末尾的精确偏差说明）；P7 语法栏法语句与工具箱随身句与核心一致。
- Q120：题干节点 `Si j'étais libre dimanche, j'___ à Nanterre. A.` 与选项行 `irai · B. irais · C. vais` 在两版中坐标、文本完全相同；登记表键 B=B；P8 注同为 `si + imparfait → conditionnel` 规则（韩语注略去 `présent` 一词，见非阻塞观察 2，规则内容等价）；Q119（键 B，题干 `Elle s'intéresse ___ festivals. A. à les · B. aux · C. des`，注 `s'intéresser aux（à+les）` 两版逐字相同）与 Q121（键 A，题干 `À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant`）均不动 ✓
- 法语词多重集（拉丁 token/页）：P1–P6 **完全相同**（P1 654、P2 640、P3 607、P4 717、P5 551、P6 563）；P8 除 `Traduisez` 5→0 外仅 `présent` 1→0（P8 注的韩语改写，解释层）；P7 仅 `VOL` 6→7、`P` 0→2（读者角韩语文本中的 `VOL.4`、`P8` 指称，非法语词）。即法语正文多重集逐页相同，偏差全部位于解释层（见非阻塞观察 2）。
- P8 `Traduisez` 5×→0×：P8 电池区逐行 diff（153 行 vs 153 行）证明仅 5 处指令动词替换 + 版块标题/说明行的中→韩改写，其余电池行逐字相同。5 处替换：
  - #136 `Traduisez : 他跑得比他哥哥更快。` → `프랑스어로: 그는 형보다 더 빨리 달려요.`（法语键 `Il court plus vite que son frère.` 无损）
  - #137 `Traduisez : 学生们自 10 月 17 日起就在放假。` → `프랑스어로: 학생들은 10월 17일부터 방학이에요.`（法语键 `Les élèves sont en vacances depuis le 17 octobre.` 无损）
  - #138 `Traduisez : 今晚，我们要准备书包。` → `프랑스어로: 오늘 밤 책가방을 챙길 거예요.`（法语键 `Ce soir, nous allons préparer nos cartables.` 无损）
  - #139 `Traduisez : 人们尚不知道决赛选手是谁。` → `프랑스어로: 아직 결승 진출자를 몰라요.`（法语键 `On ne connaît pas encore les finalistes.` 无损）
  - #135 `Traduisez : « Lire un programme, c'est déjà comprendre la France. »` → `한국어로: « Lire un programme, c'est déjà comprendre la France. »`（法语句子保留，方向改为韩语作答）
- `coquilles`：P8 复数 `coquilles` 9=9（建造员所称的 9=9 是 P8 口径）；全报复数 10=10（P1 1 + P8 9）；含单数的子串总数 15=15；`coquillage` 1=1。全部相等，冻结成立。

## 门 2 — P8 双门（FR 族硬性，缺一不可）

- plain `tools/p8.py` 显式双路径 + `--total 150`（未用 `--target` 形式——实测 `--target ko` 会误取 `p8-siheom.svg` 而 FileNotFound；未用默认 total——默认会取 W43 的 149 而错分段；两者皆避开）：
  - 核心 extract：noted 97/150（joined 解析）；分版 extract：noted 97/150（joined 解析）
  - 双路径 compare：**CLEAN，missing=[]，extra_count=0，uncertain=[]，keydiff=[135, 150]**，exit 0 ✓
- `hidden_files/w45/p8-fr-gap-fix/keycompare.py` 全 150 键比对：**key-mismatches: 2 [135, 150]，裸键（53 个无注项）mismatch = 0**。两处均为已注项的注语言重定向，非法语键改动：
  - #135：核心注/答案 `读一份日程，本身就是在了解法国。` → 分版 `일정을 읽는 것 자체가이미 프랑스를 이해하는 거예요.`（#135 为法→韩翻译题，答案语言随读者语言改写，合法重定向；法语句 `Lire un programme, c'est déjà comprendre la France.` 在题干中保留）
  - #150：核心 `开放题` → 分版 `열린 문제`（写作题指引键，语言改写）
  - #136–139：印刷键与核心逐字相同（法语句键无损），仅题干源句改为韩语——与 keydiff 未列入 #136–139 一致。
- P8 注 Han 表意字：0（门 1 的 Han 节点统计覆盖 P8；P8 注全部为韩语/法语，无中文残留）。

## 门 3 — 登记 / gloss / 金句 / 范文

- 登记表（自有 scratch 内复现树导入 content 模块单进程 dump，与核心基线复现树同法对照）：
  - 总量 150；分页 10/15/18/18/17/18/12/42（P1 10、P2 15、P3 18、P4 18、P5 17、P6 18、P7 12、P8 42）；级别 A2 53 / B1 75 / B2 22；与核心登记表逐项相同 ✓
  - 题号 1–150 连续；Q106 键 `Les jeunes créateurs y rencontrent leur public, en vrai.` 两版相同。
- gloss：源调用串按 `·` 切分（README #21 口径），分版与核心均为 **38 = 7/6/6/7/6/6**（P1 7、P2 6、P3 6、P4 7、P5 6、P6 6），逐页 = 核心 ✓
- 金句 8 句（核心 KIT §8 编号，P7 印出页签逐句核对，句终计数法：排除破折号/冒号引导的从句续写后计数）：
  - #1 `Le lundi 2 novembre, on reprend les cours.` (page 2) = 5（P2 1 + P7 4）
  - #2 `On ne connaît pas encore les finalistes.` (page 1) = 3（P7 2 + P8 1；P1 正文为小写从句形式，页签正确）
  - #3 `Les cimetières se sont remplis de chrysanthèmes.` (page 3) = 1（P7 1；P3 正文为破折号续写，句终计数排除）
  - #4 `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?` (page 4) = 5（P4 1 + P7 4）
  - #5 `Le festival se promène dans Paris.` (page 5) = 1（P7 1；P5 正文为冒号引导的从句，页签正确）
  - #6 `Ce calendrier peut encore bouger.` (page 6) = 3（P6 1 + P7 2）
  - #7 `Ce week-end, tout se joue.` (page 1) = 1（P7 1；P1 MOT 框为冒号引导的从句，页签正确）
  - #8 `Les jeunes créateurs y rencontrent leur public, en vrai.` (page 5) = 3（P5 1 + P7 1 + P8 1）
  - 8 句逐字、分版与核心计数全部相等，且每句均在其所标源文章页命中 ✓
- 范文：P8 MODÈLE 7 行法语范文，两版逐字相同；空白分词口径 86 词（原始拉丁 token 88 − 连字符复合词 `grand-mère`、`week-end` 各计 1 词所减 2 = 86；数字 7、8 不计词），在题面 80–100 词内，与核心 KIT 86 词一致 ✓

## 门 4 — 几何

- 规范 `tools/occlusion_audit.py`（自检先过：6 类 planted 全部命中 1 次，clean 对照静默）：
  - 分版：**0 flags**；核心：**0 flags**；`--core` 对照：**NEW 0** ✓
- 自有补充扫描（自写脚本，墨迹盒复用规范审计的 `ink_box` 锚定法；行定义与建造员 checks.py 相同但代码独立）：
  - 同基线 rowcheck（y<200 顶栏 + y=2624 页脚）：**0 重叠**
  - 右缘扫描（墨迹右 >1885.5）：分版 **3 处**，核心 **同 3 处同值**——均为 P8 电池冻结法语选项（y=940 右 1891.2 `b. une soirée qui dure jusqu'à la nuit`；y=1016 右 1891.2 `d. le coquillage fêté à Port-en-Bessin`；y=1054 右 1899.5 `e. plusieurs concerts en une semaine`）。卡面像素复核（排除框线列）：分版与核心同值 1898 / 1895 / 1902，均 < 内框线 1910，属继承的 guideline 越线（核心同形），非框线穿越。**建造员所称的 P6 TROIS DATES 右缘 1935 / 框线 1935 在规范墨迹法下不可复现**：该节点（x=1469, y=1367, 23pt Sans）在分版与核心中规范墨迹右均为 **1835.25**（Serif 面最宽 1866.2、Bold Serif 1879.5，亦 < 1885.5），卡面像素右均为 **1852**，在 guideline 与框线内，无溢出（见非阻塞观察 1：节点归属与数值订正，裁决结论不变——继承、无需改动）。
  - 框线扫描（墨迹 vs 外框 28/1922、内框 40/1910、上下 40/2660）：分版 **0**，核心 **0** ✓
  - P6 图表标签覆盖（画序法：标签墨迹 vs 其后绘制的 rect，排除整页框）：**0.0%**（P6 所谓“图表”实为日历表与对比栏，无柱形 rect/path 条带；<30% 门通过）；卡面目视 P6 日历表标签全部完整 ✓
  - P8 三口径（分版 vs 核心同口径）：
    - 流光标（渲染日志）：电池 1410 = 1410（<1485 条带规则）；答案区 2187 vs 2167（均 <2545）
    - 最大基线（y<1560 电池块 / 1560–2600 答案块，页脚除外）：电池 1538.0 = 1538.0；答案 2526.11 vs 2539.19
    - 墨迹底：电池 1539.8 vs 1540.0；答案 2529.6 vs 2541.2
    - 结论：分版与核心同口径下差值 ≤13px 且全部在页内，无新增溢出。注：流光标与绝对基线是两种量度（流光标为栏内游标），不直接等同；门以绝对墨迹底 + 规范审计为准。
  - P7 预告墨迹底与读者框墨迹底（框体与核心同 rect）：
    - 读者框（989, 1878, 896×380，框底 2258）：分版墨迹底 2235.1，余量 **22.9**（核心 2236.6，余量 21.4）
    - 预告框（989, 2270, 896×270，框底 2540）：分版墨迹底 2470.0，余量 **70.0**（核心 2469.5，余量 70.5）
  - 孤儿扫描（窗口 10–45，含韩语 ≥3 音节尾 mid-word 切分标准，源串 adjudication 用复现树 content 源）：
    - **SPLIT≥3 = 0；LONE-FRAG = 0**；仅 4 处 START-CLOSER，全部为继承的法语收尾符（P3 y=789.6 `: on le pose…`、P4 y=837.1 `: quarts de finale…`、P5 y=430.6 `: clôture du festival.`、P7 y=428.1 `: attention à l'accord…`），与核心同页同 y 同串 ✓
    - kinsoku 行首收尾符全报 = 上述 4 处（核心另有中文注收尾符，分版随中文解释层消失而消失，属正常替换）
- 逐页最大墨迹底（页脚除外）：分版与核心 P1–P6 逐页相等（2480.1 / 2467.9 / 2491.0 / 2511.4 / 2456.6 / 2510.5），P7 2470.0 vs 2469.5，P8 2529.6 vs 2541.2——全部在页内。

## 门 5 — 换行 / 溢出

- 自有重跑渲染日志（两轮复现 + 登记 dump，共 3 次单进程渲染）**零警告、零错误、零 Traceback**；建造树 build4b 日志同样零警告。
- 流日志中两处“终值超底线”数字（P1-hiver 2298 vs 底线 2290；P6-ex 2557 vs 底线 2540）**在核心基线渲染日志中逐字相同**，属继承的流游标行为；绝对墨迹底（P1 2480.1、P6 2510.5）与规范审计 FOOTER 0 旗共同证明无墨迹溢出。
- 结论：**零 OVERFLOW**（墨迹口径；流游标数字不作为溢出证据）。

## 门 6 — 读者角（零编造）

P7 读者框逐字摘录（分版，换行连接后）：

- 栏头：`LE COURRIER DES LECTEURS · 독자 마당`
- 编辑示例（明示非来信）：`« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).`
- 韩语点评 + 显式祈使征集句：`샤오모의 한마디 — passé composé가 안정적이고 세미콜론이 좋아요. VOL.4에 여러분의 편지와 최고의 P8 작문을 보내 주세요!`
  - 征集句字面覆盖范围裁决：`VOL.4에 여러분의 편지와 최고의 P8 작문을 보내 주세요!`（请把你们的来信与最佳 P8 作文寄给 VOL.4！）——祈使动词 `보내 주세요`（请寄来）+ 并列宾语“来信”与“最佳 P8 作文”**两者字面齐全**，征集成立。预告行 `다음 주: … 여러분의 편지도요!`（下周……还有你们的来信！）仅为预告提及，**不计作征集**（本门征集结论不依赖该行）。
- 三事实披露（法语编辑注 + 韩语编辑注双语齐全）：
  1. 无真实来信：法语 `aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru)`；韩语 `인쇄 때까지 VOL.2 편지가 오지 않았고(W44 미발행)` ✓
  2. 无 VOL.2 最佳作文：韩语 `최고의 P8 작문도 없어 예시를 싣습니다`（法语注以 `aucun texte du VOL.2` 概括，韩语注分项明示）✓
  3. 均延至 VOL.4：法语 `Le VOL.4 reprendra la promesse.`；韩语 `VOL.4에서 실제 편지와 작문을 다룹니다.` ✓
- 预告行（1 行，范围与核心一致）：栏头 `LA SEMAINE PROCHAINE · VOL.4 다음 주`；法语三项（11 月 9 日参议院审议社保预算、11 月 11 日停战纪念日、11 月 14–15 日迪耶普鲱鱼与扇贝集市）+ `Et vos lettres, enfin !`；韩语 `다음 주: 상원 사회보장 예산 심의, 11월 11일 정전 기념일, 디에프 가리비 시장. 여러분의 편지도요!`——与核心预告三项逐项对应 ✓
- 结论：示例明示为编辑示例而非真实来信，三事实披露齐全，征集句字面覆盖来信与最佳 P8 文本，**零编造** ✓

## 门 7 — 家具三方对照（核心 / W43 / 本版）

- 徽章串：分版 P1 y=574、x=975 middle、22pt、weight 700、fill BRICK `#a4553a`，串 `프랑스어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`——与 W43 同配对版**逐字节相同**（W43 同值同属性）；与 W45 核心徽章槽相同（核心同槽为中文串 y=574）✓
- 页脚：分版 `Le Lucerna · 프랑스어 주간지 VOL.3 · 텍스트는 프랑스어 · 해설은 한국어` + `제 N 면 / 총 8 면`（8 页全测）——W43 模板（VOL.2）随目标核心卷号推进为 VOL.3，形式一致 ✓
- 页线：`제 N 면 / 총 8 면` = W43 先例 ✓
- gloss 前缀：`해설 — `（6 盒全测）= W43 先例；核心为 `译注｜`，替换正确 ✓
- expl() 命名：复现树 `bslib4.py:154 def expl`，调用数 content12 4 / content34 9 / content56 9 / content7 3 / content8 1，与 transform 所述 rename 计数一致；W43 建造树同样为 `def expl`（同行号 154），命名先例一致；复现树 content/bslib 中 `bridge` 残留 0（transform.py 自身的 rename 代码除外）✓
- P8 分隔符：`— 제 N 면 —`（1–8 面全测）= W43 先例；核心为 `— 第 N 版 —` ✓
- KIT 订正核查（独立实测 W43 SVG，非采信 KIT 自述）：
  - W43 左上实测：y=92 `VOL. 2 · 제2호`——KIT 表值 `VOL. 2 · 제2호` **一致** ✓
  - W43 副标实测：y=330 `프랑스어 주간지 · VOL.2 · 깊은 가을 · 명절`，尾 `깊은 가을 · 명절`——KIT 表值 **一致** ✓
  - 订正后 KIT 的徽章/页线/gloss 前缀/P8 分隔符表值亦与本版实测逐项一致 ✓

## 门 8 — 图片

- 3 张 payload（base64 解码后 sha256 + 字节数）分版 = 核心：
  - P1 Atget：`f3705af2…` 334,674 字节，放置 (65, 1874, 896×320) = 核心
  - P2 Hiroshige：`5b772fac…` 646,242 字节，放置 (1451, 200, 434×480) = 核心
  - P3 Blanco：`be071fda…` 142,340 字节，放置 (1451, 200, 434×540) = 核心
- credit 行（文本节点，分版 = 核心，同坐标）：
  - P1 y=2271.3 `Eugène Atget (1857-1927), photographie, domaine public`
  - P2 y=757.3 `Utagawa Hiroshige (1797-1858), estampe, domaine public ·` + y=777.45 `LACMA`
  - P3 y=842.95 `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, …`
  - 作者/年代与素材元数据（Atget 1857–1927、Hiroshige 1797–1858 / LACMA、Blanco《Flora de Filipinas》）一致，credit 行确已放置 ✓

## 门 9 — 网页版 PDF

- 网页 PDF：8 页，每页 1 张 JPEG 流，标题 `Le-Lucerna-VOL3-KO-web`；印刷 PDF：8 页（矢量）。
- 从本版卡片新鲜生成（Pillow，resolution 150，与 render.py 同配方）并逐页提取 JPEG 流逐字节比对：
  - **q75：8/8 流相同**（各页字节数与 sha 前缀逐页一致，如 P1 648,877 字节 `b30977f6cc20`、P8 828,941 字节 `98544f3ac252`）
  - q72：0/8 相同（各页均更小，如 P1 617,603 字节）——建造员“q75 相同、q72 不同”的结论**独立实测成立**；流 = 卡片编码才是门，门通过。
  - 自有复现的网页 PDF 整文件哈希与交付不同，唯一原因是 PDF 元数据时间戳（交付 CreationDate/ModDate `D:20261028062148Z`，复现 `D:20261028063406Z`，标题相同；JPEG 流 8/8 相同）——内容一致，非内容差异。
- pdftoppm 150dpi 逐页 vs 卡片像素比对：8 页尺寸均为 1950×2700；mean|diff| P1–P8 为 5.71 / 5.54 / 5.13 / 5.66 / 4.55 / 4.77 / 5.76 / 8.44（q75 JPEG 伪影量级）；P8 较高源于其最密文本（亦为最大 JPEG 流），四象限均值 4.45 / 6.62 / 9.72 / 12.99 呈密度梯度，无空白页、无移位页、无离群页 ✓

## 门 10 — transform 单独复现（阻塞级）

- 方法：自有 scratch 内全新核心拷贝（`weekly-report-w45-fr-build`）+ 建造树 `transform.py` 单文件（仅此一文件取自建造树），OUT 重定向至自有复现版目录，依次运行 `TRANSFORM_ROUND=1,2,3,4`（每轮独立进程、独立日志、不经管道掩盖退出码），再以建造树 `render.py` 单进程渲染。
- 轮次结果与建造员披露的过程问题逐项对应：
  - R1 exit 0；**R2 exit 1**——与建造员披露的 (a) 完全一致：`content8.py` 的 section-2 apply 在错放的 content12 对（`"2일 월요일에 프랑스 전역이 복교해요"`，content8 中 0 处）上断言失败，content8 当轮未写入，而同轮先行的 content56/12/34/7 已保存；R3 exit 0（应用 remainder：content8 五处 E 提示缩短 + content12 的 P1 #4 键注缩短）；R4 exit 0（终版 transform.py 的 R4 旧串已为正确码位，见下）。
  - 建造员 R4 首跑日志的断言旧串经码位实测确含笔误：`17읽부터`（U+B144）；终版 transform.py 的 R4 旧串为 `17일부터`（U+C77C，7 处全为正确形式）；交付纸面 P8 中该句确为正确形式 `프랑스어로: 학생들은 10월 17일부터 방학이에요.`，笔误串 `17읽부터` / 旧句 `방학 중이에요` 在交付纸面中均为 0 处 ✓
  - 无混合状态残留：复现终态 content 文件与建造树终态 content 文件除 OUT 重定向行外**逐字节相同**；复现渲染日志流值与建造 build4b 日志逐项相同（电池 1410、答案 2187、各页累计 10/25/43/61/78/96/108/150）。
- 复现 vs 交付：**SVG 8/8 逐字节相同、卡片 8/8 逐字节相同、印刷 PDF 字节与 sha 完全相同**（15,453,079 字节，`994fff…14e26`）——最终交付确为干净完整 transform 应用的结果 ✓
- 改动范围（不接受建造员“仅 content8 → 仅 P8 + PDF”的无哈希推断，改以自有测量为准）：
  - 自有 R3-only 渲染（全新核心拷贝 + R1–R3）vs 自有终版渲染：**仅 P8 SVG 与 P8 卡片变化，其余 7 页 SVG/卡片全部不变**——R4 范围以自有哈希差分实测成立（P8 + 由其派生的 PDF）。
  - R1→R3 范围抽查：建造树 `pre-fix-round2.sha` vs `final-round4.sha`：P1、P4 不变，其余 SVG/卡片/PDF 变化——与建造员所述一致；结合自有 R4 差分，R2+R3 的变化页为 P2/P3/P5/P6/P7/P8，链条闭合，无矛盾。
- 结论：transform 复现**通过**，过程问题均已验证不影响最终交付。

## 门 11 — 工具链口径

- 建造员称无独立 run.py 步骤、SVG 生成为 render.py 单进程 import——实测成立：建造树无 run.py；`render.py` 在同一进程内依次 import content12/34/56/7/8（登记表单次累计 1–150，复现 dump 总量 150、分页与级别与核心一致），满足 README #7 单进程重渲染要求；共享登记的模块未在核心建造目录内单独导入（全部操作均在自有 scratch 拷贝内，OUT 已重定向；核心终态哈希不变已证）。
- `render.py` 一律用 venv python：本校对全部运行均用 `tools/venv/bin/python`，与记录一致；复现渲染 exit 0（首轮 PDF 写失败仅因自有复现树缺 `scratch/` 目录，补目录后干净重跑 exit 0，属复现脚手架缺口，非建造缺陷——SVG/卡片/PDF 终态均已 8/8 验证）。

## 门 12 — ABSTRACT

- 文件：单行（1 行，187 字，末尾换行），韩语，ASCII 双引号 **0**，Han 表意字 **0**，全文：
  > Le Lucerna 프랑스어 주간지 VOL.3: Rolex Paris Masters 결승 주말, Peur sur le Parc 할로윈, Goût du Large 가리비 축제, Pitchfork Paris, 국민의회 2027 예산 주간을 프랑스어 텍스트와 한국어 해설로 읽고 A2부터 B2까지 150개 연습 문제로 프랑스어를 공부하세요.
- 要素逐词刊内出处：
  - 刊头 `Le Lucerna` + `프랑스어 주간지 VOL.3`：P1 刊头 ✓
  - 真实主题关键词：`Rolex Paris Masters`（P1/P4）、`결승 주말`（VOL.3 副标尾）、`Peur sur le Parc`（P3）、`할로윈`（P3）、`Goût du Large`（P1/P4）、`가리비`（P1 gloss `la coquille Saint-Jacques 가리비`）、`Pitchfork Paris`（P5）、`국민의회 2027 예산`（P6 国民议会 2027 预算周）✓
  - 学习者短语：`프랑스어 텍스트와 한국어 해설로 읽고`（徽章串原形）+ `A2부터 B2까지 150개 연습 문제로 프랑스어를 공부하세요`（级别 A2–B2、150 题均与登记表一致）✓
- “桥接”：交付纸面（SVG 文本节点）、ABSTRACT、建造代码（transform.py + content + bslib4）与 KIT 中**出现 0 次**（KIT 自述元语言句的例外情形未触发——KIT 内亦无该词）。门通过。

## 门 13 — 全部 8 张卡目视检查

- P1：刊头徽章居中 BRICK、Atget 照片 + credit 行、QUIZ 栏完整，无重叠 ✓
- P2：Hiroshige 图 + credit、日期表、练习栏完整 ✓
- P3：Blanco 菊花图 + credit、万圣节/诸圣节栏完整 ✓
- P4：`41e édition en 2026 (40e anniversaire)` 在 chiffres 栏在位、网球栏完整 ✓
- P5：PARIS CREATOR WEEK 裸标题（R2 修复在位）、音乐栏完整 ✓
- P6：日历表标签全部完整、TROIS DATES 框内边距充足（卡面确认门 4 的 1852 测量）、对比栏完整 ✓
- P7：金句/诊所/读者角/预告四区完整；读者框底余量与预告框底余量卡面可见；读者角点评行 `최고 / 의 P8` 为 1 音节尾换行（标准内，见非阻塞观察 5）✓
- P8：电池区（135–139 韩语指令动词 + 法语句子完整）、H 写作栏 + MODÈLE 范文、答案区 1–8 面分隔符与 150 指引键完整；电池/答案边界清晰，无条带穿越 ✓
- 另看重点裁切：P1 刊头、P6 日历区、P7 读者角+预告、P8 电池区、P8 答案尾——均无缺陷。

## 非阻塞观察（单列，不计入阻塞项，不影响 ZERO PROBLEMS 结论）

1. **建造员 P6 右缘/框线数值订正**：建造员 checks-final 称 P6 TROIS DATES 右缘 1935 / 框线 (1469, 1350, 1935, 1371)。自有规范墨迹法（全部 Noto 面实测：Sans 1835.25、Serif 1866.2、Bold Serif 1879.5）与卡面像素（1852）均不可复现 1935；分版与核心在该节点上完全相同且在 guideline 与框线内。实际 >1885.5 的节点是 3 处 P8 冻结法语选项（分版 = 核心，卡面 ≤1902 < 内框线 1910）。裁决结论不变（继承、无需改动），仅节点归属与数值以本次实测为准。
2. **法语词多重集 shorthand 的精确偏差**（解释层，非正文）：P7 `VOL` +1 / `P` +2 来自读者角韩语文本中的 `VOL.4` / `P8` 指称；P8 `présent` −1 来自 #120 注的韩语改写（核心注 `si + imparfait → conditionnel présent`，分版注 `si + imparfait → conditionnel`，规则内容等价，`j'` 省音说明两版齐全）。三者均非冻结法语正文改动，不构成冻结 breach；但建造员“除 Traduisez 外逐页相同”的简述应以本报告的精确差分表为准。
3. **coquilles 计数口径**：建造员“9 = 9”为 P8 复数口径（P8 `coquilles` 9=9）；全报复数 10=10、含单数子串 15=15，全部相等。
4. **R4 范围声称的升级**：建造员原为无哈希推断；本次以自有 R3-only vs 终版双渲染哈希差分实测确认 R4 仅动 P8（+ 派生 PDF），推断升级为实测。
5. **读者角 1 音节尾换行**：点评行 `최고 | 의 P8` 与披露行 `싣습니 | 다` 为 1 音节尾换行，符合 ≥3 音节尾标准（R1-2 先例亦以 1 音节尾为标准内），卡面可读，无缺陷。
6. **P8 网页 PDF 像素差较高**：pdftoppm vs 卡片 mean|diff| P8 为 8.44（他页 4.5–5.8），源于 P8 最密文本的 q75 JPEG 噪声（四象限梯度与文本密度一致），非离群页。
7. **网页 PDF 整文件哈希差**：自有复现与交付仅差 PDF 元数据时间戳（CreationDate/ModDate），JPEG 流 8/8 相同，内容一致。
8. **流游标数字**：P1-hiver 2298（底线 2290）、P6-ex 2557（底线 2540）两处超底线数字在核心日志中逐字相同，属继承行为；绝对墨迹底在页内，不作溢出论。

## 结论重申

**ZERO PROBLEMS**——13 门全部独立重测通过，无阻塞项。本报告仅交协调员作上架串行决策参考；校对员未上架、未发 Discord、未往主聊天发卡片/PDF。
