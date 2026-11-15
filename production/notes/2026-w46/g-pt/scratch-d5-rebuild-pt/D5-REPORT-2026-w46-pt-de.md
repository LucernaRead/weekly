# D5 报告 — 2026-W46 pt × 德语（`2026-w46-pt-de`）

- 刊期：2026-W46（VOL.3）；目标语 pt；读者 德语。
- 性质：D5-only 重建（§1.1 已在 style-port 落仓，基线即新样式）；只降字号，不改内容。

## 一、装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target pt --reader de --week 2026-w46`（先 `--check` 干跑，全干净）。
- 模式 latin；`_D5_READER = "latin"`（`svglib.py:100`）；`test_d5_routing.py` **FAILURES: 0**；fix2 保留（`_QUOTE_CLS` ×4）。未跑 `--patch-core`（D40）。

## 二、基线

- run TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0（core-pt 例外：印/网差 365 字，为模板与读者版家具差，见家族报告 §6）；`issues/` pin（pdfBytes/pdfSha256）与文件一致；text.md 与 `issues/` BYTE-IDENTICAL（carry-over）；p8 extract 150/150。
- 基线印/网字节：2800990 / 849843；文字层字符 34026；D5 普查：Latin 499、Cyrillic 0、curly_in_cjk 0；D1=1、`_D5_READER`=0、Newsreader 9 行。

## 三、run1 缺陷与修法

- run1 FAIL verdict：G1、G2、G6、G12（4 缺陷）、G14（4 缺陷）、D18。
- 修复（6 处，只降字号；探针：SVG 实测墨宽线性缩放、取留 ≥2px 余量的最大适配字号）：
- content12.py:48 `], tsize=20)` → `], tsize=18)`（数字盒标题 `A SEMANA EM NÚMEROS　IN ZAHLEN`，探针余量 10.9px）
- content12.py:131 `EM POUCAS PALAVRAS　IN KÜRZE` 24 → 19.5pt（探针余量 10.8px；D47：`###` 行自导出丢失，见 D5 节）
- content12.py:178 `], tsize=19)`（f.box `PARA NÃO ERRAR　DIE MERKREGEL`，默认 23 → 19，探针余量 8.7px）
- content7.py:84 `A PALAVRA　WORT DER WOCHE` 23 → 21pt（探针余量 10.7px）
- content12.py:255 `e.head("C　COMPLETE COM OS NÚMEROS", 25)` → 22.5pt（探针余量 8.6px）
- content12.py:15–16 刊头标语 + 日期 17 → 16pt（D18：gap −11.8 → run2 PASS）
- 全部修复行 `ast.parse` 通过；`f.box` 修复引用 `tsize=` 所在收尾行（D19）。

## 四、终轮门禁 run2

- 计分门 18/18 全绿（G1–G14 + G15a + G16 + D18 + D37；G15b 仅记录，G15c N/A）。
- G1 run PASS TOTAL=150 OVF=0 HDW=0
- G2 head_check rc=0 0 defect (log g2.run2.log)
- G3 d5_census rc=0 latin=0 cyrillic=0 curly_in_cjk=0 curly_total=1 noto_sans=0
- G6 occlusion rc=0 0 flag
- G7 p8_extract rc=0 noted=150/150
- G8 p8_compare rc=0 status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138] 
- G9 freeze_baseline rc=0 baseline: 8/8 SVGs byte-identical (repointed files: none)
- G10 freeze_diff rc=0 cjk_added_total=0 latin_added=243
- G11 spill rc=0 SPILL_SWEEP 2026-w46-pt-de: 32 boxes, 70 candidates, 0 SPILL, 70 OBSERVE 
- G12 boxtitle rc=0 BOXTITLE 2026-w46-pt-de: 23 titles, 275 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal 
- G13 edge rc=0 EDGE_SCAN 2026-w46-pt-de: 8 pages, 0 TOUCH, 0 NEAR 
- G14 creambox rc=0 p7-lingua.svg: els 180->203 lines 97->92 diff 76 moved 25 defects 0 observe 0 p8-avaliacao.svg: els 406->437 lines 261->261 diff 0 moved 36 defects 0 observe 0 CREAMBOX PASS 0 defects 
- G15a print=34026 web=34026 issued=34026 print-web_diff=0 print-issued_diff=0
- G15a text.md BYTE-IDENTICAL（33217 B）。
- G15b（仅记录，D27）：SVG-only 217 / MD-only 0。
- G15c：N/A——pt 无原生校验器，carry-over 路线按 PLAN §2.1。
- G16 census_quotes rc=0   TOTAL defective: 0     Newsreader (ok): U+201Cx1 GRAND TOTAL defective: 0 
- D18 gap=34.0 slogan_centre=975.0 (vs 975) date_end=1862.0 (vs 1862=RIGHT) slogan_end=1416.7 date_start=1450.7 verdict=PASS
- D37 y=372 badge_end=1405.7 cream_left=1439.5 margin=33.8 verdict=PASS
- D47：1 行：`EM POUCAS PALAVRAS　IN KÜRZE`（已发版 text.md 第 52 行 `### Em poucas palavras`；标题文字仍在终轮印 PDF 文字层内，G15a 差 0）。

## 五、新交付物（run2 实测）

- 印刷版 PDF：`A-Lucerna-VOL3-DE.pdf`，2286402 字节，SHA-256 `e02d2108dad5444076ec3eaa7032fbc435e6f7bfb0cd2477d52b758080fbc2af`。
- 网页版 PDF：`2026-w46-pt-de.web.pdf`，767781 字节（<7 MB），SHA-256 `7327ac8993373f6da349aed3bae53bba599d71e0a49ce514a303029a0990d90d`。
- `.text.md`：33217 字节，SHA-256 `3d4242c0f1891d156cb2e89fc0d98a7c2d50a49d6068047227224a16e527cbf1`（carry-over，与已发版 BYTE-IDENTICAL）。

## 六、KIT

- `patched/2026-w46-pt-de/WEEKLY-KIT.md` 已更新：追加 D5 交付物 pin 块 + `## D5 rebuild (2026-11-15, D5-only)` 节（含装机、修前普查、逐条修复 file:line、终轮门禁分）。
