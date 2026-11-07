# W45 DE×EN 独立校对报告 — ZERO PROBLEMS（可定稿）

**校对对象：** `files/weekly-report-w45-de-en/`（德语×英语分版，Die Lucerna VOL.2）
**对照：** W45 DE 核心 `files/weekly-report-w45-de-core/`（已定稿）；W43 已发同配对 `files/weekly-report-de-en/`（VOL.1）
**校对方式：** 全部从头独立重跑，不采信接续构建员或前任的任何自述；不改交付文件，不派生下级代理。
**开工查重：** 开工时进程扫描为空；校对开始（20:38 UTC）与结束（20:42 UTC）两次全量 SHA-256 快照完全一致，零新写盘。
WEEKLY-KIT.md 的 20:37 mtime 是校对开始前已完成的交付写盘（接续构建员补写的 KIT），不是进行中的渲染，
按协调员裁定正常开工。校对期间未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 `~/workspace/weekly-git`、
未改核心与 W43 目录（核心/W43 仅只读比对）。

## 结论：ZERO PROBLEMS — 可定稿

全部必查门独立重跑通过，无编号问题。两处出处缺口如实记录于 §10，不影响结论（理由见 §10）。

## 1. Freeze 门 — 通过

工具 `tools/freeze.py diff`（tools venv，Python 3.12.3 / Pillow 13.0.0 / cairosvg 2.9.1），实测与 KIT §3 计数一致：

| 页 | 增加串 | 删除串 | CJK 核心→本版 | 新增 CJK |
|----|--------|--------|---------------|----------|
| P1 | 23 | 23 | 168 → 0 | 0 |
| P2 | 36 | 32 | 186 → 0 | 0 |
| P3 | 40 | 40 | 187 → 0 | 0 |
| P4 | 25 | 22 | 155 → 0 | 0 |
| P5 | 41 | 39 | 193 → 0 | 0 |
| P6 | 36 | 33 | 228 → 0 | 0 |
| P7 | 62 | 53 | 394 → 0 | 0 |
| P8 | 150 | 141 | 1429 → 0 | 0 |
| 合计新增 CJK | | | | **0** |

另做全文件 CJK 扫描（含 SVG 属性，不只 `<text>`）：8 页均为 **0**。

**被删含德语字符串逐项裁定：** 删除串总数按串计为 23/32/40/22/39/33/53/141（distinct 数低于此，
因重复串计 count）。其中零 CJK 的删除串仅 9 条，逐项核实如下，其余删除串全部含中文，
均为讲解层（gloss 词头＋中文注释、中文注释引用德语词、中文练习指令）或家具行（栏目标题、页脚、页码行）：

- P1 `DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND`：
  核心 P1 副标题槽位行（x=975, y=372, 19pt, #57523f），属家具；本版同槽位由配对徽章原位替换
  （见 §7），非德语正文。核心 P1 卡面目视确认该行确为副标题槽位。
- P7 `Ein Beispiel der Redaktion!`：读者园地示例标题（核心 x=1473, y=848.5），属讲解层家具；
  本版同位置为 `An example from the editors!`（x=1473, y=819.0）。
- P7 `«der Tankrabatt»（Seite 2）: die`：全角括号旧式片段，本版同项已改为半角括号
  `«der Tankrabatt» (Seite 2): die`，德语词头未删。
- P7 `……`：中文省略号标点，讲解层。
- P8 6 条零 CJK 片段（`beschließen → beschlossen） · 17. Die Preise sind am Morgen`、
  `bleiben + geschlossen）`、`tanken → getankt） · 19. Die Tankstellen haben den Rabatt`、
  `）`、`） · 16. Der Bundestag hat den Tankrabatt beschlossen.（`、
  `） · 46. An Allerheiligen bleiben die Geschäfte geschlossen.（`）：
  均为答案注释改写（中文→英文、全角→半角括号）引起的重排断行伪影。逐句核实：
  `Der Bundestag hat den Tankrabatt beschlossen`、`Die Preise sind am Morgen`、
  `Die Tankstellen haben den Rabatt`、`An Allerheiligen bleiben die Geschäfte geschlossen`
  在本版 P8 连结文本中全部存在。无德语正文、练习题干或选项被删。

