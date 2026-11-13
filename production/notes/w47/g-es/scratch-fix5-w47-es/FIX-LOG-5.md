# FIX-LOG-5 — W47 es 家庭第五轮修复 J1（text.md 小写词拼接粘连）

- **轮次**：第五轮修复（PROOF-NOTE-5 §3 的 J1，low；text.md 专属）
- **日期**：2026-11-12（UTC 20:09–20:15 前后；门禁 GATES5 DONE 20:11:28）
- **范围**：`production/2026-w47/` es 家庭 11 版：core-es（= es-zh-cn）+ `2026-w47-es-{de,en,fr,it,ja,ko,nl,pt,ru,zh-tw}`；被碰 7 版：de/en/fr/it/nl/pt/ru
- **结论：全部修完 — 实修 13 处，0 处未修；全家重扫无新增残留。**

## §1 总表

| 版 | `confinal` | `unasondeo` | `unamuestra` | `Esjueves` | 合计实修 | PROOF-NOTE-5 表列 | 差 |
|---|---|---|---|---|---|---|---|
| es-de | 1 | 0 | 0 | 0 | **1** | 1 | 0 |
| es-en | 1 | 1 | 0 | 0 | **2** | 2 | 0 |
| es-fr | 1 | 1 | 0 | 1 | **3** | 3 | 0 |
| es-it | 1 | 1 | 0 | 0 | **2** | 2 | 0 |
| es-nl | 1 | 0 | 0 | 0 | **1** | 1 | 0 |
| es-pt | 1 | 0 | 1 | 0 | **2** | 2 | 0 |
| es-ru | 1 | 0 | 1 | 0 | **2** | 2 | 0 |
| **合计** | **7** | **3** | **2** | **1** | **13** | **13** | **0** |

## §2 逐处记录（13 处）

| # | 版 | 行 | 旧串 → 新串 | 断句归属 |
|---|---|---|---|---|
| 1 | es-de | L1150 | `confinal` → `con final` | P6 Q88 C 尾 `con` + Q92 A 尾 `final` |
| 2 | es-en | L1150 | `confinal` → `con final` | 同上 |
| 3 | es-en | L1150 | `unasondeo` → `una sondeo` | Q92 C 首词 `una` + D 框首词 `sondeo` |
| 4 | es-fr | L1154 | `confinal` → `con final` | 同上 |
| 5 | es-fr | L1154 | `unasondeo` → `una sondeo` | 同上 |
| 6 | es-fr | L1756 | `Esjueves 19` → `Es jueves 19` | 答案 101 注释尾 `Es` + 答案 139 残片 `jueves 19`；以印层 `jueves 19` 为准（该行原已带 ` 19`，手术为 `Es` 与 `jueves` 间插 1 空格，不重复写 `19`） |
| 7 | es-it | L1152 | `confinal` → `con final` | 同上 |
| 8 | es-it | L1152 | `unasondeo` → `una sondeo` | 同上 |
| 9 | es-nl | L1170 | `confinal` → `con final` | 同上 |
| 10 | es-pt | L1154 | `confinal` → `con final` | 同上 |
| 11 | es-pt | L1154 | `unamuestra` → `una muestra` | Q92 C 首词 `una` + D 框次词 `muestra` |
| 12 | es-ru | L1201 | `confinal` → `con final` | 同上 |
| 13 | es-ru | L1201 | `unamuestra` → `una muestra` | 同上 |

完整 13 处逐条记录（版/行/旧串/新串）见 `fix-report.json`（`applied` 数组）。

## §3 印层核验 — 13/13 通过（双抽取交叉核对）

每处先与同版印 PDF 文字层核对断句，两种抽取互相印证（PDF 未动，SHA 与 PROOF-NOTE-5 §1 一致）：

