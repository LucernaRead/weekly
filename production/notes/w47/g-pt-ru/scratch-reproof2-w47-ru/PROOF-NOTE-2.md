# PROOF-NOTE-2 — W47 ru 家庭第二轮独立重校

- 校对员：第二轮独立重校员（全新工人，与建造者、修复者均不同，SOP §8/§8.4）
- 日期：2026-11-12
- 范围：`production/2026-w47/` 内 ru 家 **11 版**：core-ru + 10 个 `2026-w47-ru-*` fan-out（en/de/es/fr/it/pt/nl/ja/ko/zh-tw）。`production/2026-w47/` 下另有 11 个 `*-ru` 目录（de-ru、en-ru、…、zh-tw-ru）属于其他目标语家庭，**不在本任务范围**；若父协调员原意包含它们，需另派任务。
- 前置已读：`~/workspace/weekly-git/SOP.md` 全文（重点 §8）；第一轮 `scratch-reproof-w47-ru/PROOF-NOTE.md` 全文；`scratch-fix-ru/FIX-LOG.md` 全文。
- 约束遵守：只读生产文件，未改任何生产文件；未 commit、未 push、未跑 lint；解释器一律 `tools/venv/bin/python`；tools git HEAD `b9ac29a6`。磁盘开工 94G、收尾 95G（<100G 门限）。
- 本 scratch 目录：`hidden_files/w47/scratch-reproof2-w47-ru/`（门禁日志/JSON、pdftext/、diffs/、visual/、census.py、inventory.txt）。

## 总体结论：有问题，仅 low，6 项；无 MAJOR、无 MEDIUM

- 发现总数 **6**，全部 low：G-1（ru-en）、G-2（ru-de）、G-3（ru-de）、G-4（ru-de/fr/it/nl/pt + ru-ko 变体）、G-5（ru-nl）、G-6（ru-zh-tw）。
- 逐版结论：core-ru、ru-es、ru-ja **干净**；ru-en、ru-fr、ru-it、ru-pt、ru-ko、ru-zh-tw 各 1 项 low；ru-de 2 项 low；ru-nl 2 项 low。
- 机械门禁全部通过（见 §3）：p8 10/10 CLEAN、occlusion 11/11 零标记、boxtitle 11/11 零缺陷、D5 普查 CJK+Latin/CJK+Cyrillic 均为 0、弯引号全部 Newsreader、P8 最小字号 11 版均为 9.75pt（恰达 SOP §1.1 底线）。
- FIX-LOG 所称修复已逐版核实（见 §4）：F-2 在版（11/11）；22 个 PDF SHA 与 FIX-LOG 一致、未变动；9 处回补标题行全部在位。F-1、F-3 按任务要求不重报（F-1 未重测，沿用第一轮结论；F-3 本轮仅在 core P8 目视中确认 Morozko 图在版，未逐版复核）。

## 1. 发现表（全部 low）

