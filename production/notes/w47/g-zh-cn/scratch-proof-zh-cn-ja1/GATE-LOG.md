# GATE-LOG — W47 zh-cn-ja proof1（独立自跑）

校对员：独立复校员。对象：`production/2026-w47/2026-w47-zh-cn-ja/`（fan-out #3）。
解释器：`tools/venv/bin/python`（Pillow 13.0.0）。全部输出存于本目录
（`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-cn-ja1/`）。
TMPDIR 指向本目录下 `tmp/`；`PYTHONDONTWRITEBYTECODE=1` 全程。

## 0. 身份（三 SHA 自算，开工与收工两次一致）

| 文件 | 字节 | SHA-256 | 先验值 |
|---|---|---|---|
| Lucerna-VOL4-JA.pdf | 36,336,862 | c395a505f050c4a592f338b1791d44779979b933c1dfc93b85a42070cc4353b6 | 一致 |
| Lucerna-VOL4-JA-web.pdf | 2,900,721 | c620b9eefc22727fd14eb0b1cd249942d26393b94cf768ed219bb19ce74ba65a | 一致 |
| 2026-w47-zh-cn-ja.text.md | 52,444 | 68d850eac576bd5854ba2265ffa9fe69754c2779e01cc0a8ca2cf63b104dd5e4 | 一致 |

## 1. freeze.py diff --strict-cjk（核心 vs 本版）

命令：`freeze.py diff --core-svg production/2026-w47/core-zh-cn/svg --edition-svg
production/2026-w47/2026-w47-zh-cn-ja/svg --strict-cjk --json freeze-diff.json`
结果：**rc=1；TOTAL added CJK characters: 4648**（逐页：P7 +119/−126、CJK 753→1536、
added 787；P8 +696/−271、CJK 1125→2989、added 1884；其余页见 `freeze-diff.log`）。
与 KIT 所载 4648（P7 787 / P8 1884）逐值一致。**预期内**：日语讲解层本身含 CJK，
由汉字 run 守恒裁决（见 §2），不记为失败。日志 `freeze-diff.log`、`freeze-diff.json`。

## 2. 汉字 run 守恒（conserve_ja.py 自跑，builder 同款工具）

命令：`conserve_ja.py core-zh-cn 2026-w47-zh-cn-ja`
结果：**rc=0；仅 2 处缺失，均为 badge 家具**（P1 `简体中文正文`、`英语讲解`）；
P2–P8 0 缺失。核心汉字 run 全守恒（P1 120 distinct / P2 155 / P3 109 / P4 78 /
P5 119 / P6 136 / P7 122 / P8 160）。日志 `conserve-ja.log`。

## 3. freeze.py baseline（核心，现行口径）

命令：`freeze.py baseline --build production/2026-w47/core-zh-cn --core-svg
production/2026-w47/core-zh-cn/svg --out <scratch>/freeze-baseline`
结果：**exit 0；8/8 SVGs byte-identical**；`core integrity: shipped core SVGs
unchanged by the run (8 files re-hashed)`。日志 `freeze-baseline.log`，
产物 `freeze-baseline/`（仅 scratch 内）。

## 4. run.py scratch 重建（本版，OUT 在副本内）

方法：复制本版 `content*.py + bslib4.py + svglib.py + run.py + render.py + assets/`
到 `<scratch>/rebuild/`，改向全部 OUT/BASE 到副本内 `svg/`（改向前 grep 验
`production/2026-w47` 0 残留；改向后 grep 验目标确在 scratch 内），跑 `run.py`。
结果：**exit 0；TOTAL 150**（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38；
题型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1）；
`FLOW OVERFLOW / HEAD TOO WIDE` 出现 0 次；P7 teaser ends 2505.24；P8 keys end 2521.8；
`writing model chars: 138`；**重建 SVG 与生产 SVG sha256 8/8 一致**
（`svg-sha-edition.txt` vs `svg-sha-repro.txt`，diff 空）。日志 `run-rebuild.log`。
⚠️ 事故：首轮 sed 用的展开路径 `/home/hatch/...` 未命中波浪号形式的 OUT，
改向失败后仍跑了 run.py，在生产 `svg/` 原地重写 8 文件——事后快照比对 39 文件
字节全同（见 §14），无害；随后按上法正确改向重跑，本节数值为第二轮干净重建所得。

## 5. p8.py extract / compare

- `p8.py extract --p8 <edition>/svg/p8-ceyan.svg --total 150 --json p8extract.json`：
  **noted set = 150 of 150**。日志 `p8-extract.log`，JSON `p8extract.json`。
- `p8.py compare --core-p8 <core>/svg/p8-ceyan.svg --edition-p8 <edition>/svg/p8-ceyan.svg
  --total 150 --json p8compare.json`：**CLEAN，missing=[] extra_count=0 uncertain=[]
  keydiff=[]**（exit 0）。日志 `p8-compare.log`，JSON `p8compare.json`。
  注：任务先验 keydiff [137,138,139,140] 未出现——Q137–140 为填空题，
  键 `7.77` / `14` / `GEN` / `冷` 在核心与本版逐字相同（keycheck 逐项 MATCH），
  E 组键在两版均为读者语（中文），status CLEAN（见 PROOF-NOTE O-3）。

