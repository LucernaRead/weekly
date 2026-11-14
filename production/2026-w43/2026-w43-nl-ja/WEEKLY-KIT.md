# WEEKLY-KIT — NL×JA（オランダ語本文 · 日本語解説）W43 VOL.1

- **版面**: De Lucerna VOL.1 · 2026-10-19–25 · 目标语 = 荷兰语（オランダ語）、讲解语 = 日语（日本語）
- **状态**: **PASS**（独立校对一轮零缺陷、零修复，见 §7——由主线另派）
- **建造**: 2026-10-22 · build 目录 `hidden_files/weekly-report-nl-ja-build/`（核心 `hidden_files/weekly-report-nl-build/` 的副本，OUT 改道至本目录；核心全程未动，收尾 freeze baseline 复核 8/8 逐字节未变）
- **总量**: 150 题 = A2 42 · B1 76 · B2 32（逐页 10/18/18/18/18/18/12/38，与核心同）；范文 87 词

## §1 出货针脚（实测）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| De-Lucerna-VOL1-JA.pdf（印刷） | 17,268,607 | f0e5545b6162fc03a44c42d4abea1c7a58a30395831fedf9c72ec9f10a9d8d27 |
| De-Lucerna-VOL1-JA-web.pdf（网页） | 3,247,158（< 10 MB ✓） | 205b8050a49ba6dd3b90f655002bccba33c0ecb077ca758872917d92055936c9 |
| svg/ ×8 · cards/ ×8 PNG | — | 渲染自同一轮单进程 run.py + render.py |

## §2 方法

1. `freeze.py baseline` 先行:核心 8/8 SVG 逐字节复现后才动工（sha 前缀 p1 a8a2cc5d · p2 ea3f2a18 · p3 b61fbb1b · p4 eff31458 · p5 1098c657 · p6 c941eb44 · p7 097fcfa7 · p8 feba8026）。
2. **svglib = 日语核心版**,md5 `d73e23b365676c3618d7e060b835eb4d`（自 weekly-report-ja-build 复制并验 md5;与 NL 版差异恰为标准 3 处:JP 字面选择、kinsoku 追い出し + SEAM_SLACK=28、字族名）。全部日语讲解流经此版换行。
3. 变换:AST 定点清点 content12/34/56/7/8 + bslib4 中 **260 条互异 CJK 串** → 256 条译日 + 4 条 KEEP → **486 处替换**,集合等式断言通过（未映射 = 0、多余键 = 0）。`bridge()` 改名 `expl()`（bslib4 定义 + 22 调用点）。
4. **KEEP 集**（语言中立语法记号、逐字节保留）:`slapen：iedereen → slaapt`、`perfectum：heeft gewonnen`、`tellen：het onderzoek → telt`、`perfectum：heb geslapen`。另有 13 条注册表注与核心逐字节同,全为公式/箭头类语言中立项（见 §4）。
5. P1 徽章位置:占用核心 y=372 荷语标语槽（19.5pt 粗体 BRICK 居中）——EN×JA §6 先例 + 本会话查实 en/es/it-ja 出货 SVG 均为替换该槽,de-ja 同;被移除的荷语标语行在 freeze diff 中登记为家具归因（见 §4）,非冻结违规。

## §3 家具（如建，JA 列定式 · 目标名 オランダ語）

