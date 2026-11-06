# 独立校对报告 — W45 IT×DE（意大利语正文 × 德语讲解，VOL.2）

**结论：ZERO PROBLEMS — 通过，可交付（入仓由主线执行；本校对未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录）。**

- 待审交付：`files/weekly-report-w45-it-de/`（svg×8、cards×8、print `La-Lucerna-VOL2-DE.pdf` 7,174,780 B sha256 `a9f74664ee9952487fc79345ba550e6292a3c725276222fe1aaf0887ac4775da`、web `La-Lucerna-VOL2-DE-web.pdf` 3,643,700 B sha256 `aa4b340ecabf85f50ba92d8b48f30b02a6ef5aae0ad6dfd3f04cac2dcf8facaa`、`WEEKLY-KIT.md`、`ABSTRACT.txt`）。
- 对照核心：`files/weekly-report-w45-it-core/`（8 SVG sha256 前 8 位：p1 `81051bbb…`、p2 `d42ce9ae…`、p3 `9e45586d…`、p4 `62f75269…`、p5 `c907b869…`、p6 `5545f8dd…`、p7 `9fc999f4…`、p8 `3b87e54f…`，与 KIT §2 宣称逐位一致）。
- 对照 W43 同配对：`files/weekly-report-it-de/`（已上架 VOL.1）。
- 工具：`tools/venv/bin/python` + `tools/freeze.py`、`tools/p8.py`、`tools/occlusion_audit.py`（自检 6 类全触发）；补充自写扫描仅存本目录（`geom.py`），未改动共享工具。
- 证据文件（本目录）：`freeze-diff.json/txt`、`removed-strings.txt`、`deletion-adjudication.txt`、`p7-p8-detail.txt`、`p7-p8-detail2.txt`、`gloss-quotes-reader.txt`、`quotes-reader2.txt`、`quotes-wordsource.txt`、`furniture-w43.txt`、`images-pdf.txt`、`pdf-size-analysis.txt`、`counts.txt`、`counts2.txt`、`geometry-supplement.txt`、`geom.py`、`hash-before.txt`、`hash-after.txt`、`hash-core-before.txt`、`hash-core-after.txt`。

## 0. 开工查重

- 首次检查时无进行中渲染进程；距最后写盘（2026-10-27 23:12 UTC 的 ABSTRACT/KIT）75 秒复查 + 后续全程：交付与核心目录在 23:14 UTC 后**零新写盘**，判定为已完成交付，安全开工，未 stand down。
- 校对前后哈希比对：交付 18 文件（8 SVG + 8 卡片 + 2 PDF）**全部不变**；核心 8 SVG **全部不变**。校对未改动任何源码与交付物。

## 1. 冻结门

- `freeze.py baseline`（核心构建 `hidden_files/weekly-report-w45-it-build`，经工具自身 repoint 到 `tools/scratch/baseline-itde-proof` 执行）：**8/8 SVG 逐字节复现**，且运行后核心 SVG 重哈希不变。
- `freeze.py diff`（核心 vs 本版，R2 SVG）：p1 +28/−26、p2 +35/−29、p3 +32/−31、p4 +29/−25、p5 +44/−35、p6 +31/−24、p7 +44/−41、p8 +171/−166（计数含重复串；与 KIT §2 一致）。**新增 CJK = 0（全部 8 页）**；本版 SVG 全文 CJK 字符 = 0；全文检索“桥接”= 0。
- 删除串逐项裁定（无 CJK 删除串共 9 条，其余删除串均含中文讲解层字符）：
  - P1–P5：**无**无 CJK 删除串——无意大利语正文串被删。
  - P6：1 条 `bollettino · modello`——纯折行：本版同坐标 (1451, 2191.42) 节点为更长的一行 `probabilità · media · bollettino · modello`，两词原样存活，系 gloss 串重排。
  - P7：1 条 `è probabile che / è possibile che / bisogna`——纯折行：本版同坐标 (989, 627.62) 为 `Nach è probabile che / è possibile che /`，次行 (989, 657.345) 即 `bisogna che steht der Konjunktiv; …`，三词原样存活。
  - P8：7 条，逐项贴出（核心 → 本版，余见 `deletion-adjudication.txt`）：103 `nevicare：nevica` → `nevicare: nevica`；17 `mettere：io → metto` → `mettere: io → metto`；18、19、20、60、61 同式。20 另含 `（lei）` → ` (lei)`。**除标点形态外无一词改动**（精细化见 §12-a：全角冒号变体实际为 `：` → `: `，即冒号 + 空格）。
