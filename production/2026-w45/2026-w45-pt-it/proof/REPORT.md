# 独立校对报告 — W45 PT×IT（葡萄牙语正文 × 意大利语讲解）

**结论：ZERO PROBLEMS** — 全部 11 项门禁独立重测通过，无阻塞项。
校对员：独立校对（只校对，不改源码，不宣布上架）。
校对时间：2026-10-27（UTC 22:32–22:41）。交付与核心在校对前后哈希均未变（见 §12）。

**开工查重**：首查交付目录与构建树最新写盘为 BUILD-LOG（UTC 22:30），
95 秒复查零新写盘后开工；无进行中渲染进程。未发 Discord、未往主聊天发卡片/PDF、
未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）。
SOP 与工具箱 README #7–#22 已读；机械门禁一律用共享工具（freeze.py / p8.py /
occlusion_audit.py）重跑，另写独立脚本复测几何、gloss、金句、题量。

---

## 1. 冻结（freeze.py）

- `freeze.py baseline`（核心构建目录重跑）：**8/8 逐字节相同**，核心交付 SHA 与 KIT §1 表逐项一致
  （P1 0dc8089df727dfe4、P2 56db3aa80e1318db、P3 82f6fc3a94fbc11e、P4 c5647cf6e9c080ec、
  P5 92e86020ce81f3c8、P6 e6097473ded2f016、P7 a72cb75a519319f4、P8 82630480322959ad），
  且跑后复验核心未动。
- `freeze.py diff --strict-cjk`：**新增 CJK = 0**；终版 CJK 逐页皆 0（P1–P8 各 0）；
  全文「桥接」= 0（交付 SVG 文本层扫描）。
- 14 项非 CJK 删除串逐项裁定（独立复核，与构建员计数一致），**无冻结葡语句丢失**：

| # | 删除串 | 裁定 |
|---|---|---|
| P1-1 | `12h — os portões abrem no domingo 8（` | 重排碎片；葡语部分 `12h — os portões abrem no domingo 8` 在本版逐字存在，括号后为意语注 |
| P1-2 | `O JORNAL SEMANAL PARA APRENDER — O BRASIL DE VERDADE, EM PORTUGUÊS, DO BRASIL` | 刊头标语行被配对徽章替换，属登记家具；W43 PT×IT、W45 PT×EN、W45 PT×DE 均同样替换（y=372 徽章位），非正文丢失 |
| P2-1 | `NÍVEL A2 · Finados e revisão: o feriadão do Brasil` | 逐字存在于本版加长双语副标题中 |
| P5-1 | `5. Domingo 8: chegue antes das 12h（` | 重排碎片；葡语部分逐字存在，括号后为意语注 |
| P6-1 | `chamada · local · conferir` | 碎片，逐字存在于本版对应行 |
| P8-1..6 | 16/17/18/19/102/103 题 `— conferir：/abrir：/levar：/começar：` | 仅全角冒号 `：`→半角 `:`，键 token 逐字节相同 |
| P8-7..8 | 57/58 题 `mais — 18 > 16：mais` / `mais — 17 < 18：mais cedo` | 仅冒号宽度，键 `mais` 相同（58 题注续行 `una seconda entrata` 为意语注换行） |
| P8-9 | 139 题 `O feriadão é de 31 de outubro a 2 de novembro. — feriadão =` | 该串本身亦逐字存在于本版（多重集计数差由换行引起），键未动 |

## 2. P7 词框（硬性门）——通过，且强于宣称

- P7 页删除串中**非 CJK = 0**：P7 没有任何葡语字符串被删除，葡语定义句/诊所句/三栏讲解原文全部逐字保留。
- P7 新增串 40 项逐项检查：全部为意大利语家具、译文行、注释（`Nota della redazione…`、
  金句意译、错误框意注等），无葡语定义句被本地化改写。
- P2–P6 gloss 词框：葡语词条逐字保留（见 §5 逐项对照），仅释义译为意大利语。

## 3. P8

