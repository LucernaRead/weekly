# 独立校对报告 — W45 PT × FR（葡萄牙语 × 法语）

**结论：ZERO PROBLEMS**（11 项门禁全部独立重测通过，无阻塞项）

- 待审交付：`files/weekly-report-w45-pt-fr/`（svg × 8、cards × 8、print/web PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-pt-core/`（W45 PT 核心，VOL.2）+ 构建树 `hidden_files/weekly-report-w45-pt-build/`
- 同配对对照：W43 `files/weekly-report-pt-fr/`（只读）
- 开工查重：交付 mtime 止于 2026-10-27 22:25 UTC；90 秒复查零新写盘后开工（无进行中渲染进程）。校对期间未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git（仅只读 `git status`，干净）、未改核心与 W43 目录。
- 本目录证据：`diff.json`、`occlusion.json`、`extra_scans-rerun.txt`、`geom.txt`、`gloss.txt`、`p8-core.txt`、`p8-edition.txt`、`core-svg-before/after.sha`、`edition-before/after.sha`、`baseline-pt/`（freeze 复现输出）、`p8keys.py`、`p8ctx.py`、`geom.py`、`measure.py`、`gloss.py`。

## 1. 冻结（freeze.py，独立重跑）

- `freeze.py baseline`：**8/8 逐字节复现**（p1 `0dc8089d…`、p2 `56db3aa8…`、p3 `82f6fc3a…`、p4 `c5647cf6…`、p5 `92e86020…`、p6 `e6097473…`、p7 `a72cb75a…`、p8 `82630480…`，与交付前哈希一致）；运行后核心重哈希 8/8 不变。
- `freeze.py diff`：新增 CJK **8 页均为 0**（核心 CJK/页 156/177/153/148/223/118/357/1123 → 分版 0）；全文 `桥接` 0（8 页各 0）；`bridge` 0；德语残留 token（Feiertagswochenende / Eingangstore / HINWEIS / Wochenzeitung / Tag 2 ist / Prüfung / Sonntag）8 页均为 0。
- 差分逐项裁定（distinct 字符串 + 拉丁词 token 全覆盖复核）：
  - 无 CJK 的删除串仅 9 条，全部是重排/家具：P1 `12h — os portões abrem no domingo 8（`（葡语片段在分版重排后完整保留，中文注被法语注替换）；P5 `5. Domingo 8: chegue antes das 12h（`（同理）；P6 `chamada · local · conferir`（重排）；P8 8 条键行（键 token 保留，见 §3）；P2 `NÍVEL A2 · Finados e revisão…`（双语标题重排，词全在）。
  - 唯一拉丁词缺失的两条均属家具槽位，非正文丢失：① 各页页脚英文行 `LUCERNA PORTUGUESE WEEKLY` → 法语页脚（W43 同配对先例）；② P1 y=372 葡语标语 `O JORNAL SEMANAL PARA APRENDER — …` → 该槽位在 W43 即为配对徽章（W43：y=372、19pt、徽章文案与本版逐字相同），属家具惯例而非冻结丢失。其余删除串的全部拉丁词均在分版同页文本中出现。

## 2. P7 词框（硬性门）

- 定义句逐字保留，核心与分版在 P7 同坐标（x=1473，y=1187.5/1218.03，21.5pt）两行完全一致：
  - `« feriadão »: sábado, domingo e`
  - `segunda — três dias de descanso.`
  - 合成：`« feriadão »: sábado, domingo e segunda — três dias de descanso.` ✓
- 仅 gloss 本地化：`feriadão = pont de trois jours.`（同坐标 y=1278.56，20pt；核心为 `feriadão = 连休长周末，共三天。`）。定义句无任何本地化，**无冻结失败**。

## 3. P8（p8.py compare，独立重跑）

- `status: CLEAN，150 = 150，missing = []，extra = 0，uncertain = []，keydiff = [2, 4, 101, 137, 138, 146]`。
- 键 token 逐字节对照（印刷法语 key token = 核心）：
  - 2：核心 `portões` / 分版 `portões` ✓（核心注含全角括号分支，p8.py 核心侧取括号前段，属提取分支伪影；分版注 `portões = portes d’entrée du lieu d’examen`，键 token 相同）
  - 4：`13h30` / `13h30` ✓（分版注 `13h30 : début, heure de Brasília`）
  - 101：`confiro` / `confiro` ✓（分版注 `conferir : eu confiro, irrégulier`）
  - 146：`A` / `A` ✓（分版注 `seção = salle d’examen`）
- 137/138 真重定向，合法（翻译题答案语向重定向，W43 KIT 同类模式）：
  - 137：核心 `11 月 8 日周日是高考的第一天。 — 对照第 6 版标题` → 分版 `Dimanche 8 novembre, c’est le premier jour de l’Enem. — cf. le titre de la page 6`（同页交叉引用，语向已本地化）
  - 138：核心 `周日前核对确认卡。 — Confira = 请核对` → 分版 `Vérifiez la carte avant dimanche. — confira = vérifiez`（注中动词用小写词典形 confira，属注写惯例，非键错）
- 139/140：键葡语不变、词干重定向无遗漏：
  - 139 键行 `139. O feriadão é de 31 de outubro a 2 de novembro. — feriadão =` + 续行 `long week-end de pont`（完整）；练习题干（P8 E 区）`« Le feriadão va du 31 octobre au 2 novembre. » → ___`（法语译写完整）
  - 140 键行 `140. Quando você chegar, apresente o documento com foto. —` + 续行 `futur du subjonctif chegar + impératif apresente`（完整）；题干 `« Quand vous arriverez, présentez la pièce d’identité avec photo. » → ___`（跨行完整）
- 150：写作装置全法语 — 题干 `«O seu domingo 8 de novembro» Escreva 80–100 palavras:`（葡语题干保留）+ 装置 `Exercice d’écriture (sans réponse unique) ; le texte modèle (93 mots) est ci-dessous.` + 键 `150. ✓ Texte modèle dans la section H de cette page (93 mots)`；范文与核心逐字相同（见 §10），无错位（卡片目视 H 区范文完整）。
- P8 注释纯法语：分版 P8 CJK 文本节点 0；答案注行（RESPOSTAS 区）括号仅 150 装置行 `(93 mots)` 一处，p8.py CLEAN 证明无提取伪影（其余 16 处括号均在冻结的葡语选择题题干中，非注释）。

## 4. 几何（occlusion_audit.py + 独立补充扫描）

- 工具自检先行通过（6 类 planted flags 各 1 发，clean 对照静默）；分版 **0 flags / 核心 0 flags / NEW 0**。
- builder `extra_scans.py` 独立重跑，结果与 round-3 逐字一致：同基线碰撞 8 页均为 0；P6 图表标签覆盖（基线锚定墨迹法，PIL getmetrics ascent/descent，anchor ls）>0.5% 的文本 0 个，MAX **0.0%**（门 <30%）；框线压框扫描 8 页均为 0 命中。
- 全 8 页框线压框 + 右缘扫描（独立 ADVANCE 法）：advance 右缘 >1910（内框线）的文本 **8 页均为 0**；无 ≤0.5px 边界待裁定项（不存在任何超出）。
- P7 引言 clearance（独立 OA 真实墨迹复测）：预览带 rect (65, 2404, 1885, 2522)；带上最大墨迹底 **2396.17**（末引行 `Vérifier la carte, bien dormir, arriver tôt. (Página 2)` / `Se souvenir, c’est rester proche. (Página 3)`，基线 2391.17）→ 间隙 **7.83px** ≈ 构建员称 7.8px（舍入差 0.03px，非阻塞，见 §12）。
- P2 1897.2 匹配项行：分版与核心**同值** — 同行文本 `d. o objeto que dá luz e se acende em memória` 真实墨迹右缘均为 **1897.2**，内框内 12.8px（1910 − 1897.2）；分版基线 2355.0 vs 核心 2304.0（+51px 为法语注引起的版式下移，墨迹右缘继承不变，非缺陷）。

## 5. gloss（渲染后实测）

- 源 gloss() 串按 `·` 拆分：核心 26 = 分版 26；分布 **P2 6 / P3 6 / P4 5 / P5 5 / P6 4**（渲染页实测映射：P2 首项 `o feriadão = …`、P3 `o túmulo = …`、P4 `a ida = …`、P5 `a reta final = …`、P6 `os portões = …`）。
- 词头逐项 1:1 相同（5 盒全部，核心词头取首个 CJK 前的拉丁部分，分版取 ` = ` 前部分）；渲染归一化全文含全部 26 项，无缺失。
- 前缀：`Note — ` × 5（5 个 gloss 盒）+ P1 `Notes — ` × 1（桥接注）。
- P7 金句 8 句各 2×（标注页 + P7），标签与核心一致且源页实测存在：`Do feriadão à prova`→P1、`Muita gente viaja…`→P1、`Finados é o dia da memória`→P2、`lembrar é um jeito de continuar perto`→P3、`cada ponto vale uma posição…`→P4、`quem dorme bem lembra melhor`→P5、`primeiro as fáceis…`→P6、`Confira o cartão, durma bem, chegue cedo`→P2；P7 标签页码（1/1/2/3/4/5/6/2）与源页一一对应。（注：原始 SVG 跨行断句时须用归一化拼接文本核查，逐行 grep 会误报 3 句缺失，已用拼接法排除。）

## 6. 读者园地（P7 CARTAS DOS LEITORES，零编造）

- 3 事实齐全：
  1. 葡语披露句原文（与核心逐字相同）：`Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3.`
  2. 法语等义句：`Note de la rédaction : ni lettres ni meilleurs textes du VOL.1 avant le bouclage — l’exemple reste, promesse au VOL.3.`（无真实来信、无 VOL.1 最佳文本、示例保留 + VOL.3 承诺，三事实齐全）
  3. 编辑部示例标注：`— EXEMPLO DA REDAÇÃO` + `Exemple de la rédaction.`；示例句 `«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!»` 无署名、无虚构读者。
- 显性法语邀请（逐字摘录，渲染形含法语标点前空格）：`Exemple de la rédaction. Écrivez-nous ! Les meilleures paraîtront au VOL.3.` — 祈使句 `Écrivez-nous !` + VOL.3 刊登承诺 `Les meilleures paraîtront au VOL.3`，**判定：合格邀请**；下期预告行（`A PRÓXIMA SEMANA · LA SEMAINE PROCHAINE (VOL.3)` 带）未计入邀请。

## 7. 家具（与 W43 同配对实测对照）

- 版面行：40pt serif-bold（核心字号保留，W43 为 36pt）法语行 `JOURNAL PORTUGAIS · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE` 独立实测 advance **1732.14px** ≈ 构建员称 1732.1px，≤1820 ✓；居中 108.9–1841.1，内框内。
- P1 徽章：y=372、19pt，与 W43 文案逐字相同：`TEXTES EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`；顶带与 W43 逐字相同：`TODA SEMANA EM PORTUGUÊS · CHAQUE SEMAINE · LE PORTUGAIS QUE LIT LE BRÉSIL`。
- P8 分隔符：`— PÁGINA {pg} —` 形式，PÁGINA 1–8 齐全（W43 先例，非 README 的 `— Page {n} —` 形；页码行仍为法语 `Page N sur 8`）。
- ERROS 标题：`ERROS COMUNS · ERREURS`（23pt）；全长形 `ERROS COMUNS · ERREURS FRÉQUENTES` 独立实测 bold 23pt **480.75px** ≈ 构建员称 480.8px，确超 390px 盒内宽；缩短形实测 regular 23pt **309.44px**（bold 323.09px），右缘 1782.4 < 盒右 1885，余量 102.6px ✓。
- 数字盒标题：21pt bold（核心 23pt → 分版 21pt，与 W43 相同）；`A SEMANA EM NÚMEROS · CHIFFRES` 实测 advance **383.14px** ≈ 构建员称 383.1px，右缘 928.14 < 盒界 961.0 ✓。
- palavra 盒：x=1451、y=1098.5、w=434 不变，高 **184 → 188（+4px）**，与核心实测一致；gloss 行墨迹底独立实测 1283.56 < 新盒底 1286.5，余量 2.94px（见 §12 舍入差）。
- 页脚：8/8 均为 `A Lucerna · HEBDOMADAIRE PORTUGAIS VOL.2 · TEXTE EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS`（VOL.2 随核心，W43 为 VOL.1）；页码行 8/8 `Page N sur 8`。
- P8 注释缩短：KIT §5 所列 11 条缩短注全部在版且语义完整（15/30/31/48/69/81/88/98/131/144 + 13/80/92 共享卡注）；48/81 的补充子句取舍见 §12 观察（答题依据完整）。

## 8. 图片

- 仅 P1 一图：其余 7 页内嵌图 0；P1 base64 载荷 **342,316 字符**，与核心逐字节同（解码 256,737 字节，md5 `04b18fa952a61c9998ef5bf3325341f2`，核心与分版一致）。
- 署名在版：P1 (65, 2271.3) `Foto: Gary Todd / Wikimedia Commons — CC0`（Commons Artist 字段口径，与核心一致）；P1 卡片目视照片 + 图说 + 署名齐全。

## 9. ABSTRACT

- 文件 351 字节，单行（1 个换行符为行尾），无 ASCII 双引号 `"`。
- 全文：`A Lucerna VOL.2, hebdomadaire portugais pour lecteurs francophones : la semaine de l’Enem, Finados et le pont du 2 novembre, les matches retour de la Copa do Brasil, 150 exercices A2–B2 pour apprendre le portugais du Brésil, réviser le pretérito perfeito et le futur du subjonctif — comment dire feriadão et conferir o cartão en portugais.`
- 含刊名、目标语名、A2–B2、题数 150、真实主题关键词（Enem / Finados / pont du 2 novembre / Copa do Brasil）与学习者搜索短语（`apprendre le portugais du Brésil`、`comment dire feriadão … en portugais`）✓。

