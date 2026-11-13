# 独立校对笔记 — 2026-W47 德文核心版 · 第四轮（build14 全量复校）

校对员：第四轮独立校对（与 builder、各轮返修 builder、第一、二、三轮校对员均不同人）。只读不改：未改 core-de 内任何文件（终验 SHA 与开工时一致，mtime 未动），未改 tools，未跑 insert.py / lint --write / git push/add/reset/stash / commit；未碰 W43/W45/W46、其他目标语。
校对时间：2026-11-11 01:35–02:00 UTC。对象：`~/workspace/weekly-git/production/2026-w47/core-de/` build14，8 页，1462.5×2025pt。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de4/`（本笔记 + `work/` 下日志、渲染图、测量输出；另有 `probe1.txt`）。

## 开工探针（硬门禁，双通）

- `git hash-object -w`（weekly-git 内）：通，`e630ee6228d3cb0d1cd5f1635e4651d3390761c1`，rc 0。
- 真实文件写 `scratch-proof-de4/probe1.txt`：通。
- 无 Disk quota / EPERM。另：一次早期 `find` 后台任务被手动 kill（与校对无关，仅清场）。
- 任务书路径更正：`hidden_files/w47/scratch-de-fix3/FIX-LOG-de3.md` 实际在 goals 目录下（`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-de-fix3/`），已按实际路径读到；weekly-git 内无 hidden_files。

## 结论：(a) 零问题，可定稿

**D6 已修好（逐项独立实测）；D1–D5 回归重测全部通过；P8 14 枚徽章逐枚核实、级别与登记表 0 偏差；全量复校（全文精读、150 题逐题验算、全部机械门自跑、§1.1 逐项实测、8 版目视重做、KIT build14 逐项核对）零缺陷。O1 按裁定不重列（实测字号与 build10 一致，仅 span 计数因新增徽章行而变，见“O1 复核”）。本轮即为一整轮全量校对零问题（SOP §8.4）。**

---

## 身份核对（与任务书逐项一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de.pdf`（印刷） | 22,965,190 | `a51f785a0ca2df5a6452bb736a59f5532e08e535c4796736610829a856b92766` |
| `Die-Lucerna-VOL4-de-web.pdf`（网页） | 2,044,844 | `b27571eafaf109a10a3c2d686863e630758224b6bd583c53b5d122492f4e0125` |
| `2026-w47-de-zh-cn.text.md` | 49,799 | `1c219c84864ababa52c7a63985614f7cd54bb780913ccae43fff6890b393ce86` |

PDF：8 页，1462.5×2025pt。`.text.md` 与 build11 同 SHA（返修未动正文）。

---

## D6 逐项验证（独立实测，不采信返修/KIT 记录）

- **两新句均在交付 SVG 内**（join 归一化检索）：P3 `Viele Kinder haben ihren Adventskalender schon zu Hause — aber das erste Türchen öffnet sich erst am 1. Dezember.`（p3-kultur.svg）；P5 `In vielen Familien brennt im Advent eine Kerze auf dem Tisch, und auf dem Kalender leuchtet ein Stern.`（p5-jugend.svg）。两句亦在 build14 印刷版文字层（print.txt 各 1×）与 `.text.md` 各版文章段内。
- **正文段内计数（严格口径：byline 之后、译注行之前，仅主文章段；屈折/拆分形计入）**：P3 文章 6/6——Weihnachtsmarkt 4、Glühwein 2、Lebkuchen 1、**Adventskalender 1**、Weihnachtsbaum 1、Kerze 1（复数 Kerzen）；P5 文章 6/6——Türchen 3、Wunschzettel 3、Christkind 2、Schokolade 1、**Kerze 1、Stern 1**。**12/12 框词均在文章。**（脚本 `work/check_gloss_strict.py`；初版脚本因 `gebrannte Mandeln` 屈折形 `gebrannten` 与 `weiterkommen` 拆分形 `kommen weiter` 精确匹配报 0，已逐一核实为计数口径问题，非缺词。）
- **两新句无新事实**：P3 句“第一扇小门 12 月 1 日打开”与 P5 文章已有事实一致；P5 句为泛指生活描写，直接支撑 Q74/Q75 题面措辞，无编造。
- Q74/Q75 答案仍为 Kerze/Stern，题面、键未动；P5 练习 B 标题 `WÖRTER AUS DEM TEXT` 现有文章锚点。

