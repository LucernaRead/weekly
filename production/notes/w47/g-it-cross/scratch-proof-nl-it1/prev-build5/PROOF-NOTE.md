# PROOF-NOTE — 2026-W47 · nl → it（意大利语读者版）· proof1 独立复校

- 复校员：独立复校（proof1）
- 日期：2026-11-11
- 版目录：`production/2026-w47/fanout-nl/2026-w47-nl-it/`
- 核心：`production/2026-w47/core-nl/`（slug `2026-w47-nl-zh-cn`，已冻结）

## §0 身份核对（磁盘为准）

| 文件 | 任务给定 SHA | 磁盘 SHA | 字节数 | 结果 |
|---|---|---|---|---|
| 印 PDF `De-Lucerna-VOL4-nl-it.pdf` | `a05cc4be4048cc23b357d9f0d35e03725ff68a80f082ecec46249ee42175ab3c` | 同左 | 12,715,556 | 一致 |
| 网 PDF `De-Lucerna-VOL4-nl-it-web.pdf` | `072c7f2e808ad6c93cd5469f981b14688432cab0fc8794a1260e3d5c58301fe9` | 同左 | 1,575,654 | 一致 |
| text.md `2026-w47-nl-it.text.md` | `7652632d685a400130b3da86a3f731b59badfe035424376cf32c269b884c85d4` | 同左 | 46,851 | 一致 |

三个 SHA 全部与任务一致；字节数与 KIT 一致。creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383` 与任务一致。
源文件未改动、未重建、未 commit、未 push。探针：`git hash-object -w` 正常；scratch 可写正常。
（注：复校期间仓库工作树另有与本版无关的 W43 已改文件，未触碰。）

## 结论：(b) 有缺陷，不能定稿

发现 **3 项缺陷：1 项 major + 2 项 minor**。150 题答案键全部手验通过（0 不一致），其余机械门全过。
三项缺陷均须修复后整版重渲染、再从头做一轮全量复校（SOP §8.4），方可定稿。

## 缺陷清单

### D1［major · 本版 · P7］HET WOORD 框标题横向溢出奶油盒 66px，贴近页右边缘

- **定位**：P7 右栏奶油盒（`x=1439.5, y=1059.0, w=422.5, h=282.0`，右缘 1862.0），
  框标题 `HET WOORD　PAROLA DELLA SETTIMANA`（Noto Sans CJK SC Bold 23pt，`x=1461.5, y=1101.0`）。
- **实测证据（三法一致）**：
  - PIL 真墨迹：`getbbox` 全串宽 466px，墨右缘 `1461.5 + 466 = 1927.5`，超框右缘 **+65.5px**；
  - 200dpi/110dpi 渲染像素扫描：最右侧墨点 SVG `x=1927.9`，超框右缘 **+65.9px**，距页边缘（1950）仅 22px；
  - 目视：P7 整版图上标题 `…DELLA SETTIMANA` 明显跑出奶油盒、落在新闻纸上，几乎贴到页边（见 `img/p7.png`、`img/crop-p7-hetwoord.png`）。
- **归属**：本版。核心同位置标题为 `HET WOORD　本周词`（短中文）， fits；溢出由意大利语 gloss
  `PAROLA DELLA SETTIMANA` 过长引入。KIT 的 12 项修复里没有这一处（修的是 P1 副标题、数字框、P6 表头、P2 框题、P1 agenda、P8 键、P6 右栏头），属漏检。
  同类前例：it-de D1、it-fr D1/D2/D3、it-nl D1–D3、pt-fr D1–D4、es-pt D1、pt-ru D1/D2、it-ru D2–D4。
- **修复建议**：缩短意大利语 gloss，如 `HET WOORD　PAROLA` 或 `HET WOORD　LA PAROLA`，
  按 PIL 真墨迹重测至墨右缘 ≤1862（留 ≥10px 余量），重渲染后复测。
  同页其余框标题已实测 fits：`PAS OP!　CLINICA DEGLI ERRORI` 墨右缘 478（框右 510.5，余 32px），
  `BRIEVEN VAN LEZERS` 墨右缘 1701.5（余 160px）。
- **附带工具缺口**：`tools/occlusion_audit.py` 本轮报 0 旗却漏掉 D1——其 BOXTITLE 类只覆盖
  带描边（stroke）或 `#2c2822` 填充的盒子（源码 471–473 行），奶油盒（`#f0eee5` 无描边）不在检查内；
  正典 creambox.py 只量纵向 clearance，不量框标题横向溢出。横向框标题溢出目前无工具覆盖，
  见未决 O4。

### D2［minor · 机制（webpdf.py）· P1 网 PDF］网 PDF 丢失全版唯一的斜体

