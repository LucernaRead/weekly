# GATE-LOG — W47 it-es 重扩散后独立复校（re-proof）

工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-es/`（下称 `$S`）。全部输出落 $S；生产只读（收工重验：16 个 SVG sha256 与开工前逐字节一致，`svg-sha-before.txt` vs `svg-sha-final.txt` 无 diff；三件 SHA 与开工值一致）。`PYTHONDONTWRITEBYTECODE=1` 全程，`TMPDIR=$S/tmp`，未写 /tmp。解释器 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0，FreeType 2.14.3）。

## 0. 探针与 SHA（开工前）

| 检查 | 结果 |
|---|---|
| `git -C ~/workspace/weekly-git hash-object -w /dev/null` | 成功，`e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0 |
| scratch 真实写文件 `$S/probe.txt` | 成功（2026-11-11T21:59:00Z） |
| 印 PDF SHA / 大小 | `6c299214601b4936dc5329cc72627919fe3b27b90f742298a2eae8cb03554769` / 14,033,619 B ✓ 与任务给定一致 |
| 网 PDF SHA / 大小 | `c194c3421415c75ed089ced802aae069d6bbd6c3de10c9a4e694cac58c447862` / 1,291,397 B ✓ |
| 文本 SHA / 大小 | `4fd5647e2b7a13812b384963607bd67eda2c2c4fe6bd197b9b08bc08eee21643` / 56,193 B ✓ |
| 重扩散前生产三 SHA（`shas-pre.txt`） | 印 `8b7547d315a50de4858d6971483f79951c2d497ef28e4f71dc66942bc405411b` / 网 `efc1404b8797a8b133fdafe911c1886a9a2be24158a2e49a4dcaeb657cdb9266` / 文 `64a8ac2fce4e7063c7bebfcbb5b6cde2f8fe1fbde4f265a510e6abf83d007031` ✓ 与任务给定一致；文 −21 B（56,214→56,193） |

## 1. 回归 A：D-2 修正（逐项独立重测）

| 检查 | 结果 |
|---|---|
| `text.md:775` 新句 1× | `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` ✓（整句在位） |
| `text.md:777` 新句 1× | `Il verbo è leggere, regolare al futuro: leggerò.` ✓（整句在位） |
| 旧串 `Le forme sono regolari: andare` | text.md 0 / content*.py 0 / 8 SVG 0 / 印+网 PDF 全文 0 ✓ |
| 旧串 `irregolare al futuro: leggerò` | 同上，全部 0 ✓ |
| 新串 `content7.py:17/:18` | 在位，各 1× ✓ |
| 新串 p7 SVG（flat 文本） | 各 1×；旧串 0 ✓（节点拆分：`assaggerò, guardare` / `verbo è leggere, regolare al futuro: leggerò.` 各一节点） |
| 新串 印/网 PDF P7 文字层 | 各 1×、旧串 0 ✓（注：须先做空白+箭头归一化——PyMuPDF 在行尾插换行、箭头粘词 `→assaggerò,` / `guardare→`；未归一化的直接计数为 0，属提取形态问题、非内容缺失，已用归一化重测确认） |
| P7 `andare` 残留 | 文字层 2 处：Q101 题干 `(andare)` + ERRORI TIPICI `Andare vuole essere, non avere. andare lleva essere como auxiliar.`——均合法，与 D-2 旧串无关。fanout 报告“P7 出现一次”少计一处，见 PROOF-NOTE O4 |
| 与重扩散前生产版 diff（`backup/`） | text.md 恰 2 行（775/777 replace），−21 B ✓；content diff 仅 `content7.py` 17–18 行（2 行换 2 行）✓；SVG p1–p6/p8 逐字节一致、仅 p7 不同；cards p1–p6/p8 逐字节一致、仅 p7 不同 ✓；两 PDF 因 P7 重建而变 ✓ |
| p7 SVG 文本多重集 diff（不含坐标） | 仅 D-2 碎片：旧 8 非空节点（`andare` / `→` / `andrò, assaggiare` / `assaggerò,` / `guardare` / `verbo è leggere, irregolare al futuro:` / `leggerò.`）→ 新 3 非空节点（`assaggiare` / `assaggerò, guardare` / `verbo è leggere, regolare al futuro: leggerò.`）✓ |
| p7 位置重排（同文本） | A2 段少一行，Q101–104 整块上移 32.68 px（如 101. y 751.75→719.07），文本一字未动；KIT §12“仅限 2 条 D-2 句”指文本内容，位置重排未写明，见 PROOF-NOTE O6 |

