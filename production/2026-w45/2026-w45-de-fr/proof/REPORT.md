# W45 DE×FR（德语×法语）独立校对报告

## 结论先行：ZERO PROBLEMS（可定稿）

本报告由独立校对员从头重跑全部必查门得出，不采信构建员自述。待校版本
`files/weekly-report-w45-de-fr/`（SVG×8、卡片×8、印刷 PDF、网页 PDF、
`WEEKLY-KIT.md`、`ABSTRACT.txt`）**无问题，可定稿**。
校对过程未改动任何交付文件（终版 SVG 哈希与开工时一致，见 §10），未发
Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43
目录、未派生任何下级代理。

---

## 0. 开工前查重（stand-down 判定）

- 开工时（2026-10-27 20:42–20:43 UTC）`files/weekly-report-w45-de-fr/` 与
  `hidden_files/weekly-report-w45-de-fr-build/` 均无正在进行的写盘进程
  （`ps` 中无 de-fr 构建/渲染进程；仅有其他配对 de-es、de-it 的校对进程在跑，
  与本版无关）。
- 75 秒复查：de-fr 交付文件 mtime 零新写盘（SVG 20:37、卡片 20:40、PDF 20:40、
  KIT 20:41 均为已完成交付的时间戳）。按协调员裁定正常开工。

## 1. 冻结门（tools/freeze.py，独立重跑）

- **核心 8/8 基线复现**：`freeze.py baseline`（核心构建树
  `hidden_files/weekly-report-w45-de-build`）输出 8/8 byte-identical，
  8 个哈希与 KIT §2 逐一相符；核心开工前哈希与最终哈希 diff 为空
 （`CORE_UNCHANGED`；核心 SVG mtime 仍为 2026-10-26，未被触动）。
- **最终差分**（`freeze.py diff`，与 KIT §2 逐数相符）：
  P1 +23/−23、P2 +36/−32、P3 +40/−40、P4 +25/−22、P5 +44/−39、
  P6 +37/−33、P7 +60/−54、P8 +159/−141。
- **中文字符**：新增中文字符 0；分版 8 页中文字符总数 0（核心 168/186/187/
  155/193/228/394/1429 → 分版 0/页）。
- **P1–P7 德语正文多重集**（整串级差分，只看不含中文字符的移除串）：
  - P1：仅 1 串，即任务规定的副标题行
    `DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND`
    被配对徽章替换（见 §6）。
  - P2、P5：不含中文字符的移除串为 0。
  - P3、P4、P6：各仅 1 串 `。`——中文 gloss 末尾孤悬句号元素，法文版以 `.`
    结尾故无此元素，属讲解层标点伪影，非德语正文。
  - P7：4 串，均为讲解层：`Ein Beispiel der Redaktion!`（标签改法文）、
    `gesenkte Steuer auf Benzin und Diesel.`（工具箱条目改法文释义，德语词头
    `der Tankrabatt` 在版内存续）、`«der Tankrabatt»（Seite 2）: die`
    （同条目首行，法文版为 `«der Tankrabatt» (page 2) : la taxe` +
    `réduite sur l'essence et le diesel.`）、`……`（中文省略号换行伪影）。
- **词级存续补查**（独立加做：从全部移除串提取德语词元，逐词查分版同页）：
  P1–P7 缺失词仅四类，全部有备案且非正文损失：① 每页页脚英文段
  `LUCERNA / GERMAN / WEEKLY`（页脚改法文所致）；② P1 副标题行 6 词
  （规定替换）；③ P6 `Argumente`（节头改写为
  `PRO & CONTRA · Pour et contre — les arguments du débat`，法文
  `arguments` 在位，仿 DE×EN 同胞版）；④ P7 `Beispiel`（标签改法文）、
  `gesenkte`（工具箱释义改法文）。其余全部词元在分版同页存续。
- **P8 仅分隔符差异**：分隔符 8 处 `— Page N —`（N=1..8）；全角括号数 0；
  6 条无中文字符移除串均为 14.5pt→13pt + 半角括号重排后的断行碎片，
  对应德语键（`beschließen → beschlossen`、`tanken → getankt`、
  `bleiben + geschlossen` 等）在分版 P8 中完整存续。

## 2. P8 门（tools/p8.py compare，独立重跑）

- **CLEAN：150 noted = 150 noted，missing=[]，extra_count=0，uncertain=[]，
  keydiff=[137, 138, 139, 150]**，与构建员所述完全一致。
