# PROOF-NOTE-fr3 — W47 法文核心版第三轮独立复校（叶子）

- 版：2026-w47-fr-zh-cn（目标 fr × 读者简体中文），VOL.4，刊期 2026-11-16..22
- 校对员：叶子（第三轮独立复校，与 builder、第一/二轮返修 builder、第一/二轮校对员均不同；只读不改）
- 日期：2026-11-11（EST）
- 结论：**(b) 缺陷清单 —— 新缺陷 1 条（D9，轻微）**。D7、D8、D3、KIT 文字订正全部独立实测通过；150 题键 0 不符；机械门全套重跑通过；§1.1 逐项重测通过；8 版卡面目视通过。
- 依据：SOP.md §8/§1.1 全文、`AGENTS.md`、`FIX-LOG-fr2.md` 全文、`PROOF-NOTE-fr2.md` 全文已读。
- 工作记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr3/`（本笔记 + 门禁日志 + 自写验证脚本与全部工具输出）

## 已核实的文件身份（与任务简报逐项一致）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4.pdf`（印刷） | 30,447,011 B，8 页 1462.5×2025pt | `98c8e128a53953e063b28b98fc98e6468c3b72e42a5a9868349a9def1bd2b61c` |
| `La-Lucerna-VOL4-web.pdf`（网页） | 2,205,780 B，8 页 | `e25434430c2b2e0415adf26ef960126665c5c9434a78adf5d03f49c06717250e` |
| `2026-w47-fr-zh-cn.text.md` | 46,445 B | `3210f6ba62df8407ffec0272fd6e5d055e6d0ac8a4de39774415287f993abe2c` |

开工探针（硬门禁）：`git hash-object -w` 通过（`5478d39e…`）；新 scratch 目录真实写文件通过。两次均无 Disk quota exceeded / EPERM。

## 缺陷清单（本轮新发现）

### D9 — P7 金句第 6 句非逐字引用（轻微内容缺陷）

- **位置**：P7「LES PHRASES DE LA SEMAINE」第 6 句（Q102 所注金句）+ Q102 题干；栏目标题注明「全部出自本期文章」。
- **问题**：金句印为 « Mercredi 18 novembre, seize films sortent **au cinéma** en France. »（page 5），Q102 题干亦为「Mercredi, seize films ___ (sortir) **au cinéma**.」；但 P5 原文是「Mercredi 18 novembre, seize films sortent **dans les salles de cinéma** en France.」——「au cinéma」为缩写改写，非原文逐字。
- **核实方法**：8 条金句逐条机械比对（去标点/空白归一化后在 P1–P6 全刊文本中检索）：Q97/Q98/Q99/Q100/Q101/Q103/Q104 均为 VERBATIM，唯 Q102 为 NOT-VERBATIM；P5 原文行已逐字定位。工具箱三句随身句（A2 博若莱句、B1 ADEME 句、B2 预算句）及 A2/B1/B2「LA PHRASE EXEMPLE」三句亦逐条核实为逐字。
- **为什么是缺陷**：引文加 « » 并标注 (page 5)，读者翻到 P5 找不到这句话；第一、二轮笔记称「金句 8/8 逐字出自本期正文」，该结论失实（实为 7/8）。SOP §4 要求金句摘自本期自己的文章——出处无误（同一句），但逐字性破了。
- **轻重**：轻微。意思未变（au cinéma = dans les salles de cinéma），出处同一句，不涉事实与答案；键 `sortent` 不受影响。
- **修法建议**：把金句与 Q102 题干一并改回 P5 原文措辞——金句改为 « Mercredi 18 novembre, seize films sortent dans les salles de cinéma en France. »；Q102 题干改为「Mercredi, seize films ___ (sortir) dans les salles de cinéma.」；键 `sortent` 不动。其余 7 条金句不动。改后按 SOP §8 重渲染并从头再做一轮全量校对。

## D7/D8/D3/KIT 逐项独立验证（全部通过）

### D7 ✓（自写几何分类脚本 `verify-d7d3d8.py`，方法与返修脚本无关）

XML 解析 SVG，收集 `fill="#f0eee5"` 浅底框，逐 `<text>` 元素按 (x,y) 是否落入框内分类为 body/框内，只在 body 文本里整词计数（屈折/复数计入，沿用 D3 口径）。base64 在 `<image>` 属性内，不在 `<text>` 元素内，天然排除。

