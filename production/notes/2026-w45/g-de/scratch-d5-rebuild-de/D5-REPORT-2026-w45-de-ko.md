# D5 重建报告 — 2026-w45-de-ko（韩语读者版）

W45 de 家 D5-only 重建（新样式 + D1 已在仓；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-14；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-de/logs/2026-w45-de-ko/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W45-DE-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core de --week 2026-w45 --i-understand-this-writes-production`（PLAN 授权）→ 只改 `production/2026-w45/core-de/svglib.py`（`_D5_READER = 'latin'` + fix2 + D5 块）。
- 本版安装：`apply_variant.py --svglib <版>/svglib.py --target de --reader ko --week 2026-w45`（先 `--check` dry-run 通过）。装后 `_D5_READER = 'cjk'`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。CJK 读者版按字符文字分流，不加 `_READER_LANG` 门，`--reader ko`（mode=cjk）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `hidden_files/style-port-de/export_de_w45.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5 拉丁 451、西里尔 0、弯引号 CJK 0；花括号总量 43，全在 Newsreader 内、0 在 CJK 内。
- 基线实测：印 PDF `114d8eca08f15e42979251cfa1d6b2ca19081593558c243ad4219df6fd7fd306`（7,303,065 B）；网 PDF `1c03e12c4e58c5d44280018482e8c71a477de1cc29175d63e2bc851310ee7be4`（1,303,325 B）。my-web vs 已发 web PDF 文字层字符多重集差 0/0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（50,947 B）。KIT 印/网 SHA 针脚已过期（已知 KIT SHA 滞后），基线以文字层/export 证据为准，不以 KIT SHA 为准。

## 三、缺陷与修复（run 1 → 二次修复）

- run 1 门禁：盒标题 3（보기 +21.6、목차 +9.0、상자 +21.7）；其余门全绿。
- 二次修复（只动字号，文字零改动；探针 `scripts/probe_titles.py` / `scripts/probe_ru_it_ja.py` 量测在案，`scripts/apply_fixes_r1.py` 47 处全落位、0 失败；盒标题内宽 400.5 / f.box 404.5，留 ≥2px 余量）：盒标题 3 处：content12.py:43 f.box tsize 23→21（보기；22pt 仍越栏）、content12.py:89 24→23（목차）、content7.py:72 23→21（상자）。
- P8：行数 211→203，距页脚线余量 40.3→40.3 px（y=2596 线、页底 2700）；p8 compare CLEAN（keydiff [137, 138, 139, 150]，预期读者键）。

## 四、门禁（run2，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1,179,830 B <7MB）；occlusion 0（含自检，6 类全触发）；p8 extract 150/150；p8 compare CLEAN；freeze 基线 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0（p8 +1536 strings / -140 strings）；spill 0（32 boxes, 156 candidates, 0 SPILL）；boxtitle 0（74 titles, 496 body lines, 0 DEFECT）；edge 0 TOUCH 0 NEAR；creambox PASS 0 缺陷（ratios n=520）；文字层 print=web 多重集差 0（print=34044 web=34044）；census_quotes 0 defective；D18 刊头间距 211.0px（>0）。
- 非门禁残留（均已定位，字符相同，不阻塞）：15b carryover rc=1（SVG-only/MD-only 21/934 tokens；SVG-only 全为裸数字，MD-only 全为 instruction/gloss 层词，零内容词差；基线同样 FAIL）；15d exact rc=1（A-only/B-only 17/27 tokens；A 侧为 `a2→b1`/`a2→b2` 等合串，B 侧为其断 run 拆分件，字符相同；基线同样 FAIL）。按 D21/D22/D27 口径以 15a + native verifier ADOPT（rc=0）验收。15b/15d 残差已逐条列出，见家族报告 §5.1。
- 日志：`hidden_files/d5-redo/scratch-2026-w45-de/logs/2026-w45-de-ko/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `6f85afe243358720cf74697fc4e517c0b281088c3e3b512fb410c9550158e2fa`（4,336,063 B）；新网 PDF `31278b6554d64bc32d2af0ca8d43f49c5f5e399fc4c148da4640efa22c7ae560`（1,179,830 B，<7MB）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder run2 原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `d9631b44ff17…` |
| p2-leben.svg | `931a27f2cbd4…` |
| p3-kultur.svg | `7f3124d7a420…` |
| p4-sport.svg | `d0e02f7bb2f4…` |
| p5-jugend.svg | `722970bfecfe…` |
| p6-vertiefung.svg | `9fa6e424b3c5…` |
| p7-sprache.svg | `c4a8d878c09a…` |
| p8-uebungen.svg | `6db103da8a7c…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（50,947 B）。
- KIT：`production/2026-w45/2026-w45-de-ko/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录；版内 SVG 针脚旧表已随 D5 重排过期，新值见上表）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