## 10. 卡片目视 + 题量（独立展开计数）

- 8 张卡片逐页目视（1950×2700 PNG）：无重叠、无截断、无压框、无页脚侵入；P7 词框/读者园地/金句带、P8 评估 + 范文 + 答案区均完整；页脚 VOL.2 与 `Page N sur 8` 逐页可见。
- 题量独立展开计数（渲染题号 + 构建源登记）：
  - 渲染题号：P1 1–10（10）、P2 11–28（14 独立号 + 25–28 配对 inline = 18）、P3 29–46（18）、P4 47–64（14 + 52–55 配对 = 18）、P5 65–82（18）、P6 83–100（18）、P7 101–112（12）、P8 113–150（34 + 141–144 配对 = 38）；连续 1–150，无缺重。
  - 级别：源登记 `ex()` 138 项（A2 45 / B1 66 / B2 27）+ 3 组 `match_set` 各 4 项（A2 / B1 / B2 各 +4）= **A2 49 / B1 70 / B2 31，总计 150** ✓（与任务给定的 PT 核心数一致；任务括号内 “B1 72?” 之问以核心实测 70 为准）。
- 范文：分版与核心逐字相同，排除标签 `Texto modelo:` 后 **93 词**（`Domingo, 8 de novembro, … domingo 15.`）；P8 键注 `(93 mots)` / `(93 词)` 一致。