| 部位 | 本版 |
|---|---|
| P1 徽章（y=372 标语槽） | «オランダ語テキスト · 日本語の解説 — 日本語読者のための版» |
| 页脚左（每页） | «De Lucerna · オランダ語週刊 VOL.1 · 本文はオランダ語 · 解説は日本語» |
| 页码（每页右） | «N ページ（全 8 ページ）» |
| P1 顶栏中 | «ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む» |
| P1 花体行 | «オ ラ ン ダ 語 週 刊 · VOL.1 · DE KLOK GAAT TERUG · HERFSTVAKANTIE · ADE WORDT 30»（40pt 同核心） |
| P1 头条带右 | 日曜、時計を戻す / 冬時間スタート · 詳しくは2ページ |
| gloss 前缀 | «解説 — »（单层） |
| 文法前缀（P8 #139 注等） | «文法ポイント — » 口径以注册表注为准 |
| 章节头 | 荷语原题 · 日语短题（如 «HET NIEUWS · トップニュース»«DE WEEK IN CIJFERS · 数字で見る今週»«VERDIEPING · 深掘り»） |
| 练习导语行 | «答えは8ページ · 問題はレベル混合、番号で探してください»式 |
| 题型标签映射（注册表实测,计数与核心 1:1） | 単選→選択問題 45 · 完成句子→文の完成 66 · 完形単選→穴埋め選択 13 · 词汇配对→単語のペア 8 · 造句→文を作る 7 · 判断対错→正誤判断 6 · 翻訳→翻訳 4 · 写作→作文 1 |
| 指令映射 | 填空→空所補充 · 判断→正誤 · 把词和释义配对→語と意味を結ぶ · 造句→文を作る |
| P8 顶栏 | «TOETS EN ANTWOORDEN · テストと解答»；副行 «8ページ · De grote toets van de week + alle antwoorden» |
| P8 解答头 | «ANTWOORDEN · 全解答と解説（1–8ページ）»；右注 «各問に日本語の解説つき · ✓ は模範文のある問題» |
| P8 分隔 | «— N ページ —»（1–8） |
| P8 式样 | 短横式 `N. key — note`,作文题 `N. ✓ note`（NL 家族口径,核心印刷全 150 注、无阈值规则;本版显式同集） |
| P7 金句 | 荷语引文逐字冻结 + 日译 + (Pagina N) 标签逐条同核心（8 条） |

## §4 机械门（全跑,实测值）

- **freeze.py diff**（终版 `tools/scratch/nl-ja-diff-final.json`）:逐页增删 p1 +28/−25 · p2 +37/−33 · p3 +31/−27 · p4 +29/−29 · p5 +39/−38 · p6 +33/−32 · p7 +40/−39 · p8 +171/−168;added CJK 合计 **2,739 字**,全数归因日语讲解层。荷语正文归因闭合:①非 CJK 移除仅 P1 荷语标语行 1 条（徽章替换,§2.5）;②非 CJK 增删对全为重排对——P3 词库行、P4/P5/P6 署名行（见 §6 的 «·» 度量说明）;③混合串（荷语+讲解）移除侧逐条有日语对应串、荷语部分逐字保留;④移除侧纯 CJK 串全属核心讲解层（家具/注/gloss/导语）。归因明细留档 `tools/scratch/nl-ja-attribution.txt`。
- **印刷注释集**:`p8.py extract` 核心 P8 = 150/150（核心印全注、无阈值）;本版同集。`p8.py compare` = **CLEAN,noted 150 = 150,missing = []、extra = 0**。
- **键差异（注册表逐项比对,权威口径）**:恰 **{137, 138, 150}**——137/138 翻译题键中译日（«日曜日は時計を戻す：1時間長く眠れる！»/«あなたの電話とコンピュータは時刻を自分で変える。»）,#150 作文装置键（«（自由記述 — 模範文は以下）»）。题干改向 {139, 140}（题干译日、键荷语冻结）。其余 147 键与核心逐字节同。
- **p8.py keydiff 伪影证伪（README 第 13 条）**:compare 另报 18 项 keydiff（5, 11, 19, 20, 24, 33, 35, 66, 70, 71, 73, 74, 78, 82, 83, 94, 109, 127）,逐项以 p8.extract 内部值复核:皆为注含全角括号触发 paren 分支、把「键 — 注首段」误作键;18 项印刷键（首个 ` — ` 前段）与核心逐字节同（如 #5 dertig、#24 2.500、#94 zoekopdracht）,#33 仅解析分支 dash→paren 翻转、键 'A' 同。注集门 CLEAN 不受影响。
- **注差异**:150 注中 137 条译日;13 条与核心逐字节同,全为语言中立项:#6/#59/#97/#140 语法箭头与 KEEP 集、#12/#16/#18/#46/#79/#84/#101/#102/#120 公式与时刻等式（03:00 → 02:00、kwart over twee = 2:15、301.000 + 246.000 = 547.000 等）。
- **occlusion_audit.py**（自检先行通过）:**NEW vs core = 0**。残余 2 旗为核心自有冻结荷语事实行（P2 'adviesdata…'、P3 'Kaartjes…' 各越界 0.7px,核心同旗）,非本版缺陷、不动。
- **同行墨迹扫描（README 第 10 条,自写 scratch/scans.py）**:同基线碰撞 = **0**。
- **行首禁则扫描**:初测 1 命中（P7 B2 bridge「ま|ったく」小假名行首）→ 改写措辞移折点后 = **0**（见 §5）。
- **拉丁词断词扫描**:候选 8 例全为完整词间折行（Week|in、de|wintertijd、Dutch|Design、het|materiaal、de|kastanje、de|speelronde、per|inwoner、in|Eindhoven,两侧皆完整词）→ 词中劈开 = **0**。
- **图表元素级（README 第 12 条）**:P6 柱条几何与核心逐字节同（x=1473 起,宽 250/204/50/5、高 18、y=304/362/420/478）;标签/值（«wintertijd» 301.000 · «klok verzetten» 246.000 · «...klok achteruit?» 60.500 · «...klok vooruit?» 6.600）同位同文、未被覆盖;荷语图注 3 行同,来源行译日 2 行同位（«出典：Wristler の調査、2026年10月20日発表；データは昨年10月の検索回数»）。
- **gloss 逐条点数**:核心 26 条（P2 6 · P3 5 · P4 5 · P5 5 · P6 5）= 本版 **26 条**,逐个调用点 1:1;P1 词表 3 条 = 3 条。
- **日历（Europe/Amsterdam,`date` 实测）**:2026-10-19 周一 · 10-24 周六（DDW 免费家庭日 Venlo）· 10-25 周日（wintertijd 03:00→02:00 + PSV–Feyenoord topper 14:30）· 11-01 周日（Expeditie Robinson 20:00 RTL 4 · VOL.2 预告）——与正文/练习/答案三方一致。
- **残留语全扫（8 SVG）**:简体专有码点（严格判别集:语读页练见词选们这么发长热买卖书让认讲诉谁谢请边还进远达过时钟…）= **0**;西里尔 = **0**;中文家具串（译注/讲解/荷兰语周报/范文/答案见）= **0**。命中之汉字（数・戻・埋・合・意・方・属・名・学・域・句・向・国・料等）全为日语同码点正用字（戻す・穴埋め・従属節・学校・無料…）,逐条裁定为日语固有表记。
- **禁用术语**:页面 SVG 与 operative code 中该词 = 0;`bridge`→`expl` 改名已落地（方法名/调用点全量）。例外披露:build 内 `scratch/` 的 transform/site_edits 脚本以核心原串作检索模式而引用该词,confined 于 scratch,不入页面与本 KIT 正文。
- **构建日志**:单进程 run.py,零 `!!` 警告（无 FLOW OVERFLOW / HEAD TOO WIDE）;各 flow 终点均在版芯内（最紧 P3 练习终点 y=2555 / 版芯 2580,余量 25px,审计无旗）。