## 2. 回归 B：P7 教学句语义（公开依据独立检索，2026-11-11）

- andare 未来时不规则（词干 andr-，andrò ≠ *anderò）：LibreTexts《Indicativo futuro》不规则词干表（andare → andr-，并以 leggere 作规则 -ere 例）、FlexiClasses（Andare → io andrò，列入不规则表）、dante-learning（vowel-drop 组：andare → andr-）。
- leggere 未来时规则（leggerò = 规则构形）：LibreTexts 同表以 leggere 为规则 -ere 动词例（io leggerò）。
- 结论：新句两处规则性标签均正确；L17 第 1 句 `andremo` 与桥句 `andremo、assaggeremo、guarderemo、leggeremo。` 未作规则性断言，指涉不悬空。**PASS**

## 3. 门禁 gates.py es（`$S/gates-es.log`，20/20）

复用 `scratch-fanout-it/gates.py`（拷入 $S，SCRATCH 改指 $S，`translations.py` 同拷），独立重跑。首次运行 4 FAIL（p8 extract/compare、freeze diff report、textmd validate）均为本人改写脚本路径的错误（`$S/es/` 目录未建；`validate_edition_textmd.py` 路径被 sed 写成双重前缀），修正后重跑 **20/20 ALL PASS，rc=0**：

- occlusion 0 flags（`tools/occlusion_audit.py`，自测先行）✓
- p8 extract noted=150 rc=0 ✓
- p8 compare vs core：verdict **CLEAN**，keydiff **[137, 138, 139]**（预期内的重定向翻译键）✓
- freeze diff P1–P7：unexplained_add=[] unexplained_rem=[]；pages 1–8 齐全 ✓
- freeze strict-cjk：新增 CJK 仅 8 × U+3000（页脚分隔符，SOP §1.1 豁免；rc=1 系 freeze.py 对任何新增 CJK 的返回值）✓
- 印/网文字层字符多重集一致：各 7,998 词 ✓
- web PDF 1,291,397 B < 7 MB；印 PDF 14,033,619 B ✓
- P8 最小字号 SVG 13.0 px = 9.75 pt ✓
- 纸色 #fbfaf6；禁色 0；VOL.5 文本节点 3（仅预告/披露）；VOL.4 ×9；徽章色 A2/B1/B2 齐全；全页矩形框 0；“·”148 处 ✓
- text.md validate forward-miss 0 / reverse-miss 0 ✓
- 答案 150（版=核心=150）；键 1–150 与核心一致（137–139 重定向、写作题除外），mismatches=[] ✓
- 注释与 translations.py 一致（137–140 + 写作除外），mismatches=[] table_gaps=[] ✓

## 4. freeze baseline（两次，`$S/freeze*.log/json`）

- **核心** `--build core-it --core-svg core-it/svg`：**8/8 byte-identical**（repointed：render.py, content12/34/56/7/8.py）；build-copy 核实确为 core-it 自身（内含 `2026-w47-it-zh-cn.text.md`、`La-Lucerna-VOL4.pdf`，`2026-w47-it-es` 出现 0 次）；核心 p7 SVG `a7e6afa4…` 与 FIX-LOG 修后值一致；发运核心 SVG 运行前后重哈希无变化。
- **本版** `--build 2026-w47-it-es --core-svg 2026-w47-it-es/svg`：**8/8 byte-identical**；build-copy 核实为本版（内含 `2026-w47-it-es.text.md`、`La-Lucerna-VOL4-ES.pdf`）；发运 SVG 运行前后重哈希无变化。
- 两次运行后生产 SVG sha256 与开工前逐字节一致（`svg-sha-before.txt` = `svg-sha-after.txt` = `svg-sha-final.txt`）。

