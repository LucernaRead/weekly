# CHECK-NOTE — 2026-W47 · nl → pt · 正典版（build 4）缺陷重测

- 核查员：check-nl-pt1（只读、只核查；未改、未重建任何生产文件；未 commit、未 push）
- 日期：2026-11-11；工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-check-nl-pt1/`（`PYTHONDONTWRITEBYTECODE=1` 全程，TMPDIR 指向本 scratch）
- 核查对象（正典，磁盘实测）：`production/2026-w47/2026-w47-nl-pt/`
  - 印 `De-Lucerna-VOL4-nl-pt.pdf`：SHA `dd74de0a45556e96fdfcc216a9d249bbae577ace249bfbc256dd564ef6e5113e`，12,672,019 B
  - 网 `De-Lucerna-VOL4-nl-pt-web.pdf`：SHA `4e795b31f65273524128656f1a0a6064ba0f18efa93a29c191f15a2f58bf5e6b`，1,618,464 B
  - 文 `2026-w47-nl-pt.text.md`：SHA `7e6b0c54dcb2f0025b90bd6074407d32ec24c8f6d78a018e4b49ae9d621f7d8f`，47,209 B
  - 三件与任务给出的正典 SHA/字节数逐一一致。开工探针：`git hash-object -w /dev/null` → `e69de29b…`，RC=0；scratch 真实写文件成功。
- 结论先行：proof1 的 D1、D2、D3、D5 在正典上**全部已不在**；D4 上半（内联类型标签）**已不在**，下半（`[Complete]` / 印刷版 `Complete` ×59）**仍在，但定性待裁决**（见 D4 节：仓库 KIT fix-14 有相反裁决，本人已核实其语言学与跨版依据成立）。

## 1. 溯源：d70937d8 从哪来——三构建时间线

三构建皆真实存在过，先后关系如下（时间均为 2026-11-11，UTC+0 磁盘 mtime；EST = UTC−5）：

| 构建 | 身份 | 位置 | 时间 | 内容要点 |
|---|---|---|---|---|
| build 2 | 印 `d70937d8fb72c5a62969c4a09792a63fc9abc930d2b5f37854013a35e57e4cc5` / 12,671,956 B；网 `05faf026…` / 1,582,075 B；文 `5b353380…` / 46,025 B | `production/2026-w47/fanout-nl/2026-w47-nl-pt/`（当时） | proof1 实测 11:38–11:52（measure.log 11:38:51，PROOF-NOTE 11:51，GATE-LOG 11:52） | proof1 验的构建。GATE-LOG §0：“任务数字与磁盘无出入”——proof1 验的即当时磁盘上的现行构建，它没有验错对象，只是对象当天又被重建了两次。 |
| build 3 | 印 `e85aa1a01bea9c7894546e9e33f45f2c519f202f3404103dff59265f5daac834` / 12,672,018 B；网 `a0c8c87b…` / 1,618,472 B；文 `865e659f…` / 47,204 B | staging `fanout-nl/2026-w47-nl-pt/`（至今仍为此值，未动） | 重建 13:07–13:11（SVG 13:07，印 PDF 13:09，文 13:10，网 13:11；pt-build.log 13:11:54；KIT 13:18） | re-fanout：以 core fix2（`5de7492f`）为底重建，实施 proof1 修复 §Fixes 11–15（D3 选项 c 短式、D5 排名行、P6 标题缩短、D4 类型标签本地化、O1 盒底垫）。文 vs build 2 恰 293 行变（D3 2 + D5 1 + P6 标题 2 + 144 类型标签行对）。 |
| build 4（正典） | 印 `dd74de0a…` / 12,672,019 B；网 `4e795b31…` / 1,618,464 B；文 `7e6b0c54…` / 47,209 B | `production/2026-w47/2026-w47-nl-pt/`（git 状态 `??`，未入仓、未 commit） | 重建 19:07–19:10（印 19:07:48，文 19:08:49，网 19:10:45；KIT 19:26） | delta：先把 staging 整目录 `cp -a` 到规范路径（diff 完全一致），再同步 core fix3/fix4/fix5。相对 build 3：仅 `p4-sport.svg`（D11 盒高 611→638）与 `p8-toets.svg`（D9 键补 `kort`）变化；文仅 415 行变（+5 字节 `kort `）；其余 6 个 SVG 字节一致。 |

证据链（d70937d8 的出处，本人定向 grep，不含全树扫生产 SVG/PDF）：

- `hidden_files/w47/scratch-refanout-nl/backup/SHA256-orig.txt:314`（mtime 12:15:47）：重建 build 3 前备份的 build 2 印 PDF SHA 即 `d70937d8…`；同目录 `SHA256-backup.txt:314` 与 `backup/2026-w47-nl-pt/WEEKLY-KIT.md:18-19`（12,671,956 字节）一致。
- `hidden_files/w47/scratch-refanout-nl/FANOUT-REPORT-nl.md:44`：pt 行记 build 3 为 `e85aa1a0…`（12,672,018），与磁盘 staging 现值一致。
- proof1 自己的 `scratch-proof-nl-pt1/PROOF-NOTE.md` 与 `GATE-LOG.md` 只记录 d70937d8（未提及其他构建）。
- `scratch-delta-nl-pt/DELTA-LOG.md §0`：delta 开工时修前三 SHA 即 build 3（e85aa1a0 / a0c8c87b / 865e659f），§7 新三 SHA 即 build 4。
- 协调员的全树 grep 结果截至本 NOTE 写成时未到（见末尾补记 1：本人自己的 hidden_files/w47 grep 在写成后到站，并补出更多出处；协调员的全树 grep 本人仍未见到）。

一句话：**proof1 是对的（验了当时的 build 2），build 2 已被 build 3（13:09）与 build 4（19:07）两次重建取代；proof1 的 D1/D2/D3/D5 在重建中已被修掉（D1/D3/D4-上半在 build 3，D2 经 core fix2 短式在 build 3，D5 在 build 3 重导时由 webpdf 斜体面修复——见各节）。**

## 2. D1–D5 逐项重测（正典 build 4）

### D1 — P6 框标题：✅ 已不在正典

- 正典标题已是建议的缩短式：`VOOR OF TEGEN?　A FAVOR / CONTRA`（SVG `p6-verdieping.svg`：`x=1461.5, y=785`，21 pt Noto Sans CJK SC Bold；奶油盒 `<rect x=1439.5 y=743 w=422.5 h=309.0>`，右缘 1862.0 px——几何与 proof1 所述一致）。
- 三法实测（脚本 `measure_canonical.py` + 200 dpi 条带像素扫描 `pix-d1-6.png`）：
  1. PIL 真墨水：ink right 1850.5 px，余量 **+11.5 px**（advance 388.2 px，1461.5→1849.7）。
  2. 交付印 PDF 渲染 span：`A FAVOR / CONTRA`（NotoSansCJKsc-Bold 15.75 pt）bbox right 1389.3 pt，盒右缘 1396.5 pt，余量 **+7.2 pt = +9.6 px**（同基线另有 `VOOR OF TEGEN?` span，右缘 1229.8 pt）。
  3. 200 dpi 像素扫描（阈值 <150）：最右墨点 1851.8 px，余量 **+10.2 px**（<100 solid 阈值同值）。
- 三法一致，余量全部 ≥+5 px 判定线（最小 +9.6 px）。与 KIT fix-13 记录的 +11.5 clearance 一致。

### D2 — P2 练习 D 选项 c：✅ 已不在正典（核心继承 → 经 core fix2 短式修掉）

- 正典该行已不是 proof1 的旧串：SVG `p2-leven.svg` 与印 PDF 均为 **`c. eten voor Sinterklaas' paard`**（`x=1473.5, y=2233`，23 pt Newsreader，位置与 proof1 同位）。旧串 `c. eten voor het paard van Sinterklaas` 在正典 P2 已不存在（印 PDF P2 仅剩 `Het paard van Sinterklaas heet ___.` 一处填空题干，属他题）。
- 归属：原缺陷确为核心继承（core 同文同位）；修复来自 core fix2 短式，经 re-fanout（KIT §Fixes 11）带入 build 3，非本版自改。
- 三法实测（同 D1 方法；像素条带 `pix-d2-2.png`）：
  1. PIL 真墨水：ink right 1790.5 px，余量 **+71.5 px**（advance 316.6 px）。
  2. 印 PDF span：`c. eten voor Sinterklaas' paard`（Newsreader 17.25 pt）bbox right 1346.0 pt，右版心 1396.5 pt，余量 **+50.5 pt = +67.3 px**。
  3. 200 dpi 像素扫描（阈值 <150）：最右墨点 1793.3 px，余量 **+68.7 px**（注：该行是灰色 #6f675d 文字，渲染亮度约 111–140，<100 solid 阈值无命中，以 <150 为准，与 proof1 方法一致）。
