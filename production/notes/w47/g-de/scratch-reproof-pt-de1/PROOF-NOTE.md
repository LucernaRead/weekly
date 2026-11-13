# PROOF-NOTE — 2026-W47 pt-de（葡萄牙语目标 · 德语读者）re-proof（fix1 重建版复校）

独立复校员：re-proof（SOP §8.4；与 fix1 修复员不同人，与原 proof1 不同人），2026-11-11。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-de1/`
（全部工作文件见该目录；生产目录零写入，未 commit，未 push。）
复校对象：fix1 D4 返修重建版（FIX-LOG.md / GATE-LOG.md 在 `scratch-fix-pt-de1/`，已读，仅作参考，
结论全部由本人独立重跑得出，未照抄）。

## §0 版身份核对（磁盘为准，开工与收工各验一次，一致）

| 文件 | 磁盘字节数 | 磁盘 SHA-256 | 与任务预期一致 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | 12,938,912 | `b8a738defa8be888fffc9ba670b32d65a2146224c10fe718f55258ebd55a513d` | ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | 1,147,636 | `2cad3d1b1b732e2ce1f11631d1f05c6fb196ab715b3f77f4965e2ca724483e69` | ✓ |
| `2026-w47-pt-de.text.md`（文） | 37,907 | `519ab0dedbae110dba11eeffe3cd8517db41141020061e9a66c5dd252d784305` | ✓（与修前逐字节相同） |

探针：`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0
（与 proof1/proof2/fix1 同值）；`/dev/null` 存在。解释器全程 `tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0）。
TMPDIR 全程指向自家 scratch 下 `tmp/`（系统 /tmp 未用）。核心 HEAD `c0382fa7`；
`git status --porcelain`：版目录仍为 untracked（`?? production/2026-w47/2026-w47-pt-de/`），无修改；
core-pt 只读，未动。

## 结论：(a) 零缺陷，可定稿

fix1 的 D4 修复经本人独立重测证实（PIL 真墨 1826.5，余量 +35.5；交付印 PDF 像素 200dpi 1826.9，余量 +34.6，
均 ≤1858 合格线；300dpi 裁图目视末字 `e` 完整在奶油框内）。全部机械门通过，D1/D2/D3 修复存活，
E1/E2 边缘未动，150 题逐题手验全部正确，8 页逐页目视无新缺陷。按 SOP §8 proofread-until-zero，本版可定稿。
缺陷清单：**无**。

## D4 修复复验（重点，独立重测，不照抄 fix1 数值）

- 源码：`content12.py:89` 现为 `"NESTA EDIÇÃO　Diese Ausgabe"`（24pt 粗体，x=gx+22 不动）；
  `tables_de.py:139` 同步为 `"本期目录": "Diese Ausgabe"`；本版 `*.py` 再无 `In dieser Ausgabe`（grep RC=1）。
- PIL 真墨（`boxtitle_ink.py`，24pt 粗体，svglib 字体）：墨迹右缘 **1826.5**，奶油盒右缘 1862.0，
  余量 **+35.5**，合格要求 ≤1858 ✓（与 fix1 称 1826.5 / +35.5 逐值一致——本次为独立重跑，非引用）。
- PIL advance（`boxtitle_core.py`）：右缘 1826.1，余量 +35.9 ✓。
- 交付印 PDF 像素（`pixel_boxtitle_pdf.py`，200dpi）：墨迹右缘 **1826.9**，余量 **+34.6** ✓。
  （注：该脚本内硬编码的标题标签仍写旧串 `In dieser Ausgabe`，但测量带取的是实际渲染标题行 y=1278，
  测得值 1826.9 即新标题实测值，标签陈旧不影响测量有效性。）
- 目视：300dpi 原生裁图 `visual/crop-p1-nesta-pdf300.png`——末字 `e` 完整在奶油框内，右端距框缘约 35 单位。
- 全版盒标题横向真墨重扫（31 框）：OVERFLOW **0** 处；最紧为 E1 +0.5、E2 +1.5，其余 ≥+22.5。

## 边缘记录（不计缺陷，确认未动）

- **E1** P1 `EM POUCAS PALAVRAS　IN KÜRZE`：PIL 真墨 1861.5（+0.5）、advance +0.9、印 PDF 像素 200dpi 1862.4——
  与修前逐值相同（proof2 同值），未动。按 ru O3 的 0.5px 边际带裁定为边缘通过。
  （注：PDF 像素口径下奶油盒右缘测为 1861.4，故像素余量记为 −1.0；该值亦与修前逐值相同，是渲染亚像素所致，
  非新溢出。）
- **E2** P1 `A SEMANA EM NÚMEROS　In Zahlen`：PIL 真墨 1410.0（框缘 1412，+1.5）、PDF 像素 200dpi 1408.3（+2.9）——
  与修前相同，未动。

## 必查项裁决

- **run.py**（scratch 副本重建）：RC=0，`TOTAL 150`（A2 48 / B1 71 / B2 31；
  每页 10/18/18/18/18/18/12/38；Sätze vervollständigen 61 / Multiple Choice 49 / Wortschatz-Zuordnung 12 /
  Satzbildung 7 / Richtig oder falsch 3 / Lückentext mit Auswahl 13 / Übersetzung 4 / Schreiben 1；model words 88），
  `OVERFLOW` 0 行。重建 SVG 与现盘 SVG **8/8 逐字节一致**（cmp）。
  `gates.py`（scratch 副本）：**16/16 PASS**，`FAILURES: none`，RC=0。pt 系 run.py 不写 `registry.json`
  （core-pt/pt-de 均无此文件，run.py/bslib4.py 内无引用；只存在于 en 系）——不判缺文件。
- **freeze**：核心 baseline **8/8**（`--build` 真核心 core-pt，`--core-svg` 核心 svg；
  核心哈希 bd87a867…a7b7a661，与 proof2 一致；核心完整性重哈希无改动）；版 baseline **8/8**
  （p1 6ced52ce、p2 613f558b、p3 c33752e6、p4 af3e206b、p5 d146ca3d、p6 dd562a7a、p7 2d53f697、p8 a4447964）；
  freeze diff 新增 CJK 共 **9 个，全部为 U+3000** 家具分隔符（P1: 2，其余每页 1）。
- **occlusion**：真实审计命令（未传 `--selftest`）**0 flags**，RC=0（`occlusion.json`：`flag_count: 0`）。
  盲区已知：BOXTITLE 检查只看带描边或 fill `#2c2822` 的矩形，无描边奶油框不在检查之列——
  本次验收不依赖 occlusion，改以 boxtitle 真墨 + PDF 像素双法复测（见上）。
