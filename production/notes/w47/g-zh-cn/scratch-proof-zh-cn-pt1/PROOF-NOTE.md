# W47 zh-cn-pt 第一轮独立校对笔记（proof1）

- 校对员：独立复校员（与 zh-cn-pt builder、zh-cn 核心 builder、各轮复校员不同人）
- 对象：`production/2026-w47/2026-w47-zh-cn-pt/`（#3 棒终版，2026-11-11）
- 日期：2026-11-11（EST 13:07 开工）
- 依据：SOP.md §8/§1.1、附则一/二，`FANOUT-REPORT-zh-cn.md` 第 3 棒、pt/`EDITION-RECORD.md`、
  `brief-coordinator.md`（实际位置见文末说明）
- 工作目录：`~/workspace/weekly-git`；笔记目录：`hidden_files/w47/scratch-proof-zh-cn-pt1/`
- 红线遵守：只复校，不改任何生产文件，不 commit、不 push、不 insert、不跑 lint --write。
  run.py 只在 scratch 副本里重建（OUT 已改向并验明在 scratch 内）；渲染只读交付 PDF；
  收工全版 41 文件 SHA 与开工快照逐一相同（见 GATE-LOG）。

## 开工探针（双通）

- `echo test | git hash-object -w --stdin` 成功（`9daeafb9…`）。
- `hidden_files/w47/scratch-proof-zh-cn-pt1/.probe` 真实写盘成功。

## 身份核对（自行算出）

| 文件 | 字节 | SHA-256（完整，我方实测） | 与任务先验值 |
|---|---|---|---|
| 印刷 PDF `Lucerna-VOL4-PT.pdf` | 41,734,759 | `2286485f2608d2a144d37e9451f7a1945313e54e1f6ba1b540aec1ab5484859c` | 一致 |
| 网页 PDF `Lucerna-VOL4-PT-web.pdf` | 2,647,093 | `030f52fb82087f8fe13f3465b74ee61b8c02b6e7d8a4740280ff7fa66cac76fa` | 一致 |
| 文本导出 `2026-w47-zh-cn-pt.text.md` | 50,846 | `9207974bed3d5d16c4312752ad22a4219f0033e33d9264c29c07adfe3d44cb71` | 一致 |

双 PDF 均为 8 页。身份相符，继续校对。

## 结论：3 条缺陷，不可定稿

按 SOP §8.4，fan-out 版定稿须经独立复校零问题。本轮发现 **3 条同类几何缺陷（D-01～D-03）**，
均为 de/fr 已出的同类缺陷——**盒标题真墨越过自家奶油盒右缘**。其余全部通过。
定稿决定权在协调员，本笔记只报事实。

## 缺陷清单

三处盒标题的可用墨宽均为 **404.5px**（盒右缘 − 标题 x），标题均按 23pt sans bold 实测。
核查方法（三重证据，逐处相同）：① PIL 真墨（与构建库同款分 run 字体：Newsreader/Noto Sans CJK SC，
`svglib._runs/_pil`）；② 交付印刷 PDF 150dpi 渲染像素扫描（橄榄绿墨点 vs 奶油 `#f0eee5` 盒缘）；
③ 裁切图目视。核心版同名标题全版扫查 0 旗（核心英文后缀短、装得下）——缺陷由 fan-out 的葡语
后缀加长引入，`box()` 不折行标题也不验标题宽。

### D-01（中）：P1 数字框标题越奶油盒右缘 21.5px

- **位置**：P1 头条流第 2 栏奶油盒，`content12.py` L47 `f.box("数字看本周　Esta semana em números", …)`。
- **实测**：盒 rect `x=538.5, w=422.5`，右缘 **961.0**；标题 `x=556.5, y=1147.3`，
  PIL 真墨右缘 **982.5**、PDF 像素右缘 **981.7** → **越边 21.5px（像素 20.7px）**。
  标题墨宽 426.0px > 可用 404.5px。
- **目视**：裁切 `render/crop-p1-numbox.png`——“números” 整词挂在奶油盒外白纸上，头版肉眼可见。
- **严重度：中**。只越盒边、未撞任何文字（该栏右侧为空白），但这是头版盒标题，属 SOP §8
  “逐版看图：查溢出” 的溢出类。

### D-02（小）：P2「本周生活小日历」标题越奶油盒右缘 4.5px

