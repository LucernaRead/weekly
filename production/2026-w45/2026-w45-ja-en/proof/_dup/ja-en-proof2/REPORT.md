# W45 JA × EN 第二轮独立校对报告（全新完整校对，只校对，不改源码，不宣布上架）

- 校对对象：`files/weekly-report-w45-ja-en/`（svg×8、cards×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-ja-core/`（JA VOL.2，只读，未改动）
- 构建树（只读）：`hidden_files/weekly-report-w45-ja-en-build/`（pre-fix 基线 `sha256-fix5-prefix.txt`）
- W43 同配对对照：`files/weekly-report-ja-en/`（VOL.1，只读，未改动）
- 校对方式：全部 10 类门从头独立重测，第一轮的通过结论一律未沿用；规范工具均用
  `tools/venv/bin/python` 现场重跑；冻结基线用我自己的 scratch
  （`hidden_files/w45/ja-en-proof2/scratch-baseline/`），未碰共享 `tools/scratch/`，
  未清理共享 scratch 目录。本轮校对脚本为本目录 `proof2.py`，输出 `proof2.json`。
- 未做事项：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、
  未改核心/W43 目录、未派生任何下级代理、未宣布上架（上架由主线串行执行）。

## 结论：ZERO PROBLEMS

第一轮的唯一阻塞项 B-1（P8 #37 中文注释）已修复，修复范围恰好收敛于 P8 + 双 PDF，
其余 10 类门全部独立重测通过，无新增阻塞项。非阻塞观察单列于文末，不影响放行判断。

---

## 0. 开工查重与无变动证明

- 开工时 `ps` 无属于本版的渲染进程；交付物最新写盘（KIT 01:37:20 UTC）至开工
  （01:40:27 UTC）已静默 187 秒，超 60–120 秒区间，属已完成交付，不是 stand down 理由。
  校对全程未见新的写盘。
- 校对前后 sha256：`sha-before.txt` 与 `sha-after.txt` diff 为空（本版 20 文件）；
  核心 `sha-core.txt` 与 `sha-core-after.txt` diff 也为空（核心 20 文件）。
  冻结基线重跑亦确认核心 8 个 SVG 在跑前跑后均未变。
- 方法注记：冻结基线第一次误以分版构建目录为 `--build`，结果 0/8（复现出的 8 个哈希
  恰好等于分版哈希，可作分版可复现的旁证，核心完整性该次亦未变）；纠正为核心构建目录
  `hidden_files/weekly-report-w45-ja-build/` 后为 8/8（见 §3）。报告中的 8/8 指后者。

## 1. 修复专项（B-1）

- P8 #37 印刷行（答案区，SVG 坐标 x=65、y=2516.548，第 1 栏）：
  `37. 8 — The exhibition runs to November 8`——键 `8` 不动，注释确为英语。
- P8 150 条答案行与核心逐行比对：**与核心完全相同的行确为 0 条**（`p8_identical_lines: []`）。
  即再无应英文化而与核心相同的行。
- 全版简体专属字扫描：`艺` 在分版 8 页均为 0（核心 P3 1、P7 1、P8 6 均已随本地化消除）；
  以简体专属字集计，分版独有（核心同页所无）的字符 8 页均为 []，真阳性 0。
  唯一 raw 命中 P4「点」为核心同页共有的冻结日语字，非残留。
- 旧串 `工艺展到11月8日` 在分版全部 8 个 SVG 中为 0；新串 `The exhibition runs to November 8`
  在 P8 出现 3 次，分别为 #32（带 `(Sunday)` 后缀）、#37、#122（同一事实的不同题），均合理。
- #37 事实核对：P3 题面 `展覧会は11月 ___ 日（日）までです。` 在核心与分版均存在；
  `date -d 2026-11-08`：东京 JST 与多伦多 EST 均为 **Sunday**；英文注释“展览到 11 月 8 日”
  与题面事实一致（#37 不带 Sunday 后缀与 #122 同式；带后缀的 #32 另有其题面依据）。
- 根因核实（仅记录，不影响放行）：现行 `transform.py` NOTES 中确有 FIX5 注释行
  `# FIX5 B-1: P8 #37 bare note … previously missing from NOTES` 及新增条目
  `("工艺展到11月8日", "The exhibition runs to November 8")`（第 97 行），其近邻为
  第 89 行传统…条目与第 94 行 #32（周日）条目，与“此前缺失裸串”的说法一致。
  但 pre-fix 版 transform.py 已被覆盖，无法直接 diff 前版源码，故该根因属间接验证
  （修复前印刷行为中文 + 冻结串范围恰好一换一 + 现行 NOTES 含 FIX5 注释），仅作记录。

