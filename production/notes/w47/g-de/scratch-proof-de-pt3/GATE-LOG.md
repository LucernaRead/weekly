# GATE-LOG — 2026-w47-de-pt · proof3

- 版次：`production/2026-w47/2026-w47-de-pt/`（rebuild 4，工具盒修后）
- 复校员：proof3（独立），2026-11-11
- 环境：TMPDIR = scratch 内 `tmp/`（/tmp 已满风险下全程规避）；工具 `~/workspace/weekly-git/tools/venv/bin/python`
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 真实写文件 OK。/tmp 探针时 2% 已用（503M 可用），仍全程用 scratch tmp/。

## 1. 基线 SHA（三向，动工前）

```
print  Die-Lucerna-VOL4-de-pt.pdf      10968902 B  c0019075c98389d84c3b71076d8828b9079de2e737332ff76d0fcd998a7ac4e0
web    Die-Lucerna-VOL4-de-pt-web.pdf   1602472 B  e48265d346544f278cf25a5a040a0a5656dd7ef639480bb7ed07ad988a64282a
text   2026-w47-de-pt.text.md            49812 B  e2ee96ebd9dca775598431f87c511f53ed04dec2547896586d46a2c57a800928
```

全部与任务书 KIT §7 基线一致。工作后复测（§10）三者未变。

## 2. 读物（动工前）

- SOP.md §1.1、§8 全文；repo AGENTS.md
- `scratch-proof-de-pt2/PROOF-NOTE.md`（proof2）
- `scratch-fix-de-pt-toolbox/FIX-LOG.md`（工具盒修）
- KIT `WEEKLY-KIT.md` §7 + rebuild-4 节
- `scratch-proof-de-en2/PROOF-NOTE.md` D1/D2 节（引号空隙方法）

## 3. 机械门（`run-gates.sh`，2026-11-11 ~10:00 UTC）

`FAIL_COUNT=0`；完整日志 `gates.log`。门后 SHA 复测：三文件未变；版次目录仍为 git 未跟踪 `??`；仓库另有 106 文件被其他 agent 的在途工作改动（例 `tools/occlusion_audit.py`、`tools/p8.py`）——非本人改动，未触碰。

| 门 | RC | 结果 |
|---|---|---|
| verify.py | 0 | SOP 1.1 审计 True；MUSTER 84 词；图表 44+33+23=100；日期 18.11+11=29.11、15.11+7=22.11、16.11+6=22.11 全 True；P8 最小 SVG 字号 13.25 → 9.9375pt |
| occlusion_audit（正式，未加 `--selftest`） | 0 | 自测 6 类植入全触发、干净对照静默；0 提示 |
| p8.py extract | 0 | 150/150 noted |
| p8.py compare vs core-de | 0 | CLEAN；missing=[]；extra=0；keydiff=[137,138,139,150]（预期） |
| freeze.py diff | 0 | 新增 CJK 合计 7（P2–P8 每页 1 个 U+3000，P1=0） |
| freeze_direct（源 + 渲染） | 0 | 源 PASS（移除 0 / 新增 0）；渲染 8/8：p1 147 `083e2a2a`、p2 163 `689045ad`、p3 195 `fc88f676`、p4 166 `df1bebf7`、p5 173 `86fa4421`、p6 175 `2bbe05f9`、p7 150 `b7aa0771`、p8 186 `57e118e7`（与 proof2/修后值相同） |
| keycheck 150 | 0 | 149/150 精确；唯一不符 Q150（提取器截为 "Tarefa livre"，预期） |
| boxtitle 7/7 | 0 | 356.5 / 386.0 / 378.5 / 333.9 / 386.1 / 384.8 / 388.1 px，预算 400.5 |
| measure | 0 | 24/24 PASS，0 FAIL |
| pdftotext 印 vs 网 | 0 | 均 50,684 B；词多重集相同；`-raw` 归一化相同（各 49,500 B） |
| chips | 0 | 每页 {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35}，合计 141；P8 A2 22 / B1 13 / B2 0 |
| P8 最小字号 | 0 | 9.94pt，349 spans，印/网相同 |
| abutting | 0 | P1 最大 0.22pt（"Die Lucerna"）；P2–P8 0.00pt |
| d2scan | 0 | 60 对；0 空隙 >0.5pt |
| creambox 全版 | 0 | 仅余已知误报：P1 −24.0、P2 −44.9、P7 −35.0 ×3（数值与修后日志相同） |
| 弯引号计数 | 0 | U+201C 33 = U+201E 33；U+201D 0；U+2019 0；« 7 = » 7 |
| Q34 题干五层 | 0 | 新 "Am Montag öffnet in Köln der erste" 1× / 旧 "öffnen … die ersten" 0× |
| D1 `pess.` 五层 | 0 | 13 处；`pers.` 全版 0 |
| §1.1 grep | 0 | 旧配色词 0；每页非配色颜色数与 core-de 相同 |