- **位置**：P2 第 3 栏奶油盒，`content12.py` L187 `f.box("本周生活小日历　Datas desta semana", …)`。
- **实测**：盒 rect `x=989.0, w=422.5`，右缘 **1411.5**；标题 `x=1007.0, y=237.0`，
  PIL 真墨右缘 **1416.0**、PDF 像素右缘 **1415.0** → **越边 4.5px（像素 3.5px）**。
  标题墨宽 409.0px > 可用 404.5px。
- **与 #3 修复的关系**：#3 把标题从 “As datas desta semana”（止于 x=1446.0）缩短为
  “Datas desta semana”（止于 1415.8），KIT 称“距山谷照 23.7px 干净”——该量是对**照片左缘
  1439.5**，不是对**盒右缘 1411.5**。照片碰撞修好了（实测距照片 23.5px），盒边仍越 4.5px。
  「卡片测量不能单独定论」正在于此：量对了边才算数。
- **目视**：裁切 `render/crop-p2-caltitle.png`——末字 “a” 贴压盒边、微越。
- **严重度：小**。幅度最小，但标题墨确实穿过盒界，与 D-01/D-03 同类，须同批修。

### D-03（小）：P5「这一周的高频词」标题越奶油盒右缘 3.5px

- **位置**：P5 第 2 栏奶油盒，标题 “这一周的高频词　Palavras da semana”。
- **实测**：盒 rect `x=538.5, w=422.5`，右缘 **961.0**；标题 `x=556.5, y=714.8`，
  PIL 真墨右缘 **964.5**、PDF 像素右缘 **963.2** → **越边 3.5px（像素 2.2px）**。
  标题墨宽 408.0px > 可用 404.5px。
- **目视**：裁切 `render/crop-p5-weekwords.png`——末字 “a” 贴在盒边、微越。
- **严重度：小**。与 D-02 同量级，须同批修。

### 为什么 11/11 门禁没抓到——工具盲区（须修工具，不计入本版缺陷数）

`tools/occlusion_audit.py` 的 BOXTITLE 类只考察**带描边**的 rect 或 `fill == "#2c2822"` 的 rect
（`occlusion_audit.py` L471–478：`e.attrs.get("stroke") not in (None, "none") or fill == "#2c2822"`）。
奶油盒 `fill="#f0eee5"` 且无描边，根本不在候选集里——审计对全部无描边奶油盒的标题是盲的。
我方自跑审计确为 0 旗（自检 6 类全触发），与上述三处越边并存，不是审计跑错，是类目覆盖缺失。
按 SOP 附则二“发现工具缺陷先修工具并复验”，此盲区应由工具线修（BOXTITLE 候选应含无描边浅底盒），
修后复验；本次校对未动工具（只复校）。

## #3 报告修复点逐项复核（全部存活，D-02 除外见上）

| #3 修复点 | 我方实测 | 结论 |
|---|---|---|
| P4 C-head “Ler o calendário” | `text_w` 25pt = **339.0px**（与报告一致）；run.py 0 HEAD TOO WIDE | 存活 |
| P7 A2-head “Final e pacotes” | `text_w` 24pt = **371.9px**；B1 345.3px、B2 318.5px，均与报告一致 | 存活 |
| P7 读者来信注去 “em VOL.4” | `content7.py` L91 实为 “VOL.3 prometeu cartas reais; nenhuma chegou até 10 nov.”；P7 teaser 止于 **2588.78**（页脚线 2596，清 7.2px） | 存活 |
| P2 日历标题缩短 | 止于 x=1415.8/1416.0，距山谷照 23.5px | 存活但未修净（D-02） |
| P4 gloss 6 行（“Notas｜”前缀实测） | `wrap("Notas｜"+…,"sans",20.5,内宽386.5)` = **恰 6 行**，与渲染 SVG 6 行逐行一致；盒底 792.2，下一行 “GEN，” 墨顶 ≈801，清 ≈9px | 存活 |
| P2 词卡例句各 1 行 | 4 句 `wrap` 均 1 行；渲染中 4 句同在 y=1752.1 单行 | 存活 |
| P8 keys 止于 2552.7 | run.py 重建 `flow[P8-keys] ended col 3/3 y=2553`，2552.7 一致（底限 2560） | 存活 |

## 核心 D4 / D5 同步落地核对（逐处源码行 + 实测值）

