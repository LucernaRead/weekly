# GATE-LOG — W47 core-nl proof3（fix3，commit f567bcea）

复校员独立重跑全部机械门。命令一律用 `tools/venv/bin/python`；输出在本目录。
工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-nl3/`
（`step0-d6d7-orphan.txt`、`step1-d3d5.txt`、`step2-d4d5.txt`、`step3-gates.txt`、
`step3b-p8compare.txt`、`step4-inkprobe.txt`、`step4b-inkprobe.txt`、
`step4c-p6-inkprobe.txt`、`occlusion.log`、`creambox.log`、`freeze.log`、
`freeze-diff.log`、`freeze-diff.json`、`p8-extract.json`、`p8.log`、`p8compare.log`、
`build-run.log`、`render.log`、`keycheck-150.json`、`render/`。）

## 关于 “gates_core 16/16”

仓内与 goals 侧均无名为 `gates_core` 的脚本（proof2 已查无此脚本）。
本轮沿用 proof2 的落法：任务书的门禁清单落为以下 16 项独立核对，
逐项实测通过（编号 G1–G16），另加构建重放与 freeze-diff 两项
（G17–G18，本轮新增的独立复现证据）。

## G1 身份核对 — PASS

```
sha256sum production/2026-w47/core-nl/De-Lucerna-VOL4.pdf
  82427d3f80af23588726311dd415ff9caefe0cc153dc3b3637444babd4bc9eb7  25,955,581 B
sha256sum De-Lucerna-VOL4-web.pdf
  44553e5c77d3fbf796939fc35bc43721292e44f1669253cd23fc76c47bcd5a39  2,103,999 B
sha256sum 2026-w47-nl-zh-cn.text.md
  2f2a650b54989e7b4b656f21cc2ae613e9dc42425a56106f03e00dff6b25d92e  44,088 B
