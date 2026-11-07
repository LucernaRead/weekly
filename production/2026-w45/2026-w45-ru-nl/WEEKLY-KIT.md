# WEEKLY-KIT — Lucerna Russian Weekly, VOL.2, RU × NL (W45)

## 1. Spec 与状态

- **分版：** 俄语正文 × 荷兰语讲解（目标 RU × 读者母语 NL），面向荷兰语读者学俄语。
- **期次：** 2026 年 11 月 2 日星期一至 11 月 8 日星期日，VOL.2，与已定稿上架的 W45 RU 核心同周。
- **底本：** 已定稿的 RU 核心（files/weekly-report-w45-ru-core/，VOL.2，150 题）。
  讲解层全部用荷兰语直接对应俄语原文写成；俄语正文冻结，见 §4。
- **状态：修复轮完成、独立复校待定（不作定稿宣称）。** 2026-10-27 修复轮
  仅修 P7 读者园地征集句一项（见 §11 修复记录）；按 SOP §8.4，修复后须
  另派独立全量复校，本轮不构成定稿。未发 Discord，
  未往主聊天发卡片或 PDF，未建 cron，未碰 weekly-git，未做 repo 插入。
- **开工查重（2026-10-27）：** 开工时 files/weekly-report-w45-ru-nl/ 与
  hidden_files/weekly-report-w45-ru-nl-build/ 均不存在，无正在进行的 ru-nl
  写盘与渲染进程；60 秒复查零新写盘后开工。核心 SVG 与 PDF 在全部工作
  前后哈希一致（§10），核心构建目录内从未 import 内容模块。

## 2. Totals（注册表，与核心一致）

- **150 题，统一编号 1–150。** 分页：P1 10、P2 18、P3 18、P4 18、P5 18、
  P6 18、P7 12、P8 38。分级：A2 51、B1 75、B2 24。
- 分题型（荷兰语题型名，题数与核心一致）：Voltooi de zin 54、
  Meerkeuze 42、Woorden koppelen 20、Cloze-meerkeuze 13、
  Zinnen bouwen 12、Zinsomvorming 4、Vertaling 4、Schrijven 1。
- P8 写作范文为冻结俄语原文，84 词（核心注册值，未改动）。
- 构建日志零 FLOW OVERFLOW、零 HEAD TOO WIDE 警告（run1.log 与 run2.log 均为 0）。

## 3. Pairing furniture（逐字抄 W43 已发 RU×NL 版，VOL.2）

- **P1 刊头配对徽章（本版实测于渲染后 P1 SVG）：**
  位置 (975, 372)，20pt 粗体，砖红 #a4553a，居中，字符串逐字为：
  «TEKSTEN IN HET RUSSISCH · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS»
- **W43 已发版对照（files/weekly-report-ru-nl/svg/p1-pervaya.svg 实测）：**
  同位置 (975, 372)，同 20pt 粗体，同砖红 #a4553a，同字符串逐字；
  仅 VOL 号不同（W43 为 VOL.1，本版为 VOL.2，徽章串本身不含 VOL 号）。
- **README #20 家族规则对照：** 俄语目标存在两种既定接受模式——372 系
  （ru-en、ru-fr、ru-it、ru-pt）与 574 系（ru-de、ru-es）。W43 同配对
  RU×NL 的实测属于 372 系：徽章原位替换 y=372 刊头副行。本版遵循 W43
  同配对实测，不采用 574 系插入槽；被替换的 y=372 行是核心自身的刊头
  家具行（见 §4 逐项），不是冻结俄语正文，因此未删除任何冻结俄语正文。
- **P1 上沿中心条：** «КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · ELKE WEEK · HET RUSSISCH DAT DE RUSSEN LEZEN»
  （W43 已发版逐字，实测于本版 P1 SVG）。
