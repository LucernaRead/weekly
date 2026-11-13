# FIX-LOG — W47 zh-cn-it fix1（proof1 D-01～D-05）

- 修复员：fix1。对象：`production/2026-w47/2026-w47-zh-cn-it/`（只改这一版；
  核心 `core-zh-cn/` 与其他版未碰；未 commit、未 push）。
- 开工：2026-11-11 13:41 EST。工作目录：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-cn-it1/`
  （`rebuild/` 为 scratch 副本，`gates-edition/` 为门禁专用副本）。
- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功
  （`e69de29b…`）；scratch 真实写盘成功（`probe.txt`）；df 55G 空闲。
- 任务书澄清：首句 "zh-cn-es…不，是 zh-cn-it" 中的 zh-cn-es 为笔误，
  对象为 zh-cn-it（SHA 与简报一致，已核验）。

## 身份（开工三 SHA，与任务书逐字一致）

| 文件 | 开工字节 | 开工 SHA-256 |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-IT.pdf` | 41,730,134 | `d1ae6f877573b068e757e12b69a9dcb67dd8fd5242e02d5c10b17b95fd52a001` |
| 网页 PDF `Lucerna-VOL4-IT-web.pdf` | 2,641,804 | `75dec91ac806b884bdd4b7cdbdccc39e2c445ff7f668d24ff4365f21f233a512` |
| 文本 `2026-w47-zh-cn-it.text.md` | 50,958 | `f954151fb204030d9d273e0f0032d9674509fd9bb170c7fc460c062eec46ecc4` |

开工快照 `snapshot-start.txt`（39 个非 `__pycache__` 文件）。

## 身份（修后三 SHA，生产盘上实测）

| 文件 | 修后字节 | 修后 SHA-256 |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-IT.pdf` | **41,730,133** | **`440490c4a389e22edc2c93f5b99fdb5bec857dafceeb1256e0f3af007598a69d`** |
| 网页 PDF `Lucerna-VOL4-IT-web.pdf` | 2,641,804（未变） | `75dec91ac806b884bdd4b7cdbdccc39e2c445ff7f668d24ff4365f21f233a512`（未变） |
| 文本 `2026-w47-zh-cn-it.text.md` | **50,916** | **`afc9b2c02a319ab1d20227d3c0826942fc969aa577f61caea56b3845d664544f`** |

旧 SHA 保留在 KIT `## Fix round 1` 一节。网 PDF 按要求未重建（入仓前全家统一重建）。

## 缺陷与修复（全部左锚定 `anchor="start"`，已逐项核对源码；缩短有效）

| 项 | 位置 / 源码 | 改前措辞 | 改后措辞 | PIL 真墨（墨右 / 盒右 / 余量）改前 → 改后 | 交付印 PDF 渲染像素（110 dpi，墨右 / 余量）改前 → 改后 |
|---|---|---|---|---|---|
| D-01（中） | P1 数字框标题 / `content12.py:47` | `数字看本周　Questa settimana in numeri` | `数字看本周　Questa settimana` | 1007.5 / 961.0 / **−46.5** → 893.5 / 961.0 / **+67.5** | 1007.7 / −46.7 → 893.4 / **+67.6** |
| D-02（中） | P5 高频词盒标题 / `content56.py:25` | `这一周的高频词　Parole della settimana` | `这一周的高频词　Parole chiave` | 994.5 / 961.0 / **−33.5** → 892.5 / 961.0 / **+68.5** | 994.6 / −33.6 → 892.6 / **+68.4** |
| D-03（中） | P1 截止线 / `content12.py:88`（:86 长段落未动） | `Chiusura: 10 nov. — la finale non ancora giocata` | `Chiusura: 10 nov. — la finale non giocata` | 1880.5 / 1862.0 / **−18.5** → 1815.5 / 1862.0 / **+46.5** | 1881.9 / −19.9 → 1815.6 / **+46.4** |
| D-04（中） | P2 日历标题 / `content12.py:187` | `本周生活小日历　Date della settimana` | `本周生活小日历　Date utili` | 1424.0 / 1411.5 / **−12.5** → 1294.0 / 1411.5 / **+117.5** | 1423.9 / −12.4 → 1293.0 / **+118.5** |
| D-05（轻） | P1 数字框第 3 项 / `content12.py:50` | `21 nov., sabato — esce il nuovo film 《试探》`（折行，`》` 独占行首） | `21 nov., sabato — esce il film 《试探》`（单行，wrap 宽 342.7 ≤ 内宽 386.5） | wrap 2 行收尾孤儿 `》`（556.5, 1366.3）→ 单行 `21 nov., sabato — esce il film 《试探》`（y=1339.3），孤儿 `》` 元素 0 | 孤儿行有墨 → 孤儿行无墨，条目行有墨 |