## 2. 修复范围专项（独立验证，不采信修复员任一遍结论）

解析方法：只取基线文件中严格匹配 `^[0-9a-f]{64}\s+\S+$` 的哈希行（字节数行、
说明行一律排除——这正是修复员第一遍误报的根源），按文件名与现行实测哈希比对。

- 18 件交付物：**恰好 4 件变化**——`p8-tesuto.svg`（65b63e637613…→a7433832d190…）、
  `p8-tesuto.png`（8b28f8e7d8d6…→641e290f07c7…）、`Lucerna-VOL2-EN.pdf`
  （a213dcf6357b…→abb86daf0ff1…）、`Lucerna-VOL2-EN-web.pdf`
  （394b93996688…→5a4893e50047…）；其余 7 页 SVG + 卡片 14 件字节不变。
  KIT 与 ABSTRACT 不在 18 件内：ABSTRACT 哈希与基线一致（未变）；KIT 在渲染后另有
  文字修订（见 §12），不属于纸面变化。
- 构建树：10 个关键文件（transform/run/render/content12/34/56/7/8/bslib4/svglib）
  中**仅 2 件变化**——transform.py（005c6a0b…→c858f930…）与 content34.py
  （0570cb3c…→935c4fe4…，为 transform 再生成的 P3 内容模块）；其余 8 件字节相同。
- 冻结串范围（与第一轮校对的 pre-fix 冻结 json 比对）：P1–P7 的 added/removed 串集合
  **完全相同**；P8 恰好一换一——新增 `37. 8 — The exhibition runs to November 8`，
  移除 `37. 8 — 工艺展到11月8日`。与构建树 `freeze-diff-fix5.json` 比对则全部 8 页
  完全相同。无超出 P8 + 双 PDF 的变化。

## 3. 冻结 / CJK / 违禁词 / 规范文件

- `freeze.py baseline`（核心构建目录，自有 scratch）：**8/8 逐字节复现**，核心哈希与交付一致。
- `freeze.py diff --strict-cjk`（exit 0）：全 8 页新增 CJK 字符 **0**；
  每页 CJK 总量：P1 1406→1275、P2 1312→1161、P3 1172→1051、P4 1263→1169、
  P5 1247→1132、P6 1186→1101、P7 1676→1308、P8 **2721→1448**。
  P8 算术核对：被移除的 #37 中文注释 `工艺展到11月8日` 含 CJK 字符恰 6 个
  （工/艺/展/到/月/日；数字 11、8 不计），1454 − 6 = 1448，与修复员说法逐位一致。
  （注：本轮 json 的 added/removed 串数为去重串数，如 P2 +23/−20；门禁日志的 +31/−28
  为出现次数加总，底层 json 与 fix5 json 逐页相同，非数据出入。）
- 违禁词「桥接」/「橋接」：SVG 全部 + KIT + ABSTRACT 均为 **0**。
- 规范 `svglib.py` md5：`d73e23b365676c3618d7e060b835eb4d`，与标称值一致，未被编辑。
- 日语正文无丢失：全部 removed 串逐页审读——均为中文讲解、家具中文半句、P8 中文注释、
  读者园地中/日披露句及其换行碎片；句末 。 缺失的 25 串（P1 3、P2 3、P3 3、P4 2、P5 3、
  P6 1、P7 9、P8 1）逐一核对，均为中文侧串或其换行碎片（如 `这四个话题，都是本期报纸的主题。`、
  `写作题（无唯一答案）；范文（167 字）见下。`、P7 披露碎片 `ます。`）；
  无一条独立日语文章/题干/图表注句被删。P6 图表注句
  `このグラフは練習用データです。数字は全部で100%になります。` 核心=本版逐字同。

## 4. 日语专项：行首禁则与词级中文残留

