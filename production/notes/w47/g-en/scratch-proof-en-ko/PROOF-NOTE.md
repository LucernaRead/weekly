# PROOF-NOTE — W47 en-ko · proof1（独立复校，en re-fanout #2 重建版）

- 版：`production/2026-w47/2026-w47-en-ko/`，刊期 2026-11-16–22，VOL.4
- 结论：**(b) 缺陷清单，不可定稿**——唯一缺陷 D4（核心级·中），P5 B Q73 题干/键不合
- 复校员：独立 proof1（与建版者/fan-out agent 非同一人）；本轮会话 `6494a7de-5444-4e09-a07c-2597f43f0d5b`
- 只复校，未改任何源文件、未重建生产件、未 commit、未 push、未动 `tools/`、未碰 core-en
- 交付：`GATE-LOG.md`（逐门结果 + 完整 SHA）、`render/`（8 页印版 + 网 P1/P8 + P2/P3/P5/P7/P8 放大裁切）
- 并行说明：同一 scratch 目录内另有会话 `248f4608-a118-4c3b-ba55-f36af524d2d8` 的同任务产物，其结论为 (a)；其两份文件已原样保存在 `PROOF-NOTE-concurrent-run-248f4608.md` / `GATE-LOG-concurrent-run-248f4608.md`。本复校全部机械门自跑自验，数值与之逐项一致；分歧仅在 D4——该会话与 ko1 proof1 均未提及 Q73。

## 缺陷清单

### D4（核心级·中）P5 B Q73 “Speak ___” 配错键 “speak”（应为 “up”）

题干（text.md:589、P5 SVG、core-en 源码一致）：

> 73. [A2] 빈칸 채우기 — **Speak ___: tell a teacher.**

答案键（三源一致）：

- `registry.json` n=73：`key: 'speak'`，`note: 'speak up = 목소리를 내다'`
- text.md 答案区：`73. [A2] 문장 완성 — speak (speak up = 목소리를 내다)`
- P8 印版 ANSWERS 块：`73. speak`（`render/print-p8.png` 及 `render/crop-p8-answers.png` 可见；P8 抽取键亦为 `speak`，keycheck 149/150 中 Q73 无差异）

完成句为 **“Speak speak: tell a teacher.”**——不合语法。所教短语动词是 speak up（同页 C 组 75. to speak up、D 组 Q79 “Children are speaking up this week.”、 해설 “to speak up = 목소리를 내다”），合乎题干的键只能是 **“up”**。同组对照：Q70 “Break the ___: speak up about bullying.” → silence（填入即成 “Break the silence”）、Q71 “wear odd ___” → socks、Q72 “Every child has ___” → rights——每题的键都是填入空格的词；Q73 空格在 “Speak” 之后，填入的词只能是 “up”，“speak” 无法填入。

根在 **core-en**（`content56.py:49–50`：`f.ex("A2", "完成句子", "speak", "speak up = 大声说出来", "Speak ___: tell a teacher.", …)`；en-ko `content56.py:49–50` 原样继承）。波及全部 12 个读者语版：已查 10 个 en-* registry（de/es/fr/it/ja/ko/nl/pt/ru/zh-tw）Q73 键均为 `'speak'`，题干均为 “Speak ___: tell a teacher.”（core-en 与 en-ja text.md 同行已核）。修法（仅供协调员/核心层参考）：核心键 `"speak"` → `"up"`，注记 `speak up = …` 不变；本复校不改源文件。

严重度：中——150 题中 1 题，但属 ko1 D2 同类核心级答案键错误（读者按答案键自查会学到错误英文 “Speak speak”）；三源一致地错过，跨源比对无法检出，须以题干/键适配逐题手验才能发现，proof1 与并行版均漏过。

## ko1 三项缺陷的修复复核（全部通过）

