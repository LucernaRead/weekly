# The Lucerna · 英语周报 VOL.1 — WEEKLY KIT

English core, week of **Monday October 19 to Sunday October 25, 2026**. First issue of the
English edition. English text is written natively from the US trend pool; the explanations
in the reader's native language (Chinese) appear as small gray glosses, notes and answer
explanations only. Masthead: **The Lucerna** (the article follows the target language).

## 一、交付物

`files/weekly-report-en-vol1/`：

- `svg/` — 8 pages of SVG sources (p1-front … p8-exercices)
- `cards/` — 8 full-page PNGs, 1950×2700
- `The-Lucerna-VOL1.pdf` — merged 8-page PDF, 24.5 MB (CairoSVG embeds the page images
  uncompressed, same as the French VOL.2 original)
- `The-Lucerna-VOL1-web.pdf` — Discord-sized compressed PDF, **4.18 MB** (< 25 MB limit;
  page JPEGs q85 at 1400 px wide)
- 本文件

构建代码在 `hidden_files/weekly-report-en-build/`：`svglib.py`（与法语版相同）、
`bslib4.py`（四栏流式排版 + 题目登记表 REG，答案页由登记表自动生成，页脚改英语版）、
`content12.py / content34.py / content56.py / content7.py / content8.py`（逐版内容）、
`assets/`（4 张图 + `CREDITS.md`）。

## 二、规格

- 8 版，1950×2700，四栏，暖象牙底、深橄榄点缀，黑体字刊头 The Lucerna。
- 难度坡度：P1 头版 A2 · P2 生活 A2 · P3 文化 A2→B1 · P4 体育 B1 · P5 青年 B1 ·
  P6 时事深读 B2 · P7 精讲（A2/B1/B2 三级专栏 + 本周金句）· P8 综合评估 + 写作范文 + 全部答案。
- 难度是坡度不是隔间：每版内题目可跨级混排，每题单独标 [A2]/[B1]/[B2]。
- 全期统一编号 1–149，答案集中印在第 8 版下方，附中文简析。

## 三、八版内容

| 版 | 内容 |
|---|---|
| P1 头版 | 头条 « First Votes, First Games : America's Biggest Week of the Autumn »（提前投票 + NBA 揭幕 + 世界大赛同周）；欧洲本周日拨钟、美国等到 11 月 1 日的深色对比横幅；本周热搜图（快照说明，无编造搜索量）；本期目录；本周词 fall back；1912 世界大赛老照片 + « FALL, THE SEASON OF FIRSTS »；快讯栏；闪电问答 4 题。即学即练 6 题 + 闪电问答 4 题 = 10 题 |
| P2 生活 | 社保 COLA 2027 年 +3.6%（SSA 10 月 14 日官宣，约 72M 人、平均 +$75/月、SSI 12 月 31 日先行）；Ida May Fuller 第一张支票故事（1940-01-31，$22.54）；Kayem 热狗召回（FSIS 10 月 17 日，约 158 万磅，冷却故障，发布时无病例报告）+ 召回通知怎么看；报时专栏（3 个自绘时钟 8:00 / 2:30 / 7:45）。17 题 |
| P3 文化 | 万圣节 $13.5B 之夜（NRF 调查 7,889 人：人均 $115.14，服装 $4.4B > 装饰 $4.3B > 糖果 $4.1B，96% 买糖，47% 用 AI）；门廊灯规则、南瓜田、1912 明信片史；1912 万圣节明信片图。18 题 |
| P4 体育 | NBA 揭幕夜 NBC/Peacock 三联播（76 人 106–100 胜尼克斯，Maxey 28 分；尼克斯升起 1973 年以来首面旗帜；LeBron 第 24 个赛季改穿费城球衣）；世界大赛 Brewers vs Rays（密尔沃基横扫道奇、坦帕周一淘汰克利夫兰、周五 G1、两队均从未夺冠）；F1 奥斯汀周末；NFL 第 7 周 + 大学橄榄球；周日 16:00 ET 国家德比。18 题 |
| P5 青年 | 开幕周活在手机上：流媒体三联播与 « lakers roster » 热搜快照、AI 策划装扮、财报周白话版（Tesla/Meta 周三盘后、Netflix/SpaceX 周二——**不印任何 EPS 预测数字**）、第二屏文化。18 题 |
| P6 深读 | 中期选举与提前投票（Reuters：众议院 218–214、广告支出截至 10 月 12 日达创纪录 $38 亿 AdImpact 数据；各州开跑日期全表；选举由各州运行）；国会山图；练习图表 « WHY DO VOTERS VOTE EARLY ? »（34/27/23/16，版面显著标注 PRACTICE DATA 教学虚构）。18 题 |
| P7 精讲 | A2 报时 + going to / B1 比较级 + 一般过去时 / B2 标题现在时 + whether；本周金句 8 句（全部出自本期文章原文，每句一语法点 + 一道跟练）；易错诊所 4 题；读者园地（编辑部示范，已明确标注，VOL.2 起登真实来信）；VOL.2 预告（10/31 万圣节 · 11/1 拨钟 · 11/3 选举日）。12 题 |
| P8 评估 | 完形 8（Maya 的 10 月 31 日）+ 单选 8 + 阅读 4（得州护士提前投票，自洽虚构小品）+ 完成句子 4 + 翻译 4（英↔中双向）+ 词汇配对 4 + 对话补全 5（投票站）+ 写作 1（« My Saturday, October 31 »，80–100 词，范文 87 词）。38 题 + 全部 149 题答案与简析 |

