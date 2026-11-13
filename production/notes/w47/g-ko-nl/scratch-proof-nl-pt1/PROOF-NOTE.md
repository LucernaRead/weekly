# PROOF-NOTE — 2026-W47 · nl → pt（荷兰语目标语 × 葡萄牙语读者）· proof1 独立复校

- 版目录：`production/2026-w47/fanout-nl/2026-w47-nl-pt/`
- 复校员：独立复校（proof1）· 2026-11-11
- 依据：仓库根 `SOP.md`（proofread-until-zero；几何遮挡扫描必过；p8 compare 必跑；讲解/导读用读者母语；对外内容禁内部标签/周次/语言代码）

## 结论：(b) 有缺陷，不能定稿

共 **5 项缺陷**（重大 3 项：D1、D3、D4；一般 1 项：D2；轻微 1 项：D5），另 3 项观察（O1–O3，不计缺陷）。
150 题答案键手验 150/150 全部通过；全部 8 页已逐页目视；机械门除下列缺陷所指处外全部通过。
任务背景预期的 D3/D4（core 级 P2 选项 c 溢出、text.md「答案：」未本地化）均已照实复现；另新发现本版自有重大缺陷 D1（P6 框标题溢出）与 D4（类型标签未本地化）。
修复后须按 SOP §8 循环规则**整期重渲染、从头再做一轮全量校对**，直到一整轮零问题。

## 缺陷清单

### D1（重大 · 本版）— P6 框标题「VOOR OF TEGEN?　A FAVOR OU CONTRA?」横向溢出奶油盒右缘约 21–25 px
- **页码/定位**：P6 右栏「VOOR OF TEGEN?」奶油盒（SVG：x=1439.5, y=743, w=422.5, 右缘 1862.0）；标题基线 y=785，21 pt Noto Sans CJK SC Bold，起笔 x=1461.5。
- **归属**：本版（fan-out）。核心同标题「VOOR OF TEGEN?　正方还是反方」本轮 PIL 实测宽 326 px（21 pt），小于 400.5 px 内宽，合规；葡语 gloss「A FAVOR OU CONTRA?」把它拉长到 423 px，溢出。nl-de 同类 D2 为 +47–48 px（德语 gloss 更长）；本版 +21–25 px，仍为肉眼可见的溢出。
- **实测证据（三法一致）**：
  1. PIL 真墨水：ink right 1883.5（+21.5 px）。
  2. 印 PDF span：`A FAVOR OU CONTRA?` bbox right 1415.2 pt，盒右缘 1396.5 pt，+18.7 pt = +24.9 px。
  3. 200 dpi 像素扫描：该行最右墨点 1414.1 pt，+23.4 px。
  8 页目视复核：标题末「?」明显伸出奶油盒右缘，落在白纸上。
- **修复建议**：缩短葡语 gloss（如「A FAVOR / CONTRA」或拆行）或降字号至合规；修后按三法重测。注意 occlusion 审计对此类无边框奶油盒标题溢出是盲的（0 flags），不得以其为据。

### D2（一般 · 核心）— P2 D 节选项 c「c. eten voor het paard van Sinterklaas」超出右版心约 8.5–13.1 px
- **页码/定位**：P2 练习 D「WOORDEN」选项列，基线 y=2233，23 pt Newsreader，起笔 x=1473.5；右版心 1862.0 px。
- **归属**：核心（core 同文同位同字号，核心亦然；fan-out 未改动此行）。与任务背景预期一致（nl-de proof1 D3 同值）。根治在核心，但本版修时可随同重排选项行。
- **实测证据（三法一致）**：PIL 真墨水 ink right 1870.5（+8.5 px）；印 PDF span +9.8 pt = +13.1 px；200 dpi 像素扫描最右墨点 1405.2 pt，+11.6 px。目视：该行比同列其他行明显探出。
- **修复建议**：选项 c 换行或缩写（如「c. eten voor het paard」），使墨水右缘 ≤1862。

