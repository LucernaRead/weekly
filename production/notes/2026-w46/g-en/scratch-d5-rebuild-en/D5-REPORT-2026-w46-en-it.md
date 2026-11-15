# D5 重建报告 — 2026-w46-en-it（Italian (it)读者版）

W46 en 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-it/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-EN-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-en/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `production/2026-w46/en_textmd.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5_latin_in_cjk=510 D5_cyrillic_in_cjk=0 curly_in_cjk=0 curly_total=0。
- 基线实测：印 PDF `99c3ec39c40133f24d0c1b0aea5c8793c563eb7a6ded0d385c8a3e5551f49e42`（14,663,347 B）；网 PDF `fc8791437d698555d5f93b41fcf4738907219ceda0f63138e4f5ad6a87a70e67`（1,435,420 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（45,145 B）。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 14/4：G1/G2 头 2（FOUR COUNTRIES、READ THE CHART 25pt）；G11 溢出 1（P2 DID YOU KNOW +12.77）；G14 盒标题 2（P1 In cifre +3.5、P4 Domenica +28.8；G12 0 DEFECT 2 OBSERVE——core 继承）。
- 二次修复（只降字号/调框高，文字零改动；探针 `bin/probe_fix.py` 量测在案）：
- `content12.py:123` FOUR COUNTRIES 25→24
- `content12.py:193/200` DID YOU KNOW 盒高 +14→+34、间距 +26→+6
- `content56.py:109` READ THE CHART 25→23
- `content12.py:46` P1 In cifre `tsize=22`
- `content34.py:169` P4 Domenica `tsize=21`
- P8：P8 行数/距页脚线余量 32.7->32.7px。

## 四、门禁（run2，ALL-GREEN）

- gates 2026-w46-en-it (patched=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w46-en/patched/2026-w46-en-it)
- 逐门：
- D18: PASS — D18 slogan 'WEEKLY IN ENGLISH\u3000Ogni settimana\u3000Di ' end_x=1346.6 date_start_x=1506.9 gap=160.3px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
- D37: PASS — D37 badge y=372 "TESTI IN INGLESE\u3000SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I " end_x=1323.8 cream_left=1439.5 margin=115.7px (PASS)
- G1: PASS — TOTAL exercises: 150, OVF=0, HDW=0
- G10: PASS — CJK added 0 (Latin added 323, run-split)
- G11: PASS — SPILL_SWEEP 2026-w46-en-it: 28 boxes, 104 candidates, 0 SPILL, 104 OBSERVE
- G12: PASS — BOXTITLE 2026-w46-en-it: 36 titles, 175 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
- G13: PASS — 0 TOUCH 0 NEAR
- G14: PASS — CREAMBOX PASS 0 defects
- G16: PASS — 0 defective
- G2: PASS — patched 0 defects (baseline-side findings: 0, D25)
- G3: PASS — CENSUS PASS
- G4: PASS — render rc=0, print 14174221 B
- G5: PASS — web 1396800 B <7MB
- G6: PASS — 0 flags
- G7: PASS — extract rc=0 (see p8-extract.json)
- G8: PASS — CLEAN, rc=0
- G9: PASS — 8/8 byte-identical
- 15b carryover 仅记录：CARRYOVER: FAIL；15c N/A（en 导出器家族，无原生校验器）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-it/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `1c3bdd2fa8ded45a94c3d9b1d403dec6bdf9ba86f86ffa5c4d3712515422eaae`（14,174,221 B）；新网 PDF `62eda0cb1b3d9fa0bb1457945c453069b1908b68c65a1402ec8bff3c0c13e90f`（1,396,800 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `9afa66a1506f…` |
| p2-life.svg | `d5055f75289d…` |
| p3-culture.svg | `7ec2ea11407f…` |
| p4-sport.svg | `66493c07ab08…` |
| p5-jeunesse.svg | `324b18d04b5c…` |
| p6-politique.svg | `fc5f1b785049…` |
| p7-langue.svg | `8b5d2d8a7648…` |
| p8-exercices.svg | `da033cc7c399…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（45,145 B，SHA `4c64a517fb3977a1d588d3b34a6118f865ae4df50671fb24b394043d4d31ab2e`）。
- KIT：`patched/2026-w46-en-it/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
