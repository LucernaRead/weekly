# W47 ko 家庭修复日志（FIX-LOG）

- 任务：修复独立重校（scratch-reproof-w47-ko/PROOF-NOTE.md，2026-11-12）发现的 5 条问题（1 中等 + 4 轻微）+ core-ko 页脚附带小修；重渲染 11 版并复核门禁。
- 范围：仅 `production/2026-w47/` 下 ko 家 11 版（`core-ko/` + `2026-w47-ko-de/en/es/fr/it/ja/nl/pt/ru/zh-tw/`）。不 commit、不 push、不跑 lint、不碰其他家庭/其他周。
- 磁盘开工：93G 已用 / 57G 可用（门限 ≥100G 停手，未触发）。
- 构建结构（据 D5-REPORT / scratch-d5-ko/RUN-LOG.md）：每版自带 `content*.py` 副本（韩文题干 11 版字节相同，讲解层按读者语），`run.py` 串行 content12→34→56→7→8 累积 REG（TOTAL 150），P8 答案键由 REG 自动生成（`content8.py` 末段按页分组打印 `n. key — note`）。故 F1 改题干即同步改 P8 键；`note`（读者语注释）须逐版写。渲染：`tools/venv/bin/python run.py` → `render.py`（PNG + 印 PDF）→ `tools/webpdf.py`（网 PDF）；text.md 由 `textmd.py` 从源码导出（去重：相同题干只列一次——这正是改前 text.md 只列 144 道的原因）。
- 改前指纹：见 `prefix-fingerprints.txt`（与 PROOF-NOTE 逐版一致）。

## F1 新题草案（6 道）与事实出处

替换原则：保留首次出现（P1 Q8/Q9/Q10、P2 Q11/Q18、P3 Q37 不动），只换后出的 6 格；新题取自本期同一页/同一篇文章的其他事实，题型与原格同型，3 选项 + 1 正确答案，长度与原题相近。

| 格 | 页/区 | 原题（删） | 新题（韩文题干 + 选项 + 答案） | 事实出处（本期文章原文） | 外部核对 |
|---|---|---|---|---|---|
| Q12 | P2 A 单选 | 김장비용은 지난해보다 어떻게 됐어요? A. 9.0% 내렸어요 · B. 9.0% 올랐어요 · C. 그대로예요（答 A） | 김장비용은 평년보다 어떻게 됐어요? A. 13.4% 낮아요 · B. 13.4% 높아요 · C. 그대로예요（答 A） | P2 正文第 1 段："지난해 11월 상순 평균 219,071원보다 9.0% 내렸어요. 평년보다도 13.4% 낮아요." | PROOF-NOTE 事实核验：较平年降 13.4% ✓（199456/219071=0.9105） |
| Q13 | P2 A 单选 | 김치의 날은 언제예요? A. 11월 22일 · B. 11월 19일 · C. 11월 28일（答 A） | 할인 행사에서 김장 재료는 몇 종을 팔아요? A. 6종 · B. 4종 · C. 20종（答 A） | P2 正文第 3 段："하나로마트 18곳에서 김장 재료 6종을 최대 반값에 팔아요." | PROOF-NOTE：首尔折扣 11/5–11，Hanaro Mart 首尔 18 店，6 种食材至多半价 ✓ |
| Q22 | P2 C 填空 | 배추 20포기는 ___원이에요。（答 54,980） | 고춧가루는 ___% 내렸어요。（答 1.8） | P2 正文第 2 段："고춧가루는 1.8%, 무는 5.6% 내렸어요." | PROOF-NOTE：辣椒粉 −1.8%、萝卜 −5.6% ✓ |
| Q47 | P4 A 单选 | 한국시리즈에서 우승한 팀은 어느 팀이에요? A. 삼성 · B. kt wiz · C. LG（答 A） | 삼성의 우승은 통산 몇 번째예요? A. 아홉 번째 · B. 다섯 번째 · C. 열두 번째（答 A） | P4 正文第 2 段："통산 아홉 번째 우승이에요." | PROOF-NOTE：通算第 9 冠（含 1985 合并冠军）✓ |
| Q74 | P5 B 填空 | 11월 22일은 ___이에요。（答 김치의 날） | 수험표를 잃어버리면 당일 아침 ___시까지 신고하면 다시 받을 수 있어요。（答 8） | P5 正文第 2 段："수험표를 잃어버리면 당일 아침 8시까지 시험장 관리본부에 신고하면 다시 받을 수 있어요." | 本期文章原文逐字（P5 第 2 段）；PROOF-NOTE 未单列此条，但与 P5 正文逐字一致 |
| Q102 | P7 A2 单选 | 김치의 날은 언제예요? A. 11월 22일 · B. 11월 19일 · C. 11월 28일（答 A） | 김치의 날은 언제 법으로 정해졌어요? A. 2020년 2월 · B. 2013년 · C. 2022년（答 A） | P7 A2 栏正文："김치의 날은 2020년 2월에 법으로 정한 기념일이에요." | PROOF-NOTE：泡菜日法定纪念日（2020 年 2 月指定）✓；干扰项 2013 年为泡菜文化 UNESCO 列入年（P2/P3 正文），属合理干扰项 |