注：verify.py 运行中重新渲染了 SVG（mtime 10:00:44–10:01:08 UTC），freeze_direct SHA 与 proof2/修后值相同，PDF/text SHA 未变——无内容变化。

## 4. P7 工具盒重测（`probe_p7.py` + `descender.py` + `creambox.py` + 200dpi 裁切）

| 项 | 实测 |
|---|---|
| 工具盒 | y=310，底=813.0，末基线 793.0，基线清除 +20.0；墨迹末端 798.2，墨清除 +14.8；末行 `Es ist fraglich, ob... = ainda duvidoso` |
| LESERBRIEFE | y=829，底=1381.5，末基线 1371.1，清除 +10.4 |
| NOCH EIN WORT | y=1398，底=1547.5，末基线 1504.6，清除 +42.9；距 1548 线 0.5px |
| 200dpi 目视 | `crop-p7-toolbox.png`：6 条全在盒内，末行 g 下伸在盒内；`crop-p7-col3-lower.png`：两盒底留白清晰，Sätze 线紧贴 NOCH EIN WORT 盒底下方、无重叠 |
| P7 印/网 200dpi 像素差 | >60 灰度 8,732/22,854,375，第 3 栏 0；差分区限于 pt x 70–378、y 970–1120（左栏图片区重采样） |

## 5. P8 引号空隙加测（`quote-gaps.py`，200dpi 像素墨列，阈值闭引号前 >0.2em = 缺陷）

| 目标 | 字体 | 闭引号前空隙（印 = 网） | 开引号后空隙 |
|---|---|---|---|
| H-DE 对照 `«Meine Novemberwoche»` | Newsreader 16.12pt | 2.16pt = 0.134em | 2.16pt = 0.134em |
| H-PT `«A minha semana de novembro»` | Noto Sans CJK SC 15.0pt | 2.16pt = 0.144em | 1.80pt = 0.120em |
| Q67 键注 `«Im Lande des Christkinds» (1903)` | Noto Sans CJK SC 9.94pt | 1.44pt = 0.145em | 2.16pt = 0.217em |

最大闭引号空隙 0.145em < 0.2em → **PASS**。«/» 字宽 0.48em（CJK 15pt：7.18pt；9.94pt：4.76pt）/ 0.57em（Newsreader：9.11pt），比例正常，非 de-en 宽体模式。Q67 开引号后 0.217em 只是 2.16pt 绝对值在 9.94pt 字号下的换算，非缺陷判据项。

脚本调试（两版 bug 已修复，最终版输出为准）：v1 rawdict chars 误取 `lines` 下、±2pt 填充吞邻字墨迹；v2 ±0.6pt 容差致邻字墨段串入（Q67 假值 −3.24pt）；最终版严格中点归属（墨段中点落入 advance 框者归属该字，« 双笔画自动合并）。

200dpi 裁切目视：`crop-p8-hbox.png`、`crop-p8-key67.png` 三处引号两端均紧贴，无可见断开。

## 6. 渲染

