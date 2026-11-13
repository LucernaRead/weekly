# PROOF-NOTE — 2026-W47 it-pt（proof1）

**复校员：** proof1（独立复校，只读；未修版、未 commit、未 push）
**复校对象：** `~/workspace/weekly-git/production/2026-w47/2026-w47-it-pt/`
**复校时间：** 2026-11-11（UTC）
**结论：(b) 有问题** —— 缺陷 D1–D7（见下）。内容事实与语言大体过关；几何上有 1 处 core 级溢出、4 处本版级标题/副标题溢出、1 处 text.md 残留中文、1 组系统性小幅右缘溢出。

## 0. SHA 核对（三件，先核对后开工，一致）

| 件 | 大小 | SHA-256（KIT §7 登记 = 盘上实测） |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-PT.pdf` | 14,036,807 B | `4492665b04a7a631c9e8ace2cd15cfe077dbd3607f78b6aab228e05470629882` |
| 网页 PDF `La-Lucerna-VOL4-PT-web.pdf` | 1,262,226 B | `164492f8ab7b69f166b47778f856ae9d16cb29ed43dc2458208cc804f41e93c1` |
| 文本导出 `2026-w47-it-pt.text.md` | 55,820 B / 1317 行 | `438656e1f9b8317c92873a5533f753d61b961c31ddac6dcb32c2ac5c6229efb1` |

复校期间三件文件未被改动（mtime 2026-11-11 03:10–03:18；复校末再次 sha256sum 核对一致）。

## 1. 缺陷清单

### D1（core 级，严重）——P2 匹配题 b、d 首行墨迹越过页面右边距
- **位置：** P2，D 节匹配题，b 行（SVG y=2162px）、d 行（y=2271px），x=1473.5 起，Newsreader 23px。
- **证据（三法一致）：**
  - PIL 真墨（`ink.py`）：b 墨迹右缘 1877.6px，**超 +15.6px**；d 1879.7px，**超 +17.7px**（右边距 1862px）。
  - 200dpi 像素扫描（`pixelscan.py`，渲染印刷 PDF）：b 墨迹右 1406.2pt，**超 +9.7pt**；d 1408.3pt，**超 +11.8pt**（抗锯齿阈值所致，数值略小于 PIL，但方向一致）。
  - PDF advance（`pdfscan.py`，PyMuPDF）：b x1=1408.2pt（超 +11.7pt）；d x1=1409.7pt（超 +13.2pt）。
  - 目视（`png/print/p-2.png`）：b 行「b. il ponte di barche per la festa del 21」、d 行「d. la piccola luce di cera che si accende」均伸到页右缘；对照 a、c 行留白 37–41pt。
- **层级：** core 级。本版与 core-it 的 b、d 行措辞完全一致（freeze-diff 10:20 前 it-es 版零增减可证）；根因在 core：`wrap()` 量测时未计入 `b. `/`d. ` 前缀。
- **修法：** core-it `content12.py` 262/264 行重措辞（缩短首行）或修 wrap 使前缀计入量测。**注：并行修复代理 `scratch-fix-core-it1` 已于 2026-11-11 10:37–10:38 UTC 改了 core**（候选 b-B2「il ponte di barche per la festa in novembre」、d-D1「la piccola luce di cera accesa in chiesa」）；core 修后，11 个 it 版须重新 fan-out，本版仍带旧文，fan-out 后重验此条。

### D2（本版级，较严重）——P1 副标题墨迹越过盒右缘及页面边距
- **位置：** P1，LA SETTIMANA 奶油盒副标题「Esta semana　Cosa succede, giorno per giorno」（Noto Sans CJK SC 19px，x=1461.5，y=694）。
- **证据（三法一致）：** PIL 真墨右缘 1876.9px，**超盒右缘（1862）+14.9px**；200dpi 像素扫描墨迹右 1405.8pt，**超边距 +9.3pt**；PDF advance x1=1407.3pt（超 +10.8pt）。
- **目视：** `p-1.png`、`w-1.png` 均确认副标题尾部「giorno per giorno」落在奶油盒外白纸上。
- **修法：** 缩短葡语副标题（例如去掉「Esta semana　」或改更短的「O que acontece, dia a dia」）或加宽盒；并与 it-de D1 同类（it-de P1 副标题 +13.7px）一并看——属各版右锚定/长行量测的系统问题。

### D3（本版级，严重）——P1 奶油盒标题漫出盒外
- **位置：** P1，「LA SETTIMANA IN CIFRE　A SEMANA EM NÚMEROS」（23px 粗体 sans，y=1388.5）。
- **证据：** PIL 真墨 [556.5, 1119.8] vs 盒 [538.5, 961.0]，**超出盒右缘 +158.8px**。目视 `p-1.png` 确认：「A SEMANA EM NÚMEROS」落在盒外白纸上（无文字碰撞，第 3 列该处为空白）。
- **注意：** occlusion audit 的 BOXTITLE 规则只查有边框的盒（描边或填 `#2c2822`），奶油盒（填 `#f0eee5`、无描边）不在查——审计 0 flags 不能作为无溢出的证据；本条及 D4、D5 均为人工补查发现。
- **修法：** 缩短葡语标题（例如「A SEMANA EM NÚMEROS」改「EM NÚMEROS」）或标题分两行。

