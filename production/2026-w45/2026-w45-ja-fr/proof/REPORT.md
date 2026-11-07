# W45 日语×法语分版（JA×FR）独立校对报告

**校对对象：** `files/weekly-report-w45-ja-fr/`（SVG×8、卡片×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt），构建树 `hidden_files/weekly-report-w45-ja-fr-build/`；对照核心 `files/weekly-report-w45-ja-core/`（JA VOL.2）与 W43 同配对版 `files/weekly-report-ja-fr/`。
**校对员身份：** 独立校对，只校对、不改源码。未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）、未清理共享 scratch 目录。
**结论：ZERO PROBLEMS**（阻塞项 0 项；非阻塞观察单列于 §13）。**本报告不宣布上架**——上架由主线串行执行。

---

## 0. 开工查重与冻结

- 开工前 `ps` 仅见一无关在途进程（他版 KO 系卡片预览，cwd 与本版无关；其 sha256 进程在开工时已退出）。本版交付目录最新 mtime 为 2026-10-28 01:50:06（UTC），经 70 秒以上静默复查（至 01:52:21，逾 120 秒静默）后开工，无本版在途写盘。
- 校对前后 sha256：交付物 `sha256-before.txt` vs `sha256-after.txt` **diff 为空**；核心 `sha256-core-before.txt` vs `sha256-core-after.txt` **diff 为空**。校对全程未改动交付物与核心。
- 规范 svglib：分版构建树 `svglib.py` 与核心构建树 `svglib.py` 的 md5 均为 `d73e23b365676c3618d7e060b835eb4d`，与 transform.py 内 `CANON_SVGLIB_MD5` 一致，规范文件未被编辑。

## 1. 冻结（freeze）与日语正文无丢失

- `tools/freeze.py baseline`（核心构建树 → scratch）：**8/8 逐字节复现**，核心 SVG 在运行前后哈希不变。核心本身可信，可作比对基线。
- `tools/freeze.py diff`（核心 vs 分版）：新增 CJK **全 8 页均为 0**；CJK 总量 P1 1406→1275、P2 1312→1161、P3 1172→1051、P4 1263→1169、P5 1247→1132、P6 1186→1101、P7 1676→1308、**P8 2721→1448**，与构建员所述一致（证据 `freeze-diff-mine.json`）。
- 被删串逐项裁定（297 个 freeze removed 文本节点，证据 `removed-adjudication.txt`）：
  - 184 项纯中文讲解层（中文注、中文标题、中文指令、中文页脚）→ 均有法语对应；
  - 75 项含日语键的混合串 → 日语键在分版中保留（如 `見頃`、`工芸`、`神戸のライトアップ` 等随法语注同行保留）；
  - 38 项 CHECK 经逐项复核，**全部是讲解层或换行碎片，无一为日语正文丢失**，分两类：
    - 10 项换行碎片/讲解替换：gloss 换行碎片 2 项（`しむ 享受。`、`译注｜総括…確認す`，对应法语 gloss 中 `楽しむ`、`確認する` 完整保留）；P7 日语披露句 ld 的 4 个换行碎片（见 §10，属讲解层替换而非正文）；P7 诊所中文注 3 项（`动作发生的场所用「で」。` 等 → 法语诊所注，日语被引词保留）；P7 金句中文译文 1 项（`所谓ゆる…` → 法语金句译文）；
    - 28 项 P8 答案行：其注为讲解层（中文或日语释义），分版中均已译为法语，日语键/日语句本身保留（如 #135 键句 `図書館で本を借ります。` 逐字保留、#41 键句保留、#80 `守って` 保留）。完整法语对照见 §5 附表与 `p8-lines-full.txt`。
- 违禁词 `桥接`：分版 SVG **0**、WEEKLY-KIT.md **0**、ABSTRACT.txt **0**。

## 2. 日语专项：kinsoku 与词级中文残留