- `p8.py compare`：**CLEAN，150 = 150**，无缺失、无多余、无 UNCERTAIN。
- keydiff 18 项逐项对照印刷 P8 行核实（工具输出与构建员名单逐项一致），结论与构建员一致：
  - **16 项括号分支提取伪影**（真实键 token 与核心逐字节相同）：2（`portões`）、4（`13h30`）、
    25（`c`）、26（`b`）、27（`d`）、28（`a`）、52（`b`）、53（`c`）、54（`a`）、55（`d`）、
    101（`confiro`，另含冒号宽度统一）、141（`b`）、142（`d`）、143（`a`）、144（`c`）、146（`A`）。
    机理：意语简析尾带括号（如 `(c)`、`(sezione)`）时工具取括号前整段为键。
  - **2 项真重定向**（翻译类按讲解版惯例重新指向读者语，题面葡语原句不动）：
    137：核心键 `11 月 8 日周日是高考的第一天。` → 本版 `Domenica 8 novembre, è il primo giorno dell'Enem.`
    （注 `Vedi il titolo di pagina 6`）；
    138：核心键 `周日前核对确认卡。` → 本版 `Controlla la tessera prima di domenica.`
    （注 `Conferir = controllare, verificare`）。
  - 139/140 键不变：`O feriadão é de 31 de outubro a 2 de novembro.` /
    `Quando você chegar, apresente o documento com foto.`（题面改为意语句，键仍为葡语）。
  - 150 写作 apparatus：两版键同为 `✓`（故不在 keydiff 内），注为意语
    `Vedi il testo modello nella sezione H di questa pagina (93 parole)`。
- P8 注释纯意大利语：P8 文本层 CJK = 0，常见英文词扫描 0 命中；
  葡语词仅作键与语法范式引用（如 `conferir: ele → confere`），符合讲解版惯例。
- P8 印刷注释集合 150/150（p8.py extract 两版均为 150 noted）。

## 4. 几何

- `occlusion_audit.py`（自检先行：6 类植入缺陷全部命中、干净对照零误报）：
  **分版 0 / 核心 0 / NEW vs 核心 0**，与构建员自查一致。
- 独立重测（自写脚本，tables.json 字体路径 PIL 实测）：
  - 同基线墨迹碰撞：**0**；框线/右缘扫描：墨迹右界越界 **0**（内框 1910 / 外框 1922 / 页边 1950，
    左界 <28 亦 0）——此为墨迹法，比 ADVANCE 法更严，仍为 0。
  - 框线压字扫描：2 旗（构建员报 1 旗，差异见 §13 第 2 条），逐项裁定如下。
  - P6 图表标签覆盖（基线锚定墨迹法：ascent 24 / descent 6，anchor ls）：
    `portões abertos` / `espera` / `prova` 3 条标签 vs 后绘条形覆盖率均为 **0.00%**（<30% 过）；
    标签墨迹右界（247.1 / 154.4 / 145.2）与条形左界（265.1 / 172.4 / 163.3）根本无 x 重叠；
    3 条数值文本与条形重叠 0。
- **P3 日历框末行 `Palmeiras, a volta.`（h@555.5）裁定：测量伪报，非真压字。**
  证据：(a) 该行坐标 x=1473.0 / y=571.18 / fs=21.5 与核心版、EN 版逐字节相同，属冻结继承；
  (b) 3× 卡片裁图：框线从两行之间通过，`Palmeiras, a volta.` 全行清晰、无一字被划；
  (c) 像素行分析：字形墨迹顶约 y=555–556，框线 555.5 至多擦过最高字母 1 像素抗锯齿边，
  属 PIL 全升部墨迹框（顶 553.2）高估所致；(d) 该区域 y=500–599 与核心卡片像素差为 0。
  结论：不动（改动将破坏冻结），与构建员裁定一致，另补上 1 像素擦边这一实测细节。
- P5 `Matemática (prévia).`（h@513.0，我方扫描多出的一旗）：裁图显示框线干净地位于文字下方，
  该区域与核心卡片像素差为 0；0.6px 墨迹底超标系我方字号取整（21.5→22）所致测量伪报。
- P7 Fix-2 后几何：金句葡语行基线 2051.0 / 2143.0 / 2235.0 / 2327.0，步距 **92**（104→92 属实）；
  末行意译基线 2376.7，墨迹底约 2383，下期预告深色框顶 **2404**（rect y=2404 h=118），
  间隙约 21px，**无压入，遮挡 0**；P7 卡片目视亦见金句区与深色预告框之间有明显空隙。
  读者园地末行（意语注）基线 1895.5，栏底约 1920，与构建员所述一致。

## 5. gloss（渲染后 · 拆分逐页逐项重数）

从渲染 SVG 的 `Nota —` 框逐行拼接后按 `·` 拆分，并与核心同法对照：

