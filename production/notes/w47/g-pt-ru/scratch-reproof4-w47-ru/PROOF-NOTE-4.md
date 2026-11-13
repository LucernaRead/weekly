# PROOF-NOTE-4 — W47 ru 家庭第四轮独立重校

- 校对员：第四轮独立重校员（与建造者、修复者及第一/二/三轮校对员均不同；只校对、不修复）
- 范围：`production/2026-w47/` ru 家庭 11 版：core-ru（= ru-zh-cn）+ `2026-w47-ru-{de,en,fr,it,ja,ko,nl,pt,ru,zh-tw}`
- 日期：2026-11-12（EST）
- 依据：SOP §8 / §8.4；第三轮 `scratch-reproof3-w47-ru/PROOF-NOTE-3.md`（H-1、H-2）；`scratch-fix3-w47-ru/FIX-LOG-3.md`（H-1、H-2 修复）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof4-w47-ru/`（`pdftext/`、`diffs/`、`gates/`、`fingerprint.json`）
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`
- 说明：上一任重校员（同目录 setup 脚本的作者）在 setup 后即被中断、未产出任何结论；本轮从头完整重做，setup 脚本复用后逐项重新跑、逐项重新确认。

## 结论：(b) 有问题 — 6 项 low，无 MEDIUM、无 MAJOR

6 项全部为同一缺陷类：同一俄语词/同一标签在一版之内有两种读者语译法（G-3 同类，含义不受影响）。H-1、H-2 已修好、无回归；G-1～G-6、F-2、2b、2c 全部在位。

| # | 严重度 | 版 | 问题 |
|---|--------|----|------|
| J-1 | low | ru-pt | УЧЕБНЫЕ ДАННЫЕ 译法分裂：`Dados de prática` ×3 处 vs `Dados de exercício` ×4 处 |
| J-2 | low | ru-ja | 同一标签分裂：`練習用データ` ×3 处 vs `練習データ` ×4 处 |
| J-3 | low | ru-ja | промокод 译法分裂：`プロモコード` ×6 处 vs `割引コード` ×5 处 |
| J-4 | low | ru-ko | 同一标签分裂：`연습용 자료` ×3 处 vs `연습 데이터` ×4 处 |
| J-5 | low | ru-ko | промокод 译法分裂：`프로모 코드` ×6 处 vs `할인 코드` ×5 处 |
| J-6 | low | core-ru + ru-zh-tw | промокод Q77 配对选项 a 标 `促销码/促銷碼`，与其余 9 处 `折扣码/折扣碼` 不一致 |

## 新发现

### J-1（low）— ru-pt：УЧЕБНЫЕ ДАННЫЕ 译法分裂

- 规范形（与 P6 章节标题一致）：`Dados de prática`——L459 标题 `DADOS DE PRÁTICA`、L475 Q85 key、L767 答案 85。
- 偏离形：`Dados de exercício`——L476 Q86 key、L477 Q87 key、L768 答案 86、L769 答案 87。
- 印 PDF 文字层亦在：`Dados de prática` ×1、`Dados de exercício` ×2（提取合行，text.md 计 4 行）。
- 其余 9 版该标签全版统一（en `Practice data`、de `Übungsdaten`、es `Datos de práctica`、fr `Données d'exercice`、it `Dati di esercizio`、nl `Oefengegevens`、ja/ko/zh-tw 见 J-2/J-4/一致）；仅 pt 分裂。
- 建议改法：L476、L477、L768、L769 的 `Dados de exercício` → `Dados de prática`。

### J-2（low）— ru-ja：同一标签分裂

- 规范形：`練習用データ`——L459 标题、L475 Q85 key、L767 答案 85。
- 偏离形：`練習データ`——L476 Q86 key、L477 Q87 key、L768 答案 86、L769 答案 87。
- 印 PDF 文字层亦在：`練習用データ` ×2、`練習データ` ×2。
- 建议改法：L476、L477、L768、L769 的 `練習データ` → `練習用データ`。

### J-3（low）— ru-ja：промокод 译法分裂

- 规范形：`プロモコード`——L404 Q72 key、L413 Q77 选项 a、L530 Q108 key、L752 答案 72、L757 答案 77、L792 答案 108（×6）。
- 偏离形：`割引コード`——L525 P7 B1 词表行（`промокод 割引コード`）、L420 Q79 句译注、L759 答案 79 句译注、L655 Q147 key 注、L833 答案 147 注（×5）。
- 印 PDF 文字层亦在：`プロモコード` ×3、`割引コード` ×3。
- 建议改法：L420、L525、L655、L759、L833 的 `割引コード` → `プロモコード`。

