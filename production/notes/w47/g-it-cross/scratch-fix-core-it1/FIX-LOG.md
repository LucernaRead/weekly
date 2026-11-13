# FIX-LOG — 2026-W47 core-it fix（D2 → D1 / D11 / P4·P8 收紧）

- 修理工：core-it fix 员（subagent）
- 日期：2026-11-11
- 对象：`~/workspace/weekly-git/production/2026-w47/core-it/`
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-it1/`
- 轮次：fix1（只修 D2）→ fix2（+D1）→ fix3（+D11、P4/P8 收紧）为最终定稿；fix1/fix2 的中间产物均被 fix3 覆盖，**只 commit 一次 fix3**。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0（`probe.txt`）；scratch 真实写文件通过；全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。

## 0. 定稿三件（fix3，2026-11-11）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4.pdf` | 27,726,350 B | `2ee50d92635ba496d65c09c085a9b70fbebad62a8d6f3b81c41afec4be47a412` |
| 网页 PDF `La-Lucerna-VOL4-web.pdf` | 1,790,620 B | `ab14a5b7bbf532e0633fee0006f5c19f44bc558b9ad475ad523d5bd0aaaecab0` |
| 文本导出 `2026-w47-it-zh-cn.text.md` | 52,676 B，1317 行（文件行数），150 题 | `d0c573b83fa679262c2da0734b08b1f504782829c11d29c9ed1e2c8cac08dbcb` |

改前（repair 定稿）对照：印刷 `fc5e952d08c000920329b60dd9527c98fd206f10abfda5615f374113118d2d3a`（27,726,384 B）/ 网页 `4381cdf740fc6d9ae025da733d4e4b2cd357ed299d686e5d37a345d4a3bfc3f5`（1,758,563 B）/ 文本 `adda0d31fa734151124f2ac256c746c3d120368a70bbfaf8e7367a20b4c5cf60`（52,729 B）。
SVG 变化：P1 `d301b886…`（D1）、P2 `a744e5d2…`（D2，fix1 起未变）、P3 `fe0a0e65…`（D11）、P4 `12ddd86c…`（收紧）、P8 `779aa98c…`（收紧）共 5 页变；P5 `08929554…`、P6 `621054ee…`、P7 `3746030a…` 与改前字节一致。
注：网页 PDF 比改前大 32,081 B，是 repo `tools/webpdf.py` 在 core 定稿后改过（字体子集/斜体面解析，commit 40963281），不是内容所致；印刷 PDF 反而小 34 B。文本行数 1317（`wc -l`）与改前一致，export 脚本打印的 1318 是 `len(out_lines)`（含末尾一个被 `.strip()` 去掉的空项），改前重导旧措辞同样得 1318——不是本次改动引入的差异；字节差 −53 恰为各处措辞改动的字符差之和。

## 1. D2 — P2 匹配题 25–28 选项 b、d 首行越过页面右边距（core 级）

### 1.1 发现与三重验证（改前）
- it-de proof1：PIL 真墨 b 1875.1 px（超 13.1 px）/ d 1877.8 px（超 15.8 px）；PDF span 框 b x1=1408.2 pt（超 11.7 pt）/ d 1409.7 pt（超 13.2 pt）；200 dpi 渲染 b 1406.8 pt（超 10.3 pt）/ d 1408.6 pt（超 12.1 pt）；裁图目视确认。
- it-pt proof1 第三次独立证实：PIL 真墨 b +15.6 px / d +17.7 px；200 dpi b +9.7 pt / d +11.8 pt；advance b +11.7 pt / d +13.2 pt。
- 我改前复现（`measure_candidates.py`，core 自身 `svglib` 度量）：b 右缘 1875.0 px / d 1877.8 px，与 proof1 一致（0.1 px 内）。
- 仅首行溢出，续行在界内；同组 a、c 在界内。

### 1.2 根因（记入方法备注）
`bslib4.match_set` 对每个选项用 `wrap(r, "serif", False, 23, self.w - 34)`（预算 388.5 px）断行，但 `wrap()` 度量的是**不含字母前缀**的纯文本，而渲染的首行是 `"b. " + 行`（前缀约 22 px）。凡是断行预算被填满的首行，渲染后必然向右多出约一个前缀宽。同一根因造成 §6 的 P4/P8 F 栏间侵入（见 §6），以及 §7 的系统性亚 2 pt 右缘超标。

