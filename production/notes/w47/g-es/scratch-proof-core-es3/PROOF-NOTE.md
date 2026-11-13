# PROOF-NOTE — W47 core-es build 10 独立复校（re-proof）

- 复校员：独立复校（core-es3）
- 日期：2026-11-11
- 对象：`production/2026-w47/core-es/` build 10 定稿（未 commit、未 push）
- 标准：仓库根 `SOP.md`（proofread-until-zero；几何遮挡扫描必过；p8 compare 必跑；讲解/导读用读者母语；对外内容禁内部标签/周次/语言代码）
- 依据：FIX-LOG（`scratch-fix-core-es1/FIX-LOG.md`，已读，尤其 KIT §6 裁定 15–24 与 build 10 门禁表）+ 磁盘实测 + 独立外部核实。不信 KIT，只信自己跑的结果。

## 结论：(a) 零问题，可定稿

- 缺陷数：**0**。
- 150 题逐题手验：150/150 通过（机械比对 149/150，仅 #150 开放题范文为例外，独立核实该例外合理，见 §5）。
- 全部机械门实跑通过（证据见 `GATE-LOG.md`）。
- 三个 SHA 与任务一致（见 §0）。

## §0 身份核对（磁盘实测）

| 文件 | 任务给定 | 磁盘实测 | 一致 |
|---|---|---|---|
| 印 PDF `La-Lucerna-VOL4.pdf` | SHA `2723a283…138b5`，17,212,955 B | SHA `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`，17,212,955 B | ✓ |
| 网 PDF `La-Lucerna-VOL4-web.pdf` | SHA `c2473211…235`，1,410,471 B | SHA `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`，1,410,471 B | ✓ |
| text.md `2026-w47-es-zh-cn.text.md` | SHA `509c95fa…8ddb`，1,822 行 | SHA `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`，1,822 行，43,788 B | ✓ |

- `git status --porcelain -- production/2026-w47/core-es/`：仅 `?? production/2026-w47/core-es/`（untracked，未 commit、未 push）✓。
- SVG 首 8 哈希（keycheck 重跑 run.py 后复核，未变）：p1 `947d1843` · p2 `4274b9ec` · p3 `f6fabc93` · p4 `897d34cb` · p5 `2fe8d4b0` · p6 `4095ea92` · p7 `a376ef8c` · p8 `19123831`，与 FIX-LOG build 10 一致；与 build 9 相比仅 p1/p2/p6/p8 变。
- 探针：`git hash-object -w --stdin` 通过（`9daeafb9…`）；goals 侧 hidden_files 可写验证通过；全程 TMPDIR 指到本 scratch 内 `tmp/`，未写系统 /tmp。

## §1 本次必查项逐项核实（fix build 10 改动）

### (a) C1：P1 CINCO CLAVES 框加高 — 通过
- 盒 `y=588 bottom=1308.0`（700→720 已落地）。creambox inside-only：末行基线 1300.0，基线 clearance **+8.0**；creambox_diag PIL 真墨：墨底 1302.2，真墨 clearance **+5.8**（≥+5px 标准）✓。
- 200dpi 印版 P1 目视：gloss 行「五大看点，不编数字：全在本期里讲清。」完整在盒内，下有奶油空隙 ✓。
- 框标题逐个实测：boxtitle 35 行、**0 溢出**（与 fix 日志逐字节一致）；最紧 `LA SEMANA EN CIFRAS` clear +16.0；`CINCO` +316.2。纯拉丁标题行亦经 boxtitle 真墨（advance 非唯一口径，工具用 PIL 墨水）覆盖 ✓。

