# PROOF-NOTE — W47 fr-ru 独立校对（proof3，重派）

- 版：`production/2026-w47/2026-w47-fr-ru/`（re-fanout #2，r2run1）
- 校对员：proof3（scratch 全新，与 proof1/2 无关）
- scratch：`hidden_files/w47/scratch-proof-fr-ru3/`
- 结论：**b — 有缺陷 1 项（D1），其余全部门禁通过；修 D1 后须重渲染 + 从头再做一轮全量校对方可定稿。**
- 无任何 commit / push；生产目录零写入（SVG 始末哈希已验无变）。

## 1. 三件 SHA 实测（开工核对，与任务一致）

| 件 | 字节 | SHA-256 实测 |
|---|---|---|
| 印 `La-Lucerna-VOL4-fr-ru.pdf` | 17,477,429 | `c2976921db3531b69adc9d0a37ab8c5fb59dde8678d6892d6d2a9d72de040229` |
| 网 `La-Lucerna-VOL4-fr-ru-web.pdf` | 1,760,007 | `a6d94e5f0d54f78d5cd822040b17bff37c04a7a6852ad25fce5388dcdca9a15a` |
| 文 `2026-w47-fr-ru.text.md` | 50,453 | `a3449fa7e9d90576241371a33fd8f1c25d17a7c723ceee019de9e29d11ccd8f9` |

核心对照 `core-fr`（fix4）：印 `a30af667…25a9d` / 网 `56f50ca8…e141` / 文 `52024e02…df`（与 FANOUT-REPORT-fr2.md 一致）。

## 2. 缺陷清单（1 项）

### D1 — P3「DATES À RETENIR」奶油盒末行下行字母越出盒底（新引入，非核心继承）

- **源码行**：`2026-w47-fr-ru/expl.py:121`，`dates3_note`：
  `Внимание: нуво выходит в четверг 19-го; праздник начинается уже вечером в среду 18-го.`
  （3 行；核心同注 2 行，末行基线 1938.9）
- **SVG 落点**：`svg/p3-culture.svg`，盒 `<rect x="1440" y="1640" width="422" height="330" fill="#f0eee5"/>`（底边 y=1970.0）；
  末行 `<text x="1461.5" y="1966.2" font-size="19.5">вечером в среду 18-го.</text>`。
- **PIL 真墨实测**（`verify_ed_ru.py`，Noto Sans CJK SC 19.5pt，`anchor="ls"` 基线相对）：
  墨盒 x 1461.5–1675.5、y 1952.2–**1971.2**，盒底 1970.0 → **越边 1.2 svg px**（全 8 页 517 个入盒文本中唯一越边）。
- **交付 PDF 渲染像素为准**（`La-Lucerna-VOL4-fr-ru.pdf` P3，fitz）：
  盒底矢量边 = 1477.199pt（SVG 1970.0 的 0.75 倍应为 1477.5pt，CairoSVG 落位 −0.3pt）；
  600dpi 扫描：暗墨（min 通道 <150）延续至约 1477.92–1478.04pt，即盒底之下 ≥0.7pt；
  300dpi 裁切 `render/../crop-p3-boxbottom.png` 目视可见：`р`（вечером）、`р`/`у`（среду）共 3–4 处下行笔画尖伸出奶油盒底、落在白纸上。
- **归属核实**：核心同盒末行基线 1938.9、墨底约 1944，余量约 26px，
  核心 0 越边；俄语注多折一行致末行贴底——**版（fan-out）新引入，非冻结核心行**。
- **修法建议（供 builder，不由校对改）**：`dates3_note` 缩短数字符使末行上移，
  或该盒内容上移 ≥2px；修后整期重渲染 + 全量重校。

## 3. re-fanout #2 复核点（逐项存活）

