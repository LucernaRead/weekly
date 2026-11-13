# GATE-LOG — 2026-W47 ja-fr 第二轮独立复校 · 机械门自跑记录

- 校对员：第二轮独立复校｜日期：2026-11-11
- 工作目录：`~/workspace/weekly-git`（main clone，只读使用；本轮未写仓内任何文件）
- 记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ja-fr2/`
- 解释器：`tools/venv/bin/python`（Python 3.12.3；PyMuPDF 2.1；与第一轮复校、fix1 同一解释器，全程只用它）。
- 复校对象身份（开工核对，与任务书逐字一致）：印刷 PDF 28,348,000 字节 / `1f3b28f4eae5b23c57bf6dac67b976d8e167efd09825ebdcdc10fa9bb9f2fdcb`；网页 PDF 4,458,587 字节 / `4f02e8c8f9dec50844906ec8c43e0e13520aa98897a49a14685468c6f6dd2b8b`；text.md 46,882 字节。

## 0. 开工探针（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- goals scratch `scratch-proof-ja-fr2/PROBE.txt` 写盘成功。
- 磁盘：`df -h` 显示 /home 可用 45G，未遇配额问题。

## 1. run.py 双轮重构建（版目录复制到 scratch 内重跑，交付目录只读）

- 方法：版目录 `cp -r` 两份到 `rerunA/`、`rerunB/`（删 `__pycache__`），同一解释器各跑一次 run.py；交付 SVG 的 sha256 与两轮重跑逐字节比对。
- 结果：**runA rc 0；runB rc 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` 0 行**。
- 登记表（两轮一致）：TOTAL 150；级别 A2 48 / B1 73 / B2 29；分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；题型 {Compléter: 50, Choix multiple: 51, Associer: 12, Former une phrase: 8, Vrai ou faux ?: 11, Texte à trous: 13, Traduire: 4, Rédaction: 1}——与 KIT 登记、fix1 登记逐项一致。
- 日志：`build-runA.log`、`build-runB.log`；SHA：`sha-runA.txt`、`sha-runB.txt`、`sha-delivered.txt`。

## 2. Freeze（8/8 + 与交付件一致）

- runA SVG vs runB SVG：**8/8 字节一致**。
- 交付 SVG vs runA SVG：**8/8 字节一致**（交付件即重构建产物，无漂移）。
- 说明：fix1 曾记 `cp -a` 保属主失败致空比对的教训；本轮用 `cp -r`，两轮均为真实构建。

## 3. Occlusion 几何审计（`tools/occlusion_audit.py`）

- 命令：先 `--selftest`，再对交付 `svg/` 目录跑 `--json occlusion.json`。
- 结果：**exit 0；0 flags**。自检先行通过：6 类 planted flags 全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），clean controls 静默。
- 日志：`occlusion-selftest.log`、`occlusion.log`；JSON：`occlusion.json`。

## 4. P8 extract + compare（`tools/p8.py`）

- extract：`p8.py extract --p8 …/svg/p8-tesuto.svg --total 150 --json p8-extract.json` → **noted set 150/150**，exit 0。
- compare：`p8.py compare --core-p8 production/2026-w47/core-ja/svg/p8-tesuto.svg --edition-p8 …/svg/p8-tesuto.svg --total 150 --json p8-compare.json`
  → **status CLEAN；missing=[]；extra_count=0；uncertain=[]；keydiff=[137, 138, 139, 140]**，exit 0。
- 150 键值与 fix1 的 `p8-extract-fix1.json` 的 `keys` 逐键比对——**0 差异**（答案键值全对、未动）；仅 6 条注文不同（新 SVG 文本行逐条核实，见 PROOF-NOTE 回归节）。

## 5. print/web 文字层一致

- `pdftotext -layout` 印刷版与网页版：各 **104,269 字节**，`cmp` **字节一致**（`print.txt` / `web.txt`）。
  注：fix1 记的 47,210 字节为无 `-layout` 的提取值；本轮两版同法提取、字节一致，结论相同。
- 网页 PDF 4,458,587 字节 < 7 MB；双 PDF 各 8 页，版面 1462.5 × 2025 pt。

## 6. text.md 导出验证（重导出字节一致）

- 命令：在 `rerunA/` 副本内跑 `tools/venv/bin/python export-textmd-fr.py`（rc 0）。
- 结果：输出与交付 `2026-w47-ja-fr.text.md` **cmp 字节一致**（46,882 字节，`wc -l` 1377 行）。
- 日志：`export-rerun.log`。

## 7. P8 字号（PyMuPDF，印刷 PDF p.8）

- 最小字号 **9.98pt**（答案，165 spans）≥ 9.75pt 门槛；次档 **10.35pt**（题干，79 spans）未动。
- 尺寸分布（pt：spans）：9.98:165、10.35:79、10.88:6、11.25:5、11.62:1、12.75:5、13.5:2、14.25:37、14.62:12、15.38:3、15.75:16、17.25:4、18.0:39、18.75:2、34.5:3——与 fix1 逐项一致。
- 记录：`p8-fontsize.txt`。

