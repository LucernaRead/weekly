# D5 重建报告 — 2026-w45-it-pt（葡萄牙语读者版）

W45 it 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
施工分工：builder v1 完成第 0–5 步、run1 全部门禁、全部字号修复与 run2 前 6 版（zh-cn/de/en/es/fr/ja）；builder v2（接替 v1，v1 被 restart drain 杀死）完成 run2 余下 5 版（ko/nl/pt/ru/zh-tw）、KIT 更新与本报告。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-it/logs/2026-w45-it-pt/`（`GATES-SUMMARY.txt` 为 run2 门禁总表，`run1/GATES-SUMMARY.txt` 为修前总表）；fix2 日志：`hidden_files/d5-redo/scratch-2026-w45-it/fix2/logs/2026-w45-it-pt/`。门禁总表复本（D29）：`production/notes/2026-w45/g-it/scratch-d5-rebuild-it/logs/2026-w45-it-pt/GATES-SUMMARY.txt`（已换为 fix2 总表，与 scratch fix2 总表逐字节一致，`cmp` 已验）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core it --week 2026-w45` → `production/2026-w45/core-it/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-it-pt/svglib.py --target it --reader pt --week 2026-w45`（先 `--check` dry-run，mode=latin 正确）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `hidden_files/style-port-it/export_it.py` 导出（第 0 步已核实：scratch 试跑 vs issues 已发版 BYTE-IDENTICAL，11/11）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 6,589,861 字节（sha256 `eef40dd1ab98…`），与 fanout 原件逐字节一致；网 PDF 635,508 字节。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF 差 **0**。
- 修前普查 `d5_census.py`：D5 违规 **488**（>0，符合装机前提）。
- 基线 P8 口径：noted **150/150**。

## 三、缺陷与修法（run1 → run2）

run1 共 1 项，全部为 D5 字体加宽引起（讲解层粗体在 Noto Sans CJK 下比 Newsreader 宽，框标题右溢；P1 溢出的标题同时造成 occlusion 墨迹重叠）。修法只动字号，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | 6 occlusion / 12 boxtitle / 14 creambox | P1 框标题 `EM NÚMEROS` | 右溢 +38.2px；墨迹与 P1 正文重叠 10.2×7.3px | `content12.py:50` 框标题 tsize 20→**18** |

P8 变化：211->211 行，距页脚线余量 57.6 → 57.6 px（正，无溢出）。

- 刊头间隙特记：D18 实测 gap **17.0px**（正值，PASS；D18 只以 ≤0 为缺陷，无需修复）。

## 四、门禁（run2，全套 17 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 6,093,415 B（fix2；run2 为 6,093,409 B） |
| 5 webpdf | RC=0，网 PDF 563,824 B（< 7 MB；fix2 重渲，run2 为 563,811 B） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**，keydiff=[137, 138, 139]，missing=[]，extra=[] |
| 9 freeze baseline | 8/8（patched 重建复现自身 SVG） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 247，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 spills |
| 12 boxtitle | 0 defects |
| 13 edge | 0 touches，0 nears |
| 14 creambox | 0 defects；P8 行数 211->211，页脚余量 57.6 px |
| 15 text layer | print=web=issues，字符多重集差 0 |
| 15a text.md | 导出 RC=0，diff = 4 行标签（F1 修复，D33），其余逐字节相同 |
| 16 census_quotes | 0 defective |
| 18 masthead（D18） | slogan–date 间隙 17.0px，PASS（>0） |

**结论：run2 ALL-GREEN；fix2 verdict FAILURES: ['15a-textmd']——仅 15a 一门红，属预期内（text.md 与已发版差恰好为 F1 的 4 行标签，见 §六；其余 17 门 + D18 全绿，见 §七）。**

## 五、新交付物 / KIT

