# 校对笔记 — 2026-W47-ja-nl（第一轮独立复校，叶子）

- 版：`2026-w47-ja-nl`（目标语日语 × 读者母语荷兰语，VOL.4，刊期 2026-11-16–22）
- 校对员：叶子（第一轮独立复校，与 builder / 核心 builder / 各轮复校员不同人）
- 日期：2026-11-11（UTC 07:41–08:05）
- 结论：**(b) 缺陷清单 — 3 条缺陷（D1 中、D2 高、D3 高），不得按零问题定稿。**
- 红线遵守：只读了 `production/2026-w47/fanout-ja/2026-w47-ja-nl/` 与 `core-ja/`（比对用）；
  未碰 core-ja、W43–W46、其他目标语家庭、`tools/`；未跑 insert.py、lint --write；
  未 git add/commit/push/reset/stash、未改任何源码/成品。run.py 两遍重跑为任务要求的机械门，
  重跑前后 8 SVG 哈希逐字节一致（见 GATE-LOG.md），成品无改动。
- 依据：SOP.md §8 / §1.1 全文、`WEEKLY-KIT.md`、`EDITION-RECORD.md`、
  `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md`（在盘，已读；第 8 棒重建、只含第 8 棒实测）。
- 方法：印刷 PDF 重新渲染 8 页逐页目视（110 dpi 全页 + 200–220 dpi 局部放大，见 `render/`）；
  网页 PDF P1/P8 目视 + P2 词条区放大；`2026-w47-ja-nl.text.md` 1379 行全文通读；
  150 题逐题验算（题干—正文—答案键三方核对）；金句 8 条逐字比对；
  P8 全部注文人名人工逐条核对公开来源（见 D2/D3）；机械门全套自跑（见 GATE-LOG.md）。

## 身份核对（先核身份，通过）

| PDF | 字节 | SHA-256（完整） | 与 KIT 登记 |
|---|---|---|---|
| 印刷 `Lucerna-VOL4-JA-NL.pdf` | 29,099,171 | `c18c551af2249561000dd50821d4e9646597c5a2cdccf316b02ee38128d40a19` | 逐字一致 |
| 网页 `Lucerna-VOL4-JA-NL-web.pdf` | 4,476,557 | `e0678a4b892ff07080d48a51b2f8b7c9ee109916752df537849000370ad9cb81` | 逐字一致 |

双 PDF 各 8 页。身份相符后方动手。

## 缺陷清单

### D1（中）— P2「11月のことば」：两条荷兰语释义溢出词框

- **页/位置**：P2 下部「11月のことば Novemberwoorden」词条框，第 1 格「熊手（くまで）」与第 4 格「小雪（しょうせつ）」。
- **原文（现状）**：第 1 格荷兰语释义折成两行
  `een bamboe hark voor voorspoedige / zaken`；第 4 格折成两行
  `wanneer er een beetje sneeuw begint te / vallen`。
  词框为固定高：`y=1618`、`h=150`（底缘 y=1768，SVG px）；第二行基线 y=1776.76，
  墨迹底约 1782.8——整行悬在框外，落在框下空白处，与下一行
  「文で覚えましょう：『19日に、浅草で熊手を買います。』」（基线 y=1800）几乎相接（约 1px 间隙）。
  另两格（手締め `vieren met geklap`、解禁 `de dag dat de verkoop begint`）为一行，在框内。
- **应为**：释义须收进框内——缩短两条荷兰语释义至一行，或按 P2/P3/P5「Jouw beurt」盒的先例
  （核心 243.5/274.0 → nl 加高至 272.5/303.0）加高词框。
- **证据**：
  - SVG 坐标（`svg/p2-kurashi.svg`）：4 格词框同为 y=1618/h=150；两行释义第二行基线均为 1776.76，
    第一行基线 1752.06 在框内。
  - 印刷 PDF 与网页 PDF 200 dpi 放大渲染（`render/p2-words2.png`、`render/web-p2-words2.png`）均可见
    `zaken`、`vallen` 印在米色框之外。
  - 对照：核心及 ja 其余 9 版（en/de/fr/es/it/pt/ru/ko/zh-tw）该 4 条释义均为一行、基线 1752.06，
    在框内——属 nl 独有 fan-out 溢出（荷兰语释义长于核心中文释义所致）。
  - 几何审计 0 旗**未覆盖**此类缺陷：溢出文字未被后绘不透明元素遮盖（COVER 不触发），
    未压线、未侵页脚带，故机械门漏检；系目视查出。
