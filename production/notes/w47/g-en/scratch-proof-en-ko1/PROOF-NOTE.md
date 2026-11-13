# PROOF-NOTE — W47 en-ko · proof1（独立复校）

- 版：`production/2026-w47/2026-w47-en-ko/`，刊期 2026-11-16–22，VOL.4
- 结论：**(b) 缺陷清单，不可定稿**
- 复校员：独立 proof1（与建版者非同一人）；只复校，未改任何源文件、未重建、未 commit、未 push、未动 `tools/`、未碰 core-en
- 交付：`GATE-LOG.md`（逐门结果 + 完整 SHA）、`render/`（8 页印版 + 网 P1/P8 + P3/P5/P7 放大裁切）

## 缺陷清单

### D1（核心级·重大）P4 Ashes 整版内容错了一年
2025–26 Ashes 系列赛已于 **2025-11-21 至 2026-01-08** 打完，澳大利亚 4–1 获胜；首场测试赛 2025-11-21–22 珀斯，澳大利亚 8 个 wicket 两天取胜。本期（刊期 2026-11-16–22）把该系列赛写成即将在 **2026-11-21 周六**珀斯开打，整整错了一年；2026 年 11 月并无 Ashes，下一届在 2027 年英格兰。

失实点（均为 2025 年 11 月事实）：Cummins 背伤缺阵 / Smith 代任队长 / Boland 顶替 / Doggett 可能首秀 / Hazlewood 腿筋伤；“Perth Stadium 从未办过 Ashes 测试赛”自 2025 年 11 月起已不成立；“英格兰上两次访澳 2017–18 与 2021–22 均 0–4 失利”——至 2026 年 11 月最近一次访澳是 2025–26（1–4 失利）；“上一届系列赛是 2023 年英格兰打平”——至 2026 年 11 月上一届是 2025–26；“测试赛 11 月 21–25 日”即 2025 年赛程；“首日已售罄”为 2025 年事实。

波及：P1 简讯（IN BRIEF "ASHES Sat, Nov 21…"）、P1 搜索榜第 2 位 "ashes"、P1 导语（"…the Ashes to Perth"）、P2 "WHAT IS ON THIS WEEK?"（"On Saturday, November 21, the Ashes begin in Perth"）、P4 整版主文 + "WHY PERTH?" 框 + "SATURDAY, NOVEMBER 21" 框 + 练习 Q46–51 / 52–55 / 60–63、P5 "THE JUNGLE, TOO"（"the Ashes begin on Saturday morning in Perth"）、P7 金句（"The Ashes are not a sport for early nights."——引文逐字无误，但所引文章本身失实）、P7 "NEXT WEEK"（"The Ashes, second week in Perth"）、P8 Q125（"The first Ashes Test starts on… C. Sat, Nov 21"，答案键与失实文章内部一致）。附带：W46 en-ko P7 "NEXT WEEK" 预告中 "The Ashes begin in Perth on Saturday, November 21" 已含同一错误，说明该错误自 W46 预告即已埋下。

根在 **core-en**（核心文本与本版一致），须报协调员、由核心层修正并联动全部 12 个读者语版；本版单独无法修。严重度：重大——整版主故事 + 跨 7 页的连锁引用全部失实。

### D2（核心级·重大）P3 C 词汇配对 Q39/Q40 答案互换
印版释义顺序（P3 印版 + SVG 节点顺序一致）：
- a = "a person who teaches and guides you"（= mentor）
- b = "a person chosen to take part in the Games"（= tribute）
- c = "a person who lives with you in the jungle camp"（= campmate）
- d = "the place where the Games are fought"（= arena）

答案键：38 tribute→b ✓、**39 mentor→d ✗（应为 a）**、**40 arena→a ✗（应为 d）**、41 campmate→c ✓。
错误同时存在于 `registry.json`、text.md 答案区、P8 印版 ANSWERS 块（"38. b · 39. d · 40. a · 41. c"），读者按答案键自查会得到错误结果。根在 **core-en**（核心 registry 与 text.md 键与本版完全相同：39=d、40=a，释义顺序亦同），须报协调员。

### D3（ko 版独有·中）P5 "ODD SOCKS, IN NUMBERS　숫자로 보기" 框题跑出奶油框
- 标题 23pt 粗体 sans，建版自有 `svglib.text_w` 实测 424.1px（boxtitle-ko.py：422.9px），起于 x=106，止于 530.1；奶油框右缘 510.5 → **超出约 19.6px（boxtitle 口径 18.4px）**。
- 放大裁切（`render/crop-p5-oddsocks.png`）目视确认：标题末尾 "보기" 落在框外白纸上，框边从 "로" 与 "보기" 之间切过。
- occlusion 审计未报：其 BOXTITLE 检查只覆盖有描边或填色 `#2c2822` 的矩形，奶油色 `#f0eee5` 无描边框不在候选内——该类缺陷的工具盲区（boxtitle-ko.py 捕获）。
- 修法建议（仅供协调员/建版者参考）：缩短韩文标题或缩小字号；本复校不改源文件。