## 四、实测体量

- **可见文字量：41,362 字符**（独立校对轮以 XML itertext 复测，见第十节；法语 VOL.2 为 40,645，同级密度）。
- **练习总量：149 题**（统一编号 1–149，登记表实测）。
  - 按难度：**A2 58 · B1 72 · B2 19**
  - 按版：P1 10 · P2 17 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38
  - 按题型：完成句子 39 · 单选 34 · 句型转换 16 · 词汇配对 12（3 组）· 阅读判断 8 ·
    完形填空 8 · 跟练 8 · 图表读数 6 · 对话补全 5 · 改错 4 · 阅读理解 4 · 翻译 4 · 写作 1
  - P8 正式评估 38 题，其余 111 题是 P1–P7 的即学即练微练习（与对标报的分工结构相同）。

## 五、对标与差距（如实）

- 对标《英语周报》实测整期 ≈155 题：本期 149 题 = 96%，**距 ~150 目标差 1 题，不宣称达标**。
- 对比法语 VOL.2（145 题）：+4 题；P8 评估 38 题 vs 法语 37 题。
- B2 题量 19 题，少于法语 VOL.2 的 25 题——顶端难度偏轻，下期可加重 P6/P7 的 B2 份额。
- 完整版 PDF 24.5 MB（内嵌图未压缩，与法语版同病）；Discord 投递请用 4.18 MB 的 web 版。

## 六、选题与事实来源

选题只取自美国英语生态当周热度池：`hidden_files/trend-research-2026-w43/batch-A-en-de-es.md`
（EN 部分）。关键事实出处：

- 中期选举：Reuters（众议院 218–214；选举由各州运行）；AdImpact 经 Reuters（广告支出
  截至 10 月 12 日 $38 亿，创纪录）；各州提前投票起始日按研究池州表（TX 10/19–10/30，
  AK/AR/CT/CO 10/19，LA/MO 10/20，DE/MD 10/22，MI 与 FL 强制期 10/24 起）。
- COLA：SSA 官方（2027 年 +3.6%，10 月 14 日周三宣布；平均退休金约 +$75/月；约 7,200 万
  受益人；SSI 约 730 万人、12 月 31 日起）；Fuller 史实经 SSA 历史页与公开资料核对。
