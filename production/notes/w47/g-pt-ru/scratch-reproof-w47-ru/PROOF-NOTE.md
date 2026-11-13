# W47 ru 家庭独立重校 — PROOF-NOTE

- 校对员：独立校对（未参与建造，全新全量通读）
- 日期：2026-11-12（Thu）
- 范围：11 版，目标语 ru，读者母语 en / de / fr / es / it / pt / nl / ja / ko / zh-cn / zh-tw
- 依据：`~/workspace/weekly-git/SOP.md` §8 全文 + §1.1 字体表；`hidden_files/w47/scratch-d5-plan/D5-PLAN.md` §1；先轮校对注（2026-11-10，core-ru 首轮）已通读
- 结论：**(b) 有问题** — 仅低严重度 3 项（F-1、F-2、F-3），无中/高严重度问题。**不宣称零问题**，因 F-1/F-2/F-3 对照任务给定标准是真实存在的不符。

## 0. 开工核对与工具版本

- 目录枚举：fan-out 10 个（`2026-w47-ru-en/de/es/fr/it/pt/nl/ja/ko/zh-tw`）+ `core-ru/` = 11 版，无多无少。`core-ru/` 即 ru-zh-cn 版（内含 `2026-w47-ru-zh-cn.text.md`、`Lucerna-VOL4.pdf`）；盘上无重复的 ru-zh-cn fan-out 目录，无需字节比对。
- tools/ git HEAD：开工时 `71f4e6f9df302d5322211cdd01437a9ac0f4fec7`；**收尾时已变为 `b9ac29a6f3c640f408965572823e5a1ccebfd1e5`**（commit「tools: D5 gates + p8/occlusion/cover/run_build fixes (W47 review round)」）。按任务要求重跑受影响检查：`p8.py` 与 `occlusion_audit.py` 均有改动，已用新版重跑（见 §1），结果与旧版一致。新 gate `d5_creambox_audit.py`（需 pre-D5 baseline 目录）与 `head_check.py`（需 build run.log）因盘上无 baseline 目录 / 无 run.log，无法运行——boxtitle 检查 + 全量目视已覆盖同类缺陷（均为 0）。
- 磁盘：开工与收尾时均为 93G 已用（门限 100G，未触发）。`/tmp`（512M tmpfs）已满 100%（他家庭校对残留文件所致，非本人文件），半尺寸阅览图改放本 scratch 目录 `view/`，写注后删除。
- 任务措辞「P8 key 100/144」含糊，已按实测处理：逐版测量**全部单行 key**的栏右余量（每版单行 key 数 131–145 不等，core-ru 恰为 144）。

## 1. 机械门（repo venv `tools/venv/bin/python`）

| 检查 | 结果（旧版 tools） | 重跑（新版 tools，HEAD b9ac29a6） |
|---|---|---|
| `tools/p8.py compare`（core vs 各 fan-out） | 10 版全部 CLEAN：150/150 noted，missing=[]，keydiff 仅 [137,138,139,140]（翻译题，信息性） | 相同：10 版 CLEAN，150/150，missing=[]，keydiff=[137,138,139,140]（新版 CLI：`compare --core-dir --edition-dir --target ru --total 150`，比对源为 p8-test.svg） |
| `tools/occlusion_audit.py`（11 版） | 11 版 0 flags（每次自检 OK） | 11 版 0 flags（自检 OK；新版修了 Noto Serif/Sans 量测面假阳性，结论不变） |
| `tools/boxtitle_check.py`（11 版） | 0 DEFECT，0 OBSERVE，0 marginal（core 57 标题/704 正文行；fan-out 55–67 标题，680–759 正文行） | 该文件本次 tools 变更未动，未重跑 |
| D5 字体普查（自写脚本 `/tmp/ru-proof/census.py`） | 全部 11 版：CJK+Latin = 0，CJK+Cyrillic = 0（无拉丁/西里尔文字残留于 Noto Sans CJK 内）；全部弯引号 U+201C/U+201D/U+2019 均在 Newsreader 内。CJK 文本数：core-ru 638，ru-en/de/es/fr/it/pt/nl 各 159，ru-ja 627，ru-ko 1181，ru-zh-tw 635 | — |
| P8 最小字号（PyMuPDF，print PDF 第 8 页） | 全部 11 版最小 9.75pt，恰为 SOP §1.1 底线；字号梯 [9.75, 9.98, 10.35, 10.88, 11.25…] 11 版完全一致 | — |
| `pdffonts`（ru-es / ru-ja print PDF，首遍字体子集爆炸史） | 全部字体 embedded=yes、subsetted=yes，字体清单正常（多 Newsreader 子集为按字号分包，属正常）；无子集爆炸，现版正常，不当作缺陷 | — |