## D1–D5 回归重测（全部通过）

### D1（题干字号）— 通过
- 自写脚本（`work/check_stems.py`：AST 提取全部 124 个 `ex()` 体，与全部 SVG `<text>` 首行最长前缀匹配；输出 `work/stems-de4.log`）：**124 个 ex() 全部命中，低于下限 0**。P1–P7 题干 22.0 单位 = 16.5pt；P8 20 题 20.5 单位 = 15.375pt。源码交叉核对：`bslib4.py` 含 `STEM_MIN = 22`、`STEM_MIN_P8 = 20.5` 及 `ex()` 内 `size = max(size, ...)` 钳制。
- 误匹配已逐一排除（非真问题）：P3 出现一个 21.5——是 Q38 题干误 match 到 col 3 事实框行 `Die offizielle Eröffnung am Dom ist`（21.5 单位事实框字，见观察项 O4），题干本行 `Die offizielle Eröffnung am Dom ist am` 实为 22；P3/P6 的 24.0 匹配是文章句（24 单位文章行）。三处均经 SVG 直接 grep 确认。
- 栏高/溢出：freeze-out 复现日志零 `FLOW OVERFLOW` / `HEAD TOO WIDE`；最紧仍 P6-ex 2523/2560、P1-quiz 2523/2560、P8-keys 2504/2560；P3-main 886/1560、P5-main 966/1080。

### D2（§8.1，P4 `die Ligaphase`）— 通过
- 严格文章段计数：das Tor 2、der Spieltag 3、torreich 1（`torreichste`）、die Ligaphase 1、weiterkommen 1（拆分形 `kommen weiter`）。**5/5 在正文。**SVG 内 `Ligaphase` 2×（文章句 + 译注行）。

### D3（§8.1，P6 `die Buße`）— 通过
- 严格文章段计数：die Buße 1、das Kirchenjahr 2、der Verstorbene 1（`Verstorbenen`）、der Friedhof 1、der Haushalt 2（`Bundeshaushalt` + `jeden Haushalt`，与 builder 称 1 为少计一致，结论不受影响）、die Einigung 1。**6/6 在正文。**Q97 与文章逐字对齐。

### D4（塞尔维亚场）— 通过（独立查源，不只信记录）
- 本轮独立检索（browser.search，2026-11-10 当日多家一致报道；检索时间 2026-11-11 01:44 UTC）：kicker.ch、bundesliga.com、fussballnationalmannschaft.net、bavarianfootballworks（dpa 口径）、gmx.ch、pressaris.gr 均确认——UEFA 观众禁令 + €50,000 罚款（因歧视性球迷行为），但按 UEFA 规则例外：15 岁以下儿童（教师/教练陪同）+ 50 名精选德国球迷可入场，预计约 5,000 人，55,000 座 Rajko-Mitić 球场“基本空着”；开球 **2026-11-13 周五 20:45**（`date -d` Europe/Berlin：13 日 = Friday ✓）；同组积分荷兰 8、希腊 8、德国 5；主教练 Jürgen Klopp。
- 关键辨析：**第一轮“零观众”是 10 月 22 日旧口径**（10 月 12/22 日来源称全面禁赛；10 月底塞尔维亚足协申请放宽）。11 月 10 日报道一致确认例外已落地，“零观众”现为事实错误。本版“vor fast leeren Rängen（仅儿童与 50 名德国球迷入场）”与最新报道一致，措辞正确。
- 四要素在位：P1 新导语含日期（13. November）、过去时（traf）、“vor fast leeren Rängen”、括号内例外（nur Kinder und 50 deutsche Fans）✓；`Serbien` 全期仅 3 处（P1 导语、P1 快讯、Q7 干扰项 A），P4 赛程表与 P5 周计划均无塞尔维亚场 ✓；旧句 `trifft Deutschland in Belgrad` / `Am Freitag (20.45 Uhr)` 全期已无（SVG + 文字层 0 次）✓；P7 工具箱同步句在位 ✓；11 月 16 日周一 20:45 对荷兰（柏林）与 P4 赛程表一致（16 日 = Monday ✓）。