### (b) C2：邮寄投票截止「antes→hasta」— 通过
- 全版 grep：源码（content12/34/56/7/8.py）+ text.md + ABSTRACT.txt 中 `antes del jueves` = **0**；text.md 中 `hasta el jueves` = **7** ✓。
- P2 残留：`content12.py:175` 为 `hasta ese día`（text.md L274 同）✓；`antes de ese día` 全版 0。text.md 其余 `antes` 出现（`antes de pagar/votar`、`un día de silencio antes de votar`）均为无关正常用法 ✓。
- 中文键注：keys 3、9、22、65、123 均为「邮寄投票最迟须在 19 日申请」；`19 日前` 全版 0（含 ABSTRACT.txt）✓；ABSTRACT 改为「邮寄投票最迟 19 日申请」✓；Q139 键句「El voto por correo se pide hasta el jueves 19.」✓。
- 外部核实（独立检索，2026-11-11）：Correos 官方通告 2026-11-10（correos.com/sala-prensa）原文「todavía pueden solicitar **hasta el día 19 de noviembre (inclusive)**」；lavozdeibiza 引 LOREG 第 72 条（申请期 10 月 6 日–11 月 19 日）；`date -d`：2026-11-19 为周四 ✓。截止日确为 11 月 19 日周四（含当日）✓。

### (c) es-ja D1/D4 — 通过
- D1：`content12.py:130` / text.md L174：`En la página 6 te enseñamos cómo leer un debate sin perderse.`（cómo 有补足语，句义完整）✓。
- D4：`content7.py:99` / text.md L1338：Marta 样信为 `el sábado veo el derbi` ✓。外部核实：Sevilla–Betis 周六 21 日 18:30（DAZN/EFE 2026-10-21、eldiariodetoledo、lagrada、Sportradar 12:30 EST=18:30 CET）；周五 20 日 21:00 为 Athletic–Espanyol（同一批来源）✓。P4 赛程表、Q49/Q118/Q124/Q134/Q138 均为周六，一致 ✓；样信金句未破（两句均非金句；金句 8/8 恰 2 次已复核）✓。

### (d) es-nl D1/D2（已裁定，照此核实）— 通过
- D1：Atresmedia 23 日周一正确。独立检索证实：zocalopublico 2026-11-09T17:25「Atresmedia… anunció este lunes que lo anticipa al día 23」；radarprensa（经 20minutos）2026-11-09T15:22「ha trasladado su debate electoral a cuatro al lunes 23」；elfolio 2026-11-09（PP 提议 26 日为 Academia 方案，未定）；diariosabemos（Abascal 已确认 Atresmedia 23 日）。11 月 4–6 日旧来源（26 日）已被 11 月 9 日改期取代 ✓。
- D2：「solo hay un debate cerrado」+ Q89 键 B 正确。独立拉到 doblelectura.es 指南（2026-11-10 数据）原文：「A 10 de noviembre de 2026 solo hay un debate cerrado: el de portavoces de laSexta, el viernes 13 a las 21:30」「Solo el de laSexta tiene hora」；SER 18 日住房辩论两党已确认但无公布时间（本轮检索未见时间），按「cerrado = 时间/主持/阵容全锁定」口径不算 cerrado；Mediaset cara a cara 16 日两党接受亦无公布时间（zocalopublico：「Socialistas y populares ya habían pactado el cara a cara… el próximo lunes 16 en los canales de Mediaset」）✓。p8 compare build9→build10 CLEAN keydiff=[]、build6→build10 仅 [139]，证实 Q89 已恢复原键 B ✓。
- P6 措辞核实：P6 正文第 2 段已把区分写清楚——「El debate de vivienda en la Cadena SER, el miércoles 18, ya está acordado (Rodríguez–Bravo), pero no se había publicado la hora al cierre de esta edición: **acordado no es cerrado**」✓；P1 lead「Fue el único debate cerrado al cierre de esta edición」+「Los dos partidos aceptan la cita, pero no hay hora publicada」✓；时间线 23 日两行（Atresmedia 四人 / RTVE 八人）+ 26 日行「El PP propone un debate a cuatro de la Academia (sin fecha pactada)」✓；ABSTRACT「截至 11 月 10 日只有 13 日晚 laSexta 四人辩论完全锁定」✓。
- P1/P2 的「PSOE 未确认」假陈述已订正为「两党接受日期、但无公布时间」✓（见 P1 lead 与 P2 正文 `los dos partidos aceptan la cita, pero no hay hora publicada`）。

