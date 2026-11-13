# WEEKLY-KIT — Le Lucerna · 法语周报 VOL.4 · 核心版（简体中文讲解）

- 目标语：法语（fr）；读者母语：简体中文（zh-cn）；期号 VOL.4，总第 4 期。
- 刊期：2026 年 11 月 16 日（周一）至 11 月 22 日（周日）；slug 周 `2026-w47`；frontmatter 周 `2026-W47`；weekStart `2026-11-16`，weekEnd `2026-11-22`。截稿：2026 年 11 月 10 日。
- 刊名：`Le Lucerna`。版式：8 版，1950×2700，4 栏，页脚配对标识每版可见，P1 配对徽章可见。
- 练习：150 道（P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42），分级 A2 53 · B1 75 · B2 22。级别徽章 134 枚（P1 10 · P2 12 · P3 18 · P4 15 · P5 14 · P6 15 · P7 12 · P8 38；150 题 − 16 道配对共享题）。P8 答案全部由登记表生成；印出注记 121/150（`tools/p8.py extract` 实测，见 §7）。
- 词汇表：6 组（葡萄酒、网球、电影、预算、日期、金句点），见 `expl.py` 各 `mots_*` / `g*` 词表。范文《Mon dimanche 22 novembre》96 词（空白切分），在 80–100 词要求内。
- 金句 8 句，全部逐字出自本期 P1–P6 正文（脚本校验 8/8，见 §7；2026-11-11 第三轮返修前第三轮复校实测为 7/8——Q102 金句非逐字，见 §八第 6 轮；D9 修后自写脚本复核 8/8；fix4 返修后重测仍 8/8，见 §八第 7 轮）。
- P1 主头条：导读条 `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI`（37 非空白字符）与显示标题 `Alcaraz, roi de Paris: le Sénat tranche mercredi`（41 非空白字符），均 ≤ `tools/cover.mjs` LIMITS.headline（other 类 56）。

## 一、头版与各版内容

- P1 头版：主标题《Alcaraz, roi de Paris: le Sénat tranche mercredi》；导语三段（阿尔卡拉斯巴黎夺冠、参议院周三社保预算投票、博若莱新酒周四零点上市）+ 议程表（16–22 日）+ 目录 + “本周三件大事” + “本周关键词（trancher）” + 预算三句话（11 月 4 日 458–0 否决）+ 快讯 + 闪电问答 4 题；Atget 巴黎街景图。
- P2 生活《Lundi 16 novembre: une semaine en trois temps》：一周三段时间（周一都灵继续 + 参议院审议、周三投票 + 电影上映、周四新酒 + 周日都灵决赛与法甲回归）；日期说法（16/17/18/19/20/21/22 日）+ 练习 15 题；Châtillon 博若莱城堡图。
- P3 文化《Le beaujolais nouveau a 75 ans》：新酒 75 周年（1951 年获准提前售酒、1985 年定为 11 月第三个周四、佳美唯一葡萄品种、博若莱与博若莱村庄两个产区、收获量同比少 22%、Sarmentelles 博热午夜开桶、里昂拖拉机送酒）+ 适度饮酒提示；练习 18 题；Moreau《收获》油画。
- P4 体育《Alcaraz gagne Paris, Turin commence》：巴黎大师赛决赛（阿尔卡拉斯 7-6(5), 7-5 胜谢尔顿，巴黎首冠、第 9 个大师赛冠军）+ 都灵年终总决赛（15–22 日，8 人，4 名首秀，菲尔斯为法国人，辛纳膝伤退赛）+ 法国队欧国联两战（12 日米兰对意大利、15 日波尔多对土耳其）+ 法甲第 11 轮（20–22 日）；练习 18 题。
- P5 青年《Mercredi 18 novembre: le cinéma, et la seconde main》：周三 16 部新片上映（《饥饿游戏》前传 2 小时 38 分、《Les Braves》、《Jupiter》、《Malika》、《Camembert》、《Fais-moi un signe》）+ 减废周（21–29 日，ADEME“最好的垃圾是不产生的垃圾”）；练习 17 题；Méliès《月球旅行记》1902 年图。
- P6 时事《Au Sénat, mercredi 18: le vote du budget de la Sécu》：社保预算参议院审议（9 日开议、9–17 日辩论、1200+ 修正案、赤字目标 12.7 亿欧元 vs 2026 年 21.8 亿、养老金指数化门槛 1260→1500 欧元提议）+ 本期自我更正（W46 曾预告的 11 月 3 日国民议会收入部分正式投票未发生：两度推迟后于 11 月 4 日晚举行，458–0 否决、全文一读落败）+ 日程图（23 Oct / 4 Nov / 9–17 Nov / 18 Nov / 20 Nov / **26 Nov（50 天期限 art. 47-1 到期）** / 9 Déc）；练习 18 题；2026-11-11 第二轮返修新增「APRÈS LE VOTE」小栏（投票后程序：两院往返审议 navette、意见不一致时 commission mixte paritaire 寻求共同文本）。
- P7 精讲：A2 未来最近时/复合过去时、B1 复合过去时/比较级、B2 `il est prévu que + 虚拟式`/`si + 条件式`；本周金句 8 句各配语法点与跟练；易错诊所 4 句；读者园地（编辑部示例《Mon dimanche 22 novembre》+ 双语说明：截至付印未收到投稿，VOL.5 将点评真实投稿）；VOL.5 预告（都灵决赛结果、法国队与法甲第 11 轮赛果、11 月 27 日黑色星期五、参议院投票结果、读者来信）；Doré《拉封丹寓言》插图。
- P8 综合评估：完形 8 + 单选 8 + 阅读 5 + 完成句子与转换 5 + 翻译 5 + 词汇配对 5 + 对话补全 5 + 写作 1（含范文），答案区按版分组；Hiroshige 红枫图。

## 二、兑现 W46 承诺（KIT 为准）

