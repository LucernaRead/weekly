# PROOF-NOTE — 2026-W47 it-de（独立复校 proof1）

- 复校员：proof1（只读，未改版、未 commit、未 push）
- 日期：2026-11-11
- 复校对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-de/`
- 对照 core（冻结源）：`~/workspace/weekly-git/production/2026-w47/core-it/`
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-it-de1/`

## 0. SHA 核对（三件与简报一致）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-DE.pdf` | 14,037,296 B | `6903d98b3adb07c1fea0ff1e9b844cc8d8950fc8cfd34adb82394582bbf304cf` |
| 网页 PDF `La-Lucerna-VOL4-DE-web.pdf` | 1,265,110 B | `a62a094705fabd79cd70efec5083835e5cc2ff2d943f36c19d851f0f36cee6e1` |
| 文本导出 `2026-w47-it-de.text.md` | 56,734 B | `851ac7af017672d3fff5a7869a205d7890b0744f1a98913f2a42393f2972fb4a` |

两 PDF 均为 8 页、1462.5×2025 pt。探针 `git hash-object -w --stdin` rc=0（`probe.txt`）。

## 1. 门禁全套（全部跑过）

| 门禁 | 结果 |
|---|---|
| occlusion audit（edition svg/） | 0 flags，selftest 正常（`occlusion.log`） |
| p8 compare（core-it 对 it-de，显式 --core-p8/--edition-p8） | CLEAN，150/150 noted；keydiff 仅 [137, 138, 139]（预期的重定向翻译键，已人工核对语义正确）（`p8compare.log`） |
| p8 extract | 150/150 noted |
| freeze diff（--core-svg 指 core-it/svg） | rc=0；新增 CJK 共 13，全为 U+3000 家具分隔符（豁免）；全文 903 行片段逐条读过——新增全为德语讲解层/家具，删除全为 core 的中文讲解层；意大利目标语文本零改动；P8 键 60/61 两边字节一致（`freeze-diff.log`、`freeze-diff.json`、`freeze-fragments.txt`） |
| freeze baseline（重建 core 比对） | **8/8 字节一致**，core 完整性复核通过（8 文件重哈希未变）（`freeze-baseline.log`） |
| 印刷/网页 text layer 字节比对 | 字节相同（各 46,184 B），词多重集相同（各 7,799 词，0 单边词）（`print.txt`、`web.txt`） |
| P8 最小字号（PyMuPDF 渲染 pt 实测） | 全局最小 9.75 pt，P8 最小 9.75 pt，符合 SOP §1.1 下限 |
| 练习编号 | 138 单题 + 3 区间（25–28、52–55、141–144）= 150，无断号；级别 A2 47 / B1 70 / B2 33，与 KIT 一致 |
| CJK 扫描（.text.md） | 仅有的汉字是「翻译」二字（Q137–140 的类型标签，各 4 次）；全角冒号：×14（冻结的动词范式注 16–20、60–61 及答案）；其余为 U+3000 家具分隔符；无「第/版」等中文字符 |
| ABSTRACT.txt（SOP §9） | 一行、德语、无 ASCII 双引号、含 Lucerna、意大利目标名、A2–B2、150 Übungen；事实与本期一致 |
| P1 封面标题 | `La Lazio resta in vetta: Inter e Roma inseguono` = 39 非空格字符 ≤ cover.mjs 上限 56 |
| creambox 全版扫描（canonical `creambox.py`，+45px 窗口） | 见 §4；真墨迹均在盒内（`creambox.log`） |
| BOXTITLE 真墨迹宽度 + 横向漫出全版扫描（PIL 真墨迹量 + PDF span 框 + 200 dpi 像素扫描三重验证） | **发现 D1、D2（见 §5）**；其余全部通过（`h-overflow.txt`、`h-overflow2.txt`、`h-pdf-scan.txt`、`h-gutter.txt`） |

## 2. 内容事实（逐条核对公开来源，无出入）

