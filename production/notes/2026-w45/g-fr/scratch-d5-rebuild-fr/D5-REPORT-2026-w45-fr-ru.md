# D5 重建报告 — 2026-w45-fr-ru（俄语读者版）

W45 fr 家 D5 + §1.1 合并重建（pre-D1 新样式：D1 修复 + D5 一次渲完）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-fr/logs/2026-w45-fr-ru/`（`GATES-SUMMARY-run3.txt` 为门禁总表；`GATES-SUMMARY-run1.txt` 为修前总表）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core fr --week 2026-w45 --i-understand-this-writes-production` → `production/2026-w45/core-fr/svglib.py` +95/−3 行，`_D5_READER = "latin"`（L100）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-fr-ru/svglib.py --target fr --reader ru --week 2026-w45`（先 `--check` dry-run，RC=0，mode ru 正确）（旧分支 `_D5_READER == "ru"`，D26；fix-xru 不带入三周）。装后 `_D5_READER = "ru"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（`U+201C` 命中）。
- D1 组装：patched svglib 为 fanout D1 版（与生产版 svglib 的 diff 恰为 D1 hunk 28 行）；content*.py/bslib4.py 与生产版逐字节相同。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `scratch-prep-p3b/export_w45_fanout_fixed.py` 导出（第 0 步已核实：fr-es 试跑 12 行差 = 6 条 gloss 行泄漏修复差，fr-zh-cn BYTE-IDENTICAL）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **463**、西里尔 331、弯引号总数 0（>0，符合装机前提）。
- 基线 P8 口径：noted **91/150**（core-fr 与 10 读者版同一集合，含 [108]）；compare 全 CLEAN，keydiff `[135, 150]`。
- 基线 D18 刊头间距 174.9px；基线 D37 副刊头行余量 42.6pt。

## 三、缺陷与修法（run1 → run3）

run1 缺陷全部为 D5 字体加宽引起（拉丁粗体在 Newsreader 下比 Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值 +12.68px）。修法只动字号 / 盒高，**未动任何文字内容**。共 2 项：

run3 追加：ET VOUS 俄文 gloss 20→19（run2 的 spill 修复把盒底推到 1612.6，越过 dy 横线 y=1598，LINEX；gloss 由 4 行变 3 行，盒底收回 1583.6，距线 14.4px）。

| 门 | 内容 | 修法 |
|---|---|---|
| spill | `sh = 62 + sum(...) + 14` | content12.py:204 14→**30** |
| box标题/刊头 | `ET VOUS 俄文 gloss（eh 公式 + 绘制行）` | content12.py:213 20→**19** |

P8 变化：206 -> 207 行，距页脚线余量 38.5 -> 38.5 px（正，无溢出）。

## 四、门禁（run3，全套 16 门 + D18 + D37，ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0 |
| 5 webpdf | RC=0，网 PDF 1467372 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 97 of 150 |
| 8 p8 compare | PASS，CLEAN（keydiff=[135, 150]，预期读者语键） |
| 9 freeze baseline | 8/8 |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 228，预期 D5 run-split；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL |
| 12 boxtitle | 0 DEFECT（backup 已补基线 svg 为真对照） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 206 -> 207，slack 38.5 -> 38.5） |
| 15 文字层 print=web + text.md | 字符多重集差 **0**；text.md BYTE-IDENTICAL vs issued |
| 16 census_quotes | 0 defective |
| D18 刊头间距 | PASS，151.5px |
| D37 副刊头行 | PASS，余量 37.7pt |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL2-fr-ru.pdf`，**9,039,620 字节**，SHA-256 `5c2bfa231e1076b08ecc9945861713fc74bb31ed1712f99052571231ffd1af5a`。
- 网 PDF：`2026-w45-fr-ru.web.pdf`，**1,467,372 字节**，SHA-256 `90c8cf32e55fde99f7188d330682d6d71dfafa69133b9c2ba63f6c234921e80e`（网 PDF 字节跨次运行不确定——closer 须拷 builder 原件，绝不重跑 webpdf）。
- text.md：`2026-w45-fr-ru.text.md`，**51,877 字节**，SHA-256 `3631ca0354bd65b4c554c6f15b572572815dcae2e040928d827023c999f3b320`（BYTE-IDENTICAL vs issued）。
- 练习总量仍为 **150 题**。

## 六、KIT

- `production/2026-w45/2026-w45-fr-ru/WEEKLY-KIT.md`：文末追加 D5 节（§14：装机、修复、终门禁 ALL-GREEN、新交付物 pins）。§14/§15 原 round-5 VOL3 pins 未动（其 pin 的是原始交付物文件名；D5 pins 在新 D5 节内）。