- 意大利语正文冻结：P1–P7 无 CJK 删除串为 0 的组合 + 全部意大利语体裁定（§2、§5）+ P8 键 12 项逐字节同（§3），三方一致。

## 2. P7 词框（硬性门）

- 意大利语定义句（空白归一化后全文检索）：`« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone.`——**核心与本版均为逐字存在**。
- 仅 gloss 本地化为德语：核心 `assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。`（2 行，(1473, 1280.62/1309.02)）→ 本版 `assaggio = Kostprobe. Seite 3: gratis kosten beim Panettone-Finale.`（2 行，同坐标）。定义句本地化 = 0 处。**硬性门通过。**
- 其余 P7 意大利语诊所句、纠错句、8 金句节点均与核心逐字节同坐标（见 §5）。

## 3. P8 门

- `p8.py compare`（显式核心/分版 P8 路径，total 150）：**CLEAN，150 noted = 150 noted，missing=[] extra=[] uncertain=[]**，keydiff = [6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 102, 137, 138, 139]——与 KIT §7 逐位一致。
- 15 项逐项对照印刷行（核心 → 本版，键部逐字节同者 12 项）：
  - 括号分支伪影 12 项：6 `previsioni`（`previsioni = 预报（复数）` → `Vorhersagen (Plural)`）；13 `guanti`；14 `crisantemi`；15 `termosifoni`；16 `fa`；20 `resta`；38 `mandorle`；58 `più bella`（核心注 `周日晚最美（主观评价）` → `Sonntagabend am schönsten (subjektiv)`，键同）；71 `gratuiti`；74 `castagne`；77 `ci sarà`；102 `fa`。12 项印刷键**全部逐字节相同**，仅注释译为德语 + 括号全角 → 半角。伪影机理与 KIT 所述一致（核心尾部全角括号组使工具走 paren 分支）。
  - 真重定向 3 项：137 `周一第一场寒冷来了。` → `Am Montag kommt die erste Kälte.`；138 `观众可以免费品尝。` → `Das Publikum darf gratis kosten.`；139 `周日晚上，佛罗伦萨对尤文图斯。` → `Am Sonntagabend spielt Fiorentina gegen Juventus.`。138/139 注释折行续行已核实（138 续行 `kosten` → 读作 `gratis kosten`；139 续行 `es wird gespielt` → 读作 `si gioca = es wird gespielt`，空格连接，与 KIT 所述一致）。
  - **139 为重定向而 140 不是的原因（实测）**：E 节（TRADUCI）137–139 题面为意大利语句 → 空白（意→读者语翻译题），故核心键本身就是读者语译文（中文），分版键须重定向为德语；140 题面在核心为中文句 `每个预报都必须清楚。→ ___`，在本版为德语句 `Jede Vorhersage muss klar sein. → ___`，答案方向是读者语 → 意大利语，键在两版均为意大利语 `Ogni previsione deve essere chiara.`，仅注释 `dovere = 必须` → `müssen`。W43 同配对呈完全同构：137/138/139 键为德语、140 键为意大利语 `Ogni cifra deve avere una fonte.`。**140 保留意大利语键正确，不是遗漏。**
- P8 注释纯德语：P8 CJK = 0；全角括号 `（）` = 0，全角冒号 `：` = 0；半角括号 28 对。
- P8 括号半角 `()` 形式：与 W43 已上架版对照——W43 P8 全角括号 0、半角 31 对，本版全角 0、半角 28 对（对数差为内容题量结构差，非形式差）。**形式与 W43 一致，胜过核心全角 `（）`（核心仅包裹中文注释）。**
- P8 分隔符 `— PAGINA N —`：本版 P8 含 PAGINA 1–8 全套、SEITE 0 处；核心 P8 同为 PAGINA 1–8；W43 P8 同为 PAGINA 1–8。**沿用 W43 已上架版正确，tables.json 通用德语 `— SEITE N —` 在此配对不适用（KIT §3 偏差说明属实）。**

## 4. 几何门

