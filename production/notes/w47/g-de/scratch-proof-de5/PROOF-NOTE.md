# 独立校对笔记 — 2026-W47 德文核心版 · 第五轮（build15 全量复校）

校对员：第五轮独立校对（叶子；与 de 核心 builder、de fix1 builder、de 各轮复校员均不同人）。只读不改：未改 core-de 内任何文件（终验 SHA 与开工时一致），未改 tools，未跑 insert.py / lint --write / git add/commit/push/reset/stash；未碰 W43–W46、其他目标语家庭。
校对时间：2026-11-11（EST 02:46 开工）。对象：`~/workspace/weekly-git/production/2026-w47/core-de/` build15，8 页，1462.5×2025pt。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de5/`（本笔记 + `GATE-LOG.md` + `work/` 下日志、渲染图、测量输出；另有 `probe1.txt`）。

## 开工探针（硬门禁，双通）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin`：通，`da0c4eb8d9a48d171a33574b380752e183286751`，rc 0。
- 真实文件写 `scratch-proof-de5/probe1.txt`：通。
- 无 Disk quota / EPERM。

## 结论：(a) 零问题，可（重新）定稿

**D-01 已修好（五处一致 + 全文 diff 仅一行）；D1–D6 逐项回归全部通过；150 题逐题验算、8 版逐版目视（自印刷 PDF 重渲染）、网页 P1/P8 目视、金句 8 条、徽章 141 枚逐页映射、禁词、VOL、P8 最小字号、全部机械门自跑——零缺陷。本轮即为一整轮全量校对零问题（SOP §8.4）。**

---

## 身份核对（与 KIT 登记逐字一致；fix1 称值仅交叉核对，亦一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de.pdf`（印刷） | 22,965,197 | `49beffc4223ede29674a3c70c341ec9fc04d2103eb632d1194e8ffcb31250607` |
| `Die-Lucerna-VOL4-de-web.pdf`（网页） | 2,044,855 | `9b63b413424caa99ed255c7b84dc8368df3ad39f1de956768bbe2353037c01a8` |
| `2026-w47-de-zh-cn.text.md` | 49,798 | `0952bc517e96351e505d4790237aa00d4ca36032763ec256d005d6eeec3c8b48` |

PDF：8 页，1462.5×2025pt。终验 SHA 与开工时一致，未改动。

---

## D-01 回归（独立实测）

- **新题干五处一致**：`"Am Montag öffnet in Köln der erste ___."` 各 1× —— 源码 `content34.py`、`.text.md` L389、P3 SVG、印刷文字层（print/web 各 1×）、网页文字层；P8 键区 `34. Weihnachtsmarkt（圣诞市场）` 不动（`.text.md` L1165、P8 SVG、印刷文字层）；REG n=34：page 3、A2、完成句子、key `Weihnachtsmarkt`、note `圣诞市场`（自跑登记表 `work/reg-de5.json`）。
- **旧题干全期 0 处**：`"Am Montag öffnen in Köln die ersten ___."`（带填空线）在源码、`.text.md`、8 张 SVG、print/web 文字层中均为 0。短串 `öffnen in Köln die ersten` 另有 3 处，均为正文原句复数形 `"Am Montag, dem 16. November, öffnen in Köln die ersten Weihnachtsmärkte"`（content34.py 1、content56.py 2、text.md 3，join 归一化计数）与 KIT §7 的修复记录引文——语法正确的复数句，非旧题干。
- **build14→build15 全文 diff 仅一行（自跑，不采信 builder 说法）**：fix4 的 `old-text-build14.md` SHA `1c219c84864ababa52c7a63985614f7cd54bb780913ccae43fff6890b393ce86` 与第四轮实测的 build14 值一致；与 build15 `.text.md` 的 diff 仅 L389 一行（题干）；P8 答案块全文一致。SVG 层佐证：freeze 逐页哈希与 build14 对照，7/8 页 byte-identical，仅 P3 变（`7dcdfe11…`→`1c2d4850…`），与单行题干改动一致。
- **补全句语法**：`"Am Montag öffnet in Köln der erste Weihnachtsmarkt."`——单数主谓一致，正确德语。
- **放大裁图**：P3 Q34 题干 3× 裁图（`work/crop-p3-q34.png`）单行干净，A2 徽章在位；P8 键 34（`work/crop-p8-q34key.png`）印刷干净无遮挡。