- **定位**：P1 HET WOORD 框内本周词 `«de groepswinst»`。
- **实测证据**：
  - 印 PDF：该 span 为 `Newsreader16pt-Italic` 16.1pt（全版唯一斜体 span）；
  - 网 PDF：字体表里完全没有 Italic 字体（只有 `LucernaNewsreader-Regular` 各子集），
    该 span 字体为 `LucernaNewsreader-Regular` 16.12pt——斜体被打平成正体；
  - 文字层本身完好：印/网逐页 token 多重集差为 0、字节数逐页相等，`«de groepswinst»` 前后空格与
    闭引号均未丢失、未脱离——ru-en D3 三联症中仅「斜体丢失」一项复现，另两项未复现。
- **归属**：机制。印版正确，网版构建（`tools/webpdf.py` 字体裁切/改名）未收录斜体 face。
  同类前例：ru-en D3。
- **修复建议**：修 webpdf.py 使其收录当期用到的全部 face（含 Italic），重建网 PDF 后复验
  （网 PDF P1 应有 1 个 Italic span）。

### D3［minor · 本版 · P7 + P8］弯引号 U+2019 在 Noto Sans CJK SC 里渲染成全角空隙，像错字

- **定位**（2 处可见）：
  - P7 ZINNEN 翻译：`La festa di San Nicola è un’ antica festa olandese. (Pagina 6)`；
  - P8 头注：`Ogni risposta ha una breve nota in italiano　✓ indica l’ esercizio di scrittura`。
- **实测证据**：SVG 文本并无空格（`un’antica`、`l’esercizio` 的 ’ 前后均无 U+0020），
  但 4 倍放大渲染图上 ’ 后有一整格空隙，读作 `un’ antica` / `l’ esercizio`。
  对照：同一字体、同一版面的直引号 U+0027 渲染紧密——P6 通栏副标题 `Sinterklaas: un'antica festa, nuovi desideri`
  无空隙。另 2 处弯引号在 Newsreader 字体里（P8 注 126 `all’Eredivisie`、注 140 `un’espressione`），
  放大图显示紧密、无空隙。
  全版统计（`<text>` 内）：U+0027 共 39 处，U+2019 共 4 处（P7 ×1、P8 ×3）；同一词 `un'antica`
  在 P6（直引号）与 P7（弯引号）用了两种写法——版内意大利语层自相矛盾。
- **归属**：本版（意大利语讲解层混用两种省音撇号；Noto Sans CJK SC 的 U+2019 字形带全角空隙）。
- **修复建议**：把 4 处 U+2019 一律改回直引号 U+0027（与本版其余 39 处一致），
  重渲染后放大复验 P7 该行与 P8 头注无空隙。

## 必查项逐项核实（任务所列 a–f）

- (a) P1 框标题/副标题横向溢出：**P1 未复现**。PIL 真墨迹 + 渲染像素扫描：
  副标题 `SETTIMANALE OLANDESE VOL.4 ORANJE SINTERKLAAS PAKJESAVOND` fits；
  `DE WEEK IN CIJFERS　IN CIFRE`（框内末行 21.5px 余量）、`GLI APPUNTAMENTI`、`L'EDIZIONE`、
  P1 日期行 `WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026`（渲染墨右缘 1861.5，框内）均 fits。
  但**同类缺陷在 P7 复现**，即 D1。
- (b) P3/P5 右栏奶油盒末行降部漫出：**未复现**。真墨迹（baseline + 降部实测，下延 = bbox 底 − ascent）：
  P2 EN JIJ 末行 `olandese e mandale alla redazione.` 无降部字母，真余量 **+5.6px**；
  P5 EN JIJ 末行 `due frasi in olandese e mandale.` 无降部字母，真余量 **+5.7px**；
  P6 图表盒末行 `(100 giovani)` 含 `g` 降部，真余量 **+4.7px**；
  P2 四词盒 `po' ironica`（`p` 降部）真余量 +6.4px；P2 WIST JE DAT 末行 +7.3px；P6 `En jij?`（`j` 降部）+9.0px。
  creambox.py 的 desc-clear −0.4/−0.3 是 0.30em 一刀切余量的误报（那两行本无降部字母）。
- (c) P7 toolbox clearance：**实测通过**。正典 creambox.py 全版扫描：P7 三盒最小框内余量 +12.5px、
  最小降部余量 +6.5px（PAS OP! +20.4、HET WOORD +12.5、BRIEVEN +28.5）。
- (d) text.md 第 E 节 type 标签本地化：**通过**。E 节为 `Traduzione`／`Traduci in italiano`／
  `Traduci in olandese`；全版 type 标签均为意大利语（Completa la frase、Scelta multipla、Abbinamento、
  Vero o falso、Forma la frase、Cloze、Scrittura），无中文「翻譯」残留。
  （注：text.md 中 `— 答案：` ×150 是所有已发版共用的导出格式标记［W46 nl-it、nl-de 亦为 150 次］，
  非本版残留；见 GATE-LOG。）