## 5. 印 PDF 重建逐字节（`$S/rebuild_print_pdf2.py`，`rebuild_print_pdf.log`）

freeze build-copy 的 8 个 SVG（已验与交付逐字节一致）经 cairosvg+pypdf 同款流程重建印 PDF：sha256 `6c299214601b4936dc5329cc72627919fe3b27b90f742298a2eae8cb03554769`，14,033,619 B，与交付 **BYTE-IDENTICAL**。注：proof2 的原脚本指 `$S/run-copy`（本轮无 run-copy，且不直接跑 run.py——其 OUT 为硬编码生产路径），改指 freeze build-copy 后跑通。

## 6. 奶油盒扫描（`$S/creambox.log`，canonical `tools/creambox.py`，8 页 29 盒）

- 盒内余量 ≥ +4.5 px；7 处“last baseline 负余量”皆 BELOW-WINDOW 假阳性，inside-only 余量均为正：P1 LA PAROLA +16.0 / P3 IL TORRAZZO +47.7 / P4 赛果表 +22.0×3 / P6 ESERCIZI +31.2、+90.0。
- desc-clear 负值 10 处：6 处末行无下行字母（0.30em allowance 假阳性）；4 处末行有真实下行字母，交付印 PDF 200 dpi 像素裁定（`$S/pixel_boxes.py`，`render/p-*.png`）：
  - P3 E TU：盒下 +1..+40 渲染 px 暗像素 0；最深墨 svg 1289.76，盒底余量 **+0.84 px** ✓
  - P5 E TU：同上 0；最深墨 1248.96，余量 **+0.84 px** ✓
  - P7 LA PAROLA：同上 0；最深墨 1343.52，余量 **+0.48 px**（proof2 报 0.96 px，相差 1 渲染 px；墨仍在盒内，见 PROOF-NOTE O7）✓
  - P7 LETTERE：盒下 +1..+15 渲染 px 暗像素 0；+1..+40 暗像素 2,643——全部是盒下 13.2 svg px 处的有意橄榄绿分隔线（`crop-p7-lettere-below.png` 目视确认：末行 `…pasa al VOL.5.` 完整在奶油盒内，下方为绿线，无文字溢出）；最深墨行 1686.24 即该绿线 ✓
- **spill 0**。P7-TOOLBOX 小结：3 盒，最小 inside 余量 +4.5，最小 desc-clear −1.5（上列已裁定）。

## 7. 几何扫描（`$S/geom_scan.log`，交付印 PDF，PyMuPDF）

- 8 页：0.5 pt 容差下超页边字符 **0**；无字符超页底；非页脚文本跨越 1977 pt 版心底边 **0** 处。
- 各页最小字号（pt）：P1–P5/P7 **11.62**，P6 **12.75**，P8 **9.75**（恰 SOP §1.1 下限）；网 PDF 各页一致。
- P1 顶栏 VENEZIA 末字母 A：300 dpi 裁图（`render/crop-p1-band-right.png`）+ 像素测量：最右墨 x=1462.32 pt（页宽 1462.5），字形完整、右腿 serif 恰触页边（advance-box 超 0.08 pt 属取整伪影；见 PROOF-NOTE O2）。

## 8. P8 孤儿检查（4 栏流，SVG 几何独立重算）

旧脚本按 3 栏分组报“188 项、40 跨栏断裂”——为分组伪影（P8 实际为 4 栏；RISPOSTE 每栏起始行 x=88/538.5/989/1439.5）。按 4 栏重算：