- **页脚（全部 8 页实测）：** 左 «Lucerna · RUSSISCH WEEKBLAD VOL.2 ·
  TEKSTEN IN HET RUSSISCH · UITLEG IN HET NEDERLANDS»；右 «Pagina N van 8»。
- **词注前缀：** «Uitleg — »（词注盒与 P1 词注行均同 W43 已发版）。
- **P8 答案分隔符：** «— Pagina N —»，N = 1..8（W43 已发版荷兰语形式；
  与 ru-en 版保留俄语分隔符的做法不同，本版以 W43 同配对版为准）。
- **P8 答案连接符：** 核心的 dash 式（N. key — note）保持不变，
  答案生成代码与核心逐字节一致；括号形式见 §5 末尾说明。
- **双语栏目标题：** 俄语原名 · 荷兰语短名，例如 «ГЛАВНАЯ ТЕМА · Hoofdthema»、
  «НЕДЕЛЯ В ЦИФРАХ · In cijfers»（W43 已发版同款短式，用于盒宽控制）、
  «ФРАЗЫ НЕДЕЛИ · Zinnen van de week (letterlijk uit dit nummer)»、
  «СЛЕДУЮЩАЯ НЕДЕЛЯ · Volgende week (VOL.3)»。
- **目录表：** 核心原文逐字保留，包括 Стр. 8 行的俄语级别标记（与 ru-en
  版对 W43 已发版的做法一致）。

## 4. Freeze baseline（冻结俄语正文逐字节一致性）

- 工具：tools/freeze.py diff（核心 SVG 对分版 SVG），结果文件
  tools/scratch/diff-w45-ru-nl.json。8 页新增汉字字符均为 0；
  分版渲染 SVG 汉字字符总数为 0（§9）。
- **西里尔词元多集对比（逐页，checks.py §1）：**
  P2–P7 精确相等，词元总数与核心一致：P2 443、P3 338、P4 306、P5 316、
  P6 354、P7 397（与 ru-en 版测得的核心计数一致）。
- **P1 差异只应是备案家具行，实测正是如此：** 词元总数 400 → 390，
  差异逐项恰为被替换的 y=372 刊头副行
  «ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ»
  的词元：ЕЖЕНЕДЕЛЬНАЯ、ДЛЯ、ИЗУЧАЮЩИХ、РУССКИЙ、ЯЗЫК、НАСТОЯЩАЯ、РОССИЯ
  各 1→0；ГАЗЕТА 2→1、ПО 3→2、РУССКИ 2→1。无其他西里尔词元差异，
  无未备案俄语词元丢失。
- **P8 差异一项，同样是备案家具：** СТРАНИЦА 8→0，恰为 §3 的分隔符
  «— СТРАНИЦА N —» → «— Pagina N —»（8 处），非正文改动。
- P1–P8 其余一切俄语正文词元多集相等；图片载荷见 §8。

## 5. P8 答案（tools/p8.py compare，dash 解析复核）

- 对比命令：p8.py compare --core-p8 核心 p8-test.svg --edition-p8 分版
  p8-test.svg --total 150。结果：**CLEAN，150 noted = 150 noted，
  missing = []，extra = []，uncertain = []；keydiff = [83, 137, 138, 148]**。
- **逐项 dash 解析复核（键 = 首个 — 之前）：**
  - 83：dash 键两边均为 B，无真改动。p8.py 列入 keydiff 是因为括号式
    键取到了注文前段：核心注文为中文，注文已译为荷兰语
    «3 vrije dagen in de week (woensdag, zaterdag, zondag)»，字母答案 B 不变。
  - 148：dash 键两边均为 A，无真改动。同理，括号注文由中文译为荷兰语
    «de promocode (mannelijk)»，字母答案 A 不变。
  - 137：真改动，翻译题重瞄准类（W43 翻译题先例）。俄语题干不变，
    指令为 «Vertaal naar het Nederlands»，答案键由中文改为荷兰语
    «Woensdag 4 november is een vrije dag.»。
  - 138：真改动，翻译题重瞄准类。俄语题干不变，指令同上，答案键由中文
    改为荷兰语 «Een promocode is een kortingscode.»。
  - 139、140 为反向题（荷兰语题干，指令 «Vertaal naar het Russisch»，
    答案键俄语原文逐字节不变），未列入 keydiff。
  - 150 为写作装置行（开放题说明与范文位置说明译为荷兰语），范文俄语
    原文不变，未列入 keydiff。