| 复核点 | 实测 |
|---|---|
| P7 披露框 6 版 3→2 行 | 末行 `обещание разобрать настоящие письма.` 基线 **2233.3**，盒 y=1878 h=380 底 2258.0，清除 +24.7；PIL 真墨末行底自测 **2238.3**（Noto Sans CJK SC 19.5，`anchor="ls"`，墨盒 y −17…+5；余量 19.7px；前轮报告写 2237.3，差 1px 为测量口径差，非版面变化）；交付 PDF 200dpi 间隙行（svg y 2258.5–2269.5）**暗像素 0**；300dpi 裁切 `render/p7-boxbottom.png` 目视：2 行完整在盒内，下方白纸间隙干净，绿条未侵 |
| Q148 | 键 `devant le`（REG + p8 extract + text.md 三处一致）；题干 P8 `(148)___ cinéma ?`，与核心逐字一致，P8 全页 `du cinéma` 出现 0 次 |
| Q130 孤儿空白行 | P8 `(989.0, 843.0)` 元素 `___`，版/核坐标与文本完全一致（观察类，见 §5） |
| Q36/Q37 | P3 x=538.5 列 29 要素，版相对核偏移全为 **+29.7**（ru 应在 +30 档 ✓）；空白行 y 1238.4/1371.1（核 1208.7/1341.4，+29.7） |
| keydiff | p8 compare **CLEAN**，keydiff **[150]**（Q150 键为读者语写作键，设计内差异）；137–139 为翻译键、与核心一致，不在 keydiff 内 |
| 孤儿扫描 | 基线分组 + 同基线判定：标点独行基线 0 处、单字母独行基线 0 处；版相对核 **0 新增**（对照试验：合成孤儿 `。` 检出；同基线 `.` 不误报） |
| "next Sunday" | 版 SVG 全文 0 命中，不触发 |

## 4. 门禁总览（详见 GATE-LOG.md）

| 门 | 实测 |
|---|---|
| ① run.py | rc=0，TOTAL 150（A2 53 / B1 75 / B2 22；按页 10/15/18/18/17/18/12/42），0 溢出；scratch 副本重建 SVG **8/8 字节一致**，生产 SVG 未动 |
| ② freeze | core-fr baseline **8/8**；版自身 baseline **8/8**；freeze diff rc=0，新增 CJK 仅 U+3000（全角空格分隔符，SOP §1.1 所定）15 处 |
| ③ occlusion | rc=0，自检 6 类全触发，**0 flags**（注：occlusion 不覆盖文本越自家盒底——D1 由 PIL + 交付 PDF 像素检出） |
| ④ p8 | extract 键 **150/150**，注记 121/150；compare **CLEAN**，keydiff [150] |
| ⑤ 印/网文字层 | pdftotext 各 107,298 B，**逐字节一致**；网 PDF 1,760,007 B < 7MB |
| ⑥ P8 最小字号 | PDF 实测 **11.625pt** ≥ 9.75pt（SVG 属性最小 15.5pt） |
| ⑦ 盒标题 PIL 真墨 | 517 个入盒文本逐一实测（正确字号、基线相对墨盒）：**1 越边 = D1**；其余 516 个全在盒内；交付 PDF 8 页外沿 3px 零墨 |
| ⑧ 150 题逐题手验 | REG 键仅 Q150 异；143 处注中俄同事实（数字/日期归一化核对 0 差异）；text.md 150 答案键与注与 REG 全等；题干逐页 string-freeze 0 缺失、0 核心讲解残留、0 未说明 CJK；MCQ 45 体 0 缺陷 0 未定位；目视 P1–P8 逐题核对键题契合（见 §6） |
| ⑨ 全页目视 | P1–P8 全读：除 D1 外无溢出/重叠/压页脚/截断；Q7–Q150 题干、选项、答案页逐项核对无误 |

## 5. 不列为缺陷（观察类 / 只记录）

- **O1 核心继承孤儿填空行**：Q130（P8）、Q36/Q37（P3）空白行位置与核心完全一致，首轮已存在，不修版、不动核心。
- **O2 D5 字体事项（只记录，不修）**：KIT 引用的 `Итог финалаMasters` / `Турина—` / `Смотреть финал—`；
  实测当前 `expl.py:122` `chiffres_note` 与 `:204` `stem_e1` 字符串间距正常
  （`Итог финала и состав Турина: см. текст на этой странице.` / `Смотреть финал: учить французский.`），
  P4/P8 渲染目视无异常间距；待用户定范围。
- **O3 P1 Atget 图中小白方块**：与核心同图同位置，核心继承，非本版问题。
- **O4 冻结核心英文 "next Sunday"**：fr 族 0 命中，不触发。

## 6. 150 题手验摘要（目视逐页，键与题干契合）

