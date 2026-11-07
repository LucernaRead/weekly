# W45 EN × ZH-TW 独立校对报告

- 校对对象：`files/weekly-report-w45-en-zh-tw/`（SVG ×8、卡片 ×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 构建树（只读审阅，未改动）：`hidden_files/weekly-report-w45-en-zh-tw-build/`
- 核心对照：`files/weekly-report-w45-en-core/`（EN VOL.2，150 题）
- W43 同配对对照：`files/weekly-report-en-zh-tw/`（只读）
- 校对员立场：只校对，不改源码、不宣布上架、不派生下级代理；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录、未改共享工具 `tools/p8.py`。
- 本报告证据同目录；上架由主线串行执行，本报告不是上架宣告。

## 结论：ZERO PROBLEMS

纸面（8 页 SVG + 8 卡 + 双 PDF）经全部 11 项独立重测，无阻塞项。下列“非阻塞观察”只涉及 KIT 记录数字与措辞、以及过程记录缺口，不触及纸面正确性，不阻挡本版。

## 开工前查重

- `ps` 检查：无任何进程在写 `files/weekly-report-w45-en-zh-tw/` 或 `hidden_files/weekly-report-w45-en-zh-tw-build/`。唯一在跑的同类进程是 `weekly-report-w45-ja-en-build/audit_round4.py`（另一分版），经 cwd/命令行确认不属于本版，不 stand down。
- 交付物最新 mtime 2026-10-28 01:10 UTC（WEEKLY-KIT.md），开工时（01:14 UTC）已静默逾 3 分钟，满足 60–120 秒静默复查，安全开工。
- 校对前后杂凑：`hashes-before.txt` vs `hashes-after.txt` 的 `diff` 为空——本版与核心在校对全程零变动。

## §1 冻结与英文正文

- **基线复现 8/8**：`tools/freeze.py baseline` 原样调用对建造员留下的 build-copy 不生效——该 copy 的 OUT 已被重定向到 `tools/scratch/baseline-w45-en-zh-tw/svg`，freeze 只重定向 `files/` 路径，故原样运行 0/8 且把输出误写回建造员旧 scratch 目录（复核：该目录复写后杂凑仍与核心 8/8 全等，无损害；核心守卫显示核心未动）。校对员改用等价显式重定向重跑：复制 pristine 核心 build（`bridge` 定义、`SC` 面齐备）→ OUT 改道本证明目录 → 单进程 import content12/34/56/7/8 → **8/8 逐字节复现**（p1 c7e7d019…、p2 07f5df7e…、p3 d9f7cc37…、p4 3b8be517…、p5 73486e2f…、p6 3e2187b3…、p7 5a268409…、p8 4de34a13…，与核心出货杂凑全等）。证据：`baseline-my/svg/`、`baseline-my-hashes.txt`。
- **freeze diff**：P1–P7 互异串数相等（P1 24/24、P2 20/20、P3 14/14、P4 14/14、P5 14/14、P6 13/13、P7 27/27）；P8 +78/−82 仅为答案块折行重排（条目级由 p8.py 证明全等，见 §4）。P7 多重集口径 +30/−32（净 −2 节点）= 3 处孤行“。”消除（2 处 FIX1 + 1 处披露重写换行，见 §6），互异串口径相等。
- **英文正文无丢失**：被删串逐项裁定（完整清单见 `freeze-removed-my.txt`）——P2–P7 被删串含 CJK 者外，纯英文被删串为 0；P1 唯一纯英文被删串是核心英文副标 `THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA`，按 W43 家具替换为繁体徽章（见 §10）；P8 的 8 条纯英文被删片段皆为同一英文答案行的折行切分差异，内容经 p8.py 与登记表逐项证明无丢失。
- **新增 CJK 逐页计数**（多重集，freeze 口径含全角标点）：P1 104、P2 80、P3 44、P4 57、P5 56、P6 50、P7 140、P8 229，合计 **760**；严格 CJK 口径（仅 U+2E80–U+9FFF）为 759，差 1 来自 P7 披露重写多出的 1 个全角逗号，。KIT §6 的 762 与终态实测不符（见非阻塞观察 O1）。
- **违禁词**：`桥接` 在 8 页 SVG 与 ABSTRACT.txt 中 = **0**；KIT 中 `桥接` = 0，仅 1 处英文 `bridge→expl` 更名说明（KIT §1.3 行），属 KIT-only 文本类，纸面为 0。

