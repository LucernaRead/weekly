# PROOF-NOTE — 2026-W47 it-ko 独立复校（proof2，全量重校）

**结论：(a) 零缺陷，可定稿。满轮全量校对零问题；下列 9 项为观察项，不计缺陷。**

- 版：`2026-w47-it-ko`（目标语 Italiano × 读者母语 한국어，VOL.4；重扩散新版，核心 it 已定稿）
- 复校员：proof2（独立于 re-fanout 与 proof1，从头全量，不引用 proof1 结论）
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-ko1/`
- 日期：2026-11-11（America/Toronto）
- 生产文件：未改任何生产文件，未 commit、未 push；KIT K6/K7 未碰。

## 1. 开工盘核（三 SHA 与任务值逐字节一致）

| 文件 | 大小 (B) | SHA-256（盘上实测） | 任务值 |
|---|---|---|---|
| 印 PDF `La-Lucerna-VOL4-KO.pdf` | 19,296,912 | `d5698327bbb331d0270e5ca86c531068fe8425f0ff11251747fc4ddd9768b7a3` | 一致 |
| 网 PDF `La-Lucerna-VOL4-KO-web.pdf` | 1,607,490 | `85722a84c68bb1e03b2bde56462d23ffc0855405ae4e4911d71e04adc819086e` | 一致 |
| `2026-w47-it-ko.text.md` | 57,347 | `e9dbe37172028913924567df9445604a4bd79584fe910de4c487662b8ab45614` | 一致 |

开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 真实写文件通过。TMPDIR 全程指向 scratch 下 `tmp/`，未写系统 /tmp。校对结束后三 SHA 复核仍为上值（生产未动）。

## 2. 门禁汇总（全部独立重跑，19/19 通过；详见 GATE-LOG.md）

| 门禁 | 实测 |
|---|---|
| run.py（scratch 副本，OUT 重定向） | RC=0，TOTAL 150，A2 47 / B1 70 / B2 33，页 10/18/18/18/18/18/12/38，模型文 99 词；0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE |
| SVG 重建 vs 生产 | 8/8 逐字节一致 |
| 印 PDF 重渲 vs 交付 | 逐字节相同，SHA `d5698327…` |
| 网 PDF 重建 | RC=0，46,953 文字字节；与交付差 5 字节（见观察 O6，文字层逐页相同） |
| freeze baseline（核心 it） | 8/8 逐字节一致；build-copy 核实确为核心版（与 core-it 仅 OUT 行不同，md5 与 KIT §11 一致：content8 `629b5b0a…`、content12 `91cdfbb9…`、content34 `18926942…`；核心 SVG 跑前后未变） |
| freeze diff（核心 → 本版） | P1–P7 0 未解释片段；P8 由 p8 compare + 150 键审计覆盖 |
| occlusion 几何遮挡审计 | 0 flags |
| p8 extract | noted 150/150 |
| p8 compare vs 核心 | CLEAN，keydiff `[137, 138, 139]`（与 it 家预期一致，见 §5） |
| 印/网文字层逐页比对 | 词多重集 8 页全同（7,414 词）；位置比对（PyMuPDF 词框，0.1pt 取整）P2–P8 0 差异；P1 仅刊头 “La Lucerna” 两词 x 差 0.4–0.5pt（见观察 O7） |
| P8 最小字号 | SVG 最小 13.0px；印 PDF 实测最小 9.75pt（737 spans），= SOP §1.1 下限 |
| §1.1 干净 | 纸 `#fbfaf6` 有；无金/红褐/近黑；VOL.4 ×9；VOL.5 仅 3 处合法节点（下周预告头、LETTERE 披露、P2 交叉引用，与核心同）；徽章色 A2/B1/B2 齐全；双线外框 0 个；字体 Newsreader / Noto Serif CJK KR / Noto Sans CJK KR / UnifrakturMaguntia |
| creambox（canonical，md5 `ee7a55d8…`） | 全部负 clearance 均为假阳性（见 §4）；9 处 desc-clear 负值全部经交付 PDF 像素实测澄清，末行真墨距盒底 +3.72~+5.58px，无一越盒底 |
| 横向溢出 PIL 真墨扫描 | 2,217 节点，3 处 +0.4~+0.5px 旗标，全部经交付 PDF 像素实测澄清（见 §4） |
| text.md 校验 | forward-miss 0 / reverse-miss 0 |
| 150 键审计 vs 核心 text.md | 150/150，键一致（137–139 重定向、写作题除外）；notes 与 translations.py 一致（137–140 + 写作题除外）；9 条无表 notes 为冻结意大利语动词变位（16–20、60–61）与算术（85–86），逐字节照搬、无 CJK |
| 150 题三源逐题手验（登记 REG vs text.md 正文键 vs Risposte vs P8 印出键） | 150/150，0 差异（脚本 `threeway.py`；含键、note、级别、页码） |
| 8 金句 | 每句在本版与核心中各恰好出现 2 次（正文 + P7），逐字一致（见 §5） |
| 日期/星期（`date -d`，Europe/Rome） | 20 个日期全验：11月16日周一…11月22日周日、11月23日周一、11月24日周二、12月2日周三、12月6日周日、12月31日周四、10月15日周四、10月28日周三、11月9日周一、11月12日周四、11月6–8日周五–周日、11月13–14日周五–周六，全部与正文星期表述一致 |
| 算术 | 13−11=2（Q85）、6+7=13（Q86）、托罗内 29届 11月7–22日=16天·3个周末、TFF 11月24日–12月2日=9天、BookCity 数字 1,360/2,487/1,164/443 与 Q70/73/80 一致，全部复算通过 |
| 全文通读（text.md 1,317 行）+ 8 页逐页目视交付印 PDF | 无拼写/语法/截断/事实错误；无溢出、重叠、压页脚、豆腐块；韩语讲解层无他语残留（SVG 汉字/假名扫描 0 命中；`·` 151 处全部在选项串或术语表内，见 §5） |
| ABSTRACT.txt | 一行韩语，无 ASCII 双引号 |

