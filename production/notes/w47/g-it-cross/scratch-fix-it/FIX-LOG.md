# FIX-LOG — W47 it 家庭修复（F-1/F-2/F-3/F-4/F-5/core-1）

**修理工**：W47 it 家庭修复工人（只修 it 家 11 版，不碰其他家庭、其他周；不 commit、不 push、不跑 lint）
**日期**：2026-11-12
**工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-it/`
**校对结论**：`../scratch-reproof-w47-it/PROOF-NOTE.md`（第二派独立重校；协调员已独立核实属实，照此修）
**SOP 依据**：`~/workspace/weekly-git/SOP.md` §8（修源头→重渲染整版→门禁→KIT→FIX-LOG）
**解释器**：`~/workspace/weekly-git/tools/venv/bin/python`
**备份**：`scratch-fix-it/backup/<edition>/`（改前 *.py + *.txt + *.md + *.pdf + svg/*.svg 全量快照，207M；cards/ 与 assets/ 未备——cards 可由 render.py 重建，assets 是输入未动）
**磁盘**：开工 `df` 已用 93G（<100G 门限）

## 0. 改前状态（实测，非抄校对结论）

| 版 | 印 PDF 字节 / SHA-256 前12 | 网 PDF 字节 / SHA-256 前12 | text.md 字节 / SHA-256 前12 |
|---|---|---|---|
| core-it (it-zh-cn) | 14,833,164 / `f867980ae60d` | 1,540,034 / `aceaf1055042` | 52,655 / `9eb9ee066254` |
| it-en | 13,497,072 / `6f0bbf408826` | 1,215,817 / `da29562db637` | 55,183 / `ad311b5bf59a` |
| it-de | 13,499,365 / `365952141076` | 1,218,125 / `e92b6b99d517` | 56,662 / `de0aa214818e` |
| it-fr | 13,496,942 / `02e2b67cdb96` | 1,215,685 / `1b26c4d53d58` | 56,517 / `aca1356c0c90` |
| it-es | 13,497,643 / `5c703a6665d2` | 1,216,392 / `f602876a0f91` | 56,193 / `4fd5647e2b7a` |
| it-pt | 13,500,354 / `30749b8d69ec` | 1,219,136 / `ddb897ef9a68` | 55,718 / `e01360ae9c40` |
| it-nl | 13,495,361 / `cbd50234b442` | 1,214,079 / `35a4070da964` | 55,488 / `b13ef7a7abe0` |
| it-ru | 13,752,905 / `ead7a5eed56f` | 1,465,974 / `f3272028c9a2` | 67,731 / `47c0471515d3` |
| it-ja | 21,050,074 / `52ed13225c1b` | 1,697,194 / `4f256d24c59e` | 58,165 / `5ac2ecf5abb2` |
| it-ko | 15,803,764 / `9815a52d5e9b` | 1,484,263 / `35a222e5f920` | 57,326 / `d4d0c6c1a004` |
| it-zh-tw | 14,906,567 / `78f1e78c3697` | 1,639,361 / `4a4a3f58fac3` | 52,494 / `c18ad203cf49` |

与 PROOF-NOTE 所记 11 版 SHA 逐项一致。

### 0.1 F-1 改前间隙（PyMuPDF 实测印 PDF P1，pt；日期左端 x=1069.3 固定）

| 版 | 标语末词右端 | 间隙 | 结论 |
|---|---|---|---|
| it-en | READING 1086.6 | −17.3 | 重叠 |
| it-fr | ITALIENS 1080.4 | −11.1 | 重叠 |
| it-pt | LEEMSETTIMANA 合并 span | ≤0（词界消失） | 重叠 |
| it-nl | LEZENSETTIMANA 合并 span | ≤0（词界消失） | 重叠 |
| it-ru | ИТАЛЬЯНЦЫSETTIMANA 合并 span | ≤0（词界消失） | 重叠 |
| it-de | LIEST 1064.3 | +5.0 | 紧但未撞，不动 |
| it-es | ITALIA 1037.6 | +31.7 | 干净 |
| it-ja | （CJK 标语末）1026.4 | +42.9 | 干净 |
| it-ko | （CJK 标语末）966.3 | +103.0 | 干净 |
| it-zh-tw | （CJK 标语末）983.5 | +85.8 | 干净 |
| core-it | （CJK 标语末）983.5 | +85.8 | 干净 |

### 0.2 F-2 改前

印 PDF P6 `pdftotext`：10 版为 `NOV.Scade`（core/en/de/fr/es/pt/nl/ja/ko/zh-tw）；it-ru 提取为 `NOV. Scade`（字体度量差异致 pdftotext 断词，SVG 源头与他版相同，见 §1.2）。SVG 实测：标签 `MAR 17 NOV.` 墨迹 x=1461.5–1601.5（宽 140.0px），正文首行 x=1603.5，间隙仅 2.0px；其余三行间隙 36–67px。

### 0.3 F-3 改前

7 处模板串（意大利语答案注，全家 11 版每串恰 1 处，均在 content12.py 5 处 + content34.py 2 处）：
`attraversare：i veneziani → attraversano`、`portare：i fedeli → portano`、`piantare：noi → piantiamo`、`pregare：la famiglia → prega`、`mangiare：la famiglia → mangia`、`vincere：ha vinto`、`pareggiare：ha pareggiato`。其余 `：` 均为 CJK 讲解文本合法标点（core-it content12.py:114 `“la vetta”：榜首…`、content34.py 各 `arrivare 用 essere：…` 等），不动。

### 0.4 text.md 导出基线（改前核实）

W46 出口商 `export_it_textmd.py`（与 `scratch-fanout-it/build_edition.py` 同款导出块）对 11 版改前源文件重导出，与盘上 text.md 比对：8 版字节全等；**3 版有既存漂移**（与本次修复无关，系 D5 轮改短了源头盒标题后 text.md 未重导出——PDF 以源头为准）：
- it-es：2 行不同（L45 `LA SETTIMANA IN CIFRE　LA SEMANA EN CIFRAS`→源头 `EN CIFRAS`；L205 `LA FRASE PER RICORDARE　PARA RECORDAR`→源头 `RECORDAR`）
- it-ru：1 行不同（L45 `НЕДЕЛЯ В ЦИФРАХ`→源头 `В ЦИФРАХ`）
- it-ko：2 行不同（L45 `숫자로 보는 이번 주`→源头 `숫자로 보는`；L205 `기억해 두세요`→源头 `기억해`）

本次按任务流程重导出 text.md 后，这 5 行将与源头/PDF 一致（漂移自动消除，属修复附带结果，记于此）。

### 0.5 F-5 说明

8 版 Q44（content34.py:98）与 Q134（content8.py:62）注同为缩短式，仅 `主语 + 动词`，漏地点与日期；en/de/core-it 三版为完整注。缩短非故意（同句的完整注在三版存在，Q136 注在 6 版含地点），故按任务裁定补全。**范围外观察（不修）**：it-nl 与 it-ru 的 Q136 注（`Il torrone si assaggia a Cremona.`）亦缺地点（`Onderwerp + werkwoord`／`Подлежащее + глагол`，text.md:965/1289 可查），与 PROOF-NOTE「Q136 注均含地点」不符——不在本次任务范围内，未动，提请协调员另行裁定。

### 0.6 text.md 重导出陷阱核查（ru 家 FIX-LOG §7 补充注意，2026-11-12）

- ru 家陷阱：其导出器 `ru_textmd.py` 的 `do_p_text` 只收 sans 粗体 ≥24pt 标题，D5 缩到 22/23pt 的框题会在重导出时被丢掉（ru 家回补 de 2、es 1、fr 2、nl 1、pt 2、en 1 行）。
- **it 家不中此陷阱，核实两点**：(1) it 家导出器是 W46 `export_it_textmd.py`，`visit()` 对 `text`／`box`／`head`／`shead` 调用无条件收录字符串，**无任何字号阈值**（源码 L216–270 逐行核对）；(2) it 家 text.md 每版仅含 1 行 `###`（导出器自加的 `### Risposte`），无 `###` 章节标题行可丢；改前基线（§0.4）新鲜导出与盘上文件 8 版字节全等、3 版仅差 5 行漂移行，已实证无丢行。
- **仍按补充注意执行既定流程**：每版重导出先干跑到 `/tmp/fix-it-dryrun/` 再与修前文件 diff；落盘时若发现被丢的标题行，在原位置逐字回补（不改导出器、不动源码字号）；最终每版与修前文件的 diff 只含 §1 有意改的行 + §0.4 已登记的 5 行漂移修正行（es 2、ru 1、ko 2，逐行与印 PDF 文本层核对一致：ru P1 文本层 `В ЦИФРАХ`、ko `숫자로 보는`／`기억해`、es `EN CIFRAS`／`RECORDAR` 均为缩短后形态）。

