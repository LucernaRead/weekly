# FIX-LOG — W47 es 家庭修复（F2/F3/F4；F1 裁定不修）

**任务**：修独立重校 PROOF-NOTE.md（2026-11-12，`scratch-reproof-w47-es/PROOF-NOTE.md`）的 F2（11 版）、F3（es-fr/es-it）、F4（es-ru）。只动 `production/2026-w47/` 内 es 家 11 版目录（core-es = es-zh-cn + 10 fan-out）；不碰其他家庭、其他周；不 commit、不 push、不跑 lint。解释器全程 `tools/venv/bin/python`。SOP §8：改源头 → 整版重渲染 → 门禁 → KIT → FIX-LOG。

**磁盘**：开工 93G 已用（150G 盘），门限 100G。

## 改前实测（与 PROOF-NOTE §1 逐一核对，一致）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-es (es-zh-cn) | `La-Lucerna-VOL4.pdf` 4,317,614 / `ed100a0f6a17` | `La-Lucerna-VOL4-web.pdf` 1,162,044 / `5486101f2fdd` | `2026-w47-es-zh-cn.text.md` 43,771 / `449922779d61` |
| es-de | `La-Lucerna-VOL4-es-de.pdf` 2,916,396 / `86db55fa894b` | `La-Lucerna-VOL4-es-de-web.pdf` 806,903 / `052cf044d65a` | `2026-w47-es-de.text.md` 45,311 / `81ff06563dd9` |
| es-en | `La-Lucerna-VOL4-es-en.pdf` 2,915,634 / `3ece32511f03` | `La-Lucerna-VOL4-es-en-web.pdf` 806,132 / `23a06fabd738` | `2026-w47-es-en.text.md` 44,983 / `6080c94c420f` |
| es-fr | `La-Lucerna-VOL4-es-fr.pdf` 2,914,976 / `671c8c129839` | `La-Lucerna-VOL4-es-fr-web.pdf` 805,449 / `a7a0b7025d03` | `2026-w47-es-fr.text.md` 45,794 / `ae1c3f3ba234` |
| es-it | `La-Lucerna-VOL4-es-it.pdf` 2,913,383 / `fab568413ff3` | `La-Lucerna-VOL4-es-it-web.pdf` 803,850 / `437c65b44ca5` | `2026-w47-es-it.text.md` 45,176 / `434e8df8f0d6` |
| es-ja | `La-Lucerna-VOL4-es-ja.pdf` 8,530,855 / `9a5338c3e29e` | `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,435 / `5f496c566aa3` | `2026-w47-es-ja.text.md` 46,554 / `7479077861f4` |
| es-ko | `La-Lucerna-VOL4-es-ko.pdf` 5,229,280 / `f059db4ed89c` | `La-Lucerna-VOL4-es-ko-web.pdf` 1,097,508 / `a555f282aceb` | `2026-w47-es-ko.text.md` 47,385 / `a24b79b06489` |
| es-nl | `La-Lucerna-VOL4-es-nl.pdf` 2,915,319 / `7f7e90229098` | `La-Lucerna-VOL4-es-nl-web.pdf` 805,821 / `7d69a9df2405` | `2026-w47-es-nl.text.md` 45,284 / `d8d8e0078a7a` |
| es-pt | `La-Lucerna-VOL4-es-pt.pdf` 2,914,545 / `8da2a440916e` | `La-Lucerna-VOL4-es-pt-web.pdf` 805,014 / `0a23b7d32fcc` | `2026-w47-es-pt.text.md` 45,535 / `9df4d30caba9` |
| es-ru | `La-Lucerna-VOL4-es-ru.pdf` 3,213,677 / `707b82670349` | `La-Lucerna-VOL4-es-ru-web.pdf` 1,062,147 / `a0889431bde2` | `2026-w47-es-ru.text.md` 52,477 / `05e7d6c91fa3` |
| es-zh-tw | `La-Lucerna-VOL4-es-zh-tw.pdf` 4,381,574 / `9a60b0786b1c` | `La-Lucerna-VOL4-es-zh-tw-web.pdf` 1,265,855 / `4851fee5b3a4` | `2026-w47-es-zh-tw.text.md` 43,800 / `930fc2bab9b7` |

## 源头改动

### F2 — P6 时间轴措辞过强（11 版全有，低）

- 位置：P6 右栏时间轴 `EL CAMINO AL 29N`，`content56.py:137`。
- 改动（11 版同一行，逐字相同）：`"23 NOV. — Atresmedia convoca un debate a cuatro (sin el PSOE)."` → `"23 NOV. — Atresmedia convoca un debate a cuatro (sin el PSOE confirmado)."`，与同页正文 `content56.py:124` 的 "sin el PSOE confirmado" 一致。
- 说明：任务书称“改一处源头”——实测西语核心文本在 11 个版目录各存一份完整副本（无共享 import；`grep -c "sin el PSOE)"` 每版均为 1），故同一核心行在 11 个 `content56.py` 各改 1 处、共 11 处，内容逐字相同。fan-out 各版此前即按此方式承接核心改动（见 `scratch-fix-es-fr1/FIX-LOG.md`：fan-out 工人在本版目录内改 `content*.py`）。
- 预检：`wrap()` 实测新行在 19pt、宽 378.5px 下仍为 2 行（与旧行同），时间轴盒高不变（`tl_h` 公式按行数计）。

### F3 — P1 刊头顶行相撞（es-fr、es-it，中）

- 位置：`content12.py:16` 顶行副标（居中，x=975）与右端日期 `SEMANA DEL 16 AL 22 DE NOVIEMBRE DE 2026`（右锚）相撞。
- 改动：
  - fr：`CADA SEMANA EN ESPAÑOL　CHAQUE SEMAINE　L'ESPAGNOL DES ESPAGNOLS` → `CADA SEMANA EN ESPAÑOL　CHAQUE SEMAINE EN ESPAGNOL`。
  - it：`CADA SEMANA EN ESPAÑOL　OGNI SETTIMANA　LO SPAGNOLO DEGLI SPAGNOLI` → `CADA SEMANA EN ESPAÑOL　OGNI SETTIMANA IN SPAGNOLO`。