- 召回：FSIS 10 月 17 日 Class I 公告（Kayem Foods，约 1,584,361 磅，生产期 3 月 31 日–
  10 月 7 日，冷却故障，公告时无确认病例）——版面取约数 1.58 million pounds。
- NBA 揭幕战比分 76ers 106–100、Maxey 28 分、Brunson 21 分：2026-10-21 建报时经
  AP/theScore/ESPN/sportradar 交叉复核一致。**LeBron 助攻数各源冲突（6 vs 7），版面不印此数**；
  只印无争议的 14 分 / 9 篮板亦未采用——版面只写第 24 个赛季与改穿费城球衣。
- 万圣节：NRF 年度调查（7,889 名消费者，9 月 1–9 日）：$13.5B（同比 +3.82%）、人均 $115.14、
  糖果 96%/$4.1B、服装 $4.4B、装饰 $4.3B、47% 用 AI；Frightgeist 2026（10 月 14 日发布）。
- Google Trends 搜索量一律不印具体数字：头版热搜图只画相对条形并注明
  « Snapshots, Mon–Wed Oct 19–21 »；唯一例外是研究池有明确出处的 « hot dog recall »
  周一快照 200K+ 一行，版面已标注为周一快照并指向第 2 版召回报道。
- 美国夏令时 11 月 1 日结束（欧洲 10 月 25 日）：对比教学，不套用欧洲版的拨钟横幅。
- 红线：无国际政治；美国国内政治（中期选举）按 SOP 允许。练习图表显著标注为教学虚构数据。
  无编造民调、引语、统计。

## 七、图片与授权

4 张图，全部 Wikimedia Commons 公有领域，2026-10-21 经 Commons API 核验授权后使用，
每张在版面图注下印出处（详单见构建目录 `assets/CREDITS.md`）：

1. P1 — 1912 世界大赛球迷照（Bain News Service / Library of Congress，Public domain）
2. P2 — 1943 年社会保障卡（US Social Security Administration，Public domain）
3. P3 — « A Halloween Wish » 1912 年万圣节明信片（Public domain）
4. P6 — 美国国会大厦全景（Public domain）

现代体育摄影均为版权图，本期一律不用；图表为自绘。

## 八、复现

```bash
python3 -m venv /tmp/wp-venv && /tmp/wp-venv/bin/pip install cairosvg pillow pypdf   # 仅首次
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-en-build
/tmp/wp-venv/bin/python -c "import content12, content34, content56, content7, content8"   # 生成 8 个 SVG（顺序不可变，登记表按导入顺序累积编号）
/tmp/wp-venv/bin/python - <<'EOF'
import cairosvg, glob, os
from pypdf import PdfWriter
from PIL import Image
base = os.path.expanduser('~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-en-vol1')
w = PdfWriter()
for f in sorted(glob.glob(base + '/svg/*.svg')):
    cairosvg.svg2png(url=f, write_to=f.replace('/svg/', '/cards/').replace('.svg', '.png'), output_width=1950)
    cairosvg.svg2pdf(url=f, write_to='/tmp/enpage.pdf'); w.append('/tmp/enpage.pdf')
w.write(open(base + '/The-Lucerna-VOL1.pdf', 'wb'))
imgs = [Image.open(f).convert('RGB') for f in sorted(glob.glob(base + '/cards/*.png'))]
for im in imgs: im.thumbnail((1400, 1938))
imgs[0].save(base + '/The-Lucerna-VOL1-web.pdf', save_all=True, append_images=imgs[1:], quality=85)
EOF
```

字体：英文正文 Noto Serif CJK、中文讲解 Noto Sans CJK（/usr/share/fonts/opentype/noto/），
刊头黑体字 UnifrakturMaguntia（~/.local/share/fonts）。不要用 /opt/meta-chromium 渲染（本机挂死）。
构建出现 `FLOW OVERFLOW` / `HEAD TOO WIDE` 即版式缺陷，须先修内容再渲染；本期最终构建零警告。

