# GATE-LOG — 2026-W47 nl-it · proof1 机械门实跑记录（delta build-6）

复校员：独立复校（proof1）· 2026-11-11
版目录：`production/2026-w47/2026-w47-nl-it/` · 核心：`production/2026-w47/core-nl/` ·
对照 staging：`production/2026-w47/fanout-nl/2026-w47-nl-it/`
工具：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）；正典 creambox：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383`）
TMPDIR 全程设为本 scratch 的 `tmp/`（系统 /tmp 为 512M tmpfs 且常满，未使用）。
全部构建在 scratch 重建副本（`rebuild/2026-w47-nl-it/`）里跑；输出重定向一律用绝对路径指向
本 scratch，绝未重定向进生产目录。生产零写入（开工/收工快照 diff 为空）。

## §0 探针与身份（开工与收尾两次实测一致）

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29b…` 正常；
  scratch 探针文件 `probe.txt` 写入成功。
- SHA（磁盘实测，见 PROOF-NOTE §0）：
  - 印 PDF `4d297162d9e9f2ac99896ab2cf41865af0588d0d060ad76b89b3a7dabe44da15`，12,667,201 B
  - 网 PDF `15d1b6480e5d3456b527f8f5f2e70b0afd6fa7d90e0b17e9e5ea145ddfe410f6`，1,610,237 B
  - text.md `f1d9e3f58b82e1bc0f9f51c52a1c7e14ac8bb69c87dd60a3d54df44bb44b781b`，47,060 B
  - 结论：三者与任务给定完全一致；收尾复测相同。
- 重建副本开工校验：`cp -a` 后 `diff -r` 干净，三 SHA 与正本一致。

## §1 构建门（scratch 重建副本）

| 门 | 实测值 | 证据 |
|---|---|---|
| `run.py` rc | **0**，TOTAL **150**，by page 10/18/18/18/18/18/12/38，A2 46 / B1 73 / B2 31；FLOW OVERFLOW / HEAD TOO WIDE **0** | `gates/run.log` |
| SVG 重建比对 | 重建 SVG 8/8 与正本 **字节一致** | `gates/run.log` 后续 sha 比对 |
| `render.py` rc | **0**；重建印 PDF 12,667,201 B，SHA = 交付印 PDF（`4d297162…`，字节可复现） | `gates/render.log` |
| `webpdf.py` rc | **0**；重建网 PDF 1,610,233 B（交付 1,610,237 B，−4 B，fontTools 子集非确定性），text bytes 46,510 | `gates/webpdf.log` |
| SVG 变化范围 vs staging | 仅 `p4-sport.svg`（D11）+ `p8-toets.svg`（D9）；其余 6 页字节一致 | §1 下 `diff -rq` |

`diff -rq` staging vs 正本差异文件（共 13 项）：`2026-w47-nl-it.text.md`、
`De-Lucerna-VOL4-nl-it-web.pdf`、`De-Lucerna-VOL4-nl-it.pdf`、`WEEKLY-KIT.md`、`bslib4.py`、
`cards/p4-sport.png`、`cards/p8-toets.png`、`content34.py`、`content56.py`、`content7.py`、
`content8.py`、`svg/p4-sport.svg`、`svg/p8-toets.svg`。与 delta 改动清单一致。

## §2 D6–D11 复核（本版 `wrap()` 0.1px 自测，见 `width-scan.py`）

| 项 | 自测带（0.1px 扫描） | 声称带 | 中点 | 行数/末行 | 结果 |
|---|---|---|---|---|---|
| D6 `w=419.4` | 399.9–439.0 | 399.9–438.9 | 在带内 | 2 行，`agli ausiliari hebben/zijn.` | 通过（上沿差 0.1px 为网格取整） |
| D7 `w=432.7` | 415.5–449.9 | 415.5–449.9 | 在带内 | 3 行，`scoren segnare.`；最宽行 415.5 < 栏宽 422.5 | 通过 |
| D8 `capcn_w=377.7` | 367.4–388.0 | 367.4–388.0 | 在带内 | 4 行，`(100 giovani)` | 通过 |
| D10 `dt_zh_w=388.7` | 343.7–433.7 | 343.7–433.7 | 在带内 | 2 行，`esempio; promessa passata a VOL.5.` | 通过 |

每项均另验：中点断行与交付 SVG 文本一致、拼接还原原文。D9：`content8.py:75` 键、`:76` 题干、
text.md:415 三源逐字一致；text.md vs staging diff 恰 415 行一处（+11 B）。
D11：SVG 盒底 1229.6 / 末基线 1209.49 / 余量 **+20.11px**；PIL 真墨底 1209.74 / **+19.86px**；
交付印 PDF 150dpi 最低墨行 SVG y=1209.53 / **+20.07px**；盒底下 7px 条带 0 非纸像素
（`gates/d11-svg.log`、`d11-rect.log`、`d11-render.log`）。

## §3 occlusion 审计

- `--selftest`（只跑自检）：通过，6 类 planted 全部触发、clean 对照静默（`gates/occlusion-selftest.log`）。
- 正式审计（`occlusion_audit.py production/2026-w47/2026-w47-nl-it/svg --core production/2026-w47/core-nl/svg`）：
  **0 flags，0 new flags**（`gates/occlusion.json`、`gates/occlusion.log`）。
