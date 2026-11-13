# PROOF-NOTE — W47 es-ja, proof round 2 (independent, re-fanout rebuild)

- **版：** `production/2026-w47/2026-w47-es-ja/`（西班牙语目标语，日语读者）
- **复校员：** proof2（独立轮）
- **日期：** 2026-11-11
- **对象：** core-es fix build 10 定稿后重建版（re-fanout，未提交、未入仓）
- **结论：(a) 零缺陷，可定稿。**

## §0 身份核对（磁盘实测，三件 SHA 与任务一致）

| 文件 | 字节 | SHA-256（磁盘实测） | 与任务 |
|---|---|---|---|
| 印 `La-Lucerna-VOL4-es-ja.pdf` | 17,294,448 | `459d570a294a14a3b170e7bf99ca4db3bc91560603dc21c43d371977e55da12f` | ✓ |
| 网 `La-Lucerna-VOL4-es-ja-web.pdf` | 1,540,831 | `5895fce90fffd07cccf1909f8de1aa481572751e8caa9bc3a0d80be00845f71f` | ✓ |
| `2026-w47-es-ja.text.md` | 46,554（1,820 行） | `7479077861f46c27c4d69ae265d43bab40e14cdc2e09bec48d53772142b3e9ea` | ✓ |

- `git status --porcelain -- production/2026-w47/2026-w47-es-ja/`：仅 `??`（未追踪，未 commit、未 push）✓。
- 全程只读生产文件：开工与收工两次 `sha256sum -c`，8 张 shipped SVG 全部 OK，未改动。`run.py` / keycheck 均在 scratch 内副本（`rerun/`）跑；`freeze.py baseline` 自带完整性校验（shipped SVG 跑前跑后重哈希一致）。
- 探针：`git hash-object -w --stdin` 通过（`5bf82ddb…`）；goals 侧 scratch 真实写文件通过；全程 `TMPDIR=<scratch>/tmp`；解释器一律 `tools/venv/bin/python`。
- `/dev/null`：开工时为普通空文件，收工时已恢复为字符设备（`crw-rw-rw- 1, 3`），未动用垫回。

## §1 核心 es 未变（重建前后复核）

core-es fix build 10 磁盘实测，与 core-es3 独立 re-proof (a) 的记录逐项一致：

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `core-es/La-Lucerna-VOL4.pdf` | 17,212,955 | `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5` |
| `core-es/La-Lucerna-VOL4-web.pdf` | 1,410,471 | `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235` |
| `core-es/2026-w47-es-zh-cn.text.md` | 43,788（1,822 行） | `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb` |

核心已定稿（独立 re-proof (a) 零问题），重建只继承、不重议。

## §2 本轮必查重建项（7 处 bridge + 导出器 #82 + proof1 四项核心缺陷）

### (a) 7 处 bridge 孤儿标点修复——逐项重验，全部通过

7 处均为 fanout 重建时 `classify-ja.txt` 的 REVERT 项（旧版=改过的短句，新版=未改的长句，REVERT 恢复短句）。
每处三重验证：新形在当前 `content*.py` 中就位、旧形全版 0 次、该桥句在 SVG 内渲染为完整单个 `<text>` 行（无独行 `。`）。

