# PROOF-NOTE — 2026-W47 de-nl · proof1（独立复校，重建版）

- 复校员：独立 proof1（与重建者 B 不是同一人）
- 日期：2026-11-11（America/Toronto）
- 版目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-de-nl/`（只读；未改源、未重建、未 commit、未 push）
- 对照：`~/workspace/weekly-git/production/2026-w47/core-de/`（build15，proof5 (a)）

## 结论：(a) 零内容缺陷，可定稿

内容缺陷 D1…：无。工具层事项见 §7（单列，不计入内容缺陷；pre-insert 以已打补丁的
`tools/webpdf.py` 重建网页 PDF 即消除）。

## §1 SHA 核对（先核对，全部相符）

| 文件 | 字节 | SHA-256（实测） | 任务给定 | 结果 |
|---|---|---|---|---|
| `Die-Lucerna-VOL4-de-nl.pdf`（印刷） | 10,964,699 | `8f47eea85f54067532cad3e21ba74d3ed98133a3eabc5605dcb34ca3cca8d6d6` | 同左 | ✓ 相符 |
| `Die-Lucerna-VOL4-de-nl-web.pdf`（网页） | 1,553,854 | `be22a1b5beda4dcaaeccbcffcb7a122e01bb3f92a488d896fd261808ffc34551` | 同左 | ✓ 相符 |
| `2026-w47-de-nl.text.md` | 49,403 | `e904fb3d7ee18a72c1316f8693f39436ff9390648261d6fbad18afcfb7fc848e` | 前 8 位 `e904fb3d` | ✓ 相符 |

## §2 逐页复校（印刷 PDF 8 页，100 dpi 全页目视 + text.md 全文 + core-de 逐项对照）

- P1：头条、导语、数字框（5 分/4 轮、20.30 开球、30 球）、JETZT ÜBEN Q1–6、FRAGEN DER
  WOCHE、IN DIESER AUSGABE、DAS WORT DER WOCHE `« der Adventskalender »`、BLITZQUIZ
  Q7–10、图注与 credit 全部与 core 一致；荷兰语说明正确。
- P2：Buß- und Bettag 全文、RECHNEN（18+11=29、15+7=22、16+6=22）、Q11–28
  （日期、Perfekt Q16–20、阅读 Q21–24、配对 Q25–28：25-d、26-c、27-a、28-b）
  全部核实；gloss（evangelisch = protestants、Pflegeversicherung =
  zorgverzekering、still = stil）正确；Opgelet 警告句用法正确。
- P3：全文、图注（Wilhelm Ritter 1930）、Q29–46 全部核实；**Q34 新题干目视确认**（见 §5）。
- P4：全部赛果（Bayern 2:0 Atlético、Dortmund 2:1 Betis、Leipzig 2:3 Man City、
  Stuttgart 0:2 Galatasaray、Leverkusen 0:1 Marseille、Hoffenheim 1:1 Crystal
  Palace、Freiburg 1:0 Trabzon；德甲 30 球；Bayern 2:1 Mainz、Dortmund 2:1
  Elversberg、Leipzig 5:2 Augsburg、HSV 3:1 Gladbach）、赛程表 3.–16.11.、
  Nations League 5/8 分、Q47–64（比较级 Q56–59、时刻 Q60–64）全部核实。
- P5：全文、WOCHENPLAN（Mo–Fr）、Q65–82（Q73 答案 Schokolade）全部核实。
- P6：全文、DIE ZAHLEN（18.11./22.11./29.11./2,05/27.11./1995）、图表
  44+33+23=100、Q83–100 全部核实；ÜBUNGSDATEN 标注正确。
- P7：三节小课、Q101–112、WERKZEUGKASTEN、LESERBRIEFE（含编辑部示例 +
  荷兰语披露，无真实来信）、NOCH EIN WORT、FEHLERKLINIK 4 条、VOL.5 预告
  全部核实。**金句 8 条逐字摘自正文**（见 §4）。
- P8：Lückentext Q113–120、Quiz Q121–128、阅读 Q129–132、造句 Q133–136、
  翻译 Q137–140、配对 Q141–144（141-c、142-a、143-d、144-b）、对话 Q145–149、
  写作 H、MUSTER、150 条答案键全部核实；**MUSTER 实测 84 词**（与标注一致）。

日期核实（`date -d`，Europe/Berlin）：13.11. 周五、16.11. 周一、17.11. 周二、
18.11. 周三（Q14 答案 Mittwoch 正确）、20.11. 周五、22.11. 周日、27.11. 周五、
29.11. 周日、3.11. 周二、8.11. 周日——全部与刊物一致。

荷兰语说明层：`tr_nl.py` 278 条翻译值逐条读过，无错译、无残留中文、无错用
Opgelet（仅 P2 警告句一处，正确）；`Uitleg — ` 前缀统一；je/jouw 口吻全版一致。

## §3 网页 PDF 逐页校对

- `pdftotext` 默认模式：印刷 50,192 B / 网页 50,194 B，**词集完全相同**；
  `-raw` 模式：均为 47,634 B，**归一化后逐字相同**；8 页齐全。
- 网页 P1、P3 在 100 dpi 下渲染与印刷版版式一致，无缺字、无溢出、无断行异常；
  Q34 在网页 P3 同样可见。
- abutting 扫描（`d2scan-full.py` 改写为 de-nl 路径后独立重跑）：54 对邻接跨度，
  最差网页间隙 0.00 pt，**>0.5 pt 为 0**。
- 工具层字重差异见 §7（与内容缺陷分开报告）。

## §4 P7 金句逐字核对（8/8 出自正文，含出处页码与级别）

1. `Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln.`
   （P1 原句后半分句原文）— Seite 1 · A2 ✓
2. `Es geht ums Viertelfinale der Nations League.` — Seite 1 · A2 ✓
3. `Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.` — Seite 2 · A2 ✓
4. `Die Märkte beginnen fast zwei Wochen früher.` — Seite 3 · A2 ✓
5. `Hinter jedem Türchen wartet eine kleine Überraschung.` — Seite 5 · B1 ✓
6. `Der FC Bayern gewann in Mainz mit 2:1.` — Seite 4 · B1 ✓
7. `Die stille Woche ist der Übergang: vom November in den Advent.` — Seite 6 · B2 ✓
8. `Am Sonntag ist es still im Land.` — Seite 6 · B2 ✓
荷兰语译文 8 条全部准确。

## §5 Q34 专项（重建唯一改动）

新题干 `Am Montag öffnet in Köln der erste ___.` 各处均为 1×：
源码 `content34.py` 1×、`.text.md` 1×、P3 SVG 1×、印刷 PDF 文本层 1×、
网页 PDF 文本层 1×，P3 印刷版与网页版均已目视确认。
旧题干 `Am Montag öffnen in Köln die ersten ___.` 全版 0×。
正文中的 `öffnen in Köln die ersten Weihnachtsmärkte`（P1/P3/P5，复数主语 +
复数动词）为合法正文句，非旧题干残留；答案键 Q34 = `Weihnachtsmarkt`，单复数一致。

## §6 专项扫描

- 弯标点：8 个 SVG + text.md 中 U+201D = 0、U+2019 = 0；U+201C 共 33 处，
  全部与 U+201E 配对（P1 5/5、P5 6/6、P7 21/21、P8 1/1），全部位于德语引文
  （`„…"` 闭引号），**荷兰语值中为 0**。版内无任何直撇号 `'`（无 's 属格），
  无 nl-en proof1 `Editor' s` 类渲染问题。
