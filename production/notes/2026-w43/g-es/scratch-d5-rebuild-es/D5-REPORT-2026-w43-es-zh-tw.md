# D5 重建报告 — 2026-w43-es-zh-tw（繁體中文读者版）

W43 es 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Noto Sans CJK 改走 Newsreader / Noto Sans）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-zh-tw/`（`GATES-SUMMARY.txt` 为门禁总表，`run1/` 子目录为修前日志归档）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core es --week 2026-w43 --i-understand-this-writes-production` → `production/2026-w43/core-es/svglib.py`（落盘 `_D5_READER = "latin"`；装入 scratch 时按 zh-cn 读者装，终值 `"cjk"`）。
- 本版安装：`apply_variant.py --svglib <版>/svglib.py --target es --reader zh-tw --week 2026-w43`（先 `--check` dry-run 通过）。装后 `_D5_READER = "cjk"`。fix2（U+201C/U+201D/U+2019 → serif）保留：本版彎引號 0 個。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由 `hidden_files/style-port-es/textexp_es.py`（SVG 路线导出器）重出核验，交付件为已发版 `.text.md` 原样沿用（见第五节）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；`render.py` + `webpdf.py` 产出与已发版文本层逐字一致（字符多重集差 0）；重建 SVG 8/8 与已发版逐字节相同。
- 修前普查 `d5_census.py`：D5 拉丁 **338**、西里尔 **0**、弯引号在 CJK **0**（>0，符合装机前提）。
- 基线实测（已发版配方）：印 PDF `129115ff97e879fa30b666e70e7e7cf3c1adf6a09914571b1723924c652fd108`（17166335 B）、网 PDF（render）`57675efd3af5547479cd39ed257ce7161b28fc27376942032d962feda589b02d`（3340861 B）、issues 网 PDF `cf8c4ea2bbfec9f482501c0bc2a82abbcd5e2509e60b22dc84dbeeb71ccf70a9`（1921948 B）。KIT 旧值（更旧配方）已过期，以上值为准。

## 三、缺陷与修复（run 1 → 二次修复）

- run 1 门禁：head_check 缺陷 **3**；occlusion **1 TEXTX（P7）**；boxtitle/creambox 缺陷 **2（P1 數字看本週 +22.5；P2 口訣 +5.7）**；P8 行数 **200**、距页脚线余量 **57.4px**；verify **ADOPT（21 REWRAP）**。
- 二次修复（只动字号，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 p.text 标题内宽 400.5）：
  1. `content12.py:125` P1 頭 `EL OTOÑO EMPIEZA DE VERDAD` 25→24（439.1→421.5）。
  2. `content7.py:16` P7 頭 `A2　DECIR LA HORA Y EL PRESENTE` 24→21（471.1→412.2；同時清除 P7 TEXTX 碰撞——該頭壓 `B1` 20.5×16.8px）。
  3. `content7.py:48` P7 頭 `B2　CREO QUE… / NO CREO QUE…` 24→23（428.8→411.0）。
  4. `content12.py:47` P1 盒 `LA SEMANA EN CIFRAS　數字看本週` tsize 23→21（427.0→389.8；22pt 仍 +3.9）。
  5. `content12.py:176` P2 盒 `LA FRASE PARA RECORDAR　口訣` tsize 23→22（410.2→392.4）。
  - P3 頭 `RECORDAR JUNTOS　一起紀念` 25pt 入欄，無需修。
- P8：行数 200→200，距页脚线余量 57.4px 不变；p8 compare CLEAN（keydiff [137, 138]）。

## 四、门禁（run 2，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1506359 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 1 个（U+3000，run 拆分）；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=378，中位 1.040）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A。
- 日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-zh-tw/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `2bc920547fce94caae23ae54885770e5bcf761a7f210cce25e1fade5a55ba6e9`（5960459 B）；新网 PDF（render）`d427ea6d0a3d1f23a2ded40f5ceae47a348a7d071fb911be02a1dded73cf8a9e`（3351530 B）；issues 网 PDF（`tools/webpdf.py`）`172aa57c838bee09a75144e49956674dd823a44e226e61d754bd3ac05b37c08d`（1506359 B）——待 closer 换入 `issues/2026-w43/2026-w43-es-zh-tw/2026-w43-es-zh-tw.pdf` 并更新 pin（已发版 `50b1ccde913b73ca76a435edd056b84af004dc7026e81fd255335fa4342db72c`，1885857 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- text.md：D5 不改文字内容；重建后重出因字体宽度变化断行重排（21 REWRAP），交付件为已发版 `.text.md` 原样沿用（BYTE-IDENTICAL）；验收 `verify_textexp_es.py --edition` 判 **ADOPT**（0 UNEXPECTED；习题号 313/313 序列一致；8 页 token 全同）。
- KIT：`production/2026-w43/2026-w43-es-zh-tw/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 末节 D5 记录（§11））。