## §5 自校缺陷与修复（建造者一轮全量自校）

1. **首轮变换损坏文件**:AST 的 col_offset 是 UTF-8 **字节**偏移,按字符行拼接致串错位。当即弃毁、从核心重拷、改按 UTF-8 编码行拼接后重跑,486 处替换 + 语法检查全过。（教训:AST 定点拼接须以字节行操作——建议主线回写 tools/README。）
2. **P1 两行日语出框（occlusion BOXTITLE NEW 旗）**:TOPZOEK 框副题 «オランダ人はGoogleで何を検索 · zoeken op Google» 右墨 1921.5 > 边 1885;快照行 «10月20日（火）のGoogleトレンド：数字は推定値» 右墨 1901 > 1885。均为讲解层自有文字——按 README 第 15 条改短:副题→«オランダ人のGoogle検索 · zoeken op Google»,快照行删「数字は」→«10月20日（火）のGoogleトレンド：推定値»。重渲染后 NEW 旗 = 0。
3. **P7 B2 bridge 禁则命中**:«まったく» 被折成「ま|ったく」（小假名行首,JA svglib 追い出し不覆盖此类,同 EN×JA §3.2 先例）。以 wrap() 实测 4 个候选后采用 «slaat nergens op は「まったく道理なし」の口語、使用は慎重に；…»——折点移至「まったく」整词后、仍 3 行、版式位移 = 0。复扫禁则 = 0。
4. **P7 读者信框底越线（几何复核发现,审计未覆盖的类）**:日语信下注比中文多 1 行,信框底 1707.5 越过全宽金线（y=1698）9.5px（核心框底 1678.5,在线之上 19.5px;无文字被盖,故 occlusion 无旗——靠逐框几何比对核心发现）。改短注文（wrap() 实测取 2 行候选）:«編集部の例文で、手紙ではありません。VOL.2 に本物の手紙と優秀作文を掲載！»——两项声明与 VOL.2 两项承诺全保留,框底回到 **1678.5 = 核心逐值**。
5. **视觉自校（8 卡逐张肉眼）**:日文字形渲染正常、无缺字/方框;徽章显著、每页页脚配对标签齐;P6 图表与来源行、P7 金句 8 条 + 页标签、P8 日语键 #137/#138 与 ✓ 行 #150 均如设计。答案抽查从荷语正文重推（#113 B · #121 A · #129 B · #145 B · #146 A 等）与印刷键一致。