---

## D6 逐项回归（独立实测）

- 两新句均在文章段内（`.text.md` 严格口径 + 源码 `f.para` 核对）：P3 `Viele Kinder haben ihren Adventskalender schon zu Hause — aber das erste Türchen öffnet sich erst am 1. Dezember.`；P5 `In vielen Familien brennt im Advent eine Kerze auf dem Tisch, und auf dem Kalender leuchtet ein Stern.`（P5 句在 P5 渲染图上跨栏完整可读）。
- 词表框 12/12 在文章段内（严格口径，见“§8.1”）：P3 6/6（Adventskalender 1、Kerze 1 为复数 Kerzen）、P5 6/6（Kerze 1、Stern 1）。Q74/Q75 题面、键未动；P5 练习 B 标题 `WÖRTER AUS DEM TEXT` 有文章锚点。
- 两新句无新事实：P3 句与 P5 已有事实一致（首扇小门 12 月 1 日开）；P5 句为泛指生活描写，直接支撑 Q74/Q75。

## D1–D5 回归重测（全部通过）

### D1（题干字号）— 通过
- 自写脚本（`work/check_stems2.py`：AST 取全部 124 个 `ex()` 的第 5 实参题干，与各页 SVG `<text>` 首 20 字匹配；输出 `work/stems-de5.log`）：**124/124 命中，低于下限 0**。P1–P7 题干 22.0 单位 = 16.5pt；P8 20 题 20.5 单位 = 15.375pt。源码交叉核对：`bslib4.py` 含 `STEM_MIN = 22`、`STEM_MIN_P8 = 20.5`。
- 三处误匹配已逐一排除（非真问题）：P2 两处 18.0 是栏目标题行 `LEVEL A2　Der Buß- und Bettag & der Alltag`（与题干共享前 20 字前缀），题干本行实为 22.0（y=2022 / y=1912）；P3 一处 21.5 是 col 3 事实框行 `Die offizielle Eröffnung am Dom ist`（16.125pt 侧栏字），题干本行实为 22.0（y=2323）。三处均经 SVG 逐行 grep 确认。
- 栏高/溢出：run.py 重跑零 `FLOW OVERFLOW` / `HEAD TOO WIDE`；最紧仍 P6-ex 2523/2560、P1-quiz 2523/2560、P8-keys 2504/2560；P3-main 886/1560、P5-main 966/1080。

### D2（§8.1，P4 `die Ligaphase`）— 通过
- 严格文章段计数（`.text.md`，byline 后、译注行前）：das Tor 2、der Spieltag 3、torreich 1（`torreichste`）、die Ligaphase 1、weiterkommen 1（拆分形 `kommen weiter`，源码 1×）。**5/5 在正文。**

### D3（§8.1，P6 `die Buße`）— 通过
- 严格文章段计数：die Buße 1、das Kirchenjahr 2、der Verstorbene 1（`Verstorbenen`）、der Friedhof 1、der Haushalt 3（`Bundeshaushalt` + `jeden Haushalt` 等，与第四轮少计一致，结论不受影响）、die Einigung 1。**6/6 在正文。**Q97 与文章逐字对齐。

