# GATE-LOG — W47 core-nl proof2（fix2，commit 5de7492f）

复校员独立重跑全部机械门。命令一律用 `tools/venv/bin/python`；输出在本目录。
工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-nl2/`
（`step1-d3d5.txt`、`step2-d4d5.txt`、`step3-gates.txt`、`step3b-p8compare.txt`、`step4-inkprobe.txt`、
`step4b-inkprobe.txt`、`occlusion.log`、`creambox.log`、`freeze.log`、`p8-extract.json`、`render/`。）

## 关于 “gates_core 16/16”

仓内与 goals 侧均无名为 `gates_core` 的脚本（`grep -rln gates_core` 在
`production/2026-w47/core-nl/` 无命中；全 goals 树递归 grep 13 分钟未完成，已终止——
结论：无此现成脚本）。本轮将任务书的 “gates_core 16/16” 落为以下 16 项独立核对，
逐项实测通过（编号 G1–G16）。

## G1 身份核对 — PASS

```
sha256sum production/2026-w47/core-nl/De-Lucerna-VOL4.pdf
  5308f4a321e6176acfe58b69b858413183093097559b6fe3bd9a50eb5bd361f8  25,955,593 B
sha256sum De-Lucerna-VOL4-web.pdf
  a5f7ecba7d8436fb9173f2f468b6074e98514e316964b6e50c8cd966d6a1cfd3  2,104,002 B
sha256sum 2026-w47-nl-zh-cn.text.md
  2f2a650b54989e7b4b656f21cc2ae613e9dc42425a56106f03e00dff6b25d92e  44,088 B
git rev-parse HEAD = 5de7492fc182e87209ffd75544b66e660f62665a
```
三项尺寸＋SHA 与任务书逐字一致。

## G2 D3 复测（advance + 真墨）— PASS

`step1_d3d5.py`（builder `text_w`）+ PIL FreeType `getbbox`（Newsreader 23px）：

| 行 | advance 右缘 / clearance | 真墨右缘 / clearance |
|---|---|---|
| a. een lijst met wensen voor（＋折行 Sinterklaas） | 1764.2 / +97.8；折行 +269.4 | 1764.5 / +97.5 |
| b. een klein versje bij een cadeau | 1816.5 / +45.5 | 1817.5 / +44.5 |
| c. eten voor Sinterklaas' paard | 1790.1 / **+71.9** | 1790.5 / **+71.5** |
| d. die staat 's avonds bij de deur | 1806.5 / +55.5 | 1806.5 / +55.5 |
| 25. de schoen | 1589.7 / +272.3 | 1583.5 / +278.5 |
| 26. de wortel | 1582.3 / +279.7 | 1576.5 / +285.5 |
| 27. het verlanglijstje | 1662.9 / +199.1 | 1653.5 / +208.5 |
| 28. het gedicht | 1603.2 / +258.8 | 1596.5 / +265.5 |

版心右缘 1862，门限 ≥+5px。旧串 P2 渲染行残留 0。印/网双 PDF 文字层含新串、旧串 0。

## G3 D4 复测（9 版 text.md）— PASS

`step2_d4d5.py`：9 版每版 430 行、新标记 142 条、新配对裸词 8 条、「答案」残留 0 处、
他语标记串入 0。见 PROOF-NOTE.md §2 表。
对照组 core-nl 432 行 / 162 行含「答案」/ `— 答案：`142 处；nl-zh-tw 430 行 / 162 行 / 142 处 —— 未动。

## G4 D5 四处存在性 — PASS

`step1/step2`：P4 SVG（两行 y=1054.37 / 1084.90）、印 PDF 文字层、网 PDF 文字层
（空白归一化整句匹配）、text.md 第 188 行，均含 `Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.`。
框：x=1439.5 y=591.6 w=422.5 h=611（底缘 1202.6），末行基线 1084.9，余量 ~118px；P4 目视行在框内。
Q63（text.md 216 行）、Q126（398 行）原文未动。

## G5 D5 事实独立核实 — PASS

公开检索 11 源一致（Sportradar / VAVEL / PitchLab / Sports Mole / Sports Oracle /
Road2Sushi / BankoZeka / TuringStats / Pitchside Lab 等）：第 12 轮（8 Nov 2026）后
PSV 26（12 场 8-2-2）、Feyenoord 25（7-4-1）、Ajax 25（7-4-1），顺序与积分榜一致。

## G6 text.md 全文通读 + 150 题手验 — PASS（149 通过＋1 开放题）

432 行全文通读；150 题逐题对照正文验算（`keycheck-150.json`）：
PASS 149、OPEN-WRITING 1（Q150，范文 81 词）、MISMATCH 0。
按版 10/18/18/18/18/18/12/38；级别 A2 46 / B1 73 / B2 31；金句 8/8 逐字出自正文。

## G7 印 PDF 8 页逐页目视 — 2 处缺陷（D6/D7）

自渲染（PyMuPDF 1.5×，`render/p1–p8.png`）：P1、P2、P4、P5、P6、P8 干净；
P3、P7 各一处句末 `。` 独占一行（见 PROOF-NOTE.md §4，裁图 `render/crop-p3-orphan.png`、
`render/crop-p7-orphan.png`）。其余目视点：P1 照片署名 CC0、P2 D 组、P4 D5 框、
P5 Robinson 配图诚实图注、P6 图表柱比、P7 金句/下期预告、P8 答案区均无异常。

## G8 几何遮挡扫描 — PASS：0 flags

```
tools/venv/bin/python tools/occlusion_audit.py --selftest production/2026-w47/core-nl/svg/
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
svg/: 0 flags
```
（`occlusion.log`）

## G9 creambox 全版 — PASS：0 真溢出

`check_creambox.py`（fix 轮同款脚本，拷入本目录重跑，`creambox.log`）：
p1 0、p2 1、p3 0、p4 0、p5 1、p6 1、p7 0、p8 0，共 3 旗标，均为 CREAM-BOTTOM（≤1.6px）。
真墨探针（`step4/step4b`，卡片 PNG 框底以下 7px 带逐像素）：
- P2 y=1383.36 行：带内非纸像素 0；墨底 1384.4 vs 框底 1387.8（余量 +3.4px）
- P5 y=932.05 行：带内非纸像素 0；墨底 933.0 vs 框底 936.5（余量 +3.5px）
- P6 y=659.44 行：带内非纸像素 0；墨底 661.4 vs 框底 665.0（余量 +3.6px）
三处均为中文末行套用拉丁 0.3×size 下伸裕量的人为假阳性。P4 含 D5 新行的框 0 旗标。
**结论：creambox 真溢出 0。**

## G10 p8 extract — PASS：150/150

```
tools/venv/bin/python tools/p8.py extract --p8 svg/p8-toets.svg --total 150 --json p8-extract.json
noted_set = 1..150（150 项，无缺无多）
```

## G11 p8 印出键 vs text.md 答案对照 — PASS：CLEAN

`step3b_p8compare.py`：text.md 解析答案 149 条（Q150 开放题除外），
与 p8 `keys` 逐题对照 **0 不符**；配对项 25–28（d/c/a/b）与 141–144（b/c/d/a）一致；
Q150 p8 印 `✓`。P2 右栏 a/b/c/d 与 P8 F 右栏 a/b/c/d（含 b 项折行 `televisie`）与 text.md 键一致。

## G12 freeze baseline — PASS：8/8

```
tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-nl \
  --core-svg production/2026-w47/core-nl/svg --out scratch-proof-core-nl2/freeze
