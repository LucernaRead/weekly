# W45 KO×RU B-1 修复独立验证报告（深度 2）

- **结论：REPRODUCTION VERIFIED — B-1 解除，ko-ru 可定稿待插（上架/入 GitHub 由协调员串行做，本验证不宣布上架）。**
- 校对报告：`hidden_files/w45/ko-ru-proof/REPORT.md`（B-1 为唯一阻塞项）；修复员报告与证据：`hidden_files/w45/ko-ru-fix/SUMMARY.md` 及其同目录证据。修复员声称值在本验证中一律视为待验证声称，全部独立重做，下述每一项均为我方实测。
- 合规：全部生成/渲染/负对照均在我方 scratch（本目录 `work/` 下）进行；从未在 build 树或交付目录原地跑生成脚本；未碰 weekly-git、未改 `tools/` 下任何文件、未改交付目录（除验证只读比对）、未发 Discord、未往主聊天发卡片/PDF、未建 cron。唯一附带说明：分析脚本以 import 方式读取 build 树 `transform.py` 时在 build 树 `__pycache__/` 内生成了一个 `transform.cpython-312.pyc`（05:16:49），发现后已立即删除，build 树恢复为原先仅含 `bslib4`/`svglib` 两个 pyc 的状态；全部 `.py` 源码哈希验证前后一致（见 §5），该缓存文件不影响任何结论。

## 开工查重与快照（硬性）

- 开工时（2026-10-28 05:16 UTC）：无任何 cwd 属于本版树或含 `ko-ru` 的进程；交付物纸面最新 mtime 为 04:34（svg/cards/PDF），KIT 为修复员编辑后的 05:11，均非进行中写入。
- 快照：`work/snapshot-before.txt`（2026-10-28 05:16:08 UTC，svg×8、cards×8、双 PDF、KIT、ABSTRACT 共 20 项哈希/大小/mtime）。
- 静默复查：05:17:14（快照后 66 秒）重哈希 18 项纸面文件（svg×8、cards×8、双 PDF），与快照逐一相同，判定为已完成交付、可以开工，不是 stand down。注：该次窄口径复查文件本身只含 18 项纸面哈希（KIT/ABSTRACT 未列入该临时文件），KIT/ABSTRACT 的前后一致性由终期全量 20 项比对覆盖（见 §5），不存在遗漏。
- 新鲜核心来源：校对方 scratch 中的核心 build 副本 `hidden_files/w45/ko-ru-proof/work/scratch/corebuild/`。来源自证：6 内容文件西里尔字母字符数均为 0、中文讲解层完整（如 content12 P1 gloss 仍为中文原版 `입동 立冬、冬季开始 · …`），即未经任何 RU 变换的原始核心；我方复现输入哈希见 `work/fresh-input-hashes.txt`。

## 1. transform.py 现状核对 — 全部成立

- 哈希：现 `transform.py` sha256 `cc72648708f7192a0aab53dc1a013e3f8afcaff5dcc003c060575e8e033b84b8`，与修复员声称的最终值逐字一致；修复前副本 `ko-ru-fix/transform-before.py` 哈希 `2895b6616ed4691864d06041edd9d185dd05767d030b6d519d7ef8aaf75475cd`，与 KIT 所记修复前值一致。
- REPL：现 257 条、修复前 257 条，键集合相等、逐条取值 0 差异——**257 条原封不动**。
- FIX2FIX3：19 条，与 `fix2.py`（12 条）＋`fix3.py`（7 条）逐条键值 0 差异（fix2/fix3 以 AST 字面量解析，未执行其写盘逻辑，避免在 build 树原地改动）。分类实测：
  - fix2（12）：P5 gloss×4、P8 注×5、来信披露×1、pitch 132→102×2；
  - fix3（7）：P1 gloss×1（含 `циклон` 简写）、P8 注×6。
- KIT 侧：19 条 src/dst 在 KIT “Fix sync B-1”小节中全部在位（前 30 字符逐条命中；KIT 内 fix2-1…12、fix3-1…7 共 19 项）。
- 说明（非缺口）：任务书措辞一处把 “P1 gloss” 同时列在 fix2 的含项里，但 `fix2.py` 本身不含 P1 gloss，P1 gloss 是 fix3-1；以 fix 文件实测为准，总数仍为 19，无缺失、无多余。另：一次终端回显中 fix3-4 目的串出现过替换符，属终端渲染 artifact，Python 层逐字符检查 19 条均无 U+FFFD，字符串干净。

## 2. 独立复现（全新核心拷贝＋现 transform.py 单独运行）— 全部成立

