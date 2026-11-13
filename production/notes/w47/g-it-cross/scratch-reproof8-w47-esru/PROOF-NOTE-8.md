# PROOF-NOTE-8 — W47 es-ru 第八轮独立重校

- **重校员**：第八轮独立重校员（与修复者、第七轮 98e7d18f、第六轮 50ffaae9 均不同人）
- **日期**：2026-11-13（UTC 约 06:00–06:20）
- **对象**：`production/2026-w47/2026-w47-es-ru/` 一版（只碰 es-ru）
- **依据**：SOP.md 全文已读（§8 校对闭环）；工具一律仓内共享工具 + `tools/venv/bin/python`
- **结论：(a) CLEAN —— 零问题。F1 已修好且无回归，全量重校零发现。**

## §0 指纹表（独立实测，与任务给定值逐字节一致）

| 件 | 字节 | SHA-256（实测） |
|---|---|---|
| 印 `La-Lucerna-VOL4-es-ru.pdf` | 3,100,959 | `c4732fd0f2ab…`（全值 `c4732fd0f2ab07d8d4ed834ab5b2356f58ab0f9f592220bf032b960035cc9bf3`） |
| 网 `La-Lucerna-VOL4-es-ru-web.pdf` | 950,846（< 7 MB） | `cc549a5a212a…`（全值 `cc549a5a212afc4960038720aae88468041562f031b96ea81292c70033fb5551`） |
| text.md `2026-w47-es-ru.text.md` | 52,367（1888 行，未重建） | `ac246f8709d3…`（全值 `ac246f8709d3535958ccebb3b6913800bd3866001de5322358d3ba026f69c42b`） |

- 印/网各 8 页，版面 1462.5 × 2025 pt。
- KIT 已更新：`WEEKLY-KIT.md` L295 记新 SHA（印 `c4732fd0…`、网 `cc549a5a…`），与实测一致。
- `ABSTRACT.txt` 在位（668 B，俄语，含本期真实主题与题数要素）。

## §1 F1 修复复核（P5 ¿Y TÚ? 框 vs EJERCICIOS 分隔线）——已修好，三重实测一致

| 量 | SVG 实测 | 印 PDF 实测（pt，×0.75） | 修复报告值 | 核对 |
|---|---|---|---|---|
| 奶油框 | x=1439.5, y=1277.55, h=321.48，框底 **1599.03** | rect y0=958.16, y1=1199.27（=1599.03px） | 框底 1599.03 | ✓ 一致 |
| EJERCICIOS 分隔线 | y=**1608**，x 88→1862，`#46581f` 2px | HLINE y=1206.00（=1608px），x 66→1396.5 | 1608，未动 | ✓ 一致 |
| 框底距分隔线 | **+8.97px 余量** | 1206.00−1199.27=6.73pt=**8.97px** | +8.97 | ✓ 一致 |
| 末行俄文 `пришлите их.` 基线 | 1592.03（距线 15.97） | rect 底 1198.20pt（=1597.6px，在线之上） | 1592.03 | ✓ 一致 |
| 西语末行基线 | 1449.56 | — | 1449.56 | ✓ 一致 |
| 西→俄块间距 | 1493.23−1449.56=43.67 | — | 43.67 | ✓ 一致 |

- **目视**：`p5-f1-zoom.png`（2× 放大裁图）——框完整收在分隔线之上，`пришлите их.` 在框内完整可读，分隔线与框无交叉，框下留白干净；全页 `p-5.png` 复核：EJERCICIOS 标题行与第 77 题等下方内容未受影响。
- **无回归**：修前 SVG SHA 清单（`scratch-fix-esru-f1/svg-before.sha256`）逐项比对当前 8 个 SVG——**仅 `p5-juventud.svg` 变**（`2396b440…` vs 修前 `2edf705d…`），p1–p4、p6–p8 字节一致。

## §2 文字未变核实（+1 B 之说独立核实，不只信修复报告）

- 印/网 `pdftotext`（plain）各 **53,414 B，逐字节一致**；`-layout` 各 **113,438 B，逐字节一致**。修前 53,413 B → 修后 53,414 B（+1 B）属实。
- **词多重集对照**（印 PDF plain 文本 vs text.md，不区分大小写）：PDF 独有词全部是页脚家具（`vol/la/lucerna/испанский/еженедельник/страница/из/spanish/weekly/4/8` 各 ×8）与纵向刊头字母切分碎片；text.md 独有词 27 个，全部是结构性词（slug、`##` 栏目标题 portada/vida/cultura/deporte/juventud/fondo/lengua、刊头 `CUARTA EDICIÓN / SEMANA DEL 16 AL 22 DE NOVIEMBRE DE 2026`——刊头为矢量路径，pdftotext 提不出）。**无一内容词差异**：文字确未变，+1 B 是 pdftotext 行分组随行距重排所致。
- SVG 文本节点：P5 框内折行不变（西语 4 行、俄文 5 行，实测 y 值与修复报告一致）；其余页 SVG 字节不变（见 §1）。

## §3 全文精读（text.md 1888 行逐行读完）

