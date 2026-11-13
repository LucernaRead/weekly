# PROOF-NOTE-fr — W47 法文核心版独立校对（叶子）

- 版：2026-w47-fr-zh-cn（目标 fr × 读者简体中文），VOL.4，刊期 2026-11-16..22
- 校对员：叶子（独立校对，与 builder 不同的人；只读不改）
- 日期：2026-11-10（EST 晚间）
- 结论：**(b) 缺陷清单** —— 共 6 条缺陷（D1–D6），另 5 项观察（O1–O5）

## 已核实的文件身份

| 文件 | 页数 / 大小 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4.pdf`（印刷） | 8 页 / 30,444,535 B | `4356f0fa119082ac69b863dc5aea0c905af5f1e996b651cc10576a52961d2ec7` |
| `La-Lucerna-VOL4-web.pdf`（网页） | 8 页 / 2,201,571 B | `333f15a4de0928320285070f38d0446d00f68b86628387cc3361327af822e627` |
| `2026-w47-fr-zh-cn.text.md` | 45,758 B | `8c439b03236098c753788bad0adf1feea476596251d9853543154e0075ac300d` |

三者均与任务简报一致。`ABSTRACT.txt`：280 B，一行简体中文，无 ASCII 双引号，含刊名、法语、A2–B2、150 道练习 ✓。

---

## 缺陷清单

### D1 — P5 事实错误：「cinquante ans avant Katniss」（严重）

- **位置**：P5 正文第一段（`Mercredi 18 novembre : le cinéma, et la seconde main`），亦见 .text.md L571。
- **问题**：原文「qui raconte Haymitch, le héros du district 12, cinquante ans avant Katniss」。Sunrise on the Reaping 的故事设定为 **Katniss 之前 24 年**、第 **50 届**饥饿游戏。本文把“第 50 届”误写成“50 年”。
- **证据**（2026-11-10 网上核实）：JustWatch 指南、Audible、Parade、Capital FM、Tatler 均称 "24 years before Katniss" / "50th Hunger Games"。该片其他事实均核实无误：法国上映 2026-11-18 周三、片长 2 h 38 / 158 分钟（BBFC）、导演 Francis Lawrence、Haymitch 16 岁。
- **影响**：正文事实错误；Q63「Haymitch est le héros... B. du prequel」不受影响（题干不含 50 年）。

### D2 — P6 Q84 无据可答（严重）

- **位置**：P6「LIRE LE CALENDRIER 读日程」Q84。
- **问题**：题干「Cinquante jours, jusqu'au... A. 9 nov. B. 26 nov. C. 18 déc.」，键 B（26 nov.）。键本身符合事实——50 天期限（art. 47-1）确于 **2026-11-26 周四午夜**到期（nosparlementaires.fr、senioractu.com 2026-11-10 核实）。但 **50 天规则与 11 月 26 日这两个信息在本期 P6 文章与日程表里完全没有出现**：P6 SVG 中「50 jours」出现 0 次；「26 nov.」只在 Q82/Q83/Q84 的选项里出现。栏目说明是「读上图日程，选出正确答案」，读者无法从报纸上推出答案。
- **证据**：P6 日程表（LE CALENDRIER）六行仅为 23 oct. / 4 nov. / 9–17 nov. / 18 nov. / 20 nov. / 9 déc.，无 50 天、无 11 月 26 日。

### D3 — §8.1 讲解词未真实出现在正文（13 词）

- **依据**：SOP §8.1（讲解词必须真实出现在正文里）；同周期 de 校对的同一标准（词表词“亦全部在正文”且通过）。
- **位置与缺失词**（词表框本身除外，屈折形式计为出现）：
  - P3「LES MOTS DU VIN 葡萄酒词表」（10 词中 7 词在正文）：缺 `bouteille`、`raisin`、`vigne`。
  - P4「LES MOTS DU TENNIS 网球词表」（8 词中 6 词在正文）：缺 `tennis`、`adversaire`。（`match` 计出现——正文有 "matches"；`point` 计出现——正文有 "10 points"。）
  - P5「MOTS DU CINÉMA 电影词表」（8 词中仅 1 词在正文）：缺 `salle`、`écran`、`acteur`、`actrice`、`réalisateur`、`scénario`、`séance`；`public` 仅在图片署名「domaine public」中出现，不是作为教学词「le public = 观众」出现。
- **核实方式**：脚本逐词核对 + 人工通读正文。

### D4 — §1.1 中文数字带空格（全刊 19 处）

- **依据**：SOP §1.1 明文：「中文里的数字不加空格：第1版／共8版、11月11日。讲解层和答案同样」。ko 第二轮校对把同一模式列为 §1.1 缺陷（ko 已修「中文数字去空格」）。
- **位置与数量**（SVG 统计）：
  - 「第 N 版」带空格 **4 处**：P2、P4、P5、P8 各 1。
  - 「N 月 N 日」带空格 **15 处**：P2 6、P5 1、P7 1、P8 7。P8 答案区如「11 月 19 日新酒上市」「8 月 13 日」「10 月 23 日」「11 月 4 日」「12 月 9 日」「11 月 16 日是星期一」——答案明确在 SOP 覆盖范围（「讲解层和答案同样」）。
  - **内部不一致**：P2「DIRE LA DATE」表头「11月16日星期一」无空格，同一框内下方行「11 月 16 日星期一」带空格（目视确认）。
  - 页脚家具合规：「第1版／共8版」无空格 ✓。
- **W46 辩护不成立**：fr builder 称此为 W46 做法，但 W46 fr KIT 无任何 §1.1 核实记录；W46 fr text.md 实际也有带空格日期（15×「11 月 … 日」）——是未经审查的沿用，不是已接受的裁定。
- **协调员注意**：同周期 de 第一轮校对曾把带空格「第 N 版」（28 处）判为通过（「与验收版一致」）——与 ko2、与本裁定冲突，请协调员统一口径。

### D5 — P8 14 道题缺级别徽章

- **依据**：SOP §4「每道题单独标 [A2]/[B1]/[B2]」。
- **位置**：P8 完形填空 Q109–116（注册级别 A2×5：109、110、111、112、116；B1×3：113、114、115）、对话 Q145–149、写作 Q150——**共 14 题完全无徽章**。
- **证据**：插桩重跑 registry：P8 仅画出 **120 个**徽章（150 题）。目视 P8 确认：完形、对红、写作三区均无徽章；徽章只出现在 Q117–139 与 Q144。配对共享一枚徽章的部分（22–25、49–52、73–76、85–88、140–144）与 de/ko 做法一致（两者均为 138 枚 = 150 − 16 共享题），fr 的缺口是这 14 题（120 vs 138）。

### D6 — P1 与 P2 题干重复 + 空格可填第二正确答案（轻微）

- **位置**：P1 Q2/Q3 与 P2 Q11/Q13。
- **问题**：
  - (a) 题干完全相同：P1 Q2「Le Sénat vote ___ 18 novembre.」= P2 Q11；P1 Q3「Le beaujolais nouveau arrive ___ 19 novembre.」= P2 Q13。同一期出现两次相同题干与相同键（Q2/Q11 键 mercredi；Q3/Q13 键 jeudi）。
  - (b) P1 的空格可填第二正确答案：法语「Le Sénat vote le 18 novembre」「Le beaujolais nouveau arrive le 19 novembre」完全合乎语法，填「le」亦对；P2 A 组有「注意星期与数字」的指示，P1 的「À VOUS!」框无此指示，学习者填「le」会被判错。
- **定级**：轻微编辑缺陷，不涉事实。

---

## 观察（非缺陷，记入台账）

### O1 — 五组配对题按相同顺序印刷

P2 Q22–25、P4 Q49–52、P5 Q73–76、P6 Q85–88、P8 Q140–144：词与释义顺序完全一致，答案必然是 a/b/c/d 顺序对应，配对无难度。**不定为缺陷**：SOP 未明确要求打乱顺序；de/ko 同周期亦为同模板做法；题仍可做、键正确。建议后续模板打乱释义顺序。

### O2 — 「seize films」（16 部新片）计数未获证实亦未证伪

P5 正文、P5「LE CINÉMA DU MERCREDI」框、Q62（键 B=16）均称 11 月 18 日 16 部新片。filmscinema.fr 的计数不稳定且方法松散：2026-11-10 搜索快照为 17 部；同日 22:49 UTC 实时页为「Semaine du 18 nov. 2026 : 24 films」，其中把「Coward」与「Les Braves (Coward)」当作两部（同一部 Lukas Dhont 电影）、计入音乐会/电视放映（BTS 直播、Chicken Shop Date），并把「Fais-moi un signe」划入 11 月 25 日那周（而 sortiraparis、ayther、geekslands 均称 11 月 18 日上映）。**不能据此判定「16」为错**。六部点名影片（Les Braves、Jupiter、Malika、Camembert、Fais-moi un signe、Hunger Games）及日期均已核实无误。建议 builder 注明计数来源（Allociné/CNC）。

### O3 — 「la course, arrêtée lundi 9 novembre」措辞小不精确

P4 正文：ATP Race 由 11 月 8 日巴黎决赛决出，积分榜于 11 月 9 日周一公布。「arrêtée lundi 9」可理解为“截至周一的积分榜”，措辞略不精确，非事实错误。**观察而已**。

### O4 — P1 头条首段无首字下沉

SOP §1.1 要求「头条第一段首字下沉」。独立核实：P1 SVG 中正文首段「Dimanche 8 novembre, Carlos Alcaraz」为 24px（18pt）整行文本，无放大首字；P1 最大非刊头字号即头条 53px（39.75pt）。**按 de 同周期裁定处理**：de 注明 FR P1 同样无首字下沉，裁定为 SOP 文本与验收版之间的共有缺口、可接受。本项记为观察，不计缺陷。

### O5 — 两处换行遗留的孤行标点（轻微版式）

- P7 B2 语法注「celui que: ……的那一个 (关系代词) 。」——句号「。」单独落在下一行行首（目视确认）。
- P2 Q18「Dimanche, vous (regarder) les finales.→」后填空线「—」单独落在下一行。
均为轻微版式瑕疵，不影响阅读。

---

## (a)(b) 两项裁定（任务项 8）

### (a) 字号阶梯

- **(a1) P1 头条 39.75pt（53px）**：**可接受**。低于 SOP 下限 40pt 仅 0.25pt，系像素取整（53px vs 53.33px）。与 de 第一轮裁定一致（头条 39.75pt 可接受），与 W46 fr 实测值相同。
- **(a2) P2–P6 标题**：builder KIT 称「Flow.title 38px = 28.5pt」**有误**。`bslib4.py` 默认值 38，但每次调用均传 32；SVG 字号确认 `font-size="32"` → **24pt**，恰为 SOP 次级标题范围上限（22.5–24pt）。**合规，无偏差**。

### (b) 讲解层中文数字带空格

**缺陷**（见 D4）。SOP §1.1 明文禁止；ko 第二轮同类模式已判缺陷并修复；W46 无 §1.1 核实记录，沿用不构成接受。

---

## VOL.5 / VOL.4 核实（任务项 9）

.text.md 中 **VOL.5 ×9、VOL.4 ×4，9 处 VOL.5 全部合法**，无一页把本期印成 VOL.5：

| # | 位置 | 内容 | 合法性 |
|---|---|---|---|
| 1 | L245 P2 | 「paraîtront dans le VOL.5 (page 7)」 | 读者习作顺延 VOL.5 |
| 2 | L497 P4 | 蓝队与法甲第 11 轮结果见 VOL.5 | 结果顺延 |
| 3 | L537 P4 | 都灵冠军名见 VOL.5 | 结果顺延 |
| 4 | L931 P7 | 「Le VOL.5 reprendra la promesse.」 | 编辑部说明 |
| 5 | L933 P7 | 中文编辑部说明：VOL.5 兑现承诺 | 同上 |
| 6 | L935 P7 | 「LA SEMAINE PROCHAINE VOL.5 下周预告」 | 下周预告栏 |
| 7 | L949 P8 | Q111 题干「seront dans le VOL.5」 | 完形题干 |
| 8 | L1035 P8 | 写作题：优秀习作见 VOL.5 | 写作说明 |
| 9 | L1075 P8 | 答案注「111. A（结果见 VOL.5）」 | 答案注释 |

SVG 计数一致（P2 1、P4 2、P7 3、P8 3）。VOL.4 ×4 为刊头/副标题与 P7 两处编辑部说明。全刊各版均印 VOL.4（目视 8 版确认）。W46 KIT「VOL.5」为 off-by-one 笔误，不影响本期。

---

## 通过的检查（全量清单）

### 机械门槛（tools/venv/bin/python）

- **几何遮挡**：`tools/occlusion_audit.py` 对 `svg/` → **0 flags**；自测 6 类 planted 缺陷均触发、干净对照静默 ✓。
- **P8 提取**：`tools/p8.py extract --p8 svg/p8-exercices.svg --total 150` → 注记集 **121/150**（parse: joined）。缺失 29 题：1, 2, 11, 16, 18, 23, 24, 25, 27, 29, 35, 36, 37, 39, 48, 49, 50, 51, 52, 63, 73, 74, 75, 76, 85, 86, 88, 98, 99。**121 题逐项核实正确**：提取集与 `content8.py` 中 `PRINT_NOTES` 列表完全一致（无差）；当前提取键与 `final-fr-p8.json` 键 0 差异。
- **向后兼容**：新版 `p8.py` 在旧「·」版 P8 SVG（`hidden_files/w47/scratch-fr/p8-before-dotfix.svg`）上抽出**同一 121/150 集**——builder 宣称属实。
- **Freeze**：在 scratch 副本重建 8 个 SVG，SHA-256 **8/8 与交付 SVG 字节一致**（p1 `f64289e7fcc8`、p2 `fde09f9e3934`、p3 `3307783b6432`、p4 `a9bc97db6855`、p5 `65186d9aca90`、p6 `42d64bc5d3f8`、p7 `3c95b6121618`、p8 `dda587fe9860`）。`tools/freeze.py` 自报 0/8 为已知 OUT 路径假象（副本落在 `<out>/build-copy/svg/`，工具查空的 `<out>/svg/`），以 SHA-256 为准。
- **Registry 插桩重跑**：总数 **150**；分级 **A2 53 / B1 75 / B2 22**；页分布 **P1 10、P2 15、P3 18、P4 18、P5 17、P6 18、P7 12、P8 42**——均与 KIT 一致。另：仅画出 120 枚徽章（见 D5）。
- **文字层**：`pdftotext` 印刷版/网页版均为 **45,939 字节**，空白归一化后**完全一致**；两份 PDF 均为 8 页、1462.5×2025pt ✓。
- **P8 字号**：PyMuPDF 对印刷版 P8 → 最小 span **11.62pt**（213 spans），≥ 9.75pt 下限 ✓（builder 称 11.6pt 属实）。
- **MCQ 折行检查器**：builder 的 `hidden_files/w47/scratch-fr/check_mcq.py` → **DEFECTS: 0, UNLOCATED: 0**（45 个题体，1416 行）。**目视复核**（见下）亦通过。

### 目视检查（8 页 100dpi 渲染图逐页精读）

- **P1**：刊头、VOL.4、头条、导读条、图片（Atget，署名完整）、目录、页脚均 clean；Q7–10 选项单行、无劈开。首段无首字下沉（见 O4）。
- **P2**：「DIRE LA DATE」表头无空格 vs 行内带空格（见 D4）；Q19–21 换行均在选项之间；配对 22–25 顺序一致（见 O1）；Q18 填空线孤行（见 O5）；Châtillon 图片 + 署名 ✓。
- **P3**：Q41–43 换行均在选项之间；Moreau 图片 + 署名 ✓；「LES MOTS DU VIN」词表可见（见 D3）；「ZOOM LES DATES EN CHIFFRES」框 ✓。
- **P4**：Q44–48 换行均在选项之间；配对 49–52 顺序一致（见 O1）；「LES CHIFFRES DU SPORT」框 ✓。措辞「arrêtée lundi 9」（见 O3）。
- **P5**：Q62–66 换行均在选项之间；Méliès 图片 + 署名 ✓；「MOTS DU CINÉMA」词表可见（见 D3）；正文「cinquante ans avant Katniss」已印出（见 D1）；「16 部新片」框（见 O2）。
- **P6**：Q79–84 换行均在选项之间；日程表六行完整，无 50 天、无 11 月 26 日（见 D2）；自我更正段落完整；配对 85–88 顺序一致（见 O1）。
- **P7**：8 句金句跨栏完整（「C'est le mercredi des sorties en / France...」「Comme dit l'ADEME...」等均在下一栏续完）；读者来信区明确标注编辑示例、无编造来信（见下）；Doré 图片 + 署名 ✓；「celui que」句号孤行（见 O5）。
- **P8**：Q109–129 选项换行均在选项之间；完形 Q109–116、对话 Q145–149、写作 Q150 无徽章（见 D5）；答案区字号可读，键与注册表一致；Hiroshige 图片 + 署名 ✓；答案区带空格日期（见 D4）。
- **总体**：8 版均无溢出、重叠、压页脚；图片与出处一一对应。

### §1.1 逐项独立核实

| 项 | 实测 | 结论 |
|---|---|---|
| 纸色 #fbfaf6 | 8 个 SVG 均有纸色矩形 | ✓ |
| 无金色 | gold `#b49a4a`/`#b3a06a` 0 处；`#f7f1e2` 0 | ✓ |
| 无双线外框 | stroke-width ≥2 边缘矩形 0 | ✓ |
| 无近黑底 | dark `#2a2419`/`#2c2822` 0 | ✓ |
| 拉丁正文 Newsreader | 字体统计 Newsreader 917 / Noto Sans CJK SC 636 / Noto Serif CJK SC 116 / UnifrakturMaguntia 1 / DejaVu Sans 4；Noto Serif CJK SC 跨度内拉丁词 0 | ✓ |
| 分隔全用全角空格 | 「·」在 8 个 SVG + .text.md + ABSTRACT.txt 均为 0；「　」各版分布：P1 35、P2 33、P3 19、P4 29、P5 23、P6 24、P7 15、P8 184，.text.md 390（P1 的 35 对 KIT 称 37 为计数口径差异，SVG 文本抽取 vs 原始文本，不计问题）；P8 答案连接符已同步改「　」 | ✓ |
| 版心 54/66/48pt | 独立核实：MX x=88px=66pt ✓；栏目带 y=72px=54pt ✓（P2 SVG）；页脚线 y1=2596 ✓；页码基线 y=2624 ✓；页面 1950×2700（1462.5×2025pt）✓ | ✓ |
| 徽章色 | A2 `#5c6e30`、B1 `#46581f`、B2 `#37402f` | ✓（颜色对；数量见 D5） |