### D4（本版级，较严重）——P2 奶油盒标题漫出盒外
- **位置：** P2，「LA FRASE PER RICORDARE　PARA LEMBRAR」（y=1280.8）。
- **证据：** PIL 真墨右缘 1048.4px vs 盒右缘 961px，**超出 +87.4px**。目视 `p-2.png` 确认「PARA LEMBRAR」落在盒外白纸上。
- **修法：** 同 D3（缩短葡语标题或分行）。

### D5（本版级，中等）——P7 奶油盒标题漫出盒外并贴到页右缘
- **位置：** P7，「ERRORI TIPICI　ERROS FREQUENTES」（y=242）。
- **证据：** PIL 真墨右缘 1878.7px vs 盒右缘 1862px，**超出 +16.7px**；PDF advance x1=1409.3pt（超 +12.8pt）。目视 `p-7.png` 确认「FREQUENTES」尾部贴到页右缘，超出盒右缘与页面边距。
- **修法：** 同 D3（缩短葡语标题）。

### D6（本版级，轻微，仅 text.md）——翻译题型标签残留中文「翻譯」×4
- **位置：** `2026-w47-it-pt.text.md` 第 969/971/973/975 行，Q137–140 题型标签 `[A2/B1/B2 · 翻译]`。
- **证据：** 全文件唯一 CJK 字符即「翻」「译」各 4 个；其余全部题型标签均为葡语（`Completa a frase`、`Escolha múltipla`、`Forma frases`、`Relaciona as palavras`、`Verdadeiro ou falso`、`Cloze`、`Escrita`，以及题末 `[Traduzir para português/italiano]`）。PDF 中 Q137–140 显示为「Traduzir para português/italiano」（正确），故仅文本导出有问题。
- **同类：** 与 it-es proof1 D1 同类（E 节 Q137–140）；KIT §8「有意保留、W46 前例」的说法不成立——it-en 同位置已本地化为 `[Translate]`。
- **修法：** 导出/翻译映射把该标签本地化为 `[Traduzir]`（与 it-en `[Translate]` 对照）。

### D7（本版级，轻微，系统性）——右缘小幅墨迹溢出，10 行，覆盖 8 页中的 6 页
- **根因（同一）：** PIL 量测与渲染器 advance 差约 0.5–0.8%，右锚定行/长行 wrap 估短。下面逐项均经 PIL 真墨 + PDF advance 双法核对（数值一致到 ±0.2pt）：
  | 位置 | 行 | PIL 真墨右缘 | 超出 |
  |---|---|---|---|
  | P1 测验头副标题 | 「Lê a primeira página e escolhe a resposta certa　Respostas na página 8」 | 1867.1px | **+5.1px = +3.8pt** |
  | P2–P6 练习头副标题（5 页同款） | 「Respostas na página 8　Os níveis misturam-se — procura pelo número」 | 1865.3px（P2、P6 实测；P3–P5 同节点同 x，PDF advance 均为 +2.5pt） | **+3.3px = +2.5pt** |
  | P2 小节副标题 | 「Una festa, una giornata verde」 | 1864.2px | **+2.2px = +1.6pt** |
  | P5 图注首行 | 「Foto: Jean-Baptiste-Camille Corot — Wikimedia Commons,」 | 1863.8px | **+1.8px = +1.4pt** |
  | P8 范文 1–2 行 | 「Testo modello: Domenica 22 novembre metto la sciarpa e」/「vado a Cremona: è l'ultimo giorno della Festa del Torrone」 | 1864.2 / 1864.3px | **+2.2/+2.3px = +1.6/+1.7pt** |
  | P8 答案头副标题 | 「Cada resposta tem uma nota de uma linha em português　✓ = tarefa com texto modelo」 | 1867.3px | **+5.3px = +4.0pt** |
