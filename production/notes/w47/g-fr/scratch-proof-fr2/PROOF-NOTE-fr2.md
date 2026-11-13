# PROOF-NOTE-fr2 — W47 法文核心版第二轮独立复校（叶子）

- 版：2026-w47-fr-zh-cn（目标 fr × 读者简体中文），VOL.4，刊期 2026-11-16..22
- 校对员：叶子（第二轮独立复校，与第一轮 builder、第一轮复校员、第一轮返修 builder 均不同；只读不改）
- 日期：2026-11-10/11（EST）
- 结论：**(b) 发现缺陷 + 清单** —— 新缺陷 2 条（D7、D8）。D1–D6、O5、O2 返修项全部独立实测通过；另 3 项遗留孤行裁定为观察（O6–O8）；de 版 P8 同类缺徽章已核实，报协调员裁定。

## 已核实的文件身份（与任务简报一致）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4.pdf`（印刷） | 30,446,210 B，8 页 1462.5×2025pt | `3833c9076893cd3be6c478407206d3540a4167d127acfba773be632f622dbcc5` |
| `La-Lucerna-VOL4-web.pdf`（网页） | 2,203,259 B，8 页 | `59341d013995a0841af8dc2148b5c85a9e8a047674f355e6895cb6f190b131b0` |
| `2026-w47-fr-zh-cn.text.md` | 46,095 B | `55295b25a5c23f6b1063947885878b8fefc42b8ce3934fece4d3e34dcaf3ed15` |

第一轮校对笔记实为 `scratch-proof-fr/PROOF-NOTE-fr.md`（任务简报所写 `PROOF-NOTE.md` 路径不存在；已按实际文件名全文读完）。FIX-LOG-fr.md 全文读完。

---

## 缺陷清单（本轮新发现）

### D7 — §8.1 译注词只在译注框内出现，共 4 词（§8.1 缺陷，与 D3 同类）

- **依据**：SOP §8.1「注释的词必须真实出现在正文里」。词表词用 D3 同标准；译注词同样：须在本版法语正文（文章/练习/其他内容框）中出现，**只在自己那条译注里出现一次等于没出现**。
- **核实方法**：SVG 全量文本节点枚举；先按词统计，再把浅底 `#f0eee5` 内容框内文本剔除后重数，最后对每词逐条看上下文。第一轮称「全部译注词均在同页正文出现，0 失败」——该结论有误：其计数把译注条目本身算作一次出现（本轮第一次 naive grep 同样误报 OK，剔除后才现形）。
- **4 词（全刊各出现恰好 1 次，且该次即译注条目本身；复数/屈折形式全刊 0 次）**：
  - P1 `un vainqueur`（译注「un vainqueur 获胜者」）：P1 正文、目录、快讯、Q1–Q10 均无 vainqueur。
  - P4 `un choc`（译注「un choc 强强对决」）：P4 正文、练习、评论员短语均无 choc。
  - P6 `une navette`（译注「une navette 两院往返审议」）：P6 正文无 navette（正文只写「part au Sénat」「commission」，未提 navette 机制）。
  - P6 `paritaire`（译注「paritaire 对等的、联合的」）：P6 正文无 paritaire（正文未提 commission mixte paritaire）。
- **对照（同法未判缺陷的近邻）**：P2 `réparer` 正文有 `répare`、P3 `trinquer` 正文有 `trinque`、P6 `réaliser` 正文有 `réalisé`、P4 `vainqueur` 在「À SUIVRE」框「le nom du vainqueur sera dans le VOL.5」、P5 `bande-annonce` 在配对 74——屈折/同版练习与内容框出现均计为出现。其余译注词均 ≥2 次且至少一次在正文。
- **修法建议**：二选一——(a) 把这 4 词自然写进同版正文/练习；(b) 删去或改写译注条目。P6 两词可随深读段补一句 navette/CMP 机制（须核实，不编造）。

### D8 — P7 Q100 语法点 `avoir lieu` 与所注金句不符（轻微内容缺陷）

