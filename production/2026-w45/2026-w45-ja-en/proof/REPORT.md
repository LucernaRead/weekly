# W45 JA × EN 独立校对报告（只校对，不改源码，不宣布上架）

- 校对对象：`files/weekly-report-w45-ja-en/`（svg×8、cards×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-ja-core/`（JA VOL.2，只读，未改动）
- 构建树（只读）：`hidden_files/weekly-report-w45-ja-en-build/`
- 校对方式：全部独立重测，不采信构建员自述。规范工具均用 `tools/venv/bin/python` 现场重跑；
  冻结基线用我自己的 scratch（`hidden_files/w45/ja-en-proof/scratch-baseline/`），未碰共享
  `tools/scratch/`，未清理共享 scratch 目录。
- 未做事项：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、
  未改核心/W43 目录、未派生任何下级代理、未宣布上架（上架由主线串行执行）。

## 结论：存在 1 项阻塞项，不写 ZERO PROBLEMS

### 阻塞项（1 项，必须修复后重跑 P8 门才能放行）

**B-1 — P8 第 37 题答案注释仍为中文，未本地化为英语。**

- 本版 P8 印刷行（与核心逐字节相同）：
  `37. 8 — 工艺展到11月8日`
- 核心同行：`37. 8 — 工艺展到11月8日`（核心是 JA×ZH，中文注释合理）。
- 同一事实的另一题已正确本地化，可作对照：第 32 题本版为
  `32. B — The exhibition runs to November 8 (Sunday)`，核心为
  `32. B — 工艺展到11月8日（周日）`。
- 因此这不是规则允许的保留，而是单题遗漏。它同时证伪构建员 KIT 的两处断言：
  “全部 150 条答案注释改写为英语”与“P8 notes all English”均不成立。
- 判定依据：150 条 P8 答案行逐行比对，本版与核心**唯一**完全相同的一条就是 #37
  （其余 149 条均已本地化或键为日语原文）；全版简体专属字扫描唯一真阳性也是 #37
  的「艺」（工艺）；全版汉字-only 交集串中唯一中文串也是 #37。
- 建议修复（仅建议，不由校对员执行）：将 #37 注释改为英语，例如
  `37. 8 — The exhibition runs to November 8`（与 #32 的 Sunday 后缀是否保留，
  由主线按题面事实裁定），随后重渲染 P8 SVG/card 与双 PDF，并重跑 freeze diff、
  p8.py compare、occlusion 三门。本项修复不影响其余 149 题的结论。

---

## 逐项独立重测结果

### 0. 开工查重与无变动证明

- 开工时 `ps` 无属于本版的渲染进程；交付物最新 mtime（KIT 01:16 UTC）至开工
  已超 60–120 秒静默区间，属已完成交付，不是 stand down 理由。校对全程未见新的写盘。
- 校对前后 sha256：`sha-before.txt` 与 `sha-after.txt` diff 为空
  （40 个文件：核心 20 + 本版 20，含 svg×8、cards×8、双 PDF、KIT、ABSTRACT）。
  冻结基线重跑亦确认核心 8 个 SVG 在跑前跑后均未变。

### 1. 冻结 / CJK / 违禁词 / 规范文件

- `freeze.py baseline`（自有 scratch 重定向）：**8/8 逐字节复现**，核心哈希与交付一致。
- `freeze.py diff --strict-cjk`：全 8 页新增 CJK 字符 **0**；每页 CJK 总量与构建员
  一致（P1 1406→1275、P2 1312→1161、P3 1172→1051、P4 1263→1169、P5 1247→1132、
  P6 1186→1101、P7 1676→1308、P8 2721→1454；减少量均为被移除的中文讲解层）。
  注：构建员 KIT 的“+31/−28”等是按出现次数加总，我的 distinct 串数（P2 +23/−20 等）
  与其最终 json 的 distinct 数逐页相同，底层数据同一，无出入。
- 违禁词「桥接」/「橋接」：SVG 全部 + KIT + ABSTRACT 均为 **0**。
- 规范 `svglib.py` md5：本版构建树与核心构建树均为
  `d73e23b365676c3618d7e060b835eb4d`，与声称值一致，未被编辑。
- 日语正文无丢失：全部 removed 串逐页审读——P1–P8 的 removed 串均为中文讲解、
  家具中文半句、P8 中文注释、读者园地中/日披露句及其换行碎片；
  以 。 结尾的核心串中缺失的也只限中文侧串（例：`这四个话题，都是本期报纸的主题。`、
  `写作题（无唯一答案）；范文（167 字）见下。`、P7 披露碎片）。无一条独立日语
  文章/题干/图表注句被删。P6 图表注句
  `このグラフは練習用データです。数字は全部で100%になります。` 核心=本版逐字同。

### 2. 日语专项：行首禁则与词级中文残留

- 行首禁则：用含 〜 的宽口径扫描，P1–P6、P8 核心=本版=0；P7 各 1 项，
  是同一条栏目词条行 `〜倍 times · 〜% percent · 〜万食 …`（核心为中文 gloss 版），
  属词条首字设计而非换行溢出，**新增 0**。以标准散文禁则集（不含 〜）计则全版 0/0。
  详见“非阻塞观察 O-1”。
- 词级中文残留：本版每页全部 CJK 词串均是同页核心文本的子串
  （`cjk_runs_not_in_core_page` 全页为空）；共享汉字词逐词核实：
  全国（冻结日语文章/题干串与核心逐字同；核心多出的 1 处是 P8 中文注释 #6，
  本版已正确英文化）、会社（`学校も会社も休み` 核心=本版）、来週
  （`来週 · Next issue (VOL.3)`，仅家具半句英文化）。简体专属字扫描全版唯一
  真阳性即阻塞项 B-1 的「艺」；`仮装` 一处为误报（合法日语词，核心亦有）。

### 3. 第 3 轮腐蚀修复专项（重点）

- P1/P4/P5/P6/P8 的 removed↔added 近似配对扫描（difflib >0.5）：
  全部配对均为合法本地化（日语键/词头保留、中文注释→英语注释；
  或家具日语半句保留、中文半句→英语半句），**无一对日语→日语小改动腐蚀对**
  （无缺 。、无改写、无断句）。
- 冻结句复原逐行验证：P1/P4/P5/P6/P8 全部冻结日语句在核心与本版的交集中逐字存在；
  句末 。 完整性检查仅中文侧串缺失（见 §1），日语句无缺字断句。
  Weekday 后缀：P8 答案注释中无日语 weekday 后缀残留（仅 #133 的键本身含
  `火よう日`，注释为英语 `subject + time + place + verb`）；P8 注释中的 weekday
  均已为英语 `(Saturday)`/`(Tuesday)` 形式。
- 专名注释：P8 专名注释均为英语（如 `The Kobe illuminations…`、`Suginami`、
  `Kanazawa Castle`），无残留中文专名注释（#37 除外，见 B-1）。
- 终轮 P1 趋势盒两行独立实测（PIL/NotoSansCJK，与 svglib 同字体）：
  `Dates in articles; not exact statistics` = **312.4 px**，
  `These four topics shape this issue.` = **293.2 px**，均 < 390 px 槽内宽，
  与构建员声称值逐位一致；P1 卡片目视两行均在槽内。

### 4. P7

- 定义句：A2/B1/B2 三栏定义段落核心=本版逐字同（拼接比对 identical）；
  框架句 `『ゆるく整える』 — ゆるく（無理をしないで）＋整える（体と心をよくする）。…`
  核心=本版；诊所日语例句（如 `金沢に紅葉を見ます → 金沢で紅葉を見ます`）保留，
  仅讲解英文化。**定义句本地化 0 处**。
- 金句：8 句原文核心=本版逐字同；去空白全册拼接计数每句在核心与本版均为 **恰 2 次**
  （文章内 1 次 + P7 列表 1 次）。
- 页标签映射（以核心实测为准）：核心 第1面×2、第2面×2、第3面、第4面、第5面、第6面
  → 本版 p.1, p.1, p.2, p.2, p.3, p.4, p.5, p.6，与构建员声称一致。
- P7 词框 gloss 仅本地化：三栏词条 A2 3 + B1 3 + B2 3 = 9，词头逐字同
  （読書週間/紹介/読み聞かせ；見頃/紅葉狩り/落葉；〜倍/〜%/〜万食，
  末项 gloss 续行 `ten-thousand servings.` 完整）。

### 5. P8（显式双路径 p8.py compare）

- `p8.py compare --core-p8 … --edition-p8 … --total 150`：**CLEAN，150 = 150，
  missing [] extra []**。口径系从核心 P8 渲染内容独立确立：核心 P8 本身即印 150 条
  注释（非 EN 核心的 78 口径），本版亦印 150 条；EXTRA_ONLY 不适用，
  两口径均未照搬。
- keydiff 21 项（与构建员名单逐项一致）印刷行对照裁定：
  - 17 项仅注释英文化，键逐字节同：#1(3)、#2(9)、#7(B)、#8(C)、#9(B)、#29(A)、
    #32(B)、#65(A)、#69(C)、#78(○)、#113(A)、#115(A)、#117(B)、#118(A)、
    #140(日语句，见下)、#146(A)、#147(A)。
  - #5/#101 括号分支伪影：印刷键分别为 **7** 与 **27**，两边逐字节同，
    仅注释由中文改为英语（含括号内英文 weekday），p8.py 的 keydiff 属提取伪影，
    非键差异。
  - #137/#138 合法 JA↔EN 重定向：键由中文句改为英语句
    （`Culture Day is November 3.` / `If you drop litter, the fine is 2,000 yen.`），
    属 E 区重定向规则内。
  - #139/#140 题面改英语而键日语逐字节同：#139 键
    `読書週間は10月27日から始まります。` 同；#140 键
    `神戸の紅葉のライトアップを見に行きたいです。` 同（其题面英语句
    `I want to go to Kobe to see the autumn-leaf illuminations.` 在 P8 练习区，
    答案区键仍为日语原句）。
  - 另：#140 在 p8.py keydiff 内是因注释括号续行提取所致，印刷键本身同上。
- P8 注释语言：除 B-1 的 #37 外，其余注释的讲解语言均为英语；
  词汇/配对键中的日语词头（如 `見頃 = best viewing season`）是被教的词本身，
  非讲解语言，不计为中文残留。
- 印刷笔记集合按题号相等：150 题号齐全，无缺无增（EXTRA_ONLY 可接受但未发生）。

### 6. 几何

- `occlusion_audit.py`（自检先行，6 类全触发）：本版 **0 flags**、核心 **0 flags**、
  NEW vs core **0**。与构建员终轮一致（其日志中的 3 flags 为第 3 轮旧态，已修复）。
- 同基线墨迹碰撞扫描：家具带同基线碰撞 0（已含于上述 0 flags）。
- P6 图表标签基线锚定墨迹法（PIL getbbox，anchor ls，条形为后绘 rect）：
  全部文本×后绘 rect 最大覆盖 **0.000**，图表区亦 0.000，<30% 门通过
  （getbbox 法为错误口径，未采用）。
- 全页右缘 ADVANCE 扫描（advance width，限 x=1885.5）：本版 0、核心 0。
- P7 预告带止点独立实测：SVG 底带 rect y=2406.12 + 高 118 = **2524.12**，
  <2540 内容限，距 2580 页脚线 55.88 px（≈56 px），与声称一致；
  P7 非页脚最大文本 y=2490.12，亦在限内。
- 8 张卡片全部目视（1950×2700 原卡的 780 宽预览逐张查看，非抽查）：
  P1–P8 均无溢出、重叠、截断标签、错位框；P1 趋势盒、P6 图表、P7 预告带、
  P8 密集答案区均正常。

### 7. gloss

- 渲染后 gloss() 串按 · 拆分，核心=本版逐项 1:1，总 **39 = 39**：
  P1 4、P2 9（4+5）、P3 8（4+4）、P4 7（4+3）、P5 7（4+3）、P6 4。
  词头序列经源码 gloss() 串与渲染行双重比对全部逐字同（渲染换行造成的
  `楽 しむ`/`確認す る` 等空格为换行碎片假象，源码词头为 `楽しむ`/`確認する`）。
- P7 桥接式词条 9 项（见 §4），日语词头逐字同，gloss 均已英文化。

### 8. 读者园地

- 日语示例信逐字不动：核心与本版示例信全文同
  （`「こんにちは。私は中学生です。読書週間には、図書館で本を2冊読みたいです。
  文化の日には、家族と金沢へ行きたいです。」— 読者の手紙の例`），零编造
  （无新增读者、姓名、引文）。
- 英语披露句逐字摘录（本版 P7）：
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
  在本版 P7 均已移除，仅英语披露为 operative；无双 operative 披露混淆。
- 最佳 P8 作文覆盖范围裁定：披露句的 `both` = 真实来信 + 最佳 P8 作文（泛指类别，
  非单篇）；VOL.3 预告行 `読者の手紙と第8版の作文の優秀作も載せます` 与之呼应，
  覆盖“选登的最佳 P8 作文”，非全部作文。
- 内容预告行（`来週 · Next issue (VOL.3)` 段）为内容预告，不计入邀请——邀请
  仅以披露句内的祈使句为准，已单独成立。

### 9. 家具 / W43 三方测量

三方：W43 同配对版（`files/weekly-report-ja-en/`，VOL.1 已发）、W45 核心、W45 本版。
W43 同配对家具胜过 README #20 泛化规则；下表刊头几何（P1 SVG 实测）：

| 项目 | W43 JA×EN | W45 核心 | W45 本版 | 裁定 |
|---|---|---|---|---|
| wordmark 基线 y | 248 | 262 | 248 | = W43 ✓ |
| 副标题 y | 316 | 330 | 316 | = W43 ✓ |
| badge | (975,356) 19pt，`TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS` | 无 | 与 W43 逐字同，(975,356) 19pt | = W43 ✓ |
| strapline y | 390 | 372 | 390 | = W43 ✓ |
| 规则线 y | 406 / 413 | 392 / 401 | 406 / 413 | = W43 ✓ |
| band y | 424 | 424 | 424 | 三方同 ✓ |
| 刊头冠词 | 无（Lucerna） | 无 | 无 | ✓（日语无冠词） |

- 页脚式：本版 `Lucerna · JAPANESE WEEKLY VOL.2 · Japanese text · English explanations`
  + `Page n of 8`，与 W43 式一致（仅 VOL.1→VOL.2 为当期所迫）。
- Note — 前缀：本版 `Note — `，与 W43 同；核心为中文前缀，已替换。
- P8 分隔符/标题：本版 `— Page N —`、`テストと答え · Test and answers`、
  `答え · Answers — grouped by page; just find your number`、
  `A short English note with every answer · ✓ = the model-text item`（位置 x=1885,y=1302
  与 W43 逐字同位），均 = W43；核心中文式已替换。
- 指令与类型名集合：本版含 W43 集合中本期出现的全部项
  （Fill in、Build a sentence、True or false?、Match words to meanings、Translate、Writing，
  及诊所句 `With 「昨日」, use the past tense.`）；W43 的 `Match events to places` 等
  本期无对应题型，不计为缺失。
- 金句 p.N 标签：见 §4，式与 W43 同（p.N）。
- band 副标题式：本版 P2–P6 为 `レベル … · 〈日语主题〉 · 〈英语主题〉`，
  与 W43（例：`レベル A2 · 紅葉と秋の味覚 · Foliage and autumn flavors`）同式；
  P7 为 `言語フォーカス · 三つのレベル、三つのテーマ · Three levels, three themes`，
  亦同式。
- 其余偏差仅为当期所迫：VOL.2、PDF 名 `Lucerna-VOL2-EN(.pdf/-web.pdf)`、
  题量/级别/范文长（见 §10）、读者园地披露句遵循 W45 统筹裁定（§8）而非 W43 短式。
  任务所列 JA 目标族几何参照值（wordmark 262 等）不否定上述 W43 实测：
  本版刊头取 W43 同配对版为准，符合 brief。

### 10. 题量 / 范文 / ABSTRACT / 图片

- 登记展开独立计数（SVG 题号标签 + 题号前 level chip 配对 + 区间题组展开，
  非原始 chip 粗计数——P1「本期内容」栏的 level chip 不是练习题）：
  **150 题，A2 46 / B1 75 / B2 29；页分布 10/18/18/18/18/18/12/38；题号 1–150 连续无缺**，
  与核心一致。P1–P7 计 112（A2 37 / B1 53 / B2 22），P8 计 38（A2 9 / B1 22 / B2 7）。
- 范文：`私の11月の週末` 全文核心=本版逐字同，计 **167 字**（不含 `例：` 前缀），
  在 150–200 区间内；P8 #150 注释 `Model text in section H on this page (167 characters)` 一致。
- ABSTRACT（单行 294 字符，无 ASCII 双引号）：
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
- PDF：印刷版 27,138,695 B、网页版 3,038,546 B（<10 MB），各 8 页，与 KIT 记录一致。

---

## 非阻塞观察（不影响放行判断，但应记录）

- O-1 — P7 行首 〜：见 §2。核心与本版各 1 项同源词条行，新增 0，不构成缺陷；
  若门集将 〜 列为禁则，核心本身亦为 1，属继承项而非本版引入。
- O-2 — 计数口径说明：KIT 的 freeze 串数为出现次数加总，与 distinct 串数不同，
  但底层 json 与我重跑的 json 逐页相同，非数据出入。
- O-3 — 误报说明：简体扫描命中 `仮装` 系日语词（核心亦有），已排除；P1「本期内容」
  栏的 level chip 不是练习题，SVG 计数须用 chip→题号配对法（已用该法闭合 150）。
- O-4 — W43 P7 预告行文与 VOL.2 预告不同，属期数内容差异，非家具偏差。

## 证据文件（本目录）

- `REPORT.md`（本文件）
- `proof.py`（独立校对脚本，只读 files/ 树，写出 proof.json）
- `proof.json`（freeze/kinsoku/gloss/P7/P8/家具/图片等全部中间证据）
- `freeze-diff-proof.json`（我重跑的 freeze diff，与构建员 freeze-diff-final.json 逐页一致）
- `p8-compare-proof.json`（显式双路径 p8.py compare 输出：CLEAN 150=150）
- `occlusion-proof.json`（occlusion 输出：0/0/0）
- `sha-before.txt`、`sha-after.txt`（diff 为空）
- `scratch-baseline/`（冻结基线重定向复现产物，8/8）
- `card-previews/`（8 张卡片 780 宽预览，目视用；原卡哈希见 sha-before.txt）

## 移交建议

仅阻塞项 B-1 待修复：改 #37 注释为英语后重渲染 P8 与双 PDF，重跑 freeze diff、
p8.py compare、occlusion 三门（其余结论不受影响）。修复与上架均由主线串行执行，
本校对不执行、不宣布。