- (e) 网 PDF 斜体三联症：**部分复现**，即 D2（斜体丢失；空格与闭引号完好）。
- (f) ABSTRACT.txt 刊名：**通过**。含 `Lucerna`、`VOL.4`、目标语 `olandese`、`150 esercizi`、
  `livelli A2–B2`；意大利语单行 278 字符，无 ASCII 双引号。

## 150 题手验摘要（详见 keycheck-150.json）

- 150/150 逐题手验：题面＋正文/图表/算术复算＋text.md 答案＋P8 印刷键三方比对，**0 不一致**。
- P8 印刷键集合 150/150，keydiff 仅 137/138（荷→意翻译重定向，已裁决非缺陷；139/140 与核心键一致）。
- 唯一键面差异：150 题为开放写作，P8 印 `✓`，范文 81 词已数（`81 parole`，与 KIT 一致）。
- 算术全对：22/45 题 19 天、43 题 1 天、44 题 4 小时、46 题 17 年、85 题 65、87 题 100（35+30+20+15）。
- 配对全对：P2 D（25–28）与 P8 F（141–144）的 a–d 选项内容已从 SVG 核对，字母映射正确。
- 外部事实抽查（核心事实，本版继承）全部核实：Grave 全国 intocht 2026-11-14 周六 12:00 Maaskade、
  市长 Marieke Moorman、Merel Westrik 主持；Amsterdam 15 日 88 届、De Omval 10:15、Scheepvaartmuseum 11:30、
  Stopera 13:00 巡游；PSV 26 分领跑（第 12 轮后，Cambuur–PSV 2–5、Heerenveen–Feyenoord 5–3、
  Twente–Ajax 2–2）；Expeditie Robinson 2026 共 19 人（10 荷＋9 弗拉芒）、Nicolette Kluijver 与 Edson da Graça 主持、
  Camille Vanuxem 记者、马来西亚、34 天、周日 20:00 RTL 4 自 11 月 1 日；11 月 24 日周二欧冠 Real Madrid–PSV、
  Feyenoord–Porto。来源见 GATE-LOG。
- 讲解层对照正文：注释词均真实出现在正文；P7 金句 8 条逐字出自本期文章（P1/P2/P3/P4/P5/P6），
  意大利语译文与原文对应、页码标注正确；P7 下期预告与 P8 范文一致。
- P8 实测最小字号 10.12pt（SOP §1.1 底线 9.75pt，目标 11.25pt——在让步第 4 步范围内，与 KIT 一致）。

## 全文通读未发现的其他问题

- 8 页逐版看图：除 D1 外无溢出、重叠、压页脚、图片压字；页脚/页码行正确（第 N 版／共 8 版）；
  P3/P6 中部留白与核心版式一致（短文章所致），非缺陷。
- 荷兰语拼写/变位/性数：通读无误；过去时/完成时（hebben/zijn）选择正确；
  `omdat` 从句动词居末正确；`kwartfinales` 复数、`kandidaten` 复数正确。
- 读者母语层：全部讲解/导读/图注/题干说明为意大利语；无他语导读残留；无内部标签/周次/语言代码
  进入正文版面（刊头、版名、页脚均为读者可见的正常内容）。
- 图片：6 图均有目标语图说＋出处（W. Punt/Anefo、Spaarnestad Photo/Wikimedia、Elise lovenko/Unsplash、
  Cristina Gottardi/Unsplash、Aaron Burden/Unsplash、Wim van Rossem/Anefo），与当周主题相关。

## 未决事项

- **O1**：text.md 首行标题含周次码 `# De Lucerna · Settimanale olandese VOL.4 · 2026-W47`。
  与冻结核心（同式）及已发 W46 nl-it（`2026-W46`）完全一致，属全版共用的导出模板格式，
  非本版可单改——需模板层决定，不计入本版缺陷。
- **O2**：P2 D 节选项 c `c. eten voor het paard van Sinterklaas` 渲染墨右缘 1872.9（超 1862 版心 10.9px）。
  该行与核心逐字节相同（同一 x、同一字体字号），属冻结核心的固有几何；无可见框线可越，
  目视仅为行尾参差的普通行——本版裁定非缺陷；如核心重排时可顺带收短。
- **O3**：`tools/freeze.py` 无 `freeze_direct` 子命令（仅 baseline/diff），按任务说明记为方法备注，
  非缺陷。freeze baseline 已实跑 8/8。
- **O4**：工具缺口——occlusion BOXTITLE 不覆盖无描边奶油盒；creambox.py 不量横向溢出。
  D1 同时漏过两道工具门。建议把「框标题墨右缘 vs 自身框右缘」补进共享工具（横向版），
  并复验 W47 其余已校版是否同类漏检（属父线/工具维护决定，本版不展开）。
