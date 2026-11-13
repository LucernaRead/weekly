# GATE-LOG — W47 zh-cn-it proof1（独立自跑）

校对员：独立复校员。对象：`production/2026-w47/2026-w47-zh-cn-it/`（fan-out #3）。
解释器：`tools/venv/bin/python`（Pillow 13.0.0）。全部输出存于本目录。

## 0. 身份（三 SHA 自算）

| 文件 | 字节 | SHA-256 | 先验值 |
|---|---|---|---|
| Lucerna-VOL4-IT.pdf | 41,730,134 | d1ae6f877573b068e757e12b69a9dcb67dd8fd5242e02d5c10b17b95fd52a001 | 一致 |
| Lucerna-VOL4-IT-web.pdf | 2,641,804 | 75dec91ac806b884bdd4b7cdbdccc39e2c445ff7f668d24ff4365f21f233a512 | 一致 |
| 2026-w47-zh-cn-it.text.md | 50,958 | f954151fb204030d9d273e0f0032d9674509fd9bb170c7fc460c062eec46ecc4 | 一致 |

## 1. freeze.py diff --strict-cjk（核心 vs 本版）

命令：`freeze.py diff --core-svg production/2026-w47/core-zh-cn/svg --edition-svg
production/2026-w47/2026-w47-zh-cn-it/svg --strict-cjk --json freeze-diff.json`
结果：**exit 0；TOTAL added CJK characters: 0**（逐页：P5 +36/−37、CJK 969→964；
P6 +42/−41、912→907；P7 +101/−97、753→748；P8 +205/−209、1125→1120；
各页 added CJK 均为 0）。日志 `freeze-diff.log`、`freeze-diff.json`。

## 2. freeze.py baseline（核心，现行口径）

命令：`freeze.py baseline --build production/2026-w47/core-zh-cn --core-svg
production/2026-w47/core-zh-cn/svg --out <scratch>/freeze-baseline`
结果：**exit 0；8/8 SVGs byte-identical**；`core integrity: shipped core SVGs
unchanged by the run (8 files re-hashed)`。日志 `freeze-baseline.log`，
产物 `freeze-baseline/`（仅 scratch 内）。

## 3. run.py scratch 重建（本版，OUT 在副本内）

方法：复制本版 `content*.py + bslib4.py + svglib.py + run.py + render.py + assets/`
到 `<scratch>/rebuild/`，在副本内跑 `run.py`（其 OUT 为副本自有 `svg/`，
运行前验目标确在 scratch 内；生产 SVG 全程未碰）。
结果：**exit 0；TOTAL 150**（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38；
题型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1）；
`FLOW OVERFLOW / HEAD TOO WIDE` 出现 0 次；P7 teaser ends 2562.26；P8 keys end 2506.4；
**重建 SVG 与生产 SVG sha256 8/8 一致**（`rebuild/svg-sha-before.txt` vs `*-after.txt`，
diff 空）。日志 `run-rebuild.log`。

## 4. p8.py extract / compare

- `p8.py extract --p8 <edition>/svg/p8-ceyan.svg --total 150`：**noted set = 150 of 150**。
  日志 `p8extract.log`，JSON `p8extract.json`。
- `p8.py compare --core-p8 <core>/svg/p8-ceyan.svg --edition-p8 <edition>/svg/p8-ceyan.svg
  --total 150`：**CLEAN，missing=[] extra_count=0 uncertain=[] keydiff=[]**（exit 0）。
  日志 `p8compare.log`，JSON `p8compare.json`。

## 5. occlusion_audit.py

命令：`occlusion_audit.py production/2026-w47/2026-w47-zh-cn-it/svg --core
production/2026-w47/core-zh-cn/svg --json occlusion.json`
结果：**selftest OK**（6 类 planted 全触发，clean controls 静默）；**本版 0 flags；
核心 0 flags；NEW vs core 0**。日志 `occlusion.log`，JSON `occlusion.json`。
⚠️ 但此 0 旗**不覆盖** PROOF-NOTE 的 D-01～D-04：BOXTITLE 只看带 stroke 或
fill `#2c2822` 的 rect（`tools/occlusion_audit.py:471-474`），本版奶油盒为无边框
`#f0eee5`，全盲。见 PROOF-NOTE「工具缺口」。

