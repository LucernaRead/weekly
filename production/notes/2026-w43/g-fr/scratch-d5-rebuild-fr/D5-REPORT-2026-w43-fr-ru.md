# D5 重建报告 — 2026-w43-fr-ru（俄语读者版）

W43 fr 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-fr/logs/2026-w43-fr-ru/`
（`GATES-SUMMARY-run3.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` / `run2.txt` 为修前总表）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core fr --week 2026-w43 --i-understand-this-writes-production`
  → `production/2026-w43/core-fr/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-fr-ru/svglib.py --target fr --reader ru --week 2026-w43`
  （先 `--check` dry-run，10 项改动 + mode ru 正确）。装后 `_D5_READER = "ru"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留。
- D1 组装（先于安装）：patched svglib 取本地 fanout D1 版（`style-port-fr/fanout-w43/ru/svglib.py`），
  组装后与生产版 svglib 的 diff 恰为 D1 hunk 一处（28 行）；content*.py/bslib4.py 与生产版逐字节相同。
- 重建：`run.py`（W47 版）→ `render.py`（fanout 版）→ `webpdf.py` → text.md 由固定版导出器
  `scratch-prep-p3b/export_w43_fanout_fixed.py` 生成（P3b 已验）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 145**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `d1-fix/work/2026-w43-fr-ru/RESULT.txt` 的 shipped（pre-D1）SHA/字节逐字节一致。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **442**、西里尔 310、弯引号在 CJK **0**（>0，符合装机前提）。
- 基线 P8 口径：noted **67/145**（与 core 一致的印刷集）。

## 三、缺陷与修法（run1 → run2 → run3）

run1 head 计数 **0**，0 FLOW OVERFLOW。run1 仅 spill 一门红（P2 两处既有缺陷，基线同值）。
修法只动字号、盒高与间距，**未动任何文字内容**。量度用装机后 svglib 自身 `text_w`；
箱标题以 creambox 实测 over 为准（`text_w` 对含空格标题低估约 1.5px/空格）。

共用法语 head：本版无缺陷（D5 后 head_check 全过），未改。

共用法语箱标题：本版无缺陷（D5 后 boxtitle/creambox 全过），未改。

- 读者 head / 箱标题：无缺陷（西里尔文在 Noto Sans 下收窄，D5 后 head/boxtitle/creambox 全过）。
- 仅 spill ×2（共用）与 run3 sav 补偿（共用）。

Spill ×2（基线已存在，11 版同值）：P1 EN BREF 箱（`content12.py`）`La fête divise. (page 3)` +10.40px → 矩形高 416→**434**；P2 LE SAVIEZ-VOUS 箱 `lire!` +12.71px → 盒高公式尾常数 +14→**+30**（run2 曾 +34，下推 ET VOUS 盒致 P2 LINEX，run3 回调 +30 并把 ET VOUS 盒间距 26→**10**，ey3 复原）。

run2 门禁仅 P2 LINEX 一门红（run2 新增：sav 盒高 +20 下推 ET VOUS 盒，末行顶到 P2 分隔线）；run3 回调 sav 增量并补偿间距后全绿。

P8 变化：208→**198** 行，距页脚线余量 32.7→**32.7 px**（正，无溢出）。

## 四、门禁（run3，全套 16 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 145，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0，印 PDF 9,033,989 B |
| 5 webpdf | RC=0，网 PDF 1,968,635 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 67/145 |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[71, 72, 73, 132, 145]（与 KIT 记载的读者语答案键一致）） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 222，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（154 OBSERVE） |
| 12 boxtitle | 0 DEFECT（45 titles，397 body lines；备份 svg 已补，backup 解析正常） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（median=0.998，boldT=0.963，boldF=1.022；P8 208→198，slack 32.7→32.7） |
| 15 文字层 print=web | 字符多重集差 **0**（各 106,829 字符） |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | fr 家无 gates.py（PLAN §3.1 之“如有”不适用） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-fr-ru.pdf`，**9,033,989 字节**，
  SHA-256 `df80755b444a4efd6811346dc9fac6b4ece0c473244f17cf08e0dad5106b4103`
  （D5 前 KIT 值见 §六）。
- 网 PDF：`2026-w43-fr-ru.web.pdf`，**1,968,635 字节**，
  SHA-256 `5992c782b1f7b1307c4530ecd2133999c3e15cbd61f1aabb3217d845c8d4af1c`
  （D5 前 issues 已发版 1,809,364 字节，`e0688ed4…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `02e10cd09e7af51737861a3599ad03eabf978002861247668f1563df4c895502`）。
- 练习总量仍为 **145 题**，与 core 逐题一致。

## 六、KIT

- `production/2026-w43/2026-w43-fr-ru/WEEKLY-KIT.md`：交付物区追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 重建记录（2026-11-13）**（装机、基线、
  缺陷与修法、门禁 ALL-GREEN、新交付物）。
