# PROOF-NOTE-fr4 — W47 法文核心版第四轮独立复校（叶子）

- 版：2026-w47-fr-zh-cn（目标 fr × 读者简体中文），VOL.4，刊期 2026-11-16..22
- 校对员：叶子（第四轮独立复校，与 builder、各轮返修 builder、第一至三轮校对员均不同；只读不改）
- 日期：2026-11-11（EST）
- 结论：**(a) 零问题**。D9 逐项回归全部通过；150 题逐题验算全对；D7/D8/D3/KIT 全部独立实测通过；机械门全套重跑通过；§1.1 逐项重测通过；8 版卡面目视（全新渲染）+ 网页 P1/P8 通过。本轮未发现新缺陷。是否定稿由协调员定。
- 依据：SOP.md §8/§1.1 全文、`AGENTS.md`、core-fr/WEEKLY-KIT.md 全文、`PROOF-NOTE.md`（第三轮复校）全文、`FIX-LOG-fr3.md`（第三轮返修）全文已读。
- 工作记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr4/`（本笔记 + GATE-LOG.md + 自写验证脚本与全部工具输出）。注：任务简报的 `hidden_files/w47/` 按 fr1–3 实际落点取 goals 侧 hidden_files；`~/workspace/weekly-git/hidden_files/w47/` 下只有 ja 的两个目录，无 fr 材料。

## 已核实的文件身份（与任务简报逐项一致）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4.pdf`（印刷） | 30,446,982 B，8 页 1462.5×2025pt | `db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7` |
| `La-Lucerna-VOL4-web.pdf`（网页） | 2,205,749 B，8 页 | `26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823` |
| `2026-w47-fr-zh-cn.text.md` | 46,477 B | `2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e` |

开工探针（硬门禁）：`git hash-object -w` 通过（`da0c4eb8…`）；新 scratch 目录真实写文件通过（`.probe`）。两次均无 Disk quota exceeded / EPERM。

## D9 逐项回归核实（自写脚本 `verify-fr4.py`，独立查 P5 原文，不采信返修记录断言）

- P5 原文（`content56.py:18` 与 P5 SVG 双重确认）：「Mercredi 18 novembre, seize films sortent **dans les salles de cinéma** en France.」——原文本在。
- P7 金句第 6 句与 Q102 题干：源码 `content7.py:83–84`、P7 SVG `<text>` 拼接、印刷版/网页版文字层、`.text.md` 四处均为「dans les salles de cinéma」；P7 SVG 内该措辞 2 处（金句 + 题干），`sortent au cinéma` 0 处，`au cinéma` 0 处。**已改回 P5 原文措辞 ✓**
- 键 `sortent` 不动：`final-fr-p8.json` Q102 = `sortent`；RÉPONSES「102. sortent（sortir 上映）」✓
- 金句 8 条逐条实测（`content7.py` 的 8 条金句原文，去标点/空白归一化后在 P1–P6 SVG 文本中检索，并在所注页码内复核）：Q97（p1）、Q98（p3）、Q99（p2）、Q100（p2）、Q101（p5）、Q102（p5）、Q103（p6）、Q104（p1）**8/8 VERBATIM，且均在所注页码内命中**。第一、二轮「8/8 逐字」失实（实为 7/8）的旧账，本轮修后为真 8/8。
- 其余页确未被改动：8 个 SVG 的 SHA-256 前 12 位与 fix2 基线（FIX-LOG-fr3 记载）逐项比对——p1 `6aad8b4bcdfb`、p2 `5709e000bbd7`、p3 `7828cfe33118`、p4 `37cf3412c3f8`、p5 `fff2a8d3d7ac`、p6 `7af7cf3c240f`、p8 `ce072a017cd4` 全部相同；**仅 p7 `629cfe063bbd`→`75237d672f20`**。✓

## D7/D8/D3/KIT 逐项独立验证（全部通过）

