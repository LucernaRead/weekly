# GATE-LOG — W47 zh-cn-ru reproof（fix1 后独立复校）

校对员：独立复校员。对象：`production/2026-w47/2026-w47-zh-cn-ru/`（fix1 后）。
解释器：`tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。全部输出存于本目录。
`TMPDIR` 一律指向本 scratch；凡 import 生产源码均设 `PYTHONDONTWRITEBYTECODE=1`。
重建/重渲均在 scratch 副本中跑（`OUT`/`BASE` 已重定向绝对路径），生产零写入。

## 0. 身份（三 SHA 自算，开工与收尾两次，均与任务书先验及 KIT 一致）

| 文件 | 字节 | SHA-256 | 先验值 | 收尾 |
|---|---|---|---|---|
| Lucerna-VOL4-RU.pdf | 33,572,610 | bcfc550ff96ae87ce46fe1199592f5c7a690b91325dd3d5a410b11d95061305b | 一致 | 一致 |
| Lucerna-VOL4-RU-web.pdf | 2,486,423 | 8d3f72d35d4ac78cb0c9f52f56a930dae1c9251fc3a4527841bc30dd0ac888d3 | 一致 | 一致 |
| 2026-w47-zh-cn-ru.text.md | 60,508 | de12db587c41005301b221cce52ae0d088ec52f9eaccf2338aa94382f00e8094 | 一致 | 一致 |

生产零写入核查：`git status --porcelain` 开工收尾相同（本版目录仅 `??` 未入仓）；
SVG sha256 8/8 与开工快照一致（哈希逐个相同）；`__pycache__` mtime 仍为 2026-11-11 14:30:58。

## 1. gates-zhcn.py 11 门全套自跑

命令：`gates-zhcn.py <edition> ru`（脚本拷入本 scratch，仅改 SCRATCH 指向本目录）。
结果：**rc=0，OVERALL: ALL PASS**。日志 `gates-ru.log`，JSON `gates-ru.json`。

| 门 | 结果 |
|---|---|
| occlusion | rc=0，0 flags（自检另见 §2） |
| img_overlap | hits=0 |
| p8_extract | rc=0，noted=150/150 |
| p8_compare | rc=0，CLEAN，keydiffs=0 |
| freeze_sha256 | run rc=0，match=8/8 |
| print_web_text | 8/8 页，posdiff=0，msdiff=0（P1 355/355、P2 350/350、P3 259/259、P4 336/336、P5 267/267、P6 315/315、P7 478/478、P8 1566/1566；新网 PDF 实测，P1 由 356→355 恰为删去的一词） |
| pdftotext_nonempty | print=52,554 B，web=52,554 B，web_size=2,486,423 |
| p8_fontsize | answer-zone min=9.98 pt，median=9.98 pt，spans=906 |
| p8_chips | core={'A2': 11, 'B1': 24, 'B2': 3}，edition 相同 |
| u2019 | files_with_U+2019=[] |
| s11_svg | off-palette={}，gold/old=False，stroked_rects=0，VOL.5=1（core 1），paper_fills=8 |

## 2. occlusion 自检与 freeze

- `occlusion_audit.py --selftest`：rc=0，**selftest OK**（planted 6 类全触发，clean 对照静默）。日志 `occlusion-selftest.log`。本版 `occlusion_audit.py svg/`：rc=0，**0 flags**。日志 `occlusion.log`。
- `freeze.py diff --strict-cjk`（核心 vs 本版）：rc=0，**TOTAL added CJK characters: 0**。
  逐页：P1 +91/−45、CJK 886→870；P2 +71/−52、1065→1060；P3 +40/−39、864→859；
  P4 +117/−43、772→767；P5 +39/−38、969→964；P6 +114/−41、912→907；
  P7 +338/−105、753→739；P8 +1405/−208、1125→1120；各页 added CJK 均为 0。
  日志 `freeze-diff.log`。
- `freeze.py baseline`（核心，`--build production/2026-w47/core-zh-cn --core-svg …/svg`）：rc=0，
  **8/8 SVGs byte-identical**；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。
  日志 `freeze-baseline.log`，产物 `freeze-baseline/`（仅 scratch 内）。

## 3. run.py scratch 重建（本版，OUT 已重定向）

方法：复制本版 `content*.py + bslib4.py + svglib.py + run.py + render.py + assets/` 到
`<scratch>/rebuild/`，5 个 `content*.py` 的 `OUT` 在副本中重定向为绝对路径
`<scratch>/rebuild/svg`（跑前已验写盘目标；生产文件未动——重建前后生产 SVG sha 与开工快照一致）。
结果：**rc=0；TOTAL 150**（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38）；
`FLOW OVERFLOW` / `HEAD TOO WIDE` 出现 **0 次**；P7 teaser ends **2588.78**（≤2596）；
P8 test flow ends col 3 y=964.8；P8 image ends 1270.6；P8 keys flow ends col 3 y=**2535.1**
（bottom 2560）。重建 SVG 与生产 SVG sha256 **8/8 一致**。日志 `run-rebuild.log`。

## 4. 印 PDF 重渲逐字节比对（scratch 副本，不碰交付）

方法：复制 `render.py + svg/` 到 `<scratch>/rerender/`，`BASE` 在副本中重定向为绝对路径
`<scratch>/rerender`，跑 `render.py`，`cmp` 对交付印 PDF。
结果：**rc=0；重渲印 PDF 33,572,610 B，SHA `bcfc550ff96ae87ce46fe1199592f5c7a690b91325dd3d5a410b11d95061305b`，
与交付印 PDF 逐字节相同（`cmp` 通过）**。日志 `render-rerun.log`。
网 PDF 未重渲（字节不可复现），只比文字层，见 §1 print_web_text（新网 PDF 实测通过）。

## 5. p8.py extract / compare（独立重跑）

- `p8.py extract --p8 <edition>/svg/p8-ceyan.svg --total 150`：**noted set = 150 of 150**。
  日志 `p8extract.log`，JSON `p8extract.json`。
- `p8.py compare --core-p8 <core>/svg/p8-ceyan.svg --edition-p8 <edition>/svg/p8-ceyan.svg
  --total 150`：**CLEAN，missing=[] extra_count=0 uncertain=[] keydiff=[]**（rc=0）。
  日志 `p8compare.log`。

## 6. 150 题 keycheck 与题干对照（自跑）

- `extract_stems.py`：ru 150 条、core 150 条；stem/key/level/type/opts **mismatches 0**。
  注记 149/150 含西里尔字母（Q150 为 f-string 范文）。日志 `stems-ru.log` / `stems-core.log`，
  JSON `stems-ru.json` / `stems-core.json`，对照 `stem-compare.txt`。
- `keycheck.py ru <edition> <scratch>`（REG vs P8 抽取键）：REG 150 条，P8 抽取键 150 条，
  **exact match 149/150**；唯一非精确为 Q150（REG 键 `(开放题，范文如下)`，印刷键 `✓`，开放写作题按设计）。
  日志 `keycheck.log`，JSON `keycheck-150.json`。
  注：keycheck.py 自身 rc=1，只因其硬编码期望英文抽取词 `Open task`；
  俄版抽取值为任务书明定的 `✓`，不属缺陷（proof1 同样记录）。

## 7. D-01 重测三法（修后，交付文件实测）

| 方法 | 墨右 | 盒右 1862.0 | 余量 | 要求 |
|---|---|---|---|---|
| PIL 真墨（新串 19 pt；旧串复现 advance 430.2 / ink_right 1891.5 / −29.5） | 1850.5 | 1862.0 | **+11.5 px** | ≥+5 ✓ |
| 交付印 PDF 150 dpi 渲染像素（3047×4219 px，scale 0.63997 units/px） | 1848.2 units | 1862.0 | **+13.8 units** | ≥+5 ✓ |
| 文字层 PyMuPDF span（印/网一致；旧串 0 命中） | 1850.6 units | 1862.0 | **+11.4 units** | ≥+5 ✓ |

- 盒右缘校准 y=650 处实测 1861.7 units；同盒 18.5 pt 行最右墨 1836.7 units。
- SVG p1 y=1252.0 单 run 新串在位；`content12.py:88` 新串在位，`:86` 长段落 `ещё` 仍在。
- 日志 `measure.log`（PIL+渲染+分%-页字号）、`textlayer-D01.log`（文字层）、
  `svgtexts.log`；渲染 `render-p1-fix1.png`、裁图 `crop-p1-pressline-fix1.png`。

## 8. 几何自测（PIL 真墨，tools/venv）

- `cream_sweep.py` / `cream-sweep.json` / `cream-sweep.log`：全刊 599 个奶油盒内文本元逐个量右缘——
  **溢出 0 处**；贴边（<8 px）**0 处**。纵向奶油盒溢出 **0**；最紧 4 处基线距盒底 5.1 px
  （P6 5.7 px），下行墨 5 px，墨底余 0.1 px（P6 0.7 px），见 PROOF-NOTE O-1。
- 页界 spill：全部文本元 x∈[0,1950]、y∈[0,2700]，**0 处**。
- 孤儿扫描（行首闭合标点 + 同基线左邻判定）：ru **0 处**。日志 `orphan.log`、`text-checks.log`。
- 栏目标题复量：A-head advance 406.3（墨右 494.0、栏右 510.5、余 16.5）；
  P8 D-head advance 417.4（墨右 1406.0、栏右 1411.5、余 5.5）；
  P4 C-head advance 376.6（余 45.5）；P5 C-head advance 376.3（余 46.5）；
  P1 数字标题墨右 941.5（盒右 961、余 19.5）；
  P2 日历标题墨右 1403.0（照片左缘 1439.5、余 36.5）。
- P4 gloss：俄文前缀「Примечания｜」量得 **6 行**（y=595.9–744.5），盒底 792.21，
  下方 GEN 行 y=822.4，净空 30.2 px。
- P8 Q150 键：单基线、**1 行**；键流终值 2535.1（§3）。

## 9. 印/网文字层比对与字号（独立实测）

- `pdftotext`（gates 内）：印 52,554 B / 网 52,554 B；PyMuPDF 逐页位置排序比对：
  8/8 页 posdiff=0 msdiff=0（counts 见 §1 print_web_text 行；新网 PDF 实测）。
- P8 字号（PyMuPDF 独立实测，印/网一致）：P8 最小 **9.98 pt**（最大 34.50 pt）
  ≥ SOP §1.1 底线 9.75 pt；各页最小：P1 10.50、P2–P5 11.62、P6 12.75、P7 11.62、P8 9.98 pt。
  gates 另测 answer-zone median 9.98 pt，spans 906。

## 10. fix 范围核查

- `text.md` vs 修前（fixer `textmd-before.md`）：`diff` **仅 L127 一行**。
- SVG vs 修前快照（fixer `svg-sha-before.txt`）：**仅 p1 变化**
  （`be2231cb…` → `fbe71fe7…`），p2–p8 逐字节一致 7/7。
- `WEEKLY-KIT.md`：Artifacts 一节三 SHA 与盘上交付一致；
  Fix round 1 一节旧三 SHA（印 `7cd883dd…`、网 `ab0aaf10…`、文 `f722ad0f…`）为已取代版本，保留在案。

## 11. 文本层核对

- ABSTRACT.txt 426 B，尾换行在位（`od -c` 末字节 `\n`）。
- 引号配对：SVG 层「“”」2/2、「«»」6/6、ASCII 引号 0；逐行失衡 0。
  （proof1 计「«»」8/8 为 text.md 层；SVG 层 6/6。）
- 禁词：SOP/proofread/cover/lint/占位/内部/geometry audit 全 0；
  「VOL.」SVG 层 14 处与核心等数（VOL.4 10、VOL.5 1）；「第4号」SVG 层 1 处与核心等数。
- CJK 守恒：`CJK(ru) − CJK(core) = ∅`；核心独有仅「英」「解」二字（徽章）。日志 `cjk-diff.log`。
- U+2019：0（.text.md 与 .py 层；gates 0 文件）。
- 「Конструкция:」SVG 层 2 处（P7 句式框标签 y=1109.0 + 句式行 y=1200.1），「Структура:」0 处。
- 金句 8 条各在正文 + P7 出现 2 次。
- D4：中文「第一次」2 处均带「全球总决赛」限定（P4 `:695`、Q56 `:817`）；
  键注 56 俄文带 на Worlds；SVG P4 同句 1 处。D5：「GEN 今年一场没输」0 处；
  「GEN在S16一场没输」P1/P4 在位；「GEN今年 — 淘汰赛一局没输」与核心逐字一致。
- 日期星期（`date -d`，2026）：11月4日周三、5日周四、6日周五、7日周六、8日周日、
  9日周一、11日周三、14日周六、15日周日、21日周六、22日周日；文中星期断言全符
  （8日星期日、9日星期一、11日星期三、14日星期六、15日星期日、21日星期六、22日星期日）；
  P7 俄文注 (вс 15 нояб.)/(вс 22 нояб.)/(сб 21 нояб.) 全对；Q107 选项 A「11月22日星期日」✓。
- 徽章：P1 y=434「КИТАЙСКИЙ ТЕКСТ　ПОЯСНЕНИЯ НА РУССКОМ」，0 中文；
  advance 333.8 px、墨右 422（x=88 起）。

## 12. 目视

- 交付印 PDF 110 dpi 全 8 页（`render/p1–p8.png`）逐页读过 + 网 P1（`render/web-p1.png`）：
  零缺陷；P1 截稿行已收进盒内（裁图 `crop-p1-pressline-fix1.png`）；
  P2 尾行贴边见 PROOF-NOTE O-1（裁图 `crop-p2-tail-reproof.png`，未越出）；
  P8 keys 1–150 + 页脚清；P7 预告条底 2588.78 清页脚。详见 PROOF-NOTE §K。
