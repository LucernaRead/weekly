# W47 pt 核心版独立校对笔记（叶子，2026-11-10）

对象：`production/2026-w47/core-pt/`（2026-w47-pt-zh-cn，VOL.4，刊期 2026-11-16..22）
结论：**(b) 缺陷清单 — 1 项硬缺陷，不算定稿**（另有 3 项次要观察，不阻塞但建议随硬缺陷一并改）。

## 硬缺陷

### D1. 同一场比赛在 P1 与 P3 印了两个不同的开球时间（P1 错）
- **位置**：P1 右栏「A SEMANA, DIA A DIA」：`Ter 17 — Singapura × Brasil, às 7h15, amistoso da Seleção.`（渲染图 pg-1.png 目视确认；`.text.md` 第 44 行）
- **对照**：P3 右栏「A SEMANA, DIA A DIA」：`Ter 17 — Singapura × Brasil, às 7h.`（渲染图 pg-3.png 目视确认；`.text.md` 第 167 行）
- **事实**：CBF 官方通稿（cbf.com.br，2026-10-29 征召公告）：“A Amarelinha enfrentará o Japão no dia 14 de novembro, às 7h15 (de Brasília), e no dia 17, às 7h (de Brasília), jogará contra Singapura. As duas partidas serão realizadas no Estádio Nacional de Singapura”。多家媒体一致：sportbuzz / fatofluminense / bolavip / portaldasradios 均写 11 月 17 日 7h。**11 月 14 日对日本是 7h15，11 月 17 日对新加坡是 7h**——builder 把两场的时间混为一谈。
- **根源**：KIT §2 写“11 月 17 日 7h15 新加坡 × 巴西”；KIT §6 修复 7 称把 Ter 17 从“às 7h”改成“às 7h15”“与已核实 7h15 开球一致”——该“核实”本身是错的，且只改了 P1，没改 P3，于是同一期出现两个时间，P1 的是错的。
- **修复方向**：P1 改为 `às 7h`（与 P3 一致、与 CBF 一致）；KIT §2 与修复记录同步更正。按 SOP §8，改源码后须整期重渲染并从头再做一轮全量校对。

## 次要观察（不阻塞，建议随 D1 一并处理）

- **O1. P6 时间线漏写 Linguagens**：P6 右栏「O CAMINHO ATÉ O GABARITO」写 `8 NOV. Primeiro dia do Enem: redação e Humanas.`，漏了 Linguagens；同版正文写全了（redação, Linguagens e Ciências Humanas）。时间线是摘要，可接受但不完整。
- **O2. P1 鲁格拉斯图注年份约数**：P1 图注“por volta de 1830”。该版画出自 Rugendas《Voyage pittoresque dans le Brésil》（巴黎，1835 年出版），原稿画于 1822–25 年巴西之行。“约 1830”在约数容差边缘，建议改为“约 1835 年出版”或“19 世纪 20 年代”。画家 1802–1858，公版身份不受影响。
- **O3. P5 配图 CC0 未由我现场复核**：P5 Gary Todd 图（Sias 图书馆自习）本地 md5 `04b18fa952a61c9998ef5bf3325341f2` 与 KIT 所称源文件 md5 一致；Gary Todd 确为 Sias 大学任教的美籍教授、其 Commons 上传均引自其 Flickr；但本次未现场打开该图 Commons 授权页复核 CC0（无相反证据）。

## 已通过的检查（逐项）