## 仅作观察（非缺陷）
- **O1** P3 "HAYMITCH'S GAMES　헤이미치의 경기"：424.1px 口径下 401.9px，止于 1859.4，框右缘 1862，**余量仅约 2.6–3.8px**，入框但极紧。目视确认在框内。
- **O2** P2/P6 佐治亚决选句为条件式教学句（"In Georgia, a Senate race with no majority winner goes to a runoff on December 1"），佐治亚决选法本身正确；但本期算术（35 席中 33 席已定、仅 AK/MS 未定）暗含佐治亚已定，存在轻微内部张力。条件式措辞，无直接矛盾。
- **O3** P7 "VOL.3 promised real letters from VOL.4"：W46 实际措辞为条件式（"And your real letters, if they arrive"），W47 此句将其表述为承诺，略有夸大；实质处理诚实无误（无来信、承诺保留、真信自 VOL.5 起刊登），且与 W46 P7 编辑示例（"no real reader letters had arrived when this issue went to press"）一致。
- **O4** `·` 分隔符：U+00B7 见于术语注释行与 P8 答案分隔（P8 184 处），继承自核心与 W46 ko 翻译记忆库、全周一致；各栏目标题与页脚用全角空格 U+3000，符合 §1.1。
- **O5** KIT §3 "P8 min font 13.5pt"：实测 P8 最小字号 10.125pt（答案块，SVG 13.5px）——13.5 是 px 数而非 pt。仍 ≥ §1.1 底线 9.75pt，通过；仅 KIT 措辞口径问题，非本版缺陷。
- **O6** P5 配图说明 "Children from Lawrence, Massachusetts, marching in New York on February 19, 1912"：照片本身为真（Bain News Service，经美国国会图书馆，1912 年 Bread and Roses 罢工期间劳伦斯儿童赴纽约）；具体日期 2 月 19 日未能从所查公开来源中确认（首批 119 名儿童 2 月 10 日抵纽约、另有一批 92 名儿童在第五大道游行，日期未核定）。无反证，不列为缺陷，请协调员复核该日期。
- **O7** P5 "约八百万儿童"：对照 NCB 官方 "逾 750 万" 为可接受约数。

## 已核实无误（要点）
- 全文 1305 行通读；150 题答案键与 registry 150/150 一致；P8 抽取键与 registry 比对仅 2 处可解释差异（见 GATE-LOG）。
- 外部事实逐项核实属实：中期选举（美联社 11 月 8 日数据：众院 254–162、19 未定；参院 20–13、AK/MS 未定；7 席翻转全归民主党；5 州长翻转；选前 218–214 / 53–47；第 120 届国会 2027-01-03 就职）、I'm a Celebrity 2026（11 月 16 日周一晚 9 点 ITV1，Ant & Dec，Murwillumbah，Unpacked 在 ITV2，因 11 月 15 日英格兰对西班牙欧国联比赛推迟一天）、ATP 总决赛 2026（11 月 15–22 日都灵，八人名单无误；Sinner 为 2024+2025 两届冠军、膝伤缺席）、英超 11 月 21–22 日赛程、NFL 第 11 周（小马–德州人 11 月 19 日周四休斯顿晚 8:15 ET；维京人–49 人 11 月 22 日周日墨西哥城晚 8:20 ET；爱国者该周轮空）、反欺凌周（11 月 16–20 日，主题 "Break the Silence"，Odd Socks Day 十周年，200 多名儿童参与选定主题）、《饥饿游戏：日出时分收割》（11 月 20 日周五上映，Zada / McKenna Grace / Ralph Fiennes / Francis Lawrence，改编自 Collins 2025 年小说，第 50 届、选手翻倍；原声专辑 11 月 13 日发行、多方信源确认）、Mike Johnson（11 月 4 日宣布不竞选新一届众议院共和党领袖；领袖选举 11 月 10 日）、密西西比常规大选无决选。
- 全部日期/星期均用 `date` 核验通过；P7 金句 8 条与原文页面逐字一致；P6 图表数字内部一致（254/162/19；20/13/2；翻转 7；州长 5；254+162+19=435）；P8 完形叙事星期一致。
- 图片与出处：国会大厦（Noclip，PD，Wikimedia Commons）、火鸡（Audubon）、Rousseau《Surprised!》1891、W. G. Grace（Herbert Rose Barraud，1880 年代末，PD）、劳伦斯儿童（Bain News Service，经 LoC，PD）、投票亭（Kenneth C. Zirkel，CC0）、Samuel Johnson 肖像（Reynolds 1772，PD）、国会图书馆主阅览室（Carol M. Highsmith，PD）——出处齐全。
- 目视：印版 P1–P8 + 网版 P1/P8 全页干净，无溢出/重叠/压页脚（除 D3 外）；P7 工具盒墨水全部在盒内（见 GATE-LOG creambox）；P8 答案块字小但完整、未压页脚。