- **括号形式（README #14，家族构建代码为准）：** P8 答案生成代码与核心
  逐字节一致；注文字符串本身的括号随翻译文本书写——荷兰语注文使用
  半角括号（与 W45 ru-en 版对同一批注文的做法一致，其 keydiff 集合
  亦恰为 [83, 137, 138, 148]）。核心渲染 SVG 单独看不能作为括号形式的依据。

## 6. 几何遮挡审计与补充扫描（全部 0 flags）

- tools/occlusion_audit.py：自检通过（6 类 planted 全部触发，干净对照静默）。
  首轮分版审计 4 flags（见 §11 修复记录），修复并单进程重渲染后
  **终轮：分版 0 flags，核心对照 0 flags，NEW vs 核心 0**。
  结果文件 tools/scratch/occlusion-w45-ru-nl2.json。
  修复轮 FIX1 重测（新几何）：分版 0 flags，核心对照 0 flags，
  NEW vs 核心 0，结果文件 tools/scratch/occlusion-w45-ru-nl-fix1.json。
- **同基线墨迹补充扫描（README #10）：** 按 PIL 真实宽度逐页同基线
  （同 y）相邻文本段间隙扫描，< 5 单位的旗标为 0，包括 P1 顶栏与徽章行。
- **P6 图表逐元素检查（README #12）：** 文本墨迹与后绘矩形的重叠为 0；
  卡片目视确认四条柱标签与数值 34、28、22、16 全部可见，
  与核心一致；RU P6 无冻结压字情形，0 重叠为正常结果。
- P1、P6、P7 卡片经构建员目视抽查；P2–P5、P8 由上述审计与词元对比覆盖。

## 7. P7 读者园地（沿用核心示例 + 披露，无编造）

- 示例信与俄语披露沿用核心原文逐字（示例署名 «— М. (пример от редакции)»，
  经页面拼接文本验证在分版 P7 中完整存在）；未编造任何人名、信件或引言。
- 荷兰语披露行（修复后分版 P7 实测，分三行渲染）：
  «Nog geen echte brieven of beste teksten — redactievoorbeeld; belofte voor VOL.3.
  Stuur je brief en je beste tekst voor VOL.3!»
  三事实原文不动，新增第 3 行为页上显性的公开征集（祈使句，邀来信与
  最佳作文投向 VOL.3）；基线 y=1709.88 / 1738.28 / 1766.68。
- **盒几何（修复后，偏离核心值系设计内后果，已备案）：** 读者园地盒矩形
  (1451, 1254.58, 434 × 502)，盒底 **1756.58**（旧 1727.58，+29 = 恰一
  行披露）；金句区横线 y=**1785**（旧 1756，+29），盒底→横线净空
  仍为 **28.42**；金句标题 y=1823（旧 1794）；末句译文基线 y=2370.67
  （旧 2341.67）；下期预告盒 y=**2433–2551**（旧 2404–2522），页脚线
  2580 余量 **29**；构建日志 «P7 col3 ends 1756.58»。错误诊所盒与词盒
  矩形仍与核心逐值相同（1451 列前两盒：200 + 808.08、1020.08 + 222.5）。
