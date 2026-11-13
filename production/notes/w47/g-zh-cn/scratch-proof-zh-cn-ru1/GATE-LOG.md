# GATE-LOG — W47 zh-cn-ru proof1（独立自跑）

校对员：独立校对员。对象：`production/2026-w47/2026-w47-zh-cn-ru/`（fan-out #3）。
解释器：`tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。全部输出存于本目录。
`TMPDIR` 一律指向本 scratch；凡 import 生产源码均设 `PYTHONDONTWRITEBYTECODE=1`。

## 0. 身份（三 SHA 自算，开工与收尾两次）

| 文件 | 字节 | SHA-256 | 先验值 | 收尾 |
|---|---|---|---|---|
| Lucerna-VOL4-RU.pdf | 33,572,611 | 7cd883dd1b5311e878abc0d8a2a899864c69cdae6b03aed740d738a3a9b19b93 | 一致 | 一致 |
| Lucerna-VOL4-RU-web.pdf | 2,486,444 | ab0aaf106dba13e9b329550b560ad59757d71e528793fdceeb75bbf8955634f6 | 一致 | 一致 |
| 2026-w47-zh-cn-ru.text.md | 60,515 | f722ad0fb0f617bcb54c76afb2163b00f6fc7b9c7af79bc46e3476214717cd3d | 一致 | 一致 |

核心对照 SHA（自算）：印 `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa`、
网 `6b7a12f517749738de2028569556be326aabe00ab556ac3ec8e59cc936a263d9`、
文 `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04`。
生产零写入核查：`git status --porcelain` 开工收尾相同；SVG sha256 8/8 与开工快照一致
（`svg-sha-production-s.txt` vs `svg-sha-end.txt` diff 空）。例外见 PROOF-NOTE O-3：
手工重建曾以同字节内容写回 8 个 SVG（mtime 变、内容零变）。

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
| print_web_text | 8/8 页，posdiff=0，msdiff=0（P1 356/356、P2 350/350、P3 259/259、P4 336/336、P5 267/267、P6 315/315、P7 478/478、P8 1566/1566） |
| pdftotext_nonempty | print=52,561 B，web=52,561 B，web_size=2,486,444 |
| p8_fontsize | answer-zone min=9.98 pt，median=9.98 pt，spans=906 |
| p8_chips | core={'A2': 11, 'B1': 24, 'B2': 3}，edition 相同 |
| u2019 | files_with_U+2019=[] |
| s11_svg | off-palette={}，gold/old=False，stroked_rects=0，VOL.5=1（core 1），paper_fills=8 |

## 2. occlusion 自检与 freeze

- `occlusion_audit.py --selftest`：rc=0，**selftest OK**（planted 6 类全触发，clean 对照静默）。日志 `occlusion-selftest.log`。
- `freeze.py diff --strict-cjk`（核心 vs 本版）：rc=0，**TOTAL added CJK characters: 0**。
  逐页：P1 +91/−45、CJK 886→870；P2 +71/−52、1065→1060；P3 +40/−39、864→859；
  P4 +117/−43、772→767；P5 +39/−38、969→964；P6 +114/−41、912→907；
  P7 +338/−105、753→739；P8 +1405/−208、1125→1120；各页 added CJK 均为 0。
  日志 `freeze-diff.log`。差额定性见 PROOF-NOTE §C（翻译/页脚俄化/重排绕，无 CJK 丢失）。
- `freeze.py baseline`（核心）：rc=0，**8/8 SVGs byte-identical**；
  `core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。
  日志 `freeze-baseline.log`，产物 `freeze-baseline/`（仅 scratch 内）。

## 3. run.py scratch 重建（本版）

方法：复制本版 `content*.py + bslib4.py + svglib.py + run.py + render.py + assets/` 到
`<scratch>/rebuild/` 后跑 `run.py`。**注意**：副本未重定向绝对 `OUT`，8 个 SVG 以
逐字节相同内容写回生产目录（见 PROOF-NOTE O-3；内容 sha 8/8 与开工一致）。
结果：**rc=0；TOTAL 150**（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38）；
`FLOW OVERFLOW` / `HEAD TOO WIDE` 出现 **0 次**；P7 teaser ends **2588.78**（≤2596）；
P8 test flow ends col 3 y=964.8；P8 image ends 1270.6；P8 keys flow ends col 3 y=**2535.1**
（bottom 2560）。重建 SVG 与生产 SVG sha256 **8/8 一致**（gates freeze repro，
已重定向副本）。日志 `run-rebuild.log`。

## 4. p8.py extract / compare（独立重跑）

- `p8.py extract --p8 <edition>/svg/p8-ceyan.svg --total 150`：**noted set = 150 of 150**。
  日志 `p8extract.log`，JSON `p8extract.json`。
- `p8.py compare --core-p8 <core>/svg/p8-ceyan.svg --edition-p8 <edition>/svg/p8-ceyan.svg
  --total 150`：**CLEAN，missing=[] extra_count=0 uncertain=[] keydiff=[]**（rc=0）。
  日志 `p8compare.log`，JSON `p8compare.json`。

## 5. 150 题 keycheck（自跑）

