# D5 重建报告 — 2026-w46-en-ja（Japanese (ja)读者版）

W46 en 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-ja/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-EN-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "cjk"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-en/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `production/2026-w46/en_textmd.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5_latin_in_cjk=375 D5_cyrillic_in_cjk=0 curly_in_cjk=0 curly_total=0。
- 基线实测：印 PDF `6d08eeb422ce8f057465313154a69821d425b627cc1f175675a69f02785a07db`（25,976,528 B）；网 PDF `162ebc7bfdaab2b9b9bf2cae2059d748faf00adf18dc4651b34a3206a0c3f71a`（1,892,676 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（45,737 B）。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 11/7：G1/G2 头 2（FOUR COUNTRIES、D SENTENCES 24pt）；G6 暗带重叠 1（左标题与右标题交叠 31.7px）；G11 溢出 1（P2 DID YOU KNOW +12.77）；G12/G14 盒标题 5（P1 今週の数字 +36.5、P2 あなたのことを話そう +2.8、P3 スクルージの夜 +10.0、P4 日曜の試合 +29.8、P6 練習用投票用紙 +38.4）；D37 量测脚本 bug（已修）。
- 二次修复（只降字号/调框高，文字零改动；探针 `bin/probe_fix.py` 量测在案）：
- `content12.py:123` FOUR COUNTRIES 25→24
- `content12.py:193/200` DID YOU KNOW 盒高 +14→+34、间距 +26→+6
- `content8.py:71` D SENTENCES 24→22（gap=8 保留）
- `content12.py:25` 暗带左标题 46→44
- `content12.py:46` P1 今週の数字 `tsize=21`；`content12.py:205` AND YOU 标题 24→23
- `content34.py:83` P3 スクルージの夜 `tsize=22`；`:169` P4 日曜の試合 `tsize=21`
- `content56.py:105` P6 練習用投票用紙 `tsize=20`
- P8：P8 行数/距页脚线余量 32.7->32.7px。

## 四、门禁（run2，ALL-GREEN）

- gates 2026-w46-en-ja (patched=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w46-en/patched/2026-w46-en-ja)
- 逐门：
- D18: PASS — D18 slogan 'WEEKLY IN ENGLISH\u3000毎週1回\u3000英語圏で話題のこと' end_x=1217.0 date_start_x=1506.9 gap=289.9px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
- D37: PASS — D37 badge y=372 '英語テキスト\u3000日本語の解説 — 日本語読者のための版' end_x=1168.3 cream_left=1439.5 margin=271.2px (PASS)
- G1: PASS — TOTAL exercises: 150, OVF=0, HDW=0
- G10: PASS — CJK added 0 (Latin added 323, run-split)
- G11: PASS — SPILL_SWEEP 2026-w46-en-ja: 28 boxes, 111 candidates, 0 SPILL, 111 OBSERVE
- G12: PASS — BOXTITLE 2026-w46-en-ja: 37 titles, 250 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
- G13: PASS — 0 TOUCH 0 NEAR
- G14: PASS — CREAMBOX PASS 0 defects
- G16: PASS — 0 defective
- G2: PASS — patched 0 defects (baseline-side findings: 0, D25)
- G3: PASS — CENSUS PASS
- G4: PASS — render rc=0, print 19632806 B
- G5: PASS — web 1759693 B <7MB
- G6: PASS — 0 flags
- G7: PASS — extract rc=0 (see p8-extract.json)
- G8: PASS — CLEAN, rc=0
- G9: PASS — 8/8 byte-identical
- 15b carryover 仅记录：CARRYOVER: FAIL；15c N/A（en 导出器家族，无原生校验器）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-en/logs/2026-w46-en-ja/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `80cf6369e42cb2a706de1e52c511a08f69a4fb8c6633f4373a9b74efd2133374`（19,632,806 B）；新网 PDF `eef28e9ae5b9cb6534f4d0bd7f2f0cfd69e320292aac9082693548f79a635d4f`（1,759,693 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `8798904f4497…` |
| p2-life.svg | `d5dc1f825b77…` |
| p3-culture.svg | `cd0414e19b1f…` |
| p4-sport.svg | `d1666eb1bf2c…` |
| p5-jeunesse.svg | `aebebe93d7c6…` |
| p6-politique.svg | `fb2a25da444b…` |
| p7-langue.svg | `2b616ae70d33…` |
| p8-exercices.svg | `50f3750e04a2…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（45,737 B，SHA `7693cc0ca1b6d7a6184feadd1d83286df497a7bd18fdded929a8e35973b89f94`）。
- KIT：`patched/2026-w46-en-ja/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