- **keydiff 逐项判定（全部为 DE→FR 真改动，无括号/dash 提取伪影）**：
  - 137：核心中文键 `油价减税持续到十二月。` → 分版
    `La réduction du carburant dure jusqu'en décembre.(laufen = durer)`。
    原始行完整，无截断。
  - 138：核心 `我周二看足球。` → 分版
    `Je regarde le football mardi.(schauen = regarder)`。
  - 139：核心 `学校又开学了。` → 分版
    `L'école a repris.(wieder begonnen = avoir repris)`。
  - 150：核心 `开放题 — 要点见写作框，范文在第 8 版写作框内` → 分版法文
    apparatus（登记表：`Tâche ouverte — suivez les points du cadre
    d'écriture ; le texte modèle est dans le cadre de cette page`，
    注 `Noté selon les points listés`）；范文德语正文未动（P8
    `MUSTER · Texte modèle (84 mots)` 框内 7 行德语范文与核心逐行一致）。
- **反向题 140（不在 keydiff 中，正确）**：两版提取键均为
  `Am Sonntag schlafe ich eine Stunde länger.`，分版 P8 练习区指令为
  `Traduire en allemand`，提示句 `Je dors une heure de plus le dimanche.`，
  注 `dormir une heure de plus = eine Stunde länger schlafen`——键德语不变已核实。
- **登记表**（`hidden_files/weekly-report-w45-de-fr-build/reg.json` 独立重计）：
  150 题，题号 1–150 连续；分页 10/18/18/18/18/18/12/38；级别
  A2 66 / B1 70 / B2 14；题型 QCM 52、à compléter 41、transformation 11、
  appariement 12、vrai/faux 8、texte à trous 8、construction de phrase 8、
  dialogue à compléter 5、traduction 4、rédaction 1——与核心一致。

## 3. 几何审计门（tools/occlusion_audit.py + 同基线扫描，独立重跑）

- **最终：分版 0 flags、核心 0 flags、NEW 0 flags**（自检 planted 6 类全部触发，
  clean 对照静默，审计本身可信）。
- **同基线墨迹扫描**（独立重写实现，advance 宽度，<5px 阈值）：
  分版 1 项、核心 1 项，同一处——P1 目录行
  `Ferienwechsel & Herbst` 与级别标签 `A2→B1`（y=1436，advance gap −4.6）。
  卡面裁图（`crop-p1-sommaire.png`）证实：`Herbst` 真墨迹与 `A2→B1` 之间有
  清晰空隙，属 advance 宽度测量伪影，核心同款，不构成缺陷。
- **P6 图表标签与柱条重叠 0**（实测 + 卡面目视，见 §8 末）：
  柱条起点 x=535；标签墨迹右缘 domicile 506.0（净空 29.0px）、
  service 490.5（44.5px）、retraite 493.3（41.7px）。卡面裁图
  （`crop-p6-chart.png`）三标签完整、与柱条无接触。

## 4. gloss 门（按 `·` 本身拆分，逐项计数）

- 构建文件 gloss 调用：content12.py 1 处×5 项、content34.py 2 处×10 项、
  content56.py 2 处×10 项，**总计 25 项**。
- 与核心逐项 1:1：5 组调用的德语词头在剥离核心中文释义后逐字相等
  （`der Tankrabatt`、`die Zapfsäule`、`die Energiesteuer`、
  `die Mehrwertsteuer`、`der Angehörige`；`der Ferienwechsel`、
  `die Schülerin`、`der Ausflug`、`der Advent`、`die Lesung`；
  `die Englische Woche`、`auswärts`、`empfangen`、`der Favorit`、
  `eröffnen`；`der Pausenhof`、`die Klassenarbeit`、`das Referat`、
  `ausschlafen`、`die Probe`；`der Angehörige`、`die Pflegeversicherung`、
  `der Pflegedienst`、`die Stagnation`、`der Aufschwung`——
  `der Angehörige` 在核心与分版中均为 2 次，无增删合并）。
- 渲染存续：25 项德语词头 + 法文释义全部在最终 SVG 文本中在位。
  分组形态为 5+10+10（与 de-en/de-es 的 5 盒×5 不同，以总数与词头为准，已核实）。

## 5. P7 金句门（从 SVG 几何独立提取，非构建代码）

- 8 句德语原文在全刊 SVG 文本（空白归一化）中**恰为 2×**（源文章＋P7 表），
  与核心计数一致。
