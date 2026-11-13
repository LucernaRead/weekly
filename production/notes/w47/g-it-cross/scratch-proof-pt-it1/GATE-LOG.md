# GATE-LOG — 2026-W47 pt-it (proof1, independent re-runs)

- Proofreader: independent proof1 (subagent proof-pt-it1), 2026-11-11
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-it1/`
- Tooling: `~/workspace/weekly-git/tools/venv/bin/python` throughout; `TMPDIR` set to the scratch `tmp/` dir for every run (system /tmp untouched).
- Canonical creambox: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py` (md5 `ee7a55d8b2057cf4ad42a97bb1197383`).
- All logs below live in the scratch dir; source files were not modified (final SHA re-check: print/web/text.md identical to §0 of PROOF-NOTE).

## §0 与 KIT 不符处（磁盘为准）

1. **Occlusion：KIT 称 1 flag，我重跑 0 flags。** 原因查明，非 SVG 变化：构建者 `it-occlusion.json`（2026-11-11 03:52 UTC）记 P1 LINEX flag，墨顶 2312.8、line@197；我重跑（同批 SVG，mtime 未变）得 0 flags，墨顶 2313.1、line@204。两处差异皆有解释：(a) `tools/occlusion_audit.py` 工作树在 2026-11-11 05:01 UTC 被改过（未提交；git diff：新增嵌套 `<svg>`/`<g transform>` 坐标映射，元素计数随之变化——line@197→204）；(b) Pillow 版本差异：venv Pillow 13.0.0 量得该行墨顶 2313.1（与线框底 2313.0 间隙 +0.1px），系统 Pillow 10.2.0 量得 2312.85（重叠 0.15px）。即：是否 flag 只差 0.15–0.3px 的亚像素测量，取决于工具版本与 Pillow 版本。像素裁决：`p1-graze-crop.png`（200dpi 级放大）见绿线与「em Brasília. (Página 4)」之间有清晰间隙，线未触字。**裁决：非缺陷。** 建议工具侧把 Pillow 版本钉死（venv 已是 13.0.0；构建者当次疑似用了系统 python3）。
2. **其余 KIT 数字全部复现一致**：gates 16/16、p8 extract 150/150、p8 compare CLEAN + keydiff [137, 138]、freeze baseline 8/8、freeze diff 新增 CJK 仅 U+3000（9 个）、P8 最小字号 9.75pt、印/网文字层词集差 0、P1 头条 41 字符、范文 88 词。

## 机械门实跑证据（全部自己跑，不信 KIT）