- 三法一致在内，余量约 +67–72 px（KIT fix-11 称 +71.9 px，方法口径差异内一致）。

### D3 — text.md 答案标记：✅ 已不在正典（156 之谜已查明）

- `答案`：grep 全文 **0 处**；CJK 字符共 59 个，全部为 U+3000 全角空格分隔符（SOP §1.1 规定），无中文残留。
- 本地化标记实测（`2026-w47-nl-pt.text.md`，432 行 / 47,209 B）：
  - `— Resposta:`：**142 处**（与任务称一致）。
  - `(Resposta …)` 配对题内标记：**8 处**（行 122–125：#25–28；行 418–421：#141–144；格式 `(Resposta d · schoen = sapato d)`，与 proof1 所述的旧 `(答案 d · …)` 型一一对应，恰当）。
  - 142 + 8 = 150，覆盖全 150 题。
- “156 多出 6 处”的来源：另有 **6 处 `Respostas na página 8`**（复数，行 57、99、144、190、241、292，每节说明行末的导航句，如行 57 `Lê a primeira página e escolhe a resposta certa　Respostas na página 8`）。156 = 142 + 8 + 6，全部是合法葡语，不是答案标记残留。
- 另：小写 `resposta` 7 处——6 处 `a resposta certa`（各节题干说明）+ 1 处 `sem resposta única`（#150 开放题注），均为合法葡语正文。
- 结论：D3 的 150 处中文标记已在 build 3 重导时全部本地化，正典无残留。