## 2. 每版文件清单（即本次校对的文件；尺寸 + SHA-256 前 12）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| ru-zh-cn（core-ru） | 24,713,345 / `e3c4c0ee155a` | 3,898,257 / `0bdc87e621d7` | 60,953 / `348511e061c2` |
| ru-en | 20,875,448 / `f20b04c8244c` | 3,328,931 / `21781f8396d9` | 62,786 / `5dba64557898` |
| ru-de | 20,880,795 / `0aa0287b13ea` | 3,334,227 / `98f015bd027b` | 63,471 / `d0f9b48c8fab` |
| ru-es | 20,880,148 / `047ef0fbf75a` | 3,333,651 / `662998dc1e54` | 64,176 / `332c8e4f5478` |
| ru-fr | 20,880,952 / `7dbe1f0d6716` | 3,334,434 / `6841ac968654` | 63,361 / `e4cc50fd4195` |
| ru-it | 20,877,054 / `6b79403a69c5` | 3,330,486 / `7c2ecb0479b1` | 63,972 / `0bb5739a9e2a` |
| ru-pt | 20,883,576 / `eb3c2905d2f8` | 3,337,084 / `cc52dfb7f87b` | 65,116 / `ab21732233d8` |
| ru-nl | 20,876,339 / `b355efedd9fc` | 3,329,813 / `15cf757d8482` | 64,013 / `849015f1e920` |
| ru-ja | 27,365,531 / `f65820348bef` | 3,692,485 / `b6fed518a3c1` | 64,477 / `07824474bb88` |
| ru-ko | 21,975,314 / `2f6ecdcc2abf` | 3,494,622 / `a2ea1b41922a` | 65,012 / `5e9bd67201fd` |
| ru-zh-tw | 24,763,703 / `a6c1b4cffbef` | 3,976,325 / `8eb6f61cef46` | 60,850 / `277a24f8a167` |

每版目录另有 `ABSTRACT.txt`、`WEEKLY-KIT.md`、`svg/`（8 页 SVG）、`cards/`（8 张 PNG 1950×2700）。印 PDF 约 20–27MB（图片重），网 PDF 约 3.3–4.0MB。核对时 SHA 重新计算，与开工记录一致，文件未变。

## 3. 全量通读结果（逐版结论）

**印 PDF 8 页逐页目视：88/88 页已看**（生产目录 `cards/*.png` 的半尺寸 975×1350 阅览副本；不重渲染）。每版均核对：P1 刊头 + 配对徽章 + 页脚配对标注、D5 重排版残留（粗体盒标题、P8 变长）、P8 head/subtitle 互撞修复残留、溢出/重叠/压页脚/豆腐块/截断句。**88 页均未见版式缺陷**。各版讲解层语言正确（逐页抽查的词汇注释与 P7 译文均准确，见下）。

