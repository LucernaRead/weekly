# D5 重建报告 — 2026-w45-fr-ja（日语读者版）

W45 fr 家 D5 + §1.1 合并重建（pre-D1 新样式：D1 修复 + D5 一次渲完）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-fr/logs/2026-w45-fr-ja/`（`GATES-SUMMARY-run3.txt` 为门禁总表；`GATES-SUMMARY-run1.txt` 为修前总表）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core fr --week 2026-w45 --i-understand-this-writes-production` → `production/2026-w45/core-fr/svglib.py` +95/−3 行，`_D5_READER = "latin"`（L100）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-fr-ja/svglib.py --target fr --reader ja --week 2026-w45`（先 `--check` dry-run，RC=0，mode cjk 正确）。装后 `_D5_READER = "cjk"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（`U+201C` 命中）。
- D1 组装：patched svglib 为 fanout D1 版（与生产版 svglib 的 diff 恰为 D1 hunk 28 行）；content*.py/bslib4.py 与生产版逐字节相同。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `scratch-prep-p3b/export_w45_fanout_fixed.py` 导出（第 0 步已核实：fr-es 试跑 12 行差 = 6 条 gloss 行泄漏修复差，fr-zh-cn BYTE-IDENTICAL）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **444**、西里尔 0、弯引号总数 0（>0，符合装机前提）。
- 基线 P8 口径：noted **91/150**（core-fr 与 10 读者版同一集合，含 [108]）；compare 全 CLEAN，keydiff `[135, 150]`。
- 基线 D18 刊头间距 176.5px；基线 D37 副刊头行余量 184.0pt。

## 三、缺陷与修法（run1 → run3）

run1 缺陷全部为 D5 字体加宽引起（拉丁粗体在 Newsreader 下比 Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值 +12.68px）。修法只动字号 / 盒高，**未动任何文字内容**。共 13 项：

run3 追加：keys para 15.5→15（run1/run2 的 P8 `PARSE_FAIL`：D5 加宽致答案流断行切进 "36."，p8.py 无法抽取；本地 wrap 仿真 15/14.5/14/13.5 均 150/150，取最小改动 15）。

| 门 | 内容 | 修法 |
|---|---|---|
| head_check | `LIRE LE CALENDRIER　日程を読む` | content56.py:131 25→**23**（406.2px ✓） |
| head_check | `IL EST PRÉVU QUE + SUBJONCTIF` | content56.py:164 25→**23**（411px ✓） |
| head_check | `LE COMPARATIF EN POLITIQUE` | content56.py:170 25→**24**（410.1px ✓） |
| head_check | `IL EST PRÉVU QUE + SUBJONCTIF` | content7.py:38 24→**23**（411px ✓） |
| head_check | `CLINIQUE DES ERREURS　間違い` | content7.py:97 25→**24**（413.1px ✓） |
| box标题/刊头 | `LES MOTS DES FÊTES　祭りの単語` | content34.py:76 23→**22**（388.2px ✓） |
| box标题/刊头 | `DATES À RETENIR　今週のカレンダー` | content34.py:94 23→**21**（393.5px ✓） |
| box标题 tsize | `LES PHRASES DU COMMENTATEUR` | content34.py:166 23→**21**（402.5px ✓） |
| box标题/刊头 | `LES MOTS DU TENNIS　テニス用語` | content34.py:176 23→**22**（391px ✓） |
| box标题 tsize | `TROIS DATES POUR COMPRENDRE` | content56.py:194 23→**21**（391.7px ✓） |
| spill | `sh = 62 + sum(...) + 14` | content12.py:192 14→**30** |
| LINEX | `決まる、行われる。今週末はすべてが決まります。` | content12.py:116 19→**18** |
| box标题/刊头 | `keys para (kf.para)` | content8.py:161 15.5→**15** |

P8 变化：204 -> 202 行，距页脚线余量 37.1 -> 32.2 px（正，无溢出）。

## 四、门禁（run3，全套 16 门 + D18 + D37，ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0 |
| 5 webpdf | RC=0，网 PDF 1691163 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 97 of 150 |
| 8 p8 compare | PASS，CLEAN（keydiff=[135, 150]，预期读者语键） |
| 9 freeze baseline | 8/8 |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 372，预期 D5 run-split；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL |
| 12 boxtitle | 0 DEFECT（backup 已补基线 svg 为真对照） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 204 -> 202，slack 37.1 -> 32.2） |
| 15 文字层 print=web + text.md | 字符多重集差 **0**；text.md differs from issued by exactly 24 lines = 6 gloss lines (fixed `", [("` leak; rest BYTE-IDENTICAL) |
| 16 census_quotes | 0 defective |
| D18 刊头间距 | PASS，121.0px |
| D37 副刊头行 | PASS，余量 185.5pt |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL2-fr-ja.pdf`，**14,313,092 字节**，SHA-256 `c0a986e69e74f2a48cf32a9654969388c4fa08fca11f8acce6c0154b624d8198`。
- 网 PDF：`2026-w45-fr-ja.web.pdf`，**1,691,163 字节**，SHA-256 `25413f11638ef6008ffa8606c3eb3e8de156e7f3bcb17ce1e2e4cf696bdebb08`（网 PDF 字节跨次运行不确定——closer 须拷 builder 原件，绝不重跑 webpdf）。
- text.md：`2026-w45-fr-ja.text.md`，**47,804 字节**，SHA-256 `9749487b424beccbd6ba8933ff3e7b0e5f56d54a47a4839016aa07f65effc97a`（differs from issued by exactly 24 lines = 6 gloss lines (fixed `", [("` leak; rest BYTE-IDENTICAL)）。
- 练习总量仍为 **150 题**。

## 六、KIT

- `production/2026-w45/2026-w45-fr-ja/WEEKLY-KIT.md`：文末追加 D5 节（文末 D5 rebuild 节：装机、修复、终门禁 ALL-GREEN、新交付物 pins）。§14/§15 原 round-5 VOL3 pins 未动（其 pin 的是原始交付物文件名；D5 pins 在新 D5 节内）。
