# W47 fr 家庭独立重校记录（第二轮，SOP §8.4）

- 校对员：独立重校（第二轮），与建造者、第一轮校对员、修复工人均不同；只校对、不修复、不重建、不 commit、不 push、不跑 lint。
- 日期：2026-11-12（EST）。范围：目标语 fr × 读者母语 en de es it ja ko nl pt ru zh-cn zh-tw，共 11 版（core-fr = fr-zh-cn 版 + 10 个 fan-out）。
- 依据：`~/workspace/weekly-git/SOP.md` §8 + §1.1；第一轮 `scratch-reproof-w47-fr/PROOF-NOTE.md`（16 项）；修复记录 `scratch-fix-fr/FIX-LOG.md`（全文已读）。
- 目录核对：fan-out 10 个（`2026-w47-fr-de/en/es/it/ja/ko/nl/pt/ru/zh-tw`）+ `core-fr/` = 11 版，无多无少。无 `2026-w47-fr-zh-cn` fan-out 目录（与第一轮一致）。

## 结论：(b) 有问题 —— 3 项，全部 low，无 MAJOR、无 MEDIUM、无事实错误、无 P8 答案错误、无版式破损

第一轮 16 项已全部修复到位（见下节逐项核实）。本轮全量重校新发现 3 项 low：

### R2-1（low，4 版）—— P7 文法点题头 `se terminer en beauté` 被截为 `en beauté`

- 位置：P7「LES PHRASES DE LA SEMAINE」文法点行（text.md 约 L900，Q100 上方）。
- 内容：ja、ko、nl、ru 四版的文法点题头只写 `en beauté`，丢了动词部分 `se terminer`；其余 6 版 + core 均为完整 `se terminer en beauté`。
- 证据原文（text.md）：
  - ja：`*文法 | en beauté：美しく締めくくる。*`；ko：`*문법 | en beauté: 아름답게 마무리하다.*`；nl：`*Grammatica | en beauté: mooi eindigen.*`；ru：`*Грамматика | en beauté: красивый финал.*`
  - 对照 de：`*Grammatik | se terminer en beauté: schön enden.*`；en：`*Grammar | se terminer en beauté: to end in style.*`；es：`*Gramática | se terminer en beauté: terminar muy bien.*`；it：`*Grammatica | se terminer en beauté: finire in bellezza.*`；pt：`*Gramática | se terminer en beauté: terminar em beleza.*`；zh-tw：`*文法｜se terminer en beauté：圓滿收尾。*`；core 同 zh-tw。
- 严重度 low：四版释义本身都正确（“美しく締めくくる / 아름답게 마무리하다 / mooi eindigen / красивый финал”均为“圆满收尾”之意），Q100 答案 `beauté` 及其简析（四版内同样用 `en beauté` 题头）自洽，不影响做题与改题；仅为跨版题头不一致，读者看到的仍是同一短语的正确释义。P7 渲染图目视确认四版该行均干净无溢出。
- 注：P7 工具箱（BOÎTE À OUTILS）引用的完整例句 `« La semaine se termine en beauté … »` 在四版均完整无缺，丢的只是文法点题头的动词部分。

### R2-2（low，1 版）—— fr-nl P4 NOTE `un vainqueur` 丢了 `een`

- 位置：P4 译注行（text.md P4 NOTE）。
- 内容：nl P4 NOTE 为 `un vainqueur winnaar`；同版 P1 NOTE 为 `un vainqueur een winnaar`，其余拉丁版 P4 NOTE 均带冠词（en `a winner`、de `ein Sieger`、es `un ganador`、it `un vincitore`、pt `um vencedor`）。
- 严重度 low：与第一轮 D2（zh-tw 丢 `une`）同类，仅为译注冠词缺失，词义无误。

### R2-3（low，1 版）—— fr-zh-tw P8 答案 93 简析 `les députés` 译作「眾議員」

- 位置：P8 答案区，93. `ont rejeté（眾議員否決收入部分）`。
- 内容：core（zh-cn）为 `93. ont rejeté（议员否决收入部分）`；zh-tw 用「眾議員」指法国国民议会议员。台湾用法中「眾議員」通常指美国众议院议员，法国 députés 一般作「議員 / 國民議會議員」；但国民议会确为法国议会下院，以「眾議員」指下院议员并非错译，只是表述不够贴切。
- 严重度 low：答案键 `ont rejeté` 本身正确，简析词义可懂，不影响做题。

### 逐版缺陷计数（本轮新发现）

