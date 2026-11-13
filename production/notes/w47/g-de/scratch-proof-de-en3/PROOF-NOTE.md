# PROOF-NOTE — proof3（独立全量复校）Lucerna Weekly 2026-W47 de-en（rebuild 6，fix2 后）

- 复校员：proof3；只读复校，未修版、未 commit、未 push、未派 subagent；全部写件在 goals 侧本 scratch 目录。
- 对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-de-en/`
- 依据：SOP.md §1.1、§8、§9；proof2 PROOF-NOTE；fix2 FIX-LOG；本版 WEEKLY-KIT.md；机械门详见同目录 `GATE-LOG.md`。

## 对象核对

| 文件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `Die-Lucerna-VOL4-de-en.pdf` | 10,966,410 B | `c8904dea16d2474afdd6629789af266eabfa5d5b9ea06813d9b0fd95e38722cd` |
| 网页 PDF `Die-Lucerna-VOL4-de-en-web.pdf` | 1,597,904 B | `2c190c75c61f9dbc75db62b251cb07ba965f98866425bcd287cab08f423d9f3a` |
| 文本导出 `2026-w47-de-en.text.md` | 49,665 B | `f3f0c08455b647c9b8f2844fbf16c33008e2717f30c584d7a3b835f98cb8a53e` |

三件 SHA 与任务值一致（开工、收尾各核一次）；text.md SHA 与 fix1 相同，字符一字未动。

## §1 本次重点：D1/D2 闭引号独立重测 —— 已治愈

fix2 唯一改动：版内 `svglib.py` 的 `_char_font` 把 sans 串里的闭引号 U+201C 经 serif 分支路由到 Newsreader（不动字符、不动键）。两处闭引号现为独立 `<text>“</text>` span（Newsreader16pt-Regular）。

**独立重测（400 dpi 窄带墨列法 + PDF rawdict 字符框 + 200/400 dpi 裁切目视）：**

| 实例 | 实测前空隙 | fix2 宣称 | 结论 |
|---|---|---|---|
| D1 P8 H 框 `„My week in November"`（15.00pt） | **0.18pt = 0.012em**（r 墨止 450.90 → 引号墨起 451.26，纯白 1 像素 = 0.18pt/px） | 0.18pt / 0.01em | 一致；目视贴紧，无白洞，无触碰 |
| D2 P8 键 67 `„Im Lande des Christkinds"`（9.94pt） | **0.72pt = 0.072em**（s 墨止 455.76 → 引号墨起 456.66，纯白 4 像素） | 0.72pt / 0.07em | 一致；目视贴紧，无白洞，无触碰 |
| 对照 P8 对话 `„Eine stille, schöne Woche",`（14.62pt） | 前空隙 **1.44pt = 0.098em**；后空隙 **1.26pt = 0.086em** | fix2 引「1.26pt = 0.09em」为对照 | 见注记 |

字形结构（rawdict 确认）：Newsreader 的 `“` 在 x 投影上恒为两个逗点团——D1 (451.26–453.42)+(454.14–456.12)，D2 (456.66–457.92)+(458.46–459.90)，对照 (502.20–504.36)+(504.90–507.06)。D1 第二团 (454.14–456.12) 位于引号 span advance [450.52, 457.14] 内、句点 advance 起点 457.14 之前，确为引号第二逗点，非句点。本轮初测 `quote_pixel3c.py` 曾误取第二团报 D2 0.36pt（脚本取团 bug），profile 数据已推翻，不作证据；`quote_pixel3.py` / `quote_pixel3b.py` 的早期结果亦已作废（取团/针位错误，见 GATE-LOG）。

**注记（非缺陷）**：fix2 报告的对照值 1.26pt 是对照组 `Woche“,` 的**后**空隙（引号→逗号），不是前空隙；对照组真前空隙为 1.44pt = 0.098em。结论不变：D1 0.012em 偏紧于对照带（fix2 已披露，成因是 sans 字母 `r` 右侧空白约 0）但为正、无触碰；D2 0.072em 落在对照带内。仅 fix2 日志的引用口径需纠正，不影响本版。

**其余 33 对 „ " 未变**：全版 U+201C = U+201E = 35（P1 5、P5 6、P7 21、P8 3），U+201D = 0，U+2019 = 0，U+0022 = 0；core-de U+201C = 33（P8 1），多出的 2 个恰为 D1/D2。**键 B 未动**：Q67 键 B、Q8 键 A、Q56 键 mehr 均 REG / builder / P8 提取三方一致。**P7 工具盒 +16.0 未回退**：canonical creambox 测得工具盒底 799.9，末条基线 783.9，清除量 +16.0，desc-clear +9.9。

## §2 内容事实逐条网查 —— 全部通过