### D7 ✓（自写几何分类脚本，与返修脚本无关）
XML 解析 SVG，收集 `fill="#f0eee5"` 浅底框，逐 `<text>` 元素按 (x,y) 是否落入框内分类为 body/框内，含「译注｜」的行一律作注记剔除：
- P1 `vainqueur`：body 1 次（« Le vainqueur remporte son premier titre à Paris »，头条正文）。PASS。
- P4 `choc`：body 1 次（« Un choc remporté en deux sets »）。PASS。
- P6 `navette`：body 1 次（« navette parlementaire, les allers-retours… »，APRÈS LE VOTE 栏）；`paritaire`：body 1 次（« commission mixte paritaire — sept députés et sept sénateurs »）。PASS。
- 结论：4 词各在同版正文出现 1 次真身，D7 修完。

### D3 ✓（同脚本，13/13）
P3 `bouteille`（« mettre leur vin en bouteille »）、`raisin`（« couper le raisin »）、`vigne`（复数 « dans les vignes »，屈折计入）；P4 `tennis`（« tournoi de tennis »）、`adversaire`（« son adversaire, Ben Shelton »）；P5 `salle`（« dans les salles de cinéma »）、`écran`（« grand écran »）、`acteur`、`actrice`、`réalisateur`、`scénario`、`séance`、`public`（« le public a l'embarras du choix »，另 1 次为图片署名 « domaine public »，真身仍在）均在同版正文命中。**13/13 PASS**。

### D8 ✓
- `expl.py`：`gp4` = 「语法点｜se terminer en beauté：圆满收尾。」、`n_gp4` = 「se terminer en beauté 圆满收尾」。
- P7/P8 SVG：`<text>` 元素内 `lieu` 各为 0 处；全文件原始文本内 `lieu` 亦为 0 处。
- P7 卡面语法点行、P8 答案区「100. beauté（se terminer en beauté 圆满收尾）」均目视确认；Q100 题干与键 `beauté` 不动。

### KIT 文字订正 ✓
- (a) §7「未改动」段与 §九第 4 条：已为「实测 32px=24pt（规范次级标题 22.5–24pt，恰为上限，合规；KIT 旧称 38px=28.5pt 有误，2026-11-11 第二轮返修按 SVG 实测订正——8 个 SVG 中 `font-size="38"` 为 0 处）」。本轮独立实测：`font-size="38"` 全刊 0 处；P2–P6 各 2 处 `font-size="32"`（文章标题），32px=24pt 合规。KIT 内「28.5pt」仅出现于两处历史说明（「旧称…有误」「已订正 KIT 旧称 28.5pt」），无一处仍作现行主张。
- (b) §九第 1 条与 §二.4：已为 F-MAIL 规则准确表述——「投稿只认用户直接发来的；用户未直接发来投稿即无来信，**不查邮箱、不核实邮箱状态**」；「入仓前不核查邮箱」。P7 读者园地标注明确的编辑部示例 + 法文/中文双语说明（截至付印未收到 VOL.4 投稿，VOL.5 兑现承诺），无编造来信。

## 150 题逐题验算

