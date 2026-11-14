# D5 重建报告 — 2026-w43-fr-nl（荷兰语读者版）

W43 fr 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-fr/logs/2026-w43-fr-nl/`
（`GATES-SUMMARY-run3.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` / `run2.txt` 为修前总表）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core fr --week 2026-w43 --i-understand-this-writes-production`
  → `production/2026-w43/core-fr/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-fr-nl/svglib.py --target fr --reader nl --week 2026-w43`
  （先 `--check` dry-run，10 项改动 + mode latin 正确）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留。
- D1 组装（先于安装）：patched svglib 取本地 fanout D1 版（`style-port-fr/fanout-w43/nl/svglib.py`），
  组装后与生产版 svglib 的 diff 恰为 D1 hunk 一处（28 行）；content*.py/bslib4.py 与生产版逐字节相同。
- 重建：`run.py`（W47 版）→ `render.py`（fanout 版）→ `webpdf.py` → text.md 由固定版导出器
  `scratch-prep-p3b/export_w43_fanout_fixed.py` 生成（P3b 已验）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 145**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `d1-fix/work/2026-w43-fr-nl/RESULT.txt` 的 shipped（pre-D1）SHA/字节逐字节一致。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **557**、西里尔 0、弯引号在 CJK **0**（>0，符合装机前提）。
- 基线 P8 口径：noted **67/145**（与 core 一致的印刷集）。

## 三、缺陷与修法（run1 → run2 → run3）

run1 head 计数 **9**，0 FLOW OVERFLOW。缺陷全为 D5 字体加宽引起（拉丁粗体在
Newsreader SemiBold 下比 Noto Sans CJK 宽约 5%），另 P2 spill 两处为既有缺陷（基线同值）。
修法只动字号、盒高与间距，**未动任何文字内容**。量度用装机后 svglib 自身 `text_w`；
箱标题以 creambox 实测 over 为准（`text_w` 对含空格标题低估约 1.5px/空格）。

共用法语 head 5 处：P1 `L'AUTOMNE, SAISON DES LIVRES` 25→**23**；P2 `LES VACANCES DE LA TOUSSAINT` 25→**23**；P3 `HALLOWEEN : LA FÊTE QUI DIVISE` 25→**22**；P3 `LA TOUSSAINT DANS LE MONDE` 25→**24**；P6 `LE COMPARATIF EN CAMPAGNE` 25→**24**。

共用法语箱标题 2 处：P4 `LES PHRASES DU COMMENTATEUR` +36.5px → `content34.py:176` 加 `tsize=20`；P6 `TROIS DATES POUR COMPRENDRE` +24.5px → `content56.py:222` 加 `tsize=21`。

- 读者 head ×4：P6 `LIRE LE GRAPHIQUE　DE GRAFIEK` 25→**22**；P7 `CLINIQUE DES ERREURS　PAS OP!` 25→**22**；P8 battery B `CHOIX MULTIPLE　MEERKEUZE` 24→**21**、F `LES MOTS　WOORDENSCHAT` 24→**23**。
- 箱标题：scrutin box `LES MOTS DU SCRUTIN　WOORDEN` +41.5px → 加 `tsize=20`；p.text 标题：P3 fêtes `WOORDEN` +24.3px → 21、zoom `GRAVEN VAN SCHRIJVERS` +28.6px → 21、P4 sport `WOORDEN` +15.5px → 22、P5 écrans `WOORDEN` +47.5px → 20。
- Occlusion：P6 `MICRO-DRILLS` 叠 `WOORDEN` 13.5×5.8 + LINEX、P8 `MEERKEUZE` 叠答案文 14.6×3.6、`DE GRAFIEK` 叠 `B2` 4.6×13.8 → 相关标题缩字号后消除。

Spill ×2（基线已存在，11 版同值）：P1 EN BREF 箱（`content12.py`）`La fête divise. (page 3)` +10.40px → 矩形高 416→**434**；P2 LE SAVIEZ-VOUS 箱 `lire!` +12.71px → 盒高公式尾常数 +14→**+30**（run2 曾 +34，下推 ET VOUS 盒致 P2 LINEX，run3 回调 +30 并把 ET VOUS 盒间距 26→**10**，ey3 复原）。

run2 门禁除 P2 LINEX（run2 新增：sav 盒高 +20 下推 ET VOUS 盒，末行顶到 P2 分隔线）与 en scrutin +1.5px 外全绿；run3 回调 sav 增量并补偿间距后全绿。

P8 变化：211→**186** 行，距页脚线余量 32.7→**31.7 px**（正，无溢出）。

## 四、门禁（run3，全套 16 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 145，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0，印 PDF 8,680,274 B |
| 5 webpdf | RC=0，网 PDF 1,705,000 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 67/145 |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[71, 72, 73, 132, 145]（与 KIT 记载的读者语答案键一致）） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 338，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（146 OBSERVE） |
| 12 boxtitle | 0 DEFECT（36 titles，296 body lines；备份 svg 已补，backup 解析正常） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（median=1.006，boldT=1.057，boldF=0.979；P8 211→186，slack 32.7→31.7） |
| 15 文字层 print=web | 字符多重集差 **0**（各 107,067 字符） |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | fr 家无 gates.py（PLAN §3.1 之“如有”不适用） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-fr-nl.pdf`，**8,680,274 字节**，
  SHA-256 `90b142516be6b2cbf43efd803c404ae0e5c8559a9bbbd2c5904e9c7707900c71`
  （D5 前 KIT 值见 §六）。
- 网 PDF：`2026-w43-fr-nl.web.pdf`，**1,705,000 字节**，
  SHA-256 `6a8fec6be9a30435e8dd6f8ef9ef7ca9f4ec852dcfe99188a9e301b723383808`
  （D5 前 issues 已发版 1,742,059 字节，`bbbafbfd…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `0c497143f4fbc68b130f7d6130949f084a81f631f64d5916622fff5e63184006`）。
- 练习总量仍为 **145 题**，与 core 逐题一致。

## 六、KIT

- `production/2026-w43/2026-w43-fr-nl/WEEKLY-KIT.md`：交付物区追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 重建记录（2026-11-13）**（装机、基线、
  缺陷与修法、门禁 ALL-GREEN、新交付物）。