- **严重度**：中。文字可读、无字形重叠；但属肉眼可见的版式缺陷（字跑出底色框外），读者一眼可见。

### D2（高）— P8 答案注文：藤凌駕罗马字拼错，5 处

- **页/位置**：P8「答え Antwoorden」注文：第 49、54、63、111、116 条。
- **原文（现状）**：`Fujiryūga`（5 处：49 `Fujiryūga versloeg Hōshōryū op dag 3`；
  54 `Kinboshi van Fujiryūga: 11e toernooi sinds debuut`；
  63 `Fujiryūga won een kinboshi op dag 3`；111 同 54；116 `Hōshōryū verloor op dag 3 van Fujiryūga`）。
- **应为**：`Fujiryōga`（凌读 りょう，非 りゅう）。
- **证据**：公开来源一致——スポーツ報知 2026-11-11：
  「藤凌駕 雅治（ふじりょうが・まさはる）」；日刊スポーツ 2025-10-01：
  「藤凌駕（ふじりょうが、22＝藤島）」。同家庭 en/de/fr/es/pt 五版 P8 注文均为 `Fujiryōga`。
  注文事实本身正确（3 日目战胜豊昇龍得首个金星、初土俵起第 11 个场所），只拼写错。
  双 PDF 文字层中 `Fujiryūga` 各 5×，正确拼写 0×——缺陷在交付成品中，不只在源码。
- **严重度**：高。语言学习报纸把错误罗马字教给读者；且同一错误出现 5 次。

### D3（高）— P8 答案注文：美ノ海罗马字拼错，1 处

- **页/位置**：P8「答え Antwoorden」注文：第 48 条。
- **原文（现状）**：`48. B — Umi-no-umi verloor op dag 1 van Hōshōryū`。
- **应为**：`Chura-no-umi`（美读 ちゅら，非 うみ）。
- **证据**：公开来源一致——日刊スポーツ 2018-06-25：「改名したしこ名『美ノ海（ちゅらのうみ）』」；
  日刊スポーツ 2018-05-30：「美ノ海（ちゅらのうみ、25＝木瀬）」；
  「美」取冲绳方言“美丽”（ちゅら）之意。同家庭 fr/es/pt 版注文均为 `Chura-no-umi`
 （en `Churanōmi`、de `Churanoumi`，均为正确读法的不同连写）。
  注文事实本身正确（初日败给豊昇龍），只拼写错。
  双 PDF 文字层中 `Umi-no-umi` 各 1×，正确拼写 0×。
- **严重度**：高。同 D2。

## 已核实无问题的要点（抽样以外的全量结论）

- **150 题逐题验算**：编号 1–150 连续无缺重；分版 10/18/18/18/18/18/12/38；
  级别 A2 48 / B1 73 / B2 29（与 KIT 一致，run.py 注册表复核）；
  题型 zinnen aanvullen 50 / meerkeuze 51 / combineren 12 / zinnen bouwen 8 /
  waar of onwaar 11 / gatentekst 13 / vertalen 4 / Schrijven 1。
  全部 150 条答案键逐条对照题干与正文/图表验算无误（含图表算术 38−24=14、38+24=62、
  38+24+22+16=100；日期星期：11 月 19 日周四、11 月 8 日周日、11 月 22 日周日、
  11 月 5 日周四、12 月 1 日周二均与 2026 年日历及公开报道一致；相扑 3 日战绩与
  日刊スポーツ/スポーツ報知/デイリー报道一致）。
  范文（H 部例文）去空格计 154 字符，与注文“154 tekens”相符。
  练习小节头一律日语（A 理解、B ことば、C 数字と日付、C 文を作りましょう、
  D ペアにしましょう、D 正しい・正しくない、B グラフ、C 数字と事実、
  D 文を完成しましょう、B 一般問題），无 tr-en 式英译残留。
  题型标签均为荷兰文（Vul in / meerkeuze / gatentekst / Koppelen / Bouw een zin /
  Waar of niet waar? / Vertaal / Schrijven）。
