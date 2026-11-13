探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功（`e69de29…`）+ scratch 真实写盘 `probe-fix-zh-cn-ko1.txt` 成功；磁盘 58G 空闲。｜新三 SHA：印 `69744432ab7424ee8b1e8553d1e75e49c1601c34583e91a277bdb1030593ff30`（36,966,247 B）／网 `bbf0d14d05f2daab9437373b9082e127993dd7eb39eafd023efd60785d7fe02a`（2,817,987 B）／文 `eb5fdedda37c2b9feec54c8b89098e1eeaff4f8760a3038507c728013b3063c0`（52,725 B）。｜D-01 修后三法：PIL 真墨墨右 929.5、余 +31.5 px；交付印 PDF 渲染像素墨右 922.9 svg 单位、余 +38.1；PDF 文字层韩文 run 止于 925.4 svg 单位、余 +35.6。｜门禁：11/11 ALL PASS；freeze 8/8；Hanzi-added 0（8 页全过）；p8 extract 150/150；p8 compare CLEAN，keydiff []（实测）。

# FIX-LOG — W47 zh-cn-ko fix round 1 (D-01 only)

## 缺陷与修法

- **D-01（proof1 (b)，2b33204e）**：P5 高频词盒标题 `这一周的高频词　이번 주 자주 나오는 단어` 越出奶油盒右缘。盒 `x=538.5 y=618.32 w=422.5 h=168.0`，盒右 961.0；标题 `x=556.5 y=655.32`，23pt bold，Noto Sans CJK SC。修前三法：PIL 真墨 advance 421.3、墨右 977.5、越 16.5 px；交付印 PDF 渲染像素墨右 969.6、超 9.6 svg 单位；PDF 文字层韩文 run 止于 972.9 svg 单位、超 11.9。
- **修法（fixer 定）**：缩短韩文 gloss，中文半句不动。`content56.py:25`：
  - 旧：`f.box("这一周的高频词　이번 주 자주 나오는 단어", [`
  - 新：`f.box("这一周的高频词　이번 주 고빈도 단어", [`
  - 选 `고빈도 단어`（“高频词”的直译，韩语语言教育常用术语）而非 `핵심 단어`／`주요 단어`——保义优先；`이번 주 자주 나온 단어` 仅余 +4.5 px，未达 ≥+5 px 自定门槛，弃用。候选实测（PIL，23pt Bold）：`자주 나온` +4.5；`핵심 단어` +53.5；`주요 단어` +53.5；`고빈도 단어` +31.5；核心对照 `Words of the week` +12.5。
- 未动：Q 键、其他页、其他版、核心；未 commit、未 push。

## 修后三法重测（新交付件，2026-11-11）

| 方法 | 修前 | 修后 | 余量 | 结论 |
|---|---|---|---|---|
| PIL 真墨（Noto Sans CJK SC Bold 23pt，与构建同字体；以新 p5 SVG 内实际标题串为准） | advance 421.3，墨右 977.5，越 16.5 px | advance 372.6，墨右 929.5 | **+31.5 px** | 过 |
| 交付印 PDF 渲染像素（150 dpi，`render-p5-150-fix1.png`；奶油右缘实测 960.0 svg 单位，与盒右 961.0 差 1 单位舍入，同 proof1 口径） | 墨右 969.6，超 9.6 | 墨右 922.9 | **+38.1 svg 单位** | 过 |
| PDF 文字层（PyMuPDF，页宽 1462.5 pt → svg 单位 ×4/3；韩文 run） | 止于 972.9，超 11.9 | 止于 925.4（中文 run 止于 717.5） | **+35.6 svg 单位** | 过 |

