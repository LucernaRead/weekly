# PROOF-NOTE-3 — W47 ru 家庭第三轮独立重校

- 校对员：第三轮独立重校员（与建造者、第一/二轮校对员及修复者均不同；只校对、不修复）
- 范围：`production/2026-w47/` ru 家庭 11 版：core-ru（= ru-zh-cn）+ `2026-w47-ru-{de,en,fr,it,ja,ko,nl,pt,ru,zh-tw}`
- 日期：2026-11-12（EST）
- 依据：SOP §8 / §8.4；第二轮 `scratch-reproof2-w47-ru/PROOF-NOTE-2.md`（G-1～G-6）；`scratch-fix-ru/FIX-LOG.md` §8；`scratch-fix2b-w47-ru/FIX-LOG-2b.md`；`scratch-fix2c-w47-ru/FIX-LOG-2c.md`
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof3-w47-ru/`（`pdftext/`、`diffs/`、`gates/`、`visual/`）
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`

## 结论：(b) 有问题 — 2 项 low，无 MAJOR、无 MEDIUM

| # | 严重度 | 版 | 位置 | 问题 |
|---|--------|----|------|------|
| H-1 | low | ru-it | text.md L35；印 PDF P1 | P1 栏目标题 `СЕЙЧАС ВЫ · TOCCA A VOI` 用 voi（复数/敬语），与全版主导人称 tu 混用 |
| H-2 | low | ru-pt | text.md L35；印 PDF P1 | P1 栏目标题 `СЕЙЧАС ВЫ · AGORA VOCÊ` 用 você，与全版主导人称 tu 混用 |

H-1、H-2 均为 G-4（第二轮：А ВЫ? 栏人称混用）同类，但位置不同（P1 栏目标题而非 P2 А ВЫ? 栏），第一/二轮均未报。含义不受影响；与 G-4 同级 low。

## 新发现

### H-1（low）— ru-it：P1 标题 TOCCA A VOI 与全版 tu 体冲突

- text.md L35：`## СЕЙЧАС ВЫ · TOCCA A VOI`。
- 全版命令式均为 tu：Leggi / scegli / Completa / Forma / Rispondi / Scrivi / Metti / Unisci；А ВЫ? 栏已按 G-4 修为 `E TU?` / `E tu? Scrivi…`。
- grep 全文：`voi`（不分大小写）仅此 1 处（L35）；印 PDF 文字层 `TOCCA A VOI` ×1、`E TU?` ×1。
- FIX-LOG §8.1 it 行称“voi 仅见于 G-4 标题本身”与盘上事实不符，是其漏网的原因。
- 目视：印 PDF P1 该标题在位、无溢出/遮挡（`visual/it-p1.png`，已读后删除——见§遗留）。

### H-2（low）— ru-pt：P1 标题 AGORA VOCÊ 与全版 tu 体冲突

- text.md L35：`## СЕЙЧАС ВЫ · AGORA VOCÊ`。
- 全版命令式均为 tu：Lê / escolhe / Completa / Forma / Junta / Escreve / Traduz / Responde；А ВЫ? 栏已按 G-4 修为 `E TU?` / `E tu? Escreve…`；2b 修 5 处指令行、2c 修 P1 注 `Leia` → `Lê`。
- grep 全文：`VOCÊ` / `você` 仅此 1 处（L35；注：`grep -i você` 在 C locale 下因重音字母大小写折叠失效返回 0，须用显式 `VOCÊ\|você` 模式）；印 PDF 文字层 `AGORA VOCÊ` ×1、`E TU?` ×1。
- FIX-LOG §8.5 的 pt você 残留清单未列 P1 标题。
- 目视：印 PDF P1 该标题在位；同一页下方 quiz 注行已是 tu 体（`Lê a primeira página e escolhe a resposta certa`），同一页内两种人称并存（`visual/pt-p1.png`）。

### 佐证：其余 9 版 P1 标题均与其主导人称一致

core-ru `即学即练`、ru-en `TRY IT NOW`、ru-de `SIE SIND DRAN`、ru-es `AHORA TÚ`、ru-fr `À VOUS`、ru-nl `NU U`、ru-ja `さあ、あなたも`、ru-ko `지금, 여러분 차례`、ru-zh-tw `即學即練`——仅 it / pt 偏离。