- 实测（重渲染后 PyMuPDF，新印 PDF P1）：日期左端固定 x=1039.4pt；fr 副标右端 x1=974.1pt → **间隙 65.3pt**（要求 ≥10pt），旧合并词 `ESPAGNOLSSEMANA` 已消失；it 副标右端 x1=970.7pt → **间隙 68.7pt**，旧合并词 `SPAGNOLISEMANA` 已消失。P1 目视确认：两版 `cards/p1-portada.png` 顶行副标与日期间隙清晰、无粘连。

### F4 — P2 "DECIR LA HORA" 尾行错位（es-ru，中）

- 实测成因（改前 PyMuPDF）：ru 版 DECIR 标题 y0=984.8pt（en/de 为 926.8pt），即俄语日历框把该段压低 58pt；段落末行 `nunca «en las 21:00».` 溢出 Flow 底限（1540px），被排到下一栏顶 (741.8, 154.6)。`wrap()` 实测俄语日历框 30 行 vs 核心 23 行（每行 21pt×1.36=28.56px）。
- 改动（只动 `2026-w47-es-ru/content12.py` 日历框内俄语注释，不动任何西语正文；每处删的都是西语行已有的信息——日期/人名/党名/投票方式）：
  - Lunes：`(понедельник: Международный день фламенко; Народная партия предлагает дебаты Санчес — Фейхоо)` → `(понедельник: день фламенко; дебаты Санчес — Фейхоо)`（6→5 行）
  - Martes：`(вторник: кампания едет по Испании)` → `(вторник: кампания по Испании)`（4→3 行）
  - Miércoles：`(среда: дебаты о жилье на радио, PSOE против PP)` → `(среда: дебаты о жилье на радио)`（5→4 行）
  - Jueves：`(четверг: последний день заявки на голосование по почте)` → `(четверг: последний день заявки на голосование)`（4→3 行）
  - Domingo：`(воскресенье: «Барса» — «Вильярреал»; день святой Цецилии)` → `(воскресенье: «Барса» — «Вильярреал»; св. Цецилия)`（5→4 行）
  - 合计 30→25 行，日历框缩短 5×28.56≈143px；DECIR 标题预计上移约 143px 至 ~1170px，段落末行预计回到同栏 ~1340px 内（底限 1540px）。
- 实测（重渲染后 PyMuPDF，新印 PDF P2）：DECIR 标题 y0=877.7pt（改前 984.8pt，**上移 107.1pt ≈ 143px，与预测一致**）；末行 `nunca «en las 21:00».` 位于 (403.9, 1052.9)，与标题同栏（x=403.9），在段落正下方、栏内（en/de 对照为 (403.9, 1095.8)）。P2 目视确认：`cards/p2-vida.png`，DECIR LA HORA 整段同栏完整，尾行已回位；日历框俄语注释已缩短，页面无其他移位。

### F1 — 缺首字下沉（11 版全有，协调员裁定：不修，记为已知引擎偏差）

