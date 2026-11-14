# D5 重建报告 — 2026-w45-it-ru（俄语读者版）

W45 it 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
施工分工：builder v1 完成第 0–5 步、run1 全部门禁、全部字号修复与 run2 前 6 版（zh-cn/de/en/es/fr/ja）；builder v2（接替 v1，v1 被 restart drain 杀死）完成 run2 余下 5 版（ko/nl/pt/ru/zh-tw）、KIT 更新与本报告。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-it/logs/2026-w45-it-ru/`（`GATES-SUMMARY.txt` 为 run2 门禁总表，`run1/GATES-SUMMARY.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-it/scratch-d5-rebuild-it/logs/2026-w45-it-ru/GATES-SUMMARY.txt`（与 scratch run2 总表逐字节一致，`cmp` 已验）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core it --week 2026-w45` → `production/2026-w45/core-it/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-it-ru/svglib.py --target it --reader ru --week 2026-w45`（先 `--check` dry-run，mode=ru 正确）。装后 `_D5_READER = "ru"`。ru 读者版用安装器旧分支（拉丁 AND 西里尔 → Noto Sans，D26；fix-xru 只限 W47，未带入）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `hidden_files/style-port-it/export_it.py` 导出（第 0 步已核实：scratch 试跑 vs issues 已发版 BYTE-IDENTICAL，11/11）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 6,685,485 字节（sha256 `b8f42aa01ecc…`），与 fanout 原件逐字节一致；网 PDF 681,934 字节。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF 差 **0**。
- 修前普查 `d5_census.py`：D5 违规 **593**（>0，符合装机前提）。
- 基线 P8 口径：noted **150/150**。

## 三、缺陷与修法（run1 → run2）

run1 即 **ALL-GREEN**，无缺陷、无修复。P8 变化：209→213 行（D5 换字体后答案行多绕 4 行），距页脚线余量 56.6 → 56.6 px（正，无溢出）。

- ru 读者版特记：`Noto Sans` 元素 **769**（>0，门 3 必需）；P8 行数 209→213（D5 换字体后答案行多绕 4 行），页脚余量仍 56.6px 为正，无溢出。

## 四、门禁（run2，全套 17 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0；`Noto Sans` 元素 769（>0） |
| 4 render | RC=0，印 PDF 6,405,908 B（fix1；run2 为 6,405,907 B） |
| 5 webpdf | RC=0，网 PDF 799,413 B（fix1；run2 为 799,370 B；< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**，keydiff=[137, 138, 139]，missing=[]，extra=[] |
| 9 freeze baseline | 8/8（patched 重建复现自身 SVG） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 171（fix1；run2 为 169），run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 spills |
| 12 boxtitle | 0 defects |
| 13 edge | 0 touches，0 nears |
| 14 creambox | 0 defects；P8 行数 209->214（fix1；run2 为 209->213），页脚余量 56.6 px |
| 15 text layer | print=web 差 0；web-vs-issues +10/-2（F3 全式新增字符，见 §六） |
| 15a text.md | 导出 RC=0，diff = 4 行（137/138/140 标签 + 139 标签与答案全式，F1+F3 修复，D33），其余逐字节相同 |
| 16 census_quotes | 0 defective |
| 18 masthead（D18） | slogan–date 间隙 103.4px，PASS（>0） |

**结论：run2 ALL-GREEN；fix1 除 15/15a 外全绿（见 §六）。**

## 五、新交付物 / KIT

- 印 PDF：`scratch-2026-w45-it/fix/2026-w45-it-ru/The-Lucerna-VOL3.pdf`（fix1 原件）— 6,405,908 字节，sha256 `5f8f738b63c721918ba5bfd9a284b32f162d936b32d676d9e5fa57cfc5589c0d`（文件名 VOL3 为 render.py 既有命名，基线同名，刊头 VOL.2 无误；run2 为 6,405,907 B，`825f0b9c5828…`）。
- 网 PDF：`scratch-2026-w45-it/fix/2026-w45-it-ru/2026-w45-it-ru.web.pdf`（fix1 原件）— 799,413 字节，sha256 `600811a1fab914cde7e7a966d575062d02abb0c814dccdbbac8223d903c0ae4f`。网 PDF 跨次运行字节不确定，**closer 须拷 fix 原件，绝不重跑 webpdf**；KIT 记录的 fix SHA 即交付值（run2 为 799,370 B，`4d1677735f8a…`）。
- text.md：`scratch-2026-w45-it/fix/2026-w45-it-ru/2026-w45-it-ru.text.md.new`（fix1 导出）— 66,641 字节，sha256 `b9a211a93e748d0ed0d80e267e9323a40956fe809ae5f00039d07d8cce638e54`，与 issues 已发版 diff = 4 行（137/138/140 标签 + 139 标签与答案全式，F1+F3 修复，D33），其余逐字节相同。
- KIT：`production/2026-w45/2026-w45-it-ru/WEEKLY-KIT.md` 针脚行已更新为上述新值 + 文末 D5 节（§17）。

## 六、F1–F4 修复（fix1，2026-11-14，D33）

- F1：`production/2026-w45/2026-w45-it-ru/content8.py:69/71/73/75`，`f.ex` 第 2 参数 "翻译" → "Перевод"（4 行）。基线核实：已发版 text.md 4 行均为 `[翻译]`，先存缺陷、非 D5 回归。
- F3：同文件 `:73`，E139 答案 "«Фиорентина» — «Ювентус» в воскр. веч." → 全式 "«Фиорентина» — «Ювентус» в воскресенье вечером"（同文件 28 行即有此全式）。基线核实：已发版 text.md E139 答案行即为缩写片段，先存缺陷、非 D5 回归。改后核对 E139 提示/答案对应正确；全式未致溢出（门 14 defects=0、门 6 flags=0、页脚余量仍 56.6px），无需协调员另定措辞。
- 修复后在 `scratch-2026-w45-it/fix/2026-w45-it-ru/` 全量重建 + 全部门禁重跑（`gates_fix.py`，tag fix1）：TOTAL 150、p8 150/150 CLEAN keydiff=[137, 138, 139]；P8 行数 209->214（fix1；run2 为 209->213——全式答案多绕 1 行，良性，余量不变）；freeze-diff 新增拉丁 strings 171（run2 为 169）；刊头间隙 103.4px PASS。
- fix1 门禁 verdict：FAILURES: ['15-textlayer', '15a-textmd']——两门红均属预期内（均以已发版为对照，内容修复必然改动对照）：门 15 print-vs-web 差 0，web-vs-issues +10/-2，字符多重集差逐字核对即 F3 全式（新增 {е×4, р, о, с, м, н, ь}、去掉句点 ×2），无其他字符变化；门 15a text.md 与已发版差恰好为 4 行（137/138/140 标签 + 139 标签与答案全式），其余逐字节相同。
- 新交付物（fix1 原件，§五已更新，KIT pin 已更新）：印 PDF 6,405,908 B，sha256 `5f8f738b63c721918ba5bfd9a284b32f162d936b32d676d9e5fa57cfc5589c0d`；网 PDF 799,413 B，sha256 `600811a1fab914cde7e7a966d575062d02abb0c814dccdbbac8223d903c0ae4f`；text.md 66,641 B，sha256 `b9a211a93e748d0ed0d80e267e9323a40956fe809ae5f00039d07d8cce638e54`。门禁总表复本（D29）：`production/notes/2026-w45/g-it/scratch-d5-rebuild-it/logs/2026-w45-it-ru/GATES-SUMMARY.txt` 已换为 fix1 总表。
