# GATE-LOG — 2026-W47 ja-nl 第二轮独立复校 · 机械门自跑记录

- 校对员：叶子（第二轮独立复校）｜日期：2026-11-11（UTC 08:22–08:31）
- 工作目录：`~/workspace/weekly-git`（main clone）；记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ja-nl2/`
- 解释器：`tools/venv/bin/python`（与第一轮复校、第一轮返修同一解释器，全程只用它）。
- 任务书身份：印刷 PDF 29,099,141 字节 / `c8b82a84…`；网页 PDF 4,476,527 字节 / `7a7f5fc9…`；text.md 45,627 字节。

## 0. 开工探针（双通才动手，08:22 UTC）

- `echo probe-ja-nl-proof2 | git -C ~/workspace/weekly-git hash-object -w --stdin` → `7511ae7d3c8c706e6d47833eff9f9f8dac35c009`，成功。
- goals scratch `scratch-proof-ja-nl2/.probe` 真实写盘成功。磁盘 `df -h`：46G 可用。未遇 EDQUOT。

## 1. 修前身份核对（与任务书逐字一致）

| PDF | 字节 | SHA-256 |
|---|---|---|
| 印刷 `Lucerna-VOL4-JA-NL.pdf` | 29,099,141 | `c8b82a8491a0d4c54a01214806cede29188e8f4bf6c81c6cf8a1b3bd5ceafa56` |
| 网页 `Lucerna-VOL4-JA-NL-web.pdf` | 4,476,527 | `7a7f5fc96730e82ba8c6697a9accd10387d6aa84a731f81fe3083310df0f97b8` |

双 PDF 各 8 页。text.md 45,627 字节；`wc -l` 与 Python splitlines 均为 1377 行
（KIT 称 1378，见 PROOF-NOTE.md O9，计数口径误差，非成品问题）。

## 2. run.py 重渲染两遍（freeze）

- 命令：`tools/venv/bin/python run.py`（先删 `__pycache__`），日志 `proof-run1.log`、`proof-run2.log`。
- 结果：**两遍均 exit 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` 0 行**。
- 登记表：TOTAL 150；级别 A2 48 / B1 73 / B2 29；分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；
  题型 {zinnen aanvullen: 50, meerkeuze: 51, combineren: 12, zinnen bouwen: 8, waar of onwaar: 11, gatentekst: 13, vertalen: 4, schrijven: 1}；
  范文 154 字；P8-keys flow 末行 col 3 y=2428（底 2540，余 112px）。——与 KIT 登记逐项一致。
- Freeze：run1 SVG（`svg-sha-run1.txt`）vs run2 SVG（`svg-sha-run2.txt`）：**8/8 字节一致**；
  run1 vs 开工前（`svg-sha-pre.txt`）：**8/8 字节一致**（重跑未改任何成品）。

## 3. Occlusion 几何审计（`tools/occlusion_audit.py`）

- 命令：`tools/venv/bin/python tools/occlusion_audit.py <svg dir> --selftest`，再 `--json proof-occlusion.json`。
- 结果：**exit 0；0 flags**。自检先行通过：6 类 planted flags 全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），clean controls 静默。
- 日志：`proof-occlusion.log`；JSON：`proof-occlusion.json`（flags: []）。
- 另：P2 词条框几何复核——修后 4 条释义基线同为 y=1752.06（框内，底缘 1768），y=1776.76 出现 0×。

## 4. P8 extract + compare（`tools/p8.py`）

- extract：`p8.py extract --p8 …/svg/p8-tesuto.svg --total 150 --json proof-p8.json` → **noted set 150/150**，exit 0。
- compare：`p8.py compare --core-p8 production/2026-w47/core-ja/svg/p8-tesuto.svg --edition-p8 …/svg/p8-tesuto.svg --total 150 --json proof-p8compare.json`
  → **status CLEAN；missing=[]；extra_count=0；uncertain=[]；keydiff=[137, 138, 139, 140]**，exit 0。
