# PROOF-NOTE-5 — W47 ru 家庭第五轮独立重校

- 校对员：第五轮独立重校员（与建造者、fix4 工人 bd49579f、第四轮校对员 642ff1ae 均不同；只校对、不修复）
- 范围：`production/2026-w47/` ru 家庭 11 版：core-ru（= ru-zh-cn）+ `2026-w47-ru-{de,en,fr,it,ja,ko,nl,pt,ru,zh-tw}`
- 日期：2026-11-12（EST）
- 依据：SOP §8 / §8.4；第四轮 `scratch-reproof4-w47-ru/PROOF-NOTE-4.md`（J-1～J-6）；`scratch-fix4-w47-ru/FIX-LOG-4.md`（J-1～J-6 修复）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof5-w47-ru/`（`pdftext/`、`diffs/`、`gates/`、`fingerprint.json`）
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`（全程未用系统 python3）
- 说明：本轮从头完整重做：core 全文通读 + 10 版 diff 逐行读完 + 全部计数与门禁逐项重新跑、逐项重新确认；未复用第四轮结论。

## 结论：(a) CLEAN — 0 findings

J-1～J-6 全部修好、在位、无回归；H-1/H-2、G-1～G-6、F-2、2b、2c 全部在位、无回归；全量重读未发现新问题；机械门禁全部通过；指纹 33/33 与 FIX-LOG-4 §4 一致，其余 6 版（en/de/es/fr/it/nl）与 PROOF-NOTE-4 一致，fix4 无外溢。

## J-1～J-6 核实（全部修好）

text.md 计数与印 PDF 文字层计数逐版实测（ko 的 PDF 层提取丢词内空格，按去空格形核验）：

| 项 | 版 | text.md 新串 / 旧串 | 印 PDF 文字层新串 / 旧串 |
|----|----|---------------------|--------------------------|
| J-1 | ru-pt | `Dados de prática` ×6 / `Dados de exercício` ×0 | `Dados de prática` ×3 / ×0 |
| J-2 | ru-ja | `練習用データ` ×7 / `練習データ` ×0 | `練習用データ` ×4 / ×0 |
| J-3 | ru-ja | `プロモコード` ×11 / `割引コード` ×0 | `プロモコード` ×6 / ×0 |
| J-4 | ru-ko | `연습용 자료` ×7 / `연습 데이터` ×0 | 去空格 `연습용자료` ×4 / `연습데이터` ×0 |
| J-5 | ru-ko | `프로모 코드` ×11 / `할인 코드` ×0 | 去空格 `프로모코드` ×6 / `할인코드` ×0 |
| J-6 | core-ru（两份 text.md 均查） | `折扣码` ×11 / `促销码` ×0 | `折扣码` ×6 / ×0 |
| J-6 | ru-zh-tw | `折扣碼` ×11 / `促銷碼` ×0 | `折扣碼` ×6 / ×0 |

网 PDF 文字层与印 PDF 一致（提取字符数印/网完全相同，见指纹节）。计数与 FIX-LOG-4 §3 逐一吻合。

## H-1/H-2、G-1～G-6、F-2、2b、2c 核实（全部在位，无回归）

