# PROOF-NOTE — W47 es-it fix1 后独立复校（re-proof，弯撇号专项）

- **版**：2026-W47 es-it（西班牙语正文 + 意大利语讲解）
- **复校员**：独立复校员，与 fix1 agent（6b7c9286）不同人；亦与 proof1 / 前一轮 proof2 不同人
- **探针（开工前通过，失败即停）**：`ls /dev/null` 存在（字符设备）；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；goals 侧真实写文件成功（`probe.txt`，2026-11-11T14:04:25Z）。三者皆通后开工。
- **对象（任务书 SHA 与盘上实测一致；复核前后各测一次，未变）**：`~/workspace/weekly-git/production/2026-w47/2026-w47-es-it/`（未 commit，未 push；`git status` 仅显示该目录未追踪 `??`，无任何修改）
  - 印 `La-Lucerna-VOL4-es-it.pdf` 3,522,764 B，SHA-256 `5af794cbd0454944099ba311597bade7d8eff0b2ede08ee0ba1c14bccd8bcb53`
  - 网 `La-Lucerna-VOL4-es-it-web.pdf` 883,013 B，SHA-256 `eb0b2635dfdd46d8d6bc6a392365c59f2582f906958bd2c6b3dbf12ba7694da1`
  - 文 `2026-w47-es-it.text.md` 45,232 B / 1,806 行，SHA-256 `81f41695cf1aef7e93152aed8c81f958fa43e57c7faada7bfe76284eb9f4f444`
- **本目录前情（重要）**：本 scratch 在我开工前已被前一轮 proof2 agent 使用（12:56–13:20 UTC，针对 fix1 **重建前**的旧 build：印 3,498,553 B / SHA `12e7e081…`）。其 `PROOF-NOTE.md` / `GATE-LOG.md` 原件已原样归档为 `PROOF-NOTE-pre-fix-build.md` / `GATE-LOG-pre-fix-build.md`，未改动；本文件是我针对 fix1 **重建后**新 build 的独立复校记录。另：我复制 gates helper 脚本时覆盖了该轮留下的同名脚本复件（`gates.py` / `creambox.py` / `creambox_diag.py` / `boxtitle_core.py`，现为 fix1 版）；其 GATE-LOG 中已记下原复件 md5，可追溯。
- **复校范围**：text.md 全文 1,806 行通读；150 题逐题三源核对（content 源 / P8 keys / text.md 答案区）+ 逐题对题干核对；8 页印版逐页渲染目视（150 dpi，`renders/p-1.png`～`p-8.png`）+ 网版 P1/P3 渲染目视；全部机械门独立重跑；28 处弯撇号逐处核对（字符、位置、字体、渲染）；C1/C2 回归重测；D5 只记录。
- **生产目录只读**：未改任何生产文件，未 commit、未 push。网 PDF 只在 scratch 里重渲（`renders/web-p1-1.png`、`web-p3-3.png`），绝未覆盖生产目录的网 PDF。

## 结论：(b) 不定稿 — 缺陷 1 项（E1-空隙，12 处）

除 E1-空隙外，本轮未发现影响理解、答案正确性或版面完整性的缺陷；其余全部机械门绿（见 GATE-LOG.md 与下表）。按 repo `AGENTS.md`（定稿须一轮零发现复校），本版在 E1-空隙修复并重渲、从头再校一轮之前不能定稿。