1. **巴黎大师赛结果**：已兑现。2026 年 11 月 8 日（周日）决赛，2 号种子阿尔卡拉斯 7-6(5), 7-5 胜 3 号种子谢尔顿（南泰尔），巴黎首冠、第 9 个大师赛 1000 冠军（ATP 官方 + 美联社，11 月 8–9 日）。P1 头版、P1 快讯、P4 正文、P7 金句与预告一致；W46 曾写“结果未出，见 VOL.5”已由本期结果取代，无虚构。
2. **预算投票结果**：已兑现并自我更正。W46 预告的国民议会 11 月 3 日收入部分正式投票未发生：投票先由 10 月 20 日推迟、11 月 3 日再度推迟，实际于 11 月 4 日（周三）晚举行，收入部分以 458–0（2 票弃权）被否决，全文一读落败，文本以政府原版送交参议院。P6 深读段与日程图均按此更正（“ce numéro corrige son propre calendrier”）。参议院社保预算正式投票约 11 月 18 日（周三）为单源日程口径，文中一律写作“est prévu”，以实际结果为准，VOL.5 报道结果。另：10 月 23 日社保预算收入部分 115–1 被否决已核实；参议院 11 月 20 日起审议国家预算，正式投票 12 月 9 日，70 天期限至 12 月 17 日午夜。
3. **博若莱新酒 11 月 19 日（周四）**：已兑现。第 75 届新酒之约，11 月 19 日 0 时上市，11 月第三个周四（1985 年起规则），佳美葡萄，仅博若莱与博若莱村庄两个产区（红与桃红）。P1、P2、P3、P5、P7、P8 均有呼应。
4. **真实来信**：未收到，沿用 W46 做法。截至 11 月 10 日付印，编辑部未收到 VOL.4 投稿（见 P7 法语说明 + 简体中文说明，标注明确的编辑部示例）。**F-MAIL 规则（2026-11-11 第二轮返修订正）**：投稿只认用户直接发来的；用户未直接发来投稿即无来信，**不查邮箱、不核实邮箱状态**。承诺顺延至 VOL.5。
5. **编号纠正**：W46 FR KIT 通篇写“VOL.5”是 off-by-one 笔误，W47 就是 VOL.4。本期版面、页脚、刊别、P7 预告、ABSTRACT、`.text.md` 一律印 VOL.4；VOL.5 指下一期（11 月 23–29 日刊期）。W46 正文本身 frontmatter vol 为 3（其 PDF 误印 VOL.4，见 SOP §9 `VOL_MISPRINTS`）。
6. **W45 曾预告的国民议会 11 月 3–6 日分任务投票未发生**：W46 已自我更正，本期不再复活；P6 只报已核实的 11 月 4 日投票结果。

## 三、事实来源（2026 年 11 月 10 日检索，截稿时状态）

- 巴黎大师赛决赛（8 日，阿尔卡拉斯 7-6(5), 7-5 胜谢尔顿，巴黎首冠、第 9 大师赛冠军；首盘挽救 6 个破发点、第二盘 6-5 破发）：ATP Tour 官方战报 + 美联社 2026-11-08/09。
- 国家预算 PLF 2027：国民议会 11 月 4 日晚收入部分 458–0（2 弃权）否决、全文一读落败（议会报道多源一致）；参议院自 11 月 20 日审议，正式投票 12 月 9 日，70 天期限至 12 月 17 日午夜（senat.fr 议程 + Public Sénat）。
- 社保预算 PLFSS 2027：10 月 23 日国民议会收入部分 115–1 否决；参议院 11 月 9–17 日辩论（11 日假日、15 日可能休会），1200+ 修正案，正式投票定于 11 月 18 日（周三，senat.fr + Public Sénat，日程口径）；赤字目标 12.7 亿欧元（2026 年 21.8 亿）；参议院社保事务委员会提议养老金指数化门槛由 1260 提至 1500 欧元并承诺守住 12.7 亿赤字；CMP（7+7）于 18 日后召开，50 天期限至 11 月 26 日午夜。
- 立法程序 navette / commission mixte paritaire（2026-11-11 第二轮返修新增「APRÈS LE VOTE」栏事实来源）：法案在两院间往返直至通过同一文本（《宪法》第 45 条第 1 款）；意见持续不一致时可召开 commission mixte paritaire——7 名国民议会议员 + 7 名参议员，就仍在讨论的条款提出共同文本（《宪法》第 45 条第 2 款）。来源：senat.fr《La participation des chambres hautes à l'élaboration de la loi》、Assemblée parlementaire de la Francophonie《La procédure législative》。
- 博若莱新酒：75 周年（Inter Beaujolais）；1951 年获准提前售酒、1985 年定为 11 月第三个周四；Sarmentelles 博热自 18 日晚、午夜开桶；里昂 18 日 23 时拖拉机送酒；收获自 8 月 13 日（极早），农业部预计勃艮第–博若莱产量同比少 22%；500+ 活动。
- 都灵 Nitto ATP 年终总决赛：11 月 15–22 日，Inalpi Arena；8 人——兹维列夫、阿尔卡拉斯、谢尔顿、梅德韦杰夫、科博利、菲尔斯、蒂亚弗、约达尔（Race 第 9）；辛纳膝伤 10 月 6 日结束赛季；4 名首秀（科博利、菲尔斯、蒂亚弗、约达尔），菲尔斯为法国人；分组抽签 11 月 12 日，小组赛 15–20 日，半决赛 21 日，决赛 22 日。
- 足球：意大利–法国 11 月 12 日 20:45 米兰、法国–土耳其 11 月 15 日 20:45 波尔多；法国 A1 组 4 战 10 分居首，可锁定八强席位。法甲第 11 轮 11 月 20–22 日（20 日特鲁瓦–勒阿弗尔；21 日尼斯–巴黎 17:15 + 20:45 多场；22 日巴黎 FC–昂热、洛里昂–雷恩、马赛–勒芒 20:45）。
- 电影：11 月 18 日（周三）16 部新片——《饥饿游戏：收获日出》（弗朗西斯·劳伦斯，海米奇前传，**故事设定为卡特尼斯之前 24 年、第 50 届饥饿游戏**，2 小时 38 分）、《Les Braves》（卢卡斯·东特）、《Jupiter》（亚历山大·斯米亚，德尼·梅诺谢饰核危机中的总统）、《Malika》（穆尼亚·梅杜尔）、《Camembert》（克里斯汀·斯科特·托马斯 + 吉列尔莫·吉兹）、《Fais-moi un signe》（Mipo O）。**“16 部”计数口径说明（2026-11-10 返修补注）**：为截稿时当周排片表的计数；filmscinema.fr 同日计数不稳定（搜索快照 17 部、实时页 24 部，含重复条目与跨周/音乐会放映），未采用其计数；六部点名影片及上映日期已逐一核实无误。
- 减废周 SERD：11 月 21–29 日，ADEME 协调，主题“从超消费到负责任消费”；11 月 20 日为世界儿童日（联合国纪念日）。
- VOL.5 预告用：11 月 27 日（周五）黑色星期五（日历核验）。

## 四、图片（6 图，全部公共领域，2026 年 11 月 10 日核实）