- P1 `vainqueur`：body 1 次（x=88, y=940：« Nanterre. Le vainqueur remporte son premier titre à Paris »，头条正文主栏），框内 1 次（译注本身）。PASS。
- P4 `choc`：body 计 2 次，其中 1 次为真身（x=88, y=937：« Un choc remporté en deux sets »），另 1 次为中栏译注行（x=989, y=290：« 译注｜un choc 强强对决 … »）——该行在任何浅底框之外（上方中栏译注行，框自 y=520 起），纯几何分类误判为 body；剔除该行后 body 仍为 1 次真身。PASS（已按最严口径复核）。
- P6 `navette`：body 1 次（x=1440, y=2131：« navette parlementaire, les allers-retours… »，APRÈS LE VOTE 栏，无浅底背景，属正文）；`paritaire`：body 1 次（x=1440, y=2238：« commission mixte paritaire — sept députés et sept sénateurs »）。PASS。
- 结论：4 词各在同版正文出现，D7 修完。第二轮复校方法（字符串剔除）与本轮几何分类法结论一致；b22b2bf1 的 grep 观察未被采信为结论，以上为独立验证。

### D3 ✓（同脚本，13/13）

P3 `bouteille`（« mettre leur vin en bouteille »）、`raisin`（« couper le raisin »）、`vigne`（仅复数 « dans les vignes »，屈折计入）；P4 `tennis`（« tournoi de tennis »）、`adversaire`（« son adversaire, Ben Shelton »）；P5 `salle`（仅复数 « dans les salles de cinéma »）、`public`（« le public a l'embarras du choix »，另 1 次为图片署名 « domaine public »）、`réalisateur`、`scénario`、`écran`、`acteur`、`actrice`、`séance` 均在同版正文命中 1 次以上。**13/13 PASS**。

### D8 ✓

- `expl.py`：`gp4` = 「语法点｜se terminer en beauté：圆满收尾。」、`n_gp4` = 「se terminer en beauté 圆满收尾」。
- P7/P8 SVG：`<text>` 元素内 `lieu` 各为 0 处；全文件原始文本内 `lieu` 亦为 0 处（本轮 build 已无 base64 误命中；b22b2bf1 的旧观察未被采信，以上为独立验证）。
- P7 卡面语法点行、P8 答案区「100. beauté（se terminer en beauté 圆满收尾）」均目视确认；Q100 题干「La semaine se termine en ___ (beau).」与键 `beauté` 不动；金句逐字出自 P2 正文（机械比对 VERBATIM）。P1「ont lieu」/「aura lieu」/P4「a eu lieu」等为正文正确用法，不在 D8 范围内，未动。

### KIT 文字订正 ✓

- (a) §7「未改动」段与 §九第 4 条：已改为「实测 32px=24pt（规范次级标题 22.5–24pt，恰为上限，合规；KIT 旧称 38px=28.5pt 有误，2026-11-11 第二轮返修按 SVG 实测订正——8 个 SVG 中 `font-size="38"` 为 0 处）」。本轮独立实测：`font-size="38"` 全刊 0 处；P2–P6 各 2 处 `font-size="32"`（文章标题），32px=24pt 合规。
- (b) §九第 1 条与 §二.4：已改为 F-MAIL 规则准确表述——「投稿只认用户直接发来的；用户未直接发来投稿即无来信，**不查邮箱、不核实邮箱状态**」；「入仓前不核查邮箱」。P7 读者园地标注明确的编辑部示例 + 法文/中文双语说明（截至付印未收到 VOL.4 投稿，VOL.5 兑现承诺），无编造来信。

## 150 题逐题验算

- `p8.py extract --json` 与 `final-fr-p8.json` 逐项相同：注记集 121/150（parse: joined）、键 150 条、total 150，零差异。
- 键 vs `.text.md` RÉPONSES 区（自写切分脚本 `verify-keys3b.py`/`verify-keys3c.log`，按 "N. " 切分、剥离注记与版分隔符）：**150/150 一致，0 不符**（Q150 按既定口径：p8 抽出「开放题」，.text.md 为全句，前缀一致）。
- 逐题对照题干/原文/图表独立验算（P1–P8 全 150 题，含 P8 Q109–150 逐题重算）：**全部 150 键正确，每题仅一解**。重点复核：
  - Q2/Q3（新题干「C'est ___ que…」）：仅容 mercredi/jeudi，`le` 无法填入（« C'est le que… » 不合语法）；Q4 premier、Q5 12,7、Q6 22 均与正文一致。
  - Q84：键 B（26 nov.），可从 P6 日程图「Fin du délai de 50 jours (art. 47-1)」推出。
  - Q100：beauté，金句逐字出自 P2。
  - Q102：键 sortent 不变（见 D9；题干措辞待改，键不受影响）。
  - Q109–116 完形：lundi/Beaujeu/résultats/goûté/propose/aimé/jouent/écrit 逐项唯一（Q112 goûté：« un régal » 为品尝语境，acheté 不合该语境；Q113 主语单数排除 proposent，se tient 不接宾语；Q114 avoir + 过去分词无配合）。
  - Q117–129 单选/阅读：逐项与题面、原文、日程图一致，唯一解。
  - Q130–134：futur proche / si + imparfait → 条件式 / passé composé / Selon moi / 虚拟式 examine，全部唯一。
  - Q135–139 翻译：与 RÉPONSES 区逐句一致。
  - Q140–144 配对：a/b/c/d/e 与 P8 选项顺序一致；Q145–149 对话：des billets/deux/quelle heure/devant/film 唯一。
  - Q150 写作：范文 96 词（80–100 内），与 RÉPONSES 区「开放题」口径一致。
