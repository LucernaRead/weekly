# GATE-LOG — 2026-W47 ja-fr 第一轮返修（D1/D2）· 机械门自跑记录

- 返修 builder：叶子（第一轮返修）｜日期：2026-11-11
- 工作目录：`~/workspace/weekly-git`（main clone）；记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-fr-fix1/`
- 解释器：`tools/venv/bin/python`（Python 3.12.3；与第一轮复校同一解释器，全程只用它）。
- 修前身份（第一轮复校已核实，与 KIT §8 一致）：印刷 PDF 28,347,993 字节 / `5903a36b…`；网页 PDF 4,458,579 字节 / `99fd99af…`；文字层 47,208 字节；text.md 46,880 字节。

## 0. 开工探针（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- goals scratch `scratch-ja-fr-fix1/probe.txt` 写盘成功。

## 1. run.py 重渲染（runA，在版目录内）

- 命令：`tools/venv/bin/python run.py`（先删 `__pycache__`），日志 `build-fix1-runA.log`。
- 结果：**exit 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` 0 行**。
- 登记表：TOTAL 150；级别 A2 48 / B1 73 / B2 29；分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；
  题型 {Compléter: 50, Choix multiple: 51, Associer: 12, Former une phrase: 8, Vrai ou faux ?: 11, Texte à trous: 13, Traduire: 4, Rédaction: 1}；
  范文 154 字。——与 KIT 登记逐项一致，与修前一致。
- P8-keys flow 末行 col 3 y=2411（底 2540，余 129px），与修前一致；P8-ex flow 末行 y=561（底 1252）。

## 2. render.py（卡片 PNG + 印刷 PDF）

- 命令：`tools/venv/bin/python render.py`，日志 `render-fix1-runA.log`。
- 结果：**exit 0**；8 张卡片全出；印刷 PDF `Lucerna-VOL4-JA-FR.pdf` **28,348,000 字节**（修前 28,347,993，+7），8 页。

## 3. webpdf.py（网页 PDF）

- 命令：`tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-JA-FR-web.pdf`，日志 `webpdf-fix1-runA.log`。
- 结果：**exit 0**；`Lucerna-VOL4-JA-FR-web.pdf` **4,458,587 字节**（修前 4,458,579，+8），8 页，601 个 distinct 字符，47,210 text bytes。

## 4. export（text.md 重导出）

- 命令：`tools/venv/bin/python export-textmd-fr.py`（本版目录内重建的脚本；修前已在修前 SVG 上验证输出与修前 text.md 字节一致）。
- 结果：**exit 0**；`2026-w47-ja-fr.text.md` 1350 行、**46,882 字节**（修前 46,880，+2 = `Chura-no-umi` 比 `Umi-no-umi` 长 2 字符）。
- diff（修前 text.md，取自第一轮复校 rerun 副本）：**精确 6 行**——L1264（48）、L1265（49）、L1270（54）、L1279（63）、L1333（111）、L1339（116），其余 0 差异。

## 5. Freeze（直接 sha256 比对 8/8）

- 方法：版目录全量复制到 `scratch-ja-fr-fix1/rerun/`（删 `__pycache__`），同一解释器重跑 run.py（runB，日志 `build-fix1-runB.log`，rc 0，零溢出，登记表与 runA 一致，P8-keys y=2411）。
- 结果：runA SVG（`sha-fix1-runA.txt`）vs runB SVG（`sha-fix1-runB.txt`）：**8/8 字节一致**。
- 相对修前（第一轮复校 `sha-orig.txt`）：**仅 p8 变化**（`fbe9bdb8…` → `6fe4b27f…`）；p1–p7 字节一致。预期内：注文只画在 P8，P4/P7 练习页本身不印注文。
- （注：首次 freeze 复制用了 `cp -a`，因保属主失败返回 1 导致 `&&` 链中断、runB 未真正跑，初版比对是空比对；已如实记录，并用 `cp -r` 重做，第二次为真实两轮构建比对。）

## 6. Occlusion 几何审计（`tools/occlusion_audit.py`）

- 命令：`tools/venv/bin/python tools/occlusion_audit.py <svg dir> --json occlusion-fix1.json`（先 `--selftest`）。
- 结果：**exit 0；0 flags**。自检先行通过：6 类 planted flags 全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），clean controls 静默。
- 日志：`occlusion-selftest.log`、`occlusion-fix1.log`；JSON：`occlusion-fix1.json`。

## 7. P8 extract + compare（`tools/p8.py`）

- extract：`p8.py extract --p8 …/svg/p8-tesuto.svg --total 150 --json p8-extract-fix1.json` → **noted set 150/150**，exit 0。
- compare：`p8.py compare --core-p8 production/2026-w47/core-ja/svg/p8-tesuto.svg --edition-p8 …/svg/p8-tesuto.svg --total 150 --json p8-compare-fix1.json`
  → **status CLEAN；missing=[]；extra_count=0；uncertain=[]；keydiff=[137, 138, 139, 140]**，exit 0。