- 印 PDF：`scratch-2026-w45-it/fix2/2026-w45-it-pt/The-Lucerna-VOL3.pdf` — 6,093,415 字节，sha256 `7701f8f6505a064cfe4b8fcabff7b923f58349e6d59ab7af78926c4c8b1ee7d5`（fix2；run2 旧值为 6,093,409 字节 `bb7f380372ef6008380dd655e4174f09fa795d40799db1a871dad15718d5a8c2`，文件名 VOL3 为 render.py 既有命名，基线同名，刊头 VOL.2 无误）。
- 网 PDF：`scratch-2026-w45-it/fix2/2026-w45-it-pt/2026-w45-it-pt.web.pdf` — 563,824 字节，sha256 `83880dc68332d33f0caafe6832ecf64fe612b5aaf037e019a50c0f55c0c6379e`（fix2；run2 旧值为 563,811 字节 `06618d95f10e0d6ee3c2b0b3fb0cac7709c843d42c99b0648af65f090e400761`）。网 PDF 跨次运行字节不确定，**closer 须拷 fix2 原件，绝不重跑 webpdf**；KIT 记录的 fix2 SHA 即交付值。
- text.md：`scratch-2026-w45-it/fix/2026-w45-it-pt/2026-w45-it-pt.text.md.new`（fix1 导出）— 55,673 字节，sha256 `c3d13e9d3572d0b0bca0c6efb07c04bdf302ed232f55f2a22564716a50868143`，与 issues 已发版 diff = 4 行标签（F1 修复，D33），其余逐字节相同。
- KIT：`production/2026-w45/2026-w45-it-pt/WEEKLY-KIT.md` 针脚行已更新为上述新值 + 文末 D5 节（§14）。

## 六、F1–F4 修复（fix1，2026-11-14，D33）

- F1：`production/2026-w45/2026-w45-it-pt/content8.py:69/71/73/75`，`f.ex` 第 2 参数 "翻译" → "Tradução"（4 行）。基线核实：已发版 text.md 4 行均为 `[翻译]`、基线 text.md 字节相同，先存缺陷、非 D5 回归。core-it/zh-cn 同处 "翻译" 正确，未动。
- 修复后在 `scratch-2026-w45-it/fix/2026-w45-it-pt/` 重建（`gates_fix.py`，tag fix1；production 改动源 + patched 其余文件原样）：印 PDF **字节与 builder run2 完全一致**（6,093,409 B，sha256 `bb7f380372ef…`）；其余 16 门 + D18 全绿（TOTAL 150、p8 150/150 CLEAN keydiff=[137, 138, 139]、文字层 print=web=issues 差 0）。
- fix1 门禁 verdict：FAILURES: ['15a-textmd']——仅 15a 一门红，属预期内：text.md 与已发版差恰好为 E137–140 的 4 行标签，其余逐字节相同。新 text.md：`scratch-2026-w45-it/fix/2026-w45-it-pt/2026-w45-it-pt.text.md.new`，55,673 字节，sha256 `c3d13e9d3572d0b0bca0c6efb07c04bdf302ed232f55f2a22564716a50868143`。§四 15a 行与 §五 text.md 行已按此更新；KIT pin 不动（PDF 未变）。

## 七、F-G1 版式修复（fix2，2026-11-14，D37）

