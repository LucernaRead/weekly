# W47 zh-tw 家族独立重校 PROOF-NOTE-2（SOP §8/§8.4，第二轮全量重校）

- 校对员：独立重校员（全新工人，与建造者、第一轮校对员、修复者均不同；只校对、不修复、不重建、不 commit、不 push、不跑 lint）
- 校对范围：目标语 zh-tw × 读者母语 en de fr es it pt nl ru ja ko，共 10 版；不做 zh-cn×zh-tw 版
- 刊期：2026 年 11 月 16–22 日，VOL.4
- 盘上目录核对：`core-zh-tw`（= zh-tw-en）+ `2026-w47-zh-tw-{de,es,fr,it,ja,ko,nl,pt,ru}`，共 10 个，无多无少；无单独 `2026-w47-zh-tw-en` fan-out 目录
- 磁盘门限：开工 94G 已用；收尾 95G 已用（< 100G，未触发停手）
- 先读：SOP.md 全文（重点 §8）+ 第一轮 `scratch-reproof-w47-zh-tw/PROOF-NOTE.md` 全文 + `scratch-fix-zh-tw/FIX-LOG.md` 全文
- 工具 HEAD：repo HEAD `b06cb15e`（"§1.1 style: English W43, 11 editions re-rendered"）；`tools/` 最新提交 `b9ac29a6`（与第一轮收尾复核时相同，工具未变）
- 本文件只记录校对结论；发现的问题不修

## 结论：(a) 干净 —— 0 条新发现

第一轮的 1 条低严重度问题（P7 金句第 8 条缺「香港」二字）已在 10 版全部修复并逐版核实（见「修复核实」）。本轮从头全量重校未发现任何新问题：内容事实、翻译准确、术语一致、引文逐字、答案正确、机械门禁全部通过（日版仅一项已书面定性的人为产物，见下）。

| 严重度 | 数量 |
|---|---|
| MAJOR | 0 |
| MEDIUM | 0 |
| low | 0 |
| **合计新发现** | **0** |

## 修复核实（FIX-LOG 所称修复逐版核实）

- 10 版 text.md 的 P7 第 8 条引文均为「香港迪士尼聖誕，從11月17日開始」，逐版计数恰 2 处（P5 原句 + P7 引文），裸引文（无「香港」）0 处。
- 10 版 text.md 尺寸均为修前 +6 字节（「香港」二字 UTF-8 各 3 字节），SHA12 与 FIX-LOG 修后表逐项一致；印 PDF / 网 PDF 的尺寸与 SHA12 亦与 FIX-LOG 修后表逐项一致（见「文件清单」）。
- freeze diff（修前 SVG 快照 vs 现版）：10 版全部仅 P7 有变化，新增 CJK 恰 {香:1, 港:1}，P8 零变化。
- textcheck-adapted：10 版全部 PASS（印/网文字层多重集差 0；修前→修后印层仅 +香/港）。

## 文件清单（校对的那份文件：尺寸 + SHA256 前 12，与 FIX-LOG 修后值逐项一致）

| 版 | 印 PDF（字节 / SHA12） | 网 PDF（字节 / SHA12） | text.md（字节 / SHA12） |
|---|---|---|---|
| core-zh-tw (zh-tw-en) | 11195126 / 27afa3281b1d | 1898131 / 45d076003801 | 49804 / 9b8b5295ddd8 |
| zh-tw-de | 11196101 / 2a22bcdaa8ca | 1903630 / a67ffad91835 | 51820 / 8187f6196326 |
| zh-tw-es | 11194154 / 25216239cbf9 | 1902298 / f8c0086a1a66 | 52252 / e8a36b7996f6 |
| zh-tw-fr | 11191659 / 47320e77d6f1 | 1899287 / 233658513953 | 52476 / a2df8892d632 |
| zh-tw-it | 11187826 / 0cdf05fef852 | 1895728 / 3ed32974c27d | 51691 / 788ed6f6600c |
| zh-tw-ja | 16365954 / dbbe03ab27b3 | 2447388 / 660f93940fe8 | 53759 / 6e5b4b81e131 |
| zh-tw-ko | 12719179 / e49ab5fee582 | 2134244 / 7419fee9eedf | 53922 / 0215bc2cf6a6 |
| zh-tw-nl | 11189718 / 20ad418b233c | 1898763 / d28897aea142 | 50602 / 487127dd7d72 |
| zh-tw-pt | 11198017 / 7c59676c6ef0 | 1907201 / 90caf45fab41 | 51498 / 542bfae121e5 |
| zh-tw-ru | 11366471 / eb3fd9aae5e2 | 2070994 / 16a6d20a755e | 62498 / ea9c1514df96 |

