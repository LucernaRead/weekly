# 校对笔记 — 2026-W47 en-de 第一轮独立复校（叶子）

- 版：`2026-w47-en-de`（英语目标语 × 德语读者版），VOL.4，8 版，150 题
- 校对员：叶子（第一轮独立复校；与 builder、core-en builder、各轮复校员不同人）
- 日期：2026-11-11（UTC 07:41–08:05 左右）
- 依据：SOP §8 / §1.1、`AGENTS.md`、本版 `WEEKLY-KIT.md`、`scratch-fanout-en/FANOUT-REPORT-en.md`
- 只检查、不改源码/成品；未碰 core-en、W43–W46、其他目标语家庭、tools/；未跑 insert.py、lint --write，未 git add/commit/push/reset/stash。

## 身份核对（先核身份，通过）

版目录内实际文件名（注意 `.web.pdf`  点式命名）：

| 文件 | 字节 | SHA-256（实测完整串） | 与 KIT 登记 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-de.pdf` | 29,330,795 | `6d91162fac10c81e59ec811362136cd69e4e535a5b7ad04b4b98c94d530d95ba` | 一致 |
| `The-Lucerna-VOL4-en-de.web.pdf` | 2,377,924 | `e8c6746167d7351e0cda55427ec191da98af9112e94f281cf390e5488f28d751` | 一致 |

两 PDF 均为 8 页、1462.5 × 2025 pt。身份相符后开工。

## 结论：(b) 缺陷清单 — 1 条缺陷（轻微，版式类）

本轮不是零问题。以下 1 条需修（修后按 SOP §8.4 须整期重渲染、从头再做一轮全量校对）。

### 缺陷 D1（轻微）— P7 金句第 8 条的出处行被孤立到第 3 栏顶部

- **页/位置**：P7（LANGUAGE IN HAND），第 3 栏顶部；印刷版与网页版均有（同源 SVG）。
- **原文（实际呈现）**：
  - 第 2 栏底部：第 8 条金句以 `Senate, and for governor in 36 states.”` 结束（`svg/p7-lang.svg`，x=538.5，y=2526.47）。
  - 第 3 栏顶部孤立一行 `—— From page 1 of this issue.`（x=989.0，y=219.0），其下紧接 `THE DRILLS　Übungen`（y=275.6）。
- **应为**：出处行应紧跟在其金句之后（与本版其余 7 条金句一致；与 core-en 一致：core 的同一出处行在第 2 栏 y=2321.28，紧跟金句末行）。
- **证据**：
  - 从印刷 PDF 全新渲染的 P7（非 builder 的 card 图）目视确认；网页版 P7 同位置渲染亦确认（裁图存 `render/p7-col3-top.png`、`render/w-p7-col3-top.png`）。
  - SVG 坐标核实：本版 8 个出处行 y 值 1468.48 / 1574.95 / 1714.79 / 1854.63 / 1994.47 / 2167.68 / 2340.89（第 2 栏内）与 219.0（第 3 栏顶部）；core-en 8 行全部在第 2 栏内（末行 y=2321.28）。
  - 成因（推断）：德语讲解层比 core 中文讲解层长，金句栏整体下推约 260pt，最后一行出处溢出到下一栏。非遮挡、非缺字（occlusion 审计 0 flags；文字层完整）。
- **严重度**：轻微。全部文字都在、无错误内容、无遮挡/溢出；但读者在 THE DRILLS 栏顶会看到一行无所指的出处，是肉眼可见的版式缺陷。

## 全量复校结果（逐项，均已查）

1. **8 版印刷版逐版目视**（从印刷 PDF 用 pdftoppm 全新渲染 110 dpi，非 builder card 图）：P1–P8 均读完；除 D1 外无溢出、重叠、压页脚、截断、豆腐块。网页 P1、P7、P8 亦渲染目视，与印刷版一致。
2. **150 题逐题验算**：registry 150 条，编号连续 1–150；分版 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；分级 A2 62 / B1 66 / B2 22；与 KIT 登记一致。逐题对照题面/原文/图表验算答案，全部正确（含：Q84 “33 of 35”=20+13；Q87 254+162+19=435；匹配题字母映射逐项核对：P2 24=b/25=c/26=a/27=d；P3 38=b/39=d/40=a/41=c；P4 56=b/57=c/58=d/59=a；P5 74=d/75=a/76=b/77=c；P8 141=b/142=c/143=d/144=a）。
3. **金句 8 条逐字比对正文**：8 条全部逐字见于本期正文，出处页码全部正确（P1×2、P2、P3、P4、P5、P6×2）。P7 呈现顺序与 KIT §5 顺序不同，但 8 条齐全、文字逐字一致。
4. **禁词扫描**：可见文本扫描 `W47 / 2026-w47 / 2026-W47 / cover / SOP / proofread / TODO / Lorem / placeholder / en-de / zh-cn / XXXX / TBD`，零命中。内部结构标记（周次、语言代码、仓库链接、“cover”、内部流程词）无。
5. **VOL.4**：P1 刊头 VOL.4；全部 8 页页脚 `ENGLISH WEEKLY VOL.4`；VOL.5 提及 8 处（P2 1、P3 1、P6 2、P7 3、P8 1），与 core 一致，均为合法下期预告；VOL.3 提及 P6 1、P7 2，与 core 一致（“VOL.3 promised real letters…”）；无错印 VOL 号。
6. **徽章逐页计数与级别**：两种独立方法（徽章文字计数、徽章色小矩形计数）逐页核对，de 与 core 完全一致：P1 16、P2 15、P3 16、P4 16、P5 16、P6 19、P7 13、P8 23；各题徽章级别与 registry 一致（抽查 P8 Q113–120 选项级、B2 137–140、145–149 “Levels: 145–149 [A2]”、H “Schreiben [B1]”均在版）。
7. **P8 最小字号**：`svg/p8-test.svg` 全部 font-size 集合最小值 13.5pt ≥ 9.75pt（SOP §1.1 底线），无需让步。
8. **日期/星期**：全部日期逐个用日历核验：11月3日周二、11月8日周日、11月9日周一、11月10日周二、11月16日周一、11月18日周三、11月19日周四、11月20日周五、11月21日周六、11月22日周日、11月26日周四、11月27日周五、12月1日周二，全部与正文一致。佐治亚决胜轮 12月1日（投票后 4 周）正确。
9. **事实抽查**：
   - “密西西比无决胜轮（常规选举，得票最多者获胜）”——经公开来源核实正确：密西西比州务卿已确认常规联邦大选无决胜轮；2018 年决胜轮是特别选举（规则不同）。来源：the-downballot.com、congresscountdown.com、msindy.org（2026-11 报道）。
   - P3 图注 “Rousseau《Surprised!》(1891)，一生未离法国”：画作 1891 年无误；Q44 “Rousseau (paint) jungles he never saw” 有图注为据。
   - 人名拼写（见下专项）全部核对无误。

## 翻译层专项（fan-out 特有）

- **讲解/界面语言确为德文**：全部讲解层、栏目标题、家具、页脚、答案简析均为德文；无英文讲解残留、无中文讲解残留。
- **核心 CJK/源语字面量转写**：freeze diff 核实——新增 CJK 字符共 9 个，全部为 U+3000 表意空格（家具分隔符）；可见文本零真实 CJK 字符；唯一 CJK 字符是 P1 非可见 SVG `<title>Lucerna 三色蛾</title>`（与 core 共有，非可见文字），已逐处说明。
- **E 组中文句答案键已译成德文**：137 “Die Demokraten haben das Repräsentantenhaus und den Senat gewonnen.”、138 “Die Auszählung geht weiter.”、139 “Der neue Kongress tagt ab Januar 2027.”、140 “Brich das Schweigen.”——译文准确；150 为开放题短标签（与 core 短标签模式一致）。
- **德语质量抽查**：家具与讲解德语通顺正确（如 “So sagt man das Datum” 已修正；“Wahltag 3. November · Demokraten gewinnen beide Häuser”；“Relative Beliebtheit, keine exakten Suchzahlen.”；P7 工具箱三句译文；读者园地德文段；P8 写作题德文说明）。未发现德语拼写/语法错误。
- **核心英文层未动**：freeze diff 显示新增串全部为德语讲解/家具或重排的 P8 答案行；删除串全部为中文讲解层、W46 惯例的 gloss-box 英文行、重排的 P8 答案行、“Translate:”→“Übersetze:” 等预期替换；无英文正文改动。

## U+2019 缺陷类回归

- 8 个 SVG 全扫：U+2019 总数 **0**（逐文件均为 0）。
- 目视抽查含撇号的行（P1 “president's four-year term”、P4 “Cummins's place”、P5 “Friday's Words” 等）：无宽字形、无断裂间隙，ASCII 撇号渲染正常。

## P8 答案注文人名专项（人工逐条核对公开来源，未只信机械门）

P8 印刷答案注中出现的人名（其余人名只在题面/正文，不在注中）：

| 注中人名 | 呈现 | 核对 |
|---|---|---|
| Joseph Zada（Q29 注） | “Joseph Zada spielt den jungen Haymitch” | 正确：饰演青年 Haymitch 的演员（P3 正文亦同名） |
| Ralph Fiennes（Q31 注） | “Ralph Fiennes spielt den jungen Präsident Snow” | 正确：饰演青年 Snow 总统的演员（P3 正文亦同名） |
| Collins（Q42 答案句） | “Collins published the novel in 2025.” | 正确：Suzanne Collins，《Sunrise on the Reaping》作者，2025 年出版（P3 正文全名） |
| Rousseau（Q44 答案句） | “Rousseau painted jungles he never saw.” | 正确：Henri Rousseau（P3 图注全名），画中丛林未亲见 |
| Haymitch（Q43 答案句） | “Haymitch won the 50th Games.” | 虚构人物，与 P3 正文一致 |
| Tom（Q129–132 注） | “Tom ist Lehrer in Manchester / Tom trägt eine rote und eine blaue Socke / Toms Klasse liest über die Wahl” | P8 阅读题虚构人物，与题面一致 |
| Maya（P8 完形题干） | 虚构学生，与题面一致 | — |
| ITV（Q45 答案句） | “ITV chose Monday for the launch.” | 机构名，与 P3 正文一致 |

另：Q47/48/51 的注（Cummins / Steve Smith / Sinner）在印刷版 P8 答案区为简写形式（只印键，无人名注）——与 core 同模式，非缺失。**本版无日语家庭式的罗马字人名问题；P8 全部注文人名无拼错。**

## 机械门全套自跑（结果见 GATE-LOG.md）

- occlusion（tools/venv）：selftest OK，**0 flags**。
- p8 extract：noted set 60/150，与 core 集合相同。
- p8 compare：**CLEAN**，missing=[]、extra_count=0、uncertain=[]；keydiff=[137, 138, 139, 140, 150]，均为预期内（德语翻译键 + 写作题短标签；W46 en-de 同样 keydiff）。
- p8 extract keys vs registry：150/150，唯一差异为 Q150 短标签（印刷 “Offene Aufgabe” vs registry 全文），与 core 同模式。
- freeze：直接 sha256 比对再生 SVG 与送审 SVG **8/8 MATCH**（见 GATE-LOG 关于 freeze.py baseline 因磁盘配额改走等效瘦复制的说明）；freeze diff：新增 CJK 仅 9 个 U+3000。
- print/web 文字层：pdftotext 各 48,076 字节，token 多重集差 0/0，字节完全一致；web PDF 2,377,924 字节 < 7 MB。
- run.py 重跑：exit 0，零 OVERFLOW / TOO WIDE；全部 flow 末端 y 在底线内（最紧 P1-countries 2298/2300）；TOTAL exercises 150；MODEL words 82。
- model 文 82 词（alphanumeric-token 计），在 80–100 词要求内。
- text.md 51,989 字节（与 KIT 一致）；ABSTRACT.txt 628 字节，德文单行，零 ASCII 双引号。

## 观察项（单独列，不计缺陷）

1. **P2 A 组说明 “Ergänze die Sätze nach Datum und Uhrzeit.”**：本周 5 道题全部是日期、无钟点题；“und Uhrzeit”用词偏宽。但这是 core 中文说明 “根据日期与时间” 的忠实翻译，且 W46 en-de 同款写法（当时 SAY IT 教钟点）——属模板通用措辞，非本版新错。
2. **ABSTRACT.txt 两处措辞偏松**（正文无误，仅摘要）：(a) “Die geprüften Ergebnisse der US-Zwischenwahl”——“geprüft”易与“认证结果”混淆，而正文反复强调 AP call 不是认证结果（认证期 11月10日–12月18日，摘要后半句亦写明）；(b) “am Samstag, 21. November, … das ATP-Finale in Turin”——ATP 决赛在周日 11月22日，周六是半决赛；正文 P4/P6 写法正确（周六半决赛、周日决赛日）。
3. **引号方向**：德文引文用 «…»（法式/瑞士式），如 P8 “«Mein Montag, der 16. November»”、答案注 “«Break the Silence»”；标准德语常用 »…« 或 „…“。全版一致，非错（瑞士德语即用 «»）。
4. **“Anmerkung | Erklärung |” 双前缀**：P2/P3/P4/P5/P6/P7 的 Erklärung 框均有双前缀——KIT 已记为已确认的 W46 惯例，本轮核实为有意保留，非缺陷。
5. **P8 印刷答案注为节选**：150 条 registry 注中 83 条未印在 P8 答案区（只印键或短注）；core 同模式（96 条未印），属模板惯例，非缺失；键本身 150/150 齐全。
6. **版面留白**：P3 第 3 栏止于 1619、P4 第 3 栏止于 1713、P5 第 2 栏止于 597、P6 第 3 栏止于 1256——与 core 相同的模板 flow 行为，KIT 已记。
7. **P1-countries flow 余量仅 2pt**（2298/2300）：在底线内，无溢出；仅记一笔。
8. **freeze.py baseline 未能按原样跑**：整树复制时磁盘配额（EDQUOT）爆满中断；改用等效方式（同一 tools/venv 解释器、同一构建源码的瘦复制）重跑并逐字节比对，8/8 一致。详见 GATE-LOG.md。

## 未核查项

- 无。本任务清单内各项均已核查（身份、8 版目视、150 题、8 金句、禁词、VOL、徽章、P8 字号、翻译层、U+2019、P8 人名、全部机械门、print/web 一致、run.py 重跑）。
