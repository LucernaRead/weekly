# PROOF-NOTE-3 — W47 fr 家庭第三轮独立重校

- **日期**：2026-11-12（EST）
- **校对员**：第三轮独立重校员（与建造者、第一轮校对员、第一轮修复者、第二轮校对员、第二轮修复者均不同）
- **范围**：target fr × reader natives en de es it ja ko nl pt ru zh-cn zh-tw，共 11 版。`core-fr/`（= fr-zh-cn）+ fan-out `2026-w47-fr-{de,en,es,it,ja,ko,nl,pt,ru,zh-tw}/`
- **依据**：SOP §8/§8.4 proofread-until-zero；PROOF-NOTE-2（R2-1/R2-2/R2-3）；FIX-LOG-2；FIX-LOG（第一轮 16 项）
- **方式**：只校对、不修复、不重建、不 commit、不 push、不跑 lint。门禁只读跑盘上文件。工具解释器一律 `tools/venv/bin/python`。
- **工作目录**：`hidden_files/w47/scratch-reproof3-w47-fr/`（`work/` 提取与 diff，`gates/` 门禁日志，`run_gates3.sh` 门禁脚本）

## 总体结论：(a) 干净 —— 零问题轮次

**发现 0 项：MAJOR 0、MEDIUM 0、low 0。**

- core-fr text.md 1087 行全文通读；10 版讲解层 diff 逐行读完（de/en/es/it/nl/pt/ru 各 205 行差异、ja 203 行、zh-tw 176 行）；P8 答案 1–150 逐题复核；日期/星期、算术、引文逐字核对；ABSTRACT 11 版齐全。
- R2-1/R2-2/R2-3 三项修复均在版（text.md + 印 PDF 文字层 + 渲染目视三重核实）。
- 第一轮 16 项（D1–D3-14）全部仍在版；D1 孤儿句号未再现。
- 机械门禁 11 版全绿（见 §5）。

## 1. 文件指纹（尺寸 + SHA-256 前 12 位）

与 FIX-LOG-2（5 版新值）及 PROOF-NOTE-2（6 版未变值）逐版一致，全部匹配。

| 版 | 印 PDF（B） | 印 SHA | 网 PDF（B） | 网 SHA | text.md（B） | text SHA |
|---|---|---|---|---|---|---|
| core-fr | 18,475,436 | `f36c32f020e4` | 1,985,431 | `ff08e74903d6` | 46,471 | `52024e024d32` |
| fr-de | 17,035,304 | `234a877ebbbb` | 1,626,645 | `68c62c41b596` | 46,559 | `de37011a23a0` |
| fr-en | 17,031,641 | `0503cff0885d` | 1,622,982 | `11e5babac345` | 46,146 | `82f53a7aa6af` |
| fr-es | 17,031,455 | `57d86cd14c5a` | 1,622,809 | `0f89bcd285da` | 46,655 | `d348eda26a40` |
| fr-it | 17,027,797 | `179461e905ff` | 1,619,126 | `be09601e1dcf` | 46,537 | `0ca8ff5439bf` |
| fr-ja | 20,149,490 | `f3f9d526f158` | 2,019,995 | `a1951960b852` | 47,548 | `d243033462d4` |
| fr-ko | 20,086,280 | `acb99672c246` | 1,923,242 | `f7341f1a0a4f` | 47,356 | `4929e183f280` |
| fr-nl | 17,030,093 | `c7e99156a889` | 1,621,462 | `d846793366f5` | 46,309 | `a5f5c7ebbfc8` |
| fr-pt | 17,031,948 | `4a76ddaca94d` | 1,623,288 | `302da684a631` | 46,494 | `c7a3f3244476` |
| fr-ru | 17,332,158 | `387991e60727` | 1,882,380 | `5fdfbf439848` | 50,537 | `1985e95d9be2` |
| fr-zh-tw | 18,532,749 | `e6ef33ce2f62` | 2,075,855 | `0d6b19e48c69` | 46,008 | `3dc051e14be0` |

