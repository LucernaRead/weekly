# W47 it 重 fan-out 前置：10 版手补丁盘点（PATCH-INVENTORY.md）

- 日期：2026-11-11（UTC）
- 范围：`2026-w47-it-{de,en,es,fr,ja,ko,nl,pt,ru,zh-tw}` 相对 core-it 的 `content*.py`（`content12/34/56/7/8.py` 全量；另核查 `.text.md` / `render.py` / `bslib4.py`）
- 性质：**只读盘点**。未改任何生产文件，未 commit、未 push。`git status --porcelain -- production/2026-w47/` 无 tracked 修改（仅有此前已存在的 untracked 版目录）。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 通（`9daeafb9…`，仅写了一个未引用 loose object，无分支/文件改动）；goals 侧写入正常；全程 `TMPDIR=<本 scratch>/tmp`。

## 0. 结论总览

| 版 | (c) 手补丁（须重打/合回） | (b) fix3 自动带入（9 行/版） | 机制已修自动带入（E 型标签 4 行/版） | 来源不明的补丁 |
|---|---|---|---|---|
| it-de | 0 | 9 行（D1×1、P2 b/d×2、D11×1、P4 b/c×2、P8 F×3） | 4 行 | 无（内容文件层） |
| it-en | 0 | 9 行，同上 | 4 行 | 无（内容文件层；text.md 层另见 §7） |
| it-es | 0 | 9 行，同上 | 4 行 | 无 |
| it-fr | 0 | 9 行，同上 | 4 行 | 无 |
| it-ja | 0 | 9 行，同上 | 4 行 | 无 |
| it-ko | 0 | 9 行，同上 | 4 行 | 无 |
| it-nl | **1**：`content12.py:18` masthead `spacing 11.5 → 11.0` | 9 行，同上 | 4 行 | 无 |
| it-pt | 0 | 9 行，同上 | 4 行 | 无 |
| it-ru | 0 | 9 行，同上 | 4 行 | 无 |
| it-zh-tw | 0 | 9 行，同上 | 4 行 | 无 |
| **合计** | **1 项（仅 it-nl）** | **90 行（9 行 × 10 版）** | **40 行（4 行 × 10 版）** | **内容文件层：0；text.md 层：1 处（it-en，见 §7）** |

**核心结论（与任务前提不同，请协调员注意）：exporter 报告所称“10 版 content8.py 都有 fan-out 后 proof 补丁（L80–82 释义等）、各版另有自己的补丁（如 it-es L35）”，经逐行核实，绝大部分已是 fix3 的内容——core-it fix3（本地 commit `36bdec2e`）正是为收这些漂移而做的定稿。真正不在机制里、重 fan-out 会丢的手补丁只有 it-nl 的 1 行 masthead 间距。** 其余差异要么是翻译表生成的（a），要么 fix3 已覆盖（b），要么 exporter 机制修复已覆盖（E 型标签）。

## 1. 方法与基线（可复现）

1. **三方比对**：现版（`~/workspace/weekly-git/production/2026-w47/2026-w47-it-*/content*.py`）× fan-out 冻结基线（`scratch-fanout-it/<lang>/freeze-baseline/build-copy/`）× core-it 新旧两版。
2. **基线来源**：`git show 36bdec2e^:production/2026-w47/core-it/content8.py` **取不到**——core-it 的 5 个源文件是 `36bdec2e` 本次首次入仓（`2071 insertions(+), 0 deletions`），父提交里没有该路径。fix3 前 core 文案取自 `scratch-fix-core-it1/oldmd/content*.py`（fix 轮次开工前冻结的改前副本；`md5(core-it/content8.py) == md5(git show 36bdec2e:…/content8.py) == 629b5b0a…`，现 core 与 fix3 commit 一致）。`oldmd` 与现 core 的差分恰为 fix3 的改动（§4），基线可信。
3. **决定性验证——重 fan-out 模拟（只读、内存内、不建 PDF）**：逐字复刻 `scratch-fanout-it/build_edition.py` 的源文件变换（OUT 重定向、E 节重定向、`instr="写作"`、P8 分隔符、最长优先翻译表全量替换，计数断言改为只记日志），用**当前** `translations.py`（240 条，含「翻譯」映射）分别从 fix3 前 core（`oldmd`）和 fix3 后 core（现 `core-it`）重跑 10 版，与现版逐行比对：
   - 从旧 core 模拟 → 与现版**字节全等**（`content12/34/56/7.py` 10 版全 0 行差异；`content8.py` 仅差 E 型标签 4 行/版，见 §5；**唯一例外 it-nl `content12.py` 差 1 行**，见 §3）。模拟过程**零** `rep1` 计数失配、**零**表计数失配。——即：现版 = 旧 core + 当前机制，不含任何机制外的手改（除 nl 间距）。
   - 从新 core 模拟（= 重 fan-out 预演）→ 与现版仅差 §4 的 fix3 9 行/版 + §5 的 E 型标签 4 行/版（it-nl 另 + 间距 1 行）。`content56.py` / `content7.py` 0 差异。
   - 另核：现版 vs fan-out 冻结基线：每个 `content*.py` 仅差 OUT 路径 1 行（冻结基线 OUT 指 scratch 路径，现版指版目录路径），即**冻结后无任何人再改过内容源文件**；`render.py` 仅差 BASE 路径 1 行（搬运所致）；`bslib4.py` / `svglib.py` / `run.py` 0 差异。