- 行首禁则：标准集（、。．，」』））】〕）下，核心=本版=**全 8 页 0**；
  含 〜 的宽口径下，P1–P6/P8 仍为 0，P7 核心=本版=各 1 项，为同一条 B2 词条行
  `〜倍 times · 〜% percent · 〜万食 …`（核心为中文 gloss 版），属词条首字设计而非换行溢出，
  **新增 0**（见非阻塞观察 O-1）。
- 词级中文残留：本版每页全部 CJK 词串均是同页核心文本的子串
  （`cjk_runs_not_in_core_page` 全页为空）；简体专属字分版独有字符全页为空（见 §1）；
  共享汉字词逐词核实：全国（冻结日语文章/题干串与核心逐字同）、会社
  （`学校も会社も休み` 核心=本版）、来週（`来週 · Next issue (VOL.3)`，仅家具半句英文化）；
  `仮装` 为合法日语词（核心亦有），非残留。

## 5. 腐蚀修复复核（重新抽查，非沿用上一轮）

- P1/P4/P5/P6/P8 的 removed↔added 近似配对（difflib >0.5）全部重跑：
  含假名双侧配对共 37 对（P1 4、P4 2、P5 3、P6 1、P8 27），逐对审读——
  **全部为合法本地化**（日语键/词头保留、中文注释→英语注释；或家具日语半句保留、
  中文半句→英语半句），无一对日语→日语小改动腐蚀对（无缺 。、无改写、无断句）。
  例：P1 `毎週、日本語で · 每周一期 · …` → `· Weekly · …`；P8 #133 键
  `私は火よう日に金沢へ行きます。` 保留、注释 `主语＋时间＋地点＋动词` → `subject + time + place + verb`。
- 冻结句复原：P1/P4/P5/P6/P8 全部冻结日语句在核心与本版交集中逐字存在；
  句末 。 完整性仅中文侧串缺失（见 §3），日语句无缺字断句。
- Weekday 后缀：分版 P8 答案注释中日语 weekday 串（月～日よう日、（周×））为 **0**；
  唯一含 `火よう日` 的是 #133 的键本身（被教的日语句），注释为英语。
- 专名注释：P8 专名注释均为英语（如 `The Kobe illuminations…`、`Suginami`、
  `Kanazawa Castle`），无残留中文专名注释。
- P1 趋势盒两行独立实测（PIL/NotoSansCJK，与 svglib 同字体）：
  `Dates in articles; not exact statistics` = **312.4 px**，
  `These four topics shape this issue.` = **293.2 px**，均 < 390 px 槽内宽；
  P1 卡片目视两行均在槽内。

## 6. P7

- 定义句：P7 定义段落核心=本版逐字同——框架句
  `『ゆるく整える』 — ゆるく（無理をしないで）＋整える（体と心をよくする）。忙しい人でも、ゆっくり体を整える、という意味です。`
  拼接比对 identical；诊所日语例句（`金沢に紅葉を見ます → 金沢で紅葉を見ます`、
  `「昨日」` 过去式、`「こと」` 名词化、`「か所」` 数场所）保留，仅讲解英文化。
  核心 P7 文本中以 。 结尾而分版缺失的 4 串逐一裁定：3 串为中文诊所讲解、
  1 串 `ます。` 为日语披露句的换行碎片（披露句按统筹裁定替换，见 §10），
  **定义句本地化 0 处**。
- 金句：8 句原文核心=本版逐字同；去空白全册拼接计数每句在核心与分版均为 **恰 2 次**
  （文章内 1 次 + P7 列表 1 次）。
- 页标签映射（以我自己的核心实测为准）：核心 第1面×2、第2面×2、第3面、第4面、第5面、第6面
  → 本版 **p.1, p.1, p.2, p.2, p.3, p.4, p.5, p.6**。
- P7 词框 gloss 仅本地化：三栏词条 A2 3 + B1 3 + B2 3 = **9**，词头逐字同
  （読書週間/紹介/読み聞かせ；見頃/紅葉狩り/落葉；〜倍/〜%/〜万食，
  末项 gloss 续行 `ten-thousand servings.` 完整）；B2 栏核心单行在分版因英文 gloss 更长
  而换行，内容完整无缺。

## 7. P8 keydiff 清单对齐专项（#139 歧义的独立裁定）

