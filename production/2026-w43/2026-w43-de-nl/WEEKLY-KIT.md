# Die Lucerna VOL.1 — DE × NL（德语正文 + 荷兰语讲解）

配对：目标语 Deutsch × 读者母语 Nederlands。由德语核心版（files/weekly-report-de-vol1/）扇出，
仅重写讲解层；德语正文、图片、版式几何全部冻结。

## 基线（freeze.py）
- 核心 build 复制到 hidden_files/weekly-report-de-nl-build/ 后未修改运行：
  tools/freeze.py baseline → **8/8 SVG 与已发布核心逐字节一致**
  （p1 be1b0f7b…、p2 cac83eb5…、p3 d862d862…、p4 591eaa94…、p5 b48ed810…、
  p6 a69b6fee…、p7 b4f74e08…、p8 8fb288ff…）。
- 收尾复跑 baseline 再次 8/8 一致，核心文件未被触碰。

## 总量
- 习题 **150**（A2 67 · B1 69 · B2 14），与核心一致；逐页分布与核心相同。
- P7 本周句子：8 条引文与核心逐字节相同、来源标签相同、全文出现次数与核心逐条相等
  （2,2,2,2,2,2,3,2；计数程序化核验）。
- 日历核验（Europe/Berlin）：2026-10-24 周六（图书馆日）、10-25 周日（换冬令时
  03:00→02:00）、10-31 周六、11-01 周日、2027-03-28 周日（冬令时结束）——与版面一致。

## 答案键差异登记（key-diff registry，p8.py compare 实测 keydiff=[137, 138, 150]）
德国家庭含翻译题，差异仅限以下条目，其余 147 条键与核心逐字节相同：
- **137**（译德→荷）键改为荷兰语译文：«Deze nacht heeft 25 uur.»
  注释 «(Stunden = uren)»（核心 «Stunden = 小时» 对应荷兰语化）；题干加方向标注（见下）。
- **138**（译德→荷）键改为荷兰语译文：«Ik verzet de klok op zaterdagavond.»
  注释 «(umstellen = de klok verzetten)»（核心 «umstellen = 拨（钟）» 对应荷兰语化）。
- **139 / 140**（译荷→德）题干改为荷兰语原句，**德语键不变**：
  139 题干 «Ik slaap op zondag een uur langer.»，注释改为荷兰语短语在前
  «(een uur langer slapen = eine Stunde länger schlafen)»（核心 «多睡一小时 = eine Stunde
  länger schlafen»）；140 题干 «In de bibliotheek kun je boeken lenen.»
- **150**（写作开放题 apparatus）键改为荷兰语：
  «Open opdracht — punten in het schrijfblok; de modeltekst staat in het modelblok op deze pagina»，
  注释 «(Beoordeling op basis van de punten)»；P8 写作区指令与清单同步荷兰语化。
- 呈现微调（不改键）：137–140 的翻译方向从题干括号内移到题头 instr 标签
  （«Vertaal naar het Nederlands» / «Vertaal naar het Duits»），因荷兰语括号注会使
  P8 测验区溢出栏底（实测 +4 行 ≈ +113px，栏底 1505、内容冲至 1610）；移动后栏内结束 1494。

## 家具（verbatim，与 tables.json NL 列 + EN×NL/FR×NL 已发版式一致）
- P1 strap：«WÖCHENTLICH AUF DEUTSCH · ELKE WEEK · HET DUITS DAT DE DUITSERS LEZEN»
- P1 46pt 副题：«DUITS WEEKBLAD · VOL.1 · KLOK · VAKANTIE · VORST»
- P1 配对徽章（核心无 badge 元素，按 DE 家族惯例置于 tagline 槽 y=372，20pt sans bold 砖红居中）：
  «TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS»
- 时钟带右行：«Zondag gaat de klok terug» / «De nacht van 25 uur · zie pagina 2»
- 页脚左：«Die Lucerna · DUITS WEEKBLAD VOL.1 · TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS»
  （形容词不变格 «DUITS WEEKBLAD»，同 EN×NL/FR×NL）；页脚右：«Pagina N van 8»
