# PROOF-NOTE — 2026-W47 pt–fr (Portuguese target, French explanations) · proof1 (re-fanout rebuild)

- Proofreader: independent proof1 (pt-fr2), 2026-11-11
- Edition dir: `production/2026-w47/2026-w47-pt-fr/` (untracked in repo; zero writes — final SHA re-check at end of session identical to start)
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-fr2/`
- Core (read-only): `production/2026-w47/core-pt/` — core SVGs re-hashed by freeze before/after, unchanged

## §0 身份核对（SHA / 字节数，以磁盘为准，任务给定逐一核对）

| 文件 | 磁盘 SHA-256 | 任务给定 | 字节数 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `4b9f41475eb5ec7ec7e81cb372c50a58b6d7516c17a21fd1e2745ff7189f7653` | 一致 | 12,934,630 |
| `A-Lucerna-VOL4-web.pdf`（网） | `1f5cc5adc131bf16bd4a1f3a796e3470a399293f7f99e15f61f0ccfdb5080fb3` | 一致 | 1,141,286 |
| `2026-w47-pt-fr.text.md` | `39d06879d21b37ecca7b42ddb55214391bcb3c1aa6215cbcb39b184176e0a8e2` | 一致 | 37,699 |

三个 SHA 与任务消息一致，探针（`echo test | git hash-object -w --stdin`，在 `~/workspace/weekly-git` 内）通过；全程 `TMPDIR` 指向自有 scratch/tmp，未用系统 /tmp；解释器一律 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）。

## 结论：(a) 零缺陷，可定稿

本轮全量复校（SOP §8.4）零缺陷。首轮 6 项缺陷 D1–D6 全部复验存活（见下），150 题逐题手验 150/150，全部机械门绿。

**一项阈值冲突提请协调员裁定（不是缺陷，见 §5）：**任务门禁写 "P8 最小 PDF 字号 ≥10pt"，实测 9.75pt；但 SOP §1.1 明文规定答案字号下限即 9.75pt（"答案字号降到不低于 9.75pt（W46 现行众数）"），KIT 已记录 9.75pt，首轮亦接受。按 SOP 不判为缺陷；若协调员坚持 ≥10pt，则需改判——请裁定，未裁定前本结论按 SOP 作出。

## 缺陷清单

无。本轮发现 0 项缺陷。

## 首轮修复复验（D1–D6 全部存活，逐项源码行 + 实测值 + 渲染证据）

### D1 — P1 数字框标题 `数字 → Chiffres` ✓ 存活
- 源码：`tables_fr.py:123` `"数字": "Chiffres"`；渲染 `svg/p1-capa.svg` 标题 `A SEMANA EM NÚMEROS　Chiffres`，基线 y=823.18，23pt 粗体。
- 实测（23pt 真墨，boxtitle_core.py）：墨右缘 1392.8，盒右 1411.5，余 **+18.7px**（首轮缺陷：墨右缘 1424.0，超盒右 12.5px）。
- 渲染证据：独立真墨全扫 `ink.json` box_right 0 处；像素条带（scratch 重渲卡片 `build-copy/cards/p1-capa.png`，标题带 y795–845）：盒右间隙 x1412–1440 暗像素 **0**（间隙外 x≥1463 的暗像素是右侧 "A SEMANA, DIA A DIA" 框自身的正文，与标题无关）；全页目视标题完整在奶油盒内。

### D2 — P2 口诀标题 `口诀 → À retenir` ✓ 存活
- 源码：`tables_fr.py:57` `"口诀": "À retenir"`；渲染 `svg/p2-vida.svg` 标题 `PARA NÃO ERRAR　À retenir`，基线 y=642.02，23pt 粗体。
- 实测（23pt 真墨）：墨右缘 871.3，盒右 961.0，余 **+89.7px**（首轮缺陷：墨右缘 965.0，超盒右 4.0px）。
- 渲染证据：像素条带（标题带 y620–650，x961–1020）暗像素 **0**；全页目视 `retenir` 完整在盒内。

### D3 — P7 常见错误标题 `常见错误 → Erreurs` ✓ 存活
- 源码：`tables_fr.py:106` `"常见错误": "Erreurs"`；渲染 `svg/p7-lingua.svg` 标题 `ERROS COMUNS　Erreurs`，基线 y=242，23pt 粗体。
- 实测（23pt 真墨）：墨右缘 1750.8，盒右 1862.0，余 **+111.2px**（首轮缺陷：墨右缘 1879.2，超盒右 17.2px 且超出版心）。
- 渲染证据：像素条带（标题带 y215–250，x1862–1930）暗像素 **0**；全页目视标题完整在盒内。

### D4 — P1 kicker `sub330_size` 32→30 ✓ 存活
- 源码：`furniture.py:72` `FURN[fr].sub330_size: 30`；渲染 `svg/p1-capa.svg` y=330 行，30pt。
- 实测（独立真墨 `ink.json` p1_titles）：整行墨 139.5–1810.7（首轮 32pt 时 83.7–1866.4，双向超出版心约 4.4px），在 88–1862 版心内，左余 51.5px、右余 51.3px；KIT 称 139.5–1810.5，实测右缘 1810.7，差 0.2px，无实质差异。
- 渲染证据：像素条带（y300–340）：版心外左 x0–88 与右 x1862–1950 暗像素均为 **0**；全页目视刊头条居中、未顶版宽。

### D5（释义）— P4 `o título champion → o título le titre` ✓ 存活
- 源码：`content34.py:134` gloss 行 `… · o título le titre · …`；`tables_fr.py:38` 新增 SEG 键 `"冠军头衔": "le titre"`；`tables_fr.py:37` 共享映射 `"冠军": "champion"` 未动（仍供 `a taça = le trophée du champion` 等正确处使用，`tables_fr.py:40`）。
- 实测：P4 SVG Note 框逐字为 `o título le titre`；PIL 探针（KIT 称 4 行、末行右余 +68.5px、底余 +42.7px）与本轮 boxtitle log 一致（该 Note 框标题行 `Note — o agregado …` 右余 +19.3）；P8 答案注 146/147 自身体系亦用 `titre`。
- 渲染证据：P4 全页目视 Note 框行完整，无溢出。

### D6 — text.md P7 小标题英文残留 ✓ 存活
- 源码/文本：`2026-w47-pt-fr.text.md:433` 已为 `### Frases da semana (extraites mot pour mot de ce numéro)`；全版扫描 `verbatim` 出现 **0** 次（SVG 8/8 与 text.md 均 0）；PDF P7 同处印法语一致。

