# D5 重建报告 — 2026-w43-es-ru（俄语读者版）

W43 es 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Noto Sans CJK 改走 Newsreader / Noto Sans）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-ru/`（`GATES-SUMMARY.txt` 为门禁总表，`run1/` 子目录为修前日志归档）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core es --week 2026-w43 --i-understand-this-writes-production` → `production/2026-w43/core-es/svglib.py`（落盘 `_D5_READER = "latin"`；装入 scratch 时按 zh-cn 读者装，终值 `"cjk"`）。
- 本版安装：`apply_variant.py --svglib <版>/svglib.py --target es --reader ru --week 2026-w43`（先 `--check` dry-run 通过）。装后 `_D5_READER = "ru"`。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 0 个。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由 `hidden_files/style-port-es/textexp_es.py`（SVG 路线导出器）重出核验，交付件为已发版 `.text.md` 原样沿用（见第五节）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；`render.py` + `webpdf.py` 产出与已发版文本层逐字一致（字符多重集差 0）；重建 SVG 8/8 与已发版逐字节相同。
- 修前普查 `d5_census.py`：D5 拉丁 **338**、西里尔 **250**、弯引号在 CJK **0**（>0，符合装机前提）。
- 基线实测（已发版配方）：印 PDF `3b64621ce52051c8e2b658828e18f0659fca6b7f17cae2f61e4e269ac389ed5c`（5169873 B）、网 PDF（render）`b9f25af22eab293b782929115191f81c628746507eee583bac07940c0258db01`（3539100 B）、issues 网 PDF `1128ce31dbbe4c98d10419e10b28435a2e47526cbded5ac8d8eaf2302d3e3fed`（1187860 B）。KIT 旧值（更旧配方）已过期，以上值为准。

## 三、缺陷与修复（run 1 → 二次修复）

- run 1 门禁：head_check 缺陷 **0**；occlusion **0**；boxtitle/creambox 缺陷 **1（P1 Para entender la semana +16.1）**；P8 行数 **228**、距页脚线余量 **44.7px**；verify **HOLD — 导出器误拆行（见下）**。
- 二次修复（只动字号，文字零改动；实测 advance，patched svglib `text_w`，sans regular；盒内宽 400.5）：
  1. `content12.py:69` P1 `Пять главных тем　Para entender la semana` p.text 19→18（416.2→394.3）。
  - 本版头（P1/P3/P7）与 P7 碰撞首轮即全过，无需修。
- P8：行数 228→231，距页脚线余量 44.7px 不变；p8 compare CLEAN（keydiff [137, 138]）。

## 四、门禁（run 2，17 门绿；gate 15 ADOPT，D16 修后）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0（noto_sans_elements=772，ru 读者预期）；render RC=0；webpdf RC=0（1308732 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 1 个（U+3000，run 拆分）；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=405，中位 1.001）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A。gate 15 textmd-verify **ADOPT**（D16 修后，独立重校末位重跑：0 UNEXPECTED、REWRAP 24）：P7 行 `bueno→mejor и malo→peor —` 在修后导出中恢复为一行。根因是导出器 `textexp_es.py` 的 `kind_of()` 不认 `Noto Sans`（ru 读者拉丁文走该字体），默认按 `serif`（Newsreader）量宽——`bueno` 量得 58.98，真实 62.75，算出间距 3.72px > GROUP_GAP 2.0 误拆；真实间距 −0.05px（run 相接）。D16 修复：`kind_of()` 加 `Noto Sans` → sans 映射（`textexp_es.py:54`，机制方已修）。新版 SVG 各 run 拼接与已发版该行逐字相同；其余 7 页 token 全同，习题号 313/313 序列一致。
- 日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-ru/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `0c31a56b2db62c904eed9a81c236a0c8eb53c16367880085e39fc67737e33b20`（4811727 B）；新网 PDF（render）`0473e3d41f13649012a3cf7d7ba406b873165db171a64ee5e58d51c42a8b53c8`（3547345 B）；issues 网 PDF（`tools/webpdf.py`）`3863f81013be3f6b143d0654abf6a1b087df09c79647a04801df8427fd04dd30`（1308732 B）——待 closer 换入 `issues/2026-w43/2026-w43-es-ru/2026-w43-es-ru.pdf` 并更新 pin（已发版 `d365d2874f1199a12d3a055a1f1d1d1e560ea0d6c0a34c162fc1b1e7a301f3c2`，1151782 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- text.md：D5 不改文字内容；重建后重出因字体宽度变化断行重排（24 REWRAP，D16 修后），交付件为已发版 `.text.md` 原样沿用（BYTE-IDENTICAL）；验收 `verify_textexp_es.py --edition` 判 **ADOPT**（D16 修后，独立重校末位重跑：0 UNEXPECTED、REWRAP 24）——P7 行 `bueno→mejor и malo→peor —` 在修后导出中恢复为一行（新导出第 2301 行，与已发 text.md 第 2299 行同文）。根因是导出器 `textexp_es.py` 的 `kind_of()` 不认 `Noto Sans`（ru 读者拉丁文走该字体），默认按 `serif`（Newsreader）量宽——`bueno` 量得 58.98，真实 62.75，算出间距 3.72px > GROUP_GAP 2.0 误拆；真实间距 −0.05px（run 相接）。D16 修复：`kind_of()` 加 `Noto Sans` → sans 映射（`textexp_es.py:54`）。新版 SVG 各 run 拼接与已发版该行逐字相同；其余 7 页 token 全同，习题号 313/313 序列一致。新导出与已发 text.md 的 diff（104 行）全为换行重排，无内容差异。重排统计：24 REWRAP（D16 修后；修前 37）。
- KIT：`production/2026-w43/2026-w43-es-ru/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 末节 D5 记录（§15））。
