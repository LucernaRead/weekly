# GATE-LOG — 2026-W47 de-it · proof2（rebuild 4）

日期：2026-11-11。复校员：proof2（独立）。工作目录（scratch）：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-it2/`
（子目录 `tmp/`（TMPDIR）、`render/`、`gates/`）。
版目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-de-it/`。
复校全程只读，未改源、未 commit、未 push。
build 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（含 fitz/PIL；
系统 python3 无 fitz）。

## 0. 探针与 SHA

- 探针（开工前）：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
  rc=0，hash `9daeafb9…`；在 scratch 真实写文件通过。后又跑多次，长命令
  未见 rc 变化。
- SHA 核对（开工、收尾各一次，两次相同）：
  - `Die-Lucerna-VOL4-de-it.pdf` 10,965,087 B
    `ca802fb853eb3f18c61cddd5da406c72c9c0471cabd84c76731478f4cdf6f2c0`
  - `Die-Lucerna-VOL4-de-it-web.pdf` 1,596,994 B
    `09fb247059a96c37c0fa1fe0178b7dacf35cd1e5500fe6f089b929c722c82300`
  - `2026-w47-de-it.text.md` 49,712 B
    `1594ba080bece8b9a947cf011a64a355125b8869f82413ccdb03ae31a269f255`
- `pdfinfo`：两份 PDF 均为 8 页，1462.5 × 2025 pt。
- verify.py 跑后 `sha256sum -c gates/before.sha`——8 份 SVG + 2 份 PDF + text.md
  全部未变。收尾 `git status --porcelain production/2026-w47/2026-w47-de-it/`
  仅显示 `?? production/2026-w47/2026-w47-de-it/`（该版目录本来就是未追踪），
  我无改动。

## 1. 全套门禁（命令 + RC + 结果）

| # | 命令 / 工具 | RC | 结果 |
|---|---|---|---|
| 1 | `tools/occlusion_audit.py`（全部 8 页 SVG） | 0 | **0 flags**；selftest 6 类全触发、干净对照静默。`gates/occlusion.json`, `occlusion.log` |
| 2 | `tools/p8.py extract` | 0 | **150/150**。`gates/p8extract.json`, `p8extract.log` |
| 3 | `tools/p8.py compare`（vs core-de） | 0 | **CLEAN**；keydiff `[137,138,139,150]`（预期）。`gates/p8compare.json`, `p8compare.log` |
| 4 | `tools/freeze.py` diff（vs core） | 0 | 新增 CJK 合计 **7**，全为 U+3000（P2–P8 各 1）。`gates/freeze.json`, `freeze.log` |
| 5 | rebuild-A `freeze_direct.py --core-svg core-de/svg` | 0 | 源码级 PASS（520 删 / 528 增，0 未 accounted）；渲染级 **8/8**（147/163/195/166/173/175/150/186；sha 083e2a2a/689045ad/fc88f676/df1bebf7/86fa4421/2bbe05f9/b7aa0771/57e118e7）。`gates/freeze-direct.json`, `freeze-direct.log` |
| 6 | rebuild-A `keycheck.py`（150 题） | 0 | **149/150** 精确；唯一非精确：Q150 抽取器截断（预期）。`gates/keycheck-150.json`, `keycheck.log` |
| 7 | rebuild-A `boxtitle.py` | 0 | **7/7**（364.1 / 361.3 / 242.2 / 331.9 / 379.5 / 371.9 / 395.0 ≤ 400.5px）。`gates/boxtitle.log` |
| 8 | rebuild-A `measure.py` | 0 | **24/24 PASS，0 FAIL**。`gates/measure.log` |
| 9 | `verify.py` | 0 | TOTAL 150、编号连续、verbatim OK、SOP 1.1 审计 True、P8 字号底线 True、17 禁词全无、图表 44+33+23=100、日期加法三条全 True。`gates/verify.log`。注：`verify.py` 文件不可执行（直接运行 rc=126），须 `tools/venv/bin/python $ED/verify.py` 显式调用。 |
| 10 | `pdffonts`（两份 PDF） | 0 | 网页 PDF 现嵌 `LucernaNewsreader-Bold` 与 `LucernaNewsreader-Italic`（proof1 T1/T2 已修）。 |
| 11 | `pdftotext`（默认模式 + `-raw`，两份 PDF） | 0 | 默认模式各 50,592 B **逐字节相同**；-raw 各 49,392 B，归一化文本完全相同。`gates/print.txt`, `web.txt`, `print-raw.txt`, `web-raw.txt` |
| 12 | `abut_scan.py`（印/网，venv python） | 0 | 各 **23 处、逐处相同**，全部为 "→ ___" 设计间距（5.4 SVG 单位 ≈ 4.05pt）；真实缺口 0。`gates/abut-print.log`, `abut-web.log` |
| 13 | canonical `tools/creambox.py`（8 份 SVG，32 盒） | 0 | **真漫出 0**。工具盒：底 803.5、末基线 783.9、clearance +19.6（desc-clear +13.5）；LESERBRIEFE y 819.5、clearance +10.4（desc-clear +4.5）；NOCH EIN WORT 底 1538.0、clearance +42.9。4 处窗口负值均为已知假阳性（inside-only 全部为正：P1 标题盒 +16.0；P7 BEISPIELE 三盒各 +47.4）。`gates/creambox-all.log` |
| 14 | `quote_pixel.py`（200 dpi，H 框 / Q67） | 0 | H 框闭引号前空隙 **1.8pt = 0.12em**；Q67 **0.72pt = 0.07em**；均 PASS（≤0.2em）。`gates/quote-pixel.log`, `gates/spots.json` |