收尾复核：10 版 text.md SHA12 与上表一致（本任务全程只读，未改动生产目录）。

## 逐版结论

### core-zh-tw（zh-tw-en，读者母语英语）
- text.md 全文通读（6023 行）：150 题答案逐题复核，全部正确；编号连续；答案与题面/原文/图表一致
- P7 8 条金句逐条核对：每条在 P7 出现 1 次、在 P1–P6 原文出现 1 次，全部逐字（第 8 条含「香港」，见上）
- 算术全验：1200+800=2000、退货后实付 800；11 月 6–22 日 = 17 天；17:00→18:30 = 1.5 小时；11 月 17 日–1 月 3 日 = 48 天（14+31+3）；11 月 17–22 日 = 6 天；11 月 13 日–12 月 27 日 = 45 天；5×10=50、7×10=70、距 100 差 30；14:00→19:00 = 5 小时；主灯秀 17:30–23:00 每半小时 = 12 场
- 模范作文实测字符数 = 142（去空白），与标注一致
- 日期/星期（Asia/Taipei `date` 独立核对）：11 月 13 日周五、15 日周日、16 日周一、17 日周二、19 日周四、21 日周六、22 日周日、24 日周二、12 月 27 日周日、2027 年 1 月 3 日周日、11 月 6 日周五、10 月 23 日周五、11 月 11 日周三——纸面星期表述全部正确
- 繁體字形/标点：中文数字无空格（第1版／共8版、11月11日等），未见简体字混入
- P1 刊头 + 配对徽章、页脚配对标注、摘要（英文读者版，7 主题、150 题、A2–B2）均在
- 版式：P1、P8 卡片图目视 + P7 联系表目视，无溢出/重叠/压页脚/豆腐块/截断
- **新发现：0**

### zh-tw-de（读者母语德语）
- 讲解层全文通读（与 core 的 diff 全量，580 行新增）：翻译准确；全部事实/数字/日期与 core 一致；150 条 P8 注释答案键与 core 完全相同
- 术语：鑑賞期作 "Bedenkzeit"（德语法定概念），恰当；"1.200 NT$" 德语千分位点正确
- 页脚中文 + 德语页码行 "Seite N von 8"；摘要德语版，7 主题、150 题一致
- P7 金句第 8 条含「香港」；其余 7 条译文与核心一致
- **新发现：0**

### zh-tw-es（读者母语西班牙语）
- 讲解层全文通读（586 行新增）：翻译准确；事实/数字/日期与 core 一致；150 条 P8 注释答案键与 core 相同
- 术语：鑑賞期作 "periodo de desistimiento"、"63.ª"、"8.º" 序数写法正确
- 页脚中文 + 西班牙语页码行 "Página N de 8"；摘要西班牙语版一致
- P7 金句第 8 条含「香港」
- **新发现：0**

### zh-tw-fr（读者母语法语）
- 讲解层全文通读（577 行新增）：翻译准确；事实/数字/日期与 core 一致；150 条 P8 注释答案键与 core 相同
- 术语：鑑賞期作 "délai de rétractation"、"1 200 NT$" 法语千分位空格正确；《月球之旅》作 "Le Voyage dans la Lune"，正确法语片名
- 页脚中文 + 法语页码行 "Page N sur 8"；摘要法语版一致
- P7 金句第 8 条含「香港」
- **新发现：0**

### zh-tw-it（读者母语意大利语）
- 讲解层全文通读（562 行新增）：翻译准确；事实/数字/日期与 core 一致；150 条 P8 注释答案键与 core 相同
- 术语：鑑賞期作 "periodo di recesso"、"parata scudetto"（封王游行）地道
- 页脚中文 + 意大利语页码行 "Pagina N di 8"；摘要意大利语版一致
- P7 金句第 8 条含「香港」
- **新发现：0**

### zh-tw-ja（读者母语日语）
- 讲解层全文通读（假名行提取全量，616 行）：翻译准确；事实/数字/日期与 core 一致；150 条 P8 注释答案键与 core 相同
- 术语：鑑賞期作 "クーリングオフ期間"（日本法定概念），恰当；"トップ記事"（頭條）恰当
- P7 A2 "ナイトパレードは19:00に始まる" 经原文 grep 核实完整（"19:00" 在 text.md 第 4038 行，提取断行系假名行切分所致，非缺失）
- 页脚中文 + 日语页码行 "第Nページ／全8ページ"；摘要日语版一致
- P7 金句第 8 条中文引文含「香港」（译文「ディズニーのクリスマスは11月17日から始まる」为译文，非引文本身）
- **新发现：0**（checks.py SIMP_ONLY 一项为已书面定性的人为产物，见「机械检查」）

