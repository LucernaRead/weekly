# PROOF-NOTE — W47 zh-cn-pt 独立 re-proof（reproof, 2026-11-11）

- **版次**：`production/2026-w47/2026-w47-zh-cn-pt/`（简体中文读者 × 葡萄牙语目标）
- **结论：(a) 零缺陷，可定稿。**
- **复校员**：独立 re-proof（第二轮复校，fix1 之后）
- **工作区**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-zh-cn-pt1/`
  （只读生产；生产文件未改动，未 commit，未 push，未重渲染交付 web PDF）

## 开工三 SHA（开工 19:24 UTC 与收工 19:46 UTC 两次核对，完全一致）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| 印 `Lucerna-VOL4-PT.pdf` | 41,734,802 B | `6644cd43e033e99b27eb02f8bbaca9b470002eb40c9ebac12fed75a73cb7dccb` |
| 网 `Lucerna-VOL4-PT-web.pdf` | 2,647,093 B | `030f52fb82087f8fe13f3465b74ee61b8c02b6e7d8a4740280ff7fa66cac76fa` |
| 文 `2026-w47-zh-cn-pt.text.md` | 50,834 B | `ed0858346f731013dd8b8f6c5d4c85c15a3b6d7eae61099d62e36e3bd9808d94` |

三 SHA 与 `WEEKLY-KIT.md` 所记一致。探针：`git hash-object -w /dev/null` 成功，
scratch 真实写文件成功；`TMPDIR` 全程指向自有 scratch；Python 一律 `tools/venv/bin/python`
（Pillow 13.0.0 / FreeType 2.14.3）；`PYTHONDONTWRITEBYTECODE=1`，生产 `__pycache__`
的 .pyc mtime 仍为 2026-11-11 14:16 UTC（任务开始前），未被触动。

## fix1 三处修复逐项独立重测（PIL 真墨 + 交付印 PDF 150 dpi 像素，双法）

门限 ≥ +5 px（相对奶油盒右缘）。三处均为左锚定、字号不动 23 pt、中文半句未动。

| 项 | 页 | 源码行 | 修复后标题 | PIL 真墨 | 像素法（交付 PDF） | 渲染裁图 |
|---|---|---|---|---|---|---|
| D-01 | P1 | `content12.py:47` `f.box("数字看本周　Números da semana", [` | 数字看本周　Números da semana | 墨 925.5 / 盒缘 961.0，**+35.5 px** | 墨 922.9 / 盒缘 960.6，**+37.8 pt** | `evidence-p1-title.png`（绿线=墨右缘，红线=盒缘，绿在红左） |
| D-02 | P2 | `content12.py:187` `f.box("本周生活小日历　Datas da semana", [` | 本周生活小日历　Datas da semana | 墨 1382.0 / 盒缘 1411.5，**+29.5 px** | 墨 1381.1 / 盒缘 1410.6，**+29.4 pt** | `evidence-p2-title.png` |
| D-03 | P5 | `content56.py:25` `f.box("这一周的高频词　Palavras-chave", [` | 这一周的高频词　Palavras-chave | 墨 912.5 / 盒缘 961.0，**+48.5 px** | 墨 912.6 / 盒缘 960.6，**+48.0 pt** | `evidence-p5-title.png` |

三处实测值与 fix1 声称逐值一致（PIL ±0.0，像素 ±0.0）。三张裁图目视：标题均完整在盒内，
无裁切、无与他元素重叠。P2 标题同时离山谷照有余量（盒缘 1411.5，照片左缘约 1439.5）。

## 同类盲区专项（zh-cn-ru proof1 刚发现的 P1 截稿行越盒类缺陷）

- P1 截稿段（`content12.py:43`，`本期截稿时是11月10日，总决赛还没打……`）逐行 PIL 真墨：
  最紧一行 y=1532.3（`打。谁是冠军？下一期再报。想看决赛的`）墨右缘 520.0，离中栏起点 538.5
  尚有 **+18.5 px**；其余行余量 32.9–299.0 px。**无越栏、无越盒**（该段不在奶油盒内，是左栏正文）。
- 全版奶油盒横向真墨扫（`scan_all.py` + fix1 `sweep.py` 复跑）：**0 flags**；
  每页最紧余量：P1 21.9 / P2 20.5 / P3 19.5 / P4 15.5（`看比赛的中文　Palavras dos jogos`，盒标题，
  仍在盒内）/ P5 30.5 / P6 25.5 / P7 21.3 / P8 无奶油盒。
- P1 数字盒内 8 行正文逐行量过，最紧余量 30.5 px（`11–13 nov. — o pico de encomendas: três`，
  墨 930.5 / 盒缘 961.0）。
- P1/P8 整页 110 dpi 渲染目视（`full-p1-1.png`、`full-p8-8.png`）：版面干净，无溢出、无重叠、
  无裁切字形；P1 徽章 Latin-only（`TEXTO CHINÊS　EXPLICAÇÕES EM PORTUGUÊS`），页脚
  `Lucerna　简体中文周报 VOL.4　LUCERNA — SEMANAL EM CHINÊS SIMPLIFICADO`，`Página 1 de 8`。

## 其他独立核实（均通过；详见 GATE-LOG.md）

- **重建**：scratch 重建 `run.py` RC=0，TOTAL 150（A2 56 / B1 69 / B2 25；
  分页 10/18/18/18/18/18/12/38），0 FLOW OVERFLOW，0 HEAD TOO WIDE；8/8 SVG 字节一致。
- **重渲**：重渲印 PDF 41,734,802 B，SHA 与交付印 PDF **逐字节相同**
  `6644cd43e033e99b27eb02f8bbaca9b470002eb40c9ebac12fed75a73cb7dccb`。
- **freeze**：`freeze.py baseline` 核心 8/8，核心 SVG 未变；`freeze.py diff --strict-cjk`
  TOTAL added CJK **0**；本版自身重建 8/8（上条）。
- **occlusion**：0 flags；自检六类（BOXTITLE / COVER / EDGE / FOOTER / LINEX / TEXTX）全部触发，
  干净对照静默。按任务说明，`boxtitle_rc: 0` 对纯填色 `#f0eee5` 奶油盒为空信号，
  本轮盒标题证据只取 PIL 扫 + 像素扫（上表），不取 occlusion。
- **spill**：页界溢出 0（墨右缘 >1950 或 y 越界 0 项）。
- **孤儿**：P1–P7 橄榄色题号徽章集合与核心**逐页完全相同**
  （P1 10 / P2–P6 各 14 / P7 12）；REG 有号而 SVG 无徽章的 20 项恰为 5 组 `match_set`
  的子项（Q25–28、43–46、61–64、79–82、97–100），核心同结构，**0 新增孤儿**。
- **P8**：`p8.py extract` 150/150；`compare` **CLEAN**，keydiff []；P8 答案区最小字号 **9.98 pt**
  （≥9.75，371 spans，中位 9.98 pt）；chips A2 11 / B1 24 / B2 3 = 核心。
- **150 题三方手验**：REG 150 = 源码 AST 150，对齐 0 错位；键核对 149/150 自动通过，
  Q150 人工重组核实——P8 实印 `150. ✓ Tarefa aberta — a resposta modelo está impressa acima,
  seção F (138 caracteres)` 与 REG note 逐字一致，范文 138 字（`MODELO` 去空格计 138，
  在题目 120~180 字范围内），键流止于 2552.7 < 2560，无截断。故 **150/150**。
  配对题 5 组逐组核对，键均为 a/b/c/d 的排列；单题语义抽查 12 题
  （Q1/Q7/Q9/Q11/Q12/Q24/Q56/Q113/Q114/Q117/Q130/Q149/Q150，见下）全部与正文事实一致。
- **语义抽查要点**：Q11 139.38亿件/22天（text.md:239,1107，且 1107 明言勿与 7.77 混淆）；
  Q12 配送高峰 12–15 日（text.md:243）；Q56 `第一次` 带 `全球总决赛的BO5` 限定
  （text.md:695）；Q114“今年是第20个小雪节气”判错，note 释明“小雪是第20个节气、不是第20个小雪”
  （text.md:489）；Q117 半决赛早上6点（text.md:709）；Q149“先看数据再看广告”（text.md:1117）。
- **D4/D5 在位**：`第一次` 在 text.md 恰 2 处，均带限定（:695 BLG 首次 BO5 赢 T1；:817 同题干）；
  Q56 键注 `pela primeira vez num BO5 dos Worlds` 在位（`content34.py:210`，text.md 2 处，P8 1 处）；
  `今年一场没输` / `今年一局没输` 0 命中。另：`GEN在S16一场没输，只丢了一小局` 与核心同文
  （核心 text.md:697 注 `对LYON 2比1`），非本版引入。
- **#3 修复点全部存活**：P4 C-head `Ler o calendário`（`content34.py:212`，25 pt）；
  P7 三头 `Final e pacotes` / `Hora e datas` / `Ler as notícias`（`content7.py:16/32/48`）；
  P4 gloss 恰 6 行（y 595.9–744.5，`GEN，` 行在其后）；P7 teaser 止于 2588.78；P8 keys 止于 2552.7；
  P2 词卡例句各 1 行（sweep 0 flags 覆盖）。
- **text.md 仅 3 行变化**：新标题恰在 :47、:271、:915 三行；旧标题中仅 `Palavras da semana`
  尚存 1 处（:1315），为 P7  recap 句（KIT 明言不动）；字节 50,846 → 50,834（−12 = −4−3−5，与三次缩短一致）。
- **150 题键未动**：REG 与 proof1 的 `stems.json` 对齐 0 错位；P8 compare CLEAN。
- **日期全验**（`date -d`，America/Toronto）：11月16日星期一 – 11月22日星期日；
  11月8日星期日、11月9日星期一、11月10日星期二（截稿）、11月15日星期日（决赛凌晨3点，
  与范文“星期日凌晨3点”一致）、11月21日星期六（`21 nov., sábado`）、
  11月22日星期日（小雪，`22 nov., domingo`）。“next Sunday”一词在本版与核心均不存在，无可裁定。
- **§1.1**：纸色 `#fbfaf6` ×8；off-palette {}；gold 0；stroked rects 0；VOL.5 仅 1 处 = 核心同数
  （P7 下期预告，合法）；每版 VOL.4 各 1 处；U+2019 0（SVG + text.md）。

## 预期项（非缺陷，按任务说明记）

- **印/网文字层门预期 FAIL**：网 PDF 仍为 fix1 前旧版，带 3 处旧标题。
  实测逐词差分恰为三处标题词而已——P1 print-only `Números, da` / web-only `Esta, em, números`；
  P2 `da` / `desta`；P5 `Palavras-chave` / `Palavras, da, semana`；其余 5 页 posdiff/msdiff 均为 0。
  待全家统一重建网 PDF 后该门自愈；**印 PDF 为权威终稿**，不受影响。

## 观察类（非缺陷，不修不报）

- O-1：配对题（`match_set`）右侧选项按 a–d 与左侧词同序印出，键与释义一一对应、内部一致，
  只是题面不打乱顺序——核心同构（`bslib4.py:230` 共用实现），难度设计问题，非 correctness 缺陷。
- O-2：Q130/Q36/Q37 式孤儿填空行属核心继承的观察类，按任务说明不修不报。
- O-3：生产 SVG 的 mtime 在任务窗内显示为 2026-11-11 19:40–19:41 UTC（另有其他 agent
  在同期活动），但 8/8 SVG 与 19:26 拷贝字节相同，三 SHA 开工收工两次核对无变，
  内容未动；本轮所有写操作只进自有 scratch，生产 `__pycache__` 未触动。
- O-4：`boxtitle_rc: 0`（occlusion）对纯填色奶油盒为空信号，本轮未用作盒标题证据（见上）。

## 缺陷清单

无。结论 (a) 零缺陷，可定稿。
