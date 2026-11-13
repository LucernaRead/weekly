# GATE-LOG — 2026-W47 fr-de proof2（re-fanout #2，2026-11-11，复校员独立重跑，盘上实测）

Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-de2/`
（`probe.txt`、`tmp/`、`proof_gates.py`、`gates-proof2.log/.json`、`occlusion-proof2.json`、`p8-proof2.json`、`p8compare-proof2.json`、`check_s11_fr.py`、`check_s11-proof2.log`、`verify_ed_fr.py`、`verify_ed-proof2.log`、`check_extra.py`、`extra-proof2.log`、`check_mcq.py`、`creambox.py`、`creambox-proof2.log`、`creambox_check.py`、`creambox-check-proof2.log`、`pil_p7.py`、`pil_p7-proof2.log`、`spill_sweep.py`、`spill-proof2.log`、`dump_keys.py`、`keycheck-manual.txt`、`scan.py`、`minfont.py`、`fillcheck.py`、`freeze-proof2.log`、`freeze-core-proof2.log`、`freeze-final/`、`freeze-core/`、`freeze-diff-proof2.json/.log`、`print-proof2.txt`、`web-proof2.txt`、`print-nl-proof2.txt`、`web-nl-proof2.txt`、`webpdf-proof2.log`、`render-web/`、`web-rerender-proof2.txt`、`d5-proof2.log`、`render/print/p-1..8.png`、`render/print/p7hi-7.png`、`render/print/p7-box-crop.png`、`render/web/p-1..8.png`）
工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`。`TMPDIR=<scratch>/tmp`。`/dev/null` 开工检查正常（字符设备）。未写 /tmp，未改生产文件（收工 SHA 复核与开工一致，见 §0），未 commit、未 push。

## 0. 对象核对（任务书先验值 + 盘上 sha256sum，2026-11-11 实测）

| 文件 | 字节 | SHA-256（完整） | 结果 |
|---|---|---|---|
| `La-Lucerna-VOL4-fr-de.pdf` | 17,424,223 | `77842fe4dc5d162adc7f2b8694ad92e985fe83a1fcd9a49c2c3e3ae2886d8e7b` | 与任务书先验值一致 ✓ |
| `La-Lucerna-VOL4-fr-de-web.pdf` | 1,706,936 | `df62f6ee61ae8cc6cd57c837a4a2da74187f855b0d71d2c5a07751ebfb9fdf37` | 与任务书先验值一致 ✓ |
| `2026-w47-fr-de.text.md` | 46,632 | `d3735ef592bc02fcbe9712c3a184c2c2c963fd3fcfaf3311363ccf2baf95bc18` | 与任务书先验值一致 ✓ |
| core 印 `La-Lucerna-VOL4.pdf` | 30,446,975 | `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d` | 与重建报告 fix4 一致 ✓ |
| core 网 `La-Lucerna-VOL4-web.pdf` | 2,241,835 | `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141` | 与重建报告 fix4 一致 ✓ |
| core 文 `2026-w47-fr-zh-cn.text.md` | 46,471 | `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df` | 与重建报告 fix4 一致 ✓ |

探针：`ls /dev/null` 正常；scratch 写 `tmp/probe.txt` 成功；`git hash-object -w /dev/null` RC=0（`e69de29b…`）。收工三件 SHA 与开工一致，未变。`git status` 上该版目录为未提交新目录（builder 工作状态，复校未动）。

## 1. 机械门（`proof_gates.py`，#1 proof 的 fr 适配版，路径改指 scratch-refanout-fr2 + 本 scratch，日志 `build-r2run1.log`，输出改名 proof2）