- **E 组 137–140**：答案键确已译成荷兰文，逐条核实正确：
  137 `Ni-no-tori is 19 november.`（二の酉は11月19日です）；
  138 `De nieuwe wijn komt uit op 19 november.`（新酒は11月19日に解禁されます）；
  139 `De nominaties voor het modewoord zijn bekendgemaakt op 5 november.`
  （流行語のノミネートは、11月5日に発表されました）；
  140 `Wie herfstbladeren gaat bekijken, moet voorspelde data en huidige stand controleren.`
  （紅葉を見に行く人は、予報の日付と今の様子を確かめましょう）。
  p8 compare keydiff 恰为 [137, 138, 139, 140]，预期内。
- **金句 8 条**：逐字比对正文——7 条逐字出自 P1–P4 新闻正文且页码引用准确（见观察项 O1 论第 6 条）；
  荷兰语译文 8 条均准确（`ryuuryuu`、`Chiikawa` 如裁定；`hanendagen` = 酉の日，准确）。
- **讲解/界面语言**：确为荷兰文（页脚 `JAPANS WEEKBLAD VOL.4 Japanse tekst Uitleg in het Nederlands`、
  页码行 `Pagina N van 8`、各栏荷兰文标题/注释/披露/预告/答案注文）。荷兰语通读无硬伤（见 O2 两处小疵）。
- **CJK/源语字面量转写**：核心日文原文逐字节冻结（与 core-ja 比对：8 句金句、P1–P6 正文、
  练习题干日文部分一致）；`りくりゅう` 罗马字 `ryuuryuu`（P7 金句译文、P8 注 66/77/80/105）；
  `ちいかわ` 译 `Chiikawa`，无中文名 `吉伊卡哇`。
- **中文残留**：0。标记词 `吉伊卡哇`/`参考答案`/`酉之市`/`提名`/`说说你自己`/`每周一期`/
  `日语周报` 在 SVG + text.md + content*.py 全 0×；
  以“们/这/那/就/都/还/没/很/能/会/让/给/说/的/是/在/了/吗/呢/吧/啊/对/为/从/过/得”
  扫 text.md 得 25 行，逐行核实均为日语固有词（京都、会社、会場等）。有意保留的中文原文引用：无。
- **U+2019**：8 SVG + text.md + content*.py 全 0×。撇号均为直撇号 U+0027
  （如 P7 `Drie niveaus, drie thema's`），渲染正常，无宽字形断裂。
- **VOL**：期号 VOL.4 全版一致（页脚、刊头、目录）；VOL.3 仅 1×（P4 前号注，正确）；
  VOL.5 共 4×（见 O4），均为合法下期预告，无错印。
- **图片来源**：5 图署名与 `assets/CREDITS.md` 一致
  （P1 maple — Poliphilo CC0；P3 beaujolais — Alainauzas 公共领域；
  P5/P8 Arashiyama — lumoplank CC0；P7 tori — Mozzucu CC0，注“2025年11月24日照片”）；
  P4 无图如 KIT 所述。
- **禁词**：国际政治类扫描 0 命中（ウクライナ/乌克兰/戦争/战争/ガザ/プーチン/トランプ/
  ミサイル/核兵器/台湾问题/南シナ海）。
- **P8 人名逐条核对（公开来源）**：Yoshinofuji ✓（義ノ富士，小结，初日胜大の里，属实；
  其罗马字为自然读法 よしのふじ）；Ōnosato ✓；Hōshōryū ✓；
  Miura Riku / Kihara Ryuichi ✓（三浦璃来/木原龍一，花滑搭档）；
  Fujiryūga ✗（→ Fujiryōga，D2）；Umi-no-umi ✗（→ Chura-no-umi，D3）。
  其余 P8 注文人名/机构名：Weathernews ✓、Beaujolais Nouveau ✓、Tokio（荷兰语拼法）✓、
  Fukuoka Kokusai Center ✓、Kyushu-toernooi ✓。

## 观察项（不计缺陷）

- **O1 — 金句第 6 条出处**：「『りくりゅう』は、フィギュアスケートのペアです。」
  逐字出处仅为 P7 自身 B1 栏（「流行語のことばを覚えましょう。『りくりゅう』は、
  フィギュアスケートのペアです。……」），P5 课文相应句为
  「フィギュアスケートのペア、三浦璃来選手と木原龍一選手のことです。」（句式不同）。
  其余 7 条逐字出自 P1–P4 新闻正文（#1/#2 P1、#3/#8 P2、#4 P3、#5 P4、#7 P1）。
  第 6 条引注 (p. 7) 属实；该句为冻结核心文本，改动与否须核心层定夺，故列观察不计缺陷。