### D4（塞尔维亚场）— 通过（独立重查，不只信记录）
- 本轮独立检索（browser.search，2026-11-11；bundesliga.com、fussballnationalmannschaft.net、kicker.ch、gmx.ch、feverpitch.de、pressaris.gr、otisimveni.gr，均为 2026-11-10 报道）：UEFA 观众禁令 + €50,000 罚款（歧视性球迷行为），例外：15 岁以下儿童（教师/教练陪同）+ 50 名精选德国球迷可入场，预计约 5,000 人，55,000 座 Rajko-Mitić 球场“基本空着”；开球 **2026-11-13 周五 20:45**（`date -d` Europe/Berlin：13 日 = Friday ✓）；同组荷兰 8、希腊 8、德国 5、塞尔维亚 0；主教练 Jürgen Klopp。
- 四要素在位：P1 新导语含日期（13. November）、过去时（traf）、“vor fast leeren Rängen”、括号内例外（nur Kinder und 50 deutsche Fans）✓；`Serbien` 全期仅 3 处（P1 导语、P1 快讯、Q7 干扰项 A），P4 赛程表与 P5 周计划均无塞尔维亚场 ✓；旧句 `trifft Deutschland in Belgrad` / `Am Freitag (20.45 Uhr)` 全期已无（源码 + `.text.md` + 8 SVG 均为 0）✓；P7 工具箱同步句在位 ✓；11 月 16 日周一 20:45 对荷兰（柏林）与 P4 赛程表一致（16 日 = Monday ✓）。

### D5（P3 Q42）— 通过
- 新题干 `Wie viel früher als der erste Advent beginnen die Märkte?` 在 P3 渲染图、`.text.md`、P3 SVG、印刷文字层四处一致；旧题干 `Warum beginnen die Märkte vor dem ersten Advent?` 全期 0 次。
- 仅一解验算：A `Sie öffnen fast zwei Wochen früher.` 唯一时间跨度表述，与文章 `Die Märkte beginnen fast zwei Wochen früher.` 一致（市场 11 月 16 日开，将临期 11 月 29 日，相差 13 天 ≈ 快两周）；B、C 非时间跨度。**仅 A 可解** ✓。选项、键、注记不变（P8 键 `42. A`）。

---

## P8 徽章核实（逐页映射，级别与登记表逐键比对）

- 全刊 chip（SVG `rx="2.7"` 矩形计数）：**141**——P1 10、P2 15、P3 18、P4 15、P5 18、P6 18、P7 12、**P8 35**，与 KIT 一致。
- 逐页 chip 级别序列与 REG 比对（文档顺序；配对题共享一枚 chip，已折叠）：P1 10/10、P2 15/15（Q25–28 词汇配对共一枚 A2）、P3 18/18、P4 15/15（Q52–55 共一枚 B1）、P5 18/18、P6 18/18、P7 12/12、P8 35/35（Q141–144 共一枚 B1；完形 Q113–120 全 A2；对话条 145 A2、146 A2、147 A2、**148 B1**、149 A2；写作 Q150 B1）——**0 处不匹配**。

---

## 全量复校（每项都跑过）

### 全文精读
- `.text.md` 49,798 字节（42,392 字符，1185 行）逐行读完（P1–P8）。德语拼写、变格、变位、性数配合、标点未见错误；未见重复词、截断句；中文讲解层与德文对照无误。
- §8.1 全量（严格文章段口径，`work/check_gloss_strict.py`）：P1 4/4、P2 5/5、P3 6/6、P4 5/5、P5 6/6、P6 6/6，**全部在当版文章段内**；词表框 P3/P5 各 6/6（见 D6）。
- 事实与日期抽查：P2 日期加法 18+11=29、15+7=22、16+6=22 ✓；P3 `Vor fast 100 Jahren`（1930→2026 为 96 年 ✓）、市场 11 月 16 日–12 月 23 日且 22 日关闭与 Q40 键一致、正式开幕 17 日 19 点 ✓；P4 `4. Spieltag der Ligaphase`（3–4 日周二/周三 ✓）、第 9 轮总进球重算 4+3+3+7+4+1+3+2+3 = **30** ✓、9 场赛果全在赛程表 ✓；P5 1903 年日历“über 120 Jahre alt”（123 年 ✓）；P6 预算 11 月 27 日周五表决（27 日 = Friday ✓）、2,05 欧分与 Q91/Q127 一致；P7 纠错诊所 4 条全部正确；P7 下期预告 VOL.5 承诺与 KIT §9 一致。
- 日期星期（`date -d` Europe/Berlin）：3 日周二、4 日周三、5 日周四、6 日周五、7 日周六、8 日周日、13 日周五、15 日周日、16 日周一、17 日周二、18 日周三、20 日周五、22 日周日、24 日周二、25 日周三、26 日周四、27 日周五、29 日周日，全部核对 ✓。

