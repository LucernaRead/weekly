# WEEKLY-KIT — IT×JA（イタリア語テキスト · 日本語の解説）W43 VOL.1

- **版次**：2026-W43（2026-10-19 – 10-25）· La Lucerna · イタリア語週刊 VOL.1
- **配对**：目标语 = 意大利语（正文逐字节冻结于意语核心 VOL.1）；读者母语 = 日语（讲解层全日语）。
- **状态：PASS**（独立校对一轮零问题，2026-10-22，见 §10）。
- **总量**：150 题 = A2 46 · B1 71 · B2 33；逐页 10/18/18/18/18/18/12/38；P8 范文 90 词（与核心一致）。

## §1 方法

1. 复制意语核心 build（hidden_files/weekly-report-it-build）→ hidden_files/weekly-report-it-ja-build；OUT 改道 files/weekly-report-it-ja（expanduser 写法已覆盖核对，首跑前打印验证）。
2. **freeze.py baseline 先行**：副本 8/8 SVG 与出货核心逐字节一致后才动工；收尾再跑 baseline 复核，核心 8 文件重哈希未变。
3. svglib.py 替换为日语核心版（见 §4）。
4. 讲解层变换：AST 定位 6 个 operative 文件中全部 484 个含 CJK 常量（259 个不同值），逐条以预先撰写的中→日映射替换（scratch/map_ja.py + transform_ja.py，断言未映射 = 0 后才落盘）；bridge() → expl() 改名（定义 1 + 调用 20 处）；固定点编辑：P1 徽章、P8 分隔符。
5. 一进程构建（run.py：content12→34→56→7→8 单进程，README 第 7 条）→ render.py 出卡与双 PDF。

## §2 交付物与实测针脚

- svg ×8、cards ×8（1950×2700）、印刷 PDF、网页 PDF，位于 files/weekly-report-it-ja/。
- 网页 PDF：**1590179 B**，sha256 `7c6b701e811b48f761398884aa664246a118b68b3d778e561d1bfa9a94690450`（D5 重建，tools/webpdf.py 发运件，< 7 MB；旧 3,546,696 B 值为 render.py 时代网页 PDF）。
- 印刷 PDF：**13919631 B**，sha256 `dcf2cd70ee2ba57b86aa75c439ecff0ad2add1cff3a091611408a5d1776a2386`（D5 重建）。

## §3 JA 列家具（照 EN×JA KIT §3 定式，目标名 = イタリア語）

- P1 顶带：`OGNI SETTIMANA IN ITALIANO · 毎週一号 · イタリア人が読んでいるイタリア語を読む`。
- P1 衬线行：`イ タ リ ア 語 週 刊 · VOL.1 · L'ORA SOLARE · IL MALTEMPO · IL CINEMA`（主题词沿用核心意语）。
- **P1 徽章**（IT 家族先例：替换核心 (975,372) tagline 呼び出し，20pt 粗体 BRICK 居中）：`イタリア語テキスト · 日本語の解説 — 日本語読者のための版`。
- P1 深色带右侧：`今週の日曜は1時間長く眠れる` / `標準時に戻る夜 · 詳しくは2ページ`。
- 页脚左：`La Lucerna · イタリア語週刊 VOL.1 · 本文はイタリア語 · 解説は日本語`；页码：`N ページ（全 8 ページ）`（bslib4 foot 片段映射：第→空、` 版 / 共 `→` ページ（全 `、` 版`→` ページ）`）。
- gloss 前缀：`解説 — `（gloss() 付加，调用值不带前缀；expl() 直接文字列自带前缀——P1 词汇行；P7 文法行前缀 `文法ポイント — `）。
- 章节头双语：意语原题 · 日语短题（VITA · 生活 / CULTURA · 文化 / SPORT · スポーツ / GIOVANI · 青年 / LINGUA · 言語 / APPROFONDIMENTO · 深掘り）。
- P8 头：`RISPOSTE · 全解答と解説（1–8ページ）`；右注：`各問に日本語の短い解説つき · ✓ は模範文のある問題`；分隔：`— N ページ —`。
- 题型/指令印刷形：空所補充 / 選択肢 / 文を作る / 語と意味を結ぶ / 正誤 / 空所補充・選択 / 翻訳 / 作文 / 書きかえ。
- P7 短语页标签沿用核心意语形 `(Pagina N)`（冻结）。

