# GATE-LOG — 2026-W47 · nl → de · proof1 独立复校（delta 重建版）

- 版：`2026-w47-nl-de`（VOL.4）· 复校员 proof1 · 2026-11-11
- 全部实测均在本轮独立重跑（生产目录零写入；重建在自有 scratch 的 `rebuild/` 副本中；core-nl 与 staging 只读）
- 交付三 SHA 开工已核：印 `26faddf4…44ef` / 12,669,889 B；网 `74f10eef…97aa0` / 1,617,811 B；文 `ac56f6f9…0117c` / 46,219 B

## 16 项机械门（逐项实测值）

| # | 门 | 实测值 | 结论 |
|---|---|---|---|
| 1 | `run.py`（自有 rebuild 副本） | rc=0；TOTAL 150；分页面 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；0 FLOW OVERFLOW / HEAD TOO WIDE；`P4 col3 ends 1229.6`、`P6 chart ends 717`、`P7 col3 ends 1927.5` | PASS |
| 2 | `render.py`（同副本） | rc=0；重建印 PDF 12,669,889 B（与交付同字节）；SVG 8/8 与交付字节一致（`svg-sha-rebuilt.txt` vs `svg-sha-delivered.txt` 零 diff；registry dump 后复核仍 8/8） | PASS |
| 3 | Occlusion 真实审计（`tools/occlusion_audit.py svg/`，未用 `--selftest` 标志、但自检行照常输出） | rc=0；自检 6 类 planted 全触发，干净对照静默；**0 flags** | PASS |
| 4 | p8 extract（`tools/p8.py extract --total 150`） | noted set **150/150** | PASS |
| 5 | p8 compare（core vs 本版，直接读 `p8-compare.json` 本体） | `status: CLEAN, total: 150, missing: [], extra: [], uncertain: [], keydiff: [137, 138]`；137/138 为翻译题（核心中文键 vs 本版德文键，按设计不同，非缺陷）；修前 keydiff [137,138,140]，D9 已把 140 移出 | PASS |
| 6 | Freeze 核心标准比对（`freeze.py baseline --build <core-nl> --core-svg <core-nl>/svg`，现行口径，freeze.py 强制 `--core-svg`） | rc=0；**8/8 字节一致**；核心 shipped SVG 跑前后哈希不变（未碰核心） | PASS |
| 7 | 版内自比对（clean-dir 重跑 `run.py` 再 sha256 比对） | **8/8**（与门 2 同一重建；registry dump 后复核仍 8/8） | PASS |
| 8 | 印/网文字层（PyMuPDF，交付件；span 级，0.1pt） | 8 页 msdiff 0；posdiff 仅 P1 1 个：masthead `De Lucerna` x 394.0（印）vs 393.8（网），0.2pt 字体子集微移（与核心 fix5 同一已知现象）；其余 7 页 posdiff 0；span 数 219/204/188/185/196/201/187/386 | PASS |
| 9 | 印/网文字层（词级，`gates.py` 套件内） | 8/8 页 posdiff 0、msdiff 0；tokens 832/813/719/720/795/729/890/2256（与 DELTA-LOG 一致；与门 8 口径不同——词级 vs span 级，见注记） | PASS |
| 10 | pdftotext | 印 46,739 B = 网 46,739 B = 自有 web 重渲染 46,739 B；印 vs 网逐字节相同 | PASS |
| 11 | Web PDF（只比文字层） | 自有 scratch 重渲染 `web-rerender.pdf` 1,617,822 B（交付 1,617,811 B，相差 11 B——web PDF 字节不可复现是已知根因，永不以 SHA/字节数论证）；文字层与印 PDF 8 页 msdiff 0；从未覆盖生产目录的网 PDF | PASS |
| 12 | P8 最小字号（SOP §1.1 下限 9.75pt；PyMuPDF） | 答案区 min **10.12pt**（median 10.12，187 spans；全 P8 spans min 10.12 / median 10.35）≥ 9.75pt | PASS |
| 13 | Creambox（`check_creambox_reproof.py`，PIL 真墨） | TOTAL **2 flags**（与修前完全相同的两处：P2 y=1468.56、P5 y=1017.25），均为已知假阳性——几何底仍在盒内（P2 1474.6 < 1474.8；P5 1023.2 < 1023.5），盒底下 7px 条带逐像素探查 **0 非纸像素**（<200 且 <240 均为 0，条带均值 248.7/249.1 = 纸色）；P4（D11 盒）0 flags。**真溢出 0** | PASS |
| 14 | Spill 横扫（全版奶油盒，0–60px 上/下/侧） | **0 spills**；P4 HET PROGRAMMA 盒（底 1229.6）无任何 BELOW 命中；其余 BELOW 命中（+24/+32/+50.5/+60px）均为独立版块（下一节标题、提示语、gloss），ABOVE/SIDE 均为图注/邻盒标题——与核心 fix5 同类裁决 | PASS |
| 15 | 孤儿横扫（自写脚本，PIL + svglib 双 advance，1458/1461 行；另暴力检查） | (a) 独行标点 **0**，(b) 行首标点 **0**，双法 8 页全 0；以标点开头的 `<text>` 元素 **0 个**（CJK + 拉丁标点均纳入） | PASS |
| 16 | §1.1 等效检查（re-proof `check_s11_core_nl.py` 同类检查，重定向到本版 svg；nl 家族无专用 check_s11/verify_ed）+ fanout 门禁套件（`gates_delta.py`，9 项） | s11 等效：rc=0，**17 PASS，FAILURES: none**——纸 #fbfaf6 8/8、level chips 均在 LV 色集、VOL.5=5（= core，均为正文“VOL.5 承诺”内容）、p4 未引入新填充色；套件：**ALL PASS 9/9**（occlusion / p8_extract / p8_compare / freeze_sha256 / print_web_text / pdftotext_nonempty / p8_fontsize / p8_chips / s11_svg，见 `gates.log`、`gates-de.json`） | PASS |