### (e) es-pt C2：P6 RTVE 免费分钟 — 通过（带 O3 备注，非缺陷）
- 数字：PSOE 45 / PP 45 / Vox 30 / Frente Amplio 30 / Podemos 15 + 3×10 = **195**，算术核对 ✓；图表条形与标签目视无压字 ✓；Q84 键 B（195）✓；Q83 A、Q85 C ✓；Q88 注「只刊登选管会公布数据并注明来源」随脚注成立 ✓。
- 脚注归因：「Acuerdo de la Junta Electoral Central del 4 de noviembre: 195 minutos en total, del 13 al 27 de noviembre. Tres formaciones más tienen 10 minutos cada una: Frente Obrero, PCTE y SALF.」✓。
- 外部核实（独立检索）：BOE-A-2026-23258 确为 JEC 2026 年 11 月 4 日决议——「Acordar la distribución… en los términos de la propuesta formulada por la Comisión de Radio y Televisión [LOREG art. 65]」「Dicha distribución está publicada en la página web de la Junta Electoral Central」「recursos… antes de las 14 horas del viernes 6 de noviembre」「alegaciones hasta las 10 horas del martes 10 de noviembre」✓。LOREG 第 64 条档位（10/15/30/45）与 2023 年得票推导（PP 33.06%→45、PSOE 31.68%→45、Vox 12.39%→30、Sumar 12.33%→FA 30、Podemos ~2%→15）自洽；档位对 Sumar 继承争议稳健（Podemos 即使按 2.6% 计仍为 15）✓。
- PCTE 保留：JEC 逐党表公布于 JEC 网站、本轮检索同样未直读到（与 FIX-LOG 一致，记为 O3）。独立旁证：BOE-A-2026-23103（11 月 3 日公布名单）确含 PCTE 本名及 PCTE/ELAK 等地区联合会 denominations（检索片段实证：Alicante PCTE 第 5 名、PCTE/ELAK 第 7 名）；articulo14/Civio 2026-11-08：「PCTE presenta candidaturas bajo diferentes denominaciones territoriales」、SALF 国会 46 选区、Frente Obrero 全 52 选区；LOREG 64.2 阈值 75%（国会 40/52）+ JEC 判例 666/671/2011（任一院达标即可）。以 BOE + LOREG 为准：无任何积极证据表明 JEC 排除 PCTE，195 总数与 P8 #83–85 一致 ✓。未重做 18,684 行全量逐省点数（见 GATE-LOG §方法备注）。

### (f) C3（已裁定接受现状，禁改）— 通过（未动）
- `content56.py:79` 词库仍为 `sobre · papeleta · censo · identidad · plazo · urna`，未动 ✓；P5 B 组练习（Q70–75：correo/papeleta/envío/identidad/censo/plazo）与键一致，6 答案无歧义 ✓。未提议替换 ✓。