## §4 svglib 标准与双扫

- 日语讲解流 svglib = 日语核心版，**md5 d73e23b365676c3618d7e060b835eb4d**（构建前验、构建后复验一致；含 SEAM_SLACK=28 接缝修复）。
- **行首禁则扫描 = 0**（scratch/scan_lines.py：闭括号/标点/小假名/长音符行首违规 0）。
- **拉丁词断词 = 0**：以插桩方式在真实一进程构建中钩住每一次 wrap() 调用，逐串核对拉丁词序列（源 vs 渲染行）全等（scratch/check_wrap.py）——FR×JA 的 «moin/s»、«avoi/r» 缺陷类在本版不存在。
- 同行墨迹碰撞扫描（README 第 10 条，scratch/rowcheck.py，PIL 真墨迹）：**0**。

## §5 Manovra 诚实披露（双处，IT 家族口径）

1. **P6 图注**：冻结意语原句逐字节在位——`Tre voci pubblicate nel DPB del 15 ottobre — non è il totale della manovra (circa 23,5 miliardi).`；图表标题双语部分译日语：`LE CIFRE DEL DPB · 予算ファイルの数字 (...)`。图表全部 rect 几何与核心逐字节相同（条 5,0/5,0/3,4 与值标签不变）。
2. **P8 #85 印刷行**：`85. B — 5 + 5 + 3,4 = 13,4（合計ではない）`——13,4 ≠ 总额 23,5 以日语明示；#86 注 `5 − 3,4 = 1,6` 为语言中立式，逐字节沿用。

## §6 键差异登记（注册表级实测，scratch/registry_diff.py）

注册表键差异**恰 3 项**，全属合法类：

| # | 类 | 核心键 | 本版键 |
|---|---|---|---|
| 137 | 翻译题（键为中文句 → 改向日语） | 周日我们多睡一个小时。 | 日曜日、私たちは1時間長く眠ります。 |
| 138 | 翻译题（同上） | 展览一直开放到四月。 | 展覧会は4月までずっと開いています。 |
| 150 | 装置项（写作范文题） | （开放题，范文如下） | （自由作文、模範文は以下） |

- 题干改向（键不变、题干由中文改日语）：#139 `土曜18時、ナポリ対ローマ。→ ___`（键意语 `Sabato alle 18:00 si gioca Napoli–Roma.` 不变）；#140 `すべての数字には出典が必要です。→ ___`（键 `Ogni cifra deve avere una fonte.` 不变）。
- **印刷注释门**：p8.py extract 核心 P8 = 150 注；本版显式同集；`p8.py compare` = **CLEAN**（missing=[] extra=0）。
- p8.py 报告的 printed keydiff [12, 37, 58, 72, 78, 101, 137, 138] 裁定：137/138 为上表真实差异；**12/37/58/72/78/101 为提取伪影**（README 第 13 条口径）——逐项核印刷行，键逐字节相同（12 `mezza`、37 `castagne`、58 `più bella`、72 `muti`、78 `ci saranno`、101 `Sono`），差异仅来自注文含 `=`/折行位置；#150 印刷形为 `150. ✓ 注文`（无键），故不在 printed keydiff 内，与注册表一致。
- **语言中立注（逐字节沿用，共 10 条）**：#14 `12:00 = 正午 mezzogiorno`（正午为日语固有表记）、#15/#16/#17/#19/#60/#61/#102/#103（意语变位公式注）、#86 `5 − 3,4 = 1,6`。其余 140 条注全译日语。

## §7 机械门结果

