# 独立复校笔记 — 2026-W47 es-de（第二轮，叶子）

- 复校对象：`production/2026-w47/2026-w47-es-de/`（clone main，未改任何源码/成品；无 git 写操作，未跑 insert.py、lint --write）
- 探针：`git hash-object -w` 成功；`hidden_files/w47/scratch-proof-es-de2/.probe` 写盘成功。双通后开工。磁盘 45G 可用，无 EDQUOT。
- 身份核验（自算 SHA-256，与任务书及 KIT 登记逐字一致）：
  - print `La-Lucerna-VOL4-es-de.pdf`：3,503,020 B，SHA-256 `e97c5acc601179bcb629688e146183c6a690e1c381decb0743e13dea96934a72`
  - web `La-Lucerna-VOL4-es-de-web.pdf`：852,182 B，SHA-256 `7760133bec9f34b991de63d24339092fefe4d8bf57454b10f9d27ddb185c767e`
  - `2026-w47-es-de.text.md`：1,784 行

## 结论：零问题（a）

本轮为 SOP §8.4 从头全量复校：全文重读（text.md 1,784 行）、双 PDF 逐版目视（印刷 P1–P8 + 网页 P1/P8，均从送审 PDF 自行渲染）、150 题逐题验算、全部机械门独立重跑。第一轮的 D1、D2 经几何实测与目视双重确认已修；未发现新缺陷。按 SOP §8「一整轮全量校对零问题」口径，本版可定稿（定稿决定由协调员做）。

## fix1 复核（D1、D2 均已修）

### D1（P1 “AHORA TÚ　DU BIST DRAN”）— 已修
- 实测（送审 SVG）：栏目标题基线 (538.5, 1658.89)（核心版 1656.84）；Q1 题号 (610.5, 1707.89)（核心版 1705.84），紧跟同栏标题之下；Q2–Q6 题号 x=1061.0（第 3 栏，与核心版同构）。
- 目视（印刷 P1 全页，100dpi 自渲染）：标题下无白洞，A2 徽章 + Q1 题面同栏紧贴；数字框两条德文括号已收紧为“(15 Tage)”“(Donnerstag, 19.: letzter Tag)”，西文未动。
- fix1 字符串在 SVG 中各出现 1 次；`Anmerkung der Redaktion` 0 次（已删）。

### D2（P7 预告横幅）— 已修
- 实测（送审 SVG）：横幅 rect y=2458.51、高 118 → 下缘 2576.51；页脚线 y=2596，横幅在其上 19.49px，且 ≤ 核心版下缘 2582.51。横幅内文字基线 2502.51 / 2542.51（墨底约 2547），页脚文字基线 2624。
- 目视（印刷 P7 全页，100dpi 自渲染）：浅色页脚线在横幅下方干净通过，未被打断；页脚文字清晰。
- 编者注确为 3 行新文案（“Keine echten Leserbriefe bis zum Redaktionsschluss; ein Beispielbrief. Das Versprechen gilt für VOL.5.”），事实要素全留。

## 已核实无问题（全量结果）

