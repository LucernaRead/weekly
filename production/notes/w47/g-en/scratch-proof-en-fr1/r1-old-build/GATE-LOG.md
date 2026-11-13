# GATE-LOG — 2026-W47 en-fr proof1（2026-11-11，复校员独立重跑，盘上实测）

Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-fr1/`
（`probe.txt`、`occlusion.log/.json`、`p8-extract.log/.json`、`p8-compare.log/.json`、`freeze.log`、`freeze-diff.log`、`print.txt`、`web.txt`、`creambox-all.log`、`creambox-check.log`、`creambox-core.log`、`creambox-check-core.log`、`creambox.py`（引自 `scratch-proof-de-es1/` 原样复制）、`creambox_check.py`（引自 `scratch-fix-de-en1/` 原样复制）、`render/print/p-1..8.png`、`render/web/p1-1.png`、`render/web/p8-8.png`、`render/crop-p1-searches-1.png`、`render/crop-p2-didyouknow-2.png`）
工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`。`TMPDIR=<scratch>/tmp`。未写 /tmp，未改源文件。

## 0. 对象核对（KIT §7 + 盘上 sha256sum，2026-11-11 09:40 UTC 实测）

| 文件 | 字节 | SHA-256（完整） | 结果 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-fr.pdf` | 29,330,444 | `14da9810fa348a577d16927d90c7c2c05e67c537c533266ff81860486b7c11a5` | 与任务书/KIT 一致 ✓ |
| `The-Lucerna-VOL4-en-fr.web.pdf` | 2,376,712 | `0f188504a65e13488a5e07c2591c9ea9fa6f2adb0b5c0b2c3719797b8d7e22c3` | 与任务书/KIT 一致 ✓ |
| `2026-w47-en-fr.text.md` | 53,239 | `b882d0e9f348bcee2270f80434a379b652460c1f5e5542ed2992c9fd799c81c3` | 与任务书/KIT 一致 ✓ |

两 PDF 各 8 页（PyMuPDF：印 8 页 1462.5×2025 pt；网 8 页）。印/网文字层：pdftotext 印 48,830 B、网 48,831 B；token 多重集差 0/0，内容同一 ✓；网 < 7 MB ✓。

## 1. 机械门（逐门重跑）

| 门 | 命令 / 位置 | 结果 |
|---|---|---|
| occlusion 审计 | `tools/venv/bin/python tools/occlusion_audit.py <ed>/svg --json occlusion.json` | **0 flags**，自检 OK（6 类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 阳性对照全触发，干净对照静默）✓ |
| p8 extract | `tools/p8.py extract --p8 <ed>/svg/p8-test.svg --total 150` | **150/150**，noted set 60/150（与核心 noted 集相同）✓ |
| p8 compare | `tools/p8.py compare --core-p8 core-en/svg/p8-test.svg --edition-p8 <ed>/svg/p8-test.svg --total 150` | **CLEAN**，missing=[] extra_count=0 uncertain=[]；keydiff=[137, 138, 139, 140, 150]（读者语翻译键+写作键，预期内，与 W46 en-fr 同）✓ ——但该门只核对版与核心一致，不核对键与题面；D1 两边同错故未拦住，见 PROOF-NOTE D1 |
| p8 extract vs registry | 提取键逐项对 `registry.json` | 150/150；仅 Q150 差异（registry 长式 vs 提取短标 `Tâche ouverte`，与核心同 pattern）✓ |
| freeze 渲染 | `tools/freeze.py baseline --build <ed> --core-svg <ed>/svg --out freeze-final` | **8/8 SVGs byte-identical**，core integrity 8 文件未变 ✓ |
| freeze diff vs core | `tools/freeze.py diff --core-svg core-en/svg --edition-svg <ed>/svg` | 每页新增串均为法语讲解/家具，删去串均为中文讲解层/W46 惯例词表行/重排 P8 键行/家具；新增 CJK 字符仅 U+3000（全版 9 个）✓ |
| creambox.py 全版扫查 | 原版（+45 px 窗口，引自 `scratch-proof-de-es1/`）对 8 页 SVG | 2 处真漫出：P1 SEARCHES 盒 -18.0（D2）、P2 DID YOU KNOW 盒 -12.7（D3）；其余负值均为已知假阳性（下块标题/流文在盒底下约 35–37 px，de 家庭同 pattern）——已逐行裁定，见 §2 |
| creambox_check.py 精炼版 | 0–8 px 溢出带，引自 `scratch-fix-de-en1/`，8 页全扫 | **NO OVERFLOW，RC=0**；但其 8 px 带漏掉了 D2（18.0 px）与 D3（12.7 px）——工具缺口，已记入 PROOF-NOTE |
| creambox 对照（core-en） | 原版 + 精炼版均跑 core-en 8 页 SVG | 原版：core 同盒同值（P1 -18.0、P2 -12.7）；精炼版：core 同样 NO OVERFLOW。D2/D3 为核心模板几何，非本版法语层引入 ✓ |
| P7 工具盒 | 上两门 P7 行 + 目视 | 工具盒 rect y=651、盒底 1038.7、盒内间隙 **+48.5 px**，无漫出 ✓（精炼版 P7 7 盒间隙 +47.7…+48.5） |
| P8 最小字号 | PyMuPDF 读印版 PDF spans + SVG 属性 | PDF 有效最小 **10.12 pt**（P8 答案键块，0.75 缩放组内；其余页最小 11.62 pt 为图片出处行）；SVG 属性最小 13.5 pt；均 ≥ §1.1 下限 9.75 pt ✓。备注：KIT “13.5 pt” 为属性值，非渲染有效值 |
| boxtitle 宽度 | occlusion 审计 BOXTITLE 类（含框题墨迹 vs 自身框界）+ P7 目视 | 审计 0 flags；P7 三处曾 HEAD TOO WIDE 的节头（ERROR CLINIC / READERS' CORNER / AN EXAMPLE LETTER）渲染中均在栏宽内 ✓ |
| keycheck | p8 extract vs registry（上）+ 150 题人工逐题核对（§3） | 机械部分 150/150；人工发现 D1（Q39/Q40 互换，registry 与 P8 印键同错）✗ |
| 引号/字符 | 8 页 SVG 文本正则统计 | “ 82 / ” 82 成对 ✓；U+2019 0 ✓；ASCII 撇号 72；U+00B7 282（与核心完全一致）；U+3000 141；真实 CJK 仅 3 字（P1 非可见 `<title>Lucerna 三色蛾</title>`，与核心共有）；“Note \| Note \|” 0；禁词（TODO/FIXME/Lorem/占位/SOP/proofread/cover/bridge/XXXX/TBD）0 ✓ |
| VOL 计数 | 8 页 SVG 逐页统计，与 core-en 逐页对照 | VOL.4 12、VOL.5 8、VOL.3 3，逐页与核心完全一致 ✓（VOL.5 均为下期预告/选项，合法） |

## 2. creambox 逐行裁定（原版 +45 px 窗口，24 行负值）

真漫出（盒内自有末行超出盒底）仅 2 行：P1 y=588 盒 `Intérêt relatif, pas des volumes exacts.` -18.0（D2）；P2 y=833 盒 `November 3.` -12.7（D3）。其余 22 行均为下块标题或盒后流文（-35.5…-37.0，如 `TRY IT NOW　À vous de jouer`、`WHAT IS ON THIS WEEK?`、`A　COMPREHENSION`、`FIVE SENTENCES`、`READERS' CORNER　Courrier` 等，距盒底约 36 px 的正常块间距）及 P2 AND YOU? 盒 +5.0（盒内，紧但未出）。P8 MODEL 盒 +92.4。裁图证据：`render/crop-p1-searches-1.png`、`render/crop-p2-didyouknow-2.png`（200 dpi，印版 PDF 裁切）。

