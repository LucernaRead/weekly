# PROOF-NOTE — 2026-W47 de-it · proof1（独立复校，重建版）

- 版：`2026-w47-de-it`（德语正文，意大利语讲解）· VOL.4 · 刊期 2026-11-16–22
- 复校员：独立 proof1（与重建者非同一人）· 2026-11-11
- 结论：**(a) 零缺陷，可定稿** —— 内容与几何零缺陷（D 项：无）。
  工具层 T1/T2 另列（见 §7）：网页 PDF 系 D2 补丁落地前旧 webpdf.py 所建，
  衬线粗体/斜体渲染与印版不一致，属构建工具版本问题、非本版内容缺陷；
  按任务简报，pre-insert 将以定稿工具全部重建网页 PDF，重建后须另行核查。
- 未改源、未重建、未 commit、未 push。核查中 verify.py 重跑后 8 份 SVG 与
  两份 PDF 的 SHA-256 逐一复核，全部未变（见 GATE-LOG）。

## §1 SHA 核对（开工第一步，全部相符）

| 文件 | 字节 | SHA-256（前 16 位） | 结果 |
|---|---|---|---|
| `Die-Lucerna-VOL4-de-it.pdf`（印版） | 10,965,095 | `0d7be5816da19474` | ✓ 相符 |
| `Die-Lucerna-VOL4-de-it-web.pdf`（网页） | 1,553,872 | `dbbe5880e1b8b130` | ✓ 相符 |
| `2026-w47-de-it.text.md` | 49,712 | `1594ba080bece8b9` | ✓ 相符 |

两份 PDF 均为 8 页，1462.5 × 2025 pt。探针：开工前及每次写盘前
`git hash-object -w` + 真实写文件均通过（见 probe.txt，三次）；
全程未遇 `Disk quota exceeded`。

## §2 Q34 专项（重建唯一内容改动）

新题干 `"Am Montag öffnet in Köln der erste ___."` 各处 1×、旧题干 0×：

| 位置 | 新题干 | 旧题干 |
|---|---|---|
| `content34.py` | 1 | 0 |
| `2026-w47-de-it.text.md` | 1 | 0 |
| `svg/p3-kultur.svg` | 1 | 0 |
| 印版文字层（pdftotext） | 1 | 0 |
| 网页文字层（pdftotext） | 1 | 0 |
| P3 目视（印版 + 网页，100 dpi） | 可见新单数题干 ✓ | — |

键 `Weihnachtsmarkt` 不变（P8 答案键 Q34 核对一致）。
P3 冻结 sha 由上一轮 `093cf378` 变为 `fc88f676`，与重建报告一致——
冻结集仍为 195 条，仅 Q34 字符串本身改了；其余 7 页冻结 sha 与上一轮一致。
正文 P3 首段仍为复数 `"öffnen in Köln die ersten Weihnachtsmärkte"`
（指多家市场开市），与 Q34 单数填空（`der erste ___` = 一家市场）不矛盾，
与 core build15 一致。

## §3 逐页目视（印版 100 dpi，P1–P8 全看；网页 100 dpi，P1–P8 全看）

- **P1**：刊头、主标题、导语、FRAGEN DER WOCHE、IN DIESER AUSGABE、
  DAS WORT DER WOCHE、ZAHLEN 盒（`"(Bayern-Colonia 20.30)"` 两行、在栏内，
  rebuild-2 修复保留）、JETZT ÜBEN 1–6、足球图+图注、KURZ & GUT、
  BLITZQUIZ 7–10、页脚 `Pagina 1 di 8`。无溢出、无遮挡。
- **P2**：正文、Nota 盒、四侧栏（标题均在盒内）、RECHNEN 表
  （18.11.+11 天=29.11.、15.11.+7 天=22.11.、16.11.+6 天=22.11.，全对）、
  练习 A–D（11–28）。`DIE STILLE WOCHE　Tranquilla` 在盒内。
- **P3**：正文、Nota 盒、1930 年市场画+图注（Wilhelm Ritter，public domain）、
  `WEIHNACHTSWÖRTER　Parole` 在盒内、`DER TIPP　Consiglio` 在盒内、
  练习 A–D（29–46）。Q34 见 §2。
