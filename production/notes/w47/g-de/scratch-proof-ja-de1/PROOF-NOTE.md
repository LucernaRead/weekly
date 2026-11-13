# 校对笔记 — 2026-W47 ja-de（第一轮独立复校）

- 校对员：叶子（第一轮，与 builder / core-ja builder / 各轮复校员不同人）
- 日期：2026-11-11（EST 00:26 开工）
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-de/`（未入仓，未追踪）
- 依据：SOP.md §8、§1.1；AGENTS.md；KIT（`WEEKLY-KIT.md`）；core `2026-w47-ja-zh-cn` 全文逐行对照
- 结论：**(b) 缺陷清单 — 3 条，不能定稿**。按 SOP §8.4，修复构建源码、整期重渲染后，须从头再做一轮全量校对。

## 0. 身份复核（先核身份，通过）

| 文件 | 字节 | SHA-256 | 结果 |
|---|---|---|---|
| `Lucerna-VOL4-JA-DE.pdf`（印刷） | 29,102,629 | `b5d66e17d9ac29b6362d934e65a254a1bb63df5ea00ed305ce1b362cea06a239` | 与任务给定一致 |
| `Lucerna-VOL4-JA-DE-web.pdf`（网页） | 4,483,732 | `c55dd68cfcd6f0acc4cad79987a7ceb7fbe4c86d83cdf637c86c795497aff26a` | 与任务给定一致 |

- 两 PDF 均为 8 页，1462.5 × 2025 pt。
- 开工探针双通：`git hash-object -w --stdin` 成功；`hidden_files/w47/scratch-proof-ja-de1/.probe` 真实写盘成功。

## 1. 缺陷清单（3 条）

### D1 — 人名罗马字拼错：藤凌駕写成 `Fujiryūga`（应为 `Fujiryōga`）

- 位置：P8 答案简析 5 处——
- key 49：`Fujiryūga schlug Hōshōryū an Tag 3`
- key 54：`Fujiryūgas kinboshi: 11. Turnier seit dem Debüt`
- key 63：`Fujiryūga holte an Tag 3 einen kinboshi`
- key 111：`Fujiryūgas kinboshi: 11. Turnier seit dem Debüt`
- key 116：`Hōshōryū verlor an Tag 3 gegen Fujiryūga`
- 原文（SVG `p8-tesuto.svg` 与印刷 P8 渲染图均已目视确认）：`Fujiryūga` / `Fujiryūgas`。
- 应为：`Fujiryōga` / `Fujiryōgas`。
- 证据：
- 凌駕读作 りょうが（ryōga），不是 りゅうが。Wikipedia `Fujiryōga Masaharu`（藤凌駕 雅治）明文：shikona **Fujiryōga**，combining … the name Ryōga (凌駕）；并确认“On the third day of the November 2026 tournament, Fujiryōga earned the first kinboshi of his career by defeating yokozuna Hōshōryū”（事实本身与本期 P4 一致，错的只是罗马字元音 ū→ō）。
- 日文正文（core 冻结）只写汉字 藤凌駕，未给读音；罗马字是 fan-out 层自加的，责任在 fan-out 层。
- 影响：键值本身（A / 11 / ○）不受影响，但 5 条答案简析把一个真实人物的名字拼错，学习者会记住错误罗马字。

### D2 — 人名罗马字读错：美ノ海写成 `Umi-no-umi`（应为 `Churanoumi`）

- 位置：P8 答案简析 key 48（1 处）：`Umi-no-umi verlor an Tag 1 gegen Hōshōryū`。
- 原文（SVG 与印刷 P8 渲染图均已确认）：`Umi-no-umi`。
- 应为：`Churanoumi`（`Churanoumi verlor an Tag 1 gegen Hōshōryū`）。
- 证据：
- 该力士为 美ノ海 義久，读音 ちゅらのうみ（Churanoumi）：sumo-guide.com「美ノ海（ちゅらのうみ）」「美ノ海 義久（ちゅらのうみ よしひさ）」；Daily Sports 2026-10-27「美ノ海義久（ちゅらのうみ・よしひさ）」；九州场所初日战报 tachiai.org / sumojapones.com：`Hoshoryu (1-0) oshidashi K1e Churanoumi (0-1)`。
- `Umi-no-umi` 是对汉字 美之海 的字面误读（美=umi、之=no、海=umi）；日文正文写的是 美ノ海，core 中文简析写“美之海”只是“之”作“ノ”的通用转写，不能据此拼出 Umi-no-umi。
- 事实本身正确（初日败给丰升龙的是美ノ海），错的只是名字读音。
- 影响：同 D1，键值（B）不受影响，简析人名错误。

### D3 — 德语语法错误：P7 易错诊所第 4 条 `im ます-Form`（应为 `in der ます-Form`）

- 位置：P7 右栏「まちがい診療所 Fehlerklinik」第 4 条末句，SVG `p7-kotoba.svg` 原文：`Das Verb im ます-Form beenden.`（P7 渲染图目视确认）。
- 应为：`Das Verb in der ます-Form beenden.`（`Form` 为阴性，`die Form` → `in der Form`；`im` = `in dem`，只配阳/中性）。
- 证据：全版其余 `im` 用法均正确（`im November`、`im September`、`im Fukuoka Kokusai Center`——November/September 为阳性，Center 为中性），仅此一处冠词性别错误；其余 3 条诊所简析均正确（`Mit 「昨日」 steht das Verb in der Vergangenheit.` / `Zum Substantivieren eines Verbs 「こと」 anhängen.` / `Für den Ort des Kaufens steht 「で」.`）。
- 影响：意思仍可理解，但错误出现在“教语法”的栏目里，且是德语讲解层自身的语法错误。

## 2. 已核实无问题（方法与结果）

### 2.1 全量文本复校（core 逐行 diff，全 150 个差异块逐块审读）

- core `2026-w47-ja-zh-cn.text.md`（1356 行）vs de `2026-w47-ja-de.text.md`（1376 行）：差异块 150 个，**全部为讲解层（中文→德文）或版式家具（页脚 `Seite N von 8`、页眉）**；日文目标语正文零改动。
- 讲解/界面语言确为德文：页脚 `JAPANISCHE WOCHENZEITUNG VOL.4　Japanischer Text　Deutsche Erklärungen`；练习类型标签 `Ausfüllen / Auswahl / Lückentext / Zuordnen / Satz bilden / Richtig/Falsch / Übersetzen / Schreiben`；P8 头 `答え　Antworten — nach Seiten geordnet; einfach die Nummer suchen`。
- 练习小节头冻结为日语：P1–P8 的 `A 理解 / B ことば / C 数字と日付 / D ペアにしましょう / 文を作りましょう / 正しい・正しくない / 文を完成しましょう / 読んで答えましょう / 文を作りましょう / 週のクロニクル / 一般問題 / 書いてみましょう` 等均未动。
- §8.1 讲解词真实性：全部 `Anm.` 注释头词均在其所在页正文中出现（机械核查：0 缺失）；P7 术语表 10 词（酉の市/熊手/手締め/一番太鼓/見頃/解禁/りくりゅう/ちいかわ/ノミネート/金星）均在正文中。

### 2.2 150 题逐题验算

- 登记（本次 `run.py` 重跑，见 §4）：TOTAL 150；级别 A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；题型 Ausfüllen 50 / Auswahl 51 / Zuordnen 12 / Satz bilden 8 / Richtig/Falsch 11 / Lückentext 13 / Übersetzen 4 / Schreiben 1——与 KIT §1 登记逐项一致。
- `tools/p8.py extract`：noted set 150/150；`compare` vs core：status **CLEAN**，missing=[]、extra_count=0、uncertain=[]、**keydiff=[137, 138, 139, 140]**（与预期一致）。146 条键值与 core 字节一致。
- keydiff 4 条逐条核实原因（均为 E 组翻译题答案由中文译成德文，翻译正确）：
- 137：core `二之酉在11月19日。` → `Ni-no-tori ist am 19. November.` ✓
- 138：core `新酒在11月19日解禁。` → `Der neue Wein erscheint am 19. November.` ✓
- 139：core `流行语提名在11月5日发表。` → `Die Schlagwort-Nominierungen wurden am 5. November bekannt gegeben.` ✓
- 140：core `去看红叶的人应该同时确认预报日期和现在的状况。` → `Wer das Herbstlaub sehen will, sollte sowohl die Prognosedaten als auch die aktuelle Lage prüfen.` ✓
- 算术验算：图表 38/24/22/16 合计 100 ✓；key 91（38−24=14）✓；key 92（38+24=62）✓；key 89/90（38/24）✓。
- 星期验算（`date -d`）：11月19日周四、22日周日、23日周一、7日周六、5日周四、12月1日周二、8日周日、13日周五、10月29日周四、11月29日周日、12月4日周五、12月12日周六、21日周六——与版内全部断言一致。
- 相扑事实（独立于 D1/D2 的名字拼写）：初日大の里败给義ノ富士 ✓、初日豊昇龍胜美ノ海 ✓、3日目藤凌駕胜豊昇龍首获金星 ✓（tachiai.org 初日战报、Wikipedia Fujiryōga 条目）；“初土俵后第 11 个场所”“年 6 场所制以来第 7 快”与 P4 正文一致。
- 题干↔答案抽查（覆盖各版）：65–68、77、83–86、101、105–106、110、113–132、133–136、141–150 均与题干一致；141–144 配对（熊手→c、解禁→a、金星→d、見頃→b）与 P8 F 区选项一致。
- 范文 154 字：实数 154 字（`私の11月の1週間は…楽しい季節です。`），与 core 字节一致，与 P8 标注一致。

### 2.3 金句 8 条

- 8 条日语句逐字与 core 相同（在 de P7 SVG 中逐条核实存在）；德文 gloss 与页码标注 `(S. 1/2/3/4/7)` 均与句子出处一致。

### 2.4 徽章、VOL、版式

- 级别徽章标签（`>A2< / >B1< / >B2<`）逐页：P1 14（11/2/1）、P2 15、P3 15、P4 18、P5 18、P6 18、P7 12、P8 35——**与 core 逐页完全一致**（P1 多出的 4 个 A2 为词卡级别标、配对组共用徽章等冻结行为）。
- VOL.4：每版页脚 1×；P1 另有刊头/版名共 3×；VOL.3 仅 P4 前号注 1×、VOL.5 仅 P4 次号预告 1×与 P7 来週 2×——均为 core 冻结的文章内文，符合 KIT §1 说明。
- `Seite N von 8` 每版 1×；`·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×；禁用金色 `#c9a227` 0×。
- P8 最小字号 9.98pt（PyMuPDF 实测，≥9.75pt 门槛；KIT 称 9.975pt，吻合）；P8 题干 10.35pt（79 处）未动。
- 8 版印刷 PDF 逐版目视（从印刷 PDF 新渲染，非 builder 的图）+ 网页 P1/P8 目视：无溢出、无重叠、无压页脚；P2 词卡首条 gloss `Bambusrechen für florierende Geschäfte` 已为单行（F3 修复目视确认）；P7 teaser 末端 y=2554.62（页脚 2580，25px 余量）；P8 练习流末端 y=531、答案流末端 y=2382（底 2540，158px 余量）。非页脚文字 y>2580：0 处。
- 图片出处：P1 `Foto: Poliphilo — CC0 (Wikimedia Commons)`、P3 `Foto: Alainauzas — gemeinfrei (Wikimedia Commons)`、P5/P8 `Foto: lumoplank — CC0 (Wikimedia Commons)`、P7 `Foto: Mozzucu — CC0 (Wikimedia Commons)`，均与 core 一致。
- ABSTRACT.txt 为德文，含 Tori-no-ichi、Beaujolais Nouveau、Sumo、30 Nominierungen、Arashiyama、A2–B2、150 Übungen。

