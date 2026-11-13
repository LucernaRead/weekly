# PROOF-NOTE — W47 es-it 独立复校 (proof1)

- **版**：2026-W47 es-it（西班牙语正文 + 意大利语讲解）
- **复校员**：独立复校员（与建版者非同一人），SOP §8.4 全量复校
- **对象（已核 SHA，见 GATE-LOG.md）**：`production/2026-w47/2026-w47-es-it/`
  - 印刷 `La-Lucerna-VOL4-es-it.pdf` 3,498,408 B，SHA-256 `d4eaaf2fd3f955c17140f3a648ccfef538fa21564a5dde28f71e5da1ee96a2a7`
  - 网页 `La-Lucerna-VOL4-es-it-web.pdf` 845,673 B，SHA-256 `24bd25008151e3dd14d7e2d8769aa541781bd9dc3ffc2a0006aca5ba4e70a435`
  - `2026-w47-es-it.text.md` 44,644 B / 1,788 行，SHA-256 `a2c3606482b56d17fd191b5998c76307fb4e696e4b1a5225ea498586e01e5181`
- **核心**：core-es 已定稿；以下缺陷凡根在核心的，均只记为核心级候选，未碰核心。
- **复校范围**：text.md 全文通读；150 题逐题核对答案键；8 页印版全目视 + 网页版 P1/P8 渲染目视；外部事实逐项核实；弯引号/撇号；禁词；印/网文字层同一；全部机械门。

## 结论：(b) 缺陷清单 — 共 4 项，均为轻微（minor）/装饰性（cosmetic），无 blocking 缺陷

本轮未发现影响理解、答案正确性或版面完整性的严重缺陷。4 项中 3 项根在核心（C1–C3，同样的几何/文字在 core-es 里逐字存在，另 es-fr 版亦有同样的 C1 数值），须协调员裁定是否在核心层修；1 项为本版讲解层装饰性不一致（E1）。

---

### C1（核心级，轻微·视觉）— P1 CINCO CLAVES 工具盒：意大利语 gloss 行落在奶油盒底之外

- **定位**：`svg/p1-portada.svg`，奶油盒 `x=1439.5 y=588 w=422.5 h=700`，盒底 `y=1288.0`；
  文本行 `«Cinque chiavi, zero numeri inventati.»`（fs 19），基线 `y=1300.0`，即基线在盒底之下 12 px（creambox clearance **−12.0**）。
- **目视证据**：`crop-p1-cincoclaves-bottom.png`（本 scratch 目录）— 该行印在盒底之外的白纸上，与盒内末行 `en esta edición.`（基线 1266）脱开，下方紧接下一栏目标题，观感为盒内文字漫出盒底。
- **根在核心**：core-es 同一盒、同一坐标，中文 gloss 行 `五大看点，不编数字：全在本期里讲清。` 同在基线 1300.0（实测）；es-fr 版同位置亦为 −12.0。此为核心几何，非 fan-out 引入。
- **严重度**：轻微。文字完整可读、无重叠遮挡（occlusion 审计 0 flags）；仅一行 gloss 脱离色块，视觉不洁。
- **建议**：协调员裁定——核心层把该盒加高 ≥12 px（或把 gloss 行并回盒内），12 个 fan-out 版随核心重渲。

### C2（核心级，轻微·措辞）— 邮寄投票截止日写成“antes del jueves 19”，与“hasta el 19”自相矛盾

