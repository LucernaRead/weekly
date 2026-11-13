# PROOF-NOTE — 2026-W47 · nl → de（荷兰语目标语 × 德语读者）· proof1 独立复校

- 版目录：`production/2026-w47/fanout-nl/2026-w47-nl-de/`
- 复校员：独立复校（proof1）· 2026-11-11
- 依据：仓库根 `SOP.md`（proofread-until-zero；几何遮挡扫描必过；p8 compare 必跑；讲解/导读用读者母语；对外内容禁内部标签/周次/语言代码）

## 结论：(b) 有缺陷，不能定稿

共 **5 项缺陷**（重大 3 项：D1、D2、D4；一般 1 项：D3；轻微 1 项：D5），另 2 项未决（O1、O2）。
150 题答案键手验 150/150 全部通过；全部 8 页已逐页目视；机械门除下列缺陷所指处外全部通过。
修复后须按 SOP §8 循环规则**整期重渲染、从头再做一轮全量校对**，直到一整轮零问题。

## 缺陷清单

### D1（重大）— P1 框标题「IN DEZE EDITIE　IN DIESER AUSGABE」横向溢出奶油盒右缘约 32–34 px
- **页码/定位**：P1 右栏「IN DEZE EDITIE」奶油盒（SVG：x=1439.5, y=1312, w=422.5, 右缘 1862.0）；标题基线 y=1352，24 pt Noto Sans CJK SC Bold，起笔 x=1461.5。
- **归属**：本版（fan-out）。核心同标题「IN DEZE EDITIE　本期目录」宽 296 px、右缘 1757.5，合规；德语 gloss「IN DIESER AUSGABE」把它拉长到 434 px。
- **实测证据（三法一致）**：
  1. PIL 真墨水：ink right 1895.5（+33.5 px）。
  2. 印 PDF span：`IN DIESER AUSGABE` bbox right 1421.9 pt，盒右缘 1396.5 pt，+25.4 pt = +33.9 px。
  3. 200 dpi 像素扫描：该行最右墨点 1420.2 pt，+31.7 px。
  8 页目视复核：标题末字「AUSGABE」明显伸出奶油盒右缘。
- **修复建议**：缩短德语 gloss（如「IN DEZE EDITIE　AUSGABE」，实测须 ≤400.5 px 内宽）或降字号至合规；修后按三法重测。注意 occlusion 审计对此类无边框奶油盒标题溢出是盲的（0 flags），不得以其为据。

### D2（重大）— P6 框标题「VOOR OF TEGEN?　DAFÜR ODER DAGEGEN?」横向溢出奶油盒右缘约 47–48 px
- **页码/定位**：P6 右栏「VOOR OF TEGEN?」奶油盒（SVG：x=1439.5, y=743, w=422.5, 右缘 1862.0）；标题基线 y=785，21 pt Noto Sans CJK SC Bold，起笔 x=1461.5。
- **归属**：本版（fan-out）。核心同标题「VOOR OF TEGEN?　正方还是反方」宽 326 px、右缘 1787.5，合规；德语 gloss「DAFÜR ODER DAGEGEN?」拉长到 449 px。
- **实测证据（三法一致）**：PIL 真墨水 ink right 1909.5（+47.5 px）；印 PDF span +36.2 pt = +48.3 px；200 dpi 像素扫描最右墨点 1431.8 pt，+47.0 px。8 页目视复核：标题「DAFÜR ODER DAGEGEN?」明显伸出盒外。
- **修复建议**：缩短德语 gloss（如「VOOR OF TEGEN?　DAFÜR / DAGEGEN」或拆行）或降字号；修后三法重测。

### D3（一般）— P2 D 节选项 c「c. eten voor het paard van Sinterklaas」超出右版心约 11.5 px
- **页码/定位**：P2 练习 D「WOORDEN」选项列，基线 y=2233，23 pt Newsreader，起笔 x=1473.5；右版心 1862.0 px。
- **归属**：核心（core 同文同位同字号，P2 核心亦然；fan-out 未改动此行）。根治在核心，但本版修时可随同重排选项行。
- **实测证据（三法一致）**：PIL 真墨水 ink right 1870.5（+8.5 px）；印 PDF span +9.8 pt = +13.1 px；200 dpi 像素扫描最右墨点 1405.1 pt，+11.5 px。目视：该行比同列其他行明显探出。
- **修复建议**：选项 c 换行或缩写（如「c. eten voor het paard」），使墨水右缘 ≤1862。

### D4（重大）— text.md 全文 150 处答案标记未本地化，中文「答案：」残留
- **页码/定位**：`2026-w47-nl-de.text.md` 全文：142 处「— 答案：」+ 8 处配对题内「(答案 d · …)」型标记（#25–28、#141–144），共 150 处；除「答/案」外该文件无其他中文字符。印 PDF / 网 PDF 无此问题（pdftotext 0 处）。
- **归属**：核心/机制（nl-core 导出模板硬编码「答案：」）。核查：nl 全家 10 个 fan-out 版 text.md 各含 142 处同型标记、核心 168 处；其余语系已本地化（en-fr 用「— Correct:」，de-en/fr-de/es-de 均为本地化标记，0 处「答案」）。
- **为什么是缺陷**：text.md 是交付件（网站正文体 + SEO），德语读者在每道题后都看到中文标记，违反「讲解层用读者母语」与对外内容语言一致要求。任务必查项 (d) 的 E 节 type 标签本身已本地化（übersetzen 等，见 GATE-LOG §9），但答案标记属于同类未本地化残留。
- **修复建议**：导出模板按读者语本地化标记（德语版：「— Antwort:」；配对题「(Antwort d · …)」）；nl 全家 11 版同改。修后 grep 验证 text.md 中 CJK 字符为 0（U+3000 分隔符除外）。