| 版 | 缺陷 | 编号 |
|---|---|---|
| fr-zh-cn（core-fr） | 0 | — |
| fr-en | 0 | — |
| fr-de | 0 | — |
| fr-es | 0 | — |
| fr-it | 0 | — |
| fr-ja | 1 | R2-1 |
| fr-ko | 1 | R2-1 |
| fr-nl | 2 | R2-1、R2-2 |
| fr-pt | 0 | — |
| fr-ru | 1 | R2-1 |
| fr-zh-tw | 1 | R2-3 |
| **合计** | **3 项 / 6 版次** | 全 low |

## 第一轮 16 项修复逐项核实（全部在版）

逐项在 text.md 与印 PDF 文字层中 grep 核实，并对关键页渲染目视（`/tmp/reproof2-fr/`，临时件）：

| # | 版 | 位置 | 核实结果 |
|---|---|---|---|
| D1 | fr-ja | P1 NOTE `un vin primeur 新酒` | text.md L45、印 PDF 文字层均有；渲染 P1 目视 NOTE 行含 `primeur 新酒`，排版干净 |
| D2 | fr-zh-tw | P2 `une virgule 逗號` | text.md L229、印 PDF 均有；渲染 P2 目视确认 |
| D3-1 | fr-es | P7 `CLINIQUE DES ERREURS　ERRORES` | text.md L921、印 PDF 均有；渲染 P7 目视 |
| D3-2 | fr-it | P7 `…　ERRORI` | 同上 |
| D3-3 | fr-ja | P7 `…　誤り` | 同上 |
| D3-4 | fr-ko | P7 `…　오류` | 同上 |
| D3-5 | fr-nl | P7 `…　FOUTEN` | 同上 |
| D3-6 | fr-pt | P7 `…　ERROS` | 同上 |
| D3-7 | fr-ru | P7 `…　ОШИБКИ` | 同上 |
| D3-8 | fr-zh-tw | P7 `…　易錯診所` | 同上 |
| D3-9 | fr-nl | P5 `LE CINÉMA DU MERCREDI　FILMS` | text.md L655、印 PDF 均有 |
| D3-10 | fr-ru | P5 `…　КИНО` | 同上 |
| D3-11 | fr-ru | P6 `LIRE LE CALENDRIER　КАЛЕНДАРЬ` | text.md L723、印 PDF 均有 |
| D3-12 | fr-nl | P7 `BOÎTE À OUTILS　GEREEDSCHAP` | text.md L855、印 PDF 均有；渲染 P7 目视无溢出（fix2 版） |
| D3-13 | fr-ru | P7 `BOÎTE À OUTILS　ИНСТРУМЕНТЫ` | 同上（fix2 版） |
| D3-14 | fr-ru | P1 `DANS CE NUMÉRO　СОДЕРЖАНИЕ` | text.md L109、印 PDF 均有；渲染 P1 目视在页内无溢出 |

**D1 专项（孤儿日文句号 。）**：ja P1 NOTE 补回「新酒」后重排，SVG 核查：`p1-une.svg` 中 `新酒　` 元素（y=1336.93）后接 `レー。`（y=1366.65），句号附在 `ボジョレー` 词尾，非独行；全 ja 版 SVG 无任何独立 `。` 文本元素（grep `>。 <` 零命中）。**孤儿句号未再现。**另核实：11 版 P1 NOTE 的 `primeur` 译注全部在位（逐版 sed L45 均为 1 处）。

## 校对文件清单（本次校对的文件；尺寸 + SHA-256 前 12）

与 FIX-LOG §2 的修后值逐项比对，**全部一致**（未改动的 en/de/core 亦与第一轮一致）：