git rev-parse HEAD = f567bcea (W47 core-nl fix3: D6/D7 orphan 。 (proof2 rounds))
```

三项尺寸＋SHA 与任务书逐字一致；收工时三项 SHA 重验一致。
（fix2 的印/网 PDF 与 fix3 不同：25,955,593→25,955,581 B；
2,104,002→2,103,999 B。text.md 与 fix2 字节一致。）

## G2 D6/D7 回归（逐元素级 diff + 断行实测）— PASS

`step0_d6d7_orphan.py`：对照基线为 proof2 freeze build-copy 中的 fix2 SVG
（哈希与 fix3 `svg-hashes-before.txt` 逐字节一致）。

- D6：P3 桥句两行 `用现在完成时补全，注意助动词` / `hebben/zijn。`
  （x=538.5，y=2250.5/2280.225），独行 `。` 0。fix2→fix3 仅 2 个
  `<text>` 变化，(x, y) 相同；P3 y 值集合完全相同，零位移。
- D7：P7 gloss 三行 `de wedstrijd 比赛；de groepswinst 小组` /
  `头名；de kwartfinale 四分之一决赛；` / `scoren 进球。`
  （x=88.0，y=725.66/755.385/785.11），独行 `。` 0。fix2→fix3 仅 3 个
  `<text>` 变化，(x, y) 相同；P7 y 值集合完全相同，零位移。
- 机制：`bslib4.py` `Flow.para`/`Flow.bridge` `w=None` 默认栏宽；
  `content34.py:78` 传 `w=CW - 40`（382.5px），`content7.py:19` 传
  `w=CW - 35`（387.5px），CW=422.5。
- 当前 8 页 SVG 哈希与 fix3 `svg-hashes-after.txt` 逐字节一致；
  before→after 仅 p3、p7 变化，其余 6 页与 fix2 字节一致。

## G3 孤儿标点全版扫查 — PASS：0

`step0_d6d7_orphan.py`：8 版 SVG 按基线 y 分组，基线拼接后单字元
`。` / `» ” ’ ） 」 》` / `：` / `–` 全部为 0。
P8 的 7 个单字元 `）`逐一核对，均与同基线 4–6 个 sibling 共行
（答案区行内定位符，非孤儿；见 PROOF-NOTE.md §3 表）。

## G4 D3 复测（advance + 真墨）— PASS

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
（`step3-gates.txt` 真墨段逐数一致。）

## G5 D4 复测（9 版 text.md）— PASS

`step2_d4d5.py`：9 版每版新标记 142 条、新配对裸词 8 条、「答案」残留 0 处、
他语标记串入 0。见 PROOF-NOTE.md §4 表。
对照组 core-nl 432 行 / 162 行含「答案」/ `— 答案：`142 处；nl-zh-tw 430 行 / 162 行 / 142 处 —— 未动。
行数注记：de/en/es/fr/it 实测 431 行（proof2 表记 430 行），系并行重 fan-out
已按 fix2 核心重生成 5 版（D5 积分行 +1 行），D4 实质在两种状态下完全一致；
fan-out 不在 core-nl 复校范围。

## G6 D5 四处存在性 + Q126 一致性 — PASS

`step1/step2`：P4 SVG（两行 y=1054.37 / 1084.90）、印 PDF 文字层、网 PDF 文字层
（空白归一化整句匹配）、text.md 第 188 行，均含
`Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.`。
框：x=1439.5 y=591.6 w=422.5 h=611（底缘 1202.6），末行基线 1084.9，余量 ~118px；P4 目视行在框内。
Q63（text.md 216 行）、Q126（398 行，答案 B·26 分）原文与该行一致。

## G7 D5 事实独立核实 — PASS

本轮新检索 12 源一致（Sportradar / PitchLab / Sports Mole×2 / VAVEL×2 /
elFutbolero / Road2Sushi / Sports Oracle / TuringStats / Pitchside Lab / BankoZeka）：
第 12 轮（8 Nov 2026）后 PSV 26（12 场 8-2-2）、Feyenoord 25（7-4-1）、
Ajax 25（7-4-1），顺序与积分榜一致。第 13 轮四场开球时间经 UTC→CET 换算一致
（15:30/17:45/13:30/11:15 UTC → 16:30/18:45/14:30/12:15 CET）。

## G8 text.md 全文通读 + 150 题手验 — PASS（150 通过＋0 不符）

432 行全文通读；150 题逐题对照正文验算（`keycheck-150.json`）
+ 三源交叉（text.md 答案 / P8 印出键 / 各版 SVG 渲染题干）：
PASS 150、MISMATCH 0。Q150 为开放写作题（范文 81 词），P8 印 `✓`。
按版 10/18/18/18/18/18/12/38；级别 A2 46 / B1 73 / B2 31（`run.py` 注册表）；
金句 8/8 逐字出自正文。

## G9 印 PDF 8 页逐页目视 — PASS：0 缺陷

自渲染（PyMuPDF 1.5×，`render/p1–p8.png`）：P1、P2、P3、P4、P5、P6、P7、P8
全部干净；P3/P7 的 fix3 修复点目视确认（D6 两行、D7 三行，句末 `。` 已归位）。
其余目视点：P1 照片署名 CC0、P2 D 组、P4 D5 框、P5 Robinson 配图诚实图注、
P6 图表柱比（35/30/20/15 与数值成比例）、P7 金句/下期预告、P8 答案区均无异常。
P7 VOLGENDE WEEK 带贴底（N3）与 proof2 实测完全一致，未变。

## G10 几何遮挡扫描 — PASS：0 flags

```
tools/venv/bin/python tools/occlusion_audit.py --selftest production/2026-w47/core-nl/svg/
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/core-nl/svg/
.../svg/: 0 flags
```

（`occlusion.log`）

## G11 creambox 全版 — PASS：0 真溢出

`check_creambox.py`（fix 轮同款脚本，拷入本目录重跑，`creambox.log`）：
p1 0、p2 1、p3 0、p4 0、p5 1、p6 1、p7 0、p8 0，共 3 旗标，均为 CREAM-BOTTOM（≤1.6px）。
真墨探针（框底以下 7px 带逐像素，`step4/step4b/step4c`）：

- P2 y=1383.36 行：带内非纸像素 0；墨底 1384.4 vs 框底 1387.8（余量 +3.4px）
- P5 y=932.05 行：带内非纸像素 0；墨底 933.0 vs 框底 936.5（余量 +3.5px）
- P6 y=659.44 行：带内非纸像素 0；墨底 661.0–661.4 vs 框底 665.0（余量 +3.6~+4.0px）

三处均为中文末行套用拉丁 0.3×size 下伸裕量的人为假阳性。P4 含 D5 新行的框 0 旗标。
**结论：creambox 真溢出 0。**

## G12 p8 extract — PASS：150/150

```
tools/venv/bin/python tools/p8.py extract --p8 svg/p8-toets.svg --total 150 --json p8-extract.json
noted set = 150 of 150 (parse: lines)
```

## G13 p8 印出键 vs text.md 答案对照 — PASS：CLEAN

`step3b_p8compare.py` + `keycheck_150.py`：text.md 解析答案 149 条
（Q150 开放题除外）与 p8 `keys` 逐题对照 **0 不符**；
配对项 25–28（d/c/a/b）与 141–144（b/c/d/a）一致；Q150 p8 印 `✓`。
`p8.py compare --core-p8 … --edition-p8 … --total 150`（core 对自身）：
`status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]`。
P2 右栏 a/b/c/d 与 P8 F 右栏 a/b/c/d（含 b 项折行 `televisie`）与 text.md 键一致。
MCQ 键抽查：7:B、9:C、11:B、29:B、47:C、51:B、63:Niet waar、65:B、67:C、
81:Niet waar、92:B、103:B、113:B、121:A、126:B、127:B、128:C —— 均与 text.md 一致。

## G14 freeze baseline — PASS：8/8

```
tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-nl \
  --core-svg production/2026-w47/core-nl/svg --out scratch-proof-core-nl3/freeze