## 九、校对记录（构建者全文校对，2026-10-21）

逐版通读 8 张整版图，所有答案逐题重推，日期与星期逐一对照 2026 年日历
（10/19 周一 … 10/25 周日、10/31 周六、11/1 周日、11/3 周二均核对无误），交叉引用逐条核对。
本轮修掉 6 处：

1. P7 金句 5 处引文与原文不符（压缩改写）→ 全部改为文章原句；1 处虚构出处
   （« Mallory 家的蜡烛 »，第 2 版并无此内容）→ 删除并换用第 2 版真实句子。
2. P1 第 5 题答案 opens 与头条文章用词（opened）及第 8 版第 126 题标准不一 → 统一为 opened。
3. P3 第 43 题原答案 « is going to buy » 与题面无时态提示、与同组一般现在时题冲突 → 改为 buys。
4. P5 « the first tripleheader in history » 超出来源表述 → 改为与来源一致的说法。
5. P6 右栏 « THE EARLY-VOTING WEEK · 提前投票周历 » 框标题超宽被裁 → 缩短标题。

裁定保留的提示（非错误）：

- P2 练习流末端超出版心下限 3px，落在页脚留白内，成图不可见。
- P1 热搜图免责行右端抵到版框，但未被裁切。
- P7 三级专栏在金句带上方留约 200px 空白，与法语版同版式节奏（版面分节）。
- P7 易错诊所的 ✗ 在当前字体下渲染为方框叉号，与法语 VOL.2 完全一致，可读。
- 范文 87 词，在题目要求 80–100 词内。

后续：本期将另行进入独立校对轮（全文 + 答案 + 事实再核一轮），源码与登记表结构保证改版成本低。

## 十、独立校对记录（2026-10-21，独立轮，非构建者自校）

方法：提取 8 个 SVG 全部可见文本逐版精读；149 题答案逐题对题面、原文、图表重新推导（语法、阅读事实、完形适配、翻译等值、图表验算）；题号连续性、逐版题量、目录与跨版引用逐项核对；全部日期与星期对照 2026 年日历；事实逐条回查研究池（batch-A EN 部分）与第六节出处；8 张整版 PNG 全部看图。构建者声称的 6 处修正逐项在成图中验证落地情况。修正全部写入构建源码后整期重渲染，再做一轮完整复校（全文重提取 + 与首轮 diff、改动版看图、其余版 SVG 与首轮字节一致）。

**共发现并修正 4 处**：事实 1 · 引文 3。另有由引文补全引起的版式溢出 1 处（已修），及本 KIT 实测数字 2 处更正（见下）。

| # | 类别 | 版 | 修正前 → 修正后 |
|---|---|---|---|
| 1 | 事实（无来源） | P4 « THE KING'S NEW TEAM » 框 | « He arrived this summer with Jaylen Brown, traded from Boston. Two stars, one new team, and a win… » → « He arrived this summer, and on night one, his new team won on the champions' floor. »；中文行 « 与从波士顿交易来的布朗一起加盟 » → « 首夜就在冠军主场取胜 »。理由：Jaylen Brown 交易一事在研究池与第六节出处中均无依据（研究池 NBC 稿件标题中的是 Jalen Brunson，系尼克斯球员），属无源事实，按 SOP 删除 |
| 2 | 引文 | P7 金句 1 | « The season opened with something new : a tripleheader. » → 改为第 4 版原句节录 « On Tuesday, October 20, the 2026–27 season opened with something new : a tripleheader. »（原引文删去了日期与年份，非原句） |
| 3 | 引文 | P7 金句 2 | « When the prices go up, the checks go up too. » → 改为第 2 版原句 « When the prices of food, homes and energy go up, the checks go up too. »（原引文删去了 of food, homes and energy） |
| 4 | 引文 | P7 金句 8 | « The clocks fall back on Sunday, November 1. » (page 1) → 改为第 2 版原文节录 « In Europe, the clocks fall back on Sunday — in America, on Sunday, November 1. »，出处标注改 (page 2)（原引文为拼合句，第 1 版并无此句） |