- **位置**：P7 金句第 4 句语法点「avoir lieu：举行、发生。」；P8 答案注「100. beauté（avoir lieu 举行）」沿用同一标签。
- **问题**：所注金句为「Et dimanche 22 novembre, la semaine se termine en beauté : les finales de Turin, et le retour de la Ligue 1 — Marseille reçoit Le Mans à 20 h 45.」；Q100 题干为「La semaine se termine en ___ (beau).」，键 `beauté`。句中、题中均无 `avoir lieu`；考点实为 `se terminer en beauté`。Q97–99、Q101–104 的语法点（battre / arriver / voter / celui que / sortir / rejeter / trois temps）均出自所注句，唯 Q100 错配。
- **核实**：P7 SVG 中 `lieu` 全页仅此 1 处（即该语法点本身）；P8 答案区亦仅此 1 处。

---

## D1–D6 / O5 / O2 逐项独立验证（全部通过）

- **D1 ✓**：P5 正文「vingt-quatre ans avant Katniss」在位（SVG 文本抽取确认）；全刊 `cinquante` 0 处（`Cinquante` 仅 Q84 题干「Cinquante jours」1 处）；其余事实未动（11 月 18 日、2 h 38、Francis Lawrence、Haymitch 16 岁）。独立再核：JustWatch/Audible/Tatler/Capital FM 均称 24 years before Katniss / 50th Hunger Games / Haymitch 16 岁。
- **D2 ✓**：P6 日程图 7 行在位，含「26 nov. — Fin du délai de 50 jours (art. 47-1)」（卡面目视确认）；Q84 题干/选项/键 B 未动；读者可从图推出 B（题干「Cinquante jours」→ 图行「Fin du délai de 50 jours」→ 26 nov.）。外部核实：50 天期限（art. 47-1）确至 11 月 26 日（多源一致）。
- **D3 ✓**：13 词全部在同版正文段内（本轮两次独立脚本：SVG 词表框原文与署名精确剔除后整词匹配；.text.md 逐行剔除后复核）。`bouteille`「mettre leur vin en bouteille」、`raisin`「couper le raisin」、`vigne` 仅复数「dans les vignes」；`tennis`「tournoi de tennis」、`adversaire`「son adversaire, Ben Shelton」；`salle` 仅复数「dans les salles de cinéma」、`public`「le public a l'embarras du choix」（观众义，非署名）、`réalisateur`/`scénario`/`écran`/`acteur`/`actrice`/`séance` 均在 P5 正文。注：vigne、salle 仅复数形式出现，按第一轮「屈折形式计为出现」口径计通过。
- **D5 ✓**：全刊徽章 134 枚（SVG `rx="2.7"` 矩形计数：P1 10、P2 12、P3 18、P4 15、P5 14、P6 15、P7 12、P8 38）；分级 A2 `#5c6e30` 50、B1 `#46581f` 65、B2 `#37402f` 19；150−16 配对共享题 = 134，与登记表（A2 53/B1 75/B2 22；配对 22–25、49–52、73–76、85–88、140–144 各共享 1 枚）逐项对得上。P8 完形 Q109–116 行首 chip（A2/A2/A2/A2/B1/B1/B1/A2）、对话 Q145–149 标题后徽章条（A2/A2/B1/A2/A2）、写作 Q150 标题行首 B1 chip，卡面均目视确认。**算术订正确认**：150−16=134，第一轮笔记「应有 138 枚」确为误算。
- **D6 ✓**：P1 Q2/Q3 新题干「C'est ___ que le Sénat vote, le 18 novembre.」「C'est ___ que le beaujolais nouveau arrive, le 19 novembre.」在位；`le` 无法填入（「C'est le que…」不合语法）；与 P2 Q11/Q13（旧题干「Le Sénat vote ___ 18 novembre.」「Le beaujolais nouveau arrive ___ 19 novembre.」，未动）不再相同；键 mercredi/jeudi 不变；P8 答案区 Q2/Q3 注记仍为 mercredi/jeudi（「2. mercredi　3. jeudi（11 月 19 日新酒上市）」，SVG 与卡面均确认）。
- **O5 ✓**：P2 Q18「Dimanche, vous (regarder) les finales → ___」已单行（卡面确认）；P7 gp5「celui que：……的那个（关系代词）。」已单行（卡面确认）。
- **O2 ✓**：KIT §三有「16 部」计数口径注记（filmscinema.fr 同日计数不稳定未采用；六部点名影片已核实）。「16」本身仍无法证实亦无法证伪，维持观察。
- **D4**：按协调员裁定（全周统一口径：接受的 W46 做法，W47 不修，ko 除外），不列缺陷，不再提。

