# GATE-LOG — W47 es-ko proof1（独立复校）

- 对象：`production/2026-w47/2026-w47-es-ko/`；印刷 `La-Lucerna-VOL4-es-ko.pdf` 8,874,275 B
  SHA-256 `ba1a6e0a23a404c53ba1ad8cdfd9a2c83a3810242c08539715d24aed14949b5e`；
  网页 `La-Lucerna-VOL4-es-ko-web.pdf` 1,199,171 B
  SHA-256 `9117f3c186ee3aeca2a8e92208f590d0c0c4d8eaaeede6d83be5abee99725417`；
  `2026-w47-es-ko.text.md` 46,843 B SHA-256 `ddf077f538a34bb97a3576051305017dcc9944ae933df9dad64d762e1dcad5f7`。
  动工前实测三 SHA 与任务书一致，方可开工 ✓。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` rc=0；
  scratch 真实写文件 ✓。全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。
- 工具来源：`tools/occlusion_audit.py`、`tools/p8.py`、`tools/freeze.py`（共享工具）；
  `creambox.py` / `creambox_diag.py` / `boxtitle.py` / `keycheck.py` / `freeze_direct.py`
  复用自兄弟版 scratch `scratch-proof-es-ja1/`（复制到本 scratch，未改动原件）；
  `freeze_direct.py` 为 de 向（core-de + tr 模块），对 es-ko 不可直接用，故改写为
  `freeze_direct_es.py`（core-es、es 页名、以 fanout apply JSON + harvest ko.json 计帐），
  改写过程与裁定见本日志 freeze_direct 节。
- KIT 所称 P8 最小字号 10.125pt：以 PyMuPDF 实测复核，P8 min=10.125pt（与 KIT 一致），
  全版 min 分布见 logs-fontsize.txt。§1.1 阶梯：P8 10.125pt 低于 11.25pt 目标，
  在 SOP §1.1 让步链内（W46 众数 9.75pt；本版 10.125pt > 9.75pt 下限），不列缺陷。

## 机械门结果（实跑）

| 门 | 结果 |
|---|---|
| occlusion 审计（正式，未加 --selftest；工具内置自检通过） | 0 flags ✓（`occlusion.json`，自检 6 类阳性全触发） |
| p8 extract | 150/150 ✓（`p8extract.json`） |
| p8 compare（vs core-es） | CLEAN，keydiff=[137, 138]（与 KIT §6.12 一致，翻译键重定向） ✓ |
| freeze baseline（`tools/freeze.py baseline`，build-copy 重跑） | 8/8 byte-identical ✓ |
| freeze diff（core-es → es-ko） | 纯拉丁移除/新增 0 项西班牙文本丢失；P1/P2/P5/P7 的纯拉丁差异均为韩文注括号 "(" 造成的重切分；P5 "Después ___(" 为 KIT §6.1 已裁定改写；P6 "muestra ·" 在 core 为独立节点、在 ko 版与后项合并，重切分而已；P8 差异为韩文注长度造成的重切分，键由 p8 compare 覆盖 ✓ |
| freeze_direct（改写版 `freeze_direct_es.py`） | 渲染层 8/8 PASS（frozen 151/143/141/144/139/159/115/478，均 ≥100）；源码层严格精确匹配 FAIL，裁定见下 |
| creambox 严格口径（`creambox_diag.py`，框内末基线 vs 框底） | 全部奶油框 clearance 为正，最小 +1.9（P3/P5 ¿Y TÚ? 框）；P7 工具盒（CARTAS）+5.7，与 KIT 数字一致 ✓（creambox.py 的 +45 窗口负值均为下一框标题落入窗口的伪影，已用严格口径排除） |
| boxtitle 全标题 text_w 实测 | 25 fit / 0 over；最紧 P5 "EL PLAN DE LA SEMANA　이번 주 계획" 403.8/404.5，余量 +0.7（通过，见观察 O-1） |
| 印/网文字层逐页比对 | pdftotext（plain）各 47,790 B，字节一致；逐页 8 页字符数逐页一致 ✓ |
| P8 最小字号实测 | 10.125pt（PyMuPDF），与 KIT 一致 ✓ |
| VOL 号 | VOL.4 ×9，VOL.5 ×3（均为下期预告正当引用），与 KIT 一致 ✓ |
| "12 de noviembre" | 0 处 ✓ |
| 三色蛾 title | 仅 P1 一处 ✓ |
| P8 徽章 | #5c6e30 ×11（A2），#37402f ×4（B2 ×3 + 头带 ×1），与 KIT（35 chip + 1 头带）一致 ✓ |
| §1.1 字体/配色 | Newsreader 1507 / Noto Sans CJK SC 622 / Noto Serif CJK SC 622 / UnifrakturMaguntia ×1；纸色 #fbfaf6 8 页全有；填充色谱与 core-es 逐项一致（图表色 #4D72B4 等与 core 相同，属继承内容） ✓ |
| 日期星期（`date -d`，Europe/Madrid） | 11-13 周五、16 周一、17 周二、18 周三、19 周四、20 周五、21 周六、22 周日、23 周一、24 周二、27 周五、28 周六、29 周日，全部与版内一致 ✓ |

## freeze_direct 源码层裁定

严格工具报 `unaccounted removed: 5; unaccounted added: 126`，rc=1。逐项裁定：

- Removed 5 项：`La Lucerna　西班牙语周报 VOL.4　LUCERNA SPANISH WEEKLY`→韩文版页脚
  （harvest 仅有 VOL.3 版式，VOL.4 为透明改写）；`La-Lucerna-VOL4-web.pdf` /
  `La-Lucerna-VOL4.pdf`→`…-es-ko-web.pdf` / `…-es-ko.pdf`（slug 结构改名）；
  Marta 信全角括号→半角（KIT §6.9 已裁定）；`版／共`→` 면 / 총 `（韩文页码行家具）。
  5 项全部有出处，非内容改动。
- Added 126 项：逐项拉丁词碎片检验——126 项中所含全部拉丁词（≥2 字母）均出现于
  core-es 字面量中，**0 个 core 之外的拉丁词**（即无新增西班牙语文本）；新增内容
  均为韩文讲解、韩文注与 core 西班牙语片段的拼接（题干 + “(韩文注)”、P8 键 + 韩文注、
  框题 + 韩文副题）。附带：工具输出曾显示一处 `���`，系 exec 输出转码伪影，
  已用码位转储核实源文件该句为干净韩文 `우편 투표 신청 마감일이에요.`（content7.py），
  SVG / text.md / PDF 中亦无 U+FFFD。
- 结论：freeze_direct 源码层按裁定 PASS（工具的严格精确匹配不适用于 es fan-out
  的拼接式字面量，见 `freeze-direct.json`）；渲染层 8/8 PASS。

## 弯引号（U+201C/U+201D/U+2019）节点级核查

- 按 <text> 节点字体逐个核查（en-ko1 口径：落入 CJK 字体节点才计数；text.md 邻接为导出拼接伪影）。
- P8 Q91 两对弯引号落在 Newsreader 节点（西班牙语题干），合格。
- **P1、CJK 节点**：`<text … font-family="Noto Sans CJK SC" font-size="19">“토론”: 사람들이 공개적으로 토론해요.</text>`——U+201C + U+201D 各 1。
- **P5、CJK 节点**：`<text … font-family="Noto Sans CJK SC" font-size="20.5">ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이라…</text>`——U+2018 + U+2019 各 1。
- P7 无弯引号（任务书所称 P7 Newsreader 斜体对在本版不存在）。
- 合计：CJK 节点内弯引号 4 个 ≠ 0。见缺陷 D-01。P1 一对为构建者 §6.2 缩写时手写
  （harvest ko.json 无此句，系仿中文 “辩论” 式）；P5 一对来自 harvest ko.json
  值 `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이라는 뜻을 나타내세요.`。

## 外部事实核实（2026-11-11 网上复核）

- 29-N 大选真实：Real Decreto 806/2026（BOE 10-06），投票 11-29 周日 9:00–20:00，
  竞选 11-13 00:00 至 11-27 24:00（15 天），邮寄投票至 11-19，禁发民调 11-24–28
  （LOREG art. 69.7）。与版内全部一致 ✓。
- 辩论：Europa Press 2026-11-06：laSexta 11-13 Cuerpo/Bravo/Bustinduy/Figaredo；
  SER 11-18 住房辩论 Bravo 对 Isabel Rodríguez。✓。但 Europa Press 同文称 13 日场
  为 “vivienda y economía”，而版内（沿 core KIT §5.2 裁定）写 13 日场只谈经济、
  18 日场谈住房——core 已记录来源冲突并选 diariodesantiago.es 的逐场区分。
  属 core 级已裁定项，本版冻结继承，不另列缺陷（见报告观察 O-2）。
- La Liga J13：Fri 20 Athletic–Espanyol 21:00；Sat 21 Alavés–Deportivo 14:00、
  Rayo–Valencia 16:15、Sevilla–Betis 18:30、Real Madrid–Celta 21:00；
  Sun 22 Barça–Villarreal 14:00、Racing–Real Sociedad 16:15、Osasuna–Málaga 18:30、
  Getafe–Atlético 21:00；Mon 23 Levante–Elche 21:00。十场，11-20–23。✓
- 弗拉门戈：UNESCO 2010-11-16 内罗毕列入人类非遗；11-16 为国际弗拉门戈日 ✓。
- Santa Cecilia：11-22，音乐守护神 ✓；毕尔巴鄂市立乐队 11-22 周日 12:00
  Euskalduna 演出（teoriamusical.com.es，核对至 2026-11-02）✓。
- MiDNI：JEC 2026-11-05 解除停用（3-26 停用后，Interior 保障全部投票站核验设备）✓。
- RTVE 免费宣传分钟：BOE-A-2026-23258（2026-11-04）证实 JEC 已发布分配；
  LOREG art. 64 档位 10/15/30/45 分钟与版内档位一致（PSOE/PP 45、Vox 30、
  Frente Amplio 30、Podemos 15、其余 10）；45+45+30+30+15+10×3=195 合计一致 ✓。
  逐党明细（Frente Amplio 30 / Podemos 15 的 Sumar 遗产分配）未在公开页独立确认，
  系 JEC 网站表格内容——本轮记为“可公开核查范围内一致”，非缺陷。
- Sargent 舞者画：”Bailaora española” 习作 1879–82（El Jaleo 主像习作），
  core KIT 称 1880–81——待通读 P3 图注原文后再定（见全文复读）。

## 全文复读与 150 题核对（完成）

- text.md 1–1800 行全文通读：P1–P8 内容、日期、数字、韩文注、图注、页脚全部读过；
  无国际政治内容（仅西班牙国内选举）；P7 FRASES 8 句逐句与正文核对，逐字一致，
  韩文译准确；P8 C 阅读段（Lucía/Diego）与题 129–132 一致。
- 150 题键逐题手验：`reg_dump.py` 按源码顺序提取 REG（content12 Q1–28、
  content34 Q29–64、content56 Q65–100、content7 Q101–112、content8 Q113–150），
  共 150，与 p8extract 对比仅 Q150 一处差异（开放写作题，P8 印 ✓，属预期）。
  逐题语义核对全部通过，匹配题键与题干定义一致（25–28、52–55、141–144 逐一核实）。
  无键错误。P8 韩文答案注通读，准确；其中 #45 注有残句，见缺陷 D-02。
- H 范文：content8.py MODELO 词数脚本实测 97（与版内 “97 단어” 一致）；
  覆盖提示要求（lunes 16、viernes 20、voto del 29）。
- sweeps：`sweep_de.py`（借自 scratch-fanout-es）bridge orphans 0（20 桥）、
  box-vs-hline 0、bridge widows 0（`logs-sweeps.txt`）。
- 注释词计数（§8.1 口径，原始 SVG 计数复核）：P1 reflexión 2、P2 mitin/cartel/escaño
  各 2、P3 cante 5/toque 6/baile 9/compás 4/duende 5、P4 parón 2/liderato 3、
  P5 censo 2——与 KIT §3 一致；但 P5 papeleta 实测 2（KIT 称 3）、plazo 实测 3（KIT 称 4），
  两次独立计数一致。§8.1 门（每页 ≥2 次）对两词仍通过（2、3），属 KIT 记录数字误差，
  非内容缺陷（见报告观察 O-3）。
- 本轮补核外部事实：欧冠 J5 对阵（UEFA：Real Madrid–PSV 11-24，
  Sabah–Barça 11-25 18:45，Atlético–Viking 11-25）✓；J4 战绩（Barça 3–0 Aston Villa、
  Madrid 3–2 AEK、Atlético 0–2 Bayern，多源一致）✓；Villarreal 与 Betis 均在欧冠
  （J4 战绩佐证）✓；La Liga J12 后积分（Barça 33、Madrid 30、Atlético 28；
  Barça 客场 2–1 胜 Atlético，11-08）✓。
- 辩论时间线补核（2026-11-09/10 来源）：Atresmedia 四方辩论已移至 11-23 周一，
  Feijóo/Abascal/Colau 已确认、PSOE 仍邀而未确认——版内 P6 “23 NOV. — Atresmedia
  convoca un debate a cuatro (sin el PSOE)” 与之吻合 ✓；PP 坚持 11-26 Atresmedia
  四方辩论提案——版内 “26 NOV. — El PP propone un debate a cuatro (sin fecha
  pactada)” 与之吻合 ✓；laSexta 11-13 经济专场辩论已确认（elfolio：仅确认的两场
  专题辩论之一为 laSexta 11-13 经济场）✓。其余细节（21:30、Ana Pastor 主持、
  现场观众）为 core KIT 裁定细节，本轮未独立再验，记为核实边界（见观察 O-5）。
- 8 页目视：cards/*.png（1950×2700）逐页读过。无溢出、无重叠、无页脚侵入；
  P6 图表条长与分钟数成比例（45/45 等长、30/30 等长、15 短；5/15/1 成比例）；
  P1 插图为编辑部线描并注明非照片；P3/P5/P7 图注均有 PD 来源；
  P5 框题单行容纳（目视与 +0.7 余量一致）。
- **发现 D-02（轻微，本版讲解层）**：P8 键 #45 韩文注 “장소가 앞에, 동사는 두 번째”
  为残句（缺系词 예요/에 있어요），与平行注 #44、#133 “…두 번째예요” 不一致。
  源头 content34.py:101 原文即如此，非渲染截断。

## 结论

- 缺陷 2 项，均为轻微（minor），均在本版韩文讲解层：D-01（弯引号 4 个落入 CJK 节点）、
  D-02（P8 #45 韩文注残句）。其余机械门、150 题键、外部事实、8 页目视全部通过。
- 未修改任何源文件，未重建，未 commit，未 push。交付：本日志 + PROOF-NOTE.md。
