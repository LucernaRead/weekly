# PROOF-NOTE — W47 en-ko · proof1（独立复校，en re-fanout #2 重建版）

- 版：`production/2026-w47/2026-w47-en-ko/`，刊期 2026-11-16–22，VOL.4
- 结论：**(a) 定稿零缺陷**（观察项 O1–O6 为非缺陷记录，不修）
- 复校员：独立 proof1（与建版者/fan-out agent 非同一人）；本轮会话 `248f4608-a118-4c3b-ba55-f36af524d2d8`
- 只复校，未改任何源文件、未重建生产件、未 commit、未 push、未动 `tools/`、未碰 core-en
- 交付：`GATE-LOG.md`（逐门结果 + 完整 SHA）、`render/`（8 页印版 + 网 P1/P8 + P3/P5/P7/P2 放大裁切）

## 缺陷清单

无。ko1（旧版）的三项缺陷在本重建版中全部已修复，逐项复核如下：

- **ko1 D1（Ashes 整版错一年）→ 已修复**：P4 已全文改写为 2025–26 回顾（“Perth, One Year On: How Australia Kept the Ashes”）。首场 2025-11-21 周五珀斯、澳大利亚两天 8 wicket 取胜、系列赛 2025-11-21–2026-01-08、总比分 4–1，Cummins 背伤 / Smith 代任队长 / Boland / Doggett 首秀 / Hazlewood 腿筋伤一律过去时；P1 简讯、P1 搜索榜（“ashes” 已撤下）、P2 “WHAT IS ON THIS WEEK?”、P5 “THE JUNGLE, TOO”、P7 金句与 “NEXT WEEK”（“England's rematch waits until June 2027”）连锁引用全部改为回顾口径；“Perth is winning” / “Ashes begin” / “second week in Perth” 全版 0 处。外部复核：Wikipedia 2025–26 Ashes 系列赛（21 Nov 2025–8 Jan 2026、Australia won 4–1、1st Test 21–22 Nov 2025 Perth、Australia won by 8 wickets、shortest by balls since 1888）逐项吻合；Q46（首场 2025-11-21 珀斯）A、Q52 hosted、Q55 won、Q125（4–1）A 均与回顾一致。
- **ko1 D2（P3 C Q39/Q40 答案互换）→ 已修复**：四源一致——registry（39 mentor→a，40 arena→d；38 b、41 c）、text.md 答案区（39 a、40 d）、P3 SVG C 配对释义顺序（a = teaches and guides you、b = chosen to take part in the Games、c = lives with you in the jungle camp、d = place where the Games are fought）、P8 抽取键（38–41 = b/a/d/c）。P8 印版 ANSWERS 块亦为 “38. b · 39. a · 40. d · 41. c”。
- **ko1 D3（P5 ODD SOCKS 框题出框约 19.6px）→ 已修复**：标题改为 “ODD SOCKS, IN NUMBERS　숫자로”，源级实测 375.4px、SVG 实测余量 +29.1px；放大裁切 `render/crop-p5-oddsocks.png` 目视确认标题全在奶油框内，右侧留白清晰。

## 仅作观察（非缺陷）

- **O1** P3 “HAYMITCH'S GAMES　헤이미치의 경기”：SVG 实测 advance 401.9px，框右缘 1862，余量 **+2.6px**；PIL 真墨余量 **+2.5px**。入框但极紧（ja 姊妹版同标题 +1.5px 更紧，本版重测亦为个位数余量）。放大裁切 `render/crop-p3-haymitch.png` 目视确认：末字 “기” 完整在框内，字形无裁切、真墨未压框边、未碰他元素；与备份旧版相比为修复而非回归（旧版同标题 401.9px，同一数值）。按 STRADDLE 裁定规则不构成缺陷。注：源级 `boxtitle-ko.py` 对该标题标 OVER（400.7px vs 386.5px 通用预算）是口径 artifact——该奶油框实为更宽框（内宽 404.5px），以 SVG 实测 sweep（18/18，0 溢出）为准。
- **O2** P2 “AND YOU?” 框末行基线余量 **+5.0px**：框底 1544.9，末行 “요.” 基线 y=1539.85。放大裁切 `render/crop-p2-andyou.png` 目视确认：末行（含 “요” 下行笔画）完整在框内，下方仍有奶油边。紧但在内，0.30×size 的下行启发式所报 −1.0px 为假阳性（与 fanout-en2 记录一致）。
- **O3** 孤行填空线 ×7（核心级同位、第一轮已有、非返修回归）：全版扫查发现 7 处填空线 `___` 独占一行——P2 Q16（y=2164.5，blank-only）、P2 Q19（y=2529.5，blank-only）、P3 Q37（y=763.5，`___.`）、P3 Q42（y=1575.0，blank-only）、P3 Q44（y=1807.5，`→ ___` 独行）、P3 Q45（y=1940.0，blank-only）、P4 Q62（y=1867.5，`→ ___` 独行）。逐处与 core-en SVG 逐行比对：**7/7 坐标完全相同**（y 值逐项一致），题干英文原文亦同——根在 core-en，属第一轮即有的排版形态，非本轮返修回归。7 处填空线本身渲染完整、无裁切、无横向溢出（皆位于栏左缘、短行），练习仍可正常作答。处理：记为观察项，不列缺陷、不修版——与本周期 core-fr WEEKLY-KIT.md:123 对同类 O5 孤行填空线（Q130、P3 Q36/Q37）的定性一致（观察项、非缺陷、核心不动、无零风险修法）；任何修法都须改 core-en 共享题干并重排全部 12 个读者语版，核心已定稿，不动。供下一轮 proof2 / 核心层复核。
  - 与 O3 区分：孤儿标点全版扫为 **0 真孤儿**（8 处纯标点节点皆为同基线折分 artifact，见 GATE-LOG）；O3 的 7 处是填空线、不是标点，不计入该门。