- **O2 — 两处荷兰语小疵（意思可懂）**：P8 注 55/112
  `De 7e snelste kinboshi sinds de zes toernooien per jaar`——`sinds` 后宜接时间点/事件，
  更顺为 `sinds er zes toernooien per jaar zijn`；注 86
  `Weervoorspelling Japan: Arashiyama vanaf 13 nov.` 为电报体简写。均为答案注简写体，不影响理解。
- **O3 — 核心继承的版面现象（非 fan-out 缺陷）**：P1 趋势盒第 1 条末字「敗」单独换行；
  P4 栏顶「5) でお知らせします。」跨栏续接；P2/P3/P6 栏中大面积留白；
  P8 栏头徽章顶缘 y=180 与深绿栏条底缘 y=182 有 2px 交叠（徽章后绘盖住栏条，视觉为相接，
  与 core-ja 几何逐值一致）。
- **O4 — KIT 的 VOL.5 计数不准（非成品缺陷）**：KIT §1 称 VOL.5 出现 3×，
  实测 4×——P4 正文「次号（VOL.5）」1×、P4 底栏横幅「次号（VOL.5）」1×、
  P7 读者园地披露 1×、P7 下期预告头 (VOL.5) 1×。其中 P4 正文一处分属两个文本节点
  （`次号（VOL.` + `5）でお知らせします。`），故字串 grep 只命中 3×。四处均为合法下期预告，无错印。
- **O5 — 核心注 47 的汉字笔误（nl 本身不受影响）**：core-ja P8 注 47 中文写“一之富士”，
  与正文及公开报道“義ノ富士”不符；nl 版注文用罗马字 `Yoshinofuji`，与正文一致、正确。
  请协调员知会核心线，nl 无需因此改动。
- **O6 — 与任务备忘的出入（实测为准）**：备忘称 en/de/fr/es 五版 P8 注文“均中”同类拼错；
  实测盘上 en/de/fr/es/pt 四版 SVG 均为正确拼写 `Fujiryōga` / `Chura-no-umi`
  （en 用无连字符 `Churanōmi`、de 用 `Churanoumi`），de/fr/es/pt 的 text.md 亦同。
  it 版 SVG 亦正确，但其 text.md 仍为旧拼写（导出件滞后于 SVG）。
  盘上唯一交付 SVG 仍带两处错拼的是 nl 版（D2/D3）。此点特此说明，备忘所述与盘上实测不符。
- **O7 — FANOUT-REPORT-ja.md**：文件在盘（`hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md`），
  已读；其为第 8 棒重建、只含第 8 棒实测，前棒章节缺失（文件自述）。不影响本次校对。
- **O8 — 工作树既有修改与本次无关**：`git status` 显示 `issues/2026-w43/` 下有已修改的已跟踪文件，
  其 mtime 为 2026-11-10 17:44 UTC，早于本次开工（11-11 07:41 UTC）；本次未碰仓内其他目录。
  run.py 两遍重跑前后 8 SVG 哈希 8/8 一致，未改任何成品。

## 证据文件（本轮校对，写在仓外 scratch）

`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ja-nl1/`
- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`
- `proof-run1.log`、`proof-run2.log`（run.py 两遍）、`svg-sha-pre.txt`、`svg-sha-run1.txt`、`svg-sha-run2.txt`
- `proof-occlusion.json`、`proof-occlusion.log`、`proof-p8.json`、`proof-p8compare.json`
- `proof-print.txt`、`proof-web.txt`（pdftotext，各 45,989 B，逐字节一致）
- `render/p1.png`–`render/p8.png`（印刷 PDF 重新渲染）、`render/web-p1.png`、`render/web-p8.png`、
  `render/p2-words2.png`、`render/web-p2-words2.png`（D1 放大证据）、
  `render/p2-jouw.png`、`render/p3-jouw.png`、`render/p5-jouw.png`（Jouw beurt 盒在框内）、
  `render/p8-head.png`、`render/p8-q124.png`、`render/p8-key124.png`