## 1. 源头改动

（逐项填：文件、改前→改后、核实计数）

### 1.1 F-1：缩短 5 版读者语副标（content12.py:15，日期不动）

| 版 | 改前读者语段 | 改后读者语段 |
|---|---|---|
| it-en | `EVERY WEEK　THE ITALIAN THAT ITALIANS ARE READING` | `EVERY WEEK IN ITALIAN` |
| it-fr | `CHAQUE SEMAINE　L'ITALIEN QUE LISENT LES ITALIENS` | `CHAQUE SEMAINE EN ITALIEN` |
| it-pt | `TODA SEMANA　O ITALIANO QUE OS ITALIANOS LEEM` | `TODA SEMANA EM ITALIANO` |
| it-nl | `ELKE WEEK　HET ITALIAANS DAT DE ITALIANEN LEZEN` | `ELKE WEEK IN HET ITALIAANS` |
| it-ru | `КАЖДУЮ НЕДЕЛЮ　ИТАЛЬЯНСКИЙ, КОТОРЫЙ ЧИТАЮТ ИТАЛЬЯНЦЫ` | `КАЖДУЮ НЕДЕЛЮ ПО-ИТАЛЬЯНСКИ` |

全行仍为 `OGNI SETTIMANA IN ITALIANO　<读者语段>`，居中 x=975，字号 17 不变。

