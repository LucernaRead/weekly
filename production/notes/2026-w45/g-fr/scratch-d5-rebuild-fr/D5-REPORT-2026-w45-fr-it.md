# D5 重建报告 — 2026-w45-fr-it（意大利语读者版）

W45 fr 家 D5 + §1.1 合并重建（pre-D1 新样式：D1 修复 + D5 一次渲完）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-fr/logs/2026-w45-fr-it/`（`GATES-SUMMARY-run2.txt` 为门禁总表；`GATES-SUMMARY-run1.txt` 为修前总表）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core fr --week 2026-w45 --i-understand-this-writes-production` → `production/2026-w45/core-fr/svglib.py` +95/−3 行，`_D5_READER = "latin"`（L100）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-fr-it/svglib.py --target fr --reader it --week 2026-w45`（先 `--check` dry-run，RC=0，mode latin 正确）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（`U+201C` 命中）。
- D1 组装：patched svglib 为 fanout D1 版（与生产版 svglib 的 diff 恰为 D1 hunk 28 行）；content*.py/bslib4.py 与生产版逐字节相同。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `scratch-prep-p3b/export_w45_fanout_fixed.py` 导出（第 0 步已核实：fr-es 试跑 12 行差 = 6 条 gloss 行泄漏修复差，fr-zh-cn BYTE-IDENTICAL）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **562**、西里尔 0、弯引号总数 0（>0，符合装机前提）。
- 基线 P8 口径：noted **91/150**（core-fr 与 10 读者版同一集合，含 [108]）；compare 全 CLEAN，keydiff `[135, 150]`。
- 基线 D18 刊头间距 124.1px；基线 D37 副刊头行余量 108.6pt。

## 三、缺陷与修法（run1 → run2）

run1 缺陷全部为 D5 字体加宽引起（拉丁粗体在 Newsreader 下比 Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值 +12.68px）。修法只动字号 / 盒高，**未动任何文字内容**。共 18 项：

| 门 | 内容 | 修法 |
|---|---|---|
| head_check | `MICRO-DRILLS　ALLENAMENTO` | content34.py:191 24→**23**（410.1px ✓） |
| head_check | `LIRE LE CALENDRIER　LEGGERE` | content56.py:131 25→**23**（411px ✓） |
| head_check | `IL EST PRÉVU QUE + SUBJONCTIF` | content56.py:164 25→**23**（411px ✓） |
| head_check | `LE COMPARATIF EN POLITIQUE` | content56.py:170 25→**24**（427.9px ✓） |
| head_check | `MICRO-DRILLS　ALLENAMENTO` | content56.py:178 25→**23**（410.1px ✓） |
| head_check | `IL EST PRÉVU QUE + SUBJONCTIF` | content7.py:38 24→**23**（411px ✓） |
| head_check | `BOÎTE À OUTILS　STRUMENTI` | content7.py:48 27→**25**（411.6px ✓） |
| head_check | `CLINIQUE DES ERREURS　CLINICA` | content7.py:97 25→**22**（414.2px ✓） |
| head_check | `A　TEXTE À TROUS　COMPLETA` | content8.py:28 24→**23**（417.3px ✓） |
| head_check | `D　PHRASES　COSTRUISCI FRASI` | content8.py:72 24→**23**（417.3px ✓） |
| box标题/刊头 | `DANS CE NUMÉRO　SOMMARIO` | content12.py:93 24→**22**（383px ✓） |
| box标题 tsize | `LES PHRASES DU COMMENTATEUR` | content34.py:166 23→**21**（402.5px ✓） |
| box标题/刊头 | `MOTS DE LA MUSIQUE　LESSICO` | content56.py:70 23→**22**（393.1px ✓） |
| box标题/刊头 | `PARIS CREATOR WEEK　CREATOR` | content56.py:83 23→**21**（388.4px ✓） |
| box标题 tsize | `TROIS DATES POUR COMPRENDRE` | content56.py:194 23→**21**（391.7px ✓） |
| box标题/刊头 | `LUNEDÌ SI TORNA A SCUOLA　TUTTA LA FRANCIA` | content12.py:27 27→**23**（621.6px ✓） |
| P1 标题 | `LUNDI 2 NOVEMBRE : LA FRANCE REPREND !` | content12.py:25 46→**44** |
| spill | `sh = 62 + sum(...) + 14` | content12.py:192 14→**30** |

P8 变化：190 -> 199 行，距页脚线余量 37.3 -> 50.0 px（正，无溢出）。

## 四、门禁（run2，全套 16 门 + D18 + D37，ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0 |
| 5 webpdf | RC=0，网 PDF 1202248 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 97 of 150 |
| 8 p8 compare | PASS，CLEAN（keydiff=[135, 150]，预期读者语键） |
| 9 freeze baseline | 8/8 |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 342，预期 D5 run-split；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL |
| 12 boxtitle | 0 DEFECT（backup 已补基线 svg 为真对照） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 190 -> 199，slack 37.3 -> 50.0） |
| 15 文字层 print=web + text.md | 字符多重集差 **0**；text.md differs from issued by exactly 24 lines = 6 gloss lines (fixed `", [("` leak; rest BYTE-IDENTICAL) |
| 16 census_quotes | 0 defective |
| D18 刊头间距 | PASS，36.2px |
| D37 副刊头行 | PASS，余量 75.8pt |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL2-fr-it.pdf`，**8,676,210 字节**，SHA-256 `52d0b087c3789fa3bde2f96ad979bf04b74578f93f03ebd83f19eb54cd059f0c`。
- 网 PDF：`2026-w45-fr-it.web.pdf`，**1,202,248 字节**，SHA-256 `f7f1a166210fea9f41abd3a5b10f73269938f1a3a5ccd4ec959bd774c8e200a6`（网 PDF 字节跨次运行不确定——closer 须拷 builder 原件，绝不重跑 webpdf）。
- text.md：`2026-w45-fr-it.text.md`，**46,306 字节**，SHA-256 `8f23d6959ad9505f69026ec984f4e0e79c86a251ae7d6c9e329cd628a3df759b`（differs from issued by exactly 24 lines = 6 gloss lines (fixed `", [("` leak; rest BYTE-IDENTICAL)）。
- 练习总量仍为 **150 题**。

## 六、KIT

- `production/2026-w45/2026-w45-fr-it/WEEKLY-KIT.md`：文末追加 D5 节（§18：装机、修复、终门禁 ALL-GREEN、新交付物 pins）。§14/§15 原 round-5 VOL3 pins 未动（其 pin 的是原始交付物文件名；D5 pins 在新 D5 节内）。