- **盒底接触模式（修复后实测，非旧结论沿用）：** 新增第 3 行基线
  1766.68，位于盒底 1756.58 之下 10.1——与修复前第 2 行的接触量
  （1738.28 对 1727.58，下 10.7）同量级；卡面裁切放大目视三行披露
  全部可读、无溢出、无与金句横线重叠；遮挡审计 0 flags（见 §6）。
  盒底值现偏离核心值 +29，属征集句加行所致，独立复校时须以此
  新几何为准，不得沿用旧的盒底等值结论。

## 8. 词注、金句、图片

- **词注计数（README #21：按 · 本身拆分）：** 核心与分版的 gloss() 调用
  字符串拆分后均为 **26 项**，逐项计数一致；分版 26 项的俄语首词
  在渲染文本中全部存在，无缺失。
- **图片载荷逐字节相同：** P1、P4、P5 图片 href 数据哈希与核心一致
  （P1 299e7e477ee35be9、P4 db6982729417df21、P5 75b89f36224f4ee3，
  前 16 位）；其余页核心与分版均无内嵌图片。
- **P7 金句 8 句：** 俄语原文逐字摘录自本期文章，页面拼接文本中
  每句在核心与分版中均为恰 2 次（源文章 + P7 表）；8 句荷兰语译文
  在分版 P7 中全部存在；页码标签序列与核心一致
  （1、1、2、3、4、5、6、6，俄语 «Страница N» 形式保留）。

## 9. 荷兰语排版与汉字残留

- **行首孤儿标点扫描：** 渲染 SVG 全部文本行中，行首为闭合标点
  （. , ; : ! ? ) % »）的行数为 **0**。
- **渲染 SVG 汉字残留：** 8 页汉字字符数均为 0（freeze.py diff 亦证
  新增汉字字符总数为 0）。俄语正文无汉字；svglib.py 文档字符串内的
  汉字仅存在于源码注释，不进入渲染文本，故不计入。
- 150 题统一编号、分页、分级徽章齐全（§2）；P1 刊头配对徽章与
  每页页脚配对标识齐全（§3）；VOL.2；8 页（4 的倍数）。

## 10. 交付与核心未动证明

- 交付目录 files/weekly-report-w45-ru-nl/：
  svg/ × 8、cards/ × 8（1950×2700 PNG，实测全部 8 张）、
  印刷 PDF Lucerna-VOL2-NL.pdf（13,553,046 字节，8 页）、
  网页 PDF Lucerna-VOL2-NL-web.pdf（3,183,174 字节，8 页，< 10 MB）、
  WEEKLY-KIT.md（本文件）、ABSTRACT.txt（荷兰语单行，294 字符，
  无 ASCII 双引号，含真实主题关键词与学习者搜索短语）。
- PDF 哈希（修复后新值，旧 pins 已失效）：
  印刷版 febfeacfe9c490274cf34ae4e39ef86c274fab2d90bd5c09fd3f407270909339；
  网页版 eea7ce331440820c126ed41f5622fc2e9899846ab2bf04a3d604e9b878c4d067。
  旧 pins：印刷版 13,553,002 字节
  988c306c73f2af2d764fd3b955479e4071e0a15433b184c6115fba8537f6f0ce；
  网页版 3,180,221 字节
  8c19f6603ff7db6db3d7ae0a6b245ce52cc9fe91eb6dd3e62da1126201ac02ba。
- 核心未动：全部工作前后，核心 8 张 SVG 与 2 份 PDF 的哈希值
  与开工前基线（hidden_files/weekly-report-w45-ru-nl-build/core-baseline.txt）
  逐一相同。

## 11. 构建与复现（含修复记录）

- 构建树：hidden_files/weekly-report-w45-ru-nl-build/（核心构建树的
  复制品，重定向后执行；核心构建目录内从未 import 内容模块）。
- 转换脚本：tools/scratch/transform-w45-ru-nl.py（整行与精确唯一
  字面量替换 + 计次断言；值映射用裸文本；无 AST 字节偏移拼接）。
  内容模块共享注册表，故全部渲染均经单进程驱动 run.py
  （content12 → 34 → 56 → 7 → 8），再经 render.py 出卡片与 PDF。