- `occlusion_audit.py`（自检 6 类全触发）：**分版 0 / 核心 0 / NEW 0，exit 0**。
- 右缘 ADVANCE 法（PIL 实测，[40, 1910] 框带）：**8 页 0 标记**。页脚 advance：左串止于 1103.9（自 x=65 起宽 1038.9，与 KIT 宣称的 W43 量值一致）、右页码行起于 1767.9，净空 664.0 px，8 页相同。
- 同基线碰撞扫描（全部同 y 文本节点 advance 盒）：**8 页 0 重叠**。P1 顶带 y=92：左止 392.3 → 中起 643.7 → 中止 1306.3 → 日期起 1450.6（与 KIT §8 逐值一致）。
- P6 图表标签覆盖（基线锚定墨迹法，PIL getmetrics、anchor `ls`、后绘 rect vs 标签墨迹）：**全部标签最高 0.0%**（含 Torino/Milano/Bologna/Roma/Napoli 及数值标），门限 <30% 全幅通过。卡片目视亦确认柱条与标签/数值无接触。
- 全 8 页框线压框 + 右缘扫描：审计 0 标记 + ADVANCE 0 标记 + 卡片目视 8/8 无压框/截断（§11）。
- 流程终值复测：R2 构建日志值 P1-headline 1497、P7 col3 1673.0、P6-ex 2569、P8-keys 2529 均在 `build-log-r2.txt` 中重读确认；节点几何佐证其三：P8 末键基线 2513.3（+15.7 ≈ 2529）；P7 col3 末节点基线 1667.95（+5.05 ≈ 1673.0），距 FRASI 规则线 1686 恰 13 px；P6 末练习基线 2540.55（+28.45 ≈ 一个行距 2569，底 2580 与核心同）。P1-headline 1497 为 flow 内部坐标（多栏流终点），SVG 节点无法单独还原该量，报告如实记为日志值（非节点推导值）；独立几何审计 0 标记 + 卡片目视不依赖该量。
- R1→R2 修复范围（哈希 diff 核实）：`sha256-r1.txt` → `sha256-r2.txt` 恰为 **p1/p2/p7 的 SVG + 卡片 + 双 PDF** 变化，其余 15 项（p3–p6、p8 SVG/卡片）纹丝不动。R1 的 6 个 NEW 经 `occlusion.txt` 重读：EDGE P1 脚注、LINEX P1 parola 注、BOXTITLE P1 settimana 副题、BOXTITLE P1 脚注、BOXTITLE P2 frase 标题、BOXTITLE P7 parola 标题——**6 项全部是德语讲解层溢出**（脚注占 2 项），终版审计 0 标记，**已全部消除**。R1→R2 五处收紧逐项落地：脚注拆为两短行（(1473, 1237.2/1263.2) `Termine nach Veranstaltungskalendern; / Zeiten können sich ändern.`）；parola 注单行化（(1451, 1846.3) `„il primo freddo“: Kälte nach mildem Herbst.`，在 1864 规则线上方）；settimana 副题缩为 `Der Wochenplan · Giorno per giorno`（标题措辞收紧，正文无损）；P2 frase 标题 `LA FRASE PER RICORDARE · MERKE`；P7 parola 标题 `LA PAROLA · WORT DER WOCHE`（去 `DAS`，与 W43 形式同）。

## 5. gloss 与金句

- 核心 gloss() 源串（核心构建 `content*.py`，按 `·` 拆分，README §21 法）：P2 6（il cappotto · la sciarpa · i guanti · a strati · il termosifone · il crisantemo）、P3 5（il panettone · il torrone · l'assaggio · la bancarella · il cantiere）、P4 4（la giornata · la presentazione · gli spalti · la sera）、P5 4（il cosplay · gratuito · il documentario · lo schermo）、P6 5（la probabilità · la media · il modello · il bollettino · aggiornare），**合计 24，从核心独立实测，非 PT 族 26**。
- 本版 gloss() 源串同分布同词头顺序（仅注释译为德语）；渲染后 24 词头**逐项在对应页 SVG 中实测存在**（1:1）。
- P1 桥接词表（gloss 外）：核心 `il primo freddo · il versante adriatico · la previsione · assaggi` 4 项 → 本版 `il primo freddo · versante adriatico · previsione · assaggi` 4 项 1:1（versante/previsione 前冠词省略，词头身份无损，正文带冠词出现处未动；见 §7）。
- P7 金句 8 句：意大利语引文节点与核心逐字节同坐标；`(Pagina)` 标签序列本版 = 核心 = **(1, 1, 2, 2, 3, 4, 5, 6)**；词序列法逐句核实：8 句内文词串在所标源页（P1×2、P2×2、P3、P4、P5、P6）与 P7 均存在（方法差异见 §12-c）。

