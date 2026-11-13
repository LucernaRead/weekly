# 独立校对笔记 — 2026-W47 德文核心版 · 第二轮（返修后复校）

校对员：第二轮独立校对（与 builder、第一轮校对不同人）。只读不改；未改 core-de 内任何文件，未改 tools，未跑 insert.py / lint --write / git push/add/reset/stash / commit；未碰 W43/W45/W46 的任何文件（仅只读实测 W46 法文验收版 PDF 作 §1.1 对照标尺）。
校对时间：2026-11-10 晚。对象：`~/workspace/weekly-git/production/2026-w47/core-de/`，印刷 PDF `Die-Lucerna-VOL4-de.pdf`（22,963,572 字节，SHA-256 `ea41866fd6669f3cf3380c8c53d66ef3a0da4b30a6ccddee9b786711b112801b`，与任务书一致），网页 PDF `Die-Lucerna-VOL4-de-web.pdf`（2,043,235 字节，SHA-256 `7394de6113d9a045cdd871b1c01e5d9942f4bcebbcc9bd81fef0f87ba749f522`，与任务书一致），正文 `2026-w47-de-zh-cn.text.md`（SHA-256 `e7ba369b1ea94b747c062d9ecbaf802d937c694ec8ce80efeff838c190b26bae`，与任务书一致），8 页，1462.5×2025pt。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de2/`（本笔记 + `work/` 下日志、渲染图、测量脚本）。

## 结论：(b) 缺陷清单 — 共 1 项（轻，§8.1 词汇框锚定）

**D1–D5 逐项验证全部通过**（见下节；D4 builder 偏离返修 brief 是正确的，独立查源证实其版本属实）。全量复校另发现 1 项轻缺陷 D6（与 D2/D3 同类 §8.1 问题，第一轮称“词表框 12 词亦全部在正文”——复核为不属实）。**不是定稿**，待 D6 裁定/修复后需再走一轮全量校对（SOP §8.4）。

---

## 缺陷清单

### D6（§8.1）— 词汇框 3 个词未出现在当版文章里（其中 2 个所在的练习还自称“用方框里的词”即“WÖRTER AUS DEM TEXT”）
- 位置：
  - P3 `WEIHNACHTSWÖRTER　圣诞词汇` 框：`der Adventskalender — 降临节日历`；
  - P5 `ADVENTSWÖRTER　降临节词汇` 框：`die Kerze — 蜡烛`、`der Stern — 星星`；同版练习 B 的方框词表（`Türchen · Wunschzettel · Christkind · Schokolade · Kerze · Stern`）亦含此二词，练习标题为 `B　WÖRTER AUS DEM TEXT　用方框里的词填空`。
- 证据（独立重数，计数范围 = 当版文章段落，即译注行之前的正文；屈折形计入，与 D2/D3 同口径）：
  - P3 文章含 `Weihnachtsmarkt` 4×、`Glühwein` 2×、`Lebkuchen` 1×、`Weihnachtsbaum` 1×、`Kerze` 1×（作复数 `Kerzen`），**`Adventskalender` 0×**（文章只出现单独的 `Advent`；`Adventskalender` 全 P3 仅见于词汇框本身与 Q41 选项 C）。
  - P5 文章含 `Türchen` 4×、`Wunschzettel` 4×、`Christkind` 2×、`Schokolade` 1×，**`Kerze` 0×、`Stern` 0×**（两词全 P5 仅见于词汇框本身与练习 B 方框）。
  - 其余 9 个框词全部在文章里（见“通过项·§8.1 全量”）。
- SOP 依据：§8.1「注释的词必须真实出现在正文里」。词汇框带中文释义，属讲解层；P5 练习 B 更以标题明示“WÖRTER AUS DEM TEXT”，而 Kerze/Stern 不在文中。
- 正确应为：从框中去掉这 3 个词（或在文章里自然植入：P3 文章提一次 Adventskalender、P5 文章提一次 Kerze/Stern；改哪处由协调员定）。
- 严重程度：**轻**（单处词汇锚定缺口；词本身拼写、释义、答案键 Q74 Kerze / Q75 Stern 均正确，无事实错误）。
- 注：第一轮笔记“词表框 12 词亦全部在正文”与本次复核不符——第一轮若按整版（含练习）计数则成立，按文章段计数则 3 词不成立。本轮按 D2/D3 修复时确立的“正文段内”口径执行。

---

## 返修逐项验证（D1–D5，全部独立实测，不采信 builder 说法）

### D1（题干字号）— 通过
- 方法（自写脚本 `work/measure_stems2.py`，AST 提取全部 124 个 `ex()` 体，与 SVG 全部 `<text>` 元素做最长公共前缀匹配，取最佳匹配行的字号；另跑第一版脚本交叉核对）：124 个 `ex()` 体全部命中。
- 结果：**P1–P7 全部题干 22.0 单位 = 16.5pt**（P1 10/10、P2 14/14、P3 18/18、P4 14/14、P5 18/18、P6 18/18、P7 12/12）；**P8 全部 20 题 20.5 单位 = 15.375pt**（20/20）。低于下限（P1–P7 <22 / P8 <20.5）：**0**。
- 源码交叉核对：`bslib4.py` 含 `STEM_MIN = 22`、`STEM_MIN_P8 = 20.5` 及 `ex()` 内 `size = max(size, ...)` 钳制；124 个显式 `size=` 为 104×22 + 20×20.5（与 SVG 实测一致）。
- 排查过的疑似命中（均证实为误匹配，非真题干）：Q33 首行曾误 match 到 21.5 单位的侧栏盒文字，题干本行实为 22（`x=88.0 y=2323.4`）；Q38/Q81/Q98 首行曾误 match 到 24 单位的文章句，题干本行实为 22（直接 grep 确认）；Q66/Q121/Q126 因换行切分致第一版脚本漏配，第二版最长前缀匹配确认 22/20.5。
- 栏高与溢出：冻结复现日志零 `FLOW OVERFLOW` / `HEAD TOO WIDE`；各流终点与 builder 所称一致（最紧 P6-ex 2523/2560，余 37px；P1-quiz 2523/2560；P8-keys 2504/2560；P7 图 ends 1541.8 vs Sätze 横线 1548，余 6.2px）；occlusion 0 flags；8 版渲染图目视无溢出/重叠/压页脚（见“8 版逐版看图”）。
- 注：P8 15.375pt 比 SOP §1.1 让步值 15.4pt 低 0.025pt——20.5 单位换算的舍入量级（20.5×0.75=15.375），不计缺陷。
- 观察项 O1（不计缺陷，见文末）：P8 完形填空段落与对话段落 19.5 单位 = 14.625pt、其选项行 18.5 单位 = 13.875pt，低于 P8 让步值。属返修前已有的结构（W46-DE `content8.py` 第 40 行即为 18.5，与本次返修无关）；验收版 W46-FR 的 P8 同类位置亦低于阶梯（完形段落 15.75pt、选项行 14.62pt，实测见 O1 节）。D1 任务书定义的核查范围是 ex() 题干，本项留协调员裁定。

### D2（§8.1，P4 `die Ligaphase`）— 通过
- 第二处查清：`Ligaphase` 在 `p4-sport.svg` 内确为 **2×**：文章行 `<text x=88.0 y=577.14 …>Ligaphase. Der FC Bayern gewann in…`（文章句“ihren 4. Spieltag der / Ligaphase.”换行，Ligaphase 为行首）+ 译注行 `<text x=1007.0 y=557.585 …>… die Ligaphase`。协调员 grep 得 1 次是行计数假象（SVG 单行文件，`grep -c` 只计行不计次；`grep -o` 得 2 次）。`.text.md` 亦 2 次。builder 所称 2× 属实。
- P4 全部注释词逐词计数（范围 = P4 文章段，屈折/可分动词拆分形计入）：`das Tor` 2、`der Spieltag` 3、`torreich` 1（`torreichste`）、`die Ligaphase` 1、`weiterkommen` 1（`kommen weiter`）。**5/5 在正文**。D2 修好。

### D3（§8.1，P6 `die Buße`）— 通过
- `Buße` 在 `p6-vertiefung.svg` 内 **3×**：文章行 `Buße und zum Nachdenken ein: Was…`（`Er lädt zur Buße und zum Nachdenken ein:`）+ 译注行 + 练习 D 词框。P6 Q97 填空 `Der Buß- und Bettag lädt zur ___ ein` 与文章逐字对齐。
- P6 全部注释词逐词计数（文章段）：`die Buße` 1、`das Kirchenjahr` 2、`der Verstorbene` 1（`Verstorbenen`）、`der Friedhof` 1、`der Haushalt` 2（builder 称 1，实为 2：`Bundeshaushalt` + `jeden Haushalt`；词在正文，计数差不影响结论）、`die Einigung` 1。**6/6 在正文**。D3 修好。

### D4（塞尔维亚场，builder 偏离返修 brief）— 通过（偏离正确）
- 独立查源（2026-11-10 当日多家一致报道，均在任务书之外独立检索）：
  - `fussballnationalmannschaft.net`（2026-11-10）：“Doch kein Geisterspiel in Belgrad: Kinder unter 15 Jahren in Begleitung von Lehrern oder Trainern dürfen … dazu 50 ausgewählte deutsche Fans”；“Wir rechnen zurzeit mit etwa 5.000 Besuchern”；“Anpfiff ist am 13. November um 20.45 Uhr”；UEFA Zuschauerausschluss + 50,000 欧罚款。
  - `kicker.ch`（2026-11-10）：“Kinder und 50 ausgesuchte deutsche Fans in Belgrad erlaubt”；“Der Verband rechnet mit rund 5000 Zuschauern im Stadion Rajko Mitic”；周五晚 20.45 Uhr。
  - `bundesliga.com`（2026-11-10，官方文）：“weitestgehend leer … Lediglich Kindern und ihren Begleitern sowie 50 Fans des DFB wird der Zutritt gewährt, in etwa 5.000 Zuschauer werden erwartet.”
  - `feverpitch.de` / `gmx.ch`（2026-11-10）同上：50 名德国球迷、约 5,000 人、€50,000 罚款（feverpitch 写儿童“unter 14 Jahren”，版本取“仅儿童”未写年龄，无冲突）。
- 裁断：**builder 的版本属实，第一轮“全场空场、零观众”不属实**（零观众是 10 月 22 日 DFB 确认的旧口径，11 月 10 日 UEFA 规则例外已更新）。约 5,000 人例外入场、55,000 座球场“基本空着”——“vor fast leeren Rängen”准确。
- 日期/时间/球场：**2026-11-13 周五 20:45**（`date -d` Europe/Berlin：13 日 = Friday ✓），贝尔格莱德 Rajko-Mitić 球场 ✓，欧国联 ✓。11 月 16 日周一 20:45 对荷兰（柏林）亦与 P4 赛程表一致（16 日 = Monday ✓）。
- P1 新导语逐字核对：`Doch zuerst die Nationalmannschaft — schon am Freitag, dem 13. November: Deutschland traf in Belgrad auf Serbien, vor fast leeren Rängen (UEFA-Strafe: nur Kinder und 50 deutsche Fans durften ins Stadion). Am Montag (20.45 Uhr) folgt das Endspiel gegen die Niederlande in Berlin.`——过去时 + 日期 + 处罚括号齐全，旧句 `trifft Deutschland in Belgrad` / `Am Freitag (20.45 Uhr)` 已无；P1 金句 #2 `Es geht ums Viertelfinale der Nations League.` **逐字保留**（verify.py 金句 8 条各恰 2×，#2 在列）。
- P4 赛程表、P5 周计划：全文检索 `Serbien` 全期仅 3 处——P1 导语（已注日期、过去时）、P1 快讯 `Serbien auswärts`（无日期/时态主张）、Q7 干扰项 `A. Serbien`；**P4、P5 均无塞尔维亚场** ✓。
- P7 工具箱同步句 `vor fast leeren Rängen = 几乎空场（欧足联处罚，仅儿童与 50 名德国球迷入场）` 在位 ✓。D4 修好，偏离 brief 是正确的。

### D5（P3 Q42）— 通过
- 新题干在位：`Wie viel früher als der erste Advent beginnen die Märkte?`（P3 渲染图 + `.text.md` + SVG 一致），旧题干 `Warum beginnen die Märkte vor dem ersten Advent?` 全期已无。
- 仅一解验算：A `Sie öffnen fast zwei Wochen früher.` 是唯一时间跨度表述，且与文章 `Die Märkte beginnen fast zwei Wochen früher.` 一致（市场 11 月 16 日开，将临期 11 月 29 日，相差 13 天 ≈ 快两周）；B `Der Advent ist schon vorbei.` 为假（将临期在未来）且非时间跨度；C `Die Märkte sind neu.` 非时间跨度。**仅 A 可解** ✓。
- 选项、键、注记不变：P8 答案键 `42. A（市场比将临期早近两周开市）` 与题干一致 ✓（p8.py compare keydiff=[] 亦佐证键无漂移）。

---

## 全量复校（每项都跑过）

### 全文精读
- `.text.md` 42,176 字符逐行读完（P1–P8）。德语拼写、变格、变位、性数配合、标点未见错误；未见重复词、截断句；中文讲解层与德文对照无误。
- 抽查要点：P2 `Elf Tage vor dem ersten Advent`（18+11=29 ✓）；P3 `Vor fast 100 Jahren`（1930→2026 为 96 年 ✓）、市场开放 11 月 16 日–12 月 23 日且 22 日关闭与 Q40 键一致；P4 `4. Spieltag der Ligaphase`（3–4 日周二/周三 ✓）；P5 1903 年日历“über 120 Jahre alt”（123 年 ✓）；P6 预算 11 月 27 日周五表决（16 日周一→27 日周五 ✓）、2,05 欧分与 Q91/Q127 一致；P7 纠错诊所 4 条全部正确（动词第二位、`halb neun = 8.30 Uhr`、Partizip II 句末、ob 从句动词句末）；P7 下期预告与 VOL.5 承诺（29 日将临期、24–26 日欧战、读者来信）与 §9 一致。

### 150 题逐题复核（答案键逐题独立验算，尤其 P8 113–150）
- 登记表：TOTAL **150**，按版 10/18/18/18/18/18/12/38，编号连续 1–150；级别 A2 69 / B1 67 / B2 14；题型与 KIT 一致（单选 52 / 完成句子 41 / 句型转换 11 / 判断对错 8 / 完形 8 / 造句 8 / 词汇配对 12 / 翻译 4 / 对话补全 5 / 写作 1）。除 Q42 题干外其余题目文本与第一轮已校的 build9 一致（本次仍逐题重算，未采信第一轮结论）。
- P1（1–10）：全部与头版文章一致（Bundesliga / Niederlande / Sachsen / Totensonntag / fünf / 29. November / B / A / B / B）。
- P2（11–28）：日期题 11–15 全对（18 日周三——16 日周一故 18 日为周三 ✓）；Perfekt 16–20 全对（`ist … abgeschafft worden` / `sind … geblieben` / `sind … gegangen` / `hat … behalten` / `sind … geblieben`）；21–24 B/B/A/B；配对 25–28 键 d/c/a/b 与释义逐一相符。
- P3（29–46）：判断 29–33（R/F/R/F/R）与文章一致；填空 34–38 全对；39–41 B/B/A；**42 A（仅一解，见 D5）**；造句 43–46 动词第二位全对。
- P4（47–64）：比分题 47–50 全对；第 9 轮总进球重算：4+3+7+3+4+1+3+2+3 = **30** ✓；51 B（荷兰 8、德国 5，顺序与题面一致）；配对 52–55 d/b/c/a 全对；比较级 56–59（mehr / später / früher / mehr）均与数据相符（莱比锡 5 球 > 多特 2 球；20:30 晚于 15:30；11 月 3 日早于 8 日；8 分 > 5 分）；时间题 60–63（20.45 / 20.30 / 18.30 / 17.30）与赛程表一致；64 B（3:1）✓。
- P5（65–82）：65–69 A/B/B/B/A；70–75（Türchen / Wunschzettel / Christkind / Schokolade / Kerze / Stern）与方框一致；weil 句 76–79 动词置尾全对；80–82 R/F/R ✓。
- P6（83–100）：图表题 83–88 全对（44+33=77、总和 100、23% 最小）；89–92 B/A/B/B；语法 93–96（wird / ob / geht / beginnt）；97–100（Buße / Kirchenjahr / Friedhof / Einigung）与文章一致，98 `des ___s` = Kirchenjahr + s（属格）✓。
- P7（101–112）：101–104（wird / werden / wird / A 被动）；105–108（stiller / weil / weil 句 / A）；109–112（ob / fraglich / `dass … braucht` 动词句末 / B）✓。
- P8（113–150，逐题重算）：完形 113–120（A/B/A/B/A/A/B/A）——主语均为 Lena/Der Advent（第三人称单数），干扰项复数/过去时均排除，**每题仅一解**；121–128（A/B/B/B/B/A/B/B）；阅读 129–132（A/B/B/B）与 Berger 一家短文逐句相符；造句 133–136 动词第二位全对；翻译 137–140（`Am Montag schaue ich zu Hause Deutschland gegen die Niederlande.` 第一人称 schaue ✓）；配对 141–144（c/a/d/b）释义逐一相符；对话 145–149（A/B/A/A/A：öffne / machst / schaue / schaue / lese，人称与对话一致）；150 开放题无固定键 ✓。
- 金句：8 条各恰 2×、逐字出自本期正文（verify.py `verbatim OK: True`；P1 #2 含新导语在内）；出处页码/级别与正文一致。
- 目录与跨版引用：P1 目录 S.2–S.8 与各版栏目/级别一致；`详见第 4 版`、`答案见第 8 版`等引用页码无误；页码行 8 版齐全 `第{n}版／共8版`。
- MUSTER 84 词（空白切分，verify.py），在 80–100 词范围内 ✓。
- 禁用词扫描：`Geisterspiel / Karneval / Volkstrauertag / NFL / American Football / Tankrabatt / Hart aber fair / Klassiker / Allerheiligen / VOL.3 / Le Lucerna / The Lucerna / 11.11` 全期 0 次（verify.py）。
- §8.1 全量：P1–P6 六条译注共 32 词逐词重数，**全部在当版文章段内**（P1 4/4、P2 5/5、P3 6/6、P4 5/5、P5 6/6、P6 6/6；屈折/拆分形计入）。词表框 12 词：9 词在文章，3 词不在——即 D6。

### 机械门（独立重跑，日志在 work/）
- `tools/occlusion_audit.py` 全 svg 目录：**0 flags**，自检通过（6 类植入全触发、干净对照静默）。
- `tools/p8.py extract --p8 svg/p8-uebungen.svg --total 150`：**150/150**；`compare` 核心对自身：`status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]`。
- freeze 复现：整 `core-de` 复制到 scratch 副本跑 `run.py`（不在原目录写文件），8 个 SVG 与交付 SVG **逐字节 sha256 一致 8/8**（`tools/freeze.py` 自报 0/8 是已知收集器假象，以直接 sha256 为准；复现日志 `work/freeze.log`，零 FLOW OVERFLOW / HEAD TOO WIDE）。
- 文字层：`pdftotext` 默认模式 print/web 各 **50,180 字节**，归一化后同为 41,779 字符，**字符多重集相同**，仅 P6 图表区 token 顺序不同（`读者最关心什么？` 与 `44 %` 的分组位置互换——poppler 布局分组差异）；`-raw` 模式各 49,094 字节，归一化后**完全相同**。web PDF 带真实文字层，2,043,235 字节 < 7MB。
- P8 最小字号实测 ≥9.75pt：PyMuPDF 实测 P8 最小 span **10.12pt**（95 处答案键）；其余各版最小 11.62–12.75pt。
- verify.py（独立重跑，`work/verify.log`）：exit 0；TOTAL 150；SVG 重跑后字节相同；§1.1 风格审计 True，旧式 hex []；P6 图柱 748/561/391；图表 44+33+23=100；日期加法 18+11/15+7/16+6 全对。

### §1.1 逐项实测
- 纸色：渲染像素 (251,250,246) = **#fbfaf6** ✓；无金色/近黑底/双线外框（verify.py 风格审计 True，旧式 hex []）；纸面 rect 全页 #fbfaf6。
- 字体：PDF 内嵌 Newsreader（拉丁正文）、UnifrakturMaguntia（刊头 147pt）、Noto Sans/Serif CJK SC（中文讲解层），`pdffonts` 核实全部 embedded ✓。
- 徽章三色：A2 #5c6e30 / B1 #46581f / B2 #37402f（verify.py 风格审计 True；bslib4.LV_COLOR 与第一轮实测一致）。
- 家具全角空格：页脚 `Die Lucerna　德语周报 VOL.4　LUCERNA GERMAN WEEKLY`、页码行 `第{n}版／共8版`、刊别 `德语周报　VOL.4　德甲回归　安静的一周` 均用全角空格 ✓（8 版渲染图目视确认）。
- 头条标题 40 字符 ≤56 ✓；头条 39.75pt、band 副标题 #cac8ba、无首字下沉——与 W46 法文验收版逐项一致，第一轮已裁定可接受，本轮不重列（SOP 文本与验收实践共有的缺口）。
- 中文数字带空格：按任务书全周统一口径（接受的 W46 做法，W47 不修），**不列缺陷**。

### 8 版逐版看图（自印刷版 PDF 每页 110dpi 渲染，`work/pg-1.png` … `pg-8.png`，逐版目视）
- P1：新导语完整无溢出；头条、数字栏、即学即练、快讯、闪电问答齐全；页脚/页码行齐全。无问题。
- P2：练习区完整，配对块落位，Rechnen 横线间隔清晰；Q18 箭头换行属正常折行。无问题。
- P3：Q42 新题干在位、选项齐全；画作图注与出处齐全。无问题。
- P4：`Spieltag der Ligaphase` 在位；赛程表仅 Mo 16.11. 荷兰场，无塞尔维亚场；Und-Sie 框中德文齐全。无问题。
- P5：周计划 Mo 16.11.–Fr 20.11.，无塞尔维亚场；1903 日历图注与出处齐全。无问题。
- P6：图表 44/33/23 完整、ÜBUNGSDATEN 标注在位；Q100 落在页脚上方留空处（最紧页，余 37px，视觉清晰）。无问题。
- P7：工具箱新译注完整；图注与 Sätze 横线间隔清晰；金句 8 条、诊所 4 条、读者来信编辑示例标识清晰。无问题。
- P8：完形/问答/阅读/造句/翻译/配对/对话完整；1905 图 + 图注与写作横线间隔清晰；MUSTER 清晰；答案键四栏完整，均在页脚上方结束。无问题。

### 事实抽查（独立查源；日期星期用 `date -d` Europe/Berlin 核对）
- D4（见上）：塞尔维亚场日期/时间/球场/观众例外——4 家 2026-11-10 来源一致证实 builder 版本 ✓。
- 10 月 20–22 日德甲第 10 轮开球时间：Schalke–Stuttgart 周六 18:30 CET（bundesliga.com 17:30Z；fussballdaten.de 直接列 CET 18:30）、Bremen–Hamburg 周日 17:30 CET（16:30Z）——KIT 纠正正确，Q62/Q63 键正确 ✓。
- 其余事实（德甲第 9 轮 30 球与 9 场比分、欧战 11 月 3–8 日赛果、欧国联积分与 11 月 16 日荷兰场、欧战 24–26 日、Buß- und Bettag 与 Totensonntag 规则、科隆圣诞市场日期、Ritter 1930 年画作、Kepler 1903 年日历、预算 11 月 27 日表决）第一轮已逐项核实来源，build10 未改动其中任何事实（token 差分仅涉 D1–D5 五处），本轮抽查 P4 赛程表与 P5 周计划与之一致，未发现出入。

### 图片许可与署名（逐张核对 assets/CREDITS.md，第一轮结论复核无改动）
- P1 fussball.jpg（DVIDS 333458，PD）、P4 kopfball.jpg（DVIDS 333408，PD）、P3 weihnachtsmarkt1930.jpg（Ritter 1860–1948，PD）、P5 christkind.jpg（Kepler 1903，PD）、P7 lesesaal.jpg（Highsmith，国会图书馆，PD）、P8 fussball1905.jpg（1905 年，作者不详，PD）——印署与 CREDITS 一致，未见版权不明肖像。

### ABSTRACT.txt
- 单行、无 ASCII 双引号、简体中文；含刊名、目标语名、A2–B2 分级、150 道练习与本期真实主题 ✓。

### P7 读者来信
- 明确标明编辑示例（`Ein Beispiel der Redaktion!` + 截稿未收到真实来信、见 VOL.5，中德双语）✓；无编造来信；承诺顺延 VOL.5 ✓。

---

## 观察项（不计缺陷，留协调员知悉）

### O1：P8 完形填空段落与对话段落 14.625pt、选项行 13.875pt
- 实测：P8 完形段落（`Lena freut sich…`）与对话段落（`— Hallo, Lena!…`）为 19.5 单位 = 14.625pt；其选项行（`113. A. schaut…` 等 13 行）为 18.5 单位 = 13.875pt（PyMuPDF：P8 13.88pt span 共 13 处、14.62pt span 36 处，与之吻合）。
- 定位：上述文字不是 `ex()` 题干（D1 核查范围），是 P8 特有的段落式题型（完形 113–120、对话 145–149）的段落与选项行；返修未动此处（W46-DE `content8.py` 第 40 行即为 18.5，属继承结构）。
- 对照：验收版 W46-FR 的 P8 同类位置亦低于阶梯——完形段落 15.75pt、选项行 14.62pt（PyMuPDF 实测该版 P8）；德文版比法文版低约 0.75–1.1pt，但结构模式相同（段落 > 选项行，均低于 ex() 题干）。
- 处理建议：不计入本轮缺陷；若协调员认为 P8 段落亦应执行 15.4pt 让步下限，可在下一修轮统一调整（需重排 P8 版面）。

---

## 未改动声明
- 未修改 core-de 任何文件；freeze 复现与登记表重跑均在 scratch 副本内完成（复现副本已删，仅留 `work/freeze.log`）；未改 tools；未跑 insert.py、lint --write、git push/add/reset/stash；未碰 W43/W45/W46（仅只读实测 W46 法文验收版 PDF 作 §1.1 对照标尺）。
- 写入过程无 EPERM / 磁盘配额 / ffmpeg 失败。