## 3. 缺陷

**无（0 项）。**

## 4. 盒边与页边裁决（全部以交付 PDF 渲染像素为准，200 dpi，SCALE=2.0833）

### 4.1 奶油盒 desc-clear 负值（9 处）——全部澄清，非缺陷

canonical creambox 报 9 处 desc-clear 为负（−1.0~−1.5px，0.30em 保守系数），末行真墨逐盒像素实测（盒内 x 范围、末行基线至盒底+8px 窗口）：

| 盒 | 末行 | 盒底 | 末行真墨底 | 余量 |
|---|---|---|---|---|
| P2 LO SAPEVI? | della musica e dei musicisti. | 960.6 | 955.20 | +5.40 |
| P2 E TU? | 에 보내세요. | 1350.6 | 1346.40 | +4.20 |
| P3 IL WEEKEND DOLCE | continua fino al 6 dicembre. | 1021.1 | 1015.68 | +5.42 |
| P3 E TU? | 문장을 써서 보내세요. | 1290.6 | 1286.88 | +3.72 |
| P4 E TU? | 아어로 두 문장을 써서 보내세요. | 1140.4 | 1136.64 | +3.76 |
| P5 I GIOVANI IN NUMERI | domenica 22 novembre. | 1010.7 | 1005.12 | +5.58 |
| P5 E TU? | 장을 써서 보내세요. | 1249.8 | 1246.08 | +3.72 |
| P7 LA PAROLA | 치오가 29점으로 선두. | 1344.0 | 1340.16 | +3.84 |
| P7 LETTERE | 습니다. 약속은 VOL.5로 이어집니다. | 1673.0 | 1668.48 | +4.52 |

（单位：SVG px；真墨阈值灰度<200。）负 desc-clear 只是 0.30em 系数对无下行字母行（韩语无下行笔，意大利末行 “della musica e dei musicisti.” / “continua fino al 6 dicembre.” / “domenica 22 novembre.” 均无 p/q/g/y/j 下行字形）的保守高估；真墨全部留在盒内。P7 工具盒汇总：3 盒，最小盒内 clearance +4.5，最小 desc-clear −1.5（上表 LA PAROLA，真墨余量 +3.84）。

其余 creambox 负 clearance 全部是 +45px 窗口的假阳性，inside-only 行自证清白：P1 三处（ADESSO TU +37.0、LA PAROLA DELLA SETTIMANA +24.0、QUIZ LAMPO 说明 +44.0，均为盒下块标题）、P3 一处（IL TORRAZZO +37.0，下块标题）、P4 三处（斑马表素行，见 §5）、P6 两处（ESERCIZI 6면 연습 +42.0，下块标题）。各盒 inside-only clearance 均为正（+4.5~+90.0）。

### 4.2 横向页边（3 处 PIL 旗标 + 全页像素扫描）