新题与现存题不重复核对：Q12 新题干（평년보다）/ Q13（6종）/ Q22（고춧가루 1.8%）/ Q47（통산 아홉 번째）/ Q74（수험표 분실 8시 신고）/ Q102（법으로 정해졌어요）均无现存同题干；Q102 与 Q29/Q9/Q13 原题（김치의 날은 언제예요）题干不同。近似重复（Q29、Q67/Q92/Q120/Q121、Q68/Q86、Q33/Q89/Q110、Q15/Q31）按任务要求不动。

各版读者语注释（P8 键用，与各版原注释风格一致）：

| 格 | zh-cn | zh-tw | en | de | fr | es | it | pt | nl | ru | ja |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q12 | 比平年低13.4% | 比平年低13.4% | 13.4% below the average year | 13,4 % unter dem Durchschnitt der Vorjahre | 13,4 % sous la moyenne des années passées | Un 13,4 % por debajo de la media de otros años | Il 13,4 % sotto la media degli altri anni | 13,4 % abaixo da média de outros anos | 13,4% onder het gemiddelde van andere jaren | На 13,4 % ниже среднего за прошлые годы | 平年より13.4%安い |
| Q13 | 折扣卖6种泡菜食材 | 折扣賣6種泡菜食材 | 6 kinds of kimjang ingredients on sale | 6 Sorten Kimjang-Zutaten im Angebot | 6 sortes d'ingrédients de kimjang en promotion | 6 tipos de ingredientes de kimjang en oferta | 6 tipi di ingredienti per il kimjang in offerta | 6 tipos de ingredientes de kimjang em oferta | 6 soorten kimjangingrediënten in de aanbieding | 6 видов продуктов для кимчжана со скидкой | 割引で売るキムジャン材料は6種類 |
| Q22 | 辣椒粉降了1.8% | 辣椒粉降了1.8% | Chili powder fell 1.8% | Chilipulver wurde 1,8 % billiger | La poudre de piment a baissé de 1,8 % | El chile en polvo bajó un 1,8 % | Il peperoncino in polvere è sceso dell'1,8 % | A pimenta em pó baixou 1,8 % | Chilipoeder werd 1,8% goedkoper | Перец чили подешевел на 1,8 % | 唐辛子粉は1.8%下がった |
| Q47 | 三星累计第9次夺冠 | 三星累計第9次奪冠 | Samsung's 9th title overall | Samsungs neunter Titel insgesamt | Neuvième titre de Samsung au total | Noveno título de Samsung en total | Nono titolo in totale per Samsung | Nono título do Samsung no total | Negende titel in totaal voor Samsung | Девятый титул «Самсунга» в истории | サムスン通算9回目の優勝 |
| Q74 | 准考证丢失当天早上8点前申报可补领 | 准考證遺失當天早上8點前申報可補領 | Lost ticket: report by 8 a.m. on the day | Verlorener Ausweis: bis 8 Uhr am Tag melden | Carte perdue : à signaler avant 8 h le jour même | Si pierdes la tarjeta, avisa antes de las 8 | Tessera smarrita: da segnalare entro le 8 | Cartão perdido: avisar até as 8 h no dia | Kaart kwijt: meld het vóór 8 uur op de dag zelf | Потерянный пропуск: сообщить до 8 утра в день экзамена | 受験票をなくしたら当日の朝8時までに届け出る |
| Q102 | 泡菜日2020年2月法定 | 泡菜日2020年2月法定 | Kimchi Day was fixed by law in Feb 2020 | Der Kimchi-Tag wurde im Feb. 2020 gesetzlich festgelegt | Le Jour du kimchi fixé par la loi en fév. 2020 | El Día del Kimchi se fijó por ley en feb. de 2020 | Il Giorno del Kimchi fissato per legge nel feb. 2020 | O Dia do Kimchi foi fixado por lei em fev. de 2020 | Kimchidag werd in feb. 2020 bij wet vastgelegd | День кимчхи закреплён законом в феврале 2020 года | キムチの日は2020年2月に法律で定められた |