## 3. 150 题逐题核对（text.md 全文通读 + SVG 题面核对 + registry 对照）

- 编号连续 1–150；每页 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；级别 A2 62 / B1 66 / B2 22。
- 逐题核对题面、原文、图表、算术：除 D1 外全部正确。抽查要点：Q7 B 254、Q9 C 218、Q49 A 2010–11、Q55 sold、Q83 C 19、Q84 A 33/35、Q87 C 435（254+162+19）、Q97 takes、Q100–107 演练（won/more/lost/will/published/whether/chose/win）、Q108–111 改错、Q112–119 完形（Tuesday/call/continues/will meet/writes/will certify/wears/will watch）、Q120–132 选择/阅读、Q133–136 句型、Q137–140 翻译（法译准确）、Q141–144 配对（b/c/d/a 全对）、Q145–149 对话（row/film/popcorn/show/Friday）、Q150 开放写作。
- 五组配对题逐组对 SVG 渲染核对：P2（24b/25c/26a/27d ✓）、P3（38b ✓、**39a/40d 应然 vs 印键 39d/40a ✗**、41c ✓）、P4（56b/57c/58d/59a ✓）、P5（74d/75a/76b/77c ✓）、P8（141b/142c/143d/144a ✓）。
- 金句：P7 8 句逐字出自本期正文，页码标注（P1/P2/P3/P4/P5/P6）正确。

## 4. 8 页目视（印版 P1–P8 全页 + 网版 P1/P8）