- **P4**：正文、Nota 盒、头球图+图注、UND SIE? 盒、9 行结果表、
  练习 A–D（47–64）。表与正文比分逐项一致（拜仁 2:0 马竞、多特 2:1 贝蒂斯、
  莱比锡 2:3 曼城、斯图加特 0:2 加拉塔萨雷、勒沃库森 0:1 马赛、霍芬海姆 1:1
  水晶宫、弗赖堡 1:0 特拉布宗、30 球第 9 轮、拜仁 2:1 美因茨、多特 2:1
  埃尔弗斯贝格、莱比锡 5:2 奥格斯堡、汉堡 3:1 门兴、德国 5 分荷兰 8 分）。
  O1 按裁定保留（正文提斯图加特 0:2 加拉塔萨雷为欧冠 prose，结果表只列德甲）。
- **P5**：正文、Nota 盒、ADVENTSKALENDER 盒、`ADVENTSWÖRTER　Avvento` 在盒内、
  UND SIE? 盒、1903 年日历图+图注（Richard Ernst Kepler，public domain）、
  周计划表（Mo 16.11. 国家队 20.45、Di 17.11. 开幕 19 点、Mi 18.11. 忏悔祈祷日、
  Do 19.11. 做日历、Fr 20.11. 拜仁–科隆 20.30）、练习 A–D（65–82）。
- **P6**：正文、Nota 盒、DIE ZAHLEN 盒（18.11./22.11./29.11./2,05/27.11./1995）、
  DIE STILLE WOCHE 通栏盒、DIE DEBATTE 盒、柱条 44/33/23（标签清晰）、
  ÜBUNGSDATEN 单行、练习 A–D（83–100）。44+33=77、44+33+23=100 与键一致。
- **P7**：三课 A2/B1/B2、BEISPIELE 三盒、工具箱 6 条（末条在盒内）、
  LESERBRIEFE（编辑部示例 + 意大利语披露，见 §5）、NOCH EIN WORT、
  阅览室图+图注（Carol M. Highsmith，public domain）、Sätze der Woche 8 句
  （§4）、FEHLERKLINIK 4 组、VOL.5 通栏。无溢出。
- **P8**：A 完形（113–120）/ B 问答（121–128）/ C 阅读（129–132）/
  D 造句（133–136）/ E 翻译（137–140）/ F 配对（141–144）/
  G 对话（145–149，5 枚徽章）/ H 写作（MUSTER 84 词，独立计数 84 ✓）/
  ANTWORTEN 8 组齐全、1905 足球图。键区末行距底边 118px，无溢出。
- 网页 8 页：内容、版式、几何与印版逐页一致（像素差异仅见 §7 工具层
  字重/斜体与图片重压缩带）；Q34 在网页 P3 同样可见。

## §4 核对项（数字、日期、金句、答案键）

- **日期星期**（Europe/Berlin 实测）：3.11.二、4.11.三、5.11.四、6.11.五、
  7.11.六、8.11.日、13.11.五、16.11.一、17.11.二、18.11.三、20.11.五、
  22.11.日、27.11.五、29.11.日——与表内 Di/Mi/Do/Fr/Sa/So 及正文
  “Freitag, dem 13.”、“Montag, dem 16.”、“Dienstag, 17.”、“Mittwoch, 18.”、
  “Freitag, 20.”、“Sonntag, 22.”、“Sonntag, 29.” 全部一致；
  Q14 键 Mittwoch ✓、Q89 键 18. November ✓、Q92 键 27. November ✓。
- **P7 金句 8 句逐字摘自正文**（正文 + P7 SVG 双向核对，8/8 逐字一致，
  出处页码全对）：P1“Nach zwei Wochen Pause spielt am Freitagabend der FC
  Bayern gegen den 1. FC Köln.”、P1“Es geht ums Viertelfinale der Nations
  League.”、P2“Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher
  Feiertag.”、P3“Die Märkte beginnen fast zwei Wochen früher.”、P5“Hinter
  jedem Türchen wartet eine kleine Überraschung.”、P4“Der FC Bayern gewann in
  Mainz mit 2:1.”、P6“Die stille Woche ist der Übergang: vom November in den
  Advent.”、P6“Am Sonntag ist es still im Land.”（verify.py verbatim OK 亦同）。