## §6 给校对者的注记

- **«·» 度量重排（预期现象,勿报冻结违规）**:«·»(U+00B7) 在 SC 字面宽 19.0、JP 字面宽 10.66（两版 svglib 实测）→ 核心中折 2 行的署名行（«Van de redactie van De Lucerna · Leesniveau: B2» 434.5 > 栏宽 434）在本版合为 1 行（426.2）,其后 flow 整体上移 24.7px（19pt × 1.3）;P6 因此出现整块换栏（gloss 框落点 核心第 3 栏顶 → 本版第 2 栏 y=1341）。荷语段落折行在两版逐行同宽（栏宽恒 434）,freeze diff 已证每页荷语文本多重集全等——同 EN×JA §6(b)「相邻重排」裁定口径。
- **flow 终点差**（对核心）:P2 特稿 +30、P3 练习 +148（终点 2555,余量 25)、P7 col3 ±0（信框修复后终点 1678.5 与核心逐值同,见 §5.4)、P8 键列 +15（终点 2458 / 2552）——均在版芯内、审计零新旗。
- 讲解层无国际政治引入;内容红线同核心。
- 本 KIT 状态 **PENDING**:待独立校对（日语母语级通读 + 逐题重推）后由主线置 FINAL 并入仓。本建造未入仓、未发 Discord。

## §7 独立校对记录（2026-10-22，校对者独立复跑/复测，未采信建造者自报）

**结论：PASS — 完整一轮零缺陷、零修复，无重渲染。** 校对工件：`hidden_files/proof-nl-ja/`（双 build 副本、注册表 dump、items 全量导出、scans）。

