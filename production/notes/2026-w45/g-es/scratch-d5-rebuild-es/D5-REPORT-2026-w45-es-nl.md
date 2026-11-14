# D5 重建报告 — 2026-w45-es-nl（荷兰语读者版）

W45 es 家 D5 + §1.1 合并重建（pre-D1 新样式：port 已入仓，D1 未应用——D1 修复 + D5 一次渲完）。施工 2026-11-14；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-es/logs/2026-w45-es-nl/`（`GATES-SUMMARY-run2b.txt` 为门禁总表，复本见 `production/notes/2026-w45/g-es/scratch-d5-rebuild-es/logs/2026-w45-es-nl/GATES-SUMMARY.txt`，D29，cmp 已核）。家族报告：`hidden_files/d5-redo/FAMILY-W45-ES-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core es --week 2026-w45 --i-understand-this-writes-production`（PLAN 授权）→ 只改 `production/2026-w45/core-es/svglib.py`（+95/−3 行，`_D5_READER = "latin"` 常驻，D24：patched zh-cn 同步为 `"cjk"`，不特殊处理）。
- D1 施工法（pre-D1 前例，FAMILY-W43-FR-BUILD.md）：D1 修复 = 规范 §2a 补丁，`svglib.py` 单 hunk（28 行 diff），只改发射、不动 `wrap()`、不重排。来源 `hidden_files/style-port-es/fanout-2026-w45/<reader>/svglib.py`（11/11 各含恰 1 处 `# D1 fix` 标记；生产 svglib 0/11）。装配前核实：每版 fanout svglib vs 生产 svglib diff 恰 28 行；`content*.py`/`bslib4.py` 逐字节同；`run.py` 全家同；`render.py` 仅 core 有文件名差。装配脚本 `scripts/assemble_d1.sh`（日志 `logs/d1-assembly.txt`），11/11 diff 恰 28 行、标记各 1，余文件逐字节同。
- 本版安装：`apply_variant.py`（`--check` dry-run 先行，通过后安装）。装后 `_D5_READER = "latin"`（svglib.py L100）。fix2 保留（U+201C 1 处，`_QUOTE_CLS` 4 处）。路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`（依次，不跳步）；text.md 由已核实导出器重出（见 §二导出器注记）。

## 二、基线（修前，全部干净才装机）

- 导出器核实（第 0 步）：任务简报所指 `scratch-prep-p3b/export_w45_fanout_fixed.py` 实为 **fr 家**导出器（解析 `2026-w45-fr-` 前缀、重建 fr 刊头），不能用于 es 版（见家族报告 §0/§8 的导出器更正）。本家实测导出器为 SVG 路由 `hidden_files/style-port-es/textexp_es.py`（D16 已修：`kind_of` 将 `"Noto Sans"` 映为 `sans`）。试跑 vs `issues/` 已发 `.text.md`：**11/11 BYTE-IDENTICAL**（本版亦同）。
- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。印/网 PDF 与 `issues/` 已发 web PDF 文字层字符多重集差 0；p8 extract 150/150；boxtitle 基线对照见 §三。
- 修前普查 `d5_census.py`：502 (lat 502 / cyr 0 / curly-in-CJK 0)（总量 >0，符合 D5 重建前提）。
- 基线实测：印 PDF `8a8058ccf0940b5d…`（D1-fixed ref 6589213 B；本次基线重建 6,589,171 B，Δ -42 B，工具链版本差）；网 PDF（本次基线重建，当前 `tools/webpdf.py`）654,311 B（D1-fixed ref 617573 B；差值系当前 webpdf 另嵌 Newsreader-Bold/Italic 子集，文字层无差）。text.md vs `issues/` 已发版 **BYTE-IDENTICAL**（47,106 B）。
- D18 基线：刊头标语/日期 SVG 间距全家 >0（nl 84.7px、pt 83.1px 为最小两档；余见家族报告 §8）。nl/pt 的 run1 缺陷（−4.7/−5.2px）为 D5 变宽所致，见 §三；run2 值见 §四。
- 基线 p8：extract 150/150；compare vs 基线 core **CLEAN，keydiff [137, 138]**（zh-cn 为 core 本身，keydiff []）。

## 三、缺陷与修复（run1 → 二次修复）

run1 门禁红项（其余门全绿）：

- G6 occlusion 1 flag（P1 刊头与右带 NOG 27 DAGEN 重叠 7.1×20.8px）
- G12 boxtitle 3 DEFECT（P1 In cijfers +6.5；P1 In dit nummer +21.7；P4 +51.5）
- G14 creambox FAIL 3 defects
- D18 刊头标语/日期间距 -4.7px（真缺陷，≤0）
- G15c native verifier HOLD（标语末 run 与日期行在 text.md 中粘连为 LEZENSEMANA，与 D18 同因）

二次修复（只动字号与断行，不动文字内容；探针 `scripts/probe_fixes.py` 以本版 svglib `text_w` 实测、10px 余量目标逐处算出新字号，`scripts/apply_fixes_run2.py` 42 处全家落位、断言全中；行号按 D19——f.box 的 tsize 以 close 行为准）：

- `content12.py:15`：P1 masthead slogan 17 -> 16 (D18 gap run1 -4.7px -> run2 +17.7px; also un-merged the slogan/date lines in text.md, G15c HOLD -> ADOPT)
- `content12.py:25`：P1 headline “¡LA VIVIENDA DECIDE LA CAMPAÑA!” 46 -> 45 (run1 TEXTX overlap 7.1px; run2 margin 12.8px)
- `content12.py:48`：f.box title “LA SEMANA EN CIFRAS　In cijfers” tsize 23 -> 22 (run1 over +6.5px; run2 margin 11.5px)
- `content12.py:91`：P1 contents box title “EN ESTA EDICIÓN　In dit nummer” 24 -> 22 (run1 over +21.7px; run2 margin 13.5px)
- `content34.py:127`：P4 box title “EL CLÁSICO, UNA SEMANA DESPUÉS” 23 -> 19.5 (run1 over +51.5px, was +2.5px; run2 margin 17.3px)

- P8：行数 239 -> 239（run1 → run2，未变），距页脚线余量 47.7px（y=2596 线、页底 2700，正余量、无溢出）。
- 修完重渲 + 全套门禁重跑（tag run2b），见 §四。

## 四、门禁（fix，ALL-GREEN 除 15a/15c 两处预期 F1 差；run2b 原值见 §七）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（573,954 B <7MB，run2b 为 573,966 B）；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150；p8 compare CLEAN，keydiff [137, 138]；freeze 基线 8/8；G10 freeze_diff_vs_base: p8: +83 strings / -33 strings（run2b 为 +82 / -32，恰为改动的一串）；CJK core 15 -> edition 15; added CJK chars: 0 ; added Latin strings: 40 (unexpected 40) TOTAL added CJK characters: 1 TOTAL added Latin strings: 273 (unexpected 273) ；G11 spill: SPILL_SWEEP 2026-w45-es-nl: 30 boxes, 82 candidates, 2 SPILL, 80 OBSERVE；G12 boxtitle: BOXTITLE 2026-w45-es-nl: 29 titles, 276 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal；edge 0 TOUCH 0 NEAR；G14 creambox: P8 p8-ejercicios.svg: lines 239->239 slack_footer 47.7->47.7 CREAMBOX PASS 0 defects ；G15a textlayer: print=35990 web=35990 issued=35988 diff_pw=0 diff_pi=18（18 恰为一词字符多重集差，见 §七）；text.md DIFF 114 lines（110 行重排断行差与 run2b 相同 + 4 行 F1 hunk），原生校验器 HOLD（2 UNEXPECTED，均为 E144a 一词之差，见 §七）；census_quotes 0 defective；G17 N/A（es 无家族 gates.py）；D18 masthead: 2026-w45-es-nl: SVG gap=17.7px (slogan_x=558.0 date_x=1409.7) model_gap=20.7px (slogan_w=874.1 date_w=452.3) PASS；D37 submasthead: 2026-w45-es-nl: y=372 line_end_x=1413.0 box_top=588 N/A (line above box top, no overlap possible) (3 runs, 16pt bold=False) :: TEKSTEN IN HET SPAANS　UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERL。
- 残留（均已定位，不阻塞）：
  - G10 新增 CJK 1：P6 U+3000 ×1——重排 run 拆分件（patch P6  lone-U+3000 run 10 处 vs 基线 0 处，字符净 +1；P8 词元多重集核对仅见同串拆分，无内容增删）。11 版同征，见家族报告 §8。
  - G11 2 SPILL：冻结核心原有，与已发基线逐字同位（P1 末项 `5)` +10.40px、y=2300.4；P7 读者栏末行 +11.98px、y=1830.6），非 D5 引入；提请重校裁定，见家族报告 §8。
  - G12 0 marginal。
  - G15c run1 曾 HOLD（nl/pt 标语粘连，见 §三），run2 已 ADOPT。
- 日志：`hidden_files/d5-redo/scratch-2026-w45-es/fix/logs/2026-w45-es-nl/GATES-SUMMARY-fix.txt`（复本已进 production/notes，cmp 核实逐字节同；run2b 表归档于 `fix/logs/run2-summaries/`）。

## 五、新交付物与 KIT

- 新印 PDF `La-Lucerna-VOL2-es-nl.pdf`：`3d621b1c22e45ec090941f7de6af9f0b75a0e298075f5893fdd102cab3cca252`（6,028,566 B，F1 fix；run2b 为 `31f7659d…` / 6,028,562 B）；新网 PDF `2026-w45-es-nl.web.pdf`：`fd946c15b3bde860bde46a42ff8fd24822f87fefe4dbb93c79b3b9ddfb7ad8b4`（573,954 B，<7MB，F1 fix；run2b 为 `416f133b…` / 573,966 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web=issued 差 0，fix 后 diff_pi=18 恰为 F1 一词之差，见 §七）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 fix 原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2b，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-portada | `d17c1c7bc916…` |
| p2-vida | `78652b816485…` |
| p3-cultura | `9baad297a980…` |
| p4-deporte | `cc2af253de0f…` |
| p5-juventud | `e120e56cbf14…` |
| p6-afondo | `2e050c66e8bb…` |
| p7-lengua | `8b03be2fc3eb…` |
| p8-ejercicios | `71dc415ee6da…`（F1 fix；run2b 为 `89551a8ffd39…`） |

- text.md：D5 不改文字内容，F1 fix 改一词；交付件为已核实导出器（`textexp_es.py`，D16 已修）重出，vs `issues/` 已发 `.text.md` DIFF 114 lines（110 行重排断行差与 run2b 相同 + 4 行 F1 hunk），原生校验器 HOLD（2 UNEXPECTED，均为 E144a 一词之差，见 §七；其余各节词元相同、练习序列相等）。新 text.md 47,107 B，SHA-256 `e9e218d164623423a143148bfe5185b5ba643525370b4f940ab4918bce00a9c1`。
- KIT：`patched/2026-w45-es-nl/WEEKLY-KIT.md`（patched 侧 custody，见家族报告 §8；closer 同步进 production；交付物针脚行已更新为 run2b 实测值 + 末节 `## D5 rebuild (2026-11-14)`；版内 SVG 针脚表与历史修复轮记录未动，范围外）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。

