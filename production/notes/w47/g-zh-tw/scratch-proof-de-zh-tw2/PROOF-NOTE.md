# PROOF-NOTE — 2026-W47 de-zh-tw 独立复校（proof2，fix1 后从头全量复校）

- 复校员：独立复校员（与 fix1 不是同一人；与 proof1 也不是同一人）
- 复校时间：2026-11-11 09:55–10:07 UTC
- 复校对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-de-zh-tw/`（德文目标语 × 繁體中文读者语，fix1 重建版）
- 结论：**零缺陷，可定稿（a）**
- 红线遵守：只复校，未改任何源文件、未重建、未 commit、未 push、未动 tools/。全部渲染与中间件在本人 scratch 目录，`TMPDIR=<scratch>/tmp`，未写 /tmp、未动他人文件。
- 先读：SOP.md §8 与 §1.1 全文、repo AGENTS.md、协调员 brief 全文；另读 proof1 笔记（scratch-proof-de-zh-tw1）与 fix1 FIX-LOG/GATE-LOG（scratch-fix-de-zh-tw-toolbox）作为对照——但以下全部结论均为本轮独立重跑、重读、重测所得。

## 1. 身份核对（SHA 开工与收尾两次核对一致，未变）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de-zh-tw.pdf`（印刷） | 23,048,426 B | `74faeb9d898e254cd3f27a675063739701a9e40e387bde4b3622be5b7f240545` |
| `Die-Lucerna-VOL4-de-zh-tw-web.pdf`（网页） | 2,343,141 B | `352ead22cee3fc77c56aa5d036015ba3e309679848cbf722a5e11d22ceb296b9` |
| `2026-w47-de-zh-tw.text.md` | 49,092 B，1,185 行 | `fe62ddb59ac6ee2b2c474c7d11019295652e95e3c6bbd22b138fb4c7e798b0f9` |

两 PDF 均为 8 页，1462.5 × 2025 pt。探针：开工前 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功 + scratch 内真实写盘（`PROBE.txt`）。

## 2. 本轮重点：fix1 核实（只改 content7.py:76 一行，pad 90→110）

- 源码确认：`content7.py:76` 为 `+ 110`（注释写明 pad 110 恢复 core-de 值及清除量算式），其余源码未动。
- **creambox.py 全版扫查（实测）**：工具盒 y=330，盒底 **774.0**，末条基线 754.8，清除量 **+19.2** ✓（fix1 前 −0.8 已消除）；LESERBRIEFE y=790，盒底 1314.5，末基线 1304.4，清除量 **+10.1 不变** ✓；NOCH EIN WORT y=1330，盒底 **1480.5**，末基线 1437.6，清除量 +42.9，距 1548 Sätze 线 **67.5px** ✓。工具盒与 LESERBRIEFE 间 16px 间隙保留。
- 200 dpi 裁切目视（`renders/crop-p7-toolbox-200dpi.png`、`crop-p7-col3bottom-200dpi.png`）：6 条工具句（含末条 `Es ist fraglich, ob ... = 是否……尚未確定`）全部在盒内，盒下留白干净；NOCH EIN WORT 盒底与下方橄榄绿 Sätze 线分离清晰。
- 全版其余负清除量行均为 creambox 匹配器的已知误报（与 fix1 修复前相同位置、相同数值）：P1 −37.0/−24.0（其后栏目头落在 +45 窗口内）、P7 BEISPIELE −35.0×3（练习题号 101./105./109. 在盒下 35px 处），occlusion 审计 0 flags + 整页目视确认非缺陷。
- **text.md 与 proof1 版字节一致**：SHA `fe62ddb5…` 与 proof1 GATE-LOG 所记完全相同，零内容变化 ✓。