- RISPOSTE：col1 1–37、col2 38–75、col3 76–112、col4 113–150，各栏连续、栏首均为新题号（1/38/76/113，y≈1421–1453）、栏末题 37/75/112/150 均在本栏内结束（y 2504–2536，底 2552）。
- 练习：col1 113–124、col2 125–134、col3 135–146、col4 147–150，连续有序。
- 栏内 y 间距 >60 的 5 处逐行裁定皆为栏界伪影：124→RISPOSTE 标题（136.5）、37→页脚行（87.6，y=2624）、144→G 节标题（74.0）、146→RISPOSTE 副标题（63.2）、150→范文后配图说明/图注（234.8/110.7，范文 11 行本身连续 20.8 px 行距）。
- **跨栏断裂题 0；栏首续行 0。**

## 9. 盒标题横向溢出（STRADDLE 规则 + 备份对照）

- P7 全部标题节点（14 个，含 `A2 IL FUTURO`、`ERRORI TIPICI ERRORES TÍPICOS`、`LA PAROLA PALABRA DE LA SEMANA` 等）与备份旧版逐字逐坐标一致（`titles old==new: True`）→ 与备份不同即回归：**无回归**。
- p1–p6/p8 SVG 与备份逐字节一致 → 标题无任何变化 → **无回归**。
- occlusion BOXTITLE 类 0 flags；P6 `LE MINIME DI ESEMPIO MÍNIMAS DE EJEMPLO (DATI INVENTATI PER L'ESERCIZIO)` 在盒上横条内，渲染目视完整。**STRADDLE 判定：0 缺陷（无字形被裁、无墨水重叠、无备份差异）。**

## 10. 日期星期全验（`date`，Europe/Rome）

11-06 周五、07 周六、08 周日、09 周一、12 周四、13 周五、14 周六、15 周日、16 周一、17 周二、19 周四、20 周五、21 周六、22 周日、23 周一、24 周二；12-02 周三、12-06 周日、12-31 周四；10-15 周四、10-28 周三；1441-10-25 周一——与正文全部一致。**PASS**

## 11. 文字层与 KIT/ABSTRACT

- `pdftotext`（无 -layout）：印/网各 **46,032 B**，一致（与 KIT §7 “46,032 text bytes” 相符；`-layout` 版各 107,134 B，亦一致）；PyMuPDF 字符数各 43,606。
- KIT §7/§12 三 SHA 与字节与盘上逐字一致；§12 D-2 节陈述与本轮实测一致（§12 行 94 的“仅限 2 条 D-2 句”措辞见 O6）。
- ABSTRACT.txt：西语单行 428 B，无 ASCII 双引号，含 La Lucerna、italiano、A2–B2、150 ejercicios；事实与本期一致。**PASS**

## 12. 三源 150 题（机械层）

- 题干编号：141 条单行题干 + 3 组组题头（25–28、52–55、141–144）= 150 题，无缺号、无重号；分级 A2 47 / B1 70 / B2 33（与 KIT 一致）。
- P8 extract 150/150；edition text.md 答案 vs core text.md 答案 150/150 一致（137–139 重定向、写作题除外）；P8 印刷键 vs 核心 CLEAN（keydiff [137,138,139]）。
- 范文实测 **99 词**（80–100 词题面要求内）；8 金句各出现恰好 **2 次**（正文 + P7）；text.md CJK 0、翻譯/翻译 0。
- 150 题语义逐题手验见 PROOF-NOTE §4（全文 1317 行逐行读完）。

## 13. 事故记录

- gates.py 首次运行 4 FAIL：本人改写路径所致（见 §3），与内容无关；修正（建 `$S/es/`、修双重前缀路径）后重跑 20/20。未动生产。
- 未直接跑 run.py / render.py：其 OUT/BASE 为硬编码生产绝对路径（proof2 §11 同一教训）；重建验证只用 freeze.py baseline（自带 repoint）+ freeze build-copy 重建 PDF。