- **新鲜抽取**：本轮以 venv python + PyMuPDF 自印 PDF 重抽 11 版文字层（`txt-print/es-*-print.txt`，各 8 页）。
- **对照抽取**：第四轮 `pdftotext -layout` 印层 txt（`scratch-reproof4-w47-es/txt/*-print.txt`，PDF 未变，仍有效）。
- **粘连串不在印层**：`confinal` / `unasondeo` / `unamuestra` / `Esjueves` 在两种抽取、7 版中均为 **0**。
- **分隔形式在印层**（空白归一化后）：
  - `con final`：`-layout` 视觉行 7 版各 1 处（`… C. solo datos oficiales, con     final · B. una foto …`，同行空格分隔）；PyMuPDF 阅读序 7 版真短语齐全（`solo datos oficiales, con fuente` + `A. un resultado final`）。
  - `una sondeo`（en/fr/it）：en 的 `-layout` 视觉行 1 处（`· C. una sondeo · muestra · …`）；fr/it 的 `-layout` 中 `una` 与 `sondeo` 分处相邻两视觉行（fr L584 框行尾 `… l'encadré : sondeo` / L586 行 `· C. una        · muestra …`；it L586/L587 同式），两词分明、从未粘连；PyMuPDF 阅读序 3 版真短语齐全（`C. una promesa` + 框 `sondeo · muestra · indecisos`）。
  - `una muestra`（pt/ru）：ru 的 `-layout` 视觉行 1 处（`· C. una muestra · indecisos · …`）；pt 的 `-layout` 中 `una` 与 `muestra` 分处相邻两视觉行（L591 框行 `Complete com as palavras: sondeo · muestra` / L592 行 `· C. una        · indecisos …`）；PyMuPDF 阅读序 2 版真短语齐全（同上）。
  - `Es jueves 19`（fr）：`-layout` 视觉行 1 处（`101. Es — Pour 1 heure, on emploie le singulier Es jueves 19 64. La jornada …`）；PyMuPDF 阅读序 `singulier Es` 1 处（答案 101 尾）+ `jueves 19` ×21（各为答案 139 一带残片所属的正当位置）。
- **结论**：13 处断句与印层完全一致——两词在印版中本就分开（同行空格或相邻行），text.md 的粘连纯属导出器栏间拼接丢空格；无一处印层亦粘连或无法判定，故无未修项。

## §4 修复方法与断言

- **手术式行内替换**：只改 7 份 `*.text.md`，逐行 span 替换（每处插 1 个空格；fr L1756 为 `Esjueves 19` → `Es jueves 19`，即 `Es` 与 `jueves` 间插 1 空格），未全量重导出 text.md（FIX-LOG-2 导出器陷阱：重导会重分段约 200 行/版）。脚本 `fix5.py`，解释器 `~/workspace/weekly-git/tools/venv/bin/python`。
- **断言**：每处替换前断言原文在记录行号上恰为 1 处；替换后断言 4 个旧串全文件计数均为 0、新串在位；落盘后逐版 diff 核对——diff 只含意改行（de 1 行、en 1 行、fr 2 行、it 1 行、nl 1 行、pt 1 行、ru 1 行），行数变化为 0（纯行内替换，不增删行）；逐版行级逆向还原（新串→旧串逐行 revert）与修复前备份 `text-pre-es-*.md` 逐字节相同（`verify_after.py`）。
- **PDF 未动**：7 版印/网 PDF SHA-256 与 PROOF-NOTE-5 §1 逐项核对，全部不变（印/网 SHA 不变是 KIT 更新的前提）。

## §5 全家重扫 — 无新增残留

**方法**（PROOF-NOTE-5 §3 建议的词表差集法；脚本 `rescan.py`，结果 `rescan.json`）：

- 每版 text.md 词表（拉丁词 len≥2 + 西里尔词 len≥2，小写化）减印层词表（新鲜 PyMuPDF 抽取 ∪ 第四轮 `-layout` 抽取，两源取并集，PDF 未变）；差集候选逐项看上下文定性。
- **方法自验**：同一差集法跑修复前备份 `text-pre-es-*.md`——7 版候选恰为 4 个粘连词 + 语言代码 artifact + `Portada`，13 处旧串全部命中（de `confinal`、en `confinal`+`unasondeo`、fr `confinal`+`unasondeo`+`esjueves`、it `confinal`+`unasondeo`、nl `confinal`、pt `confinal`+`unamuestra`、ru `confinal`+`unamuestra`），证明该法对本类缺陷无漏网。
- **修后结果**：11 版差集候选仅剩两类非缺陷（逐项核实）：
  - `Portada` ×1/版（11 版全有）：text.md L3 导出器自带节标题 `## Portada`，非报纸正文词，不在印层——单字实词，非粘连。
  - 语言代码 artifact（L1 文件头 `# 2026-w47-es-xx` 的 slug 分词）：core `zh`/`cn`、fr `fr`、it `it`、ja `ja`、ko `ko`、nl `nl`、pt `pt`、ru `ru`、zh-tw `zh`/`tw`，各 ×1；`de`/`en`/`es` 未入候选（其本身即印层实词）。非粘连。