## 3. 机械门（全跑，全部通过；日志见 `gates/`，命令与输出见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| occlusion 审计 | **0 flags**；内建自检 6 类 planted 均触发、干净对照静默 |
| p8 extract | **150/150**，parse "joined" |
| p8 compare（vs core-de） | **CLEAN**；missing=[]，extra=0；keydiff=[137, 138, 139, 150]（见 §4 逐项说明） |
| freeze diff | exit 0；新增 CJK 合计 1,328（P1 109 / P2 89 / P3 135 / P4 80 / P5 121 / P6 109 / P7 174 / P8 511），与 proof1 逐页一致 |
| freeze_direct | **渲染 8/8 PASS**（frozen 151/164/206/166/182/176/170/191；sha8 54c9b51e / 2db0dd83 / ad74f280 / df1bebf7 / b42a8c3d / babfe417 / 9dc31873 / 961dd98a，与 proof1/fix1 全 8 页逐项一致——P7 文本冻结值不变，只动了盒几何）；源层级仅 4 条预期内 TC 字体切换串（删 `Noto Serif CJK SC`，增 `TC` / `Noto Sans CJK TC` / `Noto Serif CJK TC`） |
| Q34 | 新题干 `Am Montag öffnet in Köln der erste ___.` 在 content34.py、P3 SVG、text.md、印版文字层、网页文字层各 **1×**；旧复数题干 **0×**；key `Weihnachtsmarkt` 不变 |
| 弯引号 | U+201C ×33 与 U+201E ×33 成对（德文 „…"）；U+00AB ×6 与 U+00BB ×6 成对（«…»）；U+201D 0、U+2019 0（8 个 SVG + text.md + content*.py + 两版 PDF 文字层全扫） |
| P8 最小字号 | 印版与网页均为 **9.94 pt**（下限 9.75 pt，SOP §1.1 step 4） |
| boxtitle（400.5 px 预算） | **7/7 PASS**，最大 363.6 px（`DIE STILLE WOCHE 寧靜的一週`） |
| keycheck | **149/150 exact**；唯一 Q150 PREFIX——提取器把键 `開放任務 — 依寫作框中的要點進行` 截断为 `開放任務`；完整键经核实在 P8 SVG 内，属提取器 artifact，非缺陷 |
| 印/网文字层 | 各 49,905 B；逐页字节相同（P1 4712 / P2 4738 / P3 6030 / P4 5349 / P5 5340 / P6 5346 / P7 5349 / P8 13041）；逐词多重集逐页相同；`-raw` 规整化后 **逐字节相同**（48,777 B） |
| chips（SVG 徽章节点） | 合计 **141** = P1 10 / P2 15 / P3 18 / P4 15 / P5 18 / P6 18 / P7 12 / P8 35 |
| 禁词（印版文字层） | 全部 0：Le Lucerna、The Lucerna、VOL.3、VOL.2、Geisterspiel、Karneval、Volkstrauertag、NFL、American Football、11.11、Tankrabatt、14,04、Hart aber fair、Klassiker、Allerheiligen、8,35、ZEW |
| 繁體字形 | 渲染文本无简体专属字（`常` 仅见于 平常/常見，简繁同形，非简体专属）；TC 形 為/國/學/讀/說/請/還/過/這/進/運/連/長/門/間/開/關/見/話/譯/護/聖/誕/曆/願/裡/複/並 全部在位 |
| ABSTRACT.txt | 294 B，单行，繁體中文，无 ASCII 双引号；含刊名、目标语（德文）、A2–B2、150 道練習及本期真实话题 |
| 字体嵌入 | 两 PDF 全部字体 emb=yes；网页版已嵌 `LucernaNewsreader-Italic`（proof1 的缺 Italic 备注已由本次重建解决；Bold 多子集仍在，属 webpdf 子集化行为，渲染正常，见 §8 观察项） |

## 4. p8 compare keydiff 逐项说明

- Q137–139：题型「譯成繁體中文」，键为繁中译文，与 core 德文键自然不同，合法。
- Q140：「譯成德文」，键为德文句，与 core 相同，故不在 keydiff 内。
- Q150：开放写作任务，键为任务说明（见 §3 keycheck 行）。

## 5. 追加测量：de-en proof2 D1/D2 闭引号宽体类（200 dpi 像素墨列测量，同法）

任务追加：de-en proof2 发现 P8 H 写作框指示行与 Q67 答案键注里的闭引号 U+201C 在 Noto Sans CJK SC 里宽体渲染（空隙 9.72pt/7.20pt），要求按其 D1/D2 方法（200 dpi 像素墨列测量）加测本版两处；>0.2em 列为缺陷，≤0.2em 记为已测通过。方法：200 dpi 印刷 PDF 单连续窗口像素墨列分析（`quote_pixel.py`，阈值 <128；闭引号墨迹以其墨列起点落在该字符 advance 框内为准——首版重叠判据曾把 Q67 前一字母 `s` 的墨列误算进引号，已修正并重测；两次数值一致）。