- 协调员裁定复述：属实，但为全刊引擎级缺口——SOP §1.1 第 97 行确有要求（头条第一段首字下沉，橄榄绿，约 4 行高），构建代码中无任何首字下沉实现；已发行 W46 印 PDF 的 P1 除刊名 147pt 外无 >60pt 元素（即 W46 亦无首字下沉，非 W47 回退）。实现首字下沉须改共享构建引擎 + 全 130 版重渲染，不在本轮按家修复范围内；记为已知引擎偏差，进模板 backlog（与 zh-cn F2 同类已裁定项、pt P2 栏目标题孤儿同列）。本轮未动任何模板/引擎代码，只修 F2/F3/F4。

## 重建

`build_all.sh` 逐版 `run.py` → `render.py`（内含 webpdf.py）→ `extract_text2_d5.py` 干跑导出到 `scratch-fix-es/text-<ED>.md`（不落盘）。每版 run rc=0、TOTAL 150、0 FLOW OVERFLOW / HEAD TOO WIDE；render rc=0。

| 版 | run | render（印 / 网，字节） | text 干跑行数 |
|---|---|---|---|
| core-es | rc=0, TOTAL 150 | 4,317,615 / 1,162,042 | 1803 |
| es-de | rc=0, TOTAL 150 | 2,916,396 / 806,895 | 1837 |
| es-en | rc=0, TOTAL 150 | 2,915,635 / 806,124 | 1848 |
| es-fr | rc=0, TOTAL 150 | 2,914,957 / 805,426 | 1850 |
| es-it | rc=0, TOTAL 150 | 2,913,352 / 803,822 | 1833 |
| es-ja | rc=0, TOTAL 150 | 8,530,855 / 1,280,428 | 2058 |
| es-ko | rc=0, TOTAL 150 | 5,229,281 / 1,097,497 | 2651 |
| es-nl | rc=0, TOTAL 150 | 2,915,320 / 805,809 | 1876 |
| es-pt | rc=0, TOTAL 150 | 2,914,546 / 805,017 | 1855 |
| es-ru | rc=0, TOTAL 150 | 3,213,296 / 1,061,817 | 1866 |
| es-zh-tw | rc=0, TOTAL 150 | 4,381,575 / 1,265,861 | 1797 |

**中断与恢复（2026-11-12 15:30 UTC）**：运行时重启杀掉了 `build_all.sh`，当时 es-pt 正渲染中——核查：es-pt 的 8 个 SVG 已全新（15:24–15:25）、印 PDF 已完整写入（8 页、P6 含 `confirmado`、P1 文本正常），仅网 PDF 未生成（仍为 08:08 旧版）；es-ru、es-zh-tw 未动。`build_resume.sh`（同流程）只重跑 pt/ru/zh-tw 三版，全部 OK（日志 `build-resume.log`，RESUME DONE 15:39:08）。磁盘 94G（门限 100G，未触发停手）。

**门禁重跑插曲**：`gates_all.sh` 首次执行时出现两个实例并行（运行时疑似重放了一次调用），日志交错不可信；已双双 kill、删净门禁输出、单实例干净重跑一次（`gates-all.log`，GATES_EXIT=0）。重跑前 partial 结果与最终结果一致（core-es、es-de 各门全绿），未采信交错日志。

## text.md 导出器陷阱核查（协调员补充令，ru 家 FIX-LOG §7）

- ru 家陷阱：其导出器 `ru_textmd.py` 的 `do_p_text` 只收 sans 粗体 ≥24pt 标题，D5 后缩到 22/23pt 的框题在重导出时被丢掉；ru 家做法：干跑到 /tmp、与修前文件 diff、在原位置逐字回补被丢标题行，最终 diff 只含意改行。
- es 家核查（本任务实测）：
  - es 家导出器（`extract_text2.py` / `extract_text2_d5.py` / `extract_text_es_*.py`）代码中无 ≥24pt 标题规则（grep `24|do_p_text` 无匹配）；D5 缩字号的 5 处标题（P1 栏头 25→23pt、P3 栏头 25→24pt、P3 手工题 24→23pt）在 es-de 干跑导出中**全部在场**（D5 工具与旧工具各 1 次），未被丢掉。
  - 干跑复现性：旧工具（`extract_text_es_de.py`）在 D5 前基线 SVG（`scratch-d5-rebuild-es/2026-w47-es-de/baseline-svg/`）上与已装 `2026-w47-es-de.text.md` **逐字节相同（diff 0 行）**，证明已装 fan-out text.md 是旧工具 + D5 前 SVG 的产物；同一工具在新 SVG 上为 1844 行（已装 1802 行），D5 工具为 1837 行——差异全是 D5 分段重排（行断点/并行移动，字符内容除意改外一致），不是丢标题。
  - 结论：es 家无 ru 式丢标题陷阱；但 fan-out 版**不得直接落盘重导出**（会引入数百行重排，违反“最终 diff 只含意改行”），改用手术式逐行替换（见下）；core-es 用 D5 工具重导出，diff 恰为 F2 一行，可直接落盘。
