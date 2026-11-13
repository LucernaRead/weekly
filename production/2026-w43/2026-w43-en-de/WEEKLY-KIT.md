# The Lucerna · ENGLISH WEEKLY VOL.1 — DEUTSCHE AUSGABE (EN × DE)

**配对 / Pairing: Englischer Text · Deutsche Erklärungen — 英语正文 + 德语讲解版**
读者对象：以德语为母语的英语学习者。内容与核心版（英语正文 + 中文讲解，`files/weekly-report-en-vol1/`，已定稿投递）完全相同：同一期（2026-10-19 → 10-25，W43）、同样的 149 道练习、同样的图片与署名；仅讲解层（注释、语法、指令、说明、诊所、图表注、全部答案简析）改写为德语，配对在版面明确标注。

## 一、交付物

- `svg/` — 8 版 SVG 源（1950×2700）
- `cards/` — 8 张整版 PNG（1950 宽）
- `The-Lucerna-VOL1-DE.pdf` — 完整版 PDF（8 版，8,623,563 字节）
- `The-Lucerna-VOL1-DE-web.pdf` — 压缩版 PDF（4,394,567 字节 < 10 MB，可直接投递）
- D5 重建（2026-11-13，见十一节）：印 `The-Lucerna-VOL1-en-de.pdf` **7,500,351 字节**
  （SHA-256 `fa012bcb406c23c749ab34f65b17381686405346fdb1f015a94c69ed8d77f37c`）；网
  `2026-w43-en-de.web.pdf` **1,069,759 字节**（SHA-256
  `b0c18a07aba2cd5df11a586607121369baac1820508f713f3e1bd3840d182fe3`，< 7 MB）；
  text.md 与已发版字节一致（SHA-256 `eb6a1179cdf3621a06746c2b74b56cb04a0e5a997200775b09221a12487380db`）。
  D5 前值：印 8,623,563 字节、网 1,114,484 字节（`e086bc0c…`，issues 已发版）。
- 构建源码：`hidden_files/weekly-report-en-de-build/`（核心版源码的副本上改写，核心目录未动）

## 二、配对标注（SOP 配对标准）

- 第 1 版刊头副行（粗体橄榄色）：**ENGLISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER**
- 第 1 版刊头主行：ENGLISCHES WOCHENBLATT · VOL.1 · SPORT · WAHLEN · KÜRBISSE；刊名 The Lucerna 不变
- 每版页脚：左 "The Lucerna · ENGLISH WEEKLY VOL.1 · Englischer Text · Deutsche Erklärungen"，右 "Seite N von 8"

## 三、数字（实测）

- 练习总数 **149**，与核心版逐题一致；分级 **A2 58 · B1 72 · B2 19**；分页 10/17/18/18/18/18/12/38 —— 与核心版登记表逐项相同
- 可见文字量 49,526 字符（8 版 `<text>` 内容实测合计；核心版 41,362——德语讲解与全量简析更长）
- 构建零警告（无 FLOW OVERFLOW）；第 8 版答案最低基线 2529.3，距页脚线（2580）**50.7px** ≥ 40px 要求

## 四、冻结校验（核心版对照）

- **登记表 diff**：149 题逐题比对核心版——等级、分页全同；**答案键仅 3 处不同**，全部为登记在案的改向/登记行（见 §五）；其余 146 题键与核心版逐字节相同
- **SVG 文字 diff**（8 版逐版）：全部差异均为讲解层（中文→德语）、页脚/刊头家具、§五条目；英文正文、题干、选项、引用例句零改动（仅个别因讲解行长变化引起的换行点移动，文字本身不变）
- **印刷答案核验**：第 8 版下半页答案区以程序重组全文，148 题印刷键与登记表逐字吻合（0 不符）；第 149 题（开放写作）印刷完整含简析
- **图片**：4 张图片与核心版逐字节相同（MD5 比对），署名行不变（Bain News Service / Library of Congress；Social Security Administration；Halloween postcard, 1912；United States Capitol——均为 public domain）
- **CJK 扫描**：成品 SVG 中 CJK 字符 = 0；禁用中间语/桥接表述全版（含源码注释）零出现
- **金句回查**：第 7 版 8 句金句逐字回查原文版面（第 2/4/6 版），页码标注全对
- **事实一致**：NBA 揭幕 10 月 20 日（周二）、World Series 10 月 23 日（周五）开打、F1 奥斯汀、众议院 218–214、图表四数 34/27/23/16（和 =100；34+27=61、27+16=43、34−16=18 复算无误）

