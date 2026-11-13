# FIX-LOG — 2026-W47 pt-en 第一轮返修（D1/D2/D3）

- 返修 builder：叶子（第一轮返修；与 pt-en builder、pt 核心 builder、pt 各轮复校员、第一轮复校员不同人）
- 时间：2026-11-11（EST）
- 对象：`production/2026-w47/2026-w47-pt-en/`（main clone 内，未入仓新目录）
- 依据：SOP.md §8 / §1.1、AGENTS.md、WEEKLY-KIT.md、`scratch-proof-pt-en1/PROOF-NOTE.md`（D1/D2/D3）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-pt-en-fix1/`
- 红线遵守：未改 core-pt、未碰 W43–W46、其他目标语家庭、tools/；未跑 insert.py、lint --write；未 git add/commit/push/reset/stash。

## 0. 开工探针

- 探针 1：`echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功（`da0c4eb8…`）。
- 探针 2：在本目录真实写 `.probe` 成功。双通后动手。

## 1. 动手前独立核实（D1/D2/D3 逐项）

### D1（P1 刊头标语歧义）— 核实通过

- 源句：`tables_en.py:197` SEG `"读巴西人正在读的葡萄牙语": "The Portuguese Brazil is reading"`，与复校报告一致。
- 姊妹版对照（各版 P1 SVG `<text>` 实测，10/10 齐全）：
  - de `Das Portugiesisch, das Brasilien liest`、fr `Le portugais que lit le Brésil`、es `El portugués que lee Brasil`、it `Il portoghese che legge il Brasile`、nl `Het Portugees dat Brazilië leest`、ru `Португальский, который читает Бразилия`、ja `ブラジルが読むポルトガル語`、ko `브라질이 읽는 포르투갈어`、zh-tw 沿用中文原文 `讀巴西人正在讀的葡萄牙語`。
  - 9/9 非英文版均用显性关系代词（或日韩语前置定语结构），唯 en 省略关系代词，首要 parse 为“葡萄牙语的巴西正在阅读”。缺陷成立。
- 修复：SEG 值改为 `The Portuguese that Brazil is reading`（按任务指定译法；不取祈使 `Read …` 式，因该行在版式上为标语性名词短语，且任务已指定该译法）。

### D2（P4 词表注 `o título champion`）— 核实通过

- 源：`tables_en.py:36` SEG `"冠军": "champion"`；核心 `core-pt/content34.py:134` 词表行 `o título 冠军`；该 SEG 键在全版仅此一处使用（`champion` 在 en 构建文件仅 `content34.py:134` 一处；`the champions' trophy` 属另一键 `冠军奖杯`，不受影响）。
- 同期正确用法：P8 注 146 `Grêmio chase a sixth title`、147 `Palmeiras chase a fifth title`（`content8.py:90/92`）。
- 修复：SEG `"冠军"` 值改为 `title`。

### D3（P8 答案注冒号后缺空格，4 处）— 核实通过

- 核心源（全角冒号后无空格，中文排版正确）：`core-pt/content34.py:204` `3 > 1：mais`、`:206` `5 > 4：mais`、`:208` `16:30 < 17:00：mais cedo`；`core-pt/content7.py:22` `cair numa sexta-feira：落在周五`。
- 英文版对应：`2026-w47-pt-en/content34.py:204/206/208`、`content7.py:22`，冒号后均无空格，与复校报告一致。
- 同一答案流内有空格的先例：59. `2 days < 7 days: menos`、101. `em + date: em 20 de novembro`——二者均由 OVR 整句覆盖实现（`tables_en.py:243` `'2 天 < 7 天：menos' -> '2 days < 7 days: menos'`、`265` `'em + 日期：em 20 de novembro' -> 'em + date: em 20 de novembro'`），即已有“OVR 整句覆写、冒号后补空格”的先例。本轮沿用同一机制。
- 修复：在源串中补空格——以 4 条 OVR 整句覆盖加入 `tables_en.py`（OVR 先于 SEG、长键优先；4 条源串无其他 SEG/OVR 子串冲突，`cair numa sexta-feira：落在周五` 内的 `落在周五`/`周五` SEG 键因 OVR 先行而不生效）：
  - `'3 > 1：mais' -> '3 > 1: mais'`
  - `'5 > 4：mais' -> '5 > 4: mais'`
  - `'16:30 < 17:00：mais cedo' -> '16:30 < 17:00: mais cedo'`
  - `'cair numa sexta-feira：落在周五' -> 'cair numa sexta-feira: falls on a Friday'`