## G-1～G-6 核实（全部在版；text.md + 印 PDF 文字层双重确认）

| 项 | 核实结果 |
|----|----------|
| G-1 | ru-en text.md L99 `родина homeland`；印 PDF `homeland` ×1、`home town` ×0 ✓ |
| G-2 | ru-de text.md L35 `## СЕЙЧАС ВЫ · SIE SIND DRAN`；印 PDF `SIE SIND DRAN` ×1、`JETZT SIE` ×0 ✓ |
| G-3 | ru-de text.md `мокрый снег = nasser Schnee` 在 L170/L512/L515/L691/L786（另 L141 词表 `nasser Schnee`）；`Schneeregen` 仅存于 key 126 两处（L616、L812，整句答案说明，已裁定不动）；印 PDF `nasser Schnee` ×3、`Schneeregen` ×1（key 126）✓ |
| G-4 | 各版 А ВЫ? 栏标题（L125）与说明句（L129）人称现一致：de `UND SIE?` / `Und Sie? Schreiben Sie…`；fr `ET VOUS?` / `Et vous? Écrivez…`；it `E TU?` / `E tu? Scrivi…`；nl `EN U?` / `En u? Schrijf…`；pt `E TU?` / `E tu? Escreve…`；ko `여러분은요?` / `여러분은요? …보내세요`；es 始终 tú；ja 敬语一致；en / zh-tw 无敬语区分 ✓ |
| G-5 | ru-nl text.md L145 `ijzel` 小写；印 PDF `ijzel` ×4、`IJzel` ×0；词表 `Dooi`（L137）与答案键 `Dooi c`（L646/L827）大小写一致，按 FIX-LOG-2b 裁定不动；印 PDF `Dooi` ×2 ✓ |
| G-6 | ru-zh-tw text.md L538 `по данным = 據……數據`（L543、L796 同式）；印 PDF `據……數據` ×2、`官方數據` ×0 ✓ |

### de LINEX 回炉句（FIX-LOG §8.3）

text.md L129：`Und Sie? Schreiben Sie zwei russische Sätze an die Redaktion: …`；印 PDF 中该句跨两行（`Und Sie? Schreiben Sie zwei russische` / `Sätze an die Redaktion: …`，pdftext L257 起）；目视 de P2：该句两行恰好装进 А ВЫ? 框、无溢出，Morozko 图注行下方留白正常 ✓。occlusion 11 版 0 flags（见机械门禁）。

### ru-pt tu 体统一（2b + 2c）

text.md 5 处指令行在位：L250 `Completa a forma verbal…`、L268 `Forma frases corretas…`、L341 `Completa com o tempo correto…`、L418 `Forma frases corretas…`、L495 `Junta as duas frases…`；舊 você 式 4 式计数 0；L471 `Responde com a faixa…`。印 PDF：`Lê a primeira página e escolhe a resposta certa` ×1、`Leia a primeira` ×0、`Completa a forma verbal` ×1、`Forma frases corretas` ×2、`Junta as duas frases` ×1、`Responde com a faixa` ×1 ✓。

### F-2 回补的 9 处标题行（第一轮修复）

全部在位：en L58 `В ЭТОМ НОМЕРЕ · IN THIS ISSUE`；de L449 `ЗА И ПРОТИВ · PRO UND CONTRA`、L666 `ОТВЕТЫ · LÖSUNGEN — NACH SEITEN GEORDNET; AUFGABENNUMMER SUCHEN`；es L449 `PROS Y CONTRAS`；fr L58 `AU SOMMAIRE`、L449 `POUR ET CONTRE`；nl L449 `VOOR EN TEGEN`；pt L46 `СМИ · O QUE DIZEM OS MEDIA`、L449 `PRÓS E CONTRAS`。11 版 text.md 均恰含 1 行 `— СТРАНИЦА 8 —`（L668）✓。

## 指纹：33/33 全对

SHA-256 前 12 位 + 字节数，与 FIX-LOG §8 / FIX-LOG-2b / FIX-LOG-2c / PROOF-NOTE-2 核对一致（`fingerprint.json`）：