- 意甲第 11 轮（11 月 6–8 日）10 场结果全对，24 球；Lazio 29、Inter 28、Roma 27（31 球最佳攻击）、Milan 第 4 名 24 分、Como 23、Udinese 末位 5 分；"La Lazio di Gattuso" 有来源支撑。
- 第 12 轮：Lazio–Lecce 周六 11 月 21 日 15:00、Atalanta–Inter 周日 11 月 22 日 20:45、Monza–Fiorentina 周一 11 月 23 日 20:45。
- Nitto ATP Finals 都灵 11 月 15–22 日，决赛周日 22 日；Sinner 膝伤缺席，Zverev 世界第一，Cobolli 首秀，8 人/2 组/半决赛周六 21 日。
- Eurochocolate 佩鲁贾第 32 届 11 月 13–22 日，主题 «Fate dolci»，嘉宾大区卡拉布里亚，«I tesori della Calabria Straordinaria» 周五 20 日 18:15，Iginio Massari 周日 22 日闭幕。
- Festa del Torrone 克雷莫纳第 29 届 11 月 7–22 日（16 天），主题 «Il Confine»，Torrone d'Oro 授予 Davide Simonetta（周日 22 日 11:00 Palatorrone），游行 16:00（>150 人），Sforza–Visconti 婚礼重演 17:00 市政广场，旗手/烟火至 18:00，压轴 «Il torrone va in brodo» 18:00；1441 婚礼传说已按传说表述。
- BookCity 米兰第 15 届 11 月 23–29 日，主题 «Il senno sulla Luna»（阿里奥斯托），1,360 活动 / 2,487 人物 / 1,164 书 / 443 场地；开幕周一 23 日 20:00 Dal Verme 剧院（Colson Whitehead，两届普利策）；预展周日 22 日 16:00 Luigi Rovati 基金会（Edmund de Waal）。
- 都灵电影节第 44 届 11 月 24 日–12 月 2 日（9 天，官方章程）；Filmmaker Festival 米兰 11 月 14–22 日，周日 22 日闭幕；Alba 白松露集市第 96 届 10 月 10 日–12 月 6 日。
- 2027 预算法：DPB 10 月 15 日送布鲁塞尔；2027 增长 +0.8%、赤字 3.4%；部长会议 10 月 28 日批准法案；约 260 亿（政府口径；DPB 口径 235 亿——文中已注明 260 亿为报纸重建数，可接受）；法案号 C. 3174-bis（11 月 4 日三条款被删后重编号）；听证会 11 月 9–12 日（意大利银行、UPB、Giorgetti 部长周四 12 日）；修正案截止周二 17 日 18:00；终批截止 12 月 31 日；Irpef 第二档 33% 由 5 万延至 5.5 万；约 50 亿来自银行/保险。P1/P2/P6 均有 "PROPOSTA ≠ LEGGE" 提示；P6 练习图表已标注虚构数据。
- 欧国联：意大利–法国周四 12 日（圣西罗）、比利时–意大利周日 15 日（布鲁塞尔），A1 组；文中未印赛果（截稿后开赛，留待 VOL.5）正确。
- 威尼斯：Madonna della Salute 11 月 21 日，1630 誓愿，Longhena 圣殿建于 1631–1687 年，castradina 11 月 20 日晚，船桥；植树节 11 月 21 日（1898 首届植树节、2013 国家立法）；圣塞西莉亚 11 月 22 日，音乐主保。Torrazzo 称意大利最高钟楼（通行说法，未列缺陷）。

## 3. 语言与键（全文逐句读过）

- 意大利语正文与德语讲解层逐句读：拼写/语法/术语/一致性无问题。
- 150 题答案键全部读过；匹配题逐项人工核对题干语义：P2 25–28（salute→c、ponte votivo→b、candela→d、piantare→a）、P4 52–55（vetta→d、imbattuto→b、girone→c、debutto→a）、P8 F 141–144（manovra→d、deficit→c、copertura→b、scaglione→a）均正确。
- Q137–140 翻译正确；Q58 più bella、Q59 meglio、Q82 Falso、Q120 B（TFF 11 月 24 日）、Q149 B 均核对。
- P7 FRASI DELLA SETTIMANA 8 条引文逐字核对原文及页码（P1 ×2、P2、P3、P4、P5、P6 ×2）无误；Q150 范文逐词数 = 99 词。
- P7 ERRORI TIPICI 4 项正确；LETTERE 为标注的编辑示例 + 德语说明（无真实来信，W46 模式）；VOL.5 预告栏在位。
- `.text.md` 与 PDF 文本层：逐页词比对——差异全部可解释：md 含 57 处行内 "— key:" 注解（答案行内注，PDF 各页无对应行，答案只在 P8）与 "[A2 · …]" 类型标签（PDF 用德语短标签，如 "Einsetzen" 56 次）；PDF 提取存在并词（缺空格）与宽距刊头拆字（SETT IMANA 等）。按句子级比对的"缺失"全部是上述结构/提取 artifacts；全文人工通读未发现任一内容句单边缺失。KIT 称的 "0/0" 漏检因双方结构不同无法用同一口径复现，记为**未核实**（不是缺陷）。