- 落盘执行（2026-11-12）：
  - `text_install.py`：core-es 落盘 D5 导出（43,782 B，SHA-12 `e537146d733d`）；其余 10 版手术替换，F2/F3 逐版断言恰 1 处。**小插曲**：脚本用 `ed.split('-')[-1]` 拼文件名，zh-tw 被拼成 `2026-w47-es-tw.text.md`，在已完成 de..ru 后报 FileNotFoundError 中断；zh-tw 的 F2 改用一次直接替换补做（断言恰 1 处），脚本本身已就地修正为 `f"{ed}.text.md"`。`text_install_ru.py`（F4 词级手术，行号锚定、断言原文）随后执行成功。
  - 落盘后逐版 diff 核查（vs `text-pre/`）：8 版仅 F2 一行；fr/it 为 F2 + 副标一行；ru 为 F2 一行 + F4 词级改动（删 5 行：224/229/230/282/324；改 5 行：245/263/271/283/323）；core-es 仅 F2 一行。**无一版含非意改行。**
  - 陷阱复核：D5 缩字号的 3 处标题（`UNA SEMANA, TRES ESCENARIOS`、`LO QUE QUEDA DE NOVIEMBRE`、`EL FLAMENCO, EN TRES DATOS`）在 11 版新 text.md 中各出现恰 1 次，无丢标题。ru 词多重集核对：删词恰为 `Международный/Народная/партия/предлагает/едет/радио，/против/PP）/по/почте）/день/святой/Цецилии`（F2 的 `PSOE).`→`PSOE`+`confirmado).` 另计），增词恰为 `）×2/радио/св./Цецилия/confirmado).`，与意改完全一致。