- 未动 `transform.py` 的全角冒号映射（`：`→`:`）：全局改映射会波及全版所有全角冒号（含行尾冒号、括号内冒号等），超出 6 处缺陷范围；OVR 整句覆写是任务指定的“在源串中补空格”且与既有先例一致的最小改法。

### D3 全版同类残留 grep（P8 注文，模式 `:` 后紧跟非空格）

- 修前 P8 SVG 扫描：仅 4 处缺陷行（56/57/58/102）为冒号后直接接字母；另 1 行 65. `Day 2 is natural sciences and mathematics, 13:30 to 18:30` 的冒号后为数字，属时刻写法，非缺陷。修后复扫（见 §5）。

### D2 同类抽查（“葡词直译成英文词”误译）

- P1–P6 词表注 29 项逐项核对（5 个 gloss 框，6/6/6/6/5）：除 D2 `o título champion` 外全部正确（feriadão/a three-day holiday、folga/time off、programação/programme、quilombo/a runaway-slave settlement、escravizado/enslaved person、agregado/aggregate score、pênaltis/penalty shoot-out、decisão/the final、pausa/the break、taça/trophy、gabarito/answer key、prazo/deadline、dia útil/working day、chute/a lucky guess 等）。
- 12 条 `词=释义` 配对注逐条核对（content34.py:200 等）：全部为多词准确释义，无单字直译误译（agregado=the two legs added together、volta=the second match of a tie、pênaltis=the shoot-out from the eleven-metre mark、taça=the champions' trophy、consciência=knowing and remembering、feriadão=a three-day weekend with a holiday 等）。
- 结论：D2 同类误译仅此 1 处，无新增修复。

## 2. 改动清单（源码层，共 6 处，均经 transform 机制）

| # | 缺陷 | 文件 | 改法 |
|---|---|---|---|
| 1 | D1 | `tables_en.py`（scratch-fanout-pt 机制表 + 版目录内副本，两份保持逐字节一致） | SEG `"读巴西人正在读的葡萄牙语"` 值 → `The Portuguese that Brazil is reading` |
| 2 | D2 | 同上 | SEG `"冠军"` 值 → `title` |
| 3 | D3-56 | 同上 | 新增 OVR `'3 > 1：mais' -> '3 > 1: mais'` |
| 4 | D3-57 | 同上 | 新增 OVR `'5 > 4：mais' -> '5 > 4: mais'` |
| 5 | D3-58 | 同上 | 新增 OVR `'16:30 < 17:00：mais cedo' -> '16:30 < 17:00: mais cedo'` |
| 6 | D3-102 | 同上 | 新增 OVR `'cair numa sexta-feira：落在周五' -> 'cair numa sexta-feira: falls on a Friday'` |

- `transform.py` 未动；`furniture.py` 未动；`core-pt` 未动。
- 再生路径：改表 → 在 scratch 副本上重跑 `transform.py`（核心新拷）→ diff 构建文件仅含上述 6 处等效改动 → 落盘到版目录 → 重跑 `textmd.py` 再生 `.text.md` → `run.py` + `render.py` + `webpdf.py` 全量重渲染。

## 3. 再生验证（transform 复现性）

