# PROOF-NOTE — 2026-w47-ja-en 第一轮独立复校（叶子）

- 版：`2026-w47-ja-en`（日文目标语 × 英文读者），VOL.4，刊期 2026-11-16〜22
- 校对员：叶子（第一轮独立复校；与 builder、core-ja builder、各轮复校员不同人）
- 日期：2026-11-11（UTC 05:26 起）
- 复校对象：`production/2026-w47/fanout-ja/2026-w47-ja-en/`
- 身份核对（开工时 + 收工时两次）：印刷 PDF `Lucerna-VOL4-JA-EN.pdf`
  27,440,477 字节，SHA-256 `c29f6f987ba709082145c4ca71b7a656eb0b6bcc5f5f49d89f22b35a6161bbeb` ✓；
  网页 PDF `Lucerna-VOL4-JA-EN-web.pdf` 4,428,571 字节，SHA-256
  `9d10efc5fdc72c1c46194eea25cb5ff7b59f52c316a13fb5564395439396beb1` ✓。
  两份 PDF 在复校全程未被改动（收工复核 SHA 与开工一致）。
- 方法：8 版印刷版逐版目视（从印刷 PDF 重新渲染，100 dpi，不采信 builder 的图）+
  网页 P1/P8 目视；core-ja 与 fan-out 全量源码 diff 逐行审读（5 个 content 模块 +
  bslib4/render）；全部机械门自跑（见 GATE-LOG.md）。
- 本人只检查、不改任何源码/成品。以下缺陷须返修后重渲染并从头再做一轮全量校对
  （SOP §8.4）。

## 缺陷清单（共 2 条，同一类：英文答案简析中力士名罗马音拼错）

### D1 — 「美ノ海」误作 `Umi-no-umi`（P8 答案 48）
- 位置：P8 答案区 Page 4 组，第 48 条（另见 P4 A组第 48 题的答案简析）。
- 原文（印刷）：`48. B — Umi-no-umi lost to Hōshōryū on day 1`
- 应为：`48. B — Churanōmi lost to Hōshōryū on day 1`
- 证据：美ノ海的正式读法是「ちゅらのうみ」（日刊スポーツ 2018-05-30 改名报道：
  「美ノ海（ちゅらのうみ）」；sumo-guide 力士名鉴：四股名「美ノ海 義久
  （ちゅらのうみ よしひさ）」）。`Umi-no-umi` 是按汉字字面拼出的错误读法，
  「美」在此读作 `chura`（冲绳方言「美丽」），不是 `umi`。
  键本身 B 正确；错的是简析里的罗马音人名。
- 严重度：中。答案键正确，但教学材料的注释把真实人物的名字拼错，
  读者会学到错误的读法。本版内仅此 1 处。
- 来源：core 中文简析「首日败给丰升龙的是美之海」不含罗马音，
  是 fan-out 英译时新引入的拼写。

### D2 — 「藤凌駕」误作 `Fujiryūga`（P8 答案 49、54、63、111、116，共 5 处）
- 位置：P8 答案区 — Page 4 组第 49、54、63 条；Page 7 组第 111 条；
  Page 8 组第 116 条。
- 原文（印刷）：
  - `49. A — Fujiryūga beat Hōshōryū on day 3`
  - `54. 11 — Fujiryūga's kinboshi: 11th tournament since debut`
  - `63. ○ — Fujiryūga won a kinboshi on day 3`
  - `111. 11 — Fujiryūga's kinboshi: 11th tournament since debut`
  - `116. A — Hōshōryū lost to Fujiryūga on day 3`
- 应为：`Fujiryōga`（`Fujiryōga beat …` / `Fujiryōga's kinboshi …`）。
- 证据：藤凌駕读作「ふじりょうが」（日刊スポーツ 2025-10-01：
  「藤凌駕（ふじりょうが）」；日本相扑协会官方资料 via ozumo.jp：
  「藤凌駕 雅治（ふじりょうが まさはる）」；体育报知 2026-11-11 亦同）。
  `凌駕` 读 `ryōga`，长音是 ō 不是 ū。本版其余长音一律用 macron
  （Ōnosato、Hōshōryū、Shōsetsu），故 `Fujiryōga` 与版内体例也一致。
  5 处键本身（A / 11 / ○ / 11 / A）全部正确；错的只是简析里的罗马音。