## 4. 版式几何——目视与 creambox

- 8 页印刷 PDF 72 dpi 全页渲染逐页目视：无溢出、重叠、页脚侵入、豆腐块。P3/P5 中部结构性留白为 core 固有模式（KIT 已诚实注明）；P1 体育场照片注 "(Pagina 4)" 是指向体育版的交叉引用，不是错误。
- canonical creambox 扫描（`creambox.log`，344 行已读完）：全部"末基线"负清除量均为误报——窗下行是下一节标题/行/图注，不是溢出（如 P1 IN QUESTO NUMERO 盒 −24.0 → 下方 'LA PAROLA DELLA SETTIMANA' 标题；P3 HINWEIS −37.0 → 下方标题；P4 结果表行 −40.0/−40.0/−26.0 → 下一行文字；P6 图表盒 −42.0 → 'ESERCIZI' 标题）；盒内清除量均为正（+16.0 至 +90.0）。
- 9 个盒子呈系统性偏紧模式：盒内清除量约 +4.5–5.6 px、desc-clear −0.4 至 −1.5 px（P2 LO SAPEVI?、P2 E TU?、P3 IL WEEKEND DOLCE、P3 E TU?、P4 E TU?、P5 I GIOVANI IN NUMERI、P5 E TU?、P7 LA PAROLA、P7 LETTERE）。经逐字核查：这 −0.4…−1.5 px 是 0.30 em 下行字母预留超过约 5 px 盒底间隙造成的计量 artifact，不是真墨迹漫出——多数末行根本无下行字母；唯一带下行字母的末行是 P7 LETTERE 的 "…gilt für VOL.5."（g），其下行约 3.2 pt < 3.85 pt 间隙。200 dpi 裁图（`crop-p7-parola-bottom.png`、`crop-p7-lettere-bottom.png`、`crop-p4-etu-bottom.png`、`crop-p2-losapevi-bottom.png`）目视确认：末行文字完整在盒内，下方留白清晰，无墨迹越过盒边。**不列为缺陷**。
- BOXTITLE 真墨迹宽度：最长标题实测均在界内——P1 "LA SETTIMANA IN CIFRE　DIE WOCHE IN ZAHLEN" 墨迹右缘 1099.9 px（盒跨 538.5–1411.5）；P6 "LE MINIME DI ESEMPIO　BEISPIEL-MINIMA ZUM ÜBEN (DATI INVENTATI PER L'ESERCIZIO)" 墨迹右缘 1208.3 px（页内）；P7 "FRASI DELLA SETTIMANA　SÄTZE DER WOCHE (WÖRTLICH AUS DIESER AUSGABE)" 墨迹右缘 1153.2 px。occlusion BOXTITLE 0 flags 与独立实测一致。

## 5. 缺陷

### D1 — P1 LA SETTIMANA 盒副标题墨迹越过盒右缘与页面右边距（本版级）

- **位置**：P1 右栏奶油盒（rect x=1439.5, w=422.5，右缘 = 页面右边距 1862 px）顶部副标题，SVG y=694。
- **证据**（三重独立验证一致）：
  - PIL 真墨迹量（SVG 源，Noto Sans CJK SC 19 px）：墨迹右缘 1875.7 px，超右边距 13.7 px（≈10.3 pt）。
  - PDF span 框（PyMuPDF，交付件实测）："Cosa succede, giorno per giorno" x1=1407.5 pt，超右边距 1396.5 pt 达 11.0 pt。
  - 200 dpi 渲染像素扫描（`crop-d1-p1-subtitle.png`）：末字墨迹最右 1406.4 pt，超 9.9 pt；同行背景在 962.5 px 处由奶油色（亮度 237）变纸白（249），即盒缘恰在边距处，末字 "giorno" 的尾部落在盒外白纸上（裁图目视可确认）。