- 键 vs `.text.md` RÉPONSES 区（自写切分脚本 `verify-keys-fr4.py`，按 `N. ` 连接行切分、剥离注记与版分隔符）：**150/150 一致，0 不符**（Q150 按既定口径：p8 抽出「开放题」，.text.md 为「150. 开放题 — 要点见写作框…」，前缀一致）。
- 分版题量：RÉPONSES 区按「— 第 N 版 —」分段机械计数：P1 10（1–10）· P2 15（11–25）· P3 18（26–43）· P4 18（44–61）· P5 17（62–78）· P6 18（79–96）· P7 12（97–108）· P8 42（109–150），与 KIT 登记一致；题号连续无缺重。
- 分级：徽章颜色实测 A2 50 / B1 65 / B2 19（见下），5 组配对共享徽章（Q22–25 A2、Q49–52 B1、Q73–76 B1、Q85–88 B2、Q140–144 B1）各组题数减 1 枚徽章折算：A2 50+3=**53**、B1 65+3+3+4=**75**、B2 19+3=**22**，合计 150，与 KIT 登记一致。
- 逐题对照题干/原文/图表独立验算（.text.md 全文精读 1–1087 行，P1–P8 全 150 题）：**全部 150 键正确，每题仅一解**。重点复核：
  - Q2/Q3（「C'est ___ que…」）：仅容 mercredi/jeudi，`le` 无法填入；Q4 premier、Q5 12,7、Q6 22 均与正文一致。
  - Q84：键 B（26 nov.），可从 P6 日程图「Fin du délai de 50 jours (art. 47-1)」推出。
  - Q100：beauté，金句逐字出自 P2（本轮 8/8 复核在内）。
  - Q102：键 sortent 不变；题干已改回 P5 原文措辞（见 D9）。
  - Q109–116 完形：lundi/Beaujeu/résultats/goûté/propose/aimé/jouent/écrit 逐项唯一（Q112 goûté：« un régal » 为品尝语境，acheté 不合该语境；Q113 主语单数排除 proposent，se tient 不接宾语；Q114 avoir + 过去分词、无前置宾语故无配合）。
  - Q117–129 单选/阅读：逐项与题面、原文、日程图一致，唯一解。Q120 irais（si + imparfait → 条件式）。
  - Q130–134：futur proche / si + imparfait → 条件式 / passé composé / Selon moi / 虚拟式 examine，全部唯一。
  - Q135–139 翻译：与 RÉPONSES 区逐句一致（regarder une finale / plus vite que son frère / depuis lundi / préparer nos affaires / ne…pas encore）。
  - Q140–144 配对：a/b/c/d/e 与 P8 选项顺序一致；Q145–149 对话：des billets/deux/quelle heure/devant/film 唯一。
  - Q150 写作：范文 96 词（空白切分，80–100 内），与 RÉPONSES 区「开放题」口径一致。
- 日期/星期：`date -d` 核验 2026-11-04（周三）、08（周日）、09（周一）、11（周三）、12（周四）、15（周日）、16（周一）、17（周二）、18（周三）、19（周四）、20（周五）、21（周六）、22（周日）、23（周一）、26（周四）、27（周五）、12-09（周三），与全刊所写星期全部一致。

## 机械门（本轮全部重跑）

| 门 | 本轮实测 | 结论 |
|---|---|---|
| 印刷/网页/`.text.md` 身份 | 尺寸与 SHA-256 与简报逐项一致（见首表） | ✓ |
| SVG 冻结差分 | `freeze.py baseline`（**`tools/venv/bin/python`，即构建解释器**：Python 3.12.3 / Pillow 13.0.0；系统 python3 为 Pillow 10.2.0，未用）从核心目录运行 `--build . --core-svg svg`，**8/8 byte-identical**，`ok: 8`；p7 `75237d672f20f44b`，其余 7 页与 fix2 逐项相同；core integrity：交付 SVG 未被重建改动 | ✓ |
| 几何遮挡审计 | `occlusion_audit.py` 自检 OK（6 类阳性对照触发、干净对照静默），**0 flags** | ✓ |
| P8 注记/键 | `p8.py extract --total 150`：注记集 **121/150**（parse: joined）；与 `final-fr-p8.json` 逐项相同——keys 150 条、noted_set 121 条全同（原始 JSON 整体不等仅因 `p8` 字段为绝对路径 vs 相对路径的字符串差异，内容无差）；`p8.py compare`：**CLEAN**，121/121，missing=[] extra_count=0 keydiff=[] | ✓ |
| MCQ 折行 | `check_mcq.py`：45 题体、1,449 渲染行，**DEFECTS: 0，UNLOCATED: 0** | ✓ |
| 文字层双版一致 | `pdftotext -layout` 印刷版/网页版各 **103,001 字节**、**逐字节一致** | ✓ |
| P8 最小字号 | PyMuPDF（tools/venv）：P8 469 spans，最小 **11.62pt** ≥ 9.75pt | ✓ |
| 徽章 | SVG `rx="2.7"` 矩形计数 P1 10、P2 12、P3 18、P4 15、P5 14、P6 15、P7 12、P8 38，**总计 134**；分级 A2 `#5c6e30` 50、B1 `#46581f` 65、B2 `#37402f` 19 | ✓ |
| 字体（§1.1） | `<text>` 元素统计与 fix3 一致；Noto Serif CJK SC 跨度内拉丁词 0（沿用第三轮方法复核） | ✓ |

