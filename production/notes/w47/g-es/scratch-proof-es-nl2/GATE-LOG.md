# W47 es-nl proof2 — GATE-LOG（独立重跑记录）

- 版：`production/2026-w47/2026-w47-es-nl/`；日期 2026-11-11；工作目录 S = `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-nl2/`
- 运行时：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR = goals 侧 `hidden_files/w47/scratch/tmp`
- 驱动：S 内 `gates.py`（自 refanout 驱动复制，S 路径改向本目录），`gates.py nl`；其余脚本见 PROOF-NOTE §11
- 结论：除注明的 harness 路径错与网 PDF 字节不可复现外，全部 rc=0

## 1. 驱动总表（`nl-gates.json`，我方实测）

```json
{"render_rc": 0, "occlusion_rc": 0, "p8extract_rc": 0, "p8compare_rc": 0,
 "freeze_rc": 0, "freezediff_rc": 0, "creambox_rc": 2, "boxtitle_rc": 0,
 "keycheck_rc": 0, "sweep_rc": 0, "print_bytes": 3502134, "web_bytes": 887963,
 "print_sha": "d5e63a7f5ee3c974b345ebdb72ca438082718de970e2469dba7c2f96b60db68c",
 "web_sha": "0287321285ab7c67524328f10045b4671479dcea8b776e4b910d4aedbb6f62b8",
 "text_sha": "d8d8e0078a7a121cf9a68bb22ee8074c6245462ebd86ef768cf87ee88c44b91e",
 "text_lines": 1835, "pdftotext_rc": [0, 0],
 "print_web_text_equal": true, "print_web_text_bytes": 109833, "minfont_rc": 0}
```

### 注 1 — `creambox_rc=2` 是 harness 路径错，不是门禁失败

`gates.py` 调 `S/creambox.py`，但 S 内该文件名为 `creambox13.py`（复制时改名），报 `can't open file …/creambox.py`（见 `nl-creambox.log`）。已补跑两版，
均 rc=0，结果一致：`nl-creambox-canonical.log`（canonical `hidden_files/w47/tools/creambox.py`）
与 `nl-creambox13.log`（13 行版），6 条负值相同；真墨裁决 `nl-creambox-diag.log`（rc=0），见 PROOF-NOTE §5。

### 注 2 — `web_bytes`/`web_sha` 与构建者版不同

构建者版 887,959 B / `54fbf35e…`（复核前我本人实测一致）；驱动重渲染后 887,963 B / `02873212…`。
决定性试验：同批 SVG 再跑 `tools/webpdf.py` 到 `S/web-retest.pdf`，得 887,962 B / `005712c0…`（`web-retest.log`）。
字节差定位在内嵌字体子集流（`/FontFile2 … /Length 1976` vs `1977`），PDF 内无 CreationDate/ModDate/ID。
结论：webpdf.py 字节级不可复现；印 PDF 两次渲染字节相同，文字层印=网逐字节一致（109,833 B）。
入仓时须从最终网 PDF 重量 SHA（PROOF-NOTE §1.3）。

## 2. 各门明细