### (g) 全文重读 + 150 键手验 + P7 toolbox — 通过
- text.md 1,822 行全文通读（P1–P8），另印 PDF P1/P6/P7/P8 100dpi 目视复核。未发现新事实/语言缺陷（详见 §2 抽查与 §3）。
- 150 题逐题手验：150/150 通过，逐题依据见 `keycheck-150.json`（`hand_check`/`hand_basis` 字段）。机械 REG vs 印刷 149/150，仅 #150 例外（见 §5）。
- P7 toolbox clearance 实测：3 盒 inside-only +42.5 / +26.5 / **+8.8**，desc-clear 最小 +2.8，真墨最小 +6.8（CARTAS 盒末行「延至 VOL.5。欢迎来信！」墨底 1837.7，盒底 1844.5）✓；P7 col3 终点 1844.5，预告框底未压页脚线，P7 目视页脚清晰 ✓。
- 外部事实抽查（除 (b)(c)(d)(e) 外）：欧冠 J4——巴萨 3–0 阿斯顿维拉、皇马 3–2 AEK、马竞 0–2 拜仁（Sportradar + 多源）✓；西甲 J12 后积分巴萨 33 / 皇马 30 / 马竞 28、11 月 8 日巴萨客场 1–2 胜马竞 ✓；日期星期全核（`date -d` Europe/Madrid：9 日周一、10 日周二、13 日周五、16 日周一、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、26 日周四、27 日周五、28 日周六、29 日周日）✓；竞选 15 天（13–27 日）、禁发民调 5 天（24–28 日）、静默日 28 日、投票 29 日 9:00–20:00 均与日历自洽 ✓。
- 金句：`content7.py` quotes 8 句，在全版 SVG 文本中（去空白精确匹配）每句恰出现 **2 次** ✓。范文：AST 实测 `MODELO` 97 词 ✓（run.py 亦报 MODELO words: 97；P8 印「范文（97 词）」✓）。
- 译注词：P1–P5 各版 gloss 词元在当版 SVG 文本中全部 ≥2 次（P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 5；P5 sobre 5 / papeleta 2 / censo 3 / plazo 3 / urna 5；余见 GATE-LOG）✓。P2 无 la papeleta（build 6 已删）✓。
- 弯引号：text.md 中 U+201C/U+201D 各 5 对、U+2019 0、直引号/直撇号 0；8 张 SVG 文本节点内直引号/直撇号均为 0，弯引号成对（P1/P3/P5 各 1 对，P8 2 对）✓。E1（P2 C 组引言弯撇号）为 es-it 版级项，不属核心 ✓。
- 对外标签扫查：text.md 无 SOP/proofread/cover/语言代码/周次等内部标记；「VOL.4/VOL.5」仅为刊别与下期预告（读者可见的正常刊名信息），无内部结构语义 ✓。讲解/导读均为读者母语（简体中文）✓。

## §2 缺陷清单

无。缺陷数 0。

## §3 未决事项（O，观察/备注，均不构成缺陷、不阻塞定稿）

- **O1 — doblelectura 指南一句「Frente Amplio se echó atrás」未获佐证，正文不受影响。** 该指南（2026-11-10 数据）一处称 FA 对 Atresmedia 23 日「se echó atrás, según la cadena」（引 El Independiente）。本轮独立检索未找到任何佐证：反为 FA 自身 2026-11-09 20:50 声明（nuevaradio 引述）称 Colau 将参加 RTVE 与 Atresmedia 两场四人辩论；20minutos/radarprensa 11 月 9 日称 Colau 已确认；democrata 11 月 9 日 21:08 与 diariodia 11 月 9 日 23:35 称 FA 重申参加全部已提议辩论。且**正文全文无「Colau」一字**（grep 0 命中），P6 仅称「sin el PSOE confirmado」（只断言 PSOE 未确认，不含 Colau 断言）。故不论该传闻真伪，正文无假陈述，无需改动。KIT §5.2 括号内「Colau 已确认」以 11 月 9 日多源为准，不改。
- **O2 — 既有紧度（build 6 即有，非本次改动所致）。** 真墨 clearance 最紧两处均为 +0.1px（P2 ¿SABÍAS QUE…? 盒末行 `ley.` 墨底 543.4/盒底 543.5；P5 VOTAR 盒末行 `compara precios antes de pagar.` 墨底 1251.4/盒底 1251.5），墨仍在盒内、未溢出；P3 ¿Y TÚ? 盒 +2.5、P1 C1 +5.8。其余盒均 ≥+3.0。按 scope 不动。P2-feature 尾端 y=1537/底限 1540 同为 build 6 既有紧度。
- **O3 — JEC 逐党表未直读（与 FIX-LOG 相同 caveat）。** BOE-A-2026-23258 正文确认决议存在且分摊表公布于 JEC 网站；本轮检索未取回逐党表。本 proof 以 BOE 决议 + LOREG 第 64 条档位 + BOE-A-2026-23103 结构旁证为准核实 195 与 PCTE 保留；未重做 18,684 行全量逐省点数。如后续 JEC 申诉裁定改表，再行更新。
- **O4 — 195 为图示 8 党之和（FIX-LOG §5 已记备查）。** 脚注「195 minutos en total」指图示 8 党合计，非全国所有政党分钟总和；图表标题为「minutos de propaganda por partido」，未声称全国总和。不改版面。

