# GATE-LOG — 2026-W47 ja-fr 第一轮独立复校 · 机械门自跑记录

- 校对员：叶子（第一轮）｜日期：2026-11-11
- 工作目录：`~/workspace/weekly-git`（main clone）；笔记目录：`hidden_files/w47/scratch-proof-ja-fr1/`
- 解释器：`tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）——SOP/AGENTS 规定解释器。
  （注：系统 python3 为 Pillow 10.2.0，未使用；ko 家庭已证实 Pillow 版本差可致 freeze 翻转，故全程只用 tools/venv。）

## 0. 开工探针（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- `hidden_files/w47/scratch-proof-ja-fr1/.probe` 写盘成功。

## 1. 身份复核（自行算出，与 KIT §8 比对）

- 印刷 PDF `production/2026-w47/fanout-ja/2026-w47-ja-fr/Lucerna-VOL4-JA-FR.pdf`：
  28,347,993 字节；SHA-256 `5903a36b47668d91c04dafb047f94022299f8f5308647696fe7cff9c47244517`（前 8 位 5903a36b）——与 KIT 一致。
- 网页 PDF `Lucerna-VOL4-JA-FR-web.pdf`：
  4,458,579 字节；SHA-256 `99fd99aff8f1a8289ae58435efc0a85e04b36e79d1a09ce7d700493e3658c47c`（前 8 位 99fd99af）——与 KIT 一致。

## 2. run.py 重跑（freeze 用副本）

- 方法：整版目录复制到 `scratch-proof-ja-fr1/rerun/`（删 `__pycache__`），`tools/venv/bin/python run.py`，日志 `gates/run-rerun.log`。
- 结果：**exit 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` 0 行**；P8-keys flow 末行 col 3 y=2411（底 2540，余 129px）。
- 登记表：TOTAL 150；级别 A2 48 / B1 73 / B2 29；分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；
  题型 {Compléter: 50, Choix multiple: 51, Associer: 12, Former une phrase: 8, Vrai ou faux ?: 11, Texte à trous: 13, Traduire: 4, Rédaction: 1}；
  范文 154 字。——与 KIT §1 登记逐项一致。

## 3. Freeze（直接 sha256 比对 8/8）

- 原版 SVG（`gates/sha-orig.txt`）vs 重跑 SVG（`gates/sha-rerun.txt`）：**8/8 字节一致**。
  - p1 `ee6170ef…`、p2 `a09e586b…`、p3 `6cfcf368…`、p4 `6deffcba…`、p5 `6860640a…`、p6 `b454eb02…`、p7 `2501facf…`、p8 `fbe9bdb8…`（完整值见 sha 文件）。
- （注：首次比对因相对路径写错报 DIFF，属比对脚本路径错误；用绝对路径重比后为 8/8 OK。此处如实记录。）

## 4. Occlusion 几何审计（`tools/occlusion_audit.py`）

- 命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/fanout-ja/2026-w47-ja-fr/svg --json gates/occlusion.json`
- 结果：**exit 0；0 flags**。自检先行通过：6 类 planted flags 全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），clean controls 静默。
- 日志：`gates/occlusion.log`；JSON：`gates/occlusion.json`。

## 5. P8 extract + compare（`tools/p8.py`）

- extract：`p8.py extract --p8 …/svg/p8-tesuto.svg --total 150 --json gates/p8-extract.json` → **noted set 150/150**，exit 0。
- compare：`p8.py compare --core-p8 production/2026-w47/core-ja/svg/p8-tesuto.svg --edition-p8 …/svg/p8-tesuto.svg --total 150 --json gates/p8-compare.json`
  → **status CLEAN；missing=[]；extra_count=0；uncertain=[]；keydiff=[137, 138, 139, 140]**，exit 0。
- keydiff 逐条核实（extract JSON 的 keys 字段与 core 对照）：
  - 137 core `二之酉在11月19日。` → fr `Ni-no-tori, c'est le 19 novembre.`
  - 138 core `新酒在11月19日解禁。` → fr `Le vin nouveau sort le 19 novembre.`
  - 139 core `流行语提名在11月5日发表。` → fr `Nominations des mots à la mode : 5 novembre.`
  - 140 core `去看红叶的人应该同时确认预报日期和现在的状况。` → fr `Qui veut voir les feuilles doit vérifier à la fois les dates prévues et la situation actuelle.`
  - 4 条均为 E 组答案的 JA→FR 翻译，日期与事实全保留；其余 146 键与 core 字节一致。