- P1 `atget-paris.jpg`：Eugène Atget（1857–1927），巴黎街景，W46 复用图，公共领域。
- P2 `chatillon-beaujolais.jpg`：Château de Châtillon（博若莱），作者自拍并释出为公共领域（Wikimedia Commons，File:Chatillon Château1.jpg）。
- P3 `vendanges-moreau.jpg`：Adrien Moreau（1843–1906）《收获》，布面油画，作者逝世 1906 年，公共领域；原图 3852×2880 降至 1280×957（q88）。
- P5 `melies-lune.jpg`：Georges Méliès（1861–1938）《月球旅行记》1902 年手绘，公共领域（File:Le voyage dans la lune drawing.jpg）。
- P7 `dore-hare-frogs.jpg`：Gustave Doré（1832–1883）拉封丹寓言插图，W46 复用图，公共领域。
- P8 `hiroshige-maple.jpg`：歌川广重（1797–1858），红枫版画，W46 复用图，公共领域，LACMA。
- 规则：P5/P7/P8 各一图（W47 新增要求），6 图 credits 详见 `assets/CREDITS.md`（含作者、来源、验证日期）。

## 五、构建与复现

构建目录：`production/2026-w47/core-fr/`（`bslib4.py`、`svglib.py` 自 W46 核心复制；`run.py`、`render.py` 自 W47 意大利核心复制，`render.py` 仅改 BASE 路径 core-it→core-fr；W46 文件未动）。

复现（顺序不可变，登记表按导入顺序累积；必须用 `tools/venv/bin/python`，永不去 /tmp）：

```bash
cd ~/workspace/weekly-git/production/2026-w47/core-fr
~/workspace/weekly-git/tools/venv/bin/python run.py        # -> svg/*.svg
~/workspace/weekly-git/tools/venv/bin/python render.py      # -> cards/*.png + La-Lucerna-VOL4.pdf
~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg La-Lucerna-VOL4-web.pdf
W47_BUILD_DIR=<core-fr> W47_OUT_MD=<core-fr>/2026-w47-fr-zh-cn.text.md \
  ~/workspace/weekly-git/tools/venv/bin/python \
  ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fr/export47.py
```

门禁（同上 venv）：`tools/p8.py extract --p8 svg/p8-exercices.svg --total 150`、`tools/occlusion_audit.py svg/`（先自检）、`tools/freeze.py baseline --build . --core-svg svg --out <dir>`、MCQ 完整性检查 `hidden_files/w47/scratch-fr/check_mcq.py .`（见 §7）。

本地改动（相对 W46 复制的构建代码，仅本核心内）：
- `svglib.py`：`wrap()` 增加 MCQ 选项整组不可拆分（见 §7）；其余与 W46 字节相同。
- `content*.py` / `expl.py`：本期全部新写内容（仅法语正文 + 简体中文讲解层）；`expl.py` 集中全部非正文字符串（沿用 W46 集中式讲解层，见 §六）。
- 仓内共享工具 `tools/p8.py` 有一处最小扩展（见 §7，未提交，待协调员复核）。

## 六、设计说明：集中式讲解层（与 W46 模式的偏离）

沿用 W46：所有非正文（读者语言）字符串集中于各版唯一的 `expl.py`（`E["key"]`），正文文件 `content*.py` 只含法语 + `E[...]` 查找。目的与 W46 KIT §六相同：`freeze.py diff` 只显示讲解层差异，避免逐版字符串替换风险。`svglib.py` 各版字节相同（本核心仅加 §7 的 `wrap()` 选项合并）。登记表类型名沿用中文（内部元数据，不印刷）。翻译题方向统一为“读者语言题干 → 法语键”。

## 七、门禁输出（实测）

### §1.1 视觉规范逐项核对（SOP §1.1，2026-11-06 版；协调员 2026-11-10 跟进要求）

| # | 项目 | 结论 |
|---|---|---|
| 1 | 纸色 #fbfaf6（非 W46 暖象牙 #f7f1e2） | 通过。`svglib.py` `PAPER = "#fbfaf6"`；8 个 SVG 均无 #f7f1e2。 |
| 2 | 禁用金色 | 通过。无 GOLD/BRICK 常量；SVG 无 #b49a4a；鹅黄 #f6e08e 为规范允许色（书衣绿上副标题）。 |
| 3 | 去掉双线外框 | 通过。`BSPage4` 只加纸色矩形，`save()` 不加外框；卡面目视确认。 |
| 4 | 不用近黑底 | 通过。无 DARK 常量、无 #2a2419；栏目条用书衣绿 #37402f。 |
| 5 | 拉丁正文 Newsreader（非 NotoSerifCJK） | 通过。`svglib.py` 逐字符选字体：拉丁 → Newsreader（正文与讲解层同为 Newsreader；D5 2026-11-12：讲解层拉丁不再走 Noto Sans CJK SC，见 §八 D5 重建），CJK → Noto Serif CJK SC（正文）/ Noto Sans CJK SC（讲解层）。SVG 字体普查（`<text>` 元素 font-family 统计，2026-11-12 D5 r2 重测）：P1 190 Newsreader / 42 Noto Sans CJK SC / 10 Noto Serif CJK SC / 1 UnifrakturMaguntia；P8 537 / 350 / 23；D5 普查（`mechanism/d5_census.py`）拉丁在 CJK Sans 0、西里尔 0、弯引号在 CJK 0；Noto Serif CJK SC 段全为中文与「→」「　」（P3 词表中文释义、P5 电影词表中文释义、P8 翻译题干中的中文），零拉丁文落入 CJK 衬线体。注：本轮前 KIT 写的 P1 94/2、P8 91/170/8 为另一计数口径；按本口径对第一轮 build-copy 重数分别为 P1 102/76/10/1、P8 108/169/23，与返修后一致（P8 Sans 169→191 为新增 14 枚徽章的级别字 + 对白条 5 个题号 + 3 条完形选项行折行所致；第二轮返修 P1 Newsreader 102→103 为 P1 头条首段改写所致、P8 Sans 191→192 为 Q100 注记改长所致）。 |
| 6 | 刊头/页脚/分隔用全角空格（非「·」） | 通过（见下文“「·」→「　」”小节）。8 个 SVG、`2026-w47-fr-zh-cn.text.md`、`ABSTRACT.txt` 中「·」出现次数均为 0；「　」出现次数（SVG 源码统计，fixfam1 2026-11-13 重测）：P1 35、P2 35、P3 19、P4 29、P5 22、P6 25、P7 15、P8 180、`.text.md` 392。注：相对 D5 r2（P2 33、P5 23、P6 24、P8 182、text.md 390），P2 +2 系 A2 新增两行译注各带 1 个「　」；P5 −1、P6 +1、P8 −2 系 C1–C4 改写后折行变化、「　」在折行处被 `wrap()` 的 `rstrip()` 消耗或释放（机制见 §七「·」小节；内容无缺失，门禁全绿）。 |
| 7 | 版心上 54pt 左右 66pt 下 48pt | 通过。MX=88px=66pt（左右）；`band()` y=72px=54pt（上）；页脚线 2596、页码基线 2624（版心底边 1977pt=2636px，页脚基线在其上 12px）；CONTENT_BOTTOM=2560（正文底边在版心底边之上，留白只多不少）；P1 刊别行基线 y=92（墨顶约 79px≈59pt，不越 y=72px=54pt 线）。 |
| 8 | 等级徽章 A2 #5c6e30 / B1 #46581f / B2 #37402f | 通过。`LV_COLOR` 与规范逐字相同；`chip()` rx=2.7（约 2pt 圆角），白字。**徽章总数 134**（2026-11-10 返修补齐后实测，按 chip 矩形统计：A2 #5c6e30 50 · B1 #46581f 65 · B2 #37402f 19；分版 P1 10 · P2 12 · P3 18 · P4 15 · P5 14 · P6 15 · P7 12 · P8 38；150 题 − 16 道配对共享题）。P8 新增：完形 Q109–116 各一枚（A2/A2/A2/A2/B1/B1/B1/A2）、对话 Q145–149 徽章条（A2/A2/B1/A2/A2）、写作 Q150 一枚 B1。 |