## §2 繁体独立性（最重要）

方法（不采信建造员的 209 字表）：参照集 R = W43 EN×ZH-TW 全部 SVG 的 CJK 字符集（496 字）∪ W45 繁中核心 `weekly-report-w45-zhtw-core` 全部 SVG 的 CJK 字符集（773 字），并集 913 字。本版 CJK 444 字（1864 token）；界外字 = 本版 − R，逐字按语境裁定；另加建造员 7 命中复核、大陆词汇扫描、里/裡与導/道专项。

- **界外字实测 55 个（非建造员所称 54 个）**：久亥伍伯俄制博哥塊士夠如孩宣密尋尼尾崎帽怪慕承拉擇擬映書某烏無然爾獅相睡破織耐薩蘇該諾豚足逐邁郵里銜靈願顯馬黑。逐字语境裁定**全部合法**：慕尼黑（慕尼黑）、退伍軍人（伍）、伯納烏（伯烏）、俄亥俄（俄亥）、制度（制）、博士（博士）、哥斯拉（哥拉）、第二塊螢幕（塊）、就夠（夠）、一如既往（**如**）、孩子問為什麼這麼久（孩、**久**）、宣布（宣）、搜尋（尋）、慕尼黑賽（尼）、收尾（尾）、山崎貴（崎）、貓的帽子（帽）、怪物（怪）、承諾（承諾）、選擇（擇）、模擬選票（擬）、上映（映）、博士的書／教書（書）、某場（某）、伯納烏（烏）、無法（無）、仍然（然）、比爾·哈德（爾）、雄獅（獅）、相對（相）、多睡（睡）、破折號（破）、組織（織）、耐心（耐）、披薩（薩）、蘇斯（蘇）、該州（該）、承諾（諾）、海豚（豚）、足球／補足語（足）、逐州（逐）、邁阿密（邁）、郵寄（郵）、馬德里（**里**，专名用字）、頭銜（銜）、阿靈頓（靈）、意願（願）、顯示（顯）、馬德里（馬）、慕尼黑（黑）。其中久為兩岸同形字，是建造员 54 字清单漏计的 1 字（见 O2）；其余皆为正确繁体字形，无一简体形。
- **完整性证明**：本版全部 444 个 CJK 字中，每字或在 R 内（有已发繁体版佐证），或在上述 55 字 adjudicated 清单内——无第 3 类字符。**简体残留 = 0**（本结论立足本节完整交叉核验，不立足建造员字表）。
- **建造员 7 命中复核**（逐字语境，3 处与建造员说法有出入，皆不构成残留）：
  - 第（30 处，皆“第 N 版”）、不（9 处）、如（1 处“一如既往”）：两岸同形，成立。
  - 里（3 处）：皆“馬德里”，专名用字正确；裡另有 1 处“夜裡”，裡／里分工正确。
  - **道（1 处）：建造员称“道＝報導”不成立**——本版“道”仅见于“一道小題”（量词，两岸同形）；“報導”实际用字是 **導**（U+5C0E，3 处：報導、導演、引導），皆为正确繁体形，简体“导”= 0。建造员混淆了道／導二字，但纸面无误。
  - 黑（1 处“慕尼黑”）：成立。
  - **斯（2 处）：建造员称“斯＝蘇斯博士”不完整**——除蘇斯博士外，另 1 处为“哥斯拉”（斯拉），同为音译同形字，无残留。