### D5（P3 Q42）— 通过
- 新题干 `Wie viel früher als der erste Advent beginnen die Märkte?` 在 P3 渲染图、`.text.md`、P3 SVG（join 拼接后）、印刷文字层四处一致；旧题干全期 0 次。
- 仅一解验算：A `Sie öffnen fast zwei Wochen früher.` 唯一时间跨度表述，与文章 `Die Märkte beginnen fast zwei Wochen früher.` 一致（市场 11 月 16 日开，将临期 11 月 29 日，相差 13 天 ≈ 快两周）；B、C 非时间跨度。**仅 A 可解** ✓。选项、键、注记不变（P8 键 `42. A`）。

---

## P8 徽章核实（本轮重点：逐枚映射，级别与登记表逐键比对）

- 全刊 chip（SVG `rx="2.7"` 矩形计数）：**141**——P1 10、P2 15、P3 18、P4 15、P5 18、P6 18、P7 12、**P8 35**，与任务书/KIT 一致。
- P8 35 枚逐枚映射（脚本 `work/check_badges_p8.py`，按 `chip()`/`badge_opt`/`badge_strip`/`match_set`/写作 chip 的几何口径配对题号，再与独立复现的登记表比对）：**0 处不匹配**。
  - 完形 Q113–120：8 枚行首 chip，全 **A2**（登记表 `cloze_defs` 全 A2）✓。
  - 对话 Q145–149：徽章条 2 行（3+2）：145 A2、146 A2、147 A2、**148 B1**、149 A2（登记表 `ddefs` 一致；148 的 B1 底色在渲染图上 visibly 更深）✓。
  - 写作 Q150：H 标题行首 **B1** chip ✓。
  - 其余 P8 chip（B–E 各 `ex()`、F 配对共享一枚 B1 141–144）级别全部与登记表一致。
  - （脚本标签小注：Q147 在日志里被标为 `badge_opt`，是配对容差把 strip 的题号文也命中所致；其 chip 位置/级别 A2 正确，非成品问题。）
- P1–P7 逐页映射（脚本 `work/check_badges_all.py`）：每页全部登记题号均有 chip 且级别一致，0 缺失、0 错误、0 未配对 chip。分版 chip 级别分布与登记表逐页一致（如 P6 B1 8 / B2 10；P7 A2/B1/B2 各 4）。
- `badge_opt`/`badge_strip` 只画徽章、不碰 REG（源码已读；编号连续性由独立复现的登记表证实）。

---

## 全量复校（每项都跑过）

### 全文精读
- `.text.md` 49,799 字节（42,393 字符，1185 行）逐行读完（P1–P8）。德语拼写、变格、变位、性数配合、标点未见错误；未见重复词、截断句；中文讲解层与德文对照无误。
- §8.1 全量：P1–P6 六条译注逐词重数（严格文章段口径），**全部在当版文章段内**——P1 4/4、P2 5/5、P3 6/6、P4 5/5、P5 6/6、P6 6/6。词表框 12/12 在文章（见 D6）。
- 抽查要点：P2 日期加法 18+11=29、15+7=22、16+6=22 ✓；P3 `Vor fast 100 Jahren`（1930→2026 为 96 年 ✓）、市场 11 月 16 日–12 月 23 日且 22 日关闭与 Q40 键一致；P4 `4. Spieltag der Ligaphase`（3–4 日周二/周三 ✓）；P5 1903 年日历“über 120 Jahre alt”（123 年 ✓）；P6 预算 11 月 27 日周五表决（27 日 = Friday ✓，`date -d`）、2,05 欧分与 Q91/Q127 一致；P7 纠错诊所 4 条全部正确；P7 下期预告 VOL.5 承诺（29 日将临期、24–26 日欧战、11. Spieltag、读者来信）与 KIT §9 一致。
- 日期星期（`date -d` Europe/Berlin）：3 日周二、4 日周三、5 日周四、7 日周六、8 日周日、13 日周五、16 日周一、17 日周二、18 日周三、20 日周五、22 日周日、24 日周二、25 日周三、26 日周四、27 日周五、29 日周日，全部核对 ✓。

