# D5 重建报告 — 2026-w46-en-pt（Portuguese (pt)读者版）

W46 en 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-pt/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-EN-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-en/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `production/2026-w46/en_textmd.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5_latin_in_cjk=515 D5_cyrillic_in_cjk=0 curly_in_cjk=0 curly_total=0。
- 基线实测：印 PDF `4ec6be86002d1a14b77bc1aa5c31f09e3da69baf968ba92815d3dfb90e350883`（14,668,657 B）；网 PDF `aa10ee53e475666e22771aa9c366a1f110a0daa21c8c59e1e888b5e698abe93b`（1,442,599 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（45,377 B）。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 13/5：G1/G2 头 2（FOUR COUNTRIES、READ THE CHART 25pt）；G11 溢出 1（P2 DID YOU KNOW +12.77）；G12/G14 盒标题 3（P1 Números +23.5、P4 Porquê Munique? +13.8、P4 Domingo +17.8；G12 1 DEFECT 2 OBSERVE）。
- 二次修复（只降字号/调框高，文字零改动；探针 `bin/probe_fix.py` 量测在案）：
- `content12.py:123` FOUR COUNTRIES 25→24
- `content12.py:193/200` DID YOU KNOW 盒高 +14→+34、间距 +26→+6
- `content56.py:109` READ THE CHART 25→24
- `content12.py:46` P1 Números `tsize=21`
- `content34.py:108` P4 Porquê Munique? `tsize=22`；`:169` P4 Domingo `tsize=21`
- P8：P8 行数/距页脚线余量 32.7->32.7px。

## 四、门禁（run2，ALL-GREEN）

- gates 2026-w46-en-pt (patched=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w46-en/patched/2026-w46-en-pt)
- 逐门：
- D18: PASS — D18 slogan 'WEEKLY IN ENGLISH\u3000Todas as semanas\u3000D' end_x=1348.4 date_start_x=1506.9 gap=158.5px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
- D37: PASS — D37 badge y=372 'TEXTOS EM INGLÊS\u3000EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS' end_x=1432.0 cream_left=1439.5 margin=7.5px (PASS)
- G1: PASS — TOTAL exercises: 150, OVF=0, HDW=0
- G10: PASS — CJK added 0 (Latin added 345, run-split)
- G11: PASS — SPILL_SWEEP 2026-w46-en-pt: 28 boxes, 105 candidates, 0 SPILL, 105 OBSERVE
- G12: PASS — BOXTITLE 2026-w46-en-pt: 34 titles, 176 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
- G13: PASS — 0 TOUCH 0 NEAR
- G14: PASS — CREAMBOX PASS 0 defects
- G16: PASS — 0 defective
- G2: PASS — patched 0 defects (baseline-side findings: 0, D25)
- G3: PASS — CENSUS PASS
- G4: PASS — render rc=0, print 14182624 B
- G5: PASS — web 1405181 B <7MB
- G6: PASS — 0 flags
- G7: PASS — extract rc=0 (see p8-extract.json)
- G8: PASS — CLEAN, rc=0
- G9: PASS — 8/8 byte-identical
- 15b carryover 仅记录：ERROR: no verify_textmd table for reader 'pt' yet — calibrate it from that edition's own SVG/.text.md until its residual is 0, then add it to READER_TABLES in /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/tools/verify_textmd.py；15c N/A（en 导出器家族，无原生校验器）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-pt/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `bfa60f3d045a498559f315418a3effdb1546a10746d83548d2e1d75fe8758871`（14,182,624 B）；新网 PDF `e51307b135474f69125a7bb2e5e35ddd1da5e8907f56879d6c5e4f7f7115f0a4`（1,405,181 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `e3461781dd78…` |
| p2-life.svg | `6f7ac5a041ed…` |
| p3-culture.svg | `736b587c9c62…` |
| p4-sport.svg | `46fb5eced636…` |
| p5-jeunesse.svg | `e96f15dc7d96…` |
| p6-politique.svg | `69e7de34cdfd…` |
| p7-langue.svg | `a6f2e2404839…` |
| p8-exercices.svg | `6e19623c7b92…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（45,377 B，SHA `a0d79ff0c87f5db4eb2a4354423d13052a9c17c26fac9e559853b820f14058b7`）。
- KIT：`patched/2026-w46-en-pt/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
