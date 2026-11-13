# PROOF-NOTE — W47 core-pt 独立复校（fix2 后，re-proof）

- 复校员：独立复校（与构建者 / fix2 不同人）。日期：2026-11-11。
- 对象：`production/2026-w47/core-pt/`，fix2 本地 commit `d2b0e182`（未 push；核查时 HEAD 已移到 `f567bcea`（core-nl fix3），但 `git log -- production/2026-w47/core-pt/` 显示触及 core-pt 的最新提交仍是 `d2b0e182`，且三处跟踪生产文件相对 fix2 提交干净无改动）。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-pt2/`（只写 goals 侧；生产文件只读，未 commit、未 push、不碰其他周）。
- 探针：`ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` 通；goals 侧写 `probe-proof-core-pt2.txt` 成功。TMPDIR 全程在 scratch 下 `tmp/`。

## 结论：(a) 零问题，可定稿

fix2 的 D5 修复独立复测通过，D1/D2/D3/D7 回归全部通过（无回退），全部门禁全过，150 题逐题手验零语义错误，8 页逐页目视干净。**无缺陷，可定稿。**

## §0 三件 SHA（开工前核对，与任务所给一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | 25,312,258 | `4b58f4dfec2245f77dbb57b53c58cbab4913fdc85e4cf8566d706d4d3ec141b6` ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | 1,609,033 | `9f2d70e5404a964d303182faae69b4884e46dbcc168a632323fb2bff61a2a7b5` ✓ |
| `2026-w47-pt-zh-cn.text.md` | 36,882 | `3cd3793f198a40d8c4b895275bbce9c6593168eeb93ae2e7fea7ce0e7f4fbce2` ✓ |

附：印/网各 8 页，1462.5×2025pt；KIT §6 所记三件尺寸/SHA 与磁盘实测逐字一致。fix2 提交内仅 3 文件（`content34.py`、`text.md`、`WEEKLY-KIT.md`）；SVG/PNG/PDF 为未跟踪的构建产物，磁盘即 fix2 重建后状态。

## §1 D5 回归复测 — 通过（fix2 的唯一修复项）

源码核实（正则，不含歧义串）：
- `content34.py:134`：`f.gloss("… o título 冠军头衔 …")`；裸 `o título 冠军`（不带“头衔”）= **0 处**，全形 `o título 冠军头衔` = 1 处。
- `text.md:215`：同一串；裸 = **0 处**，全形 = 1 处；`git show d2b0e182` 证实 text.md 相对 fix1 仅第 215 行一处改动（36,876→36,882 B，+6 B）。
- 其余“冠军”用法未动：Q55 `taça=冠军奖杯`（正确）、P8 简析“第六冠/第五冠”（正确）。

P4 gloss 盒独立重测（自写 `pil_re2.py`；PNG 为本人用 `tools/venv/bin/python` + cairosvg 自 SVG 重渲染，1950×2700，**与 repo `cards/` 逐字节相同**，即与印 PDF 同源；墨 = 灰度均值 <180）：

| 指标 | fix2 称 | 本轮实测 | 判定 |
|---|---|---|---|
| 行数（SVG `x=1007` / 20.5pt 译注行） | 仍 3 行 | **3 行**（基线 308.98 / 338.71 / 368.43） | ✅ 无新断行 |
| 末行 PIL 宽（`svglib.text_w`，sans 20.5） | 383.4px，内宽余 +3.1px | **383.4px，内宽 386.5 余 +3.1px**（另两行 367.7 / 370.7px） | ✅ 逐字复现 |
| 末行渲染墨右缘（盒右 1411.5） | 1387，余 24.5px | **1388，余 +23.5px** | ✅（1px 方法差，见注） |
| 墨底（盒底 416.15） | 372，余 44.2px | **373，余 +43.1px** | ✅（1px 方法差） |
| creambox 纵向余量 | +47.7px 不变 | **+47.7px（desc-clear +41.6）** | ✅ 不变 |

2× 裁切目视（`crop-d5.png`）：3 行完整在盒内，末行 `军头衔 · a pausa 休整期 · a taça 奖杯。` 距盒右缘与盒底均有明显奶油余量；“冠军头衔”在行 2 末 `冠` / 行 3 首 `军头衔` 处按汉字自然断字，无孤字、无溢出。

注：1px 差异（墨右 1388 vs 1387、墨底 373 vs 372）为抗锯齿阈值舍入，与 D1/D7 的同类 1px 差一致；盒内余量均 ≥23px，不影响结论。

## §2 D1/D2/D3/D7 回归复测 — 全部通过，无回退

| 缺陷 | 末行 / 位置 | 本轮实测（墨底 / 框底） | clearance | fix1/proof1 值 | fix2 称 | 判定 |
|---|---|---|---|---|---|---|
| D1 | P1 EM POUCAS PALAVRAS 盒，末行 `em Brasília. (Página 4)` | 墨行 2283–2303 / 2312–2332；框底 2348；2333–2348 无墨（2349–2350 为盒下 quiz 分隔线，不在盒内） | **+16px** | +16 | +17 | ✅ 通过（≥+5；与 fix1/proof1 一致，fix2 的 +17 为 1px 方法差，非回退） |
| D2 | P3 schedule 盒（x 1439.5–1862），末行 `16h30.` | 墨行 500–514 / 526–540；框底 551；552–570 无墨 | **+11px** | +11 | +11 | ✅ 通过 |
| D3 | P6 timeline 盒（x 1439.5–1862），末行 `Página do Participante.` | 墨行 796–811 / 825–845；框底 854；855–875 无墨 | **+9px** | +9 | +9 | ✅ 通过 |
| D7 | P8 范文 10 行（15pt，栏右缘 1862） | 10 行墨右缘 1723–1840；最紧行 `Zumbi e Palmares e escrevo duas frases em português.` 墨右 1840；SVG 计 90 词 = 88 正文词 + `Texto modelo:`（2 词） | 距栏边最紧 **+22px**（余量 +22…+139） | +22 | 22 | ✅ 通过（无行超右缘；行 2 实测 1814 vs proof1 1813，1px 舍入，最紧行一致） |

2× 裁切目视（`crop-d1/d2/d3/d7.png`）：D1 末行在盒内、盒底有干净奶油余量、quiz 线不再穿字；D2 `16h30.` 在盒内、下有白空隙；D3 `Página do Participante.` 降部不触边；D7 十行行末距栏边均有明显余白。与 PIL 数值一致。

补充：全 31 奶油盒 PNG 真墨横扫（自写脚本，逐盒量盒内末墨行 vs 框底）——**31/31 通过，零溢出**，最小余量 +3.5px（P5 E-VOCÊ 盒底 782.5 / P7 工具盒底 1372.5，均为中文末行无降部）；6 处 desc-clear 负值全部复现为已知假阳性类（末行中文/数字，真墨余量 +3.5…+6.0px）。

## §3 全文重读 + 150 键逐题语义核对（手验，非仅 p8 compare）

- text.md 全文（534 行）已通读；150 题逐题对照正文核对题干与键，**零语义错误**。按页小结（全量核对表见 GATE-LOG §8）：
  - P1：1–10 全对（20 日=周五、决赛 12 月 6 日、decidem 现在时 eles 形）。
  - P2：11–28 全对；25–28 配对与正文 gloss 一致。
  - P3：29–46 全对；31 题关键区分 12.519（创日）vs 14.759（定为假日）；44–46 造句均为正文合法句。
  - P4：47–64 全对；52–55 配对正确；56–59 比较级方向正确；60–64 过去时正确。
  - P5：65–82 全对；68/81/82（TRI、官方答案归属 Inep）与正文一致；76–79 将来时正确。
  - P6：83–100 全对；83–86 算术自洽（16–30 日共 15 天 = 10 工作日 + 5 休息日）；94 题“não contam”正确。
  - P7：101–112 全对；108 `saíram`（过去时复数，半决赛已赛完）；109–112 虚拟式将来（sair/for/tiver）正确，112 题排除 sai（陈述式现在时）与 saia（虚拟式现在时）。
  - P8：113–150 全对；120 题第二天 5 小时（13h30–18h30）；125 题“rodada 36”与“35 轮周三/周四结束、21 日周六打 36 轮”自洽；133–136 造句、137–140 翻译句与正文一致；141–144 配对正确；146/147 sexto/quinto 与两队杯赛冠军数一致；148 `na internet` 正确；150 范文 88 词（本人逐词数过，含 `×` 计 88）。
- 印 PDF RESPOSTAS 块与 text.md 逐项比对：**150/150 一致**（自写 `keycheck2.py`，顺序解析 1→150，Q134 内嵌“1 a 1.”幽灵键已排除；Q140 因版式换行亦一致，Q150 `✓ 范文见本版 H 区（88 词）`一致）。
- 读者面内部语扫描：印 PDF 全文无 SOP/proofread/cover/TODO/placeholder/lint 内部标记（7 处命中全为葡语词 `todo(s)`“全部”的子串误报）；`VOL.3` 仅出现 2 次，均在 P7 读者来信说明内（门禁逐字核对过，允许）。

## §4 外部事实抽查（本轮新检索 + 自算）

fix2 未改任何事实内容；本轮对两个最重事实组做新检索复核，其余组与 proof1（2026-11-11，同日）验证一致、内容未变：

1. **Copa 决赛 + 半决赛**（2026-11-11 新检索）：决赛 Palmeiras × Grêmio，12 月 6 日周日、单场、Mané Garrincha（首届单场决赛，CBF 11 月 9 日确认）；Grêmio 第 10 次进决赛、冲第 6 冠，Palmeiras 冲第 5 冠；半决赛 Grêmio 1–1 Atlético-MG（11 月 7 日周六 Arena MRV，首回合 2–0，总比分 3–1）、Vasco 2–1 Palmeiras（11 月 8 日周日 São Januário，首回合 Palmeiras 1–0，总比分 2–2），点球 5–4 帕尔梅拉斯晋级；Renan Lodi / Carlos Vinícius 进球与正文一致。来源：bolavip / sportytrader / portaldopalestra / foot-analytics。
2. **Enem**（2026-11-11 新检索，含 DOU 原文）：Edital nº 64/2026；两天 11 月 8/15 日周日，第二天 13h30–18h30（Natureza + Matemática 各 45 题 = 90 题，5 小时）；官方答案“até o 10º dia útil após o 2º dia”（item 15.1）；自算工作日：11 月 16 日起计，扣 11 月 20 日假日与两个周末，10º dia útil = 11 月 30 日；正文“27–30 日”区间如实覆盖两种计法（27 日为把 20 日计入的算法）；个人成绩 2027 年 1 月、Página do Participante；TRI 按连贯性与难度计分。来源：in.gov.br（DOU Edital 64）、ulti、sisu.pro.br、cursosdoportal。
3. **日历骨架**（本轮自算）：`TZ=America/Sao_Paulo date -d` 核 13 个日期的星期全部与正文一致（11 月 7 日周六、8 日周日、15 日周日、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、27 日周五、30 日周一、12 月 6 日周日）；16–30 日 = 15 天 = 10 工作日 + 5 休息日。

## §5 门禁结果（全过；详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| gates_core.py（check_core） | 16/16 PASS，FAILURES: none |
| occlusion audit | 0 flags（自检 6 类阳性全触发） |
| creambox.py 全版（规范版，md5 `ee7a55d8…`，与 proof1 一致） | 31 盒，0 真溢出（6 处 BELOW-WINDOW 皆已知假阳性类：下块标题/独立段落；6 处 desc-clear 负值皆中文/数字无降部字母，PIL 真墨复测余量 +3.5…+6px） |
| p8 extract | 150/150 |
| p8 compare --total 150 | CLEAN（missing=[]，keydiff=[]） |
| freeze baseline | 8/8 SVGs byte-identical，core 完整性 8 文件重哈希无改动 |
| freeze diff | +0/−0，新增 CJK 0 |
| 印/网文字层 | layout 抽取各 104,920 字节、raw 各 44,487 字节，两版逐字节相同；词数 7,262（layout）/ 7,263（raw），词多重集差 0；弯引号 “ ” 各 3、’ 0、«» 各 40，两版一致 |
| P8 最小字号 | 10.12pt（全版最小亦 10.12pt，仅在 P8）≥ 9.75pt |
| ABSTRACT.txt | 含 masthead “A Lucerna 葡萄牙语周报 VOL.4”（SOP §9）✓ |
| keycheck（印 PDF RESPOSTAS vs text.md，自写顺序解析器） | 150/150 |

## §6 缺陷清单

无。零问题，可定稿。

## §7 备注

- 1px 级数值差（D1 +16 vs fix2 +17；D5 墨右 1388 vs 1387、墨底 373 vs 372；D7 行 2 墨右 1814 vs 1813）均为抗锯齿阈值/舍入所致：本轮 PNG 与 repo `cards/` 逐字节相同、与印 PDF 同源；所有相关余量均 ≥+3.1px（PIL 宽）/ ≥+16px（盒底），不构成回退或缺陷。
- 布局文字层字节数较 proof1 的 104,916 变为 104,920（+4 B）：源于 gloss 多“头衔”二字后的 layout 换行空格变化；印/网两版彼此逐字节相同，门禁成立。
- 生产文件只读：除核对 SHA 与渲染 PNG/PDF 读数外，未改 repo 内任何文件；未 commit、未 push。fix2 本地 commit `d2b0e182` 状态未动。
- 工具：正典 creambox `hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与 proof1 核对一致）；构建一律 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3），未用系统 python3。
- 范围外事项（不在本轮核）：pt-ko O1 字体漂移另案处理；D5 的 9 版 fan-out 一词修正属 fan-out 修复，不在本轮核。
