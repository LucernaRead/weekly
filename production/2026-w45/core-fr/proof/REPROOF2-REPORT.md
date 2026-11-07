# W45 法语核心 VOL.3 · 第二轮复校报告（SOP §8.4 第四轮修复后从头全量复校）

- 待校版本：`files/weekly-report-w45-fr-core/`（svg ×8、cards ×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 构建目录（只读，未导入、未执行）：`hidden_files/weekly-report-w45-fr-build/`
- 复校时间：2026-10-27 14:55–15:30 EDT（UTC 18:55–19:30）
- 本报告目录：`hidden_files/w45/fr-core-reproof2/`

## 结论（先行）

**不通过——但唯一问题在 KIT 统计数字，不在纸面。纸面本身 ZERO PROBLEMS。**

- 问题 1（KIT，唯一）：KIT §三“实测量化”逐版字符数与 shipped SVG 实测不符（见 §9）。按任务规则“纸面零问题但 KIT 不一致同样判不通过”，本轮判不通过。
- 修复成本极低：仅刷新 KIT §三数字为实测值（P1 4179 / P2 4227 / P3 4027 / P4 4619 / P5 3574 / P6 3904 / P7 4453 / P8 8399，合计 37,382），**无需改纸面、无需重渲染**。数字刷新后即可定稿。
- 本轮未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改任何源码、未派生下级代理；content 模块一律只 grep、未 import（SOP 工具 README 警示：import 会当场重写核心 SVG）。

## 0. 开工前查重

- 首次检查（18:55 UTC）：无渲染/构建进程；最近写盘为第四轮交付（SVG 18:52:30–31、卡 18:52:47–18:53:02、PDF 18:53:03–05、KIT 18:54:22 UTC）。
- 90 秒后复查（18:56:43 UTC）：两目录零新写盘、无 FR 进程。按协调员裁定（规则本意是无并发写盘者），正常开工。

## 1. 第四轮改动验证（唯一改动 content34.py:172）

- 源码行在位：`content34.py:172` 为 `41e édition en 2026 (40e anniversaire). Dernier Masters 1000 de la saison. En salle, sur dur, à Nanterre. Qualifications les 31 octobre et 1er novembre ; tableau principal du 2 au 8 novembre ; finales dimanche 8.`（只读 grep，未 import）。
- 纸面在位：P4 `LE MASTERS EN CHIFFRES` 框首句确为该新句（SVG 文本节点 + P4 卡面目视：框内排布正常，次段未动，无溢出、无重叠）。
- 旧句零残留：SVG 文本节点口径 `40e édition en 2026`（不含 anniversaire 后缀的旧句）= 0 处；`54e` = 0 处（原始 grep 的 base64 图片数据命中已排除，与前轮口径一致）。
- 全部 `40e` 处置（文本节点口径，与 KIT §8.8 处置表逐项核对一致）：
  - P4 新句中的 `(40e anniversaire)`：1 处，正确（1986 创立含首届 counting：2025=第 40 届、2026=第 41 届兼 40 周年；见 §7 外部核实）。
  - P3 菊花“绝不送生日”句及同句练习、P7 金句诊所引用 `un anniversaire. »`、P8 题面+答案注 `chrysanthèmes pour un anniversaire`：生日语境，与赛事无关，保留 ✓。
  - 题号 `40.`（P3）与配对 `140–144.`（P8）：编号，非届数，保留 ✓。
  - 他赛事：P1/P4 扇贝节 `22e édition`、P5 Pitchfork `15e édition`（含 Q63 选项）：保留 ✓。
  - KIT §8.5–§8.7 提及 `40e` 的历史记录行：保留原样（§8.8 已声明取代其事实结论），符合任务要求 ✓。
- 无连带引用：P4 微练习 Q56–61（finale/quarts/demi-finales/tableau/fauteuil/choc）、P4 Q44–46（决赛日期/场地/卫冕冠军）、P8 周末范文 Masters 句均无届数引用 ✓。
- 仅 P4 变化的证据链（附诚实限度）：
  - 第四轮时刻（18:52 UTC）唯一被触动的构建源码是 content34.py（mtime 18:52:27；content56 17:36、content7 17:43、content8 18:17 分属第二、三轮）。
  - content34.py 同时写 P3 与 P4（第 112/212 行 save），而 P3 SVG 哈希与 17:23 pre-fix 哈希逐字节一致，证明本次重渲染是确定性的、未引入其他漂移。
  - 当前 P4 SVG SHA-256 `240f379d…` 与 KIT §8.8 宣称的第四轮后值一致；P1/P2/P3/P5 与 pre-fix 逐字节一致。
  - 限度：手头没有第三轮后快照，无法直接逐字节 diff“第三轮后”状态；P6/P7/P8 与 17:23 pre-fix 的差异由第二、三轮源码改动（17:36/17:43/18:17）解释，不属于第四轮。以上证据链支持“第四轮仅 P4 变化”，但非直接 diff 证明。

