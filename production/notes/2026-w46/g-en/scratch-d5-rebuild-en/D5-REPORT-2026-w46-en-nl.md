# D5 重建报告 — 2026-w46-en-nl（Dutch (nl)读者版）

W46 en 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-nl/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-EN-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-en/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `production/2026-w46/en_textmd.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5_latin_in_cjk=544 D5_cyrillic_in_cjk=0 curly_in_cjk=0 curly_total=0。
- 基线实测：印 PDF `b2501fa8d49e785e08672695b9ac244968143a026520b7aac15671c0c359ce07`（14,667,704 B）；网 PDF `794a6bb351ed077789609425d5eac5d1cf44c7a10d2041a1b5eaa1b2b4c97c99`（1,441,726 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（44,935 B）。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 13/5：G1/G2 头 2（FOUR COUNTRIES、B MULTIPLE CHOICE 24pt）；G11 溢出 2（P2 DID YOU KNOW +12.77、P7 读者信箱 +10.00）；G12/G14 盒标题 2（P3 Scrooge-nacht +11.0、P4 Waarom München? +33.8）。
- 二次修复（只降字号/调框高，文字零改动；探针 `bin/probe_fix.py` 量测在案）：
- `content12.py:123` FOUR COUNTRIES 25→24
- `content12.py:193/200` DID YOU KNOW 盒高 +14→+34、间距 +26→+6
- `content8.py:43` B MULTIPLE CHOICE 24→22（gap=8 保留）
- `content34.py:83` P3 Scrooge-nacht `tsize=22`；`:108` P4 Waarom München? `tsize=21`
- `content7.py:112` P7 读者信箱 rect 300→318
- P8：P8 行数/距页脚线余量 34.8->34.9px。

## 四、门禁（run2，ALL-GREEN）

- gates 2026-w46-en-nl (patched=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w46-en/patched/2026-w46-en-nl)
- 逐门：
- D18: PASS — D18 slogan 'WEEKLY IN ENGLISH\u3000Elke week\u3000Waar de ' end_x=1330.1 date_start_x=1506.9 gap=176.8px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
- D37: PASS — D37 badge y=372 'TEKSTEN IN HET ENGELS\u3000UITLEG IN HET NEDERLANDS — DE EDITIE V' end_x=1413.7 cream_left=1439.5 margin=25.8px (PASS)
- G1: PASS — TOTAL exercises: 150, OVF=0, HDW=0
- G10: PASS — CJK added 0 (Latin added 371, run-split)
- G11: PASS — SPILL_SWEEP 2026-w46-en-nl: 28 boxes, 108 candidates, 0 SPILL, 108 OBSERVE
- G12: PASS — BOXTITLE 2026-w46-en-nl: 36 titles, 175 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal
- G13: PASS — 0 TOUCH 0 NEAR
- G14: PASS — CREAMBOX PASS 0 defects
- G16: PASS — 0 defective
- G2: PASS — patched 0 defects (baseline-side findings: 0, D25)
- G3: PASS — CENSUS PASS
- G4: PASS — render rc=0, print 14177107 B
- G5: PASS — web 1399678 B <7MB
- G6: PASS — 0 flags
- G7: PASS — extract rc=0 (see p8-extract.json)
- G8: PASS — EXTRA_ONLY, rc=0
- G9: PASS — 8/8 byte-identical
- 15b carryover 仅记录：CARRYOVER: FAIL；15c N/A（en 导出器家族，无原生校验器）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-nl/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `e7480b282e0b4d9181e1675ffa7f43dadbc0337f6a5318694bc0c8502988d059`（14,177,107 B）；新网 PDF `9749499f4c645da2f24c131bb5bbc75040870e6dd85ca7253b941bdbbf5457ee`（1,399,678 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `bcb9b5938b6a…` |
| p2-life.svg | `50e031b58409…` |
| p3-culture.svg | `4eb51dfb1757…` |
| p4-sport.svg | `5c9ac30f9210…` |
| p5-jeunesse.svg | `7540d5926b66…` |
| p6-politique.svg | `77f2e836cea6…` |
| p7-langue.svg | `a09005154c15…` |
| p8-exercices.svg | `879bb6fefa86…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（44,935 B，SHA `578af9d063673d2f6cc3e434f69af672bd67dce24f709efbff914ee4881a7274`）。
- KIT：`patched/2026-w46-en-nl/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