- 德甲第 9 轮（6–8 Nov 2026）9 场比分全对：HSV–Gladbach 3:1、Dortmund–Elversberg 2:1、Leipzig–Augsburg 5:2、Mainz–Bayern 1:2、Paderborn–Frankfurt 2:2、Stuttgart–Bremen 1:0、Köln–Leverkusen 1:2、Freiburg–Union 2:0、Hoffenheim–Schalke 2:1；总进球 4+3+7+3+4+1+3+2+3 = **30** ✓；积分榜 Bayern 第 1（21 分，29:9）、Köln 第 15（9 分，10:14）✓。
- 欧冠第 4 轮（3–4 Nov）：Atlético–Bayern 0:2（Karl 54'、Laimer 74'）✓；Dortmund–Betis 2:1 ✓；Leipzig–Man City 2:3 ✓；Galatasaray–Stuttgart 2:0（Batrakov 12'、15'）✓。欧联/欧协 5 Nov：Leverkusen–Marseille 0:1、Crystal Palace–Hoffenheim 1:1、Trabzonspor–Freiburg 0:1 ✓。
- 国家队：Serbien–Deutschland 周五 13 Nov 20:45 贝尔格莱德 Rajko Mitić，UEFA 观众禁令、U15 儿童 + 50 名 DFB 球迷豁免、约 5,000 人；德国 5 分、荷兰 8 分、希腊 8 分（A2 组）✓。**荷兰之战（本轮新核）**：周一 16 Nov 2026 20:45，柏林奥林匹克体育场，ARD 直播，小组末战 ✓（文中 "Mo 16.11. 20.45 Nations League: Deutschland – Niederlande (Berlin, ARD)"、Q60 B 皆正确）。
- 第 10 轮（20–22 Nov）：Bayern–Köln 周五 20:30；周六 5 场 15:30（Leverkusen–Paderborn、Frankfurt–Hoffenheim、Union–Leipzig、Gladbach–Dortmund、Elversberg–Freiburg）+ Schalke–Stuttgart 18:30；周日 Augsburg–Mainz 15:30、Bremen–Hamburg 17:30 ✓。
- 科隆圣诞市场 2026：Dom（Roncalliplatz）16 Nov–23 Dec，22 Nov（Totensonntag）闭市，官方开幕周二 17 Nov 19:00；Markt der Engel 16 Nov–23 Dec；Hafen（Schokoladenmuseum）13 Nov–3 Jan；Aachen 20 Nov–23 Dec ✓。
- Buß- und Bettag 周三 18 Nov 2026，仅萨克森法定假日，1995 年起废除（1994 年决定，为护理保险融资），萨克森雇员多缴 +0.5pp；巴伐利亚学校停课；"stiller Tag" 禁舞 ✓。**萨克森禁舞时段（本轮新核）**：SächsSFG §6 官方文本——Buß- und Bettag 公开舞会禁令 "von 3.00 Uhr bis 24.00 Uhr"，文中 "von 3 bis 24 Uhr" 与 Q23 键 A 完全正确 ✓。Totensonntag 周日 22 Nov（教会年最后主日）；首个将临期周日 29 Nov；18+11=29、15+7=22、16+6=22 ✓。
- 1903 年首个印刷版降临节日历 "Im Lande des Christkinds"：Gerhard Lang，Richard Ernst Kepler 插画，儿童以图画粘贴覆盖窗口 ✓（"über 120 Jahre" = 123 年 ✓）。
- Wilhelm Ritter（1860–1948），画作 "Weihnachtsmarkt auf der vorderen Insel Schütt"（1930）✓（"vor fast 100 Jahren" = 96 年 ✓）。
- 2027 联邦预算：表决计划周五 27 Nov 2026（bundestag.de）；家庭电税 2.05 Cent/kWh，自 2003 年未变；总理 Friedrich Merz 欲全民降至欧盟最低；联盟党/社民党协议未达成 ✓。
- 欧冠第 5 轮（24–25 Nov）：Arsenal–Dortmund、Leipzig–Lens（24 日）；Inter–Stuttgart、Lille–Bayern（25 日）✓。欧联 26 Nov：Dinamo Zagreb–Leverkusen、Hoffenheim–Sturm Graz ✓。

## §3 德语正文与英语讲解层逐句读 —— 通过

text.md 全文 1186 行逐行读过；8 页印刷渲染逐页目视；网页版 P1/P8 目视与印刷一致。

