# GATE-LOG — 2026-W47 pt-nl proof1 机械门实跑证据

复校：proof1（独立复校），2026-11-11。工具链：`~/workspace/weekly-git/tools/venv/bin/python`；
正典 creambox `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与任务所给一致）。
本目录（scratch）即证据存放处：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-nl1/`。
全程 `TMPDIR` 指向本目录下 `tmp/`，未用系统 /tmp。仓库侧 `hidden_files/` 未写入。

## §0 身份核对（磁盘为准）

```
$ sha256sum A-Lucerna-VOL4.pdf A-Lucerna-VOL4-web.pdf 2026-w47-pt-nl.text.md
5a58050b684893bba2a4e35ab3569f74f7a14e8bfb74da65db0da1104a3bfe48  A-Lucerna-VOL4.pdf
30db8b9ca8a3331ca2ff323c673c7422ab8cd2cffae1df6263f4156fd4a69b99  A-Lucerna-VOL4-web.pdf
c2ff3429ed601e7b2e43451eb30f7406780752fb018a40ac526da26146164a35  2026-w47-pt-nl.text.md
A-Lucerna-VOL4.pdf 12935390 bytes / A-Lucerna-VOL4-web.pdf 1105901 bytes / 2026-w47-pt-nl.text.md 37571 bytes
```
三项 SHA 与任务消息完全一致。印/网 PDF 各 8 页（PyMuPDF 计数）。

## §1 gates.py（构建者自查门，proof1 重跑）— 16/16 PASS

`gates-proof1.log`：`[PASS]` ×16，`FAILURES: none`。逐项：
VOL.4 + 周日期；副标题主题；footer + 页码行 8/8；无 VOL.3 刊别残留（VOL.3 仅现于 P7 承诺引述）；
截稿注 + 决赛命名；P1 刊头行 fit 1820（`{330: 300.4, 372: 808.5}`）；同基线墨迹碰撞 0；
页框墨迹穿越 0（最小边距 L/R/T/B = [47.0, 3.5, 35.0, 32.0]，按内框 40..1910×40..2660 计；
其中 R=3.5 即 D6 标题墨迹右缘 1906.5——gates 框限 1910 只拦出页框，不拦出奶油框，故 D6 在此门下仍为 PASS，
须以 §8 的 PIL 框界实测为准）；
P6 图表标签覆盖 0%；gloss 29 项枚举（P2–P6 各 6/6/6/6/5）；gloss 词头存活 0 缺失；
P7 金句 8 条各 2× + 页签 + 荷兰语；读者园地 5/5；图片 + 出处 5/5；
P7 金句区与预告框无交（末行基线 2351.17）；P1 头条 41 非空字符 ≤56。

## §2 occlusion_audit.py — 自测通过，本次运行 0 flags（与构建者记录的差异见 §5）

```
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
svg: 0 flags
```
`occlusion-proof1.json`：`{"svgdir": "svg", "flags": [], "flag_count": 0}`。
注意：该审计对奶油框内溢出、框标题横向溢出、降部溢出是盲的——D1–D6 均由 creambox + PIL 真墨迹 + 像素裁图另行实测（§4、§8），不以此 0 flags 为无缺陷证据。

## §3 p8.py — extract 150/150，compare CLEAN

