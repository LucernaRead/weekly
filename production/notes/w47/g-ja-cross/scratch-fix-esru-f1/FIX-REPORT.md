# FIX-REPORT — W47 es-ru F1（P5 分隔线横穿 ¿Y TÚ? 框）

- **工人**：es-ru 单版修复（与第七轮重校员不同人；只修 es-ru 一版）
- **日期**：2026-11-13（UTC 约 05:50–06:05）
- **来源**：`hidden_files/w47/scratch-verify-es/VERIFY-REPORT.md` §4 + `PROOF-NOTE-7.md` §1（F1，low，P5）
- **结论：F1 已修。纯几何修，未动文字，未动分隔线，未动其他页。全部机械门禁绿；P5 目视复核通过。须再做一轮全量重校（SOP §8.4）后才能定稿。**

## §0 修前复现（当前印 PDF 直接实测，修前未改任何东西）

| 量 | 修前实测值 |
|---|---|
| ¿Y TÚ? 奶油框（SVG/PDF 双重实测） | x=1439.5，y=1277.55，h=356.0，**框底 1633.55** |
| EJERCICIOS 分隔线 | y=**1608**，x 88→1862，全宽，橄榄绿 2px，后绘于框之上 |
| 超出量 | 框底 − 分隔线 = **25.55px**（与 PROOF-NOTE-7 的 25.5px 一致） |
| 框内俄文末行 `пришлите их.` | 基线 y=1626.59（分隔线之下、框底之内）；上一行 `Напишите два предложения и` 基线 1599.61（分隔线之上） |
| 目视 | 150dpi 全页 P5 + 局部放大：绿线在两行俄文之间横穿框体（见 `p5-before-zoom.png`） |

F1 在当前印 PDF 上复现成功（SVG 几何 + PDF 矢量实测 + 目视三重一致），才动手。

## §1 修法（协调员已定：优先纯几何修）

几何手段已省出 34.52px（> 所需 26px），**无需缩短俄文，未动任何文字**。text.md 未重建（措辞未改，SHA 不变）。

改动文件：`production/2026-w47/2026-w47-es-ru/content56.py`，仅 ¿Y TÚ? 框（行 49–71）：

| 改动 | 旧值 | 新值 | 省出 px |
|---|---|---|---|
| 标题→正文间距（行 69） | `yy3 += 52` | `yy3 += 46` | 6.00 |
| 西语行距（行 70） | `1.42`（步长 30.53） | `1.38`（步长 29.67） | 3.44（含 para 回返步长） |
| 西→俄块间距（行 70） | `+ 10` | `+ 2` | 8.00 |
| 俄文首行偏移（行 71） | `yy3 + 20` | `yy3 + 12` | 8.00 |
| 俄文行距（行 71） | `1.42`（步长 26.98） | `1.30`（步长 24.70） | 9.12 |
| **合计** | | | **34.56**（实测 34.52，0.04 为浮点舍入） |

- 字号不变：西语 21.5pt、俄文 19pt；折行不变：西语 4 行、俄文 5 行（`wrap()` 实测确认）。
- 框高公式改按实际绘制偏移推导（行 60–65：`es_first` / `ru_first` / `ru_last` / `eh = ru_last + 7`），取代旧启发式 `62 + …×30.5 + 12 + …×27 + 25`——旧公式与实际绘制漂移（绘制的末行基线偏移 349.04，公式只算到 331）是本次框底失控的机制性原因之一；新公式与绘制共用同一组参数，不会再漂移。
- 分隔线（`ey = 1620`，`hline … ey - 12`）未动；其余页、其余框未动。

## §2 修后实测值（SVG + 印 PDF 双重实测，一致）

| 量 | 修前 | 修后 | 变化 |
|---|---|---|---|
| 框高 eh | 356.0 | **321.48** | −34.52 |
| 框底（y=1277.55 + eh） | 1633.55 | **1599.03** | −34.52 |
| 分隔线 y | 1608 | 1608（未动） | 0 |
| 框底距分隔线 | −25.55（超出） | **+8.97（余量）** | +34.52 |
| 末行俄文 `пришлите их.` 基线 | 1626.59 | **1592.03**（距线 15.97） | −34.56 |
| 西语末行 `Escribe dos frases en español.` 基线 | 1458.14 | 1449.56 | −8.58 |
| 西→俄块间距（末行基线→首行基线） | 60.53 | 43.67 | −16.86，仍为清晰分块 |
| 框底内边距（末行基线→框底） | 6.96 | 7.00 | +0.04 |

## §3 新 SHA-256（修后完整值）