### 1.3 修复（选 (a)，见 §1.4）：源字符串重措辞 + 提前断行（`content12.py:262/264`）
| 行 | 改前 | 改后 | 键 | 备注 |
|---|---|---|---|---|
| b | il ponte di barche per la festa del 21 novembre | il ponte di barche per la festa in novembre | b 不变 | 只去日期中的日（21），留月份；日期本身在正文（P2）及 ex. 23/120 中考查，不丢信息；断成两行与 proof1 建议的断行形状一致 |
| d | la piccola luce di cera che si accende in chiesa | la piccola luce di cera accesa in chiesa | d 不变 | 关系从句 → 分词 `accesa`，零信息丢失；`accesa` 在本期 ex. 13 “candele accese” 中已出现，是已用词汇 |

题干、左项、键、注释、其他行一律不动。只改源 `content*.py`，不改 SVG 生成件。

### 1.4 方向抉择 (a) vs (b) 与“fan-out 改写”说法的时序核实
协调员的磁盘核实（D2 范围更正）称：core 源行“本身没问题”，是 fan-out 改写了两处 frozen 意大利语——证据是 core `content12.py:262/264` 当时已是新措辞，而 it-ko/it-de 同行为旧措辞；5 个 `content*.py` 全量 diff 显示除中→韩解释层外仅此两处非 CJK 行改动；`translations.py` 无对应条目。
我核实后的结论：**选 (a)——core 采纳新措辞并修 P2 换行（即本 fix 已做的），(b)“11 版还原 core 措辞”按字面理解不可行**。理由与证据：
1. **改前 core 即为旧措辞且自身溢出**，不是 fan-out 引入：我任务开始时直接读到的 `content12.py:262/264` 就是旧措辞；同时读到的改前 `svg/p2-vita.svg` 中 b/d 两行 `<text>` 就是旧文本（x=1473.5、y=2162/2271、23 px）；我改前用该字符串复现的 PIL 值与 proof1 的 core 侧数值一致；proof1 PROOF-NOTE §5 D2 也写明“core-it/svg/p2-vita.svg 中两行 x/y/字号/文本完全相同，core 本身即溢出”；改前 P2 SVG SHA `ce286225…` 与 proof1 freeze-baseline.log 所载一致。最硬的一点：我的 fix1 编辑是以旧措辞为 `old_text` 精确匹配成功的——文件在改前必然含旧措辞。
2. **“fan-out 改写”的推断来自改后的磁盘状态**：it-pt 记录我于 10:37–10:38 UTC 已改 core（即 fix1），协调员的 diff 读到的是改后的 core（新措辞）对 editions（旧措辞）。5 文件 diff 与 `translations.py` 的结论我独立复核属实——但其正确读法是：**diff 呈现的是 fix1 之后的 core 与 editions 的差**；`translations.py`（`hidden_files/w47/scratch-fanout-it/translations.py`）只翻译 CJK 解释层字面量，确实无改写意大利语的条目/机制；fan-out 是忠实继承了改前 core 的旧措辞，而非改写。
3. 因此 (b) 若理解为“把 11 版改回旧措辞”会**恢复溢出**，不可取；若理解为“11 版采用 core 定稿措辞”，则与 (a) 的终态相同。定稿：(a)。**重 fan-out 时必须带上定稿措辞**（D2 两行 + 本轮 D1、D11、P4/P8 收紧，见 §9），勿让旧措辞残留在任何版。

### 1.5 修后验证（三法一致）
| 行 | PIL 真墨（SVG） | PDF span（印刷 PDF） | 200 dpi 渲染像素 |
|---|---|---|---|
| a（未改） | 1811.1 px（余 50.9） | x1=1359.8 pt（余 36.7 pt） | 1359.4 pt（余 37.1 pt） |
| b | **1830.9 px（余 31.1）** | **x1=1375.1 pt（余 21.4 pt）** | **1374.5 pt（余 22.0 pt）** |
| c（未改） | 1806.4 px（余 55.6） | x1=1356.4 pt（余 40.1 pt） | 1355.8 pt（余 40.7 pt） |
| d | **1821.7 px（余 40.3）** | **x1=1367.6 pt（余 28.9 pt）** | **1366.9 pt（余 29.6 pt）** |
| 续行 novembre / chiesa | 1580.3 / 1539.4 px（余 281.7 / 322.6） | — | 1185.5 / 1154.2 pt（在界内） |

P2 全页横向扫描（PIL 全 8 页 + PDF span 全 8 页 + 200 dpi 全 8 页）：除 §8 的一处既有亚 1 pt 痕迹外，无其他溢出行；P2 匹配块 200 dpi 裁图目视通过（`crop-p2-match-fix3.png`，四行均在界内、右侧留白清晰）。