| # | 位置 | 新形（已就位） | 旧形（全版 0 次） | 渲染 |
|---|---|---|---|---|
| 1 | P2 C-intro，`content12.py:275` | `記事を読んで正しい答えを選ぼう。` | `2ページの記事を読んで、正しい答えを選ぼう。` | p2 单行 ✓ |
| 2 | P4，`content34.py:168` | `記事を読んで正しい答えを選ぼう。` | `4ページの記事を読んで、正しい答えを選ぼう。` | p4 单行 ✓ |
| 3 | P4，`content34.py:190` | `比較級か -ísimo 形で補おう。` | `かっこ内の言葉の比較級か -ísimo 形で補おう。` | p4 单行 ✓ |
| 4 | P4，`content34.py:200` | `過去形（pretérito indefinido）に直そう。` | `文を過去形（pretérito indefinido）に直そう。` | p4 单行 ✓ |
| 5 | P5，`content56.py:66` | `記事を読んで正しい答えを選ぼう。` | `5ページの記事を読んで、正しい答えを選ぼう。` | p5 单行 ✓ |
| 6 | P5，`content56.py:93` | `ir a + 不定詞で書きかえよう。` | `ir a + 不定詞で文を書きかえよう（近い未来）。` | p5 单行 ✓ |
| 7 | P6，`content56.py:198` | `グラフを見て正しい答えを選ぼう。` | `上の2つのグラフを見て、正しい答えを選ぼう。` | p6 单行 ✓ |

（注：#2 归属 P4 而非 P3——`content34.py:168` 的桥句渲染在 p4-deporte.svg；7 处合计 P2×1 + P4×3 + P5×2 + P6×1，与 builder 的 6 处 widow + P2 C-intro 预修一致。）
独立孤儿扫查：`sweep_de.py` bridge orphans **0/20**、bridge widows **0**、box-vs-hline **0**；
`<text>` 节点直扫：独行 `。` **0**、行首 `。` **0**、独行右引号 `」` **0**。
直扫另有 6 处单节点标点，均逐一裁定为同行多 run 的误报、非独行（见 §5）。

### (b) 导出器 #82 修正——通过

- `282.` 在 text.md、印版文字层、网版文字层中均为 **0** 次；#82 键为 `82. Verdadero — 今年はMiDNIで身分確認して投票できる`，`p8extract.json` 中 `keys['82'] = 'Verdadero'`，keycheck 150/150 中 #82 一致。
- 新导出 1,820 行，键号 1–150 齐全，无 >150 的假键。

### (c) proof1 四项核心缺陷（D1–D4）的落地——全部通过

- **D1**（P1 consejo 截句）：现为 `En la página 6 te enseñamos cómo leer un debate sin perderse.`（content12.py:131 / text.md L176；P1 SVG 内两次出现，目视完整）✓。
- **D3**（`antes del jueves 19` ×5）：`antes del jueves` 在 text.md 与 8 张 SVG 内均为 **0**；`hasta el jueves 19` 在 P1 标题、Q3、Q116、Q139 键、H 范文内一致 ✓。
- **D4**（P7 样信德比星期）：现为 `el sábado veo el derbi`（content7.py:99 / text.md L1363；P7 SVG 内目视确认）✓。
- **D2/C3**（P5 词库缺 correo/envío）：词库仍为 `sobre · papeleta · censo · identidad · plazo · urna`，未动——与 core-es3「已裁定接受原样」一致；6 个答案（correo/papeleta/envío/identidad/censo/plazo）与键无歧义 ✓。

## §3 缺陷清单

**无。缺陷数 0。**