## 6. 读者园地

- 意大利语信件逐字保留（P7 LETTERE 框，同坐标）：`«Ciao! Sono Li, studio italiano a Pechino. Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone — almeno in foto!» — Li` + `(esempio della redazione)`，与核心逐节点一致。
- 德语披露句逐字摘录（3 行，(1473, 1611.15/1639.55/1667.95)）：`Redaktionsbeispiel, keine Leserpost, kein bester Seite-8-Text. Schreiben Sie uns — die besten erscheinen in VOL.3!`
- 三事实齐全：① 无真实来信（`keine Leserpost` + `Redaktionsbeispiel` + `(esempio della redazione)`）；② 无最佳 P8 作文（`kein bester Seite-8-Text`）；③ 示例 + 顺延 VOL.3（`Redaktionsbeispiel` + `die besten erscheinen in VOL.3`）。零编造（无虚构读者、姓名、引文）。
- 显性德语邀请逐字：`Schreiben Sie uns — die besten erscheinen in VOL.3!`——祈使句（Schreiben Sie uns）+ VOL.3 刊登承诺（die besten erscheinen in VOL.3），位于读者框内，**成立**。
- **最佳 P8 作文覆盖范围裁定：通过（非阻塞），理由如下。** 邀请句字面 `die besten` 未限定类别（比 PT×DE 的 `Beste Briefe` 更宽，不专指来信）；其前一句披露句已显性点名两类顺延对象（`keine Leserpost, kein bester Seite-8-Text`）；同页预告行（意大利语冻结正文，非邀请本身、不计入邀请）显性点名两类：`le vostre lettere vere e i testi migliori della pagina 8`。三者合计，读者在 P7 一页内即被明确告知可寄信、可寄 P8 作文、最佳者见 VOL.3。先例：PT×DE 校对（`hidden_files/w45/pt-de-proof/REPORT.md`）对字面仅提来信的邀请句作同一裁定——“邀请句字面只提最佳来信，但最佳作文征集在同一页他处有显性表达……现行邀请门满足，不构成阻塞（同 PT×EN 裁定模式）”；PT×ES 校对亦明言“族内现行门从来是三者合计”。本版按同一标准通过；预告行本身未被计为邀请（邀请仅凭框内德语句成立）。

## 7. 家具（与 W43 同配对实测对照）

| 项 | W43 实测 | 本版实测 | 裁定 |
|---|---|---|---|
| P1 徽章串/槽位/字号 | (975, 574) 22pt 700 #a4553a 居中 `ITALIENISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER` | **逐字节同**（同坐标/字号/字重/颜色） | 一致（IT 族插入式，§20 情形适用：y=372 为冻结正文 strapline，徽章插于 574，带底 542 → 徽章 574 → 头 606，无位移） |
| 报头 | La Lucerna | La Lucerna（目标语冠词，意大利语） | 一致 |
| 页脚模板 | `La Lucerna · ITALIENISCHE WOCHENZEITUNG VOL.1 · TEXT AUF ITALIENISCH · ERKLÄRUNGEN AUF DEUTSCH` | 同模板，**VOL.2**（核心卷次驱动） | 偏差仅 VOL.1→VOL.2，合规 |
| 页码行 | `Seite N von 8`（8 页） | `Seite N von 8`（8 页） | 一致 |
| gloss 前缀 | `HINWEIS · `（全大写，W43 各页实测） | `HINWEIS · ` | 一致；**未照搬 NL 族 `Hinweis · `**（该族结论与本配对无关） |
| P8 分隔符 | `— PAGINA N —`×8 | `— PAGINA N —`×8 | 一致（见 §3） |
| 答题体 | 破折号体 `N. key — note` | 破折号体（答案生成码与核心同族，IT 为破折号族） | 一致 |
| 指令词 | Ausfüllen / Zuordnen / Sätze bilden / Übersetzen / Entscheiden / Schreiben 均在 W43 各页出现 | 6 词均在本版出现（页分布与当期题型对应） | 一致 |
| P1 顶带 | `OGNI SETTIMANA IN ITALIANO · ITALIENISCH, WIE ITALIEN ES LIEST` | 逐字同 | 一致；副标题 `ITALIENISCH · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A` 为当期主题，合规 |
| 级别/范文 | W43 实测：150 题，A2 46/B1 71/B2 33；范文 90 词（本校对自 W43 SVG 独立展开计数 + 范文逐词计数） | 150 题，**A2 47/B1 70/B2 33**；范文 **81 词**（与 W45 核心逐页逐级完全一致，见 §11） | 差异均为**核心驱动**，非分版改动 |
| P1 桥接 gloss 省略冠词 | W43 桥接词表含冠词 | versante/previsione 前冠词省略（§5） | 纯措辞收紧（德语长度所迫），词头与正文带冠词出现处无损 |
| P1 settimana 脚注拆两行 / P1 parola 注单行化 / P2 frase 标题 `MERKE` / P7 parola 标题去 `DAS` | —（W43 无对应） | 逐项落地（§4） | 纯措辞收紧，无内容丢失；P7 标题去 DAS 后与 W43 形式同 |
| 未列入 KIT §11 的两处德语半句译法差 | IN BREVE `KURZ NOTIERT`；ERRORI TIPICI `FEHLERKLINIK` | IN BREVE `KURZ GEMELDET`；ERRORI TIPICI `TYPISCHE FEHLER` | 两者均为正确德语、同义级译法，**非缺陷**；仅记为 KIT §11 偏差表完备性注记（见 §12-d） |