- **严重度：** 轻微。无碰撞、无裁切、距页缘仍 ≥85px；但属边距违规（墨迹过 1862px 线）。
- **修法：** 右锚定行与长行 wrap 留 2–3% 安全余量，或改用渲染器实测 advance；与 D2 一并修（同根因）。
- **已排除的同类嫌疑（不入缺陷）：** P2 Canaletto 图注墨迹 1861.7px（内 0.3px）；页脚「Página N de 8」墨迹超 +0.4px（亚像素量测噪声级，与 it-de O3 的 0.1px 同类）；P1 日期「2026」advance 超 +0.2pt（进位噪声）。

## 2. 观察（O，非缺陷，建议协调员知悉）

- **O1 — MER 18 缺席（core 级，需协调员确认意图）：** P1 LA SETTIMANA / GIORNO PER GIORNO 列 LUN 16、MAR 17、GIO 19、VEN 20、SAB 21、DOM 22，无水曜日 11 月 18 日。core-it `content12.py` 73–78 行源数据即只有 6 天；全刊无任何 11 月 18 日的事项（manovra 听证 9–12 日、修正案截止 17 日、Eurochocolate 20 日、Serie A 21 日、闭幕 22 日），属 core 编辑取舍，非构建丢行；但「giorno per giorno」的逐日表跳过一日，读者可能视为缺口。建议确认意图（不改，或补一行）。
- **O2 — P1 导语措辞松：** 「Domenica 22 novembre torna la Serie A con la 12ª giornata」对 P4「La Serie A riparte sabato 21 novembre」（MD12 实际 11 月 21–23 日，首场周六）。P4 已澄清，非事实错误；仅措辞上周日像首日。
- **O3 — P5 计划第 1 项用简称：** «I tesori della Calabria»，而 P1 用官方全名 «I tesori della Calabria Straordinaria」（Eurochocolate 来源可证）。内容一致，仅简称。
- **O4 — P1 masthead 墨迹 [0.0, 1949.9]px：** 末字 A 距页缘 0.1px，首字 S 贴左缘 0.0px；字形完整无裁切（目视 `p-1.png` 确认），属设计（KIT §10 披露）；KIT §10「right edge ≈1881」的数字不准（实测 1949.9）。同 it-es O2。
- **O5 — P7 LA PAROLA 末行 +0.5px / P2 E TU 末行 0.0px：** 200dpi 像素扫描盒底下方 0 墨点，属亚像素量测噪声，非溢出（与 it-es 同盒裁决一致）。
- **O6 — 文字层词数：** print/web 各 7,982 词（Python split），KIT §8 称 7,981——差 1 词，观察级（`wc -w` 为 7,435，因不切 U+3000）。
- **O7 — manovra「约 €26bn」：** DPB 总额 €23.5bn，但 10 月 28 日 CdM 批准的法案多家媒体报「circa 26 miliardi」（takethedate、2duerighe）；本版措辞为「circa 26 miliardi di euro, secondo le ricostruzioni dei giornali」，并在正文提示「Chi legge i giornali trova cifre diverse per le coperture」——表述有据且已设防，非事实错误。

## 3. 门禁与检查（全部跑过，日志在 scratch 目录）

