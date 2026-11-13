# GATE-LOG — 2026-W47 ja-nl 第一轮返修（D1/D2/D3）· 机械门自跑记录

- 返修 builder：叶子（第一轮返修）｜日期：2026-11-11
- 工作目录：`~/workspace/weekly-git`（main clone）；记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja-nl1/`
- 解释器：`tools/venv/bin/python`（Python 3.12.3；与第一轮复校同一解释器，全程只用它）。
- 修前身份（第一轮复校已核实，与 KIT §8 一致）：印刷 PDF 29,099,171 字节 / `c18c551a…`；网页 PDF 4,476,557 字节 / `e0678a4b…`；文字层 45,989 字节；text.md 45,685 字节、1379 行。

## 0. 开工探针（双通才动手，08:02 UTC）

- `echo probe-ja-nl-fix1 | git -C ~/workspace/weekly-git hash-object -w --stdin` → `1043d7b1f7e73a44ca830703e3521f6f2d9b9ca1`，成功。
- goals scratch `scratch-fix-ja-nl1/.probe` 写盘成功。磁盘 46G 可用。

## 1. run.py 重渲染（runA，在版目录内）

- 命令：`tools/venv/bin/python run.py`（先删 `__pycache__`），日志 `build-runA.log`。
- 结果：**exit 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` 0 行**。
- 登记表：TOTAL 150；级别 A2 48 / B1 73 / B2 29；分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；
  题型 {zinnen aanvullen: 50, meerkeuze: 51, combineren: 12, zinnen bouwen: 8, waar of onwaar: 11, gatentekst: 13, vertalen: 4, schrijven: 1}；
  范文 154 字。——与 KIT 登记逐项一致，与修前一致。
- P8-keys flow 末行 col 3 y=2428（底 2540，余 112px），与修前一致；P8-ex flow 末行 y=531（底 1252）。

## 2. render.py（卡片 PNG + 印刷 PDF）

- 命令：`tools/venv/bin/python render.py`，日志 `render-runA.log`。
- 结果：**exit 0**；8 张卡片全出；印刷 PDF `Lucerna-VOL4-JA-NL.pdf` **29,099,141 字节**（修前 29,099,171，−30），8 页。

## 3. webpdf.py（网页 PDF）

- 命令：`tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-JA-NL-web.pdf`，日志 `webpdf-runA.log`。
- 结果：**exit 0**；`Lucerna-VOL4-JA-NL-web.pdf` **4,476,527 字节**（修前 4,476,557，−30），8 页，45,931 text bytes。

## 4. export（text.md 重导出）

- 命令：`tools/venv/bin/python export-textmd-nl.py`（本版目录内重建的脚本；修前已在修前 SVG 上验证输出与修前 text.md 字节一致）。
- 结果：**exit 0**；`2026-w47-ja-nl.text.md` 1378 行、**45,627 字节**（修前 45,685，−58）。
- diff（修前 text.md 副本 `text-prefixed.md`）：**精确 12 行**——词条框两行并一行 ×2（L212–213、L222–223）、注 16/25/28/141 释义缩短 ×4、注 48/49/54/63/111/116 拼写 ×6；其余 0 差异。

## 5. Freeze（直接 sha256 比对 8/8）

- 方法：版目录构建文件全量复制到 `scratch-fix-ja-nl1/rerun/`（`cp -r`，不保属主；删 `__pycache__`），同一解释器重跑 run.py（runB，日志 `build-runB.log`，rc 0，零溢出，登记表与 runA 一致，P8-keys y=2428）。
- 结果：runA SVG（`sha-runA.txt`）vs runB SVG（`sha-runB.txt`）：**8/8 字节一致**。
- 相对修前（`sha-prefixed.txt`）：**仅 p2、p8 变化**；p1/p3–p7 字节一致。预期内：D1 只改 P2 词条框，D2/D3 注文只画在 P8。
- （注：中途一次 `diff` 因 sha-runB.txt 的路径前缀被坏 sed 污染而误报不一致；已用干净生成的 sha-runB.txt 重比，8/8 一致，并如实记录于此。）

## 6. Occlusion 几何审计（`tools/occlusion_audit.py`）

- 命令：`tools/venv/bin/python tools/occlusion_audit.py <svg dir> --selftest`，再 `--json occlusion.json`。
- 结果：**exit 0；0 flags**。自检先行通过：6 类 planted flags 全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），clean controls 静默。
- 日志：`occlusion-selftest.log`、`occlusion.log`；JSON：`occlusion.json`（flags: []）。
- 另：P2 词条框几何复核——修后 4 条释义基线同为 y=1752.06（框内，底缘 1768），y=1776.76 出现 0×。

## 7. P8 extract + compare（`tools/p8.py`）

- extract：`p8.py extract --p8 …/svg/p8-tesuto.svg --total 150 --json p8-extract.json` → **noted set 150/150**，exit 0。
- compare：`p8.py compare --core-p8 production/2026-w47/core-ja/svg/p8-tesuto.svg --edition-p8 …/svg/p8-tesuto.svg --total 150 --json p8-compare.json`
  → **status CLEAN；missing=[]；extra_count=0；uncertain=[]；keydiff=[137, 138, 139, 140]**，exit 0。
