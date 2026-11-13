# PROOF-NOTE — 2026-W47 en-ja · proof1（独立复校）

- **版**：2026-W47，英语目标语 × 日语读者版（en-ja），VOL.4，刊期 2026-11-16..22
- **复校员**：独立复校（与建版者不是同一人），SOP §8.4 proof1
- **复校日期**：2026-11-11
- **对象目录**：`production/2026-w47/2026-w47-en-ja/`
- **结论：(b) 缺陷清单** —— 共 6 项缺陷，含 1 项 MAJOR（答案键错误）。**不可直接定稿**，须修后复验。

## 对象核对（SHA 全量匹配）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-ja.pdf`（印刷） | 41,509,526 B | `5cfb282caa800c343435639ee1b54a325f7d902e4fa6a3c53f2bc4e1374aa63c` |
| `The-Lucerna-VOL4-en-ja.web.pdf`（网页） | 2,843,624 B | `f20c1affd5a53ab23dd8619715dfa86f72c3c6322c0faf5f8daf4c0b4cc7eabb` |
| `2026-w47-en-ja.text.md` | 52,982 B | `1fcc919c1d72958cba7d8039a031eab12444aa066ad5a947f50e637061151f79` |

三者均与 KIT §7 / 任务简报一致。两 PDF 各 8 页，页尺寸 1462.5 × 2025 pts。

## 缺陷清单

### D1 — MAJOR（答案键错误，核心级候选）
**位置**：P3 匹配题 Q39 / Q40；答案刊于 P8 解答区与 `registry.json`。
**事实**：P3 印刷 SVG 的 defs 为 a. "a person who teaches and guides you"（= mentor），b. "a person chosen to take part in the Games"（= tribute），c. "a person who lives with you in the jungle camp"（= campmate），d. "the place where the Games are fought"（= arena）。
正确键应为 38 tribute = **b** ✓，39 mentor = **a**，40 arena = **d**，41 campmate = **c** ✓。
而 registry（en-ja 与 core-en 两版）及印刷 P8 答案均写 **39 = d，40 = a** —— 两键互换。印刷与网页文字层均已确认（print.txt 第 872 行："38. b · 39. d · 40. a · 41. c"），P8 卡片目视亦确认。
**根源**：在 core-en 的 registry → **核心级候选，报协调员，绝不碰核心**。其余 4 组匹配题已逐组对印刷字母核对无误：P2 Q24–27、P4 Q56–59、P5 Q74–77、P8 Q141–144。
**修法**：将 registry 与 P8 答案中 39 改为 a、40 改为 d（核心与本版同步修正；须确认其余 11 个 en-* 版是否同源同错）。

### D2 — MINOR（核心级候选）：P2 DID YOU KNOW 盒末行溢出盒底
**位置**：P2 右栏 DID YOU KNOW 奶油盒。盒底 y=1158.4；末行内文基线 1140.5（"…one of them was on the ballot"），下一行 "November 3." 基线 1171.1，**超出盒底 12.7 px**，落在白底上。P2 卡片裁切目视确认：句尾 "…was on the ballot on / November 3." 被奶油边切断。core-en 几何完全相同（同盒、同 −12.7）→ 核心级候选。文字完整可读，属外观缺陷。

### D3 — MINOR（核心级候选）：P1 SEARCHES 注脚溢出盒底
**位置**：P1 右栏 SEARCHES 盒。盒底 y=1256.0；日语注 "人気の目安で、正確な検索数ではありません。" 基线 1274.0，**超出盒底 18.0 px**，落在白底上。core-en 相同 → 核心级候选。视觉上读作盒下脚注（完整句，非句中断裂），严重度低于 D2。