## 8. U+2019 缺陷类回归（全扫）

- 8 个 SVG + content*.py + text.md + WEEKLY-KIT.md：U+2019 总数 **0**；撇号均为 U+0027（SVG 内 ×51）。

## 9. §1.1 / 版式 grep 审计（8 个交付 SVG）

- `·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×（共 8×）；`Page N sur 8` 每版 1×（共 8×）；刊头 196px 仅 P1。
- VOL：`VOL.4` ×10，`VOL.3` ×1（P4 冻结正文「前号（VOL.3）」），`VOL.5` ×4（P4 冻结正文「次号（VOL.5）」+ P7 法文读者园地 ×2 + P7 预告），`VOL.2` 0×。
- 徽章 chip（60×30 rect，fill 配对）：P1 10×A2、P2 15×A2、P3 7×A2+8×B1、P4 18×B1、P5 18×B1、P6 18×B2、P7 4+4+4、P8 9×A2+22×B1+4×B2；合计 141（A2 45 / B1 70 / B2 26），**fill 配对 0 错配**。
- 中文残留：`参考答案` / `酉之市` / `提名` / `吉伊卡哇` / `译注` 全部 0×。
- ABSTRACT.txt：330 字节（与 EDITION-RECORD 一致），法文单行，无 ASCII 双引号。

## 10. 回归 grep（fix1 的 6 处）

- `Fujiryūga` / `Umi-no-umi` 在 content*.py、svg/、text.md 中 **0×**；仅 WEEKLY-KIT.md 与 EDITION-RECORD.md 以「改前 → 改后」引文形式出现（有意记录）。
- P8 SVG 新拼写：`Fujiryōga` ×5、`Chura-no-umi` ×1；text.md 同样 5+1。
- 6 行原文（SVG 逐字抄录）：
  - `48. B — Chura-no-umi a perdu contre Hōshōryū le jour 1`
  - `49. A — Fujiryōga a battu Hōshōryū au jour 3`
  - `54. 11 — Kinboshi de Fujiryōga : 11e tournoi depuis le début`
  - `63. ○ — Fujiryōga a gagné un kinboshi au jour 3`
  - `111. 11 — Kinboshi de Fujiryōga : 11e tournoi depuis le début`
  - `116. A — Hōshōryū a perdu contre Fujiryōga au jour 3`

## 11. CJK 增量核查（fr vs core-ja SVG 文本）

- 方法：fr 1082 行、core 1062 行；fr-only 293 行、core-only 273 行；core-only 行中无 CJK 的仅 1 行（图注换行残片 `Commons）`，属排版断行差异。
- fr-only 行的 CJK 词串经「全核心文本去空白拼接」核对：**新增 CJK 词串 0 个**。记录：初版按行比对曾报 2 个「缺失」（出来栄え、味わう）——系 SVG 换行把词切在两行所致的测量伪报，拼接核对后两者均在核心正文里（`今年の出来栄えを確かめながら`、`味わいましょう`）。
- 脚本：`check_cjk.py`、`check_stems.py`。

## 12. 目视记录

- 印刷 PDF 8 页自渲染（110 dpi，`render-print/p-1.png` … `p-8.png`）；网页 PDF P1/P8 自渲染（`render-web/w-1.png`、`w-8.png`，另有 w-2…w-7 同批渲染）。8 版 + 网页 2 页全部读完，无溢出、无重叠、无截断、无压页脚。
- P8 答案区 200 dpi 放大核实：`p8-ans-col1.png`（48/49/54/63 清晰）、`p8-ans-col3.png`、`p8-ans-bottom.png`（111 清晰）、`p8-ans-115-121.png`；116 另见整版渲染 + SVG/text.md 原文三重印证，6 处全部清晰可读、拼写与 §10 一致。
- 范文实测 154 字（150–200 字区间内）；Q124 选项经 SVG 原文核实为 A. 2勝1敗 / B. 3勝0敗 / C. 1勝2敗（110 dpi 小图曾误读，新 SVG 文本为准）。

## 13. 新交付物（复核，与任务书一致）

| Item | Bytes | SHA-256 |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-JA-FR.pdf` | 28,348,000 | `1f3b28f4eae5b23c57bf6dac67b976d8e167efd09825ebdcdc10fa9bb9f2fdcb` |
| 网页 PDF `Lucerna-VOL4-JA-FR-web.pdf` | 4,458,587 | `4f02e8c8f9dec50844906ec8c43e0e13520aa98897a49a14685468c6f6dd2b8b` |
| `2026-w47-ja-fr.text.md` | 46,882 | —（1350 行正文，重导出字节一致） |
| 8 SVG | — | 见 `sha-delivered.txt`（= runA = runB） |