| 编号 | 严重度 | 位置 | 证据原文 | 说明 |
|---|---|---|---|---|
| G-1 | low | ru-en text.md L99（P2 词汇注）及印 PDF 同处 | `родина home town` | родина = 故乡/祖国；hometown 应为 родной город。其余 9 版均译为 Heimat / tierra natal / pays natal / terra natale / 故郷 / 고향 / geboortestreek / terra natal / 故鄉，唯 en 版偏离。印 PDF 文字层亦含 `home town`（1 处），非仅 text.md 问题。 |
| G-2 | low | ru-de text.md L35（P1 即学即练标题）及印 PDF 同处 | `## СЕЙЧАС ВЫ · JETZT SIE` | 不合德语（字面“现在你”）。其余 9 版均为自然标题：TRY IT NOW / AHORA TÚ / À VOUS / TOCCA A VOI / NU U / AGORA VOCÊ / さあ、あなたも / 지금, 여러분 차례 / 即學即練。 |
| G-3 | low | ru-de text.md L512（P7 A2 栏小结）及印 PDF 同处 | `мокрый снег Schneeregen` | 与本版内 4 处一致的 `nasser Schnee` 矛盾（text.md L170/L515/L691/L786；印 PDF 另有 key 126 `Regen mit Schneeregen`）。Schneeregen 本身是可辩护的天气译法，缺陷在**同一俄语词在同一版内两个德语对应词**（语言学习报纸一词一译）。 |
| G-4 | low | ru-de/fr/it/nl/pt text.md L125 与 L129（P2「А ВЫ?」栏）；ru-ko 同栏变体 | de `UND SIE? / Und du?`；fr `ET VOUS? / Et toi?`；it `E VOI? / E tu?`；nl `EN U? / En jij?`；pt `E VOCÊ? / E tu?` | 标题正式体、说明非正式体混用。pt 另在 L471 用 você 式 `Responda`，与 L129 `Escreve`（tu 式）再混一次。ko 变体：L125 `당신은요?`（单数）vs L129 `여러분은요?`（复数）。es/ja/zh-tw/en 无此问题（es 始终 tú；ja 敬语一致；zh-tw/en 无敬语区分）。含义不受影响，属系统性 fan-out 模式。 |
| G-5 | low | ru-nl text.md L137–L149（P2 词表）及印 PDF 同处 | `IJzel` | 词表内唯一大写项（Dooi / natte sneeuw / IJzel / gladheid op de weg）；荷兰语 ijzel 应小写。印 PDF 文字层亦为 `IJzel`（1 处）。 |
| G-6 | low | ru-zh-tw text.md L538（P7 A2 栏小结）及印 PDF 同处 | `по данным 官方數據` | по данным = “据……数据”，无“官方”之意；与本版 L543 `據……數據` 及 core `据……数据` 矛盾，属误译 + 版内不一致。印 PDF 文字层亦含 `官方數據`（1 处）。 |

## 2. 逐版结论

| 版 | 结论 | 发现 |
|---|---|---|
| core-ru | 干净 | — |
| 2026-w47-ru-en | 有问题（low） | G-1 |
| 2026-w47-ru-de | 有问题（low） | G-2、G-3 |
| 2026-w47-ru-es | 干净 | — |
| 2026-w47-ru-fr | 有问题（low） | G-4 |
| 2026-w47-ru-it | 有问题（low） | G-4 |
| 2026-w47-ru-pt | 有问题（low） | G-4 |
| 2026-w47-ru-nl | 有问题（low） | G-4、G-5 |
| 2026-w47-ru-ja | 干净 | — |
| 2026-w47-ru-ko | 有问题（low） | G-4 变体 |
| 2026-w47-ru-zh-tw | 有问题（low） | G-6 |

### 通读方法与覆盖

- core-ru text.md（838 行，`2026-w47-ru-zh-cn.text.md`）全文通读 P1–P8 + Answers。
- 10 版 fan-out 各与 core 生成 diff（`diffs/ru-<lang>.diff.txt`，每版 375–376 行变更行，共 3722 行），**10 份 diff 已全部逐行读完**。俄语核心层经行集合比对 10 版一致（identical lines 460–499/838，差异均为讲解层）。
- 11 版印 PDF 文字层已抽取（`pdftext/<dir>.txt`，每版约 104–110KB，均为 8 页）；网 PDF pdftotext 字节 >0（core 56087，ru-en 57370）。G-1/G-2/G-3/G-5/G-6 均在印 PDF 文字层复核确认在版（grep 计数：`home town` 1、`JETZT SIE` 1、`Schneeregen` 2、`IJzel` 1、`官方數據` 1）。
- E 节翻译题 137–140：10 版 fan-out 译文与第一轮 PROOF-NOTE §6 表逐字一致，全部正确（en 版 139「On Tuesday Russia play Venezuela」为英式集合名词复数，非缺陷）。

### 事实核验（本轮复核通过）