### 150 题逐题复核（答案键逐题独立验算，尤其 P8 113–150）
- 登记表（独立复现，见“机械门”）：TOTAL **150**，按版 10/18/18/18/18/18/12/38，编号连续 1–150；级别 A2 69 / B1 67 / B2 14；题型与 KIT 一致（单选 52 / 完成句子 41 / 句型转换 11 / 判断对错 8 / 完形 8 / 造句 8 / 词汇配对 12 / 翻译 4 / 对话补全 5 / 写作 1）。
- P1（1–10）：1 Bundesliga、2 Niederlande、3 Sachsen、4 Totensonntag、5 fünf、6 29. November；7 B、8 A、9 B、10 B——全部与头版文章一致。
- P2（11–28）：日期题 11–15 全对（18 日周三 ✓）；Perfekt 16–20 全对；21 B、22 B（1995）、23 A、24 B；配对 25–28 键 d/c/a/b 与释义逐一相符。
- P3（29–46）：判断 29–33（R/F/R/F/R）与文章一致；填空 34–38（Weihnachtsmarkt/Glühwein/Lebkuchen/Advent/Weihnachtsbaum）与方框一致，**34 新题干与单数键主谓一致**；39 B、40 B、41 A、**42 A（仅一解，见 D5）**；造句 43–46 动词第二位全对。
- P4（47–64）：比分题 47–50 全对；51 B（荷兰 8、德国 5）；配对 52–55 d/b/c/a 释义逐一相符；比较级 56–59（mehr / später / früher / mehr）均与数据相符；时间题 60–63（20.45 / 20.30 / 18.30 / 17.30）与赛程表一致；64 B（3:1）✓。
- P5（65–82）：65 A、66 B、67 B、68 B、69 A；70–75（Türchen / Wunschzettel / Christkind / Schokolade / Kerze / Stern）与方框一致；weil 句 76–79 动词置尾全对；80 R、81 F、82 R ✓。
- P6（83–100）：图表题 83–88 全对（44+33=77、总和 100、23% 最小）；89 B、90 A、91 B、92 B；语法 93–96（wird / ob / geht / beginnt）；97–100（Buße / Kirchenjahr / Friedhof / Einigung）与文章一致，98 `des ___s` = Kirchenjahr + s（属格）✓。
- P7（101–112）：101 wird、102 werden、103 wird、104 A；105 stiller、106 weil、107 weil 句、108 A；109 ob、110 fraglich、111 `Ich finde, dass das Gedenken Stille braucht.`（dass 句动词句末）、112 B ✓。
- P8（113–150，逐题重算）：完形 113–120（A/B/A/B/A/A/B/A）——主语均为 Lena（第三人称单数现在时），干扰项复数/过去时均排除，**每题仅一解**；121–128（A/B/B/B/B/A/B/B）；阅读 129–132（A/B/B/B）与 Berger 短文逐句相符；造句 133–136 动词第二位全对；翻译 137–140（140 `Am Montag schaue ich zu Hause Deutschland gegen die Niederlande.` 第一人称 schaue ✓）；配对 141–144（c/a/d/b）释义逐一相符；对话 145–149（A/B/A/A/A，人称与对话一致）；150 开放题无固定键 ✓。
- 金句：8 条各恰 2×、逐字出自本期正文（verify.py 口径，scratch 副本内重跑：`verbatim OK: True`；8 条出处页码 Seite 1/1/2/3/5/4/6/6 与文章逐字核对一致）。
- 目录与跨版引用：P1 目录 S.2–S.8 与各版栏目/级别一致；`详见第 4 版`、`答案见第 8 版`等引用页码无误；页码行 8 版齐全 `第{n}版／共8版`。
- MUSTER 84 词（空白切分，独立重数）✓。禁用词扫描：`Geisterspiel / Karneval / Volkstrauertag / NFL / American Football / Tankrabatt / Hart aber fair / Klassiker / Allerheiligen / VOL.3 / VOL.2 / Le Lucerna / The Lucerna / 11.11 / 8,35 / 14,04 / ZEW` 全期 0 次（print 默认/-raw/web -raw 三份文本）；`VOL.5` 7 处全部为合法的下期预告/读者来信/写作框语境（逐处核对上下文）✓。

