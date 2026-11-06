# WEEKLY-KIT — Die Lucerna VOL.2 · DE × NL（德语正文 + 荷兰语讲解）

配对：目标语 Deutsch × 读者母语 Nederlands。由 W45 德语核心版
（files/weekly-report-w45-de-core/，Die Lucerna VOL.2，已定稿上架）扇出，
仅重写讲解层为直接写给荷兰语母语读者的荷文；德语正文、图片、版式几何全部冻结。
Issue week: **Mon 2 – Sun 8 November 2026**。8 页，1950×2700。

状态：**builder-complete，未定稿，待独立校对**。未发 Discord、未往主聊天发
卡片/PDF、未建 cron、未碰 weekly-git、未改核心目录与 W43 目录。

## 1. 总量

- 习题 **150**，连续编号 1–150；逐页 10/18/18/18/18/18/12/38，与核心一致。
- 级别 **A2 66 · B1 70 · B2 14**，与核心一致。B2 仅 14 属实（B2 负荷在 P6 + P7），
  未为凑数重定级，如实记录。
- 题型（荷兰语登记名 ← 核心中文名）：meerkeuze 52 ← 单选 · invullen 41 ← 完成句子 ·
  omvormen 11 ← 句型转换 · koppelen 12 ← 词汇配对 · juist/onjuist 8 ← 判断对错 ·
  gatentekst 8 ← 完形填空 · zinnen bouwen 8 ← 造句 · dialoog aanvullen 5 ← 对话补全 ·
  vertalen 4 ← 翻译 · schrijven 1 ← 写作 = 150。
- 指令词（W43 NL 实测形式）：Vul in · Herschrijf · Beoordeel · Vorm de zin ·
  Vertaal naar het Nederlands / Vertaal naar het Duits · Combineer。

## 2. 基线（tools/freeze.py baseline，逐字节复现验证）

- 开工前核心哈希登记（8 页，见 §12 针脚对照）；构建树复制核心 build 后未修改运行：
  `freeze.py baseline --build hidden_files/weekly-report-w45-de-nl-build
  --core-svg files/weekly-report-w45-de-core/svg` → **8/8 SVG 与已发布核心逐字节一致**。
- 收尾复核：核心 8 页哈希与开工前逐字节相同（CORE UNCHANGED，diff 为空），
  核心文件未被触碰。构建全程未在核心构建目录内 import 内容模块；
  寄存器转储（dump_reg.py）为单进程重跑，输出与交付 SVG 逐字节一致。

## 3. 冻结对照（tools/freeze.py diff，终版）

- added CJK = **0**（8 页全部：P1 168→0、P2 186→0、P3 187→0、P4 155→0、
  P5 193→0、P6 228→0、P7 394→0、P8 1429→0；终版 SVG 零汉字）。
- P1–P7 删除串分类完毕（终版 freeze-diff JSON：
  tools/scratch/w45-de-nl-freezediff-final.json）：
  - 唯一整段删除的德语串是 P1 tagline
    «DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND»
    （徽章按 DE 家族惯例占 tagline 槽，家具替换；W43 同配对先例相同）。
  - P7 读者框标签 «Ein Beispiel der Redaktion!» → 荷文标签（EN 同族先例相同）。
  - P7 NOCH EIN WORT 框定义句 «die gesenkte Steuer auf Benzin und Diesel»
    → 修复轮已恢复德语原句（见 §17）；荷兰语 gloss «Brandstofkorting.» 保留，
    该行对应核心第三行讲解层；DE×EN 同族版亦逐字保留德语句。
  - 其余删除串全部含中文（讲解层）或为绕排碎片（双语串换行切分、
    P7 省略号碎片 ……）；无德语正文句子丢失。
- P8 删除串：中文讲解层 + 全角括号绕排碎片（核心全角括号 → 本版半角括号后
  键行重绕排所致，见 §4）；无德语测验正文丢失。
- 新增串（P1–P7）全部为荷文讲解、家具，或双语 gloss 串内的德语词头
  （如 «Uitleg — der Tankrabatt =»）；无新增德语正文句子。