| 处 | 字体/字号 | 闭引号前空隙 | 结论 |
|---|---|---|---|
| P8 H 框指示行 `«Meine Novemberwoche»` | Newsreader 16.12pt（**不是 sans**——SVG 21.5pt Newsreader，PDF span `Newsreader16pt-Regular`） | **1.80pt = 0.11em** | PASS |
| P8 Q67 注 `«Im Lande des Christkinds»` | Noto Sans CJK **TC** 9.94pt（`NotoSansCJKtc-Regular`） | **1.08pt = 0.11em** | PASS |
| 对照：P8 对话 `„Eine stille, schöne Woche"` | Newsreader 14.62pt | 1.44pt = 0.10em | — |
| 对照：P5 标题 `„Im Lande des Christkinds"` | Newsreader 18.0pt | 1.80pt = 0.10em | — |

- **de-en D1/D2 缺陷类在本版不复现**：H 框指示行是 Newsreader 而非 sans；Q67 的闭引号是 U+00BB »（advance 仅 4.76pt，墨迹贴在其字元左缘、起于框内 0.63pt 处），不是 de-en 的 U+201C（全宽字元、墨迹贴右缘）。两处空隙与 Newsreader 对照组同量级（0.10–0.11em），远低于 0.2em 阈值。
- 200 dpi 裁切目视（`renders/crop-p8-hbox-200dpi.png`、`crop-p8-key67-200dpi.png`）：两处闭引号均贴紧前一字母，与开引号对称，无可见断开。
- 本版 33 对 „…" 全部以 Newsreader 呈窄体；6 对 «…» 中仅 Q67 一处在 sans 语境，其 » 亦窄。

## 6. text.md 全文通读（1,185 行）与 150 键逐项核对

- **P1**：头条 Bundesliga Bayern–Köln；Q1–10 全对（Q5 答案 5 分；Q6 29. November；BLITZQUIZ Q7 B、Q8 A、Q9 B、Q10 B）。目录页（S.2–S.8）与实际页/等级相符。图注：Staff Sgt. Stephanie Jacobs, U.S. Air Force，public domain。
- **P2**：Buß- und Bettag；1995 废除/Pflegeversicherung/仅萨克森 + 更高缴费；舞蹈禁令 3–24 Uhr；RECHNEN 18+11=29、15+7=22、16+6=22；Q11–28 全验（Perfekt：abgeschafft worden / geschlossen geblieben / gegangen / behalten；配对 25=d、26=c、27=a、28=b——与渲染页显示的 a–d 释义逐项一致）。
- **P3**：科隆市集；Q29–46 全验；Q34 新单数题干、键 Weihnachtsmarkt；Q32 false（画是 Nürnberg，非 Köln）；Q40 B（23. Dezember）；Q42 A（早近两周，13 天）。
- **P4**：成绩表；Q47–64 全验（Q51 B = 荷兰 8、德国 5；Q56 mehr、Q57 später、Q58 früher、Q59 mehr；配对 52=d、53=b、54=c、55=a——与渲染页显示的 a–d 释义逐项一致；Q60 A 20.45、Q61 B 20.30、Q62 C 18.30、Q63 A 17.30、Q64 B 3:1）。MD9 进球和：4+3+3+7+4+1+3+2+3 = 30 ✓。
- **P5**：Adventskalender 1903《Im Lande des Christkinds》（Richard Ernst Kepler）；Q65–82 全验（Q67 B、Q68 B、Q81 Falsch、Q82 Richtig；weil 句 76–79 动词末位 ✓）。Wochenplan 星期/日期一致。
- **P6**：图表 44/33/23 = 100；Q83–100 全验（Q85 B 77、Q88 B 100；Q93 wird、Q94 ob、Q95 geht、Q96 beginnt；Q98 Kirchenjahrs 属格 ✓）。图表明确标注 ÜBUNGSDATEN 练习数据、非真实调查（SOP §2 ✓）。
- **P7**：Q101–112 全验（101 wird、102 werden、103 wird；105 stiller、106 weil、109 ob、110 fraglich、111 dass 句动词末位 ✓）。**8 条 Sätze der Woche 全部逐字出自本期正文**（SOP §4）：P1 ×2、P2、P3、P5、P4、P6 ×2，Seite/等级标注正确；繁中译文全部准确。Fehlerklinik 4 对全对（halb neun = 8.30 Uhr ✓）。Leserbriefe 披露为编辑示例、尚无真实来信，最佳真实来信见 VOL.5。VOL.5 预告：首个将临主日 11 月 29 日、欧战结果 11 月 24–26 日、第 11 轮——全部一致。
- **P8**：A 完形 113–120（schaut/bastelt/schreibt/sieht/beginnt/liest/denkt nach/ist ✓）；B 121–128 ✓；C 129–132（A/B/B/B ✓）；D 133–136 ✓；E 137–140 译文全验（137 德甲週五回歸。、138 週日市集休息。、139 我正在做將臨期日曆。、140 `Am Montag schaue ich zu Hause Deutschland gegen die Niederlande.` ✓）；F 141=c、142=a、143=d、144=b ✓（与渲染页 a–d 释义逐项一致）；G 145–149（öffne/machst/schaue/schaue/lese ✓）；H MUSTER 文 83 个实词 + 1 个独立 em-dash token = 84 个空白分隔 token，标注「84 詞」——**与 de-en 版同一惯例**，属全刊惯例，非缺陷。答案区 Q1–150 全部与题干相符。
- 日期/星期经 `date`（Europe/Berlin）核对：2026-11-03 周二、11-04 周三、11-05 周四、11-06 周五、11-07 周六、11-08 周日、11-13 周五、11-16 周一、11-17 周二、11-18 周三、11-20 周五、11-22 周日、11-24 周二、11-25 周三、11-26 周四、11-27 周五、11-29 周日、12-01 周二、12-23 周三。本期周 2026-11-16–22，VOL.4。

