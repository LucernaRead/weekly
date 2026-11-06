# 独立校对报告 — W45 ES×IT（西班牙语×意大利语）

## 结论：ZERO PROBLEMS，可定稿

待校版本 `files/weekly-report-w45-es-it/`（svg ×8、cards ×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
经 SOP §8 全量独立验证，**零问题**。纸面检查与 KIT 一致性双双通过，无编号问题清单。
本校对只读待校版本与对照版本，未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰
weekly-git；全部写盘只在校对目录内。

## 开工查重

- 开工时（18:28 UTC）待校目录最新写盘为 18:11（WEEKLY-KIT.md），构建树最新写盘 18:08；
  无进行中的渲染进程（仅一个无关的 ko 推送进程）。
- 90 秒复查零新写盘后开工，符合协调员裁定（已完成交付、无并发写盘者）。

## 逐项验证（12 项全部通过）

1. **基线**：`tools/freeze.py baseline` 在核心构建树上重跑，**8/8 逐字节相同**
   （p1 a1b30102…、p2 10e78c2e…、p3 5986ba9e…、p4 1894836e…、p5 cd15c68b…、
   p6 fcfccf82…、p7 b1774024…、p8 d1c46fa4…，与任务书基线逐字一致）；
   事后核心重哈希无变化；校对结束时核心哈希再次核对无变化。
2. **freeze diff（--strict-cjk）**：8 页 added CJK 均为 0，本版 CJK 均为 0
   （核心 CJK 170/280/161/169/247/80/388/981 → 本版 0）。
   独立 token 存活分析：每页被删字符串中的拉丁词元，**除页脚英文 SPANISH、WEEKLY
   外全部在本版同页存活**——与 builder 声称的“唯一未存活删除词元”逐字一致。
   源码树对照（核心构建树 vs 本版构建树）：仅 bslib4.py、content12/34/56/7/8.py、
   render.py 有改动（+ pycache）；340 行旧改动中 318 行含中文讲解层，22 行无中文行
   全部是备案项——5 处 OUT 重定向、render 路径/文件名、P8 字号/行距、P6 间距 3→1
   （题干逐字相同）、P7 信件全角括号→半角括号。**零未备案西语改动**。
   svglib.py 逐字节相同。
3. **P8**：`tools/p8.py compare` **CLEAN，150=150，missing=[]，extra=0**，
   keydiff [83, 85, 95, 96, 98, 107, 117, 137, 138, 148] 与任务书一致。
   独立 dash-parse（首破折号切分，不依赖工具提取）复核：8 项（83:A、85:C、
   95:para que、96:Aunque、98:muestra、107:mejor、117:A、148:A）印出键逐字节相同，
   且意语注尾恰为 ASCII 括号组 (34%)、(55,7%)、(scopo)、(fatto noto)、(5.025 persone)、
   (senza más)、(il Bernabéu ospita la NFL)、(il contratto)——确为工具提取 artifact；
   真改动仅 137（`Il lunedì è festivo in nove comunità.`，注 `confronta con l'originale`）、
   138（`La domenica vediamo la NFL e l'Atlético–Barça.`，同注），符合 W43 意大利版
   KIT §3 同配对翻译重瞄准先例；139/140 西班牙语键逐字节相同
   （`El Bernabéu acoge un partido de la NFL.` / `Cada gráfico tiene que llevar su fuente.`）；
   150 范文行 `150. ✓ Il modello è nella sezione H di questa pagina (84 parole)`，
   范文体实测恰 84 词（空白切分计数，文本已在 P8 印出）。
4. **遮挡审计**：`occlusion_audit.py --selftest` 通过（6 类各触发 1 次，干净对照静默）；
   本版 **0 flags**，`--core` 对比 **NEW flags = 0**，核心对照 0 flags。
   同基线墨迹扫描：本版 7 hits 与核心对照 7 hits 集合相同，均为 P1 目录行 +4.0px
   正间隙，无重叠，无新增同基线缺陷。
5. **P6 图表**：全元素对照——除 14 个练习等级芯片（gap 3→1 的流量后果，y 位移
   -2/-4/-6/-8px）外，全部 rect 相同；图表区（y<1968）文字零差异。
   Inmigración 几何：标签 x=1011 y=1717、墨迹终点 1144.25、条形 x=1139（y=1699 行），
   与核心**逐值相同**，5.25px 压字为冻结核心缺陷（协调员裁定非阻塞），**不列为问题**。
6. **gloss**：按 `·` 本身拆分，核心 19 = 本版 19，分框 5/5/5/4（P2/P3/P4/P5）；
   19 个西语词头逐项相同；词头内容词均在非 gloss 正文源码中出现（≥1 次，多为多次），
   本版 SVG 合并文本中 19 项计数均 ≥1。注：不定式短语词头（如 recortar la distancia）
   在正文中以变位形式出现，与冻结核心完全一致，非本版缺陷。
7. **图片**：P3 栗子载荷 sha256 d6bc00b1…（627,056 字节）、P5 南瓜载荷
   sha256 331412bf…（461,668 字节），与核心逐字节相同，几何相同（x=1451 y=200）；
   图注冻结相同（P3 `Foto: Wikimedia Commons — CC0 (dominio público)`，
   P5 美国农业部来源行）；P1 无 raster 图、路径元素与核心多重集相等，房屋为核心
   代码绘制插图，未动。
8. **P7 金句与 150 题结构**：8 句西语原文裸句计数各恰 2 次，所在页与页签一致
   （Página 1/2/3/4/5/6/6/1 = 文章页 + P7）；独立复现渲染的 registry 统计：
   **A2 50 / B1 72 / B2 28，分页 10/18/18/18/18/18/12/38，总计 150**；
   最终构建 **零 FLOW OVERFLOW / 零 HEAD TOO WIDE**（复现日志实测）。