## de 版徽章核实（供协调员裁定；de 版已定稿后又返修 D6）

- de 全刊 chip 总数 **127**（`core-de/svg/*.svg` 直接计数：P1 10、P2 15、P3 18、P4 15、P5 18、P6 18、P7 12、P8 21），与 FIX-LOG 所称 127 一致。
- de P8 逐行 chip 映射（chip 与题号同栏、x 差 72px、dy 0–30 内）：**无 chip 的行 = 113–120（8 行）、145–149（5 行），写作标题「H SCHREIBEN」亦无 chip（P8 y>1400 仅 1 枚 chip，属 Q140 行）**——与 fr 返修前缺的 14 题（完形 8 + 对话 5 + 写作 1）同类、同数。
- 结论：**de 版同样缺这 14 枚 P8 徽章，属实**。注：de 各版分布与 fr 不同（P2 15、P5 18、P6 18 vs fr 12/14/15），「同结构」说法不精确，但 P8 缺 14 枚已在行级核实。de 是否需要补徽章返修轮次，请协调员裁定（本轮不碰 de 文件）。

## 返修 builder 留下的观察——逐项独立实测与裁定（均不构成缺陷）

- **O6 — P8 Q130 填空线孤行**：属实。SVG：题干「Futur proche : « Le Sénat vote mercredi. » →」在 y=814，填空「___」单独在 y=843（x=989）；卡面目视确认。**裁定为观察**：SOP §1.1 无「填空线不得孤行」规则（其换行规则只针对选择题选项不在选项中间折行）；与第一轮 O5 同类（O5 当时即为观察）；内容完整、无溢出。Builder 称超宽 15.3px，与实测一致（「→」止于 x≈1378，栏右缘 1411.5，仅余约 13px，而「___」约需 28px）；删句号/去空格仅省约 5px，无零风险修法。
- **O7 — P3 Q36/Q37 填空线孤行**：属实。SVG：Q36 题干 y=1831、「___」y=1865；Q37 题干 y=1964、「___」y=1997；卡面裁切放大确认。**裁定为观察**，理由同 O6。
- **O8 — P4「LES CHIFFRES DU SPORT」框中文注记孤行标点**：属实。中文注记「大师赛决赛结果与都灵名单见本版正文。」末尾「。」单独落在下一行行首（卡面裁切放大确认）。**裁定为观察**，理由同 O6（标点孤行不在 SOP 明文之列；不影响阅读；与 O5 同类）。

---

## 全量复校结果

### 事实（独立再核，2026-11-10/11 检索）

