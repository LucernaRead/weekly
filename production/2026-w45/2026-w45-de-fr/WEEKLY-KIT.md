# Die Lucerna VOL.2 — DE × FR (W45) — WEEKLY-KIT

**状态：builder-complete，未定稿，待独立校对。** 本文件为构建员自测记录，不作定稿宣称。
未发 Discord，未往主聊天发卡片/PDF，未碰 weekly-git；核心目录与 W43 目录只读。

## 1. 配对与底本

- 配对：目标语德语（DE）× 读者母语法语（FR）。德语正文全部冻结，讲解层全部改写为直接写给法语母语读者的法文。
- 底本：W45 DE 核心 `files/weekly-report-w45-de-core/`（Die Lucerna VOL.2，已定稿上架；150 题；A2 66 / B1 70 / B2 14；分页 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38）。
- 对照：W43 已发 DE×FR `files/weekly-report-de-fr/`（VOL.1）。
- 刊期：2026 年 11 月 2–8 日当周（Woche vom 2. bis 8. November 2026）。
- 构建树：`hidden_files/weekly-report-w45-de-fr-build/`（bslib4.py、svglib.py、run.py、render.py、transform.py、dump_reg.py、reg.json、build-log.txt、render-log.txt、p8-compare.txt、occlusion-edition2.txt、verify-final.txt、rowcheck.txt）。
- 方法：变换用整行或精确唯一字面量＋计次断言；值映射用裸文本；单进程重渲染（content 模块共享注册表须同一 driver 进程）；渲染一律用 `tools/venv/bin/python`。

## 2. 冻结对照（freeze.py）

- 核心 8/8 基线复现（byte-identical）；核心开工前哈希与最终哈希完全一致，diff 输出 CORE-UNCHANGED：
  - p1-front `6cbd48022b5f863d941aa422869639ddc2ad2cbd203169ba87b85ba0d4fade3e`
  - p2-leben `9362256dca74f8772f3e45944e1e137c487d68e5a3fca772f93bf47e7b4b6d22`
  - p3-kultur `3e8a8d16136a46a3781df045944f20eb821e0dba9b872e4f1ecc10758660ae9d`
  - p4-sport `b787f592599cc4d1f862c16d901766e9775e5eac82330156617a04665cb0199d`
  - p5-jugend `4dcbeb97c566f4dfb56e5cb7a6e97556f2f97246d97656e0b3f81c173decb77c`
  - p6-vertiefung `01b75ad49a54c8037c15b885279aca9fcd530e815633eda7d1e1f79e2233090b`
  - p7-sprache `fbaf8cdd8a90f2994f4ecc4a769f64d717813c38e36acec74507c3aa162f278c`
  - p8-uebungen `299524bd2ad25ec447c0f422166b3db344b3caeba127e061fce37dc1e3c13891`
- 最终差分（文本元素，含换行差异）：P1 +23/−23、P2 +36/−32、P3 +40/−40、P4 +25/−22、P5 +44/−39、P6 +37/−33、P7 +60/−54、P8 +159/−141。新增中文字符 0（核心中文字符 168/186/187/155/193/228/394/1429 → 分版 0/页）；最终 SVG 中文字符总数 0。
- P1–P7 德语正文多重集冻结裁定（整串级差分，只看不含中文字符的移除串）：
  - P1：仅 1 串——任务规定的副标题行被配对徽章替换（见 §6）。
  - P2、P5：不含中文字符的移除串为 0。
  - P3、P4、P6：各仅 1 串 `。`——中文 gloss 末尾孤悬句号元素，法文版以 `.` 结尾故无此元素，属讲解层标点伪影，非德语正文。
  - P7：4 串，均为讲解层（编辑部示例标签、词框整行改写为德语词头＋法文释义、中文省略号换行伪影）。
  - 含中文串德语词存续补查（最终 SVG 重跑）：P7 缺失词仅页脚英文段 `LUCERNA / GERMAN / WEEKLY`（页脚改法文所致，已备案）；P6 `Argumente` 一处属节头讲解层（`PRO & CONTRA · 正方与反方 — die Argumente der Debatte` → `PRO & CONTRA · Pour et contre — les arguments du débat`，仿 DE×EN 同胞版），已备案。
