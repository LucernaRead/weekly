# D5 重建报告 — 2026-w45-it-en（英语读者版）

W45 it 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
施工分工：builder v1 完成第 0–5 步、run1 全部门禁、全部字号修复与 run2 前 6 版（zh-cn/de/en/es/fr/ja）；builder v2（接替 v1，v1 被 restart drain 杀死）完成 run2 余下 5 版（ko/nl/pt/ru/zh-tw）、KIT 更新与本报告。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-it/logs/2026-w45-it-en/`（`GATES-SUMMARY.txt` 为 run2 门禁总表，`run1/GATES-SUMMARY.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-it/scratch-d5-rebuild-it/logs/2026-w45-it-en/GATES-SUMMARY.txt`（与 scratch run2 总表逐字节一致，`cmp` 已验）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core it --week 2026-w45` → `production/2026-w45/core-it/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-it-en/svglib.py --target it --reader en --week 2026-w45`（先 `--check` dry-run，mode=latin 正确）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `hidden_files/style-port-it/export_it.py` 导出（第 0 步已核实：scratch 试跑 vs issues 已发版 BYTE-IDENTICAL，11/11）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 6,625,096 字节（sha256 `8fa5bc368d3d…`），与 fanout 原件逐字节一致；网 PDF 635,728 字节。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF 差 **0**。
- 修前普查 `d5_census.py`：D5 违规 **488**（>0，符合装机前提）。
- 基线 P8 口径：noted **150/150**。

## 三、缺陷与修法（run1 → run2）

run1 共 3 项，全部为 D5 字体加宽引起（讲解层粗体在 Noto Sans CJK 下比 Newsreader 宽，框标题右溢；P1 溢出的标题同时造成 occlusion 墨迹重叠）。修法只动字号，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | 12 boxtitle / 14 creambox | P1 框标题 `Numbers` | 右溢 +30.6px | `content12.py:50` 框标题 tsize →**21** |
| 2 | 12 boxtitle / 14 creambox | P1 `IN QUESTO NUMERO　CONTENTS` | 右溢 +40.2px | `content12.py:91` 24→**21**pt |
| 3 | 12 boxtitle / 14 creambox | P7 `ERRORI TIPICI　Common mistakes` | 右溢 +9.8px | `content7.py:73` 23→**22**pt |

P8 变化：209->209 行，距页脚线余量 59.6 → 59.6 px（正，无溢出）。

## 四、门禁（run2，全套 17 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 6,091,558 B |
| 5 webpdf | RC=0，网 PDF 561,965 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**，keydiff=[137, 138, 139]，missing=[]，extra=[] |
| 9 freeze baseline | 8/8（patched 重建复现自身 SVG） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 240，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 spills |
| 12 boxtitle | 0 defects |
| 13 edge | 0 touches，0 nears |
| 14 creambox | 0 defects；P8 行数 209->209，页脚余量 59.6 px |
| 15 text layer | print=web=issues，字符多重集差 0 |
| 15a text.md | 导出 RC=0，diff = 4 行标签（F1 修复，D33），其余逐字节相同 |
| 16 census_quotes | 0 defective |
| 18 masthead（D18） | slogan–date 间隙 103.4px，PASS（>0） |

**结论：run2 ALL-GREEN。**

## 五、新交付物 / KIT

- 印 PDF：`scratch-2026-w45-it/patched/2026-w45-it-en/The-Lucerna-VOL3.pdf` — 6,091,558 字节，sha256 `c0513f07ebadb79d39ce11a26ee1d54451a41a91b0f1ff2405db82dfcd69160b`（文件名 VOL3 为 render.py 既有命名，基线同名，刊头 VOL.2 无误）。
- 网 PDF：`scratch-2026-w45-it/patched/2026-w45-it-en/2026-w45-it-en.web.pdf` — 561,965 字节，sha256 `01035b0d500c7c261e717ccfa6315dad3e41144a7132077b846d9b745b955210`。网 PDF 跨次运行字节不确定，**closer 须拷 builder 原件，绝不重跑 webpdf**；KIT 记录的 builder SHA 即交付值。
- text.md：`scratch-2026-w45-it/fix/2026-w45-it-en/2026-w45-it-en.text.md.new`（fix1 导出）— 55,137 字节，sha256 `cf0b41ad6bc186dd80255a4fa2c04b9128a98fe0ef276e9b0f4f734528704ee9`，与 issues 已发版 diff = 4 行标签（F1 修复，D33），其余逐字节相同。
- KIT：`production/2026-w45/2026-w45-it-en/WEEKLY-KIT.md` 针脚行已更新为上述新值 + 文末 D5 节（文末 “D5 rebuild” 节）。

## 六、F1–F4 修复（fix1，2026-11-14，D33）

- F1：`production/2026-w45/2026-w45-it-en/content8.py:69/71/73/75`，`f.ex` 第 2 参数 "翻译" → "Translation"（4 行）。基线核实：已发版 text.md 4 行均为 `[翻译]`、基线 text.md 字节相同，先存缺陷、非 D5 回归。core-it/zh-cn 同处 "翻译" 正确，未动。
- 修复后在 `scratch-2026-w45-it/fix/2026-w45-it-en/` 重建（`gates_fix.py`，tag fix1；production 改动源 + patched 其余文件原样）：印 PDF **字节与 builder run2 完全一致**（6,091,558 B，sha256 `c0513f07ebad…`）；其余 16 门 + D18 全绿（TOTAL 150、p8 150/150 CLEAN keydiff=[137, 138, 139]、文字层 print=web=issues 差 0）。
- fix1 门禁 verdict：FAILURES: ['15a-textmd']——仅 15a 一门红，属预期内：text.md 与已发版差恰好为 E137–140 的 4 行标签，其余逐字节相同。新 text.md：`scratch-2026-w45-it/fix/2026-w45-it-en/2026-w45-it-en.text.md.new`，55,137 字节，sha256 `cf0b41ad6bc186dd80255a4fa2c04b9128a98fe0ef276e9b0f4f734528704ee9`。§四 15a 行与 §五 text.md 行已按此更新；KIT pin 不动（PDF 未变）。
- F4（D19 文本类）：本报告 §三与 KIT 中 `content7.py:91` → `content12.py:91`（`IN QUESTO NUMERO　CONTENTS/SOMMAIRE` 24→21pt，实测 `content12.py:91` 为该标题 21pt 行）；针对性重核：11 份 KIT + 11 份 D5 报告的 `content*.py:NNN` 引用 **50/50 正确**（逐行核对 patched 源码：标题在 ±9 行内、字号/tsize 在该行；另 2 处 KIT 行尾散文提及他标题，引用本身正确）。
