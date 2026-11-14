# D5 重建报告 — 2026-w43-it-en（英语读者版）

W43 it 家 D5 + §1.1 合并重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Noto Sans CJK 改走 Newsreader / Noto Sans；§1.1 组装：port fanout .py 集进仓内 core-it，旧样式→新样式）。施工 2026-11-13（一任 builder 至 run2 循环，二任 builder 接手核实 + gate 2 补跑 + 本报告）；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-en/`（`GATES-SUMMARY.txt` 为门禁总表，`run1/` 为修前日志归档，`run2/` 为修后日志归档）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core it --week 2026-w43 --i-understand-this-writes-production` → `production/2026-w43/core-it/svglib.py`（落盘 `_D5_READER = "latin"`；本版按 英语读者装，终值 `"latin"`）。
- 本版安装：`apply_variant.py --svglib <版>/svglib.py --target it --reader en --week 2026-w43`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号修前在 CJK 0 个，fix2 后归 Newsreader。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由 `hidden_files/style-port-it/export_it.py`（源码 manuscript 路线）重出核验（见第五节）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；`render.py` + `webpdf.py` 产出与已发版文本层逐字一致（字符多重集差 0）；重建 SVG 8/8 与 fanout 逐字节相同；印 PDF 与 fanout 印 PDF SHA 逐字节一致（`1ffd541d5167…`，8526959 B）。
- 修前普查 `d5_census.py`：D5 拉丁 **490**、西里尔 **0**、弯引号在 CJK **0**（拉丁 >0，符合装机前提）。
- KIT 记录的印/网 SHA 为旧配方值，已过期（例：core-it KIT §14 仍记印 22,914,252 B / 网 3,460,204 B，§10 仅记 22.9 MB / 3.48 MB）；基线不以 KIT SHA 为准，KIT 更新时以实测发运值订正（见第五节）。

## 三、缺陷与修复（run 1 → 二次修复）

- run 1 门禁：head_check 缺陷 **1**（P3 同）；boxtitle/creambox 缺陷 **4**（P1 `LA SETTIMANA IN CIFRE　Numbers` +30.6；P1 `IN QUESTO NUMERO　CONTENTS` p.text 24pt +40.2；P7 `ERRORI TIPICI　COMMON ERRORS` +31.8；P7 `LA PAROLA　WORD OF THE WEEK` +23.5）；occlusion 0；spill 0；刊头间距 367.5px PASS；P8 201 行、余量 53.1px。
- 二次修复（只动字号，文字零改动；脚本 `scratch-2026-w43-it/fix-it.py`，逐行断言式替换；量宽用 patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 p.text 标题内宽 400.5；盒修法行号指 tsize 行，D19）：
  1. `content34.py:22` P3 头 25→22。
  2. `content12.py:51` P1 盒 `LA SETTIMANA IN CIFRE　Numbers` tsize 23→21（397.2，余 7.3px）。
  3. `content12.py:94` P1 `IN QUESTO NUMERO　CONTENTS` p.text 24→21（385.3，余 15.2px）。
  4. `content7.py:73` P7 `ERRORI TIPICI　COMMON ERRORS` p.text 23→21（394.9，余 5.6px）。
  5. `content7.py:84` P7 `LA PAROLA　WORD OF THE WEEK` p.text 23→21（387.1，余 13.4px）。
- P8：行数 201→201，距页脚线余量 53.1 px 不变；p8 compare CLEAN（keydiff [137, 138]）。

## 四、门禁（run 2，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0（弯引号总数 0，全在 Newsreader）；render RC=0；webpdf RC=0（1139183 B <7MB）；occlusion 0 flags（含自检）；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL **0**（无 U+3000，PLAN Amendments 定位步骤不适用；新增拉丁 strings TOTAL 254，run 拆分所致）；spill 0（48 OBSERVE）；boxtitle 0 DEFECT（20 titles、245 body lines）；edge 0 TOUCH、0 NEAR；creambox PASS 0 defects（ratios n=405，中位 1.04，粗体中位 1.057，常规中位 0.992）；文字层 print=web 多重集差 0（98189 字符）；text.md BYTE-IDENTICAL；census_quotes 0 defective；家族 gates.py N/A（it 家无）；刊头间距 367.5 px PASS（D18）。
- 日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-en/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `The-Lucerna-VOL1-it-en.pdf` `5174f985235ada26acfddb6a64a0f5eabcae389a71696a7bbba7bda82ef796dd`（7995110 B；修前 `1ffd541d5167596bd35b7b84ef4725be2e49bfcd07cf9d4c16301b76f6eed01b`，8526959 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- 新网 PDF（`tools/webpdf.py`）`0c49b7b5afd976de3792c069e2ca1eb4bb2033665e591fe8d2f6e32ccf669c6e`（1139183 B）——待 closer 换入 `issues/2026-w43/2026-w43-it-en/2026-w43-it-en.pdf` 并更新 pin（已发版 `3becceabe661d26155b5726656691ffe869761900b0dc4c04e7c4c8efe5a1add`，1245514 B）。
- text.md：D5 不改文字内容；重建后由 `export_it.py` 从 patched 源码重出，与 fanout `.text.md.new` **BYTE-IDENTICAL**（55327 B，SHA `ad3417cd7065e604f3548d4e043399c601e281c224755d9f2245d6d4b52390ba`）。W43 it 在 `issues/` 内无已发 `.text.md`（11 版目录均只有 `.md` + `.pdf`），closer 落仓时按 MANIFEST 把该文件补进 `issues/`（新建，非覆盖）。
- KIT：`production/2026-w43/2026-w43-it-en/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 文末追加 D5 记录节）。
