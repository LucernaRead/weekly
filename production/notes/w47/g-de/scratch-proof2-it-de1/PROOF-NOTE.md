# PROOF-NOTE — 2026-W47 it-de（独立复校 proof2，重扩散新版）

- 复校员：proof2（只读生产，未改任何生产文件、未 commit、未 push、未重渲染交付的 web PDF）
- 日期：2026-11-11
- 复校对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-de/`（重扩散新版）
- 对照 core（冻结源）：`~/workspace/weekly-git/production/2026-w47/core-it/`（fix3 commit `36bdec2e`）
- Scratch（唯一工作区）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-de1/`
- 依据：SOP §8（全量 proofread + 机械门禁 + 8 版逐版看图 + 循环规则）；重扩散报告 `scratch-refanout-it/FANOUT-REPORT-it.md` 只作对照，不作证据——全部结论均为本轮实测。

## 结论：(b) 有缺陷，见下清单（2 项）

两项均为奶油盒标题横向溢出（同类，见 §5）。其余门禁 20/20 全过、全文 1317 行已通读、8 页已逐版目视。除清单外无缺陷。

## 0. SHA 核对（三件与简报一致；KIT §7 印/网 SHA 一致，文本以字节+行数对上）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-DE.pdf` | 14,037,260 B | `ee5a962f1f3b59a8a225acbf949ee542b7d81f99451cc1dc591babb0a3c3234f` |
| 网页 PDF `La-Lucerna-VOL4-DE-web.pdf` | 1,297,292 B | `e6d3df844c9fa4fd3ef5e39dcf6cd80d740dfbd7cc5208384763efc6ee89eb84` |
| 文本导出 `2026-w47-it-de.text.md` | 56,699 B | `8660fc02b2510cce831e5c3e57b0020949dc4c05e5d4b1bd30db4e667b4cc222` |

两 PDF 均为 8 页、1462.5×2025 pt。KIT §7 L45–46 所载印/网 SHA 与盘上逐字节一致；KIT 未印文本 SHA，文本以 §7 L47 所载 56,699 B / 1317 行对上盘上实测（`wc` 56,699 B，1317 行 + 结尾换行）。探针 `git hash-object -w /dev/null` rc=0，goals-side scratch 真实写盘通过（`probe.txt`）。生产三件 SHA 在复校结束时复核仍与上表一致，mtime 未变（12:17–12:19），生产只读成立。