- 日期/星期（`date -d`，Europe/Moscow）：2026-11-04 三、11-12 四、11-16 一、11-17 二、11-18 三、11-19 四、11-20 五、11-21 六、11-22 日、11-26 四、11-27 五、11-30 一——与文中星期表述全部一致。
- P4 赛果表（印 PDF 文字层）：8 场——Локомотив–Рубин 0:1、Факел–Динамо 1:2、Ахмат–Родина 1:0、Краснодар–ЦСКА 4:2、Крылья Советов–Оренбург 2:0、Спартак–Акрон 2:1、Зенит–Ростов 2:2、Балтика–Динамо Мх 0:1；进球 1+3+1+6+2+3+4+1=**21**，与 Q6/Q21 一致。
- 第 15 轮赛程（印 PDF）：8 场，20–22 日，16 支 RPL 球队齐全；Q50（15 轮 11 月 20 日开始）一致。
- 11 月工作日：20 个工作日 + 10 个非工作日（11 月 4 日假日 + 9 个周末日）；Q83–84（一周 2 休息日/5 工作日）；P6 图表 38+26+18+18=100。
- P7「Фразы недели」8 句逐句核对，均逐字出自本期正文（P1×2、P2、P3、P4、P5、P6×2）。
- Q150 范文实测 **97 词**（80–100 范围内）。
- 饥饿游戏日期：世界首映 2026-11-20（Lionsgate/Scholastic 官方）与**俄罗斯上映 2026-11-26**（多家俄媒一致）不同属正常；文中「26 ноября」正确，**不构成发现**。
- 其他外部事实（RPL 积分、83 分钟扳平、五部首映、Ozon 2025-11-11 1440 万单、节日日期、Simonyan 百年诞辰 1926→2026、Ozon Арена）与第一轮结论一致，未发现矛盾；**范围限定：本轮未对每项做新的外部来源复查，沿用第一轮已核范围**。

### 观察到但未采纳为发现（附理由）

- de/fr「синоптики обещают = die Wetterfrösche versprechen / les météorologues promettent」等口语化译法：属风格选择，含义正确。
- ja/ko 将 мокрый снег译为 みぞれ/진눈깨비：与 es 的 nieve mojada/nieve húmeda 同义变体一样，属可接受的本地天气术语，且各版内一致（与 G-3 的版内矛盾不同）。
- en 139 英式复数、Q62「15-й тур будет」教学句式：均非错误。
- 答案区 key 112 省略号写法（en `according to ...`、de `laut ...`、pt `segundo ...`）：与 core `据……数据` 的「……」对应，属既定缩写体例，非截断。
- 拉丁版 37 个 CJK 字体 run：经核查全为 →/✓ 符号字形（Noto Sans CJK SC 回退字形），非 CJK 文本；cjk+lat=0 证实无拉丁/西里尔字母落入 CJK 字体。
- `*-ru` 版拉丁标题字体问题（Noto Sans 而非 Newsreader）：已知跨家 D5 系统性问题，按任务要求不当新发现报。

## 3. 逐版机械门禁结果