- 图片：P1/P4 内嵌图片数据与核心逐字节相同（哈希一致）。

## 4. 印刷注释门（tools/p8.py compare）

```
core    ../files/weekly-report-w45-de-core/svg/p8-uebungen.svg: 150 noted
edition ../files/weekly-report-w45-de-nl/svg/p8-uebungen.svg: 150 noted
status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]
```

- 核心印全 150 条注释，本版集合 {1..150} 与核心 **EQUAL**。
- keydiff 逐项判定（全部为合法重定向，无工具伪影）：
  - **137**（译德→荷）键改为荷兰语译文：«De brandstofkorting loopt tot december.»
    注释 «(laufen = duren)»；题干方向标注 «Vertaal naar het Nederlands»。
  - **138**（译德→荷）键改为荷兰语译文：«Ik kijk op dinsdag voetbal.»
    注释 «(schauen = kijken)»；题干方向标注 «Vertaal naar het Nederlands»。
  - **139**（译德→荷）键改为荷兰语译文：«De school is weer begonnen.»
    注释 «(wieder begonnen = weer begonnen)»；题干方向标注 «Vertaal naar het Nederlands»。
  - **150**（写作开放题 apparatus）键改为荷兰语：
    «Open opdracht — zie de punten in het schrijfblok; de voorbeeldtekst staat
    in het schrijfblok op deze pagina»，注释 «(Beoordeling op basis van de punten)»；
    P8 写作区指令与清单同步荷兰语化。
  - **140**（译荷→德）不在 keydiff 内，属正确：键保持德语不变
    «Am Sonntag schlafe ich eine Stunde länger.»，题干改为荷兰语原句
    «Ik slaap op zondag een uur langer.»（instr «Vertaal naar het Duits»），
    注释改为荷兰语短语在前
    «(een uur langer slapen = eine Stunde länger schlafen)»；p8.py 只比对键，
    故注释重定向不列入 keydiff，已逐字核实实印。
- P8 答案格式：W43 DE×NL 已发形式，`N. key (note)` 空格 + 半角括号、
  ` · ` 连接，键字号 13pt/1.3；分隔符 «— Pagina N —» ×8（N=1..8）。
- P8 括号形式以本族已发分版构建码为准（README #14）：核心全角括号为
  中文讲解路径，六个已发 DE 扇出均改半角；本版构建码改动点与 W43 DE×NL 一致。
- 可疑处先怀疑工具提取伪影（README #13）：本版 keydiff 经实印逐项复核，
  无括号/dash 提取类伪影；dash 式键行均与寄存器一致。

## 5. 几何审计（tools/occlusion_audit.py，自检先行）

- 终跑：**edition 0 flags；core 0 flags；NEW vs core 0**。
  （初跑 16 个 NEW flags，全部修复，见 §13。）
- P6 图表墨迹 vs 后绘矩形（DE×RU 盲区类，单列核查）：
  荷文标签墨迹右端 vs 条形起点 x=535：familiezorg 528.8（间隙 6.2px）·
  thuiszorg 511.9（间隙 23.1px）· zorghuis 504.4（间隙 30.6px），重叠 **0**。
  初版 thuiszorgdienst/verzorgingshuis 尾字曾被条形盖住（间隙 −34.3/−36.8px），
  已缩短并同步图表题答案注释（W43 DE×NL P6 先例：标签缩短后注释同步）。
- P1 顶带同基线间距扫描（FR×RU 教训，README #10）：y=92 三段（左/中/右）、
  y=478、y=522、页脚 y=2624 四组同基线文本，墨迹间距全部为正，无重叠。
- P1–P8 各页框底 vs 金线核查：P2 框底 1550.66 vs 金线 1554（间隙 3.34px，
  与核心完全相同）；P3 框底 1583.66 vs 金线 1608（间隙 24.34px，与核心相同）；
  P4 1164.25 vs 1628；P5 1386.54 vs 1488；P6 1320.33 vs 图表金线 1408；P7 1504.5。

## 6. gloss 计数（README #21：按 · 本身拆分）