## 2. 几何审计（SOP §8 几何门）

- `tools/occlusion_audit.py --selftest`：通过（6 类 planted 标记 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1 次，干净对照无标记）。
- 对 shipped SVG 目录实测：**0 flags**（exit 0）。
- 同基线墨迹碰撞补充扫描（审计 TEXTX 仅比不同行，同基线是已知盲区）：初筛 2 例候选，经审计同款字体（Noto Serif/Sans CJK SC，face SC=2）真墨实测均为误报——P1 头条→JOUR PAR JOUR 间隙 51px、P7 金句→语法点间隙 40px；P1 卡面目视亦确认无触碰。
- 图表区元素检查：本期无柱状图；后绘矩形 vs 文本的全部重叠候选均为框线级微触（占比 ≤0.10，DejaVu 近似口径），真墨审计 COVER（≥30%）静默；P1/P4/P7/P8 卡面目视无压线、无遮挡。P6 日历表为纯文本表，无条形遮挡。
- 卡面目视：P1、P4、P7、P8 全幅已看；P2/P3/P5 未逐幅看（其 SVG 与 pre-fix 逐字节一致 + 0 flags + 全文已读，见 §8 限度说明）。

## 3. P8 1–150 人工核对（SVG 题面 + 答案区 + 卡面，不只信工具）

- tools/p8.py extract 本版：noted 集 97/150（与任务书预警一致，属工具覆盖缺口，非纸面缺陷；第一轮 96→本轮 97 系 Q100 新注长度所致）。
- 人工口径结果：**题号 1–150 连续、无缺号、无重号；答案区 150 个条目首号顺序恰为 1–150；全部键逐题对照题源通过**（含易错点：Q114 avoir 后宾语在后不配合→A goûté；Q113 se promener→C；Q131 si+imparfait→venais；Q140–144 配对 a/b/c/d/e；Q145–149 对话 samedi/coquilles/goûter/recette/week-end；Q150 开放题+范文）。
- 逐题键表见本报告附录。
- 前三轮保留项逐项在位：
  - 第一轮：P8 Q114 键 A ✓；Q112 题干含 `un régal`、键 B ✓。
  - 第二轮：P7 金句 #4 为 P4 辩论框原文 `plus excitante ou plus frustrante ?`（B1 讲解段、B1 例句框、工具箱 B1 行三处同步 ✓）；后续题 Q100 键 `plus excitante`、级别 B1 ✓；金句 #8 为 P5 原文 `Les jeunes créateurs y rencontrent leur public, en vrai.` ✓；诊所 Q106 纠正主谓一致错误、键 rencontrent、注“créateurs 复数 → rencontrent，不是 rencontre”✓；P6 专栏旧句同步为 `Ce calendrier peut encore bouger.`（P6 正文 + P6 记者句框 + P7 B2 例句框 + P7 金句 #6 四处一致）✓。
  - 第三轮：Q120 题面 `Si j'étais libre dimanche, j'___ à Nanterre. A. irai · B. irais · C. vais`、键 B、级别 B2、注“si + imparfait → conditionnel présent；j' 是 je 在元音前的省音”✓；邻题 Q119（键 B）✓、Q121（键 A）✓ 不动。
  - 旧 Q120 形式（`je ___` / `j'irais` / `je vais` 选项）残留 0 处 ✓。

## 4. 分页与分级