## F2–F5 与附带小修

- F2（11 版）：P1 导语第 2 段末句 `이번 주의 조치가 아니에요` → `이번 주의 다른 날의 조치가 아니에요`（与 P5 完整表述一致；11 版 content12.py 第 40 行同一韩文句）。
- F3（仅 core-ko）：content8.py P8 B 区 Q125 注释 `杜鹃山林业厅预报峰值11月11日` → `头轮山林业厅预报峰值11月11日`（题面 두륜산；其余 10 版均正确，全家仅此一处 "杜鹃山"）。
- F4（7 版 en/fr/es/it/pt/nl/ru）：P7 金句第 6 条译文改回过去时（de/ja/zh-cn/zh-tw 已正确，不动）：
  - en "Report results with the scores." → "It reported the results with the scores."
  - fr "Annoncez les résultats avec les scores." → "Il a rapporté les résultats avec les scores."
  - es "Da los resultados con los marcadores." → "Informó los resultados con los marcadores."
  - it "Riporta i risultati con i punteggi." → "Ha riportato i risultati con i punteggi."
  - pt "Dá os resultados com os marcadores." → "Reportou os resultados com os marcadores."
  - nl "Vermeld uitslagen met de scores." → "De krant vermeldde de uitslagen met de scores."
  - ru "Сообщайте результаты вместе со счётом." → "Газета сообщила результаты вместе со счётом."
- F5（仅 ko-es）：P1 顶行 `매주 한국어로　Un número cada semana　Aprende coreano con las noticias más recientes` → `매주 한국어로　Un número cada semana　한국 사람이 읽는 한국어를 읽어요`。
- 附带小修（仅 core-ko）：bslib4.py `foot()` 左文 `Lucerna　韩语周报 VOL.4　LUCERNA KOREAN WEEKLY` → `Lucerna　韩语周报 VOL.4　LUCERNA KOREAN WEEKLY　正文韩语　讲解简体中文`（仿 zh-tw 页脚 `正文韓語　講解繁體中文` 的全角空格格式；foot() 用于 8 版，与 fan-out 一致）。

## 改源记录

（编辑脚本 `apply_fix.py`，按（题干，字号）唯一定位：Q12/Q13 用 size=19 区别于 P1 闪电问答 size=21 的同题干；Q47 用 size=20；Q102 用 size=20.5；Q22 取 content12.py 中 "배추 20포기는 ___원이에요." 的第 2 次出现；Q37（P3 B）与 Q74（P5 B）同题干但在不同文件，只改 content56.py。）

## 自查发现：Q74 答案键漏改（已修复，fan-out 重建前）