- extract（`p8-extract-proof1.log/json`）：`svg/p8-avaliacao.svg: noted set = 150 of 150`，题号 1–150 连续无缺重。
- compare vs core-pt（`p8-compare-proof1.log/json`）：`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。
  - 137/138 为翻译题答案的读者语 rendering：137 `Vrijdag 20 november is een nationale feestdag.`、138 `Palmeiras won met 5–4 na strafschoppen.`，已逐字验为正确荷兰语译文（keycheck-150.json Q137/Q138），非缺陷。
- 印刷键与 text.md 答案对照：150/150 一致（Q150 印刷键为 `✓` 标记，text.md 为 `✓ Zie de modeltekst…` 指向句，同一结论；见 keycheck-150.json）。

## §4 正典 creambox.py 全版扫描（+45px 窗口 + 逐行 clearance + P7 toolbox）

`creambox-proof1.log`：31 个奶油框。逐框裁决（inside-only 末行 clearance / desc-clear 为准；below-window 行为框外下一元素时为假阳性）：

| 页/框 | inside-only 末行 | clearance | desc-clear | below-window | 裁决 |
|---|---|---|---|---|---|
| P1 数字框 y=786 | 1175.2 `20–22 november)` | +45.0 | +39.0 | +37.0 `AGORA VOCÊ`（下一栏目标题） | 假阳性，通过 |
| P1 日历框 y=588 | 1161.3 `Friday chega na sexta, 27.` | +51.0 | +44.6 | — | 通过 |
| P1 目录框 y=1238 | 1562.4 `Pág. 8` | +16.0 | +9.7 | — | 通过 |
| P1 KORTOM y=1874 | 2300.4 `…6 de dezembro,` | +9.6 | +3.6 | +17.6 `em Brasília. (Página 4)` | **D1：该行是框内条目续行，整行出框** |
| P2 PARA NÃO ERRAR y=605 | 797.9 `o horário do comércio.` | +48.1 | +41.6 | — | 通过（纵向）；标题横向见 §8 D5 |
| P2 gloss y=858 | 1015.4 `…prijskaartje.` | +47.7 | +41.6 | — | 通过 |
| P2 VOCÊ SABIA y=200 | 507.6 `feriadão de três dias.` | +11.4 | +4.9 | — | 通过 |
| P2 E VOCÊ y=545 | 904.0 `twee zinnen en stuur ze op.` | +5.0 | −1.0 | — | 见 §8：PIL 墨迹底 = 框底，不越边 |
| P2 日程 4 格 y=1618 | 1731.9 / 1761.2 / 1731.9 / 1731.9 | +36.1/+6.8/+36.1/+36.1 | +30.4/+1.1/+30.4/+30.4 | +32.0 `Atenção:…`（框下注文） | 假阳性，通过 |
| P3 gloss y=200 | 357.4 `combate strijd.` | +47.7 | +41.6 | +37.0 `UM DIA, DOIS SENTIDOS`（下一节标题） | 假阳性，通过 |
| P3 日程 y=200 | 510.1 `Sáb 21 — Palmeiras × Flamengo, às` | +14.9 | +8.4 | +15.6 `16h30.` | **D2：该行是框内条目续行，整行出框** |
| P3 E VOCÊ y=551 | 848.9 `stuur ze op.` | +5.1 | −0.9 | — | 见 §8：PIL 墨迹底 −0.1px 在内 |
| P3 记忆词 y=880 | 1060.6 `feriado de memória.` | +19.4 | +13.0 | — | 通过 |
| P4 gloss y=270 | 398.2 `…a taça beker.` | +47.7 | +41.6 | — | 通过 |
| P4 finalistas y=200 | 465.2 `Mané Garrincha, Brasília.` | +110.8 | +104.4 | — | 通过 |
| P4 E VOCÊ y=602 | 899.9 `ze op.` | +5.1 | −0.9 | — | 见 §8：PIL 墨迹底 −0.1px 在内 |
| P5 计划 y=200 | 833.0 `…dankbaar zijn)` | +46.6 | +40.3 | — | 通过 |
| P5 gloss y=892 | 1019.2 `· pesar afwegen.` | +47.7 | +41.6 | — | 通过 |
| P5 数字 y=200 | 507.6 `2027.` | +5.4 | −1.1 | — | 见 §8：无降部，墨迹 −5.4px 在内 |
| P5 E VOCÊ y=539 | 806.4 `…stuur ze op.` | +5.1 | −0.9 | — | 见 §8：PIL 墨迹底 −0.1px 在内 |
| P6 gloss y=343 | 441.4 `…een gok.` | +47.7 | +41.6 | — | 通过 |
| P6 时间线 y=200 | 811.4 `A nota individual sai na` | +28.6 | +22.3 | +0.8 `Página do Participante.` | **D3：该行是框内步骤续行，降部出框** |
| P6 读数 y=866 | 1046.6 `…diz pouco.` | +19.4 | +13.0 | — | 通过 |
| P6 图表两框 y=1594 | 1876.0 / 1854.0 | +40.0/+62.0 | +34.8/+56.8 | +42.0 练习栏目标题 | 假阳性，通过 |
| P7 工具箱 y=200 | 1102.9 `…loopt tot zondag 22.` | +32.6 | +26.8 | — | 纵向通过；标题横向见 §8 D6 |
| P7 词语 y=1158 | 1427.0 `…en de cultuur.` | +4.5 | −1.5 | — | **D4：降部溢出 +0.5px（PIL，§8）** |
| P7 读者园地 y=1454 | 1948.9 `…naar VOL.5.` | +9.6 | +3.7 | — | 通过 |
| P8 | （无奶油框） | — | — | — | — |

P7-TOOLBOX 小结：3 框，min inside clearance +4.5，min desc-clear −1.5（即 D4 框）。
core-pt 对照扫描（`creambox-core-pt.log`）：P1 KORTOM、P3 日程、P6 时间线三框数值与本版逐字相同（inside-only 2300.4/+9.6、510.1/+14.9、811.4/+28.6），证实 D1–D3 为核心层几何。

## §5 occlusion 1 flag → 0 flags 的差异说明

构建者 scratch `nl-occlusion2.json` 记 1 flag：P1 LINEX，`em Brasília. (Página 4)`，
墨迹框 `[1461.5, 2312.8, 1665.5, 2332.6]`，线框 `[87.0, 2311.0, 1863.0, 2313.0]`（Quiz 分隔线 `y=2312`）。
本次 proof1 同 SVGs（freeze 8/8 校验未变）重跑为 0 flags。
`git log tools/occlusion_audit.py`：最近改动 `8418be11`（§1.1 样式上线：审计识别 Newsreader + DejaVu Sans，页脚线阈值 2580→2596），
属工具版本漂移。该 flag 的实质几何经 PIL 手工复核属实，即 D1（墨迹顶 2311.6，线 y=2312 横贯升部），
已列入缺陷，不因工具 0 flags 而放过。

## §6 freeze.py — baseline 8/8，diff 新增 CJK 仅 U+3000

- baseline（`freeze-baseline-proof1.log`）：`8/8 SVGs byte-identical (repointed files: none)`，
  8 页哈希逐一匹配；`core integrity: shipped core SVGs unchanged by the run`。
- diff vs core-pt（`freeze-diff-proof1.log/json`）：各页增减字符串为讲解层替换；
  新增 CJK 字符合计 9 个，全部为 U+3000（家具分隔符，P1 ×2、其余各页 ×1）；无新增中文/其他 CJK 实字。

## §7 印/网文字层比对、P8 字号、引号扫描、CJK/内部标签扫描

- 印/网文字层：`pdftotext` 印 47,243 字节、网 47,250 字节；词多重集差 **0**（各 8,589 词，按空白分词；
  KIT 记 8,561 词为计数方法差，不影响差为 0 的结论）；两文本非逐字节相等（仅空白/版式差）。
- P8 最小字号（PyMuPDF 实测 print PDF P8 全部 394 spans，非 KIT 配置数）：
  最小 **9.75pt**（印/网一致），等于 SOP §1.1 下限 9.75pt；样例：`1. consciência — consciência = …`、`100. chute — chute = een gok` 均为 9.75pt。
- 弯引号：SVG 可见文本中 U+201C/U+201D 各 2 次，仅 P8 E139/E140（荷兰语源句各一对，配对正确）；
  U+2019 全版 0 次；直引号（ASCII `"`/`'`）在可见文本中仅 1 处：P7 A2 `cair betekent 'vallen op een dag'`（见 PROOF-NOTE O1）。