方法：`keycheck.py ru <edition> <scratch>`（tr_ru 为本 scratch 内自建最小 shim，
仅供 gloss 前缀 `Примечания｜` 与 note_wrap；stub 为 it 版同款）。
结果：REG 150 条，P8 抽取键 150 条，**exact match 149/150**；唯一非精确为 Q150
（REG 键 `(开放题，范文如下)`，印刷键 `✓`，开放写作题按设计）。
日志 `keycheck.log`，JSON `keycheck-150.json`。
注：keycheck.py 自身 rc=1，只因其硬编码期望英文抽取词 `Open task`；
俄版抽取值为任务书明定的 `✓`，不属缺陷。题干-键语义逐题手验见 PROOF-NOTE §F
（AST 茎与核心 150/150 全等，`stems-ru.json` / `stems-core.json` / `stem-compare.txt`；
配对题 5 组 20 键逐项对选项原文核对，全对）。

## 6. 印/网文字层比对与字号（独立实测）

- `pdftotext`（gates 内）：印 52,561 B / 网 52,561 B；PyMuPDF 逐页位置排序比对：
  8/8 页 posdiff=0 msdiff=0（ counts 见 §1 print_web_text 行）。
- P8 字号（PyMuPDF 独立实测，印/网一致）：P8 最小 **9.98 pt**（最大 34.50 pt）
  ≥ SOP §1.1 底线 9.75 pt；各页最小：P1 10.50、P2–P5 11.62、P6 12.75、P7 11.62、P8 9.98 pt。
  gates 另测 answer-zone median 9.98 pt，spans 906。

## 7. 几何自测（PIL 真墨，tools/venv）

- `cream_sweep.py` / `cream-sweep.json` / `cream-sweep.log`：全刊 599 个奶油盒内文本元逐个量右缘——
  **溢出 1 处**（PROOF-NOTE D-01：P1 截稿行 y=1252.0，clear **−29.5 px**）；
  贴边（<8 px）0 处。纵向奶油盒溢出 **0**；最紧 4 处基线距盒底 5.1 px（P6 5.7 px），
  下行墨 5 px，墨底余 0.1 px（P6 0.7 px），见 PROOF-NOTE O-1。
- D-01 复核（PIL + 交付印 PDF 150 dpi 渲染像素）：SVG 真墨 ink_right 1891.5 vs 盒右 1862.0；
  核心同位英文行 ink_right 1851.5、余 10.5 px；渲染像素最右墨 1889.2 units、超盒 27.2 units，
  盒右缘像素实测 1861.7 units；段内 18.5 pt 行最右墨 1836.1 units、余 25.9。
  裁图 `crop-p1-pressline.png`、`crop-p2-tail.png`；渲染 `render-p1.png`、`render-p2-150.png`。
- 栏目标题复量：A-head advance 406.3（墨右 494.0、栏右 510.5、余 16.5）；
  P8 D-head advance 417.4（墨右 1406.0、栏右 1411.5、余 5.5）；
  P4 C-head advance 376.6（余 45.5）；P5 C-head advance 376.3（余 46.5）；
  P1 数字标题墨右 941.5（盒右 961、余 19.5）；
  P2 日历标题墨右 1403.0（照片左缘 1439.5、余 36.5）。
- P4 gloss：俄文前缀「Примечания｜」量得 **6 行**（y=595.9–744.5），盒底 792.21，
  下方 GEN 行 y=822.4，净空 30.2 px。
- 行首闭合标点扫描（逐元素 + 同基线左邻判定）：ru **0 处**，核心 **0 处**。
- P8 Q150 键：单基线 y=2519.69、17 runs，**1 行**；键流终值 2535.1（§3）。

## 8. 文本层核对

- ABSTRACT.txt 426 B，尾换行在位（`od -c` 末字节 `\n`）。
- 引号配对：「“”」2/2、「«»」8/8、ASCII 引号 0；逐行失衡 0。
- 禁词：SOP/proofread/cover/lint/占位/内部/geometry audit 全 0；
  「VOL.」6 处与核心等数；「第4号」2 处与核心等数。
- 繁体残留：`CJK(ru) − CJK(core) = ∅`，opencc 残留 0。
- U+2019：0（.text.md 与 .py 层；gates 0 文件）。
- 「Конструкция:」1 处（P7 `:1451`），「Структура:」0 处。
- 金句 8 条各在正文 + P7 出现 2 次（全文 count 均为 2）。
- D4：中文「第一次」2 处均带「全球总决赛」限定（P4 `:695`、Q56 `:817`）；
  键注 56 俄文带 на Worlds；SVG P4 同句 1 处。D5：「GEN 今年一场没输」0 处；
  「GEN在S16一场没输」P1/P4 在位；「GEN今年 — 淘汰赛一局没输」与核心逐字一致。
- 日期星期（`date -d`，2026）：11月4日周三、5日周四、6日周五、7日周六、8日周日、
  9日周一、11日周三、14日周六、15日周日、21日周六、22日周日；文中星期断言全符。
- 徽章：P1 y=434「КИТАЙСКИЙ ТЕКСТ　ПОЯСНЕНИЯ НА РУССКОМ」，0 中文；
  advance 333.8 px、墨右 422（x=88 起）。

## 9. 目视

- 交付印 PDF 110 dpi 全 8 页（`render/p1–p8.png`）逐页读过 + 网 P1（`render/web-p1.png`）：
  除 D-01 外零缺陷；P8 keys 1–150 + 页脚清；P7 预告条底 2588.78 清页脚。
  详见 PROOF-NOTE §I。