## 七、F1 fix（2026-11-14，独立重校 F1 的修复）

独立重校报告 `FAMILY-W45-ES-REPROOF.md` §11 verdict NOT PASSED，唯一 finding F1：
nl P8 E144a 把 `junta electoral` 释为 `het stembureau`（投票站），其余 10 版均为
"选举委员会"（de `Wahlkommission`、en `the electoral board`、fr `la commission
électorale`、it `commissione elettorale`、ja/ko `選挙管理委員会`、pt `comissão
eleitoral`、ru `избирательная комиссия`、zh-cn `选举委员会`、zh-tw `選舉委員會`）。
答案字母 a 正确，仅荷兰语释义错。

- 基线核实（先存缺陷，非 D5 回归）：`het stembureau` 在 production、patched、
  baseline 三处 `content8.py:85` 均有；已发 `issues/.../2026-w45-es-nl.text.md`
  L3102 亦有（`144. a — junta electoral = het stembureau — a`）。
- 修法（仅一词，不动句式与余词）：`content8.py:85`
  `junta electoral = het stembureau — a` → `junta electoral = de kiescommissie — a`；
  `py_compile` 通过。修法同时落在 production、patched、fix 三处，三方 `diff -q`
  一致（fix 报告 §6），防 closer 同步以旧 patched 覆盖。
