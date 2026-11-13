# PROOF-NOTE-2 — W47 pt 家庭第二轮独立重校

- **校对员**：第二轮独立重校员（全新工人，与建造者、修复者均不同；SOP §8/§8.4）
- **日期**：2026-11-12
- **范围**：pt 家全部 11 版 — `core-pt`（pt-zh-cn）+ 10 fan-out（`2026-w47-pt-en/de/fr/es/it/ja/ko/nl/ru/zh-tw`），`~/workspace/weekly-git/production/2026-w47/` 内
- **依据**：SOP.md 全文（重点 §8）；第一轮结论 `scratch-reproof-w47-pt/PROOF-NOTE.md`；修复记录 `scratch-fix-pt/FIX-LOG.md`
- **方法**：只读生产文件，未改任何生产文件；未 commit/push，未跑 lint；解释器一律 `tools/venv/bin/python`
- **总体结论：干净（CLEAN）—— 本轮发现 0 条。**

## §1 修复核实（FIX-LOG 所称修复逐项在版）

### F1（P7 B2 讲解句主谓不一致）—— 4/4 确认在版
| 版 | 新形式（text.md 命中 1 / 旧形式 0） | P7 印 PDF 文字层 | SVG |
|---|---|---|---|
| pt-en | `take`（`quando, se, quem take the future`） | P7 第 83 行在版 | 在版 |
| pt-fr | `prennent`（`prennent le futur du`） | 在版 | 在版 |
| pt-es | `llevan`（`llevan el futuro de`） | 在版 | 在版 |
| pt-nl | `krijgen`（`krijgen de toekomende tijd`） | 在版 | 在版 |

- 11 版印 PDF SHA-256 前 12 位与 FIX-LOG 改后值逐一吻合；F1 四版 text.md md5 为改后值（en `ed59cccd8eab`、fr `596207ea7baa`、es `8f4657d0e9fb`、nl `6592eca08f2d`）。
- 印/网 PDF 文字层字节数差量恰好等于 F1 改动：en −1（takes→take）、fr +3（prend→prennent）、es +1（lleva→llevan）、nl +1（krijgt→krijgen）。
- de/it/ru 单数形式仍在原处未动（`steht danach im Futur` / `vuole il futuro` / `требует будущего`），与第一轮裁定一致。

### F2（ABSTRACT.txt 缺刊名）—— 5/5 确认在版，11 版全部合规
- 11 版 ABSTRACT.txt 的 `lucerna`（不区分大小写）计数全部为 1，均含 `VOL.4`、目标语、A2–B2、150 题；全文存 `toolout/abstracts.txt`。
- 改后开头示例：it `Il Settimanale portoghese di A Lucerna VOL.4: …`、ja `A Lucerna ポルトガル語週報 VOL.4：…`、ko `A Lucerna 포르투갈어 주간지 VOL.4: …`、nl `Het Portugese Weekblad van A Lucerna VOL.4: …`、ru `Португальский еженедельник A Lucerna VOL.4: …`。
- 字节级核查：11 版均无 U+FFFD、均单行、无 ASCII 双引号、`VOL.4` 恰出现 1 次（pt-ko 摘要先前终端显示的 `��` 为终端渲染伪影，文件字节干净）。

### 不重报项（按任务要求）
- **F3**（P2「D AS PALAVRAS」标题与内容分栏分离）：FIX-LOG 末节已裁定不修，不重报。
- **pt-ru 拉丁标题字体问题**（拉丁文用 Noto Sans 而非 Newsreader）：已知跨家 D5 系统性问题，另有跨家工人统一修 svglib.py，不重报。本轮按字体分列普查：西里尔文 0 落在 Newsreader 内（4736 字符在 Noto Sans、4010 字符在 Noto Serif CJK SC）；D5 全仓普查（`scratch-d5-census/D5-CENSUS-130.md` §2）已登记 pt-ru 拉丁 357 处 + 西里尔 255 处在 CJK Sans，属同一已知系统性问题，修法归跨家工人，不属 pt 家新发现。本轮自写 census 脚本的 `cyr_in_latin=4736` 是把 Noto Sans 划入“拉丁字体”所致的假阳性，已用分列普查纠正。

## §2 发现表

**无发现。** MAJOR 0、MEDIUM 0、low 0。

## §3 全量重读（core-pt text.md 535 行 + 印 PDF 全文）

