# GATE-LOG — 2026-w47-es-zh-tw proof2

工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-zh-tw2/`（下称 S2）
解释器：一律 `~/workspace/weekly-git/tools/venv/bin/python`。TMPDIR=S2/tmp。
生产文件只读，永不改/提交/推送。run/render 在 S2/copy 副本中跑。

## 0. 开工前

| 步 | 命令/操作 | 结果 |
|---|---|---|
| SHA 复核 | `sha256sum` 印/网/text.md + 核心三件 + 旧版三件 | 全部与任务/基线一致（见 PROOF-NOTE §1） |
| 探针 | `git hash-object -w --stdin` + S2 真实写文件 `probe-es-zh-tw2.txt` | 通过 |
| /dev/null | `ls -la /dev/null`；一次 git 报 "could not open '/dev/null'" 后 `touch /dev/null` 垫回；13:26 起恢复为正常字符设备（crw 1,3） | 恢复 |

## 1. run.py（副本）

```
cd S2/copy && ~/workspace/weekly-git/tools/venv/bin/python run.py > S2/run-copy.log 2>&1
```
rc=0。TOTAL 150；A2 50 / B1 72 / B2 28；页分布 1:10 2:18 3:18 4:18 5:18 6:18 7:12 8:38；
MODELO 97 词；`flow[P8-keys] ended col 3/3 y=2506 (bottom 2560)`，无 OVERFLOW。
8/8 SVG 与生产版逐字节相同（sha256 比对）。

## 2. render.py（副本，后台会话 proc_a7322fe47c62，194 s）

```
cd S2/copy && ~/workspace/weekly-git/tools/venv/bin/python render.py > S2/render-copy.log 2>&1
```
rc=0。重渲染印 PDF SHA 与交付版**完全相同**（`ef5f1cde…`）。
重渲染网 PDF 1,725,940 B vs 交付 1,725,936 B，差 4 字节，SHA 不同
（`8d48ee5b…` vs `5b7d8796…`）；文字层逐字节相同（`copy-web.txt` 与 `web.txt` cmp 相同）；
8 页渲染逐像素相同；41 个字体子集标签完全相同——内容等价，见 PROOF-NOTE O6。

## 3. occlusion_audit.py

```
python tools/occlusion_audit.py --edition <版> > S2/logs/occlusion.log 2>&1   # 自检另见 occlusion-selftest.log
```
自检：6 类 planted 全部触发 1 次，干净对照静默。本版：**0 flags，rc=0**。`occlusion.json`。

## 4. p8.py（extract + compare）

```
python tools/p8.py extract --edition <版>  > S2/logs/p8-extract.log   # 150/150，rc=0
python tools/p8.py compare --edition <版> --core <core-es> > S2/logs/p8-compare.log  # CLEAN，rc=0
```
extract 150/150；compare missing=[]、extra=0、keydiff=[137, 138]（读者语翻译题）。
`p8-extract.json`、`p8-compare.json`。

## 5. freeze.py

```
python tools/freeze.py baseline --build S2/copy --core-svg <版>/svg  > S2/logs/freeze.log        # 8/8 字节相同，rc=0
python tools/freeze.py diff --core <core-es> --edition <版> > S2/logs/freeze-diff.log                 # rc=0
python tools/freeze.py diff --core <core-es> --edition <版> --strict-cjk > S2/logs/freeze-diff-strict.log  # rc=1（预期）
```
diff 逐页 ± 串见 PROOF-NOTE §3；新增 CJK 952；西语正文与 core build 10 逐字节相同。
`--strict-cjk` rc=1 为**预期行为**：zh-tw 为读者语，freeze 严格 CJK 模式要求
新增 CJK 字符必须在核心 CJK 字符集内（或为核心字符的繁体对应），而读者语讲解天然引入
核心没有的繁体字（如 佛朗明哥、繁體中文副标题）——rc=1 是模式含义，非缺陷；
逐字裁定见 §4（新增简体独有字符 = 空集）。

## 6. creambox.py + creambox_diag.py

```
python tools/creambox.py <版>          > S2/logs/creambox.log
python tools/creambox_diag.py <版>     > S2/logs/creambox-diag.log
```
全量盒本盒末行在内；0 本盒墨迹溢出。D3 修复确认：CINCO CLAVES 盒底 1308.0，
本盒末基线 1300.0（+8.0），墨迹底 1302.2（+5.8）。
最紧墨迹空隙 +0.1：P2 ¿SABÍAS? `ley.` 543.4/543.5；P5 VOTAR `compara precios antes de pagar.` 1251.4/1251.5。
窗下行全部裁定：下一盒标题（owner-rect=下一盒 y）或无主标题行；无真溢出。
P7 工具箱最小 +8.8（CARTAS 盒）。

## 7. boxtitle_core.py / sweep_de.py

```
python tools/boxtitle_core.py <版> > S2/logs/boxtitle.log   # 25 行标题，0 负空隙 = 0 超框
python tools/sweep_de.py <版>       > S2/logs/sweep.log      # box-vs-hline 0；桥 20，桥孤儿 0，桥寡妇 0
```

## 8. keycheck_core.py

```
python tools/keycheck_core.py --edition S2/copy --p8 S2/p8-extract.json > S2/logs/keycheck.log
```
**149/150** 精确；唯一不符 #150（REG `（開放題，範本如下）` vs 印 `✓`，已裁定的开放题例外）。
注：该工具将其 JSON 写到其 `__file__` 旁，覆盖了 builder 的
`scratch-refanout-es/keycheck-150.json`——内容确定性相同；已另存 `S2/keycheck-150.json`。

## 9. minfont.py（P8，印 PDF）

```
python tools/minfont.py <印PDF> p8 > S2/logs/minfont.log
```
最小有效 **10.125 pt**（n=718），0 处低于 9.75 pt 下限。

## 10. 印/网文字层

```
pdftotext -layout <印PDF> S2/print.txt; pdftotext -layout <网PDF> S2/web.txt
pdftotext <印PDF> S2/print-plain.txt; pdftotext <网PDF> S2/web-plain.txt
pdftotext -layout S2/copy/<网PDF> S2/copy-web.txt
```
-layout：印 = 网，**逐字节相同，106,384 B**（旧版印/网仅在第 14 行尾空格填充上不同，
已知 artifact）。纯文本：印 = 网，44,733 B。副本网 = 交付网文字层（cmp 相同）。

## 11. 渲染与像素比对

```
pdftoppm -png -r 100 <印PDF> S2/png/p    # rc=0（后台会话 proc_6d09eb9d103c，351 s，含网/副本网共 24 页）
pdftoppm -png -r 100 <网PDF> S2/png/w    # rc=0
pdftoppm -png -r 100 S2/copy/<网PDF> S2/png/cw  # rc=0
pdftoppm -png -r 200 -f 8 -l 8 <印PDF> S2/png/p200-8  # P8 200 dpi 裁切用
```
- 生产 cards/ 8 张 PNG 与 S2/copy 重渲染**逐字节相同**（sha256）。
- 印 vs 网像素差（强差 >30）：P1 14,010（仅行 0–400，黑体刊头字体子集渲染差；400 行以下 0 强差）、
  P2 767、P3 221,609、P4 63、P5 231,112、P6 505、P7 55,901、P8 98,225——
  P3/P5/P7/P8 为照片降采样（webpdf.py 已知行为），其余为抗锯齿噪声；无内容差异。
- 交付网 vs 副本网渲染：**8 页逐像素相同**。
- 新 vs 旧（proof1 渲染）：P1 28,620、P2 10,467、**P3/P4/P5 相同**、P6 249,809、P7 3,386（仅 derbi 行）、
  P8 10,876——全部在已记录修复区内，无意外变化。
- 目视：印 P1–P8 逐页 + 网 P1/P8，见 PROOF-NOTE §6。

## 12. 简体泄漏重验（重点）

```
grep 本周计划 / 本週計劃 / antes del jueves / hasta el jueves / antes de ese día / 19 日前  # content*.py + text.md + ABSTRACT.txt
~/workspace/weekly-git/tools/venv/bin/python S2/scan_cjk.py   # OpenCC s2t(c)!=c 全扫 → S2/logs/scan-cjk.log
freeze CJK 多重集配对重算（新增 947 / 移除 932；新增简体独有 = {}）
```
结果：残留 **0**。唯一 OpenCC 命中「台」×1 裁定为同形字（「電台」，见 PROOF-NOTE §4）。

## 13. 150 题手验 / 文本核查

- `S2/stem-key-table.txt`（844 行）：138 ex() + 3 match_set = 150 REG 条目，逐题通读；
  三源（REG / P8 提取 / text.md RESPUESTAS:1388–）0 不一致。Q150 范文手数 97 词。
- text.md 1,803 行通读（4 段）；P7 8 金句 exact-match 各 2×；弯引号配对（« 53/53、「 5/5；直引号 0）；
  内部标签扫（SOP/proofread/cover/lint 0）；`12 de noviembre` 0；VOL.4 ×1 / VOL.5 ×3；
  词汇表复现 P3/P5 均 ≥2×；ABSTRACT.txt 事实与繁体复核。
- 孤儿标点扫（SVG `<text>`、text.md 行、pdftotext 行）：独行 。/独行右引号/独行 ：/– **实质 0**
  （4 个独行 –/— 为行内分段）。另：孤字换行全扫仅 3 处（P2/P5「止）」、P8「二」），
  与旧版逐坐标相同、core 亦有，见 PROOF-NOTE O3。
- P7 横幅几何：深色矩 y=2464.51 h=118 底 2582.51，页脚线 2596，空隙 13.5 px，与 core 相同。
  P8 最末基线 2554.06（key 75 注），与旧版相同。
- WEEKLY-KIT.md §7（重建节）通读：SHA、分类计数、门禁结果与盘上一致（§1 仍引旧 SHA，见 O7）。
- 字体（只记录）：SVG 声明 Noto Sans/Serif CJK SC；`svglib.py` 指向 SC .ttc；系统同 .ttc 内含 TC 字面。
  见 PROOF-NOTE §7。

## 14. 旧版对比

- `S2/logs/textmd-old-new.diff`（backup-old → 新 text.md）：127 行变、约 40 段，全部由修复集解释。
- `S2/logs/print-old-new.diff`（pdftotext 旧印 vs 新印）：行级 diff 以 -layout 列移噪声为主；
  token 多重集 diff：移除 `antes`×11 等、新增 `hasta`×11 等，见 PROOF-NOTE §6。