- **O4** P7 “VOL.3 promised real letters from VOL.4”：W46 实际措辞为条件式（“And your real letters, if they arrive”），W47 此句将其表述为承诺，略有夸大；实质处理诚实无误（无来信、承诺保留、真信自 VOL.5 起刊登），且与 W46 P7 编辑示例一致。沿用 ko1 O3，不列缺陷。
- **O5** P5 配图说明 “Children from Lawrence, Massachusetts, marching in New York on February 19, 1912”：照片本身为真（Bain News Service，经美国国会图书馆，1912 年 Bread and Roses 罢工期间劳伦斯儿童赴纽约）；具体日期 2 月 19 日未能从所查公开来源中确认（首批 119 名儿童 2 月 10 日抵纽约、另有一批 92 名儿童在第五大道游行，日期未核定）。无反证，不列为缺陷，请协调员复核该日期。沿用 ko1 O6。
- **O6** D5 字体：全版未发现字体问题——韩文层在全部 8 页渲染与裁切中字形完整、无缺字（tofu）；弯引号成对（“ 81 / ” 81）、英文撇号 ASCII 40 个、P3 框题撇号 ASCII U+0027；freeze 新增 CJK 入账干净（2323 = Hangul 2309 + U+3000 9 + CJK 标点 5，新增汉字 0）。只记录，不判。

## 已核实无误（要点）

- 全文 1305 行通读；150 题答案键三源一致（text.md vs registry 仅 Q34 解析器 artifact，原文与键一致；registry vs P8 抽取键 149/150 + #150 截断例外）；5 组配对题释义顺序逐组对 SVG 核对无误；P8 抽取键与 registry 比对仅 #150 可解释差异（见 GATE-LOG）。
- ABSTRACT 已改写为全文形式（624 字节、一行韩文、无 ASCII 双引号，与 fanout-en2 `abstracts/ko.txt` 字节一致）：中期选举发表结果、认证期、反欺凌周/짝짝이 양말의 날、世界儿童日+饥饿游戏、英超回归+ATP 决赛+Ashes 4–1 回顾、读者语韩语、A2–B2、150 题齐全。
- 外部事实逐项核实属实（除 Ashes 回顾见上，另据 ko1 已核实且本轮未改动的各节）：中期选举（美联社 11 月 8 日数据：众院 254–162、19 未定；参院 20–13、AK/MS 未定；7 席翻转全归民主党；5 州长翻转；选前 218–214 / 53–47；第 120 届国会 2027-01-03 就职）、I'm a Celebrity 2026（11 月 16 日周一晚 9 点 ITV1，Ant & Dec，Murwillumbah，Unpacked 在 ITV2，因 11 月 15 日英格兰对西班牙欧国联比赛推迟一天）、ATP 总决赛 2026（11 月 15–22 日都灵，八人名单；Sinner 为 2024+2025 两届冠军、膝伤缺席）、英超 11 月 21–22 日赛程、NFL 第 11 周（小马–德州人 11 月 19 日周四休斯顿；维京人–49 人 11 月 22 日周日墨西哥城晚 8:20 ET；爱国者该周轮空）、反欺凌周（11 月 16–20 日，主题 “Break the Silence”，Odd Socks Day 十周年，200 多名儿童参与选定主题）、《饥饿游戏：日出时分收割》（11 月 20 日周五上映，Zada / McKenna Grace / Ralph Fiennes / Francis Lawrence，改编自 Collins 2025 年小说，第 50 届、选手翻倍；原声专辑 11 月 13 日发行）、Mike Johnson（11 月 4 日宣布不竞选新一届众议院共和党领袖；领袖选举 11 月 10 日）、密西西比常规大选无决选。
- 全部日期/星期均用 `date` 核验通过；P7 金句 8 条与原文页面逐字一致（8/8）；P6 图表数字内部一致（254/162/19；20/13/2；翻转 7；州长 5；254+162+19=435）；P8 完形叙事星期一致；MODEL 范文 84 词（80–100 内）。
- 图片与出处：国会大厦（Noclip，PD，Wikimedia Commons）、火鸡（Audubon）、Rousseau《Surprised!》1891、W. G. Grace（Herbert Rose Barraud，1880 年代末，PD）、劳伦斯儿童（Bain News Service，经 LoC，PD）、投票亭（Kenneth C. Zirkel，CC0）、Samuel Johnson 肖像（Reynolds 1772，PD）、国会图书馆主阅览室（Carol M. Highsmith，PD）——出处齐全。
- 目视：印版 P1–P8 + 网版 P1/P8 全页干净，无溢出/重叠/压页脚；P7 工具盒墨水全部在盒内（清除量 +48.5px）；P8 答案块字小但完整、未压页脚；网版与印版逐页目视一致。
- KIT（`WEEKLY-KIT.md`，192 行）与新交付一致：三件 SHA/字节与实测相同，§5 记录 re-fanout #2 改动（Q39/Q40、Ashes 回顾、ODD SOCKS 修复、ABSTRACT 全文式）与 HAYMITCH 紧余量（+2.6 advance / +2.5 真墨）。