- **结论：无新增同类小写粘连残留，无一并修。**
- **附带复扫**（9 类模式，`rescan.py` 后半段；与 FIX-LOG-4 §4 同类）：数字粘连/句号→大写/句号→小写/驼峰/逗号/中点/右括号/分号粘连 11 版均为 0，命中仅为已知排除项——`29N`（每版 2 处，有意缩写）、品牌驼峰 `laSexta` ×9 / `LaLiga` ×1 / `MiDNI` ×8、slug `w47` 中的 `w4`（L1 文件头）、pt 时刻 `21h30`/`12h00`/`18h30`/`14h00`（`h3`/`h0` 命中为时刻写法本身，合法）。

## §6 未修 / 歧义项

- **未修：0 处。** 13 处候选全部印层核验通过，无"印版亦粘连或无法判定"项。
- **排除项（已核查，不动）**：见 §5（`Portada` 节标题、语言代码 slug、`29N`、品牌驼峰、pt 时刻、`w47` slug）。

## §7 逐版 text.md 新旧 SHA 对照

| 版 | 旧字节 → 新字节 | 旧行数 → 新行数 | 改动行 | 旧 SHA-256 | 新 SHA-256 |
|---|---|---|---|---|---|
| es-de | 45,369 → 45,370 | 1803 → 1803 | 1 | `92013d1495760a8a45983beb89be565502e346945d35854d40d76c11bdf44a0c` | `ff0387066ca9ad21400cae865592e43ad24c029693a2e7883733e87440b57b6e` |
| es-en | 45,044 → 45,046 | 1798 → 1798 | 1 | `dd34d3a3cd4857ab26da2e679508b04ddb9344f6a38731d21b26ed1062937a3a` | `3c2ef9876638c384cd5c5b4288b55d2917e65756d1d431daf11a2474ad2a680b` |
| es-fr | 45,831 → 45,834 | 1816 → 1816 | 2 | `0086ceee4c72a38b365870ead29c34b6531fda78980fca642c67051cce6a9bee` | `ad8bcbcd0c4fa340840baf16e3927bdd23363bf3478bf255c66da74d70ab45f5` |
| es-it | 45,209 → 45,211 | 1807 → 1807 | 1 | `f9d0cf98767b6c2721e88b78345ce4f54f9e32c6b205a70e710861b11a594bdf` | `491044bcfaab758cb49187d07f5aa19e16be568844867c8977a80583ee3d4755` |
| es-nl | 45,341 → 45,342 | 1836 → 1836 | 1 | `2afcdcf2c3094e5c5b9cce14ac4abf9e5d41bb34b0c71f289746345ec7d5b6d0` | `d477656f5ef01f954068e4d002e424a16b3a872b911d22c3280c03feda911fd5` |
| es-pt | 45,574 → 45,576 | 1816 → 1816 | 1 | `7c7ad36c3eb91c330e578acfea7b502d183e97cf0dea9d8ac9e22ca36e52bedd` | `7db6b340f4f631b4aa2b3c3c596dbcba57aa39c8124d7b6905cc7a38f4f7ce2f` |
| es-ru | 52,365 → 52,367 | 1889 → 1889 | 1 | `6f89a108c8fdb314083cb44f7e8b34b409b4d9dab50b1e2af1f5b0b18bc240a6` | `ac246f8709d3535958ccebb3b6913800bd3866001de5322358d3ba026f69c42b` |

每处 +1 字节（1 个 ASCII 空格），字节增量 = 修复处数。行数按 FIX-LOG-4 惯例计（`split("\n")` 计数，含末尾空元素；`wc -l` 计为各少 1：de 1802、en 1797、fr 1815、it 1806、nl 1835、pt 1815、ru 1888——同一文件、两种计数口径，行数变化均为 0）。注：ru KIT H1 节"文件："行写"1888 行"（`wc -l` 口径），与 I1/J1 节的 1889 行口径不同——为既有写法差异，本轮未动该数字（行数本身未变）。

## §8 KIT 更新