- **大陆词汇 = 0**：得州／视频／在线／信息流／精彩／里面／发展／屏幕／搜索／报道／计划／软件／网络／质量／信息／视频／连休／于（单字亦 0）等全册检索皆 0；台湾／香港用语在版：印地安泉、比爾·哈德、比數、螢幕、搜尋量、報導、計畫、第二螢幕是手機、披薩、貼紙、撥回、週。
- **引号**：全册「」= 2 对，**皆在 P8**（82. `38% 選「不用排隊」`、136. `whether 引導「是否」從句`）；大陆式 “” = 0；版面文本节点 ASCII 双引号 = 0；法式 « » 93 对与核心全等（冻结正文，不动）。
- **TC 字体**：建造目录 svglib 仅做面切换（`_sc_index`→`_tc_index`，`SC`→`TC` 面名，默认族名 `Noto Serif/Sans CJK TC`），与 W43 同配对版同形；PIL 实测 4 个 TTC 的面索引皆为 **3**（JP=0/KR=1/SC=2/TC=3/HK=4），与 tables.json 一致；出货 SVG 的 font-family 皆为 `Noto Serif/Sans CJK TC`（另 1 处黑体字 masthead）。

## §3 P7

- **英文定义句与金句原文逐字保留**：P7 纯非 CJK 文本多重集核心 = 本版（差集为空）；**定义句本地化 = 0 处**；8 句金句在 P7 原文逐字在版。
- **金句级别（校对员自核心源 content7.py phrases 表实测，非建造员清单）**：[A2, A2, B1, B1, B2, B2, A2, B1]，本版源同序同级。金句 8 句：Tuesday, November 3, is Election Day…／The hour from 1 to 2 happened twice.／Which film would you choose ?／Two games, two continents, one league — that is the modern NFL.／The results will still be there in the morning.／Patience is part of the system, not a failure of it.／Not every place changes.／One Sunday is not enough — good thing the week has seven days.
- **全册句频（校对员自出货 SVG 实测）**：3／2／2／2／2／4／3／2（P7 句＋原文出处＋翻译题干；第 1、6、7 句另见 P8 翻译题），与建造员声称一致。
- **全册句频核心 = 本版**：金句出现位置与核心一致（P7 句＋各原文出处页＋P8 翻译题），无新增、无丢失。

## §4 P8（显式双路径，--total 150）

- **78 项口径独立确立**：`p8.py extract --total 150` 对出货核心 P8 导出 noted 集 = **78**：{11, 12, 14, 19, 29, 30, 31, 33, 41, 44, 47, 48, 51, 58, 64, 66, 67, 68, 69, 71, 74, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 100, 102, 107, 108, 109, 110, 111} ∪ {112–150}，与本版 content8.py 的显式 `PRINT_NOTES` 集逐号全等。
- **compare（显式双路径 `--core-p8`／`--edition-p8`，`--total 150`）**：**CLEAN**，核心 78 noted = 本版 78 noted，missing=[]、extra=0、uncertain=[]、keydiff=[137, 138, 139, 140, 150]。
- **total 陷阱实测**：`--core-dir` 形式不带 `--total` 时默认取 tables.json 的 W43 英语题量 149（`exercises_w43=149`），此时门测得 77 noted、keydiff=[137, 138, 139, 140, 149]——第 150 项被排除在口径外、149 被误标为键差，属错误口径；只有 `--total 150` 的 CLEAN 有效。`--target zh-tw` 的 core-dir 形式会误取 `p8-test.svg` 而报错，正确目标码为 en（此为调用形式问题，不影响显式双路径结论）。
- **keydiff 逐项印刷行对照**（出货 SVG 答案区节点直连，非法空格为折行换行 artifact，见注）：
  - 137：核心 `耐心是制度的一部分，而不是制度的失败。（part of 一部分；not a failure 不是失败）` → 本版 `耐心是制度的一部分，而不是制度的失敗。(part of 一部分；not a failure 不是失敗）`——合法：失败→失敗繁体化；外括号半角化（EN 族 W45 式）。
  - 138：核心 `11 月 3 日周二是美国的选举日。（Election Day 选举日；on Tuesday）` → 本版 `11 月 3 日週二是美國的選舉日。 (Election Day 選舉日；on Tuesday)`——合法：周二→週二、美国→美國、选举→選舉。
  - 139：核心 `这周日，NFL 在马德里比赛。（on Sunday；in Madrid）` → 本版 `這週日，NFL 在馬德里比賽。 (on Sunday；in Madrid)`——合法：这→這、马德里→馬德里。本版渲染 `· 139.這週日`（点后空格缺失）即 p8.py 放宽所针对的情形，渲染本身正确（中文排版无需该空格）。
  - 140：核心 `并非每处都拨回时钟。（not every 并非每处；change 变化）` → 本版 `並非每處都撥回時鐘。 (not every 並非每處；change 變化)`——合法：并→並、每处→每處、拨→撥、时钟→時鐘。
  - 150：核心 `开放题 — 要点见写作框，范文在第 8 版写作框内（按要点给分）` → 本版 `開放題 — 要點見寫作框，範文在第 8 版寫作框內 (按要點給分)`——合法：装置键繁体化。
  - 其余 145 条键与核心逐字节相同（登记表双 dump，见 §11）。
  - 注：核心印刷行 `11 月 3日周二`、`inMadrid`、`第8 版` 与本版 `139.這週日`、`140.並非` 的空格有无，皆为 svglib wrap 在行首丢弃空格 token 的渲染 artifact（核心与本版互有丢弃），非内容差异；p8.py 的 norm 化比对已将其归一。