- 注释前缀：«Uitleg — »；P8 分隔符：«— Pagina N —»
- P8 答案格式：`N. key (note)` 空格 + 半角括号、` · ` 连接（DE 扇出惯例；
  核心本体为全角括号，×DE 已发各版均为此式）。
- 指令词：Vul in · Herschrijf · Combineer · Corrigeer · Beoordeel · Vorm de zin。
- 刊名 Die Lucerna 与核心一致。

## 印刷注释门（tools/p8.py compare 实跑输出）
```
core    ../files/weekly-report-de-vol1/svg/p8-uebungen.svg: 150 noted
edition ../files/weekly-report-de-nl/svg/p8-uebungen.svg: 150 noted
status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 150]
```
核心印全 150 条注释，本版集合 {1..150} 与核心 **EQUAL**。

## 几何审计（tools/occlusion_audit.py，自检先行）
- 初跑 13 个 NEW flags，全为荷兰语单行文本过长（见缺陷表），逐项缩短措辞修复。
- 终跑：**edition 0 flags；core 1 flag（核心自有）；NEW vs core: 0**。
  存档：tools/scratch/de-nl-audit-final.json。
- freeze.py diff：8 页 added CJK = 0，终版 SVG 零汉字；全部差异归类为讲解层。

## 缺陷与修复（建造者全量自校，8 页逐页看渲染图）
1. 审计 13 flags：P1 时钟带右行与德语标题墨迹相交 → 缩为 «Zondag gaat de klok terug»；
   P1 数字框标题越框 → «· In cijfers»；P1 Fragen 框副题/底行出页 → 缩短；
   P1 目录框标题越框 → «· Inhoud»；P6 健康框荷兰段压图表线 → 缩短至 4 行；
   P6 图表免责声明出页 → 荷括号注缩短；P7 工具箱标题出页 → «· Op zak»（同 FR×NL 解法）；
   P7 短语 3 译文 4 行致标签撞下一行引文 → 译文缩至 2 行（凝练 gloss，已登记）。
2. **审计漏检、像素裁定**：P2 «UND SIE?» 框荷兰段末行被时钟带顶线（y=1558）穿过
   （框底 1577.75 越线；SVG 实测末行基线 1572.13）→ 荷兰段缩至 3 行，框底 1548.75 < 1558 ✓。
3. P7 «NOCH EIN WORT» 框：德荷同段合计 4 行、末行基线 1471.33 在框底 1456 之外 →
   荷兰 gloss 缩为 «Duitse voetbal-klassieker.»，末行基线 1442.22，入框 ✓。
4. P6 图表第二条荷兰标签 «tijd met het gezin» 尾字被条形盖住（条始 x=570）→
   缩为 «tijd met gezin»（答案 #86 注释同步用 gezin）。
5. P2 B 区指令 «Zet de zinnen in het Perfekt (de voltooide tijd).» 在栏底断行难看 →
   缩为 «Zet de zinnen in het Perfekt.»（Perfekt 构成在 P8 注释 #16–20 有荷兰语讲解）。
6. 版面留白/溢出类：P1 头条流、P6/P7/P8 各流初跑溢出，均以缩短荷兰措辞解决，
   终跑 run.py 零 OVERFLOW / 零 TOO WIDE（P8 键字号按 zh-TW×PT 先例收紧至 13.0/1.16）。
7. 已知核心冻结现象（非本版缺陷，不改）：P8 F 区选项 a 德语文本尾端抵页框——
   与核心卡片同区域裁图 **sha256 完全相同**（dd13ee46…），系核心自有几何。
8. 中间层术语：paper/KIT/operative code 中 0 出现；核心的讲解方法已改名 `expl()`。
   唯一例外：scratch/transform.py 中 1 处以核心原调用串作搜索模式（按既定披露惯例）。