印/网 PDF 均为 8 页（PyMuPDF 核查：core、ja、nl、ru、zh-tw 8 页；FIX-LOG-2 §2 载明 10 版重渲文件均为 8 页）。

## 2. R2 修复核实（全部在版）

### R2-1 — ja/ko/nl/ru P7 文法点题头 `en beauté` → `se terminer en beauté`

- text.md L893：四版题头均为完整 `se terminer en beauté`。
  - ja：`文法 | se terminer en beauté：美しく締めくくる。`
  - ko：`문법 | se terminer en beauté: 아름답게 마무리하다.`
  - nl：`Grammatica | se terminer en beauté: mooi eindigen.`
  - ru：`Грамматика | se terminer en beauté: красивый финал.`
- text.md L1079 答案 100 简析：ja/ko 全角括号、nl/ru 半角括号，均为 `(se terminer en beauté = …)`；core/zh-tw 用无 `=` 体例（`se terminer en beauté 圆满收尾` / `圓滿收尾`），与同行相邻答案体例一致。
- 印 PDF 文字层：四版各含 `se terminer en beauté` 2 处（P7 题头 + P8 答案 100），旧形 `(en beauté` / `（en beauté` 各 0 处。
- 渲染目视（110 dpi，P7 整页）：四版题头均完整折为 2 行，栏内正常折行，无溢出、无截断、无碰撞；Q100 位置不受影响。
- 全家旧形普查：`（en beauté =` 0 处、`(en beauté =` 0 处。

### R2-2 — nl P4 NOTE `un vainqueur winnaar` → `un vainqueur een winnaar`

- text.md L465：`un vainqueur een winnaar`，与同版 P1 NOTE（L45）一致。
- 印 PDF 文字层：P4 处完整出现；P1 处因 `pdftotext -layout` 换行拆散为两行（`…le Sénat de Senaat un` / `vainqueur een winnaar trancher`），文字本身在位，非缺失。旧形 `un vainqueur winnaar` 0 处。

### R2-3 — zh-tw P8-93 `眾議員` → `議員`

- text.md L1075：`93. ont rejeté（議員否決收入部分）`；答案键 `ont rejeté` 不动。
- 印 PDF 文字层：`議員否決收入部分` 在位；`眾議員` 全家 0 处（text.md 与印 PDF 文字层均查）。
- 渲染目视（zh-tw P8 整页）：答案区完整，`93. ont rejeté（議員否決收入部分）` 清晰在版，无溢出。

### D1 孤儿句号未再现

- ja 版 SVG 无独立 `。` 文本元素（`grep '>。<'` 0 命中）。
- ja P1 渲染目视：NOTE 行 `un vin primeur 新酒 le beaujolais ボジョレー。`——句号附在词尾，无孤儿句号。

## 3. 全量重校覆盖

- **core-fr text.md 1087 行全文通读**（P1–P8）：日期/星期逐一对 2026 日历核实（Europe/Paris：11-08 周日、11-09 周一、11-12 周四、11-15 周日、11-16 周一、11-17 周二、11-18 周三、11-19 周四、11-20 周五、11-21 周六、11-22 周日、11-04 周三、10-23 周五、11-26 周四、12-09 周三、11-27 周五、11-03 周二）；11 月第三个周四 = 19 日 ✓；1951→2026 = 75 周年 ✓；比分/票数/日期内部一致（Alcaraz 7-6(5) 7-5、115–1、458–0 + 2 票弃权、22% 削减、16 部影片 / 6 部具名、50 天期限至 26 日、Q22–25/49–52/73–76/85–88/140–144 配对、Q105–108 诊所改错、Q109–150 答案逐题对照题干）。无错误。
- **10 版讲解层 diff 逐行读完**（`work/expl3-*.txt`，CORE vs 各版行对）：
  - de/en/es/it/nl/pt/ru：各 205 行差异，410 行对；ja：203 行差异，406 行对；zh-tw：176 行差异，352 行对。
  - core 法语行在 10 版 fan-out 中逐字节一致；仅讲解层行有差异。
  - ja 有 2 行与 core 完全相同，均为日文汉字同形所致，非缺陷：L319 `## CULTURE　文化`、L397 `une bouteille — 瓶`（瓶为合法日文汉字，第二轮已裁定）。
  - 其余接受项（与第二轮一致，不重报）：各版头条缩写（de `SENAT STIMMT MI.`、en `SENATE VOTES WED`、es `SENADO VOTA MIÉRC.`、it `SENATO VOTA MERC.`、nl `SENAAT STEMT WO.`、ru `ГОЛОСУЕТ В СР.`）；ru L135 `Смотреть финал: учить французский.` 风格宽松；ru L141 `vainqueur = чемпион` 与 NOTE `победитель` 用词不一。