## 1. 门禁全套（全部本轮重跑，见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| run.py（scratch 副本） | RC=0；TOTAL 150；A2 47 / B1 70 / B2 33；页 10/18/18/18/18/18/12/38；范文 99 词；FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE = 0（`out/run.log`） |
| SVG 重建 | 8/8 字节一致（重建 SHA vs 交付 `svg/`，`sha256sum -c` 全 OK，`out/rebuilt-names.sha256`） |
| 重渲印 PDF | RC=0；重渲件 14,037,260 B，SHA = 交付件 `ee5a962f…`，逐字节相同（render.py 仅改 BASE 后在 scratch 跑，`out/render.log`） |
| freeze baseline（`tools/freeze.py baseline`） | **8/8 字节一致**，core 完整性复核通过（`out/freeze-baseline.log`） |
| freeze diff vs core | 0 unexplained fragments（P1–P7）；新增 CJK 仅 U+3000 ×13（家具分隔符，豁免）；其余新增全为德语讲解层/家具，删除全为 core 中文讲解层；意大利目标语零改动（`out/gates.log`） |
| occlusion audit | **0 flags**，selftest 6 类阳性对照全触发、干净对照静默（`out/occlusion.log`）。但本轮证实：occlusion 对无边框奶油盒横向溢出是盲的（见 §5），0 flags 不能为盒标题背书 |
| p8 extract | **150/150 noted**（`out/p8-extract.json`） |
| p8 compare vs core | **CLEAN**，missing=[]，keydiff = **[137, 138, 139]**（预期：重定向的读者句键；Q140 为意语句键，core 与本版相同、无 diff，正确）（`out/p8-compare.json`） |
| 印/网文字层 | pdftotext 多重集相同（各 7,787 词，字符集相等）；网 PDF 文字层 46,127 B（与印版逐字节等长）；网 PDF 1,297,292 B < 7 MB |
| P8 最小字号 | SVG 最小 13.0 px = **9.75 pt**（SOP §1.1 下限） |
| §1.1 扫描 | 纸色 #fbfaf6 在；无金/砖/近黑；VOL.4 ×9；VOL.5 仅 3 处合法节点（预告/LETTERE 说明/P2 交叉引用）；徽章色 A2/B1/B2 在；无双层外框（0 全页 rect） |
| text.md validate | forward-miss 0 / reverse-miss 0 |
| 150 键复核 | 键 1–150 与 core 一致（除 137–139 重定向与写作项）；notes 与 translations.py 一致（除 137–140 + 写作项）；table_gaps=[] |
| 奶油盒 PIL 真墨扫（本轮自写 `creambox-proof2.py`） | 29 个 #f0eee5 盒全扫：横向溢出 2 处（即 §5 缺陷 D1/D2）；纵向 9 盒紧（见 §4，像素复核全为正清除量） |
| 横向 spill 扫（本轮自写 `h-overflow-proof2.py`，1617 节点） | 页边溢出 15 处 PIL 标记，交付 PDF 200 dpi 像素裁定后：实墨越线仅 P8 家具行 +2.4 px 与范文行 +1.4 px（见 §6，非缺陷）；其余为 ≤0.4 px 亚像素噪声 |
| 孤儿扫（`out/orphan.log`） | **0 孤儿**（见 §4） |
| 日期/星期全验 | 文中全部星期表述与 `date` 实测一致（见 §3） |
| 标题数实测 | 「56 titles」是幻数：机械规则计 104 个标题行；清洗后本版实有 61 个具名标题（见 §3） |

## 2. proof1 缺陷复核（逐项实测，均已修）

- proof1 D1（P1 LA SETTIMANA 盒副标题越右边距 13.7 px）：**已修**。本轮 `measure_built.py de` 实测 D1 副标题 `Die Woche　Cosa succede, giorno per giorno` 墨迹右缘 1856.5 px，盒/边距 1862，清除量 **+5.5 px**，与 table-fix 预测一致；交付 PDF 200 dpi 像素：该行最右墨迹 SVG 1861.4，未越线。
- proof1 D2（P2 匹配题 b、d 首行越右边距 13.5/16.5 px）：**已修**。fix3 改写后 b `il ponte di barche per la festa in novembre`、d `la piccola luce di cera accesa in chiesa`；本轮 h-overflow 扫：两行均无页边标记；P2 全页像素最右墨迹仅 +0.4 px（`verde` 行末 `e`，见 §6）。
- proof1 其余已接受项未变：P3/P5 中部结构性留白（core 固有模式）、P3 末行 `costruzioni.`（见 §4）。

## 3. 内容事实与语言（全文 1317 行逐句读过）

