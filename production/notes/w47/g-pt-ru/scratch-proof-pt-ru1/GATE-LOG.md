# GATE-LOG — 2026-W47 pt-ru proof1 机械门实跑证据

复校：proof1 独立复校，2026-11-11。全部命令以 `~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3）实跑，
`TMPDIR=<scratch>/tmp`，日志与 JSON 均存于本 scratch 目录。源文件未改动、未 commit、未 push。
正典 creambox：`hidden_files/w47/tools/creambox.py`，md5 `ee7a55d8b2057cf4ad42a97bb1197383`（已验）。

## §0 身份与探针

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0；
  goals 侧 `hidden_files/w47/scratch-proof-pt-ru1/probe.txt` 写入成功。
- SHA（`sha256sum` 实测，与任务一致）：
  - 印 `A-Lucerna-VOL4.pdf` `d2822ae0ea1c50d12610a8f529efeec6361f608ee344ee6af36868f8bf98db0f`，12,916,544 字节
  - 网 `A-Lucerna-VOL4-web.pdf` `a6a5f25f93265a8914462a17975934d91bef85201bd768ee5221387a716db5ef`，1,151,627 字节
  - `2026-w47-pt-ru.text.md` `3d7597d949cf279fcca5c97b243b470735ce56e3ae31993372cb3e0fadf8904f`，39,719 字节

## 1. gates.py（builder 自查，复跑）— 16/16 PASS，rc=0

`gates.log` 全文 16 行 PASS，FAILURES: none。要点：
`P1 VOL.4 + week dates` / `P1 subtitle topics` / `footer+page line 8/8` / `no VOL.3 residue` /
`press-time note + final named` / `P1 masthead lines fit 1820`（{330: 262.9, 372: 821.0}）/
`same-baseline ink collisions = 0` / `page-frame ink crossings = 0`（min margins L/R/T/B = [47.0, 23.5, 35.0, 32.0]）/
`P6 chart-label coverage <30%`（GRAZE 0%）/ `gloss items enumerated`（29）/ `gloss headwords survive`（0 missing）/
`P7 quotes 2x + page tag + RU`（8/8）/ `readers corner disclosure`（5/5）/ `images + credits 5/5` /
`P7 quotes clear of preview box`（max baseline 2351.17）/ `P1 headline <= 56`（41 字符）。

## 2. occlusion_audit.py — 0 flags（与 KIT 出入，见下）

`occlusion.log`：selftest OK（planted classes fired `BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX` 各 1，clean controls silent）；
`svg: 0 flags`，`ru-occlusion.json`：`{"flag_count": 0, "flags": []}`，rc=0。
**出入**：KIT §6 称 run5 为 1 flag（P1 LINEX graze：quiz 规则线 y=2312 擦 `em Brasília.` 行墨顶 2312.8，0.2px）。
我实跑为 0 flags——工具现态对该 graze 不报。几何本身仍存在，但已被 PROOF-NOTE D3 包含：
该行整行在框底（2310）与规则线（2311–2312）之下，问题比 0.2px graze 大得多，不单列。

## 3. 正典 creambox.py 全版扫描 — 发现 D1–D5（`creambox-all.log`，438 行）

`+45px 窗口 + 逐行 clearance + P7 toolbox` 全版扫描，rc=0。负 clearance / 负 desc-clear 逐项裁决如下
（像素核实均在 1:1 卡片 PNG 上做，奶油色 #f0eee5 / 墨色 sum<450 逐行计数）：

| 位置 | creambox 读数 | 像素核实 | 裁决 |
|---|---|---|---|
| P7 ERROS COMUNS 标题 | 框右 1862，墨右 1886.5（−24.5） | 标题行墨至 x=1885，奶油至 1858 | **D1 缺陷**（本版引入） |
| P1 数字框标题 | 框右 1411.5，墨右 1417.0（−5.5） | 标题行墨至 1416 | **D2 缺陷**（本版引入） |
| P1 EM POUCAS 框 | inside 末行 +9.6；BELOW +17.6 `em Brasília. (Página 4)` 基线 2327.6 | 奶油止 2309，规则线 2311–2312，该行墨 2313–2336 | **D3 缺陷**（核心携带，整行漫出） |
| P3 周框 | inside 末行 +14.9；BELOW +15.6 `16h30.` 基线 540.6 | 奶油止 524，该行墨 526–540 | **D4 缺陷**（核心携带，整行漫出） |
| P6 时间线框 | inside 末行 +28.6；BELOW +0.8 `Página do Participante.` 基线 840.8 | 奶油止 839，该行墨 825–845（降部至 845） | **D5 缺陷**（核心携带，降部漫出 ~5px） |
| P2 E VOCÊ 框 | inside 末行 +5.0，desc-clear −1.0 | 墨止 908，框底 909 | 非缺陷（0.30  allowance 高估） |
| P3 E VOCÊ 框 | inside 末行 +5.1，desc-clear −0.9 | 墨止 853，框底 854 | 非缺陷 |
| P4 E VOCÊ 框 | inside 末行 +5.1，desc-clear −0.9 | 墨止 904，框底 905 | 非缺陷 |
| P5 E VOCÊ 框 | inside 末行 +5.7，desc-clear −0.3 | 墨止 839，框底 840.5 | 非缺陷 |
| P5 数字框 `2027.` | inside 末行 +5.4，desc-clear −1.1 | 墨止 507，奶油至 512（`2027.` 无降部字母） | 非缺陷 |
| P7 A PALAVRA 框 | inside 末行 +4.5，desc-clear −1.5 | 墨止 1431，框底 1431.5 | 非缺陷（0.5px 内，零余量，见 O3） |
| P1 AGORA VOCÊ +37 / P2 `Atenção…` +32 / P3 `UM DIA, DOIS SENTIDOS` +37 / P6 `EXERCÍCIOS…` +42 | BELOW-WINDOW 行 | 各为框下另起的标题/正文，非本框续行 | 假阳性 |
| 其余全部框 | inside clearance ≥ +4.5 | — | 通过 |

P7-TOOLBOX 汇总：3 框，min inside clearance **+4.5**，min desc-clear **−1.5**。
core-pt 对照扫描（`creambox-core.log`）：P3 `16h30.` −15.6、P6 `Página do Participante.` −0.8、P1 同窗末行 2348
与本版几何一致——D3/D4/D5 为核心携带；core P7 标题墨至 1756、P1 数字框标题墨至 1340——D1/D2 本版无对照问题。

## 4. p8 compare — CLEAN，keydiff=[137, 138]（`p8-compare.log` / `ru-p8-compare.json`）

`core 150 noted / edition 150 noted / status: CLEAN / missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`，rc=0。
逐个裁决：
- **137**：core（葡语原文）→ ru `Пятница, 20 ноября, — национальный праздник.`。SVG 答案区 y=2118.4 行重建：
  `137. Пятница, 20 ноября, — национальный праздник. — Смотри …`——全文在印，正确翻译。
  提取器显示 `Пятница, 20 ноября,` 是其在首个 ` — ` 处截断的 artifact，非缺陷。
- **138**：ru `Палмейрас выиграл 5–4 по пенальти.` = `O Palmeiras venceu nos pênaltis por 5 a 4.`，正确翻译，非缺陷。
其余 148 键与 core 完全一致。

## 5. freeze — baseline 8/8，diff 仅 U+3000

- `freeze.py baseline`：`baseline: 8/8 SVGs byte-identical (repointed files: none)`，8 个 OK，rc=0（`freeze-baseline.log`）。
- `freeze.py diff` vs core-pt：各页增减字符串均为讲解层替换；added CJK 仅 U+3000，共 **9** 个（P1 2，余每页 1），rc=0
  （`freeze-diff.log` / `ru-freeze-diff.json`）。

## 6. keycheck — 150/150（`keycheck-150.json`）

`p8.py extract --total 150`：`noted set = 150 of 150`，rc=0（`p8-extract.log` / `ru-p8-extract.json`）。
手验方法：逐题对照题面 + text.md 正文 + in-exercise 答案 + SVG 答案区 + core 键。
150/150 通过，无错键。易错点均已逐一核实并记入 JSON notes：
Q58 `mais cedo`、Q108 `saíram`、Q112 `sair`、Q120 5 小时、Q124 P8 选项重排后 B=Norris、
Q125 周六赛属第 36 轮、Q131 A、Q83–86 工作日 10+5=15、Q150 开放题 + 样文 88 词。

## 7. boxtitle 逐个实测（PIL 真墨迹，`inkprobe.log`）

全版横向扫描：唯一超页右边界 1884 的元素是 P7 标题（墨右 1886.5，D1）。
全部 33 个奶油框首行标题墨右缘 vs 框右缘：仅两处为负——P1 数字框 −5.5（D2）、P7 −24.5（D1），
其余最小余量 +8.5（P1 EM POUCAS PALAVRAS）。P1 头条墨 x=88–1351，无溢出。

## 8. 印/网文字层比对

`pdfinfo`：两 PDF 均为 8 页，1462.5×2025pt。`pdftotext`：
印 54,990 字节 / 网 54,994 字节，各 8,173 词，词多重集差 0；
`diff` 仅断行/行序差异（masthead 断行、P1 日历行序），无内容差。网 PDF 文字层字节与 KIT 所述 54,994 一致。

## 9. P8 最小字号实测（`inkprobe.log` §C）

P8 全部字号（SVG 单位）：13.0–46.0；答案区（y>1250）最小 **13.0 单位 ×0.75 = 9.75pt**，
共 1327 个 span，恰为 SOP §1.1 下限 9.75pt，不低于下限。KIT 的 9.75pt 与实测一致。
P8 答案流末行基线 2546.68（y>2500 扫描，页脚 2624 除外），墨底约 2551 < 2560，余量约 9px。

## 10. 弯引号 + CJK 全版扫描（`inkprobe.log` §D/E）

- U+201C/U+201D/U+2019：P1–P7 全部为 0；P8 为 201C×2、201D×2、2019×0——
  位于 E139/E140 俄语句源（`“…”.`），正确用法；正文内容中直引号 `"` 为 0。
