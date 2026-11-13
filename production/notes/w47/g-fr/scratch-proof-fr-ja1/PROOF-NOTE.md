# PROOF-NOTE — W47 fr-ja 独立校对（proof1，re-fanout #2）

- 版：`2026-w47-fr-ja`（目标 fr × 读者 ja），VOL.4，刊期 2026-11-16..22
- 校对员：独立校对员（与 builder、fan-out、协调员均不同）；只读生产文件，**未改任何生产文件、未 commit、未 push**
- 日期：2026-11-11（EST）；Python：仓库 `tools/venv/bin/python`（Pillow 13.0.0）
- 结论：**(a) 零缺陷，可定稿**
- 核心对照：`production/2026-w47/core-fr/`（fix4；三 SHA 已核对，与 KIT 一致）
- 说明：本 scratch 之前留有一份 fan-out #1 的 PROOF-NOTE（结论 (b)，三处孤儿句号 D1–D3 未修；印 SHA `b137834d…` / 30,566,551 B），已归档为 `PROOF-NOTE-fanout1.md` / `GATE-LOG-fanout1.md` 备查。本文件只针对 **re-fanout #2**（下表 SHA），前轮三处缺陷均已修复并由本轮独立实测确认。

## 已核实的文件身份（re-fanout #2，开工前核对，与任务简报一致）

| 文件 | 大小 | SHA-256（实测） |
|---|---|---|
| `La-Lucerna-VOL4-fr-ja.pdf`（印） | 30,565,630 B | `291a514f7980e4a30e0f736d22f3c89c720996f96d83770206d92343e6096f63` |
| `La-Lucerna-VOL4-fr-ja-web.pdf`（网） | 2,309,603 B | `031684fd076ba8e1b3c64ae4f3df17330e10d838650ca2577cd110bc04ab44d3` |
| `2026-w47-fr-ja.text.md`（文） | 47,532 B | `aca654257d25d33d331db2c201724d287e050bdcb288c84057b74c8ef8461498` |
| 核心 fix4 印 PDF | 30,446,975 B | `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d` |
| 核心 fix4 网 PDF | 2,241,835 B | `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141` |
| 核心 fix4 .text.md | 46,471 B | `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df` |

## 缺陷清单

**无。** 本轮未发现缺陷。

## 门禁总表（全部实测值见 GATE-LOG.md）

| # | 门 | 实测 |
|---|---|---|
| ① | run.py 重建 | rc=0，TOTAL 150，0 FLOW OVERFLOW，8/8 SVG 字节一致 |
| ② | freeze | baseline 8/8（rc=0）；diff rc=0，新增 CJK 2329 字全为日文（0 简体独用字） |
| ③ | occlusion | 0 flags（自检 6 类阳性全触发） |
| ④ | p8 | extract 150/150（注记 121/150，双边一致），compare CLEAN，keydiff `[150]`；P8 印出答案 150/150 与登记表 0 差异 |
| ⑤ | 印/网文字层 | 各 102,405 B，7192 tokens，顺序+多重集全同 |
| ⑥ | P8 最小字号 | 11.625pt ≥ 9.75pt（且 ≥ 11.25pt 目标） |
| ⑦ | 盒标题真墨 | PIL 实测 474 个框内文本 0 越边；交付 PDF 像素核查：134 徽章最小边距 27px（150dpi），带条 L 47–54 / R 46px，下期条 L 35 / R 64px |
| ⑧ | 150 题手验 | 题干 123/123 与核心同文（另 5 道翻译题干为读者语设计内差异、逐条手验契合）；键 149/150 与核心同（仅 Q150 写作键为读者语）；.text.md 答案与登记键 0 不符；150 条键+注逐条读过，契合无误 |
| ⑨ | 全页目视 | P1–P8 全页 + 7 处裁图，零问题 |

## re-fanout #2 复核点（逐项独立实测，全部存活）