| 门禁 | 结果 |
|---|---|
| p8.py compare `--total 150`（10 版 fan-out） | **10/10 CLEAN**，150/150 noted，missing=[]，extra_count=0，uncertain=[]，keydiff=[137,138,139,140]（E 节翻译题，预期）。日志+JSON：`p8-ru-<lang>.log/.json` |
| occlusion_audit.py（11 版 `svg/`） | **11/11 rc=0，0 flags**，自检 OK（planted BOXTITLE 类别均触发）。日志 `occlusion-summary.log`，JSON `occ-<dir>.json` |
| boxtitle_check.py（11 版） | **rc=0，11 版全部 0 DEFECT、0 OBSERVE、0 marginal**（core 57 标题/704 正文行；fan-out 55–67 标题，680–759 正文行）。日志 `boxtitle.log`，JSON `boxtitle/` |
| D5 census（自写 `census.py`，结果 `d5-census.json`） | **CJK+Latin=0、CJK+Cyrillic=0，全部 11 版**（core 579 / ja 570 / ko 1125 / zh-tw 584 个 CJK run；拉丁版 37 个 CJK run 全为 →/✓ 符号）。弯引号 U+201C/U+201D/U+2019 **全部在 Newsreader 内**（每版 2–4 处） |
| P8 最小字号（PyMuPDF，印 PDF 第 8 页） | **11 版均为 9.75pt**（恰达 SOP §1.1 底线），最大 34.50pt；页数 8/8 |
| 目视抽查（自印 PDF 100dpi 渲染，`visual/`） | 8 页：core P1/P8、ru-en P1/P8、ru-de P8、ru-pt P8、ru-ja P1、ru-ko P1——**无溢出、无遮挡、无缺图**。core P8 Morozko 图在版（F-3 目视旁证） |
| text.md 与 PDF 标题一致性 | 8 个框题（ТУР В ЦИФРАХ / СМИ / В ЭТОМ НОМЕРЕ / СЛОВО НЕДЕЛИ / ЗА И ПРОТИВ / ФРАЗЫ НЕДЕЛИ / ТЕСТ И ОТВЕТЫ / ОТВЕТЫ）逐版 grep：除 **СЛОВО НЕДЕЛИ 在 text.md 11/11 缺失**外其余全部在位；该缺失为第一轮 §5 已裁定的导出器已知局限（词条正文在 В ЭТОМ НОМЕРЕ 下完整），**不计入发现** |
| ABSTRACT.txt | 11/11 在位，均为读者母语（core 372B、en 355B、de 420B、es 395B、fr 435B、it 391B、pt 405B、nl 394B、ja 393B、ko 417B、zh-tw 348B） |

## 4. FIX-LOG 核实（逐项）

- **F-2（已修）——核实在版**：11 版 ×（印 PDF + 网 PDF + text.md）SHA-256 前 12 位与字节数与 FIX-LOG §2.1/§4 逐一比对，**22 个 PDF 全部一致、未变动**；11 版 text.md SHA 与 FIX-LOG 修后值一致（core 两份 `a54372a10afc…`，en `47e10cd4ea18…`，de `4bed5e5b83be…`，es `bb298469263f…`，fr `7cb8ee227f1e…`，it `b1265804a67e…`，pt `690570b42975…`，nl `c9ae09e22bc7…`，ja `2a298d44abc5…`，ko `3ed67e6ea61c…`，zh-tw `fa1040dd81ca…`）。每版 text.md 恰含 1 行「— СТРАНИЦА 8 —」，12 份文件（含 core 两份）无「СТРАНИЦА?」字面占位符。FIX-LOG §2.2 的 9 处回补标题行逐版 grep 核实全部在位（ru-en 1、ru-de 2、ru-es 1、ru-fr 2、ru-nl 1、ru-pt 2）。清单见 `inventory.txt`。
- **KIT SHA 抽查**：ru-en KIT L52–54（印 `f20b04c8244c911d…`、网 `21781f8396d9d936b…`、text.md `47e10cd4ea18…`）与实测 SHA-256 一致；core KIT L142（印 `e3c4c0ee155a96a…`、网 `0bdc87e621d75bb…`）与实测一致。
- **F-1、F-3（已裁定不修）**：按任务要求不重报。F-1 未重测，沿用第一轮结论。F-3 本轮仅在 core P8 目视中确认 Morozko 图在版，未逐版复核。

## 5. 遗留说明

- 导出器 ≥24pt 标题收集阈值问题：FIX-LOG 回补的 9 处标题行已核实在位；除已知 СЛОВО НЕДЕЛИ 缺失外，本轮未发现新的标题行丢失（见 §3 标题一致性表）。
- 第一轮 §5 的其余 text.md 导出器已知局限（P1 目录行、P4 赛果表/赛程、照片来源缺失）同样不计入问题，仅此记录。
- 本轮未跑 lint（任务禁止）；未核对 `*-ru` 11 版（范围外）。