1. **全文精读**（print PDF `-layout` 提取全文 866 行 + 8 页渲染图逐页目视）：葡语拼写/重音/性数/变位/标点未见错误；中文讲解层逐项对照正文；目录页码与级别徽章与各版一致（P1 目录：P2 A2 / P3 A2→B1 / P4 B1 / P5 B1 / P6 B2 / P7 A2→B2 / P8 todos；各版刊头一致）。
2. **150 题逐题复核**：题号 1–150 连续无缺重（`.text.md` 与 P8 提取双重确认）；答案逐题对题面/原文/图表验算——P1 1–10、P2 11–28、P3 29–46、P4 47–64、P5 65–82、P6 83–100、P7 101–112、P8 113–150 全部正确（含易错点：Q56–59 比较级 mais/menos、Q58 16h30 mais cedo、Q91 周末假日不计工作日、Q100 chute、Q108 saíram、Q112 sair、Q125 周六 21 日、Q127 数字 10 指工作日、Q141–144 配对、Q145 Mané、Q146 sexto、Q147 quinto、Q148 na、Q149 obrigado）。范文实测 88 词（80–100 区间内）。
3. **几何审计**：`tools/occlusion_audit.py` 自检通过（6 类植入均触发、干净对照静默），当前 SVG **0 flags**。
4. **P8 答案集合**：`tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150` → **150/150**（1–150 全集）。
5. **Freeze 复现**：`tools/freeze.py baseline` 工具自报 0/8（工具重定向局限：副本写进 `build-copy/svg/` 而非 `--out/svg/`，与 KIT 所述一致）；直接 `sha256sum` 比对副本与交付 SVG：**8/8 一致**；工具自检“shipped core SVGs unchanged”。
6. **P1 头条**：`Consciência Negra: sexta é feriado em todo o país` 去空白 41 字符 ≤ cover.mjs LIMITS.headline other=56 ✓。
7. **金句**：8 条在 `.text.md` 全文各恰好出现 2 次，逐字出自本期正文（P1/P1/P3/P3/P4/P5/P6/P2），页码标签正确。
8. **注释对照**：29 个译注词头全部真实出现在印刷文本中（脚本核查 29/29）。
9. **正文完整度**：`.text.md` 中全部纯散文长句（≥40 字符）在 SVG 文本中 token 子序列 0 缺失；137 个可解析题干齐全（另 13 条造句/翻译按惯例在 → 后填答案）。
10. **P8 答案字号独立实测**：SVG 答案字号 13.5 单位（733 处）× 页面缩放 0.75（1950×2700 单位 → 1462.5×2025 pt）= **10.125pt**；pdftotext `-bbox` 实测 P8 答案区词框高 10.12pt；300dpi 渲染答案行距 11.19pt。≥ SOP §1.1 下限 9.75pt，与 KIT 所称 10.1pt 一致。pdftohtml 报的 15.0 是内嵌字体名义字号（未计页面缩放），不作渲染字号。
11. **文字层一致性**：print/web 各 8 页；pdftotext（无 -layout）44,436 vs 44,441 字节，与 KIT 所述完全一致；**词级多重集 diff = 0（完全相同）**；5 字节差 = web 版多 5 个空行（1026 vs 1021），源于刊头行 `VOL.4 CONSCIÊNCIA NEGRA GABARITO DO ENEM A FINAL DA COPA` 与 P2 日程盒在 web 版被拆成多个文本对象——**提取引擎 artifact，无真实内容差异**，门槛通过（文字层 >0 且与 print 版实质一致）。web PDF 1,571,215 字节 < 7MB ✓。
12. **ABSTRACT.txt**：单行、无 ASCII 双引号、简体中文、含 VOL.4 / 150 道 / 本期真实关键词（黑人意识日、祖比、巴西杯决赛格雷米奥×帕尔梅拉斯 12 月 6 日、Enem）✓。注：摘要行尾一个换行符，计 1 行。
13. **图片**：5 幅均有目标语图说 + 出处；CREDITS.md 全表；capoeira（Rugendas，PD）、zumbi（Parreiras 1927，PD）、estudo（Gary Todd，CC0，见 O3）、lusiadas（1572 初版扉页，PD）、garrincha（Luis Dantas，PD）。8 页渲染图逐页目视：无溢出/重叠/压页脚；P3、P5、P6 中部有大面积留白（版式疏朗，非 SOP 违规）。
14. **事实核查（逐项已验）**：
    - 巴西杯：Atlético-MG 1–1 Grêmio（11 月 7 日，Arena MRV；Renan Lodi 25'/26'、Carlos Vinícius 37'/38'，Vitão 下半场红牌；首回合 Grêmio 2–0；总比分 3–1；格雷米奥第 10 次进决赛、争第 6 冠，冠军年份 1989/1994/1997/2001/2016）✓；Vasco 2–1 Palmeiras（11 月 8 日，São Januário；总比分 2–2，点球 5–4；首回合 Palmeiras 1–0；帕尔梅拉斯争第 5 冠，1998/2012/2015/2020）✓；决赛 12 月 6 日周日单场、马内·加林查、史上首次单场决赛 ✓。
    - 黑人意识日：Zumbi 1695 年 11 月 20 日去世、帕尔马雷斯（今阿拉戈斯 Serra da Barriga）、Lei 12.519/2011 设纪念日、Lei 14.759（2023 年 12 月 21 日签署）定全国假日自 2024 年起、Portaria MGI 11.460/2025 列入 2026 假日表、2026 年 11 月 20 日周五、连休 20–22 日 ✓；Parreiras《Zumbi》1927 年 ✓。
    - Enem：Edital nº 64/2026（2026 年 5 月 21 日）第 15.1 条“até o 10º dia útil”✓；窗口 27–30 日（是否计 20 日假日之差；多家独立信源同为 27–30 日窗口，不计假日则 30 日）✓；第二天 11 月 15 日周日、自然科学 45 + 数学 45 = 90 题、13h30–18h30、5 小时；第一天 11 月 8 日、redação + Linguagens + Humanas、13h30–19h；两日均为 12h 开门、13h 关门；确认报名 5,051,345 人（MEC；纸面只写“Mais de 5 milhões”，无冲突）；个人成绩 2027 年 1 月；TRI 答对数 ≠ 分数 ✓。
    - F1 圣保罗大奖赛 11 月 8 日：Norris（McLaren）杆位夺冠、Verstappen 第 21 位发车获第二、Hadjar 第三、Russell 第四、Antonelli 第五、71 圈、梅赛德斯锁定车队冠军 ✓。
    - 国家队：11 月 14 日日本 × 巴西 7h15、11 月 17 日新加坡 × 巴西 **7h**（见 D1）、均在新加坡国家体育场、Ancelotti 征召 26 人、2026 年最后两场 ✓（除 D1 外）。
    - 巴甲：35 轮 11 月 18 日 Cruzeiro × Palmeiras 20h30、Flamengo × Athletico-PR 20h30；11 月 19 日 Vasco × Internacional 19h30、São Paulo × Fluminense 21h30；36 轮 11 月 21 日 Palmeiras × Flamengo 16h30（Nubank Parque）✓；日期星期经 `date` 核验：11 月 7 日周六、8 日周日、14 日周六、15 日周日、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、27 日周五、30 日周一、12 月 6 日周日 ✓。
    - 下期预告与 W46 承诺兑现：巴西杯次回合赛果+决赛队（P4）、黑人意识日 11 月 20 日周五头条（P1）、Enem gabaritos（P5+P6）✓；读者来信：无真实来信，P7 刊编辑部示例 + 葡/中双语披露、承诺顺延 VOL.5，标注清晰、无编造读者 ✓。

## 未改动声明
只读校对：未修改 core-pt 内任何文件；未跑 insert.py / lint --write / git 操作；未碰 W43/W45/W46。校对产物仅本笔记与 scratch-proof-pt/ 下的提取文本、渲染图、freeze 副本、工具输出。
