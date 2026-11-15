# D5 重建报告 — 2026-w46-en-de（German (de)读者版）

W46 en 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-de/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-EN-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-en/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `production/2026-w46/en_textmd.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5_latin_in_cjk=546 D5_cyrillic_in_cjk=0 curly_in_cjk=0 curly_total=0。
- 基线实测：印 PDF `b314cc5bac4037b94d4065724103de853e9416acaa8ffc12fb2925ce9b96679e`（14,669,384 B）；网 PDF `71a2a7310daed60409c904a863e3e88a200b7cc8f281501ccf49c9a73fb09d57`（1,443,113 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（44,922 B）。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 11/7：G1/G2 头 3（FOUR COUNTRIES、THE TOOLBOX 27pt、THE ERROR CLINIC 25pt）；G11 溢出 2（P2 DID YOU KNOW +12.77、P7 读者信箱 +10.00）；G12/G14 盒标题 4（P3 Scrooge-Nacht +14.0、P4 Warum München? +22.8、P4 Sonntag +9.8、P6 Stimmzettel +16.4）；D18/D37 量测脚本 bug（已修，见家族报告 §0.1）。
- 二次修复（只降字号/调框高，文字零改动；探针 `bin/probe_fix.py` 量测在案）：
- `content12.py:123` FOUR COUNTRIES 25→24
- `content12.py:193/200` DID YOU KNOW 盒高 +14→+34、间距 +26→+6
- `content7.py:48` THE TOOLBOX 27→25；`content7.py:99` THE ERROR CLINIC 25→24
- `content34.py:83` P3 Scrooge `tsize=22`；`:108` P4 Warum München? `tsize=21`；`:169` P4 Sonntag `tsize=22`
- `content56.py:105` P6 Stimmzettel `tsize=22`
- `content7.py:112` P7 读者信箱 rect 300→318
- P8：P8 行数/距页脚线余量 34.9->34.8px。

## 四、门禁（run2，ALL-GREEN）

- gates 2026-w46-en-de (patched=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w46-en/patched/2026-w46-en-de)
- 逐门：
- D18: PASS — D18 slogan 'WEEKLY IN ENGLISH\u3000Jede Woche neu\u3000Was' end_x=1392.0 date_start_x=1506.9 gap=114.9px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
- D37: PASS — D37 badge y=372 'ENGLISCHER TEXT\u3000DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTS' end_x=1380.4 cream_left=1439.5 margin=59.1px (PASS)
- G1: PASS — TOTAL exercises: 150, OVF=0, HDW=0
- G10: PASS — CJK added 0 (Latin added 359, run-split)
- G11: PASS — SPILL_SWEEP 2026-w46-en-de: 28 boxes, 109 candidates, 0 SPILL, 109 OBSERVE
- G12: PASS — BOXTITLE 2026-w46-en-de: 36 titles, 179 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
- G13: PASS — 0 TOUCH 0 NEAR
- G14: PASS — CREAMBOX PASS 0 defects
- G16: PASS — 0 defective
- G2: PASS — patched 0 defects (baseline-side findings: 0, D25)
- G3: PASS — CENSUS PASS
- G4: PASS — render rc=0, print 14179912 B
- G5: PASS — web 1402509 B <7MB
- G6: PASS — 0 flags
- G7: PASS — extract rc=0 (see p8-extract.json)
- G8: PASS — EXTRA_ONLY, rc=0
- G9: PASS — 8/8 byte-identical
- 15b carryover 仅记录：CARRYOVER: FAIL；15c N/A（en 导出器家族，无原生校验器）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-de/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `bc68a33fa76da6ce8dfdffc5cb990fb969243dedaa22d8202ed598604367a3d2`（14,179,912 B）；新网 PDF `645f89003c5283f166a72d12db1d3ef1596d25e0465af721ea5a4163c050718b`（1,402,509 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `4095d97d3fd0…` |
| p2-life.svg | `5084e767f0bd…` |
| p3-culture.svg | `0dea93cf97c2…` |
| p4-sport.svg | `b81254f2e5b6…` |
| p5-jeunesse.svg | `f7bcd9cdf261…` |
| p6-politique.svg | `bdd6346e650a…` |
| p7-langue.svg | `26ddb36ed828…` |
| p8-exercices.svg | `2ab129dc5888…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（44,922 B，SHA `375f756cba2cee70b902ddb95767e00f6dd42a0760450495afeab0619c37bedc`）。
- KIT：`patched/2026-w46-en-de/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
