# COVER-REPORT 底稿（W47 网站封面）

> 本文件为底稿，存于 scratch；定稿由父协调员汇总后入仓。本次只写“页号核实”一节。

## 页号核实（2026-11-13，封面页号核实员）

- 范围：`production/covers/2026-w47/cover.json` 全部页号字段——12 目标语 ×（more[0..5].page 6 个 + word.page 1 个）= **84 项**。头条（第 1 版）与导读（第 i 行 = 第 i+2 版）按 SOP 附则五 §6a 不用写，不在内。
- 方法：逐项打开对应核心 PDF（`production/2026-w47/core-<target>/` 非 web 版，8 页）核对。先逐页抽页脚 `第N版／共8版`：12 份核心 PDF 的 PDF 页序与页脚版号全部一致（1–8）。more 标题用去空白+大小写折叠全文匹配，删词缩短标题用词序子序列匹配，多页匹配项逐页看上下文区分正文标题与 P1 目录提及 / P8 练习·答案提及；word 先定位 P1「Word of the Week」框核对框内词。
- 结果：**84 项全部一致，不符 0 项。**more 72 项：文章实际所在版 = cover.json 值（所谓“机械填入 [2,3,4,5,6,7]”的怀疑不成立——more 本就按核心报版序填，P2–P7 与文章版序吻合）。word 12 项：11 项为 P1 框词、页 1；de 为 P6 词语讲解文、页 6。
- cover.json 页号改动：**0 处**。封面块：scratch 复核重生成 12 块与已提交块逐字节一致；原目录跑 `node tools/cover.mjs 2026-w47` 退出 0、0 problems，cover.json 与 12 块在 git 中无改动（工作树里另有 9 张图片被并行图片工作改动，与本次无关、未碰）。
- 逐项明细：见同目录 `PAGE-AUDIT.md`（84 行表：目标语 / 项目 / 标题·词 / cover.json 值 / 实测值 / 结论 / 证据）。
- ⚠️ 上报 1 项内容问题（不属页号，不改）：de `word.term` = Totensonntag，但 de 核心 P1「DAS WORT DER WOCHE」框内词是 der Adventskalender；P6 深读文〈Eine stille Woche: Was bedeuten Buß- und Bettag und Totensonntag?〉即 Totensonntag 的词语讲解，gloss 与之相符。若词保持 Totensonntag，页号 6 正确；若词应为框词 der Adventskalender，则 term 与 page（→1）须一起改——改 term 属内容决定，超出本次只改页号的授权，请父协调员定夺。