- P7 表内页码标签按栏位配对（x=65/527/989/1451 四栏 × 两行）：
  句 1 Seite 4·B1、句 2 Seite 2·A2、句 3 Seite 2·A2、句 4 Seite 5·B1、
  句 5 Seite 3·A2、句 6 Seite 4·B1、句 7 Seite 6·B2、句 8 Seite 6·B2。
  合计 Seite 2×2、3×1、4×2、5×1、6×2；等级 A2×3、B1×3、B2×2——
  与构建员所述分布逐项相符。

## 6. 家具三方对照（本版 / W43 已发同配对 / README #20）

- **W43 已发同配对 SVG 逐字胜出**：P1 配对徽章元素与 W43 de-fr
  **逐字节一致**（含全部属性）：
  `<text x="975" y="372" font-family="Noto Sans CJK SC" font-size="20"
  font-weight="700" fill="#a4553a" text-anchor="middle">TEXTE EN ALLEMAND ·
  EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES</text>`。
  未用 README #20 的法语作目标语泛化值（(975,574) 22pt 情形仅适用于
  FR/IT 作目标语的 family——其 y=372 为冻结 strapline 故须另插徽章；
  本版目标语为德语，DE 核心在 y=372 有原生副标题槽位，徽章原位替换，
  W43 de-fr 已如此 shipped）。注：#20 泛化文字称 EN/DE/ES 槽位情形为
  19.5pt，但 W43 de-fr 实际 shipped 为 20pt；按“W43 逐字胜出”规则，
  本版与 W43 的 20pt 一致为正确，不构成缺陷。
- **8 页页脚齐全**：每页
  `Die Lucerna · HEBDOMADAIRE ALLEMAND VOL.2 · TEXTE EN ALLEMAND ·
  EXPLICATIONS EN FRANÇAIS` + `Page N sur 8`（N=1..8），VOL.2 每页齐全。
- **masthead**：P1 `Die Lucerna`（168pt，目标语德语冠词），正确；
  法语冠词不适用。

## 7. 读者园地强制项（es-ru 教训，P7 右栏）

P7 页上三事实 + 显性征集 + 示例标注全部在位（SVG 文本 + P7 卡面目视双重核实）：

- **示例标注**：`Un exemple de la rédaction !`（法语标点空格，见 §11 注 3）。
  示例德语正文冻结，落款 `Viele Grüße — die Redaktion`，**无编造来信、无编造人名**。
- **无真实来信**：法文注文 `Aucune vraie lettre ni aucun meilleur texte de page 8
  reçu ; suite en VOL.3.`（2 行式）+ 德语冻结句
  `Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3.`。
- **无最佳 P8 作文**：同一法文注文中的 `ni aucun meilleur texte de page 8 reçu`
  覆盖。
- **示例＋承诺顺延 VOL.3**：示例标注 + 德语冻结 invite
  `Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten
  Briefe drucken wir in VOL.3.` + 法文注文 `suite en VOL.3.`。
- **显性公开征集句（独立判定：构成显性征集）**：P7 页上原文
  `Écrivez-nous vos vraies lettres — les meilleures paraîtront dans VOL.3.`
  （2 行式，卡面目视在读者框内完整）。祈使 `Écrivez-nous` + 限定
  `vos vraies lettres`（直指真实来信，非泛泛“写信”）+ 刊登承诺
  `les meilleures paraîtront dans VOL.3.`，三要素齐全，是显性公开征集，
  非暗示。内容预告栏与他页投稿提示未计入本项。

## 8. 构建员自修复（KIT §8，8 项）与终版几何审计 11 项新标记——逐项复核