## 6. occlusion_audit.py

命令：`occlusion_audit.py production/2026-w47/2026-w47-zh-cn-ja/svg --core
production/2026-w47/core-zh-cn/svg --json occlusion.json`
结果：**selftest OK**（6 类 planted 全触发，clean controls 静默）；**本版 0 flags；
核心 0 flags；NEW vs core 0**。日志 `occlusion.log`，JSON `occlusion.json`。
⚠️ 但此 0 旗不覆盖奶油盒内越边（BOXTITLE 只看带 stroke 或 fill `#2c2822` 的 rect，
本版奶油盒为无边框 `#f0eee5`，同 it1 工具缺口）——故另做 §7 纵+横双扫。

## 7. 奶油盒纵扫 + 横扫双法（PIL 真墨 + 交付 PDF 渲染像素）

- `cream_sweep.py` / `cream-sweep.json`：全刊 **544 个奶油盒内文本元逐个量右缘——
  溢出 0 处**，贴边（<8px）0 处。最紧 10 处见 `cream-sweep.json`（最小余 11.5 px）。
  重点标题（源码行 + 实测值）：
  - P1 数字框标题 `数字看本周　今週の数字`（svg p1 x=556.5 y=1117.54, 23pt Bold）：
    墨右 809.5，盒右 961.0，余 **151.5 px**。
  - P5 高频词标题 `这一周的高频词　今週の頻出語`（x=556.5, 23pt Bold）：
    墨右 878.5，盒右 961.0，余 **82.5 px**。
  - P2 日历标题 `本周生活小日历　今週のカレンダー`（x=1007.0, y=237.0, 23pt Bold）：
    墨右 1375.0，盒右 1411.5，余 **36.5 px**。
  - P1 締切行 `締切：11月10日 — 決勝はまだ行われていない`（x=1461.5, y=1252.0, 19pt）：
    墨右 1850.5，盒右 1862.0，余 **11.5 px**（全刊最紧）；同盒上一行墨右 1820.5，余 41.5 px。
- 交付印 PDF 110 dpi 渲染像素复核（`pixel-check.log`；
  奶油底渲染值为 (239,237,228)，PDF 色彩取整所致，非 #f0eee5 原值）：
  P1 締切行墨右 SVG 1849.3（PIL 1850.5），盒右 1862，余 ≈12.7；
  P1 数字框标题墨右 SVG 806.4（PIL 809.5），盒右 961；
  P2 日历标题墨右 SVG 1371.9（PIL 1375.0），盒右 1411.5。
  （P2 初测 1498.5 为山谷照片暗像素，已剔除，限盒内重测。）
  渲染证据：`crop-p1-shimekiri.png`、`crop-p1-numbers-title.png`、`crop-p2-cal-title.png`；
  全版渲染 `render/p-*.png`、网 P1 `render/web-p-1.png`。

## 8. spill / 孤儿扫（自写 orphan_spill.py，4059 元）

- Spill（墨出页界 / 压页脚线 y=2596）：**0**。
- 行首闭合标点孤儿：**0**（修正后）。初版报 1 处候选 P7 `、優勝者）、半决赛`
  （x=175.2, y=304.18）：经核为检测器 artifact——该元为行中续接元，左邻 `(guànjūn`
  墨右 177.0 与其 x=175.2 重叠 1.8 px；核心同基线结构平行
  （`(guànjūn, the champion), ` 在 x=196.8）；左邻容差由 1.0 改为 5.0 px 后重扫为 0。
  日志 `orphan-spill.log`，JSON `orphan-spill.json`。
- 填空 `___` 元：P8 13 处与核心 x/y 全同；P3 Q36/Q37 式空白均为行中元（x=642.5/658.5，
  核心同位同 x），核心继承的观察类，不修不报。

## 9. 印/网文字层比对

- `pdftotext`（默认模式）：印 46,219 B / 网 46,219 B；归一化文本逐字相同。
- gates-zhcn.py 内 PyMuPDF 逐页位置排序比对：8/8 页 posdiff=0 msdiff=0
  （P1 238、P2 257、P3 201、P4 247、P5 203、P6 212、P7 216、P8 908）。

## 10. P8 字号（PyMuPDF 独立实测，render.log）

印 PDF 与网 PDF 均为：P8 最小 **9.98pt**（最大 34.50pt）≥ SOP §1.1 底线 9.75pt；
各页最小：P1 10.50、P2–P5 11.62、P6 12.75、P7 11.62、P8 9.98pt。
gates 另测 answer-zone median 9.98pt，spans 804。

## 11. P8 chips / U+2019 / §1.1 SVG 审计（gates-zhcn.py 内）

- chips：核心 {'A2': 11, 'B1': 24, 'B2': 3}，本版相同。
- U+2019：0 文件（含 .text.md）。
- s11_svg：off-palette={}，无金色/近黑，stroked_rects=0，VOL.5=1（核心亦 1，
  为 P7 下期预告内容引用），paper #fbfaf6 ×8。