### 内容与题量（150 题逐题验算）
- 副本 run.py 重跑：rc=0，TOTAL 150；级别 A2 50 / B1 72 / B2 28；分版 P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38；题型 Sätze vervollständigen 48 / Multiple Choice 47 / Wörter zuordnen 12 / Richtig oder falsch 8 / Sätze bilden 7 / Sätze umformen 10 / Lückentext (Auswahl) 13 / Übersetzen 4 / Schreiben 1；MODELO 97 词（run log 登记）；FLOW OVERFLOW 0 / HEAD TOO WIDE 0；重跑 SVG 与成品 8/8 逐字节一致。
- 150 题逐题核对题面、原文/图表与答案键：P1 1–10、P2 11–28、P3 29–46（含配对 25–28 c/b/d/a、词框 5 词各用一次）、P4 47–64（含配对 52–55 c/b/a/d）、P5 65–82、P6 83–100（含 RTVE 图表算术）、P7 101–112、P8 113–150。键与核心版一致（p8 compare CLEAN，见机械门）。
- 算术复核：RTVE 45+45+30+30+15+10+10+10=195（Q84=B）；PSOE−Vox=45−30=15（Q87=B）；禁发民调 11 月 24–28 日 = 5 天（Q86=A、Q90=A、Q127=B）；金句 8 条在 8 个 SVG 中各出现恰好 2 次（原文 + P7 引用），德文译注准确，页码注（Página 1/4/2/5/3/6/3/6）与出处页一致。
- 星期/日期：`date` 核验 2026-11-09（周一）至 11-29（周日），文中全部星期表述（周五 13、周一 16、周三 18、周四 19、周五 20、周六 21、周日 22、周一 23、周二 24、周四 26、周五 27、周六 28、周日 29）均吻合。
- 禁词：全文（8 个 SVG 文本）“12 de noviembre”0 次；Ucrania/Rusia/guerra/Trump/Putin/OTAN/Israel/Gaza/Palestina 各 0 次。西班牙国内政治选题在红线允许范围内。
- VOL：VOL.4 共 9 处，VOL.5 共 3 处（均为下期预告正当引用），VOL.3 0 处。
- 徽章（白字 A2/B1/B2 文本计数，逐个映射到题号）：P1 10（A2 8/B1 2）、P2 15、P3 18、P4 15、P5 18、P6 18、P7 12（A2 4/B1 4/B2 4）、P8 35（A2 11/B1 21/B2 3，与核心版 P8 完全一致）；合计与题数之差恰为 3 个共用徽章组（25–28、52–55、141–144）。
- P8 最小字号：pypdf Tm 有效字号（Tf 字号 × Tm 缩放），149 条目，最小 10.125pt ≥ SOP §1.1 下限 9.75pt；P8 答案流终 y=2506（流底 2560，余 54px）。
- §8.1 讲解词核实（SVG 文本计数，大小写不敏感）：P1 reflexión 2；P2 mitin/cartel/escaño 各 2；P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 6；P4 parón 2 / liderato 3；P5 papeleta 2 / censo 3 / plazo 3。与 KIT 逐项一致。
- ABSTRACT.txt：德文一行、无 ASCII 双引号；事实（laSexta 辩论 13 日、大选 29 日、邮寄投票截止 19 日、弗拉门戈日 16 日、圣塞西莉亚 22 日、联赛第 13 轮、欧冠、150 题、A2–B2、VOL.4）均与本期内容一致。
- .text.md：1,784 行，CJK 表意文字 0；题号 1–150 齐全（“N.” 扫描另含一处正当“página 8.”，不计）；U+3000 共 99 个。

### 翻译层（fan-out 专项）
- 讲解/界面语言确为德文：全部 gloss/桥句/栏目标题/答案注文/页眉页脚配对行为德文；西语正文冻结（freeze diff 见机械门）。
- freeze diff（core-es vs es-de）：P1 +27/−38、P2 +50/−51、P3 +33/−30、P4 +34/−27、P5 +44/−47、P6 +19/−17、P7 +46/−46、P8 +161/−626；新增 CJK 合计 1 个 = U+3000 全角空格（SOP §1.1 分隔符）。
- CJK 残留：8 个 SVG 的 `<text>` 元素内 CJK 表意文字/假名/韩字均为 0；仅剩 SOP §1.1 规定的全角空格分隔符 U+3000（P1 21 / P2 16 / P3 13 / P4 15 / P5 14 / P6 14 / P7 12 / P8 14）与未渲染的蛾标元数据 `<title>Lucerna 三色蛾</title>`（与核心版 identical，见观察项 O3）。
- E 组翻译题：Q137 键为德语句 “Montag ist der Internationale Flamencotag.”、Q138 键为 “Am Samstag sehen wir das Derby von Sevilla.”，注 “Vgl. Original.”——与 W45/W46 ES×EN 裁定一致；Q139/Q140 键为西语句、注文为德文，符合同一裁定。keydiff [137, 138] 属预期内。
- 德文译注准确性：全文德文逐行读过（text.md 1,784 行），未见拼写/语法/事实错误；人名/机构名/数字/日期与正文一致。Q139 德文源句与西文键、Q140 德文源句与西文键互译准确。

### U+2019 缺陷类回归
- 8 个 SVG 全扫：U+2019 总数 0（每版 0）；U+0027 撇号 0 处；全角标点 0 处。
- 目视抽查：P1 „Debatte“ 引号、P8 #91 „Vorgeschlagen“/„beschlossen“ 德文引号在印刷/网页渲染中均正常，无宽字形断裂。

