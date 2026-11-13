# FIX-LOG-2 — W47 it 家庭第二轮修复（R2-1/R2-2）

**修理工**：W47 it 家庭第二轮修复工人（只修 it 家 2 版，不碰其他家庭、其他周；不 commit、不 push、不跑 lint）
**日期**：2026-11-12
**工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix2-w47-it/`
**校对结论**：`../scratch-reproof2-w47-it/PROOF-NOTE-2.md`（第二轮独立重校；协调员已逐项核实属实，照此修）
**SOP 依据**：`~/workspace/weekly-git/SOP.md` §8（修源头→重渲染整版→门禁→KIT→FIX-LOG）
**解释器**：`~/workspace/weekly-git/tools/venv/bin/python`
**备份**：`scratch-fix2-w47-it/backup/<edition>/`（改前 *.py + *.txt + *.md + *.pdf + svg/*.svg 全量快照，46M；cards/ 与 assets/ 未备——cards 可由 render.py 重建，assets 是输入未动）
**磁盘**：开工 `df` 已用 95G，收尾 95G（<100G 门限）

## 0. 未动声明

**未动 9 版**：it-en、it-de、it-fr、it-es、it-pt、it-nl、it-ru、it-ja、it-ko——一字未改（it-fr 的 `6–8 novembre` 为法语正确写法，核实未动；其印 PDF SHA 仍为一轮值 `ffb20e7b9620…`）。只改 core-it（it-zh-cn）与 it-zh-tw 两版。

## 0.1 改前状态（实测，非抄校对结论）

| 版 | 印 PDF 字节 / SHA-256 前12 | 网 PDF 字节 / SHA-256 前12 | text.md 字节 / SHA-256 前12 |
|---|---|---|---|
| core-it (it-zh-cn) | 14,839,774 / `77d33bf8c581` | 1,546,123 / `7680a0ea63ac` | 52,630 / `c6e9ef6c9f0a` |
| it-zh-tw | 14,907,350 / `45abf7bfc8a7` | 1,640,994 / `6d7a1efc737c` | 52,541 / `cf5a828688a3` |

与 PROOF-NOTE-2 所记门禁基线一致。改前核实：两版 text.md 各含无空格 `=` 对 24 处（正则 `[a-zà-ÿ]+=[^ ]` 24 命中），P4 标题行 L445 各含 `6–8 novembre`。

## 1. 源头改动

### 1.1 R2-1：P4 赛果标题月份本地化（content34.py，各 1 处）

| 版 | 文件:行 | 改前 | 改后 |
|---|---|---|---|
| core-it | content34.py:160 | `I RISULTATI DELL'11ª GIORNATA　第 11 轮赛果（6–8 novembre）` | `I RISULTATI DELL'11ª GIORNATA　第 11 轮赛果（11月6–8日）` |
| it-zh-tw | content34.py:158 | `I RISULTATI DELL'11ª GIORNATA　第 11 輪賽果（6–8 novembre）` | `I RISULTATI DELL'11ª GIORNATA　第 11 輪賽果（11月6–8日）` |

月份与日期均本地化，破折号保留 en dash，与 ja/ko 一致。标题字号 26 不变。

### 1.2 R2-2：配对题注释 `=` 两侧加空格（各 12 处源头行，各 24 处 text.md 行）

12 组词 × 练习区 + 答案区 = 24 处/版，改为 ja/ko 同款带空格无逗号形式（`word = 译文 key`）。源头为 3 个文件的 `match_set` 注释列表：

| 版 | content12.py | content34.py | content8.py |
|---|---|---|---|
| core-it | :268 `salute=健康 c`、`ponte votivo=还愿桥 b`、`candela=蜡烛 d`、`piantare=种植 a` | :203 `vetta=榜首 d`、`imbattuto=不败的 b`、`girone=小组 c`、`debutto=首次亮相 a` | :85 `manovra=预算法案 d`、`deficit=赤字 c`、`copertura=资金来源 b`、`scaglione=税级 a` |
| it-zh-tw | :266 `salute=健康 c`、`ponte votivo=還願橋 b`、`candela=蠟燭 d`、`piantare=種植 a` | :201 `vetta=榜首 d`、`imbattuto=不敗的 b`、`girone=小組 c`、`debutto=首次亮相 a` | :85 `manovra=預算法案 d`、`deficit=赤字 c`、`copertura=資金來源 b`、`scaglione=稅級 a` |

每处均由 `word=` 改为 `word = `（词内空格保留，如 `ponte votivo = 还愿桥 b`）。改后源头 6 行 grep 无空格 `=` 对 0 残留。

**注（任务清单与实测的出入，已核实）**：任务清单列出 13 个词（含 `votivo=还愿桥`），但盘上并无独立的 `votivo=` 字符串——`votivo` 只出现在 `ponte votivo=` 词组内。12 组词即上表 12 项，24 处/版（12×练习区+答案区）与 PROOF-NOTE-2 的计数一致；`votivo` 一项无额外改动可做。

## 2. 重建

**流程**：照抄一轮 `scratch-fix-it/rebuild_one.py` + `gates_it.sh` + `export_textmd.py`（复制到本轮目录，改路径；MARKERS 换为本轮词表；gates 的 p8 compare 改用任务指定形式 `--core-dir/--edition-dir/--target it`；其余逻辑不变）。

| 版 | run.py | render.py | text.md 干跑 diff | 印 PDF 字节 / SHA-256 前12 | 网 PDF 字节 / SHA-256 前12 | text.md 字节 / SHA-256 前12 |
|---|---|---|---|---|---|---|
| core-it (it-zh-cn) | TOTAL 150，0 溢出；P8-keys 2499/2552 | 见下 | 25 行，全为替换（c） | 14,839,776 / `7b3034a08180` | 1,546,116 / `393e65473a1c` | 52,677 / `24b37ae72af3` |
| it-zh-tw | TOTAL 150，0 溢出；P8-keys 2499/2552 | 完成 | 25 行，全为替换（c） | 14,907,346 / `3cf43a808c2a` | 1,640,999 / `133b04d123f1` | 52,588 / `1ae5edf7b167` |

text.md diff 构成（每版）：标题 L445 1 行 + `=` 间距 24 行（练习区 L285/287/289/291、L499/501/503/505、L981/983/985/987 + 答案区 L1067/1069/1071/1073、L1121/1123/1125/1127、L1299/1301/1303/1305），无增加/删除行——导出器陷阱未触发（无标题丢失；一轮 FIX-LOG §0.6 已证 it 家导出器无字号阈值，本轮干跑 diff 再次实证）。每版 text.md 1317 行不变。

**core-it render.py 中断与恢复**：首跑 `rebuild_one.py` 时 run.py RC=0 正常，render.py 在 8 张 PNG 卡片全部渲完后以 RC=-15（SIGTERM）被杀，日志为空（缓冲输出随进程丢失）。原因未确证：当时机器并行跑着多家其他 worker（ps 见 de/nl/ko 等家 run.py、webpdf、census 同跑），可用内存一度仅 ~0.8–1.3G，疑似内存压力下的运行时回收。恢复办法：render.py 改用 `nohup … python -u render.py` 独立重跑，一次成功（印 PDF 落盘）；其余步骤（export 干跑→落盘→webpdf）按原流程手工续跑，门禁脚本照常。it-zh-tw 的 render.py 直接用同一 nohup 方式跑，一次成功。源头改动未因此多改一字。

## 3. 门禁结果（2/2 ALL-GREEN）

| 版 | run.py | occlusion | p8 extract / compare | D5 census | boxtitle | spill | edge | 印/网文本层 |
|---|---|---|---|---|---|---|---|---|
| core-it | TOTAL 150，0 溢出，0 HTW；P8-keys 2499/2552 | 0 flags | 150/150；compare 跳过（自身） | 0/0/0；弯引号 4/4 Newsreader | 24 题 320 行，0 DEFECT | 29 盒 103 候选，0 SPILL | 0 TOUCH 0 NEAR；P8 底距 55.8pt | 38,091 = 38,091，差 0 |
| it-zh-tw | TOTAL 150，0 溢出，0 HTW；P8-keys 2499/2552 | 0 flags | 150/150；CLEAN，keydiff=[137,138,139] | 0/0/0；弯引号 4/4 Newsreader | 24 题 325 行，0 DEFECT | 29 盒 104 候选，0 SPILL | 0 TOUCH 0 NEAR；P8 底距 55.8pt | 37,930 = 37,930，差 0 |

门禁日志：`logs/gates-core-it.log`、`logs/gates-2026-w47-it-zh-tw.log` + `gates-core-it/`、`gates-2026-w47-it-zh-tw/`（keydiff=[137,138,139] 为三道翻译题的读者母语译文差异，属设计差异，一轮已确认）。P8-keys 末值 2499 ≤ 2552，无需实测 PDF 末行（it-ja 的 2561 流光标假象与本轮无关）。

## 4. 改后核实（逐项实测）

- **R2-1**：两版印 PDF 文本层各含 `11月6–8日` 1 处；`novembre）` 0 处。fr 版 text.md 仍含 `6–8 novembre` 1 处，未动。
- **R2-2**：两版 text.md 无空格 `=` 对 0 残留（正则 `[a-zà-ÿ]+=[^ ]` 0 命中），带空格形式 24 处在位；两版印 PDF 文本层无空格 `=` 对亦为 0，带空格 ` = ` 34 处（含填空题等原有带空格形式）。PDF 中配对题练习区以左右分列渲染，`word = 译文 key` 注释串只出现在 P8 答案区（12 处/版）——与一轮导出结构一致，属渲染形态，非缺失。
- **页数**：印/网 PDF 各 8 页（pypdf 实测，两版共 4 个文件）。
- **文本层一致**：印/网逐字节多重集相等（core-it 38,091 字，zh-tw 37,930 字，nonws 差 0）。
- **P8 答案**：text.md 答案区 150 题（1–150）全有；p8 extract 150/150。
- **U+201C/U+201D 普查**：两版 text.md 弯引号各 3 对（“ 3 / ” 3），ASCII 直引号 0；census 弯引号 4/4 在 Newsreader 内，成对。
- **改动范围**：与备份 diff 核对，每版仅 7 类文件有变——content12.py、content34.py、content8.py、text.md、印 PDF、网 PDF、WEEKLY-KIT.md，及重生成的 svg/p4-sport.svg（R2-1 标题）与 svg/p8-valutazione.svg（R2-2 答案）；其余源文件、svg、ABSTRACT.txt 均未动。

## 5. KIT 更新

两版 WEEKLY-KIT.md 各追加一节「Fix round 2 — W47 it proof fixes R2-1/R2-2」（`update_kits2.py` 写入，逐版核对新 SHA 与字节数无误）：core-it §13（ supersedes §12）、it-zh-tw §16（supersedes §15）；每节含修复 bullet、构建与门禁摘要、新旧三 SHA（新 SHA 全文，旧一轮 SHA 保留备查）。

| 版 | 印 PDF 字节 / SHA-256 前12 | 网 PDF 字节 / SHA-256 前12 | text.md 字节 / SHA-256 前12 |
|---|---|---|---|
| core-it (it-zh-cn) | 14,839,776 / `7b3034a08180` | 1,546,116 / `393e65473a1c` | 52,677 / `24b37ae72af3` |
| it-zh-tw | 14,907,346 / `3cf43a808c2a` | 1,640,999 / `133b04d123f1` | 52,588 / `1ae5edf7b167` |

新 SHA 全文：core-it 印 `7b3034a0818000a1d4e3746ca038d228ddcb3935a755f9347e5f2407532e908e`、网 `393e65473a1c28a79542395de67381a71cbe3bf9eebb34b027c7179958a1cf8f`、text `24b37ae72af304dd55b4e2ce9b56e6e5552ebc766f19a997193fdb2b8a6cc3d9`；it-zh-tw 印 `3cf43a808c2a5d1734115378ffa931a00dca7e7a59e08d57a49279d21e987ac5`、网 `133b04d123f18825bc9c91f9409740ce84eb22bc340ba027d5e9aed750f0139e`、text `1ae5edf7b167d6d9ff263072bca34ba464c95949582017f85fd5a354fbcc4d43`。

## 6. 残留问题

无。2 项 low 全部修复，2 版门禁全部绿灯，KIT 已更新。无 commit、无 push、无 lint；磁盘收尾 95G（<100G 门限）。