## §4 机械门禁（全部自跑，证据见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| run.py（rerun 副本） | rc=0，0 OVERFLOW / 0 TOO WIDE，TOTAL 150，A2 50 / B1 72 / B2 28，MODELO 97 词，P8-keys y=2521 |
| freeze baseline（重建 8/8） | rc=0，8/8 SVG 逐字节相同；另 direct rerun SVG 8/8 与 shipped 一致 |
| freeze diff | rc=0；新增 CJK 2,946，逐个分类入账，未入账 **0**（见 §6）；Latin-only 增减均为 re-wrap/注 swaps，无新增西语内容 |
| freeze diff --strict-cjk | rc=**1，属预期**（见 §6 说明） |
| occlusion audit | **0 flags**（selftest 六类全过） |
| p8 extract | **150/150** |
| p8 compare（vs core-es） | **CLEAN**，keydiff=[137, 138]（已裁定，见 §5） |
| 印/网文字层 | `pdftotext -layout` 两版逐字节相同，**109,951 B**，8 页，1462.5×2025 pt |
| keycheck（REG vs 印版提取） | **149/150**，仅 #150 開放題例外（REG 描述性文字 vs 印版 `✓`，与 core 相同约定） |
| creambox（逐盒裁定） | 全部有文盒 baseline clearance **+1.9 ~ +110.8**；P1 两空盒为图版与描边框（无文，符合设计） |
| boxtitle（两种方法） | **25/25 fit，0 溢出**；最紧 P5 `EL PLAN DE LA SEMANA　今週の計画` +4.3 |
| P8 最小字号 | **10.125 pt**（735 spans），<9.75pt 为 0 |
| sweep | bridge orphans 0/20，widows 0，box-vs-hline 0 |
| §1.1 | 纸 #fbfaf6 ×8 页；masthead `La Lucerna` 196 units = 147pt；VOL.4 ×9，VOL.5 ×3（全在 P7）；chips P1 10 / P2 15 / P3 18 / P4 15 / P5 18 / P6 18 / P7 12 / P8 35（A2 11 / B1 21 / B2 3）；弯引号 0、直引号（文本节点内）0；`12 de noviembre` 全版 0；ABSTRACT.txt 日语单行 447 B，无 ASCII 双引号 |
| gloss 词元（SVG 实测，≥2/页） | P1 reflexión 2；P2 mitin 2 / cartel 2 / escaño 2；P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 5；P4 parón 2 / liderato 3；P5 papeleta 2 / censo 3 / plazo 3 |

## §5 逐项裁定（非缺陷）

- **keydiff [137, 138]**：#137/#138 的键是日语句（`月曜日は国際フラメンコの日。` / `土曜日にセビージャ・ダービーを見る。`），core 的对应键是西班牙语句——按读者语重定向的翻译题，键语不同属设计；题干-键一致（#137 译“周一是国际弗拉门戈日”，#138 译“周六看塞维利亚德比”），P8 印版中两键各带 `— 原文と比べよう。` ✓。
- **6 处单节点标点**（直扫误报，均在同一可视行内有邻文，非独行）：
  1. p2 `）`（x=808.6）：同行 `オの住宅討論、` + `PSOE` + `対` + `PP`，为 `(水曜：ラジオの住宅討論、PSOE対PP）` 换行后的闭括号；
  2. p5 `）`（x=804.1）：同行 `Después ___` + `（不定形：` + `enviar` + `el sobre.`，为 Q72 题干的括号闭合；
  3. p8 `：`（x=1094.3）：同行 `85. C — Podemos` + `15` + `分`，为键注 `Podemos：15分` 的行内冒号；
  4. p8 `）`（x=1183.3）：同行 `103. las — a las 21:00` + `（前置詞` + `a`，为 `（前置詞 a)` 闭合；
  5. –6. p8 `— ` ×2（#137/#138 行）：`月曜日は国際フラメンコの日。 — 原文と比べよう。` 的句中分隔符。
- **#44 注换行**（`動詞は2` / `番目`）：渲染器字符级 CJK 断行，proof1 已撤回，KIT §6.14；语义完整，非缺陷。
- **Q42**（`Después del Día del Flamenco, la próxima gran fecha es...` → B 选举）：同文亦提及圣塞西利亚（22 日），但其不在选项内；“gran fecha” 在选举周报纸语境下指大选，选项内 B 唯一正确。可接受，非缺陷。
- **P4 欧冠对阵**（Sabah / Viking / AEK）：core build 10 内容，重建未动；前两轮已独立联网核实、无缺陷，本轮不重开（以 core-es3 (a) 结论为准；版内自洽：J5 24–25 日、J4 比分与 Q52–54 改写、P8 键全一致）。
- **#150 例外**：开放题无唯一答案，印版 `✓` 为既定约定，与 core 一致，非缺陷。

