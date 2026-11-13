# GATE-LOG.md — W47 es-en proof2（重建版，2026-11-11）

工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-en2/`
解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0）；TMPDIR = 本工作目录。
版：`~/workspace/weekly-git/production/2026-w47/2026-w47-es-en/`；核心：`~/workspace/weekly-git/production/2026-w47/core-es/`。
结论：**(a) 定稿**，零缺陷。观测项 14 项（见 PROOF-NOTE.md），其中 D5 字体为记录项不计判定。

## 探针与身份核对

| 检查 | 结果 |
|---|---|
| `git hash-object -w` | rc=0 → `a7e6fcddc35f16bc353304c0452bcbbe6e604a0e` |
| scratch 写测试（真实文件 `probe-es-en2.txt`） | 成功 |
| `/dev/null` 存在且可写 | OK |
| 印 PDF | 3,500,924 B，SHA `80b4ce0a095551599adbf0e8e0c617715513a6df3c6ad004cc1428d8bb99b602` ✓ |
| 网 PDF | 886,730 B，SHA `f03047b1631fba034e3e65d2804a95c4c4ea40ba6af36a46e312921a7a70b5b0` ✓ |
| text.md | 44,983 B / 1,797 行，SHA `6080c94c420fd1077fedee777bba77ec789fd4c6c431ef70e7b7313923cc8906` ✓ |
| core-es 印/网/text.md（重建前后复核） | 17,212,955 B `2723a283…138b5` / 1,410,471 B `c2473211…85e235` / 1,822 行 `509c95fa…8ddb` ✓与 re-fanout 报告 §0 完全一致，未变 |
| 开工快照 | shipped 8 个 SVG SHA（`shipped-svg-sha.txt`）+ mtime（`shipped-mtimes.txt`） |
| 旧版备份 identity | print `e881ebb9c50efe590a97684962f848d8386abd24ca43504945ca9b45f7256b16`（3,500,745 B）/ web `8ab8c66cc9c4e642b7d12c183423fef8c7a167aed338baaf91b6d92683696a77` / text.md `886b6af5e84dde8f641975a2f907208283cc00ca09d5998b6c6e2cbfff13ecd3`（44,386 B）——均与 proof1 记录逐字一致 |

## 门禁逐项

| # | 门 | 命令 / 方法 | rc | 结果 |
|---|---|---|---|---|
| 1 | run.py 重跑（scratch 副本） | 版复制到 `rerun/2026-w47-es-en/`（去 `__pycache__`），`run.py` 重跑 | 0 | TOTAL 150，OVERFLOW 0，TOO WIDE 0；A2 50 / B1 72 / B2 28；按页 10/18/18/18/18/18/12/38；按型 48/47/12/8/7/10/13/4/1；MODELO 97 词；P5 col3 1574.55，P7 col3 1844.51，P8-keys 终 y=2569；重跑 8 SVG 与 shipped **逐字节一致**（`rerun.log`） |
| 2 | occlusion_audit | `tools/occlusion_audit.py` 自跑 | 0 | **0 flags**；自检 6 类阳性对照全数触发，干净对照静默（`occlusion.json` / `.log`） |
| 3 | p8 extract | `tools/p8.py` 自跑 | 0 | **150/150**（`p8-extract.json` / `.log`） |
| 4 | p8 compare（vs core-es） | `tools/p8.py compare` 自跑 | 0 | **CLEAN**；missing=[] extra=0 uncertain=[]；keydiff=[137, 138]（已裁定，翻译题键重定向；其余 148 键逐字节相同）（`p8-compare.json` / `.log`） |
| 5 | keycheck（REG vs P8 抽取键，rerun 副本） | `keycheck_core.py` 自跑 | 0 | 149/150 逐字一致；唯一差异 #150（REG 键为“150. (open question — the model text follows)”占位句，抽取键 “✓”；与 text.md 备注一致，为设计）（`keycheck.log` / `keycheck-150.json`） |
| 6 | freeze baseline | `freeze.py baseline`（自带写穿守卫，out 到本目录 `freeze-es-en-proof/`） | 0 | **8/8 SVG 逐字节一致**（p1 `3147e374…`、p2 `d9a7002d…`、p3 `101be06d…`、p4 `ee3ce37f…`、p5 `24a0f31b…`、p6 `6756deed…`、p7 `8a48923c…`、p8 `cc90c0c6…`）；core 完整性：重哈希 8 文件未变（`freeze.log`） |
| 7 | freeze diff（core vs 本版） | `freeze.py diff` 自跑 | 0 | added CJK 字符数每页均为 0（p1 +29/−38、p2 +50/−52、p3 +33/−30、p4 +33/−27、p5 +45/−48、p6 +19/−17、p7 +47/−46、p8 +164/−626）（`freeze-diff.json` / `.log`） |
| 8 | creambox 全扫 | `creambox.py` 全扫 | — | 6 条原始负值，均为已知框下标题（与重建门禁一致）（`creambox.log`） |
| 9 | creambox 逐盒真墨裁定 | `creambox_diag.py`（PIL 真墨） | — | **0 处自有墨溢出**；最小墨隙 +0.1px（P2 Note 盒，墨底 543.4 / 框底 543.5；P5 Note 盒，墨底 1251.4 / 框底 1251.5）；其余 +1.7…+47.5px；所有框下窗口内文本均为节标题或后一盒盒题（`creambox-diag.log`） |
| 10 | boxtitle（宽度 + P1/P2 真墨复测） | `boxtitle_core.py` + PIL getbbox 自定义复测（P1/P2） | — | 25 盒 **0 溢出**；最小余量 +21.3px（P5 “EL PLAN DE LA SEMANA　The plan”）；P1 真墨最小 +27.5px（“LA SEMANA EN CIFRAS　Numbers”）；P2 真墨最小 +51.0px（`boxtitle.log`） |
| 11 | sweep（box-vs-hline / bridge orphans / bridge widows） | `sweep_de.py` 自跑 | — | box-vs-hline 0；bridge orphans 0（20 座 bridge 全数同栏连续）；bridge widows 0（`sweep.log`） |
| 12 | 印/网文字层 | `pdftotext -layout` ×2 + `cmp` | 0/0 | 各 107,966 字节，**逐字节一致**；均为 8 页、1462.5×2025 pt；网 886,730 B（< 7 MB）→ 相对旧网 849,020 B（`print.txt` / `web.txt`） |
| 13 | P8 最小字号 | `minfont.py`（PyMuPDF + pypdf 双测） | — | min effective **10.125 pt**（n=378），≥ 9.75 pt 底线；低于 9.75 pt 者 0（`minfont.log`） |
| 14 | P8 末键墨 | PIL 真墨 + 向量坐标 | — | 末键基线 2553.14，最大墨底 2556.6；距页脚线 2596 约 **39.4px**；流终点 y=2569 与旧版同值（KIT §6.8 已裁定） |
| 15 | 孤儿标点全扫 | 8 个 SVG 全部 `<text>` 行人工规则过 | — | 独行 。/ 独行右引号 `”` / 独行 `：` / 独行 `–` 均为 **0**；行首闭合标点亦 0 |
| 16 | U+2019 全扫 | 8 个 SVG 全局计数 | — | U+2019 **0**；U+2018 0；ASCII 撇号 8 处；含撇号行目视无宽字形断裂 |
| 17 | CJK / 中文残留 | 8 个 SVG 全局计数 + `.text.md` | — | 可见文本仅 U+3000 ×117；汉字 0；唯一汉字在非渲染 `<title>Lucerna 三色蛾</title>`（与 core 一致）；`.text.md` CJK 97，全部为 U+3000 |
| 18 | em-dash 假阳性专项 | `p8-extract.json` 键全文统计 + 渲染裁切/源行核对 | — | 含破折号抽取键仅 #60 “El Barça ganó 1–2 al Atlético.”、#62 “El Atlético perdió 0–2 con el Bayern.”（比分类 en-dash，非键–注分隔符，提取正确）；无键含 em-dash “ — ”；compare `uncertain=[]`。es-ru #137 式假阳性**未遇上** |
| 19 | 答案三源一致（150/150） | 定向核查 `text.md` 答案区逐项含 “N. KEY” 原文（P8 抽取键 + REG 键双向核对） | — | 150/150；#150 为 “150. ✓ See the model text in section H on this page (97 words)”（`answer-3way.json`）；注：naive 逐行切分会因栏拼合法误切（如 “201067. C”、false “20. ” start），故用定向原文法 |

## 旧 vs 新对比（backup-old build 5 → 新重建版）

- 源码差分：仅 content12.py（26 行）、content56.py（9 行）、content7.py（2 行）、content8.py（12 行）有改动；content34.py / bslib4.py / svglib.py / run.py / render.py 零改动（`old-new-py.diff`，186 行）。
- 逐行归类：全部改动对应已记录的 core build 10 变更——C1（P1 CINCO CLAVES 700→720）、C2（`antes del jueves`→`hasta el jueves` + 全部题键/注 “by the 19th at the latest”）、debate 协议新段落（cara a cara 双方接受、无公布时间；Academia 承办两场辩论）、SER 住房辩论已 acordado、RTVE debate-a-ocho 时间轴 INSERT 行、RTVE 图表注加 “Acuerdo de la Junta Electoral Central del 4 de noviembre”、consejo 句补全、来信德比 viernes→sábado。无 DELETE，无未记录改动。
- SVG 可见文本差分：P1 +9/−9、P2 +5/−5、P3 0、P4 0、P5 0、P6 +26/−13、P7 +1/−1、P8 +12/−10（均为 C2 相关键/注/题干/MODELO；+2 为 #139 注换行与 #150 行空格分隔符）（`old-new-svgtext.diff`）。
- 渲染像素差分（96 dpi，阈值 >8；脚本 `pixdiff.py`，结果 `pixdiff.txt`）：P1 27,695 px（头条段落+CINCO 盒+图注+consejo 行）、P2 10,118 px（仅第 1 栏特稿段落）、**P3/P4/P5 0 px（像素全同）**、P6 236,919 px（重写段落+时间轴+图表注）、P7 3,238 px（仅来信句）、P8 9,552 px（C2 相关键/注/题干/MODELO 区）。
- 结论：新旧差异完全收敛在已记录的重建修复处，无意外变化。de/fr 的 boxtitle 溢出类修复（各 2 处）与 fr/nl 的 P8 注缩行（各 5 条）在 es-en 均无同类问题（boxtitle 0 溢出、P8 注无溢出警告）。

## 目视记录

- 印刷 8 页逐页：`rerender/p-1.png` … `p-8.png`（96 dpi，1950×2700；印 PDF 独立重渲染）。网页 P1/P8：`rerender/web-p-1.png` / `rerender/web-p-8.png`（目视与印刷一致）。旧版对照渲染：`old-render/p-1.png` … `p-8.png`。
- P1–P8：无溢出、无重叠、无压页脚、无截断句、无图片缺失。P2 Note 盒末行 “escaño = seat in parliament.”、P5 Note 盒末行 “box.” 均在框内；P5 “¿Y TÚ?” 盒在 EJERCICIOS 分隔线上方结束；P6 重写段落跨栏断句正确（“Un debate «propuesto» no es un debate” → “«cerrado»: la primera lección…”）；P7 八条金句及页码引用正确，LA PRÓXIMA SEMANA 横幅远离页脚；P8 键终止于页脚线上方，RESPUESTAS 栏标题与天鹅图注无重叠。

## no-touch 复核（收尾）

- 三件 SHA（印 `80b4ce0a…` / 网 `f03047b1…` / text.md `6080c94c…`）收尾复核一致。
- 8 个 SVG SHA：与开工 `shipped-svg-sha.txt` 快照一致（diff 空）。
- 全部 SVG / PDF / text.md / content*.py mtimes：与开工 `shipped-mtimes.txt` 快照一致（diff 空）。
- `git status`：仅显示两个未追踪目录（`?? production/2026-w47/2026-w47-es-en/`、`?? production/2026-w47/core-es/`），无任何修改。
- 未改源码/成品；未碰 core-es、W43–W46、其它语言家庭、tools/；未跑 insert.py / lint --write / render.py（原地）；未 git add / commit / push / reset / stash。run.py 与 keycheck 只在 scratch 副本上跑；freeze baseline 自带写穿守卫并复核 core 未变。本日志 + PROOF-NOTE.md + 全部产物均只写在 scratch-proof-es-en2/ 内。

## 一本账（产物清单）

`boxtitle.log`、`boxtitle_core.py`、`creambox.log`、`creambox.py`、`creambox-diag.log`、`creambox_diag.py`、`freeze.log`、`freeze-diff.json`、`freeze-diff.log`、`freeze-es-en-proof/`、`keycheck.log`、`keycheck-150.json`、`keycheck_core.py`、`minfont.log`、`minfont.py`、`occlusion.json`、`occlusion.log`、`old-new-diff-rq.log`、`old-new-py.diff`、`old-new-svgtext.diff`、`answer-3way.json`、`p8-extract.json`、`p8-extract.log`、`p8-compare.json`、`p8-compare.log`、`pixdiff.py`、`pixdiff.txt`、`print.txt`、`web.txt`、`probe-es-en2.txt`、`rerun/`、`rerun.log`、`shipped-svg-sha.txt`、`shipped-mtimes.txt`、`rerender/`（新印 P1–P8 + 网 P1–P8）、`old-render/`（旧印 P1–P8）、`sweep.log`、`sweep_de.py`。