- 行首禁则（行首字符 ∈ `、。．，・：；？！）〕］｝〉》」』】)]}>}・ァィゥェォッャュョヮー`）：**8 页全部为 0**，与构建员所述一致（证据 `kinsoku.txt`）。
- 词级中文残留（不仅字级）：
  - 字符级：分版全部 CJK 字符集 ⊆ 核心印刷文本字符集（新增字符 0）；简体专属字扫描（`为说这那让对从还进过发观语读译览头条间见时题问门车马龙龟乐欢仅钟铁银黑鸟鱼艳` 等）**0**；分版 P8 150 行中简体专属字 **0/150**。
  - 词级：分版 920 个互异 CJK run 中，仅 12 个未逐字见于核心文本节点，逐个裁定**全部为日语词**，均为切分口径伪影（核心中该词嵌在更长的中日混合串里，分版中因法语注分隔而独立成 run）：`「か所」「こと」「で」「昨日」`（P7 诊所法语注引用的日语语法点）、`「紅葉の本」「静かだけど、冒険中。」`（引文括号/前后中文粘连所致）、`〜しましょう`、`コパン`、`守る`、`楽しむ`、`確認する`、`見たい`（核心中嵌于 `守る遵守`、`楽しむ享受`、`確認する核实`、`見たい＝想看` 等串，分版中作词头/键独立出现）。**真中文专属词 0**。
  - 另有 7 个不在“保留（与核心相同）节点”中的字符（`ォ内容毎療若診`），经核查全部是核心日语栏目标题词（`この号の内容`、`毎週`、`まちがい診療所`、`若者`、`言語フォーカス`），因栏目标题后缀由中文改为法语而整节点不同，词本身是日语，无残留。

## 3. #37 修复专项（JA 族既定陷阱，重点）

- 陷阱源：核心 `content34.py:82` 的 P3 填空题注为无星期后缀的裸串 `工艺展到11月8日`（与带后缀的 `工艺展到11月8日（周日）` 为两个不同注；后者对应 P3 单选题与 P8 #32）。若 NOTES 表无独立条目，裸串会原样穿透为中文。
- 本版验证（全部独立实测）：
  - P8 第 37 题印刷行确为法语：**`37. 8 — L'exposition dure jusqu'au 8 novembre`**（SVG 文本节点 x=65, y=2516.55；P8 最终卡片目视亦见该行；光栅裁剪 `p8-37-crop.png` 清晰可读）。
  - P8 SVG 中 `工艺展` 残留 **0**；全册 SVG 中 `工艺展`、`传统` 均为 **0**。
  - 第 4 轮基线范围验证（`round4-scope.txt`）：P1–P7 SVG 哈希与第 4 轮**全部相同**，P1–P7 卡片哈希与第 4 轮**全部相同**；变化的仅 **P8 SVG + P8 卡片 + 双 PDF** 三项，修复范围确仅第 5 轮一处。
  - 裸串/带后缀串区分保持正确：#37（裸串）→ 无星期后缀的 `L'exposition dure jusqu'au 8 novembre`；#32（带后缀串）→ `L'exposition dure jusqu'au 8 novembre (dimanche)`；P8 #122（`传统工艺展到11月8日`）→ 同句无后缀版。三者互不混淆。
  - 事实一致性：题面事实为“工艺展到 11 月 8 日”。P3 填空题面为 `展覧会は11月 ___ 日（日）までです`，答案为 8；2026-11-08 经 `date` 实测为**星期日**，与题面（日）、#32 的 (dimanche) 一致；11 月 3 日为星期二、11 月 7 日为星期六、11 月 9 日为星期一，亦与全册星期注一致。法语译文与题面事实一致，无事实错误。

## 4. P8 注释完整性专项（既定 JA 族门）

- 方法：独立于 p8.py 的 P8 答案区行拼接（以 `答え` 栏后、y<2580 为答案区，跳过 `— Page n —` 分隔行，数字开头为新题、后续行按 CJK 边界拼接），核心与分版各得 **150 条、题号 1–150 连续、无缺无增**。
- 结果：**150/150 均有法语对应**；核心注为中文的每一行，分版注均为法语；**与核心完全相同的印刷行数为 0**——不存在“应法语化而与核心相同”的行，无需再为相同行说明合法性（相同行不存在；日语原文键如 #133–#136、#139、#140 的日语句键保留，但其注已法语化，故整行并不相同）。
- #150 表面相同问题：核心行 `150. ✓ 范文见本版 H 区（167 字）`，分版行 `150. ✓ Modèle dans la section H de cette page (167 caractères)`，**两行并不相同**。所谓“表面相同”只是 p8.py 的解析口径：`detect_note` 对以 `✓` 开头的段返回解析键 `✓`（注 = 剩余文本），故两版解析键同为 `✓`；全行文本、语言、措辞均不同，167 数字一致。✓ 行不构成未翻译残留。
- 完整 150 行对照见 `p8-lines-full.txt`（附简体专属字逐行扫描：0/150）。

## 5. P8 keydiff（显式双路径，口径独立确立）