- **Occlusion audit：0 flags**（自测 6 类全触发）。盲区已人工补查：看不见文字漫出自家盒底、看不见 BOXTITLE 漫出奶油盒、看不见横向漫出、看不见按基线定盒高时的下行字母漫出——D3–D5、D7 均属审计盲区。
- **p8 compare（core-it 对 it-pt，显式路径）：CLEAN，150/150。** keydiff=[137,138,139]（预期重定向翻译键）。10:42 UTC 对当前 core 重跑，仍 CLEAN。日志 `p8-compare.log/.json`、`p8-compare-rerun.json`、`p8-extract-core.json`、`p8-extract-pt.json`。
- **freeze：** added 仅葡语讲解层/家具/P8 注释 + U+3000×8（每页 1 个）；removed 为中文层 + 重绕意大利片段。2 条意大利 added 片段（P2 b/d 行）为时序伪影：2026-11-11 10:37–10:38 UTC 并行 core 修复改了 core-it，it-es 10:20 的 freeze-diff 显示 b/d 零增减——本版与冻结时 core 一致，非本版缺陷。日志 `freeze-diff.log/.json`、`freeze-added.txt`。
- **freeze baseline：8/8 SVG 字节一致**（重建复现已发 SVG；repointed 文件 render.py、content12.py、content34.py、content56.py、content7.py、content8.py）。日志 `freeze-base.log`。
- **Canonical creambox（`tools/creambox.py`，8 个 SVG）：exit 0。** 全部 inside 清除量为正；负值均为 BELOW-WINDOW 假阳性（P1 IN QUESTO NUMERO −24.0→inside +16.0；P3 Nota −37.0→inside +47.7；P4 赛果表 −40/−26→inside +22.0；P6 图表 −42→inside +31.2/+90.0）。P7 工具盒汇总：3 盒，min inside +4.5px，min desc-clear −1.5px（即 LA PAROLA +0.5px 盒底，已像素裁决为噪声，见 O5）。日志 `creambox.log`。
- **PIL 真墨（`ink.py`、`ink2.py`）：** D1/D2/D3/D4/D5/D7 全部数值见上；其余 boxtitle 均合格（含 P6 最宽「LE MINIME DI ESEMPIO…」、P7「LA PAROLA」「LETTERE」）；其余紧盒底均合格（无下行字母，余量 4.5–5.3px）。
- **200dpi 像素扫描（`pixelscan.py`）：** D1/D2 确认（见上）；P7 LA PAROLA、P2 E TU 盒底下方 0 墨点（O5）。
- **PDF span 扫描（`pdfscan.py`）：** 除 D1/D2/D5/D7 所列及页脚 +0.6pt advance 噪声、masthead 设计带外，无其他边距违规；无真实 span 重叠（重叠项均为行盒/黑体跨度伪影，真墨 TEXTX 审计 0 flags + 目视干净）；P8 最小字号 **9.75pt**（实测，符合 SOP 下限）；每页图片 P1/P2/P3/P4/P5/P7/P8 各 1 张、P6 0 张（图表为程序绘图），共 7 张照片，与 KIT §5 一致。
- **印刷/网页 text layer：** 各 45,891 字节，词多重集一致（Python split 各 7,982 词）。
- **目视：** 8 页印刷全读（`png/print/p-1..p-8.png`，150dpi）+ 网页 `w-1`、`w-8` 抽查（与印刷一致，无网页独有问题；D2、D3 在网页版同样可见）。

## 4. 内容与语言（已核）

- **150 题键与题干语义逐题核对：** P2 25→c、26→b、27→d、28→a；P4 52→d、53→b、54→c、55→a；P8 141→d、142→c、143→b、144→a 全部一致。Q58 `più bella`、Q59 `meglio`、Q64 `ha preso`、Q82 Falso（BookCity 开幕为周一 11 月 23 日，预览 11 月 22 日）、Q93–96/109–112 虚拟式、Q137–140 翻译全部正确。
- **题号：** 1–150 齐全（138 单题 + 3 组×4：25–28、52–55、141–144）；答案 150 条齐全；P1 测验为 Q7–10；P5 计划 1–5 项与分级表「1. Lazio — 29 punti」等为栏目内编号，非练习题。
- **金句：** 8 句各现 2 次（正文 + P7 FRASI），页码全部属实（P1×2、P2、P3、P4、P5、P6×2）。
- **IN QUESTO NUMERO：** Pag. 2–8 页码全部属实（P2 Venezia、P3 Torrone、P4 Serie A、P5 Giovani、P6 Manovra、P7 Frasi、P8 Esercizi）。
- **VOL：** SVG 中 VOL.4 ×9、VOL.5 ×3（3 处均为合法的下期引用：P7 LETTERE 两处 + P7 底栏「LA PROSSIMA SETTIMANA (VOL.5)」）；text.md 中 VOL.4 ×1、VOL.5 ×3。
- **`·`：** 162 行，仅见于选项串/词汇表/组头（150 题 + Nota 词汇表 + 词库 + 组头），无他用。
- **禁词扫描：** Ucraina/Russia/Putin 干净。ABSTRACT（SOP §9）：单行葡语、零 ASCII 双引号、含刊名/italiano/A2–B2/150 练习与真实主题，合格。
- **日期/星期（Europe/Rome，`date` 核）：** 11 月 16 日周一…22 日周日、23 日周一、24 日周二、12 月 2 日周三、12 月 6 日周日、12 月 31 日周四、10 月 15 日周四、10 月 28 日周三——文中星期主张全部正确。
- **范文（Q150）：** 恰 99 词。

