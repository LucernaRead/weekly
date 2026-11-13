# GATE-LOG — 2026-w47-ja-en 第一轮独立复校 机械门自跑记录（叶子）

- 解释器：`tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）——与 KIT §9
  登记的构建解释器一致（ko 家庭 Pillow 版本差教训：已先确认解释器再跑冻结）。
- 工作目录：`~/workspace/weekly-git`；只读 `production/2026-w47/fanout-ja/2026-w47-ja-en/`；
  未碰 core-ja、W43–W46、其他目标语、tools/；未跑 insert.py、lint --write；
  未 git add/commit/push/reset/stash。

## 0. 开工探针（双通才动手）
- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → 成功
  （`da0c4eb8d9a48d171a33574b380752e183286751`）。
- `hidden_files/w47/scratch-proof-ja-en1/.probe` 真实写入成功。

## 1. 身份核对（开工 + 收工两次一致）
- 印刷 PDF `Lucerna-VOL4-JA-EN.pdf`：27,440,477 字节，
  SHA-256 `c29f6f987ba709082145c4ca71b7a656eb0b6bcc5f5f49d89f22b35a6161bbeb` ✓
- 网页 PDF `Lucerna-VOL4-JA-EN-web.pdf`：4,428,571 字节，
  SHA-256 `9d10efc5fdc72c1c46194eea25cb5ff7b59f52c316a13fb5564395439396beb1` ✓
- 8 页（pdfinfo / PyMuPDF 均确认 8 页）。

## 2. run.py 重跑（exit 0，零溢出）——两次
- `tools/venv/bin/python run.py`（两次，均在 build dir 内）：
  exit 0；日志中 `overflow` / `too wide` 出现 0 次。
  日志：`run-proof1.log`、`run-proof2.log`。
- REGISTRY STATS（两次一致）：TOTAL 150；
  by level {'A2': 48, 'B1': 73, 'B2': 29}；
  by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}；
  by type {'fill-in': 50, 'multiple choice': 51, 'matching': 12,
  'sentence building': 8, 'true/false': 11, 'cloze': 13, 'translation': 4,
  'writing': 1}；model chars: 154。
- 流量实测与 KIT 一致：P7 col3 ends 1783.1；P7 teaser ends 2557.1（footer 2580）；
  P8-ex ends col 3 y=531（bottom 1252）；P8-keys ends col 3 y=2426（bottom 2540）。

## 3. Freeze（直接 sha256 比对 8/8）
- 重跑前快照 `/tmp/proof-ja-en1-sha-before.txt`；两次重跑后
  `sha-proof1.txt`、`sha-proof2.txt` 逐字节比对：8/8 byte-identical。
  （重跑只重写了 SVG，二者与构建时的 SVG 哈希相同；PDF 未重建、未改动。）
- p1 `c695313e…` / p2 `da0faee4…` / p3 `42f368e3…` / p4 `53bc8f7c…` /
  p5 `96bc4ac9…` / p6 `9efab662…` / p7 `9d437896…` / p8 `cc6c9357…`

## 4. Occlusion 几何审计 —— 0 flags
- `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/fanout-ja/2026-w47-ja-en/svg`
  → exit 0；自检 OK（6 类 planted 全部触发，clean 对照静默）；
  `0 flags`。输出：`occlusion-proof.json`（`flag_count: 0`）。

## 5. P8 extract + compare —— CLEAN
- `tools/p8.py extract --p8 …/svg/p8-tesuto.svg --total 150`
  → noted set = 150 of 150，exit 0。输出：`p8-extract-proof.json`。
- `tools/p8.py compare --core-p8 …/core-ja/svg/p8-tesuto.svg --edition-p8 …/svg/p8-tesuto.svg --total 150`
  → status CLEAN，missing=[]，extra_count=0，uncertain=[]，
  keydiff=[137, 138, 139, 140]，exit 0。输出：`p8-compare-proof.json`。
- 4 条 keydiff 已逐条核实原因（PROOF-NOTE §7）：均为 E 组翻译题答案由中文译成英文；
  其余 146 条键逐字节一致。

## 6. print/web 文字层一致
- `pdftotext -layout` 双份各 99,987 字节，`cmp` 逐字节相同；
  两份均非空（>0），无图片版问题。
- 文字层中 U+2019 0 次、U+2018 0 次、吉伊卡哇 0 次。

## 7. §1.1 / U+2019 / VOL / 徽章 grep 审计（8 SVG）
- U+2019：8 版均为 0；`·`：8 版均为 0；`#fbfaf6` 每版 1 次；
  `#f7f1e2` 0 次；禁色（金 `#c9a227`、红褐）0 次；
  `Page N of 8` 每版 1 次；刊头 `font-size="196"`（P1）1 处；
  VOL.4：P1 3 次、P2–P8 各 1 次；VOL.3 仅 P4 1 次；VOL.5 仅 P4 1 次 + P7 3 次
  （与 core-ja 计数逐版相同）。