### 150 题逐题复核（答案键逐题独立验算，尤其 P8 113–150）
- 登记表（独立复现，见“机械门”）：TOTAL **150**，按版 10/18/18/18/18/18/12/38，编号连续 1–150；级别 A2 69 / B1 67 / B2 14；题型与 KIT 一致（单选 52 / 完成句子 41 / 句型转换 11 / 判断对错 8 / 完形 8 / 造句 8 / 词汇配对 12 / 翻译 4 / 对话补全 5 / 写作 1）。
- P1（1–10）：1 Bundesliga、2 Niederlande、3 Sachsen、4 Totensonntag、5 fünf、6 29. November；7 B、8 A、9 B、10 B——全部与头版文章一致。
- P2（11–28）：日期题 11–15 全对（18 日周三 ✓）；Perfekt 16–20 全对（16 `ist … abgeschafft worden`、17/20 `sind … geblieben`、18 `sind gegangen`、19 `hat behalten`）；21 B、22 B（1995）、23 A、24 B；配对 25–28 键 d/c/a/b 与 `content12.py` 的 `match_set`（rights 顺序 a. ruhig und leise / b. der Tag, an dem man nicht arbeiten muss / c. zur evangelischen Kirche gehörend / d. der Tag zum Nachdenken und Beten，keys [d,c,a,b]）逐一相符。
- P3（29–46）：判断 29–33（R/F/R/F/R）与文章一致；填空 34–38（Weihnachtsmarkt/Glühwein/Lebkuchen/Advent/Weihnachtsbaum）与方框一致；39 B、40 B、41 A、**42 A（仅一解，见 D5）**；造句 43–46 动词第二位全对。
- P4（47–64）：比分题 47–50 全对；第 9 轮总进球重算 4+3+3+7+4+1+3+2+3 = **30** ✓；51 B（荷兰 8、德国 5）；配对 52–55 d/b/c/a 与 `content34.py` 的 `match_set`（keys [d,b,c,a]）相符；比较级 56–59（mehr / später / früher / mehr）均与数据相符；时间题 60–63（20.45 / 20.30 / 18.30 / 17.30）与赛程表一致；64 B（3:1）✓。
- P5（65–82）：65 A、66 B、67 B、68 B、69 A；70–75（Türchen / Wunschzettel / Christkind / Schokolade / Kerze / Stern）与方框一致；weil 句 76–79 动词置尾全对；80 R、81 F、82 R ✓。
- P6（83–100）：图表题 83–88 全对（44+33=77、总和 100、23% 最小）；89 B、90 A、91 B、92 B；语法 93–96（wird / ob / geht / beginnt）；97–100（Buße / Kirchenjahr / Friedhof / Einigung）与文章一致，98 `des ___s` = Kirchenjahr + s（属格）✓。
- P7（101–112）：101 wird、102 werden、103 wird、104 A；105 stiller、106 weil、107 weil 句、108 A；109 ob、110 fraglich、111 `Ich finde, dass das Gedenken Stille braucht.`（dass 句动词句末）、112 B ✓。
- P8（113–150，逐题重算）：完形 113–120（A/B/A/B/A/A/B/A）——主语均为 Lena（第三人称单数现在时），干扰项复数/过去时均排除，**每题仅一解**；121–128（A/B/B/B/B/A/B/B）；阅读 129–132（A/B/B/B）与 Berger 短文逐句相符；造句 133–136 动词第二位全对；翻译 137–140（140 `Am Montag schaue ich zu Hause Deutschland gegen die Niederlande.` 第一人称 schaue ✓）；配对 141–144（c/a/d/b）释义逐一相符；对话 145–149（A/B/A/A/A，人称与对话一致）；150 开放题无固定键 ✓。
- 金句：8 条各恰 2×、逐字出自本期正文（自写脚本按 verify.py 口径 join 全部 SVG 文本计数，`work/golden-de4.log`）。注：pdftotext 默认模式因栏序重排会把跨行金句计成 1×，属提取口径问题，SVG 层计数为准。
- 目录与跨版引用：P1 目录 S.2–S.8 与各版栏目/级别一致；`详见第 4 版`、`答案见第 8 版`等引用页码无误；页码行 8 版齐全 `第{n}版／共8版`。
- MUSTER 84 词（空白切分，`.text.md` 逐字数）✓。禁用词扫描：`Geisterspiel / Karneval / Volkstrauertag / NFL / American Football / Tankrabatt / Hart aber fair / Klassiker / Allerheiligen / VOL.3 / VOL.2 / Le Lucerna / The Lucerna / 11.11` 全期 0 次；`VOL.5` 7 处全部为合法的下期预告/读者来信/写作框语境 ✓。