| 门 | 结果 | 证据位置 |
|---|---|---|
| run（scratch 副本） | rc=0，TOTAL 150（A2 50 / B1 72 / B2 28；页 10/18/18/18/18/18/12/38） | `run-copy.log`（副本已清，日志留存） |
| SVG 重建一致性 | 副本重建 8/8 与 shipped 字节一致 | `run-copy.log` 下 `identical` 8 行 |
| occlusion | 0 flags（自检 6 类全触发） | `it-occlusion.log` / `it-occlusion.json` |
| p8 extract | 150/150，[1..150] 连续 | `it-p8-extract.log` |
| p8 compare（vs core-es） | CLEAN，keydiff=[137, 138]（已裁定，见下） | `it-p8-compare.log` |
| freeze baseline | 8/8 OK，core SVG 未变 | `it-freeze.log` |
| freeze diff | CJK 新增 6，全为 U+3000（每页 1 个，P7/P8 为 0） | `it-freeze-diff.log` |
| creambox | 6 处负余量：5 处假阳性 + C1（见下） | `it-creambox.log` |
| creambox_diag | 0 负真墨余量；C1 真墨余量 **+3.8** | `it-creambox-diag.log` |
| boxtitle | 0 溢出，最小余量 +14.4 | `it-boxtitle.log` |
| keycheck | 149/150，仅 #150 ✓ 例外 | `it-keycheck.log` |
| 印/网文字层 | `pdftotext -layout` 逐字节一致，108,653 B | `it-print.txt` / `it-web.txt` |
| P8 最小字号 | 10.125 pt（n=375），<9.75pt 为 0 | `it-minfont.log` |
| sweep（桥接/孤儿/寡行） | 0 / 0 / 0 | `it-sweep.log` |
| 孤儿标点全版扫 | SVG 0，text.md 0 | 本文件 §5 |
| 150 题三源逐题手验 | 150/150 通过 | 本文件 §4 |
| 范文词数 | 97 词（SVG 实数，80–100 内） | 本文件 §4 |
| C1 回归 | 真墨余量 +3.8，非真溢出 | §3 |
| C2 回归 | 已修：`antes del jueves` 0 处，`hasta el jueves 19` 5 处 | §3 |

---

### E1-空隙［本版 · 弯撇号渲染空隙 · 12 处 · (b)］— 弯撇号 U+2019 在 Noto Sans CJK SC 里渲染出整字宽空隙，像错字

**一句话**：fix1 把 28 处意语省音撇号改成弯撇号 U+2019，字符本身改对了；但其中 12 处落在 Noto Sans CJK SC（sans 解说层）里，该字体 U+2019 的 advance 是整整 1 em，渲染出来撇号后跟了一个空格——`l’ anima`、`L’ EDIZIONE`，读者看来就是错字。另 16 处落在 Newsreader（P8 答案键）里，渲染紧密、无空隙。

**独立复测（fix1 的自报只当线索，以下全部是我自己的实测）**：

1. **字体度量（fontTools，我自己测）**：系统字体 `/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc`，SC face 为第 2 个，upm=1000：
   - U+2019 弯撇号 advance **1000 = 1.000 em**；U+0027 直撇号 **278 = 0.278 em**；U+0020 空格 **224 = 0.224 em**；字母 l 284、a 563。
   - 对照：`tools/fonts/Newsreader-Regular.ttf`（upm=2000）：U+2019 **512 = 0.256 em**，U+0027 432 = 0.216 em，空格 487。Newsreader 的弯撇号只比直撇号宽 0.04 em——这就是它渲染紧密的原因。
   - 结论：弯撇号在 sans 里比直撇号宽 **3.6 倍**、比空格本身还宽 4.5 倍；空隙是字体度量决定的，不是渲染器偶然。
2. **28 处逐处按字体归类（SVG `<text>` 元素实测，见 §1 表）**：Noto Sans CJK SC **12 处**（P1 ×1、P2 ×1、P3 ×2、P4 ×1、P5 ×2、P7 ×4、P8 ×1）；Newsreader **16 处**（全在 P8 答案键；fix1 称 15 处是把 147 题的两个弯撇号算成一处，实际元素 15 个、字符 16 个）。
3. **渲染截图目视——12 处 sans 全部逐一裁图判定，有空隙 12/12**（150 dpi 印版渲染，3 倍放大裁图；`crops/` 目录）：
   | # | 页 | 词（渲染实读） | 裁剪图 | 判定 |
   |---|---|---|---|---|
   | 1 | P1 | `L’ EDIZIONE`（刊头配文，16pt） | `crops/new-p1-LEDIZIONE.png` | 有空隙 |
   | 2 | P2 | `l’ articolo`（桥接句，20.5pt） | `crops/new-p2-larticolo.png` | 有空隙 |
   | 3 | P3 | `l’ anima`（gloss 行末，20.5pt） | `crops/new-p3-lanima.png` | 有空隙 |
   | 4 | P3 | `l’ articolo`（桥接句，20.5pt） | `crops/new-p3-larticolo-bridge.png` | 有空隙 |
   | 5 | P4 | `l’ articolo`（桥接句，20.5pt） | `crops/new-p4-larticolo-bridge.png` | 有空隙 |
   | 6 | P5 | `l’ urna.`（gloss 行末，20.5pt） | `crops/new-p5-lurna.png` | 有空隙 |
   | 7 | P5 | `l’ articolo`（桥接句，20.5pt） | `crops/new-p5-larticolo-bridge.png` | 有空隙 |
   | 8 | P7 | `L’ ora`（解说行首，20.5pt） | `crops/new-p7-Lora.png` | 有空隙 |
   | 9 | P7 | `l’ indicativo.`（解说，20.5pt） | `crops/new-p7-lindicativo.png` | 有空隙 |
   | 10 | P7 | `L’ una`（解说，19.5pt） | `crops/new-p7-Luna.png` | 有空隙 |
   | 11 | P7 | `d’ errore,`（例句，19.5pt） | `crops/new-p7-derroire.png` | 有空隙 |
   | 12 | P8 | `un’ unica`（H 组头注，20.5pt） | `crops/new-p8-ununica.png` | 有空隙 |
   - 对照（Newsreader，紧贴无空隙）：P8 147 题 `Dov’è l’urna?` + 146 题 `d’identità`，`crops/new-p8-Dove-lurna-newsreader.png`。
