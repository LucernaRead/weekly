# PROOF-NOTE — 2026-W47 es-fr 独立复校（proof1，SOP §8.4）

**对象**：`production/2026-w47/2026-w47-es-fr/`
- 印刷 `La-Lucerna-VOL4-es-fr.pdf` 3,499,799 B，SHA-256 `c1c3ecdc326da7d91a4c55e8ad578e66d574db4436d6ec7a23164d653f54b168`
- 网页 `La-Lucerna-VOL4-es-fr-web.pdf` 846,204 B，SHA-256 `e6e5abbf4f923e4dfbae62777b1cea88f863e444d5be2e61892609005a245065`
- `2026-w47-es-fr.text.md` 45,272 B，SHA-256 `94476219c438fc47ba2613e45b7a266302540ec57ece4d39203400def46a4bc7`
- 两 PDF 各 8 页。SHA 与 brief 逐项核对一致后开工。
- 复校员与建版者不是同一人。只复校，未改任何源文件，未重建、未 commit、未 push，未动 `tools/`。
- 探针：`git hash-object -w --stdin` 成功；scratch 目录真实写文件成功。渲染中间件全部放在本 scratch 目录，`TMPDIR=<scratch>/tmp`，未写 /tmp，未删他人文件。

## 结论：(b) 缺陷清单 — 1 项轻缺陷，需修后按 §8.4 从头再做一轮全量复校

本轮不是零缺陷，不能定稿。

## 缺陷

### D1（轻，fan-out 层，非核心）— P3、P5「¿Y TÚ?」盒法语末行降部字母漫出奶油盒底

- **位置**：P3 右栏「¿Y TÚ?　ET TOI ?」盒（`x=1440..1862`，盒底 `y=1594.8`）；P5 右栏同名盒（盒底 `y=1574.5`）。
- **现象**：两盒末行均为法语「deux phrases et envoie-les.」，基线距盒底仅 1.9px，未留降部余量。实测墨水底（PIL + 仓库 `tools/fonts/Newsreader-Regular.ttf`，原字号 19）：
  - P3：墨水底 `y=1597.55`，**漫出盒底 +2.75px**；
  - P5：墨水底 `y=1577.35`，**漫出盒底 +2.85px**。
  越界的是 `phrases` 的 `p` 降部尾。3× 裁图目视证实（本目录 `crop-p3-youturn-bottom.png`、`crop-p5-youturn-bottom.png`）：`p` 尾伸出米色盒底、落在白纸上。
- **判定依据**：与 de 家庭已修缺陷同类（creambox 扫查的盲区正是此类；occlusion 审计对此盲；de-fr 曾以基线 clearance −0.4px 立项修复）。本项墨水实越 +2.8px，属同类真缺陷，虽在整版视图几乎不可见、仅放大可见，仍按 §8.4 计为发现。
- **根因**：fan-out 层。法语译文行比核心中文行长，盒高按基线 +1.9px 定，未计降部。核心同位置中文行无降部字母，不存在此问题，故不是核心缺陷。
- **修法建议**（供建版者定，不由复校员改）：两盒底各下延约 5px（P3 至 ~1600，仍在 `y=1608` 分隔线之上 8px；P5 至 ~1580），或改断法语末行；修后整期重渲染、从头再做一轮全量复校。
- **其余盒**：全版 creambox 扫查其余 20 盒，墨水均在盒内（P7 三盒 clearance 墨水余量 +42.5 / +26.5 / +0.95px，无漫出；P7 工具盒合格）。creambox 原始负 clearance 6 处经逐项核对均为误报：盒下标题（AHORA TÚ、DECIR LA HORA、LO QUE QUEDA、LA PALABRA）、盒下注文（CINCO CLAVES 法语注、投票箱图注）——与核心同坐标、同布局一致，属设计如此，非溢出。

## 观察（不计缺陷）

- **O1（边际）**：P2「¿SABÍAS QUE…?」盒末行 `ley.` 墨水底 543.45 vs 盒底 543.5（余 0.05px）；P5「VOTAR POR PRIMERA VEZ」盒末行 `compara precios antes de pagar.` 墨水底 1251.45 vs 盒底 1251.5（余 0.05px）。墨水未越界，但零余量、尾巴贴着盒边。若修 D1 时顺手动这两盒，建议同样给约 5px。
- **O2（文笔）**：P8 答案 #56 注「más + importante (la course au titre)」——题面「El Barça–Villarreal es ___ que un amistoso」与「争冠」无直接关系，括号属于多余解读；事实不误（巴萨确实领跑争冠），可修可不修。

## 核心级候选（报协调员，绝不碰核心）

- **C1**：11 月 13 日 laSexta 辩论主题。版内写只谈经济（P1「cuatro portavoces hablaron de economía」、P6「a hablar de economía」）。核心 KIT §6.10 已裁定此点，依据 diariodesantiago.es 2026-11-06 的逐场区分（13 日经济／18 日住房）。本轮检索另见两源称 13 日场为「vivienda y economía」（democrata.es 2026-11-06；quadratin.com 2026-11-10《Economía y vivienda centran el primer debate electoral de España》）。这本身不足以推翻核心裁定（11 月 2 日 laSexta 场亦冠名「vivienda y economía」，后文可能沿用旧标签），但协调员可在 VOL.5 前决定是否重核。本项不计为 es-fr 缺陷，核心未动。