### D3（重大 · 核心/机制）— text.md 全文 150 处答案标记未本地化，中文「答案：」残留
- **页码/定位**：`2026-w47-nl-pt.text.md` 全文：142 处「— 答案：」+ 8 处配对题内「(答案 d · …)」型标记（#25–28、#141–144），共 150 处；除「答/案」外该文件无其他 CJK 字符（CJK 共 300 个，全为「答/案」）。印 PDF / 网 PDF 无此问题（pdftotext 0 处）。
- **归属**：核心/机制（nl-core 导出模板硬编码「答案：」）。核查：nl 全家 10 个 fan-out 版 text.md 各含 142 处同型标记、核心 168 处；其余语系已本地化（en-fr 用「— Correct:」，de-en/fr-de/es-de 均为本地化标记，0 处「答案」）。与任务背景预期一致（本版读者是葡萄牙语，「答案：」中文标记确为未本地化）。
- **为什么是缺陷**：text.md 是交付件（网站正文体 + SEO），葡语读者在每道题后都看到中文标记，违反「讲解层用读者母语」与对外内容语言一致要求。
- **修复建议**：导出模板按读者语本地化标记（葡语版：「— Resposta:」；配对题「(resposta d · …)」）；nl 全家 11 版同改。修后 grep 验证 text.md 中 CJK 字符为 0（U+3000 分隔符除外）。

### D4（重大 · 本版）— 练习类型标签未本地化：text.md 全 150 题英文标签 + 印刷版 59 处「Complete」
- **页码/定位**：两处表现，同一根因（葡语版类型名表未翻译）：
  1. text.md 内联标签：全部 150 题的 `[级别 · 类型]` 均为英文——complete 65、choice 44、cloze choice 13、make sentences 8、true or false 7、translate 4、matching 2、writing 1（144 个标签实例，配对题 25–28 与 141–144 各共用 1 个，覆盖 150 题）。
  2. 尾标与印刷版：text.md 尾标 `[Complete]` ×59 未本地化；印刷版 SVG 中 `Complete` ×59（P2 9、P3 13、P4 9、P5 10、P6 9、P7 9），在印 PDF 上直接可见（如 P3「B1 34. Complete」）。
- **归属**：本版（nl-pt fan-out）。横向对照：nl 全家其余 8 版类型标签全部已本地化——nl-es（Completar las frases / Una opción / Traducción）、nl-fr（Compléter les phrases / Choix unique / Traduction）、nl-it（Completa la frase / Scelta multipla / Traduzione）、nl-ko、nl-ja、nl-ru、nl-zh-tw；it-pt 亦为葡语本地化（Completa a frase / Escolha múltipla / Forma frases / Relaciona as palavras）。仅 nl-pt（与 nl-en——英文即读者语，正确）保留英文。
- **为什么不是“本来就这样”**：同一文件/同一版内其他类型标签已是葡语——尾标「Forme a frase」×8、「Verdadeiro ou falso?」×7、「Traduzir para português」×2、「Traduzir para neerlandês」×2、「Escreva」×1，印刷版亦然（Forme a frase ×8、Verdadeiro ou falso? ×7、P8 E 节「Traduzir para português/neerlandês」）。只有 complete 类型漏译，且内联标签全系漏译，并非既定写法。
- **修复建议**：按读者语本地化类型名表（参照 it-pt/nl-es：complete→「Completa a frase」/「Completar」，choice→「Escolha múltipla」，cloze choice→「Cloze」，make sentences→「Forma frases」，true or false→「Verdadeiro ou falso?」，translate→「Traduzir」，matching→「Relaciona as palavras」，writing→「Escreva」）；text.md 内联标签与尾标、印刷版标签同改；修后 grep 验证 text.md 与 SVG 中无英文类型词残留。

### D5（轻微 · 机制）— 网 PDF 丢失 P1 本周词斜体（nl-de D5 同类）
- **页码/定位**：P1「HET WOORD VAN DE WEEK」«de groepswinst»。
- **归属**：机制（tools/webpdf.py 字体裁切未带斜体面）。
- **实测证据**：印 PDF：该词 1 处 Newsreader Italic span（16.12 pt，bbox 1079.6–1201.8 pt）；网 PDF：全书 0 处 italic span，同词改用 LucernaNewsreader-Regular（bbox 宽 131.1 pt vs 印版 122.2 pt）。文字层本身完好：印/网 pdftotext 词多重集 diff 为 0（各 8000 词），无空格丢失、无闭引号脱离——三联症其余两项未复现。
- **修复建议**：webpdf.py 裁切字体时带上 Newsreader Italic 面；修后核查网 PDF 全书 italic span 数 = 印版数（本版：1 处）。