### 机械门（独立重跑，日志在 work/）
- `tools/occlusion_audit.py` 全 svg 目录（tools/venv 解释器）：**0 flags**，自检通过（6 类植入全触发、干净对照静默）。（`work/occlusion15-de5.log/json`）
- `tools/p8.py extract --p8 svg/p8-uebungen.svg --total 150`：**150/150**；`compare` 核心对自身：`status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]`。（`work/p8extract-de5.log/json`、`work/p8compare-de5.log/json`）
- **freeze 真跑**（`tools/freeze.py baseline`，tools/venv 解释器，与构建相同；`work/freeze-de5.log`）：rc 0，**8/8 SVGs byte-identical**，core integrity：交付 SVG 在运行前后未变。逐页哈希：p1 2b0a53ad…、p2 b354e140…、p3 **1c2d4850…**、p4 ba0f0505…、p5 710457f7…、p6 1f49f462…、p7 e5f5dc07…、p8 7814b613…——与 build14 对照仅 P3 变，其余 7 页不变。
- `run.py` 在 scratch 副本内重跑（`work/run-de5.log`，未动原目录）：rc 0，TOTAL 150，`FLOW OVERFLOW` 0 次、`HEAD TOO WIDE` 0 次；流终点与 KIT 一致（P3-main 886/1560、P5-main 966/1080、P6-ex 2523/2560、P1-quiz 2523/2560、P8-keys 2504/2560、P8-battery 1409/1555、P7 image ends 1541.83）。
- `verify.py` 在 scratch 副本内重跑（`work/verify-de5.log`）：rc 0，全绿——TOTAL 150、分版/级别/题型与 KIT 一致、编号连续、SVGs byte-identical after run、SOP §1.1 style audit True、旧式 hex []、金句 2×、禁词全空、头条 40 字（限 56）、图柱 748/561/391、MUSTER 84、日期加法全对、P8 答案下限 True。
- 登记表独立复现（`work/check_de5.py` 在副本内跑同款顺序；`work/reg-de5.json`）：TOTAL 150；by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；levels A2 69 / B1 67 / B2 14；types 与 KIT 一致；numbering continuous True；Q34 key `Weihnachtsmarkt`（A2）。
- 文字层：`pdftotext` 默认模式 print/web 各 **50,498 字节**，词多重集相同（7,235 token）；`-layout` 模式归一化词序完全相同（0 处差异块）；`-raw` 模式各 49,381 字节，**逐字节相同**（`cmp` 通过）。web PDF 带真实文字层，2,044,855 字节 < 7MB。默认模式归一化文本仅 P6 图表区一处块顺序差异（poppler 分组，词多重集相同；KIT 已披露同类差异）——见观察项 O10。
- P8 最小字号实测 ≥9.75pt：PyMuPDF 实测 P8 最小 span **10.12pt**；其余各版最小 11.62–12.75pt（P1/P3/P4/P5/P7 11.62，P2/P6 12.75）。
- P6 图柱：SVG 橄榄绿矩形宽 748/561/391 ✓；图表 44+33+23=100 ✓；ÜBUNGSDATEN 标注在位。