## §4 判为非缺陷的项

- P2 日历 / P6 时间线无条件列 SER 18 日辩论（O7）：所述为已确认的事件，为真；P6 正文已以「acordado no es cerrado」澄清；Q89 键不受影响。按裁定只动表述、不动键。
- Q89 选项 C「el debate a cuatro」：泛指四人辩论，非特指某场；键 B（laSexta）唯一正确，无歧义。
- P6 正文跨栏断句「Un debate «propuesto» no es un debate / «cerrado»」：正常栏流断句，语义完整，无缺陷。
- P1「El primer debate fue también el viernes 13」：laSexta 13 日按时间最早（SER 为 18 日），为真。
- 23 日两场辩论同日（Atresmedia 四人 + RTVE 八人）：两源一致，时间线两行并列无误。
- #150 例外：见 §5。

## §5 核实摘要

- 全文通读：text.md 1,822 行 + 印 PDF P1/P6/P7/P8 目视；其余 4 页以 SVG 文本 + pdftotext 逐字覆盖。
- 150 键手验：150/150 通过（`keycheck-150.json`）。机械门：REG vs 印刷 149/150，仅 #150 开放题范文例外——REG 键为描述性文字「（开放题，范文如下）」，印刷键为「✓」（范文见 H 区，97 词已独立实测）。该例外合理：开放题无唯一答案，✓ 是既定排版约定，非错误。判为非缺陷。
- 机械门（全部自跑，证据见 GATE-LOG）：occlusion 0 flags（selftest 六类全过）；creambox 全版扫描 + 真墨裁定（C1 +5.8，其余盒末行真墨均 ≥+0.1 在盒内）；P7 toolbox 最小 +8.8；p8 extract 150/150；p8 compare build9→build10 CLEAN keydiff=[]、build6→build10 CLEAN keydiff=[139]；freeze baseline 8/8 逐字节相同；boxtitle 35 行 0 溢出；印/网文字层逐字节相同（106,440 字节）；P8 最小字号实测 10.125pt（723 runs，0 条 <9.75pt）；弯引号全版扫描通过；§1.1 字体/颜色：Newsreader、Noto Sans/Serif CJK SC、UnifrakturMaguntia，墨 #302c28、书绿 #46581f/#37402f、奶油 #f0eee5/#F1E8D4 均在 SVG 内。
- 外部事实：Correos 官方通告、JEC/BOE-A-2026-23258、BOE-A-2026-23103、LOREG 64/65/72、Atresmedia 改期（11 月 9 日多源）、doblelectura 指南（11 月 10 日数据，直接引用）、laSexta/SER/Mediaset/Academia、德比与欧冠比分、LaLiga 积分与赛程——除 O1/O3 备注外，全部独立核实通过。
- 源文件未改动、未重建、未 commit、未 push。keycheck 重跑 run.py 为进程内重建（确定性构建），事后复核 8 张 SVG 哈希与 build 10 一致，未改变交付物。

## 附：方法备注（非缺陷）

- `tools/freeze.py` 仅有 `baseline`/`diff` 两个子命令，无 `freeze_direct` 子命令——按任务要求记为方法备注，不当缺陷。freeze baseline 已实跑 8/8。
- 本轮 creambox 实跑（正典 `creambox.py`，md5 `ee7a55d8b2057cf4ad42a97bb1197383`）含逐行明细表，fix 的 `creambox10.log` 无逐行表——工具调用版本差异；inside-only 清除量逐项一致，creambox_diag 日志与 fix 的逐字节一致（`diff` IDENTICAL），数值结论相同。
- 本轮首次以绝对路径跑 freeze 时因 cwd 错误报过一次 `can't open file`（相对路径解析问题），纠正 cwd 后重跑 8/8；该失败为调用错误，非工具/构建问题。