## 8. 图片

- 每页嵌入载荷（base64 解码 sha256 前 16 位 + SVG 显示尺寸）：P3 核心 = 本版 = `b074a3c2cfe1c8ad`（434×265）；P5 核心 = 本版 = `39eaac936006604a`（434×300）；其余 6 页核心与本版均无嵌入图片（图表为矢量绘制）。**各页载荷 = 核心，逐页一致。**
- 解码像素尺寸：P3 核心与本版均为 **1280×862**（构建员宣称核实）；P5 均为 1280×960。W43 P3 载荷与本版同（`b074a3…`，W43 另有一张 P3 第二图，本期核心无此图，核心驱动）。
- 署名在版：P3 `Foto: Wikimedia Commons — dominio pubblico`、P5 `Foto: Wikimedia Commons — CC0`，核心与本版逐字同，卡片目视均在图下。

## 9. 印刷 PDF 体量（构建员自承“未解”——本校对已核实解开）

- 内容等价性核实：本版 print 与核心 print 均为 **8 页**，页框尺寸**同为 (0, 0, 1462.5, 2025)**；P3/P5 嵌入图片字节量**逐页相同**（P3 1,740,912 B、P5 2,523,465 B）；文本**可提取**，且本版各页提取字符数均高于核心（德语注释长于中文注释，合理）；页脚/徽章文本在版（print P1 尾部提取出 `…ERKLÄRUNGEN AUF DEUTSCH Seite 1 von 8`，8 页页脚标记齐全；web PDF 为整页光栅化，8 页、页框 (0, 0, 1400, 1938) 与核心 web 版同，文本不可提取为 web 版固有形态，非缺失）。
- 体量差**本身不是缺陷**，机理已实测：两版 print 嵌入同一组字体面（NotoSerif/Sans CJK SC + UnifrakturMaguntia），但核心中文讲解层迫使每页嵌入约 0.93–1.03 MB 的 CJK 字形子集（NotoSansCJKsc Regular/Bold），本版德语层仅用拉丁字形，子集约 51 KB/面；逐面最大子集求和：核心 ≈17.21 MB，本版 ≈1.49 MB，差额 ≈15.7 MB 量级与文件差（21,037,777 − 7,174,780 = 13,862,997 B）吻合（子集按页分册，逐面取最大为近似口径，机理证据充分，非编造解释）。**内容无缺失，体量差不阻塞。**

## 10. ABSTRACT

- `ABSTRACT.txt`：德语**单行**（1 内容行 + 末尾换行），**无 ASCII 双引号**，长 300 字符。
- 内容：`La Lucerna VOL.2, 2.–8. November 2026: erste Kälte in Italien, Allerseelen am 2. November, Panettone-Weltmeisterschaft in Mailand am 7.–8. November, Torrone-Fest in Cremona und Serie A am 11. Spieltag – Italienisch lesen und lernen, mit deutschen Erklärungen, Niveau A2–B2, 150 Übungen mit Lösungen.`
- 真实主题关键词（erste Kälte、Allerseelen 2. November、Panettone-Weltmeisterschaft Mailand 7.–8. November、Torrone-Fest Cremona、Serie A 11. Spieltag）均与本期内容对应；学习者搜索短语（`Italienisch lesen und lernen`、`mit deutschen Erklärungen`）+ 刊名 + 目标语名 + A2–B2 + 150 题齐全。**通过。**