### 2.5 翻译层专项

- `ちいかわ`：`Chiikawa`（P7 1×、P8 3×、text 4×）；中文 `吉伊卡哇` 全版 0×（SVG + text.md）。
- `りくりゅう`：romaji `ryuuryuu`（P7 1×、P8 4×、text 5×）。
- 中文残留：全量扫描 `参考答案 / 酉之市 / 提名 / 吉伊卡哇 / 中文 / 中国 / 练习 / 答案 / 解释 / 单词 / 语法 / 阅读` 在 SVG 与 text.md 中均为 0×；更强的字符集核查：de 文本引入的汉字集合 − core 汉字集合 = **空集**（de 未引入任何 core 没有的汉字）；core 的 263 个纯中文汉字已全部清零。唯一有意保留的“中文原文引用”：无（本期无此类引用；所有汉字均为日文正文用字）。
- 221 键：map 文件缺失（见观察项 O5），无法直接数 map 键；以效果验证代替——core↔de 全量 diff 的 150 个差异块已覆盖全部讲解字符串，无一遗漏、无一日文改动、无一中文残留。
- 其余罗马字抽查无误：Ōnosato、Hōshōryū、Yoshinofuji、Miura Riku、Kihara Ryuichi、Miyajima、Fukuoka Kokusai Center、Hanshin Umeda、Shōsetsu、kinboshi、kumade、Tori-no-ichi、Ni-no-tori、Ichi-no-tori、Weathernews。