4. **与直撇号版的同区域对照（修前旧 PDF 的同 DPI 渲染，fix1 留存 `scratch-fix-es-it2/old-p1-1.png`、`old-p3-3.png`，与我的新渲染同为 150 dpi、同坐标裁切）**：
   - P1 `L'EDIZIONE`：旧直撇号紧贴；新弯撇号 `L’ EDIZIONE`，撇号后空一整格。`crops/old-p1-LEDIZIONE-straight.png` vs `crops/new-p1-LEDIZIONE.png`。
   - P3 `l'anima`：旧直撇号紧贴（旧版断行不同，词跨两行）；新弯撇号 `l’ anima`，空隙醒目。`crops/old-p3-lanima-straight.png` vs `crops/new-p3-lanima.png`。
5. **墨迹间隙像素实测（150 dpi 渲染，亮度 <128 为墨，词带内墨迹列轮廓；1pt = 2.08px）**：
   - 新印 P1 `L’EDIZIONE`（16pt）：词内最大白空隙 **24px**（≈11.5pt ≈ 0.72 em），其余字母间隙 ≤6px；旧直撇号版最大仅 **6px**。
   - 新印 P3 `l’anima`（20.5pt）：最大白空隙 **28px**（≈13.4pt ≈ 0.66 em），其余 ≤6px；旧直撇号版最大 10px（旧断行所致，仍远小于 28px）。
   - 新**网** P1 / P3：同样 **24px / 28px**——空隙同样在交付的网 PDF 里（网版内嵌同一字体子集），不是印版独有。`crops/web-p1-LEDIZIONE.png`、`crops/web-p3-lanima.png` 目视与印版完全一致。
6. **同类前例**：nl-it proof1（c53043f4）D3——同一字体、同一机制，P7 `un’ antica`、P8 `l’ esercizio` 被判 minor 缺陷，建议改回直撇号。本版是同一缺陷在 12 处的复现，且含刊头 P1，位置更显眼。

**归属**：本版。fix1 的字符替换本身正确（28/28 皆为意语省音，见 §1），缺陷来自字符与字体的组合：弯撇号 + Noto Sans CJK SC 全角 advance。根在字体层（D5，见下），但可见后果落在交付物正文。

**修复建议**：**整批 revert 回直撇号 U+0027**（28 处全改回，直撇号版是 proof1 已通过的形态，渲染紧贴、逐字核实过），重建三件套后从头再校一轮。备注（供协调员裁定，不作为本轮结论）：只 revert 12 处 sans、保留 16 处 Newsreader 弯撇号也能消除全部可见空隙——Newsreader 的 16 处实测紧密；但那样版内同一省音符号出现两种写法，需协调员定。字体层根治（给拉丁解说层换比例西文字体）超出本 fix 范围，属 D5 全周待定项。

---

## §1 28 处弯撇号逐处核对（字符正确，位置正确）

**内容源逐字符计数**（`content*.py` 实测）：content12.py 弯 2 / 直 0；content34.py 弯 5 / 直 0；content56.py 弯 6 / 直 0；content7.py 弯 6 / 直 0；content8.py 弯 9 / 直 10。合计弯 **28**，与任务书一致。