- gloss() 调用串逐项计数，核心与本版 **1:1，不得增删合并**：
  P2 5 · P3 5 · P4 5 · P5 5 · P6 5 = 25 项，逐项对应。
- gloss 前缀 «Uitleg — »：P1–P6 各 1 处（与 W43 DE×NL 登记一致）。

## 7. P7 金句（VERBATIM contiguous excerpts）

- 8 条德语引文全部为本期文章原文逐字摘句，全刊出现次数核心与本版均为
  **2, 2, 2, 2, 2, 2, 2, 2**（源文章 1 次 + P7 表 1 次）。
- 页码标签分布如实记录：Seite 4 · B1、Seite 2 · A2、Seite 2 · A2、
  Seite 5 · B1、Seite 3 · A2、Seite 4 · B1、Seite 6 · B2、Seite 6 · B2。
- 第 7 条荷文译文为 2 行版（«De economie komt langzaam uit de stagnatie,
  maar het herstel draagt zichzelf nog niet.»），标签不顶诊所金线；
  译文删 «Duitse» 一词（引文与上下文已明示德国），其余 7 条译文与核心逐条对应。

## 8. 家具三方对照（本版／W43 已发同配对／README #20）

- 家族情形：DE 核心有原生副题槽 y≈372 → 徽章原位替换（README #20 的
  EN/DE/ES 情形）。#20 泛化值 19.5pt 与 W43 已发同配对实测 20pt 不一致时，
  **W43 已发同配对 SVG 逐字胜出**：本版徽章节点属性与 W43 DE×NL P1 实测
  逐字相同——x=975 y=372、Noto Sans CJK SC、20pt、bold、fill #a4553a
  （BRICK）、居中；字符串逐字相同：
  «TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS»。
- 副题（W43 形式，VOL.2）：«DUITS WEEKBLAD · VOL.2 · VOETBALWEEK ·
  BRANDSTOFKORTING · ZORG»（形容词不变格 «DUITS WEEKBLAD»，同 EN×NL/FR×NL）。
- 顶带 strap（W43 逐字）：«WÖCHENTLICH AUF DEUTSCH · ELKE WEEK ·
  HET DUITS DAT DE DUITSERS LEZEN»。
- 页脚（8 页逐页程序化核对）：«Die Lucerna · DUITS WEEKBLAD VOL.2 ·
  TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS»／«Pagina N van 8»。
- 刊名：masthead 用核心的 **Die Lucerna**（目标语为德语），8 页齐全。
- 工具箱标题取 W43 NL 已发短式：«DER WERKZEUGKASTEN · Op zak»。
- P8 题头短式取 W43 NL 已发：«B · WISSENSFRAGEN · Kennis»、
  «C · LESEVERSTEHEN · Lezen»。
- 未为凑 #20 泛化描述改动或删除任何冻结德语行。

## 9. 读者园地（P7 LESERBRIEFE · Lezersbrieven，强制项）

- 标签（编辑部示例标注）：«Een voorbeeld van de redactie!»。
- 德语冻结行原样保留：defer «Bis Redaktionsschluss keine Briefe oder Texte —
  sie erscheinen in VOL.3.»、示例信正文、德语征集句（冻结德语，不计入荷文征集）。
- 荷文事实句（note_nl，实印逐字）：
  «Geen echte brief: nog geen brieven of beste pagina-8-tekst; belofte naar VOL.3.»
  三事实映射：示例身份由标签句承担（编辑部示例，非真实来信）；
  无真实来信 = «nog geen brieven»；无最佳 P8 习作 = «geen beste pagina-8-tekst»；
  承诺顺延 VOL.3 = «belofte naar VOL.3»。
- 荷文显性公开征集句（invite_nl，实印逐字，本版计入的唯一征集句）：
  «Schrijf ons! Stuur je echte brieven in!»
- 内容预告栏（IN DER NÄCHSTEN AUSGABE）的德语 «Schreiben Sie uns!» 句与
  各页 UND SIE? 投稿提示均**不算**征集（按任务口径）；本版征集成立不依赖它们。
- 无编造读者来信／人名／引言：示例信为核心冻结的编辑部示例，标签明示。

