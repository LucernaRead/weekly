# GATE-LOG — W47 es-ko proof2（重建版独立复校）

- 对象：`production/2026-w47/2026-w47-es-ko/`；印刷 `La-Lucerna-VOL4-es-ko.pdf` 8,874,351 B
  SHA-256 `65e3a3993f2f315f9a89c316788f6f93ed79ef69212c4b32f08f52a9976cb0f7`；
  网页 `La-Lucerna-VOL4-es-ko-web.pdf` 1,237,415 B
  SHA-256 `54494cef95ba3a7b98dc70aba67bd8a5cd03676106f14b6c928f38f417715351`；
  `2026-w47-es-ko.text.md` 47,369 B（1,818 行）
  SHA-256 `f49dd7088c16f7a40c14618019a05800b45418be8a9a137c8f83ddb8554dbc3e`。
  动工前与收工后两次实测三 SHA 与任务书一致，方可开工 ✓。
- 核心 es 未变：core-es print `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`、
  web `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`、
  text.md `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`，
  与 KIT §8 所载 core build-10 三 SHA 逐一一致 ✓。另：整个 `production/2026-w47/`
  在本克隆中为 untracked（`??`），无已提交基线可 diff——核心未变以 SHA 比对 + freeze 为据。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` rc=0；scratch 真实写文件 ✓；
  `/dev/null` 存在；全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。
  解释器一律 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）。
- 工具来源：`tools/occlusion_audit.py`、`tools/p8.py`、`tools/freeze.py`（共享工具）；
  `creambox.py` / `creambox_diag.py` / `boxtitle.py` / `keycheck.py` / `reg_dump.py` /
  `freeze_direct_es.py` 复用自兄弟版 scratch `scratch-proof-es-ko1/`（复制到本 scratch，
  未改动原件；`freeze_direct_es.py` 为 es-ko 改写版，见 proof1 日志）；
  `keycheck_ast.py` 为本轮新写（见下 keycheck 节）；`sweep_de.py` 借自
  `scratch-fanout-es/`；`svgtext.py` / `cjk_audit2.py` 为本轮旧版比对与 CJK 分类脚本。
- KIT 所称 P8 最小字号 10.125pt：以 PyMuPDF 实测复核，印/网 P8 min 均为 10.125pt
  （与 KIT 一致），全版 min 分布见 logs-fontsize.txt（P1/P3/P5/P7 11.625pt；
  P2/P4/P6 12.75pt）。§1.1 阶梯：P8 10.125pt 低于 11.25pt 目标，
  在 SOP §1.1 让步链内（W46 众数 9.75pt；本版 10.125pt > 9.75pt 下限），不列缺陷。

## 机械门结果（实跑）

| 门 | 结果 |
|---|---|
| run.py（build-copy 中跑，生产文件只读） | rc=0，0 OVERFLOW / TOO WIDE，TOTAL 150（A2 50 / B1 72 / B2 28；按页 10/18/18/18/18/18/12/38）；P8-keys y=2506，P8-ex y=872；MODELO words 97 ✓ |
| occlusion 审计（正式，未加 --selftest；工具内置自检通过） | 0 flags ✓（`occlusion.json`，自检 6 类阳性全触发） |
| p8 extract | 150/150 ✓（`p8extract.json`） |
| p8 compare（vs core-es） | CLEAN，keydiff=[137, 138]（与 KIT §6.12 一致，翻译键重定向） ✓ |
| freeze baseline（`tools/freeze.py baseline`，build-copy 重跑） | 8/8 byte-identical ✓（core 侧 8 文件重哈希确认未变） |
| freeze diff（core-es → es-ko） | 新增 CJK 3,462 = 韩语音节 3,461 + U+3000 ×1，未入账 0；西班牙文本丢失仅 D-02 一处中文桥接句内术语（见缺陷） |
| freeze_direct（改写版 `freeze_direct_es.py`） | 渲染层 8/8 PASS（frozen 151/143/141/144/139/172/115/478，均 ≥100）；源码层严格精确匹配 FAIL，裁定见下 |
| creambox 严格口径（`creambox_diag.py`，框内末基线 vs 框底） | 27 框全部 clearance 为正，最小 +1.9（P3/P5 ¿Y TÚ? 框）；P7 工具盒（CARTAS）+5.7，与 KIT 数字一致 ✓（creambox.py 的 6 条 raw 负值均为下一框标题/框外图注落入窗口的伪影，已用严格口径排除；另 P1 两处 -999 为无文图框，见下） |
| boxtitle 全标题 text_w 实测 | 25 fit / 0 over；最紧 P5 "EL PLAN DE LA SEMANA　이번 주 계획" 403.8/404.5，余量 +0.7（通过，见观察 O-3） |
| 印/网文字层逐页比对 | pdftotext plain 各 48,324 B 字节一致；layout 版亦字节一致；逐页 8 页字符数逐页一致（4919/5567/4335/4686/4843/5337/5635/13002） ✓ |
| P8 最小字号实测 | 10.125pt（PyMuPDF，印/网一致），与 KIT 一致 ✓ |
| VOL 号 | VOL.4 ×9，VOL.5 ×3（均为下期预告正当引用），与 KIT 一致 ✓ |
| "12 de noviembre" | 0 处 ✓ |
| 三色蛾 title | 仅 P1 一处 ✓ |
| §1.1 字体/配色 | Newsreader 1519 / Noto Sans CJK SC 622 / Noto Serif CJK SC 621 / UnifrakturMaguntia ×1；纸色 #fbfaf6 8 页全有 ✓（与 proof1 的 1507/622/622/1 之差为重建文本重排的节点切分变化） |
| 日期星期（`date -d`，Europe/Madrid） | 11-13 周五、16 周一、17 周二、18 周三、19 周四、20 周五、21 周六、22 周日、23 周一、24 周二、27 周五、28 周六、29 周日，全部与版内一致 ✓ |
| 注释词计数（§8.1 口径，原始 SVG 计数复核） | P1 reflexión 2、P2 mitin/cartel/escaño 各 2、P3 cante 5/toque 6/baile 9/compás 4/duende 5、P4 parón 2/liderato 3、P5 censo 2——与 KIT §3 一致；P5 papeleta 实测 2（KIT 称 3）、plazo 实测 3（KIT 称 4），与 proof1 的两次独立计数一致。§8.1 门（每页 ≥2 次）对两词仍通过（2、3），属 KIT 记录数字误差，非内容缺陷（见观察 O-2） |
| 孤儿标点全扫（视觉行口径） | 独行 。 0 / 独行右引号 0 / 独行 ： 0 / 独行 – 0 ✓；但检出独行 `)` ×1（P1，D-03）与独行音节 `일)` ×1（P2，D-04），见缺陷清单 |

## freeze_direct 源码层裁定

严格工具报 `unaccounted removed: 5; unaccounted added: 128`，rc=1。逐项裁定：

- Removed 5 项：与 proof1 完全相同的 5 项——`La Lucerna　西班牙语周报 VOL.4　LUCERNA SPANISH WEEKLY`→韩文版页脚
  （harvest 仅有 VOL.3 版式，VOL.4 为透明改写）；`La-Lucerna-VOL4-web.pdf` /
  `La-Lucerna-VOL4.pdf`→`…-es-ko-web.pdf` / `…-es-ko.pdf`（slug 结构改名）；
  Marta 信全角括号→半角（KIT §6.9 已裁定）；`版／共`→` 면 / 총 `（韩文页码行家具）。
  5 项全部有出处，非内容改动。
- Added 128 项（proof1 为 126 项；+2 来自核心 build-10 的字面量变化，
  content12.py 字面量 367→370）：逐项拉丁词碎片检验——128 项中所含全部拉丁词
  （≥2 字母）均出现于 core-es 字面量中，**0 个 core 之外的拉丁词**（即无新增
  西班牙语文本）；新增内容均为韩文讲解、韩文注与 core 西班牙语片段的拼接
  （题干 + “(韩文注)”、P8 键 + 韩文注、框题 + 韩文副题）。
- 结论：freeze_direct 源码层按裁定 PASS（工具的严格精确匹配不适用于 es fan-out
  的拼接式字面量，见 `freeze-direct.json`）；渲染层 8/8 PASS。
- 附带：工具输出曾显示一处 `���`，系 exec 输出转码伪影，已用码位转储核实
  源文件该句为干净韩文 `모범 답안(97단어)은 아래에 있어요.`（content8.py），
  8 个 SVG / text.md / 印网 PDF 文字层中 U+FFFD 均为 0。

## 弯引号（U+201C/U+201D/U+2018/U+2019）节点级核查——D-01 已修复

- 按 <text> 节点字体逐个核查（en-ko1 口径：落入 CJK 字体节点才计数）。
- CJK 节点内弯引号 **0 个** ✓。P1 词汇注现为 ASCII `"토론"`，P5 C 节副标题
  现为 ASCII `'~할 것'`，P1/P5 卡片目视均为直引号。
- 仅存弯引号：P8 Q91 的两对（Newsreader 节点，西班牙语题干的韩文注
  `“제안된 것”이 “확정된 것”과 같지 않아요`），合格；text.md 中弯引号共 4 个，
  全部在 L1710（即 Q91 注），与 SVG 一致。
- D-02 未修复：见 PROOF-NOTE 缺陷 D-01（P8 #45 注残句仍在源码、SVG、text.md、
  印 PDF 四处）。

## hangul 宽度修复重验（任务书点名项）

- Exporter：修复版 `extract_text_es_ko.py` 重跑导出，与已发 text.md
  **字节一致**（`logs-export.txt`）。修复已生效。
- freeze baseline 8/8；freeze diff 新增 CJK 3,462 = 韩语音节 3,461 +
  全角空格 U+3000 ×1，未入账 0（`logs-cjk-audit.txt`）。
- 视觉行断行扫描（全 8 页，按 y±3 成行、x 间隙 >120 分栏）：
  独行 `。`/右引号/`：`/`–` 均为 0；P8 Q91 的两个 `”` 节点经坐标核实
  均在行中（y=1853.64，紧贴 `것` 之后、`이`/`과` 之前），非独行。
  但检出两处断行孤儿：P1 y=1414.5 独行 `)`（D-03）、P2 y=1113.4 独行音节
  `일)`（D-04）。两者在旧版 build 1 同一坐标已存在（proof1 框记录可佐证），
  重建未引入、亦未修复。
- 注意：节点级扫描曾报 122 个“单音节韩文节点”，经核查全部不是孤儿——
  其中 P8 注为渲染器按词分发的 <text> 节点（同基线多词成行）、P1/P2/P5
  为日历单元格（单格单音节，属设计），P8 三处视觉行单音节
  （`8면 La gran prueba…` 标题行、`54. a — liderato = 1위 a`、
  `35. baile — baile = 춤`）均为双语键行、内容完整，非换行尾行。
  真正的换行尾行孤儿只有 D-03、D-04 两处（视觉行口径）。

## creambox 逐盒裁定

- 严格口径（框内末基线 vs 框底）27 框：P1 +45.7 / +8.0 / +16.0 / +44.0；
  P2 +46.6 / +47.7 / +5.3 / +5.6；P3 +47.7 / +5.3 / +1.9；P4 +47.7 / +110.8 / +5.7；
  P5 +46.6 / +47.7 / +5.4 / +1.9；P6 +55.7 / +19.4 / +35.2 / +35.2；
  P7 +42.5 / +26.5 / +5.7。最小 +1.9（P3/P5 ¿Y TÚ? 框），全部为正。
- P1 两处 STRICT -999（x=88 y=1874、x=362 y=1999）为无文图框（插图区），
  框内无文本节点；图注文字在框底之外（y=2218 起），属版式设计，与 proof1
  完全相同，非溢出。
- creambox.py 6 条 raw 负值：P1 四条（AHORA TÚ / EN ESTA EDICIÓN /
  LA PALABRA / urna 图注）、P2 一条（DECIR LA HORA）、P3 一条
  （LO QUE QUEDA DE NOVIEMBRE）——均为下一框标题或框外图注落入 +45 窗口
  的伪影（KIT §8 已注“6 raw negative lines per edition are the known
  below-box headings, identical to core”），严格口径已排除。

## keycheck（150 题三源一致）

- 源码 REG：`reg_dump.py`（AST 提取）按源码顺序提取 Q1–150（见 `logs-regdump.txt`），
  TOTAL 150。
- import 式 `keycheck.py` 在本 scratch 跑不通：其借来的 `stub_bslib`（de 向）
  缺少 `illus_voto`（content12.py:123 调用，定义在 svglib.py:353）。
  改用 AST 版 `keycheck_ast.py`（同一比对逻辑：源码 REG 键 vs p8extract 键，
  不执行 content 文件），结果写入 `keycheck-150.json`。
- 结果：exact match **149/150**，唯一差异为 Q150（开放写作题，REG 键
  `(열린 문제 — 모범 답안은 아래에 있어요)`，P8 印 `✓`，属预期），rc=0。
- 逐题语义手验（REG 150 行逐行读过，结合 P8 键与正文）：
  Q1–6 日期键 13/29/19/16/20/15 全对；Q7–10 选项键 C/B/A/B 全对；
  Q11–20 填空键（16/19/29/22/noviembre/empieza/dura/vuelve/recorren/llega）全对；
  Q21–24 B/A/C/B 全对；匹配题 25–28（c/b/d/a）、52–55（c/b/a/d）、141–144
  （c/d/b/a）对照 SVG 选项原文逐一核实，定义与键一致；
  Q29–33 判断题（V/V/F/F/V）与正文一致；Q34–38（cante/baile/guitarra/palmas/
  compás）全对；Q39–42（B/A/C/B）全对；Q43–46 造句键全对；
  Q47–51（A/B/C/A/B）全对；Q56–59（más importante/muchísimos/peor/mejor）全对；
  Q60–64 过去时（ganó/recibió/perdió/volvió/cerró）全对；
  Q65–69（B/A/C/B/A）全对；Q70–75（correo/papeleta/envío/identidad/censo/plazo）全对；
  Q76–79（ir a + 不定式）全对；Q80–82（V/F/V）全对；
  Q83–92（A/B/C/A/B/C/B/A/C/B）全对，其中 Q87 45−30=15、Q89 唯一已确认辩论为
  laSexta 场、Q91 «propuesto»=尚未确认；Q93–100（tenga/sea/para que/Aunque/
  sondeo/muestra/indecisos/margen de error）全对；
  Q101–104（Es/Son/las/B）全对；Q105–108（más goles/tan rápido/mejor/B）全对；
  Q109–112（baje/sea/es/B）全对；Q113–120（A/B/A/A/A/B/A/A）全对；
  Q121–128（A/B/A/C/B/C/B/C）全对；Q129–132 对照 P8 C 阅读段（Lucía 在塞维利亚
  看德比、Diego 在马德里看 Madrid–Celta、两人都读纲领、标题«Dos ciudades,
  un sábado»）键 A/A/A/B 全对；Q133–136 造句键全对；Q137/138 韩文翻译键
  （已裁定的重定向键）与 Q139（hasta el jueves 19，C2 改动已同步）Q140 全对；
  Q145–149 对话填空（votar/identidad/urna/sobre/cierra）全对；Q150 开放写作题。
  **150 题键无一错误。** P8 韩文注逐条读过，仅 #45 一处残句（见缺陷 D-01）；
  其余注均完整准确（含 #32/#92/#140 的 §6.11 缩短版，事实完整）。

## 外部事实核实（本轮网上复核，针对重建新增改动项）

- RTVE Debate a 8：Europa Press 2026-10-05（经 noticiasde.es）：RTVE 提案含
  “debate con los portavoces parlamentarios, propuesto prioritariamente para
  el lunes 23 de noviembre”，八个议会党团（Popular, Socialista, Vox, Sumar,
  Republicano, Junts, EH Bildu, Vasco）；canariasenpleno / diariosabemos
  （2026-11-05）同证“Debate a 8 el 23”。版内“RTVE propone un debate a ocho,
  con los portavoces de los ocho grupos, para el lunes 23”准确，
  “propone”与提案性质相符 ✓。
- Academia 协议：RTVE Noticias / Demócrata / elFolio 2026-11-09：PSOE 与 PP
  于 11 月 9 日周一达成由 Academia de Televisión 组织两场辩论（面对面 +
  四方辩论）；PP 提议 16 日面对面、26 日四方辩论；日期/时间/人选
  “siguen sin cerrarse”。版内“el lunes 9, PSOE y PP acuerdan que la Academia
  de Televisión organice los dos debates, pero las fechas, las horas y los
  participantes siguen sin cerrarse”逐字相符 ✓。
- 面对面“两党接受邀约但未公布时间”：多源 2026-11-09/10 证实双方已接受
  Mediaset 11 月 16 日面对面；截稿时无公开时间；版内已注
  “esta página no da por cerrado lo que aún se negocia” ✓。
- 其余核心事实未改动，沿 proof1 的网上复核结论（29-N 大选、La Liga J13/J12、
  欧冠 J5/J4、弗拉门戈、Santa Cecilia、MiDNI、RTVE 195 分钟）；本轮全文
  重读未发现新的事实出入。

## 旧版逐页对比（SVG 文本节点 diff，旧版取 proof1 freeze build-copy SVG）

- P1：变化 10 行——PSOE 面对面句改写、C2 antes→hasta ×4、D-01 弯引号→ASCII、
  A2→B2 标记随重排移动。余无变化。
- P2：变化 5 行——PSOE 句改写、C2 ×2。余无变化。
- P3：0 行变化。P4：0 行变化。
- P5：变化 2 行——D-01 P5 弯引号→ASCII（`‘~할 것’이라…` → `'~할 것'이라는…`）。
- P6：节点 176→189，变化 39 行——SER 段前移 + 未公布时间从句、Academia 协议句、
  RTVE 八方辩论行 INSERT、26 NOV 行加 `de la Academia`、JEC 行加
  `Acuerdo ... del 4 de noviembre`。全部为核心 build-10 改动，无意外变化。
- P7：变化 1 行——derbi viernes→sábado（D4）。
- P8：变化 6 行——C2 ×3（含韩文注 `19일 전에 → 19일까지`，节点 1379→1377
  系 `일/전에` 并为 `일까지`）、#116/#139 键同步 C2。
- 文字层 diff（新旧 print-plain，252 行）逐行核对：除上述记录项与纯重排外
  无意外变化。

## 全文复读与 8 页目视（完成）

- text.md 1–1818 行全文通读：P1–P8 内容、日期、数字、韩文注、图注、页脚全部读过；
  无国际政治内容（仅西班牙国内选举）；P7 FRASES 8 句逐句与正文核对，逐字一致，
  韩文译准确（#8 保留 §6.11 前的长式译文）；P8 C 阅读段与题 129–132 一致；
  H 范文手数 97 词（与 run.py 及版内 “97 단어” 一致），覆盖 lunes 16、viernes 20、
  voto del 29。
- 8 页目视：cards/*.png（1950×2700）逐页读过。除 D-03、D-04 两处断行孤儿外，
  无溢出、无重叠、无页脚侵入；P6 图表条长与分钟数成比例（45/45 等长、30/30
  等长、15 短；5/15/1 成比例）；P1 插图为编辑部线描并注明非照片；
  P3/P5/P7 图注均有 PD 来源；P5 框题单行容纳（目视与 +0.7 余量一致）；
  P4 D 节标题 `EL PRETÉRITO INDEFINIDO` 在桥接句正上方（见缺陷 D-02 的缓解）。

## 结论

- 缺陷 4 项，均为轻微（minor）：D-01（P8 #45 韩文注残句，proof1 D-02 未修复）、
  D-02（P4 桥接句丢 `(pretérito indefinido)`）、D-03（P1 数字框独行 `)`）、
  D-04（P2 日历框独行音节 `일)`）。其余机械门、150 题键、外部事实（新增项）、
  8 页目视（除两处断行孤儿外）、旧版对比全部通过。
- 未修改任何源文件，未重建，未 commit，未 push。交付：本日志 + PROOF-NOTE.md。
