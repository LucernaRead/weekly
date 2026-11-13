# GATE-LOG — 2026-W47 de-it · proof1（独立复校）

工作目录：`~/workspace/weekly-git`；构建解释器：`tools/venv/bin/python`
（Python 3.12.3）。版目录 `ED=production/2026-w47/2026-w47-de-it`，
核心 `CORE=production/2026-w47/core-de`，本目录 `OUT=…/hidden_files/w47/scratch-proof-de-it1`。
未跑 run.py / render.py / webpdf.py / export（会重写交付件）；verify.py 重跑
后 8 份 SVG + 两份 PDF 的 SHA-256 逐一复核，全部未变。

## 探针（每次写盘前）

| # | 命令 | 结果 |
|---|---|---|
| 1 | `echo test \| git -C ~/workspace/weekly-git hash-object -w --stdin` + 写 `OUT/probe.txt` | RC 0，`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；写盘成功 |
| 2 | 同上（门禁前） | RC 0，写盘成功 |
| 3 | 同上（写 PROOF-NOTE 前） | RC 0，写盘成功 |

全程未遇 `Disk quota exceeded`（df：/home/hatch 78G 可用）。

## SHA 核对

| 命令 | RC | 结果 |
|---|---|---|
| `sha256sum Die-Lucerna-VOL4-de-it.pdf Die-Lucerna-VOL4-de-it-web.pdf 2026-w47-de-it.text.md` | 0 | 印 `0d7be5816da19474…`、网 `dbbe5880e1b8b130…`、文 `1594ba080bece8b9…`，与任务简报一致；字节 10,965,095 / 1,553,872 / 49,712 |
| `pdfinfo` 两份 PDF | 0 | 各 8 页，1462.5 × 2025 pt，PDF 1.7 |

## Q34 / 弯标点 / 文本 diff（系统 python3 + grep）

| 命令 | RC | 结果 |
|---|---|---|
| Q34 新/旧题干计数：`content34.py`、text.md、`svg/p3-kultur.svg`、印版/网页文字层；core `content34.py` 对照 | 0 | 5 处均为新 1× / 旧 0×；core 新 1× / 旧 0× |
| U+201C/201D/2019 扫描：8 份 SVG、text.md、content*.py | 0 | 2019=0、201D=0；201C=33，全为德语 „… “ 右引号（配对 201E=33），意语值内 0 |
| U+201C 33 处上下文逐条打印 | 0 | 全部在德语引文内 |
| `diff` de-it text.md vs core-de text.md（940 行）+ 机械德语漂移扫描（SequenceMatcher + 标签/词注剥离） | 0 | 标记对 101，残留 13 经逐对复核均为正则表达式伪报（多词术语拆分）；德语词干零漂移 |
| CJK/U+FFFD 扫描：text.md、8 份 SVG | 0 | text.md CJK 表意字 0、U+FFFD 0；SVG 仅 P1 logo `<title>Lucerna 三色蛾</title>`（与 core 逐字节同，非渲染文本） |
| ABSTRACT.txt | 0 | 393 B，一行，ASCII 双引号 0 |
| 日期星期 `TZ=Europe/Berlin date -d`（14 个日期） | 0 | 全部与版内星期表述一致 |

## 门禁重跑（tools/venv/bin/python）

| 门禁 | 命令 | RC | 结果（日志） |
|---|---|---|---|
| occlusion | `tools/occlusion_audit.py $ED --json $OUT/occlusion.json` | 0 | 0 flags；selftest 6 类全触发，干净对照静默（`occlusion.log`） |
| p8 extract | `tools/p8.py extract --p8 $ED/svg/p8-uebungen.svg --total 150 --json $OUT/p8extract.json` | 0 | 150/150（`p8extract.log`） |
| p8 compare | `tools/p8.py compare --core-p8 $CORE/svg/p8-uebungen.svg --edition-p8 $ED/svg/p8-uebungen.svg --total 150 --json $OUT/p8compare.json` | 0 | `status: CLEAN missing=[] extra_count=0 keydiff=[137, 138, 139, 150]`（`p8compare.log`） |
| freeze diff | `tools/freeze.py diff --core-svg $CORE/svg --edition-svg $ED/svg --json $OUT/freeze.json` | 0 | TOTAL added CJK 7，全 U+3000，P2–P8 各 1（`freeze.log`） |
| freeze-direct | `scratch-fanout-de-rebuild-A/freeze_direct.py it $ED $OUT` | 0 | 源码级未 accounted 0/0；渲染级 8/8（147/163/195/166/173/175/150/186；sha 083e2a2a/689045ad/fc88f676/df1bebf7/86fa4421/2bbe05f9/b7aa0771/57e118e7）（`freeze-direct.log`） |
| keycheck | `scratch-fanout-de-rebuild-A/keycheck.py it $ED $OUT` | 0 | 149/150 精确；仅 Q150 抽取器截断（`keycheck.log`、`keycheck-150.json`） |
| boxtitle | `boxtitle.py it`（cwd=scratch-fanout-de-rebuild-A） | 0 | 7/7（364.1/361.3/242.2/331.9/379.5/371.9/395.0 ≤ 400.5px）（`boxtitle.log`） |
| measure | `scratch-fanout-de-rebuild-A/measure.py it $ED` | 0 | 24/24 PASS，0 FAIL（`measure.log`） |
| verify | `$ED/verify.py` | 0 | TOTAL 150、编号连续、SVG 重跑后逐字节相同、SOP 1.1 审计 True、verbatim OK、P8 字号底线 True、17 禁词全无（`verify.log`） |
| verify 后交付件未变 | `sha256sum -c /tmp/deit-before.sha`（8 SVG + 2 PDF） | 0 | 10/10 OK |
| chips | 正则计数 rx=2.7 矩形 | 0 | 每页 10/15/18/15/18/18/12/35，总数 141；P8 A2 22 / B1 13 / B2 0 |
| P8 最小字号 | PyMuPDF 逐 span | 0 | 印版/网页 P8 最小跨度均为 9.94pt |
| pdffonts | `pdffonts` 两份 PDF | 0 | 网页 PDF 仅 Newsreader-Regular（无 Bold/Italic 子集）；印版含 Newsreader16pt-Italic 等 |

## 文字层

| 命令 | RC | 结果 |
|---|---|---|
| `pdftotext`（默认模式）印版/网页 | 0 | 50,593B / 50,597B；词多重集相同 |
| `pdftotext -raw` 印版/网页 | 0 | 各 49,392B；归一化文本完全相同 |
| `pdftotext -layout` 印版/网页（/tmp/deit-print.txt、/tmp/deit-web.txt） | 0 | 116,340B / 116,389B（仅作 Q34 与目视对照底本） |
| abutting 扫描 `abut_scan.py`（自写，PyMuPDF 行内跨度，阈值 0.5pt） | 0 | 印版/网页各 23 处、逐处相同；全部为练习 "→ ___" 设计间距（SVG 空格为独立元素，宽 5.4 单位 ≈ 4.05pt）；真实缺口 0（`abut-web.log`、`abut-print.log`） |

## 目视

| 命令 | RC | 结果 |
|---|---|---|
| `pdftoppm -png -r 100` 印版 → `/tmp/deit-proof/print-p-{1..8}.png`（2032×2813） | 0 | 8 页逐页看过，零问题 |
| `pdftoppm -png -r 100` 网页 → `/tmp/deit-proof/web-p-{1..8}.png` | 0 | 8 页逐页看过；内容/几何与印版一致，仅字重/斜体工具层差异（§7） |
| 像素差异 print vs web（PIL，灰度均值） | 0 | P1 1.22% / P2 0.34% / P3 0.29% / P4 0.37% / P5 0.32% / P6 0.37% / P7 0.93% / P8 0.07%（>40 灰度像素占比）；差异带定位于粗体标题区、金句区与图片区，无内容差异 |
| 200 dpi 标题栏并排对照（印版上/网页下） | 0 | 衬线粗体标题在网页为常规字重（T1；`/tmp/deit-proof/crop2-compare.png`） |
| 200 dpi 本周词并排对照 | 0 | «der Adventskalender» 印版斜体、网页正体（T2；`/tmp/deit-proof/crop4-compare.png`） |

## 逐字/逐键核对（python3）

| 命令 | RC | 结果 |
|---|---|---|
| P7 金句 8 句：正文（SÄTZE 节之前）+ P7 SVG 双向逐字核对 | 0 | 8/8 body=OK、svg=OK |
| MUSTER 词数（text.md 空白切分） | 0 | 84 词 |
| Q34 / 各键抽查（diff 人工 + keycheck 机械） | 0 | 见 PROOF-NOTE §4 |