## 10. 渲染与版本（工具链裁定执行记录）

- run.py：构建员自选解释器，**交付 SVG 本身为准**。
  实际使用：系统 python3 3.12.3 + PIL 10.2.0（主渲染），以及
  tools/venv/bin/python 3.12.3 + PIL 13.0.0（复核重跑）——两路输出
  **8/8 逐字节相同**；基线复现（§2）为 venv 路径 8/8。
- render.py（cairosvg，必须用 venv，系统 python3 缺 cairosvg）：
  tools/venv/bin/python 3.12.3 + PIL 13.0.0 + cairosvg 2.9.1 + pypdf 6.21.2；
  卡片 PNG 1950px、印刷 PDF 向量、网页 PDF JPEG q85 @1400px。修复轮：run.py 与 render.py 均用 tools/venv/bin/python 3.12.3 + PIL 13.0.0（render.py 另 + cairosvg 2.9.1 + pypdf 6.21.2），单进程重渲染（见 §17）。
- KIT §5 度量（occlusion 审计）用 venv PIL；run.py 内 wrap 换行决策不受
  该约束（按协调员裁定），且双解释器输出一致已证实无版本敏感差异。
- 单进程重渲染：全程经 build 目录 run.py 一次进程跑 content12→34→56→7→8
  （共享 REG 注册表，README #7）；无分段重渲染。
- 变换规则：整行或精确唯一字面量＋计次断言（transform.py，393 处替换）；
  值映射（题型／指令）用裸文本，无 repr 泄漏（README #17–#18）。

## 11. PDF 针脚（终版）

- 印刷版 Die-Lucerna-VOL2-NL.pdf：**4,138,969 B**，8 页，
  1462.5×2025 pt（与核心印刷版页尺寸一致），sha256
  bbd0f30b0ae2a944f635704a734a5530e474dff6d004824966642df05e695555。
  （注：核心印刷版 17,030,165 B 为另一配方；本版与 W45 DE×EN 同族
  render.py 配方，EN 印刷版 4,137,635 B，量级一致。）
- 网页版 Die-Lucerna-VOL2-NL-web.pdf：**4,140,002 B**（< 10 MB ✓），8 页，
  1400×1938 pt，sha256
  7a667deaa87616730ff720d3265e7f45d7375d8d0fe771cd41ac237820ec01ac。
- SVG 针脚：p1 42ba63f4…、p2 da08a038…、p3 9da2e711…、p4 452c69e9…、
  p5 b034ba99…、p6 18d2c3c3…、p7 95dfd5fd…、p8 ee928685…（完整哈希见交付目录实测）。
- 卡片 1950×2700 PNG ×8（p1–p8），哈希与交付实测一致。

## 12. 自修复清单（构建轮内全部修复，终版零残留）

1. P1-headline 流溢出（+93px）：桥接句删 trivial 的 Bundesliga 同义项、
   Zahlen 三行括号注缩短 → 零 OVERFLOW（P1-fussball/P1-quiz 的 8/12px
   超底与核心/EN 完全相同，系固定位流继承，非本版缺陷）。
2. P8 题头超宽：«Kennisvragen»→«Kennis»、《Leesvaardigheid»→«Lezen»
   （W43 NL 已发短式）→ 零 TOO WIDE。
3. 初版 occlusion 16 NEW flags：P1 Zahlen 标题越框→«Cijfers»；
   Fragen 副题越框→«Vijf veelbesproken vragen.»；P6 免责声明出页→
   «(Oefencijfers, geen echte enquête.)»；P7 工具箱标题越框→«Op zak»；
   P7 金句头右锚越界→«Woord voor woord uit dit nummer»；
   金句 7 译文 3 行顶诊所金线→ 2 行版；其余 9 旗均为 P7 右栏超高连锁，
   由读者框＋工具箱裁剪根治（见 4）。
4. P7 右栏超高 231.5px（col3 终点 1736→1504.5，与 EN 版持平）：
   工具箱 4 项缩至单行（删 «bespaard»/«(passief)»/«Het is de vraag of ...»
   的冗长尾巴，德语词头不动）；note_nl 5 行→2 行、invite_nl 3 行→1 行；
   rh 公式残留续行清理（transform 首行替换遗留，EN 版同款手工修正），
   常数取 EN 先例 +32（6 段结构相同）。