- 改前值全部自己重测，与 proof1 分毫不差（D-01 1007.5、D-02 994.5、D-03 1880.5、
  D-04 advance 1424.3、D-05 孤儿位置 556.5/1366.3）；候选措辞先算 PIL 再动手，
  备选 `finale non ancora giocata`（删 `la `，仅余 +1.5 px）已弃用。
- D-04 以盒右缘 1411.5 为准（builder #3 只量了照片 1439.5 的错误边界已纠正）。
- 事实不变：D-05 删 `nuovo `（`esce` 已含"新出"；日期、星期六、片名全留）；
  D-03 删 `ancora `（截稿时决赛未打的事实不变）；其余只缩意大利语尾。
  P7 的 `Parole della settimana:` 词汇表头是另一元素，未动（见 GATE-LOG）。

## 过程事故（已恢复、已验证，如实记录）

- 第一次 scratch `run.py` 运行时，`content*.py:6` 的 `OUT` 是写死的生产绝对路径
  （`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-it/svg`），
  重建的 8 张 SVG 写进了生产（日志重定向本身在 scratch，是对的；构建输出不是）。
  当时生产 p1/p2/p5 被改写（其余 5 张字节一致），其余生产文件未动。
- 发现：重建 SVG 时间戳未更新 + 仍是旧串 → 查 `Page.save`/`OUT` 定位原因 →
  生产快照比对确认仅 3 张 SVG 被改。
- 恢复：用 rsync 副本里的原始 SVG（SHA 与开工快照一致）拷回生产 p1/p2/p5，
  全树比对 `snapshot-restored.txt` == `snapshot-start.txt`（39/39 文件），
  `__pycache__` 未变（`PYTHONDONTWRITEBYTECODE=1` 全程）。
- 此后：scratch 副本 5 个 `content*.py` 的 `OUT` 改指 `rebuild/svg`，
  重跑 `run.py`（RC=0，TOTAL 150）——3 张新 SVG 的 SHA 与事故那次逐字节相同
  （c5fc85af… / e9103b1b… / b1272c96…），证明构建确定、事故产物与正式产物同一批字节。
  生产源码的 `OUT` 保持原样（同步时只带 5 行修复，不带 scratch 的 `OUT` 改动）。
- 教训：以后凡跑 `run.py`/`render.py`，先读 `OUT`/`BASE` 的写盘目标；
  本版 content 与 render 均系硬编码生产路径，scratch 重建必须先改副本内的指向。

## 同步进生产（11 个文件，别无其他）

开工快照 → 收工快照 diff，恰好 11 个文件变化：

| 文件 | 变化 |
|---|---|
| `content12.py` | 4 行（:47、:50、:88、:187；`OUT` 行未变） |
| `content56.py` | 1 行（:25；`OUT` 行未变） |
| `svg/p1-touiban.svg` | c5fc85afef8d6e743389d59409fbf0c2752d664149f5cb70c2b3fe21cb0f586a |
| `svg/p2-shenghuo.svg` | e9103b1ba20b49e23879f66cdb9b62f43ed0a14e15475406dfe221108f042a92 |
| `svg/p5-qingnian.svg` | b1272c9630f1e9c8ffca069eff8ac1a38e7c49164de0265cae1184266f90a941 |
| `cards/p1-touiban.png` | 随 SVG 重渲（其余 5 张卡片字节一致，未动） |
| `cards/p2-shenghuo.png` | 同上 |
| `cards/p5-qingnian.png` | 同上 |
| `Lucerna-VOL4-IT.pdf` | 41,730,133 B，440490c4…（见上表） |
| `2026-w47-zh-cn-it.text.md` | 50,916 B，afc9b2c0…（diff 恰好 5 行） |
| `WEEKLY-KIT.md` | 新 SHA + `## Fix round 1` 章节，旧 SHA 保留 |

未动：网 PDF、ABSTRACT.txt、其余 .py、其余 SVG/卡片、render.py、核心与其他版。
未 commit、未 push。

## SVG 变化页清单

p1-touiban、p2-shenghuo、p5-qingnian 变化；p3-wenhua、p4-tiyu、p6-shendu、
p7-ciyu、p8-ceyan 与生产原版字节一致。