- 徽章 rect 计数：P1 A2 10 / P2 A2 15 / P3 A2 7+B1 8 / P4 B1 18 / P5 B1 18 /
  P6 B2 18 / P7 A2 4+B1 4+B2 4 / P8 A2 9+B1 22+B2 4；总数 141。
  与登记 reconciliation：3 个 matching 组（P2 A2、P3 B1、P8 B2）各 4 题共用
  1 枚徽章，141 = 150 − 3×3；折合级别 A2 48 / B1 73 / B2 29，与登记一致。

## 8. P8 字号（PyMuPDF，印刷 PDF 第 8 页）
- 最小字号 9.98pt（165 个 span）≥ 9.75pt ✓（即 KIT 登记的 9.975pt）；
  次小 10.35pt（79 个 span）= 题干字号，抽查 113 题题干为 10.35pt，未动。
  其余字号：10.88 / 11.25 / 11.62 / 12.75 / 13.5 / 14.25 / 14.62 / 15.38 /
  15.75 / 17.25 / 18.0 / 18.75 / 34.5。

## 9. 翻译层专项核查（源码 diff 全量）
- core-ja ↔ fan-out 5 个 content 模块 + bslib4/render 全量 diff 逐行审读；
  274 个 distinct 已改字面量 + bslib4 4 处全部为中→英忠实转写；
  未改的全部 CJK 字面量（AST 抽取，含 call 参数与所有字符串常量）逐一核查，
  均为冻结日语，无一处遗漏的中文讲解。
- `Chiikawa` P7 1 次 + P8 3 次；`吉伊卡哇` 0 次；`ryuuryuu` P7 1 次 + P8 4 次；
  `りくりゅう` 出现次数与核心逐版相同（P1 1、P5 5、P7 3）。
- 金句 8 条：逐条在 SVG 文本中定位，所注页码的正文中一字不差存在
  （第 6 条在 P7 出现 2 次：B1 栏目原文 + 金句区）。

## 10. 目视（从印刷 PDF 重渲染，100 dpi）
- 印刷版 P1–P8 逐版目视 + 网页版 P1/P8 目视：无溢出、无重叠、无压页脚、
  无豆腐块；图片 5 张与出处齐全；P6 图表 38/24/22/16 = 100% 且柱形比例正确。
  渲染图：`render/print-{1..8}.png`、`render/web-p1-1.png`、`render/web-p8-8.png`。
- 撇号放大抽查：`render/zoom-p7-apos.png`（France's）、`render/zoom-p8-apos.png`
  （Fujiryūga's）——窄形 ASCII 撇号，无宽字形断裂。

## 缺口（非本版缺陷）
- `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md` 及该目录全部文件
  在本 clone 中不存在（全仓 `find` 无此文件）；builder 的审计节与裁定备忘、
  门输出 JSON、map 文件无法复核，改以 KIT §7/§11 + 本轮全部自跑门 +
  全量源码 diff 作等效核实。
