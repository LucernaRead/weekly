# de 版状态 — 配额再次断续阻塞（2026-11-11，#2）

## 时间线（UTC）
- 08:00 开工探针：小写 + 仓内 1MB 写盘均通过。
- 08:02–08:26 run/render/webpdf/export 全通；de 门禁初验全绿（见下）。
- 08:26–08:51 修 4 处缺陷，各重跑一次构建，均通。
- 08:52 1MB 探针失败（EDQUOT）；08:54 重探通过；08:57 连 2 字节写盘都失败；/tmp 写盘仍通。
- 结论：配额在 cap 上下抖动（16 线并发写盘），不是磁盘满（df 105G 已用 / 45G 空闲）。

## de 版当前精确状态：SVG 已定稿，PDF 待最后一轮重建
- run.py（run-de-7.log）RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；P7 teaser ends 2583.3。
- occlusion 0 flags（occlusion-de-5.log，自检 OK）；图片重叠扫描 0 处（scan-img-overlap.py）。
- SVG（svg/，07? 08:55 版）已含全部 5 处修复；cards/ 与双 PDF 仍是 08:51 旧件（P7 修复未渲染）。
- web PDF 盘上是 08:42 旧件（2,736,660 B，SHA a5caf2fb…）；.text.md 是 08:42 版（含旧 "Diese Woche im Kalender" 一句）。

## 恢复后待办（de 版，只剩收尾）
1. 重探（小写 + 1MB）通过后：render.py → webpdf.py → export_de.py。
2. 终验（同一批文件上）：freeze baseline 8/8、p8 compare CLEAN（P8 未变，06 版已 CLEAN）、
   print/web 字符多重集差 0、P8 最小字号 ≥9.75pt（前值 9.98）、U+2019 扫 0、泄漏重扫 0。
3. P8 目视（P1–P7 已目视通过，见 EDITION-RECORD 草稿下节）。
4. 写 WEEKLY-KIT.md + de/EDITION-RECORD.md，FANOUT-REPORT 记一行。

## 本棒修的 5 处缺陷（全在版内 content 文件 + 共享表）
1. P8 D-head 455.2px > 栏宽 422.5（会蹭到第 4 栏填空线）：content8.py 字号 24→22（417.3）。
2. P1 "Redaktionsschluss: 10. Nov. — das Finale noch nicht gespielt" 531px 冲出页边：
   content12.py 改为 "Redaktionsschluss: 10. Nov. — Finale offen"（373.2）。
3. P4 Hinweise 框 7 行过高盖住正文 "GEN，"：content34.py 删 ", die Halbfinalisten"（6 行，框底 792.2，同核心）。
4. P2 "Practice example　Übungsbeispiel"（英文留存、中文被译——全表 62 个拉丁首条目中唯一反向）：
   fresh.py 该条 9 语全改 "<X>　练习例子"，gen_tables.py 重跑（276 条 0 缺 0 余），
   content12.py 改为 "Übungsbeispiel　练习例子"（另：旧标题 392.1px 超框内宽 386.5，新标题 290.5）。
5. P2 日历框标题 "Diese Woche im Kalender" 468.9px 被右邻照片盖掉 36px（"der" 不可见）：
   content12.py 改为 "Kalender der Woche"（411.2，离照片 21px）。
6. P7 下期预告条：de 第 3 栏德文更长 → img_end 1889.3（核心 1840.7）→ 条底 2615.3 压住页脚线
   （2596）与页脚文字：content7.py 金句行距 120→112，条底 2583.3，页脚清。
   工具缺口（记下，未动手修，tools/ 不在权限内）：occlusion_audit 对 <image> 遮挡与
   rect 压页脚带不敏感——P2 照片盖标题（36px）与 P7 色条压页脚均 0 flags，全靠目视发现。
   另：occlusion 与 webpdf 各出现一次 RC=120 空日志瞬断，重跑即通（疑似配额抖动前兆）。

## 门禁实测（最后一批完整数据，08:42 件）
- run RC=0 TOTAL 150（A2 56/B1 69/B2 25，按版 10/18/18/18/18/18/12/38），0 溢出 0 警告。
- occlusion 0 flags；p8 extract 150/150、compare CLEAN、keydiff=[]。
  （任务原语 keydiff 预期 [137,138,139,140] 不适用：137–140 键是 7.77/14/GEN/冷，
  与核心逐字相同本就正确；E 组键是选项字母 A，注记已译成德文。）
- freeze baseline 8/8 字节一致；freeze diff：仅讲解层互换，新增 CJK 仅 1 字 "德"（P1 配对徽章 "德语讲解"，应有）。
- print/web 字符多重集差 0（23,752 字）；P8 最小字号 9.98pt（双 PDF）；U+2019 全扫 0；
  英文泄漏扫：仅 "Level A2/B1/B2"（W46 已发版同款保留）与已修的 Practice example。
- print PDF 44,831,669 B（08:51 件，SHA 未终验）；web PDF 2,736,660 B SHA a5caf2fb…（08:42 旧件）。