- 运行：`tools/venv/bin/python transform.py`，exit 0；**276 ok（257 REPL＋19 FIX2FIX3）、0 skip、0 失败**，与修复员声称一致。日志 `work/fresh-transform-out.txt`（第二阶段标记后恰为 19 条 ok）。
- 6 内容文件 vs 已交付 build 文件（`work/compare-fresh-out.txt`）：
  - OUT 行处理如实说明：我方复现 OUT 行指向 scratch（核心原始 OUT 行指向 ko-core 交付目录），故原始哈希必然不同；但这只是 OUT 行一处差异——
  - **OUT 归一化后 6/6 一致**（bslib4 无 OUT 行，严格一致）；
  - **还原交付 OUT 行后 6/6 严格逐字节一致**（content12/34/56/7/8 各仅差 OUT 行中 `ko-core`（7 字符）vs `ko-ru`（5 字符）的 2 字节；行数 260/310/249/235/137/136 与交付逐一相等）。
  - 修复员“OUT 行归一化后一致、还原交付 OUT 行后严格逐字节一致”的声称**成立，不是含糊带过**。
- 19 映射 ↔ 23 内容行出现对账（`work/reconcile23-out.txt`）：以校对方旧 transform 输出为前 fix 态，逐条计数 FIX2FIX3 源串出现数与交付目的串出现数：
  - content12 差 2、content34 差 3、content56 差 10、content7 差 3、content8 差 5，合计 **23 = 任务书分布**，逐文件、逐条、总数三者全部吻合；
  - 我方新鲜复现输出中 19 条源串出现数全为 0、目的串出现数分布同样为 2/3/10/3/5；
  - 附注：旧版 vs 交付版的 difflib 行数为 3/4/11/4/6，恰为“出现数＋1 行 OUT 行”（校对方复现曾将 OUT 重定向为其 repro-svg 绝对路径），与 23 出现数无矛盾。
- 8 SVG 逐页哈希（`work/fresh-svg-hashes.txt`）：p1 `d188d1c7…`、p2 `c8ce33ac…`、p3 `de57bfbe…`、p4 `8ce74068…`、p5 `ebbea645…`、p6 `56eff22f…`、p7 `e57f374e…`、p8 `8fa66246…`——**与已交付 SVG 逐字节一致（8/8）**。
- 运行日志（`work/fresh-run-out.txt`，OUT 重定向到 scratch 后以 tools venv `run.py` 渲染）：**FLOW OVERFLOW 0 处**；P1-headline 1413、P5-feature 1268、P7 预告 2517.46、P8-keys 2456、TOTAL 150——与已交付 round-3 值**逐一相同**；另附级别 A2 51 / B1 72 / B2 27、页分布 10/18/18/18/18/18/12/38、范文 157 字，均与校对报告一致。

## 3. 幂等重跑（已交付 build 拷贝上再跑现 transform.py）— 全部成立

- 运行：exit 0，**276 skip、0 ok，文件逐字节未变**（`work/idem-before.txt` vs `work/idem-after.txt` 差分空）。
- 分解核实：skip（already applied）258 ＋ skip（superseded by fix）18 = 276，与修复员声称的分解**分毫不差**；
  - 阶段拆分：第一阶段 257 条（239 already ＋ 18 superseded，含 P1 gloss、P5 gloss×4、来信披露等 18 条被 fix 取代的 REPL 项）；第二阶段 19 条全部 already applied。
- 结论：现 transform.py 对已交付树幂等，重复运行不会改动纸面。

## 4. 负对照（我方独立设计，非复述修复员结果）— 4 项有效，全部非零退出

跳过逻辑不是无条件放行。以下均在交付拷贝的我方 scratch 内做损坏后重跑，且失败后文件哈希与损坏前一致（transform 仅在全部通过后写盘，无部分写入）：

- **Neg-A（P1 短版 gloss 损坏，content12）**：短版 `циклон.` 末尾损坏 → exit 1，AssertionError 指名 P1 gloss 的 REPL 项（中文源串 absent、长版目的串 absent、取代短版亦 absent）。
- **Neg-B2（FIX 目的串内部损坏，content56，×2 处）**：`не летают` 改为 `не летаюX` → exit 1，失败于第一阶段取代路径（指名 `听力时段飞机不起降` 项；其取代短版已被损坏，故不予放行）。注：Neg-B 首次尝试为**无效对照，已废弃、不计作证据**——仅在串尾追加 `XXX` 时，因跳过检查是子串匹配，目的串仍为损坏串的子串，致 exit 0；该结果只说明“尾部追加式损坏测不出子串检查”，不说明逻辑放行。有效的损坏必须破坏子串本身（如本项的内部改字符），Neg-B2、Neg-D 均按此标准重做。
- **Neg-C（链式 E 项终态损坏，content8）**：`instr="Переведите"` 的终态行改为 `ПереведитеXXX` → exit 1，AssertionError 指名该链式 REPL 项（源串 absent、即时目的串与终态均 absent）。
- **Neg-D（第二阶段孤立损坏，content7 pitch）**：pitch 目的串 `* 102` 改为 `* 10X` → 第一阶段 257 skip 全过、第二阶段 17 skip 后 exit 1，AssertionError 指名 pitch 源串 `cyq = fy + 66 + (i % 4) * 132`。此项单独证明第二阶段同样不是无条件放行。

