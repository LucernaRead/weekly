# 独立校对笔记 — W47 意大利文核心版 (2026-w47-it-zh-cn, VOL.4)

- 校对员：叶子（独立校对，未改任何 core-it 文件；只读）
- 校对时间：2026-11-10 晚（截稿后）
- 校对对象：`~/workspace/weekly-git/production/2026-w47/core-it/`
  - 印刷 PDF `La-Lucerna-VOL4.pdf`（8 页，29,163,288 字节）
  - 网页 PDF `La-Lucerna-VOL4-web.pdf`（8 页，1,918,807 字节）
  - KIT `WEEKLY-KIT.md`，`2026-w47-it-zh-cn.text.md`，`ABSTRACT.txt`，`svg/` 8 个
- 结论：**(b) 缺陷清单 — 不是定稿**，须按 SOP §8 规则 4 修源码 → 整期重渲染 → 从头再做一轮全量校对。

## 缺陷清单

### 缺陷 1（硬）：P4 词汇配对 53 / 54 答案互换 — P8 答案印错两题
- 位置：P4 B·LE PAROLE（52–55 题）与 P8 RISPOSTE「— PAGINA 4 —」
- 证据（渲染成品 P4，可见）：
  - 左列：52. la vetta / 53. imbattuto / 54. il girone / 55. il debutto
  - 右列释义：a. la prima volta in un torneo importante / b. che non ha mai perso, ancora senza sconfitte / c. il gruppo di squadre che giocano tra loro / d. il primo posto in classifica, la cima
  - 正确配对：imbattuto → b（从未输过）；il girone → c（一组相互比赛的球队）。
  - P8 印的是：`53. c — imbattuto=不败的 c` / `54. b — girone=小组 b`——两题互换，全错。
- 证据（源码）：`content34.py` 约 199–200 行，`match_set` 的 keys 为 `["d","c","b","a"]`，应为 `["d","b","c","a"]`；`match_set`（`bslib4.py` 239–243 行）按列表顺序以 a/b/c/d 依次渲染释义，故字母顺序即证据。`.text.md` 第 497–499、1119 行载有同一错误答案，说明错在登记表本身，不在导出步骤。
- 对照：另两组配对已逐项核对无误——P2 25–28（c/b/d/a）与 P6 141–144（d/c/b/a）均正确。

### 缺陷 2（硬）：P4 第 11 轮赛果表把两场周六比赛错写到周五
- 位置：P4 `I RISULTATI DELL'11ª GIORNATA` 表，`VEN 6.11` 行
- 证据：表上 VEN 6.11 行列了 3 场：Venezia–Udinese 2–1、**Cagliari–Frosinone 1–0、Torino–Lecce 1–1**；SAB 7.11 行只列 Parma–Bologna 1–2、Roma–Sassuolo 3–0。
- 事实（多源一致）：Cagliari–Frosinone 与 Torino–Lecce 均在**周六 11 月 7 日 15:00**踢：
  - antoniogenna.com（2026-11-09 刊，逐日逐时赛程）：Venerdì 6 novembre 只有 Venezia–Udinese 2–1（20.45）；Sabato 7 novembre：Cagliari–Frosinone 1–0（15.00）、Torino–Lecce 1–1（15.00）、Parma–Bologna 1–2（18.00）、Roma–Sassuolo 3–0（20.45）。
  - tuttoatalanta.com（11 月 8 日 00:41 版，周六赛程）与 minuto91.it 亦一致。
- 正确分组：VEN 6.11 仅 Venezia–Udinese；SAB 7.11 为 Cagliari–Frosinone、Torino–Lecce、Parma–Bologna、Roma–Sassuolo；DOM 8.11 五场不变。
- 其余赛果与积分榜核无误：10 场比分、24 球、Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Frosinone 20 / Juventus 18 / Bologna 17 / Cagliari 16 / Napoli 15 / Torino 14 / Atalanta 14 / Genoa 13 / Lecce 10 / Fiorentina 9 / Parma 8 / Sassuolo 8 / Monza 7 / Venezia 6 / Udinese 5，均与 minuto91 / tuttoatalanta / antoniogenna / sportradar 一致；第 12 轮赛程（11 月 21–23 日，含 Atalanta–Inter 周日 20:45 贝加莫）亦与 antoniogenna 的下轮表一致。