| 版 | 印 PDF（8 页） | 网 PDF | text.md |
|---|---|---|---|
| fr-zh-cn（core-fr） | `La-Lucerna-VOL4.pdf` 18,475,436 `f36c32f020e4` | 1,985,431 `ff08e74903d6` | 46,471 `52024e024d32` |
| fr-en | `La-Lucerna-VOL4-fr-en.pdf` 17,031,641 `0503cff0885d` | 1,622,982 `11e5babac345` | 46,146 `82f53a7aa6af` |
| fr-de | `La-Lucerna-VOL4-fr-de.pdf` 17,035,304 `234a877ebbbb` | 1,626,645 `68c62c41b596` | 46,559 `de37011a23a0` |
| fr-es | `La-Lucerna-VOL4-fr-es.pdf` 17,031,455 `57d86cd14c5a` | 1,622,809 `0f89bcd285da` | 46,655 `d348eda26a40` |
| fr-it | `La-Lucerna-VOL4-fr-it.pdf` 17,027,797 `179461e905ff` | 1,619,126 `be09601e1dcf` | 46,537 `0ca8ff5439bf` |
| fr-ja | `La-Lucerna-VOL4-fr-ja.pdf` 20,149,418 `3121d66228dd` | 2,019,912 `8c52331f7ce6` | 47,524 `354f6b094247` |
| fr-ko | `La-Lucerna-VOL4-fr-ko.pdf` 20,086,243 `bfeb8970f59f` | 1,923,201 `d972b7cbc104` | 47,332 `fd2dfe488c05` |
| fr-nl | `La-Lucerna-VOL4-fr-nl.pdf` 17,030,024 `45c0b11e87a7` | 1,621,399 `fb98be3aa292` | 46,281 `ad506a852519` |
| fr-pt | `La-Lucerna-VOL4-fr-pt.pdf` 17,031,948 `4a76ddaca94d` | 1,623,288 `302da684a631` | 46,494 `c7a3f3244476` |
| fr-ru | `La-Lucerna-VOL4-fr-ru.pdf` 17,332,080 `038ee398d117` | 1,882,292 `f0e9d27b3934` | 50,513 `3b6f2cf61934` |
| fr-zh-tw | `La-Lucerna-VOL4-fr-zh-tw.pdf` 18,532,970 `3f4f58df81c3` | 2,076,083 `6972666e0e72` | 46,011 `e257f1023046` |

- 印 PDF 均为 8 页（pdfinfo 核实）。ABSTRACT.txt 11 版齐全，均为读者母语、单行、无 ASCII 双引号（尺寸与第一轮一致：de 231B、en 198B、es 233B、it 210B、ja 245B、ko 250B、nl 207B、pt 233B、ru 365B、zh-tw 203B、core-fr 280B）。
- 练习总数 150（与第一轮一致）。

## 机械门（全部通过；只读门禁，未重建）

在盘上现成文件上跑（未跑 run.py/render.py/webpdf.py，不动生产文件；日志见 `gates/`）：

| 门 | 结果（11 版） |
|---|---|
| `tools/p8.py compare --core-dir core-fr --edition-dir <版> --target fr --total 150` | 10 个 fan-out 版全部 **CLEAN，121/121 noted，missing=[]，extra_count=0**，keydiff=[150]（Q150 开放题读者语标签差异，已知非失败，与第一轮一致） |
| `tools/occlusion_audit.py` | 11 版 **0 flags**，自检通过（6 类植入全触发） |
| `tools/boxtitle_check.py` | 11 版 **0 DEFECT，0 OBSERVE，0 marginal**（core 40 / de 34 / en 34 / es 38 / it 38 / ja 41 / ko 47 / nl 38 / pt 36 / ru 43 / zh-tw 40 titles） |
| `tools/spill_sweep.py` | 11 版 **0 SPILL**（OBSERVE 仅为 P7 框下 VOL.5 预告框的 below-box 提示，非缺陷） |
| `tools/pdf_edge_scan.py` | 11 版 **0 TOUCH / 0 NEAR**（8 页） |
| D5 census（`scratch-d5-plan/mechanism/d5_census.py`） | 11 版 **PASS**：拉丁入 CJK=0、西里尔入 CJK=0、弯引号入 CJK=0、弯引号总数=0 |
| 引号普查（text.md + 印 PDF 文字层） | U+201C/U+201D/U+2019/U+2018 均为 **0**；法语用 « »（148 处，ru 160 处——俄文讲解层亦用 « »，一致）；直引号 `"` 为 0；法语省音撇 `'` 为正常法文字符 |
| P8 答案编号连续性（印 PDF 提取文本） | 11 版 **1–150 全有，missing=[]** |
| 网 PDF vs 印 PDF 提取文本 | 11 版**逐字节一致（同一 MD5）** |
| P8 字号（PyMuPDF 实测） | 11 版 P8 最小字号均为 **11.62pt ≥ SOP 目标 9.75pt** |
| 核心法语层一致性 | core 的 882 行非 CJK 行在 10 个 fan-out 版 text.md 中**逐字相同、零缺失**；各版均为 1087 行，与 core 行数一致 |
| 文字污染核查（text.md） | 拉丁版 0 CJK/0 西里尔/0 假名/0 谚文；ja 仅 CJK+假名；ko 仅谚文（0 CJK）；ru 仅西里尔；zh-tw 仅 CJK |
| KIT 抽查 | ja KIT 的印/网/text.md 字节+SHA 与盘上实测一致（含 FIX-LOG §7 所称更新） |