### D4 — MINOR（本版特有）：ABSTRACT.txt 违反 SOP §9 内容规则
**位置**：`ABSTRACT.txt`（193 B，一行日语）。
现文："英語週刊、日本語解説版。アメリカ中間選挙、ジャングル番組の復活、パースのアッシュズ、新作ハンガー・ゲーム——練習問題と解答つき。"
SOP §9 要求 abstract 包含刊名（Lucerna）、目标语名、A2–B2 级别与题数；本版**四项皆无**："Lucerna"、"A2–B2"、"150" 均未出现。兄弟版 en-de、en-fr 及 core-en 均为完整 abstract。en-ko 同样偏短（同类缺陷，不属本版评判范围）。

### D5 — MINOR（本版特有）：P3 盒标题溢出奶油盒
**位置**：P3 右栏盒标题 "HAYMITCH'S GAMES　ヘイミッチの大会"（sz 23）。以建版者自有 `svglib.text_w` 实测宽 431.4 px，右缘 1888.9 vs 盒右缘 1862.0，**超出 26.9 px**；裁切目视确认末字贴近/越过奶油边。core-en 对应标题 "HAYMITCH'S GAMES　海米奇的比赛" 宽 385.4，右缘 1842.9（−19.1，合规）——故为本版特有（日语 gloss 比中文 gloss 宽）。KIT §4 "all short forms, no collision" 之说对此标题不成立。occlusion 审计对此盲（仅报越 1950 页缘者）——这正是 boxtitle 门存在的原因。其余 39 个同类标题全部通过。

### D6 — MINOR（本版特有）：P5 D 节说明跨栏断裂
**位置**：P5。栏 2 底部：节头 "D　PRESENT CONTINUOUS"（y=2497）+ 说明第 1 行 "現在進行形で書きかえよう（今起きているこ"（y=2544）；尾部 **"と）。"** 被孤立在栏 3 顶部（x=989，y=220），位于 Q78 上方。P5 卡片目视确认。core-en 无此现象（其 D 节头在 y=2438，无断裂；中文说明一行放得下）。成因：日语说明较长折两行，第二行流入下一栏。内容与答案完整，属版式缺陷。

## 已核实无缺陷的项目

- **150 题答案键**：text.md 答案 1–150 与 registry.json 逐项一致（键、级别、题型；编号连续 1..150；每页 10/17/18/18/18/18/12/39；级别 A2 62 / B1 66 / B2 22）；每键再对题干做语义核对，**除 D1 外全部正确**。
- **外部事实**：全部逐项核实，见下节。无捏造。
- **弯引号**：text.md " 81 / ” 81，成对，0 处贴 CJK；8 页 SVG " 82 / ” 82，成对，0 处贴 CJK（多出的一对是 Rousseau 图注 "Surprised!"，SVG 有、text.md 无——见观察项）。无 ‘/’。全宽冒号（：）仅见于日语正文标点，正常。
- **禁词 / 残留简体中文**：中期选举/众议院/民主党赢下/参议院/星期五/金句/范文/桥接/占位/TODO/FIXME/Lorem 在 text.md 中 0 命中。
- **印/网文字层**：内容同一（词多重集相同；5 字符差异纯为空白排版差）。
- **家具**：masthead "The Lucerna"、"英語週刊 VOL.4"、"WEEK OF NOVEMBER 16 TO 22, 2026"、8 页页脚 "The Lucerna　英語週刊 VOL.4　本文は英語　解説は日本語" + "{n} ページ（全8 ページ）"、徽章 "英語テキスト　日本語の解説 — 日本語読者のための版" 全部齐全一致。Readers' Corner 正确说明无来信、示例信标为编辑所写，无虚构读者来信。
- **金句（P7）**：8 条引文逐字对源页核对（P2、P1、P4、P6、P6、P3、P5、P1），页码标注全部正确。
- **MODEL 散文**：86 词，在 80–100 要求内。P8 最小字号 SVG 13.5 pt；PDF 最小 span 10.12 pt（≥ 9.75 下限）。
- **星期**：经 `date -d` 核对，Nov 3 2026 周二、Nov 8 周日、Nov 9 周一、Nov 10 周二、Nov 15 周日、Nov 16 周一、Nov 18 周三、Nov 19 周四、Nov 20 周五、Nov 21 周六、Nov 22 周日、Nov 26 周四（感恩节 = 11 月第 4 个周四 ✓）、Nov 27 周五、Dec 1 周二 —— 与印刷一致。
- **P7 工具盒**：creambox 实测盒底 y=1008.2，末行基线 y=960，**清除量 +48.2**，三行全部在盒内，目视确认干净。
- **其余 39 个栏 3 盒标题**：宽度全部通过（仅 D5 一项失败）。

