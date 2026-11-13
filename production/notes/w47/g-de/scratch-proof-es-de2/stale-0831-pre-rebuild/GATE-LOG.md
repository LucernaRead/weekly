# GATE-LOG — 2026-W47 es-de 第二轮独立复校（叶子）

复校员：叶子（第二轮独立复校，与 es-de builder / es 核心 builder / 第一轮复校员不同人）
工作目录：~/workspace/weekly-git（clone，main）；笔记目录：~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-de2/
日期：2026-11-11

## 0. 探针与身份核验（自算，SHA-256 与任务书及 WEEKLY-KIT.md 登记逐字一致）
- 探针：`git hash-object -w` 成功；`scratch-proof-es-de2/.probe` 写盘成功。
- print `La-Lucerna-VOL4-es-de.pdf`：3,503,020 B
  SHA-256 `e97c5acc601179bcb629688e146183c6a690e1c381decb0743e13dea96934a72`
- web `La-Lucerna-VOL4-es-de-web.pdf`：852,182 B
  SHA-256 `7760133bec9f34b991de63d24339092fefe4d8bf57454b10f9d27ddb185c767e`
- `2026-w47-es-de.text.md`：1,784 行

## 1. run.py 重跑（副本，scratch-proof-es-de2/run-rerun/）
- rc=0；TOTAL 150；级别 A2 50 / B1 72 / B2 28
- 分版 P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38
- 题型：Sätze vervollständigen 48 / Multiple Choice 47 / Wörter zuordnen 12 / Richtig oder falsch 8 / Sätze bilden 7 / Sätze umformen 10 / Lückentext (Auswahl) 13 / Übersetzen 4 / Schreiben 1
- MODELO：97 词（run log 登记）
- FLOW OVERFLOW 0 次；HEAD TOO WIDE 0 次
- 重跑 8 个 SVG 与成品逐字节一致：8/8（日志 `run-rerun.log`，比对在 `gates-part2.log`）

## 2. freeze（tools/venv 解释器）
- baseline：`8/8 SVGs byte-identical`，rc=0；shipped SVG 跑后未变（core integrity 8 文件重哈希一致；日志 `freeze-baseline.log`）。
- diff（core-es vs es-de）：P1 +27/−38、P2 +50/−51、P3 +33/−30、P4 +34/−27、P5 +44/−47、P6 +19/−17、P7 +46/−46、P8 +161/−626；新增 CJK 合计 1 个 = U+3000 全角空格（SOP §1.1 分隔符；日志 `freeze-diff.log` / `freeze-diff.json`）。与 fix1 GATE-LOG 的预期值逐项一致（P1、P7 各少 2/1 个新增串，正是 fix1 删掉的 3 行德文）。

## 3. 遮挡审计（tools/venv/bin/python）
- 自检六类全触发（selftest OK：BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1，干净对照静默）；本版 0 flags（日志 `occlusion.log`）。
- 盲区人工补位：审计只查文字墨迹、不查矩形。D2（P7 横幅 rect）已人工目视 + SVG 坐标实测：横幅底 2576.51，页脚线 2596，之上 19.49px（见 PROOF-NOTE.md 与 `geometry.log`）。

## 4. p8（`p8-extract.json` / `p8-compare.json`）
- extract：150/150（`p8-extract.json`，文本格式，set=[1..150]）。
- compare vs core-es：CLEAN，missing=[]，extra_count=0，keydiff=[137, 138]
  - 137 键：德语句 “Montag ist der Internationale Flamencotag.”（注 “Vgl. Original.”）
  - 138 键：德语句 “Am Samstag sehen wir das Derby von Sevilla.”（注 “Vgl. Original.”）
  - 裁定：翻译题方向键（139/140 键仍为西语句）沿 W45/W46 ES×EN 裁定，预期内；P8 其余 148 个键与核心版逐字一致。
  - 注：首次 compare 调用误用 `--core` 歧义参数（rc=2），改用 `--core-p8/--edition-p8 --total 150` 后 rc=0。

## 5. 印刷/网页文字层
- pdftotext：print = web = 45,770 字节，逐字节一致（`print.txt` / `web.txt`，`cmp` 通过）。
- web PDF 852,182 B（< 7 MB）。

