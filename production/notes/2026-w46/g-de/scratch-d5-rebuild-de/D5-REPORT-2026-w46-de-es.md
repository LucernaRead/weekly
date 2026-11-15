# D5 重建报告 — 2026-w46-de-es（西班牙语读者版）

W46 de 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-de/logs/2026-w46-de-es/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-DE-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target de --reader es --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-de/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `hidden_files/style-port-de/export_de.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5 拉丁 622、西里尔 0、弯引号 CJK 0；花括号总量 30，全在 Newsreader 内、0 在 CJK 内。
- 基线实测：印 PDF `eecb0bdbfc308b2c0a1ddd95a25d5afe36afb3d1556efb86eb61b38d62779ff1`（3,599,246 B）；网 PDF `4697a5003361e4b3d0780483e110a704958c2a6b32c548905c9fcb3686a68702`（1,018,979 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（49,309 B）。KIT 印/网 SHA 针脚已过期（已知 KIT SHA 滞后），基线以文字层/export 证据为准，不以 KIT SHA 为准。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 14/19：盒标题 1（En cifras +10.8）+ 预告带 TEXTX 1（与 SEMANA DE SELECCIONES 重叠 171.7px）+ D37 1（余量 −13.0px）；其余门全绿。
- 二次修复（只动字号，文字零改动；探针 `bin/probe_fix.py` 量测在案，留 ≥2px 余量；盒标题 f.box `tsize=` / `p.text` 字号字面量）：
- `content12.py:25` P1 预告带左标题 46→38pt（TEXTX 与右标题 `SEMANA DE SELECCIONES` 重叠 171.7px）
- `content12.py:43–47` P1 数字盒 `f.box` 加 `tsize=22`（标题右越 10.8px，23pt）
- `content12.py:19` P1 副刊头行（y=372）16→15pt（D37 余量 −13.0px）
- P8：行数 216->220，距页脚线余量 36.2->40.4 px（y=2596 线、页底 2700）；p8 compare CLEAN（keydiff [137, 138, 139, 150]，预期读者键）。

## 四、门禁（run2，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（933,590 B <7MB）；occlusion 0（含自检，6 类全触发）；p8 extract 150/150；p8 compare CLEAN；freeze 基线 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0（新增 Latin 字符串 392，断 run 拆分，仅记录）；spill 0（32 boxes, 83 candidates, 0 SPILL）；boxtitle 0（50 titles, 238 body lines, 0 DEFECT）；edge 0 TOUCH 0 NEAR；creambox PASS 0 缺陷；文字层 print=web 多重集差 0（print=107874 web=107874）；census_quotes 0 defective；D18 刊头间距 38.2px（>0）；D37 副刊头余量 16.9px（>0）。
- 非门禁残留（D21/D22/D27 口径，仅记录）：15b carryover（4x 'español'、4x 'der'）；按 D21/D22/D27 口径以 15a + native verifier ADOPT 验收。15c native verifier ADOPT（0 UNEXPECTED）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-de/logs/2026-w46-de-es/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `07ec8e29b5e7977562f53e610297a9c408beb1523bdfe4e3fab4836001054194`（2,986,957 B）；新网 PDF `656d08c4002f653810c390f0edf7d5d7fe4005793aad01ebe52a166ac76a33c5`（933,590 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `7f7ca7708c5a…` |
| p2-leben.svg | `7d83c58c9d8e…` |
| p3-kultur.svg | `543d33a114da…` |
| p4-sport.svg | `8bafbfc17bff…` |
| p5-jugend.svg | `64487af8afb7…` |
| p6-vertiefung.svg | `4fd36468353f…` |
| p7-sprache.svg | `8b092f1b0197…` |
| p8-uebungen.svg | `d17620dabd5f…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（49,309 B，SHA `e8b1f51acfd7ddefbc3d7e2a4179fdb3dd538df59f855122421b52f3f9b02266`）。
- KIT：`patched/2026-w46-de-es/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录；版内 SVG 针脚旧表已随 D5 重排过期，新值见上表）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。