## 外部事实核实结果（2026-11-11 联网检索）

- **美国中期选举（头条）——核实**：民主党赢下两院。报纸数字（AP 11 月 8 日周日 call）：众院 D 254 / R 162 / 19 未定；参院 33 席中 D 20、R 13、2 未定（阿拉斯加、密西西比）；7 席参院翻转 **Iowa, Kansas, Maine, North Carolina, Ohio, South Carolina, Texas**；5 州州长翻转 **Georgia, Iowa, Nevada, Ohio, Texas**；选前众院 R 218–214、参院 R 53–47；议长 Mike Johnson 不再竞选众院共和党领袖；众院共和党 11 月 10 日投票、众院民主党 11 月 18–19 日投票；36 场州长选举。以上与多源一致。**注意快照差异**：另一来源（political.org，同样标注 "as of Nov. 8, 2026"）给出 252–161、22 未定；Ballotpedia（11 月 6 日）称 "at least 250–157"。报纸的 254–162 与 11 月 7–8 日 AP 计数（多源引述，含 AP 11 月 8 日晚 9 点 ET 计数）一致，且报纸已正确加护栏（"numbers can still move a little"、"will not guess the final numbers"、"the calls of Sunday, November 8"）。非捏造，记为快照口径差异。
- **佐治亚决选 / 密西西比 / 认证窗口——核实**：佐治亚无人过半则 12 月 1 日决选（Ossoff 已首轮胜出，故本次无需决选；报纸作条件句表述 ✓）；密西西比无决选、得票最多者胜 ✓；各州认证窗口 11 月 10 日至 12 月 18 日 ✓（Ballotpedia 日历）。
- **饥饿游戏：日出时分收割——核实**：11 月 20 日（周五）上映；小说 Suzanne Collins 2025 年 3 月 18 日出版；Joseph Zada 饰少年 Haymitch（16 岁，12 区）；McKenna Grace 饰 Maysilee Donner；Ralph Fiennes 饰少年 Snow 总统；Francis Lawrence 导演；第 50 届、第二次四分之一大赛、贡品双倍；Woody Harrelson 在旧作中饰 Haymitch。原声专辑 11 月 13 日发行，29 首 ✓。
- **I'm a Celebrity——核实**：11 月 16 日周一晚 9 点回归，ITV1/ITVX；Ant & Dec 主持；因英格兰对西班牙欧国联比赛在 11 月 15 日周日，首播比惯例晚一天；"How to Survive the Jungle" 一次性特辑 11 月 15 日周日 18:00 ✓；营地在 Murwillumbah, NSW ✓；Unpacked 由 Sam Thompson 与 Kemi Rodgers 主持（ITV2）✓；参赛名单 ITV 尚未正式确认（报纸表述与此一致）。
- **灰烬杯——核实**：首场 11 月 21 日周六，珀斯 Optus Stadium；Cummins 背伤缺阵、Hazlewood 腿筋伤缺阵；Steve Smith 任队长；Scott Boland 顶替 Cummins；Brendan Doggett 有望首秀；Ben Stokes 任英格兰队长。英格兰上次在澳赢系列赛 **2010–11**；最近两次客场之旅 **2017–18 与 2021–22 均 0–4 落败**；2023 年英格兰主场 **2–2 平**。澳大利亚 2024 年 11 月在该场地首场测试赛负于印度 **295 分** ✓；珀斯体育场此前从未主办灰烬杯测试赛（此前珀斯灰烬杯均在 WACA）。首球 10:20 当地时间 = 伦敦 2:20（珀斯 UTC+8、伦敦 11 月为 GMT，算术 ✓）。
- **反欺凌周——核实**：11 月 16–20 日周一至周五；主题 **"Break the Silence"**；Anti-Bullying Alliance 主办；Odd Socks Day 11 月 16 日周一，**十周年**（始于 2017）；主题由 200 多名儿童参与选定；去年逾 800 万儿童参与。
- **世界儿童日——核实**：11 月 20 日周五；主题 **"My day. My rights. My future."**（UNICEF）；UNICEF 牵头；该日纪念 1989 年 11 月 20 日联合国通过《儿童权利公约》。
- **ATP 总决赛——核实**：都灵 11 月 15–22 日；阵容恰为 **Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe, Rafael Jodar**；**Sinner 膝伤缺阵**（两届卫冕冠军）；两组各四人。
- **英超——核实**：11 月 21 日周六 Man City–Fulham 12:30、Newcastle–Arsenal 17:30；11 月 22 日周日 Liverpool–Man Utd 16:30；为国际比赛日后首轮。
- **NFL 第 11 周——核实**：11 月 19 日周四 Colts at Texans 晚 8:15 ET；11 月 22 日周日 Vikings at 49ers 于墨西哥城晚 8:20 ET（NBC）；Patriots 第 11 周轮空（此前 11 月 15 日周日在慕尼黑对 Lions）✓。
- **未独立确认的微观说法（未发现矛盾，记为未证实）**："Day one is already sold out"（P4，灰烬杯首日售罄）；"more than 80% of schools"（P5，反欺凌周参与学校比例）。