### D4 — 类型标签：⚠️ 上半已不在正典；下半仍在，但定性待裁决

#### 上半（内联 `[级别 · 类型]`）：✅ 已不在正典

- text.md 内联标签 144 实例，全部葡语，无一英文（`grep -o "\[[^]]*\]"` 统计）：
  - `Completa a frase` 65（A2 19 / B1 32 / B2 14）、`Escolha múltipla` 44（21/16/7）、`Cloze` 13（B1）、`Verdadeiro ou falso` 7（B1 6 / B2 1）、`Forma frases` 8（B1 3 / B2 4 / A2 1）、`Traduzir` 4、`Relaciona as palavras` 2、`Escrita` 1（B1）。合计 144，覆盖 150 题（配对题共用标签，与 proof1 计数口径一致）。
  - 英文类型词 grep：`complete` 59（见下半，全部是尾标 `[Complete]`，非内联标签）、`choice`/`matching`/`writing`/`translate`/`true or false`/`make sentences`/`cloze choice` 均为 **0**。
  - SVG 全版同查：`Choice`/`choice`/`Matching`/`matching`/`Translate`/`Writing`/`True or False`/`Make sentences`/`Cloze choice` 均为 **0**（`Cloze` 在 SVG 亦为 0——印刷版不印类型标签，只印每题 instr 动词）。

#### 下半（尾标 `[Complete]` ×59 + 印刷版 `Complete` ×59）：⚠️ 仍在——但 KIT fix-14 有相反裁决，需协调员定夺

- 仍在，数量与分布与 proof1 所述**逐字一致**（本人实测，非沿用）：
  - text.md 尾标 `[Complete]`：**59 处**（行号清单见本 scratch `d4-text-lines.txt`；例行 109：`16. [A2 · Completa a frase] Kinderen zetten hun ___ bij de deur. — Resposta: schoen（schoen = sapato） [Complete]`）。
  - 印刷版 SVG `Complete`：**59 处**，分布 P2 9 / P3 13 / P4 9 / P5 10 / P6 9 / P7 9，P1/P8 0（逐页实测；元素坐标清单见本节末方法注）。
  - 源头：`instr="Complete"` 共 **59 处**，分布 `content12.py` 9 / `content34.py` 22 / `content56.py` 19 / `content7.py` 9（`content8.py` 0；行号全单见本 scratch `d4-source-sites.txt`）。text.md 尾标与 SVG 均由这些源码调用点生成（重建 + 重导同步）。
- **相反裁决（KIT fix-14，build 3 写入正典 KIT，须正视）**：`Complete` 不是英文残留，而是葡萄牙语 você-命令式（动词 completar 的第三人称命令式），是 trans_table INSTRS 葡语行有意映射的写法；平行例为西语 `Completar` ×59、意语 `Completa`。
- 本人核实的支撑证据（均为本轮实测）：
  1. 同版同文件内另有同型 você-命令式 instr：`Forme a frase` ×8、`Escreva` ×1——与 `Complete` 同一语法形式；其余 instr 为不定式 `Traduzir para português/neerlandês`（各 2）、`Palavra e significado`/`Ligue palavra-significado`（各 1）。即 `Complete` 处于一个葡语命令式 instr 集合内，不是孤立英文词。
  2. 跨版平行（本人实测）：nl-es text.md `[Completar]` ×59、SVG `Completar` ×59；it-pt text.md `[Completa]` ×56、`Completa a frase` 61 处、SVG `Completa` 65 处。裸动词作每题 instr 是全家设计（es 不定式、it/pt 命令式）。
  3. 葡语读者视角：`Complete` 在葡语中是合法词（“请补全”），题面语境（填空题上方）无歧义。
  4. 反方（proof1 原判）：该串拼写与英文单词 `Complete` 完全相同；同一文件的类型标签已全部本地化为 `Completa a frase`，instr 沿用 `Complete` 在拼写上无法与英文区分——proof1 按“对外内容禁英文残留”判为重大缺陷。