### 机械门（独立重跑，日志在 work/；未在原目录写文件）
- `tools/occlusion_audit.py` 全 svg 目录：**0 flags**，自检通过（6 类植入全触发、干净对照静默）。（`work/occlusion14-de4.log/json`）
- `tools/p8.py extract --p8 svg/p8-uebungen.svg --total 150`：**150/150**；`compare` 核心对自身：`status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]`。（`work/p8extract-de4.log/json`、`work/p8compare-de4.log/json`）
- **freeze 真跑**（`tools/freeze.py baseline`，`--out work/freeze-out`；`work/freeze-de4.log/json`）：rc 0，**8/8 SVGs byte-identical**，core integrity：交付 SVG 在运行前后未变。并用直接 sha256 比对 OUT 重建产物：`freeze-out/build-copy/svg/*.svg` 与交付 SVG **8/8 一致**（p1 2b0a53ad…、p2 b354e140…、p3 7dcdfe11…、p4 ba0f0505…、p5 710457f7…、p6 1f49f462…、p7 e5f5dc07…、p8 7814b613…）。——KIT 称 freeze14a.log 为 0 字节、本轮未 claim freeze 8/8；**本次真跑补上了 8/8**，未用 build-copy 冒充。（注：第一版直接比对误用了空的 `freeze-out/svg/`，已纠正为 `freeze-out/build-copy/svg/`，见日志。）
- 登记表独立复现（`work/reg_dump.py`：把 core-de 复制到 scratch 副本内跑 `run.py` 同款顺序，**不在原目录写文件**；`work/reg-de4.json/log`）：TOTAL 150；by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；levels A2 69 / B1 67 / B2 14；types 与 KIT 一致；numbering continuous True；flow 终点与 KIT build14 一致（P8 battery 1409.44、图高 140、图结束 1633.24、keys 2504；P3-main 886、P5-main 966、P6-ex 2523、P1-quiz 2523、P8-keys 2504、P7 image ends 1541.83）。verify.py 本身未在原地重跑（它会在 core-de 内重写 SVG）；其全部断言已按上法逐项独立重推（登记表、风格审计、金句、禁词、图柱、MUSTER、最小字号）。
- 文字层：`pdftotext` 默认模式 print/web 各 **50,499 字节**，词多重集相同（7,235 token）；`-raw` 模式各 49,382 字节，**逐字节相同**（`cmp` 通过）。web PDF 带真实文字层，2,044,844 字节 < 7MB。
- P8 最小字号实测 ≥9.75pt：PyMuPDF 实测 P8 最小 span **10.12pt**（95 处答案键）；其余各版最小 11.62–12.75pt（P1/P3/P4/P5/P7 11.62，P2/P6 12.75）。P8 字号直方图：10.12×95、13.88×16、14.62×41、15.38×60（P8 题干）、18.0×46——与 O1 复核一致。
- P6 图柱：SVG 橄榄绿矩形宽 748/561/391 ✓；图表 44+33+23=100 ✓；ÜBUNGSDATEN 标注在位。

