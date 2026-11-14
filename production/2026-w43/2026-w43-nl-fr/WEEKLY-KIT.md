# WEEKLY-KIT — De Lucerna VOL.1 · NL × FR（荷兰语正文 × 法语讲解）

Lucerna Weekly W43（2026-10-19 – 10-25）扇出刊：目标语 = 荷兰语（核心版逐字冻结），讲解层 = 法语（为法语母语读者原生撰写）。构建目录：`hidden_files/weekly-report-nl-fr-build/`（`bslib*.py`/`svglib.py`/`mediaimg.py` 与核心构建逐字节相同；仅 `bslib4.py`、`content12/34/56/7/8.py`、`render.py` 有讲解层改动）。产物目录：`files/weekly-report-nl-fr/`。

## 一、身份与配对标示（如印出）

- 刊头：De Lucerna（荷兰语无冠词刊名，与核心版同）。
- P1 配对徽标（砖红 #a4553a，20pt 粗体 sans，y=568，顶栏之下、头条带之上，与 NL×DE 同位）：
  `TEXTES EN NÉERLANDAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`
- 页脚左（8 版全同）：`De Lucerna · HEBDOMADAIRE NÉERLANDAIS VOL.1 · TEXTE EN NÉERLANDAIS · EXPLICATIONS EN FRANÇAIS`
- 页脚右：`Page N sur 8`
- P1 刊期行（36pt serif 粗体，居中）：`JOURNAL NÉERLANDAIS · VOL.1 · DE KLOK GAAT TERUG · HERFSTVAKANTIE · ADE WORDT 30`（见 §五实测说明；荷兰语主题词 HERFSTVAKANTIE 等核心内容一字未删）。
- P1 顶栏中段（21pt）：`ELKE WEEK IN HET NEDERLANDS · CHAQUE SEMAINE EN NÉERLANDAIS`（见 §五）。
- 头条带右注：`DIMANCHE : L'HORLOGE RECULE` / `L'HEURE D'HIVER COMMENCE · PAGE 2`。

## 二、基线证明（先证同源，再改讲解）

未改动的构建副本先行复现核心版 8 张已出货 SVG，逐字节一致（md5）：
p1 db377cb78f11c77b0d2c0d51e346caec · p2 97d6162cc33bc2b9130bf5243dcbce6e · p3 e9f8e382310a83892f12ebfd2d45fff5 · p4 88ee5c1ff81a0cd168d01d712e72069f · p5 cd8777cc9dee0ce5ed33714a649f46bc · p6 acd42490af13442724af3667883a123c · p7 351912e2a836576fa2ac18a4b88a4700 · p8 30bfd7e5c73e2b54b63ea1f61043d194。
基线所用核心已含两处程序级补丁：P8 答案 13.5pt/lh 1.16/gap 0.5（流底 2552）与 P1 全宽横线 y=1844→1853。

## 三、计数（与核心注册表逐项相同）

- 总题数 **150**；分级 A2 42 · B1 76 · B2 32；分页 10/18/18/18/18/18/12/38；范文 87 词。
- 题型字符串：content12/34/56/7 沿核心中文注册元数据（不印出，与 NL×DE 构建同）；content8 题型本地化为法语（Cloze 13 · Choix 12 · Phrase 4 · Traduction 4 · Appariement 1 · Rédaction 1），仅注册元数据，不影响键与计数。
- 指令词：Compléter（填空）· Associer（配对）· Vrai ou faux（判断）· Former la phrase（造句）· Traduire（翻译）· Écrire（写作）。

## 四、键差异登记（注册表级 diff，仅此 3 项，均为文档化例外）

构建后以注册表转储对核心逐项比对（编号/页/级/键）：差异恰为 3 项 —