- 150 键逐题复核：新 extract 的 `keys` 与第一轮复校 `proof-p8.json` 的 `keys` 逐键比对——**0 差异**；
  keydiff 137–140 仍为 E 组答案 JA→NL 翻译（逐条核实正确，未变）。

## 5. print/web 文字层一致

- `pdftotext` 印刷版与网页版：各 **45,931 字节**，`cmp` **字节一致**（`proof-print.txt` / `proof-web.txt`）。
- 双 PDF 各 8 页（PyMuPDF `page_count`）。网页 PDF 4,476,527 字节 < 7 MB。

## 6. P8 字号（PyMuPDF，印刷 PDF p.8）

- 最小字号 **9.98pt**（答案）≥ 9.75pt 门槛；次档 **10.35pt**（题干）。
- 尺寸分布（pt）：9.98、10.35、10.88、11.25、11.62、12.75、13.5、14.25、14.62、15.38、15.75、17.25、18.0、18.75、34.5——与第一轮复校、fix1 复核逐项一致。

## 7. U+2019 缺陷类回归（全扫）

- 8 个 SVG + text.md + content*.py：U+2019 总数 **0**；撇号均为 U+0027。

## 8. 旧罗马字拼写全扫 + 新拼核实

- `Fujiryūga` / `Umi-no-umi` 在 content*.py、svg/（8 个）、text.md、双 PDF 文字层中：**全部 0×**（逐文件 grep -o 计数）。
- 新拼写：P8 SVG `Fujiryōga` ×5、`Chura-no-umi` ×1；双 PDF 文字层旧拼各 0×；
  注 48/49/54/63/111/116 六行逐行在位（200 dpi 放大 + 文字层双重确认）。
- 47 `Yoshinofuji versloeg Ōnosato op dag 1` 未动。

## 9. D1 旧释义全扫 + 新释义核实

- 旧释义精确串 `een bamboe hark voor voorspoedige zaken` / `wanneer er een beetje sneeuw begint te vallen`
  在 content*.py、svg/、text.md 中：**全部 0×**。
- 新释义 `een bamboe hark voor voorspoed` / `wanneer er een beetje sneeuw valt` 在位，
  与 P8 注 16/25/28/141 一致；200 dpi 放大确认四格均单行在框内。

## 10. §1.1 / 版式 grep 审计（8 个 SVG）

- `·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×（共 8×）；`Pagina N van 8` 每版 1×（共 8×）。
- VOL：`VOL.4` ×10，`VOL.3` ×1（P4 冻结正文「前号（VOL.3）」），`VOL.5` ×3（grep；第 4 处分属两个文本节点，见 PROOF-NOTE.md O4），`VOL.2` 0×。
- 中文残留标记词（`吉伊卡哇`/`参考答案`/`酉之市`/`提名`/`说说你自己`/`每周一期`/`日语周报`）：content*.py、svg/、text.md 全 0×。
- 国际政治禁词（ウクライナ/乌克兰/戦争/战争/ガザ/プーチン/トランプ/ミサイル/核兵器/台湾问题/南シナ海）：svg/ + text.md 全 0×。

## 11. 目视记录

- 印刷 PDF 8 页自渲染（110 dpi，`render/p-1.png` … `p-8.png`）；网页 PDF 8 页自渲染（`render/web-p-1.png` … `web-p-8.png`）。
- P2 词条区 200 dpi 放大（`render/p2-words.png`）：四格逐格目视，均单行完整在米色框内，无溢出；下行例句行清晰无贴靠。
- P8 答案区 200 dpi 放大（`render/p8-answers.png`）：注 48/49/54/63/111/116 逐行清晰可读，拼写与 §8 一致；注 16/25/28/141 释义缩短后与词条框一致。
- 8 页全页已读：无溢出、无重叠、无截断、无压页脚、无豆腐块；网页版 P1/P8 与印刷版版式一致。
- 已知观察项（第一轮复校 O1–O8，本轮沿用；新增 O9 KIT 行数计数、O10 P6 spot 页数字复验说明）：见 PROOF-NOTE.md，均非成品缺陷。