**核心完整性（校对员事后重哈希）：** 8 个核心 SVG SHA-256 与 build 树
`core-hashes-before.txt` / `core-hashes-after.txt` 逐值一致，核心未被触动。

## 2. P8 门 — CLEAN 150=150，keydiff 四项逐项核实通过

工具 `tools/p8.py compare --core-dir …de-core --edition-dir …de-en --target de` 实测：
`status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]`，
核心 150 noted，本版 150 noted。`extract` 单独重跑两边亦各为 150/150。

- **137（registry type=translation, A2）：** P8 §E 卡面实测 `Translate into English` +
  德语题干 `Der Tankrabatt läuft bis Dezember.`；核心键 `油价减税持续到十二月。`，
  本版键 `The fuel discount runs until December.`（注 `laufen = to run, to last`）。
  合法重定向，非提取伪影。
- **138（translation, A2）：** `Translate into English` + `Ich schaue am Dienstag Fußball.`；
  核心键 `我周二看足球。`，本版键 `I watch football on Tuesday.`（注 `schauen = to watch`）。合法重定向。
- **139（translation, B1）：** `Translate into English` + `Die Schule hat wieder begonnen.`；
  核心键 `学校又开学了。`，本版键 `School has started again.`（注 `wieder begonnen = started again`）。合法重定向。
- **140（对照项，非 keydiff）：** `Translate into German` + 英语题干 `I sleep an hour longer on Sunday.`，
  键两边同为 `Am Sonntag schlafe ich eine Stunde länger.`。佐证 137–139 确为本期仅有的三项
  DE→读者语翻译重定向（registry 中 translation 类型共 4 项，137/138/139/140，140 为反向）。
- **150（registry type=writing, B1）：** 核心键 `开放题 — 要点见写作框，范文在第 8 版写作框内`，
  本版键 `Open task — follow the points in the writing box; the model text is in the box on this page`
  （注 `Marked against the points listed`）。P8 卡面实测：写作框 `H · SCHREIBEN · Writing`
  （80–100 words, «Meine Fußballwoche»）与 `MUSTER · Model text (84 words)` 框同在 P8，
  故 "the box on this page" 准确；范文与评分要点无实质改动，仅装置语言改写。
- 无括号/dash 提取伪影：两边 joined-parse 均为干净 150 集，uncertain 为空。

## 3. Occlusion 门 — 分版 0、核心 0、NEW 0，盲区补查通过

工具 `tools/occlusion_audit.py`（自检先行通过， planted classes 全触发，clean 对照静默）实测：
`edition: 0 flags; core: 0 flags; NEW vs core: 0`，exit 0。

**盲区补查 1 — P1 顶栏同基线（y=92），真墨迹（venv PIL，与审计同方法）：**

| 文本 | 墨迹盒 x 区间 | 与下一项余量 |
|------|---------------|-------------|
| `VOL. 2 · ZWEITE AUSGABE`（x=65, start, 23pt 700） | 64.8–366.8 | 165.7 px |
| `WÖCHENTLICH AUF DEUTSCH · ONE ISSUE A WEEK · THE GERMAN THAT GERMANS READ`（x=975, middle, 21pt） | 532.5–1417.5 | 58.7 px |
| `WOCHE VOM 2. BIS 8. NOVEMBER 2026`（x=1885, end, 23pt） | 1476.2–1885.0 | — |

x 重叠 0，通过。

**盲区补查 2 — P6 图表真墨迹扫描：**

- 条形与核心几何完全一致：x=535；y=1482 w=1156 / y=1534 w=340 / y=1586 w=204（fill #3e4c2a）。
- 标签（x=425, 20pt）右墨迹缘：`family care` 526.8（余量 8.2 px）、
  **`care service` 534.8（余量 0.2 px — 最紧点，无重叠）**、`care home` 523.2（余量 11.8 px）。
- 百分比均在条末之外：68 % 起于 1707（条末 1691，余 16）、20 % 起于 891（条末 875，余 16）、
  12 % 起于 755（条末 739，余 16）。