- **ru-zh-cn（core-ru）**：P1–P8 全净。刊头「Lucerna + РУССКАЯ ГАЗЕТА VOL.4」；配对「КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ / 正文俄语 讲解简体中文」；页脚「第N版/共8版，VOL.4」。P8 Morozko 图在版（见 F-3）。
- **ru-en**：8/8 净。P1「RUSSIAN TEXT / ENGLISH EXPLANATIONS」，lead「Round 14 is over」，「WORD OF THE WEEK = Black Friday (year-end sale)」；P8「TEST AND ANSWERS」，E 节「Translate into English」，答案「ANSWER KEY – ARRANGED BY PAGE」，Morozko 图按设计缺席（key 占满，无空洞缺陷）。
- **ru-de**：8/8 净。「RUSSISCHER TEXT / DEUTSCHE ERKLÄRUNGEN」；「WORT DER WOCHE = Black Friday (Ausverkauf)」；P7 译文「Alle acht Spiele des 14. Spieltags sind gespielt」等均正确；页脚「Seite N von 8」。
- **ru-es**：8/8 净。「TEXTO EN RUSO / EXPLICACIONES EN ESPAÑOL」；「LA PALABRA = Black Friday (rebajas)」；P7「Los ocho partidos de la jornada 14 han terminado」等正确；页脚「Página N de 8」。
- **ru-fr**：8/8 净。「TEXTE EN RUSSE / EXPLICATIONS EN FRANÇAIS」；「LE MOT DE LA SEMAINE = Black Friday (soldes)」；P7「Les huit matches de la 14e journée sont terminés」等正确；页脚「Page N sur 8」。
- **ru-it**：8/8 净。「TESTI IN RUSSO / SPIEGAZIONI IN ITALIANO」；「LA PAROLA = Black Friday (saldi)」；P7「Tutte e otto le partite della 14ª giornata sono finite」等正确；页脚「Pagina N di 8」。
- **ru-pt**：8/8 净。「TEXTOS EM RUSSO / EXPLICAÇÕES EM PORTUGUÊS」；「PALAVRA SEMANAL = Black Friday (saldos)」；P7「Os oito jogos da jornada 14 já terminaram」等正确；页脚「Página N de 8」。
- **ru-nl**：8/8 净。「TEKSTEN IN HET RUSSISCH / UITLEG IN HET NEDERLANDS」；「WOORD VAN DE WEEK = Black Friday (uitverkoop)」；P7「Alle acht wedstrijden van speelronde 14 zijn gespeeld」等正确；页脚「Pagina N van 8」。
- **ru-ja**：8/8 净。「本文はロシア語 / 解説は日本語」；「今週の単語 = ブラックフライデー」；P7「第14節の8試合はすべて終了した」等正确；页脚「Nページ（全8ページ）」。字体子集正常（见 §1）。
- **ru-ko**：8/8 净。「텍스트는 러시아어 / 해설은 한국어」；「이번 주 단어 = 블랙프라이데이 (연말 세일)」；P7「제14라운드의 여덟 경기가 모두 끝났습니다」等正确；页脚「제 N 면 / 총 8 면」。CJK 文本数 1181 偏高系韩文讲解层逐字注音所致，目视无碎片化异常。
- **ru-zh-tw**：8/8 净。「正文俄語 / 講解繁體中文」；「本週單詞 = 黑色星期五（年末大促）」；P7「14輪的八場比賽全部結束」等正确；页脚「第N版 / 共8版」。P8 Morozko 图在版（见 F-3）。

**text.md 全文**：core-ru 全文已读（839 行，60,953 字节）；其余 10 版俄语正文经 SVG 哈希证明与 core 完全一致（Noto Serif 文本哈希 `6a1e7d9a6d76`，每版 2913 条；core 仅因 P8 Morozko 图注词 + 一处换行 artifact「можно」而不同），讲解层为唯一差异层，已逐版核对 E 节翻译题 137–140（见 §4）并抽查注释。

**P8 答案逐题复核**：1–150 编号连续，答案与题面/原文/图表一致（core 全量核对；fan-out 与 core 的 p8 比对 CLEAN）。P7「Фразы недели」8 句已逐句核对原文与页码；P2 D 25–28、P3 C 39–42、P4 C 57–60、P5 C 75–78、P8 F 141–144 配对 key 已在渲染页上核对。

**事实/日期/星期核验**（core，独立核对）：2026 年 11 月星期（12 日四、16 日一、17 日二、18 日三、19 日四、20 日五、21 日六、22 日日、27 日五、30 日一、29 日为月末周日即母亲节）；11 月俄罗斯 20 工作日 + 10 非工作日（11 月 4 日假日 + 9 个周末日）；第 14 轮总进球 21 = 1+3+1+6+2+3+4+1（8 场比分表核对）；P6 图表 38+26+18+18=100，柱宽与数值成比例；Q150 范文 97 词（80–100 范围内，实数）。**范围限定**：先轮已核的外部事实（RPL 积分榜、83 分钟扳平、第 15 轮赛程、黑色星期五日期、Ozon 2025-11-11 1440 万单、五部首映、节日）本次仅核内部一致性 + 日期/星期，**未独立重查外部来源**。

**ABSTRACT.txt**：11 版全部在位，均为读者母语，内容与本期一致（8 场赛果、31 分并列、乌兹别克斯坦 11 月 12 日、委内瑞拉 11 月 17 日、黑色星期五、11 月 19 日五部首映、大学生节、严寒老人生日、A2–B2、150 道练习）。zh-tw 为繁体字，zh-cn 为简体字；fr 冒号前空格符合法语排版惯例。

**已知缺陷类核对结果**：
- 先轮 D-1（P4 C 选项 a「играет с ЦСКА 4:2」时态错）：**11 版全部已修复**，现均为过去时「победил ЦСКА 4:2」（grep 计数 11 版一致：`играет`=2 均为合法现在时用法，`победил`=3）。
- 17 处字号缩小修复（奶油盒标题溢出 14 处、P8 head/subtitle 互撞 3 处）：现版无残留（boxtitle 0 缺陷 + 88 页目视）。
- ru-es/ru-ja 首遍字体子集爆炸：现版正常（见 §1 pdffonts），不当作缺陷。
- 交叉语言污染扫描：非英文版 text.md 中英文功能词（the/and/with/for/you/this/that）命中 0，ru-nl 仅 2 处均为片名「The Hunger Games」（荷兰亦用此片名，合法）；ru-en 对照组 145 处。