## 5. 交付物未变证明＋KIT 文字核查 — 全部成立

- 终期快照：`work/snapshot-after.txt`（2026-10-28 05:19:15 UTC）与开工快照全量比对：**20 项哈希全部一致**（svg×8、cards×8、双 PDF、KIT、ABSTRACT），差分空；交付物 mtime 无刷新（svg/cards/PDF 仍为 04:34，KIT 仍为修复员编辑后的 05:11）。
- 双 PDF：印刷版 30,916,571 B、sha256 `b4756358b2b821495d18ec66b6db56c3cedba7c964957df252941a52a5907070`；网页版 3,622,912 B、sha256 `76e8b5032d0378b53f228e4d6a69d81f48d63987b63ab004bf9282dad81ffb01`——与修复员声称及校对报告逐字一致。
- build 树源码：验证结束时 6 内容文件＋transform.py 哈希与验证开始时逐一相同（未被我方改动）。
- KIT 文字改动确为 B-1 同步记录，且未伴随任何纸面变化：
  - Method 声明修正：KIT 第 41–44 行，原句后附 CORRECTION，言明该句对 fix2/fix3 为 FALSE；
  - fix2/fix3 小节标题修正：第 80 行 fix2、第 94 行 fix3 均标注 “NOT appended … at the time — corrected by the B-1 sync below”；
  - B-1 章节：第 106 行起 “Fix sync B-1”，含 19 条清单（fix2-1…12、fix3-1…7）与复现结果（276 ok、SVG 哈希前缀、1413/1268/2517.46/2456/150、276 skip 分解、前后 transform 哈希、双 PDF 哈希/大小）——经核对，KIT 所记数值与本验证实测**全部相符**；
  - KIT 自身哈希在验证期间未变（`63c38b2c4eaa6d39f38c8de7fd443ec02fd0d0526b5cbc66e509af75b7b94b41`），即 KIT 改动发生在我方开工之前，验证期间无新增改动。

## 6. 纸面门状态承接 — 成立

- B-1 是校对报告中的唯一阻塞项，其余 12 门在校对报告中已通过；按任务要求，本验证无需重做全部 12 门。
- 本验证证实纸面（svg×8、cards×8、双 PDF）哈希与开工快照逐字节一致、且新鲜复现 SVG 与交付 SVG 逐字节一致，因此校对结论的纸面基础未变，**足以承接其余 12 门的通过结论**；纸面无任何变化，故不存在“纸面变化即 NOT VERIFIED”的触发情形。

## 缺口清单

无。编号缺口 0 项。唯一须记录的非缺口说明见 §1（任务书 fix2 含项措辞与 fix2.py 实测分类的出入，以文件为准）与 §4（一次无效负对照的废弃说明）。

## 证据目录（`work/` 下）

`snapshot-before.txt`、`snapshot-recheck.txt`、`snapshot-after.txt`、`transform-analysis.txt`、`analyze_transform.py`、`fresh/`（新鲜核心复现树）、`fresh-input-hashes.txt`、`fresh-transform-out.txt`、`compare_fresh.py`、`compare-fresh-out.txt`、`reconcile23.py`、`reconcile23-out.txt`、`olddiff.py`、`olddiff-out.txt`、`repoint_and_run.py`、`repoint-out.txt`、`fresh-run-out.txt`、`fresh-svg/`、`fresh-svg-hashes.txt`、`idem/`、`idem-before.txt`、`idem-after.txt`、`idem-out.txt`、`build_negs.py`、`negs-build-out.txt`、`negA/`、`negA-out.txt`、`negA-exit.txt`、`negB/`（无效对照，废弃）、`negB-out.txt`、`build_negB2.py`、`negB2/`、`negB2-out.txt`、`negC/`、`negC-out.txt`、`build_negD.py`、`negD/`、`negD-out.txt`。