- P8 仅分隔符差异：分隔符改为 `— Page {pg} —`，答案键格式改为半角括号 `(note)`、13pt、行距 1.26（W43 de-fr 构建码实测；核心为全角括号、14.5pt、1.3）。最终 P8 全角括号数 0，分隔符 8 处。
- 新增讲解语言外字符备案：无。法文层字符均为法语/德语正文所需（é、è、à、ç、ü、ß 等）；无中文字符残留。

## 3. P8 对照（tools/p8.py compare）

- **CLEAN：150 noted = 150 noted，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 150]**。
- 逐项判定（全部为真改动，无括号/dash 提取伪影）：
  - 137：核心中文键 → 分版 `La réduction du carburant dure jusqu'en décembre.(laufen = durer)`——DE→FR 重定向。
  - 138：核心中文键 → 分版 `Je regarde le football mardi.(schauen = regarder)`——DE→FR 重定向。
  - 139：核心中文键 → 分版 `L'école a repris.(wieder begonnen = avoir repris)`——DE→FR 重定向。
  - 140（不在 keydiff 中，正确）：键德语 `Am Sonntag schlafe ich eine Stunde länger.` 保持不变；提示改为法文 `Je dors une heure de plus le dimanche.`，指令 `Traduire en allemand`，注 `dormir une heure de plus = eine Stunde länger schlafen`——反向题键已核实。
  - 150：写作登记行改为法文 apparatus（`Tâche ouverte — suivez les points du cadre d'écriture; le texte modèle est dans le cadre de cette page`＋注 `Noté selon les points listés`），范文德语正文未动。
- P8 答案注文全部为法文；题号连续 1–150；登记表（dump_reg.py 单进程导出）：总数 150，分页 10/18/18/18/18/18/12/38，级别 A2 66 / B1 70 / B2 14（与核心一致，B2 仅 14 属实，未重定级）；题型 QCM 52、à compléter 41、transformation 11、appariement 12、vrai/faux 8、texte à trous 8、construction de phrase 8、dialogue à compléter 5、traduction 4、rédaction 1。

## 4. 几何审计（tools/occlusion_audit.py）

- 最终：**分版 0 flags、核心 0 flags、NEW 0 flags**（初版 11 项新标记全部修复，见 §8）。
- 同基线墨迹扫描（rowcheck.py，advance 宽度，<5px 阈值）：分版 1 项、核心 1 项，同一处——P1 目录行 `Ferienwechsel & Herbst` 与级别标签 `A2→B1`（y=1436）。卡面裁图复核：该行真墨迹间距充足，属 advance 宽度测量伪影，核心同款，不构成缺陷。
- P6 图表专项：柱条 68% / 20% / 12%，标签德语＋法文短式；标签墨迹右缘 506.0 / 490.5 / 493.3，均 < 柱条起点 535，文本与后绘矩形重叠 0。
- 最终渲染几何（零 FLOW OVERFLOW / HEAD TOO WIDE 警告）：P1-headline ends 1555（底限 1828）；P2 col3 box4 ends 1550.66；P3 col3 ends 1583.66；P4 col3 ends 1135.25；P5 col3 ends 1417.07；P6 col3 ends 1320.33；P7 col3 ends 1504.5（金句区规则线 1508，净空 3.5px）；P8-battery y=1500（底限 1505）；P8-keys y=2336（底限 2560）。P1-fussball y=2298（底限 2290，末字形底约 2259）与 P1-quiz y=2552（底限 2540）为核心同款 benign 情形。

## 5. gloss 计数（README #21：按 `·` 本身拆分）