## 4. 发现的问题（仅低严重度 3 项）

### F-1（低）：P8 单行 key 栏右余量低于 +5px 底线 — 9/11 版

- **标准**：任务给定「P8 key 单行栏右余量须在 +5px 底线以上」。
- **方法**：解析各版 p8-test.svg 的 P8 答案 key 文本行，用 PIL 真实墨迹 bbox 量每条单行 key 右端至所属栏右缘的余量；栏右缘（SVG 坐标）：栏1 ≈961.5，栏2 =1411.5，栏3 =1862（页右内容缘，页宽 1950，空白页边 88px）。像素验证：对最差 3 例在渲染 PNG 上量最右深色像素。
- **结果**（单行 key 总数 / 低于底线数 / 具体 key 与余量）：

| 版 | 单行 key 数 | 低于 +5px | 具体（key：余量） | 最小余量 |
|---|---|---|---|---|
| ru-zh-cn（core-ru） | 144 | 1 | 80：2.3px | 2.3px |
| ru-en | 138 | 0 — 通过 | — | 8.0px |
| ru-de | 136 | 2 | 11：4.5px；97：0.8px | 0.8px |
| ru-es | 137 | 1 | 97：3.8px | 3.8px |
| ru-fr | 138 | 0 — 通过 | — | 11.5px |
| ru-it | 137 | 1 | 46：1.0px | 1.0px |
| ru-pt | 138 | 2 | 97：0.8px；**140：−1.9px** | −1.9px |
| ru-nl | 131 | 3 | 81：−0.5px；97：0.8px；140：0.8px | −0.5px |
| ru-ja | 143 | 2 | 80：2.9px；139：0.1px | 0.1px |
| ru-ko | 143 | 2 | 80：4.1px；139：2.8px | 2.8px |
| ru-zh-tw | 145 | 1 | 80：2.3px | 2.3px |

- **像素验证**（渲染 PNG，栏右缘 1862/1411.5）：ru-pt key 140 最右深色像素 x=1863（超缘 1px，与墨迹测算 −1.9px 在 1px 内吻合）；ru-nl key 81 x=1412（超缘 0.5px）；ru-de key 97 x=1410（余 1.5px）。测算与像素一致。
- **严重度：低**。最差仅超栏缘约 2px，进入空白页边（页边宽 88px），无重叠、无触页缘，正常阅读距离不可见；88 页目视亦未见任何溢出。成因系统性：同一长 key 在多版重复低于底线（key 97「Неделя обычная, поэтому ритм ровный。」+ 注释；key 80「«Чёрная пятница» начинается 16 ноября。」+ 注释；key 139/140 翻译题长译文 + 注释）。
- **附带观察**（同 F-1，不另立项）：ru-it key 139 为折行 key，其首行以「играть」结尾，墨迹约触栏缘（最右深色像素 x=1862，恰在缘上）；折行 key 的首行未计入上表单行统计。

### F-2（低）：text.md 中字面占位符「— СТРАНИЦА? —」— 11/11 版

- **位置**：每版 text.md 各 1 处（导出器 `ru_textmd.py:609` 硬编码分隔符，其文件头注明为有意设置的分隔符；PDF 中对应位置为真实「— СТРАНИЦА N —」分隔线）。
- **严重度：低**。仅影响网站正文（text.md）一处分隔行，PDF 印刷版无此问题。先轮校对未提及此项；本次如实记录，不归为新发现的版式缺陷。

### F-3（低）：text.md 末尾 Morozko 图注行 vs 印版图片仅 2 版有图 — 11/11 版

- **事实**：11 版 text.md 末尾均有 Morozko 图注行；印版 P8 的 Morozko 图片按 `content8.py` 条件放置（仅当答案流在第 3 栏结束且有空位），实际仅 core-ru 与 ru-zh-tw 有图（`<image>` 计数 1），其余 9 版为 0。
- **严重度：低**。按设计（非错误），但 9 版 text.md 引用了一张印版中不存在的图片；网站正文与印刷版存在此一处不一致。ru-en P8 目视确认 key 占满、无空洞缺陷。

## 5. 已知格式局限（非新发现，不计入问题）