- core-ko 首版重建后，按 SVG run 核对 P8 键时发现：Q74 题干已换新，但答案键仍为旧值 `74. 김치의 날`——`apply_fix.py` 只换了题干与注释，漏换 `content56.py` 中 Q74 的 key 参数（旧 key `김치의 날`，新题答案应为 `8`）。同类检查：Q22 已同步改 key 为 `1.8`（SVG 核实 `22. 1.8 —` ✓）；Q12/Q13/Q47/Q102 为单选、答案字母 A 不变 ✓；F3 只改注释、key B 不变 ✓。
- 修复：`fix_q74_key.py`，11 版 `content56.py` 的 Q74 key 一律改为 `"8"`（定位：含 `수험표를 잃어버리면 당일 아침` 且含 `___` 的行；正文段落同句不碰）。text.md 不含 key，无需重导出。
- 教训：换题必须同时核对 key 参数；P8 键核对不能只看 `p8.py extract/compare` 的题号集合，须逐行核对印出的 key——已写 `check_p8keys.py`（按栏 + y 拼行）用于每版重建后核对 6 道新题 + Q125。
- core-ko 首版重建结果作废（P8 键含错），已重跑。

## 重渲染与门禁复核（逐版）

- 渲染命令（D5-REPORT 同款）：`rebuild-fix.sh` = 先以修后源码 + `svglib.pre-d5` 重建 base-venv 对照（D5 的 scratch base/ 已清，故每版现建），再 `run_edition.sh <dir> <reader> <mode> rebuild-gates`（venv `run.py` → `render.py` → `tools/webpdf.py` + 全套门禁）。freeze baseline 用系统 python3（D5 协调员已批的一次性例外）。
- 注意：VM 当前多 worker 并行拥堵，单版重建约 15–22 分钟；内存可用仅 ~1G，故 10 个 fan-out 严格串行，不并行。
- freeze baseline 每版均为 7/8（P1 已知解释器 artefact：大字 "1" 185 vs 183pt，文本多重集差 0，D5 已裁定非缺陷），freeze diff 均为 +0/−0、新增 CJK 0。

### core-ko（ko-zh-cn）— DONE（第 2 版重建；第 1 版因 Q74 键错作废）
- 改前 → 改后：印 PDF 45,167,884 B `fa67a1af9d6d…` → **45,181,315 B `7248314a5ae2…`**；网 PDF 4,210,506 B `5b596e5fe459…` → **4,226,882 B `ac97b284fe16…`**；text.md 34,606 B `da1d3a323f7c…`（452 items）→ **35,159 B `ad28cb68c0bf…`（458 items）**（见下“标题行核对”一节：初版重导出时 title 参数误带 `#`，已修正，-2 字节）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check 0 findings；occlusion 0 flags；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0；spill 0；boxtitle 0 DEFECT（63 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS（18,225=18,225）。
- 印 PDF 实测：6 新题题干全在（P2/P4/P5/P7）；P8 键逐行核对（`check_p8keys.py`，150 号齐全）：12. A — 比平年低13.4% / 13. A — 折扣卖6种泡菜食材 / 22. 1.8 — 辣椒粉降了1.8% / 47. A — 三星累计第9次夺冠 / 74. 8 — 准考证丢失当天早上8点前申报可补领 / 102. A — 泡菜日2020年2月法定 / 125. B — 头轮山林业厅预报峰值11月11日；F2 句已改（P1 印为"이번 주의 다른 날의 조치가 아니에요"，旧句全家 0 残留）；页脚 8 版均有"正文韩语　讲解简体中文"。

