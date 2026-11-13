# GATE-LOG — 2026-W47 de-en fix2（重建 6，2026-11-11）

构建：`TMPDIR=<scratch>/tmp tools/venv/bin/python build_edition.py en`
（解释器 `~/workspace/weekly-git/tools/venv/bin/python`；
日志 `build-fix2b.log`；另 `measure-fix2.log` 24/24 先行通过）。
重建 5（`build-fix2.log`，手写 `'news'` 版）门禁行与重建 6 **逐项一致**
（diff 全同），唯一差异是 freeze_direct 源层级（重建 5 FAIL、
重建 6 PASS，见下）与网页 PDF 2 B。

## 门禁总表（build_edition.py 输出，ALL GATES PASS）

| 门 | 结果 |
|---|---|
| run.py exit 0 / 0 FLOW OVERFLOW / 0 HEAD TOO WIDE / TOTAL 150 | PASS |
| render.py exit 0，印版 10,966,410 B | PASS |
| webpdf exit 0，网页 1,597,904 B < 7 MB | PASS |
| verify.py TOTAL 150，编号连续，SVG 重跑字节一致，SOP 1.1 样式审计 True，verbatim OK，P8 字号底线 True，17 禁词全无 | PASS |
| occlusion_audit.py 自检通过（6 类 planted 全触发，clean 对照静默） | **0 flags** PASS |
| p8.py extract | 150/150 PASS |
| p8.py compare vs core | **CLEAN**，missing=[]，extra=0，keydiff=[137, 138, 139, 150] PASS |
| freeze.py diff exit 0 | 新增 CJK 7 个，全为 U+3000（P2–P8 各 1，P1 0）PASS |
| print/web 文字层（pdftotext） | default 50,433B / 50,433B，词多重集相同；-raw 归一化 49,277B 双方完全相同 PASS |
| chips（rx="2.7" 矩形） | 逐页 10/15/18/15/18/18/12/35，TOTAL 141；P8 A2 22 / B1 13 / B2 0 PASS |
| text export（源稿导出） | exit 0，49,665 B，48,034 字符，591 条目，150 题 PASS |
| P8 最小字号（PyMuPDF） | **9.94pt** ≥ 9.75pt 底线 PASS |
| measure.py en | **24/24 PASS，0 FAIL** |

流向末端（build.log）：P1-headline 1554、P3 col3 1643.19、P5-ex 2441（= core）、
P7-A2 1278 / B1 1342 / B2 1306、P7 image ends 1541.83、**P7 col3 ends 1534.38**、
P8-battery 1409、P8-keys 2481（底边 2560，余 79px）。与 fix1 逐项一致。

## keydiff 逐项说明（[137, 138, 139, 150]，全部预期内）

同 fix1：Q137–139 E 组正向翻译题（键译成英文），Q150 开放写作题标签；
Q140 不在 keydiff 中（反向题，键为德文目标语句，正确）。

## keycheck（独立，keycheck-150.json）

- REG 150 条 vs P8 抽取键：**149/150 精确**；唯一非精确 Q150（抽取器把 REG 键
  "Open task — follow the points in the writing box" 截断为 "Open task"，预期内，
  Q150 已在 keydiff 中）。D2 所在 Q67 键 `B` = 提取 `B`（只改了键注引号的
  **渲染字体**，字符与键值均未动）。

## freeze 直接冻结（freeze_direct.py，freeze-direct.json）

- 渲染级：**8/8 PASS**，frozen 数 / sha8 与 rebuild 3、fix1 逐字节一致：
  P1 147 `083e2a2a` / P2 163 `689045ad` / P3 195 `fc88f676` /
  P4 166 `df1bebf7` / P5 173 `86fa4421` / P6 175 `2bbe05f9` /
  P7 150 `b7aa0771` / P8 186 `57e118e7`。
  （D1/D2 均不在冻结交集内：是英文独有串；冻结指纹不动正是"未动德文正文"的证据。）
- 源层级：**PASS**（unaccounted removed 0 / added 0；core 2556 字面量，
  版 2570，removed 520 / added 534 全部记账）。
  重建 5 在此 FAIL（`'news'` ×3 无账），重建 6 以递归派生改写后 PASS——
  新增字面量只剩 `“`（×2，tr D1/D2 值的子串）与 `serif`（×2，tr tbh
  公式串的子串）、`sans`（×2，chipfix 注入记账）。