| 件 | 字节 | SHA-256 |
|---|---|---|
| 印 `La-Lucerna-VOL4-es-ru.pdf` | 3,100,959（修前 3,100,944，+15 B） | `c4732fd0f2ab07d8d4ed834ab5b2356f58ab0f9f592220bf032b960035cc9bf3` |
| 网 `La-Lucerna-VOL4-es-ru-web.pdf` | 950,846（修前 950,823，+23 B；< 7 MB） | `cc549a5a212afc4960038720aae88468041562f031b96ea81292c70033fb5551` |
| text.md `2026-w47-es-ru.text.md` | 52,367（未变，未重建） | `ac246f8709d3535958ccebb3b6913800bd3866001de5322358d3ba026f69c42b` |

KIT 已更新：§8 印/网改为新值，末尾新增 `fix-esru-f1` 一节（新 SHA 各 ×2 处：§8 + 该节）。

## §4 重建范围核实

- `run.py` rc=0（TOTAL 150；0 FLOW OVERFLOW / HEAD TOO WIDE；分级 A2 50 / B1 72 / B2 28，与修前一致）→ `render.py` rc=0（印 + 网一次生成）。
- SVG diff（修前 SHA 清单 `svg-before.sha256`）：**仅 `p5-juventud.svg` 变**，p1–p4、p6–p8 字节一致。
- 俄文未缩短：无改动前后文字对照（无文字改动）。

## §5 全部门禁（`gates-fix.sh` / `gates-fix.log`，2026-11-13 05:59 UTC，全部绿）

| 门 | 工具 | 结果 |
|---|---|---|
| p8 extract | `tools/p8.py extract --total 150` | 150/150，rc=0 |
| p8 compare vs core-es | `tools/p8.py compare --total 150` | **CLEAN**，missing=[] extra=0，keydiff=[137, 138]（已裁定的读者语翻译题差异，同前），rc=0 |
| D5 census | `scratch-d5-plan/mechanism/d5_census.py` | **CENSUS PASS**，rc=0 |
| 几何遮挡（真实审计，门） | `tools/occlusion_audit.py svg/`（不带 `--selftest`） | **0 flags**，rc=0 |
| 几何遮挡自检（仅 sanity check，不当门） | `tools/occlusion_audit.py svg/ --selftest` | selftest OK，rc=0 |
| 框题 | `tools/boxtitle_check.py` | 38 titles / 584 body lines，**0 DEFECT**，0 OBSERVE，0 marginal，rc=0 |
| 溢出 | `tools/spill_sweep.py` | 27 盒 / 149 candidates，**0 SPILL**，149 OBSERVE，rc=0 |
| 页缘 | `tools/pdf_edge_scan.py` | 8 页，**0 TOUCH / 0 NEAR**，rc=0 |
| 冻结复现 | `tools/freeze.py baseline` | **8/8 SVGs byte-identical**，rc=0 |
| 印/网文字层 | `pdftotext` + `cmp`（plain 与 `-layout` 两版） | 各 53,414 B（plain）/ 113,438 B（-layout），**逐字节一致** |

注：修前印/网 pdftotext 为 53,413 B，修后 53,414 B（+1 B）——文字未变（text.md SHA 不变，SVG 文本节点只改了 y 坐标），+1 B 是 pdftotext 行分组随行距重排所致；门禁要求的是印/网之间逐字节一致，修后两侧均为 53,414 B，通过。

## §6 P5 目视复核（修后印 PDF，150dpi）

- 放大裁图前后对照：修前 `p5-before-zoom.png`（绿线横穿框体）→ 修后 `p5-after-zoom.png`（框完整收在分隔线之上，`пришлите их.` 在框内、完整可读，分隔线与框无交叉，框下留白干净）。
- 全页 P5 渲染 `p5-after-5.png`：EJERCICIOS 标题行与第 77 题等下方内容均未受影响（练习流起于固定 ey=1620，与框无关）。

## §7 工作记录与约束遵守

- 只碰 es-ru 一版；未 commit、未 push、未跑 `lint --write`、未 reset/stash/add -A；只动 W47 目录（`content56.py` + 生成物 + KIT）。
- 工具一律仓内共享工具 + `tools/venv/bin/python`。
- 磁盘：开始 97G 已用（150G 卷），结束 97G，未触发 ≥100G 停线。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-esru-f1/`：`FIX-REPORT.md`（本文件）、`gates-fix.sh` / `gates-fix.log` / 各门禁日志与 JSON（`p8-extract/ p8-compare/ census/ occlusion[.json] / boxtitle/ spill/ edge/ freeze/`）、`p5-before-5.png` / `p5-before-zoom.png` / `p5-after-5.png` / `p5-after-zoom.png`、`svg-before.sha256`、`print.txt` / `web.txt` / `print-plain.txt` / `web-plain.txt`。
- 建议下一步：按 SOP §8.4 再派一轮全量重校（与本轮修复者、第七轮重校员均不同人）；es 家其余 10 版未动（VERIFIED CLEAN 不变），es 家 bundle 入仓须等 es-ru 重校通过。