## 2. 渲染与目视

- `render/`：100 dpi 印版 P1–P8（`print-p-{1..8}.png`）、网页 P1–P8
  （`web-p-{1..8}.png`）；200 dpi：`print200-p1/p7/p8`、`web200-p1/p7`；
  重点裁切：`crop-p7-toolbox-print/web20`、`crop-p8-hbox`、`crop-p8-key67`、
  `crop-p1-head-print/web20`、`crop-p1-word-print/web20`。
- 目视：印版 P1–P8 全页看过；网页 P7–P8 全页、P1–P6 以像素差异核对。
  印/网 100 dpi 像素差异：P1 0.26% / P2 0.00% / P3 0.06% / P4 0.14% /
  P5 0.10% / P6 0.00% / P7 0.03% / P8 0.01%（图像重压缩带，无内容差异）。
- P8 最小字号（PyMuPDF，venv python）：印版 9.94pt、网页 9.94pt（≥9.75pt）。
- chips（rx="2.7" 矩形）：每页 10/15/18/15/18/18/12/35，总计 141；
  P8 A2 22 / B1 13 / B2 0。
- spot 查找脚本 `find_spots.py`（rawdict：span 层无 'text'，须由
  `chars[].c` 拼接；首两次尝试因 KeyError 失败后修正）。

## 3. 文本核对

- text.md 全文 1,185 行逐行读过。MUSTER 独立空白切分计数 **84 词**。
- Q34：新题干 `"Am Montag öffnet in Köln der erste ___."` 于 content34.py、
  text.md、P3 SVG、印版文字层、网页文字层各 1×；旧题干五处均为 0×。
- P7 金句 8 句：text.md 中每句恰 2 次（正文 + P7），出处页码全对；
  verify.py verbatim OK 同。
- 150 键逐题人工复核见 PROOF-NOTE §6。
- 德语冻结：与 core-de text.md 的德语引文多重集 25/25 完全相同；
  diff 行数 940，与 proof1 相同（意大利语替换层）。

## 4. 事实网查

逐条 Web 查证（2026-11-11）：Buß- und Bettag（2026 年 11 月 18 日星期三、
萨克森法定假日、1995 年废止、+0.5pp、3–24 时禁舞）；Totensonntag 11 月 22 日 /
第一待降节 11 月 29 日；科隆三市场开市期与 Totensonntag 闭市；亚琛
11 月 20 日–12 月 23 日；Wilhelm Ritter (1860–1948) 画题；Kepler 1903
《Im Lande des Christkinds》；德甲 MD9 九场比分与 30 球；MD10 赛程；
欧冠 MD4 四场；11 月 5 日欧联/欧协联三场；塞尔维亚–德国 11 月 13 日 20:45
贝尔格莱德（RTL）与德国–荷兰 11 月 16 日 20:45 柏林（ARD）（5 分 / 8 分；
儿童 + 50 球迷豁免）；欧战 11 月 24–26 日六场对阵；2027 预算表决
11 月 27 日与电税 2,05 欧分/千瓦时（自 2003 年未变）。全部与正文一致。
日期星期另以 `TZ=Europe/Berlin date -d` 核验（3.11.二 … 29.11.日，见
PROOF-NOTE §5）。

## 5. 结论

verdict **(b)**：D1 一项（KIT §5/§6 仍登记 rebuild 3 的旧 SHA，文档问题、
低严重度；只改 KIT 两行文字，不动交付件、不重建）。交付件三件内容与几何
零缺陷；proof1 的 T1/T2 已修（字体 + 200 dpi 对照双确认）；P7 工具盒
fix1 宣称全部实测属实；de-en D1/D2 宽引号类在本版不复现（H 框 / Q67
均 PASS）。观察项 O1–O6 见 PROOF-NOTE §8。
