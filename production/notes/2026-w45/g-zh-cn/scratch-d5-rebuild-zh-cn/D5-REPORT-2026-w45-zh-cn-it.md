# D5-REPORT-2026-w45-zh-cn-it — W45 zh-cn/it (D5 + §1.1 rebuild, D3 canonical)

Builder: subagent (2026-11-14). Status: **BUILD COMPLETE — run2 ALL-GREEN**; awaiting independent reproof + closer. No commit, no push, scratch NOT cleared (closer's job).

## 一、装机

- Installer `apply_variant.py` 在 face= 引擎上 FATAL（`cmap: pattern found 0x, expected 1`）—— hand-port `scripts/d5_port_zhcn.py`（D5_BLOCK/FIX2_BLOCK/READER_CONST 逐字抄 installer；仅锚点与 `_PATH`→`_FONT_FILE` 改动）。见家族报告 §1。
- `--check` dry-run rc=0（10 项改动列出）；安装 rc=0；adapted routing test `test_d5_routing_zhcn.py` FAILURES: 0；fix2 标记 5，`_QUOTE_CLS` 4；`_D5_READER="latin"`（variant SC）。
- D3 canonical：fanout svglib 已重打 canonical §2a（core/de/es/nl/pt 用 `apply_canon.py`；fr/it/ru 用 caron-preserving 变体 `apply_canon_caron.py`——CARON FIX 循环保留，见家族报告 §4）。canon-only 验收：本版 run.py TOTAL 150，p8 抽 150/150，compare exit 0 CLEAN。
- Step 3 production 写入：core-zh-cn svglib = canon+D5（32,945 B，与 patched 逐字节一致）；其余 7 版 production svglib = canon-only；ja/ko production svglib 未动（closer 以 patched/ 同步）。

## 二、基线（修前，`logs/baseline_all.log`）

- run.py rc=0 TOTAL 150 / FLOW 0 / HEAD 0；render rc=0；webpdf rc=0。
- 印 PDF 44,289,766 B，MANIFEST pin 漂移（fr −3 B / it OOM-anomaly pin / ru +52 B，见家族报告 §2）；网 PDF 2,525,943 B（< 7 MB）。
- pdfdiff vs 已发网 PDF：verdict: IDENTICAL；vs fanout 网 PDF：verdict: IDENTICAL；印 vs 网 multiset rc=0。
- textexp 与 fanout `.text.md.new` 逐字节一致（43,543 B）；SVG 8/8 与 fanout 一致。
- 修前普查：拉丁 464（>0，符合修前预期）；p8 抽 150/150，缺 []；compare vs 基线 core：0 {'status': 'EXTRA_ONLY', 'missing': [], 'extra': [2, 4, 5, 6, 19, 36, 101, 106, 131, 134, 146], 'keydiff': [16, 17, 18, 20, 34, 35, 37, 38, 52, 53, 54, 55, 56, 70, 71, 72, 73, 74, 88, 89, 90, 91, 92, 103, 108, 110, 112, 132, 133, 135, 136, 137, 138, 139, 140]}。

## 三、缺陷与修法（run1 → run2）

run1 门禁：NOT GREEN: G6 occlusion, G12 pdf_edge。修法一律只动字号/盒高（caron 修法只动 svglib 逻辑），绝不改文案；每次修复后全量重渲 + 全部门禁重跑。

| # | 门 / 缺陷 | 修法 | P8（修前→修后）/ 页脚余量 |
|---|---|---|---|
| F0 | G12 pdf_edge BLOCKED (rc=2) | Same duplicate-PDF cause as de; same fix. | — |
| F1 | G6 occlusion TEXTX ×7 (caron runs) | Same CARON FIX re-base repair as fr (patched svglib only). After repair: 0 flags. | P8 unchanged (re-measure on run2) |

- P8（creambox 实测）：235→235 行，页脚余量 45.6→45.6px（页脚线 y=2596，页底 2700；P1-only 修复，P8 不变，符合预期）。
- run1 门禁日志保留为 `logs/2026-w45-zh-cn-it/gates-run1.log` + `GATES-SUMMARY-run1.txt`。

## 四、门禁（run2，`logs/2026-w45-zh-cn-it/GATES-SUMMARY.txt`）

| 门 | 结果 |
|---|---|
| G1 run | G1 run: PASS — rc=0 TOTAL=150 FLOW=0 HEAD=0 ALL-DONE=True |
| G2 head_check | G2 head_check: PASS — rc=0 defects=0 |
| G3 d5_census | G3 d5_census: PASS — rc=0 lat=0 cyr=0 curly_cjk=0 noto_sans_elements=0 |
| G4 render | G4 render: PASS — rc=0 print=36060116 B sha=b4d64aded34b |
| G5 webpdf | G5 webpdf: PASS — rc=0 web=2319429 B (<7MB) sha=b83c75f5f238 |
| G6 occlusion | G6 occlusion: PASS — selftest rc=0 audit rc=0 flags=0 |
| G7 p8 extract | G7 p8 extract: PASS — extracted 150/150 missing=[] |
| G8 p8 compare | G8 p8 compare: PASS — exit=0 status=CLEAN missing=[] extra=[] keydiff=[] |
| G9 freeze | G9 freeze: PASS — baseline 8/8 rc=0 diff rc=0 added-CJK=0（added Latin strings 275，added CJK 0） |
| G10 spill_sweep | G10 spill_sweep: PASS — rc=0 SPILL=0（35 boxes / 102 candidates） |
| G11 boxtitle | G11 boxtitle: PASS — rc=0 DEFECT=0（46 titles / 514 body lines） |
| G12 pdf_edge | G12 pdf_edge: PASS — rc=0 TOUCH=0 NEAR=0 |
| G13 creambox | G13 creambox: PASS — rc=0 CREAMBOX PASS 0 defects |
| G14 text layer | G14 text layer: PASS — print chars=84802 web chars=84802 multiset diff=0（print/web 各 84802 字符） |
| G15a text.md | G15a text.md: PASS — patched textexp BYTE-IDENTICAL vs baseline export |
| G15b verify_textmd | G15b verify_textmd: RECORDED — patched rc=1 residual SVG/MD=378/1805 | baseline-control rc=1 residual SVG/MD=363/1771 (D27 calibration gap) |
| G15c native verify | G15c native verify: PASS — rc=0 UNEXPECTED=0 ADOPT: 0 UNEXPECTED |
| G16 census_quotes | G16 census_quotes: PASS — rc=0 defective=0 |
| D18 masthead | D18 masthead: PASS — gaps=[529.3, 386.5]（gaps [529.3, 386.5]） |
| D37 P1 subhead | D37 P1 subhead: PASS — right_edge=1382.8 box_left=1439.5 margin=56.7（right edge 1382.8，框左缘 1439.5，余量 56.7px） |

**run2 结论：ALL-GREEN。** 15b 为 RECORDED（D27 口径：共享工具校准缺口，15a + 15c + 重校全文通读为验收；基线对照同样 FAIL，残差差为 run-split 分词所致，零内容差异）。

## 五、新交付物（run2，builder 原件，`patched/2026-w45-zh-cn-it/`）

- 印 PDF `2026-w45-zh-cn-it.pdf`：36,060,116 B，sha256 `b4d64aded34bfc09b3b7e65f7cd5f21487d9bd66f0f1084bb28a57adf625f4c2`
- 网 PDF `2026-w45-zh-cn-it.web.pdf`：2,319,429 B（< 7 MB），sha256 `b83c75f5f2386cd61e462a110aa408158523d309119ae560688dd884cedf9796`
- text.md `2026-w45-zh-cn-it.text.md`：43,543 B，sha256 `43b50acae92c48ba8842b2be2b807a1e879e49f2d890373e787e431d105d6e13`（导出器新建；issues/ 无已发版 `.text.md`，随 bundle 发货）
- 完整 SHA 表：`logs/SHAS-D5.txt`。Closer 拷网 PDF 原件，绝不重跑 webpdf（字节跨次非确定）。

## 六、KIT

- `production/2026-w45/2026-w45-zh-cn-it/WEEKLY-KIT.md`：pin 行已移至 D5 值（印/网字节 + SHA，其中有 SHA 的版），并附 `## D5 重建记录 (2026-11-14)` 一节（含 D5 前值与门禁结论）。
- Dated fix-log 记录保留 port-era 数值（历史测量，非当前 pin）；当前 pin 以 D5 记录节为准。

## 七、Closer 补记（2026-11-15）

- 网 PDF 换件：builder run2 原件（2,319,419 B，sha256 `6402aa316f3be7d58a47b0d34d94d208ca0da4b23e9d830f9968e4c3d874dd0d`）在独立重校重建时被重校 run 的网 PDF（2,319,429 B，sha256 `b83c75f5f2386cd61e462a110aa408158523d309119ae560688dd884cedf9796`）覆盖；全仓 127 份 `*.web.pdf` SHA 扫查证实 builder 原件无其他副本（仅 en/ja/ko 三版 builder 原件仍在 patched/）。重校 run 10/10 ALL-GREEN，印/网文字层多重集差 0（closer 直测），内容与 builder 原件逐字相同，仅 fontTools 跨次字节漂移（+10 B）。落仓发货为重校 run 的网 PDF（即当前 `patched/` 文件），未重跑 webpdf。
- 本报告 §四 G5 行与 §五网 PDF 行已按发货文件重 pin（D19 类文本修正）；KIT pin 行与 D5 节同步更新。印 PDF 与 text.md 仍为 builder 原件，字节 + SHA 与 `logs/SHAS-D5.txt` 一致。builder 网 PDF 原值见家族报告 `FAMILY-W45-ZH-CN-BUILD.md` §9 与 `SHAS-D5.txt`（随 scratch 清理，值见 CLOSE 报告）。