| 项 | 核实结果 |
|----|----------|
| H-1 ru-it | text.md L35 `## СЕЙЧАС ВЫ · TOCCA A TE` ✓；印 PDF `TOCCA A TE` ×1，`TOCCA A VOI` ×0；text.md `voi`（大小写不敏感）0 ✓ |
| H-2 ru-pt | text.md L35 `## СЕЙЧАС ВЫ · AGORA TU` ✓；印 PDF `AGORA TU` ×1，`AGORA VOCÊ` ×0；text.md `você` 0 ✓ |
| G-1 | ru-en text.md L99 `родина homeland`；印 PDF `homeland` ×1、`home town` ×0 ✓ |
| G-2 | ru-de text.md L35 `## СЕЙЧАС ВЫ · SIE SIND DRAN`；印 PDF `SIE SIND DRAN` ×1、`JETZT SIE` ×0 ✓ |
| G-3 | ru-de text.md `мокрый снег = nasser Schnee` ×6 处；`Schneeregen` 仅 key 126 两处（L616、L812，整句答案说明，已裁定不动）；印 PDF `nasser Schnee` ×3、`Schneeregen` ×1 ✓ |
| G-4 | 各版 А ВЫ? 栏标题（L125）与说明句（L129）人称现一致：de `UND SIE?` / `Und Sie? Schreiben Sie…`；fr `ET VOUS ?` / `Et vous ? Écrivez…`；it `E TU?` / `E tu? Scrivi…`；nl `EN U?` / `En u? Schrijf…`；pt `E TU?` / `E tu? Escreve…`；es 始终 tú；ja/ko 敬语一致；en / zh-tw 无敬语区分 ✓ |
| G-5 | ru-nl text.md L145 `ijzel` 小写；印 PDF `ijzel` ×4、`IJzel` ×0；`Dooi` 按既往裁定不动 ✓ |
| G-6 | ru-zh-tw text.md L538 `по данным = 據……數據`（L543、L796 同式）；印 PDF `據……數據` ×2、`官方數據` ×0 ✓ |
| F-2 | 9 处回补标题行全部在位：en L58 `В ЭТОМ НОМЕРЕ · IN THIS ISSUE`；de L449 `ЗА И ПРОТИВ · PRO UND CONTRA`、L666 `ОТВЕТЫ · LÖSUNGEN — NACH SEITEN GEORDNET; AUFGABENNUMMER SUCHEN`；es L449 `PROS Y CONTRAS`；fr L58 `AU SOMMAIRE`、L449 `POUR ET CONTRE`；nl L449 `VOOR EN TEGEN`；pt L46 `СМИ · O QUE DIZEM OS MEDIA`、L449 `PRÓS E CONTRAS`；11 版 text.md 均恰含 1 行 `— СТРАНИЦА 8 —` ✓ |
| 2b | ru-pt 5 处 tu 体指令行在位：L250 `Completa a forma verbal…`、L268 `Forma frases corretas…`、L341 `Completa com o tempo correto…`、L418 `Forma frases corretas…`、L495 `Junta as duas frases…`；L471 `Responde com a faixa…` ✓ |
| 2c | ru-pt tu 体在位：印 PDF `Lê a primeira página e escolhe a resposta certa` ×1、`Leia a primeira` ×0 ✓（见末节“记录订正”：PROOF-NOTE-4 对 text.md L157 的引文为转述，原文见该节） |

## 指纹：33/33 全对（与 FIX-LOG-4 §4 对照）

SHA-256 前 12 位 + 字节数（`fingerprint.json`）；网 PDF SHA 为盘上实时值：

| 版 | 印 PDF | 网 PDF | text.md |
|----|--------|--------|---------|
| core-ru | `a114f1d24694` / 24,713,343 B | `e37922c048d1` / 3,898,280 B | `2a38d3dab649` / 60,953 B |
| ru-en | `7339c020640f` / 20,875,444 | `a3148c31c5a9` / 3,328,923 | `6c6932fb809f` / 62,785 |
| ru-de | `36d4cb6795ae` / 20,880,736 | `acc21d4dd4a6` / 3,334,229 | `31d3eb3eb223` / 63,483 |
| ru-es | `047ef0fbf75a` / 20,880,148 | `662998dc1e54` / 3,333,651 | `bb298469263f` / 64,176 |
| ru-fr | `0c38972146f9` / 20,880,950 | `b36ecf778e27` / 3,334,407 | `445daf81541a` / 63,364 |
| ru-it | `dc1e47616857` / 20,877,136 | `6ea69cc772a6` / 3,330,610 | `a46c6da64262` / 63,970 |
| ru-pt | `de64a14d7ce5` / 20,883,714 | `a8c1afb03722` / 3,337,256 | `67ced8562a71` / 65,102 |
| ru-nl | `5dedd8ecc30d` / 20,876,260 | `1abee50e0035` / 3,329,737 | `b600944e5e5f` / 64,011 |
| ru-ja | `bc7bccfe15ca` / 27,365,839 | `dc9f27b03891` / 3,692,713 | `465a2e4ebcd8` / 64,504 |
| ru-ko | `fece66f1bfec` / 21,975,394 | `a6a997780723` / 3,494,572 | `050d18839631` / 65,030 |
| ru-zh-tw | `0c4bffc78bdc` / 24,763,427 | `cc348ad4ae16` / 3,975,999 | `948538470d3c` / 60,855 |