### 1.6 it-ja / it-en 同样呈现 D2（只查墨迹，未改版）——(a) 漏检
- 两版 `svg/p2-vita.svg` 的 b/d 行与改前 core **字节相同**（x=1473.5、y=2162/2271、23 px、旧文本）；PIL 真墨 b 1875.0 px / d 1877.8 px。
- 两版印刷 PDF span：b x1=1408.2 pt（超 11.7 pt）/ d x1=1409.7 pt（超 13.2 pt），与 it-de 完全一致。
- 结论：**it-ja / it-en 的 (a) 零问题为漏检，待重 fan-out + 重校时覆盖**，不要另派。本 fix 只修 core，不改 editions。

## 2. D1 — P1 头条时间自相矛盾（core 级，medium）
- 改前 P1 第 3 段（`content12.py:39`）：“Domenica 22 novembre torna la Serie A con la 12ª giornata: la sera, a Bergamo, c'è Atalanta–Inter. Sabato 21 la Lazio capolista gioca in casa con il Lecce.”——同句内周日开赛与周六比赛矛盾。
- 佐证：第 12 轮始于周六 21 日——P4 “La Serie A riparte sabato 21 novembre con la 12ª giornata, che si chiude lunedì 23”（`content34.py:119`）、P1 日程 “SAB 21 — Madonna della Salute a Venezia; torna la Serie A.”、DAZN 赛程（协调员已核）。
- 修复：改为 “Sabato 21 novembre torna la Serie A con la 12ª giornata: domenica sera, a Bergamo, c'è Atalanta–Inter. Sabato 21 la Lazio capolista gioca in casa con il Lecce.”
  - **“la sera”→“domenica sera”是同一修的一部分**：裸 “la sera” 会挂到刚说的周六，而 Atalanta–Inter 是周日 20:45；不改则修完仍错。
  - 句内其余时间复核：Lazio–Lecce 周六 21 日 ✓；Atalanta–Inter 周日 22 日 20:45 贝加莫 ✓（与 P4 及 CIFRE 栏 “20.45 — l'ora di Atalanta–Inter, domenica 22 novembre” 一致）；邻段 “E domenica 22 novembre è anche il giorno dei dolci…”与“A Torino, domenica 22 novembre, si gioca la finale…”均一致。
  - 练习影响：无。ex. 5/9 只考地点 Bergamo，键不变。
- 验证：P1 段落在印刷 PDF 中 200 dpi 裁图目视通过（`crop-p1-d1b-fix3.png`）；P1 headline flow end y=1362（底 1828），build 0 overflow。

## 3. D11 — P3 “Torrazzo 意大利最高钟楼”事实错误（core 级，轻微）
- 改前（`content34.py:23`，text.md 第 317 行）：“Il Torrazzo di Cremona è il campanile più alto d'Italia.”
- 核实（公开来源）：Mortegliano 大教堂钟楼 113.20 m 为全意第一，Torrazzo 112.54 m 第二。it.wikipedia “Torri e campanili più alti d'Italia”：1º Mortegliano 113,20 / 2º Torrazzo；it.wikipedia “Torrazzo di Cremona”：“È la torre medievale e la torre in laterizi più alta d'Italia”；ita.travel：“tallest brick bell tower in Europe”。
- 修复：改为 “Il Torrazzo di Cremona è il campanile medievale in mattoni più alto d'Italia.”——加“中世纪 + 砖结构”两个限定，沿用 it-wiki 的定性；**不采纳“欧洲最高”**：Landshut 砖塔（约 140 m）更高，欧洲头衔有争议。
- 影响面：全源仅此一处 “più alto”（`grep` 核）；无练习题干/键/注释提及该头衔，键零改动；P3 段落 200 dpi 裁图目视通过（`crop-p3-torrazzo-fix3.png`）。

## 4. D12 — P1 “GIORNO PER GIORNO”缺周三 18 日（core 级）：核查结论为接受记录，不补条目
- 核查（按追加指示“先核实再补”，不编造）：
  - 全源检索：`content*.py` 与文本导出中 “18 novembre” / “mercoledì” / “MER 18” **零命中**；“18” 的命中全是时间（18:00、18.15）或尺寸数字。
  - P6 “LA STRADA DELLA MANOVRA”时间线四步：28 OTT / 9–12 NOV / MAR 17 NOV / 31 DIC——无 11 月 18 日事项。
  - P5 “IL PIANO DELLA SETTIMANA”五条：周五/周六/周日/周日/周一——无周三。
  - P1 日程现有 6 条（LUN 16、MAR 17、GIO 19、VEN 20、SAB 21、DOM 22），其余 6 条内容全部核实无误。