## 观察项（非本版缺陷）

- **P4 "B SENTENCES" 节头孤悬**：节头在栏 2 底部（y=2437），题目 Q52–55 在栏 3 顶部——别扭，但 core-en 结构相同（节头 y=2407），属继承的核心版式特征。
- **creambox 负值多为误报**：脚本 +45 px 窗口会抓到盒下下一块的标题（如 −37.0 的 "TRY IT NOW"、"WHAT IS ON THIS WEEK?"、"READERS' CORNER"）；core-en 在同一盒子上出现**相同**负值，证实为下标题伪影而非溢出。真正溢出仅 D2/D3（盒自身内容越过盒底）。
- **text.md 缺 7 处图注**（Capitol、Audubon 火鸡、Rousseau "Surprised!"、W. G. Grace、Lawrence 姐弟、投票亭、Samuel Johnson）——core-en 的 text.md 同样缺这 7 处，属导出器的既定行为，非本版缺陷。
- **KIT 时效（非版面缺陷）**：KIT §3 称 freeze 新增 CJK = 2,096；本次重跑为 **2,092**，差值恰为 P4 gloss 修正删去的 4 个全宽冒号（"a Test：…" → "a Test = …"）；KIT 数字早于该修正。P4 SVG 现为 0× U+FF1A，修正已验证。
- **p8.py FOOTER_RE 工具 bug（KIT §10，已知）**：混合大小写页脚会漏进抽出的第 150 键。keycheck 可见（抽出的 Q150 含 "… (要点ごとに採点) The Lucerna·英語週刊 VOL.4·…8 ページ"）。工具问题，非版面缺陷。
- **D4 同类**：en-ko 的 abstract 同样偏短，同类缺陷，不属本版评判。

## 复校方法

全文通读 text.md（1,306 行）；150 题逐题核对答案键并对题干做语义核对；8 页印刷卡片全部目视 + 网页 PDF P1/P8 渲染目视；机械门全跑（见 GATE-LOG.md）；外部事实逐项联网检索；核心对照 core-en（freeze 8/8 字节一致、p8 抽取集相同、creambox 对照相同）。
**未做**：未改任何源文件、未重建、未 commit、未 push、未动 tools/。缺陷根在核心者记为核心级候选报协调员。