### §1.1 逐项实测（PDF 实测值；FR 为已验收 W46-FR zh-cn 版对照）
| 项 | SOP 要求 | DE build14 实测 | 结论 |
|---|---|---|---|
| 版数/答案 | 8 版，答案在 P8 | 8 页，答案 P8 | ✓ |
| 纸色 | #fbfaf6 | SVG rect #fbfaf6；渲染采样 (251,249,246)（见 O2） | ✓ |
| 墨/正文/说明/细线/书衣绿/橄榄绿/鹅黄/米白/浅底 | #302c28/#3a3631/#6f675d/#d8d2c4/#37402f/#46581f/#f6e08e/#f4efe1/#f0eee5 | `svglib.py` 常量与之一致（INK/OLIVE/PAPER/CLOTH/GOOSE/ONCLOTH/BOX/LINE/GREY 全对）；旧式金色 hex 全期 0 | ✓ |
| 徽章三色 | A2 #5c6e30 / B1 #46581f / B2 #37402f | `bslib4.py` LV_COLOR 一致；PDF 内 chip 填充与之一致 | ✓ |
| 刊头 | 147pt，UnifrakturMaguntia | 147.0pt（= FR 147.0） | ✓ |
| 刊别 | 27pt / 700 | 27.0pt 粗体 | ✓ |
| 导读条/栏目条标题 | 34.5–37.5pt | P1 导读条 34.5pt、P2 栏目条 34.5pt（= FR 34.5） | ✓ |
| 头条标题 | 40–45pt | **39.75pt**（= FR 39.75；见 O3） | 观察 |
| 次级标题 | 22.5–24pt | 24.0pt（P2–P6 各版头） | ✓ |
| 头条正文 | 18–19pt | 24 单位 = 18pt | ✓ |
| 侧栏正文、练习题干 | 16.5–17.5pt | 题干 16.5pt ✓；侧栏事实框 16.125pt（见 O4） | 观察 |
| 栏目小字 | 12.75pt | 12.75pt（顶栏/页脚） | ✓ |
| 讲解层、图注、说明 | 11.25–13.5pt | 译注 15.375pt（见 O5）；图注 14.25pt、图注出处 11.62pt（见 O6） | 观察 |
| 答案 | 让步顺序，最低 ≥9.75pt | 10.12pt（让步第 4 步，未扩版） | ✓ |
| 线条与版心 | 无双线外框；版心上 54/左右 66/下 48pt | 无描边双线框；MX 88px=66pt、band top 72px=54pt（源码 + 渲染确认） | ✓ |
| 排字 | 全角空格分隔；`第N版／共8版` 无空格；无首字下沉问题另记 | 页脚/页码行/刊别均为全角空格；`VOL.4` 刊头 9 处式样正确；首字下沉缺失（见 O7） | 观察 |
| 字体 | Newsreader（拉丁）/ UnifrakturMaguntia（刊头）/ Noto Sans CJK（中文） | PDF 内嵌：Newsreader 16pt（Regular/Italic）、UnifrakturMaguntia、NotoSans/SerifCJKsc（Regular/Bold），全部 embedded | ✓ |
| VOL 号 | 台账 VOL.4 | 刊头/页脚/刊别均为 VOL.4；VOL.3 0 处；VOL.5 仅预告语境（见上） | ✓ |
| P8 题干 | 让步 15.4pt | 15.375pt（20.5 单位，60 spans） | ✓（已裁定现值） |