| 门 | 命令 / 位置 | 结果 |
|---|---|---|
| run（构建日志） | builder `build-r2run1.log` 扫描 | **PASS**：exit 0，0 OVERFLOW / 0 TOO WIDE，TOTAL 150；by level {A2: 53, B1: 75, B2: 22}；by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}（`P7 DORE NOSPACE` 已知良性行已过滤，与 #1/#2 构建报告一致） |
| occlusion 审计 | `tools/occlusion_audit.py svg/`（真实命令，未加 --selftest） | **PASS：0 flags**（`occlusion-proof2.json`） |
| p8 extract | `tools/p8.py extract --p8 svg/p8-exercices.svg --total 150` | **PASS：keys 150/150，printed notes 121/150**（`p8-proof2.json`） |
| p8 compare | `tools/p8.py compare --core-p8 core-fr/svg/p8-exercices.svg --edition-p8 svg/p8-exercices.svg --total 150` | **PASS：CLEAN，keydiff [150]**（仅写作题键；137–139 为翻译题键，与核心逐字相同）（`p8compare-proof2.json`） |
| source freeze | content/bslib/svglib/run 与 core 逐字节比对 | **PASS**：`content12/34/56/7/8.py`、`bslib4.py`、`svglib.py`、`run.py` 与 core 字节相同；`expl.py` 仅读者语值不同（预期内）；`render.py` 差异仅 BASE+PDF 名 |
| string freeze | 核心非 CJK 串按页存活 + 核心 E 残留 + 未入账 CJK | **PASS**：全部非 CJK 核心串按页存活；0 核心 E 残留；0 未入账 CJK；1 串因翻译 E 值豁免 |
| text layer | `pdftotext -layout` 印/网 | **PASS**：逐字节一致（104,632 B）；web 1,706,936 B < 7 MB；print 17,424,223 B（`print-proof2.txt` / `web-proof2.txt`） |
| p8 font | PyMuPDF 读印版 P8 spans | **PASS：P8 min font 11.625pt ≥ 9.75pt** |
| scans | 8 页 SVG 字符统计 | **PASS**：U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | 每页 `fill="#ffffff"` 计数 | **PASS：134 total [10, 12, 18, 15, 14, 15, 12, 38]** |
| keycheck（vs `core-fr/final-fr-p8.json`） | 抽取键 vs 核心键 | **PASS：150 键仅 Q150 不同，核心 150 键 / 抽取 150 键** |
| mcq（`check_mcq.py`） | SVG MCQ 选项分拆扫描 | **PASS：bodies 45，rendered lines 1485，DEFECTS: 0，UNLOCATED: 0** |
| widths | 31 单行串 `svglib.text_w` 预算 | **PASS：31 单行串全部在预算内；4 组共行对均 ≤1757** |
| band_spans（印刷 PDF span 实测） | P1 标题/带几何 | **PASS：FR title ends 1236.9，band_r1 starts 1337.5，FR sub ends 837.2，band_r2 starts 1417.5** |
| **合计** | | **PROOF-GATES 14/14 PASS**（`gates-proof2.json`） |

## 2. check_s11 / verify_ed（fr 适配版，见 PROOF-NOTE 方法备注）