### 2.6 U+2019 缺陷类回归

- 8 个 SVG 中 U+2019 总数 **0**；text.md 中 0。
- 另查：ASCII 撇号 `'` 0×；德文弯引号 „ “（U+201E/U+201C）0×——本版德文注释用日文 「」 引注，无任何撇号/弯引号字符可供渲染出错；目视抽查 P1 Anm.、P7 诊所等含引号的行，无宽字形断裂。

### 2.7 P8 题干与答案

- P8 题干 10.35pt 不动（已记录的 adjudication，不列缺陷）✓；答案最小 9.98pt ≥ 9.75pt ✓。

## 3. 观察项（不计缺陷）

- O1（core 侧，非 de 缺陷）：core P8 key 47 中文简析写“一之富士”，key 115 写“义之富士”，日文正文为 義ノ富士——key 47 疑为 core 中文笔误（义→一）。de 两处均正确译为 `Yoshinofuji`，fan-out 处理无误；提请 core 侧另行注意，本轮不计 de 缺陷。
- O2：同一词两种德译——P1 Anm. `一番太鼓 = die erste Trommel` vs key 27 `一番太鼓 = die Mitternachtstrommel`；两种译法各自成立，只是不一致。
- O3：P7 B2 术语表 `金星 kinboshi` 仅给罗马字、未给德译（同栏其余词均有德译）；但该词在同版正文、P4 注释与答案简析中均有解释，属可接受的术语保留。
- O4：`Fujiryūgas` 属格形式随 D1 一并改，不另计。
- O5（资料缺失）：任务要求先读的 `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md` 在 clone 中不存在（`hidden_files/w47/` 下只有 `scratch-proof-ja-de1/` 与 `scratch-proof-ja-en1/`）；`map-de.json`、`apply.py`、构建日志（`build-de-run6.log`、`de-sha-run5/6.txt`、`de-p8*.json` 等）均随该目录缺失。本轮的 221 键核查与构建解释器确认因此只能以 KIT §9 + 全量 diff 效果验证代替（见 §2.5、§4）。
- O6：fan-out 目录 `production/2026-w47/fanout-ja/2026-w47-ja-de/` 在 git 中完全未追踪（`??`），insert 尚未执行——属协调员步骤，非内容问题。
- O7：P8 key 92 简析为 `38+24=62`、key 65 为 `30 Nominierungen am Donnerstag, 5. November`，均为 F2 缩短方针下的电报体，算术/事实无误，不计缺陷。
- O8：P3 `D ペアにしましょう` 节头在第 2 栏底、条目在第 3 栏——与 P2 同构的冻结版式，非缺陷。

