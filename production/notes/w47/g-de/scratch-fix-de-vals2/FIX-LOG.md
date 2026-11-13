# FIX-LOG — W47 de 机制表 vals 补值（2 条 EN 值 × 8 语 = 16 值）

日期：2026-11-11（EST 04:57 起）
操作员：de-vals 补值员（subagent）
目录：`hidden_files/w47/scratch-fanout-de/`（8 份 vals_*.json）
Scratch：`hidden_files/w47/scratch-fix-de-vals2/`（备份 `backup/`、验证 `verify/`、临时 `tmp/`、脚本 `insert16.py`、md5 记录 `md5-before.txt` / `md5-after.txt`、live tr md5 `live-tr-md5-before.txt` / `live-tr-md5-after.txt`）
未改任何版文件、未重建、未 commit、不 push、未写盘任何 tr 文件。

## 0. 探针（开工前，均通过）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0
- scratch 目录新建并真实写文件 `tmp/probe.txt`（内容 `probe-write-ok`）
- TMPDIR 全程指向 scratch 内 `tmp/`，未写 /tmp（注：执行时 /tmp 实际仅用 2%，任务所称满未复现，但仍全程遵守）
- 路径说明：任务所称 `production/2026-w47/scratch-fanout-de/` 在本机实际位于
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/`
  （`~/workspace/weekly-git/production/2026-w47/` 下无此目录）；FIX-LOG 亦按此实际路径。
  任务所称 `hidden_files/w47/scratch-fix-de-vals1/` 同为 goals hidden_files 下路径，与上棒一致。

## 1. 动工前验收（上一棒 40648887 的键名修补，通过）

- 旧键 `WEIHNACHTSWÖRTER␣Christmas words`（␣ = U+3000）：8 份合计 **0 处**
- 新键 `WEIHNACHTSWÖRTER␣Words`：8 份合计 **8 处**（每份 1 处）
- 8 份原文件已备份至 scratch `backup/`，md5 与上棒 FIX-LOG §1“改后”逐一核对一致
  （见 `md5-before.txt`；es e2742838…、it 41fe091f…、ja b05fae68…、ko ce4e93e3…、
  nl 53a59e8f…、pt a91d66a9…、ru 4e089434…、zh-tw 6f8d605d…）。

## 2. 关键发现：新 EN 与旧 EN 仅差引号字形，16 值全部复用旧译

以现行 tr_en.py（TR_EN 共 278 条）为准逐字比对（脚本断言）：

| 条 | 新 EN 键（vals["values"] 的键） | 旧 EN 键（vals 中已存在） | 逐字差异 |
|---|---|---|---|
| (a) | `The 1903 calendar: „Im Lande des Christkinds“` | `The 1903 calendar: “Im Lande des Christkinds”` | 仅 2 处引号字形：pos 19 `“`(U+201C)→`„`(U+201E)，pos 44 `”`(U+201D)→`“`(U+201C)；长度同为 45 |
| (b) | `Write in German, 80–100 words: „My week in November“. Say what you make, which games you watch and with whom — and add one sentence about the Buß- und Bettag or Totensonntag.` | 同上文、引号为 `“…”` 的版本 | 仅 2 处引号字形：pos 31 `“`→`„`，pos 51 `”`→`“`；长度同为 174 |

- 两条新 EN 与旧 EN 词句、语义完全相同（仅德式引号 `„…“` 替换英式 `“…”`），故旧译对新 EN 完全贴切，**16 值全部复用旧译、逐字照搬，无一新译**。
- 复用来源经三重核对一致：(i) 各语 vals 旧 EN 键的值；(ii) 现行 tr_&lt;lang&gt;.py 对应中文键的值；(iii) 8 语 × 2 条，`tr == vals-old` 全部 True。
- (b) 措辞复核（Say what you make / which games you watch and with whom / add one sentence about Buß- und Bettag or Totensonntag）：8 语旧译均完整覆盖三要素（手工、比赛+同伴、一句关于两节日的话），无需新译。
- 旧 EN 键保留在 vals 中未删（任务只要求加 16 值；gen_tr.py 只按新 EN 查值，多余旧键无害）。

### 16 值清单（键 = 新 EN 值；值 = 复用旧译；来源：vals 旧 EN 键值 = 现行 tr_&lt;lang&gt;.py 同键值）

(a) 键 `The 1903 calendar: „Im Lande des Christkinds“` —— 8 语值相同，均为
`«Im Lande des Christkinds» (1903)`（复用）。

(b) 键 `Write in German, 80–100 words: „My week in November“. Say what you make, which games you watch and with whom — and add one sentence about the Buß- und Bettag or Totensonntag.`：

| 语 | 值（复用） |
|---|---|
| es | Escribe en alemán, 80–100 palabras: «Mi semana de noviembre». Di qué manualidades haces, qué partidos ves y con quién, y añade una frase sobre el Buß- und Bettag o el Totensonntag. |
| it | Scrivi in tedesco, 80–100 parole: «La mia settimana di novembre». Di' cosa costruisci, quali partite guardi e con chi, e aggiungi una frase sul Buß- und Bettag o il Totensonntag. |
| ja | ドイツ語で80–100語：「11月の私の一週間」。何を作り、誰とどの試合を見るか書き、Buß- und Bettag か Totensonntag について一文加えよう。 |
| ko | 독일어로 80–100단어: 『11월의 나의 한 주』. 무엇을 만들고, 누구와 어떤 경기를 보는지 쓰고, Buß- und Bettag이나 Totensonntag에 대해 한 문장 더하세요. |
| nl | Schrijf in het Duits, 80–100 woorden: «Mijn week in november». Vertel wat je knutselt, welke wedstrijden je kijkt en met wie, en voeg één zin toe over de Buß- und Bettag of Totensonntag. |
| pt | Escreve em alemão, 80–100 palavras: «A minha semana de novembro». Diz o que fazes, que jogos vês e com quem, e acrescenta uma frase sobre o Buß- und Bettag ou o Totensonntag. |
| ru | Напишите по-немецки 80–100 слов: «Моя неделя в ноябре». Расскажите, что вы мастерите, какие матчи смотрите и с кем, и добавьте предложение о Buß- und Bettag или Totensonntag. |
| zh-tw | 用德文寫 80–100 詞：「我十一月的一週」。寫你做了什麼、和誰看哪些比賽，並加一句關於 Buß- und Bettag 或 Totensonntag 的話。 |

## 3. 改动（每份恰 2 条新增键值对，其余一字不动）

- 写法：原始文本插入（脚本 `insert16.py`，在 scratch 内）：在各语旧 EN 键所在行正下方插入
  新键行（2 空格缩进、`json.dumps(..., ensure_ascii=False)` 格式，与文件原有 raw UTF-8、无 `\u` 转义的格式一致）。
- 脚本内断言（全部通过）：改前新键 0 处、旧键各 1 处；改后解析：除 values 外全部字段与改前完全一致；
  values 由 273 → 275 条，仅新增 2 键，旧 273 条值一字不动；新增值 = 旧键值。
- 改后 md5（见 `md5-after.txt`）：es 4a770f40…、it 8991fb55…、ja df81844b…、ko 311e7f41…、
  nl 3ac51839…、pt 49f7d8f3…、ru b99b7001…、zh-tw d500076f…。
- `diff backup/ → 改后`：每份恰 2 行新增（`210a211` / `231a233`；zh-tw 为 `179a180` / `200a202`），无其他任何行差异。
- `python -m json.tool`：8 份全部可解析（OK）。

## 4. 决定性验证（只在 scratch verify/ 内做）—— gen_tr.py 已通过；逐字节比对发现 1 处任务范围外既有漂移，已按指令停下

- 在 scratch `verify/` 内复制 gen_tr.py + tr_en.py + 改后 8 份 vals + 现行 tr_&lt;lang&gt;.py（另存 `verify/orig/` 作比对基准）。
- `python3 gen_tr.py <lang>` 全 8 语：**RC=0**，每语 `wrote …: 278 TR keys, typemap 10, instrmap 5, E 4`
  （上棒 RC=1 的 2 条缺失 EN 值断言已消除；“缺少 EN 值”缺口至此补齐）。
- 生成物与 live tr_&lt;lang&gt;.py 逐字节比对（`cmp` + 逐键解析比对，278 键/语）：

| 语 | 结果 |
|---|---|
| es / it / ja / ko / nl / ru / zh-tw（7 语） | **IDENTICAL，0 差异**（含本次补的 2 条新键，生成值 = 现行值） |
| pt（1 语） | **1 处差异**，与本次补值无关（见下） |

### pt 唯一差异（任务范围外既有漂移，逐项列出）

- 键：`'ist（第三人称单数）'`（verify/tr_pt.py:243）
- 现行 live tr_pt.py：`'ist (3.ª pess. sg.)'`
- verify 内按改后 vals 生成：`'ist (3.ª pers. sg.)'`
- 根因（只读诊断）：现行 vals_pt.json 中 EN 键 `'ist (3rd pers. sg.)'` 的值即为
  `'ist (3.ª pers. sg.)'`；而 live tr_pt.py 记的是 `'pess.'`。注：vals_pt.json 内其余同类
  7 条（bastelt/beginnt/denkt … nach/liest/schaut/schreibt/sieht + `(3rd pers. sg.)`）
  值均为 `'(3.ª pess. sg.)'`，仅 `ist` 一条为 `'pers.'`——vals 内部本身不一致；
  是 vals 后改 / tr_pt.py 曾手改 / 生成时 vals 不同，三者之一造成的既有漂移，无法由本次补值判定。
  本次补的 2 条 pt 新键在生成物与现行文件中完全一致，排除本次改动为成因。

### 停下声明

- 已按任务指令停下：**未修 live tr_pt.py、未改 vals_pt.json 该条、未写盘任何 tr 文件**，
  未 commit、未 push。等协调员裁决该 pt `pess.` / `pers.` 差异（以 vals 为准重生成 tr_pt.py，
  或以 live tr_pt.py 为准改 vals_pt.json）。
- live tr_&lt;lang&gt;.py 生成前后 md5 逐一比对完全一致（`live-tr-md5-before.txt` vs `live-tr-md5-after.txt`，diff 空）——验证过程未触动现行 tr 文件。

## 5. 状态总结

- ✅ 16 值全补：8 份 vals 各 +2 键（values 273 → 275），其余一字不动（diff 每份恰 2 行新增；json.tool 全过）。
- ✅ 16 值来源：全部复用旧译（新 EN 与旧 EN 仅差引号字形 2 处/条，语义相同；复用值与现行 tr 文件逐字一致）。
- ✅ gen_tr.py 全 8 语 RC=0（278 TR keys/语）；上棒 §3 的 2 条缺失断言已消除。
- ⚠️ 逐字节比对：7 语 0 差异；pt 1 处既有漂移（`ist（第三人称单数）`：live `pess.` vs 生成 `pers.`），与本次补值无关，已按指令停下等协调员裁决。
- ⛔ 未修 live 文件、未 commit、未 push。