- 结论：**core 素材里没有 11 月 18 日的真实事项，6 天日程是编辑取舍**——修理轮 KIT §7 fix #4 记载，当时因盒子溢出主动去掉了填充性周三条目。**D12 降为接受记录，不编造条目**。
- 独立佐证（盒子容量）：用 core 自身 `wrap()` 模拟，7 条加现有脚注会使盒内容末端 byy ≈1362，超出盒底 1288（约 74 px）；盒子无法放大（下方 sommario 栏始于 1312，LA PAROLA 栏与 row-B 横线 1864 已排满）。补条目须删/缩其他内容，代价远超其信息价值。

## 5. D6/D7 评估项：P4 与 P8 F 匹配题选项伸入栏间空白——本次一并收紧
- 改前实测（PIL，含前缀；与 it-de proof1 O1 一致，0.1 px 内）：P4-b +7.7 px、P4-c +12.3 px；P8-a +18.4 px、P8-b +18.8 px、P8-c +8.2 px——均只进入 28 px 宽的空沟槽，未越版心、距下栏文字最近 ≥9.2 px、零碰撞、读者不可见（proof1 O1 原判“建议后续收紧，不拦停”）。
- 决定：**本次一并收**。理由：与 D2 同一根因、同一修复 pattern（源字符串缩短，键/注释不动）；改动面小（5 行、2 文件）；D11 已触发全量重建与全套门禁，边际成本低；一次扫清该缺陷类，免留 fix2。反面已评估：缩短略去的是冗余/次要修饰（见下表），匹配语义完整保留。
- 改动（`content34.py:196–198`、`content8.py:80–82`）：

| 行 | 改前 | 改后 | 键 | 语义说明 | 修后首行右缘（PIL） |
|---|---|---|---|---|---|
| P4-b (53) | che non ha mai perso, ancora senza sconfitte | che non ha mai perso | b 不变 | “ancora senza sconfitte”与“non ha mai perso”重复，删之零损失；“imbattuto”=不败，同义精确 | col2：821.7 px（余 139.3） |
| P4-c (54) | il gruppo di squadre che giocano tra loro | il gruppo di squadre in un torneo | c 不变 | 去“互踢”细节，留“锦标赛中的分组”；对干扰项仍唯一指向 girone | col2：943.4 px（余 17.6） |
| P8-a (144) | la parte del sistema fiscale, un livello di reddito | un livello di reddito del sistema fiscale | a 不变 | 去“la parte del”，“税制中的收入档”即税级，零损失 | col3：1377.3 px（余 34.2） |
| P8-b (143) | i soldi che pagano una misura, la sua fonte | i soldi che pagano una misura | b 不变 | 去“其来源”，“为一措施付款的钱”即资金来源（copertura） | col3：1359.8 px（余 51.8） |
| P8-c (142) | la differenza tra spese ed entrate, in rosso | la differenza tra spese ed entrate | c 不变 | 去“in rosso”，收支差即赤字（deficit 已含负义） | col3：1387.5 px（余 24.0） |

- 未改动：P4-a（余 83.4）、P4-d（余 2.4，紧但在界内，不动）、P8-d（余 18.0）。
- **未碰**：P4 成绩表行侵入沟槽（Cagliari–Frosinone +11.1、Torino–Lecce +10.2、Genoa–Milan +11.0；另两行 +30.2/+78.5 属两栏宽表格的 deliberate 跨栏）——机制不同（表格单元格，非 match_set 断行），仍留 O1 观察项。
- 修后：5 行全部回到栏内（PDF span 复核：P4 b x1=617.2 pt、c 708.6 pt；P8 a 1034.9 pt、b 1021.1 pt、c 1043.9 pt，均在各栏右缘内）；P4/P8 SVG 重排后门禁全过（§8）。

## 6. 门禁盲区备注（不修工具，只记录）
- `tools/freeze.py diff` 只做 **CJK 会计**：冻结意大利语的纯拉丁改动（如 D2 两处措辞在 core 与 editions 间的差异）对其完全不可见。
- `tools/p8.py compare` 只比**键值**：选项文本改动不改变键，同样不可见。
- 两个门禁都不能发现 core/edition frozen 意大利语文本漂移。记录在此，供后续工具改进参考；本次不改 `tools/`。
- it-nl proof1 D5 的另一面：该改写“正确且更好”，两名独立复校员一致认定新措辞更好——与本次选 (a) 一致。