### D5（轻微）— 网 PDF 丢失 P1 本周词斜体（ru-en D3 同类，1/3 复现）
- **页码/定位**：P1「HET WOORD VAN DE WEEK」«de groepswinst»。
- **归属**：机制（tools/webpdf.py 字体裁切未带斜体面）。
- **实测证据**：印 PDF：该词 1 处 Newsreader Italic span（16.12 pt，bbox 1079.6–1201.8 pt）；网 PDF：全书 0 处 italic span，同词改用 LucernaNewsreader-Regular（bbox 宽 131.1 pt vs 印版 122.2 pt）。文字层本身完好：印/网 pdftotext 归一化 diff 为空，无空格丢失、无闭引号脱离——D3 三联症的其余两项未复现。
- **修复建议**：webpdf.py 裁切字体时带上 Newsreader Italic 面；修后核查网 PDF 全书 italic span 数 = 印版数（本版：1 处）。

## 未决事项

- **O1**：P3 阿姆斯特丹入城路线/时刻细节（10:15 De Omval 出发、13:00 Stopera 骑行出发、经 Rembrandtplein/Utrechtsestraat 至 Leidseplein、「88e editie」）本轮未做外部核实。文中自洽（题 32、123 的 88e 与正文一致）；Grave 方面已外部核实无误（见核实摘要）。建议定稿前由协调员外部核对一次；此项不阻塞本版的关键（题键只依赖文内一致性）。
- **O2**：P2「ZO ONTHOUD JE HET　MERK ES DIR」标题超出盒右缘 0.5–1.0 px（PIL +0.5 px；印 PDF span +1.0 px；KIT 已注明“0.5 px past the box edge, invisible”）。边框不可见的奶油盒上 1 px 不可见，**不计为缺陷**；但修 D1/D2 时顺手缩短为宜（核心同标题仅 307 px，德语版 405 px 顶满 404.5 px 内宽）。

## 判为非缺陷的项（摘要，详见 GATE-LOG）
- 几何遮挡审计 0 flags（自检通过）；creambox 全版扫描仅 2 处负 clearance，均为盒下相邻标题的已知假阳性（+24/+32 px）；P7 toolbox 实测 min inside clearance +12.5、min desc-clear +6.5；P3/P5 右栏奶油盒末行降部：无溢出（PDF span 底缘全部在内，像素扫描确认；任务必查项 (b) 未复现）。
- freeze baseline 8/8；freeze diff 新增 CJK 仅 7 个 U+3000（SOP §1.1 规定的全角空格分隔符，非中文）；p8 compare CLEAN，keydiff [137, 138] 为翻译题合法重定向（键本身正确）；P8 extract 150/150。
- P8 最小字号实测 10.12 pt（KIT 数字属实；SOP §1.1 让步阶梯允许 ≥9.75 pt）。
- 弯引号：全版仅 1 对 „ "（P1「„Gruppensieg"」，合法德语引号）；U+201D/U+2019 为 0；「Sinterklaas' s」式间距与核心一致，非缺陷。
- PSV 26 分（题 63、126）已外部核实属实；intocht Grave 全部事实已外部核实属实；下期预告欧战对阵已外部核实属实（UEFA）。
- E 节 type 标签已本地化（übersetzen 等）；P8 答案键与 text.md 键 150/150 一致；范文 81 词（80–100 内）；P7 八句金句逐字出自本期正文（页码标注正确）；ABSTRACT.txt 德语单行 309 字节，无 ASCII 双引号。

## 核实摘要
- **身份核对**：印 PDF SHA `0df8e614…fc13e`、网 PDF SHA `8859e18a…f8de64`、text.md SHA `1531c25e…7a00d2` 与任务一致；字节数 12,669,843 / 1,581,124 / 46,161。
- **全文通读**：text.md 全文 + 印 PDF 8 页逐页目视（150 dpi 自渲染）；日期/星期全部用日历核验（14/11 周六、15/11 周日、16/11 周一、21/11 周六、22/11 周日、24/11 周二、29/11 周日、5/12 周六，全部吻合）。
- **外部事实来源**：PSV 26 分（VAVEL Eredivisie standings 2026/27，2026-11-08 更新；PitchLab；Cambuur 2–5 PSV）；Grave 入城（vandaagingrave.nl、kidsproof.nl、mamaliefde.nl：2026-11-14 周六、Maaskade、约 12:00、节目 12:00–16:00、市长 Marieke Moorman、NPO Zapp/NPO 3 直播、Merel Westrik 主持、Ozosnel）；欧战下期预告（UEFA.com 2026/27 Champions League 赛程：Matchday 5，2026-11-24 周二，Real Madrid vs PSV、Feyenoord vs Porto）。
- **150 题手验**：`keycheck-150.json`，150/150 ok；算术题重算（19 天、1 天、4 小时、17 年、65、100）；配对题字母对照印刷版 a–d 列表核实；P8 印刷键与 text.md 键逐题比对 0 不符。
- **源文件未动**：未改动、未重建、未 commit、未 push 任何源文件；全部工作在 goals 侧 scratch。