- 重导出（`textexp_es.py`，D16 已修；fr 家导出器未用）：新 text.md vs run2b 导出
  恰好 1 行不同（E144a，L3100）；vs 已发版 114 行 = run2b 的 110 行重排断行差
  （逐 hunk 相同）+ 4 行 F1 hunk。
- 重渲（tag fix，`fc-cache -f` 已暖）：run rc=0、render rc=0、webpdf rc=0、
  textexp rc=0，TOTAL 150。P8 行数 239→239，slack_footer 47.7px 不变；P8 全页
  目检新释义完整入框、无溢出（`fix/work/pages/nl-p8-fix-8.png` 及 144 行放大图）。
- 门禁（tag fix，16 门 + D18 + D37 全量重跑）：除以下两处预期 F1 差外全绿——
  G15a text.md DIFF 114 行（110 重排 + F1 hunk）；G15a 文字层 print=35990
  web=35990 issued=35988，diff_pw=0，diff_pi=18（`het stembureau`→`de
  kiescommissie` 字符多重集差恰为 18）；G15c 原生校验器 HOLD（rc=1，2 UNEXPECTED
  块，均为 E144a 词元/行之差；其余 7 节词元相同，练习序列相等，REWRAP 28 与
  run2b 同值）。G10 p8 +83/−33（run2b +82/−32，恰为改动的一串）。其余门与 run2b
  逐字段相同（G1 150/0、G2 PASS、G3 0/0/0、G6 0 flags、G7 150/150、G8 CLEAN
  [137, 138]、G9 8/8、G11 2 SPILL、G12 0/0/0、G13 0/0、G14 PASS、G16 0、G17 N/A、
  D18 17.7px PASS、D37 N/A）。