| 题号 | 核心键（中文） | 本刊键（法语） | 原因 |
|---|---|---|---|
| 137（P8 Traduire，A2） | 周日时钟拨回：多睡一小时！ | Dimanche, l'horloge recule : une heure de sommeil en plus ! | 译向读者母语（荷→法），题面荷兰语原句不变 |
| 138（P8 Traduire，B1） | 你的手机和电脑会自动更改时间。 | Ton téléphone et ton ordinateur changent l'heure tout seuls. | 同上（zelf = tout seuls） |
| 150（P8 Rédaction，B1） | （开放题，范文如下） | (Question ouverte — texte modèle ci-dessous) | 开放题装置行法语化；注 = Texte modèle dans la section H de cette page (87 mots) |

- #139 / #140 为反向翻译（法→荷）：题面改法语（`La Dutch Design Week est à Eindhoven. → ___` / `Dimanche, j'ai dormi une heure de plus. → ___`），**键保持荷兰语原文逐字节不变**（注册表 diff 中不出现）。
- 其余 147 键与核心逐字节相同（MC 字母、填空词、造句句、配对字母序全同）；P8 答案注全部法语原生撰写。

## 五、家具与版式决定（全部以生产字体实测为准）

- **P1 刊期行**：40pt 下 HEBDOMADAIRE 版 2086.3px、JOURNAL 版 1927.8px，均超 1820 通道；按 FR 栏先例改用 JOURNAL 变体并降至 36pt = 1734.9px ✓（HEBDOMADAIRE @36 仍 1877.5px 超限）。荷兰语主题段一字未删（与 NL×DE 当初误删 HERFSTVAKANTIE 的教训相反，本刊自始保留）。
- **P1 顶栏中段**：三段式 936.4px 会侵入右段周线（起于 x=1411.5），改两段式 704.1px（居中 623–1327，与右段留 84px），同 NL×DE 裁定。
- **徽标** 1058.8px ≤ 1820 ✓。
- **栏目带左题**：LEVEN · VIE / CULTUUR · CULTURE / SPORT · SPORT / JONGEREN · JEUNESSE / VERDIEPING · APPROFONDISSEMENT / TAAL · LANGUE / TOETS EN ANTWOORDEN · TEST ET RÉPONSES。
- **栏目带右副题**：荷兰语段冻结，尾段法语（如 `NIVEAU A2 · De wintertijd, stap voor stap · L'heure d'hiver, pas à pas`）。
- **版头**：HET NIEUWS · À LA UNE · DE WEEK IN CIJFERS · CHIFFRES（`· EN CHIFFRES` 版 410.4px 超 398 盒宽，去 EN，同 PT×FR 先例）· NU JIJ · À TOI DE JOUER · IN DEZE EDITIE · SOMMAIRE · IN HET KORT · EN BREF · BLIKSEMQUIZ · QUIZ ÉCLAIR · OEFENINGEN · EXERCICES（右注 `Réponses page 8 · exercices mélangés par niveau, cherchez par numéro`）· DE CIJFERS · LES CHIFFRES · AFSCHAFFEN OF NIET? · SUPPRIMER（385.9px ≤ 390）· PAS OP! · PIÈGES FRÉQUENTS（348.2px；`ERREURS FRÉQUENTES` 版 387.6px 余量仅 2.4px，不取）· HET WOORD · MOT DE LA SEMAINE · ZINNEN VAN DE WEEK · PHRASES DE LA SEMAINE (MOT POUR MOT, DE CETTE ÉDITION)（1149.0px ✓）· VOLGENDE WEEK · LA SEMAINE PROCHAINE (VOL.2)。
- **趋势注脚**（P1）：核心中文一行改法语两行（byy+102 / +128，同 NL×DE）：`Google Trends, mardi 20 octobre :` / `instantané ; les chiffres sont des estimations`（388.8px ≤ 412）。
- **趋势小标**：`Ce que les Pays-Bas cherchent sur Google`（366.3px ≤ 390）。
- **数字框/小贴士框括号注**：法语括号前加空格、半角括号（`…in Eindhoven (le nombre de jours de la Dutch Design Week à Eindhoven)` 等 8 处）。
- **gloss 框前缀**：`Note — `（bslib4 gloss）；讲解行首串以 `Notes — ` 起（P1）。
- **读者信**（P7）：示例信署名本地化 Camille / Parijs（荷兰语信体仅人名与城市替换，同 NL×DE 的 Emma/Berlijn 先例）；法语注 2 行（与核心 wrap 行数一致），P7 三栏收尾 1678.5 与核心逐点相同。
- **禁词**：被禁的中间层术语在本刊纸面、本 KIT 与代码中零出现（grep 实测 0）；继承的同名方法已改名 `expl()`（bslib4 定义 + 全部调用点）。