5. P6 图表 GRAZE（审计盲区，像素/墨迹核查发现）：thuiszorgdienst/
   verzorgingshuis 尾字被条形盖住 → thuiszorg/zorghuis，图表题答案注释同步；
   familiezorg 间隙 6.2px 保留（零重叠，审计 0 旗）。
6. P3 TIPP 框底越练习区金线 4.66px（框底 1612.66 vs 金线 1608）：
   UND SIE? 荷文提示 3 行→2 行（«Lees je in de herfst meer? Welk boek ligt
   naast je bed? Schrijf twee Duitse zinnen!»），框底复归核心值 1583.66。
7. P7 NOCH EIN WORT 定义句荷文化（原登记有误，见 §17 修复轮：已恢复德语句）；
   P3/P4/P6 孤字 «。」绕排碎片随双语串重绕消失，终版冻结分类无此项。

## 13. 新增讲解语言外字符备案

- 新增码点仅 3 个，均为荷文单词内字母：q（Bliksemquiz）、ê（enquête）、
  ó（vóór）。无新增字形类别；核心已有的 é（Atlético）与本版一致（预组合）。
- 丢失字符：496 个中文字符（讲解层替换，预期）+ «Y»（仅旧页脚
  «LUCERNA GERMAN WEEKLY»）+ «…»（中文省略号 → 荷文 ...）。
- 术语口径：交付 SVG 中『桥接』出现 0 次；本 KIT 元语言提及 2 次（第 185、216 行），均指已删除的旧表述，不作交付用语。构建码（*.py）中该中文词出现 0 次。

## 14. 目视检查（8 张卡面全部目视）

- P1：徽章/副题/顶带/头条/数字框/Fragen 框/照片/quiz 全部干净。
- P2：UND SIE? 框、RECHNEN 宽框、gloss 框、练习区全部干净。
- P3：TIPP 框修后与练习区金线间隙正常；其余干净。
- P4：赛程表、UND SIE? 框、练习区干净。
- P5：周计划宽框、UND SIE? 框、练习区干净。
- P6：图表三标签全部脱离条形；免责声明单行入页；练习区干净。
- P7：读者框 6 段全部入框；词框、金句格、诊所、预告干净。
- P8：测验区、写作框＋范文、全部答案键干净；E 区方向标注正确。

## 15. 交付目录

- files/weekly-report-w45-de-nl/svg/ ×8、cards/ ×8、
  Die-Lucerna-VOL2-NL.pdf、Die-Lucerna-VOL2-NL-web.pdf、
  WEEKLY-KIT.md（本文件）、ABSTRACT.txt。
- 构建树：hidden_files/weekly-report-w45-de-nl-build/
  （transform.py、run.py、render.py、content*.py、bslib4.py、svglib.py、
  build-log.txt、reg-dump.json、syspy-svgs/ 对照）。

## 16. 校对状态

- 建造者全量自校：完成（冻结三门工具复跑 + gloss/P7/级别/图表/家具
  程序化核对 + 8 卡目视 + 自修复 7 项）。
- **独立校对：未进行。状态为 builder-complete，未定稿，待独立校对。**

- **修复轮（2026-10-27，见 §17）：独立校对阻塞问题 1 已修复并重渲染、全部守门重跑；状态仍为未定稿，须按 SOP §8.4 另派独立全量复校后方可定稿。**

## 17. 修复轮记录（2026-10-27，独立校对问题 1，单项纸面改动）

- 阻塞：P7 NOCH EIN WORT 框德语定义句被改写为荷兰语（校对报告
  hidden_files/w45/de-nl-proof/REPORT.md 问题 1，门 1 冻结失败）。
  所引 DE×EN 先例不实：DE×EN、DE×ES、DE×IT 均逐字保留德语句；
  DE×FR、DE×PT 同样本地化但均为未定稿 builder-complete，不能作放行先例。
