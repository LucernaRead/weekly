# D5 重建报告 — 2026-w46-en-zh-tw（Traditional Chinese (zh-tw)读者版）

W46 en 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-zh-tw/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-EN-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "cjk"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-en/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `production/2026-w46/en_textmd.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5_latin_in_cjk=370 D5_cyrillic_in_cjk=0 curly_in_cjk=0 curly_total=0。
- 基线实测：印 PDF `32c09d1e6da40c0cffa1327afc62fc9e4113129de9c133597454ca8e7a996e83`（23,451,014 B）；网 PDF `fa264957612f6f0427c8dbef732a1741ac7b500831313795a22e7b9aef3e4eea`（1,982,926 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（43,204 B）。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 14/4：G1/G2 头 1（FOUR COUNTRIES）；G11 溢出 1（P2 DID YOU KNOW +12.77）；G14 盒标题 2（P1 數字看本週 +36.5、P4 週日賽程 +6.8；G12 0 DEFECT 2 OBSERVE）。
- 二次修复（只降字号/调框高，文字零改动；探针 `bin/probe_fix.py` 量测在案）：
- `content12.py:123` FOUR COUNTRIES 25→24
- `content12.py:193/200` DID YOU KNOW 盒高 +14→+34、间距 +26→+6
- `content12.py:46` P1 數字看本週 `tsize=21`
- `content34.py:169` P4 週日賽程 `tsize=22`
- P8：P8 行数/距页脚线余量 32.7->35.1px。

## 四、门禁（run2，ALL-GREEN）

- gates 2026-w46-en-zh-tw (patched=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w46-en/patched/2026-w46-en-zh-tw)
- 逐门：
- D18: PASS — D18 slogan 'WEEKLY IN ENGLISH\u3000每週一期\u3000讀英語世界正在談的事' end_x=1229.8 date_start_x=1506.9 gap=277.1px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
- D37: PASS — D37 badge y=372 '英語正文\u3000繁體中文講解 — 給繁體中文讀者的版本' end_x=1152.5 cream_left=1439.5 margin=287.0px (PASS)
- G1: PASS — TOTAL exercises: 150, OVF=0, HDW=0
- G10: PASS — CJK added 0 (Latin added 320, run-split)
- G11: PASS — SPILL_SWEEP 2026-w46-en-zh-tw: 28 boxes, 113 candidates, 0 SPILL, 113 OBSERVE
- G12: PASS — BOXTITLE 2026-w46-en-zh-tw: 37 titles, 233 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
- G13: PASS — 0 TOUCH 0 NEAR
- G14: PASS — CREAMBOX PASS 0 defects
- G16: PASS — 0 defective
- G2: PASS — patched 0 defects (baseline-side findings: 0, D25)
- G3: PASS — CENSUS PASS
- G4: PASS — render rc=0, print 15488945 B
- G5: PASS — web 1751666 B <7MB
- G6: PASS — 0 flags
- G7: PASS — extract rc=0 (see p8-extract.json)
- G8: PASS — CLEAN, rc=0
- G9: PASS — 8/8 byte-identical
- 15b carryover 仅记录：CARRYOVER: FAIL；15c N/A（en 导出器家族，无原生校验器）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-zh-tw/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `ece9a8fba0470705c9e12490d8ca8bc8bb4e9de844ff41ac88156d0a4cbbc60e`（15,488,945 B）；新网 PDF `cd65f8a27a7f21d2d4ce550898e56f4213285a9c85df24f9a77492f5806082b8`（1,751,666 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `cd8368028e5b…` |
| p2-life.svg | `c76214af1c6e…` |
| p3-culture.svg | `9ebde786fd38…` |
| p4-sport.svg | `c8dc551b5abd…` |
| p5-jeunesse.svg | `33682febda5f…` |
| p6-politique.svg | `c405d5170440…` |
| p7-langue.svg | `34e8837dc4a7…` |
| p8-exercices.svg | `ce0423bbffa2…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（43,204 B，SHA `bf5f0fc07fa1fab734f1bd3b9b0e5a6733f7c6d138185b3573af11b0f69ca1a5`）。
- KIT：`patched/2026-w46-en-zh-tw/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