### 8 版逐版看图（自 build14 印刷版 PDF 每页 110dpi 重新渲染，`work/pg-1.png` … `pg-8.png`，逐版目视；KIT Status 行所称 build11 那轮视觉复校已被本轮取代）
- P1：新导语完整无溢出；头条、数字栏、即学即练、快讯、闪电问答齐全；页脚/页码行齐全。无问题。
- P2：练习区完整，配对块落位，Rechnen 横线间隔清晰。无问题。
- P3：D6 新句在位、Q42 新题干在位、选项齐全；画作图注与出处齐全；词汇框含 Adventskalender。无问题。
- P4：`Spieltag der Ligaphase` 在位；赛程表仅 Mo 16.11. 荷兰场，无塞尔维亚场；Und-Sie 框中德文齐全；赛程表脚注只列欧联赛事（Dinamo Zagreb–Leverkusen、Hoffenheim–Sturm Graz），Freiburg–Twente 属欧协联未列入，不属遗漏。无问题。
- P5：D6 Kerze/Stern 句在位；周计划 Mo 16.11.–Fr 20.11.，无塞尔维亚场；1903 日历图注与出处齐全；练习 B 方框含 Kerze/Stern。无问题。
- P6：图表 44/33/23 完整、ÜBUNGSDATEN 标注在位；Q100 落在页脚上方留空处。无问题。
- P7：工具箱新译注完整；金句 8 条、诊所 4 条、读者来信编辑示例标识清晰；VOL.5 预告在位。无问题。
- P8：完形/问答/阅读/造句/翻译/配对/对话完整；徽章条 145–149 齐全且级别正确（放大裁图 `work/crop-p8-dialog.png`）；1905 图 + 图注与写作横线间隔清晰（放大裁图 `work/crop-p8-image.png`）；MUSTER 清晰；答案键四栏完整，均在页脚上方结束（放大裁图 `work/crop-p8-keys.png`，末行与页脚线有清晰间距）。无问题。
- **P8 图高 140 落地**：电池流结束 col3 y=1409.44（bottom 1555）；图高 140 SVG 单位，图（含图注）结束 1633.24；写作条 wy=1650。渲染图上图片未被压扁（与 build12/13 的 79.55px 压扁态不同）。PDF 内图片放置框 316.88×129.29pt：该值是 slice 模式下未裁剪的放置框（源图 1000×408，长宽比 2.451；按宽覆盖算高 422.5/2.451=172.38 单位=129.285pt），可见高度仍为 140 单位 = 105pt（见“O8 测量澄清”）。

### 图片许可与署名（逐张核对 assets/CREDITS.md，build10 以来无改动）
- P1 fussball.jpg（DVIDS 333458，PD）、P4 kopfball.jpg（DVIDS 333408，PD）、P3 weihnachtsmarkt1930.jpg（Ritter 1860–1948，PD）、P5 christkind.jpg（Kepler 1903，PD）、P7 lesesaal.jpg（Highsmith，国会图书馆，PD）、P8 fussball1905.jpg（1905 年，作者不详，PD）——印署与 CREDITS 一致，未见版权不明肖像。

### ABSTRACT.txt
- 单行、无 ASCII 双引号、简体中文；含刊名、目标语名、A2–B2 分级、150 道练习与本期真实主题（德甲回归、欧国联荷兰、忏悔祈祷日与亡灵主日、科隆市场、11 月 3–8 日赛果），与 KIT §5 逐字一致 ✓。296 字节。

### P7 读者来信（F-MAIL）
- 明确标明编辑示例（`Ein Beispiel der Redaktion!` + 截稿未收到真实来信、见 VOL.5，中德双语）✓；无编造来信；承诺顺延 VOL.5 ✓；未查邮箱。

### KIT 核查（build14 数值逐项）
- §5 交付物：字节与 SHA 与本轮实测一致（print 22,965,190 / a51f785a…、web 2,044,844 / b27571ea…、.text.md 49,799 / 1c219c84…、42,393 字符、150 题）✓；ABSTRACT 逐字一致 ✓。“591 entries”无法精确复现（文件 1185 行、非空行/块 593；591 = 块数 − 2，或为扣掉 2 个题头块的口径），属 KIT 元数据小口径，不影响文件本身（SHA 已验），见 O9。
- §6 门禁：与本轮独立重跑一致（occlusion 0、p8 150/150 + CLEAN、题干字号、文字层 50,499 字节、P8 最小 10.12pt、栏高终点、图柱、MUSTER）✓；freeze 8/8 由本轮真跑补上（KIT 称待第四轮重跑，已完成）✓。
- §7：D6 修复说明与实测相符（植入文章法、两句位置、未动项清单）；D1–D5 记录与本轮重测相符 ✓；FIX-LOG-de3 的根因（build12/13 补偿未落盘、fix3b col3 补偿使图恢复 140）与本轮实测一致（电池流 1409.44、图 140、图结束 1633.24）。
- §8：O1 已记入（见下节）；短缺项（无真实来信、13/15/16 日赛事仅为预告、图表为练习数据、P8 字号让步、无首字下沉）与实测一致 ✓。
- §9 VOL.5 承诺：逐项已核实（29 日周日首个将临期、24–26 日欧战、11. Spieltag 27–29 日、圣诞市场、真实来信）✓。