4. **抽查验证（a 类）**：见 §2。fan-out 当时的缩短（如 de build2 的 13 串、nl 的 13 值、zh-tw 的 cifre 重写与 44/134 注缩短）均已写进 `translations.py` 本身（例：`"主语 + 动词 + 地点 + 日期"` 的 es/fr/pt/nl/ru/ja/ko/zh-tw 值均为缩短形 `"Sujeto + verbo"` 等，表 L1385 起），故重跑可复现——模拟 0 差异已全量证明，不必逐条枚举。

工作底稿（均在本 scratch，不在生产目录）：
- `diff_all.py`、`simulate.py`——比对与模拟脚本；`diff-summary.txt`、`sim-summary.txt`——汇总
- `diff-ed-vs-fan-*.txt`（现版 vs 冻结基线）、`diff-fan-vs-coreold-*.txt`（冻结基线 vs 旧 core）、`diff-ed-vs-corenew-*.txt`（现版 vs 新 core）
- `sim-OLD-*-*.txt`（旧 core 模拟 vs 现版）、`sim-NEW-*-*.txt`（新 core 模拟 vs 现版，即重 fan-out 预演差分）

## 2. (a) 翻译层差异——不是补丁，不列入清单（抽查）

现版与 core 的全部讲解层差异均由 `translations.py`（240 条）+ `build_edition.py` 的定式变换生成，模拟已全量复现。抽查示例（it-es `content8.py`）：

| 位置 | core-it（中文键） | it-es（表值，模拟复现一致） |
|---|---|---|
| L16–17 | `"完形单选"` / `"拉齐奥 = Lazio"` | `"Cloze"` / `"Lazio"` |
| L35 | `"单选"` / `"国米 2–0 战胜科莫"` | `"Opción múltiple"` / `"El Inter ganó 2–0 al Como"` |
| L69–75（E 节，除 type 外） | `"圣母健康节人们走过还愿桥。"` 等 | `"Para la Madonna della Salute, …"` 等（E 节重定向，`instr` 本地化） |
| L84 | `"manovra=预算法案 d"` 等 | `"manovra = proyecto de presupuestos, d"` 等 |
| L103–105 | 写作桥接中文 | `"Tarea de escritura (sin respuesta única); …"` |

另：D 节 Q134 注 `"主语 + 动词 + 地点 + 日期"` → es `"Sujeto + verbo"`（缩短形）**就是表值**（表 L1385–1390），不是版内手改；同理 Q136 `"Sujeto + verbo + lugar"`、zh-tw cifre 行重写与 44/134 注缩短，均已进表。各版 RECORD 记载的 fan-out 当时缩短（de build2 13 串、nl 13 值、zh-tw 5 值预缩短等）全部已在表内，模拟 0 差异为证。

## 3. (c) 手补丁清单——共 1 项

### C-1（唯一）：it-nl `content12.py:18` masthead 字距 11.5 → 11.0

- **版 / 文件:行**：it-nl / `content12.py:18`
- **旧文案（机制产出）→ 新文案（现版）**：
  `p.text(975, 330, "ITALIAANS WEEKBLAD　VOL.4　LA SERIE A　IL TORRONE　VENEZIA", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)`
  → `… spacing=11.0`（其余字节全同）