- freeze.py baseline：动工前 8/8 逐字节复现；收尾复跑核心完整性通过（8 文件重哈希未变）。
- freeze.py diff：逐页分类闭合。移除侧非讲解项仅三类——(a) P1 tagline 被徽章替换；(b) 署名行/词库行折行点移位碎片（意语内容全等，JP 字体拉丁度量略窄所致）；(c) P8 分隔符 `— PAGINA n —` → `— n ページ —`（家具）。意语正文文本多重集与核心全等；新增 CJK 全部为日语讲解（假名占比逐页可见）。
- occlusion_audit.py（自检先行）：核心 0 旗；本版终版 **0 旗**。
- P7 短语：8 句逐字继承，出现次数与 `(Pagina N)` 页标签逐条 = 核心（程序核对）。
- gloss 词条逐条点数：5 处 gloss 调用词条数与核心全等（5/5/4/4/5，P2/P3/P4/P5/P6）。
- 日历对照真实 2026（Europe/Rome）：10/20 周二、10/23 周五、10/24 周六、10/25 周日（ora solare 03:00→02:00）、10/28 周三（Manovra 表决 + Lucca 开幕）、11/1 周日（Ognissanti）、12/6 周日（Alba 闭幕）、2027/3/28 周日（夏令时回归）——与纸面全部相符。
- 残留扫描：中文讲解残留 = 0（`来` 命中全在 未来形/未来、`点` 在 難点，均为日语固有词，逐条裁定）；荷/俄家具残留 = 0；禁用中介术语在 paper/KIT/operative code = 0（scratch/transform_ja.py 中出现的旧方法名仅作改名搜索模式，confined 于 scratch 并在此披露，依既定裁定属建造卫生注记）。
- 内容红线：讲解层未引入国际政治；P6 为意大利国内政治（核心口径沿用）。

## §8 自校缺陷与修复（全量自校一轮）

1. **P1 头条流 FLOW OVERFLOW**：数字盒两条日语括注折行 3 行（核心 2 行），盒体溢出与 B 行图像区相撞。修复：缩短两条括注（`（土曜→日曜の夜は25時間）`、`（日曜未明に変更）`），盒体回到核心行数；终版 P1-headline 流止于 y=1809 < 1828。
2. **P6 练习流 FLOW OVERFLOW**：A 节指令行宽 441px > 栏宽 CW=434，多折一行并连锁推挤三栏，最终题溢出页脚带。修复：指令缩为 `上の2図を見て、正しい答えを選びなさい。`；终版 P6-ex 止于 y=2569，与核心逐点相同，末题行 y=2540.5 与核心一致。
3. **P7 右栏三盒增高**：ERRORI 四条日语注各多折一行（+118）、PAROLA/LETTERE 注各多折行，LETTERE 盒底达 1850 压入 FRASI 区（核心 1674）。修复：六条日语注逐条按核心行数缩短并以 wrap 实测验证；终版三盒底 **984.0 / 1314.5 / 1674.0 与核心逐点相同**。
4. **遮挡审计初版 5 旗（全在 P1）**：快照注 EDGE 出页（墨迹至 x=1998）、RICERCHE 盒题 BOXTITLE、数字盒题 BOXTITLE、天气注 LINEX 压 1864 线。修复：四条讲解文字列逐条缩短（快照注改 `Google トレンド 10月20日（火）。数字は概数です。`；盒题改 `火曜の検索 · …`；数字盒题改 `数字で今週`；天气注改一行形 `「悪天候」：大雨、強風、嵐、名前は Adam。`）；重渲后审计 **0 旗**。
5. 构建警告总计：终版 run 日志 FLOW OVERFLOW = 0、HEAD TOO WIDE = 0。

## §9 备注

- 身份映射裁定（CJK 串与核心同形但为日语固有表记者）：`VITA · 生活`、`CULTURA · 文化`、`GIOVANI · 青年`、`12:00 = 正午 mezzogiorno`、`manovra = 予算案`、`previsione = 予測`——逐条裁定为日语表记，予以保留。
- 字体口径（tables.json）：Noto Sans/Serif CJK JP（index 0）；衬线标题 UnifrakturMaguntia。8 卡目视全过：无缺字、无方框。
- 本版未入仓、未发 Discord（依当前投递口径，入仓由主线以 insert.py 串行执行）。

## §10 独立校对记录（2026-10-22）— PASS（一轮零缺陷、零修复、无重渲染）

校对工件：hidden_files/proof-it-ja/（freeze diff JSON、p8 JSON、双注册表 dump、自备三扫脚本与结果）。