- Box-title：`boxtitle.py nl` 独立重跑，**7/7 在盒内**（预算 400.5px；
  最宽 DER WERKZEUGKASTEN `Werktuig` 395.5px，余 5.0px；其余 319.4–380.4px）。
- CJK 残留：仅 U+3000 家具分隔符（146 处）+ moth 标志 `<title>Lucerna 三色蛾</title>`
  内 3 字（非渲染文本）；无读者可见中文。
- ABSTRACT.txt：一行荷兰语，无 ASCII 双引号 ✓。

## §7 工具层事项（单列，不计入内容缺陷）

本版网页 PDF 系 D2 补丁落地前旧 `tools/webpdf.py` 所建；pre-insert 将以定稿工具
全部重建。独立测量（PyMuPDF，印刷 vs 网页逐行/逐跨度比对，1,850 行）：

- Newsreader（衬线）行宽差 >0.5 pt 共 **61 行**：最严重 P1 头条
  `Die Bundesliga kehrt zurück — Bayern gegen Köln` 网页窄 **49.09 pt**；
  P7 24 行（金句与 Fehlerklinik 粗体行）、P1 11 行、P6 7 行、P2 6 行、
  P3/P4/P5 各 4 行、P8 1 行。机制与已知的 D2 一致：印刷用 SemiBold、
  网页用了 Regular（Noto Sans/Serif 跨度差 0.00%，不受影响）。
- 斜体 1 处：P1 `« der Adventskalender »` 印刷斜体 173.44 pt，网页直体
  Regular 183.13 pt（宽 9.69 pt，网页无 Newsreader 斜体面）。
- Abutting 邻接间隙本身为 0（§3），即缺陷只表现为整行收窄，不产生词间空洞；
  网页版无溢出、无缺字。
- `tools/webpdf.py` 现已包含补丁（`:weight=200` bold / `:weight=100` regular，
  第 94–98 行注释与 ru-en 补丁一致），pre-insert 重建即消除。

## §8 门禁（全部独立重跑，命令与 RC 见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| occlusion_audit.py | 0 flags，selftest OK（6 类 planted 全触发），RC 0 |
| p8.py extract | 150/150，RC 0 |
| p8.py compare vs core-de | CLEAN，missing=[]，keydiff=[137, 138, 139, 150]（预期），RC 0 |
| freeze.py diff | 8/8，新增 CJK 仅 7 个 U+3000（P2–P8 各 1，P1 0），RC 0 |
| keycheck.py（150 键独立重跑） | 149/150 exact；唯一不符 Q150 为提取器截断（预期，开放写作题），RC 0 |
| boxtitle.py nl | 7/7 fit，RC 0 |
| 印刷/网页文本层 | 词集相同；-raw 归一化相同 |
| abutting 扫描 | 54 对，worst 0.00 pt，>0.5 pt 为 0 |

## 附：复校方法

印刷 PDF 8 页 100 dpi 全页目视；`.text.md`（591 条）全文读过并与 core-de
`.text.md` 逐行比对（940 行 diff 全部归入说明层）；`tr_nl.py` 278 条值逐条读过；
P8 答案键与 REG 逐条比对（keycheck 独立重跑）；数字/日期全部以 `date -d` 与
算术复算；MUSTER 逐词计数 84。