### 2026-w47-ko-de — DONE
- 改前 → 改后：印 PDF 43,753,274 B `01c8a283684b…` → **43,754,319 B `8d217beb86ae…`**；网 PDF 3,953,949 B `b0ee1af9d6ed…` → **3,956,937 B `4b1a54ce3040…`**；text.md 35,162 B `a192156f3c49…` → **35,715 B `69294b88b3b7…`**（标题 `#` 修正，-2 字节，见下）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 590（D5 同款 run-splitting 预期值）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全；12. A — 13,4 % unter dem Durchschnitt der Vorjahre / 13. A — 6 Sorten Kimjang-Zutaten im Angebot / 22. 1.8 — Chilipulver wurde 1,8 % billiger / 47. A — Samsungs neunter Titel insgesamt / 74. 8 — Verlorener Ausweis: bis 8 Uhr am Tag melden / 102. A — Der Kimchi-Tag wurde im Feb. 2020 gesetzlich festgelegt；印 PDF 6 新题全在，旧 F2 句 0 残留。

## text.md 标题行核对（父协调员补充指令，ru 家陷阱）

- 背景：ru 家发现重导出会丢标题行（其导出器 `ru_textmd.py do_p_text` 只收 sans 粗体 ≥24pt 的标题，D5 后缩到 22/23pt 的框题会被丢）。ko 家导出器 `textmd.py`（11 版副本 md5 均为 `bc6394a3`，与 KIT 所记一致）**没有字号过滤**：`p.text` 只按 y≥200 收、`f.head` 无条件收。尽管如此，仍按指令做了干跑 + 与修前文件 diff。
- 事故：首次重导出时 title 参数误把文件第一行原文（含 `# `）照搬传入，而 `textmd.py main()` 会再加 `# `，导致 11 版第一行变成 `# # Lucerna ...`（每版 +2 字节）。发现经过：重建修前文件时逐版 SHA12+字节数对不上（系统性 +2），查第一行确认。已修正：11 版全部用不带 `#` 的 title 重导出，items 数不变（458/455/456）。
- 修前文件重建（`recon_prefix.py`，/tmp 干跑）：因重导出时已覆盖盘上修前文件，改从源码还原——把当前 `content*.py` 拷到 /tmp，精确反向还原本次全部有意改动（6 题干+注释、F2 句、F3 注释、F4 译文；key/页脚/顶行标语不进 text.md，不影响），用未改动的导出器重跑，与修前 SHA12+字节数（`prefix-fingerprints.txt`，与 PROOF-NOTE 一致）逐版比对：**11 版全部 MATCH**（SHA12 前 12 位 + 字节数）。随后 `diff` 重建修前文件 vs 盘上修后文件（`diff-recon-<版>.txt`）：**只含意改行**——F2 句 1 行、6 道新题干各 1 行、F4 版 1 行译文；无任何标题行增删。结论：ko 家本次重导出**没有丢标题**，且盘上文件与修前文件的 diff 只含意改行。
- 另：`notes_old.json` / `notes_new.json` 为重建用的新旧注释对照表；`check_textmd2.py` 复核 11 版 text.md 150/150 题全在（每页 10/18/18/18/18/18/12/38）。

### 2026-w47-ko-en — DONE
- 改前 → 改后：印 PDF 43,747,373 B `eb62691270b7…` → **43,748,448 B `f10c5065bb5b…`**；网 PDF 3,948,079 B `4c9091c06423…` → **3,951,102 B `59bb38b0bc77…`**；text.md 34,922 B `9339a9931859…` → **35,484 B `b94dadb654db…`**（455 items；标题 `#` 修正后值）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 592（D5 同款预期值）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全；12. A — 13.4% below the average year / 13. A — 6 kinds of kimjang ingredients on sale / 22. 1.8 — Chili powder fell 1.8% / 47. A — Samsung's 9th title overall / 74. 8 — Lost ticket: report by 8 a.m. on the day / 102. A — Kimchi Day was fixed by law in Feb 2020；F4 金句第 6 条已改过去时 "It reported the results with the scores."；印 PDF 6 新题全在，旧 F2 句 0 残留。