- **翻译题方向（以渲染为准）**：4 道翻译题题面全为英语句子（137 `Translate : « Patience… »`、138 `翻譯：Tuesday, November 3, is Election Day…`、139 `翻譯：On Sunday, the NFL plays in Madrid.`、140 `Translate : « Not every place changes. »`），键全为中文，实际为 **4 道 EN→ZH 题**；核心 KIT 与本版 KIT 的“EN↔ZH 双向”说法与渲染不符，纸面以渲染为准（见 O4）。137、140 的 `Translate :` 为冻结英文不动，138、139 的题干前缀 `翻译：`→`翻譯：`。
- **P8 注释纯繁体**：答案区 78 条半角括号注与 noted 集一一对应；注文字符全部落在 R ∪ 55 字清单内，界外字符 0；全角括号仅 4 处：答案头 `（第 1–8 版）` 1 处 + 3 处注内嵌套限定语（不規則變化／比較級／美式英語），皆为内容括号而非注式违规；与 W43 同配对版括号格局同形（W43：全角 4 处、半角 80 处）。

## §5 共享工具改动专项（tools/p8.py）——验证通过，可信任

建造员改动（2026-10-27）：`split_joined` 分隔符正则 `r"\.\s"` → `r"\.\s?"`（起因：第 139 项 `· 139.這週日` 点后空格缺失致旧工具 `joined-split-fail`）。校对员未再改共享工具。

- **与旧版 diff**：仅正则 1 字符 + 5 行注释，改动范围最小（`scratch/p8-before-fix.py` 对照，证据见本节）。
- **第一性原理验证**：分隔符锚点为前导 `·` + 数字 + 点，空格仅出现在点后；CJK 行首时 wrap 丢空格且 join2 不补空格，故点后空格时有时无；将其置为可选不引入新分隔歧义（键内不存在 `· N.` 形分隔串；搜索起点 pos 逐项推进，不回溯）。放宽不改变 noted 集判定逻辑（missing/extra/uncertain/keydiff 均在切分后条目上运算）。
- **三项回归全部复现**：
  - 核心自比：CLEAN，keydiff=[]。
  - W43 EN×ZH-TW extract（--total 149）：62，与其 KIT §4 的 62 全等。
  - W45 EN×PT compare（--total 150）：CLEAN，keydiff=[137, 138, 139, 140, 150]（与本版同形，合理：同为 4 道翻译＋150 号装置项重定向）。
- **反向对照（放宽未掩盖真实错配）**：
  - 干净项错键：复制本版 P8，将答案区 11. `one` 改为 `two` → keydiff 新增 11（[11, 137, 138, 139, 140, 150]），错键仍被检出。
  - 删注：删除答案区 11. 的注括号 → **SHORT**，missing=[11]，exit 1。
  - 旧工具对本版：`PARSE_FAIL (joined-split-fail)`，证实改动确为必需、非无故放宽。