### 1.2 F-2：时间线 MAR 行正文右移（content56.py，11 版同改）

标签墨迹宽 140.0px（x=bx+22 起，止于 bx+161.9），正文原 x=bx+164 仅留 2.0px。改循环：仅 `MAR 17 NOV.` 行正文 x→bx+172（间隙 10.0px），右缘保持 bx+CW−22（宽 CW−186→CW−194）；其余三行 x 与宽不变。首行 `Scade il termine per gli` 墨迹宽 223.0px < 新宽 228.5px，不断行（行数不变，无下行重排）。

### 1.3 F-3：7 处模板全角冒号改半角（content12.py + content34.py，11 版同改）

逐串替换 `：`→`:`，每版恰 7 处；其余 `：` 逐版核实未动。

### 1.4 F-4：P2 盒标题改回「记住」类译法（content12.py，5 版）

tsize 由 `tools/boxtitle_check.py` 的 `ink_bbox`（与 D5 校准：fr 旧标题 @23 测得 margin −44.3，与 D5 记录 +44.3 溢出完全一致）实测选定，盒宽 422.5px、标题起 x=盒左+18：

| 版 | 改前标题 | 改后标题 | tsize 改前→改后 | 墨迹右缘 / 盒右缘 422.5 | 余量 |
|---|---|---|---|---|---|
| it-fr | `LA FRASE PER RICORDARE　DEVISE` | `LA FRASE PER RICORDARE　À RETENIR` | 20.5→18.5 | 413.3 | +9.2 |
| it-pt | `LA FRASE PER RICORDARE　LEMA` | `LA FRASE PER RICORDARE　PARA RECORDAR` | 21→16 | 413.8 | +8.7 |
| it-nl | `LA FRASE PER RICORDARE　LEUS` | `LA FRASE PER RICORDARE　OM TE ONTHOUDEN` | 21.5→15 | 415.4 | +7.1 |
| it-zh-tw | `LA FRASE PER RICORDARE　口訣` | `LA FRASE PER RICORDARE　請記住` | （默认 23）→21.5 | 415.2 | +7.3 |
| core-it | `LA FRASE PER RICORDARE　口诀` | `LA FRASE PER RICORDARE　请记住` | （默认 23）→21.5 | 415.2 | +7.3 |