### 2026-w47-ko-es — DONE
- 改前 → 改后：印 PDF 43,751,757 B `8672ef924611…` → **43,752,798 B `709b794a694f…`**；网 PDF 3,952,529 B `105856e3608c…` → **3,955,564 B `cb2f55019eee…`**；text.md 35,207 B `8c5396b8d0a3…` → **35,766 B `8ad63cfbb479…`**（455 items；标题 `#` 修正后值）。
- 备注：首次重建在门禁做到 p8 compare 后被运行时重启 SIGTERM 杀掉（22 分钟处）；rebuild-fix.sh 幂等，重跑 8 分钟完成，RC=0。base-venv 对照跑中有一条 `FLOW OVERFLOW [P2-feature] col 2 y=1179`（对照跑，D5 同款警告，非修后成品问题；成品 render RC=0）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 597（D5 同款预期值）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全；12. A — Un 13,4 % por debajo de la media de otros años / 13. A — 6 tipos de ingredientes de kimjang en oferta / 22. 1.8 — El chile en polvo bajó un 1,8 % / 47. A — Noveno título de Samsung en total / 74. 8 — Si pierdes la tarjeta, avisa antes de las 8 / 102. A — El Día del Kimchi se fijó por ley en feb. de 2020；F4 P7 金句第 6 条已改过去时 "Informó los resultados con los marcadores."（印 PDF P7 实测在）；F5 P1 顶行已改为 "매주 한국어로 Un número cada semana 한국 사람이 읽는 한국어를 읽어요"（印 PDF P1 实测在，旧标语 0 残留）；印 PDF 6 新题全在，旧 F2 句 0 残留。

### 2026-w47-ko-fr — DONE
- 改前 → 改后：印 PDF 43,750,452 B `dedad96d3ee2…` → **43,751,522 B `1f6add20c07d…`**；网 PDF 3,951,154 B `eea62fb6f68e…` → **3,954,158 B `dc933cc18cfe…`**；text.md 35,275 B `4e5487a69ec8…` → **35,834 B `20f1aac8f591…`**（455 items；标题 `#` 修正后值）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 591（D5 同款预期值）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全；12. A — 13,4 % sous la moyenne des années passées / 13. A — 6 sortes d'ingrédients de kimjang en promotion / 22. 1.8 — La poudre de piment a baissé de 1,8 % / 47. A — Neuvième titre de Samsung au total / 74. 8 — Carte perdue : à signaler avant 8 h le jour même / 102. A — Le Jour du kimchi fixé par la loi en fév. 2020；F4 P7 金句第 6 条已改过去时 "Il a rapporté les résultats avec les scores."（印 PDF P7 实测在）；印 PDF 6 新题全在，旧 F2 句 0 残留。

### 2026-w47-ko-it — DONE
- 改前 → 改后：印 PDF 43,745,554 B `3a83150347fb…` → **43,746,645 B `edfda4420e46…`**；网 PDF 3,945,989 B `58e4b864e4f1…` → **3,949,052 B `f0efba8a29ab…`**；text.md 35,213 B `247ed6bd653c…` → **35,771 B `402952fdf7ea…`**（455 items；标题 `#` 修正后值）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 602（D5 同款预期值）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全；12. A — Il 13,4 % sotto la media degli altri anni / 13. A — 6 tipi di ingredienti per il kimjang in offerta / 22. 1.8 — Il peperoncino in polvere è sceso dell'1,8 % / 47. A — Nono titolo in totale per Samsung / 74. 8 — Tessera smarrita: da segnalare entro le 8 / 102. A — Il Giorno del Kimchi fissato per legge nel feb. 2020；F4 P7 金句第 6 条已改过去时 "Ha riportato i risultati con i punteggi."（印 PDF P7 实测在）；印 PDF 6 新题全在，旧 F2 句 0 残留。