28 处逐处（源行 + 词 + SVG 落点 + 字体；全部为意语省音、全部在双引号字符串内）：

| # | 内容源 | 词 | SVG 落点 | 字体 / 字号 |
|---|---|---|---|---|
| 1 | content12.py:21 | L’EDIZIONE | P1 x=650.9 y=614 | sans 16 |
| 2 | content12.py:275 | l’articolo | P2 x=538.5 y=2559.7 | sans 20.5 |
| 3 | content34.py:22 | l’anima | P3 x=556.5 y=327.7 | sans 20.5 |
| 4 | content34.py:61 | l’articolo | P3 x=88.0 y=1747.5 | sans 20.5 |
| 5 | content34.py:87 | L’UNESCO | P8 key 39 x=538.5 y=1406.2 | Newsreader 13.5 |
| 6 | content34.py:93 | l’elezione | P8 key 42 x=538.5 y=1495.1 | Newsreader 13.5 |
| 7 | content34.py:168 | l’articolo | P4 x=88.0 y=1707.5 | sans 20.5 |
| 8 | content56.py:29 | l’urna | P5 x=556.5 y=962.1 | sans 20.5 |
| 9 | content56.py:66 | l’articolo | P5 x=88.0 y=1747.5 | sans 20.5 |
| 10 | content56.py:86 | d’identità | P8 key 73 x=538.5 y=2494.7 | Newsreader 13.5 |
| 11 | content56.py:107 | Quest’anno | P8 key 82 x=989.0 y=1554.5 | Newsreader 13.5 |
| 12 | content56.py:218 | d’errore | P8 key 92 x=989.0 y=1883.3 | Newsreader 13.5 |
| 13 | content56.py:237 | d’errore | P8 key 100 x=989.0 y=2120.6 | Newsreader 13.5 |
| 14 | content7.py:20 | L’ora | P7 x=88.0 y=594.9 | sans 20.5 |
| 15 | content7.py:21 | l’una | P8 key 101 x=989.0 y=2182.5 | Newsreader 13.5 |
| 16 | content7.py:27 | L’una | P8 key 104 x=989.0 y=2271.5 | Newsreader 13.5 |
| 17 | content7.py:52 | l’indicativo | P7 x=989.0 y=624.7 | sans 20.5 |
| 18 | content7.py:69 | L’una | P7 x=1461.5 y=608.6 | sans 19.5 |
| 19 | content7.py:124 | d’errore | P7 x=989.0 y=2421.2 | sans 19.5 |
| 20 | content8.py:44 | l’app | P8 key 126 x=1439.5 y=1762.1 | Newsreader 13.5 |
| 21 | content8.py:67 | all’inizio | P8 key 136 x=1439.5 y=2058.7 | Newsreader 13.5 |
| 22 | content8.py:70 | l’originale | P8 key 137 x=1439.5 y=2104.0 | Newsreader 13.5 |
| 23 | content8.py:72 | l’originale | P8 key 138 x=1439.5 y=2133.7 | Newsreader 13.5 |
| 24 | content8.py:86 | d’errore | P8 key 143 x=1439.5 y=2297.6 | Newsreader 13.5 |
| 25 | content8.py:91 | d’identità | P8 key 146 x=1439.5 y=2386.6 | Newsreader 13.5 |
| 26 | content8.py:93 | Dov’è | P8 key 147 x=1220.6 y=1804.8 | Newsreader 13.5 |
| 27 | content8.py:93 | l’urna | P8 key 147 x=1250.5 y=1804.8 | Newsreader 13.5 |
| 28 | content8.py:100 | un’unica | P8 x=1439.5 y=453.4 | sans 20.5 |

交叉核对：text.md 弯 28 / 直 0；印版 PDF 文字层 `pdftotext -bbox` 含弯撇号的词 **28 个**（与上表一一对应）；网版同。content8.py 残留 10 处直撇号逐处核实，全部为代码引号——L133 `txt = f"{e_['n']}. {e_['key']} — {e_['note']}"`（6 处）、L135 `txt = f"{e_['n']}. ✓ {e_['note']}"`（4 处），皆为 f-string 字典键引号，非正文。fix1 的排除正确。