- **结论**：该改动可信任，不构成阻塞。证据：`p8-reg-core-self.json`、`p8-reg-w43.json`、`p8-reg-enpt.json`、`p8-mut-wrongkey11.svg`、`p8-mut-nonote.svg`、`p8-old.py`（旧版复制件，仅用于对照运行）。

## §6 中途事故专项（构建树误删后重建＋FIX1）

- **重建保真度（校对员独立再生）**：将 `scratch/gen_full.py`＋`pairs.py` 复制到本证明目录、改道 pristine 核心 copy 后重跑，生成 transform.py：229 键、398 处，与 KIT 声称全等；剔除 FIX1 块与 B 路径行后，与现行 `transform.py` **逐字相同**。即现行 transform = gen_full 输出＋FIX1 块，无其他掺入。
- **FIX1 范围确仅 P7**：FIX1 块恰 2 条，皆为 content7 的 P7 语法点注（`happen 的過去式是 happened，規則變化。`→`happen 過去式是 happened，規則變化。`；`part of = ……的一部分；not 表否定對照。`→`part of = ……的一部分；not 表否定。`）；终态出货 SVG 中 FIX1 新串仅见于 P7；其余 7 页与首轮杂凑清单（`scratch/baseline-round1.txt` vs `baseline-round2.txt`）比对：仅 P7 变化（首轮 86a6539d…→终轮 c3a4dbbf…），其余 7 页逐字节同。
- **其余 7 页完整、无核心原文误渲染混入**：渲染后残留检查——229 条 MAP 中全部非全等简体键在本版 SVG 文本中 = 0；P1–P6 被删串皆为讲解层（见 §1）；P8 差异仅为折行＋5 条繁体键。
- **FIX1 语义**：2 处皆为省字换行（去“的”、去“對照”），语法点仍正确；第 2 处“not 表否定”较原文“not 表否定對照”略失“对照” 细微差别，但陈述本身正确，不构成事实错误（见 O3）。
- **过程记录缺口（不掩盖）**：首轮 SVG 本体未留存（仅杂凑清单），pre-FIX1 的 transform.py 未留存——`scratch/transform-backup.py` 与现行 `transform.py` 杂凑全等（4ccc520f…），实为 FIX1 后备份，非事故前备份。终态全部项目均经本报告独立实测，不存在因缺口而放行的未实测项；缺口仅为过程记录缺口。

## §7 几何

- **canonical `tools/occlusion_audit.py`**：自检先行通过（6 类全触发，干净对照静默）；本版 **0 旗**／核心 **0 旗**／**NEW = 0**（`occlusion-my.json`）。
- **同基线 advance 碰撞**：校对员解码后（HTML 实体解码）全册扫描 = **0 旗**。建造员声称的 1 处 P1 目录 p.3 行旗，实为未解码度量 artifact：原始串 `A cat, a monster &amp; screens` 按 5 字符 `&amp;` 量得 advance 框 [1523, 1830.3]，与 `A2→B1` [1800, 1863] 重叠 30px；解码后标题框为 [1523, 1780.8]，与级别框间隙 19.2px；PIL 真墨框标题 [1523, 1781.0]、级别 [1799.0, 1863.0]，墨迹间隙 18px；卡片像素同断面标题墨止于 1777、级别墨起于 1800。核心同行数值全等。故该旗为虚报，且其根因是实体未解码（比“advance 虚报”更精确）。
- **全页右缘 advance 扫描＋框线压框**：advance 旗恰 5 处，与核心逐值全等；框线压框 advance 旗 = 0：
  - P4 图说 `Frank R. Snyder — public domain, via Wikimedia Commons` advance 右 1888.6（核心同值）；卡片墨止 1869（＜1885 内容界），advance 虚报；裁图目视图说完整无截断。
  - P8 `b. an election in the middle of a term` advance 1903.8→PIL 墨 1899、卡片墨 1901；`d. the paper you mark your choice on` advance 1903.8→PIL 墨 1904、卡片墨约 1904（与 1909–1910 框线不相交）；`— Good morning ! Is this the voting place` advance 1890.3→PIL 墨 1890、卡片墨 1885；`Everybody has one on their jacket. — The` advance 1891.3→PIL 墨 1891、卡片墨 1887。
  - 精确裁定：5 旗皆为冻结英文行、核心同款；其中 P4 与 Good morning 在卡片真墨上未逾 1885 内容界（纯 advance 虚报），其余 3 处真墨逾 1885 界 2–19px 但皆未逾 1913 内框、卡面完整可读、无截断。按“核心同款＋框内＋可读则不重报”的既定口径，**皆不列为缺陷**。本报告如实记录：5 旗并非 ≤0.5px 舍入伪影（超量远大于 0.5px），其不列缺陷的理由是核心同款＋框内＋可读，而非“纯 advance 虚报”。