另核实：刊头 `Le Lucerna` 196px=147pt UnifrakturMaguntia 居中；刊别 36px=27pt 700 橄榄绿、字距 11.5px≈0.32em；导读条标题 46px=34.5pt（规范下限）；刊头下一道橄榄绿线 y=420，三色蛾居中 (975, 420)；蛾 SVG 颜色无金色 #b49a4a。家具字符串（`expl.py`）已全用全角空格：页脚 `Le Lucerna　法语周报 VOL.4　正文法语　讲解简体中文`、页码行 `第{n}版／共{total}版`（数字无空格）、刊别 `VOL. 4　总第4期`、副标题、导读条。

**「·」→「　」修复与 `tools/p8.py` 扩展（2026-11-10）：** 初版沿用 W46 旧样式，印刷字符串中共 15 处 `expl.py`（译注框 g1–g6、桥接语、日期行）与 content12/34/56/8.py 各处（议程、选项、图注、例句、图表选项、P8 答案区连接符）使用「·」作分隔。已全部改为全角空格。唯一例外是 P8 答案区的连接符曾依赖「·」作 `p8.py` 的条目边界（`split_joined` 用 `·\s*N\.` 定位条目；「　」为空白字符，会被 `svglib.wrap()` 的 `rstrip()` 在折行处吃掉，无法作可靠边界）。处理：答案连接符同样改为「　」，并对共享工具 `tools/p8.py` 作最小向后兼容扩展（未提交，待协调员复核）：`split_joined` 在空白折叠前将「　」归一为内部标记「·」；条目定位失败时回退到带 `(?<![\d.])` 前瞻的空白边界（防止 `21.8` 等小数造成假条目）；`joined` 检测接受 `[·　]`。验证：新 `p8.py` 在旧「·」版 P8 SVG 上仍抽出同一注记集 121/150（与已发 `final-fr-p8.json` 逐项相同）；在新「　」版 SVG 上抽出 121/150，注记集与键表与旧版逐项相同。`design/pdf-style` 样张 P8/P9 已查：样张答案页为第 9 页布局（SOP 明示不采用），其分隔符未作定论；本次以 SOP §1.1 正文为准。

**MCQ 选项折行修复（§1.1 排字“选择题的选项不在选项中间折行”）：** 「·」→「　」后每个分隔符宽约 2–3px，翻转了 23 个题体的临界折行，另有 10 处在旧版即已折行。机械扫查（`hidden_files/w47/scratch-fr/check_mcq.py`，解析 SVG 文本行，45 个 MCQ 题体逐项核对）于 build 5 报 33 处选项中间折行（孤立字母 `B.`、选项词组被劈开等）。根治：本核心 `svglib.py` 的 `wrap()` 在分词后将每个 MCQ 选项组（字母 + 其后各词，至下一全角空格分隔符或下一选项字母）合并为一个不可拆分 token，折行只允许发生在选项之间，不在选项之内（仅精确匹配 `A.`/`B.`/`C.`/`D.` 且前有空格/全角空格/行首时触发；小写配对字母 `a.`/`b.` 不受影响；正文不受影响）。重建后检查器报 **0 缺陷、0 未定位**（45/45 题体定位成功），并经 8 版卡面目视复核（P1 Q7/Q8、P2 Q19/Q21、P3 Q41、P4 Q44–Q48、P5 Q62–Q66、P6 Q79–Q84、P8 Q117–Q129、完形选项行 109–116 全部整组完整）。此为缺陷类根治（非逐题改写），工具改动仅限本核心的 `svglib.py` 副本；是否上收至仓内 `tools/` 由协调员定。

**未改动、记入此处的两项观察（不在协调员 8 项核对内；与 W46 做法相同）：** 字号阶梯——P1 显示标题 53px=39.75pt（规范头条 40–45pt，下限差 0.25pt），P2–P6 文章标题 `Flow.title` **实测 32px=24pt（规范次级标题 22.5–24pt，恰为上限，合规；KIT 旧称 38px=28.5pt 有误，2026-11-11 第二轮返修按 SVG 实测订正——8 个 SVG 中 `font-size="38"` 为 0 处，P2–P6 文章标题均为 32px）**；两项均沿用 W46 引擎的既有尺寸，未动。中文数字空格——讲解层与答案注记沿用 `11 月 18 日星期三`、`15 日`、`75 周年`的带空格写法；§1.1“中文里的数字不加空格”按本项目既有解释适用于页脚/页码行等家具（`第1版／共8版`已合规），W46 同样 shipped，留待协调员裁定是否全刊统一。

### 其余门禁（实测）