### zh-tw-ko（读者母语韩语）
- 讲解层全文通读（843 行新增）：翻译准确；事实/数字/日期与 core 一致；150 条 P8 注释答案键与 core 相同
- 术语：鑑賞期作 "청약 철회 기간"（韩国法定概念），恰当；"톱 기사"（頭條）恰当
- B2 小雪句经原文核实完整："小雪은 스물네 절기 중 스무 번째, 立冬 다음 이에요"（text.md 第 4713 行含「立冬」，diff 提取时因与核心相同而未列入）
- 页脚中文 + 韩语页码行 "제N면／전체 8면"；摘要韩语版一致
- P7 金句第 8 条含「香港」
- **新发现：0**（小雪译名不统一为第一轮已记观察，见「观察」）

### zh-tw-nl（读者母语荷兰语）
- 讲解层全文通读（546 行新增）：翻译准确；事实/数字/日期与 core 一致；150 条 P8 注释答案键与 core 相同
- 术语：鑑賞期作 "bedenktijd"（荷兰法定概念），恰当；"HOOFDVERHAAL"（頭條）恰当
- P7 A2 首词 gloss "(parade)" 与核心英文相同，故未出现在 diff 中，非缺失
- 页脚中文 + 荷兰语页码行 "Pagina N van 8"；摘要荷兰语版一致
- P7 金句第 8 条含「香港」
- **新发现：0**

### zh-tw-pt（读者母语葡萄牙语）
- 讲解层全文通读（576 行新增）：翻译准确；事实/数字/日期与 core 一致；150 条 P8 注释答案键与 core 相同
- 术语：鑑賞期作 "prazo de arrependimento"（葡语法定概念），恰当；"MANCHETE"（頭條）恰当
- 页脚中文 + 葡萄牙语页码行 "Página N de 8"；摘要葡萄牙语版一致
- P7 金句第 8 条含「香港」
- **新发现：0**

### zh-tw-ru（读者母语俄语）
- 讲解层全文通读（934 行新增）：翻译准确；事实/数字/日期与 core 一致；150 条 P8 注释答案键与 core 相同
- 术语：鑑賞期作 "период охлаждения"，恰当；"ГЛАВНАЯ ТЕМА"（頭條）恰当；大巨蛋音译 "Тайбэй Доум" 一致
- 弯引号：5 处 U+201C 均为俄语嵌套引号 „…"（如 «Мире „Холодного сердца"»），字体路由正确；拉丁标题字体问题按任务指令不重报（已知跨家 D5 系统性问题，另有工人统一修）
- 页脚中文 + 俄语页码行 "Страница N из 8"；摘要俄语版一致
- P7 金句第 8 条含「香港」
- **新发现：0**

## 中文正文跨版一致性
- CJK 字符序列 diff（core vs 各 fan-out）：de/es/fr/it/nl/pt/ru 各 18 处操作，全部为预期改动——配对标注（英語講解→读者语讲解）、本周一词释义译文、页脚/页码行本地化；ja 289 处、ko 294 处操作均为讲解层日文汉字/韩文汉字，预期内。中文文章内容无分歧。

## 机械检查（`~/workspace/weekly-git/tools/venv/bin/python`，只读重跑，未重建）

门禁脚本：本目录 `reproof2_gates.sh`（checks / occlusion / p8 compare / spill / boxtitle / edge / D5 census / 引号普查 / freeze diff vs 修前快照 / textcheck-adapted / P8 字号）。输出：`gates/<slug>/GATES-SUMMARY.txt` 及各门日志。

| 版 | checks | occlusion | p8 (150) | spill | boxtitle | edge | D5 census | 引号普查 | freeze diff | textcheck-adapted | P8 字号 | OVERALL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| core | PASS | 0 flags | extract 150/150 | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | ALL-GREEN |
| de | PASS | 0 flags | CLEAN | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | ALL-GREEN |
| es | PASS | 0 flags | CLEAN | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | ALL-GREEN |
| fr | PASS | 0 flags | CLEAN | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | ALL-GREEN |
| it | PASS | 0 flags | CLEAN | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | ALL-GREEN |
| ja | FAIL（仅 SIMP_ONLY，见下） | 0 flags | CLEAN | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | HAS-FAILURES（仅此一项） |
| ko | PASS | 0 flags | CLEAN | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | ALL-GREEN |
| nl | PASS | 0 flags | CLEAN | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | ALL-GREEN |
| pt | PASS | 0 flags | CLEAN | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | ALL-GREEN |
| ru | PASS | 0 flags | CLEAN | 0 SPILL | 0 DEFECT | 0/0 | PASS | 0 缺陷 | +香/港 | PASS | 9.75pt / 8 页 | ALL-GREEN |

