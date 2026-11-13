# PROOF-NOTE — 2026-W47 nl-en（英语读者 × 荷兰语目标）独立复校 第 2 棒（proof1，build 10）

- 对象：`production/2026-w47/2026-w47-nl-en/`（正典版，build 10，delta 已完）
- 校对员：第 2 棒（独立重跑；第 1 棒 scratch-proof-nl-en1/ 只作方法参考，未复用其输出作证据）
- 日期：2026-11-11（UTC 20:13–21:0x 开工；全部证据在本棒自有 scratch 重跑）
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-en2/`
- 文件名说明：本 scratch 内已有的 `PROOF-NOTE.md` / `GATE-LOG.md` 是更早一轮 build-8 proof2-en2 的交付物（结论 (a)），
  未覆盖；本轮 build-10 交付物另存为 `PROOF-NOTE-build10.md` / `GATE-LOG-build10.md`。
- 规则：只读生产，绝不改生产文件、不 commit、不 push；`PYTHONDONTWRITEBYTECODE=1` 全程；TMPDIR = 自有 scratch

## 结论：(b) 有缺陷，列清单如下（共 1 项）

全量复校 150 题、8 版文字、8 版渲染图、全部机械门之后，**发现 1 项缺陷（D12）**，故本轮不能定稿。
修好后须按 SOP §8.4 循环规则重渲染并从头再做一轮全量校对。

## 缺陷清单

### D12 — P8 答案 F 组 141–144 配对注释中，142 / 144 两条的 `=` 两侧缺空格，与本版其余 39 处不一致

- **源码**：`content8.py:85`，注释表原文：
  `["journaal = news programme b", "groepswinst=group win c", "schoen = shoe d", "gedicht=poem a"]`
  （同一表中 141、143 有空格，142、144 没有。）
- **text.md**：第 142 行 `142. de groepswinst — de eerste plaats in de groep (Correct c · groepswinst=group win c)`；
  第 144 行 `144. het gedicht — een klein versje bij een cadeau (Correct a · gedicht=poem a)`。
- **渲染证据**：交付印 PDF 第 8 版答案区（150dpi 渲染 `render-delivered/p-8.png`；局部裁图 `d12-crop-p8-answers.png`，
  SVG 坐标 x[1430,1870] × y[2260,2400]），肉眼可见：
  - `141. b — journaal = news programme b`（有空格）
  - `142. c — groepswinst=group win c`（无空格）
  - `143. d — schoen = shoe d`（有空格）
  - `144. a — gedicht=poem a`（无空格）
  - `145. A — schoen = shoe`（有空格）
  SVG 侧：`svg/p8-toets.svg` 中 `142. c — groepswinst=group win c`（x=1439.5, y=2297.3）、
  `144. a — gedicht=poem a`（x=1439.5, y=2356.6）。
- **同类全扫**（`eq-spacing-sweep.log`）：全版 `content*.py` 字面量、`.text.md`、8 个 SVG 可见文本行中，
  无空格 `=` 仅此 2 处；有空格 ` = ` 在 text.md 中共 39 处（D 组 25–28 全部有空格，F 组 141/143 有空格）。
  键本身无误：25–28 = d/c/a/b，141–144 = b/c/d/a（已再验）。
- **根因**：core-nl 同表四条全无空格（`journaal=新闻节目 b` 等）；fan-out 改写时 141/143 补了空格、142/144 漏补，
  造成本版内部不一致。不是键错、不是溢出、不影响版式。
- **建议修复**：`content8.py:85` 两条改为 `"groepswinst = group win c"`、`"gedicht = poem a"`（与本版其余 39 处一致），
  重跑 run.py + render.py + webpdf.py + export，重验 P8 两行宽度（现行单行约 300px，栏宽 422.5px，有余量；
  修复方重跑门禁时复核），然后整轮重校。

## 观察项（非缺陷，已裁定，不阻定稿）

- **O1 — P8 标题 `A　VUL DE KRONIEK IN`：观察，非缺陷**（独立实测，未照搬 nl-ko 版结论）。
  SVG：`p8-toets.svg`，x=88.0，y=201，21pt，Noto Sans CJK SC 700，advance 234.86；
  PIL 真墨盒 (87.00,185.00)–(323.00,201.00)，墨右 323.00。
  交付印 PDF 300dpi 渲染（`render-delivered/p8-300-8.png`，scale 3.1251）紧带扫描（墨行 y[185,201] × 第 1 栏 x[88,510.5]）：
  墨右 x=320.63（与 PIL 323.00 一致，PIL 盒保守约 2px），栏右缘 510.5，**栏内余 +189.87px**；逐行墨右均为 320.63
  （y=185 行 237.75 为首行大写 A 的缺口行，属字形正常形态）。
  所谓 −26.5 数量级：同带内第 2 栏 B1 色块左缘实测 x=538.64（色块 rect 左缘 538.5，抗锯齿外溢 −0.14px 即无），
  全行无栏限制扫描会报 `538.64 = 510.5 + 28.14` —— 扫到的是第 2 栏 B1 色块，不是标题墨。
  core-nl 同位逐值相同（紧带墨右 320.63、色块左缘 538.64、像素数 n=14538 全同）。
  300dpi 裁图目视（`p8title-crop300.png`）：标题在栏内，下划线止于栏缘，B1 色块分离清晰。
- **O2 — freeze diff `--strict-cjk` RC=1：裁定为误报，非缺陷。**
  15 个新增 CJK 字符全部是 U+3000（全角空格，p1 +1、p2–p8 各 +2），零汉字、零 CJK 标点；
  全版可见文本行 CJK 标点 0（8 版逐查）。U+3000 是 SOP §1.1 强制的分隔符（`HET NIEUWS　TOP STORY` 等），
  core 本身每版亦有 12–19 个。工具文档将 strict 规则限定于 zh/ja 版（新增目标语文本才算违规），
  本版为 en 读者版，不适用。`<title>Lucerna 三色蛾</title>` 是蛾标元数据（非可见文本），core 同位同值。
- **O3 — print/web 文字层坐标差 2（0.1pt 舍入口径）：非缺陷。**
  坐标法（0.1pt）P1 有 2 个 token 位置差，全是刊头 `De Lucerna`、Δx ≤ 0.22pt；
  词序法（gates.py 同款：sorted-text 空白分词）8 版 posdiff=0、msdiff=0，
  token 数 790/828/738/735/807/748/915/2319 与 KIT 一致。pdftotext 均为 45,434 B。
- **O4 — §1.1 版外调色：非缺陷。**
  出调色板填充只在蛾标路径内（#84A283/#F1E8D4/#4D72B4/#7898CD/#D7B257/#EDD17F，P1 各 1–4 次）与
  绿底次级文字 #CAC8BA（P1×1、P7×2），与 core-nl 逐项同数（蛾为 SOP 点名的品牌标记，三色蛾落于刊头线）。
  金色：无 #d4af37/#c9a227；"gold" 字串命中均为 base64 图数据内噪声。描边矩形 0；VOL.5 = 5 = core；纸色填充 8 版。
- **O5 — spill 候选 31 条：全部裁定非溢出。**
  奶油盒 PIL 真墨容纳 0 flags（修正前 v1 的 14 flags 是 getbbox 未减 ascent 的度量错，见 GATE-LOG）；
  5 处盒底 7px 条带暗像素复核均为 0（P2 EN JIJ / P5 / P7 BRIEVEN / P4 / P3）。
  31 条候选分属：相邻盒的盒题（8）、页眉/栏目条（5）、图注/说明（6）、上一盒末行（7）、下一盒首行/注释（5），
  无一条属于盒内文本出盒。
- **O6 — core 遗留核查债（KIT §9）：非本版缺陷。**
  德国/周五比分、intocht 官方日程之外细节，core-nl 侧已列为待赛后补丁的开放项；fan-out 未改目标语文本，
  本版不引入新事实。交协调员定夺，不在本轮修复范围。
- **O7 — F 组注释另两处格式**：141/143 已有空格，与 D 组一致，无问题；不另立项。

## 全量文字复校摘要（SOP §8.4）

- 逐字精读 `.text.md` 431 行 + 8 版 SVG 文本 + 8 版 150dpi 交付渲染图；编号 1–150 无缺无重；
  级别 A2 46 / B1 73 / B2 31；题型 complete 65 / choice 44 / matching 8 / true-or-false 7 / make-sentences 8 /
  cloze-choice 13 / translate 4 / writing 1；范文 81 词（空白切分，含独立短横 `–` 一词；不计为 80，仍在 80–100 档内；
  与注册表及 P8 注 `(81 words)` 一致）。
- 日期星期全验（Europe/Amsterdam）：11-01 周日、11-11 周三、11-13 周五、11-14 周六、11-15 周日、
  11-16 周一、11-18 周三、11-21 周六、11-22 周日、11-24 周二、11-29 周日、12-05 周六——文中全部星期表述吻合。
  天数验算：11-16→12-05 = 19 天（Q22/Q45 与文中“over negentien dagen”一致）；11-22→12-05 = 13 天（P5 一致）；
  14→15 日 = 1 天、12:00–16:00 = 4 小时、2009→2026 = 17 年；积分榜自洽（荷 8 分：胜塞×2、平德、平希；
  进球 7–5；德 5 分：平荷、负希、胜塞、平希；图表 35+30+20+15=100，35+30=65）。
  8 条金句逐字与正文核对无误，各带页码与英译。
- 全部 150 题答案逐题对题面/原文再验：键、释义、时态（包括 Q53 复数 kwartfinales、Q75 复数 kandidaten、
  Q107 单数 speelde 对 Q60 复数 speelden、omdat 从句动词末位 Q111/Q112）均正确；D 组与 F 组配对键已再验。
- 弯引号全扫：U+2018/2019/201C/201D/201A/201E/2032/2033 在 `content*.py`、SVG、`.text.md` 中均为 0；
  `Editor's`（P7 BRIEVEN）与 `"Group win"`（P1）均为直引号，渲染目视无宽缝。