- **首轮审计修复（唯一一次内容返工）：** 首轮遮挡审计 4 flags，
  全部源于三条荷兰语配对说明过长（P2 出页边、P3/P4 与级别徽章
  及题号重叠）。修复：三条说明统一改为与 ru-en 版同款短式
  «Koppel de paren»（5 处，逐文件计次断言），转换脚本同步修正；
  随后单进程重渲染，终轮审计 0 flags，P7 盒底值保持 1727.58 不变。
- 另有两处为保几何而取的短式（均在转换脚本内，附量测依据）：
  P7 词盒行取 «промокод = promocode.»（一行，保盒底值）；
  P7 B1 词行取 «скидка korting; цена prijs; список lijst; ввести промокод invoeren.»
  （两行，与核心行数一致）。
- 自查脚本：hidden_files/weekly-report-w45-ru-nl-build/checks.py
  （只读，从不 import 内容模块），输出存 checks1.log。
- **修复轮 FIX1（2026-10-27，独立校对问题 1，唯一改动）：**
  开工查重：无进行中渲染进程，75 秒复查 files/ 与 build/ 零新写盘
  （mtime 停在 19:45–19:51 UTC），按已完成交付裁定正常开工。
  变换（整行替换 + 计次断言各 1 次，content7.py 三行）：disc_cn 追加
  «Stuur je brief en je beste tekst voor VOL.3!»；fy 1770 → 1799、
  py 2404 → 2433（下游金句区与下期预告盒同步下移 29，保净空与
  页脚余量）。措辞说明：W43 全句（«In VOL.3 echte brieven en de
  beste teksten van pagina 8!»）实测占 2 行新增（披露 2→4 行，+58），
  将把预告盒底推至页脚线 2580，几何上不可行；本句为其紧缩版——
  祈使征集 + 来信与最佳作文 + VOL.3 三要素齐全，实测恰 1 行新增。
  三事实原文、示例信署名、冻结俄语披露、下期预告俄语原文一律未动，
  未编造人名/信件/引言。单进程重渲染 run.py → render.py（render 须
  用 tools/venv/bin/python，系统 python3 缺 cairosvg）；构建日志
  run-fix1.log / render-fix1.log，自查 checks-fix1.log。
  重测门：遮挡审计分版 0 / 核心 0 / NEW 0；p8.py compare CLEAN
  150=150，keydiff 仍 [83, 137, 138, 148]；注册表 150（A2 51 / B1 75 /
  B2 24，分页 10/18/18/18/18/18/12/38）；P7 外各页 SVG 与卡片逐字节
  同修复前（仅 p7-yazyk.svg 与 p7-yazyk.png 变化）；P7 西里尔词元
  397=397 diff={}；核心 8 SVG + 2 PDF 哈希与基线逐一相同；
  P7 卡面目视三行披露全部可读。审计产物
  tools/scratch/occlusion-w45-ru-nl-fix1.json、
  tools/scratch/p8-w45-ru-nl-fix1.json。

## 12. 交独立校对的已知事项

- 本版为修复轮完成、独立复校待定；定稿须另派独立全量复校
  （SOP §8.4），复校重点建议：P7 新征集句与新几何（盒底 1756.58、
  金句横线 1785、预告盒 2433–2551、页脚余量 29）、荷兰语讲解通顺度、
  P8 翻译题重瞄准（137、138）、以及 P2–P5、P8 的卡片目视。
- §7 的盒底值已由修复轮 FIX1 改为 1756.58（偏离核心 +29），旧的
  “与核心逐值相同”结论不再适用；独立复校须以 §7 新几何为准。
- 未发 Discord、未往主聊天发卡片或 PDF、未建 cron、未碰 weekly-git、
  未做 repo 插入；插入与投递由主线另行安排。