- 其余 6 版（en/de/es/fr/it/nl）印/网 PDF 与 text.md SHA+字节与 PROOF-NOTE-4 逐一核对不变：fix4 无外溢。
- core-ru 两份 text.md（`2026-w47-ru-core.text.md` 与 `2026-w47-ru-zh-cn.text.md`）字节一致。
- 11 版印 PDF 均为 8 页；印/网 PDF 提取字符数完全一致（core 31,510；en 37,128；de 37,551；es 37,584；fr 37,515；it 37,590；pt 37,890；nl 37,790；ja 32,168；ko 32,180；zh-tw 31,414）。字符数变化与 fix4 改动一致：pt 37,894→37,890（−4）、ja 32,163→32,168（+5）、ko 32,177→32,180（+3）、core/zh-tw 不变。

## 全量重校覆盖

- core-ru text.md（838 行）全文通读 P1–P8 + Answers，未见新问题。
- 10 版讲解层 diff 逐行读完（`diffs/ru-<lang>.diff.txt`，difflib 逐行比对 core vs 各版，只列版侧差异行；共 3,721 行）：en / de / es / fr / it / pt / nl / ko 各 376 行，ja 375 行，zh-tw 339 行；相同行数 en / de / es / fr / it / pt / nl / ko 462、ja 463、fr 460（fr 版 836 行）、zh-tw 499——与第四轮计数完全一致，俄语核心层 10 版一致。
- P8 答案 1–150：题面编号与 Answers 区编号 11 版均为 150/150、无缺号（`checks.py`）；p8.py compare 10/10 CLEAN（见机械门禁）；E 节翻译题 137–140 十版均已逐行读过、全部正确。
- 框题：`СЛОВО НЕДЕЛИ` 11/11 缺 text.md 项（text.md 0 处、印 PDF 文字层 1 处；第一轮已裁定为导出器设计局限，非缺陷，不重报）；其余框题均在位。
- ABSTRACT.txt 11/11 齐全，逐一读过：均为读者母语、单行、内容与本期一致（core 372B、en 355B、de 420B、es 395B、fr 435B、it 391B、pt 405B、nl 394B、ja 393B、ko 417B、zh-tw 348B）。

## 事实核验（独立重算）

- 日期/星期（`date -d`，Europe/Moscow）：2026-11-04 三、11-06 五、11-07 六、11-08 日、11-10 二、11-12 四、11-16 一、11-17 二、11-18 三、11-19 四、11-20 五、11-21 六、11-22 日、11-26 四、11-27 五、11-29 日、11-30 一——与文中星期表述一致；11 月 29 日为 11 月最后一个周日，与“День матери 29 ноября”一致。
- 算术：P4 赛果 8 场比分均在印 PDF 文字层（0:1、1:2、1:0、4:2、2:0、2:1、2:2 均在列），进球 1+3+1+6+2+3+4+1 = 21，与 Q6 / Q21 一致；P6 图表 38+26+18+18 = 100；11 月工作日 30−9（周末日）−1（11 月 4 日假日）= 20；Simonyan 1926 年生 → 2026 年百年（2026−1926 = 100）。
- P7「Фразы недели」8 句逐字出自本期正文（脚本核验 8/8 在正文内），页码标注正确：P1 ×2、P2、P3、P4、P5、P6 ×2。
- Q150 范文 97 词（core L664 `Пример: ` 行直接实测 97 词，80–100 词要求内；见末节脚本口径说明）。
- P8 最小字号：11 版印 PDF P8 最小字号均为 9.75pt（SOP 下限），最大 34.50pt。

## 机械门禁（只读跑盘上文件；解释器 `tools/venv/bin/python`；日志存 `gates/`）

| 门禁 | 结果 |
|------|------|
| p8.py compare `--total 150`（10 版 fan-out） | 10/10 CLEAN；`missing=[] extra_count=0 uncertain=[] keydiff=[137,138,139,140]`（E 节翻译题预期差异） |
| occlusion_audit.py（11 版 svg/） | 11/11 0 flags |
| boxtitle_check.py（11 版） | 11/11 0 DEFECT、0 OBSERVE、0 marginal（it 55 titles、ko 67、其余 57） |
| spill_sweep.py（11 版） | 11/11 0 SPILL（OBSERVE 为邻近文字候选项，非缺陷） |
| pdf_edge_scan.py（印 PDF，200dpi） | 11/11 ok，每版 8 页；四边 touch 全为 0、near 全空；最小页边距 fr 15.1pt、nl 29.2pt、其余 ≥45.0pt |
| head_check.py（fix4 的 5 份 run.log，只读） | PASS 0 defects（生产目录内无 run.log，故以 fix4 本次构建日志为输入；其余 6 版无本次构建，无输入可查） |
| D5 census（census.py：字体 + 弯引号普查，rc=0） | 11/11：CJK+Latin 0、CJK+Cyrillic 0；弯引号全部 Newsreader（core 4、en 2、de 3、es 2、fr 4、it 2、pt 2、nl 2、ja 2、ko 2、zh-tw 4）——与第四轮计数完全一致 |
| 引号普查（`scratch-gatefix-u201c-ru/census_quotes.py`，11 版 svg） | 11/11 GRAND TOTAL defective: 0 |

