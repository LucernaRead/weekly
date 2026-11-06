# P8 keydiff 21 项逐项对照（独立重测：tools/p8.py extract，total=150，lines 口径）

真键 = 印刷段在首个 ' — ' 之前的部分；p8.py 提取键在括号分支下会把提示前缀并入键，故提取键差异 ≠ 真键差异。

| 题号 | 核心印刷段 | 本版印刷段 | 真键（核心→本版） | 裁定 |
|---|---|---|---|---|
| 1 | 3 — 文化日在11月3日（周二） | 3 — Der Kulturtag ist am 3. November (Dienstag) | 3 → 3（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 2 | 9 — 读书周到11月9日（周一） | 9 — Die Lesewoche läuft bis zum 9. November (Montag) | 9 → 9（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 5 | 7 — 神户灯光秀从7日（周六）开始 | 7 — Die Beleuchtung in Kobe beginnt am 7. (Samstag) | 7 → 7（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 7 | B — 文化日在11月3日（周二） | B — Der Kulturtag ist am 3. November (Dienstag) | B → B（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 8 | C — 读书周到11月9日（周一） | C — Die Lesewoche läuft bis zum 9. November (Montag) | C → C（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 9 | B — 立冬在11月7日（周六） | B — 立冬 ist am 7. November (Samstag) | B → B（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 29 | A — 文化日在11月3日（周二） | A — Der Kulturtag ist am 3. November (Dienstag) | A → A（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 32 | B — 工艺展到11月8日（周日） | B — Die Ausstellung läuft bis zum 8. November (Sonntag) | B → B（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 65 | A — 万圣节在10月31日（周六） | A — Halloween war am 31. Oktober (Samstag) | A → A（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 69 | C — 横滨中区民祭在11月8日（周日） | C — Bürgerfest Naka, Yokohama, 8. November (Sonntag) | C → C（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 78 | ○ — ハロウィンは10月31日（土） | ○ — Halloween war am 31. Oktober (Samstag) | ○ → ○（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 101 | 27 — 读书周从10月27日（周二）开始 | 27 — Die Lesewoche begann am 27. Oktober (Dienstag) | 27 → 27（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 113 | A — 文化日在11月3日（周二） | A — Der Kulturtag ist am 3. November (Dienstag) | A → A（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 115 | A — 日本大赛第1战在10月24日（周六） | A — Spiel 1 der Japan Series war am 24. Oktober (Samstag) | A → A（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 117 | B — 万圣节在10月31日（周六） | B — Halloween war am 31. Oktober (Samstag) | B → B（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 118 | A — 立冬在11月7日（周六） | A — 立冬 ist am 7. November (Samstag) | A → A（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 137 | 文化日是11月3日。 — 对照第3版 | Der Kulturtag ist am 3. November. — Siehe Seite 3 | 文化日是11月3日。 → Der Kulturtag ist am 3. November.（不同） | 真重定向（E区翻译题答案语言 ZH→DE） |
| 138 | 乱扔垃圾，要罚2,000日元。 — 对照第5版 | Wer Müll wegwirft, zahlt 2.000 Yen Strafe. — Siehe Seite 5 | 乱扔垃圾，要罚2,000日元。 → Wer Müll wegwirft, zahlt 2.000 Yen Strafe.（不同） | 真重定向（E区翻译题答案语言 ZH→DE） |
| 140 | 神戸の紅葉のライトアップを見に行きたいです。 — 对照第6版（神户的灯光秀） | 神戸の紅葉のライトアップを見に行きたいです。 — Siehe Seite 6 (Kobe-Beleuchtung) | 神戸の紅葉のライトアップを見に行きたいです。 → 神戸の紅葉のライトアップを見に行きたいです。（相同） | 提示本地化（键日语原样，提示德化；因括号分支落入 keydiff） |
| 146 | A — 借りられます＝能借（可能形） | A — 借りられます = ausleihen können (Potentialform) | A → A（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |
| 147 | A — 读书周到11月9日（第7版） | A — Die Lesewoche läuft bis zum 9. November (Seite 7) | A → A（相同） | 括号分支伪影（真键不变，提取键因提示译文/括号位置而变） |

合计：21 = 2 真重定向（#137、#138）+ 1 提示本地化落入 keydiff（#140）+ 18 括号分支伪影。
提示本地化总数 2 项：#139（不在 keydiff，因无括号、dash 分支键相等）与 #140（在 keydiff，因括号分支）。
另：#37 不在 keydiff（键 8 相同、提示存在性相同），但其提示本身未翻译，见 REPORT.md 阻塞项 B1。

## P8 全 150 段唯一相同段

| 题号 | 核心 = 本版印刷段 | 说明 |
|---|---|---|
| 37 | 8 — 工艺展到11月8日 | 唯一一段核心与本版逐字相同的 P8 段；中文提示原样残留，未德化（阻塞项 B1）。其余 149 段均已变化且提示为德语（或日语词头+德语释义）。 |