## 像素复测（quote_pixel.py，quote-pixel-fix2.log；方法见 FIX-LOG §4）

| 处 | 修前（proof2，200dpi） | 修后（400dpi 窄带） | 门 ≤0.2em |
|---|---|---|---|
| D1 闭引号（20pt） | 9.72pt = 0.49em | **0.18pt = 0.01em**（后隙 1.80pt） | PASS |
| D2 闭引号（9.94pt） | 7.20pt = 0.72em | **0.72pt = 0.07em**（后隙 0.72pt） | PASS |
| 对照 P8 对话（同法） | 1.80pt = 0.12em | 1.26pt = 0.09em | — |

- 200dpi 全行带复核：D1 读 2.16pt = 0.11em（合并列读法，落在对照带内）。
- 字体核实：两处 U+201C 的 PDF span 字体均为 Newsreader；SVG 中 P8 的
  3 个 U+201C 全为 Newsreader，其中 2 个为独占 `<text>“</text>` run。

## 弯标点全扫（U+201C/U+201D/U+2019；SVG + text.md + 双 PDF 文字层）

| 位置 | U+201D | U+201C | U+201E | U+2019 |
|---|---|---|---|---|
| P1–P8 SVG（合计） | 0 | 35 | 35 | 0 |
| text.md | 0 | 35 | 35 | 0 |
| 印版文字层 | 0 | 35 | 35 | 0 |
| 网页文字层 | 0 | 35 | 35 | 0 |

- **全版 U+201D = 0，U+2019 = 0**；U+201C = U+201E = 35（P1 5、P5 6、
  P7 21、P8 3），与 fix1 逐项一致——字符一字未动。
- 方案否决记录（ink_test.py，PIL 墨宽预试）：ASCII `"` 在 sans 下
  D1 0.77pt（0.038em）但 D2 −0.31pt（墨迹相触），且字形与德式 „ 不配，
  否决；Newsreader U+201C 预试 D1 0.77pt / D2 0.68pt，均为正间隙，取用。

## 盒间隙核查（creambox）

- 精炼版 creambox_check.py（溢出带 = 底边外 0–8px，8 页全扫）：**NO OVERFLOW**，
  exit 0。
- P7 工具盒（creambox.py，+45px 窗口，creambox-after-p7.log）：
  盒 y=330 底 **799.9**，末基线 783.9，间隙 **+16.0**
  （`Es ist fraglich, ob ... = Whether … is open`），与 fix1 结论一致，未回退。

## 盒标题（boxtitle）

- `boxtitle.py en`（共享 tr_en.py）：**7/7**——DIE STILLE WOCHE 394.6、
  WEIHNACHTSWÖRTER Words 359.9、DER TIPP 262.5、ADVENTSWÖRTER 397.9、
  DER WERKZEUGKASTEN 382.9、LESERBRIEFE 352.8、NOCH EIN WORT 366.1
  （预算 400.5px），与 fix1/proof2 逐项一致。
- 发货 SVG 实测同值（NOCH EIN WORT 按其 22pt 计为 366.1）。

## Q34 与 content12 不回退

- 新题干 `"Am Montag öffnet in Köln der erste ___."`：源码 1×、text.md 1×；
  旧题干 `"Am Montag öffnen in Köln die ersten ___."` 源码 0×、text.md 0×。
  P3 冻结 sha `fc88f676` 不变。
- content12.py:58 未动（`Deutschland hat nach vier Spielen ___ Punkte.`）。

## 目视

- P8 全页 100 dpi（render/print-p8.png）：H 写作框、MUSTER、答案键、页脚
  均在位，无重叠、无越线；D1 行读作 `„My week in November“.`，无白洞。
- P8 H 写作框 200 dpi 裁切（render/crop-p8-hbox-d1-200dpi.png）：D1 引号
  贴紧 `November`，与同页 `«Leserbriefe»` 的 `»` 紧贴程度一致。
- P8 键区 200 dpi 裁切（render/crop-p8-key67-d2-200dpi.png）：`67. B
  (The 1903 calendar: „Im Lande des Christkinds“)` 引号贴紧，键 B 清晰。