按先轮 §6 裁定，text.md 缺失表格/盒子属于**导出器设计局限**，非逐版缺陷，本次同样裁定、仅记录：
- P1 目录行（「Стр. 2」–「Стр. 8」）缺失；「СЛОВО НЕДЕЛИ」标题缺失，其正文误归于「В ЭТОМ НОМЕРЕ」标题下；P4 赛果表（8 场）与第 15 轮赛程（8 场）缺失（标题在、行缺失——以原生 `p.text` 循环构建，导出器不遍历）；照片来源（credit）缺失（导出器文档注明有意不导出）。
- 上述缺失在 11 版中模式完全一致；W46 已发版文件相同。

## 6. E 节翻译题 137–140 核对（逐版，读者母语）

11 版 key 全部为正确读者母语，译文准确；印版 P8 与 text.md 的 key 一致（ko 版经 pdftotext 逐字验证，其余经 PyMuPDF/目视验证；en 版 139「On Tuesday Russia play Venezuela」印版与 text.md 一致，英式集合名词复数用法，非缺陷）：

| 版 | 137 | 138 | 139 | 140 |
|---|---|---|---|---|
| zh-cn | 11月17日星期二，大学生节。 | 包裹要追踪、领取并检查。 | 星期二俄罗斯队对阵委内瑞拉队。 | 祝大家大学生节快乐！ |
| en | Tuesday 17 November, Students' Day. | A parcel must be tracked, collected and checked. | On Tuesday Russia play Venezuela. | Happy Students' Day to everyone! |
| de | Dienstag, 17. November, Tag der Studierenden. | Ein Paket muss verfolgt, abgeholt und geprüft werden. | Am Dienstag spielt Russland gegen Venezuela. | Allen einen schönen Tag der Studierenden! |
| es | Martes 17 de noviembre, Día del Estudiante. | Un paquete debe rastrearse, recogerse y revisarse. | El martes Rusia juega contra Venezuela. | ¡Feliz Día del Estudiante a todos! |
| fr | Mardi 17 novembre, Journée des étudiants. | Un colis doit être suivi, retiré et vérifié. | Mardi, la Russie joue contre le Venezuela. | Bonne Journée des étudiants à toutes et à tous ! |
| it | Martedì 17 novembre, Giorno degli studenti. | Un pacco va tracciato, ritirato e controllato. | Martedì la Russia gioca contro il Venezuela. | Buon Giorno degli studenti a tutti! |
| pt | Terça-feira, 17 de novembro, Dia do Estudante. | Uma encomenda deve ser seguida, levantada e verificada. | Na terça-feira a Rússia joga contra a Venezuela. | Feliz Dia do Estudante a todos! |
| nl | Dinsdag 17 november, Studentendag. | Een pakket moet gevolgd, opgehaald en gecontroleerd worden. | Op dinsdag speelt Rusland tegen Venezuela. | Fijne Studentendag allemaal! |
| ja | 11月17日（火）、学生の日。 | 荷物は追跡し、受け取り、確認すること。 | 火曜、ロシアはベネズエラと対戦する。 | みなさん、学生の日おめでとう！ |
| ko | 11월 17일 화요일, 대학생의 날. | 소포는 추적하고, 찾아가고, 확인해야 합니다. | 화요일 러시아는 베네수엘라와 맞붙습니다. | 모두 대학생의 날 축하합니다! |
| zh-tw | 11月17日星期二，大學生節。 | 包裹要追蹤、領取並檢查。 | 星期二俄羅斯隊對陣委內瑞拉隊。 | 祝大家大學生節快樂！ |

## 7. 结论

- **结论 (b)：有问题 — 仅低严重度 3 项**：F-1（P8 单行 key 余量低于 +5px 底线，9/11 版，1–3 条/版，最差超栏缘约 2px，不可见）、F-2（text.md 占位符「— СТРАНИЦА? —」，11/11 版）、F-3（text.md Morozko 图注 vs 印版仅 2 版有图）。
- **无中/高严重度问题**：88 页印版无溢出/重叠/压页脚/豆腐块/截断；P8 答案 150/150 完整一致；D5 字体归属正确；先轮 D-1 与 17 处字号修复均无残留；ru-es/ru-ja 字体子集正常；P8 最小字号 9.75pt 恰达底线；摘要、配对徽章、页脚标注 11 版全部正确。
- 仅校对，未修复、未重建、未 commit、未 push、未跑 lint；读写限于 `production/2026-w47/` 与 `hidden_files/w47/`。
- 工作文件：阅览副本 `scratch-reproof-w47-ru/view/`（80 张半尺寸图）已删除；测量脚本存于 `/tmp/ru-proof/`（临时，VM 重启即失）；机械门报告存于 `/tmp/occ-*.json` 与 `/tmp/ru-proof/boxtitle/`（临时）。
