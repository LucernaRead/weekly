# PROOF-NOTE — 2026-W47 ru → pt (proof1)

- 版：`2026-w47-ru-pt`（俄语家庭 × 葡萄牙语读者），VOL.4
- 印 PDF：`Lucerna-VOL4-ru-pt.pdf`，SHA `e6171dabf8d871619b75a45c691ffbf41cd994bf1ef597ad6907294b6f26ff88`，21,199,772 字节
- 网 PDF：`Lucerna-VOL4-ru-pt-web.pdf`，SHA `cc8fea68fcf0c8292cae4f73ee0ed23c2facacae1d34e77f9fdd1b2d995323ce`，3,344,677 字节
- text.md：`2026-w47-ru-pt.text.md`，SHA `7e785cc00f4d48821bb7736d000bbcb491974525477a03a3772890229dcd021e`，65,098 字节，838 行
- 三个 SHA 均与任务一致（磁盘实测，见 GATE-LOG §0）。
- 方法：全文通读（印 PDF 8 页 + text.md 全文 838 行）+ 150 题逐题手验 + 全部机械门实跑（不信 KIT，只信自己跑的结果）+ 8 张 card 逐版目检。

## 结论：(b) 有缺陷，不能定稿

共 **7 项缺陷**：MAJOR 3 项（D1、D6、D7），minor 4 项（D2、D3、D4、D5）。
修复后须重跑全部机械门并重新复校受影响页。

## 缺陷清单

### D1 — MAJOR · 本版 fan-out · P1 框标题横向溢出
- 位置：P1 右栏「СЛОВО НЕДЕЛИ / A PALAVRA DA SEMANA」标题，y=1660，bold 22，x=1617.5。
- 证据（右文本边 = 1862 px，四法一致）：
  - PDF 渲染（印 PDF，1950 px）：墨右 1886 → **+24 px**；
  - PDF span：advance 右 1887.5 → +25.5 px；
  - PIL 真墨（NotoSansCJK）：墨右 1886.5 → +24.5 px；
  -  shipped card（CairoSVG PNG）：墨右 1888 → +26 px。
- 原因：葡萄牙语 gloss `A PALAVRA DA SEMANA` 比核心版标题长，超出右栏边界。
- 修复：缩短标题（如只留 `A PALAVRA DA SEMANA` 缩版或减字号）并重测四法全部 ≤1862。

### D2 — minor · 本版 fan-out · P1 quiz 桥接行轻微溢出
- 位置：P1 底部 `Leia a primeira página e escolha a resposta certa　Respostas na página 8`，y=2348。
- 证据：PDF 渲染 1865（+3），span advance 1866.9（+4.9），PIL 真墨 1862.5（+0.5），card 1856（Cairo 偏差，见 GATE-LOG §6）。
- 修复：缩短约 5 px（如删 `a resposta certa` 的一个词或减一空格）。

### D3 — minor · 本版 fan-out · P2–P6 页脚说明行轻微溢出（5 处同一行）
- 位置：`Respostas na página 8　Os níveis podem misturar-se; procure pelo número do exercício`，P2 y=1876，P3/P5 y=1648，P4 y=1939.3，P6 y=1866。
- 证据：五页 PDF 渲染均为 1864（+2）；span advance 1866.5；PIL 真墨 1862.3；card ≤1862。
- 修复：缩短约 5 px（一处改动，五页同修）。

### D4 — minor · 核心继承 · P2 练习选项溢出
- 位置：P2 D 组选项 `b. Международный день студента`，y=2162，size 23。
- 证据：PDF 渲染 1868（+6），span 1870.0，PIL 真墨 1867.7，card 1870；**核心 core-ru 印 PDF 同一 span 的 x1 亦为 1402.5 pt**，几何完全一致 —— 核心问题。
- 修复：在 core 修（缩短选项或减字号），fan-out 随之继承。

### D5 — minor · 本版 fan-out · P8 答案说明行轻微溢出
- 位置：P8 `Cada resposta com uma breve nota em português　✓ = texto modelo`，y=1302。
- 证据：PDF 渲染 1864（+2），span advance 1865.9。
- 修复：缩短约 4 px。

### D6 — MAJOR · 核心继承 · Q20 答案键错误（教错格）
- 位置：P2 练习 B 第 20 题。题干：`Дети пишут Деду Морозу о своём ___.`
- 现状：答案键到处都是 `желание`——text.md 题干内联键、text.md Answers §、P8 印出答案键、核心 core-ru text.md 与核心 P8 键完全一致。
- 错误：`о` 支配前置格，且代词 `своём` 已是前置格，名词必须是前置格。`желание` 是中性 -ие 名词，前置格为 **-ии**，正确形式是 **`желании`**。现行键给出的是主格词典形，不是题目要求的屈折形。
- 依据：本版惯例一律给正确屈折形（Q38 → `ноября`；Q73 → `заказов`）；公开语法来源：masterrussian.com 前置格表（-ие 中性名词前置格取 -и）、settemilalingue.com（neuter nouns in -ие: `здание → в здании`）。链接见 GATE-LOG §8。
- 修复：在 core 修（core-ru text.md + 核心 P8 键），fan-out 随之继承。