### D4：BO5 首胜 vs T1 加「全球总决赛」限定——全部同步

- P4 正文段 `content34.py` L130 / text.md:695：“…BLG赢了T1，这是中国队**第一次在全球总决赛的BO5里**打赢T1。”——与核心逐字同。
- Q56 题干 `content34.py` L211 / text.md:817：“BLG是**第一次在全球总决赛的BO5里**打赢___。”——与核心逐字同（仅 instr "Fill in"→"Completa"）。
- Q56 键注 text.md:1905：“56. T1 — A BLG venceu a T1 **pela primeira vez num BO5 dos Worlds**.”——“primeira vez + dos Worlds”限定齐全，与核心注 “BLG beat T1 for the first time in a Worlds BO5.” 对应。
- 全版扫查：中文 “第一次” 恰 2 处（上两处），均带限定；`首胜/首次打赢/第一次打赢` 等无限定表述 0 命中。

### D5：GEN「今年一场没输」为假——已改 S16 表述；「淘汰赛一局没输」为真、保留

- P1 `content12.py` L42 / text.md:37：“GEN**在S16一场没输**，只丢了一小局：瑞士轮3胜0负，八强3比0，半决赛3比0。”——S16 限定在位。
- P4 `content34.py` L131 / text.md:697：“GEN**在S16一场没输**，只丢了一小局——瑞士轮3胜0负（**对LYON 2比1**），八强3比0，半决赛3比0。”——S16 限定 + 瑞士轮 2–1 负 LYON 的丢局细节在位。
- 保留句 `content34.py` L160 / text.md:729 与 P4 事实框：“**GEN今年 — 淘汰赛一局没输**”——淘汰赛限定，3–0/3–0 两场确一局未丢，为真，保留正确。
- 残留扫查：`今年一场没输 / 今年一局没输` 在 .py、text.md、8 个 SVG 中 0 命中。

## de/fr 同类缺陷专项排查

| 缺陷类 | 我方实测 | 结论 |
|---|---|---|
| P1 数字框标题越奶油盒右缘 | 见 D-01（21.5px） | **有缺陷** |
| P2「本周生活小日历」标题越边 | 见 D-02（4.5px） | **有缺陷** |
| P1 数字框内引用收尾引号孤儿行首 | 盒内 14 行逐行核查：无一行以 》」』】)）开头；「《试探》」独占一行、行首为《（kinsoku END-pass 设计行为）；两处 “)” 是同行拉丁 run 的独立 `<text>` 元素（与行内其余文字同 y=1287.3 / 1418.3），非行首 | 通过 |
| P1 截止线越边 | Fecho 段 5 行 + 单行 “Fecho: 10 nov. — a final ainda não jogada”：墨右缘最大 1823.5，清版心右缘 1862 达 38.5px；均在日历盒（底 1288）内 | 通过 |

## 逐项核查结果

### 1. 全量目视（自交付印刷 PDF 重新渲染 110dpi，不采信 builder 的图；网版 P1/P8 同法）

- P1–P8 逐版目视：除 D-01～D-03 三处盒标题越边外，零溢出、零重叠、零压页脚、图片与出处均在位。
- 网版 P1/P8 目视与印刷版一致（P1 同一越边在网版亦可见），无豆腐块。
- P4 gloss 盒 6 行、盒底清 “GEN，”行；P7 下期预告带清页脚线；P8 答案区末行清页脚。
- 事实抽查（均与正文/表格互核一致）：P2 练习例 320−80=240；P4 四分之一决赛 4 场比分与 Q57–60 一致、决赛 11月15日凌晨3点；
  P6 图表 139.38（22天总数）vs 7.77（单日最高）两柱与 Q93–95 一致；11月15日为星期日、11月22日为星期日
  （与“周日 11月15日”“周日 11月22日”一致）；Q76/Q77 片名《珠穆朗玛：云中彼岸》《我们仅有一次的人生》
  为简体（ja 版繁体片名缺陷未复现）。

### 2. 150 题逐题手验（AST 提取题干 + REG + P8 印刷键三源对齐，再逐题验算键与题干配对）

- 方法：AST 提取 150 道题的题干/键/注（`stems.json`），与 REG（`reg.json`）逐项对齐 0 不符；
  再与 P8 印刷键（`p8extract.json`）比对：**149/150 精确**，唯一非精确为 Q150 开放写作题，
  印刷键为 “✓”（“✓ = 写作题”设计，与 P8 栏头 “Todas as notas em português ✓ = a tarefa de escrita”一致）。
