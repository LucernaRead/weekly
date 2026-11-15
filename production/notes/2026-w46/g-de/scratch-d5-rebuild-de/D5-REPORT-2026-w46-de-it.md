# D5 重建报告 — 2026-w46-de-it（意大利语读者版）

W46 de 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-de/logs/2026-w46-de-it/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-DE-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target de --reader it --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-de/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `hidden_files/style-port-de/export_de.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5 拉丁 622、西里尔 0、弯引号 CJK 0；花括号总量 30，全在 Newsreader 内、0 在 CJK 内。
- 基线实测：印 PDF `7b714abd0399beaa48c558fa57d78862b084d6f01c773749b4fb48e5f67652dd`（3,594,471 B）；网 PDF `b926e2319fa8e45af14967a7c4c7aea79907bc83aa60094dcd70a0cdc27b026e`（1,012,136 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（48,792 B）。KIT 印/网 SHA 针脚已过期（已知 KIT SHA 滞后），基线以文字层/export 证据为准，不以 KIT SHA 为准。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 16/19：盒标题 6（In numeri +22.8、Sommario +8.5、San Martino +14.0 ×2、Attrezzi +24.0、Ancora una parola +17.6）+ 预告带 TEXTX 1（与 SETTIMANA DELLA NAZIONALE 重叠 173.2px）；其余门全绿。
- 二次修复（只动字号，文字零改动；探针 `bin/probe_fix.py` 量测在案，留 ≥2px 余量；盒标题 f.box `tsize=` / `p.text` 字号字面量）：
- `content12.py:25` P1 预告带左标题 46→38pt（TEXTX 与右标题 `SETTIMANA DELLA NAZIONALE` 重叠 173.2px）
- `content12.py:43–47` P1 数字盒 `f.box` 加 `tsize=21`（标题右越 22.8px，23pt；22pt 仍越 4.0px）
- `content12.py:89` P1 目录标题 24→22pt（右越 8.5px）
- `content34.py:46` + `content56.py:45` P3/P5 圣马丁词盒标题 24→22pt（右越 14.0px ×2）
- `content7.py:72` P7 工具箱标题 23→21pt（右越 24.0px）
- `content7.py:98` P7 `NOCH EIN WORT` 标题 22→20pt（右越 17.6px；21pt 仅余 1.3px）
- P8：行数 230->213，距页脚线余量 40.3->47.7 px（y=2596 线、页底 2700）；p8 compare CLEAN（keydiff [137, 138, 139, 150]，预期读者键）。

## 四、门禁（run2，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（926,581 B <7MB）；occlusion 0（含自检，6 类全触发）；p8 extract 150/150；p8 compare CLEAN；freeze 基线 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0（新增 Latin 字符串 391，断 run 拆分，仅记录）；spill 0（32 boxes, 83 candidates, 0 SPILL）；boxtitle 0（44 titles, 246 body lines, 0 DEFECT）；edge 0 TOUCH 0 NEAR；creambox PASS 0 缺陷；文字层 print=web 多重集差 0（print=108748 web=108748）；census_quotes 0 defective；D18 刊头间距 18.1px（>0）；D37 副刊头余量 95.3px（>0）。
- 非门禁残留（D21/D22/D27 口径，仅记录）：15b carryover（4x 'b1'、4x 'level'）；按 D21/D22/D27 口径以 15a + native verifier ADOPT 验收。15c native verifier ADOPT（0 UNEXPECTED）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-de/logs/2026-w46-de-it/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `6aa82584b7ece2ede2963781d2ab7843bbab14eb3bfc948aab520195d396f23e`（2,979,929 B）；新网 PDF `55842062673279b68ee000688e3a520861a1f61c487932f753433ae94c4b9f3a`（926,581 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `efa6dcfc21f6…` |
| p2-leben.svg | `534b277d216d…` |
| p3-kultur.svg | `89c855319d2a…` |
| p4-sport.svg | `8e04efb7f1d6…` |
| p5-jugend.svg | `9927d23e8254…` |
| p6-vertiefung.svg | `d5d38d06ce1a…` |
| p7-sprache.svg | `ecc1e01ac495…` |
| p8-uebungen.svg | `af01b7d54917…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（48,792 B，SHA `6f00bc98c8d6d498b1bc034f473080650f9a11d98be730942cad5b32271db9f3`）。
- KIT：`patched/2026-w46-de-it/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录；版内 SVG 针脚旧表已随 D5 重排过期，新值见上表）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。