### D7 — MAJOR · 机制（webpdf.py） · 网 PDF 丢失斜体 + 闭引号脱离
- 位置：P1 每周词 `«чёрная пятница»`（y=1712）。全版只有 P1 有斜体（5 个 run：`«` `чёрная` ` ` `пятница` `»`，Newsreader/Noto Serif italic 21.5）。
- 证据：
  - 印 PDF：确有斜体字体（`NotoSerif-MediumItalic`、`Newsreader16pt-Italic`），渲染为斜体，闭引号紧贴（`«чёрная пятница»`）。
  - 网 PDF：**全 8 页没有任何斜体字体**（字体表只有 Regular/Bold）；渲染为正体；闭引号 visibly 脱离 —— 网 PDF 渲染图可见 `«чёрная пятница »`，`»` 与 `пятница` 之间有明显空隙；文字层亦为 `«чёрная пятница »`（印版为 `«чёрная пятница»`）。
  - 三联症核查：斜体丢失（有）、闭引号脱离（有，渲染可见）、斜体词内丢空格（无，`чёрная пятница` 间空格正常）。与 ru-en D3 同类。
- 修复：webpdf.py 须处理斜体字体（subset NotoSerif-Italic + Newsreader-Italic，或合成 oblique），重建网 PDF；重建后重验 P1 词框渲染与文字层。

## 判为非缺陷的项（证据见 GATE-LOG）

1. **occlusion 42 TEXTX**：全是相邻 run 的包围盒假阳性（目检 3 处：P8 `ОТВЕТЫ / TESTE E RESPOSTAS` 带清晰分离；P1 `«Зенит»` 的 `»` 间隙正常）；0 COVER/LINEX/FOOTER/EDGE/BOXTITLE。核心同跑亦为 42 TEXTX，38 处完全相同。
2. **P2 cream box 末行降部**：box y=795，bottom=1159.0，末行基线 1154.0（`para o Avô Gelo.`），desc-clear −1.0 仅为基线算法；PIL 真墨实测墨底 = 基线 +5 px = 1158.98，渲染像素扫描最末深色行 y=1158，1159 及以下无墨，3× 放大确认 `p` 降部在框内。非缺陷，但余量仅 0.02 px，见 O3。
3. **P1 `O QUE DIZEM OS MEDIA`**：PDF 渲染恰为 1862（贴边），span +1.5、PIL +2.4、card +2 —— 在 ±2 px 光栅抖动内，不计缺陷；建议修 D1 时顺手处理。见 O1。
4. **P1 `Segundo os media russos, novembro de 2026`**：span/PIL/PDF 渲染均 ≤1861，仅 card 读出 1866，属 Cairo 与 PDF 渲染分歧，非缺陷。
5. **P2 `Quatro palavras sobre o tempo de novembro`**：仅 span advance +2.1，PDF 渲染 ≤1862，非缺陷。
6. **P1 `ГОДА` 顶条与全部页脚**（`Página N de 8`）：PDF 渲染 ≤1862；card 1863 为 Cairo 抖动，非缺陷。
7. **Nota 框内俄词—葡 gloss 间距窄**（如 `поздравитьfelicitar`）：PIL 实测间隙 4.3–5.0 px（`поздравить→felicitar` 4.8，`биография→biopic` 4.9，`криминальная→policial` 4.3，`экранизация→adaptação` 5.0），与 KIT 所述 4–6 px 一致；缩略图上看似粘连是降采样所致。非缺陷。
8. **text.md `— СТРАНИЦА ? —` 分隔符与尾部 `«Морозко»` 署名行**：与核心 core-ru text.md 完全一致（行 668、838），属核心导出器格式。非缺陷。
9. **text.md 第 E 节 type 标签**：全部为葡萄牙语（`[Traduzir para português]` ×4、`[Tradução]` 等），text.md **0 个 CJK 字符**，无中文残留。必查 (d) 通过。
10. **印/网文字层 43 空格差**：空白剥离后字符多重集完全相等（各 31,041 字符），纯 pdftotext 分段噪声；网版（索引件）空格完整。非缺陷。见 O2。
11. **Q140 译注**：`Поздравляю с Днём студента!` → `Feliz Dia do Estudante a todos!`——`a todos` 为地道问候许可，非缺陷。
12. **Q150**：P8 印 `✓`，text.md 给开放题说明 —— 与核心一致；范文 97 词（手数，简报 80–100）。非缺陷。
13. **P8 无 Morozko 图**：构建条件跳过该图，与 W46 ru-pt 及核心一致；text.md 署名行保留。非缺陷。

