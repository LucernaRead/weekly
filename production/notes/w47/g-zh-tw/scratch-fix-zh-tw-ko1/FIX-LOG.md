# FIX-LOG — W47 zh-tw-ko fix1（M1–M5 + D1-韓語，機制層修復）

- **Builder**：fix1（葉子，未再派 subagent）
- **範圍**：只改 `scratch-fanout-zh-tw/tables.py` 的 ko 值 + M1/M2 兩條英文源串。
  未改任何版目錄文件、未碰 core-zh-tw、未碰其他家庭、未碰 tools/、issues/，
  未重建、未跑 insert.py / lint --write、無任何 git 寫操作（僅探針 `git hash-object -w`）。
- **復校對象**：`production/2026-w47/2026-w47-zh-tw-ko/`，PROOF-NOTE 結論 (b)。
- **先讀**：SOP.md §8、§1.1 全文；`weekly-git/AGENTS.md`；協調員 brief；
  `scratch-proof-zh-tw-ko1/PROOF-NOTE.md` 全文；`scratch-fix-zh-tw-it1/FIX-LOG.md`（參照其機制層做法）。

## 探針

- 開工 2026-11-11 ~09:31 UTC：`git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0；
  筆記目錄 `scratch-fix-zh-tw-ko1/probe-fix-zh-tw-ko1.txt` 真實寫盤 rc=0。
- 全程無 EDQUOT；`df`：/home/hatch 150G 總，73G 已用，77G 可用。/tmp 未用。

## 重要前提：表已位移，M4 條目已由他輪先補

- 本輪開工時 tables.py 為 **2474 行、ENTRIES = 242**（it fix1 時 2430 行 / 238 條）。
  任務書給的行號（M1 :2063/:2072、M2 :2128/:2138、M5 :2392）已過期，**全部改動均按內容 grep 重新定位**；
  D1（:254/:276/:331）與 M3（:666）行號未變。以下行號均為改後實測行號。
- **M4 的 4 條 ENTRIES 在本輪開工前已存在**（:1655/:1666/:1677/:1688，9 語齊全；
  it fix1 09:11 時尚缺，是之後另一輪補的，ko 值照抄已發版手寫補丁的正式體）。
  本輪 M4 只改其中 4 條 ko 值的語體，未新增 ENTRIES。
- **「5 條源串」是沿用計數誤差**：6 條答案注只對應 **4 條不同源串**
  （Q98/Q117/Q138 同串 "Xiaoxue is Nov 22."），FANOUT-REPORT/de.md 列 4 條卻寫 5 條。
  實證：scratch-ko vs 已發版 diff（見 GATE-LOG）除本輪 13 行與平行修復外無任何 P8 缺口行，
  即不存在第 5 條缺失源串；Q91 的 "Xiaoxue is Nov 22, the same day."（:1644）早有條目且 ko 已是 해요體。

## 改動清單（共 11 處替換，均在 tables.py）

### D1 韓語 ×3：「다음 주 일요일」→「이번 주 일요일」

| 表行 | 改前（片段） | 改後（片段） |
|---|---|---|
| :254（P1 頭條 gloss） | `…우승 퍼레이드는 다음 주 일요일, 11월 22일 14:00에…` | `…우승 퍼레이드는 이번 주 일요일, 11월 22일 14:00에…` |
| :276（P2 小雪 gloss） | `다음 주 일요일, 11월 22일은 Xiaoxue(소설), …` | `이번 주 일요일, 11월 22일은 Xiaoxue(소설), …` |
| :331（P4 頭條 gloss） | `…우승 퍼레이드는 다음 주 일요일, 11월 22일 14:00에…` | `…우승 퍼레이드는 이번 주 일요일, 11월 22일 14:00에…` |

3 處 ko 值全文其餘一字未動。中文 11 處未碰（隨核心 fix1、重擴帶上）。

### M1（中）：P7 A2 詞表「終點」注音錯

- **源串 :2107** 改前：`Parades give you four useful words: 遊行 (parade), 封王 (clinching the title), 夜間 (night-time) and 終點 (finish line). Learn them once, and every parade makes sense.`
- **源串 :2107** 改後：`Parades give you four useful words: 遊行 (parade), 封王 (clinching the title), 夜間 (night-time) and 終點 (end point). Learn them once, and every parade makes sense.`（只改 `(finish line)` → `(end point)`）
- **ko :2116** 改前：`퍼레이드에서 네 가지 유용한 단어를 배울 수 있어요. 遊行(퍼레이드), 封王(우승 확정), 夜間(밤의), 終點(결승선). 한 번 외우면 어떤 퍼레이드든 이해가 돼요.`
- **ko :2116** 改後：`퍼레이드에서 네 가지 유용한 단어를 배울 수 있어요. 遊行(퍼레이드), 封王(우승 확정), 夜間(밤), 終點(끝나는 곳). 한 번 외우면 어떤 퍼레이드든 이해가 돼요.`
- 一致性佐證：同欄後文（:2138）自釋「終點은 퍼레이드가 끝나는 곳」已是「끝나는 곳」，改後詞表與正文一致。

### M2（中）：P7 B1 記憶法順序反 + 星光大道稱「場所」

- **源串 :2173** 改前：`Memory trick: learn 入圍 first, then the ceremony （頒獎）, then the place it happens （星光大道）.`
- **源串 :2173** 改後：`Memory trick: learn 入圍 first, then 星光大道 (the red carpet at 17:00, before the ceremony), then the ceremony （頒獎） at 18:30.`（照 fr 的順序與措辭邏輯：紅毯 17:00 在前、頒獎 18:30 在後，不稱場所）
- **ko :2182** 改前：`외우는 요령: 먼저 入圍을 외우고, 그다음 시상식（頒獎）, 그다음 열리는 장소（星光大道）를 외워요.`
- **ko :2182** 改後：`외우는 요령: 먼저 入圍을 외우고, 그다음 星光大道(17:00 레드카펫, 시상식 전), 그다음 시상식(頒獎) 18:30을 외워요.`
- 他語值一字未動（見下「M2 另 7 語現值」）。

### M3（低）：P4 U 幣注前綴

- **ko :666** 改前：`참고: 11월 방문은 한 번에 10점(평소에는 5점)을 줘요. 10번 × 10 = 100점, 교환 기준이에요.`
- **ko :666** 改後：`참고｜ 11월 방문은 한 번에 10점(평소에는 5점)을 줘요. 10번 × 10 = 100점, 교환 기준이에요.`
  （只改 `참고:` → `참고｜`；全版其餘 13 處皆用 ｜；驗證：scratch-ko 內 `참고:` 歸零。）

### M4（低）：P8 6 條答案注正式體 → 해요體（4 條目 ko 值）

| 表行 | 源串 | ko 改前 | ko 改後 | 覆蓋 |
|---|---|---|---|---|
| :1664 | `The ceremony is at the Taipei Music Center.`（:1655） | `시상식은 타이베이 음악 센터입니다.` | `시상식은 타이베이 음악 센터예요.` | Q92 content56:178 |
| :1675 | `Xiaoxue is Nov 22.`（:1666） | `샤오쉐는 11월 22일입니다.` | `샤오쉐는 11월 22일이에요.` | Q98 content56:191、Q117 content8:26、Q138 content8:70 |
| :1686 | `Four big events fall on the same Sunday.`（:1677） | `네 가지 큰 행사가 같은 일요일에 열립니다.` | `네 가지 큰 행사가 같은 일요일에 열려요.` | Q100 content56:195 |
| :1697 | `Collecting points is 集點.`（:1688） | `포인트를 모으는 것은 集點입니다.` | `포인트를 모으는 것은 集點이에요.` | Q134 content8:62 |

他語值一字未動。驗證：scratch-ko 5 個 content 文件內 `입니다` 歸零（已發版為 5 處）。

### M5（極微）：P8 第 150 條注 ASCII 連字符

- **ko :2436** 改前：`개방형 과제 - 모범 답안은 위 F란에 실려 있어요 (`
- **ko :2436** 改後：`개방형 과제 — 모범 답안은 위 F란에 실려 있어요 (`
  （只改 ` - ` → ` — `；全表 `개방형 과제 - ` 歸零。）

### D2：不動，等重擴（已核核心 fix2 落地）

- 盤上 core-zh-tw 已無 `BABYMONSTER`（`grep -rn BABYMONSTER content*.py` 0 命中）；
  scratch-ko diff 顯示核心 fix2 完整帶入：P5 香港表行刪除、表框高 480→418、by4 偏移 498→436
  （與 PROOF-NOTE 所述 fix2 做法逐數一致）。本輪未改任何版文件，無需版內修。

## M1 另 8 語現值清單（改前原文，未動，待 sweep）

源串 :2107 所屬條目，ko 以外 8 語現值（均為 "finish line" 式譯法，同錯）：

- **de** :2108：`Paraden geben dir vier nützliche Wörter: 遊行 (Parade), 封王 (Meistertitel sichern), 夜間 (nachts) und 終點 (Ziellinie). Lerne sie einmal, und jede Parade ergibt Sinn.`
- **fr** :2109：`Les défilés vous donnent quatre mots utiles : 遊行 (défilé), 封王 (remporter le titre), 夜間 (de nuit) et 終點 (ligne d'arrivée). Apprenez-les une fois, et chaque défilé devient clair.`
- **es** :2110：`Los desfiles te dan cuatro palabras útiles: 遊行 (desfile), 封王 (conseguir el título), 夜間 (nocturno) y 終點 (meta). Apréndelas una vez y cada desfile tendrá sentido.`
- **it** :2111：`Le parate ti danno quattro parole utili: 遊行 (parata), 封王 (conquistare il titolo), 夜間 (notturno) e 終點 (traguardo). Imparale una volta e ogni parata avrà senso.`
- **pt** :2112：`Os desfiles lhe dão quatro palavras úteis: 遊行 (desfile), 封王 (conquistar o título), 夜間 (noturno) e 終點 (linha de chegada). Aprenda-as uma vez e todo desfile fará sentido.`
- **nl** :2113：`Parades geven je vier handige woorden: 遊行 (parade), 封王 (de titel pakken), 夜間 ('s nachts) en 終點 (finish). Leer ze één keer en elke parade wordt duidelijk.`
- **ru** :2114：`Парады дают четыре полезных слова: 遊行 (парад), 封王 (завоевание титула), 夜間 (ночной) и 終點 (финиш). Выучите их раз — и любой парад станет понятен.`
- **ja** :2115：`パレードからは四つの便利な言葉が学べる。遊行（パレード）、封王（優勝を決める）、夜間（夜の）、終點（ゴール）。一度覚えれば、どのパレードも意味が分かる。`

## M2 另 7 語現值（fr 已正確，未動，待 sweep）

源串 :2173 所屬條目：

- **de**：`Merktipp: Lerne zuerst 入圍 — dann die Zeremonie （頒獎）, dann den Ort, an dem sie stattfindet （星光大道）.`
- **fr**（正確，不動）：`Astuce mémoire : apprenez d'abord 入圍, puis 星光大道 (le tapis rouge à 17:00, avant la cérémonie), puis la cérémonie （頒獎） à 18:30.`
- **es**：`Truco de memoria: aprende primero 入圍, luego la ceremonia （頒獎）, luego el lugar donde ocurre （星光大道）.`
- **it**：`Trucco per ricordare: impara prima 入圍, poi la cerimonia （頒獎）, poi il luogo dove si svolge （星光大道）.`
- **pt**：`Truque de memória: aprenda primeiro 入圍, depois a cerimônia （頒獎）, depois o lugar onde acontece （星光大道）.`
- **nl**：`Geheugensteuntje: leer eerst 入圍, dan de ceremonie （頒獎）, dan de plek waar die plaatsvindt （星光大道）.`
- **ru**：`Приём для памяти: сначала выучите 入圍, потом церемонию （頒獎）, потом место, где она проходит （星光大道）.`
- **ja**：`覚え方のコツ：まず入圍、次に式典（頒獎）、そして行われる場所（星光大道）の順に覚えよう。`

## D1 另 8 語現狀（ko 已修，其餘待 sweep；英文源串仍錯）

3 條英文源串至今仍寫 "next Sunday"，本輪按任務只改 ko，未動源串與他語：

- :245（遊行 P1）：`The Wei Chuan Dragons' championship parade is set for next Sunday (Nov 22) at 14:00, …`
- :267（小雪 P2）：`Next Sunday (Nov 22) is Xiaoxue (Minor Snow), the 20th solar term and the second of winter: …`
- :322（遊行 P4）：`The Wei Chuan Dragons' championship parade is set for next Sunday (Nov 22) at 14:00, …`（+ U-Sport 句）

其餘各語對 "next Sunday" 的譯法（同 3 條目逐條核對）：de `nächsten Sonntag`、fr `dimanche prochain`、
es `el próximo domingo`、it `domenica prossima`、pt `o próximo domingo`、ja `来週の日曜日`——
6 語 × 3 條同錯；**nl 中性**（`op zondag 22 nov.` / `Volgende zondag`：遊行兩條只寫日期無 "next"，
小雪條 `Volgende zondag` 仍錯）；**ru 已是正確寫法**（遊行兩條 `на это воскресенье`、小雪條 `В это воскресенье`）。
Sweep 時源串應同步改為 "this Sunday"，否則 transform 的源串匹配仍以舊串為準（見下「核心對齊」）。

## ⚠ 核心對齊前置條件（重擴前必做，不在本輪權限內）

**M1/M2 的源串一改，transform 即以新源串為匹配鍵；盤上 core-zh-tw 仍是舊串，重擴會直接失敗。**
已在 scratch 實證（見 GATE-LOG §2）：

- 未補 scratch 核心時，ko transform 拋 `AssertionError: 'Parades give you four useful words: … and 終點 (end point). …': found 0 < 1`。
- 機制：`transform.py` 要求每條源串至少匹配 1 次（`expect_min=1`），否則 loud fail。

重擴前，核心 fix3（或協調員指定的人）必須把**同樣的兩處字串改動**做到
`~/workspace/weekly-git/production/2026-w47/core-zh-tw/content7.py`：

- :18 `… and 終點 (finish line). …` → `… and 終點 (end point). …`
- :52 `Memory trick: learn 入圍 first, then the ceremony （頒獎）, then the place it happens （星光大道）.` →
  `Memory trick: learn 入圍 first, then 星光大道 (the red carpet at 17:00, before the ceremony), then the ceremony （頒獎） at 18:30.`

本輪只在 **scratch 核心副本**裡做了這兩處改動以便驗證，未碰真實 core-zh-tw；
scratch 副本驗證後已刪。未做此對齊就重擴，9 語 transform 將在 M1 條目處全數失敗。

## Scratch 驗證（見 GATE-LOG）

- 方法（沿用 it fix1）：筆記目錄 `work/` 內複製 core-zh-tw + 改後 tables.py + transform.py
  （僅 PROD 指針改向 scratch `work/prod`），9 語全部重跑 transform：**9/9 TRANSFORM OK**（各 248 行日誌；
  it fix1 時 244 行，+4 行為他輪補的 M4 4 條目）。
- ko：20 個 hunks 全部分類——D1-core 中文 11 行（平行修復）＋ D1-ko 3 行（本輪）＋ D2（核心 fix2 帶入）
  ＋ 核心另改 1 行（`先選一件，再看轉播——四件事只能取捨`，盤上核心 content56.py:131 已帶，非本輪）＋
  M1 ×1、M2 ×1、M3 ×1、M4 ×6 行、M5 ×1（本輪 13 行）；bslib4.py / render.py / ABSTRACT.txt diff 為空。
- 其餘 8 語：100 個 hunks 全部分類——D1-core、D2、核心另改 + 各語前存平行修復（it D3 ×5、fr Astuce ×1、
  de P7 預告條手修 ×1、ru 措辭漂移 ×5、ja 迪士尼 48 天改寫 ×1）；**本輪改動零波及其他語**。
- 舊串全表歸零：`다음 주 일요일` 0、`finish line` 0、`결승선` 0、`밤의` 0、
  `the place it happens` 0、`열리는 장소` 0、`개방형 과제 - ` 0、`참고: 11월` 0、
  M4 正式體 4 串各 0。`import tables` 成功，ENTRIES = 242。
- 驗證用副本（core 拷貝 33M ＋ 9 版產出約 300M）已刪，只留日誌與 diff 檔
  （`diff-ko.txt`、`diff-others.txt`、`transform-*.log`）。

## 版面影響評估（供隨後重建輪次複核）

- M1 ko：`밤의`→`밤`（-1 字）、`결승선`→`끝나는 곳`（+1 字），淨 +0；M2 ko：舊 52 字 → 新 56 字（+4 字，
  時刻標註 17:00/18:30 佔位）；M3：`:`→`｜`等長；M4：`입니다`→`예요`等長、`열립니다`→`열려요`等長；
  M5：`-`→`—`等長；D1 ko：`다음 주`→`이번 주`等長。均在 P7 A2/B1 欄、P4 注、P8 答案注內，
  無超長風險；P7 欄 3 底距 footer 餘量（PROOF-NOTE 提醒 18.7px）重建輪重跑 occlusion 終驗。
- PROOF-NOTE「低度觀察」1（Méliès 注主語鬆動，:320 ko）與 2（Q72「為夜晚收尾」，ko "트리 점등식이 저녁을 마무리해요"）
  **不在本輪任務範圍，未碰**。

## 未做

- 未碰 D1 中文 11 處（核心 fix1 的事）、未改版目錄任何文件、未碰 core-zh-tw、
  未碰其他家庭、未碰 tools/、issues/；未重建、未跑 insert.py / lint --write；無 commit、無 push。
- 未擅自改 M1/M2/D1 的他語值（只抄錄在 FIX-LOG 供 sweep）。
- 未改 PROOF-NOTE 低度觀察 1/2（範圍外）。

## 待協調員跟進

1. **核心對齊（重擴前置，最高優先）**：core-zh-tw content7.py:18/:52 按上文改兩個源串，否則重擴 9 語 transform 全敗。
2. **M1 的 8 語 sweep**：另派一輪，按本 LOG「M1 另 8 語現值清單」把終點譯法改為遊行路線終點（end point），勿再寫賽跑終點線。
3. **M2 的 7 語 sweep**：de/es/it/pt/nl/ru/ja 按 fr 的順序與措辭邏輯改（fr 已正確，不動）。
4. **D1 的 6 語 sweep**：de/fr/es/it/pt/ja 的 3 條目 "next Sunday" 譯法改為 "this Sunday"；
   英文源串（:245/:267/:322）同步改為 "this Sunday"（否則 transform 源串匹配仍以舊串為準）；
   nl 遊行兩條已中性（只寫日期）不動，但小雪條 `Volgende zondag` 仍錯、須改為 `Deze zondag`；
   ru 三條皆已正確，不動。
5. **ru/ja 表值前存漂移**（非本輪造成，供相關 fix 輪順手核）：ru「巨型皮卡丘氣球」三處
   `шар-Пикачу`→`надувной Пикачу`、兩處 `Диснее`→`Диснейленде`、M1 `Выучите их раз`→`Выучите их один раз`、
   Q134 `集點。`（全角句號）vs 表值 `集點.`（半角句號）；ja 迪士尼 48 天注改寫。
   另 diff 顯示的 ru "н��чинается" 為顯示偽影，已按字節核實 tables.py 含 0 個 U+FFFD，值為正確俄語。

---

# FIX-LOG（續）— W47 zh-tw-ko fix1 第 2 輪：修 proof1 新發現 K1，僅重建 ko 版

- 時間：2026-11-11 12:48–13:05 UTC（接上輪 tables.py 機制修復 + re-fanout 重建之後；proof1 (b) 新發現 K1）
- 工作目錄：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-tw-ko1/`
- 解釋器：全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；未用系統 python3。`TMPDIR=<scratch>/tmp`（/tmp 不用）。
- 依據：`scratch-proof-zh-tw-ko1/PROOF-NOTE.md` §6（K1，5 處、6 個落版點；舊輪 8 缺陷已全部驗證修復）。

## 0. 探針（開工前，兩項皆通過才動手）

- `ls /dev/null` 存在（普通文件，復校輪 touch 恢復的既有狀態，未誤判為配額問題）；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0。
- 真實寫盤：`scratch-fix-zh-tw-ko1/probe.txt` 寫入成功。磁盤：/home/hatch 150G 總，81G 已用，69G 可用。

## 1. 改了什麼

### 1.1 tables.py（共享表 `scratch-fanout-zh-tw/tables.py`，只動 ko 值 4 行）

改前備份：`scratch-fix-zh-tw-ko1/tables.py.bak`，SHA-256 `ab91bb5e162092802fc04cc171f8955e0dd58addd775e5b88e4bb503e8b9b21c`。

| 行 | 舊（錯） | 新（對） |
|---|---|---|
| :1939 | 후보에 오르는 것은 **入圍이에요**. | 후보에 오르는 것은 **入圍예요**. |
| :2171 | **入圍은** 후보에 오르는 것을 뜻해요. | **入圍는** 후보에 오르는 것을 뜻해요. |
| :2171（同行） | **鋼雕은** 강철로 만든 조각이에요. | **鋼雕는** 강철로 만든 조각이에요. |
| :2182 | 먼저 **入圍을** 외우고 | 먼저 **入圍를** 외우고 |
| :2215 | **市集는** 시장이에요. | **市集은** 시장이에요. |

5 處替換各以 count==1 斷言後寫入。`diff tables.py tables.py.bak`：**僅 4 行**（:1939、:2171、:2182、:2215），該行其餘 ko 文一字未動，其他 8 版的任何值一字未動。

### 1.2 重建（只重建 ko 一版）

- 舊版整目錄備份至 `scratch-fix-zh-tw-ko1/old-build/`（30M，21 項；`cp -a` 的 ownership 警告無害），舊 transform-ko.log 保全為 `transform-ko.log.oldbuild`。
- 刪舊目錄後 `transform.py ko`（rc=0，248 行；舊輪 244 行，差 4 行為 K1 新值 + 假 home 路徑行——舊 log 寫的是 fakehome 底本路徑，本輪為真實生產路徑，結果等價）。transform log diff（舊 vs 新）：除路徑行外僅 K1 三行值不同。
- copytree 帶入的核心舊件 3 個（`Lucerna-VOL4.pdf`、`Lucerna-VOL4-web.pdf`、`2026-w47-zh-tw-en.text.md`）經 SHA 驗證與核心逐字相同後刪除。
- 新舊 content diff：**僅 content7.py:43/:44/:52/:60 與 content8.py:58 六處**；bslib4.py、content12/34/56.py、render.py、run.py、checks.py、export_zhtw_textmd.py、svglib.py 皆 0 diff。ABSTRACT.txt 與舊版逐字相同。
- 核心核對（重建前後兩次一致，未變）：印 `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a`（19,420,552 B）、網 `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240`（2,324,042 B）、text `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b`（49,798 B）。其餘 8 版未碰（工作樹內 it-es、fanout-nl 的 `M` 為他人並行改動，與本任務無關、非本人所為）。
- 構建：run.py rc=0（0 FLOW OVERFLOW、0 HEAD TOO WIDE；P7 col3 ends 1821.42、teaser ends 2575.42，與舊版逐值相同；150 題：A2 44 / B1 74 / B2 32）；render.py rc=0；webpdf rc=0；text.md 導出 rc=0。

## 2. 新版三件（SHA + 字節）

| 件 | 字節 | SHA-256 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-KO.pdf` | 16,838,020 | `c04102a9a1ceef1cf25fc7f3df6e69266e5f3d8bb2fec8d4370a3f782217d3a6` |
| 網 PDF `Lucerna-VOL4-KO-web.pdf` | 2,325,041（< 7 MB） | `ed9e11a5c8997eb6b09cd6fd1f9bad6b64d686e2280d4730eac3d48ff65bad61` |
| text.md `2026-w47-zh-tw-ko.text.md` | 53,916 | `2af17f023ab203259aeeb294b04f31e4bbb766398a28ec5f7fd2f163622b06f7` |

舊三件（歷史）：印 16,838,018 B / `75610665146d9903c5144148f799386d2ed928f11264e2a8697cb24429c307f0`；網 2,325,041 B / `140f83acdba99fba9b67ec26f8e1418d85a2e5aa9f791d3f16238265c67bb282`；text.md 53,922 B / `2e7038cc4c1266146824db80b1a20f87f83593b69f3e8bd755596b435e6986a8`。
字節變化說明：text.md −6 B = K1-5「入圍이에요」→「入圍예요」×2 處各 −3 B，其餘 K1 為同長度替換；印 PDF +2 B 為字體子集／編碼重排所致，內容以門禁為準；網 PDF 字節不變、SHA 變（內容已換）。

## 3. 門禁匯總（全綠）

跑法：`gates.py`（自 `scratch-refanout-zh-tw/gates.py` 複製，僅改輸出目錄為本 scratch；gtools 同源）`ko fix1`，輸出 `gates/ko-fix1/gates.json`；freeze diff 與三源 keycheck 另跑。

| 門 | 結果 |
|---|---|
| run.py | rc=0，0 溢出、0 超寬 |
| checks.py（本版自帶） | PASS；8 條金句各 2 次；`SIMP_ONLY_HITS []`；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] |
| occlusion audit | selftest rc=0，flags **0** |
| p8 extract + compare | extract 150/150；compare **CLEAN**（keydiff []、missing []、extra_count 0、uncertain []） |
| freeze baseline（source freeze） | **8/8** 字節一致；核心完整性 OK；P1–P6 SVG SHA 與舊版逐字相同（p1 2f021d71…、p2 050e53b0…、p3 6b01d169…、p4 80d4d8db…、p5 96565ffd…、p6 6301c38d…），僅 P7/P8 變（p7 ba9b4b48→31f7898a…、p8 75eb33e0→a390fcc6…） |
| freeze diff（string freeze） | 逐頁增／刪與舊版相同：p1 +24/−25、p2 +35/−39、p3 +42/−47、p4 +36/−39、p5 +46/−47、p6 +31/−33、p7 +360/−120、p8 +188/−187；新增 CJK 4,690 字（舊版 4,692，−2 恰為 K1-5 兩處 이에요→예요 各少一字；新增皆為韓文音節 + 引用的中文詞） |
| 印／網文字層 | 多重集差分 **0** 字元（print 95,029 B = web 95,029 B）；「本週日」11、「下週日」0、BABYMONSTER 0 |
| PDF 指標（PyMuPDF） | 印、網皆 8 頁、1462.5×2025 pt；最小字號 **9.75pt**（整刊與 P8 皆然）；P1 最大 147.0pt；P8 最大 34.5pt |
| keycheck（三源交叉，復用 proof1 keycheck.py，輸出改至本目錄） | **150/150 一致，mismatches []**；填空鍵 **54/54** 在正文；答案 1–150 連續；SVG/text.md CJK 版獨有 {韓}、核心獨有 {英}；U+0022 0、U+0027 1（`Kanahei's Little Animals` 專名）；寫作範文 142 字（CJK+數字 126，120–180 區間內） |
| creambox（canonical） | 36 盒；負清除 **0**；各頁 inside-only 最小：P1 18.8、P2 41.8、P3 16.1、P4 35.8、P5 6.4、P6 19.9；P7 工具盒 +40.5/+12.5/+14.0（與舊版逐值相同） |
| boxtitle（真墨） | 36 盒，超框 **0**，最小右余 18.5px |
| creambox-pil（真墨） | STRADDLE **0**，CREAM-COVER **0**；P7 最小底清除 10.5px |
| P6 時間軸銜接（真墨） | 18:30「頒獎典禮」墨右緣 990.8 → 19:00「夜間遊行」墨左緣 991.4，墨縫 **0.6px**，與核心先例一致 |
| 英文泄漏掃描 | deny_hits {}（shared_ascii_long 僅「A. 12:00 · B. 14:00 · C. 19:00」時刻串，與核心共有，非散文殘留） |
| 8 頁目視（自印 PDF 渲染，100 dpi，`render/p-1.png` … `p-8.png`） | 8/8 逐版目視：無溢出、無重疊、無裁切、無頁腳碰撞；P5 香港11月節目表末行「迪士尼聖誕音樂會：11月21、22日」，無 BABYMONSTER 行；P7 工具盒／預告條乾淨；P8 答案區完整 |

## 4. K1 六落版點逐一核對表

舊錯形在新版全版（8 個 SVG + text.md）出現 **0** 次；新形各就其位：

| # | 落版點 | 舊（proof1） | 新（本版，實測） | 核對 |
|---|---|---|---|---|
| K1-1 | P7 B1 詞彙釋義，content7.py:43；SVG p7-lang | 入圍**은** … 뜻해요. | 入圍**는** 후보에 오르는 것을 뜻해요. | SVG grep 1 處 ✓；100 dpi 目視 P7 確認 ✓ |
| K1-2 | 同句；content7.py:43；SVG p7-lang | 鋼雕**은** … 조각이에요. | 鋼雕**는** 강철로 만든 조각이에요. | SVG grep 1 處 ✓；目視 P7 確認 ✓ |
| K1-3 | P7 B1 記憶法，content7.py:52；SVG p7-lang | 먼저 入圍**을** 외우고 | 먼저 入圍**를** 외우고 | SVG grep 1 處 ✓；目視 P7 確認 ✓ |
| K1-4 | P7 B2 詞彙釋義，content7.py:60；SVG p7-lang | 市集**는** 시장이에요. | 市集**은** 시장이에요. | SVG grep 1 處 ✓；目視 P7 確認 ✓ |
| K1-5a | P8 Q105 注，content7.py:44；SVG p8-test + text.md 答案區 :6210 | 후보에 오르는 것은 入圍**이에요**. | 후보에 오르는 것은 入圍**예요**. | SVG grep 1 處、text.md 1 處 ✓；目視 P8 答案區確認 ✓ |
| K1-5b | P8 Q132 注，content8.py:58；SVG p8-test + text.md 答案區 :6266 | 同上 | 同上 | SVG grep 1 處、text.md 1 處 ✓；目視 P8 答案區確認 ✓ |

合計：p7-lang.svg 新形各 1 處（入圍는／鋼雕는／入圍를／市集은），p8-test.svg 入圍예요 2 處，text.md 六新形各對應 1–2 處；舊版備份同位置為舊錯形各 1–2 處（對照已驗）。

## 5. 不碰項（已遵守）

- 核心 core-zh-tw 一字未動（重建前後 SHA 復核一致）。
- 其餘 8 版一字未動（tables.py diff 僅 4 行 ko 值）。
- O1–O6 觀察項未修（O3 小雪表記統一未做）；D5 字体全周待定項未碰。

## 6. KIT 與交付

- 該版 `WEEKLY-KIT.md` 已更新：新三件字節 + SHA 寫入正文行，舊值保留為歷史行（未刪）；新增「Fix1 — K1 韓語助詞／繫詞修正」一節。
- **未 commit、未 push**（按任務要求）。新版留在工作樹（`??` 未提交狀態），等 proof1 #2 通過後再隨 bundle 入倉。

## 7. 文件清單（本目錄，本輪新增）

- `FIX-LOG.md`（本文件，續寫）、`probe.txt`、`tables.py.bak`、`transform-ko.log`、`transform-ko.log.oldbuild`、`build-run.log`、`render.log`、`webpdf.log`、`export.log`、`gates.py`、`gtools/`、`keycheck.py`、`keycheck-150.json`、`gates/ko-fix1/gates.json` 及各門日誌、`gates/freeze-diff.json`、`gates/freeze-diff.log`、`gates/keycheck.log`、`old-build/`（舊版整目錄備份）、`render/p-1.png` … `p-8.png`、`tmp/`。
- 註：`gates/freeze-diff.log` 首次寫入因 gates/ 目錄未建而失敗一次（rc=1，僅路徑問題），建目錄後重跑 rc=0；內容無損。