- CJK：text.md 0 个 CJK 字符；8 页 SVG 可见文本 0 个 CJK 字符（仅 U+3000 分隔符与蛾标 `<title>` 内 3 字，非读者可见文本）。
- 内部标签：text.md 仅命中 `VOL.3` ×2（均在 P7 读者园地承诺引述中，gates 允许）；`翻譯/翻译/type/cover/SOP/W47/pt-nl` 均 0 命中。
  E 节无 type 标签（§见 PROOF-NOTE (d)）。
- 日期星期：`TZ=America/Sao_Paulo date -d` 核实 2026-11-07 六、08 日、14 六、15 日、16 一、17 二、20 五、21 六、22 日、23 一、27 五、12-06 日，与文中全符。
- 工作日算术（P6）：16–30 日共 15 天；工作日 10 天（16、17、18、19、23、24、25、26、27、30）、
  周末+假日 5 天（20、21、22、28、29）；10+5=15；第 10 个工作日 = 11 月 30 日；若 20 日计入则为 11 月 27 日——
  与正文“27–30 日窗口（视 20 日是否计入）”的表述一致。

## §8 PIL 真墨迹专项（D1–D6 及排除项）

方法：版内 `svglib` 同款 PIL 字体，`getbbox(anchor='ls')`，与 gates.py 同法。结果：