| # | 修复点 | 独立复核结果 |
|---|---|---|
| §8.1 | P7 读者框公式续行陷阱（整块 5 行替换） | 读者框德语 invite 全文在位；P7 无悬空续行；渲染零 IndentationError 证据见构建日志与终版 SVG 文本完整 |
| §8.2 | P7 右栏超长 → col3 ends 1504.5 | 规则线实测 y=1508.0；右栏末行基线 1490.72（20.5pt）；盒底 1504.5，净空 3.5px；卡面裁图（`crop-p7-col3-rule.png`）工具箱框与规则线无接触（见 §9(a) 裁定） |
| §8.3 | P2 右栏越线 → 2 行式 | `Vous conduisez ? Le prix de l'essence chez / vous ? Écrivez deux phrases en allemand !` 2 行在位（法语问号/感叹号前空格为正确法语标点，见 §11 注 4） |
| §8.4 | P3 右栏越线 → 2 行式 | `Lisez-vous plus en automne ? Votre livre / de chevet ? Écrivez en allemand !` 2 行在位 |
| §8.5 | P4 右栏越线 → 2 行式 | `Qui soutenez-vous ? Qui gagne samedi ? / Écrivez deux phrases en allemand !` 2 行在位 |
| §8.6 | P1 头条流溢出 → 1555、零溢出 | Fragen 结尾行 `Les cinq questions qui agitent l'Allemagne.` 在位，实测宽 395.8px < 412px 内宽；卡面裁图（`crop-p1-fragen.png`）行尾框内留白充足；终版审计 0 flags |
| §8.7 | Partizip II 术语恢复（3 处） | 见 §11 注 1：诊所行 `Au Perfekt, le Partizip II va à la fin.` 在 P7 页身；另两处为练习注文，分别在 P8 键 93 与 101（`passif : wird + Partizip II`）在位；三处全部恢复 |
| §8.8a | P1 Fragen 出页 → 短式 | 长式 `Les cinq questions qui agitent l'Allemagne cette semaine.` 全刊 absent；短式在位 |
| §8.8b | P3/P5 FERIENWECHSEL 超宽 → `FERIENWECHSEL · Vacances` | 两页均在位，长式 absent |
| §8.8c | P3 HERBSTWÖRTER 超宽 11.8px → `HERBSTWÖRTER · Automne` | 在位，长式 absent |
| §8.8d | P6 DIE ZAHLEN 超宽 22px → `DIE ZAHLEN · Chiffres` | 在位，长式 absent |
| §8.8e | P6 免责声明单行出页 → 短式 | 单元素行 y=1656，实测 advance 宽 1705.83px < 1820px 可用宽；`(Exemple d'exercice, pas une vraie enquête.)` 在位 |
| §8.8f | P6 图表三标签压盖（含 27%/21% 亚阈值两项） | 短式 `domicile / service / retraite` 在位；实测净空 29.0/44.5/41.7px；卡面裁图三标签完整无压盖；**审计不触发不等于目视通过——本次已目视通过**（P6 整页卡面亦复核：德语行 `pflegen Angehörige zu Hause / nutzen einen Pflegedienst / leben im Pflegeheim` 与法文短标签、柱条、百分比 68/20/12% 全部清晰） |
| §8.8g | P7 金句 7 译文 3 行压诊所规则线 → 2 行 | `L'économie allemande sort lentement de la / stagnation ; la reprise ne se porte pas seule.` 2 行在位 |

终版审计 0/0/0 与上述修复一致；初版 11 项新标记无一残留（长式全刊 absent、
短式全部在位、几何全部实测）。

## 9. 构建员称非缺陷的三点——独立裁定（非指令，系校对员判定）

- **(a) P7 col3 ends 1504.5 距规则线 1508 仅 3.5px——可接受。**
  实测：规则线 y=1508.0（x 65–1885）；右栏末行基线 1490.72，盒底 1504.5，
  净空 3.5px；真墨迹底约 1496，墨迹净空约 12px，无接触、无穿越。
  DE×EN 同胞版构建日志亦为 `P7 col3 ends 1504.5`，完全一致，属设计贴线，
  非溢出。**裁定：接受，非缺陷。**
- **(b) P6 图表法文标签取短式——完整形式已核实在位。**
  domicile → `soins à domicile`（P6 页身节头 `Qui soigne à domicile ?`、
  文章 `Soins à domicile : …` 及 P8 注 83/89/91）；
  service → `service de soins`（P6 gloss 框断行拼接
  `der Pflegedienst = service de soins` 及 P8 注 84）；
  retraite → `maison de retraite`（P6 图表练习注文 86/87，印于 P8 答案注；
  P6 页身图表行德语 `leben im Pflegeheim` 与短标签并列，读者可映射）。
  **裁定：接受，非缺陷。**（注文按本管线语义印于 P8，见 §11 注 2。）
- **(c) P1-fussball/quiz 底限贴线为核心同款 benign——已核实与核心几何一致。**
  P1 坐标级对照：核心 146 处文本 placement 在分版中坐标完全相同，
  移动 0 处，缺失 23 处恰为冻结差分中的讲解层/家具串；
  末 8 行文本（至基线 2510.35 < 2540）两版逐行同坐标。
  所谓“底限贴线”实为 flow 游标值，非末行基线；实际末行基线在底限之上，
  且与核心完全相同。**裁定：接受，非缺陷。**

## 10. PDF 与交付物

- **印刷版** `Die-Lucerna-VOL2-FR.pdf`：8 页，4,140,964 B，
  sha256 `b3aa075ce5072a0f3da851180706c1e6cb9b7c99eecb08aaefd22b944b22e5f6`——
  实测与构建员所述完全一致；页尺寸 1462.5×2025 pts；P1 文本抽取含徽章、
  masthead 与头条。