### 2026-w47-ko-ja — DONE
- 改前 → 改后：印 PDF 50,274,489 B `387b3922ce85…` → **50,279,548 B `f8c7508f9be8…`**；网 PDF 4,361,673 B `eddc96d9fe6d…` → **4,373,107 B `f9bb1d3a3929…`**；text.md 35,425 B `635ec8afac75…` → **35,978 B `1088c4613b36…`**（456 items；标题 `#` 修正后值）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 448；spill 0；boxtitle 0 DEFECT（63 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全；12. A — 平年より13.4%安い / 13. A — 割引で売るキムジャン材料は6種類 / 22. 1.8 — 唐辛子粉は1.8%下がった / 47. A — サムスン通算9回目の優勝 / 74. 8 — 受験票をなくしたら当日の朝8時までに届け出る / 102. A — キムチの日は2020年2月に法律で定められた；ja 不在 F4 之列；印 PDF 6 新题全在，旧 F2 句 0 残留。

### 2026-w47-ko-nl — DONE
- 改前 → 改后：印 PDF 43,747,058 B `770e3c23dce4…` → **43,748,187 B `662eb3e3e3f2…`**；网 PDF 3,947,564 B `f0b06c75ca26…` → **3,950,671 B `5f84566e41de…`**；text.md 35,040 B `a51d9fa51f86…` → **35,607 B `2d0c073ca4d6…`**（455 items；标题 `#` 修正后值）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 592（D5 同款预期值）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全；12. A — 13,4% onder het gemiddelde van andere jaren / 13. A — 6 soorten kimjangingrediënten in de aanbieding / 22. 1.8 — Chilipoeder werd 1,8% goedkoper / 47. A — Negende titel in totaal voor Samsung / 74. 8 — Kaart kwijt: meld het vóór 8 uur op de dag zelf / 102. A — Kimchidag werd in feb. 2020 bij wet vastgelegd；F4 P7 金句第 6 条已改过去时 "De krant vermeldde de uitslagen met de scores."（印 PDF P7 实测在）；印 PDF 6 新题全在，旧 F2 句 0 残留。

### 2026-w47-ko-pt — DONE
- 改前 → 改后：印 PDF 43,752,879 B `41217c9397cc…` → **43,753,908 B `70047cd27b8d…`**；网 PDF 3,953,672 B `1a973dc82d43…` → **3,956,638 B `e4028beb886a…`**；text.md 35,080 B `80cc61ef7bc9…` → **35,638 B `a4f8c30b68b0…`**（455 items；标题 `#` 修正后值）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 590（D5 同款预期值）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全；12. A — 13,4 % abaixo da média de outros anos / 13. A — 6 tipos de ingredientes de kimjang em oferta / 22. 1.8 — A pimenta em pó baixou 1,8 % / 47. A — Nono título do Samsung no total / 74. 8 — Cartão perdido: avisar até as 8 h no dia / 102. A — O Dia do Kimchi foi fixado por lei em fev. de 2020；F4 P7 金句第 6 条已改过去时 "Reportou os resultados com os marcadores."（印 PDF P7 实测在）；印 PDF 6 新题全在，旧 F2 句 0 残留。

### 2026-w47-ko-ru — DONE
- 改前 → 改后：印 PDF 43,925,173 B `8bbaf7979737…` → **43,926,409 B `96e6ab1a6113…`**；网 PDF 4,123,689 B `cfec8232a249…` → **4,126,953 B `766901b91622…`**；text.md 37,174 B `432c54dc7f21…` → **37,738 B `52710f5f9f4e…`**（456 items；标题 `#` 修正后值）。
- 门禁：TOTAL 150，0 警告；census PASS（noto_sans_elements=1107，西里尔文预期值，D5 同款）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 459；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全，键（A/1.8/8）全部正确；12. A — На 13,4 % ниже среднего за прошлые годы / 13. A — 6 видов продуктов для кимчжана со скидкой / 22. 1.8 — Перец чили подешевел на 1,8 % / 47. A — Девятый титул «Самсунга» в истории / 74. 8 — Потерянный пропуск: сообщить до 8 утра в день / 102. A — День кимчхи закреплён законом в феврале 2020 года。注：check_p8keys.py 输出的俄语注释显示无空格拼接（"На13,4 % нижесреднегозапрошлыегоды"）为检查器 SVG run 拼接假象——印 PDF P8 文字层实测空格正常（pdftotext：`12. A — На 13,4 % ниже среднего за прошлые годы`），非缺陷。F4 P7 金句第 6 条已改过去时 "Газета сообщила результаты вместе со счётом."（印 PDF P7 实测在）；印 PDF 6 新题全在，旧 F2 句 0 残留。