## 观察事项（不计缺陷）

- **O1**：P2「EN JIJ?」奶油盒末行「em neerlandês e envia-as à redação.」真墨水距盒底仅 0.9 px（盒底 1445.8 px，墨底 1444.9 px；ç 降部所致；baseline 余量 +5.6 px，desc-clear −0.4 px）。紧但在内，按 nl-de 同类先例（0.4–0.5 pt 紧但在内）不计缺陷；重建时给该盒 +2 px 底垫即可消除风险。P5 同型盒末行墨底余量 5.6 px，P3 16.0 px，均安全。
- **O2**：P1「HET WOORD VAN DE WEEK」葡语 gloss 第二行「direto aos quartos de final.」落在全幅分隔线（y=1853）之下（首行基线 1846.2、次行基线 1871.85；线两侧各约 5 px，文字不触线、不跨线）。与 nl-de 同几何、同裁决，不计缺陷。
- **O3**：P7「HET WOORD　PALAVRA DA SEMANA」标题极紧：PDF span 指标称 +1.5 px 溢出，但 200 dpi 像素真墨水为 −0.6 px（墨右 1396.1 pt，盒右 1396.5 pt），以像素为准判在内，不计缺陷。

## 判为非缺陷的项（摘要，详见 GATE-LOG）

- 几何遮挡审计 0 flags（自检通过）；creambox 全版扫描仅 2 处负 clearance，均为盒下相邻标题的已知假阳性（+24/+32 px）；P7 toolbox 实测 min inside clearance +13.1、min desc-clear +7.1，像素复核三盒墨底余量 13.1/13.1/24.1 px；P3/P5 右栏奶油盒末行降部无溢出（像素：P3 −16.0 px、P5 −5.6 px）。
- P1 框标题「IN DEZE EDITIE　NESTA EDIÇÃO」三法一致在内（PIL −29.5 px、span −27.9 px、像素 −29.4 px）——nl-de D1 在本版未复现。P2「ZO ONTHOUD JE HET　LEMBRA-TE」PIL −14.5 px，在内。
- freeze baseline 8/8；freeze diff 新增 CJK 仅 7 个 U+3000（SOP §1.1 规定的全角空格分隔符，非中文）；移除串孤儿仅两项，均已裁定：（a）刊头「LUCERNA DUTCH WEEKLY」→ 葡语刊头副标（fan-out 设计）；（b）「perfectum」→ 葡语「perfeito」（P8 答案注 40/42），讲解层合法翻译。
- p8 compare CLEAN，keydiff [137, 138] 为翻译题合法重定向（键本身正确：137「As notícias do Sinterklaas passam todos os dias às 18:00.」；138「Os dois primeiros passam aos quartos de final.」）；139、140（葡→荷）键与核心一致。P8 extract 150/150。
- P8 最小字号实测 10.12 pt（SOP §1.1 让步阶梯允许 ≥9.75 pt），合规，非缺陷。
- 弯引号：全版仅成对 « »（P1/P2 各 2 对、P7 30 对、P8 2 对）；U+201C/U+201D/U+2019/U+201E 均为 0；text.md 10 处直引号全为荷兰语 `'s` 属格（'s avonds 等），与核心一致，非缺陷。
- ABSTRACT.txt：葡语单行 320 字节，含「Lucerna」「VOL.4」、目标语名、A2–B2、150 题；「Lucerna VOL.4」写法与 nl 全家 8 版一致（nl-de「Lucerna Niederländische Wochenzeitung VOL.4」、nl-es「Semanario neerlandés de Lucerna VOL.4」等），pt-zh-tw D4（摘要全文无「A Lucerna」亦无「VOL.4」）在本版未复现——「A Lucerna」是葡语目标语版的刊头（core-pt），本版目标语为荷兰语、刊头为「De Lucerna」，摘要取全家通行的裸「Lucerna VOL.4」写法，不计缺陷。
- P8 答案键与 text.md 键逐题比对：149/150 逐字一致，唯一形式差异 #150 为开放写作题——印刷版键为「✓」，text.md 为「(tarefa aberta, texto modelo abaixo)」，语义相同；范文 81 词（80–100 内）。
- P7 八句金句逐字出自本期正文，页码标注正确（P1×2、P2、P3、P4、P5、P6×2）；P1「IN DEZE EDITIE」页码 Pag. 2–8 与实际页码一致；7 张照片均带目标语图说 + CC0/公有领域出处（Wim van Rossem/Anefo、Anefo、W. Punt/Anefo、Spaarnestad Photo/Wikimedia、Elise lovenko/Unsplash、Cristina Gottardi/Unsplash、Aaron Burden/Unsplash）。
- 外部事实 7 组全部核实属实（见核实摘要）；日期/星期 8 个全部用日历核验吻合；算术题重算（19 天、1 天、4 小时、17 年、65、100）全对。