- **p8**：extract **150/150**；compare 直接读 `p8-compare.json` 本体：**status CLEAN**，core 150 / edition 150，
  `keydiff: [137, 138]`（预期；两句德语译文逐题验过，正确——见下），missing []、extra []。
- **keycheck**：**149/150**，仅 #150 例外（开放写作题，REG 键 `(offene Aufgabe — Mustertext unten)`，
  提取为 `✓`，预期内）。
- **creambox**（正典，`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`）：
  31 框 OWN 真墨余量全部为正，最小 **+2.1**（P2 `Palmeiras–Flamengo-Duell`）；6 处 inside-only desc-clear 负值
  （−0.3…−1.1）均为已知无降部误报，真墨复测墨余 +4.8–5.4；5 处 below-window 负值（−32.0/−37.0/−42.0）
  均为已知下块标题假阳性（diag 判 owner-rect=NONE，与修前同）。
- **D1/D2/D3 存活**：D1 `content12.py:138` 框 474 在位，末行 `em Brasília. (Página 4)` 墨底 2332.6，
  墨余 **+15.4** ✓；D2 `content34.py:40` `+ 58` 在位，末行 `16h30.` 墨底 540.9，墨余 **+10.1** ✓；
  D3 `content56.py:132` 框 654 在位，末行 `Página do Participante.` 墨底 846.0，墨余 **+8.0** ✓。
- **回归（SVG）**：以 proof2 修前基线为准（`scratch-proof-pt-de2/build-copy/svg/`，freeze 哈希 f988db96…a4447964），
  仅 **p1 不同**（f988db96 → 6ced52ce，即 D4 标题一处），**p2–p8 逐字节一致**（cmp 7/7）。
  注：任务括号所指 `scratch-refanout-pt/backup-old/` 是第一轮备份（core-pt fix2 重 fanout 之前），
  其 p3/p4/p6/p8 与现盘各差 1 行（SVG 为单行文件，即整行）——那是 D1/D2/D3 核心修复本身，
  非 fix1 回归；以 proof2 基线为准才是 fix1 前后比对的正确口径。