- **freeze**：`freeze.py baseline` 核心 8/8 逐字节（哈希与 §2 登记全合）；另将核心与本版两 build 各复制改道后单进程重跑，出货 SVG 双方均 8/8 逐字节复现（确定性自证），核心零触碰。
- **freeze diff 分账**：added CJK 恰 **2,739** 字全归因日语讲解层；非 CJK 增删逐页闭合——P1 仅荷语标语行被徽章替换（§2.5 先例）、P3 词表行重分行、P4/P5/P6 署名行 «·» 度量合行（§6 口径逐值复现）、P7 非 CJK 差异 = **0**、P8 分隔行替换 + «Eindhoven»/«___» 折行碎片（印刷键直查证明内容全等）。荷语 token 多重集逐页比对：差异全为家具替换/讲解层引述/标点邻接伪影。P7 8 金句荷语引文逐字 = 核心，页标签分布 {1:1, 2:2, 3:1, 4:1, 5:1, 6:2} 全等。
- **注册表逐字节比对**（双副本各一进程独立导出）：150 = 150，level/page 分布全等，题型 zh→ja 1:1 映射计数逐类全同；**键差异恰 {137, 138, 150}** 与 §4 登记逐字合；题干改向 {139, 140} 代码级确证（键荷语冻结、题面译日忠实）；注 137 译日、13 条未变 {6, 12, 16, 18, 46, 59, 79, 84, 97, 101, 102, 120, 140} 逐条为公式/箭头/语法记号类语言中立项，裁定成立；范文实数 **87 词**（80–100 区间）。
- **手工重推导**：自核心荷语正文逐题重推全部 **150 键，零分歧**（含 #46 票价 19,50+19,50+32,50=71,50、#84 301+246=547、#85 750−547=203、#87 60.500÷6.600≈9、两组配对映射、对话完形 #145–149、翻译 #137–140 双向核）。
- **p8.py**：独立 extract 核心印刷集 = 150；compare **CLEAN 150=150**（missing=[]、extra=0）。compare 所报 20 项 keydiff 中 18 项逐项以印刷行直查证伪（README 第 13 条）：18 项印刷键首段（首个 « — » 前）与核心逐字节同（dertig/B/drie uur/achteruit/2.500/A/thema/C/artiesten/locaties/kandidaten/avontuur/gaat winnen/Waar/301.000/zoekopdracht/ruzie/B），#33 为 dash→paren 分支翻转伪影；余 2 项 {137, 138} 为真实翻译键。150 项印刷键段与双注册表逐项全合。P8 式样短横式 «N. key — note»、«150. ✓ …» 在版实证。
- **遮挡审计**：`occlusion_audit.py`（自检先行通过）本版 2 旗 = 核心同 2 旗，**NEW vs core = 0**：P2 «adviesdata…»、P3 «Kaartjes…» 两条冻结荷语行与核心同串同坐标（x/y/字号逐值同，仅字面名 JP/SC 之别、拉丁度量一致），底墨越界各 0.7px 与核心同值——冻结元素继承，非本版缺陷（README 第 15 条界内）。
- **同行扫描**（README 第 10 条，参考实现复跑）：本版 7 处 gap=4.0 与核心逐值相同，全为 P1 目录行 «Pag. N» 与标题的设计间距（无重叠），NEW = 0；P1 顶带三段净空正常。
- **图表兜底**（第 12 条）：P6 四柱几何与核心逐字节同（x=1473、宽 250/204/50/5、高 18、y=304/362/420/478），标签/值/图注同位同文，覆盖 0%。
- **JA 列定式验收**：§3 家具逐项在版且逐字合——徽章 (975, 372) 19.5pt 居中 ×1、页脚 ×8 全同登记串、页码 «N ページ（全 8 ページ）» 1–8 对位、顶带含 «毎週一号»、花体行逐字合、P8 头 «ANTWOORDEN · 全解答と解説（1–8ページ）»、分隔 «— N ページ —» ×8、gloss «解説 — » 单层（双前缀 = 0）；目标名 オランダ語 与名表一致。核心注册表无语法点注，故 «文法ポイント — » 本版 0 次与核心口径一致（§3 登记语「以注册表注为准」）。
- **svglib/双扫**：build svglib.py md5 实测 = `d73e23b365676c3618d7e060b835eb4d` 与日语核心逐字节同；行首禁则全册逐行 = **0**；拉丁断词（假名承载行口径）候选 25 条逐条裁定为完整词间折行或异块相邻，**词中劈开 = 0**（含建造者 8 候选逐条复核）；§5.3 禁则修复行在版实证（«まったく» 整词居行末、次行首 «道理なし»、仍 3 行）。
- **建造者修复复核**：§5.2 两条改短串在版（«オランダ人のGoogle検索 · zoeken op Google»、«10月20日（火）のGoogleトレンド：推定値»），BOXTITLE NEW = 0；§5.4 信框底——P7 rect 底边集 1550–1800 段内本版与核心同为唯一值 **1678.5**，金线 y=1698，卡面像素复核 1670–1711 行带内仅金线本身（1697–1698）且两版一致，无墨迹触线。
- **gloss 点数**：AST 逐条 **26 = 26**（6/5/5/5/5），词头序列同序、译文逐条忠实；P1 词表盒 3 = 3 同位。
- **日历**（`date` Europe/Amsterdam 实测）：10-10 六 · 10-17 六（秋假/DDW 开始）· 10-19 一 · 10-20 二（快照 «（火）» 合）· 10-21 三（ADE 开始）· 10-24 六（Venlo 家庭日）· 10-25 日（wintertijd 03:00→02:00 + topper 14:30）· 11-01 日（Robinson)，与纸面全合。
- **短尾行**：≤4 字假名行本版 13/293，为 ×JA 家族最低（EN×JA 31 · ES×JA 24 · FR×JA 21 · PT×JA 17；日语核心自身 44），实例皆正常句尾段——家族常态，非缺陷。
- **红线/残留**：日语注政治词全扫 = 0；简体专有码点 = 0、西里尔 = 0、中文家具 = 0、他列家具 = 0（P8 «R.A.W.» 引号式 «» 为讲解层引号规范化，内容全等）、纸面禁用术语 = 0（scratch 例外与 §4/§6 披露一致）。
- **最终针脚（磁盘实测，与 §1 登记逐字全合）**：网页版 `De-Lucerna-VOL1-JA-web.pdf` **3,620,618 B** · sha256 `8521baf352ac953c02043859aca8efafa61ac3705c24d85bda211460dc6045d0`（< 10 MB），8 页；印刷版 `De-Lucerna-VOL1-JA.pdf` **23,627,011 B** · sha256 `57d576df903ddbfcd66b64dd176e0f30c25e7cbad5e4021faff4e80307b9ffde`，8 页；cards ×8。