## 观察到但不采纳为发现

- de L538 `синоптики обещают = die Wetterfrösche versprechen`、nl L538 `de weermannen beloven`：口语化译法，含义正确，属风格选择（第二/三/四轮同样处理）。
- ja / ko 将 мокрый снег译为 みぞれ / 진눈깨비：各版内一致的本地天气术语，非 G-3 式版内矛盾。
- en L139 `On Tuesday Russia play Venezuela`：英式集合名词复数，第二轮已裁定非缺陷。
- fr L585 金句译文 `Les fêtes professionnelles ne donnent pas de jour férié`（core：`Профессиональные праздники не дают выходных`）：“jour férié”较“jours de repos”略松，但句意完整保留，且同版 L163 关键句用准确的 `n'ajoutent pas de jours de repos`；不列为发现。
- key 112 省略号写法（en `according to...`、de `laut...`、pt `segundo...`）：与 core `据……数据` 的「……」对应，属既定缩写体例。
- fr 版比分在法语讲解中写作 `4-2`/`0-1`（连字符）：全版一致的体例，俄语题干仍为 `4:2`，不列为发现。
- 各版词表大小写参差（如 en `Thaw` / `wet snow` / `Freezing rain` / `black ice`）：多版共有的既有体例，非本版内术语分裂，不列为发现。

## 不重报项（按任务）

FIX-LOG 裁定不修项（F-1 P8 key 栏右余量、F-3 Morozko 图注行、ru-nl `Dooi` 不动、de key 126 `Schneeregen` 不动）；第一/二/三/四轮已接受残留；`*-ru` 拉丁标题字体问题（已知跨家 D5 系统性问题，另有工人统一修）；`СЛОВО НЕДЕЛИ` 缺 text.md 项（导出器设计局限）。

## 逐版结论

| 版 | 结论 |
|----|------|
| core-ru | 干净（J-6 已修好） |
| ru-en | 干净 |
| ru-de | 干净 |
| ru-es | 干净 |
| ru-fr | 干净 |
| ru-it | 干净（H-1 已修好） |
| ru-pt | 干净（J-1、H-2 已修好） |
| ru-nl | 干净 |
| ru-ja | 干净（J-2、J-3 已修好） |
| ru-ko | 干净（J-4、J-5 已修好） |
| ru-zh-tw | 干净（J-6 已修好） |

## 记录订正与脚本口径说明（非发现）

- 2c 引文订正：PROOF-NOTE-4 称 ru-pt L157 为 `Lê a primeira página e escolhe a resposta correta`；实测现行 text.md L157 与 fix4 前快照均为 `*Lê a página 2 e escolhe a resposta correta.*`（L240/L313/L390 同式为第 3/4/5 版）。`Lê a primeira página e escolhe a resposta certa` 是印 PDF P1 quiz 注的另一行（×1）。2c 实质（tu 体、无 `Leia`）不受影响，仍在位；仅第四轮引文为转述，特此订正。
- Q150 词数脚本口径：复用的 `checks.py` 用 `Пример: (.*?)\n` 匹配，命中 L508 词汇行（6 词）而非 L664 范文行；本轮以 L664 行直接实测为准：97 词。

## 遗留说明

- 本轮为只读校对：未修复、未重建、未 commit、未 push、未跑 lint、未改 SOP；除本 scratch 目录外未写任何东西。
- 磁盘：开工与收尾均为 `/home/hatch` 已用 95G（150G 盘，64%），全程未触发 100G 门限；工作目录约 2.9M（pdftext + diffs + gates + fingerprint.json）。
- 未做目视渲染抽查：H-1/H-2 的 P1 标题已在第四轮目视核验在位，本轮改动（J-1～J-6）全部位于 P7 词表 / P8 练习与答案区，门禁（occlusion / boxtitle / spill / edge）全部通过，且文字层计数与 text.md 逐项吻合；不再重复渲染。