- 150 键逐题复核：新 extract 的 `keys` 与第一轮复校 `proof-p8.json` 的 `keys` 逐键比对——**0 差异**（答案键值全对、未动）；仅注文不同。
- keydiff 137–140 仍为 E 组答案 JA→NL 翻译（与第一轮复校逐条核实一致，未变）。

## 8. print/web 文字层一致

- `pdftotext` 印刷版与网页版：各 **45,931 字节**，`cmp` **字节一致**（`print.txt` / `web.txt`）。修前 45,989，−58。
- 双 PDF 各 8 页（PyMuPDF `page_count`）。网页 PDF 4,476,527 字节 < 7 MB。

## 9. P8 字号（PyMuPDF，印刷 PDF p.8）

- 最小字号 **9.98pt**（答案）≥ 9.75pt 门槛；次档 **10.35pt**（题干，79 spans 档，未动）。
- 尺寸分布（pt）：9.98、10.35、10.88、11.25、11.62、12.75、13.5、14.25、14.62、15.38、15.75、17.25、18.0、18.75、34.5——与第一轮复校逐项一致（修前 9.975pt 为同一值，仅舍入不同）。

## 10. U+2019 缺陷类回归（全扫）

- 8 个 SVG + text.md + content*.py：U+2019 总数 **0**；撇号均为 U+0027。

## 11. 旧拼全版复扫 + 新拼核实

- `Fujiryūga` / `Umi-no-umi` 在 content*.py、svg/（8 个）、text.md 中：**全部 0×**（逐文件 grep -o 计数）。
- 新拼写：P8 SVG `Fujiryōga` ×5、`Chura-no-umi` ×1；双 PDF 文字层（print.txt / web.txt）旧拼各 0×，新拼 48/49/54/63/111/116 六行逐行在位。
- P8 六处改动逐行核实（新 p8 SVG 文本行 + 印刷 PDF 文字层）：
  - `48. B — Chura-no-umi verloor op dag 1 van Hōshōryū`
  - `49. A — Fujiryōga versloeg Hōshōryū op dag 3`
  - `54. 11 — Kinboshi van Fujiryōga: 11e toernooi sinds debuut`
  - `63. ○ — Fujiryōga won een kinboshi op dag 3`
  - `111. 11 — Kinboshi van Fujiryōga: 11e toernooi sinds debuut`
  - `116. A — Hōshōryū verloor op dag 3 van Fujiryōga`
- 47 `Yoshinofuji versloeg Ōnosato op dag 1` 未动。

## 12. §1.1 / 版式 grep 审计（8 个新 SVG）

- `·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×；`Pagina N van 8` 每版 1×；刊头 196px 仅 P1。
- VOL：`VOL.4` ×10，`VOL.3` ×1（P4 冻结正文「前号（VOL.3）」），`VOL.5` ×3（grep；第 4 处分属两个文本节点，复校 O4 同述），`VOL.2` 0×。

## 13. 目视记录

- 印刷 PDF 8 页自渲染（110 dpi，`render/p-1.png` … `p-8.png`）；网页 PDF 8 页自渲染（`render/web-p-*.png`）。
- P2 词条区 200 dpi 放大（`render/p2-words.png`）：四格逐格目视——熊手 `een bamboe hark voor voorspoed`、手締め `vieren met geklap`、解禁 `de dag dat de verkoop begint`、小雪 `wanneer er een beetje sneeuw valt`，均单行完整在米色框内，无溢出；下行例句行清晰无贴靠。
- P2 全页（`render/p-2.png`）与 P8 全页（`render/p-8.png`）已读：无溢出、无重叠、无截断、无压页脚。
- P8 答案区 200 dpi 放大（`render/p8-answers.png`，y≈1600–2420）：注 48/49/54/63/111 逐行清晰可读，拼写与 §11 一致；116 在 SVG 坐标 + 文字层中核实（col 4，y=1341.3，不在该裁图范围内）；注 16/25/28/141 释义缩短后与词条框一致。
- 已知观察项（第一轮复校 O1–O8，未动，非本轮范围）：O1 金句第 6 条出处、O2 两处荷兰语小疵、O3 核心继承版面现象、O4 KIT VOL.5 计数、O5 核心注 47 汉字笔误（nl 不受影响）、O6 备忘与盘上实测出入、O7 FANOUT-REPORT 缺前棒章节、O8 工作树既有 W43 修改——本轮目视/门禁均与修前一致，无变化。

## 14. 新交付物

| Item | Bytes | SHA-256 |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-JA-NL.pdf` | 29,099,141 | `c8b82a8491a0d4c54a01214806cede29188e8f4bf6c81c6cf8a1b3bd5ceafa56` |
| 网页 PDF `Lucerna-VOL4-JA-NL-web.pdf` | 4,476,527 | `7a7f5fc96730e82ba8c6697a9accd10387d6aa84a731f81fe3083310df0f97b8` |
| `2026-w47-ja-nl.text.md` | 45,627 | —（1378 行） |
| 8 SVG | — | 见 `sha-runA.txt`（= runB） |