### §1.1 逐项实测
| 项 | SOP 要求 | DE build15 实测 | 结论 |
|---|---|---|---|
| 版数/答案 | 8 版，答案在 P8 | 8 页，答案 P8 | ✓ |
| 纸色 | #fbfaf6 | SVG rect #fbfaf6（verify.py style audit True） | ✓ |
| 墨/正文/说明/细线/书衣绿/橄榄绿/鹅黄/米白/浅底 | #302c28/#3a3631/#6f675d/#d8d2c4/#37402f/#46581f/#f6e08e/#f4efe1/#f0eee5 | `svglib.py` 常量与之一致；旧式金色 hex 全期 0（verify.py） | ✓ |
| 徽章三色 | A2 #5c6e30 / B1 #46581f / B2 #37402f | `bslib4.py` LV_COLOR 一致；PDF 内 chip 填充与之一致 | ✓ |
| 刊头 | 147pt，UnifrakturMaguntia | P1 SVG 与 build14 byte-identical，刊头未变（见 O3 观察） | ✓ |
| 刊别 | 27pt / 700 | 27.0pt 粗体（verify.py 日志） | ✓ |
| 导读条/栏目条标题 | 34.5–37.5pt | P1 导读条 34.5pt、P2 栏目条 34.5pt | ✓ |
| 头条标题 | 40–45pt | **39.75pt**（= FR 39.75；见 O3） | 观察 |
| 次级标题 | 22.5–24pt | 24.0pt（P2–P6 各版头） | ✓ |
| 头条正文 | 18–19pt | 24 单位 = 18pt | ✓ |
| 侧栏正文、练习题干 | 16.5–17.5pt | 题干 16.5pt ✓；侧栏事实框 16.125pt（见 O4） | 观察 |
| 栏目小字 | 12.75pt | 12.75pt（顶栏/页脚） | ✓ |
| 讲解层、图注、说明 | 11.25–13.5pt | 译注 15.375pt（见 O5）；图注 14.25pt、图注出处 11.62pt（见 O6） | 观察 |
| 答案 | 让步顺序，最低 ≥9.75pt | 10.12pt（让步第 4 步，未扩版） | ✓ |
| 线条与版心 | 无双线外框；版心上 54/左右 66/下 48pt | 无描边双线框；MX 88px=66pt、band top 72px=54pt（源码 + 渲染确认） | ✓ |
| 排字 | 全角空格分隔；`第N版／共8版` 无空格 | 页脚/页码行/刊别均为全角空格；`VOL.4` 刊头 9 处式样正确 | ✓ |
| 字体 | Newsreader（拉丁）/ UnifrakturMaguntia（刊头）/ Noto Sans CJK（中文） | PDF 内嵌字体与 build14 一致（P1/P8 除外 SVG 均未变；P3 只改一行题干，无新字体） | ✓ |
| VOL 号 | 台账 VOL.4 | 刊头/页脚/刊别均为 VOL.4（raw 文本 8 处，每版页脚 1 处）；VOL.3 0 处；VOL.5 仅预告语境 | ✓ |
| P8 题干 | 让步 15.4pt | 15.375pt（20.5 单位，20/20） | ✓（已裁定现值） |