### D5（字体）— 只记录，不判
- 任务明示：拉丁解释层在 Noto Sans CJK SC 是已知待用户裁定的事，不作缺陷。实测：8 个 SVG 字体普查 Newsreader 947 / Noto Sans CJK SC 644 / Noto Serif CJK SC 27 / UnifrakturMaguntia 1；法语 gloss 元素（如 P1 `trois jours de congé`）确为 Noto Sans CJK SC 27pt bold。记录如上，不判缺陷。

## §1 150 题逐题手验（gate 5）

- **150/150 OK**（逐题记录 `keycheck-hand.json`；每题有 key + 依据）。
- 方法：text.md 535 行逐行读完（全部题干 + 答案提示 + Respostas）；8 页渲染卡片逐页目视；机械交叉：Respostas 解析 150 题 vs REG 键 0 差异、vs P8 印出键 0 差异（Q150 除外，见下）；150 个题干经规范化比对全部在其 SVG 页内找到（`scan8b.log`：0 缺失）。
- fr vs core 键差异仅 **[137, 138]**（`p8-extract-core.json` 独立抽取比对）：137 `Le vendredi 20 novembre est un jour férié national.` 与 138 `Palmeiras a gagné 5–4 aux tirs au but.` 均为葡萄牙语答案的正确法语译文，已逐项裁决，非缺陷。
- 重点复核：
  - **Q73**（三源同错教训）：题干 `Depois da prova, começa a ___.`，P5 正文 `Depois da prova, começa a espera pelo gabarito.`，键 `espera` 唯一正确。
  - **Q125**：第 36 轮 = 周末轮（35 轮为 18/19 日周中轮），Palmeiras × Flamengo 在周六 21 日，键 A 正确；与 P4 赛程表一致。
  - **Q102** `O feriado cai ___ sexta-feira.` 键 `numa`（正文 `cai numa sexta`）；**Q108** `Os finalistas ___ no fim de semana.` 键 `saíram`（7–8 日周末已决出）；**Q112** `Quando ___ o gabarito, o país respira.` 键 `sair`（P7 B2 规则：quando 后接 futuro do subjuntivo）。
  - **Q139/Q140**（法译葡）：139 `O gabarito oficial sai até o fim de novembro.`；140 `Anote as suas respostas e confira quando sair o gabarito oficial.`（quando 后 `sair` 未来虚拟式正确；印出行为 em-dash 分隔，是解析假象，键一致）。
  - **Q150**：开放写作题，无唯一答案；印出键 `✓` + 范文 88 词（实数）；REG 键改为 `(exercice ouvert — texte modèle ci-dessous)`，为登记标签变化，不影响印出答案。
  - **Q44–46 / Q133–136** 造句题键与题面词序逐项核对无误；**Q25–28 / Q52–55 / Q141–144** 配对题键逐项核对无误；**Q56–59** 比较级 mais/mais/mais/menos 与数值一致（16h30 早于 17h 为 mais cedo；两天少于一周为 menos）。
  - **Q83–87** 图表读数：16–30 日 15 天 = 10 工作日 + 5 周末/假日，第 10 个工作日为期限，算术复核无误。
  - **Q65–69 / Q80–82 / Q88–92** Enem 事实键与 P5/P6 正文一致（15 日第二天、非官方答案当晚出、官方答案 11 月底、个人成绩 2027 年 1 月）。