- 意甲 11 轮 10 场结果全对，24 球；Lazio 29、Inter 28、Roma 27（罗马 31 球最佳攻击）、Milan 第 4 名 24 分、Como 23、Udinese 末位 5 分；12 轮 Lazio–Lecce 周六 21 日、Atalanta–Inter 周日 22 日 20:45、Monza–Fiorentina 周一 23 日 20:45。
- Nitto ATP Finals 都灵 11 月 15–22 日，决赛周日 22 日；Sinner 缺席、Zverev 第一、Cobolli 首秀、8 人/2 组/半决赛周六 21 日；欧国联意–法周四 12 日、比–意周日 15 日，文中未印赛果（截稿后开赛，留待 VOL.5）正确。
- Eurochocolate 佩鲁贾第 32 届 11 月 13–22 日，主题 «Fate dolci»，卡拉布里亚大区，«I tesori della Calabria Straordinaria» 周五 20 日 18:15，Massari 周日 22 日闭幕；Torrone 克雷莫纳第 29 届 11 月 7–22 日（16 天），主题 «Il Confine»，Torrone d'Oro 授予 Davide Simonetta（周日 22 日 11:00 Palatorrone），游行 16:00（>150 人），婚礼重演 17:00，压轴 «Il torrone va in brodo» 18:00；1441 婚礼传说已按传说表述；Torrazzo 为「意大利最高中世纪砖钟楼」（fix3 措辞，Mortegliano 113.20 m 居首的限定已隐含在「中世纪砖」中）。
- BookCity 米兰第 15 届 11 月 23–29 日，主题 «Il senno sulla Luna»，1,360 活动 / 2,487 人物 / 1,164 书 / 443 场地；开幕周一 23 日 20:00 Dal Verme（Colson Whitehead，两届普利策）；预展周日 22 日 16:00 Rovati 基金会（Edmund de Waal）。都灵电影节第 44 届 11 月 24 日–12 月 2 日（9 天）；Filmmaker Festival 米兰 11 月 14–22 日，周日 22 日闭幕；Alba 白松露集市第 96 届至 12 月 6 日。
- 2027 预算法：DPB 10 月 15 日送布鲁塞尔；增长 +0.8%、赤字 3.4%；部长会议 10 月 28 日批准；约 260 亿（已注明为报纸重建数）；法案号 C. 3174-bis；听证会 11 月 9–12 日（意银行、UPB、Giorgetti 部长周四 12 日）；修正案截止周二 17 日 18:00；终批截止 12 月 31 日；Irpef 第二档 33% 由 5 万延至 5.5 万；约 50 亿来自银行/保险。P1/P2/P6 均有「PROPOSTA ≠ LEGGE」提示；P6 练习图表已标注虚构数据（Torino 5° / Milano 6° / Bologna 7° / Roma 11° / Napoli 13°；Q83 Torino 最冷、Q84 Napoli 最热、Q85 13−11=2、Q86 6+7=13，全对）。
- 威尼斯：Madonna della Salute 11 月 21 日，1630 誓愿，Longhena 圣殿 1631–1687 年，castradina 11 月 20 日晚；植树节 11 月 21 日（1898 首届、2013 立法）；圣塞西莉亚 11 月 22 日。
- **日期/星期全验**（`TZ=Europe/Rome date -d`）：11 月 6 日周五、7 日周六、8 日周日、9 日周一、12 日周四、13 日周五、14 日周六、15 日周日、16 日周一、17 日周二、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、12 月 2 日周三（TFF 9 天：11 月 24 日–12 月 2 日）、12 月 6 日周日、12 月 31 日周四、10 月 15 日周四、10 月 28 日周三——与文中全部星期表述（VEN 6.11 / SAB 7.11 / DOM 8.11 / giovedì 12 / martedì 17 / lunedì 23 / martedì 24 / LUN 16 / MAR 17 / GIO 19 / VEN 20 / SAB 21 / DOM 22）一致。LA SETTIMANA 无周三 18 日条目（fix3 已接受 D12，不虚构）。
- 意大利语正文与德语讲解层逐句读过：拼写/语法/术语/性数配合无问题。150 题答案键全部读过：P2 25–28（salute→c、ponte votivo→b、candela→d、piantare→a）、P4 52–55（vetta→d、imbattuto→b、girone→c、debutto→a）、P8 F 141–144（manovra→d、deficit→c、copertura→b、scaglione→a）均正确；Q137–140 翻译正确（E 区标签已为德语 `Übersetzen`，无「翻譯」残留）；Q58 più bella、Q59 meglio、Q82 Falso、Q120 B（TFF 11 月 24 日）、Q149 B 均核对。P7 FRASI 8 条引文逐字核对原文及页码（P1 ×2、P2、P3、P4、P5、P6 ×2）无误；Q150 范文实数 **99 词**；P7 ERRORI TIPICI 4 项正确（德语注各 1 行）；LETTERE 为标注的编辑示例 + 德语说明（无真实来信，W46 模式）；VOL.5 预告栏在位。
- **标题数实测**（「56 titles」是幻数）：机械规则（`## ` 页标题 + 全大写字母行）计 **104** 个标题行；清洗后：8 页标题 + 28 个练习节字母（A–H）+ 9 个日期标签 + 3 个 IN BREVE kicker 词 + 2 个级别徽章残片 = 54 个全大写具名标题，另 7 个句首大写文章标题（6 篇头条 + `I RISULTATI DELL'11ª GIORNATA`），合计本版实有 **61 个具名标题**。56 与任一口径均不符。
- CJK 扫描（.text.md）：**汉字 0 个**（无「翻譯」/任何中文残留）；全角冒号 ×14（冻结的动词范式注 16–20、60–61，各在练习与答案中出现一次）；U+3000 ×106（家具分隔符，豁免）。ABSTRACT.txt：一行、德语、无 ASCII 双引号、含 Lucerna / 意大利目标名 / A2–B2 / 150 Übungen，事实与本期一致。
- fix3 九行核对（grep + 通读）：D1（`domenica sera`，P1/P4）、P2 b/d 改写、D11、P4 b/c、P8 F 短式（`un livello di reddito del sistema fiscale`）均在位，旧措辞无残留。