- P1 Q1–Q10：Q1–Q6 填空（Alcaraz/Sénat/beaujolais/预算/决赛日期）键与题干一致；Q7–Q10 选择题选项日期与星期一致（8 日周日、18 日周三、19 日周四、22 日周日）。
- P2 Q11–Q25：日期填空（mercredi/jeudi/dimanche）、futur proche（va voter/allons goûter/vas raconter/allez regarder）、
  Q19–Q21 事实选择（20 日/21 日/22 日）、Q22–25 词义配对（vote/décision、primeur/jeune vin、déchet/ce qu'on jette、finale/dernier match）全契合。
- P3 Q26–Q43：Vrai/Faux（1951/第二→第三周四/19 日/巴黎→Beaujeu/gamay）与填空（gamay/jeudi/Beaujeu/1985）、
  改写（jamais/ne…pas）、Q38–40（75 ans/minuit/troisième）、Q41–43（cépage/13 août/saucisson）全契合；Q36/Q37 空白行见 O1。
- P4 Q44–Q61：决赛日期/胜者/都灵开赛/首秀法国人/法甲复赛、词义配对（forfait/tableau/tirage/trêve）、
  比较级（plus vite/plus grand/moins longue）、填空（forfait/finale/groupes/tirage/Bordeaux/Milan）全契合；数字与正文一致。
- P5 Q62–Q78：16 部新片/prequel/Dhont（拼写正确）/Ménochet/Trivial Pursuit、填空（mercredi/prequel/Ménochet/21/produit/acheter）、
  词义配对（prequel/bande-annonce/seconde main/atelier）、对话（des billets/deux）全契合。
- P6 Q79–Q96：日历读数（115–1/458–0/18 日/20 日/9 déc/26 日）、词义配对（sénateur/rejeter/vote/commission）、
  比较级（plus long/moins simple/aussi important）、填空（examine/ont rejeté/part/peut/connus）全契合。
- P7 Q97–Q108：动词填空（battu/est arrivé/vote/beauté/produit/sortent/rejetée/jouer）、
  改错（battre→battu、votent→vote、va examiner→examine、vendredi 20→jeudi 19）全契合。
- P8 Q109–Q150：完形（lundi/Beaujeu/résultats/goûté/proposent/aimé/jouent/écrit）、
  选择（dimanche 15/un vin primeur/mercredi 18/irais/semble/reçoit/prequel/19 nov./journal/finales/20 h 45/l'école/retournent）、
  句型（va voter/venais/a goûté/Selon/examine）、翻译（finale/beauté/depuis/préparer/ne…pas encore）、
  词义配对（140–144）、对话（des billets/deux/quelle heure/**devant le**/film）、写作 Q150 全契合。
- 数字核对：21,8→12,7；115–1；458–0（+2 票弃权，正文有）；7-6(5), 7-5；1951/1985/75 周年；1 260→1 500 欧元；50 天→11 月 26 日；
  16 部新片；2 h 38；23/10、4/11、9–17/11、18/11、20/11、26/11、9/12——中俄注逐项对过，无事实出入。

## 7. 检测器修正记录（本轮修的 3 处检测器 bug，非版式问题）

1. **PIL 墨盒锚点**：第一版用 PIL 默认锚点 `la`（自升部线度量），全部墨盒系统性下偏约一个升部高，误报 156 处；
   改为 `anchor="ls"`（基线相对）后仅剩真实 D1 一处。`verify_ed_ru.py` 内已注记。
2. **text.md 答案解析**：第一版按 U+3000 切分条目，把注内含 U+3000 的 8 条（22/87/114/140–144）切碎，
   且 `[^)]*` 处理不了嵌套括号（Q114）；改为仅在 `　+数字.` 处切分、注取首 ` (` 至末 `)` 后重跑，150 键 + 121 注全等。
3. **数字归一化**：第一版把 `сенатор` 误读为月份 `сен`→9、`Лига 1` 当数字、中文数词（两/四/三单）未归一；
   改为显式月份形（`сент` 等）+ 专名剔除 + 数词映射后 0 差异；另 P7 间隙扫描首版误含 y=2270 绿条首行，
   改为 svg y 2258.5–2269.5 后间隙 0 暗像素（3 处像素证据见 GATE-LOG）。

## 8. 归属核对（冻结核心行 vs 版）

- D1 已按核心源码 + 机制核实：核心同盒末行 1938.9、0 越边；越边是俄语注多折一行所致，属版责任，非核心行。
- 其余全部机械门均为版自身实测；freeze baseline 8/8 证明核心可复现，版重建 8/8 证明版可复现。