fix1 改动范围核实：`diff` fix1 留存 `text-md-BEFORE.md` vs 当前 text.md——全部差异仅为 28 处直→弯 + 1 处重排（P3 gloss：旧 452–453 行 `l'anima / del flamenco.` → 新 `= / l’anima del flamenco.`，同词同序同框）。无任何其他内容改动。fix1 所述两处版式变化属实：P1 刊头配文行 middle-anchored，起始 x 657.5 → 650.9（弯撇号更宽，仍居中，同 y）；其余 SVG 元素与重建前一致（副本重建 8/8 字节一致佐证）。

## §2 p8 compare keydiff [137, 138] 裁定（与 proof1 同结论，重测通过）

- **137**：核心键为中文译句（读者语=中文）；本版键 `Lunedì è la Giornata internazionale del flamenco.`——题干 `El lunes es el Día del Flamenco. → ___`（西→意翻译题），键与题干逐句对应，正确。差异纯因读者语不同。
- **138**：同理。核心键中文；本版键 `Sabato guardiamo il derby di Siviglia.`——题干 `El sábado vemos el derbi Sevilla–Betis. → ___`，对应正确。
- 其余 148 键与核心逐字节一致。

## §3 C1 / C2 回归重测

- **C1（P1 CINCO CLAVES 工具盒）**：proof1 量的是基线余量 −12.0（盒底 1288.0 vs 基线 1300.0）。核心层已修：KIT 记载该盒高 700→720；我实测盒底 **1308.0**、OWN 末行基线 1300.0（余量 +8.0）、**真墨底 1304.2、真墨余量 +3.8**（`it-creambox-diag.log` P1 第 4 行）。即墨水未漫出盒底；naive creambox 扫出的 −44.0 下方行是下一栏目的标题（owner-rect y=1312），假阳性。C1 按真墨标准已无溢出，不列缺陷。
- **C2（`antes del jueves 19`）**：已修。本版 text.md 中 `antes del jueves` **0 处**，`hasta el jueves 19` **5 处**（P1 正文、图注、题 3、题 116、P8 139 键）；WEEKLY-KIT.md:100 确认核心层共改 `antes del jueves`→`hasta el jueves`。C2 不复现。
- **C3（P5 B 组词框，两词未用、两答案不在框内）**：proof1 结论为核心级且 KIT 记载“left as-is per adjudication”，本轮不重开。

## §4 150 题三源逐题手验（150/150 通过）

方法：text.md 全文 1,806 行通读 + 每题题干对答案键逐题核对（三源：content 源题干 / text.md 答案区 / P8 SVG keys；keycheck 149/150 + p8 extract/compare 机械佐证，#150 ✓ 例外为开放写作题）。

- P1（1–10）：13 / 29 / 19 / 16 / 20 / 15 / C·29日 / B·15天 / A·19日 / B·16日——全对（与头条“13 天”、15 天竞选、19 日截止、16 日弗拉门戈日一致）。
- P2（11–28）：16 / 19 / 29 / 22 / noviembre / empieza / dura / vuelve / recorren / llega / B·16日 / A·19日 / C·20日 / B·24–28 / c·dibattito / b·comizio / d·cartellone / a·seggio——全对。
- P3（29–46）：V / V / F（非仅舞蹈）/ F（圣塞西莉亚 22 日非 16 日）/ V（毕尔巴鄂乐队 22 日 12:00）/ cante / baile / guitarra / palmas / compás / B·Nairobi / A·duende 时刻 / C·Andalucía / B·29 日选举 / 43–46 造句（语序 S-V-O / 时间前置 / 地点前置 / 间接疑问 si）——全对。
- P4（47–64）：A·33 分 / B·20–23 日 / C·18:30 / A·周日 14:00 / B·24–25 日 / c / b / a / d / más importante / muchísimos / peor / mejor / ganó / recibió / perdió / volvió / cerró——全对。
- P5（65–82）：B·19 日 / A·9 日 / C·9:00–20:00 / B·MiDNI / A·27 日 / correo / papeleta / envío / identidad / censo / plazo / Voy a pedir / Vas a votar / Va a abrirse / Van a comparar / V（Correos）/ F（静默日周六 28 非周日 29）/ V（MiDNI）——全对。
- P6（83–100）：A·各 45 分钟 / B·195 分钟（45+45+30+30+15+3×10=195，自洽）/ C·Podemos 15 / A·5 天 / B·15 / C·官方数据+来源 / B·仅 laSexta 已确认 / A·13 日 21:30 / C·提议≠确认 / B·foto con margen d’errore / tenga / sea / para que + subjuntivo / Aunque + 直陈 / sondeo / muestra / indecisos / margen de error——全对。
- P7（101–112）：Es / Son / las / B·Es la una / más goles / tan rápido / mejor / B·más mejor 错 / baje / sea / es / B·tenga——全对（101–104 与 P7 解说“Es la una 单数、Son 复数”一致；111 creo que + 直陈 es；112 ojalá + 虚拟 tenga）。
- P8（113–150）：A·suena / B·empieza / A·21:30 / A·19 日 / A·vuelve / B·周六 / A·músicos / A·vota / A·13 日 / B·16 日 / A·19 日 / C·18:30 / B·27 日 / C·应用 / B·24–28 日 / C·24–25 日 / A·Lucía / A·Diego / A·读纲领 / B·《两城一星期六》/ 133–136 造句 / 137–140 翻译（137/138 见 §2）/ 141 c / 142 d / 143 b / 144 a / A·votar / A·identidad / A·urna / A·sobre / A·cierra / 150 ✓ 范文——全对。
- 范文（H 组）：SVG 实数 **97 词**，在 80–100 词要求内，与版面标注“97 parole”一致。