- 三态结论：**下半“仍在”——但是否为缺陷，取决于协调员采纳 proof1 原判还是 KIT fix-14 的反裁决。本 NOTE 不擅自裁决，给出两种裁决下的 fix1 清单（见 §3）。**

### D5 — 网 PDF 丢 P1 斜体：✅ 已不在正典（机制已修）

- PyMuPDF 全书 span 扫描（脚本 `measure_canonical.py`）：
  - 印版 italic span：**1 处**——P1 `«de groepswinst»`，Newsreader16pt-Italic，16.12 pt，bbox (1079.6, 1284.1, 1201.8, 1300.3)。
  - 网版 italic span：**1 处**——同词同页，LucernaNewsreader-Italic，16.12 pt，bbox **逐值相同** (1079.6, 1284.1, 1201.8, 1300.3)。
- 网版 1 = 印版 1，斜体面已带上。属 build 3 重导时 webpdf.py 机制修复（proof1 指出的“字体裁切未带斜体面”已不在）；无需再动 webpdf.py。

## 3. fix1 精确 scope

**正典上仍成立的确定缺陷：无。** D1、D2、D3、D5 及 D4 上半均已在 build 3 / build 4 中关闭（关闭路径见 §1 时间线）。

唯一 open 项是 **D4 下半的定性裁决**，fix1 scope 取决于协调员一句话：

### 情形 A —— 采纳 KIT fix-14（本人核实的证据支持此裁决）
- fix1 scope：**空，不改、不重建。** proof1 五项缺陷在正典全部关闭；正典 build 4（dd74de0a）可直接进入定稿流程。
- 不改的理由：`Complete` 是合法葡语 você-命令式（同版有 `Forme a frase`、`Escreva` 同型；跨版 es/it 平行）；改它反而破坏 instr 集合的一致性。

### 情形 B —— 坚持 proof1 原判（拼写与英文相同即算未本地化）
- fix1 唯一改动：59 处源码调用点 `instr="Complete"` → **`instr="Completar"`**（不定式，西语平行写法；单字替换，不改版式、不改字号；候选之二 `Completa a frase` 与类型标签重复且过长，不取）。
- 精确清单（文件 + 行号，全单在本 scratch `d4-source-sites.txt`，59 行）：
  - `production/2026-w47/2026-w47-nl-pt/content12.py`：9 处（行 252、254、256、258、260、264、266、268、270）
  - `production/2026-w47/2026-w47-nl-pt/content34.py`：22 处（行 68、70、72、74、76、80、82、84、86、90、92、94、96、165、167、169、171、173、177、179、181、183）
  - `production/2026-w47/2026-w47-nl-pt/content56.py`：19 处（行 83、85、87、89、91、93、97、99、101、103、185、187、189、191、193、210、212、214、216）
  - `production/2026-w47/2026-w47-nl-pt/content7.py`：9 处（行 21、23、27、37、39、41、53、57、59）
  - 旧串：`instr="Complete"`；新串：`instr="Completar"`；其余源码不动（`content8.py` 无此串；`bslib4.py`/`render.py`/`run.py` 无此串）。
- 重建与重导（fix1 执行方）：`run.py` → `render.py` → text.md 重导 → `webpdf.py`；预期仅 `svg/p2–p7` 六个 SVG（P1/P8 无此串）+ 两 PDF + text.md 变化；不碰核心、不碰 staging、不碰其他版。
- 重测方法（fix1 后，逐项 grep + 计数，须全绿）：
  1. text.md：`[Complete]` 0 处、`[Completar]` 59 处；`Complete` 全词 0 处；内联类型标签仍 144 实例全葡语；`答案` 仍 0。
  2. SVG：`Complete` 0 处、`Completar` 59 处，分布仍为 P2 9 / P3 13 / P4 9 / P5 10 / P6 9 / P7 9。
  3. 版式回归：P2–P7 六页无新增溢出（`Completar` 9 字母 vs `Complete` 8 字母，19.5 pt 下约 +11 px，栏内余量充足；仍须像素复核一次）。
  4. 三 SHA 重新核对（印/网/文），KIT 更新 build 5 记录；其余 D1/D2/D3/D5 不复发（本 NOTE 实测值即基线）。

