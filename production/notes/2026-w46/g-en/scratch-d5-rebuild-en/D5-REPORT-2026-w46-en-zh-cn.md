# D5 重建报告 — 2026-w46-en-zh-cn（Simplified Chinese (zh-cn)读者版）

W46 en 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-zh-cn/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-EN-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "cjk"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-en/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `production/2026-w46/en_textmd.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5_latin_in_cjk=373 D5_cyrillic_in_cjk=0 curly_in_cjk=2 curly_total=4。
- 基线实测：印 PDF `ff08f65652f6d8e2232da7894245ef0ea622642a209170f4af72a53c0ce76285`（26,757,171 B）；网 PDF `cc83acfb7a85e432b7c582b74b06f02324391a18f970ed7c6db2e7cd7cd2afc8`（1,833,011 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（43,160 B）。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 13/5：G1/G2 头 1（FOUR COUNTRIES 25pt）；G11 溢出 1（P2 DID YOU KNOW 末行 +12.77）；G12/G14 盒标题 2（P1 数字盒 +36.5、P4 周日赛程 +6.8）。
- 二次修复（只降字号/调框高，文字零改动；探针 `bin/probe_fix.py` 量测在案）：
- `content12.py:123` FOUR COUNTRIES 25→24
- `content12.py:193` DID YOU KNOW 盒高 +14→+34，`content12.py:200` 两盒间距 +26→+6
- `content12.py:46` P1 数字盒 `tsize=21`
- `content34.py:169` P4 周日赛程 `tsize=22`
- P8：P8 行数/距页脚线余量 52.8->33.7px。

## 四、门禁（run2，ALL-GREEN）

- gates 2026-w46-en-zh-cn (patched=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w46-en/patched/core-en)
- 逐门：
- D18: PASS — D18 slogan 'WEEKLY IN ENGLISH\u3000每周一期\u3000读英语世界正在谈的事' end_x=1229.8 date_start_x=1506.9 gap=277.1px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
- D37: PASS — D37 badge y=372 "THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM LONDON TO" end_x=1302.6 cream_left=1439.5 margin=136.9px (PASS)
- G1: PASS — TOTAL exercises: 150, OVF=0, HDW=0
- G10: PASS — CJK added 0 (Latin added 371, run-split)
- G11: PASS — SPILL_SWEEP core-en: 28 boxes, 113 candidates, 0 SPILL, 113 OBSERVE
- G12: PASS — BOXTITLE 2026-w46-en-zh-cn: 37 titles, 233 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
- G13: PASS — 0 TOUCH 0 NEAR
- G14: PASS — CREAMBOX PASS 0 defects
- G16: PASS — 0 defective
- G2: PASS — patched 0 defects (baseline-side findings: 0, D25)
- G3: PASS — CENSUS PASS
- G4: PASS — render rc=0, print 15434179 B
- G5: PASS — web 1666411 B <7MB
- G6: PASS — 0 flags
- G7: PASS — extract rc=0 (see p8-extract.json)
- G8: PASS — CLEAN, rc=0
- G9: PASS — 8/8 byte-identical
- 15b carryover 仅记录：CARRYOVER: FAIL；15c N/A（en 导出器家族，无原生校验器）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-zh-cn/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `ebe1c0039027a495d9f080883b6ec0c851c5a4aa53aaff3b8221052d4d4c5da2`（15,434,179 B）；新网 PDF `9287b167a9e7be681dc0517f44eccf41d4ffc4ffc69082e5cc714110d026e8fe`（1,666,411 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `5a03391fbff8…` |
| p2-life.svg | `ba03c903cfa2…` |
| p3-culture.svg | `ddc03745cd2f…` |
| p4-sport.svg | `c8c0719d24d1…` |
| p5-jeunesse.svg | `39fe414263a0…` |
| p6-politique.svg | `b09381bd11e4…` |
| p7-langue.svg | `9ff54b0e77b0…` |
| p8-exercices.svg | `60638bec44a2…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（43,160 B，SHA `604fbf0bf3e8182b7aef06934679f59e7d771741e74906e52507175352b04373`）。
- KIT：`patched/core-en/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
