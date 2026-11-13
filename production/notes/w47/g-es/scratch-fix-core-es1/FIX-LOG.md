# FIX-LOG — W47 core-es fix（重开已定稿核心，build 7 → build 10）

> 范围：只动 `production/2026-w47/core-es/` 内文件；不碰任何 fan-out 版、不碰 `tools/`、不 commit、不 push。
> 工作目录：`~/workspace/weekly-git/hidden_files/w47/scratch-fix-core-es1/`（下称“本 scratch”）；全程 `TMPDIR` 指向本 scratch 内 `tmp/`，未写 `/tmp`。
> 日期：2026-11-11。构建工具：`~/workspace/weekly-git/tools/venv/bin/python`（run.py / render.py / tools/*）。

## 0. 编号消歧（六份 proof1 的编号易混，先定）

| 编号 | 含义 | 归属 |
|---|---|---|
| C1 | P1 CINCO CLAVES 盒 gloss 行漫出盒底 −12.0px | 核心，本轮修（build 7） |
| C2（es-it） | 邮寄投票截止日措辞 antes→hasta | 核心，本轮修（build 7，8 处） |
| es-ja D1 | P1 consejo 句截断（孤零零的 «cómo.»） | 核心，build 8 |
| es-ja D4 | P7 Marta 样信德比日期（周五→周六） | 核心，build 8 |
| es-ja D2 | P5 词库缺 correo/envío | = C3，**裁定不动**（见 §2.8） |
| es-nl D1 | Atresmedia 辩论日期 | 核心；build 9 误修→build 10 订正（见 §2.5） |
| es-nl D2 | “仅一场已确定”＋Q89 键 | 核心；build 9 误修→build 10 订正（见 §2.5） |
| es-pt C2 | RTVE 免费分钟脚注 | 核心，build 9（数字保留，只改脚注） |
| es-pt C1 | 11 月 13 日主题（经济-only vs 经济＋住房） | **不在 scope**，KIT §6.10 已裁定经济-only |
| es-zh-tw D1 | = C2（antes→hasta） | 核心项，见 §2.7 |
| es-zh-tw D2 | = es-ja D1（consejo 截断） | 核心项，见 §2.7 |
| es-zh-tw D3 | = C1（盒矮 20px） | 核心项，见 §2.7 |
| es-zh-tw D4 | = C3（词库干扰项） | **裁定不动**（见 §2.8） |
| es-zh-tw D5 | = es-ja D4（德比日期） | 核心项，见 §2.7 |
| es-ru PCTE | P6 RTVE 表＋Q84 键 B 称 PCTE 10 分钟 | 核心；核实后**保留，数字不动**（见 §2.6） |
| E1（es-it） | P2 C 组引言弯撇号 ’ | **本版级，es-it fix1 时修**，本轮不动 |
| O7 | P2 日历／P6 时间线无条件列 SER 18 日辩论，紧挨“propuesto ≠ cerrado”一课 | 观察；build 10 只改表述、不动 Q89 键（见 §2.5） |

## 1. 构建史与 SHA

（注：以 `…` 标示的 SHA 为截断值；build 9／10 给出全值。build 6/7/8 的全值未在本轮留存记录中，交付以 build 10 全值为准。）

### 基线 build 6（开工前实测，未改任何源码）
- 印刷版 `La-Lucerna-VOL4.pdf`：17,212,236 B，SHA-256 `4787e5c8…3870c`（截断值；本轮以 KIT §7 字节数与磁盘实测三 SHA 为准开工，符合即开工）
- 网页版 `La-Lucerna-VOL4-web.pdf`：1,372,318 B，SHA-256 `6e8fb9c8…30bbf`
- 文本导出 `2026-w47-es-zh-cn.text.md`：1,799 行，SHA-256 `c36412a7…6c8`
- SVG 首 8 哈希：p1 `53b84164` · p2 `4990202a` · p3 `f6fabc93` · p4 `897d34cb` · p5 `2fe8d4b0` · p6 `ba4b11c0` · p7 `220f647a` · p8 `99135e1c`
- 开工前快照：本 scratch `prefix-svg/`（build 6 SVG 全套）＋ build 6 PDF／text 副本。

### build 7（C1＋C2）——已交付内容
- 改动：`content12.py` 盒高 700→720（C1）；C2 8 处 antes→hasta（§2.2）。
- run.py rc=0，0 警告；TOTAL 150（A2 50／B1 72／B2 28；版面 10/18/18/18/18/18/12/38）；MODELO 97 词。
- 印刷版 17,212,752 B，SHA `db09f608…f0b89c`；网页版 1,410,286 B，SHA `f45171b4…0496a1`；text.md SHA `1a821289…ff748c`（43,221 B，1,799 行；与 build 6 diff 仅 C2 行）。
- SVG：仅 p1 `fc536bd7`、p2 `2c600daf`、p8 `fa6ac05f` 变。
- 门：occlusion 正式审计 0 flags（selftest 六类全过）；p8 extract 150/150；p8 compare build6→build7 CLEAN，keydiff=[139]（仅 #139 C2）；freeze baseline 8/8＋direct 8/8。

### build 8（＋es-ja D1/D4）
- 改动：`content12.py:130` consejo 句补足；`content7.py:99` «el viernes veo el derbi» → «el sábado veo el derbi»。
- run.py rc=0，0 警告。印刷版 17,212,757 B，SHA `b072fc16…9f6d0a793`；网页版 1,410,296 B，SHA `cb77ba42…caf928`；text.md SHA `49696333…e413a815`（1,799 行；与 build 7 diff 恰 2 行：L174 `cómo.` → `cómo leer un debate sin perderse.`；L1320 `el viernes veo el derbi` → `el sábado veo el derbi`）。
- SVG：仅 p1 `e24a4e35`、p7 `a376ef8c` 变。
- 门：occlusion 0 flags；p8 extract 150/150；p8 compare build7→build8 CLEAN keydiff=[]；build6→build8 CLEAN keydiff=[139]；freeze 8/8；creambox 与 build 7 相同。

### build 9（＋es-nl D1/D2＋es-pt C2）——D1/D2 部分已被 build 10 推翻，见 §2.5；C2 部分保留
- 改动：es-nl D1/D2（Atresmedia→26 日；“两场已确定”＋Q89 重写）；es-pt C2（P6 脚注改为 JEC 11 月 4 日决议口径）。
- run.py rc=0，0 溢出警告；P6-main col 1/2 y=669（原 523），P6 col3 尾 1267.2，timeline 盒高 810.7（＋1 折行），P6-ex col 3/3 y=2533 不变，P8-keys y=2382 不变；TOTAL 150，MODELO 97 词。
- 印刷版 17,213,724 B，SHA `71a782ecae197cb6c78c21723c2e317523490a1ed5271de73143418069a5f4c2`；网页版 1,411,243 B，SHA `bccff753b554803d5c87f80d33818ab6101374bb1de3de217a5666a4d7207577`（文字层 44,433 字节）；text.md SHA `9dd206c465119843c2d596d5062b94678801ea6834f89d4b2343d79e86c9aade`（1,807 行；与 build 8 diff 仅 D1/D2/C2 行＋P6 重排）。
- SVG：仅 p1 `2b6303c7`、p6 `63594326`、p8 `e83c4504` 变；p2 `2c600daf`、p3 `f6fabc93`、p4 `897d34cb`、p5 `2fe8d4b0`、p7 `a376ef8c` 不变。
- 门：occlusion 0 flags；p8 extract 150/150；p8 compare build8→build9 CLEAN keydiff=[]；build6→build9 CLEAN keydiff=[139]；freeze 8/8＋direct 8/8；keycheck 149/150（仅 #150 开放题例外，见 §3）；印/网文字层 9/9 逐页相同；P8 最小字号 10.125pt，0 条 < 9.75pt 底线；boxtitle 0 溢出；creambox 扫描＋diag；C1 200dpi 裁切目视已验。

### build 10 首渲（**已作废，不交付**）
- 源码状态：仅含 es-zh-tw 三项残留（§2.7），仍含 build 9 的 D1/D2 误修文本。
- 渲染于 2026-11-11 ~10:59。印刷版 17,213,731 B，SHA `e71afccca79566c9302500358a44996c0064c0f9d558932201be16cd5032822c`；网页版 1,411,256 B，SHA `77acf69e94385a903445e0ac1da22159b4d722ec0d0deb39a4232451ec8cd33d`。
- 作废原因：订正 steer（steer 6）到达后，D1/D2 文本必须重写；本组 SHA 不再代表交付物。日志留存：本 scratch `run10-pre-correction.log`、`render10-pre-correction.log`。另：该 period 的更早 `run10.log` 已保存为 `run10-pre-residue.log`（背景：es-zh-tw 残留于 2026-11-11 10:42 落源码，早于 10:30–10:31 的 run，盘上产物当时仍为 build 9——SHA 与 build 9 完全一致、text.md 仍含 “antes de ese día”×1 与 “須在 19 日前申請”×5——故 10:59 重跑以再生制品）。

### build 10 最终（**交付**，D1/D2 订正＋es-zh-tw 残留＋P1/P2 确认状态句）
- run.py rc=0，0 警告；render.py rc=0。
- 印刷版 `La-Lucerna-VOL4.pdf`：17,212,955 B，SHA-256 `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`。
- 网页版 `La-Lucerna-VOL4-web.pdf`：1,410,471 B，SHA-256 `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`（文字层 44,707 字节；< 7 MB）。
- 文本导出 `2026-w47-es-zh-cn.text.md`：1,822 行，43,788 B，SHA-256 `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`。
- SVG 首 8 哈希：p1 `947d1843` · p2 `4274b9ec` · p3 `f6fabc93` · p4 `897d34cb` · p5 `2fe8d4b0` · p6 `4095ea92` · p7 `a376ef8c` · p8 `19123831`。与 build 9 相比仅 p1、p2、p6、p8 变（本次改动所及版面）。
- 流程终点：P1-headline 1371/1828；P2-feature 1537/1540（**既有紧度**，pre-correction 日志同值，非本次改动所致；build 6 即为 1537，见 KIT §6.14）；P6-main col 1/2 y=920（底限 1540）；P6 col3 尾 1347.5，timeline 盒高 891.0；P6-ex 2533/2580；P8-keys 2382/2560；TOTAL 150，MODELO 97 词。
- text diff build9→build10：仅订正改动行（D1/D2 回退＋残留 (a)(b)(c)＋P1/P2 cara-a-cara 状态句＋abstract 句）及 P6 栏位重排。

## 2. 逐项改动记录

### 2.1 C1 — P1 CINCO CLAVES 盒 gloss 行漫出盒底（build 7）
- 缺陷：盒 `x=1439.5 y=588 w=422.5 h=700`，底边 y=1288.0；gloss 行 `五大看点，不编数字：全在本期里讲清。` 基线 y=1300.0，漫出 −12.0px。
- 修复（`content12.py`）：盒高 700→720，底边 1288→1308。
- 验证：基线清除量 **+8.0**；PIL 真墨清除量 **+5.8**（墨底 1302.2）；200dpi 裁切目视（本 scratch `c1-box-crop-200dpi.png`）确认 gloss 全入盒、下有奶油空隙。标准 ≥+5px，两项度量均达标。
- 全版同类扫查：creambox 全版扫描＋真墨裁定——其余盒 gloss 行均在盒内；最紧者 P2 盒（y=200，底 543.5，末行 `ley.`）墨清除量 +0.1（基线 +5.3）、P5 盒（y=939，底 1251.5，`compara precios antes de pagar.`）墨 +0.1（基线 +5.4）、P3 盒（y=1298，底 1571.8，`魂”的音乐？写两句寄来。`）基线 +4.5／墨 +2.5——**均在盒内**，属既有紧度、非溢出，按 scope 不动，列为观察（§5）。

### 2.2 C2 — 邮寄投票截止日措辞 antes→hasta（build 7，8 处）
- 事实（2026-11-11 网查核实）：Correos 官方通告 2026-11-10——“todavía pueden solicitar hasta el día 19 de noviembre (inclusive)”；JEC 日历（申请期 10 月 6 日–11 月 19 日）；LOREG 第 72 条；2026 年 11 月 19 日为周四（`date -d`）。
- 改动（`antes del jueves 19` → `hasta el jueves 19`）：
  1. `content12.py:41` P1 正文
  2. `content12.py:56` P1 题 3 题干
  3. `content12.py:124` P1 图注
  4. `content12.py:157` P1 闪电问答题干（同类额外发现）
  5. `content12.py:254` P2 题 12 题干
  6. `content8.py:23–24` P8 题 116 题干＋注（键 A 不变）
  7. `content8.py:74–75` P8 题 139 键句＋注＋中文题干（`邮寄投票须在周四 19 日前申请。` → `邮寄投票最迟须在周四 19 日申请。`）
  8. `content8.py:104` P8 模范文（同类额外发现）
- 核对：`antes del jueves` 在源码与新 text.md 中均为 0；`hasta el jueves` 在 text.md 中为 7。答案键 19 不动；Q116 键 A 不变。
- 一致性：版内他处已是 `hasta` 的说法（P2 正文、P5 正文、P8 题 123）保持一致，未动。

### 2.3 es-ja D1 — P1 consejo 句截断（build 8）
- `content12.py:130`：句尾孤零零的 `cómo.` → `En la página 6 te enseñamos cómo leer un debate sin perderse.`（与紧邻图注措辞一致）。

### 2.4 es-ja D4 — P7 Marta 样信德比日期（build 8）
- `content7.py:99`：`el viernes veo el derbi` → `el sábado veo el derbi`。
- 事实：塞维利亚德比（Sevilla–Betis）周六 21 日 18:30；周五 20 日为 Athletic–Espanyol。核对 P4 赛程表（`content34.py:120/131/146`）与 Q118（键 B，“塞维利亚德比在周六”）、Q124、Q134、Q138——样信为唯一例外。
- 金句未破（两句均非金句）。

### 2.5 es-nl D1/D2 —— build 9 误修，build 10 订正（本轮最重要的一次转向）
- **build 9 的改动（已推翻）**：D1 把 Atresmedia 四方辩论改到 11 月 26 日（改 P6 正文＋时间线：RTVE 23／Atresmedia 26）；D2 把 P6＋P1 改为“两场已确定”（laSexta＋SER），并重写 Q89 题干（键仍为 B）。
- **订正的触发**：协调员 steer（2026-11-11 06:03 EST）指出 es-zh-tw proof1 的核对表（协调员已从磁盘核实其引用的来源与日期）证明 build 9 的 D1/D2 定性有误，要求按一手来源直接核实、不得只凭某一方 proof1 改。
- **D1 订正——Atresmedia 23 日是对的，不改到 26 日**（2026-11-11 直接核实）：
  - zocalopublico.com 2026-11-09T17:25:38Z：“Ese duelo… lo fijaron tanto Atresmedia como RTVE para el mismo día, el 26. Ante esa coincidencia, el grupo propietario de Antena 3 y La Sexta anunció este lunes que lo anticipa al día 23. Los líderes del PP, Vox y FA han confirmado su presencia… pero no así el PSOE. Atresmedia, en una nota, insistió en que 'la invitación sigue abierta a Sánchez'.”
  - radarprensa.com 2026-11-09T15:22:24Z（经 20minutos）：“Atresmedia ha trasladado su debate electoral a cuatro al lunes 23 de noviembre… El cambio responde al bloqueo que provocaba la coincidencia con el debate a cuatro de RTVE, previsto para el jueves 26 de noviembre.”Feijóo、Abascal、Colau 已确认；PSOE 邀请开放。
  - elfolio.es（Academia 文，11 月 9–10 日）：“Atresmedia ha trasladado al 23 de noviembre su propuesta… cuenta con la aceptación del PP, Vox y Frente Amplio. La participación del PSOE continúa pendiente de confirmación.”；“RTVE había propuesto organizar su propio debate a cuatro el 26 de noviembre… también había ofrecido un cara a cara entre Sánchez y Feijóo para el 17 de noviembre y otro encuentro con representantes de los ocho grupos parlamentarios del Congreso para el día 23.”
  - diariosabemos.com：Abascal 已确认 Atresmedia 四方 23 日（与 Feijóo、Colau 同场；邀请 Sánchez 开放）；“Atresmedia decidió adelantar su debate al 23 de noviembre para evitar la coincidencia con el encuentro que RTVE había propuesto para el día 26.”
  - vibrasencorte.es：“Atresmedia 已把四方辩论移到 11 月 23 日周一，Feijóo、Abascal、Colau 已确认，邀请 Sánchez 仍待回复。”
  - 结论：es-nl D1 的证据（11 月 4–6 日，cronicadecantabria.com 2026-11-04T21:02：Feijóo 将出席 Atresmedia 四方辩论、当时提议为 26 日）按当时正确，**已被 11 月 9 日改期取代**。按 11 月 10 日截稿口径，“Atresmedia 23 日”成立，不是缺陷。
  - 26 日时间线行：指 PP 另提的方案。elfolio.es：“La propuesta del PP sitúa este debate el 26 de noviembre… No obstante, todavía no existe una confirmación definitiva del calendario ni de la composición del encuentro.”；diariodia.es 2026-11-09T23:35：PP 接受 Academia 组织辩论；cara a cara 11 月 16 日、另一场 11 月 26 日（4–5 名主要全国候选人）；democrata.es 2026-11-09T19:52：PP 提议 cara a cara 11 月 16 日＋第二场 11 月 26 日（4–5 名主要候选人）；elfolio.es：“Las fechas definitivas, los horarios, los moderadores y la lista definitiva siguen sin cerrar.”11 月 9 日周一 PSOE 与 PP 达成协议：Academia de Televisión 组织两场辩论（cara a cara＋四方）。
  - RTVE 计划（多源一致）：cara a cara 11 月 17 日、Debate a 8（8 个议会党团发言人）11 月 23 日、四方辩论 11 月 26 日（articulo14.es 11 月 3 日；actualtv.es 10 月 23 日；democrata.es 10 月 23 日表：“Debate de portavoces parlamentarios | 23 de noviembre | RTVE | Propuesto por la corporación y aceptado por el PP; sin confirmación completa de participantes”）。故 11 月 23 日同时有 RTVE Debate a 8（提议，PP 已接受）与 Atresmedia 四方辩论（3 党已确认，PSOE 待定）。
- **D2 订正——Q89 键 B 未错，裁定保留**（两源冲突，最新来源支持本版）：
  - doblelectura.es 指南（2026-11-10 数据；协调员已从磁盘核实原文；本 agent 未直接拉取该指南全文，独立多源复核结论一致）：«A 10 de noviembre de 2026 solo hay un debate cerrado: el de portavoces de laSexta… Solo está cerrado el debate de laSexta»——«cerrado» = 全锁定（时间／主持／阵容）。
  - laSexta 周五 13 日 21:30：时间、主持（Ana Pastor）、阵容（Carlos Cuerpo PSOE、Juan Bravo PP、Pablo Bustinduy Frente Amplio、José María Figaredo Vox）、主题（经济）、现场观众——全部已公布→全锁定→“cerrado”（diariodesantiago.es 11 月 6 日；doblelectura.es 指南引文，KIT §5.2 已引：“Cerrado. A las 21:30, con Ana Pastor. Cuerpo, Bravo, Bustinduy y Figaredo.”）。
  - SER 住房辩论周三 18 日：两党 10 月 21–22 日已确认（Tellado 致函提议；Torró 接受；PP：“Aceptamos: quedamos a la espera de la concreción de los detalles”——democrata.es／cronicadecantabria.com／elconstitucional.es，均为 2026-10-22）。**2026-11-11 检索未发现任何已公布时间**（检索 “Cadena SER debate vivienda 18 noviembre 2026 Isabel Rodríguez Juan Bravo hora” 无时间）。diariodesantiago.es 11 月 6 日“ Solo hay dos encuentros temáticos confirmados” 用的是 “confirmados”（作为事件已确认）——比 “cerrado”（全锁定）弱一档。按 “cerrado = 全锁定” 口径，SER 不算 cerrado。
  - Mediaset cara a cara 周一 16 日：两党接受，但 articulo14.es 11 月 3 日：“todavía no se ha comunicado oficialmente la hora de comienzo ni la duración”→同样未全锁定。
  - democrata.es 10 月 23 日表的标准：“Las propuestas y aceptaciones parciales no equivalen a una convocatoria cerrada con horario, formato y todos los participantes confirmados.”
  - 结论：本版 “solo hay un debate cerrado”（laSexta）正确。Q89 键 B 保留；Q90 不受影响（laSexta 事实为真）。
- **build 10 的 8 处源码改动（全部在 core-es 内）**：
  1. `content12.py:39`（P1 lead）：“Fue uno de los dos debates cerrados al cierre de esta edición.” → “Fue el único debate cerrado al cierre de esta edición.”（build 8 原文恢复）
  2. `content12.py:40`（P1 lead）：“El lunes 16, el PP propone un cara a cara entre Sánchez y Feijóo. El PSOE no lo había confirmado el 10 de noviembre: esta página no da por cerrado lo que aún se negocia (página 6).” → “El lunes 16, el PP propone un cara a cara entre Sánchez y Feijóo. Los dos partidos aceptan la cita, pero no hay hora publicada: esta página no da por cerrado lo que aún se negocia (página 6).”——旧句按 11 月 10 日口径为假：PSOE 10 月 22 日已接受 Mediaset cara a cara 11 月 16 日（Ferraz 声明，cronicadecantabria.com 与 democrata.es 2026-10-22 引述）；PP 提议 11 月 16 日（Tellado，11 月 9 日）。截至 11 月 10 日无公布时间（articulo14.es 11 月 3 日；elfolio.es 11 月 9–10 日：时间仍待定）。与 D1/D2 同类（11 月 10 日确认状态），随订正一并修。
  3. `content12.py:174`（P2 正文，Flamenco 段）：“Y ese mismo lunes, el PP propone un cara a cara entre Sánchez y Feijóo: a 10 de noviembre, el PSOE no lo había confirmado.” → “Y ese mismo lunes, el PP propone un cara a cara entre Sánchez y Feijóo: los dos partidos aceptan la cita, pero no hay hora publicada.”——同一假陈述的第二处， broad sweep 后发现。
  4. `content56.py:123`（P6 正文第 1 段）：“Al cierre de esta edición, el 10 de noviembre, hay dos debates cerrados: el de portavoces de laSexta, el viernes 13 a las 21:30, con Ana Pastor, y el de vivienda en la Cadena SER, el miércoles 18, con Isabel Rodríguez (PSOE) y Juan Bravo (PP). En laSexta van Carlos Cuerpo (PSOE), Juan Bravo (PP), Pablo Bustinduy (Frente Amplio) y José María Figaredo (Vox), a hablar de economía, con público en el plató.” → “Al cierre de esta edición, el 10 de noviembre, solo hay un debate cerrado: el de portavoces de laSexta, el viernes 13 a las 21:30, con Ana Pastor. Van Carlos Cuerpo (PSOE), Juan Bravo (PP), Pablo Bustinduy (Frente Amplio) y José María Figaredo (Vox), a hablar de economía, con público en el plató.”（build 8 原文恢复）
  5. `content56.py:124`（P6 正文第 2 段）重写——“El debate de vivienda en la Cadena SER, el miércoles 18, ya está acordado (Rodríguez–Bravo), pero no se había publicado la hora al cierre de esta edición: acordado no es cerrado. El PP propone un cara a cara entre Sánchez y Feijóo para el lunes 16, y un debate a cuatro para el jueves 26; el lunes 9, PSOE y PP acuerdan que la Academia de Televisión organice los dos debates, pero las fechas, las horas y los participantes siguen sin cerrarse. Atresmedia convoca su propio debate a cuatro para el lunes 23, sin el PSOE confirmado. RTVE propone un debate a ocho, con los portavoces de los ocho grupos, para el lunes 23. Un debate «propuesto» no es un debate «cerrado»: la primera lección de esta página es leer el verbo.”（O7 澄清＋Academia 11 月 9 日协议＋Atresmedia 23 日恢复＋RTVE 八人 23 日保留；build 8 的 “El PSOE no había confirmado ninguna fecha el 10 de noviembre” 未恢复——按 11 月 10 日口径为假。）
  6. `content56.py` 时间线：`"23 NOV. — RTVE propone un debate a ocho, con los portavoces de los ocho grupos.",` → `"23 NOV. — Atresmedia convoca un debate a cuatro (sin el PSOE).",` ＋新增行 `"23 NOV. — RTVE propone un debate a ocho, con los portavoces de los ocho grupos.",`；`"26 NOV. — Atresmedia propone un debate a cuatro (el PP lo acepta).",` → `"26 NOV. — El PP propone un debate a cuatro de la Academia (sin fecha pactada).",`（澄清 26 日为 PP／Academia 方案，区别于 Atresmedia 的 23 日辩论）。
  7. `content56.py` Q89：题干恢复为 “El único debate cerrado es... A. el cara a cara · B. el de laSexta · C. el debate a cuatro”，**键仍为 B**，键注恢复为 “截至 11 月 10 日只有 laSexta 辩论已确定”。（选项 C 确认为 “el debate a cuatro”：text8 导出中 “C. el debate a cuatro portavoces” 的杂糅是 Q89 “C. el debate a cuatro” 与 Q93 “cuatro portavoces” 片段在导出中交错所致。）
  8. `ABSTRACT.txt`：“截至 11 月 10 日已确定的辩论有 13 日晚 laSexta 四人辩论与 18 日 SER 住房辩论” → “截至 11 月 10 日只有 13 日晚 laSexta 四人辩论完全锁定”。
- **未动的决定**：时间线 `"16 NOV. — El PP propone el cara a cara Sánchez–Feijóo (sin confirmar)."`（按 “cerrado” 标准不假——无公布时间）；P2 日历 SER 行（`content12.py:180`，“Miércoles 18 — debate sobre vivienda en la Cadena SER: Isabel Rodríguez (PSOE) y Juan Bravo (PP)”）与 P6 时间线 `"18 NOV. — Debate sobre vivienda en la Cadena SER (Rodríguez–Bravo)."`（已确认的事件，为真）；Q90 不变；已核实正确的项目不动（Mediaset cara a cara 周一 16 日、laSexta 周五 13 日 21:30、SER 周三 18 日）。
- **观察 O7**（记为观察，非缺陷）：P2 日历与 P6 时间线无条件列出 SER 18 日辩论，紧挨本页 “propuesto ≠ cerrado” 一课。steer：如要动，只动表述、不动 Q89 键，除非直查到 11 月 10 日前 SER 辩论已全锁定的证据（未找到）。build 10 在 P6 正文增一句澄清（见改动 5 首句），日历／时间线条目保持原样（所述为已确认的事件，为真）。

### 2.6 es-pt C2 — RTVE 免费分钟（build 9；数字保留，只改脚注）与 es-ru PCTE 核查（数字不动）
- **es-pt C2**：P6 图表数字保留（PSOE 45／PP 45／Vox 30／Frente Amplio 30／Podemos 15＋3×10=195）。只改图表脚注的归因：
  - 旧：“Junta Electoral Central: 195 minutos en total”（裸呈现为 JEC 已定事实）。
  - 新：“Acuerdo de la Junta Electoral Central del 4 de noviembre: 195 minutos en total, del 13 al 27 de noviembre. Tres formaciones más tienen 10 minutos cada una: Frente Obrero, PCTE y SALF.”
- **不改写成“RTVE 提案，待 JEC 批准”**——该表述事实有误：JEC 11 月 4 日决议（BOE-A-2026-23258）已按 Radio/TV 委员会提案（LOREG 第 65 条）同意分配；申诉截止 11 月 6 日周五 14:00，答辩截止 11 月 10 日周二 10:00，RTVE 同日答复。KIT §5.3 原引的 queproponen.es 页面无法独立检索证实，改引 BOE-A-2026-23258。
- **档位推导（LOREG 第 64 条）**：10 分钟（无议席）、15 分钟（有议席、得票 <5%）、30 分钟（5–20%）、45 分钟（≥20%）。2023 年：PP 33.06%→45、PSOE 31.68%→45、Vox 12.39%→30、Sumar 12.33%→Frente Amplio 约 26/31 席≈10.35%→30、Podemos 5 席×（3,044,340/31≈98,204）≈491k≈2.0%→15；Frente Obrero／PCTE／SALF 无 2023 年议席→各 10 分钟。
- **档位对 Sumar 权利继承争议稳健**：即使按 Podemos 自称的 21% Sumar 权利计（≈639k≈2.6%），Podemos 仍为 15 分钟，Frente Amplio 仍为 30 分钟。Frente Amplio 与 Podemos 正在 JEC 争夺 Sumar 2023 年权利的继承（diariodia.es／Europa Press 2026-11-01，更新 11-09）；JEC 第一轮判 Frente Amplio 胜（En Comú 议席＋1），Podemos 独立议员主张被驳回。JEC 判例 doctrine：联盟票按席位分摊（党得票＝联盟总票÷席位数×该党席位数）；无法按比例分摊时均分。
- Q83–85 键不变；Q88 注（只刊登选管会公布数据并注明来源）随脚注注明来源而成立；Q87 不变。
- **观察**：195 为图示 8 党之和，非全国所有政党——记备查，不改版面。
- **es-ru PCTE 核查——决定：保留（无内容改动）**：
  - 质疑：P6 表＋Q84 键 B 称 PCTE 10 分钟、总计 195 分钟。PCTE 只有 39 个 Congreso 选区（BOE 3 Nov，按 es-ru）；JEC 判例（671/2011、666/2011）要求 40 个（或 Senado 46 个）；39/52 恰为 75.0%，差 1 个。JEC 表本身（BOE-A-2026-23258，4 Nov）搜不到，PCTE 的 Senado 路数未知。若 JEC 表排除 PCTE，则“PCTE 10 分钟”、195 总分钟、Q84 键 B 全错（应为 185）。
  - **法律（2026-11-11 核实）**：LOREG 第 64.2 条（JEC 自身 LOREG 文本）：免费分钟权利要求在媒体覆盖范围内的选区中参选超 75%。第 64.3 条例外（某自治区 ≥20%→全国 15 分钟、仅在该区播出）不适用于 PCTE。JEC Acuerdos 671/2011＋666/2011（原文）：任一院达标即可（“basta con presentar candidatura a cualquiera de las Cámaras”）；国会 52 选区→需 **40 个已公布参选名单**；参议院 **60** 选区（48 省、2 自治市、10 岛区）→需 **46** 个。671/2011 §3：某党在部分选区单打、部分选区联盟参选的，**不可相加**。674/2011：按分配时已公布参选名单计数；如申诉后计数超阈值，则启用时段。
  - **BOE-A-2026-23103 逐省点数（11 月 3 日公布名单，18,684 行；browser.open＋browser.find 逐省核对，以省节标题分类）**：

    | 名称 | 国会 | 参议院 |
    |---|---|---|
    | PCTE 本名 | 32 | 30 |
    | ELAK（Euskadi 联合会） | 3 | 3 |
    | PCTG（Galicia 联合会） | 3 | 3 |
    | PCTC（Catalonia 联合会） | 4 | 4 |
    | **家族合计** | **42** | **40** |
    | 并集省份 | **45** | — |

    并集 45 省与 Europa Press “PCTE，con listas en 45 provincias”（clm21.es／cronicadecantabria.com，2026-11-03，按已提交名单）**完全吻合**，旁证计数。es-ru 的“39”最可能是本名 32＋ELAK 3＋PCTC 4＝39（漏计 PCTG 的 3 个），或另一种聚合口径；不是家族全数。
  - **计数纠错记录**：两处边界误读在复核中被发现并纠正——L13128 初读为 Palencia 参议院，实为 Las Palmas 国会（开 L12966–13574 核实：Las Palmas 国会 PCTE 第 7 名，首位 Domingo González Perdomo）；L6457 初读为 A Coruña 参议院，实为 Cuenca 国会。PCTE 本名全缺的省：Albacete、Badajoz、Barcelona（有 PCTC）、Ciudad Real、Lleida（有 PCTC）、Lugo、Palencia、Ceuta、Melilla；Lleida／Lugo／Barcelona／Ciudad Real／Badajoz／A Coruña 有联合会名单。
  - “未公布”抽查：抽样的 PCTE 标题后均跟候选人姓名（已公布）；未发现未公布的 PCTE 标题，但 62 处未逐一核查。BOE 全文 “No proclamada” 共 32 处，已识别的在已开窗口内为 FE de las JONS、I.P.A.L.、JUSTICIA Y LEY、PACMA——非 PCTE／SALF／FO。稳健性：家族国会 42 对阈值 40——即使 2 个 PCTE 国会名单未公布，仍达标。
  - **SALF**（同 BOE）：“SE ACABÓ LA FIESTA (SALF)”＝44 处，**全部国会**（抽样：Albacete、Alicante、Almería、Álava、Asturias、Zamora、Zaragoza 国会；抽样的参议院节均无）→44≥40（84.6%）→10 分钟达标。FO：抽样各省均有公布；democrata.es：全 52 省。
  - Instrucción 2/2026（JEC，2026 年 10 月 26 日，免费时段分配；2026-11-11 全文读过）：仅设委员会与授权，不解决联合会计数。Acuerdo 489/2023（2023 年分配）同样无表——JEC 惯例为分配表是单独的网站文件（“Dicha distribución está publicada en la página web de la Junta Electoral Central”），不在 acuerdo／BOE 正文内。
  - **JEC 逐党表本身：仍未取回**——6 次以上检索＋BOE 全文＋diariodia 全文＋RTVE 排期＋pcte.es 检索（2026-11-11）。diario.jurilia.com 明言具体逐党分摊“no está aún en las fuentes consultadas”。无任何二手来源列出 10 分钟获得者名单。
  - **裁定**：PCTE 保留 10 分钟；195 总分钟；Q84 键 B 不变。理由：按 JEC 自身阈值与 BOE 计数，PCTE 家族计数（42）达标；聚合问题取决于 JEC 是否把地区联合会（ELAK／PCTG／PCTC）计为同一“政治实体”——与 PSOE／PSC 平行、与 671/2011 §3（针对单打与联盟混参，不针对联合会）一致；联合会按第 64／65 条为单一实体。es-ru 质疑的前提（“39 国会，差 1 个”）本身计数有误（家族实为 42，非 39）。无任何积极证据表明 JEC 排除 PCTE（无申诉、无新闻、无反向表格）。
  - **残留 caveat（实话实说）**：JEC 逐党表公布于 JEC 网站、未被检索收录；本决定以法律＋已公布参选名单计数为准。如后续 JEC 申诉裁定改表，再行更新——但就本刊所引的 11 月 4 日决议（即本刊归因的对象）而言，PCTE 达标。

### 2.7 es-zh-tw 归属裁定与三项核心残留（build 10）
- **归属裁定（协调员 steer 4）**：es-zh-tw proof1 把 D1/D2/D3/D5 归为“fan-out 引入、核心本来就是对的”是**错的**——它拿已在修的核心当基线量。证据：① es-fr fix1 同期记录：2026-11-11 约 10:12–10:13 核心 `content12.py`／`content8.py` 被从 antes 改为 hasta（正是本轮 C2）；② 核心 `content7.py:99` 现已是 «el sábado veo el derbi»（本轮 es-ja D4 已落地）；③ 本 scratch `creambox9.log` 显示核心 P1 CINCO CLAVES 盒底现为 1308.0（本轮 C1 已落地），而各版仍为 1288.0。结论：D1（=C2 antes→hasta）、D2（=es-ja D1 consejo 截断）、D3（=C1 盒矮 20px）、D5（=es-ja D4 德比日期）**全部是核心项，本就属于本轮 scope**，各版随核心重建即解决。**不得让任何人手改 10 个版的 `content12.py`／`content7.py`。**
- **残留 (a)**：P2 正文 `tiene que pedirlo en Correos o por internet antes de ese día` → `hasta ese día`（`content12.py:175`）。该句前半（“El jueves 19 es un día clave: termina el plazo para pedir el voto por correo.”）为 P7 金句 #2——未动，无金句破损。
- **残留 (b)**：中文键注 `郵寄投票須在 19 日前申請`（keys 3、9、22、65、123）→ `最遲 19 日/截至 19 日`。5 处均经 sed 改为 `邮寄投票最迟须在 19 日申请`（与 Q139 已修注 `邮寄投票最迟须在周四 19 日申请。` 平行）：`content12.py:55`（Q3 注）、`:156`（Q9 闪电问答注）、`:277`（Q22 注）、`content56.py:67`（Q65 注）、`content8.py:38`（Q123 注）。旧串在核心源码中现为 0。P8 Q139 注 build 7 时已正确。
- **残留 (c)**：`ABSTRACT.txt`——同一行含两个过期事实：`邮寄投票 19 日前申请` 与 `唯一已确定的辩论是 13 日晚 laSexta 四人辩论`（D2 的假陈述，同类、同行、核心文件）。build 10 首渲时先改为 `…截至 11 月 10 日已确定的辩论有 13 日晚 laSexta 四人辩论与 18 日 SER 住房辩论，11 月 29 日大选投票，邮寄投票最迟 19 日申请；…`；订正时辩论句再改为 `截至 11 月 10 日只有 13 日晚 laSexta 四人辩论完全锁定`（见 §2.5 改动 8）。

### 2.8 裁定不动（写明以免后轮重提）
- **C3 / es-ja D2 / es-zh-tw D4 —— 裁定 ACCEPTED as-is，不动**：P5 B 组词框 2 答案在框外＋框内 2 词未用＝干扰项设计（4 用词＋2 干扰词，6 答案全部正确无歧义），协调员已裁定接受现状。**未动 `content56.py:79`，未把 sobre·urna 换成 correo·envío。**es-zh-tw D4 提议的“把 sobre·urna 换成 correo·envío”不执行——同一项、同一裁定。
- **E1 —— 本版级，es-it fix1 时修**：P2 C 组引言 1 处弯撇号 ’，与本轮无关，未动。
- **es-pt C1 —— 不在 scope**：11 月 13 日主题经济-only vs 经济＋住房；KIT §6.10 已裁定经济-only，未动。
- **Q90 不受影响；已核实正确的辩论项目不动**（Mediaset cara a cara 周一 16 日、laSexta 周五 13 日 21:30、SER 周三 18 日）。
- **不编造数字**（es-pt C2；PCTE）。MODELO 保持 97 词。Q116 键 A 不变。

## 3. 门禁结果（build 10 最终，全部跑于 2026-11-11）

| 门 | 工具／方法 | 结果 |
|---|---|---|
| 构建 | `run.py` | rc=0，0 警告；TOTAL 150（A2 50／B1 72／B2 28）；MODELO 97 词 |
| 渲染 | `render.py` | rc=0；print 17,212,955 B；web 1,410,471 B |
| 几何遮挡审计 | `tools/occlusion_audit.py`（正式审计，未加 --selftest；selftest 在内自动跑） | **0 flags**（selftest 六类全过） |
| p8 提取 | `tools/p8.py extract`（p8 SVG，total 150） | **150/150**（`p8-extract10.json`） |
| p8 比对 | `tools/p8.py compare` | build9→build10 **CLEAN，keydiff=[]**（`p8-compare10.json`）；build6→build10 **CLEAN，keydiff=[139]**（`p8-compare10b.json`；仅 #139 变——build 7 的 C2 改动；Q89 不在 keydiff 内，证实 D2 回退恢复了原键） |
| freeze | `tools/freeze.py baseline` | **8/8 SVG 逐字节相同**（`freeze10.log`；本构建目录下工具直接报 8/8；§6.9 的 0/8 为旧 scratch-es 布局下的收集盲区，见 §6） |
| keycheck | 本 scratch `keycheck_core.py`（进程内跑 run.py；须先 `sys.argv=['run.py']`，因 run.py 从 `sys.argv[1:]` 取文件列表） | **149/150**（`keycheck-150.json`）；仅 #150 不符——开放题，REG 键 `（开放题，范文如下）` vs 印刷 `✓`，已知预期例外，rc=0 |
| creambox | `creambox.py`（es-it proof 原样复制）全版扫描＋`creambox_diag.py` 真墨裁定 | C1 盒基线 +8.0／真墨 +5.8；其余盒自有末行真墨清除量均 ≥ +0.1；无其他 gloss 溢出（同类扫查 CLEAN） |
| boxtitle | `boxtitle_core.py`（见 §6 事故记录） | 35 行、**0 溢出**；与 build 9 唯一差：`LEER UN DEBATE` 盒 y=1037→1117（时间线盒 810.7→891.0 增高所致），清除量同值 +202.4 |
| 印／网文字层 | `pdftotext -layout` 两 PDF，逐页比对 | **9/9 相同**（8 页＋尾页换页符；各 106,440 字节） |
| P8 最小字号 | pypdf visitor，有效字号 `font_size*|tm[3]|` | 最小 **10.125pt**，0 条 < 9.75pt 底线（723 条 runs；注：不用 tm 比例的朴素 visitor 会误报 1.0pt） |
| §1.1 | SVG 内字体／颜色 | Newsreader 1200、Noto Sans CJK SC 608、Noto Serif CJK SC 310、UnifrakturMaguntia 1；#302c28 墨、#46581f 书绿／橄榄、#f0eee5 奶油、#F1E8D4 |
| 日期星期 | `date -d`，Europe/Madrid | 11 月 9 日周一、10 日周二、13 日周五、16 日周一、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、25 日周三、26 日周四、27 日周五、28 日周六、29 日周日 |
| 外部事实 | 网上逐项核实（见 §4） | 全部核实通过（Correos／JEC／LOREG；Atresmedia 11 月 9 日改期；laSexta／SER／Mediaset／Academia；RTVE 分钟 BOE-A-2026-23258；PCTE 计数 BOE-A-2026-23103） |
| 150 题答案键语义核对 | text10.md 全文通读（L1590–1822） | 150 键全部在册、与版面内容及已核实事实一致（抽查：#3/#9/#22/#65/#123 邮寄“最迟须在 19 日申请”；#49/#118/#124/#129 德比周六；#83–88 RTVE 分钟；#89 B“截至 11 月 10 日只有 laSexta 辩论已确定”；#90 A laSexta 周五 13 日 21:30；#91 C“propuesto ≠ cerrado”；#139“邮寄投票须在周四 19 日申请。”；#150 ✓ 开放题）。P1 lead 与 P6 正文／时间线区域已按最终文本读过并核实 |
| 金句 | 全 SVG 语料程序计数 | 8 句每句恰出现 **2 次**（包括 #7 “En campaña, no todo lo que se anuncia está cerrado.” 与 #8 “Una encuesta es una foto con margen de error, tomada en un día concreto.”；其余 6 句为 P1、P2、P3、P4、P5、P6 lead 句在 P7 “FRASES DE LA SEMANA” 栏的引用）。改动句无一是金句，无破损。P1 “El primer debate fue también el viernes 13” 仍真（laSexta 周五 13 日按时间最早；SER 为周三 18 日） |
| 字数 | SVG 文本节点长度求和（同法跨构建） | build 6＝35,103；build 9＝35,365；build 10＝**35,620**。注意：KIT §3 既往 36,660（build 6）为另一口径，不可直接与本数比较；KIT 更新已注明方法与同法三值 |

## 4. 外部事实核实总表（2026-11-11）

- 邮寄投票截止日：Correos 官方通告 2026-11-10（“hasta el 19 de noviembre (inclusive)”）；JEC 日历（申请 10 月 6 日–11 月 19 日）；LOREG 第 72 条；11 月 19 日＝周四。
- 德比：Sevilla–Betis 周六 21 日 18:30；Athletic–Espanyol 周五 20 日。
- Atresmedia 改期：zocalopublico.com 2026-11-09T17:25；radarprensa.com（经 20minutos）2026-11-09T15:22；elfolio.es 2026-11-09；diariosabemos.com；vibrasencorte.es（见 §2.5 原文）。
- laSexta 锁定：diariodesantiago.es 2026-11-06；doblelectura.es 指南 2026-11-10（“Cerrado. A las 21:30, con Ana Pastor.”；“solo hay un debate cerrado: el de portavoces de laSexta”——协调员已从磁盘核实原文；本 agent 未直接拉取该指南全文，独立多源复核结论一致）。
- SER 住房辩论：两党 10 月 21–22 日确认（democrata.es／cronicadecantabria.com／elconstitucional.es，2026-10-22）；**无公布时间**（2026-11-11 检索，未见）。
- Mediaset cara a cara：PSOE 10 月 22 日 Ferraz 声明接受；PP 提议 11 月 16 日；无公布时间（articulo14.es 2026-11-03；elfolio.es 2026-11-09–10）。
- Academia 协议：11 月 9 日 PSOE 与 PP 同意 Academia de Televisión 组织两场辩论；PP 提议 16 日 cara a cara＋26 日四人辩论；日期／时间／主持／参与者未定（elfolio.es、diariodia.es 2026-11-09T23:35、democrata.es 2026-11-09T19:52）。
- RTVE 分钟：BOE-A-2026-23258（JEC 2026 年 11 月 4 日决议）；LOREG 第 64／65 条；Sumar 权利争议 diariodia.es／Europa Press 2026-11-01（更新 11-09）；canariasenpleno 11 月 5 日 RTVE 新闻覆盖占比（FA 6% vs Podemos 0.86% 的新闻块）是**另一回事**（新闻覆盖，非免费广告分钟）。
- PCTE：BOE-A-2026-23103（11 月 3 日公布名单）；JEC Acuerdos 666/2011、671/2011、674/2011；LOREG 第 64.2／64.3 条；Europa Press “PCTE，con listas en 45 provincias”（clm21.es／cronicadecantabria.com，2026-11-03）。

## 5. 观察（非缺陷，不修，记备查）

- 既有紧度（盒内，不溢出）：P2 盒墨 +0.1、P5 盒墨 +0.1、P3 盒墨 +2.5（§2.1）；P2-feature 尾端 y=1537／底限 1540（build 6 即有）。
- 195 为图示 8 党之和，非全国所有政党（§2.6）。
- `antes de ese día` 观察：P2 正文一处同类措辞，已随残留 (a) 改为 `hasta ese día`（§2.7）。
- O7（§2.5）：P2 日历／P6 时间线无条件列 SER 18 日辩论，紧挨“propuesto ≠ cerrado”一课；build 10 以 P6 正文一句澄清解决，未动 Q89 键。
- 字数口径：KIT 既往 36,660（build 6）与本轮同法实测 35,103（build 6）差约 1,500 字符——两法口径不同；KIT 更新已写明同法三值（35,103／35,365／35,620），不混用。
- JEC 逐党表未取回（见 §2.6 末段）。
- build 9 摘要曾称 boxtitle 最紧清除量 +103.9，但 `boxtitle9.log` 本身显示 +16.0 的行（例如 `LA SEMANA EN CIFRAS` clear=+16.0）——+103.9 的说法与日志不一致；门禁标准是 0 溢出，build 9 与 build 10 均过，数字以日志为准。

## 6. 工具事故与方法记录

- **`creambox_diag.py` 锚点 bug（2026-11-11 发现并修复）**：首版用 `font.getbbox()` 未减 ascent，高估墨底约 24px。已按 `tools/occlusion_audit.py` 的 `ink_box` 修正（墨底 ＝ ty − ascent ＋ bbox[3]/SCALE）。build 9／10 的数字为修正后值。
- **`boxtitle.py` 错目录事故**：从 es-pt proof 复制的 `boxtitle.py` 硬编码 glob es-pt 版目录（`2026-w47-es-pt/svg/*.svg`），忽略参数——首跑测的是 es-pt 版而非核心（报出 `LA SEMANA EN CIFRAS` 溢出 −10.9 与葡萄牙语 gloss `Em números`，属 es-pt 版，不属核心）。已改 `boxtitle_core.py`（目录取 `sys.argv[1]`，并补缺失的 `import sys`）；核心 build 10：35 行、0 溢出。
- **freeze.py baseline**：本构建目录下直接报 8/8。KIT §6.9 记录的 build 6 时 0/8 为旧 scratch-es 布局下的收集盲区（工具只在 `--out/svg` 收集经“重定向”写出的 SVG，本构建输出为相对构建目录的 `svg/`），等价证据为直接 sha256 对比（build 6 时即为 8/8）。
- **C1 裁切比例**：`pdftoppm -r 200` 印版第 1 页为 4063×5625 px；SVG viewBox 为 1950×2700，故比例 k=2.0833——首次裁切用了错比例、切错区域；修正后裁切存为本 scratch `c1-box-crop-200dpi.png`。
- **P8 字号**：须用有效字号 `font_size*|tm[3]|`；不用 tm 比例的朴素 visitor 会误报 1.0pt。
- **keycheck_core.py**：进程内跑 run.py 前须先重置 `sys.argv=['run.py']`（run.py 从 `sys.argv[1:]` 取文件列表）。
- **build 9 build 10 两版 SVG 快照**：本 scratch `build7-svg/`、`build8-svg/`、`build9-svg/`（build 10 当前 `svg/` 即 build 10，无 `build10-svg/` 快照——当前 `svg/` 就是 build 10）；`freeze7/8/9/10/`、`run7/8/9/10.log`、`render7/8/9/10.log`、`occlusion7/8/9/10.json+log`、`p8-extract7/8/9/10.json`、`p8-compare7/8/8b/9/9b/10/10b.json`、`keycheck-150.json`、`keycheck-150-build9.json`、`creambox9/10.log`、`creambox_diag9/10.log`、`boxtitle9/10.log`、`text7.md`、`text8.md`、`text9.md`、`text7-shipped.md`、`text8-shipped.md`、`text9-shipped.md`、`text10.md`、`text10-export.log`、`tmp/print10.txt`、`tmp/web10.txt`。

## 7. 交付物

- 核心源码（已改）：`content12.py`（C1 盒高、C2、es-ja D1、D1/D2 订正 3 处、残留 (a)(b)）、`content8.py`（C2、残留 (b)）、`content7.py`（es-ja D4）、`content56.py`（es-pt C2 脚注、D1/D2 订正、残留 (b)）、`ABSTRACT.txt`（残留 (c)＋D2 订正）。
- 核心制品（build 10 最终）：`La-Lucerna-VOL4.pdf`（17,212,955 B，SHA `2723a283…138b5`）、`La-Lucerna-VOL4-web.pdf`（1,410,471 B，SHA `c2473211…235`）、`2026-w47-es-zh-cn.text.md`（1,822 行，SHA `509c95fa…8ddb`）、`svg/`（8 张，首 8 哈希见 §1）。
- KIT 已更新：`WEEKLY-KIT.md`（§2 P1／P6 行、§3 实测值、§5.2 辩论重写、§5.3 RTVE 分钟重写、§6 新增裁定 15–24、§7 build 10 命令与门、§8 返修轮次记录）。
- 本 FIX-LOG：`hidden_files/w47/scratch-fix-core-es1/FIX-LOG.md`。
- **未 commit、未 push。** 修后核心重校另派。