- 将 `core-pt` 新拷至本目录 `repro/core-pt`，拷入已改的 `transform.py` / `tables_en.py` / `furniture.py` / `make_gates.py`，用 `tools/venv/bin/python transform.py <copy> en` 重跑：**rc=0，`CJK 0 OK in all build sources`，`TRANSFORM COMPLETE`**。
- 再生 6 文件与版目录 diff：仅 6 处等效改动（`content12.py:15` 标语、`content34.py:134` 词表、`content34.py:204/206/208` 三注、`content7.py:22` 一注），`bslib4.py` / `content56.py` / `content8.py` 逐字节一致。
- 唯一计划外 diff：`content12.py:19`——再生值为 `TEXT IN PORTUGUESE　EXPLICATIONS IN ENGLISH`，版目录现值为 `…EXPLANATIONS…`（正确）。成因：scratch `furniture.py` FURN[en] 的 `badge372` 仍为从法语条目抄来的 `EXPLICATIONS`，builder 建版后在版目录内手工改成 `EXPLANATIONS`，未回写 scratch 机制表。**本次未动该行**（不在 D1–D3 范围内；现值正确；机制表 stale 属既有问题，已写入 KIT §6 机制注 + 本日志，供协调员定夺）。版目录 6 处改动逐行落盘后，版目录构建文件与再生输出**除该 1 行外逐字节一致**。
- `tables_en.py` 两份（scratch 机制表 + 版目录副本）改后仍逐字节一致（`diff -q` 通过）。
- 注意：`repro/` 副本（39MB）已在配额事故恢复时删除（见 §4），其 diff 结论记录于此；`textmd.py` 的 `en-textmd-diff.json` 已另存本目录。
- `.text.md` 再生：`textmd.py <core-pt/2026-w47-pt-zh-cn.text.md> <版目录> en`，rc=0，535 行，CJK 0，题号 150/150；与旧 `.text.md` diff 仅 1 行：215 行 `o título champion` → `o título title`（标语与 D3 四注本就不在 `.text.md` 内，见 §1）。

## 4. 重渲染

- `run.py`：rc=0，TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；范文 88 词）；`FLOW OVERFLOW` / `HEAD TOO WIDE` 0 处。8 个 SVG 已再生，含 6 处修复（grep 验：新串各 1 处、旧串 0 处）；SVG 哈希变化仅 p1/p4/p8 三页。
- `render.py`：**首跑失败**——写盘中途报 `Disk quota exceeded`（配额，非磁盘满：df 显示 45G 空闲；属共享卷配额触顶），rc=120，印刷 PDF 被截断在 10,690,560 字节（pdfinfo 报无 trailer/xref，作废）。恢复：删除本目录已验证完毕的 `repro/` 核心副本（39MB）后写盘恢复，**重跑 render.py rc=0**，零溢出，印刷 PDF 有效（8 页，1462.5×2025 pt）。被截断的 PDF 从未被采信或汇报。
- `webpdf.py`：rc=0（`WROTE A-Lucerna-VOL4-web.pdf: 1102777 bytes, 46073 text bytes`，8 页）。
- 新旧双 PDF：见 §6。

## 5. 机械门与复核