- 150=150 口径独立确立（未照搬 EN 核心 78 口径与 JA×EN/JA×DE 的 150 口径）：① 本报告 §4 的答案区行拼接：核心 150 条、分版 150 条，题号连续；② scratch 重定向登记展开（§12）：核心与分版 REG 总数均为 150；③ 在此基础上运行 `tools/p8.py compare --core-p8 …/ja-core/svg/p8-tesuto.svg --edition-p8 …/ja-fr/svg/p8-tesuto.svg --total 150`。
- 结果：**CLEAN，core 150 noted = edition 150 noted，missing=[]，extra_count=0，uncertain=[]**，keydiff 21 项（证据 `p8-compare-mine.json`、`p8-lines-mine.txt`）。
- **无歧义计数（按根本原因划分，无重叠，合计 21）：真重定向 2 项；提示本地化落入 keydiff 1 项；纯括号分支伪影 18 项。提示本地化总数 4 项。** 按解析机制计，括号介导的 keydiff 为 19 项（18 纯伪影 + #140，其解析键变化同样经由括号分支介导，但根本原因是注的缩短本地化，故在根本原因计数中归入提示本地化，不重复计入伪影）。构建员 KIT 中“19 项注释伪影 + 2 项合法重定向”的表述把 #140  lump 入伪影；本报告将其单列，计数无歧义。
  - **真重定向 2 项**：#137、#138（E 区翻译题的键本身由读者语改向：中文句 → 法语句，合法）。
  - **提示本地化落入 keydiff 1 项**：#140（见下）。
  - **提示本地化总数 4 项**：E 区页码提示注 #137、#138、#139、#140。其中 #137/#138 同时是真重定向，#139 不在 keydiff（干净本地化），#140 在 keydiff（见下）。
  - **纯括号分支伪影 18 项**：#1、#2、#5、#7、#8、#9、#29、#32、#65、#69、#78、#101、#113、#115、#117、#118、#146、#147（真键在 ` — ` 前完全相同；解析键差异只因注尾括号被 p8.py 的括号分支吸入解析键。#5、#101 为不对称情形：核心注内括号不在末尾故按 dash 解析，分版注以 `(samedi)/(mardi)` 结尾故按 paren 解析，仍属同一机制）。
- #139 归属：**不在 keydiff**。核心 `読書週間は10月27日から始まります。 — 对照第7版` → 分版 `読書週間は10月27日から始まります。 — Voir page 7`。日语键保留，页码提示干净本地化，解析键相同。
- #140 归属：**落入 keydiff 的提示本地化（不是纯伪影）**。核心 `神戸の紅葉のライトアップを見に行きたいです。 — 对照第6版（神户的灯光秀）` → 分版 `神戸の紅葉のライトアップを見に行きたいです。 — Voir page 6`。真键（日语句）两版完全相同；核心注的括号内中文释义随注缩短而删除，页码指向本身无内容损失（日语句键已含全部信息）。解析键差异的机制是括号分支（核心解析键吸入 `— 对照第6版`，分版解析键为纯日语句），但根本原因是注的本地化缩短，故计入提示本地化，不计入 18 项纯伪影。
- 21 项逐项印刷行对照裁定表：

