# PROOF-NOTE — 2026-W47 pt–fr (Portuguese target, French explanations) · proof1

- Proofreader: independent proof1 (pt-fr1), 2026-11-11
- Edition dir: `production/2026-w47/2026-w47-pt-fr/` (untracked in repo; no files modified, no commit, no push)
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-fr1/`

## §0 身份核对（SHA / 字节数，以磁盘为准）

| 文件 | 磁盘 SHA-256 | 任务给定 | 字节数 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `fe02b4fbb3a5869c53657e1ef8abae2e2b6a6b6b9314f4f633c88483884cd7cd` | 一致 | 12,934,799 |
| `A-Lucerna-VOL4-web.pdf`（网） | `96190bcacb57c5304d4356ab4c91aac75a270913abde2c6cc06624bfc024717e` | 一致 | 1,104,302 |
| `2026-w47-pt-fr.text.md` | `f3cb6a085b203dc421186ef64d77f5b51ebc9f70a4652d6f7b7b130b54ef0018` | 一致 | 37,687 |

三个 SHA 与任务消息一致。探针（`git hash-object -w --stdin`）通过；scratch 可写验证通过；creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383` 与任务给定一致；全程 `TMPDIR` 指向自有 scratch/tmp，未用系统 /tmp。

## 结论：(b) 有缺陷，不能定稿

共 6 项缺陷（D1–D6），全部在讲解层/版式，无一涉及 150 题答案键（keycheck 150/150 全过）。
修复后须重渲染并从头再做一轮全量复校（SOP §8），直至一整轮零问题。

## 缺陷清单

### D1 — P1 数字框标题溢出奶油盒（中）
- 严重度：中（标题末字落在白底上，整页第一眼可见）
- 位置：P1，奶油框 `(989, 786.2, 422.5×434)`，标题基线 y=823.18，`A SEMANA EM NÚMEROS　En chiffres`
- 归属：本版（法语 gloss 加长所致；核心同标题墨水右缘 1351.0，距盒右 1411.5 余 60.5px）
- 实测证据（三法一致）：
- PIL 真墨迹（正典 occlusion_audit.py `ink_box`，Newsreader/Noto Sans 实字体 4× 超采样）：墨水右缘 1424.0，超盒右 1411.5 计 **12.5px**；
- 200dpi 像素扫描（cards/p1-capa.png）：标题行带 y 795–832、x 1412–1460 有 64 个深色像素，x 至 1423；
- 裁图目视（`crops/p1-numbers-title.png`）：`En chiffres` 末尾 `s` 完整落在白底上。
- 修复建议：缩短法语 gloss（如 `En chiffres` → `Chiffres`，省约 40px）或缩小该框标题字号；修后重测墨水右缘 ≤ 盒右。

### D2 — P2 `PARA NÃO ERRAR` 框标题溢出奶油盒（轻）
- 严重度：轻（约 4–6px，末字母骑边）
- 位置：P2，奶油框 `(538.5, 605, 422.5×241)`，标题基线 y=642.02，`PARA NÃO ERRAR　La règle à retenir`
- 归属：本版（核心同标题墨水右缘 820.2，距盒右 961.0 余 140.8px）
- 实测证据：PIL 真墨迹右缘 965.0，超盒右 961.0 计 **4.0px**；像素扫描标题行带 x 961–1000 有 39 个深色像素，x 至 967；裁图（`crops/p2-paranao-title.png`）显示 `retenir` 末尾 `r` 骑在盒界上。
- 修复建议：缩短 gloss（如 `La règle à retenir` → `À retenir`）或缩小字号；修后重测。

### D3 — P7 `ERROS COMUNS` 框标题溢出奶油盒并超出版心右界（中）
- 严重度：中（17.2px，末字母在白底上且超出页右版心）
- 位置：P7 工具箱，奶油框 `(1439.5, 200, 422.5×935.5)`，标题基线 y=242，`ERROS COMUNS　Erreurs fréquentes`
- 归属：本版（核心同标题墨水右缘 1759.5，距盒右 1862.0 余 102.5px）
- 实测证据：PIL 真墨迹右缘 1879.2，超盒右 1862.0 计 **17.2px**，同时超过页右版心（1950−88=1862）17.2px；像素扫描标题行带 x 1862–1930 有 111 个深色像素，x 至 1879；裁图（`crops/p7-erros-title.png`）显示 `fréquentes` 末尾 `s` 落在白底上；全版 PIL 扫描中唯一的 `box_right` + `right_margin` 双命中。
- 修复建议：缩短 gloss（如 `Erreurs fréquentes` → 更短的等义表达）或缩小该框标题字号；修后重测墨水右缘 ≤ 盒右且 ≤1862。