- **来源轮次**：fan-out nl **build1→build2**（非 proof 轮；`scratch-fanout-it/nl/RECORD.md` Build history）。build1 门禁 19/20，唯一失败 `[EDGE] p1-prima.svg "ITALIAANS WEEKBLAD" ink box (-2.7, 303.75, 452.3, 331.5) outside the page`；根因：P1 masthead 以 `x=975` 居中 + 字距 11.5 绘制，荷兰语刊名是 10 版中最长的拉丁刊名，带子比页面宽约 5.4 px。**只改了版源文件**（RECORD 原话 "Fix at source (edition file only)"），未进 `translations.py` / `build_edition.py`（字距是数字字面量，本来就不在表里）。
- **处置意见**：**重 fan-out 后重打**（`spacing 11.5 → 11.0`，仅 it-nl `content12.py:18`），否则 masthead 溢出复现；或更彻底——在机制里加一条 nl 专用的 masthead 字距规则（core 的 11.5 对中文刊名合适，只荷兰语译名超长，合回 core-it 是错的）。重打后须重跑 gates 验 `[EDGE]` 消失（build2 门禁全过，首节点 x=10.5）。
- **备注**：冻结基线里已是 11.0（build2 后冻结），所以“现版 vs 冻结基线”看不出它；只有“机制模拟 vs 现版”能发现它。这正是本次盘点要防的漏网类。

## 4. (b) core fix3 已覆盖的差异——重 fan-out 自动带入，无须重打（9 行/版 × 10 版）

fix3（commit `36bdec2e`，`W47 core-it fix: D1/D2/D11 + P4/P8 matching tightening`；FIX-LOG 在 `scratch-fix-core-it1/FIX-LOG.md`；定稿三件见其 §0，§11 有明确的重 fan-out 清单）。以下 9 行在 10 版现版中**行号、旧文案全同**（已逐版 grep 核实，如 `Domenica 22 novembre torna` 每版恰 1 命中、F 旧释义每版恰 1 命中），重 fan-out 后自动变为新文案：

| # | 逻辑修复 | 文件:行（现版） | 旧文案（现版）→ 新文案（core-it fix3） | 来源 |
|---|---|---|---|---|
| B-1 | D1：P1 头条时间自相矛盾 | `content12.py:39` | `"Domenica 22 novembre torna la Serie A con la 12ª giornata: la sera, a Bergamo, c'è Atalanta–Inter. …"` → `"Sabato 21 novembre torna la Serie A con la 12ª giornata: domenica sera, a Bergamo, c'è Atalanta–Inter. …"`（“la sera”→“domenica sera”是同一修的一部分，Atalanta–Inter 为周日 20:45） | core fix3 FIX-LOG §2；佐证 P4 `content34.py:119` “riparte sabato 21” 及 DAZN 赛程。**即 exporter 报告的 “it-es content12 L35 'Domenica 22 novembre'”**（行号差 4，同一句） |
| B-2 | D2：P2 匹配题 Q26 选项 b 首行越版心 | `content12.py:262` | `"il ponte di barche per la festa del 21 novembre"` → `"il ponte di barche per la festa in novembre"` | it-de proof1 发现（PIL 真墨 b 1875.1 px 超 13.1 px）、it-pt proof1 独立证实；fix3 FIX-LOG §1。**即 exporter 报告的 “Q26 释义”**。附：it-nl proof1 D5 曾把此差异记为“freeze 违规（fan-out 改写）”，fix3 FIX-LOG §1.4 已核实方向：改前 core 即为旧措辞且自身溢出，不是 fan-out 引入；定稿方向 (a) = 采用新措辞，与 D5 的修法方向一致 |
| B-3 | D2：P2 匹配题 Q27 选项 d 首行越版心 | `content12.py:264` | `"la piccola luce di cera che si accende in chiesa"` → `"la piccola luce di cera accesa in chiesa"` | 同 B-2。**即 exporter 报告的 “Q27 释义”** |
| B-4 | D11：P3 Torrazzo“全意最高钟楼”事实错 | `content34.py:23` | `"Il Torrazzo di Cremona è il campanile più alto d'Italia."` → `"Il Torrazzo di Cremona è il campanile medievale in mattoni più alto d'Italia."` | fix3 FIX-LOG §3；核实：Mortegliano 113.20 m 第一、Torrazzo 112.54 m 第二（it.wikipedia）；未采纳“欧洲最高”（Landshut 约 140 m 有争议） |
| B-5 | P4 匹配题 b 伸入栏间空白 | `content34.py:197` | `"che non ha mai perso, ancora senza sconfitte"` → `"che non ha mai perso"`（删重复修饰） | fix3 FIX-LOG §5（与 D2 同根因：`wrap()` 预算不含字母前缀）；键 b 不变 |
| B-6 | P4 匹配题 c 伸入栏间空白 | `content34.py:198` | `"il gruppo di squadre che giocano tra loro"` → `"il gruppo di squadre in un torneo"` | 同 B-5；键 c 不变 |
| B-7 | P8 F 匹配题 a 伸入栏间空白 | `content8.py:80` | `"la parte del sistema fiscale, un livello di reddito"` → `"un livello di reddito del sistema fiscale"` | fix3 FIX-LOG §5；键 a 不变。**即 exporter 报告的 “L80 释义”**（其所谓“fan-out 后 proof 补丁”实为 fix3 前 core 旧文案） |
| B-8 | P8 F 匹配题 b 伸入栏间空白 | `content8.py:81` | `"i soldi che pagano una misura, la sua fonte"` → `"i soldi che pagano una misura"` | 同 B-7；键 b 不变。**即 “L81 释义”** |
| B-9 | P8 F 匹配题 c 伸入栏间空白 | `content8.py:82` | `"la differenza tra spese ed entrate, in rosso"` → `"la differenza tra spese ed entrate"` | 同 B-7；键 c 不变。**即 “L82 释义”** |