- p8 compare：9 个 fan-out 版全部 `CLEAN`，150/150 noted，missing []、extra_count=0、uncertain []、keydiff []
- occlusion：10 版全部 0 flags（自检 6 类全触发）
- spill：10 版全部 0 SPILL；boxtitle：10 版全部 0 DEFECT；edge：10 版全部 0 TOUCH / 0 NEAR
- D5 census：10 版全部 0 个拉丁字符落入 CJK-sans `<text>` 元素（D5_latin_in_cjk=0，curly_total=0；ru 的 5 处弯引号在 Newsreader 字串内，路由正确）
- 引号普查：10 版全部 0 缺陷字
- text.md 与印 PDF 一致性：10 版全部多重集差仅为已知导出 artifact（text.md 标题行/ Markdown 标记、PDF 独立 `Lucerna` 刊头字标），**CJK 字符零差异**
- P8 最小字号 10 版全部 9.75pt（达 SOP §1.1 下限），最大 34.5pt；10 版全部 8 页

### ja SIMP_ONLY（不重报，已书面定性的人为产物）
- 本轮重跑：ja 版 `checks.py` 报 `SIMP_ONLY_HITS ['国', '学']`，`CHECKS FAIL`（RC=1），与修前快照及 FIX-LOG 记录完全相同的一组。
- 定性沿用 FIX-LOG：误报，与修复无关——`国`/`学`是 P3 日文讲解句「高雄国際鋼雕芸術祭」等的正常日文汉字，不在本次改动文件内。其余 9 门全部通过。

## 红线核查
- 选题为台湾/香港活动（游行、金马奖、钢雕、耶诞城、迪士尼、爵士、宝可梦），目标国是中国语境下中文版不碰中国国内政治——core 及全部 fan-out（共享同一中文正文）无违规内容

## 观察（非问题，不计入结论；均为第一轮已记或任务明令不报项）
1. P4 注释「封王：拿下總冠軍，叫封王——上週本報已經教過這個詞了」（core text.md:2088 行附近），而 P1 本周一词也是封王；"上週已教"为跨期主张，本周文件内无法核实（第一轮已记，本轮同样不作发现）
2. ko 版 P8 注释中小雪表述不统一（Q98/Q117/Q138 "샤오쉐" vs Q25 "소설" vs 其余 "Xiaoxue"）；每处均紧邻中文原词「小雪」，不影响理解（第一轮已记，本轮同样不作发现）
3. `svglib.py` 注释 "exactly 2 glyphs in this edition" 已过期（当前构建 core + 8 版为 0 处弯引号）；代码注释问题，非版面缺陷（第一轮已记，FIX-LOG 已裁定不管）
4. zh-tw-ru 版拉丁标题字体问题（拉丁文用了 Noto Sans 而非 Newsreader）：已知跨家 D5 系统性问题，另有跨家工人统一修 svglib.py；按本轮任务指令不重报；该版内容照常校对，无问题

## 版式目视
- 方法：10 版 P7 卡片图拼为 2 张 5 联联系表（半幅）目视 + 核心 P1、P8 整页目视；联系表为临时中间件，目视后已删除
- 结果：10 版 P7 全部干净——语言聚焦三栏、易错诊所、金句栏（8 条两栏）、下期预告均无溢出/重叠/压页脚/豆腐块/截断；核心 P1 刊头 + 配对徽章、头条、侧栏、测验区与 P8 测验 + 全部答案区均干净；机械 occlusion 审计 0 旗标与目视一致

## Scratch 文件
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof2-w47-zh-tw/`：
`PROOF-NOTE-2.md`（本文件）、`reproof2_gates.sh`、`gates/<slug>/GATES-SUMMARY.txt` 及各门日志（`gates/<slug>/` 下）、`diff-en-{de,es,fr,it,ja,ko,nl,pt,ru}.txt`、`plus-readable-{de,es,fr,it,ko,nl,pt,ru}.txt`、`ja-kana.txt`。联系表 `p7-sheet-*.png`、`core-p1-front.png`、`core-p8-test.png` 目视后已删除。