版式连带修正：3 处引文补全后金句带 FLOW OVERFLOW 129px（构建警告实测），将金句带字号 22→20.5、行距与间距略收（仅版式参数，不动文字），重渲染后构建零警告，金句带完整落在版区内，第 7 版看图确认无压栏、无与易错诊所/读者园地重叠。

本 KIT 数字更正：§四可见文字量 41,357 → **41,362**（首轮成图实测为 41,325，修正后复测 41,362，原数字两种口径均对不上）；web 版 PDF 大小 4.19 MB → **4.18 MB**（重渲染后实测 4,184,825 字节）。

**构建者 6 处声称修正的落地核验**：① 金句引文——部分落地：8 句中 5 句为原文逐字节录，3 句仍为压缩/拼合，已由本轮第 2–4 项补全；被删的虚构出处（« Mallory 家的蜡烛 »）确认已不在报上。② P1 第 5 题与 P8 第 126 题统一 opened——已落地，两处答案均为 opened 且与原文时态一致。③ P3 第 43 题 buys——已落地。④ « the first tripleheader in history »——已删除，全文无此表述。⑤ P6 框标题缩短——已落地，« THE EARLY-VOTING WEEK » 看图无裁切。⑥ 计数说明：构建者「6 处」实际列 5 项（第 1 项打包多处引文修正），本记录以逐项核验为准。

**复核无误的大项**：题号 1–149 连续无缺重，逐版题量 10/17/18/18/18/18/12/38 与 §四一致；149 题答案逐题复核无误——完形 8 空、单选、阅读 4 题、判断、三组配对（24–27、51–54、140–143）、翻译 4 题等值、对话补全 5 空（ID/line/ballot/sticker/November）均对题面与原文成立；练习图表四项合计 100%，读图 6 题（#82–87）逐题验算无误（61%、18 points、43<50 等）；P2 算术框 3.6%×$1,000/$2,000 = $36/$72 无误，$75 均增与「平均支票略高于 $2,000」自洽；全部星期（10/19 周一…10/25 周日、10/31 周六、11/1 周日、11/3 周二、10/14 周三、10/17 周六）与 2026 年日历一致；COLA、召回、NRF、AdImpact $3.8B（截至 10/12）、众议院 218–214、各州提前投票起始日、NBA 揭幕比分 106–100/Maxey 28、43 场、F1 音乐会阵容、NFL 第 7 周赛程均与研究池出处一致；LeBron 助攻冲突数未印、任何 EPS 预测未印；Google Trends 只以日期标注的快照呈现（« hot dog recall » 200K+ 已标注为周一快照）；练习图表显著标注 PRACTICE DATA；无国际政治；中文讲解逐条对照正文（每条讲解的词均在所注文章中出现，答案简析表述无误）；4 张图与 `assets/CREDITS.md` 一致且均为公版，图注与画面内容相符（1912 球迷照、1943 社保卡、1912 万圣节明信片、国会大厦）；P2 三只时钟指针与所标时间一致（8:00 / 2:30 / 7:45）；范文在 80–100 词要求内；机器扫描无重复词；术语核查通过——用户取消的那个中间层提法，其英文词与汉字词在正文与本 KIT 中均无出现。

**标记保留（裁定）**：① 构建者 4 项保留提示（P2 练习流末端 3px、P1 热搜免责行抵版框、P7 金句带上方留白、易错诊所 ✗ 字形）逐项看图复核，全部成立，沿裁定保留（P1 免责行末字完整未裁）。② P7 第 100 题答案 opened：该题为照金句原句设计的一般过去时形式练习，语法点决定唯一答案，且与第 126 题标准一致，保留。③ P7 B1 例句 « Maxey scored more points than Brunson » 为编辑部构造例句（非金句带），其数据（28 比 21）见第 4 版第 58 题，保留。④ P8 阅读 Rosa Delgado 为 KIT §三已声明的虚构练习小品，不作新闻呈现，保留。