- 渲染：零 `FLOW OVERFLOW` / `TOO WIDE` / `NOSPACE`；终值（2026-11-11 第三轮返修后 build-fix3）：P1 头条 1556（底线 1812）、P1 预算 2242（2300）、P1 闪电问答 2491（2560）、P4 主流 771（2560）、P6 深读 1288（1300）、P6 练习 2402（2560）、P6 微练 2355（2560，新增「APRÈS LE VOTE」栏）、P7 B1 流 855（多雷插图槽 y0=871，图 260×170 已放置）、P7 金句流 1718（1830，D9 加长两句后 +30px，余量 112px）、P8 综合练习 1428（1485）、P8 答案流 2046（广重图 y=2055.7 已放置）。2026-11-11 fix4 重跑 `run.py`（build-fix4），终值与上一轮完全一致，登记表仍 150 题（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42）。
- `tools/occlusion_audit.py`：**0 flags**（自检 OK：6 类阳性对照全部触发，干净对照静默；2026-11-11 fix4 重跑）。`final-fr-occlusion.json`：`flag_count: 0`（内容不变）。
- `tools/p8.py extract --total 150`：印出注记集 **121/150**（parse: joined）；`content8.py` 沿用 W46 的显式 `PRINT_NOTES` 列表。`p8.py compare`：**CLEAN**（121/121，missing=[] extra_count=0 keydiff=[]）。抽出注记集与全部 150 键与 `final-fr-p8.json` 逐项相同（2026-11-11 fix4 重跑；本轮唯一键变化为 Q148 `devant`→`devant le`，系有意修复，`final-fr-p8.json` 已按本次抽出结果刷新该键，其余 149 键与注记集不变）。
- `tools/freeze.py baseline`（2026-11-11 fix4，从核心目录运行 `--build . --core-svg svg`，跑两次均为 **`ok: 8`**）：**人工逐项 SHA-256 比对 8/8 字节相同**（`hidden_files/w47/scratch-fix-core-fr4/freeze-fix4.json`，`--json` 输出）：p1 `6aad8b4bcdfb`、p2 `5709e000bbd7`、p3 `7828cfe33118`、p4 `7e46e630eb6b`、p5 `fff2a8d3d7ac`、p6 `7af7cf3c240f`、p7 `75237d672f20`、p8 `5bee4d4473bf`（前 12 位）。`final-fr-freeze.json` 已刷新为本次工具输出（`ok: 8`）。未改动页 P1–P3/P5–P7 的哈希与上一轮完全一致；仅 P4、P8 哈希变化，与本轮两处改动一一对应（P4 仅注记行、P8 仅对白题干与答案区折行）。**工具 artifact 提醒（沿用）**：`freeze.py` 的 OUT 参数为 `__file__` 绝对路径，复本写到 `<out>/build-copy/svg/`，而工具在空的 `<out>/svg/` 下比对时 `produced_sha256` 全空；从核心目录运行（`--build .`）时比对路径正确，本次 8/8；`--json` 标志才是报告输出口（非 `--json-out`）；build-copy 内附带的 `final-fr-freeze.json` 只是开工前核心文件的复本，不能当作本次工具输出——本次以 `--json` 写入 scratch 的 `freeze-fix4.json` 为准刷新。D5 重建（2026-11-12 r2）重跑 freeze 仍为 `ok: 8`，8 页哈希：p1 `f3e6f6d994e1`、p2 `d39cfc493b0a`、p3 `88866677d673`、p4 `3b36fccbeff9`、p5 `912f3265193a`、p6 `1061fabdde2c`、p7 `93cf42e425eb1`、p8 `870a684ba67e`（前 12 位；`hidden_files/w47/scratch-d5-rebuild-fr/core-fr/freeze-r2.json`）；8 页哈希相对 fix4 全变，系 D5 换字体所致。
- 金句逐字校验（脚本，以 `content7.py` 的 8 条金句原文对 P1–P6 SVG 文本）：**8/8**（2026-11-11 fix4 自写脚本 `hidden_files/w47/scratch-fix-core-fr4/verify-fix4.py` 复核 8/8；第三轮复校前为 7/8——Q102 金句「sortent au cinéma」非逐字，见 §八第 6 轮 D9）；范文词数 96（80–100 内）；P8 键 1–150 齐全；日期/星期核对无误（16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日）。
- P8 答案实测字号：**11.62pt**（2026-11-11 fix4，`tools/venv` 的 PyMuPDF 提取 P8 全部 469 个 span，最小 11.62pt、214 个 span 处此字号；SVG 键字号 15.5px×0.75=11.625pt；≥9.75pt 下限；与上一轮相同）。D5 r2（2026-11-12）重测：P8 全部 865 个 span，最小仍 11.62pt、560 个 span 处此字号；≥9.75pt 下限。fixfam1（2026-11-13）重测：P8 全部 858 个 span，最小仍 11.62pt；≥9.75pt 下限。
- 大报版 PDF：8 页，18,488,886 字节，SHA-256 `8809c4bae4b679d3fec2039982a30d033dfc53f40fbeea0f3c93bf2a289d3eb2`，版面 1462.5×2025pt（2026-11-13 minor1 重渲；fixfam1 18,488,281 字节 `45745d5874df…`）。
- 网页版 PDF（`tools/webpdf.py`）：8 页，1,989,709 字节（< 7 MB），SHA-256 `c024e0ad6061ad5a4c16f01e9acf71632dacbc8d30febe2cdf7d4d7a6f2c315a`；pdftotext -layout 提取印刷版/网页版各 100,857 字节、逐字节一致；webpdf 计文字 46,596 字节（2026-11-13 minor1）。
- `.text.md`：`2026-w47-fr-zh-cn.text.md`（46,553 字节，SHA-256 `5416a602158f7904da6bd2546eaac890ec8a8a2214e2e5772e2dcd59318aa56f`），由源稿导出器（`hidden_files/w47/scratch-fr/export47.py`，stub 布局模块记录调用顺序，复用 W46 stub）从 `content*.py` 源稿导出，非 PDF 反抽；39,351 字符，542 条目，150 题齐全（含 5 个配对范围行与对话/写作题），Page 1–8 标题齐全，6 图注齐全，「·」0 个、「　」392 个。`ABSTRACT.txt`：280 字节，一行简体中文，无 ASCII 双引号。
- 渲染说明：`render.py` 首次尝试（render-fix2）在 P1 卡片后异常退出（exit 120，无 traceback 输出，与第一轮 render4 同类瞬态）；重跑 render-fix2b 成功（8/8 卡片 + 大报版 PDF），未改源码。第三轮返修 render-fix3 一次成功（rc 0，8/8 卡片），无 exit 120 瞬态；本轮无 `Disk quota exceeded`（第二轮返修曾三次偶发，见 §八第 5 轮）。fix4：run/render/webpdf/export 均一次成功（rc 0），无 exit 120、无 Disk quota exceeded；本轮无偶发事件。

## 八、校对记录