- PIL 旗标 3 处（+0.4~+0.5px）：P1 “SETTIMANA DAL 16 AL 22 NOVEMBRE 2026”、P1 QUIZ LAMPO 说明、P8 “각 정답에 한국어 한 줄 설명 ✓ = 모범 답안 과제”。行级像素实测（行带窗口，不伸进 gutter）：真墨右缘分别为 1860.96（−1.04）、1855.68（−6.32）、1851.84（−10.16），全部在 1862 页边内——PIL advance 与渲染真墨之差，非溢出。
- 全页像素扫描：P1/P3/P4/P6/P7 最右真墨 1861.44（−0.56）；P2、P5 各有 8/6 行真墨越过 1862，均为 +0.40px、0 个实色像素（灰度<100 为 0，最浅 104），即抗锯齿毛边，非实墨（P2：副标 “Una festa, una giornata verde” 行顶；P5：Corot 图注行）。最左真墨 87.36px 系 x=88 处 band 矩形/照片/徽章边缘的抗锯齿（P1 聚类核实：y 470–588 为 band 矩形，y 1876–2194 为照片左缘，y 2367–2394 为 A2 徽章，其余为 x=88 文本字形毛边），非文本溢出。
- **P8 模型文两行（“VUL DE KRONIEK IN” 类）独立行级实测**：‘Testo modello: Domenica 22 novembre metto la sciarpa e’（基线 631.33）与 ‘vado a Cremona: è l’ultimo giorno della Festa del Torrone’（基线 652.13）真墨右缘均为 1863.36，即越过 1862 内容边 **+1.36 SVG px（= 1.02pt ≈ 0.36mm）**，越边像素 18/21 个、其中实色（<100）12/13 个，最深灰度 45——是实墨，非毛边。但：① 两行字符串、x、字号与冻结核心逐字相同（PIL 真墨 1861.50/1860.50，边内）；② 核心印 PDF 第 8 页同位置渲染出**逐像素相同的结果**（+1.36px、18/21 越边像素、12/13 实色像素），即该行为冻结核心固有、且核心已通过零问题复校；③ 越边处为空白纸面，无裁切、无重叠、无碰撞，肉眼不可辨（边线本身不印刷）。故记**观察 O2，不计缺陷**。裁图：`out/crops/p8-model-right-edge.png`。

## 5. 其他核实

- **keydiff**：实测 `[137, 138, 139]`，p8 compare  verdict CLEAN，与 it 家预期一致。Q140 的键在核心与本版都是意大利语（“Ogni cifra deve essere chiara.”，韩→意翻译题），无差异是正确行为，不是遗漏。Q137–139 为 E 节重定向的读者句键（韩语句），符合 KIT §9。
- **标题数（实测，不用 “56 titles”）**：定义 = 字号 ≥26.5 SVG px（≈19.9pt）的非空标题文本节点，按（页，基线）合并同行多 run、band 行左右分列标题分计。**标题项 43**（P1 7、P2 7、P3 6、P4 6、P5 6、P6 6、P7 3、P8 2）；同口径另计：原始节点 48、不同基线 35。三个口径均不复现 “56”——该数为幻数。
- **P4 斑马表**：10 场结果分 5 行，cream/none 交替（VEN 6.11 奶油、SAB 7.11 素行、SAB 7.11 奶油、DOM 8.11 素行、DOM 8.11 奶油），日标签每行重复。核心 P4 同区 21/21 行位置与冻结文本逐一相同——为核心冻结设计，非本版缺陷，渲染观感为规整斑马表。裁图：`out/crops/p4-table.png`。
- **P5 词表**：第二行以 ‘·’ 开头（“· indipendente · lettrice”），与 KIT §10 披露一致，核心同断点模式；视觉无重叠。
- **P1 无首字下沉、P3/P5 中段留白**：均为核心既有格局（KIT §10 已披露），本版与核心一致。
- **Q32 引号**：P8 答案 32. “Fate dolci” 用直引号，而正文（P3）与题干用 «Fate dolci»——translations.py ko 原值逐字如此，与 nl 版同源（KIT §10 已披露）。内容正确，仅引号样式与他版不同。裁图：`out/crops/p8-key32-quotes.png`。
- **意大利语事实抽查**（核心冻结内容，复核一致）：Madonna della Salute 1630 年许愿、圣殿 1631–1687 年 Longhena 设计、植树节 1898 年起源/2013 年立法、Torrone 1441 年 10 月 25 日 Sforza–Visconti 婚礼、Eurochocolate 第 32 届、TFF 第 44 届（1982 创办，2026 年为第 44 届）、BookCity 第 15 届、Colson Whitehead 两届普利策、Sinner 为 2025 年 ATP 总决赛冠军；“Gattuso 执教 Lazio / Zverev 世界第一”为本期设定前提，核心已定稿。总分榜 29/28/27/24/23/5 与 10 场比分（24 球）自洽：那不勒斯–拉齐奥 1–1、国际–科莫 2–0、罗马–萨索洛 3–0 的比分在头条、P4 正文、积分榜、结果表、Q2/3/4/48/60/61 中六处一致。
- **禁词扫描**：Ucraina/Russia/Putin 0 命中（正文+讲解层；继承核心）。