- 实测分页：P1 10（1–10）/ P2 15（11–25）/ P3 18（26–43）/ P4 18（44–61）/ P5 17（62–78）/ P6 18（79–96）/ P7 12（97–108）/ P8 42（109–150）= 150。P8 的 42 = 编号题 28（117–144）+ 完形空 8（109–116）+ 对话空 5（145–149）+ 写作 1（150）。与任务书 FR 实测串一致；通用串 10/18/18/18/18/18/12/38 对 FR 不适用，未据此判不合格。
- 分级：136 个编号题面印刷级别 + 14 个 P8 无印刷级别题（完形/对话/写作）登记表级别 = **A2 53 / B1 75 / B2 22**，与 KIT 一致。推导：编号题面 A2 44 / B1 70 / B2 22；登记表补 109–116（A2×5、B1×3）、145–149（A2×4、B1×1）、150（B1×1）。登记表与印刷级别在 117–144 重叠区全部一致，故登记表口径可信。
- KIT 逐版题数（P1 10 / P2 15 / P3 18 / P4 18 / P5 17 / P6 18 / P7 12 / P8 42；P1–P7 微练习 108 + P8 42 = 150）与纸面一致 ✓。

## 5. P7 金句 8 条（来源文章 + 页码标签）

| # | 金句 | 页码标签 | 来源核实 |
|---|---|---|---|
| 1 | Le lundi 2 novembre, on reprend les cours. | page 2 | P2 正文+日期例 ✓ |
| 2 | On ne connaît pas encore les finalistes. | page 1 | P1 头条 ✓ |
| 3 | Les cimetières se sont remplis de chrysanthèmes. | page 3 | P3 正文逐字 ✓ |
| 4 | Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? | page 4 | P4 辩论框逐字 ✓ |
| 5 | Le festival se promène dans Paris. | page 5 | P5 正文 ✓ |
| 6 | Ce calendrier peut encore bouger. | page 6 | P6 正文+记者句框 ✓ |
| 7 | Ce week-end, tout se joue. | page 1 | P1 头条/本周词 ✓ |
| 8 | Les jeunes créateurs y rencontrent leur public, en vrai. | page 5 | P5 Creator Week 框 ✓ |

教学栏/工具箱的重复引用为 KIT 既定设计，不计缺陷。金句跟练 Q97–104 键全对（见附录）。

## 6. 读者角与 W43 预告

- 读者园地：编辑部示例明确标注 `(ce texte n'est pas une lettre de lecteur)`，法+中双语编辑部说明在版（截至付印未收到 VOL.2 第 8 版投稿，W44 未出刊；VOL.4 将兑现点评真实投稿）。无编造投稿、点评、读者姓名/引语 ✓。
- W43 VOL.2（weekly-report-vol4，页脚 VOL.2）P7 预告三项，逐项兑现：
  1. 万圣节 10 月 31 日 → P3 整版报道 + P1 快讯 ✓；
  2. 诸圣节 11 月 1 日 → P3 整版报道 + P1 快讯 ✓；
  3. 冬令时第一周 → 本期按“刚过去的报道”处理：法国 10 月 25 日入冬令时，本期为第二周（P1/P2 均表述为第二周，不再称第一周）✓；“夜里早读什么”有 P2 回应（短文本、一章、二十页）✓。
  - 披露项：W43 预告中的“18 时整点天黑”表述本期未沿用（全期只写“天黑得早/更早”，无整点时间）；KIT 事实池明示“无来源不重申整点日落时间”。属有披露的纠正，非 silent 遗漏——提请协调员确认此项是否计入“三项皆兑现”。
- VOL.4 预告（P7）：11 月 9 日参议院社保预算、11 月 11 日停战纪念日、11 月 14–15 日迪耶普扇贝集市、读者来信；与 P3 日历、P6“11 月 9 日起参议院审议”一致 ✓。

## 7. 事实 / 日期 / 星期（date -d，Europe/Paris）

- 全部核实通过：10/17 周六（假期始）、10/20 周二（议程来源日）、10/23 周五（115–1 否决）、10/25 周日（入冬令时）、10/31 周六（万圣节）、11/1 周日（诸圣节）、11/2 周一（复课+亡灵日）、11/3 周二、11/4 周三、11/5 周四、11/6 周五、11/7 周六、11/8 周日、11/9 周一（参议院）、11/11 周三（停战纪念日）、11/14 周六–11/15 周日（迪耶普集市）。
- 冬令时表述一致：10 月 25 日切换 → 10/26–11/1 为第一周、11/2–8 为第二周；P1“DEUXIÈME SEMAINE D'HIVER”与 P2“deuxième semaine”一致 ✓。
- 巴黎大师赛：主赛 11/2–8、资格赛 10/31–11/1、四分之一决赛 11/6、半决赛 11/7、决赛 11/8（含单打/双打/轮椅单打正午）；2026 决赛选手明确写“截稿时未知、周六晚揭晓”，无编造胜负 ✓。
- 外部核实（公开来源）：
  - 官方 Rolex Paris Masters 站：首届 1986 年、“2026 年庆祝 40 周年”→ 41 届/40 周年算术成立 ✓。
  - ATP 2025 决赛报道：Sinner 胜 Auger-Aliassime 夺 2025 巴黎大师赛冠军 → P4“2025 卫冕冠军 Sinner”成立 ✓。
  - Pitchfork 巴黎 2026：11/2–8、10 场地、约 100 艺人、Avant-Garde 11/5–7 巴士底、开幕夜 Iceage 双场 → P5 成立；首届巴黎 2011 + 2020 停办 → 2026 为第 15 届成立 ✓。