## 补记（2026-11-11 20:0x UTC，本 NOTE 写成后到站的两份证据）

### 补记 1 — 本人的 hidden_files/w47 全域 grep 已完成
- 命令 `grep -rl "d70937d8" hidden_files/w47 --include=*.md|*.log|*.json|*.txt`（194.5 s）结果：除 §1 所列外，`d70937d8` 还出现于：
  - `scratch-fanout-nl/FANOUT-REPORT-nl.md:32` 与 `scratch-fanout-nl/pt.md:8`：d70937d8 是**原始 fan-out 交付构建**（12,671,956 B / 1,582,075 B / 46,025 B，门禁 ALL PASS）——即 KIT 所称 build 2 的来源，时间线 §1 的“build 2”定性再获佐证。
  - `scratch-inventory-families/INVENTORY.md:234`：同上三 SHA 一行。
  - `run-log.md:1750`：协调员派 proof1 时“SHA 自盘核实”，pt 三 SHA 即 d70937d8…——**旧 SHA 来自任务书本身**（派发时盘上即此值，正确）；re-fanout 在其后重建，proof1 验的仍是派发时的现行构建。
  - `ledger.md:1130`（19:56 UTC）与 `run-log.md:2993`：协调员已记录“验错构建”诊断及本次核查的派发（a33d8a3c）；两处均称“协调员对 d70937d8 的全树 grep 仍在后台跑，结果到后补记”——**协调员的全树 grep 结果本人截至补记时仍未见到**，此处补记的只是本人自己的 hidden_files/w47 grep。
  - `dd74de0a` 同 grep 还出现于 `run-log.md`、`ledger.md`、`scratch-delta-nl-pt/DELTA-LOG.md` 及下述 proof1b。

### 补记 2 — 正典已有另一轮独立全量复校 proof1b，结论 (a) 零缺陷
- `hidden_files/w47/scratch-proof-nl-pt1b/PROOF-NOTE.md` + `GATE-LOG.md`（mtime 2026-11-11 19:53 UTC）：复校员独立全量复校 **delta build 4（正典）**，结论 **(a) 零缺陷 — 可定稿**；D1–D5 逐项回归“全部修好、无回归”，delta D6–D11 逐项验证成立，另 4 项观察 O1–O4 不计缺陷。
- 与本 NOTE 的交叉验证：proof1b 的 D1–D5 回归结论与本 NOTE §2 逐项一致；其 D4 裁决与 KIT fix-14 相同——“尾标 `[Complete]` ×59 是葡语 você-命令式（completar），非英文残留：与 es `Completar` ×59、it `Completa` 对位”（PROOF-NOTE.md:50）。即 §3 情形 A（不改）现已有**两处独立佐证**（KIT fix-14 + proof1b 全量复校）。
- 定位说明：本核查是 D1–D5 针对性重测 + fix1 scope（非全量复校）；正典的全量复校结论以 proof1b 为准，协调员定稿时应以 proof1b 的 (a) 为主、本 NOTE 为辅。本 NOTE §3 情形 B（改 59 处）仅作为“若协调员同时推翻 KIT fix-14 与 proof1b 裁决”的备用清单留存。

- 方法：PIL 真墨水（NotoSansCJK-Bold.ttc index 2；Newsreader-Regular.ttf，`tools/fonts/`）+ PyMuPDF span（SVG px→PDF pt 系数 0.75；盒右缘 1396.5 pt = 1862.0 px）+ `pdftoppm -r 200` 条带像素扫描（阈值 <150；D2 灰字见注）。grep 均为磁盘实测值；未复用 proof1/delta 的结论作证据。
- 本 scratch 产物：`CHECK-NOTE.md`（本件）、`measure_canonical.py`（D1/D2/D5 实测脚本）、`pix-d1-6.png` / `pix-d2-2.png`（200 dpi 条带）、`d4-source-sites.txt`（59 处源码行号全单）、`d4-text-lines.txt`（59 处 text.md 尾标行号）、`probe.txt`（开工探针）。
- 未动确认：生产目录只读（除 grep/读取与 PDF 渲染外无写入）；未改任何生产文件；未 commit、未 push；未重建正典。