- **工具门（独立复跑）**：freeze.py baseline 核心 8/8 逐字节（哈希 bd04af2f…58f37fd4 与收尾复核全等，核心未动）；双 build 改道副本复渲出货 SVG 各 8/8 逐字节。freeze.py diff 分账闭合：纯拉丁净变化仅三类（P1 tagline→徽章、署名/词库折行再分割、P8 分隔符）；意语正文多重集 = 核心；added CJK 全为日语讲解。p8.py：extract 核心 = 150；compare **CLEAN 150=150**，keydiff=[12, 37, 58, 72, 78, 101, 137, 138]。occlusion_audit（自检先行）：本版 0 旗、核心 0、NEW vs core = 0。
- **注册表逐字节比对（自备一进程 dump）**：键差异恰 {137, 138, 150}（值与 §6 登记逐字合）；题干差异 {139, 140}（键意语逐字节未动，印刷行实证）；注差异 140 条、未变恰 10 条 {14, 15, 16, 17, 19, 60, 61, 86, 102, 103} 全为变位/算式公式（#86 «5 − 3,4 = 1,6» 逐字节）；题型映射 9↔9 双射，与 §3 指令形登记合；page/level 差 0；总量 150 = A2 46 · B1 71 · B2 33；逐页 10/18/18/18/18/18/12/38。p8.py 余 6 项 keydiff 证伪：注册表键逐字节相同（12 mezza、37 castagne、58 più bella、72 muti、78 ci saranno、101 Sono），差异仅注内 «=»/折行（README 第 13 条）。
- **手工重推导**：150 键逐题自意语正文重推导零分歧（含配对 #25–28 c/d/a/b、#52–55 c/b/d/a、#141–144 b/c/d/a；图表 5+5+3,4=13,4、5−3,4=1,6；虚拟式 #93–96/109–112；范文逐词手数 90 词、在 80–100 区间，文本在双版 P8 中去空白包含实证为冻结）。
- **Manovra 双处披露**：P6 图注冻结原句逐字节在版（去空白包含亦合）；图表 rect 与核心 30=30 逐元素全同（条 170/170/115.6px = 5,0/5,0/3,4 ×34）；文字压条 0、值标签距条尾恰 18px ×3。P8 «85. B — 5 + 5 + 3,4 = 13,4（合計ではない）» 在版实证。
- **JA 列定式核**：徽章实测 (975,372) 20pt 粗体 BRICK #a4553a 居中、文与 EN×JA §3 定式逐字合；顶带/衬线行合 §3；页脚 ×8 逐字同登记串；页码 «N ページ（全 8 ページ）» 1–8 对位；P8 头 «RISPOSTE · 全解答と解説（1–8ページ）» + 右注合；分隔 «— N ページ —» ×8、旧形 PAGINA 分隔 = 0；gloss «解説 — » 单层 6 处（双前缀 0）、文法ポイント — ×3；章节头双语 ×7 全合；目标语名 イタリア語 与 §3.1 名表一致。svglib md5 = d73e23b365676c3618d7e060b835eb4d（与日语核心逐字节同）。
- **自备三扫**：行首禁则（宽集含小假名/閉括弧/ASCII 閉符）= 0；拉丁断词（假名行衔接处以核心词库裁定）= 0；同行墨迹碰撞（PIL 真墨迹）= 0。
- **几何兜底**：P7 col3 三盒底 984.0/1314.5/1674.0 双版逐点相同；P6 末题基线 2540.5 双版相同；P1 rect 全表与核心全同（建造者 §8 修复 1/4 落点实证）；P6 rect 全同（修复 2 落点）；P2–P5/P8 rect 差异仅题号 chip 纵移与 E TU 等内容盒随讲解行数增高，盒内自洽、审计 0 旗，非缺陷。P8 #40 注两元素同栏相邻行（Δy=15.66=行高）衔接连贯。P7 rect 差异仅 A2/B1 栏 chip 纵移。
- **gloss/P7**：gloss 词条 P2–P6 = 5/5/4/4/5 同数同序、P1 expl 4 条；8 金句逐字回溯原文（P1/P2/P3/P4/P5/P6 原文逐条命中）、(Pagina N) 标签计数双版全同 {1:2, 2:2, 3:1, 4:1, 5:1, 6:1}。
- **日历（Europe/Rome 实测）**：10-10 六、10-19 一、10-20 二、10-21 三、10-22 四、10-23 五、10-24 六、10-25 日（ora solare）、10-28 三、10-31 六、11-01 日、11-02 一、12-06 日、2027-03-28 日——与纸面全合。
- **残留**：西里尔 0、韩字 0；他列家具 0（«Pagina » 12 处全为冻结意语互见标签，«van 8» = 0）；禁用术语纸面 paper/KIT/operative/bridge = 0；无假名汉字串逐条裁定全为日语固有表记（国の予算案・全国的・2点・難点・未来形等），中文讲解残留 = 0；讲解无国际政治新增。
- **最终针脚（D5 重建 2026-11-13，磁盘实测，与 §2 登记逐字全合）**：网页 PDF 1590179 B / sha256 7c6b701e811b48f761398884aa664246a118b68b3d778e561d1bfa9a94690450；印刷 PDF 13919631 B / sha256 dcf2cd70ee2ba57b86aa75c439ecff0ad2add1cff3a091611408a5d1776a2386。未入仓、未发 Discord。

