# GATE-LOG — 2026-W47 ko-zh-tw proof1（独立复校）

工作区：`hidden_files/w47/scratch-proof-ko-zh-tw/`。所有门禁均由复校员在本工作区独立重跑；
生产目录 `production/2026-w47/2026-w47-ko-zh-tw/` 只读。解释器：freeze baseline/diff、run.py、
check_core/check_gloss、textmd 用 `/usr/bin/python3`（Pillow 10.2.0）；render.py、webpdf.py 用
`tools/venv/bin/python`；p8font 用 venv（PyMuPDF）。

## 交付物 SHA（复核前 = 复核后）

- 印 `Lucerna-VOL4-KO-ZH-TW.pdf` 46,280,042 B
  `180d3ce0ef35f88aef9842e30835b29c77f0b7d5082e6529f9255f019610a949` ✓
- 网 `Lucerna-VOL4-KO-ZH-TW-web.pdf` 4,348,626 B
  `cfe20ece5a19f03e9ec7e3593c8fced61eae3f78d7eb19fdd09ba9d0729a78ab` ✓
- text `2026-w47-ko-zh-tw.text.md` 34,637 B
  `af183ae64f665c405f86a54edf1a76315f80901e9fac615f7ba9b7cd70c453e2` ✓
- ABSTRACT.txt 268 B `88f967a1267da0e6b6b352582fea454de11a31ce171b5a46c0d67311b34d7767` ✓
- core-ko（复核前后未变，见 `core-sha-before.txt` / `core-sha-after.txt`）：
  印 46,232,227 B `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27`；
  网 4,232,878 B `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7`；
  text `2026-w47-ko-zh-cn.text.md` 34,606 B `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a`。

## 门禁产物（同目录）

| 门禁 | 日志 / 产物 | 结果 |
|---|---|---|
| 探针 | `probe.txt`（git hash-object 通；/dev/null 存在） | 通过 |
| run.py 重跑 | `run-proof1.log`（+ 工作区副本 `work/`） | rc=0；0 FLOW OVERFLOW / 0 HEAD TOO WIDE；TOTAL 150（A2 51/B1 72/B2 27；每页 10/18/18/18/18/18/12/38）；P8-keys 2351；P7 teaser 2425.7；8 SVG 与交付逐字节相同 |
| freeze baseline | `freeze-baseline-proof1.log` / `.json` | 8/8（系统 python3，rc=0） |
| freeze venv 对照 | `freeze-baseline-venv.log` | ABORT rc=2（ko 豁免，预期） |
| freeze diff | `freeze-diff-proof1.log` / `.json` | +822 CJK（47/66/49/60/56/42/97/405）；字符串 +267/−268；rc=0 |
| freeze diff 裁决 | `trace-freeze-diff-proof1.log`（`trace-freeze-diff-proof1.py` 自写） | added 未解释 0 / removed 未解释 0；builder verifier 在我的 diff JSON 上亦 0/0 |
| occlusion | `occlusion-proof1.log` / `.json`、`occlusion-selftest-proof1.log` | 0 flags；NEW vs core 0；selftest 六类全触发 |
| p8 extract | `p8-extract-proof1.log` / `.json` | 150/150 noted |
| p8 compare | `p8-compare-proof1.log` / `.json` | CLEAN；keydiff=[138] |
| check_core | `check-core-proof1.log`（`checks/check_core.py`，BUILD 指工作区副本） | rc=0；gloss fails 0；phrases 8/8 verbatim；orphan 0 |
| check_gloss | `check-gloss-proof1.log`（`checks/check_gloss.py`） | rc=0；gloss fails 0 |
| textmd 重导出 | `textmd-proof1.log` / `textmd-proof1.md` | 450 项；与交付逐字节相同（SHA `af183ae6…`） |
| 印/网文字层 | `print-plain-proof1.txt` / `web-plain-proof1.txt`（各 49,645 B）、`print-proof1.txt` / `web-proof1.txt`（-layout，各 92,239 B） | 两种提取均逐字节相同 |
| P8 最小字号 | `p8font-proof1.log` | 9.975pt（163 spans / 158 at-min），PASS ≥9.75pt；重渲染 PDF 同值 |
| creambox | `creambox-proof1.log`（正典 tools/creambox.py，md5 ee7a55…） | 49 盒；inside-only 全 >0，最紧 +4.5；P7 toolbox min +12.2 / desc +6.2 |
| creambox 真墨 | `creambox-diag-proof1.log`（es-de2 版 diag，PIL 真墨） | 真墨 clearance 最小 +2.5（3 盒），0 负值 |
| boxtitle | `boxtitle-proof1.log` | 8/8 ≤386.5px；最紧 349.3px（P3） |
| keycheck（自写） | 见 `verify-150-proof1.log` 末段方法 + 本表 150 题行 | 149 exact + #150 `✓` = 150/150 |
| 150 题三源 | `verify-150-proof1.log`（`verify-150-proof1.py` 自写） | 不符 0；锚定抽样 27/27 在 content*.py 有出处 |
| census | `census-proof1.log` | ex/match 166 项 0 missing；D6 missing 0 |
| §1.1 | `style11-proof1.log` | OK；P7 VOL.5 3→2 by design；CJK 417/426 allowed，stray none；U+2019 0 |
| D5 字体 census | （p8font 同批命令输出，未单存文件；见 PROOF-NOTE §3） | Latin-in-NotoSansCJK 226 / 全部 NotoSansCJK spans 732（只记录，不判 (b)） |
| 渲染可复现 | `render-proof1.log`、`webpdf-proof1.log`、`web-proof1-scratch.txt` | 印 PDF 重渲染 SHA 与交付完全相同 `180d3ce0…`；网 PDF 同字节数、同文字层逐字节相同，SHA 不同（铁律预期） |
| 8 页目视 | `pages/p-1.png` … `p-8.png`（100dpi，交付印 PDF）、`render-png-proof1.log` | 8/8 干净，0 问题（见 PROOF-NOTE §5） |
| 旧版对比 | —（W46 仓内无 PDF/svg，见 PROOF-NOTE §6） | 无旧版 PDF 可比 |

## 注：freeze baseline 首跑 0/8 的原因（已纠正，非版本问题）

首跑误将 `--core-svg` 指向 `core-ko/svg`，得到 0/8——这是参照取错：freeze baseline
比对的是“重建产物 vs 参照目录”，本版 SVG 与核心本就差 +822 CJK，0/8 是预期结果。
纠正参照为本版自有 `svg/` 后重跑得 8/8（rc=0，逐字节相同；另用全哈希逐一核对
freeze build-copy 的 8 张 SVG 与交付相同后删除 build-copy）。
venv 对照 ABORT rc=2 符合任务书预期（ko 豁免已装好：ko 族须 Pillow 10.x）。

## 其他核查

- “next Sunday”：core-ko、ko-zh-tw（含 SVG/text.md）、`tools/tables.py` 全 0 命中——无适用对象。
- 弯引号：U+201C/U+201D/U+2019/U+2018 = 0/0/0/0（8 SVG + text.md）。
- 孤标点：真孤标点 0（SVG + text.md；`·`/`—` 引导均为设计分隔符）。
- 直引号 `'` 54 处与 core-ko 逐页计数相同（6/4/4/0/2/8/30/0），核心继承。
- W46 旧版：仓内无 PDF（`git ls-files` 仅源码/text.md/ABSTRACT/KIT），无逐页对比对象。
- 清理：scratch 重渲染的印/网 PDF 已删（SHA 已验）；工作区现 31M；生产目录零写入。
- 未 commit、未 push。