- 150 题键与题干逐题语义核对：REG 复现 150 题（按页 10/18/18/18/18/18/12/38；A2 69 / B1 67 / B2 14；MC 52、填空 41、改写 11、判断 8、完形 8、造句 8、配对 12、翻译 4、对话 5、写作 1），编号 1–150 连续；REG vs builder `en/keycheck-150.json` **0 差异**；REG vs P8 提取 **149/150**（仅 Q150 开放写作题被提取器截为 "Open task"，预期）。抽核非平凡键：Q51 B（荷 8 / 德 5）、Q56–59 比较级（mehr / später / früher / mehr）、Q85 B（44+33=77）、Q91 B（2.05）、Q98 Kirchenjahr(s)、Q110 fraglich、Q113–120 完形（schaut/bastelt/schreibt/sieht/beginnt/liest/denkt/ist）、Q137–140 翻译、Q141–144 配对、Q145–149 对话（öffne/machst/schaue/schaue/lese 与人称一致）、Q16–20 Perfekt（abgeschafft worden / geblieben / gegangen / behalten / geblieben）——全部正确。
- P7 逐字 8 句 ×2 出现（Sätze der Woche 与正文逐字一致）✓；MUSTER 范文 84 词，标签 84 一致 ✓。
- ABSTRACT（SOP §9）：356 B、1 行、无 ASCII 双引号；内容与 KIT 一致（德甲回归、荷兰决战、忏悔祈祷日与亡灵主日、科隆市场开市、11 月 3–8 日欧战与德甲赛果；德语正文、英语讲解、A2–B2、150 题）✓。

## §4 版式几何逐页目视 + 全套门禁 —— 全部通过

- 8 页印刷渲染逐页目视：无溢出、无重叠、无页脚侵入；图片（P1 足球、P3 1930 纽伦堡市场画、P4 头球、P5 1903 日历、P7 阅览室、P8 1905 足球）均在位、图注完整；P6 图表三条橄榄绿条 748/561/391、44%+33%+23%=100，ÜBUNGSDATEN 单行完整。
- occlusion audit **0 flags**（自检 6 类植入均触发，审计有效）；canonical creambox 全版扫描 **NO OVERFLOW**（27 盒清除量全正，最小 +10.4；BELOW-WINDOW 10 行均为 +24.0～+44.9 已知误报带，无整行溢出）；measure 24/24 PASS；p8 compare **CLEAN**；freeze diff 新增 CJK 7 个皆 U+3000；freeze 直接层 8/8（计数与 SHA 与宣称全同）；boxtitle 7/7（双通道，数值逐项相同，最紧 P5 余 2.6px）；abutting **PASS**（最大位移 0.20pt；P6 图表 strip 印/网像素差 max 0）；印/网文字层逐页词 multiset 全同；P8 最小字号 **9.94pt ≥ 9.75pt**；chips 141（P8 A2 22 / B1 13）；Q34 新题干五处 1×/旧 0×；pdffonts：两版字体全部嵌入+子集（含网页版 LucernaNewsreader-Bold/Italic）。
- 细节见 `GATE-LOG.md`（24 项门禁逐项）。

## §5 观察（非缺陷，不影响定稿）

- **O1（core 继承，proof2 已记）**：P4 正文提及斯图加特在加拉塔萨雷客场 0:2 失利，赛果表未列该场。无练习依赖该比分。
- **O2（proof2 已记）**：Q56/Q58 答案注记行文压缩（"5–2 more goals than 2–1"、"3 Nov. earlier than 8 Nov."），可读、无歧义。
- **O3（KIT 诚实短板，core 继承）**：P1 头条首段无首字下沉（drop cap），与 core 一致。
- **O4（本轮新记，fix2 报告的风险，非本版缺陷）**：版内 `svglib.py` 的 fix2 改动在下次 re-transform 时会被 core-de 的 `svglib.py` 重新拷贝覆盖而丢失；持久修复应在 core-de/svglib.py 中做。不属于本版内容问题，不由复校员修复。
- **O5**：P1 头条用过去时 "Deutschland traf in Belgrad auf Serbien" 写 13 Nov 之战——刊期为 11 月 16–22 日，读者视角下 13 Nov 已成过去，时态正确。
- **O6**：P3 盒标题 200 dpi 裁切坐标错位（取到词表体而非标题），该裁切未作证据；7 个盒标题已由全页目视 + 双通道墨宽测量覆盖。

## VERDICT

**(a) 零问题，可定稿。**

proof2 的 D1/D2 已由 fix2 治愈：D1 0.18pt、D2 0.72pt，独立重测与宣称逐项一致，裁切目视贴紧、无白洞、无触碰；其余 33 对引号未变、键 B 未动、text.md SHA 不变、P7 工具盒 +16.0 未回退。全文事实、德语与英语层、150 题键、版式几何、全套门禁（occlusion、p8、freeze、measure、canonical creambox、boxtitle、abutting、印/网一致、字号、字体嵌入）全部通过，无新发现缺陷。

## 收尾核对

- 三件 SHA 收尾复核与任务值一致（见上表）；版目录任何文件未被复校改动：`git status` 中 `2026-w47-de-en` 相关 10 条均为 `??` 未跟踪（fix2 未提交的新版目录），无 `M` 修改；工作树另有 106 处 `M` 为 W43 issues 文件，系其他并行工作，非本复校所动。
- 本复校全部写件仅在 goals 侧 scratch（PROOF-NOTE.md、GATE-LOG.md、`gates/`、`render/`、`text/`、`copy/`、`tmp/`），未写进 repo 的 `hidden_files/w47/`。