- F-G1：pt P1 副刊头行（16pt 粗体居中，SVG y=612）`TEXTOS EM ITALIANO EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA` 末尾 3 字母 ESA 被右栏奶油框（`LA SETTIMANA` 框，PDF x=1079.6）遮住。重校 v2 实测：重建印 PDF 同行末尾 x1=1103.3pt，超框缘 +23.7pt。
- 基线核实（修前）：已发版 pt web PDF 同行末尾 x1=1060.0pt（框缘内，余量 19.6pt），`PORTUGUESA` 完整可见；行文与 patched 一字未改（vs-issues diff 仅 4 行 F1 标签）；builder run2 印 PDF（6,093,409 B，sha256 `bb7f380372ef…`）同行末尾 x1=1103.3pt——缺陷在 builder 交付物本身，D5 字体切换引入（同行宽度 653.7→738.2pt）。
- 修法（只降字号，不缩短文案、不移动奶油框、不改其他版、不改其他行）：`content12.py:29` 字号 16pt → **14pt**，一行。14pt 首试即达标，无需再降档。
- 改动文件（三处同改，仅 :29 一行）：`production/2026-w45/2026-w45-it-pt/content12.py:29`、`scratch-2026-w45-it/patched/2026-w45-it-pt/content12.py:29`、`scratch-2026-w45-it/fix2/2026-w45-it-pt/content12.py:29`。改后核实：fix2 构建源 `content12.py` 与 patched/ 逐字节一致（`diff` rc=0）；与 production 的差仅 :50 一行（`tsize=20` vs `18`，为 builder §5 `EM NÚMEROS` 修复、尚未同步的既有差，closer 按 BUILD §8.2 同步 patched→production 时带入，本次不碰）。
- 重建验证（`scratch-2026-w45-it/fix2/2026-w45-it-pt/`，`gates_fix2.py`，tag fix2；run → render → webpdf + 全部门禁重跑；渲染前 `fc-cache -f` 已暖，`df -h` 74G/150G 未触 100G 线）：行尾 x 实测 **1056.7pt**（印/网 PDF 一致），框缘内余量 **22.9pt**（≥10pt 要求）；行宽 738.2→645.9pt。P1 全页目检：`PORTUGUESA` 完整可见，行尾与奶油框之间有清晰空白。
- fix2 门禁 verdict：FAILURES: ['15a-textmd']——仅 15a 一门红，属预期内（text.md 与已发版差恰好为 F1 的 4 行标签）。其余 17 门 + D18 全绿：TOTAL 150、head_check 0 defects、d5 census 0、occlusion 0、p8 150/150 CLEAN keydiff=[137, 138, 139]、freeze baseline 8/8、freeze-diff new-CJK 0（new-Latin 247）、spill 0、boxtitle 0、edge 0/0、creambox 0（P8 211->211，页脚余量 57.6）、文字层 print=web=issues 差 0、census_quotes 0、刊头间隙 17.0px PASS。
- 新交付物：印 PDF 6,093,415 B，sha256 `7701f8f6505a064cfe4b8fcabff7b923f58349e6d59ab7af78926c4c8b1ee7d5`；网 PDF 563,824 B，sha256 `83880dc68332d33f0caafe6832ecf64fe612b5aaf037e019a50c0f55c0c6379e`（fix2 原件，closer 须拷原件、绝不重跑 webpdf）；text.md `fix2/2026-w45-it-pt/2026-w45-it-pt.text.md.new`，55,673 字节，sha256 `c3d13e9d3572d0b0bca0c6efb07c04bdf302ed232f55f2a22564716a50868143`——与 fix1 值逐字节一致（`cmp` MATCH，只改字号、文字零改动）。§四门 4/5 行、§五印/网行已按此更新；KIT §11 针脚行与 §14 D5 节印/网 pin 已更新为 fix2 值；GATES-SUMMARY 复本已换为 fix2 总表（`cmp` 已验）。
- 其余 10 版未动：印 PDF 与 run2/fix1 值逐版核对字节一致（zh-cn 7,426,081 `c71c23977abf`、de 6,094,436 `6182d725576e`、en 6,091,558 `c0513f07ebad`、es 6,092,999 `707bcdfe6eb2`、fr 6,091,311 `75e90ca8fb76`、ja 12,016,510 `4378035f00a0`、ko 7,858,684 `60298464bf94`、nl 6,089,380 `6eb4fbbef0d8`、ru 6,405,908 `5f8f738b63c7`、zh-tw 7,491,805 `da50f82f50f7`）；其余 10 版 KIT/D5/GATES-SUMMARY 一律未动。
- F-K1–F-K6 未动（closer 落仓时修）：本 fix2 只改了 pt KIT 的印/网 PDF pin；六版 KIT 文末 D5 节 text.md pin 行一律未碰。正确 SHA 见重校 v2 §7（de `9c99c586fc9c…f3b3`、en `cf0b41ad6bc1…ee9`、es `9a7e6fc9525f…80ac`、fr `16155ed27e57…3224`、ja `d479249b8c1d…ac16`、pt `c3d13e9d3572…8143`）。