- **严重度**：中。文字完整可读、无遮挡、无内容丢失（距物理页边仍有约 52 pt），但副标题 visibly 伸出盒外与版心，违反版心留白规则；属 proofread-until-zero 的拦停项。
- **级别**：**本版级**。core-it 同位置副标题为「本周日程　Cosa succede, giorno per giorno」（x=1461.5、19 px 相同），德语前缀 "Diese Woche" 比中文前缀「本周日程」宽约 24 px，core 的墨迹右缘约 1851 px、在界内；溢出由德语讲解层加宽引入。
- **修法建议**：缩短德语前缀，如 "Diese Woche" → "Die Woche"（省约 17 px，墨迹右缘约 1858.7 px < 1862），或字号 19→18 px；改后重新量墨迹与重跑横向扫描验证。

### D2 — P2 匹配题 b、d 首行墨迹越过页面右边距（core 级）

- **位置**：P2 右栏（第 4 栏）匹配题 25–28 选项 b、d 的首行，SVG y=2162（b）、2271（d）。
- **证据**（三重独立验证一致）：
  - PIL 真墨迹量（SVG 源，Newsreader 23 px）：b 行墨迹右缘 1875.1 px（超 13.1 px）、d 行 1877.8 px（超 15.8 px）。
  - PDF span 框：b 行 x1=1408.2 pt（超 11.7 pt）、d 行 x1=1409.7 pt（超 13.2 pt）。
  - 200 dpi 渲染像素扫描（`crop-d2-p2-options.png`）：b 行末字墨迹最右 1406.8 pt（超 10.3 pt）、d 行 1408.6 pt（超 12.1 pt）；裁图目视：两行均伸至接近物理页边，明显越过版心右缘。
  - 全文为 "b. il ponte di barche per la festa del 21 / novembre" 与 "d. la piccola luce di cera che si accende / in chiesa"；仅首行溢出，续行在界内；同组 a、c 行在界内。
- **严重度**：中。文字完整可读、无遮挡、无内容丢失，但两行 visibly 伸出版心约 4 mm；属 proofread-until-zero 的拦停项。
- **级别**：**core 级**。core-it/svg/p2-vita.svg 中两行 x/y/字号/文本完全相同，core 本身即溢出；本版系忠实继承。修 core 后须重新 fan-out 全部 11 个母语版（缺陷随 core 传播）。
- **修法建议**：在 core 中提前断行，如 b 行断为 "b. il ponte di barche per la festa" / "del 21 novembre"，d 行断为 "d. la piccola luce di cera" / "che si accende in chiesa"（或缩短措辞）；改后重跑横向扫描验证全部 11 版。

## 6. 观察（非缺陷，无需修）

- **O1 横向沟槽侵入（无碰撞）**：P4 结果表行 "Cagliari – Frosinone 1–0"（+11.1 px）、"Torino – Lecce 1–1"（+10.2 px）、"Genoa – Milan 1–2"（+11.1 px）、匹配题 b/c 行（+7.7/+12.4 px）；P8 匹配题 F 选项 a/b/c 首行（+18.5/+18.9/+8.2 px）。墨迹均只进入 28 px 宽的空沟槽，距下一栏文字最近仍有 9.5 px，零碰撞、读者不可见。建议后续收紧换行宽度，不拦停。
- **O2 desc-clear 负值**（见 §4）：计量 artifact，真墨迹均在盒内，不列缺陷。
- **O3 贴边未超**："Die Stufen sind gemischt — Antworten nach Nummer suchen"（P2–P6 各页）墨迹右缘 1861.8 px（边距内 0.2 px）；P8 "✓ = Modelltext-Aufgabe" 墨迹右缘 1862.1 px（超 0.1 px，量测噪声级）。均不列缺陷。
- **O4**：P7 FRASI 德译行 "Vierundzwanzig Tore in zehn Spielen. (Pagina 1)" 墨迹右缘 518.4 px——该节为双栏宽块，属自然行尾，非溢出。

## Verdict

**(b) 有问题，须修后重校：D1、D2 共 2 项。**

- D1（本版级）：P1 副标题越过盒右缘与页面右边距约 10 pt。
- D2（core 级）：P2 匹配题 b、d 首行越过页面右边距约 11–13 pt；修 core 后须重 fan-out 全部 it 母语版。
- 其余：事实、语言、150 题键、门禁（occlusion、p8、freeze 8/8、text layer、P8 字号、abstract、creambox 盒底）全部通过；O1–O4 为观察项，不拦停。