## 12. gates-zhcn.py 11 门全套自跑

方法：取 zh-cn-it1 的 `gates-zhcn.py` 拷入本 scratch，仅改 SCRATCH 指向本目录，
跑 `gates-zhcn.py production/2026-w47/2026-w47-zh-cn-ja ja`（PYTHONDONTWRITEBYTECODE=1）。
结果：**rc=0，OVERALL: ALL PASS**——occlusion 0 旗；img_overlap 0；
p8_extract 150/150；p8_compare CLEAN keydiffs 0；freeze_sha256 8/8；
print_web_text 8/8；pdftotext 46,219 B 双份；p8_fontsize 9.98pt；
p8_chips = 核心；u2019 0；s11_svg clean。日志 `gates-ja.log`，JSON `gates-ja.json`。

## 13. 150 题 keycheck（自跑）

方法：取 it1 的 `keycheck.py` + `stub_svg/stub_bslib` 拷入本 scratch，
自写最小 `tr_ja.py`（`TR_JA={'译注｜': '注釈｜'}`，SVG 实测前缀；`NOTE_WRAP_JA='full'`），
跑 `keycheck.py ja <edition> <scratch>`（读本目录 p8extract.json）。
结果：REG 150 条，P8 抽取键 150 条，**exact match 149/150**；唯一非精确为 Q150
（REG 键 `(开放题，范文如下)`，印刷键 `✓`，开放写作题预期内标记）。
日志 `keycheck.log`（其 stub 渲染数 `P7 teaser ends 2394` 为 stub 自身量法，
与真实 run.py 的 2505.24 无关；真实值见 §4），JSON `keycheck-150.json`。
逐题题干配对另见 `reg-dump.txt` / `reg-dump.json`（`regdump.py` 自跑，
REG + 题干逐条导出，150/150 键与题干/正文/图表相符，详见 PROOF-NOTE）。

## 14. 其他自测

- 金句 8 条：SVG joined-text 计数各 2 次（正文 + P7），逐字一致。
- 泄漏扫描：SVG `<text>` 全部拉丁词人工过目，无真实英文残留（保留项见 PROOF-NOTE：
  Level / Sunday, Nov 22 / Worlds / Double 11 / 专名 / 7 处写真署名 / 队名）。
  SIMP_ONLY ['国','学']：12 处含假名 + 国/学元全为日语正词或中文原文，误报。
  “next Sunday”：核心与本版全文检索均为 0 处。
- 范文：自数 138 字（含标点全字符），与 run.py `writing model chars: 138` 一致。
- ABSTRACT.txt：315 B，日语单行，0 ASCII 双引号。
- 徽章：P1 `中国語（簡体字）テキスト　日本語の解説 — 日本語読者のための版`（x=88, y=434, 14pt）。
- D4/D5 SVG/text.md 计数：`GEN在S16一场没输` P1/P4 各 1、`只丢了一小局` P1/P4 各 1、
  `对LYON 2比1` P4 1、`淘汰赛一局没输` P4 1（保留）、`全球总决赛的BO5` P4 2
  （text.md ×2）、旧措辞 `GEN今年一局没输`/`第一次在BO5里打赢T1`（无限定）全刊 0、
  P8 键 56 日语 `BLGはワールズのBO5で初めてT1に勝った`。
- P4 gloss：注釈 5 行（y=595.86–714.76），盒底 762.485，下方 GEN 行 y=822.42，净空；
  核心/it 同盒为 6 行（日语译文更短），4 词条齐全（见 PROOF-NOTE O-2）。
- P2 词卡例句：4 句各 1 行（y=1752.06，19pt），均在卡内（奶油扫覆盖）。
- 日期 `date -d`（America/Toronto）：11-16 星期一、11-22 星期日、11-15 星期日、
  11-21 星期六、11-08 星期日、11-11 星期三、11-14 星期六、11-10 星期二、
  11-04 星期三、11-07 星期六、11-09 星期一——与正文/题面一致。
- 全版渲染目视：`render/p-1.png` … `render/p-8.png`（交付印 PDF 110 dpi 自渲染），
  网 P1 `render/web-p-1.png` 与印版视觉一致。

## 15. 生产零写入核对

- 开工快照 `snapshot-start.txt`（39 文件）→ 收工 `snapshot-end-final.txt`：
  39 个真实文件（全部 .py 来源、SVG、PDF、text.md、KIT、ABSTRACT）**SHA 字节全同**
  （diff 空）。中途 `snapshot-end.txt`（事故后即刻）亦全同。
- `__pycache__/`：仅开工已有的 2 个 .pyc（bslib4 11-11 14:48、svglib 11-11 15:01），
  无新增——全程 `PYTHONDONTWRITEBYTECODE=1`。
- 事故记录：§4 首轮重建误跑生产 SVG（8 文件 mtime 19:24–19:25，字节全同，
  构建确定性所致，无害重写）；git status 仅 `??` 未追踪目录，与开工一致。