- 盲区记录：BOXTITLE 只覆盖带描边或 `#2c2822` 填充的盒子，奶油盒框标题横向越框不在检查内；
  框标题已用 PIL 真墨 + 交付 PDF 渲染像素另行验证（§7），不单独采信 occlusion。

## §4 正典 creambox.py 全版扫描

命令：`creambox.py production/2026-w47/2026-w47-nl-it/svg/*.svg`（现行 CLI 接受 SVG 文件列表）。
结果：**无真溢出**（`gates/creambox-all.log`）。
- P7 toolbox（HET WOORD / PAS OP! / BRIEVEN VAN LEZERS）：3 盒，最小框内余量 +12.5px、
  最小降部余量 +6.5px。
- 两个 BELOW-WINDOW 负值是下一独立块（P1 `HET WOORD VAN DE WEEK` +24.0；
  P2 `Let op: schrijf je gedicht…` +32.0），非盒内溢出。
- desc-clear 负值两处均为误报，真墨重测（`gates/creambox-trueink.log`，PIL 4×）：
  P2 EN JIJ 末行 `olandese e mandale alla redazione.` 真余量 **+5.34px**（无降部字母）；
  P5 EN JIJ 末行 `due frasi in olandese e mandale.` 真余量 **+5.40px**（无降部字母）；
  P6 图表盒 `(100 giovani)`（含 `g` 降部）真余量 **+3.97px**；
  P2 四词盒 `po' ironica`（`p` 降部）**+7.11px**；P6 `En jij?`（`j` 降部）**+9.75px**。
- creambox 只量纵向 clearance，不量框标题横向溢出——框标题见 §7。

## §5 spill 扫一遍（fix5 法，`spill_creambox.py`，ED 已改指本轮重建副本）

- BELOW/ABOVE 命中 **28** 项，偏移全部 +24.0 ~ +60.0px，逐项 adjudicated：
  全部为独立块（下一栏目头、下一奶油盒标题、图注、照片署名、Nota 盒、练习说明），
  无一是盒内整行漫出；最小 BELOW 偏移 +24.0（P1 `HET WOORD VAN DE WEEK` 栏目头）。
  P4 D11 盒无 BELOW 命中。
- 每奶油盒底下 7px 条带（自 `ceil(bottom)` 起，card PNG）：**全部 0 非纸像素**（26 盒）。
- D11 PIL 真墨：墨底 1209.74，余量 **+19.86px**。
- 结论：**0 spills**（`gates/spill.log`）。

## §6 孤儿扫一遍（fix4 法，`orphan_sweep.py`）

- 1,451 line segments；(a) lone closer **0**；(b) line-initial closer **0**；
  brute-force closer-leading 元素 **0**，leftmost **0**（`gates/orphan.log`）。

## §7 框标题横向真墨扫描（PIL 真墨为准，交付 PDF 渲染像素裁决）

- 集合：粗体 Noto Sans CJK SC ≥21pt 标题 **85** 个（超集；任务所称 56 个无法还原——
  橄榄色奶油盒标题 17 个、奶油盒内含行 25 个、超集 85 个，见 PROOF-NOTE M1）。
  PIL 真墨（本版 svglib 的 `_runs`/`_pil`，4× 绘制）：**OVER 0、TIGHT（余量 <15px）0**。
- 奶油盒标题 17 个：最小 PIL 余量 **+32.0px**
  （`VOOR OF TEGEN?　PRO O CONTRO?` 与 `PAS OP!　CLINICA DEGLI ERRORI` 并列最紧）。
- 交付印 PDF 150dpi 渲染复核（gutter 限窗，避免邻栏墨迹误报）：
  25 个奶油盒内含行全部 fits，最紧渲染余量 **+32.3px**；PIL 与渲染读数一致在 2px 内。
  P7 `HET WOORD　PAROLA`：PIL 墨右缘 1715.1、渲染 1715.1，余 **+146.9px**（build-5 为 +65.9px 溢出，现已消除）。
- `DE WEEK IN CIJFERS　IN CIFRE` 第一版渲染读数 −79.0 为邻栏误报（窗宽伸进第 3 栏正文），
  gutter 限窗重测：渲染墨右缘 903.0，余 **+58.0px**，与 PIL +56.2 一致。
- 结论：**0 越边**（`gates/box-title-scan.log`、`box-title-render2.log`、`headings-scan.json`）。

## §8 p8 compare（显式双路，--total 150）

- `p8.py extract`：noted set **150/150**（`gates/p8-extract-ed.json`）。
- `p8.py compare` core vs edition：**CLEAN**，missing [] extra 0 uncertain []，
  keydiff **[137, 138]**——两项均为翻译题，键按设计用读者语（意大利语 vs 核心的中文释义），非缺陷。
  D9 后 140 已不在 keydiff 中（build-5 为 [137,138,140]）。
- P8 最小字号（PyMuPDF，印 PDF）：**10.12pt**（7,452 字符），≥ SOP §1.1 底线 9.75pt；
  网 PDF P8 最小字号亦为 10.12pt。