**注记**：(i) 门 8 与门 9 的 token 数不同是口径不同（span 级 vs 词级），相对 diff 均为 0，结论一致；(ii) `gates.py` 日志的 `p8_compare keydiffs=0` 是对 stdout 的计数，权威 JSON 本体（门 5）keydiff=[137,138]；(iii) 纸灰实测约 249、奶油灰约 238，故 7px 条带的“非纸”判定须用 <240（或 <200）阈值，<250 会把纸色本身计入——D11 与 creambox 的 0 像素结论均按此口径；(iv) web PDF 重渲染只在自有 scratch 内，生产目录网 PDF 未动。

## 全部框标题 clear 表（PIL 真墨；最紧 4 处另有交付 PDF 200 dpi 渲染像素交叉验证）

盒右缘统一 1862.0；`clear` = 真墨边到盒边的距离（正值 = 在盒内）。无任何溢出，无任何页缘超限（全版 advance 右缘 ≤1862.0；end/middle 锚定文本另行核对，0 flags）。

| 页 | 盒（x, y, w×h） | 标题 | 左 clear | 右 clear | PDF 渲染交叉验证 |
|---|---|---|---|---|---|
| P1 | (538, 1411, 422×384) | DE WEEK IN CIJFERS　IN ZAHLEN | +20.0 | +33.8 | — |
| P1 | (1440, 588, 422×700) | DEZE WEEK | +24.2 | +249.0 | — |
| P1 | (1440, 1312, 422×340) | IN DEZE EDITIE　AUSGABE（旧 D1，已修复） | +24.0 | +91.2 | 右 +91.0（左 +23.8） |
| P1 | (1440, 1874, 422×430) | IN HET KORT　KURZ GEMELDET | +24.0 | +29.5 | 右 +27.7（左 +23.8） |
| P2 | (538, 827, 422×215) | ZO ONTHOUD JE HET　MERK DIR | +19.0 | +34.0 | — |
| P2 | (1440, 645, 422×352) | WIST JE DAT? | +22.5 | +245.5 | — |
| P2 | (1440, 1022, 422×452) | EN JIJ?　UND DU? | +24.0 | +186.2 | — |
| P3 | (1440, 597, 422×510) | SINTERKLAAS IN CIJFERS（未动，与 staging 完全相同） | +23.0 | +105.0 | — |
| P4 | (1440, 592, 422×638) | HET PROGRAMMA（D11） | +24.0 | +191.2 | — |
| P5 | (538, 647, 422×543) | ZO KIJK JE ROBINSON | +19.0 | +157.2 | — |
| P5 | (1440, 200, 422×406) | JONGEREN IN CIJFERS | +22.5 | +136.8 | — |
| P5 | (1440, 632, 422×392) | EN JIJ?　UND DU? | +24.0 | +186.2 | — |
| P6 | (1440, 200, 422×517) | DE GRAFIEK　ÜBUNGSDATEN | +24.0 | +59.2 | — |
| P6 | (1440, 743, 422×309) | VOOR OF TEGEN?　DAFÜR / DAGEGEN（全版最紧） | +21.8 | **+15.8** | 右 **+15.2**（左 +21.9） |
| P7 | (1440, 200, 422×841) | PAS OP!　FEHLERKLINIK | +24.0 | +122.2 | — |
| P7 | (1440, 1059, 422×282) | HET WOORD　WORT DER WOCHE | +24.0 | +29.0 | 右 +29.1（左 +23.8） |
| P7 | (1440, 1359, 422×568) | BRIEVEN VAN LEZERS | +24.0 | +161.2 | — |