- **题号**：1–150 连续无缺（脚本核实：150 项、min 1、max 150、缺失 []）。
- **日期/星期**（`TZ='America/Sao_Paulo' date -d` 实测）：11-01 周日、11-07 周六、11-08 周日、11-15 周日、11-16 周一、11-17 周二、11-18 周三、11-19 周四、11-20 周五、11-21 周六、11-22 周日、11-23 周一、11-27 周五、11-30 周一、12-06 周日——与正文全部表述一致。
- **事实（外部公开来源抽查，2026-11-12 检索）**：
  - Enem 2026：8 日与 15 日两个周日；第 1 天 13h30–19h、第 2 天 13h30–18h30、每天 90 题（45+45）；Edital nº 64/2026；官方答案至第 2 天后第 10 个工作日，窗口 11 月 27–30 日（取决于 20 日假日计法）；结果 2027 年 1 月中旬。来源：Inep edital 引文 + centerdrop / focaedu / estrategia 等多家一致。
  - 巴西杯半决赛：Grêmio 2–0 主场胜 Atlético-MG（11 月 1 日）+ 1–1 客场平（11 月 7 日 Arena MRV），总比分 3–1；Renan Lodi 首开纪录、Carlos Vinícius 扳平。Palmeiras 首回合 1–0 胜 Vasco，次回合客场 1–2 负（11 月 8 日 São Januário），总比分 2–2，点球 5–4 晋级。决赛 12 月 6 日 Mané Garrincha 单场。来源：noataque / infobotucatu / estacaolivremt / futebolinterior / Sportradar。
  - F1 圣保罗站 11 月 8 日：Norris 冠军、Verstappen 第 2、Hadjar 第 3，Mercedes 锁定车队冠军。来源：Formula1.com/FIA 官方赛报引文 + lance / flashscore / gazetaesportiva。
  - 法律：Lei 12.519/2011（2011 年 11 月 10 日）设纪念日、无假日；Lei 14.759/2023（2023 年 12 月 21 日）定为全国假日；Zumbi 卒于 1695-11-20；2026-11-20 为周五。来源：Planalto 法条引文 + afrocultura / TRF2。
  - Grêmio 争第 6 冠（此前 5 冠）、Palmeiras 争第 5 冠（此前 4 冠），与正文一致。
- **P6 算术**：16–30 日 = 15 天 = 10 工作日 + 5 周末/假日；第 2 天 13h30–18h30 = 5 小时；90 题；TRI 计分说明与正文一致。
- **配对题与答案**：Q25–28、Q52–55、Q141–144 与答案一致；E 节翻译 137–140 十版均准确（见 §4）。
- **8 句「Frases da semana」**：与正文逐字一致（逐句比对过），页码标注正确。
- **模型文**：实测 88 词；P7 读者来信披露 VOL.3 承诺未兑现、顺延至 VOL.5，与正文一致。

## §4 fan-out 全量 diff（10 版 vs core，`toolout/textmd-diff-vs-core.txt` 1646 行逐行读完）

- 差异行数对称：en 50/50、de/fr/es/it/ja/ko/nl/ru 各 51/51、zh-tw 48/48（`<`/`>` 行数相等，仅讲解层行不同）。
- 葡语核心层逐字节相同；所有差异行均为正确读者母语的讲解/翻译，无跨语言残留；E 节 137–140 十版均准确；zh-tw 为规范繁体（連假/週五/十二碼/價籤/獎盃/巴西盃），无简体残留。
- pt-nl 第 393 行已为修复后形式 `krijgen`；pt-ru 第 393 行单数 `требует`（第一轮裁定可辩，不重报）。

## §5 机械门禁（逐版结果）

| 门禁 | 结果（11 版） |
|---|---|
| p8.py compare --total 150 | 10 版全部 CLEAN，150/150，keydiff 仅 [137, 138]（合法翻译重定向） |
| occlusion_audit.py | 11 版全部 0 标记，自检通过 |
| boxtitle_check.py | rc=0；11 版 0 DEFECT、0 OBSERVE、0 marginal |
| spill_sweep.py | rc=0；11 版 0 SPILL（OBSERVE 项为候选计数，非缺陷） |
| pdf_edge_scan.py | rc=0；11 版 0 TOUCH、0 NEAR（每页最小边距 ≥53.6 pt） |
| D5 弯引号普查 | core 6、fr/it 各 5、其余 8 版各 4，全部在 Newsreader 内；`lat_in_cjk=0`、`cjk_in_latin=0` 全版 |
| 印/网 PDF 文字层 | 11 版逐版字节相等（zh-cn 44343、en 45957、de 47966、fr 47433、es 47061、it 46710、ja 47917、ko 47284、nl 47101、ru 54970、zh-tw 44534） |