### D4 — P1 刊头条（kicker 行）左右双双超出版心（轻）
- 严重度：轻（各约 4.4px）
- 位置：P1，y=330 行：`HEBDOMADAIRE PORTUGAIS　VOL.4　CONSCIÊNCIA NEGRA　GABARITO DO ENEM　A FINAL DA COPA`
- 归属：本版（法语家具标签 `HEBDOMADAIRE PORTUGAIS` 长于核心的 `葡萄牙语周报`；核心同行墨水 198.4–1751.9，居中且在版心内；法语版行被撑宽）
- 实测证据：PIL 真墨迹左缘 83.7（版心左界 88，超 **4.3px**），右缘 1866.4（版心右界 1862，超 **4.4px**）；像素扫描：右 x 1862–1949 有 76 个深色像素（x 至 1871），左 x 0–88 有 28 个深色像素（x 至 86）；裁图（`crops/p1-kicker.png`）整行顶满版宽。
- 修复建议：将该行字号 32→30 或重新分 spacing，使墨水收进 88–1862。

### D5 — P4 词汇注法语释义错：`o título` ≠ `champion`（轻）
- 严重度：轻（单个注词错义，无题键受影响）
- 位置：P4 Note 框，`o título champion`（`content34.py:134` 的 gloss 行）
- 归属：本版讲解层（根在核心中文注 `o título 冠军` 的歧义：`冠军` 既可指“冠军头衔”也可指“冠军本人”；法语取了“人”的义）
- 实测证据：
- 文中 `o título` 两处皆指头衔：`O Grêmio busca o sexto título`、`A Mercedes garantiu o título de construtores`；
- 本版自身体系内即用 `titre`：P8 答案注 146 `Grêmio vise un sixième titre`、147 `Palmeiras vise un cinquième titre`；
- 兄弟版对照：en 作 `o título title`（正确）；de `Meister`、es `campeón` 与 fr 同误，说明是中文注歧义的系统性误译，en 除外。
- 修复建议：仅改 P4 Note 行 `o título champion` → `o título le titre`；**不要**动共享映射 `tables_fr.py:37`（`冠军 → champion`，该映射还供 `a taça = le trophée du champion` 等正确处使用）。

### D6 — text.md P7 小标题夹英文内部语（轻；仅 text.md，PDF 无）
- 严重度：轻（读者可见的网站正文，PDF 不受影响）
- 位置：`2026-w47-pt-fr.text.md`，`### Frases da semana (verbatim from this issue)`
- 归属：本版导出（text.md 导出时带入的英文内部标注）
- 实测证据：`verbatim` 在 8 个 SVG 中出现 0 次；PDF P7 同处印的是法语 `(extraites mot pour mot de ce numéro)`，正确。text.md 中 `verbatim` 出现 1 次，即此行。
- 修复建议：删去括号，或按 PDF 用法语 `(extraites mot pour mot de ce numéro)`。

## 必查项核实结果

- (a) P1 框标题/副标题横向溢出：**复现**，D1（P1 数字框）+ D3（P7）+ D2（P2）+ D4（P1 kicker 行）。全版 PIL 真墨迹扫描：除此 4 处外无其他框标题/正文超出版心（`right_edge` 0 处超 1950 页边；`box_right` 仅 3 处，即 D1/D2/D3；`box_left` 0 处）。
- (b) P3/P5 右栏奶油框末行降部漫出框底：**未复现**。6 处最紧的框（desc-clear −0.9…−1.5px，皆为保守余量假警）全部经 PIL 真墨迹 + 像素条带扫描核实：0 墨水越过框底。最紧两例：P2 E VOCÊ 末行墨水底 908 vs 框底 909（余 1px）；P7 词框末行墨水底 1426 vs 框底 1431.5（余 5.5px）；其余 4 处（P3/P4/P5 E VOCÊ、P5 数字框）框底下 6px 条带 0 深色像素。早先一次误指的像素扫描（把相邻 gloss 框的下一行当成漫出）已用正确框坐标重做并推翻，见 GATE-LOG。
- (c) P7 toolbox clearance 实测：**已实测**，见 D3（标题横向溢出）与 (b)（词框底余 5.5px）。正典 creambox.py 全版扫描：P7 3 框，min inside clearance +4.5px（词框），min desc-clear −1.5px（余量假警，真墨 5.5px 余量）。occlusion 审计 0 flags（自检阳性对照 6 类全触发）。盒底无溢出，盒顶标题横向溢出 1 处（D3）。
- (d) text.md 第 E 节 type 标签本地化：**无中文残留**。§E 标题 `Traduza`（葡语）；text.md 与 8 个 SVG 的非 U+3000 CJK 均为 0；但发现英文内部语残留 1 处（D6）。

