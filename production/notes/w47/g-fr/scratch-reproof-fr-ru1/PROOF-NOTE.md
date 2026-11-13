# PROOF-NOTE — W47 fr-ru re-proof（独立全量复校，SOP §8.4）

- 对象：`production/2026-w47/2026-w47-fr-ru/`（fix1 已落地）；核心对照 `production/2026-w47/core-fr/`（fix4 定稿）
- 复校员工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-fr-ru1/`（唯一、专用；全部构建、渲染、日志、裁切均在此；TMPDIR 指向其内 `tmp/`）
- 方法：生产目录只读。源码拷入 scratch `build/` 重建 → 逐字节复现 → 渲染 → 全部工具自跑自验。fix1 的 FIX-LOG / GATE-LOG 仅作方法参考，未照抄任何结论——以下每项均为本次重跑重测的实测值。
- 解释器：`tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）

## 结论：(a) 零缺陷，可定稿

全量复校未发现新缺陷。D1 已修好（双方法独立重测通过）；全部 16 门禁 + 存活项 + 150 题三方手验全部通过；生产零写入。

## 0. 开工 / 收尾核对

| 项 | 开工实测 | 收尾实测 | 结论 |
|---|---|---|---|
| 印 PDF | `0f89cf1590a0ee04bdb75baa73c512c5d6f9b7f0671199a1b8935c8cdfae39f2` / 17,477,392 B | 相同 | 与任务书一致 |
| 网 PDF | `9373b750bc266644cf634f2d65bfc9d9930a9df658486409544775d8e62931e3` / 1,759,960 B | 相同 | 与任务书一致 |
| text.md | `9aa919b7c64738b412484c7d491fedb1d314024779e835584ef13b6c48cf978d` / 50,418 B | 相同 | 与任务书一致 |
| 生产快照（47 文件，大小+路径） | `snapshot-pre.txt` | `snapshot-post.txt`，diff 为空 | 零写入 |
| 生产 SVG SHA（8 个） | `snapshot-svg-pre.sha` | `snapshot-svg-post.sha`，diff 为空 | 零写入 |
| 核心 SVG SHA（8 个） | fix1 收尾快照 | 本次收尾，逐项相同 | 核心未动 |
| 磁盘探针 | `git hash-object -w /dev/null` 成功 + scratch 真实写文件成功 | — | 可写 |

## 1. D1（P3「DATES À RETENIR」奶油盒越边）——已修好，双方法独立重测

- 源码行：生产 `expl.py:121` `dates3_note` = `Нуво выходит в четверг 19-го; праздник — уже вечером в среду 18-го.`；`text.md:439` 同串；核心 `expl.py:122` = `注意：新酒 19 日周四上市，18 日晚已有庆祝活动。`——事实一致（19 日周四上市；18 日晚已有庆祝）。
- PIL 真墨（重建 p3 SVG，Noto Sans CJK SC 19.5pt，`getbbox(anchor="ls")` 逐行实测，`ink-rebuilt.log`）：
  - SVG 实印注文重组：`'Нуво выходит в четверг 19-го; праздник — уже вечером в среду 18-го.'`，与源码完全一致。
  - **2 行**，基线 1911.6 / **1938.9**；末行墨降部 5.00 → **墨底 1943.9**；盒底 1969.6 → **余量 +25.7px**（要求 ≥ +5px）。
  - 末基线 1938.9 与核心同值（核心同注 2 行，末基线 1938.9，墨底 1940.9，余量 +28.7px，`ink-core.log`）。
  - 盒内全部文本最深墨同为 1943.9，无其他越边。
- 交付 PDF 600dpi 像素（交付印 PDF P3，fitz 裁切，`pdf-pixel.log`）：
  - 注 x 范围内盒底（1477.20pt）下 **0 暗像素**；盒内最深暗墨 1457.48pt（= 1943.3 svg px，与 PIL 1943.9 一致，抗锯齿取整差）。
