# W45 ES×FR 独立校对报告（2026-w45-es-fr）

## 结论

**除徽章字号一项待协调员裁定外，ZERO PROBLEMS。**

- 徽章字号三方实测：本版 20、W43 已发版 20、工具箱 README #20 标准 19.5pt。
  按任务指令，20px vs 19.5pt 本身不由校对员单独判不通过，交协调员据证据裁定。
  但补充证据：W43 同配对 KIT §2 亦记载该徽章为 20px、本版与 W43 已发版 SVG 的徽章元素逐字节相同
  （串、槽位 y=372、字号、粗体、颜色 #a4553a、居中锚点全同），即本版遵循的是同配对已发先例，
  而非偏离；19.5pt 是 README #20 中 EN-core 家族的通用规则。
- 徽章串、槽位、颜色、页脚、页行、gloss 前缀、P8 分隔符与 W43 已发版全部相符（见下）。
- 已知缺陷（非阻塞，协调员已裁定）：P6 第二组图表 Inmigración 标签被条形压约 5.3px，
  几何与核心逐字节相同，确认为核心冻结缺陷、本版未新引入——不因此判不通过。

## 逐项核查（全部独立重跑，非采信构建者自述）

### 1. 基线 freeze（8/8）
- `tools/freeze.py baseline`（核心构建目录 → 核心 SVG）：8/8 逐字节相同，
  p1 a1b30102…、p2 10e78c2e…、p3 5986ba9e…、p4 1894836e…、p5 cd15c68b…、
  p6 fcfccf82…、p7 b1774024…、p8 d1c46fa4…；运行前后核心重哈希无变化。
- 交付版 SVG 哈希与 KIT §8 全同；PDF sha 与 KIT §7 全同（print 7,157,921 字节、
  web 3,732,117 字节，各 8 页）；8 张 PNG 均为 1950×2700。

### 2. 可复现重建（全新副本 + 同一转换脚本 + 单进程 driver）
- 核心构建全新副本 + 转换脚本（BUILD 重定向至副本，脚本本体未改逻辑）：
  transform 290 项替换全部命中、残留 CJK 检查通过；`run.py` 退出 0。
- 重建 8 张 SVG 与交付版逐字节相同（见 repro-compare.txt）。
- 重建日志：0 个 `FLOW OVERFLOW` / 0 个 `HEAD TOO WIDE`（该两串确为 bslib4.py 的警告文本，
  故 0 命中是有效阴性）；P7 col3 止于 1822.08，P6 练习流止于 y=2561，P8 答案流止于 y=2501。

### 3. 源码树 diff（核心构建 vs 分版构建）
- 仅 7 个文件不同：bslib4.py、content12/34/56/7/8.py、render.py——与构建者自述一致。
- render.py diff 仅 3 处：BASE 路径 core→fr、两个 PDF 文件名加 -FR 后缀。
- 剔除含 CJK 的行后，剩余删除行仅为：OUT 路径、P1 标语行（徽章替换）、content56 的
  gap=3→1 行（题干本身不变）、content8 的两行 lh 参数、content12 的 CIFRAS tsize 收尾行。
  无任何西班牙语正文行被改动。

### 4. freeze diff（strict-cjk）
- 各页 added CJK = 0（核心 CJK 170/280/161/169/247/80/388/981 → 分版 0）；分版 SVG 直接扫描 CJK 字符 0。
- 删除的非中文串共 14 条，逐项定性：
  - P1 标语行 1 条：徽章替换（装置性）；
  - P2/P5 换行碎片 3 条：词元在分版全文中全部存活；
  - P8 答案行 10 条：9 条词元全部存活（键经 dash-parse 验证相同，见 §5）；
    余 1 条为 #1 答案行换行：键 `programas` 不变，注由西班牙语句子译为法语
    （注层翻译属分版职责；该句词元除分号粘连形式外在分版中仍可找到，属答案行重排，非正文删改）。

### 5. p8.py compare + 34 项 dash-parse 逐项裁定
- `p8.py compare`：CLEAN，150 = 150，missing = []，extra = 0，keydiff 与构建者所列 34 项完全一致：
  17, 18, 20, 25, 26, 27, 28, 52, 53, 54, 55, 60, 61, 62, 63, 83, 85, 93, 94, 95, 96, 98,
  107, 109, 110, 111, 117, 137, 138, 141, 142, 143, 144, 148。
- 独立 dash-parse（印出段首个 ` — ` 拆分，逐字节比对；详见 dashparse.log / dashparse.json）：
  - 32 项非 137/138：印出键全部逐字节相同；分版注尾确为 ASCII 括号组
    （(singulier)/(pluriel)/(passé)/(b)/(c)/(d) 等），且 p8.py 工具抽键方法确为 paren——
    工具 artifact 成立，注-only，通过。
  - 全量 150 项 dash 键差异仅 [137, 138]，无其他印出键差异。
  - #137：核心 `周一在九个自治区是假日。` → 分版 `Le lundi est férié dans neuf communautés.`
    （注 `d'après le texte`）；#138：核心 `周日我们看 NFL 和马竞–巴萨。` →
    分版 `Le dimanche, nous regardons la NFL et l'Atlético–Barça.`（注 `d'après le texte`）。
    与 W43 同配对翻译题重瞄准先例一致（注：该先例在 W43 KIT §3，非任务所写的 §5；
    §5 为 W43 的版式缺陷节——节号出入不影响实质，构建者 KIT 引用 §3 正确）。
  - #139/#140：题干已重瞄准法语（`Le Bernabéu accueille un match de la NFL. → ___`、
    `Chaque graphique doit indiquer sa source. → ___`），西班牙语键与核心逐字节相同。
  - #150：印出 `150. ✓ Texte modèle dans la section H de cette page (84 mots)`；
    H 区范文与核心逐字节相同，空白切分计词恰为 84 词（连字符复合词按空白切分计 1 词，
    与核心自身的 84 词口径一致；正则分词 87 系连字符拆分所致，非差异）。
  - 注册表逐项比对（核心构建 REG vs 分版构建 REG）：n/page/level/type 零差异；
    总量 150，A2 50 / B1 72 / B2 28，分页 10/18/18/18/18/18/12/38；
    键差异仅 137/138/150（150 的 REG 键与印出行分属同一题的两面，与核心结构相同）；
    注差异 148 项（翻译），注相同 2 项（#19 `nosotros → descansamos`、#87 算式
    `34 + 22,2 + 17,1 = 73,3`，均为语言中性——构建者正文称“1 项”系少计，不影响结论）。

