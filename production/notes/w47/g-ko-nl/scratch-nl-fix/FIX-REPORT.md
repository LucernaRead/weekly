# 返修报告 — 2026-W47 荷兰文核心版 (core-nl, D1/D2 + T1–T3)

返修 builder：叶子（与第一轮 builder、校对员不同的人）。时间：2026-11-10 21:47–22:05 UTC。
对象：`~/workspace/weekly-git/production/2026-w47/core-nl/`（2026-w47-nl-zh-cn，VOL.4）。

## 修复内容（全部在 content12.py 与 WEEKLY-KIT.md）

| # | 位置 | 改动 | 证据 |
|---|---|---|---|
| D1 | P1 DEZE WEEK 注语 | "in de artikelen op pagina 2–4." → "pagina 2–5."；"本周日程见第2–4版文章" → "第2–5版文章" | 5 项逐项核对源码：MA 16 德国–荷兰 P4；ZA 21 NEC–PSV、Feyenoord–Excelsior P4；ZO 22 Ajax–ADO P4；ZO 22 Robinson 20:00 P5（"Elke zondag om 20:00 uur is Expeditie Robinson te zien op RTL 4"）。渲染图 P1 右栏注语已改；print.txt:145 行。 |
| D2 | P1 目录第 7 行 | "Woorden van de week" → "Drie gereedschappen"（P7 真实标题 "Drie niveaus, drie gereedschappen" 的删词缩短，与另 6 行做法一致；级别栏 "A2→B2" 已含"级别"信息，保留"工具"一半） | 中间尝试 "Drie niveaus, gereedschappen"（274.6px）被 occlusion_audit 拦下：TEXTX 与右端 "A2→B2" 重叠 25.2×13.2px——advance 宽度估算低估了真实墨迹范围。改短为 "Drie gereedschappen"（194.7px）后重审 0 flags。渲染图 P1 目录行与级别标签间留白清晰；print.txt:225 行。 |
| T1 | P1 顶栏 | "VOL. 4" → "VOL.4" | 与刊头副题、8 页页脚一致；print.txt:1 行；全刊 grep 无 "VOL. 4" 残留（core-nl 内）。 |
| T2 | P1 数字框第 2 行 | "20:45 — uur: de aftrap" → "20:45 — de aftrap"（自然荷兰语；中文译注不变，已含"柏林奥林匹克体育场开球"） | 仍为 2 行，数字框 cliff 几何不变；print.txt:159 行；P1 渲染图框内无溢出。 |
| T3 | 仅 KIT §4 | 希腊 "8 (5:4)" → "8 (5:3)"（失球：对塞 1、对德 0、对德 0、对荷 2） | 印品只印 "7 tegen 5" 进球对比、未印失球数，印品不动。 |
| T4 | — | 非缺陷，未动 | 范文 81/80 词两种口径均在 80–100。 |

改动文件：`content12.py`（4 处 P1 文本）、`WEEKLY-KIT.md`（§4 数字 + 新增 §12 返修记录 + §9 补充说明）。未碰 `tools/p8.py`（其未提交改动原样保留）、未跑 insert.py / lint --write / git 操作、未碰 W43/W45/W46。

## 重渲

- `run.py` exit 0：TOTAL 150（分版 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；范文 81 词），零 FLOW OVERFLOW / HEAD TOO WIDE。
- `render.py` exit 0：print PDF 25,955,551 字节。
- `export47.py` exit 0：`.text.md` 44,026 字节；142 单题行 + 2 配对头 + 8 配对项 = 150；金句 8 条；gloss 6 行。
- `webpdf.py` exit 0：web PDF 2,067,793 字节，44,135 text bytes。

## 全量自查（返修轮，零发现）

1. **全文精读**：重渲后 print PDF 文字层全文（44,134 字节）逐版读完，无新问题。与校对员 pre-fix 提取做 token 多重集差分：仅 4 处有意改动（+ pdftotext 换行点移动的伪差）；150 道答案逐条在 P8 答案区核对，关键键与校对员已验清单一致（43=1、44=4、45=19、46=17、85=65、87=100、126=B、141–144 b/c/d/a）。
2. **150 题复核**：`p8.py extract --total 150` → noted set 150/150；registry TOTAL 150 分布与 KIT 一致；`.text.md` 150/150。
3. **8 卡看图**：cards/p1–p8 逐版目视：无溢出、无重叠、无压页脚；7 照片 + P6 图表在位；P1 四处修复渲染正确。
4. **三工具**：
   - `occlusion_audit.py svg/`：selftest OK（6 类阳性全触发、阴性静默），**0 flags**。
   - `p8.py extract --total 150`：**150/150**。
   - freeze 直接 sha256 比对（干净目录重跑 `run.py`）：**8/8 MATCH**（`freeze-sha256.log`、`repro.log`）。
   - P8 字号实测（PyMuPDF）：答案区 min = median = **10.12pt** ≥ 9.75pt。
   - 文字层：web 44,135 vs print 44,134 字节（差 1 字节为尾部换行）；PyMuPDF 位置排序提取 8 页逐页 positional diff 0、multiset diff 0（6,511 token）。
5. **§1.1**：本次只改 4 处 P1 纯文本，未动颜色/字体/版心/徽章；P1 渲染图复核：纸色、刊头、页脚、徽章均与 pre-fix 一致。

## 过程记录

- 共享文件系统在本轮间歇性报 "Disk quota exceeded"（EDQUOT）：第一次 `webpdf.py` 在裁字体中途死亡（exit 120）、一次 `export47.py` 死亡（exit 120、0 字节日志）、一次 freeze 复现 `mkdir` 失败。当时磁盘实有 46 GB 空闲，疑为并行多 agent 写盘瞬时触发配额；无 EPERM、无 ffmpeg 失败。每次均为单次全新重跑且以自身输出验证通过，未硬锤重试。
- 本轮日志：`hidden_files/w47/scratch-nl-fix/`（build/render/export/webpdf/occlusion-fix1/2.log、p8-fix1.log、p8-fontsize-fix.log、webprint-fix.log、print.txt、web.txt、freeze-sha256.log、repro/ + repro.log、本报告）。