## 5. 事实核查（本人独立网查，2026-11-11）

- **Serie A MD11（11 月 6–8 日）：** 24 球/10 场；Lazio 29（1–1 Napoli，Gattuso 队，不败）、Inter 28（2–0 Como）、Roma 27（3–0 Sassuolo，最佳攻击 31 球）、Milan 24（2–1 Genoa）、Como 23、Udinese 末位 5 分（1–2 Venezia）；10 场赛果与 P4 赛果表一一相符。
- **Torrone：** 29 届，11 月 7–22 日（16 天、3 周末），主题«Il Confine»；Torrone d'Oro 授予 Davide Simonetta（周日 22 日 11:00，Palatorrone）；游行 16:00（>150 人）、Sforza–Visconti 婚礼重演 17:00、旗手与火舞至 18:00、「Il torrone va in brodo」18:00；1441 婚礼为传说。
- **BookCity：** 15 届，11 月 23–29 日，1,360 活动 / 2,487 主角 / 1,164 书 / 443 场地，主题«Il senno sulla Luna»（Ariosto）；开幕周一 23 日 20:00 Teatro Dal Verme，Colson Whitehead（2× Pulitzer）。预览（周日 22 日 16:00 Fondazione Luigi Rovati，Edmund de Waal）为 it-de proof1 已验，**本人未独立复核**。
- **ATP Finals：** 11 月 15–22 日都灵 Inalpi Arena；Zverev 世界第一；Sinner 膝伤缺席（2025 冠军）；Cobolli 首秀；Alcaraz 热门。
- **Eurochocolate：** 32 届，11 月 13–22 日，«Fate dolci»；Calabria 首任客座大区（bergamotto、cedro、peperoncino、fichi）；«I tesori della Calabria Straordinaria» 周五 20 日 18:15；Massari 22 日闭幕。
- **Manovra：** DPB 10 月 13 日 CdM 批准、10 月 15 日送布鲁塞尔；2027 增长 +0.8%、赤字 3.4% GDP；法案 C. 3174-bis；听证 11 月 9–12 日（Giorgetti 12 日）；修正案截止周二 17 日 18:00；终票 12 月 31 日前；Irpef 第二档 33% 由 €50k 扩至 €55k；金融业约 €5bn（DPB 为 0.21% GDP ≈ €4.6bn；媒体称 5bn；本版措辞「circa 5 miliardi…secondo le prime ricostruzioni」有据）。
- **Nations League：** 意大利–法国周四 11 月 12 日、比利时–意大利周日 15 日；本版未印赛果（推迟至 VOL.5），表述一致。

## 6. 时序说明（重要）

复校中途，core-it 被并行修复代理 `scratch-fix-core-it1` 改动：2026-11-11 10:37–10:38 UTC 改 `core-it/content12.py` 262/264 行（修复 it-de proof1 的 core D2），重渲染 core SVG 并重导出 core text.md（新 SHA `d6cd45e7…`，修前 `adda0d31…`）。**本版三件文件未被改动**，上述结论针对 SHA 已验的三件文件。core 修复后，11 个 it 版须重新 fan-out（协调员跟进，非本复校任务）；D1 的 core 侧修复已存在，fan-out 后重验。

## 7. Verdict

**(b) 有问题。** D1（core 级）+ D2–D7（本版级），共 7 项。修后重验：D1 须待 core 修复 fan-out 到本版；D2–D5 缩短标题/副标题或调盒；D6 修复导出映射；D7 给右锚定行与长行加安全余量。O1 建议协调员确认意图；其余 O 项仅作记录。