- **P6 图表标签（基线锚定墨迹法，PIL getmetrics 上升／下降，anchor ls）**：全页标签被后续 rect 覆盖的最差值 **0.0%**（门限 ＜30%），核心同值；4 条教学图表标签墨框：`No lines : 38%` [527, 1170.4, 683, 1189.4]、`Work on Tuesday : 29%` [527, 1222, 785, 1247]、`Travel plans : 21%` [527, 1275.6, 729, 1299.6]、`Habit : 12%` [527, 1328.2, 655, 1347.2]，卡面逐个清晰；版面明确标注为教学数据、非真实民调。注：核心源中图表为文本标签行（`bw` 栏宽变量未实际绘条），此为核心固有形态，非本版缺陷。getbbox 法口径未采用（错误口径）。
- **8 张卡片全部目视（无抽查）**：P1–P8 逐页目视——TC 面无缺字／方框；徽章与配对页脚每版在位；P1 热搜条 5 条递减对齐；P6 图表与 38／29／21／12 对应、选票框 ☐ 与 P7 诊所 ✗ 的渲染与核心卡片像素全等（选票框裁图杂凑 ed = core = d30db36e…，属冻结核心渲染，非繁体回归）；P8 答案区右缘墨迹皆在框内；无重叠、无截断、无溢框文字。

## §8 gloss

渲染后 gloss() 串按 · 拆分，核心 = 本版逐项 1:1：P2 3 项（to fall back／a costume／trick or treat）、P3 4 项（to open／a monster／a catchphrase／a series）、P4 4 项（a fixture／a title／to defend／a fan）、P5 3 项（a map／too close to call／a second screen）、P6 4 项（to register／a governor／to shape laws／patience），合计 **18**；英文词头逐项全等，中文讲解皆繁体化。另 P1 讲解框 4 项（a midterm／a ballot／a race／to call a race）核心 = 本版同数同序。

## §9 读者园地

- **英语信件逐字冻结、零编造**：P7 信件 3 节点核心 = 本版逐字节同：`« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)`；信件自带 editor's example 标注，无编造；本版未新写任何核心没有的英语披露句（P7 纯非 CJK 文本多重集核心 = 本版）。
- **繁体披露句逐字摘录**：`編輯說明｜截至發稿，編輯部未收到真實來信，也沒有收到可刊登的 VOL.1 寫作投稿；本期園地所刊為編輯部示例，刊登真實來信的承諾順延至 VOL.3。請把你的來信與寫作寄來，VOL.3 起刊登收到的真實來信。`
  - 事实 1（无真实来信）：`編輯部未收到真實來信` ✓
  - 事实 2（无可刊登 VOL.1 写作投稿）：`也沒有收到可刊登的 VOL.1 寫作投稿` ✓
  - 事实 3（本期为编辑部示例）：`本期園地所刊為編輯部示例` ✓
  - 顺延：`刊登真實來信的承諾順延至 VOL.3` ✓
  - 显性祈使邀请：`請把你的來信與寫作寄來`（祈使句，独立在位）✓
  - VOL.3 刊登承诺：`VOL.3 起刊登收到的真實來信` ✓
  - 内容预告行（NEXT WEEK · VOL.3 下週預告＋英／繁预告句）未计入邀请；邀请句在披露段内独立存在。