## 6. 观察项（不计缺陷，共 9 项）

| # | 位置 | 现象（源码行 + 实测值 + 证据） | 判定理由 |
|---|---|---|---|
| O1 | P5 IL PIANO DELLA SETTIMANA 第 2、3 条（content56.py 词条；SVG p5 y≈611/751） | 韩语括注收尾 “)” 独占一行：第 2 条 “(토요일: 베네치아 성모 건강 축일” 后 “)” 独行；第 3 条同类（“(일요일: 필름메이커 영화제 폐막” 后 “)” 独行）。盒内，无溢出、无重叠。裁图 `out/crops/p5-il-piano-dangle.png` | 换行 artifact，与 KIT 已接受的 ‘·’ 行首同类；可读，无硬门违规 |
| O2 | P8 模型文第 1–2 行（content8.py 模型文；p8 y 631.33/652.13） | 真墨右缘 1863.36，越 1862 边 +1.36px（1.02pt），实墨 12/13 像素；与核心渲染逐像素相同（§4.2） | 冻结核心固有行为，空白纸面，无裁切/重叠 |
| O3 | P2 副标行（y 1594）、P5 图注行（y 602.95） | 真墨右缘 1862.40（+0.40px），越边像素 8/6 个、实色 0 个、最浅灰度 104 | 抗锯齿毛边，非实墨 |
| O4 | P8 答案 32（content8.py 键表；p8 y 2394.8） | note 用 “Fate dolci” 直引号，正文/题干用 «Fate dolci»；translations.py ko 原值，与 nl 版同 | 内容正确；KIT §10 已披露 |
| O5 | P5 底部词表（content56.py；p5 y≈1885） | 第二行以 ‘·’ 开头 | KIT §10 已披露，核心同断点 |
| O6 | 网 PDF 重建 | 重建 1,607,485 B vs 交付 1,607,490 B（差 5 B）；首个差异字节在 obj 20 字体子集流内（/Length1 3096），多处子集流解压后等长但字节不同，仅 /Length 数字 ±2；逐页文字、分词、字体名、元数据全同 | fontTools 子集化跨进程非字节稳定；非内容差异 |
| O7 | 印/网 P1 刊头 | “La/ Lucerna” 两词 x 差 0.4–0.5pt（印 404.8/599.5 vs 网 404.3/599.1），其余 7 页词框 0 差异 | 子集字体重测；0.5pt 不可见 |
| O8 | P4 结果表 | SAB 7.11、DOM 8.11 日标签各出现两次（每行自带） | 核心冻结设计，21/21 行与核心相同 |
| O9 | P1 / P3 / P5 | P1 头条无首字下沉；P3 第二栏、P5 第三栏中段留白（P3-main col1 止于 y≈1249、P5 col1 止于 y≈1217 量级，核心同） | 核心既有格局，KIT §10 已披露 |

## 7. 方法与证据文件

- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-ko1/`
- `logs/run.log`（run.py RC=0，TOTAL 150）、`logs/render.log`（印 PDF 逐字节同）、`logs/webpdf.log`（网 PDF 重建）、`logs/freeze-baseline.log`（8/8）、`logs/gates-ko.log`（19 门全过）、`logs/h-overflow.log`（2,217 节点，3 旗标）、`logs/creambox.log`（canonical 工具全版扫描）、`logs/pixel-check.log`（交付 PDF 像素：9 盒 + 全页边）、`logs/rowlevel.log`（P2/P5/P8 行级真墨实测）、`logs/threeway.log`（150 题三源 0 差异）、`logs/dump_reg.log`（REG 导出）
- `ko/p8-extract.json`（150/150）、`ko/p8-compare.json`（CLEAN，[137,138,139]）、`ko/freeze-diff.json`（0 未解释片段）
- `out/reg.json`（REG 150 条）、`out/crops/`（P5 括注、P8 模型文右缘、P8 键 32 引号、P5 词表、P4 斑马表）
- `rebuild/`（重建用源码副本 + 重建 SVG 8/8 + 重建印/网 PDF）、`freeze-baseline/build-copy/`（核心版复现副本，仅 OUT 行不同）、`pages/`（交付印 PDF 200 dpi 渲染 8 页 + 核心 P8 对照页）
- 工具链：repo `tools/venv/bin/python`（Pillow 13.0.0；it-ko 为 it 家，用 venv 栈）；共享工具 `tools/freeze.py`、`tools/p8.py`、`tools/occlusion_audit.py`、`tools/webpdf.py`；奶油盒 canonical `hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`）；横向溢出与逐题核对脚本为本 scratch 自写（`h-overflow-proof2.py` 适配 KR 字体、`threeway.py`、`pixel-check.py`、`rowlevel.py`）。