- 第 1 轮（卡面目视 8 版，build 4）：2 类缺陷。(a) P5“周三电影”框：法文段末行与中文注记重叠（注记固定偏移按旧段长计算）→ 注记下移至 dy5+400，框高 440→480，辩论框下移 40px。(b) 10 条答案注记与新题错配（复用 W46 键值未改）：Q1/Q4/Q5/Q6/Q13/Q33/Q34/Q64/Q110/Q126 逐条按新题重写；另脚本审计全部 150 条注记与 5 组配对，余者均合。两类均修复后重建。
- 第 2 轮（P5 + P8 复核，build 4）：P5 电影框干净（段落结束、注记在下、无重叠）；P8 答案区 Q1–Q150 注记逐项核对无误（抽查 Q5/Q6/Q64/Q110/Q126 均正确）。结论：零问题轮次。P1–P4/P6/P7 自第 1 轮后未动，当时已零问题。
- 第 3 轮（§1.1 自查，协调员 2026-11-10 跟进，build 5→6）：(a) 「·」分隔符全刊扫查并改为「　」，`tools/p8.py` 最小扩展保持门禁可用（新旧两版 SVG 均抽出同一 121/150 注记集与同一键表）。(b) 选项中间折行：机械扫查发现 33 处，`wrap()` 选项整组合并根治，重建后检查器 0 缺陷、0 未定位，8 版卡面目视逐题复核通过。(c) §1.1 其余 7 项逐项核对通过（见 §7 表格）。(d) 两处误报澄清：P1 图注无“Wikimedia Commons”属原文如此（P1 图注 credit 本即如此，仅 P2 图注含该署名）；P2“你呢”框注记“写两句法语寄来”为源码原词（小图下“寄”易误读为“奇”）；P8 答案区“121. A（主语三单 → semble）”经 `p8.py` 抽出键表复核为 A，与登记表一致，小图下易误读为 B。结论：零问题轮次。
- 第 4 轮（第一轮校对 D1–D6 返修，2026-11-10，build-fix3/4）：D1 P5「cinquante ans avant Katniss」→「vingt-quatre ans avant Katniss」（另全刊 grep 确认无同类错误）；D2 P6 日程图加第 7 行「26 nov. — Fin du délai de 50 jours (art. 47-1)」，Q84 键 B 不变、题干不动，现可从图推出；D3 13 词全部自然写进同页正文（P3 bouteille/raisin/vigne、P4 tennis/adversaire、P5 salle/écran/acteur/actrice/réalisateur/scénario/séance/public），逐词 grep 验证（剔除词表框与署名后仍命中）；D5 P8 补 14 枚徽章（完形 8、对白条 5、写作 1），徽章总数 120→134（=150−16 配对共享题）；D6 P1 Q2/Q3 改写为「C'est ___ que…」结构，与 P2 Q11/Q13 不再重复且「le」无法填入，键不变（mercredi/jeudi）。O5 两处顺手修：P2 Q18 去句号后填空线单行、P7 gp5 删一字后单行；O2「16 部」计数口径已注于 §三。两处算术订正：校对笔记称 P8 应有 138 枚（150−16=134，误算）、称 de 有 138 枚（实测 de 127，亦缺同 14 题）；fr 目标 134 已达。返修附带改动：P6 图表高 44px 死区回收（第 7 行净增约 4px）、P8 B–E 组 gap 11→5（省约 138px 供徽章）、`content8.py` 新增 `badge_opt`/`badge_strip` 两个仅绘制 helper（登记表与编号不动）、export stub 加 `_fit` 守卫（badge helper 在导出桩下仅记文本、不绘徽章）。门禁全部重跑：run.py 零溢出、render + webpdf 重渲、occlusion 0 flags、p8.py extract 注记集与 `final-fr-p8.json` 逐项相同、p8.py compare CLEAN（121/121）、check_mcq 0 缺陷 0 未定位、freeze 工具 8/8（从核心目录运行）、print/web 文字层词级多重集相等、P8 最小字号 11.62pt、§1.1 逐项重测通过、8 版卡面目视通过。结论：零问题轮次。记录见 `hidden_files/w47/scratch-fr-fix/FIX-LOG-fr.md`。
- **返修后观察（非缺陷，留待下一轮校对）**：Q130、P3 Q36/Q37 存在与 O5 同类的孤行填空线，均为第一轮已有、非返修回归；Q130 实测超宽 15.3px，删句号/删空格只能省约 5px，无零风险修法，故不动。P4「LES CHIFFRES DU SPORT」框注记的孤行「。」已于 fix4 修掉（见第 7 轮），不再是观察项。
- 第 5 轮（第二轮校对 D7/D8 返修，2026-11-11，build-fix2）：D7 4 词全部自然写进同页正文，不删译注——P1 头条首段「Premier titre à Paris, neuvième en Masters 1000.」→「Le vainqueur remporte son premier titre à Paris, le neuvième en Masters 1000.」（事实不变：巴黎首冠、第 9 个大师赛冠军，ATP/美联社已核）；P4 第 2 段末句「Une victoire en deux sets, sans tie-break dans le deuxième.」→「Un choc remporté en deux sets, sans tie-break dans le deuxième.」（事实不变）；P6 右栏末新增「APRÈS LE VOTE」小栏：「Après le vote du Sénat, le texte repartira vers l'Assemblée : c'est la navette parlementaire, les allers-retours entre les deux chambres. Si le désaccord persiste, une commission mixte paritaire — sept députés et sept sénateurs — cherchera un texte commun.」（事实来源：senat.fr + APF，《宪法》第 45 条第 1/2 款，见 §三；P6 深读流余量仅 12px，加句会溢出，故置于微练流末，P6-micro 1985→2355/2560）。验证：SVG 文本枚举、剔除译注字符串后重数，4 词每词正文恰好 1 次（`d7-verify-fix2.py`，PASS，上下文逐条可见）；`.text.md` 剔除译注行后复核亦通过。D8：P7 金句第 4 句语法点「avoir lieu：举行、发生。」→「se terminer en beauté：圆满收尾。」；P8 答案注「100. beauté（avoir lieu 举行）」→「100. beauté（se terminer en beauté 圆满收尾）」；Q100 题干与键不动；P7/P8 `lieu` 均为 0 处。KIT 文字订正：§7「未改动」段与 §九第 4 条的「P2–P6 标题 38px=28.5pt」按 SVG 实测订正为 32px=24pt（次级标题上限，合规；`font-size="38"` 全刊 0 处）；§九第 1 条与 §二.4 按 F-MAIL 规则改写（投稿只认用户直接发来的，不查邮箱）。不修：O6/O7/O8、D4、头条 39.75pt、无首字下沉、中文数字带空格，均未动。门禁全部重跑：run.py 零警告、render + webpdf 重渲、occlusion 0 flags、p8.py extract 121/150 与 compare CLEAN（121/121）、check_mcq 0 缺陷 0 未定位（45 题体、1,448 渲染行）、freeze 工具 8/8 + 人工 SHA-256 比对 8/8、print/web 文字层逐字节一致（46,695 字节、7,292 词）、150 题键与 `.text.md` RÉPONSES 区机械比对 0 不符（Q150 为 p8.py 抽出截断旧 artifact，前缀一致）、P8 最小字号 11.62pt、§1.1 逐项重测通过、8 版卡面目视通过。结论：零问题轮次。记录见 `hidden_files/w47/scratch-fr-fix2/FIX-LOG-fr2.md`。本轮偶发事件：`render.py` 首次跑 exit 120（P1 卡片后，与第一轮同类瞬态），重跑成功；三次写盘偶发 `Disk quota exceeded`（磁盘 46G 空闲，小文件写与重跑均成功，无数据丢失）。
- 第 6 轮（第三轮复校 D9 返修，2026-11-11，build-fix3）：D9——P7 金句第 6 句与 Q102 题干把 P5 原文「dans les salles de cinéma」缩写成「au cinéma」，非逐字引用（第三轮复校 8 条金句机械比对：其余 7 条 VERBATIM，唯 Q102 NOT-VERBATIM；前两轮称「金句 8/8 逐字」失实，实为 7/8）。修复只动 `content7.py` 两处（金句 → « Mercredi 18 novembre, seize films sortent dans les salles de cinéma en France. » (page 5)；Q102 题干 → 「Mercredi, seize films ___ (sortir) dans les salles de cinéma.」），键 `sortent` 不动、其余 7 条金句不动；P5 原文（content56.py）及其他「au cinéma」正文句（P5「Et si on ne va pas au cinéma…」、P5 讨论题、P8 对白）均未动。独立核实：源码、P7 SVG（`<text>` 元素拼接后逐字在位，旧措辞 0 处）、印刷版/网页版文字层、`.text.md` 四处一致。改后整期重渲染：run.py 零警告（P7 金句流 1688→1718/1830）、render + webpdf + export 均一次成功；门禁全部重跑：occlusion 0 flags、p8.py extract 121/150 与 compare CLEAN（121/121）、check_mcq 0 缺陷 0 未定位（45 题体）、freeze 工具 8/8（跑两次，`--json` 输出 `freeze-fix3.json`，`final-fr-freeze.json` 已刷新；仅 P7 哈希变 629cfe063bbd→75237d672f20，其余 7 页与上一轮字节相同）、print/web 文字层逐字节一致（各 103,001 字节）、150 题键与 `.text.md` RÉPONSES 区机械比对 0 不符（自写 `verify-fix3.py` 与 fix2 的 `keys-verify-fix2.py` 双重验证，Q150 按既定口径）、金句逐字复核 8/8、P8 最小字号 11.62pt、徽章 134 枚（50/65/19）、§1.1 逐项重测通过（纸色/金色/「·」/38px/「　」计数与上一轮一致）、8 版卡面目视通过（P7 新折行干净，无溢出/压诊所栏；其余 7 版无回归）。结论：零问题轮次。记录见 `hidden_files/w47/scratch-fr-fix3/FIX-LOG-fr3.md`。本轮无偶发事件（无 exit 120、无 Disk quota exceeded）。
- 第 7 轮（第四轮复校 fix4 返修，2026-11-11，build-fix4）：两处已确认缺陷，只动核心源两文件。Q148 法语错（核心错，10 版共有；6 个 fr proof1 一致记为 R1）：`content8.py:170` 键 `devant`→`devant le`，`:176` 对白题干 `On se retrouve (148)___ du cinéma ?`→`On se retrouve (148)___ cinéma ?`（删 "du"）；对话其余 4 空与键未动，键注「电影院门口」不变。填入后句子通顺：`On se retrouve devant le cinéma ?`。三源一致：源码、`.text.md` 第 1039 行题干与第 1083 行附录「148. devant le（电影院门口）」、P8 SVG 对白节点与答案节点。P4 孤儿句号（与 fr-ja D1–D3、nl D6/D7 同类，贪心断行器把句号单独断行；旧版 P4 SVG y=550.53 独行「。」）：`expl.py:123` `chiffres_note` 删「决赛」二字（实测整串 387.0px 仅超栏宽 378.5px 8.5px，删 2 字后 344.0px 单行；信息完整——「大师赛结果」仍指大师赛决赛结果，框内上文已写巴黎决赛比分），由 `wrap()` 验证单行；未改断行宽度（原串只超 8.5px，无需动 `content34.py:168` 的栏宽）。P4 SVG 文本逐项比对（对 fix3 build-copy）：仅 2 行去、1 行入，其余 213 行坐标与内容全同，零位移。改后整期重渲染：run.py rc 0 零警告（流终值与上一轮完全一致）、render + webpdf + export 均一次成功；门禁全部重跑：occlusion 0 flags、p8.py extract 121/150 与 compare CLEAN（121/121）、check_mcq 0 缺陷 0 未定位（45 题体）、freeze 工具 8/8（跑两次，`--json` 输出 `freeze-fix4.json`，`final-fr-freeze.json` 与 `final-fr-p8.json` 已刷新——仅 P4 哈希 37cf3412c3f8→7e46e630eb6b、P8 哈希 ce072a017cd4→5bee4d4473bf，其余 6 页与上一轮字节相同；键表唯一变化为 Q148）、print/web 文字层逐字节一致（各 102,978 字节）、150 题键与 `.text.md` RÉPONSES 区机械比对 0 不符（自写 `verify-fix4.py` 与 fix2 的 `keys-verify-fix2.py` 双重验证，Q150 按既定口径）、孤儿标点全扫 0（独行 。/，/、/：/；/！/？/./:/–/闭引号全 0；P4/P6 各 1 处独行 "— " 为 fix3 基线即有的同坐标折行，非本轮回归、不动）、creambox 0 违规（#f0eee5 框内文本均在框界内，实测字体计量）、金句逐字复核 8/8、P8 最小字号 11.62pt、徽章 134 枚（50/65/19）、§1.1 逐项重测通过（纸色/金色/「·」/38px/「　」计数与上一轮一致）、8 版卡面目视通过（P4 注记单行干净，P8 对白与答案区折行干净；其余 6 版无回归）、网页版 P4/P8 另行渲染目视通过。结论：零问题轮次。记录见 `hidden_files/w47/scratch-fix-core-fr4/FIX-LOG.md`。本轮无偶发事件（无 exit 120、无 Disk quota exceeded；一次 `exec` 会话中途 aborted，freeze 第二次运行重跑即通，非构建问题）。
- D5 重建（2026-11-12，用户 B 档三周全修；机制见 `hidden_files/w47/scratch-d5-plan/D5-PLAN.md` 与 `mechanism/PILOT-REPORT.md`）：核心 svglib 装 D5（`_D5_READER = "cjk"`，机制 `apply_variant.py` 补丁 + fix2 路由保留；`svglib.py` 23,410 字节）。r1 门禁（06:26–06:44 UTC）除两项外全绿：census PASS（拉丁/西里尔/弯引号在 CJK 均为 0）、occlusion 0 flags、p8 121/150 compare CLEAN（vs 核心与 vs 修前基线）、spill 0、edge 0 TOUCH/NEAR、freeze 8/8、印/网文字层逐字节一致；**boxtitle 4 DEFECT**（P3 `LES DATES EN CHIFFRES` +7.6px、P4 `LES PHRASES DU COMMENTATEUR` +36.5px、P5 `周三电影` +43.3px、P6 `TROIS DATES POUR COMPRENDRE` +24.5px，均为粗体拉丁在 Newsreader SemiBold 变宽所致）；creambox 审计崩溃（基线目录缺 moth，已补）。修复 8 处（只降字号、未改一字，`.text.md` 无需重出）：content34.py `head_zoom` 23→22、P4 框题 `tsize=21`；content56.py `head_cine` 23→20、语法头 25→23、`head_comp6` 25→24、P6 框题 `tsize=21`；content7.py 语法头 24→23、`head_clinic` 25→23。r2 全套门禁（07:44–07:46 UTC）**全绿**：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE（`tools/head_check.py` PASS）；render + webpdf 重渲（网 PDF 07:31 曾被运行时重启打断，r2 重跑补齐）；occlusion 0 flags；p8 121/150、CLEAN；freeze 8/8、diff +0 CJK/+0 Latin；boxtitle 0 DEFECT；creambox PASS 0 defects（n=492，中位 1.016、粗体 1.049、常规 1.000；P8 193 行、余量 36.1px 不变）；spill 0；edge 0 TOUCH/NEAR；census PASS（0/0/0）；印/网文字层逐字节一致（各 101,106 字节；webpdf 计文字 46,527 字节）。印 PDF 18,475,436 字节 SHA-256 `f36c32f0…`、网 PDF 1,985,431 字节 SHA-256 `ff08e749…`（前 12 位；见 §七）。P8 最小字号重测仍 11.62pt。门禁日志：`hidden_files/w47/scratch-d5-rebuild-fr/core-fr/logs-r2/`；工作日志：`hidden_files/w47/scratch-d5-fr/RUN-LOG.md`。
- 图片核查：6 图均为公共领域（Wikimedia Commons 文件页 2026-11-10 核实，见 `assets/CREDITS.md`）；P1/P2/P3/P5/P7/P8 图注与 credits 一致；Châtillon 与 Moreau 收获图卡面目视确认。
- fixfam1（2026-11-13，独立重校 A1/A2/C1–C5 返修；工作日志 `hidden_files/w47/scratch-fix-fr-family1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/core-fr/logs-fixfam1/`）：A1 P2 图注改写为城堡描述（`content12.py:184`）；A2 DIRE LA DATE 表补 ven. 20（儿童节）与 sam. 21（都灵半决赛 + 减废周首日）两行（`content12.py` + `expl.py` 新增 `date_20`/`date_21`），行距 40→34、练习区块下移 36（`ey = dy + 356`），实测行墨隙 3.2、"Exemples" 距分隔线 10.6、练习流底距流限 8；C1 `debat5_note` 张→件（text.md 两处同源）；C2 P8 E 节 135–139 删 `Traduisez : `×5；C3 答案 120/131 `半过去时`→`未完成过去时`；C4 三栏目 gloss 区分（À VOUS !→轮到你了！、MICRO-DRILLS→微练习、博若莱副标题行→博若莱新酒小测）；C5 `export47.py` 头行改为中文（经重导出）。门禁全绿：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心与 vs 修前基线，keydiff=[]）；boxtitle 0 DEFECT（40 titles）；creambox PASS 0 defects；spill 0；edge 0 TOUCH/NEAR；census PASS；freeze diff +0 CJK/+0 Latin；印/网文字层逐字节一致（各 100,873 字节）；text.md diff 仅含意改行（+8 行 A2、余为替换行）；P2 卡面目视通过（图注与城堡图相符、7 行日期表干净无溢出）。
- minor1（2026-11-13，全新一轮重校发现 2 返修；工作日志 `hidden_files/w47/scratch-fix-fr-minor1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/core-fr/logs-minor1/`）：发现 2——P3 BEAUJOLAIS 盒子桥接行 `bridge_dieppe`（`expl.py:95`）两节近义并列（C4 副作用），改为 `微练习　博若莱新酒小测。`（首节取 MICRO-DRILLS gloss `微练习`，与 head_micro 一致；次节取盒子 gloss `博若莱新酒小测`，与兄弟版 `<MICRO-DRILLS gloss>　<盒子 gloss>` 结构一致——en "Quick drills　the Beaujolais Nouveau quiz."、zh-tw "微練習　薄酒萊小測。"；次节与盒子标题 gloss `博若莱小题` 不重复）。已核实该源只被 core-fr 用（各版 `bridge_dieppe` 各在自家 `expl.py:94/95`，其余 10 版原已是正确结构，无需改）。门禁全绿：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心与 vs 修前基线，keydiff=[]）；boxtitle 0 DEFECT（40 titles）；creambox PASS 0 defects；spill 0（102 OBSERVE）；edge 0 TOUCH/NEAR；census PASS（0/0/0）；freeze diff +0 CJK/+0 Latin；印/网文字层逐字节一致（各 100,857 字节，94,229 字符，multiset 0）；text.md diff 恰 1 行（L383 桥接行）；逐页 SVG 哈希：仅 p3-culture.svg 变；P3 卡面目视通过（桥接行 `微练习　博若莱新酒小测。` 在栏内干净）；P8 最小字号重测仍 11.62pt（858 spans）；「　」计数不变（text.md 392）。三件 SHA：印 18,488,886 B `8809c4bae4b6…`、网 1,989,709 B `c024e0ad6061…`、文 46,553 B `5416a602158f…`。未 commit、未 push。