- 图表文本与后绘矩形重叠：程序化核对 6 个图表文本 × 其后全部 rect，**重叠 0**。
- P6 卡面目视：三标签全部完整可读，`care service` 与条形间有可见空隙；ÜBUNGSDATEN 脚注行完整在页内。

0.2 px 点判定：**通过**（墨迹未触及条形；卡面亦可见空隙）。此为紧但合法的继承布局，
建议后续周期知悉，不列为问题。

## 4. Gloss 门 — 25/25，词头与顺序 1:1

按 `·` 本身拆分 build 源码 `gloss()` 调用：核心与本版均为 **5 盒 × 5 项 = 25 项**，
每盒德语词头与顺序逐盒 1:1（仅注释语言中文→英文）。25 条英文 gloss 在本版 SVG 连结文本中全部逐字找到：

- P2：der Tankrabatt = fuel discount · die Zapfsäule = petrol pump · die Energiesteuer = energy tax ·
  die Mehrwertsteuer = VAT · der Angehörige = relative
- P3：der Ferienwechsel = holiday changeover · die Schülerin = schoolgirl · der Ausflug = trip ·
  der Advent = Advent · die Lesung = reading
- P4：die Englische Woche = English week · auswärts = away · empfangen = to host ·
  der Favorit = favorite · eröffnen = to open
- P5：der Pausenhof = schoolyard · die Klassenarbeit = class test · das Referat = class talk ·
  ausschlafen = to sleep in · die Probe = rehearsal
- P6：der Angehörige = relative · die Pflegeversicherung = care insurance ·
  der Pflegedienst = care service · die Stagnation = stagnation · der Aufschwung = upturn

另核实 P1 桥接行（非 gloss 盒）4 词头完整：`Notes — die Englische Woche = English week ·
der Spieltag = matchday · empfangen = to host · die Bundesliga = Bundesliga.`。

## 5. P7 金句 — 8/8 逐字，每句恰 2×

逐句在源文章页连结文本与 P7 表中计数，每句总数恰 2（源文章 1 + P7 表 1），无第三处：

| # | 金句（德语） | 来源页 | P7 标签 |
|---|-------------|--------|---------|
| 1 | Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga. | P4 | Seite 4 · B1 |
| 2 | Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter. | P2 | Seite 2 · A2 |
| 3 | Wer 50 Liter tankt, spart rund 8,35 Euro. | P2 | Seite 2 · A2 |
| 4 | Die Schule hat nach den Herbstferien wieder begonnen. | P5 | Seite 5 · B1 |
| 5 | Die Tage sind kurz, die Abende lang. | P3 | Seite 3 · A2 |
| 6 | Zwei schwere Auswärtsspiele für die deutschen Teams. | P4 | Seite 4 · B1 |
| 7 | Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst. | P6 | Seite 6 · B2 |
| 8 | Es geht langsam aufwärts — aber von allein geht es nicht. | P6 | Seite 6 · B2 |

页码标签分布：Seite 2×2、Seite 3×1、Seite 4×2、Seite 5×1、Seite 6×2；等级：A2×3、B1×3、B2×2。
与宣称一致。表头规则句 `Quoted word for word from this issue's articles` 在 P7  present。

## 6. 读者园地（P7，es-ru 教训强制项）— 通过

P7 `LESERBRIEFE · Readers' letters` 栏（x=1473 列）SVG 文本 + 卡面双重核实，三事实与显性征集句同在该栏内：

- **事实 1 — 无真实来信：** `Editors' example, not a real letter: no real letters or best page-8 writing yet.`
  （德语伴行：`Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3.`）
- **事实 2 — 无最佳 P8 作文：** 同上英文句（`…or best page-8 writing yet.`）。
- **事实 3 — 示例＋承诺顺延 VOL.3：** 栏目标注 `An example from the editors!` ＋ 示例信全文
  `„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die Fußballwoche ist toll!
  Viele Grüße — die Redaktion"` ＋ VOL.3 刊登承诺（见征集句及德语行
  `Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.3.`）。
- **显性公开征集句（独立判定：构成显性征集）：**
  `Write to us! Send your real letters — the best will be printed in VOL.3.`
  （栏内 y=1301.61–1330.72，两行连结）。判定理由：祈使句直接邀请读者寄真实来信（`Send your real letters`），
  并给出刊登承诺；它位于读者园地栏内，不是下期预告、不是单题投稿提示。