### 6. 遮挡审计 + 同基线扫描
- `occlusion_audit.py --selftest` 通过（6 类 planted 全触发，clean 对照静默）；
  最终审计 0 flags，--core 对比 NEW flags = 0，核心对照 0 flags。
- 同基线墨迹扫描（builder rowcheck 方法重跑）：分版 7 项 = 核心 7 项，集合完全相同，
  均为 P1 目录行 `Pág. N` 与标题的 +4.0px 正间隙（非重叠）。
- P6 图表区：容器矩形 2 个 + 条形 8 个 = 10 个矩形逐字节相同；
  y=1634–1903.5 的图表文本 23 个逐字节相同（另含 1576 节标题共 24 个亦相同）。
  全页 34 个矩形中仅 10 个不同，均为练习流标记矩形 y 位移（gap 3→1 的备案改动），非图表几何。
- P3/P5 图片：href 载荷 sha 与 x/y/w/h 与核心完全相同（P3 627,079 字节载荷、P5 461,691 字节载荷）；
  P3  credit 行 `Foto: Wikimedia Commons — CC0 (dominio público)` 不变。

### 7. 家具三方实测（本版 vs W43 已发版 vs 核心）
- 徽章（P1）：本版与 W43 已发版元素逐字节相同——
  `TEXTES EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`，
  x=975 y=372，font-size=20，bold，fill=#a4553a，middle 锚点；核心同槽位 y=372 为 19px 灰色标语行，
  故为原位替换。字号三方：本版 20 / W43 已发版 20 / README #20 标准 19.5pt（待协调员裁定）。
- 页脚（8 页全）：`La Lucerna · HEBDOMADAIRE ESPAGNOL VOL.2 · TEXTE EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS`；
  W43 同串仅 VOL.1→VOL.2 之差。页行 8 页全为 `Page N sur 8`，与 W43 一致。
- gloss 前缀：分版 P2–P5 词表首行均为 `Note — `，与 W43 形式一致。
- P8 分隔符：分版与 W43、核心均为 `— PÁGINA N —`（N=1–8）。

### 8. ABSTRACT.txt
- 法语单行（仅尾换行）、无 ASCII 双引号；含 29-N、logement、lundi 2 novembre、
  neuf communautés、NFL、Bernabéu、Atlético–Barça、A2–B2、150 exercices、
  apprendre l'espagnol / actualité espagnole——真实主题关键词 + 学习者检索短语齐全。

### 9. P7 金句与读者园地
- 金句 8 句：严格计数各恰 2 次（正文页 + P7），页签 Página 1, 2, 3, 4, 5, 6, 6, 1，与核心一致。
- 读者园地：示例信体、Ana、Shanghái 与核心一致，仅署名括号全角→半角
  `(ejemplo, escrito por la redacción)`；西班牙语披露行与核心逐字节相同，
  法语注含全部事实（无真实来信、无最佳 P8 文本、刊登示例、承诺顺延 VOL.3、邀约来信）。
  未编造新读者/信件。

### 10. 已知缺陷（只报告存在，不判不通过）
- P6 第二组图表 Inmigración 标签：标签墨迹 1011→1144.25（自测；构建者称 1144.4，差值属字体取整），
  条形起于 x=1139，压约 5.3px。标签元素与条形矩形（x=1139 y=1699 w=156.75）在核心与分版中
  逐字节相同——确为核心冻结缺陷，非讲解层新引入重叠。

## 合规声明
- 仅校对：未改核心构建目录、核心已发 SVG、W43 目录；未发 Discord、未往主聊天发卡片/PDF、
  未建 cron、未碰 weekly-git。全部写出均在 hidden_files/w45/es-fr-proof/ 下。

## 审计输出路径
- 报告本体：~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-fr-proof/REPORT.md
- 基线：freeze-baseline.log / freeze-baseline.json；diff：freeze-diff.log / freeze-diff.json
- p8：p8-compare.log / p8-compare.json，逐项裁定：dashparse.log / dashparse.json
- 遮挡：occlusion-selftest.log / occlusion.log / occlusion.json；同基线：rowcheck-ed.log / rowcheck-core.log
- 复现：repro-transform.log / repro-run.log / repro-compare.txt；注册表：core-reg/reg.json / repro/reg.json
- 哈希与尺寸：hashes.txt / pdf-sizes.txt / png-sizes.txt；源码文件清单：sourcediff-files.txt