pt @16 与 es 版 D5 实测「PARA RECORDAR 需 16pt 方合」一致。es 版 `RECORDAR`（D5 已缩短，义为记住）不在 F-4 范围，不动。

### 1.5 F-5：Q44/Q134 注补全（content34.py:98 + content8.py:62，8 版）

按 Q136 同版注的「地点」词形补全（fr `lieu`、es `lugar`、pt `lugar`、ja `場所`、ko `장소`、zh-tw `地點`；nl/ru 的 Q136 注亦缩短，故按 en `place` 直译 `plaats`／`место`）：

| 版 | 改前 | 改后 |
|---|---|---|
| it-fr | `Sujet + verbe` | `Sujet + verbe + lieu + date` |
| it-es | `Sujeto + verbo` | `Sujeto + verbo + lugar + fecha` |
| it-pt | `Sujeito + verbo` | `Sujeito + verbo + lugar + data` |
| it-nl | `Onderwerp + werkwoord` | `Onderwerp + werkwoord + plaats + datum` |
| it-ru | `Подлежащее + глагол` | `Подлежащее + глагол + место + дата` |
| it-ja | `主語 + 動詞` | `主語 + 動詞 + 場所 + 日付` |
| it-ko | `주어 + 동사` | `주어 + 동사 + 장소 + 날짜` |
| it-zh-tw | `主語 + 動詞` | `主語 + 動詞 + 地點 + 日期` |

替换以含题钥 `Eurochocolate chiude a Perugia il 22 novembre.` 的整行匹配，每版恰 2 处；Q136 行未动。

### 1.6 core-1：页脚与摘要补配对标注（仅 core-it）

- 页脚 `bslib4.py:67`：`La Lucerna　意大利语周报 VOL.4　LUCERNA ITALIAN WEEKLY` → `La Lucerna　意大利语周报 VOL.4　正文意大利语　讲解简体中文`（照 zh-tw `La Lucerna　義大利語週報 VOL.4　正文義大利語　講解繁體中文` 格式；`LUCERNA ITALIAN WEEKLY` 只在 core-it bslib4.py:67 与 8 个 SVG 内，源头一处改动即覆盖 8 版页脚）。
- 摘要 `ABSTRACT.txt`：`意大利语 A2–B2` → `意大利语正文与简体中文讲解，A2–B2`（照 zh-tw 摘要 `義大利語正文與繁體中文講解，A2–B2 級別` 位置）。
- 仅改 ABSTRACT.txt，不重渲染摘要（摘要不进 PDF）；页脚在 PDF 内，core-it 须重渲染。
- KIT §1 Format 行内页脚引文同步更新为新页脚。

### 1.7 R-1：ru P8-keys 溢出的补偿缩短（F-5 + Q136 的直接后果，第二接替工人 2026-11-12 补）

- 现象：ru 重建 run.py 报 `!! FLOW OVERFLOW [P8-keys] col 3 y=2547 need 15 bottom 2552`，flow end 2580/2552（超 28px）。其余 10 版均无此警告。
- 根因（实测）：ru P8-keys 本已最紧——D5 版末行基线 2545.3，flow end ≈2561（已悄悄超底 9px，但末段 `_fit` 检查只看段首，故无警告；KIT §9 亦记「only 23 px spare」）。F-5（Q44/Q134 注各 +14 字）未增行（两注本已折 2 行）；Q136 注 `+ место` 使 Q136 由 1 行变 2 行（`136. … — Подлежащее + глагол +` 391.9px + `место` 38.9px），col 4 自 Q145 起下移 14.8px，末段 Q150 触发 `_fit` 警告。
- 补偿（沿用本家先例：KIT §9 build2「Q29 注缩短使 2 行答案变 1 行」）：把两处 `nevichi` 注 `è possibile che + сослагательное наклонение nevichi` → `è possibile che + сослагательное nevichi`（content56.py:219 P6 Q94 + content7.py:54 P7 Q110，两处同改）。实测：改后单行 340.3px < 422.5px，两题答案各由 2 行变 1 行，共省 2×14.82px ≈ 29.6px，抵消 Q136 的 +14.8px 并把 flow end 拉回 2552 底线内。完整术语「сослагательное наклонение」仍保留在 P7 桥段 content7.py:50（`После è probabile che / è possibile che / bisogna che — сослагательное наклонение`），教学信息未丢；题干本身含 `È possibile che`，触发语未丢。
- text.md 影响：nevichi 注在 text.md 占 4 行（P6/P7 练习行 + 答案区 Q94/Q110），故 ru 预期改动行由 22 增至 26；rebuild_one.py MARKERS 补 `nevichi`。F-5/Q136 的裁定文本本身一字未动。