## 改后 SHA（2026-11-12，盘上实测；完整 SHA-256 见 `scratch-fix-es/post-sha.txt`）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-es (es-zh-cn) | `La-Lucerna-VOL4.pdf` 4,317,615 / `6089c0fa5420` | `La-Lucerna-VOL4-web.pdf` 1,162,042 / `f0f6ed1de57a` | `2026-w47-es-zh-cn.text.md` 43,782 / `e537146d733d` |
| es-de | `La-Lucerna-VOL4-es-de.pdf` 2,916,396 / `3fdc2ce60e6a` | `La-Lucerna-VOL4-es-de-web.pdf` 806,895 / `fd7edd4b8415` | `2026-w47-es-de.text.md` 45,322 / `c08388962767` |
| es-en | `La-Lucerna-VOL4-es-en.pdf` 2,915,635 / `a7d5aba8bd0f` | `La-Lucerna-VOL4-es-en-web.pdf` 806,124 / `bb690dd25b6c` | `2026-w47-es-en.text.md` 44,994 / `cfdd39a9779d` |
| es-fr | `La-Lucerna-VOL4-es-fr.pdf` 2,914,957 / `fd0e9f83a989` | `La-Lucerna-VOL4-es-fr-web.pdf` 805,426 / `960de8cf8d3b` | `2026-w47-es-fr.text.md` 45,790 / `a9aed8190e83` |
| es-it | `La-Lucerna-VOL4-es-it.pdf` 2,913,352 / `0cffc84e47c0` | `La-Lucerna-VOL4-es-it-web.pdf` 803,822 / `f533bb1aa133` | `2026-w47-es-it.text.md` 45,170 / `ee56751564b3` |
| es-ja | `La-Lucerna-VOL4-es-ja.pdf` 8,530,855 / `6d89a8ddf67b` | `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,428 / `c2e0230bac8c` | `2026-w47-es-ja.text.md` 46,565 / `998a9ac32500` |
| es-ko | `La-Lucerna-VOL4-es-ko.pdf` 5,229,281 / `e2ae545b1462` | `La-Lucerna-VOL4-es-ko-web.pdf` 1,097,497 / `fad91509e34f` | `2026-w47-es-ko.text.md` 47,396 / `981d43e91837` |
| es-nl | `La-Lucerna-VOL4-es-nl.pdf` 2,915,320 / `c716ce60992a` | `La-Lucerna-VOL4-es-nl-web.pdf` 805,809 / `8be3118b5080` | `2026-w47-es-nl.text.md` 45,295 / `225181a991b5` |
| es-pt | `La-Lucerna-VOL4-es-pt.pdf` 2,914,546 / `434d8d8fe9c6` | `La-Lucerna-VOL4-es-pt-web.pdf` 805,017 / `50f4402a6a19` | `2026-w47-es-pt.text.md` 45,546 / `f9531af2c638` |
| es-ru | `La-Lucerna-VOL4-es-ru.pdf` 3,213,296 / `0ca1beca6d74` | `La-Lucerna-VOL4-es-ru-web.pdf` 1,061,817 / `2febbe24084b` | `2026-w47-es-ru.text.md` 52,347 / `dadb3e8478e5` |
| es-zh-tw | `La-Lucerna-VOL4-es-zh-tw.pdf` 4,381,575 / `fd3e65ef1840` | `La-Lucerna-VOL4-es-zh-tw-web.pdf` 1,265,861 / `8871073245fd` | `2026-w47-es-zh-tw.text.md` 43,811 / `4795332ea53a` |

改前→改后印 PDF 字节变化：core-es +1、en +1、ko +1、nl +1、pt +1、zh-tw +1、de 0、ja 0、fr −19（副标缩短）、it −31（副标缩短）、ru −381（日历框缩短 5 行）；网 PDF 全部变（重建时间戳）；text.md：F2 单版 +11 字节，fr −4（+11−15）、it −6（+11−17）、ru −130（词删），其余 +11。

## 门禁（`gates_all.sh` 单实例干净重跑，GATES_EXIT=0，2026-11-12 16:16 UTC；日志 `gates-all.log`）

全 11 版：occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异，10/10）；boxtitle 0 DEFECT；spill 0 SPILL；edge 0 TOUCH / 0 NEAR；D5 census PASS（弯引号全在 Newsreader）；freeze baseline 8/8 SVGs byte-identical；印/网 pdftotext 逐字节一致（见下表）；网 PDF 全部 < 7 MB。

| 版 | boxtitle（标题/正文行） | spill（27 盒，candidates） | 印/网文字层（字节） | D5 census（弯引号，Newsreader 内） |
|---|---|---|---|---|
| core-es | 30 / 330，0 DEFECT，0 marginal | 0 SPILL，85 | 44,562 一致 | 10 / 10 |
| es-de | 24 / 264，0 DEFECT，**1 marginal**（已知 +0.7px，容差内） | 0 SPILL，67 | 46,258 一致 | 3 / 3 |
| es-en | 26 / 261，0 DEFECT | 0 SPILL，70 | 45,867 一致 | 6 / 6 |
| es-fr | 24 / 269，0 DEFECT | 0 SPILL，71 | 46,661 一致 | 0 / 0 |
| es-it | 22 / 266，0 DEFECT | 0 SPILL，71 | 46,034 一致 | 0 / 0 |
| es-ja | 26 / 346，0 DEFECT | 0 SPILL，84 | 47,479 一致 | 0 / 0 |
| es-ko | 38 / 604，0 DEFECT | 0 SPILL，149 | 48,250 一致 | 4 / 4 |
| es-nl | 26 / 264，0 DEFECT | 0 SPILL，71 | 46,142 一致 | 4 / 4 |
| es-pt | 24 / 266，0 DEFECT | 0 SPILL，69 | 46,461 一致 | 0 / 0 |
| es-ru | 30 / 372，0 DEFECT | 0 SPILL，72 | 53,420 一致 | 0 / 0 |
| es-zh-tw | 26 / 328，0 DEFECT | 0 SPILL，82 | 44,605 一致 | 0 / 0 |

附加核查：F2 印 PDF 全文检索——11 版 `sin el PSOE confirmado` 各出现 1 次、旧串 `sin el PSOE).` 出现 0 次（PASS）；F3 实测见上（fr 65.3pt / it 68.7pt）；F4 实测见上（标题 877.7pt，nunca (403.9, 1052.9)）。

## KIT 更新

11 版 `WEEKLY-KIT.md` 各末尾追加一节「es 家庭修复 F2/F3/F4（2026-11-12，独立重校 PROOF-NOTE (b) 返修）」，含：改动摘要（F2/F3/F4 + F1 裁定复述）、重建方式、新印/网/text.md 尺寸与完整 SHA-256、门禁全绿摘要、日志路径。es-ru 的 KIT 节注明：本版事后由跨家 *-ru 工人重渲染一次字体路由。D5 行保留未动。

## 不动项

- O1（ja 源码 "正誤正誤" 未上版面）与 PROOF-NOTE §5 其他已排除项不是缺陷，未动。
- 未动 `tools/`、未动模板/引擎代码、未动其他家庭与周次；未 commit、未 push、未跑 lint。
