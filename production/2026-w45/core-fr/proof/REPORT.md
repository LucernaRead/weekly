# W45 法语核心 VOL.3 — 独立复校报告（SOP §8.4，修复后从头全量复校）

## 结论先行：不是 ZERO PROBLEMS — 1 项纸面问题待协调员裁定

**问题清单（仅 1 项，见 §1）。除 §1 外全部通过，包括三轮修复的每一项、P8 1–150 人工核对、分级、几何审计、KIT 尺寸一致性、ABSTRACT、红线、读者角披露、图片署名。**

- 若协调员裁定 §1 接受（即把 “40e édition” 当作赛事官方 “40th anniversary edition” 的简写），则其余项为零问题，可定稿。
- 若按严格届数 counting，§1 须改 1 处文字（仅 P4 数字框，无题键影响）后重渲染 P4 + 双 PDF，再做一次 P4 专项复核即可，不必全量重校。
- 本复校**只读**：未改任何源码/SVG/KIT，未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git。

## 开工查重

- 开工时无渲染进程在跑；files/ 与 build/ 最近写盘为本次交付（2026-10-27 18:17–18:19 UTC），90 秒复查零新写盘（snapshot1.sha256 = snapshot2.sha256），按协调员裁定（规则本意是无并发写盘者）正常开工。

## §1 问题清单

### 问题 1（事实措辞，P4）：「40e édition en 2026」与严格届数不符

- 纸面位置：P4 `LE MASTERS EN CHIFFRES` 首行：“40e édition en 2026.”
- KIT §8.6 第一轮的理由是“赛事 1986 年创立，2026 年为第 40 届”——这是 2026−1986 的周年数，不是届数。按含首届的届数 counting：1986 为第 1 届，则 2025 为第 40 届、2026 为第 41 届。
- 独立证据（非采信自述）：
  - ATP 官方 2025 赛季前瞻称 2025 年赛事为 “the 40th edition of the tournament”。
  - 赛事官网 2026 赛季文章称 2026 为 “40th anniversary edition” / “celebrating its 40th anniversary this year”——即 40 周年版，不是第 40 届。
  - ATP 的“2025 年为第 40 届”一说本身即锚定了含首届 counting（1986 为第 1 届）；2020 年亦举办，无停办年份可抵消这一届差。
- 建议改法（二选一，由协调员定，不由复校员擅自改）：
  - (a) `41e édition en 2026 (40e anniversaire)`；或
  - (b) 删届数、只写 `40e anniversaire en 2026`。
- 影响面：仅此 1 处文字；P4 练习、P8 答案均不涉及届数，无题键连带改动。任务书要求核实的“巴黎大师赛 11/2–8 与 40 周年”中，11/2–8（资格赛 10/31–11/1、主赛 11/2–8、四分之一决赛 6 日、半决赛 7 日、决赛 8 日、轮椅单打决赛 8 日 12 时）全部核实无误，唯届数措辞与“周年”混淆。
- 注：第一轮 54e→40e 的改动本身已落地（全量 grep 54e 为 0，见 §2），本问题不是“旧错未改”，而是第一轮定下的 40 这个数在严格 counting 下仍差 1。

## §2 三轮修复逐项验证（全部在位）

### 第一轮
- P4 届数：`40e édition en 2026` 在位；`54e` 全量 SVG 文本节点 grep = 0（原始 SVG base64 串中的偶然命中不计，属图片数据）。
- P8 Q114 键 B→A：在位。题面 `Léa a (114)___ la musique.`，选项 A. goûté / B. goûtée / C. goûter，答案区 `114. A（avoir + 过去分词 goûté（不配合））`。法语上正确：avoir 助动词、直接宾语后置，故不变格。
- P8 Q112 题干加 `un régal` 消歧、键 B 不变：在位。题面 `« À Port-en-Bessin, on a (112)___ des coquilles, un régal ! »`，选项 A. acheté / B. goûté / C. vendu，答案 `112. B（品尝语境（un régal）→ goûté）`。