### 1.8 Q136 补全（协调员新增裁定，第二接替工人 2026-11-12 执行；§0.5 的范围外观察就此结案）

- it-nl content8.py:66：`Il torrone si assaggia a Cremona.` 注 `Onderwerp + werkwoord` → `Onderwerp + werkwoord + plaats`（照 en 版 `Subject + verb + place`，加地点）。
- it-ru content8.py:66：同句注 `Подлежащее + глагол` → `Подлежащее + глагол + место`。
- 每版 text.md 占 2 行（练习行 + 答案区），故 nl/ru 预期改动行由 20 增至 22（ru 再 +4 行 R-1，见 §1.7，合计 26）。
- 注意：Q136 注只在 content8.py:66 一处（f.ex）；content34.py 无此句——text.md 里出现两次是导出器把同一 f.ex 同时写进练习区与答案区，不是两个源头。

## 2. 重建与门禁

**分工**：第一任工人（900dce54，被运行时重启中断）已完成源头改动 §1.1–§1.6，并重建了 it-en（全套）与 it-de（run+render+text.md 落盘，webpdf 未跑——其 `rebuild_one.py` 在 `os.replace` 跨设备复制处崩溃，见下）。第二接替工人接手时先逐项核实 §1.1–§1.6 均已在盘上（F-1 五版副标、F-2 `bx+172` 11 版、F-3 模板冒号、F-4 五版盒标题、F-5 八版注、core-1 页脚+摘要），再补 Q136（§1.8）与 R-1（§1.7），然后重建其余 9 版 + it-de 的 webpdf。

**工具修补（第二工人）**：
- `rebuild_one.py`：dry-run 目录由 `/tmp/fix-it-dryrun/` 改为 scratch 内 `dryrun/`——/tmp 在两任工人之间被清掉，fr 首跑即以 `FileNotFoundError` 失败；另把 `os.replace` 改为 `shutil.copyfile`（/tmp 与 workspace 跨设备，it-de 首跑即崩于此）；MARKERS 补 `Il torrone si assaggia a Cremona`（Q136 行）与 `nevichi`（R-1 行），否则门禁误判为意外改动行。
- `gates_it.sh` 本身无改；core-it 门禁首跑报 FAIL 只是 harness 取错 run 日志名（找 `run-core-it.log`，实际为 `run-2026-w47-it-zh-cn.log`），补拷一份后重跑即 ALL-GREEN。

**重建结果**（run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；text.md 干跑 diff 只含预期行、无丢行；每版印/网 PDF + text.md 均落盘）：