- 题号连续性：各页题号标记并集覆盖 1–149（150 为写作题，无数字标记，属正常）；分版 10/15/18/18/17/18/12/42，分级 A2 53/B1 75/B2 22，与 KIT 登记表一致。

## 机械门（本轮全部重跑）

- `occlusion_audit.py`：自检 OK（6 类阳性对照触发、干净对照静默），**0 flags**。
- `p8.py extract --total 150`：注记集 **121/150**（parse: joined），与 `final-fr-p8.json` 逐项相同。`p8.py compare`：**CLEAN**，121/121，missing=[] extra_count=0 keydiff=[]。
- `check_mcq.py`（`scratch-fr/check_mcq.py`）：45 题体、1,448 渲染行，**DEFECTS: 0，UNLOCATED: 0**。
- `freeze.py baseline`（`--build production/2026-w47/core-fr --core-svg …/svg --out scratch-proof-fr3/freeze3`）：**8/8 byte-identical**（p1 `6aad8b4bcdfb`、p2 `5709e000bbd7`、p3 `7828cfe33118`、p4 `37cf3412c3f8`、p5 `fff2a8d3d7ac`、p6 `7af7cf3c240f`、p7 `629cfe063bbd`、p8 `ce072a017cd4`——与 fix2 哈希逐项相同）；core integrity：交付 SVG 未被重建改动。
- 文字层：`pdftotext` 印刷版/网页版各 **46,695 字节**、7,292 词，**逐字节一致**。
- P8 最小字号（PyMuPDF）：469 spans，最小 **11.62pt**（214 spans）≥ 9.75pt。
- 徽章：SVG `rx="2.7"` 矩形计数 P1 10、P2 12、P3 18、P4 15、P5 14、P6 15、P7 12、P8 38，**总计 134**；分级 A2 `#5c6e30` 50、B1 `#46581f` 65、B2 `#37402f` 19 = 150−16 配对共享题。
- 字体（`<text>` 元素统计）：Newsreader 935 / Noto Sans CJK SC 660 / Noto Serif CJK SC 116 / UnifrakturMaguntia 1 / DejaVu Sans 4；与 fix2 变化一致（P1 102→103、P6 123→131）；Noto Serif CJK SC 跨度内拉丁词 0。

## §1.1 逐项实测

| 项 | 实测 | 结论 |
|---|---|---|
| 纸色 #fbfaf6 | 8/8 有；旧纸 #f7f1e2 0 | ✓ |
| 无金色/近黑 | #b49a4a/#b3a06a 0；#2a2419/#2c2822 0 | ✓ |
| 无双线外框 | stroke-width≥2 元素：橄榄绿 #46581f 分隔线（2px=1.5pt，规范内）+ 刊头蛾装饰（P1 两组 #34483A stroke-width=7 的 `<g>`、P3 蛾 path）；无边缘矩形 | ✓ |
| 徽章三色 | A2 #5c6e30、B1 #46581f、B2 #37402f，白字 rx=2.7 | ✓（数量见上） |
| 分隔符全角空格 | 「·」8 SVG + .text.md + ABSTRACT 均为 0；「　」P1 35/P2 33/P3 19/P4 29/P5 23/P6 24/P7 15/P8 182、.text.md 390、ABSTRACT 0 | ✓ |
| 刊头 196px=147pt | P1 `Le Lucerna` UnifrakturMaguntia 196px 居中 | ✓ |
| 头条 53px=39.75pt | 低于 40pt 下限 0.25pt，像素取整所致；沿用第一/二轮可接受裁定 | 观察（已裁定可接受） |
| 无首字下沉 | P1 头条首段无放大首字；沿用第一轮/de 裁定 | 观察（已裁定可接受） |
| P2–P6 文章标题 | SVG 实测 32px=24pt，恰为次级标题范围上限；`font-size="38"` 全刊 0 处 | ✓ |
| VOL.4/VOL.5 | .text.md VOL.4 ×4、VOL.5 ×9；9 处 VOL.5 已在第二轮逐处核实均为合法下期指称，本轮通读未见新增误印 | ✓ |