- **第一轮 16 项（D1–D3-14）全部仍在版**：通读中逐项核对（D1 primeur 新酒、D2 une virgule、D3 诊所题头、D3-9/10/11/12/13/14 各行均在位）。
- **ABSTRACT**：11 版齐全，尺寸与第二轮一致（core 280B、de 231、en 198、es 233、it 210、ja 245、ko 250、nl 207、pt 233、ru 365、zh-tw 203），每版 ASCII 双引号 0 个。

## 4. 逐版结论

| 版 | 结论 | 备注 |
|---|---|---|
| core-fr | 干净 | 全文通读无发现；门禁全绿 |
| fr-de | 干净 | 讲解层 205 行读完无发现；门禁全绿 |
| fr-en | 干净 | 同上 |
| fr-es | 干净 | 同上 |
| fr-it | 干净 | 同上 |
| fr-ja | 干净 | R2-1 在版；P7 渲染目视干净；门禁全绿 |
| fr-ko | 干净 | R2-1 在版；P7 渲染目视干净；门禁全绿 |
| fr-nl | 干净 | R2-1/R2-2 在版；P7 渲染目视干净；门禁全绿 |
| fr-pt | 干净 | 讲解层 205 行读完无发现；门禁全绿 |
| fr-ru | 干净 | R2-1 在版；P7 渲染目视干净；门禁全绿 |
| fr-zh-tw | 干净 | R2-3 在版；P8 渲染目视干净；门禁全绿 |

## 5. 机械门禁结果（只读跑盘上文件，`gates/summary.log`）

| 版 | occlusion | boxtitle | spill | edge | D5 census | p8 compare |
|---|---|---|---|---|---|---|
| core-fr | 0 flags, selftest OK | 40 titles, 0 DEFECT / 0 OBSERVE / 0 marginal | 0 SPILL (33 boxes, 102 cand.) | 8 pp, 0 TOUCH / 0 NEAR | PASS (noto_sans 0) | —（core 本身） |
| fr-de | 0 flags | 34 titles, 0/0/0 | 0 SPILL (102) | 0/0 | PASS (0) | CLEAN 121/121, keydiff=[150] |
| fr-en | 0 flags | 34 titles, 0/0/0 | 0 SPILL (102) | 0/0 | PASS (0) | CLEAN 121/121, keydiff=[150] |
| fr-es | 0 flags | 38 titles, 0/0/0 | 0 SPILL (100) | 0/0 | PASS (0) | CLEAN 121/121, keydiff=[150] |
| fr-it | 0 flags | 38 titles, 0/0/0 | 0 SPILL (107) | 0/0 | PASS (0) | CLEAN 121/121, keydiff=[150] |
| fr-ja | 0 flags | 41 titles, 0/0/0 | 0 SPILL (104) | 0/0 | PASS (0) | CLEAN 121/121, keydiff=[150] |
| fr-ko | 0 flags | 47 titles, 0/0/0 | 0 SPILL (136) | 0/0 | PASS (0) | CLEAN 121/121, keydiff=[150] |
| fr-nl | 0 flags | 38 titles, 0/0/0 | 0 SPILL (101) | 0/0 | PASS (0) | CLEAN 121/121, keydiff=[150] |
| fr-pt | 0 flags | 36 titles, 0/0/0 | 0 SPILL (103) | 0/0 | PASS (0) | CLEAN 121/121, keydiff=[150] |
| fr-ru | 0 flags | 43 titles, 0/0/0 | 0 SPILL (107) | 0/0 | PASS (noto_sans 1014，已知字体问题，见 §6) | CLEAN 121/121, keydiff=[150] |
| fr-zh-tw | 0 flags | 40 titles, 0/0/0 | 0 SPILL (104) | 0/0 | PASS (0) | CLEAN 121/121, keydiff=[150] |