- `p8.py compare`（显式双路径，`--total 150`）：**CLEAN，150 = 150，missing [] extra []**。
  口径从核心 P8 渲染内容独立确立：核心 P8 本身即印 150 条注释（非 EN 核心的 78 口径），
  本版亦印 150 条；EXTRA_ONLY 不适用。
- 答案区印刷行（答案标题后、换行续行已拼接）与核心逐行比对：150 条全变（0 条相同），
  其中**印刷键（— 之前的部分）相同的为 147 条**，不同的仅 3 条：
  #137、#138（合法 E 区重定向，见下）、#150（范文指向语本身，见下）。
- p8.py keydiff 21 项 `[1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113, 115, 117, 118, 137, 138, 140, 146, 147]`
  与我重跑的输出逐项一致，分解如下（逐项贴出印刷行对照见 `proof2.json` 的 `p8_printed_diff`）：
  - 19 项印刷键逐字节同：17 项仅注释英文化（#1、#2、#7、#8、#9、#29、#32、#65、#69、#78、
    #113、#115、#117、#118、#140、#146、#147）+ #5/#101 括号分支伪影
    （印刷键分别为 **7** 与 **27**，两边逐字节同；p8.py 提取的分版键含 ` — <注释首段>`，
    是因注释含括号内英文 weekday `(Saturday)`/`(Tuesday)` 致提取分支切分所致，非键差异；
    提取对照：核心 `7` vs 分版 `7 — The Kobe illuminations start on the 7th`）。
  - 2 项 genuine 键重定向（E 区合法）：#137 键由中文句改为英语句
    `Culture Day is November 3.`；#138 键改为 `If you drop litter, the fine is 2,000 yen.`。
- **#139 的有无及原因（歧义裁定）**：#139 **不在** p8.py keydiff 内，且不属于 keydiff 项。
  其印刷行核心 `139. 読書週間は10月27日から始まります。 — 对照第7版`、
  分版 `139. 読書週間は10月27日から始まります。 — See page 7`——印刷键（日语句）逐字节同，
  p8.py 提取键亦同（`読書週間は10月27日から始まります。`），故两系统均不将其列为 keydiff。
  #139 的变化在练习区题面（核心中文提示 `读书周从10月27日开始。→ ___` →
  分版英语提示 `Reading Week starts on October 27. → ___`），与 #140 同属“题面改英语、
  键日语同”类，但 #140 因注释含括号续行换行（核心 `— 对照第6版（神` + 续行 `户的灯光秀）`，
  分版 `— See page 6` + 续行 `(Kobe illuminations)`）致 p8.py 提取键含注释前缀而进入 keydiff，
  #139 的注释为干净的单行 dash 式故未进入。第一轮报告“#139/#140 题面改英语而键日语同”
  的表述是把两者按题面类并列，并非称两者均为 keydiff 项；以本轮印刷行 + 提取键双重证据为准，
  #139 非 keydiff、#140 为提取伪影，均不构成缺陷。
- #150（非 p8.py keydiff 项，但印刷键字面不同）：核心 `150. ✓ 范文见本版 H 区（167 字）` →
  分版 `150. ✓ Model text in section H on this page (167 characters)`——该“键”本身即为
  范文指向语，英文化是规则要求，非键差异；p8.py 不将其列为 keydiff 与此一致。
- 结论：21 项 keydiff 中无一项无法归类；无阻塞项。
- P8 注释纯英语：47 条注释含 CJK 串，逐一核对均为被教的日语词头/引文/语法助词
  （如 `見頃 = best viewing season`、`The slogan is 「静かだけど、冒険中。」`、
  `place + で + あります`），无中文讲解残留；注释中的 weekday 均为英语
  `(Saturday)`/`(Tuesday)` 形式。
- 印刷笔记集合按题号相等：150 题号齐全，无缺无增（EXTRA_ONLY 可接受但未发生）。

## 8. 几何

- `occlusion_audit.py`（自检先行，6 类全触发）：本版 **0 flags**、核心 **0 flags**、
  NEW vs core **0**。
- 同基线墨迹碰撞扫描（同 y 文本墨迹盒 getbbox 交叠）：8 页均为 **0**。
- P6 图表标签基线锚定墨迹法（PIL getbbox，anchor ls，条形为后绘 rect）：
  4 个标签（38%/27%/21%/14%）与条形 rect 的最大覆盖均为 **0.000**，<30% 门通过
  （getbbox 法为错误口径，未采用；标签 x 均在条形右端之外）。