## 4. 机械门（自跑结果，详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| 身份（双 PDF 字节 + SHA-256） | 通过，与给定值一致 |
| `run.py` 重跑（`tools/venv/bin/python`，拷贝目录中运行，未动原件） | exit 0，FLOW OVERFLOW / HEAD TOO WIDE 0 条；登记与 KIT 一致 |
| freeze（原 SVG vs 重跑 SVG 直接 sha256） | 8/8 字节一致 |
| occlusion（`tools/occlusion_audit.py`，自检通过） | 0 flags |
| p8 extract（`tools/p8.py extract --total 150`） | 150/150 |
| p8 compare（vs core） | CLEAN，keydiff=[137,138,139,140]（4 条原因已逐条核实，见 §2.2） |
| print/web 文字层 | `pdftotext` 字节一致（105,188 字节） |
| P8 字号（PyMuPDF） | 最小 9.98pt；题干 10.35pt |

## 5. 工作文件

- 本笔记：`hidden_files/w47/scratch-proof-ja-de1/PROOF-NOTE.md`
- 门日志：`hidden_files/w47/scratch-proof-ja-de1/GATE-LOG.md`
- 扫描与门输出：`scan1.txt`–`scan7.txt`、`de-p8-proof1.json`、`de-p8compare-proof1.json`、`de-occlusion-proof1.json`、`rerun-log.txt`
- 重跑拷贝：`rerun/`（构建源码拷贝 + 重跑生成的 SVG，含 `rerun/svg/`）；渲染图：`render-print/p-*.png`（印刷 8 版）、`render-web/p1-1.png`、`p8-8.png`
- 未改动任何成品、源码或仓库状态；未跑 `insert.py`、`lint --write`；未 git add/commit/push。