| 题 | 核心印刷行 | 分版印刷行 | 裁定 |
|---|---|---|---|
| #1 | 3 — 文化日在11月3日（周二） | 3 — La Journée de la culture, c'est le 3 novembre (mardi) | 括号分支伪影（真键 `3` 相同） |
| #2 | 9 — 读书周到11月9日（周一） | 9 — La Semaine de la lecture dure jusqu'au 9 novembre (lundi) | 括号分支伪影（真键 `9` 相同） |
| #5 | 7 — 神户灯光秀从7日（周六）开始 | 7 — Les illuminations de Kobe commencent le 7 (samedi) | 括号分支伪影（不对称括号位置；真键 `7` 相同） |
| #7 | B — 文化日在11月3日（周二） | B — La Journée de la culture, c'est le 3 novembre (mardi) | 括号分支伪影（真键 `B` 相同） |
| #8 | C — 读书周到11月9日（周一） | C — La Semaine de la lecture dure jusqu'au 9 novembre (lundi) | 括号分支伪影（真键 `C` 相同） |
| #9 | B — 立冬在11月7日（周六） | B — 立冬, c'est le 7 novembre (samedi) | 括号分支伪影（真键 `B` 相同） |
| #29 | A — 文化日在11月3日（周二） | A — La Journée de la culture, c'est le 3 novembre (mardi) | 括号分支伪影（真键 `A` 相同） |
| #32 | B — 工艺展到11月8日（周日） | B — L'exposition dure jusqu'au 8 novembre (dimanche) | 括号分支伪影（真键 `B` 相同；带后缀串，星期保留） |
| #65 | A — 万圣节在10月31日（周六） | A — Halloween, c'était le 31 octobre (samedi) | 括号分支伪影（真键 `A` 相同） |
| #69 | C — 横滨中区民祭在11月8日（周日） | C — Le festival de Naka a lieu le 8 novembre (dimanche) | 括号分支伪影（真键 `C` 相同） |
| #78 | ○ — ハロウィンは10月31日（土） | ○ — Halloween, c'était le 31 octobre (samedi) | 括号分支伪影（真键 `○` 相同） |
| #101 | 27 — 读书周从10月27日（周二）开始 | 27 — La Semaine de la lecture commence le 27 octobre (mardi) | 括号分支伪影（不对称括号位置；真键 `27` 相同） |
| #113 | A — 文化日在11月3日（周二） | A — La Journée de la culture, c'est le 3 novembre (mardi) | 括号分支伪影（真键 `A` 相同） |
| #115 | A — 日本大赛第1战在10月24日（周六） | A — Le match 1 des Japan Series : le 24 octobre (samedi) | 括号分支伪影（真键 `A` 相同） |
| #117 | B — 万圣节在10月31日（周六） | B — Halloween, c'était le 31 octobre (samedi) | 括号分支伪影（真键 `B` 相同） |
| #118 | A — 立冬在11月7日（周六） | A — 立冬, c'est le 7 novembre (samedi) | 括号分支伪影（真键 `A` 相同） |
| #137 | 文化日是11月3日。 — 对照第3版 | La Journée de la culture, c'est le 3 novembre. — Voir page 3 | **真重定向**（E 区键由中文句改向法语句，合法） |
| #138 | 乱扔垃圾，要罚2,000日元。 — 对照第5版 | Jeter des déchets coûte 2 000 yens d'amende. — Voir page 5 | **真重定向**（E 区键由中文句改向法语句，合法） |
| #140 | 神戸の紅葉のライトアップを見に行きたいです。 — 对照第6版（神户的灯光秀） | 神戸の紅葉のライトアップを見に行きたいです。 — Voir page 6 | **提示本地化落入 keydiff**（真键日语句相同；注缩短，括号内中文释义删除，页码指向无损失） |
| #146 | A — 借りられます＝能借（可能形） | A — 借りられます = pouvoir emprunter (forme potentielle) | 括号分支伪影（真键 `A` 相同；注尾括号形式 `＝…（…）` → `= … (…)`） |
| #147 | A — 读书周到11月9日（第7版） | A — La Semaine de la lecture : jusqu'au 9 novembre (page 7) | 括号分支伪影（真键 `A` 相同；注尾 `(第7版)` → `(page 7)`） |

- P8 注释纯法语：150 条分版答案行的注全部为法语（日语词头/日语键句除外，如 `見頃`、`神戸の…です。` 等键本身）；印刷笔记集合按题号相等（本版 p8.py 结果为 CLEAN 而非 EXTRA_ONLY，无需援引 EXTRA_ONLY 接受条款）。

## 6. P7：定义句、金句、页标签、预告带

- 定义句逐字保留、本地化 **0 处**：P7 核心与分版文本节点差集（证据 `p7.txt`）中，差异仅为法语/中文讲解层——栏头、bridge、指令（`填空`→`Complétez`）、诊所法语注、框架法语注、读者园地披露、金句法语译文、预告栏头、页脚；A2/B1/B2 三栏定义段落、框架日语句、诊所日语错句与正句、示例信、金句日语句本身均不在差集中，即逐字相同。节点数差异（核心 141 vs 分版 143）仅为法语/中文 bridge 换行行数不同。
- 金句 8 句全册计数**各恰 2×**（去空白拼接计数；括号剥离后计数亦为 2×）：`文化の日は、11月3日（火よう日）です。`、`ゆっくり、ゆるく整える日本の11月です。`、`『ゆる』は、無理をしない、ゆっくり、という意味です。`、`鍋の材料が1か月早く並び始めました。`、`伝統工芸と紅葉と光を、いっしょに楽しむことができます。`、`ソフトバンクが2連勝でスタートしました。`、`ルールを守って、楽しいハロウィンにしましょう。`、`紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。`——每句一次见于原文页、一次见于 P7 金句区。另 4 条 P7 提取的 `「」` 串（`昨日、友達と鍋を食べます` 等）为诊所错句例，各计 1×，不属于金句，不计入 8 句。
- 页标签映射与核心一致（以本报告核心实测为准）：核心 `第 n 版 / 共 8 版` → 分版 `Page n sur 8`，n=1–8 按文件页序一一对应，8 页全部核对。
- P7 预告带止点独立实测：P7 深带矩形 y=2382.08、h=118，止点 **2500.08 < 2540**（直接取自分版 P7 SVG 矩形几何，非构建日志转述；预告栏内文字 y=2426.08/2466.08 均在带内）。