- **定位**：P1 正文 `Tiene que pedirlo antes del jueves 19`、P1 题 3 与 P2 题 12 题干 `El voto por correo se pide antes del jueves ___ de noviembre`、P8 题 116 `se pide antes del ___`、P1 图注 `cómo pedir el voto por correo antes del jueves 19`。
- **事实**：经核实（Correos 官方通告 2026-11-10、JEC 日历、La Moncloa 指南），申请截止日为 **11 月 19 日周四（含当天）**，文件自 11 月 9 日起寄出。严格读法 `antes del jueves 19` = 19 日之前（即不含 19 日），与截止日差一天。
- **自相矛盾**：同版他处用的是正确说法——P2 正文 `El voto por correo se pide hasta el jueves 19`、P5 正文 `hasta el jueves 19 de noviembre`、P8 题 123 `se pide hasta... A. jueves 19`。
- **根在核心**：core-es text.md 第 51/123/169/364 行逐字同款（`antes del jueves`）。答案键本身（19）无误，不影响判题。
- **严重度**：轻微。口语中 `antes del jueves 19` 常被宽松理解为“19 日之前办好”，读者大概率按 19 日理解；但与版内 `hasta` 并存即为措辞不一致。
- **建议**：协调员裁定——核心层把 5 处 `antes del jueves 19` 统一为 `hasta el jueves 19`（题干与答案 19 不变）。

### C3（核心级，轻微·练习设计）— P5 B 组词框：两词未用、两答案不在框内，与题干说明不符

- **定位**：P5 `B PALABRAS DEL TEXTO`，词框 `sobre · papeleta · censo · identidad · plazo · urna`，题 70–75。
- **实测**：答案 70 `correo`、72 `envío` 不在词框内（72 题干自带 `(infinito: enviar)`，71 `papeleta`、73 `identidad`、74 `censo`、75 `plazo` 在框内）；词框内 `sobre`、`urna` 全卷无题使用。
- **题干说明**：`Completa con le parole del riquadro.`（用框内词完成）——与实际 2/6 答案在框外不符。
- **根在核心**：core-es 同一词框、同一题干（core text.md 第 952 行词框、第 880 行题 70），西班牙语题面冻结未动。
- **严重度**：轻微。6 个答案全部正确且无歧义（70 只能是 correo；72 由题干给出的不定式 enviar 变位得 envío）；仅是指令与词框的对应不严密，多余两词可作干扰项。
- **建议**：协调员裁定是否接受现状（干扰项是常见设计）或在核心层调整词框/说明。

### E1（本版讲解层，装饰性）— P2 C 组引言用了弯撇号 ’，全版其余 27 处意大利语省音撇号均为直撇号 '

- **定位**：`svg/p2-vida.svg`，C 组引言 `Leggi l’articolo e scegli la risposta giusta.`（U+2019）。
- **实测**：全版 8 个 SVG 中意大利语省音撇号共 28 处：直撇号 ASCII `'` 27 处（P1 `L'EDIZIONE`、P3/P4/P5 组引言 `l'articolo`、P7 `L'una`/`l'indicativo`、P8 答案注 `l'originale`、`d'errore`、`Quest'anno` 等），弯撇号 ’ 仅此 1 处。
- **对照**：同族 es-fr、es-en 的讲解层亦全用直撇号（es-fr 56 直 / 0 弯；es-en 8 直 / 0 弯），故本版 1 处弯撇号是孤例。
- **严重度**：装饰性。渲染时字形略有差异，正常阅读距离难以察觉；不影响任何内容。
- **建议**：本版可直接把该处 ’ 改为 '（与全版一致），改后按 SOP 重渲 + 从头再校一轮（如协调员接受现状不改，亦请书面记录）。

---

## 已核实无误的要点（抽样之外的全量结论）