- 事实与日期：`date -d` 核验 2026-11-07（六）、08（日）、14（六）、15（日）、16（一）、17（二）、18（三）、19（四）、20（五）、21（六）、22（日）、23（一）、27（五）、30（一）、12-06（日），全部与刊载一致。本轮重建未改任何事实（仅 D1–D6 + 核心 gloss），首轮外部来源核实（Copa 半决赛比分、F1 圣保罗站、Enem Edital 64/2026 §15.1、Zumbi 1695、Lei 12.519/2011、Lei 14.759/2023、5,051,345 报名）依然有效，不再重复拉取。

## §2 全文通读与版面目视

- 印 PDF 8 页（scratch 重渲卡片，全页目视）+ text.md 535 行逐行读完；未见拼写、重音、性数、变位、标点、截断、重复词问题。
- P1 头条 41 字符 ≤56；范文实数 88 词（80–100）；8 句本周句在 text.md 中各出现恰好 2 次。
- P3/P5 `Complétez avec les mots de l'encadré.` 栏底 intro + 次栏词表、P4 `B AS PALAVRAS` 栏底孤头，均为核心流式行为（与 core-pt 一致），非缺陷。P2/P3/P5/P6 栏间大面积空白为文章在固定练习带上方结束的核心版式，非缺陷。
- P7 引言区末行法语基线 2380.17 < 2404 预览框顶（gates.py 实测），无遮挡。

## §3 机械门摘要（详见 GATE-LOG.md）

- run.py rc=0，TOTAL 150（A2 48 / B1 71 / B2 31；页分布 10/18/18/18/18/18/12/38），0 溢出；scratch 重建 SVG 与现盘 8/8 字节一致；scratch 重渲印 PDF 与交付件 SHA 完全一致。
- freeze 核心比对（--build core-pt，--core-svg core-pt/svg）8/8；版内自比对补充 8/8；freeze diff 新增 CJK 仅 U+3000 ×9（P1:2，其余每页 1）。
- occlusion 真实审计 0 flags（自检 6 类全触发）；p8-compare.json 本体 CLEAN，keydiff=[137, 138]；keycheck 149/150（唯一 Q150 已知抽取例外）。
- 印/网文字层逐页 token 差 0（993/825/761/931/811/859/883/2566），pdftotext 字节一致（110,813）；P8 最小字号 9.75pt（见 §5 阈值冲突）；check_s11（pt 适配版）全 PASS；sweep 0/0/0；斜体 span 印 1 = 网 1。
- 盒标题真墨（23pt 粗体）：全部 31 框标题右余为正，最紧 +12.0px（P1 EM POUCAS PALAVRAS）；occlusion 0 与 boxtitle 0 之外，独立真墨全扫 box_right/box_left/box_bottom 均为 0。
- creambox：5 处负值均为框下标题（owner-rect=NONE 假警）；最紧真墨底余 +0.3px（P2/P3/P4 E VOCÊ 框，墨在盒内），+0.4px（P5 E VOCÊ），+4.2px（P7 词框）。
- 弯引号成对（“” 各 2，直引号 0）；无汉字/假名/韩文（仅全角分隔符 ｜ U+FF5C，核心亦有，见 §4）；禁词/简体残留 0；`..` 仅出现在 `...` 省略号内（45 处，印/网一致）；VOL.3 仅见于 P7 读者园地披露（允许）。