## 六、在建缺陷与修复（构建内自查发现）

1. **盒题溢出 ×2**（盒界检查脚本发现，模型墨迹 vs 自身盒右界）：
   - P2 `ZO ONTHOUD JE HET · L'ASTUCE MÉMO` 墨迹至 x=1460，盒右界 1423（溢出 37px）→ 缩为 `ZO ONTHOUD JE HET · ASTUCE`（360.9px）。
   - P5 `ZO PLAN JE ADE · CONSEILS FESTIVAL` 墨迹至 x=981，盒右界 961（溢出 20px）→ 缩为 `ZO PLAN JE ADE · CONSEILS`（325.6px）。
   修复后盒界检查 0 标记。仅缩法语家具，荷兰语正文与几何未动。
2. **P8 答案溢出**：核心字参 13.5/1.16/0.5 下法语注使 keys 流溢出底线 2552（3 项冲至 2582）→ 收紧至 13.0/1.12/0.4（同 NL×DE 终值）。修复后流终点 2240，无 FLOW OVERFLOW；实测各栏最低基线 ≤2544，墨底 ≤2548，距页脚线 2580 ≥32px。
3. **P1 词条讲解 2 行几何**：法语讲解 `« Régler l'horloge » : changer l'heure — cette semaine, une heure en arrière.` 在 434 通道折 2 行（核心中文 1 行）。像素实测：第 1 行墨 1830–1850，全宽线 1853（1852–1854）自两行间空隙（1851–1855）穿过，第 2 行墨起 1856 — 线不触任何墨迹，与已出货 NL×DE 的裁定几何相同，特此明示供独立校对复核。
4. **P2/P5 EN JIJ 法语注 3 行**（核心 2 行）：盒高公式自适应，栏收尾 P2 1383.1 / P5 1261.1，均远在版区底线（1540/1560）之上，无碍。
5. P6 图注法语一行（capcn）与 gloss 框均由 box/para 自动计高，栏收尾 1055.5 ≤ 1560 ✓。

## 七、几何遮挡审计（出货门，自检轮）

- 方法：paint-order SVG 解析 + 生产字体（svglib text_w）墨带（基线 −0.88em…+0.30em）；`<line>` 按半线宽膨胀（零高盒盲区修正）；检查 (a) 后画不透明形覆盖 ≥30%、(b) 墨入页脚带（>2580）、(c) 墨出页边、(d) 后画细线穿墨带。脚本：构建目录 `audit_nl_fr.py` + `audit_texttext.py` + 盒界检查。
- **合成阳性对照先行验证**：自造含「盒盖字 / 线穿字 / 页脚带侵入」三类缺陷的测试页，审计恰报 3 标记、干净文本不报 — 工具灵敏度成立。
- 结果：**遮挡审计 0 标记（8/8 页）**；盒界检查 0 标记；text-text 扫描仅 1 项 = 刊头字标（248pt 显示字，模型墨带高估）与刊期行重叠，像素实测两带墨间隙 30px（字标墨 140–265 / 刊期行墨 295–329），非缺陷。
- CJK：8 张终版 SVG 中文字符数 = 0；禁词 = 0。页边溢出 0。
- 8 张卡片全部肉眼复核（1950×2700）：家具、注脚、答案区均无压字、无出界。

## 八、事实与星期核查（荷兰语正文，对 2026 真实日历逐项验）