- **D5 gloss**：P4 gloss 框实测 4 行，末行 `pausa die Pause · a taça Pokal.` 右余 **+101.5**、底余 **+42.7**，
  无溢出；渲染 `o título Titel`（第 3 行）。D5 字体问题只记录不判：P5 印 PDF 共 **4** 个内嵌字体子集
  （`NGCYSB+NotoSansCJKsc-Regular`、`UIKPPO+Newsreader16pt-Regular`、`WRUMGD+Newsreader16pt-Regular`、
  `YCHKXS+NotoSansCJKsc-Bold`；即 3 个字体族）。
- **印/网文字层**：`pdftotext -layout` 逐字节一致（111,358 B；修前 111,362 B，差 4 字节为标题删去 `In ` 所致）；
  fitz 逐页比对 **8/8** 一致（5366/4598/4280/4919/4599/4536/5215/13489；P1 5370→5366 为标题少一词所致）；
  check_final 词数印 8,435 = 网 8,435（修前 8,436，差 1 为标题删去的 `In` 一词），multiset diff 0；
  斜体 span 印 1 = 网 1（`« consciência »`）。网 PDF 只在 scratch 重渲比对
  （`web-rerender.pdf` 1,147,640 B，SHA 与交付不同为预期现象——fontTools 嵌时间戳），
  文字层与交付网 PDF 逐页一致；交付网 PDF 未被触碰（收工 SHA 仍为 `2cad3d1b…`）。
- **P8 最小字号**：9.75pt（n=380），低于 9.75pt 者 0——正好 SOP §1.1 底线，不低于；
  check_final P8 答案区 span 最小 9.75。
- **孤儿标点**：SVG 文本行首孤儿标点扫 **0**（1,637 行）；弯引号成对：text.md `«` 40 = `»` 40，
  `“` 2 = `”` 2，单弯引号 0；SVG `«` 40 = `»` 40，无失衡文件；text.md CJK 字符 **0**，
  SVG 非 U+3000 CJK 仅 3 字（`三色蛾`，位于 P1 logo `<title>Lucerna 三色蛾</title>` 元数据内，
  非渲染正文，core-pt 8 页 SVG 亦同款——品牌标记，非缺陷）。
  禁词/简体残留：text.md 内 `简体/繁体/中文/TODO/XXX/Lorem` 均为 0。
  观察项（非缺陷，proof2 O1 同款，核心继承）：text.md `«consciência»` ×1 与 `« consciência »` ×1 并存，
  引号内空格不一致。
- **sweep**：box-vs-hline flags 0；bridges found 20；bridge orphans **2**（均为
  `Ergänzen Sie mit den Wörtern aus dem Kasten.`，P3/P5 行 1 `(88.0, 2564.45)`、行 2 `Kasten. (538.5, 1696.5)`——
  与修前备份坐标逐字节相同，proof1 O4，KIT 已注明，核心流式排版行为）；bridge widows **0**。
- **溢出横扫（gate 7，本人新写 `sweep_overflow.py`）**：189 个矩形 × 1,637 行文本逐一真墨核算，
  13 标记——**全部 13 处与 core-pt 同脚本扫出的 13 处逐项相同**（同文本、同数值），无一处为本版新增：
  12 处 PAGE-LEFT 为左对齐标题大写字母字形侧边距伸出内容边 88.0 仅 1.0 单位（墨迹 87.0，核心同款，
  设计固有，非裁切边溢出）；1 处 V-SPILL（P8 `A　COMPLETE A CRÔNICA`，墨底 202.0 vs 刊头带底 182.0）
  为本人脚本窗口过宽的假阳性——该标题基线 y=202 在刊头带（88,72,1774×110）之下，本就不属于该框，
  核心同款。结论：横扫 **0 本版新增溢出**。
- **check_s11（pt 适配版）**：ALL PASS（色集 core 21 = edition 21；三徽章色齐全；
  P8 最小 SVG 字号 13.0 单位 = 9.75pt；P8 芯片数/色与核心一致 35；题号 113–119 + 145–149 与 `120.` 齐全；
  `ESCREVA VOCÊ` 在位）。注：芯片位置与核心差 8 处（fix1 记 4 处，计数口径差），
  P8 SVG 与 proof2 修前基线逐字节一致（a4447964），属修前既有德语排版流位移，非本次改动所致。