## 7. 外部事实抽查（2026-11-11 网页检索，本轮独立重验）

- 塞尔维亚–德国，2026-11-13 周五 20:45，贝尔格莱德 Rajko Mitić，欧足联观众禁令（U15 以下儿童 + 50 名指定 DFB 球迷入场，约 5,000 人）——与 P1 表述完全一致。德国 4 战 5 分，欧国联 A2 组第 3，落后荷兰与希腊（各 8 分）。德国–荷兰 11 月 16 日周一 20:45 柏林。
- Bayern–Köln：第 10 轮，2026-11-20 周五 20:30，Allianz Arena（fcbayern.com / fussballdaten / come-on-fc）；fussballdaten 第 10 轮对阵表注 Bayern (1.)、Köln (15.) ✓。
- 科隆圣诞市集 2026：Dom（Roncalliplatz）+ Markt der Engel（Neumarkt）11 月 16 日–12 月 23 日，11 月 22 日周日（Totensonntag）关闭；Hafen-Weihnachtsmarkt（Schokoladenmuseum）自 11 月 13 日起；免费入场（colognecathedral.de / koeln.de 系来源）✓。
- Bundeshaushalt 2027：Bundestag 终表决计划 **2026-11-27 周五**（bundestag.de 原文）；家庭 Stromsteuer 2.05 Cent/kWh，工业 0.05；Merz 希望全民下调、尚未决定（"Ob eine Einigung gelingt, ist offen" ✓）。
- 其余事实（欧冠 MD4 比分、欧联/欧协联 11 月 5 日赛果、德甲 MD9 9 场 30 球、第 10 轮前瞻时刻、Ritter 1930 年 Nürnberg 画作、萨克森舞蹈禁令 3–24 Uhr、Aachen 市集 11 月 20 日–12 月 23 日）与 proof1 2026-11-11 的逐项核实一致，且本轮全文通读未发现与之矛盾的内部表述；MD9 30 球已由成绩表逐场加和复算（§6 P4）。

## 8. 目视复核（印刷版 8 页全看 + 网页版 P1、P8 + 200 dpi 裁切 4 张）

渲染件：`renders/print-p-1.png` … `print-p-8.png`（100 dpi，2032×2813，PIL 校验全部通过）、`renders/web-p1-1.png`、`renders/web-p8-8.png`；200 dpi：`print-p5-200dpi-5.png`、`print-p7-200dpi-7.png`、`print-p8-200dpi-8.png` 及 4 张裁切。