### 2026-w47-ko-zh-tw — DONE
- 改前 → 改后：印 PDF 45,215,288 B `17c39f4f4887…` → **45,219,886 B `65118aabee9f…`**；网 PDF 4,314,413 B `fe0220266520…` → **4,323,857 B `189fde45fc9e…`**；text.md 34,637 B `af183ae64f66…` → **35,190 B `ff0a0af289d3…`**（456 items；标题 `#` 修正后值）。
- 门禁：TOTAL 150，0 警告；census PASS（0/0/0）；quotes 0；head_check []；occlusion 0；p8 extract 150/150，compare CLEAN；freeze baseline 7/8（P1 artefact）；freeze diff +0/−0，新增 CJK 0，新增 Latin 451；spill 0；boxtitle 0 DEFECT（63 titles）；edge 0/0；creambox PASS 0 defects；textlayer PASS。
- P8 键：150 号齐全；12. A — 比平年低13.4% / 13. A — 折扣賣6種泡菜食材 / 22. 1.8 — 辣椒粉降了1.8% / 47. A — 三星累計第9次奪冠 / 74. 8 — 准考證遺失當天早上8點前申報可補領 / 102. A — 泡菜日2020年2月法定；zh-tw 不在 F4 之列；印 PDF 6 新题全在，旧 F2 句 0 残留。

## WEEKLY-KIT.md 更新（2026-11-12）

- 11 版 KIT 全部更新：印/网/text 三行改为本次实测盘上值（印 SHA、网 SHA、text SHA 均为完整 64 位；D5 旧值保留在括号内作对照），并在各版 Fixes log 表追加一行 fix rebuild 2026-11-12 记录（core #19、de #7、en #4、es #5、fr #5、it #4、ja #4、nl #3、pt #3、ru #3、zh-tw #1）。核对：11 版 KIT 各含 3 处 "fix rebuild 2026-11-12"，其余家庭 KIT 0 处——只动了 ko 家。
- 印/网 PDF pdftotext 字节数：11 版印与网均字节相同（core 49,738；de 52,066；en 50,704；es 52,068；fr 52,326；it 51,959；ja 53,268；nl 51,672；pt 51,820；ru 59,174；zh-tw 49,681），已写入各版 KIT 网 PDF 行。
- 更正：本日志 es/fr/it/ja/nl/pt/ru/zh-tw 八版条目里原先抄录的"改前"印/网字节数有误（与 `prefix-fingerprints.txt` 及各版 KIT 的 D5 值不符，SHA12 正确、仅字节数抄错），已按 `prefix-fingerprints.txt`（修前实测，与 PROOF-NOTE 一致）逐一订正。core/de/en 三版"改前"值原本即正确，未动。教训：改前值只认 `prefix-fingerprints.txt`，不凭记忆抄。
- 磁盘：收尾时已用 94G / 可用 56G（门限 100G，未触发）。

## 收尾

- 5 条全修，11 版全部重渲染 + 门禁复核通过（见各版 DONE 条目）。未 commit、未 push、未跑 lint、未碰其他家庭/其他周。
- 工作文件：`hidden_files/w47/scratch-fix-ko/`（FIX-LOG.md、apply_fix.py、fix_q74_key.py、check_p8keys.py、check_textmd.py、check_textmd2.py、rebuild-fix.sh、verify_edition.sh、recon_prefix.py、notes_new.json、notes_old.json、diff-recon-<版>.txt、prefix-fingerprints.txt、kit-values.json、d5-baseline-backup/、rebuild-<版>.log、verify-<版>.txt）。