- 严重度：中。同 D1。5 处同源（一处译名、五处引用），返修时须五处同改。
- 补充核实：除此二人外，本版其余罗马音人名均已核对无误——
  Yoshinofuji（義ノ富士 よしのふじ ✓，出现在答案 47、115）、Ōnosato、
  Hōshōryū、Miura Riku、Shōsetsu、Ni-no-tori、Ichi-no-tori、kumade、
  Chiikawa、ryuuryuu（按 KIT 指定拼法）皆正确；Kotosakura/Kotozakura/
  Aonishiki/Kirishima/Ura 未进入任何英文简析。

## 已核实通过的项目（无缺陷）

1. **题量与分布**：run.py 重跑 REGISTRY STATS：总数 150；级别 A2 48 / B1 73 /
   B2 29；分版 10/18/18/18/18/18/12/38；题型 fill-in 50 / multiple choice 51 /
   matching 12 / sentence building 8 / true/false 11 / cloze 13 / translation 4 /
   writing 1——与 KIT §1 登记完全一致。8 版题号目视连续 1–150，无缺重。
   徽章计数逐页复核与登记一致（3 个 matching 组各 4 题共用 1 枚徽章，故徽章
   总数 141 = 150 − 3×3；按级别 A2 45(+3)/B1 70(+3)/B2 26(+3) 与登记吻合）。
2. **金句 8 条**：逐字比对正文——8 条日语句子一字不差出现在所注页码的文章里
   （p.1×3、p.2×2、p.3×1、p.4×1、p.7×1，其中第 6 条在 P7 B1 栏目原文与
   金句区各出现一次）；英文释义忠实，无新增事实。
3. **VOL**：VOL.4 每版均有（P1 3 次、P2–P8 各 1 次）；VOL.3 仅 P4 1 次、
   VOL.5 仅 P4 1 次 + P7 3 次，核对与 core-ja 计数完全相同，均为冻结的
   正文文字（前号注记/下期预告），无误印。
4. **讲解语言**：讲解层、界面、图注、页脚、答案简析全为英文；核心日文
   正文、题干、栏目名逐字节与 core-ja 一致（源码 diff 证实）。
5. **小节头冻结**：A 理解 / B ことば / C 数字と日付 / C 文を作りましょう /
   D ペアにしましょう / D 正しい・正しくない / B グラフ / C 数字と事実 /
   D 文を完成しましょう / B 一般問題 / スポーツ 体育 等全部为日语原文，
   版内无任何英文小节头；题型标签（fill-in、multiple choice、cloze、
   matching、sentence building、true/false、translation、writing）与
   instr（Fill in、Match words to meanings、Build a sentence、Translate、
   True or false?、Writing）均为英文。
6. **221 键转写（机制核实）**：core-ja 与 fan-out 5 个 content 模块 +
   bslib4/render 全量 diff 逐行审读——274 个 distinct 已改字面量 +
   bslib4 4 处全部是中→英的忠实转写（抽查的相扑事实、日期、图表数字
   均与正文一致）；未改的全部 CJK 字面量逐一核查，均为冻结日语
   （文章、题干、栏目名、桥接词日语部分），无一处遗漏的中文讲解
   （含 F3/F4 同类：P8 答案头、P7 两处桥接均已是英文）。
   注：map-en.json / map-keys.json / apply.py 不在本 clone
   （scratch-fanout-ja/ 缺失，见观察项 O3），221 这个数字本身无法
   从 map 重数；上述 diff 审计覆盖的范围与 map 相同且更严（逐字面量），
   可作等效核实。
7. **E 组 4 条 keydiff**：p8 compare keydiff 恰为 [137, 138, 139, 140]，
   status CLEAN；逐条核实原因——每条都是核心的中文翻译答案被译成英文：
   137「二之酉在11月19日。」→ "Ni-no-tori is November 19."；
   138「新酒在11月19日解禁。」→ "The new wine is released November 19."；
   139「流行语提名在11月5日发表。」→ "The buzzword nominees were announced November 5."；
   140「去看红叶的人应该同时确认预报日期和现在的状况。」→
   "People going to see the leaves should check both the forecast dates and how things look now."。
   其余 146 条键与核心逐字节一致。
8. **ちいかわ / りくりゅう**：`Chiikawa` P7 1 次 + P8 3 次，与核心的
   「吉伊卡哇」出现次数逐版对应；`吉伊卡哇` 全版 0 次；`ryuuryuu`
   P7 1 次 + P8 4 次，与核心一致；`りくりゅう` 出现次数与核心逐版
   相同（P1 1、P5 5、P7 3）。