- content12.py：1 处调用，核心 5 项 → 分版 5 项；content34.py：2 处调用，核心 5+5=10 项 → 分版 10 项；content56.py：2 处调用，核心 5+5=10 项 → 分版 10 项。**总计 25 项，逐项 1:1，不得增删合并；每项德语词头在渲染中存续。**
- gloss 前缀：`Note — `（W43 de-fr 构建码 bslib4.py gloss 方法实测）。
- P7 金句逐字核对：8 句德语原文在全刊 SVG 文本中恰为 2×（源文章＋P7 表），页码标签分布：Seite 4 · B1（句 1）、Seite 2 · A2 ×2（句 2–3）、Seite 5 · B1（句 4）、Seite 3 · A2（句 5）、Seite 4 · B1（句 6）、Seite 6 · B2 ×2（句 7–8）；法文译文为新讲解层，德语引文本身冻结。

## 6. 家具三方对照（本版 / W43 已发同配对 / README #20）

- **W43 已发同配对 SVG 逐字胜出。** P1 配对徽章实测（本版与 W43 de-fr 元素逐字节一致）：
  - 文本：`TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`
  - 槽位：x=975（居中）、y=372（替代核心副标题行原位）；字号 20pt；sans 粗体（font-weight 700）；颜色 BRICK `#a4553a`。
  - 注意：README #20 中关于法语的 (975,574) 22pt 描述的是法语作目标语的情形，不是法语作读者语的情形——DE×FR 以 W43 de-fr 实测为准，未采用 #20 泛化值。
- 页脚（全部 8 页齐全）：`Die Lucerna · HEBDOMADAIRE ALLEMAND VOL.2 · TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS`；页码行 `Page N sur 8`（N=1..8）；VOL.2 每页齐全；P1 徽章齐全。
- masthead：目标语为德语，故用 `Die Lucerna`（见核心）；法语 masthead 文章按目标语惯例——本版不适用法语冠词。
- P1 版头行（46pt serif 粗体，实测宽 1516.4 < 1820 可用宽）：`JOURNAL ALLEMAND · VOL.2 · FOOTBALL · CARBURANT · SOINS`。
- P1 顶条中段（21pt，实测宽 940.2）：`WÖCHENTLICH AUF DEUTSCH · CHAQUE SEMAINE · L'ALLEMAND QUE LISENT LES ALLEMANDS`。
- W43 DE×FR 题型／指令词汇照抄：à compléter、QCM、construction de phrase、transformation、vrai/faux、texte à trous、appariement、dialogue à compléter、traduction、rédaction；Compléter、Former une phrase、Relier les paires、Réécrire、Vrai ou faux?、Traduire en français、Traduire en allemand。
- W43 DE×FR 栏目法文短式照抄：LEBEN · Vie；KULTUR · Culture；SPORT · Sport；JUGEND · Jeunesse；VERTIEFUNG · Approfondissement；SPRACHE · Langue；DER WERKZEUGKASTEN · Outils；LESERBRIEFE · Vos lettres；NOCH EIN WORT · Un mot de plus；SÄTZE DER WOCHE · Phrases de la semaine；IN DER NÄCHSTEN AUSGABE · Au prochain numéro (VOL.3)；P8 各节 Texte à trous、Quiz、Lecture、Phrases、Traduction、Les paires、Dialogue、Rédaction；MUSTER · Texte modèle (84 mots)；ANTWORTEN · Toutes les réponses commentées (pages 1 à 8)。

## 7. 读者园地（P7 右栏，强制项）