### P8 答案 vs text.md「Respostas」比对（自写 `p8_vs_textmd.py`，`toolout/p8-vs-textmd.txt`）
- 11 版 P8 extract 均为 150 键，text.md Respostas 解析 143 项；表面不符每版 8 项，**全部为解析伪影，非真实差异**：
  - 7 项（#10、#28、#46、#64、#82、#100、#112）是 Respostas 页眉（`**Página N** —`）后首题被并入前一分块所致；印 PDF 文字层直接核实：`11. B`、`150. ✓` 等均在版。
  - #150：P8 键为 `✓`，text.md 附加范文指引（如 en `See the model text in section H of this page (88 words)`），属格式差异。
  - pt-ru 另有 #137：P8 extract 截断为 `Пятница, 20 ноября,`，印 PDF 文字层完整值为 `137. Пятница, 20 ноября, — национальный праздник.`——提取器在破折号处截断，非印刷缺陷；与 keydiff [137, 138] 的合法翻译重定向一致。
- **结论：P8 答案与 text.md 150/150 一致。**

### 逐版门禁总表
| 版 | p8 compare | occlusion | boxtitle | spill | edge | 弯引号（Newsreader 内） | 印/网文字层 |
|---|---|---|---|---|---|---|---|
| core-pt | — | 0 | 0 DEFECT | 0 SPILL | 0/0 | 6 | 相等 44343 |
| pt-en | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 4 | 相等 45957 |
| pt-de | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 4 | 相等 47966 |
| pt-fr | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 5 | 相等 47433 |
| pt-es | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 4 | 相等 47061 |
| pt-it | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 5 | 相等 46710 |
| pt-ja | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 4 | 相等 47917 |
| pt-ko | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 4 | 相等 47284 |
| pt-nl | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 4 | 相等 47101 |
| pt-ru | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 4 | 相等 54970 |
| pt-zh-tw | CLEAN | 0 | 0 DEFECT | 0 SPILL | 0/0 | 4 | 相等 44534 |

## §6 目检抽查（72 dpi 渲染，/tmp 渲染件已清理）

- **en/fr/es/nl P7**（F1 修复所在页）：修复句在版（`take` / `prennent` / `llevan` / `krijgen`），无溢出、无重叠、无压页脚。
- **core P1、P8**：刊头、头条、数字栏、快讯、闪电问答、P8 全部习题与答案区、88 词范文、Mané Garrincha 图注完整，无溢出/截断/豆腐块。
- **ru P7、P8**：俄语讲解层渲染正常，无豆腐块；P7 第 4 行金句俄文译文（`Без памяти нет будущего。`）完整可见于 `A PRÓXIMA SEMANA` 预告框之上——D5 遮挡修复有效；P8 答案区完整（含 137/138 俄文译文）。

## §7 备注（非发现，仅记录）

1. P6 称第 10 个工作日“entre 27 e 30 de novembro, conforme a contagem”：按正文所述计数（从 16 日起算、20 日假日不计）第 10 个工作日实为 11 月 30 日；27–30 为计法差异的宽泛表述。外部来源亦确认窗口取决于计法（有来源称 27 日、有来源称 30 日）。第一轮已接受，不构成错误。
2. pt-ko 1695 行用敬语 `돌아가셨어요` 描述 Zumbi 去世，可接受。
3. `CARTAS DOS LEITORES` 小节标题在全部 11 版（含 core）均无读者母语译文并列——模板层面统一行为，非单版缺陷。

## §8 收尾复核

- 校对期间生产文件未被改动：22 份印/网 PDF 的 SHA-256 前 12 位与开工 `toolout/inventory.txt` 逐一一致；11 份 text.md md5 全部一致。
- 磁盘：95G/150G（64%），未触 100G 门限。
- 本轮产出：`scratch-reproof2-w47-pt/` 下 `PROOF-NOTE-2.md`、`census.py`、`p8_vs_textmd.py`、`toolout/`（inventory、p8-compare150、occlusion、boxtitle/spill/edge 日志与 JSON、textmd-diff-vs-core、curly-census、textlayer、abstracts、p8-vs-textmd）。

## 总体结论

**干净。** F1 4/4、F2 5/5 修复均已核实在版；全量重读、fan-out diff、全部机械门禁、P8 答案比对、目检抽查、外部事实抽查均无新问题。pt 家 11 版通过第二轮独立重校。