- **覆盖范围显式裁定（写作投稿／P8 范文）**：披露句的“寫作投稿”指读者 VOL.1 写作投稿；P8 的 MODEL 范文《My Tuesday, November 3》为编辑部范文，不属读者投稿，不受“未收到可刊登投稿”句影响。邀请覆盖来信与写作二者（`來信與寫作`）；VOL.3 刊登承诺句明文所指为`真實來信`，写作的刊登承诺由同一邀请句承载、且与核心措辞全等，本版未相对核心缩小承诺范围。

## §10 家具／W43

与 W43 EN×ZH-TW 逐字对照（W43 同配对家具胜过 README #20 泛化规则）：

| 件 | W43 | 本版 | 裁定 |
|---|---|---|---|
| P1 徽章（y=372，19.5pt 粗体 BRICK 居中） | `英語正文 · 繁體中文講解 — 給繁體中文讀者的版本`（元素属性 x=975/y=372/19.5/700/#a4553a/middle 全等） | 同文 | 逐字同 |
| 頁腳（8 版全） | `The Lucerna · 英語週報 VOL.1 · 正文英語 · 講解繁體中文` | `The Lucerna · 英語週報 VOL.2 · 正文英語 · 講解繁體中文` | 仅 VOL.1→VOL.2 |
| 頁碼行（8 版全） | `第 N 版 / 共 8 版` | 同形 | 逐字同 |
| gloss 前缀 | `譯注｜` | `譯注｜` | 逐字同 |
| P8 答案头 | `ANSWERS · 全部答案與簡析（第 1–8 版）` | 同文 | 逐字同 |
| P8 分隔 | `— 第 N 版 —`（N=1–8） | 同形 | 逐字同 |
| P8 注式 | 半角括号＋前置空格 ` (注)`（W43 实测：全角 4 处为答案头＋3 处注内嵌套，半角 80 处） | 同式 | 沿用 W43 式，KIT §8 说法成立 |
| 引号裁定 | 「」台式 | 「」2 对皆 P8 | 逐字同（见 §2） |
| 報頭／刊名 | The Lucerna | The Lucerna | 同 |

W43 偏差清单（相对 W43）：VOL.1→VOL.2；P8 印刷集 62→78（核心集本身变化，显式集强制）；披露按 W45 协调员裁定重写（3 事实＋显性邀请）；新增主题词皆为 W45 核心事实。

## §11 题量／范文／ABSTRACT／图片

- **题量**：校对员独立再生登记表（核心 build-copy 重跑＋本版 build copy 改道重跑）：总数 **150**；级别 A2 60／B1 69／B2 21；页分布 P1 10／P2 17／P3 18／P4 18／P5 18／P6 18／P7 12／P8 39；n／page／level 逐项与核心全等（0 错位）；题型计数 1:1 对译：單選 41／完成句子 33／詞彙配對 20（5 组）／句型轉換 16／完形填空 8／跟練 8／圖表讀數 6／對話補全 5／改錯 4／閱讀理解 4／翻譯 4／寫作 1（合计 150）。
- **范文**：P8 MODEL《My Tuesday, November 3》节点 160–165 核心 = 本版逐字节同；空白切分 **85 词**，去标点实词 81，与核心同一字串。
- **ABSTRACT**：繁体单行（1 行，尾换行符除外）、无 ASCII 双引号；含刊名 The Lucerna、英語週報 VOL.2、正文英語、講解繁體中文、A2–B2 分级、150 道練習；真实主题关键词：美國中期選舉投票日 11 月 3 日星期二、11 月 1 日時鐘撥回、11 月 6 日星期五電影《貓帽子》與《哥斯拉-1.0》、11 月 8 日星期日 NFL 馬德里賽與聖保羅 F1；学习者搜索短语：`適合學英語的讀者通過美國新聞學英語`。全文：`The Lucerna 英語週報 VOL.2：美國中期選舉投票日 11 月 3 日星期二、11 月 1 日時鐘撥回、11 月 6 日星期五電影《貓帽子》與《哥斯拉-1.0》、11 月 8 日星期日 NFL 馬德里賽與聖保羅 F1；正文英語、講解繁體中文，A2–B2 分級，150 道練習，適合學英語的讀者通過美國新聞學英語。`
- **图片**：逐页载荷 = 核心（几何与 base64 载荷杂凑逐页全等）：P1（投票亭，896×320）、P2（Halloween 明信片，434×440）、P3（Manet 猫图，434×470）、P4（1910 橄榄球，434×470）、P6（国会大厦，434×300）；P5／P7／P8 无照片（与核心同）。署名在版且与核心逐字同：P1 `Kenneth C. Zirkel — CC0, via Wikimedia Commons`、P2 `Public domain, via Wikimedia Commons`、P3 `Édouard Manet — CC0, via Wikimedia Commons`、P4 `Frank R. Snyder — public domain, via Wikimedia Commons`、P6 `Public domain, via Wikimedia Commons`——皆为公有领域／CC0，署名完整。
- **双 PDF**：印刷版 8 页 28,641,015 字节（sha256 fdc31a75…91ca10）、网页版 8 页 3,712,890 字节（＜10 MB，sha256 199611ac…7708e98），与 KIT §8 针脚全等；卡片 8 张皆 1950×2700 RGB。