## 九、待协调员确认

1. **读者来信（F-MAIL 规则）**：投稿只认用户直接发来的；用户未直接发来投稿即无来信，**不查邮箱、不核实邮箱状态**。本期 P7 读者园地为标注明确的编辑部示例（见 §二.4）；入仓前不核查邮箱。
2. **`tools/p8.py` 扩展复核**：`split_joined` 归一「　」+ 回退边界 + `joined` 检测接受 `[·　]` 三处改动在工作树中未提交；已验证向后兼容（旧「·」版仍抽出同一注记集），请复核后决定是否提交。另 `tools/freeze.py` 的 OUT 路径 artifact（复本写 `<out>/build-copy/svg/`，比对却查空的 `<out>/svg/`）请工具负责人修复；本次以人工 8/8 比对为准。
3. **`svglib.py` `wrap()` 选项合并是否上收**：改动仅限本核心的 `svglib.py` 副本（W46 与其他核心未动）；如认定为通用缺陷类修复，请决定是否合入仓内 `tools/` 或各核心模板。`check_mcq.py` 在 `hidden_files/w47/scratch-fr/`，可作同类检查的复用工具。
4. **字号阶梯与中文数字空格两项观察**（见 §7）：P1 显示标题 39.75pt（规范下限差 0.25pt）、P2–P6 标题实测 32px=24pt（规范次级标题上限，合规；2026-11-11 第二轮返修已订正 KIT 旧称 28.5pt）、讲解层中文数字带空格，均沿用 W46 引擎既有做法，未动；请裁定是否全刊统一。
5. **参议院 11 月 18 日投票结果**：本期按单源日程口径写“est prévu”；VOL.5 须以实际投票结果为准（另：11 月 20 日国家预算审议、12 月 9 日正式投票、11 月 27 日黑色星期五，见 VOL.5 预告）。