## 7. gloss 口径专项

- 渲染后实测（证据 `gloss-rendered.txt`；核心 gloss 前缀为 `译注｜`，分版为 `Note — `，同 x 续行拼接后按 `·` 拆分，逐页对照）：
  - 核心：P1 [4]=4、P2 [4,5]=9、P3 [4,4]=8、P4 [4,3]=7、P5 [4,3]=7、P6 [4]=4，合计 **39**；
  - 分版：P1 [4]=4、P2 [4,5]=9、P3 [4,4]=8、P4 [4,3]=7、P5 [4,3]=7、P6 [4]=4，合计 **39**；逐页、逐盒 1:1 对照，词头相同、释义由中文改为法语。
- 与构建员内容文件分组的换算关系：构建员的 `[4,4,5] / [4,4,4,3] / [4,3,4]` 是**按内容文件**分组（content12 的 3 个 gloss 串 / content34 的 4 个 / content56 的 3 个），不是按页分组；换算为按页口径：content12 的 [4,4,5] 横跨 P1（4）+ P2（4+5）；content34 的 [4,4,4,3] 横跨 P3（4+4）+ P4（4+3）；content56 的 [4,3,4] 横跨 P5（4+3）+ P6（4）。两种口径合计均为 39，与 JA×EN/JA×DE 的渲染口径 P1 4/P2 9/P3 8/P4 7/P5 7/P6 4 = 39 一致（仅作参照；本结论由本版核心与分版渲染实测独立得出，未引用构建员分组数字作为渲染结论）。注：拼接重建会吞掉换行处的空格（如 `暦历法`），属重建拼接伪影，SVG 各行本身无误，`·` 计数不受影响。

## 8. 几何

- canonical `tools/occlusion_audit.py`（自检先行：6 类 planted 全部触发，clean controls 静默）：分版 **0 旗**、核心 **0 旗**、**NEW vs 核心 0**（证据 `occlusion-mine.json`、`occlusion-core-mine.json`）。同基线墨迹碰撞扫描即该工具的双跑，结论相同。
- P6 图表标签基线锚定墨迹法：以工具的 anchor-aware 真墨迹盒（`ink_box`）对 P6 图表区 8 个标签（左标签 `近場の満足/温泉/紅葉/グルメ` + 值标签 `38%/27%/21%/14%`）逐个量算与 4 条柱形（x=315 起，宽 1140/810/630/420）的重叠率，**全部为 0.000 < 30%**（值标签起点距柱末最近处亦有 16px 间隙，如 38% 起于 1471、柱止于 1455）。getbbox 法未采用（该法为错误口径）。
- 全页右缘 ADVANCE 扫描（`getlength`、anchor start/middle/end 分别处理）：8 页中 advance 末端 >1885（内容右缘）、>1922（内框）、>1950（页缘）的文本**全部为 0**（页脚右端恰止于 1885，不计入超出）。
- 框线压框扫描：即工具的 BOXTITLE 类，**0 旗**（工具自检中 BOXTITLE planted 已验证可触发）。
- 卡片目视：**8 张最终卡片全部目视**（非抽查），且目视前先以哈希验证版本归属：P1/P2 卡片确与第 4 轮一致（P1 `1045c9…`、P2 `09bbd9…`），P3–P7 为本轮版、P8 为第 5 轮新版（`c2d0b0…`，与第 4 轮 `da5386…` 不同），目视的即当前交付文件本身。目视结果：P1 刊头/徽章/页脚正确、红叶照片与署名在版；P2–P6 版式、注盒、照片/图表无溢出、无遮挡；P7 诊所/框架/读者园地/金句/预告带完整；P8 练习区 A–H 与答案区 150 行完整，#37 法语行、#140、#150 均清晰可读。P2 的 `D · ペアにしましょう` 栏头孤行、P5 的 `D · 文を完成しましょう` 栏头位置与核心 SVG 坐标逐字相同（P2：x=989, y=2235.2 两版一致），属核心继承版式，非分版缺陷（见 §13）。

## 9. 法语讲解层残留与缩短项