## 全文精读（.text.md 1–1087 行逐行 + 8 版卡面）

- P1：新句「Le vainqueur remporte son premier titre à Paris, le neuvième en Masters 1000.」在位，重排干净；事实与快讯栏一致（巴黎首冠、第 9 个大师赛冠军）；目录、议程、快讯、闪电问答、图注、页脚干净。
- P2：Q18 已单行；ET VOUS 框注记在框内；日期表与 Q11–Q14 一致；「seize nouveaux films」与 P5「16 部」一致（O2 计数未证实，维持观察，KIT 已注口径）。
- P3：bouteille/raisin/vignes 已进正文；词表 10 词可见；Q36/Q37 填空线孤行仍在（O7，裁定不修）；Q26（1951 年获准提前售酒）与 Q42（采收自 8 月 13 日）与正文一致。
- P4：新句「Un choc remporté en deux sets, sans tie-break dans le deuxième.」在位；Q44–48 选项整组完整；「LES CHIFFRES DU SPORT」框中文注记「。」孤行仍在（O8，裁定不修）；O3（« la course, arrêtée lundi 9 novembre » 措辞略不精确）维持观察。
- P5：D1 已改（vingt-quatre ans / réalisateur / scénario / grand écran / salles / le public / acteur / actrice / séance）；电影词表 8 词可见；Méliès 图与图注干净；16 部 vs 点名 6 部表述自洽。
- P6：日程图 7 行，26 Nov 行位置正确；Q79–84 选项完整，Q84 可答；新增「APRÈS LE VOTE」栏在右栏末，距页脚有余量；navette/CMP 机制表述（将来时/条件式，不预断本期法案后续）与《宪法》第 45 条一致。
- P7：gp4 已为「se terminer en beauté：圆满收尾。」；8 金句、诊所、园地、预告、Doré 图均在；读者园地标注明确；**唯 Q102 金句非逐字（见 D9）**。
- P8：完形 8 枚徽章、对白条 5 枚、写作 B1 1 枚均画出；答案区 1–150 齐全；Hiroshige 图已放置；页脚干净；Q100 注「100. beauté（se terminer en beauté 圆满收尾）」在位；Q130 填空线孤行仍在（O6，裁定不修）。
- 总体：8 版均无溢出、重叠、压页脚、豆腐块。

## 留待观察（非缺陷，沿用既往裁定）

- O1（第一轮）：五组配对题顺序一致，答案必然 a/b/c/d 顺序对应；SOP 未要求打乱，维持观察。
- O2（第一轮）：「16 部新片」计数未证实亦无法证伪；KIT 已补口径注记，维持观察。
- O3（第一轮）：P4「la course, arrêtée lundi 9 novembre」措辞略不精确，非事实错误；维持观察。
- O4：头条 39.75pt、无首字下沉（均已裁定可接受）。
- O5（已修）：P2 Q18、P7 gp5 本轮确认已单行。
- O6–O8：Q130、P3 Q36/Q37、P4 体育数字框注记的孤行填空线/标点（已裁定观察，理由同前：SOP §1.1 无相关规则，内容完整、无溢出）。
- D4：中文数字带空格按全周统一口径不列缺陷、不改。
- P7 B1「LE PASSÉ COMPOSÉ, ENCORE」与 A2 同用 Alcaraz 例句：栏目标题即标明「ENCORE」（螺旋复现），属有意设计，不列缺陷。
- Q112 干扰项 acheté：« on a goûté le vin primeur, un régal ! » 中 « un régal » 为品尝语境，goûté 为唯一合意解；acheté 不合该语境。已复核，可接受。

## 工作树状态

本轮只读不改：未跑 insert.py / lint --write / git push / git add / reset / stash；未提交；未碰 W43/W45/W46、其他目标语、tools。`git status` 中 `tools/freeze.py`、`tools/p8.py` 的修改为返修前已有状态（FIX-LOG-fr2 已记），非本轮所改；`production/2026-w47/core-fr/` 8 个 SVG 的 SHA-256 与 fix2 记录逐项相同，未被本轮 freeze 重建改动。

## 工作文件

- 本笔记：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr3/PROOF-NOTE.md`
- 门禁日志：同目录 `GATE-LOG.md`
- 自写脚本与输出：`verify-d7d3d8.py` / `verify-d7d3d8.log`、`verify-keys3.py` / `verify-keys3b.py` / `verify-keys3b.log` / `verify-keys3c.log`、`occlusion3.log` / `occlusion3.json`、`p8-extract3.log` / `p8-3.json` / `p8-compare3.log`、`check-mcq3.log`、`freeze3.log` / `freeze3.json` / `freeze3/`、`print3.txt` / `web3.txt`、`p8-font3.log`、`section11-3.log`