## §1.1 逐项实测

| 项 | 实测 | 结论 |
|---|---|---|
| 纸色 #fbfaf6 | 8/8 有；旧纸 #f7f1e2 0 | ✓ |
| 无金色/近黑 | #b49a4a 0；#2a2419/#2c2822 0 | ✓ |
| 无双线外框 | stroke-width≥2 元素仅规范内橄榄绿分隔线与刊头蛾装饰；无边缘矩形 | ✓ |
| 徽章三色 | A2 #5c6e30、B1 #46581f、B2 #37402f，白字 rx=2.7 | ✓（数量见上） |
| 分隔符全角空格 | 「·」8 SVG + .text.md + ABSTRACT 均为 0；「　」P1 35/P2 33/P3 19/P4 29/P5 23/P6 24/P7 15/P8 182、.text.md 390、ABSTRACT 0 | ✓ |
| 刊头 196px=147pt | P1 `Le Lucerna` UnifrakturMaguntia 196px 居中 | ✓ |
| 头条 53px=39.75pt | 低于 40pt 下限 0.25pt，像素取整所致；沿用第一/二轮可接受裁定 | 观察（已裁定可接受） |
| 无首字下沉 | P1 头条首段无放大首字；沿用第一轮/de 裁定 | 观察（已裁定可接受） |
| P2–P6 文章标题 | SVG 实测 32px=24pt，恰为次级标题范围上限；`font-size="38"` 全刊 0 处 | ✓ |
| VOL.4/VOL.5 | .text.md VOL.4 两处（刊头、副题）为本期；VOL.5 共 9 处（L245、L497、L537、L939、L941、L943、L957、L1043、L1083）已逐行核实，均为合法下期指称（赛果/投稿/预告），无误印；SVG 各页 VOL.5 均为预告/承诺语境 | ✓ |

## 禁词扫描（本轮自定口径，SVG `<text>` + `.text.md` 全文）

扫描表：内部流程词 `SOP`、`proofread`、`校对`、`geometry`、`occlusion`、`lint`、`TODO`、`FIXME`、`XXX`、`占位`、`待写`、`lorem`、`cover`；红线政治词 `乌克兰`、`俄乌`、`加沙`、`以色列`、`台海`、`战争`；周次标记 `2026-w47`、`2026-W47`；分隔符 `·`。**全部 0 处**。✓

## 全文精读与 8 版卡面目视（从印刷 PDF 重新渲染，不采信旧图）