## §4 已核实、非缺陷事项

- 直撇号 `'`（SVG 52 处，皆为法语省音 `l'`/`d'`/`s'`/`n'`/`qu'`；text.md 22 处），与兄弟版一致，SOP 无正文强制弯撇号规则；U+2019 仅 1 处（P1 `L'ÉDITION`）。
- `L' ÉDITION` 副标题可见小空隙：Newsreader 渲染特性，源文本为 U+2019 无空格，机制性旧项。
- P7 A2 `cair signifie « tomber un jour »`、B1 `attention à l'accent au passé d'abrir, garantir et sair` 为压缩式注，含义可辨，可接受（首轮 O2 同判）。
- P8 页眉 `Une courte note par réponse　✓ marque le texte modèle` 墨右缘恰为 1862.0（= 版心，超 0.0），非缺陷。
- P2/P3/P4 E VOCÊ 框末行真墨底余仅 +0.3px：墨在盒内、无越界，印刷尺度下为亚像素余量，非缺陷（与首轮同判；当年首轮实测 1px）。
- SVG 用 `Note —` 而 text.md 用 `Note｜`：同一 Note 行的分隔符写法在两种导出中不同（内容一致），首轮已是如此，非本轮回归，非缺陷。
- 核心 P8 有重复裸 `138.` token，本版仅一个，非缺陷。P6 `27–30 novembre` 区间与 Edital §15.1 口径一致（20 日假期是否计为工作日之争，本期印两种日期）。

## §5 提请协调员裁定（阈值冲突，非缺陷）

- **P8 最小 PDF 字号**：任务门禁写 "≥10pt"，三法实测均为 **9.75pt**（minfont.py P8 最小有效字号 9.75pt，374 runs，0 处 <9.75；check_final.py 答案区 span 最小 9.75pt，186 spans；check_s11_pt.py SVG 最小字号 13.0 单位 = 9.75pt）。SOP §1.1 明文允许 9.75pt（答案字号下限，W46 现行众数），KIT §6 已记录 9.75pt，首轮亦接受。核心 P8 最小为 13.5 单位（10.125pt），法语版因法语答案注更长而用 13 单位（p8_keys_small，KIT §6），属于 SOP 让步阶梯第 4 步。按 SOP 不判为缺陷；若任务 "≥10pt" 为硬性要求，请协调员裁定以何为准。

## §6 文件（scratch）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`、`keycheck-hand.json`（150 题手验逐题记录）、`keycheck-150.json`（REG 键 vs 印出键机械比对）
- 证据：`run.log`、`gates.log`、`freeze-core.log/.json`、`freeze-ed.log/.json`、`freeze-diff.log/.json`、`occlusion.log/.json`、`p8-extract.log/.json`、`p8-extract-core.json`、`p8-compare.log/.json`、`keycheck.log`、`check-final.log`、`fr-textdiff.json`、`fr-p8size.json`、`minfont.log`、`italic.log`、`check-s11.log`、`sweep.log`、`boxtitle.log`、`ink.log/.json`、`creambox.log`、`creambox-diag.log`、`scan8.log`、`scan8b.log`、`verify150.log`、`render.log`、`webpdf.log`、`print.txt`、`web.txt`、`web-rerender.pdf/.txt`（网 PDF 仅在 scratch 重渲，未覆盖交付件）
- 生产目录零写入；core-pt 只读（freeze 前后重哈希无变化）。

## §7 补充检查（pt-it 复校触发，独立量测、独立判定）