### J-4（low）— ru-ko：同一标签分裂

- 规范形：`연습용 자료`——L459 标题、L475 Q85 key、L767 答案 85。
- 偏离形：`연습 데이터`——L476 Q86 key、L477 Q87 key、L768 答案 86、L769 答案 87。
- 印 PDF 文字层亦在：`연습용자료`（L974 标题区、L1525 答案 85）、`연습데이터`（L1526/1527 答案 86/87；提取丢空格，两种形式可辨）。
- 建议改法：L476、L477、L768、L769 的 `연습 데이터` → `연습용 자료`。

### J-5（low）— ru-ko：промокод 译法分裂

- 规范形：`프로모 코드`——L404 Q72 key、L413 Q77 选项 a、L530 Q108 key、L752 答案 72、L757 答案 77、L792 答案 108（×6）。
- 偏离形：`할인 코드`——L525 P7 B1 词表行（`промокод 할인 코드`）、L420 Q79 句译注、L759 答案 79 句译注、L655 Q147 key 注、L833 答案 147 注（×5）。
- 印 PDF 文字层亦在：`프로모코드` ×3（提取丢空格）、`할인코드` ×3（L1136 词表、L1518 答案 79、L1594 答案 147）。
- 建议改法：L420、L525、L655、L759、L833 的 `할인 코드` → `프로모 코드`。

### J-6（low）— core-ru + ru-zh-tw：Q77 配对选项 a 标与全版 gloss 不一致

- 全版规范形：`折扣码`（core）/ `折扣碼`（zh-tw）——L404 Q72、L420 Q79、L525 P7 词表、L530 Q108、L655 Q147、L752 答案 72、L759 答案 79、L792 答案 108、L833 答案 147（×9）；印 PDF 文字层 ×5。
- 偏离形：`促销码`（core）/ `促銷碼`（zh-tw）——仅 L413 Q77 配对行（`77. промокод — код со скидкой (key a · 促销码 a)`）与 L757 答案 77（`77. a — 促销码 a`）；印 PDF 文字层仅 P8 答案区 `77. a — 促销码a` ×1。
- 同一练习内其余三项选项标均与 gloss 一致（75 大促销/大促銷、76 退货/退貨、78 折扣），仅 77 偏离；其余 8 版 Q77 选项 a 标均与其版内规范形一致（en `promo code`、de `Rabattcode`、es `código promocional`、fr `code promo`、it `codice promozionale`、pt `código promocional`、nl `kortingscode`、ja `プロモコード`、ko `프로모 코드`）。
- 建议改法：两版 L413、L757 的选项 a 标 → `折扣码`（core）/ `折扣碼`（zh-tw）；配对选项源头若另有出处须同步改、重建 PDF。注意：core 是全家庭俄语核心层来源，修 core 时须确认不波及其他家庭（本轮只报 ru 家庭）。

## H-1/H-2 核实（已修好，无回归）

| 项 | 核实结果 |
|----|----------|
| H-1 ru-it | text.md L35 `## СЕЙЧАС ВЫ · TOCCA A TE` ✓；印 PDF 文字层 `TOCCA A TE` ×1 仅 P1，`TOCCA A VOI` ×0；`voi` 大小写不敏感 text.md 0、印/网 PDF 文字层 0 ✓ |
| H-2 ru-pt | text.md L35 `## СЕЙЧАС ВЫ · AGORA TU` ✓；印 PDF 文字层 `AGORA TU` ×1 仅 P1，`AGORA VOCÊ` ×0；`você`/`VOCÊ` text.md 0、印/网 PDF 文字层 0 ✓ |
| 目视 | 印 PDF P1 渲染（100dpi，读后删除）：it `СЕЙЧАС ВЫ · TOCCA A TE`、pt `СЕЙЧАС ВЫ · AGORA TU` 在位、无溢出/遮挡；pt 同页 quiz 注 `Lê a primeira página e escolhe a resposta certa` 与标题同为 tu 体，不再并存两种人称 ✓ |

## G-1～G-6、F-2、2b、2c 核实（全部在位，无回归）