## 4. 版式几何——目视、奶油盒与孤儿

- 8 页交付印 PDF 200 dpi 全页渲染逐页目视（`out/pages/p-1.png` … `p-8.png`）：除 §5 两处盒标题溢出外，无溢出、重叠、压页脚、图片与出处问题，无豆腐块。P3/P5 中部结构性留白为 core 固有模式；P1 体育场照片注 "(Pagina 4)" 为指向体育版的交叉引用。
- 奶油盒纵向（9 盒 0.30 em 余量为负，−0.4…−1.5 px）：像素复核（`out/creambox-pixel.log`）全部为正真墨清除量 **+4.8…+5.8 px**，末行均无下行字母，属计量 artifact，不是漫出——与 proof1 的裁定一致。最紧为 P7 LETTERE **+0.7 px**，裁图目视（`out/crop-p7-lettere-bottom.png`）确认末行 `…gilt für VOL.5.` 的下行字母完整在盒内，盒底留白清晰。
- 孤儿扫 **0**：P3-main 末行 `costruzioni.` 为单字行，但它是文章最后一行（core 同文同断行，core y=1202.94，本版 y=1232.67；续栏 col 2 该高度无正文），不是栏断孤儿；其余单字节点均为徽章、题号、节标、练习短词等结构项，无栏底/栏顶单字孤儿。
- P8 家具行与范文行的页边越线见 §6（非缺陷）。

## 5. 缺陷清单

### D1 — P1 cifre 盒标题墨迹越出奶油盒右缘 138.5 px（本版级）

- **位置**：P1 右中奶油盒（rect x=538.5, w=422.5，右缘 961 px）顶部标题，SVG y≈1379。源码：`content12.py:44`（`f.box("LA SETTIMANA IN CIFRE　DIE WOCHE IN ZAHLEN", …)`）；盒绘制 `bslib4.py:174`（`box()`），标题绘制 `bslib4.py:186`（`self.p.text(x + pad, yy + tsize - 4, title, tsize, "sans", True, OLIVE)`）——**标题以单行 start-anchor 绘制，无任何宽度核对**，是根因。
- **证据**（三重独立验证一致）：
  - PIL 真墨迹量（SVG 源，Noto Sans CJK SC 23 px bold，build 同款 `measure.ink_right`）：墨迹右缘 **1099.5 px**，超盒右缘 961 达 **+138.5 px**。
  - 交付 PDF 200 dpi 渲染像素（`out/ann-p1-cifre-title.png`，红线=盒右缘 961，蓝线=墨迹右缘 1099.5）：`DIE WOCHE IN ZAHLEN` 整段落在奶油盒外的白纸上，目视可确认；盒底点采样证实奶油在 x=960 处结束、x=1000 处已是纸白。
  - 对照 core：core 同标题 `LA SETTIMANA IN CIFRE　数字看本周` 墨迹右缘 960.5 px，恰在盒内（−0.5 px）——溢出由德语讲解层加长引入，是本版级缺陷。