- 扇贝节区分：波尔诺曼底 Le Goût du Large 11/7–8（第 22 届）与迪耶普集市 11/14–15 严格区分，P3 日历、P7 预告均只在“将至”位置提迪耶普；Q8/Q124 干扰项 Dieppe/Courseulles/14–15 日均有明确区分意图 ✓。
- 预算周：P6 日程（3 日文化/媒体、4 日农业、5 日国土协调/科研、6 日公共财政/经济）全文标注“计划日程、结果未出”，不编造表决结果与民调 ✓。

## 8. 其他 SOP 项

- 刊头与配对徽章：8 版均有 `Le Lucerna`（法语冠词 Le，符合法语规则）；P1 徽章“法语正文 · 简体中文讲解 — 给简体中文读者的版本”；8 版页脚均为“Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文”✓。
- 图片：仅 P1–P3 各 1 图（SVG image 元素；P4–P8 0 图），全部 base64 内嵌；图说与出处均已排版：P1 Eugène Atget (1857–1927), photographie, domaine public；P2 Utagawa Hiroshige (1797–1858), estampe, domaine public · LACMA；P3 Flora de Filipinas (Blanco), XIXe siècle, domaine public；与构建目录 assets/CREDITS.md 及 KIT §六一致，均为公有领域 ✓。
- ABSTRACT.txt：366 字节、简体中文单行（仅 1 个换行符为行尾）、无 ASCII 双引号 ✓；KIT §七交付物描述一致（KIT 不逐字引用摘要文本，仅说明交付，此为描述方式而非不一致）。
- 红线：Ukraine/乌克兰 0 处、guerre 0 处；P6 预算周为法国国内政治（允许类），无国际政治 ✓。
- 双 PDF：均为 8 页；大报版 23,571,932 字节、网页版 5,257,574 字节，与 KIT §七第四轮实测一致；网页版 SHA-256 `855112b5f38586317b380ea1187d645c595df974283d7ee30083093ac47e952e` 与 KIT §8.8 一致（磁盘实测）；大报版 SHA-256 `92228133120dba3ab888bb47d7a782ffd9419767ac677d469459a9433082cad2` 与 KIT §8.8 一致。网页版为每页 1 张 JPEG 的光栅 PDF（故 pdftotext 为空），SVG 为权威文本源。
- 范文：P8 MODÈLE 空白分词 86 词，在 80–100 范围内，与 KIT 一致 ✓。

## 9. 唯一问题：KIT §三字符统计与实测不符（问题 1）

- 方法：对 shipped SVG 用 XML 解析器提取全部 `<text>` 节点（节点数 P1 177 / P2 178 / P3 187 / P4 197 / P5 160 / P6 172 / P7 169 / P8 267，与正则提取一致），strip 后求和（法语正文+中文讲解合计，即 KIT 宣称口径）。
- 对照表：

| 版 | KIT §三 | 实测 | 差 |
|---|---|---|---|
| P1 | 4306 | 4179 | −127 |
| P2 | 4230 | 4227 | −3 |
| P3 | 4007 | 4027 | +20 |
| P4 | 4595 | 4619 | +24 |
| P5 | 3538 | 3574 | +36 |
| P6 | 3889 | 3904 | +15 |
| P7 | 4187 | 4453 | +266 |
| P8 | 8135 | 8399 | +264 |
| 合计 | 36887（KIT 称“约 36,900”） | 37382 | +495（+1.3%） |

