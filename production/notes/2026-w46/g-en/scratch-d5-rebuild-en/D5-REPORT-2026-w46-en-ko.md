# D5 重建报告 — 2026-w46-en-ko（Korean (ko)读者版）

W46 en 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-ko/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-EN-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "cjk"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-en/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `production/2026-w46/en_textmd.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5_latin_in_cjk=374 D5_cyrillic_in_cjk=0 curly_in_cjk=1 curly_total=2。
- 基线实测：印 PDF `e08c7e8a3cbbf6626ed3c894f7a5bdc8055d4989449129a391e01fdd3abf3d1c`（17,158,620 B）；网 PDF `516f647725a309819bed56729cdcdb89255576ee8a8c31ece9d208bff01ba7e9`（1,622,188 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（45,561 B）。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 12/6：G1/G2 头 1（FOUR COUNTRIES）；G6 暗带重叠 1（交叠 8.2px）；G8 p8 #150 丢失（D5 分行丢破折号前空格，tools/p8.py D21 校准已修）；G11 溢出 1（P2 DID YOU KNOW +12.77）；G14 盒标题 1（P4 일정 +25.7；G12 0 DEFECT）。
- 二次修复（只降字号/调框高，文字零改动；探针 `bin/probe_fix.py` 量测在案）：
- `content12.py:123` FOUR COUNTRIES 25→24
- `content12.py:193/200` DID YOU KNOW 盒高 +14→+34、间距 +26→+6
- `content12.py:25` 暗带左标题 46→45
- `content34.py:169` P4 일요일 일정 `tsize=21`
- G8：`tools/p8.py` D21 校准（detect_note 补 CJK 后破折号前空格恢复；回归 22 组仅 ko 一行变化，见家族报告 §0.1）
- P8：P8 行数/距页脚线余量 32.7->52.8px。

## 四、门禁（run2，ALL-GREEN）

- gates 2026-w46-en-ko (patched=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w46-en/patched/2026-w46-en-ko)
- 逐门：
- D18: PASS — D18 slogan 'WEEKLY IN ENGLISH\u3000매주 한 번\u3000영어권에서 지금 화제' end_x=1284.0 date_start_x=1506.9 gap=222.9px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
- D37: PASS — D37 badge y=372 '영어 텍스트\u3000한국어 해설 — 한국어 독자를 위한 판' end_x=1142.1 cream_left=1439.5 margin=297.4px (PASS)
- G1: PASS — TOTAL exercises: 150, OVF=0, HDW=0
- G10: PASS — CJK added 0 (Latin added 320, run-split)
- G11: PASS — SPILL_SWEEP 2026-w46-en-ko: 28 boxes, 146 candidates, 0 SPILL, 146 OBSERVE
- G12: PASS — BOXTITLE 2026-w46-en-ko: 54 titles, 319 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
- G13: PASS — 0 TOUCH 0 NEAR
- G14: PASS — CREAMBOX PASS 0 defects
- G16: PASS — 0 defective
- G2: PASS — patched 0 defects (baseline-side findings: 0, D25)
- G3: PASS — CENSUS PASS
- G4: PASS — render rc=0, print 14932033 B
- G5: PASS — web 1566054 B <7MB
- G6: PASS — 0 flags
- G7: PASS — extract rc=0 (see p8-extract.json)
- G8: PASS — CLEAN, rc=0
- G9: PASS — 8/8 byte-identical
- 15b carryover 仅记录：CARRYOVER: FAIL；15c N/A（en 导出器家族，无原生校验器）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-ko/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `c1e641305ad7d150e213aaa8f99aaca28701464767282f898c5306f4f48e2ac7`（14,932,033 B）；新网 PDF `fddd09355eeac4ee0a381f7ab6f66196856f58f541e67937d9d989727c9013a6`（1,566,054 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `1bea2a294222…` |
| p2-life.svg | `3d8006d90c47…` |
| p3-culture.svg | `4985a4ec97f9…` |
| p4-sport.svg | `a89bc40b4636…` |
| p5-jeunesse.svg | `acc06639a762…` |
| p6-politique.svg | `43d8c0b980db…` |
| p7-langue.svg | `5e54ac94d03a…` |
| p8-exercices.svg | `6c6c8ac02fe7…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（45,561 B，SHA `901814843eef538b136d4b38465cf7dc17d34dd152ea9ec6d32e17358832a631`）。
- KIT：`patched/2026-w46-en-ko/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