- 巴黎大师赛：Alcaraz 7-6(5), 7-5 胜 Shelton，11 月 8 日周日，南泰尔，巴黎首冠、第 9 个大师赛冠军、首盘挽救 6 个破发点、次盘 6-5 破发（ATP 官方 + AP/NBC/Sportsnet 多源一致）。种子（兹维列夫 1、阿尔卡拉斯 2、谢尔顿 3）、辛纳 2025 卫冕冠军、因膝伤 10 月 6 日赛季结束，均与第一轮核实一致。
- 预算：11 月 4 日晚国民议会收入部分 458–0（2 票弃权，scrutin n° 9759）否决，全文一读落败，政府原版送参议院（AFP + nosparlementaires.fr 多源一致）；投票曾两度推迟（10 月 20 日、11 月 3 日）；10 月 23 日 PLFSS 收入部分 115–1 否决（第一轮已核）；参议院 PLFSS 11 月 9–17 日辩论、正式投票「prévu」11 月 18 日周三（senat.fr 议程原文：explications de vote + scrutin public solennel；AFP/Public Sénat 一致）——**本期凡涉 18 日投票一律写「est prévu」，未写成事实，正确**；赤字 21.8→12.7 Md€、养老金指数化门槛 1260→1500€ 提议、参议院守住 12.7 Md€ 承诺（banquedesterritoires.fr/AFP）；50 天期限 11 月 26 日、70 天期限 12 月 17 日午夜、国家预算参议院 11 月 20 日–12 月 9 日，均与多源一致。
- 博若莱：11 月 19 日周四 0 时上市、第三个周四（1985 年法令）、75 周年、1951 年获准提前售酒（13 Nov 1951 note）、Sarmentelles 11 月 18 日晚午夜开桶、里昂拖拉机送酒、采收自 8 月 13 日、农业部预计勃艮第–博若莱 −22%、500+ 活动（Inter Beaujolais 经多源核实，均与本期一致）。
- 其余事实：都灵 11 月 15–22 日、8 人名单、4 名首秀、菲斯为法国人、抽签 11 月 12 日、小组赛 15–20 日、半决赛 21 日、决赛 22 日；法国 A1 组 4 场 10 分、意大利–法国 11 月 12 日 20:45 米兰、法国–土耳其 11 月 15 日 20:45 波尔多；法甲第 11 轮 11 月 20–22 日；六部影片及导演/主演；SERD 11 月 21–29 日、ADEME 协调与主题；11 月 20 日世界儿童日——均与第一轮核实一致，本轮重点复核无出入。
- 日期/星期（`date` 核验，Europe/Paris）：11 月 3 日周二、4 日周三、8 日周日、9 日周一、12 日周四、15 日周日、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、26 日周四、27 日周五、12 月 9 日周三、12 月 17 日周四、10 月 23 日周五、8 月 13 日周四——**全部与报纸一致**。11 月 19 日为 11 月第三个周四（5/12/19/26 日）。
- VOL.5 预告（都灵决赛结果、法国队与法甲第 11 轮赛果、11 月 27 日黑色星期五、参议院投票结果、读者来信）：只写已核实的日程与顺延承诺，无编造。

### 150 题答案键逐题独立验算

- `p8.py extract` 键表（150 键）与 `final-fr-p8.json` 逐项相同；与 `.text.md` RÉPONSES 区机械比对：**150 条解析、0 不符**。
- 逐题对照题干/原文/图表独立验算（P1–P8 全 150 题，含 P8 Q109–150 逐题重算、改动题 Q2/Q3/Q18/Q84/Q26/Q42/Q62–Q69 逐项复核）：**全部 150 键正确，每题仅一解**。其中：Q84 键 B 现可从 P6 日程图推出（见 D2）；Q2/Q3 在新题干下仅容 mercredi/jeudi；Q18 仅去句号，键不变；Q26（1951 年获准提前售酒）与新正文一致；Q42（13 日）与「dès le 13 août」一致；Q62–Q69 与新正文一致；Q113（Le cinéma *propose*，主语单数，B *proposent* 复数排除、C *se tient* 不接宾语）、Q114（avoir + 过去分词无配合，*aimé* 唯一）、Q121（*semble*）、Q131（si + imparfait → *venais*）、Q133（*Selon* moi，空在 moi 前）均唯一。

### 机械门（本轮全部重跑）