| 门 | 命令 / 位置 | 结果 |
|---|---|---|
| §1.1 / P8 检查 | `check_s11_fr.py de`（`check_s11-proof2.log`） | **ALL §1.1/P8 CHECKS PASS，RC=0**：色集 core 19 / edition 19，无多无少；徽章色 A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` 齐全；P8 min font-size 属性 15.5；Q109–116 完形空 + Q117–119 题干 + `113. A. propose` 选项行 + `145. des billets` 答案 + Q120 芯片 + `ÉCRITURE` 标题均在；注记：`p6-politique.svg: VOL.5 count core=0 ed=1`（见 PROOF-NOTE R1，合法翻译，不判 FAIL） |
| verify_ed | `verify_ed_fr.py de`（`verify_ed-proof2.log`） | **VERIFY ALL PASS，RC=0**：core `final-fr-p8.json` 150 键；text.md RÉPONSES 块解析 150 答案；Q39 `minuit`、Q40 `troisième`、Q46 `C`、Q52 `d`、Q55 `moins longue`、Q125 `A`、Q148 `devant le` 与核心一致；Q150 开放题；Q64 Dhont；Q148 题干无 `du cinéma`；P8 最小 PDF 字号 11.62pt ≥ 9.75pt；SVG 零真实 CJK |

## 3. 确定性 freeze（`tools/freeze.py`，标准口径：`--build` 指构建目录，`--core-svg` 指 svg 目录）

| 门 | 命令 | 结果 |
|---|---|---|
| freeze 渲染（本版） | `tools/freeze.py baseline --build <ed> --core-svg <ed>/svg --out freeze-final` | **8/8 SVGs byte-identical**（`freeze-proof2.log`）：p1 `35c72f4e`、p2 `38a1a6fc`、p3 `93a010c3`、p4 `cd216538`、p5 `32c60e8a`、p6 `083360a7`、p7 `700bee74`、p8 `660522e4`；core integrity：8 文件未变 |
| freeze core 对照 | `tools/freeze.py baseline --build core-fr --core-svg core-fr/svg --out freeze-core` | **8/8 SVGs byte-identical**；核心 8 页 SVG 哈希与 fix4 一致，核心未动（`freeze-core-proof2.log`） |
| freeze diff vs core | `tools/freeze.py diff --core-svg core-fr/svg --edition-svg <ed>/svg --json freeze-diff-proof2.json` | p1 +26/−23、p2 +39/−33、p3 +35/−44、p4 +46/−49、p5 +38/−42、p6 +31/−30、p7 +43/−34、p8 +124/−123；**新增 CJK 共 7 个，全为 U+3000**（每页 0–2 个） |

## 4. creambox 规范扫描（`hidden_files/w47/tools/creambox.py`，逐文件参数；`creambox-proof2.log`）

- 33 盒。7 条 naive `clearance -` 行全部判定为**下一节标题误报**（BELOW-WINDOW +24.0/+37.0，下一节标题首行；逐行核对：P1 `LE MOT DE LA SEMAINE` +24.0、P2 `LA SEMAINE EN CHIFFRES` +37.0、P3/P4/P5 `À VOUS !　DU BIST DRAN` 各 +37.0、P6 `IL EST PRÉVU QUE + SUBJONCTIF` +37.0、P6 `LE DÉBAT　DEBATTE` +37.0；inside-only 清除全部为正）。
- **P7 披露框（#1 D1 修复验证）**：盒 `y=1878 bottom=2258.0`，末基线 **2233.3，清除 +24.7**，desc-clear +18.8；per-line 表：德文注 2 行（2206.0 / 2233.3），无第 3 行；其余 P7 工具盒最小清除 +48.5。
- 其余盒 inside-only 最小清除：P1 +48.0、P2 +5.0（ET VOUS 盒，紧但未出；desc-clear −1.0 为行距口径，基线仍在盒内 5.0px）、P3 +30.7、P4 +46.4、P5 +24.0、P6 +20.0、P8 +64.9。
- 精炼版 `creambox_check.py`（逐文件参数）：**NO OVERFLOW，RC=0**（`creambox-check-proof2.log`）。
- PIL 真墨（`pil_p7.py de`，印刷 PDF 200 dpi，字色 `#6f675d`）：末行真墨 svg y **2237.8**；间隙 2258–2270 **NONE (clean)**（`pil_p7-proof2.log`）。
- 200 dpi 盒底裁切（`render/print/p7-box-crop.png`，svg x 960–1890 / y 1860–2310）：末行字形完整在奶油盒内，下方白纸间隙干净，绿带未侵入。目视通过。

## 5. spill sweep + 盒标题真墨扫描（`spill_sweep.py`，本复校自写；`spill-proof2.log`）

- §1 spill sweep（baseline 落在奶油盒外的整行，x 重叠、盒底 +60px 内）：**零候选行**（creambox 会跳过盒外行，本扫补全）。
- §2 盒标题真墨扫描（150 dpi 印刷渲染，PIL 实测；白字深底按亮墨量，深字浅底按暗墨量；字墨组自标题 x 起、50px 断开）：
  - 全部粗体 ≥23pt 标题通过（终版量法下仅 P7 一处旗标，且已核实为误判，见下）；其余标题真墨余量均 ≥12px。初版单阈值量法的余量数字（P3 标题 2.9px、P5/P7/P8 题号 3.5–11.8px）为整行墨量误计，已废弃，不作为证据。