## 图片与授权（承核心 KIT，均为 public domain，署名行照核心印于版面）
- P1 frost.jpg — Courtney Celley, U.S. Fish and Wildlife Service — public domain
- P2 atomuhr.jpg — NIST — public domain
- P3 luther.jpg — Lucas Cranach d.Ä., 1528 (Veste Coburg) — public domain
- P5 kuerbis.jpg — U.S. Department of Agriculture — public domain

## PDF 针脚（终版）
- 网页版 2026-w43-de-nl.web.pdf：**1,461,565 B**，sha256
  8b97b3c9b30a07164ad1419b1b7f53f5e2b8cf130b07a04fcbc0537a77a08eb2（< 7 MB ✓；D5 重建，2026-11-13；旧配方值 4,257,170 B 已过期，见末节 D5 记录）
- 印刷版 The-Lucerna-VOL1-de-nl.pdf：9,349,638 B，sha256
  e578f25e9d0473c513013ae53e7a08e882b4c5529182fd75dac3dbbc659f691a（D5 重建，2026-11-13；旧配方值 10,478,874 B 已过期，见末节 D5 记录）

## 校对状态
- 建造者全量自校：完成（逐页读图 + 150 键对核心程序化比对 + 短语/日历核验 + 三门工具复跑）。
- **独立校对：PASS**（2026-10-21，完整一轮零问题；记录见下节）。

## 独立校对记录（2026-10-21）
- **工具三门（独立实跑）**：freeze.py baseline 8/8 逐字节复现核心（哈希与本 KIT 登记一致，
  核心完整性复核无损）；freeze.py diff 全 8 页 added CJK = 0，全部删除串分类完毕——
  唯一整段删除的德语串是 P1 tagline（徽章按 NL 列惯例占 tagline 槽，家具替换），
  其余为中文讲解层、P7 全/半角括号重排片段与 P8 答案行绕排片段，无未登记正文丢失；
  p8.py compare **CLEAN 150 = 150，keydiff=[137, 138, 150]**；occlusion_audit.py
  （自检先行）edition **0 flags**、core 1 flag、NEW vs core 0——核心那 1 个 flag 为核心自有
  P1 Fragen 框中德标题 BOXTITLE（右墨迹 1904.2 > 框 1885），本版荷兰标题已缩短，未继承。
- **寄存器独立转储**（两版 build 复制到 scratch 改道输出、一进程重跑）：150 = 150，
  A2 67 · B1 69 · B2 14、逐页分布（10/18/18/18/18/18/12/38）两版全同；键差异恰为
  {137, 138, 150}；印刷键（p8.py extract）与寄存器 150/150 吻合、版间印刷键差异同为
  {137, 138, 150}。scratch 重建 SVG 与交付版 8/8 逐字节一致、零 OVERFLOW/TOO WIDE。
- **150 键手工重推导**：逐页通读德语正文与题干，150 键全部从正文独立推出并与寄存器
  一致（含 P6 图表算术 46+18=64、46+22+18+14=100、Familie+Lesen 40 > Sport 14；
  P8 Muster 模型文实数 87 词 = 版面所标 «87 woorden»）。
  137/138 荷兰译文、139/140 荷兰题干+德语键、150 apparatus 均与版面实印一致
  （实印：137 «Deze nacht heeft 25 uur. (Stunden = uren)»、138 «Ik verzet de klok op
  zaterdagavond. (umstellen = de klok verzetten)»、139 注释 «(een uur langer slapen =
  eine Stunde länger schlafen)»）。呈现微调实测复核：方向标注已移至题头 instr
  （137/138 «Vertaal naar het Nederlands»、139/140 «Vertaal naar het Duits» 在版面题干上方），
  P8-battery 流实测结束 y=1494 ≤ 栏底 1505 ✓。
- **日历**：程序化核对 Europe/Berlin——10-19 周一（霜夜周一→周二）、10-23 周五、10-24 周六
  （图书馆日）、10-25 周日 03:00→02:00 换冬令时、10-26 周一、10-31 周六、11-01 周日、
  2027-03-28 周日（冬令时结束）全部与版面一致。