| 项 | 核实结果 |
|----|----------|
| G-1 | ru-en text.md L99 `родина homeland`；印 PDF `homeland` ×1、`home town` ×0 ✓ |
| G-2 | ru-de text.md L35 `## СЕЙЧАС ВЫ · SIE SIND DRAN`；印 PDF `SIE SIND DRAN` ×1、`JETZT SIE` ×0 ✓ |
| G-3 | ru-de text.md `мокрый снег = nasser Schnee` 在 L141/L170/L512/L515/L691/L786；`Schneeregen` 仅存于 key 126 两处（L616、L812，整句答案说明，已裁定不动）；印 PDF `nasser Schnee` ×3、`Schneeregen` ×1 ✓ |
| G-4 | 各版 А ВЫ? 栏标题（L125）与说明句（L129）人称现一致：de `UND SIE?` / `Und Sie? Schreiben Sie…`；fr `ET VOUS ?` / `Et vous ? Écrivez…`；it `E TU?` / `E tu? Scrivi…`；nl `EN U?` / `En u? Schrijf…`；pt `E TU?` / `E tu? Escreve…`；es 始终 tú；ja/ko 敬语一致；en / zh-tw 无敬语区分 ✓ |
| G-5 | ru-nl text.md L145 `ijzel` 小写；印 PDF `ijzel` ×4、`IJzel` ×0；`Dooi` 词表（L137）与答案键（L646/L827）大小写一致，按既往裁定不动；印 PDF `Dooi` ×2 ✓ |
| G-6 | ru-zh-tw text.md L538 `по данным = 據……數據`（L543、L796 同式）；印 PDF `據……數據` ×2、`官方數據` ×0 ✓ |
| F-2 | 9 处回补标题行全部在位：en L58 `В ЭТОМ НОМЕРЕ · IN THIS ISSUE`；de L449 `ЗА И ПРОТИВ · PRO UND CONTRA`、L666 `ОТВЕТЫ · LÖSUNGEN — NACH SEITEN GEORDNET; AUFGABENNUMMER SUCHEN`；es L449 `PROS Y CONTRAS`；fr L58 `AU SOMMAIRE`、L449 `POUR ET CONTRE`；nl L449 `VOOR EN TEGEN`；pt L46 `СМИ · O QUE DIZEM OS MEDIA`、L449 `PRÓS E CONTRAS`；11 版 text.md 均恰含 1 行 `— СТРАНИЦА 8 —`（L668）✓ |
| 2b | ru-pt 5 处 tu 体指令行在位：L250 `Completa a forma verbal…`、L268 `Forma frases corretas…`、L341 `Completa com o tempo correto…`、L418 `Forma frases corretas…`、L495 `Junta as duas frases…`；L471 `Responde com a faixa…` ✓ |
| 2c | ru-pt L157 `Lê a primeira página e escolhe a resposta correta`；印 PDF `Lê a primeira página e escolhe a resposta certa` ×1、`Leia a primeira` ×0 ✓ |

## 指纹：33/33 全对

SHA-256 前 12 位 + 字节数，与 FIX-LOG-3 §4（it/pt 改后值）及 PROOF-NOTE-3（其余 9 版）核对一致（`fingerprint.json`）：

| 版 | 印 PDF | 网 PDF | text.md |
|----|--------|--------|---------|
| core-ru | `e3c4c0ee155a` / 24,713,345 B | `0bdc87e621d7` / 3,898,257 B | `a54372a10afc` / 60,953 B |
| ru-en | `7339c020640f` / 20,875,444 | `a3148c31c5a9` / 3,328,923 | `6c6932fb809f` / 62,785 |
| ru-de | `36d4cb6795ae` / 20,880,736 | `acc21d4dd4a6` / 3,334,229 | `31d3eb3eb223` / 63,483 |
| ru-es | `047ef0fbf75a` / 20,880,148 | `662998dc1e54` / 3,333,651 | `bb298469263f` / 64,176 |
| ru-fr | `0c38972146f9` / 20,880,950 | `b36ecf778e27` / 3,334,407 | `445daf81541a` / 63,364 |
| ru-it | `dc1e47616857` / 20,877,136 | `6ea69cc772a6` / 3,330,610 | `a46c6da64262` / 63,970 |
| ru-pt | `7624d63eec28` / 20,883,723 | `a8773dcdbcdc` / 3,337,277 | `93b60dc2d78d` / 65,110 |
| ru-nl | `5dedd8ecc30d` / 20,876,260 | `1abee50e0035` / 3,329,737 | `b600944e5e5f` / 64,011 |
| ru-ja | `f65820348bef` / 27,365,531 | `b6fed518a3c1` / 3,692,485 | `2a298d44abc5` / 64,477 |
| ru-ko | `d97e04c036d6` / 21,975,345 | `90059d0d6f40` / 3,494,537 | `5e34a2c5d29e` / 65,015 |
| ru-zh-tw | `7db5bece16d6` / 24,763,429 | `31a07aa54b5a` / 3,976,005 | `bc0a26a5267f` / 60,855 |