| 版 | 印 PDF | 网 PDF | text.md |
|----|--------|--------|---------|
| core-ru | `e3c4c0ee155a` / 24,713,345 B | `0bdc87e621d7` / 3,898,257 B | `a54372a10afc` / 60,953 B |
| ru-en | `7339c020640f` / 20,875,444 | `a3148c31c5a9` / 3,328,923 | `6c6932fb809f` / 62,785 |
| ru-de | `36d4cb6795ae` / 20,880,736 | `acc21d4dd4a6` / 3,334,229 | `31d3eb3eb223` / 63,483 |
| ru-es | `047ef0fbf75a` / 20,880,148 | `662998dc1e54` / 3,333,651 | `bb298469263f` / 64,176 |
| ru-fr | `0c38972146f9` / 20,880,950 | `b36ecf778e27` / 3,334,407 | `445daf81541a` / 63,364 |
| ru-it | `b83c981d399f` / 20,877,138 | `47201c0d411c` / 3,330,609 | `ba59c4ff2368` / 63,971 |
| ru-pt | `6ed8d2b9ba49` / 20,883,753 | `f71d4e50cf40` / 3,337,277 | `00e972b717fb` / 65,113 |
| ru-nl | `5dedd8ecc30d` / 20,876,260 | `1abee50e0035` / 3,329,737 | `b600944e5e5f` / 64,011 |
| ru-ja | `f65820348bef` / 27,365,531 | `b6fed518a3c1` / 3,692,485 | `2a298d44abc5` / 64,477 |
| ru-ko | `d97e04c036d6` / 21,975,345 | `90059d0d6f40` / 3,494,537 | `5e34a2c5d29e` / 65,015 |
| ru-zh-tw | `7db5bece16d6` / 24,763,429 | `31a07aa54b5a` / 3,976,005 | `bc0a26a5267f` / 60,855 |

core-ru 两份 text.md（`2026-w47-ru-core.text.md` 与 `2026-w47-ru-zh-cn.text.md`）字节一致。11 版印 PDF 均为 8 页；印/网 PDF 提取字符数完全一致（core 31,510；en 37,128；de 37,551；es 37,584；fr 37,515；it 37,591；pt 37,896；nl 37,790；ja 32,163；ko 32,177；zh-tw 31,414）。

## 全量重校覆盖

- core-ru text.md（838 行）全文通读 P1–P8 + Answers，未见新问题。
- 10 版讲解层 diff 逐行读完（`diffs/ru-<lang>.diff.txt`，difflib 逐行比对 core vs 各版，只列版侧差异行；共 3,722 行）：en / de / es / fr / it / pt / nl / ko 各 376 行，ja 375 行，zh-tw 339 行；相同行数 en / de / es / fr / it / pt / nl / ko 462、ja 463、fr 460（fr 版 836 行）、zh-tw 499——与第二轮计数完全一致，俄语核心层 10 版一致。
- P8 答案 1–150：题面编号与 Answers 区编号 11 版均为 150/150、无缺号（`checks.py`）；p8.py compare 10/10 CLEAN（见机械门禁）；E 节翻译题 137–140 十版均已逐行读过、全部正确。
- 框题：8 个框题中 7 个在 11 版 text.md 均在位；`СЛОВО НЕДЕЛИ` 11/11 缺 text.md 项（第一轮已裁定为导出器设计局限，非缺陷，不重报）。
- ABSTRACT.txt 11/11 齐全，均为读者母语、单行、内容与本期一致（core 372B、en 355B、de 420B、es 395B、fr 435B、it 391B、pt 405B、nl 394B、ja 393B、ko 417B、zh-tw 348B）。

## 事实核验（独立重算）

- 日期/星期（`date -d`，Europe/Moscow）：2026-11-04 三、11-06 五、11-07 六、11-08 日、11-10 二、11-12 四、11-16 一、11-17 二、11-18 三、11-19 四、11-20 五、11-21 六、11-22 日、11-26 四、11-27 五、11-29 日、11-30 一——与文中星期表述一致；11 月 29 日为 11 月最后一个周日，与“День матери 29 ноября”一致。
- 算术：P4 赛果 8 场进球 1+3+1+6+2+3+4+1 = 21，与 Q6 / Q21 一致；P6 图表 38+26+18+18 = 100；11 月工作日 30−9（周末日）−1（11 月 4 日假日）= 20；Simonyan 1926 年生 → 2026 年百年（2026−1926 = 100）。
- P7「Фразы недели」8 句逐字出自本期正文（脚本核验 8/8 在正文内），页码标注正确：P1 ×2、P2、P3、P4、P5、P6 ×2。
- Q150 范文 97 词（`Пример: ` 行实测 97 词，80–100 词要求内）。
- P8 最小字号：11 版印 PDF P8 最小字号均为 9.75pt（SOP 下限），最大 34.50pt。