## §6 freeze 新增 CJK 逐个分类（2,946 字，未入账 0）

freeze-diff 的 `cjk_added_total`（332 个不重复字）分类如下；另对全版 289 个不重复汉字做 opencc `s2t`/`t2s` 双向核查。

| 类别 | 字数 | 说明 |
|---|---|---|
| 平假名 | 986 | 日语讲解层 |
| 片假名 | 644 | 同上 |
| 全角标点/符号（。、、・「」＝：？〜…— + 全角（）？：＋） | 215 | 日语标点 |
| 汉字·简繁同形 | 1,084 | 中日共享字形 |
| 汉字·简体形（新字体） | 17 | 下述 16 字中的 17 次出现，**全部为常用汉字** |
| **未入账** | **0** | 简体形且非常用汉字：0 |

### SIMP_ONLY 裁定（逐字核对）

- 全版经 `s2t` 变化的字（即简体形）共 **16 字**：`争会体党写参叙号国届数断来点画静`——逐字对照常用汉字表（Wikipedia `List of jōyō kanji` + writejapanese.com 常用汉字 2,136 字表）**全部在表**（如 写 #841・新字体 写/旧字體 寫・3 年级；号 #651・新字体 号/旧字體 號・3 年级；会 #175、国 #323、争 #104、来 #179、体 #218、党 #699、参 #285、叙 #631、届 #335、数 #1422、断 #919、点 #497、画 #167、静 #1520——writejapanese 表内序号），且各有日语语境（`首位争い` `集会` `自体` `国民党` `写真` `参照` `叙述` `毎週一号` `国際` `届く` `数字` `断定` `来週` `時点` `計画` `静粛日`）。**结论：全部为日语汉字假阳性，无一真简体中文残留。**
- 任务示例中的 `学`：**本版中 0 次**（SVG、text.md、content*.py 全查无），不构成问题。
- 典型简体-only 残留字直查：`读 话 说 语 认 对 发 达 过` 全部 **0 次**。
- 反向 `t2s` 变化的 77 字（繁体形，如 読話語問題時間）：逐字看语境，全部为正常日语词（`問題` `時間` `世界遺産` `言語` `読む` 等），非中文残留。
- **--strict-cjk rc=1 说明（属预期）：** `freeze.py diff --strict-cjk` 要求新增 CJK 为 0，该规则只在 core 与版共享同一读者语时成立；本版读者语为日语、core 为简体中文，日语讲解层合法新增 2,946 字，上表已全部入账、未入账 0。故 rc=1 是工具对读者语不同的正常反应，不是失败；非 strict 的 diff rc=0，且 baseline 重建 8/8。

## §7 150 题逐题手验（三源一致）

机械 backbone：`keycheck-150.json`（REG vs P8-提取 149/150 + #150 例外）；另从 `content*.py` AST 提取全部 138 个 `f.ex()` 题干与 3 组配对题（12 项），逐题核对题干→答案（`stems-150.txt`）。