| 项 | 行/标题 | 框界 | PIL 墨迹 | 溢出 |
|---|---|---|---|---|
| D1 P1 | `em Brasília. (Página 4)` 基线 2327.6 | 底 2310.0 | 2311.6..2332.6 | **+22.6px**（整行出框；线 y=2312 横贯） |
| D2 P3 | `16h30.` 基线 540.6 | 底 525.0 | 524.6..540.6 | **+15.6px**（整行出框） |
| D3 P6 | `Página do Participante.` 基线 840.8 | 底 840.0 | 825.8..845.8 | **+5.8px**（降部） |
| D4 P7 | `herinnering aan de strijd en de cultuur.` 基线 1427.0 | 底 1431.5 | 1410.0..1432.0 | **+0.5px**（降部） |
| D5 P2 | 标题 `PARA NÃO ERRAR␣Het ezelsbruggetje` | 右 961.0 | 右缘 985.5 | **+24.5px**（横向） |
| D6 P7 | 标题 `ERROS COMUNS␣Veelgemaakte fouten` | 右 1862.0 | 右缘 1906.5 | **+44.5px**（横向；页余量 43.5px） |
| 排除 P2 E VOCÊ | `twee zinnen en stuur ze op.` | 底 909.0 | 底 909.0 | 0.0（贴边，不越边） |
| 排除 P3 E VOCÊ | `stuur ze op.` | 底 854.0 | 底 853.9 | −0.1（在内） |
| 排除 P4 E VOCÊ | `ze op.` | 底 905.0 | 底 904.9 | −0.1（在内） |
| 排除 P5 E VOCÊ | `Schrijf twee zinnen en stuur ze op.` | 底 811.5 | 底 811.4 | −0.1（在内） |
| 排除 P5 数字 | `2027.` | 底 513.0 | 底 507.6 | −5.4（在内；无降部） |

全框体横向扫描（8 页全部奶油框、全部行，墨迹右缘 vs 框右缘、左缘 vs 框左缘）：
仅 D5、D6 两处溢出；core-pt 同扫描 0 处。P1 框标题/副标题无横向溢出
（KORTOM 标题墨迹右缘 1853.5 < 框 1862；刊头行 fit 1820 通过；顶栏三行墨迹右缘 293.0 / 1222.1 / 1800.5，均在页内）。
PDF span 实测全版文字最小右余量 39.3px（P7 D6 标题本身），无文字出页边。
像素裁图证据：`crop-p1-kortom.png`、`crop-p3-sched.png`、`crop-p6-timeline.png`、
`crop-p7-wordbox.png`、`crop-p7-tooltitle.png`、`crop-p2-paratitle.png`、
`crop-p2-evoce.png`、`crop-p5-numbers.png`；整版图 `page-p1.png` … `page-p8.png`（印 PDF 渲染，110dpi）。

## §9 外部事实来源（独立检索，2026-11-11）