### 8 版逐版看图（自 build15 印刷版 PDF 每页 110dpi 重新渲染，`work/pg-1.png` … `pg-8.png`，逐版目视；另看网页版 P1/P8 `work/web-p1-1.png`、`work/web-p8-8.png`，与印刷一致）
- P1：新导语完整无溢出；头条、数字栏、即学即练、快讯、闪电问答齐全；页脚/页码行齐全。无问题。
- P2：练习区完整，配对块落位，Rechnen 横线间隔清晰。无问题。
- P3：Q34 新题干单行在位（放大裁图确认）、D6 新句在位、Q42 新题干在位、选项齐全；画作图注与出处齐全；词汇框含 Adventskalender。无问题。
- P4：`Spieltag der Ligaphase` 在位；赛程表 9 场齐全、仅 Mo 16.11. 荷兰场，无塞尔维亚场；Und-Sie 框中德文齐全；赛程表脚注只列欧联赛事，Freiburg–Twente 属欧协联未列入，不属遗漏。无问题。
- P5：D6 Kerze/Stern 句在位；周计划 Mo 16.11.–Fr 20.11.，无塞尔维亚场；1903 日历图注与出处齐全；练习 B 方框含 Kerze/Stern。无问题。
- P6：图表 44/33/23 完整、ÜBUNGSDATEN 标注在位；Q100 落在页脚上方留空处。无问题。
- P7：工具箱新译注完整；金句 8 条、诊所 4 条、读者来信编辑示例标识清晰；VOL.5 预告在位。无问题。
- P8：完形/问答/阅读/造句/翻译/配对/对话完整；徽章条 145–149 齐全且级别正确（148 B1 底色 visibly 更深）；1905 图 + 图注与写作横线间隔清晰；MUSTER 清晰；答案键四栏完整，均在页脚上方结束，末行与页脚线有清晰间距。无问题。

### 图片许可与署名（逐张核对 assets/CREDITS.md，build10 以来无改动；P1/P8 除外 SVG 均未变，P3 只改一行题干）
- P1 fussball.jpg（DVIDS 333458，PD）、P4 kopfball.jpg（DVIDS 333408，PD）、P3 weihnachtsmarkt1930.jpg（Ritter 1860–1948，PD）、P5 christkind.jpg（Kepler 1903，PD）、P7 lesesaal.jpg（Highsmith，国会图书馆，PD）、P8 fussball1905.jpg（1905 年，作者不详，PD）——印署与 CREDITS 一致，未见版权不明肖像。

### ABSTRACT.txt
- 单行、无 ASCII 双引号、简体中文；含刊名、目标语名、A2–B2 分级、150 道练习与本期真实主题（德甲回归、欧国联荷兰、忏悔祈祷日与亡灵主日、科隆市场、11 月 3–8 日赛果），与 KIT §5 逐字一致 ✓。296 字节。

### P7 读者来信（F-MAIL）
- 明确标明编辑示例（`Ein Beispiel der Redaktion!` + 截稿未收到真实来信、见 VOL.5，中德双语）✓；无编造来信；承诺顺延 VOL.5 ✓；未查邮箱。

### KIT 核查（build15 数值逐项）
- §5 交付物：字节与 SHA 与本轮实测一致（print 22,965,197 / 49beffc4…、web 2,044,855 / 9b63b413…、.text.md 49,798 / 0952bc51…、42,392 字符、150 题）✓；ABSTRACT 逐字一致 ✓。“591 entries”口径仍无法精确复现（见 O9，文件本身 SHA 已验）。
- §6 门禁：与本轮独立重跑一致（occlusion 0、p8 150/150 + CLEAN、题干字号、文字层 50,498 字节、P8 最小 10.12pt、栏高终点、图柱、MUSTER、freeze 8/8 本轮真跑）✓；freeze 8/8 由本轮真跑（build14 日志曾为空的问题已解决，见 GATE-LOG）。
- §7：D-01 修复说明与实测相符（只改题干一行、键不动、全文 diff 仅 L389）；D1–D6 记录与本轮重测相符 ✓。
- §8：O1 已记入（见下节）；短缺项（无真实来信、13/15/16 日赛事仅为预告、图表为练习数据、P8 字号让步、无首字下沉）与实测一致 ✓。
- §9 VOL.5 承诺：逐项已核实（29 日周日首个将临期、24–26 日欧战、11. Spieltag、圣诞市场、真实来信）✓。

---