- 三法余量均 ≥ +5 px（最低 +31.5）。渲染像素与文字层墨右略小于 PIL 真墨（-6.6／-4.1），与修前同向偏差一致（修前渲染 -7.9、文字层 -4.6），为光栅化／字形取整口径差，非新问题。
- 目视：`crop-p5-head-fix1.png`（新印 PDF 150 dpi 裁图，2×）——标题完整落在奶油盒内，右缘留白清晰；盒内两行 20pt 正文亦在框内。
- 测量脚本：`measure_d01_fix1.py`（PIL）+ 向量化重跑（numpy，直接读已渲染 PNG）；首版逐像素扫描在高负载下过慢被杀，改向量化后秒出——渲染 PNG 本身是同一份，未重渲。

## 重建与验证

- **Scratch 重建**：整版目录拷至 `scratch-fix-zh-cn-ko1/build/`，仅改拷贝内 5 个 `content*.py` 的 `OUT` 为 scratch 绝对路径（生产 `OUT` 未动；`~/…` 形式 sed 误写风险见 proof1 O-2，本次先验路径再跑）。`run.py` RC=0，TOTAL 150（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38），0 FLOW OVERFLOW，0 HEAD TOO WIDE；P7 teaser 2531.76；P8 keys 2475.7——与修前逐值一致。
- **SVG 变化页清单（仅 p5）**：重建 8 SVG 与生产对照——p1/p2/p3/p4/p6/p7/p8 逐字节一致，仅 `p5-qingnian.svg` 不同；断言验证 `rebuild == prod.replace(old, new, 1)` 为真（单串替换，文件 -7 B；新 SHA `9f22432094129549f127da31d2fc801c9395891800a36125aabec6ea6be0bd26`，1,076,839 B）。随后仅该文件拷回生产 `svg/`。
- **text.md 重生成 knock-on**：先试 core-ko 的 `textmd.py`——导出的不是本版格式（406 项、U+3000 变半角空格、无 P8 键行，27,679 B），未采用；改用 zh-cn 家族正确导出器 `scratch-fanout-zh-cn/export_ed.py`（stub 记录运行时字符串），先写 scratch 再 diff：在版 text.md 仅差标题 1 行（`915c915`），随即拷回生产。52,732 → 52,725 B（-7）。
- **印 PDF**：`render.py`（BASE 即生产目录，交付路径）RC=0，cards 重渲；36,966,399 → 36,966,247 B（-152）。
- **网 PDF**：`tools/webpdf.py svg/ Lucerna-VOL4-KO-web.pdf`（默认 1400 px）RC=0；2,818,175 → 2,817,987 B（-188）；1072 distinct chars、字体子集字节与修前逐值一致；pdftotext 46,012 B（修前 46,019，-7 = 标题串字节差）。
- **生产状态核对**：修前快照 `sha-pre-fix.txt` 复核——仅 4 文件变（p5 SVG、印 PDF、网 PDF、text.md），其余 7 SVG 与修前逐字节一致；旧串 `자주 나오는 단어` 在 content56.py／p5 SVG／text.md 中计数均为 0。

## 门禁逐项（重建后最终件）

- `gates-zhcn.py`（proof1 脚本拷至本 scratch，仅改 SCRATCH 指向）：**11/11 ALL PASS**——occlusion 0 flags（selftest OK）；img_overlap 0；p8 extract 150/150；p8 compare CLEAN（keydiffs 0）；freeze_sha256 8/8；print/web text 8/8 页 posdiff 0 msdiff 0（P1 253、P2 263、P3 205、P4 263、P5 208、P6 229、P7 280、P8 998，与修前一致）；pdftotext 46,012 B both；P8 answer-zone min 9.98 pt（≥9.75）；P8 chips A2 11 / B1 24 / B2 3 = core；U+2019 0；§1.1 SVG audit clean（paper #fbfaf6 ×8，VOL.5 = core 1）。日志 `gates-fix1.log`，JSON `gates-ko.json`。
- `freeze.py diff --strict-cjk`：TOTAL **4038**（修前 4040；仅 p5 221 → 219，-2 = 本次韩文净变：去 `자주 나오는` 5 音节、加 `고빈도` 3 音节；其余 7 页逐值不变），rc=1 仅因此项——预期、已裁定（解释层 Hangul；见 KIT 裁定）。
- `freeze.py baseline`（core）：**8/8 SVGs byte-identical**，core integrity 确认（`freeze-baseline-fix1.log`）。
- Hanzi-added 核算（`hanzi_ko.py`，与 freeze 同口径 multiset，只计 U+4E00–U+9FFF）：**added Hanzi = 0，8 页全过**（p1 739→725，p2 913→909，p3 752→748，p4 647→643，p5 802→798，p6 787→783，p7 618→612，p8 962→944，与修前逐值一致）。
- p8 extract **150/150**；p8 compare **CLEAN**；**keydiff 实测 []**——任务书预期 [137,138,139,140] 未出现，与 proof1 O-3 一致（E 组 137–140 键为中文句，与核心逐字一致，无需译成读者语）；以盘上实测为准。
- `run.py` 0 溢出（见上）；P8 keys flow 终值 2475.7 不变。