- 每版 `WEEKLY-KIT.md` 仅改现行 text.md 段（de/en/fr/it/nl/pt 为 F2/F3/F4 节"新 PDF"行；ru 为 H1 节"文件："行，按 FIX-LOG-4 §8 惯例）：text.md 字节数 + SHA 更新为盘上实时值；印/网 PDF 字节数与 SHA 一字未动（已逐版断言：目标行改后仍含原印/网完整 SHA；ru 行字节注由"（I1 +18 B）"改为"（I1 +18 B，J1 +2 B）"、text.md"改前"指向 I1 状态 `6f89a108…`）。
- 每版 KIT 末尾追加 `## 第五轮独立重校修复 J1（2026-11-12，PROOF-NOTE-5 §3 返修）` 一节（改动/重建/文件/门禁/日志，沿用前轮格式）。
- 独立核验（`verify_kit.py`）：7 版新 text.md SHA 各出现 2 次（现行行 + J1 节）；旧 SHA 各 2 次（I1 节"文件："行 + J1 节"改前"；ru 另 +1 次为 H1 行"改前"，共 3 次，符合链式记录）；I1 节"文件："行字节数未动（仍为 J1 前值）；I1/J1 两节各 1 处。

## §9 门禁（`gates5.sh`，GATES5 DONE 20:11:28）

| 版 | p8 extract | p8 compare vs core-es |
|---|---|---|
| es-de | 150/150 rc=0 | CLEAN，keydiff [137, 138] |
| es-en | 150/150 rc=0 | CLEAN，keydiff [137, 138] |
| es-fr | 150/150 rc=0 | CLEAN，keydiff [137, 138] |
| es-it | 150/150 rc=0 | CLEAN，keydiff [137, 138] |
| es-nl | 150/150 rc=0 | CLEAN，keydiff [137, 138] |
| es-pt | 150/150 rc=0 | CLEAN，keydiff [137, 138] |
| es-ru | 150/150 rc=0 | CLEAN，keydiff [137, 138] |

- p8 extract 7/7 为 150/150；compare 7/7 CLEAN（keydiff [137, 138] 为已裁定的翻译题设计差异，与第五轮一致）。
- 未重渲染 PDF（PDF 未动，印/网 SHA 不变）；未跑 lint，未 commit，未 push，未改 SOP，未碰其他家庭/其他周。

## §10 工作记录

- 只碰 `production/2026-w47/2026-w47-es-{de,en,fr,it,nl,pt,ru}/` 的 `*.text.md` + 各版 `WEEKLY-KIT.md`（共 14 个文件，以 mtime 核实；未碰版 core/ja/ko/zh-tw 的 text.md mtime 仍为 19:32，未动），及本 scratch 目录；未动任何 `.py` / `.pdf` / `.svg`；解释器 `~/workspace/weekly-git/tools/venv/bin/python`。
- 磁盘：开工 95G 已用 / 55G 空闲（150G 盘），结束 95G，未触发 ≥100G 门限。
- 工作目录 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix5-w47-es/`：`FIX-LOG-5.md`（本文件）、`fix5.py`、`fix-report.json`（13 处全量记录 + 新旧 SHA）、`text-pre-es-*.md`（7 份修复前备份）、`verify_print.py` / `verify_after.py` / `verify_kit.py`（核验脚本）、`extract_print.py` / `extract_print_all.py` / `txt-print/`（11 版印层新鲜抽取）、`rescan.py` / `rescan.json` / `rescan_pref.py`（全家重扫 + 方法自验）、`kit5.py`、`gates5.sh` / `gates5.log` / `p8-extract-*.json,log` / `p8-compare-*.json,log`。
- 过程注记：`verify_after.py` 首版把 pt 网 PDF SHA-12 误写作字节数混入串（`804705c8eb9`），断言失败后核对 PROOF-NOTE-5 §1 更正为 `06514f66f69d`，重跑全过——误写在期望值一侧，盘上文件无误；`kit5.py` 首版 ru 断言 `old_sha not in new_line` 未考虑 ru 行"改前"链式保留旧 SHA，已修正为 ru 允许 1 次、其余 0 次，重跑全过。
- 建议下一步：按 SOP §8.4 对被碰 7 版做新一轮独立重校（第六轮）；导出器根治时补词表差集扫描——本轮已验证该法对小写粘连无漏网（§5 方法自验），可直接作为导出后门禁。