- Copa do Brasil 2026 半决赛次回合：Grêmio 1–1 Atlético-MG（7 日周六，Arena MRV，首回合 Grêmio 2–0，总比分 3–1）；
  Vasco 2–1 Palmeiras（8 日周日，São Januário，首回合 Palmeiras 1–0，总比分 2–2，点球 5–4）；
  决赛单场 6 日，马内·加林查，巴西利亚。
  来源：infobotucatu.com〈Copa do Brasil 2026: Palmeiras e Grêmio garantem classificação〉（2026-11-09）、
  futebolinterior.com.br〈Vasco 2 (4) x (5) 1 Palmeiras〉（2026-11-08）、sportradar.com 两场赛果页。
  与正文 P1/P4 及 Q47–50、Q122–123 全符。进球者名（Renan Lodi / Carlos Vinícius）未在检索片段中出现，见 PROOF-NOTE O2。
- F1 圣保罗大奖赛 2026-11-08：Norris 冠军、Verstappen 第 2、Hadjar 第 3、Mercedes 车队冠军。
  来源：theScore/AP〈Norris wins Sao Paulo GP, Mercedes secures constructors'〉、frontstretch.com 赛评（2026-11-10）。
  与正文 P4 及 Q51、Q124 全符。
- `Nubank Parque`：Allianz Parque 于 2026 年 5 月 4 日更名为 Nubank Parque（球迷投票选定）。
  来源：en.wikipedia.org/wiki/Nubank_Parque、palmeiras.com.br〈Nubank Parque〉。与正文 P4 表格全符。

## §10 判为非缺陷的项

1. E VOCÊ 四框末行（P2/P3/P4/P5）：creambox desc-clear −0.9~−1.0 提示窄带，但 PIL 真墨迹底恰为框底（0.0/−0.1px），
   未越边；0.30em allowance 高估了 `p` 的实际降部深度。不记缺陷。
2. P5 数字框 `2027.`：desc-clear −1.1，但该行无降部字母，PIL 墨迹底 −5.4px 在内。不记缺陷。
3. P1 LINEX 0.2px 擦线（构建者记录）：实质即 D1，已按 D1 计，不另立项。
4. P2/P3/P5/P6 中部留白：核心版式流，与 core 一致（PROOF-NOTE O4）。
5. P3/P4 练习栏目标题孤悬栏底（`B AS PALAVRAS DO TEXTO` 等）：KIT 已记的核心流行为，不记缺陷。
6. P1 词数 8,589 vs KIT 8,561：计数方法差，多重集差 0（PROOF-NOTE O5）。
7. 直引号 `'vallen op een dag'`：与 pt-en 版共用写法（PROOF-NOTE O1），不记本版缺陷。
8. Q150 印刷键 `✓` vs text.md `✓ Zie de modeltekst…`：同一结论的不同形式（标记 vs 指向句），不记 mismatch。
9. `VOL.3` 两现：均在 P7 承诺引述内，gates 允许。不记残留。
10. P7 金句区与预告框：末行基线 2351.17，距预告框顶 2404 约 48px（含墨迹余量），gates 通过，目视通过。

## §11 未改动声明

复校全程只读版源文件；未改动、未重建、未 commit、未 push 任何版文件。
`git status --porcelain` 显示版目录仍为未追踪新目录（复校前即然）；freeze baseline 在 scratch 副本内重跑，
并校验 shipped SVG 前后哈希未变（`core integrity: shipped core SVGs unchanged`）。
本目录新增文件：`PROOF-NOTE.md`、`GATE-LOG.md`、`keycheck-150.json`、`build_keycheck.py`、
`textmd-answers.json`、各门日志/JSON（`gates-proof1.log`、`occlusion-proof1.log/json`、
`p8-extract-proof1.log/json`、`p8-compare-proof1.log/json`、`freeze-baseline-proof1.log`、
`freeze-diff-proof1.log/json`、`creambox-proof1.log`、`creambox-core-pt.log`）、
裁图与整版图（`crop-*.png`、`page-p*.png`）、`print.txt`、`web.txt`、`probe.txt`。
