# GATE-LOG — 2026-W47 ru → pt (proof1)

复校员：独立 proof1（subagent）。源文件未改动、未重建、未 commit、未 push。
工作目录：`~/workspace/weekly-git`；版目录 `production/2026-w47/2026-w47-ru-pt/`；scratch
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-pt1/`。
工具 venv：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，已验证一致）。`TMPDIR` 全程指向 scratch 下 `tmp/`。

## §0 身份核对（磁盘实测，与任务一致）

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；探针文件写于 `<scratch>/probe.txt`。✓
- 印 PDF `Lucerna-VOL4-ru-pt.pdf`：SHA `e6171dabf8d871619b75a45c691ffbf41cd994bf1ef597ad6907294b6f26ff88`，21,199,772 字节。✓ 与任务一致。
- 网 PDF `Lucerna-VOL4-ru-pt-web.pdf`：SHA `cc8fea68fcf0c8292cae4f73ee0ed23c2facacae1d34e77f9fdd1b2d995323ce`，3,344,677 字节。✓ 与任务一致。
- text.md `2026-w47-ru-pt.text.md`：SHA `7e785cc00f4d48821bb7736d000bbcb491974525477a03a3772890229dcd021e`，65,098 字节，838 行。✓ 与任务一致。

## §1 occlusion 审计

- 自测（`logs/occlusion-selftest.log`）：6 类 planted 缺陷全部触发，干净对照静默。✓
- 本版（`logs/occlusion.log/.json`）：**42 TEXTX，0 COVER / 0 LINEX / 0 FOOTER / 0 EDGE / 0 BOXTITLE**。
- 核心 core-ru 同跑（`logs/occlusion-core.log/.json`）：亦为 42 TEXTX；38 处与本版完全相同，4 处几何相同、仅翻译后家具标签不同（P6 `? DADOS DE PRÁTICA` vs `?`；P7 `LÍNGUA` vs `语言`；P8 `TESTE E RESPOSTAS` / `RESPOSTAS — …` vs 中文对应）。
- 目检 3 处：P8 带 `ОТВЕТЫ / TESTE E RESPOSTAS` 清晰分离；P1 标题 `«Зенит»` 的 `»` 间隙正常；其余均为相邻 run 包围盒假阳性。
- **判定：CLEAR，非缺陷**（继承核心几何）。注：occlusion 对奶油框内溢出、框标题溢出、横向溢出、降部溢出是盲的 —— 均已另行实测（§2、§6）。

## §2 正典 creambox 扫描（+45 px 窗口 + 逐行 clearance）

- 全版 32 盒（`logs/creambox.log`）。全部负 clearance 盒均为窗口下方标题（+28..+37 px），假阳性。
- **P2 盒**（§2 必查 (b)）：y=795，bottom=1159.0，末行基线 1154.0（`para o Avô Gelo.`），clearance +5.0，desc-clear −1.0（基线算法）。
  PIL 真墨实测（NotoSansCJK-Regular TTC idx 2 与 Newsreader 双验）：墨底 = 基线 +5 px = 1158.98；
  渲染 card 像素扫描：最末深色行 y=1158，≥1159 无墨；3× 放大裁切（`crop-p2-boxbottom.png`）确认 `p` 降部在框内。
  **判定：非缺陷，余量仅 0.02 px**（见 PROOF-NOTE O3）。
- **P7 toolbox**（必查 (c)）：3 盒，最小 inside clearance +11.9，最小 desc-clear +5.9。**通过**。
- P7 另两盒（词框、读者来信框）desc-clear 分别 +5.9 / +17.3，框内无漫出。

## §3 p8 compare（显式 --core-p8 / --edition-p8）

- `logs/p8-compare.log/.json`：**CLEAN**，noted 150/150 双侧，missing=[]，extra_count=0，uncertain=[]，
  keydiff = **[137, 138, 139, 140]** —— 四条 E 节 RU→PT 翻译键，已逐一核实为正确翻译（见 §7）。无缺失/多余。

## §4 freeze

- `freeze.py baseline`（core-ru，`logs/freeze-baseline.log`）：**8/8 SVG 字节一致**；核心完整性重哈希 OK。
- `freeze.py diff`（`logs/freeze-diff.log/.json`，--core-svg 指到 `core-ru/svg`）：
  新增 CJK 仅 U+3000（全角空格）×6（P1–P5、P8 各 1，P6–P7 为 0）；
  P1–P5 西里尔 run 序列一致；
  P6/P7/P8 差异仅为讲解层翻译，葡语对应均在 diff 中找到（P6 图表标签 `УЧЕБНЫЕ ДАННЫЕ` + 实践数据披露 → `DADOS DE PRÁTICA` + 葡语句；
  P7 `Три уровня три темы` → `Três níveis, três temas`；P8 `Большой тест недели все ответы` → `O grande teste da semana + todas as respostas`；
  另 P8 Morozko 图注差因构建条件跳过该图，与 W46 ru-pt 一致）。**无新增西里尔串不在核心中。**
- **本版重建**（`logs/freeze-rebuild-edition.log`）：将版目录复制到 scratch，在副本内跑 `run.py`（content12/34/56/7/8），
  重建的 8 个 SVG 与 shipped **8/8 字节一致**；registry TOTAL 150（按页 10+18+18+18+18+18+12+38；按类型 Completar 54、Escolha 55、Associação 20、Construção 12、Transformação 4、Tradução 4、Escrita 1）。
- 方法备注：`tools/freeze.py` 无 `freeze_direct` 子命令（仅 baseline/diff），按任务要求记为方法备注，**非缺陷**。

## §5 keycheck 150/150

- `p8.py extract`（本版 P8，`logs/p8-extract.log/.json`）：noted set 150/150。
- P8 印出键 vs text.md Answers：**149/150 形式一致**；唯一 Q150 形式不同（P8 印 `✓`，text.md 给开放题说明 —— 与核心一致）。
- text.md Answers §（行 670 起）解析 150 条；题干内联键 129 处全部与 Answers 一致；21 处无内联键者为 5 个匹配组（20 题）+ Q150，符合预期。
- 5 个匹配组逐一对照 SVG 选项表核实：
  P2-D（a=День психолога，b=Международный день студента，c=Всемирный день ребёнка，d=день рождения Деда Мороза；25=b，26=d，27=c，28=a ✓）；
  P3-C（a=зритель，b=биография，c=сеанс，d=документальный；39=b，40=d，41=c，42=a ✓）；
  P4-C（a=Краснодар胜ЦСКА 4:2，b=Локомотив负 0:1，c=Спартак胜Акрон 2:1，d=Зенит平Ростов 2:2；57=b，58=a，59=c，60=d ✓）；
  P5-C（a=промокод，b=возврат，c=скидка，d=распродажа；75=d，76=b，77=a，78=c ✓）；
  P8-F（a=счёт，b=гололедица，c=оттепель，d=распродажа；141=c，142=d，143=a，144=b ✓）。
- 其余全部逐题对照正文语义核实（详见 `keycheck-150.json` 逐题 `verification_basis`）。
- **唯一 FAIL：Q20**（D6，见 PROOF-NOTE）。逐题记录：`keycheck-150.json`（150 条，pass 149，fail 1）。

## §6 横向溢出（boxtitle / 全版实测）

文本区 1950×2700 px，边距 88 px，**右文本边 = 1862 px**。方法：PIL 墨水全扫（8 个 SVG）+
PDF span + 200 dpi 像素扫描（shipped card 与印 PDF 新渲染双份）。关键发现：**Cairo PNG 与 PDF 对两行相差可达 ~9 px**
（P1 `Segundo…` 行：card 1866 vs PDF 渲染 1859 / span 1860.9 / PIL 1860.5；P1 桥接行：card 1856 vs PDF 渲染 1865 / span 1866.9 / PIL 墨 1862.5）。
CairoSVG 新渲染当前 p1 SVG 与 shipped card 完全一致（1888/1864/1866/1856），故 card 对 SVG 忠实；**PDF 为交付件，以 PDF 为准**，span + PIL + MuPDF 渲染在两行上一致地反对 card。

- D1：P1 `A PALAVRA DA SEMANA`（y=1660，bold 22，x=1617.5）：PDF 渲染 1886、span 1887.5、PIL 1886.5、card 1888 → **+24~26 px**（`logs/pdf-render-global.log`、`logs/ink-sweep.log`、`crop-p1-palavra.png`）。
- D2：P1 桥接行（y=2348）：PDF 渲染 1865（+3）、span 1866.9（+4.9）、PIL 1862.5（+0.5）、card 1856。
- D3：P2–P6 页脚说明行（P2 y=1876，P3/P5 y=1648，P4 y=1939.3，P6 y=1866）：五页 PDF 渲染均为 1864（+2）；span advance 1866.5；PIL 1862.3；card ≤1862。
- D4：P2 选项 b `Международный день студента`（y=2162，size 23）：PDF 渲染 1868（+6）、span 1870.0、PIL 1867.7、card 1870；核心 core-ru 印 PDF 同一 span x1=1402.5 pt（`logs/core-pdf-spans.log`），几何一致 —— 核心继承。
- D5：P8 说明行（y=1302）：PDF 渲染 1864（+2）、span advance 1865.9。
- 贴边/已清：P1 `O QUE DIZEM OS MEDIA`——span +1.5、PIL +2.4、card +2，**PDF 渲染恰为 1862**（±2 px 光栅抖动内，不计缺陷）；
  P1 `Segundo os media russos, novembro de 2026`——span/PIL/PDF 渲染 ≤1861，仅 card 1866（渲染器分歧）；
  P2 `Quatro palavras sobre o tempo de novembro`——仅 span advance +2.1，PDF 渲染 ≤1862；
  P1 `ГОДА` 顶条与全部页脚（`Página N de 8`，PDF 渲染 ≤1862；card 1863 为 Cairo 抖动）。

## §7 印/网文字层比对 + 斜体三联症（必查 (e)）

- `pdftotext`：印 58,153 字节 / 38,771 字符；网 58,200 字节 / 38,818 字符。
  字符多重集差异**仅为网版多 43 个空格 + 4 个换行**；空白剥离后多重集完全相等（各 31,041 字符）—— 纯分段噪声。
  （注：KIT「31,041 字符各」指剥离空白后计数，与本实测一致。）
- 斜体：全版仅 P1 有斜体 run（5 个，y=1712，`«чёрная пятница»`，`logs/italic-check.log`）；
  P2–P8 为 0。印 PDF P1 字体表有 `NotoSerif-MediumItalic` + `Newsreader16pt-Italic`；
  **网 PDF 全 8 页无任何斜体字体**（仅 Regular/Bold）。
- 渲染对比（`print-wordbox.png` vs `web-wordbox.png`，同区域 3×）：
  印：`«чёрная пятница»` 斜体，闭引号紧贴；网：**正体，且 `»` visibly 脱离**（`«чёрная пятница »`，肉眼可见空隙）；
  文字层：网 `«чёрная пятница »` vs 印 `«чёрная пятница»`。
  span 位置：`»` 在印/网中同为 x=1220.6 —— 脱离是网版字体替换（斜体 run 被正体替代）所致，非位置移动。
- 三联症：斜体丢失（有）、闭引号脱离（有，渲染可见）、斜体词内丢空格（无）。
- **判定：D7 缺陷**（机制 webpdf.py，未处理斜体字体；与 ru-en D3 同类，见 PROOF-NOTE）。

## §8 其它机械门

- **P8 最小字号**（PyMuPDF，印+网一致，`logs/pdf-spans.log`）：**9.75 pt**（386 个 span；直方图另有 9.98×24、10.35×255、…、34.5×3）。
  符合 SOP §1.1 下限 9.75 pt（目标 11.25 pt）。注：KIT「P8 min font」为配置 px，非渲染 pt —— 以实测为准。
- **弯引号扫描**：SVG 全版 0 个 U+201C/U+201D/U+2019，唯 P7 故意保留的 `«на “чёрной пятнице”»` 一对（1 × “，1 × ”）；
  text.md « » 平衡 165/165。✓
- **CJK 扫描**：SVG 仅 p1 moth `<title>` 元数据内 `三色蛾`（与核心一致）；text.md **0 个 CJK 字符**。✓
- **ABSTRACT.txt**：405 字节（KIT 称 404，差一个换行，非缺陷），单行葡语，无 ASCII 双引号，含真实主题 + masthead + A2–B2 + 150。✓
- **text.md 第 E 节**：type 标签全部为葡语（`[Traduzir para português]` ×4、`[Tradução]` 等），0 CJK。必查 (d) 通过。✓
- **P4 赛果表**（自 SVG 重建，`logs/table-matching.log`）：8 场——6.11 Локомотив–Рубин 0:1；7.11 Факел–Динамо 1:2；
  7.11 Ахмат–Родина 1:0；7.11 Краснодар–ЦСКА 4:2；8.11 Крылья Советов–Оренбург 2:0；8.11 Спартак–Акрон 2:1；
  8.11 Зенит–Ростов 2:2；8.11 Балтика–Динамо Мх 0:1。总进球 21 ✓ 与 P1 数字框一致；星期标签 Пт/Сб/Вс 与日期吻合；
  与正文、top-5（Zenit/Dynamo 31、Spartak 29、Krasnodar/CSKA 26、Lokomotiv 第 15）及 VOL.3 更正（Балтика–Динамо Мх 0:1，11 月 8 日 20:45）一致。
- **P7 金句 8/8**：逐字见于原文，页码引用正确（P1×2、P2、P3、P4、P5、P6×2）；范文 H 手数 **97 词**（简报 80–100）。✓
- **第 15 轮赛程**（P4）：8 场，日期/星期吻合（Пт 20.11、Сб 21.11、Вс 22.11）。✓
- **日期/星期**（`date -d`，America/Toronto）：2026-11-04 三、11-06 五、11-07 六、11-08 日、11-12 四、11-16 一、11-17 二、11-18 三、11-19 四、11-20 五、11-22 日、11-27 五（黑五 ✓）、11-30 一（网一 ✓）。
  11 月仅 11 月 4 日（民族团结日）一个公共假日 → 20 工作日 + 10 休息日 ✓（P6 正文）；
  11 月 29 日母亲节为当月最后一个周日（P7 VOL.5 预告，刊期外）✓。
- **外部事实来源**：
  - 赛果/赛程/黑五/天气/电影/节日：核心 KIT §3（`core-ru/WEEKLY-KIT.md`，2026-11-10 核查）——
    RPL 第 14 轮 sports.ru / Forbes / rusfootball.info；第 15 轮赛程已核实；
    乌兹别克斯坦–俄罗斯 11 月 12 日场截稿时（11 月 10 日）无法核实，正文已如实披露「赛果未知，完整结果见 VOL.5」；
    黑五：Ozon 11 月 13 日–12 月 2 日、Wildberries 11 月 16–30 日、«М.Видео» 自 12 日、«Яндекс Маркет» 预热 25–27 日、Lamoda 27–30 日、俄罗斯自 2013 年办黑五；
    天气 weather.com 10 日预报 + Fobos 月度展望；11.11 数据沿用 W46 已核实数据。
    **本版未对线下真实赛果再做独立联网复核**（核心为冻结来源）；赛果表内部一致性已验（见上）。
  - Q20 语法（D6）：https://www.settemilalingue.com/en/languages/ru/grammar/prepositional-case
    （neuter nouns in -ие: `здание → в здании`）；http://masterrussian.com/aa081500a.shtml
    （neuter nouns ending in -ие get -и in the prepositional）。
  - 日历/星期：`date -d`（本机）。
- **8 张 card 逐版目检**：P1–P8 全部读过（`cards/p1-pervaya.png` … `cards/p8-test.png`）。版式、图片/图注（P1 公园、P2 尤恩《冬·罗斯托夫》、P4 1912 奥运队、P5 市场玉米、P7 普希金肖像）、
  P6 日历条与图表、P7 错例诊所与读者来信框、P8 答案键完整性均无其他可见问题；P3/P5/P6 中栏留白为空气感版式，非缺陷。
  目检另确认：P2 Q20 题干确为 `Дети пишут Деду Морозу о своём ___.`；P8 印出键 Q20 确为 `желание`。

## §9 判为非缺陷的项（汇总，证据见上）

1. occlusion 42 TEXTX（§1）。2. P2 cream box 末行降部（§2，余量 0.02 px）。3. P1 `O QUE DIZEM OS MEDIA` 贴边（§6）。
4. P1 `Segundo…` 行 card-only 1866（§6）。5. P2 `Quatro palavras…` 仅 span advance +2.1（§6）。
6. P1 `ГОДА` 顶条与全部页脚（§6）。7. Nota 框俄—葡间距 4.3–5.0 px（PIL 实测，见 §6 注：P2 `поздравить→felicitar` 4.8、
   P3 `биография→biopic` 4.9、`криминальная→policial` 4.3、`экранизация→adaptação` 5.0；与 KIT 4–6 px  ruling 一致）。
8. text.md `— СТРАНИЦА ? —` 与尾部 `«Морозко»` 署名行（与核心 text.md 行 668、838 完全一致，核心导出器格式）。
9. text.md 第 E 节全葡语、0 CJK（§8）。10. 印/网 43 空格差为分段噪声（§7）。11. Q140 译注 `a todos`（地道问候许可）。
12. Q150：P8 `✓` vs text.md 开放题说明（与核心一致；范文 97 词）。13. P8 无 Morozko 图（构建条件跳过，与 W46 ru-pt 一致；署名行保留）。

## §10 日志与证据文件

全部在 `<scratch>/logs/`：`occlusion.log/.json`、`occlusion-core.log/.json`、`occlusion-selftest.log`、`creambox.log`、
`p8-compare.log/.json`、`p8-extract.log/.json`、`p8-extract-core.json`、`freeze-baseline.log`、`freeze-diff.log/.json`、
`freeze-cyr-check.log`、`freeze-rebuild-edition.log`、`pdf-spans.log`、`core-pdf-spans.log`、`ink-sweep.log`、
`pixel-global.log`、`pdf-render-global.log`、`key-compare.log`、`table-matching.log`、`matching-options.log`、
`text-checks.log`、`italic-check.log`、`italic-spans.log`、`print.txt`、`web.txt`。
裁切证据：`crop-p1-palavra.png`、`crop-p1-media.png`、`crop-p1-bridge.png`、`crop-p2-mezhdunarodny.png`、
`crop-p1-mediabox-bottom.png`、`crop-p1-x1866-nearest.png`、`crop-p1-headline-zenit.png`、`crop-p8-band.png`、`crop-p7-band.png`、
`crop-p2-boxbottom.png`、`fresh-p1.png`、`pdf-p1-render.png`、`print-wordbox.png`、`web-wordbox.png`；
重建副本：`rebuild-copy/`（scratch 内，源文件未动）。