- 全部命令 rc=0；keydiff=[150] 为已知 Q150 开放题读者语标签差异，非失败。
- 门禁脚本：`run_gates3.sh`（occlusion / boxtitle / spill / edge / D5 census / p8 compare，未跑 run/render/webpdf，未重建）。

## 6. 其他核查

- **印 = 网文字层**：11 版印/网 PDF 提取文字逐字节一致（`cmp` 通过）。
- **P8 答案 1–150**：印 PDF 文字层中 1–150 全部在位，missing=[]（11 版）。
- **P8 最小字号**：11 版均为 11.62pt ≥ SOP 目标 9.75pt。
- **引号普查**（text.md 与印 PDF 文字层）：U+201C/U+201D/U+2019/U+2018 与 ASCII `"` 均为 0；法语引号 « » 成对：每版 74/74，ru 80/80。
- **文字污染普查**（text.md）：拉丁 6 版无任何非拉丁文字；ja 仅 CJK 1220 + 假名 1292；ko 仅韩文 2369（CJK 0）；ru 仅西里尔 5259；zh-tw 仅 CJK 2005；core 仅 CJK 2090。均符合预期。
- **KIT 抽查**：ja/ko/nl/ru/zh-tw 五版 WEEKLY-KIT.md 均记录 R2 修复条目，SHA 与盘上指纹一致；ja/ko Visual QA rebuild #2 均为 "Zero problems"（ja 改页 P1/P4/P6/P8，ko 仅 P8，与重渲范围一致）。
- **渲染目视**：ja/ko/nl/ru P7、zh-tw P8、ja P1 整页（110 dpi，`/tmp/reproof3-fr/`，临时文件）均干净；ko P7 gp4 末尾句号独占折行行首（`.` 单独成行）为 FIX-LOG-2 §7 已记录观察项，非缺陷，本轮状态未变。

## 7. 不重报项（已裁定，见 FIX-LOG §8 / PROOF-NOTE-2）

- es/it/nl clinic 标题伸入空白边距（es 445.2px、it 423.4px、nl 432.6px）；nl P7-clinic HEAD TOO WIDE（已接受）。
- ru creambox 3 缺陷：r1 已裁定误报（P5 `debat5_note` 重匹配错误；本轮 spill_sweep 0 SPILL 佐证）。
- fr-ru 拉丁标题字体问题：已知跨家 D5 系统性问题，另有跨家工人统一修 svglib.py；本轮 census ru `noto_sans_elements=1014` 为同一已知问题，不另报。
- es/it/pt `LIRE LE CALENDRIER` gloss `HORARIO`/`ORARIO`/`HORÁRIO`；ru L135 风格宽松；ja L397 `瓶`；zh-tw 与 core 同形字预期一致；"seize films" 16 部计数依据、50 天期限至 11 月 26 日起算日（第一轮未决非缺陷）。

## 8. 发现表

无。发现 0 项。

## 9. 磁盘状态

- 开工时 /home/hatch 已用 95G/150G（63%）；收尾时复查 95G/150G（63%），未触及 100G 门限，全程未停手。
- 本轮新增文件仅限工作目录内小文本/日志（提取、diff、门禁日志）及 /tmp 临时渲染图（6 张 PNG，约 6MB），未写生产目录。