- 全页右缘 ADVANCE 扫描（advance width，限 x=1885.5）：本版 0、核心 0（本轮仅计分版；
  核心 0 为第一轮实测的复核引用，不计入本轮结论——本轮 occlusion 核心 0 已独立覆盖）。
- P7 预告带止点独立实测：SVG 底带 rect y=2406.12 + 高 118 = **2524.12**，
  <2540 内容限，距 2580 页脚线 55.88 px（≈56 px）；P7 非页脚最大文本 y=2490.12，亦在限内。
- 8 张卡片全部目视（1950×2700 原卡的 780 宽预览逐张查看，非抽查）：
  P1–P8 均无溢出、重叠、截断标签、错位框；P1 趋势盒、P6 图表、P7 预告带、P8 密集答案区均正常。
  P8 #37 另做全分辨率裁剪复核：`37. 8 — The exhibition runs to November 8`
  在其栏内（x=65，基线 y=2516.548），无溢出/重叠，距页脚线清晰。

## 9. gloss

- 渲染后 gloss() 串按 · 拆分，核心=本版逐项 1:1，总 **39 = 39**：
  P1 4、P2 9、P3 8、P4 7、P5 7、P6 4。
- 词头序列：P1/P2/P6 直接逐字同；P3/P4/P5 的表观差异（核心 `楽`/`確認す`/`守`/`話`
  vs 分版 `楽しむ`/`確認する`/`守る`/`話題`）经去空白拼接核实均为渲染换行碎片假象——
  去空白后的 gloss 块在核心与分版均含完整词头 `楽しむ`、`確認する`、`守る`、`話題`。
  故词头序列实质逐字同。
- P7 桥接式词条 9 项（见 §6），日语词头逐字同，gloss 均已英文化。

## 10. 读者园地

- 日语示例信逐字不动：核心与分版示例信拼接全文同
  （`「こんにちは。私は中学生です。読書週間には、図書館で本を2冊読みたいです。
  文化の日には、家族と金沢へ行きたいです。」— 読者の手紙の例`），零编造
  （无新增读者、姓名、引文）。
- 英语披露句逐字摘录（本版 P7，分行拼接）：
  > Editor's sample, not a real letter. No real letters or best Page 8 compositions
  > had arrived by the deadline; both will appear in VOL.3. Send us your letter in
  > Japanese — selected letters will be printed in VOL.3!
- 3 事实逐项核实：(1) 无真实来信（`No real letters` + `Editor's sample, not a real
  letter`）✓；(2) 无最佳 P8 作文（`No … best Page 8 compositions had arrived`）✓；
  (3) 样本 + 顺延 VOL.3（`both will appear in VOL.3`）✓。
- 显性祈使征集邀请：`Send us your letter in Japanese`（祈使句）✓；
  VOL.3 刊登承诺：`selected letters will be printed in VOL.3!` ✓。
- 中文披露句与日语披露句均未作为 operative 披露残留：核心中文披露
  （`编辑部示例信，非真实来信…`）与日语披露
  （`※この手紙は編集部の例です。…優秀作は届きませんでした。VOL.3に載せます。`）
  在本版 P7 均已移除（碎片检索 4/4 为 False），仅英语披露为 operative；无双 operative 披露混淆。
- 最佳 P8 作文覆盖范围裁定：披露句的 `both` = 真实来信 + 最佳 P8 作文（泛指类别，
  非单篇）；VOL.3 预告行 `読者の手紙と第8版の作文の優秀作も載せます` 与之呼应，
  覆盖“选登的最佳 P8 作文”，非全部作文。
- 内容预告行（`来週 · Next issue (VOL.3)` 段）为内容预告，不计入邀请——邀请
  仅以披露句内的祈使句为准，已单独成立。

## 11. 家具 / W43 三方测量

三方：W43 同配对版（`files/weekly-report-ja-en/`，VOL.1 已发）、W45 核心、W45 本版。
W43 同配对家具胜过 README #20 泛化规则；下表刊头几何（P1 SVG 实测）：

