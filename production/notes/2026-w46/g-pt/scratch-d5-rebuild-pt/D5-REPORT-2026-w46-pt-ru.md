# D5 报告 — 2026-W46 pt × 俄语（`2026-w46-pt-ru`）

- 刊期：2026-W46（VOL.3）；目标语 pt；读者 俄语。
- 性质：D5-only 重建（§1.1 已在 style-port 落仓，基线即新样式）；只降字号，不改内容。

## 一、装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target pt --reader ru --week 2026-w46`（先 `--check` 干跑，全干净）。
- 模式 ru；`_D5_READER = "ru"`（`svglib.py:100`）；`test_d5_routing.py` **FAILURES: 0**；fix2 保留（`_QUOTE_CLS` ×4）。未跑 `--patch-core`（D40）。

## 二、基线

- run TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0（core-pt 例外：印/网差 365 字，为模板与读者版家具差，见家族报告 §6）；`issues/` pin（pdfBytes/pdfSha256）与文件一致；text.md 与 `issues/` BYTE-IDENTICAL（carry-over）；p8 extract 150/150。
- 基线印/网字节：2683612 / 885792；文字层字符 33962；D5 普查：Latin 356、Cyrillic 255、curly_in_cjk 0；D1=1、`_D5_READER`=0、Newsreader 9 行。

## 三、run1 缺陷与修法

- run1 FAIL verdict：无（run1 即 18/18 全绿）。
- 修复（0 处，只降字号；探针：SVG 实测墨宽线性缩放、取留 ≥2px 余量的最大适配字号）：
- 无修复。
- 全部修复行 `ast.parse` 通过；`f.box` 修复引用 `tsize=` 所在收尾行（D19）。

## 四、终轮门禁 run2

- 计分门 18/18 全绿（G1–G14 + G15a + G16 + D18 + D37；G15b 仅记录，G15c N/A）。
- G1 run PASS TOTAL=150 OVF=0 HDW=0
- G2 head_check rc=0 0 defect (log g2.run2.log)
- G3 d5_census rc=0 latin=0 cyrillic=0 curly_in_cjk=0 curly_total=0 noto_sans=776
- G6 occlusion rc=0 0 flag
- G7 p8_extract rc=0 noted=150/150
- G8 p8_compare rc=0 status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138] 
- G9 freeze_baseline rc=0 baseline: 8/8 SVGs byte-identical (repointed files: none)
- G10 freeze_diff rc=0 cjk_added_total=0 latin_added=164
- G11 spill rc=0 SPILL_SWEEP 2026-w46-pt-ru: 32 boxes, 71 candidates, 0 SPILL, 71 OBSERVE 
- G12 boxtitle rc=0 BOXTITLE 2026-w46-pt-ru: 29 titles, 323 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal 
- G13 edge rc=0 EDGE_SCAN 2026-w46-pt-ru: 8 pages, 0 TOUCH, 0 NEAR 
- G14 creambox rc=0 p7-lingua.svg: els 182->208 lines 99->103 diff 79 moved 50 defects 0 observe 0 p8-avaliacao.svg: els 1492->1524 lines 244->246 diff 207 moved 16 defects 0 observe 0 CREAMBOX PASS 0 defects 
- G15a print=33962 web=33962 issued=33962 print-web_diff=0 print-issued_diff=0
- G15a text.md BYTE-IDENTICAL（34940 B）。
- G15b（仅记录，D27）：SVG-only 153 / MD-only 0。
- G15c：N/A——pt 无原生校验器，carry-over 路线按 PLAN §2.1。
- G16 census_quotes rc=0   p8-avaliacao.svg: defective=0   TOTAL defective: 0 GRAND TOTAL defective: 0 
- D18 gap=189.6 slogan_centre=975.0 (vs 975) date_end=1862.0 (vs 1862=RIGHT) slogan_end=1265.5 date_start=1455.1 verdict=PASS
- D37 y=372 badge_end=1393.5 cream_left=1439.5 margin=46.0 verdict=PASS
- D47：无。

## 五、新交付物（run2 实测）

- 印刷版 PDF：`A-Lucerna-VOL3-pt-ru.pdf`，2548664 字节，SHA-256 `6ca7280bb30394815e91dcc5f97d3125915dc559058e69c95bc71525abbbe3db`。
- 网页版 PDF：`2026-w46-pt-ru.web.pdf`，1010316 字节（<7 MB），SHA-256 `4578021be66e5305ab14316a339becafb1fe9923f861cf2924b6b97ae0ebd185`。
- `.text.md`：34940 字节，SHA-256 `2b122a224837615fbff14cd2d63a9742cb14884f4c4f2a9100187078faa91e37`（carry-over，与已发版 BYTE-IDENTICAL）。

## 六、KIT

- `patched/2026-w46-pt-ru/WEEKLY-KIT.md` 已更新：追加 D5 交付物 pin 块 + `## D5 rebuild (2026-11-15, D5-only)` 节（含装机、修前普查、逐条修复 file:line、终轮门禁分）。
