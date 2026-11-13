# FIX-LOG — W47 core-zh-tw fix2：proof1（zh-tw-pt）D2 台北演唱会错放香港表

- **修复对象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（仅核心，不碰其他家庭、tools/、issues/）
- **缺陷**：zh-tw-pt proof1 D2（`scratch-proof-zh-tw-pt1/PROOF-NOTE.md` §D2）——P5 右栏「香港11月節目 Hong Kong」表末行 `BABYMONSTER台北演唱會：11月21、22日（台北小巨蛋）`，事实无误（BABYMONSTER《CHOOM》确于 11/21 19:30、11/22 18:00 在台北小巨蛋），错在归属：台北场不属香港表。
- **时间**：2026-11-11 09:06–09:2x UTC
- **日志目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-zh-tw2/`

## §0 探针（开工前 + 每次写盘前重探）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 每次 RC=0（`9daeafb9…`）。
- 探针写盘 `scratch-fix-core-zh-tw2/probe.txt` 成功；全程无 `Disk quota exceeded`。
- `df`：/home/hatch 72G 已用 / 78G 可用，无配额压力。

## §1 先查后动（全源 grep，动手前完成）

- `grep --include='*.py' "BABYMONSTER"` 全核心：仅 `content56.py:105` 一处。
- `grep --include='*.py' "台北演唱會"`：同上一处。
- `grep --include='*.py' "台北"`：其余命中全为封王游行（天母→台北大巨蛋）与金马奖（台北流行音乐中心）及读者来信，与该行无关。
- text.md：`BABYMONSTER` 仅 P5 表行（L3473–3475，导出品，重建即更新）。
- **结论**：该行只出现在 P5 香港表；P8 无题/键涉此行（content8.py 0 命中）；核心无台北节目表可移入。
- D1（「下週日」→「本週日」，fix1 已修）一概未碰：重建后 text.md / 双 PDF 文字层核查，本週日 11、 下週日 0（见 GATE-LOG §2）。

## §2 处置：只删除，不硬塞

- 从「香港11月節目」表中移出台北这一行（proof1 建议：移出该列）。
- 不把台北场塞进香港表其他位置；核心另无台北节目表，故不移入他表，只删除。

## §3 改动（仅 content56.py，3 处）

1. 删表行：`"BABYMONSTER台北演唱會：11月21、22日（台北小巨蛋）",`（原 L105；表由 6 行→5 行）。
2. 表框高：`p.rect(rx, by3, CW, 480, fill=BOX)` → `418`。依据：该行实测单行，行距 24 + 22.5×1.32 + 8 = 61.7px（SVG 行基线 1503.6→1565.3→…→1841.8，间距皆 61.7）；480−61.7 = 418.3，取 418。改后末行基线 1780.1、框底 1823.6，底距 43.5px，与改前（末行 1841.8、框底 1885.6、底距 43.8px）一致，无多余留白。
3. `by4 = by3 + 498` → `by3 + 436`（附注说明）。依据：保 18px 框间距（418+18=436）；其下「爵士音樂節時間表」框整体上移 62px（y 1903.6→1841.6，底 2333.6→2271.6），页脚线 2596 之前留白 324px，属正常页尾空白。

## §4 重建（工具 venv，日志见本目录）

- `run.py` RC=0（build.log；TOTAL 150，A2 44 / B1 74 / B2 32，分頁 10/18/18/18/18/18/12/38，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；重跑一次 SVG 哈希不变）。
- `render.py` RC=0（render.log）；`webpdf.py` RC=0（webpdf.log）；`export_zhtw_textmd.py` RC=0（export.log）。
- 导出小插曲：第一次 export 误传 H1 标题（写成 "Lucerna Weekly VOL.4 — …"），当即发现并用原 H1（"Lucerna Weekly — Traditional Chinese, English explanations"）重导；终版 text.md 与 fix1 仅差 H1 不变 + 移出行（49,816→49,735 B，少 81 字节 = 移出行 3 行文字 + 空行）。

## §5 交付物（新双 PDF + text.md）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 `Lucerna-VOL4.pdf` | 19,419,829 B | `3ab3f75815444d6b6da389f026e82a17e4d747226698083c16f6b26523d3474e` |
| 网页 `Lucerna-VOL4-web.pdf` | 2,323,405 B（< 7 MB） | `582c4aa7b1a90a065c5d5e5e0f4b7219394a0089b67ee1791d2e700c8d46938e` |
| `2026-w47-zh-tw-en.text.md` | 49,735 B | `7e1a45165dc663af5301d95784567b03f4e9f512766571e507663086d510791c` |

- 双 PDF 各 8 页、1462.5×2025 pt。
- fix1 基线（2026-11-11 08:47）：print 19,421,129 B / `daa43834…19210`；web 2,324,807 B / `596defd7…34ac1f`；text.md 49,816 B / `1dd4afab…8bc17`。
- Web-PDF 注：webpdf.py 每次重跑 SHA 都不同（fontTools 子集化随机标签：fix2 实测三跑 2,323,404 / 2,323,405 / 2,323,400 B、SHA 皆不同，首差在压缩字体流内；印刷 PDF 两跑 SHA 相同）。KIT 登记以本次交付文件为准。
- WEEKLY-KIT.md 已更新（新双 PDF 尺寸+SHA、text.md 尺寸+SHA、fix1+fix2 构建史、BABYMONSTER 来源行改注移除、文字层数据更新）。

## §6 未做事项（按任务范围）

- 未跑 insert.py、lint --write；未做任何 git 写操作（除任务要求的 hash-object 探针外；`git status` 仅只读查看：core-zh-tw/ 目前未入 git 追踪，属 W47 生产中状态）。
- 未碰 fan-out 各版、tools/、其他目标语、其他家庭；D1 未碰、未回归以外核查（仅文字层计数确认无回归）。
- 未派复校：核心重校随后由协调员一次派发（覆盖 fix1+fix2）。