补充：fix3 还改了 core `WEEKLY-KIT.md` 与 core `.text.md`（非版文件，不计入上表）；D12（缺周三 18 日）核查结论为**接受记录、不补条目**（core 素材里无 11 月 18 日真实事项，FIX-LOG §4），重 fan-out 不产生该项。另 fix3 FIX-LOG §11 注：it-ja/it-en 的 D2 属漏检（只查墨迹未改版），重 fan-out + 重校时覆盖——此为重校范围提醒，不是补丁。

## 5. 机制已修、重 fan-out 自动带入——E 节型标签「翻譯」4 行/版

`content8.py:69/71/73/75`（E 节 Q137–140）的 type 仍是中文 `"翻译"`（fan-out 时 `translations.py` 有意不映射，W46 前例）。exporter 机制修复（`scratch-fix-export-it1/`，FIX-LOG + MECHANISM-FIX-REPORT）已补映射（表 239→240 条）+ `build_edition.py` 计数与残留 CJK 门收紧。重 fan-out 后 10 版自动本地化：en Translate / de Übersetzen / fr Traduire / es Traducir / pt Traduzir / nl Vertalen / ru Переведите / ja 翻訳 / ko 번역하기 / zh-tw 翻譯。**无须重打。**

text.md 层同一问题的既有手修（仅 text.md，不在内容源文件，不计入 (c)）：
- it-es：fix1（commit `8f2bba56`）手修 text.md L969/971/973/975 四行 `[· 翻译]` → `[· Traducir]`；机制修复 harness Phase 2 已验证：修后机制重导出与 fix1 手修的 text.md **字节全等**（56,267 B，SHA 一致）。重 fan-out 后由机制复现，无须重打。
- it-en：text.md 同 4 行已是 `[· Translate]`（现版 vs 冻结基线差恰 8 行 = 4 行 × 2），但 `content8.py` 仍含「翻譯」；见 §7 来源不明。
- 其余 8 版 text.md 与冻结基线 0 差异（仍带「翻譯」），重 fan-out 后由机制一次性本地化。

## 6. 其他内容文件核查结果

- `content56.py`、`content7.py`：10 版全部 0 差异（模拟新旧 core 皆 0），无补丁、无 fix3 项。
- `content12.py` 除 §3（nl 间距）与 §4（B-1/B-2/B-3）外无差异；`content34.py` 除 §4（B-4/B-5/B-6）外无差异；`content8.py` 除 §4（B-7/B-8/B-9）与 §5（E 型标签）外无差异。
- 非内容文件：`render.py` 仅 BASE 路径行差异（冻结基线指 scratch 路径，现版指版目录路径；另有 PDF 名 `La-Lucerna-VOL4.pdf` → `La-Lucerna-VOL4-<CODE>.pdf`，均为机制定式变换）；`bslib4.py`（PAGE_LINE 本地化）、`svglib.py`（ru/zh-tw 变体、ja/ko 索引 + kinsoku）、`run.py` 均为机制定式变换，无手补丁。

## 7. 来源不明的补丁——有 1 处，但只在 text.md 层，不在内容文件

