# FIX-LOG — W47 zh-tw 记忆法条目重 key（tables.py L2173）

**时间：** 2026-11-11 ~05:00 EST；**执行：** 记忆法条目重 key 员。
**对象：** `hidden_files/w47/scratch-fanout-zh-tw/tables.py`（238 条 × 9 语）唯一条目 L2173–2183。
**备份：** 同目录 `tables.py.bak-pre-rekey`（改前原文件，SHA 与改前一致，diff 校验用）。
**范围纪律：** 只改这一个条目（0 键 + 7 值）；core 任何文件、transform.py、其余条目均未动；不 commit、不 push。

## 探针

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0。
- scratch 真实写：`tmp/probe-rekey-1.txt` 写入并读回成功。/tmp 已满，全程 `TMPDIR=<scratch>/tmp/`，未写 /tmp。

## 1. 源句实测（core 为准绳）

`~/workspace/weekly-git/production/2026-w47/core-zh-tw/content7.py:52`（磁盘实测，fix4 后）：

> `Memory trick: learn 入圍 first, then 星光大道 (the red carpet at 17:00, before the ceremony), then the ceremony （頒獎） at 18:30.`

与 core-zh-tw fix4 FIX-LOG 所述字符串逐字节一致（交叉核对通过）。

## 2. 源键核对：未漂移，不动键

tables.py L2173 源键经 Python 逐字节比对：与 core 源句 **BYTE_IDENTICAL: True**（各 140 UTF-8 字节）。
结论：**源键未漂移，键未改**。与 ja fix1 FIX-LOG（`scratch-fix-zh-tw-ja1/FIX-LOG.md` §4）所述一致：表侧源键已先行改写为新句，7 语值未跟上——本轮即补这 7 值。

## 3. 9 语值核对与改动

| 语 | 处理 | 结果 |
|---|---|---|
| fr | 只验证，未动 | 已正确：顺序 入圍 → 星光大道 → 頒獎；红地毯 17:00 在先、颁奖 18:30 在后；无“place”字眼（无 lieu/endroit）。与 ja fix1 FIX-LOG §3③ 所述 fr 值逐字一致 |
| ko | 只验证，未动 | 已正确：顺序正确，17:00 红地毯在先、18:30 颁奖在后；无 장소。与 ja fix1 FIX-LOG §3③ 所述 ko 值逐字一致 |
| ja | 改值（FIX-LOG §3② 提案值原文） | `覚え方のコツ：まず入圍、次に星光大道（式典の前のレッドカーペット）、そして式典（頒獎）の順に覚えよう。`（注：该提案值本身不含 17:00/18:30 时间注，按任务书原文取用，未自行加时间） |
| de | 新译 | `Merktipp: Lerne zuerst 入圍, dann 星光大道 (der rote Teppich um 17:00 Uhr, vor der Zeremonie), dann die Zeremonie （頒獎） um 18:30 Uhr.` |
| es | 新译 | `Truco de memoria: aprende primero 入圍, luego 星光大道 (la alfombra roja a las 17:00, antes de la ceremonia), y luego la ceremonia （頒獎） a las 18:30.` |
| it | 新译 | `Trucco per ricordare: impara prima 入圍, poi 星光大道 (il red carpet alle 17:00, prima della cerimonia), poi la cerimonia （頒獎） alle 18:30.` |
| pt | 新译 | `Truque de memória: aprenda primeiro 入圍, depois 星光大道 (o tapete vermelho às 17:00, antes da cerimônia), e depois a cerimônia （頒獎） às 18:30.` |
| nl | 新译 | `Geheugensteuntje: leer eerst 入圍, dan 星光大道 (de rode loper om 17:00 uur, vóór de ceremonie), dan de ceremonie （頒獎） om 18:30 uur.` |
| ru | 新译 | `Приём для памяти: сначала выучите 入圍, потом 星光大道 (красная дорожка в 17:00, перед церемонией), а потом церемонию （頒獎） в 18:30.` |

改前 6 语 + ja 的旧值共同错误：顺序倒置（頒獎在先、星光大道在后）且含“地点”说法（de Ort / es lugar / it luogo / pt lugar / nl plek / ru место / ja 行われる場所）。
改后程序核查（9 语全过）：每语 入圍 → 星光大道 → 頒獎 顺序正确；“地点”类禁词 0 命中（de Ort、es lugar、it luogo、pt lugar、nl plek/plaats、ru место、ja 場所、fr lieu/endroit、ko 장소）；除 ja（提案值无时间）外 8 语均含 17:00 与 18:30。

**diff 校验（改后 tables.py vs 备份）：** 仅 7 行值变（L2174 de、L2176–2181 es/it/pt/nl/ru/ja），键 L2173 与 fr L2175、ko L2182 零改动；`ast.parse` 通过。

## 4. 验证：transform 9/9（沙箱跑法说明）

transform.py 为 one-shot（目标版目录已存在即拒跑），而真实 `production/2026-w47/2026-w47-zh-tw-<lang>` 9 个版目录已存在（第 7 棒已建版），故**未在真实 production 目录跑 transform**。
改用沙箱：`HOME=<scratch>/tmp/fakehome`（其 `workspace/weekly-git/production/2026-w47/core-zh-tw` 为指向真实 core 的符号链接），transform 在此假 HOME 下建版；改前/改后各一套（`tmp/run-before` + `tmp/fakehome`，`tmp/run-after` + `tmp/fakehome-after`）。

- **改前基线：** transform de/fr/es/it/pt/nl/ru/ja/ko **9/9 OK**（`TRANSFORM OK`，无 AssertionError）。
- **改后：** transform 同样 **9/9 OK**。
- **逐语核查生成文件：** 改后 9 版 `content7.py:52` 记忆法行与 tables.py 新值逐字一致（fr/ko 为原值）。
- **改前/改后 diff 分类（`diff -rq` 全量 9 版）：**
  - fr、ko：`rc=0`，整版**完全相同**（值未动，符合预期）。
  - de、es、it、pt、nl、ru、ja：仅 **1 个文件**不同（`content7.py`），仅 **1 行**不同（L52 记忆法行，旧值 → 新值）；其余全部文件（bslib4.py、content12/34/56/8.py、render.py、ABSTRACT.txt 等）零差异。
  - 结论：除该条目外，9 语 transform 输出与改前**无差异**。

## 5. 待协调员注意

1. ja 值按 ja fix1 FIX-LOG §3② 提案原文取用，**不含 17:00/18:30 时间注**（与 fr/ko/其余 6 语不一致）；若协调员要求 ja 也补时间，须再改一处。
2. 真实 production 版目录（`2026-w47-zh-tw-<lang>`）**未重建**：本轮只改了 scratch 的 tables.py；已发版 9 版的 content7.py 仍含旧记忆法行，需协调员定重扩/重建时机（transform one-shot 限制 + 各版 P7 已调栏，径直重跑会丢版内手工修正——见 FANOUT-REPORT 各版“修过”项，故本轮不擅自重建）。
3. 未 commit、未 push。沙箱运行产物在 `<scratch>/tmp/`（run-before/run-after、fakehome/fakehome-after），transform 日志各 9 份在 run 目录内。