`renders/`：`print-p-1..8.png`（100dpi，2026-11-11 10:02–10:03 UTC）、`print-p8-200-8.png`、`print-p7-200-7.png`、`web-p8-200-8.png`、`web-p7-200-7.png`（200dpi）、`web-p1-100-1.png`（100dpi）、裁切 `crop-p7-toolbox.png`、`crop-p7-col3-lower.png`、`crop-p8-hbox.png`、`crop-p8-key67.png`。

## 7. 内容复读

- `2026-w47-de-pt.text.md` 1–1187 行全文读完；150 题答案键逐题语义复核，全对。
- P7 金句 8/8 逐字核对原文出处；Fehlerklinik 4 对正确；MUSTER 84 词。
- 日期/星期 `date -d`（Europe/Berlin）：3.11 二、4.11 三、5.11 四、6.11 五、7.11 六、8.11 日、13.11 五、16.11 一、17.11 二、18.11 三、19.11 四、20.11 五、22.11 日、24.11 二、25.11 三、26.11 四、27.11 五、29.11 日——与报内一致。
- 外部事实网上核实：欧冠/德甲/欧联/欧国联比分与赛程、圣诞市场日期与开幕时间、Ritter 画作、1903 日历、电力税、2027 预算、欧冠第 5 轮、德甲第 10 轮、Buß- und Bettag 通识——全部一致。本次补核：马竞–拜仁进球者 Karl 54'、Laimer 74'（fcbayern.com）✓。
- 8 页 100dpi 逐页目视：无溢出/重叠/缺字；页脚「Página N de 8」齐全；图片说明与来源齐全。

## 8. 其余小项

- ABSTRACT.txt：400 B，单行葡语，ASCII 双引号 0。
- core-de 文本比对（`core-de/2026-w47-de-zh-cn.text.md` 1185 行/233 行 CJK vs 本版 1185 行/0 行 CJK）：差异 235 行 = 233 行读者层替换 + L3 卷名行 + L17 刊头标语行；德语正文零漂移。
- SVG 残留 CJK：8 页除 U+3000 外 CJK 字符 0；U+3000 每页 15–24 个；唯一含 CJK 的 `<title>` 为 P1 moth 标记 `Lucerna 三色蛾`。
- P1 印/网像素差（100dpi）：强差 8,130 像素（0.14%），集中刊头显示字体区（y 0–200pt：2,801）、标题带区（y 200–400pt：约 1,854，稀疏）、底部照片区（y 1400–1800pt：3,475）；其余 0——与 proof2 T1 定性一致，无内容差异。

## 9. 结论

**结论 (a) 零缺陷 → 本版定稿。缺陷清单：空。**

## 10. 工作后 SHA 复测（全部工作完成后）

```
c0019075c98389d84c3b71076d8828b9079de2e737332ff76d0fcd998a7ac4e0  Die-Lucerna-VOL4-de-pt.pdf      10968902 B
e48265d346544f278cf25a5a040a0a5656dd7ef639480bb7ed07ad988a64282a  Die-Lucerna-VOL4-de-pt-web.pdf   1602472 B
e2ee96ebd9dca775598431f87c511f53ed04dec2547896586d46a2c57a800928  2026-w47-de-pt.text.md            49812 B
```

与 §1 基线完全一致——复校过程未改动任何文件。

## 文件清单（本 scratch）

- `PROOF-NOTE.md`、`GATE-LOG.md`（本文件）
- `run-gates.sh`、`gates.log`、`verify.log`、`occlusion.json/.log`、`p8extract.json/.log`、`p8compare.json/.log`、`freeze.json/.log`、`freeze-direct.json/.log`、`keycheck.log`、`keycheck-150.json`、`boxtitle.log`、`measure.log`、`print.txt`、`web.txt`、`print-raw.txt`、`web-raw.txt`、`abutting.log`、`d2scan.py/.json/.log`、`creambox.py/.log`、`descender.py/.log`、`probe_p7.py`、`quote-gaps.py`、`quote-gaps.json`、`quote-gaps.log`、`renders/`、`tmp/`、`probe.txt`
