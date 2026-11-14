# D5 重建报告 — 2026-w43-de-ko（ko 读者版）

W43 de 家 D5+§1.1 合并重建（SOP §1.1 新样式：Newsreader/Noto Serif 字体修复；D5 缺陷：sans 层拉丁/西里尔字符落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者））。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-de/logs/2026-w43-de-ko/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W43-DE-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：先把 port 版 `w43/core/svglib.py` 拷入 `production/2026-w43/core-de/svglib.py`（port 器拒绝旧式 svglib，D5-METHOD §1.7 移植模板路线），再 `apply_variant.py --patch-core de --week 2026-w43 --i-understand-this-writes-production` → 落盘 `_D5_READER = "latin"` + fix2 + D5 sans 块。
- 本版安装：`apply_variant.py --svglib <版>/svglib.py --target de --reader ko --week 2026-w43`（先 `--check` dry-run 通过）。装后 `_D5_READER = "cjk"`。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 33 个全在 Newsreader。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由 `hidden_files/style-port-de/export_de_w43.py`（SVG 路线导出器，试跑与 port `.text.md.new` BYTE-IDENTICAL）重出，交付件为 port `.text.md.new` 原样沿用（见第五节）。

## 二、基线（修前 §1.1 组装版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；重建 SVG 8/8 与 port fanout 逐字节相同；印 PDF 与 fanout BYTE-IDENTICAL；印/网 PDF 文本层字符多重集差 0；导出与 port `.text.md.new` BYTE-IDENTICAL。
- 修前普查 `d5_census.py`：D5 拉丁 **461**、西里尔 **0**、弯引号在 CJK **0**（拉丁/西里尔 >0，符合装机前提；弯引号 33 个全在 Newsreader）。
- 基线实测（§1.1 组装版，fanout 实测）：印 PDF `049e5d848d8032185662a5a438688caca83eb516d0859ea6cbe239c3839c1604`（14515279 B）、网 PDF `e91aaf89ce549c1a06a08c983c9b845e01769d8e4e85454abeca76cb62e11959`（1843719 B）。KIT 旧值（更旧配方）已过期，以上值为准。
- 注：本家 `issues/` 无已发 `.text.md`（0 个），基线以 port fanout 为准；已发网 PDF（`issues/2026-w43-de-ko/2026-w43-de-ko.pdf`，1941886 B，`32c4c971e3f56eae…`）与本版重建网 PDF 的文本层差仅为 port 家具（`·`→U+3000 等）与断行 token 化，mine-only 词 0，`verify_de_w43.py` 判 ADOPT（0 UNEXPECTED）。

## 三、缺陷与修复（run 1 → 二次修复）

- run 1 门禁：head_check 1 缺陷（P1 herbst 头）；occlusion 2 flags（35.0+38.0）；spill 3；boxtitle 3（보기 +21.6、목차 +9.0、상자 +21.7）；edge 0/0；creambox 3；刊头间距 205.5px（首次读数 -261.4 为量具误读，见家族报告 §5 注）；--exact 残留 b2。
- 二次修复（只动字号与断行，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 两 p.text 标题内宽 400.5；D5 fix 行注释已入源码）：
  1. `content12.py:25` P1 band 标题 36→31pt（与最紧 band-right 左界 ru 1542.0 间隙 76.7px）。
  2. `content12.py:124` herbst 头 25→22pt（框宽 422.5；25pt 430.2 超 7.7px，22pt 378.6）。
  3. `content12.py:47` numbers 盒 `f.box` 加 tsize=21（最差 +25.8；21pt 最大 392.8 < 404.5）。
  4. `content12.py:89` contents `IN DIESER AUSGABE` 24→22pt（最差 +9.0）。
  5. `content12.py:175` merksatz 盒 `f.box` 加 tsize=21（最差 +25.5；21pt 最大 392.5 < 404.5）。
  6. `content34.py:35` / `content56.py:34` P3/P5 facts 盒 +14→+34（末行溢出约 12.7px；en 家先例）。
  7. `content56.py:56` P5 Saturday-plan 头 24→22pt（nl +55.3；22pt 829.3 < 849.4）。
  8. `content56.py:155` P6 timeline 头 24→22pt（pt +10.3；22pt 376.1 < 400.5）。
  9. `content7.py:72` Toolbox 23→21pt（最差 +23.0；21pt 最大 386.4 < 400.5；22pt en 404.7 仍超）。
  10. `content7.py:92` NOCH EIN WORT 22→21pt（最差 +11.6；21pt 393.0 < 400.5）。
  11. `content8.py:74` P8 D 组头 24→22pt（it 428.3、nl 431.5 均超 422.5；22pt 最大 395.6）。

- P2 例外（run2 全量重渲后 en 门禁发现）：P2 facts 盒 +20 下推「Und Sie?」盒底至 1568.75，压过 `dy=1566` 习题分隔线（1554），线切其末行 `sentences in German!`。P2 栏顶已满（基线盒底 1548.75，距线仅 5.25px），无加高空间。run2b：11 版 P2 facts 盒改回 +14（高度不变，下方不动）；facts 正文 21.5→21pt（实测 wrap 8→7 行，末行基线偏移 368.7→333.9，盒底 356，余 22.1px）。P3/P5 保持 +34（下方有空间，run2 已验 spill 0）。
- P8：行数 205→212，距页脚线余量 38.9px（y=2596，页底 2700）；p8 compare CLEAN（keydiff [137, 138, 150]，预期读者键）。

## 四、门禁（run2b，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0（弯引号总数 33，全在 Newsreader）；render RC=0；webpdf RC=0（1708955 B <7MB）；occlusion 0（含自检，6 类全触发）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=526，中位 1.007）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A；D18 刊头间距 205.5px（>0）。
- 非门禁残留（均已定位，字符相同，不阻塞）：carry-over verify RC=2（无读者表（no table），基线固有，未校准）；`--exact` FAIL（A-only 8 tokens，B-only 15 tokens；A 侧如 a2→b1, a2→b2, - 等，均为 token 拆分，字符相同；详见 `verify-exact.log`）。
- 日志：`hidden_files/d5-redo/scratch-2026-w43-de/logs/2026-w43-de-ko/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `5cce0b2643f81d654780fffae672772ddc546093a98349d8e9ea13184819f83c`（11312599 B）；新网 PDF `d7c993f022ef4eb1ea00d7c18f9f407cdd647f7ddb85c18dd20d298341921008`（1708955 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。注：网 PDF 非确定性——同源重建可差 1 字节，KIT 以最终实测值为准。
- text.md：D5 不改文字内容；交付件为 port `.text.md.new` 原样沿用（BYTE-IDENTICAL，50743 B，sha256 `ef976372d5ffa5928439baa26f376b53802817afac0e4a26838928231a3d901b`，570 条目 / 150 习题）；重建后重出 token-identical（rewrap RC=0）。
- KIT：`production/2026-w43/2026-w43-de-ko/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 末节 D5 记录）。production 源码同步待 closer（见家族报告 §7；本版为 §1.1 port + D5，非 D5-only，故不走 es 式部分回拷）。