| 版 | text.md 改动行 | 印 PDF 字节 / SHA-256 前12 | 网 PDF 字节 / SHA-256 前12 | text.md 字节 / SHA-256 前12 |
|---|---|---|---|---|
| core-it (it-zh-cn) | 15 | 14,839,774 / `77d33bf8c581` | 1,546,123 / `7680a0ea63ac` | 52,630 / `c6e9ef6c9f0a` |
| it-en | 15 | 13,496,925 / `aeae0796361c` | 1,215,698 / `e071a54f8f30` | 55,126 / `a4d863d96180` |
| it-de | 14 | 13,499,265 / `8cf7241a5d60` | 1,218,051 / `13414d0fbe1b` | 56,634 / `27f58fca0f39` |
| it-fr | 20 | 13,497,005 / `ffb20e7b9620` | 1,215,747 / `d08db2eb54b2` | 56,524 / `b4d1ec47ff3a` |
| it-es | 20 | 13,497,563 / `4393ba30bd49` | 1,216,301 / `c40c7a0067bd` | 56,214 / `e19cf39d5ef6` |
| it-pt | 20 | 13,500,238 / `c4d4fe0f005e` | 1,218,997 / `a6e7e8365466` | 55,736 / `03cc7389d3ed` |
| it-nl | 22 | 13,495,268 / `b5a24a8f4234` | 1,213,994 / `8fc2d76c044a` | 55,535 / `92ddd5838d6f` |
| it-ru | 26 | 13,752,697 / `af296c0525ea` | 1,465,756 / `597e400ffcec` | 67,681 / `298c2cd79bb8` |
| it-ja | 18 | 21,050,187 / `38a236a3d0ca` | 1,697,338 / `e035db45098e` | 58,209 / `3dafa38c8b40` |
| it-ko | 20 | 15,803,899 / `66dffb4ebd5c` | 1,484,256 / `7419a5a624e5` | 57,349 / `c37668224de7` |
| it-zh-tw | 19 | 14,907,350 / `45abf7bfc8a7` | 1,640,994 / `6d7a1efc737c` | 52,541 / `cf5a828688a3` |

改动行构成（每版均由门禁逐行校验，只含 §1 有意改的行 + §0.4 已登记漂移行）：F-1 副标 1 行（en/fr/pt/nl/ru）、F-3 14 行（7 串×练习区+答案区）、F-4 盒标题 1 行（fr/pt/nl/zh-tw/core）、F-5 Q44/Q134 注 4 行（fr/es/pt/nl/ru/ja/ko/zh-tw）、Q136 注 2 行（nl/ru）、R-1 nevichi 注 4 行（ru）、漂移 es 2 / ru 1 / ko 2。F-2 时间线不在 text.md 导出范围内，占 0 行；core-1 页脚/摘要亦不在 text.md 内，占 0 行。

**门禁结果（11/11 ALL-GREEN）**：每版 run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 150/150、compare vs core-it CLEAN（keydiff=[137,138,139]，读者语翻译属设计差异；core-it 自身跳过 compare）；D5 census 0/0/0（ru noto_sans_elements=777，西里尔在 Noto Sans，属设计）；boxtitle 0 DEFECT；spill 0 SPILL；edge 0 TOUCH / 0 NEAR；印/网文字层多重集相等（it-ko 仅差 1 换行，已知 pdftotext 噪声，nonws diff 0）。逐版数字：

| 版 | boxtitle（titles/body） | spill（boxes/cand） | 印=网文字层字符数 |
|---|---|---|---|
| core-it | 24 / 320 | 29 / 101 | 38,078 |
| it-en | 18 / 256 | 29 / 69 | 43,831 |
| it-de | 22 / 259 | 29 / 71 | 44,743 |
| it-fr | 20 / 248 | 29 / 68 | 44,641 |
| it-es | 20 / 249 | 29 / 70 | 44,590 |
| it-pt | 22 / 247 | 29 / 68 | 44,217 |
| it-nl | 22 / 252 | 29 / 68 | 44,674 |
| it-ru | 26 / 320 | 29 / 69 | 44,243 |
| it-ja | 24 / 341 | 29 / 107 | 38,957 |
| it-ko | 36 / 493 | 29 / 177 | 39,407（网 39,406，差 1 换行） |
| it-zh-tw | 24 / 325 | 29 / 102 | 37,917 |

门禁日志：`logs/gates-<slug>.log` + `gates-<slug>/`（it-en 为第一任工人所跑 `gates-2026-w47-it-en/`；core-it 重跑后 `logs/gates-core-it.log` 为 ALL-GREEN）。ru P8-keys flow end 2543/2552（R-1 之后，余量 9px；D5 版为 ≈2561，已悄悄超底 9px 且无警告——见 §1.7）。

## 3. KIT 更新