### 内容与事实（全部 150 题逐题复核，键全部正确）

- **150 题答案逐题独立验算**：对题干、原文、图表再验算，含 P8 Q109–150（尤其 Q131「Si tu venais dimanche, tu verrais les finales」正确，与 pt 的 Q131 键错教训不同）；Q121「A (semble)」确认非 B。**全部 150 键正确**（D2 的 Q84 键本身正确，但题无据可答；D6 的 Q2/Q3/Q11/Q13 键为预期答案，但空格另有合法答案）。
- **金句 8/8 逐字出自本期正文**（脚本核查；第 8 句「Une semaine en trois temps: voter, fêter, jouer.」在正文出现两次）。
- **P1 头条标题**「Alcaraz, roi de Paris: le Sénat tranche mercredi」= **41 个非空白字符 ≤ 56**；导读条 37 字符 ≤ 56。
- **§8.1 译注**：全部译注词均在同页正文出现，0 失败（脚本 + 人工通读）。**但词表词见 D3**。
- **页脚**：`第{n}版／共8版` 每页 1 次、1–8、无空格，印刷版文字层 ✓。
- **P7 读者来信**：明确标注 `Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)` + 法文说明「aucun texte du VOL.4 n'était arrivé au moment de mettre sous presse. Le VOL.5 reprendra la promesse.」+ 对应中文说明——无编造来信，符合 F-MAIL 规则（未查邮箱；投稿只认用户直接发来的，无即无）。✓
- **W46 承诺兑现项**：巴黎大师赛阿尔卡拉斯 7-6(5), 7-5 胜谢尔顿、11 月 8 日 ✓（ATP + AP/Sportsnet/NBC；9 个大师赛冠军、首个巴黎冠军、首盘挽救 6 个破发点、次盘 6-5 破发；种子：兹维列夫 1、阿尔卡拉斯 2、谢尔顿 3；第 41 届为 ATP 巡回赛周期第 41 届；辛纳 2025 卫冕冠军、因膝伤 2026-10-06 赛季结束）；预算投票：11 月 3 日投票未发生、11 月 4 日晚 458–0 否决 ✓（scrutin n° 9759，2 票弃权；全文一读落败，政府原版送参议院；投票曾两度推迟 10 月 20 日、11 月 3 日；参议院 11 月 20 日起审议国家预算、12 月 9 日庄严投票；70 天期限 12 月 17 日午夜）；PLFSS：10 月 23 日 115–1 否决（22 弃权）、参议院 11 月 9 日周一起辩论、11 月 18 日 16:30 庄严投票、1200+ 修正案、赤字 21.8→12.7 Md€、养老金指数化门槛 1260→1500€ 提议 ✓；P6 自我更正段落完整 ✓；参议院 18 日投票写「est prévu」✓；博若莱新酒 11 月 19 日、75 周年 ✓（Inter Beaujolais；第三个周四规则自 1985；1951 年首次提前售酒；采收自 8 月 13 日；Agreste：勃艮第-博若莱 −22% vs 2025；仅佳美；两个 AOC；Sarmentelles 11 月 18–22 日、23:00 火炬游行、午夜开桶；里昂 11 月 18 日 23:00 拖拉机运抵、午夜 Terreaux 广场开桶；500+ 活动）。
- **其他事实**：都灵总决赛 11 月 15–22 日、Inalpi Arena、8 人名单（兹维列夫、阿尔卡拉斯、谢尔顿、梅德韦杰夫、科博利、菲斯、蒂亚福、若达）、辛纳缺席、若达 Race 第 9（3,234 分）11 月 6 日入围、4 名首秀、抽签 11 月 12 日约 12:45 CET、小组赛 15–20 日、半决赛 21 日、决赛 22 日 ✓；法国国家联赛 A1 组 4 场 10 分（3 胜 1 平）、意大利–法国 11 月 12 日 20:45 圣西罗、法国–土耳其 11 月 15 日 20:45 波尔多 ✓；法甲第 11 轮 11 月 20–22 日五场赛程时间全对 ✓；11 月 18 日六部影片（Les Braves、Jupiter、Malika、Camembert、Fais-moi un signe、Hunger Games）及导演/主演全对 ✓；SERD 11 月 21–29 日、ADEME 协调、主题「Passer de l'ultra-conso à la consommation responsable」✓；星期/日期：11 月 16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、11 月 3 日周二、4 日周三、8 日周日、9 日周一、12 日周四、15 日周日、27 日周五（黑色星期五）均与报纸一致 ✓。

### p8.py 工具说明

使用的为改动后工具（未提交；fr builder 仅 3 处小改动：`split_joined` 在空白折叠前将「　」归一为内部标记；定位失败时回退带 `(?<![\d.])` 前瞻的空白边界；joined 检测接受 `[·　]`）。提取行为正常，无异常；向后兼容性已验证（见上）。未改动工具、未提交任何东西。

---

## 待协调员处理

1. D1–D6 六条缺陷须 builder 修复后重跑校对（proofread-until-zero）。
2. D4 的口径冲突：de 第一轮曾判带空格「第 N 版」通过；ko2 与本校对判为缺陷。请统一 §1.1 执行口径。
3. O2「16 部新片」计数来源建议补注；O1 配对顺序建议后续模板打乱。

## 工作文件

- 校对笔记：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr/PROOF-NOTE-fr.md`（本文件）
- 渲染图：同目录 `pages/p-1.png` … `p-8.png`；日志：`occlusion.log`、`p8-extract.log`、`p8-old-extract.log`、`p8-current.json`、`check-mcq.log`、`vol5-textmd.txt`、`print.txt`、`web.txt`、`textlayer-diff.txt`、`registry.json`、`build-copy/`。
