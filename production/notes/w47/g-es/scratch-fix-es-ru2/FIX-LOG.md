# FIX-LOG — es-ru boxtitle 回归修复（fix-es-ru2，2026-11-12）

- 任务：协调员 #4 派修 2026-w47-es-ru 的 1 处 boxtitle 右溢（P1）。只修本版。
- 缺陷来源：`scratch-sweep-xru-occl-2/SWEEP-LOG.md`——P1 [TITLE] 'цифрах' +22.3px 右溢（core −18.0，回归；ink_r 983.3，框右界 961.0；overlap=None，clip=False）。occlusion 0 flags。
- 工作目录：本目录 `hidden_files/w47/scratch-fix-es-ru2/`；构建目录 `production/2026-w47/2026-w47-es-ru/`。

## 修法

- 仅降字号，不改措辞：`content12.py:46`，`f.box("LA SEMANA EN CIFRAS　В цифрах", …)` 加 `tsize=21`（默认 23pt）。
- 选型实测（`measure_title.py`，工具自带 ink 数学，框右界 961.0，标题起笔 556.5）：
  23pt ink_r 986.1（+25.1px，与扫查 +22.3px 一致，量级相同）；22pt 966.6（+5.6px，仍溢）；21pt 949.1（余 11.9px）；20pt 929.5（余 31.5px）。
  22pt 不够，故取 21pt——循 de-fr 的 D5 先例（同类 Newsreader 变宽标题 23→21pt）。
- 措辞未动 → text.md 无需重导出（L89 `LA SEMANA EN CIFRAS　В цифрах` 不变）。

## 重建

- `run.py` rc=0，TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE（`build-run.log`）。
- `render.py` rc=0，印 + 网一次生成（`build-render.log`）。
- SVG diff vs 修前（`pre-svg.sha256`）：仅 p1-portada.svg 变，p2–p8 字节一致。

## 新旧 SHA

| PDF | 修前 | 修后 |
|---|---|---|
| 印 `La-Lucerna-VOL4-es-ru.pdf` | 3,100,942 B，`277b2d2695f8…` | 3,100,944 B，`d383753b48628ce402c7c91d082e8596f7d8472c93eb21acbe84f6c2938fe5f5`（+2 B） |
| 网 `La-Lucerna-VOL4-es-ru-web.pdf` | 950,829 B，`985368280784…` | 950,823 B，`b6246122f94d949c61cd67aec16ee17194355981d486a8fd8b3b020db56bb544`（−6 B） |
| text.md | 52,367 B，`ac246f8709…` | 未变 |

## 门禁逐项（全绿）

| 门 | 证据 | 结果 |
|---|---|---|
| run.py 零溢出 | `build-run.log` | rc=0，TOTAL 150，0 OVERFLOW / 0 TOO WIDE |
| render.py | `build-render.log` | rc=0，印 3,100,944 B / 网 950,823 B，各 8 页 |
| boxtitle | `boxtitle.log` + `boxtitle/2026-w47-es-ru.json` | rc=0，**0 DEFECT**，0 OBSERVE，0 marginal |
| boxtitle 直接核实 | `title-direct-measure.log` | 标题 21pt 三段 ink_r 最大 946.3px，框右界 961.0，**余 14.7px**（注：21pt 低于工具 22pt 检测下限，titles 计 38 vs 修前 41——三段标题被计为 BODY，同 de-fr 情况；故另做直接测量 + creambox 差分核实） |
| occlusion | `occlusion.log` / `occlusion.json` | rc=0，**0 flags**，自检通过 |
| spill | `spill.log` | rc=0，**0 SPILL**（27 盒，149 candidates，149 OBSERVE） |
| edge | `edge.log` | rc=0，8 页 **0 TOUCH / 0 NEAR** |
| p8 extract | `p8extract.log` | 150/150 |
| p8 compare vs core-es | `p8compare.log` | **CLEAN**，missing=[] extra=0，keydiff=[137, 138]（读者语翻译题应有差异，同前） |
| D5 census | `probe.log` / `probe-post.json` | 与修前一致：runs=3184，LAT@NotoSans=0，LAT@Newsreader=21934，CYR@NotoSans=4300，CJK+CYR=555——字体路由未动 |
| 文字层多重集 修前/修后 | `textcheck.log`（`pre-text.txt` vs `post-text.txt`） | **MULTISET IDENTICAL**，35,160 非空格字符 |
| 文字层 印/网 | `textcheck-print-web.log`（`print.txt` vs `web.txt`） | 各 53,413 B，**MULTISET IDENTICAL**，35,160 非空格字符 |
| freeze | `freeze.log` / `freeze/` | rc=0，**8/8 SVGs byte-identical**，shipped SVGs 未变 |
| D5 creambox 差分 | `creambox.log` / `creambox.json` | rc=0，**PASS 0 defects**（仅 P1 diff 65 / moved 39，系标题降字号 + 框矮 2px；p2–p8 diff 0） |

## 其他

- 未 commit、未 push、未动其他版。KIT 已更新（§8 新 SHA + 本节记录）。
- `baseline-pre/` 为修前版副本（svg + 源文件，content12.py 已还原修前态），供 creambox 差分用。
