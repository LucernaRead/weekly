# GATE LOG — W47 core-ko fix1 (run 11)

- 对象：`production/2026-w47/core-ko/` run 11（D2/D3/D4 修复后整期重建）
- 解释器锁定：构建 run.py / check_core / check_gloss / textmd 与 freeze 门用 `/usr/bin/python3`（PIL 10.2.0）；render.py / webpdf.py 用 `tools/venv/bin/python`（cairosvg/fontTools）。occlusion 双解释器各跑一次。
- 全部日志在同目录：`build-run11.log`、`render-run11.log`、`webpdf-run11.log`、`textmd-run11.log`、`check-core-run11.log`、`check-gloss-run11.log`、`p8-extract-run11.log/.json`、`p8-compare-run11.log/.json`、`occlusion-run11.log/.json`、`occlusion-run11-syspy.log/.json`、`freeze-run11.log/.json`（产物 `freeze-run11/svg/`）、`freeze-diff-run10-run11.log/.json`、`print11.txt`、`web11.txt`、`svg-hashes-run11.txt`、`work/`（4 张改动处放大裁图）。

## 门禁结果（全绿）

| 门 | 工具 / 方法 | 结果 |
|---|---|---|
| 构建 0 警告 | `/usr/bin/python3 run.py` | 0 FLOW OVERFLOW / 0 HEAD TOO WIDE；TOTAL 150（A2 51 / B1 72 / B2 27；逐页 10/18/18/18/18/18/12/38） |
| 遮挡审计 | `tools/occlusion_audit.py`（venv + 系统 python3） | 各 0 flags；自检 6 类（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX）全触发，干净对照静默 |
| p8 extract | `tools/p8.py extract --p8 svg/p8-siheom.svg --total 150` | 150/150 |
| p8 compare | `tools/p8.py compare --core-p8 … --edition-p8 …（同文件） --total 150` | CLEAN，missing=[] extra_count=0 uncertain=[] keydiff=[] |
| freeze 基线 | `/usr/bin/python3 tools/freeze.py baseline --build … --core-svg … --out freeze-run11` | **8/8 逐字节一致**（逐文件 OK 行俱全）；core integrity：shipped SVG 未变。注：首次跑 2 秒即异常退出 120、日志为空（外部中断，非工具结论）；原样重跑一次即 8/8，无文件损坏 |
| freeze diff run10→run11 | `tools/freeze.py diff --core-svg scratch-ko-fix4/freeze-run10/svg --edition-svg svg/` | 仅 p1/p4/p7 变：p1 +2/−2，p4 +4/−4，p7 +6/−6；p2/p3/p5/p6/p8 +0/−0；新增 CJK 28 字全为新句字（p1 +4、p4 +4、p7 +20），无计划外字符串 |
| 文字层一致 | `pdftotext` print vs web + `cmp` | 各 49,451 字节，逐字节一致（run 10：49,379） |
| U+2019 全扫 0 | 8 SVG + text.md + ABSTRACT.txt 逐字计数 | U+2019=0，U+201C=0，U+201D=0 |
| check_core | `/usr/bin/python3 check_core.py` | gloss fails 0；P7 phrases 8/8 verbatim（新 #7 通过）；orphan issues 0；日期全对 |
| check_gloss | `/usr/bin/python3 check_gloss.py` | 10 项，日志与 run 10 逐字节同（已裁定类） |
| P8 答案字号 | PyMuPDF，P8 y≥1302/2700 区 | 162 spans，最小 9.975pt（≥9.75，与 run 10 同） |
| 目视（改动处） | 4 张放大裁图 + P7 整版 | P1 ex10、P4 ex47/48、P7 框架例句、P7 金句 #7 均干净无溢出/压线；P7 整版无溢出/重叠/压页脚 |

## 成品

- 印刷 `Lucerna-VOL4.pdf`：46,232,227 B，SHA-256 `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27`
- 网版 `Lucerna-VOL4-web.pdf`：4,232,878 B（< 7 MB），SHA-256 `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7`
- text.md：26,048 B / 333 项，SHA-256 `ba1b80f8edabc76eac398e34e80718254e1e584966a39a7c5a9a504b5fe9dda3`
- SVG 哈希：p1 `00227ca1…`、p2 `faf9e3c5…`（同 run 10）、p3 `b447a559…`（同）、p4 `d997631e…`、p5 `09f7fc23…`（同）、p6 `d45b0355…`（同）、p7 `14b7cf13…`、p8 `e88f7d42…`（同）

## 待后续

- 本轮只做构建方自查 + 机械门全绿；按 SOP §8.4，须协调员另派独立核心 re-proof（从头全量一轮）与全家重扩，本轮结论不替代复校。