## 三 SHA（新／旧）

| 件 | 新字节 | 新 SHA-256 | 旧字节 | 旧 SHA-256 |
|---|---|---|---|---|
| 印 `Lucerna-VOL4-KO.pdf` | 36,966,247 | `69744432ab7424ee8b1e8553d1e75e49c1601c34583e91a277bdb1030593ff30` | 36,966,399 | `7a664d88cd6f129463c2a9d5a8946c54b5db3c8f45a95aab27bf20300509a3ce` |
| 网 `Lucerna-VOL4-KO-web.pdf` | 2,817,987 | `bbf0d14d05f2daab9437373b9082e127993dd7eb39eafd023efd60785d7fe02a` | 2,818,175 | `64085a3e92316c72a20c63f0dd5f294ce22e2db6d919be61069660881390cdcc` |
| 文 `2026-w47-zh-cn-ko.text.md` | 52,725 | `eb5fdedda37c2b9feec54c8b89098e1eeaff4f8760a3038507c728013b3063c0` | 52,732 | `cce71e996d494135c6c82f1f744676186119b46d8f46737112ac920a1947c904` |

## 改动文件清单（生产目录内）

- `content56.py:25`（标题串 1 行）
- `svg/p5-qingnian.svg`（单串替换；其余 7 SVG 未动）
- `2026-w47-zh-cn-ko.text.md`（标题 1 行）
- `Lucerna-VOL4-KO.pdf`、`Lucerna-VOL4-KO-web.pdf`（同步重建）
- `WEEKLY-KIT.md`（Fix round 1 一节 + 新三 SHA，旧 SHA 保留）
- `cards/p5-qingnian.png`（render.py 重渲的渲染缓存；其余 7 张卡片由未变的 SVG 确定性重渲，未逐字节核对修前卡片——修前未留卡片 SHA）

## 工作目录与证据

- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-cn-ko1/`——`probe-fix-zh-cn-ko1.txt`、`sha-pre-fix.txt`、`run-rebuild-fix1.log`、`export-fix1.log`、`render-fix1.log`、`webpdf-fix1.log`、`gates-fix1.log`、`gates-ko.json`、`freeze-diff-fix1.log`、`freeze-baseline-fix1.log`、`freeze-baseline-fix1.json`、`hanzi-fix1.log`、`measure-d01-fix1.json`、`measure_d01_fix1.py`、`render-p5-150-fix1.png`、`crop-p5-head-fix1.png`、`build/`（重建拷贝）、`textmd.py`（误用的 core-ko 导出器，仅作对照）、`export_ed.py`（实际用导出器，OUT 已改 scratch）、`2026-w47-zh-cn-ko.text.md.new`（误用导出器产物，未采用）、`2026-w47-zh-cn-ko.text.md.new2`（已采用的导出结果）。
- `PYTHONDONTWRITEBYTECODE=1` 全程；`TMPDIR` 一律本 scratch；未 commit、未 push；未碰核心与其他版。
- 待 proof2 复验：D-01 三法 + 11 门（本 FIX-LOG 所载均为 fixer 自测值）。