- **P8 练习 150 题与答案键**：p8 extract 150/150；compare CLEAN，
  keydiff `[137, 138, 139, 150]` 为预期（137–139 为意译键、150 为开放写作题；
  Q140 为反向题、键即德语句子，故不 diff）；150 键独立复核 149/150 精确，
  唯一非精确项为 Q150（抽取器将长键截为 "Esercizio libero"，预期内）。
  逐键抽查：Q34 Weihnachtsmarkt、Q43–46 造句、Q47–51 比分、Q52–55 配对
  （d/b/c/a）、Q56–59 比较级（mehr/später/früher/mehr）、Q60–64 时间
  （20.45/20.30/18.30/17.30/3:1）、Q65–69、Q70–75 词汇、Q76–79 weil 句、
  Q80–82 判断、Q83–88 图表（44/33/23）、Q89–92、Q93–96 语法、Q97–100 词汇、
  Q101–104、Q105–108、Q109–112、Q113–120 完形（schaut/bastelt/schreibt/
  sieht/beginnt/liest/denkt…nach/ist）、Q121–132、Q133–136、Q137–140 翻译
  （137 "La Bundesliga torna venerdì."、138 "I mercatini chiudono la
  domenica."、139 "Sto facendo un calendario dell'Avvento."、140 反向德语句）、
  Q141–144（c/a/d/b）、Q145–149（öffne/machst/schaue/schaue/lese）、Q150
  开放题——全部与 core 一致，意语键翻译准确。
- **text.md 与 core 全量 diff**（940 行）：逐对核查，德语正文/题干/键
  零漂移；全部差异均为讲解层（意大利语 vs 中文），包括 101 对
  “两侧都含德语词但无共享 U+3000 段”的标记对——逐对复核后均为
  指令标签（[Completa]/[Riscrivi]/[Vero o falso?] 等）或词注释义的语言差异，
  德语词干逐字相同。text.md 含 CJK 表意字 0 个、U+FFFD 0 个；
  唯一 CJK 残留为 P1  logo 内嵌 `<title>Lucerna 三色蛾</title>`（非渲染文本，
  与 core 逐字节相同，见观察项 O3）。
- **意语讲解质量**：全文意语通读，词注与译文准确（如 Stoccarda=斯图加特、
  Trebisonda=特拉布宗、Magonza=美因茨、Brema/Amburgo、"2,05 centesimi"、
  "44+33+23=100"）；指令标签全刊一致；ABSTRACT 一行 393 B、无 ASCII 双引号。

## §5 弯标点与 box-title 专项

- U+2019：8 份 SVG、text.md、content*.py 全部为 **0**（省音均用直撇号 U+0027，
  如 l'Avvento、d'Avvento、c'è，渲染紧凑）。U+201D：全部为 **0**。
- U+201C：text.md 33 处、SVG 合计 33 处——逐处核对，**全部为德语正文引文的
  右引号**，与 U+201E（„）成对（„… “），无一处落在意大利语值里；
  意语引文用 «»（如 P1 «der Adventskalender»、P5 «Im Lande des Christkinds»、
  NOCH EIN WORT «der Adventskalender»），符合意语规范。
- box-title 7/7：boxtitle.py 全过（DIE STILLE WOCHE Tranquilla 364.1、
  WEIHNACHTSWÖRTER Parole 361.3、DER TIPP Consiglio 242.2、ADVENTSWÖRTER
  Avvento 331.9、DER WERKZEUGKASTEN Attrezzi 379.5、LESERBRIEFE Lettere dei
  lettori 371.9、NOCH EIN WORT Ancora una parola 395.0，预算 400.5px），
  目视 8 版确认 7 个标题全部收进奶油盒内（最紧为 NOCH EIN WORT，余 5.5px）。
- P7 工具箱末条 "Es ist fraglich, ob ... = ancora dubbio" 在盒内；
  P7 末行距 1548 线 30px（EDITION-RECORD 称 1518.0）。

## §6 门禁（独立重跑，全部绿）