- 可见汉字 0；CJK 标点 0；标题实测：大标题行 17 条（P1 3 条：顶栏 1 条 + `VANAVOND IN BERLIJN!` + 头条；
  P2–P8 各 2 条：栏目题 + `De Lucerna` 页眉）+ 奶油盒题 21 条 = 38 条（按 SVG 文本 run 计 46 个，P1 顶栏拆 8 个 run；
  “56 标题”在本版无任何定义可复现，不采用）。盒题墨迹扫描 21/21 在盒内，最紧 +8.5px
  （P1 `DE WEEK IN CIJFERS　IN NUMBERS`、P7 `HET WOORD　WORD OF THE WEEK`），0 出边。
- P1 HET WOORD 注 `"Group win": first in the group.` 基线 1846.2，`p` 降部墨至 y≈1850，1851–1861 行暗像素 0，
  1853 发色线（#d8d2c4 细线）之下无注墨——整注在线上，符合 fix 记录。

## D6–D11 逐项复核

| 项 | 结论 | 证据 |
|---|---|---|
| D6（P3 bridge `。` 孤儿）| 预先不存在 ✓ | `content34.py:78` 英文桥句；SVG 2 行 `Complete with the present perfect. Watch` / `the auxiliaries hebben/zijn.`；全版孤儿扫 (a)/(b) 均为 0 |
| D7（P7 词桥 `。` 孤儿）| 预先不存在 ✓ | `content7.py:19` 英文桥句；SVG 3 行，末行 `score.` 为词非标点；孤儿扫 0 |
| D8（P6 caption `。` 行首）| 预先不存在 ✓ | `content56.py:143` 英文 caption，CW−44；SVG 4 行，末行 `people)`；孤儿扫 0 |
| D9（Q140 键缺 `kort`）| 已修，三处同步 ✓ | `content8.py:75`、text.md:415、P8 节点（x=1439.5, y=2222.28）均为 `Ik maak een surprise met een kort gedicht.`；题干 `I am making a surprise with a little poem.` 不变 |
| D10（P7 `dt_zh` `，` 行首）| 预先不存在 ✓ | `content7.py:91` 英文 1 行（y=1812.77）；孤儿扫 0 |
| D11（P4 HET PROGRAMMA 盒末行出盒）| 已修，独立再算 ✓ | `content34.py:130-138` top reserve 89（16+52+21 注释在位）；盒 rect x=1439.5 y=591.6 w=422.5 h=638.0，底 1229.6；末基线 1209.49（`18:45 uur.`），**基线余量 +20.11px**；真墨最低 y=1209.00（cards 1×）/+20.60px、1208.91（交付 150dpi）/+20.69px；盒底 7px 条带暗像素 0；P3 同形盒交叉核对 +16.20px。公式是结构性的：5 条 facts 换行 3/3/3/2/3 = 14 行（wrap 再算与 SVG 基线逐值吻合，首 680.60、末 1209.49）|