### P8 注文人名专项（人工逐条核对）
- 与第一轮结论一致：仅 Lucía、Diego（P8 练习 C 的虚构人物，与题面逐字一致）；其余为 laSexta、MiDNI、Correos、UNESCO、PSOE、PP、Vox、Podemos、Barça、Sevilla、Madrid、Bilbao、Nairobi、Andalusien、Champions League、Black Friday 等机构/地名/赛事名，均与本期正文原词一致，无拼写偏差；无 ja 类罗马字人名缺陷。

### 目视（从送审 PDF 自行渲染，不采信 builder 的图）
- 印刷版 P1–P8 逐版目视（100dpi 全页）+ 网页版 P1/P8 目视：无溢出、重叠、压页脚、图片错位、缺字（豆腐块）。
- P2：日历、DECIR LA HORA、LOS DÍAS 表、习题 A–D 齐全。P3：Sargent 画作 + 图注/出处齐全；¿Y TÚ? 框底在 EJERCICIOS 分隔线之上。P4：LA JORNADA 13 六场表齐全；习题 A–D 齐全。P5：Jebulon 投票箱照片 + 图注/出处齐全；B 组桥句完整、词框与题同栏。P6：RTVE 与民调禁发两图齐全，数值与正文一致；习题 A–D 齐全。P7：Book of Hours 图 + 图注齐全；金句 8 条 + 译注 + 页码注齐全；除已修 D2 外无问题；第 1–3 栏习题下留白与核心版同构。P8：RESPUESTAS 头注与天鹅笔照片图注无重叠；答案流 150 条齐全；范文 97 词。
- 渲染工具注：pdftoppm 在本机渲染送审印刷 PDF 时第 5 页段错误退出（rc=139，随后单页重跑亦 rc=1 “Could not write image”）；改用 PyMuPDF（tools venv）8 页全部正常渲染且内容完整——属 poppler 工具问题，PDF 本身无损坏（pdftotext 正常、PyMuPDF 正常、freeze/p8 均正常读 SVG 源）。

## 观察项（不计缺陷；O1–O5 与第一轮一致，未变）
- O1（P5 B 组词框，沿自核心版）：词框 6 词中 sobre、urna 未作任何题的键；Q70 键为 correo、Q72 键为 envío。核心版 P5 词框与键完全相同（p8 compare CLEAN），属核心版设计（疑似干扰词），非本版改动。
- O2（¿Y TÚ? 德文译注为凝缩版，非全文翻译）：与第一轮所列一致；译注本身正确完整、可作答。
- O3（非渲染元数据）：P1 蛾标内 `<title>Lucerna 三色蛾</title>` 与核心版 identical、从不渲染；KIT §6.13 已裁定不动。
- O4（措辞小事）：P7 ERRORES 第 1 条德注“1 Uhr ist Singular: nimm es.”略口语，可懂无错；P8 #56 注括号“(der Titelkampf zählt mehr)”提示较含糊，无错。
- O5（P1 CINCO CLAVES 副标题为混合行）：“Fünf Themen　Para entender la semana”——与 es-en 版同一处理，属 fan-out 既定做法，不计问题。
- O6（新增观察，栏目标题跨栏——核心版同构，不计问题）：P2 “D LAS PALABRAS”、P4 “B LAS PALABRAS”、P5 “B PALABRAS DEL TEXTO”三处栏目标题落在栏底、内容在下一栏顶。本轮用核心版 PDF 同页对照核实：核心版 P2/P4/P5 同位置完全相同（标题栏底、内容次栏），属共享版式结构的继承现象，非本版引入。occlusion 审计 0 flags。

## 机械门结果（全部自跑，见 GATE-LOG.md）
- 遮挡审计（tools/venv 解释器）：selftest 六类全触发；本版 0 flags。
- p8 extract：150/150；p8 compare vs core：CLEAN，missing=[] extra=0，keydiff=[137, 138]（已裁定，见上）。
- freeze baseline：8/8 SVG 字节一致；另自跑 run.py 重跑（副本）：rc=0，FLOW OVERFLOW 0 / HEAD TOO WIDE 0，TOTAL 150，重跑 SVG 与成品 8/8 一致。
- print/web 文字层：pdftotext 各 45,770 字节，逐字节一致；web PDF 852,182 B < 7 MB。
- P8 最小字号 10.125pt（≥9.75pt 下限）。