- 目视（`crop-p3-dates.png`，交付印 PDF P3，300dpi 裁切，本人目视确认）：注 2 行全在奶油盒内，末行下有完整一段盒底留白；其下 `POUR OU CONTRE ?` 位置未动。

## 2. 全部门禁实测（逐项值见 GATE-LOG.md）

| # | 门 | 实测值 | 结论 |
|---|---|---|---|
| 1 | build | `run.py` rc=0；FLOW OVERFLOW 0；HEAD TOO WIDE 0；**TOTAL 150**（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42） | 通过 |
| 2 | render | scratch 重建 SVG **8/8 逐字节相同**；重渲印 PDF 与交付印 PDF **SHA 逐字节相同**（`0f89cf15…`，17,477,392 B） | 通过 |
| 3 | webpdf | rc=0；重建网 PDF 1,759,954 B（与交付 1,759,960 B 差 6 B，属已知不可复现字节）；文字层 51,246 B 与交付网 PDF 相同 | 通过 |
| 4 | D1 PIL | 见 §1：2 行，末基线 1938.9，墨底 1943.9，余量 **+25.7px** | 通过 |
| 5 | D1 PDF 像素 | 见 §1：盒底下 **0 暗像素** | 通过 |
| 6 | 奶油盒全版扫描 | 8 页 379 盒内文本，**0 越边**；孤儿启发式命中 432，与 fix1 修前/修后集逐项相同（diff 空）→ **0 新增孤儿** | 通过 |
| 7 | occlusion 审计 | 自检六类全触发；**0 flags**；core 0 flags；NEW vs core 0 | 通过 |
| 8 | p8 extract | rc=0；noted **121/150**（parse: joined）；keys 150 条 | 通过 |
| 9 | p8 compare | rc=0；**CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=**[150]** | 通过 |
| 10 | keycheck-150 | **149/150 精确**；唯一不精确 Q150（抽取截断，见 §4） | 通过 |
| 11 | freeze baseline | **8/8 逐字节相同**（`freeze-baseline.log`；注：fix 时 7/8 是因当时生产仍为修前 p3；现生产已是 fix1，8/8 为正确复校值） | 通过 |
| 12 | freeze diff | p3 **+34/−34**；新增 CJK 总计仍 **15，全 U+3000**（p3 1 个、p8 14 个）；其余 7 页逐项相同 | 通过 |
| 13 | 印/网文字层 | 交付印 vs 交付网：plain 各 **51,246 B 逐字节一致**；`-layout` 各 **107,192 B 逐字节一致**；逐页 1–8 plain+layout 全部一致；重建网 plain 与交付网一致 | 通过 |
| 14 | P8 最小字号 | 印 + 网两版同值：P8 **11.625pt** ≥ 9.75pt；各页最小 11.625–12.75pt | 通过 |
| 15 | §1.1 风格 | 纸 #fbfaf6 8/8 页；rect/text 填色全在调色板；禁用色 0；VOL.4 ×11 + 间隔体 `VOL. 4` ×1（核心同式，见备注）；VOL.5 ×9；可见真实 CJK 字形 0（仅 U+3000 分隔符；`<title>Lucerna 三色蛾</title>` 不渲染）；字体 Newsreader / Noto Serif CJK SC / Noto Sans CJK SC / UnifrakturMaguntia / DejaVu Sans；报头 `Le Lucerna` | 通过 |
| 16 | 变更控制 | 仅 p3 注行 3→2 行；text.md 仅第 439 行一处；生产/核心零写入（见 §0） | 通过 |
| 17 | 盒标题横向真墨扫描 | 379 盒内文本横向 **0 越边**；最差左余量 +16.0px（p5 `REGARDER UN FILM`），最差右余量 +16.5px（p4 `LES PHRASES DU COMMENTATEUR`） | 通过 |

