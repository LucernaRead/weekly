# GATE-LOG — 2026-W47 pt-it (proof1, re-fanout 重建版复校)

- Proofreader: independent proof1 (subagent proof-pt-it2), 2026-11-11
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-it2/`
- Tooling: `~/workspace/weekly-git/tools/venv/bin/python` throughout (Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3); `TMPDIR` set to the scratch `tmp/` dir for every run.
- Canonical creambox: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py` (md5 `ee7a55d8b2057cf4ad42a97bb1197383`, 与首轮一致）。
- 生产目录零写入：所有构建/审计都在 scratch 副本或只读输入上跑；收工复验三份 SHA 与任务值一致（见 §0）；`git status` 版目录仅为 untracked，无修改。

## §0 身份核对（磁盘为准，开工与收工各验一次）

| 文件 | 磁盘 SHA-256 | 字节 | 与任务一致 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `6c8a5f3db220dcdfba6e0904b12ec66e37062f0007cfaeb9aed71b208e9911ce` | 12,930,828 | ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | `5ebf28b436f60fe0b59dcff89a4f1bf62dc0aa93bf4a4e2e7da9a2e965114e89` | 1,137,080 | ✓ |
| `2026-w47-pt-it.text.md` | `37c1980caacc6cef28d9df50133b09b45a51a8d4f17296e34412b2cd88285209` | 37,419 | ✓ |

探针：`echo test | git hash-object -w --stdin` 在 repo 内返回 `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0（首次在 repo 外跑因不在 git 仓失败，属探针位置问题，非 /dev/null 缺失；/dev/null 存在）。

## §1 机械门实跑证据（全部自己跑，不信 KIT）

| 门 | 命令 / 口径 | 结果 | 日志 |
|---|---|---|---|
| run.py（scratch 副本） | `build-copy/` 内 `python -u run.py` | **rc=0，TOTAL 150**（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；范文 88 词）；0 OVERFLOW / 0 TOO WIDE；重建 8 张 SVG 与交付 SVG **逐字节一致 8/8** | `run-proof1.log` |
| gates.py（scratch 副本） | `build-copy/` 内 `python -u gates.py` | **16/16 PASS，FAILURES: none** | `gates-proof1.log` |
| occlusion 真实审计 | `tools/occlusion_audit.py <版 svg> --json occlusion.json`（审目录，非 --selftest；自检 6 类阳性全触发作对照） | **0 flags**（`flag_count: 0`） | `occlusion.log`、`occlusion.json` |
| p8 extract | `tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150 --json p8-extract.json` | **150/150 noted** | `p8-extract.log`、`p8-extract.json` |
| p8 compare | `tools/p8.py compare --core-p8 ../core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150 --json p8-compare.json` | **CLEAN**（`status: CLEAN, missing: [], extra: null, keydiff: [137, 138]`——直接读 `p8-compare.json` 本体） | `p8-compare.log`、`p8-compare.json` |
| freeze baseline（标准核心比对） | `tools/freeze.py baseline --build production/2026-w47/core-pt --core-svg production/2026-w47/core-pt/svg --out freeze-core` | **8/8 SVGs byte-identical**（repointed: none；core 完整性：8 文件复哈希未变）。`freeze-core/build-copy/` 内确为 core-pt（有 core 的 `2026-w47-pt-zh-cn.text.md`），非版目录，证据有效 | `freeze-core.log` |
| freeze baseline（版内自比对，补充） | `... baseline --build production/2026-w47/2026-w47-pt-it --core-svg .../2026-w47-pt-it/svg --out freeze-ed` | **8/8** | `freeze-ed.log` |
| freeze diff | `tools/freeze.py diff --core-svg ../core-pt/svg --edition-svg svg --json freeze-diff.json` | rc=0；新增 CJK 字符仅 **U+3000，共 9 个**（P1 2 个、其余每页 1 个，家具分隔符） | `freeze-diff.log`、`freeze-diff.json` |
| 印/网文字层 | `pdftotext -layout` 两版 + 词集比对 | 各 **110,388 字节，逐字节相同**；词集 2,032 词；**only-in-print 0、only-in-web 0** | `print.txt`、`web.txt` |
| P8 最小字号（PDF） | PyMuPDF 取印/网 P8 全部 span | **9.75pt（174 spans）**，其余 ≥10.5pt；印/网一致；全文档最小亦 9.75pt。**= SOP §1.1 下限（SOP.md:35「答案字号降到不低于 9.75pt」），不低于下限**。说明：任务写「≥10pt」，与 SOP 下限 9.75pt 字面不符；以 SOP 与 check_s11 的 9.75 阈值为准判 PASS，见 §6 注记 | （本文件记录） |
| check_s11（pt 改编版） | 自写 `check_s11_pt.py`（en 原版为 en 家族专用：页名/注册表结构不同，pt 无对应脚本，故按同一检查项改编：纸底色、色集、VOL 计数、徽章数/色集、P8 最小字号、P8 题号、H 头） | **ALL §1.1/P8 CHECKS PASS**（rc=0）：8 页纸底 `#fbfaf6` 齐全；色集 core=edition=21 色，extra/missing 皆无；VOL.4/VOL.5 逐页计数与 core 一致；徽章 8 页逐页同数同色（10/15/18/15/18/18/12/35 = 141 枚）；P8 SVG 最小字号 13.0（= 9.75pt）；P8 题号 113–150 齐全；H 头 `ESCREVA VOCÊ`、`Scrittura`、`✓` 齐全 | `check_s11.log`、`check_s11_pt.py` |
| creambox 全版扫描 | canonical `creambox.py svg/*.svg` | 31 盒；**D1–D3 已修（见 §2）**；其余负 clearance 4 处皆为已裁决假阳性（见 §4）；desc-clear 负值 6 处已真墨迹复验为非缺陷（见 §4） | `creambox.log` |
| boxtitle 真墨 | 自写 `boxtitle_ink.py`（svglib `_pil`/`_runs`，与 gates.py 同路径；每标题按其**自身 SVG 字号**量）+ 交付 PDF 300dpi 像素复验 `pixel_boxtitle.py` | **1 处真溢出 D6（见 PROOF-NOTE）**；其余盒标题全在框内；D4/D5 修复存活（见 §2） | `boxtitle-ink.log`、`pixel_boxtitle.log` |
| 溢出横扫（gate 7） | 自写 `sweep_all.py`：每奶油盒 × 盒列 ±60px 窗口内全部文本，真墨迹量横/纵向 | 仅 D6 一处基线在盒内的 H-OVER；其余旗标皆为盒外章节标题/正文（见 §4） | `sweep-all.log` |
| 150 题手验 | 自写 `keycheck.py`：印刷键（p8 extract）× 核心键 × text.md 行内答案 × Respostas 汇总 四源比对 + 逐题读题干配对 | **机械 0 不符**；逐题手验 **149/150 PASS + Q150 开放写作 ✓**（任务预期 149/150，Q150 为已知抽取例外，见 §3） | `keycheck.log`、`keycheck-150.txt`、`keycheck-150.json` |
| 引号/CJK/禁词 | 自写 `sweep_text.py`：SVG 文本节点 + text.md + 印/网 pdftotext | 弯引号成对（见 §5）；CJK 仅 U+3000；渲染文本禁词 0；简体残留 0；非省略号 `..` 0 | `sweep-text.log` |
| 逐页看图 | 印 PDF 8 页 110dpi 全页 + 5 张 300dpi 裁图 | D6 像素确认；D1–D3 目视确认已修；其余各页无溢出/重叠/压页脚 | `view-p*.png`、`crop-*.png` |

## §2 首轮缺陷 D1–D5 复验（全部已修并存活）

| 项 | 首轮值 | 本轮实测 | 结论 |
|---|---|---|---|
| D1 P1「EM POUCAS PALAVRAS」框 | 框底 2310，末行基线 2327.6 在框外 | 框底 **2348.0**，末行基线 2327.6，clearance **+20.4**，desc-clear +14.4（与 core-pt 逐一一致：同框底 2348.0） | 已修 ✓ |
| D2 P3「A SEMANA, DIA A DIA」框 | 框底 525，碎片「16h30.」基线 540.6 在框外 | 框底 **551.0**，末行基线 540.6「16h30.」，clearance **+10.4**，desc-clear +3.9（core 同值） | 已修 ✓ |
| D3 P6「O CAMINHO ATÉ O GABARITO」框 | 框底 840，末行基线 840.8 骑边 | 框底 **854.0**，末行基线 840.8「Página do Participante.」，clearance **+13.2**，desc-clear +6.9（core 同值） | 已修 ✓ |
| D4 P7「A PALAVRA」标题 | gloss「La parola della settimana」墨右 +29.5 溢出 | 标题现为「A PALAVRA　La parola」（`content7.py:93`，fs=23；`tables_it.py:136`）；PIL 真墨墨右 1710.5，clear **+151.5**（KIT 称 +151.6，差 0.1）；交付印 PDF 300dpi 像素墨右 1711.0，clear **+151.0**；网 PDF 同 | 修复存活 ✓ |
| D5 P1「NESTA EDIÇÃO」标题 | gloss「In questo numero」墨右 +2.5 溢出 | 标题现为「NESTA EDIÇÃO　Questo numero」（`content12.py:89`，fs=24；`tables_it.py:138`）；PIL 真墨（fs=24）墨右 1838.5，clear **+23.5**（KIT 称 +23.3 at fs=24，差 0.2）；交付印 PDF 像素墨右 1840.3，clear **+21.7**；网 PDF 同 | 修复存活 ✓ |

字号口径说明（任务 gate 6）：本轮每标题按其**自身 SVG 字号**量真墨——D4 标题 fs=23、D5 标题 fs=24（SVG 元素与源码一致）。pt-en 案「24pt 量的 +40.5/+32.5 是错字号假数」是指该版标题实际 fs=23 却按 24 量；本版 D5 标题实际就是 fs=24，按 23 量反而会低估。两法交叉验证一致：PIL（自身字号）与交付 PDF 像素的墨右差 ≤2.9（D5：1838.5 vs 1840.3；D4：1710.5 vs 1711.0；D6：1020.5 vs 1023.4），以 PDF 像素为准结论不变。

## §3 150 题手验（keycheck 149/150 + Q150 ✓）

- 机械四源比对：印刷键 = 核心键（仅 137/138 例外）= text.md 行内答案 = Respostas 汇总，**0 不符**（Q150 除外：印刷键 `✓`，行内为开放写作注，Respostas 为 `✓ + 范文指引`）。
- 逐题读题干配对（`keycheck-150.txt` 全表已逐行读完）：**149/150 PASS**。Q73「Depois da prova, começa a ___.」→ `espera` 与题干配对正确（与 Q70「começa a espera pelo ___」→ `gabarito` 各配各题，无三源同错）；Q125 rodada 36 已外部核实（见 §7）；Q137/138 意大利语译文正确（见 PROOF-NOTE）。
- Q44 模型句在词表外补「de novembro」（`o dia 20 / é / feriado nacional → O dia 20 de novembro é feriado nacional.`）：与核心逐字一致，属造句题范文惯例，非缺陷。

## §4 creambox / sweep-all 逐项裁决（除 D6 外）

creambox 负 clearance 4 组（皆为盒下章节标题/正文，假阳性，与首轮同文同值）：
- P1 numbers 框 BELOW-WINDOW +37.0「AGORA VOCÊ」：下一节标题。
- P2 日程框 BELOW-WINDOW +32.0「Atenção: …」：框下正文段落。
- P3 Nota 框 BELOW-WINDOW +37.0「UM DIA, DOIS SENTIDOS」：下一节标题。
- P6 图表框 BELOW-WINDOW +42.0「EXERCÍCIOS」：下一节标题（两框同值）。

desc-clear 负值 6 处（本轮独立真墨迹复验，非复述首轮）：行内均无降部字母，真墨底距框底 **+4.5~+5.4**（首轮称 +4.2~+4.9，口径差 0.5 内，结论一致），全部非缺陷：
- P2 −1.0「Scrivi due frasi e inviale.」基线 904.0，墨底 904.0，框底 909.0；
- P3 −0.9「frasi e inviale.」874.9 / 874.9 / 880.0；
- P4 −1.5「due frasi e inviale.」871.5 / 871.5 / 876.0；
- P5 −1.1「2027.」507.6 / 507.6 / 513.0；
- P5 −0.9「inviale.」806.4 / 806.4 / 811.5；
- P7 −1.5「memoria della lotta e della cultura.」1456.5 / 1456.5 / 1461.0。

sweep-all 其余旗标裁决（`sweep-all.log`）：
- P2/P5 两处「Nota — …」行基线在上盒底之下 50px：实为**下邻盒内首行**（P2 Nota 在 y=858.02 盒内，P5 同类），该盒内无 H-OVER 旗标；为窗口重叠假阳性，非缺陷。
- 其余 H-OVER 皆为盒外章节标题（基线在盒顶之上，如 P2「O FERIADÃO, DIA A DIA」y=1594 在盒 y=1618 之上；P6「O FIM DE NOVEMBRO EM NÚMEROS」y=1576 在盒 y=1594 之上）：非盒内容，非缺陷。
- L-OVER −1.0 两处（P1「AGORA VOCÊ」墨左 988.0 vs 盒左 989.0；「A PALAVRA DA SEMANA」1438.5 vs 1439.5）：两行基线皆在盒底之下，属盒外标题，1px 为字形侧轴承，非缺陷。
- V-OVER：0 处。

boxtitle 其余实测值（PIL 真墨，自身字号；框右缘 1862，D6 除外全在框内）：
- P1「A SEMANA EM NÚMEROS　In cifre」+28.5；「A SEMANA, DIA A DIA」+129.5；「EM POUCAS PALAVRAS　IN BREVE」**+3.5**（最紧；PDF 像素复验 +3.1，双法一致，在框内）；「NESTA EDIÇÃO　Questo numero」+23.5（D5 已修）。
- P2「VOCÊ SABIA?」+250.5；「E VOCÊ?　Parla di te」+161.5；「SEX 20/SÁB 21/DOM 22/SEG 23」+282.5/+282.5/+264.5/+282.5。
- P3「A SEMANA, DIA A DIA」+159.5；「E VOCÊ?」+161.5；「PALAVRAS DA MEMÓRIA」+145.5。
- P4「OS FINALISTAS」+233.5；「E VOCÊ?」+161.5。
- P5「O PLANO DA ESPERA」+173.5；「OS JOVENS EM NÚMEROS」+100.5；「E VOCÊ?」+161.5。
- P6「O CAMINHO ATÉ O GABARITO」+91.5；「LER OS NÚMEROS」+190.5；「A CONTAGEM」+505.0；「DOIS GABARITOS」+548.0。
- P7「ERROS COMUNS　Errori frequenti」+17.5（PDF 像素 +18.5）；「A PALAVRA　La parola」+151.5（D4 已修）；「CARTAS DOS LEITORES」+143.5。
- 非盒粗体文本全页边扫描（全部文本、任意字重）：墨右最紧为 P1 测验说明 +0.5、P8 137 键行 +0.5、页脚「Pagina N di 8」+0.3；墨左无 <88 者。见 §6。

## §5 引号 / CJK / 禁词（sweep-text.log）

- 弯引号：U+201C/U+201D 全版仅 P8 各 2/2（Q139/140 意语句），P1–P7 0/0；U+2019 仅 P1 徽标「L'EDIZIONE」1 处；ASCII 双引号 0；« » 全版平衡（P7 33/33；text.md 40/40；印/网 pdftotext 40/40）。
- CJK：SVG 文本节点仅 U+3000（每页 13–20 个，家具分隔符）；text.md 0；印/网 pdftotext 0；freeze diff 新增 CJK 仅 U+3000（9 个）。
- CJK 孤儿标点：0（无 `。、` 等 CJK 标点；U+3000 仅作分隔符，无行首/行末孤儿）。
- 禁词（渲染文本节点 + text.md）：Ucrânia/Israel/Palestina/Trump/Putin/Rússia/Estados Unidos/EUA/guerra/SOP/proofread/VOL.3/VOL.2/lorem/TODO/XXX 皆 0。注：裸 grep 全 SVG 文件时 SOP/XXX/EUA 有命中，上下文皆为**内嵌图片 base64**，非渲染文本，特此说明。
- 简体残留：简体专属字表 0 命中；`翻译`/`中文` 0；非省略号 `..` 0（45 处 `..` 皆在 `...` 内）；`?Scrivi` 合并 0；双空格 0。

## §6 注记（只记录、不判缺陷；与任务口径出入处）

1. **P8 最小字号 9.75pt vs 任务「≥10pt」**：实测印/网 P8 最小均为 9.75pt（174 spans）。SOP §1.1 下限即 9.75pt（「答案字号降到不低于 9.75pt」），check_s11 阈值亦为 9.75，KIT 与首轮同一数值。9.75pt 恰为下限、不低于下限，判 PASS；任务「≥10pt」与 SOP 字面不符，已如实记录，供协调员复核。
2. **P8 注行墨右 +0.4**：「Una breve nota per risposta　✓ segna il testo modello」（fs=19.5，y=1302.0）PIL 真墨墨右 1862.4，超右版心 +0.4（首轮方法测 +0.2）。在 ru O3 的 0.5px 边际带内，字形完整未裁，判非缺陷。同类家具行墨右：P2「Três dias…」−0.4、P2–P6「Risposte a pagina 8…」−0.2、P1 测验说明 +0.5——皆为贴版心家具的正常侧轴承，≤0.5 皆不计缺陷。
3. **拉丁解释层字体**：意大利语讲解层用 Noto Sans CJK SC（SOP §1.1 规定拉丁读者语家具用 Newsreader 之外的已知待裁定事项，任务明示只记录不判）。本轮仅记录，不作缺陷。
4. **P1 顶栏标语意译**：`tables_it.py:201`「读巴西人正在读的葡萄牙语」→「Il portoghese che legge il Brasile」（`content12.py:15`）。直译回中文为「读巴西的葡萄牙语」，与原文「巴西人正在读的葡萄牙语」主客颠倒，疑似意译偏差；但属标语修辞、语法完整、首轮未 flag，本轮仅记观察、不计缺陷，由协调员定夺是否改「Il portoghese che i brasiliani leggono」。
5. **P7 字体问题**：同注记 3（任务已明示只记录不判）。
6. Q44 模型句补「de novembro」：见 §3，核心一致的范文惯例，非缺陷。
7. P1「AGORA VOCÊ」等小节标题无奶油框、P3「B AS PALAVRAS DO TEXTO」标题孤悬栏底、P2/P5 大段留白：皆为核心固有排版行为（首轮已披露），内容齐全，非缺陷。

## §7 外部事实来源（live 核查，2026-11-11；关闭首轮 O2/O3）

- **Q125 / rodada 36（首轮 O2，已关闭）**：Palmeiras × Flamengo，36ª rodada，2026-11-21 周六 16h30，Nubank Parque——CBF 10 月 30 日公布的 35/36 轮详细赛程（Gazeta Esportiva 10-30、Lance 10-30、Flashscore、brasileirao.com.br 11-07 均同）；「o jogo que pode decidir o título」亦同。另：35 轮 Flamengo × Athletico-PR 在周三 18 日 20h30 马拉卡纳（brasileirao.com.br）与本版 P4 表一致。
- **O Grêmio busca o sexto título / décima final；O Palmeiras busca o quinto título（首轮 O3，已关闭）**：Grêmio 五冠（1989/1994/1997/2001/2016），本次为第十次决赛、争第六冠（portaldopalestra 11-08、mktesportivo 11-08、valeeuropeunoticias 11-09）；Palmeiras 四冠（1998/2012/2015/2020），争第五冠（同上）；决赛 12 月 6 日单场 Mané Garrincha（同上）。
- **Singapura × Brasil 周二 17 日 7h**：CBF 官网 10 月 29 日征召公告——巴西 11 月 14 日 7h15 对日本、17 日 7h 对新加坡，皆在新加坡国家体育场（edmaisesporte 11-09/11-10 同）。
- **Enem**：2026 年 5,051,345 人确认报名（「Mais de 5 milhões」，sisu.pro.br 11-09、blogdovestibular 同）；Edital nº 64/2026 第 15.1 条「até o 10º dia útil após o 2º dia」，第 2 日为 11 月 15 日，计入 11 月 20 日国定假日则第 10 个工作日 = 11 月 30 日（blogdovestibular、sisu.pro.br 同；Ulti 11-09 注「27–30 日之间，视 20 日假期是否计入」与本版 P6「entre 27 e 30 de novembro, conforme a contagem」逐字一致）；个人成绩 2027 年 1 月中旬、Página do Participante（同上）；第 2 日 90 题、13h30–18h30（同上）。
- **半决赛比分 / F1（首轮已 live 核实，本轮未重复检索；与 P4 逐字相符）**：Atlético-MG 1–1 Grêmio（11-07，首回合 2–0，总比分 3–1）、Vasco 2–1 Palmeiras（11-08，点球 5–4，首回合 1–0，总比分 2–2）；F1 圣保罗站 Norris 冠军、Verstappen 第 2、Hadjar 第 3、Mercedes 锁定车队冠军。
- **日期星期**（`date -d`，与首轮同）：2026-11-16 周一、11-15 周日、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日。
- **P6 工作日算术**：11 月 16–30 日 15 天 = 10 工作日（16、17、18、19、23、24、25、26、27、30）+ 5 周末/假日（20、21、22、28、29）；第 10 个工作日 = 11 月 30 日。

## §8 判为非缺陷的项（摘要，详见上文）

1. 首轮 O4 的 P8 注行 +0.2（本轮 +0.4）：0.5 边际带内，非缺陷。
2. 6 处 desc-clear 负值：真墨迹复验，余量 +4.5~+5.4，非缺陷。
3. 4 处 creambox BELOW-WINDOW + 6 处 sweep-all 盒外标题：皆为盒外章节标题/正文，非缺陷。
4. 「o título → titolo」（core fix2 D5 gloss）、「cair → cadere in un giorno」：五版 pt fan-out 共用 gloss 惯例，非本版错误。
5. ASCII 省略号撇号（c'è、l'attesa）：全 program 惯例。
6. 「L'EDIZIONE」徽标间距：SVG 文本 `L'EDIZIONE`（U+2019、无空格），字体渲染特性。
7. Q44 模型句补「de novembro」：核心一致的范文惯例。
8. 顶栏标语意译疑似（§6.4）：仅观察，不计缺陷。
9. D5 字体问题（§6.3/6.5）：任务明示只记录不判。