- 标签（编辑部示例标注）：`Un exemple de la rédaction!`
- 德语 defer（冻结）：`Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3.`
- 德语示例（冻结）：`„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die Fußballwoche ist toll! Viele Grüße — die Redaktion“`
- 德语 invite（冻结）：`Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten echten Briefe drucken wir in VOL.3.`
- 法文注文（2 行，与标签合计覆盖三事实：示例、无真实来信、无最佳 P8 作文、承诺顺延 VOL.3）：`Aucune vraie lettre ni aucun meilleur texte de page 8 reçu; suite en VOL.3.`
- **法文显性公开征集句原文（P7 页上，内容预告栏与他页投稿提示不计入）：`Écrivez-nous vos vraies lettres — les meilleures paraîtront dans VOL.3.`**
- 最终 P7 SVG 中上述五片段全部 present 已验证；示例未冒充真实来信，无编造人名／引言。

## 8. 自修复清单（本构建轮内发现并修复，全部经重渲染＋重跑门确认）

1. **P7 读者框公式续行陷阱**：核心 rh 公式占 5 行；初版变换只替换首行，留下悬空续行导致 IndentationError。改为整块（5 行）替换；读者框公式尾部用 +32（fix1 的 +16 再加 +16，对应 note＋invite 两个新增段落，与 DE×EN 一致）。
2. **P7 右栏超长**：初版 P7 col3 ends 1736.0，压过金句区规则线 1508。逐步缩短后定为 1504.5（与 DE×EN 完全一致）：工具箱 3 项改为 1 行式（`rund 8,35 Euro = environ 8,35 euros`；`Meiner Meinung nach = À mon avis`；`Es ist fraglich, ob = Il est douteux que`）；读者注文最终 2 行式；征集句最终 2 行式。
3. **P2 右栏越线**：UND SIE 提示法文 3 行致 box4 ends 1579.66，压过 Rechnen 宽框固定金线 1554。缩短为 2 行式 `Vous conduisez? Le prix de l'essence chez vous? Écrivez deux phrases en allemand!`，恢复 box4 ends 1550.66（与核心一致）。
4. **P3 右栏越线**：UND SIE 提示法文 3 行致 col3 ends 1612.66，压过练习区金线 1608。缩短为 2 行式 `Lisez-vous plus en automne? Votre livre de chevet? Écrivez en allemand!`，恢复 col3 ends 1583.66。
5. **P4 右栏越线**：UND SIE 提示法文 3 行致 col3 ends 1164.25，压入固定赛程表首行矩形（y=1156 起）。缩短为 2 行式 `Qui soutenez-vous? Qui gagne samedi? Écrivez deux phrases en allemand!`，恢复 col3 ends 1135.25。
6. **P1 头条流溢出**：法文讲解行＋数字框行数增长致 `FLOW OVERFLOW [P1-headline]`、flow ended 1921。缩短三处后恢复 1555、零溢出警告（讲解行去掉同义重复的 Bundesliga 段；数字条 1、3 各压回 2 行）。
7. **德语语法术语恢复（W43 DE×FR 惯例）**：初版把 3 处注文中的 `Partizip II` 译为法文；已恢复为德语术语，法文框架保留：`passif: wird + Partizip II`（P6、C7 P7 各 1 处）；`Au Perfekt, le Partizip II va à la fin.`（P7 纠错诊所）。恢复后几何未变；P7 含中文串德语词补查重跑归零（仅页脚英文段备案）。
8. **几何审计 11 项新标记（最终轮）**：P1 Fragen 结尾行出页（→ `Les cinq questions qui agitent l'Allemagne.`，375.8px < 412px 内宽）；P3/P5 FERIENWECHSEL 框题超宽（→ `FERIENWECHSEL · Vacances`）；P3 HERBSTWÖRTER 框题超宽 11.8px（→ `HERBSTWÖRTER · Automne`）；P6 DIE ZAHLEN 框题超宽 22px（→ `DIE ZAHLEN · Chiffres`）；P6 免责声明单行出页（→ `(Exemple d'exercice, pas une vraie enquête.)`，1705.8px < 1820px）；P6 图表三标签被柱条压盖（`maison de retraite` 35% 已触发，另两项 27%/21% 低于审计 30% 阈值未触发——README #12 盲区，三项一并改短为 `domicile / service / retraite`，练习注文保留完整形式）；P7 金句 7 译文 3 行致标签压诊所规则线（→ `L'économie allemande sort lentement de la stagnation ; la reprise ne se porte pas seule.`，2 行）。修复后审计 0/0/0，transform.py 已同步全部修正（含图表标签 bars 行专属后处理）。