备注（门 15 VOL 计数）：fix1 日志写 `VOL.4 ×12`；本次 XML 解析实测为 11× `VOL.4` + 1× 间隔体 `VOL. 4`（P1 刊别行 `VOL. 4　№ 4`，出自 `expl.py:11` `vol_line`，核心同为 `VOL. 4　总第4期`，属核心继承格式，非差异）。合计 12 处刊次提及，与 fix1 计数一致，无新问题。

## 3. 存活项逐项复测（源码行 + 实测值 + 渲染证据）

| 项 | 源码 / 位置 | 实测值 | 渲染证据 |
|---|---|---|---|
| P7 披露 2 行 | p7 SVG y≈2206/2233 | 基线 2206.0 / **2233.3**，末行墨底 **2238.3**；`survivors.log` S1 | `crop-p7-disclosure.png`：2 行全在奶油盒内，下有留白 |
| Q148 `devant le` | `content8.py` dlg_defs `(A2, "devant le", E["n_g4"])`；`expl.py:335` `n_g4` = `У кинотеатра` | P8 键行 y=1956.1：`148. devant le (У кинотеатра)`；text.md 键行同串 | `crop-p8-keys.png`：`148. devant le (У кинотеатра)` 清晰印出 |
| Q148 题干无独立 `du` | P8 battery y=1226.0–1385.6 六行全文 + text.md §G 对话全文 | 全文无独立 `du`（逐行读过：`— Tu vas au cinéma mercredi ? — Oui, pour voir Hunger Games. — Tu as pris (145)___ ? — Oui, (146)___ billets. — La séance est à (147)___ ? — À 20 heures. — On se retrouve (148)___ cinéma ? — Oui, à 19 h 30. Bon (149)___ ! — Merci !`）；`devant le` 填入成句 `On se retrouve devant le cinéma ?` 语法成立 | P8 SVG 元素逐行摘录见 `survivors.log` S2 |
| Q130 坐标 | P8 SVG (989.0, 843.0) | 元素存在：Newsreader 20.0 `___`（Q130 填空线） | `survivors.log` S3 |
| Q36/Q37 坐标与核心一致 | p3 SVG `36.`/`37.` 编号元 vs 核心 p3 | Q36 1829.0−1799.3 = **+29.7**；Q37 1961.7−1932.0 = **+29.7** | `survivors.log` S4 |
| p8 keydiff | p8 compare | CLEAN，keydiff **[150]**（仅写作题键为读者语，按设计） | `p8-compare.json` |
| 孤儿填空行 | boxscan 孤儿集 | 432 命中与修前/修后逐项相同，0 新增（Q130 孤儿填空行属核心继承观察类，不修） | `orphans-mine.txt` vs `orphans-fixpost.txt` diff 空 |

## 4. 150 题三方手验（REG vs text.md vs P8）