- 分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；级别 A2 56 / B1 69 / B2 25；
  题型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1；编号连续 1–150。均与 KIT 一致。
- **键本身逐题验算**（题干、原文、图表再验算，非仅 P8==REG）：**150/150 的键与题干/正文/图表相符**，
  含易错点：Q9 包裹高峰 11–13日（非 12–15日）、Q22 240=320−80、Q56 D4（见上）、Q76/Q77 片名日期 6/7日、
  Q90 “二十二”中文数词、Q113–120 判断题（Q114 “第20个小雪节气”为假、B 正确）、Q117 半决赛早上6点（赛程原文）、
  Q126 冯绍峰、Q141–146 小林阅读 passage（深圳/半决赛/书/妈妈/顺序 A/深圳）、Q147–149 情景对话。
  配对题逐组核对选项表：Q25–28 a/b/c/d、Q43–46 b/d/a/c、Q61–64 d/b/c/a、Q79–82 c/b/d/a、Q97–100 c/d/a/b，均正确。
- 结论：三源同错类风险已用手验排除（如 en Q73 前车之鉴的查法），**本题键表无内容错误**。

### 3. 金句 8 条逐字比对正文（SOP §4：须摘自本期自己的文章）

8 句在 text.md 中各出现 **2 次**（正文 1 次 + P7 1 次），逐字一致，出处页码与标注一致：

1. 「决赛对阵GEN」（P1）2. 「包裹都到了吗」（P2）3. 「小雪气寒而将雪矣」（P3）4. 「两支中国队进了四强」（P4）
5. 「先看简介，再决定」（P5）6. 「无高峰，全高峰」（P6）7. 「先打开看一看，再确认收货」（P6）8. 「悦读深圳」（P3）

葡文译文均准确（如 8. “Ler com alegria em Shenzhen — o tema do Mês da Leitura de Shenzhen.”）。

### 4. 讲解层专项（fan-out 特有）

- 讲解/界面语言确为葡文：栏目副题、桥接、说明、注前缀 `Notas｜`、工具箱、读者来信披露、图表注、答案简析、
  ABSTRACT 均为葡文；葡文拼写/性数抽查无误。
- 泄漏扫描：核心与本版 SVG `<text>` 交集 1087 串中，含 3 个以上英文词的未译英文散文串 **0 条**；
  冻结差分显示被替串均为英文讲解层（如 “Fill in the blank”→“Completa a frase”）。
  「体育　Sport」为葡文同形（KIT 已裁定）；「悬疑 = suspense, b」同形渲染（KIT 已裁定）。
- 读者来信：P7 为编者示例 + 葡文披露（“Nota da redação: VOL.3 prometeu cartas reais; nenhuma chegou até 10 nov.
  Adiado, não cancelado.”），与 KIT / F-MAIL 规则一致；中文半句 “VOL.3曾预告本期刊登真实来信和最佳作文”在位。
- MUSTER 范文：`MODELO` 去空格实数 **138 字**（120–180 内）；P8 栏 “Um modelo de 138 caracteres segue.” 一致；
  “Texto-modelo” 全文与源码一致。
- ABSTRACT.txt：葡文单行，331 字节，0 个 ASCII 双引号，= `tables.py` ABSTRACT['pt'] + 换行（AST 核对），内容与本期事实一致。
- P1 徽章拉丁-only：“TEXTO CHINÊS　EXPLICAÇÕES EM PORTUGUÊS”，无 CJK（freeze strict-CJK 0 印证）。

### 5. VOL.4、徽章、字号

- VOL.4：刊头 `简体中文版　VOL.4　S16决赛　包裹到了　小雪`、页脚
  `Lucerna　简体中文周报 VOL.4　LUCERNA — SEMANAL EM CHINÊS SIMPLIFICADO`、页码行 `Página N de 8`（N=1–8）逐页核实；
  P7 下期预告 “Na próxima semana (VOL.5)” 为合法下期指称，与核心 “Next week (VOL.5)” 一致，非误印。
- 徽章：SVG `rx="2.7"` 矩形逐页 {1:10, 2:15, 3:15, 4:15, 5:15, 6:15, 7:12, 8:38}，**全刊 135 枚**，与核心逐页相同；
  P8 键注 A2 11 / B1 24 / B2 3 = 核心。