- **ko1 D1（Ashes 整版错一年）→ 已修复**：P4 已全文改写为 2025–26 回顾（“Perth, One Year On: How Australia Kept the Ashes”）。首场 2025-11-21 周五珀斯、澳大利亚两天 8 wicket 取胜、系列赛 2025-11-21–2026-01-08、总比分 4–1，Cummins 背伤 / Smith 代任队长 / Boland / Doggett 首秀 / Hazlewood 腿筋伤一律过去时；P1 简讯（“A year ago: Australia beat England 4–1 in the 2025–26 Ashes. (p. 4)”）、P1 搜索榜（“ashes” 已撤下，现为 midterm results / thanksgiving / hunger games / i'm a celebrity / anti-bullying week）、P2 “WHAT IS ON THIS WEEK?”、P5 “THE JUNGLE, TOO”、P7 金句与 “NEXT WEEK”（“England's rematch waits until June 2027”）连锁引用全部改为回顾口径；“Perth is winning” / “Ashes begin” / “second week in Perth” 全版 0 处。外部复核（实时检索，见 GATE-LOG）：Sky Sports 系列赛总结 4–1、珀斯 8 wicket、布里斯班 8 wicket、墨尔本英格兰 4 wicket、悉尼 5 wicket、11 月 21 日–1 月 8 日；cricket.com.au / TNT：珀斯首场 847 球，为 1888 年以来最短 Ashes Test。Q46（首场 2025-11-21 珀斯）A、Q52 hosted、Q55 won、Q125（4–1）A 均与回顾一致。
- **ko1 D2（P3 C Q39/Q40 答案互换）→ 已修复**：四源一致——registry（39 mentor→a，40 arena→d；38 b、41 c）、text.md 答案区（39 a、40 d）、P3 SVG C 配对释义顺序（a = teaches and guides you、b = chosen to take part in the Games、c = lives with you in the jungle camp、d = place where the Games are fought）、P8 抽取键（38–41 = b/a/d/c）。P8 印版 ANSWERS 块亦为 “38. b · 39. a · 40. d · 41. c”。
- **ko1 D3（P5 ODD SOCKS 框题出框约 19.6px）→ 已修复**：标题改为 “ODD SOCKS, IN NUMBERS　숫자로”，源级实测 375.4px、PIL 真墨余量 +29.5px；放大裁切 `render/crop-p5-oddsocks.png` 目视确认标题全在奶油框内，右侧留白清晰。

## 仅作观察（非缺陷）

- **O1** P3 “HAYMITCH'S GAMES　헤이미치의 경기”：SVG 实测 advance 401.9px，框右缘 1862，余量 **+2.6px**；PIL 真墨余量 **+2.5px**（ink_end 1859.5）。入框但极紧（ja 姊妹版同标题 +1.5px 更紧）。放大裁切 `render/crop-p3-haymitch.png` 目视确认：末字 “기” 完整在框内，字形无裁切、真墨未压框边、未碰他元素；与旧版同值 401.9px（修复而非回归）。按 STRADDLE 裁定规则不构成缺陷。注：源级 `boxtitle-ko.py` 对该标题标 OVER（401.9px vs 386.5px 通用预算）是口径 artifact——该框内宽实为 404.5px（左垫 18px、右缘即框缘），以 SVG 实测 + PIL 真墨为准。
- **O2** P2 “AND YOU?” 框末行基线余量 **+5.0px**：框底 1544.9，末行 “요.” 基线 y=1539.85。PIL 真墨实测（anchor="ls"）“요.” 墨水止于基线，真墨余量 +5.05px；canonical creambox 所报 desc-clear −1.0 为 0.30×size 下行启发式假阳性（韩文音节无下行笔画）。放大裁切 `render/crop-p2-andyou.png` 目视确认末行完整在框内，下方仍有奶油边。紧但在内。
- **O3** 独立填空线 19 处（核心级同位、第一轮已有、非返修回归）：全版 `___` 独立文本节点 P2 4 / P3 5 / P4 4 / P5 4 / P8 2，edition 与 core-en SVG 逐页坐标完全一致；填空线本身渲染完整、无裁切、无横向溢出，练习仍可正常作答。记为观察项，不列缺陷、不修版——与 core-fr WEEKLY-KIT.md 对同类孤行填空线的定性一致（观察项、非缺陷、核心不动）；任何修法都须改 core-en 共享题干并重排全部 12 个读者语版，核心已定稿，不动。与之区分：孤儿标点全版扫为 **0 真孤儿**（8 处纯标点节点皆为同基线折分 artifact，见 GATE-LOG）。
- **O4** P7 “VOL.3 promised real letters from VOL.4”：W46 实际措辞为条件式（“And your real letters, if they arrive”），W47 此句将其表述为承诺，略有夸大；实质处理诚实无误（无来信、承诺保留、真信自 VOL.5 起刊登），且与 W46 P7 编辑示例一致。沿用 ko1 O3，不列缺陷。
- **O5** P5 配图说明 “Children from Lawrence, Massachusetts, marching in New York on February 19, 1912”：照片本身为真（Bain News Service，经美国国会图书馆，1912 年 Bread and Roses 罢工期间劳伦斯儿童赴纽约）；具体日期 2 月 19 日未能从所查公开来源中确认（首批 119 名儿童 2 月 10 日抵纽约、另有一批 92 名儿童在第五大道游行，日期未核定）。无反证，不列为缺陷，请协调员复核该日期。沿用 ko1 O6。
- **O6** D5 字体（只记录、不判）：全版未发现字体问题——韩文层在全部 8 页渲染与裁切中字形完整、无缺字（tofu）；P6 练习选票 ☐ 正常渲染；弯引号成对（“ 81 / ” 81）、英文撇号 ASCII 40 个、P3 框题撇号 ASCII U+0027；freeze 新增 CJK 入账干净（2323 = Hangul 2309 + U+3000 9 + CJK 标点 5，新增汉字 0）。只记录，不影响结论。
- **O7** Q108 纠错题最小修正问题：原错句 “The Democrats win the House in 2026.” 的公布正解为 “The Democrats won the House.”（删去了 “in 2026”）。正解本身合语法、合事实，属可接受的改写；最小修正应为 “The Democrats won the House in 2026.”。不列缺陷。
- **O8** P2/P6 佐治亚决选句为条件式教学句（“In Georgia, a Senate race with no majority winner goes to a runoff on December 1”），佐治亚决选法本身正确；本期算术（35 席中 33 席已定、仅 AK/MS 未定）暗含佐治亚已定，存在轻微内部张力。条件式措辞，无直接矛盾。沿用 ko1 O2。
- **O9** 构建栈记录：本版由 tools/venv（Pillow 13.0.0 / FreeType 2.14.3）构建，系统 python3（Pillow 10.2.0）重跑 7/8 DIFF 属栈 artifact（同 TOTAL、同流末值，仅 x 坐标微差）；后续复校须用 venv 重跑。另：freeze.py 文档中 ko 家族系统栈之说适用于 core-ko / ko-* 版，不适用于本版（en-ko 实测 venv 8/8）。
- **O10** `·` 分隔符：U+00B7 见于术语注释行与 P8 答案分隔，继承自核心与 W46 ko 翻译记忆库、全周一致；各栏目标题与页脚用全角空格 U+3000，符合 §1.1。沿用 ko1 O4。