## 11. 卡片目视与独立计数

- 8 张卡片（1950×2700）**逐页目视**：P1（徽章、脚注两行、parola 注单行、页脚）、P2（MERKE 标题入框）、P3（照片 + 署名）、P4（赛程表）、P5（照片 + CC0 署名）、P6（图表标签/数值无遮盖、练习数据标注 `dati inventati` 在版）、P7（col3 与 FRASI 规则线间隙、词框/信框入框）、P8（答案末行距页脚净空）——**无重叠/截断/压框**。
- 题量与级别（渲染后 SVG 独立展开计数，chip→题号法，P8 限练习区）：本版 = 核心 = **150 题，A2 47/B1 70/B2 33**，页分布 **10/18/18/18/18/18/12/38**，题号集合恰为 1–150，无缺重。
- 范文：本版与核心范文**逐字相同**，除 `Testo modello:` 标签外 **81 词**（含标签 83 词）；P8 150 题行标注 `(81 Wörter)` 一致。

## 12. 与构建员自述不符处（即使非阻塞，一并列出）

- a. P8 7 行标点差：KIT 称“仅标点形态差”，实测为全角冒号 `：` → ASCII 冒号 **+ 空格**（`: `），另 20 项含全角括号 → 半角括号 + 空格。词级内容零改动，**非阻塞**，仅表述精细化。
- b. P6/P7“折行碎片”删除串：两碎片在连接后渲染文本中**原样存活**（P6 被更长 gloss 行包含；P7 `bisogna` 在次行），diff 条目反映的是节点/多重集切分 churn 而非删除。构建员“重排”定性属实，**非阻塞**。
- c. 金句“各 2×”：按 `«…»` 整节点精确计数，8 句中 7 句仅得 1×（正文出现处无 `«»` 包裹或句首大写不同）；按词序列法核实，8 句在所标源页与 P7 **均存在**，实质成立。**非阻塞**，仅方法口径差异。
- d. KIT §11 偏差表遗漏两处德语半句译法差（IN BREVE `KURZ GEMELDET`、ERRORI TIPICI `TYPISCHE FEHLER`，见 §7）。两者正确且同义，**非阻塞**，仅 KIT 完备性注记。
- e. 构建员“print PDF 体量未解”：本校对已用字体子集实测解开（§9），原观察不再成立。
- f. P1-headline 1497：为 R2 构建日志值，节点几何无法单独还原（其余三终值已节点佐证），报告如实区分（§4），**非阻塞**。
- g. 其余构建员自述经重测**全部属实**：冻结 8/8、diff 计数、CJK 0、P8 CLEAN 与 keydiff 列表、几何 0/0/0、ADVANCE 0、同基线 0、P6 覆盖 0%、R1→R2 变更范围、gloss 分布 24、金句标签、读者园地三事实与邀请句、家具 W43 项（除 §12-d 两处译法差外）、P3 1280×862、题量/级别/范文、双 PDF 哈希与字节数——无一不符。

## 13. 非阻塞观察

- 意大利语后无空格直连德语/中文注释的括号体（如 P1 cifre `leggera(mögliche Schneefallgrenze)`、P5 周计划 `Milano(Dienstag: …)`）为**核心原样体式**（核心同坐标为 `leggera（可能…`），非分版引入。
- P1 末行 `E lo sport chiude la settimana:` 为核心冻结句（同坐标），其续接为版面结构（雪花图框 + P4 体育），非截断。
- P2/P3/P4/P5 各页 `E TU?` 练习提示提及 VOL.3（如 P2 `le migliori escono nel VOL.3`）为练习题面，**未计入** P7 邀请（邀请仅凭 P7 读者框德语句成立）。
- 共享 scratch 目录未清理；`freeze.py baseline` 的输出位于工具自有 `tools/scratch/baseline-itde-proof/`，属工具正常写盘，非校对清理对象。

## 14. 阻塞项

**无。结论：ZERO PROBLEMS。**