- **150 题逐题复核**：题号 1–150 连续无缺重；分布 P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38 = 150。答案键逐题对照题面、原文、图表复算，**全部正确**（含：Q25–28 配对 c/b/d/a；Q52–55 配对 c/b/a/d；Q87 45−30=15；Q141–144 配对 c/d/b/a；Q137/138 翻译题与俄文原文一致）。
- **分级**：A2 50 / B1 72 / B2 28（逐题数出，与 run.py 口径一致），合计 150。
- **日期/星期**（`date` 核验，Europe/Madrid）：11月13日周五、16日周一、17日周二、18日周三、19日周四、20日周五、21日周六、22日周日、23日周一、24日周二、27日周五、28日周六、29日周日、9日周一、10日周二、4日周三、5日周四——**文中全部星期表述与日历一致**。
- **算术**：竞选 13→27 日共 15 天 ✓；11月16日距 29 日 13 天 ✓；24–28 日禁发民调共 5 天 ✓；RTVE 45+45+30+30+15+3×10=195 分钟 ✓；PSOE−Vox=15 分钟 ✓；P6 图表条形与数字一致 ✓。
- **范文词数**：P8 H 节范文逐词数出 **97 词**，与所称 97 词一致，落在 80–100 要求内。
- **8 金句**（P7 FRASES DE LA SEMANA）：逐句与原文对照——P1 竞选句、P4 联语句、P2 周四句、P5 首投句、P3 弗拉门戈句、P6 宣布句、P3 歌舞句、P6 民调句，**8/8 逐字一致**，页码标注（1/4/2/5/3/6/3/6）全部正确。
- **图注事实**（抽查外源核实）：UNESCO 于 **2010年11月16日**在内罗毕将弗拉门戈列入非遗（UNESCO 提名文件为内罗毕 2010 年 11 月第五届会议）✓；Sargent《Spanish Dancer》确为 **1880–1881** 年油画（与《El Jaleo》1882 不同作）✓；圣塞西莉亚 11月22日 ✓；Jebulon 青铜票箱 CC0 图注与图片内容一致（箱身 “SUFFRAGE UNIVERSEL” 可见）✓。
- **跨页引用**：目录页码（P2–P8）与各版栏目一致；P1 “см. страницы 2 и 6”、P7 读者来信“承诺转 VOL.5”与 P7 末 “LA PRÓXIMA SEMANA (VOL.5)” 承接一致；P2 “los mejores salen en la página 7” 与 P7 CARTAS 栏一致。
- **语言**：西语重音/性数/变位、俄语讲解逐项读过，无拼写、截断、重复词问题；讲解层所注之词均真实出现于正文。

## §4 8 页逐页看图（150dpi 印 PDF 渲染，`p-1.png`–`p-8.png`）

- P1–P8 逐页目视：无溢出、无重叠、无压页脚、无图注错位。P5 中栏、P3 中栏、P7 下半的空白为栏目内容短造成的版面留白，非缺陷。
- P6 两组图表（RTVE 分钟条形、禁发民调 5/15/1）渲染正确，数字与正文一致。
- P8 答案区 1–150 按页分组齐全，无侵入页脚带。

## §5 全部门禁（`gates-r8.sh` / `gates-r8.log`，2026-11-13 06:07 UTC，全部绿）

| 门 | 工具 | 结果 |
|---|---|---|
| p8 extract | `tools/p8.py extract --total 150` | 150/150，rc=0 |
| p8 compare vs core-es | `tools/p8.py compare --total 150` | **CLEAN**，missing=[] extra=0，keydiff=[137, 138]（已裁定的读者语翻译题差异，同前轮） |
| D5 census | `scratch-d5-plan/mechanism/d5_census.py` | **CENSUS PASS**，rc=0 |
| 几何遮挡自检（仅 sanity check，不当门） | `tools/occlusion_audit.py svg/ --selftest` | selftest OK（6 类 planted 全触发，clean 对照静默），rc=0 |
| 几何遮挡真实审计（门） | `tools/occlusion_audit.py svg/`（不带 `--selftest`） | **0 flags**，rc=0 |
| 框题 | `tools/boxtitle_check.py` | 38 titles / 584 body lines，**0 DEFECT**，0 OBSERVE，0 marginal，rc=0 |
| 溢出 | `tools/spill_sweep.py` | 27 盒 / 149 candidates，**0 SPILL**，149 OBSERVE，rc=0 |
| 页缘 | `tools/pdf_edge_scan.py` | 8 页，**0 TOUCH / 0 NEAR**，rc=0 |
| 冻结复现 | `tools/freeze.py baseline` | **8/8 SVGs byte-identical**，rc=0 |
| 印/网文字层 | `pdftotext` + `cmp`（plain 与 `-layout` 两版） | 各 53,414 B / 113,438 B，**逐字节一致** |

## §6 备注（观察，非问题）

- 本周核心前提为建构情景（11月29日大选、欧冠 Sabah/Viking/AEK 等对阵）：情景内部完全一致（正文、侧栏、赛程表、练习 Q51/Q128 同一口径），与 core-es 一致，前轮已通过；本轮不作改判。
- Q145–149 对话题答案全为 A，属出题单调，不构成错误。

## §7 工作记录与约束遵守

- 只读核对：未改任何生产文件，未 commit/push，未跑 `lint --write`，未 reset/stash/add；只碰 es-ru 一版。
- 磁盘：97G 已用（150G 卷），未触发 ≥100G 停线。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof8-w47-esru/`：本文件、`gates-r8.sh` / `gates-r8.log` / 各门禁日志与 JSON（`p8-extract/ p8-compare/ census/ occlusion[.json] / boxtitle/ spill/ edge/ freeze/`）、`p-1.png`–`p-8.png`、`p5-f1-zoom.png`、`print.txt` / `web.txt`。