## §9 三方比对（自写 `threeway.py`：registry vs text.md vs P8）

- registry：scratch 重建副本跑 content12/34/56/7/8 重建，TOTAL 150（`gates/registry.json`）。
- text.md 解析 150 行；P8 键 150 项。
- 结果：**149/150 MATCH**；唯一差异 Q150 开放写作（registry/text.md
  `(compito aperto, testo modello sotto)` vs P8 `✓`，设计如此）。
- 配对键：25–28 = d/c/a/b，141–144 = b/c/d/a（与核心一致）。
- 语义手验：150 题干-键逐题读过（`gates/qa-table.txt`），0 不一致；
  配对选项内容已从 P2/P8 SVG 核对；Daan 129–132 已与 P8 G 节对话原文核对；
  Q150 范文 81 词已数（`81 parole`）。

## §10 印/网文字层比对（PyMuPDF，0.3pt 容差；只比文字层，未重渲染交付 web PDF）

| 页 | 印 tokens | 网 tokens | msdiff | posdiff |
|---|---|---|---|---|
| P1 | 817 | 817 | 0 | 0 |
| P2 | 826 | 826 | 0 | 0 |
| P3 | 730 | 730 | 0 | 0 |
| P4 | 737 | 737 | 0 | 0 |
| P5 | 806 | 806 | 0 | 0 |
| P6 | 754 | 754 | 0 | 0 |
| P7 | 922 | 922 | 0 | 0 |
| P8 | 2380 | 2380 | 0 | 0 |

- 交付印 PDF vs 交付网 PDF：msdiff 0、posdiff 0，全部 8 页。
- 交付印 PDF vs 本轮重建网 PDF：同样 0/0（8 页）。
- pdftotext：印 46,510 B = 网 46,510 B（KIT line 44 的 46,461 B 是 build-3 历史记录；
  build-6 的 46,510 B 在 KIT line 26 与 line 224 均已正确记录）。
- 斜体（旧 D2）：交付网 PDF 含 `LucernaNewsreader-Italic`，P1 `«de groepswinst»`
  在印/网两版均为 Italic 16.12pt；渲染图确认斜体（`img/crop-p1-italicb.png`）。

## §11 freeze baseline / diff

- baseline 核心（`--build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg`）：
  **8/8 MATCH**（`gates/freeze-core.log`）；核心 shipped SVG 经运行前后复哈希，未被改动。
- baseline 本版自身（`--build production/2026-w47/2026-w47-nl-it --core-svg production/2026-w47/2026-w47-nl-it/svg`）：
  **8/8 MATCH**（`gates/freeze-self.log`）。

## §12 §1.1 风格核对

- 8 版、1950×2700、4 栏；纸色 `#fbfaf6`；调色板全部为 SOP 颜色（墨 `#302c28`、橄榄绿 `#46581f`、
  说明 `#6f675d`、A2 `#5c6e30`、B2/栏目条 `#37402f`、奶油 `#f0eee5`、条上字 `#f4efe1`、
  鹅黄 `#f6e08e`）；无金色/红褐色/近黑底。`#cac8ba` ×3 为深底上的浅色字（P1 头条 gloss、
  P7 下期预告），非违规。
- 字体（`<text>` 计数）：Newsreader 969、Noto Sans CJK SC 643、Noto Serif CJK SC 25、
  UnifrakturMaguntia 1（刊头 `De Lucerna` 196pt）；讲解层用 Noto Sans CJK SC（意大利语读者层），
  符合 §1.1；无思源宋体拉丁字形排西文。
- P8 最小字号 10.12pt（见 §8），让步第 4 步范围内，≥ 9.75pt 底线。
- 弯引号全版扫描：U+2019 **0**、U+0027 **44**、U+201C/U+201D **0**（本版用 « »）。
- text.md E 节 type 标签全意大利语，「翻譯」0 次；ABSTRACT.txt 意大利语单行，含 Lucerna/VOL.4/
  olandese/150 esercizi/A2–B2。

## §13 D5 字体问题（只记录，不作门、不修）

- 字体统计见 §12。纯拉丁-on-CJK 段（本轮口径：CJK 字体 `<text>` 且内容仅拉丁字母/数字/标点/空格，
  含等级徽章）：各页 56/63/55/58/60/62/49/68，合计 **471**（`gates/style-d5.log`）。
  口径与核心 re-proof 的 245 不同，不作比较。

## §14 目视（交付印 PDF 150dpi 渲染，`img/`）

- 整版 `p1.png`–`p8.png` 全部看过：无溢出、重叠、压页脚、图片压字；页脚/页码行正确。
- 裁切确认：P4 D11 盒（`18:45 uur.` 在盒内，留白清晰）、P7 HET WOORD（标题在盒内）、
  P8 Q140 题干与键、P3 D6 桥（2 行）、P7 D7 桥（3 行）、P6 D8 图注（4 行）、P7 D10 来信（2 行）、
  P1 斜体 `«de groepswinst»`、P7 金句 8 条（译文与页码均正确，`un'antica` 直引号紧密无空隙）。