- gates.py（`gates.py`，构建解释器）：**16/16 PASS，FAILURES: none**（rc=0）。P1 刊头标语加长后 masthead 行宽门仍绿。
- tools/occlusion_audit.py（tools/venv 解释器）：自检阳性对照 6 类全触发、干净对照静默；**0 flags**（rc=0）。
- tools/p8.py extract：**150/150**（rc=0）。compare vs 核心：**CLEAN**，missing=[]，extra_count=0，**keydiff 仍为 [137, 138]**（仅翻译题答案，与上一轮一致，rc=0）。
- tools/freeze.py baseline（构建解释器）：**8/8 SVGs byte-identical**（repointed files: none；核心 SVG 完整性复核通过，rc=0）。freeze diff：新增 CJK 共 9 个，全部为 U+3000 家具分隔符（P1 2 个、其余每页 1 个），与上一轮同一分布；新增汉字 0（rc=0）。
- check_final.py：页数 8/8；print/web 词数各 8,507（上一轮 8,502；+5 = 标语多 1 词 "that" + 4 处冒号空格使 `1:mais` 类 token 拆词），**词多重集 diff 0**；P8 答案区最小字号 **9.75pt**（§1.1 下限），187 spans，1,543 词（上一轮 1,539，+4 来自冒号空格）。
- U+2019 全扫：8 个 SVG 总数 **0**。
- 冒号复扫：`:` 后紧跟字母 0 处；`:` 后紧跟非空格非数字 0 处（时刻 `13:30` / `18:30` 等属数字写法，已排除）。
- 150 键逐题复核（新旧 p8 extract JSON 对比）：noted_set 完全一致（150/150），150 个答案键 **0 处差异**；注文仅 56/57/58/102 四处变（冒号后补空格）。与上一轮相比，除上述 6 处修复外全部一致。
- §1.1 抽查：纸色 #fbfaf6 共 8 处；金色 #d4af37 0；"double" 0；可见文本内 TODO/FIXME/XXX 0（原始 grep 的 10 处 XXX 均为 base64 图数据，与核心同类）；徽章三色齐全（A2 #5c6e30 / B1 #46581f / B2 #37402f）；VOL.4 ×9（+顶条 `VOL. 4` 1 次）、VOL.5 ×3（均在 P7 披露/预告内）；`.text.md` 双空格 0 行。
- 8 版目视（全新渲染，`render/print-p--*.png` + `web-p1--1.png` / `web-p8--8.png`）：P1 刊头标语 `The Portuguese that Brazil is reading` 单行居中完整、无溢出、无碰撞；P4 Note 框 `o título title`；P8 答案区 56/57/58/102 空格已入版、无溢出、页脚完整；P2/P3/P5/P6/P7 与上一轮一致（P3 中部大空白、P2/P4 栏尾孤行均为核心版式，见复校 O2；P1 数字盒贴边为既有 O8，occlusion 0）。网页 P1/P8 与印刷版内容一致。
- D2 同类抽查结论：见 §1（29 项词表注 + 12 条配对注，仅 D2 一处误译，无新增修复）。

## 6. 交付物

- 印刷 PDF `A-Lucerna-VOL4.pdf`：**12,932,451 字节**，8 页，1462.5×2025 pt，sha256 `0146a4202b015f44659b4bba067a7411f90891cb640085dee5fec2010bd06af1`（旧：12,932,446 字节，`8d2b58152bc0969151f8a7ab8becb0976221efdc62cac0d3cce877de8f160e4a`）。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：**1,102,777 字节**，8 页，sha256 `a974ef7ccf7c879f58e3626d874d9ce18e3da5f2a35faef43717e81706254c80`（旧：1,102,770 字节，`40bc2f444dbc31fbf0ef49643f1f81da13c134cab5ba0ec0a3ea804574a5e49c`），文字层 46,073 字节。
- `.text.md`：535 行，CJK 0，题号 150/150（仅 215 行改动）。
- WEEKLY-KIT.md §6（门禁记录）+ §8（.text.md 注）已更新为新值与本轮修复记录。
- 机械门全绿，见 GATE-LOG.md。按任务要求，改后第二轮全量复校由协调员另派，本轮不作定稿决定。
- 本轮未作任何 git 提交；版目录仍为未入仓新目录；未改 core-pt、W43–W46、其他目标语家庭、tools/（tools/freeze.py、occlusion_audit.py、p8.py 的 `M` 状态为本轮开工前已有的其他并行工作改动，mtime 2026-11-10 21:37–2026-11-11 05:01 UTC，早于本轮开工，非本人改动）。
- 遗留待协调员定夺（非缺陷）：scratch `furniture.py` FURN[en] `badge372` 的 `EXPLICATIONS` 拼写 stale（见 §3）；磁盘配额一度触顶（见 §4），并行多 agent 写盘时配额吃紧。