runtime: tools/venv/bin/python | Pillow 13.0.0 | FreeType 2.14.3
baseline: 8/8 SVGs byte-identical (repointed files: none)
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```

（`freeze.log`；重建在干净拷贝目录中进行，未碰 shipped 文件。）

## G15 freeze diff（string freeze）— PASS：+0/−0，新增 CJK 0

```
tools/venv/bin/python tools/freeze.py diff --core-svg <core>/svg --edition-svg <core>/svg
p1–p8: 每页 +0 strings / −0 strings；CJK core == edition（217/237/146/148/230/205/387/1074）；added CJK chars: 0
TOTAL added CJK characters: 0
```

（`freeze-diff.log`、`freeze-diff.json`）

## G16 P8 最小字号 — PASS：10.12pt ≥ 9.75pt

PyMuPDF 印 PDF 第 8 页 span 尺寸直方图：最小 10.12pt（560 spans），其余 ≥10.35pt。
（`step3-gates.txt`）

## G17 印/网文字层一致 — PASS：0 diff

PyMuPDF position-sorted tokens（逐页）：

| 页 | print tokens | web tokens | 位置 diff | 多集 diff |
|---|---|---|---|---|
| P1–P8 | 760/715/673/671/700/659/738/1685 | 相同 | 0 | 0 |

`pdftotext` 字节：print 44,197＝web 44,197。
（与 fix2 的 44,198 差 1 字节：D6 重排丢掉助动词与 hebben/zijn 之间的
单个空格，FIX-LOG 已解释；D7 部分字节中性。）

## G18 构建重放（source freeze 独立复现）— PASS

干净拷贝中重跑 `run.py`（`build-run.log`）：TOTAL 150，
按版 10/18/18/18/18/18/12/38，级别 A2 46 / B1 73 / B2 31，
0 FLOW OVERFLOW / 0 HEAD TOO WIDE；重建 8 页 SVG 与已交付逐字节一致；
重跑 `render.py`（`render.log`）重建的印 PDF 与已交付**逐字节一致**
（25,955,581 B，SHA `82427d3f…b4bc9eb7`）。

## 补充门禁（任务书点名项）

- **scans**：occlusion 0 flags（G10）。
- **chips**：级别芯片 A2/B1/B2 与注册表 46/73/31 一致（G8/G18）；P8 目视芯片无错位。
- **keycheck**：150/150（G13）。
- **mcq**：单选题键全量对照 0 不符（G13）。
- **widths**：D3 advance＋真墨全表（G4）。
- **band_spans**：P7 VOLGENDE WEEK 带重测——带 rect y=2439 h=118 底 2557.0，
  末行基线 2551.56，墨底约 2556.6，0px 溢出，与 proof2 完全一致（N3，未变）。
- **D5 字体**（全周级已知待定项，只记录）：CJK 字体段 619 段，
  含拉丁字母者 335 段，纯拉丁字母者 245 段（分版 38/23/30/29/29/26/18/52）。
- **弯引号**：ASCII 双引号 0、反引号 0；`« »` 成对；`“ ”` 仅 P1 一对（G8 段）。
- **金句**：8/8 逐字出自正文（`step3-gates.txt`；本轮已修该节 `md` 为 list
  的崩溃 bug，见 PROOF-NOTE.md §8）。
- **Q150 范文**：81 词（除独立 `–` 计 80 词），在 80–100 内。

## 汇总

- 18 项门禁：18/18 通过；缺陷 0；nits 5 项（proof2 原样携带，见 PROOF-NOTE.md §7）
- 结论：**(a) 无缺陷，可定稿**
