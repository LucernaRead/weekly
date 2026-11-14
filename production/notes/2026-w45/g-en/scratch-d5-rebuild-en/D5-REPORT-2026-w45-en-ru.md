# D5 重建报告 — 2026-w45-en-ru（俄语读者版）

W45 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-en/logs/2026-w45-en-ru/`（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-en/scratch-d5-rebuild-en/logs/2026-w45-en-ru/GATES-SUMMARY.txt`。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w45` → `production/2026-w45/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-en-ru/svglib.py --target en --reader ru --week 2026-w45`（先 `--check` dry-run，mode ru 正确）。装后 `_D5_READER = "ru"`。用 installer 输出的旧分支（Latin AND Cyrillic → Noto Sans，D26；fix-xru 只限 W47，绝未带入本轮）
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（9 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `scratch-prep-p3b/en_textmd_w45.py` 导出（第 0 步已核实：hardcode 仅 W45 刊头 1 行；scratch 试跑 vs issues 已发版 BYTE-IDENTICAL）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `style-port-en/MANIFEST-W45-D1.md` 逐字节一致（16707935 字节，sha256 `99643b61…`）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF **非空字符差 0**，仅空格数浮动（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，零词字符丢失）。
- 修前普查 `d5_census.py`：D5 违规 **704（拉丁 398，西里尔 306）**（>0，符合装机前提）。
- 基线 P8 口径：noted **78/150**（CLEAN（core 78 → 本版 78））。

## 三、缺陷与修法（run1 → run2）

run1 共 2 项缺陷，均为既有溢出（基线同值），与 D5 字体加宽无关。修法只动框高，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | spill | P2 DID YOU KNOW 框 “bags.” | 框底 BELOW +12.74px（既有缺陷，基线同值） | `content12.py:193` 框高公式尾数 +14→**+34** |
| 2 | spill | P7 读者园地框 “опубликуем полученные письма.” | 框底 BELOW +10.00px（既有缺陷，基线 spill_sweep 同为 2 SPILL；框 (989.0, 1878.0, 873.0, 300.0)，底 2178.0；编者按段 `content7.py:115`，20pt sans） | `content7.py` 框高 300→**316**（`p.rect(rx, by7 + 8, rw, 316, fill=BOX)`；距 NEXT WEEK 框 24px，修复后余 8px） |

P8 变化：200 → 200 行，距页脚线余量 32.7 → 32.7 px（正，无溢出）。

## 四、门禁（run2，全套 16 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0，`noto_sans_elements=802`（ru-reader 须 >0 ✓） |
| 4 render | RC=0，印 PDF 16516502 B |
| 5 webpdf | RC=0，网 PDF 2190261 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 78/150 |
| 8 p8 compare | **CLEAN**（core 78 noted vs 本版 78 noted；keydiff=[137, 138, 139, 140, 150]） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 227，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（99 OBSERVE） |
| 12 boxtitle | 0 DEFECT（38 titles, 185 body lines；以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 200 → 200，slack 32.7 → 32.7） |
| 15a 文字层 print=web | 字符多重集差 **0**；text.md BYTE-IDENTICAL |
| 16 census_quotes | 0 defective |
| D18 刊头 | gap **149.9px** PASS |
| 17 家族 gates.py | en 家无 gates.py |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）

- 印 PDF：`The-Lucerna-VOL2-en-ru.pdf`，**16516502 字节**，
  SHA-256 `11c3472bace30268fe3b103e40ddd534e252dea231c7376850a05f8e0e2db973`
  （D5 前基线 16707935 字节）。
- 网 PDF：`2026-w45-en-ru.web.pdf`，**2190261 字节**，
  SHA-256 `fe22efd81faa61d3fe2c89a1a1dcd703d16bd3c62c406a540a7b18e334201551`。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**（50295 字节，SHA-256 `8d6999cebcfd136401b38cdc146ee8038a8741ed837c5574f2ac21cf4464c488`）。
- 练习总量仍为 **150 题**，与 core 逐题一致。

## 六、KIT

- `production/2026-w45/2026-w45-en-ru/WEEKLY-KIT.md`：§一 pin 更新；文末追加 §十三。