## 7. D7 方法备注（不列为本次修复项）
- it-pt D7：右缘系统性小幅墨迹溢出 10 行（+1.4~+4.0 pt），根因同一类（PIL 量测与渲染器 advance 差约 0.5–0.8%），无碰撞、无裁切。只作方法备注。
- Core 侧我实测：印刷 PDF span 框超边距的共 6 处（P1 “2026”+0.2 pt、P2 图注 +0.0 pt、P2 “Una festa, una giornata verde”+1.6 pt、P5 Corot 图注 +1.6 pt、P8 范文两行 +1.8/+1.9 pt）；200 dpi 渲染真墨：P2 +0.7 pt、P5 +0.7 pt、P8 +1.0 pt；PIL（builder 度量）基本在界内（最紧 “Una festa” 1862.03 px）。三法数值互有出入、量级在 0–2 pt，正是渲染器与度量字体 advance 差的特征。**三数值在 it-de/it-ja/it-en 已发 PDF 中完全相同**——属管线系统性特征，非本次重建引入，不修。

## 8. 其他核查发现
- **P2 全页横向扫描的唯一其他痕迹**：200 dpi 下 P2 只有 “Una festa, una giornata verde”（宽盒副标题，y≈1190 pt）真墨 +0.7 pt（11 像素，约 0.25 mm）。该行元素改前改后字节一致（不在本次改动内）；span 框 +1.6 pt 与 PIL +0.03 px 互不一致，属 §7 的度量差类。**记录在案，未修**（只修 D2/D1/D11/收紧，不扩大范围；下轮 proof 可裁定亚 1 pt 痕迹是否拦停）。
- **“Foto: Canaletto”图注的原始扫描伪阳性**：朴素 PIL 单字体度量曾报其 1873.5 px（超 11.5），但 builder 自身度量为 420.7 px 宽、右缘 1860.2 px（在界内），且 PDF span +0.0 pt、200 dpi 渲染无越线。原因是朴素度量用了 CJK 字体的宽体拉丁 advance，而渲染器对拉丁用窄体回落。不是缺陷；本轮三法均以“builder 度量 + PDF span + 渲染像素”为准。
- **其余 it-nl 缺陷**（D1–D3 荷兰语框标题、D4 P2 匹配题、D8「翻譯」标签、D9、D10 直引号）均为**本版层**，随重 fan-out / 各版 fix1 处理，不由本次 core fix 修；D13 为观察项。

## 9. 门禁全表（fix3 最终构建）
| 门禁 | 结果 | 日志 |
|---|---|---|
| 构建（run.py + render.py + webpdf + export） | rc=0，0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE；TOTAL 150；A2 47 / B1 70 / B2 33；页 10/18/18/18/18/18/12/38；范文 99 词 | build-fix3.log、render-fix3.log、webpdf-fix3.log、export-fix3.log |
| occlusion audit（selftest 先过） | selftest OK（6 类阳性全触发、干净对照沉默）；8 页 **0 flags** | occlusion-fix3.log / .json |
| freeze baseline | **8/8 字节一致**，core 完整性复核通过 | freeze-baseline3.log |
| p8 extract + 键回归 | noted 150/150；SVG 键 vs 文本导出 **0 差异**；vs 改前 p8.json **0 差异**（noted 集相等）；25–28 c/b/d/a、52–55 d/b/c/a、141–144 d/c/b/a 与 proof1 已核语义一致 | p8-fix3.log / .json |
| 150 题语义核对 | 仅改动的 7 处释义逐项人工核对（D2 两行、P4 两行、P8 三行，见 §1.3/§5）；其余键与改前字节一致（P8 SVG 除 F 区外未变，P5/P6/P7 SVG 与改前字节一致） | 本 LOG §1/§5 |
| 印/网 text layer | `pdftotext` 字节相同（各 44,001 B），词数相同（各 6,897 词） | print3.txt / web3.txt |
| P8 最小字号（PyMuPDF 实测） | 全局最小 9.75 pt，P8 最小 9.75 pt，符合 SOP §1.1 下限 | — |
| creambox 全版扫描（canonical） | 29 盒；盒内清除量全部为正；8 处负窗清除量均为已知假阳性（窗下行是下一节标题/行，见下）；desc-clear 负值 −1.1…−2.1 共 9 处，均为无下行字母末行的计量 artifact，最差一处（P3 E TU，−2.1）200 dpi 裁图目视确认末行完整在盒内、下方留白清晰 | creambox-fix3.log、crop-p3-etu-bottom-fix3.png |
| BOXTITLE 真墨迹宽度 | occlusion BOXTITLE 0 flags；全页横向扫描无标题越边距（最长标题均在界内） | h-scan-fix3.txt |
| 横向漫出（PIL + PDF span + 200 dpi 三法） | P2/P4/P8 匹配行全部在界内（§1.5/§5）；全页无其他溢出行（除 §8 的 +0.7 pt 痕迹） | h-scan-fix3.txt、h-pdf-scan-fix3.txt、render-scan-fix3.txt、gutter-fix3.txt |
| 文本导出校验 | forward-miss 0 / reverse-miss 0 | validate-fix3.log |
| 目视裁图（200 dpi） | P2 匹配块、P1 D1 段、P3 Torrazzo 段、P3 E TU 盒底全部通过 | crop-p2-match-fix3.png、crop-p1-d1b-fix3.png、crop-p3-torrazzo-fix3.png、crop-p3-etu-bottom-fix3.png |
| 练习编号 | 138 单题 + 3 区间（25–28、52–55、141–144）= 150，无断号；级别与 KIT 一致 | build-fix3.log |