- `occlusion_audit.py`：自检 OK（6 类阳性对照触发、干净对照静默），**0 flags**。
- `p8.py extract --total 150`：印出注记集 **121/150**（parse: joined），与 `final-fr-p8.json` 逐项相同；缺失 29 题为无注记题，属正常（121/150 且 compare CLEAN 即通过）。`p8.py compare`：**CLEAN**，121/121，missing=[] extra_count=0 keydiff=[]。
- `freeze.py baseline`（从核心目录运行）：工具报告 **8/8** byte-identical（p1 `be2964d5713bf`、p2 `5709e000bbd7`、p3 `7828cfe33118`、p4 `785f4561ff32`、p5 `fff2a8d3d7ac`、p6 `8e569290ac8f`、p7 `077ebc44cfe4`、p8 `24ea15398fffc`，与 FIX-LOG 一致）；core integrity：交付 SVG 未被重建改动。
- 文字层：`pdftotext` 印刷版/网页版各 **46,353 字节**，词级多重集相等（7,240 词）；8 页 1462.5×2025pt。
- P8 最小字号：PyMuPDF 468 spans，最小 **11.62pt**（213 spans）≥ 9.75pt。
- MCQ 完整性：`check_mcq.py` 45 题体、1,437 行，**DEFECTS: 0，UNLOCATED: 0**。
- 全刊文本：150 题齐全（A2 53/B1 75/B2 22；分版 10/15/18/18/17/18/12/42，与 KIT 一致）；金句 8/8 逐字出自本期正文；范文 96 词（80–100 内）；头条 41 非空白字符 ≤56、导读条 37 字符。

### §1.1 逐项实测

| 项 | 实测 | 结论 |
|---|---|---|
| 纸色 #fbfaf6 | 8/8 有；旧纸 #f7f1e2 0 | ✓ |
| 无金色/近黑 | #b49a4a/#b3a06a 0；#2a2419/#2c2822 0 | ✓ |
| 无双线外框 | stroke-width≥2 的元素全为橄榄绿 #46581f 分隔线（2px=1.5pt，在 1.1–1.5pt 规范内）+ 1 条装饰 path；无边缘矩形 | ✓ |
| 徽章三色 | A2 #5c6e30、B1 #46581f、B2 #37402f，白字 rx=2.7 | ✓（数量见 D5） |
| 分隔符全角空格 | 「·」8 SVG + .text.md + ABSTRACT 均为 0；「　」P1 35/P2 33/P3 19/P4 29/P5 23/P6 24/P7 15/P8 181、.text.md 390（与返修后重测一致） | ✓ |
| 刊头 196px=147pt | P1 `Le Lucerna` UnifrakturMaguntia 196px 居中 | ✓ |
| 头条 53px=39.75pt | 低于 40pt 下限 0.25pt，像素取整所致；沿用第一轮可接受裁定 | 观察（已裁定可接受） |
| 无首字下沉 | P1 头条首段无放大首字（O4）；沿用第一轮/de 裁定（共有缺口、可接受） | 观察（已裁定可接受） |
| 字体 | Newsreader 926 / Noto Sans CJK SC 658 / Noto Serif CJK SC 116 / UnifrakturMaguntia 1 / DejaVu Sans 4；Noto Serif CJK SC 跨度内拉丁词 0 | ✓ |
| P2–P6 文章标题 | SVG 实测 32px=24pt，恰为次级标题范围上限（22.5–24pt）——KIT §7「38px=28.5pt 偏高」一语与 SVG 不符，属 KIT 文字有误（见下文），成品合规 | ✓（KIT 文字待订正） |
| VOL.4/VOL.5 | .text.md VOL.5 ×9、VOL.4 ×4；SVG VOL.5 9 处（P2 1/P4 2/P7 3/P8 3）、VOL.4 11 处；9 处 VOL.5 逐处核实均为合法下期指称（读者习作顺延、赛果顺延、编辑部说明、下周预告、Q111 题干、写作说明、答案注），**无一处把本期误印成 VOL.5** | ✓ |

### 目视（本轮自印刷版 PDF 重新渲染 100dpi，8 版逐版精读）

