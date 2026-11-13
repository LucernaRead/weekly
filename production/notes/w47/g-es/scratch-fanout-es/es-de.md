# 2026-w47-es-de — 工作记录

## 应用
- `apply_fanout.py de`：476 次字面替换；4 处 manual 覆盖 harvest（CULTURA/JUGEND/LEBEN 段名首字母大写非全大写；“Después ___ (Infinitiv: enviar)” 冒号）；leftover zh keys NONE；.py 内 CJK 残留 NONE。135 项 de-missing 事前核查：MANUAL+harvest+特殊处理（页脚/330 行/配对行）全覆盖，0 缺口。
- diff 审：仅讲解层字符串 + 配对行 + 330 行 spacing（11.5→4）改动；西文冻结；无新增 CJK 行。
- 预修（build1 前，先测 wrap 再动手，en 教训的德语版）：P1 gloss 缩为一行（„Debatte“: Menschen diskutieren öffentlich.，19 单位，1 行；忠实版 3 行）；P7 word-box gloss 4→2 行（debate = Debatte: eine öffentliche Diskussion; die Wahl ist am 29.；“mit Redeanteilen” 在上行西语词条里已有）、F-MAIL 德注 6→4 行 19 单位（Anmerkung der Redaktion: Keine echten Leserbriefe bis zum Redaktionsschluss; diese Ausgabe zeigt einen Beispielbrief. Das Versprechen gilt für VOL.5.）；P5 “Your turn” 5→3 行 19 单位；P8 RESPUESTAS 头移至 y=1337、keys 流起 1363（en 验证过的几何）；P6 band 补全（Den Wahlkampf lesen: Debatten, Programme und Umfragen，1025 单位）；来信括号改半角。

## 构建
- build1：run rc=0，TOTAL 150；P8-keys 溢出 7 处（终 y=2605）；P3 col3 1629.75（越 y=1608 线 21.75px）；P5 col3 1574.55；P7 col3 1865.51（预估，见 KIT §6.2）。
  - 原因：德语答案注释比中文多 21 条真换行（核心仅 2 条：#44、#139）。
  - 修复：收紧 18 条注释（content34 ×7：#29/#30/#31/#32/#33/#43/#45；content56 ×5：#68/#82/#88/#89/#92；content8 ×6：#136/#137/#138/#148/#149/#150），均用 wrap() 实测为 1 行；保留 #1（键冻结、无注释，无法收）、#44/#139（与核心一致的换行）。P3 “Your turn” 改为 3 行 19 单位（Hast du schon Flamenco gehört? … schick sie ein.；框底 1594.75）。
- build2：run rc=0，零 OVERFLOW / TOO WIDE；P8-keys 终 y=2506（余 54px）；TOTAL 150（A2 50 / B1 72 / B2 28；各页 10/18/18/18/18/18/12/38）。
- 渲染（build2）：render.py rc=0：print 3,503,448 B；web 852,618 B，文字层 45,898 字节。
- 机械门（build2）：p8 extract 150/150；compare CLEAN（keydiff [137, 138]，翻译题重定向，W46 先例已裁定——德语句为键）；freeze 直接 sha256 8/8；pdftotext print=web 45,898 B 逐字节一致；P8 最小字号 10.125pt；occlusion **0 flags**。bridge sweep（新写 `sweep_de.py`，同页/同 x/连续 y 链式匹配——共享行文本 “richtige Antwort.” 使首行匹配失效，另修复了 unicode_escape 解码 mojibake）发现 **P2 C 导语孤行**（与 en 同坐标：行 1 在第 2 栏底 538.5/2559.7，行 2 “richtige Antwort.” 孤悬第 3 栏顶 989/1924.5）+ **P5 B 引言孤行**（3 行 bridge：行 1–2 在第 1 栏底 88/2535.5、2565.2，行 3 “müssen konjugiert werden.” 孤悬第 2 栏顶 538.5/1696.5）。
- 修复（build2→build3）：P2 C 导语缩为一行（“Lies den Artikel und wähle die Antwort.”，20.5 单位 1 行）。
- build3：run rc=0，零 OVERFLOW；P8-keys 终 y=2506；渲染 rc=0：print 3,503,402 B，web 852,569 B；occlusion **0 flags**；p8 CLEAN；bridge sweep 剩 1 孤行（P5 B 引言）；box-vs-hline 0。目视 P1–P4。
- 修复（build3→build4）：P5 B 引言缩为两行（“Fülle die Lücken mit den Wörtern aus dem Kasten; konjugiere, wo nötig.”，20.5 单位 2 行，两指令都保留）。
- build4（终版）：run rc=0，零 OVERFLOW / TOO WIDE；TOTAL 150；P3 col3 1594.75，P5 col3 1574.55，P7 col3 1865.51，P8-keys 终 y=2506；渲染 rc=0：print 3,503,348 B，web 852,515 B；occlusion **0 flags**；p8 CLEAN；bridge sweep 0 孤行；box-vs-hline 全版干净；freeze 直接 sha256 8/8；pdftotext print=web 45,853 B 逐字节一致；P8 最小字号复测 10.125pt。
- §1.1 实测：纸 #fbfaf6 ×8 版；金/砖红/近黑 0；徽章三色齐；刊头 196 单位=147pt；VOL.4 ×9、VOL.5 ×3（皆为下期预告正当引用）；P8 徽章 35 枚与核心一致（A2 11 / B1 21 / B2 3），Q113–150 徽章无缺。P7 横幅墨底 ~2574，距页脚线 2596 有余量，审计 0 flags。
- 注释词逐词计数（核心 §8.1 口径）：各版 Note 词在当版全文 ≥2 次（P1 reflexión 2；P2 mitin/cartel/escaño 2；P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 6；P4 parón 2 / liderato 3；P5 papeleta 2 / censo 3 / plazo 3）。
- 全宽标点：.py 内 0，渲染 SVG 文本内 0；SVG 文本 CJK 仅蛾标元数据三色蛾（P1，继承自核心，不渲染）。
- .text.md：`2026-w47-es-de.text.md` 1,789 行（核心 extract_text2.py，仅改标题 slug，复制为 `extract_text_es_de.py`），全文逐行读完（德层逐行核对、西文冻结同核心）；1–150 题号齐全；CJK 0；无 “12 de noviembre”。
- 150 键逐题复核：REG 全表读完（`es-de-keys.txt`），键与核心一致（p8 CLEAN），德注准确；匹配题 25–28 / 52–55 / 141–144 逐字母核对正确。
- ABSTRACT.txt：德语一行、无 ASCII 双引号。
- WEEKLY-KIT.md：已写（规格、逐版内容、实测、来源沿用核心、裁定 §6、复现命令、4 轮自校记录）。
- **本轮自查结论：零问题。es-de 完成，待独立复校。**
- PDF 终版：print 3,503,348 B，SHA-256 `4919afbceb9b02a04cd00b281524b38545e3c3324443c052e0bc8e6a81354f19`；web 852,515 B，SHA-256 `69a3ae61e53784cdbe24c9cb56ec213dd85dcd8d55d7003c7abc6f107c51126d`。