### 缺陷 3（硬）：都灵电影节日期两头都错，波及 P1、P5、P8 共 6 处
- 事实（官方规程，FilmFreeway，2026-03-06 更新，英意双语一致）：
  > "The 44th Torino Film Festival will be held from Tuesday, November 24th to Wednesday, December 2nd, 2026, for a total of nine days."
  > "Il 44° Torino Film Festival si svolgerà da martedì 24 novembre a mercoledì 2 dicembre 2026, per la durata di nove giorni."
  官方节目册（torinofilmfest.org）亦写开幕式 11 月 24 日、颁奖 12 月 2 日；「11 月 20 日–12 月 8 日」是都灵国家电影博物馆的门票优惠期（"biglietto ridotto… (dal 20 novembre all'8 dicembre 2026)"），不是电影节档期——builder 显然把优惠期当成了电影节日期。
- 本期印错的 6 处（均已在渲染图上确认）：
  1. P1 `LA SETTIMANA`：「VEN 20 — A Torino apre il Torino Film Festival, 44ª edizione.」（电影节 11 月 20 日并未开幕；11 月 24 日周二才开幕）
  2. P5 正文：「E venerdì 20 novembre, a Torino, apre il Torino Film Festival, la 44ª edizione, fino all'8 dicembre」——开幕日与闭幕日皆错。
  3. P5 `IL PIANO DELLA SETTIMANA` 第 1 条：「Venerdì: apre il Torino Film Festival」。
  4. P5 `I GIOVANI IN NUMERI`：「Torino Film Festival: dal 20 novembre all'8 dicembre, 44ª edizione.」
  5. P5 练习 81（判断）：「Il Torino Film Festival apre il 20 novembre. Vero o falso?」——P8 答案 `81. Vero` 是错的，应为 Falso。
  6. P8 练习 120：「Il Torino Film Festival apre... A. il 22 novembre · B. il 20 novembre」——P8 答案 `120. B` 是错的；且两个选项都不含正确答案 11 月 24 日，本题按印法无解。
- 附带：P5 标题「il cinema apre a Torino」亦建立在错误的周五开幕前提上。第 44 届届数本身正确（练习 68 答案 A 无误）。

### 缺陷 4（系统性，已由 builder 自认）：未执行 SOP §1.1 视觉规范，仍用旧样式
- KIT §7 自述："shipped W46 IT core PDF uses Noto Serif/Sans CJK SC + UnifrakturMaguntia, old-style svglib.py (PAPER #f7f1e2, GOLD, double frame) — NOT the Newsreader/§1.1 new style… the §1.1 Newsreader migration is a separate re-render wave, not this builder's job."
- 独立核实（源码 + 渲染图）：
  - `svglib.py:69` `PAPER = "#f7f1e2"`（§1.1 要求 `#fbfaf6`）；`GOLD = "#b3a06a"` 且多处使用（§1.1：不用金色）；`svglib.py:77–78` 双线外框（两道 rect，3pt + 1.2pt；§1.1：去掉每页的双线外框）；`INK = "#28251d"` 近黑底条（§1.1：不用近黑底）；字体为 NotoSerifCJK（§1.1：拉丁目标语标题/正文用 Newsreader）；刊头/页脚多处用「·」分隔（P1「VOL.4 · QUARTA EDIZIONE」「意大利语周报 · VOL.4 · LA SERIE A · IL TORRONE · VENEZIA」；§1.1：不用「·」做分隔，用全角空格）。
- 定性：SOP §1.1 称「本节是 PDF 视觉的唯一正本」。W46 同款旧样式出过刊，但本期按现行 SOP 仍属偏离；是否接受旧样式出 W47 由父线/用户裁定，校对员如实上报。

