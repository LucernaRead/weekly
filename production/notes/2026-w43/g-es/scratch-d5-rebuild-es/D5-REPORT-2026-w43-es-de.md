# D5 重建报告 — 2026-w43-es-de（德语读者版）

W43 es 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Noto Sans CJK 改走 Newsreader / Noto Sans）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-de/`（`GATES-SUMMARY.txt` 为门禁总表，`run1/` 子目录为修前日志归档）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core es --week 2026-w43 --i-understand-this-writes-production` → `production/2026-w43/core-es/svglib.py`（落盘 `_D5_READER = "latin"`；装入 scratch 时按 zh-cn 读者装，终值 `"cjk"`）。
- 本版安装：`apply_variant.py --svglib <版>/svglib.py --target es --reader de --week 2026-w43`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 3 个修前在 CJK，fix2 后归 Newsreader。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由 `hidden_files/style-port-es/textexp_es.py`（SVG 路线导出器）重出核验，交付件为已发版 `.text.md` 原样沿用（见第五节）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；`render.py` + `webpdf.py` 产出与已发版文本层逐字一致（字符多重集差 0）；重建 SVG 8/8 与已发版逐字节相同。
- 修前普查 `d5_census.py`：D5 拉丁 **498**、西里尔 **0**、弯引号在 CJK **3**（>0，符合装机前提）。
- 基线实测（已发版配方）：印 PDF `bc352a27013751fd7a1991926b15686bf3c24ca060906268dd69faf6898b838f`（5162960 B）、网 PDF（render）`7658a810dde1b13624a51995c11fb4162894869519d9821cbca4fc3cba8530f4`（3527600 B）、issues 网 PDF `e4e31b78262457228b826a45f03edfd7da7cea61d43bf9e627af28f4de4dccba`（1146544 B）。KIT 旧值（更旧配方）已过期，以上值为准。

## 三、缺陷与修复（run 1 → 二次修复）

- run 1 门禁：head_check 缺陷 **4**；occlusion **1 TEXTX（P7）**；boxtitle/creambox 缺陷 **4（P1 ZAHLEN +13.5；P2 MERKSATZ +61.9；P7 TYPISCHE FEHLER +20.3；P7 WORT DER WOCHE +19.5）**；P8 行数 **205**、距页脚线余量 **57.4px**；verify **ADOPT（16 REWRAP）**。
- 二次修复（只动字号，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 p.text 标题内宽 400.5）：
  1. `content12.py:128` P1 头 `EL OTOÑO EMPIEZA DE VERDAD` 25→24（439.1→421.5）。
  2. `content34.py:23` P3 头 `RECORDAR JUNTOS　GEDENKEN` 25→23（449.6→413.6）。
  3. `content7.py:16` P7 头 `A2　DECIR LA HORA Y EL PRESENTE` 24→21（471.1→412.2；同时清除 P7 TEXTX 碰撞——该头压 `B1` 20.5×16.8px）。
  4. `content7.py:48` P7 头 `B2　CREO QUE… / NO CREO QUE…` 24→23（428.8→411.0）。
  5. `content12.py:50` P1 盒 `LA SEMANA EN CIFRAS　ZAHLEN` tsize 23→22（418.0→399.8）。
  6. `content12.py:179` P2 盒 `FRASE PARA RECORDAR　MERKSATZ` tsize 23→19（466.4→385.2；20pt 仍 +1.0 越框）。
  7. `content7.py:79` P7 `ERRORES TÍPICOS　TYPISCHE FEHLER` p.text 20→18（420.9→378.8；19pt 余量仅 0.6px）。
  8. `content7.py:90` P7 `LA PALABRA　WORT DER WOCHE` p.text 23→21（419.3→382.8）。
- P8：行数 205→205，距页脚线余量 57.4px 不变；p8 compare CLEAN（keydiff [137, 138]）。

## 四、门禁（run 2，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1065792 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 1 个（U+3000，run 拆分）；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=398，中位 1.040）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A。
- 日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-de/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `7087772835a236d4b01001278f4313be5545715e238e92f73bd8adf8f23485a1`（4554501 B）；新网 PDF（render）`3263b0813177dce752caf5d2f58e037a61b92e154a6cdbb7adfcb45550ad650e`（3541931 B）；issues 网 PDF（`tools/webpdf.py`）`992a7c2195b2cacabff0f13cdf52c8a2e16a32fa711b6f865bbcd4371b9d6872`（1065792 B）——待 closer 换入 `issues/2026-w43/2026-w43-es-de/2026-w43-es-de.pdf` 并更新 pin（已发版 `b99f60f06b10b670557b7d102bceaf4c00e68ca570802560f3e4cdc4607b971e`，1109963 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- text.md：D5 不改文字内容；重建后重出因字体宽度变化断行重排（16 REWRAP），交付件为已发版 `.text.md` 原样沿用（BYTE-IDENTICAL）；验收 `verify_textexp_es.py --edition` 判 **ADOPT**（0 UNEXPECTED；习题号 313/313 序列一致；8 页 token 全同）。
- KIT：`production/2026-w43/2026-w43-es-de/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 末节 D5 记录）。