- **严重度**：高。标题过半落在盒外白纸上，全页目视即见（P1 全页图亦可见），违反盒标题须在盒内的版式规则；proofread-until-zero 的拦停项。
- **级别**：**本版级**（core 标题在盒内；同类缺陷亦见于 it-en：`THIS WEEK IN NUMBERS` 墨迹右缘 1117.5 px，+156.5 px——跨版共性，见 §7 备注）。
- **修法建议**：缩短德语标题半段（如 `DIE WOCHE IN ZAHLEN` → 更短的德语形式，使墨迹右缘 < 961），或令 `box()` 对标题做宽度核对/换行；改后重新量墨迹与重跑横向扫描验证。注意：occlusion 0 flags 测不出此类缺陷（无边框盒横向溢出在其盲区内），须以本轮的奶油盒扫描 + 渲染像素为准。

### D2 — P2 frase 盒标题墨迹越出奶油盒右缘 30.5 px（本版级）

- **位置**：P2 中栏奶油盒（rect x=538.5, y=1273.475, w=422.5，右缘 961 px）顶部标题，SVG y≈1300。源码：`content12.py:177`（`f.box("LA FRASE PER RICORDARE　MERKSATZ", …)`）；根因同 D1（`bslib4.py:186` 标题无宽度核对）。
- **证据**（三重独立验证一致）：
  - PIL 真墨迹量（同款方法）：墨迹右缘 **991.5 px**，超盒右缘 961 达 **+30.5 px**。
  - 交付 PDF 200 dpi 渲染像素（`out/ann-p2-frase-title.png`，红线=盒右缘 961，蓝线=墨迹右缘 991.5）：`MERKSATZ` 的 `SATZ` 部分落在盒外白纸上，裁图目视可确认。
  - 对照 core：core 同标题 `LA FRASE PER RICORDARE　口诀` 墨迹右缘 918.5 px，在盒内（−42.5 px）——溢出由德语讲解层加长引入，是本版级缺陷。
- **严重度**：中。溢出 30.5 px（约 23 pt），`SATZ` 尾部在盒外，近看可见；同类规则的拦停项。
- **级别**：**本版级**（it-en 同标题 `REMEMBER` 墨迹右缘 1001.5 px，+40.5 px——跨版共性）。
- **修法建议**：同 D1，缩短德语半段（如 `MERKSATZ` → 更短形式）或 `box()` 标题宽度核对；改后重测。

## 6. 实测未列为缺陷的项（数值在案，供协调员复核）

- **P8 家具行越过版心右边距 +2.4 px**：`Jede Antwort hat eine einzeilige Notiz auf Deutsch　✓ = Modelltext-Aufgabe`（P8 y=1382，`content8.py` 家具行），PIL 真墨 1862.3（+0.3 px），交付 PDF 像素最右实墨 1864.3（+2.4 px，灰度 104 的实墨，非抗锯齿边）。未列为缺陷的理由：① 幅度仅 2.4 px（≈1.8 pt），在 66 pt 宽的版心边距内，无裁切、无重叠、无遮挡，occlusion 0 flags；② 同型家具行在 it-en 亦超 +1.8 px，是跨版系统性的「贴边家具行」渲染度量效应，非本版独有；③ proof1 同口径仅将 +13.5 px 以上列为缺陷，+0.2 px 项未列。裁图 `ann-p8-furniture.png`（红线=边距 1862）存档。
- **P8 范文行越过版心右边距 +1.4 px**：`Testo modello: Domenica 22 novembre metto la sciarpa e`（P8 col 3），PIL 真墨 1861.5（盒内），像素最右实墨 1863.4。未列为缺陷：该行是冻结意大利文，与 core 逐字节相同，且 core 同行像素亦为 +1.4 px——core 已复校 (a) 时即在，属 core 级固有特征，非本版可改（改即破 freeze）。
- **P2 `Una festa, una giornata verde` / P5 Corot 图注越边距 +0.4 px**：像素最右实墨 1862.4，灰度 104 的实墨仅 1 列渲染像素（0.48 SVG px），属光栅化亚像素噪声，未列为缺陷。
- **P7 LETTERE 盒底真墨清除量仅 +0.7 px**：在盒内（见 §4 裁图），紧但合格，未列为缺陷。
- **其余 15 处 PIL 页边标记**（`out/h-overflow.log`）：交付 PDF 像素复核后，页脚 `Seite N von 8` 各行最右墨迹为 SVG 1861.0（在边距内），PIL 的 +0.2/+0.4 px 为度量舍入，未列为缺陷。