另：全文通读未发现与 proof1 已核实外部事实矛盾的新表述；未独立锁定的两项沿用 proof1（RTVE 195 分钟逐项第二来源；Sargent 图年份 1880–81 到年精度），不列缺陷。

## §5 其余核查（均有实测）

- **孤儿标点**：SVG `<text>` 元素全扫（纯标点元素、行首闭标点）**0**；text.md 纯标点行 **0**。
- **引号**：弯引号 « » 成对（proof1 已核，本轮 text.md 未见落单；直双引号 0）。
- **禁词/内部语义**：text.md CJK 0 处（除 U+3000 分隔符外，freeze-diff 见 GATE-LOG）；`SOP` / `proofread` / `cover` / 仓库链接等内部词 0。VOL.4 印刷层 9 次 + 刊头 1 次（合法）；VOL.5 3 次均为下期预告（合法）。
- **题量分布**：P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38，合计 150；级别 A2 50 / B1 72 / B2 28（与 run.py REGISTRY 一致）。
- **ABSTRACT.txt**：意大利语单行，无 ASCII 双引号，含刊名、目标语名、A2–B2、150 esercizi 与本期真实主题词（沿用 proof1 结论，重测无变）。
- **日期星期**：沿用 proof1 逐项校验（11 月 9/10/13/16/19/20/21/22/23/24/25/26/27/28/29 日星期全吻合；16 日→29 日 13 天与头条“trece días”一致），本轮通读未见改动。
- **8 页目视**：印版 8 页逐页渲染（`renders/p-1.png`～`p-8.png`），P6 全页目视干净（图表、练习区、页脚均无溢出/重叠）；其余各页以撇号裁图 + creambox/occlusion 机械门覆盖。除 E1-空隙外无新增视觉缺陷。
- **D5 字体（只记录，不判 (b)）**：拉丁讲解层落在 Noto Sans CJK SC，全周级已知待定项。本轮实测字体分布（SVG `<text>` 元素）：Newsreader 973、Noto Sans CJK SC 632、Noto Serif CJK SC 43、UnifrakturMaguntia 1；与前一轮 proof2 实测分布一致。sans 632 段按我的口径：纯拉丁字母段 392、含 U+3000 段 99、仅标点/数字段 141（口径与前一轮不同，其数值为 491/120/21；分布总数一致，仅分类边界不同）。E1-空隙正是 D5 字体问题的可见后果，但 D5 本身仍只记录——(b) 的判定对象是交付物上的 12 处可见空隙（E1-空隙），不是字体选型本身。

## fix1 评价（供协调员参考）

- 字符替换 28/28 全对（逐处是意语省音、无一错改、无一漏改）；代码引号 10 处正确排除；改动范围干净（仅 28 字符 + 1 重排）；全部机械门绿；SHA 链完整。可惜弯撇号与 sans 字体的组合在渲染上翻车——这是字符层修复时未做渲染目视的后果，不是字符判断错。