| 页 | 本版（词条） | 核心 | 对照 |
|---|---|---|---|
| P2 | 6：o feriadão, o cemitério, a vela, o crisântemo, a missa, conferir | 6 | 1:1，词条逐字相同 |
| P3 | 6：o túmulo, a flor, acender, rezar, o silêncio, a lembrança | 6 | 1:1 |
| P4 | 5：a ida, a volta, o finalista, a decisão, a rodada | 5 | 1:1 |
| P5 | 5：a reta final, a véspera, a maratona, separar, a cabeça | 5 | 1:1 |
| P6 | 4：os portões, a segunda chamada, conferir, a correria | 4 | 1:1 |
| 合计 | **26** | **26** | 逐页 1:1 |

**FLAG 裁定：构建员「P3 11」不是分布错误。** 构建日志「P3 11」与 KIT §7「P3 6+5」
是把 P3（6）与 P4（5）合并书写的口径/笔误；渲染 SVG 独立重数证明 P3 实为 6、P4 实为 5，
与任务书所载 PT 核心分布（P2 6 / P3 6 / P4 5 / P5 5 / P6 4）逐页相符。
分布错误不成立，不阻塞；但 KIT/BUILD-LOG 的合并写法应订正为逐页写法（见 §13）。

## 6. 金句

- 本版 P7 金句 8 句，标签序列（按版面左栏→右栏）**(1, 1, 2, 3, 4, 5, 6, 2)**：
  P1 `Do feriadão à prova: a semana do Enem`、P1 `Muita gente viaja, visita a família e vai ao cemitério levar flores`、
  P2 `Finados é o dia da memória`、P3 `lembrar é um jeito de continuar perto`、
  P4 `cada ponto vale uma posição, cada gol vale uma história`、P5 `quem dorme bem lembra melhor`、
  P6 `primeiro as fáceis, depois as difíceis`、P2 `Confira o cartão, durma bem, chegue cedo`。
- 独立实测核心版：同一 8 句、同一标签序列、同一标注页；程序计数（去 «»、空白归一）
  本版与核心版均为**每句恰 2 次**（源页 1 次 + P7 1 次），且每句在其标注页上实测存在。
- 构建员所称标签序列经核心 SVG 独立实测证实无误（未采信自述）；金句签均为 `Página N` 式，
  与核心/W43 一致。

## 7. 读者园地

P7 右栏逐字摘录与判定（零编造）：

- 葡语披露句原文（保留，与核心逐字相同）：
  `Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o
  fechamento — fica o exemplo, e a promessa passa para o VOL.3.`
- 意语等义句：`Nota della redazione: le lettere vere e i migliori testi promessi nel VOL.1 non erano
  arrivati alla chiusura — resta l'esempio e la promessa passa al VOL.3.`（含 `migliori testi`）。
- 示例标注：`— EXEMPLO DA REDAÇÃO` + 意语 `Esempio della redazione — non è una lettera vera.`；
  示例本身为葡语原句 `«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!»`，无虚构读者/人名。
- **显性意语邀请（3 行，y=1554.6 / 1583.0 / 1611.4）**：
  `Esempio della redazione — non è una lettera vera. Mandate le vostre lettere: le migliori saranno
  pubblicate nel VOL.3!`
  判定：祈使句 `Mandate` ✓ + VOL.3 刊登承诺 `saranno pubblicate nel VOL.3` ✓，构成显性邀请；
  下期预告行（`A PRÓXIMA SEMANA` 内容行）未计入。
- Fix-2 后 P7 几何见 §4：金句末行与预告框无压入。

## 8. 家具（与 W43 PT×IT 实测对照）