- **150 题答案键逐题核对**：1–150 全部与题干/原文/图表一致。含：P1 1–10、P2 11–28（含配对 25–28：debate=c、mitin=b、cartel=d、escaño=a）、P3 29–46（含 35 `baile`、43–46 造句）、P4 47–64（含配对 52–55：jornada=c、derbi=b、liderato=a、fase liga=d；56 `más importante`、57 `muchísimos`、58 `peor`、59 `mejor`；60–64 过去时变位）、P5 65–82（含 70–75、76–79 ir a + 不定式、80–82 正误）、P6 83–100（含图表题 83–88：RTVE 分钟数 45/45/30/30/15、总和 195；89–92 阅读；93–96 虚拟式/让步；97–100 词框）、P7 101–112（时间/比较级/虚拟式）、P8 113–150（含配对 141–144：sondeo=c、muestra=d、margen de error=b、junta electoral=a；137/138 翻译题见下；150 写作范文 97 词，逐词数过，80–100 词范围内）。
- **keydiff [137, 138]（已说明，非缺陷）**：翻译题 137/138 题干为西班牙语句、答案须为意大利语句。核心版（中文读者）该两键为中文译句；本版键为 `137. Lunedì è la Giornata internazionale del flamenco.` / `138. Sabato guardiamo il derby di Siviglia.`，与题干 `El lunes es el Día del Flamenco.` / `El sábado vemos el derbi Sevilla–Betis.` 逐句对应正确，符合 W45/W46 ES×EN 裁定（译入题的键用读者语）。其余 148 键与核心逐字节一致（p8 compare CLEAN）。
- **P7 金句 8/8**：8 句均逐字出自本期正文，意大利语 gloss 准确，页码标注（P1/P2/P3/P4/P5/P6）全部与出处页相符；另核对：P1 词条、P7 词条、读者来信示例及“承诺顺延至 VOL.5”的编辑注均与核心一致，无编造来信。
- **外部事实逐项核实**（2026-11-11 公开网络复核）：
  - 大选 29-N：Real Decreto 806/2026，11 月 29 日周日投票 9:00–20:00；竞选 11 月 13 日周五 00:00 至 27 日周五 24:00（15 天）；28 日静默日；11 月 16 日→29 日为 13 天。La Moncloa 官方指南、BOE 均证实。
  - 邮寄投票：申请截至 11 月 19 日周四（含）、Correos 柜台或网上；文件自 11 月 9 日起寄出；寄回截至 11 月 25 日。Correos 官方通告证实（本版未写寄回截止日，无错误表述）。
  - 辩论（doblelectura.es 指南，数据截至 11 月 10 日）：唯一已确定的辩论确为 laSexta 发言人辩论 11 月 13 日周五 21:30，Ana Pastor 主持，Cuerpo（PSOE）/ Bravo（PP）/ Bustinduy（Frente Amplio）/ Figaredo（Vox）； cara a cara 11 月 16 日为 PP 提议、PSOE 截至 11 月 10 日未确认；SER 住房辩论 11 月 18 日周三 Rodríguez–Bravo；Atresmedia 四人辩论 11 月 23 日周一、无 PSOE 确认；PP 四人辩论提议 11 月 26 日周四、无 pactada 日期。均与本版 P1/P2/P6 一致。注：指南称 13 日场主题为“vivienda y economía”，本版写作“economía”——核心 KIT §5 已记录该来源冲突并裁定以 diariodesantiago.es 的逐场区分（13 日经济/18 日住房）为准，不属新发现。
  - 民调禁发 11 月 24–28 日（投票前 5 天，LOREG 口径）✓；投票站 9:00–20:00 ✓。
  - MiDNI：JEC 于 11 月 5 日解除停用（多家 11 月 6–7 日报道；核心 KIT 写的决议号 334/342 与个别报道写的 330/359 有出入，但本版正文未写决议号，只写“11 月 5 日解除停用”，无误）。
  - 西甲第 13 轮（11 月 20–23 日）：Athletic–Espanyol 周五 21:00；Sevilla–Betis 周六 18:30；Real Madrid–Celta 周六 21:00；Barcelona–Villarreal 周日 14:00；Getafe–Atlético 周日 21:00；Levante–Elche 周一 21:00——六场时间经 LaLiga 赛程/DAZN/多家媒体逐场证实；积分榜 Barça 33 / Madrid 30 / Atlético 28，Barça 客场 1–2 胜 Atlético（11 月 8 日）证实。
  - 欧冠第 5 轮（11 月 24–25 日）：Real Madrid–PSV 周二 21:00；Sabah–Barça 周三 18:45；Atlético–Viking 周三 21:00；Villarreal（Slavia 客场 18:45）与 Betis（Slovan 客场周二 21:00）亦赛。J4：Barça 3–0 Aston Villa、Madrid 3–2 AEK、Atlético 0–2 Bayern 证实。
  - 弗拉门戈：2010 年 11 月 16 日内罗毕 UNESCO 列入非物质文化遗产、国际弗拉门戈日 11 月 16 日、安达卢西亚起源、cante/toque/baile 证实；Santa Cecilia 11 月 22 日周日、音乐守护神 ✓；毕尔巴鄂市立乐队 11 月 22 日 12:00 Euskalduna 音乐厅（teoriamusical.com.es）证实；Black Friday 11 月 27 日周五 ✓。
  - Sargent 图：内嵌 JPEG 的 EXIF 题名确为 `Sargent, John Singer - Spanish Dancer`；图面为持披巾的舞者，与图注“una bailaora con su mantón”相符；年份“1880–81”未独立锁定到年（相关研究称该习作为 1879–82 年间《El jaleo》主角习作），无矛盾证据，不列为缺陷。
  - RTVE 免费时段 45/45/30/30/15 + 3×10 = 195 分钟：算术自洽，分档与 LOREG 第 64 条口径相符；本次独立检索未找到逐项核对的第二来源（核心 KIT 引用 queproponen.es），无矛盾证据，不列为缺陷。
  - 全部日期与星期经 `date`（Europe/Madrid）逐项校验：11 月 9 日周一、10 日周二、13 日周五、16 日周一、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、25 日周三、26 日周四、27 日周五、28 日周六、29 日周日，全部吻合。
