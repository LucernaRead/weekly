# GATE-LOG — 2026-W47 ko-es proof1

工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-es1/`
（`work/ko-es/` = 生产版 scratch 副本；`logs/` = 全部本轮日志；`freeze/` = freeze 基线产物）
解释器：freeze baseline/diff、run.py、check_core/check_gloss、textmd 用
`/usr/bin/python3`（Pillow 10.2.0 / FreeType 2.13.2，ko 家庭锁）；render/webpdf
类用 `tools/venv/bin/python`。**网 PDF 只核落盘 SHA，未重渲染。**

## 0. 开工核对

- 印 45,679,580 B `20c7f485832a5ff7e13e0a2687c728a27db818350f6d9654f08f94ec4a79c426` ✓
- 网 4,032,263 B `624c1933067d8f0f102971ed79d27eeb335526fa9fc0f330032bfdbb2d399d3f` ✓
- text.md 35,207 B `8c5396b8d0a342d6ffc4cc8d537138d94680bbf1586282f7a336d6e4c0252e89` ✓
  （文件名为 `2026-w47-ko-es.text.md`）
- 核心 ko：印 46,232,227 B `53bf14ed…a2f27`；网 4,232,878 B `9592945a…43bc7`；
  text.md 34,606 B / 452 项 `da1d3a32…8181a`——与 #3 基线一致，未变 ✓
- 探针：`git hash-object -w` 成功；scratch 写文件成功；`/dev/null` 存在 ✓

## 1. run.py

- 命令：`cd work/ko-es && /usr/bin/python3 run.py` → `logs/run.log`
- rc=0，0 FLOW OVERFLOW / HEAD TOO WIDE；TOTAL 150；
  by level A2 51 / B1 72 / B2 27；by page 10/18/18/18/18/18/12/38；
  by type Completar 48 / Opción múltiple 52 / Relacionar 16 / Transformar 4 /
  Formar frases 8 / Verdadero o falso 4 / Texto con huecos 13 / Traducir 4 /
  Escribir 1；model chars 169；P2-feature 1531，P8-keys 2457，P7 teaser 2483.7
- 重建 SVG 哈希 `logs/svg-rebuilt.sha`：与生产 SVG 8/8 字节一致；
  与 #2 run 3（`scratch-fanout-ko/es/sha-es-run3.txt`）比对：
  仅 P7 `eb377a55…` → `f73e0a06…`，其余 7 页一致 ✓

## 2. render（印 PDF 重渲染，venv，仅 scratch）

- 命令：`tools/venv/bin/python render.py` → `logs/render.log`
- rc=0；重渲染印 PDF 45,679,580 B，SHA `20c7f485…`，与交付字节一致 ✓
- 卡片：`work/ko-es/cards/p1..p8.png`（1950×2700），目视 8/8 干净

## 3. freeze

- baseline：`/usr/bin/python3 tools/freeze.py baseline --build work/ko-es
  --core-svg <生产 svg> --out freeze/` → `logs/freeze-baseline.log`，
  rc=0，**8/8 byte-identical**（Pillow 10.2.0 / FreeType 2.13.2）✓
- diff：`freeze.py diff --core-svg core-ko/svg --edition-svg <生产 svg>
  --json logs/freeze-diff.json` → `logs/freeze-diff.log`，rc=0，
  TOTAL added CJK 7，全为 U+3000（p2–p8 各 1，p1 0）✓

## 4. p8 / keycheck / 150 题

- `p8.py extract`（本次新鲜，venv）→ `logs/p8-extract.log/.json`：
  noted set 150/150 ✓；与 ko3 `p8-es.json` 键逐一相同 ✓
- `p8.py compare` vs 核心 → `logs/p8-compare.log/.json`：CLEAN，
  missing=[] extra_count=0 keydiff=[137, 138] ✓
- 核心 P8 提取 → `logs/p8-core.json`：137/138 为 E 组设计重定向，
  139/140 键仍韩文，其余 146 键与核心相同 ✓
- `keycheck-ko.py es`（共享工具，生产路径）→ `logs/keycheck.log`：rc=0，
  REG 150 / SVG keys 150 / exact 149 / trunc-ok 1（#150 `✓`）/ BAD 0 ✓
- `keycheck-mine.py es`（同工具，输入改为本次 scratch 副本 + 本次新鲜提取）
  → `logs/keycheck-mine.log`：rc=0，同样 150/150 ✓
- `verify150.py` → `logs/verify150.log`，REG 表 `logs/reg150.json`：
  记录表 150 行逐行比对（页/类型/键）0 差异；多字键在印文字层 0 缺失；
  6 条注（#79/#81/#91/#125/#133/#136）在 pdftotext 扁平串未整串命中，
  已逐条核实为栏序交错 artifact（P8 SVG 中完整折行存在）✓

## 5. boxtitle / occlusion / checks / census

- `boxtitle-ko.py work/ko-es` → `logs/boxtitle.log`：rc=0，8/8 ≤ 386.5px；
  最紧 P2 `Lista de la compra` 385.8px ✓
- `occlusion_audit.py --selftest` → `logs/occlusion-selftest.log`：rc=0，
  六类全触发，干净对照静默 ✓
- `occlusion_audit.py --json logs/occlusion.json work/ko-es/svg` →
  `logs/occlusion.log`：rc=0，**0 flags** ✓
- `check_core.py` / `check_gloss.py`（核心源复制到 scratch，BUILD 指到本次
  副本，gloss 前缀改为 `Nota — `）→ `logs/check-core.log`、
  `logs/check-gloss.log`：rc=0 / rc=0；gloss fails 0；短语 8/8 原文；
  orphan 0；日期 2026-11-16 Mon D-3 / 11-18 Wed D-1 / 11-19 Thu D-day /
  11-22 Sun 김치의 날 ✓
- `census.py <生产 text.md> work/ko-es` → `logs/census.log`：rc=0，
  ex/match 166 项 0 缺失；D6 0 缺失 ✓

## 6. textmd / 文字层 / 字号 / §1.1

- `textmd.py` 重导出（正确标题参数）→ `logs/textmd.log`，
  `textmd-reexport.md`：rc=0，449 项，与交付 **字节一致**
  （SHA `8c5396b8…`）✓（首次误用标题参数致首行差异，已纠正重跑；
  该次失败为调用参数错误，非工具/内容问题）
- 文字层：PyMuPDF 提取印/网各 48,446 B，`cmp` 一致；
  pdftotext 提取印/网各 107,850 B，`cmp` 一致
  （`logs/textlayer-print.txt`、`logs/textlayer-web.txt`、
  `logs/print-pdftotext.txt`、`logs/web-pdftotext.txt`）✓
  ——网 PDF 未重渲染，只核落盘 SHA ✓
- `p8font.py`（交付印 PDF）→ `logs/p8font.log`：rc=0，
  region spans 172，min **9.975pt**，at-min 167，PASS ≥ 9.75 ✓
- `style11-ko.py es` → `logs/style11.log`：rc=0；paper/VOL.4/`·`/颜色与核心
  逐页一致；汉字 0；U+2019 0；P7 VOL.5 3→2 按设计 ✓

## 7. creambox（正典工具，md5 ee7a55d8b2057cf4ad42a97bb1197383）

- `creambox.py work/ko-es/svg/*.svg` → `logs/creambox.log`：rc=0；
  49 盒，全部 inside-only；基线 clearance 最小 +5.1（三处 ¿Y tú?），
  其余 ≥ +12.5；P7-TOOLBOX 3 盒，最小 +12.5 / desc-clear +6.5 ✓
- `creambox_diag.py`（PIL 真墨，系统 python3）→ `logs/creambox-diag.log`：
  rc=0；49 盒真墨 clearance 全部 ≥ **+0.4**（三处 ¿Y tú? +0.4，
  其余 ≥ +8.7）；19 条 below-window 行 owner-rect 全部 NONE
  （下一标题/图注，+26..+44px）✓

## 8. 扫查

- 弯引号：U+201C/U+201D/U+2019 在 8 SVG + text.md 均为 0；
  「」P7 21 对、P1/P2/P8 各 1–2 对，text.md 24 对 ✓
- 孤儿标点：SVG `<text>` 行首 。/」/：/独行 。/」/：/– 均为 0；
  text.md 行首 。/」/：/– 及 ’/”/．/,/、均为 0 ✓
- text.md 扫描：汉字 0；`译注` 0；弯引号 0；`Todo` 0 次（P1 SVG 1 次）；
  `lcn2`/`lko` 0 次；`___` 75 处（与核心同为导出惯例）✓
- P2/P8 instr：新串在位，旧串全版 0 次 ✓
- H 范文：去空格 169 字，与印文 `(169 caracteres)` 一致 ✓

## 9. 目视

- 卡片 `work/ko-es/cards/*.png`（由交付 SVG 重渲染）：P1–P8 逐页读过，
  0 问题。P7 Frame `Marco: 「después de ~」. Pregunta: 「〜 후에 뭐 해요?」`
  目视确认；P8 F 标题单行无重叠，答案 1–150 齐。

## 10. 收尾核对

- `git status`：`2026-w47-ko-es/` 与 `core-ko/` 仍仅为 `??`，生产文件未动；
  无 commit、无 push ✓
- 缺陷：0。结论：**(a) 定稿**。