- 改动（仅 P7 该框 3 行，源文件 content7.py 第 106 行 + transform.py
  第 327–328 行映射同步修正，其余源文件未动）：
  - 改前：`«der Tankrabatt» (pagina 2): de` / `verlaagde belasting op benzine en` /
    `diesel. Brandstofkorting.`
  - 改后：`«der Tankrabatt» (Seite 2): die` / `gesenkte Steuer auf Benzin und Diesel.` /
    `Brandstofkorting.`——德语定义句按核心/EN 版两行排布恢复（第 1 行页标亦随
    冻结德语句恢复为 (Seite 2)，与 EN 版逐字相同；EN 版第 3 行为 `Fuel discount.`，
    本版第 3 行荷兰语 gloss `Brandstofkorting.` 保留，对应核心第三行讲解层）。
- 几何（改后实测，与改前逐值相同）：框 rect x=1451 y=1354.5 w=434 h=150，
  底 1504.5；3 行基线 y=1432.5 / 1461.61 / 1490.72（与 EN 版同坐标）；
  金句区横线 y=1508，框底低于横线 3.5px；读者框底 1338.5，距词框顶 16px。
- 改动范围（修复前基线哈希见构建树 fix-round-baseline-hashes.txt；P7
  修复前 SVG 副本见构建树 p7-sprache.PRE-FIX.svg）：
  SVG 仅 P7 变化（5700fb81… → 95dfd5fd…），P1–P6、P8 逐字节一致；
  卡片仅 P7 变化（afc348d3… → 77e87032…），其余 7 张逐字节一致；
  双 PDF 因内嵌 P7 而变化（属预期）；P7 文本元素数 188 = 188，仅该框 3 行有变。
- 工具链（本轮）：run.py 与 render.py 均用 tools/venv/bin/python 3.12.3 +
  PIL 13.0.0；render.py 另 + cairosvg 2.9.1 + pypdf 6.21.2。
  单进程重渲染：build 目录 run.py 一次进程跑 content12→34→56→7→8
  （P7 col3 ends 1504.5，总题 150），再经 render.py 出卡片与双 PDF。
- 守门重跑（全部输出见构建树 fix-round-gates.txt）：
  冻结核心基线 8/8；冻结差分新增 CJK 0（P1 168→0、P2 186→0、P3 187→0、
  P4 155→0、P5 193→0、P6 228→0、P7 394→0、P8 1429→0）；
  P7 纯拉丁删除串仅剩家具（P1 副题槽、P7 读者框标签、中文省略号碎片，
  及全角括号改半角后的绕排碎片）；德语句第 2 行与核心逐字节相同、
  未被删除，第 1 行与核心仅差全角/半角括号（与 EN 版相同）；
  p8.py compare CLEAN 150=150，keydiff=[137, 138, 139, 150]；
  occlusion 自检 6 类全触发，分版 0 flags、核心 0 flags、NEW vs core 0；
  gloss 5 处调用 × 5 项 = 25 = 25（P2–P6，见 §6 订正后页码）；
  P7 金句 8 句全刊出现次数核心与本版均为 2, 2, 2, 2, 2, 2, 2, 2；
  8 张卡面全部目视（P7 词框、金句格、诊所、预告干净；P6 图表三标签
  familiezorg / thuiszorg / zorghuis 全部脱离条形；其余各页无重叠、无截断）。
- PDF 针脚（改后）：印刷版 4,138,969 B、8 页、1462.5×2025 pt，
  sha256 bbd0f30b0ae2a944f635704a734a5530e474dff6d004824966642df05e695555；
  网页版 4,140,002 B（< 10 MB）、8 页、1400×1938 pt，
  sha256 7a667deaa87616730ff720d3265e7f45d7375d8d0fe771cd41ac237820ec01ac。
- KIT 文字订正（本轮一并改，无需重渲染）：§6 gloss 页码笔误“P1 5”→“P2 5”；
  §13 术语口径修正为交付 SVG 中 0 次、KIT 元语言提及 2 次（第 185、216 行）。
- 状态：**未定稿**。按 SOP §8.4，渲染变化后须另派独立全量复校；本轮不宣称定稿。
