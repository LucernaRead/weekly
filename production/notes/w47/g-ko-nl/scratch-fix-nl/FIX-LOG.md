# W47 nl 家庭修复 FIX-LOG（第二接替工人，2026-11-12）

- 范围：只动 `production/2026-w47/` 内 nl 家 11 版（core-nl + 10 fan-out）；不 commit、不 push、不跑 lint。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`。
- 磁盘：接手时 94G 已用 / 150G（< 100G 门限，可开工）。
- 上一任（f1a5b33c）无 FIX-LOG；本 LOG 为接手后重建。

## 接手核实（2026-11-12，逐版指纹 vs PROOF-NOTE）

| 版 | 印 PDF（SHA-12 / 字节） | 网 PDF（SHA-12 / 字节） | text.md（SHA-12 / 字节） | 与 PROOF-NOTE 对照 |
|---|---|---|---|---|
| core-nl | 0c5d63b942d2 / 13830540 未变 | 2b6f223eaff9 / 1874709 未变 | aa1f470353f9 / 44087 **变 −6B** | 13 已落地：仅删 text.md 第 5 行裸 `VOL.4`（与 scratch `text-core-before.md` diff 唯一一行） |
| nl-de | 97420549c81e / 12104230 未变 | 2361bedfd4d5 / 1536341 未变 | c1342c3fe20d / 46226 未变 | 无待修项 |
| nl-en | d87a5242afec / 12102271 未变 | db7a9ace064a / 1534348 未变 | 9596c4acbb27 / 45115 未变 | 12 待修（BRIEVEN 英文注释缺 best P8 texts） |
| nl-es | 2da02d5b3081 / 12107937 未变 | 249fda66604b / 1540062 未变 | 44fc3d5c4287 / 47649 未变 | 无待修项 |
| nl-fr | 08f57ec27d86 / 12106421 未变 | 1b429a3ff61e / 1538511 未变 | f1d1154442c4 / 47744 未变 | 无待修项 |
| nl-it | 675f2bf33c42 / 12102402 未变 | 81a3ffaf8e8e / 1534500 未变 | f1d9e3f58b82 / 47060 未变 | 6、16、17 待修 |
| nl-ja | ada454de4dae / 18803544 **变 −308B** | 402cb8e7004a / 1967745 **变** | b7e5f5dc8b48 / 47804 **变 +3B** | 1、3 已落地（印 P8 含 サプライズ；主語＋動詞 ×6）；**2 未全落地**：P2 栏目标题已改，但 P2 band 副标题 `靴とパッケスアフォント`（content12.py:165）仍为旧形，印 PDF 全文旧形残留 ×1（p2-leven.svg 内） |
| nl-ko | e7fa69a263fe / 13871386 **变 +78B** | 218aebe12b4b / 1791786 **变** | e13db87160d1 / 47576 **变 −9B** | 4、5 已落地（印 P8 팍예스아폰트 ✓、파크예스아본트 0；주어·동사 ×6；ABSTRACT.txt 已为 팍예스아폰트） |
| nl-pt | dc43c521becb / 12110806 未变 | b9e2c0d5b7f2 / 1542946 未变 | 7e6b0c54dcb2 / 47209 未变 | 6、14、15 待修；P1 重叠实测仍在（LEEMWEEK 1002.9→1083.9） |
| nl-ru | 8fa079cbd094 / 12367658 未变 | 69678fdcdd00 / 1779868 未变 | dd1c0c087c46 / 57909 **变 +39B** | 7 源头已改（content12.py:44）+ text.md 已改，但 **SVG 未改**（p1 含 `Нидерланды, Берлин` 计数 0）、印 P1 仍截断 `(16 ноября: Германия)`——只改了 text.md，未重渲染 |
| nl-zh-tw | 90710eae78ae / 13888370 未变 | 42b892b5c065 / 1976958 未变 | 30af89dfbfe2 / 44320 未变 | 10、11 待修（禮物之夜 ×4 / 收禮夜 ×6；Q135/136 仍用 主語/賓語） |

补充核实：
- 上一任的 ja/ko gates.json 均 ALL PASS（web 尺寸与现盘一致），但 **KIT 未更新**：ja/ko/ru KIT 仍记 PROOF-NOTE 的旧 SHA（ja 印 `67aeebb40b58…`、ko 印 `fd8daad8ba7e…`、ru text.md 57,870B `f23da475ff54…`）。本轮逐版更新 KIT 为盘上实际 SHA。
- core 印 P1 的裸 `VOL.4`：实测为顶行左端刊头家具 span（x=66.0, y=59.6, 12.8pt），另一次在页脚（y=1958.6），非正文 stray 行；故 13 只改 text.md、不重渲染的裁定成立。
- it P2 重叠实测仍在：标题 `PAKJESAVOND IN QUATTRO PAROLE` 止于 899.5，提问始于 897.7（重叠 1.8pt）；`RICORDA` 633.0→721.3，盒右缘 720.8（溢出 0.5pt）。
- it/pt 的 `[B1 · Cloze]`：SVG 全目录 grep 0 命中，只见于 text.md；源头为 content8.py 的题型标签（de 用 `Lückentext`、es/fr 同理本地化）。
- 协调员补充：nl-ko 印 PDF 亦已变（PROOF 后），与上表一致。

## 修复记录（逐版；全部完成）

### nl-ja（2 残留：P2 band 副标题）——已完成
- 源头：`content12.py:165` band 副标题 `靴とパッケスアフォント` → `靴とパッケスアーフォント`（其余 1、3 由上一任落地，本轮只补此一处）。
- 重渲染：`run.py` TOTAL 150 RC 0 → `render.py` RC 0 → 导出干跑 /tmp 与在运 text.md 字节一致（band 属家具，不进导出）后重导出（150 题、8 金句、6 gloss）→ `webpdf.py` RC 0。
- 验：印 PDF 全文新形 ×7、旧形 ×0；P8 含 サプライズ。
- 门禁（`tools/gates.py` ALL PASS）：occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0（8 页）；pdftotext 印=网=47,840 B；P8 答案区最小 10.12pt；P8 chips = core {A2: 8, B1: 24, B2: 3}；§1.1 SVG 审计 clean。 extras：boxtitle 0 DEFECT；spill 0 SPILL（67 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS 0 defects；d5_creambox PASS 0 defects。
- 新 SHA：印 `b886a483f64181624efef8f17c4d1a6d2e421571cf26c2de576f72b5682399b6`（18,803,540 B）；网 `2b38c2547606d2a33b436cea4337acf4a93ddfbe4acdd93ef5533781d2755b7b`（1,967,732 B）；text.md `b7e5f5dc8b484da52b0a22493149d93f0bbd3a0aeb79deb56b2f28e017a80084`（47,804 B，本轮未变）。KIT 已更新。

### nl-ko（4、5 已落地）——本轮复核 + KIT
- 本轮无源头改动。复核：印 P8 팍예스아폰트 ✓、파크예스아본트 0；주어·동사 ×6；ABSTRACT.txt 已为 팍예스아폰트。
- 括号前缺空格（任务 5 后半）：印 PDF 全文扫描 25 处无空格 `(`、涉及多种不同字符串——全版系统性习惯，非单一模板源头，按任务要求不管，记入此条。
- 门禁（本轮自跑，ALL PASS）：occlusion 0；p8 150/150；compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0；pdftotext 印=网=47,512 B；P8 最小 10.12pt；chips = core；§1.1 clean。extras：boxtitle 0 DEFECT；spill 0 SPILL（123 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS（用上一任 run.log）；d5_creambox PASS 0 defects。
- SHA（盘上实际值）：印 `e7fa69a263fe85ef08205ac654e55e2333f590de5f6bd6f1ea73103150746bff`（13,871,386 B）；网 `218aebe12b4ba140a0180cfdd3fcb2719547737f1e7c59682aca83a57fed231a`（1,791,786 B）；text.md `e13db87160d1477972824431d9f4e194f90f53a53b7954e659cc74484801f537`（47,576 B）。KIT 已更新。

### nl-ru（7：重渲染）——已完成
- 源头已由上一任改好（`content12.py:44` + text.md:13）；本轮只重跑管线：`run.py` TOTAL 150 RC 0 → `render.py` RC 0 → 导出干跑 /tmp 与在运 text.md 字节一致后重导出（150 题）→ `webpdf.py` RC 0。
- 验：印 P1 现为 `16 — november: Duitsland – Nederland in Berlijn (16 ноября: Германия – Нидерланды, Берлин)`（三行折行，完整）。
- 门禁（ALL PASS）：occlusion 0；p8 150/150；compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0；pdftotext 印=网=55,025 B；P8 最小 10.12pt；chips = core；§1.1 clean。extras：boxtitle 0 DEFECT；spill 0 SPILL（36 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS；d5_creambox PASS 0 defects。
- 新 SHA：印 `bb407a7b067e0ce84e8f61149a5fcd913e32174b6a6db1ac755ba466468b78f8`（12,368,148 B）；网 `1c13bb4f7311b55d6c048cf0a8f72142829aa8b49e6be0a4f210a67ef5014363`（1,780,327 B）；text.md `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228`（57,909 B，本轮未变）。KIT 已更新。8/9 未动（见“不修项”）。

### nl-it（6、16、17）——已完成
- 源头：`content8.py` 13 处 `Cloze` → `Testo con lacune`；`content12.py:213` 栏目标题 `PAKJESAVOND IN QUATTRO PAROLE` → `PAKJESAVOND IN 4 PAROLE`；`content12.py:177` 奶油盒标题 `ZO ONTHOUD JE HET　RICORDA` → `ZO ONTHOUD JE HET　NOTA`。
- 重渲染：`run.py` TOTAL 150 RC 0（by type `Testo con lacune`: 13）→ `render.py` RC 0 → 导出干跑 → 重导出 → `webpdf.py` RC 0。
- 验（印 P2 实测）：16 标题止于 797.1，提问始于 897.7 → 间隙 100.6pt（原重叠 1.8pt）；17 `NOTA` 止于 688.4，盒右缘 720.8 → 余 32.4pt（原溢出 0.5pt）。
- 导出器陷阱：干跑 diff 除意改行外多一行——第 287 行 `### VOOR OF TEGEN?　PRO O CONTRO?` 被导出器丢了 `### ` 前缀（与 ru 家 FIX-LOG §7 同类）；已手工回补；最终 diff 只含意改行（73 NOTA、83 4 PAROLE、383–390 + 423–427 Testo con lacune）。另核：其余版同行均为 `### VOOR OF TEGEN? …`，回补符合既成格式。
- 门禁（ALL PASS）：occlusion 0；p8 150/150；compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0；pdftotext 印=网=46,365 B；P8 最小 10.12pt；chips = core；§1.1 clean。extras：boxtitle 0 DEFECT，1 marginal——P6 `DATI INVENTATI` 墨迹超盒缘 0.6px，在工具 1.0px 容差内（旧的 P2 `RICORDA` marginal 已随 NOTA 修复消失）；spill 0 SPILL（39 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS；d5_creambox PASS 0 defects。
- 新 SHA：印 `dc91af0aa78da597d0f3025087cd8695ccda1cb9ca454fc5445924e12bbe0059`（12,102,273 B）；网 `9eff96cf487a6beb5e26413ac9683bf771aac12f0ef9d6c2eca1de5b399fbf93`（1,534,364 B）；text.md `e9880da2da990ad87348c650cc4f82637a108284d7929de2ed901019ef77ac0a`（47,194 B）。KIT 已更新。

### nl-pt（6、14、15）——已完成
- 源头：`content8.py` 13 处 `Cloze` → `Texto com lacunas`；`content12.py:15` kicker 葡语部分 `O NEERLANDÊS QUE OS NEERLANDESES LEEM` → `TODAS AS SEMANAS EM NEERLANDÊS`；`content12.py:18` 刊名行首段 `WEEKBLAD IN HET NEDERLANDS` → `SEMANÁRIO NEERLANDÊS`（逐版字符串：es/it 同位分别为 `SEMANARIO NEERLANDÉS` / `SETTIMANALE OLANDESE`；与本版 H1 `Semanário neerlandês`、页脚 `SEMANÁRIO NEERLANDÊS VOL.4` 一致；en 版未动）。
- 宽度预演（14）：Newsreader 12.75pt + 1.7px 字距实测模型——旧串总宽 628.2pt、新串 563.6pt，预测右端 1013.1、间隙 26.4pt。
- 重渲染：`run.py` TOTAL 150 RC 0（by type `Texto com lacunas`: 13）→ `render.py` RC 0 → 导出干跑 → 重导出 → `webpdf.py` RC 0。
- 验（印 P1 实测）：kicker 止于 1014.6，日期始于 1039.5 → 间隙 24.9pt（原重叠 44.4pt）；`LEEMWEEK` 合并 span 消失；刊名行读作 `SEMANÁRIO NEERLANDÊS VOL.4 ORANJE SINTERKLAAS PAKJESAVOND`；P1 渲染卡片已目视确认（顶行间隙清晰、刊名本地化、其余版面干净）。
- 导出器陷阱：干跑 diff 除意改行外多两行——第 287 行 `### VOOR OF TEGEN?　A FAVOR / CONTRA` 与第 360 行 `### HET WOORD　PALAVRA DA SEMANA` 被导出器丢了 `### ` 前缀；均已手工回补；最终 diff 只含 13 处 Cloze 行。
- 门禁（ALL PASS）：occlusion 0；p8 150/150；compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0；pdftotext 印=网=46,588 B；P8 最小 10.12pt；chips = core；§1.1 clean。extras：boxtitle 0 DEFECT, 0 OBSERVE, 0 marginal；spill 0 SPILL（39 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS；d5_creambox PASS 0 defects。
- 新 SHA：印 `e2fe3b3a95686bd48e01a7975f62ee33bb821dd6a8a743c1a188bb8e6f119d37`（12,110,707 B）；网 `40c51869695b80e165661c6adb9309c70341342d56d632c472a7ba18f9ace508`（1,542,854 B）；text.md `67516e2163c8c769ab9574b60b472c7d97706b3c4d89182bb95faa221513727a`（47,365 B）。KIT 已更新。

### nl-zh-tw（10、11）——已完成
- 源头：`content12.py:58/155/243/259` 四处 `禮物之夜` → `收禮夜`；`content8.py:64` Q135 `主語` → `主詞`；`:66` Q136 `主語` → `主詞`、`賓語` → `受詞`。
- 重渲染：`run.py` TOTAL 150 RC 0 → `render.py` RC 0 → 导出干跑 → 重导出 → `webpdf.py` RC 0。
- 验：印 PDF 全文 禮物之夜 0 / 收禮夜 ×10；主語 0 / 賓語 0 / 主詞 ×6 / 受詞 ×3。最终 diff 只含 6 处意改（text.md:22, 61, 104, 113, 409–410）；导出器陷阱本轮未触发。
- 门禁（ALL PASS）：occlusion 0；p8 150/150；compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0；pdftotext 印=网=44,242 B；P8 最小 10.12pt；chips = core；§1.1 clean。extras：boxtitle 0 DEFECT, 0 OBSERVE, 0 marginal；spill 0 SPILL（55 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS；d5_creambox PASS 0 defects。
- 新 SHA：印 `3fd293bfef564ea277f4f96495710f7391ad5204da659bdd43dc2ce3edfde693`（13,887,537 B）；网 `542c6f1bc8e2f71b0cdf558e169dca3d1738e981919433c63182a304a44754ec`（1,976,266 B）；text.md `bf1f627d1bbf6387cb0f782e6ede2feb3fe18ffb48bd599ce3720be3238b9855`（44,308 B）。KIT 已更新。

### nl-en（12）——已完成
- 源头：`content7.py:91` 英文注释 `No letters yet — an example; VOL.5 next.` → `No letters or best P8 texts yet — an example; VOL.5 next.`（对标 fr `ni meilleur texte` / it `né migliori testi` / pt `nem melhores textos`；荷兰语核心行 dt_nl 本就含 `beste pagina-8-teksten`，未动；de 版读者行同样未提 best texts，但 PROOF 未列、任务未派，未动）。
- 重渲染：`run.py` TOTAL 150 RC 0 → `render.py` RC 0 → 导出干跑 → 重导出 → `webpdf.py` RC 0。
- 验：印 P7 含 `No letters or best P8 texts yet — an example; VOL.5 next.`。
- 导出器陷阱：干跑 diff 除意改行外多两行——第 287 行 `### VOOR OF TEGEN?　FOR OR AGAINST?` 与第 360 行 `### HET WOORD　WORD OF THE WEEK` 被导出器丢了 `### ` 前缀；均已手工回补；最终 diff 只含 366 行。
- 门禁（ALL PASS）：occlusion 0；p8 150/150；compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0；pdftotext 印=网=45,367 B；P8 最小 10.12pt；chips = core；§1.1 clean。extras：boxtitle 0 DEFECT, 0 OBSERVE, 0 marginal；spill 0 SPILL（37 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS；d5_creambox PASS 0 defects。
- 新 SHA：印 `1900408aabb9bb4e9714e29a9cf6ce762527d3ff9c606cf5cda7bf7e14d07b33`（12,102,278 B）；网 `7174a848673ff655c87e70af4a95133171cbe4c79679be21a5efb30502a961ca`（1,534,350 B）；text.md `da6d999d5b51d7c86f3cfc244be4ce1c1b4afc38f23e9c872d710056aec0d912`（45,132 B）。KIT 已更新（该 KIT 无 Files delivered 节，只在 D5 rebuild 条后追加 fix 条）。

### core-nl（13）——已完成（text.md only）
- text.md 已由上一任改好（删第 5 行裸 `VOL.4`，diff 唯一一行）；本轮不重渲染（印/网 PDF 未变）。印 P1 的 `VOL.4` 经核为顶行左端刊头家具 span（x=66.0, y=59.6, 12.8pt）+ 页脚一次，非正文 stray 行，裁定成立。
- text.md 现 SHA：`aa1f470353f9fa24bdec29028e596dd924387fe7d05956f208a57006025e2327`（44,087 B）。KIT 已更新（Deliverables 行 + §18 后追加 fix 条）。

## D5 census（本轮自跑；tools 内无 census 工具，以 SVG font-family 直计为准）
- ja/ko/it/pt/zh-tw/en：纯拉丁文本落入 Noto Sans（D5_lat 嫌疑）= 0；弯引号 U+201C/U+201D/U+2019 落入 CJK 字体 = 0。
- ru：D5_lat 嫌疑 = 338（与 PROOF 问题 8 的“338 个纯拉丁”一致）；Noto Serif CJK SC 元素 611（问题 9 的 P8 答案层）。两项均为已知、协调员裁定不修（后续 *-ru 工人统一处理），本轮未动任何 svglib.py 字体路由。
- 其余版的 `Noto Sans CJK SC` 元素（如 it/pt/en 的 118–127 个）均为 U+3000 表意空格与 `→` 箭头（PROOF 已核：无拉丁字母，非违规）。

## 导出器陷阱（本轮三次触发，ru FIX-LOG §7 同类）
- 新导出会丢个别奶油盒标题的 `### ` 前缀：it 第 287 行、pt 第 287 + 360 行、en 第 287 + 360 行；ja/ru/zh-tw 干跑与在运文件字节一致，未触发。
- 处理：干跑到 /tmp、diff、逐字回补；最终 diff 只含意改行（it 15 行、pt 13 行、en 1 行、zh-tw 6 行；ja/ru 干跑零 diff）。
- 注：导出器本身未修（超出本轮范围）；若后续工人重导出，仍须先干跑 diff。

## 门禁与 KIT（汇总）
- 6 版重渲染（ja/ru/it/pt/zh-tw/en）：`tools/gates.py` 全部 ALL PASS（occlusion 0 flags、p8 extract 150/150、p8 compare CLEAN keydiff=[137,138]、freeze 8/8、印/网文字 posdiff 0 msdiff 0、P8 答案区最小 10.12pt、chips = core、§1.1 clean）+ boxtitle/spill/edge/head_check/d5_creambox 全绿（唯一 marginal：it P6 `DATI INVENTATI` 0.6px，容差内）。
- ko：上一任落地，本轮自跑全套门禁 ALL PASS（同上口径）。
- core：无重渲染，text.md 一行改动。
- 8 份 KIT 均已更新为盘上实际 SHA（ja/ko/ru/it/pt/zh-tw/en/core）；de/es/fr 未动、KIT 未动。
- 未 commit、未 push、未跑 lint。未动任何 svglib.py。磁盘收尾 94G（门限 100G，未触发）。
- 日志：本目录各版子目录（run/render/export/export-dryrun/webpdf/gates/boxtitle/spill/edge/head-check/d5-creambox + text-before.md）。

## 不修项（协调员裁定，复述）
- 8（nl-ru R1 拉丁标题误用 Noto Sans）、9（nl-ru R2 P8 答案误用 Noto Serif CJK SC）：D5 机制跨家系统性问题，由后续跨家 *-ru 工人统一修 svglib.py 并重渲染；本轮绝不动任何 svglib.py 的字体路由。但 nl-ru 的问题 7（内容）仍由本轮修、照常重渲染。
- 18（pt P2 盒标题余 2.0pt）、19（es P7 余 2.6pt）、20（pt P6 余 2.4pt）：正余量、无溢出，记为已知偏紧，不修。
- 21 观察项：不动。

## 最终 SHA 总表（2026-11-12 收尾核查，盘上实际值；SHA-12）

| 版 | 印 PDF | 网 PDF | text.md |
|---|---|---|---|
| core-nl | 0c5d63b942d2 / 13830540（未变） | 2b6f223eaff9 / 1874709（未变） | aa1f470353f9 / 44087 |
| nl-de | 97420549c81e / 12104230（未变） | 2361bedfd4d5 / 1536341（未变） | c1342c3fe20d / 46226（未变） |
| nl-en | 1900408aabb9 / 12102278 | 7174a848673f / 1534350 | da6d999d5b51 / 45132 |
| nl-es | 2da02d5b3081 / 12107937（未变） | 249fda66604b / 1540062（未变） | 44fc3d5c4287 / 47649（未变） |
| nl-fr | 08f57ec27d86 / 12106421（未变） | 1b429a3ff61e / 1538511（未变） | f1d1154442c4 / 47744（未变） |
| nl-it | dc91af0aa78d / 12102273 | 9eff96cf487a / 1534364 | e9880da2da99 / 47194 |
| nl-ja | b886a483f641 / 18803540 | 2b38c2547606 / 1967732 | b7e5f5dc8b48 / 47804（本轮未变） |
| nl-ko | e7fa69a263fe / 13871386（上一任落地，本轮复核） | 218aebe12b4b / 1791786 | e13db87160d1 / 47576 |
| nl-pt | e2fe3b3a9568 / 12110707 | 40c51869695b / 1542854 | 67516e2163c8 / 47365 |
| nl-ru | bb407a7b067e / 12368148 | 1c13bb4f7311 / 1780327 | dd1c0c087c46 / 57909（本轮未变） |
| nl-zh-tw | 3fd293bfef56 / 13887537 | 542c6f1bc8e2 / 1976266 | bf1f627d1bbf / 44308 |

de/es/fr 三版与 PROOF-NOTE 字节一致，未动。全部 11 版印 PDF 均为 8 页；网 PDF 文字层与印版字节一致（各版 gates 的 print_web_text / pdftotext 门均通过）。

---

# 第二轮修复（2026-11-12，接 PROOF-NOTE-2.md 的 3 项新发现：2 low + 1 trivial）

- 范围：只动 `production/2026-w47/` 内 nl-de、nl-es、nl-en 三版；不 commit、不 push、不跑 lint。未动 svglib.py（ru 字体问题另有跨家工人处理）。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`。
- 磁盘：接手时 95G 已用 / 150G，收尾 95G（< 100G 门限，未触发）。
- 改前指纹（与 PROOF-NOTE-2 §一逐一一致）：de 印 `97420549c81e` / 12,104,230、网 `2361bedfd4d5` / 1,536,341、text `c1342c3fe20d` / 46,226；es 印 `2da02d5b3081` / 12,107,937、网 `249fda66604b` / 1,540,062、text `44fc3d5c4287` / 47,649；en 印 `1900408aabb9` / 12,102,278、网 `7174a848673f` / 1,534,350、text `da6d999d5b51` / 45,132。

## 修复记录（逐版；全部完成）

### nl-de（1 low：BRIEVEN 读者注释缺 "best P8 texts"）——已完成
- 源头：`content7.py:91` `Keine echten Briefe — Beispiel; Versprechen für VOL.5.` → `Keine echten Briefe oder besten P8-Texte — Beispiel; Versprechen für VOL.5.`（与 en `No letters or best P8 texts yet — an example; VOL.5 next.` 句式平行；fr `ni meilleur texte` / it `né migliori testi`；荷兰语核心行 `dt_nl` 本就含 `beste pagina-8-teksten`，未动）。
- 版式：新句在 `dt_zh_w` 353.25（20pt sans）折行 2 → 3 行（`wrap()` 实测）；盒高公式自适应，`P7 col3 ends` 1927.5 → 1956.5——与 en 版已发行的值完全相同。印 P7 目视确认（裁图）：三行在奶油盒内，末行 `Beispielbrief der Redaktion…` 在分隔线之上，无溢出、无压线。
- 重渲染：`run.py` TOTAL 150 RC 0 → `render.py` RC 0 → 导出干跑 /tmp → 重导出（150 题、8 金句、6 gloss）→ `webpdf.py` RC 0。
- 验：印 P7 含 `Keine echten Briefe oder besten / P8-Texte — Beispiel; Versprechen für / VOL.5.`（三行）。
- 导出器陷阱：干跑 diff 除意改行外多一行——第 287 行 `### VOOR OF TEGEN?　DAFÜR / DAGEGEN` 被导出器丢了 `### ` 前缀；已手工回补；最终 diff 只含 366 行。
- 门禁（`tools/gates.py` ALL PASS）：occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0（8 页）；pdftotext 印=网=46,678 B；P8 答案区最小 10.12pt；chips = core {A2: 8, B1: 24, B2: 3}；§1.1 clean。extras：boxtitle 0 DEFECT, 0 OBSERVE, 0 marginal；spill 0 SPILL（38 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS 0 defects；d5_creambox PASS 0 defects（修前基线在 /tmp 重建：P8 lines 228 → 228，footer slack 43.5px 不变）。
- 新 SHA：印 `9032021929da68607da8097bd50612aeec93f4b5de76d0e15e8757712172fb19`（12,104,245 B）；网 `fbf0c25a503a8fb532b60dc60d1b95b265a00659df1c69afb334b6bddf299795`（1,536,368 B）；text.md `6825c35db04c62e1bec4f8f6e6a511597a17af0b02b17bc5260a560043575785`（46,247 B）。KIT 已更新（Files delivered 同步 + 尾部 fix 条）。

### nl-es（2 low：Q140 源句 `sorpresa` 与版内术语 `surprise` 不一致）——已完成
- 源头：`content8.py:76` `Hago una sorpresa con un poema corto. → ___` → `Hago un surprise con un poema corto. → ___`（答案 `Ik maak een surprise met een kort gedicht.` 及附注 `(surprise: expresión fija; corto = kort)` 不动；对标 Q14 答案注释 `Un surprise es un regalo disfrazado`、词表 `de surprise regalo disfrazado`）。
- 重渲染：`run.py` TOTAL 150 RC 0 → `render.py` RC 0 → 导出干跑 /tmp → 重导出（150 题、8 金句、6 gloss）→ `webpdf.py` RC 0。
- 验：印 P8 含 `Hago un surprise con un poema corto.`，旧形 `Hago una sorpresa` 0。
- 导出器陷阱：干跑 diff 除意改行外多一行——第 280 行 `### DE GRAFIEK　DATOS DE PRÁCTICA` 被导出器丢了 `### ` 前缀；已手工回补；最终 diff 只含 415 行。
- 工具修补（本次导出必需）：共享导出器 stub `scratch-nl/stub_bslib47.py` 缺 es 专用的 `NOTE_RIGHT`（es `bslib4.py:21` 定义，core bslib 无此名，而 stub 加载的是 core bslib；es 全家仅 es 版用此名，共 8 处）——首次干跑报 `NameError: name 'NOTE_RIGHT' is not defined`（`content12.py:147`）。修法：stub 补 `NOTE_RIGHT = RIGHT - 10` 并加入 stub 的 `__all__` 白名单（只加定义不够：`from bslib4 import *` 只导 `__all__` 内名字，第一次只补定义仍报同一错，查到 `__all__` 后才通）。未动任何生产源文件、未动 svglib.py；第一轮未跑过 es 导出，故此前无人触发。
- 门禁（ALL PASS）：occlusion 0；p8 150/150；compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0；pdftotext 印=网=46,703 B；P8 最小 10.12pt；chips = core；§1.1 clean。extras：boxtitle 0 DEFECT, 0 OBSERVE, 0 marginal；spill 0 SPILL（39 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS；d5_creambox PASS 0 defects（修前基线在 /tmp 重建：P8 lines 237 → 237，footer slack 41.7px 不变）。
- 新 SHA：印 `06f0e2e00aece0d687edf0540098e4cc8b6e4e4c62b451792a1be6cb11608874`（12,107,932 B）；网 `7025ce05d97599d1910ab4e27f1e1c583ae86d43ef5d64a169b22bdb77ef0721`（1,540,051 B）；text.md `672bd4c0080c14ab11026a13ccdecf826bd759cc3f348c5751852386efe4684b`（47,648 B）。KIT 已更新（Files delivered 同步，含补登 text.md 的 sha256 行 + 尾部 fix 条）。

### nl-en（3 trivial：L45 ASCII 直引号）——已完成
- 他版同行核对（先核对后改）：其余 10 版同行均为排版引号——de `„Gruppensieg"`、es/fr/it/pt/ru `«…»`、ja/ko/zh-tw `「…」`。英语取排版双引号 `“…”`。
- 源头：`content12.py:113` `"Group win": first in the group.` → `“Group win”: first in the group.`。
- 重渲染：`run.py` TOTAL 150 RC 0 → `render.py` RC 0 → 导出干跑 /tmp → 重导出（150 题、8 金句、6 gloss）→ `webpdf.py` RC 0。
- 验：印 P1 含 `“Group win”: first in the group.`，直引号 0；SVG 文本节点内直引号 0。
- 导出器陷阱：干跑 diff 除意改行外多两行——第 287 行 `### VOOR OF TEGEN?　FOR OR AGAINST?` 与第 360 行 `### HET WOORD　WORD OF THE WEEK` 被导出器丢了 `### ` 前缀；均已手工回补；最终 diff 只含 45 行。
- 门禁（ALL PASS）：occlusion 0；p8 150/150；compare CLEAN，keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0；pdftotext 印=网=45,371 B；P8 最小 10.12pt；chips = core；§1.1 clean。extras：boxtitle 0 DEFECT, 0 OBSERVE, 0 marginal；spill 0 SPILL（37 OBSERVE）；edge 0 TOUCH, 0 NEAR；head_check PASS；d5_creambox PASS 0 defects（修前基线在 /tmp 重建：P8 lines 236 → 236，footer slack 38.4px 不变）。
- 新 SHA：印 `7e35b073ade00c564981bfee31526d1f6306c86e9c9ff3ae58199a278f9426af`（12,102,396 B）；网 `c7ffd6676cfa31798994f11af35a469485e6fefd1fa3a8e079c47c7aae3b0d95`（1,534,493 B）；text.md `e3273f300f42236a06faaddd3302b5be1a4a340adca285efdff19f2b23f3f316`（45,136 B）。KIT 已更新（该 KIT 无 Files delivered 节，在 D5 rebuild 条后追加 fix 条）。

## D5 census + 引号普查（本轮自写 `d5_census_round2.py`，SVG font-family 直计；tools 内无 census 工具）
- de/es/en：纯拉丁文本落入 Noto Sans（D5_lat 嫌疑）= 0；弯引号 U+201C/U+201D/U+2019 落入 CJK 字体 = 0。
- en 弯引号总数 2（本次新增的一对 `“ ”`），全部在 Newsreader 内；de 1、core 2（与 PROOF-NOTE-2 一致），其余版 0。
- 引号普查（11 版 text.md 全量）：ASCII 直引号 `"` 全部为 0——en 的一对是全家仅有的直引号，现已清零。
- ru：D5_lat = 478（本法口径；第一轮 338、PROOF-NOTE-2 329，均为方法口径差异——本法把纯标点/数字节点也计入；ru 未动，属已知跨家 D5 问题，不修）。

## 门禁与 KIT（汇总）
- 3 版重渲染：`tools/gates.py` 全部 ALL PASS（occlusion 0 flags、p8 extract 150/150、p8 compare CLEAN keydiff=[137,138]、freeze 8/8、印/网文字 posdiff 0 msdiff 0、P8 答案区最小 10.12pt、chips = core、§1.1 clean）+ boxtitle/spill/edge/head_check/d5_creambox 全绿，0 marginal。
- 3 份 KIT 均已更新为盘上实际 SHA（逐项与磁盘核对通过）；de/es 的 Files delivered 节同步，en 追加 fix 条。
- 未 commit、未 push、未跑 lint。未动任何 svglib.py。磁盘收尾 95G（门限 100G，未触发）。
- 日志：本目录各版子目录（run/render/export/export-dryrun/webpdf/gates/boxtitle/spill/edge/head-check/d5-creambox + text-before.md）+ 本轮 census 脚本 `d5_census_round2.py` 与 `census-round2.log`；门禁复用 `scratch-reproof2-w47-nl/gates.py` 的副本（`scratch-fix-nl/gates.py`）。
- /tmp 干跑目录与修前基线目录（dryrun-de/es/en、base-de/es/en）已清理。

## 不修项（复述）
- 第一轮已裁定不修的项（18/19/20、21、ko 括号习惯）未动；nl-ru 拉丁标题字体问题未动（跨家工人统一处理）；PROOF-NOTE-2 §五观察项（core ABSTRACT 未写明周次、it P6 `DATI INVENTATI` 0.6px marginal）未动。

## 最终 SHA 总表（第二轮，2026-11-12 收尾核查，盘上实际值；SHA-12）

| 版 | 印 PDF | 网 PDF | text.md |
|---|---|---|---|
| nl-de | 9032021929da / 12104245 | fbf0c25a503a / 1536368 | 6825c35db04c / 46247 |
| nl-es | 06f0e2e00aec / 12107932 | 7025ce05d975 / 1540051 | 672bd4c0080c / 47648 |
| nl-en | 7e35b073ade0 / 12102396 | c7ffd6676cfa / 1534493 | e3273f300f42 / 45136 |

其余 8 版未动，SHA 与第一轮总表一致。