## 次要观察（不列为硬缺陷，供修版时顺手处理）
- P1 `LA SETTIMANA IN CIFRE`：「150 — i figuranti del corteo di chiusura del Torrone」。来源（foodtour.info / chebello.info / 官方节目）均为 150 人以上（"more than 150 people" / "oltre centocinquanta figuranti"）；P3 正文正确写了「oltre centocinquanta」，P1 裸写 150 与来源及 P3 不一致（中文注「150 多名演员」是对的）。建议 P1 改为「oltre 150」。
- `assets/CREDITS.md` 仍停留在 VOL.1/W45（无 W47 七张图的条目）；W47 图片核验只在 KIT §5 的文字里， credits 文件未更新。
- P3、P5 中部有大面积空白（正文栏约在 55% 高度结束，下方留白直至练习区）——无溢出，但版面偏空。
- P1 `LA SETTIMANA` 「GIO 19 — Si avvicina il weekend: Torino prepara il tennis.」措辞含糊：ATP Finals 自 11 月 15 日已在进行中，19 日说「准备」不妥（填充句，无硬事实可核）。
- P1/P2/P6 的「修正案截止 11 月 17 日 18 点」：截止日 11 月 17 日已由多源证实（2duerighe、ilpoliticoweb、QuiFinanza）；「18 点」这一时刻未在本次检索的来源中找到，未独立证实、亦未证伪。
- P8 范文第 4 句「Sabato, a Venezia, c'è la Madonna della Salute」出现在以周日（22 日）为叙事时间的范文里，用现在时写周六的活动，时态略别扭（可改为 c'era）；属文体小问题，未列缺陷。

## 已通过的检查（逐项，含工具输出摘要）

### 机械门槛（全部用 `tools/venv/bin/python` 重跑）
- `tools/occlusion_audit.py production/2026-w47/core-it/svg --json work/occlusion.json`：selftest OK（6 类阳性全触发），**0 flags**，exit 0。
- `tools/p8.py extract --p8 svg/p8-valutazione.svg --total 150 --json work/p8.json`：**noted set = 150 of 150**，题号 [1..150] 连续无缺重，exit 0。（注意：集合齐全 ≠ 答案全对——缺陷 1、3 的答案错误不在此工具覆盖范围。）
- `tools/freeze.py baseline --build production/2026-w47/core-it --core-svg production/2026-w47/core-it/svg --out work/freeze`：**8/8 SVG 字节一致**（`baseline: 8/8 SVGs byte-identical`），shipped SVG 跑前跑后 hash 不变，exit 0。

### 文字层与 PDF
- `pdfinfo`：两 PDF 均为 8 页、1462.5 × 2025 pt。
- `pdftotext`：print 与 web 版提取文本均为 **44,083 字节，逐字节一致**（`cmp` 通过，与 KIT 所述一致）；web PDF 1,918,807 字节 < 7MB。

### P8 答案字号（独立核实）
- `svg/p8-valutazione.svg` 全部字号集合最小值 **13 px**（152 个节点）；`content8.py` 答案流 `af.para(txt, 13, lh=1.14, ...)`；版面 1950 px = 1462.5 pt，换算系数 0.75 → **13 × 0.75 = 9.75 pt**，恰为 SOP §1.1 下限，不低于下限；KIT 所述无误。页内无更小字号。

### 150 题逐题复核
- 逐题对照题面、原文、图表验算：除缺陷 1（53/54）、缺陷 3（81、120）外，其余 146 题答案全部正确。
- 验算例：P6 图表 13−11=2（85 题 B）、6+7=13（86 题 A）；P4 比较级 più/meno/più bella/meglio；P7 101–112（andremo/assaggeremo/guarderemo/è partito/abbiamo visto/hanno comprato/è finita/piova/nevichi/leggano/torna）；P8 113–150 逐题核对原文与选项；范文 99 词（逐词数得 25+19+15+15+13+12=99，符合 80–100 词 brief）。
- 题量分布：按 P8 答案分组核得 P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38 = 150；级别分布由 SVG 徽章独立核算：A2 47 / B1 70 / B2 33（与 KIT 一致；核算方法：SVG 内 `>A2<` 类徽章 145 枚，减目录页 4 枚非练习徽章，加 3 组各 4 题共用 1 枚徽章的配对题补 9 题）。
- P2/P6 另两组配对题答案正确（25–28 与 141–144）。