## 10. KIT 更新
- `WEEKLY-KIT.md` §7：新增 fix 条目 12（D2）、13（D1）、14（D11）、15（P4/P8 收紧）、16（D12 接受记录）、17（方法备注：门禁盲区 + D7）。
- §8：印刷/网页 PDF 尺寸与 pdftotext 字节更新；新增 fix-round 自检段落。
- §9：三件尺寸更新；构建日志索引加 `hidden_files/w47/scratch-fix-core-it1/`。
- §5（图片）无需改动；§2/§4 无过时断言（Torrazzo 最高一说的旧句只在正文，不在 KIT）。

## 11. Commit（本地，不 push）
- Commit hash：`36bdec2ed2b32000e512bfa65e7fb705464d8243`（main，2026-11-11，本地，未 push；`git log -1` 已核）。
- 只含 5 个源文件：`production/2026-w47/core-it/content12.py`、`content34.py`、`content8.py`、`WEEKLY-KIT.md`、`2026-w47-it-zh-cn.text.md`。不含 PDF / svg / cards / jpg 等生成件；不含 `tools/`；不含其他版。
- re-fan-out 清单（给协调员）：11 个 it 母语版须从本定稿 core 重 fan-out，带上定稿措辞——D2 两行、D1 句、D11 句、P4 b/c、P8 a/b/c；重校时覆盖 it-ja/it-en (a) 漏检（D2 同样呈现）与 it-de D1（本版级副标题，另案）；D12 不补条目；P4 成绩表行沟槽侵入留 O1。

## 附：全部源字符串改动对照
| 文件 | 位置 | 改前 | 改后 |
|---|---|---|---|
| content12.py:39 | P1 第 3 段 | Domenica 22 novembre torna la Serie A con la 12ª giornata: la sera, a Bergamo, c'è Atalanta–Inter. Sabato 21 la Lazio capolista gioca in casa con il Lecce. | Sabato 21 novembre torna la Serie A con la 12ª giornata: domenica sera, a Bergamo, c'è Atalanta–Inter. Sabato 21 la Lazio capolista gioca in casa con il Lecce. |
| content12.py:262 | P2 26-b | il ponte di barche per la festa del 21 novembre | il ponte di barche per la festa in novembre |
| content12.py:264 | P2 27-d | la piccola luce di cera che si accende in chiesa | la piccola luce di cera accesa in chiesa |
| content34.py:23 | P3 | Il Torrazzo di Cremona è il campanile più alto d'Italia. | Il Torrazzo di Cremona è il campanile medievale in mattoni più alto d'Italia. |
| content34.py:197 | P4 53-b | che non ha mai perso, ancora senza sconfitte | che non ha mai perso |
| content34.py:198 | P4 54-c | il gruppo di squadre che giocano tra loro | il gruppo di squadre in un torneo |
| content8.py:80 | P8 144-a | la parte del sistema fiscale, un livello di reddito | un livello di reddito del sistema fiscale |
| content8.py:81 | P8 143-b | i soldi che pagano una misura, la sua fonte | i soldi che pagano una misura |
| content8.py:82 | P8 142-c | la differenza tra spese ed entrate, in rosso | la differenza tra spese ed entrate |