## 6. print/web 文字层一致

- `pdftotext` 印刷版与网页版：各 **47,208 字节**，`cmp` **字节一致**（`gates/print.txt` / `gates/web.txt`）。
- 网页 PDF 4,458,579 字节 < 7 MB。

## 7. P8 字号（PyMuPDF，印刷 PDF p.8）

- 最小字号 **9.975pt**（答案，165 spans，实测显示 9.98）≥ 9.75pt 门槛；次档 **10.35pt**（题干，79 spans）未动。
- 尺寸分布（pt：spans）：9.98:165、10.35:79、10.88:6、11.25:5、11.62:1、12.75:5、13.5:2、14.25:37、14.62:12、15.38:3、15.75:16、17.25:4、18.0:39、18.75:2、34.5:3。

## 8. U+2019 缺陷类回归（全扫 8 个 SVG）

- U+2019 总数 **0**；撇号均为 U+0027（×51）；U+02BC 0×。
- 目视抽查含撇号的行（P1 `Jeudi, c'est Ni-no-tori`、`la fin de l'année`、`des saveurs d'automne` 等）：无宽字形断裂。

## 9. §1.1 / 版式 grep 审计（8 个 SVG）

- `·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×；`Page N sur 8` 每版 1×；刊头 196px 仅 P1。
- VOL：`VOL.4` ×10（刊头/标题/页脚），`VOL.3` ×1（P4 冻结正文「前号（VOL.3）」），`VOL.5` ×4（P4 冻结正文「次号（VOL.5）」+ P7 法文读者园地 ×2 + P7 预告），`VOL.2` 0×。
- 徽章 chip（60×30，rx=2.7 的 rect + 白字）：P1 10×A2、P2 15×A2、P3 7×A2+8×B1、P4 18×B1、P5 18×B1、P6 18×B2、P7 4+4+4、P8 9×A2+22×B1+4×B2；合计 141（A2 45 / B1 70 / B2 26）；fill 与文字逐一配对，0 错配；逐页计数与核心版完全一致。

## 10. 翻译层机械核实

- fr-vs-core SVG 文本行全量差分：fr-only 379 行、core-only 358 行；fr-only 行中含 CJK 的 92 行全部是「日文冻结头 + 法文」混合行；**新增 CJK 词串 0 个**（410 个 distinct CJK 词串逐项过目，均为日语词汇）。
- 中文残留扫描：`译注` / `参考答案` / `酉之市` / `提名` / `吉伊卡哇` 全部 0×；`Chiikawa` ×4；`ryuuryuu` ×5；`参考答案` 等无。
- 金句 8 条：日文与核心逐字一致，去空白归一化后逐条在正文所标页码真实出现（p.1 ×3、p.2 ×2、p.3、p.4、p.7）。
- 范文字符数：154（实测去空白计数，与登记一致）。
- 日期/星期（`date -d`，Asia/Tokyo）：2026-11-16 周一、11-19 周四、11-22 周日、11-05 周四、11-08 周日、11-23 周一、12-01 周二——与正文所标全部一致。

## 11. 目视记录

- 印刷 PDF 8 页自渲染（110 dpi，`render-print/p-1.png` … `p-8.png`）；网页 PDF P1/P8 自渲染（`render-web/web-p1.png`、`web-p8.png`）。8 版 + 网页 2 页全部读完，无溢出、无重叠、无截断。
- Q124 放大核实（`gates/q124-zoom.png`）：选项 A 为 `2勝1敗`（低分辨率初读误为 `2勝0敗`，已纠正；与核心版逐字一致）。

## 12. 缺口记录

- `hidden_files/w47/scratch-fanout-ja/` 内仅有 `.probe-stick8`；任务书要求先读的 `FANOUT-REPORT-ja.md` 及 KIT §8 引用的门文件（`fr-occlusion-run5.json`、`fr-p8-run5.json`、`fr-p8compare-run5.json`、`fr-sha-run5.txt`、`fr-sha-run6.txt`、`build-fr-run6.log`、`map-fr.json`）均不在仓内——本轮全部机械门均为独立重跑（见上），结论不依赖上述文件。