## 9. 交付物

- SVG ×8：`svg/p1-front.svg` … `svg/p8-uebungen.svg`（最终 sha256）：
  - p1 `eb835c9b67e77bddc0273f33ed5688280483e66d7a70a44d3ccda4c242aa7810`
  - p2 `6e92c84f665a1a666ada8e857ea80fa8a716a18b799232671064586eea3e69b7`
  - p3 `b37d331de13d2265e6b55c46a260aa62f4d4403c10a845857a2ee03c68c3f21e`
  - p4 `9ac914b8802a51ef800bb1fbcf720047eacaf40257f906cef9c0bfb1102ba78b`
  - p5 `6f5f8829d69c4daa24c0759812f487ac591bce8a172afb0d8435aecaa75760bb`
  - p6 `c07f4a5c8e1def8c48bd7f35f210d6d1d2b5df721c85492f59aef866721bc11f`
  - p7 `c1af3967ed70b0867b4dddb9e3f98ab37d6d046ac981b03513497106edcd8757`
  - p8 `6a21d6130121b68e9b12fa173805e3700ac800a966f5e3d58e0283768bcec9cc`
- 卡片 ×8（1950×2700 PNG）：`cards/` p1 1,270,120 / p2 854,076 / p3 833,248 / p4 1,168,536 / p5 775,039 / p6 818,529 / p7 720,443 / p8 1,273,779 字节。**8 张卡面全部目视，无缺陷。**
- 印刷 PDF：`Die-Lucerna-VOL2-FR.pdf`，8 页，4,140,964 字节，sha256 `b3aa075ce5072a0f3da851180706c1e6cb9b7c99eecb08aaefd22b944b22e5f6`。
- 网页 PDF：`Die-Lucerna-VOL2-FR-web.pdf`，8 页，4,171,068 字节（<10 MB），sha256 `684a973a7f8dbd79b8c0457229b0be879e932bc30174e19b652bec3891781156`。
- `ABSTRACT.txt`：法文单行，无 ASCII 双引号，含刊名 Die Lucerna、目标语德语名、A2–B2 分级、150 题、本期真实主题关键词（足球周：欧冠／欧联／德甲第 9 轮；油价减税 Tankrabatt 14,04 欧分／升至 12 月 31 日；居家护理；假期交接；ZEW）＋学习者搜索短语（apprendre l'allemand en lisant）。

## 10. 事实说明与图片授权（沿用核心，不新增事实）

- 事实（与核心 KIT §4 一致）：赛程（欧冠／欧联／德甲第 9 轮，11 月 2–8 日）、油价算术（14,04 欧分／升；50 升 ≈ 8,35 欧元；2,5 亿欧元级财政成本口径沿用核心）、ZEW（预期 28,1、−6,6 点；现状 −35,9、+11,2 点）、护理节目归因（ARD《Hart aber fair》10 月 26 日）等均未改动；P6 图表数字为编辑部练习示例（非真实调查），免责声明在图下与 P8 注中均有说明。
- 图片授权（沿用核心）：P1 fussball.jpg、P4 kopfball.jpg，DVIDS 公共领域，图说与出处与核心一致，数据 URI 与核心一致。

## 11. 待独立校对注意点（非缺陷，仅供校对员复核）

- P7 col3 ends 1504.5 距金句区规则线 1508 仅 3.5px——与 DE×EN 同胞版完全一致，属设计贴线，非溢出。
- P6 图表法文标签取短式（domicile / service / retraite），完整形式见同页练习注文与 P8 答案注。
- P1-fussball / P1-quiz 的底限贴线为核心同款 benign 情形（末字形底在底限之上）。
