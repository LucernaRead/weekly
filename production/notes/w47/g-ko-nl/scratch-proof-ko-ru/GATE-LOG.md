# GATE-LOG — W47 ko-ru proof1 独立复校（2026-11-11）

工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-ru/`
（`edition/` 为生产版的 scratch 副本；所有重渲染/重跑只在副本内进行，生产目录只读。）
解释器锁：freeze baseline/diff、run.py、check_core/check_gloss、textmd、boxtitle、keycheck、creambox 均用 **/usr/bin/python3（Pillow 10.2.0 / FreeType 2.13.2）**；render.py、webpdf.py、PyMuPDF 检查用 **tools/venv/bin/python（Pillow 13.0.0）**。
环境探针：`ls /dev/null` 存在；`echo test | git hash-object -w --stdin` 通（`9daeafb9…`）；goals 侧写文件成功。复核中未遇配额问题（`/home/hatch` 83G 已用 / 66G 空闲）。

## 0. 探针与 SHA（复核前）

- 印 `Lucerna-VOL4-KO-RU.pdf` 44,014,545 B，SHA `bcc7eedf64d6d4ac4056e32eb86c40059b20f162dfaa0bd39346df8fa580ffaa` ✓
- 网 `Lucerna-VOL4-KO-RU-web.pdf` 3,985,120 B，SHA `2d553d300fe83f71f3f0cf262cce371754f0b2844b1bf18a0603dced99c062f9` ✓
- text `2026-w47-ko-ru.text.md` 37,195 B，SHA `956b6fccf1d67c0c67159c5525004bda504bf4e56a3e90488bd580a3aed19771` ✓
- `ABSTRACT.txt` 500 B，SHA `c0d5fa6ffcc91fde62ef5fc376fa1a8e80eb1e984492339f6df46f732ae7b214` ✓
- core-ko（复核前）：印 `53bf14ed…a2f27`（46,232,227 B）、网 `9592945a…bc7`（4,232,878 B）、text `da1d3a32…81a`（34,606 B）——与 FANOUT-REPORT-ko3.md 基线一致。

## 1. run.py 重跑 — PASS

- 命令：`cd edition && /usr/bin/python3 run.py`
- 产物：`run-proof.log`；rc=0；`FLOW OVERFLOW` / `HEAD TOO WIDE` 计数 0；TOTAL 150（A2 51 / B1 72 / B2 27；每页 10/18/18/18/18/18/12/38）；`ALL DONE`。

## 2. freeze baseline — PASS，8/8

- 命令：`/usr/bin/python3 tools/freeze.py baseline --build <scratch>/edition --core-svg <prod>/2026-w47-ko-ru/svg --out <scratch>/freeze-out --json freeze-baseline.json`
- 产物：`freeze-baseline.log`、`freeze-baseline.json`（build-copy 已按规清理）。
- 结果：`runtime: /usr/bin/python3 | Pillow 10.2.0 | FreeType 2.13.2`；`baseline: 8/8 SVGs byte-identical`，8 行 OK；`core integrity: shipped core SVGs unchanged`；rc=0。

## 3. freeze diff vs core — PASS，added CJK 7（全 U+3000）

- 命令：`/usr/bin/python3 tools/freeze.py diff --core-svg <core>/svg --edition-svg <prod>/2026-w47-ko-ru/svg --json freeze-diff.json`
- 产物：`freeze-diff.log`、`freeze-diff.json`；rc=0。
- 结果：p1 0，p2–p8 各 1，TOTAL added CJK 7，全部 `\u3000`（footer 分隔符）；与 builder 的 `freeze-diff-ru.log` 逐页一致。

## 4. occlusion audit — PASS，0 flags

- 命令：`/usr/bin/python3 tools/occlusion_audit.py --selftest`；`/usr/bin/python3 tools/occlusion_audit.py --json occlusion.json <scratch>/edition/svg`
- 产物：`occlusion-selftest.log`、`occlusion.log`、`occlusion.json`；rc=0。
- 结果：selftest 6 类全触发 `{BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX}`，干净对照静默；本版 `0 flags`。

## 5. p8.py extract / compare — PASS，150/150，CLEAN

- 命令：`/usr/bin/python3 tools/p8.py extract --p8 <scratch>/edition/svg/p8-siheom.svg --total 150 --json p8-ru.json`；`compare --core-p8 <core>/svg/p8-siheom.svg --edition-p8 <scratch>/edition/svg/p8-siheom.svg --total 150 --json p8-compare.json`
- 产物：`p8-extract.log`、`p8-ru.json`、`p8-compare.log`、`p8-compare.json`；rc=0。
- 结果：extract `noted set = 150 of 150`；compare `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`（E 组重定向，预期）。

## 6. keycheck（150 键）— 内容 150/150；#137 已裁决

- 命令：`/usr/bin/python3 keycheck-proof.py ru`（`keycheck-ko.py` 的复校副本：SCR/ED 指到本工作区，p8 keys 取自自提的 `p8-ru.json`）
- 产物：`keycheck-proof.py`、`keycheck.log`、`ru/p8-ru.json`；rc=1（仅因 #137 的 BAD 行，工具行为与 builder 一致）。
- 结果：`REG 150, SVG keys 150, exact 148, trunc-ok 1 (#150 ✓), BAD 1 (#137)`；逐页 10/18/18/18/18/18/12/37+1（#137  adjudicated）。
- #137 三源核验（见 PROOF-NOTE §2）：源码 `content8.py:69`、P8 SVG 文本元素（x=1439.5, y=2059.8）、交付印 PDF 文字层均含全句 `137. 22 ноября — День кимчхи. — См. страницу 2`；`tools/p8.py detect_note` 按第一个 ` — ` 切分，机制已核对源码。

## 7. 印/网文字层逐字节一致 — PASS，59,120 字节

- 命令：`pdftotext`（无 `-layout`）分别抽取交付印/网 PDF；`cmp`
- 产物：`print-plain.txt`、`web-plain.txt`（各 59,120 B）、`print-ru.txt`、`web-ru.txt`（`-layout`，各 112,373 B）。
- 结果：两种抽取方式下印/网文字层均 `cmp` rc 0；与 builder 的 59,120 B 一致；P8 8 页标记俱全。

## 8. P8 最小字号 — PASS，9.975pt

- 命令：`tools/venv/bin/python <ko3>/p8font.py <prod>/Lucerna-VOL4-KO-RU.pdf`
- 产物：`p8font.log`；rc=0。
- 结果：`region spans 173, min 9.975pt, at-min 168, PASS >=9.75`。

## 9. boxtitle — PASS，8/8

- 命令：`/usr/bin/python3 <ko3>/boxtitle-ko.py <scratch>/edition`
- 产物：`boxtitle.log`；rc=0。
- 结果：`boxtitle: 8/8 within 386.5px`（最宽 366.1px，P3；其余 217.6–350.6px）。

## 10. U+2019 / 孤标点 / 汉字残留扫查 — PASS，全 0

- 命令：自写内联扫查（8 SVG + text.md 的 `‘’“”` 计数；`<text>` 元素首尾孤标点；text.md 汉字计数）
- 产物：`sweeps.log`。
- 结果：U+201C/U+201D/U+2019 = 0/0/0；孤标点候选 0；text.md 汉字字符 0。

## 11. check_core / check_gloss — PASS，rc=0

- 命令：自 patch 副本（`checks/check_core.py`、`checks/check_gloss.py`：BUILD/路径指到 scratch 副本，`译注` 前缀改为 `Пояснение — `，与 builder 的 patch 方式相同）`/usr/bin/python3 check_core.py` / `check_gloss.py`
- 产物：`checks/`、`check-core.log`、`check-gloss.log`；rc=0。
- 结果：gloss fails 0；orphan issues 0；P7 phrases 8/8 verbatim（含新句 #7 (1면)）；日期 D-3/D-1/D-day/김치의 날 及 weekday 全对。

## 12. census / itemgap / §1.1 — PASS

- census：`/usr/bin/python3 <ko3>/census.py <prod>/2026-w47-ko-ru.text.md <scratch>/edition` → `census.log`，rc=0：ex/match 166 项 0 missing；D6 0 missing。
- itemgap：`/usr/bin/python3 <ko3>/itemgap.py <scratch>/edition` → `itemgap.log`，rc=0：core accepted 484（unique 452），ed accepted 482（unique 450），rejected 40 both。
- §1.1：`/usr/bin/python3 <ko3>/style11-ko.py ru` → `style11.log`，rc=0：`style11: OK`（paper/VOL.4/`·`/颜色逐页与 core 一致；hanzi 0；U+2019 0；P7 VOL.5 3→2 按设计）。

## 13. textmd 重导出 — PASS，逐字节一致

- 命令：`cd edition && /usr/bin/python3 textmd.py . 2026-w47-ko-ru <scratch>/textmd-reexport2.md "Lucerna Korean Weekly VOL.4 — Korean text, Russian explanations (2026-W47)"`
- 产物：`textmd-reexport2.md`、`textmd2.log`；rc=0；450 items。
- 结果：SHA `956b6fccf1d67c0c67159c5525004bda504bf4e56a3e90488bd580a3aed19771`，与交付件 `cmp` 一致。
- 注记：首次重跑（`textmd-reexport.md`，`textmd.log`）因我猜的 title_line 与交付件第一行不符，仅此一行不同；已记录在 PROOF-NOTE §6，非版本缺陷。

## 14. creambox 真墨复核 — PASS，0 问题

- 命令：`/usr/bin/python3 creambox-check.py`（自写 v2：锚点 start/middle/end + 顶层矩形判定 + advance 盒蕴含真墨盒）
- 产物：`creambox-check.py`、`creambox.log`；rc=0。
- 结果：奶油底（`#f0eee5`/`#fbfaf6`）矩形 55 个，其上文字 250 段，issues 0。
- 注记：v1 检查器报 16 旗标，经核查全为检查器伪像（未处理 `end` 锚点、纵向窗口过宽、未区分顶层深底矩形）；P1 淡黄标题 `#f6e08e` 与 P6 表头浅字 `#f4efe1` 均坐在深底矩形（`#37402f`）上，属有意设计。canonical occlusion audit 0 flags 佐证。

## 15. 150 题三源手验（印 PDF 第三源）— PASS，150/150

- 命令：`tools/venv/bin/python print-p8-check.py`（自写：REG 取自本版源码 AST；PyMuPDF 取交付印 PDF 第 8 页，空白归一化后逐题比对 `N. key`）
- 产物：`print-p8-check.py`、`print-p8-check.log`；rc=0。
- 结果：`print-P8 check: 150/150 present, BAD 0`；#137、#138 全句逐字命中。

## 16. 印/网 PDF 重渲染验证（仅 scratch 副本）— PASS

- 印：`cd edition && tools/venv/bin/python render.py` → `render-proof.log`，rc=0；重渲染印 PDF 44,014,545 B，SHA `bcc7eedf64d6d4ac4056e32eb86c40059b20f162dfaa0bd39346df8fa580ffaa`，**与交付字节级一致**。
- 网：`tools/venv/bin/python tools/webpdf.py svg <scratch>/web-rerender.pdf` → `webpdf-proof.log`，rc=0；重渲染网 PDF 3,985,120 B，文字层与交付网 PDF `cmp` 一致，8 页（SHA 本就每次不同，不作数）。
- 清理：重渲染产物（副本内两份 PDF、freeze-out build-copy、`cards/`）已删，日志与文本抽取保留；工作区现约 30M。

## 17. 8 页逐页渲染目视 — PASS，8/8 零问题

- 产物：`pages/p-1.png` … `pages/p-8.png`（交付印 PDF，`pdftoppm -png -r 100`，2032×2813）。
- 逐页结论见 PROOF-NOTE §5。观察项（非缺陷）：P8 #138 折行收尾孤字 `4`（同类折行见 #136/#140）；P3 跨栏续句 `확인되지 / 않았어요`；P4/P5 右栏下方空白为版式设计。

## 18. 旧版逐页对比（W46 ko-ru，VOL.3 旧版式）— 无缺陷

- 产物：`pages-w46/p-1.png` … `pages-w46/p-8.png`（`issues/2026-w46/2026-w46-ko-ru/2026-w46-ko-ru.pdf`，100dpi）。
- P1、P8 逐页比对：差异均为有意的版式迁移（W47 新版标准样式 §1.1：书绿+近白新闻纸、VOL.4；W46 为米色纸底+红字俄语副标题行+旧 footer）；P8 结构（A–H 组 + 答案区）同构；无 W46 家具被误带入。

## 19. D5 字体数量（只记录，不判 (b)）

- `Noto Sans CJK SC` 段数：**0**（8 页全 0）。
- 讲解层实际字体 `Noto Sans CJK KR` 段数：P1 67、P2 81、P3 79、P4 71、P5 85、P6 70、P7 68、P8 105，**合计 626**；`Noto Serif CJK KR` 合计 883。

## 20. “next Sunday”冻结规则 — 无适用对象

- `grep -ri "next sunday"` 在 core-ko 全部源码、ko-ru 全部源码、`tools/tables.py` 中 **0 命中**（含二进制文件逐个计 0）。

## 21. SHA 复核（复核后）— 全部未变

- 印 `bcc7eedf…ffaa`、网 `2d553d30…62f9`、text `956b6fcc…9771`、ABSTRACT `c0d5fa6f…214`：与复核前一致。
- core-ko 印 `53bf14ed…a2f27`、网 `9592945a…bc7`、text `da1d3a32…81a`：与复核前一致。
- 无 commit、无 push；`git status` 在本科目（core-ko、ko-ru）无修改（两目录此前即为 untracked；其余 family 的 M 项非本次工作产生）。