### 第二轮
- P7 金句 #4（Q100）：P4 辩论框原文 `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?` 在 P7 三处同步在位——B1 比较级讲解段首例、B1 例句框（`le comparatif du débat sportif (page 4)`）、工具箱 B1 行；金句 #4 讲解 `comparatif：plus + 形容词，ou 对举。`；跟练 `La finale est ___ (excitante) !`；键 `plus excitante`；级别徽章为 B1（卡面目视亦为 B1）。旧句 `En salle, la balle va plus vite` 文本节点 = 0。
- P7 金句 #8（Q104）+ 诊所 Q106：金句 `Les jeunes créateurs y rencontrent leur public, en vrai. (page 5)` 在位，与 P5 Paris Creator Week 框末句逐字一致；跟练 `Ils ___ (rencontrer) leur public.`，键 `rencontrent`；诊所 Q106 错句 `✗ « Les jeunes créateurs y rencontre leur public, en vrai. »`，答案注 `主谓一致：créateurs 复数 → rencontrent，不是 rencontre`。旧句 `Le festival dure sept jours` = 0；单数旧错 `sept jour`（不带 s）= 0，现存两处均为正确复数 `sept jours`（P5 正文与 Q62 选项）。
- P6 专栏旧句同步：`LES PHRASES DES JOURNAUX` 框第二句 `« Ce calendrier peut encore bouger. »` 在位。保持不动的两处经核实确属非引用句，正确：P6 深读段句中形式 `ce calendrier peut encore bouger`（小写句中成分）；P6 微练习 `Le calendrier ___ encore bouger.`（动词填空，键 peut）。旧引用句 `Le calendrier peut encore bouger`（无 Ce 的引句形式）文本节点 = 0。

### 第三轮（唯一改动 content8.py:49）
- 源码第 49 行在位：`("B2", "B", "si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j' 是 je 在元音前的省音", "Si j'étais libre dimanche, j'___ à Nanterre. A. irai · B. irais · C. vais")`。
- 纸面 P8 B 区在位（SVG 文本 + P8 卡面目视）：`B2 120. Si j'étais libre dimanche, j'___ à Nanterre. A. irai · B. irais · C. vais`，填入 B 得 `j'irais`，无主语重复；级别徽章仍 B2；答案区 `120. B（si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j' 是 je 在元音前的省音）`。
- 旧题干/旧选项/旧注零残留（SVG 文本节点口径）：`Si j'étais libre dimanche, je ___` = 0；`j'irais`（作选项或旧注）= 0；`je vais` = 0；旧注 `conditionnel j'irais` = 0。新选项与新注仅见于 Q120 一处。
- 邻题一律不动：在位且与第二轮一致——Q119 `Elle s'intéresse ___ festivals. A. à les · B. aux · C. des`，键 B，注 `s'intéresser aux（à+les）`；Q121 `À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant`，键 A，注 `主语 ce programme 三单 → semble`。
- P1–P7 与第二轮后一致性的佐证与限度：文本节点口径下，P1–P7 恰含第一轮 + 第二轮的全部预期字符串、且不含任何第三轮改动字符串；build 目录源码时间戳亦显示第三轮仅 content8.py 在 18:17 改动，其余 content 文件停留在第二轮时间。但**第二轮 SVG 快照未在本复校视野内留存，逐字节一致性无法独立复现**——此为限度说明，不是已证伪；KIT 第三轮“P1–P7 逐字节一致”的说法本复校未采信为证据，仅记录为构建方自述。另：现 SVG 哈希与 build 目录 pre-fix-hashes.txt 对照，P1/P2/P3/P5 完全一致，P4/P6/P7/P8 变化——变化页恰为第一、二轮触及的页，与“第三轮仅动 P8 源码”一致（P4/P6/P7 的变化应归于第一、二轮，而非第三轮）。

## §3 全量复校（SOP §8，与首轮同标准）

### 几何审计
- `tools/occlusion_audit.py --selftest`：通过（6 类 planted 标记各 1 次，干净对照无标记）。
- 本版审计：**0 flags**（exit 0）。`--core` 同目录复核：`core: 0 flags; NEW vs core: 0`。
- 图表区元素人工核对：P1 决赛周末日程、P1 逐日表、P2 日期栏、P3 本周日历、P4 数字框、P6 计划日程表（mar. 3 Culture · mer. 4 Agriculture · jeu. 5 Cohésion · Recherche · ven. 6 Finances · Économie）均与正文及练习 79–82 一致，无错位文字；P8 卡面与 P7 卡面全页目视无重叠、无压线。