- **verify_ed（pt 适配版）**：ALL PASS（23/23：D4 源两处 + SVG + PIL 真墨 + PDF 像素、E1/E2 原位、
  D1/D2/D3 源码行 + 实测、Q137/138 德语键、Q150 `✓`、text.md 不变、两 PDF 各 8 页）。
- **8 页目视**（印 PDF 130dpi，`visual/p-1.png`…`p-8.png` + P1 300dpi 裁图）：无新缺陷。
  所见均为已知接受项：P3/P5 `Kasten.` 孤字（O4）、P2/P5 中部版式留白（固有）、
  P3/P4 `B AS PALAVRAS DO TEXTO` 栏目标题落栏底（O4）、P1 E1 末字 `E` 贴框边（E1 原位）。
  P6 图表柱 10 天 : 5 天 = 2:1；D 节桥接 `Kasten: prazo · dia útil · coerência · chute` 同栏连续；
  P7 `FRASES DA SEMANA` 8 句（含 `(wörtlich aus dieser Ausgabe)`）；P8 A–H 节 113–150 齐全，
  RESPOSTAS 含 `150. ✓ Siehe den Mustertext… (88 Wörter)`，Mané Garrincha 照片 + 出处干净。

## 150 题逐题手验（text.md 535 行通读 + REG 键逐项核对 + P8 目视）

- 题号 1–150 连续；每页题量 10/18/18/18/18/18/12/38；Respostas 节键与各页练习键逐项一致。
- **Q73**（教训所指类）：题干 `Depois da prova, começa a ___.`，键 `espera`——
  P5 正文原句即 `Depois da prova, começa a espera pelo gabarito.`，逐字适配，正确。
  （Q70 `começa a espera pelo ___.` 键 `gabarito` 与之互补，无冲突。）
- **Q83–87** 工作日重算：11 月 16–30 日共 15 天；工作日 10 天（16–19、23–27、30，扣 20 日假期）；
  周末 + 假期 5 天（21、22、28、29 + 20 日）；10+5=15。Q83 B（15 天）、Q84 A（10）、Q85 B（5）、
  Q86 B（15）、Q87 B（期限）全对。
- **Q120**：13h30–18h30 = 5 小时，键 B 正确。**Q125**：36ª rodada Palmeiras × Flamengo，周六 21 日 16h30，
  Nubank Parque——proof1 已用 CBF 赛程外部核实，本次未重复外部核查，结论沿用 proof1。
- **Q137/138**（p8 keydiff 两题）：137 `Freitag, 20. November, ist ein nationaler Feiertag.`、
  138 `Palmeiras gewann das Elfmeterschießen mit 5:4.`——德语正确。
  Q139 `O gabarito oficial sai até o fim de novembro.`、Q140 `Anote as suas respostas e confira quando sair o gabarito oficial.`——
  德→葡翻译正确。Q141–144 配对（c/d/b/a）、Q52–55 配对（b/a/d/c）、Q25–28 配对（a/b/c/d）、
  Q56–59 比较级（mais/mais/mais/menos）、Q76–79 将来时（sairá/publicarão/decidirá/chegará）、
  Q101–112 语法（含 Q108 `saíram`、Q109 `sair`、Q110 `for`、Q111 `tiver`）、Q113–120、Q121–132（Rafael 阅读）、
  Q133–136 造句、Q145–149 对话（Mané/sexto/quinto/na/obrigado）逐题验过，全部正确。
  范文重数 **88 词**（实测 88）。Q1–Q64 填空/动词变位/选择题逐题验过，与正文事实一致
  （如 Q29 C 1695、Q31 B 14.759、Q47 A 1–1/3–1、Q49 B 5–4、Q51 A Norris、Q65 B、Q80–82 V/F/V）。
- keycheck 机械比对 149/150（仅 #150，预期）；P8 目视核对答案键与 Respostas 节一致。

## 说明

1. 本次复校未向生产目录写任何文件；build-copy、web 重渲、全部日志与图片均在自家 scratch 内。
2. proof2 的 D4 已由 fix1 修复并经本次独立重测证实；proof1 的 D1/D2/D3 修复全部存活。
3. 工具链说明：pt 系无现成 check_s11.py/verify_ed.py，沿用 fix1 在其 scratch 写的 pt 适配版
   （en 原版未动）；creambox.py 为正典共享工具（`hidden_files/w47/tools/`），未改动。
