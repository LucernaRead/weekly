# GATE-LOG — W47 core-es build 10 独立复校机械门实跑证据

- 复校：core-es3，2026-11-11。工作目录 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-es3/`（`gates/` 子目录存原始日志/JSON；`tmp/` 为 TMPDIR）。
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox `hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，开工核对一致）。
- 全部命令均为本轮独立实跑；与 fix 日志相同处均经 `diff` 核对，不只看结论。
- 源文件未改动、未重建、未 commit、未 push（keycheck 进程内重建为确定性构建，事后 SVG 哈希复核未变）。

## §0 身份与探针

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`（通过）；goals 侧 `scratch-proof-core-es3/probe.txt` 写入成功（通过）。
- SHA（`sha256sum` 实测）：印 PDF `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`（17,212,955 B）；网 PDF `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`（1,410,471 B）；text.md `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`（1,822 行，43,788 B）。三者均与任务给定一致。
- `git status --porcelain -- production/2026-w47/core-es/`：仅 `?? production/2026-w47/core-es/`。
- SVG 哈希（keycheck 后复核）：p1 `947d1843` · p2 `4274b9ec` · p3 `f6fabc93` · p4 `897d34cb` · p5 `2fe8d4b0` · p6 `4095ea92` · p7 `a376ef8c` · p8 `19123831`。

## §1 机械门总表

| 门 | 命令 / 方法 | 结果 |
|---|---|---|
| 构建复核 | keycheck 进程内跑 run.py（`sys.argv=['run.py']`） | rc=0；TOTAL 150（A2 50 / B1 72 / B2 28；按版 10/18/18/18/18/18/12/38）；MODELO 97 词；P1-headline 1371/1828；P2-feature 1537/1540（既有紧度）；P6-main col 1/2 y=920；P6 col3 1347.5（timeline 891.0）；P6-ex 2533/2580；P7 col3 1844.51；P8-keys 2382/2560；0 警告（日志 `gates/keycheck.log`） |
| 几何遮挡审计 | `tools/occlusion_audit.py production/2026-w47/core-es/svg --json gates/occlusion.json` | **0 flags**，rc=0；selftest 六类全过（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1 阳性，clean 对照静默） |
| creambox 全版扫描 | 正典 `creambox.py svg/*.svg` → `gates/creambox.log` | 全部盒 inside-only clearance ≥ +4.5（基线）；C1 盒 +8.0；最紧 P3 ¿Y TÚ? +4.5、P2/P5 盒 +5.0–+5.4；+45px 窗口内负值均为下一标题假阳性（below-window owner-rect 另属他盒，diag 已裁定） |
| creambox 真墨裁定 | fix 同款 `creambox_diag.py` → `gates/creambox_diag.log` | **与 fix `creambox_diag10.log` 逐字节一致（diff IDENTICAL）**；C1 真墨 +5.8（墨底 1302.2）；最紧真墨 P2 `ley.` +0.1、P5 `compara precios…` +0.1、P3 `魂”…` +2.5，全部在盒内 |
| P7 toolbox | creambox P7 小结（同上） | 3 盒，min inside clearance **+8.8**，min desc-clear +2.8；真墨最小 +6.8（CARTAS 盒） |
| p8 提取 | `tools/p8.py extract --p8 svg/p8-ejercicios.svg --total 150` | **150/150**（parse: lines），rc=0 |
| p8 比对 | `tools/p8.py compare --core-p8 … --edition-p8 … --total 150` | build9→build10 **CLEAN，keydiff=[]**；build6（prefix-svg）→build10 **CLEAN，keydiff=[139]**（仅 #139，C2 改动；Q89 不在 keydiff 内，证实 D2 回退恢复原键） |
| freeze baseline | `tools/freeze.py baseline --build production/2026-w47/core-es --core-svg …/svg --out gates/freeze10` | **8/8 SVGs byte-identical**，rc=0；core integrity： shipped SVG 未变 |
| freeze_direct | `tools/freeze.py --help` | **无此子命令**，仅 baseline/diff——方法备注，不当缺陷（任务已预见） |
| keycheck | `gates/keycheck_core.py`（fix 同款，改写输出到本 scratch）+ p8-extract.json | **149/150**，rc=0；唯一不符 #150（REG 键「（开放题，范文如下）」vs 印刷「✓」）；输出 `keycheck-150.json` 与 fix 的逐字节一致（diff 前）——后补 `hand_check`/`hand_basis` 逐题手验字段，仍为同一 150 行 |
| boxtitle | fix 同款 `boxtitle_core.py svg/` → `gates/boxtitle.log` | 35 行、**0 溢出**；与 fix `boxtitle10.log` 逐字节一致（diff IDENTICAL）；最紧 `LA SEMANA EN CIFRAS` +16.0；P6 `LEER UN DEBATE` y=1117（时间线盒 891.0 所致），clear +202.4 |
| 印/网文字层 | `pdftotext -layout` 两 PDF → `gates/print.txt` / `gates/web.txt` | 各 **106,440 字节**，`cmp` 逐字节相同（8 个换页符 = 8 页） |
| P8 最小字号 | pypdf visitor，有效字号 `font_size*|tm[3]|`（`gates/p8font.py`） | 最小 **10.125pt**，723 条 runs，**0 条 < 9.75pt** 底线 |
| §1.1 字体/颜色 | SVG 内 grep | Newsreader、Noto Sans CJK SC、Noto Serif CJK SC、UnifrakturMaguntia；#302c28、#46581f/#37402f、#f0eee5、#F1E8D4、#f6e08e、#d8d2c4、#6f675d |
| 弯引号全版扫描 | 文本节点提取（strip 标签/属性）+ text.md | text.md “/” 各 5 对，’ 0，直引号/直撇号 0；SVG 文本节点内直引号/直撇号 0，弯引号成对（P1/P3/P5 各 1 对，P8 2 对） |
| 日期星期 | `date -d`，Europe/Madrid | 9 日周一、10 日周二、13 日周五、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、26 日周四、27 日周五、28 日周六、29 日周日 |

## §2 逐项 grep 证据

- `antes del jueves`：源码 5 文件 + text.md + ABSTRACT.txt 均为 **0**；`hasta el jueves` text.md = **7**；`antes de ese día` = 0，`hasta ese día` 在位（content12.py:175、text.md L274）。
- `19 日前`：全版 0；中文键注 5 处均为「邮寄投票最迟须在 19 日申请」（keys 3/9/22/65/123）；ABSTRACT「邮寄投票最迟 19 日申请」。
- D1：`En la página 6 te enseñamos cómo leer un debate sin perderse.`（content12.py:130、text.md L169/L174）。
- D4：`el sábado veo el derbi`（content7.py:99、text.md L1338）。
- D1/D2：P6 时间线「23 NOV. — Atresmedia convoca un debate a cuatro (sin el PSOE).」+「23 NOV. — RTVE propone un debate a ocho…」+「26 NOV. — El PP propone un debate a cuatro de la Academia (sin fecha pactada).」；P1「Fue el único debate cerrado」；P6「solo hay un debate cerrado」「acordado no es cerrado」；Q89 键 B（p8-extract.json）。
- C2：脚注「Acuerdo de la Junta Electoral Central del 4 de noviembre: 195 minutos en total, del 13 al 27 de noviembre. Tres formaciones más tienen 10 minutos cada una: Frente Obrero, PCTE y SALF.」；45+45+30+30+15+3×10=195；Q83=A、Q84=B、Q85=C。
- C3：content56.py:79 仍为 `sobre · papeleta · censo · identidad · plazo · urna`。
- `Colau`：text.md grep **0 命中**（O1 依据）。
- 金句：`content7.py` quotes 8 句，去空白精确匹配在全版 SVG 文本中每句恰 **2 次**。
- 范文：AST 解析 `content8.py` MODELO，`len(MODELO.split())` = **97**。
- 译注词元（当版 SVG 文本计数，全部 ≥2）：P1 campaña 13 / debate 12 / cara a cara 3 / correo 8 / reflexión 2；P2 debate 5 / mitin 2 / cartel 2 / escaño 2；P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 5；P4 jornada 19 / derbi 7 / liderato 3 / parón 2 / liga 9；P5 sobre 5 / papeleta 2 / censo 3 / plazo 3 / urna 5。
- 内部标签扫查：text.md 中 SOP/proofread/cover/语言代码/周次 0 命中；「VOL.4/VOL.5」仅刊别与下期预告。

## §3 外部事实来源（本轮独立检索 2026-11-11）

1. **邮寄投票截止**：Correos 官方通告 2026-11-10，https://www.correos.com/sala-prensa/asi-es-el-voto-por-correo-en-las-elecciones-generales-del-29-de-noviembre/ ——「todavía pueden solicitar hasta el día 19 de noviembre (inclusive)」；lavozdeibiza 引 LOREG（申请期 10 月 6 日–11 月 19 日）；politican.es（2026-11-11）同证 15 天竞选期（13 日 00:00–27 日 24:00）与材料寄出自 11 月 9 日。
2. **德比**：DAZN/EFE 2026-10-21，https://www.dazn.com/es-ES/news/fútbol/sevilla-betis-sábado-21-de-noviembre-a-las-1830-y-barça-villarreal-domingo-a-las-1400/zsdb1ccuex51teq2zh5q1mec ——「Sevilla-Betis, sábado 21 de noviembre a las 18.30」；eldiariodetoledo、lagrada.org、Sportradar 同证；Athletic–Espanyol 周五 20 日 21:00（同批来源）。
3. **Atresmedia 改期**：zocalopublico 2026-11-09T17:25，https://zocalopublico.com/el-rechazo-del-pp-a-rtve-complica-el-acuerdo-sobre-los-debates-electorales/ ——「Atresmedia… anunció este lunes que lo anticipa al día 23」「Los líderes del PP, Vox y FA han confirmado… pero no así el PSOE」；radarprensa 2026-11-09T15:22（经 20minutos）；elfolio.es 2026-11-09（PP 提议 Academia 16 日 + 26 日，未定）；diariosabemos.com（Abascal 确认 23 日）。
4. **仅一场已锁定**：doblelectura.es 指南（2026-11-10 数据），https://doblelectura.es/guia/debates-electorales-elecciones-generales-2026 ——「A 10 de noviembre de 2026 solo hay un debate cerrado: el de portavoces de laSexta, el viernes 13 a las 21:30」「Solo el de laSexta tiene hora」「Atresmedia convocó su propio debate a cuatro para el lunes 23, sin el PSOE confirmado」；zocalopublico 同证 Mediaset cara a cara 16 日两党已 pactado。
5. **RTVE 分钟**：BOE-A-2026-23258，https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-23258 ——JEC 11 月 4 日决议，按 Radio/TV 委员会提案（LOREG art. 65）同意分配；分摊表公布于 JEC 网站；申诉截止 11 月 6 日周五 14:00；答辩截止 11 月 10 日周二 10:00，RTVE 同日答复。
6. **PCTE 旁证**：BOE-A-2026-23103，https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-23103 ——公布名单含 PCTE 本名及 PCTE/ELAK 等地区联合会 denominations（检索片段实证：Alicante PCTE、PCTE/ELAK）；articulo14/Civio 2026-11-08，https://www.articulo14.es/politica/que-partidos-se-presentan-a-las-elecciones-del-29-n-candidaturas-y-coaliciones-20261108.html ——「PCTE presenta candidaturas bajo diferentes denominaciones territoriales」、SALF 国会 46 选区、Frente Obrero 全 52 选区、534 国会 + 361 参议院 proclamadas。
7. **欧冠 J4 与西甲积分**：Sportradar——巴萨 3–0 阿斯顿维拉、皇马 3–2 AEK、马竞 0–2 拜仁；showupandplay 2026-11-08——「Atlético 1-2 Barcelona」「Top: Barcelona 33, Real Madrid 30, Atlético 28」。
8. **O1 相关（FA/Colau）**：nuevaradio.org 2026-11-09T20:50，https://www.nuevaradio.org/2026/11/09/el-pp-acuerda-que-la-academia-de-television-coordine-los-debates-electorales-tras-el-rechazo-del-psoe-a-las-cadenas-privadas/ ——「Frente Amplio confirmó… su candidata Ada Colau participe en ambos debates a cuatro, uno organizado por RTVE y el otro por Atresmedia」；democrata.es 2026-11-09T21:08 与 diariodia.es 2026-11-09T23:35——FA 重申参加全部已提议辩论。doblelectura 指南「Frente Amplio se echó atrás, según la cadena」一句未找到佐证（见 PROOF-NOTE O1）。

## §4 判为非缺陷的项（证据）

- #150 例外：REG 键描述性文字 vs 印刷 ✓；范文 97 词 AST 实测；开放题无唯一答案，✓ 为既定约定。
- O7（P2 日历/P6 时间线列 SER 18 日）：所述事件为真（两党 10 月 21–22 日已确认）；P6 正文「acordado no es cerrado」已澄清；Q89 键 B 不受影响。
- 紧度：C1 +5.8（达标）；P2 `ley.` +0.1 / P5 `compara…` +0.1 墨在盒内（build 6 既有）；P2-feature 1537/1540（build 6 既有）。
- 195 为图示 8 党之和：图表标题「minutos de propaganda por partido」，脚注未声称全国总和。
- freeze_direct 缺失：工具仅 baseline/diff，方法备注。

## §5 方法备注

- freeze 首次调用因 cwd 在 home、相对路径 `tools/freeze.py` 解析失败（`can't open file '/home/hatch/tools/freeze.py'`）；纠正为 `cd ~/workspace/weekly-git` 后重跑，8/8。失败为调用错误，非工具问题。
- creambox：本轮用正典工具跑出逐行明细表；fix 的 `creambox10.log` 无逐行表（调用版本差异）——inside-only 清除量逐项一致，diag 日志逐字节一致，结论相同。
- creambox +45px 窗口内的负 clearance 行均为下一标题/框标题假阳性（below-window owner-rect 另属他盒），creambox_diag 已逐一裁定（`owner-rect=NONE (head/caption/outside)` 或 `['y=1312']`）。
- PCTE：未重做 BOE-A-2026-23103 全量 18,684 行逐省点数；以 BOE 决议 + LOREG 档位 + BOE 23103 结构旁证 + Civio 计数为准（任务允许的口径），并注明。
- 150 键手验：机械 REG vs 印刷（149/150）之外，逐题对照题干/正文/已核实事实人工核对，依据写入 `keycheck-150.json` 每行的 `hand_basis`。

## §6 输出文件

- `PROOF-NOTE.md`（结论 (a)，缺陷 0，O1–O4）
- `GATE-LOG.md`（本文件）
- `keycheck-150.json`（150 行：REG 键 vs 印刷键 + `hand_check`/`hand_basis` 逐题手验；150/150 pass，#150 为预期例外）
- `gates/`：`run.log`（occlusion/p8）、`occlusion.json`、`p8-extract.json`、`p8-compare-self/b9-b10/b6-b10.json`、`freeze.log`、`freeze10/`、`creambox.log`、`creambox_diag.log`、`boxtitle.log`、`boxtitle_core.py`、`keycheck.log`、`keycheck_core.py`、`keycheck-150.json`（原始）、`p8font.py`、`print.txt`、`web.txt`
- `png/`：印 PDF P1/P6/P7/P8 100dpi 渲染（目视复核用）