| 家具 | W45 PT×IT 实测 | W43 PT×IT 实测 | 结论 |
|---|---|---|---|
| P1 徽章 | 19pt 700 砖红 #a4553a，y=372，`TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI` | 同串、19pt 700 #a4553a、y=372 | 一致 ✓ |
| 页脚 | 20pt，`A Lucerna · SETTIMANALE PORTOGHESE VOL.2 · TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO` | 同式，VOL.1 | 仅期号不同，理由：本期核心即 VOL.2 ✓ |
| 页码行 | `Pagina N di 8` | 同式 | 一致 ✓ |
| gloss 前缀 | `Nota —` | `Nota —` | 一致 ✓ |
| P8 分隔符 | `— PÁGINA {n} —`，无 ASCII `PAGINA` 式 | 同式 | 一致 ✓（tables.json 泛写不适用） |
| 金句签 | `Página N` | `Página N` | 一致 ✓ |
| 金句框头 | 27pt，`FRASES DA SEMANA · FRASI DELLA SETTIMANA (tratte parola per parola da questo numero)` | 同串 27pt | 一致 ✓ |
| 错误框头 | 23pt `ERROS COMUNS · ERRORI` | 同串 23pt | 一致 ✓ |
| 栏目头 | `VIDA · VITA QUOTIDIANA` 36pt 等，PT·IT 双语式 | 同式 | 一致 ✓ |
| 刊头 | `A Lucerna` 168pt；副刊头 36pt | 同式（VOL.1） | 一致 ✓（期号跟核心） |
| P1 数字框头 | 20pt `A SEMANA EM NÚMEROS · IN CIFRE`（351.7px ≤ 框内 390） | 23pt `A SEMANA EM NÚMEROS · CIFRE` | 字号差异有理由（23pt 线性推算约 404px > 390，沿 EN 版同类改动降为 20pt）；意语词 `IN CIFRE` vs `CIFRE` 的措辞差 KIT §4 未说明，见 §13（非阻塞） |
| P7 金句行距 | 92 | 158（W43 每栏 3 句，步距不同） | 差异有理由：Fix-2 修复预告框压入（§4），且 W43 金句仅 6 句、本期核心 8 句，内容本就不同 |
| 目录级别签 | `todos` 保留 | `todos` | 一致 ✓ |
| P8 副标题 | `Pagina 8 · A grande prova da semana + todas as respostas`（葡语描述语） | 同式 | 一致 ✓ |

## 9. 图片

- 全期仅 P1 一图：`<image>` 元素 P1 = 1，其余 7 页 = 0；核心版同样分布。
- 载荷：P1 内嵌 base64 解码后 SHA-256 与构建树 `assets/estudo.jpg` 完全一致，
  base64 串 SHA 前 16 位 `fd231e77993f09e0` 与核心版逐字节同（与 KIT §10 一致）。
- 署名行 `Foto: Gary Todd / Wikimedia Commons — CC0` 在 P1 图说下方在版（卡片目视确认），
  核心版同行亦在版。

## 10. 跨族残留

- 中文（CJK）：逐页 0（freeze --strict-cjk 新增 0，终版 8 页各 0）。
- 西里尔 / 韩文 / 假名：逐页 0。
- 英文独立词：0。核查：`Note |` 0、`Page N of` 0、常见英文词（the/and/with/from/note/page/answer 等）
  全文 0 命中；仅有的 `COMPLETE` 两处为核心冻结葡语栏目标题
  （P2 `C · COMPLETE COM OS NÚMEROS`、P8 `A · COMPLETE A CRÔNICA`），与核心逐字节相同；
  `VOL.2` 为期号标记、`Enem` 为葡语专名，均非英文残留。
- ABSTRACT.txt：意大利语单行（362 字节，1 个换行符结尾），ASCII 双引号 0 个；
  含刊名 `A Lucerna`、目标语 `portoghese`、读者语 `italiano`、分级 `A2–B2`、题数 `150 esercizi`、
  真实主题关键词 `Enem` / `Finados` / `Copa do Brasil`，及学习者搜索短语
  `imparare il portoghese del Brasile leggendo`。事实均取自本期内容。

## 11. 卡片目视与题量

- 8 张卡片逐页目视：P1–P8 均无重叠、无截断、无压框、无侵入页脚带；页脚 8/8 为 VOL.2，
  配对徽章/页眉页脚齐全；P7 金句区与预告框间隙清晰；P6 条形图标签完整在条形左侧。
- 题量独立展开计数（渲染 SVG fs=24 题号节点，含 `25–28.` / `52–55.` / `141–144.` 合并组展开）：
  **150 题连续 1–150，无缺重**；页分布 **10 / 18 / 18 / 18 / 18 / 18 / 12 / 38**。
- 级别独立配对计数（题号节点 ±3px 内徽章节点配对，合并组内各题同继承组徽章；
  5 枚未配对徽章均为栏目阅读级别签，非题目徽章）：
  **A2 49 / B1 70 / B2 31**，与任务书 PT 核心数一致。
- 题型（重跑构建登记表于隔离复算目录，输出与构建日志一致）：
  完成句子 61 / 单选 49 / 配对 12 / 造句 7 / 判断 3 / 完形 13 / 翻译 4 / 写作 1；
  可见标签佐证：`Traduci` 4、`Scrivi` 1、`Forma la frase` 7 块、`Abbina` 3 组（12 题）。