## 11. 校对前后哈希不变

- 核心 SVG：校对前后 sha256 逐项一致（`core-svg-before.sha` = `core-svg-after.sha`）。
- 分版 SVG + cards：校对前后 sha256 逐项一致（`edition-before.sha` = `edition-after.sha`）。
- PDF：print `A-Lucerna-VOL2-FR.pdf` 8 页、3,470,958 B、sha256 `545d6849cd6df0d5788f927eda2f3e6a79024c1f73f7b2beea8e888666702f4d`；web `A-Lucerna-VOL2-FR-web.pdf` 8 页、3,471,235 B、sha256 `28965e764e220d6fe4d03aec7f95c7c7eb4dfdf12c1bbfb64cf4afe9af041c22` — 与任务给定值一致。
- 共享 scratch 目录未清理；W43 目录与 weekly-git 未改动。

## 12. 与构建员自述不符处（均非阻塞）与非阻塞观察

1. palavra gloss 墨迹底：构建员称 1283.3，本独立 PIL（anchor ls）实测 **1283.56**（+0.26px）；新盒底 1286.5 下余量 2.94px（非其隐含的 3.2px），结论同为通过。
2. P7 引言间隙：构建员称末引墨迹 2396.2，本独立 OA 真实墨迹实测 **2396.17**，间隙 7.83px（非 7.8px 舍入值），结论同为通过。
3. P2 1897.2 行基线：分版 2355.0 vs 核心 2304.0（+51px 版式下移）；构建员“冻结继承”指墨迹右缘值继承（已证同值），非基线坐标继承。
4. 邀请渲染形：KIT 行文作 `Écrivez-nous!`，渲染实测为法语标点形 `Écrivez-nous !`（感叹号前空格），符合法语排版，判定不变。
5. KIT §4 “P8 注释无括号”字面 scope：P8 全页括号 17 对，但 16 对在冻结葡语选择题题干、1 对在 150 装置行 `(93 mots)`；答案注行本身无括号分支，p8.py CLEAN 佐证无提取伪影。字面表述宜收窄为“答案注行”，不影响结论。
6. KIT §8 措辞 “139/140 词干 FR→PT 重定向”：P8 键行词干在核心与分版均为葡语；实际重定向发生在 P8 E 区练习题干（核心中文译写 → 分版法语译写），已逐项核实完整。措辞问题，非内容问题。
7. P8 缩短注 48/81 的补充子句：48 核心注含 “周日 8 日 17 点，圣雅努阿里奥”，分版注仅保留 fixture + 日期；81 核心注双子句（突击非好计划 + 每天复习一点好），分版注仅保留后半句。答题依据（48 的日期选项、81 的 Falso 判断）完整，且 17h/圣雅努阿里奥等细节在 P4 题干与正文在版；不构成内容丢失，列为观察。
8. tables.py 通用家具表对 fr/pt 报 VOL.1，与本期核心 VOL.2 不符；分版正确采用 W43 先例 + 核心 VOL.2（页脚 VOL.2），以实测 shipped 先例为准。
9. freeze diff 输出计数口径：命令行 total 为 multiset 实例数，diff.json 为 distinct 串数（如 P2 −33 vs −25），两者口径不同但裁定基础（distinct 串 + token 全覆盖）一致。
10. 非阻塞观察：P1 暗带右题 `SEMAINE DE L’ ENEM` 为双节点宽距排版（继承式样），目视清晰、无重叠（rowcheck 0）；P7 ERROS 盒高 797.5（W43）→ 876.5、palavra 盒下移（1019.5 → 1098.5），系法语诊所注变长所致，几何门仍为 0。

**最终结论：ZERO PROBLEMS — 本版通过独立校对，可交付（入仓与否由主线决定；本校对未做任何上架动作）。**