- 渲染：`pdftoppm -r 100` 自 `La-Lucerna-VOL4.pdf` 重渲 8 页 + 自网页版重渲 P1/P8，存 `render4/`；逐版目视。
- P1：刊头/导读条/头条两栏/译注框/LES DATES/À VOUS Q1–6/议程/目录/词/Atget 图/三句话/快讯/闪电问答 Q7–10/页脚均干净，无溢出、重叠、压页脚。
- P2：Q18 已单行；ET VOUS 框注记在框内（放大裁图确认「寄」字清晰，注记行在框底之上）；日期表与 Q11–14 一致；「seize nouveaux films」与 P5「16 部」一致（O2 维持观察）。
- P3：bouteille/raisin/vignes 已进正文；词表 10 词可见；Moreau 图与图注干净；Q36/Q37 填空线孤行仍在（O7，裁定不修，放大裁图确认状态与既往记录一致）。
- P4：新句「Un choc remporté en deux sets…」在位；Q44–48 选项整组完整；「LES CHIFFRES DU SPORT」框中文注记「。」孤行仍在（O8，裁定不修，放大裁图确认）；O3（« la course, arrêtée lundi 9 novembre »）维持观察。
- P5：D9 出处句「seize films sortent dans les salles de cinéma en France.」在位；电影词表 8 词可见；Méliès 图与图注干净；16 部 vs 点名 6 部表述自洽。
- P6：日程图 7 行（23 oct. / 4 nov. / 9–17 nov. / 18 nov. / 20 nov. / **26 nov.** / 9 déc.），Q79–84 选项完整，Q84 可答；「APRÈS LE VOTE」栏在右栏末，距页脚有余量；LE DÉBAT 中文注记经放大裁图确认「。」与「（已定）」在同一行，**无新增孤行**（低分辨率整版图下的疑似孤行属误读，已纠正）。
- P7：**D9 两处已改到位**——金句第 6 句 « Mercredi 18 novembre, seize films sortent dans les salles de cinéma en France. » (page 5) 三行排布干净；Q102「Mercredi, seize films ___ (sortir) dans les salles de cinéma.」两行排布干净；金句流未压诊所栏；gp4 已为「se terminer en beauté：圆满收尾。」；8 金句、诊所（Q105–108）、园地、预告、Doré 图均在；页脚干净。
- P8：完形 8 枚徽章、对白条 5 枚、写作 B1 1 枚均画出；答案区 1–150 齐全（含「102. sortent（sortir 上映）」）；Hiroshige 图已放置；页脚干净；Q130 填空线孤行仍在（O6，裁定不修）。
- 网页 P1/P8：与印刷版同版面逐项一致，无缺图、无豆腐块。
- 总体：8 版均无溢出、重叠、压页脚、豆腐块。

## 留待观察（非缺陷，沿用既往裁定）

- O1：五组配对题顺序一致，答案必然 a/b/c/d（140–144 为 a/b/c/d/e）顺序对应；SOP 未要求打乱，维持观察。
- O2：「16 部新片」计数未证实亦无法证伪；KIT 已补口径注记，维持观察。
- O3：P4「la course, arrêtée lundi 9 novembre」措辞略不精确，非事实错误；维持观察。
- O4：头条 39.75pt、无首字下沉（均已裁定可接受）。
- O6–O8：Q130、P3 Q36/Q37、P4 体育数字框注记的孤行填空线/标点（已裁定观察，理由同前：SOP §1.1 无相关规则，内容完整、无溢出）。
- D4：中文数字带空格按全周统一口径不列缺陷、不改。
- P7 B1「LE PASSÉ COMPOSÉ, ENCORE」与 A2 同用 Alcaraz 例句：栏目标题即标明「ENCORE」（螺旋复现），属有意设计，不列缺陷。
- Q112 干扰项 acheté：« on a goûté le vin primeur, un régal ! » 中 « un régal » 为品尝语境，goûté 为唯一合意解；acheté 不合该语境。已复核，可接受。

## 工作树状态

本轮只读不改：未跑 insert.py / lint --write / git push / git add / reset / stash；未提交；未碰 W43–W46、其他目标语、tools/。`git status` 中 `tools/freeze.py`、`tools/p8.py`、`tools/occlusion_audit.py` 的修改均为本轮开工前已有状态（mtime 分别为 2026-11-10 22:59、21:37 与 2026-11-11 05:01 UTC，均早于本轮开工 05:29 UTC），非本轮所改；`issues/2026-w43/` 的修改亦为开工前已有状态，非本轮所改。freeze 重建复核确认交付的 8 个 SVG 未被本轮改动（8 文件重哈希一致）。

## 工作文件

- 本笔记：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr4/PROOF-NOTE.md`
- 门禁日志：同目录 `GATE-LOG.md`
- 自写脚本与输出：`verify-fr4.py` / `verify-fr4.log`、`verify-keys-fr4.py` / `verify-keys-fr4.log`、`occlusion4.log` / `occlusion4.json`、`p8-extract4.log` / `p8-4.json` / `p8-compare4.log` / `p8-compare4.json`、`check-mcq4.log`、`freeze4.log` / `freeze4.json` / `freeze4/`、`print4.txt` / `web4.txt`、`render4/`（印刷版 8 页 + 网页 P1/P8 全新渲染 + 放大裁图 5 张）