- 150 键逐题复核：新 extract 的 `keys` 与第一轮复校 `gates/p8-extract.json` 的 `keys` 逐键比对——**0 差异**（答案键值全对、未动）；仅 6 条注文不同（新 SVG 文本行逐条核实，见 §11）。
- keydiff 137–140 仍为 E 组答案 JA→FR 翻译（与第一轮复校逐条核实一致，未变）。

## 8. print/web 文字层一致

- `pdftotext` 印刷版与网页版：各 **47,210 字节**，`cmp` **字节一致**（`print.txt` / `web.txt`）。修前 47,208，+2 = key 48 注文长 2 字符。
- 网页 PDF 4,458,587 字节 < 7 MB。

## 9. P8 字号（PyMuPDF，印刷 PDF p.8）

- 最小字号 **9.98pt**（答案，165 spans）≥ 9.75pt 门槛；次档 **10.35pt**（题干，79 spans）未动。
- 尺寸分布（pt：spans）：9.98:165、10.35:79、10.88:6、11.25:5、11.62:1、12.75:5、13.5:2、14.25:37、14.62:12、15.38:3、15.75:16、17.25:4、18.0:39、18.75:2、34.5:3——与第一轮复校逐项一致。

## 10. U+2019 缺陷类回归（全扫）

- 8 个 SVG + text.md + content*.py + WEEKLY-KIT.md：U+2019 总数 **0**；撇号均为 U+0027（SVG 内 ×51）。

## 11. P8 六处改动逐行核实（新 p8 SVG 文本行）

- `48. B — Chura-no-umi a perdu contre Hōshōryū le jour 1`
- `49. A — Fujiryōga a battu Hōshōryū au jour 3`
- `54. 11 — Kinboshi de Fujiryōga : 11e tournoi depuis le début`
- `63. ○ — Fujiryōga a gagné un kinboshi au jour 3`
- `111. 11 — Kinboshi de Fujiryōga : 11e tournoi depuis le début`
- `116. A — Hōshōryū a perdu contre Fujiryōga au jour 3`
- SVG 内残留：`Fujiryūga` 0×、`Umi-no-umi` 0×；`Fujiryōga` ×5、`Chura-no-umi` ×1。

## 12. §1.1 / 版式 grep 审计（8 个新 SVG）

- `·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×；`Page N sur 8` 每版 1×；刊头 196px 仅 P1。
- VOL：`VOL.4` ×10，`VOL.3` ×1（P4 冻结正文「前号（VOL.3）」），`VOL.5` ×4（P4 冻结正文「次号（VOL.5）」+ P7 法文读者园地 ×2 + P7 预告），`VOL.2` 0×。
- 徽章 chip（60×30 rect，fill 配对）：P1 10×A2、P2 15×A2、P3 7×A2+8×B1、P4 18×B1、P5 18×B1、P6 18×B2、P7 4+4+4、P8 9×A2+22×B1+4×B2；合计 141（A2 45 / B1 70 / B2 26），与第一轮复校逐页一致。

## 13. 目视记录

- 印刷 PDF 8 页自渲染（110 dpi，`render-print/p-1.png` … `p-8.png`）；网页 PDF P1/P8 自渲染（`render-web/web-p1-1.png`、`web-p8-8.png`）。8 版 + 网页 2 页全部读完，无溢出、无重叠、无截断、无压页脚。
- P8 答案区放大核实（`render-print/p8-answers-zoom.png`）：6 处改动逐行清晰可读，拼写与 §11 一致。
- 已知观察项（第一轮复校 O1–O8，未动，非本轮范围）：O1 P7 诊所第 4 条措辞、O2 金句 gloss 第 6 条句首小写、O3 选项折行（核心冻结）、O4 P4 句跨栏在词中切断（核心冻结）、O5 徽章 141 vs 练习 150（Associer 每组 1 枚 chip，核心实现）、O7 P5 D 节头落位与中栏留白（核心版式）——本轮目视均与修前一致，无变化。

## 14. 新交付物

| Item | Bytes | SHA-256 |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-JA-FR.pdf` | 28,348,000 | `1f3b28f4eae5b23c57bf6dac67b976d8e167efd09825ebdcdc10fa9bb9f2fdcb` |
| 网页 PDF `Lucerna-VOL4-JA-FR-web.pdf` | 4,458,587 | `4f02e8c8f9dec50844906ec8c43e0e13520aa98897a49a14685468c6f6dd2b8b` |
| `2026-w47-ja-fr.text.md` | 46,882 | —（1350 行） |
| 8 SVG | — | 见 `sha-fix1-runA.txt`（= runB） |