- **Q1–Q10（P1）**：日期 13/29/19/16/20/15，选项 C/B/A/B——与刊期（竞选 13–27 日共 15 天、投票 29 日、邮寄截止 19 日、弗拉门戈 16 日、J13 20 日）全一致 ✓。
- **Q11–Q24（P2）**：16/19/29/22/noviembre/empieza/dura/vuelve/recorren/llega/B/A/C/B——`recorren` 有正文句 `los partidos recorren España` 为据；Q24 禁发民调 24–28 日 → B ✓。
- **Q25–28 配对**：debate→c（公开讨论）、mitin→b（竞选集会）、cartel→d（街头大字报）、escaño→a（议会席位）——字母按 rights 数组顺序，与 P2 印版 a–d 逐项对上 ✓。
- **Q29–Q46（P3）**：V/F 5 项（16 日/2010 年/非独舞/圣塞西利亚 22 日非 16 日/毕尔巴鄂 22 日 12:00）✓；填空 cante/baile/guitarra/palmas/compás ✓；Q39 奈洛比 B、Q40 duende A（**无 en 系 Q39/Q40 互换**）✓；Q42 见 §5；Q43–46 组句/间接疑问 ✓。
- **Q47–Q64（P4）**：榜首巴萨 33 分 A；J13 20–23 日 B；德比周六 18:30 C；巴萨–比利亚雷亚尔周日 14:00 A；欧冠 J5 24–25 日 B；配对：jornada→c、derbi→b、liderato→a、fase liga→d ✓；比较级 más importante/muchísimos/peor/mejor ✓；过去时 ganó/recibió/perdió/volvió/cerró——J12 巴萨客场 1–2 胜马竞、马竞 0–2 拜仁与正文一致 ✓。
- **Q65–Q82（P5）**：邮寄投票 B/A/C/B/A；填空 correo/papeleta/envío/identidad/censo/plazo——与正文句一一对应 ✓；ir a + 不定式 4 项 ✓（`Va a abrirse la urna` 反身保留）；V/F：Correos 申请 ✓、静默日周六非周日 ✓、MiDNI ✓。
- **Q83–Q100（P6）**：45/195/15/5 天/15 分（45−30）/C/B/A/C/B；tenga/sea/para que/Aunque/sondeo/muestra/indecisos/margen de error——虚拟式与直陈式区分正确 ✓。
- **Q101–Q112（P7）**：Es/Son/las/B；más goles/tan rápido/mejor/B；baje/sea/es/B（ojalá + 虚拟式；creo que + 直陈式）✓。
- **Q113–Q132（P8 A–D）**：复选题与读解全对；Q121–124 与 H 范文一致（Lucía 看德比、Diego 看皇马–塞尔塔、两人读纲领、标题 B《两城一土曜》）✓。
- **Q133–Q150（P8 E–H）**：对话填空 votar/identidad/urna/sobre/cierra ✓；配对：sondeo→c、muestra→d、margen de error→b、junta electoral→a ✓；翻译 #137/#138 日语句 ✓；#139 `hasta el jueves 19` ✓；#140 `Cada promesa tiene que llevar datos.`（tener que = 必须）✓；#150 开放题，范文实测 **97 词**（与 run.py、P8 标注一致）✓。
- **P7 FRASES 8 句**：源码级逐字比对 P1–P6 正文，**8/8 verbatim**（text.md 导出栏流交错致其中 1 句整句检索失效，已在源码级证实无误）✓。
- **P7 语法栏/典型错误/本周单词/读者来信**：语法规则、纠错、LA PALABRA 释义均正确；样信 D4 已修 ✓。

## §8 8 页逐页目视（150 dpi 印版渲染，`png/p-1.png`–`p-8.png`）

- **P1**：刊头、五大看点、CINCO CLAVES 盒、目录、LA PALABRA、BREVES、投票箱插图、consejo 完整句、QUIZ Q7–10——无溢出、无压字、无裁切 ✓。
- **P2**：日历盒、讲解盒、¿SABÍAS QUE…?、¿Y TÚ?、DECIR LA HORA、日期表、练习 A–D；C 桥单行 ✓。
- **P3**：Sargent 舞者图+图注、EL FLAMENCO EN TRES DATOS 盒、¿Y TÚ? 盒在分隔线上方（末行基线 clearance +1.9，墨在盒内）、练习 A–D ✓。
- **P4**：J13 六场赛程表、欧冠盒、¿Y TÚ? 盒、练习 A–D；A/C/D 三桥均单行 ✓。
- **P5**：投票箱照片+图注、EL PLAN 盒、讲解盒、VOTAR 盒、¿Y TÚ? 盒在分隔线上方（+1.9）、练习 A–D；词库未动 ✓；Q72 `Después ___（不定形：enviar）el sobre.` 单行 ✓。
- **P6**：EL CAMINO AL 29N 时间线按 13/16/18/19/23/23/24–28/26/27/28/29 顺序，**RTVE 八人辩论行已在位**；RTVE 图表（45/45/30/30/15，脚注 195 + 3×10）与数字盒（5/15/1）无压字；练习 A–D；D 桥单行 ✓。
- **P7**：三栏语法、时辰书图、ERRORES 4 条各 1 行、LA PALABRA、CARTAS（样信半角括号 + 日语编辑注 4 行在盒内）、FRASES 8 句、VOL.5 预告横幅远离页脚 ✓。
- **P8**：A–H 练习区、RESPUESTAS 150 键、MODELO 范文（97 词）、鹅毛笔图、页脚清晰；键区末端 y=2521，余 39px ✓。