- **P7 披露框**（`content7.py:117`，框 `p7 y=1878 h=380` → 底 2258.0）：披露文 2 行，末基线 **2233.3**，基线清除 **+24.7**，desc-clear +18.8；PIL 真墨底 **2236.3**（re-fanout 报告所称 2234.4 与本轮实测差 1.9px，系墨迹底口径差异——本轮按整行最大墨迹底计，仍清出盒底 **21.7px**；结论不变）。裁图 `crop-p7-disclosure.png` 目视：两行干净，盒底留白充足。
- **孤儿日文句号 。×3 已修**（前轮 D1–D3）：P1 g1 `primeur　le beaujolais ボジョレー。`（节点 p1 (556.5, 1336.9)，句号在行末节点内）；P4 bridge_comp4 `比較級（plus / moins）で文を完成しよう。`（单行节点 p4 (538.5, 1693.2)，裁图 `crop-p4-bridge2.png` 确认）；P6 bridge_chart `上のカレンダーを読んで答えを選ぼう。`（单行节点 p6 (88.0, 1911.5)，裁图 `crop-p6-bridge2.png` 确认）。全版孤儿标点扫查 **0**（见下）。
- **Q148**：键 `devant le`（`content8.py:170`；登记表；P8 对白题干 `(148)___ cinéma ?`，`content8.py:176` 原为 `({gnums[3]})___ cinéma ?`，无 `du`）；P8 答案区印出 `148. devant le（映画館の前）`；填入后 `On se retrouve devant le cinéma ?` 通顺。
- **Q130 / Q36 / Q37**：Q130 (989.0, 843.0) 与核心坐标全同；Q36 (538.5, 1864.7)、Q37 (538.5, 1997.4) 与核心全同（ja 版在 +0 档，与任务预期一致）。P3 全部 12 处 `___` 节点坐标与核心逐一相同。
- **keydiff `[150]`**：p8.py compare CLEAN，keydiff 仅 Q150（写作键读者语）；Q137–139 键与核心逐字同（法文翻译键）。
- **D7（前轮核心缺陷，已修）**：4 词均在本版法语正文出现（非仅译注）：P1 `Le vainqueur remporte son premier titre`；P4 `Un choc remporté en deux sets`；P6 `navette parlementaire, les allers-retours`、`commission mixte paritaire — sept députés et sept sénateurs`。D8：`avoir lieu` 全版 **0** 处；P7 Q100 语法点为 `en beauté：美しく締めくくる。`（卡面确认）。
- **"next Sunday"**：fr 族 **0** 命中，不触发。

## 日语读者版特别核查

- **新增 CJK 审计**（freeze-diff.json 全量）：新增 2329 字、359 个不同字：假名 116、汉字 230、日文标点 13。简体独用字 **0**（精选约 150 字简体独用表：说/读/语/汉/这/对/发/观/练/线/经……全 0）。无假名语境的 25 个汉字逐字核过，全为标准日语熟语：通算、日常生活、空欄補充、酒蔵、樽、前回優勝者、抽選、上映回、対戦相手、若者、俳優、監督、脚本、観客、基礎、訂正、選択肢、翻訳、一致/無一致、3人称。
- **SIMP_ONLY `['国','学']`**：`国` 在新增集里出现 **0** 次；`学` 出现 1 次，出处为 `学校`（Q129 注）与 `学んでいる`（Q135 题干）——均为日语用法。两者皆为日文新字体共有字，不是缺陷；本轮的简体独用字判定与之无关（见上）。
- **简体中文残留**：.text.md 全文简体独用字扫描 **0**；SVG 新增 CJK 同上；冻结新增汉字 0 之外的新增字全部为日文假名/汉字（来源：读者语讲解层——家具、词表、题干说明、答案注记、P7 金句注、P8 答案注）。
- **字体/tofu**：交付 PDF 文字层无 U+FFFD（0 处）；P1–P8 渲染目视无豆腐块；印/网 token 全同。

## 观察项（非缺陷，不修版、不判 b）

- **O1 — 核心继承的孤儿填空行**（首轮已存在，任务明确不修）：Q130（P8，(989.0, 843.0)）、Q36/Q37（P3，(538.5, 1864.7)/(538.5, 1997.4)）。本版与核心坐标全同；裁图 `crop-p8-q130.png`、`crop-p3-q3637.png` 确认形态与核心一致。
- **O2 — D5（只记录，不修）**：核心 KIT 的 D5 是 P8 徽章补 14 枚（120→134），已在 fix3/4 落地——本版实测徽章 134 枚 [10,12,18,15,14,15,12,38]，A2 50 / B1 65 / B2 19，与登记表 150−16=134 一致。在 fr-ja 范围内未找到任何待修的字体问题（无 tofu、无缺字、渲染干净）；按任务要求仅记录、不作改动。

## 本轮修掉的检测器误报（非版面缺陷，先修检测器、重跑确认）

