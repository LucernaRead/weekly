# FIX-LOG — 2026-W47 pt-de fix1（D4 返修）

返修员：fix1，2026-11-11。Scratch：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-de1/`
（全部工作文件见该目录；生产目录只改了本版两个源文件 + 重建产物，未 commit，未 push。）
复校对象：proof2（`scratch-proof-pt-de2/`，结论 (b)，缺陷 D4 一项）。

## §0 版身份核对（先验 SHA，开工核对一致才动手）

| 文件 | 开工字节数 | 开工 SHA-256 | 与任务一致 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | 12,938,914 | `77243c72c38a14232ea443f03856ccf0a88f3d4b2c0c89e75aa87cf658e6284a` | ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | 1,147,629 | `56eb92d0251d691956e8dac6cccab0e9bf2a4bbadd9dc662c55632eb1b13b84b` | ✓ |
| `2026-w47-pt-de.text.md` | 37,907 | `519ab0dedbae110dba11eeffe3cd8517db41141020061e9a66c5dd252d784305` | ✓ |

核心 HEAD：开工 `c0382fa7`（含 `d2b0e182` core-pt fix2 为祖先）；版目录 git 状态
`?? production/2026-w47/2026-w47-pt-de/`（未入仓）。`core-pt/` 无任何修改（`git status
--porcelain -- production/2026-w47/core-pt/` 只有未追踪文件，无 `M`）。
探针：`/dev/null` 存在；`echo test | git hash-object -w --stdin` →
`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0（与 proof1/proof2 同值）；
scratch 写 `probe-write.txt`（`ok`）成功。
解释器全程 `tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0）；
TMPDIR 全程指向 scratch 下 `tmp/`（系统 /tmp 未用）。

## §1 缺陷 D4 与修法选择

- 缺陷：P1 `NESTA EDIÇÃO　In dieser Ausgabe` 框标题横向溢出奶油框右缘 1862.0。
  修前复测（基线，与 proof2 逐值一致）：PIL 真墨右缘 1863.5（余量 −1.5）；
  交付印 PDF 像素 200dpi 1864.8 / 96dpi 1864.0。
- 源：`content12.py:89` 字面量（`p.text(gx + 22, sy + 40, "NESTA EDIÇÃO　In dieser Ausgabe",
  24, "sans", True, OLIVE)`），德语部分译自 `tables_de.py:139`
  （`"本期目录": "In dieser Ausgabe"`）。核实：`core-pt/content12.py:89` 为
  `"NESTA EDIÇÃO　本期目录"`，transform 经 SEG 表替换生成了本版字面量；
  `run.py → render.py` 只读字面量，不读表——因此只改表不改字面量会是空修，
  两处必须同改。
- 三候选实测（同口径 PIL 真墨，修前探针 `width_probe.py`）：
  (a) 缩短副标题 → `Diese Ausgabe`：墨迹右缘 1826.5，余量 **+35.5**；
  (b) 字号 24→23：1846.5，+15.5；（22：1830.5，+31.5）
  (c) 标题左移 8：1855.5，+6.5。
- 选用 **(a)**：余量最大（对渲染器间约 5 单位宽度差最稳健——正是 D4 的成因），
  保持 24pt（与 E1/E2 两同框标题一致）与 gx+22 左对齐（与全版框标题一致），
  与 pt-it 同类缺陷 D4 的先例一致（`本期目录` → `Questo numero`，FANOUT-REPORT-pt.md §6）。
  `Diese Ausgabe`（“本期”）为自然德语等义表述。

## §2 改动（仅本版两个源文件，两行）

1. `content12.py:89`：
   `"NESTA EDIÇÃO　In dieser Ausgabe"` → `"NESTA EDIÇÃO　Diese Ausgabe"`
   （U+3000 分隔符保留；字号 24、粗体、x=gx+22 均不动）。
2. `tables_de.py:139`：`"本期目录": "In dieser Ausgabe"` → `"本期目录": "Diese Ausgabe"`
   （与渲染字面量保持一致，使未来重 fanout 不复活长式）。
3. 改后 grep：本版 `*.py` 再无 `In dieser Ausgabe`（`text.md:433`
   的 `(wörtlich aus dieser Ausgabe)` 为另一字符串，不受影响）。
4. 未动：core-pt、其他版、D1/D2/D3 源码行（见 §4）、E1/E2 标题、其他任何文件。

## §3 重建（整版，生产目录内按 KIT §7 正典命令）

1. `run.py`：RC=0，`TOTAL 150`（A2 48 / B1 71 / B2 31；每页 10/18/18/18/18/18/12/38），
   `OVERFLOW` 0 行。
2. `render.py`：RC=0，8 张卡片 + 印 PDF。
3. `gates.py`：RC=0，16/16 PASS，`FAILURES: none`。
4. `textmd.py`（`scratch-fanout-pt/textmd.py`，core zh-cn text.md → 本版 text.md）：
   RC=0，**text.md 逐字节不变**（SHA 仍为 `519ab0de…`，37,907 B）——标题不在 text.md 内，
   `"本期目录"` 亦不在 core text.md 内（grep 0 处）。
5. `tools/webpdf.py`（生产目录内正典命令）：RC=0，生产网 PDF 重渲。
   另在 scratch 重渲 `web-rerender.pdf` 专供比对（见 GATE-LOG §7；**未用 scratch 文件
   覆盖生产网 PDF**）。

## §4 修后三件 SHA（收工核对）

| 文件 | 字节数 | SHA-256 | 变化 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | 12,938,912 | `b8a738defa8be888fffc9ba670b32d65a2146224c10fe718f55258ebd55a513d` | 改变（标题缩短） |
| `A-Lucerna-VOL4-web.pdf`（网） | 1,147,636 | `2cad3d1b1b732e2ce1f11631d1f05c6fb196ab715b3f77f4965e2ca724483e69` | 改变（同上） |
| `2026-w47-pt-de.text.md` | 37,907 | `519ab0dedbae110dba11eeffe3cd8517db41141020061e9a66c5dd252d784305` | 不变 |

## §5 D4 修复复测（PIL 真墨 + 交付 PDF 像素双法）

| 方法 | 修前墨迹右缘 | 修后墨迹右缘 | 框右缘 | 余量 | 要求 ≤1858 |
|---|---|---|---|---|---|
| PIL 真墨（`boxtitle_ink.py`，svg） | 1863.5 | **1826.5** | 1862.0 | **+35.5** | ✓ |
| PIL advance（`boxtitle_core.py`） | 1863.6 | 1826.1 | 1862.0 | +35.9 | ✓ |
| 交付印 PDF 像素 200dpi | 1864.8 | **1826.9** | 1862.0 | **+34.6** | ✓ |
| 交付印 PDF 像素 96dpi（vs 卡片） | 1864.0 | 1827（卡片 1824） | 1862.0 | +34（卡片 +37） | ✓ |

300dpi 裁图 `visual/crop-p1-nesta-pdf300.png`：末字 `e` 完整在奶油框内，右端距框缘
约 35 单位，目视确认修复。

## §6 E1/E2 与 D1/D2/D3 复测（均在原位，无回归）

- E1 `EM POUCAS PALAVRAS　IN KÜRZE`：PIL 真墨 1861.5（+0.5）、PDF 像素 200dpi 1862.4 /
  96dpi 1862——与修前逐值相同，未动；300dpi 裁图末字 `E` 完整、右缘贴框边。
- E2 `A SEMANA EM NÚMEROS　In Zahlen`：PIL 真墨 1410.0（框缘 1412，+1.5）、PDF 像素
  200dpi 1408.3（+2.9）——与修前相同，未动。
- D1（P1 闪讯框）：源码 `content12.py:138` 框 474 在位；creambox-diag 真墨底 2332.6，
  墨余 **+15.4**（修前同值）✓。
- D2（P3 日程框）：源码 `content34.py:40` `+ 58` 在位；末行 `16h30.` 墨底 540.9，
  墨余 **+10.1** ✓。
- D3（P6 时间线框）：源码 `content56.py:132` 框 654 在位；末行 `Página do Participante.`
  墨底 846.0，墨余 **+8.0** ✓。
- 仅 P1 SVG 改变：freeze 8 字节哈希修前 f988db96/613f558b/c33752e6/af3e206b/
  d146ca3d/dd562a7a/2d53f697/a4447964 → 修后仅 p1 变为 6ced52ce，p2–p8 逐字节一致。

## §7 门禁总表（详见 GATE-LOG.md；缺一不可，全过）

| 门 | 结果 |
|---|---|
| run.py | RC=0，TOTAL 150，0 溢出 |
| gates.py | 16/16 PASS，FAILURES: none |
| occlusion 真实审计 | 0 flags（RC=0；BOXTITLE 盲区已知，另以 boxtitle 真墨 + PDF 像素复测） |
| creambox（正典，md5 ee7a55d8…） | 31 框 OWN 真墨余量全正，最小 +2.1；0 溢出 |
| creambox spill sweep | 5 处 below-window 负值均为已知下块标题假阳性（owner-rect=NONE，与修前同）；6 处 desc-clear 负值（−0.3…−1.1）均为已知无降部误报，真墨复测墨余 +4.8–5.4 |
| p8 extract / compare | 150/150；CLEAN，keydiff [137, 138]（预期） |
| keycheck | 149/150，仅 Q150 例外（开放写作题，提取为 `✓`） |
| freeze（核心对照 `--build` core-pt） | 8/8 byte-identical；核心哈希与修前一致，核心完整性无改动 |
| freeze（版内基线，补充） | 8/8 byte-identical |
| freeze diff | 新增 CJK 9 个，全部 U+3000（P1: 2，其余每页 1） |
| 印/网文字层 | pdftotext -layout 逐字节一致（111,358 B）；fitz 逐页 8/8 一致；check_final 词数印 8,435 = 网 8,435（修前 8,436，差 1 为标题删去的 `In` 一词），multiset diff 0；斜体 span 印 1 = 网 1（`« consciência »`） |
| 网 PDF scratch 重渲比对 | `web-rerender.pdf` 与交付网 PDF 文字层 8/8 一致；SHA 浮动（重渲 be50b91a… vs 交付 2cad3d1b…，预期现象）；交付网 PDF 未被 scratch 文件覆盖 |
| check_s11（pt 适配版，见 GATE-LOG §8 说明） | ALL PASS（色集 21=21、三徽章色齐全、P8 SVG 最小字号 13.0 单位、P8 芯片数/色与核心一致 35、题号齐全、`ESCREVA VOCÊ` 在位） |
| verify_ed（pt 适配版） | ALL PASS（23/23：D4 源+SVG+双法、E1/E2、D1/D2/D3 源+实测、Q137/138/150、text.md 不变、两 PDF 各 8 页） |
| P8 最小字号 | 9.75pt（n=380），低于 9.75pt 者 0 |
| 全版盒标题横向真墨重扫 | 0 溢出（31 框；最紧 E1 +0.5、E2 +1.5、其余 ≥+22.5） |
| 孤儿标点全版重扫 | 0 处（1,637 行） |
| 8 页逐页目视（印 PDF 130dpi + P1 300dpi 裁图） | 无新缺陷；所见均为已知接受项（O4 `Kasten.` 孤字 P3/P5、`B AS PALAVRAS` 栏目标题落栏底、P2/P5 中部版式留白） |

## §8 说明与未决

1. **registry**：pt 系 run.py 不写 `registry.json`（核实：core-pt/pt-de 均无此文件，
   run.py/bslib4.py 内无 `registry.json` 引用；该文件只存在于 en 系版本）。
   本次“registry 重 dump”执行为 pt 系等价物并留檔：`p8-extract.json`（150 键登记）、
   `keycheck-150.json`（149/150）、`de-gates.json`（本 scratch 内全部门禁汇总）。
2. **check_s11.py / verify_ed.py**：pt 系无此二脚本的现成版本（proof1/proof2 scratch
   均无；现存副本均为 en 系，硬编码 core-en/en slug/en 内容检查如 Ashes/Q39，
   无法在 pt-de 上运行）。本次在自家 scratch 写了 pt 适配版
   （`check_s11_pt.py`、`verify_ed_pt.py`，en 原版未动），按 `de` 运行，全部通过
   （见 GATE-LOG §8；适配差异：P8 芯片以数量+颜色对核心为准——4 处 y 位移为德语
   排版流所致且 P8 SVG 与修前基线逐字节一致，属修前既有；P8 题号以 `NNN.` 文本元
   素核查——pt 系不渲染 en 式 `(NNN)` 空白）。
3. **occlusion 盲区**：BOXTITLE 检查不覆盖无描边奶油框（D4 因此漏网），本次验收
   不依赖 occlusion，改以 boxtitle 真墨 + PDF 像素双法复测；工具改进建议沿用 proof2
   的（属工具改进，不在本版定稿条件内）。
4. 未 commit、未 push；收工 HEAD 仍为 `c0382fa7`；core-pt 未动。