- 注：ru 版 census `noto_sans_elements=1010`——即任务指明的已知跨家 D5 系统性问题（拉丁标题用了 Noto Sans 而非 Newsreader），**按任务要求不重报**，另有跨家工人统一修 svglib.py；census 本身 PASS（拉丁入 CJK=0）。
- 注：es/it/nl clinic 标题伸入空白边距（445.2/423.4/432.6px）为 FIX-LOG §8 已接受项，**不重报**；本轮渲染目视三版 P7 均无碰撞。

## 全量通读（text.md + 印 PDF 全文）

- core-fr text.md 全文 1087 行逐行通读（P1–P8）：内容事实、日期星期、引文、答案逐题复核，未发现新问题；与第一轮已核实的事实清单一致（ATP 都灵 11 月 15–22 日、法国队 11 月 12 日意大利/15 日波尔多、社保预算 115–1 与 458–0、博若莱 75 周年与 22% 减产、SERD 11 月 21–29 日、11 月 18 日六部新片等）；core SHA 未变，内容与第一轮所校相同，未重复跑浏览器事实核查。
- 10 个 fan-out 版：逐版做 core 对齐 diff（`work/md-diff2-fr-<版>.txt`），法语核心行逐字相同；讲解层 205 行/版（zh-tw 176 行，其余与 core 同形字行相同）**逐版全文通读**（`work/expl2-fr-<版>.txt`），包括全部译注、词表、题干说明、E 节翻译源句、P8 答案简析。未发现翻译错误、术语不一致或答案错误（除上列 3 项 low）。
- P8 答案逐题复核：150 题答案键与 core 一致（跨版答案 token 比对仅 1 处正则伪报——de 版括号内日期，经核实答案键相同）；Q105–108 诊所纠错、Q109–150 综合评估答案均与题面/原文一致。
- text.md 与 PDF 一致性抽查：16 项修复全部在印 PDF 文字层在位；P1/P7/P8 关键页渲染目视 15 页（ja P1/P7、nl P7、ru P1/P7、es/it/ko/pt/zh-tw P7、zh-tw P2、core P8、en P8、de P1），无溢出、无重叠、无压页脚、无截断句、无豆腐块。

## 已排除的疑点（查过、不列为缺陷）

- es/it/pt `LIRE LE CALENDRIER` 译注为 `HORARIO` / `ORARIO` / `HORÁRIO`：三版共用同一译法；该栏为日期日程表，horario/orario（时刻表/日程）可作其译注，非错误。
- ru 135. `Смотреть финал: учить французский.`：第一轮已记为风格松紧，非缺陷。
- ja L397 `une bouteille — 瓶` 与 core 逐字相同：瓶为合法日文汉字，非中文残留（第一轮已裁定）；zh-tw 与 core 相同的行均为繁简同形字，属预期内。
- 第一轮两项“核查未定论”（“seize films”16 部计数口径、50 天期限 11 月 26 日计数起点）维持原结论，非缺陷，不重报。
- 第一轮已排除项（zh-tw/core P1 标题栏 1.1pt bbox 重叠实为字间距吸收、de `SENAT STIMMT MI.` 缩写、P8 Hiroshige 配文、范文风格等）均维持，不重报。
- FIX-LOG 末节（§8）已裁定接受的项（es/it/nl clinic 栏外伸入空白边距）不重报；*-ru 版拉丁标题字体问题不重报（见上）。

## 工作文件

- 本记录：`hidden_files/w47/scratch-reproof2-w47-fr/PROOF-NOTE-2.md`。
- 工作目录 `hidden_files/w47/scratch-reproof2-w47-fr/`：`work/`（各版印/网 PDF 提取文本、`md-diff2-fr-<版>.txt`、讲解层全文 `expl2-fr-<版>.txt`）；`gates/`（`summary.log` + 逐版 occlusion/boxtitle/spill/edge/census/p8 日志与 JSON）。
- 渲染图在 `/tmp/reproof2-fr/`（临时，VM 重启即失；可从印 PDF 用 venv PyMuPDF 重渲）。
- 磁盘：收尾时 /home/hatch 95G/150G（63%），未触 100G 门限。

## 未做事项

- 未修复任何问题（只记录）；未重建、未 commit、未 push、未跑 lint、未碰其他周次、其他家庭；未改动 `production/2026-w47/` 内任何文件（fr 版目录在 clone 中本就为 untracked，状态未变）。