## D5 rebuild (13 Nov 2026; this build supersedes all earlier deliverable figures in this KIT)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib 2026-w43-nl-ja/svglib.py --target nl --reader cjk --week 2026-w43` (`--check` dry-run first, RC=0). `_D5_READER = "cjk"`. Routing unit test `test_d5_routing.py`: FAILURES: 0. D1 fix2 retained.
- Pre-rebuild census (`d5_census.py`, D5 elements in the pre-D5 SVGs): 325.
- Baseline (pre-D5 rebuild, venv, disk-measured): run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; print `De-Lucerna-VOL1-JA.pdf` 22,776,469 B (sha256 `64ae450a5c7aa1e491fbf67183e7b2bb483227c68a8912aa30684f4bc154a14b` — pre-D5 build, superseded); web `De-Lucerna-VOL1-JA-web.pdf` 1,554,398 B (sha256 `b15f281f6de0bf14341e731c756c213bee8fd0edf60ebfeee1d822c427dbb821`). Text layer print vs shipped web PDF multiset diff 0 (Python `len()` chars). The KIT-recorded print/web figures predate the §1.1 style port and the D1 re-render and are superseded by the disk-measured baselines above.
- Defects found by the 17 gates (run 1) and fixed by size only — text unchanged throughout:
  - Feature heads `ETEN BESTELLEN WORDT HELDER` (P2) / `EROPUIT IN DE HERFSTVAKANTIE` (P3) HEAD TOO WIDE at 25 pt (advance 472.2/466.0 px vs column 422.5 px) → head size 25 → 22 (`content12.py` P2 head, `content34.py:20`).
  - P1 box title `DE WEEK IN CIJFERS　数字で見る今週` over +38.2 px (right) → f.box tsize 23 → 20 (`content12.py:48`).
  - P6 p.text `AFSCHAFFEN OF NIET?　廃止か継続か` over +11.6 px (right) → size 21 → 20 (`content56.py:166`).
  - Occlusion TEXTX: P1 `数字で見る今週` title ink overlapped `De Dutch Design Week is in ___.` by 10.2×13.0 px — resolved by the P1 box-title fix above.
- P8: 212 → 212 lines, slack to footer rule 56.4 → 56.4 px (unchanged by §4; `content8.py` untouched).
- Gates (full re-run after fixes, run 2): **ALL-GREEN** — run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; head_check 0; d5 census 0; render RC=0; webpdf RC=0, web < 7 MB; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8 byte-identical; freeze diff vs baseline added CJK 0; spill 0 SPILL; boxtitle 0 DEFECT; edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web multiset 0, text.md BYTE-IDENTICAL; census_quotes 0 defective. Logs: `hidden_files/d5-redo/scratch-2026-w43-nl/gates/2026-w43-nl-ja/` (`GATES-SUMMARY.txt` master). Full record: `production/notes/2026-w43/g-nl/scratch-d5-rebuild-nl/D5-REPORT-2026-w43-nl-ja.md`.
- New deliverables (rebuilt 13 Nov 2026): print `De-Lucerna-VOL1-JA.pdf` 17,268,607 B, sha256 `f0e5545b6162fc03a44c42d4abea1c7a58a30395831fedf9c72ec9f10a9d8d27`; web `De-Lucerna-VOL1-JA-web.pdf` 3,247,158 B, sha256 `205b8050a49ba6dd3b90f655002bccba33c0ecb077ca758872917d92055936c9` (< 10 MB); text-layer web `2026-w43-nl-ja.web.pdf` 1,372,523 B, sha256 `025369496dc148f21b99202c492cc0a1655f84946e14f4cfd46ef126b6f5fcd4` (< 7 MB); `2026-w43-nl-ja.text.md` 40,337 B, sha256 `1c302aaeb0ecc17fa1edef11dcb5d267ac584a025b33f4a170be3a8e83fe5fc5`, **BYTE-IDENTICAL** to the shipped `issues/2026-w43/2026-w43-nl-ja/2026-w43-nl-ja.text.md` (exported from the build source with the scratch exporter `hidden_files/d5-redo/scratch-2026-w43-nl/export_text_w43nl.py`, W46 generic AST exporter + W43-nl italic-serif fix + `IN DEZE EDITIE` heading fix).
- Status: builder DONE, all gates green. Independent re-proof (SOP §8) is the coordinator's separate step; no commit, no push by the builder.