---

## O1 复核（不列缺陷，按协调员裁定）
- 实测字号不变：P8 完形段落与对话段落 19.5 单位 = 14.625pt、选项行 18.5 单位 = 13.875pt，与 build10 一致；P8 渲染图上该两段落与选项行清晰可读，无溢出、重叠、无法辨认等新的读者可见问题。属继承结构（W46-DE 即为 18.5 单位）、模板级问题，本次不修。**不重新列为缺陷。**
- Span 计数变化说明（非字号变化）：14.62pt span 由 build10 的 36 处变为本轮 41 处——正好 +5，为徽章条新增的 5 个题号文（`145.`–`149.`，19.5 单位）；13.88pt span 由 13 处变为 16 处——为完形 3 行折两行（Q113/Q115/Q117，徽章使选项行变窄）多出的 3 行。字号本身未变。

---

## 观察项（不计缺陷，留协调员知悉）

### O2：渲染采样纸色 G 通道差 1（与第三轮相同）
- SVG 纸面 rect 填色确为 `#fbfaf6`；72dpi 采样 (251,249,246)，G 通道 249 而非 250。属 CairoSVG/PDF 渲染舍入，非纸色错误。不计缺陷。

### O3：头条标题 39.75pt，低于 SOP 阶梯下限 40pt 0.25pt（与验收版一致）
- DE 与已验收 W46-FR 版实测同为 39.75pt（53px）。模板级共性，非 de 单版偏差；视觉上标题清晰完整。不计缺陷。

### O4：col 3 事实框正文 21.5 单位 = 16.125pt，低于侧栏 16.5pt 下限 0.375pt（与验收版一致）
- P2–P5 手写事实框（`content34.py` 等，21.5 单位）。已验收 FR 版同类侧栏文实测 16.12pt。模板级共性，视觉清晰。不计缺陷。

### O5：译注（讲解层）15.375pt，高于 SOP 11.25–13.5pt 上限（与验收版一致）
- `gloss()` 用 20.5 单位；已验收 FR 版译注行实测同为 15.38pt（9 spans）。模板级共性，非 de 单版偏差。不计缺陷。

### O6：图注 14.25pt，高于 SOP 11.25–13.5pt 上限 0.75pt（模板级）
- `caption()` 用 19 单位；图注出处 15.5 单位 = 11.62pt 在范围内。模板级共性（W46 起即如此），视觉清晰；FR 版图注未单独取到可比样本，故不称“与 FR 一致”，仅记为模板级观察。不计缺陷。

### O7：头条第一段无首字下沉（与验收版一致）
- SOP §1.1 要求首字下沉；已验收 W46-FR 版同样没有。本轮不重列（第三轮已裁定）。

### O8：P8 图高测量澄清（非缺陷）
- FIX-LOG/KIT 称“PDF 实测图高 129.285pt”：该值是 slice 模式下未裁剪的放置框高（源图 1000×408，按宽覆盖 172.38 单位），可见高度仍为 build14 宣称的 140 单位（105pt），渲染图已证实图片未压扁。以后引用时建议区分“放置框高”与“可见高”。

### O9：KIT“591 entries”口径无法精确复现（不影响文件）
- `.text.md` 1185 行、非空行 593、空白行分隔块 593；591 = 块数 − 2（或为扣掉 2 个题头块的口径）。文件本身 SHA 已验一致，仅 KIT 该数字的定义不明，记一笔，不列缺陷。

---

## 未改动声明
- 未修改 core-de 任何文件：终验 SHA（印版 a51f785a…、网版 b27571ea…、.text.md 1c219c84…）与开工时一致；8 个 SVG 的 SHA 与 freeze 前一致，mtime 停在 2026-11-11 01:01–01:04（build14 产物时间）。
- freeze 复现与登记表重跑均在 scratch 副本内完成（`work/freeze-out/`）；未改 tools；未跑 insert.py、lint --write、git push/add/reset/stash；未碰 W43/W45/W46。
- 写入过程无 Disk quota / EPERM / ffmpeg 失败。