---

## §11 D5 重建记录（2026-11-13）

D5 + §1.1 合并重建记录（2026-11-13；一任 builder 至 run2 循环，二任 builder 接手核实 + gate 2 补跑；不 commit、不 push；独立重校另派他人）。

- 装机：`apply_variant.py --patch-core it --week 2026-w43 --i-understand-this-writes-production`（core-it 落盘 `_D5_READER = "latin"`）；本版 `apply_variant.py --svglib <版>/svglib.py --target it --reader ja --week 2026-w43`，`_D5_READER = "cjk"`；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2（U+201C/U+201D/U+2019 → serif）保留。
- 基线：run TOTAL 150、0 警告；SVG 8/8 与 fanout 逐字节相同；印 PDF 与 fanout SHA 一致（21087394 B）；修前普查 D5 拉丁 341 / 西里尔 0 / 弯引号 CJK 0。
- 二次修复（只动字号，文字零改动；盒修法行号指 tsize 行，D19）：`content34.py:22` P3 头 25→22; `content12.py:48` P1 盒 `LA SETTIMANA IN CIFRE · 数字で今週` tsize 23→20（383.7，余 20.8px；21pt 仅余 1.5px 太薄，不取）; `content12.py:70` P1 Trends 行 `火曜の検索　Cosa cerca l'Italia (Google Trends)` p.text 19→18（387.9，距盒右缘 12.6px）; `content12.py:91` P1 `IN QUESTO NUMERO · 今号の内容` p.text 24→23（391.7，余 8.8px）; `content12.py:181` P2 盒 `LA FRASE PER RICORDARE · 覚え方` tsize 23→22（399.8，余 4.7px）。
- P8：行数 209→209，距页脚线余量 57.4 px；p8 compare CLEAN（keydiff [137, 138]）。
- 新交付物：印 PDF `The-Lucerna-VOL1-it-ja.pdf` `dcf2cd70ee2ba57b86aa75c439ecff0ad2add1cff3a091611408a5d1776a2386`（13919631 B；修前 `b602ca1c7d5b67d932062607cc6241f300e51c662a6af5cec9a75104556bde30`，21087394 B）；网 PDF（tools/webpdf.py）`7c6b701e811b48f761398884aa664246a118b68b3d778e561d1bfa9a94690450`（1590179 B；已发版 `53a34b8aa9cc337763e7c51f3cbdf7db1eeb2a0eab370f872d775a0afa0c13ae`，1912174 B）；text.md 与 fanout `.text.md.new` BYTE-IDENTICAL（56222 B，SHA `8680b796df4a68bc428f2c8d87f68fff4a8d3e61315fb71b2d1a0888b54ed34c`），W43 it issues/ 内无已发 `.text.md`，closer 落仓时新建补入。
- 门禁 run2 ALL-GREEN（18 门：run TOTAL 150 / head_check 0 / d5 census 0/0/0 / render RC=0 / webpdf RC=0 / occlusion 0 / p8 extract 150/150 / p8 compare CLEAN / freeze baseline 8/8 / freeze diff 新增 CJK TOTAL 0 / spill 0 / boxtitle 0 DEFECT（28 titles、331 body lines）/ edge 0/0 / creambox PASS 0 defects（n=395）/ 文字层 print=web 多重集差 0 / census_quotes 0 defective / 家族 gates.py N/A / 刊头间距 306.8 px PASS）。日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-ja/GATES-SUMMARY.txt`；D5 报告：`production/notes/2026-w43/g-it/scratch-d5-rebuild-it/D5-REPORT-2026-w43-it-ja.md`。
- 本 KIT 交付物行已更新为以上 D5 新值；旧针脚为旧配方值，已过期，以上实测发运值为准。