- P1：Q2/Q3 新题干在位；刊头/议程/目录/快讯/闪电问答/图注/页脚干净；Q7–10 选项完整。
- P2：Q18 已单行；Q11/Q13 未动；ET VOUS 中文注记经裁切放大确认在框内、未被裁切；图与框无溢出。
- P3：bouteille/raisin/vignes 已进正文；词表 10 词可见；Q36/Q37 填空线孤行（见 O7），余无异常。
- P4：tennis/adversaire 已进正文；Q44–48 选项整组完整；「LES CHIFFRES DU SPORT」框中文注记「。」孤行（见 O8）。
- P5：D1 已改（vingt-quatre ans / réalisateur / scénario / grand écran / salles / le public / acteur / actrice / séance）；电影词表 8 词可见；Méliès 图与图注干净。
- P6：日程图 7 行，26 Nov 行位置正确；Q79–84 选项完整；Q84 可答。
- P7：gp5 单行；8 金句、诊所、园地、预告、Doré 图均在；读者来信标注明确（见下）。
- P8：完形 8 枚徽章、对白条 5 枚、写作 B1 1 枚均画出；答案区 1–150 齐全；Hiroshige 图已放置；页脚干净。Q130 填空线孤行（见 O6）。
- 总体：8 版均无溢出、重叠、压页脚、豆腐块。

### KIT 核查

- §7 门禁输出与本轮实测一致（徽章 134 与 50/65/19、freeze 8/8 及各页哈希、P8 11.62pt、两 PDF 尺寸/SHA、.text.md 46,095 B/SHA、§1.1 计数）；§8 第 4 轮返修记录完整；§三「16 部」注记在位；§二承诺清单逐项兑现（巴黎大师赛结果、预算投票自我更正、博若莱 11 月 19 日、VOL.5 顺延；真实来信未收到，沿用标注示例，见下）。
- **KIT 文字小误（观察，非成品缺陷）**：§7「未改动」段称「P2–P6 文章标题 Flow.title 38px=28.5pt（规范上限高 4.5pt）」——SVG 实测标题字号为 32px=24pt（第一轮 (a2) 已裁定合规），38px 并非实际印出字号。请协调员订正 KIT 该句，以免后人误读。
- **F-MAIL**：P7 读者园地明确标注 `Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)` + 法文说明「aucun texte du VOL.4 n'était arrivé au moment de mettre sous presse. Le VOL.5 reprendra la promesse.」+ 对应中文说明——无编造来信，符合「投稿只认用户直接发来、无即无」规则。未查邮箱（任务禁令；KIT §九第 1 条仍请协调员入仓前核实邮箱状态）。
- 工作树状态：本轮未改任何源码/成品；`git status` 显示 `tools/freeze.py`、`tools/p8.py` 有未提交修改——为返修前已有的 builder 工具扩展（KIT §九第 2 条待复核），非本轮所改；`production/2026-w47/core-fr/` 为未追踪新目录（既有状态）。freeze 重建未改动交付 SVG（core integrity OK，render.py diff 为空）。

---

## 留待观察（非缺陷）

- O1（第一轮）：五组配对题顺序一致，答案必然 a/b/c/d 顺序对应；SOP 未要求打乱，维持观察。
- O2（第一轮）：「16 部新片」计数未证实亦未证伪；KIT 已补口径注记，维持观察。
- O3（第一轮）：P4「la course, arrêtée lundi 9 novembre」措辞略不精确，非事实错误；维持观察。
- O4：P1 头条首段无首字下沉（已裁定可接受）；头条 39.75pt（已裁定可接受）。
- O5（第一轮，已修）：P2 Q18、P7 gp5 本轮确认已单行。
- O6–O8（本轮新记）：Q130、P3 Q36/Q37、P4 体育数字框注记的孤行填空线/标点（见上文裁定）；建议后续在 wrap 引擎层面处理「→ ___」不可拆分，而非逐题改写。
- D4：协调员已裁定不修，不再列入。

## 工作文件

- 本笔记：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr2/PROOF-NOTE-fr2.md`
- 渲染图：同目录 `p-1.png` … `p-8.png`；裁切图 `crop-p2-etvous2.png`、`crop-p3-q3637.png`、`crop-p3-q37.png`、`crop-p4-chiffres2.png`、`crop-p8-q130b.png`；日志与脚本：`print2.txt`、`web2.txt`、`keys2.txt`、`d3-verify2.py`、`d3-verify2b.py`、`freeze2/`。