### P8 1–150 人工核对（SVG 文本 + 卡面，不只信 tools/p8.py）
- 题号：1–150 连续、无缺号重号。实测分页（按题号）：P1 10（1–10）、P2 15（11–25）、P3 18（26–43）、P4 18（44–61）、P5 17（62–78）、P6 18（79–96）、P7 12（97–108）、P8 42（109–150，含写作 150）= 150。P1–P7 微练习 108 题 + P8 综合评估 42 题。
- 分级（登记表口径，含 P8 未在版面印级别徽章的 A 区与 G/H 组）：A2 53 / B1 75 / B2 22 = 150，与 KIT 一致。P1–P7 实测：A2 37 / B1 56 / B2 15 = 108；P8：A2 16 / B1 19 / B2 7 = 42。
- tools/p8.py extract：keys = 150/150（全部题号均有印刷键），noted 集 = 97/150——与第二轮一致，属已知工具覆盖缺口（仅印出简析的题才计入 noted 集），非纸面缺陷；人工口径已覆盖全部 150 题的题面与键。
- 逐节键核对（抽查逻辑全部通过，含易错点）：P1 1–10、P2 11–25（含 19 C ensemble lundi、20 B 25 oct.）、P3 26–43（含 28/29 Faux、35–37 否定改写）、P4 44–61（含 53 plus vite、55 moins longue、61 choc）、P5 62–78（含 71 danse、72 découvre、77 ce soir、78 deux places）、P6 79–96（含 83 B 115–1、84 C 9 nov.、95 peut）、P7 97–108（含 98 encore、99 déguisés、100 plus excitante、104 rencontrent、105–108 改错）、P8 109–150（含 109 C dimanche、113 C se promène、115 C ont lieu、120 B 新题、131 Si tu venais、134 examine、136–139 翻译、140–144 a–e、145 samedi、147 goûter、148 recette、149 week-end、150 开放题）。
- 范文：P8 范文空白分词实测 86 词，在题面要求的 80–100 词内（KIT 称 86，与实测一致）。

### P7 金句 8 条
- 8 条逐字连续摘句（仅句首大写与句末标点截断属既定容许）与页码标签全部正确：
  1. `Le lundi 2 novembre, on reprend les cours.` (page 2，P2 例句)；
  2. `On ne connaît pas encore les finalistes.` (page 1，P1 正文)；
  3. `Les cimetières se sont remplis de chrysanthèmes.` (page 3，P3 正文)；
  4. `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?` (page 4，P4 辩论框)；
  5. `Le festival se promène dans Paris.` (page 5，P5 正文)；
  6. `Ce calendrier peut encore bouger.` (page 6，P6 栏目句)；
  7. `Ce week-end, tout se joue.` (page 1，P1 MOT 框冒号前部分)；
  8. `Les jeunes créateurs y rencontrent leur public, en vrai.` (page 5，P5 创作者周框)。
- 关于任务书“各恰 2 次”的口径说明：若指“来源文章 + P7 金句表”这一对，则 8 条全部满足；P7 内教学栏/工具箱对 #1、#2、#4、#6 的重复引用是 KIT 既定教学设计（栏内例句与工具箱随身句），故全报原始出现次数高于 2，不应按原始全报计数判为缺陷。KIT 本身未立“恰 2 次”的原始计数规则。

### 事实 / 日期 / 星期（Europe/Paris，date -d 实测）
- 全部星期–日期配对正确：10/17 星期六（假期始）、10/23 星期五（115–1 否决）、10/25 星期日（冬令时切换日，CEST→CET）、10/31 星期六（万圣节）、11/1 星期日（诸圣节）、11/2 星期一（复课 + 亡灵日）、11/3 星期二（文化）、11/4 星期三（农业）、11/5 星期四（国土协调/科研）、11/6 星期五（财政/经济）、11/7 星期六（半决赛 + 最后夜场）、11/8 星期日（决赛）、11/9 星期一（参议院起审）、11/11 星期三（停战纪念日，VOL.4 预告）、11/14 星期六–11/15 星期日（迪耶普集市，VOL.4 预告）。
- 冬令时表述一致：P1 与 P2 均称本周为“第二周”，法国 10 月 25 日进入冬令时后，11/2–8 确为第二周；未再表述为第一周。
- 巴黎大师赛：资格赛 10/31–11/1、主赛 11/2–8、决赛 8 日、轮椅单打决赛 8 日 12 时，均与赛事官网 2026 信息一致；2025 卫冕冠军 Sinner 仅作背景，未编造 2026 决赛选手与胜负（全文“截稿时未知、周六晚揭晓”）。
- Pitchfork：11/2–8、10 场地、约 100 艺人、开幕夜 Headache/Iceage/DIIV、Avant-Garde 11/5–7 巴士底、俱乐部夜 11/6–7；第 15 届经含首届 counting 核实（2011–2019 共 9 届、2020 停办、2021–2026 共 6 届，合计 15 届）。
- 预算周：10 月 23 日社保预算收入 115–1 被否决、法案送交参议院 11 月 9 日起审议，均有公开报道佐证；P6 全文标注“计划日程、结果未出”，未编造表决结果与民调。
- 创作者周：11 月 4–5 日拉维莱特，与公开报道一致。
- 扇贝节：P1 称 22 届、11/7–8 日；迪耶普集市 11/14–15 日仅在 P3 日历“将至”位置与 P7 VOL.4 预告出现，与本周波尔诺曼底扇贝节严格区分，未混淆。22 届一数未找到反证，不列为问题。