## 五、翻译题改向（仅此 4 题的题面/键变化，SOP 允许）

第 8 版 §E Übersetzung 共 4 题，改为对德语读者双向练习（核心版 §E 为英译中/中译英）：

| 题 | 题面（德版） | 键（德版） | 说明 |
|---|---|---|---|
| 136 | 英译德：Translate : « Voting is no longer a day ; it is a season. » | **Das Wählen ist nicht länger ein Tag; es ist eine Jahreszeit.** | 键由核心版的中文译文改为德文译文 |
| 137 | 德译英：Übersetze: Die 76ers siegten 106 zu 100. | The 76ers won the game 106–100. | 题面改为德语（核心版为中文题面）；键（英文）不变 |
| 138 | 德译英：Übersetze: Die vorzeitige Stimmabgabe begann dieses Jahr am Montag. | This year, early voting opened on Monday. | 同上 |
| 139 | 英译德：Translate : « Neither club has ever won the Series. » | **Keiner der beiden Klubs hat je die World Series gewonnen.** | 键由核心版的中文译文改为德文译文 |

第 149 题登记行（开放题说明）属讲解层，德文化："Offene Aufgabe — Stichpunkte im Schreibkasten; Mustertext im Kasten auf Seite 8"，简析 "Bewertung nach Stichpunkten"。

## 六、讲解层德语标准

- 全部简析印刷（149 题每题一条德语简析，括号前空格，半角括号）——为此答案字号 15.5 → 13.5、答案流底界 2545 → 2530（最低基线实测 2529.3，见 §三）
- 德语数字惯例：小数逗号（3,6 %、0,45 kg、3,8 Mrd.），千分点（7.889），引号 „…"
- 术语与核心版一一对应：ballot = Stimmzettel、early voting = vorzeitige Stimmabgabe、COLA 说明、midterms = Zwischenwahlen 等
- 第 6 版文章末注释框为容纳德语长度删去 incumbent 一词（该词在同版边栏词表与第 8 版 §F 简析中均有德语注释，不缺失）

## 七、版式适配（仅几何，内容不变）

德语讲解更长，本版做了以下版式回收（均不改变英文内容与题目）：
1. 第 2 版 AND YOU 框德语提示压至 2 行（"Hot Dog im Kühlschrank? Geld im Monat? Schreib zwei englische Sätze!"），框底回到核心版同高 1534.6，与报时栏金线（1558）间距与核心版相同
2. 第 2 版练习流：3 条导语压至 1 行、4 个栏目标题与练习间距收紧、B 组字号 24 → 22
3. 第 6 版文章注释框：内边距 18 → 14（内容见 §六）
4. 第 6 版图表诚实声明：核心版为单行（英文+中文），德语版过长会撞第 2 栏 READING 栏目标尺——改为双行段落（全文不变：英文原文 + 德语全译），图表框上移配合（框顶 +20、高 −20，框底与核心版相同）
5. 第 8 版评估卷：§E 第 137 题德语题面压至 1 行（"siegten"），栏目与练习间距收紧；评估卷末端 1426 ≤ 底界 1485（核心版 1418）

## 八、几何遮挡审计（SOP 附则，强制门）

四项全查（实字宽 PIL 实测，含描边矩形边缘线与下行部墨带）：
(a) 后绘不透明图形覆盖文字 ≥30% —— 0
(b) 正文侵入页脚带（2580）—— 0（最大字形底 2555，第 2 版）
(c) 文字越出页框（25..1925）—— 0
(d) 后绘细线/描边穿过文字墨带 —— 0
**审计结果：8 版 0 标记。** 审计灵敏度已验证：升级墨带（基线 +0.28em 含下行部）后，旧第 6 版声明行与栏目线的相撞可被检出（相交 548 px²），修复版为 0。