- **未计入项（与 KIT 一致）：** 下期预告栏 `Ihre Briefe: Schreiben Sie uns! Die besten echten Briefe
  erscheinen in VOL.3!`（P7 底部 y=2511.4）与 P8 写作任务行
  `Die besten Texte drucken wir in VOL.3 (Seite 7, «Leserbriefe»)` 均未计入，栏内本身已满足要求。

## 7. 家具三方对照 — 通过，20pt 成立

实测 W43 已发 DE×EN P1 SVG（非转述）：徽章行
`TEXT IN GERMAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`，
x=975, y=372, Noto Sans CJK SC, **20pt, weight 700, fill #3e4c2a, text-anchor=middle**。
本版 P1 徽章行逐属性相同（字符串、槽位、字号、颜色、粗细、锚点、字体全部一致）。

- **字号裁定：20pt 成立。** README #20 泛写 DE 家族槽位徽章 19.5pt，但 W43 已发同配对实测为 20pt；
  按任务要求以 W43 为准，本版抄 20pt。未为凑 #20 改动或删除任何冻结德语行：
  唯一被替换的德语行是核心自有副标题槽位内容（§1），正是 #20 所述"徽章原位替换副标题槽位"的情形。
  （附注：核心自有副标题槽位实测为 19pt #57523f，可见 #20 的 19.5pt 本就是泛写，非任一实测值。）
- **页脚 8/8：** `Die Lucerna · GERMAN WEEKLY VOL.2 · German text · English explanations`
  （x=65, y=2624, 20pt, start，W43 仅 VOL.1 之差）。
- **页码行 8/8：** `Page 1 of 8` … `Page 8 of 8`（x=1885, y=2624, 20pt, end）。
- **Masthead：** `Die Lucerna`，UnifrakturMaguntia **168pt**，x=975, y=262，middle ——
  核心、W43、本版三方一致（取自核心，未改动）。
- 其余家具：顶栏 strapline（y=92, 21pt）与 W43 逐字相同；版次行（y=330, 46pt bold）
  `GERMAN WEEKLY · VOL.2 · FOOTBALL WEEK · FUEL DISCOUNT · CARE` 格式与 W43 相同（VOL 1→2、主题替换）；
  栏目标题德·英双语；P8 分隔符 `— Page N —`（N=1…8）齐全；两张公有领域图片署名行与核心逐字相同
  （P1 `Foto: Staff Sgt. Stephanie Jacobs, U.S. Air Force — public domain`；
  P4 `Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain`）。

## 8. PDF / 卡片 / 题量 / ABSTRACT / KIT 实测 — 通过

- **印刷 PDF** `Die-Lucerna-VOL2-EN.pdf`：**4,137,635 B，8 页**，页尺寸 1462.5×2025 pt，
  SHA-256 `9d12db530cc871cac670fd6e5b624a531cefd29052bbecdc23eeb647ef77611d`，与 KIT §10 一致。
- **网页 PDF** `Die-Lucerna-VOL2-EN-web.pdf`：**4,094,288 B，8 页**，页尺寸 1400×1938 pt，
  SHA-256 `fc7676359c54a8ac062451dc9c394e3f2dd354403ecd4b7e80bd876ab47f467c`，与 KIT §10 一致
  （网页 PDF < 10 MB 仓限）。
- **卡片 8/8：** 全部 1950×2700 RGB，字节数与 KIT §10 逐一一致
  （p1 1,272,716；p2 843,709；p3 827,764；p4 1,164,110；p5 758,501；p6 796,073；p7 698,882；p8 1,231,723）。
  8 张卡面全部目视：无重叠、无截断、无缺框。P3/P5 `FERIENWECHSEL · Holidays`、
  P6 `DIE ZAHLEN · Numbers` 框标题全部在框内（首版审计的 4 项溢出已修复，复测为 0）。
  目视接受的继承项（非本版缺陷）：德语低引号样式（P2 `„verschwindet "` 等，核心亦然）；
  P1 Fragen 栏色块经核心 P1 卡面比对确为核心原有设计；P6 图表 0.2 px 点见 §3。