## 已核实无误（要点）

- 全文 1305 行通读；150 题答案键三源一致（text.md vs registry 150/150；registry vs P8 抽取键 149/150 + #150 截断例外）；5 组配对题释义顺序逐组对 SVG 核对无误；P8 抽取键与 registry 比对仅 #150 可解释差异（见 GATE-LOG）。
- ABSTRACT 已改写为全文形式（624 字节、一行韩文、无 ASCII 双引号，与 fanout-en2 `abstracts/ko.txt` 字节一致）：中期选举发表结果、认证期、反欺凌周/짝짝이 양말의 날、世界儿童日+饥饿游戏、英超回归+ATP 决赛+Ashes 4–1 回顾、读者语韩语、A2–B2、150 题齐全。
- 外部事实逐项核实属实（除 Ashes 回顾与 ATP 总决赛见 GATE-LOG 实时检索外，另据 ko1 已核实且本轮未改动的各节）：中期选举（美联社 11 月 8 日数据：众院 254–162、19 未定；参院 20–13、AK/MS 未定；7 席翻转全归民主党；5 州长翻转；选前 218–214 / 53–47；第 120 届国会 2027-01-03 就职）、I'm a Celebrity 2026（11 月 16 日周一晚 9 点 ITV1，Ant & Dec，Murwillumbah，Unpacked 在 ITV2，因 11 月 15 日英格兰对西班牙欧国联比赛推迟一天）、英超 11 月 21–22 日赛程（曼城–富勒姆 12:30、纽卡–阿森纳 17:30；利物浦–曼联 11 月 22 日 16:30）、NFL 第 11 周（小马–德州人 11 月 19 日周四休斯顿；维京人–49 人 11 月 22 日周日墨西哥城晚 8:20 ET；爱国者该周轮空）、反欺凌周（11 月 16–20 日，主题 “Break the Silence”，Odd Socks Day 十周年，200 多名儿童参与选定主题）、《饥饿游戏：日出时分收割》（11 月 20 日周五上映，Zada / McKenna Grace / Ralph Fiennes / Francis Lawrence，改编自 Collins 2025 年小说，第 50 届、选手翻倍；原声专辑 11 月 13 日发行、多方信源确认）、Mike Johnson（11 月 4 日宣布不竞选新一届众议院共和党领袖；领袖选举 11 月 10 日）、密西西比常规大选无决选。
- 全部日期/星期均用 `date` 核验通过（18 个日期，见 GATE-LOG）；P7 金句 8 条与原文页面逐字一致；P6 图表数字内部一致（254/162/19；20/13/2；翻转 7；州长 5；254+162+19=435）；P8 完形叙事星期一致；MODEL 范文 82 词（构建计数），在 80–100 词范围内。
- 图片与出处：国会大厦（Noclip，PD，Wikimedia Commons）、火鸡（Audubon）、Rousseau《Surprised!》1891、W. G. Grace（Herbert Rose Barraud，1880 年代末，PD）、劳伦斯儿童（Bain News Service，经 LoC，PD）、投票亭（Kenneth C. Zirkel，CC0）、Samuel Johnson 肖像（Reynolds 1772，PD）、国会图书馆主阅览室（Carol M. Highsmith，PD）——出处齐全。
- 目视：印版 P1–P8 + 网版 P1/P8 全页干净，无溢出/重叠/压页脚（除 D4 文字缺陷外）；P7 工具盒墨水全部在盒内（清除量 +48.5px）；P8 答案块字小但完整、未压页脚；网版与印版逐页目视一致。