| 项目 | W43 JA×EN | W45 核心 | W45 本版 | 裁定 |
|---|---|---|---|---|
| wordmark 基线 y | 248 | 262 | 248 | = W43 ✓ |
| 副标题 y | 316 | 330 | 316 | = W43 ✓ |
| badge | (975,356) 19pt，`TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS` | 无 | 与 W43 逐字同，(975,356) 19pt | = W43 ✓ |
| strapline y | 390 | 372 | 390 | = W43 ✓ |
| 规则线 y | 406 / 413 | 392 / 401 | 406 / 413 | = W43 ✓ |
| band rect y | 424 | 424 | 424 | 三方同 ✓ |
| 刊头冠词 | 无（Lucerna） | 无 | 无 | ✓（日语无冠词） |

- 页脚式：本版 `Lucerna · JAPANESE WEEKLY VOL.2 · Japanese text · English explanations`
  + `Page n of 8`，与 W43 式一致（仅 VOL.1→VOL.2 为当期所迫）。
- Note — 前缀：本版 `Note — ` 出现 10 处，与 W43 同数；核心为中文前缀，已替换。
- P8 分隔符/标题：本版 `— Page N —`（N=1–8）、`テストと答え · Test and answers`、
  `答え · Answers — grouped by page; just find your number`、
  `A short English note with every answer · ✓ = the model-text item`，
  与 W43 逐项同；核心中文式已替换。
- 指令与类型名集合：本版含 W43 SVG 可见集合的全部项
  （Fill in、Build a sentence、True or false?、Match words to meanings、Translate、Writing），
  另多一项 `Match events to places and dates`——其对应练习（P3 43–46 配对组）
  在核心的指令为 `把活动和地点·时间配对`，英文化正确；W43 VOL.1 本期无此题型，
  故其 SVG 中无此串，属期数题型所迫，非家具偏差。
- 金句 p.N 标签：见 §6，式与 W43 同（p.N）。
- band 副标题式：本版 P2–P6 为 `レベル … · 〈日语主题〉 · 〈英语主题〉`，
  与 W43 同式；P7 为 `言語フォーカス · 三つのレベル、三つのテーマ · Three levels, three themes`，
  与 W43 P7 逐字同。
- 其余偏差仅为当期所迫：VOL.2、PDF 名 `Lucerna-VOL2-EN(.pdf/-web.pdf)`、
  题量/级别/范文长（见 §12）、读者园地披露句遵循 W45 统筹裁定（§10）而非 W43 短式。

## 12. 题量 / 范文 / ABSTRACT / 图片 / KIT

- 登记展开独立计数（SVG 芯片→题号配对 + 区间题组展开，非原始 chip 粗计数——
  P1「本期内容」栏的 level chip 不是练习题，已排除；区间：P2 25–28、P3 43–46、P8 141–144）：
  **150 题，A2 46 / B1 75 / B2 29；页分布 10/18/18/18/18/18/12/38；题号 1–150 连续无缺**，
  与核心一致。P1–P7 计 112（A2 37 / B1 53 / B2 22），P8 计 38（A2 9 / B1 22 / B2 7）。
- 范文：`私の11月の週末` 全文核心=本版逐字同（6 个换行段拼接），
  计 **167 字**（不含 `例：` 前缀），在 150–200 区间内；P8 #150 注释
  `Model text in section H on this page (167 characters)` 一致。
- ABSTRACT（单行正文 294 字节含末尾换行，无 ASCII 双引号）：
  `Lucerna Japanese Weekly VOL.2 for English-speaking readers: Culture Day on November 3,
  autumn leaves at Naruko Gorge and the Kobe illuminations, gentle yuru eating, Reading Week,
  and the Japan Series in Yokohama — learn Japanese by reading real news, A2 to B2,
  150 exercises with full answers.`
  含真实主题关键词（Culture Day、Naruko Gorge、Kobe illuminations、yuru、Reading Week、
  Japan Series）、学习者搜索短语（`learn Japanese by reading real news`）、刊名、
  目标语（Japanese）、A2–B2、150 题 ✓。
- 图片：4 张图片载荷逐页 = 核心（base64 sha256 前 12 位：P1 92f3f41c7cec、
  P3 76f4abb34efc、P4 ab8d113ff083、P5 f954d75303c8）；署名在版且核心=本版逐字同
  （P1 Poliphilo CC0、P3 歌川広重（三代）1876 PD、P4 Syced CC0、P5 Petr Kratochvil PD，
  均为 Wikimedia Commons）。