- **网页版** `Die-Lucerna-VOL2-FR-web.pdf`：8 页，4,171,068 B（<10 MB），
  sha256 `684a973a7f8dbd79b8c0457229b0be879e932bc30174e19b652bec3891781156`——
  实测一致；页尺寸 1400×1938 pts。
- **SVG 哈希**（8/8 与 KIT §9 一致）：
  p1 `eb835c9b…aa7810`、p2 `6e92c84f…e69b7`、p3 `b37d331d…3f21e`、
  p4 `9ac914b8…2ba78b`、p5 `6f5f8829…60bb`、p6 `c07f4a5c…bc11f`、
  p7 `c1af3967…8757`、p8 `6a21d613…c9cc`（全值见 `edition-hashes.txt`）。
- **卡片×8**：全部 1950×2700 PNG，字节数与 KIT §9 逐一相符
  （p1 1,270,120 / p2 854,076 / p3 833,248 / p4 1,168,536 / p5 775,039 /
  p6 818,529 / p7 720,443 / p8 1,273,779），**8 张全部目视，无缺陷**。
- **ABSTRACT.txt**：法文单行（仅尾换行），无 ASCII 双引号，含
  `Die Lucerna VOL.2`、德语名、A2 à B2、150 exercices、本期真实主题关键词
  （足球周：Ligue des champions / Ligue Europa / 9e journée de Bundesliga；
  Tankrabatt 14,04 centimes par litre jusqu'au 31 décembre；soins à domicile；
  changement de vacances；ZEW）＋学习者搜索短语
  `apprendre l'allemand en lisant`。
- **“桥接”一词**：KIT 与全部 8 个 SVG 中出现 0 次；ABSTRACT.txt 0 次、
  中文字符 0。KIT 本身中文 prose（1995 个中文字符）为构建员记录语言，
  非版面内容，不计入本项。
- **交付文件未改动**：校对结束时分版 SVG 哈希与开工时逐一相同
  （`EDITION_UNCHANGED`），核心 mtime 与哈希均未变。

## 11. 澄清项（非缺陷，系措辞/位置说明，供协调员备查）

1. **Partizip II 三处的“位置”**：KIT §8.7 称“P6、C7 P7 各 1 处”易误读为
   P6/P7 页身。实测：P6、P7 页身均无 `passif : wird + Partizip II` 字面串
   （页身仅有 P7 诊所行 `Au Perfekt, le Partizip II va à la fin.` 与
   `Es wird gespielt. = On jouera (passif)`）。三处中的两处是练习注文，
   按本管线设计注文只印于 P8 答案注：P6 练习 → P8 键 93，P7 练习 → P8 键 101，
   两处 `wird(passif : wird + Partizip II)` 均在位。故三处全部恢复，
   KIT 措辞指练习定义来源，不指页身位置。
2. **注文的可见位置**：同理，P6 图表练习的完整形式注文（83–87）印于 P8
   答案注而非 P6 页身；§9(b) 的核实即按此语义判定。
3. **读者框标签标点**：KIT §7 转录 `Un exemple de la rédaction!`（无空格），
   终版 SVG 实际为 `Un exemple de la rédaction !`（感叹号前有法语标点空格），
   属正确法语排版，非不一致。
4. **UND SIE 法文提示标点**：初查以无空格形式（`conduisez?`）匹配曾得假阴性；
   实际渲染为法语规范 `Vous conduisez ? … en allemand !` 等，断行后仍为
   2 行式，§8.3–8.5 全部成立。
5. **README #20 的 19.5pt 泛化值**：见 §6——W43 shipped 20pt 胜出，本版与 W43
   一致。

## 证据文件（本校对轮内写盘，仅限 proof 目录）

- `hidden_files/w45/de-fr-proof/REPORT.md`（本报告）
- `hidden_files/w45/de-fr-proof/freeze-baseline.log`、`freeze-diff.log`、
  `freeze-diff.json`、`p8-compare.log`、`p8-compare.json`、`p8-ed.json`、
  `p8-core.json`、`occlusion.log`、`occlusion.json`、`occlusion-core.log`、
  `core-hashes-before.txt`、`core-hashes-after.txt`、`edition-hashes.txt`
- `hidden_files/w45/de-fr-proof/crop-p1-sommaire.png`、
  `crop-p6-chart.png`、`crop-p7-col3-rule.png`、`crop-p1-fragen.png`
- `hidden_files/w45/de-fr-proof/baseline-core/`（核心基线复现输出）