## O1 复核（不列缺陷，按协调员裁定）
- 实测字号不变：P8 完形段落与对话段落 19.5 单位 = 14.625pt、选项行 18.5 单位 = 13.875pt，与 build10/14 一致（P8 SVG 哈希与 build14 相同，未变）；P8 渲染图上该两段落与选项行清晰可读，无溢出、重叠、无法辨认等新的读者可见问题。属继承结构（W46-DE 即为 18.5 单位）、模板级问题，本次不修。**不重新列为缺陷。**

---

## 观察项（不计缺陷，留协调员知悉；O2–O9 与第四轮相同，因 7/8 SVG 与 build14 byte-identical、P3 仅改一行题干，数值未变）

### O2：渲染采样纸色 G 通道差 1（与第三、四轮相同）
- SVG 纸面 rect 填色确为 `#fbfaf6`；72dpi 采样 (251,249,246)，G 通道 249 而非 250。属 CairoSVG/PDF 渲染舍入，非纸色错误。不计缺陷。

### O3：头条标题 39.75pt，低于 SOP 阶梯下限 40pt 0.25pt（与验收版一致）
- DE 与已验收 W46-FR 版实测同为 39.75pt（53px）。模板级共性，非 de 单版偏差；视觉上标题清晰完整。不计缺陷。

### O4：col 3 事实框正文 21.5 单位 = 16.125pt，低于侧栏 16.5pt 下限 0.375pt（与验收版一致）
- P2–P5 手写事实框（21.5 单位）。已验收 FR 版同类侧栏文实测 16.12pt。模板级共性，视觉清晰。不计缺陷。

### O5：译注（讲解层）15.375pt，高于 SOP 11.25–13.5pt 上限（与验收版一致）
- `gloss()` 用 20.5 单位；已验收 FR 版译注行实测同为 15.38pt。模板级共性，非 de 单版偏差。不计缺陷。

### O6：图注 14.25pt，高于 SOP 11.25–13.5pt 上限 0.75pt（模板级）
- `caption()` 用 19 单位；图注出处 15.5 单位 = 11.62pt 在范围内。模板级共性（W46 起即如此），视觉清晰。不计缺陷。

### O7：头条第一段无首字下沉（与验收版一致）
- SOP §1.1 要求首字下沉；已验收 W46-FR 版同样没有。本轮不重列（第三轮已裁定）。

### O8：P8 图高测量澄清（非缺陷）
- 沿用第四轮澄清：PDF 内图片放置框 316.88×129.29pt 是 slice 模式下未裁剪的放置框高，可见高度仍为 140 单位（105pt），渲染图已证实图片未压扁。

### O9：KIT“591 entries”口径无法精确复现（不影响文件）
- `.text.md` 1185 行、42,392 字符；文件本身 SHA 已验一致，仅 KIT 该数字的定义不明，记一笔，不列缺陷。

### O10（本轮新增）：默认模式 print/web 归一化文本在 P6 图表区有一处块顺序差异
- `pdftotext` 默认模式归一化后，print 与 web 在 P6 图表区词序不同（print：`… 读者最关心什么？ 44 % Bundesliga und Nations League 足球 …`；web：`… Bundesliga und Nations League 足球 … 读者最关心什么？ 44 % 33 % 23 % …`），属 poppler 块分组差异；词多重集相同（7,235 token），`-layout` 模式归一化词序完全相同，`-raw` 模式逐字节相同。KIT §6 称默认模式“仅一行断行差异”，措辞不够精确，但实质（同词、poppler 分组）与披露一致。不计缺陷。

---

## 未改动声明
- 未修改 core-de 任何文件：终验 SHA（印版 49beffc4…、网版 9b63b413…、.text.md 0952bc51…）与开工时一致；8 个 SVG 的 SHA 与 freeze 前一致。
- run.py / verify.py / freeze 复现均在 scratch 副本内完成（`work/copy-de5/`、`work/freeze-out/`）；未改 tools；未跑 insert.py、lint --write、git push/add/reset/stash；未碰 W43/W45/W46。
- 写入过程无 Disk quota / EPERM 失败。