| 门 | 命令 / 产物 | 结果摘要 |
|---|---|---|
| render | `render.py`（版内） | rc=0；印 PDF 3,502,134 B，SHA 与构建者版逐字节相同 |
| freeze baseline | `tools/freeze.py baseline --build <ed> --core-svg <svg> --out S/freeze-es-nl` | rc=0；**8/8** byte-identical；core 8 文件重算无变（`nl-freeze.log`） |
| freeze diff | `tools/freeze.py diff --core-svg core-es/svg --edition-svg <svg> --json S/nl-freeze-diff.json` | rc=0；added 362 / removed 553；新增 CJK 仅 U+3000 ×75，其余 0 |
| occlusion | `tools/occlusion_audit.py <svg> --json S/nl-occlusion.json` | rc=0；**0 flags**；自检 6 类全触发，干净对照静默 |
| p8 extract | `tools/p8.py extract --p8 <svg>/p8-ejercicios.svg --total 150 --json S/nl-p8-extract.json` | rc=0；**150/150** |
| p8 compare | `tools/p8.py compare --core-p8 core-es/svg/p8-ejercicios.svg --edition-p8 <svg>/p8-ejercicios.svg --total 150 --json S/nl-p8-compare.json` | rc=0；**CLEAN，keydiff [137,138]**（已裁决 E 组译键） |
| boxtitle | `S/boxtitle_core.py <svg>` | rc=0；**0 溢出**；最紧 P1 `EN ESTA EDICIÓN　In dit nummer` +6.0；D4 +7.3、D5 +94.3 |
| keycheck | `S/keycheck_core.py <ed> S/nl-p8-extract.json`（进程内 run.py） | rc=0；REG 150；**149/150**，唯一 mismatch #150 抽取 `✓`（已知例外）；`keycheck-150.json`；`flow[P8-keys] ended col 3/3 y=2506`，0 OVERFLOW；REG 统计 A2 50 / B1 72 / B2 28，页分布 1:10 / 2:18 / 3:18 / 4:18 / 5:18 / 6:18 / 7:12 / 8:38；MODELO 97 词 |
| sweep | `S/sweep_de.py <ed>` | rc=0；box-vs-hline 0；bridges 20，orphans 0，widows 0 |
| print/web 文字 | `pdftotext -layout` 印/网 | rc=[0,0]；**逐字节一致，109,833 B** |
| minfont | `S/minfont.py <print-pdf>`（P8） | rc=0；min **10.125 pt**（n=376），< 9.75pt 计 0 |
| creambox canonical | `S/creambox_canonical.py <svg>/*.svg` | rc=0；6 条负值（见 PROOF-NOTE §5） |
| creambox 13 行 | `S/creambox13.py <svg>/*.svg` | rc=0；与 canonical 逐字节一致的 6 条负值 |
| creambox diag | `S/creambox_diag.py <svg>/*.svg` | rc=0；自有末行墨 clearance 全部 ≥ 0（最小 +0.1 两处，见 PROOF-NOTE O2） |
| check_p8keys | `S/check_p8keys.py <svg>/p8-ejercicios.svg` | rc=0；keys 区 142 行；多行答案 6 项（#1、#44、#84、#139、#141、#36）——逐列复核后 #84/#141/#36 为跨列合并假象（各 1 行），#1/#44/#139 为先前已有长注（各 2 行，版面已容纳，终 y 2506） |
| D3–D6 真墨 | `S/d_measure.py` | rc=0；D3 +6.42、D4 +7.3、D5 +94.3、D6 横幅 2464.5 = core、页脚间隙 28.75、P7 col3 +9.20、P1 C1 +3.25（`nl-d-measure.log`） |
| D5 字体普查 | `S/font_census.py` | rc=0；Noto Sans CJK SC 拉丁-only 段 **396**（分页面见 `nl-font-census.log`）；core 同口径 218 |
| P8 三源交叉 | `S/p8_xcheck.py S/nl-p8-extract.json S/core-p8-extract.json` | rc=0；**PASS 150/150**：[1] 仅 #150 ✓ 例外；[2] text.md 0 问题；[3] keydiff 仅 [137,138]（`nl-p8-xcheck.log`） |
| core p8 抽取 | `tools/p8.py extract --p8 core-es/svg/p8-ejercicios.svg --total 150 --json S/core-p8-extract.json` | rc=0；150/150 |

## 3. SHA 复核（复核前后）

- 复核前：印 `d5e63a7f…` / 网 `54fbf35e…`（887,959 B）/ text `d8d8e007…`；core 印 `2723a283…` / 网 `c2473211…` / text `509c95fa…`。
- 复核后：印、text 与 core 三件均未变；网为重渲染副本 `02873212…`（887,963 B），见注 2。
- git 状态：版目录仍为未追踪（`?? production/2026-w47/2026-w47-es-nl/`），无 commit、无 push。