| 门 | 命令（相对 `~/workspace/weekly-git`，venv python） | 结果 | 日志 |
|---|---|---|---|
| gates 自检 | `python -u gates.py`（版目录内） | **16/16 PASS，FAILURES: none** | `gates-rerun.log` |
| occlusion 审计 | `python ../../../tools/occlusion_audit.py svg --json occlusion.json` | **0 flags**；自检通过（6 类阳性全触发） | `occlusion.log`、`occlusion.json` |
| creambox 全版扫描 | `python <goals>/hidden_files/w47/tools/creambox.py svg/*.svg` | 见下：3 处真溢出（D1–D3）+ 2 处框标题右溢（D4–D5，见 boxtitle）+ 6 处 desc-clear 负值全部裁决为非缺陷 | `creambox.log` |
| p8 extract | `python tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150` | **150/150 noted** | `p8-extract.log`、`p8-extract.json` |
| p8 compare | `python tools/p8.py compare --core-p8 ../core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150` | **CLEAN**，missing=[] extra=0，**keydiff=[137, 138]** | `p8-compare.log`、`p8-compare.json` |
| freeze baseline | `python tools/freeze.py baseline --build production/2026-w47/2026-w47-pt-it --core-svg production/2026-w47/2026-w47-pt-it/svg --out freeze-base` | **8/8 SVGs byte-identical**，repointed: none；core SVG 复哈希未变 | `freeze-base.log` |
| freeze diff | `python tools/freeze.py diff --core-svg ../core-pt/svg --edition-svg svg` | RC=0；新增 CJK 字符仅 U+3000，9 个（每页 1–2 个，家具分隔符） | `freeze-diff.log`、`freeze-diff.json` |
| 印/网文字层 | `pdftotext -layout` 两版 + 词集比对 | 各 8,487 词；**only-in-print 0、only-in-web 0**；print 110,299 字节 / web 110,364 字节 | `print.txt`、`web.txt` |
| P8 最小字号 | PyMuPDF（venv）取 P8 全部 span 字号 | **9.75pt（174 spans）**，其余 ≥10.5pt；印/网一致；页框 1462.5×2025pt（0.75 缩放）；= SOP §1.1 下限，不低于下限 | （本文件记录；无单独日志） |
| 弯引号扫描 | 文本节点级统计 U+201C/U+201D/U+2019/U+2018 + ASCII 引号 | U+201C/U+201D：P8 各 2/2 平衡（Q139/140 意语句），P1–P7 0/0；U+2019：仅 P1 徽标 1 处；ASCII 省略号撇号为全 program 惯例（见非缺陷项）；text.md 弯引号 2/2、ASCII 双引号 0 | `quotes.log`、`quotes2.log` |
| boxtitle 实测 | 自写脚本：审计工具 `ink_box` 真墨迹 vs 奶油框右缘 + 右版心 1862 | D4 +29.5px、D5 +2.5px（缺陷）；其余标题均在框内（最紧：P1「EM POUCAS PALAVRAS IN BREVE」−3.2px、P7「ERROS COMUNS」−18.0px）；P8 注行 +0.2px 容差内 | `boxtitle.log`、`boxtitle2.log` |
| keycheck | 150 题逐题手验（见 `keycheck-150.json`） | **150/150 PASS**；三源一致（印刷键/行内答案/Respostas 汇总） | `keycheck-150.json`、`key-agreement*.log` |
| 逐版看图 | 8 张 cards 全页 + 9 张放大裁图 | D1–D5 全部像素确认（见 PROOF-NOTE）；其余各页无溢出/重叠/压页脚 | `view-p*.png`、`p1-d1-crop.png`、`p3-d2-crop.png`、`p6-d3-crop.png`、`p7-d4-crop.png`、`p1-d5-crop.png`、`p1-graze-crop.png`、`p8-e-crop.png`、`p8-h-crop.png` |

### p8 keydiff [137, 138] 逐个裁决
- 137：印刷键「Venerdì 20 novembre è festa nazionale.」——葡萄牙语「Sexta, 20 de novembro, é feriado nacional.」的正确意大利语译文。接受。
- 138：印刷键「Il Palmeiras ha vinto 5–4 ai rigori.」——「O Palmeiras venceu nos pênaltis por 5 a 4.」的正确意大利语译文。接受。
- 其余 148 键与核心逐字一致；Q131 = A（核心 D2 修复已在）；Q150 = ✓（开放写作，范文标记）。

### creambox 逐项裁决（除 D1–D3 外）
- P1 numbers 框 BELOW-WINDOW +37.0「AGORA VOCÊ」：下一节标题，假阳性。
- P2 日程框 BELOW-WINDOW +32.0「Atenção: …」：框下正文段落，假阳性。
- P3 Nota 框 BELOW-WINDOW +37.0「UM DIA, DOIS SENTIDOS」：下一节标题，假阳性。
- P6 图表框 BELOW-WINDOW +42.0「EXERCÍCIOS」：下一节标题，假阳性（两框同值）。
- desc-clear 负值 6 处（P2 −1.0、P3 −0.9、P4 −1.5、P5 −1.1/−0.9、P7 −1.5）：逐行真墨迹核实——「Scrivi due frasi e inviale.」「frasi e inviale.」「due frasi e inviale.」「2027.」「inviale.」「memoria della lotta e della cultura.」**均不含降部字母**，真墨底距框底 +4.2~+4.9px；另 P2 SÁB 21 格「Palmeiras–Flamengo」desc-clear +1.1，真墨底（含 g 降部）距框底 +2.1px。全部非缺陷——负值只是 0.30×字号一刀切余量的假象。
- P7 toolbox：3 框，最小 inside 余量 +4.5px（A PALAVRA 框，见 D4 标题问题不在此项——标题横向溢出，纵向余量正常）、最小 desc-clear −1.5px（同上，无降部字母，真墨余量 +4.2px）；末引基线 2380.67，距预告框顶 2404 约 18px，gates「P7 quotes clear」通过且 P7 全页目视无碰撞。

