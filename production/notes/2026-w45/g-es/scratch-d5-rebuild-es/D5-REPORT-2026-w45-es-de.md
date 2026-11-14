# D5 重建报告 — 2026-w45-es-de（德语读者版）

W45 es 家 D5 + §1.1 合并重建（pre-D1 新样式：port 已入仓，D1 未应用——D1 修复 + D5 一次渲完）。施工 2026-11-14；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-es/logs/2026-w45-es-de/`（`GATES-SUMMARY-run2.txt` 为门禁总表，复本见 `production/notes/2026-w45/g-es/scratch-d5-rebuild-es/logs/2026-w45-es-de/GATES-SUMMARY.txt`，D29，cmp 已核）。家族报告：`hidden_files/d5-redo/FAMILY-W45-ES-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core es --week 2026-w45 --i-understand-this-writes-production`（PLAN 授权）→ 只改 `production/2026-w45/core-es/svglib.py`（+95/−3 行，`_D5_READER = "latin"` 常驻，D24：patched zh-cn 同步为 `"cjk"`，不特殊处理）。
- D1 施工法（pre-D1 前例，FAMILY-W43-FR-BUILD.md）：D1 修复 = 规范 §2a 补丁，`svglib.py` 单 hunk（28 行 diff），只改发射、不动 `wrap()`、不重排。来源 `hidden_files/style-port-es/fanout-2026-w45/<reader>/svglib.py`（11/11 各含恰 1 处 `# D1 fix` 标记；生产 svglib 0/11）。装配前核实：每版 fanout svglib vs 生产 svglib diff 恰 28 行；`content*.py`/`bslib4.py` 逐字节同；`run.py` 全家同；`render.py` 仅 core 有文件名差。装配脚本 `scripts/assemble_d1.sh`（日志 `logs/d1-assembly.txt`），11/11 diff 恰 28 行、标记各 1，余文件逐字节同。
- 本版安装：`apply_variant.py`（`--check` dry-run 先行，通过后安装）。装后 `_D5_READER = "latin"`（svglib.py L100）。fix2 保留（U+201C 1 处，`_QUOTE_CLS` 4 处）。路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`（依次，不跳步）；text.md 由已核实导出器重出（见 §二导出器注记）。

## 二、基线（修前，全部干净才装机）

- 导出器核实（第 0 步）：任务简报所指 `scratch-prep-p3b/export_w45_fanout_fixed.py` 实为 **fr 家**导出器（解析 `2026-w45-fr-` 前缀、重建 fr 刊头），不能用于 es 版（见家族报告 §0/§8 的导出器更正）。本家实测导出器为 SVG 路由 `hidden_files/style-port-es/textexp_es.py`（D16 已修：`kind_of` 将 `"Noto Sans"` 映为 `sans`）。试跑 vs `issues/` 已发 `.text.md`：**11/11 BYTE-IDENTICAL**（本版亦同）。
- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。印/网 PDF 与 `issues/` 已发 web PDF 文字层字符多重集差 0；p8 extract 150/150；boxtitle 基线对照见 §三。
- 修前普查 `d5_census.py`：497 (lat 496 / cyr 0 / curly-in-CJK 1)（总量 >0，符合 D5 重建前提）。
- 基线实测：印 PDF `b35489fec2c4b4b0…`（D1-fixed ref 6588308 B；本次基线重建 6,588,267 B，Δ -41 B，工具链版本差）；网 PDF（本次基线重建，当前 `tools/webpdf.py`）655,190 B（D1-fixed ref 618000 B；差值系当前 webpdf 另嵌 Newsreader-Bold/Italic 子集，文字层无差）。text.md vs `issues/` 已发版 **BYTE-IDENTICAL**（46,532 B）。
- D18 基线：刊头标语/日期 SVG 间距全家 >0（nl 84.7px、pt 83.1px 为最小两档；余见家族报告 §8）。nl/pt 的 run1 缺陷（−4.7/−5.2px）为 D5 变宽所致，见 §三；run2 值见 §四。
- 基线 p8：extract 150/150；compare vs 基线 core **CLEAN，keydiff [137, 138]**（zh-cn 为 core 本身，keydiff []）。

## 三、缺陷与修复（run1 → 二次修复）

run1 门禁红项（其余门全绿）：

- G6 occlusion 1 flag（P1 刊头与右带 NOCH 27 TAGE 重叠 102.2×20.8px）
- G12 boxtitle 5 DEFECT（P1 ZAHLEN +13.5；P4 +51.5；P5 DEIN PLAN +28.0；P7 TYPISCHE FEHLER +20.3；P7 WORT DER WOCHE +19.5）
- G14 creambox FAIL 5 defects

二次修复（只动字号与断行，不动文字内容；探针 `scripts/probe_fixes.py` 以本版 svglib `text_w` 实测、10px 余量目标逐处算出新字号，`scripts/apply_fixes_run2.py` 42 处全家落位、断言全中；行号按 D19——f.box 的 tsize 以 close 行为准）：

- `content12.py:26`：P1 headline “¡LA VIVIENDA DECIDE LA CAMPAÑA!” 46 -> 40 (run1 TEXTX overlap 102.2px vs right-band text; run2 margin 16.8px)
- `content12.py:49`：f.box title “LA SEMANA EN CIFRAS　ZAHLEN” tsize 23 -> 21.5 (run1 over +13.5px; run2 margin 13.8px)
- `content34.py:127`：P4 box title “EL CLÁSICO, UNA SEMANA DESPUÉS” 23 -> 19.5 (run1 over +51.5px, was +2.5px; run2 margin 17.3px)
- `content56.py:27`：f.box title “EL PLAN DEL PUENTE　DEIN PLAN” tsize 23 -> 20.5 (run1 over +28.0px; run2 margin 19.0px)
- `content7.py:79`：P7 clinic box title “ERRORES TÍPICOS　TYPISCHE FEHLER” 20 -> 18.5 (run1 over +20.3px; run2 margin 11.4px)
- `content7.py:90`：P7 word box title “LA PALABRA　WORT DER WOCHE” 23 -> 21 (run1 over +19.5px; run2 margin 17.0px)

- P8：行数 243 -> 243（run1 → run2，未变），距页脚线余量 41.7px（y=2596 线、页底 2700，正余量、无溢出）。
- 修完重渲 + 全套门禁重跑（tag run2），见 §四。

## 四、门禁（run2，ALL-GREEN，残留见下）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（575,311 B <7MB）；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150；p8 compare CLEAN，keydiff [137, 138]；freeze 基线 8/8；G10 freeze_diff_vs_base: p8: +84 strings / -33 strings; CJK core 15 -> edition 15; added CJK chars: 0 ; added Latin strings: 40 (unexpected 40) TOTAL added CJK characters: 1 TOTAL added Latin strings: 268 (unexpected 268) ；G11 spill: SPILL_SWEEP 2026-w45-es-de: 30 boxes, 81 candidates, 2 SPILL, 79 OBSERVE；G12 boxtitle: BOXTITLE 2026-w45-es-de: 21 titles, 281 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal；edge 0 TOUCH 0 NEAR；G14 creambox: P8 p8-ejercicios.svg: lines 243->243 slack_footer 41.7->41.7 CREAMBOX PASS 0 defects ；G15a textlayer: print=35656 web=35656 issued=35656 diff_pw=0 diff_pi=0；text.md DIFF 94 lines（重排断行差，非内容差），原生校验器 ADOPT（0 UNEXPECTED）；census_quotes 0 defective；G17 N/A（es 无家族 gates.py）；D18 masthead: 2026-w45-es-de: SVG gap=32.9px (slogan_x=573.2 date_x=1409.7) model_gap=34.8px (slogan_w=845.8 date_w=452.3) PASS；D37 submasthead: 2026-w45-es-de: y=614 line_end_x=1379.2 box_left=1439.5 margin=60.3px (3 runs, 16pt bold=False) PASS :: SPANISCHER TEXT　DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIG。
- 残留（均已定位，不阻塞）：
  - G10 新增 CJK 1：P6 U+3000 ×1——重排 run 拆分件（patch P6  lone-U+3000 run 10 处 vs 基线 0 处，字符净 +1；P8 词元多重集核对仅见同串拆分，无内容增删）。11 版同征，见家族报告 §8。
  - G11 2 SPILL：冻结核心原有，与已发基线逐字同位（P1 末项 `5)` +10.40px、y=2300.4；P7 读者栏末行 +11.98px、y=1830.6），非 D5 引入；提请重校裁定，见家族报告 §8。
  - G12 1 marginal（工具计数，未具名；run1 同值）。
  - 
- 日志：`hidden_files/d5-redo/scratch-2026-w45-es/logs/2026-w45-es-de/GATES-SUMMARY-run2.txt`（复本已进 production/notes，cmp 核实逐字节同）。

## 五、新交付物与 KIT

- 新印 PDF `La-Lucerna-VOL2-es-de.pdf`：`d48078e257ac4b1aea1ec828fc6ec9854a0a3256013be3088fd4c9ebf44da9e6`（6,029,858 B）；新网 PDF `2026-w45-es-de.web.pdf`：`eb5b77c1256d33317c143078aca72a6ea5276a8b2d80b4c71aa081b322371aec`（575,311 B，<7MB）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web=issued 差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder run2 原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run2，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-portada | `a0aac9eb1c93…` |
| p2-vida | `3a713d857b66…` |
| p3-cultura | `bbc08648e16b…` |
| p4-deporte | `40c5e2712ad5…` |
| p5-juventud | `389cc35e9867…` |
| p6-afondo | `50cbff710790…` |
| p7-lengua | `3e6a3fc0c351…` |
| p8-ejercicios | `3c2c322afb78…` |

- text.md：D5 不改文字内容；交付件为已核实导出器（`textexp_es.py`，D16 已修）重出，vs `issues/` 已发 `.text.md` DIFF 94 lines（全为重排断行差），原生校验器 ADOPT（exercise 序列 + 每页词元多重集相等，0 UNEXPECTED）。
- KIT：`patched/2026-w45-es-de/WEEKLY-KIT.md`（patched 侧 custody，见家族报告 §8；closer 同步进 production；交付物针脚行已更新为 run2 实测值 + 末节 `## D5 rebuild (2026-11-14)`；版内 SVG 针脚表与历史修复轮记录未动，范围外）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。