## 核实摘要

- 全文通读：印 PDF 8 页（cards 全页目视）+ text.md 535 行逐行读完；未见拼写、性数、变位、标点、截断、重复词问题。
- 150 题答案键逐题手验：**150/150 OK**（`keycheck-150.json`，每题有 key + 依据）。印 P8 答案与 text.md Respostas 机械比对 150/150 一致（Q140 em-dash 分隔、Q150 分节点两处解析假象已逐项核实澄清）。
- 事实：全部日期星期经 `date -d` 核验（8 日周日、7 日周六、15 日周日、16 周一、17 周二、18 周三、19 周四、20 周五、21 周六、22 周日、23 周一、27 周五、30 周一、12 月 6 日周日）；工作日数算术复核（16–30 日 15 天 = 10 工作日 + 5 周末/假日，第 10 个工作日 11 月 30 日；27–30 日区间与 edital 口径一致）；Copa 半决赛比分/射手/总比分/决赛 12 月 6 日 Mané Garrincha、F1 圣保罗站 Norris/Verstappen/Hadjar + 梅赛德斯车队冠军、Enem 8/15 日 + Edital 64/2026 §15.1 + 10 日工作日 + 1 月出分 + 5,051,345 报名、Zumbi 1695 年 11 月 20 日 + Lei 12.519/2011 + Lei 14.759/2023——以上均有外部来源核实（见 GATE-LOG）；第 36 轮 Palmeiras×Flamengo 在 21 日（35 轮为 18/19 日周中轮）与赛程注一致。
- 机械门：gates.py 16/16；occlusion 0 flags；creambox 全版扫描完成（见上）；p8 extract 150/150；p8 compare CLEAN，keydiff=[137, 138]（两处皆为正确的法语译文答案，已逐项裁决）；freeze baseline 8/8；freeze diff 仅 9 个 U+3000 增加；印/网文字层字节均为 46,525、词多重集差 0；P8 最小字号实测 9.75pt（= SOP §1.1 下限，174 个 span）；弯引号扫描：直引号 0，弯引号成对（P8 2 对），直撇号 52 处皆为法语省音（与兄弟版一致，无 SOP 强制要求，见 O1）；P1 头条 41 字符 ≤56；范文实数 88 词；8 句本周句在 text.md 中各出现恰好 2 次。
- 未改动任何源文件；未 commit、未 push。

## 未决事项

- O1：法语省音用直撇号 `'`（52 处，如 `l'`, `d'`, `s'`），而家具 `L'ÉDITION` 用 U+2019；兄弟版（en 8 处、de 2 处、es 2 处）亦然，SOP 无正文强制弯撇号规则。是否统一为 U+2019，请协调员定夺——不阻塞本版。
- O2：P7 首句法语 `Jour de la Conscience noire: jour férié national un vendredi.` 措辞电报体（缺逗号/语序紧），含义可辨，暂判可接受；另 P7 A2 `cair signifie « tomber un jour »` 与 B1 `attention à l'accent au passé d'abrir, garantir et sair` 为压缩式注，含义可辨，暂判可接受。如协调员要求打磨，可随 D1–D6 一并修。
- O3：P1 副标题 `L' ÉDITION` 有可见小空隙——KIT 已注明的 Newsreader 字体渲染特性（源文本为 U+2019 无空格），机制性旧项，非缺陷。

## 修复后要求

D1–D6 修后须重渲染 → 全部机械门重跑（gates / occlusion / creambox / p8 compare / freeze / 印网比对）→ 从头再做一轮全量复校，直至一整轮零问题（SOP §8）。重点复测：三处框标题墨水右缘、kicker 行版心、P4 Note 行、text.md 标题行。