baseline: 8/8 SVGs byte-identical（p1–p8 逐页哈希一致）
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```
（`freeze.log`；重建在干净拷贝目录中进行，未碰 shipped 文件。）

## G13 P8 最小字号 — PASS：10.12pt ≥ 9.75pt

PyMuPDF 印 PDF 第 8 页 span 尺寸直方图：最小 10.12pt（560 spans），其余 ≥10.35pt。
（`step3-gates.txt`）

## G14 印/网文字层一致 — PASS：0 diff

PyMuPDF position-sorted tokens（逐页）：

| 页 | print tokens | web tokens | 位置 diff | 多集 diff |
|---|---|---|---|---|
| P1–P8 | 760/715/673/671/700/659/738/1685 | 相同 | 0 | 0 |

`pdftotext` 字节：print 44,198＝web 44,198。
注：token 计数与 FIX-LOG（751/706/665/659/686/649/736/1668＝6,520）略有出入，
系分词口径不同（本轮用 `get_text("words")`）；print==web 的 0 diff 结论在两种口径下一致，
不构成缺陷。

## G15 弯引号全扫 — PASS

8 版 SVG `<text>`＋text.md：ASCII 双引号 `"` 0 处、反引号 0 处；
`« »` 成对（P1 1对、P2 2对、P7 30对、P8 2对）；`“ ”` 仅 P1 一对（本周词中文释义，与 text.md 第 46 行一致）。
直引号 `'` 11 处全部为荷兰语合法省音/所有格（`'s avonds`、`'s nachts`、`Sinterklaas'`），
已逐条列出（`step3b-p8compare.txt`），无直引号误用。

## G16 外部事实独立核查 — PASS

见 PROOF-NOTE.md §5 全表：Nations League 表格＋8 场 MD1–MD4 比分、Eredivisie R12 比分＋
R13 四场开球时间、Sinterklaas Grave＋阿姆斯特丹（88 届、全部时刻与路线）、Heel Nederland Leest、
Expeditie Robinson、欧冠 24 Nov＋Feyenoord–Ajax 29 Nov、全部日期验算——**全部一致，0 事实错误**。
已知 §4 未决项（周五 MD5 比分未刊登）未作缺陷：正文未宣称周五比分。

## 汇总

- 16 项门禁：16/16 通过（G7 目视项下挂 D6/D7 两处同类轻微排版缺陷，见 PROOF-NOTE.md §4）
- 结论：(b) 有缺陷，不可定稿；fix3 修 D6/D7 后重校