## 6. 孤儿标点与 Q148（`check_extra.py` 修正版，`extra-proof2.log`）

- 孤儿：total 0，new 0，inherited 0，remnant 0，shared_baseline 0。**EXTRA PASS**。
- 孤行填空线：core P3 (538.5, 1864.7)、(538.5, 1997.4)、P8 (989.0, 843.0)；de P3 (538.5, 1894.4)、(538.5, 2027.1)、P8 (989.0, 843.0)；ok=True（Q130 分毫不差；Q36/Q37 +30）。
- Q148：stem_ok=True，key_in_content8=True，extracted=`devant le`。
- 另行三重核对（GATE-LOG §8）：P8 SVG 文本层含 `On se retrouve` + `cinéma ?` + `148. devant le`，不含 `du cinéma`。

## 7. 印/网文本层 + 网 PDF 重渲（只在 scratch 里渲染，未覆盖生产文件）

- `pdftotext -layout`：印=网=104,632 B，逐字节一致；无 layout 版亦逐字节一致。token 多重集差 **0/0**（各 8,051 tokens）。
- 网 PDF 重渲：scratch 内 `tools/webpdf.py <ed>/svg render-web/rerender-web.pdf`（RC=0），1,706,937 B（交付 1,706,936 B，+1 B 浮动，预期内）；文字层与印版及交付网版**逐字节一致**（`web-rerender-proof2.txt` cmp 印/网均 identical）。生产网 PDF SHA 未变（收工复核见 §0）。

## 8. 与 #1 备份回归对照（`scratch-refanout-fr2/backup-old/2026-w47-fr-de/`）

| 检查 | 结果 |
|---|---|
| SVG 哈希旧→新 | P1 `35c72f4e`、P2 `38a1a6fc`、P3 `93a010c3`、P4 `cd216538`、P5 `32c60e8a`、P6 `083360a7` 均**相同**；仅 P7 `4bc0ef75→700bee74`、P8 `7e3269a2→660522e4` 变化 |
| 源文件 diff | 恰好 3 行：`expl.py:182` 删披露中句；`content8.py:170` `devant`→`devant le`；`content8.py:176` 删 `du`；其余 7 个 py 文件字节相同 |
| KEEP | #1 修复全部保留：`Dhont` 新旧 `expl.py` 各 1 处、`Dont` 0 处；`ABSTRACT.txt` 与 #1 备份字节相同（231 B） |
| REVERT | 0 处 |
| ABSTRACT | 德语单行 + 结尾换行，231 B |

## 9. 目视与内容手验

- 8 页逐页目视（印刷 PDF 150 dpi，`render/print/p-1..8.png`）：除 R3 观察项外零问题。P1 band 无重叠（FR 标题止 1236.9 / 德文带起 1337.5）；各页无溢出、无遮挡、无截断；P7 披露框见 §4；P8 Q148 见 §6。
- 网页 PDF 抽查（100 dpi，`render/web/p-1.png`、`p-7.png`）：与印刷版布局、图片一致；P7 披露框在网页版同样正常。
- 150 题逐题手验（`.text.md` 全文 1,088 行通读 + `keycheck-manual.txt` 对照表）：150 键全部正确（见 PROOF-NOTE §4）。
- D5 字体普查（`d5-proof2.log`，只记录不判定）：Newsreader 946 段、Noto Sans CJK SC 695 段（570 段含拉丁字母）、Noto Serif CJK SC 17 段、DejaVu Sans 4 段、UnifrakturMaguntia 1 段；真实 CJK 0；核心对照 Noto Sans CJK SC 660 段（438 段含拉丁字母）。

## 结论

机械门 proof_gates **14/14** + check_s11 **ALL PASS** + verify_ed **ALL PASS** + freeze 8/8（版+核心）+ creambox **NO OVERFLOW** + 孤儿新增 **0** + 印/网文字层 **0 差** + 目视/手验 **150/150**，**唯一历史缺陷 D1 已修好并实测验证，R1 已落地**，故结论 **(a) 零缺陷，可定稿**。