- 渲染：`pdftoppm -r 72` 自印版 PDF（`render/print/p-1..8.png`）与网版 PDF（`render/web/p1-1.png`、`render/web/p8-8.png`）；网版与印版视觉一致。
- 结果：除 D2/D3 外，无溢出、重叠、压页脚、图片与出处问题；页脚 `Page N sur 8` 全 8 页正确；刊头/徽章/栏目条齐全；P8 答案块在页内，未压页脚。
- P7 工具盒目视：三行 A2/B1/B2 均在奶油盒内，盒底留白充足（与 +48.5 px 实测一致）。

## 5. 外部事实核对（2026-11-11 网上检索 + 日历验算）

- 星期/日期（`date -d`，America/New_York）：11 月 3 日周二、8 日周日、9 日周一、10 日周二、16 日周一、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、26 日周四、27 日周五、12 月 1 日周二、12 月 18 日周五——文中 14 处星期表述全对；感恩节为 11 月第四个周四（11 月 26 日）✓。
- 选举（AP live 页 + political.org / Boston Report / bitcoinversus / 111things）：众院 254/162/19（AP 快照，AP live 现为 254/167，计票继续移动中）、参院 20/13、未定 Alaska/Mississippi、7 翻转（IA/KS/ME/NC/OH/SC/TX）、5 州长翻转（GA/IA/NV/OH/TX）、选前众院 218–214/参院 53–47、Johnson 不竞选共和党领袖、众院共和党 11 月 10 日/民主党 11 月 18–19 日选领袖——全部核对 ✓。数值为 AP call（非认证结果），与正文口径一致。
- Hunger Games（TechRadar/drawpie 等）：11 月 20 日上映、Zada 演 Haymitch、Fiennes 演年轻 Snow、McKenna Grace 演 Maysilee Donner、Lawrence 导演、Collins 2025 小说、50 届 Second Quarter Quell、2 倍 tribut、16 岁 12 区、Harrelson 演年长 Haymitch ✓。
- I'm a Celebrity（Wikipedia/Radio Times/ITV）：S26 11 月 16 日周一 21:00 ITV1/ITVX、Ant & Dec、Murwillumbah、因英格兰–西班牙国家联赛（11 月 15 日）晚一天、Unpacked 在 ITV2（Sam Thompson/Kemi Rodgers）、`How to Survive the Jungle` 特别节目 11 月 15 日、截稿时（11 月 9 日）营员未公布 ✓。
- Ashes（多家 11 月报道）：首 Test 11 月 21–25 日珀斯 Optus Stadium、Cummins 背伤缺席、Hazlewood 腿筋缺席、Smith 队长、Boland 顶替、Doggett 首秀、英格兰上次在澳赢系列 2010–11、2017–18 与 2021–22 均 0–4、2023 平局、澳大利亚 2024 年 11 月在珀斯首败印度 295 分、珀斯此前未办过 Ashes Test、首球 10:20 当地 = 02:20 伦敦 ✓。
- Anti-Bullying Week（ABA 官网）：11 月 16–20 日、主题 Break the Silence、Odd Socks Day 11 月 16 日十周年、约 800 万儿童、80%+ 学校、200+ 儿童定主题、ABA 主办、英格兰/威尔士/北爱 ✓。世界儿童日 11 月 20 日、《儿童权利公约》1989 年 ✓（2026 主题措辞未独立再核实，见 PROOF-NOTE）。
- ATP 总决赛（LiveTennis/TNT/ATP）：11 月 15–22 日都灵、两组四人、8 人名单（Zverev/Alcaraz/Shelton/Medvedev/Cobolli/Fils/Tiafoe/Jódar）与文中逐字一致、Sinner 两届卫冕冠军因膝伤缺席（10 月 6 日宣布赛季结束）✓。
- 英超第 11 轮（premierleague.com/Radio Times）：曼城–富勒姆周六 12:30、纽卡–阿森纳周六 17:30、利物浦–曼联周日 16:30，国际比赛日后回归 ✓。
- NFL 第 11 周：小马–德州人 11 月 19 日周四 20:15 ET、维京人–49 人墨西哥城 11 月 22 日周日 20:20 ET、爱国者慕尼黑赛（11 月 15 日对雄狮）后第 11 周轮空 ✓。
- 其余：Rousseau《Surprised!》1891、W.G. Grace 照片（Barraud，19 世纪 80 年代末）、Johnson 肖像（Reynolds，1772）与常识一致；Lawrence 儿童照片日期、投票亭图注细节、原声专辑 11 月 13 日、ATP 决赛“不早于 18:00”、认证窗口 11 月 10 日–12 月 18 日未独立再核实（已列入 PROOF-NOTE）。

## 6. 结论

机械门除 creambox 两处真漫出与人工发现的 D1 外全绿；全文、150 题、8 页目视、外部事实已全量复校。结论 (b)：**有缺陷，不可定稿**。缺陷：D1（严重，核心级）、D2/D3（中等，核心级）、D4（轻微，核心级）、D5（轻微，本版）。详见 PROOF-NOTE.md。