## 6. 印/网文字层比对

- `pdftotext`（默认模式）：印 44,907 B / 网 44,907 B；归一化文本逐字相同；
  词多重集 4,823 词一致。文件 `print.txt`、`web.txt`。
- gates-zhcn.py 内 PyMuPDF 逐页位置排序比对：8/8 页 posdiff=0 msdiff=0
  （P1 383、P2 377、P3 280、P4 353、P5 279、P6 355、P7 527、P8 1837）。

## 7. P8 字号（PyMuPDF 独立实测）

印 PDF 与网 PDF 均为：P8 最小 **9.98pt**（最大 34.50pt）≥ SOP §1.1 底线 9.75pt；
各页最小：P1 10.50、P2–P5 11.62、P6 12.75、P7 11.62、P8 9.98pt。
gates 另测 answer-zone median 9.98pt，spans 369。

## 8. P8 chips / U+2019 / §1.1 SVG 审计（gates-zhcn.py 内）

- chips：核心 {'A2': 11, 'B1': 24, 'B2': 3}，本版相同。
- U+2019：0 文件（含 .text.md）。
- s11_svg：off-palette={}，无金色/近黑，stroked_rects=0，VOL.5=1（核心亦 1，
  为 P7 下期预告内容引用），paper #fbfaf6 ×8。

## 9. gates-zhcn.py 11 门全套自跑

方法：把 builder 的 `gates-zhcn.py` 拷入本 scratch，仅改 SCRATCH 指向本目录
（不写他人 scratch），跑 `gates-zhcn.py production/2026-w47/2026-w47-zh-cn-it it`。
结果：**rc=0，OVERALL: ALL PASS**——occlusion 0 旗；img_overlap 0；
p8_extract 150/150；p8_compare CLEAN keydiffs 0；freeze_sha256 8/8；
print_web_text 8/8；pdftotext 44,907 B 双份；p8_fontsize 9.98pt；
p8_chips = 核心；u2019 0；s11_svg clean。日志 `gates-it.log`，JSON `gates-it.json`。
⚠️ 11 门全绿仍未拦下 D-01～D-05（同 §5 工具缺口；孤儿 "》" 亦无对应机械门）。

## 10. 150 题 keycheck（自跑）

方法：取 scratch-fanout-de 的 `keycheck.py` + `stub_svg/stub_bslib/tr_it` 拷入本
scratch，stub 补 `Flow.glossline` 与 `Flow.ci`（zh-cn 内容模块所用、本 stub 缺失），
跑 `keycheck.py it <edition> <scratch>`（读本目录 p8extract.json）。
结果：REG 150 条，P8 抽取键 150 条，**exact match 149/150**；唯一非精确为 Q150
（REG 键 `(开放题，范文如下)`，印刷键 `✓`，开放写作题预期内标记）。
日志 `keycheck.log`，JSON `keycheck-150.json`。
逐题题干配对另见 `reg-dump.txt` / `reg-dump.json`（`regdump.py` 自跑，
REG + 题干逐条导出，150/150 键与题干/正文/图表相符，详见 PROOF-NOTE）。

## 11. 几何自测（PIL 真墨，tools/venv）

- `measure.py` / `measure.json`：P1 数字框标题墨右 1007.5（盒右 961.0，越 46.5）；
  A-head 全串 advance 377.1（栏余 45.5）；P2 日历标题 advance_end 1424.3
  （照片余 15.2，但盒右 1411.5，越 12.5）；Chiusura 行1 墨右 1805.5（余 56.5），
  行2 墨右 1880.5（盒右 1862.0，越 18.5）；P8 D-head advance 407.8（栏余 14.5）。
  三处 builder 数值（377.1 / 407.8 / 1424.3）与我方实测分毫不差，量法已对表。