9. **家具三方比对（本版 vs W43 es-it 已发版 vs 核心）**：徽章字符串
   `TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`
   在 W43 与本版中 x=975 y=574、22pt 粗体、fill #a4553a 完全一致；
   y=372 西班牙语标语在三方均保留；页脚 `La Lucerna · SETTIMANALE SPAGNOLO VOL.2 ·
   TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO` + `Pagina N di 8`（8 页全对，
   相对 W43 仅 VOL.1→VOL.2）；gloss 前缀 `Nota — `（20.5pt）；
   P8 分隔符 `— PÁGINA N —`（14pt，N=1..8）；
   instr 映射与计数与 W43 逐字相同（Completa 42、Abbina le parole 3、
   Vero o falso 8、Costruisci 7、Riscrivi 10、Traduci 4、Scrivi 1）；
   栏头（y=116，7 个）与 W43 逐字相同；KIT §2 所列 22 条家具字符串全部在本版
   SVG 中原样出现。README #20 的 372/19.5pt 替换确为英文栏实例，不适用意栏。
10. **ABSTRACT.txt**：意大利语单行（371 字节，1 个换行结尾）、无 ASCII 双引号、
    无 CJK；含真实主题关键词（29 novembre 选举、casa/campagna、2 novembre 九
    社区 ponte、8 novembre NFL/Bernabéu/Atlético–Barça 21:00）+ 学习者搜索短语
    （`per imparare lo spagnolo con le notizie spagnole`）+ `A2–B2` + `150 esercizi`。
11. **读者园地**：Ana 示例信正文与核心逐字相同（仅署名括号全角→半角，W43 先例）；
    西班牙语披露冻结原文（三事实：无真实来信、无最佳 P8 作文、示例信 + 承诺顺延
    VOL.3）；意语注 `Nota della redazione: senza lettere vere né migliori testi di
    pagina 8, pubblichiamo questo esempio; la promessa passa al VOL.3. Scriveteci!`
    三事实 + 邀约齐全；无编造读者/信件/引言。
12. **PDF 与卡片**：两 PDF 均为 8 页；print 7,156,450 字节
    sha256 f975d8e6…、web 3,713,123 字节（<10 MB）sha256 839c5379…，与 KIT §7/§8
    实测一致；8 张卡片均为 1950×2700；8 卡逐张目视：无溢出、无遮挡、无页脚碰撞
    （P6 Inmigración 压字在卡片尺度下字形仍完整可读，且几何已证与核心相同）。

## 附加独立复现（超出任务书的加强证据）

- 已转换构建树复现：8/8 SVG 与交付版逐字节相同，零溢出。
- 端到端复现：核心构建树副本 + transform 脚本（仅重定向其 BUILD 路径的副本）
  + run.py → 8/8 SVG 与交付版逐字节相同，零溢出，transform 断言全部通过；
  残留 CJK 行仅为冻结 registry 的 `typ` 值（不渲染），与 KIT §1 一致。
- KIT 一致性：KIT §7 尺寸/哈希、§8 SVG 哈希与核心基线哈希，全部与实测逐字一致，
  **未发现 KIT 不一致**。

## 非问题说明（已裁定，不计入问题）

- P6 Inmigración 约 5px 条形压字：几何与核心逐值相同，属冻结核心缺陷，协调员已
  裁定非阻塞，本报告仅记录一致性，不列为问题。
- Gloss 不定式词头在正文中以变位形式出现：与冻结核心行为相同，非本版缺陷。

## 审计输出路径

校对目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-it-proof/`

- 本报告：`PROOF-REPORT.md`
- 基线：`freeze-baseline.txt`（8/8）、`core-hashes-before/after/final.txt`
- freeze diff：`freeze-diff.txt`、`freeze-diff.json`（与 builder 的 diff JSON 逐字节相同）、
  `freeze-diff-full.txt`、`diff-token-analysis.txt`、`analyze_diff.py`
- P8：`p8-compare.txt/json`（CLEAN）、`p8-dashparse.txt/json`、`p8_dashparse.py`、
  `p8-artifact8-full.txt`、`p8-extract-core/ed.json`、`modelo-wordcount.txt`（84 词）
- 遮挡：`occlusion-selftest/edition/corecmp/core.txt + json`、`rowcheck-ed/core.txt`（各 7 hits）
- 图表/图片/gloss/金句/家具/读者园地：`p6-chartcheck.txt`、`p6-inmigracion2.txt`、
  `images-check2.txt`、`credits-check.txt`、`p1-paths.txt`、`gloss-check/body/body2.txt`、
  `p7-quotes.txt`、`furniture-triple/rest.txt`、`reader-corner-full.txt`、
  `reader-corner-abstract.txt`
- 复现：`repro-log.txt`、`repro-hashes.txt`、`transform-log.txt`、`transform-run-log.txt`、
  `repro-svg/`、`transform-svg/`（各 8/8 与交付版相同）
- 源码对照：`sourcediff-full.txt`、`sourcediff-noncjk.txt`
- 交付物度量：`edition-hashes.txt/final.txt`、`pdf-hashes.txt`、`pdf-pages.txt`、
  `card-sizes.txt`

## 合规声明

- 未写入：`files/weekly-report-w45-es-core/`（哈希开工/结束一致）、
  `files/weekly-report-es-it/`（文件时间戳均为 2026-10-22，未动）、
  `files/weekly-report-w45-es-it/`（哈希开工/结束一致）。
- 未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git。