- 字符串三方：REG vs text.md 键 **150/150**；REG vs P8 抽取键 **149/150**；题干编号 text.md 149/150（见下）。
- 唯一不精确 Q150：写作题。p8.py 抽取截断为 `Открытый вопрос`；P8 实印全键已重组核实——y=1996.4 行 `150. Открытый вопрос — баллы в рамке; образец в` + y=2016.5 续行 `рамке на с. 8 (По баллам)`，与 REG 键 `Открытый вопрос — баллы в рамке; образец в рамке на с. 8` 逐字一致；text.md:1083 键行同串。属工具截断，非内容差（`crop-p8-keys.png` 目视：全键两行完整印出）。
- Q150 题干编号：text.md 正文 H ÉCRITURE 写作题无 `150.` 编号，仅键行有编号。核对核心：核心 P8 SVG 同样仅键行有 `150.`，核心 text.md 同样无编号——属核心继承结构，非本版缺陷，不修。
- 语义手验（防三方一致也查不出的键–干错配；逐项读题干 + 选项原文 + 键 вручную判断）：
  - 配对题全部五组（选项字母逐一对定义原文核实）：22–25（P2：a 决定 / b 新酒 / c 丢弃物 / d 决赛，键 a/b/c/d）、49–52（P4：a 弃权 / b 赛程表 / c 抽签 / d 休赛，键 a/b/c/d）、**73–76（P5：a `un film qui raconte l'avant d'une histoire`→73 un prequel；b 短视频→74 une bande-annonce；c 买二手→75 la seconde main；d 修理场所→76 un atelier；键 a/b/c/d）**、85–88（P6：a 参议员 / b 否决 / c 表决 / d 委员会，键 a/b/c/d）、140–144（P8：a 参议员 / b 冠军 / c 抽签 / d 新酒 / e 废弃物，键 a/b/c/d/e）——全部正确。
  - 抽查单题：Q1 `a ___ le Masters` → `gagné`；Q10 决赛 `B. dimanche 22`（22 日为周日，见下）；Q36/37 否定句改写（`On ne boit pas…` / `Le beaujolais n'est pas…`）；Q43 `du saucisson`；Q61 `à Milan`（正文：`Jeudi 12, à Milan, puis dimanche 15, à Bordeaux`）；Q78 `deux`（两张票）；Q79 `B. rejetées`、Q80 `B. 458–0`（P6 图表原文：`Rejet 115–1 des recettes de la Sécu` 23 oct. / `Rejet 458–0 des recettes du budget` 4 nov.；正文 `par 115 voix contre 1` / `458 voix contre, 0 voix pour` 一致）；Q96 `connus`（`ne sont pas encore connus`）；Q108 改错 `vendredi 20` → `jeudi 19`（19 日为周四，见下）；Q125 `A. le journal`（阅读文：`Le matin, ils lisent le journal`）；Q130 未来近式 `Le Sénat va voter mercredi.`；Q145–149 对话键 `des billets / deux / quelle heure / devant le / film` 逐空成句成立；Q150 写作键与 H ÉCRITURE 提示（80–100 词 + 框内评分 + 第 8 版范文）相符。
  - 日期核验（`date -d`，America/Toronto）：2026-11-16 周一、18 周三、19 周四、20 周五、22 周日——与刊期及题干一致。

## 5. 仅记录、不作门、不修

- **D5 字体问题（待用户裁定的范围问题）**：拉丁解释层在 Noto Sans CJK SC。实测：450 个 Noto Sans CJK SC 元素含拉丁字母；该字体内拉丁字母 4,456 个、西里尔字母 5,216 个；构建器字体集根本没有 plain Noto Sans（`svglib.py:22–23` 只载 Noto Sans CJK）；SOP §1.1 字体表称俄语读者讲解层用「Noto Sans」。Noto Sans CJK SC 的拉丁字形是否可接受，属用户裁定范围，本次只记录，不作门、不修。

## 6. 交付文件（本 scratch 内）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`（门禁逐项实测值）
- 日志与证据：`build.log`、`ink-rebuilt.log`、`ink-core.log`、`pdf-pixel.log`、`boxscan.log`、`boxscan-h.log`、`orphans-mine.txt`、`occlusion.log`、`occlusion.json`、`occlusion-selftest.log`、`p8-extract.log`、`p8-extract.json`、`p8-compare.log`、`p8-compare.json`、`keycheck.log`、`keycheck-150.json`、`survivors.log`、`freeze-baseline.log`、`freeze-diff.log`、`freeze-diff.json`、`threeway.log`、`threeway2.log`、`matching-opts.log`、`q73-p5.log`、`p8-minsize.log`、`style11b.log`、`paper-vol.log`、`vol-core.log`、`d5.log`、`render.log`、`webpdf.log`、`snapshot-pre/post.txt`、`snapshot-svg-pre/post.sha`
- 渲染证据：`crop-p3-dates.png`、`crop-p7-disclosure.png`、`crop-p8-keys.png`（均取自交付印 PDF，300dpi）；`render/cards/*.png`（8 页卡片）、`render/La-Lucerna-VOL4-fr-ru.pdf`（与交付逐字节同 SHA）、`render/La-Lucerna-VOL4-fr-ru-web.pdf`（文字层与交付一致）
- 未 commit、未 push；生产目录零写入。