1. **PIL 真墨锚点错误**：`ImageFont.getbbox` 默认锚点 `la`（上行线）会把墨迹盒整体下移一个 ascent（19px 字约 23px）——首版误报 154 处徽章“越边”（margin_B 统一 −15.0）与 P7 披露框“超盒底”。改 anchor=`ls`（基线相对）后重跑：474 框内文本 0 越边，披露框真墨底 2236.3。occlusion_audit.py 自检 OK 且 0 flags，与修正后结论一致。
2. **孤儿填空行误报 ×2**：首版把 P3 (729.8, 1732.0)（Q35 行内填空，同一基线有题干 `…troisième jeudi. →`）与 P8 (1291.4, 1303.0)（Q129 行内填空，同基线 `(examiner) le texte mercredi. » →`）当成孤行。改按“同一基线无其他文本”判定后重跑：除 Q130/Q36/Q37 外 0 新增。
3. **Q148 跨节点断句误报 ×3**：对白 `On se retrouve (148)___ cinéma ?` 跨两个 SVG 节点、`148. devant le` 在答案区断行——首版按单节点全文匹配误报。改拼接全文（去空格比对）后重跑：三项全过。这是任务提示的 verify_ed 跨行 SVG 句子 artifact 同类。
4. **P8 注记解析渗漏**：首版按 `\u3000` 分块会漏掉换行处丢空格的条目（`22.a`、`vote100.`、`5. 12,7` 数字键等）与 `RÉPONSES` 带标题陷阱（P8 带头本身含 RÉPONSES）。改按“全解答与短い注”定位 + 数字边界（前非数字、后接字母/假名/汉字/数字）分段后重跑：150/150 条目，键 0 差异、注 0 差异。另：纯汉字日语熟语无假名语境属正常日语，假名语境启发式已降为信息项（不作门）。
5. **P1 照片“白色小方块”**：目视疑似 Atget 照片内白方块；核查：SVG 内无任何白色矩形与照片区重叠，渲染像素在照片区内近纯白像素 0 个；200dpi 放大裁图确认是照片本身的墙面招牌（`AU RENDEZ-VOUS des BONS PÊCHEURS` 墙漆字区的小白牌），非版面 artifact。

## 150 题手验方法（机械门禁查不出的键-题干错配，本轮人工覆盖）

- 题干：.text.md 123 条编号题干与核心逐字同（Q135–139 翻译题干为读者语，逐条手验：決勝を見れば…→`Regarder une finale, c'est déjà apprendre le français.`；兄より速く走る。→`Il court plus vite que son frère.`；月曜日から上院の採決を見守っている。→`Nous suivons le vote du Sénat depuis lundi.`；今夜スーツケースを詰める。→`Ce soir, nous allons préparer nos affaires.`；結果はまだ分からない。→`On ne connaît pas encore les résultats.`——均契合）；Q145–149 对白题干在 P8 SVG 拼接全文中核对在位；Q150 写作题干与范文框一致。
- 键：登记表（core vs ja）n/page/level/type/key 仅 Q150 一处差异（写作键读者语，设计内）；.text.md RÉPONSES 150 键与登记键 0 不符；P8 印出键+注 150/150 与登记表 0 差异（去空格比对）。
- 注：150 条日语注记逐条读过（`reg-notes.txt`），键-注契合（词义、日期、票数、语法点均与键一致；Q100 `en beauté`、Q79–84 日程图数字、Q108 事实注均核对无误）。

## 证据文件（本 scratch 目录）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`（逐项实测值）；`PROOF-NOTE-fanout1.md` / `GATE-LOG-fanout1.md`（前轮 #1 归档，结论 (b) 仅对旧 SHA 有效）
- `rebuild-run.log`（run.py rc=0，TOTAL 150）、`prod-svg-sha.txt` / `rebuild-svg-sha.txt`（8/8 字节一致）
- `freeze-baseline.log`（8/8）、`freeze-diff.json` / `freeze-diff.log`（新增 CJK 2329）
- `occlusion.log` / `occlusion.json`（0 flags）、`p8-ed.log` / `p8-core.log` / `p8compare.log`（CLEAN，keydiff [150]）
- `print.txt` / `web.txt`（各 102,405 B，7192 tokens 全同）
- `verify_fr_ja.py` / `verify-fr-ja.log`（fr 适配版门禁脚本，ALL PASS，62 PASS）、`verify_stems.py` / `stem-compare.log`（题干比对）、`dump_reg.py` / `reg-ja.json` / `reg-core.json`（登记表）、`reg-notes.txt`（150 条注记手验底本）、`p8-notes-compare.json`（P8 印出答案 150/150 0 差异）
- `png-print/p1.png`–`p8.png`（交付印 PDF 150dpi 全页渲染）、`png-print/crop-*.png`（P7 披露框、P3 Q36/37、P8 Q130、P1 带头、P1 g1、P4/P6 修复点、P1 照片放大）
- `boxtitle.json`（474 框内文本 PIL 真墨实测）