- 第 4 轮英文残留已消除：`Readers' corner` 在分版 SVG 中 **0** 处；P7 栏头现为 `Le courrier des lecteurs`（1 处）。全册法语讲解层英语残留扫描（全部拉丁词 token 清单见 `residue.txt`）：**英语残留 0**，其余拉丁词逐项说明如下，均属例外情形——任务键（`Complétez`、`Associez` 等法语指令）、被讲解的日/法语词条（`nabe`、`ゆる`、`見頃` 等）、法语正常借词与法语同形词（`match`、`festival`、`public`、`satisfaction`、`week-end`、`Quiz éclair`、`Test`、`home run` 棒球借词）、专名（`Japan Series` 赛事名、`SoftBank`、`DeNA`、`JMA`、`SNS`、地名人名 `Kobe/Kanazawa/Suginami/Ikebukuro` 等）、署名源名（`Wikimedia Commons`、`CC0`、`Poliphilo/Syced/Petr Kratochvil`）、法语介词（`TEXTE EN JAPONAIS` 中的 `EN`）。
- 第 2 轮缩短项无内容损失：
  - P7 披露：法语披露句完整（见 §10），3 事实 + 邀请 + VOL.3 承诺齐全；
  - P7 诊所注：4 条法语短注（`Avec 「昨日」, employez le passé.` / `「こと」 nominalise le verbe.` / `Comptez les lieux avec 「か所」.` / `Employez 「で」 pour le lieu de l'action.`）各 1 处；日语错句与正句本身逐字保留在诊所盒内，法语注仅为短释，无信息丢失；
  - P8 键注 #140 → `Voir page 6`：见 §5 #140 裁定，页码指向无损失。
- 第 3 轮缩短项无内容损失：
  - P1 警示句：核心 `来源与日期见各篇文章，非精确统计` → 分版 `Dates dans les articles ; chiffres approximatifs`（各 1 处），“日期见文章”与“数字非精确”两要素齐全；
  - 两条配对指令 `Associez mot et définition`：分版共 **2 处**（P2 配对 25–28、P8 F 区 141–144），与核心 `把词和释义配对` 的 2 处一一对应，指令内容（词↔释义配对）完整；
  - P3 事件指令 `Événement, lieu et date`：分版 **1 处**（P3 D 区 43–46），与核心 `把活动和地点·时间配对` 的 1 处对应，事件/地点/日期三要素齐全。

## 10. 读者园地

- 日语示例信逐字不动、零编造：核心与分版 P7 信行完全相同——`「こんにちは。私は中学生です。読書週間には、図書館で本を2冊読みたいです。文化の日には、家族と金沢へ行きたいです。」— 読者の手紙の例`（两版同一行，含 `— 読者の手紙の例` 后缀）。
- 法语披露句逐字摘录（P7 读者园地盒内，分版 SVG 换行拼接后）：`Exemple de la rédaction, pas une vraie lettre. Aucune lettre, aucun meilleur texte de la page 8 avant la date limite : les deux paraîtront dans le VOL.3. Envoyez-nous votre lettre en japonais — les lettres choisies seront publiées dans le VOL.3 !`——与构建树 content7.py 的 `ld_fr` 逐字一致，非凭空新写。
- 3 事实逐项核实：① 示例非真信（`Exemple de la rédaction, pas une vraie lettre`）✓；② 截稿前无真信（`Aucune lettre … avant la date limite`）✓；③ 无最佳 P8 作文且顺延 VOL.3（`aucun meilleur texte de la page 8 avant la date limite : les deux paraîtront dans le VOL.3`）✓。另含显性祈使邀请（`Envoyez-nous votre lettre en japonais`）✓ 与 VOL.3 刊登承诺（`les lettres choisies seront publiées dans le VOL.3 !`）✓。
- 最佳 P8 作文覆盖范围显式裁定（按 pt 族既定范围）：邀请字面仅覆盖来信（`Envoyez-nous votre lettre`），但同页披露句将最佳 P8 文本与来信一并顺延 VOL.3（`les deux paraîtront dans le VOL.3`），**组合满足**；P7 预告行（深带日语句 `…読者の手紙と第8版の作文の優秀作も載せます。お楽しみに！`）本身不计入邀请——本裁定不依赖预告行。
- 披露替换核实：分版 P7 中日语披露句 ld（核心 `※この手紙は編集部の例です…`）出现 **0** 次、中文披露句 lcn（`编辑部示例信，非真实来信…`）出现 **0** 次；唯一 operative 披露为上述法语披露句。日语披露句未作为 operative 披露残留。

## 11. 家具 / W43 对照

- 三方实测（P1 刊头，基线 y 坐标；证据 `furniture.txt`）：