core-ru 两份 text.md（`2026-w47-ru-core.text.md` 与 `2026-w47-ru-zh-cn.text.md`）字节一致。11 版印 PDF 均为 8 页；印/网 PDF 提取字符数完全一致（core 31,510；en 37,128；de 37,551；es 37,584；fr 37,515；it 37,590；pt 37,894；nl 37,790；ja 32,163；ko 32,177；zh-tw 31,414）。it（37,591→37,590）、pt（37,896→37,894）字符差恰为 fix3 改动所致（VOI→TE −1、VOCÊ→TU −2）。

## 全量重校覆盖

- core-ru text.md（838 行）全文通读 P1–P8 + Answers，未见除 J-6 外的新问题。
- 10 版讲解层 diff 逐行读完（`diffs/ru-<lang>.diff.txt`，difflib 逐行比对 core vs 各版，只列版侧差异行；共 3,721 行）：en / de / es / fr / it / pt / nl / ko 各 376 行，ja 375 行，zh-tw 339 行；相同行数 en / de / es / fr / it / pt / nl / ko 462、ja 463、fr 460（fr 版 836 行）、zh-tw 499——与第二/三轮计数完全一致，俄语核心层 10 版一致。
- P8 答案 1–150：题面编号与 Answers 区编号 11 版均为 150/150、无缺号（`checks.py`）；p8.py compare 10/10 CLEAN（见机械门禁）；E 节翻译题 137–140 十版均已逐行读过、全部正确。
- 框题：`СЛОВО НЕДЕЛИ` 11/11 缺 text.md 项（text.md 0 处、印 PDF 文字层 1 处；第一轮已裁定为导出器设计局限，非缺陷，不重报）；其余框题均在位。
- ABSTRACT.txt 11/11 齐全，逐一读过：均为读者母语、单行、内容与本期一致（core 372B、en 355B、de 420B、es 395B、fr 435B、it 391B、pt 405B、nl 394B、ja 393B、ko 417B、zh-tw 348B）。

## 事实核验（独立重算）

- 日期/星期（`date -d`，Europe/Moscow）：2026-11-04 三、11-06 五、11-07 六、11-08 日、11-10 二、11-12 四、11-16 一、11-17 二、11-18 三、11-19 四、11-20 五、11-21 六、11-22 日、11-26 四、11-27 五、11-29 日、11-30 一——与文中星期表述一致；11 月 29 日为 11 月最后一个周日，与“День матери 29 ноября”一致。
- 算术：P4 赛果表（印 PDF）8 场：0:1、1:2、1:0、4:2、2:0、2:1、2:2、0:1，进球 1+3+1+6+2+3+4+1 = 21，与 Q6 / Q21 一致（第 8 场为 «Ахмат» — «Родина» 1:0，仅见于赛果表）；P6 图表 38+26+18+18 = 100；11 月工作日 30−9（周末日）−1（11 月 4 日假日）= 20；Simonyan 1926 年生 → 2026 年百年（2026−1926 = 100）。
- P7「Фразы недели」8 句逐字出自本期正文（脚本核验 8/8 在正文内），页码标注正确：P1 ×2、P2、P3、P4、P5、P6 ×2。
- Q150 范文 97 词（`Пример: ` 行实测 97 词，80–100 词要求内）。
- P8 最小字号：11 版印 PDF P8 最小字号均为 9.75pt（SOP 下限），最大 34.50pt。

## 机械门禁（只读跑盘上文件；解释器 `tools/venv/bin/python`）