### 金句、标题、目录、徽章
- P1 主头条「La Lazio resta in vetta: Inter e Roma inseguono」去空白 39 字符 ≤ 56（cover.mjs LIMITS.headline other=56）。
- 8 条金句逐字出自本期正文：对 SVG 文本节点拼接、空白归一化后每条恰出现 **2 次**（正文 1 次 + P7 1 次），与 KIT 所述一致。
- 目录（P1 IN QUESTO NUMERO）页码与级别与各版一致；页脚「第 N 版/共 8 版」1–8 齐全；金句后页码标注（P1/P1/P2/P3/P4/P5/P6/P6）均与原文所在版一致。
- 全部讲解层 glosses 逐项核对：所注的词均真实出现在当版正文里（P1 la vetta/imbattuto/il capolista/chiudere；P2 la salute/il ponte votivo/la candela/la peste/il voto/piantare；P3 il torrone/il corteo/il figurante/la rievocazione/lo sbandieratore；P4 la vetta/imbattuto/il big match/il girone/il debutto；P5 l'anteprima/il protagonista/la sede/l'incontro/indipendente；P6 la manovra/l'audizione/l'emendamento/il deficit/la copertura/lo scaglione/l'iter）。
- 意大利语全文精读：拼写、重音、性数配合、变位、标点未发现错误；「È probabile che + 虚拟式 / so che + 陈述式」、passato prossimo 助动词、futuro 不规则变位均正确；未见截断句、重复词。