## 6. P8 最小字号
- pypdf Tm 有效字号（Tf 字号 × Tm 缩放）：149 条目，最小 10.125pt（≥ SOP §1.1 下限 9.75pt；日志 `scans4.log`）。
- 注：首次直取 Tf 字号得最小 1.0pt，系未乘 Tm 缩放的误读；乘缩放后分布与第一轮一致（10.125pt ×8 为最小档）。

## 7. U+2019 / CJK 残留（8 个 SVG 全扫；日志 `scans.log`）
- U+2019：每版 0，总数 0；U+0027 撇号：0 处；全角标点：0 处。
- `<text>` 内 CJK 表意字/假名/韩字：每版 0。
- 仅剩 U+3000 分隔符：P1 21 / P2 16 / P3 13 / P4 15 / P5 14 / P6 14 / P7 12 / P8 14（SOP §1.1 规定，与 fix1 基线逐版一致）。
- .text.md：1,784 行；CJK 表意字 0；U+3000 共 99 个；题号 1–150 齐全。

## 8. 几何复核 D1/D2（送审 SVG 坐标实测；日志 `geometry.log`）
- D1：栏目标题 (538.5, 1658.89)（核心版 1656.84）；Q1 题号 (610.5, 1707.89)（核心版 1705.84）；Q2–Q6 题号 x=1061.0（第 3 栏，与核心版同构）。
- D2：横幅 rect y=2458.51、高 118 → 下缘 2576.51；页脚线 y=2596（之上 19.49px）；核心版下缘 2582.51（本版低 6px）。横幅内文字基线 2502.51 / 2542.51；页脚文字基线 2624。

## 9. 其余核查（日志 `scans.log` / `scans3.log` / `scans4.log`）
- VOL：VOL.4 ×9；VOL.5 ×3（下期预告正当引用）；VOL.3 ×0。
- 禁词：“12 de noviembre”0 次；Ucrania / Rusia / guerra / Trump / Putin / OTAN / Israel / Gaza / Palestina 各 0 次。
- 徽章（白字 A2/B1/B2 文本计数）：P1 10 / P2 15 / P3 18 / P4 15 / P5 18 / P6 18 / P7 12 / P8 35（P8：A2 11 / B1 21 / B2 3）。注：rect 填充色计数不可靠（CINCO CLAVES 色条与 P6 图表共用同色），以白字文本计数为准。
- 金句 8 条：每条在 8 个 SVG 合并文本中恰好出现 2 次。
- 讲解词计数（大小写不敏感）：P1 reflexión 2；P2 mitin/cartel/escaño 各 2；P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 6；P4 parón 2 / liderato 3；P5 papeleta 2 / censo 3 / plazo 3。注：P5 censo 首次大小写敏感计数得 2，漏计 “Oficina del Censo Electoral” 中的大写 Censo；不敏感计数为 3，与 KIT 一致。
- ABSTRACT.txt：德文一行、无 ASCII 双引号、438 字节。
- 日期：`date` 核验 2026-11-09（周一）至 11-29（周日）星期全部吻合。
- fix1 字符串：SVG 中“(15 Tage)”1 次、“(Donnerstag, 19.: letzter Tag)”1 次、“ein Beispielbrief”1 次、“Anmerkung der Redaktion”0 次。

## 10. 目视（从送审 PDF 自行渲染，render/）
- 印刷版 P1–P8（PyMuPDF，100dpi）+ 网页版 P1/P8 逐版目视：除已修 D1、D2 外无问题。
- 渲染工具注：pdftoppm 渲染送审印刷 PDF 时第 5 页段错误（rc=139，单页重跑 rc=1 “Could not write image”）；改用 PyMuPDF（tools venv）8 页全部正常渲染。属 poppler 工具问题，PDF 本身无损坏。
- 核心版对照：核心版 P2/P4/P5 同页渲染（`core-p2.png` / `core-p4.png` / `core-p5.png`），确认 P2-D、P4-B、P5-B 栏目标题跨栏为核心版同构（见 PROOF-NOTE.md O6）。

## 11. 复校结论
- 缺陷 0 条；观察项 6 条（O1–O6，不计缺陷）。
- 回报格式 (a) 零问题。本轮为 SOP §8.4 从头全量复校，定稿决定由协调员做。