## §9 未决事项（O，观察/备注，均不构成缺陷、不阻塞定稿）

- **O1 — KIT §1 的 SHA 仍为 build 3 旧值**：`WEEKLY-KIT.md` §1 列印版 17,294,297 B / SHA `de40fa29…`、网版 1,503,253 B / SHA `859b4421…`、text.md 1,803 行；重建记录在 §8（与本轮实测一致）。属内部文档滞后，不影响版面；建议入仓时顺手更新 §1。
- **O2 — KIT gloss 计数口径差异**：KIT 记 P5 papeleta 3 / censo 2 / plazo 4；本轮 SVG 实测渲染页为 2 / 3 / 3（KIT 数含 P6 溢出：`papeletas de verdad` 与 `Termina el plazo` 在 P6）。三词在 P5 均 ≥2，门禁通过；仅计数方法备注。
- **O3 — D5 字体（生产级待定项，只记录）**：Newsreader 1109、Noto Sans CJK SC 619、Noto Serif CJK SC 319、UnifrakturMaguntia 1（proof1 为 1096/619/319/1；Newsreader +13 系 core build 10 新增拉丁文——RTVE 时间线行、`acordado no es cerrado` 段等）。CJK run 从 serif 段拆分及 `→` 箭头为渲染器设计，非缺陷。
- **O4 — P3/P5 ¿Y TÚ? 盒最紧 +1.9**：为基线 clearance，末行 `送ろう。` 全为 CJK（无下行字母），真墨即在盒内；与 proof1 一致。

## 附：方法备注（非缺陷）

- `tools/freeze.py` 仅有 `baseline`/`diff` 两个子命令；本轮另以 rerun 副本做 direct run.py + SVG sha256 8/8 复核。
- keycheck 跑 `run.py` 时取 rerun 副本目录（`keycheck_core.py <rerun-copy>`），不触生产目录；keycheck 日志的 build 输出为副本内重建。
- 常用汉字核对源：Wikipedia `List of jōyō kanji`（2,136 字，2010 年修订版）与 writejapanese.com 常用汉字表（按笔画排序）；`写` #841、`号` #651 在 Wikipedia 表内逐条定位，其余 14 字在 writejapanese 表内逐条定位。
- 外部事实：本轮不重复 proof1/core-es3 已独立联网核实过的外部事实（选举、邮政、赛程、辩论、JEC/BOE、UNESCO 等）；重建未改动这些内容（classify-ja.txt 为证），核查重心为重建变更点与版内自洽。

## 产物

`hidden_files/w47/scratch-proof-es-ja2/`：`PROOF-NOTE.md`（本件）、`GATE-LOG.md`、`logs/`（全部门禁日志）、`p8extract.json`、`p8compare.json`、`freeze-diff.json`、`freeze-diff-strict.json`、`keycheck-150.json`、`keys-compact.txt`、`stems-150.txt`、`simp-candidates.json`、`trad-candidates.json`、`print.txt`、`web.txt`、`png/p-1.png`–`p-8.png`、`rerun/`（重建副本）、`freeze-es-ja2/`（baseline 副本）。