构建方全量自校另含：8 版成图逐版目检；构建中曾发现并修复的问题——第 2 版练习流溢出、第 6 版文章流溢出、第 8 版评估卷尾段被范文框遮挡（首版）、第 8 版答案溢出页脚（首版）、第 6 版声明行撞线（成图目检发现，审计升级后纳入自动门）。

## 九、VOL.2 承诺（沿核心版，必须兑现）

- 第 3 版读者来信预告：最佳来信刊于 VOL.2 第 7 版读者园地
- 第 7 版读者园地：VOL.2 起刊登真实读者来信，并点评本期第 8 版写作投稿
- 第 7 版 VOL.2 预告（德语行）：周六万圣节之夜直播、周日全美拨钟多睡一小时、11 月 3 日周二选举日

## 十、复现

```bash
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-en-de-build
/tmp/wp-venv/bin/python -c "import content12, content34, content56, content7, content8"   # 顺序不可变，登记表按导入顺序累积编号；生成 8 个 SVG 到 files/weekly-report-en-de/svg
/tmp/wp-venv/bin/python - <<'EOF'
import cairosvg, glob, os
from pypdf import PdfWriter
from PIL import Image
base = os.path.expanduser('~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-en-de')
w = PdfWriter()
for f in sorted(glob.glob(base + '/svg/*.svg')):
    cairosvg.svg2png(url=f, write_to=f.replace('/svg/', '/cards/').replace('.svg', '.png'), output_width=1950)
    cairosvg.svg2pdf(url=f, write_to='/tmp/enpage.pdf'); w.append('/tmp/enpage.pdf')
w.write(open(base + '/The-Lucerna-VOL1-DE.pdf', 'wb'))
imgs = [Image.open(f).convert('RGB') for f in sorted(glob.glob(base + '/cards/*.png'))]
for im in imgs: im.thumbnail((1400, 1938))
imgs[0].save(base + '/The-Lucerna-VOL1-DE-web.pdf', save_all=True, append_images=imgs[1:], quality=85)
EOF
```

字体：Noto Serif/Sans CJK（/usr/share/fonts/opentype/noto），刊头 UnifrakturMaguntia。渲染禁用 /opt/meta-chromium（挂死）。
注意：**切勿单独 import 任一 content 模块重生成单版**——登记表按导入顺序累积，单版重跑会使该版题号错位（本版制作中曾因此重跑全量构建并复验）。

---
构建方自校完成（全量：核心 diff、登记表 diff、印刷键核验、CJK=0、金句回查、几何遮挡审计 0 标记、8 版目检）。待独立复校。

---

## 独立复校记录（2026-10-21，独立校对员）

**结论：整轮全量复校零问题，无修改、无重渲染。EN × DE 版定稿。**

复核方法与实测（不采信构建方自报，全部独立重测）：