- CJK：P1 仅 moth logo `<title>` 内 `三色蛾`（非读者面）；其余 7 页无 CJK（U+3000 除外）；
  text.md CJK 字符 0（Python 扫描）。

## 11. 外部事实来源

- 星期/日期：`date -d`（America/Toronto）：2026-11-15 周日、11-16 周一、11-17 周二、11-20 周五、
  11-21 周六、11-22 周日、11-27 周五、12-06 周日、11-07 周六、11-08 周日——与版内全部一致。
- 事实均冻结自 core-pt（KIT §2，2026-11-10 已核来源）；本版未加新事实。
  复校未重复核查 core 事实来源，仅核对版内自洽（Enem 13h30–18h30=5 小时；工作日 10+5=15；比分与 P4 表一致）。

## 12. 判为非缺陷的项（汇总）

1. E VOCÊ 各框 desc-clear −0.3…−1.0（P2/P3/P4/P5）——像素墨底均在框底内 0.5–1px，0.30 降部 allowance 高估。
2. P5 数字框 `2027.` desc-clear −1.1——无降部字母，墨底 507 < 奶油 512。
3. P7 A PALAVRA 框 desc-clear −1.5——墨底 1431 < 框底 1431.5（0.5px 内，零余量，列为 O3 观察项）。
4. 四处 BELOW-WINDOW 负值——框下另起标题/正文，假阳性。
5. Occlusion KIT 称 1 flag vs 实跑 0 flags——工具现态不报；几何已由 D3 覆盖，不另立项。
6. keydiff [137, 138]——正确俄译；137 提取器截断为工具 artifact。
7. text.md E 节 `Traduza`——目标语节名，各节一致；SVG 内已有俄语 `Перевод` ×4；无中文残留。
8. P1 0.2px LINEX graze——被 D3 包含，不单列。

## 文件清单（本 scratch）

`PROOF-NOTE.md` / `GATE-LOG.md` / `keycheck-150.json` / `gates.log` / `occlusion.log` / `ru-occlusion.json` /
`p8-extract.log` / `ru-p8-extract.json` / `p8-compare.log` / `ru-p8-compare.json` /
`freeze-baseline.log` / `freeze-diff.log` / `ru-freeze-diff.json` /
`creambox-all.log` / `creambox-core.log` / `inkprobe.log` / `inkprobe.py` /
`print.txt` / `web.txt` /
`crop-p1-em-poucas.png` / `crop-p3-weekbox.png` / `crop-p6-timeline.png` / `crop-p2-evoce.png` /
`crop-p7-wordbox.png` / `crop-p7-boxtitle.png` / `crop-p1-numtitle.png` / `crop-core-p7-boxtitle.png` / `probe.txt`