- PDF：印刷版 27,138,307 B、网页版 3,038,903 B（<10 MB），各 8 页。
- KIT 核验（文字错误本身若不涉及纸面，单列为非阻塞观察，见 O-2）：
  - §3：含 fix round 5 修正声明（此前“全部 150 条改写为英语”在 round 4 不成立，
    #37 于 round 5 方英文化，之后 0 条相同行）——与本轮实测一致。
  - §7：冻结数（P8 2721→1448 等）、occlusion 0/0/0、P6 覆盖 0.000、预告带 2524.12、
    P8 CLEAN 与 21 项 keydiff、卡片目视结论，均与本轮实测一致。
  - §8 Round 5 条目：变化文件（transform.py + content34.py）、变化交付物
    （P8 SVG/card + 双 PDF）、门禁重跑值，均与本轮独立验证一致。
  - §11：双 PDF 字节数与哈希与实测逐位一致（印刷版 27,138,307 B、
    sha256 abb86daf0ff11308bec4f104eb6ce7dae869847a7dacaab198339003ef39919f；
    网页版 3,038,903 B、sha256 5a4893e50047c5dbde3cce1da8c56149d1b227c24a646755609714b678036cd3）。

## 非阻塞观察（不影响放行判断，但应记录）

- O-1 — P7 行首 〜：宽口径下核心与本版各 1 项同源词条行（B2 `〜倍…` 行），新增 0，
  属继承项而非本版引入。KIT §7“kinsoku core 0 = edition 0”在标准禁则集下成立；
  若将 〜 列为禁则，核心本身亦为 1，结论不变。
- O-2 — KIT 文字：§3/§7/§8/§11 的关键数值与修正声明均经本轮实测证实，无纸面影响的
  KIT 文字问题未发现；KIT 文字错误本身按任务约定不阻塞纸面正确的版面（本轮亦无此情形）。
- O-3 — 计数口径说明：KIT/门禁日志的 freeze 串数为出现次数加总，与 json 去重串数不同
  （如 P2 +31/−28 vs +23/−20），但底层 json 与 fix5 json 逐页相同，非数据出入；
  P1「本期内容」栏的 level chip 不是练习题，SVG 计数须用 chip→题号配对法（已用该法闭合 150）。
- O-4 — 误报说明：简体扫描命中 P4「点」系核心共有的冻结日语字，已排除；
  gloss 词头表观差异系渲染换行碎片（见 §9）；P8 注释 CJK 均为被教词头/引文/语法助词，
  非中文讲解残留。
- O-5 — #139/#140 归类说明：见 §7。第一轮“#139/#140 题面改英语而键日语同”的并列表述
  易误读为两者均为 keydiff 项；本轮双重证据裁定 #139 非 keydiff、#140 为提取伪影，
  两者键均为日语原句逐字节同，无缺陷。

## 证据文件（本目录）

- `REPORT.md`（本文件）
- `proof2.py`（独立校对脚本，只读 files/ 树，写出 proof2.json）
- `proof2.json`（scope/kinsoku/freeze/gloss/P7/P8/家具/图片/几何等全部中间证据）
- `freeze-diff-proof2.json`（我重跑的 freeze diff，与 fix5 json 逐页相同）
- `p8-compare-proof2.json`（显式双路径 p8.py compare 输出：CLEAN 150=150）
- `p8-extract-core.json`、`p8-extract-ed.json`（p8.py extract 输出，keydiff 成因证据）
- `occlusion-proof2.json`（occlusion 输出：0/0/0）、`occlusion-core-proof2.json`（核心 0）
- `sha-before.txt`、`sha-after.txt`（diff 为空）、`sha-core.txt`、`sha-core-after.txt`（diff 为空）
- `scratch-baseline/`（冻结基线重定向复现产物，8/8）
- `card-previews/`（8 张卡片 780 宽预览 + P8 #37 全分辨率裁剪，目视用；原卡哈希见 sha-before.txt）

## 移交

本轮结论 ZERO PROBLEMS，无阻塞项。修复与上架均由主线串行执行，本校对不执行、不宣布。