| 正文主张 | 2026 实际 | 判定 |
|---|---|---|
| wintertijd：zaterdag 24 → zondag 25 oktober，03:00 → 02:00 | 10-24 周六、10-25 周日 | ✓ |
| herfstvakantie Midden/Zuid：zaterdag 17 – zondag 25 oktober（9 天） | 10-17 周六、10-25 周日 | ✓ |
| herfstvakantie Noord：10 – 18 oktober；maandag 19 oktober 开学/数据注 | 10-10 周六、10-18 周日、10-19 周一 | ✓ |
| Dutch Design Week：17 – 25 oktober（9 天）；gratis familiedag zaterdag 24 oktober | 同上 | ✓ |
| ADE：woensdag 21 – zondag 25 oktober，30 年，>3.000 艺人 / >200 场地 | 10-21 周三、10-25 周日 | ✓ |
| 欧战周：PSV dinsdag（10-20）客场 1–0 FC Porto；Feyenoord woensdag Sevilla；Ajax donderdag Atalanta；topper zondag 14:30；Sparta–Ajax 16:45 | 10-20 二 / 10-21 三 / 10-22 四 / 10-25 日 | ✓ |
| Expeditie Robinson：zondag 1 november 20:00 RTL 4，19 名候选人 | 11-01 周日 | ✓ |
| Google Trends 快照 dinsdag 20 oktober；Wristler 研究 10-20 发布、计去年 10 月搜索（301.000 + 246.000 = 547.000；750.000 − 547.000 ≈ 203.000；60.500 ÷ 6.600 ≈ 9 倍） | 10-20 周二；算术全对 | ✓ |
| 票价：€ 32,50 / 学生 € 19,50；#46 题 19,50 + 19,50 + 32,50 = 71,50 | — | ✓ |

**星期类发现：无。**（与 ES 核心 jueves 误植不同，本核心全部星期—日期对自洽；quiz 中的 vrijdag 为干扰项，非主张。）事实层未动：herfstvakantie、Dutch Design Week、Amsterdam Dance Event、wintertijd 拨钟与核心版一致。

## 九、P7 金句核查

8 句荷兰语引文逐字取自本刊对应版面文章（程序核验：每句在本刊被引版面正文与 P7 各出现，即恰 2 次，版目标注正确）；法语译文为本刊新译（如 `«Samen zijn dat 547.000 zoekopdrachten»` → `Ensemble, cela fait 547.000 recherches. (Pagina 6)`）。

## 十、图片与署名

8 版 `<image>` 元素与全部署名行与核心版逐字节相同（程序比对 8/8 一致）：P1 Westertoren（Wim van Rossem / Anefo, Nationaal Archief — CC0）、P2 怀表（photo-nic.co.uk / Wikimedia Commons — CC0）、P3 Kinderdijk 风车（Nationaal Archief — CC0）+ 秋林（Vovogov90 — CC0）、P4 1912 国家队（Spaarnestad Photo — publiek domein）、P5 运河船（W. Punt / Anefo — CC0）、P6 图表（Wristler 数据，报社自制图）。

## 十一、产物（files/weekly-report-nl-fr/）

- `svg/` ×8、`cards/` ×8（1950×2700 PNG）
- 印刷 PDF：`De-Lucerna-VOL1-FR.pdf` — 9,677,412 B，sha256 `910199e6967fe6941cf82c26238c7a2d5fd7cbdd8c890c1ff319b9d4b6e2f8d6`
- 网络 PDF：`De-Lucerna-VOL1-FR-web.pdf` — 3,326,020 B（< 10 MB，JPEG q85 @1400px），sha256 `0ea5a11a520fbed51b5b59267ae3a4ba089e4263792a0480bdf6965df16dd738`

## 十二、校对状态

- 构建者自校：全轮完成（计数/键 diff/星期/金句/图片/几何审计/盒界/8 卡肉眼）。
- **独立校对：PENDING** — 待独立校对员零问题轮后由上级入库（本构建未入 GitHub 仓、未发 Discord）。

