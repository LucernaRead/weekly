# D5 重建报告 — 2026-w43-es-ja（日语读者版）

W43 es 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Noto Sans CJK 改走 Newsreader / Noto Sans）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-ja/`（`GATES-SUMMARY.txt` 为门禁总表，`run1/` 子目录为修前日志归档）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core es --week 2026-w43 --i-understand-this-writes-production` → `production/2026-w43/core-es/svglib.py`（落盘 `_D5_READER = "latin"`；装入 scratch 时按 zh-cn 读者装，终值 `"cjk"`）。
- 本版安装：`apply_variant.py --svglib <版>/svglib.py --target es --reader ja --week 2026-w43`（先 `--check` dry-run 通过）。装后 `_D5_READER = "cjk"`。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 0 个。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由 `hidden_files/style-port-es/textexp_es.py`（SVG 路线导出器）重出核验，交付件为已发版 `.text.md` 原样沿用（见第五节）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；`render.py` + `webpdf.py` 产出与已发版文本层逐字一致（字符多重集差 0）；重建 SVG 8/8 与已发版逐字节相同。
- 修前普查 `d5_census.py`：D5 拉丁 **340**、西里尔 **0**、弯引号在 CJK **0**（>0，符合装机前提）。
- 基线实测（已发版配方）：印 PDF `bf2e639b97f79677fd7bcdb037c329176bad6bdffc8cd6fe0e1e95485db08615`（18045216 B）、网 PDF（render）`955c7f6c9e3cc130747df8c1ad57f260b78bec711cec431209c4c44a62ea9640`（3438455 B）、issues 网 PDF `837c034070182f0702a8d2e35a802d91289e48106b89f112afadb04fbe7dba42`（1752354 B）。KIT 旧值（更旧配方）已过期，以上值为准。

## 三、缺陷与修复（run 1 → 二次修复）

- run 1 门禁：head_check 缺陷 **3**；occlusion **1 TEXTX（P7）**；boxtitle/creambox 缺陷 **3（P1 今週の数字 +22.5；P2 一句 +5.7；P7 よくある間違い +8.7）**；P8 行数 **222**、距页脚线余量 **41.7px**；verify **ADOPT（20 REWRAP）**。
- 二次修复（只动字号，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 p.text 标题内宽 400.5）：
  1. `content12.py:125` P1 头 `EL OTOÑO EMPIEZA DE VERDAD` 25→24（439.1→421.5）。
  2. `content7.py:16` P7 头 `A2　DECIR LA HORA Y EL PRESENTE` 24→21（471.1→412.2；同时清除 P7 TEXTX 碰撞——该头压 `B1` 20.5×16.8px）。
  3. `content7.py:48` P7 头 `B2　CREO QUE… / NO CREO QUE…` 24→23（428.8→411.0）。
  4. `content12.py:47` P1 盒 `LA SEMANA EN CIFRAS　今週の数字` tsize 23→21（427.0→389.8；22pt 仍 +3.9）。
  5. `content12.py:176` P2 盒 `LA FRASE PARA RECORDAR　一句` tsize 23→22（410.2→392.4）。
  6. `content7.py:79` P7 `ERRORES TÍPICOS　よくある間違い` p.text 23→22（409.2→391.3）。
  - P3 头 `RECORDAR JUNTOS　ともに偲ぶ` 25pt 入栏，无需修。
- P8：行数 222→222，距页脚线余量 41.7px 不变；p8 compare CLEAN（keydiff [137, 138]）。

## 四、门禁（run 2，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1547194 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 1 个（U+3000，run 拆分）；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=395，中位 1.040）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A。
- 日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-ja/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `53aef2d8d57fe87f1c0b1c07e82fb86f536ba707fd9fef60ce9e7081f4375004`（11775499 B）；新网 PDF（render）`653e235f39a0768037ff5aa73b8a16e87780b0f6c78098713fcb2f0a44ed27c3`（3449690 B）；issues 网 PDF（`tools/webpdf.py`）`5d8fd9b1ad2b38152bbcf99494c22de52cff2eff157bc80d364e333daf40ba93`（1547194 B）——待 closer 换入 `issues/2026-w43/2026-w43-es-ja/2026-w43-es-ja.pdf` 并更新 pin（已发版 `6aff84ace50444208b129f56fb1c99c7d77e3b0fb1ac917f19c4d33abb3b32ed`，1716266 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- text.md：D5 不改文字内容；重建后重出因字体宽度变化断行重排（20 REWRAP），交付件为已发版 `.text.md` 原样沿用（BYTE-IDENTICAL）；验收 `verify_textexp_es.py --edition` 判 **ADOPT**（0 UNEXPECTED；习题号 313/313 序列一致；8 页 token 全同）。
- KIT：`production/2026-w43/2026-w43-es-ja/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 末节 D5 记录（§8））。