- P8 最小字号：PyMuPDF 独立实测印刷 PDF 与网页 PDF 均为 **9.98pt ≥ 9.75pt**（SOP §1.1 底线；低于 11.25pt 目标，
  属 §1.1 让步 4，KIT 已记）。P8 其余字号 9.98–34.5pt。

### 6. 机械门全套自跑（构建解释器 tools/venv/bin/python，PIL 13.0.0）

详见 GATE-LOG.md。结果一览：

| 门 | 我方自跑结果 |
|---|---|
| rebuild（scratch 副本 run.py） | RC=0，TOTAL 150，0 溢出警告；**8 SVG 与生产件逐字节一致** |
| occlusion | **0 flags**（自检 OK，6 类 planted 全触发；核心 0 旗；NEW 0）——但对奶油盒标题盲（见工具盲区） |
| p8 extract | **150/150** |
| p8 compare（核心 vs 本版） | **CLEAN**，missing=[]，extra_count=0，keydiff=[] |
| freeze diff --strict-cjk | exit 0；新增 CJK **0**（逐页 0/0/0/0/0/0/0/0） |
| freeze baseline（核心） | exit 0；**8/8** 字节一致，核心完整性未变 |
| print/web 文字层 | pdftotext `-layout` 均为 97,374B、`-raw` 均为 43,825B；归一化文本逐字相同；词多重集相同（4,876 词）；PyMuPDF 逐页词数相同 [396, 381, 292, 364, 292, 361, 540, 1898] |
| P8 最小字号 | 印刷 + 网页均为 **9.98pt** |
| 徽章/P8 芯片 | 135 枚 = 核心；P8 A2 11 / B1 24 / B2 3 = 核心 |
| U+2019 | 8 页 SVG `<text>` + text.md + ABSTRACT.txt **总数 0** |
| §1.1 | 纸色 `#fbfaf6` ×8；金色 0（raw 命中均为图片 base64 内串）；VOL.5 仅合法下期预告 1 处 |

## KIT 交叉核对

- KIT 全部 SHA/字节数与我方实测一致；门禁数值（occlusion 0、p8 150/150、CLEAN、freeze 0、P8 9.98pt、芯片、
  U+2019 0、P7 teaser 2588.78、P8 keys 2552.7、P4 C-head 339.0、P7 三头 371.9/345.3/318.5）逐项复现一致。
- **KIT “Visual — zero defects” 与事实不符**：P1/P2/P5 三处盒标题越边未被 KIT 提及；
  P2 标题的 KIT 量值只对照片边、不对盒边。
- KIT 逐页词数（386/366/282/358/285/352/532/1879）与我方 PyMuPDF 原生词数（396/381/292/364/292/361/540/1898）
  绝对值不同（计数口径不同），但印/网逐页相等这一结论两种口径一致，不计问题。

## 观察项（单独列，不计缺陷）

- **O-1**：P1/P4/P6 等版中部留白较大（栏流提前结束），与核心 flow ends 一致，属继承版式，非 fan-out 引入。
- **O-2**：Q150 印刷键为 “✓” 而 REG 键为 “(开放题，范文如下)”——开放写作题的设计表达（栏头已说明），不计缺陷。
- **O-3**：任务所指 `hidden_files/w47/briefs/brief-coordinator.md` 在 weekly-git 内不存在；
  实际位置为 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`，
  FANOUT-REPORT 与各版 EDITION-RECORD 同在该 goals 路径下；已按实际位置读取，无内容影响。
- **O-4**：P2 标题的“末字 a”式越边（D-02/D-03）在 110dpi 整版图上不易察觉，须 150dpi 裁切或像素扫描才定论——
  这正是任务要求“PIL 真墨 + 交付 PDF 渲染像素双重验证”的原因；两法一致才定案。

## 未做事项（明示）

- 未重跑 `render.py` / 全量 `webpdf.py`（会重写成品 PDF；SVG 层重建 + 文字层比对已覆盖该门；
  网 PDF SHA 不可重现，只比文字层）。
- 未检查核心版 core-zh-cn 自身的全部校对记录；D4/D5 的核心同源性仅核对了相关源码行与 text.md 行。
- 未改 `tools/occlusion_audit.py`（BOXTITLE 盲区须工具线修；本次只复校）。
