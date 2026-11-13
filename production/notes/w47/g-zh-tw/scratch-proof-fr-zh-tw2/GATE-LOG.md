# GATE-LOG — W47 fr-zh-tw proof2（re-fanout #2 独立复跑）

- 时间：2026-11-11 15:50–17:10 EST；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR：本目录 `tmp/`。另：开工前读过 `~/workspace/weekly-git/AGENTS.md`（内容仓指南；本次只复校、不入库，无冲突）。
- 探针：`/dev/null` 存在；`git hash-object -w` 在仓库内通（rc=0，`b295aecf…`）；goals 侧写文件探针通。开工前磁盘 SHA 已核对（见 PROOF-NOTE，与任务书先验值完全一致）；收工后三件 SHA 复测一致，核心三件 SHA 复测一致（fix4），生产文件未动（`git status` 仍仅 `?? production/2026-w47/2026-w47-fr-zh-tw/`，builder 状态）。
- 复跑脚本：同目录 `proof_gates.py`（复刻 builder `gates.py` 14 门，逐门复刻；结果写本目录；**未在生产目录重跑构建**——确定性门改为沙盒副本重建）。`check_extra.py` 为重建者修正版（同基线判定，本目录副本，LOGD 指本目录）。`check_s11.py` 为 en 模板改写的 fr 版（见 §8 说明两处初版误报的纠正经过）。`verify_ed_fr.py` 为 fr 等效版 verify_ed（en 模板的 Ashes/Q39 内容不适用于 fr，见 §8）。
- 注：core-fr 无 `check_core.py`（ru/pt 系有）；fr 系等效覆盖 = freeze diff + source/string freeze + 确定性重建，均已跑并通过。

## 1. freeze 首检

`tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-zh-tw/svg` → rc=0，**8/8 页**（日志 `freeze-diff.log` / `freeze-diff.json`）：

| 页 | +/− 串 | 新增 CJK 字符数 |
|---|---|---|
| p1 | +21/−22 | 79 |
| p2 | +27/−28 | 93 |
| p3 | +22/−23 | 54 |
| p4 | +33/−32 | 89 |
| p5 | +30/−30 | 76 |
| p6 | +22/−24 | 79（含 U+3000 ×1） |
| p7 | +32/−32 | 139 |
| p8 | +99/−106 | 364（含 U+3000 ×10） |
| **合计** | | **973 字符** |

与 #1 的差值（p2 +27 vs +29、p3 +22 vs +23、p4 +33 vs +32、总数 973 vs 976）恰为 D1/D2/Q148 四处改值所致，无他。

### 1b. 简体残留逐字核对（opencc s2t 全扫）

对 8 页 SVG + `expl.py` + `.text.md` 全部 CJK 字逐字 `s2t(ch) != ch` 判定：**简体字 0 个**（`simplified-residue-proof2.json` 为 `{}`）。`expl.py` 全文 `准` 0 个、`準` 2 个（`zoom_note:120`、`n_vf1:230`）。D1 已修。

## 2. 独立门禁 14/14 PASS（`gates-proof2.json`，日志 `gates-proof2-run.log`）