## 核实通过的部分（本轮实测）

- **全文通读**：`2026-w47-es-fr.text.md` 全文读完。西班牙语正文与核心冻结文本一致（freeze diff 仅讲解层增减）；法语讲解层逐行核对，无中残留（可见文本 CJK 仅全角空格 U+3000，SOP §1.1 规定分隔符；唯一真 CJK 是 P1 虫标内非渲染 `<title>Lucerna 三色蛾</title>`，与核心相同，KIT §6.12 已裁定）。
- **150 题逐题核对**：答案键逐题对照题面/原文/图表复核，1–150 全部一致。配对组 25–28（debate→c、mitin→b、cartel→d、escaño→a）、52–55（jornada→c、derbi→b、liderato→a、fase liga→d）、141–144（sondeo→c、muestra→d、margen de error→b、junta electoral→a）逐字母核对无误。p8 compare CLEAN，keydiff 仅 [137, 138]（翻译题按 W45/W46 裁定改以法语句为键，法译本身核对正确：137「Lundi, c'est la Journée internationale du flamenco.」/ 138「Samedi, nous regardons le derby de Séville.」）。法语答案注逐条核对，无错注（#96 «Aunque + indicatif (fait connu)»、#101–104 时间表达、#109–112 虚拟式均正确）。
- **外部事实**（现场检索核实）：29-N 大选日历（La Moncloa 指南、RD 806/2026：竞选 11-13 00:00 至 11-27 24:00，28 日静默日，29 日投票 9:00–20:00，邮寄申请至 11-19，11-24–28 禁发民调）✓；UNESCO 弗拉门戈 2010-11-16 内罗毕 ✓；西甲第 13 轮六场时间＋积分榜巴萨 33／皇马 30／马竞 28＋11 月 8 日巴萨客场 1–2 胜马竞 ✓；欧冠 J4（巴萨 3–0 阿斯顿维拉、皇马 3–2 AEK、马竞 0–2 拜仁）与 J5（皇马–PSV 11-24 21:00、Sabah–巴萨 11-25 18:45、马竞–Viking 11-25 21:00）✓；MiDNI（JEC 2026-11-05 解除停用，Acuerdo 342/2026）✓；全部日期星期经 `date`（Europe/Madrid）校验 ✓；Black Friday 2026-11-27 为周五 ✓；RTVE 分钟合计 45+45+30+30+15+3×10=195 ✓，LOREG 档位（45/30/15/10）自洽——唯具体分党数字引自核心 KIT §5.3（queproponen.es），本轮未能从独立源再核到 JEC 的具体分配，记为核实限度，非缺陷。
- **金句**：P7 八句逐字摘自本期文章，全文计数各恰 2 次（原文＋P7 引文），页码标注 P1/P2/P3/P4/P5/P6 均正确。
- **范文 97 词**：实数 97 词，与版面标注一致。
- **译注词**：各版 Note 词在当版全文出现 ≥2 次（P1 réflexion 2；P2 mitin/cartel/escaño 2；P3 cante 5/toque 6/baile 9/compás 4/duende 6；P4 parón 2/liderato 3；P5 papeleta 2/censo 3/plazo 3）。
- **弯引号/撇号**：SVG 文本 « 56 = » 56，成对；无直引号、无弯双引号；撇号统一 ASCII（全版一贯，非缺陷）。
- **禁词**：「桥接」0；「12 de noviembre」0；「SOP/proofread/cover」等内部语义 0。VOL.4 ×9（8 页脚＋1 刊别）、VOL.5 ×3（均为下期预告正当引用）。
- **印/网一致**：pdftotext 印版＝网版 46,247 字节，逐字节一致；网版 <7MB；P8 最小字号实测 10.12pt（≥9.75pt 底线）。
- **8 页目视**：印刷全 8 页＋网页 P1/P8 逐页看过，无溢出、重叠、压页脚、图片与出处不符。P7 预告框底离页脚线有余量、页脚字落在象牙底上（核心 §6.7 缺陷的同类位置已复核无问题）；P1「À LA UNE　VOIR PAGES 2 ET 6」与核心「见第2、6版」逐字对应；四图（Sargent 舞者、Jebulon 投票箱、「SUFFRAGE UNIVERSEL」铭文完整、《时祷书》装饰首字母、天鹅羽笔）与图注一致。

## 机械门结果（详见 GATE-LOG.md）

occlusion 0 flags（自检六类全触发）· p8 extract 150/150 · p8 compare CLEAN（keydiff [137, 138] 已裁定）· freeze 8/8 · creambox 全版扫查（见 D1）· keycheck 150/150 · P8 最小字号 10.12pt · boxtitle 0 flags。