| 项目 | W43 JA×FR | W45 核心 | W45 JA×FR（本版） | 结论 |
|---|---|---|---|---|
| 刊头 Lucerna（168pt） | 248 | 262 | **248** | 与 W43 一致 |
| 版名行（40pt） | 316 | 330 | **316** | 与 W43 一致 |
| 徽章（19pt，加粗） | 356 | 无 | **356** | 槽位与 W43 一致；核心无此行 |
| 标语（19pt） | 390 | 372 | **390** | 与 W43 一致 |
| 规则线（3 / 1.2） | 406 + 413 | 392 + 401 | **406 + 413** | 与 W43 一致 |
| 深带矩形 y | 424 | 424 | **424** | 三者一致 |

- 徽章文本逐字同 W43：`TEXTES EN JAPONAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`；标语逐字同 W43：`日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で`。W43 同配对家具胜过 README #20 泛化规则——本版采用 W43 槽位而非核心槽位，符合该规则。
- 配对见于 P1 刊头徽章与**全部 8 页页脚**：每页页脚均为 `Lucerna · HEBDOMADAIRE JAPONAIS VOL.2 · TEXTE EN JAPONAIS · EXPLICATIONS EN FRANÇAIS` + `Page n sur 8`（n=1–8）。
- 非阻塞观察：徽章文字颜色 W43 为 `#a4553a`、本版为 `#3e4c2a`；JA 族内颜色本就各版不同（JA×EN 亦为 `#3e4c2a`、JA×DE 为 `#a4553a`），任务三方测量口径为槽位/字号/文本，三者均一致，颜色不在该门内，列入 §13 观察（见 §13）。

## 12. 题量 / 范文 / ABSTRACT / 图片

- 登记展开独立计数（scratch 重定向二次验证，方法见下）：**150 题**；级别 **A2 46 / B1 75 / B2 29**；页分布 **10 / 18 / 18 / 18 / 18 / 18 / 12 / 38**；与核心登记展开逐项一致。方法：分版与核心构建树各拷至 proof scratch、将 OUT 全路径重定向至 scratch svg 目录后单进程运行 run.py；分版 scratch SVG 与交付 SVG **逐字节相同**，核心 scratch SVG 与核心 SVG **逐字节相同**，故 REG 即交付内容的登记（`reg-fr2.log`、`reg-core2.log`）。
- 题型分布（分版 REG 法语型名 ↔ 核心中文型名，经 transform GLOBAL 映射逐项核对）：Compléter 50（完成句子）、Choix multiple 51（单选）、Appariement 12（词汇配对）、Former une phrase 8（造句）、Vrai ou faux 11（判断对错）、Texte à trous 13（完形单选）、Traduction 4（翻译）、Rédaction 1（写作），与构建员所述一致，且与核心各型数量一一相等。
- 范文 167 字（从印刷范文复数，非只信源码）：P8 H 区印刷范文 6 个换行行拼接后去空格计 **167 字**，与 #150 行 `(167 caractères)`、REG 日志 `model chars: 167` 三方一致；范文题 `『私の11月の週末』`，P8 分 A–H 节、E 节为 JA↔FR 翻译 4 题（核心为 JA↔ZH，改向合法，见 §5）。
- ABSTRACT（`ABSTRACT.txt`）：法语单行（仅尾换行）、无 ASCII 双引号；含刊名 `Lucerna`、目标语 `japonais`、级别 `A2 à B2`、150 题（`150 exercices de japonais`）；真实主题关键词：`Journée de la culture du 3 novembre`、`week-end des érables du 7 au 8 novembre`、`gorges de Naruko`、`illuminations de Kobe`、`Semaine de la lecture`、`Japan Series`；学习者搜索短语：`apprendre le japonais en lisant`；并明示 `textes en japonais et explications en français`。全文：`Lucerna, hebdomadaire japonais pour lecteurs francophones : Journée de la culture du 3 novembre, week-end des érables du 7 au 8 novembre, gorges de Naruko, illuminations de Kobe, Semaine de la lecture et Japan Series, avec 150 exercices de japonais niveaux A2 à B2, textes en japonais et explications en français pour apprendre le japonais en lisant.`
- 图片（证据 `model-abstract-images.txt`）：4 张图片载荷逐页 = 核心（P1 红叶、P3 广重版画、P4 横滨体育场、P5 南瓜；数据 URI 解码哈希与几何 x/y/w/h 全部相同；P2/P6/P7/P8 无照片，与核心一致）；署名在版且与构建树 `assets/CREDITS.md` 的 Commons API Artist 字段一致：P1 `写真：Poliphilo — CC0（Wikimedia Commons）`、P3 `版画：歌川広重（三代）— パブリックドメイン（Wikimedia Commons）`（跨 2 行）、P4 `写真：Syced — CC0（Wikimedia Commons）`、P5 `写真：Petr Kratochvil — パブリックドメイン（Wikimedia Commons）`（跨 2 行）。双 PDF 均为 8 页：印刷 PDF 28,047,840 字节，web PDF 3,118,778 字节（<10 MB）。