- **SVG 几何：** 8 页均为 1950×2700。
- **练习 150 题：** registry 实测分页 10/18/18/18/18/18/12/38，等级 A2 66 / B1 70 / B2 14，
  与核心 KIT 一致；独立等级芯片序列与核心逐页相同（P1 14 · P2 15 · P3 19 · P4 16 · P5 18 · P6 18 · P7 12 · P8 21）。
- **ABSTRACT.txt：** 英文单行，无 ASCII 双引号，含真实主题关键词
  （football week, Champions League, Europa League, Bundesliga matchday 9, fuel discount to 31 December,
  autumn holiday changeover, home-care debate）与学习者搜索短语
  （`for learners who want to learn German by reading real German news`），与交付页面内容相符。
- **“桥接”扫描：** 8 个 SVG 与 KIT 全文均为 0 次。
- **工具链记录：** render.py 须用 tools venv（Python 3.12.3 / Pillow 13.0.0 / cairosvg 2.9.1，
  校对实测一致）；run.py 为纯 stdlib，前任未记录解释器，KIT 如实写明未虚构。
  校对以交付产物为准判定，不以此列为问题。

## 9. KIT 交叉核对

KIT §1–§12 的数值宣称逐项复测：freeze 计数、P8 状态与 keydiff、occlusion 0/0/0、
gloss 25 项、P7 金句表、读者园地引文、家具参数、PDF/卡片尺寸与 SHA、核心哈希——
除 §10 两处出处缺口（见下）外，全部与盘上实测一致。KIT 自身状态写明"builder-complete，未定稿，待独立校对"，
未冒充定稿结论，表述诚实。

## 10. 两处出处缺口 — 如实处理，不掩盖

**(a) 旧 render-log 过期。** build 树 `render-log.txt`（20:20）早于最终 20:23 渲染，
其值与盘上实测不符：印刷 PDF 4,137,638（实测 4,137,635）、网页 PDF 4,094,531（实测 4,094,288）、
p1 卡 1,273,137（实测 1,272,716）、p4 卡 1,164,238（实测 1,164,110）、p8 卡 1,230,645（实测 1,231,723）；
p2/p3/p5/p6/p7 卡片尺寸与实测一致。校对一律以盘上实测为准，旧日志值未作任何对照。

**(b) 最终 SVG 与 20:22 rerun 哈希差 3 页。** `svg-hashes-after-rerun.txt`（20:22）与盘上最终态比对：
p2/p3/p5/p6/p7 相同；**p1（20:22 `524ca3df…` → 盘上 `9bdbb681…`）、
p4（`6a28a691…` → `5cec412d…`）、p8（`e09b3034…` → `d5dd55f2…`）不同**。
最终 20:23 一进程运行改写了内容模块（content12/34/56/8 mtimes 20:23:20），中间态 SVG 未保留，
故 p1/p4/p8 的 20:22→20:23 文本增量无法从 build 树直接 diff。

**此缺口是否影响结论：不影响，理由如下（间接证据，明说其性质）：**
本校对未依赖任何中间态，而是对最终文件做了全新一遍核查：最终态 freeze、P8、occlusion 三门全部重跑通过；
最终 build-log 分页/等级总数（累计 10/28/46/64/82/100/112/150）与核心一致；
最终 P8 卡面键与 registry dump 在全部 keydiff 项上一致；p1/p4/p8 三页的卡面亦全部目视通过。
因此缺口未弥合（增量本身仍不可复原），但最终态的正确性已被最终态自身的全部守门独立证实，
结论不依赖对增量的猜测。

## 11. 未做事项（按任务边界）

未改任何交付文件；未向 Discord 投递；未向主聊天发送卡片/PDF；未创建 cron；
未触碰 `~/workspace/weekly-git`；未修改 W45 DE 核心与任何 W43 目录。
校对工作文件仅写于 `/tmp/deen-proof/`（临时）与本报告。

---

*校对员：独立校对（DE×EN），2026-10-27。交付产物 SHA 以 §8 为准；旧日志值作废。*