9. **中文残留**：全版扫描——除有意保留的中文原文引用外无中文残留。
   具体：text dump 中「吉伊卡哇」「中国」0 次；政治类禁词
   （政治/战争/选举/乌克兰/巴勒斯坦/以色列/总统/首相/政党/国会等 20 词）
   全部 0 次；未改 CJK 字面量审计（§6）0 遗漏。
10. **U+2019 回归**：8 个 SVG 中 U+2019 总数 0，U+2018 亦 0；
    印刷/网页 PDF 文字层中 U+2019 0；含撇号的行放大目视抽查
    （P7 "France's Beaujolais region"、P8 key 54 "Fujiryūga's kinboshi"），
    撇号为窄形 ASCII 撇号，无宽字形、无断裂。
11. **§1.1  grep 审计**：纸色 `#fbfaf6` 每版 1 次，旧色 `#f7f1e2` 0 次，
    禁色（金/红褐）0 次，`·` 8 版 0 次；徽章色 A2 `#5c6e30` / B1 `#46581f` /
    B2 `#37402f`；刊头 `Lucerna` 196px（P1 仅 1 处）；页码行 `Page N of 8`
    每版 1 次；页脚 `Lucerna　JAPANESE WEEKLY VOL.4　Japanese text　English explanations`。
12. **P8 字号**：PyMuPDF 实测印刷 PDF 第 8 页最小字号 9.98pt（≥9.75pt ✓，
    即 KIT 登记的 9.975pt）；题干 10.35pt（79 个 span，含抽查的 113 题题干），
    未动；范文 154 字（NCHARS 实算 154，与 P8 登记一致）。
13. **事实抽查**：相扑 1–3 日赛果、金星纪录（初土俵 11 场所、年 6 场所制
    以来第 7 快）与 2026-11-10/11 日刊体育・体育报知报道一致；
    图表 38/24/22/16 = 100%、38−24=14、38+24=62 验算无误；
    日期星期核对：11 月 16 日（月）、19 日（木）、22 日（日）、23 日（月）、
    12 月 1 日（火）、11 月 5 日（木）、7 日（土）、8 日（日）皆正确。
14. **图片与出处**：5 图与核心相同（P1 枫叶、P3 葡萄园、P5 岚山池、P7 酉市、
    P8 天龙寺），英文图注均为翻译后的出处（Photo: … — CC0 / public domain
    (Wikimedia Commons)）；P6 图表明确标注练习数据。

## 观察项（不计缺陷）

- O1（措辞）：P1 顶栏 `毎週、日本語で　Weekly　日本人が読んでいる日本語を読む`——
  "Weekly" 是核心「每周一期」的直译，夹在日语句中略显突兀，但属于可接受的
  刊头短语译法，未造成误解。
- O2（拼写体例）：答案 80 "ryuuryuu is the pair of Miura Riku and Kihara Ryuichi"——
  木原龍一写为 "Ryuichi"（无 macron），而版内其余长音用 macron
  （Ōnosato、Hōshōryū）。"Ryuichi" 是英文媒体通用拼法（如 Ryuichi Sakamoto），
  不算错误，仅体例不完全统一。
- O3（输入缺失，非本版缺陷）：任务要求先读的
  `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md`（顶部审计节与关键
  裁定备忘）及该目录下全部 builder 门输出（en-occlusion-run9.json、
  en-p8-final.json、en-p8compare-run9.json、en-sha-run9.txt、build-en-run10.log、
  map-en.json、apply.py）在本 clone 中不存在（`find` 全仓无此文件）。
  本轮改用 KIT §7/§11 + 全部机械门自跑 + 全量源码 diff 作等效核实，
  未因此漏查；但 builder 的审计记录无法逐项复核。
- O4：P2–P6 中栏下半部留白较大（特稿只占 1–2 栏、第 3 栏为边栏盒），
  与核心版式一致，非本版引入。

## 结论（报事实，不作定稿决定）

本轮发现缺陷 2 条（D1、D2，同一类：P8 答案简析中 2 个人名罗马音拼错，
共影响 6 条答案简析：48、49、54、63、111、116；答案键本身全部正确）。
其余核查项全部通过，机械门全绿（见 GATE-LOG.md）。
按 SOP §8.4，须返修（仅改 D1、D2 两处译名）→ 整期重渲染 → 从头再做
一轮全量校对，零问题方可定稿。