### W43 VOL.2 预告三项兑现
- W43 预告的 10/31 万圣节、11/1 诸圣节、冬令时第一周，在本期均按“刚过去的报道”处理：P1 快讯 + P3 双报道（笑声在前、纪念在后）+ P2/P1“第二周”表述；未把冬令时第一周安在本周。三项皆已兑现。

### 读者角
- P7 读者园地：示例文明确标注 `Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)` 及中文“编辑部示例”；法语 + 中文双语编辑部说明在位：截至付印未收到 VOL.2 第 8 版投稿作文（W44 未出刊），VOL.4 将兑现点评真实投稿的承诺。无编造的读者姓名、投稿或点评。

### 图片
- 3 图全部公有领域、署名已排版且与素材库 CREDITS.md / KIT §六一致：P1 Eugène Atget (1857–1927), photographie, domaine public；P2 Utagawa Hiroshige (1797–1858), estampe, domaine public · LACMA；P3 Flora de Filipinas (Blanco), XIXe siècle, domaine public。图片 base64 内嵌 SVG，无外链依赖。

### 红线
- 无国际政治：全文无战争、地缘、外国事务内容（grep 命中仅 `botanique` 一词内含 `otan` 子串，属误报）；P6 为目标国国内政治（国民议会预算周），在红线允许范围内。

### ABSTRACT 与 KIT 一致性
- ABSTRACT.txt：简体中文单行（366 字节，1 个非空行），无 ASCII 双引号；内容含刊名、分级、题数与本周真实关键词（复课、大师赛决赛、阿斯泰里克斯最后夜场、波尔诺曼底扇贝节、Pitchfork、法甲、预算周），与纸面一致。
- 双 PDF 实测（磁盘比对，非沿用 KIT 数）：均为 8 页；大报版 23,571,927 字节，网页版 5,146,272 字节——与 KIT §七及 §8.6 第三轮记录完全一致。
- 网页版 SHA-256（供入仓 pdfSha256 实测复核用）：`a61538b1c0fdfc302323f299d8c7381cf68f9a72edd5127ed62823353e3c8e8f`；大报版 SHA-256：`1a5cc0124f2758d62e3274ae3ca9736e5a78aa3cee18c85feee780d75df1821c`。
- 卡面：8 张 PNG 均为 1950×2700；SVG 8 个、卡 8 张、双 PDF、KIT、ABSTRACT 齐全。
- KIT 与纸面其余一致项：总量 150、分级 53/75/22、范文 86 词、P8 42 题、VOL.4 预告三项（11/9 参议院、11/11 停战日、11/14–15 迪耶普）均与纸面一致。

## 任务书口径勘误（非纸面问题，协调员请修正清单）

- 任务书所列分页 `10/18/18/18/18/18/12/38` 与纸面及 KIT 均不符。实测与 KIT §二/§三一致的分页为 **`10/15/18/18/17/18/12/42`**（P2 为 15 而非 18，P5 为 17 而非 18，P8 为 42 而非 38；三处误差恰抵消，总量仍为 150，分级亦不受影响）。纸面与 KIT 在此项上互相一致，故不应据任务书串判纸面不合格；请协调员将清单改为实测串。

## 审计输出路径

- 本报告：`hidden_files/w45/fr-core-reproof/REPORT.md`
- 几何审计：`hidden_files/w45/fr-core-reproof/occlusion.txt`、`occlusion.json`、`occlusion_selftest.txt`、`occlusion_core.txt`、`occlusion_core.json`
- P8 工具提取：`hidden_files/w45/fr-core-reproof/p8_extract.txt`、`p8_extract.json`（keys 150/150，noted 97/150）
- SVG 文本提取：`hidden_files/w45/fr-core-reproof/p1-une.txt` … `p8-exercices.txt`
- 开工快照：`hidden_files/w45/fr-core-reproof/snapshot1.sha256`、`snapshot2.sha256`（一致，零新写盘）