- **P7**：8 条引文与页标签在两版 content7.py 源码层逐字节相同；全刊出现次数逐条两版相等
  （原始计数 2,2,2,2,2,2,3,2——第 7 条 P2 出现 2 次 + P7 1 次，两版同为 3）。
- **家具**：8 页页脚 «Die Lucerna · DUITS WEEKBLAD VOL.1 · TEKSTEN IN HET DUITS ·
  UITLEG IN HET NEDERLANDS» / «Pagina N van 8» 逐页程序化核对 OK；P1 徽章、strap、副题
  «DUITS WEEKBLAD»（不变格）与 KIT 登记逐字一致；«Uitleg — » 前缀 P1–P6 各 1 处；
  P8 分隔符 «— Pagina N —» ×8、键式 `N. key (note)` 半角括号 ✓。
- **几何（墨迹口径，PIL 实测）**：P1 时钟带标题墨迹止于 1501.8、荷兰右行墨迹起于 1548.1
  （间隙 46.3）；数字框标题墨迹右端 929.8、目录框标题 1826.2 < 1885、Fragen 框副题 1693.8 /
  末行 1840.2 < 1885；P2 UND SIE 框底 1548.75（与建造者登记一致）、荷兰段 3 行末行基线
  1543.73 在框内、下方金线（y=1554、线宽 2）顶缘 1553，间隙为正；P2 Perfekt 指令单行 ✓；
  P6 图表标签 «tijd met gezin» 墨迹右端 521.0 < 条形起点 535（间隙 14；旧长标签会越界，
  缩短有效）、#86 注释同步 gezin ✓、免责声明整行在版内、健康框荷兰段 4 行（基线
  1311→1394）；P7 工具箱标题 «· Op zak» 墨迹右端 1853.0 < 1885；NOCH EIN WORT 框底
  1456.0、末行基线 1442.22 在框内 ✓（两数与建造者登记逐一吻合）。
  P8 F 区选项 a：文本节点 (x=1485, y=464, 同字体字号）与核心逐属性相同，两版卡片同区域
  裁图 sha256 完全相同（407724b2…）——核心冻结几何继承，裁定成立，不再标。
- **图片与署名**：P1/P2/P3/P5 内嵌图片数据与核心逐页字节相同（哈希一致），署名行
  （Courtney Celley/USFWS、NIST、Cranach 1528 Veste Coburg、USDA）与置入图片及核心 KIT 对应。
- **禁用术语**：终稿 SVG / 本 KIT / operative code 中 0 出现；唯一例外 scratch/transform.py
  1 处搜索模式（已披露）经 grep 确认仅此一处。
- **本轮唯一缺陷（文档层，已修）**：本 KIT 键差异登记原稿把 137/138 的注释互换错位
  （137 误记 «umstellen…»、138 误记 «een uur langer slapen…»，后者实为 139 的注释）。
  版面实印与寄存器一直正确，属登记文字之误；已按寄存器/实印改正上节登记，
  无需重渲染，PDF 针脚不变。
- **PDF 针脚（D5 重建，2026-11-13，与 KIT 登记一致）**：网页版 1,461,565 B /
  8b97b3c9b30a07164ad1419b1b7f53f5e2b8cf130b07a04fcbc0537a77a08eb2（< 7 MB）；
  印刷版 9,349,638 B / e578f25e9d0473c513013ae53e7a08e882b4c5529182fd75dac3dbbc659f691a（旧配方值 4,257,170 B / 10,478,874 B 已过期，见末节 D5 记录）。
- **核心未触碰**：核心 SVG 哈希复核未变。未入仓、未发 Discord。
## D5 重建记录（2026-11-13，W43/W45/W46 D5+§1.1 合并重修 Phase 1）

- **原因**：D5 缺陷——sans 层拉丁/西里尔字符落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者）。本版修前 census：D5 拉丁 665、西里尔 0、弯引号 CJK 0。
- **安装**：`tools/mechanism-w47/apply_variant.py --svglib <版>/svglib.py --target de --reader nl --week 2026-w43`（先 `--check` dry-run 通过）。`_D5_READER = "latin"`。路由单元测试 `test_d5_routing.py` FAILURES: 0。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 33 个全在 Newsreader。
- **基线**：重建前先证基线干净——`run.py` TOTAL 150、0 警告；重建 SVG 8/8 与 port fanout 逐字节相同；印 PDF 与 fanout BYTE-IDENTICAL。基线实测（§1.1 组装版）：印 PDF `74fbc91d3f03f345f4c1509bd9a7100294274410b0510555e8b98439db2fdcf0`（9945416 B）、网 PDF `c6767fd5f641e1dc4c4360295295df099a6bcffaa6f628c622bf93bfe7af2796`（1553130 B）。本 KIT 上方旧值（更旧配方）已过期，以上两值为准。
- **二次修复（只动字号与断行，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 两 p.text 标题内宽 400.5）**：
  1. `content12.py:25` P1 band 标题 36→31pt（与最紧 band-right 左界 ru 1542.0 间隙 76.7px）。
  2. `content12.py:124` herbst 头 25→22pt（框宽 422.5；25pt 430.2 超 7.7px，22pt 378.6）。
  3. `content12.py:47` numbers 盒 `f.box` 加 tsize=21（最差 +25.8；21pt 最大 392.8 < 404.5）。
  4. `content12.py:89` contents `IN DIESER AUSGABE` 24→22pt（最差 +9.0）。
  5. `content12.py:175` merksatz 盒 `f.box` 加 tsize=21（最差 +25.5；21pt 最大 392.5 < 404.5）。
  6. `content34.py:35` / `content56.py:34` P3/P5 facts 盒 +14→+34（末行溢出约 12.7px；en 家先例）。
  7. `content56.py:56` P5 Saturday-plan 头 24→22pt（nl +55.3；22pt 829.3 < 849.4）。
  8. `content56.py:155` P6 timeline 头 24→22pt（pt +10.3；22pt 376.1 < 400.5）。
  9. `content7.py:72` Toolbox 23→21pt（最差 +23.0；21pt 最大 386.4 < 400.5；22pt en 404.7 仍超）。
  10. `content7.py:92` NOCH EIN WORT 22→21pt（最差 +11.6；21pt 393.0 < 400.5）。
  11. `content8.py:74` P8 D 组头 24→22pt（it 428.3、nl 431.5 均超 422.5；22pt 最大 395.6）。

- P2 例外（run2b）：P2 facts 盒改回 +14（高度不变），facts 正文 21.5→21pt（wrap 8→7 行，盒底 356，余 22.1px）；P3/P5 保持 +34。
- **P8**：行数 232→217，距页脚线余量 33.7px；p8 compare CLEAN（keydiff [137, 138, 150]）。
- **新交付物（D5 重建，2026-11-13）**：印 PDF `e578f25e9d0473c513013ae53e7a08e882b4c5529182fd75dac3dbbc659f691a`（9349638 B）；网 PDF `8b97b3c9b30a07164ad1419b1b7f53f5e2b8cf130b07a04fcbc0537a77a08eb2`（1461565 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差 1 字节），以最终实测值为准。
- **text.md**：D5 不改文字内容；交付件为 port `.text.md.new` 原样沿用（BYTE-IDENTICAL，50536 B，sha256 `04c518ee250bd66118d1379985c5b7ad7c0866364047c8f7381e9a930d60b7e7`，570 条目 / 150 习题）；重建后重出 token-identical（rewrap RC=0）。本家 `issues/` 无已发 `.text.md`，基线以 port fanout 为准。
- **D5 门禁（17 门，run2b，全绿 ALL-GREEN）**：run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1461565 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=571，中位 1.007）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A；D18 刊头间距 71.1px。日志：`hidden_files/d5-redo/scratch-2026-w43-de/logs/2026-w43-de-nl/`（`GATES-SUMMARY.txt` 为总表）。D5 报告：`production/notes/2026-w43/g-de/scratch-d5-rebuild-de/D5-REPORT-2026-w43-de-nl.md`。