## 非阻塞观察（单列，不构成阻塞）

- **O1（KIT 数字 stale）**：KIT §6“新增 CJK 共 762 字”与终态实测不符——freeze 口径 760、严格 CJK 口径 759。方向与 FIX1 省字一致，但首轮文件未留存故无法逐项复原 762 的来源；纸面数字以本报告实测为准，KIT 应订正为 760（freeze 口径）并注明口径。
- **O2（建造员繁体账目 3 处小 gaps，纸面无误）**：界外字 54→实测 55（漏计同形字“久”）；7 命中之“道＝報導”实为導／道混淆（紙面報導用字正確）；“斯＝蘇斯博士”漏计“哥斯拉” 1 处。校对结论（残留 0）立足本报告完整交叉核验，不依赖建造员账目；KIT 应订正上述 3 处表述。
- **O3（FIX1 第 2 处措辞）**：`not 表否定對照`→`not 表否定`略失“对照” 细微差别，陈述本身正确，非事实错误；可接受，不要求返工。
- **O4（KIT 方向措辞）**：KIT“EN↔ZH 双向／英↔繁中”说法与渲染（4 道皆 EN→ZH）不符；纸面正确，KIT 措辞应改为 EN→ZH。
- **O5（过程记录缺口）**：首轮 SVG 本体与 pre-FIX1 transform.py 未留存（见 §6）；freeze.py 原样调用对已重定向 build-copy 会误写旧 scratch 路径（见 §1）。皆为过程／工具记录问题，终态已全部独立实测，不影响本版结论；建议后续周期保留每轮 SVG 快照、freeze 对已重定向 copy 应显式报错而非静默误写。

## 证据索引（本目录）

- `hashes-before.txt`、`hashes-after.txt`（diff 为空）
- `baseline-my/`（核心重跑 SVG）、`baseline-my-hashes.txt`
- `freeze-diff-my.json`、`freeze-removed-my.txt`
- `p8-core-my.json`、`p8-ed-my.json`、`p8-compare-my.json`、`p8-reg-core-self.json`、`p8-reg-w43.json`、`p8-reg-enpt.json`、`p8-mut-wrongkey11.svg`、`p8-mut-nonote.svg`、`p8-old.py`
- `occlusion-my.json`、`geom-my.py`、`geom-my.txt`、`geom-p6-my.txt`
- `charset-my.json`、`reg-core-my.json`、`regen-ed/reg-ed-my.json`、`regen-check/`（transform 再生对照）
- `crop-p4caption.png`、`crop-p6ballot-ed.png`、`crop-p6ballot-core.png`、`crop-p6ballot2-ed.png`、`crop-p6ballot2-core.png`、`crop-p6chart-ed.png`、`crop-p6chart2-ed.png`