- **可复现性**：两版构建源码在临时目录重跑，16 个成品 SVG（核心版 8 + 本版 8）与交付文件逐字节相同——核心版未被触碰，本版成品与源码一致。
- **登记表独立重导出**：149 题；分页 10/17/18/18/18/18/12/38；分级 A2 58 · B1 72 · B2 19；页/级逐题与核心版全同。**键仅 #136、#139、#149 三处不同**（与 §五登记一致）；#137/#138 键（英文）逐字节不变、题面已改德语且语法正确（„Die 76ers siegten 106 zu 100." / „Die vorzeitige Stimmabgabe begann dieses Jahr am Montag."）；#136 德译 „Das Wählen ist nicht länger ein Tag; es ist eine Jahreszeit." 正确；#139 „Keiner der beiden Klubs hat je die World Series gewonnen." 正确。
- **源码全量 diff 分类**（两版构建逐行比对，含 bslib4/svglib）：每一处差异均属讲解层（中文→德语）、双语家具、§五条目或 §七版式参数；**P6 五段英文正文逐字节相同**（仅 gap 参数变化）。bslib4 仅页脚行与注框前缀不同；svglib 仅注释文字不同。
- **P8 印刷完整性**：成品 P8 中 149 题「题号 + 键」逐条检出、149 条德语简析逐条检出，无一缺失；分组头 — Seite 1 — … — Seite 8 — 齐全；键字号 13.5pt（114 个文本元），括号全半角且前有空格（代码与成品双验）；全版全角括号 = 0。
- **CJK = 0**（成品 SVG 全量扫描）；禁用表述零出现。
- **几何遮挡审计（独立重跑，含下行部墨带 baseline −0.88em…+0.30em，生产字体 PIL 实测）**：(a) 后绘覆盖 ≥30% = 0；(c) 出页框 = 0；(d) 后绘细线/描边穿墨带 = 0；(b) 页脚带仅页脚家具自身（基线 2624，设计如此），正文最低墨底逐版实测：P1 2486.2 · P2 2555.4 · P3 2532.3 · P4 2542.5 · P5 2539.5 · P6 2499.1 · P7 2454.0 · P8 2533.3，全部距页脚线（2580）有净空（构建方「最大字形底 2555」复测吻合）。(e) 文本互叠 1 标记：第 1 版刊头字标与版次行墨带相交——裁图裁定**非缺陷**：两行间有清晰净空，与冻结核心版同坐标同字号（黑体字标无下行部，统一墨带公式对其高估）。
- **专项复测**：P8 答案最低基线逐栏 2529.3 / 2524.1 / 2517.8 / 2264.7（构建方 2529.3 吻合），墨底距页脚线 46.7px；P2 AND YOU 框底 1534.6，与核心版矩形逐值相同；P6 正文末行墨底 1397.2，距图表标题墨顶 63.9px（流光标 1418 ≤ 1420 与构建方一致）；P6 图表声明两行完整渲染（英文原文逐字 + 德语全译 „Übungsdaten: vereinfacht und erfunden, keine echte Umfrage."），第二行墨底 1543.6，图表框顶 1552，净空 8.4px、无穿线；图表框顶 +20 / 高 −20 / 框底与核心版同为 1888；四根柱宽 374/297/253/176 = 11px/百分点（34/27/23/16），与核心版逐值相同；和值 34+27=61、27+16=43、34−16=18、Σ=100 复算无误。
- **图片**：4 张内嵌图载荷 MD5 与核心版逐张相同，署名行不变。
- **第 1 版配对徽标**：y=372、19.5pt 粗体橄榄色，与被替换的核心版标语行同位；第 1 版逐行集合差比对完毕——核心版独有行只有中文讲解与该标语行，无其他英文内容消失。
- **P6 incumbent**：确从文末注框删去（§六已登记）；同版边栏词表 „an incumbent — Amtsinhaber"、第 96 题题干语境、P8 §F 配对 „incumbent = Amtsinhaber" 与其简析三处均有德语注释，不缺失。
- **金句回查**：第 7 版 8 句逐句回查标注版面原文（第 2/4/6 版），页码标注全对；其中 6 句为原文整句摘录并以句号收尾（与核心版同一体例，金句字符串与核心版逐字节相同），1 句（„Voting is no longer a day ; it is a season."）为逐字全句。
- **事实与星期**：日历复验 2026-10-19 周一、10-20 周二（NBA 揭幕）、10-23 周五（World Series G1）、10-24 周六（佛州强制期）、10-31 周六（万圣节）、11-1 周日（美国拨钟）、11-3 周二（选举日）——报内星期说法全对；218–214 与正文一致。
- **逐题复解**：按版逐节对原文/题干复解全部 149 题（含 P8 评估卷 38 题、图表读数、配对字母 P2 b/d/c/a · P4 d/b/a/c · P8 F b/c/d/a 与核心版一致），键全部正确；全部德语简析逐条读毕——语法、格、习语无误，数字体例统一（3,6 % · 7.889 · 0,45 kg · 13,5 Mrd.）。
- **VOL.2 承诺**：读者园地说明与第 7 版预告均已译德随版（真实来信 + 点评本期写作；万圣节夜 / 拨钟 / 11 月 3 日选举日），与 §九一致。
- **PDF**：两份均 8 版；字节数与 §一登记一致（8,623,563 / 4,394,567），web 版 < 10 MB。

记录在案的两点说明（非缺陷，不改版）：