最紧处 P6（+15.8 PIL / +15.2 PDF 渲染）仍有 15px 以上余量——卡片与 PDF 渲染可差约 3px（P1 IN HET KORT 差 1.8px），边缘裁决以交付 PDF 渲染为准，结论不变：全部通过。

## D6–D11 逐项复核

| 点 | 源码行 | 独立实测 | 结论 |
|---|---|---|---|
| D6 | `bslib4.py:119,155`（w 机制，与核心 fix3 一致）+ `content34.py:78` w=368.75 | `svglib.wrap()` 0.25px 重扫：区间 **312.00–425.50**（DELTA-LOG 称 312.0–425.5，一致），选值即区间中点（距两缘各 56.75px）；交付 P3 桥接 2 行逐字不变（2303.5 / 2333.225，句末 `.` 在行末）；p3 SVG 与修前字节一致；裁图 `crop-p3-d6.png` 目检通过 | 通过 |
| D7 | `content7.py:19` w=412.25 | 重扫区间 **394.25–450.00**（DELTA-LOG 称 394.5–430.0，上缘较窄，见 PROOF-NOTE N1）；选值在区间内（距下缘 18.0px、距上缘 37.75px）；交付 P7 桥接 3 行逐字不变（725.66 / 755.385 / 785.11，末行 `scoren treffen.`）；p7 SVG 字节一致；裁图 `crop-p7-d7.png` 目检通过 | 通过 |
| D8 | `content56.py:144,145,157` capcn_w=374.25 | 重扫区间 **358.25–390.00**（称 358.5–390.0，0.25px 步进内一致），选值近中点（距两缘 16.0/15.75px）；交付 P6 图注 4 行逐字不变（635.02/659.44/683.86/708.28）；盒高不变（`P6 chart ends 717`、`P6 col3 ends 1052.0` 与修前同）；p6 SVG 字节一致；裁图 `crop-p6-d8.png` 目检通过 | 通过 |
| D9 | `content8.py:75` 键补 `kort` | 三源一致：registry = text.md:415 = P8 节点（y=2236.28），均为 `Ik maak een surprise met een kort gedicht.`；其余 149 键未动；三源比对 **149/149 MATCH**，DIFF=[]，MISSING=[]；Q150 开放写作例外（P8 键 `✓`，text.md Tekstmodel 81 词，registry 占位）；配对键 25–28 = d/c/a/b，141–144 = b/c/d/a；p8 keydiff [137,138]（修前 [137,138,140]）；裁图 `crop-p8-q140.png` 目检通过；**但德语题干漏译“小”——见 PROOF-NOTE D12（fanout 层缺陷，非 key 错误）** | key 通过；题干见 D12 |
| D10 | `content7.py:92,93,101` dt_zh_w=353.25 | 重扫区间 **286.75–406.75**（称 300.0–406.5，下缘较窄，见 N1）；选值在区间内（距下缘 66.5px、距上缘 53.5px）；交付 P7 来信 2 行逐字不变（1783.77 / 1812.17）；盒高不变（`P7 col3 ends 1927.5` 与修前同）；p7 SVG 字节一致；裁图 `crop-p7-d10.png` 目检通过 | 通过 |
| D11 | `content34.py:130` 顶留 62→89；P3 SINTERKLAAS 盒未动 | 盒底 **1229.6**；末行 `18:45 uur.` 基线 **1209.49**，盒内余量 **+20.11px**；事实句 14 行（3/3/3/2/3）；PIL 真墨余量 **+20.11px**（墨底恰在基线）；交付 PDF 渲染 **+20.07px**；卡片 **+20.60px**；盒底下 7px 条带 0 真墨像素；`P4 col3 ends 1229.6`；裁图 `crop-p4-programma.png` 目检通过 | 通过 |

## 其余独立复核（PROOF-NOTE 详述）

- D3 回归：P2 选项 c 真墨右缘 1789.5，余量 **+72.5px**；a +98.5 / b +46.2 / d +56.0（与 fix4 的 +71.5/+97.5/+44.5/+55.5 在方法误差 ~1px 内一致）。
- text.md：431 行；142 单题 + 2 配对头 + 8 配对项 = 150；8 金句（text.md 与印 PDF 均 8/8）；引号：ASCII `"` 0、反引号 0、`« »` 35/35、德语 `„ “` 1/1。
- 150 题手验：`keytable-150.txt`，150/150 通过（唯一不一致为 D12 题干/key 跨源问题）。
- 8 页目检：200 dpi 渲染 `read-p1..p8.png` 逐页看过，无新缺陷（P6 下半页留白为版式固有，非缺陷）。