## 机械门禁（只读跑盘上文件；解释器 `tools/venv/bin/python`）

| 门禁 | 结果 |
|------|------|
| p8.py compare `--total 150`（10 版 fan-out） | 10/10 CLEAN；`missing=[] extra_count=0 uncertain=[] keydiff=[137,138,139,140]`（E 节翻译题预期差异） |
| occlusion_audit.py（11 版 svg/） | 11/11 0 flags，selftest 通过 |
| boxtitle_check.py（11 版） | 11/11 0 DEFECT、0 OBSERVE、0 marginal（it 55 titles、ko 67、其余 57） |
| spill_sweep.py（11 版） | 11/11 0 SPILL（OBSERVE 为邻近文字候选项，非缺陷） |
| pdf_edge_scan.py（印 PDF，200dpi） | 11/11 ok：每版 8 页，0 TOUCH、0 NEAR（`gates/edge.log`） |
| D5 census（census.py：字体 + 弯引号普查） | rc=0；11 版 `cjk_with_latin=0`、`cjk_with_cyrillic=0`；弯引号 2–4 处/版、全部 Newsreader 字体。与第二轮普查相比仅 de（runs 5722→5723，LINEX 回炉句重排）与 zh-tw（runs 6239→6242、cjk_runs 584→585，G-6 修复所致）有微小变化，其余 9 版完全一致；无新增 D5 缺陷 |

head_check.py 未跑：生产目录内无 run.log（构建日志不随生产文件入仓），无输入可查。

## 目视抽查

自印 PDF 渲染 6 页（100dpi，`visual/`）：core P1、core P8、ru-it P1、ru-pt P1、ru-de P2、ru-pt P8。均无溢出/遮挡/缺图；H-1、H-2 在渲染页上肉眼可见（见上）。渲染图读完即清（见§遗留）。

## 观察到但不采纳为发现

- de L538 `синоптики обещают = die Wetterfrösche versprechen`、nl L538 `de weermannen beloven`：口语化译法，含义正确，属风格选择（第二轮同样处理）。
- ja / ko 将 мокрый снег译为 みぞれ / 진눈깨비：各版内一致的本地天气术语，非 G-3 式版内矛盾。
- en L139 `On Tuesday Russia play Venezuela`：英式集合名词复数，第二轮已裁定非缺陷。
- fr L585 金句译文 `Les fêtes professionnelles ne donnent pas de jour férié`（core：`Профессиональные праздники не дают выходных`）：“jour férié”较“jours de repos”略松，但句意（职业节日不放假）完整保留，且同版 L163 关键句用准确的 `n'ajoutent pas de jours de repos`；不列为发现。
- key 112 省略号写法（en `according to...`、de `laut...`、pt `segundo...`）：与 core `据……数据` 的「……」对应，属既定缩写体例。

## 不重报项（按任务）

FIX-LOG 裁定不修项（F-1 P8 key 栏右余量、F-3 Morozko 图注行、ru-nl `Dooi` 不动、de key 126 `Schneeregen` 不动）；第一/二轮已接受残留；`*-ru` 拉丁标题字体问题（已知跨家 D5 系统性问题，另有工人统一修）；`СЛОВО НЕДЕЛИ` 缺 text.md 项（导出器设计局限）。

## 逐版结论

| 版 | 结论 |
|----|------|
| core-ru | 干净 |
| ru-en | 干净 |
| ru-de | 干净 |
| ru-es | 干净 |
| ru-fr | 干净 |
| ru-it | 1 项 low（H-1） |
| ru-pt | 1 项 low（H-2） |
| ru-nl | 干净 |
| ru-ja | 干净 |
| ru-ko | 干净 |
| ru-zh-tw | 干净 |

## 遗留说明

- 本轮为只读校对：未修复、未重建、未 commit、未 push、未跑 lint、未改 SOP。
- 磁盘：开工时 `/home/hatch` 已用 95G（150G 盘，64%），未触发 100G 门限；工作目录 9.7M。
- 渲染图 `visual/` 6 张 PNG 已读完删除；工作目录现 2.7M。