- 新交付物（fix 原件；closer 须拷 fix 原件，绝不重跑 webpdf）：
  - 印 PDF `La-Lucerna-VOL2-es-nl.pdf`：6,028,566 B，SHA-256 `3d621b1c22e45ec090941f7de6af9f0b75a0e298075f5893fdd102cab3cca252`
  - 网 PDF `2026-w45-es-nl.web.pdf`：573,954 B，SHA-256 `fd946c15b3bde860bde46a42ff8fd24822f87fefe4dbb93c79b3b9ddfb7ad8b4`
  - text.md：47,107 B，SHA-256 `e9e218d164623423a143148bfe5185b5ba643525370b4f940ab4918bce00a9c1`
  - 仅 p8 SVG 变：`p8-ejercicios` SHA-256 `71dc415ee6daa979fdbefd585c38288d426e7806c6bcc10fa9c798f85062faca`；p1–p7 与 run2b 逐字节同。
- 其余 10 版未动：其 patched 印 PDF 字节 + SHA-256 与 builder §9 值逐字节一致（已核）。
- KIT 已同步：patched KIT 针脚行 + 交付物行更新为 fix 值，末尾追加 `## F1 fix (2026-11-14)`。
- 待独立重校 v2（F1 已修，余版已由本次重校确认）。