## 未决事项

- **O1**：P1 `O QUE DIZEM OS MEDIA` 恰贴右边缘（PDF 渲染 1862，span +1.5，PIL +2.4）。不计缺陷，但修 D1 时顺手缩短 2–3 px 更稳妥。
- **O2**：印 PDF 文字层比网 PDF 少 43 个空格（pdftotext 分段噪声；空白剥离后完全相等）。网 PDF（网站索引件）不受影响。是否接受印版文字层此差异，留待机制方决定。
- **O3**：P2 cream box 末行余量仅 0.02 px（墨底 1158.98 vs 框底 1159.0）。通过，但未来构建应给降部留余量。
- **O4**：`tools/freeze.py` 无 `freeze_direct` 子命令（仅 baseline/diff），按任务要求记为方法备注，非缺陷。本版已手工重建验证：从 content*.py 重跑，8/8 SVG 与 shipped 字节一致。
- **O5**：KIT 数字小出入（非缺陷）：ABSTRACT.txt 实测 405 字节（KIT 称 404，差一个换行）；KIT「31,041 字符各」指空白剥离后计数（我实测 pdftotext 总量印 38,771 / 网 38,818 字符，剥离后各 31,041 —— 与 KIT 一致）。

## 核实摘要

- **全文通读**：text.md 838 行全读；印 PDF 8 页 card 逐版目检（P1–P8）；P4 赛果表 8 场重建（总进球 21 ✓，与 P1 数字框一致）；P6 图表 38/26/18/18=100 ✓；P7 金句 8/8 逐字核对原文与页码（P1×2、P2、P3、P4、P5、P6×2）；范文 H 计 97 词 ✓。
- **日期/星期**：`date -d` 核实 2026-11-04 三、11-06 五、11-07 六、11-08 日、11-12 四、11-16 一、11-17 二、11-18 三、11-19 四、11-20 五、11-22 日、11-27 五（黑五 ✓）、11-30 一（网一 ✓）；11 月仅 11 月 4 日一个公共假日 → 20 工作日 + 10 休息日 ✓；11 月 29 日母亲节为当月最后一个周日（VOL.5 预告，刊期外）✓。
- **keycheck**：150/150 逐题手验（`keycheck-150.json`），P8 印出键 vs text.md Answers 149/150 形式一致（仅 Q150 为 ✓ vs 开放题说明，与核心一致）；题干内联键 129 处全部与 Answers 一致；5 个匹配组（20 题）逐一对照 SVG 选项表核实；其余全部对照正文语义核实。唯一 FAIL：Q20（D6）。
- **机械门**：occlusion（自测 6 类全触发，干净对照静默；本版 42 TEXTX 均为假阳性）；正典 creambox 32 盒（见 O3；P7 toolbox 最小 desc-clear +5.9，通过）；p8 compare CLEAN（150/150，keydiff [137,138,139,140] 为四条 E 节 RU→PT 翻译键，已正确翻译）；freeze baseline 8/8 字节一致 + diff（新增 CJK 仅 U+3000 ×6；P1–P5 西里尔 run 序列一致；P6–P8 差异仅为讲解层葡语翻译）；本版重建 8/8 字节一致；P8 最小字号实测 9.75 pt（印/网一致，386 个 span；SOP §1.1 下限 9.75 pt，目标 11.25 pt）；弯引号 SVG 全版 0 个 U+201C/U+201D/U+2019，唯 P7 故意保留的 `«на “чёрной пятнице”»` 一对；text.md « » 平衡 165/165；SVG CJK 仅 p1 moth `<title>` 内 `三色蛾`（与核心一致）；text.md 0 CJK。
- **必查项 (a)–(e)**：(a) P1 溢出 —— D1（+D2/D3/D5）；(b) cream box 降部 —— 通过（O3）；(c) P7 toolbox —— 实测通过（最小 desc-clear +5.9）；(d) E 节标签 —— 全葡语，0 CJK，通过；(e) 网 PDF 斜体 —— **复现 D7**（斜体丢失 + 闭引号脱离）。
- **外部事实**：赛果与赛程以核心 KIT §3 来源为准（sports.ru / Forbes / rusfootball.info；乌兹别克斯坦 11 月 12 日场截稿时未核实，正文已如实披露「截至 11 月 10 日未知，见 VOL.5」）；天气 weather.com + Fobos；Q20 语法来源见 GATE-LOG §8。本版未对线下真实赛果再做独立联网复核（核心为冻结来源；赛果表内部一致性已验）。