- 范文：MODELO 字符串本版与核心版逐字相同，程序计数 **93 词**，P8 H 区渲染在版
  （`Texto modelo: Domingo, 8 de novembro, acordo cedo e…`），在题面 80–100 词区间内。
- 复算 SVG 8/8 与交付 SVG 逐字节相同（构建完全可复现）。

## 12. 校对前后完整性

- 交付哈希（svg×8、cards×8、print/web PDF）校对前后逐字节一致；
  核心 8 个 SVG 哈希校对前后一致（与 §1 基线表一致）。
- 交付 PDF 实测：print `A-Lucerna-VOL2-IT.pdf` 3,469,993 B，
  SHA-256 `ddedb5135e74f7f3b8ffe11979b53997825fe718f35fb134e0e3a37e84110b0f`；
  web `A-Lucerna-VOL2-IT-web.pdf` 3,483,035 B（< 10 MB），
  SHA-256 `6cab53914433d2e6f733aa23b4c14bfc6eb362e0eafd5acce077b14ec40d1a1a`；
  均与 KIT §11 一致。
- 未清理共享 scratch 目录；复算中间产物已从校对目录删除（复算日志保留）。

## 13. 与构建员自述不符处（均非阻塞）与非阻塞观察

1. **Gloss 分布写法**：构建日志「P3 11」/ KIT §7「P3 6+5」为 P3+P4 合并书写；
   独立重数证明实为 P3 6、P4 5。不是分布错误，但 KIT/BUILD-LOG 应订正为逐页写法，
   以免后人误读为 P3 一页 11 项。
2. **框线压字旗数量**：构建员报 1 旗（P3），我方独立扫描报 2 旗，多出 P5 `Matemática (prévia).`
   h@513.0（0.6px 超标）。裁图裁定为我方字号取整所致测量伪报，核心卡片同区像素差为 0，
   不构成缺陷；披露于此，不改结论。
3. **P3 旗的 1 像素细节**：构建员称「框线从两行之间干净通过」；实测字形墨迹顶（约 555–556）
   与框线 555.5 基本重合，至多擦过最高字母 1 像素抗锯齿边，3× 裁图上无字被划。
   因坐标与核心逐字节相同且属冻结版式，仍裁定为伪报、不动；此细节不影响出厂。
4. **邀请句「独立行」措辞**：KIT §7 称邀请为独立行，实际 SVG 中为 3 个换行文本节点
   （y=1554.6 / 1583.0 / 1611.4）；拼接后内容与 KIT 引文逐字一致，邀请判定不受影响。
5. **数字框头意语措辞**：W45 `IN CIFRE` vs W43 `CIFRE`；字号 20pt 的理由 KIT §4 已给，
   但措辞差未说明。`IN CIFRE` 为更完整的意大利语形式且宽度合规，非阻塞，建议 KIT 补一句。
6. **P5 gloss 框纵向移位**：本版 gloss 框 y=917–1006，核心同框 y=803–862（约 114px 下移），
   内容逐项相同，属讲解层换行重排，非冻结问题。
7. **核心继承的版式观感（非本版缺陷）**：P1 左栏末行 `E o futebol não para: a rodada 34 do`
   在照片带前收束、P2 `D · AS PALAVRAS` 栏目标题位于栏底——两处坐标与核心版逐字节相同，
   为核心原样，校对不作改动要求。
8. **P7 门表述差异**：KIT §6 称「P7 无 gloss 词框定义句本地化问题」；实测更强——P7 删除串中
   非 CJK 为 0，即 P7 无任何葡语串被删，硬性门以最强形式通过。

## 证据文件（同目录）

- `freeze-diff.json`（独立 freeze diff 原始输出）、`occlusion-edition.json`、
  `occlusion-core.json`、`occlusion-new.json`（独立遮挡审计原始输出）
- `geom.json` + `geom.py`（独立几何扫描：同基线/框线/右缘/框线压字/P6 图表/P7 Fix-2）
- `proof1.json` + `proof1.py`（gloss 重构、脚本残留、COMPLETE 对照、P7 节点）
- `rerun.log`（隔离复算登记表：150 / 49-70-31 / 页分布 / 题型）
- `delivery-sha-before.txt` / `delivery-sha-after.txt`、
  `core-sha-before.txt` / `core-sha-after.txt`（校对前后哈希，diff 为空）
- `baseline-pt/`（freeze baseline 复算产物目录）
- 本报告：`REPORT.md`
