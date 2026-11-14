# D5 重建报告 — 2026-w45-en-es（西班牙语读者版）

W45 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-en/logs/2026-w45-en-es/`（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-en/scratch-d5-rebuild-en/logs/2026-w45-en-es/GATES-SUMMARY.txt`。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w45` → `production/2026-w45/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-en-es/svglib.py --target en --reader es --week 2026-w45`（先 `--check` dry-run，mode latin 正确）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（9 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `scratch-prep-p3b/en_textmd_w45.py` 导出（第 0 步已核实：hardcode 仅 W45 刊头 1 行；scratch 试跑 vs issues 已发版 BYTE-IDENTICAL）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `style-port-en/MANIFEST-W45-D1.md` 逐字节一致（16770209 字节，sha256 `1d675a37…`）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF **非空字符差 0**，仅空格数浮动（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，零词字符丢失）。
- 修前普查 `d5_census.py`：D5 违规 **520**（>0，符合装机前提）。
- 基线 P8 口径：noted **78/150**（CLEAN；R1 落盘后重跑，D32；落盘前为 SHORT missing=[150] 抽取器盲区，见 §四）。

## 三、缺陷与修法（run1 → run2）

run1 共 9 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Noto Sans CJK 下比 Newsreader 宽），另有 P2 框溢出 1 项为既有缺陷（基线同值）。修法只动字号与框高，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | “TRY IT NOW　Practica al momento” | 25pt 宽 439.1px，超栏 16.6 | `content12.py:47` 25→**24**（421.5，余 1.0px） |
| 2 | head_check | “READ THE CHART　Lee el gráfico” | 25pt 宽 430.4px，超 7.9 | `content56.py:109` 25→**24**（413.1） |
| 3 | head_check | P7 “THE TOOLBOX　Herramientas” | 27pt 宽 423.9px，超 1.4 | `content7.py:48` 27→**25**（392.5） |
| 4 | occlusion | P1 暗带标题与副标 “Martes electoral” | 重叠 63.0px | 暗带标题 46→**42**（副标保持 27pt，修复后 gap +72.9px） |
| 5 | spill | P2 DID YOU KNOW 框 “bags.” | 框底 BELOW +12.74px（既有缺陷，基线同值） | `content12.py:193` 框高公式尾数 +14→**+34** |
| 6 | boxtitle / creambox | “THE WEEK IN NUMBERS　En cifras” | 右溢 +21.5px | tsize 23→**21** |
| 7 | boxtitle / creambox | “WHY MADRID?　¿Por qué Madrid?” | 右溢 +13.1px | tsize 23→**21** |
| 8 | boxtitle / creambox | “SUNDAY, NOVEMBER 8　Domingo” | 右溢 +2.9px | tsize 23→**21** |
| 9 | boxtitle / creambox | “TOO CLOSE TO CALL　Muy reñido” | 右溢 +5.2px | tsize 23→**21** |

P8 变化：198 → 196 行，距页脚线余量 32.7 → 33.7 px（正，无溢出）。

## 四、门禁（run2，全套 16 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 16272481 B |
| 5 webpdf | RC=0，网 PDF 1959081 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 78/150（R1 落盘后重跑，D32） |
| 8 p8 compare | **PASS（R1 landed, D32；extract core 78 / ed 78，compare CLEAN，exit 0，keydiff=[137, 138, 139, 140, 150]）** |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 340，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（93 OBSERVE） |
| 12 boxtitle | 0 DEFECT（30 titles, 170 body lines；以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 198 → 196，slack 32.7 → 33.7） |
| 15a 文字层 print=web | 字符多重集差 **0**；text.md BYTE-IDENTICAL |
| 16 census_quotes | 0 defective |
| D18 刊头 | gap **119.6px** PASS |
| 17 家族 gates.py | en 家无 gates.py |

**OVERALL: 16/16 ALL-GREEN + D18 PASS（g8 经 R1 落盘后重跑 PASS，D32）。**

g8 p8 compare PASS（R1 landed, D32；extract core 78 / ed 78，compare CLEAN，exit 0，keydiff=[137, 138, 139, 140, 150]；patched 与基线重跑均为 CLEAN）。落盘前为 FAIL RC=1，SHORT missing=[150]：150 号注释在 SVG 与文字层中全文印出（“150. Pregunta abierta: véanse los puntos en el recuadro de redacción; el modelo está en el recuadro de esta página (Se puntúa por puntos)”），为冒号式，`tools/p8.py` `detect_note()` 落盘前只认括号式 `key (note)` 与破折号式 `key — note`；R1 冒号式规则（D32）落盘后 [150] 以 `method='colon'` 检出。已发基线重跑同样 CLEAN，印 PDF 与清单字节精确一致。未改内容迁就抽取器；D31 adjudication 已转为真 PASS。

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）

- 印 PDF：`The-Lucerna-VOL2-en-es.pdf`，**16272481 字节**，
  SHA-256 `1779152f27b423aa5a82d28fc24617f57674a715c07f596a72e8b990dcb1f366`
  （D5 前基线 16770209 字节）。
- 网 PDF：`2026-w45-en-es.web.pdf`，**1959081 字节**，
  SHA-256 `0356ee55b724a48d8eee80a9c38ae3deeb15c56b7aece9ec1f3e3f25f31b63b7`。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**（43634 字节，SHA-256 `e132efb7d1680d588c6c30c291b8da8e79188939c6f1fdad94cfc7a646efa1d8`）。
- 练习总量仍为 **150 题**，与 core 逐题一致。

## 六、KIT

- `production/2026-w45/2026-w45-en-es/WEEKLY-KIT.md`：§一 pin 更新；文末追加 §十三。