1. **可见字符数口径差**：KIT §三记 49,526（核心版 41,362）；复校按成品 SVG `<text>` 解码实测为 **49,519**（核心版 41,358），差 7 / 4 字（0.014%）——系构建方按源码字符串计、复校按渲染文本计的口径差；经源码 diff 与登记表完整性双验，无任何词句缺失。
2. **家具条目微调未逐条登记**：第 3 版 A/B 头与第 5 版 B/D 头为德语单语（如 „A · WAHR ODER FALSCH ?"），第 6 版边栏框题 „HEADLINE LANGUAGE" 改为 „HEADLINE TALK · Schlagzeilen"——均为讲解层家具，不涉正文、题干、选项、键。

## 十一、D5 重建记录（2026-11-13，D5-only）

SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader（SemiBold）。
施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：
`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-de/`；
逐版报告：`production/notes/2026-w43/g-en/scratch-d5-rebuild-en/D5-REPORT-2026-w43-en-de.md`。

**装机**：core 落盘 `apply_variant.py --patch-core en --week 2026-w43`（core-en
`svglib.py` +95/−3 行，`_D5_READER = "latin"`）；本版 `--svglib patched/…/svglib.py
--target en --reader de --week 2026-w43`，装后 `_D5_READER = "latin"`（装后 svglib
md5 与 de/it/nl/pt 四版全同）；路由单元测试 FAILURES: 0（66 PASS）；fix2 块保留。

**基线**（修前生产版）：run TOTAL 149，0 警告；印 PDF 与 `MANIFEST-W43-D1.md`
逐字节一致；印/网文字层差 0；自建网 vs issues 已发 web 非空字符差 0（仅空格差）；
修前普查 D5 拉丁 592、西里尔 0、弯引号在 CJK 1；基线 P8 noted 149/149。

**缺陷与修法**（run1 共 11 项，全为 D5 字体加宽引起，另 P2 spill 为既有缺陷——基线
同值；修法只动字号，未动文字）：

- head ×6：P4 `D　VERB FORMS　Vergangenheit` 25→24；P5 `EARNINGS, IN PLAIN ENGLISH`
  26→25；P5 `C　THIS WEEK, LIVE　-ing-Form` 25→24；P6 `READING THE CHART　Diagramm`
  24→23；P7 `THE TOOLBOX　Werkzeugkiste` 27→25；P7 `THE ERROR CLINIC　Fehlerklinik`
  25→24（栏宽 422.5）。
- occlusion ×1（P1）：暗带标题与副标 `EUROPA STELLT UM` 重叠 **145.2×20.8px**（全家
  最大——德语副标 27pt 宽 295.7px，左缘 x=1559.3；46pt 标题右缘 1681.3，44pt 仍重叠
  54px）→ 暗带标题 46→**42** + 副标 27→**25**。
- creambox/boxtitle ×2：P4 `THE WEEK'S FIXTURES　Spielplan` +13.7px → 加 `tsize=22`；
  P5 `WORDS OF THE SCREEN　Wortliste` +22.9px → 加 `tsize=21`（22pt 仍超约 4px）。
- spill ×1：P2 `Check your number !` 跌出 DID YOU KNOW 框底 12.71px → 框高公式尾数
  +14→+34（框底 +20px；与 core-en 同款既有缺陷）。

P8：225→216 行，距页脚线余量 34.9→46.7 px。

**门禁 run2（全套 17 门 ALL-GREEN）**：run TOTAL 149、0 警告；head_check 0；
d5 census 0/0/0；render RC=0；webpdf RC=0（1,069,759 B < 7 MB）；occlusion 0 flags；
p8 extract noted 149/149；p8 compare **EXTRA_ONLY**（extra_count=87，裁定接受；
keydiff=[136, 139, 149]，与本 KIT 记载的读者语答案键一致）；freeze baseline 8/8；
freeze diff 新增 CJK 字符 0；spill 0；boxtitle 0 DEFECT（55 titles）；edge 0/0；
creambox PASS 0 defects；文字层 print=web 差 0（各 112,735 字符）；census_quotes
0 defective；en 家无 gates.py。

**新交付物**：印 `The-Lucerna-VOL1-en-de.pdf` 7,500,351 字节（`fa012bcb…`）；
网 `2026-w43-en-de.web.pdf` 1,069,759 字节（`b0c18a07…`）；text.md 字节一致
（`eb6a1179…`）。练习仍为 149 题，§三/§四未变。