- **it-en `.text.md` L969/971/973/975 四行 `[A2/B1/B2 · 翻译]` → `[· Translate]`**：现版与冻结基线差恰此 4 行。exporter FIX-LOG §1 已注记：“it-en 的 text.md …已是 `[A2 · Translate]`（自读记录称当时仍是「翻譯」，说明之后有人手改或重导过 text.md；其 content8.py 仍含「翻譯」，未入仓、无 git 历史可查）”。**无 commit、无 FIX-LOG、无 scratch 记录可追溯，来源不明。** 处置：无须追查重打——机制修复的映射值正是 `"Translate"`（取值依据即 it-en 磁盘 text.md 已确立的结果），重 fan-out 后机制自动生成同一标签；预期与现手修版字节一致（es 同类项已由 harness 验证字节全等；en 未经 harness 实跑验证，建议重 fan-out 后对 it-en text.md 做一次字节比对确认）。
- **内容文件层来源不明的补丁：0。** 唯一的 (c) 项 C-1 来源明确（nl RECORD build1→build2）。

## 8. 已报未修、不是补丁——重 fan-out / fix1 轮次待办（防丢清单）

以下均为各版 proof1 PROOF-NOTE 已报、但**源文件未改**（模拟 0 差异为证）的缺陷/观察，**不计入 (c)**，重 fan-out 本身不修它们，须在重 fan-out 前后另行处理：

| 版 | 待办 | 备注 |
|---|---|---|
| it-de D1（本版级，§5） | P1 奶油盒副标题 `"Cosa succede, giorno per giorno"` 前缀德语过长，墨迹超盒右缘/版心约 10 pt | 建议修法：表值 `"Diese Woche"` → `"Die Woche"`（省约 17 px）或字号 19→18；**修 `translations.py` 的德语值**，重 fan-out 前改则自动带入 |
| it-nl D1–D3（本版级，严重） | P1/P2/P7 BOXTITLE 荷兰语后半漫出奶油盒（分别超 113.2 / 136.8 / 59.2 px） | 修法 PROOF-NOTE 建议“缩短 `translations.py` 中该标题的荷兰语值或缩小字号”；重 fan-out 前改表则自动带入 |
| it-nl D4 | P2 匹配题溢出版心 | 由旧 Q26/27 长措辞引起，fix3（B-2/B-3）已缩短，重 fan-out 后复核即可 |
| it-nl D9 / D10 | Q92 注 `"Groei Prognose"` 应为 `"Groeiprognose"`；Q32 注直引号应为 «Fate dolci» | 均为**表值**（`"Groei Prognose…"` 在表 L1755）；重 fan-out 前改表 |
| it-nl D8、it-pt D6、it-ru D5、it-en D-1、it-es D1 | E 节型标签「翻譯」残留 | 机制已修（§5），重 fan-out 自动带入 |
| it-fr D1–D4 | P1/P2/P7 法语盒标题漫出（+173 / +27.2 / +30.8 / +46 px）；D5 法语讲解层字体违反 SOP §1.1 | 标题类修表值；D5 属字体/机制面，另案 |
| it-pt D2–D5 | P1 副标题、P1/P2/P7 盒标题漫出 | 同上，修表值/字号 |
| it-ru D2–D4 | P1 副标题、P1/P7 栏目标题越版心（+31.9 / +27.0 / +23.2 pt） | 同上 |
| it-ko D3 | P5 盒内两处孤悬 `）` | ko 版级外观，另案 |
| it-pt D7、it-de O1 等 | 右缘亚 2 pt 系统性墨迹溢出（观察项） | fix3 FIX-LOG §7 方法备注，未列为修复项 |
| 各版 O 项（如 it-en O-1–O-10） | 观察/风格项（cifre 英译冗余、引号风格、全宽冒号等） | 非缺陷，不拦停，复校员裁定 |

**给协调员的前置建议**：重 fan-out 之前，先把上表中“修表值”的待办（de D1、nl D1–D3/D9/D10、fr D1–D4、pt D2–D5、ru D2–D4）改进 `translations.py`，否则重跑后原样复现；C-1（nl 间距）须在重 fan-out 后重打（或机制加规则）；core re-proof（`scratch-proof-core-it3/`）目前只有检查日志、尚无 PROOF-NOTE 与 fix，若其后落 fix4，须在重 fan-out 前 fold 进 core。

## 9. 回报（任务要求）

- **手补丁 (c)**：10 版合计 **1 项**——it-nl 1 项；其余 9 版各 0 项。
- **fix3 自动带入 (b)**：每版 **9 行**（5 处逻辑修复：D1、P2 b/d、D11、P4 b/c、P8 F），10 版合计 90 行；另 E 型标签机制修复每版 4 行自动带入。
- **来源不明的补丁**：内容文件层**无**；text.md 层有 1 处（it-en 4 行 Translate 标签手修，无 commit/日志可查；机制已覆盖，无须重打，建议重 fan-out 后字节比对确认）。
- **本报告**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-inventory-it-patches/PATCH-INVENTORY.md`
