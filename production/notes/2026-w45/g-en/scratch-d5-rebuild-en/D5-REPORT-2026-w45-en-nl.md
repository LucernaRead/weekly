# D5 重建报告 — 2026-w45-en-nl（荷兰语读者版）

W45 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-en/logs/2026-w45-en-nl/`（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-en/scratch-d5-rebuild-en/logs/2026-w45-en-nl/GATES-SUMMARY.txt`。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w45` → `production/2026-w45/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-en-nl/svglib.py --target en --reader nl --week 2026-w45`（先 `--check` dry-run，mode latin 正确）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（9 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `scratch-prep-p3b/en_textmd_w45.py` 导出（第 0 步已核实：hardcode 仅 W45 刊头 1 行；scratch 试跑 vs issues 已发版 BYTE-IDENTICAL）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `style-port-en/MANIFEST-W45-D1.md` 逐字节一致（16772038 字节，sha256 `c3096f1f…`）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF **非空字符差 0**，仅空格数浮动（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，零词字符丢失）。
- 修前普查 `d5_census.py`：D5 违规 **546**（>0，符合装机前提）。
- 基线 P8 口径：noted **150/150**（EXTRA_ONLY（core 78 → 本版 150））。

## 三、缺陷与修法（run1 → run2）

run1 共 6 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Noto Sans CJK 下比 Newsreader 宽），另有 P2 框溢出 1 项为既有缺陷（基线同值）。修法只动字号与框高，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | `content8.py:43` “B　MULTIPLE CHOICE　Meerkeuze” | 24pt 宽 441.1px，超栏 18.6 | 24→**22**（23pt 仍 422.7px） |
| 2 | occlusion | P1 暗带标题与副标 “VERKIEZINGSDAG” | 重叠 115.8px | 暗带标题 46→**42**（副标保持 27pt，修复后 gap +20.1px） |
| 3 | spill | P2 DID YOU KNOW 框 “bags.” | 框底 BELOW +12.74px（既有缺陷，基线同值） | `content12.py:193` 框高公式尾数 +14→**+34** |
| 4 | boxtitle / creambox | “AT HOME THIS WEEK　Thuis kijken” | 右溢 +25.9px | tsize 23→**21** |
| 5 | boxtitle / creambox | “THE CAT'S HAT　De hoed van de kat” | 右溢 +19.7px | tsize 23→**21** |
| 6 | boxtitle / creambox | “WHY MADRID?　Waarom Madrid?” | 右溢 +10.1px | tsize 23→**21** |

P8 变化：217 → 219 行，距页脚线余量 34.8 → 34.9 px（正，无溢出）。

## 四、门禁（run2，全套 16 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 16269866 B |
| 5 webpdf | RC=0，网 PDF 1956471 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **EXTRA_ONLY**（core 78 noted vs 本版 150 noted，extra_count=72，裁定接受；keydiff=[137, 138, 139, 140, 150]） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 374，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（95 OBSERVE） |
| 12 boxtitle | 0 DEFECT（32 titles, 170 body lines；以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 217 → 219，slack 34.8 → 34.9） |
| 15a 文字层 print=web | 字符多重集差 **0**；text.md BYTE-IDENTICAL |
| 16 census_quotes | 0 defective |
| D18 刊头 | gap **110.7px** PASS |
| 17 家族 gates.py | en 家无 gates.py |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）

- 印 PDF：`The-Lucerna-VOL2-en-nl.pdf`，**16269866 字节**，
  SHA-256 `849ad5b20a25319e4a4da8b119ef6a5ec6482bf03d0855540590550ee0a2fa3f`
  （D5 前基线 16772038 字节）。
- 网 PDF：`2026-w45-en-nl.web.pdf`，**1956471 字节**，
  SHA-256 `705572ca1318c4c3b013a0fbec8db2f01a6f81273bf19b2093246640a3c7a702`。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**（43361 字节，SHA-256 `091e1581fd9e5e8e615d6d3ab598a7b06a80cca4e881e6556601d968fbd88c1f`）。
- 练习总量仍为 **150 题**，与 core 逐题一致。

## 六、KIT

- `production/2026-w45/2026-w45-en-nl/WEEKLY-KIT.md`：§12 表 + §13 pin 更新；文末追加 §14。