## 7. 备注（非缺陷，供协调员知悉）

- 两项缺陷的根因在共享机制 `bslib4.box()`（标题无宽度核对），长读者语标题的版都可能中招：本轮实测 it-en P1/P2 同类标题分别 +156.5/+40.5 px；fr/pt/nl/ru 等长标题版建议在各自 proof2 中以同一奶油盒扫描复核，不要只信 occlusion。
- 重扩散报告称「Visual check 8/8，0 defects」，但其 P1 全幅目视只核了 D1 副标题，未核 cifre 盒标题；occlusion 对此类溢出是盲的。proof2 的奶油盒扫描补上了这一盲区。
- KIT §7 未印文本 SHA（仅字节+行数），三 SHA 中文本一件以 56,699 B / 1317 行对上盘上实测，见 §0。
- 复校全程 `PYTHONDONTWRITEBYTECODE=1`，TMPDIR 指向本 scratch 的 `tmp/`；除交付的 PROOF-NOTE.md / GATE-LOG.md 与 scratch 内的日志/裁图外，未写任何生产文件；未触 web PDF 的构建（只比文字层）。

## 附：证据文件索引（均在 scratch 内）

- `out/run.log` — run.py 全日志（RC=0，150 题，0 溢出）
- `out/rebuilt-names.sha256`、`shipped-svg.sha256` — SVG 重建 8/8
- `out/render.log` — 重渲印 PDF 日志（SHA 与交付一致）
- `out/freeze-baseline.log`、`out/freeze-baseline.json` — freeze baseline 8/8
- `out/gates.log` — 20 门全过（含 freeze diff / p8 / §1.1 / textmd validate / 150 键复核）
- `out/occlusion.log` — occlusion 0 flags（selftest OK）
- `out/p8-extract.json`、`out/p8-compare.json` — p8 150/150，CLEAN，keydiff [137,138,139]
- `out/measure-de.log` — D1 副标题 +5.5 px（proof1 D1 已修证据）
- `out/h-overflow.log`、`out/pixel-edge.log`、`out/overmargin-gray.log` — 横向 spill 扫 + 像素裁定
- `out/creambox.log`、`out/creambox-pixel.log` — 奶油盒全扫 + 像素复核
- `out/orphan.log` — 孤儿扫 0
- `out/pages/p-1.png` … `p-8.png` — 交付印 PDF 200 dpi 全页渲染（目视底本）
- `out/ann-p1-cifre-title.png`、`out/ann-p2-frase-title.png` — D1/D2 盒缘标注裁图
- `out/ann-p8-furniture.png`、`out/ann-p8-modeltext.png`、`out/ann-p2-line.png`、`out/ann-p5-credit.png` — §6 越线项标注裁图
- `out/crop-p7-lettere-bottom.png`、`out/crop-p1-cifre.png`、`out/crop-p2-frase.png` — 盒底/盒标题裁图
- `h-overflow-proof2.py`、`creambox-proof2.py`、`pixel-edge.py`、`pixel-p8.py` — 本轮自写扫描脚本