- **P1**：干净。刊头、头条条、FRAGEN 侧栏、IN DIESER AUSGABE、DAS WORT DER WOCHE « der Adventskalender »（斜体）、图片+图注+credit、BLITZQUIZ 7–10 四栏、页脚 `第 1 頁／共 8 頁`，无溢出重叠。
- **P2**：干净。4 个侧栏盒、RECHNEN 表、ÜBUNGEN A–D 11–28；D 配对 a–d 字母与答案一致。
- **P3**：干净。Q34 新题干单行完整；Ritter 画+图注+credit；盒标题均在框内；ÜBUNGEN 29–46 无溢出。
- **P4**：干净。成绩表 10 行（斑马纹）与正文及核实结果一致；B 配对 a–d 与答案一致；UND SIE? 盒、图片+图注、ÜBUNGEN 47–64。
- **P5**：干净。1903 日历图与 ÜBUNGEN 标题无重叠；WOCHENPLAN 表；ÜBUNGEN 65–82；Q67 选项德文引号 „…" 正确。
- **P6**：干净。DIE STILLE WOCHE 通栏盒；图表 3 条标签与条形无压叠（44/33/23），ÜBUNGSDATEN 免责声明在位；ÜBUNGEN 83–100。
- **P7**：干净。三课 A2/B1/B2、BEISPIELE 盒、Library of Congress 图+图注、WERKZEUGKASTEN（6 条全在盒内，盒下留白干净，见 §2）、LESERBRIEFE（含披露）、NOCH EIN WORT（盒底与 Sätze 线分离清晰，见 §2）、8 条金句、FEHLERKLINIK 4 对、VOL.5 预告带；页脚 `第 7 頁／共 8 頁`。
- **P8**：干净但密。A–H 113–150 全部在位；G 对话徽章条（A2 145、A2 146、A2 147 / B1 148、A2 149）；1905 足球图+图注；H MUSTER 範文（84 詞）盒完整；ANTWORTEN 全部答案与注解在页脚上方结束，无裁切；页脚 `第 8 頁／共 8 頁`。H 框 «Meine Novemberwoche» 闭引号在 100 dpi 整页上亦贴紧。
- **网页版 P1、P8**：与印版渲染逐页一致，无缺字、无豆腐块；粗体标题正常渲染。网页文字层已全量比对（§3）。

## 9. 观察记录（非阻塞，不构成缺陷）

1. P1 称 11 月 16 日荷兰战为「das Endspiel」，P4 则精确称「das letzte Gruppenspiel … es geht um das Viertelfinale」——「Endspiel」为口语化「决战」说法，用词略松，非事实错误（沿用 proof1）。
2. MUSTER「84 詞」把独立 em-dash 计为一个空白分隔 token（83 实词）——与 de-en 版同一全刊惯例，非缺陷（沿用 proof1）。
3. 简体字仅见于源代码注释（content8.py、svglib.py 注释及 KIT §4 TYPEMAP 键），从不渲染（沿用 proof1，本轮未重扫源码注释——渲染文本已扫为零）。
4. 网页 PDF：Italic 子集本次已嵌（proof1 缺 Italic 备注已解决）；Bold 仍有多个子集条目，属 webpdf 子集化行为，渲染正常。
5. P1 无首字下沉（继承，de-en proof2 同类 O3 亦记；KIT 诚实短板）。
6. P4 正文提及斯图加特在加拉塔萨雷 0:2 告负，但赛果表未列该场——core-de 同样如此，无练习依赖（de-en proof2 O1 同类）。

## 10. 缺陷清单

**无。零缺陷。**

## 11. 结论

**定稿（a）**：印刷 PDF 与网页 PDF 全部 8 版、text.md、SVG 经从头全量复校——德文正文、繁體中文讲解、日期星期、数字、金句逐字、P8 全部 150 键、外部事实、机械门、目视——**零缺陷**。fix1 的 P7 工具盒修复实测达标（+19.2，NOCH EIN WORT 止 1480.5，LESERBRIEFE +10.1 不变），text.md 与 proof1 版字节一致；de-en proof2 的 D1/D2 闭引号宽体类经同法 200 dpi 像素测量在本版不复现（H 0.11em、Q67 0.11em，均 ≤0.2em）。可按 SOP 进入下一环节。