### S1 — P2「PARA NÃO ERRAR」框标题：通过，无漫出（非缺陷）
- 对象：`svg/p2-vida.svg` 标题元素 x=556.5、基线 y=642.02、23pt 粗体、Noto Sans CJK SC，`PARA NÃO ERRAR　À retenir`；框 x[538.5, 961.0]；gloss 源 `tables_fr.py:57`。
- PIL 真墨（`occlusion_audit.ink_box`，针对性重测，与 boxtitle log 独立重复）：墨 L=556.5、R=**871.5**，框右 961.0，余 **+89.5px**（boxtitle log 另法：右 871.3、余 +89.7；两法差 0.2px，结论一致）；左余 18.0px。pt-it 版同框漫出 −59.5 与本版无关：本版 gloss `À retenir` 比意语 `La regola da ricordare` 短约 150px。
- PDF 像素交叉验证（scratch 重渲卡片 `build-copy/cards/p2-vida.png`，标题带 y620–650）：框右外 x961–1020 暗像素 **0**；带内暗像素 x 范围 559–874，全部在盒内。
- 渲染证据：裁图 `crop-p2-paranao.png`（x520–980、y595–660，2× 放大）目视标题末端距盒右有大段奶油空位。结论：**通过，不记缺陷**。

### S2 — P1 顶栏标语「Le portugais que lit le Brésil」：语法成立，非缺陷
- 对象：`tables_fr.py:200` `"读巴西人正在读的葡萄牙语": "Le portugais que lit le Brésil"`；渲染于 P1 顶栏中段 `TODA SEMANA EM PORTUGUÊS　Chaque semaine　Le portugais que lit le Brésil`（17pt，见下几何）。
- 独立法语语法判定（**与协调员初判相反，结论：原句正确，不颠倒，不记缺陷**）：
  - 关系代词 **que 恒为直接宾语（COD），绝不作主语**；主语关系代词是 **qui**。规则（公开语法来源：live-french.net《Les pronoms relatifs》、monfrancais.fr、sandrineescoffier.com，三家一致）：`qui` = sujet，后直接跟动词；`que` = COD，后跟主语 + 动词（例 `le livre que je lis`、`le film que j'ai vu`）。
  - 拆解本句：`Le portugais [que lit le Brésil]` —— `que` = COD，即先行词 `le portugais`（葡语是被读的对象）；从句主语是动词后置的 `le Brésil`（巴西），这是法语关系从句中名词主语后置的标准语序（例 `le livre que lit Marie` = Marie 读的那本书）。
  - 因此本句意为「巴西读的那种葡萄牙语」= 中文「巴西人正在读的葡萄牙语」，主客与原文一致，**无颠倒**。协调员初判「que = le portugais 作主语」与上述规则相抵触：若 `le portugais` 作主语，关系代词须为 `qui`，即 `Le portugais qui lit le Brésil` 才表示「读巴西的葡语」——该写法在本版不存在。
  - 补充：意语 `che` 兼作主语/宾语，故 pt-it 同句确有歧义/颠倒之虞；法语 `que` 无此歧义，两版不可类推。
  - 备用改法（仅供协调员参考，不建议改）：`Le portugais que le Brésil lit`（主语前置的 SVO 语序，同义、更直白）。实测该改法与现句宽度完全相同（见下），改与不改均无版式风险；但现句语法已成立，**无修改必要**。
- 宽度量测（17pt 真墨，`ink_box`）：
  - 现句整行 `TODA SEMANA EM PORTUGUÊS　Chaque semaine　Le portugais que lit le Brésil`：墨 600.9–1231.7，宽 630.8px，版心内左余 512.9px、右余 630.3px。
  - 假想改后整行（`…Le portugais que le Brésil lit`）：墨 600.9–1231.7，宽 630.8px，**与现句完全相同**（同字符重排）；单段宽度亦同为 218.0px。改后仍在版心内，余量不变。
  - 前提勘误：任务称「该行 17pt 居中于 x=975」不准确——实测该元素为 `text-anchor="start"`、x=600.9 起排（墨中心 916.3，非 975）；但无论按何种居中理解，该行左右余量均在 500px 以上，无版式问题。
- 渲染证据：裁图 `crop-p1-strip.png`（x80–1870、y70–115）目视标语完整、居中段无溢出。
- 结论：**S2 不记缺陷**；S1、S2 均不改变 §0 结论（a）零缺陷、可定稿。