### 事实核查（逐项，来源见备注）
- 意甲第 11 轮（11 月 6–8 日）：10 场比分、24 球、积分榜前 5 与末位、Lazio 不败、Roma 最佳进攻 31 球、Gattuso 执教 Lazio——与 minuto91.it / tuttoatalanta.com / antoniogenna.com / sportradar.com 多源一致；第 12 轮赛程（11 月 21–23 日）与 antoniogenna 下轮表一致。**但赛果表星期分组错（缺陷 2）。**
- Torrone（克雷莫纳，第 29 届，11 月 7–22 日，主题 «Il Confine»，16 天）：闭幕周日 11 月 22 日、Torrone d'Oro 授予 Davide Simonetta（11:00 Palatorrone）、corteo 16:00（150+ 扮演者）、Sforza–Visconti 婚礼重演 17:00 市政广场、sbandieratori 与火杂耍、压轴 18:00 «Il torrone va in brodo»、传说（1441 年 10 月 25 日婚礼、形似 Torrazzo）——与 festadeltorrone.com 官网、foodtour.info、petitchef.it、chebello.info 一致。
- Eurochocolate（佩鲁贾，第 32 届，11 月 13–22 日，«Fate dolci»）：Calabria 首个 Regione Ospite（bergamotto/cedro/peperoncino/fichi cosentini）、Costa d'Avorio 为客座国、11 月 20 日 18:15「I tesori della Calabria Straordinaria」（LAB）、11 月 22 日 Iginio Massari 压轴——与 latuaetruria.it / radiosubasio.it / tagumbria.it / umbriaeconomia.it 一致。
- ATP Finals（都灵，11 月 15–22 日，Inalpi Arena）：8 名单打——Zverev（No.1）、Alcaraz、Shelton、Medvedev、Cobolli（首秀）、Fils、Tiafoe、Jodar；抽签 11 月 12 日周四；决赛周日 22 日；Sinner 为 2024–25 两届冠军、因膝伤赛季报销缺席——与 rallyhub.au / livetennis.com / tntsports.co.uk / spotsports.com 一致。
- 国家联赛：意大利–法国 11 月 12 日周四 20:45 米兰、比利时–意大利 11 月 15 日周日 20:45 布鲁塞尔，赛程属实（uefa.com / figc.it）；**本期未印任何赛果、无编造小组积分榜**（P4 明确推迟至 VOL.5；P2 仅提「两个 Azzurri 之夜」无比分）——兑现了「截稿后开赛、不印赛果」。
- BookCity（米兰，11 月 23–29 日，第 15 届，主题 «Il senno sulla Luna»，Ariosto）：1,360 场、2,487 主角、1,164 本书、443 场地；开幕 11 月 23 日周一 20:00 Dal Verme 剧院，Colson Whitehead（两届普利策）；预展 11 月 22 日周日 16:00 Edmund de Waal，Fondazione Luigi Rovati——与 milano-business.com / milanoweekend.it / libreriamo.it / milanofree.it 一致。
- 预算法案：DPB 10 月 15 日送布鲁塞尔、2027 增长 +0.8%、赤字 3.4% PIL；10 月 28 日部长会议通过草案（C. 3174-bis；「约 26 亿」有 2duerighe.com 2026-11-10 为据，DPB 口径为 23.5 亿，文中已写明「据报纸重建」）；Budget 委员会联合听证 11 月 9–12 日、Giorgetti 12 日周四收官；修正案截止 11 月 17 日；须 12 月 31 日前最终通过；金融业出资约 50 亿、Irpef 第二档 33% 从 5 万扩至 5.5 万欧元、卫生增资——与 2duerighe.com / nonsolocalcio.news / ilpoliticoweb.it / gaming.net / parlamentonews.com 一致；文中三处明示「尚未成为法律」。
- Madonna della Salute（威尼斯，11 月 21 日周六）：还愿桥（船桥，过大运河）、1630 年瘟疫誓愿、Longhena 巴西利卡建于 1631–1687 年、蜡烛、castradina（咸熏羊肉 + 卷心菜，传统上 11 月 20 日晚吃）——与 relaisildoge.com / vlsagency.com / rentlocar.com / adomani-italia.com 一致。植树节 11 月 21 日（1898 年始为植树节、2013 年立法为国家日）、圣塞西莉亚 11 月 22 日音乐主保，均属实。
- Alba 白松露节至 12 月 6 日（96 届，10 月 10 日–12 月 6 日）——与 visitturin.com / comune.alba.cn.it / events.europa.tips 一致；练习 33/125 答案「6 dicembre」正确。
- Filmmaker Festival（米兰，11 月 14–22 日，11 月 22 日周日闭幕）——与 filmmakerfest.com 公报、cinemaitaliano.info、filmbyfilm.it 一致。
- **都灵电影节日期错误（缺陷 3）。**
- 日期/星期（`date` 核验）：11 月 6 日周五、7 日周六、8 日周日、12 日周四、15 日周日、16 日周一、17 日周二、20 日周五、21 日周六、22 日周日、23 日周一，全部与文中一致。
- W46 承诺兑现：意甲第 11 轮赛果 + 积分榜（P1 头条、P4 报道 + 积分榜，赛果对、星期分组错见缺陷 2）；Torrone 11 月 22 日闭幕（P1、P3、P7 预告）兑现；读者来信：P7 明确标注为编辑部示例（仅署「esempio della redazione」，无编造人名），中意双语披露截稿时未收到真实来信与最佳作文、承诺顺延 VOL.5——无编造读者/来信/引语；禁国际政治：全文扫描无 Ucraina/Russia/Putin 相关内容。
- ABSTRACT.txt：一行、无 ASCII 双引号、简体中文、含刊名/目标语/A2–B2/150 题与本期真实主题（意甲第 11 轮、牛轧糖节、巧克力节、圣母健康节、书城、电影节、预算法案），事实均取自本期内容。
- 图片（KIT §5 称逐张经 Wikimedia Commons API 核验，2026-11-10）：P1 老球场、P2 Canaletto 威尼斯、P3 Torrazzo（CC0）、P4 1920 年代网球全景、P5 Corot《读书少女》c.1868、P7 但丁像（Met Museum CC0）、P8 Vermeer《写信的女人》，页上署名与 KIT 一致，未见版权不明的现代新闻照片；P6 图表为程序化绘制且四处标明练习用编造数据。本校对未逐张重查 Commons API（KIT 之外的 credits 文件亦未更新，见次要观察）。

### 逐版看图（PDF 每页 72 dpi 渲染，8 页全看）
- P1–P8：无溢出、无重叠、无压页脚（几何审计 0 flags 亦佐证）；图片与出处齐全；页脚「第 N 版/共 8 版」清晰。
- P1：头条、LA SETTIMANA、IN CIFRE、目录、IN BREVE、QUIZ LAMPO 均完整；可见缺陷 3 的 VEN 20 条目与「150」条目。
- P4：赛果表四行完整可见，缺陷 2 在图上直接可认；配对题 a/b/c/d 顺序在图上可认，佐证缺陷 1。
- P5：缺陷 3 三处在图上直接可认；练习 81 在图上可认。
- P7：但丁图与图注完整；LETTERE 披露完整；8 条金句 + 下期预告完整。
- P8：答案区 9.75pt 仍清晰可读；Vermeer 图 + 图注完整；答案末行距页脚有空隙。

## 工作文件
- 本笔记：`hidden_files/w47/scratch-proof-it/PROOF-NOTE.md`
- 工具输出与渲染图：`hidden_files/w47/scratch-proof-it/work/`（occlusion.json、p8.json、freeze.log、freeze/、print.txt、web.txt、print-layout.txt、pg1–pg8 PNG）