**复校结论：第二轮完整复校零问题。** 修正后全文实测 41,362 字符，练习仍为 149 题（编号与答案未动），完整版 PDF 24.5 MB、web 版 4.18 MB，构建零警告。本期通过 SOP 校对门，定稿。

## 十一、PATCH 记录（2026-10-21，定稿后几何审计缺陷修复）

来源：全计划几何遮挡审计（`hidden_files/occlusion-audit-2026-10-21.md` 缺陷 #8），在本期定稿并投递后发现。

**缺陷**：第 1 版右栏 « SEARCHES OF THE WEEK » 热搜图下方注释行（中文讲解层家具行）
« “hot dog recall” 周一快照搜索量 200K+（见第 2 版）。»（SVG 单节点 x=1473、y=1266、字号 19）。
以生产字体实测（PIL ImageFont、Noto Sans CJK SC，与构建 `svglib` 同法）：行宽 **488.05 px**，
自 x=1473 起右端至 **x≈1961.05**，超出页面右缘（1950）**11.05 px**，并穿过双层版框（内框线 x=1885）；
末字 « 。» 占宽 19 px，仅约 8 px 落在页内，成图上只剩一丝。修复前已截取 P1 右缘放大图目视确认
（末字被页缘裁切），与审计结论一致。该行是源码中的裸 `p.text` 调用，不经流式排版，
故构建日志的 FLOW OVERFLOW / HEAD TOO WIDE 检查覆盖不到它，前两轮均未报。

**出处说明（如实）**：第九节构建者保留提示与第十节标记保留中关于 P1 热搜图注释行
「抵到版框、末字完整未裁」的判断，系据成图肉眼判定；本次以字体精确量测复核，该判断对本行不成立，
特此更正并以本节为准。

**修正**（仅 `hidden_files/weekly-report-en-build/content12.py` 第 83 行一行，中文家具措辞微缩，
英文正文与一切事实不动）：

- 修正前：`“hot dog recall” 周一快照搜索量 200K+（见第 2 版）。`
- 修正后：`“hot dog recall” 周一快照 200K+ 见第 2 版。`
- 措辞变动逐项：删 « 搜索量 » 三字（200K+ 在热搜图语境下即搜索量，语义无损）；« （见第 2 版）»
  的全角括号改为一个空格。保留信息全部在：检索词、周一、快照、200K+、指向第 2 版。
- 修正后实测行宽 **397.30 px**，右端 x=1870.30，距内框线 14.7 px、距页缘 79.7 px。

**改动范围**：整期按第八节配方重渲染。哈希比对：仅 `svg/p1-front.svg` 与 `cards/p1-front.png`
变化；第 2–8 版 SVG 与 PNG **逐字节不变**；两份 PDF 因内嵌第 1 版而重新生成。

**验证**：

- 登记表 REG 修复前后 JSON 全等：**149 题，编号、等级、答案、简析逐项未动**。
- 构建日志 FLOW OVERFLOW / HEAD TOO WIDE 警告 **0** 条。
- 按审计同法对全 8 版做几何复扫（文字节点字框 × 后绘不透明图形覆盖 ≥30%／字框侵入页脚带
  y=2580 以下（标准页脚行除外）／字框越出页缘）：**0 标记**。
- 8 张整版 PNG 全部复看图无异常；P1 右缘放大图复核：注释行完整落在版框内，末字 « 。» 完整可见。
- 可见文字量（XML itertext 同口径）：41,362 → **41,358**（净 −4 字：删 5 字、增 1 空格）。

**最终体量**：完整版 PDF 24,496,906 字节（24.5 MB）；web 版 PDF **4,184,520 字节（4.18 MB < 10 MB）**。
本 PATCH 未向 Discord 重新投递（投递由上级步骤决定）。