## D4 / D5

- **D4**（答案标记本地化）：text.md `— Correct:` 142、`（Correct ` 8（与 KIT 一致）；P8 印版用短横式 `key — note`（不含 "Correct" 字样，
  属既定排版，p8.py 双式兼容）：答案区 150 行以题号起行、149 行含 ` — `（第 150 题为 `✓`），斜体 span 印 = 网 = 1。
- **D5**（P4 Eredivisie 积分行）：`content34.py` facts 第 4 条在位；SVG P4 y=1054.37
  `Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.`；Q63/Q126 键 26 与之自洽。

## SHA 核对（开工 / 收工两次一致）

- 印 `De-Lucerna-VOL4-nl-en.pdf`：`29073788fa2fc7dfd426e6d209251f0919bdbf2cb33f79dbbc10eb15f92b2342` / 12,665,899 B ✓
- 网 `De-Lucerna-VOL4-nl-en-web.pdf`：`6fd0ad3d700d686f9889faecd5e6076a6d9c309372f6871ad0faa4e41a253f98` / 1,610,560 B ✓
- 文 `2026-w47-nl-en.text.md`：`84ed9f3555e4995de8c4450ca9180019414ad907a63ed384ab632a8293612f91` / 45,111 B ✓
- 与 KIT §10 记载三 SHA 及任务给定值全部一致；收工复核未变（生产只读，未动）。