11 版 WEEKLY-KIT.md 各追加一节「Fix round — W47 it proof fixes F-1/F-2/F-3/F-4/F-5/core-1」（`update_kits.py` 写入，逐版核对新 SHA 与字节数无误）：core-it §12、it-en §16、it-de §16、it-fr §14、it-es §14、it-pt §14、it-nl §15、it-ru §17、it-ja §14、it-ko §14、it-zh-tw §15；每节含一条修复 bullet（各版适用项）、构建与门禁摘要、新旧三 SHA（新 SHA 全文，旧 D5 SHA 保留备查）。另按 §1.6 补做了 core-it KIT §1 Format 行页脚引文更新（`LUCERNA ITALIAN WEEKLY` → `正文意大利语　讲解简体中文`；§12 bullet 内引用的旧页脚原文属历史记录，保留）。

## 4. 改后核实（F-1 间隙 / F-2 / F-3 计数）

**F-1（五版副标右端与日期左端间隙，PyMuPDF 实测印 PDF P1，pt；`measure/ f1-post.json`）**：it-en 114.1、it-fr 92.4、it-pt 97.8、it-nl 91.6、it-ru 111.4——全部 ≥10pt。P1 刊头行五版逐版目视（`/tmp/fix-it-visual/it-{en,fr,pt,nl,ru}-p1-top.png`）：标语与 `SETTIMANA DAL 16 AL 22 NOVEMBRE 2026` 之间空白清晰、词界完整，无压叠。未修版间隙不变：it-de 5.0（观察）、it-es 31.7、it-ja 42.9、it-ko 103.0、it-zh-tw 85.8、core-it 85.8。

**F-2（P6 `NOV.Scade` 已分开）**：11 版印 PDF P6 `pdftotext` 均为 `NOV. Scade`（含 it-ru）。SVG 核实（core-it）：标签 `MAR 17 NOV.` x=1461.5，正文首行 x=1611.5（bx+172，标签墨迹止于 1601.4，间隙 10.1px）；行数不变——改前改后同为 3 行（`Scade il termine per gli` / `emendamenti, alle ore` / `18.`，末行 `18.` 单占一行改前已然）。

**F-3（计数）**：11 版 P8 SVG 内 7 处模板全角冒号残留均为 0；抽查 en/ru/core 半角已为 7 处。CJK 讲解层内合法「：」未动（ja/zh-tw/core 的 `：` 总数不变——门禁 text.md diff 只含 7 串×2 区的改动行，可证）。

**F-4（五版盒标题余量，`boxtitle_check` ink_bbox 实测 + 门禁 boxtitle 0 DEFECT 佐证）**：fr `À RETENIR` @18.5 余量 +9.2px、pt `PARA RECORDAR` @16 余量 +8.7px、nl `OM TE ONTHOUDEN` @15 余量 +7.1px、zh-tw `請記住` @21.5 余量 +7.3px、core `请记住` @21.5 余量 +7.3px。PDF P2 文字层核实：五版新标题均在位、旧词（DEVISE/LEMA/LEUS/口訣/口诀）均已消失。

**core-1（页脚与摘要）**：PyMuPDF span 核实：印 PDF 8 版页脚均为 `La Lucerna　意大利语周报 VOL.4　正文意大利语　讲解简体中文`（P1 span x1=441.1，与 zh-tw 页脚同版式），`LUCERNA ITALIAN WEEKLY` 全书 0 处；网 PDF 同样。ABSTRACT.txt 含 `意大利语正文与简体中文讲解，A2–B2`。

**Q136（两版补全）**：nl/ru text.md 两处均已为补全注（练习行 L965 + 答案区 L1289：`Onderwerp + werkwoord + plaats`／`Подлежащее + глагол + место`）；门禁 p8 compare CLEAN（Q136 键未变，只改注）。

**未动项复核**：`svglib.py` 11 版均未动（it-ru 拉丁标题字体问题另有跨家工人处理）；观察项（it-de P1 间隙 9px、it-zh-tw cifre 标题余量、CJK 手写变体块、it-ko 1 换行文字层差异）均未动。无 commit、无 push、无 lint；磁盘收尾 94G（<100G 门限）。