### boxtitle 其余实测值（真墨迹，框右缘 1862）
- P1「A SEMANA EM NÚMEROS In cifre」−28.2；「EM POUCAS PALAVRAS IN BREVE」−3.2；「A PALAVRA DA SEMANA」无框（−176.8 vs 版心）；「AGORA VOCÊ」无框。
- P7「ERROS COMUNI Errori frequenti」−18.0；「CARTAS DOS LEITORES」−143.5。
- P8：无奶油框；全页唯一超版心文本为注行 +0.2px（O4）。
- P1 徽标「L’EDIZIONE」：SVG 文本 `L’EDIZIONE`（U+2019、无空格），与 KIT 所述一致；渲染间隙为 Newsreader 字形特性，非缺陷。

## 外部事实来源（live 核查，2026-11-11）
- Copa do Brasil 半决赛次回合（与 P4 逐字相符）：Atlético-MG 1–1 Grêmio（11 月 7 日周六，Arena MRV；Renan Lodi、Carlos Vinícius 进球；首回合 Grêmio 2–0，总比分 3–1）；Vasco 2–1 Palmeiras（11 月 8 日周日，São Januário；点球 5–4；首回合 Palmeiras 1–0，总比分 2–2）；决赛 12 月 6 日单场、Mané Garrincha、巴西利亚。来源：sportradar 赛果页；infobotucatu.com（2026-11-09 刊）；estacaolivremt.com.br；futebolinterior.com.br；edmaisesporte.com.br。
- F1 圣保罗站（与 P4 逐字相符）：Norris 冠军、Verstappen 第 2、Hadjar 第 3、Mercedes 锁定 2026 车队冠军（Russell 第 4、Antonelli 第 5）。来源：Sky Sports（2026-11-08/09）；Reuters 转述（portaldasradios.com.br，2026-11-08）；sowetan.co.za。
- 日期星期（`date -d` 核对，America/Toronto）：2026-11-16 周一、11-15 周日、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日。
- P6 工作日算术（手工复核）：11 月 16–30 日 15 天；工作日 10 天（16、17、18、19、23、24、25、26、27、30 日）；周末/假日 5 天（20、21、22、28、29 日）；第 10 个工作日 = 11 月 30 日。

## 判为非缺陷的项
1. P1 LINEX 0.2px 擦痕（KIT 1 flag）：未复现（当前工具 + Pillow 13 得 0 flags，间隙 +0.1px）；像素裁图见清晰间隙。已在 §0 说明版本敏感性。
2. 6 处 desc-clear 负值：见上，真墨迹均无降部字母、余量 ≥+4.2px。
3. 「o título → campione」：五版 pt fan-out 共用 gloss 惯例（en title / fr champion / es campeón / de Meister / it campione），非本版错误。
4. 「cair → 'cadere in un giorno'」：共用 gloss 惯例（en "to fall on a day" / es "caer en un día" / de "an einem Tag fallen"），非本版错误。
5. ASCII 省略号撇号（c'è、l'attesa 等）：全 program 惯例（pt-fr 52 处、pt-en 8 处同）；U+2019 仅用于家具徽标。
6. 「L’EDIZIONE」徽标间距：SVG 文本正确，属字体渲染特性。
7. P3「B AS PALAVRAS DO TEXTO」标题孤悬栏底、P2/P5 词表引言跨栏：核心固有排版行为（KIT §6 已披露），内容齐全，非缺陷。
8. P1「AGORA VOCÊ」等小节标题无奶油框：设计如此，非缺陷。
9. P8 注行 +0.2px：取整容差内（O4）。
10. E 节标签未本地化疑似（任务必查 d）：SVG「E　TRADUZA」与 text.md「### E · Traduza」均为葡萄牙语目标语标签，与核心一致；全版无中文「翻譯」残留，P8 文本节点 CJK 计数 0。无复现。
11. P7 gates「quotes clear of preview box」：KIT 称该检查本身空洞（先滤 y<2404 再断言），本轮人工复核末引基线 2380.67、墨底约 2385.7、距预告框顶 2404 约 18px，且 occlusion 0 flags、P7 全页目视无碰撞。有效。
12. KIT 所述「P1 badge apostrophe」「?Scrivi 合并」「双句号」「" :"」等既往缺陷类：本轮全版扫描 0 复现（`?Scrivi` 0、`?Write` 0、非省略号 `..` 0、`" :"` 0）。