## 核实摘要

- **身份核对**：印 PDF SHA `d70937d8…e4cc5`、网 PDF SHA `05faf026…7658e`、text.md SHA `5b353380…2d5` 与任务一致；字节数 12,671,956 / 1,582,075 / 46,025。
- **全文通读**：text.md 全文 430 行 + 印 PDF 8 页逐页目视（150 dpi 自渲染）；日期/星期全部用日历核验（14/11 周六、15/11 周日、16/11 周一、21/11 周六、22/11 周日、24/11 周二、29/11 周日、5/12 周六，全部吻合）。
- **外部事实来源**（2026-11-11 检索）：
  - **Nations League A2 组积分榜**（题 2、3、6、9、48、53、54、114、115 的事实基础）：myfootballfacts/NBC Sports（UEFA 官方数据）：NED 4 战 2-2-0、7–5、8 分；GRE 8 分（5–3）；GER 5 分；SRB 0 分——与正文「8/8/5/0」「7 tegen 5」及各场比分（荷 1–1 德、2–1 塞客、2–2 希客、2–1 塞主；德 0–1 希主、2–0 塞、0–0 希）全部吻合。
  - **PSV 26 分**（题 63、126）：PitchLab Eredivisie 2026/27（2026-11-08 更新）：「PSV Eindhoven top the table … with 26 points from 12 games」；VAVEL：「PSV lead the table with 26 points after 12 matches」；Cambuur–PSV 2–5（8 Nov）多源一致；NEC–PSV 21 Nov 15:30 UTC = 16:30 CET（与 P4「16:30 uur」吻合）。
  - **Heerenveen–Feyenoord 5–3**（题 59、64）：Sportradar/Sky Sports：8 Nov 2026，Abe Lenstra Stadion，5–3（Meerveld 帽子戏法）。
  - **Grave 入城**（P1/P3）：vandaagingrave.nl：Landelijke intocht 2026 in Grave，14 november 2026 周六，Maaskade，市长 Marieke Moorman，NPO Zapp (NPO 3) 直播，Merel Westrik 主持，节目 12:00–16:00；mamaliefde.nl：同上 + 约 12:00 靠岸。——全部属实。（马名 Ozosnel 本轮未做外部核实，题 21 键只依赖文内一致性：P2 正文「Het paard van Sinterklaas, Ozosnel」与键一致。）
  - **阿姆斯特丹入城 88 届**（P3；闭合 nl-de O1）：uitamsterdam.com / amsterdam.org：2026-11-15 周日，10:15 De Omval 出发，11:30 Scheepvaartmuseum，13:00 Stopera 骑行出发，经 Rembrandtplein（13:15）/Utrechtsestraat（13:20）至 Leidseplein；88e editie（amsterdaminside + 市政府清单）。——全部属实。
  - **下期预告欧战**（P7 VOLGENDE WEEK）：UEFA.com 2026/27 Champions League 赛程：Matchday 5，Tuesday 24 November 2026，Feyenoord vs Porto、Real Madrid vs PSV Eindhoven。——属实。
  - **Feyenoord–Ajax 29 Nov**（P7 VOLGENDE WEEK）：FR12.nl / Sportradar：周日 29 November 2026，14:30，De Kuip，Eredivisie 第 14 轮。——属实。
- **150 题手验**：`keycheck-150.json`，150/150 ok（程序比对 text.md 键 vs 印刷版 P8 键 149 逐字一致 + #150 开放题等义；语义逐题手验：配对题字母对照印刷版 a–d 列表核实——P2 D：a 列表/b 诗/c 食物/d 门口；P8 F：a 诗/b 新闻节目/c 小组头名/d 门口；算术重算；范文计词 81）。
- **源文件未动**：未改动、未重建、未 commit、未 push 任何源文件；全部工作在 goals 侧 scratch。