- 定性：正负号不一，排除统一口径偏移；P1 方向相反，排除“仅第二至四轮增字”解释；且 P1/P2/P3/P5 与 pre-fix 逐字节一致，故该组数字连 pre-fix 状态也不匹配——应为更早状态测量后未刷新，或另一未注明的口径。属 KIT 描述性统计 stale，不影响任何规范性内容（分页、分级、题数、尺寸、SHA、键、事实均已验证一致），但按任务 gate 规则仍判本轮不通过；刷新数字即可，无需动版。
- 限度说明：P2/P3/P5 卡面未逐幅目视（理由见 §2）；第三轮后快照缺失，§1“仅 P4 变化”为证据链结论而非直接 diff；W43 预告 18 时细节见 §6 披露项。

## 附录：P8 答案区 1–150 键表（人工核对稿）

1 finales · 2 nocturne · 3 coquilles · 4 reprend · 5 samedi soir · 6 saveurs · 7 C · 8 A · 9 B · 10 A ·
11 lundi · 12 1er · 13 samedi · 14 dimanche · 15 Les élèves vont reprendre les cours lundi. · 16 Nous allons lire vingt pages ce soir. · 17 Tu vas préparer ton cartable ce soir. · 18 Vous allez raconter vos vacances lundi. · 19 C · 20 B · 21 A · 22 a · 23 b · 24 c · 25 d ·
26 Vrai · 27 Vrai · 28 Faux · 29 Faux · 30 Vrai · 31 déguisement · 32 tombe · 33 citrouille · 34 souvenir · 35 On n'offre jamais de chrysanthèmes pour un anniversaire. · 36 Les feuilles ne sont plus vertes en novembre. · 37 Le 2 novembre n'est pas la Toussaint. · 38 nocturne · 39 badge · 40 Plailly · 41 B · 42 couleurs · 43 19 heures ·
44 B · 45 A · 46 C · 47 B · 48 A · 49 a · 50 b · 51 c · 52 d · 53 plus vite · 54 plus grand · 55 moins longue · 56 quarts · 57 demi-finales · 58 finale · 59 tableau · 60 fauteuil · 61 choc ·
62 B · 63 A · 64 C · 65 B · 66 A · 67 lieux · 68 paroles · 69 affiche · 70 ambiance · 71 danse · 72 découvre · 73 a · 74 b · 75 c · 76 d · 77 ce soir · 78 deux places ·
79 B · 80 A · 81 C · 82 A · 83 B · 84 C · 85 a · 86 b · 87 c · 88 d · 89 plus long · 90 moins simple · 91 aussi important · 92 examine · 93 ont rejeté · 94 part · 95 peut · 96 connus ·
97 reprend · 98 encore · 99 déguisés · 100 plus excitante · 101 promenons · 102 peut · 103 joue · 104 rencontrent · 105 On n'offre jamais de chrysanthèmes pour un anniversaire. · 106 Les jeunes créateurs y rencontrent leur public, en vrai. · 107 Il est prévu que l'Assemblée examine la Culture mardi. · 108 La finale a lieu dimanche 8 novembre. ·
109 C · 110 A · 111 B · 112 B · 113 C · 114 A · 115 C · 116 A · 117 B · 118 A · 119 B · 120 B · 121 A · 122 B · 123 A · 124 C · 125 C · 126 A · 127 B · 128 A · 129 A · 130 Les élèves vont reprendre les cours lundi. · 131 Si tu venais samedi, tu verrais la nocturne. · 132 Elle a goûté les coquilles à Port-en-Bessin. · 133 Selon moi, les finales sont excitantes. · 134 Il est prévu que le Sénat examine le texte lundi. · 135 读一份日程，本身就是在了解法国。 · 136 Il court plus vite que son frère. · 137 Les élèves sont en vacances depuis le 17 octobre. · 138 Ce soir, nous allons préparer nos cartables. · 139 On ne connaît pas encore les finalistes. · 140 a · 141 b · 142 c · 143 d · 144 e · 145 samedi · 146 coquilles · 147 goûter · 148 recette · 149 week-end · 150 开放题（按要点给分，范文在框内）。

## 审计脚本与输出（本目录）

- `audit_stems.py`：题号/级别解析（编号题面 136 + 答案区标记 150 顺序验证）。
- `audit_geom.py`：同基线/后绘矩形补充扫描（2 例候选均经真墨复核为误报）。
- 几何审计：`tools/occlusion_audit.py` 自检通过、shipped SVG 目录 0 flags（exit 0）。
- p8.py extract：noted 集 97/150（工具覆盖缺口，已用人工口径覆盖）。
