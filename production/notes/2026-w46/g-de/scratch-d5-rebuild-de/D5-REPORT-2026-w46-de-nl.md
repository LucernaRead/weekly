# D5 重建报告 — 2026-w46-de-nl（荷兰语读者版）

W46 de 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-de/logs/2026-w46-de-nl/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-DE-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target de --reader nl --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-de/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `hidden_files/style-port-de/export_de.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5 拉丁 632、西里尔 0、弯引号 CJK 0；花括号总量 30，全在 Newsreader 内、0 在 CJK 内。
- 基线实测：印 PDF `ff31ab49f8ea9aa2af635a11d11f67ffbff24312ddb2c7c76efdeac10786c9bd`（3,596,224 B）；网 PDF `4e628cbc67eb0b5848bed39938b5981a054979aca20296a6c19fa37a529bd656`（1,014,541 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（48,479 B）。KIT 印/网 SHA 针脚已过期（已知 KIT SHA 滞后），基线以文字层/export 证据为准，不以 KIT SHA 为准。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 16/19：盒标题 4（In cijfers +9.8、Sint Maarten +23.0 ×2、Werktuig +39.0）+ 预告带 TEXTX 1（与 INTERLANDWEEK 重叠 189.2px）；其余门全绿。
- 二次修复（只动字号，文字零改动；探针 `bin/probe_fix.py` 量测在案，留 ≥2px 余量；盒标题 f.box `tsize=` / `p.text` 字号字面量）：
- `content12.py:25` P1 预告带左标题 46→38pt（TEXTX 与右标题 `INTERLANDWEEK` 重叠 189.2px）
- `content12.py:43–47` P1 数字盒 `f.box` 加 `tsize=22`（标题右越 9.8px，23pt）
- `content34.py:46` + `content56.py:45` P3/P5 圣马丁词盒标题 24→22pt（右越 23.0px ×2）
- `content7.py:72` P7 工具箱标题 23→20pt（右越 39.0px；21pt 仍越 0.3px）
- P8：行数 228->231，距页脚线余量 40.3->40.3 px（y=2596 线、页底 2700）；p8 compare CLEAN（keydiff [137, 138, 139, 150]，预期读者键）。

## 四、门禁（run2，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（925,426 B <7MB）；occlusion 0（含自检，6 类全触发）；p8 extract 150/150；p8 compare CLEAN；freeze 基线 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0（新增 Latin 字符串 387，断 run 拆分，仅记录）；spill 0（32 boxes, 83 candidates, 0 SPILL）；boxtitle 0（48 titles, 243 body lines, 0 DEFECT）；edge 0 TOUCH 0 NEAR；creambox PASS 0 缺陷；文字层 print=web 多重集差 0（print=105876 web=105876）；census_quotes 0 defective；D18 刊头间距 64.7px（>0）；D37 副刊头余量 13.7px（>0）。
- 非门禁残留（D21/D22/D27 口径，仅记录）：15b carryover（3x 'november'、3x 'nfl'）；按 D21/D22/D27 口径以 15a + native verifier ADOPT 验收。15c native verifier ADOPT（0 UNEXPECTED）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-de/logs/2026-w46-de-nl/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `c368ec021b3efe4d9252123a690509afea4b1521835f732cdcb2e01c54b5a5e7`（2,978,765 B）；新网 PDF `f7e157dd327fcb9c4ae489cf3a3f57c288ff8c347dc6bfd80562a0841c53badd`（925,426 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `964a206c5068…` |
| p2-leben.svg | `691e231fb7af…` |
| p3-kultur.svg | `f04eb31040cc…` |
| p4-sport.svg | `c1e1de7e88e5…` |
| p5-jugend.svg | `123e7e9f41ca…` |
| p6-vertiefung.svg | `89b6eb6904e0…` |
| p7-sprache.svg | `a1396300f1d4…` |
| p8-uebungen.svg | `60774287a84e…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（48,479 B，SHA `77d08947890235b5329171fd8ee29eecd1e6aeda839cedfeba2e20aa894f59dc`）。
- KIT：`patched/2026-w46-de-nl/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录；版内 SVG 针脚旧表已随 D5 重排过期，新值见上表）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。

