# GATE-LOG — 2026-W47 core-it D-2 fix（2026-11-11）

首行：探针 `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0（`probe.txt`）；新三 SHA：印 `e1f89922a2b09e66d7d132eeab12b2638528e737685fa85d70f41bb8d2d1255d`（27,726,330 B）/ 网 `09f2ef6696ad67e92e57ba161c8ba2e6b35753634fa21b7ce68ea029283d71ef`（1,790,596 B）/ 文 `9eb9ee0662542e6ccf2814a2f2534fd64b62ad326de42e9cf83282092b5b6eed`（52,655 B，1317 行）；D-2 实测：旧串全版 0 处、新串各就其位、P7 裁图目视通过；门禁汇总见下表，全部通过。

## 探针与环境

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0。
- scratch 真实写文件通过（`probe.txt` 含 `probe-ok`）；全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`，Pillow 13.0.0 / FreeType 2.14.3（freeze.log 首行实测值）。

## 改前三 SHA（盘实值，2026-11-11 开工前核对，与 KIT §8/§9 一致）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4.pdf` | 27,726,350 B | `2ee50d92635ba496d65c09c085a9b70fbebad62a8d6f3b81c41afec4be47a412` |
| 网页 PDF `La-Lucerna-VOL4-web.pdf` | 1,790,620 B | `ab14a5b7bbf532e0633fee0006f5c19f44bc558b9ad475ad523d5bd0aaaecab0` |
| 文本导出 `2026-w47-it-zh-cn.text.md` | 52,676 B，1317 行 | `d0c573b83fa679262c2da0734b08b1f504782829c11d29c9ed1e2c8cac08dbcb` |

## 新三 SHA（生产目录，改后实测）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4.pdf` | 27,726,330 B | `e1f89922a2b09e66d7d132eeab12b2638528e737685fa85d70f41bb8d2d1255d` |
| 网页 PDF `La-Lucerna-VOL4-web.pdf` | 1,790,596 B | `09f2ef6696ad67e92e57ba161c8ba2e6b35753634fa21b7ce68ea029283d71ef` |
| 文本导出 `2026-w47-it-zh-cn.text.md` | 52,655 B，1317 行 | `9eb9ee0662542e6ccf2814a2f2534fd64b62ad326de42e9cf83282092b5b6eed` |

## D-2 实测

- 改前原文（`content7.py:17/18` 实测）：L17 `Le forme sono regolari: andare → andrò, …`；L18 `Il verbo è leggere, irregolare al futuro: leggerò.`。
- 改后（实测）：L17 `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`；L18 `Il verbo è leggere, regolare al futuro: leggerò.`。
- 旧串重扫（生产目录，`content*.py` + 8 SVG + `.text.md` + 印/网 PDF 文本层）：`Le forme sono regolari: andare` 0 处；`irregolare al futuro: leggerò` 0 处。
- 新串各就其位：两句在 `content7.py`、p7 SVG、`.text.md:775/:777`、印/网 PDF 文本层各 1 处。
- 全核心 `regolar` 仅两行（`content7.py:17/18`，grep 实测 2 行）。
- P7 渲染放大目视：`crop-p7-a2.png`（200 dpi card 裁图，A2 栏 y 230–700）——两句在版、干净、无溢出/重叠；桥接句与习题区 intact。
- 习题键：Q101 `andremo`、Q102 `assaggeremo`、Q103 `guarderemo`、Q104 `B`，改前/改后逐题相等；全部 150 键相等。

## 门禁汇总（全部通过）

| 门禁 | 结果 | 证据行 / 日志 |
|---|---|---|
| 构建（scratch run.py） | RC=0；0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE；TOTAL 150；A2 47 / B1 70 / B2 33；页 10/18/18/18/18/18/12/38；范文 99 词 | build.log（`TOTAL 150`、`by level {'A2': 47, 'B1': 70, 'B2': 33}`、`model words: 99`；`grep -c` 溢出标志 = 0） |
| 构建（scratch render.py + webpdf + export） | RC=0 全部；印 27,726,330 B；网 1,790,596 B；文本 52,655 B / 1318 行（export 打印值，见 FIX-LOG §0 说明）/ 150 题 | render.log、webpdf.log、export.log |
| freeze baseline（生产，`--core-svg` 指 core-it 自身 `svg/`） | **8/8 字节一致**；P7 `a7e6afa4…` 精确复现；其余 7 页与改前字节一致；发运 SVG 运行前后重哈希无变化 | freeze.log（`baseline: 8/8 SVGs byte-identical`；运行时 `Pillow 13.0.0`） |
| occlusion audit | selftest OK（6 类阳性全触发、干净对照沉默）；生产 8 页 **0 flags** | occlusion-selftest.log、occlusion-prod.log（`0 flags`） |
| p8 extract | noted **150/150** | p8-post.log（`noted set = 150 of 150`） |
| p8 compare（三源之一：改前 vs 改后） | CLEAN，missing=[]、extra_count=0、keydiff=[] | p8-compare.log（`status: CLEAN`） |
| p8 vs 文本导出（三源之二） | 150/150，0 差异 | 本 LOG §D-2 实测（md 键解析 150 个，diffs 0；脚本输出 `md keys parsed: 150 diffs vs p8 extract: 0`） |
| `.text.md` 校验 | forward-miss 0 / reverse-miss 0 | validate.log、validate-prod.log（`forward-miss: 0 reverse-miss: 0`） |
| 印/网 text layer | `pdftotext` 字节相同，各 43,979 B / 5,948 词，`cmp` rc=0 | print-prod.txt、web-prod.txt（`-layout` 版各 105,745 B 亦相同） |
| PIL 横向扫描（全 8 页） | 无行越过页面边距；仅两条家具线恰止于 1862.0 px（+0.0，改前已有）；左缘越界 NONE | h-scan.txt（`OVER page right margin` 仅 2 行 +0.0；`LEFT of margin 88` NONE；P2 匹配块 b 余 31.1 px / d 余 40.3 px，与 fix3 一致） |
| 200 dpi 渲染扫描（全 8 页） | P7 无越边距墨迹；P2 +0.7 pt、P5 +0.7 pt、P8 +1.0 pt 痕迹与 fix3 改前值完全相同 | render-scan.txt（`P7: no ink past margin`） |
| 目视裁图 | P7 A2 栏两句在版、干净 | crop-p7-a2.png |

## 未做 / 未碰

- 未 commit、未 push（按任务要求）。
- 未碰 11 个 it fan-out 版（重扩散由协调员另派）。
- 未改 `tools/` 下任何工具（freeze.py / gates.py 等）；复用的 fix1 扫描脚本只改指了输入路径，未改逻辑。
- 未直接跑生产 `run.py` / `render.py`（OUT/BASE 硬编码生产路径）；构建在 OUT/BASE 已改指 scratch 的拷本里完成，产物核验后才拷回生产目录。