## D5 rebuild (13 Nov 2026; this build supersedes all earlier deliverable figures in this KIT)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib 2026-w43-nl-fr/svglib.py --target nl --reader latin --week 2026-w43` (`--check` dry-run first, RC=0). `_D5_READER = "latin"`. Routing unit test `test_d5_routing.py`: FAILURES: 0. D1 fix2 retained.
- Pre-rebuild census (`d5_census.py`, D5 elements in the pre-D5 SVGs): 488.
- Baseline (pre-D5 rebuild, venv, disk-measured): run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; print `De-Lucerna-VOL1-FR.pdf` 10,264,583 B (sha256 `1ab6c7be81fa384a83e9967dd0dbb7a14b6fac551c3cbdd32a18015365edd594` — pre-D5 build, superseded); web `De-Lucerna-VOL1-FR-web.pdf` 988,708 B (sha256 `3b6419e25a4888b547dc615b35aa6a93bfd3e7779b0bfbfda21856e3ecb04fae`). Text layer print vs shipped web PDF multiset diff 0 (Python `len()` chars). The KIT-recorded print/web figures predate the §1.1 style port and the D1 re-render and are superseded by the disk-measured baselines above.
- Defects found by the 17 gates (run 1) and fixed by size only — text unchanged throughout:
  - Feature heads `ETEN BESTELLEN WORDT HELDER` (P2) / `EROPUIT IN DE HERFSTVAKANTIE` (P3) HEAD TOO WIDE at 25 pt (advance 472.2/466.0 px vs column 422.5 px) → head size 25 → 22 (`content12.py` P2 head, `content34.py:20`).
  - P1 box title `DE WEEK IN CIJFERS　CHIFFRES` over +3.2 px (right) → f.box tsize 23 → 22 (`content12.py:49`).
  - P6 p.text `AFSCHAFFEN OF NIET?　SUPPRIMER` over +23.6 px (right) → size 21 → 19 (`content56.py:166`).
  - P7 p.text `HET WOORD　MOT DE LA SEMAINE` over +44.1 px (right) → size 23 → 20 (`content7.py:84`).
- P8: 235 → 235 lines, slack to footer rule 35.9 → 35.9 px (unchanged by §4; `content8.py` untouched).
- Gates (full re-run after fixes, run 2): **ALL-GREEN** — run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; head_check 0; d5 census 0; render RC=0; webpdf RC=0, web < 7 MB; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8 byte-identical; freeze diff vs baseline added CJK 0; spill 0 SPILL; boxtitle 0 DEFECT; edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web multiset 0, text.md BYTE-IDENTICAL; census_quotes 0 defective. Logs: `hidden_files/d5-redo/scratch-2026-w43-nl/gates/2026-w43-nl-fr/` (`GATES-SUMMARY.txt` master). Full record: `production/notes/2026-w43/g-nl/scratch-d5-rebuild-nl/D5-REPORT-2026-w43-nl-fr.md`.
- New deliverables (rebuilt 13 Nov 2026): print `De-Lucerna-VOL1-FR.pdf` 9,677,412 B, sha256 `910199e6967fe6941cf82c26238c7a2d5fd7cbdd8c890c1ff319b9d4b6e2f8d6`; web `De-Lucerna-VOL1-FR-web.pdf` 3,326,020 B, sha256 `0ea5a11a520fbed51b5b59267ae3a4ba089e4263792a0480bdf6965df16dd738` (< 10 MB); text-layer web `2026-w43-nl-fr.web.pdf` 909,402 B, sha256 `271619d29b1ef348c28e43e671df983b757ec8a0503a669ecd5aef97cecb28f7` (< 7 MB); `2026-w43-nl-fr.text.md` 40,826 B, sha256 `adcd00148b58c32a7dd3f691b40c260ee18e8125e87f3e2fd42085a06baf8e3f`, **BYTE-IDENTICAL** to the shipped `issues/2026-w43/2026-w43-nl-fr/2026-w43-nl-fr.text.md` (exported from the build source with the scratch exporter `hidden_files/d5-redo/scratch-2026-w43-nl/export_text_w43nl.py`, W46 generic AST exporter + W43-nl italic-serif fix + `IN DEZE EDITIE` heading fix).
- Status: builder DONE, all gates green. Independent re-proof (SOP §8) is the coordinator's separate step; no commit, no push by the builder.