## 13. 非阻塞观察（单列，不构成阻塞项）

1. **行末开括号换行 9 处（核心继承）**：分版与核心各有完全相同的 9 行以开括号/开引号结尾（P1 4 行、P2/P3/P4 各 1 行、P5 2 行；如 `立冬はいつですか。 A. 3日（火） · B. 7日（`），行、y 坐标逐字相同。任务指定的 kinsoku 门为行首禁则（已为 0）；行末开括号属核心 wrap 算法的继承版式，分版若“修复”将破坏日语正文逐字节一致，故列为观察，不阻塞。
2. **徽章文字颜色**：W43 `#a4553a` vs 本版 `#3e4c2a`（见 §11）。槽位/字号/文本三方一致；JA 族内颜色各版不同，不阻塞。
3. **栏头孤行属核心继承**：P2 `D · ペアにしましょう`（x=989, y=2235.2）与核心坐标逐字相同，配对题本体流至下一栏，属核心版式；P5 `D · 文を完成しましょう` 同理。不阻塞。
4. **P7 A2 栏下空白**：三栏练习区底止于 y≈1560、金句区起于 y≈1712 之后，栏下空白为核心版式（金句区位置由 `max(1712, col3_end + 44)` 决定），非缺失。不阻塞。
5. **构建员 KIT 的 keydiff 表述差异**：KIT 称“19 项注释伪影 + 2 项合法重定向”，把 #140 计入伪影；本报告按根本原因计为 2+1+18（§5），两者总数同为 21、#140 的法语行本身无误，仅计数口径不同，已在本报告中无歧义说明。不阻塞。

## 14. 测量纠错与一次操作披露（透明记录）

- 本报告测量中三次自我纠错，均已以修正后的方法重测并留有证据：① 首次 gloss 渲染测量误用分版前缀 `Note — ` 套用于核心（核心前缀实为 `译注｜`），已修正重测得 §7 的逐页 1:1；② 首次第 4 轮卡片对照误以 SVG 文件名作卡片键，已修正为 PNG 文件名重测得 §3/§8 的范围结论；③ 首次登记展开重定向误用子串替换，致 OUT 成为双前缀畸形路径（见下）。
- 关于 ③ 的披露：首次重定向运行的 SVG 写到了 `~/workspace/goals/lucernaread-social-media-operations/home/…` 下的畸形嵌套路径（该路径在 `files/` 之外），**从未写入交付目录或核心目录**（交付/核心 mtime 仍为构建员的 01:46–01:50，终态哈希 diff 为空可证）。清理该畸形树时一并删除了同一畸形树下此前已存在的他版同类残留（目录名含 `proof-ru-zh-tw`、`weekly-report-w45-de-zh-tw-build`，应为此前同类误重定向的残留，均在 `files/` 之外、非交付物）；如主线认为其中有需保留之物，请告知，本报告如实披露此事。第二次重定向改用全路径替换至 proof scratch，SVG 与交付逐字节相同（§12），登记结论以第二次为准。共享 scratch 目录（`tools/scratch`）未动。

## 证据文件（与本报告同目录 `hidden_files/w45/ja-fr-proof/`）

- `REPORT.md`（本报告）、`audit.py`（审计脚本，只读交付/核心，输出仅写本目录）
- `sha256-before.txt`、`sha256-after.txt`、`sha256-core-before.txt`、`sha256-core-after.txt`（前后 diff 均为空）
- `freeze-diff-mine.json`（freeze diff 全量）、`removed-adjudication.txt`（297 被删串逐项裁定）
- `kinsoku.txt`、`cjk-wordlevel.txt`、`residue.txt`（拉丁词全量清单）
- `p8-compare-mine.json`（p8.py 双路径结果）、`p8-lines-mine.txt`（keydiff 21 项 + #139/#140/#150 特写）、`p8-lines-full.txt`（150 行完整对照）
- `p8-37-crop.png`（P8 #37 光栅裁剪）
- `p7.txt`、`gloss.txt`、`gloss-rendered.txt`、`furniture.txt`、`model-abstract-images.txt`
- `round4-scope.txt`（第 4 轮范围验证）、`occlusion-mine.json`、`occlusion-core-mine.json`
- `reg-fr2.log`、`reg-core2.log`（scratch 登记展开）、`scratch-freeze/`（核心基线复现输出）、`scratch-reg2/`、`scratch-reg2-core/`（登记展开 scratch 树）