- `cream_sweep.py` / `cream-sweep.json`：全刊 522 个奶油盒内文本元逐个量右缘——
  **溢出 4 处**（D-01～D-04），贴边 1 处（P4 盒标题余 6.5 px，通过）。
- 行首闭合标点扫描（逐元素 + 同基线左邻判定）：全刊仅 1 处行首闭合标点——
  P1 数字框孤儿 "》"（D-05）；核心 0 处。P3/P6 "”"、P7 "」"、P4 "），八强"
  均为行中且与核心同位。
- P4 gloss：`Note｜` 起 6 行（y=595.9–744.5），盒底 792.2，下方 GEN 行 y=822.4，净空。
- P2 词卡例句：4 句各 1 个 `<text>`，19pt，对 378.5 px 卡内宽余 27.0/11.2/12.6/142.9 px。
- 核心对照：核心同位标题/行全部通过（余 289.5/243.5/243.5/56.4/10.2 px），
  D-01～D-04 确为 fan-out 引入。
- 渲染证据（交付印 PDF 110 dpi + 网 PDF P1）：`crop-p1-numbers-title.png`、
  `crop-p1-chiusura.png`、`crop-p1-numbers-box.png`、`crop-p2-cal-title.png`、
  `crop-p5-freq-title.png`、`crop-web-p1-numbers-title.png`；全版渲染 `render/p-*.png`、
  网 P1 `render/web-p-1.png`。

## 12. 其他自测

- 金句 8 条：SVG joined-text 计数各 2 次（正文 + P7），逐字一致。
- 泄漏扫描：SVG `<text>` 全部拉丁词频人工过目，无真实英文残留（保留项见 PROOF-NOTE）。
- 范文：自数 138 字，与 run.py `writing model chars: 138` 一致。
- ABSTRACT.txt：319 B，意大利语单行，0 ASCII 双引号。
- 徽章：P1 `TESTO CINESE　SPIEGAZIONI IN ITALIANO` 拉丁-only（x=88, y=434, 14pt）。
- D4/D5 SVG 计数：`GEN在S16一场没输` P1/P4 各 1、`只丢了一小局` P1/P4 各 1、
  `对LYON 2比1` P4 1、`淘汰赛一局没输` P4 1（保留）、`全球总决赛的BO5` P4 2、
  旧措辞 `GEN今年一局没输`/`第一次在BO5里打赢T1`（无限定）全刊 0、
  P8 键 56 意大利语 `per la prima volta in un BO5 dei Worlds` 1。

## 13. 生产零写入核对

- 开工快照 `snapshot-start.txt`（41 文件）→ 收工：39 个真实文件
  （全部 .py 来源、SVG、PDF、text.md、KIT、ABSTRACT）**SHA 字节全同**
  （`snapshot-start-real.txt` vs `snapshot-end-real.txt`，diff 空）。
- 事故记录：keycheck/regdump 导入生产 .py 时，Python 在生产目录
  `__pycache__/` 写了 5 个新 .pyc；清理时我误删了开工已有的
  bslib4/svglib 2 个 .pyc，已用同一解释器 `py_compile` 重编恢复
  （`bslib4.cpython-312.pyc`、`svglib.cpython-312.pyc` 均已回位）。
  但新编字节与原文件 SHA 不同（原字节已无法恢复：无备份、未入 git；
  尺寸相同但 hash 不同，推测原文件由不同编译上下文生成）。
  .pyc 仅为 gitignored 的 Python 导入缓存，不属交付物、未入 git，
  Python 下次导入即按源码重建；39 个真实文件零写入已验。
  教训：以后凡 import 生产源码一律先 `PYTHONDONTWRITEBYTECODE=1`，
  或只在副本里 import。