| 门 | 结果 |
|---|---|
| run（builder `build-r2run1.log` 读检） | PASS：exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE；`P7 DORE NOSPACE` 单条已知良性行已过滤；TOTAL 150，A2 53 / B1 75 / B2 22，by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion（`tools/occlusion_audit.py`，不用 --selftest） | PASS：0 flags，selftest OK（`occlusion-proof2.json`） |
| p8_extract（`tools/p8.py extract --total 150`） | PASS：keys 150/150，printed notes 121/150（`p8-proof2.json`） |
| p8_compare（vs core P8 SVG） | PASS：CLEAN，keydiff [150]（writing key only）（`p8compare-proof2.json`） |
| source_freeze | PASS：content*.py / bslib4.py / svglib.py / run.py 与核心字节相同；render.py 仅 BASE+PDF 名差异 |
| string_freeze | PASS：全部非 CJK 核心串按页存活；0 核心 E 残留；0 未入账 CJK；1 串因翻译 E 值豁免（核心 `stem_e1` 前缀 `Traduisez : `） |
| text_layer | PASS：印/网 pdftotext 逐字节一致（101,463 B）；web 2,552,871 B < 7MB；print 30,551,086 B（`print-proof2.txt` / `web-proof2.txt`） |
| p8_font | PASS：P8 最小字号 11.625pt ≥ 9.75pt |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS：134 total [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck（vs `core-fr/final-fr-p8.json`） | PASS：150 键仅 Q150 不同（`開放題` vs 核心 `开放题`），核心 150 键 / 抽取 150 键 |
| mcq（`check_mcq.py`，重建者版） | PASS：bodies 45，rendered lines 1442，DEFECTS: 0，UNLOCATED: 0（`mcq-proof2.log`） |
| widths | PASS：31 单行串全部在预算内；4 组共行对均 ≤1757 |
| band_spans（印刷 PDF span 实测，1920 单位口径） | PASS：FR title ends 1236.9，band_r1 starts 1405.0，FR sub ends 837.2，band_r2 starts 1571.4 |

## 3. 确定性（沙盒副本重建，替代 gates 第 7 门）

版目录完整拷贝至本目录 `rebuild/ed/`（副本已删，仅留 `rebuild/rebuild-proof2.log`），删 svg 后重跑 `run.py`（rc=0，TOTAL 150，类型分布与 builder 一致：完成句子 49、单选 26、句型转换 7、词汇配对 21、阅读判断 5、图表读数 6、跟练 8、改错 4、完形填空 8、阅读理解 5、翻译 5、对话补全 5、写作 1），8 个 SVG sha256 与在版文件**逐字节一致 8/8**：`bc9050c8 / b46154cf / 22af3699 / 5af79c73 / a1981b77 / 81a3f8ff / 087855db / 7b8c6116`（与 builder `freeze_direct` 记录的哈希逐一相同）。

## 4. 孤儿标点全扫 + Q148 + 填空线（修正版 `check_extra.py`，`extra-proof2.json`）

- 孤儿元素：total=3，**new=0**，inherited=2（P4 y=623.13 `—`、P6 y=653.69 `—`，核心继承行首破折号），**recorded_remnant=1（P4 y=550.53 `。`，即 D3）**，shared_baseline=0。EXTRA PASS（按该脚本口径：无新增；D3 为已知记录残留，由本复校另行裁定为缺陷，见 PROOF-NOTE）。
- 填空线：core 与 zh-tw 完全相同 3 条——P3 (538.5, 1864.7)、P3 (538.5, 1997.4)、P8 (989.0, 843.0)，ok=True。Q36/Q37 y 档 +0，Q130 与核心分毫不差。
- Q148：stem_ok=True（基线拼接文本含 `On se retrouve` + `cinéma ?`，无 `du cinéma`）、key_in_content8=True、extracted=`devant le`。

## 5. check_s11.fr（`check_s11-proof2.log`）与 verify_ed.fr（`verify_ed_fr-proof2.log`）

- check_s11（fr 改写版：core-fr、fr 页名、§1.1 色集/VOL/徽章、P8 最小字号、Q120 芯片、ÉCRITURE 标题）：**ALL PASS**。色集 core 19 = edition 19，无增减；徽章三色齐全；P8 最小字号（SVG 口径）15.5；Q113–116 完形填空 `(113)–(116)` 在文内、117–119 为单选题号；Q120 芯片 `#37402f`（B2）位于 `120.` 左侧，与核心同色同位；`ÉCRITURE` 标题在。
- verify_ed_fr（fr 等效版，见 §8）：**ALL PASS**。text.md 答案解析 150/150；P8 抽取键 150/150；vs 核心仅 Q150 不同；text.md vs P8 抽取 0 mismatch（Q150 除外）；Q150 写作键 `開放題`；Q148 三重核对全过（content8.py 键+题干、P8 SVG 基线拼接题干无 `du`、抽取键）；P8 最小字号（PDF 口径）11.625pt ≥ 9.75pt。

## 6. creambox 规范扫描（`hidden_files/w47/tools/creambox.py`，日志 `creambox-proof2.log`）

- 33 盒。7 条 naive `clearance -` 行全部判定为**下一标题误报**（BELOW-WINDOW +24.0/+37.0，下一节标题首行；inside-only 清除全部为正）。
- **P7 盒 `y=1878 bottom=2258.0`**：naive 行即 `last baseline 2233.3 clearance +24.7`；inside-only 末基线 2233.3，clearance **+24.7**，desc-clear **+18.8**；P7-TOOLBOX 汇总：4 盒，最小盒内清除 +24.7，最小 desc-clear +18.8。
- PIL 真墨复核（`png/` 渲染 + fitz span bbox）：末行墨底 2238.9，盒内余白 **19.1 px**；深绿带起于 2270.0。**P7 干净，无溢出。**
- 其余各页盒内最小清除量均为正（P1 +48.0 / P2 +47.7 / P3 +47.7 / P4 +47.7 / P5 +47.7 / P6 +48.5 量级；详见日志）。

## 7. spill sweep（真墨扫，`spill_sweep.py` / `spill_sweep.json` / `spill_sweep-proof2.log`）

- 用 fitz span 真实墨迹 bbox（真 SVG 坐标 1950×2700）对全部奶油盒（含无描边纯填充盒）与盒标题做补充扫描：**盒右缘溢出 0、页右缘溢出 0**。
- 基线落在盒下 60px 内的行 25 条（全为 `below_box_baseline`），逐条核对核心同基线：24 条与核心同基线同坐标（下一节标题/下一盒标题，如 `LE MOT DE LA SEMAINE` +24.0、`LA SEMAINE PROCHAINE` +58.0 等）；1 条 P1 `LES DATES / 三個日期`（y=1433.7，上一盒底 +49.0）实为其自身日期盒（y=1396.7）内的标题，清除 +287，非溢出。**真溢出 0。**

## 8. 脚本适配说明（两次初版误报，均为本复校脚本之误，已纠正重跑）

如实记录，勿作版面问题：

1. `check_s11.py` 初版照搬 en 模板，要求 P8 文内含 `(117)`–`(119)` 填空——fr 版完形填空文内仅 `(113)–(116)`，117–119 为独立单选题（`117.` 题号），en 模板假设不适用于 fr；核心 P8 同样无 `(117)`。已按 fr 结构修正（文内查 `(113)–(116)`，117–119 查题号），重跑 PASS。
2. `verify_ed_fr.py` 初版两处解析错误：(a) text.md 答案区为多题同行、U+3000 分隔（`1. gagné　2. mercredi…`），初版按行首 `N. […] — key` 解析仅得 4 条；(b) Q148 题干跨 2 个基线（`...On se retrouve` y=1292.76 / `(148)___ cinéma ?...` y=1324.68），初版要求同一 `<text>` 元素同时含两段而误判。后改按 RÉPONSES 节全文、答案全文（截至于 `（` / U+3000 / 换行）解析 150 条，Q148 按基线拼接文本核对；另修掉了 `index("RÉPONSES")` 误取 951 行练习标题的问题（改 `rindex` 取 1051 行答案区标题）与 Q25 跨页标 `— 第3版 —` 的截断问题。重跑 150/150、0 mismatch，ALL PASS。
3. `verify_ed.py` en 模板（Ashes/Q39/Q40）内容专属于 en 核心，不适用于 fr；本复校以 fr 等效版 `verify_ed_fr.py` 覆盖同等检查面（150 键三源交叉 + Q148 + P8 字号 + text.md 答案解析）。

## 9. D5 字体普查（只记录，不判定；`d5-font-census-proof2.json`）

- 本版：Newsreader 931、Noto Sans CJK SC 654、Noto Serif CJK SC 115、DejaVu Sans 4、UnifrakturMaguntia 1；CJK 字体 769 段中纯拉丁 394 段。
- 核心对照（同一方法）：Newsreader 936、Noto Sans CJK SC 660、Noto Serif CJK SC 115、DejaVu Sans 4、UnifrakturMaguntia 1；CJK 字体 775 段中纯拉丁 391 段。
- 差集（本版仅有）：`。`（P4 孤儿，即 D3）、`CLINIQUE DES ERREURS`（双语标题拆 run，proof1 已记）、3 段译文换行分段差（含 `selon moi＝` 全角等号 vs 核心半角 `=`）。注：计数方法与 proof1 略异（Serif CJK 115 vs proof1 的 62，系 `<text>` 元素计数口径差），但与核心的同方法对照结论一致：差量小且均可解释。

## 10. 目视与内容手验

- 8 页逐页目视（印刷 PDF 150 dpi，`png/p1.png`–`p8.png`）：除 D3（P4 孤儿 。，300 dpi 裁切 `png/p4-note-crop.png`）外零问题；P1 band 无重叠；各页无溢出、无遮挡、无截断。
- D2 三处修复点 200 dpi 裁切目视确认（`png/p2-gloss-crop2.png`、`png/p2-etvous-crop.png`、`png/p3-zoom-crop2.png`）。
- 网页 PDF 抽查（`png/web-p1.png` 100 dpi、`png/web-p7.png`）：与印刷版布局、图片一致；印/网 token multiset diff **0**（各 101,463 B）。
- 150 题逐题手验（`.text.md` 1,087 行全文通读 + 三源交叉 `verify_ed_fr.json`）：150/150 一致，仅 Q150 不同；答案区 150 条全解析、0 缺失；带注记答案 121 条，与 P8 抽取注记数一致。key-vs-stem 适配逐项手核（Q73 教训专项，见 PROOF-NOTE）。仅 D3 一项缺陷。

## 11. 回归对照（vs #1 备份 `scratch-refanout-fr2/backup-old/`）

- SVG 逐页哈希：P2（7e372c72→b46154cf）、P3（f3280832→22af3699）、P8（86da3308→7b8c6116）变；P1、P4、P5、P6、P7 字节相同。
- `expl.py` diff 恰 4 行（D1×2 + D2×3 的全部 hand patch，无丢失）；`content8.py` diff 恰 2 行（Q148 键+题干），新版与 core-fr 字节相同；`.text.md` diff 恰 5 处；`ABSTRACT.txt` 字节相同；其余差异仅三件 PDF、`WEEKLY-KIT.md`、`__pycache__` 与 `cards/p2|p3|p8.png`。
- D3 所在 P4 与 #1 字节相同——残留未被重建者改动，非回归引入，是 fix4 未同步到读者语的一处。

## 结论

机械门 14/14 + freeze 8/8 + 确定性 8/8 + creambox 33 盒 + spill sweep 真墨 0 溢出 + 三源交叉 150/150 均通过，**未过项为 D3（P4 残留孤儿句号 。，`expl.py:122`，全句 387.0px > 栏 378.5px，句号独行 y=550.53，300 dpi 目视可见）**，故结论 **(b) 不定稿**，修法为释义删「決賽」二字（修后 344.0px 单行，与核心 fix4 同值）；修后重跑全套门禁 + P4/text.md 重验。
