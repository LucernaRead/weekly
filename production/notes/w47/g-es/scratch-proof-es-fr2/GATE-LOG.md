# W47 es-fr proof2 — GATE-LOG

- 版：`production/2026-w47/2026-w47-es-fr/`（未 commit、未 push）
- 复校：独立重跑，工作目录 S2 = `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-fr2/`
- 环境：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR=S2/tmp
- 探针：`ls /dev/null` 存在（常规文件，0 字节——git hash-object 仍通，未误判）；`echo test | git hash-object -w --stdin` 通；goals 侧真实写文件成功后开工。

## 逐项日志

| 步骤 | 命令（要点） | 日志 | rc / 结果 |
|---|---|---|---|
| 探针 | git hash-object + goals 侧写文件 | `probe.txt` | 通 |
| 身份核对（前） | sha256sum 三件 + core-es 三件 | §1 | 三件与任务给定一致；core 印 SHA 前缀 2723a283… |
| run | `python run.py`（edition 内） | `fr-run.log` | rc=0；TOTAL 150（A2 50/B1 72/B2 28）；8 SVG 哈希与 shipped 一致 |
| render | `gates.py fr` 内含 `render.py` | `fr-render.log` | rc=0；印 PDF 逐字节复现；网 PDF 内容一致、字节差 1（见注） |
| occlusion | `tools/occlusion_audit.py svg/ --json` | `fr-occlusion.log/.json` | rc=0；0 flags |
| p8 extract | `tools/p8.py extract --total 150` | `fr-p8-extract.log/.json` | rc=0；150/150 |
| p8 compare | `tools/p8.py compare --core-p8 core-es/... --total 150` | `fr-p8-compare.log/.json` | rc=0；CLEAN；keydiff [137,138]；missing/extra/uncertain [] |
| core p8 extract | `tools/p8.py extract`（core-es P8，独立） | `core-p8-extract.log/.json` | rc=0；150/150；与版 keys 仅 137/138 不同（中文→法语，已裁决） |
| freeze baseline | `tools/freeze.py baseline --build` | `fr-freeze.log`、`freeze-es-fr/` | rc=0；8/8 逐字节一致 |
| freeze-diff | `tools/freeze.py diff` | `fr-freeze-diff.log/.json` | rc=0；新增 CJK 1 × U+3000（p1 刊头结构空格） |
| creambox（canonical） | `hidden_files/w47/tools/creambox.py svg/*.svg` | `fr-creambox.log` | rc=0；inside-only 负 0；P7-TOOLBOX min inside +5.7 / desc-clear +0.0 |
| creambox 真墨 | `creambox_diag.py svg/*.svg` | `fr-creambox-diag.log` | rc=0；全部自有末行墨 clearance ≥ 0（C1 +3.8；D1 各 +6.7；O1 各 +10.1；最小 P4 +1.3） |
| boxtitle 真墨 | `boxtitle_core.py svg/` | `fr-boxtitle.log` | rc=0；0 溢出；min clear +14.8；Chiffres +43.1；Erreurs +90.5 |
| keycheck | `keycheck_core.py <edition> fr-p8-extract.json` | `fr-keycheck.log`、`keycheck-150.json` | rc=0；149/150（仅 #150 开放写作例外） |
| sweep | `sweep_de.py <edition>` | `fr-sweep.log` | rc=0；box-vs-hline 0；bridges 20 / orphans 0 / widows 0 |
| text_layer | `pdftotext -layout` 印 vs 网 | `fr-print.txt`、`fr-web.txt` | rc 0/0；逐字节一致 109,748 B；与 builder 文本层亦逐字节一致 |
| p8_font | `minfont.py <print pdf>` | `fr-minfont.log` | rc=0；最小 10.125pt；< 9.75pt 者 0 |
| 三向手验 | P8 keys vs text.md RESPUESTAS vs 核心 P8 keys（脚本 + 全文通读） | PROOF-NOTE §3.2 | 149/150 解析 0 不符（#150 例外）；版 vs 核仅 [137,138] |
| D5 字体 | SVG font-family 统计 | PROOF-NOTE §6 | 拉丁-only 落在 Noto Sans CJK SC：398 段（p1–p8：47/50/52/49/50/40/53/57） |
| 目视 | cards PNG 全页 + 9 裁图 | `visual/` | 8 页干净；C1/D1/O1/盒题/最薄盒裁图均确认墨在盒内 |
| 身份核对（后）+ 还原 | 恢复网 PDF 原始字节；全目录哈希 diff | `final-hashes.txt` | 三件 SHA 与复核前一致；生产目录 35 文件 diff 为空；core-es 未变 |

## gates.json 快照（重渲染当时）

```json
{
 "render_rc": 0, "occlusion_rc": 0, "p8extract_rc": 0, "p8compare_rc": 0,
 "freeze_rc": 0, "freezediff_rc": 0, "creambox_rc": 0, "boxtitle_rc": 0,
 "keycheck_rc": 0, "sweep_rc": 0,
 "print_bytes": 3500186, "web_bytes": 884226,
 "print_sha": "688152c7a055a25414e9c72b33f9e6d074b8137c2a9e2c9ea365b4d541e14894",
 "web_sha": "6e0c2ab76eaa4bd93b7d05cf6b1207b172d9acef2157da29740185c1d51f0f99",
 "text_sha": "ae1c3f3ba234a0b3f5ce2128770e4e4983d509822fdd520d03da4e98a76fad43",
 "text_lines": 1815, "pdftotext_rc": [0, 0],
 "print_web_text_equal": true, "print_web_text_bytes": 109748, "minfont_rc": 0
}
```

**注：上表 `web_bytes`/`web_sha` 是我方重渲染的当时值，不是交付值。**
重渲染的网 PDF 为 884,226 B / `6e0c2ab7…`，与交付的 884,225 B / `3c2d6069…` 差 1 字节，
已证实为字体子集化排序噪声（18/18 font 流字节不同、解压长度相同；内容流与文本层零差异；
两版 8 页 72dpi 渲染差异像素 0）。我方已用 builder freeze build-copy 的原始字节恢复网 PDF，
复核后实测：印 688152c7…、网 **3c2d6069…**、text ae1c3f3b…，生产目录与复核前逐字节一致。