- **跨页引用**：P1→P3/P4/P5/P6、P2→P3/P4/P5/P7、P3→P6、P5→P6、P6→P5 的页码引用全部与对应内容所在页相符；目录（EN ESTA EDICIÓN）8 行页码与级别与各版一致。
- **弯引号**：全版 «/» 各 56 处（逐页 2/2、10/10、2/2、0/0、1/1、3/3、31/31、7/7），全部成对；直引号 0。撇号见 E1。
- **禁词**：text.md 中 CJK 0 字符；SOP/proofread/cover/“12 de noviembre”/桥接 0；VOL.4 印刷层 9 次 + 刊头 `VOL. 4` 1 次，VOL.5 3 次均为合法的下期预告（P7 编辑注、P7 金句栏后横幅）。
- **印/网同一**：pdftotext 均为 45,642 字节且逐字节一致；网页版 P1/P8 渲染与印版目视一致，无豆腐块、无缺字。
- **意语层**：全文通读，拼写/变位/性数配合无误；讲解层只用意大利语，无中文残留（freeze 差分：新增串全部为意大利语，无 CJK 字符，唯一的新增 CJK 码点为全角空格 U+3000，即 SOP §1.1 规定的分隔符）。

## 机械门结果（详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| SHA 核对（KIT §7 + 盘上 sha256sum） | 3 件全符（完整 SHA 见 GATE-LOG） |
| 页数 | 印/网各 8 页，1462.5 × 2025 pt |
| occlusion 审计 | 0 flags（自检六类全触发） |
| p8 extract | 150/150 |
| p8 compare（vs core） | CLEAN，missing=[] extra=0，keydiff=[137, 138]（已说明） |
| freeze baseline（重建） | 8/8 SVG 逐字节一致， shipped SVG 未被改动 |
| freeze diff | 西语内容零丢失；新增仅意大利语层 |
| creambox 全版扫查 | P7 工具盒 3 盒余量 +42.5 / +26.5 / +5.7；全版另 5 处负余量经裁图核实为假阳性（次栏目标题/图注在盒外下方），仅 C1 为真 |
| P8 最小字号 | 10.125 pt ≥ SOP §1.1 下限 9.75 pt |
| boxtitle 宽度 | occlusion BOXTITLE 类 0 flags |
| 印/网文字层 | 45,642 B，逐字节一致 |

## 复校员说明

- 本版除上述 4 项轻微问题外，其余全部通过。是否定稿由协调员裁定：若接受 C1–C3 留待核心层后续处理、E1 接受现状或随核心重渲一并改，则本版可按协调员书面决定定稿；否则按 SOP §8.4，改源码 → 整期重渲染 → 从头再做一轮全量校对。
- 本复校未改任何源文件、未重建、未 commit、未 push、未动 tools/。全部工作文件在 `hidden_files/w47/scratch-proof-es-it1/`。