| 门禁 | 命令要点 | 结果 |
|---|---|---|
| occlusion_audit.py | 工具 + edition dir | RC 0，**0 flags**，selftest 6 类全触发、干净对照静默 |
| p8.py extract | P8 SVG，total 150 | RC 0，**150/150** |
| p8.py compare | core P8 vs edition P8 | RC 0，**CLEAN**，keydiff `[137, 138, 139, 150]`（预期） |
| freeze.py diff | core SVG vs edition SVG | RC 0，新增 CJK 7 个、全为 U+3000（P2–P8 各 1，P1 为 0） |
| freeze_direct.py | 源码级 + 渲染级 | RC 0，源码级未 accounted 0/0；渲染级 **8/8**（147/163/195/166/173/175/150/186；sha 083e2a2a/689045ad/fc88f676/df1bebf7/86fa4421/2bbe05f9/b7aa0771/57e118e7，与重建报告一致） |
| keycheck.py | 150 键 vs REG | RC 0，**149/150** 精确，仅 Q150 抽取器截断（预期） |
| boxtitle.py | 7 标题宽度 | RC 0，**7/7** |
| measure.py | 24 项定量几何 | RC 0，**24/24 PASS** |
| verify.py（重跑） | TOTAL/编号/样式/verbatim/字号/禁词 | RC 0，TOTAL 150、编号连续、SVG 重跑后逐字节相同、SOP 1.1 审计 True、verbatim OK、P8 字号底线 True、17 禁词全无 |
| pdftotext 文字层 | 默认模式 + -raw | 印版 50,593B / 网页 50,597B，**词多重集相同**；-raw 各 49,392B，**归一化文本完全相同** |
| abutting 扫描 | 自写 abut_scan.py（PyMuPDF 行内跨度） | 印版/网页各 23 处、**逐处相同**，全部为练习 "→ ___" 的设计间距（SVG 中空格为独立文本元素，宽 5.4 SVG 单位 ≈ 4.05pt）；**真实缺口 0** |
| chips | rx=2.7 矩形计数 | 每页 10/15/18/15/18/18/12/35，**总数 141**；P8 A2 22 / B1 13 / B2 0 |
| P8 最小字号 | PyMuPDF 实测 | 印版/网页均为 **9.94pt**（≥ 9.75pt 底线） |
| CJK 残留 | SVG 扫描 | 除 logo `<title>`（O3）外无 CJK 表意字；U+FFFD 0 |

（注：run.py / render.py / webpdf.py / export 未重跑——重跑会重写交付件；
verify.py 重跑已覆盖 TOTAL/编号/样式/verbatim/字号/禁词，且交付件 SHA
复核未变。）

## §7 工具层问题（单列，非内容缺陷；待 pre-insert 定稿工具重建网页 PDF）

- **T1 — 网页 PDF 衬线粗体丢失**：旧 webpdf.py 只嵌入 Newsreader-Regular，
  未嵌 Newsreader-Bold（pdffonts 核实：网页 PDF 无 Newsreader-Bold；
  印版有 Newsreader16pt-Italic/Bold 系）。200 dpi 标题栏并排对照：
  印版 "Die Bundesliga kehrt zurück – Bayern gegen Köln" 为粗衬线，
  网页为常规衬线。影响全刊所有 Newsreader 700 字重处（各版标题、金句、
  MUSTER 体等）；无衬线粗体（Noto Sans CJK SC Bold 已嵌入）不受影响。
  内容、换行、几何均不受影响（词多重集与 -raw 文本与印版完全相同）。
- **T2 — 网页 PDF 斜体丢失**：旧 webpdf.py 未嵌 Newsreader-Italic。
  全刊唯一斜体为 P1 本周词 «der Adventskalender»：印版斜体，网页正体
  （200 dpi 并排对照确认）。其余各页无斜体。
- 上述两项为构建工具版本所致（重建报告已载明：D2 补丁在 de-it 08:29 建成后、
  de-pt 08:31 之前落地；本版网页 PDF 用旧代码建成），非本版内容缺陷；
  pre-insert 以定稿工具重建网页 PDF 后应重新目视核查字重/斜体。
  网页 PDF 其余方面有效：8 页、真实文字层、< 7 MB、与印版文本一致。

## §8 观察项（非缺陷，不阻塞）

- **O1**：P5 UND SIE 意语提示只转述了德语提问的后半句——"Cosa c'è nella
  tua lista dei desideri? Scrivi in tedesco!"（德语原文另问 "Basteln Sie
  einen Adventskalender?"）。意语提示本身通顺、任务明确，属讲解层节略。
- **O2**：P7 工具箱 "vor fast leeren Rängen = davanti a tribune quasi vuote"
  未带中文版有的 UEFA 细节括号说明；词注本身准确。
- **O3**：P1 母版 logo 内嵌 `<title>Lucerna 三色蛾</title>`（与 core 逐字节相同；
  `<title>` 为非渲染元数据，读者不可见）。
- **O4**：Q18/Q35/Q77 等 "→ ___" 空格换行到下一行（与 core 版式相同，属
  源版式，非缺陷）。

## §9 缺陷清单

**无。D1…：空。**

---
*门禁命令与 RC 详见同目录 GATE-LOG.md；日志与 JSON 在同目录
（occlusion/p8extract/p8compare/freeze/freeze-direct/keycheck/boxtitle/
measure/verify/abut-web/abut-print/print.txt/web.txt）。*