| 门禁 | 结果 |
|------|------|
| p8.py compare `--total 150`（10 版 fan-out） | 10/10 CLEAN；`missing=[] extra_count=0 uncertain=[] keydiff=[137,138,139,140]`（E 节翻译题预期差异） |
| occlusion_audit.py（11 版 svg/） | 11/11 0 flags |
| boxtitle_check.py（11 版） | 11/11 0 DEFECT、0 OBSERVE、0 marginal（it 55 titles、ko 67、其余 57） |
| spill_sweep.py（11 版） | 11/11 0 SPILL（OBSERVE 为邻近文字候选项，非缺陷） |
| pdf_edge_scan.py（印 PDF，200dpi） | 11/11 ok，每版 8 页；四边 touch 全为 0、near 全空；最小页边距 fr 15.1pt、nl 29.2pt、其余 ≥45.0pt |
| head_check.py（fix3 的 it/pt run.log，只读） | PASS 0 defects；其余 9 版生产目录内无 run.log，无输入可查（同第三轮） |
| D5 census（census.py：字体 + 弯引号普查，rc=0） | 11/11：CJK+Latin 0、CJK+Cyrillic 0；弯引号全部 Newsreader（core 4、en 2、de 3、es 2、fr 4、it 2、pt 2、nl 2、ja 2、ko 2、zh-tw 4） |

FIX-LOG-3 §5 提到的 `census_quotes.py` 在盘上找不到（`tools/`、`scratch-reproof2-w47-ru/`、`scratch-reproof3-w47-ru/`、`scratch-fix2b/2c-w47-ru/`、`scratch-fix3-w47-ru/` 均无此文件），未能复跑；引号普查以 census.py 的弯引号计数（runs 数 + 字体）为准。

## 目视抽查

自印 PDF 渲染 2 页（100dpi，读后删除）：ru-it P1、ru-pt P1。两处新标题在位、无溢出/遮挡；pt 同页 quiz 注已是 tu 体。渲染图已删除。

## 观察到但不采纳为发现

- de L538 `синоптики обещают = die Wetterfrösche versprechen`、nl L538 `de weermannen beloven`：口语化译法，含义正确，属风格选择（第二/三轮同样处理）。
- ja / ko 将 мокрый снег译为 みぞれ / 진눈깨비：各版内一致的本地天气术语，非 G-3 式版内矛盾。
- en L139 `On Tuesday Russia play Venezuela`：英式集合名词复数，第二轮已裁定非缺陷。
- fr L585 金句译文 `Les fêtes professionnelles ne donnent pas de jour férié`（core：`Профессиональные праздники не дают выходных`）：“jour férié”较“jours de repos”略松，但句意完整保留，且同版 L163 关键句用准确的 `n'ajoutent pas de jours de repos`；不列为发现。
- key 112 省略号写法（en `according to...`、de `laut...`、pt `segundo...`）：与 core `据……数据` 的「……」对应，属既定缩写体例。
- fr 版比分在法语讲解中写作 `4-2`/`0-1`（连字符）：全版一致的体例，俄语题干仍为 `4:2`，不列为发现。
- 各版词表大小写参差（如 en `Thaw` / `wet snow` / `Freezing rain` / `black ice`）：多版共有的既有体例，非本版内术语分裂，不列为发现。

## 不重报项（按任务）

FIX-LOG 裁定不修项（F-1 P8 key 栏右余量、F-3 Morozko 图注行、ru-nl `Dooi` 不动、de key 126 `Schneeregen` 不动）；第一/二/三轮已接受残留；`*-ru` 拉丁标题字体问题（已知跨家 D5 系统性问题，另有工人统一修）；`СЛОВО НЕДЕЛИ` 缺 text.md 项（导出器设计局限）。

## 逐版结论

| 版 | 结论 |
|----|------|
| core-ru | 1 项 low（J-6，与 zh-tw 共有） |
| ru-en | 干净 |
| ru-de | 干净 |
| ru-es | 干净 |
| ru-fr | 干净 |
| ru-it | 干净（H-1 已修好） |
| ru-pt | 1 项 low（J-1；H-2 已修好） |
| ru-nl | 干净 |
| ru-ja | 2 项 low（J-2、J-3） |
| ru-ko | 2 项 low（J-4、J-5） |
| ru-zh-tw | 1 项 low（J-6，与 core 共有） |

## 遗留说明

- 本轮为只读校对：未修复、未重建、未 commit、未 push、未跑 lint、未改 SOP。
- 磁盘：开工时 `/home/hatch` 已用 95G（150G 盘，64%），全程未触发 100G 门限；工作目录约 3M（pdftext + diffs + gates + fingerprint.json）。
- 渲染图 `visual/` 2 张 PNG 已读完删除。
